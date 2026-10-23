# Pome mathematical audit — 2026-10-23: exact Hopf-basic energy tails and independent Gauduchon crosschecks

**Reviewed current main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Starting audit branch head:** `47001d69d14580fe34a55faf5a6474defad9213c` (existing branch, not reset).
**Scope:** first selected proof-level inspection of the integrated §17.16 (the radial example in Proposition 17.16.30 and the Hopf fiber-integration formula in Proposition 17.16.16); independent selected-step inspections of §12.19 (the sharp one-variable periodic-profile argument in Proposition 12.19.20) and §12.20 (change-of-metric and log-order proof of Proposition 12.20.1). **No entire section is certified.** The 25 chapters and 747 current sections remain an inventory rather than a proof-review count.

## Finding POME-HOPF-BASIC-ENERGY-EXACT-TAIL-001

**Severity:** low. **Status:** verified conditional deduction; the underlying Pome theorems are not claimed false or incomplete.

**Primary integrated source and immutable anchors:** `docs/sections/perron-interpolation-and-the-geodesic-equation/index.html`, main blob `dc8dc381257360c94fe1c792499bb1ddf1bf5997`; Proposition 17.16.30, source `non-kahler-pluripotential-theory:A8DE6D81`, permanent tag `9355B610E2C3`, physical lines 560–596 (especially 580–593). Supporting Proposition 17.16.16, source `non-kahler-pluripotential-theory:0FE78EAA`, permanent `0290ABD0E348`, physical lines 292–323; fiber-integration Equation 17.16.18, source `non-kahler-pluripotential-theory:DD3FEF42`, permanent `6D09A14331E6`, lines 302–305. The exact `dd^c=i/(2π)∂\bar∂` convention and mass-one Fubini–Study normalization are retained.

### Statement: an exact distribution law, not merely an E² threshold

Let `n≥3`, `d=n−1`, `Y=ℙ^d` with `∫_Y κ^d=1`, and `o=[1:0:…:0]`. For `0<a<1` let
[
\psi=\log\frac{\sum_{j=1}^d|z_j|^2}{\sum_{j=0}^d|z_j|^2},
\qquad v_a=1-(1-\psi)^a.
]
Write `μ_a=MA_κ(v_a)` for its **non-pluripolar** Monge–Ampère probability measure. For every real `R≥0`, put `\tau_R=(1+R)^{1/a}`. Then the **exact**, not asymptotic, sublevel-mass formula is
[
\boxed{\displaystyle
\mu_a\{v_a<-R\}=
\left[e^{1-\tau_R}
+a(1-e^{1-\tau_R})\tau_R^{a-1}\right]^d.}
\tag{1}
]
Consequently, with `β=d(1−a)/a>0`,
[
\boxed{\lim_{R\to\infty}R^\beta\mu_a\{-v_a>R\}=a^d.}\tag{2}
]
For **every** `q>0` (not only `q=2`),
[
\boxed{\int_Y(-v_a)^q\,d\mu_a<\infty
\quad\Longleftrightarrow\quad
q<\beta
\quad\Longleftrightarrow\quad
a<\frac d{d+q}.}\tag{3}
]
At `q=β` the divergence is logarithmic. More precisely, `-v_a` belongs to the sharp weak Lebesgue space `L^{β,∞}(\mu_a)` but not to strong `L^β(\mu_a)`.

For the basic pullback to the Hopf manifold `X=H_n`, Proposition 17.16.16 gives exactly
[
\boxed{\operatorname{MA}^{\mathrm{ext}}_\omega(\pi^*v_a)
\{\pi^*v_a<-R\}=2n\,\mu_a\{v_a<-R\}.}\tag{4}
]
Therefore (2) and (3) hold for the pullback with tail coefficient `2na^d`. In the usual full-mass definition of the finite `q`-energy class, formula (3) characterizes this family's `\mathcal E^q` membership. This extends the printed `q=2` threshold; it does **not** assert a general equivalence between the nonclosed Hopf energy theories and all Kähler energy classes.

### Self-contained radial calculation

Use the same affine chart and symbols as the integrated proof:
[
s=\log|z'|^2,\quad L=\log(1+e^s),\quad
P=\frac{e^s}{1+e^s},\quad
T=1+L-s.
]
As `s` runs from `−∞` to `+∞`, `T` decreases strictly from `+∞` to `1`. Crucially, not just asymptotically,
[
\boxed{P=\exp(1-T).}\tag{5}
]
Indeed, `T−1=\log(1+e^s)−s=−\log P`.

