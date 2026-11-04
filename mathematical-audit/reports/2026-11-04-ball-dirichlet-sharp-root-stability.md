# Exact sharp constants and density exponent for ball Dirichlet stability

**Date:** 2026-11-04. **Finding:** `POME-BT-BALL-DIRICHLET-SHARP-ROOT-STABILITY-001`. **Classification:** low / **verified conditional deduction**. **Original theorem:** correct; no confirmed false theorem or proof gap.

## Pinned current reading-edition target

- Reviewed production `main`: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- Integrated path: `docs/sections/bedford-taylor-products-and-local-capacity--the-ball-dirichlet-problem-with-continuous-density/index.html`; blob `ff1d5dfff1913156b45875eabf921f60af553b99` on that main.
- Actual ToC: **§7.9, The ball Dirichlet problem with continuous density**, permanent section tag `0897D387268D`; source collection `foundations-of-pluripotential-theory`.
- Lemma **7.9.1**, source `foundations-of-pluripotential-theory:89405657`, permanent tag `0FF4AFFE0ED0`, physical HTML lines **17–35**: density-root linearity and maxima.
- Theorem **7.9.2**, source `foundations-of-pluripotential-theory:69935D4D`, permanent tag `A092925717E1`, lines **41–50**: existence, uniqueness, envelope and stability on arbitrary balls.
- Equation **7.9.3**, source `foundations-of-pluripotential-theory:0390D064`, permanent tag `B8751A529320`, lines **46–48**. Normalization under the affine ball map: lines **58–61**. Actual proof of the stability inequality and passage to continuous data: lines **130–154**.
- Contextual dependent: `docs/sections/bedford-taylor-products-and-local-capacity--bounded-measurable-densities/index.html`, main blob `762b841b0cb243784dc988f04dbf2779da66c469`: §7.10 explicitly extends estimate (7.9.3) to bounded measurable densities. Its distinct `L^1` convergence argument is **not** inferred from this supremum-norm estimate.

## Hypotheses and complete direct calculation

Fix any complex dimension `n >= 1`, `a in C^n`, `R>0`, and the ball `B=B(a,R)`. Use the **printed** normalization `eta=dd^c|z|^2`, so that `dd^c|z-a|^2=eta`. For arbitrary real parameters `s>=t>=0` and `d>=0`, choose the smooth constant data
`f=s^n, g=t^n, varphi=-d, chi=0`. Let
`Q(z)=|z-a|^2-R^2`. Then `Q=0` on the boundary, `-R^2<=Q<0` in the ball, and
`dd^c(sQ-d)=s eta`, `dd^c(tQ)=t eta`. Hence, **by direct wedge multiplication**,
`(dd^c(sQ-d))^n=s^n eta^n`, `(dd^c(tQ))^n=t^n eta^n`, with the required boundary data. Both are smooth plurisubharmonic solutions even when `s=0` or `t=0`. Their identification with `H_{f,varphi}` and `H_{g,chi}` uses only the uniqueness stated in Theorem 7.9.2, or the standard comparison principle under the stated hypotheses. Therefore
`
H_{s^n,-d}(z)=sQ(z)-d,   H_{t^n,0}(z)=tQ(z).
`
Their difference equals `(s-t)Q(z)-d`, is nonpositive, and its negative is maximized at `z=a`. Consequently the **exact equality**, for every `s>=t>=0` and `d>=0`, is
`
||H_{s^n,-d}-H_{t^n,0}||_{L^infty(B)}
  = d+R^2(s-t)
  = ||varphi-chi||_{L^infty(partial B)}
    +R^2||f^(1/n)-g^(1/n)||_{L^infty(B)}.
`
Thus the boundary coefficient `1` and density coefficient `R^2` in the **correct printed inequality (7.9.3)** are simultaneously attained with both terms strictly positive (choose `s>t` and `d>0`). Neither coefficient can be decreased even if the other is kept unchanged. This is exact, not an asymptotic model, and works in every dimension including the zero-density endpoint.

The elementary inequality `|x^(1/n)-y^(1/n)|<=|x-y|^(1/n)` for nonnegative `x,y` follows from subadditivity of the concave power `r=1/n`: for `x>=y`, `x^r=(y+(x-y))^r<=y^r+(x-y)^r`. Therefore (7.9.3) yields, without any extra analytic assumptions,
`
||H_{f,varphi}-H_{g,chi}||_infty
  <= ||varphi-chi||_infty + R^2 ||f-g||_infty^(1/n).
`
This **density exponent `1/n` is globally optimal** with no positive lower bound on `f,g`. Indeed, take `d=0, t=0, f=epsilon>0, g=0`, and `s=epsilon^(1/n)`. The exact left side equals `R^2 epsilon^(1/n)`; dividing by `epsilon^alpha` tends to infinity as `epsilon -> 0+` for every `alpha>1/n`. Thus no universal finite `C` (even depending on the fixed `n,R`) can give an exponent `alpha>1/n` over all such bounded smooth constant data. For `n=1`, the sharp endpoint is Lipschitz `alpha=1`; for `n>=2`, the singular zero-density endpoint prevents any higher uniform Hölder exponent. Away from zero, the constant-density model has derivative `(1/n)f^{1/n-1}Q(z)`, explaining the degeneration as `f downarrow 0`.

## Scope, dependencies, proposed correction

**Status: verified conditional deduction**, **severity: low**. The original Theorem 7.9.2, its proof and Equation 7.9.3 are **not refuted**. The elementary model computation is complete; identification with the notation `H` assumes the existing comparison/uniqueness result as indicated. No claim is made that the full nonlinear Bedford–Taylor existence proof, all upstream weak-convergence lemmas or the §7.10 bounded-density approximation proof was independently certified. The cited §7.10 estimates inherit the same unavoidable exponent boundary in the class containing smooth constant data; they do **not** imply an `L^1` stability rate of this type.

**Suggested addition only (not a body edit):** immediately after Equation 7.9.3, note that equality holds for constant densities and constant boundary data as above; the density `L^infty` Hölder exponent `1/n` is sharp at zero density. Keep all existing permanent tags, source attributions, versions and conventions untouched.

**Actual new coverage:** exact model, coefficient and exponent boundary check of §7.9.1–2 / Equation 7.9.3, and statement-level crosscheck of the already partly visited §7.10. It is **not** a whole-section certification, a new complete existence theorem, or a revisiting of user-excluded regularization/Bergman/weighted-L²/OT work. Existing confirmed errors, proof gaps, proposed repairs and **deferred-by-user** exclusions are unchanged. Current actual ToC is 25 chapters / 747 numbered sections / zero complete mathematical-section certifications. No build, project tests, CI, formal verification or website publication was run.
