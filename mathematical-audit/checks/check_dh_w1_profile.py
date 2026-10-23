#!/usr/bin/env python3
"""Exact finite-atom DH profile / Wasserstein identity checks.

This checks only finite arithmetic, NOT geometric NA or positive-current results.
"""
from fractions import Fraction
from itertools import combinations_with_replacement

def distance(x, y):
    # equally weighted, sorted atomic laws: monotone quantile coupling
    n = len(x)
    return sum((abs(a-b) for a,b in zip(x,y)), Fraction(0))/n

def tail_integral(x,y):
    pts=sorted(set(x)|set(y))
    n=len(x)
    result=Fraction(0)
    for lo,hi in zip(pts,pts[1:]):
        diff=sum(b>=hi for b in y)-sum(a>=hi for a in x)
        result+=Fraction(abs(diff),n)*(hi-lo)
    return result

checked=0
for n in range(1,6):
    vectors=list(combinations_with_replacement(map(Fraction,range(-2,3)),n))
    for x in vectors:
        for y in vectors:
            assert tail_integral(x,y)==distance(x,y)
            if all(a<=b for a,b in zip(x,y)):
                assert distance(x,y)==sum((b-a for a,b in zip(x,y)), Fraction(0))/n
            checked+=1
print('PASS',checked,'exact finite-atom W1/profile cases, including unordered pairs')
