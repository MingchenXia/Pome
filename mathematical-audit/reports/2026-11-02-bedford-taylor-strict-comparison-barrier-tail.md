# Bedford–Taylor comparison: barrier-weighted quantitative estimate and weak-L^n tail

**Date:** 2026-11-02. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Audit branch baseline:** 3d22cf0a27b7c6a50df3f80f987880a6afb945ae.

**Finding:** POME-BT-BARRIER-WEAKLN-001. **Severity:** low. **Status:** verified conditional deduction; not a false printed theorem, confirmed proof gap, applied patch, or full dependency-chain verification.

## Exact integrated reading-edition anchors

- File: docs/sections/bedford-taylor-products-and-local-capacity--decreasing-continuity-and-symmetry/index.html, blob 96a9e39e85fab5774ebdac0c6d9d006338a4e42c.
- Proposition 7.3.10 (locality on a strict maximum region), source foundations-of-pluripotential-theory:0C37DA3F, permanent tag 0453AAB39932, physical lines 279–296.
- Theorem 7.3.11 (bounded-domain comparison), source foundations-of-pluripotential-theory:A7DD3972, permanent tag D0AF90DDC7A5, lines 304–341, particularly compact-support and strict-set steps 314–338.
- Corollary 7.3.12 (domination), source foundations-of-pluripotential-theory:3A1D42EE, permanent tag F2BBEF3BF09B, lines 346–363, particularly mixed-product positivity and the Euclidean density normalization at 356–360.
- Dependence: Bedford–Taylor decreasing weighted continuity Theorem 7.3.7, source foundations-of-pluripotential-theory:8B1F9B78, tag D87C13B3250A, lines 134–229; recursive product positivity Proposition 7.2.2 (tag D9911E035563) and Euclidean normalization equation 7.2.4 (tag 706A589A680C).

This session directly read the complete displayed argument of Theorem 7.3.11, Corollary 7.3.12, and the strictly positive-region localization in Proposition 7.3.10, not just their headings. The section already had selected checks of Theorem 7.3.7; these are **new selected passages**, not new first-section coverage or a whole-section certificate.

## New quantitative deduction

Let D be a bounded open subset of C^n, n≥1. Let u,v be locally bounded plurisubharmonic functions on D, satisfying

\[
\liminf_{D\ni z\to x}(v(z)-u(z))\ge 0\qquad (x\in\partial D).
\]

Let χ be any locally bounded plurisubharmonic function on D with χ≤0, and let δ>0. Define the Borel set E_δ={v<u+δχ}. Then, with Bedford–Taylor products,

\[
\boxed{\delta^n\int_{E_\delta}(dd^c\chi)^n
\ \le\ \int_{\{v<u\}}(dd^cv)^n.}\tag{A}
\]

The right-hand side is allowed to be infinite; the conclusion is informative whenever it is finite. Neither a continuous boundary extension of u,v,χ nor a globally finite Monge–Ampère mass was assumed.

**Proof.** Set b_δ=u+δχ. It is locally bounded and plurisubharmonic. Because χ≤0, the boundary hypothesis gives
\(\liminf(v-b_\delta)\ge\liminf(v-u)\ge0\), and \(E_\delta\subset\{v<u\}\). Apply Theorem 7.3.11 with the ordered pair (a,b)=(v,b_δ):

\[
\int_{E_\delta}(dd^cb_\delta)^n\le\int_{E_\delta}(dd^cv)^n.
\]

Positivity, symmetry, and multilinearity of the bounded Bedford–Taylor mixed products give the **measure inequality**

\[
(dd^cb_\delta)^n
=\sum_{k=0}^n {n\choose k}\delta^k
(dd^cu)^{n-k}\wedge(dd^c\chi)^k
\ \ge\ \delta^n(dd^c\chi)^n.
\]

Combining these two inequalities and the inclusion of Borel sets proves (A). No approximating sequence, non-pluripolar cutoff, regularization, or interchange of limits is needed beyond the printed bounded-product theorem.

**Sharpness of the coefficient 1 in (A).** Take D=B(0,R), \(\rho(z)=|z|^2-R^2<0\), χ=ρ, u=0, and \(v=c\delta\rho\) with c>1. The boundary difference is zero, \(E_\delta=D=\{v<u\}\), and the quotient of the right side of (A) by the left side is exactly \(c^n\to1\) as c↓1. Hence no universal larger left-hand coefficient can hold.

**The sign premise χ≤0 cannot simply be deleted.** With u=v=0 on the unit ball and χ=|z|^2+1>0, the boundary premise for u,v holds and E_δ=D, but the proposed left side is strictly positive while the right side is zero. Thus χ≤0 has a genuine logical role (both maintaining the boundary inequality and ensuring E_δ⊂{v<u}).

## Weak-L^n control of the positive difference

Suppose D⊂B(0,R), R>0, and put \(M=\int_{\{v<u\}}(dd^cv)^n\). Choosing \(\chi(z)=|z|^2-R^2\) and δ=t/R² in (A) gives for every t>0,

\[
\boxed{
t^n\,\mathcal L^{2n}\{z\in D:u(z)-v(z)>t\}
\ \le\ \frac{\pi^n R^{2n}}{n!}\,M .
}\tag{B}
\]

Indeed \(-R^2\le\chi<0\), so \(u-v>t\) implies \(v<u+\delta\chi\); and the Pome convention \(dd^c=i\partial\bar\partial/(2\pi)\) gives \((dd^c|z|^2)^n=(n!/\pi^n)dV_{2n}\). Consequently, if M<∞, \((u-v)_+\) has the displayed weak-L^n tail bound. The constant in (B) is an explicit valid constant, **not claimed optimal**.

The exponent n is forced by homogeneity among estimates of form \(t^p|\{u-v>t\}|\le C M\) with a universal scale-independent C: on B(0,R), u=0 and \(v=c(|z|^2-R^2)\), take \(t=\alpha cR^2\) with fixed 0<α<1. The superlevel volume is independent of c, whereas M is proportional to c^n. Letting c run over (0,∞) rules out any p≠n for this homogeneous estimate.

## Review of the printed argument; limits and scope

Theorem 7.3.11 uses a **compact** exceptional region from its pointwise boundary liminf (finite cover of ∂D), then the compact-support identity for the signed difference \((dd^c\max\{u,v-\varepsilon\})^n-(dd^cu)^n\). On a relatively compact D' containing that region, both masses are finite, so equality of total masses does not rely on globally finite mass on D. Proposition 7.3.10 provides the Borel strict-region localization and the monotone increase of \(\{u<v-\varepsilon\}\) as ε↓0. Corollary 7.3.12 correctly uses a strictly plurisubharmonic quadratic perturbation, all-positive mixed terms and almost-everywhere uniqueness of psh representatives. No new error in these examined steps was established.

**Proposal:** optionally place (A) and (B) as a new quantitative corollary after Corollary 7.3.12, retaining the original statement, proof, source attribution, canonicalization and permanent tags. **Affected conceptual dependents:** local Bedford–Taylor comparison and capacity (§§7.3–7.5), with potential use in quantitative comparison and stability estimates; no downstream theorem is newly certified.

**Unverified scope:** the complete source proof of Theorem 7.3.7 and its earlier current/mass compactness and weighted approximations remain conditional dependencies. This report does **not** certify any complete Pome numbered section, project build, formalization, or the whole capacity theory. The user-excluded Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale and positivity-loss programme remain deferred-by-user, neither examined nor repaired in this run.