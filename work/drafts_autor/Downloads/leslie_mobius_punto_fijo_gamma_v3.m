function resultado = leslie_mobius_punto_fijo_gamma_v3(b0, Kf, fraccionEntreno, Ncriba)
% LESLIE_MOBIUS_PUNTO_FIJO_GAMMA_V3
% Corrige la orientacion fila/columna del refinamiento espectral.
% Estima frecuencias omega en n SOLO en b0, elimina la frecuencia cero,
% congela gamma = omega/log(b0), y resuelve despues el punto fijo
%
%   b -> theta_k(b)=plegar_pi(gamma_k*log(b))
%     -> intervalo admisible de r para positividad
%     -> b_obj = r_min^2.
%
% Esta version NO necesita volver a muestrear M en cada b. Asi evita que
% b grande deje solo 7 puntos. M solo fija gamma en el tramo inicial.
%
% USO
%   R = leslie_mobius_punto_fijo_gamma_v3
%   R = leslie_mobius_punto_fijo_gamma_v3(1.15,6,0.65,2e7)
%
% FICHERO
%   Busca moebius.bin, mobius.bin o mu.bin, int8 con mu(1),mu(2),...

if nargin < 1 || isempty(b0), b0 = 1.15; end
if nargin < 2 || isempty(Kf), Kf = 6; end
if nargin < 3 || isempty(fraccionEntreno), fraccionEntreno = 0.65; end
if nargin < 4 || isempty(Ncriba), Ncriba = 2e7; end

cfg.maxIter = 100;
cfg.tolB = 1e-10;
cfg.tolTheta = 1e-9;
cfg.tolCoef = 1e-12;
cfg.margenR = 1e-10;
cfg.bMax = 1e12;
cfg.separacionFreq = 0.05;
cfg.refinaAncho = 0.03;
cfg.refinaPuntos = 81;
cfg.refinaVueltas = 5;
cfg.amortiguacion = 0.35;
cfg.detectarCiclo = true;

%% 1. Mu y observable inicial
mu = cargar_o_cribar_mu(Ncriba);
N = numel(mu);
M = cumsum(mu);
[n,x,y,ntr,itr,ite] = observable_inicial(M,N,b0,Kf,fraccionEntreno);

