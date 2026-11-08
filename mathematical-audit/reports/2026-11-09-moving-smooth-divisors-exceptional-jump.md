# Smooth moving divisors: weakly continuous pullback versus discontinuous exceptional coefficients

**Finding:** `POME-BDIV-EXCEPTIONAL-COEFFICIENT-JUMP-001`  
**Date:** 2026-11-09  
**Status:** verified conditional deduction (not an error in the printed statements).  
**Severity:** low; caution for proposed coefficientwise limits and canonicalization of divisor traces.  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Audit branch:** `review/mathematical-audit` (audit Markdown only).

## Exact reading-edition scope

- `docs/sections/divisorial-currents-on-compact-modifications/index.html`, blob `79d6e21f9d3784bf3761846f77f90ad075253644`: Proposition **20.4.22**, source `non-kahler-pluripotential-theory:B3489943`, permanent `D7373D3639FA`, physical lines **437–464** (weak continuity of pullback and mass bound, Eq. 20.4.23); Corollary **20.4.24**, physical lines **469–480** (pullback of positive divisorial sums). Parent discussion lines 433–435.
- `docs/sections/divisors-and-logarithmic-limits-on-analytic-cycles/index.html`, blob `dae567406b2030e550664ca57b1fe77911d956d4`: Lemma **20.5.2**, source `demailly-complex-geometry:72B4BF94`, permanent `551A781E3A1C`, physical lines **11–27** (local `L^1` convergence of logarithms of holomorphic functions); Theorem **20.5.5**, source `demailly-complex-geometry:D58680EB`, permanent `F1C928146DBC`, especially lines **64–75, 119–127** (divisor-current limits).
- Normalization from §20.5 line 7: `dd^c=(i/2π)∂∂̄`, so `dd^c log|f|²=[div(f)]`.

The checked claim is *not* that Proposition 20.4.22 is wrong: its topology is the weak topology on **entire currents**, not convergence of generic Lelong/divisor coefficients along individual exceptional prime divisors. The following example shows why that distinction matters.

## Exact projective degeneration for every prescribed jump

Fix an integer `m≥1`, put `Y=ℙ²` with homogeneous coordinates `[Z₀:Z₁:Z₂]`, and let `p=[1:0:0]` and `L={Z₁=0}`. For nonzero `t∈ℂ` set

```text
F_t(Z₀,Z₁,Z₂) = Z₁^m + t(Z₀^m + Z₂^m),
D_t = div(F_t),       F_0 = Z₁^m,       D_0 = mL.
```

For `m=1` the `D_t` are lines. For `m≥2`, each `D_t` is a **smooth degree-m plane curve** for `t≠0`: if all three partial derivatives of `F_t` vanished at a projective point, then `Z₀=Z₁=Z₂=0`, impossible (the coefficients `m,t` are nonzero). Also `F_t(p)=t≠0`, hence `p∉D_t`. As `t→0`, the defining sections converge uniformly in local bundle trivializations to `Z₁^m`; Lemma 20.5.2 (or directly the local holomorphic-logarithm argument) yields

`[D_t] ⇀ m[L]` on `Y`.

Let `g:X=Bl_pY→Y` be the blowup, `E≃ℙ¹` its exceptional divisor, and `\widetilde L` the strict transform of `L`. Since `p∉D_t`, the pullback divisor `g^*D_t` is exactly the strict transform `\widetilde D_t` and has **generic exceptional coefficient zero**:

`ν(g^*[D_t],E)=0` for every `t≠0`.

By contrast, `L` has multiplicity one at `p`, so

`g^*(m[L])=m[\widetilde L]+m[E]`, and `ν(g^*(m[L]),E)=m`.

This is elementary in the two standard affine blowup charts. In `Z₀≠0` let `x=Z₁/Z₀`, `y=Z₂/Z₀`. The defining function is `f_t=x^m+t(1+y^m)`. In the `x`-chart of the blowup `x=s,y=sv` it pulls back to

`f_t∘g=s^m+t(1+s^m v^m)`.

For each `t≠0`, this restricts to `t` on `E={s=0}`; at `t=0` it is `s^m`, giving exceptional multiplicity exactly `m`. In the complementary chart `x=uv,y=v` the equation is

`f_t∘g=u^m v^m+t(1+v^m)`.

There `E={v=0}` and `\widetilde L={u=0}`; the limit is `u^m v^m`, explicitly revealing **both** multiplicity-`m` components.

Because `f_t∘g→f_0∘g` locally uniformly holomorphically and the latter is nonzero on every blowup coordinate ball, Lemma 20.5.2 gives **local `L¹` convergence of `log|f_t∘g|²`**, hence distributional convergence of their `dd^c`. Therefore, independently of any unverified global proof chain,

`g^*[D_t]=[\widetilde D_t] ⇀ m[\widetilde L]+m[E]=g^*(m[L])` on `X`.

This is exactly the **weak continuity** asserted in printed Proposition 20.4.22. The coefficient functional `T↦ν(T,E)`, however, jumps `0→m`. The jump can be arbitrarily large while every approximating `D_t` is **smooth**, misses the blowup center, and has the same numerical degree `m`. There is no contradiction with positivity, current compactness, or generic-Lelong upper semicontinuity: an upward jump is permitted.

As a cohomological check, writing `H=g^*c₁(O_{ℙ²}(1))`, one has `[\widetilde D_t]=mH` for `t≠0` and `[\widetilde L]=H-[E]`; thus `m[\widetilde L]+m[E]=mH` in `H^{1,1}(X)`. The exceptional mass emerges **inside a fixed cohomology class**, not by losing total mass at infinity.

## Audit verdict and proposal

1. **Printed Proposition 20.4.22 and Corollary 20.4.24: correct on the inspected point.** Weak convergence of full pullbacks coexists with nonconvergence of generic coefficients on fixed divisors. No proof gap or false theorem is alleged.
2. **Verified conditional deduction:** any proposed extraction of coefficientwise limits for b-divisors, Siu parts, or trace divisors from weak current convergence needs *additional hypotheses* (for example, direct coefficient control); it does not follow from Proposition 20.4.22 alone.
3. **Proposed change, not applied:** add a self-contained Remark/Example following Proposition 20.4.22, keeping both original source attribution and permanent tags. In particular, do not conflate the weakly continuous total-transform map `D↦g^*D` with the noncontinuous strict-transform map `D↦\widetilde D` along a family whose limiting divisor passes through the blowup center.
4. **Possible dependents for hypothesis checks, not flagged as wrong:** §20.1 b-divisor coefficients, §20.2 trace and restriction, and §20.4.26 exceptional corrections. No downstream assertion was claimed false or independently certified here.

**Scope:** selected §20.4.22, the local divisor-convergence input §20.5.2, and their exact projective example; **not** full §20.4/§20.5 mathematical certification or a claim of new first section visits. No Demailly regularization, Bergman, `L²`, Ohsawa–Takegoshi, multiscale-atlas or positivity-loss work was performed. Existing excluded checkpoints remain **deferred-by-user**, not resolved.
