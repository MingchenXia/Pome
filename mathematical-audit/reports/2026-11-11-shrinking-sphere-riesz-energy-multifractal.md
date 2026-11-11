# 2026-11-11 — exact Riesz-energy threshold for the singular shrinking-sphere probability in §15.26

## Revision, source anchors, and scope

Reviewed production `main` **`b6933b772f41b45918f7e25ed1afbbb1fd892272`**, not the audit branch's mathematical body. Directly examined the integrated reading edition
`docs/sections/equations-with-prescribed-singularities--singular-measures-on-shrinking-spheres/index.html`, Git blob **`354dfdf5224fac8896103ec09aa5936351021914`**:

- Equation **15.26.1**, original source `non-kahler-pluripotential-theory:4C0F3404`, permanent tag `938F2C76C18A`, physical lines **10–23**: the fixed geometric radii, normalized sphere probabilities, and their weights.
- Proposition **15.26.2**, original source `non-kahler-pluripotential-theory:92442012`, permanent tag `8F3C95237950`, physical lines **27–65**: singular non-pluripolar probability and its bounded Hölder Monge–Ampère dominating potential.
- Corollary **15.26.3**, original `:BBB972F3`, permanent `AB5B44EC4BDD`, physical lines **70–81**; Theorem **15.26.4**, original `:7EBE40DC`, permanent `6076D6F3256C`, physical lines **85–103**: downstream solution results, **dependency context only**.

**Finding ID: `POME-SPHERE-RIESZ-ENERGY-THRESHOLD-001`. Severity: low. Status: verified conditional deduction.** The precise Euclidean energy and local-dimension assertions below are independent direct computations; the Monge–Ampère domination and PDE-solvability implications are *conditional on* the printed Proposition 15.26.2, Theorem 15.25.1 and Theorem 15.26.4. **No printed theorem or proof is refuted**, and no purported proof repair is certified.

## Statement

In the local holomorphic chart used by Eq. 15.26.1, fix complex dimension `n >= 2`, real dimension `d=2n`, `r_0>0` sufficiently small, and
\[
r_j=r_0 2^{-j},\qquad
S_n=\sum_{j\ge1}r_j^{n/2}
     =\frac{r_0^{n/2}}{2^{n/2}-1},\qquad
w_j=\frac{r_j^{n/2}}{S_n},\qquad
\rho=\sum_{j\ge1} w_j\sigma_{r_j},
\]
where `sigma_r` is normalized Euclidean surface measure on the sphere `|z|=r`. This is exactly the original measure, not a new choice of weights.

For `s>0` define the ordinary *real Riesz self-energy*
\[
\mathcal I_s(\rho)
=\iint_{\mathbb R^{2n}\times\mathbb R^{2n}}
   |z-w|^{-s}\,d\rho(z)\,d\rho(w),
\]
allowing `+infinity`. Then the **sharp threshold is**
\[
\boxed{\mathcal I_s(\rho)<\infty\quad\Longleftrightarrow\quad 0<s<n.}
\]
In particular the classical Newtonian kernel exponent in real dimension `2n` is `s=2n-2 >= n`, and **`rho` has infinite Newtonian self-energy in every complex dimension `n >= 2`**, despite its printed non-pluripolarity and Hölder Monge–Ampère domination.

The measure has two distinct exact local scaling exponents:
\[
\lim_{t\downarrow0}\frac{\log\rho(B(0,t))}{\log t}=\frac n2,
\qquad
\lim_{t\downarrow0}\frac{\log\rho(B(x,t))}{\log t}=2n-1
\quad\text{for every }x\in\{|z|=r_j\},\ j\ge1.
\]
Thus it is **not Ahlfors regular with a single exponent on its support**. All of these exponents and the finiteness threshold persist under replacing Euclidean distance by the distance of any fixed smooth Hermitian metric in the relatively compact chart, by local bi-Lipschitz equivalence.

## Complete energy proof and normalization

Let `d=2n`. The energy of one normalized unit sphere has the rotationally invariant value
\[
A_{d,s}:=\iint_{S^{d-1}\times S^{d-1}}
       |u-v|^{-s}\,d\sigma_1(u)\,d\sigma_1(v).
\]
Near the diagonal the integral is comparable to
`int_0^1 t^{d-2-s} dt`, hence `A_{d,s}<infinity` **if and only if** `s<d-1`. For `0<s<d-1`, scaling yields
`I_s(sigma_{r_j})=A_{d,s}r_j^{-s}`. An optional exact beta-integral check is
\[
A_{d,s}
 =\frac{2^{d-2-s}\Gamma(d/2)}
         {\sqrt\pi\,\Gamma((d-1)/2)}
     B\!\left(\frac{d-1-s}{2},\frac{d-1}{2}\right);
\]
it gives `A_{4,2}=1`, consistent with the four-dimensional Newtonian spherical-shell normalization.

