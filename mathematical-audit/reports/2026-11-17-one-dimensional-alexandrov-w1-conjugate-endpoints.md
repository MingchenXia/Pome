# One-dimensional Alexandrov Monge–Ampère: exact transport and conjugate-endpoint criterion

**Audit date:** 2026-11-17. **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Finding:** `POME-TORIC-1D-W1-DUAL-ENDPOINT-001` (**low; verified conditional deduction**, not a false printed statement or a repair of an erroneous theorem).

## Exact integrated-text anchors and scope

- **Primary:** `docs/sections/convex-analysis-and-toric-potentials--the-real-monge-ampere-measure/index.html`, blob `7089aa41ae2422b1bd6b5094e46668cbc8ed37be` on reviewed main. Theorem 21.5.1, source `foundations-of-pluripotential-theory:4A0FAEB3`, permanent `409656CC47D4`, physical lines **10–40**, especially the dual-gradient pushforward and mass formula at lines **11–21, 28–38**. Theorem 21.5.2, source `foundations-of-pluripotential-theory:6403CF44`, permanent `F4072D9ED060`, lines **44–84**, specifically local-uniform-to-vague continuity and full-mass criterion. Example 21.5.3, source `foundations-of-pluripotential-theory:87E8B742`, permanent `6BCC82ADB7C7`, lines **90–94** was compared only to distinguish the loss-of-mass example.
- **Narrow convergence dependency:** `docs/sections/convex-analysis-and-toric-potentials--compact-convex-envelopes-and-full-mass-limits/index.html`, main blob `b3b4e34fff767a717df812a381f905589b257fb3`: Lemma 21.6.2, source `foundations-of-pluripotential-theory:55EDF0D7`, permanent `F2FABB0A312F`, lines **32–45**.
- **Conventions only:** §21.4.1–2 identify the convex slope body `K_F` and full-mass class. The audit uses the printed dimension-one normalization `1!=1`; it does not invoke the excluded Demailly/Bergman/L2/OT programme.

## Statement and exact proof

Let `a<b` and `P=[a,b]`. Let `H:R -> R` be a **finite convex** function with `K_H=P` and with its conjugate `G=H^*` finite at **both endpoints** `a,b`. (In particular, `dom G` contains `(a,b)`.) Let `mu_H=MA_R(H)` as defined in Theorem 21.5.1. Then `mu_H(R)=b-a`, it has finite first absolute moment, and there is the **exact identity**

```text
(A)   integral_R |x| dmu_H(x) = G(a)+G(b)+2 H(0).
```

For two such functions `F,H`, writing `G_F=F^*`, `G_H=H^*`, their equal-mass optimal transport distance (with **unnormalized** transport cost) satisfies

```text
(B)   W1(mu_F,mu_H)
        = integral_a^b |G_F'(p)-G_H'(p)| dp
        = integral_R |F'_+(x)-H'_+(x)| dx.
```

The derivatives in the first integral exist almost everywhere. The `F'_+` and `H'_+` in the second integral are right derivatives. If the measures are normalized to probabilities, divide both the cost and the right-hand sides by `b-a`.

**Proof of (A).** Theorem 21.5.1 represents `mu_H` as the pushforward of Lebesgue measure on `(a,b)` by the a.e. derivative `G'(p)`. Because `G` is a closed proper convex function finite at `a,b`, it is continuous on the entire compact interval `[a,b]` (including one-sided endpoints); its a.e. derivative is monotone and integrable there, with absolute-derivative integral equal to the total variation of `G`. For any minimizer `p_0` of `G`, monotonicity of `G'` yields

```text
 integral_a^b |G'(p)| dp = G(a)-G(p_0)+G(b)-G(p_0).
```

Fenchel–Moreau duality gives `H(0)=sup_p[-G(p)]=-G(p_0)`. Substitution proves (A), including finiteness, with no differentiability or strict convexity assumption on `H`.

**Proof of (B).** The maps `p |-> G_F'(p)` and `p |-> G_H'(p)` are nondecreasing and push forward Lebesgue measure to the respective Alexandrov measures. Pairing equal parameters `p` therefore gives an admissible transport coupling. It is optimal for cost `|x-y|`: whenever `x_1<=x_2` and `y_1<=y_2`, the elementary uncrossing inequality

