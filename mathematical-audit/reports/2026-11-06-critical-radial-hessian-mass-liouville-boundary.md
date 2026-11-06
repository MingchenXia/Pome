# 2026-11-06 — a critical finite-mass radial m-Hessian model and the maximality hypothesis in Euclidean Liouville

**Stable finding:** POME-HESS-RADIAL-CRITICAL-MASS-LIOUVILLE-001.  
**Severity/status:** **low / verified conditional deduction**: a fully calculated smooth model delimiting the hypotheses of a correct printed theorem. It is **not** a counterexample to Theorem 8.3.2, an alleged gap in its proof, an external replacement, or a full §8.3 certification.  
**Reviewed production main:** **b6933b772f41b45918f7e25ed1afbbb1fd892272**; **review branch is the only writing destination**.

## Exact integrated references and scope

- **docs/sections/complex-hessian-equations--liouville-and-gradient-estimates/index.html**, main blob **74cda06ad4bf75ab5fcba6e841c9ad4aa9424981**. Its Euclidean definition of admissibility and *maximality by lower tests* appears at physical lines **7–16**. Theorem **8.3.2**, source **non-kahler-pluripotential-theory:32D9A170**, permanent **96D01E7C4F0F**, occurs at lines **34–105**; its statement is at line **34** and its dimension-reduction/contradiction proof is at **39–105**. Proposition **8.3.3**, source **non-kahler-pluripotential-theory:A456C079**, permanent **B863BB49A505**, occurs at lines **113–151**, including its vanishing-scaled-density argument at **131–151**.
- **docs/sections/complex-hessian-equations--the-admissible-cone/index.html**, blob **925e6109ab7d800cde9bec4b0487842b2e6877a8**, physical lines **7–21**: the elementary symmetric polynomials \(S_j\), the open cone \(\Gamma_m\), and closed matrix cone \(C_{n,m}\). The chapter introduction **docs/sections/complex-hessian-equations/index.html**, blob **5331b937ccdaba51f1ec006d5e72dc84f7addfbf**, physical line **7**, fixes the compact intermediate-Hessian range \(2\le m<n\); the Euclidean Theorem 8.3.2 itself expressly permits \(1\le m\le n\).
- Actual current chapter-8 contents (main **docs/chapters/complex-hessian-equations/index.html**, blob **062df83b33524a8e99600c57f9fd6cc778e389f7**) list **8.1–8.13**; the new direct check is only the Euclidean statement and selected dependencies in §8.3, not all thirteen sections. Existing overall inventory: **25 chapters / 747 numbered sections / zero fully certified mathematical sections**.

## Exact model

Fix integers \(n\ge3\) and \(2\le m<n\), and set
\[
a_*=\frac{n-m}{m}=\frac nm-1>0,\qquad s=|z|^2,\qquad
u_a(z)=-(1+s)^{-a}\quad(a>0,\ z\in\mathbb C^n).
\]
Use the same normalization as Pome:
\[
dd^c=\frac{i}{2\pi}\partial\bar\partial,\quad
\beta=\frac{i}{2\pi}\sum_{j=1}^n dz_j\wedge d\bar z_j.
\]
For every \(0<a\le a_*\), \(u_a\) is nonconstant, smooth, bounded between \(-1\) and \(0\), globally Lipschitz, and **strictly \(\Gamma_m\)-admissible at every finite point**. Nevertheless it is **not maximal** in the lower-test sense of §8.3: indeed \(u_a\) itself is an interior-cone smooth lower test at every point. The striking additional property is that, at the endpoint \(a=a_*\), its entire positive Euclidean \(m\)-Hessian mass is finite and exactly
\[
\boxed{\ \int_{\mathbb C^n}(dd^c u_{a_*})^m\wedge\beta^{n-m}=a_*^m.\ }
\]
For every subcritical \(0<a<a_*\) the corresponding global mass is infinite. For \(a>a_*\) the function fails even the closed \(\Gamma_m\)-cone condition outside a compact set. Thus in **this explicit bounded smooth radial family**, the sole exponent yielding admissibility and finite global \(m\)-Hessian mass is the critical endpoint.

This proves that **adding finite total \(m\)-Hessian mass does not permit deletion of maximality from Theorem 8.3.2**, even for uniformly bounded smooth globally Lipschitz potentials with pointwise strict cone membership. The printed theorem retains maximality and is therefore not contradicted.

## Fully explicit cone calculation

For \(F(s)=-(1+s)^{-a}\), put
\[
p(s)=F'(s)=a(1+s)^{-a-1}>0,\qquad
F''(s)=-a(a+1)(1+s)^{-a-2}.
\]
The complex Hessian is \(H(u_a)=pI+F''\,\bar z\otimes z\). Its eigenvalues are \(p\), with multiplicity \(n-1\), and
\[
q=p+sF''=a(1+s)^{-a-2}(1-as).
\]
Hence \(q/p=(1-as)/(1+s)\) decreases from \(1\) to \(-a\) as \(s\to\infty\). For every \(1\le j\le m\),
\[
\begin{aligned}
S_j(H(u_a))
 &=\binom{n-1}{j}p^j+\binom{n-1}{j-1}p^{j-1}q\\
 &=\binom nj p^j\left[1-\frac{j(a+1)}n\frac{s}{1+s}\right].
\end{aligned}
\tag{1}
\]
If \(a\le a_*\), then \(j(a+1)\le m(a+1)\le n\), and the bracket is strictly positive for every finite \(s\); at \(a=a_*\), the top bracket is exactly \(1/(1+s)>0\). Conversely, for \(a>a_*\), the \(j=m\) bracket becomes negative for sufficiently large \(s\). This establishes both the exact admissibility threshold and the sharpness of the endpoint. For \(n=m\), \(a_*=0\), so this family supplies no positive exponent; this is consistent with the bounded plurisubharmonic Liouville case.

