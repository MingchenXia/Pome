# Exact jet-generation threshold at torus fixed points of a smooth lattice-polytope embedding

**Date:** 2026-11-19. **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Review branch:** review/mathematical-audit.

## Finding and actual audit boundary

**POME-TORIC-VERTEX-JET-EDGE-THRESHOLD-001 — low / verified conditional deduction.** This is a new audit-only corollary, **not a confirmed error or a repair of a false printed statement**. The full integrated mathematical text of §21.8 (physical lines 5–155) was directly read, including Definition 21.8.1, Lemma 21.8.2, the complete multi-step proof of Theorem 21.8.3, algebraic equations and the Fubini–Study Hessian. The precise section file is docs/sections/convex-analysis-and-toric-potentials--smooth-lattice-polytopes-and-projective-charts/index.html, blob f442a7b663689b97a9b89689b8b7ae8b366a53fe. Source labels / permanent tags: Definition 21.8.1 = foundations-of-pluripotential-theory:5FF56EB5 / E11C7A4F96AC (lines 10–12); Lemma 21.8.2 = foundations-of-pluripotential-theory:86BADE82 / 41C54729DBFD (lines 24–85); Theorem 21.8.3 = foundations-of-pluripotential-theory:0F7315B0 / E49F0370E203 (lines 107–155).

The downstream **selected** proof of Theorem 21.9.5 was also directly checked at docs/sections/convex-analysis-and-toric-potentials--fans-divisors-and-character-sections/index.html, blob 7ad2e6dbdd0ce59e1bf08cd9cb3c046e8c87ff6c, source foundations-of-pluripotential-theory:BD98CC5B / permanent 69D3D97E7701, lines 138–167. This is **not** an audit of the rest of §21.9.

## Exact local jet theorem

Let $M\simeq\mathbb Z^n$, $n\ge1$, and let $P\subset M_{\mathbb R}$ be an $n$-dimensional **smooth lattice polytope**. Form the smooth projective toric variety $X_P$ and ample line bundle $L=\mathcal O_{\mathbb P^{|P\cap M|-1}}(1)|_{X_P}$ as in Theorem 21.8.3. Fix a vertex $v$. Write $e_1,\dots,e_n$ for its primitive edge basis, and let the corresponding **integer lattice lengths** $\ell_i\ge1$ be defined by the edges $E_i=[v,v+\ell_i e_i]$. Let $x_v$ be the torus-fixed point with coordinates $w_1=\dots=w_n=0$ in the vertex chart $U_v$. Put $\ell(v)=\min_i\ell_i$.

For **every integer** $k\ge0$ and $s\ge0$, the natural evaluation on jets
\[
j^s_{x_v}:H^0(X_P,L^k)\longrightarrow
 L^k\otimes_{\mathcal O_{X_P}}\mathcal O_{X_P,x_v}/\mathfrak m_{x_v}^{s+1}
\]
is surjective **if and only if**
\[
\boxed{\quad s\le k\,\ell(v).\quad}
\]
More precisely, after trivialization by the nowhere-vanishing frame $s_v^k$, its image is the span of the monomials $w^\alpha$ with $|\alpha|\le s$ and
\[
kv+\sum_i\alpha_i e_i\ \in\ kP\cap M .
\]
Hence
\[
\operatorname{rank}(j^s_{x_v})=
\#\left\{m\in kP\cap M:\ \sum_i\langle m-kv,u_i\rangle\le s\right\},
\]
where $u_i$ is the facet-normal basis dual to $e_i$. The statement concerns **jets at one torus fixed point**, not simultaneous multi-point jet ampleness or surjectivity of section multiplication.

### Proof

By Lemma 21.8.2(4) (lines 49–55 and 83–84), the facets at $v$ have inward primitive normals $u_i$ dual to $e_i$, every $m\in kP$ has nonnegative integer expansion $m-kv=\sum_i b_i(m)e_i$, and $v+e_i\in P$. Thus $\ell_i$ is a positive integer.

Theorem 21.9.5 (lines 138–164) gives a basis of global sections $H^0(X_P,L^k)$ indexed by $m\in kP\cap M$, namely $\chi^m s_0^k$; its proof is based on the vertex charts already constructed **before** the final very-ampleness paragraph of Theorem 21.8.3. Since $s_0=\chi^{-v}s_v$ in $U_v$, the coefficient of this section relative to $s_v^k$ is
\[
\chi^{m-kv}=\prod_i w_i^{b_i(m)},\qquad b_i(m)=\langle m-kv,u_i\rangle .
\]
Distinct lattice points give distinct exponent vectors, by the basis property. Reduction modulo $\mathfrak m_{x_v}^{s+1}=(w_1,\ldots,w_n)^{s+1}$ retains exactly the monomials of total degree at most $s$, proving the asserted image and rank formula. Since the monomials $w^\alpha$, $|\alpha|\le s$, form a basis of this finite-dimensional local jet space, the map is onto exactly when **all** these monomials occur among the global sections.

