# Sharp Hausdorff support dimension for continuous-potential Kähler currents

Date: 2026-10-26 (Asia/Shanghai). Reviewed main commit: b6933b772f41b45918f7e25ed1afbbb1fd892272. Starting audit head: 30f42bcd426a34956ae7f291bc227ec7f821b56c.

## Scope and source anchors

This is a **selected proof-level mathematical review**, not a certification of any whole section or its full dependency chain.

- Section 5.64, 'Null-supported Kähler currents': integrated file docs/sections/null-supported-kahler-currents/index.html; main blob 009f58a180936636f2e5927b9272f87f2c93aa29; source family transcendental-positive-cones. Lemma 5.64.1, source/permanent tag 0B34D9269CEA, lines 11–26; Theorem 5.64.2, tag E682ACE02BAF, lines 31–104, especially 43–63 (local caps and maximum), 65–95 (tie-set transversality) and 97–103 (nontrivial current). Section tag CF37B5381263.
- Section 5.65, 'Local mass bounds for pluriharmonic currents': docs/sections/local-mass-bounds-for-pluriharmonic-currents/index.html; main blob 4c2db22424afb29ff4ec2f972dc28cb50b8f0b82; source family transcendental-positive-cones. Lemma 5.65.1 (radial Jensen), tag 64884C4CF78E, lines 8–43; Corollary 5.65.2 (uniform trace growth), tag 63CAD58A60D1, lines 48–65. Section tag 0F9926EB7022.
- Reused, **not rediscovered**: the zero-Hausdorff-dimensional but nonpolar digital Cantor set from Theorem 5.51.1, tag 283A0A00F1E4, docs/sections/smooth-curves-which-are-not-pluripolar/index.html, main blob 46a19f83fb124ff5a683a25b26660c1c6a24f56e, lines 20–60. Historical POME-SMOOTH-NONPOLAR-CANTOR-CAPACITY-001 remains unchanged. We independently prove below the uniform potential-continuity statement needed here.

## Finding POME-NULL-KAHLER-SUPPORT-HDIM-SHARP-001

**Status:** verified conditional deduction; **severity:** low; **printed theorem status:** neither Theorem 5.64.2 nor Corollary 5.65.2 is alleged false. **Disposition:** optional sharpness corollary/example; no body change authorized by this review.

**Statement.** For every integer \(n\geq1\), the compact Kähler manifold
\[
X=(\mathbf P^1)^n,\qquad \omega=\sum_{j=1}^n\pi_j^*\omega_{\rm FS}
\]
has a continuous \(\omega\)-psh function \(u>0\) for which \(T=\omega+dd^cu\) is a nonzero closed positive \((1,1)\)-current and
\[
\Sigma=\operatorname{Supp}T\quad\text{is closed, Lebesgue-null, and }\quad
\dim_{\rm H}\Sigma=2n-2.
\]
All coefficient measures of \(T\) are singular. Conversely, **every** nonzero positive \(dd^c\)-closed \((1,1)\)-current on a compact Kähler \(n\)-fold has support of Hausdorff dimension at least \(2n-2\), by the uniform trace-growth bound in Corollary 5.65.2. Therefore this lower bound is optimal **even among Kähler-class currents with continuous global potentials and null supports**. In fact, the example's support is locally contained in finitely many proper real-analytic hypersurfaces.

### Proof I. Zero-dimensional support and a continuous logarithmic potential

Put \(c_k=10^{-k^2}\) and
\[
E=\bigl\{\sum_{k\geq1}\epsilon_kc_k:\epsilon_k\in\{0,1\}\bigr\}
\subset( -1,1)\subset\mathbf C.
\]
The tail \(t_k=\sum_{\ell>k}c_\ell\) is less than \(c_k/9\). Distinct first-difference \(k\) digit strings are separated by at least \(c_k-t_k>c_k/2\). Each \(k\)-prefix cylinder has diameter at most \(t_k<2c_{k+1}\), and there are \(2^k\) cylinders. Thus for every \(s>0\)
\[
\mathcal H^s(E)
\leq \liminf_{k\to\infty}2^k(2c_{k+1})^s=0,
\qquad \dim_{\rm H}E=0.
\]

Let \(\mu\) be the pushforward of fair Bernoulli measure on binary digit strings. Its support is exactly \(E\) and it is nonatomic. Distinct \(k\)-prefix cylinders are separated by \(c_k/2\), hence a ball of radius \(r_k=c_k/8\) meets at most one such cylinder:
\[
\sup_{z\in\mathbf C}\mu(B(z,r_k))\leq2^{-k}.
\]
For any \(K\), the elementary layer-cake identity gives
\[
\begin{aligned}
\sup_z\int_{|z-t|<r_K}\log\frac{r_K}{|z-t|}\,d\mu(t)
&=\sup_z\int_0^{r_K}\mu(B(z,r))\frac{dr}{r}\\
&\leq \sum_{k\geq K}2^{-k}\log\frac{r_k}{r_{k+1}}\\
&=(\log10)\sum_{k\geq K}(2k+1)2^{-k}\longrightarrow0.
\end{aligned}
\]
The truncated logarithmic potentials
\[
U_\epsilon(z)=\int\log\max\{|z-t|,\epsilon\}\,d\mu(t)
\]
are continuous and, for \(\epsilon=r_K\), converge uniformly on the entire complex plane to the finite logarithmic potential \(U(z)=\int\log|z-t|\,d\mu(t)\). The displayed bound controls their difference exactly. Consequently \(U\) is continuous. This is strictly more than finite mutual logarithmic energy; no continuity is inferred merely from that energy.

