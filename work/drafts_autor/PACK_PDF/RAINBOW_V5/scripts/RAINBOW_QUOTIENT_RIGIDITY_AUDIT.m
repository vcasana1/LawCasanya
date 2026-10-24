%% VIOLET_TRANSVERSE_QUOTIENT_RIGIDITY_AUDIT.m
% Pure MATLAB.  Transverse/Violet quotient-rigidity audit.
%
% Violet is beta = 1/2.  The supplied ordinates are used only to define
% the fixed Violet zero-to-zero lobe boundaries.  No zeros are searched or
% transported as beta varies.
%
% For each lobe n, a fixed phase coordinate q -> t_n(q) is built on the
% Violet fibre.  Every Transverse fibre W_{beta,n}(q) is evaluated on the same
% t_n(q).  Five beta-independent linear quotients Q are compared:
%   1 HERMITE_JET1       values + first derivatives at q=0,1
%   2 ENDPOINT_VALUES    values only
%   3 HERMITE_JET2       values + first + second derivatives
%   4 MINIMAL_BOUNDARY_SPLINE  four fixed anchors
%   5 ORTHOGONAL_CUBIC   weighted L2 projection off span{1,q,q^2,q^3}
%
% Projective defect:
%   M_n^Q(beta) = 1 - |<r^Q_{V,n},r^Q_{beta,n}>|^2,
%   r = QW/||QW||.
%
% The script reproduces the quotient-rigidity, same-lobe identity, and
% cross-quotient concordance diagnostics reported in the manuscript.

clear; clc; close all;
rng(20260825,'twister');

%% Paths and configuration
SCRIPT_DIR = fileparts(mfilename('fullpath'));
ROOT = fileparts(SCRIPT_DIR);

cfg = struct;
cfg.ZeroFile = fullfile(ROOT,'data','zeross.bin');
cfg.NLobes = 240;
cfg.Nq = 81;
cfg.NBeta = 49;
cfg.DeltaMin = 1e-4;
cfg.DeltaMax = 0.5;
cfg.EMOrder = 8;
cfg.InitialCutoff = 512;
cfg.MaxCutoff = 4096;
cfg.TransverseAuditTol = 2e-9;
cfg.TChunk = 900;
cfg.MonotonicRelTol = 2e-3;
cfg.MonotonicAbsTol = 2e-7;
cfg.BetaOrderNullReps = 3000;
cfg.LobeIdentityNullReps = 500;
cfg.NIdentityAnchors = 8;
cfg.SplineAnchorLeft = 0.10;
cfg.SplineAnchorRight = 0.90;
cfg.OutputDir = fullfile(ROOT,'outputs','quotient_rigidity');
if ~exist(cfg.OutputDir,'dir'), mkdir(cfg.OutputDir); end

quotientNames = { ...
    'HERMITE_JET1'; ...
    'ENDPOINT_VALUES'; ...
    'HERMITE_JET2'; ...
    'MINIMAL_BOUNDARY_SPLINE'; ...
    'ORTHOGONAL_CUBIC'};
NQ = numel(quotientNames);

fprintf('\nVIOLET TRANSVERSE QUOTIENT RIGIDITY AUDIT\n');
fprintf('------------------------------------------------------------\n');
fprintf('Violet lobes            : %d\n',cfg.NLobes);
fprintf('q points / lobe         : %d\n',cfg.Nq);
fprintf('Transverse beta fibres     : %d\n',cfg.NBeta);
fprintf('quotient families       : %d\n',NQ);
fprintf('beta-order nulls        : %d\n',cfg.BetaOrderNullReps);
fprintf('lobe-identity nulls     : %d\n',cfg.LobeIdentityNullReps);

%% Load fixed Violet boundaries
fid = fopen(cfg.ZeroFile,'rb');
if fid < 0, error('Cannot open %s.',cfg.ZeroFile); end
gamma = fread(fid,cfg.NLobes+1,'double');
fclose(fid);
if numel(gamma) < cfg.NLobes+1, error('Not enough Violet boundaries.'); end
gamma = gamma(:);

