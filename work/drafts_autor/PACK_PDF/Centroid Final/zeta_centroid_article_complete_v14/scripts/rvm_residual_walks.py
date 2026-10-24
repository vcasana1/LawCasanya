#!/usr/bin/env python3
"""Reproduce the zeta/Lambert exponential walks and the residual constructions.

Input files are local binary arrays of IEEE-754 float64 values:
 - zeross.bin: positive zeta-zero ordinates, from Odlyzko's public table.
 - zLamb.bin: paired Lambert levels.

The mathematical objects are
 Z_k = exp(i gamma_k),
 V_k = exp(i tau_k),
 b_k = Z_k - V_k,
 u_k = exp(i (gamma_k-tau_k)),
 a_k = u_k - 1.

The script writes figures in PNG/PDF, a complete text report, and checkpoint CSVs.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


def triangular_centroid(x: np.ndarray) -> complex:
  n = x.size
  w = np.arange(n, 0, -1, dtype=np.float64) / n
  return np.sum(w * x)


def cfmt(z: complex) -> str:
  return f"{z.real:.15f} {z.imag:+.15f}i"


def select_indices(n: int, target: int = 6000) -> np.ndarray:
  if n <= target:
    return np.arange(n)
  return np.unique(np.linspace(0, n - 1, target, dtype=np.int64))


def save_figure(fig: plt.Figure, stem: Path) -> None:
  fig.savefig(stem.with_suffix('.png'), dpi=220, bbox_inches='tight', pad_inches=0.25)
  fig.savefig(stem.with_suffix('.pdf'), bbox_inches='tight', pad_inches=0.25)
  plt.close(fig)


def complex_limits(*arrays: np.ndarray, pad: float = 0.04):
  re_min = min(np.min(np.real(a)) for a in arrays)
  re_max = max(np.max(np.real(a)) for a in arrays)
  im_min = min(np.min(np.imag(a)) for a in arrays)
  im_max = max(np.max(np.imag(a)) for a in arrays)
  cx = 0.5 * (re_min + re_max)
  cy = 0.5 * (im_min + im_max)
  radius = 0.5 * max(re_max - re_min, im_max - im_min)
  radius *= (1.0 + pad)
  if radius == 0:
    radius = 1.0
  return (cx - radius, cx + radius), (cy - radius, cy + radius)


def make_dual_walk_figure(stem: Path, z: np.ndarray, curve1: np.ndarray, curve2: np.ndarray,
             label1: str, label2: str, title3d: str, title2d: str):
  idx = select_indices(curve1.size, target=5000)
  xlim, ylim = complex_limits(curve1[idx], curve2[idx], pad=0.06)
  fig = plt.figure(figsize=(12.6, 5.6))
  gs = GridSpec(1, 2, figure=fig, width_ratios=[1.45, 1.0])
  ax3 = fig.add_subplot(gs[0, 0], projection='3d')
  ax3.plot(curve1.real[idx], curve1.imag[idx], z[idx], linewidth=0.30, label=label1)
  ax3.plot(curve2.real[idx], curve2.imag[idx], z[idx], linewidth=0.30, label=label2)
  ax3.set_xlim(*xlim)
  ax3.set_ylim(*ylim)
  ax3.set_xlabel('Real part')
  ax3.set_ylabel('Imaginary part')
  ax3.set_zlabel(r'$k$', labelpad=-2)
  ax3.set_title(title3d)
  ax3.legend(loc='upper left', fontsize=8)
  ax2 = fig.add_subplot(gs[0, 1])
  ax2.plot(curve1.real[idx], curve1.imag[idx], linewidth=0.28, label=label1)
  ax2.plot(curve2.real[idx], curve2.imag[idx], linewidth=0.28, label=label2)
  ax2.set_xlim(*xlim)
  ax2.set_ylim(*ylim)
  ax2.set_aspect('equal', adjustable='box')
  ax2.axhline(0.0, linewidth=0.6)
  ax2.axvline(0.0, linewidth=0.6)
  ax2.set_xlabel('Real part')
  ax2.set_ylabel('Imaginary part')
  ax2.set_title(title2d)
  ax2.legend(loc='best', fontsize=8)
  fig.tight_layout()
  save_figure(fig, stem)


def make_single_walk_figure(stem: Path, z: np.ndarray, curve: np.ndarray, title3d: str, title2d: str,
              xlabel3d: str, ylabel3d: str):
  idx = select_indices(curve.size, target=7000)
  xlim, ylim = complex_limits(curve[idx], pad=0.06)
  fig = plt.figure(figsize=(12.0, 5.5))
  gs = GridSpec(1, 2, figure=fig, width_ratios=[1.45, 1.0])
  ax3 = fig.add_subplot(gs[0, 0], projection='3d')
  ax3.plot(curve.real[idx], curve.imag[idx], z[idx], linewidth=0.30)
  ax3.set_xlim(*xlim)
  ax3.set_ylim(*ylim)
  ax3.set_xlabel(xlabel3d)
  ax3.set_ylabel(ylabel3d)
  ax3.set_zlabel(r'$k$', labelpad=-2)
  ax3.set_title(title3d)
  ax2 = fig.add_subplot(gs[0, 1])
  ax2.plot(curve.real[idx], curve.imag[idx], linewidth=0.28)
  ax2.set_xlim(*xlim)
  ax2.set_ylim(*ylim)
  ax2.set_aspect('equal', adjustable='box')
  ax2.axhline(0.0, linewidth=0.6)
  ax2.axvline(0.0, linewidth=0.6)
  ax2.set_xlabel('Real part')
  ax2.set_ylabel('Imaginary part')
  ax2.set_title(title2d)
  fig.tight_layout()
  save_figure(fig, stem)


def main() -> None:
  parser = argparse.ArgumentParser()
  parser.add_argument('--zeros', type=Path, default=Path('zeross.bin'))
  parser.add_argument('--rvm', type=Path, default=Path('zLamb.bin'))
  parser.add_argument('--outdir', type=Path, default=Path('.'))
  args = parser.parse_args()

  outdir = args.outdir.resolve()
  figdir = outdir / 'figures'
  datadir = outdir / 'data'
  outputdir = outdir / 'outputs'
  figdir.mkdir(parents=True, exist_ok=True)
  datadir.mkdir(parents=True, exist_ok=True)
  outputdir.mkdir(parents=True, exist_ok=True)

  gamma = np.fromfile(args.zeros, dtype=np.float64)
  tau = np.fromfile(args.rvm, dtype=np.float64)
  if gamma.size != tau.size:
    raise ValueError(f'Length mismatch: {gamma.size} zeta ordinates vs {tau.size} Lambert levels')
  if gamma.size == 0:
    raise ValueError('Input arrays are empty')

  n_total = gamma.size
  n_axis = np.arange(1, n_total + 1, dtype=np.float64)
  delta = gamma - tau
  zeta_phase = np.exp(1j * gamma)
  lamb_phase = np.exp(1j * tau)
  paired_residual = zeta_phase - lamb_phase
  intrinsic_phase = np.exp(1j * delta)
  intrinsic_residual = intrinsic_phase - 1.0

  s_zeta = np.cumsum(zeta_phase)
  s_lamb = np.cumsum(lamb_phase)
  r_pair = np.cumsum(paired_residual)
  s_delta = np.cumsum(intrinsic_phase)
  r_intrinsic = np.cumsum(intrinsic_residual)

  c_zeta = triangular_centroid(zeta_phase)
  c_lamb = triangular_centroid(lamb_phase)
  c_pair = triangular_centroid(paired_residual)
  c_delta = triangular_centroid(intrinsic_phase)
  c_intrinsic = triangular_centroid(intrinsic_residual)

  c_pair_identity_error = abs(c_pair - (c_zeta - c_lamb))
  intrinsic_shift_error = abs(c_delta - (c_intrinsic + (n_total + 1) / 2.0))
  b_mod_identity_error = np.max(np.abs(np.abs(paired_residual) - 2.0 * np.abs(np.sin(delta / 2.0))))

  requested = np.array([10**3, 10**4, 10**5, 5*10**5, 10**6, n_total], dtype=np.int64)
  checkpoints = np.unique(requested[requested <= n_total])
  rows = []
  abs_r = np.abs(r_pair)
  running_max = np.maximum.accumulate(abs_r)
  for m in checkpoints:
    rows.append((m, abs_r[m-1], running_max[m-1]))
  np.savetxt(
    datadir / 'rvm_paired_residual_checkpoints.csv',
    np.asarray(rows),
    delimiter=',',
    header='N,abs_R_N,max_abs_R_k_up_to_N',
    comments='',
    fmt=['%d', '%.15e', '%.15e'],
  )

  delta_stats = np.array([[np.mean(delta), np.std(delta), np.min(delta), np.max(delta), np.mean(delta > 0)]])
  np.savetxt(
    datadir / 'rvm_delta_summary.csv',
    delta_stats,
    delimiter=',',
    header='mean_delta,std_delta,min_delta,max_delta,share_positive',
    comments='',
    fmt='%.15e',
  )

  n_intro = min(100_000, n_total)
  z_intro = np.arange(1, n_intro + 1, dtype=np.float64)
  make_dual_walk_figure(
    figdir / 'intro_zeta_vs_rvm_3d',
    z_intro,
    s_zeta[:n_intro],
    s_lamb[:n_intro],
    'True-zero walk',
    'Lambert walk',
    'Three-dimensional ordered exponential walks',
    'Projection on the complex plane',
  )

  make_single_walk_figure(
    figdir / 'intro_paired_residual_3d',
    n_axis,
    r_pair,
    r'Three-dimensional paired residual $R_k$',
    r'Complex-plane projection of $R_k$',
    r'$\Re R_k$',
    r'$\Im R_k$'
  )

  make_single_walk_figure(
    figdir / 'intro_difference_before_exponential_3d',
    n_axis,
    s_delta,
    r'Three-dimensional walk $U_k=\sum_{j\leq k} e^{i(\gamma_j-\tau_j)}$',
    r'Complex-plane projection of $U_k$',
    r'$\Re U_k$',
    r'$\Im U_k$'
  )

  make_single_walk_figure(
    figdir / 'intrinsic_centered_residual_3d',
    n_axis,
    r_intrinsic,
    r'Three-dimensional centered intrinsic residual $A_k$',
    r'Complex-plane projection of $A_k$',
    r'$\Re A_k$',
    r'$\Im A_k$'
  )

  energy_scale = float(np.sqrt(np.sum(np.abs(paired_residual)**2)))
  final_pair_abs = float(abs(r_pair[-1]))
  max_pair_abs = float(np.max(np.abs(r_pair)))
  max_pair_idx = int(np.argmax(np.abs(r_pair)) + 1)

  report = []
  report.append('RVM/ZETA EXPONENTIAL RESIDUAL AUDIT')
  report.append('===================================')
  report.append(f'zeros_file = {args.zeros.resolve()}')
  report.append(f'lambert_file = {args.rvm.resolve()}')
  report.append(f'N = {n_total}')
  report.append(f'gamma_1 = {gamma[0]:.15f}')
  report.append(f'gamma_N = {gamma[-1]:.15f}')
  report.append(f'tau_1 = {tau[0]:.15f}')
  report.append(f'tau_N = {tau[-1]:.15f}')
  report.append('')
  report.append('DELTA STATISTICS')
  report.append('----------------')
  report.append(f'mean(delta) = {np.mean(delta):.15e}')
  report.append(f'std(delta) = {np.std(delta):.15e}')
  report.append(f'min(delta) = {np.min(delta):.15e}')
  report.append(f'max(delta) = {np.max(delta):.15e}')
  report.append(f'share(delta>0) = {np.mean(delta > 0):.15e}')
  report.append('')
  report.append('FINAL PARTIAL SUMS')
  report.append('------------------')
  report.append(f'S_zeta(N) = {cfmt(s_zeta[-1])}')
  report.append(f'S_Lambert(N) = {cfmt(s_lamb[-1])}')
  report.append(f'R_pair(N) = {cfmt(r_pair[-1])}')
  report.append(f'|R_pair(N)| = {final_pair_abs:.15e}')
  report.append(f'max_n |R_pair(n)| = {max_pair_abs:.15e}')
  report.append(f'argmax_n |R_pair(n)| = {max_pair_idx}')
  report.append(f'sqrt(sum |b_k|^2) = {energy_scale:.15e}')
  report.append(f'|R_pair(N)| / sqrt(sum |b_k|^2) = {final_pair_abs/energy_scale:.15e}')
  report.append(f'S_delta(N) = {cfmt(s_delta[-1])}')
  report.append(f'A_intrinsic(N) = {cfmt(r_intrinsic[-1])}')
  report.append('')
  report.append('TRIANGULAR CENTROIDS')
  report.append('--------------------')
  report.append(f'C_zeta = {cfmt(c_zeta)}')
  report.append(f'C_Lambert = {cfmt(c_lamb)}')
  report.append(f'C_pair = {cfmt(c_pair)}')
  report.append(f'C_zeta - C_Lambert = {cfmt(c_zeta-c_lamb)}')
  report.append(f'identity error C_pair-(C_zeta-C_Lambert) = {c_pair_identity_error:.15e}')
  report.append(f'C_delta_phase = {cfmt(c_delta)}')
  report.append(f'C_intrinsic_residual = {cfmt(c_intrinsic)}')
  report.append(f'identity error C_delta-[C_intrinsic+(N+1)/2] = {intrinsic_shift_error:.15e}')
  report.append('')
  report.append('TERM-BY-TERM IDENTITY CHECK')
  report.append('---------------------------')
  report.append(f'max ||b_k|-2|sin(delta_k/2)|| = {b_mod_identity_error:.15e}')
  report.append('')
  report.append('PAIRED-RESIDUAL CHECKPOINTS')
  report.append('---------------------------')
  report.append('N, |R_N|, max_{k<=N}|R_k|')
  for m, val, mx in rows:
    report.append(f'{m}, {val:.15e}, {mx:.15e}')
  report.append('')
  report.append('FIGURES WRITTEN')
  report.append('---------------')
  for stem in [
    'intro_zeta_vs_rvm_3d',
    'intro_paired_residual_3d',
    'intro_difference_before_exponential_3d',
    'intrinsic_centered_residual_3d',
  ]:
    report.append(str((figdir / (stem + '.png')).resolve()))
    report.append(str((figdir / (stem + '.pdf')).resolve()))

  report_text = '\n'.join(report) + '\n'
  report_file = outputdir / 'rvm_residual_walks_output.txt'
  report_file.write_text(report_text, encoding='utf-8')
  print(report_text, end='')


if __name__ == '__main__':
  main()
