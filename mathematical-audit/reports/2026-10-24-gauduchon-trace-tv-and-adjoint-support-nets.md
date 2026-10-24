# Gauduchon trace variation obstruction and quantitative stability of adjoint supports

**Audit checkpoint:** 2026-10-24 (Asia/Shanghai). **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Audit branch:** `review/mathematical-audit`.

**Strict scope:** new selected proof-level inspection of the *integrated reading edition* in §§11.31 and 11.33–11.36; §11.32 read for standing hypotheses only. The smoothing input cited by §11.31.11 was **not** investigated or expanded. All dedicated Demailly regularization/approximation, Bergman, L², Ohsawa–Takegoshi, multiscale atlas and positivity-loss work is **deferred-by-user**, neither resolved nor certified. None of the five sections, nor the upstream singular Monge–Ampère comparison/PDE theory, is certified in full.

## Finding POME-GAUD-TRACE-TV-COUNTEREXAMPLE-001

**Status:** verified conditional deduction (explicit counterexample to an *unasserted* stronger continuity statement, not a false theorem in Pome). **Severity:** low. **Proposed action:** optional caution after Example 11.31.8; do not alter the valid weak-topology equivalence in Theorem 11.31.2.

**Integrated source and anchors:** `docs/sections/gauduchon-traces-and-the-topology-of-potentials/index.html` at blob `1516feb665870be31c5be159edb6c2cf1898db8c`, Theorem 11.31.2, source `non-kahler-pluripotential-theory-8C0421FB`, permanent tag `160CE026081B`, physical lines 45–62; Proposition 11.31.7, source `non-kahler-pluripotential-theory-5B0B54B7`, permanent tag `56D7737A1AF0`, lines 120–158; Example 11.31.8, source `non-kahler-pluripotential-theory-1C437974`, permanent tag `B1E195FF817D`, lines **166–178**.

**Claim and proof.** The Gauduchon trace map from mean-normalized positive potentials equipped with uniform (hence L¹) convergence need **not** be continuous into measures with their total-variation norm, even restricted to smooth strictly positive potentials on a fixed elliptic curve. Indeed, use *precisely* the explicit example already printed in §11.31.8:
\[
 X=\mathbb C/(\mathbb Z+i\mathbb Z),\quad \eta=\frac i2\,dz\wedge d\bar z,\quad
 \theta=\gamma=\eta,\quad dV=\eta,\quad
 u_k=\frac{\cos(2\pi kx)}{2\pi k^2}.
\]
Its printed curvature identity is
\[
 \mathcal T_\eta(u_k)=\eta+dd^c u_k
       =\left(1-\frac12\cos(2\pi kx)\right)\eta>0.
\]
All these potentials are smooth, mean zero, and \(\|u_k\|_\infty=1/(2\pi k^2)\to0\). Nevertheless, with the standard *variation of a signed measure* (not a half-TV probability-distance convention),
\[
\begin{split}
\|\mathcal T_\eta(u_k)-\mathcal T_\eta(0)\|_{\mathrm{TV}}
 &=\frac12\int_X|\cos(2\pi kx)|\,\eta\\
 &=\frac12\int_0^1|\cos(2\pi kx)|\,dx
 =\boxed{\frac1\pi}\qquad(k\ge1).
\end{split}
\]
This is compatible with the weak convergence and the \(k^{-1}\) bounded-Lipschitz behavior proved in §11.31.8. It excludes an unnoticed promotion of the trace homeomorphism to total-variation convergence, including in later arguments pairing the trace with variable merely bounded Borel tests. **Dependents:** §11.31.2/.6/.7 topology, and any proposed stronger Gauduchon-current trace stability or use of non-continuous test functions.

## Finding POME-ADJOINT-DUAL-UNIFORM-L1-001

**Status:** verified conditional deduction; **severity:** low. **Proposed action:** optional quantitative corollary after Theorem 11.35.4 or Theorem 11.36.1, explicitly conditional on the established support/dual existence results. No source/body edit in this audit.

