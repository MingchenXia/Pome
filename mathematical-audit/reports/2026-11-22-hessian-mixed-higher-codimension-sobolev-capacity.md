# Audit: continuous complex Hessian products and Sobolev-capacity obstruction in higher transverse codimension

Date: 2026-11-22. Reviewed production `main`: `b6933b772f41b45918f7e25ed1afbbb1fd892272`; existing review branch at start: `1ee4bd79e083988cd2d0b2e193e5dcbc3bb7a2b9`. Audit-only mathematics; no production changes.

## Exact source, classification, and scope

**POME-HESSIAN-HIGHER-TRANSVERSE-CAPACITY-OBSTRUCTION-001 — low / verified conditional deduction.** The original statements are **not** claimed false. In the integrated reading edition, §8.7 Proposition 8.7.1 (source `non-kahler-pluripotential-theory:81F79DFF`, permanent tag `D2A0F255F625`, file `docs/sections/complex-hessian-equations--continuous-products-envelopes-and-domination/index.html`, blob `045d10eb63453837e8675d22436afa9b9d6335ad`, physical lines 11–36) supplies continuous mixed products, conditional on its approximation and mass arguments. §8.10 Lemma 8.10.6 (source `non-kahler-pluripotential-theory:350D7B3A`, tag `2A6BE9847309`, file `docs/sections/complex-hessian-equations--sobolev-capacity-and-two-hessian-factors/index.html`, blob `25f25433cb9b17de6715a5b05f8b3c15b95a18cd`, physical lines 186–205) gives zero first Sobolev capacity for real codimension-two compact sets; Example 8.10.7 (source `non-kahler-pluripotential-theory:36B886BE`, tag `AEB4F2397BBF`, lines 210–247) constructs a two-factor counterexample to first-Sobolev-capacity domination. The deduction below extends the *actual transverse concentration codimension* to every permitted product degree, rather than simply inserting trivial smooth additional factors.

**Hypotheses.** Let `(X,ω)` be a compact Hermitian manifold of complex dimension `n≥2`; choose the same integer `2≤m≤n` and admissible Hessian cone as Chapter 8. Given any `2≤k≤m`, there are bounded continuous global `ω`-plurisubharmonic (hence `m`-admissible) potentials `u_1,…,u_k` and a compact `E` contained in a **smooth real codimension-`k` submanifold**, for which

```math
\operatorname{Cap}_1(E)=0,\qquad
\left[\bigwedge_{j=1}^{k}(\omega+dd^cu_j)\right]\wedge\omega^{n-k}(E)>0.
```

The mixed product is the continuous product of §8.7.1 (wedge with the additional `ω^{m-k}` after its degree-`k` current). In particular no exponent `γ>0` and constant `C`, even depending on the specific potentials, gives the universal setwise domination `Q_k(A)≤C\operatorname{Cap}_1(A)^γ` for all Borel `A`. This is distinct from the first-factor trace estimate §8.10.2, and does **not** invalidate it.

## Complete local construction and proof

Choose a holomorphic coordinate chart with `z_j=x_j+i y_j`, `1≤j≤n`, and nested real boxes `B\Subset B'\Subset U`. Fix a nonnegative smooth cutoff `χ` supported in `U`, identically one on `B'`. For `1≤j≤k` set globally, by zero extension,

```math
u_j=a\chi|x_j|,\qquad
u_{j,\delta}=a\chi\sqrt{x_j^2+\delta^2}
\quad(0<\delta\le1).
```

For each `j`, `g_δ(t)=\sqrt{t^2+δ^2}` has `g_δ''(t)=δ^2(t^2+δ^2)^{-3/2}≥0`. The Leibniz terms in `dd^c(χg_δ(x_j))` other than `χdd^cg_δ(x_j)` are uniformly bounded smooth forms because both `g_δ` and `g_δ'` are uniformly bounded on the fixed cutoff support. Consequently one small `a>0`, independent of `j,δ`, ensures `ω+dd^cu_{j,δ}≥ω/2` globally. Furthermore `u_{j,δ}↓u_j` *uniformly* on `X`, so the `u_j` are continuous `ω`-PSH and are in the continuous-admissible class of §8.7.1.

Inside `B'` set `α_j=\frac{i}{4\pi}dz_j\wedge d\bar z_j=\frac{1}{2\pi}dx_j\wedge dy_j`, with Pome's `dd^c=\frac{i}{2\pi}\partial\bar\partial` convention. Direct differentiation gives

```math
dd^c u_{j,\delta} = \frac a2 g_\delta''(x_j)\,\alpha_j,
\qquad
\frac12g_\delta''(t)\,dt \rightharpoonup \delta_0.
```

