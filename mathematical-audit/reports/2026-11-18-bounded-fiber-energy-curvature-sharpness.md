# Bounded fiber-energy curvature and optimal coefficient

2026-11-18. **POME-NPP-FIBER-ENERGY-CURVATURE-001**. Severity **low**; status **verified conditional deduction** (no false printed result). Reviewed main: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.

## Exact integrated anchors

* \`docs/sections/non-pluripolar-products--fiber-integration-and-modifications/index.html\`, blob \`9954a43d90d5cae8ef744968636d7a5912348fce\`: Corollary 13.6.1 source \`non-kahler-pluripotential-theory:BAE2819F\` / permanent \`BEC54934FC2C\`, physical lines 11–31; weighted fiber Eq. 13.6.2 source \`non-kahler-pluripotential-theory:73910199\` / permanent \`F6B4982710D8\`, lines 16–22.
* \`docs/sections/relative-energy-and-perron-segments--relative-monge-ampere-energy/index.html\`, blob \`16fdcc4c6a6f0cc75e69ba267bd7da2b2d7922a1\`: Definition 17.3.2 source \`foundations-of-pluripotential-theory:582D55DC\` / permanent \`240EF1DE5889\`, lines 32–40; Eq. 17.3.3 source \`foundations-of-pluripotential-theory:8C7506A6\` / permanent \`F19AAFA93177\`, lines 33–38.
* Conditional earlier internal inputs: bounded Bedford–Taylor recursion (Definition 7.2.1), closed bounded Stokes formula (Proposition 13.5.1), and the weighted fiber Fubini result (13.6.2). These input proof chains are **not wholly certified**.

## Statement

Let \(X,Z\) be connected compact Kähler manifolds of dimensions \(r,m\ge1\). Let \(\theta\) be a smooth **closed** real \((1,1)\)-form on \(X\), \(\gamma\ge0\) a smooth **closed** \((1,1)\)-form on \(Z\), and \(\varphi\) a **bounded** \(\theta\)-psh function on \(X\). Let \(W\) be a **bounded** \((p_X^*\theta+p_Z^*\gamma)\)-psh function on \(X\times Z\). Put \(\Phi=p_X^*\varphi\), \(\chi=W-\Phi\), \(T=p_X^*\theta+p_Z^*\gamma+dd^cW\), and \(S=p_X^*\theta+p_Z^*\gamma+dd^c\Phi\). Set
\[
M=\int_X(\theta+dd^c\varphi)^r=\int_X\theta^r\ge0,\qquad
\mathcal E(z)=\frac1{r+1}\sum_{j=0}^r
\int_X(W_z-\varphi)(\theta+dd^cW_z)^j
\wedge(\theta+dd^c\varphi)^{r-j}.
\]
All factors are bounded Bedford–Taylor products, agreeing with non-pluripolar products. Each fiber integral exists for every \(z\) by Corollary 13.6.1. The bounded Borel function \(\mathcal E\) satisfies the **exact current identity**
\[
\boxed{dd^c_Z\mathcal E+M\gamma
=\frac1{r+1}(p_Z)_*(T^{r+1})\ge0.}\tag{A}
\]
Thus \(\mathcal E\) has an \(M\gamma\)-psh representative, unique up to equality almost everywhere. The proof does **not** identify the pointwise Borel fiber formula with its usc representative at every exceptional \(z\). When \(\varphi\) is a bounded *model* reference, \(\mathcal E\) is exactly the relative energy of (17.3.3), not merely a similarly normalized polynomial.

## Proof

1. For \(0\le j\le r\), \(Q_j=T^j\wedge S^{r-j}\) is a closed positive Bedford–Taylor current. Boundedness permits multiplying by \(\chi\). The bounded Bedford–Taylor recursion and linearity, using closedness of \(Q_j\), give the **current** identity
\[
dd^c(\chi Q_j)=(T-S)\wedge Q_j
=T^{j+1}S^{r-j}-T^jS^{r-j+1}.
\]
Summing telescopes:
\[
dd^c\sum_{j=0}^r\chi Q_j=T^{r+1}-S^{r+1}.
\]
No regularization or limiting interchange is needed.
2. For every smooth top-degree test form \(\eta\) on \(Z\), the *already printed* weighted fiber formula (13.6.2) identifies the pushforward \((p_Z)_*(\chi Q_j)\) with the \(j\)th fiber integral defining \(\mathcal E\). By bounded Stokes, each fiber mixed product has mass \(M\), so \(|\mathcal E(z)|\le M\|\chi\|_\infty\). Proper pushforward commutes with \(dd^c\), hence
\[
(r+1)dd^c_Z\mathcal E=(p_Z)_*T^{r+1}-(p_Z)_*S^{r+1}.
\]
3. Write \(A=\theta+dd^c\varphi\). In \(S=p_X^*A+p_Z^*\gamma\), only the term with exactly \(r\) vertical \(A\)-factors and one horizontal \(\gamma\)-factor survives integration along \(X\). Consequently
\[
(p_Z)_*S^{r+1}=(r+1)M\gamma.
\]
The current \(T^{r+1}\) is positive, so its proper pushforward is positive. This proves (A). Locally \(\gamma=dd^cb\) with \(b\) smooth; then \(dd^c(\mathcal E+Mb)\ge0\) distributionally, giving the claimed psh representative.

## Sharpness by an exact smooth model

Take \(X=\mathbf P^r\) and \(Z=\mathbf P^1\), \(\theta,\gamma\) their respective Fubini–Study forms, \(\varphi=0\) and \(M=\int_X\theta^r>0\). Set
\[
t(z)=\frac{|z|^2}{1+|z|^2},\qquad W(x,z)=-t(z).
\]
The function \(t\) extends smoothly over \(\infty\); in the convention \(dd^c=\frac{i}{2\pi}\partial\bar\partial\),
\[
dd^c t=(1-2t)\gamma,\qquad \gamma+dd^c(-t)=2t\gamma\ge0.
\]
Thus \(T=p_X^*\theta+2t\,p_Z^*\gamma\) is semipositive and each fiber Monge–Ampère form is \(\theta\). Directly, \(\mathcal E=-Mt\), and
\[
dd^c\mathcal E+M\gamma=2Mt\gamma
=\frac1{r+1}(p_Z)_*T^{r+1}.
\]
At \(z=0\), \(dd^c\mathcal E=-M\gamma\). Replacing \(M\gamma\) by \(a\gamma\) with any \(a<M\) makes \(dd^c\mathcal E+a\gamma\) **negative near \(0\)**. Hence the coefficient \(M\) is optimal even for smooth data.

## Verdict, limits, dependents

This is a **verified conditional deduction**, not a false source theorem, unqualified proof repair, or full mathematical certification of the cited sections. The new part is the bounded-product base-current identity and sharp coefficient, distinct from prior fiber disintegration, modification, and energy numerical audits. Suggested correction: optionally add an independently reviewed lemma adjacent to Corollary 13.6.1, with reference to (17.3.3); do not modify source, body, registry, canonicalization, or tags directly. It can support §§13.6 and 17.3 and later geodesic curvature arguments.

**Unresolved:** if \(\varphi,W\) are unbounded but have bounded difference, the required global \(dd^c\)-Leibniz/telescoping identity for \((W-\Phi)\langle T^jS^{r-j}\rangle\), without a pole-boundary defect current, has **not** been established here. The weighted fiber formula alone does not prove it. Do not infer an unrestricted theorem or reopen Demailly approximation and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale atlas or positivity-loss programme. No tests, build or CI were run; no full section or dependency chain was certified.
