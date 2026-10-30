#!/usr/bin/env python3
"""Independent numerical check of the P1 ideal-envelope L1 formula; not a proof."""
from math import log, log1p

def entropy(c):
    if c in (0.0, 1.0):
        return 0.0
    return -c * log(c) - (1.0 - c) * log1p(-c)

def ideal_energy(c):
    if c == 1.0:
        return 1.0
    return c + (1.0 - c) * log1p(-c)

def midpoint_integral(c, n=100000):
    if c == 0.0:
        return 0.0
    h = c / n
    H = entropy(c)
    total = 0.0
    for k in range(n):
        t = (k + .5) * h
        p = H + c * log(t) + (1 - c) * log1p(-t)
        total -= p
    return total * h

def main():
    for c in (0.1, 0.5, 0.9, 0.99, 1.0):
        direct = midpoint_integral(c)
        closed = ideal_energy(c)
        assert abs(direct - closed) < 2.0e-5, (c, direct, closed)
        print(f"c={c:.2f} direct={direct:.11f} closed={closed:.11f} error={direct-closed:+.2e}")
    for delta in (.5, .1, .01, .001):
        gap = ideal_energy(1.0) - ideal_energy(1.0 - delta)
        target = delta * (1 - log(delta))
        assert abs(gap - target) < 1e-11
        print(f"delta={delta:g} exact endpoint gap={gap:.12g}")

if __name__ == "__main__":
    main()
