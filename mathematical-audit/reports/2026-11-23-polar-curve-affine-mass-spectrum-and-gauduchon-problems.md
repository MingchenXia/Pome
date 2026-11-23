# Polar-curve affine non-pluripolar mass spectrum and Hermitian problem rotation — 2026-11-23

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Audit branch:** `review/mathematical-audit`. **New stable finding:** `POME-POLAR-CURVE-AFFINE-NPP-MASS-SPECTRUM-001`, **low / verified conditional deduction**, not a counterexample to any printed theorem. All first-visit claims are withheld pending historical reconciliation. This report concerns the actual integrated reading edition; external sources were not used to substitute for its proofs.

## New deduction: all masses in [0,1] with the same trivial multiplier ideals

**Primary integrated reading-edition anchors:** `docs/sections/non-pluripolar-products--bounded-factors-and-the-first-degree-product/index.html`, main blob `d234ab96e33bfd24ad1d53d29332b2c021cddeff`, Proposition **13.4.7** at physical lines **195–250**, permanent tag `3553558C2E27` (degree-one non-pluripolar restriction); Proposition **13.4.10** at lines **255–282**, permanent tag `FB5ACFB46DB8` (projective-line potential); Example **13.4.11** at lines **287–295**, permanent tag `E9D7DF5798B0` (atomless polar carrier). This uses a theorem and example already stated/proved in Pome; their entire upstream dependency graph is not independently certified.

**Statement.** There exist normalized Fubini–Study `(P^1, omega)`, an atomless probability measure `mu` supported on a compact polar set `K`, and a nonpositive `omega`-psh function `q` such that, with `q_0 := 0` and `q_t := t q` for `0<t<=1`,

1. every `q_t` has **zero Lelong number at every point**, and `I(s q_t) = O_{P^1}` for every real `s>0`;
2. every full positive current `T_t := omega + dd^c q_t` has mass `int_{P^1} T_t = 1`, while
3. its degree-one non-pluripolar measure is exactly
   ```
   <T_t> = (1-t) omega,     int_{P^1} <T_t> = 1-t    (0 <= t <= 1).
   ```

Thus all non-pluripolar masses from zero through one occur along one affine family of currents with identical (trivial) multiplier ideals and zero pointwise Lelong numbers. No assertion of identical *ordinary singularity types* is made.

**Proof.** Example 13.4.11, using Proposition 13.4.10 and the atomless polar-carrier measure of Proposition 4.1.12 (permanent tag `EBEA4A14BCD2`), supplies a compact polar `K`, probability `mu` supported on `K`, and `q` satisfying
```
omega + dd^c q = mu,       q|_K = -infinity,
nu(q,x) = 0 for all x,     I(cq) = O_{P^1} for all c > 0.
```
For `0<t<=1`, convexity of positive currents gives
```
T_t = omega + dd^c(tq) = (1-t)omega + t mu >= 0.
```
The pole sets of `q_t` and `q` are identical, and include `K`. Since a polar set is Lebesgue-null and `omega` is smooth, the pole set is `omega`-null. Since `mu` is carried by `K`, the degree-one identity of Proposition 13.4.7 gives
```
<T_t> = 1_{q_t > -infinity} T_t
      = (1-t) 1_{q > -infinity} omega
        + t 1_{q > -infinity} mu
      = (1-t)omega.
```
The case `t=0` is immediate because `q_0` is the identically zero function, so `<omega> = omega`. Integration uses the convention `int omega = mu(P^1) = 1`. All `T_t` have cohomological mass one, by the displayed affine identity. Their Lelong numbers are `t nu(q,x)=0`; and `I(s q_t)=I(stq)=O` is the original example's conclusion when `t>0`, while `t=0` is smooth. QED.

**Classification:** verified **conditional deduction** from printed results; no false statement, no unproved strengthening of an excluded regularization theorem, and no transitive certification. **Distinctness:** Example 13.4.11 only exhibits the two endpoints `0` and `q`; this records the exact affine *measure* and complete mass spectrum. It is distinct from the earlier toric maximum model, divisorial excision and curve pole-counting reports. **Potential downstream use:** comparisons of non-pluripolar mass with Lelong data, multiplier-ideal types and cohomological mass; no reader-body/registry/tag change is authorized.

## Direct whole current-section audit: §13.4

**Path/blob as above, complete integrated mathematical lines 7–295.**
- Lemma **13.4.1** (permanent `263D0F5AEE0A`, lines 11–68): tracked weighted CLN inequality, collar replacement, its sign in `dd^c kappa = -b`, the `b=beta/pi` normalization, increasing negative weights by monotone convergence and auxiliary-variable treatment of bidimension one. No new confirmed discrepancy.
- Lemma **13.4.2** (permanent `5D93FCFBA57F`, lines 73–94): checked the negative-psh series, summable negative weighted trace integral, vanishing of pluripolar mass, and induction for bounded Bedford–Taylor factors. No new confirmed discrepancy.
- Proposition **13.4.3** (`90E0E28D9A95`, lines 99–126): checked the use of the local-finiteness/closedness of the base, the plurifine cutoff and the zero-mass-on-poles condition in identifying mixed bounded products. No independent certification of every cited approximation/continuity lemma.
- Lemmas **13.4.4** (`CA3A887474EE`, lines 134–153) and **13.4.5** (`4AD0BFC1BFCD`, lines 158–190): reviewed measurable-kernel Dynkin-system proof, fiberwise BT/Fubini, the distinction between bounded Borel and nonnegative extended Borel tests, local mass bounds and smooth signed-base-form extension.
- Propositions **13.4.7** (`3553558C2E27`, lines 195–250) and **13.4.10** (`FB5ACFB46DB8`, lines 255–282), Example **13.4.11** (`E9D7DF5798B0`, lines 287–295): checked the degree-one pole-set restriction, planar `dd^c=Delta/(4pi)` convention, slicing argument, Fubini–Study potential at infinity and the contrast between ordinary mass and non-pluripolar mass.

