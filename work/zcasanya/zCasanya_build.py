#!/usr/bin/env python3
"""Prime-only arithmetic Newton construction. Never imports the validator.

CLI: python3 zCasanya_build.py --data-dir DIR --output DIR --stage pilot|full
The full stage consumes shortlist.json, which contains parameters, not zero data.
"""
from pathlib import Path
import argparse
import hashlib
import json
import sys
import time
from itertools import combinations_with_replacement
import numpy as np

TWO_PI = 2 * np.pi
N_EXPECTED = 2001052


def guard(event, args):
    if event == 'open' and isinstance(args[0], (str, bytes)):
        name = str(args[0]).lower()
        if 'zeross' in name:
            raise PermissionError('The construction process cannot open true-zero data')


def sha256(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(8 * 1024**2), b''):
            h.update(block)
    return h.hexdigest()


def clock(t):
    return t / TWO_PI * (np.log(t / TWO_PI) - 1) + .875


def slope(t):
    return np.log(t / TWO_PI) / TWO_PI


def clock_difference(t, tau):
    """N0(t)-N0(tau); cancellation-free Taylor remainder for |u|<.01."""
    d = t - tau
    u = d / tau
    h = np.empty_like(u)
    small = np.abs(u) < .01
    v = u[small]
    # h(u)=(1+u)log(1+u)-u=sum_{n>=2}(-1)^n*u^n/(n(n-1)).
    poly = np.full_like(v, 1 / (14 * 13))
    for n in range(13, 1, -1):
        poly = (-1.)**n / (n * (n - 1)) + v * poly
    h[small] = v * v * poly
    v = u[~small]
    h[~small] = (1 + v) * np.log1p(v) - v
    return slope(tau) * d + tau / TWO_PI * h


def load_inputs(data_dir, output):
    tau_path = data_dir / 'zLamb.bin'
    prime_path = data_dir / 'primoss.bin'
    assert tau_path.stat().st_size == 8 * N_EXPECTED
    tau = np.fromfile(tau_path, dtype='<f8')
    assert np.all(np.isfinite(tau)) and np.all(np.diff(tau) > 0)
    assert 14 < tau[0] < 15 and 1.13e6 < tau[-1] < 1.14e6
    prime_count = prime_path.stat().st_size // 8
    assert prime_path.stat().st_size % 8 == 0
    primes = np.fromfile(prime_path, dtype='<u8', count=148934)
    sieve = np.ones(2000001, dtype=bool)
    sieve[:2] = False
    for i in range(2, 1415):
        if sieve[i]:
            sieve[i*i::i] = False
    reference = np.flatnonzero(sieve)
    assert len(reference) == 148933
    assert np.array_equal(primes[:148933], reference)
    assert primes[148933] == 2000003
    with prime_path.open('rb') as f:
        f.seek(-40, 2)
        last = np.fromfile(f, dtype='<u8')
    # Check the complete prime file for order by bounded-memory blocks.
    previous, records = 0, 0
    with prime_path.open('rb') as f:
        while True:
            a = np.fromfile(f, dtype='<u8', count=1000000)
            if not len(a):
                break
            assert a[0] > previous and np.all(a[1:] > a[:-1])
            previous, records = int(a[-1]), records + len(a)
    assert records == prime_count
    info = {
        'zLamb': {'path': str(tau_path), 'dtype': '<f8', 'records': len(tau),
                  'bytes': tau_path.stat().st_size, 'first': tau[:5].tolist(),
                  'last': tau[-5:].tolist(), 'sha256': sha256(tau_path)},
        'primes': {'path': str(prime_path), 'dtype': '<u8', 'records': prime_count,
                   'bytes': prime_path.stat().st_size, 'first': primes[:8].tolist(),
                   'last': last.tolist(), 'used_records': 148933,
                   'used_last': 1999993, 'prefix_verified_by_sieve': True,
                   'all_records_strictly_increasing': True,
                   'sha256': sha256(prime_path)},
        'construction_input_allowlist': ['zLamb.bin', 'primoss.bin'],
        'no_true_zero_access_guard': True,
    }
    (output / 'input_audit.json').write_text(json.dumps(info, indent=2))
    return tau, primes[:148933].astype(np.int64)


