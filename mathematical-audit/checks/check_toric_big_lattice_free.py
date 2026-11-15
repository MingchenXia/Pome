#!/usr/bin/env python3
"""Exact small certificate for the §21.13 lattice-free big toric divisor model.
No external libraries or repository build are required.
"""
from fractions import Fraction as F

rays = [(1,0),(2,1),(1,1),(1,2),(0,1),(-1,0),(-2,-1),(-3,-2),(-1,-1),(-2,-3),(-1,-2),(0,-1)]
assert all(rays[i][0]*rays[(i+1)%len(rays)][1]-rays[i][1]*rays[(i+1)%len(rays)][0] == 1 for i in range(len(rays)))
vertices = [(F(1,3),F(1,3)), (F(1,2),F(1,4)), (F(2,5),F(2,5)), (F(1,4),F(1,2))]
a = {u: (0 if u in [(1,0),(0,1)] else -1 if u in [(2,1),(1,2)] else 2 if u in [(-3,-2),(-2,-3)] else 100) for u in rays}
def inside(p, k=1):
    return all(u[0]*p[0]+u[1]*p[1]+k*a[u] >= 0 for u in rays)
assert all(inside(p) for p in vertices)
area = abs(sum(vertices[i][0]*vertices[(i+1)%4][1] - vertices[(i+1)%4][0]*vertices[i][1] for i in range(4)))/2
assert area == F(1,60), area
for k, expected in [(1, []),(2, []),(3, [(1,1)])]:
    points = [(x,y) for x in range(3*k+1) for y in range(3*k+1) if inside((x,y),k)]
    assert points == expected, (k, points)
assert all((60*v[0]).denominator == 1 and (60*v[1]).denominator == 1 for v in vertices)
print("PASS: smooth fan, polygon area 1/60, k=1,2 no sections, k=3 one monomial, denominator 60")
