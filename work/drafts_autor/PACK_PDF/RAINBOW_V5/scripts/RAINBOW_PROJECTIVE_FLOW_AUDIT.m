%% VIOLET_TRANSVERSE_PROJECTIVE_FLOW_AUDIT.m
% Pure MATLAB. Differential Transverse/Violet projective-flow audit.
%
% The fixed Violet lobe boundaries define q -> t_n(q).  The script evaluates
% W_{beta,n}, its exact transverse beta derivative (within the chosen
% Euler--Maclaurin representation), the normalized projective defect M,
% its analytic beta derivative M_beta, and the intrinsic projective speed P.
% No beta-dependent zeros are introduced or searched.

clear; clc; close all;
rng(20260825,'twister');

SCRIPT_DIR=fileparts(mfilename('fullpath'));
ROOT=fileparts(SCRIPT_DIR);

cfg=struct;
cfg.ZeroFile=fullfile(ROOT,'data','zeross.bin');
cfg.NLobes=240;
cfg.Nq=121;
cfg.NBetaLog=90;
cfg.NBetaLinear=181;
cfg.DeltaMin=1e-5;
cfg.EMOrder=8;
cfg.InitialCutoff=512;
cfg.MaxCutoff=4096;
cfg.TransverseAuditTol=2e-9;
cfg.TChunk=700;
cfg.SplineAnchorLeft=.10;
cfg.SplineAnchorRight=.90;
cfg.DerivativeAbsTol=2e-9;
cfg.DerivativeRelTol=2e-6;
cfg.ProjectiveSpeedTol=5e-10;
cfg.FDAuditBetaCount=15;
cfg.FDAuditLobeCount=30;
cfg.OutputDir=fullfile(ROOT,'outputs','projective_flow');
if ~exist(cfg.OutputDir,'dir'), mkdir(cfg.OutputDir); end

quotientNames={'HERMITE_JET1';'ENDPOINT_VALUES';'HERMITE_JET2';'MINIMAL_BOUNDARY_SPLINE';'ORTHOGONAL_CUBIC'};
NQ=numel(quotientNames);

fprintf('\nVIOLET TRANSVERSE PROJECTIVE FLOW AUDIT\n');
fprintf('------------------------------------------------------------\n');
fprintf('Violet lobes             : %d\n',cfg.NLobes);
fprintf('q samples/lobe           : %d\n',cfg.Nq);
fprintf('quotient families        : %d\n',NQ);

%% Fixed Violet boundaries
fid=fopen(cfg.ZeroFile,'rb'); if fid<0, error('Cannot open %s.',cfg.ZeroFile); end
gamma=fread(fid,cfg.NLobes+1,'double'); fclose(fid); gamma=gamma(:);
if numel(gamma)<cfg.NLobes+1, error('Not enough Violet lobe boundaries.'); end