**Status:** section read directly in full, no new confirmed printed mathematical error. Cited upstream §7.2.5, §7.3.7, §13.2.6, §13.3.1 and the polar-carrier construction §4.1.12 remain independently uncertified as complete transitive chains.

## Two independent whole current-section audits in Chapter 24

### §24.2 — Threshold equations and singular limits

**Integrated path:** `docs/sections/problems-in-hermitian-pluripotential-theory--threshold-equations-and-singular-limits/index.html`, main blob `cb587f6666e775e88de2cc2aefa9c6a1dddd96e7`, entire mathematical lines **7–113**. Problem **24.2.2**, permanent `FBE8C5BA5CA4`, lines **27–31**.

Read all five displayed problem/analysis subsections. Checked logical separation of a positive density threshold `b_h(f)>0` from attainment of an **exact** Monge–Ampère equation, that an optimal inequality subsolution need not have finite mass, and that total-variation convergence of right-hand sides does not imply capacity convergence of normalized potentials. The source correctly keeps the zero-lower-mass/general-`L^1` question open and records partial product/density/dual criteria as conditional special cases. Also distinguished uniqueness of a scalar from uniqueness of a potential when density vanishes, and conditional selection limits from universal uniqueness. **No new confirmed error and no general open problem solved.** This is a whole **direct reading**, not certification of all of §15 or of the many downstream cross-references.

### §24.3 — Positive Gauduchon volume and bigness

**Integrated path:** `docs/sections/problems-in-hermitian-pluripotential-theory--positive-gauduchon-volume-and-bigness/index.html`, main blob `e64a919194dbc4dbd1739cd02811a5c45e252358`, entire mathematical lines **7–84**. Proposition **24.3.2**, permanent `32F82EA89236`, lines **27–68**, inequality **(24.3.3)** at lines **62–64**.

Direct check: with `A_h(gamma)=1`, the threshold `kappa_h(theta)=inf A_theta/A_h`; the volume root `lambda_mu(theta)=inf A_theta/D_mu` yields `lambda_mu(theta) D_mu(gamma) <= A_theta(gamma)`. If the background is pseudoeffective but not big, the quoted threshold criterion gives `kappa_h(theta)=0`; hence normalized minimizing sequences satisfy `A_theta->0`, and `lambda_mu>0` forces `D_mu->0`. For any threshold-minimizing sequence with `liminf D_mu>=delta>0`, passing to lower limits yields `kappa_h>=delta lambda_mu`, exactly as printed. Scaling `gamma` affects `A_h,A_theta,D_mu` by the same factor `t^(n-1)`. The distinction between closed nef and nonclosed backgrounds and the question in complex dimension two remain correctly qualified. **No new confirmed error**, no new claim about the open surface case. Upstream Gauduchon threshold §11.6.2 and determinant variational §12.2.1 not independently certified as full chains.

## Previously reviewed context, not newly counted

Directly re-read the complete integrated §13.2 (blob `81be8c5acc360c96bd3c5acba05a3cdb5fafaf4c`, lines 7–165), §13.3 (blob `f781fa61bd20944c7c4798e0e0984cfb81ef069f`, lines 7–50), §17.2 (blob `5779ef1a17a52e02052c7485a7aa04adf606aace`, lines 7–227), and §21.7 (blob `5d209b7f4d2156c19bc3fb300303405df6321230`, lines 7–105), focusing on poles vs coefficient measures, cutoff-gradient bounds, quasi-psh integration by parts, and lattice-volume normalization. All four already have historical full-review entries and **are not counted as new full-section coverage or new findings**.

## Coverage, dependency and write boundaries

- **New current full direct sections:** 3 (§13.4, §24.2, §24.3); **whole repeats:** 4 (§13.2, §13.3, §17.2, §21.7). **New mathematically demonstrated deduction:** 1; **new confirmed original errors:** 0; **complete transitive proof-chain certificates:** 0. Prior first visits remain unreconciled.
- Current `main` contains **747 unique sections** according to `docs/chapters/index.html`; the review matrix has **747 distinct matching rows** with no missing or extra section number. A row marked `LEGACY-UNRECONCILED` does not mean never previously reviewed.
- **Deferred-by-user (unchanged, not solved/certified):** Demailly approximation and regularization, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programmes. Some referenced results may have further excluded premises; those were not reopened.
- No tests, builds, GitHub Actions CI, full mathematical verification, source/reader/registry/permanent-tag edits, merge, website publication, or changes to `main` were performed. This audit is documentation-only on the review branch.
