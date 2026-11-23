# Direct audit: local Monge–Ampère density, resolved logarithmic poles, and blowup pushforwards

**Date:** 2026-11-23 (Asia/Shanghai).
**Current main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Audit branch:** `review/mathematical-audit`.
**Scope:** direct full mathematical reading of §§15.21, 15.22, 15.23 of the integrated reading edition (not a certification of their transitive inputs). No Demailly approximation/regularization, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale atlas or positivity-loss programme was examined.

## Precise main files and anchors

1. `docs/sections/equations-with-prescribed-singularities--local-density-and-boundary-control/index.html`, blob `44fa705661cd5778904e1b9a6ea7299fb19e13ff`, physical lines 5–254. Theorem 15.21.2, permanent `9826C9FA5510`, lines 18–46; Lemma 15.21.8, `5E22269BEE55`, lines 96–142; Theorem 15.21.12, `5FC2412C22E9`, lines 153–237; Example 15.21.15, `41D1398D77FC`, lines 240–252.
2. `docs/sections/equations-with-prescribed-singularities--equations-with-resolved-logarithmic-poles/index.html`, blob `bec2abe4e9b361a37adbf668837da42726b6dcda`, physical lines 5–107. Theorem 15.22.2, permanent `3B5397268E44`, lines 21–50; Example 15.22.7, `0362BBF11A0B`, lines 64–80; Proposition 15.22.10, `D1ADF0EFDD30`, lines 87–106.
3. `docs/sections/equations-with-prescribed-singularities--minimal-singularities-on-blowups/index.html`, blob `884c20eb0ab2b613129a84232e9b6688f3aba993`, physical lines 5–123. Proposition 15.23.2, permanent `E42F32DA29D8`, lines 21–58; Theorem 15.23.5, `66FFA0C36433`, lines 61–97; displayed exponent 15.23.7, permanent `7E7FF8A6A54E`, lines 68–72; Theorem 15.23.10, permanent `37D35D78F0C6`, lines 103–123.

## POME-DISCONNECTEDNESS-AUDIT-CONVENTION-RETRACTION-001

**Classification:** high audit priority / **verified audit correction (withdrawal of false positive)**, **not a printed theorem error or a repair of a false theorem**.

The main reading edition's **global convention was overlooked in the initial version of this audit note**. Section 1.1 explicitly states that, unless otherwise stated, `X` denotes a **connected compact complex manifold**: `docs/sections/conventions/index.html`, blob `ef778e54d8d7413242387e95c52269b3c7d42cae`, physical line 123 (current section stable tag `DE921263`). This convention applies to Theorem 15.22.2 (`3B5397268E44`, lines 21–50), which does not override connectedness.

The originally recorded identifier **`POME-RESOLVED-POLES-DISCONNECTED-MASS-SCALAR-001` is WITHDRAWN as a source-error claim.** The elementary thought experiment using a disjoint union of two resolved-pole `P^2` models with density 1 on one component and 2 on the other is valid **only for an extension to disconnected manifolds**. It is **not** a counterexample to the actual printed theorem because the disjoint union violates §1.1. Thus **no new §15.22.2 error has been confirmed**.

The same convention also invalidates the preceding audit's three alleged connectedness counterexamples, unless a particular theorem explicitly overrides §1.1:

- `POME-SMOOTH-MA-DISCONNECTED-GLOBAL-SCALAR-001`, §14.2.1 (`F33DA8C9DF9F`, `docs/sections/smooth-monge-ampere-equations--scalar-bounds-and-uniqueness/index.html`, blob `3f96829e18befc845df40c6d4bca13c977ae9cea`, physical line 11): **withdrawn as a source-error claim**.
- `POME-SMOOTH-MA-DISCONNECTED-UNIQUENESS-001`, §14.2.4 (`366AA2E61158`, same blob, line 50): **withdrawn as a source-error claim**.
- `POME-SMOOTH-MA-DISCONNECTED-C0-ESTIMATE-001`, §14.3.5 (`EEF74F1DEBB8`, `docs/sections/smooth-monge-ampere-equations--the-potential-bound-from-weighted-integration/index.html`, blob `f774b702e65736ce8a23847dbb3409c6b31b0211`, line 108): **withdrawn as a source-error claim**.

The same global `X` convention supersedes **four additional alleged errors** from §§11.4, 11.26, and 11.27. No relevant theorem explicitly relaxes §1.1:

