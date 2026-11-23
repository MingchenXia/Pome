# Direct review: classical subharmonic limits, Kähler \(C^{1,1}\) envelopes, and boundary questions — 2026-11-23

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Audit branch:** review/mathematical-audit. Reading-edition pages are read from this exact main, not reconstructed solely from source titles. This report records a **verified conditional deduction**, not a false original theorem or a certificate for the complete dependency chain. Historical first-visit status is **LEGACY-UNRECONCILED**.

## POME-SH-HARTOGS-L1-SHARP-UPPER-001 — sharp quantitative one-sided Hartogs modulus

**Classification:** low / **verified conditional deduction**. No printed theorem error. The additional \(C^{1,1}\) hypothesis on the limiting function is essential for the stated quadratic modulus; the qualitative original Hartogs theorem is correctly stated.

**Anchors:** **docs/sections/subharmonic-functions/index.html**, blob **3d06e9703f2eb184cf63a2c45524ed6acbeeebd2**, §3.4.12(2), original source label **foundations-of-pluripotential-theory:7E2C1398**, permanent tag **E76E281548A5**, physical lines 219–239 and 260–273 (radial mollification); §3.4.20 (Hartogs), original label **foundations-of-pluripotential-theory:CAECA7D8**, permanent tag **5784B80133BF**, lines 418–456; sharpness uses an independent smooth local construction, not the existing §3.4.24 example as a supposedly new finding.

### Precise statement

Let \(\Omega\subset\mathbb R^d\) be open, \(K\Subset U\Subset\Omega\), and let \(u\in\mathrm{SH}(\Omega)\cap C^{1,1}(U)\). Let \(v\in\mathrm{SH}(\Omega)\cap L^1_{\rm loc}(\Omega)\). Put
\[
\delta_U(v,u)=\int_U|v-u|\,dx.
\]
Then there exist \(C>0,\delta_0>0\), depending only on \(d,K,U\), a chosen fixed smooth radial probability mollifier, and a local \(C^{1,1}\) bound for \(u\), such that
\[
\boxed{\ \sup_K(v-u)\le C\,\delta_U(v,u)^{\,2/(d+2)}
\quad\text{whenever }0\le\delta_U(v,u)\le\delta_0.\ }
\]
The supremum is a **one-sided pointwise** bound; \(v\) may take \(-\infty\) values. No symmetric \(L^\infty\) estimate is claimed.

### Self-contained justification

Choose \(\rho\in C_c^\infty(B(0,1))\), nonnegative, radial, \(\int\rho=1\), and write \(\rho_t(y)=t^{-d}\rho(y/t)\). Let \(r=\operatorname{dist}(K,\mathbb R^d\setminus U)>0\). For every \(x\in K\) and \(0<t<r\), the submean/mollifier formula §3.4.13 gives
\[
v(x)\le(v*\rho_t)(x).
\]
Set \(L=\operatorname{Lip}_U(\nabla u)\), interpreted locally on the \(t\)-balls within \(U\). The second-order Taylor remainder along the segment from \(x\) to \(x-y\), together with the vanishing first moment of radial \(\rho\), yields
\[
(u*\rho_t)(x)-u(x)
\le \frac L2t^2\int_{\mathbb R^d}|z|^2\rho(z)\,dz=:A t^2.
\]
The \(L^1(U)\) estimate gives
\[
|((v-u)*\rho_t)(x)|\le \|\rho\|_\infty t^{-d}\delta_U(v,u)=B\,\delta_U(v,u)t^{-d}.
\]
Consequently
\[
\sup_K(v-u)\le A t^2+B\,\delta_U(v,u)t^{-d}.
\]
For \(0<\delta_U\le\delta_0:=\min(1,(r/2)^{d+2})\), take \(t=\delta_U^{1/(d+2)}<r\). This proves the displayed estimate with \(C=A+B\). If \(\delta_U=0\), the pointwise uniqueness of the canonical subharmonic representative in §3.4.12(2), applied on \(U\), shows \(v=u\) there. No assumption of sequential compactness or exchange of unrelated limits enters this deduction.

### Optimality of the exponent

Let \(\Omega=B(0,2)\), \(U=B(0,1)\), \(K=\overline{B(0,1/2)}\), and \(u(x)=|x|^2\). Choose any \(\phi\in C_c^\infty(B(0,1))\) with \(\phi\ge0\) and \(\phi(0)=1\). Choose \(a>0\) so small that
\[
2d+a\inf_{\mathbb R^d}\Delta\phi\ge0.
\]
For \(0<\varepsilon<1/2\), set
\[
v_\varepsilon(x)=|x|^2+a\varepsilon^2\phi(x/\varepsilon).
\]
Then \(\Delta v_\varepsilon=2d+a\Delta\phi(x/\varepsilon)\ge0\), so each \(v_\varepsilon\) is smooth subharmonic, and
\[
\delta_U(v_\varepsilon,u)=a\varepsilon^{d+2}\int\phi,\qquad
v_\varepsilon(0)-u(0)=a\varepsilon^2.
\]
Therefore no uniform replacement by \(\delta_U^\gamma\) with any \(\gamma>2/(d+2)\) can hold even for a **fixed smooth strictly subharmonic** \(u\) and smooth \(v_\varepsilon\), with uniformly bounded real Hessians. The exponent, though not a sharp numerical prefactor, is optimal.

The one-sided nature is also necessary: existing Example §3.4.24 produces bounded increasing subharmonic functions converging in \(L^1\) to zero but remaining \(-1\) at the origin. This example is **not** a new finding and is **not** asserted to establish the positive-spike exponent.

