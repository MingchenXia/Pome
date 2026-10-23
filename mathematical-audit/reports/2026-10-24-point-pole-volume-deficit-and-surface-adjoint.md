# 2026-10-24 — sharp point-pole volume deficit and Gauduchon-surface adjoint normalization

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Audit branch at start:** `7fb748161aee81ecfc0e1cf438b604db18f1dfe5`. All findings below are **verified conditional deductions**, not false printed theorems or complete theorem certifications. We read the actual integrated continuous reading edition, not just source title/number metadata. Current ToC: 25 chapters, 747 sections (inventory, NOT audited-complete sections).

## Scope, exact provenance and dependency boundaries

Freshly inspected `main/AGENTS.md`, `main/documentation/proof-expansions.md`, `main/docs/chapters/index.html`, and the review branch README, LATEST, coverage matrix and cumulative ledger. The following are the exact *integrated* main files and blob SHAs:

| Inspected scope | File, blob and physical HTML lines | Stable reader/permanent tags and source labels |
| --- | --- | --- |
| §13.16 conventions: big background, bounded mass, ordinary singularity volumes | `docs/sections/volumes-under-bounded-mass/index.html`, `94d79bfca61602054b9d09b79a76306e11a67d79`, lines 8–26, especially 20,23 | section `EEFEDC3AE6FE`; this scope is in force until §13.28 |
| §13.17 background/singularity monotonicity, addition of positive currents | `docs/sections/volumes-under-bounded-mass--comparison-of-singularity-volumes/index.html`, `7d55ffb2d7cb91897029a9a2101788eb8aa70141`, lines 20–49 and 58–77 | Theorem 13.17.1 `D7019DA65027` / source `non-kahler-pluripotential-theory-6412693D`; Proposition 13.17.2 `1C00C4C5A656` / source `non-kahler-pluripotential-theory-A9C88774` |
| §13.18 stretch/noncollapse, Lelong-deficit bound, full-volume class | `docs/sections/volumes-under-bounded-mass--volume-deficits-and-relative-full-mass/index.html`, `28323e5b08b0f7e53567f641bd9e4223472bc331`, lines 11–48, 54–73, 81–111 | Lemma 13.18.1 `92ABF533A916` / source `non-kahler-pluripotential-theory-ED39D93A`; Proposition 13.18.3 `169DBA6BAF3B` / source `non-kahler-pluripotential-theory-0442EA52`; Theorem 13.18.5 `D73DFBAE1EC1` / source `non-kahler-pluripotential-theory-1000CD7F` |
| §14.10 Gauduchon ansatz, `gamma_0` versus `gamma` | `docs/sections/smooth-monge-ampere-equations--prescribing-a-gauduchon-volume-form/index.html`, `3a16d6685c70f1a5448c2a9c09b240d6fd44ed83`, lines 7–25 | Theorem 14.10.1 `76AF759A4024` / source `non-kahler-pluripotential-theory-3E8336C1` |
| §14.12 linearization, formal adjoint, invariant density | `docs/sections/smooth-monge-ampere-equations--the-adjoint-equation-for-gauduchon-volume/index.html`, `de0b040ee22f128bf16c89048267075a01f15e66`, lines 7–46 and 51–106 | Proposition 14.12.1 `706EB82AB6A2` / source `non-kahler-pluripotential-theory-1A082A94`; Proposition 14.12.3 `029A1D30A55E` / source `non-kahler-pluripotential-theory-DAC00F18`; equation 14.12.4 `BD3712C889A6` |

The Lelong convention in §6.6 is `nu(log |z|^2,0)=1` (integrated `docs/sections/lelong-numbers-and-multiplier-ideals/index.html`, blob `4da528eba15449e622c6459d970935c4b92d4f6d`). `dd^c=i/(2pi) partial bar-partial`. The prior ledger's `POME-LELONG-MASS-DEFICIT-001` treated an earlier general deficit and a **curve** sharpness check; the higher-dimensional point-pole exact saturation below is distinct. The earlier `POME-GAUD-ADJOINT-CROSS-001` checked the adjoint signs; the surface-dependent **if-and-only-if** and normalization below are distinct, not a repeat of that sign check.

## POME-VOL-POINT-LELONG-OPTIMAL-001

**Severity:** low (sharpness/normalization insight). **Status:** `verified conditional deduction`. **Printed §13.18.3 is not contradicted.** The full exponent `1/n` and the universal constant `C_id=1` are optimal for the identity modification of `(P^n,omega_FS)`.

