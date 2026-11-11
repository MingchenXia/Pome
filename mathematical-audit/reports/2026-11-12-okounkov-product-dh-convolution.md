# Product Okounkov test curves: the exact Duistermaat–Heckman convolution coefficient

**Finding ID:** POME-OKO-DH-PRODUCT-CONVOLUTION-001  
**Date:** 2026-11-12  
**Severity / classification:** low / **verified conditional deduction**. No printed theorem is declared false.  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

## Integrated source and precise anchors

1. `docs/sections/the-theory-of-okounkov-bodies--okounkov-test-curves/index.html` at blob `20ff3089e62dd1c8349e8bcc077ec64605a9788b`, §19.6. Definition **19.6.1**, source `sgpt:26A94CBB`, permanent `ACD722F45231`, physical lines **16–44**; Definition **19.6.5**, `sgpt:9E9C0297` / `F0D4BAA63D8A`, **90–107**; Definition **19.6.7**, `sgpt:2E276BD3` / `7B20D9977149`, **113–126**; Definition **19.6.18**, `sgpt:09132002` / `51940EF88F4F`, **329–334**. Proposition **19.6.19**, `sgpt:DE3D564A` / `F397AFA38927`, **338–366**, was read for moment conventions, not globally re-proved.
2. `docs/sections/non-archimedean-pluripotential-theory/index.html` at blob `8448d710690ebe1cc28040f9611d05c9d008a961`, §22.1. Definition **22.1.55**, `sgpt:115B0C00` / `9ADEFD2FF381`, physical lines **902–912**; Theorem **22.1.56**, `sgpt:420C36E9` / `0AD7F80A793D`, **916–931** (the remainder of its proof continues through line 997). The factor `n!` in Definition 22.1.55 is essential.

## Statement proved at the abstract Okounkov-test-curve level

Let \(\Delta_i\subset\mathbb R^{n_i}\), \(i=1,2\), be compact convex bodies of positive Euclidean volumes, with \(n_i\ge1\). Let \(G_i:\Delta_i\to[-\infty,\infty)\) be concave, upper-semicontinuous, finite on the interior: exactly the test-function hypotheses of Definition 19.6.5. Write \(n=n_1+n_2\), \(\Delta=\Delta_1\times\Delta_2\) and
\[
G(x_1,x_2)=G_1(x_1)+G_2(x_2),\qquad -\infty+c=-\infty.
\]
Then \(G\) is an admissible test function on \(\Delta\) and hence, by the Legendre correspondence, defines an Okounkov test curve. Put
\[
\nu_i=n_i!(G_i)_*(\mathbf1_{\Delta_i}\,dx_i),\qquad
\nu=n!G_*(\mathbf1_{\Delta}\,dx_1dx_2).
\]
The exact finite-positive-measure identity is
\[
\boxed{\quad \nu={n!\over n_1!n_2!}\,(\nu_1*\nu_2)
=\binom{n}{n_1}\,(\nu_1*\nu_2).\quad} \tag{1}
\]
In particular, the total masses are \(V_i=n_i!\operatorname{vol}(\Delta_i)\) and
\(V=n!\operatorname{vol}(\Delta)=\binom n{n_1}V_1V_2\). Thus the **probability** DH distributions satisfy
\[
\boxed{\quad {\nu\over V}={\nu_1\over V_1}*{\nu_2\over V_2}.\quad} \tag{2}
\]
For integrable roofs, normalized means add; for square-integrable roofs, normalized variances add. For bounded roofs this extends to all moments and characteristic functions. The same conclusion holds for a finite number of factors with the corresponding multinomial coefficient.

## Complete proof

Concavity follows from the concavity of each \(G_i\), separately in each factor, after adding the two inequalities. Each \(G_i\) has a finite supremum on its compact body (usc and finite somewhere), and is bounded above; therefore the sum is usc, including at points where a summand is \(-\infty\). Both summands are finite in the respective interiors, so \(G\) is finite in \(\operatorname{Int}\Delta\). For any \(t<\sup G_1+\sup G_2\), choose interior \(x_i\) with \(G_1(x_1)+G_2(x_2)>t\); concavity and usc permit such choices even when a supremum is attained only on a boundary face. The closed superlevel \(\Delta_t=\{G\ge t\}\) is thus a compact convex set with nonempty interior. Minkowski concavity follows directly from
\[
(1-s)\Delta_t+s\Delta_{t'}\subseteq\Delta_{(1-s)t+st'}.
\]
Since every interior pair has finite \(G\), the superlevels exhaust \(\operatorname{Int}\Delta\) as \(t\to-\infty\), and their Hausdorff limit is \(\Delta\). This directly verifies Definition 19.6.1; alternatively apply the already printed Lemma 19.6.9 and Theorem 19.6.13.

