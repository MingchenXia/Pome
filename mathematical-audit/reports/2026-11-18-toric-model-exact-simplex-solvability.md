# 2026-11-18 — Exact translated-simplex criterion for toric envelope solvability

**Finding:** \`POME-TORIC-MODEL-SIMPLEX-SOLVABILITY-IFF-001\`  
**Classification:** low / **verified conditional deduction**. The printed Lemmas 11.43.2 and 11.43.3 are **not refuted**. The finding supplies the *necessary* half missing from the printed sufficient translated-simplex test; it does not constitute certification of the entire chapter or its transitive dependencies.

## Reproducible source anchors and limits

- Reviewed \`main\` commit: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
- Integrated text: \`docs/sections/normalization-and-weak-adjoint-measures--convex-body-criteria-for-varying-references/index.html\`, blob \`22591682db1e501e5359d120ed21606e25c5aba0\`.
- §11.43 preliminary definitions of \(\Sigma,L,\ell,h_K,g_K\), physical lines 10–26; Lemma 11.43.2, source \`non-kahler-pluripotential-theory:124461E4\`, permanent tag \`832F0D3BF7D6\`, statement lines 29–34 and proof lines 37–63. The displayed \(c\omega_{\rm FS}\)-psh divisor identity is lines 56–62.
- §11.43.3, source \`non-kahler-pluripotential-theory:01453428\`, permanent tag \`59D09F5BD0FB\`, statement lines 70–76 and context lines 79–96 (not a complete audit of that lemma).
- Chapter/section census freshly matched \`docs/chapters/index.html\`, blob \`c0c07abf4d8f7575b54cff2ec694fcf987f51cf8\`: 25 chapters, 747 distinct section links.
- Direct scope: the *full statement, proof, and scaling hypothesis* of Lemma 11.43.2, plus definitions and the indicated §11.43.3 cross-reference. The remaining parts of §11.43 and their upstream chains have **not** been certified.

## Exact theorem (additional deduction)

Let \(n\ge2\), \(\omega=\omega_{\rm FS}\) on \(\mathbf P^n\), and
\[
\Sigma=\{p\in\mathbf R^n:p_i\ge0,\ \sum_i p_i\le1\},\quad
L(x)=\log(1+\sum_i e^{x_i}).
\]
Let \(K\subset\Sigma\) be a compact convex body with nonempty interior. Write
\[
\ell(p)=\sum_i p_i\log p_i+(1-\sum_i p_i)\log(1-\sum_i p_i),\qquad
g_K(x)=\sup_{p\in K}\bigl(p\cdot x-\ell(p)\bigr)
\]
with \(0\log0=0\), and let \(\Phi_K\in\operatorname{PSH}(\mathbf P^n,\omega)\) be the toric extension of \(g_K-L\) constructed in Lemma 11.43.2. For every \(0\le c\le1\), put \(\delta=1-c\). Then
\[
\boxed{\quad
P_{c\omega}(\Phi_K)\not\equiv-\infty
\quad\Longleftrightarrow\quad
\exists p\in\mathbf R^n:\ p+\delta\Sigma\subset K.
\quad}
\tag{*}
\]
Here \(P_{c\omega}(\Phi_K)\) is the upper-semicontinuously regularized supremum of all \(c\omega\)-psh functions bounded above by \(\Phi_K\); nontriviality means that at least one such competitor exists.

Consequently, with the **attained** translated-simplex inradius
\[
\delta_*(K)=\max\{\delta\in[0,1]:\exists p,\ p+\delta\Sigma\subset K\},
\]
the exact critical background factor is \(c_{\rm crit}(K)=1-\delta_*(K)\), and solvability is equivalent to \(c\ge c_{\rm crit}(K)\). Since \(K\) has interior, \(\delta_*(K)>0\). For the explicit family \(K=t\Sigma\), \(0<t\le1\), one has
\[
\delta_*(t\Sigma)=t,\qquad
P_{c\omega}(\Phi_{t\Sigma})\not\equiv-\infty
\ \Longleftrightarrow\ c\ge1-t.
\tag{**}
\]
Thus the printed sufficient inclusion is also **necessary** for these toric references; the threshold is sharp.

## Proof

**Preliminaries.** The toric rotation group preserves \(\omega\) and \(\Phi_K\). The upper envelope, when nontrivial, is therefore rotation invariant. A rotation-invariant \(c\omega\)-psh function \(v\) has on the dense torus \(T=(\mathbf C^*)^n\) a finite convex representative
\[
F(x)=v(x)+cL(x),\qquad x_i=\log|Z_i/Z_0|^2.
\]
This follows directly from the distributional \(dd^c\)-positivity along the logarithmic modulus coordinates: the real Hessian of \(F\) is positive semidefinite; local integrability excludes the identically \(-\infty\) case and gives a finite continuous convex representative on all of \(\mathbf R^n\). A finite convex function has a subgradient at every point (supporting-hyperplane theorem for its epigraph). These are elementary convex/psh facts, not a Demailly approximation input.

**Necessity.** Suppose \(v=P_{c\omega}(\Phi_K)\not\equiv-\infty\), and fix a point \(x_0\in\mathbf R^n\) and any \(p\in\partial F(x_0)\). The obstacle inequality \(v\le\Phi_K=g_K-L\) on \(T\) yields
\[
F(x)\le g_K(x)-\delta L(x).
\]
For every \(d\in\mathbf R^n\) and \(s>0\), convexity gives
\[
F(x_0)+s\,p\cdot d
 \le F(x_0+sd)
 \le g_K(x_0+sd)-\delta L(x_0+sd).
\]
The boundedness of \(\ell\) on the compact simplex and the definition of \(g_K\) imply
\[
\lim_{s\to\infty}s^{-1}g_K(x_0+sd)=h_K(d),
\]
where \(h_K(d)=\max_{q\in K}q\cdot d\). Likewise
\(\lim_{s\to\infty}s^{-1}L(x_0+sd)
=\max(0,d_1,\ldots,d_n)=h_\Sigma(d)\).
Dividing by \(s\) and taking limits gives, for **every** direction \(d\),
\[
p\cdot d+\delta h_\Sigma(d)\le h_K(d).
\]
The left side is precisely \(h_{p+\delta\Sigma}(d)\). The elementary separating-hyperplane characterization of compact convex sets now gives \(p+\delta\Sigma\subset K\). This proves necessity without any limit interchange, compactness of nets, or regularization.

**Sufficiency.** Suppose \(p+\delta\Sigma\subset K\subset\Sigma\). Inclusion of its vertices forces \(p_i\ge0\) and \(\sum_i p_i+\delta\le1\), hence \(\sum_i p_i\le c\). Define on \(T\)
\[
\chi(x)=p\cdot x-cL(x).
\]
The divisor Poincaré–Lelong calculation, with the project's normalization \(dd^c=i\partial\bar\partial/(2\pi)\), gives the globally defined positive current
\[
c\omega+dd^c\chi
=\sum_{i=1}^{n}p_i[Z_i=0]
 +(c-\sum_i p_i)[Z_0=0]\ge0.
\]
Thus \(\chi\) is \(c\omega\)-psh. Because \(g_K\ge h_K\ge p\cdot x+\delta h_\Sigma(x)\) and \(0\le L-h_\Sigma\le\log(n+1)\),
\[
\chi-\delta\log(n+1)
\le g_K-L=\Phi_K
\quad\text{on }T,
\]
and the inequality extends to the global upper-semicontinuous representatives. Hence \(\chi-\delta\log(n+1)\) is a nontrivial competitor. This proves (*). It reproduces the *sufficiency* step already in printed Lemma 11.43.2, and adds the separate necessity argument above.

**Critical factor and sharp family.** Compactness of \(K\subset\Sigma\) bounds any admissible translation \(p\) and \(\delta\in[0,1]\); the inclusion condition is closed, so its maximum is attained. The set of admissible \(\delta\) is an interval starting at zero. A small translate of \(\delta\Sigma\) fits inside a Euclidean ball contained in \(\operatorname{int}K\), proving positivity. For \(K=t\Sigma\), every translated \(\delta\Sigma\subset t\Sigma\) has coordinate width \(\delta\), whereas \(t\Sigma\) has coordinate width \(t\), so \(\delta\le t\); the inclusion \(0+t\Sigma\subset t\Sigma\) attains equality. This proves (**).

## Classification, dependencies, proposed change

- **Status:** verified conditional deduction; **severity low**. No counterexample to printed Lemma 11.43.2 and **no confirmed source error**. The former theorem provides the sufficient direction; the new item proves necessity and an attained exact threshold.
- **Direct dependencies:** the stated toric extension and model-envelope construction of Lemma 11.43.2; elementary toric positivity, support functions, finite convex subgradients and the divisor identity already used in its proof. Their full transitive proofs were not independently certified.
- **Potential dependents:** §11.43.3's pullback/scaling criterion and the §11.43 continuity theory may cite the exact solvability threshold; such extensions must still be checked with their own hypotheses.
- **Proposed source/body patch, *not applied*:** append the equivalence (*) as a separate corollary to Lemma 11.43.2 and keep its existing proof, tags and attribution intact. Do not conflate the weaker original sufficient condition with an already printed iff assertion.
- **Excluded programme:** user-deferred Demailly regularization/approximation and its Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss completion tracks remain **deferred-by-user**, not resolved/certified and not reviewed here.
- No software build, test, CI, publication, registry, canonicalization, or source/body change is claimed.
