# Selected audit: Hartogs coefficient upper regularization and degenerate energy pairing

**Date:** 2026-11-02. **Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Scope:** two selected, independent nonexcluded reading-edition arguments in §§9.15 and 17.2; no theorem, section, or upstream dependency-chain certification. **Findings:** `POME-HARTOGS-USC-LIMSUP-NECESSARY-001` and `POME-ENER-IBP-DEGENERATE-CURRENT-001`, each **low / verified conditional deduction**. Neither printed statement is false and no source repair was applied.

## 1. POME-HARTOGS-USC-LIMSUP-NECESSARY-001

**Anchor.** `docs/sections/complete-hartogs-domains-and-taylor-coefficients/index.html`, `main` blob `641a66c419e4a1f7207cd301b51f27f3a6efd6f9`; Proposition **9.15.1**, source `klimek-pluripotential-theory:7CA9E7D7`, permanent tag `202C805DC8A2`, physical lines **7–16** (hypotheses and the starred limsup) and **22–26** (integrated proof). Its assumptions allow `n=2`, a pseudoconvex base disk, and the constant fiber radius `R=1`. The printed identity correctly takes the **upper-semicontinuous regularization** of the coefficient-growth limsup.

**An elementary natural-boundary series.** Let
\[
g(\zeta)=\sum_{k=1}^{\infty}\zeta^{2^k},\qquad |\zeta|<1.
\]
It converges locally uniformly in the unit disk. If `\xi` is a root of unity of order `2^N`, then for real `r\uparrow1`,
\[
g(r\xi)=\sum_{k<N}r^{2^k}\xi^{2^k}
          +\sum_{k\ge N}r^{2^k},
\]
and the second sum increases without bound, while the first sum remains bounded. Thus `g` cannot extend holomorphically through any such `\xi`. Since dyadic roots of unity are dense in the unit circle, `g` has **every** point of the unit circle as a nonextendible boundary point. This does not invoke the Hadamard gap theorem or another external mathematical input.

Set `D={|z|<1}`, `H=D\times\{|w|<1\}`, `R(z)=1`, and
\[
f(z,w)=g(z)+z\,g(w).
\]
The polydisk is pseudoconvex (for example, it has the standard product psh exhaustion). More importantly, **`H` is a domain of existence of this particular `f`**. If a holomorphic extension existed across a boundary point with `|z_0|=1`, choose an interior `w_*` close enough to its second coordinate so that `(z_0,w_*)` lies in the extension neighborhood. Restricting to `w=w_*` would extend `g(z)=f(z,w_*)-zg(w_*)` across `z_0`, a contradiction. If instead `|w_0|=1`, choose an interior `z_*\ne0` sufficiently close to its first coordinate. Restricting to `z=z_*` would extend `g(w)=(f(z_*,w)-g(z_*))/z_*` across `w_0`. These alternatives cover every boundary point, including the corners. Hence no holomorphic extension exists across any boundary point of `H`.

The expansion of `f` in the fiber variable is explicit:
\[
c_0(z)=g(z),\qquad
c_{2^k}(z)=z\ (k\ge1),\qquad
c_j(z)=0\ \text{for other }j\ge1.
\]
Assign `\log0=-\infty`. Then the **unregularized** growth function is
\[
L(z):=\limsup_{j\to\infty}\frac{\log|c_j(z)|}{j}
=\begin{cases}0,&z\ne0,\\-\infty,&z=0.\end{cases}
\]
For `z\ne0`, the subsequence `j=2^k` tends to zero after dividing the fixed `\log|z|` by `2^k`, while all other terms are `-\infty`. At `z=0` all positive-degree coefficients vanish. Consequently `L^*\equiv0=-\log R`, whereas `L(0)=-\infty\ne0`. **Even with a continuous constant radius, a pseudoconvex Hartogs domain and an individual function having precisely that domain of existence, the star cannot be omitted.**

**Classification / proposal / dependents.** **Low / verified conditional deduction (correct printed proposition).** Add an optional explicit remark immediately after Proposition 9.15.1: pointwise coefficient radii can exceed the geometric Hartogs fiber radius on a proper analytic set, so the usc regularization is essential. Do not replace the stated starred limsup by a pointwise equality when quoting the proposition or canonicalizing its versions. The only directly checked affected assertion is Proposition 9.15.1 itself and its local-PSH representation consequence; no additional printed dependent theorem is claimed erroneous. The full Oka/pseudoconvexity equivalence and general Hartogs-lemma proof are **not** re-certified by this construction.

