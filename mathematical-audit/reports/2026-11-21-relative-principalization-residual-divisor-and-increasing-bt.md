# 2026-11-21: increasing Bedford–Taylor products and the residual divisor in relative principalization

**Audit baseline:** main b6933b772f41b45918f7e25ed1afbbb1fd892272; review branch review/mathematical-audit. This examines the current Pome reading edition only. The Demailly approximation/regularization, dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme was not reopened.

## Exact inspected material

- **Full mathematical §7.6**, docs/sections/bedford-taylor-products-and-local-capacity--increasing-limits-and-exceptional-envelopes/index.html; blob 5e763bdc928794938c37dc3c7a51cc406472d076, **physical lines 7–80**, 91 lines total. Section permanent tag E5550B44EC7B. Theorem 7.6.1 source label foundations-of-pluripotential-theory:36787F42, permanent tag A4C45B704647, lines 11–59; Corollary 7.6.2 source label foundations-of-pluripotential-theory:2ACED3F4, permanent tag D865A8538D7D, lines 63–80.
- **Selected Theorem 9.7.5 and full proof only**, not all §9.7: docs/sections/complex-spaces-and-modifications--proper-images-and-relative-principalization/index.html; blob b44fe157b8c01363da7799990b8ef6ed82525553, **lines 89–127**, erroneous Step 3 sentence **line 120**. Source label foundations-of-pluripotential-theory:1524D010; permanent tag 689628C7AF7F. The Remmert/Remmert–Stein proofs in the same section were not fully audited in this session.
- **Selected premise:** Theorem 9.6.7, the marked-ideal transform (9.6.8), and associated divisor explanation, docs/sections/complex-spaces-and-modifications--blowups-and-resolution/index.html, blob f452f4b1abe5cdfe348ae11fcd934febcfdd570b, **lines 91–107**. Source B74A86AD, permanent 24330D25741D. Definition 9.6.1, permanent 757D038DF549, was also consulted.

## Finding POME-RELPRINC-RESIDUAL-DIVISOR-NONEXCEPTIONAL-001

