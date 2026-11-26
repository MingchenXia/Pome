# Effective finite-jet stability of generic multiplicities

Date: 2026-11-26. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit only.

## Finding POME-GENERIC-MULTIPLICITY-EFFECTIVE-JET-STABILITY-001

Severity low; verified conditional deduction, not a false printed theorem or a complete upstream proof certificate.

### Exact anchors and hypotheses

- docs/sections/lelong-densities-generalized-masses-and-multiplicity--a-weighted-plane-average-with-an-integrable-logarithm/index.html (blob 3dfb298e0076d50d56be26c8ebc06e5c1d341196): Theorem 6.44.5, permanent 9944A8825328, source 59269B9B, lines 70–85; Corollary 6.44.6, permanent 143206769B43, source D1A6763A, lines 90–100.
- docs/sections/lelong-densities-generalized-masses-and-multiplicity--finite-germs-and-their-actual-integer-degree/index.html (blob e2a86c5438c7770a8766f6bedf779e1879ead4c0): Proposition 6.43.1, permanent AD7655D0958A, source F459CB6C, lines 8–33.
- docs/sections/lelong-densities-generalized-masses-and-multiplicity--weights-and-generalized-lelong-masses/index.html (blob 3bfe070c28159bff5f2e90a3f8d8ba695bde26e4): Theorem 6.34.10 and Corollary 6.34.11, lines 122–156.
- Bounded holomorphic removal across a proper analytic subset: internal tag AA4164301998; finite representatives: 776A532CD79E. These internal results, classical product theory and generic-slice theorem are inputs rather than newly certified upstream chains.

Let F:(C^n,0) -> (C^N,0) be holomorphic with zero-fiber codimension >= p, 1 <= p <= n, and m=mu_p(F,0), the positive integer of Theorem 6.44.5. Then:

1. For every integer a >= m, mu_p(F^{[a]},0)=m. The qualifier “sufficiently large” in 6.44.6 can be replaced by this explicit bound.
2. If a holomorphic tuple R of the same length as F has every component in the (m+1)-st power of the maximal ideal, then F+R still has zero-fiber codimension >=p and mu_p(F+R,0)=m. Thus the m-jet of F determines its p-th generic multiplicity among arbitrary holomorphic germs with that jet, without assuming their zero-fiber codimension beforehand.
3. In the isolated-fiber case of 6.43.1 (source dimension q), sigma(F,0) <= d(F,0) for the exponent defined in 6.46.2. This estimate is sharp.

### Proof of the effective isolated-fiber bound

Let H:(C^q,0)->(C^N,0) have isolated zero. By Proposition 6.43.1 choose a cone-adapted linear target projection P so K=PH is finite onto a small target ball with generic sheet number d=d(H,0). Choose a bounded proper representative of K having only 0 over 0. On the complement of its analytic discriminant, for each source coordinate j form

$$
Q_j(w,t)=\prod_{z\in K^{-1}(w)}(t-z_j)
=t^d+\sum_{k=1}^d b_{jk}(w)t^{d-k}.
$$

The symmetric coefficients are single-valued holomorphic there by local inverse charts. All roots are uniformly bounded on the bounded source representative, so the coefficients extend holomorphically over the discriminant by bounded holomorphic removal. Properness and the single point fiber imply that all inverse points tend uniformly to zero as w tends to zero: otherwise a sequence of inverse points bounded away from zero has a convergent subsequence by properness, limiting to the wrong point of the zero fiber. Hence b_{jk}(0)=0. On a smaller ball, |b_{jk}(w)| <= C|w| by holomorphic differentiability. The identity Q_j(K(z),z_j)=0 holds off the inverse discriminant and everywhere by continuity (the finite map is locally open, so that inverse discriminant has empty interior). Shrink further to |z_j| <= 1. We get

$$
|z_j|^d\leq dC|K(z)|,\qquad
|H(z)|\geq c|z|^d
$$

with a positive c depending on the germ and the projection (use a largest coordinate and |K| <= ||P|| |H|). This proves the claimed sigma bound without invoking an effective Nullstellensatz, a length formula or any approximation theorem.

### Generic slices and perturbations

By Theorem 6.44.5, on a full invariant measure set of p-planes S, H=F|_S is finite at zero with d(H,0)=m. On every such S the isolated-fiber bound gives |F(z)| >= c_S |z|^m near zero on S. Constants and radii are allowed to depend on S.

For a>=m, |(z_1^a,...,z_n^a)| <= C|z|^a <= C|z|^m on a unit ball. Consequently the augmented norm is comparable to |F| on each good S, and its pole mass equals m by 6.34.11. The augmented germ has isolated zero in the ambient space. Apply 6.44.5 to it and intersect the two full-measure sets of planes; this proves assertion 1.

