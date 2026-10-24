%% ZETA_PRIME_POWER_ANALYTIC_AUDIT
%
% Script autocontenido para los seis tests de la descomposicion
%
%   S_q(T) = sum_{gamma_j <= T} exp(i*gamma_j*log(q))
%
% No usa ningun .mat, .csv ni resultado anterior.
% El unico dato externo necesario es el fichero original de ordenadas:
%
%   zeross.bin
%
% Si no esta en la carpeta actual, MATLAB abre un selector para localizarlo.
%
% No resta 0.5*exp(i*T). Ajusta conjuntamente una constante aditiva y
% el coeficiente de exp(i*log(q)*T). La constante se elimina antes de
% demodular.
% Todos los resumenes principales se muestran con fprintf/disp.
% No se cierra ninguna figura.
%
% TESTS
% -----
% 1. Separacion P_Q^- y P_Q^+ y termino cruzado.
% 2. Identidades de c_n^-, c_n^+ y sumas A_Q, B_Q.
% 3. Busqueda de telescopado dentro de p,p^2,...,p^R.
% 4. Funcionales positivos y matrices de Gram por bloques.
% 5. Ecuacion funcional del residuo demodulado F_Q.
% 6. Unicidad: bloques, anisotropia, gaps y frecuencias omitidas.
%
% Requiere una version de MATLAB que permita funciones locales al final
% de un script (R2016b o posterior).

clear;
clc;
format long g;

%% ========================================================================
% CONFIGURACION
% ========================================================================

zeroBinaryFile = 'zeross.bin';

% q=e reproduce exp(i*gamma).
qPhase = exp(1);
omega = log(qPhase);

% stride=10: usa todos los ceros para construir S_q, pero analiza 1 de cada 10.
% stride=1: analiza los 2,001,052 puntos completos, mucho mas lento para Q=10000.
stride = 1;

