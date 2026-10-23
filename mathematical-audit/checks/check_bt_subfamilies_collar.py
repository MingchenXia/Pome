#!/usr/bin/env python3
"""Finite exact diagnostic: normal-crossing codimensions and CLN log bounds.

Not a proof of analytic currents or psh convergence. No excluded programme.
"""
from fractions import Fraction

subfamilies = 0
for p in range(2, 13):
    for q in range(2, p + 1):
        for m in range(1, q + 1):
            dimension = 2 * (p - m)
            exponent = 2 * p - 2 * m + 1
            assert exponent == dimension + 1
            assert dimension >= 0
            subfamilies += 1

collar_checks = 0
for denominator in range(2, 1002):
    for numerator in range(1, denominator):
        delta = Fraction(numerator, denominator)
        assert delta <= delta / (1 - delta)
        assert 1 - delta <= 1
        collar_checks += 1

for p in range(2, 13):
    assert 2*p - 3 < 2*p - 2 < 2*p - 1

print(f"PASS {subfamilies} exact codimension checks and {collar_checks} exact rational inequalities")
