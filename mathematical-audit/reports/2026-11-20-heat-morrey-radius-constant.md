# 2026-11-20 — Chapter 3, §3.10: the radius parameter in the Morrey-to-heat bound

**Finding ID:** POME-HEAT-MORREY-RADIUS-UNIFORMITY-001
**Severity:** medium (the constant is used in analytic estimates).
**Status:** **confirmed error in the claimed metric-only uniformity of the constant**; **verified repair** by allowing radius dependence. This is **not** a counterexample to the numerical inequality for one *fixed* positive cutoff radius.
**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
**Integrated reading edition:** \`docs/sections/heat-kernels-on-compact-manifolds/index.html\`, blob \`c59a1b3fab9433f1aae95db99adb4821857b5d8d\`.
**Anchors:** section conventions physical line 7; Lemma **3.10.5** physical lines **85–105**, source label \`transcendental-positive-cones:DD00B1CA\`, permanent tag \`56A174D59425\`; preceding Gaussian **Lemma 3.10.1** lines **10–80**, source \`transcendental-positive-cones:327DDB8B\`, permanent \`126365F8EBD6\`. The entire mathematical §3.10, physical lines **7–108**, was directly reviewed; the elliptic/spectral prerequisites cited at line 20 were not transitively certified.

## The quantifier that fails

Line 7 says that the constants in the heat estimates depend on the **fixed metrics**, not the heat time. Lemma 3.10.5 then assumes a finite positive measure on a compact Riemannian \(m\)-manifold, \(m\ge2\), and
\[
 \rho(B_r(x))\le A r^{m-2}
 \qquad(x\in X,\quad 0<r\le r_0),
\]
and displays
\[
 \|h_t\rho\|_\infty\le C\,(A+\rho(X))/t,\qquad 0<t\le1. \tag{*}
\]
There is no *metric-only* constant \(C\) working simultaneously for all \(r_0>0\) when \(m>2\). A constant depending on a **fixed** \(r_0\) is legitimate and preserves the analytic applications with a common radius.

### Explicit counterexample to uniformity

Use the standard flat three-torus \(X=\mathbb R^3/\mathbb Z^3\). For \(0<\delta<1/10\), let \(\rho_\delta\) be normalized Euclidean volume on the embedded ball \(B_\delta(0)\). Set
\[
 r_{0,\delta}=\delta^2,\qquad A_\delta=\delta,\qquad t_\delta=\delta^2.
\]
For every center \(x\) and \(0<r\le\delta^2\), the intersection estimate for Euclidean balls gives
\[
 \rho_\delta(B_r(x))
 \le \frac{\operatorname{vol}(B_r)}{\operatorname{vol}(B_\delta)}
 =\frac{r^3}{\delta^3}
 \le\delta r=A_\delta r^{m-2},
 \qquad \rho_\delta(X)=1.
\]
Thus the *exact* original hypotheses hold with a common background metric and with \(A_\delta\to0\).

The scalar heat kernel on this torus is the positive periodization
\[
 h_t(0,y)=(4\pi t)^{-3/2}
    \sum_{k\in\mathbb Z^3}\exp\!\left(-\frac{|y+k|^2}{4t}\right).
\]
For \(t=\delta^2\) and \(y\in B_\delta(0)\), retaining the \(k=0\) summand gives
\[
 h_{\delta^2}(0,y)\ge (4\pi)^{-3/2}e^{-1/4}\delta^{-3}
 =c_0\delta^{-3}.
\]
Therefore
\[
 t_\delta(h_{t_\delta}\rho_\delta)(0)
 \ge c_0\delta^{-1}\longrightarrow+\infty.
\]
If (*) had a constant depending **only on the fixed flat metric**, its right side, multiplied by \(t_\delta\), would be \(C(A_\delta+\rho_\delta(X))=C(1+\delta)\), a contradiction. This is a full counterexample to that *uniformity assertion*, not to the fixed-\(r_0\) version.

## Explicit correction and proof

Put \(r_*=\min\{r_0,1\}\). The same Gaussian hypothesis as Lemma 3.10.1 yields a parameter-explicit bound
\[
 \boxed{\quad
 0\le h_t\rho(x)\le
 \frac{C_{X,g}}{t}
 \Big(A+\bigl(1+r_*^{\,2-m}\bigr)\rho(X)\Big),
 \qquad 0<t\le1,\ m\ge2 .
 \quad} \tag{**}
\]
Here \(C_{X,g}\) depends only on the fixed Riemannian metric; the \(\rho(X)\)-coefficient records the otherwise suppressed cutoff-radius dependence. For \(m=2\), \(r_*^{2-m}=1\), so a metric-only constant is sufficient.

For \(0<t<r_*^2\), sum the Gaussian bound over the inner ball \(B_{\sqrt t}(x)\) and dyadic annuli whose outer radii are at most \(r_*\). The growth hypothesis bounds their contribution by
\[
 C A t^{-1}\sum_{j\ge0}
 2^{(j+1)(m-2)}e^{-c4^j}\le C'A/t.
\]
The residual region outside \(B_{r_*/2}(x)\) contributes at most
\[
 C t^{-m/2}e^{-c r_*^2/t}\rho(X)
 \le C' r_*^{2-m}\rho(X)/t,
\]
since \(s^{m/2-1}e^{-cs}\) is bounded for \(s>0\). For \(t\ge r_*^2\), the global Gaussian upper bound directly gives
\[
 \|h_t\rho\|_\infty\le Ct^{-m/2}\rho(X)
 \le C r_*^{2-m}\rho(X)/t.
\]
This proves (**). In particular, for every **fixed** \(r_0>0\), the displayed estimate of Lemma 3.10.5 remains true with \(C=C(X,g,r_0)\).

The final statement of Lemma 3.10.5,
\[
 t\int_X(h_t\rho)F\,dV\to0
 \quad(F\ge0,\ F\in L^1(X,dV)\text{ fixed}),
\]
also **remains valid**: with \(r_0\) fixed, (**) gives a finite uniform bound on \(t h_t\rho\); splitting \(F\) at level \(M\), applying heat mass conservation to the bounded part and then sending \(M\to\infty\) proves the asserted limit exactly as in physical lines 99–105. No theorem involving a fixed growth radius is refuted.

## Dependency and duplication control

This radius-quantifier issue is **not** the already logged codimension-two \(L^\infty\) endpoint or the fixed-\(F\) \(L^1\) limit. The existing [2026-11-03 Frostman audit](2026-11-03-critical-frostman-heat-smoothing-and-ae-decay.md) correctly writes \(C_{g,r_0,s}\), but did not give the present family disproving the stronger **metric-only** claim made in the integrated conventions. The separate [2026-11-06 endpoint audit](2026-11-06-flat-torus-codimension-two-heat-endpoint.md) is unchanged.

**Proposed production patch (not made here):** explicitly state in Lemma 3.10.5 that \(C\) may depend on \(r_0\), or replace (*) by (**), and qualify the global line-7 constant convention accordingly. Preserve the lemma's source attribution, source label and permanent tag. Any downstream family with \(r_{0,\alpha}\to0\) requires checking whether a uniform heat estimate was used; no such downstream failure is asserted without directly inspecting that proof. The Gaussian estimate, elliptic inputs and any later uses are not declared fully certified.

**Scope:** +1 complete direct integrated section (§3.10), +0 complete upstream proof-chain certifications; previously reported partial §3.10 visits remain historical and are not counted as first visits. No tests/builds/CI were run. All user-excluded regularization, Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss work remains **deferred-by-user**, not repaired or certified.
