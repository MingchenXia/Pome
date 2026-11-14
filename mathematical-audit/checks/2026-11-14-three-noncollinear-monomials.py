#!/usr/bin/env python3
"""Exact monomial and E_1 restricted-rank checks for three noncollinear P2 points.

No third-party modules, network, source repository or build involved.
"""
from math import comb


def monomials(d, r):
    return [(a, b, d-a-b) for a in range(d+1)
            for b in range(d-a+1) if max(a, b, d-a-b) <= d-r]


def dimension(d, r):
    if 3*r > 2*d:
        return 0
    extra = comb(2*r-d, 2) if 2*r-d >= 2 else 0
    return comb(d+2, 2) - 3*comb(r+1, 2) + 3*extra


def e1_rank(d, r):
    if 2*r <= d:
        return r+1
    if 3*r <= 2*d:
        return 2*d-3*r+1
    return 0


def main():
    pairs = 0
    for d in range(1, 36):
        for r in range(0, d+1):
            a = monomials(d, r)
            assert len(a) == dimension(d, r), (d, r, 'global')
            assert sum(1 for x, y, z in a if y+z == r) == e1_rank(d, r), (d, r, 'E1')
            pairs += 1
    print(f"PASS: {pairs} finite-degree pairs (d,r)")


if __name__ == "__main__":
    main()
