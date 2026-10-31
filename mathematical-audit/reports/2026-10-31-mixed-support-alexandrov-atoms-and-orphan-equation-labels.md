# Mixed support-function Alexandrov atoms and two source-number leakage defects

**Date:** 2026-10-31. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Write boundary:** audit notes and a small exact check only, on review/mathematical-audit; no production, source, registry, permanent-tag or website edits.

## POME-TOR-MIXED-SUPPORT-ATOMS-001

**Severity and status:** low / **verified conditional deduction**. Neither a false theorem nor a certified proof of the upstream general mixed Alexandrov construction. The following is a direct consequence of its presently integrated multilinearity/diagonal assertions.

**Source / anchors.** In production docs/sections/convex-functions-and-convex-bodies/index.html, blob 2a123a863642a5a75caa173f0f73aff439a02ea4: Definition 21.11.50, source sgpt:AA859A41, permanent FF5885207F9E, physical lines 624–630; Equation 21.11.51, source sgpt:0F8A32F1, permanent 54CA724C5825, lines 626–629; Theorem 21.11.58, source sgpt:AE125FCA, permanent 59E2455286B4, physical lines 740–769, and its three permanent clause tags CFA77F02E2A6, 72A14F74D8A4, 0430553123BF. Its integrated proof identifies prior internal mixed-measure construction 21.5.4 (tag 5D8A7A7D734E); that construction is taken as an **unverified upstream premise**, not re-proved or reclassified here. Historical mixed-measure attributions CLM22, TW02 and PR04 remain intact. This finding is distinct from the already logged §21.5 versus §21.11 semantic canonicalization issue.

**Statement.** Fix a lattice N of rank n >= 1 and its dual M. Let K_1,...,K_n be arbitrary nonempty compact convex subsets of M_R, not necessarily full-dimensional. Write
\[
h_K(x)=\sup_{p\in K}\langle p,x\rangle,\qquad x\in N_{\mathbb R}.
\]
For the real Monge–Ampère convention used in 21.11.51 (Alexandrov mass multiplied by n!), the mixed measure is **exactly**
\[
\boxed{\operatorname{MA}_{\mathbb R}(h_{K_1},\ldots,h_{K_n})
   = n!\,V(K_1,\ldots,K_n)\,\delta_0.}
\]
Here V denotes lattice-normalized mixed Euclidean volume with V(K,...,K)=vol(K). Equivalently, and without quoting any separate mixed-volume existence theorem, its total Dirac mass is the coefficient of t_1...t_n in
\[
\operatorname{vol}(t_1K_1+\cdots+t_nK_n).
\]
The polynomial nature of that volume, including degenerate K_j, follows in this argument from the assumed integrated mixed Alexandrov multilinearity.

**Complete local deduction, including possible lower-dimensional K.** Support functions satisfy h_{A+B}=h_A+h_B, h_{tK}=t h_K for t>=0, and their convex subdifferentials obey ∂h_K(0)=K. If K has nonempty interior, every subgradient ∂h_K(x) for x != 0 lies in the proper exposed face {p in K : <p,x>=h_K(x)} within ∂K, whose n-dimensional Lebesgue measure is zero. If K has empty interior, every subgradient lies in the null-volume set K. Consequently ∂h_K(E) has zero n-volume whenever E is Borel and avoids 0, while its image over any E containing 0 contains exactly the full K up to null-volume faces. The Alexandrov convention therefore gives
\[
\operatorname{MA}_{\mathbb R}(h_K)=n!\operatorname{vol}(K)\delta_0
\]
without requiring K to be a convex body in the full-dimensional sense.

For any parameters t_j>=0 the same identity gives
\[
n!\operatorname{vol}(\sum_jt_jK_j)\delta_0
  =\operatorname{MA}_{\mathbb R}(\sum_jt_jh_{K_j}).
\]
Theorem 21.11.58 expands the right side into the homogeneous degree-n polynomial
\[
\sum_{i_1,\ldots,i_n}t_{i_1}\cdots t_{i_n}
     \operatorname{MA}_{\mathbb R}(h_{K_{i_1}},\ldots,h_{K_{i_n}}).
\]
All parameters range over an orthant with nonempty interior; polynomial coefficients are unique. Comparing the coefficient of t_1...t_n, with n! ordered permutations on the right, yields the claimed Dirac identity with the **exact** factor. This argument also proves the volume polynomial representation *from* the stated mixed Alexandrov theorem, so no unproved external Minkowski-polynomial theorem is silently imported. It does **not** independently verify positivity, weak continuity or construction of the upstream mixed measures.

**Sharp diagnostic instances.** In dimension two take orthogonal unit segments K_1=[0,e_1], K_2=[0,e_2]. Each *diagonal* Alexandrov measure vanishes because its individual segment has zero area, but
\[
\operatorname{MA}_{\mathbb R}(h_{K_1},h_{K_2})=\delta_0,
\quad
\operatorname{MA}_{\mathbb R}(h_{K_1}+h_{K_2})=2\delta_0.
\]
Thus no argument may bound a mixed measure by only the two diagonal total masses. For rectangles with side lengths (2,3) and (5,7),
\[
\operatorname{area}(tK_1+sK_2)=6t^2+29ts+35s^2,
\quad
\operatorname{MA}_{\mathbb R}(h_{K_1},h_{K_2})=29\delta_0.
\]
For three boxes with side lengths (1,2,3), (2,4,5), (3,5,7), the t_1t_2t_3 coefficient is 177, and the mixed measure is 177 delta_0. These three coefficients and the unit-square check were **actually reproduced** by checks/check_mixed_support_atoms.py using exact rational arithmetic and permutation enumeration; the check is finite arithmetic, not a formal proof or a Pome build.

