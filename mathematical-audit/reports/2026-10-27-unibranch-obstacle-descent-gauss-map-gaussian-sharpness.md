# 2026-10-27 — Unibranch obstacle descent, strictly convex Gauss maps, and sharp Hermitian dual energy

**Reviewed current main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting audit head:** cf7cc8c49f2fd2b51bd085ae89429a9db2ad2684. **Scope:** first selected mathematical inspection of §§9.10, 9.16, 9.53, 11.49 in the integrated reading edition, not the original source alone. None of these sections or their entire dependency chains is certified. No Demailly approximation/regularization or dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas or positivity-loss proof-completion work was reopened; all its historical entries remain **deferred-by-user**.

## POME-UNIBRANCH-CONTINUOUS-OBSTACLE-DESCENT-001

**Status:** verified conditional deduction. **Severity:** low; no false printed theorem.

**Source anchors.** Main file **docs/sections/pluripotential-theory-on-unibranch-spaces/index.html**, blob **6edfa6b19fa7cdbaf0c2665389fa7b3ca338cdf4**. Theorem 9.10.5, source label **sgpt-AFDCC00F**, permanent tag **E707851D5DBA**, physical lines 39–64 (connected fibers); Theorem 9.10.13, source label **sgpt-59A3C1AA**, tag **48473380B913**, lines 126–139 (Fornæss–Narasimhan disk test); Theorem 9.10.14, label **sgpt-EEFC0C9A**, tag **C69D2F0ABA4F**, lines 140–214; Corollary 9.10.16, label **sgpt-D36D019A**, tag **2DA8FD7B7A99**, lines 216–249 (pullback bijection). The printed Corollary 9.10.16 and standard existence of continuous-obstacle psh envelopes on smooth compact Kähler manifolds are explicit conditional inputs. The earlier **POME-UNI-EXT-FN-001**, a genuine external dependency on the converse disk criterion, remains open.

**Assertion.** Let $\pi:Y\to X$ be a proper bimeromorphic morphism from a smooth compact Kähler manifold $Y$ to a connected compact unibranch Kähler space $X$. Let $\theta$ be a smooth closed real $(1,1)$-form on $X$, with $\mathrm{PSH}(X,\theta)\ne\varnothing$, and let $f\in C^0(X,\mathbb R)$. The largest $\theta$-psh minorant $P_\theta(f)$ is well defined and
$$
\boxed{\pi^*P_\theta(f)=P_{\pi^*\theta}(f\circ\pi).}
$$

**Complete deduction from the specified inputs.** Nonemptiness of $\mathrm{PSH}(X,\theta)$ gives an admissible minorant of $f$: every fixed $\theta$-psh function is bounded above on compact $X$ and can be lowered by a constant. Its pullback lies under $f\circ\pi$, so the upstairs admissible family is nonempty. On smooth compact Kähler $Y$, let $w=P_{\pi^*\theta}(f\circ\pi)$ be the upper-semicontinuous regularized supremum. It is $\pi^*\theta$-psh. **Continuity of the obstacle matters:** regularizing a family bounded by the continuous $f\circ\pi$ still gives $w\le f\circ\pi$ everywhere. By Corollary 9.10.16 there is a unique $v\in\mathrm{PSH}(X,\theta)$ with $w=\pi^*v$. Since $\pi$ is surjective, $v\le f$. For any competing $u\in\mathrm{PSH}(X,\theta)$ with $u\le f$, its pullback is a competing minorant upstairs, hence $\pi^*u\le w=\pi^*v$. Surjectivity gives $u\le v$. Thus $v=P_\theta(f)$ and the identity follows. This proof **does not interchange** pullback with usc regularization, assume sequential compactness, or manipulate the excluded regularization programme.

**Suggested placement and dependents.** Optional precise lemma near Corollary 9.10.16 and §16's obstacle-envelope definitions. It applies to continuous obstacles, not automatically to arbitrary discontinuous singular obstacles. The Fornæss–Narasimhan input and the upstream smooth-envelope existence theorem are not re-proved here.

## POME-STRICT-CONVEX-GAUSS-DIFFEO-001

**Status:** verified conditional deduction. **Severity:** low; correct printed extreme-point theorem strengthened.

