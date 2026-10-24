%% MOBIUS_PRIME_EVERY_INTEGER_30000_PARALLEL
% Certified threshold at every integer, optimized for the observed local law.
%
% Exactness is unchanged:
%   r=f(N)-1 must be feasible;
%   r=f(N)   must be infeasible.
%
% Acceleration:
%   1. Uses f(N-1) only as a search centre, never as a certificate.
%   2. Solves r-1, r and r+1 simultaneously with Parallel Computing Toolbox.
%   3. If those levels do not bracket the transition, uses parallel trisection.
%   4. Reuses the existing checkpoint and checkpoints after every N.
%
% Requires Optimization Toolbox and Parallel Computing Toolbox.

clear;
clc;

%% User controls
Ngrid = (4:30000).';
delta = 0;
crossingStart = 4;
knowledgeMode = 'full_cutoff';

solverDisplay = 'off';
solverMaxTimeSeconds = 1800;
fastWitnessGridSize = 31;

useParallel = true;
requestedWorkers = 3;  % r-1,r,r+1 are the usual three simultaneous tests.
autoCreatePool = true;

retryOnlyUnresolvedCheckpointRows = false;
reuseCheckpointBracket = true;

checkpointFile = 'mobius_prime_every_integer_30000_checkpoint.csv';
outputMatFile = 'mobius_prime_every_integer_30000_parallel.mat';
outputFigureFile = 'mobius_prime_every_integer_30000_parallel.png';
outputIntegerLawFile = ...
    'mobius_prime_every_integer_30000_parallel_integer_law.csv';
outputIntegerLawFigure = ...
    'mobius_prime_every_integer_30000_parallel_integer_law.png';

assert(all(Ngrid >= 4 & Ngrid == floor(Ngrid)));
assert(delta >= 0);
assert(strcmp(knowledgeMode,'full_cutoff'));

if exist('intlinprog','file') ~= 2
    error('Optimization Toolbox with intlinprog is required.');
end
if useParallel && isempty(ver('parallel'))
    error('Parallel Computing Toolbox is required when useParallel=true.');
end

options = optimoptions('intlinprog', ...
    'Display',solverDisplay, ...
    'MaxTime',solverMaxTimeSeconds, ...
    'RelativeGapTolerance',0, ...
    'AbsoluteGapTolerance',0);

%% Parallel pool
if useParallel
    pool = gcp('nocreate');
    if isempty(pool) && autoCreatePool
        cluster = parcluster('local');
        workerCount = min(requestedWorkers,cluster.NumWorkers);
        pool = parpool(cluster,workerCount);
    elseif ~isempty(pool)
        fprintf('Using existing parallel pool with %d workers.\n',pool.NumWorkers);
    end
end

%% Shared arithmetic data
Nmax = max(Ngrid);
[muAll,primeListAll] = mobius_and_primes_local(Nmax);
muDoubleAll = double(muAll);
prefixSymbolCounts = [ ...
    cumsum(muDoubleAll == -1), ...
    cumsum(muDoubleAll == 0), ...
    cumsum(muDoubleAll == 1)];
MrealAll = cumsum(muDoubleAll);

realCrossingAtPosition = false(Nmax,1);
positionsForBarrier = (crossingStart:Nmax).';
realCrossingAtPosition(positionsForBarrier) = ...
    abs(MrealAll(positionsForBarrier)) > ...
    positionsForBarrier.^(0.5+delta);
realCrossingByN = cummax(realCrossingAtPosition);

primeArrivalAtSquare = zeros(Nmax,1);
primeSquaresAll = primeListAll.^2;
primeSquaresAll = primeSquaresAll(primeSquaresAll <= Nmax);
primeArrivalAtSquare(primeSquaresAll) = 1;
determiningCountByN = cumsum(primeArrivalAtSquare);

%% Checkpoint
summaryRows = empty_savings_table_local();
if isfile(checkpointFile)
    oldRows = readtable(checkpointFile);
    if all(ismember(summaryRows.Properties.VariableNames, ...
            oldRows.Properties.VariableNames))
        summaryRows = oldRows(:,summaryRows.Properties.VariableNames);
        fprintf('Resuming from %s (%d rows).\n', ...
            checkpointFile,height(summaryRows));
    end
end

runNgrid = Ngrid;
if retryOnlyUnresolvedCheckpointRows
    if isempty(summaryRows)
        error('Recovery mode requires an existing checkpoint.');
    end
    runNgrid = sort(summaryRows.N(~summaryRows.certified));
    runNgrid = runNgrid(ismember(runNgrid,Ngrid));
end

