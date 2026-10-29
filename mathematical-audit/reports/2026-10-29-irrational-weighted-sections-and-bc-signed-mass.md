# Irrational weighted section algebras and fixed-class signed-current mass

**Date:** 2026-10-29. **Production main audited:** <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code>. **Starting review head:** <code>948d02eaf49b69a442ccebf82b4312c0a813b0f8</code>.

**Scope:** The integrated reading edition was inspected directly. This pass covers selected passages of §§19.8.8–11 and 10.11.1–2, the precise internal representative dependence in §20.4.20, and navigation-only subject headers §§10.10 and 5.59. It certifies no entire numbered section or dependency chain. Neither result reopens the excluded Demailly approximation/regularization, Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss proof-completion programme.

## POME-CURVE-BOUNDED-SECTION-FG-RATIONAL-001

**Severity:** low. **Status:** verified conditional deduction, **not** a false original theorem, complete repair, or new external dependency.

**Exact integrated anchors:** <code>docs/sections/holomorphic-sections-and-hermitian-mass/index.html</code>, blob <code>5f00431e7986d899dc833c89175686b75f09371d</code>. The bounded weighted section spaces are defined at physical lines 236–248 in §19.8.8 (section tag <code>C9CFDB0867F5</code>, source <code>non-kahler-pluripotential-theory:DE44B21C</code>). The curve computation is Theorem 19.8.11 (permanent tag <code>1E6D5AA611CC</code>, source <code>non-kahler-pluripotential-theory:CB9DFB6A</code>), physical lines 253–288, especially 267–285. Example 19.8.9, tag <code>D1A2270A67A3</code>, lines 220–233, distinguishes integrable from bounded weighted spaces.

**Claim proved here.** Let \(X=\mathbb P^1\), \(L=\mathcal O_{\mathbb P^1}(1)\), \(h=h_{\mathrm{FS}}\), \(\beta=c_1(L,h)\), and, in the affine coordinate \(z=X/Y\), put
\[
u_c(z)=c\log\frac{|z|^2}{1+|z|^2},\qquad 0<c<1.
\]
This is globally defined, with \(\beta+\mathrm{dd}^{\mathrm c}u_c=(1-c)\beta+c[0]\geq0\), using Pome's convention \(\mathrm{dd}^{\mathrm c}=\frac{i}{2\pi}\partial\bar\partial\). For \(m\geq1\), define \(\mathcal H_m(u_c)\) using integrability of \(|s|^2_{h^m}e^{-mu_c}\), and \(\mathcal W_m(u_c)\) using its boundedness away from the pole. Then
\[
h^0(\mathcal H_m)=m-\lfloor mc\rfloor+1,\qquad
h^0(\mathcal W_m)=m-\lceil mc\rceil+1.
\]
Thus the dimension gap is exactly \(1\) if \(mc\notin\mathbb Z\), and \(0\) otherwise. More significantly, the graded algebra
\[
R_c=\bigoplus_{m\geq0}\mathcal W_m(u_c)
\]
is **finitely generated over \(\mathbb C\) if and only if \(c\in\mathbb Q\)**. Consequently an irrational logarithmic weight gives a positively curved current and a graded algebra with linear Hilbert growth \((1-c)m+O(1)\), yet the algebra is not Noetherian.

**Complete direct proof.** In homogeneous coordinates \([X:Y]\), the degree-\(m\) monomials \(X^kY^{m-k}\), \(0\leq k\leq m\), have vanishing order \(k\) at \([0:1]\). In a nonvanishing local frame near that point, the weighted squared norm of an order-\(k\) section is comparable to \(|z|^{2(k-mc)}\). Area integrability is equivalent to \(k-mc>-1\), i.e. \(k\geq\lfloor mc\rfloor\), whereas boundedness is equivalent to \(k-mc\geq0\), i.e. \(k\geq\lceil mc\rceil\). This proves both exact dimension formulas without invoking a global asymptotic theorem.

The algebra \(R_c\) has monomial exponent semigroup
\[
S_c=\{(m,k)\in\mathbb Z_{\geq0}^2: cm\leq k\leq m\}.
\]
If \(c=p/q\) in lowest terms, \(0<p<q\), the cone of \(S_c\) is spanned by the **integral** rays \(v=(q,p)\) and \(w=(1,1)\). For any lattice point \(s=av+bw\) of the cone with \(a,b\geq0\), subtract \(\lfloor a\rfloor v+\lfloor b\rfloor w\). The residual is an integer point in the bounded half-open parallelogram \(\{a'v+b'w:0\leq a',b'<1\}\) and remains in \(S_c\). There are only finitely many such residual points. Together with \(v,w\), they generate \(S_c\), and the corresponding monomials generate \(R_c\).

Conversely, assume \(c\) irrational and \(R_c\) finitely generated. By taking homogeneous components of a finite collection of algebra generators, we may assume each generator is homogeneous of a positive degree \(m_j\). Its vanishing order \(k_j\) at \([0:1]\) satisfies \(k_j\geq\lceil c m_j\rceil>cm_j\). Hence one \(\delta>0\) satisfies \(k_j\geq(c+\delta)m_j\) for all generators. Valuations add under products and cannot decrease under sums, so every degree-\(m\) element of the generated algebra has vanishing order at least \((c+\delta)m\). But the monomial \(X^{\lceil cm\rceil}Y^{m-\lceil cm\rceil}\in\mathcal W_m\) has vanishing-order ratio \(\lceil cm\rceil/m\to c\), a contradiction. This proves the equivalence.

