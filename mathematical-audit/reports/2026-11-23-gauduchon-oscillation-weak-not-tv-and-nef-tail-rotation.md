# Direct audit: Gauduchon oscillation, nef limits and barrier compactness

**Date:** 2026-11-23. **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Branch:** `review/mathematical-audit`.
**New result:** `POME-GAUD-DENSITY-WEAK-NOT-TV-OSCILLATION-001`, **low / verified conditional deduction**; the printed theorem and example are not false. **No full transitive proof chain certified.**

## Exact direct-reading scope

- **§12.9, whole current mathematical text**, physical lines **7–608**, `docs/sections/a-gauduchon-variational-volume--integrability-of-gauduchon-determinant-measures/index.html`, blob `42dae52119ba2bf793f104280abe615d9b25f09d`, source `non-kahler-pluripotential-theory`. Theorem 12.9.1 (source `9369A45C`, permanent `BF52D98B114F`, 14–48), Theorem 12.9.2 (`6F2BDB20`/`E7F890105D42`, 62–105), Lemma 12.9.6 (`A9AFC110`/`9F57BA26805A`, 215–264), Theorem 12.9.7 (`E0673342`/`6A30AAE398CD`, 269–310), Harnack Lemma 12.9.12 (`5C609057`/`F7130F1BDC30`, 353–426), Proposition 12.9.15 (`84780930`/`9D81484FC945`, 431–481), Theorem 12.9.18 (`A790BDE0`/`AD62F7DA0E68`, 496–549), and Example 12.9.21 (`656408ED`/`CAEF64468276`, 557–604).
- **§12.11, whole current text**, lines **7–53**, `docs/sections/a-gauduchon-variational-volume--nef-limits-and-nonattainment/index.html`, blob `086d12a65c46cfb68c7d6fe952266515ca04623b`. Theorem 12.11.1, source `F03E2CAC`, permanent `9ECB2B21B601`, 11–28; Proposition 12.11.2, source `727E9DB2`, permanent `854AAD5CF1CA`, 42–49.
- **§15.9 complete REPEAT ONLY**, lines **7–102**, `docs/sections/equations-with-prescribed-singularities--compactness-with-a-common-lower-barrier/index.html`, blob `2d4d8889cbe39cf880723c59abcb6461b26812f7`. Theorem 15.9.1, source `805DF158`/permanent `A15C1A7CB4F8` (11–49); Proposition 15.9.3 `786C08E2`/`EFAF50966FDF` (54–71); Corollary 15.9.4 `C466047F`/`F856D22ADF4C` (76–98). Earlier whole review and `POME-MA-COMMON-BARRIER-EXP-B-CRITERION-001` of 2026-11-18 are NOT new progress.
- **§20.6 complete REPEAT ONLY**, lines **7–74**, `docs/sections/analytic-cycles-and-cartier-cycles/index.html`, blob `d4817ac64b1365bd967d42cd474fec169f992e28`. The already established `POME-CARTIER-QUADRIC-NON-Q-CARTIER-001` is not relogged.
- **§12.1 standing assumptions selected only**, `docs/sections/a-gauduchon-variational-volume/index.html`, lines **8–20**: connected compact \(X\); the compact Gauduchon dual problem requires \(n\ge2\), and the later smooth coefficient-independent Harnack application in §12.9 explicitly uses \(n\ge3\).

**Actual change in coverage:** two whole current sections (§§12.9, 12.11), two complete *repeat* sections (§§15.9, 20.6), one selected standing-context reading (§12.1). Do not infer historical first visits from the existing 747-section matrix.

## POME-GAUD-DENSITY-WEAK-NOT-TV-OSCILLATION-001

**Severity/status:** low / verified conditional deduction, NOT a false printed theorem or claimed full upstream proof certificate. This refines the correct Example 12.9.21 rather than repeating the different existing §15.37 weak-not-TV finding.