%% Certified sequential sweep; parallelism is inside each N
for caseIndex = 1:numel(runNgrid)
    N = runNgrid(caseIndex);

    oldCertified = find(summaryRows.N == N & summaryRows.certified,1);
    if ~isempty(oldCertified)
        fprintf('Skipping certified N=%6d (%d/%d).\n', ...
            N,caseIndex,numel(runNgrid));
        continue;
    end

    savedFeasible = NaN;
    savedInfeasible = NaN;
    unresolvedOld = find(summaryRows.N == N & ~summaryRows.certified,1);
    if reuseCheckpointBracket && ~isempty(unresolvedOld)
        savedFeasible = summaryRows.last_feasible_level(unresolvedOld);
        savedInfeasible = summaryRows.first_infeasible_level(unresolvedOld);
    end

    previousThreshold = NaN;
    previousCertified = find( ...
        summaryRows.N < N & summaryRows.certified,1,'last');
    if ~isempty(previousCertified)
        previousThreshold = summaryRows.threshold(previousCertified);
    end

    targetCounts = prefixSymbolCounts(N,:);
    actualCrossing = realCrossingByN(N);
    determiningCount = determiningCountByN(N);
    determiningPrimes = primeListAll(1:determiningCount);

    fprintf('\n============================================================\n');
    fprintf('PARALLEL LOCAL THRESHOLD, N=%d (%d/%d)\n', ...
        N,caseIndex,numel(runNgrid));
    fprintf('pi(sqrt(N))=%d, previous threshold=%g\n', ...
        determiningCount,previousThreshold);

    caseTimer = tic;
    thresholdResult = find_threshold_parallel_local( ...
        N,targetCounts,determiningPrimes,crossingStart, ...
        delta,knowledgeMode,fastWitnessGridSize,options, ...
        previousThreshold,savedFeasible,savedInfeasible,useParallel);
    elapsedSeconds = toc(caseTimer);

    threshold = thresholdResult.threshold;
    certified = thresholdResult.certified;

    if certified
        primeSaving = determiningCount-threshold;
        savingFraction = primeSaving/max(1,determiningCount);
        if threshold == 0
            thresholdPrime = 1;
        else
            thresholdPrime = determiningPrimes(threshold);
        end
        fprintf(['CERTIFIED f(N)=%d, saving=%d/%d = %.2f%%, ', ...
            'levels=%d, wall=%.2fs\n'], ...
            threshold,primeSaving,determiningCount, ...
            100*savingFraction,thresholdResult.numberSolvedLevels, ...
            elapsedSeconds);
    else
        primeSaving = NaN;
        savingFraction = NaN;
        thresholdPrime = NaN;
        fprintf('NOT CERTIFIED: %s\n',thresholdResult.message);
    end

    newRow = table( ...
        N,determiningCount,threshold,certified, ...
        primeSaving,savingFraction,thresholdPrime, ...
        sqrt(N)-thresholdPrime,actualCrossing, ...
        thresholdResult.feasibleLevel, ...
        thresholdResult.infeasibleLevel, ...
        thresholdResult.numberSolvedLevels,elapsedSeconds, ...
        string(thresholdResult.message), ...
        'VariableNames',{ ...
        'N','determining_prime_count','threshold', ...
        'certified','prime_saving','saving_fraction', ...
        'threshold_prime','numeric_cutoff_gap', ...
        'actual_mu_crossing','last_feasible_level', ...
        'first_infeasible_level','number_solved_levels', ...
        'elapsed_seconds','message'});

    summaryRows(summaryRows.N == N,:) = [];
    summaryRows = sortrows([summaryRows;newRow],'N'); %#ok<AGROW>
    writetable(summaryRows,checkpointFile);
    save(outputMatFile,'summaryRows','Ngrid','delta', ...
        'crossingStart','knowledgeMode','useParallel','requestedWorkers');
end

%% Final audit and plots
summaryRows = sortrows(summaryRows,'N');
certifiedMask = summaryRows.certified;
unresolvedMask = ~summaryRows.certified;

fprintf('\n');
fprintf('============================================================\n');
fprintf('PRIME-SAVING SWEEP SUMMARY\n');
fprintf('============================================================\n');
fprintf('Certified cases : %d/%d\n', ...
    nnz(certifiedMask),height(summaryRows));
if any(certifiedMask)
    fprintf('Saving range    : %g to %g primes\n', ...
        min(summaryRows.prime_saving(certifiedMask)), ...
        max(summaryRows.prime_saving(certifiedMask)));
    fprintf('Relative range  : %.3f%% to %.3f%%\n', ...
        100*min(summaryRows.saving_fraction(certifiedMask)), ...
        100*max(summaryRows.saving_fraction(certifiedMask)));
end
fprintf('============================================================\n');

figure('Color','w','Name','Certified prime-information saving');
tiledlayout(2,2,'TileSpacing','compact','Padding','compact');

nexttile;
plot(summaryRows.N(certifiedMask), ...
    summaryRows.determining_prime_count(certifiedMask), ...
    'k-','LineWidth',1.25);
hold on;
plot(summaryRows.N(certifiedMask), ...
    summaryRows.threshold(certifiedMask), ...
    'bo-','MarkerSize',3,'LineWidth',1.15);
grid on;
xlabel('N');
ylabel('Prime count');
title('Determining list and certified threshold');
legend('\pi(\surdN)','f_{\cal C}(N)','Location','best');

nexttile;
stairs(summaryRows.N(certifiedMask), ...
    summaryRows.prime_saving(certifiedMask), ...
    'r-','LineWidth',1.35);
