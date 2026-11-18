# 2026-11-19 — Whole-section mathematical audit of §3.6 and a variable-obstacle real-trace lemma

## Exact source and scope

- Reviewed production `main`: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- Integrated reading edition: `docs/sections/separate-harmonicity-and-subharmonicity/index.html`, blob `1d3c9ebe0d7093f0f069dc2b25b0a47f700f907a`, **physical lines 7–93**. The section consists of two statements with their printed proofs and one intervening real-trace argument; all were read directly.
- Theorem 3.6.1: source label `klimek-pluripotential-theory:F1182878`, permanent tag `58AAF98CC15E`, printed statement lines 7–9, proof lines 11–35.
- Real-trace argument: unnumbered material, physical lines 37–46, particularly the constant-obstacle conclusion at lines 40–46.
- Theorem 3.6.2: source label `klimek-pluripotential-theory:BDD09117`, permanent tag `95AFE3B73B3D`, printed statement lines 49–51, proof lines 53–93; the coefficient argument occurs in lines 60–82 and the Baire propagation in lines 84–90.
- Chapter placement: §3.6 in Chapter 3 of the published table of contents. This is a **new whole-section direct reading**, not a completed transitive certification of its analytic dependencies.

## New finding: `POME-REALTRACE-VARIABLE-OBSTACLE-HARTOGS-001`

**Classification:** low severity; **verified conditional deduction**. No false printed theorem and no independently confirmed proof gap. The deduction uses the real-cube pluriregularity and the psh-envelope discrepancy fact invoked in printed §3.6, lines 37–46; those upstream results have not been transitively certified in this audit.

**Statement.** Let `D` be an open subset of the totally real locus `R^p` in `C^p`, and let `Ω` be a complex neighborhood of `D`. Suppose `v_j ∈ PSH(Ω)` is a sequence **locally uniformly bounded above** (allowing identically negative-infinite members). Let `g:D→R` be continuous and suppose, for every `x∈D`,
`
limsup_(j→∞) v_j(x) ≤ g(x).
`
Then for every compact `K⊂D`,
`
limsup_(j→∞) sup_(x∈K) [v_j(x)-g(x)] ≤ 0.
`
Equivalently, for each `ε>0`, `v_j(x)≤g(x)+ε` for all `x∈K` and all sufficiently large `j`. No lower estimate is implied, and the statement concerns **sequences**, not arbitrary nets.

**Complete deduction.** Fix `ε>0` and compact `K⊂D`. By uniform continuity of `g` near `K`, cover `K` by finitely many interiors of closed real cubes `Q_i` each lying strictly inside a slightly larger real cube `Q'_i⊂D`, with `osc_(Q'_i) g<ε/2`. Put `A_i=sup_(Q'_i)g`. The pointwise hypothesis implies `limsup_j v_j(x)≤A_i` for every `x∈Q'_i`. Apply the **constant-obstacle real-trace Hartogs principle** established in §3.6, lines 37–46, on `Q'_i`, with the smaller compact cube `Q_i` and tolerance `ε/2`. For each `i` there is `N_i` such that
`
v_j(x)≤A_i+ε/2≤g(x)+ε   (x∈Q_i, j≥N_i).
`
Taking the maximum of the finitely many `N_i` proves the assertion. The dependency on pluripolar discrepancy is used **only** through the already printed constant-obstacle principle; it is not silently treated as self-evident.

**Holomorphic-coefficient corollary (uniform variable-radius root test).** Let `F_j:Ω→C^{N_j}` be finite holomorphic tuples (their dimensions may vary), with `j^{-1}log∥F_j∥` locally uniformly bounded above. If `R:D→(0,∞)` is continuous and
`
limsup_(j→∞) (1/j) log∥F_j(x)∥ ≤ -log R(x)
`
at each real point, then for every compact `K⊂D` and `ε>0`,
`
∥F_j(x)∥ ≤ [exp(ε)/R(x)]^j
`
uniformly for `x∈K` and all sufficiently large `j`. Indeed, `j^{-1}log∥F_j∥` is psh (or identically negative infinite on a component), and the statement above applies with `g=-log R`. This explicitly extends the **fixed** radius `R` used for harmonic expansion coefficients in printed lines 66–82 to a continuous variable radius; it neither changes the theorem's hypotheses nor asserts uniform bounds on noncompact real sets.

**Suggested optional insertion:** after the real-trace paragraph at printed line 46, record this variable-obstacle consequence as a short lemma and use it only when a variable admissible radius is needed. Do not edit the published body or any permanent tag in the audit branch.

