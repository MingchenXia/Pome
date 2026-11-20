# 2026-11-21: Direct audit of homogeneous ball Dirichlet envelopes and mixed-density bounds

**Baseline:** current main \`b6933b772f41b45918f7e25ed1afbbb1fd892272\` (read afresh). This report is an audit-only addition to \`review/mathematical-audit\`. It makes no source, registry, permanent-tag, main, CI, or publication change.

## Exact direct mathematical scope

1. **Chapter 7, §7.7, The homogeneous Dirichlet problem and balayage:** \`docs/sections/bedford-taylor-products-and-local-capacity--the-homogeneous-dirichlet-problem-and-balayage/index.html\`, main blob \`928f3d3e36f2d03a42623b91487ecec7d189e6c7\`, mathematical physical lines **7–174**. Theorem **7.7.4**, source \`foundations-of-pluripotential-theory:FEE18534\`, permanent tag \`9181532558D7\`, lines 104–135; Corollary **7.7.5**, source \`A118D214\`, permanent \`2E8B947536C1\`, lines 140–155; Theorem **7.7.7**, source \`5C75D8E4\`, permanent \`BCFDDA1FCB7A\`, lines 160–174. The automorphism and semiconcavity input proofs are at lines 10–99.
2. **Chapter 7, §7.8, Density lower bounds and mixed products:** \`docs/sections/bedford-taylor-products-and-local-capacity--density-lower-bounds-and-mixed-products/index.html\`, main blob \`0284d93a0ac26e28746e95afda5e6875f9feaba3\`, mathematical physical lines **7–282**. Lemma **7.8.1** source \`2844C025\`, permanent \`BB19C89586B1\`, lines 23–61; Lemma **7.8.2** source \`2D6E0212\`, permanent \`1BE242B641AA\`, lines 66–95; Proposition **7.8.3** source \`183E5B3C\`, permanent \`EB2AFC8FB17C\`, lines 115–179; mixed comparison Corollaries **7.8.4** (\`66F302D3\`/\`EADDEAF9FAD9\`, lines 184–207) and **7.8.8** (\`88AEA1CD\`/\`142C8110B540\`, lines 250–282), and reverse Cauchy–Schwarz Lemma **7.8.6** (\`1BCDB7A0\`/\`91F43DBA51F0\`, lines 216–245).

The upstream statements used in this audit (7.2.2/.6, 7.3.7/.11, 5.9.2/.5, 5.10.1/.2, 5.3.3/.4, 2.8.5, 3.4.5) were checked through the printed references and hypotheses as cited by these sections, **not** given transitive complete proof-chain certification here. There is **no Demailly regularization** or dedicated excluded programme in this audit: the ordinary local convolution of bounded psh functions in these sections is a classical bounded-function tool, not the user-excluded Demailly regularization programme.

## New finding: POME-BALL-QUADRATIC-PERRON-SPECTRAL-GAP-001

**Classification:** low / **verified conditional deduction**, not a false printed theorem. The consequence below uses the printed existence/uniqueness and maximality of Theorems 7.7.4 and 7.7.7; these theorems themselves are not independently certified all the way upstream.

Let \(B=\{z\in\mathbb C^n:|z|<1\}\). Let \(A=(a_{j\bar k})\) be an **arbitrary Hermitian** matrix (not assumed positive semidefinite), let \(\lambda=\lambda_{\min}(A)\), and let \(g\) be holomorphic on a neighborhood of \(\overline B\). Write
\[
Q_A(z)=\sum_{j,k=1}^n a_{j\bar k}z_j\overline z_k,\qquad
\varphi(z)=Q_A(z)+\operatorname{Re}g(z)\quad (|z|=1).
\]
Then the *exact Perron solution* of the homogeneous ball Dirichlet problem is
\[
\boxed{\mathcal P_B[\varphi](z)
 =Q_A(z)-\lambda |z|^2+\lambda+\operatorname{Re}g(z).}
\tag{A}
\]
In particular the envelope is smooth even when \(A\) has negative eigenvalues and
\[
(\mathrm{dd}^c\mathcal P_B[\varphi])^n=0,\qquad
\mathcal H(\mathcal P_B[\varphi])=A-\lambda I\ge0,\quad
\det(A-\lambda I)=0.
\tag{B}
\]

**Complete derivation.** The Hermitian quadratic \(Q_A\) is real. Its complex Hessian in the conventions of §7.8 lines 7–13 is exactly \(A\), while \(\mathcal H(|z|^2)=I\) and \(\mathrm{dd}^c\operatorname{Re}g=0\). Because the smallest eigenvalue of \(A-\lambda I\) is zero, that matrix is positive semidefinite and singular. Thus the right-hand side of (A) is smooth psh, with vanishing Monge–Ampère determinant by the smooth determinant normalization §7.8 lines 10–13 (or §7.7.2 lines 67–69). On the sphere \(|z|=1\), its value is precisely \(Q_A+\operatorname{Re}g\). The uniqueness clause of §7.7.4 identifies this explicit function with the upper Perron envelope. This uses *no* spectral positivity assumption on the input \(A\). The same calculation verifies the claim directly; what remains conditional is only the upstream uniqueness/comparison framework.

**Exact failure of affine interpolation.** For \(n\ge2\), set
\[
u_j(z)=\sum_{k\ne j}|z_k|^2=|z|^2-|z_j|^2,\qquad 1\le j\le n.
\]
Each \(u_j\) is a smooth maximal psh function on \(B\): its complex Hessian \(I-E_{jj}\) has determinant zero. Put \(\varphi_j=u_j|_{\partial B}=1-|z_j|^2\). Formula (A), or the uniqueness in §7.7.4, gives \(\mathcal P_B[\varphi_j]=u_j\). However
\[
\frac1n\sum_{j=1}^n\varphi_j=\frac{n-1}{n}\quad\text{on }\partial B,
\]
so the envelope of the averaged boundary data is the **constant** \((n-1)/n\), while
\[
\frac1n\sum_{j=1}^n\mathcal P_B[\varphi_j]
 =\frac{n-1}{n}|z|^2.
\]
Consequently the concavity gap is exactly
\[
\boxed{
\mathcal P_B\!\left[\frac1n\sum_j\varphi_j\right]
-\frac1n\sum_j\mathcal P_B[\varphi_j]
=\frac{n-1}{n}(1-|z|^2)>0\quad (z\in B).
}
\tag{C}
\]
The average of the maximal solutions is **not maximal**, despite every individual potential having zero pure Monge–Ampère measure:
\[
\boxed{
\left(\mathrm{dd}^c\frac1n\sum_j u_j\right)^n
=\left(\frac{n-1}{n}\right)^n\eta^n>0,
\quad \eta=\mathrm{dd}^c|z|^2.
}
\tag{D}
\]
For \(n=2\) this specializes to the transparent mixed-measure identity
\[
(\mathrm{dd}^c|z_1|^2)^2
=(\mathrm{dd}^c|z_2|^2)^2=0,\qquad
\mathrm{dd}^c|z_1|^2\wedge\mathrm{dd}^c|z_2|^2=\tfrac12\eta^2>0.
\]
The factor \(1/2\) follows by expanding
\(\eta^2=(\mathrm{dd}^c|z_1|^2+\mathrm{dd}^c|z_2|^2)^2\).
This is consistent with **one-sided lower bounds** of Corollaries 7.8.4 and 7.8.8; their geometric-mean lower bound equals zero when the pure determinants vanish, and must not be misread as an upper bound or equality.

More generally \(\varphi\mapsto\mathcal P_B[\varphi]\) is concave: if \(H_j\) are Perron solutions, then any convex combination of the \(H_j\) is psh with the correspondingly averaged boundary values and so is dominated by the Perron envelope of those data. Example (C) proves strict concavity occurs, and quantifies it pointwise. This is a model implication of §7.7, **not** a claim that the general envelope operator is affine.

**Affected dependents / suggested addition:** §7.7.4 (interpretation of nonlinearity of the homogeneous Dirichlet solution operator), §7.7.7 (maximality), §7.8.4/.8 (why mixed lower-bound estimates do not imply an upper bound from pure masses). An optional explanatory example after §7.7.7 could display (A) and (C)–(D) without modifying existing statements or permanent tags. No patch to the mathematical body was made.

## Direct proof and hypothesis review

- **§7.7, lines 10–50:** The explicit ball automorphism \(T_a\) and its inverse \(T_{-a}\) are used with the correct boundary-preserving identity; \(S_{a,h}\) is smooth for \(a\) in fixed compacta and \(h\) sufficiently small. Its derivative bounds are uniform on a specified compact family, not uniform as \(a\to\partial B\).
- **§7.7, lines 58–99:** The upper second-difference bound yields a uniform *upper real Hessian* bound after mollification, and psh positivity in complex directions supplies the lower real bound. The \(C^{1,1}_{\rm loc}\) conclusion and almost-everywhere determinant formula require bounded Hessians; the proof uses the stated distributional Hessian input and does not simply interchange determinants with weak convergence.
- **§7.7, lines 104–135:** The Perron envelope is sandwiched between a psh barrier and a harmonic majorant; sphere automorphisms give the interior second-difference bound; the localized strictly psh quadratic competitor rules out positive determinant; uniform approximation of boundary data and Bedford–Taylor local continuity give the continuous case. The use of a *locally* \(C^{1,1}\) bound is consistent with the result's claimed local regularity.
- **§7.7, lines 140–174:** Decreasing local bounded psh convolutions give the homogeneous balayage, and the gluing inequality on \(\partial B\) is in the correct direction. Maximality of locally bounded psh functions is equivalent to zero top Monge–Ampère measure; in the forward implication the bounded truncation is chosen below \(u\), preserving the collar boundary order.
- **§7.8, lines 23–61:** The determinant–trace infimum and polarized two-factor inequality are correct also for singular positive semidefinite matrices by addition of \(\varepsilon I\) and continuity.
- **§7.8, lines 66–95 and 99–179:** The viscosity upper-test condition translates to distributional inequalities by a real linear change of variables and local harmonic comparison. Check especially \(\det B=1\), the real operator's factor \(1/4\), the use of **upper**, not lower, touching tests, and the direction of the comparison-principle contradiction. Passing through convolution retains a lower bound \((f^{1/n}*\rho_\varepsilon)^n\), not in general \(f*\rho_\varepsilon\).
- **§7.8, lines 184–282:** Polarization of two smooth Hessians and the \(n\)-factor mixed discriminant has the correct binomial/\(n!\) coefficients. Reverse Cauchy–Schwarz is applied only after fixing strictly positive definite remaining matrices, with a subsequent positive-semidefinite limiting step. The concluding product bounds are **lower** bounds and do not assert a converse.

**Outcome of direct review:** No newly confirmed false printed theorem or proof step in these two sections. This is not a blanket certification of the proofs on which they depend.

## Ledger and precise scope

- **New:** \`POME-BALL-QUADRATIC-PERRON-SPECTRAL-GAP-001\` — low / verified conditional deduction; derivations (A)–(D) above complete given the cited comparison and uniqueness framework.
- **No confirmed printed error** newly entered in §§7.7–7.8; no resolved old finding and no fabricated external-proof replacement.
- **Unresolved:** independent transitive certifications for BT comparison/decreasing continuity, viscosity-to-distribution inputs, the real mixed discriminant signature input and localized Hessian regularity. The exact directions and normalizations were checked here, but their earlier complete chains were not reproved.
- **Deferred-by-user:** the entire specified Demailly regularization/approximation, Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss dedicated programme is untouched and remains deferred, **not** resolved/certified.
- **Actual coverage added:** **2 full direct current mathematical sections** (§7.7 and §7.8); **0 complete upstream dependency-chain certifications**; **0 build/tests/CI**. Historical earlier visits have not been fully reconciled and are not counted as first-ever visits.
