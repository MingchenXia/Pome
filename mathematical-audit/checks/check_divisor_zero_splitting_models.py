#!/usr/bin/env python3
"""Independent small numerical consistency check, not a proof, of cusp W1 formulas."""
import cmath
import math

for m in (1, 2, 3, 5):
    for a in (1e-3, 1e-6):
        x_roots = [cmath.rect(a ** (1 / (2 * m)), 2 * math.pi * j / (2 * m))
                   for j in range(2 * m)]
        y_roots = [cmath.rect(a ** (1 / (3 * m)), 2 * math.pi * j / (3 * m))
                   for j in range(3 * m)]
        x_cost = sum(math.hypot(abs(t * t), abs(t ** 3)) for t in x_roots)
        y_cost = sum(math.hypot(abs(t * t), abs(t ** 3)) for t in y_roots)
        x_exact = 2 * m * a ** (1 / m) * math.sqrt(1 + a ** (1 / m))
        y_exact = 3 * m * a ** (2 / (3 * m)) * math.sqrt(1 + a ** (2 / (3 * m)))
        assert abs(x_cost - x_exact) < 1e-12
        assert abs(y_cost - y_exact) < 1e-12

print("Eight cusp parameter pairs, both zero families: checks passed.")