Use precisely Example 12.9.21 on a connected compact complex manifold \(X\), \(n\ge3\), with Hermitian \(\omega>0\), smooth positive probability form \(dV\), and fixed \(0<\varepsilon<1\). In a coordinate chart put \(x=\operatorname{Re}z_1\), \(\beta=dx\wedge d^cx\) (positive of rank one, \(\beta^2=0\)), and choose \(0\le\zeta\in C_c^\infty\le1\) equal to one near a point. For small fixed \(a>0\) the potentials
\[
v_j=\frac a{j^2}\zeta\sin(jx)-\sup_X\left(\frac a{j^2}\zeta\sin(jx)\right)
\]
belong to \(\mathcal V_\varepsilon\) of Eq. 12.9.17, so \((1-\varepsilon)\omega\le\Omega_j:=\omega+dd^cv_j\le(1+\varepsilon)\omega\) and \(\|v_j\|_\infty\to0\). Write
\[
c_j=\int_X\Omega_j^n,\quad c_0=\int_X\omega^n,\quad
F_j=\log\frac{\Omega_j^n}{c_j\,dV},\quad
\mu_j=e^{F_j}dV=\frac{\Omega_j^n}{c_j}.
\]
Set \(s=\operatorname{tr}_\omega\beta>0\) in the coordinate chart and extend \(\chi=\zeta s\) by zero to \(X\). It is smooth, nonnegative and nonzero. **Then**
\[
\boxed{\mu_j\rightharpoonup \mu_0=\omega^n/c_0,\qquad
\lim_{j\to\infty}\|\mu_j-\mu_0\|_{\rm TV}
=\frac{a}{\pi c_0}\int_X\chi\,\omega^n>0.}
\]
Here \(\|\mu-\nu\|_{\rm TV}=\sup_E|\mu(E)-\nu(E)|=\frac12\int|d\mu-d\nu|\) for probability measures. Moreover, **neither the smooth normalized probability densities \(e^{F_j}\), nor their uniformly bounded logarithms \(F_j\), possess a strongly convergent subsequence in any \(L^r(dV)\), \(1\le r<\infty\).**

**Complete proof.** The source's Hessian product expansion (physical lines 575–581) is
\[
dd^cv_j=-a\zeta\sin(jx)\beta+R_j,\qquad
\|R_j\|_{C^0(\omega)}=O(j^{-1}).
\]
The determinant polynomial is uniformly Lipschitz on this bounded positive cone, and \(\beta^2=0\) makes the rank-one leading calculation *exact*:
\[
(\omega-a\zeta\sin(jx)\beta)^n=(1-a\chi\sin(jx))\omega^n,
\quad
\Omega_j^n=(1-a\chi\sin(jx))\omega^n+O(j^{-1})\omega^n.
\]
Since \(\chi\,\omega^n\) is smooth and compactly supported in the chart, integration by parts in the \(x\)-coordinate shows \(\int_X\chi\sin(jx)\omega^n=O(j^{-1})\), hence \(c_j=c_0+O(j^{-1})\). Uniformly as signed densities relative to \(\omega^n\),
\[
\mu_j-\mu_0=-\frac a{c_0}\chi\sin(jx)\omega^n+O(j^{-1})\omega^n.
\]
Riemann–Lebesgue (first for smooth test functions, then continuous by approximation) gives weak convergence of these probability measures. Periodic averaging of \(|\sin(jx)|\), whose mean is \(2/\pi\), yields
\[
\lim_j\int_X|d\mu_j-d\mu_0|
=\frac{2a}{\pi c_0}\int_X\chi\,\omega^n.
\]
Taking half proves the boxed TV constant. Strong \(L^r(dV)\) convergence of any density subsequence would imply \(L^1\) convergence on the probability space. Its weak-measure limit must be \(d\mu_0/dV\), contradicting the positive defect. Uniform Hessian ellipticity and \(c_j\to c_0>0\) give uniform \(L^\infty\) bounds for the logarithms \(F_j\); the exponential is Lipschitz on their common bounded range. Thus a strongly \(L^r\)-convergent subsequence of \(F_j\) would also yield \(L^1\)-convergence of \(e^{F_j}\), which is impossible. \(\square\)

