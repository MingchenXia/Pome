"""Exact small arithmetic checks for POME-TOR-MIXED-SUPPORT-ATOMS-001.

For axis-parallel boxes K_j with side lengths a[j][i], the coefficient
of t_1 ... t_n in Vol(sum_j t_j K_j) is the permanent of (a[j][i]).
That coefficient equals the mass of the mixed n!-normalized Alexandrov
measure of the support functions. These arithmetic checks do not prove
that the measures are Dirac masses or validate the full Pome project.
"""
from fractions import Fraction
from itertools import permutations
from math import prod, factorial


def mixed_mass_box_coefficient(sides):
    n = len(sides)
    assert n >= 1 and all(len(row) == n for row in sides)
    a = [[Fraction(x) for x in row] for row in sides]
    return sum((prod(a[j][perm[j]] for j in range(n))
                for perm in permutations(range(n))), Fraction(0))


def diagonal_mass(sides):
    return factorial(len(sides)) * prod(Fraction(x) for x in sides)


if __name__ == "__main__":
    segments = ((1, 0), (0, 1))
    rectangles = ((2, 3), (5, 7))
    boxes3 = ((1, 2, 3), (2, 4, 5), (3, 5, 7))
    assert diagonal_mass(segments[0]) == diagonal_mass(segments[1]) == 0
    assert mixed_mass_box_coefficient(segments) == 1
    assert mixed_mass_box_coefficient(rectangles) == 29
    assert mixed_mass_box_coefficient(boxes3) == 177
    assert mixed_mass_box_coefficient(((1, 1), (1, 1))) == 2
    print("exact checks passed: orthogonal segments 1, rectangles 29, three boxes 177, unit squares 2")
