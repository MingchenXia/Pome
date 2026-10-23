#!/usr/bin/env python3
"""Finite exact arithmetic checks; not a proof of the analytic statements."""
from fractions import Fraction
from math import comb
from itertools import product

cases = 0
for n in range(1, 81):
    h = sum((Fraction(1, j) for j in range(1, n)), Fraction(0))
    alternating = sum((Fraction((-1) ** (k + 1) * comb(n - 1, k), k)
                       for k in range(1, n)), Fraction(0))
    assert alternating == h
    cases += 1

for N in range(1, 151):
    partial = sum((Fraction(k*k, 2**k) for k in range(1, N+1)), Fraction(0))
    assert partial == 6-Fraction(N*N+4*N+6, 2**N)
    assert sum((Fraction(k, 2**k) for k in range(1, N+1)), Fraction(0)) == 2-Fraction(N+2, 2**N)
    cases += 1

for n in range(2, 5):
    Q=2**(n+1)+1
    digit=[2*i for i in range(2**n)]
    for k in (1, 2, 3):
        prefix = [sum(d*Q**(k-j-1) for j,d in enumerate(seq))
                  for seq in product(digit, repeat=k)]
        assert len(prefix) == len(set(prefix))
        assert all(b-a >= 2 for a,b in zip(sorted(prefix), sorted(prefix)[1:]))
        cases += 1
print(f"PASS {cases} exact finite checks (not an analytic or formal proof)")