fprintf('mu(1..%d), mu(1..12) = %s\n',N,mat2str(mu(1:min(12,N))'));
fprintf('b0=%.12g | puntos=%d | entreno=%d | prueba=%d\n', ...
    b0,numel(y),numel(itr),numel(ite));

%% 2. Estimar omega en b0 y congelar gamma
[omega,omegaAntes,wmin] = estimar_frecuencias_cortadas(y(itr),n(itr),Kf,cfg);
if isempty(omega)
    error('No quedaron frecuencias despues del corte omega > 4*pi/Nentreno.');
end
gamma = omega/log(b0);
Kef = numel(gamma);

fprintf('\nFrecuencias iniciales: %d antes del corte, %d despues. wmin=%.8g\n', ...
    numel(omegaAntes),Kef,wmin);
fprintf('       omega              gamma=omega/log(b0)\n');
for k=1:Kef
    fprintf('  %14.10f        %18.10f\n',omega(k),gamma(k));
end

%% 3. Calidad predictiva inicial de libres frente a peine
mPeine = 2*Kf+1;
thetaPeine = 2*pi*(1:Kf)/mPeine;
Apeine = [cos(n*thetaPeine),sin(n*thetaPeine)];
Alibre = [cos(n*omega(:).'),sin(n*omega(:).')];
[riP,roP,moP,r2P,cP] = ajustar(Apeine,y,itr,ite);
[riL,roL,moL,r2L,cL] = ajustar(Alibre,y,itr,ite);
rmsCero = sqrt(mean(y(ite).^2));

fprintf('\nPREDICCION EN b0\n');
fprintf('Peine: RMS in %.6g | RMS out %.6g | max %.6g | R2 %+.6f\n',riP,roP,moP,r2P);
fprintf('Libre: RMS in %.6g | RMS out %.6g | max %.6g | R2 %+.6f\n',riL,roL,moL,r2L);
fprintf('Cero : RMS out %.6g\n',rmsCero);

%% 4. Resolver F(b)=0 por barrido y biseccion en tramos admisibles
% La iteracion directa puede caer en una zona con intervalo vacio aunque
% existan otros puntos fijos. Por eso esta version no concluye a partir de
% una orbita. Busca TODOS los cambios de signo sobre una malla logaritmica,
% separa discontinuidades del plegado y refina solo tramos admisibles.

bMinBarrido = 1.001;
bMaxBarrido = min(cfg.bMax,1e4);
nBarrido = 4000;
bBarrido = exp(linspace(log(bMinBarrido),log(bMaxBarrido),nBarrido))';
F = nan(nBarrido,1);
rMinBarrido = nan(nBarrido,1);
rMaxBarrido = nan(nBarrido,1);
admBarrido = false(nBarrido,1);
thetaBarrido = cell(nBarrido,1);

for ib=1:nBarrido
    [F(ib),rMinBarrido(ib),rMaxBarrido(ib),admBarrido(ib),thetaBarrido{ib}] = ...
        evaluar_F(bBarrido(ib),gamma,cfg.tolCoef);
end

% Un tramo solo es refinable si ambos extremos son admisibles, F cambia de
% signo y los angulos varian poco. Esto evita confundir un salto del plegado
% o una isla de no positividad con una raiz.
brackets = [];
for ib=1:nBarrido-1
    if ~(admBarrido(ib) && admBarrido(ib+1) && ...
            isfinite(F(ib)) && isfinite(F(ib+1)))
        continue
    end
    saltoTheta = max(abs(sort(thetaBarrido{ib})-sort(thetaBarrido{ib+1})));
    if saltoTheta > 0.10
        continue
    end
    if F(ib)==0 || F(ib)*F(ib+1)<0
        brackets(end+1,:)=[bBarrido(ib),bBarrido(ib+1)]; %#ok<AGROW>
    end
end

raices = struct('b',{},'r',{},'theta',{},'rMin',{},'rMax',{}, ...
    'F',{},'consistente',{},'L',{},'a',{},'validacion',{});
fprintf('\n================ RAICES DEL PUNTO FIJO ================\n');
for iq=1:size(brackets,1)
    lo=brackets(iq,1); hi=brackets(iq,2);
    [flo,~,~,alo,~]=evaluar_F(lo,gamma,cfg.tolCoef);
    [fhi,~,~,ahi,~]=evaluar_F(hi,gamma,cfg.tolCoef);
    if ~(alo && ahi && isfinite(flo) && isfinite(fhi)), continue; end

    valido=true;
    for it=1:100
        mb=sqrt(lo*hi);
        [fm,~,~,am,~]=evaluar_F(mb,gamma,cfg.tolCoef);
        if ~am || ~isfinite(fm)
            valido=false; break
        end
        if abs(fm)<1e-12 || abs(log(hi/lo))<1e-12
            lo=mb; hi=mb; break
        end
        if flo*fm<=0
            hi=mb; fhi=fm;
        else
            lo=mb; flo=fm;
        end
    end
    if ~valido, continue; end

    br=sqrt(lo*hi);
    [fr,rmn,rmx,adm,thr,pf]=evaluar_F_completo(br,gamma,cfg.tolCoef);
    rr=sqrt(br);
    consistente=adm && abs(fr)<1e-8 && rr>=rmn-1e-9 && rr<=rmx+1e-9;
    if ~consistente, continue; end

    [Lr,ar,valr]=construir_validar_leslie(br,thr,pf);
    nueva=struct('b',br,'r',rr,'theta',thr,'rMin',rmn,'rMax',rmx, ...
        'F',fr,'consistente',consistente,'L',Lr,'a',ar,'validacion',valr);
    if isempty(raices) || min(abs(log(br/[raices.b])))>1e-6
        raices(end+1)=nueva; %#ok<AGROW>
        fprintf(['raiz %2d: b=%.12g | r=%.12g | F=%+.3e | ' ...
                 'intervalo=[%.9g,%s] | Leslie=%d | min(a)=%.3e\n'], ...
            numel(raices),br,rr,fr,rmn,texto_inf(rmx),valr.construida,valr.minA);
    end
end

if isempty(raices)
    convergio=false;
    razonParada='no se encontro una raiz continua y admisible en el barrido';
    bFinal=NaN; rFinal=NaN; thetaFinal=[]; L=[]; a=[];
    validacion=struct('construida',false,'minA',NaN,'errPerron',NaN, ...
        'errModulo',NaN,'residuoPolinomio',NaN);
else
    convergio=true;
    razonParada=sprintf('%d puntos fijos admisibles encontrados',numel(raices));
    % Resultado principal: menor b positivo, para minimizar la escala.
    [~,imin]=min([raices.b]);
    bFinal=raices(imin).b; rFinal=raices(imin).r;
    thetaFinal=raices(imin).theta; L=raices(imin).L;
    a=raices(imin).a; validacion=raices(imin).validacion;
end

fprintf('\n================ RESULTADO ================\n');
fprintf('%s\n',razonParada);
if convergio
    fprintf('Punto fijo principal: b=%.15g | r=%.15g | K efectivo=%d\n', ...
        bFinal,rFinal,Kef);
    fprintf('Validacion: Leslie=%d | min(a)=%.3e | errP=%.3e | errMod=%.3e | resPol=%.3e\n', ...
        validacion.construida,validacion.minA,validacion.errPerron, ...
        validacion.errModulo,validacion.residuoPolinomio);
end

%% 7. Graficos
figure;
subplot(2,1,1); hold on; grid on
plot(n,y,'k.-','DisplayName','M(b0^n)/sqrt(b0^n)');
plot(n,Apeine*cP,'r-','DisplayName',sprintf('peine R2=%+.3f',r2P));
plot(n,Alibre*cL,'b-','DisplayName',sprintf('libre R2=%+.3f',r2L));
xline(n(ntr),'k--','LineWidth',1.4,'DisplayName','fin entreno');
xlabel('n'); ylabel('M/sqrt(x)'); legend show
title(sprintf('estimacion inicial b0=%.6g, K efectivo=%d',b0,Kef));
subplot(2,1,2); hold on; grid on
plot(n(ite),y(ite)-Apeine(ite,:)*cP,'r.-','DisplayName','residuo peine');
plot(n(ite),y(ite)-Alibre(ite,:)*cL,'b.-','DisplayName','residuo libre');
yline(0,'k-'); xlabel('n'); ylabel('error fuera'); legend show

figure; hold on; grid on
plot(bBarrido,F,'b-','LineWidth',1.0,'DisplayName','F(b) admisible');
yline(0,'k--','DisplayName','F=0');
for q=1:numel(raices)
    plot(raices(q).b,raices(q).F,'ro','MarkerFaceColor','r', ...
        'DisplayName',sprintf('raiz b=%.4g',raices(q).b));
end
set(gca,'XScale','log');
xlabel('b'); ylabel('F(b)=log(r_{min}(theta(b))^2/b)');
title('puntos fijos continuos y admisibles'); legend show

figure; hold on; grid on
plot(bBarrido,rMinBarrido.^2,'b-','DisplayName','r_{min}(b)^2');
plot(bBarrido,bBarrido,'k--','DisplayName','b');
set(gca,'XScale','log','YScale','log');
xlabel('b'); ylabel('escala'); title('intersecciones b=r_{min}(b)^2'); legend show

%% 8. Salida
resultado=struct;
resultado.convergio=convergio;
resultado.razonParada=razonParada;
resultado.b0=b0;
resultado.bFinal=bFinal;
resultado.rFinal=rFinal;
resultado.gamma=gamma;
resultado.omegaInicial=omega;
resultado.omegaAntesCorte=omegaAntes;
resultado.thetaFinal=thetaFinal;
resultado.raices=raices;
resultado.peine=struct('R2',r2P,'rmsOut',roP,'coef',cP);
resultado.libre=struct('R2',r2L,'rmsOut',roL,'coef',cL);
resultado.validacion=validacion;
resultado.L=L;
resultado.a=a;
resultado.bBarrido=bBarrido;
resultado.FBarrido=F;
resultado.admisibleBarrido=admBarrido;
resultado.n=n; resultado.x=x; resultado.y=y;

save('leslie_mobius_punto_fijo_gamma_v3_resultado.mat','resultado');
assignin('base','resultado_pf_gamma_v3',resultado);
if ~isempty(L), assignin('base','L_pf_gamma_v3',L); end
fprintf('Guardado: leslie_mobius_punto_fijo_gamma_v3_resultado.mat\n');

end

%% ========================================================================
function [omega,omega0,wmin]=estimar_frecuencias_cortadas(yv,nv,Kf,cfg)
yv=yv(:); nv=nv(:); yd=yv-mean(yv); Nn=numel(yv);
wmin=4*pi/Nn;
nf=2^nextpow2(32*Nn);
P=abs(fft(yd,nf)).^2;
w=2*pi*(0:nf-1)'/nf;
h=2:floor(nf/2)-1; w=w(h); P=P(h);
pico=false(size(P));
for k=2:numel(P)-1
    pico(k)=P(k)>P(k-1) && P(k)>=P(k+1);
end
id=find(pico); [~,ord]=sort(P(id),'descend'); id=id(ord);
omega0=[];
for q=1:numel(id)
    z=w(id(q));
    if z>=pi, continue; end
    if isempty(omega0) || min(abs(z-omega0))>cfg.separacionFreq
        omega0(end+1)=z; %#ok<AGROW>
    end
    if numel(omega0)>=Kf, break; end
end
omega=sort(omega0(omega0>wmin & omega0<pi-wmin)); omega=omega(:);
ancho=cfg.refinaAncho;
for vuelta=1:cfg.refinaVueltas
    for k=1:numel(omega)
        rej=linspace(max(wmin,omega(k)-ancho),min(pi-wmin,omega(k)+ancho),cfg.refinaPuntos);
        mejor=inf; zmej=omega(k);
        for z=rej
            tt=omega; tt(k)=z; tt=sort(tt);
            if numel(tt)>1 && min(diff(tt))<0.5*cfg.separacionFreq, continue; end
            tt = tt(:).'; A=[cos(nv*tt),sin(nv*tt)]; c=A\yv;
            e=norm(yv-A*c);
            if e<mejor, mejor=e; zmej=z; end
        end
        omega(k)=zmej; omega=sort(omega(:));
    end
    ancho=ancho/2;
end
omega=omega(:);
omega0=omega0(:);
end

function theta=plegar_pi(phi)
% Pliega frecuencias reales modulo 2*pi al representante de (0,pi).
theta=acos(cos(phi(:)));
theta=max(0,min(pi,theta));
end

function [rMin,rMax,adm,p,detalle]=intervalo_r_positivo(theta,tol)
p=1;
for t=theta(:)'
    p=conv(p,[1,-2*cos(t),1]);
    p=real(p);
end
p(abs(p)<tol*max(1,norm(p,inf)))=0;
rMin=1; rMax=inf; nr=0;
for j=1:numel(p)-1
    A=p(j); B=p(j+1); esc=max([1,abs(A),abs(B)]);
    if abs(A)<=tol*esc
        if B>tol*esc
            adm=false; detalle=sprintf('coef %d incompatible con pendiente cero',j); return
        end
    elseif A>0
        rMin=max(rMin,B/A); nr=nr+1;
    else
        rMax=min(rMax,B/A); nr=nr+1;
    end
end
adm=isfinite(rMin) && rMin<=rMax+tol*max(1,abs(rMin));
detalle=sprintf('%d restricciones; rMin=%.15g; rMax=%s',nr,rMin,texto_inf(rMax));
end

function qc=coeficientes_Q(p,r)
qc=[p(2:end)-r*p(1:end-1),-r*p(end)];
qc=real(qc);
end

function [F,rMin,rMax,adm,theta]=evaluar_F(b,gamma,tol)
theta=sort(plegar_pi(gamma*log(b)));
[rMin,rMax,adm]=intervalo_r_positivo(theta,tol);
if adm && rMin>0
    F=log(rMin^2/b);
else
    F=NaN;
end
end

function [F,rMin,rMax,adm,theta,p]=evaluar_F_completo(b,gamma,tol)
theta=sort(plegar_pi(gamma*log(b)));
[rMin,rMax,adm,p]=intervalo_r_positivo(theta,tol);
if adm && rMin>0, F=log(rMin^2/b); else, F=NaN; end
end

function [L,a,val]=construir_validar_leslie(b,theta,p)
r=sqrt(b);
qc=coeficientes_Q(p,r);
a=-qc.*r.^(1:numel(qc));
tolA=1e-9*max(1,max(abs(a)));
a(abs(a)<tolA)=0;
val=struct('construida',false,'minA',min(a),'errPerron',NaN, ...
    'errModulo',NaN,'residuoPolinomio',NaN);
L=[];
if min(a)<-tolA, return; end
m=numel(a); L=zeros(m); L(1,:)=a; L(2:m+1:end)=1;
ev=eig(L); [~,ip]=min(abs(ev-b)); lp=ev(ip); ev(ip)=[];
rp=[b;r*exp(1i*theta(:));r*exp(-1i*theta(:))];
pol=poly(rp.');
val=struct('construida',true,'minA',min(a),'errPerron',abs(lp-b), ...
    'errModulo',max(abs(abs(ev)-r)), ...
    'residuoPolinomio',max(abs(polyval(pol,rp)))/max(1,sum(abs(pol))));
end

function [n,x,y,ntr,itr,ite]=observable_inicial(M,N,b,Kf,f)
nmax=floor(log(N)/log(b)); n=(1:nmax)';
x=round(exp(n*log(b))); ok=x>=100 & x<=N; n=n(ok); x=x(ok);
[x,iu]=unique(x,'stable'); n=n(iu); y=M(x)./sqrt(x);
Np=numel(y); ntr=min(max(4*Kf+10,round(f*Np)),Np-5);
if Np<4*Kf+15, error('Solo %d puntos para estimar %d frecuencias.',Np,Kf); end
itr=1:ntr; ite=ntr+1:Np;
end

function [ri,ro,mo,r2,c]=ajustar(A,y,itr,ite)
c=A(itr,:)\y(itr); ei=y(itr)-A(itr,:)*c; eo=y(ite)-A(ite,:)*c;
ri=sqrt(mean(ei.^2)); ro=sqrt(mean(eo.^2)); mo=max(abs(eo));
den=sum(y(ite).^2); r2=1-sum(eo.^2)/den;
end

function h=entrada_hist(it,b,theta,rMin,rMax,bObj,bSig,res,dth,adm,detalle)
h=struct('iter',it,'b',b,'r',sqrt(b),'theta',theta(:)','rMin',rMin, ...
    'rMax',rMax,'bObjetivo',bObj,'bSiguiente',bSig,'residuoRel',res, ...
    'cambioTheta',dth,'admisible',adm,'detalle',detalle);
end

function d=cambio_theta(a,b)
if isempty(a) || numel(a)~=numel(b), d=NaN; else, d=max(abs(sort(a)-sort(b))); end
end

function s=texto_inf(x)
if isinf(x) && x>0, s='Inf'; elseif isinf(x), s='-Inf'; else, s=sprintf('%.15g',x); end
end

function exportar_historia(H,nombre)
if isempty(H), return; end
n=numel(H); iter=zeros(n,1); b=zeros(n,1); r=zeros(n,1); rMin=zeros(n,1);
rMax=zeros(n,1); bObjetivo=zeros(n,1); bSiguiente=zeros(n,1);
residuoRel=zeros(n,1); cambioTheta=zeros(n,1); admisible=false(n,1); detalle=cell(n,1);
for k=1:n
    iter(k)=H(k).iter; b(k)=H(k).b; r(k)=H(k).r; rMin(k)=H(k).rMin;
    rMax(k)=H(k).rMax; bObjetivo(k)=H(k).bObjetivo; bSiguiente(k)=H(k).bSiguiente;
    residuoRel(k)=H(k).residuoRel; cambioTheta(k)=H(k).cambioTheta;
    admisible(k)=H(k).admisible; detalle{k}=H(k).detalle;
end
T=table(iter,b,r,rMin,rMax,bObjetivo,bSiguiente,residuoRel,cambioTheta,admisible,detalle);
writetable(T,nombre);
end

function mu=cargar_o_cribar_mu(Ncriba)
mu=[];
for c={'moebius.bin','mobius.bin','mu.bin'}
    if isfile(c{1})
        fprintf('Usando fichero %s\n',c{1}); fid=fopen(c{1},'r');
        if fid<0, error('No se pudo abrir %s.',c{1}); end
        mu=double(fread(fid,inf,'*int8')); fclose(fid); break
    end
end
if isempty(mu), fprintf('Cribando hasta %g...\n',Ncriba); mu=criba_mobius(round(Ncriba)); end
end

function mu=criba_mobius(N)
mu=ones(N,1,'int8'); cof=int64(1:N)'; lim=floor(sqrt(N));
esP=true(lim,1); esP(1)=false;
for i=2:floor(sqrt(lim)), if esP(i), esP(i*i:i:lim)=false; end, end
pr=find(esP);
for k=1:numel(pr)
    p=pr(k); idx=p:p:N; mu(idx)=-mu(idx); cof(idx)=cof(idx)/int64(p);
    q=p*p; if q<=N, mu(q:q:N)=0; end
end
mu(cof>1)=-mu(cof>1); mu=double(mu);
end
