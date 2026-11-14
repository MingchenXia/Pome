# Two distinct point-pole currents: maximum, Apollonius measure, and exact transport

**Date:** 2026-11-14. **Finding:** POME-NPP-APOLLONIUS-MAX-TRANSPORT-001. **Severity:** low. **Status:** verified conditional deduction (explicit complete model calculation; upstream monotone-capacity principle used conditionally). **False printed result:** none. **Reviewed production main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Target:** mathematical audit only; no source or registry patch applied.

## Exact reading-edition anchors

1. **Max stability:** docs/sections/plurisubharmonic-functions-and-singularities--maxima-and-the-maximum-principle/index.html, blob af8c44279c1e18f00174d613473b1d175beaa44a, Lemma 5.24.1, source non-kahler-pluripotential-theory:8EAEF1E9, permanent 729BA86BCC7C, physical lines 10–25.
2. **Fubini–Study convention and normalized point current:** docs/sections/global-potentials-and-positive-cohomology-classes--curvature-and-metrics-defined-by-sections/index.html, blob ff56aa13950da3423135bb0bbaf40bcc980c21a1, Example 10.6.7, source foundations-of-pluripotential-theory:E51945FB, permanent 4CE1D9D7D803, physical lines 108–115.
3. **Definition and pole exclusion:** docs/sections/non-pluripolar-products--truncation-and-plurifine-locality/index.html, blob 81be8c5acc360c96bd3c5acba05a3cdb5fafaf4c, Definition 13.2.4, source foundations-of-pluripotential-theory:9D8E4DD8, permanent D79952D7E272, physical lines 57–63. The global first-degree convention follows by localization.
4. **Capacity/mass condition:** docs/sections/non-pluripolar-products--capacity-convergence-and-loss-of-mass/index.html, blob d66813856cb813722806ab912afdfd4815d2da97, Theorem 13.7.5, source foundations-of-pluripotential-theory:AB4EBE3B, permanent 67C4F7EC316E, physical lines 106–134; Example 13.7.6, source foundations-of-pluripotential-theory:D5678E03, permanent ACAEA8D8BE87, physical lines 138–140; Proposition 13.7.8, source foundations-of-pluripotential-theory:8CF7A9C6, permanent 4B60F7F33590, physical lines 147–171.

## Exact statement

Let \(\omega=\mathrm{dd}^{\mathrm c}\log(1+|z|^2)\) on \(\mathbf P^1\), with \(\int\omega=1\), and fix any two **distinct finite** complex numbers \(a,b\). Define globally extended \(\omega\)-psh potentials, in the affine chart,

\[
u_a(z)=\log\frac{|z-a|^2}{1+|z|^2},\qquad
u_b(z)=\log\frac{|z-b|^2}{1+|z|^2}.
\]

They have only point poles and
\[
\omega+\mathrm{dd}^{\mathrm c}u_a=[a],\qquad
\omega+\mathrm{dd}^{\mathrm c}u_b=[b],\qquad
\langle[a]\rangle=\langle[b]\rangle=0.
\]
For each real \(c\), set \(v_c=\max(u_a,u_b+c)\) and \(R=e^{c/2}\). Then \(v_c\) is **bounded and continuous** on the entire sphere, and its non-pluripolar first-degree current is the probability
\[
\mu_c=\langle\omega+\mathrm{dd}^{\mathrm c}v_c\rangle
=\omega+\mathrm{dd}^{\mathrm c}v_c
=(w^{-1})_*\lambda_R,\qquad
w(z)=\frac{z-a}{z-b},
\]
where \(\lambda_R\) is the angularly uniform measure on \(|w|=R\) in \(\mathbf P^1\). Its support is the Apollonius generalized circle
\[
\bigl\{[1:z]\in\mathbf P^1:\ |z-a|=R|z-b|\bigr\}.
\]
For \(R=1\), this is a Euclidean line completed by its point at infinity. No atoms occur at \(a,b,\infty\).

