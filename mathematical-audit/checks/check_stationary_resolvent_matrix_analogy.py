#!/usr/bin/env python3
"""Finite-state exact matrix sanity check; NOT a PDE proof.

Analog of the positive Markov resolvent, invariant adjoint probability,
and perturbation stability from POME-HERM-ADJOINT-C0-LP-LIPSCHITZ-001.
"""
import sympy as sp

h = sp.symbols('h', real=True)
L = sp.Matrix([[-2-h, 2+h, 0], [1, -4, 3], [4, 0, -4]])
assert L * sp.ones(3, 1) == sp.zeros(3, 1)
T = (sp.eye(3)-L).inv()
assert (T * sp.ones(3, 1)-sp.ones(3, 1)).applyfunc(sp.simplify) == sp.zeros(3, 1)

p0, p1, p2 = sp.symbols('p0 p1 p2')
sol = sp.solve(list((sp.Matrix([[p0, p1, p2]]) * L).tolist()[0]) + [p0+p1+p2-1], [p0,p1,p2], dict=True)
assert len(sol) == 1
pi = sp.Matrix([[sp.factor(sol[0][x]) for x in [p0,p1,p2]]])
assert sp.simplify(pi*L) == sp.zeros(1,3)
assert (pi*T-pi).applyfunc(sp.simplify) == sp.zeros(1,3)
for val in [sp.Rational(-3,4),sp.Rational(-1,2),sp.Rational(-1,10),sp.Rational(0),sp.Rational(1,10),sp.Rational(1,2),sp.Rational(3,4)]:
    pv = pi.subs(h,val)
    tv = T.subs(h,val)
    assert all(x >= 0 for x in list(pv))
    assert all(x >= 0 for x in list(tv))
    assert sum(pv) == 1
    assert pv*L.subs(h,val) == sp.zeros(1,3)
    if val:
        dist = sum(abs(x) for x in list(pv-pi.subs(h,0)))
        assert dist <= abs(val)  # finite analogue only, not the analytic constant
print('PASS 7 rational perturbations: positive resolvent, unique invariant row, normalized stability')
