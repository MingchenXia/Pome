# Quantitative weighted gradient stability and cross-chapter Bedford–Taylor review (2026-11-22)

**Production main SHA:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Proposed audit-only branch:** \`review/mathematical-audit\`. **Status:** direct mathematical-body audit, not an independent transitive proof-chain certificate. Scope excludes Demailly approximation/regularization and the dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof-completion programme in full. Existing notes about those topics remain **deferred-by-user**, neither certified nor resolved.

## Integrated reading-edition files and exact anchors

| Whole section directly read | Exact file on main | Git blob | Actual mathematical physical lines and identifiers |
| --- | --- | --- | --- |
| §7.14 Gradients against positive currents | \`docs/sections/bedford-taylor-products-and-local-capacity--gradients-against-positive-currents/index.html\` | \`520e13d0d2cc8e4a23e43bba61b940d7c5c1f8b2\` | 7–131 within 147 physical HTML lines; Lemma 7.14.3, source \`foundations-of-pluripotential-theory:3CDA1967\`, permanent \`8B33E7CC2E18\`, statement 48–64, proof 66–131; Eq. 7.14.1 permanent \`9148FE66924C\`, Eq. 7.14.4 permanent \`F48E1DFF8563\` |
| §7.16 Relative extremals on bounded hyperconvex domains | \`docs/sections/relative-extremals-on-bounded-hyperconvex-domains/index.html\` | \`c6560283c5ff9e2587ffe93f7f2e7ba687105243\` | 7–187 within 196 lines; Proposition 7.16.1 source \`klimek-pluripotential-theory:7B045988\`, permanent \`11F76749E371\`, lines 16–65; Theorem 7.16.5 source \`klimek-pluripotential-theory:68BF935A\`, permanent \`08DA18E923C1\`, lines 110–187 |
| §15.3 Bounded equations in semipositive big backgrounds | \`docs/sections/equations-with-prescribed-singularities--bounded-equations-in-a-semipositive-big-background/index.html\` | \`84f49b16943ee4e0d5dcf8d8bf59cd815a1ef15f\` | 7–233 within 245 lines; Lemma 15.3.1 source \`non-kahler-pluripotential-theory:09F238FA\`, permanent \`D716F01D638B\`, lines 19–65; Theorem 15.3.3 source \`non-kahler-pluripotential-theory:E540849F\`, permanent \`96A341EAF1D4\`, lines 74–117; Theorem 15.3.5 source \`non-kahler-pluripotential-theory:5F2BC208\`, permanent \`A972C11565ED\`, lines 125–226 |

The physical anchors are in the integrated generated HTML, not inherited source theorem numbers. Source names above are provenance, **not** instructions to inspect excluded research programmes.

## POME-BT-CURRENT-WEIGHTED-UNIFORM-C0-GRADIENT-RATE-001

**Severity:** low. **Status:** **verified conditional deduction**, not a confirmed error, proof gap, or proposed change to the printed Lemma 7.14.3. **Dependence:** the already printed locally bounded-PSH energy-gradient construction and strong convergence under decreasing smooth approximation in §7.14.3; no complete certification of its transitive Bedford–Taylor prerequisites is claimed.

**Claim.** Fix an open \(U\subset\mathbb C^n\), a closed positive current \(\Theta\) of bidimension \((1,1)\), and \(K\Subset U\). Choose a nonnegative \(\chi\in C_c^\infty(U)\) with \(\chi=1\) on a neighborhood of \(K\); put \(\mu=\Theta\wedge\beta\) and
\[
 V_\chi=\bigl|\mathrm{dd}^{\mathrm c}\chi\wedge\Theta\bigr|(U)<\infty.
\]
Suppose \(u,v\in\mathrm{PSH}(U)\) obey \(|u|,|v|\le M\) and \(|u-v|\le\delta\) on a neighborhood of \(\operatorname{Supp}\chi\), with \(M,\delta\ge0\). Let \(H\) be the bounded positive-semidefinite matrix density of \(\Theta\) from §7.14 (in particular \(H\) has trace \(1/\pi\)). Then
\[
\boxed{\quad
 \int_K |H^{1/2}\partial u-H^{1/2}\partial v|^2\,d\mu
 \le \left(2M\delta+\tfrac12\delta^2\right)V_\chi.\quad} \tag{A}
\]
The \(H^{1/2}\partial u\) and \(H^{1/2}\partial v\) here are the *intrinsic \(L^2_{\mathrm{loc}}(\mu)\) energy gradients* of §7.14, not ordinary ambient derivatives on the support of a singular current. Consequently **every** locally uniformly convergent, locally uniformly bounded family (including an **arbitrary directed net**) of PSH functions has strongly converging \(\Theta\)-weighted energy gradients on each compact set. No monotonicity of the family is required. The local \(O(\sqrt\delta)\) rate in the weighted \(L^2\) seminorm is generally optimal.

**Complete proof of (A) from printed §7.14.** Take the *same* family of local radial mollifiers for \(u,v\) on a slightly smaller neighborhood of \(\operatorname{Supp}\chi\), and write \(u_\varepsilon,v_\varepsilon\). Both are smooth PSH, decrease individually to \(u,v\), remain bounded in absolute value by \(M\), and satisfy \(\|u_\varepsilon-v_\varepsilon\|_\infty\le\delta\) on \(\operatorname{Supp}\chi\) when \(\varepsilon\) is sufficiently small. Set \(w_\varepsilon=u_\varepsilon-v_\varepsilon\). Although \(w_\varepsilon\) is not PSH, the *smooth* identity used in §7.14.3 Step 1 applies:
\[
 \int\chi\,\mathrm dw_\varepsilon\wedge\mathrm d^{\mathrm c}w_\varepsilon\wedge\Theta
 =\tfrac12\int w_\varepsilon^2\,\mathrm{dd}^{\mathrm c}\chi\wedge\Theta
   -\int\chi w_\varepsilon\,
          (\mathrm{dd}^{\mathrm c}u_\varepsilon-
           \mathrm{dd}^{\mathrm c}v_\varepsilon)\wedge\Theta.
\]
The first term on the right is at most \(\delta^2 V_\chi/2\) in absolute value. Both \(\mathrm{dd}^{\mathrm c}u_\varepsilon\wedge\Theta\) and \(\mathrm{dd}^{\mathrm c}v_\varepsilon\wedge\Theta\) are positive measures. Because \(\Theta\) is closed and \(\chi\) has compact support, integration by parts gives
\[
 0\le\int\chi\,\mathrm{dd}^{\mathrm c}u_\varepsilon\wedge\Theta
 =\int u_\varepsilon\,\mathrm{dd}^{\mathrm c}\chi\wedge\Theta
 \le M V_\chi
\]
and the identical estimate for \(v_\varepsilon\). Thus
\[
 \int\chi\,\mathrm dw_\varepsilon\wedge\mathrm d^{\mathrm c}w_\varepsilon\wedge\Theta
 \le \left(\tfrac12\delta^2+2M\delta\right)V_\chi.
\]
By (7.14.1), the integrand is \(|H^{1/2}\partial u_\varepsilon-H^{1/2}\partial v_\varepsilon|^2\,d\mu\); since \(\chi=1\) on \(K\), the \(K\)-energy is at most the left side. Apply separately the strong local \(L^2(\mu)\) convergence of \(H^{1/2}\partial u_\varepsilon\) and \(H^{1/2}\partial v_\varepsilon\) in Lemma 7.14.3. The difference therefore converges strongly and yields (A). The estimate is independent of the mollification scale, so it passes to the limit without any unsupported interchange of varying current measures. For a directed net \(u_\alpha\to u\) locally uniformly, apply (A) to each pair \((u_\alpha,u)\) with \(\delta_\alpha=\sup|\!u_\alpha-u\!|\to0\) and one uniform local bound \(M\); the resulting numerical inequality holds on the original directed set, **without selecting a sequence**.

**Optimality of the square-root exponent even for smooth PSH functions.** Work in complex dimension one on \(U=(-2,2)^2\subset\mathbb C\), with \(\Theta=1\) (the closed positive bidimension-\((1,1)\) current), \(K=[-1,1]^2\), \(\beta=(i/2)\,dz\wedge d\bar z=dx\,dy\), so \(H=1/\pi\), \(\mu=dx\,dy\). For integers \(m\ge1\), set \(k_m=m\pi\), \(\delta_m=k_m^{-2}\), and
\[
 u(z)=|z|^2,\qquad v_m(z)=|z|^2+\delta_m\cos(k_m\operatorname{Re}z).
\]
Then \(\Delta v_m=4-\cos(k_mx)\ge3\), hence every \(v_m\) is smooth PSH; all \(u,v_m\) are bounded uniformly by \(9\) on \(U\), and \(\|u-v_m\|_{L^\infty(U)}=\delta_m\to0\). Nevertheless,
\[
\begin{aligned}
 \int_K |H^{1/2}\partial(v_m-u)|^2\,d\mu
 &=\frac1\pi\frac{\delta_m^2 k_m^2}{4}
     \left(\int_{-1}^1\sin^2(k_mx)\,dx\right)
     \left(\int_{-1}^1dy\right)\\
 &=\frac{\delta_m}{2\pi}.
\end{aligned}
\]
Thus the weighted \(L^2\)-gradient norm is \((2\pi)^{-1/2}\sqrt{\delta_m}\), and no uniformly better Hölder exponent than \(1/2\) is possible under only the stated boundedness and uniform-error assumptions. Unlike the existing **POME-BT-NORMAL-TRACE-GRADIENT-OSCILLATION-001**, this is an *intrinsic weighted energy norm*, not an uncontrolled ambient normal derivative on a current's support. It is also distinct from the prior bounded-distributional-Hessian \(C^0\)-to-\(C^1\) estimate: here no ambient Hessian \(L^\infty\) bound is assumed.

**Proposed optional correction/extension:** add a separate corollary after Lemma 7.14.3 with estimate (A) and a precise note that it concerns the \(H\)-weighted gradient rather than full trace gradients; retain original lemma, permanent tags, and historical attribution. **Affected dependents:** cutoff/chain-rule estimates referring to §7.14, especially closedness arguments for non-pluripolar products around §13.3.1, *when the relevant approximants are locally uniformly convergent*. This does not prove stability for arbitrary decreasing unbounded truncations and does not repair their separate inputs.

## Other complete direct reviews (no new confirmed printed error)

**§7.14 (all 7–131):** checked coefficient-density/Hermitian matrix positivity via rational forms and trace, Borel square root, the normalization \(1/\pi\), first-derivative order-zero representation, the decreasing-gradient Cauchy argument with weighted BT convergence, \(\chi\)-energy Cauchy–Schwarz and the \(C^1\) chain rule. The sharpness model above crosschecks the \((i/2\pi)\partial w\wedge\bar\partial w\) normalization. Remaining transitive inputs: §5.3.7 positive-current coefficients, §2.8.1 Radon–Nikodym, §7.3.7 weighted BT theorem and local PSH convolution. Not independently certified as a chain.

**§7.16 (all 7–187):** checked decreasing compact-set raw extremals, negative PSH exhaustion and boundary barriers, continuous norm-ball extremals and Dini smoothing, maximality outside a compact set, compact-exhaustion domain monotonicity, Josefson/pluripolar/zero-outer-capacity equivalences, proper-map fiber maxima, and Theorem 7.16.5 inner/outer capacity and increasing/decreasing set limits. The proof correctly keeps outer capacity on arbitrary sets and allows infinite capacities for nonrelatively compact sets; it does *not* claim finite total capacity of the ambient domain. Genuine earlier inputs: Josefson theorem, BT monotone convergence, local cap comparison, bounded maximality and comparison; not re-certified. Earlier finite-proper-map and exact polydisc capacity findings are distinct and **not** relogged.

**§15.3 (all 7–233):** checked semipositive big-background strict barrier \( \theta_\rho\ge a\omega\); weighted density \((-\rho)^{2n}f\), the convex substitution \(\chi(t)=-t^{-1}-1\) with \(\chi'=t^{-2}\) and \(\chi''=-2t^{-3}>0\) for \(t\le-1\), and the lower MA subsolution bound from \(|h|\le(1+aC)(-\rho)\). Checked monotonically decreasing \(\theta+\varepsilon\omega\) exponential solutions, fixed-background mixed-product expansion, and the normalized-equation argument with upper tail maxima, lower rooftop envelopes, contact decomposition and strict domination. The normalized potential is *not* asserted unique (consistent with §14.26.1); the scalar is. Dependencies on the printed Hermitian \(L^p\) existence/estimates in §14.19, lower-barrier comparison, envelope contact inequalities and bounded BT convergence remain **conditional**. This checks the section outside the excluded regularization programme, without reading or extending that programme.

## Classification, coverage and boundaries

- New findings: **one** (low / verified conditional deduction \`POME-BT-CURRENT-WEIGHTED-UNIFORM-C0-GRADIENT-RATE-001\`); **zero** new confirmed printed errors, **zero** newly certified complete proof chains.
- Whole current integrated mathematical sections directly read: **§7.14, §7.16, §15.3**. Selected dependencies noted as context only. Historical first-visit status is not inferred.
- All preceding identified errors, gaps, unresolved external dependencies and deferred-by-user programmes remain on their previous ledgers. No duplication or canonicalization change is claimed.
- Mathematical source/documentation changes are **proposed only**; repository write scope is solely audit Markdown on \`review/mathematical-audit\`. No code tests/build, CI, formal proofs, main/source/registry/permanent-tag/website publication or PR merge was performed.