If $s\le k\ell(v)$, then $kv+s e_i$ belongs to $kE_i\subset kP$ for every $i$. For $s>0$ and any $\alpha\in\mathbb Z_{\ge0}^n$ with $|\alpha|\le s$,
\[
kv+\sum_i\alpha_i e_i
=\Bigl(1-\frac{|\alpha|}{s}\Bigr)kv+
 \sum_i\frac{\alpha_i}{s}(kv+s e_i)\in kP
\]
by convexity. This is a lattice point, so every required jet monomial occurs. At $s=0$ the vertex section supplies the constant monomial.

Conversely, if $s>k\ell(v)$, choose $i$ with $\ell_i=\ell(v)$ and put $q=k\ell_i+1\le s$. The lattice point $kv+q e_i$ lies strictly past the endpoint $kv+k\ell_i e_i$ of the edge, so it is not in $kP$. Indeed, the intersection of $P$ with that tangent ray is precisely the segment $E_i$: the $n-1$ facets at $v$ whose normals annihilate $e_i$ cut out the edge. Therefore the monomial $w_i^q$ is missing from the image of $j^s_{x_v}$, and the map cannot be surjective. This argument also covers $k=0$: only the constant section exists, so exactly the zero jet is generated. QED.

For the standard simplex $\Delta_n=\operatorname{conv}(0,e_1,\ldots,e_n)$, $\ell(v)=1$ at each vertex, and the threshold for $\mathcal O_{\mathbb P^n}(k)$ is exactly $s=k$. For a dilated simplex $d\Delta_n$ it is $s=kd$. These examples verify that the integer threshold cannot be improved.

## Inspection of the printed arguments and dependencies

**Direct §21.8 reading (entire integrated section):** the lattice primitive-direction and rational convex-combination arguments (lines 10–22, 118–125); finite-face/facet and tangent-cone proofs, including the active-normal induction (lines 24–85); vertex-chart graph closure and cover, set-theoretic homogeneous equations, Laurent-torus irreducibility (107–140); section-basis use and the positive Fubini–Study complex Hessian (141–154). No independent confirmed false statement or gap was established in those lines.

**Dependency-order check:** the final line-bundle paragraph of Theorem 21.8.3 cites Theorem 21.9.5 for the complete $H^0$ basis, while Theorem 21.9.5 cites the *earlier vertex-chart construction* of §21.8.3. This can be read in the acyclic order: (i) §21.8.2 cone/facet combinatorics, (ii) §21.8.3 vertex charts/embedding, (iii) §21.9.4 Laurent expansion and §21.9.5 section basis, (iv) §21.8.3 final full linear-system statement. Thus the back-reference is **not by itself a circular proof**; preserving this substep order is important.

The internal references Lemma 21.2.3, Corollary 21.2.9, Example 10.6.6–7 and §21.9.4 were used **only at statement/context depth or through the checked downstream proof**, not certified from the beginning of their upstream chains. The proof of the new jet theorem is complete given the displayed integrated results. There was no need to reopen any user-excluded regularization/Bergman/$L^2$/Ohsawa–Takegoshi/multiscale/positivity-loss programme; all remain **deferred-by-user**, not resolved.

## Classification and proposed production change

**Finding POME-TORIC-VERTEX-JET-EDGE-THRESHOLD-001:** severity low; status **verified conditional deduction**. No printed theorem is claimed false; no duplicate or replacement canonicalization is proposed. An optional future addition after Theorem 21.9.5 could state the local jet theorem, with permanent source tags and historical attribution preserved. Directly affected readers are the local positivity/jet properties of $L$, §21.8.3 and §21.9.5, and any later toric statements about local polynomial expansion. **Do not infer toric normal generation or simultaneous multi-point jet separation.**

**Exact coverage delta:** +1 full direct section (§21.8, lines 5–155), +1 selected downstream proof (§21.9.5, lines 138–167), +0 transitive proof-chain certifications, no first-visit claim pending legacy reconciliation. Existing 25-chapter/747-section matrix remains a coverage inventory, not a whole-project certification. No builds, tests, GitHub Actions, publishing, or production/source/registry/tag edits were performed.