For any Borel \(B\subset\mathbb R\), the definition and Tonelli/Fubini for bounded indicators give
\[
\begin{aligned}
\nu(B)
&=n!\int_{\Delta_1}\int_{\Delta_2}
\mathbf1_B(G_1(x_1)+G_2(x_2))\,dx_2\,dx_1\\
&={n!\over n_1!n_2!}\int_{\mathbb R^2}
\mathbf1_B(s+t)\,d\nu_1(s)\,d\nu_2(t)\\
&=\binom n{n_1}(\nu_1*\nu_2)(B).
\end{aligned}
\]
Values \(-\infty\) occur only on subsets of the convex bodies' boundaries, because \(G_i\) is finite on the interiors; they therefore carry zero Lebesgue mass. Equation (1) is an equality of ordinary finite Borel measures on \(\mathbb R\), without any interchange of singular Monge–Ampère limits. Integrating \(1\) gives the mass relation, hence (2). For means and variances, apply Fubini only after the stated integrability hypotheses; independence of the two product Lebesgue variables gives additivity. No unqualified moment passage is used.

## Explicit sharp normalization test

For \(n_1=n_2=1\), \(\Delta_1=\Delta_2=[0,1]\), \(G_1(x)=-x\), \(G_2(y)=-y\), each \(\nu_i\) is Lebesgue measure on \([-1,0]\) of total mass 1. The product measure has the **density**
\[
{d\nu\over dt}=
\begin{cases}
2(t+2),&-2<t<-1,\\
-2t,&-1<t<0,\\
0,&\text{otherwise}.
\end{cases}
\]
Direct integration yields
\[
\nu(\mathbb R)=2,\quad \int t\,d\nu=-2,\quad
\int t^2\,d\nu={7\over3}.
\]
Thus the probability DH mean is \(-1\) and its variance is \(1/6\). Omitting the binomial factor would incorrectly assign total mass 1 rather than 2 to the two-dimensional product. As an intersection-number crosscheck only, the class of \(\mathcal O(1,1)\) on \(\mathbb P^1\times\mathbb P^1\) has self-intersection 2; **we do not claim here that an arbitrary abstract roof is geometrically realized by an \(\mathcal I\)-model non-Archimedean potential**.

## Interpretation, status and dependencies

This proves a new **abstract convex/test-curve consistency check** for the normalization in §§19.6 and 22.1. It is not a false-theorem finding, nor a full proof of Theorem 22.1.56. A geometric product theorem for \(\mathrm{PSH}^{\mathrm{NA}}\) would additionally require showing that the exterior-product construction matches the selected geometric Okounkov test curves, including admissibility, flag and trace compatibility; these steps were **not** established here. The printed moment identity, flag independence, and general geometric realization remain independently uncertified.

**Proposed addition (not made to source):** if a geometric exterior-product compatibility theorem is supplied, record (1) with its binomial coefficient as a corollary to Definition 22.1.55 and record (2) for normalized DH probabilities. The potentially affected readers are product-volume comparisons, moment calculations and geometric product formulations. No production theorem needs correction on the present evidence.

**Deduplication:** existing §19.6 reports concern tail moments, Wasserstein rates, convergence and the separate confirmed issue in Proposition 19.6.16; existing §22.1 reports concern flag independence and spectral tails. None records the finite-product **multinomial convolution factor**. These statuses are unchanged. No Demailly approximation/regularization, dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas or positivity-loss argument was consulted.

**Exact coverage:** Direct proof-level reading of the definitions and cited portions above in previously sampled numbered §§19.6 and 22.1; **0** newly first-visited numbered sections, **0** fully certified mathematical sections; current main table of contents remains **25 chapters, 747 sections**. No build, tests, CI, formal proof, site publication, main/source/registry/tag change or global theorem certification.
