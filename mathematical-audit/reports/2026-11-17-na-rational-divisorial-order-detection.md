# Rational divisorial detection of the non-Archimedean test-curve order

**Date:** 2026-11-17. **Finding ID:** POME-NA-RATIONAL-DIVISORIAL-ORDER-DETECTION-001. **Severity:** low. **Status:** verified conditional deduction (not a false printed theorem, not a complete proof-chain certification).

## Exact integrated source and scope

Reviewed current **main** commit `b6933b772f41b45918f7e25ed1afbbb1fd892272`:
- `docs/sections/non-archimedean-pluripotential-theory/index.html`, blob `8448d710690ebe1cc28040f9611d05c9d008a961`: setup §§22.1.101–104, physical lines 1517–1540; Lemma **22.1.105** (`sgpt:E9E2946C`, permanent `CB69CB164255`), lines **1544–1579**; Eq. **22.1.106** (`sgpt:8757EB56`, permanent `99B9B27CF451`), lines **1553–1557**.
- `docs/tag/8C4DFDD0ADE0/index.html`, Corollary **21.11.26** (permanent `8C4DFDD0ADE0`), lines **6–39**: recovery of the convex conjugate and a supremum over positive rational arguments.
- `docs/tag/EE590FE41862/index.html`, Proposition **16.8.9** (permanent `EE590FE41862`), especially lines **6–29**, divisorial Lelong-number criterion for the multiplier-ideal preorder.
- `docs/tag/2E8F613E7CBE/index.html`, Proposition **16.8.17** (permanent `2E8F613E7CBE`), lines **6–27**, comparison of the ideal-model envelopes.

These last three propositions/corollaries are *used as stated*, not independently certified in their full upstream generality. This unit does not invoke Demailly approximation, Bergman, L2, Ohsawa–Takegoshi, atlas or positivity-loss proof completion.

## Strengthening extracted from the integrated proof

Let `X` be a connected projective manifold and `L` a pseudoeffective rational line bundle with smooth curvature representative \(\theta\), as in §22.1.101. For \(\Gamma,\Gamma'\in\mathrm{PSH}^{\mathrm{NA}}(X,\theta)\), put
\[
\mathscr D_{\mathbb Q}:=\{qv:\ v\in X^{\mathrm{div}},\ q\in\mathbb Q_{>0}\}\subset X^{\mathrm{An}}.
\]
Then
\[
\boxed{\quad
\Gamma\le\Gamma'\ \Longleftrightarrow\
\Gamma^{\mathrm{An}}(w)\le\Gamma'^{\mathrm{An}}(w)
\quad\text{for every } w\in\mathscr D_{\mathbb Q}.
\quad}
\]
The right-hand condition is weaker *as a stated testing requirement* than testing every non-Archimedean point. It is sufficient; this is not an assertion that the functions are continuous on \(X^{\mathrm{An}}\), or that an inequality on an arbitrary dense subset of upper-semicontinuous functions extends to the whole space.

### Proof

The forward implication follows from order preservation in Lemma 22.1.105. Conversely assume the inequalities on \(\mathscr D_{\mathbb Q}\). Fix a divisorial valuation \(v\) and \(t\in\mathbb Q_{>0}\). Then \(t^{-1}v\in\mathscr D_{\mathbb Q}\), and the integrated identity (22.1.106) yields
\[
F_v(t):=\sup_{\tau\in\mathbb R}\big(a_v(\tau)+t\tau\big)
=t\Gamma^{\mathrm{An}}(t^{-1}v)
\le t\Gamma'^{\mathrm{An}}(t^{-1}v)=:F'_v(t),
\]
where \(a_v(\tau)=(\Gamma_\tau^{\theta+\omega})^{\mathrm{An}}(v)\) and similarly for \(\Gamma'\). Here \(\omega\) is one fixed Kähler form, exactly as in the printed proof. The tests hold for **every** positive rational \(t\), not for just one scale.

The test-curve profiles \(a_v,a'_v\) have the closed concave, nonincreasing Legendre structure used in the integrated proof. Its concave inversion, with the rational-argument formula of Corollary 21.11.26, is
\[
a_v(\tau)=\inf_{t\in\mathbb Q_{>0}}\big(F_v(t)-t\tau\big),\qquad
a'_v(\tau)=\inf_{t\in\mathbb Q_{>0}}\big(F'_v(t)-t\tau\big).
\]
The formulas are interpreted with the extended-real conventions of the source (including an identically \(-\infty\) slice); no subtraction of two infinite potentials is used. Therefore \(F_v\le F'_v\) on \(\mathbb Q_{>0}\) gives \(a_v\le a'_v\) for all real \(\tau\).

Since \(v\) was arbitrary divisorial, the slice inequality implies \(\Gamma_\tau^{\theta+\omega}\preceq_{\mathcal I}\Gamma_\tau'^{\theta+\omega}\) by Proposition 16.8.9. Both slices are \(\mathcal I\)-model potentials by the §22.1 construction; Proposition 16.8.17 promotes this to the **pointwise** slice order. It holds for every \(\tau\), hence \(\Gamma\le\Gamma'\) by the definition of the test-curve order. This proves the equivalence subject to the named internal inputs.

### Why a finite set of scales is insufficient for the Legendre step

For a purely **scalar** model (not claimed to be realizable by geometric NA potentials), take any \(c>0\) and the upper-semicontinuous concave left-constant profile
\[
a_c(\tau)=
\begin{cases}
0,&\tau\le0,\\
-c\tau,&0\le\tau\le1,\\
-\infty,&\tau>1.
\end{cases}
\]
Its support transform is exactly \(F_c(t)=\max(0,t-c)\) for \(t>0\). Given any **finite** sample \(T\subset(0,\infty)\), choose distinct \(c,d>\max T\). Then \(F_c=F_d=0\) on \(T\), while \(a_c\ne a_d\). Thus a finite-scale replacement for the *rational Legendre detection step* would not follow even at the scalar convex-analytic level. This calculation does not assert a counterexample to the printed NA theorem.

## Classification, dependencies and proposed editorial addition

- **Classification:** verified conditional deduction, low severity. Lemma 22.1.105 and its printed proof are consistent with this sharpening; no false theorem or gap is claimed.
- **Complete new check:** extraction of the genuinely sufficient testing family, order of infima, and explicit finite-scale obstruction for scalar profiles.
- **Conditional dependencies:** §22.1.83/106 analytification and valuation homogeneity, §21.11.26 Legendre inversion, §16.8.9 valuative \(\mathcal I\)-preorder and §16.8.17 ideal-model envelope comparison. These are not re-proved in full; no global bijection in §22.1.111 or operations correspondence in §22.1.112 is certified.
- **Proposed source-only patch, not applied:** add a corollary after Lemma 22.1.105 stating the boxed rationally rescaled divisorial testing criterion, with the exact qualifications above. The downstream injection step in Theorem 22.1.111 could cite it. No production text, permanent tags, registry or source repo was edited.
- **Coverage:** first visits to numbered sections **0**, whole sections certified **0**; direct selected proof paragraphs §22.1.105 and its convex/ideal-model dependencies only. Current ToC 25 chapters / 747 numbered sections.
