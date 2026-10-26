# Mathematical audit — 2026-10-26: Choquet selection without an external proof; rigidity of equal-trace currents

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Review branch at the start:** `b52b5ca74b1ce183425b1ec29dbb900af3ba56e7`.
**Scope:** newly selected, nonexcluded reading-edition proofs in §§5.3–5.4, 5.13–5.14 and 16.40; no whole-section certification. This is an audit note, **not** a source/registry/permanent-tag change.

## Finding POME-CHOQUET-TOPOLOGICAL-REPAIR-001

**Severity:** low. **Status:** verified repair **of a proof dependency, proposed but NOT integrated**. The printed proposition is **correct**; its current proof still invokes an external source.

**Precise target.** Proposition **5.14.3 (Choquet's lemma)**, source label `sgpt-BAE53833`, permanent tag `1D624ECF05E9`, `docs/sections/plurisubharmonic-functions--properties-of-plurisubharmonic-functions/index.html`, main blob `e7d871122eca3eb7416ab8a993063cdc8d3987f3`, statement lines **49–51**, proof lines **57–59**. The manuscript assumes a nonempty locally uniformly upper-bounded family `(φ_i)_{i∈I} ⊂ PSH(X)` and that `X` has at most countably many connected components. The integrated proof presently reduces to a ball and invokes **[GZ17, Lemma 4.31]** rather than furnishing that last step. The countable-basis convention is explicitly justified in §5.2, `docs/sections/complex-differential-forms-and-positive-currents--complex-manifolds-and-differential-forms/index.html`, Definition 5.2.3 tag `42A02A1A5EFE` and the text at lines **80–86**, blob `886a687d5029616950683fe55defce1fe6854b12`.

### Complete internal replacement argument

A purely topological lemma suffices. Let `X` be any second-countable topological space, let `I` be nonempty, and let `(f_i)_{i∈I}` be **arbitrary extended-real-valued functions**. There is a nonempty countable `J⊂I` for which

```text
(sup_{i∈I} f_i)^* = (sup_{j∈J} f_j)^*,
```

where the star is upper-semicontinuous regularization (defined via the neighborhood limsup). No semicontinuity or potential theory is needed for the selection itself.

Choose a countable base `(B_m)_{m≥1}` of nonempty open sets. For every pair `(m,q) ∈ ℕ×ℚ` such that **some** `i∈I` and `y∈B_m` satisfy `f_i(y)>q`, choose one such index `i(m,q)`. Let `J` consist of all these indices and one arbitrarily fixed `i_0∈I`; it is countable and nonempty. Set `F_I(y)=sup_{i∈I}f_i(y)` and `F_J(y)=sup_{j∈J}f_j(y)`. For each basis member `B_m`, equality of its rational strict lower cuts yields

```text
sup_{y∈B_m} F_J(y) = sup_{y∈B_m} F_I(y)
```

in the extended real line, including the cases `±∞`. Indeed, the left side is no larger than the right; if the right side exceeds a rational `q`, the selected witness `i(m,q)` makes the left side exceed `q` as well. Now the elementary identity

```text
F^*(x) = inf_{m: x∈B_m} sup_{y∈B_m} F(y)
```

proves the desired equality at each `x∈X`.

Each connected component of a Pome complex manifold is second-countable by the §5.2 convention. If the component set is countable, their union is second-countable. Apply the topological lemma to `f_i=φ_i`; local upper boundedness and the independently stated upper-envelope theorem (Proposition 5.14.2, tag `01C3654494E2`, same section, lines **21–36**) ensure that both selected regularizations are plurisubharmonic. **This proves the entire assertion of Proposition 5.14.3 without [GZ17] or any approximation theorem.**

The countability hypothesis is also optimal *as a uniform theorem for all families*. Take an uncountable disjoint union `X=⨆_{α∈A} Δ_α` of unit complex discs (a paracompact complex manifold), and for each `α` let `φ_α` be the locally constant function equal to `1` on `Δ_α` and `0` on all other components. These are bounded pluriharmonic functions. The supremum over all `α∈A` is identically `1`; any countable subfamily has supremum `0` on every unselected open component, and upper regularization does not alter either value there.

**Proposed correction:** replace the external-proof sentence at §5.14.3 lines 57–59 by the above countable-base selection (with the short sharpness example optional). No new assumptions are needed. **Affected dependents:** upper-envelope and Choquet countable reductions in §5.14 and all later countable-family selections that cite Proposition 5.14.3. This is a *complete proposed proof*, not an assertion that the reading-edition file has already been edited.

## Finding POME-TRACE-POTENTIAL-RIGIDITY-001

**Severity:** low. **Status:** verified conditional deduction (a new consequence of the printed distributional identities, not a claim that any printed theorem is false).

**Precise targets.** Theorem **5.3.7**, source label `foundations-of-pluripotential-theory-2BB3620D`, permanent tag `1C212E45A497`; `docs/sections/complex-differential-forms-and-positive-currents--currents-and-positivity/index.html`, main blob `deba65cba51b4275b523879202e6254db0db2b5c`, statement lines **279–286**, proof **288–302** (positive currents have Radon coefficient measures). Theorem **5.4.3**, source label `foundations-of-pluripotential-theory-AA6533F0128A`, permanent tag `2408CCC1B5A0`; `docs/sections/complex-differential-forms-and-positive-currents--local-potentials-for-closed-1-1-currents/index.html`, main blob `acfdd3d1e174fdb55473771b42e7e33b6f17ea18`, statement **81–83**, distributional identity **87–93** and uniqueness **95–96**. The coefficient compatibility is Equation **5.4.1**, tag `E64CA5AFE6C4`, lines **21–24**. The smooth local `dd^c` exactness is Lemma **5.4.2**, tag `7815541A95AD`, lines **27–76**.

### Statement and proof

Let `Ω⊂ℂ^n`, `n≥1`, be open and let `β=(i/2)∑_j dz_j∧d\bar z_j`. Suppose `R` is **any real d-closed (1,1)-current**, not necessarily positive or of order zero, with **zero Euclidean trace** `R∧β^{n−1}=0`. Then `R` is a smooth closed (1,1)-form and is locally `dd^c h` for a smooth **real harmonic** function `h`.

Write `R=(i/2π)∑_{j,k}r_{j\bar k}\,dz_j∧d\bar z_k` with distribution coefficients. Because `R∧β^{n−1}=((n−1)!/π)(∑_j r_{j\bar j})\,dV_{2n}` in the local convention, its trace condition is `∑_j r_{j\bar j}=0` as a distribution. The two closedness identities in Equation 5.4.1 hold distributionally. Commuting derivatives,

```text
(1/4) Δ r_{j\bar k}
  = Σ_l ∂_{z_l}∂_{\bar z_l} r_{j\bar k}
  = ∂_{z_j}∂_{\bar z_k} Σ_l r_{l\bar l}
  = 0.
```

Thus each `r_{j\bar k}` is a harmonic distribution; the already internal Weyl lemma (Theorem 3.1.11) makes it smooth. Lemma 5.4.2 supplies locally a smooth real potential `R=dd^c h`. Taking traces gives `Δh=0`.

For **positive closed currents `T,S` with the same trace measure** in this fixed Euclidean chart, apply the lemma to `R=T−S`. Their difference is smooth. Moreover their local canonical psh potentials `u_T,u_S` (Theorem 5.4.3) differ by a smooth real harmonic function: `Δ(u_T−u_S)=0` and Weyl's lemma identifies the difference as a smooth harmonic distribution; uniqueness of canonical subharmonic representatives promotes the equality to **every point**, including polar points. Hence they have the same local singularity types, pole loci, Lelong numbers and multiplier ideals, and their coefficient measures have identical parts singular with respect to Lebesgue measure. These consequences hold without imposing positivity on the *difference*.

**Optimal limitation:** equality of traces need not give equality of currents when `n≥2`. On a ball use `u_0=∑|z_j|²` and `u_ε=u_0+2ε Re(z_1\bar z_2)`, `0<|ε|<1`. The complex Hessian of `u_ε` has eigenvalues `1±ε,1,…,1`, so both `dd^c u_0` and `dd^c u_ε` are smooth strictly positive and have the same Euclidean trace, but are different. In `n=1`, equality of trace measures **does** imply `T=S`, since `dd^c h=0` for harmonic `h` there.

**Proposed addition:** place a local equal-trace rigidity corollary after Theorem 5.4.3, explicitly stipulating the **same fixed flat chart and Euclidean trace**; do **not** silently generalize to traces computed using unrelated Hermitian metrics. **Affected dependents:** singularity invariants of positive currents (§§5–6), smooth-versus-singular coefficient decomposition, and Lelong-number comparisons. This is conditional on the printed internal Weyl lemma and local `dd^c)-exactness; those dependency proofs were inspected at the indicated steps but not wholly independently certified.

## Other new selected proof checks — no new confirmed error

- **§5.13:** Proposition 5.13.9 tag `5DCB508EA9AD` (lines 99–113) and Proposition 5.13.17 tag `726DDFDDA8F2` (lines 172–184), in `docs/sections/plurisubharmonic-functions--the-definition-of-plurisubharmonic-functions/index.html`, blob `756d3347f65bad7e06a20f52c04ee6fd466c038f`. Checked the disjunction for holomorphic pullbacks into psh pole sets and the connected-component qualification; it would be wrong to assert unqualified psh pullback.
- **§16.40:** Lemma 16.40.1 tag `DD2047D70ACD` (lines 10–34) and Theorem 16.40.2 tag `8ED77FB38EC4` (lines 38–57), in `docs/sections/local-regularity-of-analytic-polyhedra/index.html`, blob `d6f9bd0c7e54de98ea0d02c1180eb8befc857997`. Checked the product principalization, factorwise monomial extraction, fixed-sign subsequence, complexification of the real-analytic arc, nonthinness at the endpoint, and compact zero-contact criterion. The **real-analytic principalization** explicitly stated at line 7 is a genuine external resolution/principalization input in the permitted exception class. No claim that the global proof or all L-regularity inputs have been independently certified.
- **§5.2.3:** the project *explicitly* defines complex submanifolds as **closed** local coordinate planes (line 49). Thus the apparently missing closedness in Example 5.3.9 is **not an error**: the proof's use of closedness follows from the collection's convention. No finding is registered on this false alarm.

## Verification limits and scope

Only the passages listed above were checked against the actual integrated reading edition on the pinned main revision. The proof repair is complete as a mathematical argument but is **not** integrated into the reading edition. No theorem in this report is labeled falsely stated. The full trace-class theory, all prior source variations and the complete 747-section collection remain uncertified. No software builds, CI, website publication, formal verification, source-body/registry/permanent-tag changes or changes to `main` were performed.

**Author's excluded scope:** Demailly approximation/regularization and the dedicated Bergman, `L²`, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme were not examined and remain **deferred-by-user**, not resolved or certified.
