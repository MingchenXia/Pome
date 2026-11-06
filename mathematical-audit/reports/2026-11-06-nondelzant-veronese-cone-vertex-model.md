# 2026-11-06 — non-Delzant lattice triangles, exact Veronese cones, and singular vertex charts

**Stable finding:** POME-TORIC-NONDELZANT-VERONESE-CONE-001.  
**Status:** verified conditional deduction (fully computed countermodel to *dropping an assumption*, not a counterexample to the printed theorem).  
**Severity:** low. No source, reading-body, canonicalization, or permanent-tag edit is made.

## Provenance and exact scope

Production `main`: **b6933b772f41b45918f7e25ed1afbbb1fd892272**. The integrated reading edition, rather than detached source numbering, was inspected:

- `docs/sections/convex-analysis-and-toric-potentials--smooth-lattice-polytopes-and-projective-charts/index.html`, blob **f442a7b663689b97a9b89689b8b7ae8b366a53fe**, physical lines **11–20** (Definition 21.8.1, `foundations-of-pluripotential-theory:5FF56EB5` / permanent `E11C7A4F96AC`), **25–38 and 81–87** (Lemma 21.8.2, `:86BADE82` / `41C54729DBFD`), **89–112 and 118–142** (the embedding construction and Theorem 21.8.3, `:0F7315B0` / `E49F0370E203`).
- `docs/sections/convex-analysis-and-toric-potentials--lattice-points-and-volume/index.html`, blob **5d209b7f4d2156c19bc3fb300303405df6321230**, physical lines **58–63** (Theorem 21.7.3, `foundations-of-pluripotential-theory:364BCD30` / `831AEEB7084F`); only the lattice-count normalization is cross-checked.
- `docs/sections/convex-analysis-and-toric-potentials--fans-divisors-and-character-sections/index.html`, blob **7ad2e6dbdd0ce59e1bf08cd9cb3c046e8c87ff6c**, physical lines **139–165** (Theorem 21.9.5, `foundations-of-pluripotential-theory:BD98CC5B` / `69D3D97E7701`); only its stated *smooth-polytope* hypothesis and dependence on vertex charts are compared. **Its section theorem is not invoked for the nonsmooth examples.**

These checks do not certify all of §§21.7–21.9 or their dependency chains.

## Explicit family and sharp failure of affine-space vertex charts

Let \(M=\mathbb Z^2\), \(q\ge2\) an integer, and
\[
 P_q=\operatorname{conv}\{(0,0),(1,0),(0,q)\},\qquad
 A_q=P_q\cap M=\{(1,0)\}\cup\{(0,j):0\le j\le q\}.
\]
This is a full-dimensional *simple* lattice polygon. Its primitive edge directions are a unimodular basis at \((0,0)\) and \((0,q)\), but at \(v=(1,0)\) they are
\[
 e_1=(-1,0),\qquad e_2=(-1,q),\qquad
 |\det(e_1,e_2)|=q.
\]
Thus it is **not** smooth/Delzant for \(q\ge2\), and is Delzant for \(q=1\). This is exactly the integrality condition required in Lemma 21.8.2(4) and in the monomial-coordinate proof of Theorem 21.8.3.

On \(T=(\mathbb C^*)^2\), write \(z=\chi^{(1,0)}\), \(w=\chi^{(0,1)}\). The full-lattice-point embedding used in §21.8 becomes
\[
 \iota_q(z,w)=[1:w:w^2:\cdots:w^q:z]\in\mathbb P^{q+1}.
\]
Its closure \(X_q\) is the projective cone over the degree-\(q\) rational normal curve
\[
 [s:t]\longmapsto[s^q:s^{q-1}t:\cdots:t^q]\subset\mathbb P^q,
\]
with apex \(a=[0:\cdots:0:1]\). Indeed, the torus image lies on the cone, and the open set \(Z_0\ne0\) of the cone is its polynomial graph \(Z_j/Z_0=(Z_1/Z_0)^j\) with free extra coordinate \(Z_z/Z_0\); this graph contains the torus image densely. The other endpoint chart \(Z_q\ne0\) has coordinates \(w^{-1}=Z_{q-1}/Z_q\) and \(z/w^q=Z_z/Z_q\), and is likewise an affine plane. Every point of the cone except the apex belongs to one of these two charts, so the cone is smooth away from \(a\).

