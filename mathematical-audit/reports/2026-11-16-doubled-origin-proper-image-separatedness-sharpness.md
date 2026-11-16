# 2026-11-16 — The separatedness boundary for proper analytic direct images: the doubled-origin line

**Finding ID:** `POME-PROPER-NONHAUSDORFF-DOUBLE-ORIGIN-H1-001`. **Severity:** low. **Status:** verified conditional deduction (a counterexample only to an *unstated weakening* of the hypotheses). **Neither printed Lemma 9.47.1 nor printed Theorem 9.47.2 is refuted.**

**Production main inspected:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Integrated continuous reading edition:** `docs/sections/analytic-tensor-products-and-proper-direct-images--coherence-of-proper-analytic-direct-images/index.html`, Git blob `94a7e39e68ce5dee99508213be822611b96db9d2`. The section's stable tag is `0D3949EEEF52`. Lemma 9.47.1 carries permanent tag `81A3D17F4D37` (printed reader locator `9.47.1`), statement at physical line 8 and proof lines 13–22. Theorem 9.47.2 carries permanent tag `1A9A12704621` (printed `9.47.2`), statement at line 28 and proof lines 34–79, especially the invocation of the lemma at lines 48–57 and the separate nuclear/coherent-complex inputs at lines 67–79. Permanent tag URLs: `docs/tag/81A3D17F4D37/index.html` and `docs/tag/1A9A12704621/index.html`. These are exact integrated labels, not inferred legacy source coordinates.

## The geometric construction

Let \(\mathbb A^1_+\) and \(\mathbb A^1_-\) denote two copies of the complex line. Form a locally analytic complex curve
\[
 X=(\mathbb A^1_+\amalg\mathbb A^1_-)/\bigl(z_+\sim z_-\ \text{for every }z\ne0\bigr).
\]
Write \(o_+\) and \(o_-\) for the two different points over the origin. The two chart images \(U_+,U_-\subset X\) are open analytic manifolds, each biholomorphic to \(\mathbb C\). Their intersection is \(\mathbb C^\times\), embedded by the identity in both charts. The manifold \(X\) is connected and second countable, but is **not Hausdorff**: every neighborhood of \(o_+\) intersects every neighborhood of \(o_-\) along a punctured disc.

The identity coordinates glue into a surjective holomorphic map
\[
 g:X\longrightarrow\mathbb C,\qquad g([z_\pm])=z.
\]
For every compact \(K\subset\mathbb C\), \(g^{-1}K\) is the continuous quotient image of two compact copies of \(K\), hence is compact. This **compact-preimage property does not make \(g\) a proper analytic morphism in the Hausdorff/separated category used in Theorem 9.47.2**. We use it solely to show that compact fibers and compact inverse images of compact sets do not replace the printed separatedness assumption. Over \(\mathbb C^\times\), \(g\) is an isomorphism.

## Failure of the closed diagonal without Hausdorffness

The patches \(U_\pm\) meet the other local requirements of Lemma 9.47.1: each is a closed analytic subspace of its ambient coordinate polydisc \(\Omega_\pm=\mathbb C\) (the whole coordinate line is closed analytic). Nevertheless their diagonal intersection maps to
\[
 \{(z,z)\in\mathbb C^2:z\ne0\}.
\]
Its closure in \(\Omega_+\times\Omega_-\) contains \((0,0)\), which the image omits. It is therefore **not closed**. In fact it cannot be a closed analytic subset: any holomorphic germ vanishing on this punctured diagonal also vanishes at \((0,0)\), by the one-variable identity theorem. This identifies precisely why the Hausdorff argument at line 14 of the printed proof cannot be deleted. The printed lemma *has* that hypothesis, so there is no flaw in its use for the printed theorem.

## Explicit noncoherent higher direct-image stalk

