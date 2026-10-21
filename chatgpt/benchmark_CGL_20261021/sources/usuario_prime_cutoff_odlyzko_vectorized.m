function summary = prime_cutoff_odlyzko_vectorized(overrides)
% PRIME CUTOFF VS HEIGHT: LOCAL DOUBLE-PRECISION BINARY FILES ONLY.
%
% Local inputs only. Candidate evaluation does not access true-zero values.
% Cutoff optimization uses the validation zeros explicitly.
%
% Required little-endian float64 files in the MATLAB working folder:
%   zeross.bin  (or zeross(5).bin)
%   zLamb.bin   (or zLamb(4).bin)
%   zeros3.bin, zeros4.bin, zeros5.bin
%
% zeros3/4/5 can store offsets from the documented Odlyzko base.
% zeros3 may also contain absolute doubles (with limited precision).
% Absolute doubles at 1e20+ cannot resolve individual zero gaps;
% this script explicitly rejects them.
%
% Usage (run from the folder containing the binary inputs):
%   prime_cutoff_odlyzko_vectorized
%   prime_cutoff_odlyzko_vectorized(struct('dataDir','/path/to/binaries'))
%   prime_cutoff_odlyzko_vectorized(struct('selfTest',true))
% The constructor uses primes and the RVM clock. Cutoff selection and the
% fitted laws ARE calibrated with true zeros on the validation subset.
% Outputs: cutoff_by_height.csv, cutoff_full_results.mat
% Optional: zCasanya0.bin, if cfg.writeNewClock = true.

if nargin < 1, overrides = struct(); end
assert(isstruct(overrides) && isscalar(overrides), ...
    'Configuration must be a scalar struct.');

cfg.digits = 65;
cfg.lowSample = 260;
cfg.highSample = 400;
cfg.gapSample = 120;
cfg.primeBatch = 192;
cfg.evalBlock = 4000;

cfg.lowCuts = ...
    [64 128 256 512 1024 2048 4096 8192];

cfg.highCuts3 = ...
    [512 2048 8192 32768 131072];

cfg.highCuts4 = ...
    [512 2048 8192 32768 131072];

cfg.highCuts5 = ...
    [512 2048 8192 32768 131072];

cfg.writeNewClock = false;
cfg.minimumGapFraction = 0.05;
cfg.dataDir = pwd;
cfg.outputDir = fullfile(pwd,'cutoff_vectorized_output');
cfg.selfTest = false;
cfg.phaseBatch = 256;
cfg.maxTemporaryMB = 64;
cfg.seed = 20261020;

fields = fieldnames(overrides);
for k = 1:numel(fields)
    assert(isfield(cfg,fields{k}),'Unknown configuration field: %s',fields{k});
    cfg.(fields{k}) = overrides.(fields{k});
end
integerFields = {'digits','lowSample','highSample','gapSample', ...
    'primeBatch','evalBlock','phaseBatch','seed'};
for k = 1:numel(integerFields)
    a = cfg.(integerFields{k});
    assert(isnumeric(a) && isscalar(a) && isfinite(a) && a==fix(a) && a>=1, ...
        'Invalid positive integer setting: %s',integerFields{k});
end
assert(cfg.seed<=2^32-1,'seed exceeds the MATLAB random generator range.');
assert(cfg.digits>=40 && cfg.lowSample>=4 && cfg.highSample>=4, ...
    'Use at least 40 digits and four samples per dataset.');
assert(isnumeric(cfg.maxTemporaryMB) && isscalar(cfg.maxTemporaryMB) && ...
    isfinite(cfg.maxTemporaryMB) && cfg.maxTemporaryMB>=1, ...
    'maxTemporaryMB must be at least 1.');
assert(isnumeric(cfg.minimumGapFraction) && isscalar(cfg.minimumGapFraction) && ...
    isfinite(cfg.minimumGapFraction) && cfg.minimumGapFraction>0 && ...
    cfg.minimumGapFraction<=1,'minimumGapFraction must be in (0,1].');
assert(islogical(cfg.selfTest) && isscalar(cfg.selfTest) && ...
    islogical(cfg.writeNewClock) && isscalar(cfg.writeNewClock), ...
    'selfTest and writeNewClock must be scalar logical values.');
