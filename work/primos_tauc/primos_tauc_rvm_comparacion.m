function primos_tauc_rvm_comparacion
% PRIMOS_TAUC_RVM_COMPARACION
% Script independiente: solo necesita zeross.bin (float64 little-endian) en la carpeta actual de MATLAB.
%
% 1) Reloj RvM:  N0(tau_k) = k - 1/2,   N0(t) = t/(2 pi) (log(t/(2 pi)) - 1) + 7/8,   L(t) = log(t/(2 pi))/(2 pi).
% 2) tauc_k = mejor construccion Casaña sin ceros existente (ordinal_prime_cutoff v17, Teorema F;
%    LawCasanya work/v15_prep/opc_task3 etapa A + opc_task4, RMS 0.0128 en altura en el bloque de test):
%    F_Y(t) = N0(t) + S_Y(t),  S_Y(t) = -(1/pi) sum_{n = p^m <= Y} sin(t log n)/(m sqrt(n))  (potencias de primo, corte duro).
%    Etapa A: X_mon(k) = mayor potencia de primo n con B(n) = sum_{n'<=n} Lambda(n')/sqrt(n') <= (1-eta)/2 log((tau_k-1)/2pi),
%             eta = 0.1; entonces F_X' >= eta L en [tau_k - 1, inf) y la raiz de F_X = k - 1/2 se obtiene por biseccion.
%    Etapa B: continuacion de la raiz en 8 cortes geometricos de X_mon a Y_max = (tau_k/2pi)^c, c = 1.30; en cada nivel
%             Newton (7 pasos, paso acotado por 0.25/L) y aceptacion solo si residuo < 1e-9 y F_Y' > 0.1 L, F_prev' > 0.1 L
%             en 3 puntos del segmento entre raices; si falla, el indice se queda en su ultimo corte aceptado.
%    La construccion no usa ceros de zeta; gamma_k se lee solo para medir errores.
% 3) zeta de cada lista kappa (gamma, tau, tauc), producto de Hadamard:
%    zeta_kappa(s) = xi(1/2) prod_k (1 + (s - 1/2)^2/kappa_k^2) / G(s),  G(s) = (1/2) s (s-1) pi^(-s/2) Gamma(s/2);
%    ceros en 1/2 +- i kappa_k.  En la recta critica: Z_kappa(t) = -xi(1/2) prod_k (1 - t^2/kappa_k^2) / |G(1/2 + i t)|.
% 4) Primos de cada zeta por la formula explicita de Riemann con los ceros de zeta_kappa (v26, ecs. (6.2), (6.4)):
%    J_kappa(x)  = li(x) - 2 Re sum_k w_k Ei((1/2 + i kappa_k) log x) - log 2 + int_x^inf dy/(y (y^2-1) log y),
%    pi_kappa(x) = sum_{1 <= m <= log2 x} mu(m)/m J*_kappa(x^(1/m)),  J* = 0 en (0,2).
%    w_k: corte suave comun a las tres listas, funcion de tau_k.  Ei(W) = -E1(-W) para Im W > 0 (v26, ec. (6.1)).
%    Niveles primos: p_j^kappa = primer x con pi_kappa(x) >= j (v26) y q_j^kappa = primer x con pi_kappa(x) >= j - 1/2
%    (semi-nivel), malla en log x + biseccion.
% 5) Comparacion uno a uno de p_j, p_j^gamma, p_j^RvM, p_j^tauc para j <= pi(xmax), y cota exacta
%    |pi_kappa - pi_gamma| <= B_kappa E(x) (seccion 4b).
%
% Salida en ./salida_primos_tauc/ : consola.txt, tablas .csv, resultados.mat, figuras .png. Las figuras no se cierran.

clc
clear

%% ------------------------------------------------------------------ parametros
xmax      = 1000;                 % rango de x para pi
Nu        = 20000;                % puntos de la malla en u = log x
fK        = 2.5;                  % ordenadas usadas: tau_K <= fK * 2 pi * xmax (v26, Experimento 19.9)
cutStart  = 0.5;                  % corte suave: peso 1 si tau_k <= cutStart*tau_K, coseno^2 hasta tau_K
cTauc     = 1.30;                 % exponente final del corte de la construccion Casaña, Y_max = (tau/2pi)^c
etaMon    = 0.1;                  % margen de la etapa A
nNiveles  = 8;                    % niveles de la continuacion
nNewton   = 7;                    % pasos de Newton por nivel
pSplit    = 100;                  % separacion de los resumenes por tamaño de p
nBisec    = 25;                   % biseccion de cada nivel p_j
tZ        = linspace(0.5, 100, 4000)';   % malla para Z_kappa en la recta critica
chunk     = 128;                  % filas por bloque en la suma sobre ceros
zfile     = fullfile(pwd, 'zeross.bin');
outdir    = fullfile(pwd, 'salida_primos_tauc');
XI12      = 0.4971207781883141;   % xi(1/2) = -(1/8) pi^(-1/4) Gamma(1/4) zeta(1/2)

if ~exist(outdir, 'dir'), mkdir(outdir); end
dfile = fullfile(outdir, 'consola.txt');
if exist(dfile, 'file') == 2, delete(dfile); end
diary(dfile);
limpieza = onCleanup(@() diary('off'));

TP = 2*pi;
N0 = @(t) t/TP.*(log(t/TP) - 1) + 7/8;
Lp = @(t) log(t/TP)/TP;
tGlobal = tic;