- `POME-GAUDUCHON-CONFORMAL-COMPACT-CONNECTED-001`, Theorem 11.4.2 (permanent `3978AEB15BD7`, `docs/sections/gauduchon-metrics-and-linear-mass--conformal-gauduchon-metrics/index.html`, blob `ecb4bf9e593dfb25f1644f0561d1aa65bf096b10`, line 20): withdrawn. Both a disconnected compact union and the noncompact ball fail §1.1.
- `POME-RCPOSITIVE-GLOBAL-SPREAD-DISCONNECTED-001`, Theorem 11.26.3 (permanent `AFF6DB5A7BE1`, `docs/sections/gauduchon-metrics-and-linear-mass--conformal-changes-and-directional-curvature-positivity/index.html`, blob `d54016b202422bde3bc5e2c6e493e4618918a7d7`, line 35): withdrawn, disconnected union outside hypotheses.
- `POME-RCPOSITIVE-FLAT-DETERMINANT-NONCOMPACT-001`, Proposition 11.26.7 (permanent `9EFFDFAE03AF`, same main blob, line 96): withdrawn, open unit ball outside compactness hypothesis.
- `POME-RICCI-FLAT-KAHLER-RCPOSITIVE-DISCONNECTED-001`, Theorem 11.27.4 (permanent `8C2D7F0F7808`, `docs/sections/gauduchon-metrics-and-linear-mass--ricci-flat-kahler-surfaces/index.html`, blob `119ac604fd60b412ecb7d51910cfcecc04b3b7cf`, physical line 129): withdrawn, K3 disjoint union flat torus outside hypotheses.

**Total reclassified in this checkpoint: eight earlier alleged theorem errors involving missing global connectedness/compactness, including the transient §15.22.2 allegation.** They are mathematically useful warnings when considering extensions beyond project hypotheses, but are **not errors in the integrated reading edition**. Findings unrelated to this global-scope mistake are unaffected.

This is a correction of **audit classification**, not independent certification of the deep connected-manifold proofs. In particular, neither smooth Hermitian Monge–Ampère existence nor its global estimates have been transitive-certified in this session. Retain historical reports for traceability, but treat their missing-connectedness error statuses as superseded.

## POME-BLOWUP-PUSHFORWARD-WEAK-LQ-ENDPOINT-001

**Classification:** low / **verified conditional deduction**, **not** an error in Theorems 15.23.5/15.23.10. This improves their open strong-`L^s` range to a Lorentz weak endpoint without asserting strong endpoint integrability or transitive correctness of the underlying MA existence theorem.

Let `pi:X=Bl_Z(Y)->Y` be a blowup along a smooth codimension-`r` center, `r>=2`, between compact complex manifolds, and let `mu` be an upstairs smooth strictly positive volume and `nu` a downstairs smooth strictly positive volume. For `1<p<infinity`, take any `f>=0` in `L^p(X,mu)` and set `pi_*(f mu)=F nu`. Then
\[
q=\frac{rp}{(r-1)p+1},\qquad
\boxed{\sup_{t>0}t\,\nu(\{F>t\})^{1/q}\le C_{pi,\mu,\nu,p}\,\|f\|_{L^p(\mu)}.}
\]
Equivalently `F in L^{q,infinity}(Y,nu)`; in particular `F in L^s` for every `s<q` as in (15.23.7). The same statement holds at `p=infinity` with `q=r/(r-1)`.

**Proof, including the endpoint.** On each bounded blowup chart `v=(z,zw)` transverse to `Z`, the holomorphic Jacobian is `z^{r-1}`. A finite chart cover with one normal coordinate of maximal modulus gives, for `rho(y)=dist(y,Z)`,
\[
W(y):=\frac{d(\pi_*\mu)}{d\nu}(y)\asymp \rho(y)^{-2(r-1)}
\]
near `Z`, with positive bounded factors outside. Tubular volume satisfies `nu\{rho<epsilon\}=O(epsilon^{2r})`, hence
\[
\nu\{W>t\}\le C t^{-r/(r-1)}.
\]
Integrating the distribution function (split at `t=(C/\nu(A))^{(r-1)/r}`) proves for every measurable `A subset Y`
\[
\pi_*\mu(A)=\int_A W\,d\nu\le C\,\nu(A)^{1/r}.
\]
Put `A_t={F>t}` and use Hölder upstairs:
\[
t\nu(A_t)\le\int_{\pi^{-1}(A_t)}f\,d\mu
\le\|f\|_p\bigl(\pi_*\mu(A_t)\bigr)^{1-1/p}
\le C\|f\|_p\,\nu(A_t)^{(1-1/p)/r}.
\]
Since `1-(1-1/p)/r=1/q`, rearrangement proves the claimed weak endpoint with the stated norm. There is no illicit exchange of weak limits, and no use of approximation of singular plurisubharmonic functions.

