# A single natural-boundary function for max-type Hartogs radii

**Date:** 2026-11-10. **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Stable finding ID:** `POME-HARTOGS-MAX-BRANCH-LACUNARY-EXISTENCE-001`. **Severity:** low. **Status:** verified conditional deduction (an independently complete explicit model; no refutation of the printed statement, and no certification of its general proof).

## Exact integrated source and audited scope

- Integrated continuous reading edition: `docs/sections/complete-hartogs-domains-and-taylor-coefficients/index.html`, Git blob `641a66c419e4a1f7207cd301b51f27f3a6efd6f9` on the main commit above.
- Section **9.15**, source `klimek-pluripotential-theory:1253F321`, permanent tag `F6F3F90BB780`, physical line 5.
- **Proposition 9.15.1**, source `klimek-pluripotential-theory:7CA9E7D7`, permanent tag `202C805DC8A2`: complete-Hartogs assumptions and coefficient/radius identity, **physical lines 7–16**; its integrated proof of coefficient normal convergence and the upper-semicontinuous limsup, **lines 21–27**.
- The hypotheses in the printed proposition are `n>=2`, an open base `D`, a lower-semicontinuous radius `R:D→(0,+infinity]`, and `H={(z,w): z in D, |w|<R(z)}`. The exact coefficient conclusion `u=(limsup_{j→infinity} j^{-1}log|c_j|)^*` additionally assumes that **H is a domain of existence of the particular f**. This distinction is preserved.

## Explicit max-of-two-branches model

Let `d>=1` and let `P∈C[z_1,...,z_d]` be a **nonconstant** polynomial (the concrete two-dimensional instance is `d=1,P(z)=z`). Put
[
 u_P(z)=max{0,log|P(z)|},quad
 R_P(z)=min{1,|P(z)|^{-1}},quad
 H_P={(z,w)inmathbf C^d	imesmathbf C:|w|<1, |P(z)w|<1}.
]
Interpret `|P|^{-1}=+infinity` at a zero of `P`. Then `R_P=e^{-u_P}` is strictly positive and continuous. The finite-valued continuous PSH function `u_P` is the maximum of the PSH functions `0` and `log|P|`; near zeros, the maximum equals zero, so no pole survives.

Pseudoconvexity is checked **without using Proposition 9.15.1**: the smooth function
[
 Phi(z,w)=|z|^2+|w|^2-log(1-|w|^2)-log(1-|P(z)w|^2)
]
is strictly PSH on `H_P`. For each holomorphic `g`, the function `-log(1-|g|^2)` is PSH on `|g|<1`, by direct `i∂∂bar` computation, and the Euclidean term is strictly PSH. The exhaustion is proper: any sequence leaving compact subsets either has unbounded Euclidean norm or approaches a finite boundary point with `|w|=1` or `|P(z)w|=1`, forcing one logarithmic term to diverge to `+infinity`. Thus `H_P` is a smooth strictly-PSH-exhausted complete Hartogs domain.

Define the lacunary disk function and its **single** holomorphic Hartogs function by
[
 F(t)=sum_{k=0}^{infty}t^{2^k},qquad
 f_P(z,w)=F(w)+F(P(z)w).
]
On compact subsets of `H_P`, both `|w|` and `|Pw|` have a common strict upper bound below one. Both series converge uniformly absolutely; hence `f_P∈O(H_P)`. Its exact Taylor coefficients in the fiber variable are
[
 c_j(z)=
 egin{cases}1+P(z)^{2^k},&j=2^k, kge0,\
 0,&j
otin{2^k:kge0}.
 end{cases}
]
In particular `c_0=0`, and logarithms of zero coefficients below are `-infinity`.

## Pointwise coefficient identity, including the switching set

Write `p=P(z)`. If `|p|<1`, then `1+p^{2^k}→1`, so `2^{-k}log|1+p^{2^k}|→0`. If `|p|>1`, factor
[
 1+p^{2^k}=p^{2^k}(1+p^{-2^k}),
]
and obtain `2^{-k}log|c_{2^k}(z)|→log|p|`. These include `p=0` in the first case.

At the **nontrivial switching set** `|p|=1`, the upper bound `|1+p^{2^k}|≤2` gives a limsup at most zero. For any unit complex number `t`,
[
  max{|1+t|, |1+t^2|}ge1.
]
Indeed, if `|1+t|<1`, then `Re(t)<-1/2`, so `|1+t^2|=2|Re(t)|>1`. Applied to `t=p^{2^k}`, this shows that in each adjacent pair of lacunary coefficients at least one has modulus at least one. Hence arbitrarily large coefficient indices have normalized logarithm at least zero, giving the reverse limsup bound. Thus at **every base point**, including all zeros and all `|P|=1`,
[
 oxed{limsup_{j	oinfty}rac1jlog|c_j(z)|
    =max{0,log|P(z)|}=u_P(z).}
]
The raw limsup is already continuous, hence equals its upper-semicontinuous regularization here. This does **not** assert that such regularization can be omitted in the general printed proposition.

