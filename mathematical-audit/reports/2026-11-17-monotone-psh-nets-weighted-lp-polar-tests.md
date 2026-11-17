# Weighted strong convergence for increasing psh nets: the pluripolar measure boundary

**Finding:** `POME-PSH-MONOTONE-NET-WEIGHTED-LP-POLAR-001`  
**Date:** 2026-11-17  
**Classification:** low / **verified conditional deduction** (not a printed theorem error).  
**Main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Integrated section:** `docs/sections/relative-energy-and-perron-segments--continuity-and-compactness/index.html`, blob `6fd38d5ff9d0037e9d0d347814a95ad97331715f`.  
**Source and stable anchors:** `foundations-of-pluripotential-theory:24DDA159`; Proposition 17.4.1, permanent tag `049F75F5547D`, physical lines 10–15 (statement), 71–72 (Choquet/countable extraction and the **noncofinal** directed-net argument). Inputs: integrated Theorem 5.10.2, tag `D32A2FB94F6B` (upper-envelope countable reduction); the standard pluripolar exceptional-set conclusion for increasing psh envelopes, used in the printed §17.4.1 proof as well.

## Claim and precise conditions

Let `X` be a compact complex manifold, `theta` a smooth closed real (1,1)-form admitting local potentials, and `(u_i)_(i in I)` an increasing **directed net** of `theta`-psh functions, none identically minus infinity. Assume a common upper bound, and let `U=(sup_i u_i)^*`, which is `theta`-psh. Let `nu` be any fixed positive finite Borel measure which charges no pluripolar set. For a chosen `i_0`, suppose

```
        integral_X (U-u_(i_0))^p dnu < infinity,   1 <= p < infinity,
```

interpreting the difference outside a `nu`-null polar set. Then the **original directed net** satisfies

```
        ||U-u_i||_(L^p(nu))  -->  0
```

as `i` tends along `I`; there is no cofinality, metrizability-of-`I`, or subsequence assumption. In the setting of Proposition 17.4.1, the claim is additional **strong convergence** and does not replace, prove, or strengthen the independent energy/mixed-mass inputs for the displayed energy identity. No rate uniform over families or varying measures is asserted.

## Proof, including the net quantifier

Use the finite coordinate cover and Choquet countable reduction already explicitly constructed in the **Nets** paragraph of the integrated §17.4.1 proof. Fix `i_0` and, by directedness, select an increasing sequence `i_1 <= i_2 <= ...`, all dominating `i_0`, such that

```
        (sup_k u_(i_k))^* = U.
```

The indices need not be cofinal in `I`. For an increasing sequence of (quasi-)psh functions, the raw supremum agrees with its upper-semicontinuous regularization off a pluripolar set. Therefore `u_(i_k)(x) increases to U(x)` for `nu`-almost every `x`. Set `d_i=U-u_i` outside polar exceptional sets. For `i >= i_0`,

```
       0 <= d_i <= d_(i_0)       nu-almost everywhere.
```

Dominated convergence applied to `d_(i_k)^p`, bounded by the assumed `L^1(nu)` majorant `d_(i_0)^p`, yields `||d_(i_k)||_p -> 0`. Given `epsilon>0`, choose one index `i_k` with `||d_(i_k)||_p<epsilon`. Every `i>=i_k` has `d_i<=d_(i_k)` `nu`-a.e. and hence `||d_i||_p<epsilon`. This proves **convergence of the entire directed net** without mistaking the selected sequence for a cofinal sequence. The argument uses no interchange between unrelated limiting operations.

In particular, `nu=dV` is admissible on compact charts, giving `L^p` convergence whenever the displayed integrability condition holds; the usual local finite-`p` integrability of psh functions is an optional additional input, **not** required by the stated conditional result. For the energy class, the existing energy theorem still supplies its own stronger energy conclusion; we do not infer energy convergence from `L^p` convergence alone.

## Why the measure restriction is real, even for bounded subharmonic functions

On the unit disc `D` take the bounded continuous subharmonic sequence

```
        v_k(z) = max{ (1/k) log|z|, -1 },       k=1,2,...,
```

with `log|0|=-infinity`. It is increasing: `log|z| <=0` on `D`. At every `z != 0`, `v_k(z)->0`, while `v_k(0)=-1` for every `k`. Hence `(sup_k v_k)^* = 0` on the disc, but the point mass `delta_0` satisfies

```
        ||0-v_k||_(L^p(delta_0)) = 1
```

for all finite `p>=1`, despite the bounded difference `0-v_1` being `delta_0`-integrable. The singleton `{0}` is polar, showing precisely why a `nu` which charges pluripolar sets is excluded. The `v_k` are already bounded, so this failure is not caused by infinite pole values. This is a **local model** and not a counterexample to the compact finite-energy Proposition 17.4.1.

As a quantitative independent check, with planar Lebesgue area `dA` and any `p>=1`,

```
  integral_D |v_k|^p dA
   = 2*pi*[ e^(-2k)/2 + k^(-p) integral_0^k t^p e^(-2t) dt ]
   ~ (pi*Gamma(p+1)/(2^p)) * k^(-p).
```

This follows by polar coordinates `r=exp(-t)` and the definition of the Gamma integral. Thus the same bounded functions converge strongly at exact `k^(-1)` norm order for area measure, but **not at all** for the polar atom. This contrast cannot be attributed to a sequential-compactness failure: even a sequence exhibits the boundary.

## Effect, exclusions, and disposition

**Proposed documentation correction/addition:** record the weighted `L^p` conclusion as a separately conditional corollary to the original-net Choquet step of §17.4.1, explicitly fixing the measure and domination condition. No printed claim of strong `L^p` convergence against arbitrary measures should be inserted. The original Proposition 17.4.1 is **not refuted** and no existing manuscript proof needs modification on this evidence.

**Affected dependents:** potential uses of §17.4.1 in §§17.5–17.9 and other monotone-envelope arguments may employ the fixed-measure conditional `L^p` conclusion if they independently verify integrability and non-pluripolarity; no Monge–Ampère energy, changing-measure, or full-section theorem-chain verification follows.

**Actual audit scope:** reread main §17.4.1 statement and its Choquet/net proof (especially physical lines 10–15 and 71–72), cross-checked the adjacent §17.4.3–5 compactness statements for the distinct sequential-`L^1` direction, and supplied the full new weighted-net argument and disc computation. §17.4 already had partial review: **+0 newly first-reviewed numbered sections; +0 completely certified sections**. Current ToC basis remains 25 chapters / 747 numbered sections, not a claim of exhaustive chapter verification. Previously recorded findings are unchanged.

**Deferred-by-user:** Demailly approximation/regularization and the dedicated Bergman/L2/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss programme were not examined or revived. No tests, builds, CI, source/registry edits, publication or formal certification are claimed.
