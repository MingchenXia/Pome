# 2026-11-13 — Sharp quantitative cohomologous-background gauge comparison for P-envelopes

**Finding:** `POME-PENVELOPE-GAUGE-SHARP-OSC-001`
**Classification:** low severity; **verified conditional deduction** (a sharp quantitative refinement). **No printed theorem is refuted.**
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Integrated reading edition:** `docs/sections/the-envelope-operators--p-envelopes--rooftop-operator-and-the-definition-of-the-p-envelope/index.html` (blob `97681f31628eb362950837daaadde67d10507a2f`, 806 physical lines).

## Exact integrated anchors and provenance

- Section 16.3 is headed “Rooftop operator and the definition of the P-envelope”; section permanent tag `1BFD41225C11`, source `sgpt:6215ED06` (physical line 5).
- Definition **16.3.4**, source `sgpt:15C6153F`, permanent tag `395DB7860949`, physical lines **79–85**, gives the normalized upper envelope of candidates `u <= 0, u \preceq phi` (equation 16.3.5, source `sgpt:E4924BB8`, permanent `7E001B03F24A`, lines **81–84**).
- Proposition **16.3.8**, source `sgpt:EBC14D0B`, permanent tag `EF5AC4B19C4D`, lines **108–131**: under `theta' = theta + dd^c g`, `phi' = phi - g`, the two P-envelopes have the same singularity type. Its proof uses a one-sided comparison after shifting `g` to be nonnegative. The theorem and this proof are correct.
- The order and bounded-difference convention used by the proof is recalled in §16.3 after Definition **16.7.1**, link permanent tag `3E4D57445698` (the relevant §16.3 pointer is at line **79**).

## The refined assertion

Let `X` be a connected compact Kähler manifold, `theta` any smooth closed real (1,1)-form and `phi in PSH(X,theta)`. Let `g in C^infty(X,R)`, `theta' = theta + dd^c g` and `phi' = phi-g`. Put `m=min_X g`, `M=max_X g`. Write
`P=P_theta[phi]` and `P'=P_{theta'}[phi']`, each normalized with the obstacle `0` as in (16.3.5). Then the following *extended-valued pointwise inequalities* hold on all of `X`:

\[
  P-g+m\;\le\;P'\;\le\;P-g+M.                 \tag{A}
\]

In particular, the two envelopes correspond modulo bounded functions with an **explicit, input-independent constant** `M-m=osc_X(g)`. On the locus where their values are finite, (A) says
\[
 m\le P'+g-P\le M.
\]
Consequently, after centering the smooth gauge by `c=(m+M)/2`, the discrepancy `P'+g-c-P` has absolute value at most `osc_X(g)/2` wherever the difference is defined. **Do not** present this last fact as an unqualified global L-infinity norm of two extended-valued potentials: both may equal negative infinity on a pluripolar set.

The pointwise interval (A), and the centered constant `osc_X(g)/2`, are sharp in general.

## Independent proof

The candidate family in the definition of `P` is nonempty: `phi-sup_X phi` is a candidate. Because `theta'+dd^c(phi-g)=theta+dd^c phi`, the shifted potential `phi'` is admissible for the transformed background.

For any candidate `u in PSH(X,theta)` with `u<=0` and `u\preceq phi`, set
\[
  T_m(u)=u-g+m.
\]
Then `theta'+dd^c T_m(u)=theta+dd^c u\ge0`. Since `m<=g` and `u<=0`, one has `T_m(u)<=0`; subtracting the same smooth `g` preserves the singularity preorder, so `T_m(u)\preceq phi-g`. Hence `T_m(u)` is an admissible candidate for `P'`. Taking the supremum, then upper-semicontinuous regularization (which commutes with addition of a smooth function), gives the first inequality in (A).

Conversely, for an admissible `v in PSH(X,theta')` defining `P'`, let
\[
  S_M(v)=v+g-M.
\]
Then `theta+dd^c S_M(v)=theta'+dd^c v\ge0`; `v<=0` and `g<=M` imply `S_M(v)<=0`; and `v\preceq phi-g` implies `S_M(v)\preceq phi`. Thus `S_M(v)` is a candidate for `P`. Supremizing and regularizing gives `P'+g-M<=P`, the second inequality in (A). The proof neither takes limits of non-pluripolar products nor invokes regularization or an external existence theorem.

## Exact sharpness model

Take **any** positive-dimensional compact Kähler manifold `(X,theta)` with `theta>0`. Pick a nonconstant real smooth `g` with sufficiently small `C^2` norm that `theta'=theta+dd^c g>0`; one can scale any nonconstant real smooth function. Set `phi=0`, hence `phi'=-g`.

Because `theta` is Kähler, the constant zero potential is admissible, and the envelope is bounded above by its normalizing obstacle `0`. Therefore `P_theta[0]=0`. Also `theta'` is Kähler, so `0` is `theta'`-psh. Since `phi'=-g` is bounded, `0\preceq-g`; thus `0` is an admissible candidate for `P_{theta'}[-g]`, and normalization forces `P_{theta'}[-g]=0`.

It follows that
\[
    P_{theta'}[-g]+g-P_theta[0]=g.
\]
The lower and upper endpoints `m` and `M` in (A) are **both attained**, respectively at minimum and maximum points of `g`. The optimally centered maximum discrepancy is exactly `(M-m)/2`, and no smaller universal centered constant is possible. This family obeys all original assumptions and demonstrates sharpness; it is **not a counterexample to Proposition 16.3.8**.

## Consequences, dependencies, and limitations

The printed equivalence of singularity types follows immediately from (A), and the sharper statement makes explicit how background changes act on normalized representatives, as opposed to currents or singularity classes. This matters when comparing canonical normalized representatives across smooth cohomologous gauges, including the `P`-preorder in §16.8. The construction does **not** claim equality of potentials, invariance of normalizations, any curvature/energy Lipschitz bound, or a global finite-valued difference on the common polar set.

**Internal inputs used:** the literal candidate-family definition (16.3.5), the bounded-error singularity preorder, and elementary stability of the usc envelope under addition of a smooth function. No mathematical dependency on Demailly approximation/regularization, dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale atlases, or positivity-loss proof completion. These remain **deferred-by-user**, not resolved or certified. No new unproved external input is asserted.

**Proposed correction:** No source correction is needed. Optionally add (A) as a separately reviewable quantitative remark following Proposition 16.3.8; do not edit production text or permanent tags as part of this audit.

**Coverage:** Direct proof reading of Definition 16.3.4, equation 16.3.5 and Proposition 16.3.8, with a new complete elementary two-sided comparison and sharpness example. Other §16.3 statements and upstream pluripotential foundations are **not** certified. Since §16.3 had already been sampled, **0 newly first-visited numbered sections / 0 whole-section certifications**. At the reviewed main, the existing ToC inventory is **25 chapters / 747 numbered sections**. Builds, software tests, CI, and publication were not run.
