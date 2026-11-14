# Sharp logarithmic-ratio transport for the toric simplex softmax

**Date:** 2026-11-14 (Asia/Shanghai). **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Audit branch:** review/mathematical-audit. **Finding:** POME-TORIC-SOFTMAX-LOGRATIO-W1-001. **Classification:** low / verified conditional deduction; no printed theorem is false. The identified quantitative result is an *addition* to, not a repeat of, POME-TORIC-SOFTMAX-TV-001 (2026-10-25), which already proved narrow convergence and the fixed total-variation obstruction for precisely this softmax family.

## Integrated reading-edition anchors and boundaries

- docs/sections/convex-analysis-and-toric-potentials/index.html, main blob e875ab348461c739ae3799c6906f8f13b9050ba7, physical lines 7–18 (toric logarithmic coordinates, dual lattices and the n! normalization).
- docs/sections/convex-analysis-and-toric-potentials--the-real-monge-ampere-measure/index.html, main blob 7089aa41ae2422b1bd6b5094e46668cbc8ed37be: Theorem 21.5.1, source foundations-of-pluripotential-theory-4A0FAEB3, permanent tag 409656CC47D4, physical lines 10–39 (subgradient volume and Legendre pushforward); Theorem 21.5.2, source foundations-of-pluripotential-theory-6403CF44, permanent tag F4072D9ED060, physical lines 43–85 (vague continuity); Example 21.5.3, lines 90–94 (escape of mass); Proposition 21.5.4, source foundations-of-pluripotential-theory-EAD83A50, permanent tag 5D8A7A7D734E, physical lines 98–157 (smooth Hessian density and polarization).
- Earlier exact simplex softmax computation and TV obstruction: mathematical-audit/reports/2026-10-25-toric-softmax-total-variation-and-moving-lattice-bodies.md. The gradient, determinant, full mass, narrow limit and signed-variation distance **are not new findings of this report**. This pass newly computes the complete coordinate marginal laws, sharp exponential tails and the **exact metric transport coefficient**.

## New precise assertion

Fix n >= 1, the dual standard lattices N=M=Z^n, and the simplex
\[
P=\{p_i\ge0,\ \sum_{i=1}^n p_i\le1\},\qquad p_0=1-\sum_{i=1}^n p_i.
\]
For \(\varepsilon>0\) let
\[
F_\varepsilon(x)=\varepsilon\log(1+\sum_{i=1}^n e^{x_i/\varepsilon}),\quad
F_0(x)=h_P(x)=\max(0,x_1,\ldots,x_n),\quad
\mu_\varepsilon=\operatorname{MA}_{\mathbb R}(F_\varepsilon).
\]
Then \(\mu_0=\delta_0\), and for each coordinate \(i=1,\ldots,n\), the pushforward of \(\mu_\varepsilon\) under \(x\mapsto x_i\) has the **centered logistic law of scale \(\varepsilon\)**:
\[
\mu_\varepsilon\{x_i\le s\}
=\frac{e^{s/\varepsilon}}{1+e^{s/\varepsilon}},\quad
\mu_\varepsilon\{|x_i|>s\}=\frac{2}{1+e^{s/\varepsilon}}
\quad(s\ge0).
\]
For the *auxiliary lattice-coordinate \(\ell^1\) distance*
\(d_1(x,y)=\sum_i|x_i-y_i|\), the **exact** Wasserstein distance is
\[
\boxed{W_{1,d_1}(\mu_\varepsilon,\delta_0)=2n(\log2)\,\varepsilon.}
\]
The measure has total mass one, every moment finite, and contracts to \(\delta_0\) at exactly linear first-Wasserstein rate; the Euclidean \(W_1\) rate is likewise exactly of order \(\varepsilon\) (bounded between \(2\log2\,\varepsilon\) and \(2n\log2\,\varepsilon\)). The **previously recorded** signed total-variation norm remains \(2\) for every \(\varepsilon>0\). No statement is made that this is an optimal modulus for arbitrary convex functions or that narrow convergence generally implies \(W_1\) convergence.

## Complete elementary computation

