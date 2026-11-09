# Audit: constrained minima are sharply Lipschitz in a moving upper endpoint

**Stable finding ID:** `POME-ENVELOPE-MOVING-ENDPOINT-LIPSCHITZ-001`  
**Date:** 2026-11-09  
**Severity / status:** low / **verified conditional deduction** (a supplementary exact stability result; **no printed theorem is false**, and no missing proof is claimed repaired).  
**Production main SHA:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Integrated reading edition:** `docs/sections/envelopes-and-model-potentials--measures-on-contact-sets--a-minimum-with-a-varying-upper-radius/index.html`, blob `879fd87eacb65755ae0e7a9ffc95e71d1c262d39`, physical lines 10–55. Lemma **16.18.1**, stable source label `foundations-of-pluripotential-theory:1E3A3A35`, permanent tag `93E8FFBE7FEB`; hypotheses and statement at lines 10–24, scalar minimization and Euler equation at lines 27–42, Schur complement at 43–49, and distributional limit at 52–55.

## Scope and exact deduction

At a fixed base point (z), let (c>0), and let (H(s)=H(z,s)) be a (C^2) function on ((-infty,B]), possibly on a larger interval, such that (H_s\ge0), (H_{ss}>0), and (H) is bounded below as (s\to-\infty). Put
[
 F(s)=H(s)-cs,qquad V(b)=\inf_{s\le b} F(s),quad b\le B.
]
The lower bound on (H) implies (F(s)\to+\infty) at (-\infty), so this minimum exists and is unique; a minimizer is either the endpoint (b), or the unique interior solution of (H_s(s)=c).

**New precise statement.** For any (b_1\le b_2\le B),
[
              0\le V(b_1)-V(b_2)\le c(b_2-b_1). \tag{A}
]
In fact the scalar endpoint map is (C^1) and
[
              V'(b)=\min\{H_s(b)-c,0\}\in[-c,0]. \tag{B}
]
Both the coefficient (c) in (A) and the coefficient (1) in the following obstacle-error estimate are universally optimal. If functions (H_1,H_2) obey the same coercive and nonnegative-slope assumptions on all (s\le\max\{b_1,b_2\}) and
[
       |H_1(s)-H_2(s)|\le\delta
       \quad(s\le\max\{b_1,b_2\}),
]
then
[
 |\inf_{s\le b_1}(H_1(s)-cs)
    -\inf_{s\le b_2}(H_2(s)-cs)|
       \le\delta+c|b_1-b_2|.\tag{C}
]
For (z)-dependent data on a domain (D), (A)–(C) hold **pointwise** in (z), so local or global (L^\infty) bounds follow whenever the common half-line domain and uniform discrepancy assumptions hold. No curvature bound on (b_i) is required for these scalar value estimates. To obtain the **complex Hessian** bound for each minimizer, one still needs all the separate joint-Levi and Hermitian hypotheses of printed Lemma 16.18.1; (A)–(C) do **not** prove any regularity for an arbitrary limiting obstacle.

## Direct proof, including transition at the constrained/unconstrained minimum

For (b_1\le b_2), the admissible interval for (V(b_1)) is contained in that of (V(b_2)), yielding (V(b_1)\ge V(b_2)). Let (s\le b_2) be any competitor and set (t=\min\{s,b_1\}). If (s>b_1), then, using only (H_s\ge0),
[
 F(t)-F(s)=F(b_1)-F(s)
    =\int_{b_1}^{s}(c-H_s(\sigma))\,d\sigma
    \le c(s-b_1)\le c(b_2-b_1).
]
If (s\le b_1), this difference is zero. Therefore
(V(b_1)\le F(t)\le F(s)+c(b_2-b_1)).
Take the infimum over (s\le b_2) to obtain (A). This proof neither differentiates (b(z)) nor uses the Schur complement; in particular it is robust for merely measurable or continuous (b_i(z)) provided the pointwise minima are well defined.