Let \(d_{\rm ch}([1:z],[1:\zeta])=|z-\zeta|/\sqrt{(1+|z|^2)(1+|\zeta|^2)}\), and let \(W_1\) be Wasserstein distance for \(d_{\rm ch}\). For \(w=Re^{i\vartheta}\), put
\[
Q_R(\vartheta)=|1-Re^{i\vartheta}|^2+|a-bRe^{i\vartheta}|^2>0,\qquad
I(R)=\frac1{2\pi}\int_0^{2\pi}Q_R(\vartheta)^{-1/2}\,\mathrm d\vartheta.
\]
There are **exact identities**, valid for every finite \(c\):
\[
W_1(\mu_c,\delta_a)
=\frac{|a-b|R}{\sqrt{1+|a|^2}}I(R),\qquad
W_1(\mu_c,\delta_b)
=\frac{|a-b|}{\sqrt{1+|b|^2}}I(R),
\]
and hence
\[
\boxed{\displaystyle
\frac{W_1(\mu_c,\delta_a)}{W_1(\mu_c,\delta_b)}
=R\sqrt{\frac{1+|b|^2}{1+|a|^2}}}.
\]
The exact endpoint coefficients are
\[
\lim_{c\to-\infty}e^{-c/2}W_1(\mu_c,\delta_a)
=\frac{|a-b|}{1+|a|^2},\qquad
\lim_{c\to+\infty}e^{c/2}W_1(\mu_c,\delta_b)
=\frac{|a-b|}{1+|b|^2}.
\]
Nevertheless, for each finite \(c\),
\(\|\mu_c-\delta_a\|_{\rm TV}=\|\mu_c-\delta_b\|_{\rm TV}=2\)
under the total variation **norm** convention. Both zero-mass pole currents can therefore have a bounded maximum whose non-pluripolar mass is one, with exact two-sided concentration under variation of the additive constant.

## Proof

**Point currents and their first-degree non-pluripolar masses.**
The formula for the normalized \(\omega\) is precisely Example 10.6.7. The functions \(u_a,u_b\) tend to \(0\) at infinity; each is locally bounded away from its respective pole. Poincaré–Lelong in the affine chart gives
\(\mathrm{dd}^{\mathrm c}\log|z-a|^2=[a]\), and similarly at \(b\). The global equalities follow because the point currents have mass one and no additional atom at infinity. Definition 13.2.4 restricts a non-pluripolar first-degree current to the complement of its pole set: the point currents above are supported *entirely* at their respective poles. Hence both bracketed currents vanish, although their ordinary currents have total mass one.

**Maximum and its entire curvature.**
Lemma 5.24.1 ensures \(v_c\) is \(\omega\)-psh. At \(a\), its \(u_b+c\) branch is smooth; at \(b\), its \(u_a\) branch is smooth; at infinity both inputs tend to finite constants. Thus the maximum is bounded and continuous globally. In the affine chart,
\[
\omega+\mathrm{dd}^{\mathrm c}v_c
=\mathrm{dd}^{\mathrm c}\max\bigl(\log|z-a|^2,\log|z-b|^2+c\bigr).
\]
For \(z\ne b\) write the maximum as
\[
\log|z-b|^2+\max(\log|w(z)|^2,c).
\]
The first term is harmonic off \(b\); the second is the pullback by the local biholomorphism \(w\) of a radial subharmonic function. Directly, for \(g(w)=\max(\log|w|^2,c)=\max(2\log|w|,c)\), the radial derivative is \(0\) below \(R\) and \(2/\rho\) above \(R\). Thus
\[
\mathrm{dd}^{\mathrm c}g=\frac{\mathrm d\vartheta}{2\pi}\quad\text{on }|w|=R
\]
using \(\mathrm{dd}^{\mathrm c}=(1/4\pi)\Delta\,\mathrm dA\) in a complex chart. This is a probability measure. Since \(v_c\) is smooth near \(a,b\) and infinity away from the level set, no additional atom or diffuse term can occur there. The formula for \(\mu_c\) follows. Because \(v_c\) is bounded, its bracketed current is its ordinary curvature (Definition 13.2.4).

