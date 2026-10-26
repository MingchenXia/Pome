# 2026-10-27 — Finite closed maps, sheaf cohomological dimension, and sharp strong convexity

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Audit head before work:** 9ff39885f090f324eed569465cb12e69198e417c.
**Integration source:** the actual main-branch continuous reading-edition HTML, with source variant demailly-complex-geometry. The permanent tags and physical HTML line numbers below are pinned to the listed main blobs.
**Scope:** first selected proof-level passages of §§9.52, 10.61, 10.62. Neither complete sections nor transitive upstream proofs are certified. Both findings are conditional deductions, not false printed theorems.

## POME-FINITE-CLOSED-COHDIM-ASYMMETRY-001

**Status / severity:** verified conditional deduction / low. **Disposition:** optional precise corollary and counterexample; no correction to printed Theorem 10.61.3 or Theorem 10.62.2.

**Integrated anchors and dependencies:**
- docs/sections/spectral-sequences-support-and-cup-products--fibers-closed-maps-and-sheaf-cohomological-dimension/index.html, blob 747ff8bfdbc5de0b7b21343af27d5349b7cfb628: Lemma 10.61.2, tag 2E03713CB092, physical lines 12–24; Theorem 10.61.3, tag 73840D17A7B1, lines 29–46; closed-subspace Proposition 10.61.4, tag 81E5880E3C4E, lines 54–67; cohomological-dimension Definition 10.61.6, tag 849519FBA671, lines 73–74; soft-resolution equivalence Theorem 10.61.7, tag 152F9B94113B, lines 78–112; Theorem 10.61.8, tag DF25846D82A4, lines 117–128.
- docs/sections/spectral-sequences-support-and-cup-products--metric-spaces-products-and-euclidean-bounds/index.html, blob dfee93d5154f21292052ffb9bc617bf26f20ad68: metric-paracompactness Lemma 10.62.1, tag D7F045ADC482, lines 8–33; product and Euclidean-bound Theorem 10.62.2, tag 7857B1BE7A8D, lines 38–69.
- Both pages retain the demailly-complex-geometry source variant. Ordinary sheaf cohomology is meant throughout, not coherent cohomology and not a covering-dimension substitute.

**Statement.** Let \(f:X\to Y\) be a continuous closed map of nonempty topological spaces, with \(X\) Hausdorff and all fibers finite (possibly empty). Then
\[
\boxed{\operatorname{cd}(X)\leq\operatorname{cd}(Y).}
\]
Even when \(X,Y\) are compact metrizable and \(f\) is surjective with fibers of cardinality at most two, the reverse inequality is false: there exists such a map with \(\operatorname{cd}(X)=0\) and \(\operatorname{cd}(Y)=1\). If, in addition, \(f\) admits a continuous section \(s:Y\to X\), then \(\operatorname{cd}(X)=\operatorname{cd}(Y)\).

**Proof of forward inequality.** For every sheaf of abelian groups \(A\) on \(X\), Theorem 10.61.3 identifies the cohomology of \(X\) with that of \(Y\) with coefficients \(f_*A\), because \(f_*\) is exact and \(R^qf_*A=0\) for \(q>0\). Explicitly,
\[
H^k(X,A)\simeq H^k(Y,f_*A)\quad(k\geq0).
\]
If \(\operatorname{cd}(Y)\leq n\), the right side vanishes for \(k>n\), uniformly in \(A\). This is exactly the definition of \(\operatorname{cd}(X)\leq n\). If \(\operatorname{cd}(Y)=+\infty\), the stated inequality is automatic. No separation hypothesis on \(Y\) or surjectivity of \(f\) was used.

