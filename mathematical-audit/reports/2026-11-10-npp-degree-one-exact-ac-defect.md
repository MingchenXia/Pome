# Exact degree-one non-pluripolar versus absolutely continuous defect

**Finding:** `POME-NPP-DEGREE-ONE-AC-DEFECT-001`. **Date:** 2026-11-10. **Severity:** low. **Status:** verified conditional deduction (conditional only on the separately printed upstream degree-one identity); **not** a false printed theorem, a source repair, or a certification of its dependency chain.

**Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. The current integrated reading edition, not a source theorem number alone, was inspected:

- `docs/sections/non-pluripolar-products--bounded-factors-and-the-first-degree-product/index.html`, blob `d234ab96e33bfd24ad1d53d29332b2c021cddeff`: Proposition **13.4.7**, source `foundations-of-pluripotential-theory:D1BF7EF2`, permanent tag `3553558C2E27`, physical lines **195–253**; its equation **13.4.8**, source `foundations-of-pluripotential-theory:4317EC97`, permanent `6DEB3D875595`, physical lines **197–200**. Proposition **13.4.10**, source `foundations-of-pluripotential-theory:A7D5A0E9`, permanent `FB5ACFB46DB8`, **255–286**, used for normalization context only.
- `docs/sections/absolutely-continuous-and-non-pluripolar-mass/index.html`, blob `bea17d8041a7af4a252913e0f700b44d77521f82`: Lemma **13.31.1**, source `transcendental-positive-cones:6D2B462A`, permanent `C7894CAD8593`, **8–99**, including the first-degree identity explicitly recalled at **71–77**. Corollaries **13.31.3–4**, source `transcendental-positive-cones:A2E98A80` / `:AA4B08E5`, permanent `1E1CF458220D` / `04768594F11F`, **104–138**, were checked only for downstream context.
- Pome's fixed convention is `dd^c = i/(2 pi) partial barpartial`, hence `dd^c log|z|^2 = delta_0` on a complex line.

## Exact general degree-one statement and proof

Let `X` be a complex manifold, `T` a closed positive (1,1)-current, and let `u` be a local plurisubharmonic potential, `T=dd^c u`. Decompose the coefficient-measure tensor relative to smooth Lebesgue volume as `T=T_ac+T_s`, with `T_s` singular and positive (in the Hermitian tensor sense). On overlapping charts, two potentials differ by a finite pluriharmonic function, so their `-infinity` sets agree. Define the intrinsic pluripolar pole set `P(T)={u=-infinity}`.

Proposition 13.4.7 and Eq. 13.4.8 state the locally finite degree-one identity

`<T> = 1_{X\setminus P(T)} T`.

Every pluripolar set is Lebesgue-null. Consequently `1_{X\setminus P(T)} T_ac=T_ac`. Taking the mutually singular Lebesgue components of this exact restriction gives the **positive-current identity**

`<T> - T_ac = 1_{X\setminus P(T)} T_s >= 0.`  (**)

It follows, **without any closedness claim for `T_ac` or `T_s`**, that equality `<T>=T_ac` holds if and only if the singular trace measure of `T` is supported on `P(T)`. Indeed, a positive Hermitian tensor-valued measure is zero exactly when its trace measure is zero. No general assertion about higher wedge powers follows by subtracting tensor components; the proposition concerns degree one only.

On a compact Riemann surface, all (1,1)-currents are top-degree measures. Integration of (**) is therefore a complete measure-theoretic classification of the gap in the `n=1` instance of Lemma 13.31.1. On higher-dimensional complex manifolds (**) is a current identity, not a top-degree volume formula.

## Explicit sharp projective-line model

Let `X=P^1`, with affine coordinate `z`, and `omega=dd^c log(1+|z|^2)`, extended as the normalized Fubini–Study form, `int_X omega=1`. Define the probability currents `D=[z=0]` and `sigma`, normalized arclength on the unit circle `|z|=1`. In the affine chart,

`dd^c log|z|^2=D`, and
`dd^c log max(1,|z|^2)=sigma`.

