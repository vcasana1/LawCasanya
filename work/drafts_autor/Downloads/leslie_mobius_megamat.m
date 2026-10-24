function resultado = leslie_mobius_megamat(varargin)
% LESLIE_MOBIUS_MEGAMAT  Experimento final, autocontenido y reproducible.
%
% GUARDE ESTE ARCHIVO EXACTAMENTE COMO:
%   leslie_mobius_megamat.m
%
% EJECUCION NORMAL:
%   resultado = leslie_mobius_megamat();
%
% EJECUCION CON CONFIGURACION:
%   cfg = struct('archivoMu','moebius.bin','modoRapido',true);
%   resultado = leslie_mobius_megamat(cfg);
%
% OBJETIVO
%   1) Leer mu(1..N) desde un binario int8 sin cargarlo entero.
%   2) Construir y=M(x)/sqrt(x) en rejillas x=round(b^n).
%   3) Separar cronologicamente entrenamiento, validacion y prueba.
%   4) Comparar predictor cero, peine de raices de la unidad y frecuencias
%      libres elegidas EXCLUSIVAMENTE con entrenamiento.
%   5) Ejecutar controles nulos en streaming y sin matrices gigantes.
%   6) Comprobar si el espectro propuesto genera realmente un polinomio
%      companero no negativo. La semejanza diagonal D no cambia signos.
%   7) Buscar alternativas Leslie factibles sin usar datos de prueba.
%   8) Guardar MAT, CSV, TXT y PNG, incluso si el resultado es negativo.
%
% NO AFIRMA
%   Este programa no prueba cotas para M(x), RH ni un entrelazamiento
%   aritmetico. El veredicto distingue prediccion armonica de existencia
%   Leslie. Una mejora predictiva sin positividad NO cuenta como Leslie.
%
% COMPATIBILIDAD
%   Solo usa funciones base de MATLAB. No necesita Statistics, Signal
%   Processing, Optimization ni Parallel Computing Toolbox.

%% --------------------------- INICIO SEGURO -----------------------------
tInicio = tic;
close all;
clc;
rng(20260904,'twister');

cfg = configuracion_por_defecto();
if nargin >= 1
    if ~isstruct(varargin{1})
        error('La entrada opcional debe ser un struct de configuracion.');
    end
    cfg = fusionar_struct(cfg,varargin{1});
end
validar_configuracion(cfg);

nombreBase = 'leslie_mobius_megamat';
marca = datestr(now,'yyyymmdd_HHMMSS');
prefijo = fullfile(cfg.carpetaSalida,[nombreBase '_' marca]);
archivoMAT = [prefijo '_resultado.mat'];
archivoCSV = [prefijo '_modelos.csv'];
archivoTXT = [prefijo '_informe.txt'];
archivoPNG = [prefijo '_figura.png'];
archivoCheckpoint = [prefijo '_checkpoint.mat'];

diario = fopen(archivoTXT,'w');
if diario < 0
    error('No se pudo crear el informe: %s',archivoTXT);
end
limpiezaDiario = onCleanup(@() cerrar_si_abierto(diario));
logf(diario,'============================================================\n');
logf(diario,'LESLIE-MOBIUS MEGAMAT: EXPERIMENTO FINAL\n');
logf(diario,'Fecha MATLAB: %s\n',datestr(now,31));
logf(diario,'Archivo de funcion obligatorio: %s.m\n',nombreBase);
logf(diario,'============================================================\n\n');

resultado = struct();
resultado.version = '1.0.0';
resultado.configuracion = cfg;
resultado.archivos = struct('mat',archivoMAT,'csv',archivoCSV, ...
    'txt',archivoTXT,'png',archivoPNG,'checkpoint',archivoCheckpoint);
resultado.estado = 'INICIADO';
resultado.error = [];