cutFields = {'lowCuts','highCuts3','highCuts4','highCuts5'};
for k = 1:numel(cutFields)
    cuts = cfg.(cutFields{k});
    assert(isnumeric(cuts) && isreal(cuts) && isvector(cuts) && ...
        ~isempty(cuts) && all(isfinite(cuts)) && all(cuts>=8) && ...
        all(cuts==fix(cuts)) && all(diff(cuts(:))>0), ...
        'Cutoff grids must be increasing integers >=8: %s',cutFields{k});
    cfg.(cutFields{k}) = cuts(:)';
end
if cfg.selfTest
    runVerification(cfg);
    summary = table();
    return;
end
assert(isfolder(cfg.dataDir),'Input folder does not exist.');
assert(ischar(cfg.outputDir) || (isstring(cfg.outputDir) && isscalar(cfg.outputDir)), ...
    'outputDir must be a path.');
% Restore the caller's random stream after completion or error.
oldRng = rng;
rngCleanup = onCleanup(@() rng(oldRng));
rng(cfg.seed,'twister');
if ~isfolder(cfg.outputDir)
    [ok,msg] = mkdir(cfg.outputDir);
    assert(ok,'Cannot create output folder: %s',msg);
end
clockFile = fullfile(cfg.outputDir,'zCasanya0.bin');
assert(~cfg.writeNewClock || ~isfile(clockFile), ...
    'zCasanya0.bin already exists. Refusing overwrite.');

% Exact integer bases and global-index predecessors.
% Dataset position j corresponds to global zero index K+j.

H = {
    'zeros3.bin', ...
    '267653395647', ...
    '1000000000000', ...
    cfg.highCuts3;

    'zeros4.bin', ...
    '144176897509546973000', ...
    '1000000000000000000000', ...
    cfg.highCuts4;

    'zeros5.bin', ...
    '1370919909931995300000', ...
    '10000000000000000000000', ...
    cfg.highCuts5
};

%% LOAD LOW-HEIGHT DATA

fZ = findLocal(cfg.dataDir,{'zeross.bin','zeross(5).bin'});
fL = findLocal(cfg.dataDir,{'zLamb.bin','zLamb(4).bin'});

trueLow = readDoubles(fZ);
lamLow = readDoubles(fL);

assert(numel(trueLow)==numel(lamLow) && ...
       numel(trueLow)>20000, ...
       'Inconsistent low-height binary lengths.');

assert(all(diff(trueLow)>0) && ...
       all(diff(lamLow)>0), ...
       'Low-height arrays are not strictly increasing.');

N = numel(trueLow);

fprintf('LOW DATA: %d zeros, T_max=%.9f\n', ...
    N,trueLow(end));

%% AUDIT EXISTING CASANYA ARRAYS

for fn = {
    'zCasanya.bin', ...
    'zCasanya_monotona_10pctRvM.bin'
}

    if isfile(fullfile(cfg.dataDir,fn{1}))

        v = readDoubles(fullfile(cfg.dataDir,fn{1}));

        if numel(v)==N

            fprintf( ...
                '%s: RMS=%.9f, nonpositive gaps=%d\n', ...
                fn{1}, ...
                sqrt(mean((v-trueLow).^2)), ...
                nnz(diff(v)<=0));

        end

    end

end

%% REQUIRE HIGH-PRECISION PHASE ARITHMETIC

if exist('vpa','file')~=2 || exist('sym','file')~=2

    error(['Symbolic Math Toolbox is required for ' ...
           'high-height phase reduction.']);

end

%% LOW-HEIGHT WINDOWS

windows = [
       1001       8000
       8001      30000
      30001     100000
     100001     400000
     400001     800000
     800001    1300000
    1300001          N
];

windows = windows(windows(:,2)<=N & windows(:,1)<=windows(:,2),:);

Z = cell(size(windows,1)+size(H,1),1);

for b=1:size(windows,1)

    d = struct();

    d.name = sprintf('low_%d_%d', ...
        windows(b,1),windows(b,2));

    d.high = false;
    d.true = trueLow;
    d.lambert = lamLow;

    d.lo = windows(b,1);
    d.hi = windows(b,2);

    d.cuts = cfg.lowCuts;

    Z{b} = d;

end

%% LOAD ALL THREE ODLYZKO BINARY FILES