Write
\(Z=1+\sum_i e^{x_i/\varepsilon}\),
\(p_i=e^{x_i/\varepsilon}/Z\),
\(p_0=1/Z\).
Then
\[
\nabla F_\varepsilon=p,\quad
D^2F_\varepsilon=\varepsilon^{-1}
(\operatorname{diag}(p)-pp^{\mathsf T}),\quad
\det D^2F_\varepsilon=\varepsilon^{-n}p_0\prod_{i=1}^n p_i.
\]
The determinant identity is the matrix determinant lemma (or follows by elementary row operations). All \(p_i,p_0\) are positive; the gradient is a diffeomorphism from \(\mathbb R^n\) onto the interior of \(P\), with inverse
\[
x_i=\varepsilon\log(p_i/p_0).
\]
The n! normalization in Proposition 21.5.4, together with the change-of-variables formula, therefore yields
\[
\mu_\varepsilon
=(\varepsilon(\log(p_i/p_0))_{i=1}^n)_*
\bigl(n!\mathbf1_{P^\circ}\,dp\bigr).
\]
This reuses the **previously verified exact Jacobian** only as an input; what follows is a new explicit computation of the pushforward's quantitative distribution.

To evaluate that distribution *without assuming a probabilistic representation*, let \(E_0,\ldots,E_n\) be independent random variables with density \(e^{-u}\mathbf1_{u>0}\), put \(S=\sum_{i=0}^nE_i\), and set \(P_i=E_i/S\). The coordinate transformation
\((E_0,\ldots,E_n)\mapsto(S,P_1,\ldots,P_n)\)
has absolute Jacobian \(S^n\), so its joint density becomes
\(e^{-S}S^n\,dS\,dP_1\cdots dP_n\).
Integration over \(S>0\) gives
\(\int_0^\infty e^{-S}S^n\,dS=n!\), by repeated integration by parts. Thus \((P_1,\ldots,P_n)\) is exactly uniform on \(P\), with density n!, and
\[
X_i/\varepsilon\stackrel{\mathrm d}=
\log(P_i/P_0)=\log(E_i/E_0).
\]
For any \(t\in\mathbb R\), condition on \(E_0=u\) and integrate:
\[
\Pr(\log(E_i/E_0)\le t)
=\int_0^\infty(1-e^{-e^tu})e^{-u}\,du
=\frac{e^t}{1+e^t}.
\]
Consequently the law is logistic, symmetric about zero, and its two-sided tail is \(2/(1+e^t)\) for \(t\ge0\). The layer-cake formula gives
\[
\mathbb E|\log(E_i/E_0)|
=\int_0^\infty\frac{2\,dt}{1+e^t}
=2\log2.
\]
Since a transport coupling to the point mass \(\delta_0\) is uniquely determined,
\[
W_{1,d_1}(\mu_\varepsilon,\delta_0)
=\int_{\mathbb R^n}\sum_i|x_i|\,d\mu_\varepsilon
=\varepsilon\sum_i\mathbb E|\log(E_i/E_0)|
=2n\varepsilon\log2.
\]
The same logistic tail gives finite moments of all orders. As in the older report, \(\partial h_P(0)=P\) and \(\partial h_P(x)\) has volume zero for \(x\neq0\), giving \(\mu_0=\delta_0\). No projective, Bergman, L2, Ohsawa–Takegoshi or regularization input enters this computation.

## Proof review, status, and disposition

New direct checks of integrated §§21.5.1, 21.5.2 and 21.5.4 were confined to the n! change-of-variables normalization, the hypothesis **finite convex function**, and the distinction of vague, narrow, total-variation and Wasserstein topologies. The smooth \(F_\varepsilon\) satisfies all assumptions; \(h_P\) is also finite convex. The full original proofs and their dependency chains have **not** been certified by this model calculation. No error in the printed theorem was found. Suggested optional explanatory corollary: state the exact coordinate-logistic law and \(W_1\) coefficient beside the existing simplex sharpness example, explicitly citing the previous TV result rather than re-registering it.

**Affected uses:** quantitative smooth toric-to-tropical concentration, transport metrics on real Monge–Ampère measures, and any attempted normed strengthening of Theorem 21.5.2 or Lemma 21.6.2. No theorem or permanent tag should be changed on this audit branch.

**Coverage:** §21.5 was already partly proof-reviewed in 2026-10-25 and subsequent sessions; §21.1 only supplies contextual conventions. This run has **0 newly first-visited numbered sections, 0 completely certified sections**, and one new selected exact quantitative model. Current ToC inventory remains 25 chapters and 747 numbered sections; it is not a whole-project certificate. The user-excluded Demailly approximation/regularization, dedicated Bergman, L2/OT, multiscale and positivity-loss programme stays **deferred-by-user**, not resolved. No builds, tests, GitHub Actions CI, formal verification, source-body edits, or site publication were performed.
