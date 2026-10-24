function resultado = leslie_mobius_punto_fijo_eta()
% LESLIE_MOBIUS_PUNTO_FIJO_ETA
% Diagnostico escalar de autoconsistencia para Leslies rigidas.
%
% Para cada b de una malla:
%   1) muestrea M(floor(b^n))/sqrt(floor(b^n));
%   2) estima K frecuencias omega(b) en la coordenada n;
%   3) forma S_Omega(w)=prod_k(w^2-2*cos(omega_k)w+1);
%   4) calcula eta_j=log(d_j/d_{j-1});
%   5) calcula b_*(Omega)=exp(2*||eta||_inf);
%   6) evalua g(b)=log(b_*/b).
%
% La condicion rigida Leslie no negativa es g(b)<=0. Los ceros de g
% son candidatos numericos de frontera, no raices algebraicas certificadas.
%
% Entrada:
%   moebius.bin, int8, un valor de mu por entero, en la carpeta actual.
%
% Salida:
%   resultado = leslie_mobius_punto_fijo_eta;
%   Guarda un MAT y una figura PNG.
%
% Requiere MATLAB base. No usa Optimization Toolbox.

close all;
clc;
rng(20260905,'twister');
t0 = tic;

%% Configuracion
cfg.archivoMu = 'moebius.bin';
cfg.bMin = 1.010;
cfg.bMax = 1.250;
cfg.nB = 241;
cfg.K = 7;
cfg.xMin = 100;
cfg.minPuntos = 80;
cfg.bloqueLectura = 2000000;
cfg.fracFrecuencias = 0.80; % Solo prefijo temporal para estimar omega
cfg.nFFTfactor = 32;
cfg.separacionOmega = 0.05;
cfg.refinaAncho = 0.03;
cfg.refinaVueltas = 4;
cfg.refinaPuntos = 61;
cfg.tolPositividadD = 1e-12;
cfg.tolAutoconsistencia = 1e-8;
cfg.prefijo = ['leslie_eta_fixed_' datestr(now,'yyyymmdd_HHMMSS')];

if ~isfile(cfg.archivoMu)
    error('No existe %s en la carpeta actual.',cfg.archivoMu);
end
D = dir(cfg.archivoMu);
Nmu = D.bytes;
fprintf('moebius.bin: %d valores\n',Nmu);
fprintf('K=%d, b en [%.6f, %.6f], %d nodos\n', ...
    cfg.K,cfg.bMin,cfg.bMax,cfg.nB);

bGrid = linspace(cfg.bMin,cfg.bMax,cfg.nB).';

%% Construir todas las rejillas y leer M una sola vez
rejillas = cell(cfg.nB,1);
unionX = zeros(0,1);
for ib = 1:cfg.nB
    rejillas{ib} = rejilla_para_b(bGrid(ib),Nmu,cfg.xMin);
    unionX = [unionX; rejillas{ib}.x]; %#ok<AGROW>
end
unionX = unique(unionX);
fprintf('Puntos distintos de M a leer: %d\n',numel(unionX));
Munion = leer_M_en_x(cfg.archivoMu,unionX,cfg.bloqueLectura);

%% Barrido escalar
R = repmat(registro_vacio(cfg.K),cfg.nB,1);
for ib = 1:cfg.nB
    b = bGrid(ib);
    G = rejillas{ib};
    [tf,loc] = ismember(G.x,unionX);
    if ~all(tf)
        error('Error interno al reconstruir la rejilla para b=%.16g.',b);
    end
    y = Munion(loc)./sqrt(double(G.x));

    Q = registro_vacio(cfg.K);
    Q.b = b;
    Q.nPuntos = numel(y);
    Q.n = G.n;
    Q.x = G.x;

    if numel(y) < cfg.minPuntos
        Q.estado = 'POCOS_PUNTOS';
        R(ib) = Q;
        continue
    end

    nFit = max(cfg.minPuntos,min(numel(y), ...
        floor(cfg.fracFrecuencias*numel(y))));
    idx = (1:nFit).';
    [omega,omegaInicial,wmin] = estimar_omega(y(idx),G.n(idx),cfg.K,cfg);

    Q.omega = omega;
    Q.omegaInicial = omegaInicial;
    Q.wmin = wmin;
    Q.Kefectivo = numel(omega);
    Q.gamma = omega/log(b);

    if numel(omega) ~= cfg.K
        Q.estado = 'K_INCOMPLETO';
        R(ib) = Q;
        continue
    end

    [d,eta,bStar,valido,motivo] = coordenadas_eta(omega,cfg);
    Q.d = d;
    Q.eta = eta;
    Q.bStar = bStar;
    Q.validoEta = valido;
    Q.estado = motivo;

    if valido
        Q.g = log(bStar/b);
        Q.ratio = bStar/b;
        Q.autoconsistente = Q.g <= cfg.tolAutoconsistencia;
        Q.strain = norm(eta,inf);
        Q.margenCaja = 0.5*log(b)-Q.strain;
    end
    R(ib) = Q;

    if mod(ib,20)==0 || ib==1 || ib==cfg.nB
        fprintf('%4d/%4d  b=%.6f  K=%d  b*=%.6g  g=%+.3e  %s\n', ...
            ib,cfg.nB,b,Q.Kefectivo,Q.bStar,Q.g,Q.estado);
    end
