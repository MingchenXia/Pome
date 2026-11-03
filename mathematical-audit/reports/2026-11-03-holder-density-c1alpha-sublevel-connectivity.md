# A sharp Hölder-density sublevel separator threshold

**Audit date:** 2026-11-03. **Production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Stable ID:** \`POME-DENSITY-C1ALPHA-SUBLEVEL-001\`. **Severity:** low. **Status:** verified conditional deduction, **not** a false printed theorem.

## Reviewed integrated edition

Main path: \`docs/sections/uniqueness-for-degenerate-equations--extrema-and-density-sublevels/index.html\`; blob \`044f55457f10b2f640052854a7f5f14b8403be82\`. Theorem 14.21.13, source \`non-kahler-pluripotential-theory:A7BC9EDB\`, permanent \`61851D05B072\`, lines 186–223. Its square-root threshold Equation 14.21.14 has source \`non-kahler-pluripotential-theory:7BB4C3AC\`, permanent \`B72083672909\`, lines 187–189. Theorem 14.21.3, source \`non-kahler-pluripotential-theory:61B8DD0F\`, permanent \`6EB399397505\`, lines 28–50 and proof 133–171. Lemmas 14.21.5/6, source \`non-kahler-pluripotential-theory:F0F5D947\` and \`non-kahler-pluripotential-theory:E67FD2CF\`, permanent tags \`59B8A4C8DA05\` and \`96D40C4808C2\`, lines 58–104. Section 14.20 background equation: \`docs/sections/uniqueness-for-degenerate-equations/index.html\`, blob \`0c1c033d7a1a76b9ccf9fbd5b4bfc8321a33f208\`, lines 7–23.

## New independently proved geometric lemma

Let \(M\) be a connected compact smooth manifold with smooth positive volume density \(dV\). Suppose \(f\geq0\) belongs to \(C^{1,\alpha}(M)\), \(0<\alpha\le1\), and set \(U=\{f>0\}\). Then
\[
\boxed{\liminf_{t\downarrow0}\frac{\operatorname{Vol}\{f\le t\}}{t^{1/(1+\alpha)}}=0\quad\Longrightarrow\quad U\ \text{connected}.}\tag{1}
\]
In particular, \(f^{-1/(1+\alpha)}\in L^1(dV)\) implies (1), with the reciprocal interpreted as \(+\infty\) on the zero set.

**Proof.** At every zero \(z\), \(\nabla f(z)=0\) because \(f\ge0\). In a sufficiently small convex coordinate ball, write \(L=[\nabla f]_{C^\alpha}\). For a segment contained in the ball,
\[
0\le f(x)=\int_0^1\langle\nabla f(z+s(x-z))-\nabla f(z),x-z\rangle\,ds
\le\frac{L}{1+\alpha}|x-z|^{1+\alpha}.\tag{2}
\]
If the ball meets both the zero set and its complement, \(L>0\). Condition (1) forces the zero set to be volume-null. If \(U\) were disconnected in a sufficiently small coordinate ball, choose points of two distinct local components and small, parallel, transverse disks about them. Every segment between corresponding disk points crosses the zero set. All crossings lie uniformly away from the endpoints because the closed disks lie inside \(U\). Equation (2) supplies, on every such segment and for **all sufficiently small** \(t>0\), a subinterval in \(\{f\le t\}\) of length \(2((1+\alpha)t/L)^{1/(1+\alpha)}\). Fubini and local equivalence of the volume density with Lebesgue measure yield a constant \(c>0\) with
\[
\operatorname{Vol}\{f\le t\}\ge c\,t^{1/(1+\alpha)}\qquad(0<t<t_0),\tag{3}
\]
contradicting (1). Hence \(U\) intersects every sufficiently small coordinate ball in a connected, nonempty set. Overlapping balls intersect in an open subset and therefore in some point outside the null zero set; connectedness of \(M\) implies connectedness of \(U\).

For \(\gamma=1/(1+\alpha)\), integrability of \(f^{-\gamma}\) implies the zero set is null and
\[
0\le t^{-\gamma}\operatorname{Vol}\{f\le t\}
\le\int_{\{0<f\le t\}}f^{-\gamma}\,dV\to0
\]
by dominated convergence. This proves the lemma.

## Conditional complex Monge–Ampère consequence

In the §14.20 setting, let \(\omega>0\) be Hermitian and \(u,v\in C^{1,1}(X)\) satisfy \(A=\omega+dd^cu\ge0\), \(B=\omega+dd^cv\ge0\) almost everywhere, and \(A^n=B^n=f\,dV\) for a nonnegative \(C^{1,\alpha}\) density. Whenever (1) holds, \(u-v\) is constant, **using as an upstream input** the integrated Theorem 14.21.3, which only needs continuity of the density and connectedness of \(U\). Theorem 14.21.13 assumes \(C^{1,1}\) density and \(C^2\) potentials; the new threshold covers the previously unchecked \(0<\alpha<1\) regime while allowing \(C^{1,1}\) potentials. The case \(\alpha=1\) reproduces its square-root exponent.

The §14.21.5 proof's exceptional-set selection is consistent: the \(C^{1,1}\) gradient is Lipschitz and maps null sets to null sets. The §14.21.6 annular barrier \(b=e^{-\lambda|x-y|^2}-e^{-\lambda r^2}\) has
\[
Lb=e^{-\lambda|x-y|^2}(4\lambda^2 a(x-y,x-y)-2\lambda\operatorname{tr}a)>0
\]
for large \(\lambda\) under uniform ellipticity, without differentiating measurable coefficients. These are **selected local proof checks**, not transitive verification of the complete theorem.

## Exact geometric sharpness and its limitation

On the flat complex \(n\)-torus \(X=(\mathbb C/(\mathbb Z+i\mathbb Z))^n\) with Haar volume one, let \(x=\operatorname{Re}z_1\bmod1\) and \(f_\alpha=|\sin(2\pi x)|^{1+\alpha}\). Then \(f_\alpha\in C^{1,\alpha}\), its zero set consists of the two real hypersurfaces \(x=0,\tfrac12\), and \(U\) has exactly two components. Direct one-dimensional integration gives, for \(0<t<1\),
\[
\operatorname{Vol}\{f_\alpha\le t\}=\frac2\pi\arcsin(t^{1/(1+\alpha)}),\qquad
\lim_{t\downarrow0}\frac{\operatorname{Vol}\{f_\alpha\le t\}}{t^{1/(1+\alpha)}}=\frac2\pi.
\]
Consequently \(O(t^{1/(1+\alpha)})\) cannot replace \(o(t^{1/(1+\alpha)})\) in this **geometric separator** criterion. This does **not** construct two distinct solutions of any Monge–Ampère equation; it must not be represented as PDE nonuniqueness or as a replacement for the actual examples in §14.29.

**Assessment / proposed correction.** No original statement is false, and no existing proof gap is certified closed. An optional, separately reviewable \(C^{1,\alpha}\) corollary after Theorem 14.21.13 could record (1) with the distinction between geometric and PDE sharpness. The uniqueness dependent is Theorem 14.21.3; its global measurable-cofactor/contact proof remains an upstream dependency. Neither this report nor the previous §14.21 audits certify an entire section. Full project still contains 25 chapters and 747 numbered sections, with zero entire-section mathematical certificates. All Demailly approximation/regularization, dedicated Bergman, weighted \(L^2\), Ohsawa–Takegoshi, multiscale and positivity-loss work remains **deferred-by-user**. No tests, build, CI, formalization, publication or source/permanent-tag/registry edits were performed.
