# Entropy-dual sublevels: weak compactness does not upgrade to total-variation compactness

**Date:** 2026-11-16. **Finding ID:** `POME-ENTROPY-SUBLEVEL-NONSTRONG-001`. **Severity:** low. **Status:** verified conditional deduction (a fully explicit model computation conditional only on the already printed dual-identification convention); **not** a false printed theorem, proof gap, or applied repair.

## Reviewed reading-edition statements and immutable anchors

Production `main` SHA: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

- `docs/sections/normalization-and-weak-adjoint-measures--a-convex-functional-on-probability-measures/index.html`, blob `9a4ba5a98abd3273a6872c68beccf764e936d3f0`: definition (11.35.1), original source `non-kahler-pluripotential-theory:A5C670F7`, permanent `FFB47018170B`, physical lines 12–14; Theorem 11.35.4, source `:9F623A72`, permanent `6830F8DE9750`, lines 43–82, and (11.35.5), source `:3339FE17`, permanent `FA8EC628AEAE`, lines 49–51.
- `docs/sections/normalization-and-weak-adjoint-measures--entropy-and-the-closed-case/index.html`, blob `0710d0732ae7ef81de3d3d62206a0f9c6b5d321f`: Lemma 11.37.1, source `non-kahler-pluripotential-theory:C2CF0A52`, permanent `2E4E82F8C3FC`, physical lines 19–49; closed-background identity (11.37.2), source `:65FF799F`, permanent `803909FECEC0`, lines 54–61; Proposition 11.37.3, source `:460EAE65`, permanent `33DF3CE1122A`, lines 64–76.
- `docs/sections/normalization-and-weak-adjoint-measures--bounded-measurable-densities-and-stability/index.html`, blob `9c045c6e7a5bc4f0830874030c18dad0cafae905`: Theorem 11.36.1, source `non-kahler-pluripotential-theory:ECDF9BCE`, permanent `99653D7759E2`, lines 5–63, used only for a scope comparison, not as a new proof dependency.

The current section matrix already lists partial coverage of §§11.35–11.37; no first visit is being claimed. In particular, the earlier `POME-CLOSED-LOGPART-SHARP-L1-TV-001` establishes a **different** sharp estimate under *convergence of the logarithmic densities*. Do not re-register it as a new result.

## Explicit torus theorem

Let `X=C/(Z+iZ)`, with global coordinates `x,y mod 1`, and let
\[
 \theta=\mathrm dV=\frac{\mathrm i}{2}\,\mathrm dz\wedge\mathrm d\bar z
 =\mathrm dx\wedge\mathrm dy,\qquad \int_X\theta=1,\qquad \varphi=0.
\]
Use Pome's \(\mathrm dd^{\mathrm c}=(\mathrm i/2\pi)\partial\bar\partial\). Fix \(0<a<1\). For integers \(k\geq1\), set
\[
 h_k(x,y)=1+a\cos(2\pi kx),\quad F_k=\log h_k,\quad
 \nu_k=h_k\,\mathrm dV,\quad
 u_k(x,y)=-\frac{a}{\pi k^2}\cos(2\pi kx).
\]

Then all the following hold simultaneously.

1. Each \(\nu_k\) is a **smooth strictly positive probability**, and is the unique supporting probability \(\mathcal A_0(F_k)\) of (11.37.2). The \(F_k\) are uniformly bounded. More strongly, \(\theta+\mathrm dd^{\mathrm c}u_k=h_k\theta\) and
\[
 (1-a)\theta\leq\theta+\mathrm dd^{\mathrm c}u_k\leq(1+a)\theta,
 \qquad \|u_k\|_{C^1}=O_a(k^{-1}).
\]
Thus even potentials converging in \(C^1\) with a common two-sided curvature bound yield the example.

2. The dual values \(H_0(\nu_k)\) are **exactly constant**:
\[
 H_0(\nu_k)=I(a)
 =1-\sqrt{1-a^2}+
 \log\frac{1+\sqrt{1-a^2}}{2}>0.
\]
Moreover \(I(a)\to0\) as \(a\downarrow0\), with \(I(a)=a^2/4+O(a^4)\). For **every** \(L>0\) one can choose a fixed \(a>0\) with \(I(a)<L\), and the *entire infinite sequence* then lies in the single dual sublevel \(\mathcal K_L=\{H_0\leq L\}\). In the normalized torus case \(\mathcal K_0=\{\mathrm dV\}\).

3. Nevertheless,
\[
 \nu_k\longrightarrow\mathrm dV
 \quad\text{both narrowly and in }\sigma(L^1(\mathrm dV),L^\infty(\mathrm dV)),
\]
while
\[
 \|h_k-1\|_{L^1(\mathrm dV)}=\frac{2a}{\pi},\qquad
 d_{\rm TV}(\nu_k,\mathrm dV)=\frac a\pi
\]
for all \(k\). There is **no \(L^1\)-norm-convergent subsequence** and hence no total-variation-compactness upgrade of Theorem 11.35.4, however small but positive the dual entropy excess \(L\).

## Complete proof for the concrete model

