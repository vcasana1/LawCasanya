function prime_cutoff_odlyzko_local()
% PRIME CUTOFF EXPERIMENT - LOCAL FILES, NO DOWNLOADS.
%
% Place this file in the MATLAB working directory, alongside:
%   zeross.bin (or zeross(5).bin)
%   zLamb.bin  (or zLamb(4).bin)
%   zeros3.bin, zeros4.bin, zeros5.bin
% Optional: zCasanya.bin
%
% Every binary must be little-endian IEEE 754 double (float64).
% At heights ~1e20 and above, Odlyzko binaries MUST store offsets
% from the bases below, not absolute ordinates: absolute doubles
% cannot represent individual zero gaps there.
%
% Clock: three prime-power corrections [8,8,X]. Here X is a
% prime-power cutoff, NOT the number of primes.
%
% Synthetic candidates use only RvM, their indices and primes.
% True zeros are used only to select cutoffs and evaluate accuracy.
%
% Outputs:
%   cutoff_by_height.csv
%   cutoff_full_results.mat
%   zCasanya0.bin (optional, if construction enabled)
%
% High-height prime phases require Symbolic Math Toolbox.

clc;
rng(20261020);

%% SETTINGS
cfg.precisionDigits = 75;
cfg.lowSample = 300;
cfg.highSample = 400;
cfg.pairSample = 180;
cfg.primeBatch = 160;
cfg.outputBatch = 1500;
cfg.lowCuts = [128 512 2048 8192];
cfg.highCuts3 = [512 2048 8192 32768 131072];
cfg.highCuts4 = [512 2048 8192 32768];
cfg.highCuts5 = [512 2048 8192 32768];
% Increase cfg.highCuts3 to include 517352 if desired: this is slow.
cfg.createBinary = true;
cfg.gapFraction = 0.10;

%% LOW-HEIGHT INPUTS
fileZeros = findRequiredFile({'zeross.bin','zeross(5).bin'});
fileLamb = findRequiredFile({'zLamb.bin','zLamb(4).bin'});
truthLow = readDoubleFile(fileZeros);
lamLow = readDoubleFile(fileLamb);
N = numel(truthLow);
assert(N == numel(lamLow) && N >= 10001, ...
    'Inconsistent lengths for low-height binaries.');
assert(all(diff(truthLow)>0), ...
    'zeross binary is not strictly increasing.');
assert(all(diff(lamLow)>0), ...
    'zLamb binary is not strictly increasing.');

fprintf('LOW ZEROS: %d, maximum ordinate %.9f\n',N,truthLow(end));
fprintf('LAMBERT RMS: %.10f\n',sqrt(mean((lamLow-truthLow).^2)));

fileOld = findOptionalFile({'zCasanya.bin'});
if ~isempty(fileOld)
    old = readDoubleFile(fileOld);
    if numel(old)==N
        fprintf('OLD CASANYA: RMS %.10f, nonpositive gaps %d\n', ...
            sqrt(mean((old-truthLow).^2)),nnz(diff(old)<=0));
    end
end

%% DEFINE DATASETS WITHOUT DYNAMIC ARRAY GROWTH
lowWindows = [
    1001,8000;
    8001,30000;
    30001,100000;
    100001,400000;
    400001,800000;
    800001,1300000;
    1300001,N
];
lowWindows = lowWindows(lowWindows(:,2)<=N,:);
H = {
    'zeros3.bin','267653395647','1000000000000',cfg.highCuts3;
    'zeros4.bin','144176897509546973000', ...
        '1000000000000000000000',cfg.highCuts4;
    'zeros5.bin','1370919909931995300000', ...
        '10000000000000000000000',cfg.highCuts5
};
datasets = cell(size(lowWindows,1)+size(H,1),1);
nData = 0;
for b=1:size(lowWindows,1)
    d = struct();
    d.name = sprintf('low_%d_%d',lowWindows(b,1),lowWindows(b,2));
    d.high = false;
    d.truth = truthLow;
    d.lambert = lamLow;
    d.first = lowWindows(b,1);
    d.last = lowWindows(b,2);
    d.cutoffs = cfg.lowCuts;
    nData = nData+1;
    datasets{nData} = d;
end

