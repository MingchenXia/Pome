# 2026-10-28 audit: Newton polyhedra of monomial multiplier ideals and the sharp elliptic relative-embedding power

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting audit HEAD:** 3c8eab9c71d11875033be6435db7ef5e61bcf4f2.

**Scope:** new selected §6.12 monomial model; independent incremental §9.71 elliptic-family sharpness. Neither is an error in the printed theorem. No entire section or complete dependency chain is certified. The user-excluded Demailly approximation/regularization and dedicated Bergman, weighted \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion tasks remain **deferred-by-user**, neither reopened nor resolved.

## POME-MONOMIAL-NEWTON-MULTIPLIER-001

**Severity:** low. **Status:** verified conditional deduction: a complete independent analytic model, not a proof of all general cases.

**Integrated anchors:** Theorem **6.12.8**, source **foundations-of-pluripotential-theory:17D7A591**, reader tag **5BA222439952**; strict divisor inequality **Eq. 6.12.9**, source **foundations-of-pluripotential-theory:DD8A324C**, tag **2874465D0AEF**; sheaf formula **Eq. 6.12.10**, source **foundations-of-pluripotential-theory:6DB88FC2**, tag **784A47900871**; Example **6.12.19**, source **foundations-of-pluripotential-theory:C4F4BAF9**, tag **B10A1F1C864B**. Exact reading-edition path: **docs/sections/lelong-numbers-and-multiplier-ideals--birational-change-of-variables-and-logarithmic-thresholds/index.html**, blob **5336b9d58df5b21518d7436a7c42d2d7be253340**, physical lines **137–171, 291–294**. Theorem 6.12.8 employs Hironaka log resolution (permitted), but the following direct model does not.

**Claim and hypotheses.** Let \(\mathfrak a=(z^{a^{(1)}},\ldots,z^{a^{(s)}})\subset\mathcal O_{\mathbb C^n,0}\) be a nonzero monomial ideal, with \(a^{(j)}\in\mathbb N^n\), \(c>0\), and
\[
\phi=c\log\left(\sum_{j=1}^s|z^{a^{(j)}}|^2\right),
\qquad
P=\operatorname{conv}\{a^{(1)},\ldots,a^{(s)}\}+\mathbb R_{\ge0}^n.
\]
The multiplier ideal in the Pome convention \(|f|^2e^{-\phi}\in L^1_{\mathrm{loc}}\) is exactly
\[
\boxed{
\mathcal I(\phi)_0
=\big(z^b:\ b\in\mathbb N^n,\quad b+\mathbf1\in\operatorname{Int}_{\mathbb R^n}(cP)\big).
}
\]
This is **ordinary full-dimensional interior** and strict inequality on all lower supporting facets, not relative interior of an individual compact face.

**Proof (without regularization or weighted \(L^2\) arguments).** In a sufficiently small product of coordinate discs, set \(t_i=-\log|z_i|^2\), so \(t_i\ge T\). Integrating over angular variables, the radial integrand for the monomial \(z^b\), up to uniform positive multiplicative constants, is
\[
\exp[-F_b(t)]\,dt_1\cdots dt_n,\quad
F_b(t)=\langle b+\mathbf1,t\rangle-c\min_{1\le j\le s}\langle a^{(j)},t\rangle.
\]
Indeed,
\[
e^{-\min_j\langle a^{(j)},t\rangle}
\le\sum_j e^{-\langle a^{(j)},t\rangle}
\le s\,e^{-\min_j\langle a^{(j)},t\rangle},
\]
and the Euclidean complex polar Jacobian contributes \(e^{-\sum_i t_i}\) times a fixed positive factor.

The continuous positively homogeneous piecewise linear function \(F_b\) has a uniform strictly positive linear lower bound on the nonnegative cone if and only if
\[
\langle b+\mathbf1,v\rangle
>c\min_j\langle a^{(j)},v\rangle
\quad\text{for every }v\in\mathbb R_{\ge0}^n\setminus\{0\}.
\]
Compactness of the unit-direction simplex gives \(F_b(t)\ge\delta\|t\|\) for some \(\delta>0\), and therefore integrability. By the supporting-halfspace representation of the unbounded Newton polyhedron \(P\), the strict inequalities are equivalent to \(b+\mathbf1\in\operatorname{Int}(cP)\).

Conversely, if \(F_b(v)<0\) for any nonzero \(v\ge0\), a narrow solid cone of radial directions gives exponential divergence. If \(F_b(v)=0\), the positive homogeneity and global Lipschitz bound on the finite piecewise linear function imply that \(F_b(sv+w)\) stays uniformly bounded above for \(s\to\infty\) and \(w\) in a sufficiently small fixed full-dimensional transverse ball centered at a positive vector. The resulting infinite cylinder eventually lies inside the shifted positive cone, has infinite Euclidean measure, and supplies divergence. Therefore the strict inequality is necessary even at the endpoint.

