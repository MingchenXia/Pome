# Weighted shrinking-sphere measures: all Hölder exponents and Lipschitz references (2026-11-09)

**Finding ID:** `POME-SPHERE-WEIGHT-HOLDER-LIPSCHITZ-001`  
**Classification:** low / **verified conditional deduction**. The printed Proposition 15.26.2, Corollary 15.26.3, and Theorem 15.26.4 are not refuted. No complete upstream theorem chain or section is certified.

## Exact source and scope

Reviewed production `main`: `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Integrated reading-edition file: `docs/sections/equations-with-prescribed-singularities--singular-measures-on-shrinking-spheres/index.html`, blob `354dfdf5224fac8896103ec09aa5936351021914`. Equation 15.26.1: source `non-kahler-pluripotential-theory:4C0F3404`, permanent tag `938F2C76C18A`, physical lines 12–15. Proposition 15.26.2: source `non-kahler-pluripotential-theory:92442012`, permanent `8F3C95237950`, lines 26–67 (construction, positivity, Hölder regularity, and top mass). Corollary 15.26.3: `non-kahler-pluripotential-theory:BBB972F3` / `AB5B44EC4BDD`, lines 69–82. Theorem 15.26.4: `non-kahler-pluripotential-theory:7EBE40DC` / `6076D6F3256C`, lines 84–102. The local normalization `(dd^c log max{|z|²,r²})^n=σ_r` is Lemma 5.27.25, `non-kahler-pluripotential-theory:961DE4FB` / `3242D4BA1F13`; `docs/tag/3242D4BA1F13/index.html`, blob `a813ea6fc584d16922bae4f8a3efbf107d41c0a0`. Only this lemma's stated identity was used; its whole dependency chain was not re-audited.

The printed choice is the single exponent `s=1/2`. The following result is **an additional sharp-weight family**, not a claim that the printed choice is wrong.

## Proposition (weight/regularity family)

Let `X` be a compact complex manifold of dimension `n≥2`, `h>0` any smooth Hermitian metric, and use **the same fixed chart, inner ball, cutoff** `χ` and geometric radii `r_j=r_0 2^{-j}` of §15.26. Fix an arbitrary real `s>0`. Denote the normalized Euclidean spherical measures by `σ_j` and set

```text
S_s = sum_{j>=1} r_j^(ns),     Z_s = 2K sum_{j>=1} r_j^s,
d_j(s) = r_j^s/Z_s,           rho_s = S_s^(-1) sum_{j>=1} r_j^(ns) sigma_j.
psi_j = chi log max{|z|^2,r_j^2} + (1-chi), extended as 1 off the chart,
u_s = sum_{j>=1} d_j(s) psi_j - sup_X sum_{j>=1} d_j(s) psi_j.
```

Here `K≥1` is the *same uniform* lower-Hessian constant used in §15.26, chosen independent of `s,j`. Then `rho_s` is a singular non-pluripolar probability measure and

```text
u_s in PSH(X,h), sup_X u_s=0,
h+dd^c u_s >= h/2,
MA_h(u_s) >= (S_s/Z_s^n) rho_s,
0 < MA_h(u_s)(X) < infinity.
```

For `0<s<1`, `u_s` is globally `C^{0,s}` and is **not** `C^{0,t}` at the chart center for **any** `t>s`. For every `s≥1`, `u_s` is globally **Lipschitz**, including the endpoint `s=1`. For **every** `s>0`, this specific `u_s` is **not `C^1` across any of the prescribed spheres**, although for `s>1` it is differentiable at their accumulation center with zero derivative.

Thus even an arbitrary Hermitian background, with no positive lower total-mass assumption, admits a **Lipschitz strictly admissible reference** whose Monge–Ampère measure dominates a *fixed singular probability supported on countably many shrinking spheres*. For each fixed `s>0`, the solvability consequences of §§15.26.3–4 apply to bounded densities with respect to `rho_s` under their already printed internal hypotheses; this report does not re-prove those existence theorems.

## Proof

**Uniform convergence and positivity.** On the compact coordinate ball, `||psi_j||_infty <= C(1+|log r_j|)`; since `sum r_j^s(1+j)<infinity` for every `s>0`, the defining series converges uniformly, and its constant normalization is harmless. The metric-derivative error on the cutoff annulus is identical for every `j`, where `r_j` is below that annulus. Thus `dd^c psi_j>=-Kh` with one `K`, and `sum d_j=1/(2K)`. Partial sums consequently satisfy `h+dd^c sum_{j<=N}d_j psi_j >=h/2`; the same holds in the current sense for the limit.

On the inner ball (`χ=1`), `dd^c psi_j` are positive closed currents. First take finite sums and use positivity of all terms in the top-degree expansion of `(h+sum d_j dd^c psi_j)^n`. Its diagonal term for index `j` is `d_j^n (dd^c psi_j)^n=d_j^n σ_j` by the exact normalization of Lemma 5.27.25. For each fixed finite set of `j` retain these terms, then pass to the uniform bounded-potential limit using the product continuity established in the printed construction. Increase the finite set only *after* this limit. One gets the Radon measure inequality `MA_h(u_s)>=sum_{j>=1} d_j^n σ_j=(S_s/Z_s^n)rho_s`. Local mass bounds from the same bounded-product theory give finiteness; positivity follows from the strictly positive displayed lower bound. Every `σ_j` is non-pluripolar by Lemma 5.27.25 and their countable weighted sum is non-pluripolar. The countable union of real spheres has zero ambient smooth volume, making `rho_s` singular.

**Exact radial derivative (stronger than a term-by-term logarithmic modulus estimate).** On the inner ball put `R=|z|` and ignore the global additive constant. The function is radial and, at every `R>0` not equal to a radius `r_j`, its ordinary derivative is

```text
u_s'(R) = (2/(Z_s R)) sum_{r_j<R} r_j^s.
```

The derivative formula is legitimate on each annulus separated from the discrete set of positive radii: the terms with smaller radii have an absolutely summable coefficient series and all share derivative `2/R`. For geometric radii, `sum_{r_j<R} r_j^s <= C_s R^s` (with a constant depending on `r_0,s`); hence `|u_s'(R)|<=C'_s R^{s-1}`. Integrating on radial segments gives for `0<s<1`

```text
|u_s(R)-u_s(T)| <= C_s |R^s-T^s| <= C_s |R-T|^s.
```

For `s≥1`, the same derivative bound is uniformly finite on the inner ball, giving Lipschitz regularity **also at s=1**. Because `||z|-|w||<=|z-w|`, the radial estimates are Euclidean. The cutoff annulus and the complement are represented by the same fixed smooth function for every `j`; a compact finite cover transfers the local bound globally.

**Sharpness at the center and failure of C¹ on the spheres.** At `R=r_N`, exactly the terms `j>N` change from their value at zero. Thus there is the **exact identity**

```text
u_s(r_N)-u_s(0)
 = (2/Z_s) sum_{j>N}r_j^s log(r_N/r_j)
 = (2 log 2/Z_s) [ 2^(-s)/(1-2^(-s))^2 ] r_N^s > 0.
