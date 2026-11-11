# 2026-11-11 — exact polygon section rings and the dimensional boundary of normal generation

**Stable finding:** `POME-TORIC-POLYGON-NORMALGEN-PICK-REEVE-001`  
**Severity / status:** low / **verified conditional deduction**. The printed results are **not refuted**. The polygon combinatorics below is proved directly; the geometric consequences are conditional on the integrated Theorem 21.8.3 and Theorem 21.9.5. This is not a certification of their entire upstream proof chains.

## Exact reviewed production objects

- Production `main`: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- `docs/sections/convex-analysis-and-toric-potentials--smooth-lattice-polytopes-and-projective-charts/index.html`, blob `f442a7b663689b97a9b89689b8b7ae8b366a53fe`: Definition 21.8.1, source `foundations-of-pluripotential-theory:5FF56EB5`, permanent tag `E11C7A4F96AC`, physical lines 10–21; Lemma 21.8.2 source `foundations-of-pluripotential-theory:86BADE82`, tag `41C54729DBFD`, lines 24–85; Theorem 21.8.3 source `foundations-of-pluripotential-theory:0F7315B0`, tag `E49F0370E203`, lines 107–155. The permanent tag and source label of the **theorem**, not those of its containing section, identify this dependency.
- `docs/sections/convex-analysis-and-toric-potentials--fans-divisors-and-character-sections/index.html`, blob `7ad2e6dbdd0ce59e1bf08cd9cb3c046e8c87ff6c`: Theorem 21.9.5, source `foundations-of-pluripotential-theory:BD98CC5B`, permanent tag `69D3D97E7701`, physical lines 138–166 (section basis at lines 139–149; multiplication-compatible Laurent proof at 155–166).
- `docs/sections/convex-analysis-and-toric-potentials--lattice-points-and-volume/index.html`, blob `5d209b7f4d2156c19bc3fb300303405df6321230`: Theorem 21.7.3, source `foundations-of-pluripotential-theory:364BCD30`, permanent tag `831AEEB7084F`, physical lines 57–89 (asymptotic count only). This is a crosscheck, not an assertion that the printed theorem already states the exact quadratic count.

The §21.8 standing convention after line 89 assumes that the polytope used to define `X_P` is **smooth (Delzant)** and full dimensional. We preserve that premise for the geometric statements and explicitly separate the stronger **combinatorial** statement (which holds for every lattice polygon).

## Theorems and proof

Let `M` be a lattice of rank two, `P ⊂ M_R` a full-dimensional lattice polygon, `A=P∩M`, `I=#(Int(P)∩M)`, and `B=#(∂P∩M)`. Volumes are normalized so that a lattice fundamental parallelogram has area one.

**(1) Unimodular triangulation and degree-one decomposition.** Every such `P` has a finite triangulation into lattice triangles of determinant `±1`. Consequently, for each integer `k≥1` and each `m∈kP∩M` there exist `p_1,...,p_k∈P∩M` with `m=p_1+...+p_k`. More strongly, for every pair of integers `k,l≥0`,

\[
 (kP\cap M)+(lP\cap M)=((k+l)P)\cap M .
\]

*Proof.* First triangulate the convex polygon by diagonals between its lattice vertices. It remains to refine an arbitrary lattice triangle `T=conv(v_0,v_1,v_2)`. Put `u=v_1-v_0`, `v=v_2-v_0`, and `D=|det(u,v)|`. If `D>1`, the sublattice `Zu+Zv` has index `D`, so its half-open fundamental parallelogram `{tu+sv:0≤t,s<1}` contains a nonzero lattice vector `w`. If `t+s≤1`, then `v_0+w` belongs to `T`; otherwise `v_0+u+v-w` belongs to `T`, because its coefficients `1-t`, `1-s` are nonnegative and sum to `2-t-s<1`. Either point is distinct from the three vertices. Subdivide `T` at this lattice point (two triangles if it lies on an edge, three if interior). Every nondegenerate resulting lattice triangle has strictly smaller positive integer determinant, and the determinants sum to `D`. Strong induction on `D` terminates in unimodular triangles. No lattice point can lie strictly inside or on an open edge of a unimodular triangle: the affine edge matrix is an integral lattice automorphism and sends the triangle to the unit simplex.

