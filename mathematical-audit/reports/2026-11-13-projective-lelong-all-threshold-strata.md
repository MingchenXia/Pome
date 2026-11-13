# Audit of every positive Lelong threshold in the projective line-series model

**Date:** 2026-11-13.
**Finding:** POME-SIU-STRICT-LEVEL-ONLY-ONE-WALL-001.
**Status/severity:** verified conditional deduction / low. The printed statements in §5.34.2 and Example 5.34.4 are **not** false. The calculation below extends the checked example and is not a proof of general Siu analyticity.

## Pinned reading-edition input

- Reviewed production main: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
- Exact reading file: \`docs/sections/plurisubharmonic-functions-and-singularities--analytic-types-and-restriction/index.html\`, blob \`cff8b3156b07aff2f3d881d83d04608e87b7f2c8\`.
- §5.34.2, Lelong level sets: source \`non-kahler-pluripotential-theory:86D804B1\`, permanent tag \`E911F3E2C8E9\`, physical lines 65–71.
- Example 5.34.4: source \`non-kahler-pluripotential-theory:22A3233E\`, permanent tag \`697E97CED780\`, physical lines 94–132, especially the current decomposition at 109–115 and the pointwise Lelong formula at 117–130.
- Relation to previously recorded §5.34 checks: the 2026-10-28 report established the ball-area normalization and Hausdorff exponent, but did not classify **all positive thresholds** or isolate the sole strict-level nonanalyticity threshold. This is additive selected work; neither the earlier findings nor their classification are changed.

## Statement and complete example calculation

In the printed model on X=P^2 with homogeneous coordinates [x:y:z], let

- D={y=0}, L_j={x-2^{-j}z=0}, lambda_j=2^{-j-1} (j>=1);
- p_j=[2^{-j}:0:1], p_*=[0:0:1], q_infty=[0:1:0];
- u the globally defined (3/2)omega_FS-psh potential from Example 5.34.4, so (3/2)omega_FS+dd^c u=[D]+sum lambda_j[L_j].

The right-hand side is a positive closed current: the coefficient sum is 1/2 and each projective line has finite unit FS mass. At a point q, in a local Euclidean chart, a complex affine line H with distance d(q,H) has dd^c|w|^2-area inside B(q,r) exactly (r^2-d(q,H)^2)_+. Dividing by r^2 yields a number in [0,1] tending to 1 if q belongs to H and 0 otherwise. Dominated convergence for the summable coefficients gives the **pointwise**, not merely generic, Lelong number formula

    nu(u,q)=1_D(q)+sum_{j>=1}lambda_j 1_{L_j}(q).

The intersection geometry is exact: distinct L_i,L_j meet only at q_infty, which lies off D; D meets L_j only at p_j; and p_j tends to p_*, which is in D but in no L_j. Thus the possible values are:

- nu=1+lambda_j at p_j;
- nu=1 at D\{p_j};
- nu=1/2 at q_infty;
- nu=lambda_j on L_j\(D union {q_infty});
- nu=0 elsewhere.

Let E_>= (t)={q:nu(u,q)>=t} and E_>(t)={q:nu(u,q)>t}. For every **real t>0**, their complete classification is as follows (all unions indexed by lambda_j >=t or >t are **finite** because lambda_j tends to zero):

| Threshold t | E_>=(t) |
| --- | --- |
| 0<t<=1/4 | D union (union over lambda_j>=t of L_j) |
| 1/4<t<=1/2 | D union {q_infty} |
| 1/2<t<=1 | D |
| 1<t<=5/4 | {p_j:lambda_j>=t-1} |
| t>5/4 | empty |

| Threshold t | E_>(t) |
| --- | --- |
| 0<t<1/4 | D union (union over lambda_j>t of L_j) |
| 1/4<=t<1/2 | D union {q_infty} |
| 1/2<=t<1 | D |
| t=1 | {p_j:j>=1} |
| 1<t<5/4 | {p_j:lambda_j>t-1} |
| t>=5/4 | empty |

At t=1/4 the strict set excludes L_1 away from q_infty, but q_infty still has Lelong number 1/2. At t=1/2 the strict set drops q_infty; at t=5/4 it drops p_1. These endpoint conventions are part of the result.

Every E_>=(t), t>0, is a finite union of projective lines and/or points and hence an analytic subset. More sharply, **E_>(t) is analytic for every t>0 except exactly t=1.** At t=1 the set {p_j} is not closed, since p_j->p_* and nu(u,p_*)=1. Thus the original printed counterexample to replacing Siu's >= by > has a unique positive strict-level wall; all other strict thresholds remain analytic **in this particular example**.

No claim is made about strict Lelong superlevel analyticity for an arbitrary positive current, and the example's special classification cannot replace Siu's theorem.

## Audit disposition

- **Classification:** verified conditional deduction; the direct incidence/area/dominated-convergence calculation is complete for this explicit model, conditional only on the displayed integrated positive-current decomposition and standard local normalization. It does not require the general Siu theorem.
- **Correction proposed:** no correction to Example 5.34.4 or §5.34.2. An optional explanatory remark may state that nonanalyticity in this model occurs only at the strict threshold 1.
- **Affected dependents:** interpretations of §5.34.2 and the general upper-level analytic-set input Theorem 6.9.5. The calculation confirms the logical need for the non-strict inequality but neither reproves nor refutes those general results.
- **Scope:** only the above original example and Lelong-level claims were checked. No other part of §5.34 or Chapter 5, no entire theorem dependency chain, and no production source was certified. Demailly approximation/regularization and the dedicated Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss programme remain **deferred-by-user**; nothing here reopens it. No build, tests, CI, or publication was run.
