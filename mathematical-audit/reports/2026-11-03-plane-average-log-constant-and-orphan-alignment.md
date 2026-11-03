# Exact sphere logarithm and an orphan alignment in the complex-plane average

**Date:** 2026-11-03. **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Production reading file:** `docs/sections/real-currents-submersions-and-homotopies--averaging-complex-planes/index.html`, blob `2245f2fee90247cc55a3b57b9b41e0af135abcd1`. **Scope:** first selected proof-level analysis of nonexcluded §5.57, not a complete proof certification of §5.57 or its Poincaré–Lelong and current-theory dependencies. Dedicated Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss work is excluded, deferred by the owner, and not examined.

## POME-PLANE-SPHERE-LOG-HARMONIC-001 — low — verified conditional deduction

**Pinned statement:** Lemma 5.57.1, source `demailly-complex-geometry:B58E58A0`, permanent `F08E0D60DA23`, physical lines 7, 11–21 and proof lines 26–46. Its Equation 5.57.2 has source `demailly-complex-geometry:A38ACD30`, permanent `6A107C250306` (lines 12–14); Equation 5.57.3 has source `demailly-complex-geometry:79B51C09`, permanent `F0FBE5A138FA` (lines 17–19). Background convention is `dd^c=(i/2π)∂∂̄`; here the calculation uses only invariant **probability** on the unit sphere.

**Hypotheses and exact result.** For `n≥1`, `z≠0`, and normalized unitary-invariant probability `σ` on `S^{2n-1}⊂C^n`, put `a=|z|²>0` and `H_{n-1}=Σ_{j=1}^{n-1}1/j`, with `H_0=0`. Then the previously unspecified constant is exactly
[
\boxed{c_n=-H_{n-1},\quad C_n=H_{n-1},\quad
\int \log|\langle z,\xi\rangle|^2,d\sigma
=\log a-H_{n-1}.}
]
More precisely, if `n≥2`, the random variable `U=|⟨z/|z|,ξ⟩|²` has density `(n-1)(1-u)^{n-2}du` on `0<u<1`. Consequently
[
\int |\log|\langle z,\xi\rangle|^2|,d\sigma=
\begin{cases}
-\log a+H_{n-1},&0<a\leq1,\\
\log a-H_{n-1}
 +2(n-1)\displaystyle\sum_{k=0}^{n-2}
 (-1)^k {n-2\choose k}\frac{a^{-(k+1)}}{(k+1)^2},&a>1.
\end{cases}
]
For `n=1`, the absolute-log integral equals `|log a|` for every `a>0`. The printed inequality (5.57.3) is **correct and has the sharp smallest global additive constant `H_{n-1}`**, attained for all `0<a≤1`. For `n≥2` and `a>1` its triangle-inequality bound is strict.

**Independent proof.** Unitary invariance reduces to `z=|z|e_1`. Take independent standard complex Gaussian coordinates `G_j` and normalize `ξ=G/|G|`; this realizes the unitary-invariant probability. For `n≥2`, `R=|G_1|²` and `S=Σ_{j=2}^n|G_j|²` are independent with exponential and shape-`n−1` gamma densities. The elementary transformation `(R,S)↦(U=R/(R+S),T=R+S)` gives the stated beta density; its distribution function is `P(U≤u)=1-(1-u)^{n-1}`. By Tonelli,
[
E[-\log U]=\int_0^\infty P(U<e^{-s}),ds
=\int_0^1\frac{1-(1-u)^{n-1}}{u},du
=\sum_{j=1}^{n-1}\frac1j.
]
This proves the exact logarithmic constant and finiteness without invoking sphere-coordinate integrability as an unproved premise. When `a≤1`, `log(aU)≤0` almost surely, proving the first absolute-value formula and sharpness. When `a>1`, use `|x|=x+2(-x)1_{x<0}` with `x=log(aU)` to obtain
[
E|\log(aU)|=\log a-H_{n-1}
+2(n-1)\int_0^{1/a}[-\log(au)](1-u)^{n-2},du.
]
Expand the integer binomial, and use `∫_0^{1/a}u^k[-log(au)]du=a^{-(k+1)}/(k+1)^2`. This yields the finite sum. For `a>1` and `n≥2` the two terms `log a>0` and `log U<0` have opposite signs on a set of positive probability, so the published triangle bound is strict. At `n=1`, `U=1` identically.