**Source anchors.** Main file **docs/sections/local-convexity-and-defining-functions/index.html**, blob **55354bba1d289fc34e69e2c9746bb3cbe9b2d059**, source **klimek-pluripotential-theory**. Proposition 9.16.1, source label **klimek-pluripotential-theory-BAA922F2**, tag **3269D913190D**, lines 8–28 (closed locally convex sets); Proposition 9.16.2, source label **klimek-pluripotential-theory-C7D4500D**, tag **2822D619E8BC**, lines 30–48; Proposition 9.16.3, source label **klimek-pluripotential-theory-1E9F70D8**, tag **623CAE0176D7**, lines 50–94, read at its holomorphic quadratic correction, cutoff and cap steps. Its conclusion is not claimed to have been certified through all sources.

**Assertion.** Under all assumptions of Proposition 9.16.2, with $m\ge2$, $D\subset\mathbb R^m$ bounded and connected, $q\in C^2$ a defining function near $\overline D$, $dq\ne0$ on $\partial D$, and the real Hessian $D^2q$ positive definite on every tangent space $T_p\partial D$, every boundary point is **exposed** (not just extreme), and the outward Gauss map
$$
\nu:\partial D\longrightarrow S^{m-1},\qquad
\nu(p)=\frac{\nabla q(p)}{|\nabla q(p)|}
$$
is a **$C^1$ diffeomorphism**.

**Proof.** Proposition 9.16.2 proves convexity of $D$ and extremality of all its boundary points. At $p$, differentiability and convexity show that $H_p=\{x:\nu(p)\cdot(x-p)=0\}$ is supporting. If $r\ne p$ belongs to $H_p\cap\overline D$, convexity puts the segment $[p,r]$ inside this intersection; the supporting property puts the entire segment in $\partial D$, contradicting the extremality of $p$. Thus $p$ is exposed and $p\mapsto\nu(p)$ is injective. Any unit vector $e$ attains its support maximum $e\cdot x$ on compact $\overline D$ at some boundary point, whose exterior normal is $e$; this proves surjectivity. Along $w\in T_p\partial D=\nu(p)^\perp$,
$$
D\nu_p(w)
=\frac{(I-\nu(p)\otimes\nu(p))D^2q(p)w}{|\nabla q(p)|},
\qquad
\langle D\nu_p(w),w\rangle
=\frac{D^2q(p)[w,w]}{|\nabla q(p)|}>0\quad(w\ne0).
$$
Therefore $D\nu_p:T_p\partial D\to T_{\nu(p)}S^{m-1}$ is invertible, since both spaces have dimension $m-1$. The inverse function theorem and the bijection give a global $C^1$ diffeomorphism. A $C^2$ inverse is **not** asserted under merely $C^2$ boundary regularity.

**Suggested placement/dependents.** Optional sharpening after Proposition 9.16.2, useful for support functions, strictly convex caps and boundary normal coordinates. Not an error in the original theorem.

## POME-COMPLETE-HERM-GAUSSIAN-SHARPNESS-001

**Status:** verified conditional deduction. **Severity:** low; proves optimality of the existing constant, rather than validating all its analytic prerequisites.

**Source anchors.** Main file **docs/sections/complete-hermitian-laplacians-and-dual-energy/index.html**, blob **5bf728a2fa3b558bf7d922d30ea25a449c70b68b**, source **demailly-complex-geometry**. Corollary 11.49.2, source label **demailly-complex-geometry-456C31C4**, tag **28AC2C7FBC2B**, lines 8–23; Theorem 11.49.3, label **demailly-complex-geometry-C84B45BB**, tag **D6CB928B58CE**, hypotheses lines 25–46, energy-inequality and domain proof lines 48–69. Printed inputs are the exact torsion Bochner energy identity (11.48.19), the joint graph-core theorem and the closed-Hilbert-complex duality argument. No excluded approximation-specific L² proof is revisited.

