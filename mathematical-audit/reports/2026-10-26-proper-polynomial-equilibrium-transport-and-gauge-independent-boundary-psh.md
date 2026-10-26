# Pome mathematical audit: finite polynomial transport of equilibrium measures and gauge-independent boundary-distance exhaustions

**Date:** 26 October 2026. **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting audit head:** fb3f1a07c6791d6b269e32527f17fa490a82412a.

**Actual selected proof-level scope:** §16.32 (global extremals under proper polynomial maps; the raw/upper-regularized distinction; the local-map hypothesis warnings) and §9.14 (PSH hulls, directional boundary distances, sublevels of PSH functions). Context-only: §9.13.2's definition and elementary estimates for continuous complex-homogeneous distance gauges. Not all arguments or upstream dependencies have been independently certified. The already existing POME-HULL-JET-INTERP-001 at §9.13 is **not** counted as a new finding.

**Strict exclusion:** No Demailly approximation/regularization, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas or positivity-loss proof-completion work was inspected, re-run, extended or reclassified. Earlier items remain **deferred-by-user**.

## POME-PROPER-POLY-EQUILIBRIUM-PUSH-001

**Status:** verified conditional deduction, **severity:** low. Not a false printed theorem or a repair to its proof.

**Exact integrated source:** <code>docs/sections/maps-and-regularity-of-global-extremals/index.html</code>, main blob <code>b20154011d37d46a4d0cc7751863207e5debf183</code>. Theorem 16.32.1, source label <code>klimek-pluripotential-theory-B04DEE23</code>, permanent tag <code>68FB8247AB5A</code>, lines 10–35; comparison and local/nonproper limitations in Theorem 16.32.5, source label <code>klimek-pluripotential-theory-159C639B</code>, tag <code>15FA5C21941D</code>, lines 94–127, and Example 16.32.6, tag <code>446A0A9CF0BF</code>, lines 129–133.

### Claim and hypotheses

Let \(f:\mathbb C^n\to\mathbb C^n\) be polynomial, of degree \(d\ge1\), such that its degree-\(d\) homogeneous part \(f_d\) has no common zero outside the origin. Let \(E\subset\mathbb C^n\) be **bounded and non-pluripolar**. Write \(V_E\) for the raw Siciak extremal and \(V_E^*\) for its upper-semicontinuous regularization. Then

\[
\boxed{V_{f^{-1}E}^*=\frac1d V_E^*\circ f.}
\tag{1}
\]

Both sides are locally bounded plurisubharmonic functions. Their classical top-degree Bedford–Taylor measures satisfy the **exact push-forward equality**

\[
\boxed{
f_*\bigl(dd^cV_{f^{-1}E}^*\bigr)^n
=\bigl(dd^cV_E^*\bigr)^n.
}
\tag{2}
\]

Furthermore, at every \(x\in f^{-1}E\), local \(L\)-regularity is equivalent on source and target:

\[
\boxed{
E \text{ is \(L\)-regular at \(f(x)\)}
\quad\Longleftrightarrow\quad
f^{-1}E \text{ is \(L\)-regular at \(x\)}.
}
\tag{3}
\]

This includes points lying above the critical-value locus. It does **not** extend to arbitrary nonproper or only locally defined holomorphic maps.

### Proof

**Step 1 (raw and starred extremals).** Theorem 16.32.1 supplies the exact raw identity
\(V_E\circ f=dV_{f^{-1}E}\). Its leading-homogeneous hypothesis implies that \(f\) is proper, finite, surjective and open. For any locally upper-bounded function \(u\) and any continuous open map \(f\), neighborhood suprema show
\[
(u\circ f)^*=u^*\circ f:
\qquad
\inf_{U\ni x}\sup_{f(U)}u
=
\inf_{W\ni f(x)}\sup_W u.
\]
For the first infimum, \(f(U)\) is a neighborhood of \(f(x)\); for the reverse direction, continuity lets \(U\) be chosen inside \(f^{-1}(W)\). Taking upper regularizations of the raw equality proves (1).

For bounded non-pluripolar \(E\), \(V_E^*\) belongs to the usual logarithmic-growth class, is finite and nonnegative, hence locally bounded. The same holds for its composition in (1), so both Bedford–Taylor measures exist. No singular-metric or Demailly approximation input is invoked.