**Integrated sources and anchors:** standing hypotheses at `docs/sections/normalization-and-weak-adjoint-measures/index.html`, blob `031b5d62d25d7ff03d95e4a14988399527cc946a`, physical line 7; Proposition 11.33.2, source `non-kahler-pluripotential-theory-6D175DAF`, tag `2770AB03C0D2`, lines 27–51, and Theorem 11.33.5, source `non-kahler-pluripotential-theory-D502EBBF`, tag `5E3583383688`, lines 89–117, in `docs/sections/normalization-and-weak-adjoint-measures--the-scalar-functional/index.html`, blob `fff86de757578ed2be369ba752123f62f3d31044`; Theorem 11.35.4, source `non-kahler-pluripotential-theory-9F623A72`, tag `6830F8DE9750`, lines 44–82 of `docs/sections/normalization-and-weak-adjoint-measures--a-convex-functional-on-probability-measures/index.html`, blob `9a4ba5a98abd3273a6872c68beccf764e936d3f0`; Theorem 11.36.1, source `non-kahler-pluripotential-theory-ECDF9BCE`, permanent tag `99653D7759E2`, lines 10–55 of `docs/sections/normalization-and-weak-adjoint-measures--bounded-measurable-densities-and-stability/index.html`, blob `9c045c6e7a5bc4f0830874030c18dad0cafae905`.

Write \(B=B_\varphi\), \(H=H_\varphi\), and, for a fixed \(M<\infty\), put \(L_M=B(0)+2M\). Theorem 11.36.1 supplies a supporting probability \(\nu_F\in\mathcal A_\varphi(F)\) for every \(F\in L^\infty(dV)\) with \(\|F\|_\infty\le M\). Its printed calculation at lines 32–35 (valid for any supporter through the dual equality) shows
\[
 H(\nu_F)=B(F)+\int_XF\,d\nu_F\le L_M.
\]
Define the *uniform concentration modulus* of the compact dual sublevel
\[
 \Psi_{L_M}(s)=\sup\{\nu(E):\nu\in\mathcal K_{L_M},\
 E\subset X\text{ Borel},\ dV(E)\le s\}.
\]
By Theorem 11.35.4, \(\Psi_{L_M}(s)\to0\) as \(s\downarrow0\) (no explicit power rate follows from the source). For \(F,G\) in the above \(L^\infty\)-ball, let \(t=\|F-G\|_{L^1(dV)}\). Then, when \(0<t\le1\),
\[
 \boxed{|B(F)-B(G)|\le\sqrt t+2M\,\Psi_{L_M}(\sqrt t).}
\]
At \(t=0\) the left-hand side vanishes because \(B\) is defined on \(L^\infty\)-classes. Thus \(B\) is **uniformly**, rather than merely pointwise sequentially, continuous for the \(L^1\)-metric on each globally \(L^\infty\)-bounded ball.

**Full justification.** Apply the supporting inequality (11.36.2) first at \(F\), then at \(G\), with supports in the *same* \(\mathcal K_{L_M}\). This sandwiches \(B(F)-B(G)\) between signed integrals of \(F-G\), hence
\[
 |B(F)-B(G)|\le
 \sup_{\nu\in\mathcal K_{L_M}}\int_X|F-G|\,d\nu.
\]
For arbitrary \(a>0\), split into \(E=\{|F-G|>a\}\) and its complement. Chebyshev's inequality gives \(dV(E)\le t/a\), and \(|F-G|\le2M\) almost everywhere, so
\[
 \int_X|F-G|\,d\nu\le a+2M\Psi_{L_M}(t/a).
\]
Taking \(a=\sqrt t\) proves the claim. This argument uses no unnamed regularization or extra absolute-continuity rate. If \(M=0\), the bound is vacuous. **Dependents:** the scalar functional in §§11.33–11.36, quantitative stability in the measure topology, and joint limits of bounded logarithmic densities.

## Finding POME-ADJOINT-SUPPORT-NET-STABILITY-001

**Status:** verified conditional deduction; **severity:** low. **Proposed action:** optional directed-net corollary to Theorem 11.36.1; leave its correct sequential assertion intact.

**Sources:** Theorem 11.35.4 (tag `6830F8DE9750`, blob `9a4ba5a98abd3273a6872c68beccf764e936d3f0`, lines 44–82) and Theorem 11.36.1 including the dual formula (11.36.3), source `non-kahler-pluripotential-theory-4DCA70F5` / tag `12472E4CCDDC`, blob `9c045c6e7a5bc4f0830874030c18dad0cafae905`, lines 10–55. Comparison references: Theorem 11.34.2 (source `non-kahler-pluripotential-theory-97DE633E`, tag `86A7D85266AA`, lines 18–47) and Proposition 11.34.3 (source `non-kahler-pluripotential-theory-AE3FA53A`, tag `CB2DC1F2B712`, lines 52–65), blob `a8afa97be049b56b6c7d18302499364022feaa39`.

