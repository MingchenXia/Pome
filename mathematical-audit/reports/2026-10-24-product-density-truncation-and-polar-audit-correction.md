# Product density cutoffs: exact logarithmic scalar rate; withdrawal of a polar-set audit false positive

**Run date:** 2026-10-24 (Asia/Shanghai).
**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Original audit head:** `442f4d9c2be5e37a9d79facc203c7257c86769f5` (existing branch preserved).
Fresh required reads: main `AGENTS.md`, `documentation/proof-expansions.md`, `docs/chapters/index.html` (25 chapters / 747 ToC entries, inventory only); audit branch root `README.md`, `mathematical-audit/README.md`, `LATEST.md`, `SECTION_MATRIX.md`, `LEDGER.md`. Only the proof fragments stated below were reviewed, not full chapters.

## POME-PRODUCT-TRUNC-SCALAR-LOGRATE-001

**Status:** verified conditional deduction; **severity:** low; an optional quantitative strengthening, not an erroneous theorem.

**Main integrated anchors:** `docs/sections/equations-with-prescribed-singularities--exact-equations-on-products-with-zero-lower-mass/index.html`, blob `650b84dd3d354e2da7c27f66f8670c0c882748f2`: Lemma **15.30.1** source `non-kahler-pluripotential-theory:4A877CC1`, permanent tag `B30B4EF45772`, physical HTML lines 28–69 (radial formulas at 49–64); Lemma **15.30.2** source `non-kahler-pluripotential-theory:7C7DFBFB`, tag `40B884870886`, lines 72–97; Theorem **15.30.3** source `non-kahler-pluripotential-theory:F4CAE5F4`, tag `B36BAA6B4AA0`, lines 99–149, particularly the normalization-scalar sandwich at 109–122. Conditional order/homogeneity input §15.27.1, source `non-kahler-pluripotential-theory:F84443FE`, tag `CE5CA1071A3C`, `docs/sections/equations-with-prescribed-singularities--lower-mass-and-solvability-for-all-measures/index.html`, blob `fc7d4f24f72d9b6ec898eedc961b789e65ef3e25`, lines 25–47.

**Hypotheses:** precisely the product model of §15.30: compact connected Hermitian `(X_0,h_0)`, complex dimension `m>=1` and, for the full theorem, `v_-(h_0)=0`; `Y=P^k`, `k>=1`, normalized Fubini–Study `κ` of mass one; `H=h_0+κ` on `X=X_0×Y`. Write `V_0=∫h_0^m>0`, `C=binom(m+k,m)`, `c_0=CV_0`, choose *any* smooth positive probability `dV`, and set `R=(V_0^{-1}h_0^m∧κ^k)/dV`, with `0<a<=R<=A`. Fix `0<α<1`, take `ψ=log(Σ_{i=1}^k|z_i|²/Σ_{i=0}^k|z_i|²)`, `u_α=1-(1-ψ)^α`, `MA^ext_κ(u_α)=q_α κ^k`, `f=Rq_α`, and `β=k(1-α)>0`.

Define `M_t=∫_Y min(q_α,t)κ^k`. Then
\[
\boxed{\lim_{t\to\infty}(\log t)^\beta(1-M_t)=\alpha^k k^\beta.}
\]
For the **original truncated densities** `f_j=min(f,j)`, not merely the factorized cutoffs,
\[
\boxed{\lim_{j\to\infty}(\log j)^\beta\left(c_H(f_j)-c_0\right)
=c_0\alpha^k k^\beta.}
\]
In particular the normalization scalar converges from above, and the leading term is independent of `dV` and the smooth factor `R`, although finite-cutoff values may depend on them. The previously recorded `POME-RADIAL-MOMENT-SPECTRUM-001` is an **energy-moment** statement, not this density-cutoff scalar asymptotic; it is neither repeated nor replaced.

