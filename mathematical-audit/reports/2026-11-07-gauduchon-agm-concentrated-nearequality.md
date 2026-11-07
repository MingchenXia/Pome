# Mathematical audit — 2026-11-07: concentrated smooth Hessians and near-equality in Gauduchon AM–GM

**Finding:** `POME-GAUD-AGM-CONCENTRATED-NEAREQUALITY-001` — **low / verified conditional deduction**. The printed Proposition 11.5.1 and Proposition 11.5.4, including (11.5.5)–(11.5.6), are **correct**. This is a new sharp limitation on *uniform stability* of their integrated inequality, not a false theorem, a missing proof, or a repair.

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Integrated source:** `docs/sections/gauduchon-metrics-and-linear-mass--conservation-of-the-trace-mass/index.html` at blob `34af83ff391b5e5590cd9cb10ca4cd2b3faff02c`, physical lines 11–27 (Proposition 11.5.1), 35–46 (trace comparison), 53–76 (Proposition 11.5.4 and AM–GM proof).  
**Precise stable provenance:** Proposition 11.5.1 source `non-kahler-pluripotential-theory:0D4A42C8`, permanent `828FAD1A35BF`; equation (11.5.2) source `:DF6E472D`, permanent `97DCB5703B01`; Proposition 11.5.4 source `:C78BBFF1`, permanent `BFC1330527CA`; equations (11.5.5) source `:671B7CA8`, permanent `1F99A7154650`, and (11.5.6) source `:D615B576`, permanent `B78F87EF7411`. Cross-check of the convention `dd^c=(i/(2π))∂\bar∂` and Stokes: `docs/sections/torsion-and-the-variation-of-mass/index.html`, blob `9abec9685e33a1b40f9c0765381408eb52b325d3`, lines 14–31. The earlier independent all-dimensional *spectral deficit* report `2026-11-04-gauduchon-trace-amgm-spectral-deficit.md` is preserved without reclassification.

## New assertion, precisely scoped

For each integer complex dimension \(n\ge2\) there are smooth \(\omega\)-plurisubharmonic functions \(u_N\) on the **fixed compact flat complex torus**
\[
 X=(\mathbb C/(\mathbb Z+i\mathbb Z))^n,\qquad
 \beta_j=\tfrac{i}{2}dz_j\wedge d\bar z_j,\qquad
 \omega=\sum_{j=1}^n\beta_j ,
\]
such that \(\eta_N=\omega+dd^cu_N>0\), with the *uniform ellipticity* bound
\[
 \tfrac12\omega\le\eta_N\le\tfrac32\omega
\]
for all sufficiently large \(N\), and \(u_N\to0\) in \(C^1\), but
\[
 \|\eta_N-\omega\|_{C^0(\operatorname{End}_\omega)}\longrightarrow\tfrac12.
\]
Put \(f_N=\eta_N^n/\omega^n>0\), choose \(dV=\omega^n\), \(c=1\), and \(\theta=\gamma=\omega\) in the **printed** (11.5.6). Its exact nonnegative integrated deficit is
\[
 \Delta_N=\int_X\omega^n-\int_X f_N^{1/n}\omega^n
       =\frac{n! C_{n,\chi}}{N}+O(N^{-2}),\quad C_{n,\chi}>0.
\]
In particular, \(\Delta_N\to0\) with a sharp positive \(N^{-1}\) asymptotic while the \(C^0\) norm of the relative complex Hessian does **not** tend to zero. The result holds even for **Kähler** \(\eta_N\), uniformly comparable to the same Kähler background. It does *not* contradict the pointwise equality rigidity or the earlier spectral-\(L^2\) deficit.

## Construction and complete proof

Fix a nonnegative \(\chi\in C^\infty_c((-1/4,1/4))\) with \(\chi(0)=1\), \(0\le\chi\le1\); set \(A=\int_{\mathbb R}\chi(s)\,ds>0\) and \(\alpha=1/2\). For integers \(N\ge2\) define the smooth 1-periodic function
\[
 b_N(x)=\chi(N(x-\tfrac12)),\qquad
 q_N(x)=\alpha\big(b_N(x)-A/N\big).
\]
The bump is supported strictly within one period and \(\int_0^1q_N\,dx=0\). Consequently the one-dimensional periodic Poisson equation
\[
 v_N''=4\pi q_N,\qquad \int_0^1v_N=0
\]
has a unique 1-periodic solution. With the Pome normalization \(dd^c=\frac{i}{2\pi}\partial\bar\partial\) and \(\beta_1=\frac i2 dz_1\wedge d\bar z_1\),
\[
 dd^c v_N(x_1)=\frac{v_N''(x_1)}{4\pi}\beta_1=q_N(x_1)\beta_1.
\]
Take \(u_N(z)=v_N(\operatorname{Re} z_1)\). We have
\[
 \eta_N=(1+q_N(x_1))\beta_1+\sum_{j=2}^n\beta_j,\quad
 f_N=1+q_N,\quad \omega^n=n!\,\beta_1\wedge\cdots\wedge\beta_n .
\]
For \(N>A\), \(-\alpha A/N\le q_N\le\alpha(1-A/N)\), so the stated uniform positivity and upper bound hold. Also \(d\eta_N=0\), since \(dq_N\wedge\beta_1=0\): each \(\eta_N\) is Kähler. Its relative eigenvalues are exactly \(1+q_N,1,\ldots,1\), hence \(\|\eta_N-\omega\|_{C^0(\operatorname{End}_\omega)}=\|q_N\|_\infty=\alpha(1-A/N)\to1/2\) for large \(N\).