Fix any `n>=1`, normalize `int_(P^n) omega_FS^n=1`, and put
`
p=[1:0:...:0],\quad v=0,\quad
u_a=a\log\frac{\sum_{j=1}^n |Z_j|^2}{\sum_{j=0}^n |Z_j|^2},
\quad 0<a<1.
`
This is a globally defined quasi-psh function, bounded above by zero, smooth off the isolated pole `p`, and `u_a preceq v`. On the affine chart `Z_0=1`, with `s=|z|^2`, the positive curvature current is represented off `p` by
`
omega_FS+dd^c u_a=dd^c U_a(s),\qquad
U_a(s)=(1-a)\log(1+s)+a\log s.
`
It is positive, since
`
U_a'(s)>0,\quad U_a'(s)+sU_a''(s)
=\frac{1-a}{(1+s)^2}>0
`
for every `s>0`; the logarithmic singularity extends as a positive current and the background contribution stays positive. The Lelong number of `u_a` at `p` is exactly `a`.

**Radial flux derivation.** For any smooth radial `U(s)` on a punctured annulus in `C^n`, its complex Hessian has `n-1` tangential eigenvalues `U'(s)` and one radial eigenvalue `U'(s)+sU''(s)`. Polar integration with the stated `dd^c` normalization yields the *exact* annular identity
`
\int_{r<|z|<R} (dd^c U)^n
=\bigl(sU'(s)\bigr)^n\big|_{s=R^2}
 -\bigl(sU'(s)\bigr)^n\big|_{s=r^2}.
`
For normalization, `U(s)=log(1+s)` gives the standard projective Fubini–Study ball volume `[R^2/(1+R^2)]^n` and total volume one. In our case
`
sU_a'(s)=a+(1-a)\frac{s}{1+s};
\qquad \lim_{s\downarrow0}sU_a'(s)=a,\quad
\lim_{s\to\infty}sU_a'(s)=1.
`
The non-pluripolar product charges no mass at `p` and agrees with the smooth top wedge off `p`; the hyperplane `Z_0=0` is smooth for `u_a` and has zero top-dimensional mass. Consequently
`
\boxed{\int_{P^n} MA_{omega_FS}(u_a)=1-a^n.}
`
The closed-background singularity-type invariance explicitly used in §13.17, line 13 (Theorem 13.8.7) yields both volumes equal to this mass. In particular,
`
delta=\underline{vol}_{omega_FS}(0)=1,\qquad
D=\overline{vol}_{omega_FS}(0)-\overline{vol}_{omega_FS}(u_a)=a^n.
`
The conclusion of Proposition 13.18.3 at `p` and `pi=id` is therefore **an equality with constant one**:
`
\boxed{\nu(u_a,p)-\nu(0,p)=a=(D/delta)^{1/n}.}
`

**Why constant one is a valid uniform `C_id`.** Let `w in PSH(P^n,omega_FS)` and `x in P^n`. Choose a projective line `L` through `x` on which `w` is not identically `-infty` (take a second point where `w` is finite). Its restriction is quasi-subharmonic on `L\simeq P^1`; `omega_FS|_L+dd^c(w|_L)` is a positive measure of total mass exactly one by Stokes. Its atom at `x` dominates `nu(w,x)` by restriction of logarithmic upper growth, and therefore `nu(w,x)<=1`. Thus the uniform bound used in §13.18.3 can indeed take `C_id=1` on `P^n`. Our example attains equality for every `a`. Replacing the exponent by any `gamma>1/n` with a fixed constant would require `a<=C a^{n gamma}` as `a\downarrow0`, impossible.

**Suggested optional correction/addition (not applied):** an example directly after Proposition 13.18.3, explicitly recording `D=a^n` and optimality of both exponent and model constant. **Affected dependents:** quantitative comparison of ordinary models (§§13.18–13.23), Lelong-number control under modifications (§20), mass-deficit stability. **Boundary:** the radial MA calculation and uniform line bound are direct; identifying the *infimum and supremum over all equivalent singularities* invokes the already recorded internal closed-class invariance, not an independently re-proved theorem. No approximation/regularization programme is used.

## POME-GAUD-SURFACE-ADJOINT-SCALAR-001

**Severity:** low. **Status:** `verified conditional deduction`. **Neither §14.10.1 nor §14.12.3 is declared false.** The distinction `gamma_0` versus the auxiliary Gauduchon form `gamma` in §14.10.1 is essential.

Let `X` be a compact connected complex **surface** and `gamma_0` any smooth positive Hermitian form. For any smooth `u` for which the prescribed Gauduchon ansatz `Gamma_u>0`, the `n=2` form of the formula in §14.10, lines 11–15, is
`
\boxed{\eta_u=\gamma_0+dd^c u}
`
because `gamma^{n-2}=1`, so the auxiliary `gamma` disappears. In particular,
`dd^c eta_u=dd^c gamma_0`.

The same Stokes calculation gives the **exact affine volume law**
`
\begin{aligned}
\int_X\eta_u^2
 &=\int_X\gamma_0^2+
  2\int_X\gamma_0\wedge dd^c u+
  \int_X(dd^c u)^2\\
 &=\boxed{\int_X\gamma_0^2+
 2\int_Xu\,dd^c\gamma_0}.
\end{aligned}
`
Indeed `dd^c u` is exact and closed, so the top self-wedge integrates to zero, while integration by parts gives `int gamma_0 dd^c u=int u dd^c gamma_0`.

