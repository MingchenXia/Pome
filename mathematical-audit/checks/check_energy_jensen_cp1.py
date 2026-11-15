#!/usr/bin/env python3
"""Small exact-rational P^1 normalization check for the new 2026-11-15 energy audit.
This is NOT a proof of the analytic energy second-variation identity or a project test.
"""
from fractions import Fraction as Q
from math import factorial


def beta_positive_integer(a: int, b: int) -> Q:
    return Q(factorial(a - 1) * factorial(b - 1), factorial(a + b - 1))


def energy(e: Q) -> Q:
    # E_omega(e f) for f=|z|^2/(1+|z|^2) and unit-mass Fubini-Study omega.
    return e / 2 - e * e / 12


def main() -> None:
    assert beta_positive_integer(2, 1) == Q(1, 2)  # integral of f omega
    assert beta_positive_integer(2, 2) == Q(1, 6)  # integral df wedge d^c f
    for e in (Q(1, 10), Q(1, 3), Q(1, 2), Q(9, 10)):
        gap = energy(e / 2) - (energy(Q(0)) + energy(e)) / 2
        assert gap == e * e / 48
        assert e / 2 - e * e / 6 <= energy(e) <= e / 2
        assert 1 - e > 0
    print("PASS: exact beta integrals, tangent bounds and P1 midpoint defects")


if __name__ == "__main__":
    main()
