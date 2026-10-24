# Finite-curve polar retractions: exact total-variation projection constant and the degree-two threshold

**Audit date:** 2026-10-24 (Asia/Shanghai). **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting review branch:** c415400c20ea5b9147b81bedb59e4f1c5ec061fa. **Actual new proof-level coverage:** selected integrated passages of §§18.19–18.21 and 18.23–18.24, previously listed as inventory-only; §18.22 and §13.29 are dependencies, not newly recertified. All findings below concern the current integrated reading edition, not source-book numbering. No entire section certified.

## Exact current main evidence

All paths below are within the public MingchenXia/Pome repository at the pinned main SHA. The listed line numbers are **physical HTML source lines**, not screen-wrapped browser lines.

| Section and exact file | Current blob SHA | Mathematically checked anchors |
| --- | --- | --- |
| §18.19, docs/sections/multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--equality-below-all-obstacles-on-separated-products/index.html | 210f78503d542610158a162e3d9aa670c317e97b | Lemma 18.19.1, source non-kahler-pluripotential-theory-D5E145AE, permanent tag AFE454C19DE7, lines 10–47; Proposition 18.19.2, source C2A5E634, tag 36E07E6B83DA, lines 60–72; Corollary 18.19.3, source 62E5083B, tag 9E4426687FC0, lines 76–92. |
| §18.20, docs/sections/multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--auxiliary-compact-complex-factors/index.html | f1b6f67c60fe76ec140541127caf1203fea7ff7f | Lemma 18.20.1, source 99435545, tag F61F12847624, lines 19–39; Proposition 18.20.2, source B1DF5EB4, tag 85AC8B179E4B, lines 58–71; Corollaries 18.20.3–4, sources 0CCF8E3F/9C6B848E, tags 1B6E50A3B70B/47BA03C63283, lines 75–105. |
| §18.21, docs/sections/multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--a-polar-metric-in-a-background-with-unbounded-mass/index.html | 6b792da459c824cdf1aa665b07965695b4d28e98 | Example 18.21.1, source non-kahler-pluripotential-theory-C569F5CB, tag 00A4B8521863, lines 10–48. |
| §18.23, docs/sections/multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--finite-curve-factors/index.html | 87f97f2e03fb722d66ebf35be56c8bceef7c31f6 | Proposition 18.23.1, source non-kahler-pluripotential-theory-CA9D0D47, tag 6235BDB38282, lines 16–46; Example 18.23.2, source 19AC45D8, tag 47BCB7DF51C8, lines 50–76. |
| §18.24, docs/sections/multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--models-pulled-back-by-a-finite-curve-map/index.html | dd427a692bda2c364ae83207717a16bcac070cdc | Proposition 18.24.1, source non-kahler-pluripotential-theory-84211D78, tag 424A6AE6F169, lines 10–22; **Proposition 18.24.2**, source non-kahler-pluripotential-theory-6421C90F, tag **C8EE003DDDC9**, lines **26–63**; Corollary 18.24.3, source 5D79DF2B, tag F204E0019263, lines 67–82; Example 18.24.4, source 542A2364, tag 2C40EC6336AD, lines 89–115. |

The source IDs, permanent tags, conventions and attribution are to be preserved; no canonicalization or source-body edit is proposed.

## POME-CURVE-FINITE-RETRACT-SHARP-001 — verified conditional deduction / low

**Nature:** an exact sharpening of the finite-map retraction in Proposition 18.24.2 and of the degree-three witness in Example 18.24.4. **Not a false printed proposition; no missing printed hypothesis.**

