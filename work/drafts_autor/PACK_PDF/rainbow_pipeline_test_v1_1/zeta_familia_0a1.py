import mpmath as mp
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm

mp.mp.dps = 15

ts = np.linspace(0.05, 60, 3000)
betas = np.linspace(0.0, 1.0, 15)

fig = plt.figure(figsize=(13,9))
ax = fig.add_subplot(111, projection='3d')

cmap = cm.get_cmap('plasma')

for i, beta in enumerate(betas):
    vals = np.array([complex(mp.zeta(beta+1j*t)) for t in ts])
    color = cmap(i/(len(betas)-1))
    is_half = abs(beta-0.5) < 1e-9
    lw = 1.8 if is_half else 0.7
    zorder = 10 if is_half else 1
    ax.plot(ts, vals.real, vals.imag, color=('black' if is_half else color), lw=lw, zorder=zorder)

ax.plot(ts, np.zeros_like(ts), np.zeros_like(ts), color='red', lw=0.7, ls='--', alpha=0.5)

sm = cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(0.0,1.0))
sm.set_array([])
cbar = fig.colorbar(sm, ax=ax, shrink=0.6, pad=0.1)
cbar.set_label('beta')

ax.set_xlabel('t')
ax.set_ylabel('Re zeta(beta+it)')
ax.set_zlabel('Im zeta(beta+it)')
ax.set_title('zeta(beta+it), beta de 0 a 1 (linea negra = beta 1/2), t de 0 a 60')
ax.view_init(elev=20, azim=-60)

plt.tight_layout()
plt.savefig('zeta_familia_0a1.png', dpi=150)
print('guardado')
