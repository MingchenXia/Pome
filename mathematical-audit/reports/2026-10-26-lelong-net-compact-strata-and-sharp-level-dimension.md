# Selected mathematical audit: Lelong strata under weak current nets

**Date:** 2026-10-26 (Asia/Shanghai).  
**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Starting audit head:** `9f186281dfdc5eb8ce35b374496eddb273d5e747`.  
**Scope:** selected integrated statements and proofs in §§6.7 and 6.33; no entire section or dependency chain certified.

## Sources, permanent labels, and actual reading scope

1. `docs/sections/lelong-numbers-and-multiplier-ideals--logarithmic-growth-and-the-jensen-formula/index.html`, main blob `230bcb3b776ea69fbadba9f3422ed3f356280dc8`, §6.7 tag `4939444F8FDD`. Proposition 6.7.1 tag `C79BAEA70FC1`, lines 7–43; Jensen–Lelong Theorem 6.7.6 tag `BD2098F182CC`, lines 76–150 (particularly 127–149); Proposition 6.7.9 tag `43A1E607F822`, lines 155–183; its sequential upper-limit equation 6.7.10 tag `B5D2B6B6970E`, lines 159–162.
2. `docs/sections/lelong-densities-generalized-masses-and-multiplicity--lelong-densities-of-positive-currents/index.html`, main blob `48bb9c525a826e4d1e337b755fac22aaa3016e66`, §6.33 tag `38F79B8D878`. Density monotonicity Theorem 6.33.1 tag `7ACCEC6E0526`, lines 7–78 (including the `p=0` case); uniform local measure control Corollary 6.33.5 tag `6FD01B620D33`, lines 83–94; bounded-current comparison Lemmas 6.33.7–8 tags `C9AA991622D8` and `50567CE0F546`, lines 103–147 (selected formula/endpoint checks only); chart independence Theorem 6.33.10 tag `3FA889730FFE`, lines 151–193 (selected scaling/center comparison); upper semicontinuity and Hausdorff bound Theorem 6.33.13 tag `2B9769222A07`, equation 6.33.14 tag `F89B30DD3077`, lines 197–240.

The normalizations are `dd^c=(i/2π)∂∂̄`, `β=dd^c|z|²`, and `D_T(a,r)=r^{-2p}(T∧β^p)(B(a,r))` for a positive closed current of bidimension `(p,p)`. Here `0≤p≤n`. Basic positivity, weak measure convergence, and the standard Lelong–Jensen monotonicity established in these sections are **inputs** to the deductions below, not transitive certifications. The dedicated Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof programme is excluded and remains **deferred-by-user**; no proof-completion work on that programme was attempted. Local convolution appearances in existing proofs are not a reopening of that programme.

## POME-LELONG-NET-COMPACT-STRATA-001

**Status:** verified conditional deduction. **Severity:** low. **Source statements:** correct as printed, no false theorem alleged. **Proposal:** add an optional post-Theorem 6.33.13 corollary replacing *sequential* weak-current semicontinuity by a *directed-net, compact-uniform* statement. A parallel post-Proposition 6.7.9 corollary applies to psh potentials converging in local `L¹`. **Dependents:** moving Lelong-level-set compactness arguments and use of Lelong constraints in nonmetrizable or directed limits; not a replacement for Siu analyticity or any regularization assertion.

### Claim and proof

Let `(T_i)_{i∈I}` be an **arbitrary directed net** of positive closed currents of fixed bidimension `(p,p)` on an open coordinate domain `Ω⊂ℂⁿ`, converging weakly to a positive closed current `T`. For every compact `K⊂Ω`,

\[
\boxed{\limsup_{i\in I}\ \sup_{x\in K}\nu(T_i,x)
\ \leq\ \max_{x\in K}\nu(T,x).}
\tag{1}
\]

In particular, for every `c>0` and compact `K` disjoint from `E_c(T)={x:ν(T,x)≥c}`, there exists `i_0` such that

\[
\boxed{K\cap E_c(T_i)=\varnothing\quad\text{for every }i\succeq i_0.}
\tag{2}
\]

The same statements hold for `L¹_loc`-convergent directed nets of psh functions `u_i→u`, using `T_i=dd^c u_i` and the current/potential equivalence in Theorems 6.7.6 and 6.33.10.

Proof. Write `μ_i=T_i∧β^p` and `μ=T∧β^p`; then `μ_i→μ` vaguely. For each fixed compact `F⊂Ω`,

\[
\limsup_i\mu_i(F)\leq\mu(F).\tag{3}
\]

Indeed, for any `ε>0`, outer regularity and smooth cutoff approximation give `χ∈C_c^∞(Ω)`, `χ≥1` on `F`, `χ≥0`, and `∫χ\,dμ≤μ(F)+ε`. For each `i`, `μ_i(F)≤∫χ\,dμ_i`, and the latter integrals converge along the **net**. Let `ε↓0`; no sequential compactness or countable selection is used.

Fix `c>m:=\max_Kν(T,·)`. The maximum exists and is finite by Theorem 6.33.13 (upper semicontinuity) and Corollary 6.33.5 (local uniform density bounds). For each `a∈K`, select a sufficiently small radius `r_a` with `\overline B(a,r_a)⊂Ω`, `μ(∂B(a,r_a))=0`, and