**Proposed action / affected dependents.** Optionally add a compact corollary after Theorem 21.11.58 or as an explicit toric/convex model near §21.12.1; retain all source tags, source variants, normalized n! convention and historical citations. The result provides a diagnostic for smooth-versus-singular real Monge–Ampère and toric mass normalizations in §§21.5, 21.11–21.13. No global toric correspondence or complex Monge–Ampère equality is certified here.

## POME-BDIV-ORPHAN-SOURCE-EQ-001

**Severity and status:** low (mathematical impact), medium (reading/canonicalization risk) / **confirmed editorial numbering defect**, not a false definition. Source docs/sections/the-theory-of-b-divisors/index.html, immutable production blob 4a793dfd462badcb351f54a36cb030cde14a399b, physical lines **148–154**; Definition **20.1.14**, source sgpt:CB2E09F0, permanent **165D43352903**. The formula for the b-divisor of a positive current,
\[
\mathbb D(T)_Y=\{\operatorname{Reg}\pi^*T\}\in H^{1,1}(Y,\mathbb R),
\]
is mathematically sensible and not challenged. But its displayed equation is marked numbered-equation and the visible label is the legacy **11.3** at line 151, with neither a generated 20.1.* locator nor an independently displayed permanent tag/anchor. The immediately containing definition is correctly numbered 20.1.14. This conflicts with AGENTS.md and documentation/integration-layout.md lines 17–23 requiring generated current-section structured locators. It is **not** justified to assume that the source number 11.3 should be removed from provenance or that a unique equation tag already exists. Proposed correction: inspect the underlying source equation's identifier / adapter representation and its guarded registry correspondence, then make an independently reviewable structural numbering patch so the label is generated and addressable with its genuine permanent identifier if one exists; otherwise explicitly review whether it should be unnumbered. Do not hand-edit generated docs. Dependencies to recheck after that repair: the definition as used in §20.1.15 and later b-divisor discussion; no broken inbound link has been established in this run.

## POME-TROP-ORPHAN-SOURCE-EQ-001

**Severity and status:** low (mathematical impact), medium (reading/canonicalization risk) / **confirmed editorial numbering defect**, not a false formula. Production docs/sections/toric-pluripotential-theory-on-ample-line-bundles/index.html, blob 56a1a55dfc8185aee0e6d495a6a93d8a2313d76b, §21.12.1 source sgpt:2FF2CFF2, permanent **DD9C13434AA7**, physical lines **96–117**. The neighboring logarithm map equation at lines 98–100 is correctly tagged **21.12.3**, source sgpt:4AC25346, permanent **EA1385DD984D**. The *next* equation defining
\[
\operatorname{Trop}(p):\ m\longmapsto\log|\chi^m(p)|^2
\]
is an untagged numbered-equation at lines **111–114**, with the obsolete source label **5.5** at line 112 and no independent equation ID. Example 21.12.4, source sgpt:14DFB401, permanent **4214559F0471**, is properly numbered at line 117. The tropicalization formula itself is correct: the logarithm of character absolute squares defines an additive element of N_R, with no factor 1/2 under the declared convention. The inconsistent visible number violates the same reader-locator rule. Proposed repair: inspect its original source node and adapter/numbering pipeline, then submit a separate, guarded, reviewable production patch; preserve the mathematical formula, literal source attribution and all existing nearby stable tags. The §21.12.13 toric-potential correspondence is a *downstream convention dependency*, not verified in this run.

## Actual coverage, unresolved ledger and excluded scope

Read fresh production main and AGENTS.md, documentation/proof-expansions.md, collection.json, documentation/integration-layout.md; read the current audit-branch README.md, mathematical-audit/README.md, LATEST.md, LEDGER.md and SECTION_MATRIX.md. The real audit scope is the **support-function/measure/polynomial** steps of §§21.11.50/.58 (prior visits to mixed Alexandrov theory remain separate); the **facet, tropicalization and P^1 normalization** passages of §§21.12.1/.4; and the specific b-divisor defining formula of §20.1.14. §21.12.2, §21.5.4 and §20.1.15 are selected dependencies/context, **not** new theorem certifications. §20.8.1 and §20.3 references encountered but their dedicated approximation prerequisites were **not examined**.

No full proof of §21.11.58 or §21.12.13, no complete mathematical section, and no transitive external-input certification resulted. The established matrix still contains **25 chapters and 747 numbered ToC sections**, **zero entirely mathematically certified sections**. Old confirmed errors, proof gaps, conditional repairs, canonicalization records and external dependencies keep their recorded status; no repeated older issue counts as new. All Demailly approximation / regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof work remains **deferred-by-user**, not resolved or reopened. No formalization, full project tests, build, CI, main changes or website publication were performed.
