# Codimension bound for divisorial Jacobian orders; complex-space model audit

**Date:** 2026-10-24, Asia/Shanghai. **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Audit branch at entry:** `88f6d58078d2c10e0759449d16a765157e62b8f6`. This report covers **selected mathematical arguments only**, not a complete section, theorem dependency graph, or project certification.

**Scope confirmation.** Freshly inspected `main/AGENTS.md`, `main/documentation/proof-expansions.md`, the 25-chapter/747-section integrated ToC, and the review branch's `README.md`, `mathematical-audit/LATEST.md`, `SECTION_MATRIX.md`, and `LEDGER.md`. The entire Demailly approximation/regularization, dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme is **deferred-by-user** and was not inspected.

## POME-DIV-JAC-CODIM-001 — verified conditional deduction; low severity

**Exact integrated source:**
- `docs/sections/complex-spaces-and-modifications--connected-fibers-and-resolution-models/index.html`, main blob `6ad8bec31c3089b7eab91f199f5a1eb355a12c40`, Theorem 9.8.6, source label `foundations-of-pluripotential-theory-B4101D74`, permanent tag `373CA5388E72`, lines 119–171, especially Step 2 at 132–141, Step 3 at 143–168, and Step 4 at 171; its Jacobian chain equation 9.8.7, source `foundations-of-pluripotential-theory-9442059A`, tag `D52CB808B809`, lines 136–138.
- `docs/sections/complex-spaces-and-modifications--blowups-and-resolution/index.html`, main blob `f452f4b1abe5cdfe348ae11fcd934febcfdd570b`, Proposition 9.6.3, source `foundations-of-pluripotential-theory-2959F02B`, tag `865FE5EC97E6`, and blowup chart equation 9.6.4, source `foundations-of-pluripotential-theory-5649DBB5`, tag `E62F169B3F9F`, lines 49–69.

**Statement (stronger local estimate, under explicit hypotheses).**
Let `f:Y -> X` be a dominant holomorphic map between smooth complex `n`-folds, with nonzero generic Jacobian. Let `E ⊂ Y` be an irreducible hypersurface, and suppose its image has irreducible analytic closure `Z ⊂ X` of codimension `r`. At a generic smooth point of `Z`, choose target holomorphic coordinates `(z_1,...,z_n)` with `Z={z_1=...=z_r=0}`. Write `a_i=ord_E(z_i∘f)`, `1≤i≤r`. Then `a_i≥1` and

```text
ord_E(J_f) >= (a_1 + ... + a_r) - 1 >= r - 1.
```

In particular any divisor over a smooth base with center of codimension `r` has Jacobian discrepancy at least `r-1`. This is sharp: for a single smooth-center blowup of codimension `r`, Proposition 9.6.3 gives `J_π=unit * t^(r-1)` in its pivot charts.

**Complete local proof.** Work at a general point of `E_reg` mapping to `Z_reg`, avoiding all proper bad loci; because `f` has nonzero generic Jacobian, each `z_i∘f` is nonzero as a holomorphic function locally and has finite order `a_i≥1` along the local defining equation `t=0` of `E`. Thus `z_i∘f=t^{a_i}h_i` with `h_i` holomorphic. Differentiating gives

```text
d(z_i∘f) = t^(a_i-1) (a_i h_i dt + t dh_i).
```

In the wedge of these `r` one-forms, at most one term can use `dt` because `dt∧dt=0`. Every nonzero summand therefore uses `t dh_i` in at least `r-1` slots. Consequently

```text
d(z_1∘f) ∧ ... ∧ d(z_r∘f)
  = t^(a_1+...+a_r-1) * (holomorphic r-form).
```

Wedge with the remaining `d(z_{r+1}∘f),...,d(z_n∘f)`, which have holomorphic coefficients (no negative t powers), and compare with a nonvanishing source coordinate volume form. This proves the bound. All vanishing orders are orders **along the prime divisor at a generic point**, not pointwise orders at a special point. No resolution/regularization approximation theorem is used in the local estimate.