**The endpoint is genuinely only weak in general.** For a point center (or on a fixed product coordinate patch along `Z`), let `t=|s_E|` be a smooth local defining norm of the exceptional divisor and take
\[
 f(t)\asymp t^{-2/p}\bigl(\log(e/t)\bigr)^{-\gamma},
 \quad \frac1p<\gamma\le\frac1q,
\]
with cutoff in a small chart and zero outside. Upstairs smooth volume has normal factor `t\,dt`, so `f in L^p` because `gamma p>1`. Downstairs the density on a conical neighborhood is
\[
 F(y)\asymp \rho(y)^{-2(r-1+1/p)}\bigl(\log(e/\rho(y))\bigr)^{-\gamma}.
\]
Since `q(r-1+1/p)=r`, `int F^q d\nu` diverges by the radial integral `int_0 t^{-1}(log(e/t))^{-gamma q}dt`. For any `q'>q`, the same power model rules out a universal weak-`L^{q'}` estimate. If `p=infinity`, take `f=1` near `E` to obtain `F\asymp rho^{-2(r-1)}`, weak `L^{r/(r-1)}` but not strong `L^{r/(r-1)}`.

**Finite towers.** Given successive blowups of smooth centers with codimensions `r_j`, choose smooth positive reference volumes at each stage. Repeatedly applying the one-step measurable-set estimate gives
\[
(\pi_*\mu_m)(A)\le C\nu_0(A)^{1/R},\qquad R=\prod_jr_j.
\]
The same Hölder argument yields `pi_*(f mu_m)/nu_0 in L^{q_R,infinity}` with `q_R=Rp/((R-1)p+1)`, precisely the exponent in (15.23.11). No claim that this bound is optimal for every fixed tower.

**Suggested non-production addition:** an optional remark after (15.23.8) and (15.23.11) recording the weak endpoint and the absence of a strong endpoint. This result concerns measure pushforwards, not proof completion of the excluded Demailly regularization programme.

## Other directly checked steps and limitations

- In §15.21, checked the logarithmic singularity `b^{-1} in L^2` via weighted AM–GM with `4A=1/4<2`, the determinant `det(P_{j bar k})=ba_{z bar z}+|w|^2(bb_{z bar z}-|b_z|^2)=1` off the polar set, and gluing positivity from convex regularized maxima. The discontinuous constant-density example is not contradicted by the local smooth boundary-trace theorem: those traces fail the required smoothness.
- In §15.22, checked the `g=(f o pi)J` change of variables and the mass-defect identity `int h^n-int beta^n=sum_j c_j sum_i int_{D_j}H^i beta^{n-1-i}` under the stated `dd^c(h^k)=0` power hypotheses. No new normalizing or intersection-sign error confirmed for the connected case.
- In §15.23, checked that the threshold comes from `(r-1)(s-1)p/(p-s)<1`; the coefficient of `[E]` is fixed by exceptional-fiber degree, and tower exponents compose through `1-1/s=(1-1/p)/r`. The proofs of deep global existence/uniqueness and of the extended MA measure remain conditional upon the actual internal citations (not independently certified).
- **Not reviewed or certified:** transitive proofs of §§14.19.2, 15.5.1, 13.14.3, 5.24.7, 5.27.1, 11.1.7, and the full sheaf/current support theorems. None is declared defective solely because it is cited.
- **Deferred by user, not resolved or certified:** all excluded Demailly approximation/regularization and associated dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programmes. No work performed on them. No tests, builds, Actions CI, website publication, main/registry/source/permanent-tag edits, new PR or merge.

**Session accounting:** 3 entire current integrated mathematical sections directly read; 0 new confirmed printed-statement errors; 1 verified retraction of the erroneous connectedness diagnosis (also correcting three prior §14.2–14.3 diagnoses); 1 new sharp weak-endpoint conditional deduction (single blowup plus a tower corollary); 0 new complete transitive proof-chain certificates. Historical first-visit status remains unreconciled.
