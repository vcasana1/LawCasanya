function zCasanya0_optimizar()
% Law-Casanya: auditoria de errores y constructor PRIMO -> zCasanya0.bin.
% MATLAB R2019b+ (funciones locales). No requiere toolboxes estadisticos.
% Colocar en el mismo directorio de zeross.bin, zLamb.bin, zCasanya.bin
% (se aceptan tambien zeross(5).bin y zLamb(4).bin).
% No se usa zeta, arg(zeta), ni ceros verdaderos para construir un candidato.
% Los ceros verdaderos se usan SOLO para escoger el corte y evaluar el error.
% Las primeras dos ventanas se emplean para elegir; la tercera NO se toca
% hasta congelar la configuracion. Esto es seleccion empirica, NO prueba RH.

    close all;
    fileZ = find_input({'zeross.bin','zeross(5).bin'});
    fileL = find_input({'zLamb.bin','zLamb(4).bin'});
    fileOld = find_optional({'zCasanya.bin'});
    fileMono = find_optional({'zCasanya_monotona_10pctRvM.bin'});
    z = readbin(fileZ); L = readbin(fileL);
    assert(numel(z)==numel(L) && numel(z)>1,'Longitudes incompatibles');
    n=numel(z); fprintf('n=%d | ceros: %s | Lambert: %s\n',n,fileZ,fileL);
    audit('Lambert',L,z);
    if ~isempty(fileOld)
        old = readbin(fileOld); assert(numel(old)==n);
        audit('Casaña original',old,z);
    else
        old=[];
    end
    if ~isempty(fileMono)
        mono=readbin(fileMono); assert(numel(mono)==n);
        audit('Casaña monótona previa',mono,z);
    end

    % El paso 3 usa un X mayor. X=512 reproduce la estructura 8,8,512,
    % NO necesariamente cada detalle numerico del constructor Python c667.
    % Se puede ampliar cutoffs con 16384 o 32768, a costa de mas tiempo.
    cutoffs = [512 2048 8192];
    % Fraccion mínima de gap Lambert; 0 significa solo orden no decreciente.
    alphas = [0.01 0.05 0.10 0.20];
    blockSize = min(5000,floor(n/4));
    starts = [1 floor(n/2)-floor(blockSize/2)+1 n-blockSize+1];
    starts=max(1,min(n-blockSize+1,starts));
    inds=cell(1,3);
    for w=1:3, inds{w}=(starts(w):(starts(w)+blockSize-1)).'; end
    fprintf('\nOPTIMIZACION: [8,8,X], X en [%s]\n',num2str(cutoffs));
    fprintf('Bloques: entrenamiento [%d,%d], seleccion [%d,%d], test [%d,%d]\n',...
        inds{1}(1),inds{1}(end),inds{2}(1),inds{2}(end),inds{3}(1),inds{3}(end));

    score=inf; bestX=NaN; bestAlpha=NaN;
    for X=cutoffs
        fprintf('\nProbando X=%d\n',X);
        tr=prime_clock(L(inds{1}),inds{1},X);
        va=prime_clock(L(inds{2}),inds{2},X);
        for a=alphas
            ptr=monotone_project(tr,L(inds{1}),a);
            pva=monotone_project(va,L(inds{2}),a);
            ertrain=sqrt(mean((ptr-z(inds{1})).^2));
            erval=sqrt(mean((pva-z(inds{2})).^2));
            fprintf('  alpha=%5.3f, RMS train=%.9f, val=%.9f, gaps_no_pos(val)=%d\n',...
                a,ertrain,erval,sum(diff(pva)<=0));
            if erval<score
                score=erval;bestX=X;bestAlpha=a;
            end
        end
    end
    fprintf('\nCONFIGURACION CONGELADA: [8,8,%d], alpha=%.4f, RMS_validacion=%.9f\n',...
        bestX,bestAlpha,score);

    % Test final: sin reoptimizar en el bloque test.
    test=prime_clock(L(inds{3}),inds{3},bestX);
    test=monotone_project(test,L(inds{3}),bestAlpha);
    fprintf('RMS TEST INTACTO: %.9f | gaps_no_pos=%d\n',...
        sqrt(mean((test-z(inds{3})).^2)),sum(diff(test)<=0));

    % PRODUCCION COMPLETA EN EL ORDEN NATURAL. Candidato construido SIN z.
    fprintf('\nConstruyendo el candidato completo, puede consumir tiempo...\n');
    chunkSize=20000;
    cand=zeros(n,1);
    for st=1:chunkSize:n
        en=min(n,st+chunkSize-1);
        ii=(st:en).';
        cand(ii)=prime_clock(L(ii),ii,bestX);
        if mod(st-1,20*chunkSize)==0 || en==n
            fprintf('  calculados %d / %d\n',en,n);
        end
    end
    cand=monotone_project(cand,L,bestAlpha);
    audit('Casaña0 optimizada',cand,z);
    writebin('zCasanya0.bin',cand);
    fprintf('Archivo generado: %s (%d doubles)\n',fullfile(pwd,'zCasanya0.bin'),n);
    fprintf('RECUERDA: 0 inversiones de orden NO demuestra RH.\n');