```text
 |x_1-y_1|+|x_2-y_2| <= |x_1-y_2|+|x_2-y_1|
```

allows any crossed finite coupling to be uncrossed without increasing cost. Approximation of the two monotone maps by step functions, followed by truncation and the finite-first-moment bound (A), proves optimality for the actual pushforwards. This establishes the first formula. In dimension one the cumulative distribution of `mu_H` is `H'_+(x)-a`: the subgradient image of `(-infinity,x]` fills the slope interval from the left asymptotic slope `a` to `H'_+(x)`. The identical one-dimensional uncrossing/layer-cake formula `W1(mu_F,mu_H)=integral_R |CDF_F(x)-CDF_H(x)| dx` gives the second formula. No multidimensional transport result is being assumed.

**Exact convergence criterion.** Let `F_j,F` satisfy the preceding hypotheses for the same `P=[a,b]`, and suppose `F_j -> F` locally uniformly on `R`. Then

```text
(C)   W1(MA_R(F_j),MA_R(F)) -> 0
      if and only if
      F_j^*(a) -> F^*(a)  AND  F_j^*(b) -> F^*(b).
```

Indeed, Theorem 21.5.2 and Lemma 21.6.2 give narrow convergence of the equal-mass measures. Their a.e. nondecreasing quantile maps `Q_j=(F_j^*)'`, `Q=(F^*)'` therefore satisfy `Q_j(p)->Q(p)` for a.e. `p in (a,b)`: the usual generalized-inverse sandwich at every continuity point of the monotone quantile `Q` proves this directly; discontinuities are at most countable. For these maps, `integral|Q_j|=F_j^*(a)+F_j^*(b)+2F_j(0)` by (A). If both endpoints converge, these integrals converge because `F_j(0)->F(0)`. Almost-everywhere convergence plus convergence of the absolute integrals implies `Q_j->Q` in `L1(a,b)` (apply the dominated minimum argument to the positive/negative parts, equivalently Scheffé's lemma). The first formula in (B) proves `W1->0`.

Conversely, the function `x |-> |x|` is 1-Lipschitz; any coupling bounds the difference of first absolute moments by its transport cost. Thus `W1->0` forces first absolute moments to converge. Formula (A), combined with `F_j(0)->F(0)`, gives convergence of **the sum** of the two endpoint conjugate values. For each fixed `p`, the representation `F_j^*(p)=sup_x(px-F_j(x))` and pointwise convergence of `F_j(x)` imply `liminf_j F_j^*(p)>=F^*(p)`. Applied at `p=a,b`, these two individual lower bounds and convergence of their finite sum force **separate** endpoint convergence. This proves (C).

## Distinction from prior findings, proposed addition, and dependent risks

The already recorded **2026-11-05** finding `POME-TORIC-FULLMASS-WASSERSTEIN-NONUPGRADE-001` gave a full-mass sequence whose narrow convergence fails to imply `W1` convergence. **That example is not a new finding here.** The new result is the **if-and-only-if diagnostic (C)** plus the two exact transport identities (A)–(B), which pinpoint *only the endpoint conjugate values* as the additional requirements in one dimension when first moments exist. In the prior example `F_R=(1-c/R)x_++(c/R)(x-R)_+`, `F_R^*(1)=c` while `F^*(1)=0`, consistent with (C). We do not claim the old numerical example as this run's progress.

**Proposed audit-only mathematical note:** after the §21.6.2 narrow-convergence lemma, state (C) as an optional dimension-one refinement, with the endpoint-finiteness hypothesis visible. It is not a proposed amendment to the printed general-dimensional theorem. The printed Theorems 21.5.1/2 and Lemma 21.6.2 are not refuted. Any proposed `W1` convergence upgrade for one-dimensional toric models in §§21.12–21.13 must verify the two endpoint conjugate values (or a stronger moment hypothesis). No actual downstream theorem has been proved erroneous by this audit.

**Dependencies/status boundary:** Formula (A) relies on the printed dual-gradient representation in §21.5.1 and elementary one-dimensional convex calculus; (B) supplies an elementary monotone-coupling justification; (C) relies on the narrow convergence statements §21.5.2 and §21.6.2, not re-certified end to end here. This is therefore a **verified conditional deduction**, not a full independent verification of Alexandrov measure construction. No source/registry/tag changes, build, tests, CI or publication were attempted.
