# Exact ample-threshold and restricted-series model for a previously false Okounkov slice clause

**Date:** 2026-11-01. **Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Reviewed audit branch at start:** `17a53489db0f5e49c9d766038f0b1bbdb01a0824`. **Status:** `POME-OKO-AMPLE-SLICE-THRESHOLD-001` — **low / verified conditional deduction and model-only verified repair**, not a second newly discovered false theorem.

**Scope.** This audit concerns a nonexcluded algebraic section/flag calculation. It does **not** revisit Demailly approximation/regularization, the dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme, or its prerequisites. The historically registered **high / confirmed theorem-clause error** `POME-OKO-SLICE-FALSE-001` remains **unresolved** for Theorem 19.5.4(5); the present note sharpens its mathematical diagnosis and verifies a proposed restricted-series repair in one explicit family only.

## Exact integrated anchors and hypotheses

- `docs/sections/the-theory-of-okounkov-bodies--transcendental-partial-okounkov-bodies/index.html`, `main` blob `a53c6b2f80c3775e9d646f57808425823ec4a4ac`, **physical lines 42–52**: Theorem **19.5.4**, source `sgpt:CE657E18`, permanent tag `E839B4A35A2A`; clause **(5)** source `sgpt:F0C64B11`, permanent clause tag **`111D84FB6B1C`**. As printed it asserts a slice of the Okounkov body of *any big class* equals the **complete** Okounkov body on the restricted divisor, for all sufficiently small positive slicing parameters. The source attributes the theorem to `[DRWNXZ]` and explicitly treats its general proof as a black box. Preserve that historical attribution.
- `docs/sections/the-theory-of-okounkov-bodies--flags-and-valuations/index.html`, blob `9190d2ae0d3e51ca0ca965000cb9b5b2ec965c85`, **lines 9–38**: Definition **19.3.2**, source `sgpt:D3CA5409`, permanent `F1312787FCC5`, for the successive flag valuation.
- `docs/sections/the-theory-of-okounkov-bodies--algebraic-partial-okounkov-bodies/index.html`, blob `c661e264cab0995a2a344453039940028feff8e0`, **lines 113–117**: algebraic Okounkov body Definition **19.4.8**, source `sgpt:32C6E06F`, permanent `0114DCC2E021`. The comparison of this algebraic body with the book's transcendental/current-defined body is an **upstream identification**, not independently certified here.

## The blowup family and exact monomial valuation semigroup

Fix `p=[0:0:1]` in `P²_[x:y:z]`, and let `pi:X=Bl_p P² -> P²`. Write `H=pi^*O(1)`, `E` for the exceptional curve, and `F` for the strict transform of the line `y=0`, so `F=H-E`, `F²=0`, `H.F=E.F=1`. Take the flag `X superset F superset {q}`, where `q=[1:0:0]` and `r=E intersect F` is the **different** point over `p`. For each rational `0<=epsilon<1`, set `D_epsilon=H-epsilon E`. For `0<epsilon<1`, this divisor is ample: the blowup embeds in `P² x P¹` by the point and the pencil direction, and `D_epsilon=(1-epsilon)H+epsilon F` pulls back a strictly positive product Fubini–Study form. At `epsilon=0`, `H` remains big and nef but not ample.

Let `m>0` clear the denominator of `epsilon`, and put `b=m epsilon`, an integer with `0<=b<m`. Then `H^0(X,mD_epsilon)` is exactly the space of homogeneous degree-`m` polynomials vanishing at `p` to order at least `b`. A monomial `x^a y^k z^ell`, with `a+k+ell=m`, is admissible precisely when `a+k=m-ell >=b`. The flag valuation along `F` and at `q` is **exactly** `(k,ell)`: after dividing the equation `y^k`, the restriction to `y=0` is a nonzero multiple of `x^a z^ell`, with order `ell` at `q`. For a general polynomial, use its smallest nonvanishing `y`-degree and then the smallest `z`-degree; the condition that every monomial vanishes at `p` to order >=b rules out cancellation producing an inadmissible valuation.

Thus the **complete** section-value set in degree `m` is

```text
{ (k,ell) in Z_>=0^2 : 0 <= k <= m, 0 <= ell <= m-max(k,b) }.
```

Every admissible pair is attained by the monomial `x^(m-k-ell) y^k z^ell`; no saturation or unspecified approximation is needed. Taking normalized values over divisible `m`, and then the closure, gives the exact convex body

```text
Delta_(F,q)(D_epsilon) = { (t,s) : 0 <= t <= 1,
                                    0 <= s <= 1-max(epsilon,t) }.
```

At each fixed `0<t<1`, its slice is `[0,1-max(epsilon,t)]`. By intersection theory the **complete** restricted divisor on `F=P¹` has degree

```text
deg( (D_epsilon-t F)|_F ) = (H-epsilon E-t F).F = 1-epsilon.
```

