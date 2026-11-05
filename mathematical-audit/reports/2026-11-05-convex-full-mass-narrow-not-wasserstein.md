# Exact weak-topology boundary for full-mass convex Monge–Ampère measures

**Audit date:** 2026-11-05. **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (unchanged). **New selected current-ToC target:** §21.6, *Compact convex envelopes and full-mass limits*, `docs/sections/convex-analysis-and-toric-potentials--compact-convex-envelopes-and-full-mass-limits/index.html` (main blob `b3b4e34fff767a717df812a381f905589b257fb3`, physical lines 5–45). **Statement locators:** Lemma 21.6.2, source `foundations-of-pluripotential-theory:55EDF0D7`, permanent tag `F2FABB0A312F`, lines 32–45; Lemma 21.6.1, source `foundations-of-pluripotential-theory:30FFD831`, permanent tag `FCDAD9CEC8CE`, lines 10–27. Crosschecks (NOT full theorem certifications): §21.4.1, `docs/sections/convex-analysis-and-toric-potentials--slope-bodies-and-bounded-growth/index.html`, blob `56a9a1c19e7234e2aa258d5ad1b66a5679ace190`, physical lines 11–26; §21.5.1–3, `docs/sections/convex-analysis-and-toric-potentials--the-real-monge-ampere-measure/index.html`, blob `7089aa41ae2422b1bd6b5094e46668cbc8ed37be`, lines 11–21, 44–48, 90–94. §21.5.1/2 permanent tags: `409656CC47D4`/`F4072D9ED060`.

## Finding POME-TORIC-FULLMASS-WASSERSTEIN-NONUPGRADE-001

**Severity low; status: verified conditional deduction, NOT a counterexample to the printed lemma.** Lemma 21.6.2 correctly improves vague convergence to narrow convergence when *both approximants and limit* have full mass. The following exact model proves that the conclusion cannot be strengthened to convergence of first moments or any Wasserstein `W_p` (`p>=1`), even when all potentials are in the **uniformly bounded** growth class and their defining Legendre-energy integrals converge.

Work in `N_R=M_R=R` with lattice `Z`, `P=[0,1]`, and support function `h_P(x)=x_+=max(0,x)`. Fix `c>0`. For `R>c`, set `eps_R=c/R`, `F=h_P`, and

```text
F_R(x) = (1-eps_R) max(0,x) + eps_R max(0,x-R).
```

These are finite convex functions, `F_R(0)=F(0)=0`, and

```text
F(x)-F_R(x) = eps_R * min(max(x,0),R) in [0,c].
```

In particular, `h_P-c <= F_R <= h_P` **with one constant c independent of R**, so all `F_R,F` lie in `E^infty(R,P) subset E^1(R,P) subset E(R,P)` under Definition 21.4.1. On every compact interval `[-A,A]`, `sup |F_R-F| <= c A/R -> 0`. Their effective conjugate domains are exactly `P` and their slope bodies are `P`, not a smaller interval.

The slopes of `F_R` are `0` for `x<0`, `1-eps_R` for `0<x<R`, and `1` for `x>R`. By the one-dimensional Alexandrov definition and `1!=1` normalization of Theorem 21.5.1, the measures are **exactly**

```text
MA_R(F_R) = (1-eps_R) delta_0 + eps_R delta_R,
MA_R(F) = delta_0.
```

Both masses equal `vol(P)=1`. For any bounded continuous `g`, the integral difference is `eps_R (g(R)-g(0)) -> 0`, as correctly predicted by Lemma 21.6.2. On the other hand, every coupling with `delta_0` must move the `eps_R` atom at `R` to zero, so for every real `p>=1`,

```text
W_p(MA_R(F_R),MA_R(F))^p = eps_R R^p = c R^(p-1).
```

Thus `W_1=c` **never tends to zero**, `W_p -> infinity` for every `p>1`, and the first absolute moment stays `c` rather than converging to `0`. In particular, uniform potential growth bounds, full mass, normalizations at the origin, and locally uniform convergence provide no uniform integrability of the first moment.