%% HIGH-HEIGHT BINARIES
hasSymbolic = (exist('sym','file')==2 && exist('vpa','file')==2);
for b=1:size(H,1)
    name = H{b,1};
    filename = findOptionalFile({name});
    if isempty(filename)
        fprintf('HIGH FILE NOT FOUND: %s (skipped)\n',name);
        continue;
    end
    if ~hasSymbolic
        fprintf('HIGH FILE SKIPPED: Symbolic Math Toolbox required: %s\n',name);
        continue;
    end

    raw = readDoubleFile(filename);
    baseString = H{b,2};
    indexString = H{b,3};
    B = str2double(baseString);

    if median(abs(raw))>0.10*B
        if B>1e15
            fprintf(['INVALID HIGH FILE %s: absolute float64 values at this ' ...
                'height lose individual spacings. Re-export as offsets ' ...
                'from base %s.\n'],name,baseString);
            continue;
        end
        trueOffsets = raw-B;
        fprintf('%s: converted absolute float64 ordinates to offsets.\n',name);
    else
        trueOffsets = raw;
        fprintf('%s: reading float64 offsets.\n',name);
    end

    if numel(trueOffsets)<100 || any(diff(trueOffsets)<=0)
        fprintf('INVALID HIGH FILE %s: too few zeros or gaps <= 0.\n',name);
        continue;
    end

    % Exact high-height anchor: j corresponds to global index K+j.
    [A,L0] = rvmAnchor(baseString,indexString,cfg.precisionDigits);
    jLocal = (1:numel(trueOffsets))';
    baseClock = (jLocal-A)/L0;
    for iteration=1:5
        [residual,slope] = rvmHighResidual(baseClock,jLocal,A,L0,B);
        baseClock = baseClock-residual./slope;
    end
    baselineRMS = sqrt(mean((baseClock-trueOffsets).^2));
    meanSpacing = 1/L0;
    fprintf('%s: %d zeros, RvM RMS %.8f, mean spacing %.8f\n', ...
        name,numel(trueOffsets),baselineRMS,meanSpacing);

    % Reject an incompatible base, index, format or zero block.
    if ~isfinite(baselineRMS) || baselineRMS>4*meanSpacing
        fprintf(['SKIPPING %s: incompatible base/index/offset metadata. ' ...
            'No cutoff fit will be produced for this dataset.\n'],name);
        continue;
    end

    d = struct();
    d.name = name;
    d.high = true;
    d.truth = trueOffsets;
    d.lambert = baseClock;
    d.first = 1;
    d.last = numel(trueOffsets);
    d.cutoffs = H{b,4};
    d.baseString = baseString;
    d.base = B;
    d.A = A;
    d.L0 = L0;
    nData = nData+1;
    datasets{nData} = d;
end
datasets = datasets(1:nData);

%% CONSTRUCT LOW-HEIGHT PRIME BANK ONCE
lowBank = buildPrimeBank(max(cfg.lowCuts),'0',false,cfg.precisionDigits);

%% DATASET EXPERIMENT - PREALLOCATED RESULTS
blank = struct('name','','height',NaN,'bestCutoff',NaN, ...
    'primeCount',NaN,'selectionRMS',NaN,'testRMS',NaN, ...
    'observedExponent',NaN,'boundary',false, ...
    'cutoffs',[],'allSelectionRMS',[],'allTestRMS',[], ...
    'sampledBadGaps',[],'sampledMinGaps',[]);
R = repmat(blank,nData,1);

