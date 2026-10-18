function zCasanya_newton3_graficos()
% zCasanya_newton3_graficos  Mejor estimacion de ceros desde el reloj RvM
%   (tres pasos de Newton aritmeticos, fase power_sharp, cortes diadicos
%   [8, 8, 512]; reproduce zCasanya.bin) y TODAS las graficas:
%     Fig 1  paseos acumulados 3D  (Zeta, RVM, Casanya) con centroides
%     Fig 2  proyeccion en el plano complejo con centroides
%     Fig 3  segmentos exactos consecutivos (k = 1e6 .. 1e6+3000)
%     Fig 4  error gamma_k - x_k por indice (RVM vs Casanya)
%     Fig 5  RMS por bloques diadicos de altura (RVM vs Casanya)
%     Fig 6  histograma del error en unidades de ceros, L(tau)*e
%     Fig 7  |centroide parcial - centroide zeta| frente a k (deriva a frecuencia 1)
%   Todas se guardan en PNG y ninguna se cierra.
%   La construccion NO usa zeross.bin; solo las graficas y metricas lo leen.

clc; clear;

%% DIRECTORIO DE DATOS
dataDir = fullfile(getenv('HOME'), 'MATLAB');
if ~isfile(fullfile(dataDir, 'zLamb.bin')), dataDir = pwd; end
assert(isfile(fullfile(dataDir, 'zLamb.bin')), 'No encuentro zLamb.bin');

tau = readBinary(fullfile(dataDir, 'zLamb.bin'));
N   = numel(tau);
k   = (1:N)';
fprintf('zLamb.bin: %d ordenadas, tau(1)=%.6f, tau(N)=%.3f\n', N, tau(1), tau(end));
assert(all(isfinite(tau)) && all(diff(tau) > 0), 'zLamb.bin no es creciente/finito');

%% CONSTRUCCION (configuracion c667)
cutoffs = [8, 8, 512];
P = primes(max(cutoffs));
base = clock(tau) - (k - 0.5);
fprintf('max |N0(tau)-(k-1/2)| = %.3e\n', max(abs(base)));