hold on;
yline(0,'k:');
grid on;
xlabel('N');
ylabel('\pi(\surdN)-f_{\cal C}(N)');
title('Absolute saving in primes');

nexttile;
plot(summaryRows.N(certifiedMask), ...
    100*summaryRows.saving_fraction(certifiedMask), ...
    'mo-','MarkerSize',3,'LineWidth',1.15);
grid on;
xlabel('N');
ylabel('Saving (%)');
title('Relative prime-information saving');

nexttile;
plot(summaryRows.N(certifiedMask), ...
    summaryRows.numeric_cutoff_gap(certifiedMask), ...
    'go-','MarkerSize',3,'LineWidth',1.15);
hold on;
if any(unresolvedMask)
    plot(summaryRows.N(unresolvedMask), ...
        zeros(nnz(unresolvedMask),1),'rx', ...
        'MarkerSize',7,'LineWidth',1.3);
end
grid on;
xlabel('N');
ylabel('\surdN-p_{f_{\cal C}(N)}');
title('Unused numerical prime-cutoff interval');

exportgraphics(gcf,outputFigureFile,'Resolution',220);

%% Exact integer-law diagnostics; no functional fit is performed
lawRows = summaryRows(certifiedMask,{ ...
    'N','determining_prime_count','threshold','prime_saving'});
lawRows.six_d_minus_u = ...
    6*lawRows.prime_saving-lawRows.determining_prime_count;
lawRows.six_f_minus_five_u = ...
    6*lawRows.threshold-5*lawRows.determining_prime_count;
writetable(lawRows,outputIntegerLawFile);

figure('Color','w','Name','All-integer law diagnostics');
tiledlayout(2,1,'TileSpacing','compact','Padding','compact');

nexttile;
stairs(lawRows.N,lawRows.six_d_minus_u, ...
    'b-','LineWidth',1.15);
hold on;
yline(0,'k:');
grid on;
xlabel('N');
ylabel('6d(N)-\pi(\surdN)');
title('Exact integer residual at every certified N');

nexttile;
stairs(lawRows.N,lawRows.prime_saving, ...
    'r-','LineWidth',1.15);
hold on;
stairs(lawRows.N,lawRows.determining_prime_count/6, ...
    'k--','LineWidth',1.0);
grid on;
xlabel('N');
ylabel('Prime saving');
title('Observed d(N) and the central arithmetic line \pi(\surdN)/6');
legend('d(N)','\pi(\surdN)/6','Location','best');

exportgraphics(gcf,outputIntegerLawFigure,'Resolution',220);

%% Local functions

