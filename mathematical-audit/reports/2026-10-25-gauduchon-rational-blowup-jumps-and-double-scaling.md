# Gauduchon degeneration: exact single-blowup rational jumps and a double-scaling transition

**Actual checkpoint:** 2026-10-25T01:00:02.981Z (UTC). **Fresh integrated main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Review branch before writing:** `1efbbcaad782d1b0e58210ed2809d19a4fa4f9fc`. This is a selected proof-level mathematical audit of current reading-edition §§12.21–12.23 and 12.25–12.26. The related §12.24 is only dependency context; no whole section, elliptic PDE theorem, or birational factorization chain is certified.

**Scope boundary:** The user's excluded Demailly approximation/regularization programme, including its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proofs, was not examined or resumed. Historical entries remain **deferred-by-user**.

## POME-GAUD-BLOWUP-RATIONAL-JUMPS-001

**Status:** verified conditional deduction; **severity:** low. The printed source proposition is **correct**. This is a strengthening by an exact leading asymptotic and a rational-jump realization, **not** a false-theorem claim, missing-proof classification, or completed verification of its analytic inputs.

**Integrated source:** `docs/sections/a-gauduchon-variational-volume--orders-of-degeneration-at-the-nef-boundary--strict-changes-under-one-blowup/index.html`; main blob `44644097cffbe33a98a2984623353827b8298fcd`. Proposition **12.23.1**, source label `non-kahler-pluripotential-theory-F3889ABB`, permanent tag `1E30136A67F6`, physical HTML lines **13–18**, with construction **24–38**, radial mass identity Equation **12.23.2**, source `non-kahler-pluripotential-theory-D2C0DDD8`, permanent `48EE58E16325`, lines **38–51**, exact volume identity Equation **12.23.4**, source `non-kahler-pluripotential-theory-546D2583`, permanent `F24A79D3D80E`, lines **70–77**, density expansion Equation **12.23.5**, source `non-kahler-pluripotential-theory-1C89ABAB`, permanent `FE92C82454E6`, lines **79–83**, and Beta threshold Equation **12.23.6**, source `non-kahler-pluripotential-theory-836D3D8F`, permanent `85080CF9B131`, lines **86–95**.

**Hypotheses and derivation.** Choose integers `m>=2`, `p>=1`, `k>=1`, with `kp>m`, and the projective product and **single smooth-center blowup** of Proposition 12.23.1. Let `b_0>0` be the coefficient of the base Fubini–Study form, and choose its smooth fiber coefficient `q(s)=s^k` for small `s=|z|²`; outside that neighborhood it is smooth and strictly positive. Both backgrounds are smooth, semipositive, nonclosed and fixed as `epsilon` varies. Write `n=m+p`, `J_down(epsilon)=int(q+epsilon)^{-p}nu_down` and `J_up(epsilon)=int(q o pi+epsilon)^{-p}nu_up`, with the probability forms of the printed construction.

The *exact* cumulative volume formulas printed as (12.23.2) are

```text
Xi_down(s) = (s/(1+s))^m,
Xi_up(s)   = (((1+2s)/(1+s))^m - 1)/(2^m-1).
```

Consequently, in the limit `s->0`,

```text
dXi_down = [m s^(m-1) + O(s^m)] ds,
dXi_up   = [m/(2^m-1) + O(s)] ds.
```

For `d>0` and `kp>d`, direct substitution `s=epsilon^(1/k)t^(1/k)` gives

```text
int_0^s0 s^(d-1)/(s^k+epsilon)^p ds
  ~ (1/k) Beta(d/k, p-d/k) epsilon^(d/k-p).
```

To justify the asymptotic, first restrict to a fixed small `s0` where `q=s^k`; the Taylor-density remainder is bounded by `Cs` relative to the leading positive term and gives a lower-order contribution by splitting at a still smaller radius. Outside this neighborhood the integrand remains uniformly bounded. As `kp>m>=2`, the condition also implies `kp>1`; hence both divergent terms are covered. We obtain

