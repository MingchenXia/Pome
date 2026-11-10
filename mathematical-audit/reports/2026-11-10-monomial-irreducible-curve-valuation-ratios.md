# Irreducible-curve valuation ratios for diagonal finite maps (§§6.35, 6.38, 6.46–6.47)

**Finding:** `POME-MONOMIAL-IRREDUCIBLE-CURVE-VALUATION-RATIOS-001`. **Date:** 2026-11-10. **Severity:** low. **Status:** verified conditional deduction (a new calculation under explicit internal hypotheses), **not** a false theorem and **not** a proof repair.

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

## Source anchors in the integrated reading edition

| Printed result | Integrated file and current main blob | Source label / permanent tag | Physical lines |
| --- | --- | --- | --- |
| Proposition 6.47.1, Corollary 6.47.2 | `docs/sections/lelong-densities-generalized-masses-and-multiplicity--monomial-maps-and-the-sharp-directional-comparison/index.html`; `bad5cd9bb63a90871462700f5c1f7080c597ee99` | `demailly-complex-geometry:F608EF8B` / `0A17C5BE0625`; `demailly-complex-geometry:9E33C486` / `240191846A51` | 7–31, 33–45 |
| Theorems 6.46.1–2 | `docs/sections/lelong-densities-generalized-masses-and-multiplicity--proper-direct-images-and-finite-map-upper-bounds/index.html`; `1f44c5feb546ecfe43ec1bc752d3fd0bff501613` | `demailly-complex-geometry:8BBE1973` / `86EB492BC979`; `demailly-complex-geometry:784313F4` / `751F9003E019` | 7–29, 33–64 |
| Proposition 6.35.1, proper weighted projection | `docs/sections/lelong-densities-generalized-masses-and-multiplicity--holomorphic-maps-and-weights/index.html`; `d815e0a11cf3aab85abcebd9d5a943ba72c1dedb` | `demailly-complex-geometry:2034468C` / `9BBFC6858DCC` | 7–24 |
| Theorem 6.38.3, ordinary analytic multiplicity | `docs/sections/lelong-densities-generalized-masses-and-multiplicity--analytic-multiplicity-and-ordinary-density/index.html`; `a74bd5c4cecc4d310f4b7b08af1b96bc8ff667e0` | `demailly-complex-geometry:8BE55493` / `673FC5FBB2C8` | 45–77 |
| Proposition 6.43.1, finite germ integer degree (dependency crosscheck only) | `docs/sections/lelong-densities-generalized-masses-and-multiplicity--finite-germs-and-their-actual-integer-degree/index.html`; `e2a86c5438c7770a8766f6bedf779e1879ead4c0` | `demailly-complex-geometry:F459CB6C` / `AD7655D0958A` | 7–33 |

The printed bounds are **correct in the regime checked**. This report distinguishes irreducible analytic curve currents from the *previously documented* `POME-MONOMIAL-MULTIPLICITY-INTERVAL-001`, which realizes every real ratio using **convex combinations of coordinate-plane currents**. No such linear combination is used here.

## Exact formula for an irreducible analytic curve

Let `n>=2`, `1<=s_1<=...<=s_n` be integers, and `F(z)=(z_1^{s_1},...,z_n^{s_n})`. Let `(C,0)\subset(C^n,0)` be a **reduced irreducible analytic curve germ**. Let `\phi:(\Delta,0)\to(C,0)` be its finite, generically one-to-one normalization parametrization. Put `a_j=ord_0(\phi_j)\in Z_{>=1}\cup\{+infty\}`, with `a_j=+infty` when `\phi_j\equiv0`. At least one order is finite. Then

\[
\boxed{\nu([C],0)=\min_j a_j,\qquad
\nu(F_*[C],0)=\min_j(s_j a_j).}
\tag{1}
\]

Here `s_j\cdot\infty=\infty`; the current is restricted to sufficiently small representatives for which all pushforwards are proper on their supports. For arbitrary real positive `\lambda=(\lambda_1,...,\lambda_n)`, let `\rho_\lambda=\max_j\lambda_j\log|z_j|^2`. Then

\[
\boxed{\nu([C],\rho_\lambda)=\min_j(\lambda_j a_j).}
\tag{2}
\]

Consequently the ordinary finite-map ratio for an irreducible curve is

\[
R_C(F)=\frac{\min_j(s_j a_j)}{\min_j a_j}\in[s_1,s_n]\cap\mathbb Q.
\tag{3}
\]

### Proof

1. **Normalization, support and multiplicity.** Take a sufficiently small disc about the source origin. Since `\phi^{-1}(0)=\{0\}` as a germ and `\phi` is finite, its restriction is proper onto a suitable local image. Generic degree one means `\phi_*[\Delta]=[C]`. For any nonconstant holomorphic map germ `h=(h_1,...,h_n):(\Delta,0)\to(\mathbb C^n,0)` with isolated zero, let `b=\min_j ord_0 h_j`. Writing `h_j(t)=t^{b_j}v_j(t)` for finite `b_j`, with at least one unit `v_j(0)\ne0` at `b_j=b`, yields
   \[
   \log\sum_j|h_j(t)|^2=b\log|t|^2+O(1).
   \]
   The bounded term is harmless for the **atom** of `dd^c` on the disc: with Pome's `dd^c=(i/2\pi)\partial\bar\partial`, `dd^c\log|t|^2=[0]`; the atomic coefficient is exactly `b`. Proposition 6.35.1 identifies that coefficient with the ordinary Lelong number of `h_*[\Delta]` at the image origin. Applying this to `h=\phi` proves the first identity in (1), agreeing with Theorem 6.38.3.

