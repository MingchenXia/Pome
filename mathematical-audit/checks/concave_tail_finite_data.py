#!/usr/bin/env python3
"""Reproduce only finite scalar inequalities for POME-NA-CONCAVE-TAIL-REPAIR-001.

No Pome build, analytic proof, formal verification, or external dependency.
"""
from random import Random


def repaired(taus, data):
    assert len(taus) == len(data) >= 2
    assert all(x > y for x, y in zip(taus, taus[1:]))
    levels = [data[0]]
    slopes = []
    for j in range(len(data) - 1):
        slope = max([0.0] + [
            (data[i] - levels[j]) / (taus[j] - taus[i])
            for i in range(j + 1, len(data))
        ])
        slopes.append(slope)
        levels.append(levels[-1] + (taus[j] - taus[j + 1]) * slope)
    return levels, slopes


def main():
    assert repaired([1, 0], [0, -1]) == ([0, 0], [0])
    rng = Random(20261029)
    for _ in range(10000):
        n = rng.randrange(1, 12)
        taus = sorted(rng.sample(range(-50, 100), n + 1), reverse=True)
        data = [rng.uniform(-10, 10) for _ in taus]
        levels, slopes = repaired(taus, data)
        assert all(levels[i] + 1e-9 >= data[i] for i in range(n + 1))
        assert all(slopes[i + 1] <= slopes[i] + 1e-9
                   for i in range(n - 1))
    print("PASS: counterexample and 10000 seeded finite-data inequalities")


if __name__ == "__main__":
    main()
