#!/usr/bin/env python3
"""Exact-rational selected checks for POME-TORIC-FS-MINOR-LOWER-001.
No third-party dependencies; not a formal proof or project test suite.
"""
from fractions import Fraction as F
from itertools import combinations

def det3(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
          - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
          + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))

def test_square(x, y):
    vals = [F(1), x, y, x*y]
    dx = [F(0), F(1), F(0), y]
    dy = [F(0), F(0), F(1), x]
    S = sum(t*t for t in vals)
    dot = lambda a,b: sum(u*v for u,v in zip(a,b))
    g11 = (S*dot(dx,dx) - dot(dx,vals)**2)/S**2
    g22 = (S*dot(dy,dy) - dot(dy,vals)**2)/S**2
    g12 = (S*dot(dx,dy) - dot(dx,vals)*dot(dy,vals))/S**2
    det = g11*g22 - g12*g12
    cols = [vals,dx,dy]
    minor_sum = sum(det3([[row[i] for i in I] for row in cols])**2
                    for I in combinations(range(4),3))
    assert det == minor_sum/S**3
    assert minor_sum == S  # For the exact unit square embedding.
    assert det == 1/((1+x*x)**2*(1+y*y)**2)
    assert det >= S**(-3)
    if x == 0 and y == 0:
        assert det == S**(-3)
    return det

for p in [(0,0),(F(1,3),F(2,5)),(1,2),(F(5,4),F(3,2))]:
    print(p, "det =", test_square(F(p[0]), F(p[1])))

# Finite endpoint coefficient for n=4 / m=3, and first singular
# derivative's logarithmic coefficient (derived analytically in report).
m, n, t = 3, 4, F(2,3)
assert F(n*(m-1)**2, m*(m-2)) == F(16,3)
assert -n*2*m*t**m == F(-64,9)
print("Four exact-rational square checks and two coefficient identities passed.")
