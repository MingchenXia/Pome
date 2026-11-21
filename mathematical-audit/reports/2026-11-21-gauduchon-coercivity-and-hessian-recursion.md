# Direct mathematical audit: Gauduchon mass extrema (§12.16) and recursive complex Hessian currents (§8.9)

**Date:** 2026-11-21. **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (read afresh for this session). **Audit branch:** `review/mathematical-audit`. **Scope:** entire present mathematical bodies of §12.16 (physical lines 7–110) and §8.9 (physical lines 7–197); selected upstream statement/hypothesis crosschecks only, not their complete proofs.

**Source of truth / pinned integrated reading-edition blobs**
- `docs/sections/a-gauduchon-variational-volume--curvature-conditions-for-mass-extrema/index.html`, blob `cedeb939240bded77843daec0292d1a8bde0d2cb`. Lemma 12.16.1 source tag `5C8E3A8A`, permanent `744D35F9BE16` (lines 17–46); Proposition 12.16.2 source `AAC97166`, permanent `CE7BE3992C5F` (51–68); Theorem 12.16.3 source `F297E7B1`, permanent `26629526444F` (76–103), including equation (12.16.4), permanent `D5CA82478984` (97–102).
- `docs/sections/complex-hessian-equations--bounded-potentials-and-recursive-hessian-currents/index.html`, blob `117b866408974cdf706bf305df75e35e1b8affde`. Lemma 8.9.1 source `968D4676`, permanent `C35233382EB9` (14–32); Proposition 8.9.3 source `354EA0C7`, permanent `EB2FA13CDDE0` (47–79); Theorem 8.9.6 source `61CC9D08`, permanent `846671D5582A` (97–116); Proposition 8.9.7 source `633FD461`, permanent `26EFAEC0B76D` (124–143); Lemma 8.9.8 source `B3E694DA`, permanent `A1E60FC7AA88` (157–170); Example 8.9.9 source `595A54DE`, permanent `5F56B4D9CC35` (178–193).
- Relevant **selected** inputs (statements or identified proof steps only): §8.1 lines 7–16 (explicit `2≤m<n`), Lemma 8.2.7 lines 160–178 (absolute mixed-form estimate), Theorem 8.6.6 lines 174–190 (decreasing admissible approximations), Proposition 8.7.1 (continuous products), Theorem 11.1.5 / (11.1.6) lines 69–91 (mass expansion), and Theorem 12.15.4 / Proposition 12.15.6 (mass extremum identification). Their complete transitive proofs were **not** certified; in particular the smoothing step quoted in §12.15.4 was not reopened.

## Finding POME-GAUD-MASS-COERCIVE-QUADRATIC-GAP-001: quantitative detection and coercive uniqueness

**Classification:** low / **verified conditional deduction** (NOT a confirmed error or a false theorem). **Affected statements:** strengthening of Lemma 12.16.1 and Theorem 12.16.3, not a replacement. **Hypotheses:** a compact complex n-fold with smooth positive Hermitian form `ω`, fixed normalization `dd^c=i∂∂̄/(2π)`; for the mass consequence n=3, `v∈H_ω`, `Ω=ω+dd^cv`, and `dd^c(Ω²)=0`.

**(A) Quantitative detection of positivity.** For *any* smooth real `(n−1,n−1)` form `T` and real `κ`, the following are equivalent:

```math
T\geq \kappa\,\omega^{n-1}
\quad\Longleftrightarrow\quad
\int_X df\wedge d^cf\wedge T\geq
\kappa\int_X df\wedge d^cf\wedge\omega^{n-1}
\quad\text{for every }f\in C^\infty(X,\mathbb R).
```

*Proof.* The forward implication is immediate from positivity of `df∧d^cf=(i/2π)∂f∧∂̄f`. For the reverse implication apply printed Lemma 12.16.1 to the smooth real form `T−κω^{n−1}`. Its oscillatory cutoff proof is independent of the sign of `κ`: the normalized functions `k^{-1}χ sin(kℓ)` recover the form's pointwise value against any rank-one positive covector. No positivity or closedness hypothesis on `T` is omitted.

**(B) Exact mass gap on a Gauduchon threefold and rigidity.** Set `T=−dd^cω`. For every real smooth `f`, the exact identity from (12.16.4) is

```math
M_\omega(v+f)-M_\omega(v)=3\int_X df\wedge d^cf\wedge T.
```

It is valid even when `v+f` is not admissible, as a polynomial identity of smooth forms; admissibility is imposed only when comparing minimizers/maximizers. If `T≥κω²` with `κ>0`, then every admissible `v+f` satisfies

```math
M_\omega(v+f)-M_\omega(v)
\geq 3\kappa\int_X df\wedge d^cf\wedge\omega^2
=\frac{\kappa}{2\pi}\int_X|\partial f|_\omega^2\,\omega^3.
```

Here the norm is defined by `i∂f∧∂̄f∧ω²=(|∂f|_ω²/3)ω³`, so the factor is explicit in the project's `dd^c` convention. On connected compact `X`, Poincaré's inequality also yields a positive constant `c_{ω,κ}` with

```math
M_\omega(v+f)-M_\omega(v)
\geq c_{\omega,\kappa}\,
\|f-\operatorname{avg}_{\omega^3}(f)\|_{L^2(\omega^3)}^2.
```

