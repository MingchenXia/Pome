# High-codimension branch incompatibility for PSH removability

**Date:** 2026-11-07. **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Finding:** `POME-PSH-BRANCH-CODIM-NONREMOVABILITY-001` — **low / verified conditional deduction** (complete elementary countermodel to an *unstated strengthening*, not a false printed theorem). **Scope:** previously partly audited §§9.9 and 9.10; only the particular statements and new branchwise obstruction listed below were reviewed. No whole-section certification.

## Integrated reading-edition anchors

- `docs/sections/complex-spaces-and-modifications--plurisubharmonic-functions-on-reduced-spaces/index.html`, production blob `d9d8091b530c9843e5a725b49af2400936aeaa3a`, Definition 9.9.1 lines 10–18; Lemma 9.9.2 lines 19–44 (local ambient extension/disc pullback); Proposition 9.9.4 lines **62–90**. Proposition source `foundations-of-pluripotential-theory:A6674849`, permanent tag `B43080BD49F3`. Proposition 9.9.4 proves **local upper boundedness** near a set of codimension at least two on each branch, **not extension**.
- `docs/sections/pluripotential-theory-on-unibranch-spaces/index.html`, production blob `6edfa6b19fa7cdbaf0c2665389fa7b3ca338cdf4`, Definition 9.10.12 lines **110–124**, Theorem 9.10.13 lines **126–136**, Theorem 9.10.14 lines **139–155** and uniqueness/existence proof lines **158–211**. Theorem source `sgpt:EEFC0C9A`, permanent tag `C69D2F0ABA4F`; its codimension-two clause is permanent tag `C2D00AE1EE6E`. The *unibranch* hypothesis is explicit. The pre-existing author footnote on physical line 155 already gives a **one-dimensional** two-branch example. That historical/example material is **retained**, not removed or relabeled.

## Exact new model in arbitrarily high complex codimension

Fix integers `n >= 2`, `r >= 2`, write `C^{rn} = C^n_1 ⊕ ... ⊕ C^n_r`, and let `P_i = {z_j=0 for every j != i}`. Put

\[
X = \bigcup_{i=1}^r P_i \subset \mathbb C^{rn},
\qquad A=\{0\}.
\]

The reduced analytic space `X` has exactly `r` irreducible, smooth branches `P_i` of dimension `n`, pairwise meeting only at the origin; its defining ideal is the radical intersection of their linear ideals. Thus `A` has **complex codimension `n` on every branch**, which meets (and exceeds) the precise codimension-two hypothesis of Proposition 9.9.4. The origin is non-unibranch.

Choose finite real constants `c_1,...,c_r`, and define `u` on `X \ A` by `u|_{P_i\A} = c_i`. These pieces live on disjoint open-and-closed components of `X\A`; near any point they are constant restrictions of ambient pluriharmonic functions, so `u ∈ PSH(X\A)` under both integrated definitions. In particular `u` is **globally bounded**.

**Claim (if-and-only-if):** This `u` has a plurisubharmonic extension to any neighborhood of `0` in `X` if and only if `c_1=...=c_r`.

*Proof.* Suppose `v` is such an extension and write `a=v(0)`. For every `i`, the holomorphic disc `γ_i(t)=t e_{i,1}`, with `γ_i(0)=0`, lies in the `i`th branch. The pullback `v∘γ_i` is subharmonic on the disc by Lemma 9.9.2(2) (equivalently by the elementary ambient restriction in Definition 9.9.1), and equals `c_i` at every nonzero argument. Its upper semicontinuity forces `a >= c_i`; the sub-mean inequality at `0` gives `a <= c_i`. Consequently `a=c_i` for every `i`, and the constants are equal. This rules out even `a=-∞` when any `c_i` is finite. Conversely, when every `c_i=c`, the ambient constant `c` restricts to an extension in `PSH(X)`. QED.

The unique upper-semicontinuous prolongation of the original `u` has `u^*(0)=\max_i c_i`. If the constants differ, then on any lower-valued branch `P_j`, the pullback `u^*∘γ_j` is **strictly larger at the center than its punctured constant value**, contradicting subharmonicity. Thus upper boundedness and the canonical USC limsup do not suffice for removability even when the missing set has arbitrarily high complex codimension on every irreducible branch.

A slightly broader fully explicit family takes `u|_{P_i\A}=c_i+\operatorname{Re}L_i(z_i)` for arbitrary complex linear forms `L_i`. Exactly the same disc argument (or the sub-mean property of the linear harmonic term) shows extension is possible **iff all `c_i` agree**; in that case the ambient pluriharmonic function `c+\operatorname{Re}\sum_i L_i(z_i)` is an extension. The local obstruction is mismatch of branchwise values at the identified point, not a failure of a local upper bound.

## Scope and mathematical classification

The integrated **Proposition 9.9.4 is correct**: the constructed `u` is bounded. The integrated **Theorem 9.10.14 is correct under its stated unibranch assumption**: the present `X` intentionally violates that assumption. The distinction from its author-supplied footnote is **higher codimension**: the existing two-curve example has a missing point of codimension **one**, while this proof shows that *even an arbitrarily high codimension does not replace unibranchness*. No counterexample to a printed statement is asserted. The example is fully elementary and requires **no Demailly regularization, Bergman, L², OT, or related excluded program**.

**Recommended correction / dependent caution:** No change to either printed theorem. Record a reader-side warning before applying codimension-two removability on reducible/non-unibranch spaces: Proposition 9.9.4 supplies only upper bounds, and the genuine PSH extension theorem 9.10.14 requires branch compatibility (guaranteed there via unibranchness). A possible separate reviewable editorial note could cross-link Proposition 9.9.4 to the unibranch clause of Theorem 9.10.14. **Affected downstream use:** any argument attempting to deduce singular-space PSH extension or envelope descent from a codimension estimate and boundedness alone. None is claimed defective without a specific checked use.

**Inputs and outstanding verification:** The obstruction itself follows from constant functions and the disc sub-mean inequality. The full proof of the positive Grauert–Remmert theorem, its Fornæss–Narasimhan disc criterion, Hironaka prerequisites, and global applications were **not** independently verified in this increment. All existing audit ledger statuses are unchanged. **Coverage:** only the selected statements, hypotheses, author footnote and the exact new model; no other proof paths, tests, builds, CI, formal verification or publication.
