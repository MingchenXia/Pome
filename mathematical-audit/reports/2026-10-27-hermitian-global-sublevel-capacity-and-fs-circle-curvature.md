# Selected mathematical audit: a sharp Hermitian global sublevel-capacity bound and circle-supported Fubini–Study curvature

**Date:** 2026-10-27. **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting review head:** ac620c1713fd3da8d846132b457cedd1221a6977.

**Scope:** First direct selected proof-level audit of §§10.6 and 10.9 of the integrated reading edition, not their whole transitive proof systems. No mathematical-body or tag changes. Completely outside the author-deferred Demailly approximation/regularization, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes. Basic local weighted Bedford–Taylor/Chern–Levine–Nirenberg inequalities are used as established conditional inputs, not re-proved.

## 1. POME-HERMITIAN-GLOBAL-SUBLEVEL-CAP-001

**Severity:** low. **Status:** verified conditional deduction; NOT a false theorem or a completed transitive proof certification.

**Integrated anchors:**
- Main <code>docs/sections/global-potentials-and-positive-cohomology-classes--global-poles-on-compact-complex-manifolds/index.html</code>, blob <code>2346c71320d5c7772f9f055cc8b80699edf536a5</code>. Standing assumptions §10.9, lines 7–16; Definition of the global capacity, lines 269–281; Lemma 10.9.3, source <code>foundations-of-pluripotential-theory-E1B7F4E9</code>, permanent tag **40E5831EBB76**, lines 60–115 (especially clauses (2) at 67 and (4) at 73, 106–115); Theorem 10.9.19, source <code>foundations-of-pluripotential-theory-0F43067B</code>, permanent tag **E2AF1B6D37EC**, capacity proof at lines 484–490 and limit argument 492–499.
- Weighted local CLN Theorem 7.4.1, source <code>foundations-of-pluripotential-theory-93A06A12</code>, permanent tag **7C68264563C0**; earlier local sharpness finding POME-BT-PSH-SUBLEVEL-CAP-RATE-001 is NOT repeated as a new finding.
- For the explicit sharpness witness, main <code>docs/sections/global-potentials-and-positive-cohomology-classes--curvature-and-metrics-defined-by-sections/index.html</code>, blob <code>ff56aa13950da3423135bb0bbaf40bcc980c21a1</code>, Example 10.6.7, source <code>foundations-of-pluripotential-theory-E51945FB</code>, permanent tag **4CE1D9D7D803**, lines 108–113; Poincaré–Lelong Proposition 10.6.4, source <code>foundations-of-pluripotential-theory-A8F577E0</code>, permanent tag **95892535D04F**, lines 82–94.

**Statement (additional quantitative corollary).** Let \(X\) be a connected compact complex manifold of positive complex dimension, and let \(\omega\) be a fixed positive Hermitian form, not necessarily closed. For the capacity \(c_\omega\) of §10.9 and every \(u\in\operatorname{PSH}(X,\omega)\) satisfying \(\sup_Xu=0\), one has, for every \(t>0\),
\[
 c_\omega(\{u<-t\})\le \min\{c_\omega(X),C_{X,\omega}/t\}.
\]
The constant is independent of both \(u\) and \(t\). The exponent \(1\) cannot be replaced by a larger exponent, even on \((\mathbb P^1,\omega_{\rm FS})\).