**Hypotheses.** Let \(r:C'\to C\) be a finite surjective holomorphic map of degree \(d\ge1\) between connected compact Riemann surfaces, and let \(\beta\) be a smooth real \((1,1)\)-form with \(A=\int_C\beta\ge0\). Write \(\sigma=r^*\beta\). Assume the curve classification of §13.29.1 and the finite-map polar measure pullback of §5.43.16 as invoked in the **integrated** Proposition 18.24.2. Thus the ordinary model space \(\mathcal M(\sigma)\) is parametrized by positive polar curvature measures \(\mu\) of mass at most \(dA\), with distance \(\|\mu-\nu\|_{\rm TV}\). The embedded base-model locus is \(J(\mathcal M(\beta))\) for \(J(v)=v\circ r\). Proposition 18.24.2 defines the 1-Lipschitz retraction
\[
R(q)=J\left(p_\beta\left(d^{-1}r_*\mu_q\right)\right),
\qquad
\mu_{R(q)}=P\mu_q,\quad P=d^{-1}r^*r_*.
\]

**Exact strengthening.** For every \(q\in\mathcal M(\sigma)\),
\[
\boxed{\quad
d_\sigma(q,R(q))\ \le\
2\left(1-\frac1d\right)
\operatorname{dist}_{d_\sigma}\bigl(q,J(\mathcal M(\beta))\bigr).
\quad} \tag{1}
\]
For \(d=1\), both sides are zero and \(R\) is the identity. For \(d=2\), \(R\) is therefore **a nearest-point retraction**, though generally **not the unique nearest-point selection**. For every \(d\ge3\) and **positive** base area \(A>0\), the coefficient \(2(1-1/d)\) is optimal: on a regular degree-\(d\) fiber there is an analytic, ideal model \(q\) such that
\[
\boxed{\quad
\operatorname{dist}\bigl(q,J(\mathcal M(\beta))\bigr)=m,
\qquad
d_\sigma(q,R(q))=2m\left(1-\frac1d\right)>m ,
\quad} \tag{2}
\]
where \(0<m\le dA\) is the chosen polar mass. In particular, **when \(A>0\), \(R\) is a nearest-point retraction for every model if and only if \(d\le2\)**. When \(A=0\), both model spaces are smooth singletons (§18.24.2), and the metric-projection property holds trivially for every degree. The same conclusions hold under the common \(d^{-1}\) rescaling of distances for the \(p\)-normalized models in Corollary 18.24.3; there is no claim of uniqueness of their nearest models.

### Proof, including ramification and signed measures

**1. Fiber counting and order.** For \(x\in C'\), let \(e_x\ge1\) denote the local multiplicity of \(r\) at \(x\). For a finite positive Borel measure \(\mu\) on \(C'\) and bounded nonnegative Borel \(f\), the finite-map pullback convention gives
\[
\int_{C'} f\,d(r^*r_*\mu)
=\int_{C'} \left(\sum_{x:r(x)=r(z)}e_x f(x)\right)d\mu(z).
\tag{3}
\]
On the complement of the finite branch locus this is the sum over local inverse sheets; at a branch point it is the usual local \(t=z^{e_x}\) counting multiplicity. Every fiber sum contains the term \(e_z f(z)\ge f(z)\); thus
\[
r^*r_*\mu\ge\mu,\qquad P\mu\ge\mu/d.
\tag{4}
\]
The finite degree identity \(r_*r^*\lambda=d\lambda\) holds for **all finite signed measures** on \(C\), including atoms at branch values, since \(\sum_{x:r(x)=y}e_x=d\). Consequently \(P^2=P\), \(P\) is positive and total-mass preserving on positive measures, and on real signed measures
\[
\|P\tau\|_{\rm TV}
=d^{-1}\|r^*r_*\tau\|_{\rm TV}
=\|r_*\tau\|_{\rm TV}
\le\|\tau\|_{\rm TV}.
\tag{5}
\]
The equality uses the fact that pullbacks of mutually singular positive measures on \(C\) are mutually singular on \(C'\); it is **not** a claimed identity \(\|r_*\tau\|=\|\tau\|\).

**2. Exact complementary-projection norm.** If \(\mu\ge0\) has mass \(M\), then by (4)
\[
\mu-P\mu=
\left(1-\frac1d\right)\mu-
\left(P\mu-\frac1d\mu\right).
\tag{6}
\]
Both terms on the right are positive measures of equal mass \((1-1/d)M\), so
\[
\|(I-P)\mu\|_{\rm TV}\le2(1-1/d)M.
\tag{7}
\]
For a general real signed measure \(\tau=\tau^+-\tau^-\), apply (7) separately to its Jordan parts and use the triangle inequality:
\[
\|(I-P)\tau\|_{\rm TV}
\le2(1-1/d)\|\tau\|_{\rm TV}.
\tag{8}
\]
If \(d\ge2\), choose any point \(x\) in an unramified fiber \(r^{-1}(y)=\{x=x_1,\ldots,x_d\}\) and take \(\tau=\delta_x\). Then
\[
P\delta_x=d^{-1}\sum_{j=1}^d\delta_{x_j},\qquad
\|(I-P)\delta_x\|_{\rm TV}=2(1-1/d).
\tag{9}
\]
Therefore
\[
\boxed{\|I-P\|_{\mathrm{TV}\to\mathrm{TV}}=2(1-1/d)}
\tag{10}
\]
for **every** finite map of degree \(d\), regardless of ramification. For \(d=1\), \(I-P=0\). This argument is valid for arbitrary signed measures, not just atomic measures and not just probability measures.

**3. Relation with the geometric model locus.** By the printed measure-level description and curve classification, the embedded locus consists exactly of admissible polar measures fixed by \(P\). Indeed \(P(r^*\nu)=r^*\nu\), while for any \(P\mu=\mu\) one has \(\mu=r^*(d^{-1}r_*\mu)\), and the base measure is positive, polar and of mass at most \(A\). The retraction \(R\) preserves admissibility because \(P\) preserves positivity, polar support, and total mass. Hence for any embedded model \(v\) with polar measure \(\nu\), \(P\nu=\nu\), and (8) yields
\[
\|\mu_q-P\mu_q\|_{\rm TV}
=\|(I-P)(\mu_q-\nu)\|_{\rm TV}
\le2(1-1/d)\|\mu_q-\nu\|_{\rm TV}.
\]
Infimizing over \(v\) proves (1). In degree two the factor is precisely one and \(R(q)\) lies in the embedded locus, so \(R(q)\) achieves the minimal distance; this is a **complete** proof of the degree-two projection claim conditional only on the cited Pome finite-map/classification facts.

**4. Sharpness for every degree at least three.** Suppose \(A>0\), take a regular fiber as in (9), and choose \(0<m\le dA\). By the curve model classification there is a normalized model \(q\) with polar measure \(m\delta_x\); its isolated logarithmic pole is analytic, and its polar curvature is purely atomic, so this example may be taken in the analytic ideal subspace. The image of the base zero-polar model has zero polar measure, giving distance \(m\). Conversely, every image polar measure \(r^*\nu\) assigns the **same** mass \(b=\nu(\{y\})\) to each of \(x_1,\ldots,x_d\), and may carry other positive mass \(M_{\rm out}\). Thus
\[
\|m\delta_x-r^*\nu\|_{\rm TV}
\ge |m-b|+(d-1)b+M_{\rm out}
\ge m\quad(d\ge2).
\tag{11}
\]
This proves the first equality in (2). Equation (9) gives its second equality. In degree \(d\ge3\) the latter is strictly larger than \(m\), so \(R\) cannot be a nearest-point retraction. The ratio is exactly the universal constant in (1), which is therefore sharp on *admissible analytic models*, not only on arbitrary signed measures.

**5. Nearest-point nonuniqueness in degree two.** With \(d=2\), the same example has two distinct nearest images: the zero-polar model and \(R(q)\) itself. Both have distance \(m\) from \(q\) by (9) and (11), while \(m>0\) makes their polar measures different. More generally any positive base atom \(b\delta_y\) with \(0\le b\le m\) and \(b\le A\) gives the same distance. Thus the new degree-two assertion **does not** say that the metric space admits a unique nearest-point map.

**6. Dependents and bounds of the conclusion.** Corollary 18.24.3 transports the estimates to compact holomorphic fibrations with a finite curve factor; the \(p\)-normalized metric is \(d^{-1}\) times the \(q\)-normalized one (§18.23.1), so nearest-point assertions and multiplicative ratios are invariant under this rescaling. The original Proposition 18.24.2 asserts only 1-Lipschitz retraction and commutation with ideal projection; it remains correct. Example 18.24.4 exhibits one cubic failure; (2) shows that **every** degree \(\ge3\) finite curve map over a positive-area base has such a failure. No other curvature/PDE theorem is deduced.

**Suggested editorial action:** optional standalone corollary after Proposition 18.24.2 giving (1), (10), and the sharp nearest-point threshold. Keep the earlier example, attribution and permanent tags. **Affected dependents:** nearest-model selection on finite-map pullback loci (§18.24.3), comparison with the *different* nearest ideal projection (§18.20.2 and §18.24.2). No source, canonicalization, registry or published page has been changed.

## Other selected proof checks performed (no independent new finding ID)

1. **§18.19, lines 23–46, 70–72, 86–92:** verified the reduction of additive ordinary singularity order to individual factors by fixing coordinates at a common finite point, the finite-stretch sum of competitors, and the direction of the zero-obstacle implication toward all smooth (potentially mixed-coordinate) obstacles. The use of a common finite slice is legitimate for a *finite* product of nontrivial psh potentials. The curve classification and all-obstacle transport remain internal conditional dependencies; this is not a transitive certification.
2. **§18.20, lines 10–16, 33–39, 65–70, 93–105:** checked that a semipositive form which vanishes on every \(Y\)-slice has no mixed \(Y,T\) coefficients by the positive-semidefinite Hermitian matrix kernel property; the product test form in the zero-area case is \(d\)-closed even when \(\omega_T\) is non-Kähler because its \(T\)-power has *top degree*; the direct positivity proof of bigness when all curve areas and vertical \(\alpha\) are positive; and that the model isometry uses only polar data, not an ambient mass bound. Dependence on the original divisor-of-weight-one envelope/mass reduction, curve ordinary-model classification and analytic restriction statements is **not** newly resolved.
3. **§18.21, lines 17–47:** independently checked \(\dim_{\mathbb C}M=2+3+1=6\), the coefficient \(6!/(1!\,1!\,1!\,3!)=120\), the blockwise positive-current inequality and the gap between infinite ambient smooth upper mass and vanishing model-type extended volumes. The divergence of the Hopf threefold mass sequence is the separately stated Theorem 23.1.1, **not** newly reproved; no numerical script was run.
4. **§18.23, lines 30–46 and 60–76:** checked the factor \(d\) in \(\int_{C'}r^*\beta=d\int_C\beta\), its effect on Gauduchon pushforward trace normalization, and the loss of sheet information under \(r_*\) in Example 18.23.2. Branch points are omitted only from the *smooth area* covering calculation; polar atoms there require and retain local multiplicities in the independent §18.24 measure argument.
5. **§18.24, lines 20–22, 48–63, 78–82, 95–115:** checked the fiber-maximum comparison's direction, \(r_*r^*=d\), total-variation contraction, admissibility of the averaged polar measure, volume preservation, commutation with extraction of atomic polar parts, and the cubic example's numerical \(4/3>1\). Finite-map fiber-maximum psh descent (§5.43.15), polar pullback (§5.43.16) and full curve classification (§13.29.1) are named **internal dependencies** of this review, not fully checked here.

## Coverage, unresolved conditions, and exclusions

Exactly §§18.19, 18.20, 18.21, 18.23 and 18.24 receive **selected proof-passage coverage** at the pinned main SHA. Previously reviewed §18.22 and contextual §13.29, §5.43 do not receive renewed certification; the 25-chapter / 747-section coverage inventory remains an **inventory**. No theorem in these five sections is classified as false by this run, and no printed proof gap is asserted. The new quantitative result is a conditional deduction, not a complete reconstruction of all upstream Pome theorems. No software test, full build, CI, automatic merge, publication or formalization was run.

**Hard user exclusion:** Demailly approximation/regularization and its dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion work were neither opened nor extended. Their historical findings remain **deferred-by-user**, never resolved or certified. Other outstanding ledger items are unchanged.
