#!/usr/bin/env python3
"""Exact rational sanity check for the radial shell flux formula.

This checks finitely many algebraic shell/bulk decompositions only.
It does NOT prove positivity, closedness, Bedford–Taylor convergence,
or upper semicontinuity of Lelong numbers.
"""
from fractions import Fraction

count = 0
for m in range(1, 8):  # m = n - p >= 1
    for denominator in range(2, 15):
        a = Fraction(1, denominator)  # squared shell radius r_j^2
        for x in [a / 2, a, a * 2, a * 3, Fraction(2), Fraction(3, 2)]:
            # The open ball excludes the shell exactly when x <= a.
            shell = a**m if x > a else Fraction(0)
            bulk = x**m - a**m if x > a else Fraction(0)
            ball_mass = shell + bulk
            assert ball_mass == (x**m if x > a else 0)
            normalized = ball_mass / (x**m)
            assert normalized == (1 if x > a else 0)
            # The closed ball includes its boundary shell; only x=a changes.
            closed_mass = ball_mass + (a**m if x == a else 0)
            assert closed_mass == (x**m if x >= a else 0)
            if x == a:
                assert closed_mass - ball_mass == a**m
            count += 1

print(f"PASS {count} exact rational radial shell / open-ball flux cases")