%% ------------------------------------------------------------------ 1. ceros (solo diagnostico)
tauKobj = fK*TP*xmax;
K = floor(N0(tauKobj) + 0.5);
if exist(zfile, 'file') ~= 2
    error('No encuentro %s. Ejecuta desde la carpeta donde esta zeross.bin.', zfile);
end
dz = dir(zfile);
if mod(dz.bytes, 8) ~= 0
    error('%s: tamaño %d no es multiplo de 8.', zfile, dz.bytes);
end
if dz.bytes/8 < K
    error('%s tiene %d ordenadas; se necesitan %d.', zfile, dz.bytes/8, K);
end
fid = fopen(zfile, 'r');
if fid < 0, error('fopen fallo sobre %s', zfile); end
gam = fread(fid, K, 'float64', 0, 'ieee-le');
fclose(fid);
gam = gam(:);
if numel(gam) ~= K || any(~isfinite(gam)) || any(diff(gam) < 0) || abs(gam(1) - 14.134725141734693) > 1e-6
    error('zeross.bin no tiene el formato esperado (float64 little-endian, gamma_1 = 14.1347...).');
end
fprintf('xmax = %d,  K = %d ordenadas (tau_K <= %.1f),  malla Nu = %d\n', xmax, K, tauKobj, Nu);

%% ------------------------------------------------------------------ 2. reloj y tauc
t0 = tic;
k   = (1:K)';
tau = reloj_rvm(k, N0, Lp);
PP  = potencias_primo(ceil(max((tau/TP).^cTauc)) + 2);
[tauc, xA, Xmon, Yfin, acept, bracketOK] = tauc_casana(tau, k, PP, cTauc, etaMon, nNiveles, nNewton, N0, Lp);
fprintf('\nConstruccion Casaña (etapa A + continuacion a (tau/2pi)^%.2f), %.1f s\n', cTauc, toc(t0));
fprintf('  etapa A: X_mon en {%s}, intervalo inicial valido en %.4f de los indices\n', ...
    sprintf('%g ', unique(Xmon)), bracketOK);
fprintf('  aceptacion por nivel: %s\n', sprintf('%.4f ', acept));
cfin = log(Yfin)./log(tau/TP);
alto = tau > 100;
fprintf('  exponente final log Y/log(tau/2pi) (tau > 100): cuantiles 1%%, 10%%, 50%% = %.3f %.3f %.3f\n', ...
    cuantil(cfin(alto), 0.01), cuantil(cfin(alto), 0.10), cuantil(cfin(alto), 0.50));
iY = find(Yfin < xmax, 1, 'last');
if isempty(iY), iY = 0; end
fprintf('  ceros con corte final Y_k >= xmax = %d: k > %d (tau_k > %.1f), %d de %d\n', ...
    xmax, iY, tau(max(iY, 1)), sum(Yfin >= xmax), K);

e0 = tau  - gam;
eA = xA   - gam;
e1 = tauc - gam;
fprintf('\nOrdenadas frente a gamma_k (solo diagnostico), k <= %d:\n', K);
fprintf('  RMS |tau - gamma|     = %.6f    max = %.6f\n', sqrt(mean(e0.^2)), max(abs(e0)));
fprintf('  RMS |etapa A - gamma| = %.6f    max = %.6f\n', sqrt(mean(eA.^2)), max(abs(eA)));
fprintf('  RMS |tauc - gamma|    = %.6f    max = %.6f\n', sqrt(mean(e1.^2)), max(abs(e1)));
fprintf('  inversiones tauc_{k+1} <= tauc_k: %d\n', sum(diff(tauc) <= 0));
fprintf('\n  %-18s %7s %12s %12s\n', 'ventana gamma', 'n', 'RMS reloj', 'RMS tauc');
for a = floor(log2(gam(1))):floor(log2(gam(end)))
    idx = gam >= 2^a & gam < 2^(a+1);
    if any(idx)
        fprintf('  [%7d,%7d) %7d %12.6f %12.6f\n', 2^a, 2^(a+1), sum(idx), ...
            sqrt(mean(e0(idx).^2)), sqrt(mean(e1(idx).^2)));
    end
end

%% ------------------------------------------------------------------ 3. zeta de cada lista en la recta critica
Zg = Z_lista(tZ, gam,  XI12);
Zr = Z_lista(tZ, tau,  XI12);
Zc = Z_lista(tZ, tauc, XI12);
Ztrue = [];
tZt = tZ(1:20:end);
try
    th = imag(lgamma_c(0.25 + 0.5i*tZt)) - 0.5*tZt*log(pi);
    Ztrue = real(exp(1i*th).*zeta(0.5 + 1i*tZt));
    fprintf('\nZ(t) de la funcion zeta de MATLAB evaluada en %d puntos (control).\n', numel(tZt));
catch
    fprintf('\nFuncion zeta compleja no disponible: el control de Z se hace con la lista gamma.\n');
end

%% ------------------------------------------------------------------ 4. primos de cada zeta
s = tau/tau(end);
w = ones(K, 1);
iw = s > cutStart;
w(iw) = cos(0.5*pi*(s(iw) - cutStart)/(1 - cutStart)).^2;

tab = tabla_cola();

ug = linspace(log(2), log(xmax), Nu)';
xg = exp(ug);
xh = (2:xmax-1)' + 0.5;               % semienteros: pi(n + 1/2) = pi(n)
pr = primes(xmax);
pr = pr(:);
nP = numel(pr);