function output = find_threshold_parallel_local( ...
    N,targetCounts,determiningPrimes,crossingStart, ...
    delta,knowledgeMode,fastWitnessGridSize,options, ...
    previousThreshold,savedFeasible,savedInfeasible,useParallel)

    maximumPrimeCount = numel(determiningPrimes);
    solvedLevels = zeros(0,1);
    solvedStatuses = zeros(0,1);

    output = struct( ...
        'threshold',NaN,'certified',false, ...
        'feasibleLevel',NaN,'infeasibleLevel',NaN, ...
        'numberSolvedLevels',0,'message',"not started");

    % A previously certified adjacent bracket for this same N is reusable.
    if isfinite(savedFeasible) && isfinite(savedInfeasible) && ...
            savedFeasible >= 0 && ...
            savedInfeasible == savedFeasible+1 && ...
            savedInfeasible <= maximumPrimeCount
        output.threshold = savedInfeasible;
        output.certified = true;
        output.feasibleLevel = savedFeasible;
        output.infeasibleLevel = savedInfeasible;
        output.message = "adjacent checkpoint bracket reused";
        return;
    end

    % Local triplet centred at f(N-1). This is only a search hint.
    if isfinite(previousThreshold)
        centre = min(max(round(previousThreshold),0),maximumPrimeCount);
        initialLevels = unique(max(0,min(maximumPrimeCount, ...
            [centre-1;centre;centre+1])));
    else
        initialLevels = unique([0;maximumPrimeCount]);
    end

    [statuses,diagnostics] = solve_levels_parallel_local( ...
        initialLevels,N,targetCounts,determiningPrimes,crossingStart, ...
        delta,knowledgeMode,fastWitnessGridSize,options,useParallel);
    append_results_local(initialLevels,statuses,diagnostics);

    if any(statuses == 0)
        % An unresolved neighbour need not block certification if another
        % solved adjacent pair already certifies the transition.
        [done,threshold,lo,hi] = adjacent_transition_local( ...
            solvedLevels,solvedStatuses);
        if done
            certify_local(threshold,lo,hi, ...
                "adjacent local transition certified");
            return;
        end
    end

    [done,threshold,lo,hi] = adjacent_transition_local( ...
        solvedLevels,solvedStatuses);
    if done
        certify_local(threshold,lo,hi, ...
            "adjacent local transition certified");
        return;
    end

    % Ensure global feasible/infeasible endpoints exist.
    endpointLevels = zeros(0,1);
    if ~any(solvedLevels == 0 & solvedStatuses == 1)
        endpointLevels(end+1,1) = 0; %#ok<AGROW>
    end
    if ~any(solvedLevels == maximumPrimeCount & solvedStatuses == -2)
        endpointLevels(end+1,1) = maximumPrimeCount; %#ok<AGROW>
    end
    endpointLevels = unique(endpointLevels);

    if ~isempty(endpointLevels)
        [statuses,diagnostics] = solve_levels_parallel_local( ...
            endpointLevels,N,targetCounts,determiningPrimes, ...
            crossingStart,delta,knowledgeMode,fastWitnessGridSize, ...
            options,useParallel);
        append_results_local(endpointLevels,statuses,diagnostics);
    end

    feasibleCandidates = solvedLevels(solvedStatuses == 1);
    infeasibleCandidates = solvedLevels(solvedStatuses == -2);
    if isempty(feasibleCandidates) || isempty(infeasibleCandidates)
        output.message = "global feasible/infeasible endpoints not certified";
        finalize_local();
        return;
    end

    lo = max(feasibleCandidates);
    hi = min(infeasibleCandidates);
    if lo >= hi
        output.message = "monotonicity contradiction in solved statuses";
        finalize_local();
        return;
    end

    % Parallel trisection. Usually never reached after the local triplet.
    while hi-lo > 1
        q1 = floor((2*lo+hi)/3);
        q2 = ceil((lo+2*hi)/3);
        levels = unique([q1;q2]);
        levels = levels(levels > lo & levels < hi);
        if isempty(levels)
            levels = floor((lo+hi)/2);
        end

        [statuses,diagnostics] = solve_levels_parallel_local( ...
            levels,N,targetCounts,determiningPrimes,crossingStart, ...
            delta,knowledgeMode,fastWitnessGridSize,options,useParallel);
        append_results_local(levels,statuses,diagnostics);

        oldLo = lo;
        oldHi = hi;
        feasibleCandidates = solvedLevels( ...
            solvedStatuses == 1 & solvedLevels < hi);
        infeasibleCandidates = solvedLevels( ...
            solvedStatuses == -2 & solvedLevels > lo);
        if ~isempty(feasibleCandidates)
            lo = max(feasibleCandidates);
        end
        if ~isempty(infeasibleCandidates)
            hi = min(infeasibleCandidates);
        end

        if lo == oldLo && hi == oldHi
            output.message = "parallel trisection hit unresolved levels";
            finalize_local();
            return;
        end
    end

    certify_local(hi,lo,hi,"adjacent transition certified");

    function append_results_local(levels,statuses,diagnostics)
        for j = 1:numel(levels)
            duplicate = find(solvedLevels == levels(j),1);
            if isempty(duplicate)
                solvedLevels(end+1,1) = levels(j); %#ok<AGROW>
                solvedStatuses(end+1,1) = statuses(j); %#ok<AGROW>
            else
                solvedStatuses(duplicate) = statuses(j);
            end
            D = diagnostics(j);
            fprintf(['  r=%3d/%3d, cutoff=%8.3f, cores=%5d, ', ...
                'forced=%6.2f%%, status=%2d, %-12s, %.2fs\n'], ...
                levels(j),maximumPrimeCount,D.cutoff, ...
                D.unknownCoreCount,100*D.forcedRatio, ...
                statuses(j),D.method,D.elapsed);
        end
    end

    function certify_local(threshold,feasibleLevel,infeasibleLevel,message)
        output.threshold = threshold;
        output.certified = true;
        output.feasibleLevel = feasibleLevel;
        output.infeasibleLevel = infeasibleLevel;
        output.message = message;
        finalize_local();
    end

    function finalize_local()
        output.numberSolvedLevels = numel(solvedLevels);
        if isnan(output.feasibleLevel)
            c = solvedLevels(solvedStatuses == 1);
            if ~isempty(c), output.feasibleLevel = max(c); end
        end
        if isnan(output.infeasibleLevel)
            c = solvedLevels(solvedStatuses == -2);
            if ~isempty(c), output.infeasibleLevel = min(c); end
        end
    end
end

function [done,threshold,lo,hi] = adjacent_transition_local(levels,statuses)
    done = false;
    threshold = NaN;
    lo = NaN;
    hi = NaN;
    infeasible = sort(levels(statuses == -2));
    for k = 1:numel(infeasible)
        candidate = infeasible(k);
        if candidate == 0
            done = true;
            threshold = 0;
            lo = -1;
            hi = 0;
            return;
        end
        if any(levels == candidate-1 & statuses == 1)
            done = true;
            threshold = candidate;
            lo = candidate-1;
            hi = candidate;
            return;
        end
    end
end

