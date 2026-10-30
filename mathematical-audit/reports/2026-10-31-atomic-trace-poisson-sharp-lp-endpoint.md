# Atomic trace Poisson equations: sharp (L^p) stability and failure at (p=1)

**Audit date:** 2026-10-31.  
**Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Finding:** `POME-TRACE-POISSON-LP1-SHARP-001`.  
**Severity/status:** **low / verified conditional deduction**. The printed theorem is **correct**; this is an independently justified stability strengthening and sharpness test of its stated (p>1) hypothesis, **not** a source error, a general theorem repair, or a certification of all dependencies.

## Exact integrated evidence and scope

- `docs/sections/restriction-and-intrinsic-trace-data/index.html`, pinned `main` blob `dbc3b722ceacb8232fe4c7b711e5ad98b0708f06`.
- Subsection **20.3.14**, source `non-kahler-pluripotential-theory:DFBA3531`, permanent tag `E07C398EC98F`, physical HTML lines **313–315**.
- **Theorem 20.3.15**, source `non-kahler-pluripotential-theory:46A3A7FE`, permanent tag `AFC6C3B6368C`, physical lines **318–353** (hypotheses and exact scalar at **319–327**, Poisson equation **334–345**, mass/uniqueness **347–353**).
- **Theorem 20.3.10**, source `non-kahler-pluripotential-theory:C5D10418`, permanent tag `879739B42EBB`, physical lines **226–272** (finite atomic trace and Green-kernel normalization **254–270**). This is a *used internal hypothesis*, not a newly certified upstream result.
- Neighboring **Proposition 20.3.13** (lines **290–309**) was read for the independent atomic-mass normalization, but its analytic approximation inputs remain unverified and **deferred-by-user**. Earlier `POME-TRACE-ATOMIC-INTERPOLATION-001` and `POME-TRACE-CURVE-NOWHERE-LOCALLY-COMPACT-001` concern different trace and metric questions; neither is repeated here.

## Statement of the new deduction

Let (Y) be a connected compact Riemann surface, let (eta) be a smooth real ((1,1))-form with (M=int_Yeta>0), and choose a smooth probability form (eta). Let (D) be a positive finite atomic measure on (Y) with total mass (dle M), in particular (D=D_u) from Theorem 20.3.10. Write
[
 dd^c w_D=D-deta,qquad
 dd^c s_* = Meta-eta,
]
where (w_D) is the Green representative and (s_*) is smooth. Fix the additive constants by zero (eta)-mean. Let (G(x,y)) be the Green kernel normalized to have zero (eta)-mean in (x); in a local coordinate at the diagonal it has singular part (log|z(x)-z(y)|^2), with the (dd^c)-convention of §20.3.10.