```text
J_down ~ (m/k) Beta(m/k,p-m/k) epsilon^(m/k-p),
J_up   ~ m/[k(2^m-1)] Beta(1/k,p-1/k) epsilon^(1/k-p).
```

The two exact numerators in (12.23.4) are `binom(n,m)(b_0+epsilon)^m` and `binom(n,m)((b_0+2epsilon)^m-epsilon^m)`; both converge to `binom(n,m)b_0^m>0`. Dividing the exact formulas proves the sharpened positive finite ratio:

```text
V_up(epsilon)/V_down(epsilon)
 ~ (2^m-1) * Beta(m/k,p-m/k) / Beta(1/k,p-1/k)
     * epsilon^((m-1)/k).                                (*)
```

Thus the two common orders are exactly `p-m/k>0` and `p-1/k>0`, with **jump `(m-1)/k`**. Given *any positive rational* `r=a/b` (integers `a,b>=1`), choose

```text
m=a+1,  k=b,  p any integer strictly larger than (a+1)/b.
```

Then the common order rises by **exactly `a/b`** under a single blowup, *while both endpoint orders are strictly positive*. In particular, arbitrary small positive rational increases are possible: take `m=2` and `k` large, then `p=1` once `k>2`. Rational jumps of arbitrary size are possible as `m` varies. The printed proposition already realizes all positive integer increases; the rational spectrum and the exact ratio constant in (*) are the additional results.

**Proposed change, not performed:** optional corollary directly following 12.23.1, preserving its original integer claim, source attribution and tags. **Affected dependents:** comparisons of nef-boundary degeneration under modification (§12.22.5) and the fixed-cone preservation criteria (§§12.25–12.26). The smooth Monge–Ampère existence/identification in Theorem 14.2.1 and Gauduchon quotient equality in Theorem 12.2.3 remain *conditional upstream inputs*, not independently certified.

## POME-GAUD-CONE-DOUBLE-SCALE-001

**Status:** verified conditional deduction; **severity:** low. The printed constant-rank and maximum-rank criteria are **correct**. This gives an exact, dimension-independent warning about interchanging two limits, not an error in the fixed-background order formula.

**Integrated source:** `docs/sections/a-gauduchon-variational-volume--orders-of-degeneration-at-the-nef-boundary--a-maximum-rank-comparison-criterion/index.html`, blob `ccce6cecc0a14fcf89c2c385e7d8f87ff10df2c8`. Proposition **12.26.1** source `non-kahler-pluripotential-theory-841CBE9E`, permanent `94DF4FEA70D3`, lines **10–32**; Corollary **12.26.2** source `non-kahler-pluripotential-theory-091774C0`, permanent `87EBA7661A8A`, lines **36–56**; compare the closed nef volume formula explicitly used in the proof, lines **25–31**. The constant-rank precursor is Lemma **12.25.1**, source `non-kahler-pluripotential-theory-5E026F83`, permanent `DAA29135206D`, `docs/sections/a-gauduchon-variational-volume--orders-of-degeneration-at-the-nef-boundary--integer-orders-in-fixed-projective-cones/index.html` blob `82790640609d3d58b131873295a827e8d7869d85`, lines **10–58**.

**Exact calculation.** Let `q>=1`, `X=P^1 x P^q`, and let `B_1` and `B_2` be the pullback normalized Fubini–Study forms. Put `n=q+1`, `Omega=B_1+B_2` (Kähler), and for `t>=0` let `theta_t=t B_1+B_2`. These are smooth closed semipositive forms and `theta_t->theta_0` in every fixed `C^k` as `t->0`. Using the printed *closed nef* variational-volume/intersection identity, which is independent of the positive smooth probability form `mu`, and `B_1^2=B_2^(q+1)=0`, `int_X B_1 wedge B_2^q=1`, one computes **exactly**

```text
V_mu(theta_t + epsilon Omega)
    = integral_X ((t+epsilon)B_1+(1+epsilon)B_2)^n
    = n (t+epsilon)(1+epsilon)^q.                        (**)
```

