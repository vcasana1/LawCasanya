%% RVM_CYLINDER  -  exp(i*gamma) vs exp(i*tau_RVM) sobre el cilindro unidad
%
%  Eje 3 = k (indice del cero).  Ambas nubes viven sobre el cilindro de
%  radio 1, asi que "estar dentro" solo puede significar proximidad angular.
%
%  Objetivo del script: comprobar SI los puntos que se ven superpuestos en el
%  plano complejo tienen de verdad |eps_k| pequeno, o si hay aliasing
%  (eps_k ~ +-2pi da la misma superposicion visual).
%
%  Convenios del manuscrito (zeta_rvm_exponential_centroids v14):
%     eps_k = gamma_k - tau_k                                        (1.7)
%     b_k   = e^{i gamma_k} - e^{i tau_k} = 2i e^{i(g+t)/2} sin(eps/2)  (1.9)
%     |b_k| = 2|sin(eps_k/2)|  -> el modulo solo ve la discrepancia ENVUELTA
%     gamma_k - tau_k = -S_*(gamma_k)/H'(tau_k) + ...                 (C.8)
%  Este script no anade teoria: mide sobre los datos lo que (1.9) y (C.8)
%  ya dicen, y comprueba si el rango cae dentro del regimen sin aliasing.
%
%  NOTA NUMERICA IMPORTANTE
%  El cordal d_k se calcula desde eps_k, NO envolviendo cada fase por separado.
%  Con gamma ~ 1e6 rad, reducir mod 2pi en doble pierde ~1e-10 rad por termino;
%  la diferencia eps = gamma - tau es en cambio exacta a ~1e-10 absoluto sobre
%  magnitudes de orden 1. Restar primero y envolver despues elimina la
%  cancelacion catastrofica.
%
%  V. Casana / 2026-08-19

clear; close all; clc;

%% ------------------------------------------------------------------ config
DATADIR = '';            % <-- pon aqui la carpeta con zeross.bin y zLamb.bin
                         %     si se deja vacia, se busca bajo $HOME
NREAD   = Inf;           % cuantos ceros leer (Inf = todos)
STRIDE  = 400;           % submuestreo SOLO para dibujar (2e6 puntos no se ven)
KWIN    = [1 3000];      % ventana de k para la vista de detalle
TOLDEG  = 2;             % umbral de "superpuesto" en grados de angulo

%% -------------------------------------------------------------------- load
if isempty(DATADIR)
    h = getenv('HOME');
    c = dir(fullfile(h,'**','zeross.bin'));
    assert(~isempty(c),'No encuentro zeross.bin. Rellena DATADIR a mano.');
    DATADIR = c(1).folder;
end
fprintf('Datos en: %s\n', DATADIR);

gamma = readbin(fullfile(DATADIR,'zeross.bin'), NREAD);   % ordenadas verdaderas
tau   = readbin(fullfile(DATADIR,'zLamb.bin'),  NREAD);   % ordenadas RVM
N     = min(numel(gamma), numel(tau));
gamma = gamma(1:N);  tau = tau(1:N);
k     = (1:N).';
fprintf('N = %d   gamma_N = %.9f\n', N, gamma(end));

%% ------------------------------------------- desplazamiento y cordal exacto
eps_k = gamma - tau;                 % SIN envolver: esto es lo fisico
d_k   = 2*abs(sin(eps_k/2));         % |b_k| exacto, ec. (1.9)
ang_k = 2*asin(min(d_k/2,1));        % separacion angular en [0,pi]

%% ------------------------------------------------ 1) ¿hay aliasing o no?
fprintf('\n=== DESENROLLADO ===\n');
fprintf('max|eps_k|      = %.6f   (pi = %.6f)\n', max(abs(eps_k)), pi);
n_alias = sum(abs(eps_k) >= pi);
fprintf('ceros con |eps| >= pi : %d  (%.4f %%)\n', n_alias, 100*n_alias/N);
if n_alias == 0
    fprintf(['-> No hay aliasing. Superposicion en el plano <=> |eps| pequeno.\n' ...
             '   La lectura visual es legitima en TODO el rango.\n']);
else
    fprintf(['-> OJO: hay %d ceros que pueden solaparse en el dibujo con\n' ...
             '   |eps| grande. La lectura visual NO es fiable ahi.\n'], n_alias);
end

%% ------------------------- 2) seleccion COMO LO HACE EL OJO (angulo envuelto)
% Se selecciona por proximidad en el plano, sin mirar eps. Luego se examina eps.
tol   = TOLDEG*pi/180;
inside = ang_k < tol;                       % "cae dentro de la nube RVM"
ni    = sum(inside);
fprintf('\n=== SELECCION POR PROXIMIDAD EN EL PLANO (%.1f grados) ===\n',TOLDEG);
fprintf('seleccionados: %d de %d  (%.3f %%)\n', ni, N, 100*ni/N);
if ni>0
    fprintf('|eps| en los seleccionados : max %.6f   mediana %.6e\n', ...
            max(abs(eps_k(inside))), median(abs(eps_k(inside))));
    fprintf('|eps| en el resto          : mediana %.6f\n', ...
            median(abs(eps_k(~inside))));
    n_far = sum(abs(eps_k(inside)) > pi/2);
    fprintf('de los seleccionados, con |eps| > pi/2 (aliasing real): %d\n', n_far);
