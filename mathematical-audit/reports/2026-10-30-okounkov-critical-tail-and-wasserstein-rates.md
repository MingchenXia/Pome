# An Okounkov test-curve model with exact critical moment thresholds and Wasserstein rates

**Audit date:** 2026-10-30. **Reviewed production \`main\`:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Finding:** \`POME-OKO-ROOF-CRITICAL-WASSERSTEIN-001\` — **low / verified conditional deduction**. The printed definitions and moment/convergence assertions are **not false**; this is a new explicit model, not a repair of the previously recorded issue in Proposition 19.6.16. No entire reading section or underlying geometric non-Archimedean realization has been certified.

## Exact integrated source and version anchors

- \`docs/sections/the-theory-of-okounkov-bodies--okounkov-test-curves/index.html\`, production blob **\`20ff3089e62dd1c8349e8bcc077ec64605a9788b\`**, §19.6, section permanent tag \`BC31851ECB21\`. Definition **19.6.1**, source \`sgpt:26A94CBB\`, permanent tag \`ACD722F45231\`, physical lines **16–45** (positive-volume compact convex bodies, concave Minkowski test curves); Definition **19.6.5**, source \`sgpt:9E9C0297\`, permanent tag \`F0D4BAA63D8A\`, lines **89–109** (upper-semicontinuous extended-valued concave roofs); Definition **19.6.7**, source \`sgpt:2E276BD3\`, tag \`7B20D9977149\`, lines **112–130** (superlevel/inverse Legendre construction); Lemma **19.6.9**, source \`sgpt:02AA676E\`, tag \`21BC38898B4A\`, lines **137–159** (well-definedness, used only conditionally).
- Same integrated file: Definition **19.6.18**, source \`sgpt:09132002\`, tag \`51940EF88F4F\`, physical lines **328–334**, defines \(\operatorname{DH}(\Delta_\bullet)=G[\Delta_\bullet]_\#\lambda\). Proposition **19.6.19**, source \`sgpt:DE3D564A\`, tag \`F397AFA38927\`, lines **337–368**, states extended integer moment identities; Lemma **19.6.22**, source \`sgpt:B9C8ADE8\`, tag \`9C05354365F4\`, lines **370–408**, gives weak convergence of decreasing test curves, with an actual finite endpoint condition. We do **not** invoke the separately disputed increasing-direction Proposition 19.6.16.
- Context only: \`docs/sections/non-archimedean-pluripotential-theory/index.html\`, main blob **\`8448d710690ebe1cc28040f9611d05c9d008a961\`**, Definition 22.1.55 (source \`sgpt:115B0C00\`, tag \`9ADEFD2FF381\`, lines **907–912**) and Theorem 22.1.56 (source \`sgpt:420C36E9\`, tag \`0AD7F80A793D\`, lines **915–997**). Their geometric flag/volume inputs are **not** checked here; the abstract example below is not asserted to arise from an arbitrary geometric NA metric.
- New structural-only inventory in another subject: \`docs/sections/gauduchon-metrics-and-linear-mass/index.html\`, main blob **\`02d635e918120c4026c38d14119db9377eefe61f\`**, §11.3 source \`non-kahler-pluripotential-theory:67BD8090\`, permanent section tag **\`1009E65ECC4C\`**, lines **5–20**. This page is a subject introduction discussing Gauduchon conservation and positivity, not an environment containing a proof; it receives **expository/context-only** coverage, not a mathematical certification.

## Precisely stated new model

Fix an integer \(n\geq1\), \(\Delta=[0,1]^n\), \(\alpha>0\), and \(0<\varepsilon<1/4\). On the interior of \(\Delta\) define
\[
 G_\alpha(x)=-x_1^{-\alpha}-(1-x_1)^{-\alpha},
 \qquad
 G_{\alpha,\varepsilon}(x)=-(x_1+\varepsilon)^{-\alpha}
                         -(1-x_1+\varepsilon)^{-\alpha}.
\]
Extend \(G_\alpha=-\infty\) on the two facets \(x_1=0,1\). Let
\(\Delta_\bullet=\Delta[G_\alpha]_\bullet\) and
\(\Delta^\varepsilon_\bullet=\Delta[G_{\alpha,\varepsilon}]_\bullet\)
be their superlevel test curves as defined in 19.6.7, and set
\(\mu=(G_\alpha)_\#(\lambda|_\Delta)\),
\(\mu_\varepsilon=(G_{\alpha,\varepsilon})_\#(\lambda|_\Delta)\).

**Claims, all proved below:**

1. Both are valid Okounkov test curves. \(\Delta^\varepsilon_\bullet\) is bounded, \(\Delta_\bullet\) is not, and \(\Delta^\varepsilon_\bullet\) decreases to \(\Delta_\bullet\) as \(\varepsilon\downarrow0\). In particular \(\mu_\varepsilon\Rightarrow\mu\) **narrowly**, i.e. against all \(C_b(\mathbb R)\), not merely against \(C_c\). The terminal parameters are
\[
 (\Delta^\varepsilon)_{\max}=-2(1/2+\varepsilon)^{-\alpha}
 \searrow -2^{\alpha+1}=\Delta_{\max}.
\]
2. The exact negative-tail exponent and all positive absolute-moment thresholds are
\[
 \boxed{\quad
 \lim_{R\to\infty}R^{1/\alpha}\,\mu((-\infty,-R))=2,\qquad
 \int_{\mathbb R}|t|^p\,d\mu(t)<\infty\ \Longleftrightarrow\ \alpha p<1
 \quad(p>0).\quad}
\]
For \(p>0\), as \(\varepsilon\downarrow0\), the bounded roofs have
\[
 \int|t|^p\,d\mu_\varepsilon(t)
 \sim
 \begin{cases}
 2\log(1/\varepsilon),&\alpha p=1,\\
 \dfrac{2}{\alpha p-1}\,\varepsilon^{1-\alpha p},&\alpha p>1.
 \end{cases}
\]
For \(\alpha p<1\), instead their \(p\)-th moments converge to the finite moment of \(\mu\).
3. For **\(p\geq1\)** with \(\alpha p<1\), the one-dimensional optimal monotone coupling gives an **exact** identity and a sharp small-\(\varepsilon\) asymptotic:
\[
 \begin{split}
 W_p(\mu_\varepsilon,\mu)^p
 &=\int_0^1\left[
 x^{-\alpha}-(x+\varepsilon)^{-\alpha}
 +(1-x)^{-\alpha}-(1-x+\varepsilon)^{-\alpha}
 \right]^p\,dx,\\
 \boxed{\quad
 \lim_{\varepsilon\downarrow0}
 \varepsilon^{\alpha p-1}W_p(\mu_\varepsilon,\mu)^p
 =2\int_0^\infty
       \left[t^{-\alpha}-(t+1)^{-\alpha}\right]^p\,dt
 \in(0,\infty).\quad}
 \end{split}
\]
For \(p=1\), necessarily \(0<\alpha<1\), the formula becomes exactly
\[
 \boxed{\quad
 W_1(\mu_\varepsilon,\mu)
 =\frac{2}{1-\alpha}
 \bigl[1-(1+\varepsilon)^{1-\alpha}
       +\varepsilon^{1-\alpha}\bigr]
 \sim\frac{2}{1-\alpha}\varepsilon^{1-\alpha}.\quad}
\]
Thus narrow DH convergence can hold for **bounded** test curves while \(p\)-moment uniform integrability fails; it cannot generally be promoted to \(W_p\) convergence without a moment hypothesis. The failure occurs with the **same compact convex body**, a fixed total DH mass of one, and finite, convergent terminal parameters. For \(\alpha p\geq1\), the limit is not in \(\mathcal P_p(\mathbb R)\), so finite \(W_p\) convergence is impossible.

## Complete elementary verification

The functions \(t\mapsto-(t+\varepsilon)^{-\alpha}\) are strictly concave for \(t>0\) because their second derivatives equal \(-\alpha(\alpha+1)(t+\varepsilon)^{-\alpha-2}\). This includes the extended-value limit at the facets. Both roofs are upper semicontinuous and finite on the interior of \(\Delta\). Their superlevel sets at every \(\tau\) strictly below the maximum are products of a nondegenerate closed central interval in the first coordinate with \([0,1]^{n-1}\), so they are positive-volume compact convex bodies; Minkowski concavity follows from roof concavity. As \(\tau\to-\infty\), they converge in Hausdorff distance to \(\Delta\). This checks the actual conditions of Definitions 19.6.1, 19.6.5 and 19.6.7, rather than assuming an arbitrary measurable distribution is a DH measure. Each bounded roof is a bounded test curve. Since \(G_{\alpha,\varepsilon}\downarrow G_\alpha\) at every interior point, the superlevel curves decrease at every fixed \(\tau<\Delta_{\max}\); their endpoints decrease as displayed. For \(f\in C_b(\mathbb R)\), pointwise convergence and boundedness give \(\int_\Delta f(G_{\alpha,\varepsilon})\,d\lambda\to\int_\Delta f(G_\alpha)\,d\lambda\) by ordinary dominated convergence (the two facets have zero volume). This proves narrow convergence directly, without a sequential-compactness or varying-domain assumption.

For \(R>2^{\alpha+1}\), define \(r_R\in(0,1/2)\) uniquely by
\(r_R^{-\alpha}+(1-r_R)^{-\alpha}=R\).
The left-hand expression is strictly decreasing on \((0,1/2)\).
The set where \(G_\alpha<-R\) is precisely the two endpoint strips
\(x_1<r_R\) and \(x_1>1-r_R\), hence \(\mu((-\infty,-R))=2r_R\).
Since \((1-r_R)^{-\alpha}\to1\), the defining equation gives
\(Rr_R^\alpha\to1\), yielding the stated exact tail constant.
Moreover, near either endpoint \(|G_\alpha(x)|^p\sim x_1^{-\alpha p}\),
so its integral is finite exactly for \(\alpha p<1\).

For the truncated roofs, let
\(F_\varepsilon(x)=(x+\varepsilon)^{-\alpha}
 +(1-x+\varepsilon)^{-\alpha}\).
On \(0<x<\delta<1/2\), the second term is uniformly bounded,
whereas the first is the singular term. For every fixed \(p>0\),
the ratio \(F_\varepsilon(x)^p/(x+\varepsilon)^{-\alpha p}\)
tends uniformly to \(1\) as \(\delta\downarrow0\)
(up to an error \(O(\delta^\alpha)\), uniformly for small \(\varepsilon\)).
The middle interval contributes \(O_\delta(1)\).
Integrating \((x+\varepsilon)^{-\alpha p}\) on each of two endpoint
intervals gives respectively \(2\log(1/\varepsilon)+O(1)\) at
\(\alpha p=1\), and
\(2\varepsilon^{1-\alpha p}/(\alpha p-1)(1+o(1))\) for
\(\alpha p>1\).
When \(\alpha p<1\), \(0\leq F_\varepsilon^p\leq F_0^p\in L^1\),
and dominated convergence gives the moment limit.

The random variable \(r=\min(x_1,1-x_1)\) under uniform \(\lambda|_\Delta\)
has density \(2\,dr\) on \((0,1/2)\).
Both roofs are strictly **increasing** functions of \(r\):
their derivatives are positive for \(r<1/2\).
Therefore the joint law obtained by using the same \(r\) is a
monotone coupling on the real line. The uncrossing inequality for
the convex cost \(|s-t|^p\), \(p\geq1\), proves that this coupling
is optimal; equivalently, it is the quantile coupling.
This proves the **equality**, not merely an upper bound, in the
displayed \(W_p^p\) formula.

For the sharp rate split the error on \(0<r<1/2\) into
\[
 h_\varepsilon(r)=r^{-\alpha}-(r+\varepsilon)^{-\alpha},
 \qquad
 e_\varepsilon(r)=(1-r)^{-\alpha}-(1-r+\varepsilon)^{-\alpha}.
\]
The second term is uniformly \(O(\varepsilon)\).
For the first, changing variables \(r=\varepsilon t\) gives exactly
\[
 \int_0^{1/2}h_\varepsilon(r)^pdr
 =\varepsilon^{1-\alpha p}
  \int_0^{1/(2\varepsilon)}
  [t^{-\alpha}-(t+1)^{-\alpha}]^pdt.
\]
The integrand behaves as \(t^{-\alpha p}\) at zero and as
\(\alpha^p t^{-(\alpha+1)p}\) at infinity. Under
\(p\geq1\) and \(\alpha p<1\), both ends are integrable.
Since \(1/p-\alpha<1\), the \(O(\varepsilon)\) term is negligible
in \(L^p\) compared with the main size
\(\varepsilon^{1/p-\alpha}\); Minkowski's inequality proves the
claimed positive finite limit.
For \(p=1\), the ordered coupling also gives
\(W_1=\int(G_{\alpha,\varepsilon}-G_\alpha)\,d\lambda\);
integrating the two power differences yields the closed formula.

For **integer** \(m\geq1\), Proposition 19.6.19 must retain its
**extended** moment interpretation: if \(\alpha m\geq1\),
\(\int t^m d\mu(t)\) equals \(-\infty\) for odd \(m\), and
\(+\infty\) for even \(m\). The example therefore corroborates,
rather than contradicts, the printed moment theorem.

## Disposition, comparison with historical findings, and precise scope

This is an **optional explicit example** after Definitions 19.6.7/19.6.18 or Proposition 19.6.19; no correction of the printed result is necessary. It gives a sharp moment/transport boundary for applications of Lemmas 19.6.22–23 and the abstract DH construction. Related uses in §22.1 require independent geometric realizability and their own \(n!\) normalization; neither is asserted here. It is **not** the older \`POME-NA-DH-W1-PROFILE-001\` (which assumes **finite** absolute first moments and relates *two* models via profile differences) and **not** the already confirmed endpoint hypothesis issue \`POME-OKO-INCREASING-TC-REPAIR-001\` in Proposition 19.6.16. The previously recorded geometric-ray moment spectrum \`POME-RADIAL-MOMENT-SPECTRUM-001\` is also distinct from this convex-roof DH example.

**New mathematical scope:** one explicit family of bounded/unbounded **abstract** Okounkov test curves with complete tail, arbitrary \(p\)-moment, narrow convergence and sharp Wasserstein-rate proofs, attached to selected Definitions 19.6.1/.5/.7/.18, Proposition 19.6.19 and Lemma 19.6.22. Prior theorem proofs, general Okounkov-body existence/continuity, unbounded geometric NA inputs, and all of §§19.6/22.1 are **not** certified.

**New cross-chapter structural scope:** first direct reading of §11.3 Gauduchon introduction, **expository only**. The historical coverage matrix remains **25 chapters / 747 numbered current-ToC sections / zero whole-section certifications**. Every previously unresolved or confirmed error, proof gap, genuine duplicate, external dependency and deferred note retains its existing status.

**User-excluded programme:** Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof completion remain **deferred-by-user**, not reviewed, solved or certified. No source-body/registry/tag edit, no production \`main\` change, no build, tests, CI, publication or formal verification.