For an arbitrary holomorphic germ \(f(z)=\sum_{b\in\mathbb N^n}c_bz^b\), angular orthogonality and Tonelli yield a nonnegative sum of monomial radial integrals \(|c_b|^2I_b\). Consequently, every exponent in the support of an integrable \(f\) must satisfy the strict Newton condition. The allowed exponents form an upward-closed subset of \(\mathbb N^n\) with finitely many minimal elements (Dickson's lemma). Regroup the absolutely convergent Taylor series of \(f\) by one of these finitely many monomial divisors, on a smaller polydisc. Thus \(f\) belongs to the corresponding finitely generated monomial ideal. Its generators have integrable weighted squared norms, and the holomorphic coefficient germs are locally bounded, so every element of that ideal is integrable. This proves the boxed equality for all holomorphic germs, not just monomial tests.

**Numerical endpoint.** For \(\mathfrak a=(x^2,y^3)\) the Newton polyhedron is
\[
P=\{(u,v)\in\mathbb R_{\ge0}^2:u/2+v/3\ge1\},
\]
and
\[
x^py^q\in\mathcal I\big(c\log(|x|^4+|y|^6)\big)_0
\iff\frac{p+1}{2}+\frac{q+1}{3}>c.
\]
The constant function is integrable precisely when \(c<5/6\): the log canonical threshold is \(5/6\), and the constant fails at equality. At both \(c=5/6\) and \(c=1\) the multiplier ideal equals \((x,y)\). This tests the printed strict \(>\) sign and the essential log-discrepancy \(+1\) shift. The published Theorem 6.12.8 and Example 6.12.19 are **correct**.

**Proposed correction/action and dependents:** optional self-contained Newton monomial example for §6.12 and the §§6.54, 16.6 discussion of analytic-singularity multiplier jumps; preserve statement, historical attribution and permanent labels. No theorem-body correction, no certification of all resolutions, and no attempt to restart the deferred Demailly proof programme.

## POME-RELATIVE-ELLIPTIC-POWER-OPTIMAL-001

**Severity:** low. **Status:** verified conditional deduction: an exact sharpness model for a correct integrated lemma.

**Integrated anchors:** Lemma **9.71.1**, source **cao-paun-foliations:4BE67CB0**, tag **A53CEC220C70**; reading-edition file **docs/sections/local-projectivity-from-relative-positivity/index.html**, blob **f17614b598855bda6fc15f266135d6fe238638cf**, physical lines **8–11, 17–36**. Named internal input is Theorem **10.78.9** (Riemann–Roch for a line bundle), tag **7F8CC797059F**, **docs/sections/compact-curves-periods-and-complex-tori--divisors-and-riemann-roch-on-a-compact-curve/index.html**, blob **58c04d3cf4408fcdb140162e03a9052d3620610a**, lines **133–145**. Its complete general proof is not reaudited here.

**Sharpness statement.** Let \(E\) be a compact elliptic curve and \(L\) a holomorphic line bundle of degree one with a smooth positive curvature metric. Define the proper holomorphic submersion \(p:E\times\Delta\to\Delta\) and \(A=\operatorname{pr}_E^*L\). These satisfy the printed vertical positivity assumptions. The smallest integer \(k>0\) for which a closed relative projective embedding \(G:E\times\Delta\hookrightarrow\mathbb P^N\times\Delta\) can satisfy \(G^*\mathcal O_{\mathbb P^N}(1)=A^k\) is **exactly \(k=3\)**.

**Proof.** Since \(K_E\simeq\mathcal O_E\), Riemann–Roch and the absence of sections of a negative-degree line bundle give, for \(k\ge1\),
\[
h^0(E,L^k)=k,\qquad h^1(E,L^k)=0.
\]
Any morphism to projective space with pullback \(\mathcal O(1)=L^k\) is defined by a basepoint-free linear subsystem of \(H^0(E,L^k)\); the image lies in a linear space of projective dimension at most \(k-1\). For \(k=1\) such an embedding is impossible (one global section vanishes at a point and gives no basepoint-free subsystem). For \(k=2\), the image lies in \(\mathbb P^1\), and a compact elliptic curve cannot embed into \(\mathbb P^1\). This remains true even when the target dimension \(N\) is arbitrarily large.

For \(k=3\), and arbitrary distinct \(x,y\in E\), Riemann–Roch gives
\[
h^0(L^3)=3,\qquad
h^0(L^3(-x))=2,\qquad
h^0(L^3(-x-y))=1,\qquad
h^0(L^3(-2x))=1.
\]
The first dimension drop gives basepoint-freeness, the second separates points, and the last separates first jets. Thus the complete linear system \(|L^3|\) embeds \(E\) as a smooth plane cubic into \(\mathbb P^2\). Taking its product with the identity of \(\Delta\) is a closed relative embedding with the asserted pullback identity. Hence the existential high-power requirement in Lemma 9.71.1 **cannot** be replaced by \(k=1\) or \(k=2\), even for a trivial family.

**Proposed action and dependents:** an optional relative Kodaira sharpness example at §9.71, preserving the existing lemma and source tags. The full proof in families still quotes Grauert's precise proper base-change theorem and a pre-existing vanishing result: those are **not** independently proved by this model. The excluded weighted \(L^2\) proof completion is not reopened.

## Actual coverage and preserved audit boundaries

**First selected direct model in previously inventory-only §6.12:** Theorem 6.12.8 and its two display equations and Example 6.12.19. §6.12.4 was consulted only for change-of-variables conventions. **Incremental, not first, selected model in §9.71:** the exact elliptic-fiber power threshold. **Internal/contextual only:** §10.78.9 and §7.1's current Bedford–Taylor introductory normalization (path **docs/sections/bedford-taylor-products-and-local-capacity/index.html**, blob **41bc964bad8bf8505892c2cb3762e5cce2071ae6**, lines **7–13**). The latter is *not* counted as first theorem-proof coverage.

The live table of contents retains **25 chapters and 747 numbered section rows**, with **zero** entire sections or chapters certified. Every previous confirmed error, proof gap, external dependency and conditional repair retains its status. All user-deferred Demailly approximation/regularization and dedicated Bergman, weighted \(L^2\), Ohsawa–Takegoshi, multiscale atlas and positivity-loss proof-completion work stays **deferred-by-user**. No production main, manuscript body, source repository, registry, canonicalization, permanent tags, published website, builds, software tests, GitHub Actions, or formal proofs changed.