Because the `k` mollified singular factors depend on **different real variables**, their joint measures converge as products of one-dimensional approximate identities; this is elementary Fubini plus uniform continuity of compactly supported tests. Taking the locally uniform limit in the continuous mixed product gives, on `B'`,

```math
Q_k:=\bigwedge_{j=1}^k(\omega+dd^c u_j)\wedge\omega^{n-k}
=\sum_{S\subseteq\{1,\dots,k\}} a^{|S|}
\left(\bigwedge_{j\in S} \alpha_j\delta_{\{x_j=0\}}\right)
\wedge\omega^{n-|S|}.
```

There are no hidden mixed-background derivatives in this local *explicit* product identity: each smooth approximating factor is `ω+(a/2)g_δ''(x_j)α_j` on `B'`, and the formula follows term-by-term.

Choose a compact `E\Subset B'` of positive relative `(2n-k)`-dimensional measure inside `\{x_1=\cdots=x_k=0\}`, for example a closed small box in the remaining real coordinates. Any proper subset `S\subsetneq\{1,…,k\}` misses a delta restriction in some normal real variable, hence its associated measure gives `E` zero mass. Only the full subset survives:

```math
Q_k(E)
=a^k\int_E\Bigl(\alpha_1\wedge\cdots\wedge\alpha_k\wedge\omega^{n-k}\Bigr)
\prod_{j=1}^k\delta_{\{x_j=0\}} >0 .
```

The displayed integral denotes the natural transverse Dirac contraction (rather than the restriction of an ambient top-degree differential form to a lower-dimensional submanifold); strict positivity follows from `ω>0`. Since `k≥2`, `E` is contained in the smooth real codimension-two submanifold `\{x_1=x_2=0\}` within the coordinate chart; §8.10.6 and monotonicity of `Cap_1` give `Cap_1(E)=0`. Thus the asserted universal power-capacity bound fails on this **fixed** Borel set `E`.

This generalizes the two-normal-variable case `k=2` of printed Example 8.10.7 but does not mistake that existing example for a new finding. The new content is the *exact singular measure supported in real codimension `k` for all `2≤k≤m`*, with every factor carrying a distinct transverse singularity.

## Direct mathematical review performed (separately from the new deduction)

- **Entire integrated §8.7 mathematical text, physical lines 7–222**, blob `045d10eb63453837e8675d22436afa9b9d6335ad`: uniform smooth product bounds and telescoping (8.7.1, lines 11–36); contact comparison (8.7.2, 44–57); penalized envelopes and contact support (8.7.3–4, 65–99); declared *linear elliptic* Green estimate (8.7.5, 103–110); nonvanishing mass (8.7.6, 117–148); domination and strict proper-equation comparison (8.7.7–9, 156–222). Mixed-product positivity and the distinction between a stated linear analytic input and an internally verified proof were preserved. No newly confirmed source error in these direct passages.
- **Entire integrated §8.10 mathematical text, physical lines 7–251**, blob `25f25433cb9b17de6715a5b05f8b3c15b95a18cd`: Sobolev capacity and Gauduchon trace (8.10.1–2, 32–96), Mazur/Dini quasicontinuity (8.10.3–4, 101–150), recursive two-factor symmetry and convergence (8.10.5, 155–178), codimension-two capacity nullity and transverse tensor-product current (8.10.6–7, 186–247). The `dd^c` coefficient `α_j` and the transverse Dirac mass factors were recalculated, not inferred from the assertion.
- **Selected-only prerequisites**: §8.6.1/.2/.6 as invoked for smooth Hessian approximants; §8.9.1/.3/.6 as invoked for current coefficient bounds; §11.4.2 as invoked for positive Gauduchon multiplier; §21.2.3 as a separate convex duality comparison from a cross-chapter direct reading. **These have not been reread or certified in full in this run**, and their use is recorded as dependency, not a completed transitive proof chain.

**Status:** the new codimension-`k` counterexample is a *verified conditional deduction* assuming the chapter's existing continuous mixed-product framework; the original §§8.7/8.10 statements have not been shown false. **Affected dependents:** any proposed extension of §8.10.2's `Cap_1^{1/2}` control to arbitrary positive mixed Hessian measures of degree ≥2; the local higher Hessian-capacity machinery of §8.11 is consistent with, and motivated by, this obstruction. **Proposed correction:** no theorem correction; optionally cross-reference this higher-codimension version after Example 8.10.7 in a separately reviewable future mathematics PR. Do not modify production.

**Audit limitations:** complete upstream verification: 0; mathematical findings: 1 low conditional deduction, 0 confirmed printed errors, 0 new identified circularities. No tests, builds, GitHub Actions, website publication or editing of main/source/registry/permanent tags. Demailly regularization and its dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof-completion programme remain **deferred-by-user, neither resolved nor certified**.