Write \(D_r=\{z:|z|<r\}\). The inverse image \(g^{-1}D_r\) is covered by \(D_r^+\) and \(D_r^-\), each an analytic disc, with overlap \(D_r^\times\). The Mayer–Vietoris sequence for the holomorphic structure sheaf contains the exact segment
\[
 \mathcal O(D_r)\oplus\mathcal O(D_r)
 \xrightarrow{(f_+,f_-)\mapsto f_+-f_-}
 \mathcal O(D_r^\times)\xrightarrow{\delta_r}
 H^1(g^{-1}D_r,\mathcal O_X).
\]
The image of the first arrow is exactly \(\mathcal O(D_r)\). Thus, *without invoking any positive-degree cohomology vanishing*, the connecting map embeds
\[
 \mathcal O(D_r^\times)/\mathcal O(D_r)
 \hookrightarrow H^1(g^{-1}D_r,\mathcal O_X).
\]
These injections commute with restriction to smaller discs, by naturality of Mayer–Vietoris. For each integer \(k\ge1\), the class of \(z^{-k}\) cannot become a holomorphic function on any smaller disc, so it yields a nonzero germ
\[
 c_k\in (R^1g_*\mathcal O_X)_0
     =\varinjlim_{r\downarrow0}H^1(g^{-1}D_r,\mathcal O_X).
\]
The displayed stalk identification is the usual derived-direct-image stalk formula, as used in the integrated Proposition 9.43.2 and in the last paragraph of Theorem 9.47.2 (line 77); its standard proof uses injective/flabby resolutions and exact filtered colimits. We do not need the stronger equality \(H^1=\mathcal O(D_r^\times)/\mathcal O(D_r)\), which additionally follows from the acyclicity of the two ordinary discs.

The germ \(z\in\mathcal O_{\mathbb C,0}=\mathbb C\{z\}\) acts by multiplication on the classes. Consequently
\[
 z^k c_k=0\quad(k\ge1),\qquad
 z^N c_{N+1}=c_1\ne0\quad(N\ge0).
\]
Away from \(0\), \(g\) is a local isomorphism and its inverse-image neighborhoods are ordinary discs; thus \((R^1g_*\mathcal O_X)|_{\mathbb C^\times}=0\).

If \(R^1g_*\mathcal O_X\) were coherent near \(0\), its stalk \(M\) would be a finite \(\mathbb C\{z\}\)-module supported at the closed point. A finite module over the Noetherian one-dimensional local domain \(\mathbb C\{z\}\) with support \(\{(z)\}\) is annihilated by a common power of \(z\): indeed a finite module with zero localization at the fraction field has finite torsion generators, each killed by some nonzero analytic germ, hence by a suitable power of \(z\). Equivalently this follows from the cyclic-module classification over the DVR. But the identities \(z^N c_{N+1}=c_1\ne0\) contradict every proposed uniform annihilating power. Therefore
\[
 \boxed{R^1g_*\mathcal O_X\text{ is not coherent near the origin}.}
\]
This gives an explicit failure of a naive extension of Theorem 9.47.2 to non-Hausdorff analytic manifolds merely by requiring compact preimages of compact target sets. The failure already occurs for a smooth, one-dimensional, second-countable source, with two-point special fiber and \(\mathcal S=\mathcal O_X\).

## Verdict, precise dependent scope, and limitations

1. **Lemma 9.47.1 (tag `81A3D17F4D37`):** the diagonal-closedness proof at physical line 14 is consistent under its stated Hausdorff hypothesis. The example proves that this hypothesis cannot be omitted; it is not a counterexample to the stated lemma.
2. **Theorem 9.47.2 (tag `1A9A12704621`):** the printed proper-image coherence theorem explicitly assumes Hausdorff source and target. The example does not refute it. The example shows that no proof-level generalization can discard source separatedness and retain only compact-preimage behavior. A possible *expository* clarification is to keep the Hausdorff condition visibly adjacent to the diagonal lemma and to distinguish the compact-preimage property from separated analytic properness. **No change to the theorem is proposed.**
3. **Affected dependents:** any future reuse of the graph/diagonal construction of §9.47.1 or higher direct-image coherence §9.47.2 outside the Hausdorff/separated analytic category; not the actual printed applications under their existing hypotheses.
4. **Not independently certified in this run:** analytic coherent direct-image behavior of closed embeddings, Oka coherence, strongly 1-complete coherent vanishing, fully transverse nuclear finite-free complexes in §9.46.7, and the total correctness of the higher-direct-image comparison of §9.43.2. The displayed elementary cohomology obstruction needs only the standard Mayer–Vietoris exact sequence and the derived-stalk construction; it does **not** prove the full printed proper-image theorem.

**Coverage:** this is a renewed direct selected examination of §9.47.1 and 9.47.2, rather than a first section visit. In the actual main reading edition there are 25 chapters and 747 distinct numbered sections; the central section matrix already inventories all 747. This run adds **0 first-visited numbered sections and 0 fully certified numbered sections**. No project build, test suite or CI was run. No mathematical text, source file, source label, registry, published documentation, or permanent tag was changed.

**User-deferred scope:** Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remain **deferred-by-user**, not solved, not audited, and not used here.