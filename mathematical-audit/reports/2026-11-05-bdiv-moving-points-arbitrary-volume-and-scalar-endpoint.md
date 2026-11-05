# Mathematical audit: moving point blowups, the full volume-jump spectrum, and the zero-scalar endpoint

**Date:** 2026-11-05. **Production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (unchanged).
**Audit scope:** integrated Chapter 20, section 20.1 only, with §20.1.7–9 and §20.1.39–43 checked at their exact hypotheses. No approximation/regularization research undertaken.

**Integrated reading file:** `docs/sections/the-theory-of-b-divisors/index.html`, main blob `4a793dfd462badcb351f54a36cb030cde14a399b`. Physical lines 66–119 (volumes, upper semicontinuity, moving-point example) and 737–833 (the domain of the two mixed products and their homogeneity statements).

## POME-BDIV-MOVING-POINT-ARBITRARY-VOLUME-001
**Severity:** low. **Status:** verified conditional deduction (with an elementary proof of the additional model, conditional only on the printed definitions of nef Cartier b-divisor and their volume). **No printed theorem is false.**

**Source anchors.** Lemma 20.1.7: `sgpt:54FCB4C1`, permanent `F5B2C1F1E318`, lines 66–96; Example 20.1.9: `sgpt:048A0D73`, permanent `7AF528B0FB3B`, lines 100–120. The exact upper-semicontinuity formula is Equation 20.1.8, `sgpt:D44AA2EA`, permanent `3BFB2E87E034`, lines 68–70. Definition 20.1.5 of a Weil b-divisor: `sgpt:2A98D289` / `178D74F44C30`, lines 39–53; Definition 20.1.6 of its volume: `sgpt:0B20B6FE` / `E6F6681E7170`, lines 56–63; nef Cartier Definition 20.1.11: `sgpt:DF932FEE` / `FB2640F8F828`, lines 128–130.

**Exact stronger statement.** Fix *any* pairwise distinct sequence of points `p_i` in `X=P^2`; no generic-position hypothesis is necessary. Write `pi_i:Y_i=Bl_{p_i}X -> X`, with exceptional curve `E_i`, and `H=c_1(O_X(1))`. For *any* sequence `0<=a_i<=1`, let `B_i` be the Cartier b-divisor realized by `pi_i^*H-a_i[E_i]` on `Y_i`, and let `B` be the Cartier b-divisor realized by `H` on `X`. Then:

1. Every `B_i` is nef with root `H`; `B_i` is big exactly if `a_i<1`.
2. `B_i -> B` in the **projective-limit topology on all modifications**, indeed every fixed model trace is equal to the corresponding trace of `B` for all sufficiently large `i`.
3. `vol(B_i)=1-a_i^2` and `vol(B)=1`.

Hence **every** prescribed numerical sequence `v_i in [0,1]` occurs as `vol(B_i)` for a convergent sequence of nef Cartier b-divisors with the **same big root `H`** (take `a_i=sqrt(1-v_i)`). If all `v_i>0`, all approximants are **big and nef**. In particular, choosing alternating `a_{2i}=1/2`, `a_{2i+1}=sqrt(3)/2` produces positive, nonconvergent volumes `3/4,1/4,3/4,1/4,...` for a convergent sequence, rather than just the zero-versus-one endpoint in the printed example. The original upper-semicontinuity inequality remains sharp; the construction neither provides nor contradicts a lower-semicontinuity theorem.

**Proof, without any regularization.**

*Step 1: the nef cone and the volume on a single blowup.* There are two morphisms `pi:Y -> P^2` and `f:Y -> P^1`, the latter given by the pencil of lines through `p`. The divisor classes `pi^*H` and `pi^*H-E=f^*c_1(O_{P^1}(1))` are nef, as pullbacks of ample classes. For `0<=a<=1`,
`pi^*H-aE=(1-a)pi^*H+a(pi^*H-E)` is nef. It is big exactly when its square `1-a^2` is positive (nef-surface volume). For clarity this volume can also be checked directly, including real `a`, without invoking an asymptotic intersection formula. Choose homogeneous coordinates with `p=[1:0:0]`. Degree-`k` homogeneous polynomials vanishing to order at least `m_k=ceil(ka)` at `p` have dimension
`binom(k+2,2)-binom(m_k+1,2)` for `0<=m_k<=k`; the excluded monomials are exactly those with total degree in `x_1,x_2` smaller than `m_k`. Consequently `lim_{k->infinity}(2/k^2)h^0(Y,k(pi^*H-aE))=1-a^2`, using the conventional rounded-real-divisor interpretation. For `a=1` this limit is zero, while for `a<1` it is positive. The Cartier b-divisor's volume is the volume on its nef realization: on dominating models the class is a pullback, with the same volume; any other model is dominated by a common refinement and has no smaller volume by the printed birational volume monotonicity used in Definition 20.1.6. Thus its infimum over model traces is exactly `1-a^2`.

