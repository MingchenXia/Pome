#!/usr/bin/env python3
"""Exact-rational check of the Newtonian shell Gram/finite-block identities.

This is an independent sanity check, not a mathematical proof or a Pome build.
"""
from fractions import Fraction
from itertools import product


def radius(j, p):
    assert j >= 2 and p >= 1
    return 1 - Fraction(1, j**p)


def pair(j, k, p):
    # Newton's theorem: I(sigma_r,sigma_s)=1/max(r,s).
    return 1 / max(radius(j, p), radius(k, p)) - 1


def delta(j, p):
    return 1 / radius(j, p) - 1


def test():
    checked = 0
    for p in (1, 2, 3, 5):
        for n, m in ((2, 3), (2, 7), (4, 8), (7, 13)):
            direct = sum(
                (pair(j, k, p)
                 for j, k in product(range(n, m + 1), repeat=2)),
                Fraction(0),
            )
            weighted = sum(
                ((2 * (j - n) + 1) * delta(j, p)
                 for j in range(n, m + 1)),
                Fraction(0),
            )
            assert direct == weighted, (p, n, m, direct, weighted)
            checked += 1
    print(f"{checked} exact rational Gram/block checks passed")


if __name__ == "__main__":
    test()
