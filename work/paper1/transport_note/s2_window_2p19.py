"""Mean square of s_k = (k - 1/2) - N0(gamma_k) over 2^19 < gamma_k <= 2^20,
the window of Table 7 (tab:transport) of v14. Used to compare <t_k^2> with c^2 <s_k^2>.
zeross.bin is read only for evaluation (s_k is a statistic of the true ordinates)."""
import numpy as np, json, os
here = os.path.dirname(os.path.abspath(__file__))
g = np.fromfile(os.path.join(here, '../../../data/zeross.bin'), '<f8')
k = np.arange(1, g.size + 1)
m = (g > 2**19) & (g <= 2**20)
t, kk = g[m], k[m]
theta = t/2*np.log(t/(2*np.pi)) - t/2 - np.pi/8 + 1/(48*t) + 7/(5760*t**3)
s = (kk - 0.5) - (theta/np.pi + 1)
s2 = float((s**2).mean())
table = {'1/5': 0.004905, '1/3': 0.011391, '1/2': 0.018283}   # <t_k^2> from Table 7, v14
cs = {'1/5': 0.2, '1/3': 1/3, '1/2': 0.5}
out = {'count': int(m.sum()), 'mean_s2': s2,
       'loglogT_over_2pi2_at_2^19': float(np.log(np.log(2**19))/(2*np.pi**2)),
       'rows': {c: {'c2_s2': cs[c]**2*s2, 't2_table': table[c], 'ratio': table[c]/(cs[c]**2*s2)} for c in cs}}
json.dump(out, open(os.path.join(here, 's2_window_2p19.json'), 'w'), indent=1)
print(json.dumps(out, indent=1))
