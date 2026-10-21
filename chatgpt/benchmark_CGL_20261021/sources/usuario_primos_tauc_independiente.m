function primos_tauc_independiente
% Script independiente: no necesita ningun .mat previo.
% Lee zeross.bin de la carpeta actual de MATLAB.
% 1) reloj tau0, paso de Newton tau1 y tauL (Newton iterado nTerms veces), con Y = (tau/2pi)^c
% 2) elige la lista tauc de menor RMS frente a gamma_k (solo para seleccionar)
% 3) pi_tauc(x) por la formula explicita de Riemann con los ceros tauc
% Salida: pantalla, primos_tauc_resultados.txt, primos_tauc_resultados.mat,
%         primos_tauc_vs_pi.png (la figura no se cierra).

clc
clear

% ---- parametros ----
Kuse   = 20000;     % numero de ceros (subir despues)
c      = 1;         % corte Y(tau) = (tau/(2 pi))^c
nTerms = 6;         % iteraciones de Newton para tauL
xgrid  = linspace(2, 1000, 200)';

% ---- 1) lectura de ceros ----
f1 = fullfile(pwd, 'zeross.bin');
if ~isfile(f1)
    error('No encuentro %s. Ejecuta MATLAB desde la carpeta donde esta zeross.bin.', f1);
end
fid = fopen(f1, 'r');
if fid < 0
    error('fopen fallo sobre %s', f1);
end
gam = fread(fid, Kuse, 'float64', 'l');
fclose(fid);
if numel(gam) < Kuse
    error('zeross.bin tiene %d ceros; se piden %d.', numel(gam), Kuse);
end
gam = gam(:);

% ---- 2) reloj tau0 (inversa de la N(t) asintotica) ----
N_asym = @(t) (t./(2*pi)).*(log(t./(2*pi)) - 1) + 7/8;
tau0 = zeros(Kuse, 1);
for k = 1:Kuse
    g = max(14, 2*pi*k/log(k+2));
    tau0(k) = fzero(@(t) N_asym(t) - (k - 0.5), g);
end
pr = primes(ceil(max((tau0/(2*pi)).^c)) + 10);

% ---- 3) Newton y Newton iterado ----
tau1 = newton_step(tau0, N_asym, pr, c);
tauL = tau0;
for it = 1:nTerms
    tauL = newton_step(tauL, N_asym, pr, c);
end

% ---- 4) mejor lista tauc (diagnostico frente a gamma) ----
e0 = tau0 - gam;  e1 = tau1 - gam;  eL = tauL - gam;
rms = [sqrt(mean(e0.^2)), sqrt(mean(e1.^2)), sqrt(mean(eL.^2))];
listas = {tau0, tau1, tauL};
nombres = {'tau0', 'tau1', 'tauL'};
[~, ib] = min(rms);
tauc = sort(listas{ib});
tauc = tauc(tauc > 0);
fprintf('RMS frente a gamma: reloj=%.6g  Newton=%.6g  Newton_iterado=%.6g\n', rms);
fprintf('Lista usada: %s   (K = %d ceros)\n', nombres{ib}, numel(tauc));

% ---- 5) pi_tauc por la formula explicita ----
p   = primes(1000);
pix = zeros(size(xgrid));
pc  = zeros(size(xgrid));
for i = 1:numel(xgrid)
    x = xgrid(i);
    pix(i) = nnz(p <= x);
    pc(i)  = pi_tauc(x, tauc);
end

err = pc - pix;
fprintf('pi_tauc - pi en [2,1000]: RMS = %.6g   max|.| = %.6g\n', ...
    sqrt(mean(err.^2)), max(abs(err)));

fprintf('%10s %8s %14s %14s\n', 'x', 'pi(x)', 'pi_tauc(x)', 'error');
for j = 1:20:numel(xgrid)
    fprintf('%10.3f %8d %14.6f %14.6f\n', xgrid(j), pix(j), pc(j), err(j));
end

% ---- 6) figura (no se cierra) ----
fig = figure('Color', 'w');
subplot(2,1,1)
stairs(xgrid, pix, 'k-', 'LineWidth', 1); hold on
plot(xgrid, pc, 'r--', 'LineWidth', 1);
xlabel('x'); ylabel('conteo');
legend('\pi(x)', '\pi_{\tau^c}(x)', 'Location', 'northwest'); grid on
subplot(2,1,2)
plot(xgrid, err, 'b-', 'LineWidth', 1);
xlabel('x'); ylabel('\pi_{\tau^c}(x) - \pi(x)'); grid on
exportgraphics(fig, 'primos_tauc_vs_pi.png', 'Resolution', 200);

% ---- 7) salida txt y mat ----
fid = fopen('primos_tauc_resultados.txt', 'w');
if fid < 0
    error('No puedo escribir primos_tauc_resultados.txt');
end
fprintf(fid, 'x pi_x pi_tauc err\n');
fprintf(fid, '%.10g %d %.12g %.12g\n', [xgrid pix pc err]');
fclose(fid);
save('primos_tauc_resultados.mat', 'xgrid', 'pix', 'pc', 'err', 'tauc', ...
     'tau0', 'tau1', 'tauL', 'gam', 'rms', 'Kuse', 'c', 'nTerms');

end

% =====================================================================

function tn = newton_step(t, N_asym, pr, c)
% Un paso de Newton para N(t) + S_Y(t) = k - 1/2, con Y = (t/2pi)^c.
tn = zeros(size(t));
for k = 1:numel(t)
    tk = t(k);
    Y  = (tk/(2*pi))^c;
    p  = pr(pr <= Y);
    f  = N_asym(tk) + phase_S(tk, p) - (k - 0.5);
    df = (1/(2*pi))*log(tk/(2*pi)) + dphase_S(tk, p);
    tn(k) = tk - f/df;
end
end

function S = phase_S(t, p)
% S(t) ~ -(1/pi) sum_p atan2(a sin th, 1 - a cos th), a = p^(-1/2), th = t log p
a  = p.^(-0.5);
th = t .* log(p);
S  = -(1/pi) * sum(atan2(a.*sin(th), 1 - a.*cos(th)));
end

function dS = dphase_S(t, p)
% Derivada analitica de phase_S respecto a t
a  = p.^(-0.5);
lp = log(p);
th = t .* lp;
u  = a.*sin(th);     up = a.*cos(th).*lp;
v  = 1 - a.*cos(th); vp = a.*sin(th).*lp;
dS = -(1/pi) * sum((v.*up - u.*vp) ./ (u.^2 + v.^2));
end

function J = J_tauc(y, tauc)
% J(y) = li(y) - sum_rho li(y^rho) - log 2 + int_y^inf dt/(t(t^2-1)log t)
% Los zeros rho = 1/2 + i tau y conj(rho) aportan 2 Re li(y^rho).
% Re li(z) = Re(-E1(-z)) con la rama principal de expint.
ly   = log(y);
w    = (0.5 + 1i*tauc) * ly;
li_y = real(-expint(-ly));
sumz = 2 * sum(real(-expint(-w)));
tail = integral(@(t) 1./(t.*(t.^2 - 1).*log(t)), y, Inf);
J    = li_y - sumz - log(2) + tail;
end

function pc = pi_tauc(x, tauc)
% pi_tauc(x) = sum_{m=1}^{floor(log2 x)} mu(m)/m * J_tauc(x^(1/m))
M  = floor(log2(x));
pc = 0;
for m = 1:M
    mu = mu_mob(m);
    if mu ~= 0
        pc = pc + mu/m * J_tauc(x^(1/m), tauc);
    end
end
end

function mu = mu_mob(n)
% Funcion de Mobius
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