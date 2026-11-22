# Direct mathematical audit: closed-nef subtraction, warped endpoints and trace constraints

**Date:** 2026-11-23. **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Review branch:** review/mathematical-audit.

**New finding:** POME-WARPED-FLAT-ZERO-LOG-VOLUME-001 — **low / verified conditional deduction**, not an error in the printed theorem. **New full direct current reviews: two sections** (§§12.12–12.13); **selected nonexcluded passages** §§15.10 and 19.8 only. **New confirmed printed errors: zero; completed transitive upstream certifications: zero.** Earlier unrelated findings are not counted again.

## Exact integrated reading scope and identity

1. **§12.12, complete mathematical text**, physical lines 7–166: docs/sections/a-gauduchon-variational-volume--subtraction-with-a-closed-nef-core/index.html; blob 88e74272e61ae22c6f87b2a9fba781178da14d70. Source non-kahler-pluripotential-theory. Theorem 12.12.2 (source 74C32CFB; permanent 026E84610646), lines 24–76; Proposition 12.12.4 (source 00962E6E; permanent FBFFC53EC40F), lines 87–109; Example 12.12.7 (source 9D36D469; permanent D37A528BDFB8), lines 133–166.
2. **§12.13, complete mathematical text**, lines 7–150: docs/sections/a-gauduchon-variational-volume--subtraction-on-warped-products/index.html; blob 5bff92967df7c96355d202871fc3dc033c99010d. Theorem 12.13.1 (source non-kahler-pluripotential-theory:3199B4CA, permanent B5C9469E9BB3), lines 26–74; Proposition 12.13.4 (source D87E6BC6, permanent 6E8682D7FD89), lines 82–106; Proposition 12.13.6 (source F535A551, permanent 172CF285DEA0), lines 111–136. Formula 12.13.2 (permanent 503F3EDAE05A), lines 31–33, is the decisive new-deduction input.
3. **§19.8 selected ONLY**: Gauduchon degree, Theorem 19.8.5 (source non-kahler-pluripotential-theory:6E03C7D3, permanent 1DFDCCEF325D), physical lines 104–148; divisorial trace Theorem 19.8.7 (source 7C3569E2, permanent 165328A043C0), lines 150–213. Integrated file docs/sections/holomorphic-sections-and-hermitian-mass/index.html; blob 5f00431e7986d899dc833c89175686b75f09371d. The dedicated Bergman and weighted L2 material is **not** reviewed, nor is §19.8 claimed complete; a 2026-11-22 selected §19.8 review also remains in the matrix.
4. **§15.10 selected ONLY**: the **conditional bounded-measurable-density limit** in Theorem 15.10.1, source non-kahler-pluripotential-theory:E589A1BA, permanent BA5CB37AAAC1, lines 58–104 of docs/sections/equations-with-prescribed-singularities--a-bounded-subsolution-theorem/index.html; blob 6240b6dc071d12eac1476ed548736d012c1a4fa2. The earlier smoothing construction at lines 26–56 and its approximation input are expressly **deferred-by-user**, not checked or certified. No inference that the entire theorem's prerequisites are now proved.

These are present-main reading-edition HTML, not title-based source substitutes. No comparison with a private scan was needed.

## POME-WARPED-FLAT-ZERO-LOG-VOLUME-001

**Status/severity:** low / **verified conditional deduction** relative to the valid formula of Theorem 12.13.1. It is not a printed-theorem error, proof-gap repair, or proof of its transitive analytic prerequisites.

**New precise hypothesis:** Keep §12.13's connected compact Kähler base (B,α), of complex dimension m≥2, W=∫_B α^m>0; smooth positive probability form σ; compact connected curve C with probability form w; X=B×C, n=m+1 and θ_s=α+(a+t−s)w. Let Z be a nonempty compact smooth real submanifold of B of real codimension d≥1. Fix a smooth auxiliary Riemannian metric, let ρ=dist(.,Z) in a normal tube, and take, for some β>0,

\[
a(x)=\exp(-\rho(x)^{-\beta})\quad (0<\rho<\rho_0),\qquad a|_Z=0,
\]

extended smoothly and strictly positively away from Z. It is a smooth nonnegative coefficient vanishing to infinite order along Z. Write

\[
A_Z=\lim_{r\downarrow0}r^{-d}\int_{\{\rho<r\}}\sigma\in(0,\infty),
\quad T_\varepsilon=\log(1/\varepsilon),\quad
H(\varepsilon)=\int_B\frac{\sigma}{a+\varepsilon},\quad
J(\varepsilon)=\int_B\frac{\sigma}{(a+\varepsilon)^2}.
\]