end

%% Extraer vectores y componentes autoconsistentes
valido = [R.validoEta].';
g = [R.g].';
bStar = [R.bStar].';
auto = [R.autoconsistente].' & valido;
intervalos = intervalos_booleanos(bGrid,auto);
cruces = cruces_lineales(bGrid,g,valido);

fprintf('\nResultado del barrido\n');
fprintf('Nodos eta-validos      : %d/%d\n',sum(valido),cfg.nB);
fprintf('Nodos autoconsistentes : %d/%d\n',sum(auto),cfg.nB);
fprintf('Cruces de g detectados : %d\n',numel(cruces));
if isempty(intervalos)
    fprintf('Conjunto autoconsistente de malla: VACIO\n');
else
    fprintf('Intervalos autoconsistentes de malla:\n');
    for j=1:size(intervalos,1)
        fprintf('  [%.9f, %.9f]\n',intervalos(j,1),intervalos(j,2));
    end
end
if ~isempty(cruces)
    fprintf('Candidatos de frontera por interpolacion lineal:\n');
    fprintf('  %.12f\n',cruces);
end

%% Figura
fig = figure('Color','w','Position',[100 100 980 720]);
tl = tiledlayout(2,1,'TileSpacing','compact','Padding','compact');

nexttile;
plot(bGrid,bGrid,'k--','LineWidth',1.2); hold on;
plot(bGrid(valido),bStar(valido),'b-','LineWidth',1.5);
if any(auto)
    plot(bGrid(auto),bStar(auto),'g.','MarkerSize',11);
end
xlabel('b'); ylabel('b_*(\Omega(b))');
title(sprintf('Autoconsistencia Leslie rigida en coordenadas eta, K=%d',cfg.K));
legend({'b_*=b','b_*(\Omega(b))','b_*\leq b'},'Location','best');
grid on;

nexttile;
plot(bGrid(valido),g(valido),'b-','LineWidth',1.5); hold on;
yline(0,'k--','LineWidth',1.2);
if ~isempty(cruces)
    plot(cruces,zeros(size(cruces)),'ro','MarkerFaceColor','r');
end
xlabel('b'); ylabel('g(b)=log(b_*(\Omega(b))/b)');
grid on;

title('g(b) <= 0 equivale a factibilidad rigida no negativa');
title(tl,sprintf('moebius.bin: N=%d; frecuencias estimadas solo en el prefijo %.2f', ...
    Nmu,cfg.fracFrecuencias));

png = [cfg.prefijo '_diagnostico.png'];
exportgraphics(fig,png,'Resolution',180);

%% Guardar
resultado = struct();
resultado.version = 'ETA-FIXED-POINT-1';
resultado.cfg = cfg;
resultado.N = Nmu;
resultado.bGrid = bGrid;
resultado.runs = R;
resultado.valido = valido;
resultado.g = g;
resultado.bStar = bStar;
resultado.autoconsistente = auto;
resultado.intervalosMalla = intervalos;
resultado.crucesLineales = cruces;
resultado.segundos = toc(t0);
resultado.figura = png;

mat = [cfg.prefijo '_resultado.mat'];
save(mat,'resultado','-v7.3');
fprintf('Tiempo: %.2f s\n',resultado.segundos);
fprintf('Guardado: %s\n',mat);
fprintf('Figura : %s\n',png);
assignin('base','resultado_eta_fixed',resultado);
end

function G = rejilla_para_b(b,Nmu,xMin)
% Rejilla genuina dependiente de b: x_n=floor(b^n).
nMin = ceil(log(double(xMin))/log(b));
nMax = floor(log(double(Nmu))/log(b));
n = (nMin:nMax).';
x = floor(b.^n);
x = max(xMin,min(Nmu,x));
[x,ia] = unique(x,'stable');
n = n(ia);
keep = x>=xMin & x<=Nmu;
G.n = n(keep);
G.x = x(keep);
end

function [d,eta,bStar,valido,motivo] = coordenadas_eta(omega,cfg)
% Coeficientes descendentes de prod(w^2-2*cos(omega_k)w+1).
d = 1;
for k=1:numel(omega)
    d = conv(d,[1 -2*cos(omega(k)) 1]);