for datasetNumber=1:nData
    d = datasets{datasetNumber};
    population = (d.first:d.last)';
    if d.high
        sampleCount = min(cfg.highSample,numel(population));
    else
        sampleCount = min(cfg.lowSample,numel(population));
    end
    selected = population(randperm(numel(population),sampleCount));
    selectionCount = max(2,min(sampleCount-2,floor(0.65*sampleCount)));
    selectionIndices = selected(1:selectionCount);
    heldoutIndices = selected(selectionCount+1:end);

    pairPopulation = (d.first:d.last-1)';
    pairCount = min(cfg.pairSample,numel(pairPopulation));
    pairFirst = pairPopulation(randperm(numel(pairPopulation),pairCount));
    pairFirst = sort(pairFirst);
    pairIndices = reshape([pairFirst'; (pairFirst+1)'],[],1);

    cuts = d.cutoffs;
    if d.high
        bank = buildPrimeBank(max(cuts),d.baseString,true,cfg.precisionDigits);
        height = d.base+median(d.truth);
    else
        bank = lowBank;
        height = median(d.truth(selectionIndices));
    end
    selectionRMS = zeros(size(cuts));
    heldoutRMS = zeros(size(cuts));
    badGaps = zeros(size(cuts));
    minimumGaps = zeros(size(cuts));
    fprintf('\nDATASET %s; T approximately %.9e\n',d.name,height);

    for cutNumber=1:numel(cuts)
        X = cuts(cutNumber);
        ySelection = correctedPrimeClock(d,selectionIndices,X,bank,cfg.primeBatch);
        yHeldout = correctedPrimeClock(d,heldoutIndices,X,bank,cfg.primeBatch);
        yPairs = correctedPrimeClock(d,pairIndices,X,bank,cfg.primeBatch);
        gaps = yPairs(2:2:end)-yPairs(1:2:end);
        selectionRMS(cutNumber) = sqrt(mean( ...
            (ySelection-d.truth(selectionIndices)).^2));
        heldoutRMS(cutNumber) = sqrt(mean( ...
            (yHeldout-d.truth(heldoutIndices)).^2));
        badGaps(cutNumber) = nnz(gaps<=0);
        minimumGaps(cutNumber) = min(gaps);
        fprintf([' X=%7d  primes=%6d  select=%.9f  test=%.9f  ' ...
            'bad sampled gaps=%d/%d  minimum=%.8f\n'], ...
            X,nnz(bank.primeList<=X),selectionRMS(cutNumber), ...
            heldoutRMS(cutNumber),badGaps(cutNumber),pairCount, ...
            minimumGaps(cutNumber));
    end

    [~,best] = min(selectionRMS);
    q = blank;
    q.name = d.name;
    q.height = height;
    q.bestCutoff = cuts(best);
    q.primeCount = nnz(bank.primeList<=cuts(best));
    q.selectionRMS = selectionRMS(best);
    q.testRMS = heldoutRMS(best);
    q.observedExponent = log(q.bestCutoff)/log(height);
    q.boundary = (best==1 || best==numel(cuts));
    q.cutoffs = cuts;
    q.allSelectionRMS = selectionRMS;
    q.allTestRMS = heldoutRMS;
    q.sampledBadGaps = badGaps;
    q.sampledMinGaps = minimumGaps;
    R(datasetNumber) = q;
    fprintf(' CHOSEN X=%d; held-out RMS=%.9f; boundary=%d\n', ...
        q.bestCutoff,q.testRMS,q.boundary);
end

%% COMPARE CUTOFF LAWS
heights = [R.height]';
chosenCuts = [R.bestCutoff]';
onBoundary = [R.boundary]';
fitMask = ~onBoundary & heights>exp(exp(1));
provisional = false;
if nnz(fitMask)<2
    provisional = true;
    fitMask = heights>exp(exp(1));
    fprintf('\nWARNING: cutoff law fit includes boundary optima.\n');
end
cFixed = NaN;
cVariable = NaN;
lossFixed = NaN;
lossVariable = NaN;
chosenLaw = 'none';

if nnz(fitMask)>=2
    t = log(heights(fitMask));
    target = log(chosenCuts(fitMask));
    fixedPredictor = t;
    variablePredictor = t./sqrt(log(t));
    cFixed = (fixedPredictor'*target)/(fixedPredictor'*fixedPredictor);
    cVariable = (variablePredictor'*target)/(variablePredictor'*variablePredictor);
    lossFixed = sqrt(mean((target-cFixed*fixedPredictor).^2));
    lossVariable = sqrt(mean((target-cVariable*variablePredictor).^2));
    if lossVariable<lossFixed
        chosenLaw = 'variable';
    else
        chosenLaw = 'fixed';
    end
    fprintf('\nFIXED LAW:    X(T)=T^(%.9f); fit log-RMS %.7f\n', ...
        cFixed,lossFixed);
    fprintf('VARIABLE LAW: X(T)=T^(%.9f/sqrt(log(log(T)))); fit log-RMS %.7f\n', ...
        cVariable,lossVariable);
    fprintf('BEST DESCRIPTIVE LAW: %s\n',chosenLaw);
    if provisional
        fprintf('WARNING: descriptive law is provisional (grid boundaries).\n');
    end
    fprintf('\nHELD-OUT EVALUATION OF BOTH CUTOFF LAWS\n');
    for rNumber=1:nData
        q = R(rNumber);
        predictedFixed = cFixed*log(q.height);
        predictedVariable = cVariable*log(q.height)/sqrt(log(log(q.height)));
        [~,jFixed] = min(abs(log(q.cutoffs)-predictedFixed));
        [~,jVariable] = min(abs(log(q.cutoffs)-predictedVariable));
        fprintf('%s  fixed X=%d RMS=%.9f; variable X=%d RMS=%.9f\n', ...
            q.name,q.cutoffs(jFixed),q.allTestRMS(jFixed), ...
            q.cutoffs(jVariable),q.allTestRMS(jVariable));
    end
else
    fprintf('Not enough height blocks for a cutoff-law fit.\n');
end

