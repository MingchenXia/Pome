"""Finite exact-rational stress check for POME-MAGNETIC-MULTIPAIR-MIDPOINT-DEFECT-001.
The proof is in the linked report. No external packages or repository build are needed.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial

def scaled(b, E):
    """Return exact (4*pi)**n * r_b(E) for n=2 or n=3."""
    n = len(b)
    if E <= 0:
        return Q(0)
    nonzero = [x for x in b if x > 0]
    zeros = n - len(nonzero)
    result = Q(0)
    bounds = [range(int(E/x)//2+1) for x in nonzero]
    for levels in product(*bounds):
        remain = E - sum(((2*p+1)*x for p,x in zip(levels,nonzero)),Q(0))
        if remain > 0:
            result += remain**(zeros+1)/factorial(zeros+1)
    for x in nonzero:
        result *= 2*x
    return result

for n in (2,3):
    cases = [(Q(1,i+2),Q(1,j+3),Q(0))[:n]
             for i in range(3) for j in range(3)]
    cases += [(Q(1,i+2),)*n for i in range(3)]
    for b in cases:
        for E in (Q(1,4),Q(1),Q(7,3)):
            defect = scaled((Q(0),)*n,E)-scaled(b,E)
            bound = (2**(n-2))*E**(n-1)*sum(x*x for x in b)
            assert 0 <= defect <= bound, (n,b,E,defect,bound)

def ceil_fraction(x):
    return -((-x.numerator)//x.denominator)

for i in range(1,11):
    b=Q(1,i+1)
    for j in range(1,25):
        E=Q(j,7)
        x=E/(2*b)
        N=max(0,ceil_fraction(x-Q(1,2)))
        delta=Q(N)-x
        defect=scaled((Q(0),Q(0)),E)-scaled((b,Q(0)),E)
        # Exact report formula, multiplied by (4*pi)^2.
        expectation=b*b*E/6 + b**3*(delta-4*delta**3)/3
        assert defect == expectation, (b,E,defect,expectation)
print("PASS multipair rational bounds and 240 two-pair exact identities")