**Transport identities.**
The inverse Möbius map is
\[
z(\vartheta)=\frac{a-bRe^{i\vartheta}}{1-Re^{i\vartheta}},
\]
where \(z=\infty\) for the isolated case \(R=1,\vartheta=0\). Its projective value is well defined there. Algebra gives
\[
|z-a|=\frac{|a-b|R}{|1-w|},\quad
|z-b|=\frac{|a-b|}{|1-w|},\quad
1+|z|^2=\frac{Q_R(\vartheta)}{|1-w|^2}.
\]
For a Dirac target, the only transport coupling sends every source point to that target, so \(W_1(\mu_c,\delta_p)=\int d_{\rm ch}(z,p)\,\mathrm d\mu_c(z)\). Substituting the inverse-circle parametrization gives the two exact formulas and their ratio. Since \(a\ne b\), \(Q_R>0\), including at the possible projective point at infinity. Dominated convergence gives \(I(R)\to (1+|a|^2)^{-1/2}\) as \(R\to0\) and \(R I(R)\to (1+|b|^2)^{-1/2}\) as \(R\to\infty\), proving both sharp coefficients. The measures \(\mu_c\) charge neither \(a\) nor \(b\), so they are mutually singular with each Dirac; the total-variation norms of the differences are exactly two.

**Capacity convergence and lost mass.**
As \(c\to-\infty\), \(v_c\downarrow u_a\). As \(c\to+\infty\), \(v_c-c=\max(u_a-c,u_b)\downarrow u_b\). On every local chart, these are decreasing sequences (or directed nets) of psh potentials after adding the fixed smooth local \(\omega\)-potential; hence Proposition 13.7.8 gives extended capacity convergence. The explicit circle formula shows \(\mu_c\rightharpoonup[a]\) in the first limit and \(\mu_c\rightharpoonup[b]\) in the second; subtracting constants does not affect currents. At either limit, the first-degree **non-pluripolar** current is zero, while all prelimit masses are one. This is exactly the direction permitted by Theorem 13.7.5's lower-semicontinuity clause, and its additional no-mass-drop assumption is violated. No printed result is contradicted.

## Novelty boundary, dependencies, and action

The **unit-circle** case of the max of two normalized homogeneous section weights was already evaluated in the audit finding **POME-FS-MAX-CIRCLE-CURVATURE-001 (2026-10-27)**: its curvature and boundedness are **not** counted as newly discovered here. The **single-pole truncation shell and its chordal transport** were previously treated in **POME-NPP-CP1-TRUNCATION-SHELL-W1-001 (2026-11-11)**. The present new contribution is a distinct **two-arbitrary-point Apollonius family**, the global Möbius-pushforward description, **exact simultaneous two-target transport formulas and their ratio**, and the two opposite monotone-capacity/non-pluripolar mass-loss endpoints. Neither earlier model includes this two-target geometry or exact ratio.

The curvature/transport model is calculated in full. Its application to extended capacity uses the printed Proposition 13.7.8 as an **internal conditional dependency**, not as a newly certified transitive theorem chain. The Poincaré–Lelong and maximal-stability steps have been directly compared with their integrated text; their complete upstream histories were not reverified. Status remains **verified conditional deduction**, **not** verified repair of a false statement. Suggested optional **proposed** addition: a worked comparison of maxima versus first-degree non-pluripolar mass near §13.7.6, without altering its hypotheses, tags, history or original text. Affected interpretation: §5.24 maximum operation; §10.6 max metrics; §13.2 first-degree truncation; §13.7 capacity convergence and necessity of the total-mass condition. No other dependents are claimed.

**Scope:** selected direct mathematical review of already partially visited §§5.24, 10.6, 13.2, 13.7; no first-visited numbered sections and no whole-section certificates. Actual ToC remains 25 chapters / 747 numbered sections. The user-excluded Demailly approximation/regularization and its Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programmes stay **deferred-by-user**; no part was opened. No project software tests, mathematical formal verification, build, CI or publication performed.
