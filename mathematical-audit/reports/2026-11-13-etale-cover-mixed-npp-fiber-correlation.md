# Étale-cover correlation obstructs degree-normalized mixed non-pluripolar pushforward

**Date:** 2026-11-13. **Stable finding ID:** POME-NPP-ETALE-FIBER-CORRELATION-001. **Severity:** low. **Status:** **verified conditional deduction**, NOT an error in the printed bimeromorphic proposition or an applied repair.

**Main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Integrated file:** docs/sections/non-pluripolar-products--fiber-integration-and-modifications/index.html, blob 9954a43d90d5cae8ef744968636d7a5912348fce. **Exact anchor:** Proposition 13.6.3, source label foundations-of-pluripotential-theory:3F4A3A88, permanent tag 0811FFDF15B7, physical statement lines 35–44, proof lines 49–54.

## Statement being tested

Printed Proposition 13.6.3 asserts two non-pluripolar-product pushforward identities under a proper **bimeromorphic modification** between compact Kähler manifolds. The proof identifies the unique biholomorphic sheet off a proper analytic set and uses the fact that non-pluripolar products give this set zero mass. Nothing here refutes the printed theorem.

An earlier independent report, POME-NPP-FINITE-DEGREE-PUSH-SECOND-FAIL-001 (2026-11-03), established a generic degree factor for the pulled-back-current formula and found a branched finite self-map of projective space where the two unnormalized second-formula measures have **different total masses**. The present result tests the strictly stronger proposal that merely dividing by the generic degree restores the second identity. The example uses a smooth unramified covering, has **identical averaged individual currents**, and even has **equal total mixed masses**, but still fails as an equality of measures.

## Explicit degree-two étale construction

Let
\[
E=\mathbb C/(\mathbb Z+i\mathbb Z),\qquad
Y=E\times E.
\]
Use complex coordinates \(z=x+iy\), \(w=s+it\) on the covering vector space. Translation by half a real period,
\[
\tau(z,w)=(z+\tfrac12,w),
\]
is a free holomorphic involution. The quotient \(X=Y/\langle\tau\rangle\) is a compact complex torus, and \(\pi:Y\to X\) is a degree-two étale holomorphic covering. The flat Kähler form
\[
\Omega_Y=\frac{i}{2}\bigl(dz\wedge d\bar z+dw\wedge d\bar w\bigr)
\]
descends to a Kähler form \(\Omega\) on \(X\), so \(\pi^*\Omega=\Omega_Y\).

Define the globally smooth real-valued function and its real closed \((1,1)\)-form by
\[
f(z,w)=\cos(2\pi x)\cos(2\pi s),\qquad
H=dd^cf,\qquad dd^c=\frac{i}{2\pi}\partial\bar\partial.
\]
The key symmetry is \(f\circ\tau=-f\), hence \(\tau^*H=-H\). Since \(Y\) is compact, the eigenvalues of \(H\) relative to \(\Omega_Y\) are uniformly bounded. Thus for every sufficiently small positive \(\varepsilon\), both
\[
R_+=\Omega_Y+\varepsilon H,\qquad R_-=\Omega_Y-\varepsilon H
\]
are smooth **strictly positive closed** real \((1,1)\)-forms. Their non-pluripolar products are therefore simply their classical smooth wedge products, without any limiting or approximation step.

Pushforward of a topological covering counts its two sheets, so \(\pi_*\Omega_Y=2\Omega\). On the other hand,
\[
\pi_*H=\pi_*(\tau^*H)=-\pi_*H=0.
\]
Consequently the individual averaged currents agree *exactly*:
\[
\boxed{\tfrac12\pi_*R_+=\tfrac12\pi_*R_-=\Omega.}\tag{1}
\]

The square \(H^2=H\wedge H\) is invariant under \(\tau\), so it descends to a unique smooth real top-degree form \(\beta\) on \(X\), characterized by \(\pi^*\beta=H^2\). Therefore \(\pi_*H^2=2\beta\). Since wedge products of two-forms commute,
\[
R_+\wedge R_-=\Omega_Y^2-\varepsilon^2H^2,
\]
and
\[
\boxed{
\tfrac12\pi_*\langle R_+\wedge R_-\rangle
=\Omega^2-\varepsilon^2\beta,\quad
\left\langle(\tfrac12\pi_*R_+)\wedge(\tfrac12\pi_*R_-)\right\rangle
=\Omega^2.}\tag{2}
\]

The defect \(\beta\) is genuinely nonzero. At \(z=w=0\), the two diagonal complex-Hessian entries of \(f\) are \(-\pi^2\) and the off-diagonal entries vanish, since \(f_{xx}(0)=f_{ss}(0)=-4\pi^2\). It follows directly from the stated \(dd^c\) convention that
\[
H(0,0)=-\pi\Omega_Y(0,0),\qquad
H^2(0,0)=\pi^2\Omega_Y^2(0,0)\ne0.
\]
Thus \(\beta\) is positive and nonzero at the image of the origin, and the two positive smooth measures in (2) are **not equal**.

Nevertheless, their *total masses are equal*:
\[
\int_X\beta=\tfrac12\int_Y(dd^cf)^2=0.
\]
Indeed \(H=dd^cf\) is exact and closed, so \(H^2=d(d^cf\wedge H)\), and Stokes applies to compact \(Y\). Thus a mass comparison alone could not detect the new obstruction: \(\beta\) changes sign, and (2) is an intrinsically local difference.

## Scope of the deduction and possible correction

The two sides average different pairings over the sheets. The left side is the average of the **same-sheet products**; the wedge of the averaged individual currents includes **cross-sheet pairings**. These operations cannot be exchanged without a condition connecting the sheetwise currents.

A sufficient special case is \(R_j=\pi^*T_j\) for currents \(T_j\) downstairs. The *first* pullback-pushforward formula extends to such covers with the degree factor and gives the correct averaged product. It says nothing about arbitrary \(R_j\), as (1)–(2) show.

**Proposed editorial caution (not applied):** preserve the word “modification” and its bimeromorphic meaning in Proposition 13.6.3; do not assert a degree-normalized arbitrary-upstairs-current version even for finite étale maps. Any replacement needs explicit sheetwise compatibility or a correlation correction term. No original mathematical text, source, registry, canonicalization or permanent tag was changed.

**Affected potential dependents:** any planned finite-cover pushforward extension of Proposition 13.6.3; relative Monge–Ampère energy manipulations that wedge separately pushed-forward currents; canonical deduplication that confuses birational and finite-map statements. The existing birational theorem and the degree-weighted pulled-back-current identity remain intact.

**Dependencies and limits:** smooth forms, finite covering transfer, Stokes and the local fact from §13.2 that the non-pluripolar product of smooth positive forms equals their ordinary wedge. This is an independent model computation, **not** a transitive certification of §13.2, §13.5, the fiber formula in §13.6, or the full project. The 2026-11-03 branched-cover finding is **preserved**, not re-opened or represented as new work. Demailly approximation/regularization and the dedicated Bergman, weighted \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remain **deferred-by-user** and were not inspected.

**Actual coverage:** one new proof-level scope check of previously partially visited §13.6.3, contextual smooth-product check in §13.2; **+0 first-visited numbered sections, +0 fully mathematically certified sections**. The current integrated ToC has **25 chapters and 747 numbered sections**. No tests, build, CI, publication, website deployment or formal verification were run.
