# Exact global quadratic potential law for Hermitian-symplectic completion energy

**Date:** 2026-11-16. **Finding ID:** POME-HERMSYMP-GLOBAL-QUADRATIC-POTENTIAL-001. **Classification:** low / **verified conditional deduction**; **no false printed theorem** and **no claimed production repair**.

## Pinned integrated reading edition and scope

Reviewed main commit: b6933b772f41b45918f7e25ed1afbbb1fd892272. Principal file: docs/sections/monge-ampere-energy-and-torsion/index.html, blob fe1ca06167b8f5bc9868e9a9876397afad4e7ff5. The canonical completion and its norm are at physical lines 211–234. Lemma 11.2.15 (source non-kahler-pluripotential-theory:FF812850; permanent tag 19D4882CC9D5) appears at lines 237–250; Proposition 11.2.17 (source non-kahler-pluripotential-theory:F8C97F67; tag AE6CE389C569), with the crucial identity (11.2.18), permanent tag BAFFEA611460, at lines 253–287. Theorem 11.2.19 (source non-kahler-pluripotential-theory:69225BEF; tag 04BD04D6C676) and its formula (11.2.20) (source non-kahler-pluripotential-theory:56FBE8ED; tag 8B6CFC8EA37B) are at physical lines 291–319. Corollary 11.2.21 (source non-kahler-pluripotential-theory:645E67CA; tag 67DF1C6C0509) starts at 322. Cross-check: docs/sections/torsion-and-the-variation-of-mass/index.html, blob 9abec9685e33a1b40f9c0765381408eb52b325d3, Lemma 11.1.3 (source non-kahler-pluripotential-theory:0C4D5A94; tag BF56C7366FC6), lines 36–50, and Lemma 11.1.2 (tag 3B0A8DD950AD), lines 15–31.

This run directly read the completion definition, the complete displayed proof of Proposition 11.2.17, the proof of Theorem 11.2.19 and the Corollary 11.2.21 statement, along with the two indicated integration identities. The remainder of §11.2, the existence theory of arbitrary singular metrics, and the bounded-potential regularization invocation are **not** newly certified.

## Precise statement (new exact consequence of the printed proposition)

Let X be a connected compact complex fourfold, let \(\omega>0\) be a smooth real Hermitian-symplectic (1,1)-form, and normalize \(dd^c=(i/2\pi)\partial\bar\partial\), as in Pome. Let \(\rho_\omega\) be the canonical (2,0)-completion and \(F(\omega)=\frac12\int_X\rho_\omega\wedge\bar\rho_\omega\wedge\omega^2\). Put \(\Psi=dd^c(\omega^2)\). For every smooth real u with \(\omega_u=\omega+dd^c u>0\),

\[
\boxed{F(\omega_u)-F(\omega)
=-\frac16\int_Xu\,dd^c(\omega^3)
+\frac14\int_X\Psi\wedge du\wedge d^c u
=-\frac12\int_Xu\,\omega\wedge\Psi
+\frac14\int_X\Psi\wedge du\wedge d^c u.}
\tag{1}
\]

In particular \(\Psi_u=dd^c(\omega_u^2)=\Psi\) for every such u. For all smooth v,w,

\[
\boxed{H_{\omega_u}(dd^c v,dd^c w)
=\frac12\int_X\Psi\wedge dv\wedge d^c w,}
\tag{2}
\]

**independently of u**. If all three potentials u, v, and u+v are admissible, their exact polarized four-point defect is

\[
\boxed{F(\omega_{u+v})-F(\omega_u)-F(\omega_v)+F(\omega)
=\frac12\int_X\Psi\wedge du\wedge d^c v.}
\tag{3}
\]

If \(\Psi\ne0\), the same indefinite quadratic form occurs at **every** point of the positive potential slice, so **no point of that slice is a local maximum or minimum** of F. If \(\Psi=0\), F is constant on that slice. Thus the printed dichotomy at the base metric can be made basepoint-independent. This is a deduction in the smooth potential slice only, not a result for all Aeppli deformations or bounded singular potentials.

## Full proof, including signs and coefficients

1. Hermitian-symplectic implies pluriclosed: \(dd^c\omega=0\). Set \(\alpha=dd^c u\), so \(d\alpha=d^c\alpha=0\). Stokes and Lemma 11.1.2 give \(\int_X\omega\wedge\alpha^3=\int_X u\,dd^c(\omega\wedge\alpha^2)=0\). Also \(\int_X\alpha^4=0\), since \(\alpha^4=d(d^cu\wedge\alpha^3)\). Expanding \(V(\omega_u)=\frac1{24}\int_X(\omega+\alpha)^4\) gives the **exact**, not asymptotic, formula

\[
V(\omega_u)-V(\omega)
=\frac16\int_Xu\,dd^c(\omega^3)
+\frac14\int_X\omega^2\wedge\alpha^2 .
\tag{4}
\]

The binomial coefficients are \(4/24=1/6\) and \(6/24=1/4\).

