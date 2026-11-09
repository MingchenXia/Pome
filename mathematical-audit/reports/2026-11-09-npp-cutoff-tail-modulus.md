# Tail-mass modulus for the closedness cutoff in non-pluripolar products

- **Date:** 2026-11-09
- **Stable finding:** `POME-NPP-CUTOFF-TAIL-MODULUS-001`
- **Severity / classification:** low / **verified conditional deduction**. This is an additional quantitative consequence, **not** a false printed theorem, confirmed proof gap, or unconditional verification of the analytic prerequisites.
- **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`
- **Actual integrated reading edition:** `docs/sections/non-pluripolar-products--closedness-and-cutoff-gradients/index.html`, blob `f781fa61bd20944c7c4798e0e0984cfb81ef069f`.
- **Target:** Theorem 13.3.1, source label `foundations-of-pluripotential-theory:A226C692`, permanent tag `8A125B338F90`, physical line 11 (statement) and lines 16–47 (replacement proof); section source label `foundations-of-pluripotential-theory:F7A6FBFD`, permanent tag `4D61EAFD1D21`.
- **Dependency anchors directly checked:** local truncation support and plurifine locality (lines 23–28, internal Lemma 13.2.2); gradient formula / bound (31–37, internal (7.14.4) and Theorem 5.3.7); chain rule and Cauchy–Schwarz (39–45, internal (7.14.5–6)); spanning of real forms (47, internal Proposition 5.3.2).
- **Affected dependents:** any use of the local closedness assertion in §§13.4–13.11, in mixed non-pluripolar mass arguments and in §§17.2–17.5; **no modification of their theorem statements is proposed**.

## Precise local setting

Work on a relatively compact coordinate neighborhood `U` in a complex manifold of dimension `n`. Let `1 <= p < n`, and let `u_1,...,u_p` be plurisubharmonic functions shifted so that `u_j <= 0`. As in the integrated proof set

```text
u := sum_j u_j,
u_{j,k} := max(u_j,-k),
O_k := intersection_j {u_j > -k},
Theta_k := gamma wedge (dd^c u_{1,k}) wedge ... wedge (dd^c u_{p,k}),
S := gamma wedge <dd^c u_1 wedge ... wedge dd^c u_p>,
w_k := max(1 + u/k, 0).
```

Here `gamma` is a constant strongly positive `(n-p-1,n-p-1)` form, `beta` is the fixed Euclidean Kähler form, and the trace measure `m := S wedge beta` is locally finite. By the definition and plurifine locality of non-pluripolar products,
`1_{O_k} Theta_k = 1_{O_k} S`, and `m({u=-infinity})=0`.

Fix a smooth `zeta: R -> [0,1]` with `zeta(t)=0` for `t<=1/2` and `zeta(t)=1` for `t>=1-delta`, where `0<delta<1/2`. The plateau parameter `delta` may be chosen for any cutoff admitted in the printed proof, perhaps after decreasing it.

## New quantitative statement

For every compact `KSubset U`, and every smooth compactly supported real one-form `eta` with `K_0:=supp etaSubset U`, the following bounds hold for every positive integer `k`:

```text
(1)  0 <= (S - zeta(w_k) Theta_k) wedge beta <= 1_{ {u <= -delta*k} } m,

(2)  |< d(zeta(w_k) Theta_k), eta >|
       <= C_eta [ m(K_0 intersect {u <= -delta*k}) ]^(1/2).
```

In (1) the assertion is as measures, so the total trace mass of the cutoff defect on `K` is at most `m(K intersect {u <= -delta*k})`. Constants in (2) depend on `eta`, the fixed cutoff, the local compact supports and the local mass of `S`, **but not on `k`**. They incorporate the constants in the already stated gradient estimate (7.14.6).

Since `u=sum_j u_j` and all summands are nonpositive,

```text
m(K intersect {u <= -delta*k})
   <= sum_{j=1}^p m(K intersect {u_j <= -(delta/p)*k}).
