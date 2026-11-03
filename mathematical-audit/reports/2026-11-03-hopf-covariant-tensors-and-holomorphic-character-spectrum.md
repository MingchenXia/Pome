# Contracting Hopf quotients: holomorphic tensor vanishing and diagonal character spectra — 2026-11-03

## Pinning, scope, and relation to prior audits

**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\` (freshly checked against \`main\`; identical). **Review branch before this run:** \`30302d442f39692be13e270bb0535ba497e6fae8\`.

**Direct integrated reading edition:** \`docs/sections/contracting-hopf-quotients/index.html\`, blob \`d09d9bac3785b78b557ff5178ad7a52b34b20dac\`; Theorem **23.3.3**, source **\`demailly-complex-geometry:371996B7\`**, permanent tag **\`D81E3145A1B4\`**, physical lines **9–21, 26–50**. The triangular iteration formula is Equation **23.3.4**, source **\`demailly-complex-geometry:F5EE64FF\`**, permanent **\`436562DE848D\`**, physical lines **27–34**. Relevant section and heading tags: \`20E4E5F60131\`, \`13F0D59E6BED\`.

**Conventions-only crosscheck:** \`docs/sections/meromorphic-sections-and-divisor-classes/index.html\`, blob \`d0c40d1e3f6f515eb13169ed1cd3fb447ca161c8\`, Definition **20.7.2**, source \`demailly-complex-geometry:37374C87\`, permanent \`F9B013D39957\`, physical lines **8–9**; Proposition **20.7.3**, source \`demailly-complex-geometry:00A05C89\`, permanent \`ACC6D09EDDD9\`, lines **13–27**. Its meromorphic-section/Picard exactness is not recertified here.

**New stable finding:** **POME-HOPF-HOLOMORPHIC-TENSORS-CHARACTER-001**, **low / verified conditional deduction**. The printed Theorem 23.3.3 is **not false**. The present result is a new precise consequence of its quotient construction, with a self-contained analytic extension and tensor-jet argument. The earlier findings **POME-HOPF-JORDAN-MEROMORPHIC-FIELD-001** (fields of *meromorphic functions* on triangular quotients) and **POME-HOPF-CHAR-MEROMORPHIC-SECTIONS-001** (which character line bundles admit any *meromorphic section*) address different questions and retain their original statuses.

## Exact vanishing theorem

Let \(F:\mathbb C^2\to\mathbb C^2\) be **either** contraction in the printed Theorem 23.3.3:

- \(F(z_1,z_2)=(\lambda_1z_1,\lambda_2z_2)\), with \(0<|\lambda_1|\le|\lambda_2|<1\); or
- \(F(z_1,z_2)=(\lambda z_1,\lambda z_2+z_1^s)\), with \(0<|\lambda|<1\) and integer \(s\ge1\).

Write \(U=\mathbb C^2\setminus\{0\}\), \(X_F=U/\langle F\rangle\). Then, for **every positive integer \(r\)**,
\[
\boxed{H^0\!\left(X_F,(T_{X_F}^*)^{\otimes r}\right)=0,\qquad
 H^0(X_F,\mathcal O_{X_F})=\mathbb C.}
\]
In particular \(H^0(X_F,\Omega^p_{X_F})=0\) for \(p=1,2\), and
\[
\boxed{H^0(X_F,K_{X_F}^{\otimes m})=0\quad\text{for every }m\ge1.}
\]
Thus all plurigenera vanish and \(\kappa(X_F)=-\infty\). This does **not** assert that every meromorphic function is constant; the earlier triangular \(s\ge2\) examples can have algebraic dimension one.

### Step 1. A direct Hartogs extension for all tensor coefficients

Take a holomorphic coefficient \(f\) on \(U\). Choose a bidisc centered at the missing origin and a circle \(|\zeta_1|=\rho\) strictly inside its first coordinate disc. For every \(j\ge0\), set
\[
a_j(z_2)=\frac1{2\pi i}\int_{|\zeta_1|=\rho}
 \frac{f(\zeta_1,z_2)}{\zeta_1^{j+1}}\,d\zeta_1 .
\]
The integration torus never meets the missing origin, so \(a_j\) is holomorphic in \(z_2\) **including at \(z_2=0\)**. Cauchy's formula for \(z_2\ne0\) says
\(f(z_1,z_2)=\sum_{j\ge0}a_j(z_2)z_1^j\) when \(|z_1|<\rho\). Uniform bounds on the integration circle for \(z_2\) in a smaller closed disc give normal convergence on a smaller bidisc. The series therefore extends \(f\) holomorphically across zero. Uniqueness follows from agreement when \(z_2\ne0\). Apply this argument componentwise to every covariant tensor. This step needs **no** Demailly regularization, weighted \(L^2\), Bergman, or external Hartogs citation.

### Step 2. The contraction has no positive-order fixed jet

A tensor on \(X_F\) pulls back through the holomorphic covering \(U\to X_F\) to a tensor \(T\) on \(U\) satisfying \(F^*T=T\). By Step 1, all coefficients extend holomorphically to the origin. Put \(A=DF(0)\). For the diagonal model its eigenvalues are \(\lambda_1,\lambda_2\). For the triangular model with \(s\ge2\), \(A=\lambda I\); when \(s=1\), \(A\) is a (possibly non-diagonalizable) Jordan matrix with both eigenvalues \(\lambda\). In every case the eigenvalues of \(A\) are nonzero and of modulus strictly less than one.

Suppose a nonzero holomorphic covariant \(r\)-tensor has first nonzero homogeneous coefficient of degree \(d\ge0\) at the origin. Pullback by \(F(z)=Az+O(|z|^2)\) acts on this leading jet by the degree-\((d,r)\) representation of \(A^*\) on
\[
\operatorname{Sym}^d((\mathbb C^2)^*)\otimes
 ((\mathbb C^2)^*)^{\otimes r}.
\]
In a basis triangularizing \(A\), its eigenvalues are products of **\(d+r\)** eigenvalues of \(A\), counted with multiplicity. Consequently, when \(d+r>0\), all eigenvalues have modulus strictly less than one: the induced operator has **no eigenvalue 1**, even when \(A\) has a nontrivial Jordan block. The identity \(F^*T=T\) forces the first nonzero jet to be an eigenvector with eigenvalue 1, a contradiction. Therefore all covariant \(r\ge1\) invariant tensors vanish.

For a holomorphic function \(f\), its constant term is invariant. Apply the same argument to \(f-f(0)\), whose possible first nonzero homogeneous term has \(d\ge1\), to conclude \(f=f(0)\). Since \(\Omega^p\) and \(K^{\otimes m}\) embed as subbundles of appropriate positive tensor powers of \(T^*\), their global sections vanish as asserted. The argument does **not** require \(A\) to be diagonalizable, and hence covers the printed \(s=1\) Jordan case rather than silently reducing to a scalar contraction.

## Exact holomorphic character spectrum for diagonal quotients

For the **diagonal** \(F(z)=(\lambda_1z_1,\lambda_2z_2)\), fix \(\chi\in\mathbb C^*\) and \(p\in\{0,1,2\}\). Define
\[
\mathcal H^p_\chi(F)=
 \{\alpha\in H^0(U,\Omega_U^p):F^*\alpha=\chi\alpha\}.
\]
Then it has the **explicit finite monomial basis**
\[
\boxed{\Bigl\{z_1^az_2^b\,dz_I:
 a,b\in\mathbb Z_{\ge0},\ I\subseteq\{1,2\},\ |I|=p,\
 \lambda_1^{a+\mathbf1_{1\in I}}
 \lambda_2^{b+\mathbf1_{2\in I}}=\chi\Bigr\}.}
\]
Here \(dz_\varnothing=1\), \(dz_{\{1,2\}}=dz_1\wedge dz_2\), with increasing index order. To prove it, extend the coefficient functions to the origin by Step 1 and compare each Taylor monomial under the diagonal pullback. Distinct monomials are linearly independent; their weights are the displayed products. For a fixed nonzero \(\chi\), only finitely many pairs \(a,b\) occur, since the modulus of the product tends to zero as \(a+b\to\infty\). This gives both necessity and sufficiency, **without an unproved convergence-to-polynomial inference**.

In the scalar case \(F(z)=qz\), \(0<|q|<1\), the result becomes
\[
\boxed{
\dim\mathcal H^p_\chi(F)=
\begin{cases}
\displaystyle\binom2p(k-p+1),&
 \chi=q^k\text{ for an integer }k\ge p,\\
0,&\text{otherwise}.
\end{cases}}
\]
Indeed, the coefficient polynomials must be homogeneous of degree \(k-p\), a space of dimension \(k-p+1\), and there are \(\binom2p\) choices of \(I\). In particular the \(p=0\) dimension is \(k+1\) for \(k\ge0\), whereas the earlier **meromorphic** character problem allows negative exponents and is not equivalent to this holomorphic one.

With the explicit character-bundle convention
\[
L_\chi=(U\times\mathbb C)/\bigl((z,v)\sim(Fz,\chi v)\bigr),
\]
the equivariance \(F^*\alpha=\chi\alpha\) describes a holomorphic section of \(\Omega^p_{X_F}\otimes L_\chi\); this follows by checking the covector pullback and fiber transition together, not by assuming the twist direction. For \(p=2\), \(dz_1\wedge dz_2\) yields a nowhere-zero section of \(K_{X_F}\otimes L_{\lambda_1\lambda_2}\). Thus
\(K_{X_F}\simeq L_{\lambda_1\lambda_2}^{-1}\)
**under this stated character convention**. Its ordinary untwisted section space is zero, consistent with the first theorem.

## Classification, dependency boundary and suggested addition

- **Severity / status:** **low / verified conditional deduction**, **not a confirmed error, proof repair, duplication, or certification of the full Theorem 23.3.3 dependency chain**. The quotient/covering assertion is the sole imported conclusion of that theorem; holomorphic extension, contraction-jet calculation, and character weight count above are proved directly.
- **Hypotheses and limits:** crucially complex dimension **two**, a punctured space \(U=\mathbb C^2\setminus\{0\}\), and every eigenvalue of \(DF(0)\) of modulus \(<1\). The extension and fixed-jet argument do not apply unchanged to punctured complex dimension one, where Laurent negative powers exist. The monomial character formula is asserted for the diagonal case only; no unsupported diagonal basis is claimed in the Jordan case.
- **Proposed supplement:** place the untwisted tensor/plurigenus corollary after Theorem 23.3.3 and a separate optional diagonal-character example. Do **not** replace the theorem, its topology proof, source attribution, equation 23.3.4, or permanent tags.
- **Affected statements / readers:** canonical character and twisted holomorphic forms on Hopf quotients; legitimate contrast between algebraic dimension (meromorphic functions) and Kodaira dimension (plurigenera); possible comparisons to §§20.7.2–3 and 10.47.13. Those two sections are convention/dependency checks, not newly mathematically certified.
- **Coverage actually added:** an independent proof-level consequence of §23.3.3 in a **previously partially reviewed section**; §20.7.2–3 read only for line-bundle conventions. No new whole-section certificate. Actual current collection **25 chapters / 747 numbered sections / zero complete mathematical-section certifications**.
- **Preserved findings:** all earlier confirmed errors, proof gaps, external mathematical inputs, alternative valid versions, and historical attribution retain their classifications. The user-deferred Demailly approximation/regularization, dedicated Bergman, weighted \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes were **not opened** and remain **deferred-by-user**, not resolved or certified.
- **Write scope:** this is an audit-only proposed addition, not a source/reading-body/registry/tag/production-main edit. No test suite, build, formalization, GitHub Actions CI or website publication is claimed.