For the second formula, the radial derivative is zero inside the circle and `2/r` outside; its flux jump across `r=1` is `4 pi`, and `dd^c=(4 pi)^{-1}Delta` as planar measures. Both displayed potentials have logarithmic growth at infinity; subtracting `log(1+|z|^2)` yields global quasi-psh potentials
`v_D=log(|z|^2/(1+|z|^2))`,
`v_sigma=log(max(1,|z|^2)/(1+|z|^2))`,
where `v_D` extends smoothly near infinity and has sole pole `z=0`, while `v_sigma` extends continuously everywhere.

Choose any `a,b>=0` with `a+b<=1`. Then

`T_{a,b}=(1-a-b)omega+aD+b sigma = omega+dd^c(a v_D+b v_sigma)`

is a closed positive current in `[omega]`. Its potential is `-infinity` precisely at `z=0` when `a>0`, and nowhere when `a=0`. The analytic point mass `aD` is supported on the pole set; the unit-circle measure `b sigma` is singular relative to area but **disjoint from that pole set and therefore not discarded**. The disjoint Lebesgue decomposition and (**) now give, exactly as positive measures,

`(T_{a,b})_ac=(1-a-b)omega`,
`<T_{a,b}>=(1-a-b)omega+b sigma`,
`<T_{a,b}>-(T_{a,b})_ac=b sigma`.

Taking masses (`int omega=int D=int sigma=1`),

`int_X <T_{a,b}>=1-a,`
`int_X (T_{a,b})_ac=1-a-b,`
`int_X (<T_{a,b}>-(T_{a,b})_ac)=b.`

Thus `a` independently measures the **discarded polar part** of `T`, while `b` measures the **retained singular, nonpolar part**. Equality in Lemma 13.31.1 for `n=1` holds throughout the subfamily `b=0`, even when `a>0`; the opposite endpoint `a=0,b=1` has full NPP mass one and absolutely continuous mass zero. For `a>0,b>0`, both phenomena occur in the *same current*.

This distinction is more informative than an inequality alone. It does **not** repeat the earlier `POME-NPP-MIXED-AC-WEDGE-ORDER-001` (a mixed tensor inequality and coordinate-circle example), or `POME-FULLMASS-SINGULAR-AC-001` (full-mass singular examples on higher-dimensional tori). No mathematical statement in the integrated edition is contradicted.

## Classification, dependencies, and proposed addition

- **Verdict:** verified conditional deduction; **no confirmed error** and **no proof gap alleged** in Proposition 13.4.7 or Lemma 13.31.1. The exact identity uses Proposition 13.4.7 as a standing *internal* dependency; the whole fiber-disintegration proof of that proposition and its earlier inputs were read locally but **not transitively certified**. The explicit Laplacian jump, Lebesgue decomposition and two-parameter computations are complete.
- **Suggested body-level change, proposed only:** add a remark after Proposition 13.4.7 or Lemma 13.31.1 giving (**) and the two-parameter `P^1` example. Do not change either theorem, attribution, conventions, source tags or registry; do not edit production `main`.
- **Affected dependents:** Lemma 13.31.1's `n=1` equality cases, Corollary 13.31.4's possible extremizers (without asserting universal attainment), and interpretation of degree-one polar mass in §13.4.
- **Exclusions and external inputs:** no Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale atlas, or positivity-loss proof programme was opened; all its previous notes stay **deferred-by-user**, never resolved or certified. No new external theorem required.
- **Coverage:** substantive incremental examination of Proposition 13.4.7 / Eq. 13.4.8 and Lemma 13.31.1; only normalization-context consultation of Proposition 13.4.10 and statements of Corollaries 13.31.3–4. §§13.4 and 13.31 were **previously partly reviewed**. **0 first numbered-section proof visits; 0 complete section or dependency-chain certifications; actual current ToC 25 chapters / 747 numbered sections**.
- **Checks actually done:** direct reading-edition statement/proof and source-tag inspection, hand derivation of the distributional radial flux and all decompositions. **No** tests, build, formalization, CI, website publication, or source-body modifications.