for h=1:size(H,1)

    fn = H{h,1};

    if ~isfile(fullfile(cfg.dataDir,fn))
        error('Missing required local file: %s',fn);
    end

    raw = readDoubles(fullfile(cfg.dataDir,fn));

    baseString = H{h,2};
    KString = H{h,3};

    base = str2double(baseString);

    if median(raw)>base*0.1

        if base>1e15

            error([ ...
                '%s contains absolute float64 heights near %.3e. ' ...
                'Their ULP exceeds the zero spacing. ' ...
                'Re-export the SAME zero data as float64 ' ...
                'OFFSETS from base %s.'], ...
                fn,base,baseString);

        end

        truth = raw-base;

        fprintf( ...
            '%s: converted absolute doubles to offsets.\n', ...
            fn);

    else

        truth = raw;

        fprintf( ...
            '%s: reading double offsets from base %s.\n', ...
            fn,baseString);

    end

    assert(numel(truth)>=100 && all(diff(truth)>0), ...
        '%s has too few data or nonpositive gaps.',fn);

    %% CONSTRUCT HIGH-HEIGHT RVM CLOCK

    [A,L0] = highAnchor( ...
        baseString,KString,cfg.digits);

    j = (1:numel(truth))';

    lam = (j-A)/L0;

    for it=1:4

        [res,L] = highResidual( ...
            lam,j,A,L0,base);

        lam = lam-res./L;

    end

    meanSpacing = 1/L0;

    baselineRMS = sqrt(mean((lam-truth).^2));

    fprintf([ ...
        '%s: %d zeros, base %.4e, ' ...
        'RvM RMS %.8f (%.3f spacings)\n'], ...
        fn,numel(truth),base, ...
        baselineRMS,baselineRMS/meanSpacing);

    if baselineRMS>20*meanSpacing

        error([ ...
            '%s: zero offsets, global indices, or base ' ...
            'appear inconsistent.'],fn);

    end

    d = struct();

    d.name = fn;
    d.high = true;

    d.true = truth;
    d.lambert = lam;

    d.base = base;
    d.baseString = baseString;

    d.A = A;
    d.L0 = L0;

    d.lo = 1;
    d.hi = numel(truth);

    d.cuts = H{h,4};

    Z{size(windows,1)+h} = d;

end

%% PRECOMPUTE LOW-HEIGHT PRIME BANK

B_low = primeBank( ...
    max(cfg.lowCuts),'0',cfg.digits,false,cfg.phaseBatch);

%% PREPARE RESULTS

R = struct( ...
    'name',[], ...
    'T',[], ...
    'bestX',[], ...
    'nPrimes',[], ...
    'valRMS',[], ...
    'testRMS',[], ...
    'c',[], ...
    'edge',[], ...
    'cutoffs',[], ...
    'valByX',[], ...
    'testByX',[], ...
    'gapFailures',[], ...
    'minGaps',[], ...
    'validationIndices',[],'heldOutIndices',[],'pairFirstIndices',[]);

R = repmat(R,1,numel(Z));

%% OPTIMIZE EACH HEIGHT WINDOW