Tubular smooth-volume expansion gives the limit defining A_Z. Importantly, the normalizing measure is σ, **not** α^m unless they coincide.

**Verified conclusion:** For ε↓0,

\[
\begin{aligned}
H(\varepsilon)&\sim A_Z\,\varepsilon^{-1}T_\varepsilon^{-d/\beta},\\
J(\varepsilon)&\sim A_Z\,\varepsilon^{-2}T_\varepsilon^{-d/\beta},\\
\mathcal V_\mu(\theta_{t-\varepsilon})
&\sim \frac{nW}{A_Z}\,\varepsilon T_\varepsilon^{d/\beta},\\
\lambda_\mu(\theta_{t-\varepsilon})
&\sim \left(\frac{nW}{A_Z}\right)^{1/n}
 \varepsilon^{1/n}T_\varepsilon^{d/(\beta n)},\\
\mathcal C(t-\varepsilon)
&\sim n^{-(n-1)/n}W^{1/n}A_Z^{-1/n}
 \varepsilon^{1/n-1}T_\varepsilon^{d/(\beta n)}.
\end{aligned}
\]

In particular λ_μ(θ_t)=0, the subtraction cost diverges but is integrable at t, and the total remaining cost satisfies

\[
\int_{t-\varepsilon}^t\mathcal C(s)\,ds
=\lambda_\mu(\theta_{t-\varepsilon})
\sim (nW/A_Z)^{1/n}\varepsilon^{1/n}T_\varepsilon^{d/(\beta n)}.
\]

**Proof of the inverse-moment asymptotics (not just exponent matching).** Set T=log(1/ε), R=T^{-1/β}. On ρ≤R, a≤ε, while for each fixed η∈(0,1) one has uniformly on ρ≤(1−η)R that a/ε≤exp(−((1−η)^{-β}−1)T)→0. Therefore for p=1,2 the contribution from this inner tube is asymptotic to ε^{-p} times its σ-volume, yielding a liminf for ε^p R^{-d}∫σ/(a+ε)^p of at least (1−η)^d A_Z. The entire ρ≤R tube contributes at most ε^{-p}(A_Z+o(1))R^d. For R≤ρ≤ρ_0 the integrand is bounded by a^{-p}=exp(p/ρ^β). In tubular radial coordinates its integral is at most a constant times

\[
\int_R^{\rho_0}\rho^{d-1}\exp(p/\rho^\beta)\,d\rho
=\frac1\beta\int_{\rho_0^{-\beta}}^T e^{pv}v^{-d/\beta-1}\,dv
=O(\varepsilon^{-p}T^{-d/\beta-1}),
\]

which is o(ε^{-p}R^d). The complement of the fixed tube contributes O(1). Letting η↓0 proves H∼A_Z ε^{-1}R^d and J∼A_Z ε^{-2}R^d with **the same exact coefficient**. The §12.13.1 formula for volume and its Eq. 12.13.2 for cost now yield all displayed equivalents algebraically, including the factor n^{-(n−1)/n}. Monotone convergence gives H(0)=∞; the exact cost identity Eq. 12.13.3 then gives the remaining-cost equivalent. No arbitrary net is replaced by a sequence: this is the single scalar ε↓0.

**Sharp model and limitations.** This is a genuine infinite-order zero outside the finite-order hypothesis a≍ρ^k of Proposition 12.13.4. The logarithmic multiplier T^{d/β} cannot be replaced by a constant in this model. These equivalents do **not** apply to every smooth flat zero without an explicit profile, and the endpoint is **not big** by Proposition 12.13.6 even though every preceding θ_s is strictly positive.

**Proposed correction:** None required. An optional separately reviewed corollary after Proposition 12.13.4 may add this infinite-order example without editing the source, permanent labels or registry. **Dependents:** endpoint volume and variational derivative bounds of §12.13, comparisons to §12.14 and stability claims that require nonvanishing endpoint volume. It is a quantitative example, not a proof of arbitrary Gauduchon-equation solvability.

## Direct check of the other nonexcluded mathematical steps

