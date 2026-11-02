# Critical Frostman heat smoothing, almost-everywhere decay, and sharp quantifier limits (2026-11-03)

**Stable finding ID:** `POME-HEAT-FROSTMAN-CRITICAL-QUANTIFIERS-001`  
**Status:** verified conditional deduction (**not** a false printed lemma, not a proof repair).  
**Severity:** low (useful sharpness and strengthening of the endpoint quantifiers).  
**Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Section:** 3.10, *Heat kernels on compact manifolds*; source section `transcendental-positive-cones:FD9C3E46`, permanent section tag `B8A97FFD89FE`.  
**Integrated reading edition:** `docs/sections/heat-kernels-on-compact-manifolds/index.html`, blob `c59a1b3fab9433f1aae95db99adb4821857b5d8d`.  
**Inputs and physical HTML anchors:** Lemma 3.10.1, source `transcendental-positive-cones:327DDB8B`, permanent `126365F8EBD6`, lines 10–13 (Gaussian bound) and selected proof lines 20–79 (Nash/Davies derivation); Lemma 3.10.5, source `transcendental-positive-cones:DD00B1CA`, permanent `56A174D59425`, lines 83–105 (critical ball-growth estimate and fixed-`L^1` test convergence).

## 1. Scope of the direct mathematical check

The actual integrated Lemma 3.10.1 asserts the scalar Gaussian estimate on a compact Riemannian manifold of real dimension `m`:
```math
0\le h_t(x,y)\le C t^{-m/2}\exp[-d(x,y)^2/(Ct)],\qquad 0<t\le1.
```
Its displayed proof uses the compact Nash inequality (equation 3.10.2, lines 22–29), Davies' conjugated semigroup and the differential inequality (3.10.3) (lines 31–44), dyadic `L^p` iteration (lines 46–70), and optimization of a Lipschitz gauge `\psi(z)=d(z,y)` (lines 73–79). The exponent and parameter direction are consistent with a Gaussian upper bound. We **use this printed upper estimate as an upstream input**; the preceding elliptic construction and complete general compact-manifold proof are not transitively certified here.

The printed Lemma 3.10.5 assumes a finite positive measure `\rho` with `\rho(B_r(x))\le A r^{m-2}` for `m\ge2`, and concludes `\|h_t\rho\|_\infty\le C(A+\rho(X))/t` and `t\int(h_t\rho)F\,dV\to0` for each **fixed** nonnegative `F\in L^1(dV)`. Its annular proof and its truncation of that fixed `F` (lines 98–105) are correctly quantified. The following extensions are additional elementary consequences, not contradictions of the printed statements.

## 2. Full range of Frostman exponents

**Claim A (verified conditional on the Gaussian bound).** Let `(X,g)` be a compact smooth Riemannian `m`-manifold, `m\ge2`, and let `\rho` be a finite positive measure. Suppose for fixed `0\le s\le m`, `r_0>0`, and `A\ge0`,
```math
\rho(B_r(x))\le A r^{m-s}\quad\text{for all }x\in X,\ 0<r\le r_0.
```
Then
```math
\boxed{\|h_t\rho\|_{L^\infty(X)}\le C_{g,r_0,s}(A+\rho(X))t^{-s/2}},\qquad 0<t\le1.
```
In particular, `t\|h_t\rho\|_\infty=O(t^{1-s/2})\to0` for `s<2`.

**Proof.** For `t<r_0^2`, partition `X` into `B_{\sqrt t}(x)`, annuli `B_{2^{j+1}\sqrt t}(x)\setminus B_{2^j\sqrt t}(x)` while their outer radius is at most `r_0`, and the residual outer set. The `j`th contribution is at most
```math
C t^{-m/2} A(2^{j+1}\sqrt t)^{m-s}\exp(-4^j/C)
=CA t^{-s/2}2^{(j+1)(m-s)}\exp(-4^j/C).
```
The `j=0` inner ball has the same order. The series converges for every fixed `s`. Outside radius `r_0/2` (adjusting the final annulus) the estimate is `C\rho(X)t^{-m/2}\exp(-c r_0^2/t)\le C_{r_0,s}\rho(X)t^{-s/2}`. For `t\ge c r_0^2`, compact-time boundedness of the smooth kernel gives the result after enlarging the constant. No sequential limit or interchange of integrations is used. \(\square\)

## 3. An almost-everywhere strengthening requiring no Frostman assumption

**Claim B (verified conditional on the Gaussian bound).** For **any** finite positive Borel measure `\rho` on a compact `m\ge2` dimensional Riemannian manifold,
```math
\boxed{\lim_{t\downarrow0}t(h_t\rho)(x)=0\quad\text{for }dV\text{-almost every }x.}
```
This is a full `t\downarrow0` limit, not merely a dyadic subsequence.

**Self-contained proof from the kernel bound.** Put `t_k=2^{-k}`. For `t_{k+1}<t\le t_k`, the Gaussian inequality and `m\ge2` imply
```math
0\le t(h_t\rho)(x)\le B_k(x)
:=C t_k^{1-m/2}\int_X\exp[-d(x,y)^2/(C t_k)]\,d\rho(y).
```
(The constant absorbs the factor `2^{m/2-1}` in the dyadic comparison.) Uniform Riemannian Gaussian-volume integration gives
```math
\int_X B_k(x)\,dV(x)\le C t_k\rho(X).
```
Since `\sum_k t_k<\infty`, Tonelli implies `\sum_k B_k(x)<\infty` for almost every `x`, hence `B_k(x)\to0`; the above interval estimate proves the full-time claim. This argument needs no measure differentiation theorem and places no ball-growth restriction on `\rho`. \(\square\)