for zidx=1:numel(Z)

    d = Z{zidx};

    poolSize = d.hi-d.lo+1;

    ns = min(poolSize, ...
        cfg.lowSample*(~d.high)+cfg.highSample*d.high);

    picked = d.lo-1+randperm(poolSize,ns)';

    nv = max(2,min(ns-2,round(.65*ns)));

    train = picked(1:nv);
    held = picked(nv+1:end);

    %% CONSECUTIVE PAIRS FOR GAP AUDIT

    pairPoolSize = poolSize-1;

    nPairs = min(pairPoolSize,cfg.gapSample);

    pairFirst = d.lo-1+randperm(pairPoolSize,nPairs)';

    both = reshape( ...
        [pairFirst';(pairFirst+1)'],[],1);

    cuts = d.cuts(:)';

    if d.high

        bank = primeBank( ...
            max(cuts), ...
            d.baseString, ...
            cfg.digits,true,cfg.phaseBatch);

        T = d.base+median(d.true);

    else

        bank = B_low;
        T = median(d.true(train));

    end

    fprintf('\nDATASET %-22s T=%.6e\n',d.name,T);

    % Evaluate unique indices once for validation, held-out data and pairs.
    [allIdx,~,map] = unique([train;held;both]);
    candidates = correctedGrid(d,allIdx,cuts,bank,cfg);
    nt = numel(train); nh = numel(held);
    uTrain = candidates(map(1:nt),:);
    uHeld = candidates(map(nt+(1:nh)),:);
    uPairs = candidates(map(nt+nh+(1:numel(both))),:);
    gap = uPairs(2:2:end,:)-uPairs(1:2:end,:);
    val = sqrt(mean((uTrain-d.true(train)).^2,1));
    test = sqrt(mean((uHeld-d.true(held)).^2,1));
    bad = sum(gap<=0,1);
    minGap = min(gap,[],1);
    for ci=1:numel(cuts)
        fprintf([' X=%7d primes=%6d val=%.8f test=%.8f ' ...
            'gap<=0:%3d/%d minGap=%+.7f\n'], ...
            cuts(ci),nnz(bank.primes<=cuts(ci)),val(ci),test(ci), ...
            bad(ci),nPairs,minGap(ci));
    end

    %% SELECT BEST CUTOFF BY VALIDATION

    [~,best] = min(val);

    q = struct();

    q.name = d.name;
    q.T = T;

    q.bestX = cuts(best);

    q.nPrimes = nnz( ...
        bank.primes<=cuts(best));

    q.valRMS = val(best);
    q.testRMS = test(best);

    q.c = log(q.bestX)/log(T);

    q.edge = (best==1 || best==numel(cuts));

    q.cutoffs = cuts;

    q.valByX = val;
    q.testByX = test;

    q.gapFailures = bad;
    q.minGaps = minGap;
    % Save the actual split and audit pairs for reproducibility.
    q.validationIndices = train;
    q.heldOutIndices = held;
    q.pairFirstIndices = pairFirst;

    R(zidx) = q;

    fprintf([ ...
        ' CHOSEN X=%d (%d primes); ' ...
        'held-out RMS=%.8f; edge=%d\n'], ...
        q.bestX,q.nPrimes,q.testRMS,q.edge);

end

%% FIT THE TWO CUTOFF LAWS

T = [R.T]';
bestX = [R.bestX]';
edge = [R.edge]';

valid = ~edge & T>exp(exp(1));

cFix = NaN;
cVariable = NaN;

lossFix = NaN;
lossVariable = NaN;

if nnz(valid)>=2

    Y = log(bestX(valid));

    h = log(T(valid));

    %% LAW A: X(T)=T^c

    xFix = h;

    cFix = (xFix'*Y)/(xFix'*xFix);

    %% LAW B: X(T)=T^(C/sqrt(log(log(T))))

    xVariable = h./sqrt(log(h));

    cVariable = ...
        (xVariable'*Y)/(xVariable'*xVariable);

    lossFix = sqrt(mean( ...
        (Y-cFix*xFix).^2));

    lossVariable = sqrt(mean( ...
        (Y-cVariable*xVariable).^2));

    fprintf('\nLAW A:\n');

    fprintf( ...
        'X(T)=T^(%.9g)\n',cFix);

    fprintf( ...
        'Log-cutoff fit RMS=%.7g\n',lossFix);

    fprintf('\nLAW B:\n');

    fprintf( ...
        'X(T)=T^(%.9g/sqrt(log(log(T))))\n', ...
        cVariable);

    fprintf( ...
        'Log-cutoff fit RMS=%.7g\n',lossVariable);

    %% HELD-OUT LAW COMPARISON

    fprintf('\nHELD-OUT LAW CHECK (same datasets, held-out indices):\n');

    for j=1:numel(R)

        q = R(j);

        a = exp(cFix*log(q.T));

        b = exp( ...
            cVariable*log(q.T)/ ...
            sqrt(log(log(q.T))));

        [~,ia] = min( ...
            abs(log(q.cutoffs)-log(a)));

        [~,ib] = min( ...
            abs(log(q.cutoffs)-log(b)));

        fprintf([ ...
            '%-22s ' ...
            'A: X=%7d RMS=%.8f | ' ...
            'B: X=%7d RMS=%.8f\n'], ...
            q.name, ...
            q.cutoffs(ia),q.testByX(ia), ...
            q.cutoffs(ib),q.testByX(ib));

    end

else

    fprintf('\n');
    fprintf( ...
        'Too few non-boundary optima for a reliable fit.\n');

    fprintf( ...
        'Extend the cutoff grids.\n');

