function R = mobius_surface_branches_matrixfree()
% MOBIUS_SURFACE_BRANCHES_MATRIXFREE
% Matrix-free / sparse-factor computation for the intrinsic B_N operator
%
%   D_N = (B_N J_N B_N^{-1} - (B_N J_N B_N^{-1})^*)/(2i)
%       = (A_N-A_N^*)/(2i),  A_N = K_N B_N^{-1}.
%
% The code NEVER forms A_N or D_N.  It stores only the sparse divisor
% incidence Z_N=K_N^{-1} and the sparse Mobius incidence K_N and applies
% D_N by sparse matrix products.
%
% Coordinates are indexed by integers 2,...,N.  If Z_{a,m}=1_{m|a}, then
% B_N^{-1}=J_N Z_N with J_N the lower first-difference matrix.  Therefore
%
%   A*x  = K * J * Z * x,
%   A'*x = Z' * J' * K' * x,
%
% and D*x is obtained without forming either A or D.
%
% The first truncation is solved by EIGS.  Later truncations use an adaptive
% restarted block-Davidson/Rayleigh-Ritz method initialized by zero-extension of the
% previous eigenvectors.  This is substantially faster for the persistent
% edge branches than restarting ARPACK from scratch at every doubling.
%
% OUTPUT R contains spectra, x_j^(N), exact intrinsic scale s_N, overlaps,
% old-block masses, projective exponents beta, and the frozen five-point
% predictor.  Zeta zeros are used only if COMPARE_ZETA=true, after all
% B_N spectra have been computed.
%
% Recommended first run: Nmax=262144.  Raise to 524288 or 1048576 if RAM
% permits.  For large N the one-time sparse incidence construction is the
% dominant memory cost.
%
% Victor Casana-Giner / B_N spectral experiment, August 2026.

%% ---------------- USER SETTINGS ----------------------------------------
Nlist = 2.^(13:18);              % 8192 ... 262144
kTrack = 25;                     % persistent branches carried forward
kReport = 20;                    % branches printed/analyzed
extraStart = 5;                  % random seed directions in Davidson start
maxDavidsonIter = 20;            % restarted block-Davidson iterations
ritzRelTol = 5e-8;               % relative Ritz residual target
firstEigsTol = 1e-10;
COMPARE_ZETA = true;             % only affects final comparison
SAVE_EACH_STEP = true;
outfile = 'mobius_surface_branches_results.mat';
rng(1,'twister');
%% ----------------------------------------------------------------------

Nmax = max(Nlist);
fprintf('Linear sieve to Nmax=%d ...\n',Nmax);
[mu,tau] = linear_mu_tau(Nmax);
TauSum = cumsum(tau);

nN = numel(Nlist);
lamAll = nan(kTrack,nN);
xAll = nan(kTrack,nN);
xExactAll = nan(kTrack,nN);
hAll = nan(kTrack,nN);
ritzResidual = nan(kTrack,nN);
edgeScale = nan(1,nN);
intrinsicScale = nan(1,nN);
matchOverlap = cell(1,nN);
matchAlignment = cell(1,nN);
matchMass = cell(1,nN);
matchBeta = cell(1,nN);

Vprev = [];
Nprev = [];

