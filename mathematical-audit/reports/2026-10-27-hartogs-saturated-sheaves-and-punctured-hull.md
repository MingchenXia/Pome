# 2026-10-27 — Saturated Hartogs extension, codimension, and an exact punctured holomorphic hull

**Review target:** <code>main</code> at <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code>.
**Review branch:** <code>review/mathematical-audit</code>.
**New direct selected coverage:** §9.13, specifically Proposition 9.13.1 and Theorem 9.13.2. **Incremental selected coverage:** §9.72, namely the precise force and limits of Lemma 9.72.1. §9.71 was read as a contextual dependency only. This is neither a chapter certification nor a certification of all upstream results. The previously selected §§9.71–9.73 coverage is retained and is not counted as newly opened sections.

The three findings below are **verified conditional deductions** or exact counterexamples to *stronger, unstated claims*. They do **not** identify a false printed theorem. The counterexamples have elementary, independent proofs, rather than depending on the general theorems being illustrated.

## POME-HARTOGS-SATURATED-NONBUNDLE-001 — Codimension-two saturated extension need not be a subbundle

**Status:** verified conditional deduction. **Severity:** low (sharpness and exposition).
**Exact reading-edition source:** <code>docs/sections/projective-hartogs-extension/index.html</code>, blob <code>3191443b49a20377356f519b5e98ec29259f1c7c</code>; Lemma 9.72.1, stable source label <code>cao-paun-foliations:FF53288F</code>, permanent tag <code>0A2146B324EB</code>, physical lines 9–18, especially line 17. The printed assertion is a *unique saturated coherent extension*, not an extension as a vector subbundle.

**Exact example.** Let \(U=\Delta^2\) with coordinates \(z,w\), let \(A=\{(0,0)\}\) (complex codimension two), and let \(\mathcal E=\mathcal O_U^{\oplus2}\). On \(U^\circ=U\setminus A\) define
\[
  \mathcal F^\circ=\mathcal O_{U^\circ}\cdot(z,w)
  \subseteq\mathcal O_{U^\circ}^{\oplus2}.
\]
Since \((z,w)\neq(0,0)\) on \(U^\circ\), this is a *holomorphic line subbundle*. The unique saturated extension is
\[
  \mathcal F=\mathcal O_U\cdot(z,w)\subseteq\mathcal O_U^{\oplus2}.
\]

**Proof of saturation and failure of local splitting.** Consider the sheaf morphism
\[
  q:\mathcal O_U^{\oplus2}\longrightarrow (z,w)\mathcal O_U,\qquad
  q(a,b)=zb-wa .
\]
It is surjective because \(q(0,1)=z\), \(q(-1,0)=w\). Its kernel is exactly \(\mathcal O_U(z,w)\): from \(zb=wa\) and the relative primality of \(z,w\) in the regular local ring \(\mathbb C\{z,w\}\), one gets \(a=zc,\ b=wc\); the same assertion is immediate away from the origin. Hence
\[
  0\longrightarrow\mathcal O_U
    \xrightarrow{\,c\mapsto(zc,wc)\,}\mathcal O_U^{\oplus2}
    \xrightarrow{\,q\,}\mathfrak m_0=(z,w)\mathcal O_U
    \longrightarrow0
\]
is exact. The ideal \(\mathfrak m_0\) is torsion-free, so \(\mathcal F\) is saturated. However \(\mathfrak m_0\) is not locally free at the origin: it has generic rank one, while its minimal number of generators there is two, because \(\dim_{\mathbb C}\mathfrak m_0/\mathfrak m_0^2=2\). Thus \(\mathcal F\) is not a vector subbundle of \(\mathcal E\) at the origin. Equivalently, a subbundle extension would give a holomorphic extension of
\[
  U^\circ\longrightarrow\mathbb P^1,\qquad(z,w)\longmapsto[z:w],
\]
which is impossible: the limiting values along \(w=0\) and \(z=0\) are \([1:0]\) and \([0:1]\), respectively. Nevertheless \([z:w]\) is meromorphic on \(U\), exactly as the printed lemma asserts.

**Proposed addition:** an optional example distinguishing coherent saturated extension from extension as a locally split subbundle. **Affected dependents:** uses of Lemma 9.72.1 for reflexive sheaves, meromorphic Grassmannian data, and codimension-two extension; none may silently replace “saturated coherent” by “subbundle.”

## POME-HARTOGS-CODIMONE-ESSENTIAL-001 — The codimension hypothesis is indispensable

**Status:** verified conditional deduction. **Severity:** low (sharpness).
**Exact reading-edition source:** the same Lemma 9.72.1, source label/tag and lines 9–18.

**Exact example.** Set \(U=\Delta\), \(A=\{0\}\) (codimension **one**), \(\mathcal E=\mathcal O_U^{\oplus2}\), and on \(U^\circ=\Delta^*\) set
\[
  \mathcal G^\circ=\mathcal O_{\Delta^*}\cdot(1,e^{1/z}).
\]
It is a holomorphic line subbundle with locally free quotient, via
\[
  (a,b)\longmapsto b-e^{1/z}a.
\]
It has **no saturated coherent extension** \(\mathcal G\subseteq\mathcal O_\Delta^{\oplus2}\). Indeed a coherent rank-one extension would have a local nonzero holomorphic section \((a(z),b(z))\) with \(a\not\equiv0\); on the punctured disc, the meromorphic ratio \(b/a\) would agree with \(e^{1/z}\). The latter has an essential isolated singularity, with infinitely many nonzero negative terms in its Laurent expansion, and is not meromorphic at zero. This is a contradiction. The corresponding projective map \([1:e^{1/z}]\) likewise cannot extend meromorphically. Thus changing “codimension at least two” to “codimension at least one” invalidates *both* conclusions of Lemma 9.72.1.

