# Relative capacities: zero-Lelong poles rule out any universal power modulus

**Finding:** POME-RELCAP-ZEROLELONG-NO-UNIVERSAL-POWER-001  
**Date:** 2026-11-03  
**Severity/status:** low / **verified conditional deduction** (independent quantitative sharpness model). **Not** a false printed theorem or a complete certification.  
**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Primary integrated reading file:** \`docs/sections/envelopes-and-model-potentials--comparison-of-relative-capacities/index.html\`, blob \`1c209671c3de0740018b2aaad7aa321f5647313d\`.  
**Main anchors:** §16.27.15 (source \`foundations-of-pluripotential-theory:106FDCD9\`, permanent \`A285A0B9F4B7\`, physical lines 217–259, especially the tail-dependent comparison (16.27.16), lines 227–256); §16.27.17 (source \`foundations-of-pluripotential-theory:207C29D0\`, permanent \`337360EF765B\`, physical lines 262–289).  
**Definition and nonduplicate comparison:** \`docs/sections/envelopes-and-model-potentials--singularity-constraints-and-relative-capacity/index.html\`, blob \`4207ba03590b2988456f1df4da4123e1e572c8de\`: Definition 16.25.5 (source \`foundations-of-pluripotential-theory:0AAB93DD\`, permanent \`E9BD67F94210\`, lines 104–108); Proposition 16.25.6 (source \`foundations-of-pluripotential-theory:2C3BA6F2\`, permanent \`1587DBB4654F\`, lines 113–135).

## Precise statement

Let \(X=\mathbf P^1\), \(\omega=dd^c\log(1+|z|^2)\) with \(\int_X\omega=1\), and \(\phi=0\). For **every** \(0<\alpha<1\), there is a nonpositive \(\omega\)-psh function \(\psi_\alpha\), smooth outside \(p=[1:0]\), with an unbounded pole at \(p\), **zero Lelong number everywhere**, and full non-pluripolar Monge–Ampère mass \(\mu_{\psi_\alpha}(X)=1\), such that, for \(K_T=\{|z|\le e^{-T}\}\) and \(T\to\infty\),

\[
  \operatorname{Cap}_{\omega,0}(K_T)\asymp T^{-1},\qquad
  \operatorname{Cap}_{\omega,\psi_\alpha}(K_T)\asymp T^{-(1-\alpha)}.
\]

The constants may depend on \(\alpha\), but not on \(T\). Thus, for **any** \(\gamma>1-\alpha\),

\[
 \frac{\operatorname{Cap}_{\omega,\psi_\alpha}(K_T)}
      {\operatorname{Cap}_{\omega,0}(K_T)^\gamma}\longrightarrow+\infty.
\]

In particular the continuous comparison modulus \(F\) in the correct Theorem 16.27.17 cannot, for arbitrary positive-mass reference potentials, always be chosen Lipschitz, even when both potentials have full mass and the singular one has zero Lelong number. More strongly, **no positive Hölder exponent can be chosen uniformly over all such** \(\psi_\alpha\) while keeping \(X,\omega,\phi\) and mass fixed: given \(\gamma>0\), take \(\alpha>\max(0,1-\gamma)\).

This is a **sharp two-sided scale calculation along the specified shrinking disks**, not a claim about the optimal global comparison function for all Borel sets. It does not contradict the bounded-difference comparison in Proposition 16.25.6: \(\psi_\alpha-0\) is unbounded below.

## Global construction and curvature

Use the affine coordinate \(z=Z_1/Z_0\), \(p=\{z=0\}\), and put

\[
 g=\log\frac{|z|^2}{1+|z|^2}\le0,\quad dd^c g=[p]-\omega,
 \quad dd^c=\frac{i}{2\pi}\partial\bar\partial .
\]

Fix \(0<\epsilon<1/4\), and define an increasing convex \(C^1\) function on \((-\infty,0]\) by

\[
 H(t)=
 \begin{cases}
 -\epsilon(-t)^\alpha,&t\le-2,\\
 -\epsilon2^\alpha+\epsilon\alpha2^{\alpha-1}(t+2),&-2\le t\le0.
 \end{cases}
 \qquad
 0\le H'\le \epsilon\alpha2^{\alpha-1}<1.
\]

Let \(\psi_\alpha=H(g)\). The convex chain rule on \(X\setminus\{p\}\) gives

\[
 \omega+dd^c\psi_\alpha
 =(1-H'(g))\omega+H''(g)\,dg\wedge d^cg\ge(1-\epsilon)\omega.
\]

At \(p\) the logarithmic residue is \(H'(-\infty)=0\); hence there is no Dirac mass there, and this positive current extends across \(p\). Thus \(\psi_\alpha\) is \(\omega\)-psh. Since \(g(z)=\log|z|^2+O(|z|^2)\), its local singularity is \(-\epsilon(2\log(1/|z|)+O(1))^\alpha\): it tends to \(-\infty\) and has Lelong number zero. In complex dimension one the non-pluripolar product of \(\omega+dd^c\psi_\alpha\) removes only pole-set atoms; there are none, so its mass is the cohomological total \(1\). The same holds for all \(u\) with \(\psi_\alpha-1\le u\le\psi_\alpha\): zero Lelong number and no atoms at \(p\), while these inequalities keep \(u\) locally bounded away from \(p\).

No approximation/regularization theorem, Bergman or weighted \(L^2\) argument is used.

## Radial Jensen/flux identity with the exact normalization

For any \(\omega\)-psh competitor \(u\), set \(W_u(z)=u(z)+\log(1+|z|^2)\), which is subharmonic on the affine chart, and

\[
 M_u(t)=\frac1{2\pi}\int_0^{2\pi}
 W_u(e^{t+i\vartheta})\,d\vartheta .
\]

The function \(M_u\) is convex in \(t\), and the planar Riesz/Jensen formula, normalized by \(dd^c\log|z|^2=\delta_0\), reads

\[
 \bigl(\omega+dd^cu\bigr)(\overline B_{e^t})
     =\frac12 M'_{u,+}(t).
 \tag{1}
\]

The right derivative includes mass on the boundary circle. For the non-pluripolar measures of the potentials considered here there is no mass at the pole, so (1) applies without an atomic correction. It also applies to arbitrary bounded competitors for \(\operatorname{Cap}_{\omega,0}\). The only analytic inputs are the classical submean/Jensen formula and positivity of the subharmonic Riesz measure.

For the radial function \(\psi_\alpha\), letting \(r=e^{-T}\) and \(g_r=\log(r^2/(1+r^2))\), direct differentiation gives

\[
 \mu_{\psi_\alpha}(K_T)
 =\frac{r^2+H'(g_r)}{1+r^2}
 =\frac{r^2+\epsilon\alpha(-g_r)^{\alpha-1}}{1+r^2}
 \asymp T^{\alpha-1}\qquad(T\ge4).
 \tag{2}
\]

Since \(\psi_\alpha\) itself is admissible in its own relative capacity, (2) proves the required lower bound.

For **every** admissible \(u\in[\psi_\alpha-1,\psi_\alpha]\), Jensen convexity gives

\[
 \mu_u(K_T)=\tfrac12 M'_{u,+}(-T)
 \le\frac{M_u(-T/2)-M_u(-T)}{T}
 \le\frac{M_{\psi_\alpha}(-T/2)-M_{\psi_\alpha}(-T)+1}{T}.
 \tag{3}
\]

Here \(M_{\psi_\alpha}\) is explicit and radial. For \(T\ge4\),

\[
 M_{\psi_\alpha}(-T/2)-M_{\psi_\alpha}(-T)
 =\epsilon\bigl((-g(e^{-T}))^\alpha-(-g(e^{-T/2}))^\alpha\bigr)
   +\log\frac{1+e^{-T}}{1+e^{-2T}}
 \le C_\alpha T^\alpha.
\]

Thus (3), uniformly in all competitors, proves
\(\operatorname{Cap}_{\omega,\psi_\alpha}(K_T)\le C_\alpha T^{\alpha-1}\).
Together with (2), this is a genuinely two-sided capacity estimate, not merely a test-current lower bound.

## Smooth-reference capacity: independent two-sided computation

For every competitor \(v\in\mathrm{PSH}(X,\omega)\) with \(-1\le v\le0\), its Jensen mean satisfies \(M_v(0)\le\log2\) and \(M_v(-T)\ge-1\). By (1) and convexity,

\[
 \mu_v(K_T)=\tfrac12M'_{v,+}(-T)
 \le\frac{M_v(0)-M_v(-T)}{2T}
 \le\frac{1+\log2}{2T}.
 \tag{4}
\]

For the reverse inequality choose \(T\ge4\) and the global admissible potential

\[
 v_T=\max\left\{\frac{g}{4T},-1\right\}.
\]

Indeed \(\omega+dd^c(g/(4T))=(1-1/(4T))\omega+[p]/(4T)\ge0\);
the maximum of two \(\omega\)-psh functions is \(\omega\)-psh, and
\(-1\le v_T\le0\). Near \(|z|=e^{-T}\), \(g/(4T)>-1\), hence the same radial flux calculation as in (2) yields

\[
 \mu_{v_T}(K_T)
 =\frac{r^2+(4T)^{-1}}{1+r^2}\ge\frac1{8T}.
 \tag{5}
\]

Equations (4) and (5) establish \(\operatorname{Cap}_{\omega,0}(K_T)\asymp T^{-1}\) with explicit universal constants. In particular, the global fixed-background normalization was not replaced by a local condenser capacity without proof.

## Classification and dependencies

- **Status:** verified conditional deduction / quantitative sharpness example. The original Theorem 16.27.17 remains true and its arbitrary continuous \(F,G\) are necessary in this generality. Lemma 16.27.15 remains true. No false theorem is asserted.
- **Not a duplicate:** §16.25.6, lines 117–135, proves a two-sided \((2C+1)^n\) bound **only for bounded-difference reference potentials**; the present example has an unbounded difference, even though its Lelong number is zero and mass is maximal. It tests the genuinely broader quantifiers of §16.27.17.
- **Inputs:** Poincaré–Lelong for \(g\), elementary distributional convex composition, classical one-variable Jensen/Riesz flux, positivity and degree-one definition of non-pluripolar product. No new external mathematical input beyond these standard/internal ingredients; their complete general theory was not certified here.
- **Affected dependents:** any attempt to replace Theorem 16.27.17's reference-dependent continuous modulus by a universal Hölder or Lipschitz modulus, including capacity-convergence and uniform-absolute-continuity comparisons in Proposition 16.27.18, must retain additional uniform assumptions. This is a proposed **explanatory example only**, not a source/body/registry change.
- **Coverage:** direct new model-level checks of §16.27.15 and §16.27.17, plus §16.25.5/.6 definition and bounded-difference-hypothesis crosscheck. No full §16.25 or §16.27 certificate, no assertion about §16.27.1's excluded analytic approximation, and no transitive proof certification.
