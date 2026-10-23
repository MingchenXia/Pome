#!/usr/bin/env python3
"""Exact arithmetic/symbolic checks of two *conditional* Pome audit computations.

Finite consistency tests only; not proofs of analytical semistability, Fredholm
theorems, or any whole section.
"""
from fractions import Fraction
from math import floor
import sympy as sp

cases = 0
witnesses = 0
for d in range(1, 8):
    for den in range(1, 14):
        for num in range(0, d * den + 1):
            c = Fraction(num, den)
            for k in range(1, 21):
                a = floor(k * c)
                ceiling = -floor(-k * c)
                assert ceiling - a in (0, 1)
                h0 = d * k - a + 1
                assert h0 >= 1
                assert Fraction(h0 - 1, k) >= d - c
                assert Fraction(h0 - 1, k) < d - c + Fraction(1, k)
                cases += 1
            if c.denominator > 1:
                k = next(k for k in range(1, c.denominator + 1)
                         if k * c - floor(k * c) >= Fraction(1, 2))
                assert floor(2 * k * c) == 2 * floor(k * c) + 1
                assert 2 * floor(k * c) < floor(2 * k * c)
                witnesses += 1
            for k in range(1, 10):
                for ell in range(1, 10):
                    carry = floor((k + ell) * c) - floor(k * c) - floor(ell * c)
                    assert carry in (0, 1)
                    cases += 1

# For flat C^d and w=1+lambda*|z|^2, test exact coarea/Green defect.
r, lam = sp.symbols("r lam", positive=True)
for n in range(2, 15, 2):
    I_over_v = r**n + lam * sp.Rational(n, n + 2) * r**(n + 2)
    defect = sp.simplify(r * sp.diff(I_over_v, r) - n * I_over_v)
    rhs = 2 * lam * sp.Rational(n, n + 2) * r**(n + 2)
    assert sp.simplify(defect - rhs) == 0

# M={(z,z^2)} in C^2: graph area π(t+2t²), sphere radius²=t+t².
t = sp.symbols("t", positive=True)
ratio = sp.cancel((t + 2*t**2) / (t + t**2))
assert ratio == (1 + 2*t) / (1 + t)
assert sp.simplify(sp.diff(ratio, t) - 1 / (1 + t)**2) == 0

print(f"PASS {cases} exact rational Hilbert/carry checks, "
      f"{witnesses} nonintegral witnesses, "
      "7 flat radial identities, and curved graph strictness")