**Proposed correction / dependents:** The original Example 12.9.21 and Theorem 12.9.18 remain valid. Optionally append this quantitative consequence to the example without changing permanent tags, provenance or the theorem's hypotheses. It separates weak convergence of prescribed smooth probabilities from total-variation/strong-\(L^r\) compactness, even under fixed two-sided complex-Hessian bounds. It does NOT resolve the question in §12.9 about arbitrary bounded continuous density families.

## Other mathematical checks: signs, exponents and dependencies

- **§12.9.1–2:** Pointwise matrix AGM gives \(c_h^{1/n}h\,\Gamma_0(T)\le\Omega_h\wedge T\), and \(\int\Omega_h\wedge T=1\) uses \(dd^cT=0\). The lower-density input §14.19.19 gives the \(L^{np/(np-1)}\) exponent by duality. The endpoint bound substitutes \(c_h\int h^n dV\ge v_-(\omega)\); reverse sharpness relies on the separate identification \(\inf_g c(g)=v_-(\omega)\) in §12.15.4. We did not certify that full chain.
- **§12.9.6–7:** The nonlinear map satisfies \(KQr\le1/4\), giving image radius \(\le3r/4\) and contraction \(\le1/2\). Its adjoint-factor map has \(\kappa=GC_ADr\le m/(4C_0)\le1/4\). The exact identities \(q_F=(\chi/Z)J\) and \(k_{T_F}=(\chi/Z)J^{(n-1)/n}\), with \(Z\ge2^{-(n-1)}\), reproduce the printed constants \(3^{n+1}aH_{\max}/4\) and \(3^naH_{\max}^{(n-1)/n}/2\). Fredholm/Schauder prerequisites remain conditional.
- **§12.9.12–18:** The Moser iteration avoids the exceptional power \(p=1\); the BMO estimate for \(\log u\) is the bridge from positive and negative moments to Harnack. For the Gauduchon adjoint \(d(\Omega_v^{n-1})=(n-1)d\omega\wedge\Omega_v^{n-2}\), so the first-order coefficient is controlled by fixed Hermitian torsion and bounded coefficients, not second derivatives of \(\Omega_v\). The identities \(r_v=J_v\rho_v/N_v\) and \(k_{T_v}=J_v^{-1/n}r_v\) verify the inequality directions of Eq. 12.9.19. No new statement error found.
- **§12.11:** For nef \(\theta\), positivity of \(\theta+\epsilon h\) after a smooth \(dd^c\) correction follows directly from the nef definition. Infima over \(\epsilon>0\) and Gauduchon tests commute even without compactness because they are simply two infima, and the quotient is affine increasing in \(\epsilon\). At \(\lambda_\mu(\theta)=0\), attainment implies \(\int\theta\wedge\gamma^{n-1}=0\); the smooth \(dd^c\)-exactness conclusion depends on the distinct Lemma 11.6.3, not on a spurious normalization of \(\gamma\).
- **§15.9 (repeat):** A common lower bound makes finite and infinite rooftops genuine competitors. Splitting finite rooftop contact sets by the first active index bounds the weighted discrepancy by a summable error tail; weighted lower semicontinuity and the strict smaller-background envelope condition permit singular domination; upper tail envelopes then squeeze capacity convergence. Corollary 15.9.4 still depends on the separate §13.15.23 deep-sublevel tail criterion. This is not relogged as a new exponential criterion.
- **§20.6 (repeat):** Analytic-cycle restrictions and the rank-one quadric Cartier obstruction agree with earlier reports. The already proved stronger non-\(\mathbf Q\)-Cartier statement is NOT new.

**Remaining unverified internal proof chains:** §§11.4.2, 11.6.3, 12.7.3, 12.15.4, 14.19.19, 13.14.8, 13.15.23, 15.2.2 and fixed-operator elliptic theory. An unrecursively checked internal premise is **not** automatically a proof gap. No other new confirmed error or essential external non-Hironaka input was established. All Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale atlas and positivity-loss proof-completion programmes remain **deferred-by-user**, neither resolved nor certified.

**Actions:** Only audit Markdown. No numerical/CI/build tests, no edits to main/source bodies/registry/canonicalization/permanent tags/published site; no automatic PR merge or publication.
