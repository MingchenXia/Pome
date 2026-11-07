# Bounded half-space harmonic functions: unique (L^infty) Poisson traces

**Finding:** `POME-HALFSPACE-BOUNDED-POISSON-ISOMETRY-001`  
**Severity/status:** low / **verified conditional deduction** (not a false printed theorem; no claim of a fully certified upstream proof).  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (2026-11-07).  
**Integrated reading file:** `docs/sections/kelvin-transforms-and-half-space-potentials/index.html`, blob `f2615a5393af724c3996978212162f94911ff9d9`, physical lines **55–75, 80–136, 138–180**.  
**Internal measure input:** `docs/sections/measures-and-distributions--densities-and-differentiation-of-integrals/index.html`, blob `1b600ca8444edebc8e05e300cb86ae371e9f8535`, physical lines **7–46**.  
**Stable labels:** Theorem 3.2.6, source `classical-potential-theory:1C8A330A`, permanent `6BC86EEF03A9`; Equation 3.2.7, source `classical-potential-theory:C0A46F1A`, permanent `F3ED29BBAD39`; Equation 3.2.8, source `classical-potential-theory:358F89A3`, permanent `8F7C774A9D89`; Theorem 3.2.12, source `classical-potential-theory:BB6DAC3F`, permanent `9ADD2DF19642`; Poisson normalization (3.2.13), source `classical-potential-theory:E7E82020`, permanent `AB2849CD8791`; Lemma 2.8.1, source `foundations-of-pluripotential-theory:43819F13`, permanent `9790D3B21542`.

## Precise assertion

Let (dge2), (H=mathbb R^{d-1}	imes(0,infty)), and
[
p_t(x')=rac{2t}{s_{d-1}(|x'|^2+t^2)^{d/2}}.
]
Write (mathscr H_b(H)) for the **real-valued bounded harmonic functions** on (H), with their supremum norm. The Poisson map
[
 mathcal P:L^infty(mathbb R^{d-1},dx')longrightarrowmathscr H_b(H),
 qquad flongmapsto ig[(x',t)mapsto (p_t*f)(x')ig]
]
is a linear **isometric bijection**. Every bounded harmonic function therefore has a unique almost-everywhere bounded boundary trace; its representing measure in Theorem 3.2.6 (after shifting the function by a constant to make it nonnegative) is absolutely continuous. Neither a singular boundary measure nor a nonzero (ct) term can occur for a bounded nonnegative harmonic function.

This is a strengthening, for the bounded-harmonic class, of the printed correct Theorems 3.2.6 and 3.2.12. The latter expressly allows a nonzero linear term because its conclusion concerns the unbounded growth class as well.

## Direct proof, including the noncompact boundary tail

Put (m=d-1). By (3.2.13), (int_{mathbb R^m}p_t=1). Its scaling (p_t(x)=t^{-m}p_1(x/t)), positivity, and integrability show that (p_t) is an approximate identity. For every (arphiin C_c(mathbb R^m)), (p_t*arphi	oarphi) uniformly (split the integral into (|y|<delta) by uniform continuity and (|y|gedelta) by the integrable tail of (p_1)).

**Positive bounded case.** Suppose (0le hle M) on (H). By Theorem 3.2.6, (h(x',t)=ct+int p_t(x'-z)d
u(z)) with (cge0), (
u) a positive Radon measure, and
[
  int_{mathbb R^m}(1+|z|^2)^{-d/2},d
u(z)<infty.
]
Since (ctle M) for every (t>0), necessarily (c=0).

For nonnegative (arphiin C_c^infty(mathbb R^m)), Tonelli gives
[
 I_t:=intarphi(x')h(x',t),dx'
     =int(p_t*arphi)(z),d
u(z)le Mintarphi,dx'.
]
We justify (I_t	ointarphi,d
u), **without** incorrectly applying finite-measure weak convergence to the generally infinite total measure (
u). Choose (Rge1) such that (operatorname{supp}arphisubset B_R). On (|z|le2R), convergence (p_t*arphi	oarphi) is uniform, and (
u(overline B_{2R})<infty). For (0<tle1) and (|z|>2R), (|z-x'|ge |z|/2) on the support of (arphi), whence
[
 0le(p_t*arphi)(z)le C_{arphi,R},t(1+|z|^2)^{-d/2}.
]
The tail is at most (C_{arphi,R}tint(1+|z|^2)^{-d/2}d
u), which tends to zero. Thus
[
 intarphi,d
u=lim_{tdownarrow0}I_tle Mintarphi,dx'.
]
By the order characterization of positive Radon measures, (
ule M,dx') on Borel sets. **Lemma 2.8.1** now provides (gin L^infty) with (0le gle M) almost everywhere and (
u=g,dx'). Therefore (h=p_t*g).

**Signed bounded case.** Let (u) be any real bounded harmonic function, (M=|u|_infty). Apply the preceding case to (h=u+M), which satisfies (0le hle2M). We obtain (h=p_t*g) with (0le gle2M). Since (p_t*1=1), (u=p_t*f) with (f=g-M), and (|f|_inftyle M).

**Converse and uniqueness.** The printed Theorem 3.2.12 gives (p_t*finmathscr H_b(H)) and (|p_t*f|_inftyle|f|_infty) for all (fin L^infty). For any (arphiin C_c^infty), Fubini and the (L^1)-approximate-identity property give
[
  lim_{tdownarrow0}intarphi(x')(p_t*f)(x'),dx'
       =intarphi(x')f(x'),dx'.
]
Indeed the difference is at most (|f|_infty|p_t*arphi-arphi|_1	o0); (L^1) convergence follows by the usual translation-continuity argument (or compact/tail splitting). Hence equal harmonic extensions force equal boundary functions as distributions, therefore almost everywhere. Apply this boundary limit to the constructed (f) and the estimate (|u|le M) to recover (|f|_inftyle|u|_infty); combined with the already proved reverse inequality this gives **exact norm equality**.

## Boundary cases, dependency discipline, and affected results

The positive harmonic function (u(x',t)=t) has boundary value zero at every finite boundary point but is unbounded, so a growth restriction genuinely matters. The Poisson kernel for an atomic boundary measure, (u(x',t)=p_t(x')), is nonnegative harmonic with (c=0) but becomes unbounded as ((x',t)	o(0,0)); the boundary density conclusion genuinely requires a uniform harmonic bound. These examples are logically distinct and do not contradict the printed theorems.

**Dependencies:** printed Theorem 3.2.6, normalization (3.2.13) of Theorem 3.2.12, and the **internally proved** bounded-density lemma 2.8.1; standard Tonelli, positivity of Radon measures, and elementary approximate-identity estimates. This report checks the new tail passage and isometry proof, **not** all transitive inputs to the half-space representation or to Radon-measure theory. No Demailly approximation, Bergman, weighted-(L^2), OT, multiscale or positivity-loss argument is used or reopened.

**Classification:** verified conditional deduction, low. Neither printed theorem is false; there is no proposed change to any source/permanent tag. **Optional source-body proposal for separate review:** append a bounded-harmonic Poisson classification corollary after Theorem 3.2.12, including the weighted-tail argument above. Potential consumers include bounded Dirichlet uniqueness on a half-space and interpretation of the (ct) freedom in §3.2.11. No production or registry file was edited.

**Coverage:** new selected proof-level deduction in previously partly audited §3.2, exact displayed statement (3.2.7)–(3.2.8), normalization (3.2.13), and internal Lemma 2.8.1. No first-visit recount, no full-section or upstream-dependency certification. ToC baseline 25 chapters, 747 numbered sections, zero fully certified mathematical sections.
