# Noncompact level sets and the extended non-pluripolar Monge–Ampère measure

**Date:** 2026-11-12. **Stable finding:** `POME-NPP-LEVEL-FINITE-NONCOMPACT-001`. **Classification:** medium / **confirmed error in the stated noncompact scope**; the compact version and the core truncation construction are **not refuted**.

## Checked revision and precise integrated anchors

- Production `main`: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- `docs/sections/non-pluripolar-monge-ampere-measures/index.html`, blob `5d0f652ffaaaef81cf74d1786082e429f71b3b89`: the section's chapter-level conventions at physical lines 7–10, Theorem 13.14.3 at lines **61–72** (original source label `non-kahler-pluripotential-theory:059FFA20`, permanent tag `99C7ACBB2589`), defining Eq. 13.14.4 at lines **63–65** (source `:0C05ED0A`, permanent `E6AA45ACEA33`), and the proof's finite-level argument at **76–91**.
- Lemma 13.14.2, same integrated file at lines **24–57** (source `non-kahler-pluripotential-theory:84DD8892`, permanent `D36A46B4DD86`), establishes positivity and a bounded-background comparison on the finite-level set.
- `docs/sections/plurisubharmonic-functions-and-singularities--products-with-smooth-backgrounds/index.html`, blob `e2ba89b51376ba0296846221109c664a0c29b2c3`, Proposition 5.28.2 at physical **20–46** (source `non-kahler-pluripotential-theory:890BD62D`, permanent `3EDAB69A7289`). Its local bounded-product construction is consistent, but the global finiteness observation in line 46 explicitly invokes **compact** `X`.
- `docs/sections/non-pluripolar-products/index.html`, §13.1 introductory paragraph at physical line **10**, already distinguishes possible infinite local masses for general non-pluripolar products.
- Theorem 13.14.3 does not impose compactness in its hypotheses. The section states that `X` carries a Hermitian form and a smooth probability `dV` (line 7), not that `X` is compact; line 96 explicitly says **“On compact X”** when giving the order-zero-current conclusion. Thus compactness is not a justified implicit theorem hypothesis here.

## Exact false assertion and counterexample

The theorem asserts that `MA^ext_theta(u)` “is **finite on each D_t** and σ-finite on X” for arbitrary smooth real `theta` and `u in PSH(X,theta)`.

Take the **connected noncompact** manifold `X = C^n`, `n >= 1`, with complex coordinates `z_1,...,z_n`, and use the manuscript normalization
[
 dd^c = rac{i}{2pi}partialarpartial,qquad
 	heta = dd^csum_{j=1}^n |z_j|^2
       = rac{i}{2pi}sum_{j=1}^n dz_jwedge dar z_j>0,qquad uequiv 0.
]
If the chapter's smooth positive probability-volume convention is required, set
[
 dV=pi^{-n}e^{-sum_j|z_j|^2}prod_j dx_j,dy_j.
]
Its total volume is one, and it does not enter the Monge–Ampère product. For every `t>0`, `u_t=0` and `D_t=X`. Consequently, directly from Eq. 13.14.4,
[
 mathbf1_{D_t}(	heta+dd^cu_t)^n=	heta^n
 =rac{n!}{pi^n}prod_{j=1}^n dx_j,dy_j,
 qquad mathrm{MA}^{ext}_	heta(u)(D_t)=+infty.
]
The measure is positive, locally finite, σ-finite, and non-pluripolar. **Only the unqualified finite-on-`D_t` claim is false.** No singular-potential construction, limit interchange, or Demailly regularization is involved. The special bounded-`u` case in the closing paragraph of §13.14 (line 96), where `D_t=X` for large `t`, independently confirms the obstruction.

## Complete corrected local argument

Retain the given local positivity (Lemma 13.14.2) and plurifine compatibility (Theorem 13.14.3, lines 77–86). For any compact `K subset X` and `t>0`,
[
 mathrm{MA}^{ext}_	heta(u)(Kcap D_t)
 le igl(Omega+dd^c u_tigr)^n(K) < +infty.
]
The inequality is obtained by restriction of Lemma 13.14.2; the last finiteness follows from the **local** Bedford–Taylor construction for the bounded `Omega`-psh potential `u_t` and compactness of `K`, with no global compactness assumption. Fix a compact exhaustion `K_j` of the second-countable complex manifold `X`; the countably many measurable sets `K_jcap D_m` (`j,m>=1`) cover `X\setminus\{u=-infty\}`. Each has finite extended measure, while the pole set has zero measure. Hence the extended measure is σ-finite, and is locally finite **on each finite-level set** (in the sense of finite mass on `Kcap D_t`). If `X` itself is compact, set `K=X` to recover the printed stronger finite-level claim.

The proof's current sentence at line 89 (“the mass of this measure is bounded by that of the bounded product”) is sound only as a **local mass estimate**, or globally when that bounded product has finite total mass. Boundedness of a potential alone never implies finite global mass on a noncompact manifold.

## Proposed correction and effects

Replace the phrase in Theorem 13.14.3, line 67,
> it is finite on each `D_t` and σ-finite on `X`

by
> for every compact `K subset X` and `t>0`, its restriction to `K intersect D_t` has finite mass; it is σ-finite on `X`. If `X` is compact (or the relevant bounded comparison products have finite total mass), it is finite on each `D_t`.

Modify proof line 89 to insert compact `K` before applying the bounded-product estimate, then use a countable compact exhaustion. Alternatively add **compact X** explicitly to Theorem 13.14.3, but doing so unnecessarily narrows its valid local construction. These are **proposals, not applied body edits**.

**Affected dependents:** any use of Theorem 13.14.3 to deduce global finite mass of truncation levels on noncompact `X`; its σ-finite and decomposition-invariance conclusions, the compact-case construction, and the compact geometric applications are not refuted. No downstream statement is reclassified without checking its own hypotheses. This is a false **finiteness clause**, not a failure of the non-pluripolar truncation existence proof.

**Coverage and constraints:** First direct proof-level examination here of Theorem 13.14.3 and its finite-level argument; selected crosschecks of §§13.1, 5.28 only. §13.14 already had some other numbered entries sampled: **+0 first-visited sections, +0 fully certified sections**. Current tracked ToC: 25 chapters / 747 numbered sections. No software build, test suite, CI, formal verification, source edit, registry/tag change, main edit or publication. Existing Demailly approximation/regularization and dedicated Bergman, L², OT, multiscale-atlas, positivity-loss proof programme remains **deferred-by-user**, not reviewed and not certified.
