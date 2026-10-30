# 2026-10-30: exact Haar-averaged lattice quadrature and one-generator algebraic grading

**Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (freshly fetched). **Starting audit branch:** `b9c4522b138371942d5e1510658d312ccd00dfc2`. These are two **low / verified conditional deductions**, not errors in printed theorems, corrections of previously logged findings, complete-section certifications, or deep upstream-proof repairs. All excluded approximation/regularization/Bergman/`L^2`/Ohsawa–Takegoshi/multiscale/positivity-loss proof programmes remain **deferred-by-user**; none was reviewed.

## 1. `POME-TORIC-HAAR-SHIFT-EXACT-001`: Haar averaging eliminates all finite-level shifted-grid bias

**Source anchoring.** Theorem **21.7.3**, source `foundations-of-pluripotential-theory:364BCD30`, permanent tag `831AEEB7084F`, at `docs/sections/convex-analysis-and-toric-potentials--lattice-points-and-volume/index.html`, blob `5d209b7f4d2156c19bc3fb300303405df6321230`, physical lines **58–90** (statement 58–65; translated half-open cells and proof 68–88). Corollary **21.7.4**, source `:D6B87DCB`, permanent tag `CF4226A5034F`, lines **94–105**, was checked for scope. Section-count interpretation in Theorem **21.9.5**, source `foundations-of-pluripotential-theory:BD98CC5B`, permanent tag `69D3D97E7701`, `docs/sections/convex-analysis-and-toric-potentials--fans-divisors-and-character-sections/index.html`, blob `7ad2e6dbdd0ce59e1bf08cd9cb3c046e8c87ff6c`, lines **139–167**, was used **only as context**, not recertified.

Fix a lattice `M ≅ Z^n` with covolume one, `n>=1`, its unit half-open fundamental cube `Q=[0,1)^n`, and an integer `k>=1`. For every compactly supported integrable function `h` on `M_R`, define for almost every shift `a∈Q`

```text
Q_k(a;h) = k^{-n} sum_{m in M} h((m+a)/k).
```

**Exact identity, with no limiting argument:**

```text
integral_Q Q_k(a;h) da = integral_{M_R} h(x) dx.        (A)
```

It is sufficient that `h` be integrable; compact support makes all pointwise sums finite for the continuous-weight compact-body applications below. For nonnegative `h`, Tonelli permits the extended-value formulation.

**Proof.** The measurable cells `m+Q` for `m∈Z^n` partition `R^n` up to boundaries. By Fubini, after the substitution `x=(m+a)/k`,

```text
integral_Q k^{-n} sum_m h((m+a)/k) da
 = sum_m integral_{(m+Q)/k} h(x) dx
 = integral_{R^n} h(x) dx.
```

The proof neither uses convexity nor incorrectly interchanges a mass limit with a grid limit. Applied to the exact thickening in Theorem 21.7.3, with `h=f*1_{K^(r_k/k)}`, formula (A) gives

```text
integral_Q [k^{-n} sum_{m in (kK)^(r_k) intersect (M+a)}
                         f(m/k)] da
   = integral_{K^(r_k/k)} f(x) dx.                     (B)
```

The notation on the left uses the shifted lattice point `m` itself; equivalently, write `m=l+a` and evaluate `f((l+a)/k)`. Thus the *only* averaging error relative to `integral_K f` is genuine geometric thickening; at `r_k=0` there is **exactly zero average error at every finite k**, even when `K` has empty interior. This does not assert zero deterministic error for any prescribed shift.

**Exact one-dimensional error law and optimal variance bound.** For `K=[0,alpha]`, `alpha>0`, `f=1`, `r_k=0`, set `k*alpha=q+u`, `q=floor(k*alpha)`, `0<=u<1`. For Haar-uniform `a∈[0,1)`, outside the null set of endpoint ties the normalized count `N_k(a)/k` is `(q+1)/k` with probability `u` and `q/k` with probability `1-u`. Therefore

```text
E[N_k/k] = alpha,
Var(N_k/k) = u(1-u)/k^2 <= 1/(4*k^2).               (C)
```

The constant `1/4` is attained whenever `u=1/2`. Conversely, for `K=[0,1]`, the **fixed** shift `a=0` counts `k+1` points and has error `1/k`, whereas almost every nonintegral shift counts exactly `k`. Thus exact averaged unbiasedness is a genuinely different assertion from the already recorded sharp *uniform deterministic* `O(k^{-1})` discrepancy.

The separately executed exact-rational `Fraction` check (script below) confirmed (C) for `(k,alpha)=(7,2/5),(1,1/2),(11,7/13),(9,5/3),(5,1)` and the exact expected value, yielding variances `4/1225,1/4,12/20449,0,0` respectively. This is an arithmetic crosscheck, **not** project testing or a substitute for the proof.

