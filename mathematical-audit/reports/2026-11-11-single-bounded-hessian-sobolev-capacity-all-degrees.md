# A single bounded Hessian potential charging Sobolev-polar sets in every higher degree

**Stable ID:** POME-HESS-SINGLE-POTENTIAL-HIGHER-SOBOLEV-CAP-FAIL-001  
**Severity/status:** low / **verified conditional deduction**; the printed lemmas and example are correct, not falsified.  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272  
**Date:** 2026-11-11. Branch: review/mathematical-audit.

## Anchored reading-edition audit

The integrated file `docs/sections/complex-hessian-equations--sobolev-capacity-and-two-hessian-factors/index.html` has blob `25f25433cb9b17de6715a5b05f8b3c15b95a18cd`. Lemma 8.10.2 (source `non-kahler-pluripotential-theory:1DDAECA7`, permanent tag `FFBF9CD42640`), physical lines 58–96, gives first-Hessian Sobolev-capacity domination. Lemma 8.10.6 (source `:350D7B3A`, tag `2A6BE9847309`), physical lines 185–207, makes compact pieces of smooth real-codimension-two submanifolds capacity zero. Example 8.10.7 (source `:36B886BE`, tag `AEB4F2397BBF`), physical lines 209–251, uses **two different** continuous potentials to produce a mixed degree-two measure charging such a set.

The canonical shifted product convention is Eq. 8.9.5 (source `:E021C6DE`, permanent `17FA1BFF2491`, physical line 86) and Theorem 8.9.6 (source `:61CC9D08`, permanent `846671D5582A`, lines 97–121), file `docs/sections/complex-hessian-equations--bounded-potentials-and-recursive-hessian-currents/index.html`, blob `117b866408974cdf706bf305df75e35e1b8affde`. Identification of explicit decreasing smooth products with canonical bounded products uses Theorem 8.11.12 (source `:B227378C`, permanent `C044CD1C65C4`, physical line 282 onwards), file `docs/sections/complex-hessian-equations--local-capacities-and-decreasing-products/index.html`, blob `115d285f6b1f76d284463c396e7e87db2b9dbdc3`; that general analytic theorem is a conditional internal input, not certified here.

## Statement

Fix integers \(2\le m\le n\). On a flat compact Kähler torus of complex dimension \(n\), there exists **one** bounded continuous and strictly \(\omega_0\)-plurisubharmonic (hence strictly \(m\)-admissible) function \(u\) and, for **each** \(r=2,\ldots,m\), a compact set \(E_r\) with
\[
\operatorname{Cap}_1(E_r)=0,\qquad
\left(Q_r(\underbrace{u,\ldots,u}_{r})\wedge\omega_0^{m-r}\right)(E_r)>0.
\]
More precisely, all these positive measures have an explicit nonzero restriction to a real-codimension-\(r\) box. Thus no estimate
\(\bigl(Q_r(u,\ldots,u)\wedge\omega_0^{m-r}\bigr)(F)\le C\operatorname{Cap}_1(F)^\theta\), for \(\theta>0\), can hold on every Borel \(F\), even with \(C\) depending on the fixed \(u\). The printed first-Hessian trace estimate is unaffected.

## Complete construction, limits and exact normalization