for it = 1:nN
    N = Nlist(it);
    n = N-1;
    fprintf('\n============================================================\n');
    fprintf('N = %d, dimension = %d\n',N,n);
    fprintf('Building sparse Z_N and K_N ...\n');
    tic;
    [Z,K] = build_ZK(N,mu);
    fprintf('  nnz(Z)=%d, nnz(K)=%d, build %.2f s\n',nnz(Z),nnz(K),toc);

    Dfun = @(X) apply_D(X,K,Z);

    if isempty(Vprev)
        fprintf('Initial EIGS solve for %d upper-edge eigenpairs ...\n',kTrack);
        opts.tol = firstEigsTol;
        opts.maxit = 5000;
        opts.p = max(4*kTrack+20,120);
        opts.issym = true;
        opts.isreal = false;
        tic;
        try
            [V,L] = eigs(Dfun,n,kTrack,'largestreal',opts);
        catch
            % Older MATLAB releases use 'lr'.  Since D is Hermitian the
            % returned eigenvalues are real up to roundoff.
            [V,L] = eigs(Dfun,n,kTrack,'lr',opts);
        end
        lam = real(diag(L));
        [lam,ord] = sort(lam,'descend');
        V = V(:,ord);
        DV = Dfun(V);
        res = vecnorm(DV - V.*reshape(lam.',1,[]),2,1).';
        fprintf('  eigs time %.2f s, max residual %.3e\n',toc,max(res));
    else
        fprintf('Persistent block-Davidson solve initialized from N=%d ...\n',Nprev);
        V0 = [Vprev; zeros(n-size(Vprev,1),size(Vprev,2),'like',Vprev)];
        tic;
        [lam,V,res,iterUsed] = restarted_block_davidson_edge( ...
            Dfun,V0,kTrack,extraStart,maxDavidsonIter,ritzRelTol);
        fprintf('  Davidson time %.2f s, iterations=%d, max relative residual %.3e\n', ...
            toc,iterUsed,max(res./max(abs(lam),1)));

        % Match the new Ritz vectors to the previous persistent branches.
        oldBlock = V(1:size(Vprev,1),:);
        O = abs(Vprev' * oldBlock).^2;
        oldMass = sum(abs(oldBlock).^2,1);
        Align = O ./ max(oldMass,realmin);
        map = greedy_max_assignment(O);

        lam = lam(map);
        V = V(:,map);
        res = res(map);
        O = O(:,map);
        Align = Align(:,map);
        oldMass = oldMass(map);

        chosenOverlap = diag(O);
        chosenAlign = diag(Align);
        beta = -0.5*log2(max(oldMass(:),realmin));
        matchOverlap{it} = chosenOverlap;
        matchAlignment{it} = chosenAlign;
        matchMass{it} = oldMass(:);
        matchBeta{it} = beta;

        fprintf('  branch  overlap       alignment     old-mass      beta\n');
        for j=1:min(kReport,kTrack)
            fprintf('  %3d   %.8f   %.8f   %.8f   %.8f\n', ...
                j,chosenOverlap(j),chosenAlign(j),oldMass(j),beta(j));
        end
        fprintf('  mean old-mass first %d = %.8f; mean beta = %.8f\n', ...
            min(10,kReport),mean(oldMass(1:min(10,kReport))), ...
            mean(beta(1:min(10,kReport))));
    end

    % Normalizations.  s_N is entirely internal to B_N because
    % s_N^2 = (1/2) tr(G_N^{-1}).
    edgeScale(it) = sqrt(N*log(N));
    trH = 2*TauSum(N) - tau(N) - 2*N + 1;
    intrinsicScale(it) = sqrt(0.5*trH);

    lamAll(:,it) = lam;
    xAll(:,it) = edgeScale(it)./lam;
    xExactAll(:,it) = intrinsicScale(it)./lam;
    ritzResidual(:,it) = res;
    hAll(:,it) = frozen_predictor(xAll(:,it));

    fprintf('  lambda_1 = %.12g\n',lam(1));
    fprintf('  lambda_1/sqrt(N log N) = %.12g\n',lam(1)/edgeScale(it));
    fprintf('  s_N/sqrt(N log N) = %.12g\n',intrinsicScale(it)/edgeScale(it));

    if it>1
        dx = xAll(:,it)-xAll(:,it-1);
        dh = hAll(:,it)-hAll(:,it-1);
        jj = 3:min(kReport-2,kTrack-2);
        fprintf('  B_N-only dyadic test on j=%d..%d:\n',jj(1),jj(end));
        fprintf('    mean delta x = %+.8e, RMS delta x = %.8e\n', ...
            mean(dx(jj),'omitnan'),rms_omitnan(dx(jj)));
        fprintf('    mean delta h = %+.8e, RMS delta h = %.8e\n', ...
            mean(dh(jj),'omitnan'),rms_omitnan(dh(jj)));
    end

    Vprev = V;
    Nprev = N;
    clear Z K Dfun DV oldBlock O Align

    if SAVE_EACH_STEP
        R = pack_results(); %#ok<NASGU>
        save(outfile,'R','-v7.3');
        fprintf('  checkpoint saved: %s\n',outfile);
    end
end

R = pack_results();

% Only after the complete B_N calculation, compare with fixed target zeros.
if COMPARE_ZETA
    gamma = first_zeta_zeros(kTrack);
    R.gamma = gamma;
    fprintf('\n================ ZETA TARGET CHECK (POST HOC) ==============\n');
    for it=1:nN
        h = hAll(:,it);
        jj = 3:min(18,kTrack-2); % j=3,...,18 in one-based branch labels
        e = h(jj)-gamma(jj);
        fprintf('N=%7d  mean error=%+.9f  RMSE=%.9f  SD=%.9f\n', ...
            Nlist(it),mean(e),sqrt(mean(e.^2)),std(e,1));
    end
end

if SAVE_EACH_STEP
    save(outfile,'R','-v7.3');
end

%% nested packer keeps the main script compact
    function S = pack_results()
        S.Nlist = Nlist;
        S.kTrack = kTrack;
        S.kReport = kReport;
        S.lambda = lamAll;
        S.x = xAll;
        S.x_intrinsic_scale = xExactAll;
        S.h_frozen = hAll;
        S.ritz_residual = ritzResidual;
        S.sqrt_N_log_N = edgeScale;
        S.s_intrinsic = intrinsicScale;
        S.match_overlap = matchOverlap;
        S.match_alignment = matchAlignment;
        S.match_old_mass = matchMass;
        S.match_beta = matchBeta;
    end
end


function [mu,tau] = linear_mu_tau(N)
% Euler/linear sieve computing Mobius mu(n) and divisor count tau(n).
lp = zeros(N,1,'uint32');
expo = zeros(N,1,'uint16');
mu = zeros(N,1,'int8');
tau = zeros(N,1);
primes = zeros(N,1,'uint32');
np = 0;
mu(1)=1; tau(1)=1;
for n=2:N
    if lp(n)==0
        lp(n)=uint32(n);
        np=np+1; primes(np)=uint32(n);
        mu(n)=-1; expo(n)=1; tau(n)=2;
    end
    lpn = double(lp(n));
    for ip=1:np
        p = double(primes(ip));
        m = p*n;
        if p>lpn || m>N, break; end
        lp(m)=uint32(p);
        if p==lpn
            mu(m)=0;
            expo(m)=expo(n)+1;
            eold=double(expo(n));
            tau(m)=tau(n)/(eold+1)*(eold+2);
            break
        else
            mu(m)=-mu(n);
            expo(m)=1;
            tau(m)=2*tau(n);
        end
    end
end
end


function [Z,K] = build_ZK(N,mu)
% Sparse divisor incidence Z=K^{-1} and Mobius incidence K.
% Rows/columns 1,...,N-1 correspond to integers 2,...,N.
n = N-1;
counts = floor(N./(2:N));
total = sum(counts);
ii = zeros(total,1);
jj = zeros(total,1);
pos=1;
for a=2:N
    rows = (a:a:N).';
    L = numel(rows);
    idx = pos:pos+L-1;
    ii(idx)=rows-1;
    jj(idx)=a-1;
    pos=pos+L;
end

% K_{n,a}=1_{a|n} mu(n/a).
q = round((ii+1)./(jj+1));
vk = double(mu(q));
K = sparse(ii,jj,vk,n,n);
clear q vk

% Z_{n,a}=1_{a|n}.  Try scalar expansion first to reduce peak memory.
try
    Z = sparse(ii,jj,1,n,n);
catch
    Z = sparse(ii,jj,ones(total,1),n,n);
end
clear ii jj
end


function Y = apply_D(X,K,Z)
% Matrix-free action of D=(A-A')/(2i), A=K*J*Z.
% Handles one vector or a block of vectors.
g = Z*X;
y = g;
y(2:end,:) = g(2:end,:)-g(1:end-1,:);       % J*g
Ax = K*y;

t = K'*X;
q = t;
q(1:end-1,:) = t(1:end-1,:)-t(2:end,:);      % J'*t
Atx = Z'*q;
Y = (-0.5i)*(Ax-Atx);
end


function [lam,V,res,iterUsed] = restarted_block_davidson_edge(Dfun,V0,k,extra,maxIter,relTol)
% Restarted block-Davidson/Krylov iteration for the largest algebraic
% eigenpairs of a Hermitian matrix-free operator.  Memory is O(n*k), not
% O(n*k*depth), which is important at N=262144 and above.
n = size(V0,1);
if extra>0
    Q = [V0, randn(n,extra)+1i*randn(n,extra)];
else
    Q = V0;
end
[Q,~]=qr(Q,0);
AQ=Dfun(Q);

for it=1:maxIter
    T=Q'*AQ;
    T=0.5*(T+T');
    [Y,theta]=eig(T,'vector');
    [theta,ord]=sort(real(theta),'descend');
    Y=Y(:,ord);
    if numel(theta)<k, error('Davidson subspace smaller than k.'); end
    lam=theta(1:k);
    Yk=Y(:,1:k);
    V=Q*Yk;
    AV=AQ*Yk;
    R=AV-V.*reshape(lam.',1,[]);
    res=vecnorm(R,2,1).';
    rel=res./max(abs(lam),1);
    fprintf('    Davidson %2d, subspace %3d, max rel residual %.3e\n', ...
        it,size(Q,2),max(rel));
    if max(rel)<relTol
        iterUsed=it;
        return
    end

    % Residual block gives the next Krylov correction.  Orthogonalize twice
    % against the current Ritz vectors, then restart in span{V,R}.
    R=R-V*(V'*R);
    R=R-V*(V'*R);
    [Qr,Rr]=qr(R,0);
    d=abs(diag(Rr));
    if isempty(d)
        nkeep=0;
    else
        nkeep=sum(d>1e-11*max(d));
    end
    nkeep=min([nkeep,k,size(Qr,2)]);
    if nkeep==0
        % Rare stagnation fallback.
        Qr=randn(n,extra)+1i*randn(n,extra);
        Qr=Qr-V*(V'*Qr);
        [Qr,~]=qr(Qr,0);
        nkeep=size(Qr,2);
    else
        Qr=Qr(:,1:nkeep);
    end
    AQr=Dfun(Qr);
    Q=[V,Qr];
    AQ=[AV,AQr];
end

iterUsed=maxIter;
warning('Requested Davidson tolerance not reached; max relative residual %.3e.', ...
    max(res./max(abs(lam),1)));
end

function map = greedy_max_assignment(O)
% One-to-one maximum-overlap assignment.  For the strongly persistent edge
% branches this gives the same matching as the Hungarian assignment while
% avoiding a Statistics Toolbox dependency.
[nr,nc]=size(O);
if nr~=nc, error('Expected square overlap matrix.'); end
n=nr;
[~,ord]=sort(O(:),'descend');
rowUsed=false(n,1); colUsed=false(n,1); map=zeros(n,1);
for z=1:numel(ord)
    [r,c]=ind2sub([n,n],ord(z));
    if ~rowUsed(r) && ~colUsed(c)
        map(r)=c; rowUsed(r)=true; colUsed(c)=true;
        if all(rowUsed), break; end
    end
end
if any(map==0), error('Assignment failed.'); end
end


function h = frozen_predictor(x)
% h_j = 2*pi(x_j-1)+2*pi*Delta^2 x_j+(4/pi)*Delta^4 x_j.
h = nan(size(x));
if numel(x)<5, return; end
d2 = nan(size(x)); d4 = nan(size(x));
d2(2:end-1) = x(3:end)-2*x(2:end-1)+x(1:end-2);
d4(3:end-2) = x(5:end)-4*x(4:end-1)+6*x(3:end-2) ...
             -4*x(2:end-3)+x(1:end-4);
jj=3:numel(x)-2;
h(jj)=2*pi*(x(jj)-1)+2*pi*d2(jj)+(4/pi)*d4(jj);
end


function r = rms_omitnan(x)
x=x(~isnan(x));
r=sqrt(mean(abs(x).^2));
end


function g = first_zeta_zeros(k)
% First 25 positive ordinates.  Used only for the final post-hoc check.
g25 = [ ...
14.134725141734693790; 21.022039638771554993; 25.010857580145688763; ...
30.424876125859513210; 32.935061587739189691; 37.586178158825671257; ...
40.918719012147495187; 43.327073280914999519; 48.005150881167159728; ...
49.773832477672302182; 52.970321477714460644; 56.446247697063394804; ...
59.347044002602353079; 60.831778524609809844; 65.112544048081606661; ...
67.079810529494173714; 69.546401711173979252; 72.067157674481907583; ...
75.704690699083933168; 77.144840068874805372; 79.337375020249367923; ...
82.910380854086030184; 84.735492980517050105; 87.425274613125229407; ...
88.809111207634465424];
if k>numel(g25)
    error('Hard-coded target list has only 25 zeros; extend it if kTrack>25.');
end
g=g25(1:k);
end
