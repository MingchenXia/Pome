# Separable real Monge–Ampère measures: all coordinate strata and a mixed permanent formula

**Date:** 2026-11-10. **Stable finding:** `POME-CONVEX-MA-SEPARABLE-STRATA-PERM-001`. **Severity:** low. **Status:** verified conditional deduction; **no printed theorem is shown false**. **Production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Branch:** `review/mathematical-audit`.

## Integrated mathematical statement and anchors

Directly checked `docs/sections/convex-analysis-and-toric-potentials--the-real-monge-ampere-measure/index.html` (Git blob `7089aa41ae2422b1bd6b5094e46668cbc8ed37be`), particularly Theorem 21.5.1, source `foundations-of-pluripotential-theory:4A0FAEB3`, permanent `409656CC47D4`, physical lines 10–38 (subgradient-volume and dual-gradient pushforward); Theorem 21.5.2, source `foundations-of-pluripotential-theory:6403CF44`, permanent `F4072D9ED060`, lines 43–85 (local-uniform to vague continuity); Proposition 21.5.4, source `foundations-of-pluripotential-theory:EAD83A50`, permanent `5D8A7A7D734E`, lines 98–156 (C¹,¹ density and mixed measure); polarization equation 21.5.5, source `foundations-of-pluripotential-theory:24CC29A7`, permanent `D38381F0AC43`, lines 141–156. We use the **printed** convention `MA_R(F)=n! vol(∂F(·))`, not an unnormalized determinant. All assertions below are on `N_R=R^n` in a lattice basis, `n>=1`.

## Exact statement (new special-case deduction)

For each `j=1,...,n`, let `a_{ji},b_{ji}>=0` and set

```text
F_j(x_1,...,x_n) = sum_{i=1}^n [ a_{ji}|x_i| + (b_{ji}/2)x_i^2 ].
mu_{ji} = b_{ji} dx_i + 2 a_{ji} delta_0(dx_i).
```

Each `F_j` is finite convex. In **every** nonnegative parameter range (including zero coefficients), its polarized real Alexandrov measure is the following sum of product Radon measures:

```text
MA_R(F_1,...,F_n) = sum_{sigma in S_n} tensor_{i=1}^n mu_{sigma(i),i}.          (A)
```

Thus for every `R>0`, the exact cube mass is

```text
MA_R(F_1,...,F_n)([-R,R]^n)
   = per [ 2 b_{ji} R + 2 a_{ji} ]_{j,i=1}^n.                              (B)
```

Here `per` is the **unsigned permanent**, without an additional `n!` factor. In particular, if all `F_j=F=sum_i[a_i|x_i|+b_i x_i²/2]`, then

```text
MA_R(F) = n!  tensor_{i=1}^n (b_i dx_i + 2a_i delta_0(dx_i))
        = n! sum_{S subset {1,...,n}}
            (prod_{i in S} 2a_i)(prod_{i not in S} b_i)
            [ tensor_{i in S} delta_0(dx_i) tensor_{i not in S} dx_i ]. (C)
```

This exhibits a **separate positive component on every coordinate stratum**, of codimension `|S|` when `a_i,b_i>0`. The absolutely continuous formula of Proposition 21.5.4 is not applicable to these nonsmooth corner potentials; retaining only the a.e. Hessian determinant would lose all singular components.

## Proof

**Step 1: one-dimensional inverse subgradient.** For `h(s)=a|s|+(b/2)s²` with `b>0`, the subgradient is `bs-a` for `s<0`, `[-a,a]` at zero, and `bs+a` for `s>0`. A slope `p` has the unique inverse base point

```text
T(p)=(p+a)/b if p < -a;   T(p)=0 if |p|<=a;
T(p)=(p-a)/b if p > a.
```

Therefore `T_*dp = b ds + 2a delta_0`, as can be tested on arbitrary bounded Borel functions: change variables separately on the two outside rays and integrate the middle interval of length `2a`. At `a=0` the central atom vanishes; the formula remains valid. For `b=0`, replace `b` by `b+epsilon` and use local uniform convergence in the printed Theorem 21.5.2. (Alternatively, the conjugate has slope domain `[-a,a]` and all interior slopes map to zero.)