The Euclidean Lipschitz estimate is elementary:
\[
|\nabla_{\mathbb R^{2n}}u_a(z)|
=2a|z|(1+|z|^2)^{-a-1}
\le 2a\sup_{r\ge0}\frac{r}{(1+r^2)^{a+1}}<\infty.
\]
All derivatives are smooth and the values satisfy \(-1\le u_a<0\). Since (1) is strictly inside \(\Gamma_m\), the smooth function \(u_a\) touching itself from below violates precisely the **maximality** hypothesis. This argument uses Pome's *lower-test* convention rather than substituting a different notion of maximality.

## Exact density and ball-mass identity

At each point diagonalize the Hermitian Hessian relative to \(\beta\). Since \(\beta^n=n!\,\beta_1\wedge\cdots\wedge\beta_n\) for \(\beta_j=(i/2\pi)dz_j\wedge d\bar z_j\),
\[
\frac{(dd^c u_a)^m\wedge\beta^{n-m}}{\beta^n}
=\frac{S_m(H(u_a))}{\binom nm}
=p^{m-1}\left(p+\frac mn sF''\right).
\tag{2}
\]
Therefore the density with respect to \(\beta^n\) is
\[
a^m(1+s)^{-m(a+1)}
\left[1-\frac{m(a+1)}n\frac{s}{1+s}\right].
\tag{3}
\]
For a radial integrand \(g(s)\), the normalization is
\[
\int_{|z|\le R}g(|z|^2)\,\beta^n
=n\int_0^{R^2}g(s)s^{n-1}\,ds,
\]
because \(\beta^n=(n!/\pi^n)dV_{\mathbb R^{2n}}\) and the unit-ball \(\beta^n\)-volume equals \(1\). Equation (2) implies the exact divergence identity
\[
n\,s^{n-1}\frac{(dd^c u_a)^m\wedge\beta^{n-m}}{\beta^n}
=\frac{d}{ds}\left(s^n p(s)^m\right).
\]
Consequently **for every finite \(R>0\)**,
\[
\boxed{\quad
M_a(R):=\int_{|z|\le R}(dd^c u_a)^m\wedge\beta^{n-m}
=\frac{a^mR^{2n}}{(1+R^2)^{m(a+1)}}.\quad}
\tag{4}
\]
No interchange of singular limits or application of a global nonlinear comparison theorem is involved. At \(a=a_*\), (3) becomes the particularly simple everywhere-positive density
\[
(dd^c u_{a_*})^m\wedge\beta^{n-m}
=a_*^m(1+|z|^2)^{-n-1}\beta^n
\tag{5}
\]
and (4) increases to \(a_*^m\). For \(0<a<a_*\), (4) instead grows like \(a^mR^{2[n-m(a+1)]}\to\infty\). For \(a>a_*\), (4) would tend to zero because the top density changes sign at large \(s\), in agreement with the explicit failure of \(m\)-admissibility there; one must **not** treat that signed quantity as a positive Hessian mass. In the smallest intermediate case \((n,m)=(3,2)\), \(a_*=1/2\) and
\[
(dd^c u_{1/2})^2\wedge\beta
=\frac14(1+|z|^2)^{-4}\beta^3,\qquad
M_{1/2}(R)=\frac14\left(\frac{R^2}{1+R^2}\right)^3\longrightarrow\frac14.
\]
The closed forms (1)–(5) are valid for all indicated real exponents; no sampling or numerical integration is needed.

## Mathematical disposition, dependents, and open limits

**Classification: verified conditional deduction / new sharp model**, with the numerical and analytical identities independently derived. The **printed Theorem 8.3.2 is correct as far as this model tests it**; it crucially assumes maximality. Its general Liouville proof (including the direction-energy alternative in lines 68–104) has **not** been fully recertified. The example is not a proof of the converse of the theorem, and it cannot be used to drop the zero-\(m\)-Hessian/viscosity-maximality input in the blow-up step of Proposition **8.3.3**, lines **139–151**. Precisely, a bound on total Hessian mass (even a finite one) does not imply maximality of a rescaled limit; the original proposition uses pointwise density decay to obtain the necessary viscosity condition. The model gives a concrete reason to preserve that logical distinction.

**Optional proposed correction/addition (not applied to source or main):** add a remark immediately after Theorem 8.3.2 noting that bounded, Lipschitz, smooth and globally finite-mass \(\Gamma_m\)-admissibility do **not** replace maximality in the intermediate range, with \(u_{(n-m)/m}\) as a one-line explicit example and (4) as the normalization check. Retain the printed theorem, all historical attribution and permanent tags unchanged. Neither the original statement nor its proof is declared false or repaired.

**Coverage limits:** selected §8.3 (definition, Theorem 8.3.2, the relevant maximality step of Proposition 8.3.3) and the cone definitions of §8.2; §8.1 is standing-convention context. No whole §8.2/§8.3 proof chain, general Gårding algebra, gradient estimate, or chapter-wide verification is claimed. All earlier confirmed errors, proof gaps, candidates, external dependencies, genuine duplications, verified repairs and deferred records retain their previous statuses. **Entirely excluded by user:** Demailly approximation/regularization and the dedicated Bergman, weighted \(L^2\), Ohsawa–Takegoshi, multiscale atlas and positivity-loss proof-completion programme; no part of it was reopened. No project build, test suite, CI, formalization or site publication was performed.
