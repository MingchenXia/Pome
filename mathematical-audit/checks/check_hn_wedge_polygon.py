#!/usr/bin/env python3
"""Exact combinatorial audit of HN exterior-power slope formulas.

This is a finite symbolic consistency test, NOT a proof of sheaf semistability.
"""
from itertools import combinations, combinations_with_replacement

cases = 0
for rank in range(1, 9):
    for tuple_nondec in combinations_with_replacement(range(-4, 5), rank):
        slopes = tuple(reversed(tuple_nondec))
        for q in range(1, rank + 1):
            values = [sum(slopes[i] for i in indices) for indices in combinations(range(rank), q)]
            assert max(values) == sum(slopes[:q])
            assert min(values) == sum(slopes[-q:])
            assert max(values) <= q * slopes[0]
            cases += 1
# On P^1, Λ²(O(2) ⊕ O(-1) ⊕ O(-3)) = O(1) ⊕ O(-1) ⊕ O(-4).
assert sorted([2 + (-1), 2 + (-3), (-1) + (-3)], reverse=True) == [1, -1, -4]
print(f"PASS {cases} exact integer (rank, q, slope-vector) identities and one split-bundle example")