Therefore the complete curve Okounkov body on the right of the **printed** clause (5) is `[0,1-epsilon]`, independent of `t`. Equality holds **if and only if `0<t<=epsilon`**, while **every** `epsilon<t<1` gives a strict inclusion. In particular, at the previously registered big-nef endpoint `epsilon=0`, the printed clause is false for **every** small `t>0`; when `epsilon>0` is fixed and ample, it is correct in this model for `0<t<=epsilon`. The allowable threshold tends to zero with `epsilon`; no class-uniform positive threshold is available along this degeneration.

Sanity checks independent of the disputed slice formula: the body is a trapezoid of area `(1-epsilon^2)/2`, exactly `D_epsilon²/2` since `H²=1, H.E=0, E²=-1`. This checks the **model** of Theorem 19.5.4(1), without proving its general volume identity.

## Verified restricted-section-series correction (only in this model)

Take a rational `t=k/m` with `0<=k<=m` and `b=m epsilon`. Restrict sections after **exact** order `k` vanishing along `F`; the relevant bundle on `X` is

```text
L_(m,k) = m D_epsilon-k F = (m-k)H+(k-b)E.
```

Its complete restriction to `F` has degree `m-b` regardless of `k`, hence `H^0(F,L_(m,k)|_F)` has dimension `m-b+1`. But the image of the global restriction map is

```text
Im[ H^0(X,L_(m,k)) -> H^0(F,L_(m,k)|_F) ]
 = { u : ord_r(u) >= max(k-b,0) }.
```

**Proof:** If `k<=b`, then `L_(m,k)=(m-k)H-(b-k)E`: degree-`m-k` plane polynomials vanishing to order `b-k` at `p` restrict, after removal of that exceptional twist, surjectively onto degree-`m-b` sections on the strict-transform line. The monomials `x^(m-k-ell)z^ell` for `0<=ell<=m-b` exhibit every valuation at `q`. If `k>b`, then `L_(m,k)=(m-k)H+(k-b)E` has the fixed exceptional factor `(k-b)E`; its restriction to `F` vanishes to order at least `k-b` at `r`, and the unrestricted degree-`m-k` plane monomials show this is the sole restriction. In both cases the image dimension is `m-max(b,k)+1`, and its valuations at `q` are precisely `0,...,m-max(b,k)`. Thus the **restricted-image graded series** has rescaled Okounkov interval `[0,1-max(epsilon,t)]`, agreeing exactly with the left-hand slice for all rational parameters in the model, unlike the complete series.

This establishes a **model-level** correction, **not** a general theorem with a replaced RHS: a general restricted-series/transcendental trace equality may require extra hypotheses and external input. The existing `POME-OKO-SLICE-FALSE-001` finding remains **high / confirmed error and unresolved**; do **not** mark it repaired or claim that its printed big-class statement becomes true. Any production proposal should state an asymptotic-surjectivity hypothesis or replace the full restricted body by the actual restricted-image series/trace, verify the general theorem and source attribution, and be submitted separately for review.

## Small exact check, scope, and dependents

An accompanying **standard-library-only** enumeration in `mathematical-audit/checks/okounkov_ample_slice_threshold.py` checks the flag valuations against the stated integer inequalities for `(m,b)=(5,0),(5,2),(8,3),(12,9)`; this is a finite model crosscheck, not formal proof or repository test suite. No approximation, CI, build or website publication was run.

**Actual new mathematical work:** an exact two-parameter (ample to nef) monomial valuation semigroup, sharp class-dependent slice threshold, the complete-versus-restricted-image dimension deficit, and independent volume check, focused on Theorem 19.5.4(5). Definitions §§19.3.2 and 19.4.8 were checked as hypotheses/notation; §§9.25, 16.1, 16.2, 16.10 were direct navigation-only contextual rereads, already inventoried historically, **not** newly certified mathematical sections. No other §19.5 theorem clauses or surrounding general trace/regularization theory were reverified. The general transcendental/algebraic body identification remains conditional.

**Affected dependents:** any use of a complete restricted Okounkov body in place of the first-coordinate slice, including discussions stemming from §19.5.4(5), trace/restriction in §20 and slicing arguments in §19.4–19.6. Preserve separate analytic versus algebraic variants, source labels and permanent tags. No claim is made that clauses 19.5.4(1)–(4) are false or that §19.5.32, which uses a Kähler case, is refuted.

**Coverage boundary:** actual current table of contents contains **25 chapters and 747 numbered sections**; **zero** entire mathematical sections are certified. All past resolved, unresolved, candidate, external-input and user-deferred statuses are carried forward unchanged. Work on Demailly approximation/regularization, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale atlas and positivity-loss remains **deferred-by-user**, neither resolved nor audited. This report is audit-only; no source, body, registry, tag, main branch, build, CI, formalization or publication changes.
