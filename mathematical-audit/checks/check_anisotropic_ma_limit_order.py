#!/usr/bin/env python3
"""Finite exact-rational checks for the anisotropic smooth MA model.

This checks algebra only; it does not prove pluripotential results,
weak convergence or the total mass normalization.
"""
from fractions import Fraction


def outside(eps: Fraction, r: Fraction, m: int) -> Fraction:
    """Exact tail probability for one powered complex coordinate."""
    assert eps > 0 and r > 0 and m >= 1
    return eps / (eps + r ** (2 * m))


checks = 0
for m in range(1, 41):
    for r in (Fraction(1, 2), Fraction(1, 3), Fraction(2, 3)):
        eps = r ** (2 * m)
        assert outside(eps, r, m) == Fraction(1, 2)
        assert outside(eps, r / 2, m) >= Fraction(1, 1) - Fraction(1, 2 ** (2 * m))
        assert outside(eps, r * Fraction(3, 2), m) <= Fraction(2, 3) ** (2 * m)
        checks += 3

for m in range(1, 31):
    for eps in (Fraction(1, 9), Fraction(1, 3), Fraction(3, 2)):
        for r in (Fraction(1, 7), Fraction(1, 2), Fraction(3, 2)):
            # Integrating the derivative of r^(2m)/(eps+r^(2m))
            # from r to infinity yields eps/(eps+r^(2m)).
            x = r ** (2 * m)
            assert 1 - x / (eps + x) == outside(eps, r, m)
            checks += 1

print(f"PASS {checks} finite exact rational identities/inequalities")