function [statuses,diagnostics] = solve_levels_parallel_local( ...
    levels,N,targetCounts,determiningPrimes,crossingStart, ...
    delta,knowledgeMode,fastWitnessGridSize,options,useParallel)

    nLevels = numel(levels);
    statuses = zeros(nLevels,1);
    diagnostics = repmat(struct( ...
        'cutoff',NaN,'unknownCoreCount',NaN,'forcedRatio',NaN, ...
        'method',"",'elapsed',NaN),nLevels,1);

    if useParallel && nLevels > 1
        parfor j = 1:nLevels
            [statuses(j),diagnostics(j)] = solve_prime_level_local( ...
                levels(j),N,targetCounts,determiningPrimes, ...
                crossingStart,delta,knowledgeMode, ...
                fastWitnessGridSize,options);
        end
    else
        for j = 1:nLevels
            [statuses(j),diagnostics(j)] = solve_prime_level_local( ...
                levels(j),N,targetCounts,determiningPrimes, ...
                crossingStart,delta,knowledgeMode, ...
                fastWitnessGridSize,options);
        end
    end
end

function [status,diagnostic] = solve_prime_level_local( ...
    r,N,targetCounts,determiningPrimes,crossingStart, ...
    delta,knowledgeMode,fastWitnessGridSize,options)

    maximumPrimeCount = numel(determiningPrimes);
    knownPrimes = determiningPrimes(1:r);
    cutoff = cutoff_for_level_local( ...
        r,maximumPrimeCount,determiningPrimes,N);
    model = build_prime_completion_model_local( ...
        N,targetCounts,knownPrimes,cutoff,knowledgeMode);

    levelTimer = tic;
    method = "";

    if r == 0
        positiveCount = targetCounts(3);
        explicitPosition = max(crossingStart,positiveCount);
        if positiveCount >= explicitPosition && ...
                positiveCount > explicitPosition^(0.5+delta)
            status = 1;
        else
            result = solve_crossing_completion_local( ...
                model,crossingStart,delta,options);
            status = result.status;
        end
        method = "constructive";

    elseif model.unknownCoreCount == 0
        partialSums = cumsum(model.fixedSequence);
        positions = (crossingStart:N).';
        if any(abs(partialSums(positions)) > ...
                positions.^(0.5+delta))
            status = 1;
        else
            status = -2;
        end
        method = "direct";

    else
        witness = solve_grid_crossing_witness_local( ...
            model,crossingStart,delta,fastWitnessGridSize,options);
        if witness.status == 1
            status = 1;
            method = "grid witness";
        else
            result = solve_crossing_completion_local( ...
                model,crossingStart,delta,options);
            status = result.status;
            method = "full proof";
        end
    end

    diagnostic.cutoff = cutoff;
    diagnostic.unknownCoreCount = model.unknownCoreCount;
    diagnostic.forcedRatio = model.forcedPositionCount/N;
    diagnostic.method = method;
    diagnostic.elapsed = toc(levelTimer);
end

function T = empty_savings_table_local()
    T = table( ...
        zeros(0,1),zeros(0,1),zeros(0,1),false(0,1), ...
        zeros(0,1),zeros(0,1),zeros(0,1),zeros(0,1), ...
        false(0,1),zeros(0,1),zeros(0,1),zeros(0,1), ...
        zeros(0,1),strings(0,1), ...
        'VariableNames',{ ...
        'N','determining_prime_count','threshold', ...
        'certified','prime_saving','saving_fraction', ...
        'threshold_prime','numeric_cutoff_gap', ...
        'actual_mu_crossing','last_feasible_level', ...
        'first_infeasible_level','number_solved_levels', ...
        'elapsed_seconds','message'});
end

