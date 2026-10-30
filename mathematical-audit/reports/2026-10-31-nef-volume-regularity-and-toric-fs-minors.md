# 2026-10-31 — sharp one-sided regularity of a nonclosed nef volume; exact toric Fubini–Study minors

- **Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\` (read afresh); audit branch starting HEAD to be recorded by this commit's parent.
- **Findings:** \`POME-GAUD-RADIAL-NEF-REGULARITY-001\` and \`POME-TORIC-FS-MINOR-LOWER-001\`, both **low / verified conditional deduction**. Neither identifies a false printed theorem or a proof gap.
- **Scope:** new derivatives and endpoint differentiation of §12.14.1/.6/.10; new Gram/covariance/minor calculation of §21.8.3, with §21.8.2(4) used as a conditional input and §21.9.5 compared only to delimit dependencies. No complete proof chain, section or chapter is certified. The author-excluded Demailly approximation/regularization, Bergman, \`L^2\`, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof programme is **deferred-by-user**, never reopened here.

## Source-pinned integrated targets

1. \`docs/sections/a-gauduchon-variational-volume--positive-volume-without-bigness/index.html\`, Git blob \`4e892ab379abdfa3b6520671db344e94bbc7a51a\`: **Eq. 12.14.1** (\`non-kahler-pluripotential-theory:9FF975A3\`, permanent \`71973446DB97\`, physical lines **24–26**); **Theorem 12.14.6** (\`non-kahler-pluripotential-theory:7A1559DF\`, permanent \`ECAB6BFB33FD\`, lines **100–110**, proof 120–158); **Proposition 12.14.10** (\`non-kahler-pluripotential-theory:EDD3E86A\`, permanent \`0E9506DB4E70\`, lines **178–219**, continuation 229–235). The formula for \`I_epsilon\` is in line **210**, and its explicit dimension-three evaluation is line **216**.
2. \`docs/sections/convex-analysis-and-toric-potentials--smooth-lattice-polytopes-and-projective-charts/index.html\`, Git blob \`f442a7b663689b97a9b89689b8b7ae8b366a53fe\`: **Lemma 21.8.2(4)** (\`foundations-of-pluripotential-theory:86BADE82\`, permanent \`41C54729DBFD\`, physical lines **24–55**, proof 84); **Theorem 21.8.3** (\`foundations-of-pluripotential-theory:0F7315B0\`, permanent \`E49F0370E203\`, lines **107–112**, local coordinates **126–132**, metric/hessian **142–155**).
3. Context only: \`docs/sections/convex-analysis-and-toric-potentials--fans-divisors-and-character-sections/index.html\`, blob \`7ad2e6dbdd0ce59e1bf08cd9cb3c046e8c87ff6c\`, Theorem **21.9.5** (\`foundations-of-pluripotential-theory:BD98CC5B\`, permanent \`69D3D97E7701\`, lines **139–166**). Its character basis is not needed for the determinant proof; the §21.8.3 coordinate-monomial assertion alone suffices.

## Finding 1: \`POME-GAUD-RADIAL-NEF-REGULARITY-001\`

**Severity/status:** low / **verified conditional deduction**; correct printed volume formula, no missing-step or false-theorem assertion.

**Exact hypotheses.** Use *only* the explicit model of Theorem 12.14.6: \`m>=2\`, \`n=m+1\`, \`t=(m-1)/m\`, \`X=P^m x P^1\`, \`theta=omega+a w\` and the **fiber-direction** perturbation \`theta_epsilon=omega+(a+epsilon) w\`. Fix the normalized product probability measure \`mu\` of §12.14. The theorem prints \`V_mu(theta)=n\` and, for every \`epsilon>0\`, \`V_mu(theta_epsilon)=n/H(epsilon)\` with
\[
 H(\varepsilon)=m\int_0^1\frac{y^{m-1}}{y/t+\varepsilon}\,dy
 =mt\int_0^1\frac{y^{m-1}}{y+t\varepsilon}\,dy.
\]
This **is not** an assertion for the different path \`theta+epsilon h\`, nor for arbitrary nef Hermitian backgrounds.

**Precise new conclusion.** The one-sided volume function \`V(epsilon)=V_mu(theta_epsilon)\` is \(\mathcal C^{m-2}\) at \(\varepsilon=0\) (continuous when \(m=2\)), but is **not** \(\mathcal C^{m-1}\) there. More precisely,
\[
 \boxed{\ V^{(m-1)}(\varepsilon)
  =(-1)^m n(m-1)!\,m\,t^m\log(1/\varepsilon)+O(1)
   \quad(\varepsilon\downarrow0).\ }
 \tag{A}
\]
All one-sided derivatives of order \(0\le k\le m-2\) exist and are continuous, and
\[
 H^{(k)}(0+)
  =\frac{(-1)^k k!\,m\,t^{k+1}}{m-k-1}
 \qquad(0\le k\le m-2).
 \tag{B}
\]
In particular, in dimension \(n=3\) (\(m=2\)),
\[
 V(\varepsilon)-3
 \sim \frac32\,\varepsilon\log(1/\varepsilon),
 \qquad V'(0+)=+\infty
 \quad\text{in the extended sense},
 \tag{C}
\]
whereas for \(n\ge4\),
\[
 \boxed{\ V'(0+)
 =n\,\frac{(m-1)^2}{m(m-2)}
 =n\,\frac{(n-2)^2}{(n-1)(n-3)}.\ }
 \tag{D}
\]
Thus the first **noncontinuous derivative** has order exactly \(n-2\): the model's volume extends \(\mathcal C^{n-3}\) but not \(\mathcal C^{n-2}\) to the nef nonbig endpoint. The sharp regularity loss is not a property of an unreviewed general theorem.

**Proof.** For each \(\varepsilon>0\) ordinary differentiation under the positive integral gives
\[
 H^{(k)}(\varepsilon)
 =(-1)^k k! m t^{k+1}
  \int_0^1\frac{y^{m-1}}{(y+t\varepsilon)^{k+1}}\,dy.
 \tag{1}
\]
For \(k\le m-2\) the integrand increases to \(y^{m-k-2}\) (up to the fixed coefficient), which is integrable because \(m-k-2\ge0\). Dominated convergence proves (B), including \(H(0)=1\), and yields continuous one-sided derivatives to order \(m-2\). At the first critical order \(k=m-1\), split the integral into \((0,t\varepsilon)\) and \((t\varepsilon,1)\). The first integral is uniformly bounded. On the second,
\[
 \frac{y^{m-1}}{(y+t\varepsilon)^m}
 =\frac1y+O\!\left(\frac{\varepsilon}{y^2}\right),
\]
whose integrated error is bounded. Hence the integral is \(\log(1/\varepsilon)+O(1)\), and
\[
 H^{(m-1)}(\varepsilon)
 =(-1)^{m-1}(m-1)!m t^m\log(1/\varepsilon)+O(1).
 \tag{2}
\]
Since \(H\to1\), \(\,V=n/H\), and all its lower derivatives depend polynomially/rationally on the bounded derivatives \(H^{(j)}\), \(j\le m-2\), differentiation of the reciprocal shows that its sole divergent term at order \(m-1\) is \(-nH^{(m-1)}/H^2\). The factor \(H^{-2}-1=O(\varepsilon\log(1/\varepsilon))\) in the \(m=2\) case, and \(O(\varepsilon)\) for \(m>2\), produces only a bounded remainder after multiplication by the logarithm. This proves (A). In dimension three, the exact formula printed at line 216, \(H=1-(\varepsilon/2)\log((1+\varepsilon/2)/(\varepsilon/2))\), gives (C) directly; for \(m>2\), (B) at \(k=1\) gives (D). The nonzero logarithmic coefficient prevents \(\mathcal C^{m-1}\) extension. \(\square\)

**New vs old.** The printed Proposition 12.14.10 already computes \(I_\varepsilon=-H'(\varepsilon)\) and its **mass concentration** threshold \(m=2\) versus \(m\ge3\); it does not state the differentiability hierarchy of the **volume function** at the nef endpoint, the finite directional derivatives in dimension at least four, or the logarithmic singularity at every higher-dimensional critical derivative. Previous Gauduchon findings about nef powers, volume orders, bigness thresholds, and smooth minimizer attainment stay separate.

**Proposed optional correction / dependent results.** Add a new consequence after Theorem 12.14.6 or Proposition 12.14.10 distinguishing the fiber perturbation from a general directional derivative. Consequences concern smoothness claims for \(\mathcal V_\mu\) at nonclosed nef, nonbig boundaries (see §§12.11, 12.14, 12.20 and problem 24.6); no existing proposition is asserted false. The formula for \(V\) is an existing **conditional upstream input**: its global variational characterization was not independently re-proved.

## Finding 2: \`POME-TORIC-FS-MINOR-LOWER-001\`

**Severity/status:** low / **verified conditional deduction**; positive-definiteness in the printed Theorem 21.8.3 is correct; no theorem error or proof gap.

**Exact hypotheses.** Let \(P\subset M_\mathbb R\) be an \(n\)-dimensional **smooth lattice polytope**, \(n\ge1\), and \(A=P\cap M\). Fix a vertex \(v\). Its primitive edge directions \(e_1,\dots,e_n\) are a lattice basis; by Lemma 21.8.2(4), every \(m\in A\) has unique exponent \(b(m)\in\mathbb Z_{\ge0}^n\), with \(b(v)=0\) and \(b(v+e_i)=e_i^{\mathrm{standard}}\). In the printed chart \(U_v\cong\mathbb C^n\), put
\[
 f_m(w)=w^{b(m)},\quad
 S(w)=\sum_{m\in A}|f_m(w)|^2,\quad
 H_v=\log S,\quad
 G_{j\bar k}=\partial_{w_j}\partial_{\bar w_k}H_v.
\]

**Exact new formula and sharp bound.** Form the \((n+1)\times|A|\) holomorphic matrix \(B(w)\) whose row zero is \((f_m)_{m\in A}\) and rows \(1,\dots,n\) are \((\partial_{w_j}f_m)_{m\in A}\). For \(I\subset A\), \(|I|=n+1\), let \(B_I\) be its square column submatrix. Then
\[
 \boxed{\quad
 \det G(w)=\frac{\displaystyle\sum_{I\subset A,\ |I|=n+1}
             |\det B_I(w)|^2}{S(w)^{n+1}}
 \ \ge\ \frac1{S(w)^{n+1}}.
 \quad} \tag{E}
\]
The coefficient **1 is sharp** for this functional form, because at the chart origin \(w=0\), \(S(0)=1\) and \(\det G(0)=1\). It holds on *all* of \(\mathbb C^n\), even on toric boundary strata; no division by \(w_j\) is used in (E). It is an explicit determinant strengthening of the printed positive-definiteness argument, not a claim of a uniform Euclidean lower eigenvalue over the entire noncompact vertex chart.

On the dense torus \((\mathbb C^*)^n\), with probabilities \(p_m(w)=|f_m(w)|^2/S(w)\), the same tensor is the **finite lattice covariance**
\[
 G_{j\bar k}(w)
 =\frac{\operatorname{Cov}_{p(w)}(b_j,b_k)}
         {w_j\bar w_k},\qquad
 \boxed{\quad\det G(w)=
    \frac{\det\operatorname{Cov}_{p(w)}(b)}
         {\prod_{j=1}^n|w_j|^2}.\quad} \tag{F}
\]
These forms are consistent across toric boundaries by the polynomial-minor identity (E).

**Self-contained algebraic proof.** Regard \(F=(f_m)_{m\in A}\) and \(D_jF=(\partial_{w_j}f_m)_{m\in A}\) as vectors in \(\mathbb C^{|A|}\). By direct differentiation,
\[
 G_{j\bar k}
 =\frac{\langle D_jF,D_kF\rangle}{S}
 -\frac{\langle D_jF,F\rangle\langle F,D_kF\rangle}{S^2}.
\]
The Hermitian Gram matrix of the \(n+1\) row vectors \(F,D_1F,\dots,D_nF\) has determinant \(S^{n+1}\det G\) by taking the Schur complement of its \((0,0)\) entry \(S>0\). The finite-dimensional Cauchy–Binet identity writes this Gram determinant as \(\sum_I|\det B_I|^2\), proving (E). The distinguished \(I=\{v,v+e_1,\dots,v+e_n\}\) has submatrix with first column \((1,0,\dots,0)^T\) and remaining derivative block the identity, hence \(|\det B_I|=1\) identically. At \(w=0\), every other monomial has degree at least two and vanishes together with its first derivatives, so all other full minors vanish, establishing sharpness. To obtain (F), on the torus write \(x_j=\log|w_j|^2\); then \(S=\sum_m e^{\langle b(m),x\rangle}\), and differentiating \(\log S\) twice in the real \(x\)-variables gives the covariance matrix. The chain rule \(\partial_{w_j}x_j=1/w_j\) finishes the argument. \(\square\)

**Reproducible independent check.** For the Delzant square \(P=[0,1]^2\), \(F=(1,w_1,w_2,w_1w_2)\), one has \(S=(1+|w_1|^2)(1+|w_2|^2)\), \(\det G=S^{-2}\) and \(\sum_{|I|=3}|\det B_I|^2=S\); the exact rational companion script checks this at four coordinate pairs. Independently, symbolic differentiation of the explicit \(m=2\) \(H_\varepsilon\) confirms the logarithmic coefficient \(3/2\) in (C). These are **small checks**, not project tests or formal mathematical verification.

**Proposed optional correction / dependents.** Add the exact Gram-minor formula as a quantitative remark after Theorem 21.8.3, preserving source/permanent tags and the current version of §21.9.5. The result may inform local toric Monge–Ampère density estimates and coordinate calculations in §§21.9–21.10/21.12. It does **not** establish a new global toric comparison theorem or any assertion about non-Delzant singular compactifications.

## Accounting and exclusions

This increment **directly re-read** the integrated statements/proof portions §12.14.1, §12.14.6, §12.14.10 (especially radial integral and parameter differentiation) and §21.8.2(4), §21.8.3 (lattice charts and Fubini–Study Hessian). §21.9.5 is an **upstream/context statement only**, not a new complete proof verification. The review did not re-open any excluded regularization programme or infer full certification from adjacent results. **25 current chapters, 747 numbered ToC sections, zero complete mathematical-section certifications**. All older confirmed errors/proof gaps, external inputs, duplicate adjudications and user-deferred exclusions remain unchanged. No production/body/registry/tag changes, GitHub Actions, builds, publication or formal proof checks.