## Domain of existence: all boundary faces, including corners

First, `F` has no holomorphic continuation across any point of the unit circle, by an elementary argument (no gap theorem). If `zeta^{2^N}=1`, then
[
 F(rzeta)=sum_{k<N}r^{2^k}zeta^{2^k}
                   +sum_{kge N}r^{2^k},quad 0<r<1.
]
The finite sum stays bounded and the second tends to `+infinity`: for any integer `M`, its first `M` terms tend to one as `r↑1`. Thus `F(rzeta)` is unbounded near each dyadic root of unity. Such roots are dense on the unit circle, so no local continuation is possible at any unit-circle point.

For the **mixed Hartogs boundary**, all finite boundary points satisfy `|w|≤1`, `|Pw|≤1`, with at least one equality:

1. If `|P(z_0)|<1`, necessarily `|w_0|=1`. Choose dyadic roots `zeta_ell→w_0`; the nearby boundary points `(z_0,zeta_ell)` have radial interior approaches `(z_0,rzeta_ell)`. On each approach `F(w)→+infinity` up to a bounded finite initial sum, whereas `F(P(z_0)w)` remains uniformly bounded because `|P(z_0)|<1`. Thus `f_P` has no local holomorphic continuation there, nor at `(z_0,w_0)`.
2. If `|P(z_0)|>1`, necessarily `|P(z_0)w_0|=1` and `|w_0|<1`. Choose dyadic roots `eta_ell→P(z_0)w_0`, and radial interior paths `w=reta_ell/P(z_0)`. Now `F(P(z_0)w)` is unbounded, while `F(w)` is uniformly bounded by `|w|≤|P(z_0)|^{-1}<1`. Again no local extension exists.
3. If `|P(z_0)|=1`, both boundary constraints are active and `|w_0|=1`. Nonconstant holomorphic `P` cannot have `|P|≥1` on a full neighborhood of `z_0`: there `1/P` would attain a local maximum of modulus one, forcing `P` locally, hence globally, constant by the maximum-modulus principle. Thus `z_ell→z_0` with `|P(z_ell)|<1`. Choose dyadic `zeta_ell→w_0`. The first-face singular boundary points `(z_ell,zeta_ell)` approach the corner; any putative holomorphic continuation across that corner would also continue across one of these points, a contradiction.

There are no other finite boundary points, since the base is all of `mathbf C^d`. Consequently **`H_P` is the domain of existence of `f_P`**, not merely a domain of convergence for its series. The example simultaneously verifies maximality, the exact radius, and the pointwise coefficient identity for a maximum of two competing PSH branches.

## Classification, independent scope, proposed optional patch

**Status:** verified conditional deduction, low severity. The explicit construction and all three boundary cases above are fully proved independently. The printed Proposition 9.15.1 is **not** false and **no** deficiency in its stated proof is established. A general `D`, an arbitrary PSH radius, Oka's theorem/domain-of-holomorphy existence, and the unrestricted PSH Hartogs lemma are **not** certified by this case. The section's proof depends on these separate general inputs; retain them as unreviewed, not as resolved.

This model is **genuinely different** from the earlier `POME-HARTOGS-RATIONAL-LOG-NATURAL-BOUNDARY-001`, which concerns `u=(p/q)log|z|`, a monomial singular weight and an unbounded polar fiber. Here `u_P=max(0,log|P|)` is **continuous**, has a nonempty **switching locus** and two boundary faces meeting at corners, and one explicitly controlled function has no continuation on either face. It also resolves the specific illustrative shortcoming noted by `POME-HARTOGS-EQUALITY-WITHOUT-EXISTENCE-001`: the **same domain** `H={|w|<1,|zw|<1}` previously supported a rational `f` with correct growth but many continuations, while the new lacunary `f` simultaneously has the correct growth **and** `H` as its domain of existence. The earlier findings retain their separate tags and statuses.

**Suggested review-only correction/addition:** an optional example after Proposition 9.15.1 with `P(z)=z` (or a nonconstant polynomial `P`), `f_P=F(w)+F(Pw)`, the exact coefficients and three boundary cases. No change to the canonical statement, historical attribution, source, registry, or permanent tags is warranted. Affected dependents: the explicit domain-of-existence and Taylor-coefficient clauses of §9.15.1; related complete-Hartogs/Reinhardt examples are only potential downstream users, **not** newly audited results.

**Actual coverage:** new, selected explicit model and direct integrated-reading verification of §9.15.1 lines 7–16 and proof lines 21–27. This numbered section had already been partly sampled in other checkpoints: **0 first-visited sections, 0 fully certified sections**. The main ToC remains **25 chapters / 747 numbered sections**, with no entire chapter certified. No arithmetic tests, project tests, builds, formal verification, CI, or website publication were run. Owner-excluded Demailly regularization, Bergman/L²/OT, multiscale and positivity-loss proof tasks remain **deferred-by-user**, neither resumed nor certified.
