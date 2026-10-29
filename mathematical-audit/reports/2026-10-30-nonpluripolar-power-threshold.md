# Sharp power-logarithmic threshold for locally finite non-pluripolar squares

**2026-10-30. Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Scope:** direct model audit, not entire theorem proof certification.

**Pinned integrated source:** docs/sections/non-pluripolar-products--truncation-and-plurifine-locality/index.html, blob 81be8c5acc360c96bd3c5acba05a3cdb5fafaf4c, Example **13.2.9**, source **foundations-of-pluripotential-theory:2F8E45A2**, permanent tag **6F4C920FEDCA**, physical lines **152–165**. Related non-pluripolar local-finiteness criterion: Lemma **13.2.2**, source **foundations-of-pluripotential-theory:CE1D6DA5**, permanent **D59675D9F6D8**, same file lines **35–52**, Definition **13.2.4** lines **58–63**. Smooth determinant normalization: Eq. **7.2.4**, permanent **706A589A680C**, docs/sections/bedford-taylor-products-and-local-capacity--bounded-potentials-and-recursive-products/index.html, blob **18bd2395f3b76941b2c677079c09eb6accc5a9cb**.

## POME-NPP-POWER-SINGULARITY-THRESHOLD-001

**low / verified conditional deduction.** The original Example 13.2.9 and Lemma 13.2.2 are **correct**. This is a new sharp parameter-family extension, not a false theorem or complete replacement proof. The derivation is elementary conditional on the existing psh extension, bounded Bedford–Taylor locality and smooth determinant formula.

For every real number \(0<a<1\), set
\[
 U_a=\{(x,y)\in\mathbb C^2: |x|^2<1-a,\ |y|<e^{-1}\},\qquad L=-\log|y|,
\]
\[
 u_a(x,y)=(|x|^2-1)L^a\quad(y\ne0),\qquad u_a(x,0)=-\infty.
\]
**Claim:** \(u_a\) is psh; its non-pluripolar square is locally finite **if and only if \(0<a<1/2\)**. The exact printed Example 13.2.9 is the critical member \(a=1/2\).

**Hessian and positivity.** Direct differentiation on \(y\ne0\) gives
\[
 (u_a)_{x\bar x}=L^a,\quad
 (u_a)_{x\bar y}=-\frac{a\bar x}{2\bar y}L^{a-1},\quad
 (u_a)_{y\bar y}=\frac{a(1-a)(1-|x|^2)}{4|y|^2}L^{a-2},
\]
\[
 \boxed{\det((u_a)_{j\bar k})=\frac{a(1-a-|x|^2)}{4|y|^2}L^{2a-2}.}
\]
The leading principal minor and determinant are positive because \(0<a<1\) and \(|x|^2<1-a\). Since \(|x|^2-1<-a\), the function is locally bounded above and tends to \(-\infty\) as \(y\to0\). The standard removable-polar-set psh extension gives precisely the stated axis values; this is the same input as in printed Example 13.2.9.

**Exact non-pluripolar density.** By Eq. 7.2.4, \(dd^c=i(2\pi)^{-1}\partial\bar\partial\) and \((dd^cu)^2=2\pi^{-2}\det(u_{j\bar k})\,dA(x)dA(y)\) for smooth psh \(u\). For a Borel set away from the axis, sufficiently high truncations coincide with \(u_a\), so the non-pluripolar cutoff agrees there with the smooth wedge. The axis is pluripolar and carries zero mass in the cutoff limit. Thus on the finite locus, extended by zero to the axis,
\[
 \boxed{\mu_a=\langle(dd^c u_a)^2\rangle
 =\frac{a}{2\pi^2}\frac{1-a-|x|^2}{|y|^2(-\log|y|)^{2-2a}}\,dA(x)dA(y),}
\]
whether or not \(\mu_a\) is locally finite.

Fix \(0<r<\sqrt{1-a}\), \(0<\rho<e^{-1}\), and \(K_{r,\rho}=\{|x|\le r,\ |y|\le\rho\}\subset U_a\). Then
\[
 \int_{0<|y|\le\rho}\frac{dA(y)}{|y|^2(-\log|y|)^{2-2a}}
 =2\pi\int_{\log(1/\rho)}^\infty t^{2a-2}\,dt,
\]
which converges precisely when \(a<1/2\). In that range, integration over the \(x\)-disk gives the exact formula
\[
 \boxed{\mu_a(K_{r,\rho})=
 \frac{a}{1-2a}\left((1-a)r^2-\frac{r^4}{2}\right)
 \big(\log(1/\rho)\big)^{2a-1}.}
\]
For \(a=1/2\), the inner-cutoff mass grows like \(\log\log(1/\varepsilon)\); for \(a>1/2\), like \((\log(1/\varepsilon))^{2a-1}\). Consequently every neighborhood meeting the axis has infinite limiting trace mass for \(a\ge1/2\), contrary to criterion (13.2.3); for \(a<1/2\), the density is locally integrable, and Lemma 13.2.2 yields the locally finite current. At \(a=1/2\), the Hessian determinant reduces to the printed \((1-2|x|^2)/(16|y|^2L)\), an independent normalization check.

Although the full potential has a pole along the axis, \(u_a(x,y)/\log|y|=(1-|x|^2)L^{a-1}\to0\) for fixed \(x\) and \(a<1\). Thus the critical loss of local non-pluripolar mass finiteness does not require a positive logarithmic divisor coefficient. This does **not** identify the non-pluripolar square with an unrestricted distributional self-wedge of an unbounded psh function.

**Correction proposed:** optional sharp-threshold remark after Example 13.2.9; leave the printed statement, source attribution, permanent tag and canonicalization untouched. **Downstream impact:** the local-finiteness premise of §§13.2–13.5 and later energy/relative-product arguments using finite non-pluripolar mass; no downstream theorem is declared false or independently certified.

## Additional first statement-level review: Problem 24.2.2

docs/sections/problems-in-hermitian-pluripotential-theory--threshold-equations-and-singular-limits/index.html, main blob **cb587f6666e775e88de2cc2aefa9c6a1dddd96e7**, source **non-kahler-pluripotential-theory:E3CD8C18**, permanent **FBE8C5BA5CA4**, physical lines **18–38**. The precise open scope fixes \(v_-(h)=0\), a nonzero \(f\in L^1(dV)\) with \(f\ge0\) and **positive individual threshold** \(b_h(f)>0\), and asks for an **exact** equation \(MA_h^{ext}(u)=b_h(f) f\,dV\), not merely a threshold subsolution inequality. The surrounding text distinguishes known \(L^p\), \(p>1\), and split-product cases. This was a quantifier inventory only; no dependent existence, capacity or PDE theorem was proved. Cited regularization material was not reopened.

**Actual additional coverage:** selected proof/model §13.2.9 and cutoff criterion §13.2.2, determinant convention Eq. 7.2.4; first statement-level §24.2.2. No whole section certified. The existing **25-chapter / 747 numbered-ToC-row** matrix continues to show **zero full-section certifications**. Historical errors, gaps, duplicates and external dependencies are unchanged. Demailly approximation/regularization and dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remain **deferred-by-user**. No production, source, permanent tag, website, CI, build or formal verification change.