**Proof of the upper bound.** Lemma 10.9.3(4) provides a uniform number \(M\) such that \(\int_X(-u)\omega^n\le M\) for all normalized \(u\); this uses the connected compact manifold hypothesis. Cover \(X\) by finitely many coordinate balls \(B'_a\Subset B_a\), where the smaller balls cover \(X\), and choose compact intermediate sets \(B'_a\Subset L_a\Subset B_a\). Choose a smooth \(h_a\) with \(\mathrm{dd}^ch_a\ge\omega\) on \(B_a\), and let \(H_a\ge\sup_{B_a}h_a\). On \(B_a\), set \(U_a=u+h_a-H_a\). Then \(U_a\) is nonpositive psh, \(-u\le -U_a\), and \(\|U_a\|_{L^1(L_a)}\le M_a\), uniformly in \(u\), since the Hermitian and Lebesgue volume densities are uniformly comparable on compact coordinate sets. For any admissible global capacity test \(0\le v\le1\), \(v\in\operatorname{PSH}(X,\omega)\), set \(W_a=v+h_a\), a uniformly bounded local psh function. Lemma 10.9.3(2) implies \(\omega_v^n\le(\mathrm{dd}^cW_a)^n\). Because \(-u\ge t\) on \(E_t=\{u<-t\}\), positivity and the local weighted CLN estimate give
\[
\begin{split}
 t\int_{E_t\cap B'_a}\omega_v^n
 &\le\int_{B'_a}(-u)\,\omega_v^n\\
 &\le\int_{B'_a}(-U_a)(\mathrm{dd}^cW_a)^n
 \le C_a\|U_a\|_{L^1(L_a)}
 \le C'_a.
\end{split}
\]
Summing over the finite covering and then taking the supremum over \(v\) proves \(c_\omega(E_t)\le C_{X,\omega}/t\). The uniform finite bound \(c_\omega(E_t)\le c_\omega(X)\) is already §10.9, lines 275–281. No weak-convergence or limit interchange is used here.

**Exact sharpness on \(\mathbb P^1\).** Let \(z=Z_1/Z_0\), \(\omega=\mathrm{dd}^c\log(1+|z|^2)\), and
\[
 u(z)=\log\frac{|z|^2}{1+|z|^2}\le0,\qquad
 \sup_{\mathbb P^1}u=0,\qquad \omega+\mathrm{dd}^cu=[0].
\]
For \(t\ge1\) put \(s=t+1\) and \(v_s=1+s^{-1}\max(u,-s)\). This is an admissible capacity test: \(0\le v_s\le1\), and \(\omega+\mathrm{dd}^cv_s=(1-s^{-1})\omega+s^{-1}(\omega+\mathrm{dd}^c\max(u,-s))\ge0\). The circle
\[
 C_s=\{u=-s\}=\{|z|=r_s\},\qquad r_s^2=(e^s-1)^{-1},
\]
lies strictly inside \(E_t\). The radial derivative of \(u\) is \(u'(r)=2/[r(1+r^2)]\), so its outward flux at \(C_s\), normalized by \(\mathrm{dd}^c=\frac{i}{2\pi}\partial\bar\partial=\frac1{4\pi}\Delta\,dA\) in complex dimension one, equals
\[
 \frac12 r_su'(r_s)=\frac1{1+r_s^2}=1-e^{-s}.
\]
Hence \(\omega_{v_s}\) has circle atom \(s^{-1}(1-e^{-s})\), giving
\[
 c_{\omega_{\rm FS}}(\{u<-t\})\ge \frac{1-e^{-(t+1)}}{t+1},\qquad t\ge1.
\]
Thus the universal \(O(t^{-1})\) order is sharp. This is a **global compact-Hermitian** estimate with a universal normalized \(L^1\) bound, not a duplicate of the previously established local fixed-\(V\) capacity rate.

**Dependency and action:** Conditional on the printed Lemma 10.9.3(2),(4), weighted CLN §7.4.1 and the specified normalization of \(\mathrm{dd}^c\). Optional corollary after the global capacity definition or after §10.9.19. Relevant to global pluripolar capacity and normalized compactness; not a claim that local capacities and global capacities agree. Reviewed selected proof segments in Lemma 10.9.13 (lines 290–301), Proposition 10.9.16 (372–442), and Theorem 10.9.19's capacity/limit steps (484–499): no new confirmed error. Elementary convolution at lines 458–468 is NOT independently re-audited, and no author-deferred regularization programme was opened.

## 2. POME-FS-MAX-CIRCLE-CURVATURE-001

**Severity:** low. **Status:** verified conditional deduction; NOT a false theorem or a genuine duplicate.

**Integrated anchors:** Main <code>docs/sections/global-potentials-and-positive-cohomology-classes--curvature-and-metrics-defined-by-sections/index.html</code>, blob <code>ff56aa13950da3423135bb0bbaf40bcc980c21a1</code>; Example 10.6.6, source <code>foundations-of-pluripotential-theory-6BEA6500</code>, permanent tag **01B4AD44BAC3**, lines 98–105; Example 10.6.7, tag **4CE1D9D7D803**, lines 108–113; Definition 10.6.8, source <code>foundations-of-pluripotential-theory-058B5289</code>, tag **9CC891317C85**, lines 117–123; Proposition 10.6.9, source <code>foundations-of-pluripotential-theory-869166DD</code>, tag **E5F620306821**, lines 126–142; Poincaré–Lelong Proposition 10.6.4, tag **95892535D04F**, lines 82–94.

**Statement (explicit example clarifying two kinds of regularity).** A metric belonging to \(\mathrm{FS}(\mathcal O_{\mathbb P^1}(1))\) can have **no poles and bounded (indeed continuous) local weights**, hence analytic singularity type with the trivial ideal, while its positive Chern current is purely singular, supported by a real circle, not an analytic divisor.

**Proof.** With \(h_0=h_{\rm FS}\) and homogeneous coordinate sections \(X_0,X_1\) take \(m=1\), \(N=2\), \(\lambda_i=0\) in Definition 10.6.8, so \(h=h_0e^{-\varphi}\), where
\[
 \varphi=\max\{\log|X_0|_{h_0}^2,\log|X_1|_{h_0}^2\}.
\]
These sections have no common zero; their maximum is bounded on compact \(\mathbb P^1\), and therefore \(\varphi\) is continuous and everywhere finite. On the chart \(Z_0\ne0\) in the holomorphic frame \(X_0\), the metric's local weight is exactly
\[
 -\log |X_0|_h^2
 =\log(1+|z|^2)+\max\{-\log(1+|z|^2),\,\log|z|^2-\log(1+|z|^2)\}
 =\max\{0,\log|z|^2\}.
\]
It is harmonic for \(|z|<1\) and for \(|z|>1\), with a jump in the radial first derivative from \(0\) to \(2/r\) at \(r=1\). Consequently
\[
 c_1(\mathcal O(1),h)
 =\mathrm{dd}^c\max(0,\log|z|^2)
 =\frac{d\theta}{2\pi}\quad\text{on }|z|=1,
\]
and is zero off that circle. Indeed \(\Delta\max(0,2\log r)=2\,\delta_{r=1}\) as a radial distribution, hence \((1/4\pi)\Delta f\,dA=d\theta/(2\pi)\). Its total mass is \(1\), matching \(\int_{\mathbb P^1}c_1(\mathcal O(1))=1\). The support circle is real one-dimensional, not a complex analytic divisor in a Riemann surface. Thus analytic **singularity type** does not imply smooth or analytically supported **curvature measure**; this does not contradict Proposition 10.6.9.

**Dependency and action:** Uses the integrated finite-maximum metric definition, line-bundle local curvature convention and the explicitly checked radial distribution calculation. Suggest an optional worked example after Proposition 10.6.9, distinct from the smooth classical Fubini–Study metric in Example 10.6.7. Affects interpretation of Fubini–Study max metrics, singular curvature and later section-envelope constructions. Supporting selected proofs: Lemma 10.6.1 local frames (20–31), Lemma 10.6.2 compact-section normality/finite-dimensionality (39–66), Proposition 10.6.4 (82–94) and Proposition 10.6.9 (126–142); no other confirmed error in these passages. Section 10.7 (Bergman) and §10.8 (extension estimates) were **not** opened.

## Actual coverage and unchanged obligations

Two previously inventory-only ToC rows, **§§10.6 and 10.9**, now have the selected proof/statement review detailed above. The existing **747 unique current section identifiers** and the previous coverage statuses are preserved; neither section is certified in full, and historical source labels, permanent tags and attribution remain unchanged. No theorem in this selected scope was found false. The global capacity proof uses known internal results conditionally; §10.9.19's other hard steps remain for future nonexcluded audit. This run did not perform a project build, software tests, CI, formal verification or website publication. All author-deferred Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss entries remain **deferred-by-user**, neither repaired nor certified.
