# Sharp Darvas-energy contraction and the abstract rooftop completeness criterion

**Date:** 2026-11-03 (Asia/Shanghai). **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Findings:** `POME-GEO-D1-ENERGY-SHARP-CONTRACTION-001` and `POME-ROOF-MONOTONE-COMPLETENESS-INDEPENDENCE-001`, each **low / verified conditional deduction**. Neither is a false theorem or a claimed repair.

## Integrated reading-edition anchors

Main file: `docs/sections/geodesic-rays-in-the-space-of-potentials/index.html`, blob `52bf9e459a0dfb1c8afe79556db037450be06bb3`.

- §17.10.40 (metric setup, lines 691–700): compact connected Kähler `X`, smooth closed big `theta`, model `phi` of **positive** non-pluripolar mass.
- Definition 17.10.41, source `sgpt:7B786AE5`, permanent `08EFAEA550B1`, lines 701–708: `d_1(u,v)=E(u)+E(v)-2E(u wedge v)`; equation 17.10.42, source `sgpt:BF10DF27`, permanent `D8C8C0BB6585`, lines 709–715: comparable endpoints.
- Proposition 17.10.43, source `sgpt:BB01FE5E`, permanent `61DD221912DE`, lines 717–746: nonexpansivity of rooftop in each argument.
- Definitions 17.10.55–56, source `sgpt:B84B5C1A` / `sgpt:5D3E3518`, permanent `3FB52FA474A3` / `602E107F6064`, lines 980–1020: associative, commutative, idempotent meet with nonexpansivity.
- Lemma 17.10.58, source `sgpt:3D07C59A`, permanent `DB740351ED65`, lines 1021–1042: jointly Lipschitz meet.
- Proposition 17.10.59, source `sgpt:61292BA6`, permanent `8F175566EB00`, lines 1043–1142: both monotone Cauchy types characterize completeness.
- Theorem 17.10.60, source `sgpt:097B6926`, permanent `C89C58354E49`, lines 1144–1201: completeness for relative finite-energy potentials. Its **monotone** analytic passage still invokes earlier §16.5.20/.37/.45/.53; this review does not certify those inputs.
- Lemma 17.10.62, source `sgpt:BE442E57`, permanent `ACEE2B318CA0`, lines 1203–1293: d1 convergence with monotone sandwich subsequences.
- Theorem 17.10.63, source `sgpt:C6AC67A2`, permanent `D84A6072F1A6`, lines 1295–1318: continuity of relative energy.

## 1. A sharp strengthening of energy continuity

Let `E=E_theta^phi`, `P=u wedge v` be the relative rooftop, and `u,v in E^1(X,theta;phi)`. By the definition of a rooftop, `P <= u,v`. **Only monotonicity of energy** is needed: `A=E(u)-E(P)>=0` and `B=E(v)-E(P)>=0`. By the **printed** definition of `d_1`,

```text
d_1(u,v) = A+B,
E(u)-E(v) = A-B.
```

Consequently the sharpened, quantitative form of Theorem 17.10.63 is

\[
\boxed{|E_\theta^\phi(u)-E_\theta^\phi(v)|\le d_1(u,v).}
\]

The coefficient **1 is optimal in every positive-mass model class**. Let `M=\int_X \langle\theta_\phi^n\rangle>0` (fixed by the standing §17.10.40 hypothesis) and choose `u=phi`, `v=phi+c` for a nonzero real constant `c`. Translation by a constant preserves the same full relative mass and, by the defining mixed-energy formula in §16.5.10, `E(phi+c)-E(phi)=cM`. These two endpoints are pointwise comparable. Equation 17.10.42 therefore gives

\[
d_1(\phi,\phi+c)=M|c|=|E(\phi+c)-E(\phi)|.
\]

This derives Lipschitz continuity of energy **directly** without the monotone sandwich of Lemma 17.10.62. It does **not** replace that lemma, which supplies stronger ordering/pointwise conclusions elsewhere. It relies only on the printed monotonicity, rooftop definition and translation identity; the full upstream mixed-mass theory is not certified here.

## 2. Independent hypotheses in the abstract completeness criterion

For a metric space `(E,d)` with an associative, commutative, idempotent operation `wedge` satisfying `d(x wedge z,y wedge z)<=d(x,y)`, the proof of Proposition 17.10.59 uses **both** increasing and decreasing Cauchy convergence; neither may be dropped.