**Step 2: tensorization.** For `F=sum_i h_i(x_i)`, Fenchel conjugation separates coordinates: `F^*(p)=sum_i h_i^*(p_i)`. For all `b_i>0`, the dual-gradient inverse map is `T=(T_1,...,T_n)`. The dual-gradient formula in Theorem 21.5.1 and Fubini's theorem give

```text
MA_R(F) = n! T_*(dp_1 ... dp_n)
        = n! tensor_i (b_i dx_i + 2a_i delta_0(dx_i)).
```

No unproved interchange of limits is needed here. Allowing `b_i=0` follows from local uniform convergence of `F_epsilon` and vague continuity; the displayed product measures themselves also converge vaguely on each compactly supported test function.

**Step 3: polarization.** For nonnegative scalars `t_j`, the preceding diagonal formula applied to `F(t)=sum_j t_jF_j` reads

```text
MA_R(F(t)) = n! tensor_i (sum_j t_j mu_{ji}).
```

The coefficient of `t_1...t_n` on the right is `n! sum_{sigma in S_n} tensor_i mu_{sigma(i),i}`. By symmetry and multi-additivity of the mixed measure in Proposition 21.5.4, the coefficient of the same monomial on the left is `n! MA_R(F_1,...,F_n)`. Cancellation gives (A). This coefficient argument can equally be justified by applying printed polarization identity 21.5.5 directly, so it does not require differentiating measure-valued functions. Positivity of all terms is manifest.

**Step 4: exact normalization tests.** The one-dimensional measure of `[-R,R]` is `2b_{ji}R+2a_{ji}`; evaluating (A) on a product cube proves (B). For `n=2`, `F=|x_1|+|x_2|+(x_1²+x_2²)/2` gives precisely

```text
MA_R(F) = 2 dx_1 dx_2
  + 4 delta_0(dx_1) dx_2 + 4 dx_1 delta_0(dx_2)
  + 8 delta_(0,0).
MA_R(F)([-R,R]^2) = 2(2R+2)^2.
```

For `a_i=0` for all `i`, (C) reduces to the smooth value `n!prod_i b_i dx`. For `b_i=0` for all `i`, only the single full-corner atom survives with mass `n!prod_i(2a_i)`, recovering the subgradient-box volume. In contrast, the earlier `POME-TORIC-MIXED-ESCAPE-001` uses one-sided coordinate hinges and translation to infinity to test *failure of narrow convergence*. The present result is a **fixed-location, all-codimension stratification plus arbitrary mixed-permanent formula**, not that previous escape result.

## Classification and implications

**Verdict:** Theorems 21.5.1–2, Proposition 21.5.4 and Eq. 21.5.5 pass these **selected normalization and polarization tests**; no error or missing hypothesis in their printed statements is established by this example. We used their general continuity/polarization mechanisms as **uncertified internal inputs**, so the verdict is **verified conditional deduction**, **not** a verified repair or complete theorem-chain certificate. The formula is independent of Demailly approximation, Bergman estimates, weighted L², Ohsawa–Takegoshi, multiscale atlases and positivity-loss work (all deferred-by-user).

**Proposed optional addition:** Add a separable-coordinate example or remark after Proposition 21.5.4, explicitly warning that the almost-everywhere Hessian determinant does not represent Alexandrov mass at nonsmooth creases. Potential dependents for checking, **not independently certified here:** §21.6's full-mass/tightness discussion and the real-toric mixed-measure normalization used in §§21.12–21.13. No source-body, canonicalization, reference, tag or publication changes were authorized or made.

**Coverage:** only the above particular formulas and line ranges were inspected; §21.5 had earlier selective audits. **Zero newly first-visited numbered sections and zero complete-section certifications** in this report. Current ToC baseline: 25 chapters / 747 numbered sections; earlier classified findings and user-deferred programme remain unchanged.
