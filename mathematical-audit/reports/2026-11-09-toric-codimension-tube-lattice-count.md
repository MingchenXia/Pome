# 2026-11-09 — Uniform codimension-sensitive shifted-lattice counts for thin convex bodies

**Finding:** `POME-TORIC-LOWERDIM-TUBE-COUNT-001` — **low / verified conditional deduction** (elementary, fully proved at the fixed Euclidean-lattice level). The integrated Theorem 21.7.3 and Corollary 21.7.4 are **correct**. No missing hypothesis or failure of their conclusions is alleged. This note sharpens the *rate*, for lower-dimensional bodies, of their already proved **ambient-dimensional** convergence; it is **not** a new form of intrinsic Okounkov semigroup counting.

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Primary integrated reading edition:** `docs/sections/convex-analysis-and-toric-potentials--lattice-points-and-volume/index.html`, blob `5d209b7f4d2156c19bc3fb300303405df6321230`. Theorem **21.7.3**, source label `foundations-of-pluripotential-theory:364BCD30`, permanent tag `831AEEB7084F`, physical lines **57–90** (shifted-grid cells, sandwich and modulus of continuity: 68–88). Corollary **21.7.4**, source `foundations-of-pluripotential-theory:D6B87DCB`, tag `CF4226A5034F`, lines **93–105**. Proposition **21.7.2**, source `foundations-of-pluripotential-theory:5E9AEE47`, tag `EDD78BC61BD7`, lines **27–54**, supplies the parallel-body conventions. For conceptual comparison only, `docs/sections/flags-convex-bodies-and-section-growth/index.html`, blob `83557f0e15275253661fe679c75407e6636d497c`, Theorem **19.9.9**, source `non-kahler-pluripotential-theory:4EE23942`, tag `CC2BF9294FA3`, lines **173–233**; its semigroup theorem is not reproved.

## Precise statement

Work in the chosen lattice basis of §21.7, so `M=Z^n` and Lebesgue covolume is one. Let `n>=1`, let `K⊂R^n` be any **nonempty compact convex** body with affine dimension `d<n`, and set `c=n-d>=1`. For any translations `a_k∈R^n`, radii `r_k>=0` with `r_k/k→0`, and all sufficiently large integer `k`, one has

\[
\boxed{
  \#\bigl((kK)^{r_k}\cap(\mathbb Z^n+a_k)\bigr)
    \le C(K,n)\,k^d(r_k+1)^{n-d}.                 \tag{1}
}
\]

The constant is independent of `k,r_k,a_k`. Equivalently, the normalized number is `O(((r_k+1)/k)^{n-d})`, uniformly in **all** grid translations. For every continuous `f:R^n→R` there is a constant `C(K,n,f)` such that

\[
\boxed{
 \left|k^{-n}\!\sum_{m\in(kK)^{r_k}\cap(\mathbb Z^n+a_k)} f(m/k)\right|
  \le C(K,n,f)\left(\frac{r_k+1}{k}\right)^{n-d}. \tag{2}
}
\]

The limiting integral from Theorem 21.7.3 is zero, since `K` has ambient Lebesgue measure zero. This is a one-sided uniform estimate; no positive lower bound holds without arithmetic conditions on the affine span.

## Complete elementary proof, including zero-dimensional and nonrational cases

Fix `x_0∈K`, let `A=x_0+V` be the affine span of `K`, and choose `R>=0` with `K⊂x_0+B_V(R)`. The orthogonal decomposition `R^n=V⊕V^⊥` is used **only for volume**: it does not rotate or replace the fixed integer lattice. For `0<δ<=1`, a point of `K^δ` is within distance `δ` of some point of `K`; hence it lies in the product cylinder

\[
 (x_0+B_V(R+1))\times B_{V^\perp}(\delta).
\]

Writing `ω_j` for the Euclidean volume of the unit ball in dimension `j`, with `ω_0=1`, Fubini gives the explicit parallel-tube upper bound

\[
 \operatorname{vol}_n(K^\delta)
  \le \omega_d(R+1)^d\,\omega_{n-d}\,\delta^{n-d}.           \tag{3}
\]

There is no positive-inradius premise: `d=0` is allowed.

For any `k`, decompose `R^n` into the half-open cubes `m/k+k^{-1}[0,1)^n` indexed by `m∈Z^n+a_k`. Select exactly those whose anchors satisfy `m∈(kK)^{r_k}`, and let `U_k` be their union. These half-open cells are disjoint, cover the ambient space, and have volume exactly `k^{-n}`, independently of their translation. Every point of a selected cell lies within `√n/k` of its anchor, so the direct inclusion in the printed proof of Theorem 21.7.3 (line 80) gives

\[
 U_k\subset K^{\delta_k},\qquad
 \delta_k=(r_k+\sqrt n)/k.                                  \tag{4}
\]

