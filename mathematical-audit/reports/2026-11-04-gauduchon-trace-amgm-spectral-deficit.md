# Audit 2026-11-04: a quantitative spectral deficit behind Gauduchon trace/Monge–Ampère bounds

**Finding ID:** \`POME-GAUD-AGM-SPECTRAL-DEFICIT-001\`  
**Severity / status:** low / **verified conditional deduction**; the printed propositions are correct, with no identified proof gap.  
**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\` (unchanged).  
**Actual scope:** one new quantitative all-dimensional AM–GM deduction and an exact dimension-two model in previously *partially reviewed* §11.5; no whole-section or upstream PDE certification.

## Pinned integrated reading text and provenance

- \`docs/sections/gauduchon-metrics-and-linear-mass--conservation-of-the-trace-mass/index.html\`, blob \`34af83ff391b5e5590cd9cb10ca4cd2b3faff02c\`, physical lines **11–27**, Proposition **11.5.1** (conservation of the Gauduchon trace); source \`non-kahler-pluripotential-theory:0D4A42C8\`, permanent tag \`828FAD1A35BF\`; equation **11.5.2**, source \`:DF6E472D\`, permanent \`97DCB5703B01\`.
- Same file, physical lines **57–76**, Proposition **11.5.4**, source \`non-kahler-pluripotential-theory:C78BBFF1\`, permanent \`BFC1330527CA\`; equations **11.5.5** (\`:671B7CA8\` / \`1F99A7154650\`) and **11.5.6** (\`:D615B576\` / \`B78F87EF7411\`).
- All comparisons use \`dd^c=i ∂∂bar/(2π)\` and **unscaled** exterior powers \`γ^n\`, as in the printed text. This is not a comparison of Bedford–Taylor or non-pluripolar limiting measures.

## Precise statement and complete elementary proof

Let \`X\` be a compact complex \`n\`-fold, \`γ\` a smooth Gauduchon metric, \`θ\` a smooth real (1,1)-form, and \`u\` a real smooth function for which
\[
\eta=\theta+dd^cu>0,\qquad \eta^n=c f\,dV,\qquad c>0,\ f>0.
\]
At each point let \(\lambda_1,\ldots,\lambda_n>0\) be the eigenvalues of \(\eta\) relative to \(\gamma\), counted with multiplicity. Set
\[
A_\gamma(\theta)=\int_X\theta\wedge\gamma^{n-1},\qquad
B_\gamma=\int_X\left(\frac{f\,dV}{\gamma^n}\right)^{1/n}\gamma^n.
\]
The **nonnegative integrated defect** of the printed inequality (11.5.6) admits the new quantitative estimate
\[
\boxed{A_\gamma(\theta)-c^{1/n}B_\gamma
\ \geq\ \frac1{n^2}\int_X
\sum_{1\leq i<j\leq n}(\sqrt{\lambda_i}-\sqrt{\lambda_j})^2\,\gamma^n.}
\tag{*}
\]
For complex dimension **two**, the exact identity, with **twice** the coefficient of the general estimate, is
\[
\boxed{A_\gamma(\theta)-c^{1/2}B_\gamma
=\frac12\int_X(\sqrt{\lambda_1}-\sqrt{\lambda_2})^2\,\gamma^2.}
\tag{**}
\]
The integrands are symmetric in the eigenvalues; no global eigenframe or ordering is required.

**Proof of (*).** At each point the eigenvalue description gives
\[
\frac{\eta\wedge\gamma^{n-1}}{\gamma^n}=\frac1n\sum_i\lambda_i,
\qquad
\left(\frac{\eta^n}{\gamma^n}\right)^{1/n}
=(\prod_i\lambda_i)^{1/n}.
\]
Apply AM–GM to the **square roots**:
\[
(\prod_i\lambda_i)^{1/n}
=\bigl((\prod_i\sqrt{\lambda_i})^{1/n}\bigr)^2
\leq\left(\frac1n\sum_i\sqrt{\lambda_i}\right)^2.
\]
Subtracting this upper bound from \(\frac1n\sum_i\lambda_i\) yields exactly
\[
\frac1n\sum_i\lambda_i-
\left(\frac1n\sum_i\sqrt{\lambda_i}\right)^2
=\frac1{n^2}\sum_{i<j}(\sqrt{\lambda_i}-\sqrt{\lambda_j})^2.
\]
The Gauduchon condition \(dd^c\gamma^{n-1}=0\) gives
\(\int\eta\wedge\gamma^{n-1}=\int\theta\wedge\gamma^{n-1}=A_\gamma(\theta)\)
by distributional Stokes; substituting \(\eta^n=c f\,dV\) and integrating proves (*). No special compactness, regularization, or limit interchange is involved.

**Proof of (**).** In dimension two, the elementary identity
\[
\frac{\lambda_1+\lambda_2}{2}-\sqrt{\lambda_1\lambda_2}
=\frac12(\sqrt{\lambda_1}-\sqrt{\lambda_2})^2
\]
replaces the AM–GM lower bound and gives exact equality after the same trace integration. No constant larger than \(1/2\) can multiply the squared difference in an identity valid for arbitrary positive \(\lambda_i\).

**Equality.** In any dimension \(n\ge2\), equality in the printed unstrengthened bound \(A_\gamma(\theta)\ge c^{1/n}B_\gamma\) holds if and only if \(\eta=\lambda(x)\gamma\) pointwise for a smooth positive function \(\lambda\). This follows from the equality case of AM–GM at every point and smooth positivity. If both \(\theta\) and \(\gamma\) are **closed**, then \(\eta\) is closed and
\(0=d(\lambda\gamma)=d\lambda\wedge\gamma\). Wedge with \(\gamma^{n-2}\) and use injectivity of \(\alpha\mapsto\alpha\wedge\gamma^{n-1}\) on real one-forms to conclude \(d\lambda=0\). Thus \(\lambda\) is constant on each connected component. In particular, on connected compact Kähler \(X\), when \(\theta=\gamma\), trace conservation forces \(\lambda=1\), whence \(dd^cu=0\), and \(u\) is constant. **Do not** infer constant \(\lambda\) for a general nonclosed Gauduchon metric; only pointwise proportionality follows there.

## Explicit smooth strictness model (not a duplicate of the BT determinant-mixing model)

Let \(X=(\mathbf C/(\mathbf Z+\mathrm i\mathbf Z))^2\) with
\(\omega_j=\frac{\mathrm i}{2}\,dz_j\wedge d\bar z_j\),
\(\gamma=\theta=\omega_1+\omega_2\), and \(dV=\gamma^2\).
For \(|\delta|<1\), set
\[
u_\delta=-\frac{\delta}{\pi}\cos(2\pi\,\operatorname{Re}z_1),\quad
\eta_\delta=\gamma+dd^cu_\delta
=(1+\delta\cos(2\pi x_1))\omega_1+\omega_2.
\]
Direct differentiation with the stated \(dd^c\) convention verifies this formula. It is positive. Choose \(c=1\) and \(f=1+\delta\cos(2\pi x_1)\). Here
\(\int_X\gamma^2=2\), \(\lambda_1=1+\delta\cos(2\pi x_1)\), \(\lambda_2=1\), and the conserved trace is \(A_\gamma(\theta)=2\).
The exact surface identity yields
\[
2-2\int_0^1\sqrt{1+\delta\cos(2\pi x)}\,dx
=\int_0^1(\sqrt{1+\delta\cos(2\pi x)}-1)^2\,dx
=\frac{\delta^2}{8}+O(\delta^4)>0
\]
for \(\delta\ne0\). In particular a *nonconstant smooth* Kähler potential gives a strict density bound, while the right-hand side measures the exact loss of eigenvalue isotropy.

## Mathematical classification / dependencies / proposed addition

- **Status:** \`verified conditional deduction\`, low; original Proposition 11.5.1 and Proposition 11.5.4 are **correct**, not repaired. No false theorem or missing proof is claimed.
- **Verified internal step:** Stokes for smooth potentials and \(dd^c\gamma^{n-1}=0\), plus pointwise elementary inequalities. The earlier integrated Gauduchon metric existence theorem §11.4 and general Hermitian Monge–Ampère existence theorems are **not** needed to derive (*) or (**), and not certified here. The model uses only explicit smooth forms on a flat torus.
- **Suggested separate reviewable body addition:** following Proposition 11.5.4, state the integrated spectral variance lower bound and surface equality, retaining the printed theorem and its attribution; optionally use the torus model as an example. No source/registry/entry/permanent tag is edited by this audit.
- **Affected dependents:** any attempted equality or near-equality use of Proposition 11.5.4/Equation 11.5.6 (e.g. smooth Hermitian MA normalization and Gauduchon dual calculations) gains a quantitative anisotropy criterion. This is not a general nonsmooth or polar-measure statement.
- **Precise coverage:** selected §11.5.1 and §11.5.4 proof and new spectral refinement only. Chapter 11, §11.5 as a whole, and any nonlinear existence/regularity dependency remain **unverified in full**. Actual inventory: 25 chapters / 747 numbered sections / zero entirely mathematically certified sections.
- **Exclusions:** all Demailly approximation/regularization and dedicated Bergman, weighted \(L^2\), Ohsawa–Takegoshi, multiscale-atlas, positivity-loss proof programmes remain \`deferred-by-user\`, **not resolved**. No project build, tests, formalization, CI, or publication were carried out.
