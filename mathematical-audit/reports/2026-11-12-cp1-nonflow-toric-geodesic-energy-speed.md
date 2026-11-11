# 2026-11-12 — non-flow toric weak geodesic on the projective line: energy and velocity laws

**Finding:** POME-GEOD-CP1-NONFLOW-TORIC-SPEED-001. **Severity:** low. **Status:** verified conditional deduction; **no printed theorem refuted**. This audits selected integrated statements and supplies an independent smooth model, not a complete upstream proof certification.

## Versioned reading-edition anchors

Reviewed main **b6933b772f41b45918f7e25ed1afbbb1fd892272**.

- docs/sections/relative-energy-and-perron-segments--energy-along-weak-geodesics/index.html, blob **8d9b7af925289346c96df751c67049e90c9dfe1d**: Lemma 17.8.1 (lines 10–40; source foundations-of-pluripotential-theory:9DEC569D; permanent 950F051CF55A), Lemma 17.8.2 (42–56; source :B2CECD86; permanent 3D0F1309E327), Theorem 17.8.3 and Steps 1–5 (58–113; source :907171A2; permanent 678A18D6D406), Eq. 17.8.4 (87–94; source :DD6D5F8C; permanent 2B3BEF6C25C1).
- docs/sections/relative-energy-and-perron-segments--relative-monge-ampere-energy/index.html, blob **16fdcc4c6a6f0cc75e69ba267bd7da2b2d7922a1**: Definition 17.3.2 (line 32; source foundations-of-pluripotential-theory:582D55DC; permanent 240EF1DE5889), energy Eq. 17.3.3 (lines 33–36; source :8C7506A6; permanent F19AAFA93177) and first-variation Eq. 17.3.5 (lines 43–45; source :A392067F; permanent 46190A7C1B2F).
- docs/sections/relative-energy-and-perron-segments--subgeodesics-and-perron-segments/index.html, blob **662f60d73fc585b6ea3b710f2a3472bac1de8a7c**: Definition 17.7.1 (lines 10–24; source foundations-of-pluripotential-theory:15664095; permanent B0604A42ABDF), Definition 17.7.7 (181–185; source :041BC264; permanent 4A0AFDAD6156), Theorem 17.7.8 (186–211; source :108758A0; permanent 2FECBE87C487), Proposition 17.7.9 (214–250; source :470B93BF; permanent DD04D189A4D3).

## Exact family and result

Let \(X=\mathbb P^1\), \(\omega=\omega_{\rm FS}=dd^c\log(1+|z|^2)\), where \(dd^c=(i/2\pi)\partial\bar\partial\) and \(\int_X\omega=1\). Fix \(0<\varepsilon<2\) and \(0\le t\le1\). With \(x=\log|z|^2\), put
\[
g_0(y)=y\log y+(1-y)\log(1-y),\qquad
g_t(y)=g_0(y)+t\varepsilon y(1-y)\quad(0\le y\le1),
\]
using continuous endpoint values, and define
\[
\psi_t(x)=\sup_{0\le y\le1}(xy-g_t(y)),\qquad
u_t(z)=\psi_t(\log|z|^2)-\log(1+|z|^2).
\]
Then \(u_t\) is globally smooth and \(\omega+dd^c u_t>0\), its joint complexification with \(t=-\log|w|\) is semipositive and solves the **smooth homogeneous complex Monge–Ampère equation** on \(X\times\{e^{-1}<|w|<1\}\). Conditional on the Perron construction of Theorem 17.7.8 (as already used by the printed Theorem 17.8.3), it is exactly the **unrestricted** weak geodesic between \(u_0=0\) and \(u_1\).

Write \(y_t=\partial_x\psi_t(x)\). For every real \(p\ge1\),
\[
\boxed{\int_X|\dot u_t|^p(\omega+dd^cu_t)
=\varepsilon^p B(p+1,p+1)
=\varepsilon^p\frac{\Gamma(p+1)^2}{\Gamma(2p+2)}}.
\]
Thus the \(L^1\) speed is \(\varepsilon/6\), the \(L^2\) speed is \(\varepsilon/\sqrt{30}\), and the \(L^\infty\) speed is \(\varepsilon/4\), all independent of \(t\). Moreover
\[
\boxed{E_\omega^0(u_t)=-\varepsilon t/6.}
\]
Unlike an automorphism-flow geodesic, its velocity \(-\varepsilon y(1-y)\) is **quadratic**, not affine, in the moment coordinate.

## Proof A: global smoothness and the joint Hessian

Since
\[
g_t''(y)=\frac1{y(1-y)}-2t\varepsilon\ge4-2\varepsilon>0,
\]
the maximizing point is unique and solves
\[
x=\log\frac y{1-y}+t\varepsilon(1-2y).
\]
The implicit function theorem gives smooth \(y=y_t(x)\) and \(\psi_x=y\). At \(z=0\), with \(s=|z|^2\), the equation becomes
\[
y=s(1-y)e^{-t\varepsilon(1-2y)}.
\]
Near \(s=y=0\), the implicit function theorem gives a smooth analytic \(y(s,t)\) with \(y_s(0,t)=e^{-t\varepsilon}>0\). Because \(\psi_s=y/s\), \(\psi_t\) extends smoothly over \(z=0\). For \(z=\infty\) put \(q=1-y\) and \(v=|z|^{-2}\); then
\[
q=v(1-q)e^{-t\varepsilon+2t\varepsilon q},
\]
and the same argument applies to \(\psi_t(x)-x\) at \(v=0\). The limiting curvature coefficients are positive. Thus \(u_t\) is a smooth global \(\omega\)-potential.

