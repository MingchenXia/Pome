"""Finite exact check of integral ordered/alternating Cech chain homotopy.

Python standard library only. This is not a proof, a Pome suite or a build.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product


def combine(*chains):
    out = defaultdict(int)
    for c in chains:
        for t, a in c.items():
            out[t] += a
    return {t: a for t, a in out.items() if a}


def scale(c, k):
    return {t: k*a for t, a in c.items() if k*a}


def boundary(c):
    out = defaultdict(int)
    for t, a in c.items():
        if len(t) == 1:
            continue  # Unaugmented C_{-1} = 0
        for j in range(len(t)):
            out[t[:j] + t[j+1:]] += (-1)**j * a
    return {t: a for t, a in out.items() if a}


def projection(c):
    out = defaultdict(int)
    for t, a in c.items():
        if len(set(t)) != len(t):
            continue
        inv = sum(t[i] > t[j] for i in range(len(t))
                  for j in range(i+1, len(t)))
        out[tuple(sorted(t))] += (-1)**inv * a
    return {t: a for t, a in out.items() if a}


def h_chain(c):
    return combine(*(scale(h(t), a) for t, a in c.items()))


@lru_cache(None)
def h(t):
    if len(t) <= 1:
        return {}
    e = combine({t: 1}, scale(projection({t: 1}), -1),
                scale(h_chain(boundary({t: 1})), -1))
    return {(min(t),) + u: a for u, a in e.items()}


B = [0]
for q in range(1, 6):
    B.append(2 + (q+1)*B[-1])

count = 0
max_l1 = {}
for n in range(1, 5):
    for q in range(6):
        for t in product(range(n), repeat=q+1):
            sigma = {t: 1}
            assert boundary(projection(sigma)) == projection(boundary(sigma))
            assert combine(boundary(h_chain(sigma)),
                           h_chain(boundary(sigma))) == \
                   combine(sigma, scale(projection(sigma), -1))
            magnitude = sum(abs(a) for a in h(t).values())
            assert magnitude <= B[q]
            max_l1[n, q] = max(max_l1.get((n, q), 0), magnitude)
            count += 1

assert sum(abs(a) for a in h((1, 0)).values()) == B[1] == 2
assert sum(abs(a) for a in h((2, 1, 0)).values()) == B[2] == 8
print("PASS", count, "tuples; B:", B)
print("Actual maxima at n=4:", [max_l1[4, q] for q in range(6)])
