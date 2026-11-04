# Mathematical audit — 2026-11-04 — exceptional modifications and sharp atlas distortion

**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
**Audit target:** \`review/mathematical-audit\`. Scope excludes Demailly approximation/regularization and the user's deferred Bergman, weighted-L2, OT, multiscale and positivity-loss completion work. This report inspects new, nonexcluded proof/model components of two integrated reading sections, not their full dependency chains.

## 1. POME-NPP-BLOWUP-EXCEPTIONAL-COHOMOLOGY-001

**Status:** verified conditional deduction; **severity:** low. No error in the printed proposition.

**Exact integrated source:** \`docs/sections/non-pluripolar-products--fiber-integration-and-modifications/index.html\`, main blob \`9954a43d90d5cae8ef744968636d7a5912348fce\`, physical lines **35–55** (especially statement 36–46 and proof 50–54). Proposition **13.6.3**, source \`foundations-of-pluripotential-theory:3F4A3A88\`, permanent tag \`0811FFDF15B7\`. The two asserted identities concern the pullback and pushforward of non-pluripolar mixed products under a modification of compact Kähler manifolds.

**Exact exceptional-current model.** Let \(\pi:Y=\operatorname{Bl}_{p}\mathbf P^2\to\mathbf P^2\) be the blowup of a point, let \(E\subset Y\) be the exceptional curve, and normalize the Fubini–Study form \(\omega\) by \(\int_{\mathbf P^2}\omega^2=1\). Put \(\beta=\pi^*\omega\), a smooth semipositive form, and take any \(a,b\geq0\). The currents
\[
 R_a=\beta+a[E],\qquad R_b=\beta+b[E]
\]
are closed and positive. Their local potentials have the prescribed logarithmic poles along \(E\) when the corresponding coefficient is positive. On \(Y\setminus E\) both currents are the smooth form \(\beta\). The defining truncation procedure for non-pluripolar products (the locality and no-pluripolar-mass properties from §§13.2–13.5) therefore gives
\[
 \langle R_a\rangle=\beta,\qquad
 \langle R_a\wedge R_b\rangle=\beta^2 .
\]
Indeed these identities hold off \(E\), all non-pluripolar products give \(E\) zero mass, and the smooth forms on the right give \(E\) zero mass. This reasoning includes \(a=0\) and/or \(b=0\). Consequently
\[
 \pi_*\langle R_a\wedge R_b\rangle=\omega^2
 =\langle\pi_*R_a\wedge\pi_*R_b\rangle,\qquad
 \int_Y\langle R_a\wedge R_b\rangle=1.
\]
Here \(\pi_*[E]=0\) as a \((1,1)\)-current, because \(E\) maps to a point; and \(\pi_*\beta=\omega\). This is a fully explicit test of the *second* pushforward identity, previously only viewed at statement level in the audit.

In contrast, the ordinary cohomological intersection is
\[
 [R_a]\cdot[R_b]
 =(\pi^*H+aE)\cdot(\pi^*H+bE)=1-ab,
\]
because \((\pi^*H)^2=1,\ \pi^*H\cdot E=0,\ E^2=-1\), the latter following from \(E\simeq\mathbf P^1\) and \(N_{E/Y}\simeq\mathcal O_{\mathbf P^1}(-1)\). For \(ab>1\) this pairing is even negative, despite both currents being positive and their non-pluripolar mixed mass being \(1\). Thus the current-level pushforward statement must *not* be replaced by an identity of ordinary cohomological intersection numbers; no mathematical contradiction arises.

**Boundary of verification.** The general printed proof correctly reduces to the biholomorphic locus and uses the no-pluripolar-mass property to remove exceptional subsets. This explicit model independently verifies the exceptional contribution and both pushforward factors, but does not certify the general theorem's complete analytic prerequisites or its downstream relative-energy uses. **Suggested addition:** a compact warning after Proposition 13.6.3 distinguishing non-pluripolar mass from ordinary cohomological intersection when exceptional components are present. No body or tag edit is proposed here.

## 2. POME-NPP-EXTCAP-ATLAS-SHARP-TRANSLATION-001

**Status:** verified conditional deduction; **severity:** low. Printed Definition 13.7.2 and Lemmas 13.7.1/13.7.3 are not refuted.

**Exact integrated source:** \`docs/sections/non-pluripolar-products--capacity-convergence-and-loss-of-mass/index.html\`, main blob \`d66813856cb813722806ab912afdfd4815d2da97\`. Lemma **13.7.1**, source \`foundations-of-pluripotential-theory:B581D99A88\`? **Correction:** the exact source label is \`foundations-of-pluripotential-theory:B581D99A\` (article ID), permanent \`AB4F8DB9BF3E\`, physical lines **10–34**; Definition **13.7.2**, source \`foundations-of-pluripotential-theory:9AC5981A\`, permanent \`019A8D37A03F\`, lines **36–39**; Lemma **13.7.3**, source \`foundations-of-pluripotential-theory:4720F1AB\`, permanent \`274B700496A8\`, lines **41–69**. In particular, its proof at lines **53–61** bounds the arctangent-distance change after adding the same local smooth potential by \(2(1+h^2)\).

**Sharp pointwise distortion.** For \(s,t\in[-\infty,\infty)\), let \(d_*(s,t)=|\arctan s-\arctan t|\). For every real \(h\),
\[
 d_*(s+h,t+h)\leq L(h)\,d_*(s,t),\qquad
 L(h)=\left(\frac{\sqrt{h^2+4}+|h|}{2}\right)^2
 =\exp(2\operatorname{arsinh}(|h|/2)).
\]
The convention \(-\infty+h=-\infty\) is understood. This is the **smallest possible uniform constant**. Indeed set \(x=\arctan s\), so the translation map in arctangent coordinates has derivative
\[
 \frac{d}{dx}\arctan(\tan x+h)
 =\frac{1+\tan^2x}{1+(\tan x+h)^2}
 =R_h(\tan x).
\]
For \(h\ne0\), stationary points of \(R_h(y)\) satisfy \(y^2+hy-1=0\). Substitution of the two roots gives the reciprocal extrema \(L(h)\) and \(L(h)^{-1}\); limits as \(|y|\to\infty\) equal \(1\). The mean-value theorem (or integration of the derivative on any finite subinterval) yields the inequality. Taking \(t\to s\) at a maximizer proves sharpness; continuity extends it to \(s=-\infty\) or \(t=-\infty\). For \(h=0\), \(L(0)=1\).

If \(h(x)\) is a bounded real function with \(|h(x)|\le H\) on a compact chart overlap, this gives the pointwise sharp universal bound \(L(H)\), because \(L(|h|)\) is increasing. Together with the chart-capacity comparison of Lemma 13.7.1, this proves coordinate-potential/finite-atlas independence of extended-capacity convergence **for arbitrary directed nets**, not only sequences: for each compact overlap, the error set at threshold \(\delta\) after adding \(h\) is contained in the old error set at threshold \(\delta/L(H)\); finitely many terms with capacity tending to zero are again convergent along the same directed set. No sequential subnet or cofinal sequence is selected, and no interchange of limiting operations is needed.

**Boundary of verification.** This checks precisely the local-potential distortion and the finite-cover/net passage in the integrated proof. It does not certify the full bounded-product weighted-capacity theorem 7.5.8, general lower-semicontinuity Theorem 13.7.5, or all non-pluripolar convergence applications. **Suggested addition:** optionally replace the coarse coefficient \(2(1+h^2)\) with \(L(h)\) and state explicitly that finite-atlas independence holds for nets. Retain the original definition and tags.

## Coverage and classification

This run freshly read production \`main\`, \`AGENTS.md\`, \`documentation/proof-expansions.md\`, the audit-branch \`mathematical-audit/LATEST.md\` and \`README.md\`, and the current chapter-13 table of contents. Newly performed mathematics comprises the explicit blowup computation for Proposition 13.6.3 and the optimal arctangent translation/net-gluing proof for Definition 13.7.2 and Lemma 13.7.3. The previous §13.6.1 fiber-slicing and §13.7.5 mass-loss findings remain separate and unchanged. Previously examined §11.2 torus-curl models were **not** counted as new work. No fully mathematically certified numbered section is claimed (actual inventory: 25 chapters, 747 sections). The user's Demailly regularization and dedicated Bergman/L2/OT/multiscale/positivity-loss audit programme stays **deferred-by-user**, neither solved nor reopened.

Only audit Markdown is intended for GitHub branch \`review/mathematical-audit\`; no main, integrated reading body, source, registry, permanent tags, CI, build, tests or publication are changed.
