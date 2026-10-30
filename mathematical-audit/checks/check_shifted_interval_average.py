#!/usr/bin/env python3
"""Exact rational finite-shift interval-count check; independent of project tests."""
from fractions import Fraction as Q

def count_shifted_interval(k, alpha, a):
    """Count m in Z with 0 <= m+a <= k*alpha; requires 0<a<1."""
    assert k > 0 and alpha > 0 and 0 < a < 1
    top = k * alpha - a
    return max(0, top.numerator // top.denominator + 1)

def test_case(k, alpha):
    length = k * alpha
    q = length.numerator // length.denominator
    u = length - q
    assert (Q(q) + u) / k == alpha
    # Midpoints of a subdivision aligned with the rational jump location u.
    N = 2 * u.denominator * 17
    vals = [count_shifted_interval(k, alpha, Q(2*j+1, 2*N)) for j in range(N)]
    assert set(vals).issubset({q, q+1})
    assert Q(sum(vals), N*k) == alpha
    mean = Q(sum(vals), N)
    var = Q(sum((v-mean)**2 for v in vals), N*k*k)
    assert var == u*(1-u)/(k*k)
    return (k, str(alpha), str(var))

if __name__ == "__main__":
    for k, alpha in [(7,Q(2,5)), (1,Q(1,2)), (11,Q(7,13)), (9,Q(5,3)), (5,Q(1,1))]:
        print(test_case(k, alpha))
