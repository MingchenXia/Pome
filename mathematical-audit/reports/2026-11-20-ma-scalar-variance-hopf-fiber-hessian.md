# Mathematical audit — 2026-11-20 — Hermitian scalar variance, trace-free Hessian and Hopf fiber response

**Production main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Scope:** complete direct reading of current §§14.8–14.9, selected smooth upstream proofs only. No chapter-wide or transitive dependency certification. The user-excluded Demailly approximation/regularization and the dedicated Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes are **deferred-by-user**; none were reopened.

## Integrated reading edition, statement anchors and status

- §14.8 *Variation of the normalization scalar*: <code>docs/sections/smooth-monge-ampere-equations--variation-of-the-normalization-scalar/index.html</code>, blob <code>34526fcac6d5f30e71a98cadc88a4c76817546c4</code>, directly examined mathematical lines **5–70**. Theorem 14.8.1: source <code>non-kahler-pluripotential-theory:C70BE558</code>, permanent <code>C611B2CA264A</code>, lines 14–48; combined derivative display source <code>4CC64AAD</code> / permanent <code>11F81D837A44</code>, lines 15–17; Corollary 14.8.4 source <code>E5122287</code> / permanent <code>B9C312CB7069</code>, lines 53–64. The extra formula at line 70 source <code>3CBF8D7E</code> / permanent <code>578022E3660A</code> was **already logged** as <code>POME-MA-SECOND-VARIATION-RENDER-DUPLICATE-001</code> on 2026-11-06: not a new finding.
- §14.9 *Normalization on the Hopf threefold*: <code>docs/sections/smooth-monge-ampere-equations--normalization-on-the-hopf-threefold/index.html</code>, blob <code>a0c390cff1768118798824a64318c416636b9b91</code>, directly examined mathematical lines **5–105**. Proposition 14.9.1 source <code>non-kahler-pluripotential-theory:3F745314</code> / permanent <code>CA9F2EF1D149</code> at lines 26–60; combined equations (14.9.2)–(14.9.3) source <code>A2D2957B</code> / permanent <code>028038652BCC</code> at lines 27–29. Corollary 14.9.4 source <code>B84BD0E3</code> / permanent <code>BFCF1480CC8B</code> at lines 68–99. Independent repeat of (14.9.3) source <code>3586F0DB</code> / permanent <code>9CEA8A3A68F0</code>, line 105.
- Selected dependencies: §14.4 Proposition 14.4.1, <code>docs/sections/smooth-monge-ampere-equations--the-linearized-equation-and-smooth-dependence/index.html</code>, blob <code>2f9ebecbd5bd079eb8573b4bb97df0fb5ab1bdfb</code>, lines 7–39; §23.1 <code>docs/sections/unbounded-mass-on-hopf-manifolds/index.html</code>, blob <code>f53618e8d808de21687ff9166971cb9302ea8cfb</code>, **smooth-only** Proposition 23.1.4 and (23.1.5), lines 46–103, source/permanent equation <code>97C333D9 / C46F0B405DC2</code>; and the smooth fiber Poincaré calculation of Proposition 23.1.38, lines 680–715, source/permanent <code>48EA3D0A / E42306969D71</code> and <code>E385367F / 18B65325175F</code>. The bounded-psh extension in §23.1 is expressly **not** audited or invoked.

## POME-HERMITIAN-SCALAR-VARIANCE-TRACEFREE-001

**Status:** verified conditional deduction. **Severity:** low. **Printed Theorem 14.8.1 remains correct.** This result is different from the **previously recorded** Kähler-only exact variance identity <code>POME-MA-KAHLER-NORMALIZATION-VARIANCE-001</code> (2026-11-06): here the background is a general Hermitian metric, and an explicit trace-free error term persists.

Let X be a connected compact complex n-fold (n≥1), ω a smooth positive Hermitian form (not assumed closed), dV a fixed smooth positive volume form, and F_t a smooth one-parameter family of smooth real logarithmic densities for which the smooth positive Monge–Ampère solutions of (14.1.1) exist. Put η_t=ω+dd^c u_t, let μ_t be the normalized strictly positive smooth **adjoint** probability measure of L_t=tr_{η_t}dd^c, and set

