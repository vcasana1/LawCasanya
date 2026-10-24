%% RAINBOW_REFLECTION_POLYA_AUDIT.m
% Pure MATLAB.
%
% Orthogonal-cubic follow-up audit for the transverse Violet family.
% It performs four checks that are logically distinct:
%   1) direct pointwise mixed-curvature C(alpha,beta) scans for Q_perp;
%   2) reflection-conjugation decomposition u = X + Y with a canonical
%      lobe-wise phase chi chosen at beta=1/2;
%   3) modal phase-locking and corrected adjacent Chebyshev determinants
%         Delta_m = p_m p'_{m+1} - p_{m+1} p'_m;
%   4) finite Polya generating-polynomial root diagnostics.
%
% The supplied ordinates are used only as fixed beta=1/2 lobe boundaries.
% No beta-dependent zeros are introduced or searched.

clear; clc; close all;
rng(20260825,'twister');

SCRIPT_DIR=fileparts(mfilename('fullpath'));
ROOT=fileparts(SCRIPT_DIR);

cfg=struct;
cfg.ZeroFile=fullfile(ROOT,'data','zeross.bin');
cfg.Lobes=[2 8 25];
cfg.Nq=241;
cfg.BetaCount=[11 21 11]; % endpoints later omitted from C summary
cfg.EMOrder=8;
cfg.InitialCutoff=512;
cfg.MaxCutoff=4096;
cfg.EvaluatorTol=2e-9;
cfg.TChunk=700;
cfg.MaxMode=18;
cfg.RootImagTol=1e-8;
cfg.RootRealTol=1e-10;
cfg.SignTol=1e-10;
cfg.OutputDir=fullfile(ROOT,'outputs','reflection_polya');
if ~exist(cfg.OutputDir,'dir'), mkdir(cfg.OutputDir); end

fprintf('\nRAINBOW REFLECTION / POLYA AUDIT\n');
fprintf('============================================================\n');
fprintf('lobes                  : '); fprintf('%d ',cfg.Lobes); fprintf('\n');
fprintf('q samples              : %d\n',cfg.Nq);
fprintf('maximum modal degree   : %d\n',cfg.MaxMode);

%% Fixed lobe boundaries
maxLobe=max(cfg.Lobes);
fid=fopen(cfg.ZeroFile,'rb');
if fid<0, error('Cannot open %s.',cfg.ZeroFile); end
gamma=fread(fid,maxLobe+1,'double'); fclose(fid); gamma=gamma(:);
if numel(gamma)<maxLobe+1, error('Not enough fixed lobe boundaries.'); end

q=linspace(0,1,cfg.Nq).';
wq=trapezoid_weights(q);

%% Weighted orthonormal polynomial basis.
% Start from shifted Legendre columns and re-orthonormalize under the exact
% discrete quadrature used everywhere else in this audit.  The first four
% columns span P_3 exactly on the grid.
Phi=shifted_legendre_basis(q,cfg.MaxMode);
A=sqrt(wq).*Phi;
[Qm,~]=qr(A,0);
Psi=Qm./sqrt(wq);
for j=1:size(Psi,2)
    if real(sum(Psi(:,j).*Phi(:,j).*wq))<0, Psi(:,j)=-Psi(:,j); end
end
Gram=Psi'*(Psi.*wq);
fprintf('weighted modal Gram error = %.3e\n',max(abs(Gram-eye(size(Gram))),[],'all'));