**Additional normalization crosscheck, no new independent theorem claim.** Proposition 5.57.4 (source `demailly-complex-geometry`, permanent `522ECB915F74`, physical lines 51–84) uses `∫_{S∩B_r}β^q=r^{2q}`. Directly in any unitary `q`-plane, `β^q=(q!/π^q)dV_{2q}`, while `Vol(B_r^{2q})=π^qr^{2q}/q!`; their product is `r^{2q}`. For `q=0` this is unit origin mass. The theorem's `A_0=δ_0` endpoint (source `demailly-complex-geometry:5B5618BA`, tag `AB7EED2588E5`, lines 139–151) is consistent with this normalization. We read, but **did not independently certify**, the entire plane-integration, Poincaré–Lelong, coefficient-Fubini and recursive-current chain (lines 69–151).

**Recommended change:** optional short remark after Lemma 5.57.1 giving `C_n=H_{n-1}` and explaining sharpness. This is an enhancement, **not a false printed mathematical statement or a verified applied source repair**. Its downstream dependencies include the integrability bound in the proof of Lemma 5.57.7, physical lines 109–116, and the averaged current recursion in Theorem 5.57.11; those remain conditional on their printed justifications.

## POME-PLANE-AVERAGE-ORPHAN-ALIGN-001 — low — confirmed error (reading-edition equation rendering)

**Precise locus:** The **same main** §5.57 reading page at physical **line 155**, standalone trailing reading chunk `entry-128DDD633F87`, source `demailly-complex-geometry:26C290A4`, permanent tag `128DDD633F87`. The chunk reproduces only the second/right-hand line of equation `(5.57.10)` after the proof of Theorem 5.57.11 has ended (lines 150–154). The already integrated canonical **two-line estimate** appears in the proof of Lemma 5.57.7 at **lines 109–116**, with `\begin{align}...\tag{5.57.10}\end{align}` at line 113. The trailing fragment instead contains literal nested incompatible math environments `\[\begin{aligned}\begin{align}...\tag{5.57.10}\end{align}\end{aligned}\]`. It is a genuine **duplicated and malformed displayed equation**, not a second mathematical assertion, and not a demonstrated defect in the inequality.

**Proposed reviewable fix, NOT applied:** preserve the source's permanent tag and provenance via an alias to canonical Eq. 5.57.10, or render the extra source entry as an intentional linked reference without a second malformed display. Check all permalinks before a separate integration patch. Do not delete its tag, rewrite the mathematical source, or change `main` as part of the audit. There is a similar orphan-alignment finding in §7.30, **POME-HAUS-ORPHAN-ALIGN-001**, but this is a distinct source label and page; it is not counted as that earlier finding or as a new mathematical counterexample.

## Coverage/status boundary

This is **first selected actual mathematical proof-level coverage** of §5.57, an existing current-ToC row previously marked only by its section title. The directly audited items are the exact sphere-log distribution/moment and normalization in Lemma 5.57.1 and Proposition 5.57.4; Theorem 5.57.11 and Lemma 5.57.7 were read to locate the dependence and dangling duplicate only. No entire mathematical section or transitive current-theory proof chain is certified. Existing resolved/unresolved/external/deferred ledgers remain unchanged, especially owner-excluded Demailly approximation/regularization and its dedicated Bergman/weighted-L²/OT/multiscale/positivity-loss programme. Report and ledger are proposed **audit Markdown only**, with no source/body/registry/canonicalization/permanent-tag/test/build/CI/site publication.