**Proposed optional improvement:** record this as a separate quantitative corollary after §3.4.20, explicitly requiring a \(C^{1,1}\) limit and local \(L^1\) control; retain all original tags and the unrestricted qualitative theorem. **Potential dependents:** local quantitative upper-envelope and obstacle-comparison estimates using Hartogs convergence, but none becomes fully certified merely from this corollary.

## Other direct mathematical checks

### §3.4 — entire current direct mathematical section (physical lines 7–544)

Reviewed the **actual** integrated submean/comparison argument, decreasing upper-semicontinuous continuous majorants (§3.4.4), componentwise local integrability (§3.4.8), monotone convergence (§3.4.9), Riesz measures and pointwise representatives (§3.4.11–14), convexity in dimension one (§3.4.15), Hartogs compactness (§3.4.17–20), Choquet selection for uncountable families (§3.4.22–23), and polar removal (§3.4.27). Checked signs of \(\Delta E_d=\delta_0\) and \(\Delta\log|f|=2\pi\sum\operatorname{ord}_a(f)\delta_a\), the monotonicity direction of spherical means and radial mollifiers, local-versus-global components, and almost-everywhere-to-pointwise uniqueness. No new confirmed original error or transitive proof-chain certificate.

A crucial dependency boundary is Weyl's lemma §3.1.11 and distributional positivity §2.5.6 in the Riesz and canonical-representative steps; their **entire** proofs have not been re-certified in this run.

### §16.16 — entire current direct mathematical section (physical lines 5–242)

**docs/sections/envelopes-and-model-potentials--measures-on-contact-sets--real-hessian-bounds-for-kahler-envelopes/index.html**, main blob **011d45c646798edaf993db9e1dc2821d756b4161**; Lemma **16.16.1**, original source **foundations-of-pluripotential-theory:C7639230**, permanent tag **C8D21E3D949A**, lines 35–208; Theorem **16.16.7**, original source **foundations-of-pluripotential-theory:6355DEDC**, permanent tag **4B6432E0991B**, lines 213–242.

Read the real/complex Hessian trace convention \(g_0=2\operatorname{Re}(k_{i\bar j}dz_i\otimes d\bar z_j)\) and \(\operatorname{tr}_{g_0}\nabla^2b=2D_kb\), largest-eigenvalue perturbation by a rank-\((2n-1)\) projection, the positive third-derivative spectral term, differentiations of \(\log\det G\), and the \(U+R-N\) absorption with parameter \(\varepsilon\). Verified the local estimate is conditional on the preceding penalized-equation existence and uniform trace estimate, not a free-standing proof of them. In the theorem's multi-obstacle step, the log-sum-exp Hessian has **negative** variance, giving a uniform **upper** Hessian bound despite no common lower Hessian bound; passage to the \(C^{1,1}\) limit uses distributional second derivatives. No new false statement or asserted full upstream proof certificate.

**Selected prerequisite checks only:** Lemma §16.15.7, original tag **EA811ACFD26E**, **docs/tag/EA811ACFD26E/index.html**, blob **d94d38ba821375b57206f04bedf5c2d679c61fb3**, lines 6–64; specifically the \(\beta\)-independent upper trace estimate for \(\beta>\beta_0\). The existence theorem §16.15.20, elliptic \(W^{2,p}\) input §16.14.9, and Morrey §2.9.16 are not wholly certified.

### §§24.5 and 24.6 — complete current explanatory/problem text, not proof certifications

- **§24.5:** **docs/sections/problems-in-hermitian-pluripotential-theory--closed-and-twisted-classes/index.html**, main blob **eed47dda4235b5db713fe1c6c6fcea777ee9b674**, physical lines 7–34. Checked the distinction between closed Bott–Chern representative invariance and twisted LCK/Lee classes; threshold and divisorial trace conditions are stated conditionally. The unrestricted radial-to-general LCK uniqueness, pseudoeffectivity, and Vaisman existence questions remain open. These are cross-chapter summaries, not new independent theorem proofs.
- **§24.6:** **docs/sections/problems-in-hermitian-pluripotential-theory--degeneration-orders-and-finite-distance-boundaries/index.html**, main blob **692b010fe882c30c0a612f07e29e0d2fb3307a23**, physical lines 7–33; Problem **24.6.1**, permanent tag **B93ADA1B6064** at line 20. The degeneration-order \(\epsilon\downarrow0\) direction, volume-radius separation and specified finite-dimensional cone hypotheses were checked. The metric completion is explicitly an **open problem** in general; the invariant and warped-product cases are conditional references, not a general solution.
- **Selected prerequisite check:** Proposition **12.6.1**, permanent tag **88C1708A920C**, **docs/tag/88C1708A920C/index.html**, blob **ade2ef67aac505778d0e4e194efd663abc6f166b**, physical lines 6–41: homogeneity \(\lambda(s\theta)=s\lambda(\theta)\), the radial identity \(g_\theta(\theta,\chi)=D\log\lambda_\theta(\chi)\), and exact distance splitting under the **specified finite-dimensional** setting. The Lie-group and warped-cone classification theorems §12.6.12/26/41 are not independently re-proved this run.

## Scope, ledgers, and deferred material

**Direct current mathematical sections:** 2 (§3.4, §16.16). **Entire current explanatory/problem sections:** 2 (§24.5, §24.6). **Selected prerequisite statements:** 2 (§16.15.7, §12.6.1). **New low verified conditional deductions:** 1. **New confirmed original errors:** 0. **Full transitive proof-chain certificates:** 0. Earlier reports and their stable finding IDs are not reopened or relabeled as new. The established 747-number chapter/section matrix is retained, with only the four audited status rows updated.

**Excluded without inspection:** Demailly approximation/regularization, and dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programmes. Earlier work on these remains **deferred-by-user**, neither resolved nor certified. No tests, builds, GitHub Actions CI, source/body edits, registry/canonicalization edits, permanent-tag changes, merges, or publication were carried out.