end
d = real(d(:).');
K = numel(omega);

% Solo hacen falta d_0,...,d_K. La palindromia se revisa aparte.
palErr = norm(d-fliplr(d),inf);
if palErr > 1e-9
    eta = nan(1,K); bStar=NaN; valido=false;
    motivo='FALLO_PALINDROMIA'; return
end

dHalf = d(1:K+1);
if any(~isfinite(dHalf)) || any(dHalf <= cfg.tolPositividadD)
    eta = nan(1,K); bStar=Inf; valido=false;
    motivo='D_NO_POSITIVO'; return
end

eta = log(dHalf(2:end)./dHalf(1:end-1));
bStar = exp(2*norm(eta,inf));
valido = isfinite(bStar);
if valido
    motivo='OK';
else
    motivo='BSTAR_NO_FINITO';
end
end

function I = intervalos_booleanos(b,mask)
mask = mask(:); b=b(:);
z = diff([false;mask;false]);
i0 = find(z==1); i1=find(z==-1)-1;
I = [b(i0) b(i1)];
end

function c = cruces_lineales(b,g,valido)
c = zeros(0,1);
for j=1:numel(b)-1
    if ~(valido(j)&&valido(j+1)&&isfinite(g(j))&&isfinite(g(j+1)))
        continue
    end
    if g(j)==0
        c(end+1,1)=b(j); %#ok<AGROW>
    elseif g(j)*g(j+1)<0
        c(end+1,1)=b(j)-g(j)*(b(j+1)-b(j))/(g(j+1)-g(j)); %#ok<AGROW>
    end
end
if valido(end)&&g(end)==0
    c(end+1,1)=b(end);
end
c=unique(c);
end

function [omega,omega0,wmin] = estimar_omega(y,n,K,cfg)
y = y(:)-mean(y);
n = n(:);
NN = numel(y);
wmin = 4*pi/NN;
nf = 2^nextpow2(cfg.nFFTfactor*NN);

% FFT solo para inicializar. El refinamiento usa la coordenada n real.
% Para n consecutivo esto coincide con el espectro discreto usual.
P = abs(fft(y,nf)).^2;
w = 2*pi*(0:nf-1)'/nf;
h = 2:floor(nf/2)-1;
P=P(h); w=w(h);
pico=false(size(P));
pico(2:end-1)=P(2:end-1)>P(1:end-2) & ...
    P(2:end-1)>=P(3:end);
id=find(pico);
[~,ord]=sort(P(id),'descend'); id=id(ord);
omega0=[];
for j=1:numel(id)
    z=w(id(j));
    if z>=pi, continue, end
    if isempty(omega0)||min(abs(z-omega0))>cfg.separacionOmega
        omega0(end+1)=z; %#ok<AGROW>
    end
    if numel(omega0)>=K, break, end
end
omega=sort(omega0(omega0>wmin & omega0<pi-wmin));
omega=omega(:);

ancho=cfg.refinaAncho;
for vuelta=1:cfg.refinaVueltas
    for k=1:numel(omega)
        rej=linspace(max(wmin,omega(k)-ancho), ...
            min(pi-wmin,omega(k)+ancho),cfg.refinaPuntos);
        best=Inf; zbest=omega(k);
        for z=rej
            tt=omega; tt(k)=z; tt=sort(tt);
            if numel(tt)>1 && min(diff(tt))<cfg.separacionOmega/2
                continue
            end
            X=diseno(n,tt);
            coef=X\y;
            err=norm(y-X*coef);
            if err<best
                best=err; zbest=z;
            end
        end
        omega(k)=zbest; omega=sort(omega);
    end
    ancho=ancho/2;
end
omega0=omega0(:);
end

function X = diseno(n,t)
n=n(:); t=t(:).';
X=[ones(numel(n),1),cos(n*t),sin(n*t)];
end

function M = leer_M_en_x(nombre,x,B)
fid=fopen(nombre,'rb');
if fid<0, error('No se pudo abrir %s.',nombre); end
c=onCleanup(@()fclose(fid));
x=double(x(:)); M=zeros(size(x));
q=1; done=0; s=0;
while q<=numel(x)
    v=fread(fid,B,'*int8');
    if isempty(v), break, end
    cs=s+cumsum(double(v));
    fin=done+numel(v);
    while q<=numel(x)&&x(q)<=fin
        M(q)=cs(x(q)-done); q=q+1;
    end
    s=cs(end); done=fin;
end
if q<=numel(x), error('Fin prematuro de moebius.bin.'); end
end

function S = registro_vacio(K)
S=struct('b',NaN,'nPuntos',0,'n',[],'x',[], ...
    'omega',[],'omegaInicial',[],'gamma',[],'wmin',NaN, ...
    'Kefectivo',0,'d',nan(1,2*K+1),'eta',nan(1,K), ...
    'strain',NaN,'bStar',NaN,'ratio',NaN,'g',NaN, ...
    'margenCaja',NaN,'validoEta',false, ...
    'autoconsistente',false,'estado','SIN_EVALUAR');
end
