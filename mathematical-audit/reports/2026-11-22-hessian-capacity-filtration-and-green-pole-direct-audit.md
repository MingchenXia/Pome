# Audit: smooth Hessian capacity hierarchy and classical Green poles

**Date:** 2026-11-22. **Reviewed main SHA:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Audit branch:** `review/mathematical-audit`. Review-only notes, not a production mathematical-body edit.

## POME-HESSIAN-LOCAL-CAPACITY-FILTRATION-001

**Classification:** **low / verified conditional deduction** from the printed smooth mixed-trace inequality, **not a confirmed error or a gap** in the printed result. This is not an independent certification of the antecedent Hessian analytic machinery.

**Exact anchors:** `docs/sections/complex-hessian-equations--local-capacities-and-decreasing-products/index.html` (main blob `115d285f6b1f76d284463c396e7e87db2b9dbdc3`), Definition 8.11.2 (source `non-kahler-pluripotential-theory:016F1DC8`, permanent `FA49D2074193`, physical lines 48–61) and equation 8.11.3 (source `non-kahler-pluripotential-theory:32422401`, permanent `A08EAEC63C44`, lines 64–71). The standing assumption **2 ≤ m < n** is explicitly printed in §8.1, `docs/sections/complex-hessian-equations/index.html`, blob `5331b937ccdaba51f1ec006d5e72dc84f7addfbf`, physical line 7.

### Claim and complete conditional proof

On the fixed coordinate ball `U` used in §8.11, let `c_q` be Definition 8.11.2's smooth local capacity for `0 ≤ q ≤ m`. For every pair `0 ≤ q ≤ s ≤ m` and every compact `K\Subset U`, there is a constant `C_{K,q,s}` independent of `E` such that for every Borel `E\subset K`,
\[
c_q(E)\le C_{K,q,s}\,c_s(E).
\]
The same compact-local comparison holds for outer-open capacities `c_q^*,c_s^*` and arbitrary `E\subset K`:
\[
c_q^*(E)\le C_{K,q,s}\,c_s^*(E).
\]
In particular, zero `c_s^*`-capacity implies zero `c_q^*`-capacity for every `q≤s`. This is a **one-directional** filtration statement; the converse is not claimed.

**Proof.** For `q≥1`, fix an arbitrary smooth capacity competitor `a` with `-1≤a≤0` and `dd^c a \in\overline{\Gamma_m(\omega)}`. In the smooth mixed-trace estimate (8.11.3), take the `q` potentials `f_1=\dots=f_q=a`, and choose its fixed strongly PSH barrier `b` and normalization constants `B,L`. Because the common bound is one, those constants and the resulting estimate are independent of the particular `a`. The left side is
\[
(dd^c a+\dots+dd^c a)^q\wedge\omega^{n-q}
=q^q(dd^c a)^q\wedge\omega^{n-q}.
\]
The right side is `C\Lambda_s((qa+b-B)/L)`, with normalized smooth argument admissible for the defining supremum of `c_s`. Integration over any Borel `E\subset K` and then supremum over `a` gives `q^q c_q(E)≤C c_s(E)`. If `q=0`, the zero-factor case of the same printed estimate bounds `\omega^n` by a fixed normalized strictly PSH test's `s`-Hessian trace; hence `c_0(E)=\int_E\omega^n≤Cc_s(E)`. If `q=s=0`, equality is immediate.

For the outer version, fix a relatively compact open `W` satisfying `K\subset W\Subset U`. Given any open `G\subset U` containing `E`, `G\cap W` also contains `E`, and the previous inequality gives `c_q(G\cap W)≤C c_s(G\cap W)≤C c_s(G)`. Taking the infimum over `G` proves the assertion, allowing the same uniform constant on `W`. No limit interchange, assertion about arbitrary nets, or regularization theorem is used.

**Suggested optional addition:** state this local capacity-filtration corollary after equation 8.11.3; retain the original inequality, proof, source attribution and permanent tags. **Affected dependents:** capacity-exceptional sets in §§8.11.6/8.11.10/8.11.11/8.11.13–14 and locality in §8.12. It does **not** imply the reverse inequality or a globally uniform constant across arbitrary coordinate charts.