**Dependents:** Theorem 3.6.2's harmonic-coefficient compact propagation (lines 76–82) uses the original constant-obstacle estimate and remains unchanged; later arguments that use psh log-norms of holomorphic families may optionally use the variable-obstacle version. Theorem 3.6.1 does not depend on this new lemma.

## Direct scrutiny of printed Theorem 3.6.1

1. **Majorant reduction (lines 14–20).** The two successive submean inequalities bound `u(x,y)` by the average of `M^+` on a fixed compact product. At this stage joint measurability of `u` is not assumed: each slice is measurable, and Fubini is applied to the integrable majorant rather than to an unproved jointly measurable `u`. This order is essential and is observed in the text.
2. **Joint upper semicontinuity (line 22).** Given `(x_j,y_j)→(x,y)`, the `y`-slice compactness alternative, an almost-everywhere subsequence, and the moving-point Hartogs bound yield the desired upper inequality. If the limiting slice is identically negative infinite, the nondegenerate `L^1` alternative is ruled out.
3. **Local integrability (lines 24–30).** If a nontrivial separately subharmonic function were negative infinite on a whole open product, the slice identity theorem propagates this to the full connected product. A finite point `(a,b)` provides a nondegenerate `y`-slice. The integral estimate for `u^-` then gives local integrability jointly, after joint upper semicontinuity has established measurability.
4. **Distributional closure (line 32).** Fubini now legitimately gives `Δ_xu≥0` and `Δ_yu≥0`; hence `Δu≥0`. Product radial smoothing is decreasing in both radii and recovers the canonical upper-semicontinuous representative. The printed statement is not contradicted.

No new defect is confirmed. **Conditional analytic inputs:** the local subharmonic compactness/Hartogs principle, a.e.-to-everywhere domination for subharmonic representatives, and canonical radial smoothing/decreasing limits. These were used, but no complete transitive certification is asserted.

## Direct scrutiny of printed Theorem 3.6.2

1. **One-dimensional factor (line 56).** Separate harmonicity in a one-dimensional real factor means affine dependence on that factor; two evaluations recover coefficient functions harmonic in the remaining variables.
2. **Bounded strip (line 58).** Theorem 3.6.1 gives joint local integrability on the strip; distributional cancellation of both partial Laplacians and Weyl's lemma yield joint harmonicity. The identification with the original pointwise separately harmonic function uses iterated uniqueness of harmonic representatives, not an unjustified a.e.-to-everywhere assertion.
3. **Coefficient control (lines 60–82).** Expansion in solid spherical harmonics in the `y`-variable gives the pointwise exponential radius bound; the Poisson kernel controls its polynomial-in-degree prefactor. The coefficient functions are harmonic in `x`, so they admit holomorphic extensions to a common smaller complex neighborhood with locally geometric bounds. The log of the finite-dimensional coefficient norm is psh; the printed real-trace estimate upgrades pointwise spectral radius to a compact-uniform one, justifying re-summation on smaller `y`-balls.
4. **Baire start and path propagation (lines 84–90).** Each `E_j={y:|f(x,y)|≤j for all x∈X̅}` is relatively closed in the compact `y`-ball, since each fixed-`x` slice is continuous. It covers that ball because each fixed-`y` `x`-slice is continuous and bounded on `X̅`. Baire gives a genuinely open strip; the positive boundary distance on a compact path permits finitely many propagation steps.

No new false theorem or independently confirmed proof gap is found. **Conditional inputs:** the real-cube relative extremal regularity, psh-envelope discrepancy outside pluripolar sets, holomorphic extension bounds for harmonic functions on a real ball, the relevant harmonic expansion/Poisson estimates, Baire and Weyl. These are not newly certified just because their use in this proof is coherent.

## Limits, coverage and actions

- Entire integrated §3.6 read directly (both theorems, both printed proofs, and intervening real-trace passage). §3.7 was checked only for the contrast with its separately subharmonic example and its previously recorded failure of local `L^1` control; §3.7 is **not** recertified or counted.
- **+1 entire directly read section; +0 fully checked transitive proof chains.** First-visit count is not asserted without recomputing the full historical matrix.
- No Demailly approximation/regularization or its dedicated Bergman, weighted-L2, Ohsawa–Takegoshi, multiscale-atlas or positivity-loss programme was examined. Existing notes on these topics remain **deferred-by-user**, not resolved.
- No tests, build, CI, browser checks, production-body edit, canonicalization edit, main-branch edit, or publication performed. This note is a mathematical audit, not a formal verification claim.
