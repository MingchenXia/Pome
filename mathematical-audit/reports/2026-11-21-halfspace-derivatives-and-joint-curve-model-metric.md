# Whole-section audit: half-space positive harmonic representation and curve-model metrics

**Date:** 2026-11-21. **Audited `main` commit:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Audit-only branch:** `review/mathematical-audit`.

## Scope and stable anchors

All actual mathematical text of these integrated *reading-edition* pages was read, including statement, proofs and inline consequences, not merely source headings:

| Current section | Main file and immutable blob | Mathematical physical lines | Statement source and permanent tags |
|---|---|---|---|
| §3.2 Kelvin transforms and half-space potentials | `docs/sections/kelvin-transforms-and-half-space-potentials/index.html`, blob `f2615a5393af724c3996978212162f94911ff9d9` | 7–185 | Theorem 3.2.2 `classical-potential-theory:B1AA5815` / `97BA27062B9F`; Theorem 3.2.6 `classical-potential-theory:1C8A330A` / `6BC86EEF03A9`; Theorem 3.2.12 `classical-potential-theory:BB6DAC3F` / `9ADD2DF19642` |
| §13.29 Background changes on curves | `docs/sections/volumes-under-bounded-mass--background-changes-on-curves/index.html`, blob `94ff265434461fd6baee6532decdff369da3e177` | 7–181 | Proposition 13.29.1 `non-kahler-pluripotential-theory:405CAA19` / `C9C98321BEFC`; Theorem 13.29.3 `non-kahler-pluripotential-theory:104CDD56` / `151BAA2FA1AB`; Corollary 13.29.7 `non-kahler-pluripotential-theory:DF1968BC` / `21F64887A53E` |
| §13.30 A complete space over varying curve backgrounds | `docs/sections/volumes-under-bounded-mass--a-complete-space-over-varying-curve-backgrounds/index.html`, blob `506708195b4fbeb7c1c0ac6ebea922983a764a6b` | 7–119 | Theorem 13.30.3 `non-kahler-pluripotential-theory:D0548646` / `C5551396F93B`; Corollary 13.30.5 `non-kahler-pluripotential-theory:FF7BDC58` / `8918C681057E` |

Selected prerequisite *statements/proof passages only*, not whole-section re-audits: §13.28.1 (lines 20–39), §13.28.4 (64–82), §13.28.7 (91–106), §13.28.23 (350–370), same main, `docs/sections/volumes-under-bounded-mass--model-potentials-on-curves/index.html`. The half-space derivative argument uses the integrated §3.2.6 representation; other §13.29–30 transport statements rely on §§5.27, 5.29, 13.22–13.28, 16, 18 and 20.3, whose full chains were not re-certified.

## Finding POME-HALFSPACE-POISSON-SHARP-DERIVATIVE-001

**Status:** verified conditional deduction. **Severity:** low. **Not a false printed theorem or a certified replacement proof.** **Anchor:** Theorem 3.2.6 and its converse, §3.2 lines 65–132, especially (3.2.7)–(3.2.8), 3.2.5 and the derivative estimates in lines 125–131.

