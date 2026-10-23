#!/usr/bin/env python3
"""Exact rational checks for the higher C^r anisotropic MA density parameters.

Only finite arithmetic is checked: no PDE, C^r regularity, or MA products.
"""
from fractions import Fraction

checked = 0
for n in range(3, 13):
    N = 2 * (n - 1)
    for r in range(3, N):
        alpha = Fraction(2 * N, N - r)
        beta = (r * alpha + N * (alpha - 1)) / 2
        exponent = (2 * alpha + N + beta) / (n * alpha)
        assert beta > r * alpha, (n, r)
        assert beta < N * (alpha - 1), (n, r)
        assert exponent < 2, (n, r)
        if n == 3 and r == 3:
            assert (alpha, beta, exponent) == (Fraction(8), Fraction(26), Fraction(23, 12))
        checked += 1
assert checked == 100
print(f"PASS: {checked} exact rational parameter cases")