end

%% EXPORT RESULTS

summary = table( ...
    string({R.name})', ...
    T, ...
    bestX, ...
    [R.nPrimes]', ...
    [R.valRMS]', ...
    [R.testRMS]', ...
    [R.c]', ...
    edge, ...
    'VariableNames',{ ...
        'Dataset', ...
        'Height', ...
        'BestCutoff', ...
        'PrimeCount', ...
        'ValidationRMS', ...
        'HeldOutRMS', ...
        'ObservedExponent', ...
        'GridBoundary'});

disp(summary);

writetable(summary,fullfile(cfg.outputDir,'cutoff_by_height.csv'));

save(fullfile(cfg.outputDir,'cutoff_full_results.mat'), ...
    'R','summary','cfg', ...
    'cFix','cVariable', ...
    'lossFix','lossVariable');

%% OPTIONAL: CREATE zCasanya0.bin

if cfg.writeNewClock

    if isfile(clockFile)

        error( ...
            'zCasanya0.bin already exists. Refusing overwrite.');

    end

    if ~isfinite(cFix) || ~isfinite(cVariable)

        error('No fitted cutoff law available.');

    end

    if lossVariable<lossFix

        law = 'variable';

    else

        law = 'fixed';

    end

    %% SELECT INDEX-DEPENDENT CUTOFF

    Tlocal = lamLow;

    if strcmp(law,'variable')

        target = exp( ...
            cVariable*log(Tlocal)./ ...
            sqrt(log(log(Tlocal))));

    else

        target = exp(cFix*log(Tlocal));

    end

    cuts = cfg.lowCuts(:)';

    [~,which] = min( ...
        abs(log(target(:))-log(cuts)),[],2);

    d = struct('lambert',lamLow,'high',false); % No truth in constructor.

    clock = zeros(N,1);

    %% BUILD COMPLETE CLOCK WITH VALIDATION-CALIBRATED CUTOFFS

    for ci=1:numel(cuts)

        ix = find(which==ci);

        for st=1:cfg.evalBlock:numel(ix)

            sub = ix( ...
                st:min(st+cfg.evalBlock-1,numel(ix)));

            clock(sub) = correctedGrid(d,sub,cuts(ci),B_low,cfg);

        end

    end

    gapsBefore = nnz(diff(clock)<=0);

    %% EXPLICIT MINIMUM-GAP PROJECTION

    clock = monotoneProject( ...
        clock,lamLow,cfg.minimumGapFraction);

    %% WRITE BINARY

    assert(all(isfinite(clock)) && all(diff(clock)>0), ...
        'Projected clock is not finite and strictly increasing.');
    fid = fopen(clockFile,'wb','ieee-le');
    assert(fid>=0,'Cannot create zCasanya0.bin');
    fileCleanup = onCleanup(@() fclose(fid));
    written = fwrite(fid,clock,'double');
    assert(written==N,'Incomplete clock write.');
    clear fileCleanup;

    fprintf('\n');
    fprintf( ...
        'zCasanya0.bin: law=%s\n',law);

    fprintf( ...
        'RMS=%.9f\n', ...
        sqrt(mean((clock-trueLow).^2)));

    fprintf( ...
        'Nonpositive gaps: %d -> %d\n', ...
        gapsBefore,nnz(diff(clock)<=0));

    fprintf( ...
        'Minimum gap=%.10f\n', ...
        min(diff(clock)));

    fprintf( ...
        '%d double values written.\n',N);

end

end

%% =========================================================
% SUPPORTING FUNCTIONS
% ==========================================================

function fn=findLocal(folder,names)

for j=1:numel(names)

    if isfile(fullfile(folder,names{j}))
        fn=fullfile(folder,names{j});
        return;
    end

end

error( ...
    'Missing local binary file: %s', ...
    strjoin(names,' or '));

end

function x=readDoubles(fn)

info = dir(fn);
assert(isscalar(info) && mod(info.bytes,8)==0 && info.bytes>0, ...
    'Binary file must contain complete float64 records: %s',fn);
fid=fopen(fn,'rb','ieee-le');

assert(fid>=0,'Cannot open %s',fn);

c=onCleanup(@()fclose(fid));

x=fread(fid,Inf,'double=>double');

