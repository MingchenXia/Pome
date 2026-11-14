# Moving-circle Bedford–Taylor slicing: a Borel interface and failure of slice total-variation continuity

**Finding ID:** \`POME-NPP-MOVING-CIRCLE-FIBER-TV-001\`
**Status:** verified conditional deduction, **low** severity; **no printed lemma or theorem refuted**.
**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\` (freshly fetched 2026-11-14).
**Integrated reading file:** \`docs/sections/non-pluripolar-products--bounded-factors-and-the-first-degree-product/index.html\`, production blob \`d234ab96e33bfd24ad1d53d29332b2c021cddeff\`.
**Direct proof passages:** Lemma 13.4.4, source \`foundations-of-pluripotential-theory:C504A6B9\`, permanent tag \`CA3A887474EE\`, physical lines **133–153**; Lemma 13.4.5, source \`foundations-of-pluripotential-theory:638C435E\`, permanent tag \`4AD0BFC1BFCD\`, physical lines **157–190**; slicing equation 13.4.6, source \`foundations-of-pluripotential-theory:917DDB45\`, permanent tag \`7F078C7DCBDD\`, physical lines **163–165**. Consulted Proposition 13.4.7, source \`foundations-of-pluripotential-theory:D1BF7EF2\`, permanent tag \`3553558C2E27\`, lines **194–197**, for downstream scope only.

## Precise claim and hypotheses

Use Pome's \(\mathrm{dd}^{\mathrm c}=\frac{i}{2\pi}\partial\bar\partial\) convention, so that \(\mathrm{dd}^{\mathrm c}\log|x|^2=\delta_0\) on \(\mathbb C\). Fix arbitrary integers \(r,m\ge1\), and define
\[
Q=\Delta_2^r\subset\mathbb C^r,\quad D=\Delta^m\subset\mathbb C^m,\quad
\rho=\tfrac12,\quad R(z)=\max\{|z_1|,\rho\},
\]
where \(\Delta_a=\{w:|w|<a\}\). For \(j=1,\dots,r\), set
\[
u_j(x,z)=\max\{\log|x_j|^2,\log|z_1|^2,2\log\rho\}.
\tag{A}
\]
The functions are bounded, continuous and plurisubharmonic on \(Q\times D\), including the axes. Write
\[
M=\bigwedge_{j=1}^{r}\mathrm{dd}^{\mathrm c}u_j,\quad
M_z=\bigwedge_{j=1}^{r}\mathrm{dd}^{\mathrm c}_x u_j(\cdot,z),\quad
\lambda_s=\frac1{2\pi}\int_0^{2\pi}\delta_{se^{i\vartheta}}\,d\vartheta.
\]
Here \(\lambda_s\) is a **probability** circle measure and \(dV_D\) is ordinary Lebesgue volume on the base.

**Exact independent model calculation:**
\[
\boxed{ M_z=\lambda_{R(z)}^{\otimes r},\qquad
p_D^*dV_D\wedge M
=\int_D\lambda_{R(z)}^{\otimes r}\,dV_D(z).}
\tag{B}
\]
The right equality is as positive Radon measures on \(Q\times D\), hence is valid on **every Borel set** and against every bounded Borel compactly supported test function; no density with respect to full Lebesgue measure is asserted.

For the Borel interface sets
\[
E_==\{(x,z):|x_1|=|z_1|\},\qquad
E_>=\{(x,z):|x_1|>|z_1|\},
\]
the exact values are
\[
(p_D^*dV_D\wedge M)(E_=)=\tfrac34\pi^m,\quad
(p_D^*dV_D\wedge M)(E_>)=\tfrac14\pi^m,\quad
(p_D^*dV_D\wedge M)(Q\times D)=\pi^m.
\tag{C}
\]
Both \(E_=\) and its complement boundary are Lebesgue-null in the \(x_1\)-direction: the first equality is therefore a genuinely **singular-interface** measure evaluation, not an ordinary density/Fubini calculation.

Furthermore, \(z\mapsto M_z\) is narrowly continuous (indeed continuous against every compactly supported continuous test), but if \(z^{(k)}\to z\) with \(1/2<|z_1|<1\) and \(|z^{(k)}_1|\ne|z_1|\), then
\[
\|M_{z^{(k)}}-M_z\|_{\mathrm{TV}}=2
\quad\text{for every }k
\tag{D}
\]
for the total-variation **norm** convention. Thus slice weak continuity in the published proof cannot be silently upgraded to total-variation continuity.

## Proof of the model and Borel claims

1. Each \(u_j\) is the maximum of three psh functions (the third constant), is globally bounded on the chosen product, and is continuous. For fixed \(z\),
\[
u_j(x,z)=\max\{\log|x_j|^2,\log R(z)^2\}.
\]
Its planar Laplacian vanishes off the circle \(|x_j|=R(z)\), since it is constant inside and logarithmically harmonic outside. The outward radial derivative jumps from \(0\) to \(2/R(z)\). As \(\mathrm{dd}^{\mathrm c}v=(\Delta v)/(4\pi)\,dA\) on \(\mathbb C\), the jump contributes precisely \(ds/(2\pi R(z))=\lambda_{R(z)}\). There is **no** mass at \(x_j=0\), because the potential is constant near that point. Wedge products in the independent \(x_j\) variables give the first equality (B).

2. To verify the second equality (B) **without assuming Lemma 13.4.5**, take the elementary smooth psh approximants
\[
u_{j,k}=\frac1k\log\bigl(|x_j|^{2k}+|z_1|^{2k}+\rho^{2k}\bigr),\qquad k=1,2,\ldots .
\]
These are logarithms of sums of squared moduli of holomorphic functions and one positive constant. The finite \(\ell^k\)-norm inequality implies \(u_{j,k}\downarrow u_j\), with
\(0\le u_{j,k}-u_j\le(\log 3)/k\) **uniformly**. For each \(z\), direct radial differentiation gives
\[
(\mathrm{dd}^{\mathrm c}_{x_j}u_{j,k})(\Delta_s)
=\frac{s^{2k}}{s^{2k}+|z_1|^{2k}+\rho^{2k}}\le1
\quad (0<s<2).
\]
Consequently the smooth fiber measures converge weakly to \(\lambda_{R(z)}\), and their masses on \(\Delta_2\) are uniformly bounded by \(1\). On wedging \(\bigwedge_j\mathrm{dd}^{\mathrm c}u_{j,k}\) with the full base volume form, all differentials involving \(z\) vanish; what remains is exactly the tensor product of the smooth \(x_j\)-fiber measures, integrated over \(z\). For any compactly supported continuous \(h\), ordinary Fubini, weak convergence on each fiber, and the uniform product-mass bound allow dominated convergence. On the left, bounded Bedford–Taylor decreasing continuity (the internally cited Theorem 7.3.7) identifies the limit with \(p_D^*dV_D\wedge M\). Thus equality holds against all \(C_c\) functions, and uniqueness of positive Radon measures extends it to every Borel set and every bounded Borel compactly supported weight. This isolates the only general analytic upstream input; it is **not** a transitive certification of Theorem 7.3.7.

3. On the support of \(M_z\), all \(|x_j|=R(z)\). If \(|z_1|>\rho\), then \(R(z)=|z_1|\) and \(E_=\) contains the entire fiber measure; if \(|z_1|<\rho\), then \(R(z)=\rho>|z_1|\) and \(E_>\) contains it instead. The boundary \(|z_1|=\rho\) has base Lebesgue measure zero. Since \(D=\Delta^m\), the two base volumes are respectively \((1-\rho^2)\pi^m=3\pi^m/4\) and \(\rho^2\pi^m=\pi^m/4\), proving (C).

4. For every \(a\in C_c(Q)\), \(\int a\,dM_z\) is a continuous angular average in \(R(z)\). Thus \(M_{z^{(k)}}\rightharpoonup M_z\) whenever \(z^{(k)}\to z\). If the radii are distinct, the supports \(\{|x_1|=R(z^{(k)})\}\) and \(\{|x_1|=R(z)\}\) are disjoint Borel sets, and both measures are probabilities. Hence they are mutually singular and the TV norm of their difference is exactly \(2\). This proves (D).

## Audit of the *printed* arguments

- **13.4.4, physical lines 145–153:** The proof derives measurability for open \(A\Subset Q\) by increasing compactly supported continuous cutoffs, then uses a finite-on-relatively-compact-sets Dynkin class twice, first in \(Q\), then in \(Q\times D\); it finally exhausts both open factors. The conditional finiteness and the use of Borel sections are essential and present. This review found **no error** in the selected proof passage.
- **13.4.5, physical lines 170–190:** The proof establishes uniform compact fiber mass bounds from bounded psh potentials, first proves smooth/continuous-weight Fubini, then identifies the Borel disintegration **as a Radon measure** and extends to signed smooth top-degree base forms by a local positive/negative decomposition. This is the correct order; the model (C) shows why merely asserting an a.e. density would be inadequate. The scalar fiber integrals are allowed to converge weakly without TV convergence; (D) shows that this distinction cannot be removed.
- **No source correction is required.** An optional, separate reviewable explanatory example after Lemma 13.4.5 could record (A)–(D), but no edit to production text is authorized in this audit. The conditional dependence on general bounded Bedford–Taylor monotone convergence and the internal CLN bound is **unresolved at chain level**, not a defect shown in these lemmas.
- **Affected interfaces:** degree-one non-pluripolar identification in Proposition 13.4.7 (lines 194ff.), and other references using Borel fiber integration. No implication that those full downstream proofs are verified.
- **Scope and novelty:** This is a *renewed, independent proof-level stress test* of 13.4.4 and 13.4.5. The 2026-10-31 report `2026-10-31-pairwise-geodesic-essential-speed.md` **already inspected** these same Borel/Fubini passages and explicitly recorded no new defect; the new contribution here is the moving-circle Borel interface computation and the sharp total-variation discontinuity, not first access to either lemma. This is a **first-degree, moving-log-circle, parameter-disintegration and TV-boundary** check; it is not the existing §7.33 *top-degree separated power-maximum* calculation or a repetition of earlier weak-net counterexamples.
- **Coverage accounting:** §13.4 and §§13.4.4–5 were previously partly visited (including 2026-10-31); this model is a new check, not a new first proof inspection: **0 first-visited numbered sections**, **0 fully certified sections** this session. Current chapter/section inventory remains **25/747**. No build, test suite, CI, deployment, regularization project, or source edit was performed. The user's Demailly approximation/regularization and dedicated Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale/positivity-loss programme remains **deferred-by-user**, neither resumed nor certified.