try
    %% ---------------------- ARCHIVO Y PREVUELO -------------------------
    info = dir(cfg.archivoMu);
    if isempty(info)
        error(['No existe "%s" en la carpeta actual. Coloque moebius.bin ' ...
               'junto a este .m o indique cfg.archivoMu.'],cfg.archivoMu);
    end
    Narchivo = floor(info.bytes); % int8: un byte por valor
    if Narchivo < cfg.xMinimo
        error('El binario contiene %d valores, menos que xMinimo=%d.', ...
            Narchivo,cfg.xMinimo);
    end
    Nusar = min(Narchivo,floor(cfg.Nmax));
    if isinf(cfg.Nmax), Nusar = Narchivo; end
    estimacionGB = 6*cfg.tamanoBloque*8/2^30;
    logf(diario,'Archivo mu: %s\n',cfg.archivoMu);
    logf(diario,'Valores disponibles: %d\n',Narchivo);
    logf(diario,'Valores usados como maximo: %d\n',Nusar);
    logf(diario,'Bloque streaming: %d; RAM de trabajo estimada < %.3f GB\n\n', ...
        cfg.tamanoBloque,estimacionGB);

    comprobar_cabecera_mu(cfg.archivoMu,Nusar);

    %% -------- REJILLA GLOBAL DE PUNTOS PARA TODOS LOS b ----------------
    rejillas = cell(numel(cfg.bCandidatos),1);
    todosX = [];
    for ib = 1:numel(cfg.bCandidatos)
        b = cfg.bCandidatos(ib);
        n0 = ceil(log(double(cfg.xMinimo))/log(b));
        n1 = floor(log(double(Nusar))/log(b));
        n = (n0:n1).';
        x = unique(max(1,min(Nusar,round(b.^n))));
        if numel(x) > cfg.maxPuntosPorB
            pos = unique(round(linspace(1,numel(x),cfg.maxPuntosPorB)));
            x = x(pos);
            n = round(log(double(x))/log(b));
        else
            n = round(log(double(x))/log(b));
        end
        rejillas{ib} = struct('b',b,'n',n(:),'x',x(:));
        todosX = [todosX; x(:)]; %#ok<AGROW>
    end
    todosX = unique(todosX);
    if numel(todosX) < cfg.minPuntos
        error('Solo hay %d puntos distintos; se requieren al menos %d.', ...
            numel(todosX),cfg.minPuntos);
    end
    logf(diario,'Puntos x distintos a extraer: %d\n',numel(todosX));

    %% -------- STREAMING: M Y CONTROLES SIN CARGAR EL BINARIO -----------
    [Mmu,Mcuad,Mtodos,lectura] = extraer_sumatorias_streaming( ...
        cfg.archivoMu,todosX,Nusar,cfg.tamanoBloque,cfg.semillaNulos,diario);
    resultado.lectura = lectura;
    mapa = containers.Map(num2cell(double(todosX)),num2cell(1:numel(todosX)));

    %% ----------------- BUSQUEDA HONESTA DE MODELOS ---------------------
    modelos = repmat(modelo_vacio(),0,1);
    idModelo = 0;
    for ib = 1:numel(rejillas)
        R = rejillas{ib};
        idx = zeros(numel(R.x),1);
        for j=1:numel(R.x), idx(j)=mapa(double(R.x(j))); end
        y = Mmu(idx)./sqrt(double(R.x));
        yc = Mcuad(idx)./sqrt(double(R.x));
        yt = Mtodos(idx)./sqrt(double(R.x));
        datos = struct('b',R.b,'n',double(R.n),'x',double(R.x), ...
            'y',double(y),'nuloCuadradoLibre',double(yc), ...
            'nuloTodos',double(yt));
        if numel(y) < cfg.minPuntos, continue; end

        cortes = cortes_cronologicos(numel(y),cfg.fracEntrenamiento,cfg.fracValidacion);
        for K = cfg.KCandidatos
            if 2*K+cfg.minMargenParametros >= numel(cortes.entrenamiento)
                continue;
            end
            idModelo=idModelo+1;
            modelos(idModelo,1)=evaluar_configuracion(datos,cortes,K,cfg); %#ok<AGROW>
            modelos(idModelo).id=idModelo;
            logf(diario,['Modelo %3d | b=%8.5f K=%2d | libre R2test=%+8.4f ' ...
                '| peine=%+8.4f | Leslie libre=%d peine=%d\n'], ...
                idModelo,R.b,K,modelos(idModelo).libre.test.R2, ...
                modelos(idModelo).peine.test.R2, ...
                modelos(idModelo).leslieLibre.factible, ...
                modelos(idModelo).lesliePeine.factible);
        end
        resultado.parcial = modelos;
        save(archivoCheckpoint,'resultado','-v7.3');
    end
    if isempty(modelos), error('Ninguna configuracion tuvo suficientes puntos.'); end

    %% -------- SELECCION SIN MIRAR TEST: SOLO VALIDACION ----------------
    score = arrayfun(@(s) s.libre.validacion.RMSE,modelos);
    complejidad = arrayfun(@(s) s.K,modelos);
    scoreAjustado = score .* (1 + cfg.penalizacionK*complejidad);
    [~,iMejor] = min(scoreAjustado);
    mejor = modelos(iMejor);

    % Familia Leslie: se selecciona solo entre modelos factibles y por validacion.
    fact = arrayfun(@(s) s.leslieLibre.factible,modelos);
    if any(fact)
        ids = find(fact);
        [~,q] = min(scoreAjustado(ids));
        mejorLeslie = modelos(ids(q));
    else
        mejorLeslie = modelo_vacio();
        mejorLeslie.id = NaN;
    end

    %% ----------------------- CONTROLES NULOS ---------------------------
    controles = evaluar_controles(mejor,cfg);

    %% ------------------ CERTIFICADO ESTRUCTURAL ------------------------
    certificado = construir_certificado(mejor,mejorLeslie,modelos,cfg);

    %% ------------------------- VEREDICTO -------------------------------
    veredicto = emitir_veredicto(mejor,mejorLeslie,controles,certificado,cfg);
    resultado.estado='TERMINADO';
    resultado.mejorArmonico=mejor;
    resultado.mejorLeslie=mejorLeslie;
    resultado.modelos=modelos;
    resultado.controles=controles;
    resultado.certificado=certificado;
    resultado.veredicto=veredicto;
    resultado.segundos=toc(tInicio);

    %% ------------------------- SALIDAS ---------------------------------
    guardar_csv_modelos(archivoCSV,modelos);
    crear_figura(archivoPNG,mejor,modelos,controles,certificado);
    save(archivoMAT,'resultado','-v7.3');
    if exist(archivoCheckpoint,'file'), delete(archivoCheckpoint); end

    logf(diario,'\n===================== RESULTADO FINAL =====================\n');
    logf(diario,'Mejor armonico elegido SIN test: id=%d, b=%.8g, K=%d\n', ...
        mejor.id,mejor.b,mejor.K);
    log_metricas(diario,'LIBRE entrenamiento',mejor.libre.entrenamiento);
    log_metricas(diario,'LIBRE validacion',mejor.libre.validacion);
    log_metricas(diario,'LIBRE prueba',mejor.libre.test);
    log_metricas(diario,'PEINE prueba',mejor.peine.test);
    log_metricas(diario,'CERO prueba',mejor.cero.test);
    logf(diario,'Leslie libre factible: %d; min(a)=%.6g; residuo raices=%.3e\n', ...
        mejor.leslieLibre.factible,mejor.leslieLibre.minCoef, ...
        mejor.leslieLibre.residuoRaices);
    logf(diario,'Leslie peine factible: %d; min(a)=%.6g; residuo raices=%.3e\n', ...
        mejor.lesliePeine.factible,mejor.lesliePeine.minCoef, ...
        mejor.lesliePeine.residuoRaices);
    logf(diario,'VEREDICTO: %s\n',veredicto.codigo);
    logf(diario,'%s\n',veredicto.texto);
    logf(diario,'Tiempo total: %.2f s\n',resultado.segundos);
    logf(diario,'MAT: %s\nCSV: %s\nTXT: %s\nPNG: %s\n', ...
        archivoMAT,archivoCSV,archivoTXT,archivoPNG);

    fprintf('\n============================================================\n');
    fprintf('TERMINADO. %s\n%s\n',veredicto.codigo,veredicto.texto);
    fprintf('Resultados guardados con prefijo:\n  %s\n',prefijo);
    fprintf('============================================================\n');

