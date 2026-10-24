import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sigmas = np.load('sigmas_rainbow_completo.npy')
Mvals = np.load('Mvals_rainbow_completo.npy')

fig, axes = plt.subplots(1, 2, figsize=(12,4.5))

ax = axes[0]
ax.plot(sigmas, Mvals, 'o-', ms=4, color='#2563eb')
ax.axhline(0, color='gray', lw=0.6)
ax.set_xlabel(r'$\sigma$')
ax.set_ylabel(r'$M_8(\sigma)$')
ax.set_title(r'$M_8(\sigma)$: cero en $1/2$, positivo despues (No-Exit)')

ax = axes[1]
dM = np.gradient(Mvals, sigmas)
ax.plot(sigmas, dM, 'o-', ms=4, color='#dc2626')
ax.axhline(0, color='gray', lw=0.6)
ax.set_xlabel(r'$\sigma$')
ax.set_ylabel(r"$M_8'(\sigma)$")
ax.set_title(r"$M_8'(\sigma)$: nunca negativa (monotonia)")

plt.tight_layout()
plt.savefig('fig_Mn_test_lobulo8.png', dpi=150)
print('guardado')