## Exact direct section review and dependency checks

### §8.11 — Local capacities and decreasing products (complete present-main direct read)

Integrated file `docs/sections/complex-hessian-equations--local-capacities-and-decreasing-products/index.html`; blob `115d285f6b1f76d284463c396e7e87db2b9dbdc3`; section tag `BA5052EF5C4F`; **physical mathematical lines 7–334**. Statements checked include:

- **Lemma 8.11.1**, source `7121E570`, tag `370C4F1C4AF0`, lines 20–44. The nested-cutoff CLN bound uses only locally smooth unshifted cone products; `dd^c(f^2)=2fdd^cf+2df∧d^cf` is used only after shifting `f≥0`, so the claimed positivity is appropriately qualified. At degree `q=m-1`, the gradient factor still has admissible degree `m`.
- **Definition 8.11.2 / Eq. 8.11.3**, source `016F1DC8/32422401`, tags `FA49D2074193/A08EAEC63C44`, lines 49–71. The barrier is locally fixed; the constants do not depend on a capacity competitor. The displayed quantitative corollary above is conditional on this verified smooth estimate.
- **Lemma 8.11.4**, source `E67F97DC`, tag `9AF7CFAD9A0B`, lines 75–122. Checked deleted-coordinate positivity when `q≤m-2`, the separate `q=m-1` two-index coefficient argument, pointwise Cauchy–Schwarz and finite polarization. The negative-power edge case `\omega^{n-q-2}` **does not arise**: the actual §8.1 assumption `m<n` and `q≤m-1` give `n-q-2≥n-m-1≥0`. An error report based on incorrectly allowing `m=n` would be spurious.
- **Lemma 8.11.5 / Proposition 8.11.6**, sources `CCF3D5CF/22C64532`, tags `9416072D448F/390B1CE08171`, lines 127–235. Checked the fixed-boundary-collar regularized maxima, compact support of differences, the exact torsion-corrected energy derivative (8.11.8, source `9C754164`, tag `CA5C66E53CFA`, lines 169–185), induction using lower capacities, and the order of `k→∞` before the auxiliary threshold `δ↓0`. The positive energy term is not obtained by incorrectly dropping nonclosed-background torsion.
- **Lemmas 8.11.10–11**, sources `FA167F60/59C81738`, tags `348FF027ECE6/978D54F1054C`, lines 240–277. Checked the open-set lower-semicontinuity argument for coefficient variations and the common exceptional open set for a **countable** collection of quasicontinuous functions; Dini applies on its compact complement, not on all of `K`.
- **Theorem 8.11.12**, source `B227378C`, tag `C044CD1C65C4`, lines 282–293. The recursion first proves distributional convergence; coefficient-measure convergence is claimed only below degree `m`. Symmetry is established from a common smooth diagonal approximation, without silently interchanging unrelated iterated limits. At top degree, `Q_m` is positive and has an order-zero weak limit, not a purported raw `D_m` measure.
- **Lemma 8.11.13 / Theorem 8.11.14**, sources `915C1E41/C3C23711`, tags `E64937A67BD2/945FEE7DBDC5`, lines 301–332. Fixed local strictly PSH correction dominates shifted traces, the open-set variation bound passes to decreasing limits, and the weighted limit uses outer `c_m^*` quasicontinuity. No new original error confirmed.

**Uncertified dependencies:** §8.2 Gårding mixed form inequalities, §8.6 decreasing smooth admissible approximation, §8.9 ordered recursive-current construction and local corrections. Their occurrences here are tracked as *dependencies*, not proof-completed or certified. They are distinct from, and do not authorize reopening, the excluded Demailly programme.

### §7.18 — Classical Monge–Ampère measures at one exceptional point (complete direct read)

Integrated `docs/sections/classical-monge-ampere-measures-at-one-exceptional-point/index.html`, blob `902375361e37c15e45e7f4b7055bfe4cd6a6db9d`, section tag `A9598FE840EE`, **mathematical lines 7–70**. The two initial proof expansions (lines 7–38) use compact tests constant near the single pole, truncation `max(u,-j)`, the Stokes/BT weighted identity on a derivative annulus, and a common compact mass bound. Their scope is **one-point self-products**, not the full Hausdorff-zero mixed-product Theorem 7.28.1. The residual atom inequality uses weak convergence's **closed-set upper** bound at the pole, with the inequality orientation checked.

