# Audit: cutoff-independent Martin compactification and finite coefficient comparison

**Date:** 2026-11-22. **Baseline:** `main` at `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Audit head read before writing:** `6a53d58bef1ba4dbc53eb01e1cc4e2b624e235a0`.
**Finding:** `POME-MARTIN-CUTOFF-CANONICAL-BOUNDARY-001` — **low / verified conditional deduction**, NOT a false theorem, source correction, or complete transitive proof certificate.
**Scope:** whole present-main integrated §4.5 (mathematical lines 7–213; prior direct partial visit), whole §§10.64 (lines 8–53) and 10.65 (lines 8–75). No claim of historically first visits. No regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas or positivity-loss programme reviewed.

## Pinned integrated sources and exact anchors

- `docs/sections/green-energy-and-martin-boundaries/index.html`, main blob `976a90f2a5eba299658f73a1eee8b9d3fef8020f`: Lemma 4.5.8, permanent `D878F27BAB16`, lines 95–102; cutoff/normalized kernel in lines 105–106; Theorem 4.5.9, permanent `9D6B5CF5E0CF`, lines 110–122; Lemmas 4.5.10–11, permanents `B0A113187C30`, `FDE7BF6A9927`, lines 126–161; Theorems 4.5.12–13, permanents `6736FBE7368C`, `0E65F552B1A6`, lines 166–213. Earlier energy/cone arguments are lines 7–86 (previous partial visit; directly rechecked here).
- `docs/sections/spectral-sequences-support-and-cup-products--a-finite-integer-complex-and-coefficient-comparison/index.html`, blob `5dfc94ab65a71cdd8cfe9d648552a9f014056fdf`: Theorem 10.64.1, permanent `F04BCA811EFA`, lines 8–19; Lemma 10.64.2 `7C6F99D51075`, lines 24–37; Theorem 10.64.3 `04921B659563`, lines 42–53.
- `docs/sections/spectral-sequences-support-and-cup-products--integral-two-periods-on-a-real-torus/index.html`, blob `5919e95b6add69bc972ee1fb6d7c587a4dac46eb`: Theorem 10.65.1 `19630A31AE86`, lines 8–51; Proposition 10.65.2 `769E96CD43B2`, lines 56–75.

## Finding POME-MARTIN-CUTOFF-CANONICAL-BOUNDARY-001: the boundary and its minimal representation do not depend on the compact cutoff

**Hypotheses.** Let \(\Omega\) be connected and Greenian with reference point \(a\). Let \(b_1,b_2:\Omega\to(0,\infty)\) each satisfy the exact conditions of the cutoff in §4.5, in particular \(b_i(y)=G_\Omega(y,a)\) outside some compact \(C_i\Subset\Omega\). (In the reading edition these are \(b_i=\phi_i(G_\Omega(\cdot,a))\), for smooth increasing concave cutoffs \(\phi_i\) equal to the identity below a sufficiently high threshold and constant near the pole.) Let \(M_i\) be the compact Hausdorff compactification of Lemma 4.5.8 for the coordinate functions \(k_y^{(i)}(x)=G_\Omega(y,x)/b_i(y)\) and \(C_c(\Omega)\), with boundary \(\Delta_i=M_i\setminus\Omega\).

**Claim.** There is a unique homeomorphism \(F:M_1\to M_2\) that fixes every \(y\in\Omega\) and identifies the boundary kernels **without any rescaling**:
\[
K^{(2)}(F(z),x)=K^{(1)}(z,x)\qquad(z\in\Delta_1,\;x\in\Omega).
\]
It maps the minimal Martin boundaries \(\Delta_{1,\min}\) and \(\Delta_{2,\min}\) bijectively. The finite representing measures of a positive harmonic function, when taken on the respective minimal boundaries, correspond by pushforward under \(F\). The constant-one representing measure and the Perron representation for continuous boundary data correspond likewise.

**Proof.** Put \(C=C_1\cup C_2\). The two defining kernel coordinates agree **simultaneously for every interior test point \(x\)** whenever \(y\notin C\):
\[
k_y^{(1)}(x)=\frac{G(y,x)}{G(y,a)}=k_y^{(2)}(x).
\]
A net of interior points converging to any boundary point of \(M_1\) is eventually outside **each** compact \(K\Subset\Omega\). Indeed the embedded compact \(K\) is closed in the Hausdorff compactification and its complement is a neighborhood of the boundary point. This is a net argument, not an unlicensed sequential-compactness assertion. Every \(C_c(\Omega)\) coordinate has the same prescribed extension in both constructions. Thus along such a net all the \(k^{(2)}\) coordinates eventually agree with the \(k^{(1)}\) coordinates and have definite limits. Compactness of \(M_2\) supplies a cluster point; boundary coordinate separation in Lemma 4.5.8 makes that cluster point unique, and it has the claimed normalized kernel values. Reversing the roles of the cutoffs gives the inverse identification.

For continuity at a boundary point, take an arbitrary net of points of \(M_1\) converging to it. Eventually this net avoids the closed image of \(C\). At interior points outside \(C\) the relevant coordinates agree; at boundary points their extended coordinates agree by the preceding argument. Hence every defining coordinate of the image in \(M_2\) converges. The same argument applies in reverse; the map is a homeomorphism, and by construction it is the identity on \(\Omega\). The equality of boundary kernels preserves their positive harmonic extreme-ray property; therefore \(F(\Delta_{1,\min})=\Delta_{2,\min}\). Integrating the equal kernels against the pushforward of a representing measure yields exactly the original harmonic function. Uniqueness of minimal-boundary representation in Theorem 4.5.12 identifies the two measures; Theorem 4.5.13 then identifies the representing measure of one and its Perron integrals, with boundary data transported by \(F\). No new assertion about uniqueness of arbitrary nonminimal representing measures is made. \(\square\)

**Why this matters.** §4.5.9 uses a cutoff \(b\) to remove the interior pole. The boundary kernel and its normalized minimal representation are canonical despite that local auxiliary choice. This is a compatibility/canonicalization verification, not a duplicate of the already recorded explicit strip, exterior-ball, punctured-domain, or nested-sweep model findings.

**Status and proposed insertion:** low / **verified conditional deduction** based on the printed compactification and Martin representation theorems. An optional English remark after Theorem 4.5.9 would record cutoff independence; **do not edit production source, permanent tags, or canonicalization registry automatically**. Downstream dependencies: Lemmas 4.5.10–11 and Theorems 4.5.12–13 and all comparisons of Martin models. This proof does not independently certify their compact-sweep, Riesz, Harnack or Perron input chains.

## Independent second rotation: finite integer cochains and the real torus

Entire §§10.64 and 10.65 were directly inspected on this exact main revision. Theorem 10.64.1 builds **one finite integral Čech complex** from a finite good cover, then compares \(D^\bullet\otimes A\) with sheaf cohomology naturally for every abelian group \(A\); the Noetherian hypothesis is used only for finite generation over \(R\). Lemma 10.64.2 separately identifies the torsion kernel of the integral-to-real map using an integer matrix, and Theorem 10.64.3 transports this through the natural comparisons. We did not replace homotopy/acyclic-good-cover or de Rham comparison inputs with an uncertified assertion.

For Theorem 10.65.1 check the deck transformation **including its sign**. The action
\((x,z)\mapsto(x+\gamma,e^{2\pi i\gamma_jx_k}z)\)
gives the lifted section transformation \(e(x+\gamma)=e^{-2\pi i\gamma_jx_k}e(x)\). Therefore \(B=-2\pi i x_j\,dx_k\) satisfies the requisite transformation, \(dB=-2\pi i\,dx_j\wedge dx_k\), and \((i/2\pi)dB=+dx_j\wedge dx_k\): no sign reversal was found. Proposition 10.65.2 constructs averaging with a Cartan homotopy; the averaged closed form has a **unique** constant representative. Consequently a closed real two-form \(\eta\) on \(V/\Gamma\) has integral class precisely when the coefficients of its averaged constant form in the dual lattice coordinates are integers. For rational coefficients the least positive integer scaling it into the integral image is the least common multiple of reduced denominators (a direct corollary, not a separate ledger finding). Neither theorem is claimed false. The remaining topological prerequisites are recorded as genuine existing inputs, not new discoveries.

## Review accounting and boundaries

- **Whole current integrated mathematical text directly read:** §4.5 lines 7–213 (including Martin 4.5.8–13 **not** whole-section-certified by the 19 November partial report); §10.64 lines 8–53; §10.65 lines 8–75. **Three whole current sections**, with previous selected §4.5 overlap explicitly disclosed; no first-ever-visit claim.
- **New stable finding:** exactly **one** low / verified conditional deduction. **Confirmed original false theorem: zero.** **Confirmed proof gap: zero.** **Complete transitive upstream proof-chain certificates: zero.** Underlying Martin compactification, reduction, Riesz, topological compactness and good-cover comparisons remain conditional inputs and deserve future review.
- No tests, scripts, builds or CI executed; no source/body/registry/tags/site/main changes. The Demailly regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss work remain **deferred-by-user**, neither resolved nor certified.
