# Toric trapezoids and the ruled-surface intersection/Hilbert dictionary — 2026-11-05

Finding: **POME-TORIC-TRAPEZOID-HIRZEBRUCH-CROSSCHECK-001**. Severity **low**; status **verified conditional deduction** (all exact computations in this model are supplied, but a general proof of the upstream integrated theorems is not certified). No printed theorem or statement is refuted. This is a new non-product smooth toric-surface calculation, not a duplicate of the previously checked simplex, box, translation of polytopes, or facet-distribution models.

Reviewed production main: **b6933b772f41b45918f7e25ed1afbbb1fd892272**. Review branch only; no edits to source, registry, permanent tags or production body. User-excluded approximation, regularization, Bergman, weighted L², OT, multiscale-atlas, and positivity-loss proof completion stays **deferred-by-user**.

## Exact reading-edition anchors and provenance

- §21.8.2, primitive edge basis, supporting facets, smoothness: docs/sections/convex-analysis-and-toric-potentials--smooth-lattice-polytopes-and-projective-charts/index.html, blob **f442a7b663689b97a9b89689b8b7ae8b366a53fe**, physical lines **25–87**; original source **foundations-of-pluripotential-theory:86BADE82**, permanent **41C54729DBFD**.
- §21.8.3, projective toric charts and very ampleness: same file/blob, physical lines **108–165**; source **foundations-of-pluripotential-theory:0F7315B0**, permanent **E49F0370E203**.
- §§21.9.1–2, inner normal fan, orbits, character orders: docs/sections/convex-analysis-and-toric-potentials--fans-divisors-and-character-sections/index.html, blob **7ad2e6dbdd0ce59e1bf08cd9cb3c046e8c87ff6c**, physical lines **10–68**; source **foundations-of-pluripotential-theory:4C5E5EB3**, permanent **9FD0EEED0DBF**; source **:86CCC496**, permanent **7B4A7CC50CDC**.
- §21.9.5, divisor and all-degree character-section decomposition: same file/blob, physical lines **138–173**; source **foundations-of-pluripotential-theory:BD98CC5B**, permanent **69D3D97E7701**.
- §21.7.3, ambient-normalized lattice limit: docs/sections/convex-analysis-and-toric-potentials--lattice-points-and-volume/index.html, blob **5d209b7f4d2156c19bc3fb300303405df6321230**, lines **57–91**; source **foundations-of-pluripotential-theory:364BCD30**, permanent **831AEEB7084F**.
- Independent ruled-surface comparison, §11.13.1: docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--ample-comparison-quotients-on-hirzebruch-surfaces/index.html, blob **6d836a2ed19f76c26311025602fb44a56713e390**, physical lines **10–54**, source **non-kahler-pluripotential-theory:9A9AA541**, permanent **8FE2AABC7334**. This is a mathematical comparison only; the §11.13 deformation/moduli claims are outside this review.

## Model and Delzant charts

Let \(a,b,c\) be positive integers, \(M=\mathbb Z^2\), and
\[
P_{a,b,c}=\{(x,y):0\le y\le c,\quad 0\le x\le b+ay\}.
\]
The four vertices, in cyclic boundary order, are
\[
v_{00}=(0,0),\quad v_{10}=(b,0),\quad
v_{11}=(b+ac,c),\quad v_{01}=(0,c).
\]
Their primitive inward edge bases, in that order, may be chosen as
\[
((1,0),(0,1)),\qquad
((-1,0),(a,1)),\qquad
((-1,0),(-a,-1)),\qquad
((1,0),(0,-1)).
\]
All four determinants have absolute value one; the last two pairs include the primitive sloped edge with integral vector \((a,1)\). Thus this is genuinely Delzant for every \(a\ge1\), while not a rectangle.

Writing \(X=\chi^{(1,0)}\) and \(Y=\chi^{(0,1)}\), the §21.8.3 vertex charts are, respectively,
\[
(X,Y),\quad (X^{-1},X^aY),\quad
(X^{-1},X^{-a}Y^{-1}),\quad (X,Y^{-1}).
\]
The first and fourth charts glue to a trivial \(\mathbb P^1\)-fiber over the base chart \(X\in\mathbb C\); the second and third glue similarly over \(X^{-1}\in\mathbb C\). On their intersection the finite fiber coordinate transforms by
\[
X_\infty=X_0^{-1},\qquad Y_\infty=X_0^aY_0.
\]
This is precisely the chart gluing for the lines projectivization
\(\mathbb P_{\mathbb P^1}(\mathcal O\oplus\mathcal O(a))\):
if the \(\mathcal O(a)\)-frame transforms by \(e_\infty=X_0^a e_0\), the fiber ratio \(Y=q_0/q_1\) obeys \(Y_\infty=X_0^aY_0\).
Hence the toric surface is the ruled surface \(\mathbb F_a\) of §11.13 with the **lines** convention (rather than an asserted identification from an external classification theorem). Its negative section is the toric divisor \(D_B=\{Y=0\}\); denote its class \(S\).

## Principal divisor signs, the ample class, and intersections