The local radial potential of `κ+dd^cv_a` has derivative
[
A(s)=P+a(1-P)T^{a-1}>0.
]
The radial Stokes calculation, using the unit normalization `\int d^c\log|z'|^2=1` on linking spheres, gives
[
\int_{\{s<s_0\}}\operatorname{MA}_\kappa(v_a)
=A(s_0)^d-\lim_{s\to-\infty}A(s)^d=A(s_0)^d,
]
since `A(−∞)=0`; there is **no** extra Dirac mass at `o` in the non-pluripolar product. The level condition `v_a<-R` is `T>\tau_R`, equivalently `s<s_R` with `T(s_R)=\tau_R`. Substituting (5) into `A(s_R)^d` proves (1). The hypersurface at infinity has zero mass because the measure is smooth there; thus no boundary contribution is omitted.

As `R→∞`, the term `e^{1-\tau_R}` decays super-polynomially and `1-e^{1-\tau_R}→1`. Hence the bracket in (1) is asymptotic to `a\tau_R^{a-1}=a(1+R)^{-(1-a)/a}`, proving (2). Since `v_a≤0`, layer cake yields
[
\int(-v_a)^q d\mu_a=q\int_0^\infty R^{q-1}\mu_a\{-v_a>R\}\,dR.
]
The asymptotic tail is `a^dR^{-β}`, so the integral at infinity is comparable to `\int^\infty R^{q-β-1}dR`; it converges precisely for `q<β`, and at `q=β` diverges like `q a^d\log R`. This proves (3) and weak-`L^β` sharpness. Formula (4) follows from the precise fiber identity of Equation 17.16.18, with `F=1_{\{v_a<-R\}}`, using nonnegative Borel tests.

**Dependency boundary:** The local radial positivity and non-pluripolar full-mass property are proved in the selected integrated Proposition 17.16.30, and the fiber identity in 17.16.16. The complete Kähler `d_2` completion/CAT(0) theorem quoted earlier in §17.16 is already tracked under historical ID `POME-GEO-EXT-CAT-001`; it is NOT newly reclassified here. Neither that external input nor the excluded Demailly/Bergman/L²/OT programme is invoked to prove (1)–(3).

**Proposed optional manuscript correction:** Add a short corollary after Proposition 17.16.30 giving (1)–(3), preserving all existing source and permanent tags; optionally add its pullback version by Equation 17.16.18. No underlying statement must be weakened, and no source/body or canonicalization was edited. Dependents: energy examples in §17.16; basic Hopf `\mathcal B_2` and singularity-type comparisons, and possibly examples for general energy exponents. Do not infer additional metric-completion theorems for `q≠2`.

## Two independent selected proof checks, without a new finding ID

1. **Gauduchon logarithmic orders**, `docs/sections/a-gauduchon-variational-volume--orders-of-degeneration-at-the-nef-boundary/index.html`, blob `a7c145c5d1ceb0f1326bfb155f75dc9d854f14a0`, Proposition 12.20.1, source `non-kahler-pluripotential-theory:895EF015`, permanent `EBFCF76A5A51`, lines 19–70. The key comparison is `c_1h≤h'≤c_2h` with **strictly positive** constants. Because `\log\epsilon<0`, dividing the monotonicity inequalities reverses directions. Replacing `\epsilon` by a fixed multiple changes no lower or upper logarithmic orders; the bounded-error and scaling steps are consistent. This verifies **only those algebraic limiting steps** conditional on the stated monotonicity/homogeneity of `\mathcal V_\mu`, not the whole variational theory.

2. **Vanishing-lower-mass elliptic example**, `docs/sections/a-gauduchon-variational-volume--vanishing-lower-mass/index.html`, blob `c1477be8a0df1e32c391b51dae5b7e157df3ccfd`, Proposition 12.19.20, source `non-kahler-pluripotential-theory:73E21B50`, permanent `3290D6E85075`, lines 411–463. Inspected the **one-dimensional** necessary constraints `p=f'`, `|p|≤1`, `p'≥−1` and its sharp periodic profile. With `r=\max p−\min p≤2` and `L=4π`, the proof's polynomial `Lr²/4−r³/6` has derivative `r(L−r)/2>0` for `0<r≤2`, giving `\int_0^Lp²≤L−4/3` and mass `>8` for smooth profiles. Its piecewise-linear limiting profile has a positive upward derivative atom; convolution preserves the distributional lower derivative bound. This is a consistent **selected-step check**, not a full audit of the threefold construction, smooth complex Monge–Ampère solvability, or the source's other results. No old findings are repeated.

## Verification, status and exclusions

The exact identity (5), Stokes mass flux, tail formula and layer-cake threshold were checked algebraically as written; **no numerical script, project tests, full build, CI, website publication, or formal verification were performed**. This is a proof written at the audit level, with unverified upstream results explicitly bounded. Existing audit ledger and 747-row coverage matrix must preserve historic statuses, particularly Demailly approximation/regularization and its dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss programme as **`deferred-by-user`**. No re-opening or prerequisite backdoor inspection is authorized.
