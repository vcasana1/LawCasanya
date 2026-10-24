#!/usr/bin/env python3
"""Numerical checks for the damped centroid RH-equivalence section.

This script verifies the finite algebra used in the positive Laplace
defect and reproduces the sensitivity table for one hypothetical
off-critical pair.
"""
from __future__ import annotations

import math

GAMMA1 = 14.1347251417
DELTA = 0.05
Y_VALUES = [1.0, 0.5, 0.2, 0.1415, 0.1, 0.05]


def pair_defect(y: float, delta: float = DELTA, gamma: float = GAMMA1) -> float:
  """P_pair(y)=2(1-cos(y*delta))*exp(-y*gamma)."""
  return 2.0 * (1.0 - math.cos(y * delta)) * math.exp(-y * gamma)


def complete_pair(y: float, delta: float = DELTA, gamma: float = GAMMA1) -> complex:
  """Completed-zero pair at complex frequency omega=i y."""
  return (
    complex(math.cos(y * delta), math.sin(y * delta))
    + complex(math.cos(-y * delta), math.sin(-y * delta))
  ) * math.exp(-y * gamma)


def ordinate_pair(y: float, gamma: float = GAMMA1) -> float:
  """Ordinate-only pair at complex frequency omega=i y."""
  return 2.0 * math.exp(-y * gamma)


print("DAMPED CENTROID RH-EQUIVALENCE NUMERICAL CHECK")
print(f"gamma_1             = {GAMMA1:.13f}")
print(f"hypothetical delta       = {DELTA:.8f}")
print(f"universal logical range     = 0 < y <= {4*math.pi:.15f}")
print("")
print(" y    exp(-y gamma_1)    positive pair defect    direct difference")
for y in Y_VALUES:
  damp = math.exp(-y * GAMMA1)
  p = pair_defect(y)
  direct = ordinate_pair(y) - complete_pair(y).real
  print(f"{y:6.4f}  {damp: .12e}    {p: .12e}    {direct: .12e}")

print("")
y_opt = 2.0 / GAMMA1
print(f"quadratic-model optimum 2/gamma_1 = {y_opt:.15f}")
print(f"pair defect at y_opt       = {pair_defect(y_opt):.12e}")
print("")
# Universal injectivity check underlying the theorem: if |delta|<1/2 and
# 0<y<=4*pi, then |y*delta|<2*pi. Hence cos(y*delta)=1 forces delta=0.
# We print the endpoint bound to make the strict inequality explicit.
print("At y=4*pi and |delta|<1/2, one has |y*delta|<2*pi;")
print("therefore the only possible multiple of 2*pi is zero.")