catch ME
    resultado.estado='ERROR';
    resultado.error=struct('identifier',ME.identifier,'message',ME.message, ...
        'stack',{ME.stack});
    resultado.segundos=toc(tInicio);
    try, save(archivoMAT,'resultado','-v7.3'); catch, end
    logf(diario,'\nERROR FATAL: %s\n',ME.message);
    for k=1:numel(ME.stack)
        logf(diario,'  %s, linea %d\n',ME.stack(k).name,ME.stack(k).line);
    end
    fprintf(2,'\nMEGAMAT DETENIDO: %s\nInforme: %s\n',ME.message,archivoTXT);
    rethrow(ME);
end
end

%% =========================== CONFIGURACION =============================
function cfg=configuracion_por_defecto()
cfg=struct();
cfg.archivoMu='moebius.bin';
cfg.carpetaSalida=pwd;
cfg.Nmax=inf;
cfg.xMinimo=100;
cfg.tamanoBloque=2e6;
cfg.bCandidatos=[1.08 1.10 1.12 1.15 1.18 1.22 1.28];
cfg.KCandidatos=[3 4 5 6 8 10 12];
cfg.maxPuntosPorB=260;
cfg.minPuntos=75;
cfg.fracEntrenamiento=0.60;
cfg.fracValidacion=0.20;
cfg.minMargenParametros=12;
cfg.frecuenciasMalla=1200;
cfg.separacionFrecuencias=0.045;
cfg.ridge=logspace(-8,1,18);
cfg.incluirTendencia=true;
cfg.penalizacionK=0.002;
cfg.tolPositividad=5e-10;
cfg.tolRaices=5e-7;
cfg.semillaNulos=20260904;
cfg.numeroNulosAjuste=24;
cfg.modoRapido=false;
cfg.reiniciosLeslie=8;
end

