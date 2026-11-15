"""Rational arithmetic checks for two successive toric blowups of P2.
This is not a Pome build or formal proof certification.
"""
from fractions import Fraction as Q

def area(v):
    return abs(sum(x*v[(i+1)%len(v)][1]-y*v[(i+1)%len(v)][0]
                   for i,(x,y) in enumerate(v))) / 2

def expected(a,b):
    assert 0 <= a and 0 <= b and a+b <= 1
    if b<=a:
        bad=[(Q(0),Q(0)),(a+b,Q(0)),(a-b,b),(Q(0),a)]
    else:
        bad=[(Q(0),Q(0)),(a+b,Q(0)),(Q(0),(a+b)/2)]
    v=1-2*area(bad)
    assert v == (1-a*a-b*b if b<=a else 1-(a+b)**2/2)
    return v

def sections(m,a,b):
    assert (m*a).denominator == (m*b).denominator == 1
    return sum(1 for i in range(m+1) for j in range(m+1-i)
               if i+j>=m*a and i+2*j>=m*(a+b))

def main():
    for a,b in [(Q(1,5),Q(2,5)),(Q(2,5),Q(1,5)),(Q(0),Q(1)),
                (Q(1),Q(0)),(Q(1,3),Q(1,3))]:
        v=expected(a,b)
        assert all(Q(2*sections(m,a,b),m*m)>=v for m in (30,60,90,120))
    for k in range(1,15):
        assert sections(10*k,Q(1,5),Q(2,5))==41*k*k+12*k+1
    a,b=Q(1,5),Q(2,5)
    assert expected(a,b)==Q(41,50)
    assert expected(a,b)-(1-a*a-b*b)==(b-a)**2/2
    print("exact polygon and 14 Ehrhart checks passed")

if __name__=="__main__":
    main()
