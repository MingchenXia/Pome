#!/usr/bin/env python3
"""Exact-rational tests of *abstract* TV extremizers; not a Pome test suite."""
from fractions import Fraction as Q

# Symmetric tent: sigma = delta_0 - 2 delta_(1/2) + delta_1
# TV=4; integral of k = 1/4 = TV * osc^2 / 16.
assert Q(1, 4) == Q(4, 16)

# Asymmetric tents on [0,1] with upward slope 1 and peak at d.
# sigma=k'' consists of three atoms; TV = 2/(1-d).
for d in (Q(1, 2), Q(1, 4), Q(1, 10), Q(1, 100)):
    tv = Q(2) / (1 - d)
    left_mass = d * d / 2
    ratio = left_mass / (tv * d * d / 4)
    assert ratio == 1 - d
    print("d=", d, "TV=", tv, "endpoint ratio=", ratio)
print("all 5 exact identities passed")