**Correction / dependents:** Theorem 19.8.11 and its rounding conventions are correct. An optional remark after §19.8.11 can record the exact periodic/aperiodic dimension gap and rationality criterion for finite generation. The distinction matters to the use of bounded weighted graded algebras in §19.9 (algebraic flags/Okounkov semigroups): positivity and leading Hilbert growth alone do **not** give finite generation. No assertion is made about the general non-Archimedean finite-generation programme. The proof uses only the displayed weight, the local integral test and lattice arithmetic; no excluded analytic proof is needed.

## POME-BC-FIXED-CLASS-SIGNED-MASS-001

**Severity:** low. **Status:** verified conditional deduction (sharpness countermodel to a **hypothesis deletion**, not a counterexample to the printed results).

**Exact integrated anchors:** <code>docs/sections/bott-chern-classes-and-singular-loci--closed-classes-with-hermitian-lower-bounds/index.html</code>, blob <code>cee2450e039f1efe8c32083ee516fdc67737249a</code>, §10.11.1 tag <code>7F12058085DC</code>, source <code>non-kahler-pluripotential-theory:4FDF9D6A</code>, physical lines 13–33; §10.11.2 tag <code>A8D846A01D78</code>, source <code>non-kahler-pluripotential-theory:8278956A</code>, physical lines 37–56. The canonical representative/potential statement being cross-checked is §20.4.20, tag <code>721E66DF8C88</code>, source <code>non-kahler-pluripotential-theory:281A4711</code>, <code>docs/sections/divisorial-currents-on-compact-modifications/index.html</code>, blob <code>79d6e21f9d3784bf3761846f77f90ad075253644</code>, physical lines 381–428.

**Model and complete proof.** Normalize the Fubini–Study form \(\gamma\) on \(\mathbb P^1\) so that \(\int_{\mathbb P^1}\gamma=1\). Set \(\phi([X:Y])=|X|^2/(|X|^2+|Y|^2)\). This is a smooth, real, nonconstant function, so \(\mathrm{dd}^{\mathrm c}\phi\not\equiv0\): on a compact connected Riemann surface a globally harmonic function is constant. For real \(t>0\) put
\[
T_t=\gamma+t\,\mathrm{dd}^{\mathrm c}\phi.
\]
Each \(T_t\) is a smooth **closed signed** real \((1,1)\)-current in the *same* Bott–Chern class \([\gamma]\), and Stokes gives \(\int_{\mathbb P^1}T_t=1\), independently of \(t\). Nevertheless the triangle inequality for signed measures gives the quantitative lower bound
\[
\|T_t\|_{\mathrm{TV}}\ \geq\ t\|\mathrm{dd}^{\mathrm c}\phi\|_{\mathrm{TV}}-1
\longrightarrow+\infty.
\]
Indeed \(\mathrm{dd}^{\mathrm c}\phi=f\gamma\) for a smooth real nonzero function \(f\) of integral zero, hence \(f\) changes sign. Consequently \(T_t=(1+tf)\gamma\) has no uniform lower bound \(T_t\geq-\varepsilon\gamma\) as \(t\to\infty\). This pinpoints why the lower-curvature hypothesis in §10.11.1 is indispensable: fixing the class and even its *exact* Gauduchon trace cannot replace it.

The normalized decomposition of §20.4.20 is explicit in this model:
\[
B_\gamma(T_t)=\gamma,\qquad
v_\gamma(T_t)=t\bigl(\phi-\int_{\mathbb P^1}\phi\,\gamma\bigr).
\]
Its \(L^1\) norm also grows exactly linearly in \(t\). Hence the estimate (20.4.21), which is stated on the **positive cone**, must not be applied to arbitrary signed representatives of a fixed class. This is consistent with, rather than a refutation of, the compact mass-one *pseudoeffective class* slice in Proposition 10.11.2: all classes \([T_t]\) coincide; it is the uncontrolled representatives that diverge.

**Correction / dependents:** Both printed propositions 10.11.1–2 and Lemma 20.4.20 remain correct. An optional short example after §10.11.1 could distinguish fixed cohomological trace from bounded total variation without a common negative bound. Relevant dependents: positive-current compactness §10.11.2, canonical smooth representative and potential bounds §20.4.20, and the mass estimates for modifications §20.4.22. The only general inputs to the internal proof comparison are the printed Gauduchon-trace Stokes identity and the normalized representative lemma; they are not globally recertified here.

## Coverage and restrictions

- **First orientation only:** §10.10 (<code>docs/sections/bott-chern-classes-and-singular-loci/index.html</code>, tag <code>26958A01D807</code>) has introductory prose and no theorem/proof environment; §5.59 (<code>docs/sections/positive-current-extension-and-analytic-integration/index.html</code>, tag <code>071D71F4F5CE</code>) is a navigation-only subject header. Neither counts as a mathematical section proof audit.
- **Actual newly checked mathematical content:** §19.8.8–11's local vanishing thresholds and the two section spaces, with a new exact finite-generation characterization; incremental §10.11.1–2 signed-current hypothesis stress test; §20.4.20 representative formula checked in the explicit one-dimensional model only. No claim to have reviewed the rest of §§19.8, 10.11 or 20.4, or the upstream general current-cohomology framework.
- **Inventory remains:** 25 chapters; 747 distinct numbered ToC sections; zero entire sections certified. Existing confirmed errors, unresolved gaps, conditional repairs and all author-deferred entries remain in their previous states.
- **Prohibited/deferred:** dedicated Demailly approximation/regularization, Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes remain **deferred-by-user**, neither reopened nor resolved. Reading §19.8's elementary curve section-count computation does not audit any partial Bergman kernel theorem.
- **No changes** to production main, reading-edition mathematics, source repositories, registered proofs, canonicalization, permanent tags, website or GitHub Actions. No tests, builds, CI or formal proofs were run.