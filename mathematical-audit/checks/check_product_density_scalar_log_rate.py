#!/usr/bin/env python3
"""Numerical diagnostics ONLY: logarithmic truncation tail of Pome 15.30.

No Pome import, no network, no formal-proof claim. Log-domain bisection avoids
underflow/overflow for exponential thresholds. Run with Python 3 (stdlib).
"""
from math import exp, log, log1p


def flux_and_log_density(u: float, k: int, alpha: float):
    # u=-log(r), r=|z|^2. For large u, r underflows harmlessly to zero.
    r = exp(-u) if u < 700 else 0.0
    s = 1 + u + log1p(r)
    Q = (r + alpha * s ** (alpha - 1)) / (1 + r)
    B = r * (1 - alpha * s ** (alpha - 1)) + alpha * (1 - alpha) * s ** (alpha - 2)
    # q=(1+r)^(k+1)(Q/r)^(k-1)Q',
    # Q'=r^(-1)*B/(1+r)^2, so log q is finite as r -> 0.
    logq = (k - 1) * log1p(r) + k * u + (k - 1) * log(Q) + log(B)
    return Q, logq, log1p(r)


def truncation_deficit(log_t: float, k: int, alpha: float):
    lo, hi = 0.0, max(32.0, 2 * log_t + 64.0)
    if flux_and_log_density(lo, k, alpha)[1] > log_t:
        raise AssertionError("Threshold must be above the density at infinity")
    for _ in range(180):
        mid = (lo + hi) / 2
        if flux_and_log_density(mid, k, alpha)[1] < log_t:
            lo = mid
        else:
            hi = mid
    u = (lo + hi) / 2
    Q, actual_logq, logr1 = flux_and_log_density(u, k, alpha)
    # 1-int min(q,t) κ^k = int_(q>t)(q-t) κ^k.
    # = Q(r_t)^k - t*(r_t/(1+r_t))^k for sufficiently large t.
    deficit = Q ** k - exp(log_t - k * u - k * logr1)
    return deficit, u, actual_logq


def main():
    count = 0
    for k in (1, 2, 3):
        for alpha in (1 / 3, 1 / 2, 2 / 3):
            beta = k * (1 - alpha)
            theory = alpha ** k * k ** beta
            ratios = []
            for L in (256.0, 512.0, 1024.0):
                tail, u, logq = truncation_deficit(L, k, alpha)
                assert tail > 0
                assert abs(logq - L) < 1e-9
                ratio = L ** beta * tail / theory
                ratios.append(ratio)
                count += 1
            print(f"k={k}, alpha={alpha:.6f}, beta={beta:.6f}; ratios: "
                  + ", ".join(f"{x:.6f}" for x in ratios))
            assert abs(ratios[-1] - 1) < .085, (k, alpha, ratios)
            assert abs(ratios[-1] - 1) < abs(ratios[0] - 1), (k, alpha, ratios)
    print(f"PASS: {count} numerical large-log-threshold diagnostics; not proof.")


if __name__ == "__main__":
    main()
