# 2026-10-25 — exact Robin and fixed-ball capacities of real cubes

**Audit branch before this review:** `ce0d84a24630262859540f0d02f8f2586646f8bb`. **Integrated reading edition:** `main` at `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Scope:** new selected integrated proof review of §§16.37, 16.38, 16.41; selected source cross-check in §16.36. This is not whole-section certification.

## POME-CUBE-ROBIN-EXACT-001 — low / verified conditional deduction

The printed theorems are **not** contradicted. This optional sharpness corollary rests on the already printed Joukowski and polynomial product-extremal formulas. It supplies an exact normalization and a sharpness test for the **lower** inequality of Theorem 16.37.3, not a proposed replacement of that theorem.

**Precisely pinned source.** Proposition **16.36.1**, permanent tag `6BA3C254E28C`, source `klimek-pluripotential-theory-1EE8289D`, `docs/sections/the-real-cube-equilibrium-density/index.html` (main blob `712e936992d5ae12cca72b83b85561123e932b27`, physical lines **8–35**) uses the coordinate Joukowski transformation and the product-max extremal identity. The Robin capacity definitions and Theorem **16.37.3**, permanent tag `27353237EC80`, source `klimek-pluripotential-theory-DAE157DD`, appear in `docs/sections/robin-capacity-and-its-quantitative-comparison/index.html` (main blob `525f388094d0efb6b9ef9f8701d8ac459fd22814`, lines **8–15, 80–114**).

**Statement and hypotheses.** Let `n >= 1`, `r > 0`, and `K_r=[-r,r]^n` embedded as a totally real compact subset of `C^n`. Let
[
gamma(K_r)=limsup_{|z|	oinfty}(V_{K_r}^*(z)-log|z|),quad
c(K_r)=e^{-gamma(K_r)},quad
alpha(K_r)=exp(-sup_{|z|le1} V_{K_r}^*(z)).
]
Here `V` is the **logarithmic growth-one** extremal, and `alpha` is the *fixed unit-ball* capacity, not the relative Monge–Ampère capacity. Then exactly
[
oxed{sup_{|z|le R}V_{K_r}^*(z)=operatorname{arsinh}(R/r)quad(R>0),}
]
and consequently
[
oxed{gamma(K_r)=log(2/r),qquad c(K_r)=r/2,qquad
alpha(K_r)=e^{-operatorname{arsinh}(1/r)}
=rac{r}{1+sqrt{1+r^2}}.}
]
For `0<r<=1/sqrt(n)`, the cube lies inside the closed Euclidean unit ball, as required by Theorem 16.37.3, and
[
oxed{rac{c(K_r)}{alpha(K_r)}
=rac{1+sqrt{1+r^2}}2longrightarrow1quad(rdownarrow0).}
]
Hence the coefficient **1** in that theorem's lower bound `alpha(K)<=c(K)` is sharp even restricted to non-pluripolar totally real cubes. For the maximal inscribed such cube `r=1/sqrt(n)`, the exact values are `c=1/(2sqrt(n))` and `alpha=sqrt(n+1)-sqrt(n)`. This argument asserts nothing about the upper exponent `1/n`, treated separately in Proposition 16.37.8.

**Proof.** Write `J(zeta)=(zeta+zeta^{-1})/2`. For each `w`, choose a root `zeta` of `J(zeta)=w` with `|zeta|>=1`. By the one-variable formula already used in the proof of §16.36.1,
[
v(w):=V_{[-1,1]}^*(w)=log|zeta|.
]
With `rho=|zeta|>=1`, the reverse triangle inequality yields
[
|w|=	frac12|zeta+zeta^{-1}|ge	frac12(ho-ho^{-1}),
]
hence
[
v(w)lelogigl(|w|+sqrt{1+|w|^2}igr)
=operatorname{arsinh}|w|.
]
For `w=iR`, the chosen root has modulus `R+sqrt(1+R^2)`, so equality holds. Dilation and the printed product-max formula give
[
V_{K_r}^*(z)=max_{1le jle n}v(z_j/r).
]
Therefore `V_{K_r}^*(z)<=arsinh(|z|/r)` everywhere and equality is attained at `z=(iR,0,...,0)`. This proves the exact radial supremum. Sending `R` to infinity and using `arsinh(R/r)=log(2R/r)+o(1)` proves the Robin formula; taking `R=1` proves the fixed-ball formula. Division gives the sharpness limit.

**Independent normalization check against the equilibrium measure.** Dilation of the §16.36.1 arcsine density gives
[
dmu_{K_r}=2^{-n}prod_{j=1}^nrac{dx_j}{pisqrt{r^2-x_j^2}}
quad	ext{on }K_r,qquad
mu_{K_r}(mathbb C^n)=2^{-n}.
]
The elementary arcsine log moment is
[
int_{-r}^{r}log|x|,rac{dx}{pisqrt{r^2-x^2}}
=log(r/2),
]
which yields `int log|x_j| dmu_{K_r}=2^{-n}log c(K_r)` for each `j`. It crosschecks the same Robin normalization and does not conflate the real-cube density with ambient `2n`-dimensional Lebesgue measure.

**Proposed optional correction/placement.** A short corollary after Theorem 16.37.3 could state the three exact formulas and sharpness of its lower coefficient. No alteration to the theorem, source manuscript, tag, numbering or history is necessary. **Affected dependents:** capacity normalization tests and comparisons of fixed-ball `alpha` against Robin `c`; this does not upgrade or reprove any upper comparison or continuity input.

## Distinct selected proof review, without new confirmed errors

- **§16.37:** read the integrated bounded-projective-potential proof of Proposition 16.37.2 (lines 37–79), normalization and subharmonic compactness step of Theorem 16.37.3 (80–114), sphere-volume proof of Proposition 16.37.4 (116–143), the decreasing-compact proof of Theorem 16.37.5 (144–250), and the degree-d counterexample of Proposition 16.37.8 (252–290). No complete transitive check of the long Theorem 16.37.5 argument or its capacity-continuity/mixed-product premises; no new confirmed error.
- **§16.38:** read Theorem 16.38.1 (tag `DE0691E14C0E`, source `klimek-pluripotential-theory-F97596C6`, `docs/sections/geometric-polynomial-approximation-and-local-uniqueness/index.html`, blob `334d2453d12bdfeab3379fb0489bba3ddebf1ddb`, lines 11–68), including the Banach sequence space/Baire/open-neighborhood converse and local-determination hypotheses. Read Examples 16.38.2–3 (lines 68–114) as additional boundary checks. The invoked neighborhood Bernstein–Walsh criterion was not independently reconstructed.
- **§16.41:** read Proposition 16.41.1 (tag `1129B1616DEE`, source `klimek-pluripotential-theory-8E661DED`, `docs/sections/normalized-characterization-of-compact-extremals/index.html`, blob `fd5efa1edf755ed59b0c72f3dce7e28fdd1dc2aa`, lines 12–38), including the polar-deletion and local-domination uniqueness steps. Upstream domination and maximality are conditional inputs, not silently certified.
- **§16.36:** independently revisited the Joukowski degree-`2^n` transformation and equilibrium density, solely as baseline. The earlier **POME-CUBE-LORENTZ-ENDPOINT-001** was already registered in historical audit records: its `L^p`/Lorentz findings are **not newly claimed**, re-registered, or counted as this run's progress.

The 747-row ToC matrix is a coverage *inventory*. These four sections received only the indicated **selected proof-level** coverage, not whole-section certification. No script, local test, project build, CI, formalization, PR merge, website publication or main/source/tag/registry modification was performed. The dedicated Demailly approximation/regularization and Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme stays wholly **deferred-by-user**, neither solved nor reopened.
