# 2026-11-18 — Interior simplex slopes: quantitative inverse localization without smoothness

**Finding ID:** \`POME-HOPF-TORIC-SUBGRAD-LOCALIZATION-001\`. **Severity:** low. **Status:** verified conditional deduction. **Original integrated statements:** Proposition 21.14.8 and Equation 21.14.7 remain correct; no false published theorem or repaired global proof is claimed.

## Exact reviewed source

- Production \`main\`: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
- Integrated reading edition: \`docs/sections/hopf-fibrations-and-toric-potentials/index.html\`, blob \`0e83de13efbd70dfddc64a8eed40baed2d4359c5\`.
- §21.14.6 torus-invariant logarithmic coordinates: physical lines 143–158, source \`non-kahler-pluripotential-theory:EBE38F77\`, permanent section tag \`11FD5CD723A9\`.
- Equation (21.14.7): lines 158–163, source \`non-kahler-pluripotential-theory:8E23893D\`, permanent tag \`5DB0E5246A09\`.
- Proposition 21.14.8: statement lines 165–171 and *actual integrated proof* lines 173–201, source \`non-kahler-pluripotential-theory:7515BE71\`, permanent tag \`F23340CADBE0\`. In particular, lines 184–200 establish only qualitative bounded-growth coercivity, and use smooth strict positivity for uniqueness of the inverse gradient.
- Dependency comparison (not re-certified): \`docs/sections/convex-analysis-and-toric-potentials--slope-bodies-and-bounded-growth/index.html\`, blob \`56a9a1c19e7234e2aa258d5ad1b66a5679ace190\`, Proposition 21.4.2 (permanent \`D6E7C0B06FAD\`, lines 19–58) and Lemma 21.4.6 (permanent \`F7AECD623994\`, lines 108–129); these concern slope bodies/log-sums but do not state the inverse-location bound below.

## Statement: quantitative subgradient inverse on the simplex

Let \(n\ge2\), \(k>0\), and let \(v\in\operatorname{PSH}(\mathbb P^{n-1},k\sigma)\) be **bounded** and invariant under separate coordinate rotations. No differentiability or strict positivity is assumed. On the dense coordinate torus write
\[
 F(x)=k\log\!\left(\sum_{i=1}^n e^{x_i}\right)+v([e^{x_1/2}:\cdots:e^{x_n/2}]),
 \qquad x\in\mathbb R^n.
\]
The positive current condition makes \(F\) a finite convex function; it satisfies \(F(x+t\mathbf1)=F(x)+kt\). Let
\[
 \Sigma_k=\{p_i\ge0,\ \sum_i p_i=k\},\quad
 H=\{x:\sum_i x_i=0\},\quad
 \operatorname{osc}v=\sup v-\inf v.
\]
For **every** \(p\in\operatorname{ri}\Sigma_k\), put \(\delta=\min_i p_i>0\). Then there exists \(x_p\in H\) satisfying \(p\in\partial F(x_p)\), and **every** such \(x_p\) obeys the explicit localization estimate
\[
 \boxed{\max_i(x_p)_i-\min_i(x_p)_i
        \le\frac{k\log n+\operatorname{osc}v}{\delta}.}
\]
If the curvature in Proposition 21.14.8 is smooth and strictly positive, the subgradient is a gradient and the original uniqueness assertion yields exactly one point \(x_p\in H\), now with this quantitative bound.

The localization is a statement about **relative-interior slopes**, not boundary points and not a claim that the gradient is single-valued for singular/merely bounded potentials.

## Direct proof (no Demailly regularization)

On the coordinate torus, positivity of \(k\sigma+dd^cv\) translates into positivity of the distributional matrix \((\partial_{x_i x_j}F)\) when tested against constant complex vectors, using exactly the coefficient calculation of Proposition 21.14.8 lines 175–182. A locally integrable real function whose distributional Hessian is positive semidefinite has a convex representative. In this setting the finite bounded-growth representative is continuous on \(\mathbb R^n\), and equality with the toric psh representative follows by upper semicontinuity/uniqueness of psh representatives. Alternatively the convexity criterion follows by restriction to complex torus lines. This is a *basic convexity equivalence*, not the excluded global regularization programme.

Put \(a=\inf v\), \(b=\sup v\); the pointwise inequalities
\[
 k\max_i x_i+a\le F(x)
 \le k\log\sum_i e^{x_i}+b
\]
hold on the dense torus. For \(G_p(x)=F(x)-p\cdot x\) and \(M(x)=\max_i x_i\),
\[
 G_p(x)\ge\sum_i p_i(M(x)-x_i)+a
  \ge\delta\bigl(M(x)-\min_i x_i\bigr)+a. \tag{1}
\]
Both \(G_p\) and the width \(M(x)-\min x_i\) are invariant under translation along \(\mathbf1\). On \(H\), width tends to infinity with \(|x|\), hence \(G_p|_H\) is proper and attains its minimum. Invariance implies that such a minimum is a *global* minimum of \(G_p\) on \(\mathbb R^n\); the convex subgradient inequality gives \(p\in\partial F(x_p)\). Since
\[
 G_p(x_p)\le G_p(0)=k\log n+v([1:\cdots:1])\le k\log n+b,
\]
(1) yields the boxed bound. This also proves the stated bound for **all** minimizers; no choice of a subsequence or smooth approximation is used.

## Sharp \(\delta^{-1}\) order, even for a unique subgradient preimage

The order cannot be uniformly improved if bounded toric psh potentials are allowed to be nonsmooth. Take \(n=2\), \(k=1\), \(0<\delta\le1/8\), \(\alpha=\delta/2\), \(\beta=2\delta\), and
\[
 F_\delta(x_1,x_2)=\max\left\{
 \log(e^{x_1}+e^{x_2})-1,\
 \alpha x_1+(1-\alpha)x_2-\frac38,\
 \beta x_1+(1-\beta)x_2
 \right\}. \tag{2}
\]
Every displayed affine slope belongs to \(\Sigma_1\); hence
\[
 F_0-1\le F_\delta\le F_0,\qquad F_0=\log(e^{x_1}+e^{x_2}).
\]
The difference \(v_\delta=F_\delta-F_0\) defines a **globally continuous** torus-invariant \(\sigma\)-psh function on \(\mathbb P^1\): (2) is convex and has the required homogeneity; at either coordinate divisor the \(F_0-1\) branch dominates, so \(v_\delta\to-1\). Thus \(\operatorname{osc}v_\delta\le1\).

Writing \(s=x_1-x_2\), at
\[
 s_\delta=-\frac1{4\delta}
\]
the two affine branches agree at \(x_2-\frac12\), while the logarithmic branch equals \(x_2+\log(1+e^{-1/(4\delta)})-1<x_2-\frac12\) for \(0<\delta\le1/8\). In a neighborhood of this point \(F_\delta\) is precisely the maximum of the two affine branches. Its one-sided derivatives in \(s\) are \(\alpha<\delta<\beta\), so
\[
 p_\delta=(\delta,1-\delta)\in\partial F_\delta
 \bigl(s_\delta/2,-s_\delta/2\bigr).
\]
Monotonicity of the subgradient in \(s\) shows that this is the **only** inverse image of \(p_\delta\) modulo \(\mathbb R\mathbf1\): to the left slopes are at most \(\alpha\), to the right at least \(\beta\). The width is exactly
\[
 \max x_i-\min x_i=|s_\delta|=\frac1{4\delta}.
\]
Consequently a bound of order \(o(\delta^{-1})\), independent of the bounded potential, is impossible even if the relevant subgradient inverse is unique. This does **not** prove the optimal coefficient \(k\log n+\operatorname{osc}v\), nor assert the same lower bound within the smooth strictly positive subclass.

## Classification, dependency and proposed editorial addition

- **Status:** low / verified conditional deduction; Proposition 21.14.8 is correct. This extends its inverse map to **set-valued** subgradients without strict positivity and quantifies its location. The sharpness example does not contradict the proposition's smooth-uniqueness assertion.
- **Dependency:** the elementary toric current/convexity equivalence (integrated 21.14.8, lines 175–182), the finite-dimensional convex subgradient criterion, and the normalization of \(\sigma\). No global Demailly approximation, Bergman, weighted L², Ohsawa–Takegoshi, atlas gluing, or positivity-loss step was inspected or invoked.
- **Proposed correction/addition:** an optional quantitative remark after Proposition 21.14.8 stating the bounded, possibly nonsmooth subgradient version, the explicit \(\delta^{-1}\) bound and that its order is sharp. **No production body patch has been applied.**
- **Possible dependents:** invertibility/localization steps in toric Legendre duality and moment-map pushforwards in §§21.12–21.14; nothing here certifies their entire chains or shows a downstream error.
- **Actual coverage:** new independent proof of the previously *unquantified* interior inverse step of §21.14.8, its bounded-potential extension and its sharp model, with §§21.4.2/6 checked for semantic overlap. §21.14 and §21.4 were previously partly reviewed; **+0 first-visited numbered sections / +0 wholly verified sections**; actual inventory 25 chapters / 747 sections.
- All earlier confirmed errors/gaps/external dependencies retain their classifications; the owner-excluded regularization/Bergman/L²/OT/multiscale/positivity-loss work remains **deferred-by-user**, not resolved. Only review-branch audit notes; no tests, builds, CI, publication, canonicalization, body, source, tag or main edits.