Let \((F_i)_{i\in I}\) be an **arbitrary directed net** of real \(L^\infty(dV)\)-classes with a common bound \(\|F_i\|_\infty\le M\), converging to \(F\) *in \(dV\)-measure*; let \(\nu_i\in\mathcal A_\varphi(F_i)\) be **arbitrary** supporting choices. Then:

1. All \(\nu_i\) belong to the single weakly compact and uniformly integrable \(\mathcal K_{L_M}\).
2. Every narrowly convergent subnet has a limit \(\nu\in\mathcal A_\varphi(F)\), and convergence is actually weak in \(L^1(dV)\) for their densities.
3. If \(\mathcal A_\varphi(F)=\{\nu\}\), the **whole original net** \(\nu_i\) converges weakly in \(L^1(dV)\) to \(\nu\). No countable cofinal subset of \(I\) is assumed or needed.

**Proof.** On the finite measure space, common \(L^\infty\) bounds plus convergence in measure imply \(t_i=\int|F_i-F|\,dV\to0\): for any \(a>0\), \(t_i\le a\,dV(X)+2M\,dV(|F_i-F|>a)\). The previous finding's *same-sublevel* estimate yields \(B(F_i)\to B(F)\) and, uniformly for \(\sigma_i\in\mathcal K_{L_M}\),
\(\int|F_i-F|\,d\sigma_i\to0\).
Weak compactness of \(\mathcal K_{L_M}\) gives convergent **subnets**. Theorem 11.35.4's Lusin/cutoff argument is uniform over \(\mathcal K_{L_M}\), so for every bounded measurable \(g\), weak measure convergence of a subnet implies \(\int g\,d\nu_i\to\int g\,d\nu\): this is precisely weak \(L^1\)-convergence of the densities, *for nets as well as sequences*. At such a limit,
\[
 B(F_i)+\int F_i\,d\nu_i\longrightarrow B(F)+\int F\,d\nu.
\]
Because every \(\nu_i\) is a minimizer, \(H(\nu_i)=B(F_i)+\int F_i\,d\nu_i\). Lower semicontinuity of \(H\) gives \(H(\nu)\le B(F)+\int F\,d\nu\); the reverse inequality is (11.36.3) with \(G=F\). Hence equality holds, so \(\nu\in\mathcal A_\varphi(F)\). If the latter is a singleton, any failure of convergence of the original net supplies a subnet staying outside some weak \(L^1\) neighborhood of \(\nu\); compactness yields a convergent further subnet with an inadmissible different cluster point, a contradiction.

**Boundary:** this proves neither uniqueness of supporting measures for all continuous \(F\), nor strong \(L^1\)/total-variation convergence of their densities. It does not rely on the smoothing arguments in the later divisorial subsection of §11.34. **Dependents:** nonsequential variational limits, density perturbations, and adjoint weak-measure selection.

## Additional actual verification, not full certification

- §11.31.2/.4/.6/.7: trace injectivity uses elliptic distributional regularity and maximum principle; weak measure topology is obtained from compact normalized PSH potentials; the bounded-Lipschitz/L¹ bounds use the *adjoint* inverse and Lipschitz convolution separately. §11.31.10/.11: checked the smooth gradient-energy integration-by-parts sign and the fixed-smooth-test part of the joint current limit. The cited smooth approximation lemma 5.42.5 was **not** reexamined; consequently Theorem 11.31.11 has **not** been independently certified.
- §11.33.2/.4/.5: checked decrease/translation sign, mixed density concavity, uniform-bounded \(L^1\) scalar-continuity structure. The PDE existence, strict domination and capacity-convergence dependencies remain conditional.
- §11.34.2/.3/.5/.7 and §11.35.2/.4: checked the Hahn–Banach supergradient sign, probability mass one, supporting-direction min/max signs, weak closedness, dual attainment, outer/inner regularity and the uniform-small-set argument. In §11.34.9/.11, inspected smooth-adjoint and continuous-Hessian stationarity **only**; no claim to the entire elliptic regularity chain. The later divisorial smoothing subsection is excluded from this audit.
- §11.36.1: checked the extension from continuous to bounded measurable dual tests, the \(L^1\)-uniform-density bound, and passing a joint varying logarithmic density and weak \(L^1\) probability to the limit.

**No new confirmed false theorem or theorem-wide certification.** No mathematical source/body/tag/registry/website edit, no build, CI, full test suite or formalization. The existing 747-row table of contents is a coverage inventory only; all pre-existing findings remain in the cumulative ledger, and all user-excluded approximation items remain **deferred-by-user**.
