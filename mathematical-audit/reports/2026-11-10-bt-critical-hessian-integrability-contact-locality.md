# 2026-11-10 — critical mixed Sobolev Hessians and Bedford–Taylor contact locality

**Finding ID:** `POME-BT-CRITICAL-LN-HESSIAN-CONTACT-001`. **Severity:** low. **Status:** verified conditional deduction (new extension under explicitly stronger Sobolev integrability, conditional only on the named, internally printed Bedford–Taylor continuity theorem). **Printed mathematical error:** none established. **Production main examined:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Working branch:** `review/mathematical-audit`.

## Pinned integrated statements and scope

- `docs/sections/bedford-taylor-products-and-local-capacity--bounded-complex-hessians-and-contact-sets/index.html` at production-main blob `e2697dc465a2b639120974188eaeb6c446ed8071`. Main statement: Proposition **7.13.4**, source `foundations-of-pluripotential-theory:D9CC767A`, permanent tag `1466731348C1`, physical lines **109–133** (mixed-discriminant normalization, mollification, contact restriction). Supporting Proposition **7.13.3**, source `foundations-of-pluripotential-theory:AF82FB9E`, tag `C006456D2AFC`, lines **91–101**, and Lemma **7.13.1**, source `foundations-of-pluripotential-theory:B80A5A22`, tag `8736729F21D9`, lines **14–42** (Sobolev locality). Lemma **7.13.2**, source `foundations-of-pluripotential-theory:0CFF4F56`, tag `D57C89462C1B`, lines **48–82**, supplies an alternative sufficient W²,¹ input when an L² Laplacian is known. The original proposition assumes bounded complex Hessians; the extension below does **not** attribute a stronger claim to it.
- `docs/sections/bedford-taylor-products-and-local-capacity--bounded-potentials-and-recursive-products/index.html`, blob `18bd2395f3b76941b2c677079c09eb6accc5a9cb`. Proposition **7.2.6**, source `foundations-of-pluripotential-theory:C5608495`, permanent tag `2F39A3F97E8E`, lines **125–154**, supplies the exact locally uniform continuity of products used below; this earlier theorem's full dependency graph is **not** newly certified here.
- `docs/sections/envelopes-and-model-potentials--measures-on-contact-sets/index.html`, blob `c3be9349468d2203c0b67f4bee2be49d1392f8ff`, lines **7–20**, is only a contextual statement of subsequent contact-set applications, not an examination of their full proofs.

## New conditional theorem (unbounded Hessians allowed)

Let \(n\ge1\), \(\Omega\subset\mathbb C^n\) open, and let \(p_1,\ldots,p_n\) be **finite** exponents in \([1,\infty)\) such that
\[
\sum_{j=1}^n\frac1{p_j}\le1.
\]
Suppose each \(u_j\in C(\Omega)\cap\mathrm{PSH}(\Omega)\cap W^{2,p_j}_{\mathrm{loc}}(\Omega;\mathbb R)\), and let \(A_j=((u_j)_{a\bar b})\in L^{p_j}_{\mathrm{loc}}\) be its weak complex Hessian matrix. Then the Bedford–Taylor mixed product is **absolutely continuous**, with the same normalization as the printed bounded-Hessian proposition:
\[
dd^c u_1\wedge\cdots\wedge dd^c u_n
=\frac{n!}{\pi^n}D(A_1,\ldots,A_n)\,dV_{2n}.\tag{1}
\]
In particular \(D(A_1,\ldots,A_n)\in L^1_{\mathrm{loc}}\), even though the entries of the individual Hessians need not be locally bounded. The symmetric critical case \(p_1=\cdots=p_n=n\) is included, for **all** complex dimensions, with \(W^{2,1}\) in complex dimension one.

More generally let \(v_j\in W^{2,1}_{\mathrm{loc}}(\Omega;\mathbb R)\), with weak complex Hessians \(B_j\) and arbitrary Borel representatives, and set \(E=\bigcap_j\{u_j=v_j\}\). Then the contact-set identity
\[
\mathbf1_E\,dd^c u_1\wedge\cdots\wedge dd^c u_n
=\frac{n!}{\pi^n}\mathbf1_E D(B_1,\ldots,B_n)\,dV_{2n}\tag{2}
\]
holds; its right-hand density is locally integrable **after restriction to \(E\)**. No global \(L^1\) bound for \(D(B_1,\ldots,B_n)\) off \(E\) is claimed. If the \(v_j\) are themselves continuous psh, this still does not authorize restricting weak limits to an arbitrary fixed contact set.

## Proof, including the quantitative convergence bound

Fix \(U\Subset V\Subset\Omega\) with \(U\) relatively compact open and \(V\) a compactly buffered neighborhood. For all sufficiently small \(\varepsilon>0\), convolution with a nonnegative radial mollifier defines smooth psh \(u_{j,\varepsilon}\) on a neighborhood of \(\overline U\). Continuity of \(u_j\) gives \(u_{j,\varepsilon}\to u_j\) **uniformly on compact sets**; Sobolev convolution gives \(A_{j,\varepsilon}=A_j*\rho_\varepsilon\to A_j\) strongly in \(L^{p_j}(U)\). Thus \(\sup_\varepsilon\|A_{j,\varepsilon}\|_{L^{p_j}(U)}<\infty\).