assert(numel(x)==info.bytes/8 && all(isfinite(x)), ...
    'Invalid data in %s',fn);

x=x(:);

end

%% =========================================================
% HIGH-PRECISION RVM ANCHOR
% ==========================================================

function [A,L0]=highAnchor(baseString,KString,D)

old=digits;

cleanup=onCleanup(@()digits(old));

digits(D);

B=vpa(sym(baseString),D);

K=vpa(sym(KString),D);

P=vpa(sym('pi'),D);

N0=B/(2*P)*(log(B/(2*P))-1) ...
    +vpa(sym(7)/8,D);

A=double( ...
    N0-(K-vpa(sym(1)/2,D)));

L0=double( ...
    log(B/(2*P))/(2*P));

end

%% =========================================================
% STABLE RVM RESIDUAL AT HIGH HEIGHT
% ==========================================================

function [r,L]=highResidual(u,j,A,L0,B)

% Expand N0(B+u) without forming the absolute
% height B+u as a float64 number.

r=A+L0*u ...
    +u.^2/(4*pi*B) ...
    -u.^3/(12*pi*B^2) ...
    -j;

L=L0+log1p(u/B)/(2*pi);

end

%% =========================================================
% PRIME-POWER BANK
% ==========================================================

function bank=primeBank(Xmax,baseString,D,high,phaseBatch)
% Vectorize over primes; retain small loops over exponents and phase blocks.
ps = primes(Xmax)';
lp = log(ps);
ph = zeros(size(ps));
if high
    old = digits;
    cleanup = onCleanup(@() digits(old));
    digits(D);
    BS = vpa(sym(baseString),D);
    twoP = 2*vpa(sym('pi'),D);
    fprintf('High-precision phases: %d primes, base=%s\n',numel(ps),baseString);
    for a=1:phaseBatch:numel(ps)
        ix = a:min(a+phaseBatch-1,numel(ps));
        th = vpa(BS*log(vpa(sym(ps(ix)),D)),D);
        ph(ix) = double(vpa(th-twoP.*floor(th./twoP),D));
    end
end
mMax = floor(log2(Xmax));
terms = cell(mMax,1);
for m=1:mMax
    power = round(ps.^m);
    keep = power<=Xmax;
    terms{m} = [power(keep),m*lp(keep), ...
        ps(keep).^(-m/2)/(pi*m),m*ph(keep)];
end
terms = vertcat(terms{:});
terms = sortrows(terms,1);
bank = struct('n',terms(:,1),'omega',terms(:,2), ...
    'amp',terms(:,3),'phase',terms(:,4),'primes',ps);
end

function Y=correctedGrid(d,idx,cuts,bank,cfg)
% Two shared steps, then all third-step cutoffs in one prefix-sum pass.
idx = idx(:);
Y = zeros(numel(idx),numel(cuts));
% Conservative allowance for four point-by-prime double temporaries.
rows = max(1,min(cfg.evalBlock, ...
    floor(cfg.maxTemporaryMB*1024^2/(32*cfg.primeBatch))));
for a=1:rows:numel(idx)
    ix = a:min(a+rows-1,numel(idx));
    j = idx(ix);
    y = d.lambert(j);
    for it=1:2
        S = primeSumGrid(y,8,bank,cfg.primeBatch);
        [res,L] = clockResidual(d,y,j);
        y = y-(res+S)./L;
    end
    [res,L] = clockResidual(d,y,j);
    S = primeSumGrid(y,cuts,bank,cfg.primeBatch);
    block = y-(res+S)./L;
    assert(isreal(block) && all(isfinite(block(:))), ...
        'Prime-corrected Newton iteration failed.');
    if ~d.high
        assert(all(block(:)>2*pi),'Low-height iterate left the clock domain.');
    end
    Y(ix,:) = block;
end
end

function [res,L]=clockResidual(d,y,j)
assert(isreal(y) && all(isfinite(y)),'Invalid Newton iterate.');
if d.high
    assert(all(y>-d.base),'High-height iterate left the clock domain.');
    [res,L] = highResidual(y,double(j),d.A,d.L0,d.base);
else
    assert(all(y>2*pi),'Low-height iterate left the clock domain.');
    res = y/(2*pi).*(log(y/(2*pi))-1)+7/8-(double(j)-.5);
    L = log(y/(2*pi))/(2*pi);