To check \(C^1\) convergence, note
\[
 \int_0^1|q_N|\,dx\le 2\alpha A/N.
\]
Integrating the mean-zero ODE once and choosing its integration constant to make \(v_N'\) mean zero gives
\(\|v_N'\|_\infty\le 8\pi\alpha A/N\); since \(v_N\) is mean zero, \(\|v_N\|_\infty\le\|v_N'\|_\infty\). Thus \(u_N\to0\) in \(C^1\), but not in \(C^2\).

The Gauduchon trace is conserved, directly by \(\int_0^1q_N=0\):
\[
 \int_X\eta_N\wedge\omega^{n-1}=\int_X\omega^n=n!.
\]
The AM–GM term of (11.5.6) is \(\int_X f_N^{1/n}\omega^n=n!\int_0^1(1+q_N(x))^{1/n}dx\).
Writing \(g(y)=y^{1/n}\), \(m_N=\alpha A/N\), and changing variables inside the bump gives the **exact** identity
\[
 \int_0^1g(1+q_N)\,dx
 =g(1-m_N)+\frac1N\int_{\mathbb R}
   \big[g(1-m_N+\alpha\chi(s))-g(1-m_N)\big]\,ds.
\]
Taylor expansion at \(m_N=0\), uniform on the fixed support of \(\chi\), yields
\[
 \Delta_N=\frac{n!}{N}\int_{\mathbb R}
 \left[1+\frac{\alpha\chi(s)}n-(1+\alpha\chi(s))^{1/n}\right]ds
 +O(N^{-2}).
\]
Strict concavity of \(y^{1/n}\) for \(n\ge2\) shows the displayed coefficient \(C_{n,\chi}\) is **strictly positive** because \(\chi>0\) on a nonempty open set. Its finiteness follows from compact support. No weak-limit exchange or noncompactness argument is used.

For a reproducible optional choice, use \(\chi(s)=\exp(1-(1-16s^2)^{-1})\) on \(|s|<1/4\) and \(0\) elsewhere. Direct elementary numerical quadrature gives \(A\approx0.30172508\) and \(C_{2,\chi}\approx0.00636966\). These numbers are illustrations only; the theorem is proved without numerical computation.

## Distinction, dependencies and suggested correction

The **printed proposition and its proof are correct**; the new model says that even a vanishing integrated defect, plus uniform upper and lower eigenvalue bounds and \(C^1\) convergence of potentials, does **not** furnish a \(C^0\) Hessian-stability estimate. The prior `POME-GAUD-AGM-SPECTRAL-DEFICIT-001` controls an integrated squared eigenvalue gap, consistent with concentration here: the spectral gap has small integral, not small supremum. Conversely, exact equality retains the previous pointwise proportionality rigidity.

**Internal inputs:** only the smooth trace/Stokes identity of §11.5.1 and the pointwise eigenvalue formula in §11.5.4, both verified directly in this torus model. No Hermitian MA existence, Demailly approximation/regularization, Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss argument is used. The bounded-\(\omega\)-psh approximation invoked in a *different* theorem (§11.1.7, Step 3) is explicitly **deferred-by-user**, not a prerequisite of this result.

**Proposed separate body addition:** append a scoped caveat after Proposition 11.5.4 or its quantitative spectral refinement: small integrated AM–GM defect only implies an integrated eigenvalue-anisotropy estimate and cannot imply uniform \(C^0\) Hessian closeness without further compactness/modulus hypotheses. Preserve all original statements, source variants, attribution and permanent tags. **Affected dependents:** any attempted stability strengthening based solely on (11.5.6) in smooth MA normalization, Gauduchon test comparisons or variational bounds.

**Actual coverage:** new concentration/near-equality proof for §11.5.1 and §11.5.4 and corresponding equation (11.5.6), with §11.1.2 used only for convention; these are previously partly audited, so there is **no first-visit recount**. No complete mathematical-section certification, transitive proof review, test/build/CI/formalization, or publication. The actual ToC baseline remains 25 chapters / 747 numbered sections / 0 complete section certifications; other findings remain unchanged, excluded items stay `deferred-by-user`.