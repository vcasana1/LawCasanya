function resultado = leslie_mobius_punto_fijo(b0, Kf, fraccionEntreno, Ncriba)
% LESLIE_MOBIUS_PUNTO_FIJO
% Test autocontenido del punto fijo entre:
%   b -> frecuencias de M(b^n)/sqrt(b^n) -> intervalo positivo en r -> b_nuevo.
%
% CAMBIOS CLAVE
%   1) En la estimacion espectral excluye omega <= 4*pi/Nentreno.
%   2) No prueba positividad solo en b0. Calcula de una vez el intervalo
%      completo de r para el que
%          Q(w)=(w-r)*prod_j(w^2-2*cos(theta_j)*w+1)
%      tiene todos sus coeficientes no lideres <= 0.
%   3) Itera b_{q+1}=r_min(theta(b_q))^2, con amortiguacion opcional.
%   4) Tras la iteracion compara peine rigido y frecuencias libres fuera
%      de muestra, y valida la Leslie final si existe punto consistente.
%
% USO
%   resultado = leslie_mobius_punto_fijo
%   resultado = leslie_mobius_punto_fijo(1.15,6)
%   resultado = leslie_mobius_punto_fijo(1.15,6,0.65,2e7)
%
% FICHERO DE MU
%   Busca moebius.bin, mobius.bin o mu.bin, int8 con mu(1),mu(2),...
%   Si no existe, calcula la criba hasta Ncriba.
%
% NOTA
%   El mapa puede ser discontinuo porque las frecuencias dominantes pueden
%   cambiar de orden. Por eso se guarda toda la historia y se informa tanto
%   el residuo de punto fijo como la estabilidad del conjunto angular.

if nargin < 1 || isempty(b0),               b0 = 1.15; end
if nargin < 2 || isempty(Kf),               Kf = 6; end
if nargin < 3 || isempty(fraccionEntreno), fraccionEntreno = 0.65; end
if nargin < 4 || isempty(Ncriba),          Ncriba = 2e7; end

cfg.maxIterPF       = 30;
cfg.tolRelB         = 1e-6;
cfg.tolAngulo       = 2e-4;
cfg.amortiguacion   = 0.50;   % 1 = iteracion pura; menor reduce ciclos
cfg.bMin            = 1 + 1e-10;
cfg.bMax            = 1e3;
cfg.margenR         = 1e-10;
cfg.tolCoef         = 5e-11;
cfg.tolP            = 1e-13;
cfg.separacionFreq  = 0.05;
cfg.refinaAncho     = 0.03;
cfg.refinaPuntos    = 61;
cfg.refinaVueltas   = 4;
cfg.minTest         = 5;