2. **Pushforward after the monomial map.** The composite `h=F\circ\phi` has order vector `(s_j a_j)_j`. It remains finite with the isolated zero. Functoriality of proper pushforward gives `F_*[C]=(F\circ\phi)_*[\Delta]`, **including any sheet multiplicity of the image**. The disc computation gives the second identity in (1), without assuming that `F|_C` is generically injective. Equivalently, if the composite factors through the normalization of `F(C)` with generic degree `e`, then each target coordinate order is `e` times its order on that normalization; the cycle `e[F(C)]` has Lelong number `\min_j(s_j a_j)`, independent of `e`.

3. **Directional weight.** Along `\phi`,
   \[
   \rho_\lambda(\phi(t))=\max_j\{\lambda_j a_j\log|t|^2+\lambda_j\log|v_j(t)|^2\}
   =(\min_j\lambda_j a_j)\log|t|^2+O(1).
   \]
   The coefficient of the disc atom and the proper weighted projection identity give (2). This uses the single isolated pole on the curve, not an interchange of general Bedford–Taylor limits. In particular, arbitrary `a_j=+\infty` coordinates contribute nothing to the minimum. Formula (3) follows because all finite `a_j,s_j` are positive integers. Its bounds follow directly from `s_1\min a_j\le\min(s_j a_j)\le s_n\min a_j`.

All steps after the stated finite normalization and the cited internal proper weighted projection are explicit one-variable calculations; no excluded approximation, Bergman, weighted L², Ohsawa–Takegoshi, multiscale atlas or positivity-loss construction is used. \(\square\)

## Exact irreducible-curve range in dimension two

For `n=2`, write `s=s_1<=t=s_2`, and suppose the two coordinate orders `a,b` are finite. From (3),

\[
R_C(F)=
\begin{cases}
s,&a\le b,\\
\min\{s\,a/b,\ t\},&a>b.
\end{cases}
\tag{4}
\]

Coordinates identically zero give the appropriate endpoint `s` or `t`. Every pair of coprime positive integers `(a,b)` occurs in the irreducible monomial curve parametrization `\phi(\tau)=(\tau^a,\tau^b)`. Hence for `s<t`, **the set of all ratios among irreducible reduced curve germs is a countable dense proper subset of `[s,t]`**: it consists exactly of the endpoints and values `s a/b` with rational `1<a/b<t/s`. It cannot be the entire real interval because each ratio in (3) is rational. For `s=t` it is the singleton `\{s\}`.

This is a genuine distinction from `POME-MONOMIAL-MULTIPLICITY-INTERVAL-001`: allowing arbitrary closed positive currents or even positive real combinations of two axes gives **the full real interval**, while restricting to individual irreducible analytic curve currents leaves only the stated countable dense set.

As transparent integer checks, for `F=(z_1^2,z_2^5)`, the primitive order pairs `(a,b)=(1,3),(3,2),(2,1),(3,1)` give respectively `R=2,3,4,5`. These are substitutions in the proved formula, **not software or formal verification**.

## Mathematical status and proposed action

- **Classification:** low / **verified conditional deduction**, with a complete conditional one-variable argument. Proposition 6.47.1, Corollary 6.47.2 and Theorems 6.46.1–2 are **not** refuted. No proposed source-body correction.
- **Upstream dependencies not recertified in this run:** existence and finite generic degree-one normalization of an arbitrary reduced irreducible analytic curve germ; the local integration current and functorial proper pushforward; Proposition 6.35.1's generalized Lelong projection. The formulas can alternatively be viewed as unconditional for a **given** primitive finite disc parametrization and the standard integration-current definition. This report does **not** certify the full transitive chain of §§6.35, 6.38 or 6.46–6.47.
- **Suggested addition:** an optional corollary after §6.47.2 recording (1)–(4) for `p=1`, especially the distinction between irreducible curves and positive mixtures; retain original historical attribution, source/permanent tags and stronger general-current inequalities.
- **Affected dependents:** any attempt to strengthen the §§6.46–6.47 inequalities when the current is assumed to be integration over an irreducible analytic curve; generic finite-map multiplicity estimates on parametrized branches.
- **Excluded scope:** Demailly approximation/regularization and its dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss proof programme remain **deferred-by-user** (not resolved or certified).

## Coverage integrity

Actual new direct work: §§6.47.1–2, 6.46.1–2 and 6.35.1's hypotheses checked in the integrated reading edition, §6.38.3 and §6.43.1 inspected as dependencies, and the **new irreducible-curve calculation** proved. These numbered sections were previously partially reviewed, so **0 first proof-level numbered-section visits, 0 full-section certifications**. Current real ToC baseline remains **25 chapters / 747 numbered sections**. No source tree, main branch, proof registry, tags, CI, build, site or automated publication was changed.