Since `r_k/k→0`, eventually `0<δ_k<=1`. Combining cell volume, (3), and (4),

\[
 \begin{aligned}
 \#((kK)^{r_k}\cap(\mathbb Z^n+a_k))
  &=k^n\operatorname{vol}_n(U_k) \\
  &\le \omega_d(R+1)^d\omega_{n-d}
       k^d(r_k+\sqrt n)^{n-d}\\
  &\le \omega_d(R+1)^d\omega_{n-d}
       (\max\{1,\sqrt n\})^{n-d}
       k^d(r_k+1)^{n-d}.
 \end{aligned}                                                  \tag{5}
\]

This is (1), with an explicit permissible constant. All bounds remain valid if the chosen translated lattice misses the affine span entirely. For (2), selected anchors satisfy `m/k∈K^{r_k/k}⊂K^1` for large `k`; the continuous `f` is bounded on this compact set. Bound the absolute sum by `\|f\|_{C(K^1)}` times (1). No limit exchange, sequential compactness, Hausdorff approximation, or use of an unproved semigroup-counting result occurs.

## Sharpness of *both* exponents, and why intrinsic counting is different

Let `1<=c=n-d` and take the coordinate lower-dimensional box

\[
 K=[0,1]^d\times\{0\}^{c}\subset\mathbb R^n,
 \qquad a_k=0.
\]

All integer points `(p,q)` with `p∈\{0,1,\ldots,k\}^d` and `q∈Z^c`, `|q|<=r_k`, are in `(kK)^{r_k}`. In particular the integer cube `|q_j|<=\lfloor r_k/\sqrt c\rfloor` lies in that ball, so

\[
 \#((kK)^{r_k}\cap\mathbb Z^n)
 \ge (k+1)^d\bigl(2\lfloor r_k/\sqrt c\rfloor+1\bigr)^c.
                                                                  \tag{6}
\]

For `r_k=0`, this is exactly `(k+1)^d`; for `r_k→∞` with `r_k=o(k)`, the lower bound is of order `k^d r_k^c`. Thus the order `k^d(r_k+1)^c` in (1) is optimal **in general** at fixed and increasing thickness; a uniform improvement in the powers of `k` or of large `r_k` is impossible. This does not assert an asymptotic constant for arbitrary bodies or affine directions.

Conversely, when `n>d`, fix an irrational number `α` and take

\[
 K=[0,1]^d\times\{\alpha\}\times\{0\}^{c-1},\qquad r_k=0,\quad a_k=0.
\]

Then `kα\notin Z` for every positive integer `k`, so `kK∩Z^n=∅` **for every k**, despite the affine dimension being `d` and the intrinsic `d`-volume being one (also when `d=0`, in the convention that a point has intrinsic volume one). The same phenomenon can be forced by suitable translated grids for a rational affine flat.

This is exactly why the **group-generated lattice** `Λ` and **degree period** `e` in Theorem 19.9.9 cannot be replaced by a blanket ambient lattice assertion. That theorem's positive intrinsic-volume limit requires an actual graded valuation semigroup; the arbitrary irrational flat above is **not** asserted to arise from such a semigroup. No proof step or conclusion of 19.9.9 is contradicted.

## Audit disposition and boundaries

**Classification:** low / verified conditional deduction (self-contained elementary proof based on the printed §21.7 lattice and normalization conventions); **no confirmed error, no missing theorem hypothesis, no general analytic external dependency** introduced. **Proposed change:** optionally insert a separate corollary/remark after Theorem 21.7.3 giving the codimension-sensitive upper bound, the rational-box sharpness, and the irrational-flat caution. Preserve the printed statements, source attribution, permanent tags, and the existing stronger *full-dimensional* discrepancy and moving-body reports: `POME-CONVEX-ALLBODIES-LATTICE-RATE-001`, `POME-LATTICE-MOVING-BODY-001`, and `POME-TORIC-HAAR-SHIFT-EXACT-001` are **different results** and are not reopened or relabeled.

**Actual coverage:** newly derived the tube estimate (3) and the uniform cell bound (1)–(2), verified sharpness (6), and inspected the integrated §21.7.2–4 lines 27–105. Compared only the precise §19.9.9 lattice/period hypotheses and lines 173–233, without certifying the Kaveh–Khovanskii counting input. §21.7 and §19.9 were already partly sampled in earlier sessions: **zero first section visits, zero complete mathematical section certifications**; actual current ToC is **25 chapters, 747 numbered sections, zero whole-section certificates**. Previously unresolved gaps, true errors, external inputs, and all user-deferred approximation/regularization/Bergman/L²/OT/multiscale/positivity-loss items remain classified as before. No Demailly-regularization work or excluded prerequisites were opened; no main, source, body, canonicalization, registry, tag, CI, build, tests, formalization, or publication changes.
