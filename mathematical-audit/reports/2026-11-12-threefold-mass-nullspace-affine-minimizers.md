# Affine nullspace of smooth threefold Monge–Ampère mass extrema

**Date:** 2026-11-12. **Finding ID:** \`POME-GAUD-THREEFOLD-MASS-NULLSPACE-AFFINE-001\`. **Severity:** low. **Status:** verified conditional deduction; not a false printed theorem or a claimed proof repair.

**Production main SHA:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Review branch:** \`review/mathematical-audit\`.

## Exact integrated reading anchors

- \`docs/sections/a-gauduchon-variational-volume--curvature-conditions-for-mass-extrema/index.html\`, Git blob \`cedeb939240bded77843daec0292d1a8bde0d2cb\`: Lemma 12.16.1 (source \`non-kahler-pluripotential-theory:5C8E3A8A\`, permanent tag \`744D35F9BE16\`), physical lines 17–46; Proposition 12.16.2 (permanent \`CE7BE3992C5F\`), lines 51–68; Theorem 12.16.3 (source \`non-kahler-pluripotential-theory:F297E7B1\`, permanent \`26629526444F\`), lines 76–103; equation 12.16.4 (source \`non-kahler-pluripotential-theory:10BBB84F\`, permanent \`D5CA82478984\`), lines 94–102.
- \`docs/sections/unbounded-mass-on-hopf-manifolds/index.html\`, Git blob \`f53618e8d808de21687ff9166971cb9302ea8cfb\`: identity 23.1.3 (permanent \`25275E5CD565\`), lines 33–55; Proposition 23.1.4 / mass formula 23.1.5 (permanent \`DDEBFFAFCD1F\` / \`C46F0B405DC2\`), lines 74–77; **already printed** Proposition 23.1.38 (permanent \`E42306969D71\`), lines 693–727, which characterizes Hopf minimum-mass bounded potentials by fiber pullbacks. The Hopf classification is crosschecked, **not claimed as a new result**.

## New general conclusion and precise hypotheses

Let \((X,\omega)\) be a **connected compact complex threefold** with a smooth Hermitian form. Write
\[
 \mathcal H_\omega=\{v\in C^\infty(X,\mathbb R):\omega+dd^c v>0\},\qquad
 M(v)=\int_X(\omega+dd^c v)^3.
\]
Assume **there exists** \(v_0\in\mathcal H_\omega\) for which \(\Omega_0=\omega+dd^c v_0\) is Gauduchon, and that the smooth \((2,2)\)-form
\[
 T=-dd^c\omega
\]
is semipositive in the sense of Lemma 12.16.1. This is an existence hypothesis, **not** an assertion that every Hermitian background admits such a potential. Define the nonnegative quadratic form
\[
 Q_T(f)=\int_X df\wedge d^cf\wedge T,\qquad
 \mathcal N_T=\{f\in C^\infty(X,\mathbb R):Q_T(f)=0\}.
\]
Then:

1. **Exact identity and complete equality classification:** for every \(f\) such that \(v_0+f\in\mathcal H_\omega\),
   \[
   M(v_0+f)-M(v_0)=3Q_T(f).
   \]
   The **entire smooth minimizing locus** is exactly
   \[
   \boxed{\operatorname{Argmin}_{\mathcal H_\omega}M
       = (v_0+\mathcal N_T)\cap\mathcal H_\omega .}
   \]
   It is the relatively open convex part of a fixed affine linear subspace: it may be much larger than the constants.

2. **Pointwise characterization:** \(Q_T(f)=0\) if and only if the nonnegative continuous top-degree form \(df\wedge d^cf\wedge T\) vanishes **at every point**. Equivalently the \((1,0)\)-component \(\partial f(x)\) belongs to the radical of the positive semidefinite Hermitian quadratic form on covectors induced by \(T_x\), for each \(x\). Thus \(\mathcal N_T\) is a real vector space (no constant-rank or integrability hypothesis on the radical is needed).

3. **Sharp sufficient rigidity and nonrigidity criteria:** if \(T\) is positive definite on a dense open subset of \(X\), then \(\mathcal N_T=\mathbb R\) and the minimizer is unique **up to constants**. Conversely, if \(T\equiv0\) on any nonempty open set \(U\subset X\), every sufficiently small real \(f\in C_c^\infty(U)\) gives another smooth minimizer; the minimizing locus is locally infinite-dimensional. These are sufficient conditions in different directions, **not** an exhaustive iff classification.

4. **Quantitative conditional stability:** if \(T\) is **uniformly positive definite** on \(X\), then for every auxiliary fixed Hermitian norm/volume and the associated Poincaré constant there is \(c>0\) such that
   \[
   M(v_0+f)-M(v_0)\ge c\|f-\overline f\|_{L^2}^2
   \]
   for every admissible \(f\), with \(\overline f\) its volume mean. No claim is made that the uniform-positivity hypothesis occurs for all Hermitian metrics.

The same conclusions for smooth **maximizers** follow after replacing \(T=-dd^c\omega\) with \(T=+dd^c\omega\) when the latter is semipositive and a Gauduchon smooth maximizer exists.

## Complete derivation, avoiding all excluded regularization

Set \(A=dd^cf\). Expanding the cube,
\[
 M(v_0+f)-M(v_0)
  =3\!\int_X A\wedge\Omega_0^2+
    3\!\int_X A^2\wedge\Omega_0+\int_X A^3.
\]
The first integral is zero by Stokes and \(dd^c(\Omega_0^2)=0\). The last is zero since \(A=dd^cf\) is exact and closed. A second integration by parts, with the same \(d^c\) convention as the integrated reading edition, gives
\[
 \int_X (dd^cf)^2\wedge\Omega_0
       =-\int_X df\wedge d^cf\wedge dd^c\Omega_0
       =\int_X df\wedge d^cf\wedge T,
\]
because \(dd^c\Omega_0=dd^c\omega\). This rederives precisely the printed formula 12.16.4 without any approximation theorem.

For real \(f\), \(df\wedge d^cf\) is a fixed positive multiple of \(i\partial f\wedge\bar\partial f\). The positivity of \(T\) therefore gives a pointwise nonnegative continuous top form and \(Q_T(f)\ge0\). Its integral is zero exactly when it vanishes everywhere. In any local holomorphic frame the scalar density of this form is a positive multiple of \(a_x(\partial f,\partial f)\) for a positive semidefinite Hermitian form \(a_x\); its zero set is the radical of \(a_x\). In particular, if \(f,g\in\mathcal N_T\), then \(\partial f,\partial g\) lie in this radical at each point, as does every real linear combination: \(\mathcal N_T\) is linear. The identity proves the displayed full equality locus for every admissible perturbation, not just infinitesimally.

Where \(T\) is positive definite, \(\partial f=0\) for any \(f\in\mathcal N_T\). If these points are dense, continuity of \(df\) forces \(df=0\) everywhere, so connectedness gives constants. If \(T=0\) on \(U\), smooth compactly supported functions there have \(Q_T=0\), and the strict positivity of \(\Omega_0\) on compact \(X\) guarantees admissibility for sufficiently small \(C^2\) perturbations. Under uniform strict positivity, compactness gives \(Q_T(f)\ge c_1\int|\nabla f|^2dV\); the standard Poincaré inequality yields the displayed \(L^2\) estimate. All of these arguments are finite-dimensional pointwise positivity or smooth Stokes computations.

## Checks, distinction from previous work and dependencies

On the **already printed** scalar Hopf threefold, §23.1.3 states \(dd^c\omega=-\alpha^2\) for \(\alpha=\pi^*\omega_{\rm FS}\). The nullspace of \(Q_{\alpha^2}\) consists of fiber-constant functions; this agrees with the **pre-existing** exact mass identity §23.1.5 and full bounded-minimizer characterization in Proposition 23.1.38. We do **not** log that special-case classification as new. The new scope is the abstract equality-locus theorem for **arbitrary** smooth compact complex threefold backgrounds satisfying the displayed hypotheses, including radical distributions of variable rank and non-Hopf geometry.

**Status boundary:** the equality classification is a fully justified consequence **conditional on existence of a positive Gauduchon representative \(v_0\)**. It does not prove that existence, does not certify all of §12.16 or §23.1, and does not invoke the general identification of smooth mass extrema with \(v_\pm\): the latter in §12.15.4 uses user-excluded regularization. The prior findings (including the older §12.16 optimizer characterization and the printed Hopf fiber-minimum theorem) retain their original statuses.

**Proposed correction/addition:** optional equality-case corollary immediately following §12.16.4, explicitly describing the affine kernel and distinguishing uniqueness from existence. This is **not** a required repair of an erroneous printed theorem. **Affected dependents:** use of §12.16.3 in Gauduchon mass optimizer uniqueness claims, interpretation of §23.1.5 and §23.1.38, and smooth-only extremal stability estimates. No modification of the reading edition, body, source, permanent tags, main, CI, or website is authorized by this report.

**Actual coverage:** selected additional proof-level §§12.16.1–3 / equation 12.16.4 and contextual §§23.1.3–5,23.1.38; both sections were previously partly reviewed. **0** first proof-level numbered-section visits, **0** full mathematically certified numbered sections (ToC remains **25 chapters, 747 numbered sections**). No build, project test, GitHub Actions, formal verification, or publication performed. All excluded Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss work remains **deferred-by-user**, neither resolved nor certified.