%% 1. Cargar mu
mu = cargar_o_cribar_mu(Ncriba);
N = numel(mu);
M = cumsum(mu);
fprintf('mu(1..%d), mu(1..12) = %s\n',N,mat2str(mu(1:min(12,N))'));

esperado = [1 -1 -1 0 -1 1 -1 0 0 1 -1 0]';
if N >= 12 && ~isequal(mu(1:12),esperado)
    warning('Los primeros 12 valores no coinciden con Mobius.');
end

%% 2. Iteracion del punto fijo
hist = struct('iter',{},'b',{},'Np',{},'ntr',{},'omegaMin',{}, ...
    'theta',{},'rMin',{},'rMax',{},'bObjetivo',{},'bSiguiente',{}, ...
    'intervaloVacio',{},'residuoRel',{},'cambioAngular',{},'detalle',{});

b = b0;
thetaAnterior = [];
convergio = false;
razonParada = 'maximo de iteraciones';

fprintf('\n================ PUNTO FIJO ================\n');
for it = 1:cfg.maxIterPF
    [n,x,y,ntr,itr,ite] = observable_geometrico(M,N,b,Kf,fraccionEntreno,cfg.minTest);
    Np = numel(y);
    omegaMin = 4*pi/numel(itr);
    theta = estimar_frecuencias(y(itr),n(itr),Kf,cfg);

    if numel(theta) < Kf
        razonParada = sprintf('solo se estimaron %d de %d frecuencias',numel(theta),Kf);
        fprintf('Iter %d: %s.\n',it,razonParada);
        break
    end

    [rMin,rMax,admisible,p,detalle] = intervalo_r_positivo(theta,cfg.tolP);
    if ~admisible
        h = nueva_historia(it,b,Np,ntr,omegaMin,theta,NaN,NaN,NaN,NaN,true,NaN,NaN,detalle);
        hist(end+1) = h; %#ok<AGROW>
        razonParada = 'intervalo de positividad vacio';
        fprintf('Iter %2d | b=%12.7g | intervalo r VACIO | %s\n',it,b,detalle);
        break
    end

    rElegido = max([1+cfg.margenR,rMin+cfg.margenR]);
    if isfinite(rMax) && rElegido > rMax
        h = nueva_historia(it,b,Np,ntr,omegaMin,theta,rMin,rMax,NaN,NaN,true,NaN,NaN,'margen incompatible');
        hist(end+1) = h; %#ok<AGROW>
        razonParada = 'el intervalo no admite margen interior';
        break
    end

    bObjetivo = rElegido^2;
    if bObjetivo > cfg.bMax
        h = nueva_historia(it,b,Np,ntr,omegaMin,theta,rMin,rMax,bObjetivo,NaN,false,NaN,NaN,'b excede bMax');
        hist(end+1) = h; %#ok<AGROW>
        razonParada = sprintf('b objetivo %.6g excede bMax %.6g',bObjetivo,cfg.bMax);
        fprintf('Iter %2d | b=%12.7g | r=[%.7g,%s] | b_obj=%.7g > bMax\n', ...
            it,b,rMin,texto_infinito(rMax),bObjetivo);
        break
    end

    % Amortiguacion en log b: preserva b>1 y trata mejor escalas amplias.
    logbSig = (1-cfg.amortiguacion)*log(b) + cfg.amortiguacion*log(max(cfg.bMin,bObjetivo));
    bSiguiente = exp(logbSig);
    residuoRel = abs(bObjetivo-b)/max(1,b);
    cambioAngular = distancia_conjuntos(thetaAnterior,theta);

    h = nueva_historia(it,b,Np,ntr,omegaMin,theta,rMin,rMax,bObjetivo,bSiguiente,false,residuoRel,cambioAngular,detalle);
    hist(end+1) = h; %#ok<AGROW>

    fprintf(['Iter %2d | b=%12.7g | pts=%3d | wmin=%.4g | ' ...
             'r adm=[%.7g,%s] | b_obj=%12.7g | res=%.3e'], ...
             it,b,Np,omegaMin,rMin,texto_infinito(rMax),bObjetivo,residuoRel);
    if isfinite(cambioAngular)
        fprintf(' | dtheta=%.3e',cambioAngular);
    end
    fprintf('\n');

    if residuoRel <= cfg.tolRelB && ...
            (isempty(thetaAnterior) || cambioAngular <= cfg.tolAngulo)
        convergio = true;
        razonParada = 'punto fijo consistente';
        b = bObjetivo;
        break
    end

    thetaAnterior = theta;
    b = bSiguiente;
end

if isempty(hist)
    error('La iteracion no produjo ningun estado evaluable.');
end

%% 3. Recalcular el estado final de forma coherente
bFinal = b;
[n,x,y,ntr,itr,ite] = observable_geometrico(M,N,bFinal,Kf,fraccionEntreno,cfg.minTest);
thetaLibre = estimar_frecuencias(y(itr),n(itr),Kf,cfg);
[rMin,rMax,admisible,p,detalleIntervalo] = intervalo_r_positivo(thetaLibre,cfg.tolP);
rFinal = sqrt(bFinal);
positivaEnB = admisible && rFinal >= rMin-cfg.tolCoef && rFinal <= rMax+cfg.tolCoef;

%% 4. Comparar frecuencias libres y peine con la misma particion
m = 2*Kf+1;
thetaPeine = 2*pi*(1:Kf)/m;
AP = [cos(n*thetaPeine),sin(n*thetaPeine)];
AL = [cos(n*thetaLibre'),sin(n*thetaLibre')];
[rInP,rOutP,maxOutP,R2P,cP] = ajustar_y_predecir(AP,y,itr,ite);
[rInL,rOutL,maxOutL,R2L,cL] = ajustar_y_predecir(AL,y,itr,ite);
rmsCero = sqrt(mean(y(ite).^2));

fprintf('\n================ RESULTADO FINAL ================\n');
fprintf('Parada: %s\n',razonParada);
fprintf('b final = %.12g, r final = %.12g, puntos = %d\n',bFinal,rFinal,numel(y));
fprintf('Intervalo admisible final: r en [%.12g,%s]\n',rMin,texto_infinito(rMax));
fprintf('El mismo b pertenece al intervalo: %d\n',positivaEnB);
fprintf('Peine: RMS in %.6g | RMS out %.6g | max out %.6g | R2 out %+.6f\n',rInP,rOutP,maxOutP,R2P);
fprintf('Libre: RMS in %.6g | RMS out %.6g | max out %.6g | R2 out %+.6f\n',rInL,rOutL,maxOutL,R2L);
fprintf('Predictor cero fuera: RMS %.6g\n',rmsCero);
fprintf('Detalle intervalo: %s\n',detalleIntervalo);

%% 5. Construir y validar Leslie si el punto final es positivo
L = [];
a = [];
validacion = struct('construida',false,'minA',NaN,'errPerron',NaN, ...
    'errModulo',NaN,'residuoPolinomio',NaN,'rcondVectores',NaN);

if positivaEnB
    qc = coeficientes_Q_desde_p(p,rFinal); % coeficientes no lideres en w
    a = -qc .* rFinal.^(1:numel(qc));      % vuelta a z
    dim = numel(a);
    L = zeros(dim);
    L(1,:) = a;
    L(2:dim+1:end) = 1;

    ev = eig(L);
    [~,ip] = min(abs(ev-bFinal));
    lamP = ev(ip);
    ev(ip) = [];
    errPerron = abs(lamP-bFinal);
    errModulo = max(abs(abs(ev)-rFinal));

    raicesPred = [bFinal; rFinal*exp(1i*thetaLibre(:)); rFinal*exp(-1i*thetaLibre(:))];
    coefPolZ = poly(raicesPred.');
    escalaPol = max(1,sum(abs(coefPolZ)));
    residuoPol = max(abs(polyval(coefPolZ,raicesPred)))/escalaPol;

    validacion = struct('construida',true,'minA',min(a),'errPerron',errPerron, ...
        'errModulo',errModulo,'residuoPolinomio',residuoPol,'rcondVectores',NaN);
    fprintf('\nLeslie final: dim=%d | min(a)=%.3e | err Perron=%.3e | err modulo=%.3e | residuo P=%.3e\n', ...
        dim,min(a),errPerron,errModulo,residuoPol);
else
    fprintf('\nNo se construye Leslie: b final no es positivo para sus propios angulos.\n');
end

%% 6. Controles nulos, reestimando frecuencias en cada control
soporte = mu~=0;
controles = struct('nombre',{},'rmsOut',{},'R2Out',{},'rMin',{},'rMax',{},'admisible',{});
nombres = {'signos aleatorios en soporte','signos de mu permutados'};
fprintf('\n================ CONTROLES NULOS ================\n');
for ic = 1:2
    rng(3000+ic);
    s = zeros(N,1);
    idx = find(soporte);
    if ic == 1
        s(idx) = sign(randn(numel(idx),1));
    else
        s(idx) = mu(idx(randperm(numel(idx))));
    end
    Mc = cumsum(s);
    yc = Mc(x)./sqrt(x);
    thc = estimar_frecuencias(yc(itr),n(itr),Kf,cfg);
    Ac = [cos(n*thc'),sin(n*thc')];
    [~,ro,~,r2] = ajustar_y_predecir(Ac,yc,itr,ite);
    [rmi,rma,adm] = intervalo_r_positivo(thc,cfg.tolP);
    controles(end+1) = struct('nombre',nombres{ic},'rmsOut',ro,'R2Out',r2, ...
        'rMin',rmi,'rMax',rma,'admisible',adm); %#ok<AGROW>
    fprintf('%-30s | RMS out %.6g | R2 %+.6f | intervalo %d',nombres{ic},ro,r2,adm);
    if adm, fprintf(' [%.6g,%s]',rmi,texto_infinito(rma)); end
    fprintf('\n');
end

%% 7. Graficos
figure;
subplot(2,1,1); hold on; grid on
plot(n,y,'k.-','DisplayName','M(b^n)/sqrt(b^n)');
plot(n,AP*cP,'r-','LineWidth',1.1,'DisplayName',sprintf('peine R2=%+.3f',R2P));
plot(n,AL*cL,'b-','LineWidth',1.1,'DisplayName',sprintf('libre R2=%+.3f',R2L));
xline(n(ntr),'k--','LineWidth',1.4,'DisplayName','fin entreno');
xlabel('n'); ylabel('M/sqrt(x)'); legend show
title(sprintf('b final %.6g, K=%d',bFinal,Kf));
subplot(2,1,2); hold on; grid on
plot(n(ite),y(ite)-AP(ite,:)*cP,'r.-','DisplayName','residuo peine');
plot(n(ite),y(ite)-AL(ite,:)*cL,'b.-','DisplayName','residuo libre');
yline(0,'k-'); xlabel('n'); ylabel('error fuera'); legend show

figure;
subplot(2,1,1); hold on; grid on
itv = [hist.iter];
plot(itv,[hist.b],'o-','LineWidth',1.2,'DisplayName','b usado');
bo = [hist.bObjetivo];
plot(itv,bo,'s--','LineWidth',1.2,'DisplayName','r_{min}^2');
xlabel('iteracion'); ylabel('b'); legend show; title('iteracion del punto fijo');
subplot(2,1,2); hold on; grid on
semilogy(itv,max([hist.residuoRel],realmin),'o-','LineWidth',1.2);
xlabel('iteracion'); ylabel('residuo relativo');

figure; hold on; grid on
yc = y(itr)-mean(y(itr));
nf = 2^nextpow2(32*numel(itr));
Pow = abs(fft(yc,nf)).^2;
w = 2*pi*(0:nf-1)'/nf;
half = 1:floor(nf/2);
plot(w(half),Pow(half)/max(Pow(half)),'b-','LineWidth',1.1);
for k=1:Kf, xline(thetaPeine(k),'r--'); end
for k=1:numel(thetaLibre), xline(thetaLibre(k),'g-','LineWidth',1.3); end
xline(4*pi/numel(itr),'k:','LineWidth',1.5);
xlabel('frecuencia en n'); ylabel('potencia normalizada');
title('rojo: peine; verde: libres; negro: corte de baja frecuencia');

%% 8. Salida y archivos
resultado = struct;
resultado.convergio = convergio;
resultado.razonParada = razonParada;
resultado.bInicial = b0;
resultado.bFinal = bFinal;
resultado.rFinal = rFinal;
resultado.K = Kf;
resultado.historia = hist;
resultado.thetaLibre = thetaLibre;
resultado.thetaPeine = thetaPeine;
resultado.intervaloR = [rMin,rMax];
resultado.positivaEnB = positivaEnB;
resultado.peine = struct('rmsIn',rInP,'rmsOut',rOutP,'maxOut',maxOutP,'R2Out',R2P,'coef',cP);
resultado.libre = struct('rmsIn',rInL,'rmsOut',rOutL,'maxOut',maxOutL,'R2Out',R2L,'coef',cL);
resultado.rmsCero = rmsCero;
resultado.validacion = validacion;
resultado.controles = controles;
resultado.n = n;
resultado.x = x;
resultado.y = y;
resultado.L = L;
resultado.a = a;

save('leslie_mobius_punto_fijo_resultado.mat','resultado');
exportar_historia(hist,'leslie_mobius_punto_fijo_historia.csv');
assignin('base','resultado_punto_fijo',resultado);
if ~isempty(L), assignin('base','L_punto_fijo',L); end
fprintf('\nGuardados:\n  %s\n  %s\n','leslie_mobius_punto_fijo_resultado.mat','leslie_mobius_punto_fijo_historia.csv');
end

%% ========================================================================
function mu = cargar_o_cribar_mu(Ncriba)
mu = [];
for c = {'moebius.bin','mobius.bin','mu.bin'}
    if isfile(c{1})
        fprintf('Usando fichero %s\n',c{1});
        fid = fopen(c{1},'r');
        if fid < 0, error('No se pudo abrir %s.',c{1}); end
        limpieza = onCleanup(@() fclose(fid));
        mu = double(fread(fid,inf,'*int8'));
        clear limpieza
        break
    end
end
if isempty(mu)
    fprintf('Sin fichero de mu; cribando hasta %g...\n',Ncriba);
    mu = criba_mobius(round(Ncriba));
end
end

function [n,x,y,ntr,itr,ite] = observable_geometrico(M,N,b,Kf,fraccionEntreno,minTest)
if ~(isfinite(b) && b>1)
    error('b debe ser finito y mayor que 1.');
end
nmax = floor(log(N)/log(b));
n = (1:nmax)';
% Evita overflow y redondeos duplicados antes de elevar.
logx = n*log(b);
ok = logx <= log(N);
n = n(ok);
x = round(exp(logx(ok)));
ok = x>=100 & x<=N;
n = n(ok); x = x(ok);
[x,iu] = unique(x,'stable');
n = n(iu);
y = M(x)./sqrt(x);
Np = numel(y);
minEntreno = max(2*Kf+5,4*Kf+10);
ntr = min(max(minEntreno,round(fraccionEntreno*Np)),Np-minTest);
if Np < minEntreno+minTest || ntr < 2*Kf+1 || ntr >= Np
    error('b=%.6g deja solo %d puntos: insuficientes para K=%d.',b,Np,Kf);
end
itr = 1:ntr;
ite = ntr+1:Np;
end

function th = estimar_frecuencias(yv,nv,Kf,cfg)
yv = yv(:); nv = nv(:);
yd = yv-mean(yv);
Nn = numel(yd);
wmin = 4*pi/Nn;
nf = 2^nextpow2(32*Nn);
P = abs(fft(yd,nf)).^2;
w = 2*pi*(0:nf-1)'/nf;
h = 2:floor(nf/2)-1;
w = w(h); P = P(h);
ok = w>wmin & w<pi-wmin;
w = w(ok); P = P(ok);

pico = false(numel(P),1);
for k=2:numel(P)-1
    pico(k) = P(k)>P(k-1) && P(k)>=P(k+1);
end
id = find(pico);
[~,ord] = sort(P(id),'descend');
id = id(ord);
th = [];
for q=1:numel(id)
    wq = w(id(q));
    if isempty(th) || min(dist_circular_pi(wq,th))>cfg.separacionFreq
        th(end+1) = wq; %#ok<AGROW>
    end
    if numel(th)>=Kf, break; end
end
% Si faltan picos locales, completa con máximos separados del periodograma.
if numel(th)<Kf
    [~,ordTodo] = sort(P,'descend');
    for q=1:numel(ordTodo)
        wq = w(ordTodo(q));
        if isempty(th) || min(dist_circular_pi(wq,th))>cfg.separacionFreq
            th(end+1)=wq; %#ok<AGROW>
        end
        if numel(th)>=Kf, break; end
    end
end
th = sort(th(:));

for vuelta=1:cfg.refinaVueltas
    for k=1:numel(th)
        lo = max(wmin,th(k)-cfg.refinaAncho);
        hi = min(pi-wmin,th(k)+cfg.refinaAncho);
        rej = linspace(lo,hi,cfg.refinaPuntos);
        mejor = inf; wmej = th(k);
        for wq=rej
            tt=th; tt(k)=wq; tt=sort(tt);
            if numel(tt)>1 && min(diff(tt))<0.5*cfg.separacionFreq
                continue
            end
            A=[cos(nv*tt'),sin(nv*tt')];
            c=A\yv;
            res=norm(yv-A*c);
            if res<mejor
                mejor=res; wmej=wq;
            end
        end
        th(k)=wmej;
        th=sort(th);
    end
    cfg.refinaAncho = cfg.refinaAncho/2;
end
end

function d = dist_circular_pi(w,th)
% Frecuencias reales cos/sin se representan en (0,pi).
d = abs(w-th(:)');
end

function [rMin,rMax,admisible,p,detalle] = intervalo_r_positivo(th,tol)
% p(w)=prod(w^2-2cos(theta)w+1), coeficientes en orden descendente.
% Q=(w-r)p. Para cada coeficiente no lider q_j=p_{j+1}-r*p_j <= 0.
p = 1;
for t=th(:)'
    p = conv(p,[1,-2*cos(t),1]);
    p = real(p);
end
p(abs(p)<tol*max(1,norm(p,inf)))=0;
rMin = 1;
rMax = inf;
restricciones = 0;
for j=1:numel(p)-1
    A = p(j);      % multiplica a r con signo menos
    B = p(j+1);    % termino independiente: B-r*A <= 0
    escala=max([1,abs(A),abs(B)]);
    if abs(A)<=tol*escala
        if B>tol*escala
            admisible=false;
            detalle=sprintf('coef %d exige %.3e <= 0 con pendiente nula',j,B);
            return
        end
    elseif A>0
        rMin=max(rMin,B/A);
        restricciones=restricciones+1;
    else
        rMax=min(rMax,B/A);
        restricciones=restricciones+1;
    end
end
admisible = isfinite(rMin) && rMin<=rMax+tol*max(1,abs(rMin));
detalle=sprintf('%d restricciones activas; rMin=%.12g; rMax=%s', ...
    restricciones,rMin,texto_infinito(rMax));
end

function qc = coeficientes_Q_desde_p(p,r)
% Si p=[p0,...,p_{2K}], Q=(w-r)p tiene no lideres p1-r*p0,...,-r*p_{2K}.
qc = [p(2:end)-r*p(1:end-1), -r*p(end)];
qc = real(qc);
end

function [rmsIn,rmsOut,maxOut,R2out,c] = ajustar_y_predecir(A,y,itr,ite)
c=A(itr,:)\y(itr);
eIn=y(itr)-A(itr,:)*c;
eOut=y(ite)-A(ite,:)*c;
rmsIn=sqrt(mean(eIn.^2));
rmsOut=sqrt(mean(eOut.^2));
maxOut=max(abs(eOut));
den=sum(y(ite).^2);
if den<=realmin, R2out=NaN; else, R2out=1-sum(eOut.^2)/den; end
end

function d = distancia_conjuntos(a,b)
if isempty(a) || numel(a)~=numel(b), d=NaN; return; end
a=sort(a(:)); b=sort(b(:));
d=max(abs(a-b));
end

function h = nueva_historia(it,b,Np,ntr,wmin,theta,rMin,rMax,bObj,bSig,vacio,res,cambio,detalle)
h=struct('iter',it,'b',b,'Np',Np,'ntr',ntr,'omegaMin',wmin, ...
    'theta',theta(:)','rMin',rMin,'rMax',rMax,'bObjetivo',bObj, ...
    'bSiguiente',bSig,'intervaloVacio',vacio,'residuoRel',res, ...
    'cambioAngular',cambio,'detalle',detalle);
end

function s = texto_infinito(x)
if isinf(x) && x>0, s='Inf';
elseif isinf(x), s='-Inf';
else, s=sprintf('%.12g',x);
end
end

function exportar_historia(hist,nombre)
n=numel(hist);
iter=zeros(n,1); b=zeros(n,1); Np=zeros(n,1); ntr=zeros(n,1);
omegaMin=zeros(n,1); rMin=nan(n,1); rMax=nan(n,1);
bObjetivo=nan(n,1); bSiguiente=nan(n,1); intervaloVacio=false(n,1);
residuoRel=nan(n,1); cambioAngular=nan(n,1); detalle=cell(n,1);
for k=1:n
    iter(k)=hist(k).iter; b(k)=hist(k).b; Np(k)=hist(k).Np; ntr(k)=hist(k).ntr;
    omegaMin(k)=hist(k).omegaMin; rMin(k)=hist(k).rMin; rMax(k)=hist(k).rMax;
    bObjetivo(k)=hist(k).bObjetivo; bSiguiente(k)=hist(k).bSiguiente;
    intervaloVacio(k)=hist(k).intervaloVacio; residuoRel(k)=hist(k).residuoRel;
    cambioAngular(k)=hist(k).cambioAngular; detalle{k}=hist(k).detalle;
end
T=table(iter,b,Np,ntr,omegaMin,rMin,rMax,bObjetivo,bSiguiente, ...
    intervaloVacio,residuoRel,cambioAngular,detalle);
writetable(T,nombre);
end

function mu = criba_mobius(N)
t0=tic;
mu=ones(N,1,'int8');
cof=int64(1:N)';
lim=floor(sqrt(N));
esP=true(lim,1); esP(1)=false;
for i=2:floor(sqrt(lim))
    if esP(i), esP(i*i:i:lim)=false; end
end
pr=find(esP);
for k=1:numel(pr)
    p=pr(k); idx=p:p:N;
    mu(idx)=-mu(idx);
    cof(idx)=cof(idx)/int64(p);
    q=p*p;
    if q<=N, mu(q:q:N)=0; end
end
resto=cof>1;
mu(resto)=-mu(resto);
mu=double(mu);
fprintf('Criba terminada en %.1f s\n',toc(t0));
end