def coefficients(primes, cutoff, window):
    freq, coeff = [], []
    for p in primes[primes <= cutoff]:
        q, m = int(p), 1
        while q <= cutoff:
            freq.append(m * np.log(float(p)))
            coeff.append(-1 / (np.pi * m * np.sqrt(float(q))))
            q, m = q * int(p), m + 1
    return np.array(freq), np.array(coeff)


def phase(t, primes, cutoff, window, block=65536):
    if window == 'euler_v10':
        ps = primes[primes <= cutoff].astype(float)
        f, c = np.log(ps), 1 / np.sqrt(ps)
    else:
        f, c = coefficients(primes, cutoff, window)
    result = np.zeros_like(t)
    for lo in range(0, len(t), block):
        hi = min(lo + block, len(t))
        x = t[lo:hi]
        s = np.zeros_like(x)
        for frequency, weight in zip(f, c):
            angle = frequency * x
            if window == 'euler_v10':
                s -= np.arctan2(weight * np.sin(angle), 1-weight*np.cos(angle)) / np.pi
            else:
                s += weight * np.sin(angle)
        result[lo:hi] = s
    return result


def effective_cutoffs(tau, cutoff, policy):
    if policy == 'constant':
        return np.full(len(tau), cutoff, dtype=float)
    # Dyadic lower block height, X(T)=min(Xmax,max(8,floor(T^.5))).
    # Xmax is the tunable ceiling; no ordinate correction or fitted zero is used.
    height = np.exp2(np.floor(np.log2(tau)))
    return np.minimum(cutoff, np.maximum(8, np.floor(np.sqrt(height))))


def advance(t, tau, index, primes, cutoff, window, policy):
    cut = effective_cutoffs(tau, cutoff, policy)
    s = np.zeros_like(t)
    for x in np.unique(cut):
        at = cut == x
        s[at] = phase(t[at], primes, float(x), window)
    # Retain the stored Lambert clock residual rather than assuming exact roots.
    base = clock(tau) - (index + .5)
    residual = base + clock_difference(t, tau) + s
    step = residual / slope(t)
    y = t - step
    diag = {
        'finite': bool(np.all(np.isfinite(y))),
        'domain_valid': bool(np.all(y > TWO_PI)),
        'max_abs_step': float(np.max(np.abs(step))),
        'max_step_in_local_spacings': float(np.max(np.abs(step * slope(tau)))),
        'large_step_count_2_spacings': int(np.sum(np.abs(step * slope(tau)) > 2)),
        'max_abs_displacement': float(np.max(np.abs(y - tau))),
        'cutoffs_actual': np.unique(cut).tolist(),
        'max_clock_residual': float(np.max(np.abs(base))),
    }
    return y, diag


def configs():
    out = []
    grid = [8, 32, 128, 512, 2048, 8192]
    for window in ['euler_v10', 'power_sharp']:
        for policy in ['constant', 'dyadic']:
            for x in grid:
                for steps in range(1, 4):
                    out.append({'window': window, 'policy': policy, 'cutoffs': [x]*steps})
            for x1, x2 in zip(grid[:-1], grid[1:]):
                out.append({'window': window, 'policy': policy, 'cutoffs': [x1, x2]})
                out.append({'window': window, 'policy': policy, 'cutoffs': [x1, x2, x2]})
    for i, c in enumerate(out):
        c['id'] = f'c{i:03d}'
    # Extend the original coarse sweep to every nondecreasing sequence of
    # length 2, 3 and 4 on the same preregistered grid. IDs stay stable.
    for window in ['euler_v10', 'power_sharp']:
        for policy in ['constant', 'dyadic']:
            for steps in [2, 3, 4]:
                for seq in combinations_with_replacement(grid, steps):
                    if not any(c['window']==window and c['policy']==policy and
                               c['cutoffs']==list(seq) for c in out):
                        out.append({'id':f'c{len(out):03d}', 'window':window,
                                    'policy':policy, 'cutoffs':list(seq)})
    return out


