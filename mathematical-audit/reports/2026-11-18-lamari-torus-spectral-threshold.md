# Flat-torus spectral threshold and nonattainment of smooth Gauduchon tests — direct audit of §11.6

**Finding ID:** POME-LAMARI-TORUS-SPECTRAL-THRESHOLD-001  
**Date:** 2026-11-18  
**Classification:** low / **verified conditional deduction** (with a self-contained sharp model); not a false theorem, not a gap in the printed statements.  
**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`  
**Branch before this increment:** `review/mathematical-audit`, beginning at `b36ca103a9b94d935a1f56b93ec18e03ebe1dfd4`.  
**Actual current ToC:** 25 chapters, 747 numbered sections.

## Exact integrated reading-edition targets

- `docs/sections/gauduchon-metrics-and-linear-mass--the-gauduchon-criterion-for-positivity/index.html`, blob `6dd43b62800206fb0302fd4261372d7882e5170d`, section `11.6`, permanent tag `6029C37CE10F`, source `non-kahler-pluripotential-theory:8909D36D`.
- Theorem **11.6.1** / permanent `88BE3B63D9E5` / source `non-kahler-pluripotential-theory:87DC00D0`, physical lines **11–73** (statement 11–18, positive \((n-1,n-1)\)-root 24–30, separation 34–51, scalar elliptic reconstruction 53–73).
- Corollary **11.6.2** / permanent `F83E15A1F529` / source `non-kahler-pluripotential-theory:EAE0F4AE`, lines **82–97**: the exact Gauduchon threshold \(\kappa_\omega(\theta)\).
- Lemma **11.6.3** / permanent `91B8C8A3C10E` / source `non-kahler-pluripotential-theory:DC67F892`, lines **105–116**; closing smooth-minimizer criterion **120–126**.
- Scope: `docs/sections/gauduchon-metrics-and-linear-mass/index.html`, §11.3, permanent `1009E65ECC4C` explicitly fixes **\(n\ge2\)** and a connected compact Hermitian setting for this chapter. This is important for the \((n-1)\)st root formula and is **not** a missing hypothesis.
- Selected upstream context: §11.4.2 / permanent `3978AEB15BD7`, integrated file `docs/sections/gauduchon-metrics-and-linear-mass--conformal-gauduchon-metrics/index.html`, blob `ecb4bf9e593dfb25f1644f0561d1aa65bf096b10`; §11.5.1 / permanent `828FAD1A35BF`, `docs/sections/gauduchon-metrics-and-linear-mass--conservation-of-the-trace-mass/index.html`, blob `34af83ff391b5e5590cd9cb10ca4cd2b3faff02c`. These are **dependency checks**, not separately certified whole sections.

## New exact spectral example

Let \(n\ge2\), \(X=E^n\) be a product of elliptic curves with its flat diagonal Kähler forms \(\omega_j>0\) in the \(j\)th factor. Set
\[
 \omega=\sum_{j=1}^n\omega_j,\qquad
 \theta=\sum_{j=1}^n a_j\omega_j,\qquad
 a_1=\min_j a_j,\quad a_j\in\mathbb R.
\]
There is no condition that the \(a_j\) be positive. For the exact Gauduchon-degree invariant of Corollary 11.6.2,
\[
 \boxed{\quad\kappa_\omega(\theta)=a_1.\quad}
\]
If at least one \(a_j>a_1\), this infimum is **not attained by any smooth Gauduchon metric**. Nevertheless the optimal curvature lower bound is attained by the smooth current
\[
 \boxed{\quad\theta-a_1\omega=\sum_{j=2}^n(a_j-a_1)\omega_j\ge0,\quad u=0.\quad}
\]
For the explicit sequence of flat Kähler (hence Gauduchon) metrics
\[
 \gamma_t=t\omega_1+\sum_{j=2}^n\omega_j,\qquad t>0,
\]
the ratio is **exactly**
\[
 \frac{\int_X\theta\wedge\gamma_t^{n-1}}
      {\int_X\omega\wedge\gamma_t^{n-1}}
 =\frac{a_1+t\sum_{j=2}^n a_j}{1+(n-1)t}
 =a_1+\frac{t\sum_{j=2}^n(a_j-a_1)}{1+(n-1)t}.
\]
Thus convergence to the infimum is linear in \(t\) (with positive coefficient in the non-scalar case). The normalized test forms
\[
 \Gamma_t=\frac{\gamma_t^{n-1}}{\int_X\omega\wedge\gamma_t^{n-1}}
\]
converge smoothly as forms to the *semipositive, non-strict* \((n-1,n-1)\)-form
\[
 \Gamma_0=\frac{(n-1)!\,\omega_2\wedge\cdots\wedge\omega_n}
                 {\int_X\omega\wedge (n-1)!\,\omega_2\wedge\cdots\wedge\omega_n},
 \qquad \mathrm{dd}^c\Gamma_0=0.
\]
It satisfies \(\int_X\omega\wedge\Gamma_0=1\) and \(\int_X\theta\wedge\Gamma_0=a_1\). In particular, the weakly attained dual test is not the \((n-1)\)st power of a **strictly positive** Hermitian form when the \(a_j\) are not all equal.

### Direct proof and sharpness

Since each \(a_j-a_1\ge0\), the form \(\theta-a_1\omega\) is pointwise semipositive. Therefore for **every** (possibly nontranslation-invariant) smooth Gauduchon metric \(\gamma\), the \((n,n)\)-form \((\theta-a_1\omega)\wedge\gamma^{n-1}\) is nonnegative, and
\[
  \frac{\int\theta\wedge\gamma^{n-1}}{\int\omega\wedge\gamma^{n-1}}\ge a_1.
\]
If some \(a_j>a_1\), the same top-degree form is strictly positive at every point, because \(\gamma\) is positive definite; hence the inequality is strict for every smooth \(\gamma\). Meanwhile each \(\gamma_t\) is closed and positive, so it is a legitimate Gauduchon test. The displayed exact wedge ratio tends to \(a_1\), giving the reverse bound and proving the asserted threshold and nonattainment without any regularization or limiting non-pluripolar product.

Expanding the wedge product gives \(\gamma_t^{n-1}=(n-1)!\,\omega_2\wedge\cdots\wedge\omega_n+O(t)\) in the finite-dimensional space of translation-invariant forms. Its normalized limit is \(\Gamma_0\). The limit is \(\mathrm{dd}^c\)-closed because every \(\omega_j\) is closed. It is rank-degenerate on the dual-cone side, which explains why the minimizing **current** exists although no smooth strictly positive minimizing test exists. Conversely, if all \(a_j=a_1\), then \(\theta=a_1\omega\) and every smooth Gauduchon metric attains the ratio; this proves the if-and-only-if classification for this family.

The example is compatible with the printed final smooth-minimizer criterion: a nonzero translation-invariant semipositive \(\theta-a_1\omega\) cannot be \(\mathrm{dd}^c f\), for otherwise Stokes against the flat Kähler form \(\omega^{n-1}\) would give zero whereas its integral is strictly positive.

## Direct section-level mathematical check

**11.6.1:** The positive \((n-1,n-1)\)-root step is valid under the §11.3 \(n\ge2\) convention. The sublinear majorant \(p(\Phi)=\inf\{\ell(\Gamma):\Gamma\in E,\Gamma\ge\Phi\}\) is finite: a fixed strictly positive \(\Gamma_0\in E\) gives uniform order bounds and \(\ell\ge0\) on semipositive elements of \(E\). Hahn–Banach yields a positive order-bounded functional, hence a positive current. For the \(\mathrm{dd}^c\)-exactness step, \(D(v)=\mathrm{dd}^c(v\Gamma_0)/dV\) has no zeroth-order part, has constants as its kernel by the maximum principle, and has Fredholm index zero; Stokes identifies its codimension-one range with functions of integral zero. The constructed distribution \(u\) satisfies \(\mathrm{dd}^c u=S\). No hidden sequential compactness or limit interchange is needed in this proof. **No false statement or new proof gap found.** The functional-analytic and distribution-to-psh inputs are genuine dependencies, not newly certified independently.

**11.6.2:** Normalize by the strictly positive denominator \(\int\omega\wedge\gamma^{n-1}\); the two directions of the threshold equivalence follow from the trace identity and 11.6.1 applied to \(\theta-a\omega\). The proof indeed asserts attainment of the **primal curvature bound**, not attainment by a smooth dual minimizing test.

**11.6.3 and the closing criterion:** If a positive \((1,1)\)-current has zero trace against a strictly positive \(\gamma^{n-1}\), all its coefficient measures vanish, so the current is zero. Smoothness of the potential then follows from a scalar elliptic trace equation. The conclusion about a smooth dual minimizer is consistent with the explicit flat-torus test above.

## Classification and follow-up

- **New stable finding:** POME-LAMARI-TORUS-SPECTRAL-THRESHOLD-001 — **low / verified conditional deduction**, with a complete unconditional wedge-product computation. **Affected:** Corollary 11.6.2 and the criterion after Lemma 11.6.3, only as a sharp demonstration of distinct primal and dual attainment; no source-theorem correction is needed.
- **No confirmed error, proof gap, or genuine duplication** is asserted for §11.6.
- **Precise remaining external/internal dependencies:** the general Gauduchon existence theorem §11.4.2; trace identity §11.5.1; Hahn–Banach and elliptic Fredholm/maximum principles in §11.6.1; conversion of positive current to a quasi-psh representative §5.22.2. This run checks their role, but not complete transitive proof chains. The torus computation itself needs only Stokes and elementary wedge algebra.
- **Coverage:** direct reading of **all** §11.6 statement/proof paragraphs and final criterion (physical lines 7–126), plus limited contextual reads of §§11.3–11.5. The prior ledger and original 747-section matrix are preserved, rather than marking other sections as certified. **+1 entire-section direct proof reading, +0 fully certified upstream chains.**
- **Deferred-by-user:** all Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion work. This audit did not reopen them.
- **Operations:** audit Markdown only on `review/mathematical-audit`; no source text, main, permanent tags, registry, builds, tests, CI, or publication.

Historical Lamari/Gauduchon attribution in the integrated edition is retained and is not reclassified as a missing proof.