For a smooth torus function \(u\), the stated normalization gives
\[
 \mathrm dd^{\mathrm c}u
 =\frac{\Delta u}{4\pi}\theta.
\]
Our \(u_k\) satisfies \(\Delta u_k=4\pi a\cos(2\pi kx)\). Thus the curvature formula and uniform bounds follow exactly, not asymptotically. Also \(\int_Xh_k\,\mathrm dV=1\), \(\|u_k\|_\infty=a/(\pi k^2)\), and \(\|\partial_x u_k\|_\infty=2a/k\).

In complex dimension one the normalization scalar is \(\exp B_0(F)=1/\int_X e^F\,\mathrm dV\), by integrating the equation and Stokes; this is precisely the closed identity (11.37.2) with \(m_0=1\). Differentiating the elementary logarithmic integral yields the unique support density \(e^F/\int e^F\); alternatively apply the defining supporting inequality with both positive and negative perturbations. Therefore \(\mathcal A_0(F_k)=\{\nu_k\}\). For \(\nu=h\,\mathrm dV\) with smooth positive \(h\), Jensen's inequality in the dual supremum gives
\[
 \int G h\,\mathrm dV-\log\int e^G\,\mathrm dV
 \leq\int h\log h\,\mathrm dV,
\]
with equality at \(G=\log h\). Thus **directly**, without any regularization programme or nonlinear PDE existence theorem, \(H_0(\nu_k)=\int h_k\log h_k\,\mathrm dV\).

Set \(s=\sqrt{1-a^2}\), \(r=a/(1+s)\), and \(C=(1+s)/2\). The exact factorization
\[
 1+a\cos t=C\,|1+r e^{\mathrm i t}|^2
\]
implies, by the convergent logarithmic Fourier series for \(r<1\), that
\[
 \frac1{2\pi}\int_0^{2\pi}\cos t\,\log(1+a\cos t)\,\mathrm dt=r.
\]
For \(I(a)=(2\pi)^{-1}\int(1+a\cos t)\log(1+a\cos t)\,\mathrm dt\), differentiation under the integral gives \(I'(a)=r=a/(1+s)\) and \(I(0)=0\). Integration yields exactly the formula above. Jensen's strict convexity gives \(I(a)>0\) for \(a>0\); Taylor expansion proves the stated small-\(a\) asymptotic. Since \(H_0=\operatorname{Ent}_{\mathrm dV}\) here, Jensen also gives \(H_0(\nu)\geq0\), with equality only for \(\nu=\mathrm dV\) (including the singular case by the published variational characterization).

For every \(g\in L^\infty(\mathrm dV)\), the function \(g\) is integrable and
\[
 \int_Xg(h_k-1)\,\mathrm dV
 =a\int_Xg(x,y)\cos(2\pi kx)\,\mathrm dx\,\mathrm dy\to0
\]
by the Riemann–Lebesgue lemma (or density of trigonometric polynomials in \(L^1\)). This establishes *weak \(L^1\)* convergence, which is stronger than narrow convergence. Periodicity gives
\[
 \int_X|h_k-1|\,\mathrm dV
 =\frac a{2\pi}\int_0^{2\pi}|\cos t|\,\mathrm dt
 =\frac{2a}{\pi}.
\]
For probabilities the supremum-over-Borel-sets total-variation distance is half the \(L^1\) difference. If a subsequence converged in \(L^1\) norm, its weak limit would necessarily be \(1\), contradicting the constant nonzero distance.

## Interpretation, severity and affected dependents

This is an **exact model demonstrating a sharp topology boundary**, not a counterexample to Theorem 11.35.4: that theorem asserts weak compactness and uniform integrability, both of which hold here. It is not a counterexample to Theorem 11.36.1 either: the input \(F_k=\log h_k\) does **not** converge in \(L^1(\mathrm dV)\). In fact the earlier `POME-CLOSED-LOGPART-SHARP-L1-TV-001` proves norm/TV continuity for uniformly bounded **converging** logarithmic densities in the closed case; that finding is preserved without duplication.

**Proposed source correction:** none required. An optional separately reviewable clarification after Theorem 11.35.4 could state that its compactness is weak only, citing this flat torus, while leaving permanent tags, normalizations and attribution untouched. **Affected dependents:** interpretations of weak-density compactness in §§11.35–11.38 and any attempt to promote such compactness to total variation in moving-density/moving-reference arguments. No such invalid promotion was detected in the inspected printed theorem/proof passages.

**Coverage:** directly rechecked the dual definition and complete statement/proof scope of 11.35.4, the Kähler scalar/dual identities 11.37.2–3, and the stated hypothesis of 11.36.1 for comparison. No entire upstream PDE existence, prescribed-type non-pluripolar mass, or Hermitian duality theorem was independently certified. Previously partly visited §§11.35,11.36,11.37: **+0 first-visited sections / +0 fully certified sections**; current generated table of contents counted at **25 chapters / 747 numbered sections**. Excluded Demailly approximation/regularization and its dedicated Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss programme remain **deferred-by-user**, not verified or reopened. No project build, tests, CI, source/body/registry/tag changes, or publication.
