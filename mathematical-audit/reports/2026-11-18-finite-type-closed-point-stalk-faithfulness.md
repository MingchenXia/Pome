# 2026-11-18 — Finite-type closed-point models: a complete §9.58 proof audit and a faithfulness boundary

**Finding:** POME-FT-CLOSED-POINT-STALK-FAITHFULNESS-001  
**Classification:** low / **verified conditional deduction** (no false theorem, proof gap, or confirmed duplicate).  
**Audit scope:** all mathematical assertions and both complete integrated proofs in §9.58; §9.59.1 is *context only*. This is a paper-level mathematical audit, not formal machine verification and not a certification of the surrounding chapter.

## Reproducible source anchors and scope

- Reviewed \`main\`: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`; current ToC \`docs/chapters/index.html\` contains **25 chapters / 747 distinct numbered sections**.
- Integrated section: \`docs/sections/finite-type-algebraic-models-and-analytic-structure-sheaves--finite-type-models-and-nilpotent-structure/index.html\`, blob \`96eb7c1f6ee63ce6d222ed3f608a242a0a64b7f0\`, 72 physical lines.
- §9.58 introduction and standing hypotheses (algebraically closed field \`k\`, finite-type commutative unital \`k\`-algebras, \`Spm\` means *maximal* ideals and retains nilpotents): physical lines **5–8**; section source \`demailly-complex-geometry:7A4DD1AB\`, permanent tag \`22B397F45AFE\`.
- Theorem **9.58.2**, source \`demailly-complex-geometry:3F3FF286\`, permanent \`36502A11961A\`, statement/equation at **11–17**, complete proof at **19–29**.
- Proposition **9.58.3**, source \`demailly-complex-geometry:5EF3B92E\`, permanent \`72F3ADBDFF9A\`, statement at **34–40**, complete proof at **42–58**; zero-divisor counterexample and nilradical/reduction paragraph at **59–61**.
- Adjacent affected dependency only: \`docs/sections/finite-type-algebraic-models-and-analytic-structure-sheaves--products-closed-subspaces-and-projective-charts/index.html\`, blob \`4373897c66d3fae21cab98bec91fff3457d23ade\`, Proposition **9.59.1**, source \`demailly-complex-geometry:20E582B2\`, permanent \`476B5A661E43\`, lines **10–20**. No certification of §9.59 or projective \`Proj\` arguments.

The Demailly approximation/regularization programme and its Bergman, L², OT, multiscale and positivity-loss subprogrammes were not read or used. The name of the independent algebraic source does not introduce those analytic dependencies.

## 1. Audit of Theorem 9.58.2

The hypotheses are essential: \`k\` is algebraically closed and \`A\` is of finite type over \`k\`. No assumption that \`A\` is reduced is used.

**Noetherianity.** For a Noetherian ring \`R\`, induction on the number of direct-sum coordinates proves that submodules of finite free modules, hence finite modules, are finitely generated. For a nonzero ideal \`I\subset R[T]\`, its leading coefficients generate a finitely generated ideal of \`R\`. Choose polynomials in \`I\` with leading coefficients generating this ideal and let \`d\` be the maximum of their degrees. Repeated elimination of leading terms reduces every \`f\in I\` to \`I\cap R[T]_{<d}\`, a submodule of the finite free \`R\`-module of polynomials of degree \`<d\`. These reductions terminate because degrees strictly decrease. Hence \`I\` has finitely many generators. Quotients and localizations inherit Noetherianity by lifting or contracting ideals. The zero ideal and \`d=0\` are harmless.

**Finite-type field lemma.** Suppose \`K=k[t_1,\ldots,t_r,u_1,\ldots,u_s]\` is a field and \`t_i\` are maximal algebraically independent generators. Each \`u_j\` is algebraic over \`k(t_1,\ldots,t_r)\`; after inverting one common nonzero polynomial \`f\`, all are integral over \`R=k[t_1,\ldots,t_r,1/f]\`. Since \`K=R[u_1,\ldots,u_s]\` and finitely many monomials in the integral generators span it, \`K\` is integral over \`R\`. Every \`a^{-1}\in K\` for nonzero \`a\in R\` is integral and its monic equation gives \`a^{-1}\in R\`, so \`R\` would be a field. If \`r>0\`, choose \`c\in k\` for which \`t_1-c\` is not a factor of \`f\`; this nonconstant element cannot be a unit of \`R\`. Thus \`r=0\` and the algebraically closed hypothesis implies \`K=k\`.

For \`a\notin\sqrt I\`, the nonzero finite-type \`k\`-algebra \`(A/I)[1/a]\` has a maximal ideal, whose residue field equals \`k\`; its contraction is a maximal ideal of \`A\` containing \`I\` but not \`a\`. Conversely every nilpotent maps to zero in every residue field. Therefore \` \bigcap_{\mathfrak m\supset I}\mathfrak m=\sqrt I\`, including the empty-intersection convention when \`I=A\`. All steps were checked without invoking the excluded analytic programme.

## 2. Audit of Proposition 9.58.3

**Quasi-compactness and restrictions.** The descending chain condition on Zariski closed sets follows from Noetherianity of radical ideals. Thus every open subset and every open covering of it has a finite subcover. If \`D(t)\subset D(s)\`, Nullstellensatz gives \`t\in\sqrt{(s)}\`, hence \`t^N=sa\` and \`s\` is invertible in \`A_t\`. This is the required direction for the localization restriction \`A_s\to A_t\`.

**Sheaf gluing with zero divisors.** For a finite basic cover \`D(t_i)\` of \`D(1)\`, the ideal generated by the \`t_i\` is the unit ideal. For compatible \`x_i=a_i/t_i^{n_i}\`, equality in \`A_{t_it_j}\` yields
\[
 (t_it_j)^{N_{ij}}\big(t_j^{n_j}a_i-t_i^{n_i}a_j\big)=0
\]
*in A*, not just after further localization. Choose a common integer \`r\ge n_i+N_{ij},n_j+N_{ij}\` for all pairs, and \`b_i=t_i^{r-n_i}a_i\`. Then \`t_j^rb_i=t_i^rb_j\` in \`A\`. Because \`(t_i^r)=A\`, write \`1=\sum c_it_i^r\` and \`a=\sum c_ib_i\`. This restricts to every \`x_j\`; the same finite-power clearing proves uniqueness. The printed example \`A=k\times k\`, \`t_1=(1,0)\`, \`t_2=(0,1)\`, \`a_1=(0,1)\`, \`a_2=0\` verifies that replacing localized equality by equality in \`A\` without clearing powers would be wrong. The **printed proof does clear powers correctly**.

**Stalks, functoriality, and the empty space.** The filtered colimit of the basic localizations over \`s\notin\mathfrak m\` equals \`A_{\mathfrak m}\`; its residue field is \`k\`. An algebra map \`\phi:A\to B\` induces the point map \`\mathfrak n\mapsto\phi^{-1}(\mathfrak n)\` and local fraction maps. Conversely global sections recover \`\phi\` from a local morphism of \`k\`-ringed spaces; locality fixes the point map and every fraction map. Hence the claimed *ringed-space* anti-equivalence holds. For \`A=0\`, all localization rings and the unique empty-open section ring are the zero ring, and there are no maximal ideals. The nilradical is finitely generated by Noetherianity and nilpotent by the elementary pigeonhole bound \`1+\sum(e_i-1)\` for nilpotence exponents \`e_i\`; localization preserves its quotient. The reduction loses precisely nilpotent sections, not points.

## 3. New corollary: stalk faithfulness vs. closed-point evaluations

**Statement.** For every finite-type commutative unital \`k\`-algebra \`A\` under the printed hypotheses, both canonical maps
\[
 \rho_{\rm loc}:A\longrightarrow\prod_{\mathfrak m\in\operatorname{Spm} A}A_{\mathfrak m},
 \qquad
 \rho_{\rm pt}:A\longrightarrow\prod_{\mathfrak m\in\operatorname{Spm} A}A/\mathfrak m\simeq k^{\operatorname{Spm} A}
\]
are defined, with
\[
 \boxed{\ker\rho_{\rm loc}=0,\qquad\ker\rho_{\rm pt}=\sqrt{(0)}.}
\]
Thus global sections are detected by all **local-ring stalks**, even for a nonreduced algebra, while their **scalar values at closed points** detect only the reduction.

**Proof.** If \`a\ne0\`, its annihilator \`\operatorname{Ann}(a)\` is proper. Choose a maximal ideal \`\mathfrak m\supset\operatorname{Ann}(a)\`. Were \`a/1=0\` in \`A_{\mathfrak m}\`, some \`s\notin\mathfrak m\` would satisfy \`sa=0\`, contradicting \`s\in\operatorname{Ann}(a)\subset\mathfrak m\`. Thus \`\rho_{\rm loc}\` is injective. By Theorem 9.58.2 with \`I=0\`, \`\ker\rho_{\rm pt}=\bigcap_{\mathfrak m}\mathfrak m=\sqrt{(0)}\`. The case \`A=0\` is tautological. No compactness, connectedness, smoothness, or reduction assumption has been smuggled in.

**Sharp nonreduced boundary.** With \`A=k[\varepsilon]/(\varepsilon^2)\`, \`X=\operatorname{Spm}A\` is one closed point, \`\rho_{\rm pt}(\varepsilon)=0\` but \`\rho_{\rm loc}(\varepsilon)=\varepsilon\ne0\` in its local ring. The two local \`k\`-algebra endomorphisms
\[
 \phi_0(\varepsilon)=0,\qquad \phi_1(\varepsilon)=\varepsilon
\]
induce the **same underlying point map and identical residue-field maps**, but distinct morphisms of local \`k\`-ringed spaces. Likewise the \`k\`-algebra automorphisms \`\varepsilon\mapsto c\varepsilon\` for distinct \`c\in k^\times\` act identically on the closed-point set while remaining different on the sheaf. This explicitly tests why Proposition 9.59.1 must take ringed-space morphisms and tensor-product structure sheaves, not just set-theoretic maps. It is **not** a counterexample to either printed theorem.

## Audit verdict, dependency ledger and limits

- **Theorem 9.58.2:** checked all claims and the complete printed Noetherianity/field/radical proof; **no confirmed error or missing proof step** at current main. Elementary maximal-ideal existence is the only background algebraic existence fact; the other required arguments are supplied in the proof.
- **Proposition 9.58.3:** checked the complete quasi-compactness, localization/gluing, stalk, morphism, nilpotence, and empty-ring claims, including compatibility with nonreduced rings; **no confirmed error or missing proof step**.
- **POME-FT-CLOSED-POINT-STALK-FAITHFULNESS-001:** low / **verified conditional deduction** from the two checked results plus the annihilator argument; complete self-contained proof above. The point-set countertest is an example of lost infinitesimal information, not a genuine duplication or a repaired theorem.
- **Affected dependents:** Proposition 9.59.1 (algebraic products and closed subspaces), Theorem 9.59.2 (projective charts) and §9.60 (analytic local models). These are *not* fully audited here; retain their distinct hypotheses, tags and nilpotent structure under any proposed canonicalization.
- **Coverage:** §9.58 had earlier selected direct checks; this run closes the **remaining full-section mathematical proof review** of that section (both numbered environments, introductory and concluding claims). **+0 first-visited numbered sections, +1 section with complete direct mathematical audit;** other 746 sections are not thereby certified. §9.59.1 was compared only as a dependent, not fully checked. The actual main table of contents remains 25 chapters and 747 unique sections.
- **Excluded/deferred:** Demailly regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes remain **deferred-by-user**, neither resolved nor certified. No build, test suite, CI, publication, or source/registry/tag mutation was performed.
