# 2026-10-28 — directional torus formulas, jet thresholds, and two malformed equation aliases

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Audit branch at start:** d8e5ca08d6218c1ece22e7c89236661ee672ab92.  
**Scope:** first targeted, nonexcluded, integrated-reading-edition inspection of selected arguments in sections 6.37 and 6.39. Dependency-only comparisons with sections 6.34 and 6.36 do not constitute new proof certification. This is not a review of entire sections or chapters. Existing canonical variants and historical attribution are retained.

**Exclusion:** All Demailly approximation/regularization and dedicated Bergman, weighted L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion work stays **deferred-by-user**. No excluded proof, its dedicated prerequisites, or smoothing argument was reopened.

## POME-DIRECTIONAL-EQ-ALIAS-NESTED-001

**Severity:** medium. **Status:** confirmed error — reading-edition integration only; neither Theorem 6.37.5 nor its mathematics is declared false.

**Exact integrated anchors:** main file
docs/sections/lelong-densities-generalized-masses-and-multiplicity--directional-boundary-measures-and-growth/index.html,
main blob f4db1608fec003cc9e6055d2bb9e1db447254477.
Theorem 6.37.5 comes from source demailly-complex-geometry:28BEBFE4, permanent E3EFBBDA7787, physical line 88. Its complete, two-row formulas (6.37.6) and (6.37.7) appear properly in the theorem at physical lines 89–92 and 94–97. Proof concludes at lines 124–127. At physical line 128, a *second* independent reading chunk for permanent F71249678342 (source demailly-complex-geometry:5FDE82E5) emits only the final equality of (6.37.6); a further chunk for permanent B7F196B96D6D (source demailly-complex-geometry:F9B84E02) emits only the final equality of (6.37.7). Both fragments contain the literal invalid nesting of an align environment inside an aligned environment:

    \[\begin{aligned}\begin{align} & = ... \tag{6.37.6} \end{align}\end{aligned}\]

The other fragment has the analogous tag (6.37.7). These are orphaned right-hand-side expressions, not independent mathematical formulas. The problem reproduces on both standalone equation tag pages: docs/tag/F71249678342/index.html (main blob 8bfeb65c37163428d74d764690ac09b8c43d76da; inline physical line 5) and docs/tag/B7F196B96D6D/index.html (main blob ea0ec1339dcb3e577aae9cf87c27b31ec148e7f1; inline physical line 5). Their exact nested environment strings were read, not inferred from titles.

**Diagnosis/disposition:** The canonical theorem display already includes each complete equation. The independently exported equation-tag aliases are not mathematically independent items and must not be reinserted into the section as truncated duplicates. A future separately reviewable integration patch should render each canonical equation exactly once, make each permanent equation tag resolve to a meaningful complete canonical equation (or to an explicitly identified canonical equation within the theorem), preserve both permanent tags and both source labels, and avoid wrapping raw align math inside aligned. Verify both tag pages and the section in a browser if implementing. Do not delete provenance or equate this defect with a false theorem. This is the same *class* of exporter defect as the already recorded POME-JENSEN-EQ-ALIAS-NESTED-001 in section 6.36, but it has two **different verified tags and two different main HTML loci**. We make no separate unsupported claim about the exact exporter root cause.

**Affected dependents:** readers of Theorem 6.37.5, citations to (6.37.6) and (6.37.7), permanent-tag navigation, equation rendering/canonicalization. Production source, registry, and tag IDs remain untouched.

## POME-DIRECTIONAL-JET-THRESHOLD-SHARP-001

**Severity:** low. **Status:** verified conditional deduction — necessity of a condition for the *uniform* version; printed Corollary 6.39.13 is correct.

**Exact integrated anchor:** docs/sections/lelong-densities-generalized-masses-and-multiplicity--parameter-weights-and-analytic-lelong-level-sets/index.html, main blob d3319c955c4e1fdcf3e3f909cc489b1ed4390a98; Corollary 6.39.13, source demailly-complex-geometry:ED85E555, permanent 470C5143C0D1, physical lines 222–224, with its proof at lines 226–240.

**Claim proved:** For any positive integer k the printed hypothesis
\[(k+1)\min_j\lambda_j\geq\max_j\lambda_j\]
cannot simply be omitted from a uniform k-jet invariance statement, even for smooth invertible local coordinate maps and a positive closed integration current on a smooth curve.

**Proof/countermodel:** On a small bidisc in the plane let
\[u=(z_1,z_2),\qquad u'=(z_1+z_2^{k+1},z_2),\qquad
 \lambda_1=1,\quad \lambda_2=k+2.\]