In dimension two, the adjoint equation of §14.12.3 is `dd^c(rho_u eta_u)=0` with `rho_u>0` and `int rho_u eta_u^2=1`. Therefore
`
\boxed{
\rho_u\text{ is constant}
\quad\Longleftrightarrow\quad dd^c\gamma_0=0.
}
`
For the forward implication, substitute a positive constant density and use `dd^c eta_u=dd^c gamma_0`. For the converse, if `gamma_0` is Gauduchon then `eta_u` is Gauduchon, so the constant `1/int_X eta_u^2` satisfies the adjoint and normalization equations; uniqueness is Proposition 14.12.1. The affine formula now gives `int_X eta_u^2=int_X gamma_0^2`, and hence
`
\boxed{\rho_u=\frac1{\int_X\gamma_0^2},\qquad
d\mu_u^\gamma=\frac{\eta_u^2}{\int_X\gamma_0^2}.}
`
This is valid for **all smooth admissible** `u`, not merely when `eta_u=gamma`. It is also independent of the auxiliary `gamma` in dimension two.

Finally, if an admissible pair `(u,b)` satisfies the printed equation
`eta_u^2=e^{F+b}gamma^2`, then **without** an extra assumption
`
e^b=\frac{\int_X\gamma_0^2+2\int_X u\,dd^c\gamma_0}
{\int_Xe^F\gamma^2}.
`
If in addition `gamma_0` is Gauduchon, this simplifies to the **explicit potential-independent scalar**
`
\boxed{b=\log\frac{\int_X\gamma_0^2}{\int_Xe^F\gamma^2}.}
`
A caution against omitting this hypothesis: take a flat complex two-torus with Kähler `omega` and a nonconstant positive smooth `h` such that `dd^c h\wedge omega\neq0`; put `gamma_0=h omega`, `gamma=omega`, `u=0`. Then `dd^c gamma_0\neq0`, so the invariant density `rho_0` is **not** constant, even though the auxiliary `gamma` is Gauduchon. This is a limitation of the strengthened statement, **not a counterexample to Pome**.

**Suggested optional addition (not applied):** a short corollary after Proposition 14.12.3, and a conditional scalar remark at Theorem 14.10.1. Preserve both source attributions and all permanent tags. **Affected dependents:** two-dimensional Gauduchon normalization, affine volume variation, invariant adjoint measures and uniqueness comparisons. **Boundary:** existence/uniqueness of the positive adjoint density and of the global nonlinear solution is used as already stated internally; neither the full elliptic Fredholm chain nor Theorem 14.10.1 is re-proved.

## Other inspected proof steps; non-certification

- §13.17.1 lines 28–49: the lower rooftop comparison and upper maximum proof use the correctly ordered contact and non-pluripolar mass limit. The pole-set argument relies on the **finite** total measure and absence of pluripolar mass; no false assertion was established.
- §13.17.2 lines 66–77: `w-v` is a quasi-continuous finite-a.e. obstacle off the polar set, which supplies the admissibility for the contact theorem (§15.8.6) after an arbitrary polar-set representative; this clarification is needed before invoking it. We did **not** reprove the general contact theorem.
- §13.18.1 lines 20–48: on its contact set, if `y_j=b^{-1}h_j+(1-b^{-1})v`, positivity gives `MA(y_j)>=b^{-n}MA(h_j)`; ordered contact against `w_j` gives `MA(y_j)<=MA(w_j)` on that set. This explains the coefficient `b^n` in line 39. The last tail limit uses the *non-pluripolar* measure of `w`, not the unrestricted classical top wedge. This is selected proof review, not an independent proof of all upstream contact/locality inputs.
- §14.12.1–3 lines 29–106: read the `n/(n-1)` derivative factor, first-order `D_gamma` terms and the adjoint characterization. The earlier sign audit `POME-GAUD-ADJOINT-CROSS-001` is **not relogged as new progress**; the new work here is the surface-specific affine law and precise constant-density criterion.

**Open/unchecked:** complete proofs of the cited global non-pluripolar contact and closed-class invariance, all nonlinear Fredholm/PDE existence estimates, other §§13.16–13.27 or 14.13–14.18, and the rest of the 747-section collection. No whole section is certified. No scripts, arithmetic grids, site build, Python/JS project tests, CI, automatic publication, formal proof checker, PR operation, merge, source/body/registry/permanent-tag/main edits or paid services were executed.

**User-excluded scope remains strictly `deferred-by-user`:** Demailly approximation/regularization and the dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss completion programme were not reopened, resolved or certified. Historical ledger notes retain their prior status.