The Legendre transforms can also be evaluated *exactly*, without calling any convex duality theorem:

```text
F*(t) = 0                   for 0 <= t <= 1,
F_R*(t) = R max(0,t-1+eps_R) for 0 <= t <= 1,
F_R*(t) = +infinity         for t outside [0,1].
```

The values are attained at `x=0` or `x=R`; the resulting slopes `0,1-eps_R,1` prove no other maximizers occur. Therefore

```text
integral_P F_R*(t) dt = R eps_R^2/2 = c^2/(2R) -> 0
                         = integral_P F*(t) dt.
```

Even convergence of the **defining dual-energy integral** of `E^1` does not upgrade narrow to `W_1`. This is distinct from Example 21.5.3, where the limiting potential has **lost full mass** and only vague convergence survives. Here the limit retains full mass and narrow convergence holds. No printed theorem is false.

**Proposed addition (audit-only):** append a short caution after Lemma 21.6.2 that tightness controls bounded test functions, not moment tails. Any claim about `W_p`, unbounded tests or transport convergence must posit an additional uniform-integrability/tail-moment hypothesis. A uniform bound on `|F_j-h_P|` is insufficient. Potential dependents: attempts to strengthen §21.5.2/§21.6.2 or toric weak-convergence claims in §§21.12–21.13; no existing downstream theorem is classified as erroneous on this evidence.

## Finding POME-TORIC-VAGUE-MASS-NET-UPGRADE-001

**Severity low; status: verified conditional deduction (generalization of a correct sequence lemma).** The measure-theoretic first clause of Lemma 21.6.2 remains true for **arbitrary directed nets** of finite positive Radon measures `(mu_a)` on finite-dimensional `W`. Assume vague convergence `mu_a -> mu` on `C_c(W)` and convergence of total masses `mu_a(W) -> mu(W) < infinity`. For `h in C_b(W)` and `delta>0`, choose compact `K` with `mu(W\K)<delta`; take `eta in C_c(W)` with `0<=eta<=1`, `eta|_K=1`. By both net convergences,

```text
integral (1-eta) dmu_a -> integral (1-eta) dmu <= delta.
```

Splitting `h=h eta+h(1-eta)` gives

```text
limsup_a |integral h dmu_a - integral h dmu| <= 2 ||h||_infty delta.
```

Since `delta` is arbitrary, the net converges narrowly. No subsequence, metrizability of a measure space or sequential compactness is invoked. This recovers the sequential conclusion of the printed Lemma 21.6.2 and clarifies its exact topological scope; it does not independently certify the upstream real-MA vague continuity theorem for nets.

**Proposed optional addition:** a one-sentence net extension after the finite-measure lemma, with the above direct cutoff proof. Dependents: any extension of the real-MA continuity results from sequences to nets **only after** the corresponding net-wise vague convergence and mass hypotheses are separately verified.

## Other selected proof observations and boundaries

The actual Lemma 21.6.1 proof (lines 17–27) uses finite-dimensional compactness of a common effective-domain bound, merging barycentric terms of the same index, and lower semicontinuity of each `G_i` after subtracting a common lower bound. This is compatible with variable weights approaching zero: the nonnegative renormalized terms cannot cause an omitted negative contribution. No defect was identified in those selected steps. The equality `H=(max_i G_i^*)^*` still cites internal §21.3.2–3 and was **not** independently re-proved here.

All explicit model computations above are elementary and do not use any owner-deferred Demailly approximation/regularization, Bergman, weighted-L2, Ohsawa–Takegoshi, multiscale or positivity-loss completion programme. We performed **no** project build, tests, CI, formalization or publication. No original source, registry, permanent tag, production body or main branch was edited. This audit does **not** certify either §21.6 as a whole or the general §21.5 Alexandrov construction.