end

function out=prime_clock(t0,k,X)
% Tres pasos de Newton con corte de potencias primas [8,8,X].
% F(t) = N0(t)+S_X(t)-(k-1/2).
% N0= t/(2*pi)*log(t/(2*pi*exp(1)))+7/8.
% S_X= -1/pi * sum_{p^m<=X} sin(m*t*log(p))/(m*p^(m/2)).
% Se usa N0'(t) = log(t/(2*pi))/(2*pi) como denominador de Newton.
    t=t0(:); k=k(:);
    assert(all(t>2*pi),'Se requieren t>2*pi');
    for c=[8 8 X]
        [omega,amp]=primepower_coeff(c);
        S=zeros(size(t));
        for j=1:numel(omega)
            S=S-amp(j)*sin(omega(j)*t);
        end
        smooth=t/(2*pi).*log(t/(2*pi*exp(1)))+7/8;
        ell=log(t/(2*pi))/(2*pi);
        step=(smooth+S-(k-0.5))./ell;
        % No recortar ni reordenar durante Newton: hacerlo introduciria
        % otra formulacion; la monotonia se impone despues, explicitamente.
        t=t-step;
        if any(~isfinite(t)) || any(t<=2*pi)
            error('Iteracion produce puntos invalidos. Reducir cortes o revisar altura.');
        end
    end
    out=t;
end

function [omega,amp]=primepower_coeff(X)
    pp=primes(X);
    omega=[];amp=[];
    for p=pp
        maxm=floor(log(X)/log(p)+1e-12);
        for m=1:maxm
            omega(end+1,1)=m*log(p); %#ok<AGROW>
            amp(end+1,1)=p^(-m/2)/(pi*m); %#ok<AGROW>
        end
    end
end

function y=monotone_project(x,L,alpha)
% PROYECCION ISOTONICA por PAV: min sum(y-x)^2 sujeto a
% y(k+1)-y(k) >= alpha*(L(k+1)-L(k)).
% Esto NO necesita gamma. alpha>0 y gap Lambert>0 -> gaps positivos.
    x=x(:);L=L(:);n=numel(x);
    u=x-alpha*L;
    level=zeros(n,1);weight=zeros(n,1);beg=zeros(n,1);fin=zeros(n,1);
    nb=0;
    for i=1:n
        nb=nb+1;level(nb)=u(i);weight(nb)=1;beg(nb)=i;fin(nb)=i;
        while nb>1 && level(nb-1)>level(nb)
            w=weight(nb-1)+weight(nb);
            level(nb-1)=(weight(nb-1)*level(nb-1)+weight(nb)*level(nb))/w;
            weight(nb-1)=w;fin(nb-1)=fin(nb);
            nb=nb-1;
        end
    end
    uout=zeros(n,1);
    for j=1:nb, uout(beg(j):fin(j))=level(j);end
    y=uout+alpha*L;
end

function audit(name,t,z)
    gap=diff(t); e=t-z; de=diff(e);m=min(gap);
    fprintf('\n%s\n',name);
    fprintf(' RMS=%.10f, MAE=%.10f, MaxError=%.10f\n',...
        sqrt(mean(e.^2)),mean(abs(e)),max(abs(e)));
    fprintf(' Gaps <=0: %d; min(gap)=%.12f\n',sum(gap<=0),m);
    fprintf(' max(e(k+1)-e(k))=%.12f\n',max(de));
    fprintf(' Incumplen DIF < min_gap: %d / %d\n',sum(de>=m),numel(gap));
    fprintf(' Incumplen DIF < gap_k: %d / %d; min(gap_k-DIF)=%.12f\n',...
        sum(de>=gap),numel(gap),min(gap-de));
    % gap_k-DIF = gamma(k+1)-gamma(k) es identidad exacta.
end

function fn=find_input(names)
    fn=find_optional(names);
    if isempty(fn)
        error('No encuentro los archivos: %s. Colocalos en el directorio actual.',strjoin(names,', '));
    end
end
function fn=find_optional(names)
    fn='';
    for j=1:numel(names)
        if isfile(names{j}),fn=names{j};return;end
    end
end
function v=readbin(fn)
    fid=fopen(fn,'rb','ieee-le');assert(fid>=0,['No se puede abrir ' fn]);
    c=onCleanup(@()fclose(fid));
    v=fread(fid,inf,'double=>double');
end
function writebin(fn,v)
    fid=fopen(fn,'wb','ieee-le');assert(fid>=0);
    c=onCleanup(@()fclose(fid));
    nw=fwrite(fid,v,'double');assert(nw==numel(v),'Escritura incompleta');
end