function cfg=fusionar_struct(cfg,u)
f=fieldnames(u);
for i=1:numel(f), cfg.(f{i})=u.(f{i}); end
if isfield(u,'modoRapido') && u.modoRapido
    cfg.bCandidatos=[1.10 1.15 1.22]; cfg.KCandidatos=[3 6 10];
    cfg.frecuenciasMalla=500; cfg.numeroNulosAjuste=8; cfg.reiniciosLeslie=3;
end
end

function validar_configuracion(c)
assert(ischar(c.archivoMu)||isstring(c.archivoMu),'archivoMu no valido.');
assert(c.tamanoBloque>=1000 && c.tamanoBloque==floor(c.tamanoBloque),'tamanoBloque no valido.');
assert(all(c.bCandidatos>1),'Todos los b deben ser >1.');
assert(all(c.KCandidatos>=1 & c.KCandidatos==floor(c.KCandidatos)),'K no valido.');
assert(c.fracEntrenamiento>0.4 && c.fracEntrenamiento<0.8,'Fraccion de entrenamiento no valida.');
assert(c.fracValidacion>0.1 && c.fracEntrenamiento+c.fracValidacion<0.9,'Fraccion de validacion no valida.');
if ~exist(c.carpetaSalida,'dir'), mkdir(c.carpetaSalida); end
end

%% ========================= LECTURA STREAMING ============================
function comprobar_cabecera_mu(nombre,N)
fid=fopen(nombre,'rb'); if fid<0, error('No se pudo abrir %s.',nombre); end
c=onCleanup(@() fclose(fid));
v=fread(fid,min(12,N),'*int8').';
esperado=int8([1 -1 -1 0 -1 1 -1 0 0 1 -1 0]);
if numel(v)<12 || any(v~=esperado)
    error('La cabecera no coincide con mu(1..12). Formato o desplazamiento incorrecto.');
end
if any(~ismember(v,int8([-1 0 1]))), error('El binario contiene valores no validos.'); end
end

function [Mmu,Mc,Mt,info]=extraer_sumatorias_streaming(nombre,xObjetivo,Nusar,B,semilla,diario)
fid=fopen(nombre,'rb'); if fid<0, error('No se pudo abrir %s.',nombre); end
c=onCleanup(@() fclose(fid));
xObjetivo=double(xObjetivo(:)); q=1; nDone=0; M=0; C=0; T=0;
Mmu=zeros(size(xObjetivo)); Mc=Mmu; Mt=Mmu; bloque=0; ticLectura=tic;
while nDone<Nusar && q<=numel(xObjetivo)
    nLeer=min(B,Nusar-nDone); mu=fread(fid,nLeer,'*int8');
    if isempty(mu), break; end
    L=numel(mu); ids=(nDone+(1:L)).';
    md=double(mu); cm=M+cumsum(md);
    % Signos pseudoaleatorios deterministas por indice. No se almacena N.
    z1=sin((double(ids)+semilla)*12.9898)*43758.5453;
    s1=2*(z1-floor(z1)>=0.5)-1;
    z2=sin((double(ids)+semilla+17)*78.233)*12345.6789;
    s2=2*(z2-floor(z2)>=0.5)-1;
    cc=C+cumsum(double(mu~=0).*s1); % soporte cuadrado-libre, signos aleatorios
    ct=T+cumsum(s2);                % signos aleatorios en todos los enteros
    fin=nDone+L;
    while q<=numel(xObjetivo) && xObjetivo(q)<=fin
        loc=xObjetivo(q)-nDone;
        Mmu(q)=cm(loc); Mc(q)=cc(loc); Mt(q)=ct(loc); q=q+1;
    end
    M=cm(end); C=cc(end); T=ct(end); nDone=fin; bloque=bloque+1;
    if mod(bloque,20)==0 || nDone==Nusar
        logf(diario,'  streaming %d / %d (%.1f%%), %.1f s\n', ...
            nDone,Nusar,100*nDone/Nusar,toc(ticLectura));
    end