%% Fixed phase projection
q = linspace(0,1,cfg.Nq);
wq = trapezoid_weights(q);
tGrid = violet_phase_grid(gamma,q);
Tall = reshape(tGrid.',1,[]);

fprintf('\nFIXED VIOLET PHASE PROJECTION\n');
fprintf('------------------------------------------------------------\n');
fprintf('max left endpoint residual  = %.3e\n',max(abs(tGrid(:,1)-gamma(1:end-1))));
fprintf('max right endpoint residual = %.3e\n',max(abs(tGrid(:,end)-gamma(2:end))));

%% Transverse beta grid
positiveDelta = logspace(log10(cfg.DeltaMin),log10(cfg.DeltaMax),cfg.NBeta-1).';
delta = [0; positiveDelta];
beta = 0.5 + delta;
beta(end) = 1; delta(end) = 0.5;
NB = numel(beta); NL = cfg.NLobes;

%% Frozen spline anchors
[~,iL] = min(abs(q-cfg.SplineAnchorLeft));
[~,iR] = min(abs(q-cfg.SplineAnchorRight));
splineAnchorIndex = unique([1 iL iR cfg.Nq]);
if numel(splineAnchorIndex) ~= 4, error('Spline anchors collapsed.'); end

%% Euler--Maclaurin evaluator audit
fprintf('\nTRANSVERSE NUMERICAL AUDIT\n');
fprintf('------------------------------------------------------------\n');
betaAudit = [0.5;0.5001;0.51;0.60;0.80;1.00];
pickT = round(linspace(1,numel(Tall),19));
tAudit = Tall(pickT);
Ncut = cfg.InitialCutoff;
while true
    Za = transverse_matrix(betaAudit,tAudit,Ncut,cfg.EMOrder,cfg.TChunk);
    Zb = transverse_matrix(betaAudit,tAudit,2*Ncut,cfg.EMOrder,cfg.TChunk);
    err = max(abs(Za(:)-Zb(:))./max(1,abs(Zb(:))));
    fprintf('cutoff %5d vs %5d : relative error %.3e\n',Ncut,2*Ncut,err);
    if err <= cfg.TransverseAuditTol, break; end
    Ncut = 2*Ncut;
    if 2*Ncut > cfg.MaxCutoff, error('Transverse evaluator failed audit.'); end
end
fprintf('accepted cutoff = %d\n',Ncut);

%% Complete Transverse
fprintf('\nCONSTRUCTING COMPLETE TRANSVERSE PROJECTION\n');
tic;
Transverse = transverse_matrix(beta,Tall,Ncut,cfg.EMOrder,cfg.TChunk);
fprintf('elapsed = %.2f s\n',toc);

WVraw = reshape(Transverse(1,:),cfg.Nq,NL).';
fprintf('\nVIOLET BOUNDARY AUDIT\n');
fprintf('------------------------------------------------------------\n');
fprintf('max boundary residual    = %.3e\n',max(abs([WVraw(:,1);WVraw(:,end)])));
fprintf('median boundary residual = %.3e\n',median(abs([WVraw(:,1);WVraw(:,end)])));
WVraw(:,1)=0; WVraw(:,end)=0;

identityAnchorIndex = unique(round(linspace(2,NB,cfg.NIdentityAnchors)));
Nanchor = numel(identityAnchorIndex);

%% Storage
DefectByFamily = cell(NQ,1);
MedianCurveByFamily = nan(NB,NQ);
LobeStepFractionByFamily = nan(NL,NQ);
FullMonotoneMatrix = false(NL,NQ);
IdentityObserved = nan(Nanchor,NQ);
IdentityNullMedian = nan(Nanchor,NQ);
IdentityP = nan(Nanchor,NQ);
IdentityRatio = nan(Nanchor,NQ);
OrderNullRho = nan(cfg.BetaOrderNullReps,NQ);

Summary = table('Size',[NQ 11], ...
    'VariableTypes',{'string','double','double','double','double','double','double','double','double','double','double'}, ...
    'VariableNames',{'quotient','violetDefect','beta1Defect','spearmanBeta','orderNullP', ...
    'aggregateStepFraction','medianLobeStepFraction','fullMonotoneLobes', ...
    'fullMonotoneLobeFraction','maximumDownwardStep','beta1IdentityRatio'});

%% Main loop
for jq = 1:NQ
    qName = quotientNames{jq};
    fprintf('\nQUOTIENT %d / %d : %s\n',jq,NQ,qName);
    fprintf('------------------------------------------------------------\n');

    rhoV = apply_quotient(WVraw,q,wq,qName,splineAnchorIndex);
    [rV,normV,goodV] = normalize_rows(rhoV,wq);
    fprintf('usable Violet lobes = %d / %d\n',nnz(goodV),NL);
    fprintf('median residual norm = %.8e\n',median(normV(goodV)));

    Rnormalized = complex(nan(NB,NL,cfg.Nq));
    M = nan(NB,NL);

    for ib = 1:NB
        W = reshape(Transverse(ib,:),cfg.Nq,NL).';
        if ib == 1, W(:,1)=0; W(:,end)=0; end
        rho = apply_quotient(W,q,wq,qName,splineAnchorIndex);
        [r,~,good] = normalize_rows(rho,wq);
        good = good & goodV;
        Rnormalized(ib,:,:) = r;
        inner = sum(conj(rV).*r.*wq.',2);
        align2 = min(max(real(abs(inner).^2),0),1);
        defect = 1-align2;
        defect(~good)=NaN;
        M(ib,:) = defect.';
        if ib==1, M(ib,good)=0; end
    end

    DefectByFamily{jq}=M;
    medianCurve = row_median_finite(M);
    MedianCurveByFamily(:,jq)=medianCurve;
    report = monotonicity_report(medianCurve,M,cfg);
    LobeStepFractionByFamily(:,jq)=report.lobeStepFraction;
    FullMonotoneMatrix(:,jq)=report.fullLobeMask;

    observedRho = spearman_manual(beta,medianCurve);
    for rr=1:cfg.BetaOrderNullReps
        OrderNullRho(rr,jq)=spearman_manual(beta,medianCurve(randperm(NB)));
    end
    orderP=(1+sum(OrderNullRho(:,jq)>=observedRho))/(cfg.BetaOrderNullReps+1);

    fprintf('\nSAME-LOBE IDENTITY NULL\n');
    fprintf('------------------------------------------------------------\n');
    for ia=1:Nanchor
        ib=identityAnchorIndex(ia);
        rBeta=squeeze(Rnormalized(ib,:,:));
        observed=median_finite(M(ib,:));
        nullValues=nan(cfg.LobeIdentityNullReps,1);
        for rr=1:cfg.LobeIdentityNullReps
            perm=randperm(NL);
            innerNull=sum(conj(rV(perm,:)).*rBeta.*wq.',2);
            wrongDefect=1-min(max(abs(innerNull).^2,0),1);
            nullValues(rr)=median_finite(wrongDefect);
        end
        nullMedian=median(nullValues);
        pIdentity=(1+sum(nullValues<=observed))/(cfg.LobeIdentityNullReps+1);
        IdentityObserved(ia,jq)=observed;
        IdentityNullMedian(ia,jq)=nullMedian;
        IdentityP(ia,jq)=pIdentity;
        IdentityRatio(ia,jq)=nullMedian/max(observed,realmin);
        fprintf('beta %.7f | same %.6e | wrong %.6e | ratio %.3f | p %.6g\n', ...
            beta(ib),observed,nullMedian,IdentityRatio(ia,jq),pIdentity);
    end

    fprintf('\nMONOTONICITY\n');
    fprintf('------------------------------------------------------------\n');
    fprintf('Violet defect                = %.8e\n',medianCurve(1));
    fprintf('beta=1 defect                = %.8e\n',medianCurve(end));
    fprintf('Spearman(beta,M)             = %.10f\n',observedRho);
    fprintf('beta-order null p            = %.8g\n',orderP);
    fprintf('aggregate monotone steps     = %.6f\n',report.aggregateStepFraction);
    fprintf('median lobe monotone steps   = %.6f\n',report.medianLobeStepFraction);
    fprintf('fully monotone lobes         = %d / %d\n',nnz(report.fullLobeMask),NL);
    fprintf('fully monotone lobe fraction = %.6f\n',report.fullLobeFraction);
    fprintf('largest downward step        = %.8e\n',report.maximumDownwardStep);

    Summary.quotient(jq)=string(qName);
    Summary.violetDefect(jq)=medianCurve(1);
    Summary.beta1Defect(jq)=medianCurve(end);
    Summary.spearmanBeta(jq)=observedRho;
    Summary.orderNullP(jq)=orderP;
    Summary.aggregateStepFraction(jq)=report.aggregateStepFraction;
    Summary.medianLobeStepFraction(jq)=report.medianLobeStepFraction;
    Summary.fullMonotoneLobes(jq)=nnz(report.fullLobeMask);
    Summary.fullMonotoneLobeFraction(jq)=report.fullLobeFraction;
    Summary.maximumDownwardStep(jq)=report.maximumDownwardStep;
    Summary.beta1IdentityRatio(jq)=IdentityRatio(end,jq);
end

%% Cross-quotient rigidity
allFamilyMonotone=all(FullMonotoneMatrix,2);
NallFamily=nnz(allFamilyMonotone);
NpassedByLobe=sum(FullMonotoneMatrix,2);
MedianCurveSpearman=nan(NQ,NQ);
FullGeometrySpearman=nan(NQ,NQ);
for i=1:NQ
    for j=1:NQ
        MedianCurveSpearman(i,j)=spearman_manual(MedianCurveByFamily(:,i),MedianCurveByFamily(:,j));
        FullGeometrySpearman(i,j)=spearman_manual(DefectByFamily{i}(:),DefectByFamily{j}(:));
    end
end

fprintf('\nCROSS-QUOTIENT RIGIDITY\n');
fprintf('------------------------------------------------------------\n');
fprintf('lobes fully monotone under EVERY quotient: %d / %d = %.8f\n', ...
    NallFamily,NL,NallFamily/NL);
fprintf('\nPAIRWISE SPEARMAN OF MEDIAN beta CURVES\n'); disp(MedianCurveSpearman);
fprintf('\nPAIRWISE SPEARMAN OF FULL beta x LOBE GEOMETRY\n'); disp(FullGeometrySpearman);

%% Export tables
Tlobe=table((1:NL).',NpassedByLobe,allFamilyMonotone, ...
    'VariableNames',{'violetLobe','numberOfMonotoneQuotients','monotoneUnderEveryQuotient'});
for jq=1:NQ
    vn=matlab.lang.makeValidName(['stepFraction_' quotientNames{jq}]);
    Tlobe.(vn)=LobeStepFractionByFamily(:,jq);
end
writetable(Tlobe,fullfile(cfg.OutputDir,'LOBE_BY_LOBE_QUOTIENT_RIGIDITY.csv'));
writetable(Summary,fullfile(cfg.OutputDir,'QUOTIENT_RIGIDITY_SUMMARY.csv'));

Tidentity=table('Size',[Nanchor*NQ 6], ...
    'VariableTypes',{'double','string','double','double','double','double'}, ...
    'VariableNames',{'beta','quotient','sameLobeDefect','wrongLobeMedian','wrongOverSameRatio','lowerTailP'});
row=0;
for ia=1:Nanchor
    for jq=1:NQ
        row=row+1;
        Tidentity.beta(row)=beta(identityAnchorIndex(ia));
        Tidentity.quotient(row)=string(quotientNames{jq});
        Tidentity.sameLobeDefect(row)=IdentityObserved(ia,jq);
        Tidentity.wrongLobeMedian(row)=IdentityNullMedian(ia,jq);
        Tidentity.wrongOverSameRatio(row)=IdentityRatio(ia,jq);
        Tidentity.lowerTailP(row)=IdentityP(ia,jq);
    end
end
writetable(Tidentity,fullfile(cfg.OutputDir,'SAME_LOBE_IDENTITY_ACROSS_QUOTIENTS.csv'));

%% Figures
f=figure('Name','Transverse quotient rigidity','NumberTitle','off');
for jq=1:NQ
    semilogy(beta(2:end),max(MedianCurveByFamily(2:end,jq),realmin),'LineWidth',1.4,'DisplayName',quotientNames{jq}); hold on;
end
xlabel('\beta'); ylabel('median projective defect M');
title('Transverse/Violet projective defect under five quotients');
legend('Location','best','Interpreter','none'); grid on;
save_figure_png(f,fullfile(cfg.OutputDir,'fig01_projective_defect_all_quotients.png'));

f=figure('Name','Normalized quotient rigidity','NumberTitle','off');
for jq=1:NQ
    y=MedianCurveByFamily(:,jq)/max(MedianCurveByFamily(end,jq),realmin);
    plot(beta,y,'LineWidth',1.5,'DisplayName',quotientNames{jq}); hold on;
end
xlabel('\beta'); ylabel('M(\beta) / M(1)');
title('Normalized Transverse deformation across quotient choices');
legend('Location','best','Interpreter','none'); grid on;
save_figure_png(f,fullfile(cfg.OutputDir,'fig02_normalized_defect_curves.png'));

lobeShow=min(40,NL);
f=figure('Name','One lobe across quotients','NumberTitle','off');
for jq=1:NQ
    y=DefectByFamily{jq}(:,lobeShow);
    semilogy(beta(2:end),max(y(2:end),realmin),'LineWidth',1.4,'DisplayName',quotientNames{jq}); hold on;
end
xlabel('\beta'); ylabel(sprintf('M_{%d}(\beta)',lobeShow));
title(sprintf('Same Violet lobe %d under five boundary quotients',lobeShow));
legend('Location','best','Interpreter','none'); grid on;
save_figure_png(f,fullfile(cfg.OutputDir,'fig03_lobe40_all_quotients.png'));

save(fullfile(cfg.OutputDir,'VIOLET_TRANSVERSE_QUOTIENT_RIGIDITY_COMPLETE.mat'), ...
    'cfg','gamma','q','wq','tGrid','beta','delta','quotientNames', ...
    'DefectByFamily','MedianCurveByFamily','LobeStepFractionByFamily', ...
    'FullMonotoneMatrix','IdentityObserved','IdentityNullMedian','IdentityP', ...
    'IdentityRatio','MedianCurveSpearman','FullGeometrySpearman','Summary','-v7.3');

fprintf('\nAUDIT COMPLETE\n');

%% Local functions
function rho=apply_quotient(W,q,wq,qName,splineAnchorIndex)
    switch upper(qName)
        case 'HERMITE_JET1', rho=quotient_hermite_jet1(W,q);
        case 'ENDPOINT_VALUES', rho=quotient_endpoint_values(W,q);
        case 'HERMITE_JET2', rho=quotient_hermite_jet2(W,q);
        case 'MINIMAL_BOUNDARY_SPLINE', rho=quotient_boundary_spline(W,q,splineAnchorIndex);
        case 'ORTHOGONAL_CUBIC', rho=quotient_orthogonal_cubic(W,q,wq);
        otherwise, error('Unknown quotient %s.',qName);
    end
end

function rho=quotient_hermite_jet1(W,q)
    [d0,d1]=endpoint_first_derivatives(W,q); y0=W(:,1); y1=W(:,end); x=q(:).';
    h00=2*x.^3-3*x.^2+1; h10=x.^3-2*x.^2+x; h01=-2*x.^3+3*x.^2; h11=x.^3-x.^2;
    H=y0.*h00+d0.*h10+y1.*h01+d1.*h11; rho=W-H; rho(:,1)=0; rho(:,end)=0;
end

function rho=quotient_endpoint_values(W,q)
    x=q(:).'; H=W(:,1).*(1-x)+W(:,end).*x; rho=W-H; rho(:,1)=0; rho(:,end)=0;
end

function rho=quotient_hermite_jet2(W,q)
    [d0,d1]=endpoint_first_derivatives(W,q); [dd0,dd1]=endpoint_second_derivatives(W,q);
    y0=W(:,1); y1=W(:,end);
    A=[1 0 0 0 0 0; 0 1 0 0 0 0; 0 0 2 0 0 0; 1 1 1 1 1 1; 0 1 2 3 4 5; 0 0 2 6 12 20];
    C=A\[y0.';d0.';dd0.';y1.';d1.';dd1.']; x=q(:);
    V=[ones(size(x)) x x.^2 x.^3 x.^4 x.^5]; H=(V*C).'; rho=W-H; rho(:,1)=0; rho(:,end)=0;
end

function rho=quotient_boundary_spline(W,q,idx)
    H=complex(zeros(size(W))); qa=q(idx);
    for n=1:size(W,1), H(n,:)=spline(qa,W(n,idx),q); end
    rho=W-H;
end

function rho=quotient_orthogonal_cubic(W,q,wq)
    x=q(:); B=[ones(size(x)) x x.^2 x.^3]; G=B.'*(B.*wq); RHS=B.'*(W.'.*wq); C=G\RHS; H=(B*C).'; rho=W-H;
end

function [d0,d1]=endpoint_first_derivatives(W,q)
    h=q(2)-q(1);
    d0=(-25*W(:,1)+48*W(:,2)-36*W(:,3)+16*W(:,4)-3*W(:,5))/(12*h);
    d1=(25*W(:,end)-48*W(:,end-1)+36*W(:,end-2)-16*W(:,end-3)+3*W(:,end-4))/(12*h);
end

function [dd0,dd1]=endpoint_second_derivatives(W,q)
    h=q(2)-q(1);
    dd0=(35*W(:,1)-104*W(:,2)+114*W(:,3)-56*W(:,4)+11*W(:,5))/(12*h^2);
    dd1=(35*W(:,end)-104*W(:,end-1)+114*W(:,end-2)-56*W(:,end-3)+11*W(:,end-4))/(12*h^2);
end

function [R,nrm,good]=normalize_rows(X,wq)
    nrm=sqrt(sum(abs(X).^2.*wq.',2)); good=isfinite(nrm)&nrm>1e-12; R=complex(nan(size(X))); R(good,:)=X(good,:)./nrm(good);
end

function report=monotonicity_report(curve,M,cfg)
    dc=diff(curve); sc=max(abs(curve(1:end-1)),abs(curve(2:end))); tol=cfg.MonotonicAbsTol+cfg.MonotonicRelTol.*sc;
    good=isfinite(dc)&isfinite(tol); pass=dc>=-tol;
    report.aggregateStepFraction=mean(pass(good));
    if any(good), report.maximumDownwardStep=max(max(0,-dc(good))); else, report.maximumDownwardStep=NaN; end
    NL=size(M,2); frac=nan(NL,1); full=false(NL,1);
    for n=1:NL
        y=M(:,n); dy=diff(y); sc=max(abs(y(1:end-1)),abs(y(2:end))); tol=cfg.MonotonicAbsTol+cfg.MonotonicRelTol.*sc;
        good=isfinite(dy)&isfinite(tol); if ~any(good), continue; end
        pp=dy(good)>=-tol(good); frac(n)=mean(pp); full(n)=all(pp);
    end
    report.lobeStepFraction=frac; report.fullLobeMask=full; report.medianLobeStepFraction=median_finite(frac); report.fullLobeFraction=mean(full);
end

function tGrid=violet_phase_grid(gamma,q)
    NL=numel(gamma)-1; tGrid=nan(NL,numel(q)); th=violet_theta(gamma);
    for n=1:NL
        g0=gamma(n); g1=gamma(n+1); target=th(n)+q*(th(n+1)-th(n)); t=g0+(g1-g0)*q; t(1)=g0; t(end)=g1;
        for it=1:12
            cand=t-(violet_theta(t)-target)./violet_theta_prime(t); cand=min(max(cand,g0),g1); t(2:end-1)=cand(2:end-1);
        end
        t(1)=g0; t(end)=g1; tGrid(n,:)=t;
    end
end

function y=violet_theta(t)
    t=double(t); y=.5*t.*log(t/(2*pi))-.5*t-pi/8+1./(48*t)+7./(5760*t.^3)+31./(80640*t.^5)+127./(430080*t.^7)+511./(1216512*t.^9);
end

function y=violet_theta_prime(t)
    t=double(t); y=.5*log(t/(2*pi))-1./(48*t.^2)-21./(5760*t.^4)-155./(80640*t.^6)-889./(430080*t.^8)-4599./(1216512*t.^10);
end

function Z=transverse_matrix(beta,t,Ncut,M,chunk)
    beta=double(beta(:)); t=double(t(:).'); nb=numel(beta); nt=numel(t); Z=complex(zeros(nb,nt));
    k=(1:Ncut-1).'; logk=log(k); A=exp(-beta*logk.'); logN=log(Ncut); Bernoulli=bernoulli_even(M);
    for first=1:chunk:nt
        last=min(nt,first+chunk-1); tt=t(first:last); B=exp(-1i*logk*tt); Zb=A*B; S=beta+1i*tt;
        Zb=Zb+exp((1-S)*logN)./(S-1)+.5*exp(-S*logN);
        for r=1:M
            P=ones(size(S)); for j=0:(2*r-2), P=P.*(S+j); end
            Zb=Zb+(Bernoulli(r)/factorial(2*r)).*P.*exp(-(S+(2*r-1))*logN);
        end
        Z(:,first:last)=Zb;
    end
end

function B=bernoulli_even(M)
    allB=[1/6;-1/30;1/42;-1/30;5/66;-691/2730;7/6;-3617/510;43867/798;-174611/330];
    if M>numel(allB), error('Increase Bernoulli table.'); end; B=allB(1:M);
end

function w=trapezoid_weights(q)
    q=q(:); h=q(2)-q(1); if max(abs(diff(q)-h))>1e-12, error('Uniform q grid required.'); end
    w=h*ones(numel(q),1); w(1)=h/2; w(end)=h/2;
end

function out=row_median_finite(X)
    out=nan(size(X,1),1); for i=1:size(X,1), out(i)=median_finite(X(i,:)); end
end

function m=median_finite(x)
    x=x(isfinite(x)); if isempty(x), m=NaN; else, m=median(x); end
end

function rho=spearman_manual(x,y)
    x=x(:); y=y(:); good=isfinite(x)&isfinite(y); x=x(good); y=y(good); if numel(x)<3, rho=NaN; return; end
    rx=average_ranks(x); ry=average_ranks(y); rx=rx-mean(rx); ry=ry-mean(ry); den=sqrt(sum(rx.^2)*sum(ry.^2));
    if den<=realmin, rho=NaN; else, rho=sum(rx.*ry)/den; end
end

function ranks=average_ranks(x)
    [xs,order]=sort(x); N=numel(x); sr=zeros(N,1); i=1;
    while i<=N
        j=i; while j<N && xs(j+1)==xs(i), j=j+1; end; sr(i:j)=(i+j)/2; i=j+1;
    end
    ranks=zeros(N,1); ranks(order)=sr;
end

function save_figure_png(fig,path)
    try, exportgraphics(fig,path,'Resolution',180); catch, set(fig,'PaperPositionMode','auto'); print(fig,path,'-dpng','-r180'); end
end