**Step 2 (the exact number of generic sheets).** Homogenize \(f\) to
\[
F([Z_0:Z])=
[Z_0^d:Z_0^d f_1(Z/Z_0):\cdots:Z_0^d f_n(Z/Z_0)]
\colon\mathbb P^n\longrightarrow\mathbb P^n.
\]
The right side extends across \(Z_0=0\) because \(f_d^{-1}(0)=\{0\}\); on infinity it is \([0:f_d(Z)]\). This morphism satisfies
\(F^*\mathcal O_{\mathbb P^n}(1)\simeq\mathcal O_{\mathbb P^n}(d)\).
For the hyperplane class \(H\), the cohomological degree calculation gives
\[
\deg_{\mathrm{top}}F
=\frac{\int_{\mathbb P^n}F^*(H^n)}{\int_{\mathbb P^n}H^n}
=d^n.
\]
Since the first coordinate of \(F\) is \(Z_0^d\), no affine point has a preimage at infinity. Therefore \(f\) has exactly \(d^n\) preimages over each point outside its proper analytic critical-value set \(S\), counted without multiplicity there. This is a **generic** sheet count; no assertion of \(d^n\) distinct points above a branch value is made.

**Step 3 (measure push-forward, including branch values).** Put \(u=V_E^*\), \(\mu=(dd^cu)^n\), \(\nu=(dd^c(u\circ f))^n\). On \(\mathbb C^n\setminus S\), \(f\) is a finite unramified covering, and the local biholomorphic covariance of the Bedford–Taylor construction gives
\[
f_*\bigl(\nu|_{f^{-1}(\mathbb C^n\setminus S)}\bigr)
=d^n\,\mu|_{\mathbb C^n\setminus S}.
\]
The analytic sets \(S\) and \(f^{-1}S\) are pluripolar. Monge–Ampère measures of locally bounded PSH functions charge no pluripolar sets, hence neither side has missing mass on these analytic sets. Equation (1) gives
\((dd^cV_{f^{-1}E}^*)^n=d^{-n}\nu\), yielding (2).

This argument does not need a globally defined pullback of arbitrary singular measures at branch points: covariance is used only on the unramified locus, while zero analytic-set mass completes the equality. The projective degree identity and the local Bedford–Taylor covariance are **explicit conditional internal inputs**, not claims to have independently certified every preceding chapter.

**Step 4 (regularity).** At any \(y\in E\), \(V_E(y)=0\) since the zero function is admissible and all competitors are nonpositive on \(E\). Since \(V_E\ge0\), continuity at \(y\) is equivalent to \(V_E^*(y)=0\). The same observation holds for \(f^{-1}E\). Equation (1) now gives (3).

**Concrete normalization check.** For \(n=1\), \(f(z)=z^d\) and \(E=\{|w|\le R\}\), the identity is
\(V_{f^{-1}E}^*(z)=\log^+(|z|/R^{1/d})=d^{-1}\log^+(|z|^d/R)\).
Both equilibrium measures are the normalized angular measure on their respective boundary circles; \(z\mapsto z^d\) sends one to the other. This validates the coefficient \(d^{-n}\) in the higher-dimensional argument, but is not a substitute for Step 3.

### Audit conclusion and proposal

The existing Theorem 16.32.1 is **not refuted**. The proposed optional corollary after it would make explicit that its exact extremal identity also transports top-degree equilibrium measures and gives two-sided \(L\)-regularity at the full inverse image. The hypothesis \(f_d^{-1}(0)=\{0\}\) and properness must not be dropped: the warnings/counterexamples in §16.32.6 concern weaker maps and are compatible with (2)–(3).

Affected dependents: equilibrium measures and pullback under finite maps (§§7.2–7.5 and 13.10), polynomial extremals and local regularity (§§16.31–16.32), polynomially generated models (§16.32.2). They have not all been audited independently.

## POME-BOUNDARY-GAUGE-BOUNDED-PSH-001

**Status:** verified conditional deduction, **severity:** low; not a false printed theorem.

**Exact integrated sources:** <code>docs/sections/plurisubharmonic-hulls-and-general-boundary-distances/index.html</code>, main blob <code>9b491cd7d9fcb7adb3b43c8daf2d8a29a0ed4077</code>; Proposition 9.14.1, source label <code>klimek-pluripotential-theory-DAAFC667</code>, permanent tag <code>D1E020BB8CEA</code>, statement/proof lines 13–42. Its general-gauge definition is in <code>docs/sections/holomorphic-hulls-and-domains-of-holomorphy/index.html</code>, blob <code>f2bbaea02a3b85847acc503b83d0cf4dfa11e9d0</code>, Theorem 9.13.2, source label <code>klimek-pluripotential-theory-18A483AD</code>, tag <code>8FBCDB96A2E2</code>, setup and statement lines 39–56.

