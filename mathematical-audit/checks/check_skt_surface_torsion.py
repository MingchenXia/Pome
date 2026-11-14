"""Exact 16x16 exterior-algebra check for complex-surface torsion a=3e1e2f1+4e1e2f2.
Only Python's standard library. A local check, not a formal proof of Bochner identities.
"""

def wedge_sign(left, right):
    if left & right:
        return 0
    swaps = sum(1 for i in range(4) if (left >> i) & 1
                for j in range(i) if (right >> j) & 1)
    return -1 if swaps % 2 else 1


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(16)) for j in range(16)]
            for i in range(16)]


A = [[0] * 16 for _ in range(16)]
for source in range(16):
    for factor, coefficient in ((0b0111, 3), (0b1011, 4)):
        sign = wedge_sign(factor, source)
        if sign:
            A[factor | source][source] += coefficient * sign
At = [list(row) for row in zip(*A)]
P = mul(A, At)
R = mul(At, A)
Q = [[P[i][j] + R[i][j] for j in range(16)] for i in range(16)]
assert mul(Q, Q) == [[25 * x for x in row] for row in Q]
assert sum(Q[i][i] for i in range(16)) == 100
expected = {(0, 0): 25, (0, 1): 25, (2, 1): 25, (2, 2): 25}
for p in range(3):
    for q in range(3):
        ids = [m for m in range(16) if (m & 3).bit_count() == p
               and ((m >> 2) & 3).bit_count() == q]
        trace = sum(Q[m][m] for m in ids)
        assert trace == expected.get((p, q), 0), (p, q, trace)
        assert all(Q[i][j] == 0 for i in ids
                   for j in range(16) if j not in ids)
print("PASS: Q^2=25Q; rank(Q)=4; bidegree traces exact")
