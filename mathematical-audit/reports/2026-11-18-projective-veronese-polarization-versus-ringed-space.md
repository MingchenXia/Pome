# Full direct audit of §9.59 and the Veronese polarization boundary

**Date:** 2026-11-18  
**Finding:** POME-PROJ-VERONESE-POLARIZATION-BOUNDARY-001  
**Classification:** low / **verified conditional deduction** (not a false printed theorem and not a production canonicalization defect).  
**Coverage:** **full direct reading/proof-step review of the two numbered results in §9.59**, not certification of all upstream §9.58 inputs or the project. Previously selected §9.59; **+0 first-visited numbered sections, +1 entire-section direct review**.  
**Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`  
**Reading-edition file:** \`docs/sections/finite-type-algebraic-models-and-analytic-structure-sheaves--products-closed-subspaces-and-projective-charts/index.html\`  
**Exact main blob:** \`4373897c66d3fae21cab98bec91fff3457d23ade\`  
**Section tag:** \`232528C54E90\` (line 5); source provenance \`demailly-complex-geometry:D76E1CDA\`.  
**Proposition 9.59.1:** source \`demailly-complex-geometry:20E582B2\`, permanent \`476B5A661E43\`, statement line 11, proof lines 14–22, topology/diagonal discussion lines 23–25.  
**Theorem 9.59.2:** source \`demailly-complex-geometry:979A59BB\`, permanent \`4D90B8C4C837\`, statement line 28, proof lines 31–49, affine localization identity lines 34–40, degree-one cover line 42, polynomial quotient/separation line 44, base-locus and Veronese step line 46.  
**Cross-section dependent:** §21.9 Theorem 21.9.5, source \`foundations-of-pluripotential-theory:BD98CC5B\`, permanent \`69D3D97E7701\`, in \`docs/sections/convex-analysis-and-toric-potentials--fans-divisors-and-character-sections/index.html\`, main blob \`7ad2e6dbdd0ce59e1bf08cd9cb3c046e8c87ff6c\`, lines 138–149 (character section Hilbert count only; theorem not recertified).

## 1. Finding: the *ringed space*, not the polarization, is Veronese-invariant

The last assertion of Theorem 9.59.2 is correct exactly as written: a positive Veronese subalgebra gives **the same projective ringed space**. It must not be silently upgraded to preservation of the tautological polarization.

Let \(k\) be algebraically closed, let \(B=k[x_0,x_1]\) with \(\deg x_i=1\), and let \(d\ge2\). Put \(C=B^{(d)}=\bigoplus_{m\ge0}B_{dm}\), with the **regraded** convention \(C_m=B_{dm}\). The canonical chart isomorphisms
\[
(B_{x_i})_0 \xrightarrow{\ \cong\ } (C_{x_i^d})_0
\]
are just the identity on \(k[x_{1-i}/x_i]\): for instance \(x_0^{d-1}x_1/x_0^d=x_1/x_0\). They glue with the same coordinate transition \(z\mapsto1/z\). Thus
\[
\operatorname{Proj}_{\rm cl} C\cong\operatorname{Proj}_{\rm cl} B\cong\mathbb P^1_k
\]
even as locally ringed spaces.

However, \(\mathcal O_{\operatorname{Proj} C}(1)\) is locally trivialized using the **degree-one element of \(C\)**, namely \(x_i^d\). On \(U_{x_0}\cap U_{x_1}\), the resulting transition ratio is \((x_1/x_0)^d\), not \(x_1/x_0\). Hence the canonical ringed-space isomorphism \(F\) satisfies
\[
\boxed{F^*\mathcal O_{\operatorname{Proj} C}(1)
 \simeq\mathcal O_{\mathbb P^1}(d),\qquad
 \mathcal O_{\operatorname{Proj} B}(1)=\mathcal O_{\mathbb P^1}(1).}
\]
Their degrees are \(d\) and \(1\) and their spaces of global sections have dimensions \(d+1\) and \(2\), respectively. They are not isomorphic as polarized pairs. The same calculation on \(\mathbb P^n\) gives \(\binom{n+d}{n}\) versus \(n+1\) degree-one sections. These are exact Hilbert-function checks, not a computational test.

**Status:** verified conditional deduction relative to the elementary \(\operatorname{Proj}\) and invertible-sheaf chart conventions; no error in the printed theorem.  
**Severity:** low for the theorem; an important **canonicalization boundary** if a future registry were to equate polarized objects merely because their underlying projective ringed spaces are isomorphic.  
**Proposed correction:** no source/body patch required. If citing the Veronese equivalence in an argument about section spaces, numerical divisor classes, or line bundles, append the explicit qualification \(\mathcal O_{B^{(d)}}(1)\leftrightarrow\mathcal O_B(d)\), **not** \(\mathcal O_B(1)\). Preserve both presentation gradings, degree conventions, source tags, and the actual ringed-space isomorphism.  
**Affected downstream computations:** polarized Hilbert counts, §21.9.5's toric character-section formula, degrees of projective embeddings and intersection numbers; no currently demonstrated incorrect downstream theorem.

This observation differs from the already recorded \`POME-PROJ-IRRELEVANT-TORSION-KERNEL-001\` (which concerns invisible irrelevant torsion and the underlying ringed space) and from the two nonreduced nilradical-gluing tests. Nothing from those findings is counted again here.

## 2. Full direct proof audit of Proposition 9.59.1

Assume the **algebraically closed base-field/finite-type category and closed-point localization-sheaf conventions of §9.58**. A closed point of \(\operatorname{Spm}(A\otimes_k B)\) is a pair of \(k\)-algebra homomorphisms \(A,B\to k\), hence a pair of closed points. The universal property for affine test objects follows from the tensor product; for a glued finite-affine-atlas test object, maps into an affine space are controlled by compatible algebra maps on each chart. Compatibility is equivalent to an algebra homomorphism into global functions, so the product universal property extends. Open overlaps correspond to localizing relevant factors; associativity and the cocycle compatibility are exact. This does **not** equip the product with the topological product topology.

The coherence argument uses finite generation of the base algebras, hence their Noetherian property. Kernel and cokernel finite-generation over localized Noetherian rings and exactness of localization justify coherent ideal sheaves. For ideals \(I,J\), the local scheme-theoretic intersection is \(V(I+J)\), the least closed union is \(V(I\cap J)\), and the thicker \(V(IJ)\) has the same *support* because \(\sqrt{IJ}=\sqrt{I\cap J}\). The test \(I=J=(T)\) gives union \(k[T]/(T)\), not the double point \(k[T]/(T^2)\). Both are retained as distinct subschemes.

The post-proof diagonal example is correct: the diagonal in the product of two cofinite topologies is dense, but \(V(x-y)\) is closed in the algebraic plane. The separated-denominator argument for \((1-x-y)^{-1}\) shows precisely why the algebraic product's stalk differs from a tensor of two point-local rings. The doubled-origin counterexample is also correctly a nonseparated gluing.

**Direct assessment:** all asserted product, ideal, and separation steps check under the printed finite-type/closed-point conventions. No false theorem, circularity or missing mathematical step was detected **within these lines**. The relied-upon §9.58 full faithfulness and general gluing/sheaf convention remain upstream conditional inputs, not newly certified here.

## 3. Full direct proof audit of Theorem 9.59.2

Let \(s\) be homogeneous of degree \(m>0\). Its degree-zero localization \(B_{(s)}\) is generated over \(B_0\) by the finite-dimensional space \(B_m/s\): every degree \(rm\) numerator is a sum of products of \(r\) degree-\(m\) monomials in \(B_1\), including coefficients from \(B_0\) absorbed into the first factor. This remains valid with nilpotents or zero divisors; localization at a nilpotent \(s\) gives the zero ring/empty chart.

For \(t\) homogeneous of degree \(n>0\), \(u=t^m/s^n\) has degree zero, and the canonical map
\[
B_{(s)}[u^{-1}]\longrightarrow B_{(st)}
\]
is an isomorphism. Indeed both express the degree-zero fractions on the common \(s\ne0,t\ne0\) locus: multiplying by sufficiently high powers of \(s\) and \(t\) makes denominator exponents nonnegative and equal where needed. This gives triple-overlap compatibility and handles unequal homogeneous degrees. Since \(s/s=1\) can be expanded using degree-\(m\) monomials in a basis of \(B_1\), some such monomial is nonzero at any point of \(U_s\); thus the finitely many degree-one charts cover all \(U_s\).

For the polynomial graded ring, the chart algebras are \(k[T_j/T_i:j\ne i]\), with the usual projective coordinate changes. For a general \(B\), \(B^+=k1\oplus\bigoplus_{m>0}B_m\) is generated over \(k\) by \(B_1\), with unchanged positive-degree charts: \(b_0=(b_0s)/s\). A polynomial graded ring on \(B_1\) surjects onto \(B^+\), giving a compatible homogeneous ideal and closed projective embedding even when \(B\) is nonreduced. Separatedness follows from the closed diagonal in projective space, restricted to the closed subspace.

For a graded homomorphism \(B\to C\), the natural projective morphism is only defined where the images of \(B_1\) have no common zero; for a graded surjection this open set is all of \(\operatorname{Proj}_{\rm cl}C\). The printed projection \(\mathbb P^2\dashrightarrow\mathbb P^1\) from \([0:0:1]\) correctly prevents extending a general graded homomorphism across its base point. Finally, \(B_{(s)}=B_{(s^d)}\) on all positive-degree charts, which establishes the Veronese ringed-space identification, **subject to the polarization distinction of §1**.

**Direct assessment:** both the statement and the complete proof of Theorem 9.59.2 hold under its graded finite-type assumptions. The projective-scheme and tautological-invertible-sheaf language used in §1 is a separately explicit standard chart construction. No complete verification of §9.58 or the entire project follows. This is one additional **entire numbered section directly audited**, not a proof of a new original theorem.

## 4. Coverage, dependencies and verification boundary

- Entire §9.59 integrated statement/proof text: **directly inspected and mathematically checked**, including both numbered results, their edge cases \(B_1=0\), nilpotents, arbitrary positive degrees, arbitrary graded maps, and the intervening examples. The source line anchors above are physical lines of the frozen main HTML blob, not reconstructed source-book numbers.
- §9.58.2–3: **upstream conditional dependency** (its finite-type algebra/closed-point fully faithful construction had a separate earlier audit); not counted as new coverage.
- §21.9.5: **cross-checked only** for the character-section/Hilbert-count dependent; no complete proof review or coverage credit.
- Findings: **1 new low-severity verified conditional deduction**, **0 confirmed erroneous printed theorems**, **0 new production defects**, **0 resolved older findings**. No mathematical duplicate/canonical merge was performed.
- Existing dedicated Demailly regularization/approximation, Bergman, L², Ohsawa–Takegoshi, multiscale and positivity-loss findings are **deferred-by-user**, neither settled nor reopened.
- **No code tests, builds, formal proof, CI, or browser checks were run.** No direct edits to main/source bodies/registry/permanent tags/website; this report is a review-branch-only note.