## 2. POME-ENER-IBP-DEGENERATE-CURRENT-001

**Anchor.** `docs/sections/relative-energy-and-perron-segments--integration-by-parts-for-bounded-differences/index.html`, `main` blob `5779ef1a17a52e02052c7485a7aa04adf606aace`; Lemma **17.2.7**, source `foundations-of-pluripotential-theory:D31C3788`, permanent tag `52C5A516B8C8`, physical lines **197–223**; signed non-pluripolar Hessian definition **17.2.1**, source `563C886F`, permanent `6B17AADE0338`, lines **17–47**. Lemma 17.2.7 asserts a **nonstrict** `\le0` pairing for bounded differences of equal singularity type and positive closed auxiliary factors. Its proof uses equality of total masses, plurifine locality and layer cake; we checked the direction of the resulting inequality and the degeneracy in a smooth Kähler model.

Let `X=\mathbb P^1_z\times\mathbb P^1_w` and `\omega_i=\operatorname{pr}_i^*\omega_{\mathrm{FS}}`. Put `\theta=\omega_1+\omega_2`, take an arbitrary nonconstant real `h\in C^\infty(\mathbb P^1)`, and choose `\varepsilon>0` small enough that
\[
u=\varepsilon\,h\circ\operatorname{pr}_1,\quad
v=0,\quad \theta+\mathrm{dd}^{\mathrm c}u\ge0.
\]
Both are smooth `\theta`-psh with `u\sim v`, yet `u-v` is nonconstant. For the **nonzero, smooth, closed, semipositive** current `T_1=\omega_1`, the first factor has complex dimension one, so
\[
\mathrm{dd}^{\mathrm c}(u-v)\wedge T_1
=\varepsilon\operatorname{pr}_1^*(\mathrm{dd}^{\mathrm c}h\wedge\omega_{\mathrm{FS}})=0.
\]
Thus the integral in Lemma 17.2.7 is **exactly zero for a nonconstant smooth difference**, even without singularities or mass loss. This supplies a sharp obstruction to inferring constancy from equality in its inequality.

For comparison, replacing `T_1` by `\omega_2` gives
\[
\int_X (u-v)\,\mathrm{dd}^{\mathrm c}(u-v)\wedge\omega_2
=\varepsilon^2\int_{\mathbb P^1}h\,\mathrm{dd}^{\mathrm c}h
=-\frac{\varepsilon^2 i}{2\pi}
  \int_{\mathbb P^1}\partial h\wedge\bar\partial h<0
\]
with `\int\omega_{\mathrm{FS}}=1` and the Pome normalization `\mathrm{dd}^{\mathrm c}=i\partial\bar\partial/(2\pi)`. In general, for **smooth real** `a` and a closed positive current `R`, Stokes gives `\int_X a\,\mathrm{dd}^{\mathrm c}a\wedge R=-\int_X\mathrm da\wedge\mathrm d^{\mathrm c}a\wedge R\le0`; this is strict for nonconstant `a` on a connected compact manifold whenever `R\ge\delta\omega^{n-1}` for some `\delta>0`. No such uniform lower bound is assumed in Lemma 17.2.7.

**Classification / proposal / dependents.** **Low / verified conditional deduction (correct printed lemma).** Optionally append a sharpness remark: equality does not force constant difference for degenerate auxiliary currents. Any later strict-concavity or uniqueness deduction from **equality** must provide an independent strict-positivity/nondegeneracy argument. We have **not** identified or asserted a specific downstream published false theorem, and this does not alter the lemma's statement or proof. The full upstream singular integration-by-parts chain and the general equality characterization for singular potentials remain unverified.

## Coverage, boundaries and change policy

This increment is the **first direct model/proof-level check of §9.15.1** beyond the historical context-only Taylor-coefficient reading; §17.2 had already been sampled, but the explicit degenerate-auxiliary-current equality model and strict comparison are **new selected checks**. Neither §9.15 nor §17.2, nor any entire upstream proof chain, has been mathematically certified. Current audited table of contents is **25 chapters and 747 numbered sections**, with **zero complete section certificates**.

The scope excludes, without examining or silently resolving, Demailly approximation/regularization and its dedicated Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss completion programmes. Their earlier ledger entries remain **deferred-by-user**. This is an **audit-only proposed note**, not an edit to source texts, proof registry, canonicalized bodies, permanent tags or `main`. No project builds, tests, CI, formalizations or website publication were performed.