2. The canonical-completion identity \(F(\omega_u)+V(\omega_u)=F(\omega)+V(\omega)\), Eq. (11.2.18), has a short independent check. For any completion \(\zeta\), the real form \(\Theta_\zeta=\omega+\zeta+\bar\zeta\) is closed, and in complex dimension four its fourth power gives

\[
\frac1{24}\int_X\Theta_\zeta^4
=V(\omega)+\frac12\int_X\zeta\wedge\bar\zeta\wedge\omega^2
+\frac14\int_X\zeta^2\wedge\bar\zeta^2.
\]

The same \(\zeta\) completes \(\omega_u\) because \(\partial\omega_u=\partial\omega\); moreover \(\Theta_\zeta\) changes by the exact form \(dd^cu\), hence its fourth integral is unchanged. The last term does not change, so the squared completion norm shifts by \(-[V(\omega_u)-V(\omega)]\), **independently of \(\zeta\)**. Taking the minimizer on both sides proves both the same canonical completion and the asserted identity. No external analytic theorem is used beyond the definition and finite-dimensional orthogonal projection.

3. Apply integration by parts to (4): since \(\Psi=dd^c(\omega^2)\), it is d-closed and \(d^c\)-closed, and

\[
\int_X\omega^2\wedge (dd^cu)^2
=\int_X u\,dd^cu\wedge\Psi
=-\int_Xdu\wedge d^cu\wedge\Psi.
\]

The final minus sign follows directly by integrating \(d(u\,d^cu\wedge\Psi)\) over compact X. Combining with step 2 yields the first equality of (1). By Lemma 11.1.3 and \(dd^c\omega=0\), one has
\(dd^c(\omega^2)=2d\omega\wedge d^c\omega\) and \(dd^c(\omega^3)=6\omega\wedge d\omega\wedge d^c\omega=3\omega\wedge\Psi\), proving the second equality of (1).

4. The same power identity gives \(dd^c(\omega_u^2)=\Psi+2dd^c(\omega\wedge\alpha)+dd^c(\alpha^2)=\Psi\): the two new terms vanish because \(dd^c\omega=0\), and \(\alpha\) is d- and \(d^c\)-closed. For a closed \(\Psi\), integration by parts shows

\[
\int_X\Psi\wedge dv\wedge d^cw
=-\int_Xv\,dd^cw\wedge\Psi
=\int_X\Psi\wedge dw\wedge d^cv.
\]

Hence differentiating the quadratic identity (1) twice gives (2), and expanding it for u+v gives (3). The factor in (2) matches Eq. (11.2.20), without a sign reversal.

5. If \(\Psi\ne0\), the original **local algebraic sign argument** from Theorem 11.2.19, lines 305–317, applies to the fixed \(\Psi\): the Hermitian symbols \(\Psi\wedge i\xi\wedge\bar\xi\) have opposite signs at some cotangent vectors. Indeed, if they were all semidefinite with one sign, their \(\omega\)-trace would have that sign but integrate to zero, because \(\int_X\Psi\wedge\omega=\int_X\omega^2\wedge dd^c\omega=0\); hence the symbols, and thus \(\Psi\), would vanish. Compactly supported high-frequency real cutoffs in arbitrarily many disjoint tiny balls then give arbitrarily high positive and negative definite finite-dimensional subspaces for (2). Because admissibility is C²-open, every basepoint \(\omega_u\) permits these sufficiently small variations. A nonzero first derivative immediately excludes an extremum; at a critical point either sign of the second derivative excludes local extrema. If \(\Psi=0\), the right side of (1) vanishes. This proves the last assertion.

## Classification, dependencies, correction and limits

- **Severity/status:** low / **verified conditional deduction**, not a confirmed error, not a gap in Theorem 11.2.19, and not a complete certification of the whole §11.2. The argument is algebraic and self-contained after the stated definition of Hermitian-symplectic canonical completion and Stokes; the completion identity was also rechecked in step 2.
- **Proposed addition (NOT applied to the published body):** after Theorem 11.2.19, record (1)–(3) as a smooth-potential quadratic-polynomial corollary and note basepoint-independence of the Hessian. Preserve original theorem, source tag, historical attribution, Aeppli/potential distinction and all other valid versions.
- **Affected dependents:** strengthens the smooth potential interpretation of Corollary 11.2.21; optional cross-check for smooth product constructions in Examples 11.2.23–24. It does not replace the bounded-psh equivalence in Corollary 11.2.21, which cites a regularization argument **deferred-by-user**, nor establish any general Aeppli-index claim beyond the potential subspace.
- **Coverage:** newly audited the full proof mechanism of §11.2.17 and §11.2.19 and the displayed normalization, within a previously partly visited section. **0 newly first-visited numbered sections, 0 fully certified numbered sections**; main table of contents is 25 chapters / 747 numbered sections. No build, test suite, CI, source-body or publication change.
- **Excluded scope preserved:** Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes remain **deferred-by-user**, neither repaired nor certified.