end
if q<=numel(xObjetivo), error('Lectura incompleta en x=%d.',xObjetivo(q)); end
info=struct('Nprocesado',nDone,'segundos',toc(ticLectura), ...
    'Mfinal',M,'controlCuadradoLibreFinal',C,'controlTodosFinal',T);
end

%% ========================= AJUSTE Y EVALUACION ==========================
function c=cortes_cronologicos(N,fTrain,fVal)
a=max(1,floor(fTrain*N)); b=max(a+1,floor((fTrain+fVal)*N));
c.entrenamiento=(1:a).'; c.validacion=(a+1:b).'; c.test=(b+1:N).';
if min([numel(c.entrenamiento),numel(c.validacion),numel(c.test)])<8
    error('Particion cronologica demasiado pequena.');
end
end

function s=evaluar_configuracion(datos,cortes,K,cfg)
s=modelo_vacio(); s.b=datos.b; s.K=K; s.n=datos.n; s.x=datos.x; s.y=datos.y; s.cortes=cortes;
itr=cortes.entrenamiento; iv=cortes.validacion;
thetaLibre=seleccionar_frecuencias(datos.n(itr),datos.y(itr),K,cfg);
thetaPeine=2*pi*(1:K).'/(2*K+1);
[lLibre,lamLibre]=ajustar_con_validacion(datos.n,datos.y,cortes,thetaLibre,cfg);
[lPeine,lamPeine]=ajustar_con_validacion(datos.n,datos.y,cortes,thetaPeine,cfg);
s.thetaLibre=thetaLibre; s.thetaPeine=thetaPeine; s.lambdaLibre=lamLibre; s.lambdaPeine=lamPeine;
s.libre=evaluar_predicciones(datos.y,lLibre,cortes);
s.peine=evaluar_predicciones(datos.y,lPeine,cortes);
s.cero=evaluar_predicciones(datos.y,zeros(size(datos.y)),cortes);
s.predLibre=lLibre; s.predPeine=lPeine;
s.datosNulos=struct('cuadradoLibre',datos.nuloCuadradoLibre,'todos',datos.nuloTodos);
s.leslieLibre=certificar_leslie(datos.b,thetaLibre,cfg);
s.lesliePeine=certificar_leslie(datos.b,thetaPeine,cfg);
% Busqueda local de un Leslie factible cercano a las frecuencias libres.
s.leslieOptimizado=buscar_leslie_cercano(datos.b,thetaLibre,cfg);
s.validacionUsada=iv;
end