**Claim.** For any nonnegative harmonic function `h` on the upper half-space `H = R^{d-1} × (0,∞)`, `d ≥ 2`, let `c ≥ 0` be the coefficient of `t` in the integrated positive half-space representation:
\[
h(x',t)=ct+\frac{2}{s_{d-1}}\int_{\mathbb R^{d-1}}
\frac{t}{(|x'-z|^2+t^2)^{d/2}}\,d\nu(z),
\quad
\int (1+|z|^2)^{-d/2}\,d\nu(z)<\infty.
\]
Then, pointwise throughout `H`,
\[
\boxed{\ |\nabla_{x'}h(x',t)|\le \frac{d}{2t}\bigl(h(x',t)-ct\bigr),\qquad
\frac{1-d}{t}h(x',t)+dc\le\partial_t h(x',t)\le\frac{h(x',t)}t.\ }
\]
Moreover the coefficient is intrinsically recovered by
\[
\boxed{c=\inf_{(x',t)\in H}\frac{h(x',t)}t
=\lim_{t\to\infty}\frac{h(0,t)}t.}
\]
The horizontal constant `d/2` and the vertical lower coefficient `1-d` are pointwise optimal among such functions; the vertical upper inequality is attained by `h=ct`.

**Proof.** Denote the Poisson kernel in (3.2.5) by `P`, put `r=|x'-z|`, and use the uniformly dominated differentiation already justified in the *converse* proof of §3.2.6 (main lines 125–131):
\[
\nabla_{x'}P=-dP\,\frac{x'-z}{r^2+t^2},
\qquad
\partial_tP=P\left(\frac1t-\frac{dt}{r^2+t^2}\right).
\]
Since `r/(r²+t²) ≤ 1/(2t)` (equality at `r=t`) and
`(1-d)/t ≤ 1/t-dt/(r²+t²) ≤ 1/t`, integrate the first inequality after taking the Euclidean norm and the other two against the *positive* measure `ν`; add the derivatives of `ct`. This proves all inequalities with the displayed exact `c`-dependence.

The representation makes `h/t≥c`. Along `(0,t)`,
\[
\frac{h(0,t)}t-c=\frac2{s_{d-1}}\int_{\mathbb R^{d-1}}(|z|^2+t^2)^{-d/2}\,d\nu(z).
\]
For `t≥1`, the integrand is dominated by `(1+|z|²)^{-d/2}`, integrable by (3.2.8), and tends pointwise to zero. Dominated convergence gives the limit and hence the infimum formula. For `ν=δ_z`, `c=0`, and `|x'-z|=t`, equality holds in the horizontal pointwise gradient estimate; at `x'=z`, equality holds in the vertical lower estimate. For `ν=0` and `c>0`, the vertical upper estimate is an equality. There are no hidden finite-total-mass assumptions on `ν`.

**Dependencies/affected claims:** §3.2.6 is used, not independently re-established by this corollary. This bound is available for any subsequent half-space Harnack/normal-derivative estimate, but is *not* a repair to the printed theorem. Earlier §3.2 Martin one-point compactification and weak-* findings are not recounted.

## Finding POME-JOINT-CURVE-MODEL-NONMIDPOINT-001

**Status:** verified conditional deduction. **Severity:** low. **Not a false printed theorem.** Theorem 13.30.3 explicitly asserts *completeness*, not geodesicity. **Anchor:** §13.30 formula (13.30.1), lines 10–23, (13.30.2), lines 26–39, Theorem 13.30.3 lines 43–85. §13.29.1 supplies the zero-polar model classification; the zero background case is explicitly discussed at §13.29 lines 34–37.

**Claim.** The complete metric space `(𝓜(Y),D)` of §13.30 is in general **not a geodesic metric space**, although every fixed-background fiber is geodesic when identified with its polar measures (cf. §13.28.7). It already has a pair of smooth zero-polar models with no metric midpoint.

**Proof.** Use the standard `C^k` norms defined in §13.30, each controlling the zeroth-order norm. Let `η` be the fixed positive area-one form; choose `M` large enough that `||Mη||_{C^k}≥2` for all `k≥0`. Such `M` exists because the norms include the `C^0` term. The two admissible model pairs
\[
x=(0,0),\qquad y=(M\eta,0)
\]
are normalized smooth models with polar measures zero. The truncated background metric satisfies
\[
D(x,y)=b(0,M\eta)=\sum_{k\ge0}2^{-k-1}=1.
\]
Consider any candidate `z=(σ,p)` with polar measure `μ≥0`. If `σ=0` or `σ=Mη`, one of its distances to `x,y` is at least one, excluding a midpoint. Otherwise, for every `k`,
\[
a_k=\|\sigma\|_{C^k}>0,\quad
b_k=\|M\eta-\sigma\|_{C^k}>0,\quad
a_k+b_k\ge\|M\eta\|_{C^k}\ge2.
\]
Consequently `min(1,a_k)+min(1,b_k)>1` for every `k`, and
\[
D(x,z)+D(z,y)
\ge b(0,\sigma)+b(\sigma,M\eta)>1=D(x,y).
\]
Thus *no* interior point satisfies equality in the triangle inequality, a fortiori no midpoint has both distances equal to `1/2`. No regularization or other deep analytic input is used: the obstruction comes entirely from truncating every `C^k` seminorm. The theorem's completeness claim is compatible with this observation and must be preserved. Do not conflate joint-background geometry with the genuinely geodesic fixed-background spaces.

**Dependencies/affected claims:** only §13.30's definitions and the existence of the two smooth models in backgrounds of nonnegative area. The result warns against transferring the fiberwise geodesic conclusion of §13.28.7 to the full disjoint union. It requires no change to a statement or canonical tag.

## Direct review of surrounding proofs

- **§3.2:** checked Kelvin inversion and involution, Laplacian powers and cancellation (§3.2.2, lines 17–49), ball Poisson limiting boundary measures, change-of-variables normalization and atom at infinity (§3.2.6, lines 65–132), and half-space Poisson normalization, non-tangential/unrestricted continuity-point boundary limit and linear-growth term (§3.2.12, lines 140–181). No newly confirmed printed error. The ball Poisson formula and measure-selection inputs are taken as previously stated; their complete upstream proofs were not re-certified.
- **§13.29:** directly checked gauge transport of ordinary and ideal model envelopes (lines 23–77), total-variation mass and distance formula, area-ratio similarity and composition (83–115), gauge representation for scaled models (119–138), and uniform family stability (143–181), including zero-area behavior. No newly confirmed printed error. Its Green-kernel, polar-measure classification and capacity-sublevel inputs remain conditional on their earlier proof chains.
- **§13.30:** directly checked the complete `C^∞` background metric (10–23), identification with a closed set of positive polar measures, positivity/polar support under total-variation limits (43–66), unique nearest atomic projection and ideal-model closure (68–76), capacity convergence including the zero-area limit (78–85), and gauge/scaling transport (96–119). No newly confirmed printed error. The joint-space non-midpoint model is a new *qualifying geometric consequence*, not a counterexample to the stated theorem.

## Outcome and outstanding items

**Precise new direct scope:** +3 whole current mathematical sections (§§3.2, 13.29, 13.30), +1 selected upstream §13.28, +2 verified conditional deductions, +0 newly certified complete transitive proof chains. These are not assertions of first-ever visits: earlier §3.2 and §§13.28–13.30 partial discussions were retained. All existing confirmed errors and open gaps elsewhere keep their statuses.

No source, body, registry, permanent tag, published document, `main`, website, GitHub Actions or CI changes. No build or software tests run. Demailly approximation/regularization and the dedicated Bergman, L², Ohsawa–Takegoshi, multiscale and positivity-loss programme remain **deferred-by-user, not resolved/certified**. This report is an audit-only mathematical record.
