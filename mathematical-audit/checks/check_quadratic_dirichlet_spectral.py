#!/usr/bin/env python3
"""Five exact rational checks of a quadratic ball-Dirichlet spectral formula.

Diagonal examples only: not a proof of the general theorem.
"""
from fractions import Fraction as Q


def minimum(diagonal):
    return min(diagonal)


def interpolation_defect(a, b, t):
    mixed = [(1 - t) * x + t * y for x, y in zip(a, b)]
    return minimum(mixed) - (1 - t) * minimum(a) - t * minimum(b)


cases = [
    ((Q(0), Q(1)), (Q(1), Q(0)), Q(1, 2), Q(1, 2)),
    ((Q(0), Q(2)), (Q(3), Q(0)), Q(2, 5), Q(6, 5)),
    ((Q(-2), Q(5)), (Q(1), Q(-3)), Q(1, 2), Q(2)),
    ((Q(1), Q(3)), (Q(2), Q(7)), Q(1, 3), Q(0)),
]
for a, b, t, expected in cases:
    found = interpolation_defect(a, b, t)
    assert found == expected, (a, b, t, found, expected)
    assert found >= 0

# The exact strict concavity gap at |z|^2 = 1/4 is 3/8.
assert interpolation_defect(
    (Q(0), Q(1)), (Q(1), Q(0)), Q(1, 2)
) * (Q(1) - Q(1, 4)) == Q(3, 8)
print(f"{len(cases) + 1} exact rational quadratic-boundary checks passed")