**Proof.** Set `r=Σ_{i=1}^k |z_i|²` on the affine chart centered at `o=[1:0:...:0]`, and `s(r)=1-log(r/(1+r))`. The printed radial flux is
\[
Q(r)=\frac{r+\alpha s(r)^{\alpha-1}}{1+r},\qquad
Q'(r)=\frac{1-\alpha s^{\alpha-1}+\alpha(1-\alpha)r^{-1}s^{\alpha-2}}{(1+r)^2}.
\]
The density formula `q=(1+r)^{k+1}(Q/r)^{k-1}Q'` simplifies **exactly** to
\[
q_\alpha(r)=\left(1+\frac{\alpha s^{\alpha-1}}r\right)^{k-1}
\left(1-\alpha s^{\alpha-1}+\frac{\alpha(1-\alpha)}r s^{\alpha-2}\right).
\]
Thus, with `β=k(1-α)`, as `r↓0`,
\[
Q(r)\sim \alpha s^{\alpha-1},\qquad
q_\alpha(r)\sim\alpha^k(1-\alpha)r^{-k}s^{-1-\beta}.
\tag{1}
\]
Since `s∼log(1/r)` and `r s^M→0` for every fixed `M`, logarithmic differentiation of the exact expression gives `r(d/dr)\log q_\alpha=-k+O(1/s)+o(1)`. Therefore `q_\alpha` is strictly decreasing in the radial variable for all sufficiently small `r`. Outside that neighborhood it is smooth and bounded. For large `t`, its superlevel set is a radial ball `r<r_t`, where `q_\alpha(r_t)=t` and `r_t↓0`. Equation (1) implies
\[
\log t=k\log(1/r_t)-(1+\beta)\log s(r_t)
+\log(\alpha^k(1-\alpha))+o(1),
\quad\frac{s(r_t)}{\log t}\longrightarrow\frac1k.
\tag{2}
\]
The printed radial flux and Fubini–Study radial volume give *exactly*
\[
\int_{r<r_t}q_\alpha\,\kappa^k=Q(r_t)^k,\qquad
\int_{r<r_t}\kappa^k=\left(\frac{r_t}{1+r_t}\right)^k.
\]
Consequently,
\[
1-M_t=\int(q_\alpha-t)_+\,\kappa^k
=Q(r_t)^k-t\left(\frac{r_t}{1+r_t}\right)^k.
\tag{3}
\]
The first term in (3) is asymptotic to `α^k s(r_t)^(-β)`; the second to `α^k(1-α)s(r_t)^(-1-β)`, a lower-order term. Equation (2) proves the first boxed limit.

For `f=Rq_\alpha`, §15.30.3's **actual original-density** comparison is
\[
\frac{c_0}{M_{j/a}}\ \leq\ c_H(\min(f,j))\
\leq\ \frac{c_0}{M_{j/A}}.
\]
As `log(j/a)/log j→1` and `log(j/A)/log j→1`, the first boxed limit makes both outside terms minus `c_0` asymptotic to `c_0 α^k k^β(\log j)^{-β}`. Squeezing proves the second limit.

This is **conditional on** the printed radial Monge–Ampère flux and scalar order argument, whose displayed algebra and sign/normalization directions were checked. It is **not** an independent certification of §§14.2, 14.19, 15.2 or all of §15.30. Proposed change is an optional corollary after 15.30.3, via a separate reviewable mathematics patch, preserving all source labels and tags.

## POME-AUDIT-POLAR-HYP-WITHDRAWAL-001

**Status:** verified repair of **audit classification**; **severity:** medium; **not a source/body repair**.

The historical entry `POME-EQUIL-POLAR-HYP-001` wrongly marked §16.35 Proposition 16.35.3, permanent tag `6E38A7B6271A`, as a confirmed error for allegedly assuming only compact `K`, making the global equilibrium measure `μ_K` undefined for `K={0}`. We fetched **by SHA** the very old HTML blob cited in that finding, `bec49d8c886021153d87ff8c989873430bd6f69f`, and separately the **current main** blob `568257f81e9f31491e0cdde36ba8efb357423cd7` for `docs/sections/polynomial-families-and-equilibrium-null-obstacles/index.html`. **Both already state verbatim** `Let K be compact and non-pluripolar.` in Proposition 16.35.3, source `klimek-pluripotential-theory:3F26C3AC`, current HTML lines 50–54; proof lines 59–64. The relevant §16.34 Proposition 16.34.2, tag `01D4425BEF42`, current `docs/sections/logarithmic-total-mass-and-bounded-obstacle-support/index.html` blob `47387388cb62e2b99cf6f78370c914aa6f75909d`, line 48, requires bounded *non-pluripolar* `E`, fulfilled by compact non-pluripolar `K`.

Therefore `K={0}` violates an **existing explicit hypothesis**. **Withdraw the former confirmed-error classification of `POME-EQUIL-POLAR-HYP-001` as a false positive, preserving the old text for provenance.** No mathematical theorem was repaired or edited on main in this run, and no blanket validation of the contact comparison follows. §16.35.4 tag `1C591D5634BA` should not be counted as dependent on that nonexistent defect.

## Actual coverage, duplicates, and exclusions

First selected proof-level inspection of **§15.30 Lemmas 1–2 and Theorem 3** (radial density, flux, scalar and product expansion); selected **§15.30.6** only the density/truncation steps (lines 185–238). Context only: §15.27.1 scalar order, §15.31.3 curve Green-potential curvature/full-mass lines 27–53, §16.34.2 stated hypotheses, §16.35.3 source-blob comparison and proof assumptions. Entire sections remain uncertified. The already registered §16.36 endpoint `POME-CUBE-LORENTZ-ENDPOINT-001` was recognized and **not** relogged. The ToC's 747 rows are inventory, not 747 verified sections.

The independent `checks/check_product_density_scalar_log_rate.py` ran **27 numerical** large-log-threshold diagnostics (k=1,2,3; α=1/3,1/2,2/3; log thresholds 256,512,1024), all passed its stated checks. These are *not* proofs. No complete Pome build, tests, formalization, CI, website publication, new PR/issue, merge, source/body/registry/tag/main edit, or paid service.

**Strict scope:** all Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale atlas and positivity-loss proof-completion programme remains **deferred-by-user**; nothing in it was reopened, resolved or certified. All unrelated historical issues retain their status unless expressly superseded above.