def run(args):
    sys.addaudithook(guard)
    output = Path(args.output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    tau, primes = load_inputs(Path(args.data_dir).resolve(), output)
    start = time.monotonic()
    if args.stage == 'pilot':
        # Only the first 40% can be used for pilot parameter tuning.
        index = np.unique(np.r_[np.arange(512), np.linspace(512, int(.4*len(tau))-1, 12000).astype(int)])
        parameters = configs()
        target = output / 'pilot'
    else:
        index = np.arange(len(tau))
        parameters = json.loads((output / 'shortlist.json').read_text())
        target = output / 'candidates'
    target.mkdir(exist_ok=True)
    t0 = tau[index]
    cache, manifests = {}, []
    manifest_path = output / (args.stage+'_manifest.json')
    existing = {}
    if manifest_path.exists():
        existing = {c['id']:c for c in json.loads(manifest_path.read_text())}
    for c in parameters:
        if c['id'] in existing:
            e=existing[c['id']]
            assert all(e[k]==c[k] for k in ['window','policy','cutoffs'])
            assert sha256(output/e['file'])==e['sha256']
            if args.stage=='pilot':
                a=np.load(output/e['file']); assert np.array_equal(a['index'],index)
                y=a['values']
            else:
                y=np.fromfile(output/e['file'],dtype='<f8')
            cache[(c['window'],c['policy'],tuple(c['cutoffs']))]=(y,e['diagnostics'][-1])
            manifests.append(e)
            continue
        t = t0
        diagnostics = []
        for j, cutoff in enumerate(c['cutoffs']):
            key = (c['window'], c['policy'], tuple(c['cutoffs'][:j+1]))
            if key not in cache:
                before = time.monotonic()
                y, diag = advance(t, t0, index, primes, cutoff, c['window'], c['policy'])
                diag['elapsed_seconds'] = time.monotonic() - before
                cache[key] = (y, diag)
            t, diag = cache[key]
            diagnostics.append(diag)
        dest = target / (c['id'] + ('.npz' if args.stage == 'pilot' else '.bin'))
        if dest.exists():
            # A completed checkpoint can precede its manifest write. Recover
            # only after independently recomputing and comparing every value.
            if args.stage == 'pilot':
                prior=np.load(dest)
                assert np.array_equal(prior['index'],index)
                assert np.array_equal(prior['values'],t)
            else:
                assert np.array_equal(np.fromfile(dest,dtype='<f8'),t)
        elif args.stage == 'pilot':
            np.savez_compressed(dest, index=index, values=t)
        else:
            np.asarray(t, dtype='<f8').tofile(dest)
        entry = {**c, 'file': str(dest.relative_to(output)), 'sha256': sha256(dest),
                 'records': len(t), 'diagnostics': diagnostics}
        if args.stage == 'full':
            entry['nonpositive_gaps'] = int(np.sum(np.diff(t) <= 0))
            entry['minimum_gap'] = float(np.min(np.diff(t)))
        manifests.append(entry)
        manifest_path.write_text(json.dumps(manifests, indent=2))
        print(c['id'], c['window'], c['policy'], c['cutoffs'],
              f'elapsed={time.monotonic()-start:.1f}s', flush=True)
    # Persist trailing resumed entries too, even when the last array was cached.
    manifest_path.write_text(json.dumps(manifests, indent=2))
    (output / (args.stage+'_complete.json')).write_text(json.dumps({
        'stage': args.stage, 'elapsed_seconds': time.monotonic()-start,
        'candidates': len(manifests), 'no_true_zero_access': True}, indent=2))


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--data-dir', required=True)
    p.add_argument('--output', required=True)
    p.add_argument('--stage', choices=['pilot', 'full'], required=True)
    run(p.parse_args())