\[
 A_t=\eta_t^{-1}dd^c\dot u_t,\qquad
 A_t^\circ=A_t-\frac{\operatorname{tr}A_t}{n}I,\qquad
 \overline{\dot F}_t=\int_X\dot F_t\,d\mu_t.
\]

The first differentiated equation, together with the adjoint identity \(\int_X L_t v\,d\mu_t=0\), says

\[
 \operatorname{tr}A_t=L_t\dot u_t=\dot F_t+\dot b_t
 =\dot F_t-\overline{\dot F}_t .
\]

The matrix A_t is Hermitian relative to η_t. Orthogonality of its scalar and trace-free components gives the pointwise **identity** (not only an estimate)

\[
 \operatorname{tr}(A_t^2)
  =\frac{(\operatorname{tr}A_t)^2}{n}
    +\operatorname{tr}\bigl((A_t^\circ)^2\bigr).
\]

Substituting this into the *printed* second-variation formula (14.8.3) yields

\[
 \boxed{
 -\ddot b_t-\int_X\ddot F_t\,d\mu_t
 =\frac{1}{n}\operatorname{Var}_{\mu_t}(\dot F_t)
  +\int_X\lVert A_t^\circ\rVert_{\mathrm{HS},\eta_t}^{2}\,d\mu_t.}
 \tag{A}
\]

The proof does not differentiate μ_t; the adjoint equation is applied at a fixed t. For an affine path F_t=F_0+tG, it follows that

\[
 -b''(F_0+tG)\geq \frac1n\operatorname{Var}_{\mu_t}(G),
 \tag{B}
\]
and the difference is *exactly* the integral of the trace-free complex Hessian square. The right side is positive whenever G is nonconstant, since μ_t has full support. This proves strict concavity in every nonconstant direction without requiring dω=0.

**Uniform quantitative chord version.** Fix a smooth probability measure ν on X. Along the compact parameter segment t∈[0,1], continuity and strict positivity of the smooth densities give

\[
 m=\min_{t\in[0,1],\,x\in X}\frac{d\mu_t}{d\nu}(x)>0.
\]
The variational characterization \(\operatorname{Var}_{\mu}(G)=\inf_{c\in\mathbb R}\int(G-c)^2d\mu\) implies \(\operatorname{Var}_{\mu_t}(G)\geq m\operatorname{Var}_\nu(G)\). Thus integrating (B), or subtracting the matching quadratic with second derivative \(-m\operatorname{Var}_\nu(G)/n\), gives for 0≤t≤1,

\[
 \boxed{b(F_0+tG)\ \geq\
 (1-t)b(F_0)+t\,b(F_0+G)
 +\frac{m}{2n}t(1-t)\operatorname{Var}_\nu(G).}
 \tag{C}
\]

The constant m is **segment-dependent**; there is no claimed global uniform modulus over all smooth data. Equality in the pointwise spectral inequality occurs precisely where \(A_t^\circ=0\); no assertion of universal attainment is made. The previously proved Kähler identity may improve the factor 1/n to 1 *after integration* for closed ω, but this is neither used nor recounted as new.

**Proposed correction:** optional audit-only addition (A)–(C) after Theorem 14.8.1, explicitly stating adjoint measures and compactness of the data segment; do not change source/body or canonical tags. **Dependents:** §§14.8–14.9, scalar comparison under Hermitian backgrounds, and any quantitative stability argument based on adjoint probability measures.

## POME-HOPF-FIBER-ENERGY-VARIANCE-001

**Status:** verified conditional deduction. **Severity:** low. Printed Proposition 14.9.1 and Corollary 14.9.4 remain correct. This is a quantitative comparison between their fiber energy and the Hermitian scalar Hessian, not a repetition of the Kähler-only variance formula or the existing fiber Poincaré bound.

Assume the *specific* Hopf threefold and Gauduchon metric of §23.1. Its normalized volume \(\nu=\omega^3/6\) is a probability measure and is the adjoint measure for L_0 at the zero potential. Let G∈C^\infty(X,\mathbb R), set \(\bar G=\int_XG\,d\nu\), and let v be the zero-ν-mean solution of

\[
 L_0v=G-\bar G,\qquad
 L_0v=3\,dd^cv\wedge\omega^2/\omega^3.
\]