**Sharp example.** Set $X=\mathbb C$, $\omega=i\,dz\wedge d\bar z$ (a complete flat Kähler metric) and take the trivial holomorphic line bundle $E$ with smooth Hermitian weight $|e|_h^2=e^{-\lambda|z|^2}$, $\lambda>0$. The Chern curvature and torsion satisfy $i\Theta(E)=\lambda\omega$, $T_\omega=0$; on $(1,1)$-forms $A=[i\Theta(E),\Lambda_\omega]=\lambda I$ (while the commutator is zero on $(0,1)$-forms in complex dimension one). The closed form $g=dz\wedge d\bar z\otimes e$ admits the $(1,0)$-form $u=-\bar z\,dz\otimes e$, with $\bar\partial u=d z\wedge d\bar z\otimes e=g$. Since $dV_\omega=2\,dx\,dy$ and $|dz\wedge d\bar z|_\omega^2=|dz|_\omega^2=1$,
$$
\|g\|_2^2=4\pi\int_0^\infty r e^{-\lambda r^2}\,dr
=\frac{2\pi}{\lambda},\qquad
\|u\|_2^2=4\pi\int_0^\infty r^3e^{-\lambda r^2}\,dr
=\frac{2\pi}{\lambda^2}
=\int_{\mathbb C}|g|_{A^{-1}}^2\,dV_\omega.
$$
To establish that $u$ is **minimum-norm**, note that any other solution is $u+F(z)\,dz\otimes e$ with $F$ entire and weighted $L^2$. For each $r$, the angular integral of $-\bar z\,\overline{F(z)}$ vanishes by the convergent power series of $F$: its Fourier exponents are all strictly negative. Weighted Cauchy–Schwarz makes the full integral absolutely convergent; polar Fubini therefore gives $u\perp F(z)\,dz\otimes e$. Thus every other solution has squared norm $\|u\|^2+\|F(z)\,dz\otimes e\|^2$. The universal coefficient **one** in Theorem 11.49.3 is optimal even on flat complete $\mathbb C$.

**Related conditional spectral bound.** If at a fixed degree $(p,q)$, $q\ge1$, the exact printed curvature-plus-torsion endomorphism has a global constant bound $A\ge\lambda_0 I$ with $\lambda_0>0$, the displayed energy estimate gives on the full joint graph domain
$$
\|\bar\partial v\|_2^2+\|\bar\partial^*v\|_2^2
\ge\lambda_0\|v\|_2^2.
$$
Consequently the selfadjoint Laplacian of this closed quadratic form has spectrum in $[\lambda_0,\infty)$; for distributionally closed $g$ the printed solution theorem yields
$\|u_{\min}\|_2\le\lambda_0^{-1/2}\|g\|_2$, so unreduced $L^2$ cohomology in this degree vanishes. The Gaussian example saturates the norm coefficient. **No uniform spectral gap is claimed when $\inf_X\lambda(x)=0$.**

**Suggested placement/dependents.** Optional exact sharpness example and spectral-gap consequence after Theorem 11.49.3. This report does not re-prove its transitive Bochner/graph-core/Hilbert-complex theorem chain or reopen the excluded Demailly-approximation L² project.

## Separate selected proof inspection: formal complex coordinates (§9.53)

Main file **docs/sections/formal-integrability-and-smooth-complex-coordinates/index.html**, blob **218b71104a05350a9bb37b63c64638efecbd1e42**, source **demailly-complex-geometry**. Proposition 9.53.2, label **demailly-complex-geometry-EF13FDD7**, tag **7D9D38C5DA0E**, physical lines 10–42; Lemma 9.53.5, label **demailly-complex-geometry-F9963253**, tag **30126C7FDE2C**, lines 45–76; Lemma 9.53.7, tag **53F867AC87E1**, lines 80–107. The projected bracket $[fX,gY]^{0,1}=fg[X,Y]^{0,1}$ validates tensoriality; on a $(0,1)$ covector, the $(2,0)$ part of $du$ is $-\vartheta'u$, checking the minus sign in (9.53.3). For the inductive coordinate correction, formal $d''{}^2=0$ gives $\partial_{\bar z_l}P_{jk}=\partial_{\bar z_k}P_{jl}$ at degree $s-1$. The explicit line homotopy $Q_j=\int_0^1\sum_l\bar z_lP_{jl}(z,t\bar z)\,dt$ satisfies $\partial_{\bar z_k}Q_j=P_{jk}$; the remaining term $\partial_{z_k}Q_j\,d''z_k$ has degree at least $2s\ge s+1$. The separate Levi positivity error in Lemma 9.53.7 is $O(r^{s-2})$ uniformly in $\epsilon$ for $s\ge3$. No new defect was established. **The global L² proof of Theorem 9.53.13 was not audited or certified.**

## Coverage and safeguards

Exactly four previously inventory-only ToC rows (§§9.10, 9.16, 9.53, 11.49) were upgraded to **these specified selected passages only**, not complete-section coverage. **747** unique actual ToC section IDs remain; no full section or higher dependency chain certified. Three new *low / verified conditional deduction* entries, no newly false printed theorem and no new genuine duplication. Historical external, resolved, unresolved and deferred ledgers remain unchanged, including **POME-UNI-EXT-FN-001** and every **deferred-by-user** regularization/Bergman/L²/OT/multiscale/positivity-loss item. No full build, tests, CI, formal proof verification, source/registry/tag/main mutation or website publishing.