**Proposition 7.18.1** (source `klimek-pluripotential-theory:E69DEC85`, tag `00C5CD9B3208`, lines 43–52): sufficiently deep truncations modify the potentials only in a compact interior set; cutoff Stokes transfers the total mass, and bounded comparison applies to the strictly ordered truncations. This does not require an unsupported convergence of total masses from arbitrary vague convergence.

**Proposition 7.18.2** (source `klimek-pluripotential-theory:E1312773`, tag `AD17D2D77F97`, lines 57–70): the stated book normalization gives `M_{\log|z-a|}=2^{-n}\delta_a`; logarithmic Green comparison preserves the atom, and maximality eliminates off-pole mass. The uniqueness statement explicitly requires bounded hyperconvex `D` and zero boundary values. The spherical-product identity, Green regularity and maximality are dependencies not independently certified in this increment.

### §7.19 — Symmetric envelopes and finite poles (complete direct read)

Integrated `docs/sections/symmetric-envelopes-and-finite-collections-of-poles/index.html`, blob `8e33a409fa4a7c6eea29ab48727741ed9b1e167d`, section tag `5D2B9AF5042C`, **mathematical lines 7–91**.

- **Proposition 7.19.1** (source `klimek-pluripotential-theory:02CB50B8`, tag `9261026A57C2`, lines 11–20): joint USC via locally uniform inner-ball pole estimates, PSH `L¹_loc` subsequences, and the submean inequality followed by the fixed smoothing-radius limit. No symmetry assumption is used.
- **Proposition 7.19.2** (source `33CE7712`, tag `ABA8792055E8`, lines 25–32): the converse uses a genuine negative PSH competitor in the second variable and swaps variables, rather than assuming second-variable PSH automatically implies symmetry.
- **Proposition 7.19.3** (source `5793A4E7`, tag `557F24B2F2DD`, lines 36–57): the raw symmetric envelope is identified with its joint USC regularization; separate PSH is recovered using regularized suprema over shrinking second-variable neighborhoods. The jointly subharmonic, separately PSH admissible family is not silently strengthened to jointly PSH. Residual `2^{-n}` atom is conditional on the point-mass construction just inspected.
- **Proposition 7.19.4** (source `79AD1807`, tag `0FDD375AF53F`, lines 62–73): confirmed the order of the negative planar Green-envelope supremum and use of separating bounded coordinate maps off the diagonal. The planar Greenian criterion and exhaustion symmetry remain cited internal/theoretical inputs, not a newly established transitive certificate.
- **Proposition 7.19.5** (source `00AC0DAE`, tag `A3DBF2B9E6B2`, lines 78–91): each pole has exact `α_j log|z-a_j|+O(1)` via individual upper and sum lower competitors; locality and residual invariance yield `2^{-n}\sum α_j^n δ_{a_j}`. Hyperconvex boundary uniqueness is a separate conclusion. No inference of interior continuity of the multipole envelope is made.

No new false theorem, mathematical proof gap or genuine duplication was established in these three sections. Earlier issues in §7.28 and all Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss completion programmes are **deferred-by-user** wherever in the excluded scope, not called resolved or certified.

## Coverage and operation accounting

**This increment:** **3 present-main whole-section direct reads** (§§7.18, 7.19, 8.11), **1 selected standing-hypothesis check** (§8.1), **1 new low verified conditional deduction** (capacity hierarchy), **0 newly confirmed original errors**, **0 completely certified upstream chains**. §§8.12–8.13 were viewed as dependency context, not counted as new complete reads or first visits; earlier full-review records remain. The 747-section ToC coverage matrix is retained; its legacy unknowns do not become historical first visits.

**Writes:** audit Markdown only on `review/mathematical-audit`. No build, tests, CI, main/source/body/registry/tag/canonicalization edit, PR creation/merge or website publication.