For `s=2`, Claim A gives a time-independent uniform bound on `t h_t\rho`. Claim B and dominated convergence **recover and strengthen** Lemma 3.10.5's fixed-`F\in L^1(dV)` conclusion. The distinction is essential: `F` is fixed before taking `t\downarrow0`.

## 4. Exact sharp models: the codimension-two endpoint is genuinely critical

Work on the flat torus `X=\mathbb R^m/\mathbb Z^m` with unit coordinate metric, choose `0<R<1/4`, and identify a Euclidean ball `B_R(0)`. For `0<s<m` put
```math
d\rho_s(x)=\mathbf 1_{B_R(0)}|x|^{-s}\,dV(x).
```
This is finite and satisfies `\rho_s(B_r(x))\le C r^{m-s}` for all centers: for `|x|<2r`, integrate on `B_{3r}(0)`; for `|x|\ge2r`, the density is at most `r^{-s}` on `B_r(x)`. The flat-torus heat kernel is the periodized Euclidean Gaussian. Every nonzero lattice translate is exponentially negligible for `x\in B_R(0)`. Scaling `x=\sqrt t\,z` therefore yields the **exact positive constant**
```math
\boxed{\lim_{t\downarrow0}t^{s/2}(h_t\rho_s)(0)
=\frac{1}{(4\pi)^{m/2}}\int_{\mathbb R^m}e^{-|z|^2/4}|z|^{-s}\,dz
=2^{-s}\frac{\Gamma((m-s)/2)}{\Gamma(m/2)}.}
```
For `s=2<m`, this is `1/[2(m-2)]`: `t h_t\rho_2(0)` **does not** tend to zero. For real dimension `m=2`, the critical Frostman condition is satisfied by the atom `\rho=\delta_0`, and periodization gives
```math
\lim_{t\downarrow0}t(h_t\delta_0)(0)=1/(4\pi).
```
Consequently the printed endpoint `O(1/t)` cannot be replaced by `o(1/t)` in the supremum norm.

It is likewise impossible to make the fixed-`F` conclusion uniform over `F\ge0,\ \|F\|_{L^1}\le1`: the functions
```math
F_t=\frac{\mathbf1_{B_{\sqrt t}(0)}}{\operatorname{vol}(B_{\sqrt t}(0))}
```
have unit `L^1` norm, while `t h_t\rho_2(x)\ge c>0` throughout `B_{\sqrt t}(0)` when `m>2`, by the flat Gaussian's local positive lower bound. The same conclusion holds with the atom for `m=2`. Hence `t\int(h_t\rho)F_t\,dV\ge c`, although every **fixed** `F\in L^1` satisfies the printed convergence.

Finally, for any `m\ge3` and `2<s<m`, choose `m+2-s<\beta<m` and the **fixed**, integrable `F(x)=\mathbf1_{B_R(0)}|x|^{-\beta}`. The same explicit flat Gaussian lower bound gives for `|x|\le\sqrt t`,
```math
(h_t\rho_s)(x)\ge c t^{-s/2},
\qquad
t\int_X(h_t\rho_s)F\,dV
\ge c t^{1-s/2}\int_{B_{\sqrt t}(0)}|x|^{-\beta}\,dV
=c't^{(m+2-s-\beta)/2}\longrightarrow+\infty.
```
Thus the growth exponent `s=2` is also the **sharp threshold** for a conclusion valid for *every* fixed `L^1` test under only this family of Frostman hypotheses; strict supercriticality can destroy it. No singular heat-flow computation is assumed: these models use the explicit periodized Gaussian.

## 5. Classification, possible editorial use, and limitations

- **Classification:** `POME-HEAT-FROSTMAN-CRITICAL-QUANTIFIERS-001` — **low / verified conditional deduction**. Both original Lemmas 3.10.1 and 3.10.5 remain correct as stated; the latter's quantifier on `F` is indispensable. Neither is a false theorem or a repaired proof gap.
- **Proposed optional addition**, not an applied source change: after Lemma 3.10.5, record the full `r^{m-s}\mapsto t^{-s/2}` estimate, the almost-everywhere decay for finite measures, and the flat-torus codimension-two sharpness distinction. This clarifies uses in potential estimates requiring `L^1` pairing versus uniform convergence.
- **Dependents to recheck when used:** estimates pairing heat-regularized trace measures with unbounded `L^1` coefficients; any argument that accidentally chooses the test `F=F_t` after the heat parameter or replaces the fixed-`F` limit by `L^1\to\mathbb R` operator-norm convergence. No dependent theorem is asserted faulty without inspecting its actual use.
- **Verification scope:** selected direct reading of current §3.10.1's Gaussian proof and §3.10.5's two conclusions, plus independent Frostman/periodized-Gaussian calculations and the all-times Tonelli argument. General compact-manifold spectral construction, Nash/Davies analytic prerequisites, and all downstream uses are not fully certified. No excluded Demailly approximation/regularization, Bergman, weighted `L^2`, Ohsawa–Takegoshi, multiscale, or positivity-loss proofs were opened.
- **Repository boundary:** review-only English Markdown; no source/registry/label/tag/canonicalization, project tests, build, CI, formalization, website, or production `main` changes.