%% SAVE REPORTS
names = cell(nData,1);
for rNumber=1:nData
    names{rNumber} = R(rNumber).name;
end
summary = table(names,heights,chosenCuts,[R.primeCount]', ...
    [R.selectionRMS]',[R.testRMS]',[R.observedExponent]',onBoundary, ...
    'VariableNames',{'Dataset','Height','BestPrimePowerCutoff', ...
    'PrimeCount','SelectionRMS','HeldoutRMS','Exponent','BoundaryOptimum'});
disp(summary);
writetable(summary,'cutoff_by_height.csv');
save('cutoff_full_results.mat','R','summary','cfg', ...
    'cFixed','cVariable','lossFixed','lossVariable','chosenLaw');

%% OPTIONAL COMPLETE NEW LOW-HEIGHT BIN
if cfg.createBinary
    if strcmp(chosenLaw,'none')
        fprintf('zCasanya0.bin not generated: no fitted law.\n');
    elseif isfile('zCasanya0.bin')
        fprintf('zCasanya0.bin already exists; it will NOT be overwritten.\n');
    else
        if strcmp(chosenLaw,'variable')
            targetLogX = cVariable*log(lamLow)./sqrt(log(log(lamLow)));
        else
            targetLogX = cFixed*log(lamLow);
        end
        choices = cfg.lowCuts;
        targetLogX = max(log(min(choices)), ...
            min(log(max(choices)),targetLogX));
        [~,cutIndex] = min(abs(bsxfun(@minus, ...
            targetLogX,log(choices))),[],2);
        candidate = zeros(N,1);
        lowData = datasets{1};
        lowData.lambert = lamLow;
        for cutNumber=1:numel(choices)
            ids = find(cutIndex==cutNumber);
            fprintf('Generating %d points at cutoff %d\n', ...
                numel(ids),choices(cutNumber));
            for first=1:cfg.outputBatch:numel(ids)
                last = min(first+cfg.outputBatch-1,numel(ids));
                subgroup = ids(first:last);
                candidate(subgroup) = correctedPrimeClock( ...
                    lowData,subgroup,choices(cutNumber),lowBank,cfg.primeBatch);
            end
        end
        originalBadGaps = nnz(diff(candidate)<=0);
        zNew = projectToPositiveGaps(candidate,lamLow,cfg.gapFraction);
        newBadGaps = nnz(diff(zNew)<=0);
        assert(newBadGaps==0, ...
            'Monotone projection failed to produce strictly positive gaps.');
        fprintf('NEW CLOCK: gaps <=0: %d -> %d\n',originalBadGaps,newBadGaps);
        fprintf('NEW CLOCK: minimum gap %.10f\n',min(diff(zNew)));
        fprintf('NEW CLOCK: RMS versus known zeros %.10f\n', ...
            sqrt(mean((zNew-truthLow).^2)));
        fid = fopen('zCasanya0.bin','w','ieee-le');
        assert(fid>0,'Cannot write zCasanya0.bin.');
        written = fwrite(fid,zNew,'double');
        fclose(fid);
        assert(written==N,'Incomplete zCasanya0.bin output.');
        fprintf('Saved zCasanya0.bin: %d doubles.\n',N);
    end
end
fprintf('\nEXPERIMENT COMPLETE.\n');
end

%% SUPPORT FUNCTIONS
function filename = findRequiredFile(names)
filename = findOptionalFile(names);
if isempty(filename)
    error('Required binary not found: %s',strjoin(names,', '));
end
end

function filename = findOptionalFile(names)
filename = '';
roots = {pwd,fullfile(getenv('HOME'),'Documents','MATLAB')};
for r=1:numel(roots)
    for j=1:numel(names)
        candidate = fullfile(roots{r},names{j});
        if exist(candidate,'file')==2
            filename = candidate;
            return;
        end
    end
end
end

function values = readDoubleFile(filename)
info = dir(filename);
assert(~isempty(info) && mod(info.bytes,8)==0, ...
    'Input binary has an invalid float64 byte length: %s',filename);
fid = fopen(filename,'r','ieee-le');
assert(fid>0,'Cannot read file: %s',filename);
values = fread(fid,Inf,'double=>double');
fclose(fid);
assert(~isempty(values) && all(isfinite(values)), ...
    'Binary contains empty, NaN or Inf values: %s',filename);
values = values(:);
end

