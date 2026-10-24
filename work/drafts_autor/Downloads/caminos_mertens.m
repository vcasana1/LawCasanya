function R = caminos_mertens(N, banda)
%CAMINOS_MERTENS  Enumera TODOS los reordenamientos de mu en [1,N] con los ceros fijos
%
%   R = caminos_mertens(30)          enumeracion completa
%   R = caminos_mertens(30, 'sqrt')  solo caminos dentro de la banda |M(n)-media| <= 2*sqrt(Q(n))
%   R = caminos_mertens(30, [lo hi]) solo caminos con lo <= M(n) <= hi en todo n
%
% Cada camino usa EXACTAMENTE los mismos 8 valores (+1), 11 valores (-1) y
% deja los ceros en sus posiciones aritmeticas -> el ratio global y la
% densidad de libres de cuadrados estan preservados por construccion.
% El punto final M(N) es el mismo para todos: barajar no cambia la suma.
%
% Distancias a cero que se calculan para cada camino:
%   sup|M|   = max_n |M(n)|
%   L1       = sum_n |M(n)|
%   L2c      = sum_n M(n)^2
% y se reporta el lugar exacto de la curva aritmetica real dentro de la familia.

if nargin<1 || isempty(N), N = 30; end
if nargin<2, banda = []; end

% ---------- mu, posiciones, conteos ----------------------------------------
mu   = mobius_sieve(N);          % 1 x N
sf   = find(mu~=0);
Q    = numel(sf);
v    = mu(sf);
kp   = sum(v== 1);
km   = sum(v==-1);
m    = sum(v);                   % = M(N)
ordn = cumsum(mu~=0);            % Q(n), 1 x N

K = nchoosek(Q,kp);
fprintf('N=%d   Q=%d   ceros=%d   +1=%d   -1=%d   M(N)=%d\n', N,Q,N-Q,kp,km,m);
fprintf('ordenaciones distintas  K = C(%d,%d) = %d\n', Q,kp,K);
fprintf('envolvente de la familia:  max = %+d   min = %+d\n', ...
        max(min((0:Q), 2*kp-(0:Q))), min(max(-(0:Q), (0:Q)-2*km)));

if K > 5e6
    error(['K=%d demasiado grande para enumerar.\n' ...
           'Usa prob_banda(Q,kp,lo,hi) al final de este fichero: da la ' ...
           'probabilidad exacta sin enumerar, en O(Q*ancho).'], K);
end

% ---------- todas las trayectorias ------------------------------------------
C = nchoosek(1:Q, kp);                                   % K x kp
S = -ones(K,Q);
S(sub2ind([K Q], repmat((1:K)',1,kp), C)) = 1;           % pasos +-1
W = cumsum(S,2);                                         % valor en cada ordinal
F = [zeros(K,1) W];  F = F(:, ordn+1);                   % K x N, ceros = tramos planos
clear S W C

Mreal = cumsum(mu);                                      % curva aritmetica real

% ---------- filtro opcional de banda ---------------------------------------
if ~isempty(banda)
    media = (ordn * m) / Q;                              % media exacta Q(n)*M(N)/Q
    if ischar(banda) || isstring(banda)
        env  = 2*sqrt(max(ordn,1));                      % banda "raiz cuadrada"
        keep = all(abs(F - media) <= env, 2);
        fprintf('\nfiltro: |M(n)-media(n)| <= 2*sqrt(Q(n))\n');
    else
        keep = all(F>=banda(1) & F<=banda(2), 2);
        fprintf('\nfiltro: %d <= M(n) <= %d\n', banda(1), banda(2));
    end
    fprintf('caminos que sobreviven: %d de %d  (%.4f%%)\n', sum(keep), K, 100*mean(keep));
    fprintf('¿la curva real sobrevive al filtro? %d\n', ...
            all(abs(Mreal - ((ordn*m)/Q)) <= 2*sqrt(max(ordn,1))) || ...
            (~ischar(banda) && all(Mreal>=banda(1) & Mreal<=banda(2))));
    F = F(keep,:);  K = size(F,1);
end

% ---------- distancias a cero -----------------------------------------------
sup = max(abs(F),[],2);   L1 = sum(abs(F),2);   L2c = sum(F.^2,2);
rs  = max(abs(Mreal));    r1 = sum(abs(Mreal)); r2  = sum(Mreal.^2);

R = struct('N',N,'Q',Q,'kp',kp,'km',km,'MN',m,'K',K, ...
           'sup',sup,'L1',L1,'L2',L2c, ...
           'real_sup',rs,'real_L1',r1,'real_L2',r2);

fprintf('\nM real:'); fprintf(' %d',Mreal); fprintf('\n');
informe('sup|M|',  sup, rs, K);
informe('sum|M|',  L1,  r1, K);
informe('sum M^2', L2c, r2, K);

% cotas estructurales
fprintf('\nNOTA: min(sup|M|) sobre la familia vale |M(N)|=%d por obligacion:\n',abs(m));
fprintf('      todo camino termina en %d, luego todo camino alcanza |M|>=%d.\n',m,abs(m));
end

% ============================================================================
function informe(nombre, arr, rv, K)
mn  = min(arr);
cnt = sum(arr==mn);
nl  = sum(arr<rv);
ne  = sum(arr==rv);
fprintf(['\n%-8s  real=%-6d  minimo=%-6d  #minimos=%-7d (%.4f%%)\n' ...
         '          estrictamente mejores que la real: %d  (percentil %.4f%%)   empates: %d\n' ...
         '          ¿la real esta en la clase minima? %d\n'], ...
         nombre, rv, mn, cnt, 100*cnt/K, nl, 100*nl/K, ne, rv==mn);
end

% ============================================================================
function mu = mobius_sieve(N)
mu = ones(1,N);
for p = primes(N)
    mu(p:p:N) = -mu(p:p:N);
    if p*p <= N, mu(p*p:p*p:N) = 0; end
end
end

% ============================================================================
function p = prob_banda(Q, kp, lo, hi)
%PROB_BANDA  P[ el puente (kp subidas, Q-kp bajadas) permanece en [lo,hi] ]
% Exacta, sin enumerar, en O(Q*(hi-lo+1)). Escala a Q enorme.
% Las probabilidades condicionales del puente son P(subir | j pasos, u subidas)
% = (kp-u)/(Q-j), con u=(j+v)/2.
if lo>0 || hi<0, p = 0; return; end
w = hi-lo+1;  P = zeros(1,w);  P(0-lo+1) = 1;
for j = 0:Q-1
    Pn = zeros(1,w);
    for ii = 1:w
        if P(ii)==0, continue; end
        vv = lo+ii-1;  u = (j+vv)/2;
        if u~=fix(u) || u<0 || u>kp, continue; end
        pu = (kp-u)/(Q-j);
        if vv+1<=hi, Pn(ii+1) = Pn(ii+1) + P(ii)*pu;     end
        if vv-1>=lo, Pn(ii-1) = Pn(ii-1) + P(ii)*(1-pu); end
    end
    P = Pn;
end
p = sum(P);
end