**Proposed addition:** an optional sharpness example. **Affected dependents:** all projective/Grassmannian meromorphic continuation and saturated sheaf extension steps that require the codimension-two hypothesis. The original printed lemma has the necessary hypothesis.

## POME-HOLOHULL-PUNCTURED-SPHERE-001 — Exact hull and noncompactness on a punctured two-space

**Status:** verified conditional deduction. **Severity:** low (explicit model).
**Exact reading-edition source:** <code>docs/sections/holomorphic-hulls-and-domains-of-holomorphy/index.html</code>, blob <code>f2bbaea02a3b85847acc503b83d0cf4dfa11e9d0</code>, holomorphic-hull definition at physical lines 7–13, Proposition 9.13.1 source <code>klimek-pluripotential-theory:5FBBEDD6</code>, permanent tag <code>36B688C7F361</code>, lines 17–38, and Theorem 9.13.2 source <code>klimek-pluripotential-theory:18A483AD</code>, permanent tag <code>8FBCDB96A2E2</code>, lines 52–89. Directly checked the construction of the smooth psh exhaustion and discrete interpolation (lines 22–38), the homogeneous-power/Cauchy mechanism for arbitrary continuous balanced gauges (74–82), and the Montel/Baire interpolation implication (84–88). No full verification of those external analytic inputs is claimed.

Take \(\Omega=\mathbb C^2\setminus\{0\}\) and the compact three-sphere \(K=\{z\in\mathbb C^2:\|z\|=1\}\). Then
\[
  \boxed{\widehat K_{\Omega}
  =\{z\in\mathbb C^2:0<\|z\|\le1\}.}
\]
**Proof.** Every \(f\in\mathcal O(\Omega)\) extends across the origin: on a small bidisc \(|z|,|w|<r\), choose \(0<\rho<r\) and define, for \(|w|<\rho\),
\[
  F(z,w)=\frac{1}{2\pi i}\int_{|\zeta|=\rho}
           \frac{f(z,\zeta)}{\zeta-w}\,d\zeta .
\]
The integrand is holomorphic near the integration contour even at \(z=0\), so \(F\) is holomorphic in both variables. For every \(z\neq0\), Cauchy's formula in the \(w\)-disc gives \(F(z,w)=f(z,w)\); thus \(F\) is the desired local extension, and gluing yields an entire function on \(\mathbb C^2\). The maximum-modulus principle on the closed unit ball now gives
\(|f(x)|\le\max_K|f|\) whenever \(0<\|x\|\le1\). Conversely, for \(\|x\|>1\) choose the complex-linear function
\[
  \ell_x(y)=\sum_{j=1}^2\frac{\overline{x_j}}{\|x\|}\,y_j.
\]
It has \(\sup_K|\ell_x|=1\) but \(|\ell_x(x)|=\|x\|>1\), excluding every point outside the unit ball. The displayed hull follows.

The hull is closed in \(\Omega\) and bounded in \(\mathbb C^2\), but **not compact in \(\Omega\)**: \((1/j,0)\) has no limit in \(\Omega\). This illustrates why ambient boundedness does not imply holomorphic convexity. The example is distinct from, and does not repeat, the earlier Hartogs-bridge exact-hull construction in §9.30.

**Proposed addition:** an optional exact example under §9.13.2. **Affected dependents:** distinguishing bounded holomorphic hulls from compact hulls in the manifold topology, and the domain-of-holomorphy equivalence. This does not contradict Theorem 9.13.2: \(\Omega\) is not a domain of holomorphy.

## Explicit dependency boundaries and coverage

* §9.71 Lemma 9.71.1, <code>docs/sections/local-projectivity-from-relative-positivity/index.html</code> blob <code>f17614b598855bda6fc15f266135d6fe238638cf</code>, label <code>cao-paun-foliations:4BE67CB0</code>, tag <code>A53CEC220C70</code>, lines 17–36, was rechecked **only** for its properness/evaluation/embedding chain. Its use of Grauert's proper base-change theorem, explicitly at lines 24–30, is a **previously recorded genuine external dependency**, not a new discovery and not certified here. The preceding cohomology vanishing invokes §10.102.1, which belongs to the **user-excluded approximation/L² programme**; the dependency is recorded without re-opening it.
* The general normal meromorphic codimension-two extension input in the proof of §9.72.1 remains an **uncertified internal/external upstream dependency**; the *three elementary model computations above* do not require certifying it.
* §9.73's earlier resolution/model issue has a standing ledger entry and was not reopened.
* The main table of contents contains 747 uniquely numbered sections. §9.13 is upgraded from an unreviewed inventory row to **specified-proposition selected proof inspection**. §§9.71–9.72 had earlier selected coverage; the above new edge examples do not reset or certify them. No complete section/chapter was certified.

**Disposition:** Three new, distinct, low-severity verified conditional deductions; **no newly confirmed false theorem, no claimed repair of an upstream proof gap**. No source/body/registry/canonicalization/permanent-tag changes proposed beyond optional English remarks. No builds, CI, formal verification, website publication, paid services, or excluded Demailly/Bergman/L²/Ohsawa–Takegoshi work.