**Status, novelty and dependents.** Low / verified conditional deduction (in fact a self-contained measure-theoretic identity after fixing the lattice convention). Theorem 21.7.3 and Corollary 21.7.4 remain correct. Existing `POME-LATTICE-QUANT-UNIFORM-001`, `POME-CONVEX-ALLBODIES-LATTICE-RATE-001`, and `POME-LATTICE-MOVING-BODY-001` already cover worst-case deterministic discrepancy and/or changing bodies; **do not re-register them**. Optional *separate* corollary after §21.7.3: exact shift average and one-dimensional variance. No change to toric Hilbert dimensions is claimed: their lattice is fixed, not averaged over a random shift.

## 2. `POME-NA-ONE-GENERATOR-GRADING-001`: a single infinite-order multiplier forces the full grading

**Source anchoring.** Lemma **22.1.94**, source `sgpt:AB6FE74C`, permanent tag `76252E7717AC`; Equation **22.1.95**, source `sgpt:EC9FB89B`, permanent tag `6126C03E6587`; `docs/sections/non-archimedean-pluripotential-theory/index.html`, blob `8448d710690ebe1cc28040f9611d05c9d008a961`, physical lines **1402–1414**. The neighboring algebraization Lemma **22.1.96**, source `sgpt:0D0A3D2C`, tag `AF0C82DE24E9`, lines **1418–1430**, was checked only for its distinct GAGA dependency, which **remains an external input**. No higher analytic arguments of §22.1.97 onward were inspected.

**Strengthened precise hypotheses and conclusion.** Let `R` be any commutative Noetherian complex algebra (the printed finite-type condition suffices), `I⊂R[t]` an ideal, and choose a single `a∈C^*` **not a root of unity**. Write `sigma_a(f)(t)=f(at)`. The one-sided hypothesis

```text
sigma_a(I) subset I                                                   (D)
```

already implies that `I` is homogeneous, hence stable under **every** `sigma_b`, `b∈C^*`; furthermore

```text
J_d={r∈R: r*t^d∈I},   J_0 subset J_1 subset ...,
I=J_0 + J_1*t + ... + J_{m-1}*t^(m-1) + J_m*(t^m)                 (E)
```

for some `m`, where `J_m*(t^m)` denotes the ideal generated by `J_m t^m`. The unique full graded decomposition is `I=direct_sum_{d>=0}J_d t^d` as an `R`-module.

**Proof.** For `f(t)=sum_{i=0}^d r_i t^i∈I`, hypothesis (D) gives `sigma_a^j f∈I` for each `0<=j<=d`. Their coefficient matrix is `V_{ji}=(a^i)^j`. The nodes `a^0,...,a^d` are pairwise distinct because `a` has infinite multiplicative order, hence `det(V)=product_{i<l}(a^l-a^i) !=0`. Inverting the finite Vandermonde matrix over `C` expresses each monomial `r_i t^i` as a linear combination of these elements of `I`. Therefore `I` is graded without a closure, density, or inverse-invariance assumption. Multiplication by `R` shows each `J_d` is an ideal; multiplication by `t` shows `J_d⊂J_{d+1}`. Noetherianity of `R` implies stabilization, proving (E). Multiplication `t↦bt` preserves each homogeneous monomial, giving full `C^*`-stability.

**Sharp failure for finite order.** If `a` is a root of unity of order `q>=1`, take `R=C` and `I=(t^q-1)`. Then `sigma_a(I)=I`, yet `I` is not homogeneous: the two monomials of `t^q-1` cannot individually belong to `I` (in particular `1∉I`). Thus infinite multiplicative order is the exact universal single-generator threshold. Noetherianity is needed only for a **finite stabilized** presentation, not for homogeneous decomposition.

**Status, novelty and dependents.** Low / verified conditional deduction, no printed error. The older `POME-NA-GRADED-CANON-001` established uniqueness of the coefficient filtration **under the printed all-circle hypothesis**; the new result changes that hypothesis to **one non-torsion generator** and supplies its sharp converse, without repeating canonicalization as a new finding. Optional stand-alone strengthening of Lemma 22.1.94. It may streamline equivariance checks in the elementary algebraic part of the NA construction, but does **not** establish the analytic algebraization of §22.1.96 or eliminate its GAGA input.

## Coverage and limits

This session directly re-read the specified theorem/proofs in §§21.7 and 22.1.94, plus exact one-dimensional lattice models and the finite-order algebra counterexample. §21.9.5 was a context-only section-count check; §22.1.96 was a context-only statement/proof-dependency check. Prior sessions had sampled §§21.7 and 22.1.94, so **no entire newly certified section is claimed**, and these results address newly tested quantifiers, not whole-section coverage. The actual current matrix remains **25 chapters, 747 numbered table-of-contents sections, zero mathematically certified whole sections**. All previously confirmed errors, proof gaps, external inputs, duplicates, conditional repairs and **deferred-by-user** items retain their statuses. No Demailly approximation/regularization or dedicated Bergman/`L^2`/OT/multiscale/positivity-loss work, no main/source/registry/permanent-tag/website edits, no project build, no CI, no formal verification, no publication.