```

For `0<s<1`, division by `r_N^t` diverges for any `t>s`, so no higher Hölder exponent can hold even locally at the center. When `s>1`, the derivative bound tends to zero as `R↓0`, giving differentiability at the center. At a fixed sphere `R=r_j`, the radial derivative on crossing the sphere jumps by exactly `2d_j(s)/r_j>0`; all terms with other radii are smooth in a neighborhood of that sphere. Therefore this concrete potential is never `C^1` across a supporting sphere, even when it is Lipschitz. No claim is made that all admissible potentials dominating `rho_s` fail to be `C^1`.

## Classification and limits

The proven *new* assertions are the `s>0` family, sharp subunit Hölder exponent, the **Lipschitz endpoint**, and the non-`C^1` jump. They are conditional on the independently printed bounded-potential Monge–Ampère continuity and Lemma 5.27.25 for the measure inequality; the radial regularity calculation itself is elementary and complete. **No false printed statement** and **no identified gap in §15.26.2**. Low severity, `verified conditional deduction`. Proposed action: an optional remark after Proposition 15.26.2 stating the general weights and Lipschitz example, retaining all existing labels, attribution, and source versions. No production or canonicalization changes in this audit.

Affected dependents: Corollary 15.26.3 and Theorem 15.26.4 accept each `rho_s` with the same bounded-density hypotheses and their existing internal existence results; no global solvability theorem is independently certified. Excluded Demailly regularization and its Bergman/L²/OT/multiscale/positivity-loss proof programme were not examined.

**Coverage:** new selected proof computation in already previously visited §15.26; normalization lemma §5.27.25 crosschecked only. `0` newly first visited numbered sections; `0` complete mathematical-section certifications. Directory inventory not rewritten: prior actual ToC has 25 chapters and 747 numbered sections. No build, test suite, CI, website publication, or formalization ran.