**Severity: low. Classification: confirmed error in an ancillary proof statement; not a false theorem.** Theorem 9.7.5 states that one may obtain a divisor \(H\) exceptional for \(f\), and a divisor \(H'\) disjoint from the strict transform \(W'\), together with three ideal identities. Its proof at line 120 adds the stronger assertion that \(H'\) is supported on the exceptional divisors of \(g\). This stronger assertion is **false**. An invertible, nonexceptional divisorial component of the original residual ideal survives principalization as a strict-transform divisor.

### Explicit counterexample

Let \(M=\mathbb P^2\), let \(W=\{p\}\) be a point, choose a projective line \(L\subset\mathbb P^2\) with \(p\notin L\), and take the coherent ideal
\[
\mathfrak a=\mathcal I_L=\mathcal O_M(-L).
\]
The theorem's nonvanishing condition holds because \(\mathfrak a\mathcal O_W=\mathcal O_W\). As \(\dim W=0\), the initial principalization on \(W\) has no centers: \(t=0\), \(M_t=M\), \(W_t=W\), \(H_t=0\), and \(\mathfrak a_t=\mathcal I_L\).

Blowing up a Cartier divisor is an isomorphism: locally \(L=\{f=0\}\) with \(f\) a nonzerodivisor, and the graph of the sole generator \(f\) lies in \(M\times\mathbb P^0=M\). Blowing up the smooth divisor \(L\), then dividing by its full inverse image \(E=L\) in the marked-ideal transformation (9.6.8), gives the unit transformed ideal. Hence one legitimate principalization is \(g=\mathrm{id}_M\) as a map and \(H'=L\). But \(g\) has **no contracted exceptional divisors**, whereas \(H'\neq0\). The distinction is not merely the choice of principalization: any bimeromorphic principalization of \(\mathcal I_L\) retains a component mapping dominantly onto \(L\), because its pullback has order one along the strict transform of the generic point of \(L\). Such a component is not exceptional.

This example satisfies the actual conclusion of 9.7.5 with \(M'=M\), \(f=\mathrm{id}\), \(H=0\), \(H'=L\), \(W'=W\). Indeed:
\[
\mathcal I_W\mathcal O_{M'}=\mathcal O_{M'}(-H)\mathcal I_{W'},\qquad
\mathfrak a\mathcal O_{M'}=\mathcal O_{M'}(-H-H'),
\]
and
\[
(\mathfrak a\mathcal O_W)\mathcal O_{W'}=\mathcal O_{W'}(-H|_{W'}).
\]
Moreover \(H'\cap W'=\varnothing\). Therefore **Theorem 9.7.5 itself is not refuted**. Only the additional sentence about \(H'\) being exceptional for \(g\) is wrong. The notation of an "exceptional factor" \(E_i\) in a marked-ideal algorithm does not force its image to have codimension at least two: blowing up a Cartier divisor is already the identity morphism.

### Verified local correction

Replace the false sentence by:

> The divisor \(H'\) is supported on \(g^{-1}(V(\mathfrak a_t))\), which is disjoint from \(W'=g^{-1}(W_t)\), since \(\mathfrak a_t\) is the unit ideal near \(W_t\).

This follows directly from the defining equality
\[
\mathfrak a_t\mathcal O_{M'}=\mathcal O_{M'}(-H')
\quad\Longrightarrow\quad
\operatorname{Supp}H'=V(\mathfrak a_t\mathcal O_{M'})
=g^{-1}(V(\mathfrak a_t)).
\]
The proof's Step 4 *separately* shows that \(H\), unlike \(H'\), is \(f\)-exceptional, because the images of its components are contained in the positive-codimension centers inside \(W\), hence have codimension at least two in \(M\). This one-sentence repair is valid **conditional on the accepted principalization input**, without changing the theorem, permanent labels, or attribution.

**Affected dependents:** Step 3 of Theorem 9.7.5 and any eventual application that needs \(H'\) to be exceptional instead of merely disjoint from \(W'\). No specific downstream misuse was established by this selected check. A reviewable future source patch should remove "exceptional" only for \(H'\), preserve the proof of exceptionality of \(H\), and not merge the two divisors.

## Full direct mathematical review of §7.6

**Theorem 7.6.1 (lines 11–59).** An increasing family of locally bounded psh functions with almost-everywhere limit a locally bounded psh \(u_l\) satisfies \(u_{l,j}\le u_l\) *everywhere* because psh representatives agreeing almost everywhere agree everywhere. Together with the increasing lower bound, this supplies uniform bounds on compact subsets. The \(q=0\) base case is dominated convergence, and taking \(dd^c\) of weighted \((q-1)\)-factor convergence gives the unweighted \(q\)-factor statement.

The collar maximum \(\max(v,A\psi)\) preserves the products on an interior ball and makes all quantities fixed near the outer boundary. The fixed collar justifies passing integrals over the full intermediate ball, rather than treating its characteristic function as a compactly supported test. For the weighted induction step, any subsequential weak limit \(\Theta\) of \(u_{0,j}S_j\) satisfies \(\Theta\le u_0S\) as currents: positivity of \((u_0-u_{0,j})S_j\) and the fixed-weight upper semicontinuity are used in that direction. The sign remains correct under normalization to negative psh functions. The reverse **trace-mass** inequality follows by fixing \(k\), using \(u_{0,j}\ge u_{0,k}\) for \(j\ge k\), then taking \(j\to\infty\) through the fixed-quasi-continuous-weight lemma and \(k\to\infty\) through unweighted monotone continuity plus bounded-current integration by parts. Since \(u_0S-\Theta\) is positive, compactly supported in the intermediate ball, and has zero trace mass, it vanishes. Precompactness and the subsequence contradiction conclude convergence of the full sequence.

For the **capacity** conclusion, the order \(q=n\) version of the weighted convergence controls both terms in the difference
\[
\int_B(\widehat u_l-\widehat u_{l,j})(dd^c\widehat u_{l,j})^n\longrightarrow0.
\]
The cited quantitative capacity estimate (7.4.6), together with quasi-continuity and a strict-level \(\delta/2\) comparison, then yields local convergence in outer capacity. The proof does not mistakenly infer capacity convergence simply from almost-everywhere convergence.

**Corollary 7.6.2 (lines 63–80).** The reduction to a countable subfamily of the upper envelope, successive finite maxima \(v_j\), bounded truncations \(\max(v_j,-m)\), and countable unions of the rational strict-level gaps is logically consistent. It needs neither measurability of the unregularized supremum nor sequential compactness of an arbitrary family. The example with \(u_j=\max\{j^{-1}\log|z_1|,-1\}\) has a nonempty pluripolar gap on \(\{z_1=0\}\), as the text claims.

**Result:** No new confirmed printed error in §7.6. The check is substantive but **conditional** on cited results 7.2.5 (CLN), 7.3.8 (fixed-weight integration-by-parts form), 7.4.6 (quantitative capacity), 7.5.2/7.5.7 (quasi-continuity and weighted convergence), and 5.9.1/5.10.2 (representatives and envelopes). The complete proofs of these external-to-the-section references were not recertified in this session.

## Open, resolved, deferred and scope accounting

- **Open confirmed proof-only error:** POME-RELPRINC-RESIDUAL-DIVISOR-NONEXCEPTIONAL-001; the explicit counterexample and one-sentence proposed repair above are verified locally; no source/body patch has been merged.
- **No new printed theorem counterexample:** Theorem 9.7.5 remains valid; 7.6.1 and 7.6.2 have no additional newly confirmed error from this direct reading.
- **External input:** Hironaka principalization 9.6.7, permitted by the audit rules, remains an external theorem, not independently proved here.
- **Unresolved transitive dependencies:** §7.6 cited proofs, the unreviewed remainder of §9.7, and untracked downstream uses of the false extra statement. Do not mark them certified.
- **Deferred-by-user, unchanged:** Demailly regularization/approximation and all named Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss completion efforts.
- **Actual added scope:** **+1 entire direct mathematical section (§7.6)**, **+1 selected theorem/proof (§9.7.5)**, **+1 selected §9.6.7 input**, **+0 fully certified upstream chains**. Earlier audits of these chapters remain counted historically, not claimed to be first visits.
- No builds, tests, GitHub Actions CI, publication, body/source/registry/tag or main edits.