%% Fixed phase projection
q=linspace(0,1,cfg.Nq); wq=trapezoid_weights(q); tGrid=violet_phase_grid(gamma,q); Tall=reshape(tGrid.',1,[]);
fprintf('\nVIOLET PHASE PROJECTION\n');
fprintf('------------------------------------------------------------\n');
fprintf('left endpoint error  = %.3e\n',max(abs(tGrid(:,1)-gamma(1:end-1))));
fprintf('right endpoint error = %.3e\n',max(abs(tGrid(:,end)-gamma(2:end))));

%% Dense beta grid
deltaLog=logspace(log10(cfg.DeltaMin),log10(.1),cfg.NBetaLog);
betaLinear=linspace(.5,1,cfg.NBetaLinear);
beta=unique([.5 .5+deltaLog betaLinear]).'; beta=beta(beta>=.5 & beta<=1); beta(1)=.5; beta(end)=1;
NB=numel(beta); NL=cfg.NLobes;
fprintf('\nDENSE TRANSVERSE DOMAIN\n');
fprintf('------------------------------------------------------------\n');
fprintf('beta samples          = %d\n',NB);
fprintf('Violet beta           = %.12f\n',beta(1));
fprintf('outer Transverse beta    = %.12f\n',beta(end));
fprintf('first positive delta  = %.3e\n',beta(2)-.5);

%% Spline anchors
[~,iL]=min(abs(q-cfg.SplineAnchorLeft)); [~,iR]=min(abs(q-cfg.SplineAnchorRight));
splineAnchorIndex=unique([1 iL iR cfg.Nq]); if numel(splineAnchorIndex)~=4, error('Spline anchors collapsed.'); end

%% Value and derivative audit
fprintf('\nTRANSVERSE / TRANSVERSE DERIVATIVE AUDIT\n');
fprintf('------------------------------------------------------------\n');
betaAudit=[.5;.50001;.5001;.51;.75;1]; pickT=round(linspace(1,numel(Tall),19)); tAudit=Tall(pickT); Ncut=cfg.InitialCutoff;
while true
    [Wa,dWa]=transverse_matrix_with_beta_derivative(betaAudit,tAudit,Ncut,cfg.EMOrder,cfg.TChunk);
    [Wb,dWb]=transverse_matrix_with_beta_derivative(betaAudit,tAudit,2*Ncut,cfg.EMOrder,cfg.TChunk);
    valueError=max(abs(Wa(:)-Wb(:))./max(1,abs(Wb(:))));
    derivativeError=max(abs(dWa(:)-dWb(:))./max(1,abs(dWb(:))));
    fprintf('cutoff %5d vs %5d : W %.3e   W_beta %.3e\n',Ncut,2*Ncut,valueError,derivativeError);
    if max(valueError,derivativeError)<=cfg.TransverseAuditTol, break; end
    Ncut=2*Ncut; if 2*Ncut>cfg.MaxCutoff, error('Transverse derivative audit failed.'); end
end
fprintf('accepted cutoff = %d\n',Ncut);

%% Complete differential Transverse
fprintf('\nBUILDING DIFFERENTIAL TRANSVERSE\n'); tic;
[Transverse,TransverseBeta]=transverse_matrix_with_beta_derivative(beta,Tall,Ncut,cfg.EMOrder,cfg.TChunk);
fprintf('elapsed = %.2f s\n',toc);

WVraw=reshape(Transverse(1,:),cfg.Nq,NL).';
fprintf('\nVIOLET BOUNDARY AUDIT\n');
fprintf('------------------------------------------------------------\n');
fprintf('max residual    = %.3e\n',max(abs([WVraw(:,1);WVraw(:,end)])));
fprintf('median residual = %.3e\n',median(abs([WVraw(:,1);WVraw(:,end)])));
WVraw(:,1)=0; WVraw(:,end)=0;

%% Storage
MByFamily=cell(NQ,1); MdByFamily=cell(NQ,1); PByFamily=cell(NQ,1);
FullPositiveDerivative=false(NL,NQ); StrictPositiveFraction=nan(NL,NQ); MinDerivativeByLobe=nan(NL,NQ);
Summary=table('Size',[NQ 9], ...
    'VariableTypes',{'string','double','double','double','double','double','double','double','double'}, ...
    'VariableNames',{'quotient','derivativeSampleFractionNonnegative','lobesDerivativeNonnegativeEverywhere', ...
    'lobeFractionDerivativeNonnegativeEverywhere','medianStrictPositiveFraction','minimumObservedDerivative', ...
    'minimumProjectiveSpeed','fdMedianRelativeError','fdMaximumRelativeError'});

%% Differential quotient loop
for jq=1:NQ
    qName=quotientNames{jq};
    fprintf('\nDIFFERENTIAL QUOTIENT %d / %d : %s\n',jq,NQ,qName);
    fprintf('------------------------------------------------------------\n');
    rhoV=apply_quotient(WVraw,q,wq,qName,splineAnchorIndex);
    [rV,~,goodV]=normalize_rows(rhoV,wq);
    fprintf('usable Violet lobes = %d / %d\n',nnz(goodV),NL);

    M=nan(NB,NL); Md=nan(NB,NL); P=nan(NB,NL);
    for ib=1:NB
        W=reshape(Transverse(ib,:),cfg.Nq,NL).';
        Wbeta=reshape(TransverseBeta(ib,:),cfg.Nq,NL).';
        if ib==1, W(:,1)=0; W(:,end)=0; end
        rho=apply_quotient(W,q,wq,qName,splineAnchorIndex);
        rhoBeta=apply_quotient(Wbeta,q,wq,qName,splineAnchorIndex);
        [r,normR,goodR]=normalize_rows(rho,wq); good=goodV & goodR;

        c=sum(conj(rV).*r.*wq.',2); align2=min(max(real(abs(c).^2),0),1); m=1-align2;
        a=sum(conj(rho).*rhoBeta.*wq.',2);
        rBeta=complex(nan(size(rho)));
        rBeta(good,:)=rhoBeta(good,:)./normR(good)-rho(good,:).*(real(a(good))./normR(good).^3);
        cBeta=sum(conj(rV).*rBeta.*wq.',2);
        md=-2*real(conj(c).*cBeta);
        rhoBetaNorm2=sum(abs(rhoBeta).^2.*wq.',2);
        p=rhoBetaNorm2./normR.^2-abs(a).^2./normR.^4;
        tiny=p<0 & p>=-cfg.ProjectiveSpeedTol; p(tiny)=0;
        m(~good)=NaN; md(~good)=NaN; p(~good)=NaN; if ib==1, m(good)=0; end
        M(ib,:)=m.'; Md(ib,:)=md.'; P(ib,:)=p.';
    end
    MByFamily{jq}=M; MdByFamily{jq}=Md; PByFamily{jq}=P;

    tol=cfg.DerivativeAbsTol+cfg.DerivativeRelTol.*max(abs(Md),1e-12);
    signPass=Md>=-tol; signStrict=Md>tol; finiteInterior=isfinite(Md(2:end,:));
    for n=1:NL
        good=finiteInterior(:,n); if ~any(good), continue; end
        FullPositiveDerivative(n,jq)=all(signPass(2:end,n) | ~good);
        StrictPositiveFraction(n,jq)=mean(signStrict(2:end,n) & good)/mean(good);
        MinDerivativeByLobe(n,jq)=min(Md(2:end,n),[],'omitnan');
    end
    vals=Md(2:end,:); finite=isfinite(vals); localTol=cfg.DerivativeAbsTol+cfg.DerivativeRelTol.*abs(vals);
    neg=finite & vals < -localTol; nNegative=nnz(neg); nTotal=nnz(finite); fractionNonnegative=1-nNegative/max(nTotal,1);

    finiteP=isfinite(P); minP=min(P(finiteP)); NnegativeP=nnz(P(finiteP)<-cfg.ProjectiveSpeedTol);

    %% Finite-difference audit of analytic M_beta
    betaIdx=unique(round(linspace(3,NB-2,cfg.FDAuditBetaCount)));
    lobeIdx=unique(round(linspace(1,NL,cfg.FDAuditLobeCount)));
    fdErrors=[];
    for ii=1:numel(betaIdx)
        ib=betaIdx(ii); hm=beta(ib)-beta(ib-1); hp=beta(ib+1)-beta(ib);
        for jj=1:numel(lobeIdx)
            n=lobeIdx(jj); y=[M(ib-1,n) M(ib,n) M(ib+1,n)]; if ~all(isfinite(y)), continue; end
            fd=finite_difference_nonuniform(y(1),y(2),y(3),hm,hp); ex=Md(ib,n);
            fdErrors(end+1,1)=abs(fd-ex)/max([abs(fd),abs(ex),1e-10]); %#ok<SAGROW>
        end
    end
    fdMedian=median(fdErrors); fdMax=max(fdErrors);

    fprintf('\nM_beta SIGN\n');
    fprintf('------------------------------------------------------------\n');
    fprintf('nonnegative derivative samples = %d / %d = %.9f\n',nTotal-nNegative,nTotal,fractionNonnegative);
    fprintf('lobes M_beta >= 0 for all beta = %d / %d\n',nnz(FullPositiveDerivative(:,jq)),NL);
    fprintf('median strict-positive fraction/lobe = %.9f\n',median(StrictPositiveFraction(:,jq),'omitnan'));
    fprintf('worst lobe minimum M_beta = %.12e\n',min(MinDerivativeByLobe(:,jq),[],'omitnan'));
    fprintf('\nPROJECTIVE SPEED P\n');
    fprintf('------------------------------------------------------------\n');
    fprintf('minimum P           = %.12e\n',minP);
    fprintf('invalid negative P  = %d\n',NnegativeP);
    fprintf('\nANALYTIC DERIVATIVE vs FINITE DIFFERENCE\n');
    fprintf('------------------------------------------------------------\n');
    fprintf('median relative error = %.6e\n',fdMedian);
    fprintf('maximum relative error = %.6e\n',fdMax);

    Summary.quotient(jq)=string(qName);
    Summary.derivativeSampleFractionNonnegative(jq)=fractionNonnegative;
    Summary.lobesDerivativeNonnegativeEverywhere(jq)=nnz(FullPositiveDerivative(:,jq));
    Summary.lobeFractionDerivativeNonnegativeEverywhere(jq)=mean(FullPositiveDerivative(:,jq));
    Summary.medianStrictPositiveFraction(jq)=median(StrictPositiveFraction(:,jq),'omitnan');
    Summary.minimumObservedDerivative(jq)=min(MinDerivativeByLobe(:,jq),[],'omitnan');
    Summary.minimumProjectiveSpeed(jq)=minP;
    Summary.fdMedianRelativeError(jq)=fdMedian;
    Summary.fdMaximumRelativeError(jq)=fdMax;
end

%% Cross-quotient diagnosis
allQ=all(FullPositiveDerivative,2); NallQ=nnz(allQ);
fprintf('\nCROSS-QUOTIENT DIFFERENTIAL RIGIDITY\n');
fprintf('------------------------------------------------------------\n');
fprintf('lobes with M_beta >= 0 for EVERY beta and EVERY Q: %d / %d = %.9f\n',NallQ,NL,NallQ/NL);
for jq=1:NQ, fprintf('%-28s : %3d / %3d\n',quotientNames{jq},nnz(FullPositiveDerivative(:,jq)),NL); end

fprintf('\nLOBE FAILURES\n');
fprintf('------------------------------------------------------------\n');
for jq=1:NQ
    bad=find(~FullPositiveDerivative(:,jq)); fprintf('%-28s : ',quotientNames{jq});
    if isempty(bad), fprintf('none'); else, fprintf('%d ',bad); end; fprintf('\n');
end

%% Tables
Tlobe=table((1:NL).',allQ,sum(FullPositiveDerivative,2), ...
    'VariableNames',{'violetLobe','nonnegativeForEveryQ','numberOfQPassed'});
for jq=1:NQ
    a=matlab.lang.makeValidName(['pass_' quotientNames{jq}]);
    b=matlab.lang.makeValidName(['minMd_' quotientNames{jq}]);
    c=matlab.lang.makeValidName(['strictFraction_' quotientNames{jq}]);
    Tlobe.(a)=FullPositiveDerivative(:,jq); Tlobe.(b)=MinDerivativeByLobe(:,jq); Tlobe.(c)=StrictPositiveFraction(:,jq);
end
writetable(Tlobe,fullfile(cfg.OutputDir,'LOBE_DIFFERENTIAL_SIGN_AUDIT.csv'));
writetable(Summary,fullfile(cfg.OutputDir,'PROJECTIVE_FLOW_SUMMARY.csv'));

%% Figures
f=figure('Name','Differential Transverse monotonicity','NumberTitle','off');
for jq=1:NQ, plot(beta,row_median_finite(MdByFamily{jq}),'LineWidth',1.4,'DisplayName',quotientNames{jq}); hold on; end
yline(0,'--'); xlabel('\beta'); ylabel('median M_\beta'); title('Differential sign of Transverse/Violet projective deformation');
legend('Location','best','Interpreter','none'); grid on; save_figure_png(f,fullfile(cfg.OutputDir,'fig01_projective_derivative_Mbeta.png'));

f=figure('Name','Projective speed','NumberTitle','off');
for jq=1:NQ, semilogy(beta,max(row_median_finite(PByFamily{jq}),realmin),'LineWidth',1.4,'DisplayName',quotientNames{jq}); hold on; end
xlabel('\beta'); ylabel('median P'); title('Intrinsic projective speed of the Transverse fibres');
legend('Location','best','Interpreter','none'); grid on; save_figure_png(f,fullfile(cfg.OutputDir,'fig02_projective_speed_P.png'));

lobeShow=40;
f=figure('Name','Example differential Violet lobe','NumberTitle','off');
for jq=1:NQ, plot(beta,MdByFamily{jq}(:,lobeShow),'LineWidth',1.3,'DisplayName',quotientNames{jq}); hold on; end
yline(0,'--'); xlabel('\beta'); ylabel(sprintf('M''_{%d}(\beta)',lobeShow));
title(sprintf('Differential Transverse deformation of Violet lobe %d',lobeShow));
legend('Location','best','Interpreter','none'); grid on; save_figure_png(f,fullfile(cfg.OutputDir,'fig03_lobe40_Mbeta.png'));

save(fullfile(cfg.OutputDir,'VIOLET_TRANSVERSE_PROJECTIVE_FLOW_COMPLETE.mat'), ...
    'cfg','gamma','q','wq','tGrid','beta','quotientNames','MByFamily','MdByFamily','PByFamily', ...
    'FullPositiveDerivative','StrictPositiveFraction','MinDerivativeByLobe','Summary','-v7.3');

fprintf('\nFINAL VIOLET TRANSVERSE PROJECTIVE FLOW DIAGNOSIS\n');
fprintf('------------------------------------------------------------\n');
disp(Summary);
fprintf('lobes satisfying M_beta >= 0 for EVERY beta and EVERY quotient: %d / %d = %.9f\n',NallQ,NL,NallQ/NL);
fprintf('AUDIT COMPLETE\n');

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
    [d0,d1]=endpoint_first_derivatives(W,q); [dd0,dd1]=endpoint_second_derivatives(W,q); y0=W(:,1); y1=W(:,end);
    A=[1 0 0 0 0 0;0 1 0 0 0 0;0 0 2 0 0 0;1 1 1 1 1 1;0 1 2 3 4 5;0 0 2 6 12 20];
    C=A\[y0.';d0.';dd0.';y1.';d1.';dd1.']; x=q(:); V=[ones(size(x)) x x.^2 x.^3 x.^4 x.^5]; H=(V*C).'; rho=W-H; rho(:,1)=0; rho(:,end)=0;
end
function rho=quotient_boundary_spline(W,q,idx)
    H=complex(zeros(size(W))); qa=q(idx); for n=1:size(W,1), H(n,:)=spline(qa,W(n,idx),q); end; rho=W-H;
end
function rho=quotient_orthogonal_cubic(W,q,wq)
    x=q(:); B=[ones(size(x)) x x.^2 x.^3]; G=B.'*(B.*wq); RHS=B.'*(W.'.*wq); C=G\RHS; rho=W-(B*C).';
end
function [d0,d1]=endpoint_first_derivatives(W,q)
    h=q(2)-q(1); d0=(-25*W(:,1)+48*W(:,2)-36*W(:,3)+16*W(:,4)-3*W(:,5))/(12*h);
    d1=(25*W(:,end)-48*W(:,end-1)+36*W(:,end-2)-16*W(:,end-3)+3*W(:,end-4))/(12*h);
end
function [dd0,dd1]=endpoint_second_derivatives(W,q)
    h=q(2)-q(1); dd0=(35*W(:,1)-104*W(:,2)+114*W(:,3)-56*W(:,4)+11*W(:,5))/(12*h^2);
    dd1=(35*W(:,end)-104*W(:,end-1)+114*W(:,end-2)-56*W(:,end-3)+11*W(:,end-4))/(12*h^2);
end
function [R,nrm,good]=normalize_rows(X,wq)
    nrm=sqrt(sum(abs(X).^2.*wq.',2)); good=isfinite(nrm)&nrm>1e-12; R=complex(nan(size(X))); R(good,:)=X(good,:)./nrm(good);
end
function d=finite_difference_nonuniform(ym,y0,yp,hm,hp)
    d=-(hp/(hm*(hm+hp)))*ym+(hp-hm)/(hm*hp)*y0+(hm/(hp*(hm+hp)))*yp;
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

function [Z,dZ]=transverse_matrix_with_beta_derivative(beta,t,Ncut,M,chunk)
    beta=double(beta(:)); t=double(t(:).'); nb=numel(beta); nt=numel(t); Z=complex(zeros(nb,nt)); dZ=complex(zeros(nb,nt));
    k=(1:Ncut-1).'; logk=log(k); A=exp(-beta*logk.'); Ad=-A.*logk.'; logN=log(Ncut); Bernoulli=bernoulli_even(M);
    for first=1:chunk:nt
        last=min(nt,first+chunk-1); tt=t(first:last); B=exp(-1i*logk*tt); Zb=A*B; dZb=Ad*B; S=beta+1i*tt;
        T1=exp((1-S)*logN)./(S-1); dT1=T1.*(-logN-1./(S-1)); Zb=Zb+T1; dZb=dZb+dT1;
        T2=.5*exp(-S*logN); dT2=-logN*T2; Zb=Zb+T2; dZb=dZb+dT2;
        for r=1:M
            Product=ones(size(S)); LogDerivative=zeros(size(S));
            for j=0:(2*r-2), Product=Product.*(S+j); LogDerivative=LogDerivative+1./(S+j); end
            corr=(Bernoulli(r)/factorial(2*r)).*Product.*exp(-(S+(2*r-1))*logN);
            dcorr=corr.*(LogDerivative-logN); Zb=Zb+corr; dZb=dZb+dcorr;
        end
        Z(:,first:last)=Zb; dZ(:,first:last)=dZb;
    end
end
function B=bernoulli_even(M)
    allB=[1/6;-1/30;1/42;-1/30;5/66;-691/2730;7/6;-3617/510;43867/798;-174611/330];
    if M>numel(allB), error('Increase Bernoulli table.'); end; B=allB(1:M);
end
function w=trapezoid_weights(q)
    q=q(:); h=q(2)-q(1); if max(abs(diff(q)-h))>1e-12, error('Uniform q grid required.'); end; w=h*ones(numel(q),1); w(1)=h/2; w(end)=h/2;
end
function out=row_median_finite(X)
    out=nan(size(X,1),1); for i=1:size(X,1), x=X(i,:); x=x(isfinite(x)); if ~isempty(x), out(i)=median(x); end; end
end
function save_figure_png(fig,path)
    try, exportgraphics(fig,path,'Resolution',180); catch, set(fig,'PaperPositionMode','auto'); print(fig,path,'-dpng','-r180'); end
end