**§12.12.** The curve C has ∫_C θ_s=(t−s)∫_C Ω; this excludes strict positivity at s=t and nefness after t. The nef closed core a_s has mass V_s; the closed nef volume formula and B≥0 give λ_μ(θ_t)≥V_t^{1/n}. Differentiating the smooth interior f(s)=λ_μ(θ_s) and integrating −f'(s) proves the *improper* cost identity without swapping a nonlinear limit and integral. The two initial tests κ_0 and γ_0 give the separate bounds U_μ and V_0^{1/n}+Δ_μ(B). In Proposition 12.12.4, S=∑γ_0^j κ_0^{n−2−j} is closed and nonnegative; the dd^c integration by parts has the plus sign, and ∫κ_0²∧S=(n−1)V_0. In Example 12.12.7, L²=LQ=1, Q²=0, a_0=2L+Q and V_s=1+4(1−s)+3(1−s)²; the Poincaré–Lelong identity for E of class L−Q gives θ_1+dd^c(½log|s_E|²)=B+½(L+Q)+½[E]≥Ω/2. No new confirmed statement error. The closed nef-and-big criterion in the final step remains a declared dependency rather than a newly proved theorem.

**§12.13.** With Ω_ε=A_ε+Lw and γ_s=L^{-1/m}Ω_ε one has γ_s^m=L^{-1}A_ε^m+mA_ε^{m−1}w; each term is closed, so the metric is balanced, not merely Gauduchon. The determinant equation yields γ_s^n=(nW/H)L^{-n/m}μ, hence D_μ(γ_s)=(nW/H)^{m/n}H and ∫w∧γ_s^m=WJ/H. The cost coefficient in (12.13.2) is exactly −d/ds(nW/H(t−s))^{1/n}. For finite-order zeros, the five regimes of Proposition 12.13.4 agree with radial moments; in Proposition 12.13.6 the test form ζ pulled back from B kills dd^c of any globally defined quasi-psh potential, and detects an arbitrarily small zero neighborhood without restricting the potential to the zero fiber. Remaining dependencies are the smooth base equation §14.2.1 and §12.6.32's balanced construction; they are **not** transitive-chain certified in this report.

**§19.8 selected non-Bergman portion.** Theorem 19.8.5's Poincaré–Lelong pairing m deg_γ L=∫_D γ^{n−1} has the expected positive sign. Theorem 19.8.7 subtracts only finitely many divisors with ord_E(s_m)≥ord_E(\mathfrak a_m), obtains Θ_m+dd^c w_m=[D_m]/m≥0 and passes to a positive current via normalized compactness. The limit b_i(m)/m→τ_{Y,u}(E_i) is an explicit dependency on Theorem 20.3.2, not inferred from matching title or number. The Gauduchon pairing gives the degree inequality; its converse is correctly refuted by the infinite-order unitary flat bundle on an elliptic curve (lines 210–213). Bergman/L2 constructions in this section remain unreviewed.

**§15.10 selected conditional tail.** Lines 58–104 choose bounded positive smooth f_j→f in L¹(ν); conditional on the existing fixed reference mixed inequality, write u_j=v_j+M_j and use the bound ∫θ_{v_j}∧θ_ψ^{n−1}≤C_ψ. If M_j→∞, the positive limit of ∫e^{λv_j/n}f_j^{1/n}dν contradicts that bound. The inequality |f_j^{1/n}−f^{1/n}|^n≤|f_j−f| and boundedness of the normalized exponentials justify this passage. The last L¹(ν) estimate, combined with common domination, identifies the limiting measure. This is **not** a certification of the antecedent smooth approximation/existence in lines 26–56; that excluded input remains deferred-by-user.

## Dependency and disposition ledger

- **Unresolved nonexcluded external/internal proof-chain checks:** §§12.3.2, 12.11.1, 12.6.32, 14.2.1 (Gauduchon derivative, closed-nef formula and balanced product construction); the nef-and-big Kähler-current existence invoked at §12.12 line 75; §§20.3.2 and 5.25.2 (trace limits and normalized quasi-psh compactness); §15.9.4 and §5.29.20 (common-domination capacity/trace bound). Each is a named mathematical input, not merely an historical attribution.
- **Deferred-by-user, never certified/resolved:** the Demailly approximation/regularization programme and its Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof programme. The §15.10 upstream smoothing and §19.8 dedicated Bergman/L² passages were **not** reopened. Preserve all prior notes as deferred, not repaired.
- **No genuine duplicate, no newly confirmed false printed theorem, and no full transitive certificate** from this run. No change to canonicalizations, proof registry, source manuscripts, permanent tags, main, GitHub Actions, CI, build or published site.
