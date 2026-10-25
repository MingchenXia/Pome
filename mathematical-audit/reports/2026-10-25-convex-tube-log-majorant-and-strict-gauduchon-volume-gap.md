# Convex-log tube majorants and strict Gauduchon volume gaps

**Date:** 2026-10-25. **Reviewed main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting audit branch SHA:** 7c0d4aeb97427357b864127978530f757d16fb2a.

Only selected proof passages of §§9.38–9.39 and §12.24 were inspected, together with the definitions in §12.2. No full section or transitive dependency chain is certified. All dedicated Demailly approximation/regularization and Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss tasks remain deferred-by-user.

## POME-TUBE-CONVEXLOG-MAJORANT-001

**Severity:** low. **Status:** verified conditional deduction; neither a false theorem nor a repair of one.

**Exact printed sources.** docs/sections/normal-spaces-and-tube-continuation--holomorphic-extension-from-a-connected-tube/index.html, blob a94e3aa490fee004284dab37f4f6e35094bf2bfa: Lemma 9.39.2, source label demailly-complex-geometry-CA558429, permanent tag 7D65E928B1FB, lines 27–60, with Cauchy center Eq. 9.39.3 (BA7B66342790) and local consistency Eq. 9.39.4 (6921BEE69455); Theorem 9.39.7, source demailly-complex-geometry-F7AA195B, tag E5EB0154B387, lines 97–147, especially explicit contractible path-and-dwell loops at lines 108–127, Eq. 9.39.8 tag F09A8AEAD47E, and the compatibility/gluing argument at lines 138–146.

**Precise theorem.** Let omega be a nonempty connected open subset of R^n and let f be holomorphic on T_omega=omega+iR^n. Denote its unique Bochner extension to T_conv(omega) by F. Assume that a positive continuous function M on omega bounds f uniformly in the imaginary directions:
\[
 |f(x+\mathrm i y)|\le M(x),\qquad x\in\omega,\quad y\in\mathbb R^n.
\]
For x in the convex hull put
\[
 C_M(x):=\inf\left\{\sum_{j=1}^N t_j\log M(x_j):
 N<\infty,\ t_j\ge0,\ \sum_jt_j=1,\
 x_j\in\omega,\ \sum_jt_jx_j=x\right\}.
\]
The infimum may be extended-valued. Then, with log(0)=-infinity,
\[
 \boxed{\log|F(x+\mathrm i y)|\le C_M(x)\quad
 (x\in\operatorname{conv}\omega,\ y\in\mathbb R^n).}
\]
In particular, **Bochner extension is isometric in the supremum norm**:
\[
 \boxed{\|F\|_{H^\infty(T_{\operatorname{conv}\omega})}
       =\|f\|_{H^\infty(T_\omega)}}
\]
for every bounded holomorphic f. The logarithmic bound is sharp for arbitrary real affine L(x)=a·x+b, as f(z)=exp(a·z+b) and M(x)=exp L(x) attain equality at every point.

**Proof.** Fix x=sum_j t_j x_j with finitely many points x_j in omega, discarding zero coefficients. Choose an anchor a in omega and smooth paths in omega from a to each x_j. Add auxiliary destinations forming a small real coordinate cross about a, so that the destination set affinely spans R^n and contains a in the interior of its convex hull. For 0<delta<<1 use exactly the outward-path/dwell/return smooth loops gamma_delta of the proof of 9.39.7. Assign total travel time delta, positive auxiliary dwell times O(delta²), and main destination dwell times t_j(1-delta-O(delta²)). All dwell times are positive, so the parameters belong to the *interior* of the convex parameter space P of that proof. The real part of the Schwarz disc center is
\[
 x_\delta=A_{\gamma_\delta}(0)
 =\delta c+(1-\delta-O(\delta^2))x+O(\delta^2)\longrightarrow x,
\]
where c is the fixed mean of the travels. The loops contract to the constant loop a through smooth loops inside omega.

For each fixed imaginary translation iy, Lemma 9.39.2 gives a holomorphic filling H_delta(zeta) of the boundary values f(A_gamma_delta(e^{it})+iy). The printed local compatibility and global gluing identify its center value with F(x_delta+iy). Apply the submean inequality to log|H_delta|:
\[
 \log|F(x_\delta+\mathrm iy)|
 \le \frac1{2\pi}\int_0^{2\pi}
   \log|f(A_{\gamma_\delta}(e^{it})+\mathrm iy)|\,dt
 \le \frac1{2\pi}\int_0^{2\pi}\log M(\gamma_\delta(t))\,dt.
\]
The paths form a fixed compact subset of omega, so log M is uniformly bounded on all travels and auxiliary destinations. Travels contribute O(delta), auxiliary dwells contribute O(delta²), and the main dwells contribute sum_j t_j log M(x_j)+o(1). Since x_delta tends to x, continuity of F yields the desired inequality if F(x+iy) is nonzero; if it is zero the inequality is automatic. Infimizing over all representations proves the result. There is no exchange of unproved net limits and integration; only finite loops and bounded real-variable averages occur. For nonzero bounded f, choose M equal to the constant norm of f and use restriction for the reverse inequality; f=0 is immediate. For real affine L every barycentric average of L equals L(x), giving sharpness.

**Action/dependents.** Optional corollary following Theorem 9.39.7; do not remove the connectedness hypothesis. Analytic filling and global compatibility are internal conditional inputs, **not** independently certified by this new proof. The strengthened logarithmic barycentric estimate requires submean/Jensen, not merely the triangle inequality applied to the Cauchy integral.

## POME-GAUD-STRICT-DOM-GAP-001

**Severity:** low. **Status:** verified conditional deduction; the printed monotonicity statement is correct.