end

%% --------------------------- 3) ¿se agrupan en k o estan por todas partes?
if ni>0
    ks = k(inside);
    fprintf('\nrango de k seleccionados: %d .. %d\n', min(ks), max(ks));
    q = quantile(ks,[0 .25 .5 .75 1]);
    fprintf('cuartiles de k: %s\n', mat2str(round(q)));
    fprintf(['(si fuese un subconjunto especial se agruparian; si es puro\n' ...
             ' cruce por cero de S, deben estar repartidos y densificarse con k)\n']);
end

%% ------------------- 4) prediccion: |eps| ~ 2pi sqrt(loglog g)/log(g/2pi)
L      = log(gamma/(2*pi));                 % = 2*pi/espaciado medio
pred   = 2*pi*sqrt(max(log(log(max(gamma,16))),0)/(2*pi^2))./L;  % Selberg
spac   = 2*pi./L;                           % espaciado medio local
fprintf('\n=== ESCALA ===\n');
fprintf('mediana |eps|/espaciado_medio = %.4f\n', median(abs(eps_k)./spac));
fprintf('mediana |eps| medida  = %.4f\n', median(abs(eps_k)));
fprintf('mediana |eps| predicha= %.4f   (Selberg, var S = loglog t / 2pi^2)\n', ...
        median(pred));

%% ------------------- 5) ¿los que caen en RVM tienen espaciado menor?
delta   = diff(gamma);                      % espaciados consecutivos
nrm     = delta ./ spac(1:end-1);           % normalizado a la media local
sel     = inside(1:end-1);
if any(sel)
    fprintf('\n=== ESPACIADO LOCAL ===\n');
    fprintf('delta/media en los seleccionados : %.4f\n', mean(nrm(sel)));
    fprintf('delta/media en el resto          : %.4f\n', mean(nrm(~sel)));
    fprintf('(prediccion: ~1 en ambos; caer en RVM es regularidad, no compresion)\n');
end

%% --------------------------------------------------------------- graficas
s = 1:STRIDE:N;
zg = exp(1i*gamma(s));  zt = exp(1i*tau(s));

figure('Color','w','Position',[60 60 1250 820]);

subplot(2,2,[1 3]);
plot3(real(zt),imag(zt),k(s),'.','MarkerSize',3,'Color',[.85 .35 .10]); hold on;
plot3(real(zg),imag(zg),k(s),'.','MarkerSize',3,'Color',[.00 .45 .74]);
if ni>0
    zi = exp(1i*gamma(inside));
    plot3(real(zi),imag(zi),k(inside),'k.','MarkerSize',7);
end
grid on; axis vis3d; xlabel('Re'); ylabel('Im'); zlabel('k');
legend({'RVM  e^{i\tau_k}','\zeta  e^{i\gamma_k}','coincidentes'}, ...
       'Location','northeast');
title(sprintf('Cilindro unidad, eje k  (1 de cada %d puntos)',STRIDE));
view(-37.5,20);

subplot(2,2,2);
plot(k(s),eps_k(s),'.','MarkerSize',3,'Color',[.3 .3 .3]); hold on;
plot(k(s), pred(s),'r-','LineWidth',1.2);
plot(k(s),-pred(s),'r-','LineWidth',1.2);
yline( pi,'b--','+\pi'); yline(-pi,'b--','-\pi');
grid on; xlabel('k'); ylabel('\epsilon_k = \gamma_k - \tau_k');
title('Desplazamiento y envolvente \pm2\pi\surd(loglog\gamma)/log(\gamma/2\pi)');

subplot(2,2,4);
w = KWIN(1):min(KWIN(2),N);
plot(w, eps_k(w),'-','LineWidth',.8,'Color',[.0 .45 .74]); hold on;
if ni>0
    wi = w(inside(w));
    plot(wi, eps_k(wi),'k.','MarkerSize',10);
end
yline(0,'k-'); grid on; xlabel('k'); ylabel('\epsilon_k');
title(sprintf('Detalle k = %d..%d : los coincidentes son cruces por cero de \\epsilon', ...
      w(1), w(end)));

%% ------------------------------------------------------------------ helper
function v = readbin(f, n)
    fid = fopen(f,'r','ieee-le');
    assert(fid>0, ['No puedo abrir ' f]);
    if isinf(n), v = fread(fid,Inf,'float64=>double');
    else,        v = fread(fid,n,  'float64=>double'); end
    fclose(fid);
end