Because the shells have disjoint supports and the kernel is nonnegative, Tonelli gives a decomposition into **self** and **cross** terms. The self terms sum exactly to
\[
\sum_{j\ge1}w_j^2\,\mathcal I_s(\sigma_{r_j})
=\frac{A_{2n,s}}{S_n^2}
  \sum_{j\ge1}r_j^{n-s}.
\]
For `0<s<2n-1`, this is finite iff `s<n`. More precisely, for `s<n` it is exactly
\[
A_{2n,s}\,
\frac{(2^{n/2}-1)^2}
     {(2^{n-s}-1)r_0^s}.
\]
At the critical exponent `s=n` **each individual shell contributes the same strictly positive amount**, so the sum diverges. When `s>=2n-1`, even an individual sphere has infinite energy. This already proves the **necessity** of `s<n` in all ranges.

For sufficiency assume `0<s<n`. If `j<k`, then `r_k<=r_j/2`, hence
`|z-w|>=r_j-r_k>=r_j/2` on the product of the two shells. Consequently the sum of both cross-orderings is bounded by
\[
2\sum_{j<k}w_jw_k\iint|z-w|^{-s}\,d\sigma_{r_j}d\sigma_{r_k}
\le \frac{2^{s+1}}{S_n^2}
\sum_{j\ge1}r_j^{n/2-s}\sum_{k>j}r_k^{n/2}.
\]
The inner tail equals `r_j^{n/2}/(2^{n/2}-1)`, so the last expression is at most
\[
\frac{2^{s+1}}{S_n^2(2^{n/2}-1)}
\sum_{j\ge1}r_j^{n-s}<\infty.
\]
Combining with the finite self sum proves `I_s(rho)<infinity` for every `0<s<n`.

There is no interchange of conditionally convergent sums or limits: the decomposition and all estimates use **nonnegative** integrands and Tonelli. No Bedford–Taylor or regularization input is needed for this Riesz computation.

## Exact local dimensions

For `0<t<r_1`, let `J(t)` be the smallest index with `r_{J(t)}<t`. By the strict-radius definition of the open ball and the geometric weights,
\[
\rho(B(0,t))
=\sum_{j\ge J(t)}w_j
=\frac{r_{J(t)}^{n/2}}{S_n(1-2^{-n/2})}.
\]
Because `r_{J(t)}<t<=2r_{J(t)}`, this mass is bounded above and below by fixed positive multiples of `t^{n/2}`, proving the first logarithmic limit. If `t` equals a shell radius, use the first **strictly smaller** shell in `J(t)`; the displayed formula remains valid.

Fix `x` on the `j`th sphere. For all sufficiently small `t` (e.g. `t<r_j/4`), the ball `B(x,t)` meets no other sphere and does not contain the origin. In tangent coordinates its intersection with the smooth sphere is a spherical cap whose surface area satisfies
\[
\rho(B(x,t))
= w_j\frac{\operatorname{vol}(B^{d-1})}
               {\operatorname{area}(S^{d-1})}
      \left(\frac{t}{r_j}\right)^{d-1}
     (1+o(1)).
\]
This gives the second logarithmic limit `d-1=2n-1`. The support consists of the spheres and their accumulation point `0`, so there are no other supported-point cases.

## Interpretation, scope, historical boundary

The exact **Riesz-energy threshold and the two local-dimension exponents** are new; they are **not** the earlier 2026-10-18 diagonal sphere Monge–Ampère normalization or 2026-10-25 `POME-HOLDER-BALL-MASS-EXPONENT-001` concerning *arbitrary Hölder psh potentials and ball-mass bounds*. Those earlier results are preserved, not refiled. Our energy is the real Riesz double integral; it is not the non-pluripolar Monge–Ampère mass, and the two should not be identified.

Theorem 15.26.4 (with `nu=rho`, `M_rho(rho)=1`) *conditionally* provides a bounded solution for every positive exponential parameter despite `rho`'s infinite Newtonian energy. This only excludes adding **finite Newtonian self-energy as a necessary hypothesis** to that particular sufficient solvability class; no existing theorem assumes or asserts it. The general PDE existence, comparison and Hölder-source theorems are **not independently certified**.

**Disposition:** low / verified conditional deduction. Proposed optional **English explanatory remark** following Proposition 15.26.2 or Theorem 15.26.4 recording the precise real Riesz threshold `s<n` and explicitly distinguishing it from the complex Monge–Ampère energy. **No source/body/registry/canonicalization/tag change is authorized or made.** The exact affected contextual dependents are Corollary 15.26.3, Theorem 15.26.4, and their cited Theorems 15.25.1/15.10.1; none is refuted.

**Coverage:** incremental proof-level check only of §15.26.1/.2/.3/.4 and the explicit energy/kernel computation. §15.26 had previously been sampled: **0 first-visited numbered sections, 0 whole-section certifications; current main table of contents 25 chapters / 747 sections**. No full source proof-chain verification, project build, tests, formalization, CI or publication. The user-excluded Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof-completion work remains strictly **deferred-by-user**, not reviewed, resolved or certified.
