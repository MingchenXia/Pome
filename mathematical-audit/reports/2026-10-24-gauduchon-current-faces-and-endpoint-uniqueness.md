# Gauduchon-current faces, a unique Chern–Ricci endpoint annihilator, and residual-divisor checks

**Audit date:** 2026-10-24 (Asia/Shanghai). **Fresh reviewed `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Starting review head:** `b655b89bf5a489b9916c038a407c344a80af4bf3` (preserved; no reset). **Scope:** first selected mathematical proof review of current integrated reading-edition §§12.34–12.36, with §12.7.1–2 as a strictly limited normalization dependency. These sections were previously inventory-only in the 747-row matrix. No full section, parabolic PDE package, Gauduchon variational theory, or Hopf mass construction is certified.

## Primary source anchors (public integrated edition, pinned `main`)

- `docs/sections/a-gauduchon-variational-volume--current-tests-for-smooth-positivity/index.html`, blob `4cf9e352c0d94c34ccaed0e41948a095fcfa8213`: definition of \(\mathscr G_h,m_h\) physical lines **10–16**; Theorem **12.34.1**, permanent tag `FC99385C18B8`, source anchor `non-kahler-pluripotential-theory-DC850E04`, lines **20–40**; Proposition **12.34.2**, tag `635FE1D11798`, lines **48–60**; Theorem **12.34.4**, tag `B6FA0B70406A`, lines **82–184**, especially parabolic regularity **112, 173–175**; Corollary **12.34.7**, tag `90A4213A9E87`, lines **192–213**; Proposition **12.34.12**, tag `83512AFDC859`, source anchor `non-kahler-pluripotential-theory-233B5FB5`, lines **287–308**, with its example assumptions **229–246** and geometric normalization **296–307**.
- `docs/sections/a-gauduchon-variational-volume--a-compact-dual-problem-over-gauduchon-currents/index.html`, blob `1c0f7efb92914b8a55754bd5039d7319392fb03b`: exact coefficient-matrix convention **12.7.1**, lines **13–26** (\(\beta\wedge T=n^{-1}\operatorname{tr}(B_\beta P_T)\sigma_T\), \(\operatorname{tr}P_T=n\)); this is a *normalization check only*.
- `docs/sections/a-gauduchon-variational-volume--divisorial-constraints-and-residual-volume/index.html`, blob `718dbcd7fa3ce5d5be061881c917d8a8c99406f7`: Poincaré–Lelong and Gauduchon divisor-degree conventions **10–28**; Proposition **12.35.1**, tag `C43B33AA4A18`, source anchor `non-kahler-pluripotential-theory-BA07E404`, lines **32–67**; threshold (12.35.2) **71–78**; Theorem **12.35.4**, tag `7B32818E6010`, source anchor `non-kahler-pluripotential-theory-6629041C`, lines **101–138**; derivative (12.35.5) **145–152**.
- `docs/sections/a-gauduchon-variational-volume--a-divisorial-threshold-on-the-hopf-threefold/index.html`, blob `9a5ffb97b0e8400fd7a4e65054d66938b8f75200`: Proposition **12.36.1**, tag `3A78333ED147`, source anchor `non-kahler-pluripotential-theory-6F61AFA1`, lines **10–70**.

The labels and locators identify specific current *reading-edition* content, not an inferred source-theorem number. Historical attribution, permanent tags and source content are retained unchanged.

## POME-GAUD-FACE-DERIVATIVE-001 — verified conditional deduction / low

**Claim (not a false original theorem).** Let \(X\) be connected compact complex of dimension \(n\geq1\), \(h>0\) Hermitian, and
\[
 \mathscr G_h=\{T\geq0:dd^cT=0,\ \int_Xh\wedge T=1\},\quad
 m_h(\theta)=\min_{T\in\mathscr G_h}\int_X\theta\wedge T .
\]
For smooth real \((1,1)\)-forms \(\theta,\eta\), write \(F_h(\theta)=\operatorname*{argmin}_{T\in\mathscr G_h}\int\theta\wedge T\). Then \(F_h(\theta)\) is a nonempty weakly compact exposed face, \(m_h\) is concave and 1-Lipschitz in the order-unit/operator norm
\[
 \|\xi\|_{h,\mathrm{ord}}=\inf\{C\geq0:-Ch\leq\xi\leq Ch\}.
\]
The **one-sided directional derivatives exist** and are exactly
\[
\boxed{\quad
D^+_\eta m_h(\theta)=\min_{T\in F_h(\theta)}\int_X\eta\wedge T,\qquad
D^-_\eta m_h(\theta)=\max_{T\in F_h(\theta)}\int_X\eta\wedge T.\quad}
\]
Here \(D^-_\eta\) is the conventional derivative of \(t\mapsto m_h(\theta+t\eta)\) from \(t<0\). No differentiability across a nontrivial minimizing face is claimed. The Lipschitz constant 1 is optimal, since \(m_h(\theta+ch)=m_h(\theta)+c\).

**Complete argument.** Positivity and the normalization imply \(|\int\xi\wedge T|\leq\|\xi\|_{h,\mathrm{ord}}\) for every \(T\), proving Lipschitz by taking minima twice. An infimum of continuous affine functionals is concave. The minimizer set is a nonempty closed face of the compact convex \(\mathscr G_h\): if a proper convex combination attains a minimum, both endpoints do. Put \(a(T)=\int\theta T\), \(b(T)=\int\eta T\). For \(t>0\), a \(T_0\in F_h(\theta)\) minimizing \(b\) gives
\[
\frac{m_h(\theta+t\eta)-m_h(\theta)}t\leq b(T_0).
\]
For any \(T_t\) attaining the perturbed minimum,
\[
\frac{m_h(\theta+t\eta)-m_h(\theta)}t
=\frac{a(T_t)-m_h(\theta)}t+b(T_t)\geq b(T_t).
\]
By boundedness of \(b\) and the Lipschitz estimate, \(a(T_t)\to m_h(\theta)\). Weak compactness supplies convergent **subnets** of any minimizing net as \(t\downarrow0\), and every such cluster point is in \(F_h(\theta)\). Therefore any hypothetical sequence of slopes bounded below the minimum of \(b\) on that face would contradict convergence along a subnet. This establishes the right derivative. Replace \(\eta\) by \(-\eta\) to derive the left formula. This uses compactness of nets, **not sequential compactness**.

**Exact flow-threshold consequence (affine background only).** For fixed \(\omega_0=h\) and fixed smooth \(\chi\), define \(b(\chi)=\max_{T\in\mathscr G_h}\int_X\chi\wedge T\). Then \(m_h(h-t\chi)=1-tb(\chi)\). If \(b(\chi)>0\) and \(\|\xi\|_{h,\mathrm{ord}}=\varepsilon<b(\chi)\), the positivity threshold of the affine family with \(\chi+\xi\) remains finite and
\[
 |\tau(\chi+\xi)-\tau(\chi)|
 \leq \frac{\varepsilon}{b(\chi)(b(\chi)-\varepsilon)}.
\]
Indeed \(|b(\chi+\xi)-b(\chi)|\leq\varepsilon\) and \(\tau=1/b\) for a positive \(b\). This does **not** assert that a perturbation of the *initial Hermitian metric*, which also changes \(\mathscr G_h\), satisfies the same bound; nor does it assert a twisted-flow existence theorem without its parabolic argument.

**Proposed action:** optional addendum after §12.34.1/§12.34.7, with no replacement of the existing statements. **Affected dependents:** quantitative nef/positive thresholds, active annihilator faces, and affine Chern–Ricci lifetime estimates. **Conditional inputs:** compactness of \(\mathscr G_h\) and its positivity/normalization as stated in §12.34, not any user-deferred regularization.

## POME-CRF-ENDPOINT-CURRENT-UNIQUE-001 — verified conditional deduction / low

**Claim (new strengthening, not a contradiction to Proposition 12.34.12).** In the specific projective product of §12.34.8–12, \(X=\mathbb P^m\times\mathbb P^1\), \(m\geq2\), \(Z=\{p\}\times\mathbb P^1\), \(\omega_0=(n+1)\omega+(a+2)w\), with the **given** normalization \(\int_Zw=1\), the face of normalized positive \(dd^c\)-closed currents annihilating the endpoint is not merely supported on \(Z\): it is the singleton
\[
 \boxed{\quad
 \{R\in\mathscr G_{\omega_0}:\int_X\alpha_\tau\wedge R=0\}
 =\{[Z]/2\}.
 \quad}
\]
Its unique trace probability is \(\sigma_R=w|_Z\), not just an arbitrary probability on \(Z\).

**Complete proof.** Proposition 12.34.12 establishes for any such \(R\) that \(\sigma_R=\omega_0\wedge R\) is a probability supported on \(Z\), and that its coefficient matrix satisfies \(P_R=n\Pi_{\mathrm{vert}}\), \(\sigma_R\)-a.e. For any smooth real \((1,1)\)-form \(\beta\), the coefficient convention (12.7.1) gives
\[
 \int_X\beta\wedge R
   =\int_Z \frac{\beta|_{T Z}}{\omega_0|_{T Z}}\,d\sigma_R
   =\int_Z\frac{\beta|_Z}{2w}\,d\sigma_R .
\tag{*}
\]
For every smooth real \(f\) on \(Z\), choose a smooth extension \(\widetilde f\) to \(X\). Since \(dd^cR=0\), substituting \(\beta=dd^c\widetilde f\) into (*) shows
\[
 \int_Z\frac{dd^cf}{2w}\,d\sigma_R=0 .
\]
Let \(g\in C^\infty(Z,\mathbb R)\) with \(\int_Zg\,w=0\). The standard scalar Poisson equation on the compact connected curve \(Z\simeq\mathbb P^1\) produces \(f\) with \(dd^cf=2g\,w\). Thus \(\int_Zg\,d\sigma_R=0\) for all smooth \(g\) of \(w\)-mean zero. Since both \(\sigma_R\) and \(w|_Z\) have mass one, \(\sigma_R=w|_Z\) as measures. Substituting this into (*) gives \(\int_X\beta\wedge R=\frac12\int_Z\beta=\langle [Z]/2,\beta\rangle\) for every smooth \(\beta\), so \(R=[Z]/2\). Conversely \([Z]/2\) is already shown normalized and annihilating in the printed proof.

No claim is made about arbitrary nef endpoints or about pointwise metric collapse. The statement after Proposition 12.34.12 that the preceding support/rank assertions alone do not address uniqueness remains literally accurate; the above *additional* use of \(dd^cR=0\), the curve Poisson equation and normalization supplies uniqueness.

**Proposed action:** optional corollary specific to the projective-product model, retaining original proposition and tag. **Affected dependents:** endpoint trace/lifetime (12.34.7, 12.34.12), explicit positive-volume nonbig example (12.34.10). **Conditional inputs:** Proposition 12.34.12's support/rank identification and classical compact-curve Poisson solvability, which is independent of Demailly regularization. The proof does not require a general support theorem for positive currents or an unjustified uniqueness of weak measures.

## POME-CRF-PARABOLIC-INPUT-001 — external dependency / medium

**Precise boundary.** In Theorem 12.34.4, the scalar reduction and time-dependent trace estimates are displayed at physical lines **93–171**. The continuation in **173–175** explicitly invokes a parabolic Evans–Krylov interior \(C^{2+\alpha,1+\alpha/2}\) estimate followed by parabolic Schauder bootstrapping, without proving those PDE estimates in the inspected theorem. Short-time nonlinear parabolic existence is likewise quoted at line **112**. The neighboring Corollary 14.5.8 is described as an **elliptic** analogue, not itself a proof of the parabolic estimate. This is a real analytic proof input; it is **not** a demonstrated false Chern–Ricci flow theorem and is **not** part of the user-excluded approximation programme.

**Missing self-contained step:** establish in the precise variable Hermitian background setting that the complex log-determinant's real-Hessian concave elliptic extension has the regularity and uniform constants required by the parabolic Evans–Krylov theorem, and supply an internal proof (or openly identified foundational external theorem) of that estimate and the requisite Schauder continuation. The displayed algebraic trace bound alone does not imply higher derivative bounds.

**Proposed action:** retain the classical-PDE attribution/input in the reading edition, and consider a separate internal parabolic regularity appendix; do **not** claim a complete proof of such an appendix here. **Dependents:** continuation Step 5 of Theorem 12.34.4, Corollary 12.34.7's use of the flow lifetime, and the lifetime assertion in Theorem 12.34.10. **Status remains external dependency**, not a gap in the elementary separation proof of 12.34.1.

## Other new selected passage checks — no additional finding ID

1. **§12.34.1 / Lemma 12.7.2:** Hahn–Banach separation is used in the correct Fréchet space of smooth real forms; the separating functional annihilates \(dd^cC^\infty\), and positivity plus normalization turns it into a nonzero element of \(\mathscr G_h\). Current trace normalization \(\operatorname{tr}P=n\) was checked directly. This is a **selected logical check**, not a new self-contained proof of the general functional-analytic separation theorem.
2. **§12.34.4:** checked the sign in \(dd^c=(i/2\pi)\partial\bar\partial\), \(\operatorname{Ric}=-2\pi dd^c\log\omega^n\), the affine interpolation \(\gamma_t\), the cancellation in the two displayed barrier operators at lines 118–130, and the appearance of \(\partial_t\gamma_t\) in trace calculation at 138–151. Did not rederive the full Chern trace inequality or parabolic regularity.
3. **§12.35.1 / 12.35.4:** directly checked the algebraic identity \(\beta_D+dd^c(u-\sigma_D)=\theta+dd^cu-[D]\), distributional Gauduchon degree normalization, and the reduction \(\theta+dd^c(\sigma_D+v)=[D]+\Omega\). Divisor subtraction, Lamari duality, the smooth Monge–Ampère solution and extended comparison/rigidity remain identified internal prerequisites, **not newly certified**. Both hypotheses and regularity of the ordinary-singularity-type conclusion were read: no incorrect automatic boundedness was inferred from generic Lelong numbers alone.
4. **§12.36.1:** independently recomputed \(R_a=(1-a)\alpha+\zeta\), \(R_a^3=3(1-a)^2\alpha^2\wedge\zeta=6(1-a)^2\mu_0\), \(\operatorname{vol}_{\mu_0}(\zeta+\epsilon\omega)=6\epsilon^2(1+\epsilon)\), and the Gauduchon test quotient \((1+2t)/(2t)\to1\). The choice \(\delta=1-a>0\) for \(a<1\) satisfies \(R_a-\delta\omega=a\zeta\geq0\), giving the printed unbounded-upper-mass lower bound \((1-a)^3\int_X(\omega+dd^cV_j)^3\). This last divergence depends **conditionally** on the specified Hopf family of Theorem 23.1.1, which was not recertified. The exact residual root \(6^{1/3}(1-a)^{2/3}\) has a diverging left derivative as \(a\uparrow1\); this is a consequence of the printed formula, **not** a new false-theorem or independent breakthrough.

### Coverage/accounting, excluded work and reproducibility

Newly read *selected* integrated proof passages of **§§12.34, 12.35, 12.36**. Related **§12.7.1–2** was consulted only for matrix normalization; §14.5.8, §15.28.7, §23.1.1 and general upstream PDE/trace theories were **not certified**. No other sections are marked as reviewed on the basis of these consultations. No long-standing findings were reclassified as resolved. The dedicated Demailly approximation/regularization, Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme is **strictly deferred-by-user** and was not reopened, including through prerequisite inspection. No numerical script, project test/build, CI, publication, formal verification or change to source bodies, registries, canonicalization, permanent tags or `main` was performed. All proposed mathematical insertions remain **proposals in this audit report only**.