On the *remaining vertex chart* \(Z_z\ne0\) put \(y_j=Z_j/Z_z\), \(0\le j\le q\). Its coordinate ring is
\[
 \mathbb C[y_0,\ldots,y_q]
 \big/\ker(y_j\mapsto u^{q-j}v^j)
 \cong \mathbb C[u^q,u^{q-1}v,\ldots,v^q]
 =\mathbb C[u,v]^{\mu_q},
\]
where \(\mu_q\) acts by \((u,v)\mapsto(\zeta u,\zeta v)\). To see that this is exactly the affine cone, every point off the apex has the form \((c\,s^{q-j}t^j)_{j=0}^q\); choose a complex \(q\)-th root of \(c\) and absorb it into \(s,t\). The ring has Krull dimension \(2\): \(\mathbb C[u,v]\) is integral over it (both \(u\) and \(v\) satisfy monic \(q\)-th power equations), and its fraction field has transcendence degree \(2\). It has **no nonzero linear equation in the \(y_j\)**, because the degree-\(q\) monomials \(u^{q-j}v^j\) are linearly independent. All relations have degree at least two. Consequently the Zariski tangent space at the origin has dimension \(q+1>2\), and \(a\) is singular. This gives a direct elementary reason why the coordinates from Theorem 21.8.3 cannot extend to a biholomorphism \(U_v\simeq\mathbb C^2\) without its Delzant hypothesis.

For \(q=2\), the full projective variety has the single equation
\[
 Z_0Z_2=Z_1^2\quad\text{in }\mathbb P^3.
\]
The affine apex chart is \(y_0y_2=y_1^2\) in \(\mathbb C^3\), an ordinary quadratic surface cone (an \(A_1\) singularity); the Jacobian vanishes at the apex. This is an explicit singular projective embedding with all lattice-point characters included. For \(q=1\) the same procedure produces \(\mathbb P^2\), as the smooth theorem predicts.

## Degree-by-degree count without assuming the smooth section theorem

The lattice points of \(kP_q\), for integers \(k\ge0\), are exactly
\[
 (a,b)\in\mathbb Z^2,\qquad 0\le a\le k,\quad0\le b\le q(k-a).
\]
Hence
\[
 \#(kP_q\cap M)=\sum_{a=0}^k\bigl(q(k-a)+1\bigr)
 =(k+1)\left(1+\frac{qk}{2}\right)
 =\frac q2k^2+\left(\frac q2+1\right)k+1.
\]
This is also **exactly the degree-\(k\) Hilbert function of the homogeneous coordinate ring** of the cone: a degree-\(k\) coordinate monomial with \(a\) factors of \(Z_z\) and \(k-a\) factors from \(Z_0,\ldots,Z_q\) restricts on the torus to \(z^aw^b\); every integer \(0\le b\le q(k-a)\) is a sum of \(k-a\) integers from \(0,\ldots,q\), and distinct pairs \((a,b)\) are independent Laurent characters. The homogeneous ideal of the torus closure is exactly the kernel of this character map, so these characters form a basis of each graded piece of its coordinate ring. No assertion that an arbitrary singular-variety section space equals this coordinate-ring piece is needed.

Finally \(\operatorname{area}(P_q)=q/2\), so
\[
 \lim_{k\to\infty} \frac{2!}{k^2}\#(kP_q\cap M)
 =q=2!\operatorname{area}(P_q).
\]
Thus the elementary lattice-volume normalization remains valid for this nonsmooth polytope, even though the smooth vertex-chart statement fails outside its hypotheses. This does **not** extend Theorem 21.9.5 to singular \(X_q\).

## Classification, dependencies, and recommended handling

**No false printed theorem.** Theorem 21.8.3 explicitly assumes a smooth polytope and correctly uses Lemma 21.8.2(4). The model shows that *simplicity*, full-dimensionality, and use of every lattice point do **not** replace unimodularity. It also separates projective algebraicity from smoothness. The proof above is an exact independent model calculation; the integration theorem and fan theory are only used for statement comparison, not to infer the singularity.

**Proposed correction:** no modification to the existing theorem. If a future text generalizes it to arbitrary simple lattice polytopes, use a normal affine toric or cyclic-quotient chart instead of \(\mathbb C^n\) at nonunimodular vertices; preserve all source labels and permanent tags. **Affected dependents if the assumption is ever weakened:** the vertex polynomial parametrization in §21.8.3 and the smooth-chart premises of §21.9.2 and §21.9.5. No current dependent is declared false or repaired.

**Coverage:** selected hypothesis and vertex-chart checks in §§21.8.1–3; a direct lattice count linked only to §21.7.3's normalization; selected §21.9.5 hypothesis crosscheck. The rest of all three sections, and all external/internal dependencies, remain unverified. Existing confirmed errors, proof gaps, external dependencies, and user-deferred approximation/regularization/Bergman/weighted-\(L^2\)/Ohsawa–Takegoshi/multiscale/positivity-loss programme retain their prior statuses. No tests, build, formal verification, CI, or publication were performed.