Both u and u' are local biholomorphic coordinates at zero; their Jacobian at zero is the identity, and their k-jets are equal. Let C be the coordinate line z_1=0, and T=[C], a closed positive current of bidimension (1,1). Define the exact weights
\[\phi=\log\max\{|u_1|^{2\lambda_1},|u_2|^{2\lambda_2}\},\quad
  \phi'=\log\max\{|u'_1|^{2\lambda_1},|u'_2|^{2\lambda_2}\}.\]
Both are continuous extended-valued psh functions with their sole pole at zero. Restricting to C, write t=z_2. For 0<|t|<1,
\[\phi|_C=(k+2)\log|t|^2,\qquad
  \phi'|_C=(k+1)\log|t|^2.\]
Under the actual Pome normalization dd^c log|t|^2=delta_0, the classical one-dimensional pole mass, equivalently the support-relative generalized Lelong number using the finite truncation definition of section 6.34, is exactly its nonnegative logarithmic coefficient. Thus
\[\nu_T(\phi)=k+2,\qquad \nu_T(\phi')=k+1.\]
Their values differ despite identical k-jets. The failure precisely occurs since (k+1)lambda_1=k+1<lambda_2=k+2. In particular k=1, lambda=(1,3) gives the values 3 and 2. This does **not** contradict the printed result, which explicitly imposes the inequality. The borderline equality case remains included by the existing proof; no false theorem has been found.

**Dependents and suggested action:** retain the hypothesis when canonicalizing coordinate jet bundles or applying the analytic upper-level-set conclusion; an optional short sharpness example can be proposed separately. The one-dimensional Poincare–Lelong normalization and the generalized-number definition are used, but their general proofs and the complete parameter-analyticity theorem were **not** independently re-certified. No approximation or excluded programme is invoked.

## POME-DIRECTIONAL-TORUS-BINOMIAL-GAP-001

**Severity:** low. **Status:** verified conditional deduction — exact model sharpening the correct directional angular/supremum comparison, not a false theorem.

**Exact integrated anchors:** same section 6.37 main file/blob as above. Proposition 6.37.1, source demailly-complex-geometry:8EFE1AE46FF7, permanent 8EFE1AE46FF7 (the boundary torus law); Theorem 6.37.5, source demailly-complex-geometry:28BEBFE4, permanent E3EFBBDA7787, physical lines 88–124, particularly complete equations 6.37.6/7 at lines 89–97 and the negative-r inequalities at lines 112–124. The proposition is inspected only for its relevant torus-probability normalization.

**Claim/proof:** In dimension two choose positive weights lambda_1,lambda_2, positive integers m,b, and the psh model
\[V(z_1,z_2)=\log|z_1^m+z_2^b|^2.\]
For r<0 let the weighted distinguished torus have radii
\[R_j(r)=\exp(r/(2\lambda_j)),\quad A=R_1(r)^m,\quad B=R_2(r)^b.\]
Both A and B are positive. Averaging first in the first circle variable gives the elementary exact Jensen identity
\[\frac{1}{2\pi}\int_0^{2\pi}
  \log|Ae^{im\theta}+Be^{ib\psi}|^2\,d\theta
  =2\log\max(A,B).\]
For m≥1, e^{im\theta} has uniform angular distribution. The identity also holds at A=B because the logarithmic singularities at the finitely many cancellation angles are integrable. The result is independent of the second angle. Consequently the product Haar angular mean is
\[m_V(r)=2\log\max(A,B)
       =r\min\{m/\lambda_1,b/\lambda_2\}.\]
On the closed weighted polydisc, the triangle inequality gives |z_1^m+z_2^b|≤A+B, and an aligned-phase point on the distinguished torus attains equality. Thus its **actual supremum** is
\[H_V(r)=2\log(A+B).\]
Hence the finite-radius defect is explicitly
\[H_V(r)-m_V(r)
=2\log\!\left(1+\frac{\min(A,B)}{\max(A,B)}\right)
\in(0,2\log2].\]
The value 2 log 2 is attained for *all* negative r if m/lambda_1=b/lambda_2, proving the constant is optimal in this binomial family. If the ratios are unequal, the defect tends to zero exponentially as r tends to negative infinity. Both mean and supremum divided by r have the common slope min(m/lambda_1,b/lambda_2), and the directional number of Theorem 6.37.5 therefore equals
\[\nu(dd^cV,0,\lambda)
=\lambda_1\lambda_2\min\{m/\lambda_1,b/\lambda_2\}
=\min\{m\lambda_2,b\lambda_1\}.\]
The last identification uses the printed theorem as a **conditional input**: the exact angular integration and maximum computations themselves are independent. The model does not assert a universal bounded gap for arbitrary psh functions.

**Dependents/disposition:** optional reproducible short model for section 6.37 and the directional-jet context in section 6.39. Preserve the given source theorem, normalization, weights, labels, and permanent tags.

## Coverage and status accounting

- **New direct selected-passage coverage:** section 6.37 (Theorem 6.37.5 statement, displayed formulas, key comparison proof and both orphaned alias chunks) and section 6.39 (Corollary 6.39.13 statement, its coordinate jet domination proof, and an exact countermodel to the invalid broader statement). These rows were inventory-only before this checkpoint. Proposition 6.37.1 was used for the torus normalization; not all results in either section have been verified.
- **Context only, not newly certified:** section 6.34 generalized weights and classical polar mass, section 6.36 weighted Jensen setup; do not double-count earlier review.
- **Project-wide matrix:** 25 chapters, 747 distinct numbered section IDs in the existing main-aligned coverage inventory. This checkpoint certifies **zero whole sections**, zero whole chapters, and no full proof dependency chain.
- **Statuses:** one medium confirmed *integration* error and two low verified *conditional deductions*. No mathematical theorem shown false; earlier gaps, candidates, true errors and external inputs retain their previous exact statuses. All excluded work remains **deferred-by-user**, neither resolved nor certified.
- **Changes and verification:** this file is a report proposal in the audit branch only. No production main, source manuscripts, reading HTML, proof registry, canonicalization, permanent tags, website, CI or automatic publication are modified. No project tests/build/formal verification were run.