%% Evaluator cutoff audit on all selected lobes.
tAudit=[];
for il=1:numel(cfg.Lobes)
    n=cfg.Lobes(il);
    tg=violet_phase_grid(gamma(n:n+1),q.');
    tAudit=[tAudit tg(1,round(linspace(1,cfg.Nq,9)))]; %#ok<AGROW>
end
betaAudit=[.5;.50001;.51;.75;1];
Ncut=cfg.InitialCutoff;
while true
    [Wa,dWa]=transverse_matrix_with_beta_derivative(betaAudit,tAudit,Ncut,cfg.EMOrder,cfg.TChunk);
    [Wb,dWb]=transverse_matrix_with_beta_derivative(betaAudit,tAudit,2*Ncut,cfg.EMOrder,cfg.TChunk);
    eW=max(abs(Wa(:)-Wb(:))./max(1,abs(Wb(:))));
    eD=max(abs(dWa(:)-dWb(:))./max(1,abs(dWb(:))));
    fprintf('cutoff %d vs %d : W %.3e   W_beta %.3e\n',Ncut,2*Ncut,eW,eD);
    if max(eW,eD)<=cfg.EvaluatorTol, break; end
    Ncut=2*Ncut;
    if 2*Ncut>cfg.MaxCutoff, error('Evaluator cutoff audit failed.'); end
end
fprintf('accepted cutoff = %d\n',Ncut);

CurvatureSummary=table('Size',[numel(cfg.Lobes) 6], ...
    'VariableTypes',{'double','double','double','double','double','double'}, ...
    'VariableNames',{'lobe','betaGridCount','interiorPairCount','minimumC','maximumC','negativeCount'});
ReflectionRows=[];
ChebyshevRows=[];
RootRows=[];

for il=1:numel(cfg.Lobes)
    n=cfg.Lobes(il);
    NB=cfg.BetaCount(il);
    beta=linspace(.5,1,NB).';
    tGrid=violet_phase_grid(gamma(n:n+1),q.');
    t=tGrid(1,:);

    [W,Wb]=transverse_matrix_with_beta_derivative(beta,t,Ncut,cfg.EMOrder,cfg.TChunk);
    U=quotient_orthogonal_cubic(W,q,wq);
    Ub=quotient_orthogonal_cubic(Wb,q,wq);

    %% 1) Direct pointwise mixed curvature.
    C=nan(NB,NB);
    for ia=1:NB
        ua=U(ia,:); dua=Ub(ia,:);
        for ib=1:NB
            ub=U(ib,:); dub=Ub(ib,:);
            K=weighted_ip(ua,ub,wq);
            if abs(K)<1e-14, continue; end
            C(ia,ib)=real(weighted_ip(dua,dub,wq)/K - ...
                weighted_ip(dua,ub,wq)*weighted_ip(ua,dub,wq)/(K*K));
        end
    end
    interior=C(2:end-1,2:end-1); vals=interior(isfinite(interior));
    CurvatureSummary.lobe(il)=n;
    CurvatureSummary.betaGridCount(il)=NB;
    CurvatureSummary.interiorPairCount(il)=numel(vals);
    CurvatureSummary.minimumC(il)=min(vals);
    CurvatureSummary.maximumC(il)=max(vals);
    CurvatureSummary.negativeCount(il)=nnz(vals<0);

    fprintf('\nLOBE %d : POINTWISE MIXED CURVATURE\n',n);
    fprintf('------------------------------------------------------------\n');
    fprintf('beta grid            = %d\n',NB);
    fprintf('interior pairs       = %d\n',numel(vals));
    fprintf('min C                = %.12e\n',min(vals));
    fprintf('max C                = %.12e\n',max(vals));
    fprintf('negative C           = %d\n',nnz(vals<0));

    %% 2) Canonical reflection gauge at Violet.
    uV=U(1,:);
    J0uV=conj(fliplr(uV));
    z=weighted_ip(uV,J0uV,wq);
    if abs(z)>0, exp2ichi=exp(-1i*angle(z)); else, exp2ichi=1; end
    chi=.5*angle(exp2ichi);

    X=complex(zeros(size(U))); Y=complex(zeros(size(U)));
    Xb=complex(zeros(size(U))); Yb=complex(zeros(size(U)));
    for ib=1:NB
        Ju=exp2ichi*conj(fliplr(U(ib,:)));
        Jub=exp2ichi*conj(fliplr(Ub(ib,:)));
        X(ib,:)=(U(ib,:)+Ju)/2;
        Y(ib,:)=(U(ib,:)-Ju)/2;
        Xb(ib,:)=(Ub(ib,:)+Jub)/2;
        Yb(ib,:)=(Ub(ib,:)-Jub)/2;
    end

    normU=row_weighted_norm(U,wq); normY=row_weighted_norm(Y,wq);
    normUb=row_weighted_norm(Ub,wq); normYb=row_weighted_norm(Yb,wq);

    % Exact coefficient a(q)=theta'(t(q))/Omega and its reflection defect.
    Omega=violet_theta(gamma(n+1))-violet_theta(gamma(n));
    aq=violet_theta_prime(t)./Omega;
    ap=(aq+fliplr(aq))/2; am=(aq-fliplr(aq))/2;
    asymAbs=max(abs(am));
    asymRel=asymAbs/max(min(abs(ap)),realmin);

    % Modal coefficients, including low modes for diagnostic purposes.
    coefU=modal_coefficients(U,Psi,wq);
    coefUb=modal_coefficients(Ub,Psi,wq);
    coefX=modal_coefficients(X,Psi,wq);
    coefY=modal_coefficients(Y,Psi,wq);

    m=(0:cfg.MaxMode).';
    phaseX=coefX .* exp(-1i*chi) .* ((-1i).^m);       % should be real
    phaseY=coefY .* exp(-1i*chi) .* ((-1i).^(m+1));   % should be real
    high=5:(cfg.MaxMode+1); % MATLAB indices for modes >=4
    lockX=max(abs(imag(phaseX(high,:))),[],'all')/max(max(abs(phaseX(high,:)),[],'all'),realmin);
    lockY=max(abs(imag(phaseY(high,:))),[],'all')/max(max(abs(phaseY(high,:)),[],'all'),realmin);

    fprintf('\nLOBE %d : REFLECTION DECOMPOSITION\n',n);
    fprintf('------------------------------------------------------------\n');
    fprintf('chi                   = %.12e\n',chi);
    fprintf('max ||Y||/||u||       = %.12e\n',max(normY./max(normU,realmin)));
    fprintf('max ||Y_beta||/||u_beta|| = %.12e\n',max(normYb./max(normUb,realmin)));
    fprintf('max |a_-|             = %.12e\n',asymAbs);
    fprintf('max |a_-|/min|a_+|    = %.12e\n',asymRel);
    fprintf('X modal phase defect  = %.3e\n',lockX);
    fprintf('Y modal phase defect  = %.3e\n',lockY);

    for ib=1:NB
        ReflectionRows=[ReflectionRows; n beta(ib) chi normY(ib)/max(normU(ib),realmin) ...
            normYb(ib)/max(normUb(ib),realmin) asymAbs asymRel]; %#ok<AGROW>
    end

    %% 3) Corrected adjacent Chebyshev determinants for full high-mode u.
    coeff=coefU(high,:); coeffb=coefUb(high,:);
    p=abs(coeff).^2;
    pp=2*real(conj(coeff).*coeffb);
    for ib=1:NB
        for r=1:size(p,1)-1
            Delta=p(r,ib)*pp(r+1,ib)-p(r+1,ib)*pp(r,ib);
            ChebyshevRows=[ChebyshevRows; n beta(ib) (r+3) Delta]; %#ok<AGROW>
        end
    end

    dvals=ChebyshevRows(ChebyshevRows(:,1)==n,4);
    fprintf('\nLOBE %d : ADJACENT CHEBYSHEV SIGN\n',n);
    fprintf('------------------------------------------------------------\n');
    fprintf('Delta_m samples       = %d\n',numel(dvals));
    fprintf('nonnegative fraction  = %.9f\n',mean(dvals>=-cfg.SignTol));
    fprintf('minimum Delta_m       = %.12e\n',min(dvals));

    %% 4) Polya generating-polynomial root diagnostic.
    % G(z)=sum_{r=0}^{R} p_{r+4} z^r.  This is a sufficient-route audit,
    % not an assumption and not needed for the direct C calculation.
    for ib=1:NB
        cpoly=p(:,ib).';
        cpoly=cpoly/max(cpoly);
        rr=roots(fliplr(cpoly));
        nReal=nnz(abs(imag(rr))<=cfg.RootImagTol);
        nNonPos=nnz(abs(imag(rr))<=cfg.RootImagTol & real(rr)<=cfg.RootRealTol);
        maxImag=max(abs(imag(rr)));
        maxReal=max(real(rr));
        RootRows=[RootRows; n beta(ib) numel(rr) nReal nNonPos maxImag maxReal]; %#ok<AGROW>
    end