function model = build_prime_completion_model_local( ...
    N,targetCounts,knownPrimes,cutoff,knowledgeMode)

    fixedValues = nan(N,1);
    coreValues = zeros(N,1);
    coreSigns = zeros(N,1);

    for n = 1:N
        residual = n;
        parity = 0;
        killedBySquare = false;

        for primeIndex = 1:numel(knownPrimes)
            p = knownPrimes(primeIndex);
            exponent = 0;

            while mod(residual,p) == 0
                residual = residual/p;
                exponent = exponent+1;
            end

            if exponent >= 2
                killedBySquare = true;
                break;
            elseif exponent == 1
                parity = 1-parity;
            end
        end

        knownSign = 1-2*parity;

        if killedBySquare
            fixedValues(n) = 0;
        elseif residual == 1
            fixedValues(n) = knownSign;
        elseif strcmp(knowledgeMode,'full_cutoff') && ...
                residual <= cutoff^2+10*eps(cutoff^2)
            % A residual with no prime factor <=cutoff and size <=cutoff^2
            % is prime.
            fixedValues(n) = -knownSign;
        else
            coreValues(n) = residual;
            coreSigns(n) = knownSign;
        end
    end

    unknownMask = isnan(fixedValues);
    unknownCores = unique(coreValues(unknownMask));
    unknownCoreCount = numel(unknownCores);
    zCount = 3*unknownCoreCount;

    if unknownCoreCount > 0
        [~,coreIndexByPosition] = ...
            ismember(coreValues(unknownMask),unknownCores);
    else
        coreIndexByPosition = zeros(0,1);
    end

    unknownPositions = find(unknownMask);
    numberUnknownPositions = numel(unknownPositions);

    rowIndex = zeros(2*numberUnknownPositions,1);
    columnIndex = zeros(2*numberUnknownPositions,1);
    coefficients = zeros(2*numberUnknownPositions,1);

    countRows = zeros(3*numberUnknownPositions,1);
    countColumns = zeros(3*numberUnknownPositions,1);
    countValues = ones(3*numberUnknownPositions,1);

    termCounter = 0;
    countCounter = 0;

    for positionIndex = 1:numberUnknownPositions
        n = unknownPositions(positionIndex);
        coreIndex = coreIndexByPosition(positionIndex);
        signValue = coreSigns(n);
        stateColumns = 3*coreIndex-2:3*coreIndex;

        termCounter = termCounter+1;
        rowIndex(termCounter) = n;
        columnIndex(termCounter) = stateColumns(1);
        coefficients(termCounter) = -signValue;

        termCounter = termCounter+1;
        rowIndex(termCounter) = n;
        columnIndex(termCounter) = stateColumns(3);
        coefficients(termCounter) = signValue;

        if signValue == 1
            symbolRows = [1,2,3];
        else
            symbolRows = [3,2,1];
        end

        for stateIndex = 1:3
            countCounter = countCounter+1;
            countRows(countCounter) = symbolRows(stateIndex);
            countColumns(countCounter) = stateColumns(stateIndex);
        end
    end

    termMap = sparse( ...
        rowIndex(1:termCounter), ...
        columnIndex(1:termCounter), ...
        coefficients(1:termCounter),N,zCount);

    countMap = sparse( ...
        countRows(1:countCounter), ...
        countColumns(1:countCounter), ...
        countValues(1:countCounter),3,zCount);

    fixedSequence = zeros(N,1);
    fixedSequence(~unknownMask) = fixedValues(~unknownMask);
    fixedCounts = count_symbols_local(fixedSequence(~unknownMask));

    oneHot = kron(speye(unknownCoreCount),ones(1,3));
    oneHotRhs = ones(unknownCoreCount,1);

    model.N = N;
    model.targetCounts = targetCounts(:);
    model.knownPrimes = knownPrimes(:);
    model.cutoff = cutoff;
    model.knowledgeMode = knowledgeMode;
    model.unknownCores = unknownCores;
    model.unknownCoreCount = unknownCoreCount;
    model.ambiguousPositionCount = numberUnknownPositions;
    model.forcedPositionCount = N-numberUnknownPositions;
    model.zCount = zCount;
    model.termMap = termMap;
    model.countMap = countMap;
    model.fixedSequence = fixedSequence;
    model.fixedCounts = fixedCounts(:);
    model.oneHot = oneHot;
    model.oneHotRhs = oneHotRhs;
end