### Proof II. A positive singular representative of the Fubini–Study class

Normalize \(dd^c=\frac{\mathrm i}{2\pi}\partial\bar\partial\) and \(\omega_{\rm FS}=dd^c\log(1+|z|^2)\) on the affine chart of \(\mathbf P^1\), so \(\int_{\mathbf P^1}\omega_{\rm FS}=1\) and \(dd^c\log|z-t|^2=\delta_t\). Define
\[
\phi(z)=\int_E\log\frac{|z-t|^2}{1+|z|^2}\,d\mu(t).
\]
It is continuous by Proof I. In the coordinate \(w=1/z\) near infinity the integrand equals
\(\log\bigl(|1-tw|^2/(1+|w|^2)\bigr)\), uniformly continuous for \(t\in E\), so \(\phi(\infty)=0\) extends continuously (indeed smoothly near infinity). Distributional Fubini and Poincaré–Lelong give
\[
dd^c\phi=\mu-\omega_{\rm FS},\qquad
\omega_{\rm FS}+dd^c\phi=\mu\geq0.
\]
On \(X=(\mathbf P^1)^n\), take
\[
u=C+\sum_{j=1}^n\phi\circ\pi_j,
\quad C>-\min_X\sum_j\phi\circ\pi_j.
\]
Then \(u>0\), \(u\) is continuous and \(\omega\)-psh, and
\[
T=\omega+dd^cu=\sum_{j=1}^n\pi_j^*\mu
\]
is closed, positive, and cohomologous to the Kähler form \(\omega\). Its trace measure is explicitly
\[
T\wedge\omega^{n-1}
=(n-1)!\sum_{j=1}^n
\pi_j^*\mu\wedge\bigwedge_{i\ne j}\pi_i^*\omega_{\rm FS}.
\]
In particular it is nonzero, has total mass \(n!\), and has support exactly
\[
\Sigma=\bigcup_{j=1}^n\pi_j^{-1}(E).
\]
Every component is a product \(E\times(\mathbf P^1)^{n-1}\), up to the permutation of factors. Its Hausdorff dimension is \(2n-2\): it contains a smooth \((2n-2)\)-dimensional slice, and the standard product-cover bound together with \(\dim_{\rm H}E=0\) gives the opposite inequality. This also covers \(n=1\) (dimension zero). Fubini shows \(\Sigma\) is null. Locally near \(E\), every sheet \(\pi_j^{-1}(E)\) lies in the proper real-analytic hypersurface \(\operatorname{Im}z_j=0\). The finite union has the promised local real-analytic containment.

### Proof III. Universal lower bound and optimality

For a nonzero \(dd^c\)-closed positive \((1,1)\)-current \(S\) on a compact Kähler \(n\)-fold, set \(\sigma=S\wedge\omega^{n-1}\); it has positive finite total mass and precisely the support of \(S\). Corollary 5.65.2 gives, uniformly in the ball center,
\[
\sigma(B(x,r))\leq Cr^{2n-2}
\]
for small \(r\). For any sufficiently fine ball cover of \(\operatorname{Supp}S\), summing these inequalities gives
\[
0<\sigma(X)\leq C\sum_jr_j^{2n-2}.
\]
The mass-distribution principle therefore yields \(\dim_{\rm H}\operatorname{Supp}S\geq2n-2\). Our construction attains equality, and hence any asserted universal stronger power \(r^{2n-2+\varepsilon}\) for positive \(dd^c\)-closed \((1,1)\)-currents fails, even under continuous potential and Kähler-class hypotheses. (For \(n=1\), the lower bound is the tautological zero exponent, also attained.)

### Selected checks of the printed proofs

For Theorem 5.64.2, the branch \(\max(\rho_i,c_i)\) makes the total local curvature vanish whenever a unique positive \(b_i=c_i-\rho_i\) dominates; the exceptional tie set is null because the forbidden constant differences are countable and each remaining pluriharmonic difference has proper real-analytic level sets. This supports the printed theorem. For Lemma 5.65.1, \(dd^cS=0\) suffices for the radial test \(g(\rho)\beta^{p-1}\); the radial distribution equation and its zero boundary constant recover \(v(t)=M(t)\), so the scale derivative has the stated nonnegative annular integral. Corollary 5.65.2 uses ordinary local convolution of an already \(dd^c\)-closed positive current for the mass inequality; this is not the author's excluded Demailly analytic-singularity regularization programme. These are **selected proof checks** only, not independent certification of all cited primitives.

### Boundary of scope, disposition and dependents

Theorem 5.64.2 and Corollary 5.65.2 are mathematically consistent with the sharp example. Propose an optional self-contained sharpness example after Corollary 5.65.2, cross-referencing Theorem 5.64.2, and distinguish **Lebesgue-null support** from **polar or pluripolar support** and **Hausdorff dimension**. It would also illustrate the sharpness of the codimension-two trace growth used in heat-kernel estimates. No change to current theorem bodies, tags, source manifests or website is proposed as an automatic edit.

**Explicit exclusion:** We did **not** check Lemma 5.64.3 (lines 112–165), its strict analytic approximation input, or the approximation-based part of Corollary 5.64.4 (lines 170–end). These and the user's entire dedicated Demailly/Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale/positivity-loss proof-completion programme remain **deferred-by-user, neither resolved nor certified**. Only the actual isolated statements listed above were reviewed. No project tests, build, CI, browser publication, source edit or formal verification were performed.
