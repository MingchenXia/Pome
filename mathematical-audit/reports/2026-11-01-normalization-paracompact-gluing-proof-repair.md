# 2026-11-01 — A paracompact gluing proof for normalization without global countability

**Production main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Scope:** an independent repair for the global topological step of the *existing* normalization proof, plus a limited, separate introductory reading check. **No production code, mathematical statement, permanent tag, source body, or canonical registry was edited.**

## Finding POME-NORM-PERFECT-PARACOMPACT-REPAIR-001

- **Severity / status:** medium / **verified repair (proposed proof replacement only; not applied to production)**. The original proof-step defect `POME-NORM-COUNTABLE-COVER-001` remains **confirmed error in a proof step / unresolved in the printed reader**. This report does **not** identify a false normalization theorem, a new counterexample to it, or a completed proof audit of its other steps.
- **Target:** Theorem **9.4.6** (Normalization), source `foundations-of-pluripotential-theory:7042BB57`, permanent tag `12A47DB401E2`; `docs/sections/complex-spaces-and-modifications--reduced-spaces-and-normalization/index.html` on `main`, blob `06439f43d1ce8e83d2529682c9a630bffa3d9c22`, theorem lines **142–163**, especially Step 3 at **line 157**. Its local input is Lemma **9.4.5**, source `foundations-of-pluripotential-theory:571B5EA0`, permanent tag `58E87F89D557`, same file, lines **117–140**.
- **Convention:** Definition **5.2.3**, source `foundations-of-pluripotential-theory:76F27E8E`, permanent tag `42A02A1A5EFE`, `docs/sections/complex-differential-forms-and-positive-currents--complex-manifolds-and-differential-forms/index.html`, blob `886a687d5029616950683fe55defce1fe6854b12`, **line 49**: a complex manifold is Hausdorff and paracompact, not necessarily globally second-countable. **Lines 83–86** explicitly allow uncountably many components.

### The precise defect and a countermodel to the proof step

Step 3 correctly obtains compatible local normalizations and establishes Hausdorffness, but then asserts that the base `X` has a countable basis and chooses countably many normalization charts. Neither conclusion follows from the stated global complex-space conventions. For an uncountable set `I`, the disjoint union `X = ⨿_{i∈I} Δ_i` of complex discs is Hausdorff, locally analytic, and paracompact: refine an open cover independently on each clopen component. It is not second-countable (any basis must contain at least one set in each component). Its identity normalization is finite, proper and normal. Thus **the theorem survives but the global countability step fails**.

### Independent topological lemma, fully proved

**Lemma.** If `f:Y→X` is a continuous **closed** map with compact fibers, `X` is paracompact, and `Y` is Hausdorff, then `Y` is paracompact. No countability, local connectedness, sequential compactness, or finiteness of the fibers is needed.

**Proof.** Let `{O_a}_{a∈A}` be any open cover of `Y`. For each `x∈X`, compactness of `f^{-1}(x)` yields finitely many members `O_{x,1},…,O_{x,m(x)}` covering the fiber. Put `W_x=⋃_{j=1}^{m(x)} O_{x,j}`. Since `f` is closed, `U_x=X\setminus f(Y\setminus W_x)` is open, contains `x`, and satisfies `f^{-1}(U_x)⊂W_x`. Choose a locally finite **open refinement** `{V_i}_{i∈J}` of `{U_x}_{x∈X}` covering `X`. For each `i`, fix `x(i)` such that `V_i⊂U_{x(i)}`. Then the sets
```
    f^{-1}(V_i) ∩ O_{x(i),j},   i∈J,  1≤j≤m(x(i))
```
form an open cover of `Y`, refine the initial cover, and are locally finite: the inverse images of the locally finite family `{V_i}` are locally finite by continuity, and each index `i` contributes only finitely many sets. Hence `Y` is paracompact. QED.

### Self-contained application to the exact normalization construction

Let `ν:Ẋ→X` be the space obtained by the canonical gluing in Step 3, using the compatible finite local normalizations furnished by Lemma 9.4.5 and uniqueness established in Theorem 9.4.6 Step 2. The Hausdorff argument preceding the incorrect countability sentence is independent of countability and still applies.

For each `x∈X`, there is an open neighborhood `W_x` such that `ν^{-1}(W_x)→W_x` is the finite, hence **proper**, local map of Lemma 9.4.5. To see that `ν` is proper globally without invoking paracompactness of `Ẋ`, let `K⊂X` be compact. Using local compactness and Hausdorffness of the analytic local models, choose finitely many relatively compact open sets `V_1,…,V_N` covering `K` with compact closures `\overline V_i⊂W_{x(i)}`. Every `ν^{-1}(\overline V_i)` is compact by local properness. Since `K` is closed, `ν^{-1}(K)` is a closed subset of the finite union of these compact sets, hence compact. So `ν` is globally proper. It is closed: for a closed `F⊂Ẋ` and `x∉ν(F)`, take a relatively compact neighborhood `U` of `x`; `ν(F)∩\overline U` is compact because `F∩ν^{-1}(\overline U)` is compact, and a smaller neighborhood of `x` avoids it. The fibers are finite by the local models, thus compact. Applying the proved lemma to `ν` and the paracompact base `X` gives the required **paracompactness of `Ẋ` without any global countability assertion**.

This supplies the missing topological deduction and preserves the existing local analytic structure, the proper/bimeromorphic/fiber assertions, and all source attributions. It is compatible with uncountably many connected components. It does not modify or claim a new independent verification of Steps 1, 2, 4 or every analytic input to Lemma 9.4.5.

### Proposed isolated patch and dependents

In the **proof only** of Theorem 9.4.6, replace the two sentences beginning “Since `X` has a countable basis…” through “`Ẋ` is paracompact” by the properness/closed-map/local-finite-refinement argument above (or a shorter version with the same complete justification). Keep Theorem 9.4.6 as stated, all permanent/source tags and historical attribution. Do **not** edit `main` or generated reader files directly as part of this audit.

**Affected dependents:** Corollaries 9.4.7 and 9.4.9, the normalizations and finite maps in §§9.5–9.8, and subsequent uses of normalization on disconnected complex spaces. The specific previously recorded `POME-NORM-COUNTABLE-COVER-001` proof error remains unresolved *in production* until a separate reviewable source/reader patch lands. No claim of full normalization theorem certification.

## Separate coverage and strict boundaries

Directly inspected the integrated **§11.32** introductory page `docs/sections/normalization-and-weak-adjoint-measures/index.html`, blob `031b5d62d25d7ff03d95e4a14988399527cc946a`, **lines 7–12**, section tag `7091FEDB43F0`. It contains a subject overview and links to §§11.33–11.47, **not a numbered theorem/proof**; this is **introductory/structure-only inspection**, not a certificate for its informal claims or any of those subsections. Also checked the indexed §22.1.2–19 and §22.1.54–63 statements/proof passages as **context-only, historically already sampled**: no new assertion of completeness or repeated Duistermaat–Heckman findings.

Coverage this run: **new complete elementary topological repair for the specified Step 3 only**; incremental proof-level §9.4.5/.6, and introductory §11.32. Current edition remains **25 chapters / 747 numbered sections / zero entire mathematical sections certified**. Existing ledger statuses preserved. All user-excluded Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss work stays **deferred-by-user**, neither resolved nor reopened. No repository tests, build, CI, formalization, website publication, or source/main edits were performed.