Equality of masses forces `f` to be constant; hence the minimizing **smooth potential is unique modulo constants**, provided the Gauduchon representative exists and `−dd^cω` satisfies the stated *strict* curvature bound. Reversing signs gives the corresponding strict maximum and uniqueness when `dd^cω≥κω²`. If only `T≥0`, exact equality is characterized by the pointwise vanishing of the nonnegative top form `df∧d^cf∧T`; no uniqueness is asserted in degenerate directions.

*Verification and limits.* Expand `(Ω+dd^cf)^3`. The linear term vanishes by `dd^cΩ²=0`, the cubic term integrates to zero by Stokes, and the quadratic term integrates by parts to `−3∫df∧d^cf∧dd^cΩ`; since `dd^cΩ=dd^cω` the displayed identity follows. The horizontal rank-two Hopf curvature `−dd^cω=α²` from §23.1.3 is only **semidefinite** and therefore does not satisfy `κ>0`; §23.1.38 already describes its nonunique fiber-constant minimizers. That earlier Hopf result is **not** claimed as new. This deduction does not assert that backgrounds admitting a strictly signed `dd^cω` or a Gauduchon potential always exist.

**Correction / downstream implications:** no change to printed §12.16 is required. If a future argument claims uniqueness from merely `dd^cω≤0`, it must impose strict positivity or another condition eliminating null directions. The theorem's equality of smooth and bounded extrema still uses the §12.15.4 input and is NOT independently certified here.

## Direct §12.16 verification and boundaries

- The oscillatory cutoff in Lemma 12.16.1 (lines 27–45) detects the *full pointwise* cone of `(n−1,n−1)` forms, not just a trace inequality; the error term after differentiating `k^{-1}χ sin(kℓ)` is uniformly `O(k^{-1})` on its support.
- Proposition 12.16.2 (61–67): the first variation vanishes against arbitrary smooth directions because the strict positivity cone is `C²`-open; the sign of the second variation is the negative of the test against `dd^cΩ^{n−2}` and therefore gives the stated direction.
- Theorem 12.16.3 (95–103): the cubic term is exact and the Gauduchon condition eliminates the linear term; only the quadratic term survives for n=3, so local and global extrema coincide. §12.15.4's passage from smooth to all bounded masses is an **upstream step**, not audited as part of this session.

No new confirmed original mathematical error in §12.16.

## Direct §8.9 verification and boundaries

- The local coefficient measure bound at lines 23–32 uses **the actual chapter condition** `2≤m<n` in §8.1, so `Γ_m⊂Γ_2`; the eigenvalue identity `σ_1²=∑λ_i²+2σ_2` justifies coefficient control by nonnegative trace. Its dependence on the smooth decreasing approximation theorem §8.6.6 and the degree-one CLN estimate §8.7.1 is logged, **not independently proved**.
- Lines 61–79 define ordered `D_p` using bounded canonical values multiplied by *fixed measure-coefficient* `D_{p−1}`; monotone pointwise convergence allows dominated convergence for the **outermost** index, while earlier indices are tested with a fixed smooth factor. Thus (8.9.4) proves *iterated* limits, not interchangeability or simultaneous convergence.
- Lines 97–116: the shifted positive `Q_m=R_m∧ω^{n−m}` is measure-valued; the proof deliberately does **not** infer an order-zero bound for the unwedged `D_m`. Smooth Gårding positivity and local mass estimates pass to the distributional ordered limit.
- Lines 124–143: differentiate the subset polynomial `R_p`; its two-hat terms occur twice and the product `dω∧d^cω` has **positive** sign after the graded commutation of the odd three-forms. There is no omitted torsion term. In the mixed smooth/one bounded case the ordinary product is ordering-independent; this does not establish general symmetry.
- Lines 157–170: `dd^cρ≥2ω` is a valid local cone-shift, but `d(dd^cρ−ω)=−dω`; one must retain torsion when using the corrected local potentials.
- Lines 178–193: the `n=3,m=2` example has shifted eigenvalues `(1/2,1/2,1/2)` versus `(1/5,1,1)`, giving `1/4<7/15`; their unshifted 2-Hessians are `1/4>0`, respectively. This confirms that shifting does not preserve order.

**Open upstream / downstream:** the absolute-form coefficient estimate §8.2.7, the monotone admissible approximation §8.6.6, and the CLN estimate §8.7.1 are used as stated but not fully audited here. Simultaneous weighted convergence, symmetry and comparison depend on §§8.10–8.13; they are *not* consequences of §8.9 alone. No new confirmed printed error was found in §8.9. Do not treat this conditional review as complete certification of the Hessian product chain.

## Scope accounting and exclusions

**New direct coverage:** two complete integrated mathematical sections (current §§12.16 and 8.9); **selected prerequisite checks:** six results plus §8.1 scope and a §23.1 reference check; **new transitive proof-chain certifications:** zero. Historical visits remain unreconciled and must not be reclassified as first-ever coverage. Demailly approximation/regularization and its Bergman/L²/OT/multiscale/positivity-loss programme remain **deferred-by-user**, neither proved nor certified; no dedicated proof work was performed there. No source/registry/canonical-tag/site modifications, tests, builds, CI, or publication.