**Refinement of Theorem 9.8.6's termination count.** In its Step 3, let `r` be the codimension of the current center `Z=f(E)` and let `i` be the first principalization stage whose smooth center contains the generic transform of `Z`. At its generic point, that center has codimension `r`; the equation 9.6.4 gives `J_{σ_i}=unit * e_i^(r-1)`. Its pullback to `E'` has `ord_{E'}(e_i∘ρ_i)≥1`. Thus the displayed bound at lines 161–168 sharpens to

```text
ord_{E'}(J_{f'}) <= ord_E(J_f) - (r-1).
```

The other blowup Jacobians contribute nonnegative orders, and the common-smooth-model map has order zero generically along the strict transform, exactly as in the printed chain-rule argument. The proof still depends conditionally on the **quoted Hironaka principalization** at §9.6.7 and on existence of common smooth models, which are not re-certified here. The original theorem and its weaker decrement by one remain correct; the proposed change is an **optional sharper remark**, not a source correction.

**Affected dependents:** valuation center/discrepancy comparisons, extraction of divisorial valuations via blowups (§9.8.4–6), and b-divisor model comparisons in Chapter 20. No direct downstream error identified.

## Other selected checks, with explicit limits

1. **§9.6, Proposition 9.6.2** (`docs/sections/complex-spaces-and-modifications--blowups-and-resolution/index.html`, same blob, lines 23–35): checked the local graph closure, nonzerodivisor cancellation, inversion of the pulled-back ideal and uniqueness of a lift. The potential concern that a *reduced* graph could lose nilpotent structure is **inapplicable**: §9.4 explicitly declares *all complex spaces reduced* (`docs/sections/complex-spaces-and-modifications--reduced-spaces-and-normalization/index.html`, main blob `06439f43d1ce8e83d2529682c9a630bffa3d9c22`, line 10). No counterexample is asserted.
2. **§9.7, Theorem 9.7.5** (`docs/sections/complex-spaces-and-modifications--proper-images-and-relative-principalization/index.html`, blob `b44fe157b8c01363da7799990b8ef6ed82525553`, source `foundations-of-pluripotential-theory-1524D010`, tag `689628C7AF7F`, lines 89–124): checked the restriction of the weak transform to `W_i`, the two-stage principalization, and the codimension of the components of `H`. These steps use Hironaka as an **allowed quoted input**; the entire Remmert–Stein/Remmert induction was not re-proved.
3. **§9.8, Theorems 9.8.1/9.8.6**: checked the connected-fiber contradiction and the Jacobian order bookkeeping, while not certifying the full global extraction algorithm or all analytic-image prerequisites. The finite bimeromorphic normal-target isomorphism, §9.8.2, requires **normality**: a unibranch cusp has a finite bijective normalization map that is not biholomorphic. The original statement includes normality; hence there is no theorem error here.
4. **§9.9, Proposition 9.9.4** (`docs/sections/complex-spaces-and-modifications--plurisubharmonic-functions-on-reduced-spaces/index.html`, blob `d9d8091b530c9843e5a725b49af2400936aeaa3a`, source `foundations-of-pluripotential-theory-A6674849`, tag `B43080BD49F3`, lines 63–90): inspected the codimension-two finite-projection cylinder, normalized curve slices and extension of an upper bound through the remaining bad slices. This is a selected proof check conditional on §9.5 finite projections, §9.7 proper analytic images, and the one-dimensional maximum principle; it is not a complete certification.

**Ledger classification:** only `POME-DIV-JAC-CODIM-001` is new, severity **low**, status **verified conditional deduction**. **No false theorem, new proven proof gap, duplicate, external unsupported input or global certification is claimed.** Previously registered items and all `deferred-by-user` findings remain untouched.

**Executed checks:** exact hand/symbolic exterior-product calculation and its equality test using the printed blowup pivot chart. **Not executed:** numerical grids, project-wide tests/build, CI, formalization, site publication, merge, source/body/registry/canonical/permanent-tag or main-branch changes. 