For R=O(|z|^{m+1}), on each original good S the quotient |R|/|F| tends to zero, so |F+R| and |F| are comparable there and the perturbed restriction has isolated zero. Existence of even one such p-plane implies codimension >=p for the ambient zero germ of F+R: a component of dimension >n-p would intersect the p-plane in dimension at least one, by the usual dimension inequality (impose n-p independent linear equations, each lowering dimension by at most one). Therefore 6.44.5 applies to F+R. Intersect its full-measure set with the original one and apply bounded-change invariance. This proves assertion 2. Neither a uniform radius over all planes nor an interchange of exceptional sets over uncountably many perturbations is needed: each perturbation is treated separately.

### Sharpness

For n=p take F=(z_1^m,z_2,...,z_p). The generic degree is m by direct counting of inverse points; on the z_1-axis sigma>=m, hence sigma=m. For m>=2 and 1<=a<m, augmentation by all coordinate a-th powers is norm-comparable to (z_1^a,z_2,...,z_p) near zero, so its multiplicity is a, not m. Replacing z_1^m by z_1^{m+1} changes the multiplicity from m to m+1 while preserving all jets of order <=m-1. Thus m is the best universal jet order and the augmentation threshold m is sharp. The same examples for n>p follow by ignoring the last n-p coordinates: on almost every p-plane projection onto the first p coordinates is invertible, so its restriction gives exactly the same local degrees. All statements include m=1 (the lower augmentation threshold is then vacuous).

### Proposed change and dependents

Add the effective bound as a lemma after 6.43.1; strengthen 6.44.6 with a>=mu_p(F,0) and add the finite-jet corollary. The proof of the finite-augmentation step in 6.46.1, permanent 86EB492BC979, lines 22–28, can then specify the same threshold. The exponent in 6.46.2, permanent 751F9003E019, lines 34–63, is bounded by the actual finite degree of the composite in that proof. No claim that its infimum is achieved or that the upper multiplicity is integral. Existing printed results remain valid.

## Coverage and proof checks

- Whole direct conditional §6.35, mathematical lines 7–40, blob d815e0a11cf3aab85abcebd9d5a943ba72c1dedb: Proposition 6.35.1 (source 2034468C, permanent 9BBFC6858DCC) and Corollary 6.35.2 (A83110AE / 22D3ABC6CFCD). Checked proper-support projection of continuous truncated weights by uniform approximation and bounded recursion, zero pushforward in excess degree and positivity of source mass, and sheet counting with zero mass on discriminants. Comparable norms, not just a common zero set, are necessary in the last clause.
- Whole direct conditional §6.38, mathematical lines 7–96, blob a74bd5c4cecc4d310f4b7b08af1b96bc8ff667e0: Lemma 6.38.1 (1706BEA4 / A7BC2FB7F1C6), Theorem 6.38.3 (8BE55493 / 673FC5FBB2C8), Corollary 6.38.5 (ABDB2F19 / CF13884F31CB). Checked openness of cone estimates, compact inverse images with strict radius margins, covering off critical image, bounded-change density identification and normal-base multiplicity-one argument. Triangular parametrization, analytic proper mapping, and finite bimeromorphic normality remain conditional internal inputs.
- Whole direct introductory §6.42, line 7, blob 6277ee1be4d5cc08777aca6c82e9663518be6961: normalization and classical (not non-pluripolar) products.
- Whole direct conditional §6.44, mathematical lines 7–100, blob 3dfb298e0076d50d56be26c8ebc06e5c1d341196: checked blowup direction incidence dimension, uniform radius locally away from bad planes, codimension of repeated pole families, absolute Fubini via log integrability against positive traces, measurability of averaged measures, identification of the origin atom by equality on Borel sets, and generic integer via the analytic threshold theorem. The dimension-drop, Remmert, 7.28.1, 6.39.11 and bounded-change inputs are not transitively certified here.
- Repeat dependency check §6.43 (lines 8–55) and §6.46 (8–63); selected §6.34.10–11 (122–156). Contextual read §6.45 (blob 9175f1ac475bf4a9f9d9a1749037ae86beb675e8), not certified: the rotation theorem's smoothing/threshold inputs were not reopened.
- Four sections previously LEGACY-UNRECONCILED now have exact current direct coverage (three theorem-bearing and one introduction); historical first visits are not asserted. Compared the 56 chapter-6 and 32 chapter-13 current section locators against the matrix separately; no full-book mathematical completion asserted.

No new confirmed printed errors or demonstrated gaps; one conditional strengthening with sharpness; zero complete upstream certificates. Demailly regularization, Bergman/L2/OT/multiscale/positivity-loss programmes remain deferred-by-user. No builds, tests, CI, source edits, registry changes, publication, or merge.
