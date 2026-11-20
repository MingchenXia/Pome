# Chapter 21.10: Guillemin metric, orbit strata, and its moment-volume measure

Date: 2026-11-20. **Production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
**Audit classification:** \`POME-TORIC-GUILLEMIN-MOMENT-STRATA-DH-001\` — **low / verified conditional deduction**, **not** a false printed theorem, not a completed independent certification of its upstream toric-geometry chain. No proof/body/canonical-entry changes are proposed on \`main\`.

## Exact directly reviewed text

- Integrated reading edition: \`docs/sections/convex-analysis-and-toric-potentials--the-guillemin-reference-metric/index.html\`, blob \`4458eef6df84ef46d601d39506017387ed292e08\`. Read **all mathematical physical lines 7–90** (the surrounding section/title/proof markup lies on lines 5–92).
- §21.10 section source \`foundations-of-pluripotential-theory:6A8ECAB3\`, permanent \`256A3051D9FC\`; Theorem **21.10.1**, source \`foundations-of-pluripotential-theory:E94A20D6\`, permanent \`B471B994CE64\`, statement lines 10–20, proof Steps 1–5 lines 24–90.
- Selected, **not entire-section**, upstream cross-checks: Delzant vertex coordinates Lemma 21.8.2(4), source \`86BADE82\`, permanent \`41C54729DBFD\`; orbit/face chart Proposition 21.9.2, source \`86CCC496\`, permanent \`7B4A7CC50CDC\`; real/complex Monge–Ampère comparison Proposition 21.12.24, source \`sgpt:D3D075B2\`, permanent \`725063C1ED05\`, and displayed Equation 21.12.25, source \`sgpt:C605E8F4\`, permanent \`C2BF3D2E88B4\`, in \`docs/sections/toric-pluripotential-theory-on-ample-line-bundles/index.html\` at approximately lines 466–490. These checks were **selected only**. 
- Inventory scope: one **entire direct** §21.10 reading; three selected upstream/downstream statement checks, **zero** transitive proof-chain certifications. Earlier audit records were not reclassified as first visits.

## Review of the printed theorem and proof

The printed theorem fixes a full-dimensional smooth lattice polytope \`P\`, its affine facet distances \(\ell_\rho\), the entropy function
\[
G_0(m)=\sum_{\rho}\ell_\rho(m)\log\ell_\rho(m),\qquad
G_0=+\infty\ \hbox{off }P,
\]
and \(F_0=G_0^*\). Step 1 (lines 27–35) correctly uses the strict positivity of
\[
D^2G_0=\sum_\rho\frac{u_\rho\otimes u_\rho}{\ell_\rho}
\]
and the negative infinite inward directional derivative at a facet to prove \(\nabla G_0:\operatorname{Int}P\to N_{\mathbb R}\) is a diffeomorphism. The boundedness of \(G_0|_P\) gives \(F_0-h_P\in L^\infty\).

Steps 2–3 (lines 37–73) invert the gradient near any coordinate orbit stratum, not merely near vertices. If \(w^0_i=0\) exactly for \(i\in I\), and \(J\) is the complementary index set, then on the associated face \(Q\) the minimizer \(q\) is uniquely in \(\operatorname{relint}Q\). On a neighborhood of \(q\), write \(G_0(t)=\sum_{i\in I}t_i\log t_i+g(t)\). Its block-Jacobian inverse is justified because \(g_{JJ}(q)\) is positive definite. The smooth inverse has
\[
t_i=|w_i|^2e^{-1-g_i(t)},\qquad
g_j(t)=\log|w_j|^2 \quad(j\in J).
\tag{A}
\]
The logarithmic cancellation in \(H_v\) is exact. Step 4 gives the positive Hermitian Hessian, including at boundary strata. Step 5 correctly checks frame transition functions, invariant curvature, and the Chern-class normalization. No new confirmed mathematical error or independent missing printed step was found in these arguments. Their overall validity is conditional on the cited toric chart and smooth line-bundle results; these upstream chains were not recertified here.

## New finding POME-TORIC-GUILLEMIN-MOMENT-STRATA-DH-001

**Claim (verified conditional deduction; low severity).** Under the full hypotheses of Theorem 21.10.1, put \(\omega=dd^c(F_0\circ\operatorname{Trop})\) on the dense torus and use its smooth Kähler extension to \(X_P\). Then:

1. The torus map
   \[
   \mu_0=\nabla F_0\circ\operatorname{Trop}:T(\mathbb C)\longrightarrow\operatorname{Int}P
   \]
   extends uniquely to a smooth \(T_c\)-invariant map \(\mu:X_P\to P\). At an orbit with coordinate zeros \(I\) in a vertex chart \(U_v\), \(\mu\) takes values in the **relative interior** of precisely the face \(Q=\{t_i=0:i\in I\}\); equation (A) supplies its smooth local defining functions. The induced map on the compact-torus quotient is a homeomorphism \(X_P/T_c\simeq P\).
2. For every bounded Borel function \(f:P\to\mathbb R\), with lattice-normalized Lebesgue measure \(dp\) on \(M_{\mathbb R}\),
   \[
   \boxed{\int_{X_P} f(\mu(z))\,\frac{\omega^n}{n!}
          =\int_P f(p)\,dp.}
   \tag{B}
   \]
   Thus \(\mu_*(\omega^n/n!)=\mathbf1_P\,dp\). In particular \(\int_{X_P}\omega^n=n!\operatorname{vol}(P)\), consistently with §21.12.24; **(B) is a measure-level/orbit-stratified strengthening**, not a new count of the already printed total-volume formula.
3. At any \(w^0\in U_v\) with zeros \(I\), nonzero coordinates \(J\), and \(\mu(w^0)=q\in\operatorname{relint}Q\), the complex Hessian determinant of the local metric weight is
   \[
   \boxed{\det\!\left(\frac{\partial^2H_v}
                 {\partial w_a\,\partial\bar w_b}(w^0)\right)
   =\frac{\displaystyle\prod_{i\in I}e^{-1-g_i(q)}}
          {\det(g_{jk}(q))_{j,k\in J}\displaystyle\prod_{j\in J}|w_j^0|^2}>0.}
   \tag{C}
   \]
   The empty determinant/product is \(1\); (C) also covers torus fixed points and the dense torus.

**Proof of smooth extension and quotient.**
On the dense torus, \(m=\nabla F_0(x)\) is the unique point solving \(x=\nabla G_0(m)\). Fix any chart point \(w^0\). The printed boundary inverse construction supplies the smooth \(t=t(|w_I|^2,\log|w_J|^2)\) near \(w^0\), and equation (A) gives \(t_i=0\) exactly where \(w_i=0\). The other facet distances remain strictly positive near the relative-interior face minimizer \(q\). Thus \(m=v+\sum_k t_ke_k\) is a smooth map with image in \(P\), extending \(\mu_0\) on the dense torus. On overlaps the local extensions agree by continuity and dense-torus agreement, so they glue uniquely.

For any face \(Q\), select a vertex \(v\in Q\) and the corresponding index sets \(I,J\). The restriction \(G_0|_Q\), expressed in \(t_J\)-coordinates, has positive definite Hessian, and its inward derivative tends to \(-\infty\) on each proper facet of \(Q\). The same minimization argument as printed Step 1 proves its gradient gives a diffeomorphism \(\operatorname{relint}Q\to\mathbb R^J\). Thus \(x_J=(\log|w_j|^2)_{j\in J}\) parametrizes \(\operatorname{relint}Q\) bijectively. The compact torus acts by changing phases of nonzero coordinates, and Proposition 21.9.2 identifies the unique toric orbit associated to \(Q\). Therefore points have equal \(\mu\)-image exactly when they are in the same \(T_c\)-orbit, and every face interior is attained. The descended continuous bijection \(X_P/T_c\to P\) is a homeomorphism since its domain is compact and its codomain Hausdorff. (All quoted orbit/face statements are retained as **conditional** upstream inputs.)

**Proof of the measure formula, including constants.**
Choose an oriented lattice basis and write on \(T(\mathbb C)\cong(\mathbb C^*)^n\)
\[
x_j=\log|z_j|^2,\qquad \theta_j=\arg z_j\pmod{2\pi},\qquad
\mu_j=\frac{\partial F_0}{\partial x_j}.
\]
Under the project's explicit \(dd^c=\frac{i}{2\pi}\partial\bar\partial\) convention, direct differentiation gives
\[
\omega=\frac1{2\pi}\sum_{jk}(F_0)_{jk}\,dx_j\wedge d\theta_k
      =\frac1{2\pi}\sum_k d\mu_k\wedge d\theta_k.
\]
Consequently the positive volume density in \((\mu,\theta)\)-coordinates is
\[
\frac{\omega^n}{n!}
=\frac1{(2\pi)^n}\,d\mu_1\cdots d\mu_n\,
                         d\theta_1\cdots d\theta_n.
\]
Step 1 makes \(x\mapsto\mu\) a diffeomorphism \(N_{\mathbb R}\to\operatorname{Int}P\); integrating each angular coordinate over a full period \(2\pi\) gives \(\int_{\operatorname{Int}P}f(p)\,dp\). Since \(\omega\) is smooth on compact \(X_P\), its volume form charges no analytic boundary divisor \(X_P\setminus T(\mathbb C)\), and \(\partial P\) has zero Lebesgue measure. Hence (B), first for continuous \(f\), then for all bounded Borel \(f\) by equality of finite Borel measures.

**Proof of the boundary determinant.**
At \(w^0_I=0\), the Hessian of \(H_v=h(|w_I|^2,\log|w_J|^2)\) is block diagonal as in printed lines 75–87. The \(I\)-block is diagonal with entries \(h_{y_i}=\exp(-1-g_i(q))\). The \(J\)-block has entries \((w_j^0\bar w_k^0)^{-1}(g_{JJ}(q)^{-1})_{jk}\), since \(x_J=g_J(t)\) on the face. Taking determinants yields (C) without any extra \(n!\), \(2\pi\), or lattice-covolume factor. The curvature density includes the project's \(dd^c\) factor separately. This also verifies strict boundary positivity quantitatively.

**Dependency and correction classification.**
The derivation is internal to the integrated §21.10 theorem plus the cited §§21.8–21.9 toric chart/orbit facts, the smooth Kähler metric, elementary calculus and compactness. It uses **no** Demailly approximation, Bergman, \(L^2\), Ohsawa–Takegoshi or positivity-loss programme. Formula (B) agrees with §21.12.24 but does not establish the general singular Monge–Ampère comparison of that section. Status: **verified conditional deduction**, not a proposed correction of the valid printed statement. Possible future *audit-only* enrichment: include (A)–(C) as an explicitly dependent corollary, preserving all source labels, theorem hypotheses and permanent tags. Affected potential downstream checks include toric moment-volume normalizations, invariant curvature integrals, facet degenerations and the §21.12 total-volume identity.

No project build, tests, CI, site publication, source edits, main edits or full transitive proof certification were performed in this run. User-excluded regularization work remains **deferred-by-user**, not resolved.