Take \(X=(\mathbb C/(\mathbb Z+i\mathbb Z))^n\) and
\[
\omega_0=\tfrac i2\sum_{j=1}^n dz_j\wedge d\bar z_j
          =\sum_{j=1}^n dx_j\wedge dy_j.
\]
Inside a coordinate polydisc choose a nonnegative smooth cutoff \(\chi\), supported in the chart, identically one on a smaller real coordinate box \(B_0\). For sufficiently small \(a>0\), set
\[
u=a\chi\sum_{j=1}^{m}|x_j|.
\]
Extend by zero outside the chart. Use \(g_\delta(t)=\sqrt{t^2+\delta^2}\) and \(u_\delta=a\chi\sum_{j=1}^{m}g_\delta(x_j)\). These are globally smooth, uniformly bounded, and decrease to \(u\) as \(\delta\downarrow0\). The term \(\chi\,dd^c g_\delta(x_j)\) is semipositive; every cutoff-cross term depends only on bounded \(g_\delta,g'_\delta\) and derivatives of \(\chi\). Therefore \(dd^c(\chi\sum_jg_\delta)\ge -C\omega_0\) **uniformly** in \(\delta\). Fixing \(a\le(2C)^{-1}\) gives
\(\omega_0+dd^c u_\delta\ge\frac12\omega_0\), hence the same current inequality for \(u\). This verifies the global and admissibility hypotheses without a regularization programme.

Write
\[
\alpha_j=\tfrac{i}{4\pi}dz_j\wedge d\bar z_j
         =\tfrac{1}{2\pi}dx_j\wedge dy_j.
\]
The project's \(dd^c=\frac{i}{2\pi}\partial\bar\partial\) convention gives on \(B_0\)
\[
dd^c g_\delta(x_j)=\tfrac12g_\delta''(x_j)\alpha_j,\qquad
g_\delta''(x)=\frac{\delta^2}{(x^2+\delta^2)^{3/2}},\qquad
g_\delta''(x)\,dx\rightharpoonup 2\delta_0.
\]
These independent one-dimensional approximate identities factor exactly under smooth wedge products; also \(\alpha_j^2=0\). For each \(1\le r\le m\), expand the smooth \((\omega_0+dd^c u_\delta)^r\wedge\omega_0^{n-r}\), then let \(\delta\downarrow0\). The canonical limit on \(B_0\) is the finite sum, over **distinct** coordinate indices,
\[
\mathcal H_r(u):=Q_r(u,\ldots,u)\wedge\omega_0^{m-r}
=\left(\omega_0+a\sum_{j=1}^m\delta_{\{x_j=0\}}\alpha_j\right)^r
\wedge\omega_0^{n-r}.
\]
The right-hand notation abbreviates the just-defined independent-variable products, not an unrestricted singular-current multiplication.

Let \(E_r\Subset B_0\cap\{x_1=\cdots=x_r=0\}\) be a closed relative coordinate box with positive \((2n-r)\)-dimensional Euclidean volume. Every expansion term using fewer than all \(r\) of these particular coordinate deltas is absolutely continuous in at least one omitted normal coordinate \(x_j\), hence gives **zero mass** to \(E_r\). The unique all-\(r\) set contributes \(r!\) permutations. Exactly on this box,
\[
\mathcal H_r(u)|_{E_r}
=r!a^r\left(\prod_{j=1}^r\delta_{\{x_j=0\}}\right)
\alpha_1\wedge\cdots\wedge\alpha_r\wedge\omega_0^{n-r}|_{E_r}.
\]
Since
\(\alpha_1\wedge\cdots\wedge\alpha_r\wedge\omega_0^{n-r}
=(n-r)!(2\pi)^{-r}\prod_{j=1}^n dx_j\wedge dy_j\), this yields the **exact mass**
\[
\boxed{\quad
\mathcal H_r(u)(E_r)=
\frac{r!(n-r)!a^r}{(2\pi)^r}
\operatorname{Vol}^{\mathrm{Eucl}}_{2n-r}(E_r)>0.\quad}
\]
There is only a single decreasing smooth approximation limit; no unjustified interchange of distinct singular-product limits occurs.

For \(r\ge2\), each \(E_r\subset\{x_1=x_2=0\}\), so Lemma 8.10.6 gives \(\operatorname{Cap}_1(E_r)=0\). For \(r=1\), the same \(u\) is covered by Lemma 8.10.2: with flat Gauduchon \(T=\omega_0^{n-1}\), the first trace remains absolutely continuous with respect to \(\operatorname{Cap}_1\). This exhibits the precise first/higher-degree boundary.

## Scope, novelty and ledger discipline

The prior printed Example 8.10.7 already establishes a **mixed** degree-two obstruction from **two distinct potentials**; the earlier 2026-10-22 audit read that result. It must not be counted again. The new content is the **one-and-the-same bounded continuous strictly admissible potential for all higher diagonal/self-products**, the \(r!\) multiplicity and explicit \(2n-r\)-dimensional mass formula. None of the printed assertions is false.

**Affected interpretation:** the caution after Example 8.10.7 extends to diagonal/self-products in every degree \(2\le r\le m\), while the Hessian capacity built in §8.11 must not be confused with §8.10's first-order Sobolev capacity. **Proposed correction:** optional additional remark after Example 8.10.7 giving the formula; this is an editorial proposal only, not a change to main/source/registry/tags. **Dependents:** the capacity distinction in §8.11 and any attempted higher-degree reuse of the estimate in §8.10.2. **Unresolved dependency:** the complete general proof of Theorem 8.11.12 remains unverified; only its use to identify this explicit smooth limit is recorded.

No dedicated Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas or positivity-loss proof-completion work was performed. All that programme remains **deferred-by-user**, not resolved or certified. Actual coverage: selected proof-level revisit to §8.10, dependency checks in §§8.9/8.11, **0 first visits**, **0 completely certified numbered sections**; ToC 25 chapters/747 sections. No builds, CI, formal verification or publication.