x = tau;
for j = 1:numel(cutoffs)
    Xeff = effectiveCutoffs(tau, cutoffs(j));
    S = zeros(N, 1);
    for X = unique(Xeff)'
        at = (Xeff == X);
        S(at) = phasePowerSharp(x(at), P, X);
    end
    step = (base + clockDifference(x, tau) + S) ./ slope(x);
    x = x - step;
    fprintf('paso %d  X=[%s]  max|paso|=%.4f  max|paso|/espaciado=%.3f  cruces=%d\n', ...
        j, strjoin(string(unique(Xeff)'), ' '), max(abs(step)), ...
        max(abs(step .* slope(tau))), sum(diff(x) <= 0));
end
cas = x;
assert(all(isfinite(cas)) && all(cas > 2*pi));

outFile = fullfile(dataDir, 'zCasanya_matlab.bin');
fid = fopen(outFile, 'wb', 'ieee-le'); fwrite(fid, cas, 'double'); fclose(fid);
fprintf('Guardado %s (%d registros)\n', outFile, N);

%% CEROS VERDADEROS (solo evaluacion)
gfile = fullfile(dataDir, 'zeross.bin');
haveZeros = isfile(gfile);
if haveZeros
    gamma = readBinary(gfile);
    assert(numel(gamma) == N);
    eRvM = gamma - tau;
    eCas = gamma - cas;
    fprintf('\n%-20s RMS=%.10f  max=%.6f\n', 'Lambert/RvM', rms(eRvM), max(abs(eRvM)));
    fprintf('%-20s RMS=%.10f  max=%.6f  indices mejorados=%.3f%%\n', ...
        'Casanya 3 pasos', rms(eCas), max(abs(eCas)), 100*mean(abs(eCas) < abs(eRvM)));
    fprintf('Reduccion RMS: %.6f%%\n', 100*(1 - rms(eCas)/rms(eRvM)));
else
    warning('zeross.bin no encontrado: solo paseos RVM y Casanya.');
end

%% PASEOS ACUMULADOS Y CENTROIDES
names  = {'Zeta', 'RVM', 'Casanya'};
colors = [0.05 0.35 0.95; 0.90 0.15 0.10; 0.05 0.65 0.20];
if haveZeros, seqs = {gamma, tau, cas}; else, seqs = {[], tau, cas}; end
S = cell(1, 3); centers = nan(1, 3);
for j = 1:3
    if isempty(seqs{j}), continue; end
    S{j} = cumsum(cos(seqs{j})) + 1i*cumsum(sin(seqs{j}));
    centers(j) = mean(S{j});
end
fprintf('\nCENTROIDES DEL PASEO COMPLETO\n');
for j = 1:3
    if ~isnan(centers(j))
        fprintf('%-8s %+.15f %+.15fi\n', names{j}, real(centers(j)), imag(centers(j)));
    end
end
if haveZeros
    fprintf('Zeta-RVM     %.15f\nZeta-Casanya %.15f\nRVM-Casanya  %.15f\n', ...
        abs(centers(1)-centers(2)), abs(centers(1)-centers(3)), abs(centers(2)-centers(3)));
end

plotStep = 20;
idx = unique([1:plotStep:N, N])';
z   = double(idx);

%% FIGURA 1 - PASEOS 3D
fig1 = figure('Color', 'w', 'Name', 'Paseos acumulados 3D', 'Position', [100 100 1400 900]);
ax1 = axes('Parent', fig1); hold(ax1, 'on');
for j = 1:3
    if isempty(S{j}), continue; end
    plot3(ax1, real(S{j}(idx)), imag(S{j}(idx)), z, '.', 'Color', colors(j,:), ...
        'MarkerSize', 5, 'DisplayName', names{j});
    scatter3(ax1, real(centers(j)), imag(centers(j)), (N+1)/2, 180, colors(j,:), ...
        'filled', 'MarkerEdgeColor', 'k', 'HandleVisibility', 'off');
end
xlabel(ax1, 'Re suma acumulada'); ylabel(ax1, 'Im suma acumulada'); zlabel(ax1, 'Indice k');
title(ax1, sprintf('Zeta, RVM y Casanya [8 8 512] - N = %d', N));
grid(ax1, 'on'); box(ax1, 'on'); axis(ax1, 'tight'); pbaspect(ax1, [1 1 2]);
view(ax1, 40, 25); legend(ax1, 'Location', 'northeastoutside'); rotate3d(fig1, 'on');
saveas(fig1, fullfile(dataDir, 'zCasanya_fig1_paseos3D.png'));

%% FIGURA 2 - PLANO COMPLEJO
fig2 = figure('Color', 'w', 'Name', 'Paseos - plano complejo', 'Position', [150 100 1000 850]);
ax2 = axes('Parent', fig2); hold(ax2, 'on');
for j = 1:3
    if isempty(S{j}), continue; end
    plot(ax2, real(S{j}(idx)), imag(S{j}(idx)), '.', 'Color', colors(j,:), ...
        'MarkerSize', 4, 'DisplayName', names{j});
    scatter(ax2, real(centers(j)), imag(centers(j)), 180, colors(j,:), ...
        'filled', 'MarkerEdgeColor', 'k', 'HandleVisibility', 'off');
end
xlabel(ax2, 'Re suma acumulada'); ylabel(ax2, 'Im suma acumulada');
title(ax2, 'Centroides del paseo completo');
axis(ax2, 'equal'); grid(ax2, 'on'); box(ax2, 'on'); legend(ax2, 'Location', 'best');
saveas(fig2, fullfile(dataDir, 'zCasanya_fig2_plano.png'));

%% FIGURA 3 - SEGMENTOS EXACTOS
detailStart = min(1000000, N); detailEnd = min(N, detailStart + 2999);
ids = (detailStart:detailEnd)';
fig3 = figure('Color', 'w', 'Name', 'Segmentos exactos', 'Position', [200 120 1400 900]);
ax3 = axes('Parent', fig3); hold(ax3, 'on');
for j = 1:3
    if isempty(S{j}), continue; end
    plot3(ax3, real(S{j}(ids)), imag(S{j}(ids)), double(ids), '.-', 'Color', colors(j,:), ...
        'LineWidth', 0.7, 'MarkerSize', 5, 'DisplayName', names{j});
end
xlabel(ax3, 'Re suma acumulada'); ylabel(ax3, 'Im suma acumulada'); zlabel(ax3, 'Indice k');
title(ax3, sprintf('Segmentos exactos: k = %d a %d', detailStart, detailEnd));
grid(ax3, 'on'); box(ax3, 'on'); axis(ax3, 'tight'); view(ax3, 40, 25);
legend(ax3, 'Location', 'northeastoutside'); zoom(fig3, 'on');
saveas(fig3, fullfile(dataDir, 'zCasanya_fig3_segmentos.png'));

if ~haveZeros, return; end

%% FIGURA 4 - ERROR POR INDICE
idx4 = unique([1:50:N, N]);
fig4 = figure('Color', 'w', 'Name', 'Error por indice', 'Position', [100 100 1400 700]);
ax4 = axes('Parent', fig4); hold(ax4, 'on');
plot(ax4, idx4, eRvM(idx4), '.', 'Color', colors(2,:), 'MarkerSize', 3, 'DisplayName', 'RVM');
plot(ax4, idx4, eCas(idx4), '.', 'Color', colors(3,:), 'MarkerSize', 3, 'DisplayName', 'Casanya [8 8 512]');
xlabel(ax4, 'Indice k'); ylabel(ax4, '\gamma_k - x_k');
title(ax4, sprintf('Error del reloj y del tercer paso de Newton, N = %d', N));
grid(ax4, 'on'); box(ax4, 'on'); legend(ax4, 'Location', 'best');
saveas(fig4, fullfile(dataDir, 'zCasanya_fig4_error.png'));

%% FIGURA 5 - RMS POR BLOQUES DIADICOS
lo = 2.^(3:20)'; rmsR = nan(size(lo)); rmsC = nan(size(lo)); cnt = zeros(size(lo));
fprintf('\n%10s %10s %8s %12s %12s\n', 'T_lower', 'T_upper', 'n', 'RMS RVM', 'RMS Cas');
for b = 1:numel(lo)
    sel = tau > lo(b) & tau <= 2*lo(b);
    if any(sel)
        cnt(b) = nnz(sel); rmsR(b) = rms(eRvM(sel)); rmsC(b) = rms(eCas(sel));
        fprintf('%10d %10d %8d %12.6f %12.6f\n', lo(b), 2*lo(b), cnt(b), rmsR(b), rmsC(b));
    end
end
ok = cnt > 0;
fig5 = figure('Color', 'w', 'Name', 'RMS por bloques', 'Position', [120 120 1000 650]);
ax5 = axes('Parent', fig5); hold(ax5, 'on');
semilogx(ax5, lo(ok), rmsR(ok), 'o-', 'Color', colors(2,:), 'LineWidth', 1.5, 'DisplayName', 'RVM');
semilogx(ax5, lo(ok), rmsC(ok), 's-', 'Color', colors(3,:), 'LineWidth', 1.5, 'DisplayName', 'Casanya [8 8 512]');
set(ax5, 'XScale', 'log');
xlabel(ax5, 'Altura T (bloque (T, 2T])'); ylabel(ax5, 'RMS de \gamma_k - x_k');
title(ax5, 'RMS por bloque diadico'); grid(ax5, 'on'); box(ax5, 'on'); legend(ax5, 'Location', 'best');
saveas(fig5, fullfile(dataDir, 'zCasanya_fig5_rms_bloques.png'));

%% FIGURA 6 - HISTOGRAMA EN UNIDADES DE CEROS
sR = slope(tau) .* eRvM; sC = slope(tau) .* eCas;
fig6 = figure('Color', 'w', 'Name', 'Histograma L(tau) e', 'Position', [140 140 1000 650]);
ax6 = axes('Parent', fig6); hold(ax6, 'on');
edges = linspace(-1.5, 1.5, 301);
histogram(ax6, sR, edges, 'Normalization', 'pdf', 'FaceColor', colors(2,:), 'FaceAlpha', 0.45, 'EdgeColor', 'none', 'DisplayName', sprintf('RVM  <s^2>=%.4f', mean(sR.^2)));
histogram(ax6, sC, edges, 'Normalization', 'pdf', 'FaceColor', colors(3,:), 'FaceAlpha', 0.45, 'EdgeColor', 'none', 'DisplayName', sprintf('Casanya  <s^2>=%.4f', mean(sC.^2)));
xlabel(ax6, 'L(\tau_k)(\gamma_k - x_k)  [unidades de ceros]'); ylabel(ax6, 'densidad');
title(ax6, 'Error en unidades de ceros'); grid(ax6, 'on'); box(ax6, 'on'); legend(ax6, 'Location', 'best');
saveas(fig6, fullfile(dataDir, 'zCasanya_fig6_histograma.png'));

%% FIGURA 7 - DERIVA A FRECUENCIA 1 (coeficiente de Fourier del error)
% |sum_{j<=k} e_j e^{i gamma_j}| frente a k, y el equivalente aleatorio RMS*sqrt(k)
dR = abs(cumsum(eRvM .* exp(1i*gamma)));
dC = abs(cumsum(eCas .* exp(1i*gamma)));
fig7 = figure('Color', 'w', 'Name', 'Deriva a frecuencia 1', 'Position', [160 160 1200 650]);
ax7 = axes('Parent', fig7); hold(ax7, 'on');
plot(ax7, idx, dR(idx), '-', 'Color', colors(2,:), 'LineWidth', 1.2, 'DisplayName', '|\Sigma e_j e^{i\gamma_j}|  RVM');
plot(ax7, idx, dC(idx), '-', 'Color', colors(3,:), 'LineWidth', 1.2, 'DisplayName', '|\Sigma e_j e^{i\gamma_j}|  Casanya');
plot(ax7, idx, rms(eRvM)*sqrt(z), '--', 'Color', colors(2,:), 'DisplayName', 'fases aleatorias RVM');
plot(ax7, idx, rms(eCas)*sqrt(z), '--', 'Color', colors(3,:), 'DisplayName', 'fases aleatorias Casanya');
xlabel(ax7, 'Indice k'); ylabel(ax7, 'modulo de la suma');
title(ax7, 'Respuesta del error a la frecuencia 1 (la deriva del paseo verde)');
grid(ax7, 'on'); box(ax7, 'on'); legend(ax7, 'Location', 'northwest');
saveas(fig7, fullfile(dataDir, 'zCasanya_fig7_deriva.png'));
end

%% FUNCIONES AUXILIARES

function v = clock(t)
v = t/(2*pi) .* (log(t/(2*pi)) - 1) + 0.875;
end

function v = slope(t)
v = log(t/(2*pi)) / (2*pi);
end

function d = clockDifference(t, tau)
% N0(t)-N0(tau) sin cancelacion: L(tau)(t-tau) + tau/(2pi) h(u), u=(t-tau)/tau,
% h(u) = (1+u)log(1+u) - u = sum_{n>=2} (-1)^n u^n/(n(n-1)).
dd = t - tau; u = dd ./ tau; h = zeros(size(u));
small = abs(u) < 0.01; v = u(small);
poly = ones(size(v)) / (14*13);
for n = 13:-1:2, poly = (-1)^n/(n*(n-1)) + v .* poly; end
h(small) = v.^2 .* poly;
v = u(~small); h(~small) = (1 + v) .* log1p(v) - v;
d = slope(tau) .* dd + tau/(2*pi) .* h;
end

function X = effectiveCutoffs(tau, Xmax)
% X(T) = min(Xmax, max(8, floor(sqrt(2^floor(log2 T)))))
X = min(Xmax, max(8, floor(sqrt(pow2(floor(log2(tau)))))));
end

function S = phasePowerSharp(t, P, X)
% S_X(t) = -(1/pi) sum_{p^m <= X} sin(m t log p) / (m p^{m/2})
S = zeros(size(t));
for p = P(P <= X)
    q = p; m = 1;
    while q <= X
        S = S - sin(m*log(p)*t) / (pi*m*sqrt(q));
        q = q*p; m = m + 1;
    end
end
end

function values = readBinary(filename)
fid = fopen(filename, 'rb', 'ieee-le');
assert(fid >= 0, 'No puedo abrir %s', filename);
cleanup = onCleanup(@() fclose(fid));
values = fread(fid, inf, 'double=>double');
end