**Exact printed sources.** docs/sections/a-gauduchon-variational-volume--orders-of-degeneration-at-the-nef-boundary--positive-current-subtraction-and-divisorial-residuals/index.html, blob 8c1eb4eba5af6cc9331b103ed5156251091acce7: Proposition 12.24.1, source label non-kahler-pluripotential-theory-EAC70D2C, tag 7CE9EDC18591, lines 10–34; Eq. 12.24.2 tag 2818CCA10129, lines 15–20; divisor examples Proposition 12.24.3 tag D15FEB2692E7, lines 40–73, and Corollary 12.24.5 tag 9860E4D04E6C, lines 80–98. Def. 12.2.1 tag 0C4AF7E2CEBB, Prop. 12.2.2 tag 4AF37F3C8091 and Theorem 12.2.3 tag 2DB664A6EFDF in docs/sections/a-gauduchon-variational-volume--the-quotient-and-the-smooth-equation/index.html, blob 9ec67161d46b3ba20afa1b1c9a0c84f29322763e, lines 7–80.

**Precise theorem.** Keep smooth nef theta,beta and compact X, smooth strictly positive probability mu, positive Hermitian h and L¹ potential phi from Proposition 12.24.1. Strengthen the current hypothesis to
\[
 S=(\theta-\beta)+dd^c\varphi\ge \tau h
 \quad\text{for some }\tau>0.
\]
Write L=lambda_mu(h)>0. For every epsilon>0,
\[
 \boxed{\lambda_\mu(\theta+\epsilon h)
        -\lambda_\mu(\beta+\epsilon h)\ge\tau L,}
\]
and
\[
 \boxed{\mathcal V_\mu(\theta+\epsilon h)
 -\mathcal V_\mu(\beta+\epsilon h)
 \ge [(\epsilon+\tau)^n-\epsilon^n]\mathcal V_\mu(h).}
\]
Both bounds have **optimal constants, simultaneously at all epsilon**, and the first form theta has degeneration order zero. No such strictly positive uniform gap is claimed under only S>=0.

**Proof.** For every smooth Gauduchon test gamma, integration by parts with dd^c gamma^(n-1)=0 gives
\[
 \int_X(\theta-\beta)\wedge\gamma^{n-1}
 =\langle S,\gamma^{n-1}\rangle
 \ge\tau\int_Xh\wedge\gamma^{n-1}.
\]
Divide by the positive D_mu(gamma) of Definition 12.2.1, then take infima, using inf(A_gamma+B_gamma)>=inf A_gamma+inf B_gamma. This gives the first bound. Since beta is nef, its Gauduchon pairing is nonnegative; hence lambda_mu(beta+epsilon h)>=epsilon L. The function a↦(a+tau L)^n-a^n is nondecreasing on a>=0 for every n>=1, so raising the root-volume inequality to the nth power and subtracting gives the second.

For optimality, choose beta=0, theta=tau h, phi=0 on any compact complex X, with any smooth positive Hermitian h and smooth strictly positive probability mu. These forms are nef in the Hermitian convention and S=tau h. Positive homogeneity of the defining quotient gives lambda_mu(theta+epsilon h)=(tau+epsilon)L and lambda_mu(beta+epsilon h)=epsilon L. Thus equality holds in *both* inequalities for every epsilon. Finally the root-volume lower bound tau L and the finite fixed-Gauduchon-test upper bound as epsilon decreases force theta's logarithmic degeneration order to be zero.

**Action/dependents.** Optional sharp quantitative refinement directly after Proposition 12.24.1; preserve its nonstrict version for general nonnegative currents S. The defining variational quotient, positivity for strictly positive h and nefness are used; the general nonlinear smooth Monge–Ampere existence proof is not revisited. Other divisorial-order examples in §12.24 rely on the printed §12.21 and §16.29 constructions and remain conditional.

## Additional actual proof inspection (not a third finding)

- **§9.38:** normal-space standing convention explicitly includes countable basis in physical line 7. Directly read Corollary 9.38.1 (tag 512196636E86, lines 10–24), coherent pole support/purity Lemma 9.38.2 (DA978F0F96EA, lines 29–53), normal-singular-locus codimension Theorem 9.38.3 (3F94BF9B4F4B, lines 55–87), and codimension-two meromorphic extension Theorem 9.38.5 (F35BA7139EC4, lines 89–111) in docs/sections/normal-spaces-and-tube-continuation--continuation-on-normal-complex-spaces/index.html, blob fa09a923ef076a99d638d038020ddd3b884afaa7. The prior global-second-countability issue in §9.4.6 is not automatically applicable to this section, which *explicitly imposes* second countability. Hartogs bounded extension, coherent module kernels, proper analytic images, resolution and Remmert–Stein are conditional dependencies, not newly certified.
- **§9.39:** reviewed Poisson/Schwarz-disc Fourier expansion (lines 10–23), moment open-closed argument (42–60), compressed Hilbert-transform bound (68–92), convex-fiber gluing of the Bochner theorem (105–147), and the conic real/imaginary equations and compactness in Proposition 9.39.10 (tag 08FF9CEC303A, lines 152–177). No new false statement claimed.
- **§12.24:** independently checked the Gauduchon current-subtraction sign, integer torus-volume example and negative-intersection non-nef residual, with cited fractional/oscillatory and ruled-surface prerequisites not reproved. §12.2 was a definition/concavity crosscheck only.

**Coverage discipline.** New selected proof review of exactly §§9.38, 9.39 and 12.24; §9.37 heading is orientation only. Preserve the 747-row actual table of contents and older resolved/unresolved/deferred ledger. No source, registry, permanent-tag, main, publication, CI, build or formalization changes; no software tests were executed. The user-excluded approximation/regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme remains **deferred-by-user**, not resolved or certified.