The four primitive inward facet normals and constants are
\[
u_L=(1,0),\ a_L=0;\quad
u_B=(0,1),\ a_B=0;\quad
u_R=(-1,a),\ a_R=b;\quad
u_T=(0,-1),\ a_T=c.
\]
Denote the corresponding prime boundary divisors by \(D_L,D_B,D_R,D_T\).
The §21.9.2 character-order formula yields
\[
\operatorname{div}(\chi^{(1,0)})=D_L-D_R,\qquad
\operatorname{div}(\chi^{(0,1)})=D_B+aD_R-D_T.
\]
Consequently \(D_L\sim D_R\), \(D_T\sim D_B+aD_R\). By the explicit smooth affine toric charts, neighboring boundary divisors meet transversely once, while opposite divisors do not meet. Thus
\[
D_R^2=D_LD_R=0,\quad D_BD_R=D_TD_R=1,\quad
D_B^2=D_B(D_T-aD_R)=-a,\quad
D_T^2=D_T(D_B+aD_R)=a.
\]
Putting \(f=D_R\) and \(S=D_B\), we recover exactly the §11.13 sign convention
\(S^2=-a\), \(S f=1\), \(f^2=0\), and \(D_T\sim S+af\).

The toric polarization of §21.9.5 is
\[
D_P=bD_R+cD_T\sim cS+(b+ac)f
\]
and satisfies
\[
D_P^2=2bc+ac^2.
\]
Since \(b>0,c>0\), §11.13.1's very-ample criterion
\(\beta>a\alpha\) for \(\alpha S+\beta f\) reads
\(b+ac>ac\), precisely matching the embedding of §21.8.3.
The polygon area is independently
\[
\operatorname{vol}(P)=\int_0^c(b+ay)\,dy
=bc+\frac a2c^2;
\qquad D_P^2=2!\operatorname{vol}(P).
\]
This simultaneously checks the inward-normal signs, the *lines* projectivization, the negative section, and the \(n!\) normalization for a nonsplit/nonproduct toric polygon.

## Every integer degree and two independent section counts

For \(k\ge0\) and \(m=(i,j)\in M\), the divisor of the meromorphic section
\(\chi^{(i,j)}s_0^k\) has coefficients
\[
i D_L+j D_B+(kb-i+aj)D_R+(kc-j)D_T.
\]
The section is holomorphic if and only if
\[
0\le j\le kc,\qquad 0\le i\le kb+aj.
\]
This proves directly in the model that the character set is \(kP\cap M\); for \(k=0\), the only global holomorphic character is the constant character, as required by compactness. Hence
\[
\begin{aligned}
h^0(X_P,L^k)
&=\sum_{j=0}^{kc}(kb+aj+1)\\
&=(kc+1)(kb+1)+\frac a2kc(kc+1)\\
&=k^2\left(bc+\frac a2c^2\right)
+k\left(b+c+\frac a2c\right)+1 .
\end{aligned}
\]
The boundary lattice count is exactly
\(B(P)=b+c+(b+ac)+c=2b+2c+ac\);
the same formula reads \(h^0=k^2\operatorname{vol}(P)+kB(P)/2+1\).
No unproved general Pick/Ehrhart theorem is invoked.

Independently, the **integrated** ruled-surface formula of Lemma 11.13.1 gives
\[
\pi_*\mathcal O_{\mathbb F_a}(kcS+k(b+ac)f)
=\bigoplus_{q=0}^{kc}\mathcal O_{\mathbb P^1}(k(b+ac)-aq).
\]
Every summand has nonnegative degree, so
\[
h^0=\sum_{q=0}^{kc}(k(b+ac)-aq+1),
\]
which agrees term by term with the polytope sum on setting \(j=kc-q\).
Therefore the ruled-surface sheaf computation and toric character computation yield exactly the same Hilbert polynomial, not merely the leading asymptotic. The leading term gives
\[
\lim_{k\to\infty}\frac{2}{k^2}h^0(X_P,L^k)
=2bc+ac^2=D_P^2.
\]
For the linearized torus action, the basis vector \(\chi^{(i,j)}s_0^k\) has weight \(\chi^{-(i,j)}\) in the convention explicitly used in §21.9.5. This is consistent with the contragredient action on coordinate sections and does not change the unsigned section count.

## Verdict, dependencies, and correction proposal

**Verdict:** printed Lemma 21.8.2, Theorem 21.8.3, Propositions 21.9.1–2, Theorem 21.9.5, Theorem 21.7.3 and Lemma 11.13.1 survive this nonproduct test. This model provides a new verified **conditional deduction**, not a false theorem, repaired proof, complete global certification, or genuine duplicate. The proof is fully explicit on the four charts; its extensions to arbitrary smooth polytopes are those already stated by the upstream results, which this run does not recertify.

**Affected dependents:** toric character counts, polarization/degree normalization, §21.10 Guillemin metrics, §21.12 ample toric potentials, §19 graded sections, and §11.13 ruled-surface intersection conventions. These are *consistency checks*, not independent proofs of their general results.

**Proposed nonproduction addition:** a concise ruled/toric dictionary example using the four monomial charts and the two exact section counts, located near §21.9.5 or §11.13.1; preserve both original statements, sources, historical attribution, source labels and permanent tags. No body or canonicalization edit made.

**Coverage limits:** this run reads the exact integrated statements and selected proofs at the lines above, computes one full two-dimensional family \(P_{a,b,c}\), and crosschecks the ruled-surface direct-image formula. It does not certify §§21.8–9, §11.13, the entire toric/positivity dependency graph, any general Riemann–Roch theorem, tests, builds or formal verification.