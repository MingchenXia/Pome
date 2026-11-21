# General Green-capacity interaction; direct Poincaré–Lelong and reduced-space psh review

**Date:** 2026-11-21  
**Main reference:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\` (fresh branch check).  
**Finding:** \`POME-GREEN-CAPACITY-GENERAL-CROSS-INTERACTION-001\` — **low / verified conditional deduction**, **not** a printed theorem error or an unconditional upstream proof-chain certification.  
**Audit branch:** \`review/mathematical-audit\`.

## Exact scope and immutable reading-edition anchors

The mathematical content was directly read in the **current integrated** edition, not reconstructed from original source theorem numbers:

1. **§4.3, polar sets, capacity and sweeping**, \`docs/sections/polar-sets-capacity-and-sweeping/index.html\`, Git blob \`aa814f26482e8ed27e51c945e9202c797449158b\`, mathematical physical lines **7–131**. This section already had a reported whole-section audit on **2026-11-20**. The present work is a further complete **recheck**, **not a newly visited whole section**. Central result: Theorem **4.3.7**, source \`classical-potential-theory:5388371B\`, permanent tag \`ABDF7610F7B2\`, statement **61–69**, proof **74–94**. Theorem **4.3.10**, permanent \`C4F5D8B270EB\`, statement **122**, proof **127–130**, checked for its domination hypotheses but not used to claim an additional complete upstream chain.
2. **§5.5, holomorphic zeros and the Poincaré–Lelong formula**, \`docs/sections/complex-differential-forms-and-positive-currents--holomorphic-zeros-and-the-poincare-lelong-formula/index.html\`, blob \`4231a246a84f17c3808a6f3164644f931aa0c654\`, mathematical lines **7–190**, full direct review. Section permanent tag \`0C34F7796300\`. Lemma **5.5.1** (11–22, permanent \`AD4CF8180187\`), Weierstrass preparation Theorem **5.5.2** (27–66, \`F54A645FF399\`), Proposition **5.5.3** (71–109, \`37EEAF275A32\`), Lemma **5.5.5** (126–157, \`116B90FD9752\`), Theorem **5.5.6** (162–185, \`8D4BA339507E\`), and Example **5.5.8** (190, \`DB42A2BDBC5B\`) all checked as printed.
3. **§9.9, plurisubharmonic functions on reduced spaces**, \`docs/sections/complex-spaces-and-modifications--plurisubharmonic-functions-on-reduced-spaces/index.html\`, blob \`d9d8091b530c9843e5a725b49af2400936aeaa3a\`, mathematical lines **7–90**, full direct review. Section permanent tag \`75F10F3C1577\`. Definition **9.9.1** (11, \`7A62ADAFC2A7\`), Lemma **9.9.2** (19–42, \`83D4170FB2B3\`), Proposition **9.9.3** (47–58, \`D6705783DDAD\`), and Proposition **9.9.4** (63–90, \`B43080BD49F3\`) were read including proofs.
4. **Selected supporting statements only**, not full reviews: §4.5 finite-energy/capacity characterization, particularly lines **81–85**; §9.6.7 principalization formulation **91–112**, §9.5 finite curves and §9.7 proper images as cited in §9.9; §5.9 smooth psh pullbacks; §3.4 one-variable maximum/subharmonic properties.

Source provenance, section tags, distinct valid versions and reader locators are preserved. No Demailly regularization, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas or positivity-loss programme was opened; old records stay **deferred-by-user**, neither resolved nor certified.

## New precise result: strictly subadditive capacity for arbitrary separated positive-capacity compacts

**Hypotheses.** Let \(\Omega\subset\mathbb R^d\), \(d\ge2\), be a **connected, admissible Greenian open set** in the sense preceding Theorem 4.3.7 (physical line 43). Let \(K,L\Subset\Omega\) be **nonempty disjoint compacts**, both of **strictly positive** Green capacity. Put
\[
 a=C_\Omega(K)>0,\qquad b=C_\Omega(L)>0,\qquad
 \gamma=\min_{(x,y)\in K\times L}G_\Omega(x,y)>0.
\]
The last inequality uses connectedness, strict positivity of the Green kernel and off-diagonal continuity on the separated compact product, not any Euclidean-distance approximation. Capacity is normalized by the **Riesz mass** of the equilibrium Green measure exactly as in §4.3.7; no hidden \(2\pi\), Newtonian or logarithmic factor is introduced.

**Conclusion.**
\[
 \boxed{\quad C_\Omega(K\cup L)
 \ \le\ \frac{a+b}{1+\gamma\min\{a,b\}}\ <\ a+b.\quad} \tag{A}
\]
Thus finite positive-capacity conductors have **strictly negative capacity interaction** in *every connected admissible Greenian domain*, including the planar Greenian case. The bound remains valid for unequal shapes and capacities, with no spherical symmetry. It does not assert a sharp constant for any specific pair.

**Proof.** Write \(\eta_K,\eta_L,\nu\) for the equilibrium measures of \(K,L,K\cup L\), respectively, as supplied conditionally by Theorem 4.3.7; \(G\eta_K=V_K\le1\), \(G\eta_L=V_L\le1\), \(G\nu\le1\), and their masses are \(a,b,c=C(K\cup L)\). The equilibrium potential \(V_K\) agrees with the unregularized reduction \(W_K=1\) on \(K\) except for a polar set; similarly for \(L\). Since
\[
 I(\nu)=\int_\Omega G\nu\,d\nu\le\nu(K\cup L)=c<\infty,
\]
the positive restrictions \(\nu_K:=\nu|_K\) and \(\nu_L:=\nu|_L\) have finite Green energy (the kernel is nonnegative), hence do **not** charge polar sets (the standard finite-energy/polar-capacity assertion; see §4.5 and the zero-capacity equivalence in §4.3.7). In particular, \(\int V_K\,d\nu_K=\nu_K(K)\), and analogously for \(L\).

Let \(x=\nu_K(K)\), \(y=\nu_L(L)\); the supports of \(\nu\) are in \(K\cup L\), so \(x+y=c\). Positivity and Tonelli reciprocity give
\[
 \begin{aligned}
 a&\ge\int G\nu\,d\eta_K
   =\int V_K\,d\nu_K+\int V_K\,d\nu_L\\
  &=x+\int_{K\times L}G_\Omega(s,t)\,d\eta_K(s)d\nu_L(t)
  \ \ge\ x+\gamma ay.
 \end{aligned}
\]
Interchanging \(K,L\) gives \(b\ge y+\gamma bx\). Adding,
\[
 a+b\ge x+y+\gamma(ay+bx)
       \ge c\bigl(1+\gamma\min\{a,b\}\bigr),
\]
which is (A), and the inequality is strict because \(\gamma,a,b>0\). No interchange of unrelated limits, sequential compactness, or unproved minimizer symmetry is used. \(\square\)

**Checks and necessity of hypotheses.** For separated closed balls in \(\mathbb R^d\), \(d\ge3\), this is compatible with the *previously recorded* 2026-11-15 two-equal-ball interaction \`POME-CLASS-TWO-BALL-CAPACITY-INTERACTION-001\`; the prior sharper asymptotic and its constants are **not** recounted here. The present new content is the arbitrary-domain/arbitrary-shape quantitative statement. If the Green domain is disconnected with \(K,L\) in different components, cross Green interaction is zero and capacity can be additive. If one compact has zero capacity, the claimed **strict** inequality need not hold; those exclusions are essential. Connectedness and positive capacities cannot be silently dropped. For nonadmissible Greenian opens, this argument has not been certified from Theorem 4.3.7 as quoted.

**Status and correction:** low / verified conditional deduction; no source change is proposed. It is a downstream consequence of the *conditional* equilibrium existence, quasi-everywhere equality, and finite-energy/polar assertions. A full independent certification of those inputs remains open. The affected downstream subjects are Green capacity, balayage, equilibrium charge and quantitative potential comparison, not any false printed theorem.

## Direct audit of §5.5 (no new confirmed printed error)

- **Zero loci and WPT (11–66).** Checked the induction/Fubini null-set argument for identically zero fibers, coordinate axes chosen from the nonzero homogeneous leading polynomial, argument-principle root count, holomorphic power sums and Newton identities, and the two-sided Cauchy-integral proof that the quotient \(f/W\) is a holomorphic unit. The result requires a genuinely nonzero one-variable restriction, explicitly supplied in the statement; no unjustified global analytic branch choices for roots were used.
- **Distribution and sign convention (71–109, 162–185).** With \(dd^c=(i/2\pi)\partial\bar\partial\), the one-variable formula is \(\partial_z\partial_{\bar z}\log|z|^2=\pi\delta_0\), so \(dd^c\log|z|^2=[0]\), not \(2[0]\). The fiberwise Fubini formula and vanishing on pullbacks of null projected sets yield that the singular divisor locus has zero trace mass, allowing the extension by zero. The local order-\(m\) divisor formula has the correct sign and multiplicity. No new discrepancy found.
- **Singular hypersurface step (126–157).** The holomorphic Hankel discriminant uses \(A^{\mathsf T}A\), *not* a Hermitian Gram matrix. Its nonvanishing when the maximal number \(s\) of distinct roots is attained follows because all nonzero \(s\)-minor squares have the **same complex Vandermonde square**, multiplied by a positive integer. Thus no cancellation is missed even though the roots are complex. The proof correctly excludes lower-dimensional singular support from all diagonal coefficient measures.
- **Scope.** The one-variable Laplacian fundamental solution, distribution/current coefficient criterion and certain Riesz/measure facts were selected as inputs; their entire proofs were not re-certified. No duplicate/canonicalization action is justified.

## Direct audit of §9.9 (no new confirmed printed error)

- **Local definition and pullbacks (11–42).** A local ambient representative is transported across arbitrary holomorphic local-model maps by extending coordinate components holomorphically, then composing. The possibility that the result is identically \(-\infty\) on a component is retained: the stronger \(\mathrm{PSH}(X)\) excludes it, whereas *locally* psh functions need not.
- **Maximum principle (47–58).** The compact connected case uses a curve leaving each positive-dimensional branch and the smooth maximum principle on its connected regular covering locus. Upper semicontinuity only restores the limit value *after* the smooth locus has been shown to equal the maximum. This is not an unjustified substitution of disc tests for ambient-extension psh.
- **Codimension-two local upper bound (63–90).** Checked the finite projection, null analytic image of the excluded set, cylinder avoiding that image, normalization of each one-dimensional slice, subharmonic boundary maximum, and final curve test for the omitted exceptional base slices. The claim is **only local upper boundedness**, not automatic psh extension across an arbitrary singular set; the latter is not silently inferred.
- **Uncertified inputs.** Local parametrization and finite-map results (§9.3–9.5), analytic proper-image theorem (§9.7), normalization, plus the smooth pullback/maximum principles remain upstream dependencies. No circularity or independent error is established in this direct section reading, but absence of a detected error is not a full proof certificate.

## Coverage, ledger and repository policy

**New whole-section direct reads in this session:** §§5.5 and 9.9 (**2**). **Whole-section revisit:** §4.3 (**1**, already reported fully on 2026-11-20). **Selected upstream checks:** §4.5, §9.6 and references as specified above, **not** whole sections. **New transitive proof-chain certifications:** **0**. No historic first-visit claim. The maintained inventory remains the actual **25-chapter / 747-section** current-table-of-contents matrix; it is not a list of 747 mathematically verified sections.

**Finding ledger:** one new low-severity verified conditional deduction (\`POME-GREEN-CAPACITY-GENERAL-CROSS-INTERACTION-001\`), zero new confirmed printed errors, zero source repairs certified, and no duplicate merges. Existing confirmed errors, unresolved dependencies and deferred-by-user items remain unchanged.

**Change policy:** audit Markdown only on \`review/mathematical-audit\`; no changes to main, integrated statement or proof bodies, source repositories, canonicalization/registry, permanent tags, publication, website or CI. No builds or tests were executed in this session.