function theta=seleccionar_frecuencias(n,y,K,cfg)
y=detrend_lineal(n,y); m=cfg.frecuenciasMalla;
grid=linspace(cfg.separacionFrecuencias,pi-cfg.separacionFrecuencias,m).';
pot=zeros(m,1); yc=y-mean(y);
for j=1:m
    z=exp(-1i*grid(j)*n); pot(j)=abs(z'*yc)^2/max(1,numel(y));
end
[~,ord]=sort(pot,'descend'); theta=[];
for j=1:numel(ord)
    t=grid(ord(j));
    if isempty(theta)||all(abs(angulo_envuelto(t-theta))>=cfg.separacionFrecuencias)
        theta(end+1,1)=t; %#ok<AGROW>
        if numel(theta)==K, break; end
    end
end
if numel(theta)<K, error('No se pudieron separar %d frecuencias.',K); end
theta=sort(theta);
end

function [pred,lambda]=ajustar_con_validacion(n,y,cortes,theta,cfg)
tr=cortes.entrenamiento; va=cortes.validacion; tv=[tr;va];
X=diseno_armonico(n,theta,cfg.incluirTendencia);
p=size(X,2); pen=ones(p,1); pen(1)=0;
if cfg.incluirTendencia, pen(2)=0; end
err=zeros(numel(cfg.ridge),1);
for j=1:numel(cfg.ridge)
    w=resolver_ridge(X(tr,:),y(tr),cfg.ridge(j),pen);
    err(j)=sqrt(mean((y(va)-X(va,:)*w).^2));
end
[~,q]=min(err); lambda=cfg.ridge(q);
w=resolver_ridge(X(tv,:),y(tv),lambda,pen);
pred=X*w;
end

function X=diseno_armonico(n,theta,tend)
n=double(n(:)); K=numel(theta); X=ones(numel(n),1+2*K+tend);
c=2;
if tend
    nn=(n-mean(n))/max(std(n),1); X(:,2)=nn; c=3;
end
for k=1:K
    X(:,c)=cos(theta(k)*n); X(:,c+1)=sin(theta(k)*n); c=c+2;
end
end

function w=resolver_ridge(X,y,lambda,pen)
A=X.'*X+lambda*diag(pen); rhs=X.'*y;
if rcond(A)<1e-13, w=pinv(A)*rhs; else, w=A\rhs; end
end

function out=evaluar_predicciones(y,p,c)
out.entrenamiento=metricas(y(c.entrenamiento),p(c.entrenamiento));
out.validacion=metricas(y(c.validacion),p(c.validacion));
out.test=metricas(y(c.test),p(c.test));
end

function m=metricas(y,p)
r=y-p; m.N=numel(y); m.RMSE=sqrt(mean(r.^2)); m.MAE=mean(abs(r));
m.maxAbs=max(abs(r)); den=sum((y-mean(y)).^2);
if den<=eps, m.R2=NaN; else, m.R2=1-sum(r.^2)/den; end
m.sesgo=mean(r); m.correlacion=correlacion_segura(y,p);
end

%% ===================== CERTIFICADO LESLIE EXACTO =======================
function c=certificar_leslie(b,theta,cfg)
rho=sqrt(b); roots=[b; rho*exp(1i*theta(:)); rho*exp(-1i*theta(:))];
p=poly(roots); p=real_if_close(p); a=-p(2:end).';
raicesRecon=roots_from_companion(a);
res=distancia_multiconjunto(roots,raicesRecon)/max(1,max(abs(roots)));
c=struct('factible',all(a>=-cfg.tolPositividad)&&res<=cfg.tolRaices, ...
    'a',a,'minCoef',min(a),'numeroNegativos',nnz(a<-cfg.tolPositividad), ...
    'residuoRaices',res,'rootsObjetivo',roots,'rootsReconstruidas',raicesRecon, ...
    'explicacion','a=-poly(roots)(2:end); D positiva no cambia los signos.');
end

function c=buscar_leslie_cercano(b,theta0,cfg)
mejor=certificar_leslie(b,theta0,cfg); mejor.distancia=0; mejor.theta=theta0;
objMejor=objetivo_leslie(mejor,theta0,theta0);
opt=optimset('Display','off','MaxIter',1200,'MaxFunEvals',5000,'TolX',1e-9,'TolFun',1e-10);
for r=1:cfg.reiniciosLeslie
    if r==1, q0=theta0; else, q0=sort(pi*rand(size(theta0))); end
    [q,~]=fminsearch(@(z) objetivo_theta(z,b,theta0,cfg),q0,opt);
    q=sort(mod(q,pi)); cc=certificar_leslie(b,q,cfg);
    cc.distancia=norm(sort(q)-sort(theta0))/sqrt(numel(q)); cc.theta=q;
    ob=objetivo_leslie(cc,q,theta0);
    if ob<objMejor, mejor=cc; objMejor=ob; end
end
c=mejor; c.objetivo=objMejor;
end

function z=objetivo_theta(theta,b,theta0,cfg)
t=sort(mod(theta(:),pi)); c=certificar_leslie(b,t,cfg); z=objetivo_leslie(c,t,theta0);
% Barrera contra frecuencias duplicadas o bordes.
d=diff(t); z=z+1e3*sum(max(0,cfg.separacionFrecuencias-d).^2);
z=z+1e3*sum(max(0,cfg.separacionFrecuencias-[t;pi-t]).^2);
end

function z=objetivo_leslie(c,t,t0)
neg=min(c.a,0); z=1e7*sum(neg.^2)+1e3*c.numeroNegativos+ ...
    norm(sort(t)-sort(t0))^2+1e4*c.residuoRaices;
end

function rr=roots_from_companion(a)
m=numel(a); C=zeros(m); C(1,:)=a(:).'; C(2:end,1:end-1)=eye(m-1); rr=eig(C);
end

function d=distancia_multiconjunto(a,b)
a=a(:); b=b(:); usado=false(size(b)); acc=0;
for i=1:numel(a)
    q=find(~usado); [v,j]=min(abs(b(q)-a(i))); usado(q(j))=true; acc=max(acc,v);
end
d=acc;
end

%% ============================= NULOS ===================================
function C=evaluar_controles(mejor,cfg)
C=struct(); n=mejor.n; cortes=mejor.cortes; K=mejor.K;
series={mejor.datosNulos.cuadradoLibre,mejor.datosNulos.todos};
nombres={'soporte_cuadrado_libre_signos_aleatorios','signos_aleatorios_todos'};
for i=1:numel(series)
    y=series{i}; th=seleccionar_frecuencias(n(cortes.entrenamiento),y(cortes.entrenamiento),K,cfg);
    [p,lam]=ajustar_con_validacion(n,y,cortes,th,cfg);
    C.(nombres{i})=struct('theta',th,'lambda',lam,'metricas',evaluar_predicciones(y,p,cortes));
end
% Nulos por desplazamiento circular de y: se ajustan con la misma disciplina.
r2=zeros(cfg.numeroNulosAjuste,1); rm=zeros(size(r2));
for j=1:numel(r2)
    despl=randi([max(3,round(.1*numel(n))),max(4,round(.9*numel(n)))]);
    y=circshift(mejor.y,despl);
    th=seleccionar_frecuencias(n(cortes.entrenamiento),y(cortes.entrenamiento),K,cfg);
    p=ajustar_con_validacion(n,y,cortes,th,cfg);
    e=evaluar_predicciones(y,p,cortes); r2(j)=e.test.R2; rm(j)=e.test.RMSE;
end
C.desplazamientos=struct('R2test',r2,'RMSEtest',rm, ...
    'pEmpiricoR2',(1+sum(r2>=mejor.libre.test.R2))/(1+numel(r2)));
end

%% ======================= CERTIFICADO Y VEREDICTO =======================
function C=construir_certificado(mejor,mejorL,modelos,cfg)
C=struct();
C.hayLeslieFactible=any(arrayfun(@(s) s.leslieLibre.factible||s.lesliePeine.factible||s.leslieOptimizado.factible,modelos));
C.mejorArmonicoEsLeslie=mejor.leslieLibre.factible;
C.mejorArmonicoTieneLeslieCercano=mejor.leslieOptimizado.factible;
C.numeroModelos=numel(modelos);
C.numeroFactibles=sum(arrayfun(@(s) s.leslieLibre.factible||s.lesliePeine.factible||s.leslieOptimizado.factible,modelos));
C.toleranciaPositividad=cfg.tolPositividad;
C.seleccionUsoTest=false;
C.entrelazamientoProbado=false;
if isnan(mejorL.id), C.idMejorLeslie=NaN; else, C.idMejorLeslie=mejorL.id; end
end

function V=emitir_veredicto(mejor,mejorL,controles,C,cfg)
mejora=mejor.libre.test.RMSE < mejor.cero.test.RMSE;
p=controles.desplazamientos.pEmpiricoR2;
robusto=p<=0.05;
if mejora && mejor.leslieLibre.factible && robusto
    codigo='EVIDENCIA_NUMERICA_LESLIE_LOCAL';
    texto=['El predictor seleccionado sin mirar test mejora al cero, supera los ' ...
      'desplazamientos nulos y su polinomio companero es no negativo. Es evidencia ' ...
      'numerica local, no un teorema ni un puente con Mobius.'];
elseif mejora && ~mejor.leslieLibre.factible
    codigo='SOLO_PREDICTOR_ARMONICO_NO_LESLIE';
    texto=['Existe mejora fuera de muestra del ajuste armonico, pero el espectro ' ...
      'seleccionado no define una Leslie no negativa. No cuenta como resultado Leslie.'];
elseif ~mejora && C.hayLeslieFactible
    codigo='LESLIE_FACTIBLE_SIN_PREDICCION';
    texto=['Se encontraron companeras no negativas en el dominio explorado, pero ' ...
      'el predictor elegido no mejora al predictor cero en prueba.'];
else
    codigo='RESULTADO_NEGATIVO_EN_DOMINIO_EXPLORADO';
    texto=['No aparece simultaneamente positividad Leslie y mejora predictiva ' ...
      'fuera de muestra bajo la rejilla, K, b y tolerancias declaradas.'];
end
if ~robusto && mejora
    texto=[texto ' La ventaja no supera el control empirico de desplazamientos al 5%.'];
end
if ~isnan(mejorL.id)
    texto=[texto sprintf(' Mejor modelo Leslie factible: id %d.',mejorL.id)];
end
texto=[texto sprintf(' p nulo empirico=%.4g; tolerancia positividad=%.3g.',p,cfg.tolPositividad)];
V=struct('codigo',codigo,'texto',texto,'mejoraContraCero',mejora, ...
    'superaNulos5pct',robusto,'pNuloEmpirico',p);
end

%% ============================= SALIDAS =================================
function guardar_csv_modelos(nombre,S)
fid=fopen(nombre,'w'); if fid<0, error('No se pudo crear %s.',nombre); end
c=onCleanup(@() fclose(fid));
fprintf(fid,['id,b,K,R2_libre_val,RMSE_libre_val,R2_libre_test,RMSE_libre_test,' ...
 'R2_peine_test,RMSE_peine_test,RMSE_cero_test,leslie_libre,leslie_peine,' ...
 'leslie_optimizado,mincoef_libre,mincoef_peine\n']);
for i=1:numel(S)
 fprintf(fid,'%d,%.15g,%d,%.15g,%.15g,%.15g,%.15g,%.15g,%.15g,%.15g,%d,%d,%d,%.15g,%.15g\n', ...
  S(i).id,S(i).b,S(i).K,S(i).libre.validacion.R2,S(i).libre.validacion.RMSE, ...
  S(i).libre.test.R2,S(i).libre.test.RMSE,S(i).peine.test.R2,S(i).peine.test.RMSE, ...
  S(i).cero.test.RMSE,S(i).leslieLibre.factible,S(i).lesliePeine.factible, ...
  S(i).leslieOptimizado.factible,S(i).leslieLibre.minCoef,S(i).lesliePeine.minCoef);
end
end

function crear_figura(nombre,m,modelos,C,cert)
f=figure('Color','w','Position',[50 50 1500 900]);
subplot(2,2,1); plot(m.n,m.y,'k.-'); hold on; plot(m.n,m.predLibre,'b-','LineWidth',1.2); plot(m.n,m.predPeine,'r-');
xline(m.n(m.cortes.validacion(1)),'--'); xline(m.n(m.cortes.test(1)),'--');
grid on; xlabel('n'); ylabel('M(x)/sqrt(x)'); title(sprintf('b=%.4g, K=%d',m.b,m.K)); legend('dato','libre','peine','fin train','inicio test','Location','best');
subplot(2,2,2); stem(m.thetaLibre,ones(size(m.thetaLibre)),'g','filled'); hold on; stem(m.thetaPeine,.8*ones(size(m.thetaPeine)),'r'); xlim([0 pi]); grid on; xlabel('frecuencia'); title('Frecuencias: libre verde, peine rojo');
subplot(2,2,3); r2=arrayfun(@(s)s.libre.test.R2,modelos); mc=arrayfun(@(s)s.leslieLibre.minCoef,modelos); scatter(mc,r2,36,'filled'); xline(0,'k--'); yline(0,'k:'); grid on; xlabel('min coeficiente companero'); ylabel('R2 prueba libre'); title(sprintf('Factibles globales: %d/%d',cert.numeroFactibles,cert.numeroModelos));
subplot(2,2,4); histogram(C.desplazamientos.R2test,max(5,round(sqrt(numel(C.desplazamientos.R2test))))); hold on; xline(m.libre.test.R2,'r','LineWidth',2); grid on; xlabel('R2 prueba'); title(sprintf('Nulos desplazados, p=%.4g',C.desplazamientos.pEmpiricoR2));
try, exportgraphics(f,nombre,'Resolution',170); catch, saveas(f,nombre); end
end

%% ============================ UTILIDADES ================================
function s=modelo_vacio()
s=struct('id',NaN,'b',NaN,'K',NaN,'n',[],'x',[],'y',[],'cortes',[], ...
 'thetaLibre',[],'thetaPeine',[],'lambdaLibre',NaN,'lambdaPeine',NaN, ...
 'libre',[],'peine',[],'cero',[],'predLibre',[],'predPeine',[], ...
 'datosNulos',[],'leslieLibre',[],'lesliePeine',[],'leslieOptimizado',[], ...
 'validacionUsada',[]);
end
function y=detrend_lineal(x,y)
X=[ones(numel(x),1),x(:)-mean(x)]; y=y(:)-X*(X\y(:));
end
function r=correlacion_segura(a,b)
a=a(:)-mean(a); b=b(:)-mean(b); d=norm(a)*norm(b); if d<=eps,r=NaN;else,r=(a'*b)/d;end
end
function a=angulo_envuelto(a), a=mod(a+pi,2*pi)-pi; end
function x=real_if_close(x)
if max(abs(imag(x)))<=1e-8*max(1,max(abs(real(x)))), x=real(x); else, error('Coeficientes con parte imaginaria significativa.'); end
end
function log_metricas(fid,n,m)
logf(fid,'%s: N=%d RMS=%.6g MAE=%.6g max=%.6g R2=%+.6g sesgo=%+.6g corr=%+.6g\n', ...
 n,m.N,m.RMSE,m.MAE,m.maxAbs,m.R2,m.sesgo,m.correlacion);
end
function logf(fid,varargin), fprintf(varargin{:}); fprintf(fid,varargin{:}); end
function cerrar_si_abierto(fid), try, fclose(fid); catch, end, end