function result = solve_grid_crossing_witness_local( ...
    model,crossingStart,delta,gridSize,options)

    N = model.N;
    zCount = model.zCount;

    linearGrid = round(linspace(crossingStart,N,gridSize)).';
    lateGrid = round(N*(0.50:0.025:0.975)).';
    earlyGrid = (crossingStart:min(N,crossingStart+12)).';
    crossingPositions = unique([earlyGrid;linearGrid;lateGrid]);
    crossingPositions = crossingPositions( ...
        crossingPositions >= crossingStart & ...
        crossingPositions <= N);

    numberCrossingPositions = numel(crossingPositions);
    selectorCount = 2*numberCrossingPositions;
    totalVariables = zCount+selectorCount;

    % Build only the selected prefix rows.  This avoids the N continuous
    % partial-sum variables and the 2N selector binaries of the full MILP.
    prefixMap = sparse(numberCrossingPositions,zCount);
    runningRow = sparse(1,zCount);
    previousPosition = 0;

    for positionIndex = 1:numberCrossingPositions
        position = crossingPositions(positionIndex);
        if position > previousPosition
            runningRow = runningRow + sum( ...
                model.termMap(previousPosition+1:position,:),1);
        end
        prefixMap(positionIndex,:) = runningRow;
        previousPosition = position;
    end

    fixedPartialSums = cumsum(model.fixedSequence);
    fixedPrefixes = fixedPartialSums(crossingPositions);
    thresholds = floor( ...
        crossingPositions.^(0.5+delta))+1;
    bigM = N+thresholds;

    positiveSelectorIndices = ...
        zCount+(1:numberCrossingPositions);
    negativeSelectorIndices = ...
        zCount+numberCrossingPositions+ ...
        (1:numberCrossingPositions);

    Apositive = [ ...
        -prefixMap, ...
        spdiags(bigM,0,numberCrossingPositions, ...
        numberCrossingPositions), ...
        sparse(numberCrossingPositions, ...
        numberCrossingPositions)];
    bpositive = bigM-thresholds+fixedPrefixes;

    Anegative = [ ...
        prefixMap, ...
        sparse(numberCrossingPositions, ...
        numberCrossingPositions), ...
        spdiags(bigM,0,numberCrossingPositions, ...
        numberCrossingPositions)];
    bnegative = bigM-thresholds-fixedPrefixes;

    AatLeastOne = sparse(1,totalVariables);
    AatLeastOne(positiveSelectorIndices) = -1;
    AatLeastOne(negativeSelectorIndices) = -1;

    Aineq = [Apositive;Anegative;AatLeastOne];
    bineq = [bpositive;bnegative;-1];

    AoneHot = [ ...
        model.oneHot, ...
        sparse(model.unknownCoreCount,selectorCount)];
    Acounts = [ ...
        model.countMap, ...
        sparse(3,selectorCount)];
    Aeq = [AoneHot;Acounts];
    beq = [ ...
        model.oneHotRhs; ...
        model.targetCounts-model.fixedCounts];

    objective = zeros(totalVariables,1);
    integerVariables = 1:totalVariables;
    lowerBounds = zeros(totalVariables,1);
    upperBounds = ones(totalVariables,1);

    [solution,~,exitflag,output] = intlinprog( ...
        objective,integerVariables, ...
        Aineq,bineq,Aeq,beq, ...
        lowerBounds,upperBounds,options);

    result.status = normalize_exitflag_local(exitflag,solution);
    result.exitflag = exitflag;
    result.output = output;
    result.sequence = [];
    result.firstCrossing = NaN;
    result.maximumRatio = NaN;

    if result.status == 1
        z = round(solution(1:zCount));
        sequence = model.fixedSequence+model.termMap*z;
        partialSums = cumsum(sequence);
        crossingMask = ...
            abs(partialSums(crossingPositions)) > ...
            crossingPositions.^(0.5+delta);

        assert(any(crossingMask));
        assert(isequal( ...
            count_symbols_local(sequence), ...
            model.targetCounts.'));
        validate_known_prime_rules_local( ...
            sequence,model.knownPrimes,N);

        result.sequence = int8(round(sequence));
        result.firstCrossing = ...
            crossingPositions(find(crossingMask,1,'first'));
        result.maximumRatio = max( ...
            abs(partialSums(crossingPositions)) ./ ...
            crossingPositions.^(0.5+delta));
    end
end

function result = solve_crossing_completion_local( ...
    model,crossingStart,delta,options)

    N = model.N;
    zCount = model.zCount;
    crossingPositions = (crossingStart:N).';
    numberCrossingPositions = numel(crossingPositions);
    selectorCount = 2*numberCrossingPositions;

    sIndices = zCount+(1:N);
    positiveSelectorIndices = ...
        zCount+N+(1:numberCrossingPositions);
    negativeSelectorIndices = ...
        zCount+N+numberCrossingPositions+ ...
        (1:numberCrossingPositions);
    totalVariables = zCount+N+selectorCount;

    % Partial-sum recurrence:
    % S(n)-S(n-1)-x_variable(n)=x_fixed(n).
    differenceMatrix = ...
        spdiags([-ones(N,1),ones(N,1)],[-1,0],N,N);

    Arecurrence = [ ...
        -model.termMap, ...
        differenceMatrix, ...
        sparse(N,selectorCount)];
    brecurrence = model.fixedSequence;

    AoneHot = [ ...
        model.oneHot, ...
        sparse(model.unknownCoreCount,N+selectorCount)];
    boneHot = model.oneHotRhs;

    Acounts = [ ...
        model.countMap, ...
        sparse(3,N+selectorCount)];
    bcounts = model.targetCounts-model.fixedCounts;

    Aeq = [AoneHot;Arecurrence;Acounts];
    beq = [boneHot;brecurrence;bcounts];

    thresholds = ...
        floor(crossingPositions.^(0.5+delta))+1;
    bigM = N+thresholds;

    AcrossPositive = sparse( ...
        numberCrossingPositions,totalVariables);
    AcrossPositive = AcrossPositive + sparse( ...
        (1:numberCrossingPositions).', ...
        sIndices(crossingPositions).', ...
        -ones(numberCrossingPositions,1), ...
        numberCrossingPositions,totalVariables);
    AcrossPositive = AcrossPositive + sparse( ...
        (1:numberCrossingPositions).', ...
        positiveSelectorIndices.', ...
        bigM,numberCrossingPositions,totalVariables);

    AcrossNegative = sparse( ...
        numberCrossingPositions,totalVariables);
    AcrossNegative = AcrossNegative + sparse( ...
        (1:numberCrossingPositions).', ...
        sIndices(crossingPositions).', ...
        ones(numberCrossingPositions,1), ...
        numberCrossingPositions,totalVariables);
    AcrossNegative = AcrossNegative + sparse( ...
        (1:numberCrossingPositions).', ...
        negativeSelectorIndices.', ...
        bigM,numberCrossingPositions,totalVariables);

    AatLeastOne = sparse(1,totalVariables);
    AatLeastOne(positiveSelectorIndices) = -1;
    AatLeastOne(negativeSelectorIndices) = -1;

    Aineq = [AcrossPositive;AcrossNegative;AatLeastOne];
    bineq = [ ...
        bigM-thresholds; ...
        bigM-thresholds; ...
        -1];

    objective = zeros(totalVariables,1);
    integerVariables = [ ...
        (1:zCount), ...
        positiveSelectorIndices,negativeSelectorIndices];

    lowerBounds = [ ...
        zeros(zCount,1); ...
        -N*ones(N,1); ...
        zeros(selectorCount,1)];
    upperBounds = [ ...
        ones(zCount,1); ...
        N*ones(N,1); ...
        ones(selectorCount,1)];

    [solution,~,exitflag,output] = intlinprog( ...
        objective,integerVariables, ...
        Aineq,bineq,Aeq,beq, ...
        lowerBounds,upperBounds,options);

    result.status = normalize_exitflag_local(exitflag,solution);
    result.exitflag = exitflag;
    result.output = output;
    result.sequence = [];
    result.firstCrossing = NaN;
    result.maximumRatio = NaN;

    if result.status == 1
        z = round(solution(1:zCount));
        sequence = model.fixedSequence+model.termMap*z;
        partialSums = cumsum(sequence);
        crossingMask = ...
            abs(partialSums(crossingPositions)) > ...
            crossingPositions.^(0.5+delta);

        assert(any(crossingMask));
        assert(isequal( ...
            count_symbols_local(sequence), ...
            model.targetCounts.'));

        validate_known_prime_rules_local( ...
            sequence,model.knownPrimes,N);

        result.sequence = int8(round(sequence));
        result.firstCrossing = ...
            crossingPositions(find(crossingMask,1,'first'));
        result.maximumRatio = max( ...
            abs(partialSums(crossingPositions)) ./ ...
            crossingPositions.^(0.5+delta));
    end
end

function status = normalize_exitflag_local(exitflag,solution)
    if ~isempty(solution) && exitflag > 0
        status = 1;
    elseif exitflag == -2
        status = -2;
    else
        status = 0;
    end
end

function validate_known_prime_rules_local(sequence,knownPrimes,N)
    sequence = double(sequence(:));

    assert(sequence(1) == 1);

    for primeIndex = 1:numel(knownPrimes)
        p = knownPrimes(primeIndex);

        for m = 1:floor(N/p)
            if mod(m,p) == 0
                assert(sequence(p*m) == 0);
            else
                assert(sequence(p*m) == -sequence(m));
            end
        end
    end
end

function cutoff = cutoff_for_level_local( ...
    r,maximumPrimeCount,determiningPrimes,N)

    if r == 0
        cutoff = 1;
    elseif r == maximumPrimeCount
        % At the final level we know that the supplied list contains all
        % primes up to sqrt(N), including the terminal prime gap.
        cutoff = sqrt(N);
    else
        cutoff = determiningPrimes(r);
    end
end

function [threshold,certified] = ...
    extract_threshold_local(levels,statusValues)

    threshold = NaN;
    certified = false;

    infeasibleIndex = find(statusValues == -2,1,'first');
    if isempty(infeasibleIndex)
        return;
    end

    candidateThreshold = levels(infeasibleIndex);

    if candidateThreshold == 0
        threshold = 0;
        certified = true;
    else
        previousIndex = find( ...
            levels == candidateThreshold-1,1);

        if ~isempty(previousIndex) && ...
                statusValues(previousIndex) == 1
            threshold = candidateThreshold;
            certified = true;
        end
    end
end

function print_threshold_local( ...
    label,threshold,certified,levels,cutoffs, ...
    harmonicCosts,forcedRatios,maximumPrimeCount)

    if ~certified
        fprintf('%s threshold: NOT CERTIFIED\n',label);
        return;
    end

    index = find(levels == threshold,1);
    fprintf(['%s threshold: f(N)=%d primes, ', ...
        'y=%.6f, fraction=%.6f, ', ...
        'sum(1/p)=%.6f, forced=%.2f%% [CERTIFIED]\n'], ...
        label,threshold,cutoffs(index), ...
        threshold/max(1,maximumPrimeCount), ...
        harmonicCosts(index),100*forcedRatios(index));
end

function levels = adaptive_levels_local(maximumPrimeCount)
    % The complete scan is the rigorous default for small and moderate N.
    % This reduced list preserves endpoints and powers of two for a quick
    % reconnaissance.  A certified minimum still requires resolving the
    % two adjacent levels around the transition.
    if maximumPrimeCount <= 16
        levels = (0:maximumPrimeCount).';
    else
        levels = unique([ ...
            0; ...
            2.^(0:floor(log2(maximumPrimeCount))).'; ...
            maximumPrimeCount]);
    end
end

function [mu,primes] = mobius_and_primes_local(N)
    mu = zeros(N,1,'int8');
    mu(1) = int8(1);
    primeStorage = zeros(N,1);
    primeCount = 0;
    composite = false(N,1);

    for n = 2:N
        if ~composite(n)
            primeCount = primeCount+1;
            primeStorage(primeCount) = n;
            mu(n) = int8(-1);
        end

        for primeIndex = 1:primeCount
            p = primeStorage(primeIndex);
            value = n*p;

            if value > N
                break;
            end

            composite(value) = true;

            if mod(n,p) == 0
                mu(value) = int8(0);
                break;
            else
                mu(value) = -mu(n);
            end
        end
    end

    primes = primeStorage(1:primeCount);
end

function counts = count_symbols_local(sequence)
    counts = [ ...
        nnz(sequence == -1), ...
        nnz(sequence == 0), ...
        nnz(sequence == 1)];
end
