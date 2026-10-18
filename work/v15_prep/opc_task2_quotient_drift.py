"""Task 2. Exact decomposition of the walk drift of zCasanya relative to the clock and the slow
quotient band R_N^slow(delta).

D_k = tau_k - x_k (actual), D1_k = S_X(tau_k)/L(tau_k) (one-step prime model, X = dyadic third cutoff).
V = sum_k w_k e^{i tau_k} F_k with w_k = (N-k+1)/N:
  actual  F = e^{-iD} - 1;  linear F = -iD;  quadratic F = -D^2/2;
  model:  -D1^2/2 = Re(H^2)/(4L^2) - |H|^2/(4L^2),  H = sum_{q<=X} a_q e^{i tau log q}.
Slow quotient band: ordered pairs (q,r), q != r, with |1 + log(q/r)| <= delta,
  R_{q,r} = -(a_q a_r / 4) sum_{k: q,r <= X_k} w_k e^{i tau_k (1 + log(q/r))} / L_k^2.
No true zero is used. Writes outputs/task2_*.csv/json/png.
"""
import json, csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from opc_common import *

tau = load('zLamb.bin'); cas = load('zCasanya.bin')
N = tau.size
k = np.arange(1, N + 1, dtype=float)
w = (N - k + 1) / N
Lt = L(tau)
X3 = dyadic_cut(tau, 512)
base_ph = np.exp(1j * tau)

D = tau - cas
S1, _ = S_and_dS(tau, X3, need_d=False)
D1 = (N0(tau) - (k - 0.5) + S1) / Lt

# H at tau with per-point cutoff
nt = int(np.searchsorted(PP_N, 512, side='right'))
H = np.zeros(N, complex)
diag = np.zeros(N)
for j in range(nt):
    m = X3 >= PP_N[j]
    H[m] += PP_COEF[j] * np.exp(1j * PP_FREQ[j] * tau[m])
    diag[m] += PP_COEF[j] ** 2
Fprod = np.real(H * H) / (4 * Lt ** 2)
Frat = -np.abs(H) ** 2 / (4 * Lt ** 2)
Fdiag = -diag / (4 * Lt ** 2)
ident = float(np.max(np.abs(Fprod + Frat + 0.5 * (np.imag(H) / Lt) ** 2)))

W = w * base_ph
def V(F): return complex(np.sum(W * F))
rep = {'identity_max_error': ident,
       'corr_D_D1': float(np.corrcoef(D, D1)[0, 1]),
       'rms_D_minus_D1': float(np.sqrt(np.mean((D - D1) ** 2))),
       'V_actual': V(np.exp(-1j * D) - 1), 'V_linear': V(-1j * D), 'V_quadratic': V(-D ** 2 / 2),
       'V_model_quadratic': V(-D1 ** 2 / 2), 'V_product': V(Fprod), 'V_quotient': V(Frat),
       'V_quotient_diagonal': V(Fdiag), 'V_quotient_offdiag': V(Frat - Fdiag)}

# slow quotient pairs
qs = PP_N[:nt]
pairs = []
for i in range(nt):
    for j in range(nt):
        if i == j:
            continue
        th = 1 + np.log(qs[i] / qs[j])
        if abs(th) <= 0.1:
            pairs.append((i, j, th))
print('slow pairs (|theta|<=0.1):', len(pairs), flush=True)
deltas = [0.0025, 0.005, 0.01, 0.02, 0.05, 0.1]
Rslow = {d: 0j for d in deltas}
nb = 100
edges = np.unique(np.round(np.linspace(0, N, nb + 1)).astype(int))
blk = {d: np.zeros(len(edges) - 1, complex) for d in deltas}
pair_rows = []
WL = w / Lt ** 2
for (i, j, th) in pairs:
    qmax = max(qs[i], qs[j])
    m = X3 >= qmax
    contrib = -(PP_COEF[i] * PP_COEF[j] / 4) * WL * np.exp(1j * tau * th) * m
    tot = complex(contrib.sum())
    pair_rows.append(dict(q=int(qs[i]), r=int(qs[j]), theta=th, re=tot.real, im=tot.imag, abs=abs(tot),
                          period_at_5e5=float(np.log(5e5 / TWO_PI) / abs(th)) if th else np.inf))
    cb = np.add.reduceat(contrib, edges[:-1])
    for d in deltas:
        if abs(th) <= d:
            Rslow[d] += tot
            blk[d] += cb
rep['R_slow'] = {str(d): Rslow[d] for d in deltas}

# block trajectories
def blocks(F): return np.add.reduceat(W * F, edges[:-1])
traj = {'actual': blocks(np.exp(-1j * D) - 1), 'quadratic_actual': blocks(-D ** 2 / 2),
        'linear_actual': blocks(-1j * D), 'product': blocks(Fprod), 'quotient': blocks(Frat)}
for d in (0.01, 0.02, 0.05, 0.1):
    traj[f'slow_{d}'] = blk[d]
def ccorr(a, b):
    a = a - a.mean(); b = b - b.mean()
    return float(abs(np.vdot(a, b)) / np.sqrt(np.vdot(a, a).real * np.vdot(b, b).real))
rep['block_increment_corr_with_actual'] = {kk: ccorr(traj['actual'], v) for kk, v in traj.items()}
rep['block_increment_corr_with_quotient'] = {kk: ccorr(traj['quotient'], v) for kk, v in traj.items()}
rep['top_pairs'] = sorted(pair_rows, key=lambda r: -r['abs'])[:25]

def enc(o):
    if isinstance(o, complex):
        return [o.real, o.imag]
    raise TypeError
json.dump(rep, open('outputs/task2_report.json', 'w'), indent=2, default=enc)
with open('outputs/task2_pairs.csv', 'w', newline='') as f:
    wr = csv.DictWriter(f, fieldnames=list(pair_rows[0].keys())); wr.writeheader(); wr.writerows(pair_rows)

kmid = 0.5 * (edges[:-1] + edges[1:])
fig, axs = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
for nm, st in (('actual', 'k-'), ('quadratic_actual', 'b-'), ('product', 'c-'), ('quotient', 'r-'),
               ('slow_0.02', 'm--'), ('slow_0.1', 'g--')):
    c = np.cumsum(traj[nm])
    axs[0].plot(kmid, c.real, st, label=nm); axs[1].plot(kmid, c.imag, st, label=nm)
axs[0].set_ylabel('Re cumulative'); axs[1].set_ylabel('Im cumulative'); axs[1].set_xlabel('index k')
axs[0].legend(fontsize=8); [a.grid(alpha=.3) for a in axs]
axs[0].set_title('Walk drift of zCasanya relative to the clock: exact decomposition')
fig.tight_layout(); fig.savefig('outputs/task2_drift_decomposition.png', dpi=130)
print(json.dumps(rep, indent=2, default=enc))
