#!/usr/bin/env python3
"""Exact rational calibration of the sharp pairwise Gauduchon AM-GM deficit.

This checks finitely many *flat torus* diagonal models only; the proof is
the all-dimensional arithmetic-geometric mean argument in the audit report.
No external libraries or project build steps are required.
"""
from fractions import Fraction

cases = 0
for n in range(2, 8):
    best = Fraction(1, n * (n - 1))
    for t in (2, 3, 5, 10, 100, 1000):
        # The normalized eigenvalues have product one and rational square roots.
        roots = [Fraction(t ** (n - 1))] + [Fraction(1, t)] * (n - 1)
        r = [x * x for x in roots]
        assert __import__("math").prod(r) == 1
        excess = sum(r, Fraction(0)) / n - 1
        anisotropy = sum(
            ((roots[i] - roots[j]) ** 2 for i in range(n) for j in range(i + 1, n)),
            Fraction(0),
        )
        assert excess >= best * anisotropy
        if n == 2:
            assert excess == best * anisotropy
        assert anisotropy > 0
        cases += 1
    # Compare to the limiting sharp coefficient without floating-point arithmetic.
    t = 10 ** 6
    roots = [Fraction(t ** (n - 1))] + [Fraction(1, t)] * (n - 1)
    r = [x * x for x in roots]
    excess = sum(r, Fraction(0)) / n - 1
    anisotropy = sum(
        ((roots[i] - roots[j]) ** 2 for i in range(n) for j in range(i + 1, n)),
        Fraction(0),
    )
    ratio = excess / anisotropy
    assert best <= ratio <= best + Fraction(1, 10000)
print(f"Exact pairwise deficit checks passed: {cases} finite torus samples and 6 sharp-limit samples.")
