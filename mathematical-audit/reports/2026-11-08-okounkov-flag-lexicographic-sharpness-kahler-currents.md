# Rank-two flag valuation: lexicographic monotonicity cannot be coordinatewise

**Finding:** POME-OKO-FLAG-LEX-NONCOORDINATE-001  
**Date:** 2026-11-08  
**Severity:** low  
**Status:** verified conditional deduction (sharpness of the printed hypotheses/conclusion; **no printed theorem is false**)  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272  
**Review branch:** review/mathematical-audit

## Integrated anchors checked

- Chapter 19, §19.3, integrated HTML: docs/sections/the-theory-of-okounkov-bodies--flags-and-valuations/index.html, main blob 9190d2ae0d3e51ca0ca965000cb9b5b2ec965c85.
- Smooth flag, Definition 19.3.5: source sgpt:8623A0C4, permanent tag 46E1CFFE3502, physical lines 50–56.
- Current-valued flag valuation, Definition 19.3.6: source sgpt:F2145CC7, permanent tag 78704BB19535, physical lines 59–72.
- Lexicographic monotonicity and its proof, Proposition 19.3.9(1) / equation (19.3.10): source sgpt:8C1D8954, permanent tag EF8E476D98F4; equation source sgpt:4904264E, permanent tag 98CF17AA36AD, physical lines 112–142. The proof explicitly branches on equality/strict inequality of the first generic Lelong numbers.
- Trace context only: Proposition 20.2.21, source sgpt:F53735CE, permanent tag F2C3DD7D449E, docs/sections/the-trace-operator/index.html, blob 1f3a3e4f0317a308b43bd3df53dda84c5f3fa50a, lines 350–377. This report uses a direct analytic-singularity restriction instead of claiming verification of the general trace theorem.
- Normalization: the reading edition uses dd^c = (i/2π) ∂∂̄, so dd^c log|f|² = [div(f)] locally.

## Precise assertion (not an assertion printed by Pome)

For every real 0 < a < 1, there exist **cohomologous Kähler currents** T_a, S_a in the Fubini–Study class on X = P², and a smooth flag X ⊃ H ⊃ {p}, such that their globally normalized quasi-psh potentials satisfy

    φ_T ≤ φ_S

pointwise, so in particular T_a is no less singular than S_a both in the ordinary singularity preorder and in the ideal preorder used in Proposition 19.3.9(1), yet

    ν_flag(T_a) = (a, 0),       ν_flag(S_a) = (0, a).

Thus the printed lexicographic inequality is strict and valid, but a hypothetical coordinatewise inequality fails already in the second coordinate. The phenomenon persists with a uniform positive smooth part (1-a)ω in both currents, identical cohomology classes, and analytic singularities.

## Full calculation

Let [Z_0:Z_1:Z_2] be homogeneous coordinates, put

    Σ = |Z_0|² + |Z_1|² + |Z_2|²,
    H = {Z_1 = 0},      p = [1:0:0] ∈ H,
    ω = ω_FS.

In an affine chart, ω = dd^c log Σ in the corresponding local trivialization. Define globally well-defined upper-semicontinuous ω-psh potentials

    u = log(|Z_1|²/Σ),
    v = log((|Z_1|² + |Z_2|²)/Σ).

Both ratios are invariant under rescaling homogeneous coordinates; u ≤ v. Put

    T_a = ω + dd^c(a u),
    S_a = ω + dd^c(a v).

Poincaré–Lelong gives

    T_a = (1-a)ω + a[H].

Also set B = ω + dd^c v. In the affine chart Z_0 ≠ 0, writing x = Z_1/Z_0 and y = Z_2/Z_0,

    B = dd^c log(|x|² + |y|²).

This is a positive current; outside p it is a smooth semipositive (1,1)-form, and it extends positively across p because log(|x|²+|y|²) is psh and locally integrable. On the charts Z_1 ≠ 0 or Z_2 ≠ 0, the same positivity follows directly from the local expression dd^c log(1+|w|²). Thus B is globally positive, with cohomology class [ω] and no generic divisorial mass on H. Therefore

    S_a = (1-a)ω + a B.