*Step 2: convergence on every fixed model.* For a fixed modification `rho:Z -> P^2` of smooth compact complex surfaces, the locus in the target where `rho` fails to be an isomorphism is a **finite set of points**: a nontrivial blowup with smooth divisor center is an isomorphism, and a birational morphism between smooth surfaces is a composition of finitely many point blowups (alternatively use the image of its exceptional curves). This is a standard surface modification fact, independent of any approximation or regularization theorem. Since `p_i` are pairwise distinct, all but finitely many avoid this set. For such `i`, take a smooth common model dominating `Z` and `Y_i`; the exceptional curve over `p_i` is exceptional for the map to `Z`, so its divisor class pushes forward to zero. The trace of `B_i` on `Z` is therefore exactly `rho^*H`, the trace of `B`. No limit interchange, subsequence, or assumption about the positions of the `p_i` on algebraic curves is used. As convergence of b-divisors is coordinatewise on *all* fixed models, this establishes the convergence.

*Step 3: arbitrary bounded numerical volume behavior.* Substitute `a_i=sqrt(1-v_i)` in the exact formula. The root stays `H`, fixed-model traces eventually coincide, and all the stated properties follow. In particular the full range of possible liminf/limsup phenomena is exhibited without contradicting the printed `limsup<=1`.

**Proposed non-production improvement.** In Example 20.1.9 the stronger condition that every algebraic curve contains only finitely many `p_i` can be weakened to pairwise distinct points, because a *fixed birational morphism of smooth surfaces* has only finitely many non-isomorphism points in its target. Optionally add the one-parameter family `pi^*H-aE` and the exact `1-a^2` volumes as a sharpness remark. Retain the printed original example and its attribution; it is correct as written.

**Affected dependents:** the interpretation of §20.1.7–9's upper-semicontinuity and the need to distinguish b-divisor convergence from convergence of volumes. No general nef b-divisor approximation theorem is certified here.

## POME-BDIV-BIG-PRODUCT-ZERO-SCALAR-TYPE-001
**Severity:** low. **Status:** confirmed error **of statement-domain typing only**, not a false numerical equality and not a counterexample to the extended intersection theory.

**Source anchors.** Definition 20.1.39: `sgpt:6AA949A3`, permanent `BFB26AC5F975`, lines 737–743, defines the intersection only for **big and nef** arguments. Lemma 20.1.40 clause (3): `sgpt:456D590A`, permanent `DFC2368D5436`, clause `sgpt:B89A01E8`, permanent `6704C2A24387`, lines 746–763 and proof lines 773–794, assumes the `D_j` are big and nef yet permits **lambda=0** in the first slot. The zero b-divisor is nef but **not big** (volume zero), so the left-hand intersection is **not defined by Definition 20.1.39** at this endpoint. The subsequent Definition 20.1.41 (`sgpt:8F1B53C8`, permanent `60343D71D40A`, lines 798–808) extends the intersection to arbitrary nef inputs; Proposition 20.1.43 clause (3), `sgpt:5189BD1D` / `AEC81016D4BC`, lines 809–831, correctly includes lambda=0 **in that extended domain**.

**Precise non-production correction.** Replace `lambda>=0` by `lambda>0` **only in Lemma 20.1.40(3)**, or explicitly qualify its lambda=0 endpoint as interpreted by the *later* Definition 20.1.41. Keep `lambda>=0` in Proposition 20.1.43(3). With `lambda>0`, positive scalar multiplication preserves bigness, so all terms of the earlier lemma are well typed. At `lambda=0`, the later nef extension gives the expected value zero. The homogeneous identity is mathematically consistent; the defect is that a formula is written before its full domain is defined.

**Affected dependents:** local logical ordering of Definition 20.1.39, Lemma 20.1.40, Definition 20.1.41 and Proposition 20.1.43. No proof of the general b-divisorial intersection formalism is claimed.

## Boundaries of this audit

This pass checked **only** the displayed definitions, an explicit blowup-family model, convergence on fixed smooth surface modifications, and the scalar endpoint's domain. It did **not** certify all of §20.1, the general higher-dimensional nef-b-divisor approximation, the mixed-volume machinery in §18.1, or the general intersection-product proof. All older confirmed errors, missing proof steps, external inputs, genuine duplications and verified repairs remain independently classified. All owner-excluded Demailly approximation/regularization, dedicated Bergman, weighted L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion work stays **deferred-by-user**, not resolved or certified. No source/body/registry/permanent-tag edits, build, tests, CI, or website publishing.
