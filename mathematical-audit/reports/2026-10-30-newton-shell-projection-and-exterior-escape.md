# Mathematical audit — exact radial Newtonian balayage and escape at infinity (2026-10-30)

- **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Audit branch read before writing:** `review/mathematical-audit` at `01ad380bdbcd38544d217ff794fea88f77185a82`.
- **New stable finding:** `POME-GREEN-SPHERE-SWEEP-ESCAPE-001`.
- **Severity/status:** low / **verified conditional deduction** (independent exact model, conditional only in its identification with Pome's abstract Green-energy projection terminology). **Neither a false theorem nor a claimed repair of the general proof.**
- **Actual scope:** the precise selected claims of Theorem 4.5.6, its energy pairing in §4.5.1, and the ordinary exterior-harmonic clause of Theorem 4.4.11. Theorem 4.5.2, Theorem 4.5.4, and Example 4.5.5 were consulted for conventions and differentiation from prior audit work; their entire proof chains were **not** newly certified.
- **Excluded scope:** Demailly approximation/regularization and the dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme were not examined. All old notes on them remain **deferred-by-user**, neither solved nor verified.

## Integrated reading-edition anchors and provenance

1. `docs/sections/green-energy-and-martin-boundaries/index.html` on reviewed main; **blob SHA** `976a90f2a5eba299658f73a1eee8b9d3fef8020f`. §4.5.1 positive Green-energy normalization `I(\mu,\nu)=\iint G\,d\mu\,d\nu`, physical lines **5–13**; Theorem **4.5.2**, source label `classical-potential-theory:AEA69819`, permanent Pome tag `CC3D1AD9179B`, lines **16–30**; Theorem **4.5.4**, source label `classical-potential-theory:5FB19CB2`, permanent tag `CE0D5F4DF7B2`, lines **46–68**; Example **4.5.5**, source label `classical-potential-theory:898691BF`, permanent tag `61A5D2A82793`, lines **70–73**; Theorem **4.5.6**, source label `classical-potential-theory:9D70EB64`, permanent tag `B15EFD960FD5`, statement and proof lines **76–86**. The projection criterion there is `G\mu^K\le G\mu` globally, with equality quasi-everywhere on `K`, or equivalently the energy orthogonality/variational inequality.
2. `docs/sections/perron-theory-and-fine-boundary-limits/index.html` on reviewed main; **blob SHA** `4bc2fb9317e2b6f6bb5b2d90208c677da8275eba`. Theorem **4.4.11**, source label `classical-potential-theory:07EA9CB6`, permanent tag `E16C09608A00`, statement lines **122–131** and proof **135–148**. Its exterior formula permits an ordinary harmonic function with sphere boundary data and an independently prescribed finite value `alpha` at infinity; the stronger Helms-harmonic convention requires `alpha` to be the boundary average.

The cited source labels are the exact integrated `data-tag` identifiers (not unrelated original-source theorem numbers). Historical attribution in the original reading edition is left intact.

## Exact calculation: sweeping radial measures onto a fixed sphere

Let `d>=3`, `Omega=R^d`, and choose the Newtonian Green kernel
\[
G(x,y)=|x-y|^{2-d},
\qquad -\Delta G(\cdot,y)=(d-2)|S^{d-1}|\,\delta_y.
\]
Write `S_r={|x|=r}`, and denote by `sigma_r` the **probability** surface measure on `S_r`. All finite-energy statements below use the signed energy pairing of §4.5.1. The ambient `R^d` is Greenian for `d>=3`.

**Newton's shell identity.** Rotational invariance makes `U_r=G\sigma_r` a radial function. It is harmonic both inside and outside the support sphere. The radial harmonic functions on `(0,r)` regular at the origin are constant; those on `(r,\infty)` decaying at infinity are multiples of `rho^{2-d}`. Total mass one fixes the exterior coefficient to one, and continuity across the sphere fixes the interior constant. Thus, at every point,
\[
\boxed{G\sigma_r(x)=\max\{r,|x|\}^{\,2-d}.} \tag{A}
\]
In particular, without any appeal to the general abstract projection theorem,
\[
 I(\sigma_r,\sigma_t)=\max\{r,t\}^{\,2-d},
 \qquad \|\sigma_r\|^2=r^{2-d}<\infty. \tag{B}
\]
This uses the exact coefficient of the normalized Green kernel, not an unspecified dimensional constant.

Fix `s>0`. For a single source radius `r`, put
\[
a_s(r)=\begin{cases}
1,&0<r\le s,\\
(s/r)^{d-2},&r>s.
\end{cases}
\qquad \nu_{r,s}=a_s(r)\sigma_s.
\]
By (A), `G\nu_{r,s}=G\sigma_r` at **every** point of `S_s`. Moreover,
\[
 G\nu_{r,s}\le G\sigma_r\quad\text{throughout }R^d. \tag{C}
\]
Indeed, if `r\le s`, the two potentials agree outside `S_s`, and the constant interior potential `s^{2-d}` is no larger than `G\sigma_r`. If `r>s`, they agree for `|x|\le s`, while for `s<|x|<r` the inequality is `a_s(r)|x|^{2-d}\le r^{2-d}`; for `|x|\ge r` it follows from `a_s(r)\le1`. This checks all radial regions, including both endpoints.

Let `C_s` be the positive cone of finite-energy Radon measures supported on `S_s`. For every `tau in C_s`, (A) gives
\[
 I(\sigma_r-\nu_{r,s},\tau)
 =\int_{S_s}(G\sigma_r-G\nu_{r,s})\,d\tau=0,
 \qquad I(\sigma_r-\nu_{r,s},\nu_{r,s})=0. \tag{D}
\]
Consequently, for every such `tau`,
\[
 \|\sigma_r-\tau\|^2
 =\|\sigma_r-\nu_{r,s}\|^2+\|\tau-\nu_{r,s}\|^2. \tag{E}
\]
Thus `nu_{r,s}` is the **unique** Hilbert-energy nearest point in `C_s`; the printed Theorem 4.5.6 correctly identifies it as the balayage of `sigma_r` onto `S_s`. Equation (C) independently checks its globally ordered-potential characterization.

More generally let `mu` be a **finite, positive, rotation-invariant, finite-energy** Radon measure on `R^d`. Disintegrate it radially as `mu=\int_0^\infty sigma_r\,dM(r)` (an atom at `r=0` is excluded by finite energy). Newton's formula and positive Tonelli give a constant on `S_s`:
\[
 (G\mu)|_{S_s}=\int_0^\infty \max\{s,r\}^{2-d}\,dM(r).
\]
Put
\[
\boxed{\quad
 c_s=\int_0^\infty a_s(r)\,dM(r)
 =\mu(\overline B_s)
   +s^{d-2}\int_{|y|>s}|y|^{2-d}\,d\mu(y),
 \qquad
 \mu^{S_s}=c_s\sigma_s.\quad} \tag{F}
\]
Here `0\le c_s\le\mu(R^d)<\infty`; `c_s sigma_s` has finite energy. Integrating (C) gives global potential domination, and the potentials agree on `S_s`. Orthogonality (D) and Pythagoras (E) therefore apply verbatim to `mu` and `c_s sigma_s`. No interchange of signed infinite integrals is used: `mu` and `sigma_s` have finite energy, the mixed pairing is finite by Cauchy–Schwarz, and the radial disintegration uses nonnegative potentials. The exact residual energy is
\[
 \boxed{\ \|\mu-\mu^{S_s}\|^2
       =\|\mu\|^2-c_s^2s^{2-d}.\ } \tag{G}
\]

For a **single shell**, (E) yields the two distinct formulas
\[
 \|\sigma_r-\sigma_r^{S_s}\|^2
 =\begin{cases}
 r^{2-d}-s^{2-d},&r\le s,\\[2pt]
 r^{2-d}-s^{d-2}r^{-2(d-2)},&r>s.
 \end{cases} \tag{H}
\]
In particular, outward sweeping from `r<s` preserves total mass one; inward sweeping from `r>s` leaves mass `(s/r)^{d-2}<1`. This **mass loss on inward sweeping** is not a violation of positivity or of the energy projection theorem.

## Exact comparison with the exterior Dirichlet term

On the exterior `|x|>s`, the function
\[
 h_s(x)=(s/|x|)^{d-2}
\]
is ordinary harmonic, has boundary value one on `S_s`, and tends to zero at infinity. By uniqueness for bounded ordinary harmonic functions with these boundary conditions, it is the relative sphere-hit weight. Its complement `1-h_s` is the escape-to-infinity weight. The point-source shell calculation gives
\[
 1-\sigma_r^{S_s}(R^d)
 =1-(s/r)^{d-2}=1-h_s(r),\qquad r>s. \tag{I}
\]
Thus the loss in (F) is the integral of the same escape weight over exterior source radii. This matches the last term `alpha[1-(R/r)^{d-2}]` in the **ordinary exterior harmonic** representation in Theorem 4.4.11, distinguishing the independent infinity value `alpha` from the boundary average. The function `h_s` with limit zero is **not** claimed Helms-harmonic at infinity when its sphere boundary average is one; that stronger condition would instead select the constant function one. This qualifier prevents conflating the compactified Helms convention with the ordinary exterior Dirichlet solution.

## Disposition, dependencies, and exact scope

**Status:** `POME-GREEN-SPHERE-SWEEP-ESCAPE-001`, **low / verified conditional deduction**. The model provides a complete direct proof of (A)–(I), including normalization and mass accounting. The original Theorem 4.5.6 and Theorem 4.4.11 remain **correct** in the inspected specializations. This does **not** certify abstract potential-theoretic existence, completeness of the signed energy space, or the Martin representation theorem.

**Suggested optional addition:** a short model example after Theorem 4.5.6 showing the distinction between outward mass-preserving and inward mass-losing spherical sweeping, together with the relation to the ordinary exterior kernel in 4.4.11. Keep permanent tags, historical attribution, the Helms-at-infinity convention and source variants unchanged. No source/body/registry edits were made.

**Prior findings not repeated:** `POME-MARTIN-GREEN-002`, `POME-GREEN-ENERGY-WEAK-NONSTRONG-SPHERES-001`, `POME-GREEN-SWEEP-NONEXPANSIVE-001`, and older energy/capacity results concern incompleteness, weak-versus-strong convergence, or contraction. None calculates the two-sided projection or radial mass escape in (F)–(I). Their statuses are unchanged.

**Coverage:** incrementally reviewed the specified theorem/definition passages in §§4.4 and 4.5; no entire section certified. The authoritative current table of contents still contains **25 chapters and 747 numbered sections**, with **zero completely certified sections**. All earlier confirmed errors, proof gaps, external dependencies and deferred records remain open at their historical status. No build, automated tests, formal verification, CI, publication, or mutation of main/source/published pages was performed.