To prove (B), (F'(s)=H_s(s)-c) is strictly increasing. Its lower limit at (-\infty) is (-c): indeed (H_s(s)\downarrow\ell\ge0) as (s\to-\infty), and \(\ell>0\) would force (H(s)\to-\infty), contradicting the lower bound. If (H_s(b)<c), (F) strictly decreases throughout ((-infty,b]), so (V(b)=F(b)) and (V'(b)=H_s(b)-c). If (H_s(b)>c), there is a unique (s_0<b) with (H_s(s_0)=c); the minimizer (s_0) remains unchanged as the upper endpoint moves locally, and (V'(b)=0). At (H_s(b)=c), both one-sided derivatives tend to zero by continuity; therefore (V) is (C^1), with (B).

At a fixed endpoint (b), the bound (|H_1-H_2|\le\delta) implies the minima differ by at most (delta): add/subtract the discrepancy for every admissible (s), then take infima. Apply (A) to either one of (H_1,H_2), and use the triangle inequality to prove (C).

## Sharpness and exact test models

* **Sharpness of the obstacle coefficient 1.** Let (H_2(s)=H_1(s)+\delta) with the same endpoint. Then (V_{H_2}(b)=V_{H_1}(b)+\delta); no coefficient (<1) is valid.
* **Sharpness of (c), without revisiting the previously audited curvature coefficient.** Let (H(s)=e^s), which is strictly convex, increasing and bounded below at (-\infty). For (b<\log c), (H_s(s)<c) throughout (s\le b), and
  (V(b)=e^b-cb). Hence for (h>0) with (b+h<\log c),
  [
    \frac{V(b)-V(b+h)}h
      =c-e^b\frac{e^h-1}{h}\longrightarrow c
       \qquad\text{as }b\to-\infty
  ]
  for each fixed (h>0). No constant (<c) can replace (c) in (A) or (C).
* **Why (H_s\ge0) matters.** If this hypothesis is omitted, (H(s)=e^s-Ms) for (M>0) still has (H_{ss}>0) and grows at (-\infty), but for low endpoints (V(b)=e^b-(M+c)b) has slope tending to (-(M+c)). Thus the displayed universal (c)-Lipschitz estimate is false without a lower bound on (H_s). This **does not** contradict the printed lemma, which explicitly assumes (H_s\ge0).

The (H=e^s) model had previously been used in `POME-ENVELOPE-VARYING-RADIUS-SHARP-BARRIER-001` to test the **curvature** coefficient (cC_b). The present finding tests a **different parameter and assertion**, namely endpoint-value stability with an arbitrary perturbation (b_1-b_2); no earlier (\varepsilon\log(1/\varepsilon)) penalty rate, curvature sharpness, or smoothing programme is claimed as new here.

## Hypothesis audit, proposed text and dependents

Printed Lemma 16.18.1 assumes (H_s\ge0), (H_{ss}>0), lower boundedness of (H), smooth (b) and a conditional joint Levi bound (only where (s\le b(z)) and (H_s\le c)). The scalar proof above uses exactly the first three assumptions and the existence of a common domain. Its statement is **correct**; no change to existing wording, tag, attribution, or normalization is proposed.

**Suggested optional remark after Lemma 16.18.1:** The constrained minimum is (c)-Lipschitz in its moving upper endpoint and (1)-Lipschitz under a uniform additive obstacle perturbation; (B) gives the exact endpoint sensitivity. These estimates can be used to track the error caused by changing an upper-radius constraint in later contact-set and envelope constructions, including §§16.19–16.20, **only when those constructions satisfy the common-domain and slope hypotheses**. This is not a verification of their smoothing, weak-Hessian, or PDE inputs. Do not automatically import it into Demailly approximation or the user-excluded programme.

**Ledger status:** verified conditional deduction, severity low; no confirmed error, no repaired proof gap, no source external dependency introduced. The previous `POME-ENVELOPE-VARYING-RADIUS-SHARP-BARRIER-001` remains a separate existing finding, unchanged. The historical provenance in the integrated lemma is preserved.

**Coverage:** Selected incremental proof check in already-sampled §16.18; §16.19 and §16.20 are **potential dependents only**, not newly reviewed in this increment. Zero newly first-visited numbered sections; zero whole-section certifications; directory baseline 25 chapters / 747 sections. No tests, build, CI, publication, formal proof verification, source edits, registry/canonicalization edits, or production `main` edits were performed. Demailly regularization and its designated Bergman, (L^2), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion work remain `deferred-by-user` and were not opened.