### Statement and direct proof

Let \(\Omega\subsetneq\mathbb C^n\) be **nonempty and pseudoconvex**. A distance gauge here is a continuous \(\delta:\mathbb C^n\to[0,\infty)\), positive off \(0\), satisfying \(\delta(tz)=|t|\delta(z)\) for complex \(t\). No triangle inequality, convexity, or Euclidean radial symmetry is assumed.

For any two such gauges \(\delta_1,\delta_2\), compactness of the Euclidean sphere gives constants \(0<a\le b<\infty\) with
\(a\delta_1(\xi)\le\delta_2(\xi)\le b\delta_1(\xi)\) for every \(\xi\).
Taking infima over \(w\notin\Omega\) preserves the inequalities:
\[
a\,\delta_{1,\Omega}(z)\le\delta_{2,\Omega}(z)
\le b\,\delta_{1,\Omega}(z),\qquad z\in\Omega.
\tag{4}
\]
Consequently for \(\Phi_i=-\log\delta_{i,\Omega}\),
\[
\boxed{-\log b\ \le\ \Phi_2-\Phi_1\ \le\ -\log a
\quad\hbox{throughout }\Omega.}
\tag{5}
\]
Both \(\Phi_i\) are continuous PSH by Proposition 9.14.1, **conditionally on its directional Oka argument**. Thus all gauge-defined negative-log boundary-distance potentials agree up to a **globally bounded additive function**; this is not an equality of functions or of Levi forms.

In particular, the explicit continuous PSH exhaustions
\(\rho_i=|z|^2+\max\{0,\Phi_i\}\)
satisfy
\[
\boxed{
\|\rho_2-\rho_1\|_{L^\infty(\Omega)}
\le\max\{|\log a|,|\log b|\}.
}
\tag{6}
\]
This follows because \(t\mapsto\max\{0,t\}\) is 1-Lipschitz. Equation (4) and \(\delta_i\asymp|\cdot|\) also ensure the asserted properness of each \(\rho_i\), even if \(\Omega\) is unbounded.

The estimate is purely scalar; in particular it does **not** give uniform comparison of \(dd^c\Phi_i\), curvature eigenvalues, or complete metric lengths.

### Audit conclusion and proposal

Proposition 9.14.1 is **not refuted**. Suggest an optional quantitative boundary-gauge-independence remark following it. This isolates which part of the pseudoconvex exhaustion construction depends on the auxiliary complex-homogeneous gauge (the bounded term) and which part is canonical (the boundary blow-up rate up to \(O(1)\)). Relevant dependents: hull-compactness arguments, boundary-distance tests and pseudoconvex exhaustion comparisons (§§9.13–9.16).

In §9.14.1, we inspected the supremum-of-directional-submeans step and the continuous-PSH-separator gluing; in §9.14.2 (source label <code>klimek-pluripotential-theory-ADFB854F</code>, tag <code>CE8195E08F54</code>, lines 49–57), we inspected the fixed-compact-boundary and maximum-principle passage for sublevels. The full directional Oka proof is **not independently certified** here. This note does not relabel it as external or erroneous merely because §9.14 cites it as an existing argument.

## Coverage, unresolved obligations and changes made

- §16.32: first selected proof-level reading of 16.32.1–.5 and contextual counterexample 16.32.6, regularity line in 16.32.7, with particular focus on the raw/USC envelope identity, finite proper mapping hypothesis and measure covariance. The complete section, §§16.32.7–.8 and all prior global extremal construction are **not certified**.
- §9.14: first selected proof-level reading of 9.14.1–.2, with gauge and hull-continuity details checked. The full Oka antecedent and its transitive dependencies are **not certified**. §9.13.2 was read only for gauge definitions/quantifiers; earlier jet interpolation finding POME-HULL-JET-INTERP-001 is retained but **not relogged**.
- New IDs are **conditional mathematical deductions**, not confirmed errors, not certified repairs and not full-project verification. No historical finding is closed or downgraded. Preserve all excluded Demailly items as **deferred-by-user**.
- Only this English audit note, <code>mathematical-audit/LATEST.md</code>, <code>LEDGER.md</code>, and the two corresponding rows in <code>SECTION_MATRIX.md</code> are intended to change on <code>review/mathematical-audit</code>. No source/body/registry/permanent tag, main branch, CI, build or website changes; no project tests or formal checks claimed.