Take the usual metric and `x wedge y=min(x,y)` on an interval. This is a valid rooftop metric because `min(.,z)` is 1-Lipschitz, and the induced partial order is the ordinary order.

- `E=[0,1)`: every **decreasing** Cauchy sequence has its limit in `[0,1)`, but the increasing Cauchy sequence `1-1/j` (`j>=1`) has no limit in `E`. Thus decreasing convergence alone does not imply completeness.
- `E=(0,1]`: every **increasing** Cauchy sequence has its limit in `(0,1]`, but the decreasing Cauchy sequence `1/j` does not. Thus increasing convergence alone does not imply completeness.

The complete proof of Proposition 17.10.59 was independently checked at the **abstract metric** level. Given a Cauchy sequence, pass to a subsequence `x_k` with `d(x_k,x_{k+1})<=2^{-k}`, and set `y_j^k=\bigwedge_{r=k}^{k+j} x_r`. Since `y_j^k=y_j^k wedge x_{k+j}`, nonexpansivity gives
\[
d(y_j^k,y_{j+1}^k)=d(y_j^k\wedge x_{k+j},y_j^k\wedge x_{k+j+1})
\le d(x_{k+j},x_{k+j+1})\le2^{-k-j}.
\]
Hence `y_j^k` converges by the *decreasing* Cauchy hypothesis, defining `y^k`. Joint continuity of the meet yields `y^k<=y^{k+1}`. The `y^k` sequence is Cauchy because
\[
d(y^k,y^{k+1})\le d(x_k,x_{k+1})\le2^{-k},
\]
using the finite comparison `x_k wedge z` versus `x_{k+1} wedge z`, `z=\bigwedge_{r=k+1}^{k+j+1}x_r`. It converges to `y` by the *increasing* Cauchy hypothesis. Finally induction using contraction gives
\[
d(x_k,y^k)\le\sum_{r=k}^\infty d(x_r,x_{r+1})\le 2^{1-k},
\qquad
d(y^k,y)\le 2^{1-k},
\]
hence the explicit **subsequence convergence estimate** `d(x_k,y)<=2^{2-k}`. Since the original sequence was Cauchy and a subsequence converges, the original sequence converges. No compactness, completion of a directed net, or interchange of two uncontrolled limits is used. This confirms the printed **abstract** proposition, not the transitive analytic content of Theorem 17.10.60.

## Classification, consequences and proposed optional edits

1. `POME-GEO-D1-ENERGY-SHARP-CONTRACTION-001`: **low / verified conditional deduction**, sharp energy 1-Lipschitz estimate; original Theorem 17.10.63 correct. **Proposed optional patch**: replace its long continuity argument with the two-line rooftop computation, or append as a quantitative corollary; preserve Theorem/Lemma 17.10.62 and permanent tags. **Direct dependent:** energy continuity and any energy-limit argument seeking explicit d1 rates; no new claim about weak/L1 or net convergence.
2. `POME-ROOF-MONOTONE-COMPLETENESS-INDEPENDENCE-001`: **low / verified conditional deduction**, both hypotheses of Proposition 17.10.59 shown logically independent by exact countermodels, and abstract proof checked with an explicit convergence estimate. The original proposition is true, not a mathematical error. **Proposed optional patch**: add a short remark with interval examples and `2^{2-k}` estimate; no correction to hypotheses or tags. **Direct dependents:** the abstract step of Theorem 17.10.60; its §16.5 analytic inputs remain conditional.

**Actual coverage:** first direct new check of §17.10.40–63 *metric/rooftop subsector*, specifically Definition 17.10.41; Proposition 17.10.43 as a stated prerequisite; Lemma 17.10.58; full *abstract* proof of Proposition 17.10.59; selected monotone arguments in Theorem 17.10.60; selected Lemma 17.10.62 and Theorem 17.10.63 conclusions. Earlier §17.10 endpoint and late radial-energy reviews are separate and unchanged. No entire §17.10 or analytic dependency chain certified; actual current table remains **25 chapters / 747 numbered sections / zero fully mathematically certified sections**. No project tests, builds, CI, formalization, website publication, source/body/registry/permanent-tag edits. All previous confirmed errors/proof gaps/external inputs unchanged. Explicitly excluded Demailly approximation/regularization, dedicated Bergman/weighted L2/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss programme remains **deferred-by-user**, untouched.