**Sharp failure of reverse inequality.** Write the middle-thirds Cantor space
\[
C=\Bigl\{\sum_{k=1}^{\infty}\frac{2a_k}{3^k}:a_k\in\{0,1\}\Bigr\}.
\]
The digit expansion with digits \(0,2\) is unique. Define
\[
f:C\to[0,1],\qquad
f\Bigl(\sum_{k\geq1}2a_k3^{-k}\Bigr)=\sum_{k\geq1}a_k2^{-k}.
\]
The finite partial sums on the right are continuous cylinder functions and converge uniformly, so \(f\) is continuous. Every binary expansion occurs, so \(f\) is onto. Binary representations are unique except at interior dyadic rationals, which have precisely two expansions; consequently every fiber has at most two points. Since \(C\) is compact and \([0,1]\) is Hausdorff, \(f\) is closed and proper.

We check cohomological dimension with the exact sheaf-theoretic definition used in §10.61, not merely an appeal to covering dimension. The Cantor space has a clopen basis and is compact. Let \(A\) be any sheaf of abelian groups on \(C\), \(S\subset C\) closed, and \(t\in\Gamma(S,A|_S)\). The definition of inverse-image restriction represents \(t\) locally near each point of \(S\) by an ambient \(A\)-section. By compactness choose finitely many such neighborhoods, then choose clopen sets inside them covering \(S\). Successive subtraction produces a *pairwise disjoint* finite clopen refinement of their union. On each clopen piece use the corresponding ambient section, and use the zero section on the clopen complement. The resulting global section of \(A\) restricts to \(t\). Hence every sheaf on \(C\) is soft. Since \(C\) is compact Hausdorff, Theorem 10.61.7 with \(n=0\) proves
\[
\operatorname{cd}(C)=0.
\]
For \(I=[0,1]\), Theorem 10.62.2 gives \(\operatorname{cd}(I)\leq1\). If \(\operatorname{cd}(I)=0\), every sheaf on \(I\) would be soft by Theorem 10.61.7. But for the constant integer sheaf \(\underline{\mathbb Z}\), restriction from the connected interval to the two-point closed set \(S=\{0,1\}\) is
\[
\mathbb Z=H^0(I,\underline{\mathbb Z})\longrightarrow
H^0(S,\underline{\mathbb Z}|_S)=\mathbb Z^2,\qquad
m\mapsto(m,m),
\]
which is not surjective. Thus \(\operatorname{cd}(I)=1\), while the finite closed surjection \(C\to I\) starts in dimension zero. In particular, neither a finite fiber bound nor compactness supplies the missing reverse inequality.

**Equality with a section.** If \(f\circ s=\mathrm{id}_Y\), the image \(s(Y)\) is the fixed-point set of the continuous endomorphism \(s\circ f:X\to X\); it is closed because \(X\) is Hausdorff. The restriction \(f|_{s(Y)}\) is inverse to \(s\), so \(s(Y)\simeq Y\). Closed-subspace monotonicity from Proposition 10.61.4 gives \(\operatorname{cd}(Y)=\operatorname{cd}(s(Y))\leq\operatorname{cd}(X)\), which together with the forward inequality proves equality.

**Affected dependents / proposed placement:** a qualified corollary after §10.61.3, cross-linked from §10.62.2; warns against treating finite holomorphic/topological fibers as preserving all-sheaf cohomological dimension. Leray, fiber comparisons, soft resolutions and the interval bound are the specified internal conditional inputs. No assertion about arbitrary nonclosed maps, non-Hausdorff domain finite fibers, or a reverse inequality without a section.

## POME-STRONG-Q-COMPACT-SUBMANIFOLD-OBSTRUCTION-001

**Status / severity:** verified conditional deduction / low. **Disposition:** optional sharpness and obstruction example after Theorem 9.52.8. The printed n-completeness theorem is not false.