The mixed discriminant \(D\) of Hermitian \(n\times n\) matrices is an \(n\)-linear polynomial, so, with any fixed matrix norm, \(|D(M_1,\ldots,M_n)|\le C_n\prod_i|M_i|\). Telescoping the difference of two mixed discriminants, using the generalized Hölder inequality and the finite volume of \(U\), yields
\[
\begin{aligned}
&\|D(A_{1,\varepsilon},\ldots,A_{n,\varepsilon})-D(A_1,\ldots,A_n)\|_{L^1(U)}\\
&\quad\le C_n|U|^{1-\sum_i1/p_i}\sum_{j=1}^n
\|A_{j,\varepsilon}-A_j\|_{L^{p_j}(U)}
\prod_{i\ne j}\max\{\|A_{i,\varepsilon}\|_{L^{p_i}(U)},\|A_i\|_{L^{p_i}(U)}\}
\longrightarrow0.\tag{3}
\end{aligned}
\]
The estimate is valid even when \(p_j=1\) (in that case the hypothesis forces all other factors to be absent, since exponents are finite). By the smooth polarization computation in the integrated Proposition 7.13.4 (lines 122–129), the mixed product of the smooth convolutions equals \((n!/\pi^n)D(A_{1,\varepsilon},\ldots,A_{n,\varepsilon})dV_{2n}\). On the other hand, the **locally uniform** convergence and the exact hypotheses of integrated Proposition 7.2.6 identify their weak limit with the mixed Bedford–Taylor product of the \(u_j\). The \(L^1_{\mathrm{loc}}\) convergence in (3) identifies the same weak limit with the right side of (1), proving (1) without interchanging an unjustified pointwise limit and a current product.

Since \(p_j\ge1\), each \(u_j\in W^{2,1}_{\mathrm{loc}}\). Apply the actual Proposition 7.13.3 to \(u_j-v_j\): \(A_j=B_j\) almost everywhere on \(\{u_j=v_j\}\), hence simultaneously on \(E\), with only a finite union of exceptional null sets. Multilinearity of \(D\) gives \(\mathbf1_ED(B_1,\ldots,B_n)=\mathbf1_ED(A_1,\ldots,A_n)\) almost everywhere. This is locally \(L^1\) by (3) and proves (2). Borel choices of Sobolev representatives alter the equality sets only on negligible sets and do not change the restricted absolutely continuous measure. **There is no invocation of Demailly regularization, global Bergman/L²/OT estimates, or the excluded positivity-loss programme.**

For a direct normalization check at \(n=2\), put \(u_1=|z_1|^2\), \(u_2=|z_2|^2\). Then \(D(\mathrm{diag}(1,0),\mathrm{diag}(0,1))=1/2\), so \((2!/\pi^2)D=1/\pi^2\), the product of \(dd^c|z_j|^2=dx_j\wedge dy_j/\pi\). This rules out an accidental extra \(n!\).

## Genuine strict extension, not a restatement of bounded Hessians

On a polydisc, choose \(0<\alpha<\min\{1,2/n\}\) and
\[
u_1(z)=|z_1|^{2-\alpha},\qquad
u_j(z)=|z_j|^2\ (2\le j\le n).
\]
All are continuous psh; their real weak second derivatives are locally in \(L^n\) because \(\int_{|z_1|<1}|z_1|^{-\alpha n}dx_1dy_1<\infty\) exactly when \(\alpha n<2\). Yet the complex Hessian of \(u_1\) is unbounded along \(z_1=0\). With the normalization \(dd^c=(i/2\pi)\partial\bar\partial\), an ordinary radial derivative calculation gives the **exact**, nonzero and locally integrable measure
\[
dd^c u_1\wedge\cdots\wedge dd^c u_n
=\frac{(2-\alpha)^2}{4\pi^n}|z_1|^{-\alpha}\,dV_{2n}.\tag{4}
\]
For \(n=1\), the empty product convention applies. Equation (4) verifies that the new condition is strictly weaker than the printed bounded-complex-Hessian condition. No claimed optimality for the exponent constraint \(\sum_i1/p_i\le1\): it is a **sufficient** Hölder criterion, not asserted necessary.

## Audit classification and correction direction

**Low / verified conditional deduction**, not a confirmed error, proof-gap certification, or complete-section review. Equation (1) is a short, self-contained \(L^p\) estimate on top of the stated internal Bedford–Taylor continuity result. Equation (2) uses the internally printed real Sobolev locality theorem. Both are already stated with their precise scope; the entire dependency graph of Proposition 7.2.6 is not recertified here.

**Suggested source-body change, not applied:** an optional corollary following Proposition 7.13.4 may state the finite mixed-exponent criterion and contact-set density with the \(L^1\) (rather than \(L^\infty\)) conclusion. In downstream §§16.10 and 16.13 this can only replace the original bound when the **actual** contact potentials possess the stated local Sobolev regularity; no such regularity is inferred for arbitrary envelopes. The already recorded `POME-BT-CONTACT-CUTOFF-NONCOMMUTATION-001` concerns a **singular measure on a contact hypersurface** and failure of restricted weak convergence; it is distinct and remains unchanged. Historical attributions, all permanent tags, canonicalization and prior findings remain unchanged. User-excluded Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof work stay `deferred-by-user`.

**Actual coverage:** new proof-level strengthening of §7.13.4, selected rechecking §7.13.3, contextual reading §7.2.6 and §16.10 overview; all previously sampled in the existing audit; **0 first numbered-section visits, 0 complete mathematical-section certifications**. Current production ToC remains **25 chapters / 747 numbered sections**. No project build, software test, CI, source editing, formalization or site publication was performed.