Set \(A=\omega^{-1}dd^cv\), \(A^\circ=A-\frac13(\operatorname{tr}A)I\), and \(Q(G)=\int_X|v_w|^2d\nu\). In §14.9, \(D(F)=b(F)+\log\int e^F d\nu\); the *printed* Corollary 14.9.4 gives \(D''(0;G,G)=2Q(G)\). The first and second derivatives of \(\log\int e^{tG}d\nu\) at zero are \(\bar G\) and \(\operatorname{Var}_{\nu}(G)\), while the *printed* (14.8.3) gives \(b''(0;G,G)=-\int\operatorname{tr}(A^2)d\nu\). Consequently,

\[
 \boxed{2Q(G)+\int_X\operatorname{tr}(A^2)d\nu
          =\operatorname{Var}_{\nu}(G).}
 \tag{D}
\]

Using \(\operatorname{tr}A=G-\bar G\) and the scalar/trace-free decomposition for n=3 gives the stronger exact balance

\[
 \boxed{2Q(G)+\int_X\lVert A^\circ\rVert_{\rm HS,\omega}^2d\nu
          =\frac23\,\operatorname{Var}_{\nu}(G).}
 \tag{E}
\]

Both terms on the left are nonnegative, so

\[
 \boxed{0\leq\int_X|v_w|^2d\nu\leq
        \frac13\operatorname{Var}_\nu(G),\qquad
        0\leq\int_X\lVert A^\circ\rVert^2d\nu
                 \leq\frac23\operatorname{Var}_\nu(G).}
 \tag{F}
\]

The second upper constant is **attained for every nonconstant smooth base pullback** \(G=\pi^*H\): printed Corollary 14.9.4 gives Q(G)=0, so (E) yields equality with positive variance. **No claim that the first constant 1/3 is globally optimal is made.** The lower fiber-energy equality is precisely the base-pullback case by that corollary. This quantifies the competition between variation along elliptic fibers and the trace-free ambient complex Hessian; it makes no claim of global convexity of D.

Cross-check: the smooth identity (23.1.5), the normalization \(\int\omega^3=6\), the elliptic-fiber averaging measure, and the smooth Fourier Poincaré factor in (23.1.39) agree with (14.9.2)–(14.9.3). The proof of (D)–(F) only needs the smooth instances; it neither requires nor reopens the excluded bounded-regularization argument in the latter §23.1 proof.

**Proposed correction:** optionally state (D)–(F) after Corollary 14.9.4. **Dependents:** §14.9 scalar and fiber estimates, §23.1 smooth Hopf mass/fiber-energy comparisons, other smooth perturbative arguments on this Hopf background.

## POME-HOPF-SECOND-VARIATION-VISIBLE-DUPLICATE-001

**Status:** genuine duplication (independent reading-edition display, not false mathematics). **Severity:** low. In §14.9 the line-29 combined tagged display contains (14.9.2) and (14.9.3). Line **105**, after the exposition, creates a second visible reading-chunk of precisely the same (14.9.3), under *different* source and permanent tags <code>non-kahler-pluripotential-theory:3586F0DB</code> / <code>9CEA8A3A68F0</code>. The second display wraps a full <code>align</code> inside <code>aligned</code>. The same type of defect in §14.8.3 was already logged on 2026-11-06; **that older instance is not a new finding**.

**Proposed correction:** in a future separately reviewable rendering/registry patch, show the mathematical formula once and retain both source identities, permanent tags and permalinks through an alias or link; do not conflate the tagged provenance. Nested math syntax is suspect, but no MathJax or browser rendering test was executed, so a frontend failure is only a candidate consequence. **Affected:** §14.9 continuous reader, standalone equation navigation/citation/search and any downstream exact-link consumers.

## Boundaries and status

New direct complete section readings: **2 (§14.8, §14.9)**; previously logged selected §14.8 work remains recorded and is not a new first-ever visit. Selected upstream mathematical checks: **§14.4 and the smooth-only parts of §23.1**; full upstream proof-chain certificates **0**. No new confirmed mathematically false printed theorem. No software tests, builds, CI, publication, source/body/registry changes, PR creation or merge. This report contains only public, reproducible mathematical reasoning. The 25-chapter/747-section inventory is unchanged and is not a full-project verification.