function [A,L0] = rvmAnchor(baseString,indexString,D)
oldDigits = digits;
digits(D);
B = vpa(sym(baseString),D);
K = vpa(sym(indexString),D);
p = vpa(sym('pi'),D);
N0 = B/(2*p)*(log(B/(2*p))-1)+vpa(sym(7)/8,D);
A = double(N0-K+vpa(sym(1)/2,D));
L0 = double(log(B/(2*p))/(2*p));
digits(oldDigits);
end

function [residual,slope] = rvmHighResidual(offset,j,A,L0,B)
% Avoid adding an offset to an enormous double base.
residual = A+L0*offset + offset.^2/(4*pi*B) ...
    -offset.^3/(12*pi*B^2) - j;
slope = L0+log1p(offset/B)/(2*pi);
end

function bank = buildPrimeBank(Xmax,baseString,high,D)
primeList = double(primes(Xmax));
maxTerms = numel(primeList)*(ceil(log(Xmax)/log(2))+1);
primePowers = zeros(maxTerms,1);
frequencies = zeros(maxTerms,1);
weights = zeros(maxTerms,1);
phases = zeros(maxTerms,1);
if high
    oldDigits = digits;
    digits(D);
    B = vpa(sym(baseString),D);
    twoPi = 2*vpa(sym('pi'),D);
    fprintf('High-precision phase reduction: %d primes (base %s)\n', ...
        numel(primeList),baseString);
end
nTerms = 0;
for j=1:numel(primeList)
    p = primeList(j);
    if high
        th = B*log(vpa(sym(p),D));
        th = th-twoPi*floor(th/twoPi);
        basePhase = double(th);
    else
        basePhase = 0;
    end
    power = p;
    m = 1;
    while power<=Xmax
        nTerms = nTerms+1;
        primePowers(nTerms) = power;
        frequencies(nTerms) = m*log(p);
        weights(nTerms) = p^(-m/2)/(pi*m);
        phases(nTerms) = m*basePhase;
        power = power*p;
        m = m+1;
    end
    if high && mod(j,5000)==0
        fprintf('  Completed %d of %d primes\n',j,numel(primeList));
    end
end
if high
    digits(oldDigits);
end
[sortedPowers,order] = sort(primePowers(1:nTerms));
bank.primePowers = sortedPowers;
bank.frequencies = frequencies(order);
bank.weights = weights(order);
bank.phases = phases(order);
bank.primeList = primeList;
end

function y = correctedPrimeClock(d,indices,X,bank,batch)
indices = indices(:);
y = d.lambert(indices);
steps = [8 8 X];
for j=1:numel(steps)
    S = primePowerSum(y,steps(j),bank,batch);
    if d.high
        [residual,slope] = rvmHighResidual( ...
            y,double(indices),d.A,d.L0,d.base);
    else
        N0 = y/(2*pi).*(log(y/(2*pi))-1)+7/8;
        residual = N0-(double(indices)-0.5);
        slope = log(y/(2*pi))/(2*pi);
    end
    y = y-(residual+S)./slope;
end
assert(all(isfinite(y)),'Prime-corrected clock produced NaN or Inf.');
end

function S = primePowerSum(y,X,bank,batch)
y = y(:);
S = zeros(numel(y),1);
last = find(bank.primePowers<=X,1,'last');
if isempty(last)
    return;
end
for first=1:batch:last
    ids = first:min(first+batch-1,last);
    phases = bsxfun(@plus, ...
        y*bank.frequencies(ids)',bank.phases(ids)');
    S = S-sin(phases)*bank.weights(ids);
end
end

function result = projectToPositiveGaps(values,reference,fraction)
% Least-squares isotonic projection with a minimum Lambert gap fraction.
% This is POST-PROCESSING, not a prime-derived theorem or proof of RH.
x = values(:)-fraction*reference(:);
n = numel(x);
level = zeros(n,1);
weight = zeros(n,1);
first = zeros(n,1);
last = zeros(n,1);
nBlocks = 0;
for i=1:n
    nBlocks = nBlocks+1;
    level(nBlocks) = x(i);
    weight(nBlocks) = 1;
    first(nBlocks) = i;
    last(nBlocks) = i;
    while nBlocks>1 && level(nBlocks-1)>level(nBlocks)
        newWeight = weight(nBlocks-1)+weight(nBlocks);
        level(nBlocks-1) = (weight(nBlocks-1)*level(nBlocks-1) ...
            +weight(nBlocks)*level(nBlocks))/newWeight;
        weight(nBlocks-1) = newWeight;
        last(nBlocks-1) = last(nBlocks);
        nBlocks = nBlocks-1;
    end
end
adjusted = zeros(n,1);
for i=1:nBlocks
    adjusted(first(i):last(i)) = level(i);
end
result = adjusted+fraction*reference(:);
end