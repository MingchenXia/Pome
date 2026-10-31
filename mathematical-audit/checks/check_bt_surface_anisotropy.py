#!/usr/bin/env python3
"""Exact rational checks of the smooth complex-surface Minkowski defect.

No Pome build or external dependencies except SymPy are used.
"""
import sympy as sp

t, s = sp.symbols('t s', real=True)
cases = [
    (sp.diag(1, 4), sp.diag(4, 1), sp.Integer(9)),
    (sp.Matrix([[2, 1], [1, 2]]), sp.diag(3, 1), sp.Integer(2)),
    (sp.diag(1, 4), sp.diag(2, 8), sp.Integer(0)),
    (sp.eye(2), sp.diag(9, 1), sp.Integer(4)),
    (sp.Matrix([[3, sp.I], [-sp.I, 3]]), sp.Matrix([[2, 0], [0, 2]]), None),
]
for k, (A, B, expected) in enumerate(cases, start=1):
    det_a, det_b = sp.simplify(A.det()), sp.simplify(B.det())
    assert det_a > 0 and det_b > 0
    trace = sp.simplify(sp.trace(A.inv() * B))
    cross = sp.expand((t*A+s*B).det()).coeff(t).coeff(s)
    assert sp.simplify(cross-det_a*trace) == 0
    gap = sp.simplify(det_a*trace-2*sp.sqrt(det_a*det_b))
    assert gap.is_nonnegative
    assert sp.simplify((A+B).det()-(sp.sqrt(det_a)+sp.sqrt(det_b))**2-gap) == 0
    if expected is not None:
        assert sp.simplify(gap-expected) == 0
    print(f'case {k}: det A={det_a}, det B={det_b}, gap(s=t=1)={gap}')
print('All five exact-algebra checks passed.')