end
assert(all(isfinite(res)) && all(isfinite(L)) && all(L>0), ...
    'Invalid clock residual or nonpositive slope.');
end

function S=primeSumGrid(u,cuts,bank,batch)
u = u(:);
cuts = cuts(:)';
S = zeros(numel(u),numel(cuts));
last = sum(bank.n<=cuts,1);
if isempty(u) || ~any(last), return; end
running = zeros(numel(u),1);
for a=1:batch:max(last)
    ix = a:min(max(last),a+batch-1);
    theta = u*bank.omega(ix)'+bank.phase(ix)';
    prefix = cumsum(-sin(theta).*bank.amp(ix)',2);
    hit = find(last>=a & last<=ix(end));
    if ~isempty(hit)
        S(:,hit) = running+prefix(:,last(hit)-a+1);
    end
    running = running+prefix(:,end);
end
end

%% =========================================================
% THREE-STEP PRIME-CORRECTED CLOCK
% ==========================================================

function y=correctedClock(d,idx,X,bank,batch)

idx=idx(:);

y=d.lambert(idx);

for cut=[8 8 X]

    S=primeSum(y,cut,bank,batch);

    if d.high

        [res,L]=highResidual( ...
            y,double(idx), ...
            d.A,d.L0,d.base);

    else

        N0=y/(2*pi).* ...
            (log(y/(2*pi))-1)+7/8;

        res=N0-(double(idx)-.5);

        L=log(y/(2*pi))/(2*pi);

    end

    y=y-(res+S)./L;

end

if any(~isfinite(y))

    error( ...
        'Prime-corrected Newton iteration failed.');

end

end

%% =========================================================
% PRIME-POWER SUM
% ==========================================================

function S=primeSum(u,X,bank,batch)

u=u(:);

S=zeros(numel(u),1);

last=find(bank.n<=X,1,'last');

if isempty(last)
    return;
end

for a=1:batch:last

    j=a:min(last,a+batch-1);

    theta=bsxfun( ...
        @plus, ...
        u*bank.omega(j)', ...
        bank.phase(j)');

    S=S-sin(theta)*bank.amp(j);

end

end

%% =========================================================
% OPTIONAL MONOTONE PROJECTION
% ==========================================================

function y=monotoneProject(x,reference,alpha)

% Pool-adjacent-violators projection:
%
% Minimize sum((y-x).^2)
%
% subject to
%
% y(k+1)-y(k) >=
% alpha*(reference(k+1)-reference(k)).
%
% Does not access true zeros.

u=x(:)-alpha*reference(:);

n=numel(u);

level=zeros(n,1);

weight=zeros(n,1);

first=zeros(n,1);

last=zeros(n,1);

m=0;

for i=1:n

    m=m+1;

    level(m)=u(i);

    weight(m)=1;

    first(m)=i;

    last(m)=i;

    while m>1 && level(m-1)>level(m)

        w=weight(m-1)+weight(m);

        level(m-1)= ...
            (weight(m-1)*level(m-1) ...
            +weight(m)*level(m))/w;

        weight(m-1)=w;

        last(m-1)=last(m);

        m=m-1;

    end

end

v=zeros(n,1);

for i=1:m

    v(first(i):last(i))=level(i);

end

y=v+alpha*reference(:);

end

function runVerification(cfg)
% Regression tests against the original three-step implementation.
cuts = [8 9 16 64 512 1024];
bank = primeBank(max(cuts),'0',cfg.digits,false,cfg.phaseBatch);
% Independently enumerate prime powers to check exact inclusion at boundaries.
referenceN = [];
for p=primes(max(cuts))
    q=p;
    while q<=max(cuts)
        referenceN(end+1,1)=q; %#ok<AGROW>
        q=q*p;
    end
end
assert(isequal(bank.n,sort(referenceN)),'Prime-power bank mismatch.');
u = [0;14.2;12345.678;1132490.7];
worstSum = 0;
for batch=[1 7 192 10000]
    fast = primeSumGrid(u,cuts,bank,batch);
    for ci=1:numel(cuts)
        slow = primeSum(u,cuts(ci),bank,batch);
        err = max(abs(fast(:,ci)-slow));
        worstSum = max(worstSum,err);
        assert(err<1e-11,'Prefix sum disagrees with original summation.');
    end
end
assert(isequal(size(primeSumGrid([],cuts,bank,7)),[0 numel(cuts)]));
assert(all(primeSumGrid(u,1,bank,7)==0));
% Construct RVM starting points from indices without reading true zeros.
j = [1;2;1001;100001;2001052];
t = max(14,2*pi*j./max(1,log(j+1)));
for it=1:20
    f = t/(2*pi).*(log(t/(2*pi))-1)+7/8-(j-.5);
    t = t-f./(log(t/(2*pi))/(2*pi));
end
d = struct('high',false,'lambert',zeros(max(j),1));
d.lambert(j)=t;
cfg.evalBlock=2; cfg.primeBatch=7;
fast = correctedGrid(d,j,cuts,bank,cfg);
worstClock=0;
for ci=1:numel(cuts)
    slow = correctedClock(d,j,cuts(ci),bank,cfg.primeBatch);
    err=max(abs(fast(:,ci)-slow));
    worstClock=max(worstClock,err);
    assert(err<1e-8,'Vectorized clock disagrees with original clock.');
end
assert(isequal(size(correctedGrid(d,[],cuts,bank,cfg)),[0 numel(cuts)]));
% Three high anchors and vector/scalar symbolic phase reduction.
if exist('sym','file')==2 && exist('vpa','file')==2
    bases={'267653395647','144176897509546973000','1370919909931995300000'};
    indices={'1000000000000','1000000000000000000000','10000000000000000000000'};
    worstPhase=0;
    for h=1:3
        B=str2double(bases{h});
        [A,L0]=highAnchor(bases{h},indices{h},cfg.digits);
        jh=(1:100)';
        lam=(jh-A)/L0;
        for it=1:4
            [res,L]=highResidual(lam,jh,A,L0,B);
            lam=lam-res./L;
        end
        dh=struct('high',true,'base',B,'A',A,'L0',L0,'lambert',lam);
        bh=primeBank(64,bases{h},cfg.digits,true,7);
        old=digits;
        digitCleanup=onCleanup(@() digits(old));
        digits(cfg.digits);
        twoP=2*vpa(sym('pi'),cfg.digits);
        for k=1:numel(bh.primes)
            p=bh.primes(k);
            theta=vpa(sym(bases{h}),cfg.digits)*log(vpa(sym(p),cfg.digits));
            scalarPhase=double(theta-twoP*floor(theta/twoP));
            ix=find(bh.n==p,1);
            e=abs(bh.phase(ix)-scalarPhase);
            worstPhase=max(worstPhase,e);
            assert(e<1e-13,'Symbolic vector phase disagrees with scalar phase.');
        end
        clear digitCleanup;
        ch=[8 16 64];
        fh=correctedGrid(dh,jh,ch,bh,cfg);
        for k=1:numel(ch)
            sh=correctedClock(dh,jh,ch(k),bh,cfg.primeBatch);
            e=max(abs(fh(:,k)-sh));
            worstClock=max(worstClock,e);
            assert(e<1e-8,'High clock disagrees with original clock.');
        end
    end
    fprintf('High-anchor and phase tests passed; max phase error %.3g rad.\n',worstPhase);
else
    fprintf('High-anchor tests skipped: Symbolic Math Toolbox unavailable.\n');
end
% PAVA has a sequential dependency and is deliberately retained.
x=[3;1;2;0;5]; ref=(1:5)'; alpha=.05;
y=monotoneProject(x,ref,alpha);
expected=[1.5;1.5;1.5;1.5;5]-alpha*[1.5;.5;-.5;-1.5;0];
assert(max(abs(y-expected))<1e-12,'PAVA regression failed.');
assert(all(diff(y)>=alpha*diff(ref)-1e-12),'Minimum-gap constraint failed.');
assert(max(abs(monotoneProject(ref,ref,alpha)-ref))<1e-12);
% A truncated float64 record must fail, not silently disappear.
fn=tempname;
fid=fopen(fn,'wb'); assert(fid>=0); fwrite(fid,1,'uint8'); fclose(fid);
tempCleanup=onCleanup(@() delete(fn));
caught=false;
try
    readDoubles(fn);
catch
    caught=true;
end
assert(caught,'Truncated binary was accepted.');
fprintf('SELF TEST PASSED: max sum error %.3g; max clock error %.3g.\n', ...
    worstSum,worstClock);
end
