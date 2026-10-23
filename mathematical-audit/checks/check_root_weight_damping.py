#!/usr/bin/env python3
"""Exact scalar consistency checks for POME-NPP-WEIGHT-ROOTCAP-001.

These symbolic checks do not prove positivity of Bedford--Taylor products.
"""
from sympy import symbols, Rational, simplify, diff, exp

t=symbols('t',real=True)
checked=0
for n in range(1,8):
    for q in range(n+1,n+14):
        A=Rational(n,q-n)
        F=A*(1-t)**(1-Rational(q,n))
        g=(1-t)**(-Rational(q,n))
        assert simplify(diff(F,t)-g)==0
        assert simplify(diff(F,t,2)-Rational(q,n)*(1-t)**(-Rational(q,n)-1))==0
        assert simplify(F.subs(t,0)-A)==0
        assert simplify(g**n-(1-t)**(-q))==0
        checked+=1
for n in range(1,8):
    for p in range(1,13):
        a=Rational(p,n)
        F=exp(a*t)/a
        assert simplify(diff(F,t)-exp(a*t))==0
        assert simplify(diff(F,t,2)-a*exp(a*t))==0
        assert simplify(diff(F,t)**n-exp(p*t))==0
        checked+=1
print(f'PASS {checked} exact polynomial/exponential scalar composition identities; not a current-theoretic proof')
