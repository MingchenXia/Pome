#!/usr/bin/env python3
"""Finite exact flag-semigroup check for the independent audit note; no third-party deps."""
from itertools import product

def check(m: int, b: int) -> None:
    assert 0 <= b < m
    observed = set()
    for a in range(m + 1):
        for k in range(m - a + 1):
            ell = m - a - k
            if a + k >= b:
                observed.add((k, ell))
    predicted = {(k, ell) for k in range(m + 1)
                 for ell in range(m - max(k, b) + 1)}
    assert observed == predicted, (m, b, observed ^ predicted)
    print(f'm={m} b={b} pairs={len(observed)}')

if __name__ == '__main__':
    for m, b in [(5, 0), (5, 2), (8, 3), (12, 9)]:
        check(m, b)