**Integrated anchors and dependencies:** docs/sections/convex-neighborhoods-and-coherent-vanishing--convexity-and-cohomology-in-the-top-degrees/index.html, blob e43441b6bf9c098ee7222415cb30c06331efc8ee; source variant demailly-complex-geometry; local bump Lemma 9.52.1, tag 88C2BC468CBC, physical lines 11–54; connected exhaustion Lemma 9.52.5, tag 4A19B00897C5, lines 64–75; normalization/shell construction Lemma 9.52.6, tag 1B57CC3FFF8A, lines 80–99; Corollary 9.52.7, tag 073A6ABDD1C9, lines 104–113; noncompact-exhaustion Theorem 9.52.8, tag 89227CC07C7F, lines 118–131; singular-space Theorem 9.52.10, tag E86D84BDEFC8, lines 148–173; top Runge criterion Proposition 9.52.12, tag 5366BBA720F6, lines 192–219. Strong \(q\)-convexity on an n-fold means at least \(n-q+1\) strictly positive eigenvalues of the Levi form.

**Statement and proof.** Let \(M\) be a complex n-manifold and \(S\subset M\) a nonempty compact complex submanifold of dimension \(q\), with \(1\leq q\leq n\). No smooth strongly \(q\)-convex function exists on any open neighborhood of \(S\). Indeed, the restriction of any smooth real function \(u\) to \(S\) has a maximum at a point \(p\in S\), where the restriction of its Levi form to \(T_p^{1,0}S\) is negative semidefinite. If \(u\) were strongly \(q\)-convex at \(p\), the Levi form on \(T_p^{1,0}M\) would have a strictly positive subspace \(E^+\) of dimension at least \(n-q+1\). Linear algebra forces
\[
\dim_{\mathbb C}(E^+\cap T_p^{1,0}S)
\ \geq\ (n-q+1)+q-n=1.
\]
On a nonzero vector in that intersection the Levi form would be both strictly positive and nonpositive, a contradiction. The argument uses only a compact maximum and the Levi-index convention; no existence theorem or regularization is needed.

For every \(n\geq2\), take the connected noncompact n-fold
\[
M=\mathbb P^{\,n-1}\times\mathbb C,\qquad
S=\mathbb P^{\,n-1}\times\{0\}.
\]
Its compact complex hypersurface \(S\) has dimension \(n-1\), so no smooth strongly \((n-1)\)-convex function exists globally, and in particular no such exhaustion exists. Nevertheless the exactly printed Theorem 9.52.8 guarantees a smooth strictly \(\omega\)-subharmonic exhaustion for every prescribed smooth Hermitian background \(\omega\). Positive \(\omega\)-trace implies at least one positive Levi eigenvalue, i.e. strong \(n\)-convexity. Hence its universal \(q=n\) threshold for arbitrary connected noncompact n-folds cannot be improved to \(q=n-1\) (and a fortiori to smaller \(q\)) without additional geometry. This does not contradict Theorem 9.52.10, since the ambient n-fold has no compact irreducible component of dimension \(n\).

**Affected dependents / proposed placement:** strength of q-completeness in §§9.50–9.52, top-degree Runge and coherent vanishing corollaries. This is an obstruction to an *unasserted generalization*, not a gap or error in Theorems 9.52.8/10.

## Actual coverage, exclusions and verification boundary

First selected proof-level review of §§9.52, 10.61 and 10.62: §§9.52.1, .5–.8, .10, .12 (selected computations and induction/Runge steps), §§10.61.2–.4, .6–.8 (closed fibers, stalks, soft dimension shifting), and §§10.62.1–.2 (metric paracompactness, product and interval arguments). This is **not** certification of the complete sheaf-cohomology, PDE or q-convexity upstream chains. Both findings are verified *conditional deductions* based on explicitly identified integrated inputs; no new confirmed false Pome statement, mathematical duplication or resolved legacy finding. The 747 current ToC identifiers are preserved, with only these three inventory-only rows promoted to precisely scoped selected coverage.

All Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale atlas and positivity-loss proof-completion matters remain **deferred-by-user**, not reopened or certified. No source-text, mathematical body, canonicalization, permanent tag, main, build, CI, formal verification or publication changes are included. Historical attribution and all previous audit statuses remain unchanged.