For 0<a<1 both currents dominate (1-a)ω > 0 and belong to the same de Rham/Bott–Chern class [ω]. Their singularities come from finite analytic sums of squared holomorphic functions. Since u ≤ v (globally, with the same reference form), the ordinary singularity preorder is verified *without* relying on a trace theorem; it implies the relevant ideal preorder. In the convention of (19.3.10), T_a ≼_I S_a.

We now compute the flag valuations by the displayed recursive Definition 19.3.6.

**First coordinate of T_a.** The generic Lelong number along H is a, since [H] has coefficient a while ω is smooth. After removing a[H], the residual is (1-a)ω. Its restriction to H is smooth, and its Lelong number at p is zero. Consequently ν_flag(T_a)=(a,0).

**First coordinate of S_a.** The current B has no generic Lelong mass along H: around a generic point (0,y_0) with y_0≠0, log(|x|²+|y|²) is smooth. Hence ν(S_a,H)=0.

**Second coordinate of S_a.** Because the generic Lelong number on H vanishes, the trace is directly represented by restricting the analytic local potential. On H near p (x=0),

    log(|x|²+|y|²)|_{x=0}=log|y|².

Accordingly, as currents on the compact curve H≅P¹,

    Tr_H(S_a) = (1-a)ω|_H + a[p].

One can see this globally as ω|_H+dd^c(a log(|Z_2|²/Σ|_H)); Poincaré–Lelong turns the second term into a([p]-ω|_H). Its Lelong number at p is a. Thus ν_flag(S_a)=(0,a).

The two valuation vectors satisfy

    (a,0) >_lex (0,a),   but    0 < a

in the second coordinate. The latter is a rigorous contradiction to *coordinatewise* monotonicity, not to Proposition 19.3.9(1), which asserts only lexicographic monotonicity.

## Dependency and interpretation

The printed induction at lines 135–142 first compares generic divisorial coefficients. It invokes the trace order theorem only **if these coefficients are equal**. The example shows why one must not continue comparing the later coordinates after a strict first-coordinate inequality: stronger singularity along H may leave **less** residual singularity at the marked point than a current without a generic H-component.

No theorem/proof in §19.3 or §20.2 has been proved false. The general trace comparison, ideal-equivalence, and modifications/valuation correction dependencies remain outside this narrowly checked model and are **not certified** by it. The two-blowup flag correction findings previously recorded in this repository are logically distinct and untouched.

**Proposed correction/addition:** Optional short remark after Proposition 19.3.9(1), with the above P² example and explicit Kähler-current parameter 0<a<1, explaining that “≥_lex” cannot be replaced by the product order even for cohomologous analytic-singularity Kähler currents. No modification of the original statement, proof, attribution, permanent tags, source repository, or canonicalization is warranted.

**Affected dependents:** Any attempted strengthening of §19.3.9 to coordinatewise singularity monotonicity, or an induction that omits its equal-first-Lelong-number branch. This report does **not** classify any printed downstream statement as false.

## Coverage and exclusions

New proof-level selected check of Definition 19.3.5–6, Proposition 19.3.9(1), and the analytic-flag trace in this explicit P² example. The text of Proposition 20.2.21 was inspected for hypothesis alignment only. This is an **incremental visit** to the previously partially audited §19.3; it is **not** an entire-section verification, a proof of the general trace proposition, or a verification of §19.3.12–22. The fresh main table of contents has 25 chapters and 747 uniquely numbered sections; zero complete sections certified. Excluded Demailly approximation/regularization, dedicated Bergman, weighted L², Ohsawa–Takegoshi, multiscale atlas, and positivity-loss proof-completion work remain **deferred-by-user**. No build, tests, CI, formalization, or publication were performed.