Writing \(h(y)=\varepsilon y(1-y)\), \(D=g_t''(y)>0\), implicit differentiation yields
\[
\psi_{xx}=D^{-1},\qquad
\psi_{xt}=-h'(y)D^{-1},\qquad
\psi_{tt}=h'(y)^2D^{-1}.
\]
Its joint real Hessian in \((x,t)\) is positive semidefinite and has determinant zero. In the nonzero \((z,w)\) chart, \(\partial_zx=1/z\), \(\partial_wt=-1/(2w)\); the complex Hessian of the joint local potential is a positive diagonal rescaling of this real Hessian. It therefore is positive semidefinite with zero determinant. The smooth extension over the poles gives globally
\[
(p_X^*\omega+dd^cU)^2=0.
\]
This step is classical smooth calculus and does not invoke the excluded approximation programme.

## Proof B: identification with the actual Perron envelope

The candidate is a competitor with the specified smooth endpoints. Since the endpoints and \(\omega\) are invariant under \(z\mapsto e^{i\alpha}z\), the Perron envelope \(G_t\) of Definition 17.7.7 is torus-invariant. The joint psh condition and attainment of endpoints here use the internal Theorem 17.7.8; this general theorem is **not** independently certified in this report.

Set \(\Psi(x,t)=\psi_0(x)+G_t(x)\). Torus invariance and joint psh imply joint real convexity in \((x,t)\). For every \(y\in(0,1)\) define
\[
K_y(t)=\inf_{x\in\mathbb R}\{\Psi(x,t)-xy\}.
\]
Partial minimization of a jointly convex function makes \(K_y\) convex in \(t\). The endpoint inequalities in Proposition 17.7.4 give \(\limsup_{t\downarrow0}K_y(t)\le-g_0(y)\) and \(\limsup_{t\uparrow1}K_y(t)\le-g_1(y)\), and hence
\[
K_y(t)\le-(1-t)g_0(y)-tg_1(y)=-g_t(y).
\]
Fenchel biconjugacy for each finite convex slice gives
\[
\Psi(x,t)=\sup_y(xy+K_y(t))\le\sup_y(xy-g_t(y))=\psi_t(x).
\]
Thus \(G_t\le u_t\). Since \(u_t\) is itself a competitor, the opposite inequality holds. This proves the unrestricted Perron identification **subject to the precisely named Perron upper-envelope premise**; no sequential compactness is assumed.

## Proof C: exact measure and energy normalization

Using \(z=e^{x/2+i\alpha}\) on \(\mathbb C^*\) and \(dd^c=(i/2\pi)\partial\bar\partial\),
\[
\omega_t=\omega+dd^cu_t
=\frac{\psi_{xx}(x,t)}{2\pi}\,dx\wedge d\alpha.
\]
As \(y=\psi_x\) ranges from zero to one, the pushforward \((y_t)_*\omega_t\) is **exactly Lebesgue measure** \(dy\), with no extra \(2\pi\) factor. The envelope theorem gives
\[
\dot u_t=-\varepsilon y_t(1-y_t).
\]
The exact beta integral proves the displayed \(L^p\) formula. For \(p=1,2\), the integrals are \(1/6\) and \(1/30\), respectively. These and \(g_t''\) were also checked by a small local symbolic calculation; that is not a repository test/build or mathematical certification.

For smooth \(u\), the integrated reading-edition energy formula in dimension one is
\[
E_\omega^0(u)=\tfrac12\int_Xu(\omega+\omega_u).
\]
Stokes gives \(dE(u_t)/dt=\int_X\dot u_t\,\omega_t=-\varepsilon/6\); since \(u_0=0\) and \(E(u_0)=0\), this yields \(E(u_t)=-\varepsilon t/6\). The sign and mass normalization therefore agree exactly with Theorem 17.8.3 **for this family**, not for the unsampled full generality.

## Duplication, dependencies, classification, and affected results

The 2026-11-06 finding **POME-GEO-PROJECTIVE-DIAGONAL-EXACT-001** uses a holomorphic diagonal projective flow with exponential coordinate weights and affine moment-map velocity. The present perturbation of the Legendre potential by \(\varepsilon y(1-y)\) is *not* that projective flow, and gives a continuum of nontrivial beta-distributed velocity moments. The 2026-10-29 logistic-ray moment result is likewise not re-reported as new.

**Proposed correction:** none; the selected original statements remain consistent. The calculated smooth model is independently verified; identifying it as the unrestricted weak geodesic is a **verified conditional deduction** dependent on Theorem 17.7.8. General Lemmas 17.8.1–2, the non-pluripolar multilinearity and fiber integrations in Theorem 17.8.3 (including §13.6.1 and §17.2.5), and finite-energy endpoint limits remain unverified here, *not* declared false. Affected dependents: the exact toric special case of Theorem 17.8.3 and the \(L^p\)-speed normalization; no change to any other theorem or permanent tag.

**Coverage:** §§17.3, 17.7, 17.8 were already partly reviewed; **0 first proof-level visits, 0 complete-section certifications**. Current main table of contents: **25 chapters / 747 numbered sections**. Demailly approximation/regularization and the owner's dedicated Bergman, L², OT, multiscale, and positivity-loss work remain **deferred-by-user**, not resolved. Review-only documentation; no production edits, source changes, CI, test suite, or website publication.