Now choose a unimodular triangle `conv(v_0,v_1,v_2)` containing `m/k`. Since `v_1-v_0,v_2-v_0` form a lattice basis, unique integers `a,b` satisfy
\[
 m-kv_0=a(v_1-v_0)+b(v_2-v_0).
\]
Barycentric nonnegativity gives `a,b≥0` and `a+b≤k`. Hence
\[
 m=(k-a-b)v_0+av_1+bv_2,
\]
a sum of exactly `k` lattice points of `P`. For `m∈(k+l)P∩M` split such a sum into `k` and `l` terms; the reverse Minkowski inclusion follows from convexity. The zero-degree convention is `0P∩M={0}`. QED.

**(2) Exact Hilbert function and series.** For every integer `k≥0`,
\[
 \#(kP\cap M)=\operatorname{Area}(P)\,k^2+\frac B2\,k+1,
 \qquad
 \sum_{k\ge0}\#(kP\cap M)t^k
 =\frac{1+(I+B-3)t+It^2}{(1-t)^3}.
\]

*Proof of the planar lattice count (without quoting Pick's theorem).* Take a unimodular triangulation, let `F` count its triangles and `E_{\mathrm{int}}` its interior edges. Every elementary triangle has area `1/2`, while each boundary edge of the triangulation is primitive. There are exactly `B` boundary edges. The elementary planar Euler relation can be proved by taking a spanning tree of the triangulation graph (with `V-1` edges) and noting that every edge added to the tree produces exactly one new bounded face. Hence `(I+B)-(E_{\mathrm{int}}+B)+F=1`. Counting incidences of triangle edges yields `3F=2E_{\mathrm{int}}+B`. Eliminating `E_{\mathrm{int}}` gives `F=2I+B-2`, so `Area(P)=I+B/2-1`. Apply the same reasoning to `kP`. Its area is `k^2 Area(P)`, and the number of its boundary lattice points is `kB` (each polygon edge's primitive lattice length is multiplied by `k`, and the sum of these lengths equals the number of boundary lattice points). This proves the displayed count for `k≥1`, and `k=0` follows directly. Summing the familiar geometric-series identities for `1,k,k^2` and substituting `Area(P)=I+B/2-1` proves the rational Hilbert series. QED.

**(3) Consequences for the *integrated* smooth toric surface.** Assume additionally that `P` is Delzant, so that Theorem 21.8.3 constructs its smooth projective toric surface `X_P` with `L=O(1)|_{X_P}`. The actual Theorem 21.9.5 gives
\[
 H^0(X_P,L^k)=\bigoplus_{m\in kP\cap M}\mathbb C\,\chi^m s_0^k .
\]
Multiplying character sections adds lattice exponents. By (1), the canonical map `Sym^k H^0(X_P,L)→H^0(X_P,L^k)` is onto for *every* `k≥0`, and in fact multiplication `H^0(kL)⊗H^0(lL)→H^0((k+l)L)` is onto for all `k,l≥0`. Thus `L` is normally generated. The exact dimension and generating-series formulas of (2) hold for its entire section ring, strengthening the **leading asymptotic** of Theorem 21.9.5, with no smoothness assumption needed for the *lattice-point calculation* itself.

There is also a direct integrally-closedness verification, avoiding any general toric-normality theorem. The section ring is the semigroup algebra `R=C[S]` for
\[
 S=\{(m,k)\in M\oplus\mathbb Z_{\ge0}:m\in kP\cap M\}
   =C_P\cap(M\oplus\mathbb Z),
\quad C_P=\{(x,t):t\ge0,\ x\in tP\}.
\]
A unimodular triangle inside `P` ensures that `S` generates all of `M⊕Z` as a group: differences of `(v_i,1)` give two lattice basis vectors at degree zero, together with `(v_0,1)`. Let `B_0=C[M⊕Z]`, the Laurent polynomial ring in three variables. It is a localization of `R` at monomials and is integrally closed: for a coprime rational fraction `p/q`, a monic relation over a Laurent polynomial UFD forces `q|p^N`, hence `q` is a unit. An element `z` integral over `R` is therefore a *finite* Laurent polynomial in `B_0`. For each primitive facet inequality `L_\rho(m,k)=\langle m,u_\rho\rangle+ka_\rho` and the inequality `L_0(m,k)=k`, define a Laurent-polynomial valuation `v_L(z)` as the minimum `L`-weight among nonzero monomials, extended to fractions. The initial weighted part of a product is the product of its nonzero initial parts in a domain, so `v_L` is multiplicative. Every element of `R` has `v_L≥0`. If an integral `z` had `v_L(z)<0`, its monic equation `z^d+a_{d-1}z^{d-1}+\cdots+a_0=0` would have a unique strictly smallest valuation at `z^d`, a contradiction. Thus `v_L(z)≥0` for every defining inequality. Every Laurent monomial of `z` satisfies all facet and degree inequalities; at degree zero their intersection contains only `m=0`, by boundedness of `P`. Hence every monomial of `z` belongs to `S`, and `z∈R`. The section ring is integrally closed, and because it equals the homogeneous coordinate ring generated in degree one, the §21.8 complete-linear-system embedding is **projectively normal** in dimension two. This proof uses elementary Laurent-polynomial UFD algebra, *not* a regularization or Bergman-kernel theorem.