\[
\frac{\mu(\overline B(a,r_a))}{r_a^{2p}}<c.
\tag{4}
\]

Such a radius exists because all but countably many spheres have zero `μ`-mass, and the density converges to `ν(T,a)<c`. This also works when `p=0`, with `r^{2p}=1` and the density limiting to the atom `μ({a})`. Choose `0<ρ_a<r_a` sufficiently close to `r_a` that `μ(\overline B(a,r_a))/ρ_a^{2p}<c`, and set `U_a=B(a,r_a-ρ_a)`. If `b∈U_a`, then `B(b,ρ_a)⊂ B(a,r_a)`, whence Lelong monotonicity gives

\[
\nu(T_i,b)\leq \frac{\mu_i(B(b,ρ_a))}{ρ_a^{2p}}
\leq\frac{\mu_i(\overline B(a,r_a))}{ρ_a^{2p}}.
\tag{5}
\]

By (3) and the strict margin in (4), there is an index `i_a` such that (5) is `<c` for **all** `i\succeq i_a` and **all** `b∈U_a`. Compactness of `K` provides finitely many `U_{a_j}` covering it. Directedness provides a common upper bound of their finitely many `i_{a_j}`; hence `\sup_K ν(T_i,·)<c` eventually. Since `c>m` is arbitrary, (1) follows, and (2) is the particular case `m<c`. For psh functions, local `L¹` convergence implies distributional convergence of `dd^c u_i`, and all currents are positive; Theorem 6.33.10 identifies their Lelong numbers. QED.

**Precision:** (1) concerns an upper bound on a compact set; it does *not* give convergence of the suprema, Hausdorff convergence of Lelong strata, or persistence of points with positive Lelong number. The proof uses finite covers of each **fixed** compact, not an illicit sequential extraction from a net.

**Sharp asymmetry test.** In `ℂⁿ`, `n≥1`, put `u_ε(z)=log(|z_1|²+ε)` for `ε>0` and `u(z)=log|z_1|²`. The `u_ε` are smooth psh and converge to `u` in `L¹_loc`. For `T_ε=dd^c u_ε`, `ν(T_ε,x)=0` at every point, whereas `T=dd^c u=[z_1=0]` by Poincaré–Lelong, with `ν(T,x)=1` on the hyperplane. Hence the reverse bound and lower Kuratowski/Vietoris persistence are false even for smooth positive closed approximating currents. This is a counterexample to a **possible stronger claim**, not to the printed theorems.

## POME-LELONG-LEVEL-SHARP-DIM-001

**Status:** verified conditional deduction. **Severity:** low. **Source statement:** Theorem 6.33.13's local `\mathcal H^{2p}` bound is correct and the dimension exponent is sharp. **Proposal:** optional linear-plane equality-model remark immediately after Theorem 6.33.13. **Dependents:** proposed improvements claiming level sets uniformly have Hausdorff dimension strictly less than `2p`; not a repair.

For any `0≤p<n`, fix a complex affine `p`-plane `L⊂ℂⁿ` and let `T=[L]` be its integration current, of bidimension `(p,p)`. The local normalization in §6.33, lines 7–19, gives at every `a∈L`

\[
(T\wedge β^p)(B(a,r))=\int_{L\cap B(a,r)}β^p=r^{2p},
\qquad \nu([L],a)=1.
\]

For `a∉L` a small ball does not meet the support, hence `ν([L],a)=0`. Thus `E_1(T)=L`, whose intersection with any nonempty relatively open ball of `L` has positive finite `\mathcal H^{2p}` measure and Hausdorff dimension exactly `2p` (including `p=0`, where this is a single atomic point and `\mathcal H^0` is counting measure). It is impossible to replace the bound `\dim_H E_c≤2p` by any smaller universal dimension exponent. This checks the `p=0` convention as well as the `p>0` normalization; it does not assert optimality of the specific numerical covering constant `4^{2p}`.

## Selected original-proof checks and verification boundary

- §6.7.1: radial supremum over open balls equals sphere supremum by convexity; negative logarithm reverses coefficient inequalities; exceptional null-set premise is upgraded using mean inequality. No incorrect coefficient sign found.
- §6.7.6: radial derivative `dM/d(log r²)=D_u`; mass convergence is used only at radii whose spheres are `μ`-null. The limit comparison between spherical means and suprema was read; the existing local convolution step is treated as a standard input, not as part of the excluded Demailly programme.
- §6.7.9: additive/max/supremum Lelong identities and the sequential `L¹` upper limit were compared against their hypotheses; no new false statement found.
- §6.33.1/.5: open-ball **left** continuity is separated from right limits including sphere atoms; the `p=0` atom convention and `β^p` normalization were checked.
- §6.33.7–8/.10: selected bounded-potential Stokes, truncation and chart-invariance lines were inspected for boundary and positivity conventions, but the full Bedford–Taylor recursion and continuity prerequisites were **not** independently certified.
- §6.33.13: the actual proof uses a sequence and finite disjoint-ball covers; the net and compact-uniform result above uses fresh finite-cover and cutoff arguments, without falsely attributing a net statement to the source.

**Outcome:** two optional correct-theorem refinements, no newly confirmed false theorem or proof gap. Sections §§6.7 and 6.33 receive only **selected proof-level coverage**, not full certification. No source, reading-edition body, permanent tags, proof registry, or main branch changed. No project build, CI, web publication, or formalization run.
