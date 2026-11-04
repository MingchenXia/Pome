# Bedford–Taylor capacity: homogeneous exponent and compact localization

**Date (Asia/Shanghai):** 2026-11-05. **Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
**Integrated reading file:** \`docs/sections/bedford-taylor-products-and-local-capacity--bounded-measurable-densities/index.html\`,
blob \`762b841b0cb243784dc988f04dbf2779da66c469\`.
This is a fresh **proof-level** check of Lemma 7.10.1 and the negative-tail estimate in the proof of Theorem 7.10.2, not a complete review of the section or its Bedford–Taylor prerequisites.

- **Lemma 7.10.1:** source label \`foundations-of-pluripotential-theory:74804636\`; permanent tag \`C09E42A43E93\`; printed statement physical lines **11–13**, proof **19–33**.
- **Theorem 7.10.2:** source label \`foundations-of-pluripotential-theory:9C25B561\`; permanent tag \`C9116FCEFCD2\`; statement physical lines **38–45**; reviewed proof segment **64–78**, with barriers and bounded-mass assumptions at **54–62**. Equation (7.9.3), source tag \`0390D064\` / permanent \`B8751A529320\`, is **context only** (line 42).
- **Standing normalization:** \(\eta=dd^c|z|^2\), \(dd^c=\frac{i}{2\pi}\partial\bar\partial\). Thus \(\eta^n=(n!/\pi^n)\,dV_{2n}\) and \(\int_{B_1}\eta^n=1\).

## POME-BT-CAP-EXPONENT-HOMOGENEITY-001

**Severity:** low. **Status:** verified conditional deduction. **Printed theorem:** correct; no false mathematical statement is asserted.

### Exact homogeneous test

Let \(n\ge1\), \(D=B_1\subset\mathbb C^n\), \(\lambda>0\), and set
\[
q(z)=2(|z|^2-1),\qquad u_\lambda=\lambda q,\qquad
v=0,\qquad s_\lambda=\lambda/4,\qquad t_\lambda=\lambda.
\]
These are smooth bounded plurisubharmonic functions on \(D\), with
\[
\{u_\lambda<v-s_\lambda\}=B_{\sqrt{7/8}}\Subset D,\qquad
\{u_\lambda<v-s_\lambda-t_\lambda\}=B_{\sqrt{3/8}}.
\]
Since \(dd^c u_\lambda=2\lambda\eta\), direct integration yields
\[
\int_{\{u_\lambda<v-s_\lambda\}}(dd^c u_\lambda)^n
=(2\lambda)^n(7/8)^n=(7\lambda/4)^n.
\]
The capacity \(C_n=\mathrm{Cap}_{B_1}(B_{\sqrt{3/8}})\) is a fixed positive finite number: it is positive by the admissible test \(w(z)=|z|^2-1\) (giving \(C_n\ge(3/8)^n\)), and finite by the local Bedford–Taylor capacity estimate for relatively compact balls. Hence the printed inequality is a genuinely nonvacuous estimate
\[
\lambda^n C_n\le(7\lambda/4)^n
\]
for every \(\lambda>0\). If \(t^n\) in Lemma 7.10.1 were replaced by \(A\,t^\alpha\) for any universal \(A>0\), uniformly over *all* admissible \(u,v,s,t\), this model would require
\(A C_n\lambda^\alpha\le(7/4)^n\lambda^n\) for every \(\lambda>0\).
For \(\alpha<n\), take \(\lambda\downarrow0\); for \(\alpha>n\), take \(\lambda\uparrow\infty\). Both are impossible. Thus **the exponent \(n\) is forced by homogeneity** in the unrestricted lemma; this does not claim sharpness of its numerical coefficient \(1\).

### Extracted quantitative lower tail and its scaling

Independently of any convergence sequence, assume \(u,v\) are locally bounded PSH on \(B_1\),
\(\{u<v-\delta\}\Subset B_1\), \(\delta>0\), and
\((dd^c u)^n\le M\eta^n\) with \(M\ge0\). Lemma 7.10.1 with \(s=t=\delta\), positivity, and Chebyshev give
\[
\boxed{\quad
\mathrm{Cap}_{B_1}(\{u<v-2\delta\})
\le\frac{M}{\delta^{n+1}}\int_{B_1}(v-u)_+\,\eta^n.
\quad}
\tag{BT-lower-tail}
\]
Indeed, the integration region is \(\{u<v-\delta\}\), on which \((v-u)_+>\delta\). This is precisely the quantitative mechanism used in Theorem 7.10.2, proof physical lines **66–75**; the published theorem then uses quasi-continuity to pass to *outer* capacity on compact subsets. The displayed bound is a verified deduction from the printed lemma, not a new global capacity-continuity theorem.

The exponent \(n+1\) is also fixed by joint potential/density scaling if the bound is required for *all* \(M,\delta>0\) with a universal numerical constant. In the same model, set \(\delta_\lambda=\lambda/4\), \(u_\lambda=2\lambda(|z|^2-1)\), \(v=0\), and \(M_\lambda=(2\lambda)^n\). Then
\[
\{u_\lambda<v-\delta_\lambda\}=B_{\sqrt{7/8}},\qquad
\{u_\lambda<v-2\delta_\lambda\}=B_{\sqrt{3/4}},
\]
and the normalized radial integral gives
\[
\int_{B_1}(v-u_\lambda)_+\,\eta^n
=2\lambda\bigl(1-\tfrac{n}{n+1}\bigr)
=\frac{2\lambda}{n+1}.
\]
The left capacity is a fixed strictly positive finite constant. Replacing \(\delta^{-(n+1)}\) in (BT-lower-tail) by \(\delta^{-\beta}\) with a *single* constant uniform over \(M,\delta\) would give a right side proportional to \(\lambda^{n+1-\beta}\), contradicting the fixed positive left side as \(\lambda\downarrow0\) if \(\beta<n+1\), or as \(\lambda\uparrow\infty\) if \(\beta>n+1\). This is **scaling optimality only**, not coefficient optimality, and assumes constants have no hidden dependence on the potential scale.

## POME-BT-CAP-LOCALIZATION-NECESSARY-001

**Severity:** low. **Status:** verified conditional deduction. **Printed theorem:** correct.

The relatively compact strict comparison set is substantive, not a decorative boundary assumption. Let \(D=B_1\), \(u\equiv0\), \(v\equiv2\), \(s=0\), \(t=1\). Both \(u,v\) are smooth bounded PSH, but
\(\{u<v-s\}=\{u<v-s-t\}=D\), not relatively compact. The right side of Lemma 7.10.1 is
\(\int_D(dd^c u)^n=0\), while the left side is
\(\mathrm{Cap}_D(D)\ge\int_D(dd^c(|z|^2-1))^n=1>0\).
Thus the same conclusion **cannot** hold under only local boundedness and positivity, without a replacement boundary/localization hypothesis. This does **not** contradict the printed lemma, which explicitly assumes relative compactness.

## Comparison with integrated proof and dependency ledger

- Lines **20–32** prove the lemma using the compactly supported strict comparison set, the *bounded* Bedford–Taylor comparison principle (Theorem 7.3.11), mixed-product positivity (Proposition 7.2.2 and Theorem 7.3.7), and the capacity definition (Definition 7.4.2). Our two model calculations validate the scaling and boundary scope but do **not** certify those general upstream results.
- Lines **66–78** use the lemma and \(L^1\) convergence to control the negative tail; the passage from ordinary to outer capacity invokes quasi-continuity and Lemma 7.5.4. This reliance remains **external to the precise proof scope of this report** (an unverified *internal dependency*, not a missing mathematical proof or an imported theorem).
- Theorems 7.9.2, 7.5.8 and the existence/uniqueness argument in lines **80–107** were read for hypotheses but **not completely checked**. In particular, no complete certification of Theorem 7.10.2, local capacity convergence or Bedford–Taylor continuity is claimed.
- Historical attributions and canonical source tags remain intact; no duplicate theorem, false theorem, or source/body repair has been identified.
- **Proposed optional enhancement:** add a short comment after Lemma 7.10.1 that its \(t^n\) is scale-forced, and that applying it to densities bounded by \(M\eta^n\) yields (BT-lower-tail). This is a suggested editorial/expository addition, not a production patch.
- **Affected dependents:** the negative-tail capacity step in Theorem 7.10.2 and any application replacing bounded density convergence by \(L^1\) convergence plus capacity estimates. The models validate only the exponent and localization; they do not repair or certify the general dependency chain.

**Coverage classification:** first independently recorded quantitative homogeneity/localization model for §7.10.1 and fresh direct inspection of the negative-tail proof at §7.10.2. Previously recorded §7.9 models, root-density concavity, and historic §7.10 findings remain **separate**, not repeated or reclassified. The actual current ToC remains 25 chapters / 747 numbered sections; zero complete mathematical-section certifications. Demailly approximation/regularization and its dedicated Bergman, weighted \(L^2\), Ohsawa–Takegoshi, multiscale atlas and positivity-loss programme remain **deferred-by-user**, not resolved. No build, tests, CI, website publication or main/source/registry/tag changes were performed.