**(4) Sharp dimensional caveat.** Do **not** extend the degree-one normal-generation conclusion to arbitrary three-dimensional lattice polytopes. For `q≥2`, let
\[
 Q_q=\operatorname{conv}\bigl(0,(1,0,0),(0,1,0),(1,1,q)\bigr)\subset\mathbb R^3.
\]
It has only these four lattice points. Indeed, for `0<z<q`, membership of an integer `(x,y,z)` would require `x,y≥z/q>0` and `x+y-z/q≤1`, while `x,y≥1` makes the left side strictly greater than one. The bottom and top slices give only the listed vertices. Nevertheless `(1,1,1)∈2Q_q`, because it is a nonnegative sum of the four vertices with coefficients `1/q,1-1/q,1-1/q,1/q` (in the order `0,e_1,e_2,(1,1,q)`) whose total is two. It cannot equal a sum of two points of `Q_q∩Z^3`, since those points have third coordinate either zero or `q`. This counterexample is **not Delzant** and makes **no claim** about the substantially stronger normal-generation question for arbitrary smooth higher-dimensional lattice polytopes.

## Dependency classification, effect, and proposed placement

- **Status:** low / verified conditional deduction; **no confirmed error, no proof gap in the inspected steps, and no duplicate canonization claim.**
- **Independently checked:** planar unimodular triangulation, degree-one and two-degree decomposition, the exact lattice count, the Hilbert series, and the explicit non-Delzant threefold obstruction.
- **Conditional geometric dependencies:** Theorem 21.8.3 (full sections and embedding) and Theorem 21.9.5 (character basis). Their full upstream algebraic-geometric proofs are *not* certified by this report. Theorem 21.7.3 is only a consistency check of leading coefficients.
- **Proposed optional insertion:** after Theorem 21.9.5, add a surface-specific corollary stating surjectivity of all section multiplication maps, the exact Hilbert polynomial/series, and projective normality; include the Reeve simplex only as a warning about unrestricted higher-dimensional lattice polytopes. Preserve every existing source attribution, stable tag, and convention. Do not merge this into an arbitrary-dimension theorem.
- **Affected dependents:** surface instances of later toric and section-growth arguments may invoke this stronger finite-degree statement; there is no need to amend the existing, weaker asymptotic theorem.
- **Scope/coverage:** new proof-level audit of the *normal-generation question* in §§21.8–21.9 with §21.7 normalization crosscheck; these three sections were already partially reviewed. **0 newly first-visited numbered sections, 0 fully certified sections.** The previously inventoried **25 chapters / 747 numbered sections** remain the coverage baseline.
- **Deferred-by-user:** Demailly regularization/approximation and its dedicated Bergman, weighted-L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programmes were not opened, extended, or certified. Historical attributions and unresolved external dependencies remain unchanged.
- **Actions not done:** no production main/source/body/registry/canonical/permanent-tag editing; no build, GitHub Actions, publishing, or formal verification.

Finite, non-proof diagnostic checks performed this run: brute-force counts for triangles `dΔ_2` with `d=1,2,4` and `k=1,2,3,5`, rectangles `[0,a]×[0,b]` with `(a,b)=(1,1),(2,3),(3,5)` and `k=1,...,5`, and the claimed Reeve hole for `q=2,3,5,8`. These finite instances support but do **not** replace the general proofs above.
