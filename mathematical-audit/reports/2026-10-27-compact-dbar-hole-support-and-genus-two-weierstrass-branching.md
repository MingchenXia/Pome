# 2026-10-27 — Support geometry of compact \(\bar\partial\) primitives and the genus-two Weierstrass branch divisor

**Pinned mathematical reading edition:** \`main\` at \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Review branch:** \`review/mathematical-audit\` (append-only historical ledger, not a source correction). This is **selected proof-level review**, not verification of an entire section or of every upstream result.

## Exact inspected integrated sources and boundaries

1. \`docs/sections/complex-homotopy-operators-and-hartogs-extension/index.html\`, blob \`e0aea9511e5f9e427463ae94002b38da8919ac94\`: §5.49.1, original source ID \`klimek-pluripotential-theory-4FD27637\`, permanent tag \`7ACDC1AF162C\`, physical lines 10–39; Theorem 5.49.4, source \`klimek-pluripotential-theory-411BC839\`, permanent tag \`4DB91EC236EA\`, lines 110–125; Hartogs Theorem 5.49.5, source \`klimek-pluripotential-theory-8068BB5B\`, tag \`5617D4B2FDA2\`, lines 128–138. Read the actual kernel normalization, degree-zero homotopy identity, compact-support argument, and use of the connected complement.
2. \`docs/sections/compact-curves-periods-and-complex-tori--divisors-and-riemann-roch-on-a-compact-curve/index.html\`, blob \`58c04d3cf4408fcdb140162e03a9052d3620610a\`: Lemma 10.78.4, source \`demailly-complex-geometry-EC096580\`, tag \`F25B73A1DFD0\`, lines 51–71; Riemann–Roch Theorem 10.78.9, source \`demailly-complex-geometry-B4C3A1F9\`, tag \`7F8CC797059F\`, lines 133–163; gap Corollary 10.78.14, source \`demailly-complex-geometry-D8F613F4\`, tag \`5A3D6AC0AA3E\`, lines 189–206; Riemann–Hurwitz Corollary 10.78.16, source \`demailly-complex-geometry-E01C6B43\`, tag \`0DB2FC824E28\`, lines 222–238; Wronskian Theorem 10.78.17, source \`demailly-complex-geometry-39122754\`, tag \`BE4F0C047320\`, lines 240–289.
3. \`docs/sections/compact-curves-periods-and-complex-tori--integral-periods-picard-tori-and-albanese-maps/index.html\`, blob \`81ec78509629e15d648cfd3b686fe4d691437330\`: Theorem 10.79.13, source \`demailly-complex-geometry-A929CFA1\`, permanent tag \`06A0A5883E2F\`, lines 216–239, **only** its simple-pole/degree-one-map criterion and genus-zero comparison. No wholesale verification of Jacobian/Albanese theory.

**Repeated-finding guard:** examined the existing \`LEDGER.md\` for genus-two Weierstrass weights, six Weierstrass points, and compact \(\bar\partial\)-primitive hole support. No matching stable finding was found. The older hyperelliptic positive-bundle example is a different theorem and remains untouched.

## POME-DBAR-PRIMITIVE-HOLE-SUPPORT-001

**Severity:** low. **Status:** verified conditional deduction. **Original theorem status:** correct; not a repaired false theorem.

**Claim (precise hypotheses).** Let \(n\ge2\), \(0\le p\le n\), and let \(\alpha\in C_c^\infty(\mathbb C^n,\Lambda^{p,1})\) satisfy \(\bar\partial\alpha=0\). Put \(F=\operatorname{supp}\alpha\), \(u=K\alpha\) for the exact convolution homotopy \(K\) of §5.49.1, and let \(U_\infty\) denote the unique unbounded connected component of \(\mathbb C^n\setminus F\). Then
\[
\boxed{\bar\partial u=\alpha,\qquad
 \operatorname{supp}u\subset\mathbb C^n\setminus U_\infty.}
\]
In particular, if \(\mathbb C^n\setminus F\) is connected, then \(\operatorname{supp}u\subset F\). The latter assertion **cannot** be imposed without a connected-complement hypothesis.

**Proof.** The degree-one homotopy identity gives
\(\bar\partial K\alpha+K\bar\partial\alpha=\alpha\), hence \(\bar\partial u=\alpha\). Smooth compactly supported input makes \(u\) smooth (§5.49.1). Outside \(F\) we have \(\bar\partial u=0\), so every coefficient of the \((p,0)\)-form \(u\) is holomorphic there. The printed proof of §5.49.4 proves that \(u\equiv0\) on \(\{|z|>R\}\) for any sufficiently large ball containing \(F\): fix \(n-1\) coordinates beyond the support radius, apply one-variable Liouville in the remaining coordinate to each coefficient, and use analytic continuation on the exterior of the ball. Since the exterior of every Euclidean ball in real dimension \(2n\ge4\) is connected, all points sufficiently far out lie in the same component \(U_\infty\). A holomorphic coefficient vanishing on this nonempty open subset of \(U_\infty\) vanishes everywhere on that connected component by the identity theorem. The complement of \(U_\infty\) is a closed subset contained in a sufficiently large ball, hence compact. This proves the support inclusion and the connected-complement specialization.

**Sharp bounded-hole witness.** Choose \(\chi\in C_c^\infty(\mathbb C^n)\) with \(\chi=1\) on \(\{|z|\le1\}\), \(\chi=0\) on \(\{|z|\ge2\}\), and nonconstant radial transition in \(1<|z|<2\). Take \(\alpha=\bar\partial\chi\), a compactly supported smooth closed \((0,1)\)-form with support in the annulus. Because \(K\chi=0\) in antiholomorphic degree zero, applying the homotopy to compactly supported \(\chi\) gives
\[
K\alpha=K\bar\partial\chi=\chi.
\]
Thus the *canonical* solution equals one in the inner ball, a bounded complementary component disjoint from \(\operatorname{supp}\alpha\). It is impossible to claim \(\operatorname{supp}K\alpha\subset\operatorname{supp}\alpha\) in general. The same example works in bidegree \((p,1)\) by tensoring with a constant holomorphic \(p\)-form.

**Proposed disposition and dependents.** Add an optional support-localization corollary after Theorem 5.49.4, explicitly with the connected-complement qualification; Theorem 5.49.4 and Hartogs Theorem 5.49.5 need **no** correction. Relevant to compact \(\bar\partial\) primitives, Hartogs cutoff support, and local-to-global gluing. The homotopy identity, Liouville/identity theorems, and the printed compact-support argument are upstream inputs; no general \(\bar\partial\) theory has been certified here.

## POME-GENUS2-WEIERSTRASS-BRANCH-001

**Severity:** low. **Status:** verified conditional deduction. **Original theorem status:** correct.

**Claim.** On every connected compact Riemann surface \(X\) of genus \(2\), there are **exactly six distinct Weierstrass points**, each of Wronskian weight precisely \(1\). For any one of them \(a\), there exists a meromorphic function of degree \(2\) on \(X\), defining a branched double cover \(f:X\to\mathbb P^1\), whose complete ramification locus is exactly this six-point set. Every ramification point is simple (local mapping degree \(2\)).

**Proof.** By Theorem 10.78.17, at each point the two gaps \(s_1<s_2\) lie in \(\{1,2,3\}\), and the Wronskian weight is \(\mu_a=s_1+s_2-3\). The integer \(1\) must be a gap at every point of a positive-genus curve. Indeed, a nongap \(1\) would give a nonconstant meromorphic function having a single simple pole. The simple-pole criterion explicitly proved in §10.79.13 makes that function a biholomorphism \(X\simeq\mathbb P^1\), contradicting genus \(2\). Consequently
\[
(s_1,s_2)\in\{(1,2),(1,3)\},\qquad
\mu_a\in\{0,1\}.
\]
Theorem 10.78.17 also gives \(\sum_a\mu_a=g(g+1)(g-1)=6\). Hence **exactly six** points have \(\mu_a=1\); all others have zero weight.

Fix a weight-one point \(a\). Its gaps are \(1,3\), so \(2\) is a nongap (Corollary 10.78.14 or formula 10.78.19). There is thus a meromorphic \(f\) with a unique pole, of order exactly \(2\), at \(a\). As a map \(f:X\to\mathbb P^1\), its degree is \(2\) by the constant-fiber-degree argument of Corollary 10.78.16, applied to the fiber at infinity. In particular \(e_a=2\). The Riemann–Hurwitz formula yields
\[
2g_X-2=2(2g_{\mathbb P^1}-2)+\sum_x(e_x-1)
\quad\Longrightarrow\quad
\sum_x(e_x-1)=6.
\]
Every ramification point of a degree-two map has \(e_x=2\), so there are six distinct ramification points. Let \(b\) be any one of them. If \(b=a\), then the original function \(f\) already has its unique pole of order two at \(b\). Otherwise \(f(b)\in\mathbb C\), and the degree-two fiber formula gives \(f^{-1}(f(b))=2[b]\); consequently the meromorphic function \(1/(f-f(b))\) has precisely one pole of order two, at \(b\). In either case \(2\) is a nongap at \(b\), so \(b\) is a Weierstrass point of weight one. There are six such ramification points and exactly six weight-one points; the two sets coincide. All assertions follow.

**Proposed disposition and dependents.** Optional compact genus-two corollary to Theorem 10.78.17, referring internally to Corollaries 10.78.14, 10.78.16 and §10.79.13. The printed Wronskian/gap formula is not erroneous. This corollary identifies the branch set of any degree-two model and is relevant to curve examples, canonical maps and hyperelliptic constructions. The Riemann–Roch/Serre duality input and the existing Wronskian theorem remain **conditional mathematical prerequisites**, not independently re-proved in full.

## POME-POINT-SHEAF-FINITE-CECH-ACYC-001

**Severity:** low. **Status:** verified conditional deduction. **Original Lemma 10.78.4 status:** correct. The conclusion here is *finite-cover Čech acyclicity*, not an unproved general identification with derived sheaf cohomology.

**Claim.** For the sheaf \(F(U)\) of locally finitely supported assignments \(a_x\in A_x\) from Lemma 10.78.4, and **any finite open cover** \(\mathcal U=(U_i)\) of a compact smooth manifold, every alternating Čech \(q\)-cocycle with \(q\ge1\) is a coboundary.

**Proof.** Choose a smooth partition of unity \((\rho_i)\) with \(\operatorname{supp}\rho_i\Subset U_i\), and choose \(k(x)\) with \(\rho_{k(x)}(x)>0\). For a \(q\)-cocycle \(c\) set, for \(x\in U_{i_0}\cap\cdots\cap U_{i_{q-1}}\),
\[
 b_{i_0\ldots i_{q-1}}(x)=c_{k(x),i_0,\ldots,i_{q-1}}(x).
\]
This is defined because \(x\in U_{k(x)}\). It is a locally finitely supported assignment: near any \(x_0\), indices with \(x_0\notin\operatorname{supp}\rho_k\) cannot occur after shrinking, and for each of the finitely many remaining \(k\), \(x_0\in U_k\) and the support of \(c_{k,i_0,\ldots,i_{q-1}}\) is locally finite there. The union of these finitely many supports is locally finite. Finally the cocycle identity on \((k(x),i_0,\ldots,i_q)\) reads
\[
0=(\delta c)_{k,i_0,\ldots,i_q}
=c_{i_0,\ldots,i_q}-(\delta b)_{i_0,\ldots,i_q},
\]
so \(\delta b=c\). For \(q=1\) this specializes exactly to the printed §10.78.4 proof. **No claim of derived-sheaf \(H^q(X,F)=0\) for \(q>1\)** is made without also checking the relevant higher-degree Čech comparison theorem.

**Proposed disposition and dependents.** Optional extension of the explicit principal-parts Čech argument to all positive Čech degrees; relevant to sheaves of divisors, principal parts and finite-point support. Does not replace the original result or introduce an external theorem.

## Scope, dependencies and editorial constraints

Actual new selected proof-level coverage: §5.49.1 and 5.49.4–5, §10.78.4/.9/.14/.16/.17, and §10.79.13 **only the cited simple-pole paragraph**. Three previously inventory-only ToC rows gain selected coverage. We checked the exact integrated reading edition, not merely source theorem titles. No theorem is declared false, no proof is called complete beyond its displayed and cited conditional inputs, and no original permanent tag is changed. No software build, CI, formal proof, full section certification or website publication was performed.

The owner's excluded Demailly approximation/regularization and dedicated Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof-completion programme was **not opened or extended**. Its historical audit statuses remain **deferred-by-user**, neither resolved nor certified. All changes in this commit are audit Markdown on the review branch only.