listas  = {gam, tau, tauc};
nombres = {'gamma', 'RvM', 'tauc'};
Pg = zeros(Nu, 3);
Ph = zeros(numel(xh), 3);
fprintf('\n');
for L = 1:3
    t0 = tic;
    Pg(:, L) = pi_lista(xg, listas{L}, w, tab, chunk);
    Ph(:, L) = pi_lista(xh, listas{L}, w, tab, chunk);
    fprintf('pi_%s calculada en malla y semienteros (%.1f s)\n', nombres{L}, toc(t0));
end
piG = sum(bsxfun(@le, pr', xg), 2);
piH = sum(bsxfun(@le, pr', xh), 2);
liG = li_real(xg);
liH = li_real(xh);

%% ------------------------------------------------------------------ 4b. cota exacta de |pi_X - pi_gamma|
% |d/dlambda Ei((1/2 + i lambda) u)| = sqrt(x)/|1/2 + i lambda|, luego
%   |J_X(x) - J_gamma(x)|   <= B_X sqrt(x),   B_X = 2 sum_k w_k |kappa_k - gamma_k| / min(kappa_k, gamma_k),
%   |pi_X(x) - pi_gamma(x)| <= B_X E(x),      E(x) = sum_{mu(m) ~= 0, x^(1/m) >= 2} x^(1/(2m)) / m.
Ex = envolvente(xg);
Bx = zeros(1, 3);
fprintf('\nCOTA EXACTA: |pi_X(x) - pi_gamma(x)| <= B_X E(x),  E(x) = sum_{mu(m)~=0} x^(1/(2m))/m\n');
for L = 2:3
    Bx(L) = 2*sum(w.*abs(listas{L} - gam)./min(listas{L}, gam));
    r = max(abs(Pg(:, L) - Pg(:, 1))./(Bx(L)*Ex));
    fprintf('  %-6s B_X = %.5f   max_x |pi_X - pi_gamma| / (B_X E(x)) = %.4f   (la cota exige <= 1)\n', ...
        nombres{L}, Bx(L), r);
end
fprintf('  sumas parciales sin pesos  sum_{gamma_k <= T} |kappa_k - gamma_k| / gamma_k:\n');
fprintf('  %10s %12s %12s\n', 'T', 'RvM', 'tauc');
cs1 = cumsum(abs(e0)./gam);
cs2 = cumsum(abs(e1)./gam);
for a = 5:floor(log2(gam(end)))
    i = find(gam <= 2^a, 1, 'last');
    if isempty(i), continue; end
    fprintf('  %10d %12.5f %12.5f\n', 2^a, cs1(i), cs2(i));
end
fprintf('  %10.1f %12.5f %12.5f\n', gam(end), cs1(end), cs2(end));

%% ------------------------------------------------------------------ 4c. sumas de Landau
% Landau (1911): sum_{0 < gamma <= T} n^{i gamma} = -(T/2pi) Lambda(n)/sqrt(n) + O(log T) para n fijo.
% Una lista que reproduce los saltos de pi en n debe reproducir este termino lineal en T.
nL = [2 3 4 5 6 7 8 9 10 11 12 13 16 25 30 49 97 101 500 997 1000 2003 5003];
TL = gam(end);
fprintf('\nSUMAS DE LANDAU  sum_{k <= %d} n^{i kappa_k}  frente a  -(T/2pi) Lambda(n)/sqrt(n),  T = %.1f\n', K, TL);
fprintf('%6s %12s %24s %24s %24s\n', 'n', 'Landau', 'gamma', 'RvM', 'tauc');
SL = zeros(numel(nL), 3);
for i = 1:numel(nL)
    for L = 1:3
        SL(i, L) = sum(exp(1i*log(nL(i))*listas{L}));
    end
    fprintf('%6d %12.2f   %10.2f %+10.2fi   %10.2f %+10.2fi   %10.2f %+10.2fi\n', nL(i), ...
        -TL/(2*pi)*mangoldt(nL(i))/sqrt(nL(i)), real(SL(i,1)), imag(SL(i,1)), ...
        real(SL(i,2)), imag(SL(i,2)), real(SL(i,3)), imag(SL(i,3)));
end

%% ------------------------------------------------------------------ niveles p_j^kappa y q_j^kappa
% p_j^kappa = inf{x : pi_kappa(x) >= j}        (definicion de v26)
% q_j^kappa = inf{x : pi_kappa(x) >= j - 1/2}  (semi-nivel: punto medio del salto de pi en p_j)
fprintf('\n');
Pj = nan(nP, 3);
Qj = nan(nP, 3);
for L = 1:3
    t0 = tic;
    Pj(:, L) = niveles(xg, Pg(:, L), (1:nP)',       listas{L}, w, tab, chunk, nBisec);
    Qj(:, L) = niveles(xg, Pg(:, L), (1:nP)' - 0.5, listas{L}, w, tab, chunk, nBisec);
    fprintf('niveles p_j^%s y q_j^%s calculados (%.1f s)\n', nombres{L}, nombres{L}, toc(t0));
end

%% ------------------------------------------------------------------ 5. comparacion uno a uno
D  = Pj - repmat(pr, 1, 3);                        % p_j^kappa - p_j
DQ = Qj - repmat(pr, 1, 3);                        % q_j^kappa - p_j
masCerca  = abs(D(:,3))  < abs(D(:,2));            % tauc mas cerca de p_j que RvM (nivel j)
masCercaQ = abs(DQ(:,3)) < abs(DQ(:,2));           % idem con el semi-nivel
redondeo  = round(Pj) == repmat(pr, 1, 3);         % entero mas cercano = p_j
redondeoQ = round(Qj) == repmat(pr, 1, 3);

fprintf('\nCOMPARACION UNO A UNO, NIVEL j:  p_j^X = inf{x: pi_X(x) >= j},  d = p_j^X - p_j\n');
fprintf('tc = "*" si tauc esta mas cerca de p_j que RvM\n');
fprintf('%5s %6s %11s %11s %11s %10s %10s %10s %3s\n', ...
    'j', 'p_j', 'p_j^gamma', 'p_j^RvM', 'p_j^tauc', 'd_gamma', 'd_RvM', 'd_tauc', 'tc');
for j = 1:nP
    fprintf('%5d %6d %11.5f %11.5f %11.5f %10.5f %10.5f %10.5f %3s\n', ...
        j, pr(j), Pj(j,1), Pj(j,2), Pj(j,3), D(j,1), D(j,2), D(j,3), marca(masCerca(j)));
end

fprintf('\nCOMPARACION UNO A UNO, SEMI-NIVEL j - 1/2:  q_j^X = inf{x: pi_X(x) >= j - 1/2},  dq = q_j^X - p_j\n');
fprintf('%5s %6s %11s %11s %11s %10s %10s %10s %3s\n', ...
    'j', 'p_j', 'q_j^gamma', 'q_j^RvM', 'q_j^tauc', 'dq_gamma', 'dq_RvM', 'dq_tauc', 'tc');
for j = 1:nP
    fprintf('%5d %6d %11.5f %11.5f %11.5f %10.5f %10.5f %10.5f %3s\n', ...
        j, pr(j), Qj(j,1), Qj(j,2), Qj(j,3), DQ(j,1), DQ(j,2), DQ(j,3), marca(masCercaQ(j)));
end

fprintf('\nRESUMEN DE NIVELES PRIMOS\n');
grupos = {true(nP,1), pr <= pSplit, pr > pSplit};
gnom   = {sprintf('todos (j <= %d)', nP), sprintf('p_j <= %d', pSplit), sprintf('p_j > %d', pSplit)};
for G = 1:3
    g = grupos{G};
    if ~any(g), continue; end
    fprintf('  %s, %d niveles:\n', gnom{G}, sum(g));
    for L = 1:3
        d  = D(g, L);  d  = d(~isnan(d));
        dq = DQ(g, L); dq = dq(~isnan(dq));
        fprintf('    %-6s nivel j:   media|d| = %8.5f  RMS = %8.5f  max = %8.5f  round = p_j: %3d/%d\n', ...
            nombres{L}, mean(abs(d)), sqrt(mean(d.^2)), max(abs(d)), sum(redondeo(g, L)), sum(g));
        fprintf('    %-6s nivel j-1/2: media|d| = %8.5f  RMS = %8.5f  max = %8.5f  round = p_j: %3d/%d\n', ...
            '', mean(abs(dq)), sqrt(mean(dq.^2)), max(abs(dq)), sum(redondeoQ(g, L)), sum(g));
    end
    fprintf('    tauc mas cerca que RvM: nivel j en %d de %d, semi-nivel en %d de %d\n', ...
        sum(masCerca(g)), sum(g), sum(masCercaQ(g)), sum(g));
end

% criterio exacto del semi-nivel: si |pi_X - pi| < 1/2 fuera de las ventanas |x - p| < eta,
% todos los cruces del nivel j - 1/2 estan en (p_j - eta, p_j + eta)
eta = 0.5;
fuera = true(Nu, 1);
for i = 1:nP
    fuera(abs(xg - pr(i)) < eta) = false;
end
fprintf('\nCRITERIO DEL SEMI-NIVEL (ventanas |x - p| < %.2f):\n', eta);
for L = 1:3
    E = Pg(:, L) - piG;
    malo = find(fuera & abs(E) >= 0.5, 1, 'first');
    if isempty(malo)
        fprintf('  %-6s |pi_X - pi| < 1/2 fuera de ventanas en todo [2, %d]: q_j a menos de %.2f de p_j para todo j\n', ...
            nombres{L}, xmax, eta);
    else
        fprintf('  %-6s primer x con |pi_X - pi| >= 1/2 fuera de ventanas: x = %.3f (pi_X - pi = %+.4f); garantizados los %d primos < %.3f\n', ...
            nombres{L}, xg(malo), E(malo), sum(pr < xg(malo) - eta), xg(malo) - eta);
    end
    fprintf('         sup |pi_X - pi| fuera de ventanas en [2, %d] = %.4f;  |q_j - p_j| < %.2f en %d de %d\n', ...
        xmax, max(abs(E(fuera))), eta, sum(abs(DQ(:, L)) < eta), nP);
end

fprintf('\nRESUMEN DE pi(n) EN SEMIENTEROS n + 1/2, 2 <= n <= %d\n', xmax-1);
rangos = [2 pSplit; pSplit+1 xmax-1; 2 xmax-1];
for r = 1:size(rangos, 1)
    g = xh >= rangos(r,1) & xh <= rangos(r,2) + 1;
    if ~any(g), continue; end
    fprintf('  n en [%d, %d] (%d valores):\n', rangos(r,1), rangos(r,2), sum(g));
    for L = 1:3
        d = Ph(g, L) - piH(g);
        fprintf('    %-6s RMS(pi_X - pi) = %8.5f   max|.| = %8.5f   media = %+8.5f\n', ...
            nombres{L}, sqrt(mean(d.^2)), max(abs(d)), mean(d));
    end
    d = liH(g) - piH(g);
    fprintf('    %-6s RMS(li - pi)   = %8.5f\n', 'li', sqrt(mean(d.^2)));
end
fprintf('\n%8s %6s %11s %11s %11s %11s\n', 'n', 'pi(n)', 'pi_gamma', 'pi_RvM', 'pi_tauc', 'li');
for n = [10 25 50:50:xmax-1]
    i = find(abs(xh - (n + 0.5)) < 1e-9, 1);
    if isempty(i), continue; end
    fprintf('%8d %6d %11.4f %11.4f %11.4f %11.4f\n', n, piH(i), Ph(i,1), Ph(i,2), Ph(i,3), liH(i));
end
fprintf('\nMonotonia en la malla: minimo incremento de pi_X entre puntos consecutivos\n');
for L = 1:3
    fprintf('  %-6s %+.5f\n', nombres{L}, min(diff(Pg(:, L))));
end

%% ------------------------------------------------------------------ 6. ficheros
f1 = fullfile(outdir, 'tabla_primos_uno_a_uno.csv');
fid = abrir(f1);
fprintf(fid, 'j,p_j,p_gamma,p_RvM,p_tauc,q_gamma,q_RvM,q_tauc,d_gamma,d_RvM,d_tauc,dq_gamma,dq_RvM,dq_tauc\n');
for j = 1:nP
    fprintf(fid, '%d,%d,%.10g,%.10g,%.10g,%.10g,%.10g,%.10g,%.10g,%.10g,%.10g,%.10g,%.10g,%.10g\n', j, pr(j), ...
        Pj(j,1), Pj(j,2), Pj(j,3), Qj(j,1), Qj(j,2), Qj(j,3), D(j,1), D(j,2), D(j,3), DQ(j,1), DQ(j,2), DQ(j,3));
end
fclose(fid);

f2 = fullfile(outdir, 'tabla_pi_semienteros.csv');
fid = abrir(f2);
fprintf(fid, 'x,pi,pi_gamma,pi_RvM,pi_tauc,li\n');
fprintf(fid, '%.1f,%d,%.10g,%.10g,%.10g,%.10g\n', [xh piH Ph(:,1) Ph(:,2) Ph(:,3) liH]');
fclose(fid);

f3 = fullfile(outdir, 'ordenadas_gamma_tau_tauc.csv');
fid = abrir(f3);
fprintf(fid, 'k,gamma,tau,etapaA,tauc,Xmon,Yfinal\n');
fprintf(fid, '%d,%.12f,%.12f,%.12f,%.12f,%g,%g\n', [k gam tau xA tauc Xmon Yfin]');
fclose(fid);

f4 = fullfile(outdir, 'Z_recta_critica.csv');
fid = abrir(f4);
fprintf(fid, 't,Z_gamma,Z_RvM,Z_tauc\n');
fprintf(fid, '%.8f,%.12g,%.12g,%.12g\n', [tZ Zg Zr Zc]');
fclose(fid);

save(fullfile(outdir, 'resultados.mat'), 'xmax', 'K', 'Nu', 'fK', 'cutStart', 'cTauc', 'etaMon', ...
    'nNiveles', 'nNewton', 'k', 'gam', 'tau', 'xA', 'tauc', 'Xmon', 'Yfin', 'acept', 'w', ...
    'xg', 'Pg', 'piG', 'liG', 'xh', 'Ph', 'piH', 'liH', 'pr', 'Pj', 'Qj', 'D', 'DQ', 'masCerca', ...
    'tZ', 'Zg', 'Zr', 'Zc', 'Ztrue', 'tZt', 'Bx', 'Ex', 'nL', 'SL');

%% ------------------------------------------------------------------ 7. figuras (no se cierran)
col = [0 0 0; 0 0.35 0.85; 0.85 0.2 0.1; 0.1 0.6 0.2];

fig1 = figure('Color', 'w', 'Name', 'Conteos de primos');
for sp = 1:2
    subplot(2, 1, sp);
    if sp == 1, xl = [2 xmax]; else, xl = [2 min(100, xmax)]; end
    g = xg <= xl(2);
    plot(xg(g), piG(g), '-', 'Color', col(1,:), 'LineWidth', 1.2); hold on
    plot(xg(g), Pg(g,1), '-', 'Color', [0.5 0.5 0.5], 'LineWidth', 0.8);
    plot(xg(g), Pg(g,2), '-', 'Color', col(2,:), 'LineWidth', 1);
    plot(xg(g), Pg(g,3), '-', 'Color', col(3,:), 'LineWidth', 1);
    plot(xg(g), liG(g), '--', 'Color', col(4,:), 'LineWidth', 1);
    xlim(xl); grid on; xlabel('x'); ylabel('conteo');
    legend('\pi(x)', '\pi_\gamma(x)', '\pi_{RvM}(x)', '\pi_{tauc}(x)', 'li(x)', 'Location', 'northwest');
    hold off
end
guardar_png(fig1, fullfile(outdir, 'fig1_conteos.png'));

fig2 = figure('Color', 'w', 'Name', 'Diferencias con pi');
plot(xg, Pg(:,2) - piG, '-', 'Color', col(2,:)); hold on
plot(xg, Pg(:,3) - piG, '-', 'Color', col(3,:));
plot(xg, Pg(:,1) - piG, '-', 'Color', [0.4 0.4 0.4]);
grid on; xlabel('x'); ylabel('\pi_X(x) - \pi(x)');
legend('RvM', 'tauc', '\gamma', 'Location', 'northwest');
hold off
guardar_png(fig2, fullfile(outdir, 'fig2_diferencias.png'));

fig3 = figure('Color', 'w', 'Name', 'Niveles primos uno a uno');
subplot(2, 1, 1);
plot(pr, D(:,2), 's-', 'Color', col(2,:), 'MarkerSize', 4); hold on
plot(pr, D(:,3), 'd-', 'Color', col(3,:), 'MarkerSize', 4);
plot(pr, D(:,1), 'o', 'Color', [0.4 0.4 0.4], 'MarkerSize', 4);
grid on; xlabel('p_j'); ylabel('p_j^X - p_j  (nivel j)');
legend('RvM', 'tauc', '\gamma', 'Location', 'northwest');
hold off
subplot(2, 1, 2);
plot(pr, DQ(:,2), 's-', 'Color', col(2,:), 'MarkerSize', 4); hold on
plot(pr, DQ(:,3), 'd-', 'Color', col(3,:), 'MarkerSize', 4);
plot(pr, DQ(:,1), 'o', 'Color', [0.4 0.4 0.4], 'MarkerSize', 4);
grid on; xlabel('p_j'); ylabel('q_j^X - p_j  (nivel j - 1/2)');
legend('RvM', 'tauc', '\gamma', 'Location', 'northwest');
hold off
guardar_png(fig3, fullfile(outdir, 'fig3_niveles_primos.png'));

fig4 = figure('Color', 'w', 'Name', 'Ordenadas');
semilogy(gam, abs(e0), '.', 'Color', col(2,:), 'MarkerSize', 2); hold on
semilogy(gam, abs(e1), '.', 'Color', col(3,:), 'MarkerSize', 2);
grid on; xlabel('\gamma_k'); ylabel('|ordenada - \gamma_k|');
legend('reloj RvM \tau_k', 'tauc', 'Location', 'southwest');
hold off
guardar_png(fig4, fullfile(outdir, 'fig4_ordenadas.png'));

fig5 = figure('Color', 'w', 'Name', 'Z en la recta critica');
plot(tZ, Zg, '-', 'Color', [0.4 0.4 0.4], 'LineWidth', 1.2); hold on
plot(tZ, Zr, '-', 'Color', col(2,:));
plot(tZ, Zc, '-', 'Color', col(3,:));
if ~isempty(Ztrue)
    plot(tZt, Ztrue, 'k.', 'MarkerSize', 8);
    legend('Z_\gamma', 'Z_{RvM}', 'Z_{tauc}', 'Z (zeta)', 'Location', 'northwest');
else
    legend('Z_\gamma', 'Z_{RvM}', 'Z_{tauc}', 'Location', 'northwest');
end
grid on; xlabel('t'); ylabel('Z_\kappa(t)');
hold off
guardar_png(fig5, fullfile(outdir, 'fig5_Z_recta_critica.png'));

fprintf('\nFicheros en %s\nTiempo total %.1f s\n', outdir, toc(tGlobal));
end

%% =================================================================== funciones

function tau = reloj_rvm(k, N0, Lp)
% Newton sobre la rama creciente y convexa de N0 (t > 2 pi), desde la derecha.
x = k + 1;
t = 2*pi*x./log(x) + 20;
f = N0(t) - (k - 0.5);
while any(f <= 0)
    t(f <= 0) = 2*t(f <= 0);
    f = N0(t) - (k - 0.5);
end
for it = 1:200
    t = t - f./Lp(t);
    f = N0(t) - (k - 0.5);
    if max(abs(f)) < 1e-10, break; end
end
if max(abs(f)) >= 1e-8 || any(t <= 2*pi)
    error('reloj_rvm: Newton no convergio (max residuo %g).', max(abs(f)));
end
tau = t;
end

function PP = potencias_primo(nmax)
% potencias de primo n = p^m <= nmax ordenadas, con frecuencia log n, coeficientes y B(n)
p = primes(nmax);
cnt = 0;
for i = 1:numel(p)
    cnt = cnt + floor(log(nmax)/log(p(i)) + 1e-12);
end
n = zeros(cnt, 1); lp = n; m = n;
c = 0;
for i = 1:numel(p)
    q = p(i);
    mm = 1;
    while q <= nmax
        c = c + 1;
        n(c) = q; lp(c) = log(p(i)); m(c) = mm;
        q = q*p(i);
        mm = mm + 1;
    end
end
n = n(1:c); lp = lp(1:c); m = m(1:c);
[n, o] = sort(n);
lp = lp(o); m = m(o);
PP.n     = n;
PP.freq  = m.*lp;                          % log n
PP.coef  = 1./(pi*m.*sqrt(n));             % S_Y = -sum coef sin(t log n)
PP.dcoef = lp./(pi*sqrt(n));               % S_Y' = -sum dcoef cos(t log n)
PP.B     = cumsum(lp./sqrt(n));            % B(n) = sum Lambda(n')/sqrt(n')
PP.cnt   = cumsum(accumarray(n, 1, [nmax 1]));   % numero de potencias de primo <= v
end

function [S, dS] = fase(t, Y, PP)
% S_Y(t) y S_Y'(t) con corte Y por punto (potencias de primo n <= Y)
t = t(:);
Y = Y(:);
J = zeros(size(t));
v = floor(Y);
J(v >= 1) = PP.cnt(v(v >= 1));
S  = zeros(size(t));
dS = zeros(size(t));
paso = 512;
for a = 1:paso:numel(t)
    b = min(a + paso - 1, numel(t));
    nt = max(J(a:b));
    if nt == 0, continue; end
    A = t(a:b)*PP.freq(1:nt)';
    M = bsxfun(@le, 1:nt, J(a:b));
    S(a:b)  = -(sin(A).*M)*PP.coef(1:nt);
    dS(a:b) = -(cos(A).*M)*PP.dcoef(1:nt);
end
end

function [x, xA, Xmon, Ycur, acept, bracketOK] = tauc_casana(tau, k, PP, c, eta, nNiv, nNew, N0, Lp)
K = numel(tau);
% ---- etapa A: raiz monotona certificada
thr = (1 - eta)/2*log((tau - 1)/(2*pi));
nb  = find(PP.B > max(thr), 1, 'first');
if isempty(nb), nb = numel(PP.B); end
jm  = sum(bsxfun(@le, PP.B(1:nb)', thr), 2);
Xmon = ones(K, 1);
Abound = zeros(K, 1);
Bmon = zeros(K, 1);
cA = cumsum(PP.coef);
pos = jm >= 1;
Xmon(pos)   = PP.n(jm(pos));
Abound(pos) = cA(jm(pos));
Bmon(pos)   = PP.B(jm(pos));
base = N0(tau) - (k - 0.5);
h  = 1.1*(Abound + abs(base))./(Lp(tau - 1) - Bmon/pi) + 1e-9;
lo = tau - h;
hi = tau + h;
glo = N0(lo) - (k - 0.5) + fase(lo, Xmon, PP);
ghi = N0(hi) - (k - 0.5) + fase(hi, Xmon, PP);
bracketOK = mean(glo < 0 & ghi > 0);
for it = 1:55
    mid = 0.5*(lo + hi);
    gm = N0(mid) - (k - 0.5) + fase(mid, Xmon, PP);
    neg = gm < 0;
    lo(neg)  = mid(neg);
    hi(~neg) = mid(~neg);
end
xA = 0.5*(lo + hi);
% ---- etapa B: continuacion hasta Y_max = (tau/2pi)^c
Ymax = (tau/(2*pi)).^c;
x = xA;
Ycur = Xmon;
activo = true(K, 1);
acept = nan(1, nNiv);
for lev = 1:nNiv
    Ynew = max(floor(Xmon.*(Ymax./Xmon).^(lev/nNiv)), Ycur);
    a = find(activo & Ynew > Ycur);
    if isempty(a), continue; end
    ta = tau(a); ka = k(a); xa = x(a); Ya = Ynew(a); Yp = Ycur(a);
    Lt = Lp(ta);
    bueno = true(size(a));
    for it = 1:nNew
        [S, dS] = fase(xa, Ya, PP);
        res = N0(xa) - (ka - 0.5) + S;
        der = Lp(xa) + dS;
        malo = der <= 0.1*Lp(xa);
        bueno = bueno & ~malo;
        stp = res./der;
        stp(malo) = 0;
        stp = max(min(stp, 0.25./Lt), -0.25./Lt);
        xa = xa - stp;
    end
    S = fase(xa, Ya, PP);
    bueno = bueno & abs(N0(xa) - (ka - 0.5) + S) < 1e-9;
    for sf = [0 0.5 1]
        pt = x(a) + sf*(xa - x(a));
        [~, d1] = fase(pt, Ya, PP);
        [~, d0] = fase(pt, Yp, PP);
        bueno = bueno & (Lp(pt) + d1 > 0.1*Lp(pt)) & (Lp(pt) + d0 > 0.1*Lp(pt));
    end
    x(a(bueno)) = xa(bueno);
    Ycur(a(bueno)) = Ya(bueno);
    activo(a(~bueno)) = false;
    acept(lev) = mean(bueno);
end
if any(~isfinite(x)) || any(x <= 2*pi)
    error('tauc_casana: valores fuera de dominio.');
end
end

function q = cuantil(v, p)
v = sort(v(:));
if isempty(v), q = NaN; return; end
q = v(max(1, min(numel(v), round(p*numel(v)))));
end

function Z = Z_lista(t, kap, xi12)
% Z_kappa(t) = -xi(1/2) prod_k (1 - t^2/kappa_k^2) / |G(1/2 + i t)|, con correccion de cola
t = t(:);
kap = kap(:)';
kK = max(kap);
cola = (log(kK/(2*pi)) + 1)/(2*pi*kK);        % aproxima sum_{k>K} kappa_k^(-2)
logA = zeros(size(t));
nneg = zeros(size(t));
for a = 1:256:numel(t)
    b = min(a + 255, numel(t));
    R = 1 - (t(a:b).^2)*(1./kap.^2);
    logA(a:b) = sum(log(abs(R)), 2);
    nneg(a:b) = sum(R < 0, 2);
end
logA = logA - t.^2*cola;
logG = log(0.5*(0.25 + t.^2)) - 0.25*log(pi) + real(lgamma_c(0.25 + 0.5i*t));
Z = -xi12*((-1).^nneg).*exp(logA - logG);
end

function lg = lgamma_c(z)
% log Gamma(z) para Re z > 0: desplazamiento de 10 y serie de Stirling
z = z(:);
n = 10;
acc = zeros(size(z));
for j = 0:n-1
    acc = acc + log(z + j);
end
v = z + n;
lg = (v - 0.5).*log(v) - v + 0.5*log(2*pi) + 1./(12*v) - 1./(360*v.^3) ...
     + 1./(1260*v.^5) - 1./(1680*v.^7) - acc;
end

function tab = tabla_cola()
% cola(u) = int_u^inf dv / (v (e^{2v} - 1)) = int_{e^u}^inf dy / (y (y^2-1) log y)
v = linspace(0.6, 40, 400001)';
f = 1./(v.*expm1(2*v));
I = cumtrapz(v, f);
tab.v = v;
tab.c = I(end) - I;
end

function y = li_real(x)
% li(x) = Ei(log x) para x > 1
y = -real(expint(-log(x(:))));
end

function J = J_lista(y, kap, w, tab, chunk)
u = log(y(:));
J = li_real(y) - 2*suma_ceros(u, kap, w, chunk) - log(2) + interp1(tab.v, tab.c, u, 'pchip');
end

function out = suma_ceros(u, kap, w, chunk)
% sum_k w_k Re Ei((1/2 + i kappa_k) u),  Ei(W) = -E1(-W) (Im W > 0)
% |W| >= 60: serie asintotica de 8 terminos (error relativo < 1e-11); |W| < 60: expint.
rho = 0.5 + 1i*kap(:).';
wr = w(:);
fact = [1 1 2 6 24 120 720 5040];
out = zeros(numel(u), 1);
for a = 1:chunk:numel(u)
    b = min(a + chunk - 1, numel(u));
    W = u(a:b)*rho;
    z = 1./W;
    P = fact(8);
    for n = 7:-1:1
        P = fact(n) + z.*P;
    end
    E = exp(W).*z.*P;
    sm = abs(W) < 60;
    if any(sm(:))
        E(sm) = -expint(-W(sm));
    end
    out(a:b) = real(E)*wr;
end
end

function p = pi_lista(x, kap, w, tab, chunk)
% pi_kappa(x) = sum_{1<=m<=log2 x} mu(m)/m J*_kappa(x^(1/m))
x = x(:);
M = floor(log2(max(x)));
ys = [];
own = [];
cf = [];
for m = 1:M
    mu = mobius(m);
    if mu == 0, continue; end
    y = x.^(1/m);
    a = find(y >= 2);
    ys  = [ys; y(a)];                       %#ok<AGROW>
    own = [own; a];                         %#ok<AGROW>
    cf  = [cf; (mu/m)*ones(numel(a), 1)];   %#ok<AGROW>
end
p = zeros(numel(x), 1);
if ~isempty(ys)
    Jv = J_lista(ys, kap, w, tab, chunk);
    p = accumarray(own, cf.*Jv, [numel(x) 1]);
end
end

function Lv = niveles(xg, Pv, lev, kap, w, tab, chunk, nBisec)
% primer cruce de cada nivel lev(j) en la malla y biseccion: Lv(j) = inf{x : pi_kappa(x) >= lev(j)}
n  = numel(lev);
lo = nan(n, 1);
hi = nan(n, 1);
for j = 1:n
    i = find(Pv >= lev(j), 1, 'first');
    if ~isempty(i)
        if i == 1
            lo(j) = xg(1);
            hi(j) = xg(1);
        else
            lo(j) = xg(i-1);
            hi(j) = xg(i);
        end
    end
end
ok = find(~isnan(lo) & hi > lo);
for it = 1:nBisec
    if isempty(ok), break; end
    mid = 0.5*(lo(ok) + hi(ok));
    pm  = pi_lista(mid, kap, w, tab, chunk);
    sube = pm >= lev(ok);
    hi(ok(sube))  = mid(sube);
    lo(ok(~sube)) = mid(~sube);
end
Lv = hi;
end

function E = envolvente(x)
% E(x) = sum_{1 <= m <= log2 x, mu(m) ~= 0, x^(1/m) >= 2} x^(1/(2m)) / m
x = x(:);
E = zeros(size(x));
for m = 1:floor(log2(max(x)))
    if mobius(m) == 0, continue; end
    y = x.^(1/m);
    E = E + (y >= 2).*sqrt(y)/m;
end
end

function L = mangoldt(n)
% Lambda(n) = log p si n = p^m, 0 en otro caso
f = factor(n);
if n > 1 && all(f == f(1))
    L = log(f(1));
else
    L = 0;
end
end

function mu = mobius(n)
if n == 1
    mu = 1;
    return
end
f = factor(n);
if numel(unique(f)) < numel(f)
    mu = 0;
else
    mu = (-1)^numel(f);
end
end

function fid = abrir(f)
fid = fopen(f, 'w');
if fid < 0, error('No puedo escribir %s', f); end
end

function c = marca(b)
if b, c = '*'; else, c = '-'; end
end

function guardar_png(fig, f)
try
    exportgraphics(fig, f, 'Resolution', 200);
catch
    print(fig, f, '-dpng', '-r200');
end
end
