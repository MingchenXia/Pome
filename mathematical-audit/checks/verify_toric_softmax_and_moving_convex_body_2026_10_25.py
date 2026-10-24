#!/usr/bin/env python3
"""Finite arithmetic sanity checks for the 2026-10-25 toric audit; not proofs."""
from fractions import Fraction
from functools import reduce
from math import factorial, floor, sqrt

def determinant(matrix):
    a = [list(row) for row in matrix]
    ans = Fraction(1)
    for i in range(len(a)):
        pivot = next((j for j in range(i, len(a)) if a[j][i]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            ans = -ans
        p = a[i][i]
        ans *= p
        for j in range(i + 1, len(a)):
            q = a[j][i] / p
            for k in range(i, len(a)):
                a[j][k] -= q * a[i][k]
    return ans

for n in range(1, 9):
    raw = range(1, n + 1)
    total = sum(raw) + 5
    p = [Fraction(i, total) for i in raw]
    p0 = 1 - sum(p)
    covariance = [[(p[i] if i == j else Fraction(0)) - p[i]*p[j]
                   for j in range(n)] for i in range(n)]
    assert determinant(covariance) == p0*reduce(lambda a,b:a*b, p, Fraction(1))
    assert factorial(n) * Fraction(1, factorial(n)) == 1
print("Exact covariance determinants, dimensions 1..8: PASS")

for k in (100, 400, 1600):
    left = -1 + Fraction(1, k + 1)
    right = 1 - Fraction(1, k + 1)
    rad = floor(sqrt(k))
    a = Fraction(1, 3)
    count = sum(1 for z in range(-2*k, 2*k+1)
                if left - Fraction(rad, k) <= Fraction(z, k) + a/k
                <= right + Fraction(rad, k))
    approx = count/k
    assert abs(approx - 2) <= 2 * (1/(k+1) + rad/k + 2/k)
    print(f"Moving interval: k={k}, normalized count={approx:.6f}, target=2")
print("Grid sanity checks: PASS (not a proof or project build)")