For each *fixed* `t>0` the order is **0**, since the limit of (**) as `epsilon->0` is `nt>0`. At `t=0` the order is **1**, since (**) is `n epsilon(1+epsilon)^q`. Therefore the fixed-background degeneration order is not continuous under smooth convergence of semipositive backgrounds, even in this projective closed family.

More sharply, if `t=t(epsilon)=epsilon^s` with *any real* `s>0`, then

```text
lim_{epsilon->0} log V_mu(theta_(epsilon^s)+epsilon Omega)/log epsilon
  = min{s,1}.
```

The order for this **moving** family is a crossover exponent; it is **not** a new fixed-background order. Every positive `s<1` realizes an intermediate double-limit slope, whereas all fixed `t>0` have order 0. This quantifies why the fixed-background constants in §§12.25–12.26 cannot be presumed uniform as a positive coefficient tends to zero. The statement of Corollary 12.26.2 about invariance of each *fixed* order under Kähler modifications remains untouched. In particular the exact moving-family equality (**) is **not** asserted for an arbitrary Hermitian perturbation upstairs.

**Proposed change, not performed:** optional short example after Corollary 12.26.2, emphasizing the order of the `t` and `epsilon` limits. **Affected dependents:** any uniform family comparison, variable-background asymptotic, or continuity of degeneration exponents inferred from rank-stratified cones. No regularization or limit interchange was used in the proof.

## Additional selected proof inspections (not new findings)

- **§12.21**, source `docs/sections/a-gauduchon-variational-volume--orders-of-degeneration-at-the-nef-boundary--elliptic-surface-volumes-and-order-spectra/index.html`, blob `0218ee5a373d19c4b293d9d492ba3b1fdffdef6a`: read Proposition 12.21.1 (tag `DE2BA13B1A92`, lines 25–50) and its harmonic-mean Schur determinant, and selected exponent calculations of Propositions 12.21.4/.5, tags `58574FAEC5B7`, `41097C9AFBD2`, lines 54–143; checked positivity of `(c+|r|²)/g` and its mean equation. No new invalid step demonstrated.
- **§12.22**, blob `2752af2181f07f54695112f0007173b9e4dad128`: inspected Lemma 12.22.1 (tag `0A017BFF9468`, lines 13–28), Hermitian Gauduchon test comparison Lemma 12.22.3 (tag `51797AE0DE1F`, lines 32–51), and Proposition 12.22.5 (tag `8AB4DFD2719F`, lines 55–108), including the rank defect of exceptional pullbacks and continuous cofactor determinant at semidefinite matrices. The factorization invoking **Hironaka** is a permitted stated input; not independently established.
- **§12.25**, blob `82790640609d3d58b131873295a827e8d7869d85`: inspected Lemma 12.25.1 (tag `DAA29135206D`, lines 10–58), the projective incidence/exceptional divisor model and Theorem 12.25.8 (tag `3F58257FA940`, lines 63–128), plus the selected modification and divisor passages (Prop. 12.25.11, tag `57BC641DA62E`, lines 145–173; Lemma 12.25.13, tag `5DAA9B186CEE`, lines 187–202; Theorem 12.25.14 tag `F79036F002E1`, lines 206–232). Positive comparison from a singular logarithmic divisor potential is tested against smooth Gauduchon forms by distributional Stokes, not by smoothing excluded objects.
- **§12.26**, blob `ccce6cecc0a14fcf89c2c385e7d8f87ff10df2c8`: inspected Proposition 12.26.1, Corollary 12.26.2 and Example 12.26.3 (tag `698A2684C823`, lines 63–74); verified that maximal rank is attained on an open set and survives a degree-one modification generically, for *fixed* coefficients.

No false theorem, confirmed proof gap or full section certification is alleged. **Unresolved in this session:** independent PDE existence/uniqueness underlying §12.23, complete normalization of the §12.2 variational duality, full analytic Hironaka factorization (allowed quoted input), and all uninspected results of these sections and the remaining collection. No local scripts, full build, CI, formal proof, site publication, source/body/registry/permanent-tag changes, PR creation or merge.