end

Tref=array2table(ReflectionRows,'VariableNames', ...
    {'lobe','beta','chi','relativeY','relativeYBeta','maxAbsAMinus','relativeAMinus'});
Tcheb=array2table(ChebyshevRows,'VariableNames',{'lobe','beta','mode','DeltaAdjacent'});
Troot=array2table(RootRows,'VariableNames', ...
    {'lobe','beta','rootCount','realRootCount','nonpositiveRealRootCount','maxAbsImag','maxReal'});

writetable(CurvatureSummary,fullfile(cfg.OutputDir,'POINTWISE_CURVATURE_SUMMARY.csv'));
writetable(Tref,fullfile(cfg.OutputDir,'REFLECTION_DEFECT.csv'));
writetable(Tcheb,fullfile(cfg.OutputDir,'ADJACENT_CHEBYSHEV_DETERMINANTS.csv'));
writetable(Troot,fullfile(cfg.OutputDir,'POLYA_ROOT_DIAGNOSTIC.csv'));

fprintf('\n============================================================\n');
fprintf('POINTWISE CURVATURE SUMMARY\n');
fprintf('============================================================\n');
disp(CurvatureSummary);
fprintf('Output directory: %s\n',cfg.OutputDir);
fprintf('AUDIT COMPLETE\n');