```

Each tail on the right vanishes as `k -> infinity` by local finiteness and the absence of mass on the pole sets. Thus (1) gives **local trace-norm** convergence of the positive cutoff currents, while (2) gives an **explicit conditional weak differential-error modulus**; no universal numerical convergence rate is implied.

## Complete derivation

**Support and positive trace defect.** The cutoff `zeta(w_k)` vanishes if `w_k<=1/2`, so it vanishes outside `O_k`. Locality gives the *exact current identity*
`zeta(w_k) Theta_k = zeta(w_k) S`. Consequently
`S-zeta(w_k)Theta_k=(1-zeta(w_k))S >=0`.
At any nonpolar point with `u> -delta*k`, `w_k=max(1+u/k,0)>1-delta`; hence `zeta(w_k)=1`. On the pole set `m` is zero. It follows that
`0 <= (1-zeta(w_k))m <= 1_{ {u<=-delta*k} }m`, proving (1).

**Gradient energy is uniformly bounded.** Write `E_{Theta_k}(w_k)` for the positive gradient measure of (7.14.4). Choose a nonnegative smooth compactly supported `tau`, equal to one near `K_0`. The integrated proof's lines 31–37, using positivity of `w_k dd^c w_k wedge Theta_k`, imply
```text
int tau E_{Theta_k}(w_k)
 <= (1/2)int w_k^2 dd^c tau wedge Theta_k
 <= C_tau int_{supp tau} 1_{O_k} Theta_k wedge beta
 <= C_tau m(supp tau) =: M_tau < infinity.
```
This is the **actual upstream energy inequality**, not an inference from convergence or from a project build.

**Cutoff derivative has tail support.** By the chain rule (7.14.5),
`d(zeta(w_k)Theta_k)=zeta'(w_k)dw_k wedge Theta_k`.
The derivative `zeta'` is zero outside `(1/2,1-delta)`; in particular, on its support
`u<=-delta*k`. The same support is contained in `O_k`. Therefore
```text
int_{K_0} |zeta'(w_k)|^2 Theta_k wedge beta
  = int_{K_0} |zeta'(w_k)|^2 1_{O_k} Theta_k wedge beta
 <= ||zeta'||_infinity^2 m(K_0 intersect {u<=-delta*k}).
```
Apply (7.14.6) with the weight `a=zeta'(w_k)` and test form `eta`. Its Cauchy–Schwarz factor containing `E_{Theta_k}(w_k)` is bounded by `M_tau^(1/2)`; the second factor is bounded by the square root of the displayed tail mass. This proves (2) with `C_eta` independent of `k`. Consequently the currents `zeta(w_k)Theta_k` converge to `S` on compact sets in trace norm, and their exterior differentials tend to zero weakly. Since each `Theta_k` is closed, the conclusion `dS=0` follows by continuity of differentiation in the sense of distributions.

**Individual tails.** If `u_1+...+u_p <= -delta*k`, at least one `u_j <= -(delta/p)*k`; otherwise their sum would be greater than `-delta*k`. Countable additivity and positivity of `m` give the final union bound. Each `m(K intersect {u_j <= -t})` decreases to `m(K intersect {u_j=-infinity})=0` as `t -> infinity`. No sequential compactness, exchange of infinite wedge products, or positivity-loss regularization is used.

## Verdict and limitations

The original Theorem 13.3.1 and its cutoff proof remain correct **conditional on the stated internal gradient/chain-rule and plurifine-locality results**. The new statement extracts an explicit, potentially slow local tail modulus already implicit in the proof, and strengthens its local cutoff convergence from weak convergence to trace-norm convergence **for the special cutoff currents**. It does **not** claim trace-norm convergence of raw Bedford–Taylor truncations or of arbitrary non-pluripolar products, nor does it establish a convergence rate depending only on `k`. In particular, the local finiteness hypothesis and non-charging of the pluripolar locus are indispensable for this argument. No main/source/registry/canonicalization modification is made.

**Proposed insertion (review only):** add a short remark after the proof of Theorem 13.3.1 containing (1)–(2), with the trace measure `S wedge beta` and the cutoff plateau `delta` explicitly specified. Preserve the existing theorem, permanent tags, attribution and the proof's internal citations. This report makes no assertion of full upstream verification.