For (p>1) and nonnegative (fin L^p(eta)) with (int_Yf,eta=1), define
[
 H_f(x)=int_YG(x,y)(f(y)-1),eta(y),quad
 s_{d,f}=s_*+(M-d)H_f,quad v_{D,f}=w_D+s_{d,f}.
]
Then (s_{d,f}) is bounded and continuous, (v_{D,f}) has the **ordinary** singularity type of (w_D), and
[
 eta+dd^c v_{D,f}=D+(M-d)feta,qquad
 operatorname{MA}^{m ext}_eta(v_{D,f})=(M-d)feta.
]
For (M>d) this is the unique normalized solution of the type prescribed by Theorem 20.3.15. For every (p>1), with (p'=p/(p-1)), there is a finite, explicit Green-operator constant
[
 C_{Y,eta,p}:=sup_{xin Y}|G(x,cdot)|_{L^{p'}(eta)}<infty
]
such that for two probability densities (f,gin L^p(eta)),
[
 oxed{ |s_{d,f}-s_{d,g}|_infty
 le (M-d)C_{Y,eta,p}|f-g|_{L^p(eta)}. }
]
The bounded correction depends on (D) **only through its total mass** (d). More precisely, if (E) has total mass (ele M), then
[
 |s_{d,f}-s_{e,g}|_infty
 le C_{Y,eta,p}igl((M-d)|f-g|_p+|d-e||g-1|_pigr).
]
In particular, when (fequiv1), the bounded correction is exactly the same (s_*) for **all** atomic measures (D) of mass at most (M). The atomic *Green part* still depends on locations and is not claimed to vary uniformly.

**The exponent restriction (p>1) is sharp for a universal assertion of existence in this fixed ordinary singularity type.** Even for (D=0), (Y=mathbb P^1), and (eta=eta=omega_{m FS}) with (M=1), there is a nonnegative probability density (fin L^1(eta)) for which the equation
[
 omega_{m FS}+dd^c v=f,eta
]
has no **bounded** solution (v). Hence Theorem 20.3.15's existence assertion cannot simply be extended to arbitrary (L^1) densities while retaining the ordinary trace type.

Moreover, even among **smooth strictly positive probability densities** there are (f_epsilon	o1) in (L^1(eta)) for which their zero-mean smooth solutions fail to converge uniformly to the solution for (fequiv1). Thus the (L^p	o C^0) estimate has no unrestricted (L^1	o C^0) endpoint counterpart.

## Proof

### Exact affine Poisson representation

The compact-curve Green identity (dd^c_xG(x,y)=delta_y-eta(x)) and the zero total mass of ((f-1)eta) give
[
 dd^cH_f=(f-1)eta,qquad int_YH_f,eta=0.
]
Consequently,
[
 egin{aligned}
 dd^c s_{d,f}
 &= Meta-eta+(M-d)(f-1)eta\
 &= deta+(M-d)feta-eta.
 end{aligned}
]
Adding (dd^c w_D=D-deta) proves the exact current identity. For (p>1), the Green potential is continuous (shown below), hence bounded. Thus (v_{D,f}-w_D) is bounded; the polar part of its curvature measure is exactly (D), since the other measure is absolutely continuous. This proves the extended-measure identity, including when (D) has countably many atoms. Harmonic functions on a connected compact curve are constant, proving normalized uniqueness. For (d=M) the density term is zero and (s_{d,f}=s_*), consistently with the zero-extended-mass clause of the printed theorem.

### Uniform Green bound for (p>1)

Choose finitely many conformal charts and a common radius below the injectivity radius. On their diagonal neighborhoods the Green kernel equals (log|z(x)-z(y)|^2) plus a uniformly bounded smooth term. Every finite (q) satisfies
[
 int_0^{r_0}|log r|^q r,dr <infty.
]
Outside these neighborhoods the kernel is smooth and uniformly bounded. Therefore (sup_x|G(x,cdot)|_{L^q(eta)}<infty) for every finite (q), in particular (q=p'). Hölder's inequality immediately gives the boxed estimate. The same chart decomposition, splitting a small diagonal neighborhood from its smooth complement, shows (G(x_j,cdot)	o G(x,cdot)) in (L^q(eta)) when (x_j	o x). Thus (H_f) is continuous. The two-parameter estimate follows from the exact identity
[
 s_{d,f}-s_{e,g}=(M-d)(H_f-H_g)+(e-d)H_g.
]
No elliptic bootstrap, multiplier-ideal approximation, Bergman kernel, (L^2) extension theorem, or regularization input is used.

### A fixed (L^1) density forbids bounded solutions

Take (Y=mathbb P^1), (eta=eta=omega_{m FS}), (D=0), (M=1), and a coordinate (z) centered at (o). Fix a smooth cutoff (chige0), supported in (|z|<e^{-2}) and equal to one near (o), and put
[
 f(z)=rac{c,chi(z)}
 {|z|^2(log(1/|z|))^2}
]
there, with (c>0) chosen so that (int_Y f,eta=1); let (f=0) outside the chart. The density is nonnegative and (L^1), because in polar coordinates its mass near the origin is comparable to
[
 int_0^{r_0}rac{dr}{r(log(1/r))^2}<infty.
]
But the value at (o) of its normalized Green potential diverges to (-infty):
[
 int_YG(o,y)f(y)eta(y)
  lesssim -int_0^{r_0}rac{dr}{rlog(1/r)}
 =-infty.
]
The smooth (-eta) term in the Poisson datum only adds a bounded potential. Thus the distributional solution of (dd^cv=(f-1)eta), unique up to a constant, is unbounded below. Every potential ordinarily equivalent to (w_D=0) is bounded, so no such solution has the required ordinary type. This is an explicit **failure of the proposed (p=1) extension**, not a counterexample to the printed (p>1) theorem. Note that (feta) has **no atoms**; vanishing point Lelong numbers do not fix the ordinary type.

### Smooth (L^1) convergence does not imply uniform convergence

In the same (D=0) model, let (b_epsilonge0) be a smooth probability bump supported in (|z|<epsilon), obtained by rescaling one fixed smooth radial bump in the coordinate chart and normalizing against (eta). Set (delta_epsilon=1/|logepsilon|), for (epsilon<e^{-2}), and
[
 f_epsilon=(1-delta_epsilon)cdot1+delta_epsilon b_epsilon.
]
Every (f_epsilon) is smooth, strictly positive, and has integral one, while (|f_epsilon-1|_{L^1(eta)}le2delta_epsilon	o0). Let (v_epsilon) be the zero-mean smooth solution of (dd^cv_epsilon=(f_epsilon-1)eta) and (v_0=0). Near (o), (G(o,z)=log|z|^2+O(1)), and the rescaled bump has
[
 int_Y G(o,y)b_epsilon(y)eta(y)=2logepsilon+O(1).
]
The normalization of (G) gives (int_YG(o,y)eta(y)=0) after choosing its symmetric zero-mean representative (or only an (O(1)) term with another fixed normalization). Hence
[
 v_epsilon(o)=delta_epsilon(2logepsilon+O(1))
 longrightarrow -2
]
in the stated (dd^c) convention, whereas (v_0(o)=0). In particular (|v_epsilon-v_0|_infty
ot	o0). This counterexample uses **only smooth strictly positive data** at every finite level and is independent of any approximating multiplier ideals.

## Mathematical assessment, dependencies and proposed action

- **Printed conclusion:** Theorem 20.3.15 is correct under its stated (p>1) assumption. The new result proves a quantitative (L^p) dependence and shows why the restriction cannot be dropped in a universal claim about solutions in a prescribed *ordinary* trace type. It does **not** claim a false theorem, an unproved original proof step, or that all (L^1) densities fail.
- **Internal inputs actually used:** compact Green kernel/atomic trace in Theorem 20.3.10 and the elementary compact-curve Poisson uniqueness and logarithmic singularity. These are used **conditionally** as established in the reading edition, not independently certified here.
- **Proposed source correction:** none required. An **optional** self-contained remark after Theorem 20.3.15 may record the boxed estimate and the fixed (L^1) counterexample, with the precise ordinary-type qualifier.
- **Affected readings:** subsequent use of atomic trace Poisson solutions in §20.3 and §24.9 must not infer (L^1)-uniform stability or unrestricted (L^1) existence. There is no change to the source labels, permanent tags, or canonicalization.
- **Precise newly checked coverage:** the hypotheses, scalar mass normalization, Poisson construction, and uniqueness at §20.3.15, plus §20.3.10's Green and atomic-mass conventions. §20.3.13 was context only. The broader §20.3, all of Chapter 20, and all analytic upstream dependencies remain **uncertified**. The current matrix remains **25 chapters, 747 numbered ToC sections, zero fully mathematically certified sections**.
- **Excluded scope:** Demailly approximation/regularization and its dedicated Bergman, (L^2), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remain **deferred-by-user**, neither revisited nor marked resolved.
- **Verification boundary:** manual exact Green-kernel and radial-integral proof only. No project build, tests, CI, formal proof, or site publication. No changes proposed to `main`, reading bodies, original sources, registries or tags.