%% Local functions
function z=weighted_ip(x,y,w)
    z=sum(conj(x(:)).*y(:).*w(:));
end

function n=row_weighted_norm(X,w)
    n=sqrt(sum(abs(X).^2.*w.',2));
end

function C=modal_coefficients(U,Psi,w)
    C=Psi'*(U.'.*w); % modes x beta
end

function rho=quotient_orthogonal_cubic(W,q,wq)
    B=[ones(numel(q),1) q q.^2 q.^3];
    G=B'*(B.*wq);
    RHS=B'*(W.'.*wq);
    coeff=G\RHS;
    rho=W-(B*coeff).';
end

function Phi=shifted_legendre_basis(q,M)
    x=2*q-1;
    Phi=zeros(numel(q),M+1);
    P0=ones(size(x));
    Phi(:,1)=P0;
    if M==0, return; end
    P1=x; Phi(:,2)=sqrt(3)*P1;
    for m=1:M-1
        P2=((2*m+1)*x.*P1-m*P0)/(m+1);
        Phi(:,m+2)=sqrt(2*(m+1)+1)*P2;
        P0=P1; P1=P2;
    end
end

function tGrid=violet_phase_grid(gamma,q)
    NL=numel(gamma)-1; tGrid=nan(NL,numel(q)); th=violet_theta(gamma);
    for n=1:NL
        g0=gamma(n); g1=gamma(n+1); target=th(n)+q*(th(n+1)-th(n));
        t=g0+(g1-g0)*q; t(1)=g0; t(end)=g1;
        for it=1:12
            cand=t-(violet_theta(t)-target)./violet_theta_prime(t);
            cand=min(max(cand,g0),g1); t(2:end-1)=cand(2:end-1);
        end
        t(1)=g0; t(end)=g1; tGrid(n,:)=t;
    end
end

function y=violet_theta(t)
    t=double(t);
    y=.5*t.*log(t/(2*pi))-.5*t-pi/8+1./(48*t)+7./(5760*t.^3)+ ...
      31./(80640*t.^5)+127./(430080*t.^7)+511./(1216512*t.^9);
end

function y=violet_theta_prime(t)
    t=double(t);
    y=.5*log(t/(2*pi))-1./(48*t.^2)-21./(5760*t.^4)- ...
      155./(80640*t.^6)-889./(430080*t.^8)-4599./(1216512*t.^10);
end

function [Z,dZ]=transverse_matrix_with_beta_derivative(beta,t,Ncut,M,chunk)
    beta=double(beta(:)); t=double(t(:).'); nb=numel(beta); nt=numel(t);
    Z=complex(zeros(nb,nt)); dZ=complex(zeros(nb,nt));
    k=(1:Ncut-1).'; logk=log(k); A=exp(-beta*logk.'); Ad=-A.*logk.';
    logN=log(Ncut); Bernoulli=bernoulli_even(M);
    for first=1:chunk:nt
        last=min(nt,first+chunk-1); tt=t(first:last); B=exp(-1i*logk*tt);
        Zb=A*B; dZb=Ad*B; S=beta+1i*tt;
        T1=exp((1-S)*logN)./(S-1); dT1=T1.*(-logN-1./(S-1));
        Zb=Zb+T1; dZb=dZb+dT1;
        T2=.5*exp(-S*logN); dT2=-logN*T2; Zb=Zb+T2; dZb=dZb+dT2;
        for r=1:M
            Product=ones(size(S)); LogDerivative=zeros(size(S));
            for j=0:(2*r-2)
                Product=Product.*(S+j); LogDerivative=LogDerivative+1./(S+j);
            end
            corr=(Bernoulli(r)/factorial(2*r)).*Product.*exp(-(S+(2*r-1))*logN);
            dcorr=corr.*(LogDerivative-logN); Zb=Zb+corr; dZb=dZb+dcorr;
        end
        Z(:,first:last)=Zb; dZ(:,first:last)=dZb;
    end
end

function B=bernoulli_even(M)
    allB=[1/6;-1/30;1/42;-1/30;5/66;-691/2730;7/6;-3617/510;43867/798;-174611/330];
    if M>numel(allB), error('Increase Bernoulli table.'); end
    B=allB(1:M);
end

function w=trapezoid_weights(q)
    q=q(:); h=q(2)-q(1);
    if max(abs(diff(q)-h))>1e-12, error('Uniform q grid required.'); end
    w=h*ones(numel(q),1); w(1)=h/2; w(end)=h/2;
end