Qlist = [0, 3, 10, 100, 1000, 10000];
Qlist = unique(sort(Qlist(:).'));
Qmax = max(Qlist);

numHeightBlocks = 24;
numGramBlocks = 20;
maxGramPoints = 60000;

omittedTestWidth = 500;
maxSpectralPoints = 50000;
numFrequencyGridPoints = 401;

gapMedianWindow = 1001;
resonanceTolerance = 1e-12;
minimumVariance = 1e-30;

% Si se pone true, guarda tablas y MAT al final. No son necesarios para correr.
saveResults = false;
outputDirectory = 'ZETA_PRIME_POWER_STRUCTURE_RESULTS';

%% ========================================================================
% LOCALIZAR Y LEER zeross.bin
% ========================================================================

if ~isfile(zeroBinaryFile)
    [selectedFile,selectedPath] = uigetfile( ...
        {'*.bin','Binary doubles (*.bin)';'*.*','Todos los archivos'}, ...
        'Selecciona zeross.bin');

    if isequal(selectedFile,0)
        error(['No se encontro zeross.bin y no se selecciono ningun archivo. ' ...
            'Este es el unico fichero de datos necesario.']);
    end

    zeroBinaryFile = fullfile(selectedPath,selectedFile);
end

fileID = fopen(zeroBinaryFile,'rb');
if fileID == -1
    error('No se pudo abrir %s.',zeroBinaryFile);
end

cleanupObject = onCleanup(@() fclose(fileID));
gammaAll = fread(fileID,Inf,'double=>double');
clear cleanupObject;

gammaAll = gammaAll(:);
gammaAll = gammaAll(isfinite(gammaAll) & gammaAll>0);

if numel(gammaAll)<2
    error('El fichero no contiene suficientes ordenadas validas.');
end

if any(diff(gammaAll)<=0)
    error('Las ordenadas no estan estrictamente ordenadas.');
end

Nfull = numel(gammaAll);

fprintf('\n============================================================\n');
fprintf('ZETA PRIME-POWER STRUCTURE: ANALYTIC AUDIT\n');
fprintf('============================================================\n');
fprintf('Archivo de ceros       : %s\n',zeroBinaryFile);
fprintf('Ceros disponibles      : %d\n',Nfull);
fprintf('q                      : %.17g\n',qPhase);
fprintf('omega=log(q)           : %.17g\n',omega);
fprintf('stride                 : %d\n',stride);
fprintf('Qlist                  :');
fprintf(' %g',Qlist);
fprintf('\n');

%% ========================================================================
% CONSTRUIR S_q CON TODOS LOS CEROS; MUESTREAR DESPUES
% ========================================================================

carrierAll = exp(1i*omega*gammaAll);
SphaseAll = cumsum(carrierAll);

% Parte suave analitica, salvo constante aditiva:
%
% int exp(i*omega*T)/(2*pi)*log(T/(2*pi)) dT
%
% = [exp(i omega T)log(T/2pi)-Ei(i omega T)]/(2*pi*i*omega).
%
% MATLAB: Ei(z) = -expint(-z), salvo la constante de rama, que solo
% modifica una constante aditiva y se absorbe en los ajustes.
Ei_iomegaT_all = -expint(-1i*omega*gammaAll);
AsmoothAll = (carrierAll.*log(gammaAll/(2*pi))-Ei_iomegaT_all) ...
    /(2*pi*1i*omega);

indices = (1:stride:Nfull).';
gamma = gammaAll(indices);
carrier = carrierAll(indices);
Sphase = SphaseAll(indices);
Asmooth = AsmoothAll(indices);

gapBeforeAll = [NaN;diff(gammaAll)];
gapLocalMedianAll = movmedian(gapBeforeAll,gapMedianWindow, ...
    'omitmissing','Endpoints','shrink');
gapResidualAll = gapBeforeAll-gapLocalMedianAll;

gapBefore = gapBeforeAll(indices);
gapResidual = gapResidualAll(indices);

clear carrierAll SphaseAll AsmoothAll Ei_iomegaT_all;
clear gapBeforeAll gapLocalMedianAll gapResidualAll;

Y = Sphase-Asmooth;
N = numel(gamma);

fprintf('Puntos analizados       : %d\n',N);
fprintf('gamma inicial           : %.15g\n',gamma(1));
fprintf('gamma final             : %.15g\n',gamma(end));

%% ========================================================================
% GENERAR TODAS LAS POTENCIAS PRIMAS <= Qmax
% ========================================================================

[qVec,basePrimeVec,powerExponentVec,lambdaVec] = makePrimePowers(Qmax);
numTerms = numel(qVec);

ellVec = log(qVec);
deltaMinusVec = omega-ellVec;
deltaPlusVec = omega+ellVec;

resonantIndex = find(abs(deltaMinusVec)<=resonanceTolerance,1);
if ~isempty(resonantIndex)
    error(['qPhase es resonante con n=%d. Esta version no oculta la ' ...
        'singularidad: debe introducirse el termino resonante regularizado.'], ...
        qVec(resonantIndex));
end

cMinusVec = 1i*lambdaVec ./ ...
    (2*pi*sqrt(qVec).*deltaMinusVec);

cPlusVec = 1i*lambdaVec ./ ...
    (2*pi*sqrt(qVec).*deltaPlusVec);

%% ========================================================================
% TEST 2: IDENTIDADES ALGEBRAICAS DE LOS COEFICIENTES
% ========================================================================

sumIdentityRHS = 1i*lambdaVec.*omega ./ ...
    (pi*sqrt(qVec).*(omega^2-ellVec.^2));

differenceIdentityRHS = 1i*lambdaVec.*ellVec ./ ...
    (pi*sqrt(qVec).*(omega^2-ellVec.^2));

ratioIdentityRHS = (omega+ellVec)./(omega-ellVec);

sumIdentityError = abs((cMinusVec+cPlusVec)-sumIdentityRHS);
differenceIdentityError = abs((cMinusVec-cPlusVec)-differenceIdentityRHS);
ratioIdentityError = abs((cMinusVec./cPlusVec)-ratioIdentityRHS);

AQ = cumsum(cMinusVec+cPlusVec);
BQ = cumsum(cMinusVec-cPlusVec);

fprintf('\n============================================================\n');
fprintf('TEST 2: IDENTIDADES DE COEFICIENTES\n');
fprintf('============================================================\n');
fprintf('Potencias primas <=Qmax                  : %d\n',numTerms);
fprintf('max |(c^-+c^+)-formula|                 : %.6e\n', ...
    max(sumIdentityError));
fprintf('max |(c^--c^+)-formula|                 : %.6e\n', ...
    max(differenceIdentityError));
fprintf('max |c^-/c^+-formula|                   : %.6e\n', ...
    max(ratioIdentityError));

coefficientCutoffRows = cell(numel(Qlist),9);

for jj = 1:numel(Qlist)
    currentQ = Qlist(jj);
    lastIndex = find(qVec<=currentQ,1,'last');

    if isempty(lastIndex)
        currentA = 0;
        currentB = 0;
        numberTerms = 0;
    else
        currentA = AQ(lastIndex);
        currentB = BQ(lastIndex);
        numberTerms = lastIndex;
    end

    coefficientCutoffRows(jj,:) = { ...
        currentQ,numberTerms, ...
        real(currentA),imag(currentA),abs(currentA-0.5), ...
        real(currentB),imag(currentB),abs(currentB-0.5), ...
        abs(currentB+0.5)};
end

coefficientCutoffDisplay = cell2table(coefficientCutoffRows, ...
    'VariableNames',{ ...
    'Q','num_terms','Re_AQ','Im_AQ','abs_AQ_minus_half', ...
    'Re_BQ','Im_BQ','abs_BQ_minus_half','abs_BQ_plus_half'});

disp(coefficientCutoffDisplay);


%% ========================================================================
% AUDITORIA RADIAL DIRECTA: ORIGINAL, n=3, n=2+3
% ========================================================================

fprintf('\n============================================================\n');
fprintf('AUDITORIA RADIAL DIRECTA DE LA BIMODALIDAD\n');
fprintf('============================================================\n');

numRadialBins = 220;
radialSmoothWidth = 9;

index3 = find(qVec==3,1);
index23 = find(qVec<=3);

if isempty(index3)
    error('No se encontro n=3 entre las potencias primas.');
end

ell3 = ellVec(index3);
P3minus = cMinusVec(index3).*carrier.*exp(-1i*ell3*gamma);
P3plus = cPlusVec(index3).*carrier.*exp(1i*ell3*gamma);
P3 = P3minus+P3plus;

P23 = complex(zeros(N,1));
for auditIndex = index23(:).'
    ellAudit = ellVec(auditIndex);
    P23 = P23 ...
        +cMinusVec(auditIndex).*carrier.*exp(-1i*ellAudit*gamma) ...
        +cPlusVec(auditIndex).*carrier.*exp(1i*ellAudit*gamma);
end

[radialOriginal,radialCentersOriginal,radialDensityOriginal, ...
    radialPeaksOriginal] = radialDistributionSummary( ...
    Sphase,numRadialBins,radialSmoothWidth);

[radialAfter3,radialCentersAfter3,radialDensityAfter3, ...
    radialPeaksAfter3] = radialDistributionSummary( ...
    Sphase-P3,numRadialBins,radialSmoothWidth);

[radialAfter23,radialCentersAfter23,radialDensityAfter23, ...
    radialPeaksAfter23] = radialDistributionSummary( ...
    Sphase-P23,numRadialBins,radialSmoothWidth);

radialAuditTable = table( ...
    ["original";"after_n3";"after_n2_n3"], ...
    [mean(radialOriginal);mean(radialAfter3);mean(radialAfter23)], ...
    [std(radialOriginal);std(radialAfter3);std(radialAfter23)], ...
    [numel(radialPeaksOriginal);numel(radialPeaksAfter3); ...
        numel(radialPeaksAfter23)], ...
    [joinNumericVector(radialPeaksOriginal); ...
        joinNumericVector(radialPeaksAfter3); ...
        joinNumericVector(radialPeaksAfter23)], ...
    'VariableNames',{'case_name','mean_radius','std_radius', ...
    'num_detected_peaks','detected_peak_radii'});

disp(radialAuditTable);

fprintf('Coeficiente teorico total n=3:\n');
fprintf('  c3^- = %.12g %+.12gi\n',real(cMinusVec(index3)), ...
    imag(cMinusVec(index3)));
fprintf('  c3^+ = %.12g %+.12gi\n',real(cPlusVec(index3)), ...
    imag(cPlusVec(index3)));

figure('Name','Auditoria radial: original y sustracciones pequenas', ...
    'Color','w');
plot(radialCentersOriginal,radialDensityOriginal,'LineWidth',1.3);
hold on;
plot(radialCentersAfter3,radialDensityAfter3,'LineWidth',1.3);
plot(radialCentersAfter23,radialDensityAfter23,'LineWidth',1.3);
grid on;
xlabel('Radio respecto del centro medio');
ylabel('Densidad suavizada');
legend('Original','Despues de n=3','Despues de n=2,3', ...
    'Location','best');
title('Prueba directa de la bimodalidad radial');

%% ========================================================================
% PREPARAR MATRIZ DE GRAM POR BLOQUES LOGARITMICOS DE n
% ========================================================================

gramIndices = unique(round(linspace(1,N,min(N,maxGramPoints)))).';
numGramPoints = numel(gramIndices);

logEdges = linspace(log(2),log(Qmax)+100*eps(log(Qmax)), ...
    numGramBlocks+1);

gramBlockOfTerm = discretize(ellVec,logEdges);
gramBlockOfTerm(isnan(gramBlockOfTerm)) = numGramBlocks;

gramMinus = complex(zeros(numGramPoints,numGramBlocks,'single'));
gramPlus = complex(zeros(numGramPoints,numGramBlocks,'single'));

%% ========================================================================
% BUCLE PRINCIPAL: TESTS 1, 4, 5 Y PARTE DE 6
% ========================================================================

Pminus = complex(zeros(N,1));
Pplus = complex(zeros(N,1));

nextTerm = 1;
maxIncrementIdentityError = 0;
maxConstantCancellationIdentityError = 0;

summaryRows = cell(numel(Qlist),43);
positivityRows = cell(numel(Qlist),17);

blockRows = cell(numel(Qlist)*numHeightBlocks,16);
blockRow = 0;

[constantY,cY] = fitConstantAndCarrier(Y,carrier);

RbothAtQmax = [];
FAtQmax = [];
EAtQmax = [];
PminusAtQmax = [];
PplusAtQmax = [];
cBothAtQmax = NaN;

for qi = 1:numel(Qlist)

    Q = Qlist(qi);

    while nextTerm<=numTerms && qVec(nextTerm)<=Q

        ell = ellVec(nextTerm);
        z = exp(1i*ell*gamma);

        termMinus = cMinusVec(nextTerm).*carrier.*conj(z);
        termPlus = cPlusVec(nextTerm).*carrier.*z;

        oldCombinedResidual = Y-Pminus-Pplus;

        Pminus = Pminus+termMinus;
        Pplus = Pplus+termPlus;

        newCombinedResidual = Y-Pminus-Pplus;

        incrementError = max(abs( ...
            (newCombinedResidual-oldCombinedResidual) ...
            +termMinus+termPlus));

        maxIncrementIdentityError = max( ...
            maxIncrementIdentityError,incrementError);

        gramBlock = gramBlockOfTerm(nextTerm);

        gramMinus(:,gramBlock) = gramMinus(:,gramBlock) ...
            +single(termMinus(gramIndices));

        gramPlus(:,gramBlock) = gramPlus(:,gramBlock) ...
            +single(termPlus(gramIndices));

        nextTerm = nextTerm+1;
    end

    numTermsUsed = nextTerm-1;

    % Cuatro residuos pedidos.
    RminusOnlyRaw = Y-Pminus;
    RplusOnlyRaw = Y-Pplus;
    RbothRaw = Y-Pminus-Pplus;

    % CORRECCION: la parte suave esta definida salvo constante aditiva.
    % Se ajustan [constante + portadora] conjuntamente en cada residuo.
    [constantMinus,cMinusResidual] = ...
        fitConstantAndCarrier(RminusOnlyRaw,carrier);

    [constantPlus,cPlusResidual] = ...
        fitConstantAndCarrier(RplusOnlyRaw,carrier);

    [jointConstant,cBothResidual] = ...
        fitConstantAndCarrier(RbothRaw,carrier);

    RminusOnly = RminusOnlyRaw-constantMinus;
    RplusOnly = RplusOnlyRaw-constantPlus;
    Rboth = RbothRaw-jointConstant;

    E = Rboth-cBothResidual*carrier;
    F = conj(carrier).*Rboth;
    Fc = F-cBothResidual;

    [constantPminus,projectionMinus] = ...
        fitConstantAndCarrier(Pminus,carrier);

    [constantPplus,projectionPlus] = ...
        fitConstantAndCarrier(Pplus,carrier);

    carrierCancellationIdentityError = abs( ...
        cBothResidual-(cY-projectionMinus-projectionPlus));

    constantCancellationIdentityError = abs( ...
        jointConstant-(constantY-constantPminus-constantPplus));

    maxConstantCancellationIdentityError = max( ...
        maxConstantCancellationIdentityError, ...
        constantCancellationIdentityError);

    % TEST 1: energias y termino cruzado.
    energyMinus = mean(abs(Pminus).^2);
    energyPlus = mean(abs(Pplus).^2);
    crossMinusPlus = 2*real(mean(conj(Pminus).*Pplus));
    energyCombined = mean(abs(Pminus+Pplus).^2);

    crossEnergyIdentityError = abs( ...
        energyCombined-(energyMinus+energyPlus+crossMinusPlus));

    % Forma centrada.
    PminusCentered = Pminus-mean(Pminus);
    PplusCentered = Pplus-mean(Pplus);

    centeredEnergyMinus = mean(abs(PminusCentered).^2);
    centeredEnergyPlus = mean(abs(PplusCentered).^2);

    centeredCross = 2*real(mean( ...
        conj(PminusCentered).*PplusCentered));

    centeredEnergyCombined = mean(abs( ...
        PminusCentered+PplusCentered).^2);

    % TEST 5: ecuacion funcional discreta y diferencial.
    dgamma = diff(gamma);

    derivativeDefect = diff(Rboth)./dgamma ...
        -1i*omega*0.5*(Rboth(2:end)+Rboth(1:end-1));

    discreteDefect = Rboth(2:end) ...
        -exp(1i*omega*dgamma).*Rboth(1:end-1);

    Fvariance = mean(abs(Fc).^2);
    FmaxDeviation = max(abs(Fc));
    FmeanAbsIncrement = mean(abs(diff(F)));
    FtotalVariation = sum(abs(diff(F)));
    Fanisotropy = complexAnisotropy(Fc,minimumVariance);

    corrGapReal = safeCorrelation(real(Fc),gapBefore);
    corrGapImag = safeCorrelation(imag(Fc),gapBefore);
    corrGapAbs = safeCorrelation(abs(Fc),gapBefore);

    corrGapResidualReal = safeCorrelation(real(Fc),gapResidual);
    corrGapResidualImag = safeCorrelation(imag(Fc),gapResidual);
    corrGapResidualAbs = safeCorrelation(abs(Fc),gapResidual);

    % Bloques de altura.
    heightEdges = round(linspace(1,N+1,numHeightBlocks+1));
    blockMeans = complex(NaN(numHeightBlocks,1));

    for hb = 1:numHeightBlocks

        idx = heightEdges(hb):(heightEdges(hb+1)-1);

        Fb = F(idx);
        Rb = Rboth(idx);
        blockMean = mean(Fb);
        blockMeans(hb) = blockMean;
        Fbc = Fb-blockMean;

        if numel(idx)>=2
            dgb = diff(gamma(idx));

            discreteBlock = Rb(2:end) ...
                -exp(1i*omega*dgb).*Rb(1:end-1);

            derivativeBlock = diff(Rb)./dgb ...
                -1i*omega*0.5*(Rb(2:end)+Rb(1:end-1));

            meanAbsDeltaBlock = mean(abs(diff(Fb)));

            variationPerHeight = sum(abs(diff(Fb))) ...
                /max(gamma(idx(end))-gamma(idx(1)),eps);

            discreteBlockRMS = sqrt(mean(abs(discreteBlock).^2));
            derivativeBlockRMS = sqrt(mean(abs(derivativeBlock).^2));
        else
            meanAbsDeltaBlock = NaN;
            variationPerHeight = NaN;
            discreteBlockRMS = NaN;
            derivativeBlockRMS = NaN;
        end

        blockRow = blockRow+1;

        blockRows(blockRow,:) = { ...
            Q,hb,indices(idx(1)),indices(idx(end)), ...
            gamma(idx(1)),gamma(idx(end)), ...
            real(blockMean),imag(blockMean),mean(abs(Fbc).^2), ...
            max(abs(Fb-cBothResidual)),max(abs(Fbc)), ...
            meanAbsDeltaBlock,variationPerHeight, ...
            complexAnisotropy(Fbc,minimumVariance), ...
            discreteBlockRMS,derivativeBlockRMS};
    end

    FblockMeanStd = sqrt(mean(abs(blockMeans-mean(blockMeans)).^2));

    % TEST 4: positividad elemental/Gram.
    normE2 = mean(abs(E).^2);
    normCarrier2 = mean(abs(carrier).^2);

    innerCarrierE = mean(conj(carrier).*E);
    innerEMinus = mean(conj(E).*Pminus);
    innerEPlus = mean(conj(E).*Pplus);
    innerMinusPlus = mean(conj(Pminus).*Pplus);

    carrierSchur = mean(abs(Rboth).^2) ...
        -abs(mean(conj(carrier).*Rboth))^2/normCarrier2;

    cauchyDetEMinus = normE2*energyMinus-abs(innerEMinus)^2;
    cauchyDetEPlus = normE2*energyPlus-abs(innerEPlus)^2;
    cauchyDetMinusPlus = energyMinus*energyPlus ...
        -abs(innerMinusPlus)^2;

    QEplusMinus = mean(abs(E+Pminus).^2);
    QEminusMinus = mean(abs(E-Pminus).^2);

    polarizationErrorMinus = abs( ...
        0.5*(QEplusMinus+QEminusMinus)-normE2-energyMinus);

    QEplusPlus = mean(abs(E+Pplus).^2);
    QEminusPlus = mean(abs(E-Pplus).^2);

    polarizationErrorPlus = abs( ...
        0.5*(QEplusPlus+QEminusPlus)-normE2-energyPlus);

    positivityRows(qi,:) = { ...
        Q,normE2,carrierSchur, ...
        abs(innerCarrierE),real(innerCarrierE),imag(innerCarrierE), ...
        real(innerEMinus),real(innerEPlus), ...
        cauchyDetEMinus,cauchyDetEPlus,cauchyDetMinusPlus, ...
        QEplusMinus,QEminusMinus,polarizationErrorMinus, ...
        QEplusPlus,QEminusPlus,polarizationErrorPlus};

    if numTermsUsed>0
        currentA = AQ(numTermsUsed);
        currentB = BQ(numTermsUsed);
    else
        currentA = 0;
        currentB = 0;
    end

    summaryRows(qi,:) = { ...
        Q,numTermsUsed, ...
        real(cMinusResidual),imag(cMinusResidual), ...
        real(cPlusResidual),imag(cPlusResidual), ...
        real(cBothResidual),imag(cBothResidual),abs(cBothResidual), ...
        abs(cBothResidual-0.5), ...
        real(jointConstant),imag(jointConstant), ...
        real(cBothResidual),imag(cBothResidual),abs(cBothResidual-0.5), ...
        real(projectionMinus),imag(projectionMinus), ...
        real(projectionPlus),imag(projectionPlus), ...
        carrierCancellationIdentityError, ...
        sqrt(mean(abs(RminusOnly).^2)), ...
        sqrt(mean(abs(RplusOnly).^2)), ...
        sqrt(mean(abs(Rboth).^2)),sqrt(normE2), ...
        energyMinus,energyPlus,crossMinusPlus,energyCombined, ...
        crossEnergyIdentityError, ...
        centeredEnergyMinus,centeredEnergyPlus,centeredCross, ...
        centeredEnergyCombined, ...
        Fvariance,FmaxDeviation,FmeanAbsIncrement,FtotalVariation, ...
        FblockMeanStd,Fanisotropy, ...
        sqrt(mean(abs(discreteDefect).^2)), ...
        sqrt(mean(abs(derivativeDefect).^2)), ...
        real(currentA),imag(currentA)};

    fprintf(['Q=%-6g terms=%-5d  c^-res=%.7f%+.7fi  ' ...
        'c^+res=%.7f%+.7fi  c^both=%.7f%+.7fi  ' ...
        'Var(F)=%.4e  RMS(E)=%.4e\n'], ...
        Q,numTermsUsed, ...
        real(cMinusResidual),imag(cMinusResidual), ...
        real(cPlusResidual),imag(cPlusResidual), ...
        real(cBothResidual),imag(cBothResidual), ...
        Fvariance,sqrt(normE2));

    if Q==Qmax
        RbothAtQmax = Rboth;
        FAtQmax = F;
        EAtQmax = E;
        PminusAtQmax = Pminus;
        PplusAtQmax = Pplus;
        cBothAtQmax = cBothResidual;
    end
end

summaryVariableNames = { ...
    'Q','num_prime_power_terms', ...
    'c_after_minus_real','c_after_minus_imag', ...
    'c_after_plus_real','c_after_plus_imag', ...
    'c_after_both_real','c_after_both_imag','c_after_both_abs', ...
    'distance_c_after_both_to_half', ...
    'joint_constant_real','joint_constant_imag', ...
    'joint_carrier_real','joint_carrier_imag', ...
    'distance_joint_carrier_to_half', ...
    'projection_Pminus_real','projection_Pminus_imag', ...
    'projection_Pplus_real','projection_Pplus_imag', ...
    'carrier_cancellation_identity_error', ...
    'rms_centered_Y_minus_Pminus','rms_centered_Y_minus_Pplus', ...
    'rms_centered_Y_minus_both', ...
    'rms_after_both_fitted_carrier', ...
    'energy_Pminus','energy_Pplus', ...
    'cross_term_2Re_inner_Pminus_Pplus', ...
    'energy_Pminus_plus_Pplus','cross_energy_identity_error', ...
    'centered_energy_Pminus','centered_energy_Pplus', ...
    'centered_cross_term','centered_energy_combined', ...
    'F_variance','F_max_abs_deviation_from_mean', ...
    'F_mean_abs_increment','F_total_variation', ...
    'F_block_mean_std','F_anisotropy', ...
    'carrier_discrete_defect_rms','derivative_defect_rms', ...
    'A_Q_real','A_Q_imag'};

summaryTable = cell2table(summaryRows, ...
    'VariableNames',summaryVariableNames);

positivityVariableNames = { ...
    'Q','norm_E2','carrier_schur_complement', ...
    'carrier_projection_abs','carrier_projection_real', ...
    'carrier_projection_imag','Re_inner_E_Pminus', ...
    'Re_inner_E_Pplus','cauchy_det_E_Pminus', ...
    'cauchy_det_E_Pplus','cauchy_det_Pminus_Pplus', ...
    'Q_E_plus_Pminus','Q_E_minus_Pminus', ...
    'polarization_error_minus','Q_E_plus_Pplus', ...
    'Q_E_minus_Pplus','polarization_error_plus'};

positivityTable = cell2table(positivityRows, ...
    'VariableNames',positivityVariableNames);

blockVariableNames = { ...
    'Q','block','k_start','k_end','gamma_start','gamma_end', ...
    'F_mean_real','F_mean_imag','F_variance', ...
    'sup_abs_F_minus_global_c','sup_abs_F_minus_block_c', ...
    'mean_abs_delta_F','variation_per_height','anisotropy', ...
    'carrier_discrete_defect_rms','derivative_defect_rms'};

blockTable = cell2table(blockRows(1:blockRow,:), ...
    'VariableNames',blockVariableNames);

%% ========================================================================
% DISPLAY PRINCIPAL: TEST 1 Y TEST 5
% ========================================================================

fprintf('\n============================================================\n');
fprintf('TEST 1: RAMAS; TEST 5: ECUACION FUNCIONAL\n');
fprintf('============================================================\n');

mainDisplayVariables = { ...
    'Q','num_prime_power_terms', ...
    'c_after_minus_real','c_after_minus_imag', ...
    'c_after_plus_real','c_after_plus_imag', ...
    'c_after_both_real','c_after_both_imag', ...
    'distance_c_after_both_to_half', ...
    'rms_centered_Y_minus_Pminus','rms_centered_Y_minus_Pplus', ...
    'rms_centered_Y_minus_both', ...
    'rms_after_both_fitted_carrier', ...
    'energy_Pminus','energy_Pplus', ...
    'cross_term_2Re_inner_Pminus_Pplus', ...
    'F_variance','F_max_abs_deviation_from_mean', ...
    'F_block_mean_std','F_anisotropy', ...
    'carrier_discrete_defect_rms','derivative_defect_rms'};

disp(summaryTable(:,mainDisplayVariables));

fprintf('max error R_j-R_{j-1}=-P_j                  : %.6e\n', ...
    maxIncrementIdentityError);

fprintf('max error ley de energia de ramas           : %.6e\n', ...
    max(summaryTable.cross_energy_identity_error));

fprintf('max error identidad de proyeccion portadora : %.6e\n', ...
    max(summaryTable.carrier_cancellation_identity_error));
fprintf('max error identidad de constantes            : %.6e\n', ...
    maxConstantCancellationIdentityError);

%% ========================================================================
% TEST 3: TELESCOPADO DENTRO DE CADA PRIMO p
% ========================================================================

[groupSummaryTable,groupPartialTable] = primePowerTelescopingTests( ...
    qVec,basePrimeVec,powerExponentVec,cMinusVec,cPlusVec, ...
    gamma,carrier);

fprintf('\n============================================================\n');
fprintf('TEST 3: TELESCOPADO EN p,p^2,...,p^R\n');
fprintf('============================================================\n');

if isempty(groupSummaryTable)
    fprintf('No hay primos con al menos dos potencias <=Qmax.\n');
else
    [~,orderTelescoping] = sort( ...
        groupSummaryTable.boundary_fit_relative_rms_combined,'ascend');

    numDisplay = min(20,height(groupSummaryTable));

    telescopingDisplayVariables = { ...
        'base_prime','num_powers','largest_power', ...
        'combined_energy_ratio_sum_over_individual', ...
        'combined_rms_over_sum_term_rms', ...
        'boundary_fit_relative_rms_combined', ...
        'boundary_fit_relative_rms_minus', ...
        'boundary_fit_relative_rms_plus', ...
        'boundary_alpha_first_real','boundary_alpha_first_imag', ...
        'boundary_alpha_last_real','boundary_alpha_last_imag', ...
        'tail_primitive_start_abs_minus', ...
        'tail_primitive_start_abs_plus'};

    disp(groupSummaryTable( ...
        orderTelescoping(1:numDisplay), ...
        telescopingDisplayVariables));

    fprintf(['boundary_fit_relative_rms_combined cercano a cero seria ' ...
        'evidencia de colapso a los dos bordes del bloque p^r.\n']);
end

%% ========================================================================
% TEST 4: FUNCIONALES POSITIVOS Y MATRICES DE GRAM
% ========================================================================

Gminus = double(gramMinus);
Gplus = double(gramPlus);

GcombinedCentered = Gminus+Gplus;
GcombinedCentered = GcombinedCentered-mean(GcombinedCentered,1);

GbranchCentered = [ ...
    Gminus-mean(Gminus,1), ...
    Gplus-mean(Gplus,1)];

gramCombined = (GcombinedCentered'*GcombinedCentered)/numGramPoints;
gramBranch = (GbranchCentered'*GbranchCentered)/numGramPoints;

gramCombined = 0.5*(gramCombined+gramCombined');
gramBranch = 0.5*(gramBranch+gramBranch');

eigCombined = sort(real(eig(gramCombined)));
eigBranch = sort(real(eig(gramBranch)));

fprintf('\n============================================================\n');
fprintf('TEST 4: POSITIVIDAD Y GRAM\n');
fprintf('============================================================\n');

positivityDisplayVariables = { ...
    'Q','norm_E2','carrier_schur_complement', ...
    'carrier_projection_abs','Re_inner_E_Pminus', ...
    'Re_inner_E_Pplus','cauchy_det_E_Pminus', ...
    'cauchy_det_E_Pplus','cauchy_det_Pminus_Pplus', ...
    'polarization_error_minus','polarization_error_plus'};

disp(positivityTable(:,positivityDisplayVariables));

fprintf('Gram combinada: min=%.6e, max=%.6e, negativos<-1e-10=%d\n', ...
    min(eigCombined),max(eigCombined),nnz(eigCombined<-1e-10));

fprintf('Gram por ramas: min=%.6e, max=%.6e, negativos<-1e-10=%d\n', ...
    min(eigBranch),max(eigBranch),nnz(eigBranch<-1e-10));

%% ========================================================================
% TEST 5 POR BLOQUES PARA Qmax
% ========================================================================

blockQmax = blockTable(blockTable.Q==Qmax,:);

fprintf('\n============================================================\n');
fprintf('TEST 5: F_Q POR BLOQUES DE ALTURA, Q=%g\n',Qmax);
fprintf('============================================================\n');

blockDisplayVariables = { ...
    'block','gamma_start','gamma_end', ...
    'F_mean_real','F_mean_imag','F_variance', ...
    'sup_abs_F_minus_global_c','sup_abs_F_minus_block_c', ...
    'mean_abs_delta_F','variation_per_height','anisotropy', ...
    'carrier_discrete_defect_rms','derivative_defect_rms'};

disp(blockQmax(:,blockDisplayVariables));

fprintf('Rango Re media por bloque : [%.12g, %.12g]\n', ...
    min(blockQmax.F_mean_real),max(blockQmax.F_mean_real));

fprintf('Rango Im media por bloque : [%.12g, %.12g]\n', ...
    min(blockQmax.F_mean_imag),max(blockQmax.F_mean_imag));

fprintf('Max sup global por bloque : %.6e\n', ...
    max(blockQmax.sup_abs_F_minus_global_c));

fprintf('Max sup local por bloque  : %.6e\n', ...
    max(blockQmax.sup_abs_F_minus_block_c));

%% ========================================================================
% TEST 6: FRECUENCIAS OMITIDAS
% ========================================================================

spectralIndices = unique(round(linspace(1,N, ...
    min(N,maxSpectralPoints)))).';

Ts = gamma(spectralIndices);
Fs = FAtQmax(spectralIndices)-cBothAtQmax;
Es = EAtQmax(spectralIndices);

testStart = Qmax+1;
testEnd = Qmax+omittedTestWidth;
nCandidates = (testStart:testEnd).';

[qTestAll,pTestAll,rTestAll,lambdaTestAll] = makePrimePowers(testEnd);

[isPrimePowerCandidate,locPP] = ismember(nCandidates,qTestAll);

candidateLambda = zeros(size(nCandidates));
candidateBasePrime = zeros(size(nCandidates));
candidateExponent = zeros(size(nCandidates));

candidateLambda(isPrimePowerCandidate) = ...
    lambdaTestAll(locPP(isPrimePowerCandidate));

candidateBasePrime(isPrimePowerCandidate) = ...
    pTestAll(locPP(isPrimePowerCandidate));

candidateExponent(isPrimePowerCandidate) = ...
    rTestAll(locPP(isPrimePowerCandidate));

omittedRows = cell(numel(nCandidates),19);

for jj = 1:numel(nCandidates)

    n = nCandidates(jj);
    ell = log(n);

    basisMinusF = exp(-1i*ell*Ts);
    basisPlusF = exp(1i*ell*Ts);

    fitMinusF = fitCarrier(Fs,basisMinusF);
    fitPlusF = fitCarrier(Fs,basisPlusF);

    basisMinusR = exp(1i*(omega-ell)*Ts);
    basisPlusR = exp(1i*(omega+ell)*Ts);

    fitMinusR = fitCarrier(Es,basisMinusR);
    fitPlusR = fitCarrier(Es,basisPlusR);

    theoryMinus = 0;
    theoryPlus = 0;

    if isPrimePowerCandidate(jj)
        lam = candidateLambda(jj);

        theoryMinus = 1i*lam / ...
            (2*pi*sqrt(n)*(omega-ell));

        theoryPlus = 1i*lam / ...
            (2*pi*sqrt(n)*(omega+ell));
    end

    omittedRows(jj,:) = { ...
        n,isPrimePowerCandidate(jj),candidateBasePrime(jj), ...
        candidateExponent(jj),candidateLambda(jj), ...
        real(fitMinusF),imag(fitMinusF),abs(fitMinusF), ...
        real(fitPlusF),imag(fitPlusF),abs(fitPlusF), ...
        real(fitMinusR),imag(fitMinusR), ...
        real(fitPlusR),imag(fitPlusR), ...
        real(theoryMinus),imag(theoryMinus), ...
        real(theoryPlus),imag(theoryPlus)};
end

omittedVariableNames = { ...
    'n','is_prime_power','base_prime','power_exponent','Lambda_n', ...
    'fit_F_minus_real','fit_F_minus_imag','fit_F_minus_abs', ...
    'fit_F_plus_real','fit_F_plus_imag','fit_F_plus_abs', ...
    'fit_R_minus_real','fit_R_minus_imag', ...
    'fit_R_plus_real','fit_R_plus_imag', ...
    'theory_minus_real','theory_minus_imag', ...
    'theory_plus_real','theory_plus_imag'};

omittedTable = cell2table(omittedRows, ...
    'VariableNames',omittedVariableNames);

ppMask = omittedTable.is_prime_power;
nullMask = ~ppMask;

medianPPMinus = median(omittedTable.fit_F_minus_abs(ppMask));
medianNullMinus = median(omittedTable.fit_F_minus_abs(nullMask));

medianPPPlus = median(omittedTable.fit_F_plus_abs(ppMask));
medianNullPlus = median(omittedTable.fit_F_plus_abs(nullMask));

omittedPPMask = qTestAll>Qmax & qTestAll<=testEnd;
omittedPP = qTestAll(omittedPPMask);
omittedPPLambda = lambdaTestAll(omittedPPMask);

Xomitted = complex(zeros(numel(Ts),2*numel(omittedPP)));

for jj = 1:numel(omittedPP)
    ell = log(omittedPP(jj));
    Xomitted(:,jj) = exp(-1i*ell*Ts);
    Xomitted(:,numel(omittedPP)+jj) = exp(1i*ell*Ts);
end

if isempty(Xomitted)
    fittedOmittedCoefficients = [];
    FsAfterOmittedFit = Fs;
    omittedExplainedFraction = NaN;
    fittedTheoryCorrelation = NaN;
    relativeTheoryCoefficientError = NaN;
else
    fittedOmittedCoefficients = Xomitted\Fs;
    FsAfterOmittedFit = Fs-Xomitted*fittedOmittedCoefficients;

    omittedExplainedFraction = 1 ...
        -sum(abs(FsAfterOmittedFit).^2)/sum(abs(Fs).^2);

    theoryOmittedCoefficients = complex(zeros(2*numel(omittedPP),1));

    for jj = 1:numel(omittedPP)

        n = omittedPP(jj);
        ell = log(n);
        lam = omittedPPLambda(jj);

        theoryOmittedCoefficients(jj) = 1i*lam / ...
            (2*pi*sqrt(n)*(omega-ell));

        theoryOmittedCoefficients(numel(omittedPP)+jj) = 1i*lam / ...
            (2*pi*sqrt(n)*(omega+ell));
    end

    fittedTheoryCorrelation = complexVectorCorrelation( ...
        fittedOmittedCoefficients,theoryOmittedCoefficients);

    relativeTheoryCoefficientError = norm( ...
        fittedOmittedCoefficients-theoryOmittedCoefficients) ...
        /max(norm(theoryOmittedCoefficients),eps);
end

nuMax = log(testEnd);
nuGrid = linspace(-nuMax,nuMax,numFrequencyGridPoints).';
frequencyAmplitude = zeros(size(nuGrid));

for jj = 1:numel(nuGrid)
    basis = exp(1i*nuGrid(jj)*Ts);
    frequencyAmplitude(jj) = abs(fitCarrier(Fs,basis));
end

[sortedAmplitude,sortOrder] = sort(frequencyAmplitude,'descend');
topCount = min(30,numel(sortOrder));

topFrequencyTable = table( ...
    (1:topCount).', ...
    nuGrid(sortOrder(1:topCount)), ...
    sortedAmplitude(1:topCount), ...
    'VariableNames',{'rank','demodulated_frequency','fit_amplitude'});

uniquenessTable = table( ...
    Qmax,numel(omittedPP), ...
    medianPPMinus,medianNullMinus,medianPPMinus/medianNullMinus, ...
    medianPPPlus,medianNullPlus,medianPPPlus/medianNullPlus, ...
    omittedExplainedFraction, ...
    real(fittedTheoryCorrelation),imag(fittedTheoryCorrelation), ...
    abs(fittedTheoryCorrelation),relativeTheoryCoefficientError, ...
    mean(abs(Fs).^2),mean(abs(FsAfterOmittedFit).^2), ...
    complexAnisotropy(Fs,minimumVariance), ...
    safeCorrelation(real(Fs),gapBefore(spectralIndices)), ...
    safeCorrelation(imag(Fs),gapBefore(spectralIndices)), ...
    safeCorrelation(abs(Fs),gapBefore(spectralIndices)), ...
    'VariableNames',{ ...
    'Qmax','num_omitted_prime_powers_joint_fit', ...
    'median_minus_amplitude_prime_power', ...
    'median_minus_amplitude_null', ...
    'minus_prime_power_to_null_ratio', ...
    'median_plus_amplitude_prime_power', ...
    'median_plus_amplitude_null', ...
    'plus_prime_power_to_null_ratio', ...
    'joint_omitted_explained_fraction', ...
    'fit_theory_correlation_real','fit_theory_correlation_imag', ...
    'fit_theory_correlation_abs','relative_theory_coefficient_error', ...
    'F_energy_before_omitted_fit','F_energy_after_omitted_fit', ...
    'F_anisotropy','corr_gap_realF','corr_gap_imagF','corr_gap_absF'});

fprintf('\n============================================================\n');
fprintf('TEST 6: UNICIDAD Y FRECUENCIAS OMITIDAS\n');
fprintf('============================================================\n');

disp(uniquenessTable);

omittedPrimePowerOnly = omittedTable(omittedTable.is_prime_power,:);

if ~isempty(omittedPrimePowerOnly)

    omittedPrimePowerOnly.max_branch_fit_abs = max( ...
        omittedPrimePowerOnly.fit_F_minus_abs, ...
        omittedPrimePowerOnly.fit_F_plus_abs);

    omittedPrimePowerOnly = sortrows( ...
        omittedPrimePowerOnly,'max_branch_fit_abs','descend');

    numDisplay = min(20,height(omittedPrimePowerOnly));

    fprintf('\nPotencias primas omitidas con mayor amplitud:\n');

    disp(omittedPrimePowerOnly(1:numDisplay,{ ...
        'n','base_prime','power_exponent','Lambda_n', ...
        'fit_F_minus_real','fit_F_minus_imag','fit_F_minus_abs', ...
        'fit_F_plus_real','fit_F_plus_imag','fit_F_plus_abs', ...
        'theory_minus_real','theory_minus_imag', ...
        'theory_plus_real','theory_plus_imag', ...
        'max_branch_fit_abs'}));
end

fprintf('\nFrecuencias no nulas dominantes de F_Q-mean(F_Q):\n');
disp(topFrequencyTable);

fprintf('\nDIAGNOSTICO FINAL PARA Q=%g\n',Qmax);
fprintf('mean(F_Q)                         = %.12g %+.12gi\n', ...
    real(cBothAtQmax),imag(cBothAtQmax));
fprintf('|mean(F_Q)-1/2|                  = %.6e\n', ...
    abs(cBothAtQmax-0.5));
fprintf('Var(F_Q)                         = %.6e\n', ...
    mean(abs(FAtQmax-cBothAtQmax).^2));
fprintf('sup |F_Q-mean(F_Q)|              = %.6e\n', ...
    max(abs(FAtQmax-cBothAtQmax)));
fprintf('RMS E_Q                          = %.6e\n', ...
    sqrt(mean(abs(EAtQmax).^2)));
fprintf('razon omitidas potencia/null (-) = %.6f\n', ...
    medianPPMinus/medianNullMinus);
fprintf('razon omitidas potencia/null (+) = %.6f\n', ...
    medianPPPlus/medianNullPlus);
fprintf('fraccion explicada ajuste omitido= %.6f\n', ...
    omittedExplainedFraction);

%% ========================================================================
% FIGURAS: NO SE CIERRA NINGUNA
% ========================================================================

figure('Name','Coeficientes de portadora por rama','Color','w');
tiledlayout(2,1,'TileSpacing','compact','Padding','compact');

nexttile;
semilogx(max(summaryTable.Q,1), ...
    summaryTable.c_after_minus_real,'-o','LineWidth',1.2);
hold on;
semilogx(max(summaryTable.Q,1), ...
    summaryTable.c_after_plus_real,'-o','LineWidth',1.2);
semilogx(max(summaryTable.Q,1), ...
    summaryTable.c_after_both_real,'-o','LineWidth',1.2);
yline(0.5,':');
grid on;
xlabel('Q');
ylabel('Parte real');
legend('Y-P^-','Y-P^+','Y-P^--P^+','1/2','Location','best');
title('Coeficiente ajustado de exp(i omega T)');

nexttile;
semilogx(max(summaryTable.Q,1), ...
    summaryTable.c_after_minus_imag,'-o','LineWidth',1.2);
hold on;
semilogx(max(summaryTable.Q,1), ...
    summaryTable.c_after_plus_imag,'-o','LineWidth',1.2);
semilogx(max(summaryTable.Q,1), ...
    summaryTable.c_after_both_imag,'-o','LineWidth',1.2);
yline(0,':');
grid on;
xlabel('Q');
ylabel('Parte imaginaria');
legend('Y-P^-','Y-P^+','Y-P^--P^+','0','Location','best');

figure('Name','Energia y termino cruzado de ramas','Color','w');
semilogx(max(summaryTable.Q,1), ...
    summaryTable.energy_Pminus,'-o','LineWidth',1.2);
hold on;
semilogx(max(summaryTable.Q,1), ...
    summaryTable.energy_Pplus,'-o','LineWidth',1.2);
semilogx(max(summaryTable.Q,1), ...
    summaryTable.cross_term_2Re_inner_Pminus_Pplus, ...
    '-o','LineWidth',1.2);
semilogx(max(summaryTable.Q,1), ...
    summaryTable.energy_Pminus_plus_Pplus,'-o','LineWidth',1.2);
grid on;
xlabel('Q');
ylabel('Energia');
legend('||P^-||^2','||P^+||^2','2Re<P^-,P^+>', ...
    '||P^-+P^+||^2','Location','best');
title('Cancelacion entre ramas');

figure('Name','Ecuacion funcional del residuo','Color','w');
tiledlayout(2,2,'TileSpacing','compact','Padding','compact');

nexttile;
semilogx(max(summaryTable.Q,1),summaryTable.F_variance, ...
    '-o','LineWidth',1.2);
grid on;
xlabel('Q');
ylabel('Var(F_Q)');
title('Dependencia residual de T');

nexttile;
semilogx(max(summaryTable.Q,1), ...
    summaryTable.distance_c_after_both_to_half, ...
    '-o','LineWidth',1.2);
grid on;
xlabel('Q');
ylabel('|mean(F_Q)-1/2|');
title('Distancia del coeficiente a 1/2');

nexttile;
semilogx(max(summaryTable.Q,1), ...
    summaryTable.carrier_discrete_defect_rms, ...
    '-o','LineWidth',1.2);
grid on;
xlabel('Q');
ylabel('RMS defecto discreto');
title('R_{k+1}-e^{i omega Delta T}R_k');

nexttile;
semilogx(max(summaryTable.Q,1), ...
    summaryTable.F_block_mean_std, ...
    '-o','LineWidth',1.2);
grid on;
xlabel('Q');
ylabel('STD de medias por bloque');
title('Deriva por altura');

figure('Name','Sumas parciales A_Q y B_Q','Color','w');
tiledlayout(2,1,'TileSpacing','compact','Padding','compact');

nexttile;
plot(qVec,real(AQ),'LineWidth',1);
hold on;
plot(qVec,imag(AQ),'LineWidth',1);
yline(0.5,':');
yline(-0.5,':');
set(gca,'XScale','log');
grid on;
xlabel('Q');
ylabel('A_Q');
legend('Re A_Q','Im A_Q','1/2','-1/2','Location','best');

nexttile;
plot(qVec,real(BQ),'LineWidth',1);
hold on;
plot(qVec,imag(BQ),'LineWidth',1);
yline(0.5,':');
yline(-0.5,':');
set(gca,'XScale','log');
grid on;
xlabel('Q');
ylabel('B_Q');
legend('Re B_Q','Im B_Q','1/2','-1/2','Location','best');

blockSupMatrix = reshape( ...
    blockTable.sup_abs_F_minus_global_c, ...
    numHeightBlocks,numel(Qlist)).';

figure('Name','Desviacion suprema por bloques','Color','w');
imagesc(1:numHeightBlocks,1:numel(Qlist),log10(blockSupMatrix));
colorbar;
yticks(1:numel(Qlist));
yticklabels(string(Qlist));
xlabel('Bloque de altura');
ylabel('Q');
title('log10 sup_{T en I_j}|F_Q(T)-c_Q|');

figure('Name','Eigenvalores de Gram','Color','w');
tiledlayout(1,2,'TileSpacing','compact','Padding','compact');

nexttile;
semilogy(max(eigCombined,eps),'-o');
grid on;
xlabel('Indice');
ylabel('Eigenvalor');
title('Gram combinada');

nexttile;
semilogy(max(eigBranch,eps),'-o');
grid on;
xlabel('Indice');
ylabel('Eigenvalor');
title('Gram por ramas');

figure('Name','Frecuencias omitidas','Color','w');
semilogy(omittedTable.n,omittedTable.fit_F_minus_abs,'.');
hold on;
semilogy(omittedTable.n(ppMask), ...
    omittedTable.fit_F_minus_abs(ppMask),'o');
semilogy(omittedTable.n,omittedTable.fit_F_plus_abs,'.');
semilogy(omittedTable.n(ppMask), ...
    omittedTable.fit_F_plus_abs(ppMask),'s');
grid on;
xlabel('n');
ylabel('Amplitud ajustada');
legend('Rama - todos','Rama - potencias primas', ...
    'Rama + todos','Rama + potencias primas','Location','best');

figure('Name','Espectro no nulo de F_Q','Color','w');
plot(nuGrid,frequencyAmplitude,'LineWidth',1);
grid on;
xlabel('nu en exp(i nu T)');
ylabel('Amplitud');
title(sprintf('F_Q-mean(F_Q), Q=%g',Qmax));

%% ========================================================================
% GUARDADO OPCIONAL; NUNCA ES NECESARIO PARA EJECUTAR
% ========================================================================

if saveResults

    if ~isfolder(outputDirectory)
        mkdir(outputDirectory);
    end

    writetable(summaryTable, ...
        fullfile(outputDirectory,'SIX_TESTS_SUMMARY.csv'));

    writetable(coefficientCutoffDisplay, ...
        fullfile(outputDirectory,'COEFFICIENT_CUTOFF_SUMMARY.csv'));

    writetable(groupSummaryTable, ...
        fullfile(outputDirectory,'TELESCOPING_SUMMARY.csv'));

    writetable(groupPartialTable, ...
        fullfile(outputDirectory,'TELESCOPING_PARTIALS.csv'));

    writetable(positivityTable, ...
        fullfile(outputDirectory,'POSITIVITY_FUNCTIONALS.csv'));

    writetable(blockTable, ...
        fullfile(outputDirectory,'BLOCKWISE_FUNCTIONAL_EQUATION.csv'));

    writetable(omittedTable, ...
        fullfile(outputDirectory,'OMITTED_FREQUENCIES.csv'));

    writetable(uniquenessTable, ...
        fullfile(outputDirectory,'UNIQUENESS_SUMMARY.csv'));

    save(fullfile(outputDirectory,'ALL_RESULTS.mat'), ...
        'summaryTable','coefficientCutoffDisplay','radialAuditTable', ...
        'groupSummaryTable','groupPartialTable', ...
        'positivityTable','blockTable','omittedTable', ...
        'uniquenessTable','topFrequencyTable', ...
        'gramCombined','gramBranch','eigCombined','eigBranch', ...
        'RbothAtQmax','FAtQmax','EAtQmax', ...
        'PminusAtQmax','PplusAtQmax','cBothAtQmax','-v7.3');

    fprintf('\nResultados guardados en %s\n',outputDirectory);
end

fprintf('\n============================================================\n');
fprintf('TERMINADO\n');
fprintf('Tablas disponibles directamente en el workspace:\n');
fprintf('  radialAuditTable\n');
fprintf('  summaryTable\n');
fprintf('  coefficientCutoffDisplay\n');
fprintf('  groupSummaryTable\n');
fprintf('  groupPartialTable\n');
fprintf('  positivityTable\n');
fprintf('  blockQmax\n');
fprintf('  omittedTable\n');
fprintf('  uniquenessTable\n');
fprintf('  topFrequencyTable\n');
fprintf('============================================================\n');

%% ========================================================================
% FUNCIONES LOCALES
% ========================================================================

function c = fitCarrier(z,b)

    z = z(:);
    b = b(:);

    denominator = b'*b;

    if abs(denominator)<=eps
        c = NaN;
    else
        c = (b'*z)/denominator;
    end
end

function [a,c] = fitConstantAndCarrier(z,b)

    z = z(:);
    b = b(:);

    X = [ones(size(b)),b];
    coefficients = X\z;

    a = coefficients(1);
    c = coefficients(2);
end

function value = complexAnisotropy(z,minimumVariance)

    z = z(:);
    z = z-mean(z,'omitnan');

    denominator = mean(abs(z).^2,'omitnan');

    if ~isfinite(denominator) || denominator<=minimumVariance
        value = NaN;
    else
        value = abs(mean(z.^2,'omitnan'))/denominator;
    end
end

function r = safeCorrelation(x,y)

    x = x(:);
    y = y(:);

    valid = isfinite(x) & isfinite(y);

    if nnz(valid)<3
        r = NaN;
        return;
    end

    x = x(valid);
    y = y(valid);

    x = x-mean(x);
    y = y-mean(y);

    denominator = sqrt(sum(abs(x).^2)*sum(abs(y).^2));

    if denominator<=eps
        r = NaN;
    else
        r = real((x'*y)/denominator);
    end
end

function r = complexVectorCorrelation(x,y)

    x = x(:);
    y = y(:);

    valid = isfinite(real(x)) & isfinite(imag(x)) ...
        & isfinite(real(y)) & isfinite(imag(y));

    x = x(valid);
    y = y(valid);

    denominator = norm(x)*norm(y);

    if denominator<=eps
        r = NaN;
    else
        r = (x'*y)/denominator;
    end
end

function [qVec,basePrimeVec,powerExponentVec,lambdaVec] = ...
    makePrimePowers(Qmax)

    if Qmax<2
        qVec = zeros(0,1);
        basePrimeVec = zeros(0,1);
        powerExponentVec = zeros(0,1);
        lambdaVec = zeros(0,1);
        return;
    end

    pList = primes(Qmax);

    qList = zeros(0,1);
    baseList = zeros(0,1);
    exponentList = zeros(0,1);
    lambdaList = zeros(0,1);

    for jj = 1:numel(pList)

        p = pList(jj);
        currentPower = p;
        exponent = 1;

        while currentPower<=Qmax

            qList(end+1,1) = currentPower; %#ok<AGROW>
            baseList(end+1,1) = p; %#ok<AGROW>
            exponentList(end+1,1) = exponent; %#ok<AGROW>
            lambdaList(end+1,1) = log(p); %#ok<AGROW>

            if currentPower>floor(Qmax/p)
                break;
            end

            currentPower = currentPower*p;
            exponent = exponent+1;
        end
    end

    [qVec,order] = sort(qList);
    basePrimeVec = baseList(order);
    powerExponentVec = exponentList(order);
    lambdaVec = lambdaList(order);

    [qVec,uniqueIndex] = unique(qVec,'stable');
    basePrimeVec = basePrimeVec(uniqueIndex);
    powerExponentVec = powerExponentVec(uniqueIndex);
    lambdaVec = lambdaVec(uniqueIndex);
end

function [summaryTable,partialTable] = primePowerTelescopingTests( ...
    qVec,basePrimeVec,powerExponentVec,cMinusVec,cPlusVec, ...
    gamma,carrier)

    uniquePrimes = unique(basePrimeVec);

    keep = false(size(uniquePrimes));

    for jj = 1:numel(uniquePrimes)
        keep(jj) = nnz(basePrimeVec==uniquePrimes(jj))>=2;
    end

    uniquePrimes = uniquePrimes(keep);

    summaryNames = { ...
        'base_prime','num_powers','largest_power', ...
        'combined_energy_ratio_sum_over_individual', ...
        'minus_energy_ratio_sum_over_individual', ...
        'plus_energy_ratio_sum_over_individual', ...
        'combined_rms_over_sum_term_rms', ...
        'boundary_fit_relative_rms_combined', ...
        'boundary_fit_relative_rms_minus', ...
        'boundary_fit_relative_rms_plus', ...
        'boundary_alpha_first_real','boundary_alpha_first_imag', ...
        'boundary_alpha_last_real','boundary_alpha_last_imag', ...
        'tail_primitive_error_minus','tail_primitive_error_plus', ...
        'tail_primitive_start_abs_minus', ...
        'tail_primitive_start_abs_plus'};

    partialNames = { ...
        'base_prime','power_exponent','n_prime_power', ...
        'term_rms_minus','term_rms_plus','term_rms_combined', ...
        'partial_rms_minus','partial_rms_plus','partial_rms_combined', ...
        'partial_coefficient_minus_real', ...
        'partial_coefficient_minus_imag', ...
        'partial_coefficient_plus_real', ...
        'partial_coefficient_plus_imag'};

    if isempty(uniquePrimes)
        summaryTable = cell2table(cell(0,numel(summaryNames)), ...
            'VariableNames',summaryNames);

        partialTable = cell2table(cell(0,numel(partialNames)), ...
            'VariableNames',partialNames);

        return;
    end

    totalPartialRows = 0;

    for jj = 1:numel(uniquePrimes)
        totalPartialRows = totalPartialRows ...
            +nnz(basePrimeVec==uniquePrimes(jj));
    end

    summaryRows = cell(numel(uniquePrimes),numel(summaryNames));
    partialRows = cell(totalPartialRows,numel(partialNames));

    partialRow = 0;

    for jp = 1:numel(uniquePrimes)

        p = uniquePrimes(jp);
        idxTerms = find(basePrimeVec==p);

        [~,order] = sort(powerExponentVec(idxTerms));
        idxTerms = idxTerms(order);

        R = numel(idxTerms);

        sumMinus = complex(zeros(size(gamma)));
        sumPlus = complex(zeros(size(gamma)));

        sumEnergyMinus = 0;
        sumEnergyPlus = 0;
        sumEnergyCombined = 0;
        sumTermRMSCombined = 0;

        firstMinus = [];
        firstPlus = [];
        lastMinus = [];
        lastPlus = [];

        cumulativeCoefficientMinus = 0;
        cumulativeCoefficientPlus = 0;

        for rr = 1:R

            j = idxTerms(rr);
            ell = log(qVec(j));
            z = exp(1i*ell*gamma);

            termMinus = cMinusVec(j).*carrier.*conj(z);
            termPlus = cPlusVec(j).*carrier.*z;
            termCombined = termMinus+termPlus;

            if rr==1
                firstMinus = termMinus;
                firstPlus = termPlus;
            end

            if rr==R
                lastMinus = termMinus;
                lastPlus = termPlus;
            end

            sumMinus = sumMinus+termMinus;
            sumPlus = sumPlus+termPlus;

            termEnergyMinus = mean(abs(termMinus).^2);
            termEnergyPlus = mean(abs(termPlus).^2);
            termEnergyCombined = mean(abs(termCombined).^2);

            sumEnergyMinus = sumEnergyMinus+termEnergyMinus;
            sumEnergyPlus = sumEnergyPlus+termEnergyPlus;
            sumEnergyCombined = sumEnergyCombined+termEnergyCombined;

            sumTermRMSCombined = sumTermRMSCombined ...
                +sqrt(termEnergyCombined);

            cumulativeCoefficientMinus = cumulativeCoefficientMinus ...
                +cMinusVec(j);

            cumulativeCoefficientPlus = cumulativeCoefficientPlus ...
                +cPlusVec(j);

            partialRow = partialRow+1;

            partialRows(partialRow,:) = { ...
                p,powerExponentVec(j),qVec(j), ...
                sqrt(termEnergyMinus),sqrt(termEnergyPlus), ...
                sqrt(termEnergyCombined), ...
                sqrt(mean(abs(sumMinus).^2)), ...
                sqrt(mean(abs(sumPlus).^2)), ...
                sqrt(mean(abs(sumMinus+sumPlus).^2)), ...
                real(cumulativeCoefficientMinus), ...
                imag(cumulativeCoefficientMinus), ...
                real(cumulativeCoefficientPlus), ...
                imag(cumulativeCoefficientPlus)};
        end

        sumCombined = sumMinus+sumPlus;

        energyRatioCombined = mean(abs(sumCombined).^2) ...
            /max(sumEnergyCombined,eps);

        energyRatioMinus = mean(abs(sumMinus).^2) ...
            /max(sumEnergyMinus,eps);

        energyRatioPlus = mean(abs(sumPlus).^2) ...
            /max(sumEnergyPlus,eps);

        rmsOverSumRMS = sqrt(mean(abs(sumCombined).^2)) ...
            /max(sumTermRMSCombined,eps);

        firstCombined = firstMinus+firstPlus;
        lastCombined = lastMinus+lastPlus;

        [relativeCombined,alphaCombined] = boundaryFit( ...
            sumCombined,firstCombined,lastCombined);

        [relativeMinus,~] = boundaryFit( ...
            sumMinus,firstMinus,lastMinus);

        [relativePlus,~] = boundaryFit( ...
            sumPlus,firstPlus,lastPlus);

        cM = cMinusVec(idxTerms);
        cP = cPlusVec(idxTerms);

        % Toda sucesion admite esta primitiva de cola. La identidad es
        % tautologica; lo informativo es su tamano y si existe forma cerrada.
        aM = [-flipud(cumsum(flipud(cM)));0];
        aP = [-flipud(cumsum(flipud(cP)));0];

        primitiveErrorM = max(abs(cM-(aM(2:end)-aM(1:end-1))));
        primitiveErrorP = max(abs(cP-(aP(2:end)-aP(1:end-1))));

        summaryRows(jp,:) = { ...
            p,R,max(qVec(idxTerms)), ...
            energyRatioCombined,energyRatioMinus,energyRatioPlus, ...
            rmsOverSumRMS, ...
            relativeCombined,relativeMinus,relativePlus, ...
            real(alphaCombined(1)),imag(alphaCombined(1)), ...
            real(alphaCombined(2)),imag(alphaCombined(2)), ...
            primitiveErrorM,primitiveErrorP, ...
            abs(aM(1)),abs(aP(1))};
    end

    summaryTable = cell2table(summaryRows, ...
        'VariableNames',summaryNames);

    partialTable = cell2table(partialRows(1:partialRow,:), ...
        'VariableNames',partialNames);
end

function [relativeRMS,alpha] = boundaryFit(target,firstTerm,lastTerm)

    target = target(:);
    firstTerm = firstTerm(:);
    lastTerm = lastTerm(:);

    X = [firstTerm,lastTerm];
    alpha = X\target;

    residual = target-X*alpha;

    relativeRMS = sqrt(mean(abs(residual).^2)) ...
        /max(sqrt(mean(abs(target).^2)),eps);
end


function [radius,centers,densitySmooth,peakRadii] = ...
    radialDistributionSummary(z,numBins,smoothWidth)

    z = z(:);
    z = z(isfinite(real(z)) & isfinite(imag(z)));

    center = mean(z);
    radius = abs(z-center);

    rMin = min(radius);
    rMax = max(radius);

    if rMax<=rMin
        rMax = rMin+eps(rMin+1);
    end

    edges = linspace(rMin,rMax,numBins+1);
    density = histcounts(radius,edges,'Normalization','pdf');
    centers = ((edges(1:end-1)+edges(2:end))/2).';

    densitySmooth = smoothdata(density(:),'gaussian',smoothWidth);

    candidates = find( ...
        densitySmooth(2:end-1)>densitySmooth(1:end-2) & ...
        densitySmooth(2:end-1)>=densitySmooth(3:end))+1;

    if isempty(candidates)
        peakRadii = zeros(0,1);
        return;
    end

    candidates = candidates( ...
        densitySmooth(candidates)>=0.12*max(densitySmooth));

    if isempty(candidates)
        peakRadii = zeros(0,1);
        return;
    end

    % Conserva maximos separados al menos seis bins, ordenados por altura.
    [~,heightOrder] = sort(densitySmooth(candidates),'descend');
    selected = zeros(0,1);

    for j = 1:numel(heightOrder)
        candidate = candidates(heightOrder(j));

        if isempty(selected) || all(abs(candidate-selected)>=6)
            selected(end+1,1) = candidate; %#ok<AGROW>
        end

        if numel(selected)>=4
            break;
        end
    end

    peakRadii = sort(centers(selected));
end

function s = joinNumericVector(v)

    v = v(:).';

    if isempty(v)
        s = "";
        return;
    end

    pieces = strings(size(v));

    for j = 1:numel(v)
        pieces(j) = sprintf('%.9g',v(j));
    end

    s = strjoin(pieces,', ');
end


