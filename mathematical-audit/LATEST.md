# Pome mathematical audit checkpoint — 2026-10-23 16:57 Asia/Shanghai

**Fresh main** `b6933b772f41b45918f7e25ed1afbbb1fd892272` and current 25-chapter / **747-section** table of contents (inventory, **not** certification). Freshly read `AGENTS.md`, `documentation/proof-expansions.md`, current `main`, and `README.md` / `mathematical-audit/LATEST.md` on this review branch. Actual new selected proof review: §§6.56, 9.74, 9.77, 10.103, 10.104, with upstream §9.72 and §9.76 **dependency-only** checks. No entire section or external theorem independently certified.

New [dated English mathematical report](reports/2026-10-23-compact-center-uniform-lelong-and-cohomology-jumps.md), committed at `2f53c1da18d822f7918af9dc044c3dbc7b5bea02` and verified after the Markdown delimiter cleanup commit `fe9d0488c0b4636de1341cca5daa1d344397064a`. The [cumulative 747-section coverage matrix](SECTION_MATRIX.md) was synchronized without dropping earlier rows; its current blob `7267edf5bce044f26ec3a652f39121d1b29d4008` matches the local matrix byte-for-byte. The [cumulative ledger](LEDGER.md) was also newly synchronized on this branch, retaining historical findings and their statuses (commit `f3164d2893ed84f0b0ef6e5a948774261dcdf432`). No new arithmetic/regression script was run or copied.

- `POME-CAOPAUN-CENTER-UNIFORM-LELONG-001` — **verified conditional deduction**, low: §6.56 global normal-bundle current gives exact (Q_a=\omega_C-a\Xi) and one **uniform-in-(y\in C_0)** compact-center Lelong bound, retaining the defined analytic residual hypothesis; original theorem is not false.
- `POME-CAOPAUN-PIC0-HODGE-JUMPS-001` — **verified conditional deduction**, low: vector-bundle (h^q(F\otimes\rho)) is upper semicontinuous under arbitrary `Pic^0` nets, not necessarily constant; the existing Euler-characteristic lemma is correct.
- `POME-CAOPAUN-FOLIATION-CYCLE-INPUT-001` — **external dependency**, medium: Ou2025/Barlet generic compact-cycle and meromorphic leaf quotient theorem at §9.74, openly cited but not internally proved.
- `POME-CAOPAUN-FUJIKI-DEFORMATION-INPUT-001` — **external dependency**, medium: Fujiki's Kähler deformation invariance of uniruledness needed for §9.77.1; the inspected formal contraposition is correct.

**Scope:** completely skip Demailly approximation/regularization and the dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss completion programme. Historical notes remain **`deferred-by-user`**, neither reopened, resolved nor certified. §§6.55 and 10.108's excluded analytic programmes were not reviewed. No source/body/registry/canonicalization/permanent-tag changes, `main` changes, CI, build, automatic merge, PR, formal verification or website publication. Only review-branch audit Markdown was written; exact section-level work and external dependencies are in the new report and ledger. The separate lengthy historical `COVERAGE.md` local log has not yet been completely uploaded; the newly synchronized full `SECTION_MATRIX.md` is the durable authoritative section coverage matrix.

---

# Pome mathematical audit checkpoint — 2026-10-23 15:54 Asia/Shanghai

**Reviewed `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; current table of contents: 25 chapters / 747 sections (inventory, **not certification**). Refreshed `main/README.md`, `main/AGENTS.md`, `main/documentation/proof-expansions.md`, and review-branch `README.md` / `mathematical-audit/LATEST.md`. **Actual new selected proof reading:** §5.50 (plurithin annuli and plurifine limits), §5.51 (nonpluripolar smooth curves), §5.57 (sphere logarithm and plane averages), with only limited internal dependency checks on §4.1.17 and §5.47.10. No whole section or upstream theorem chain certified.

New dated [English report](reports/2026-10-23-sharp-spherical-log-average-and-nonpolar-zero-dimensional-cantor.md), **independently fetched after GitHub commit `254f710de666362e8e354e46363b66c7d29e775a`**, and new [small exact check](checks/check_spherical_log_and_cantor_capacity.py), independently fetched after commit `be4ad6ff03848ac848cb16b2b51940a5e186c300`. The exact-rational script covers 239 finite identities/separation checks, **not** analytic/formal proofs.

- **POME-SPHERE-LOG-HARMONIC-001** — low / `verified conditional deduction`: the invariant-sphere logarithmic average has optimal constant `c_n=-H_{n-1}`; its absolute moment has an exact binomial formula, with sharp upper constant `H_{n-1}` (equality for `|z|<=1`). Strengthens Lemma 5.57.1, does not refute it.
- **POME-SMOOTH-NONPOLAR-CANTOR-CAPACITY-001** — low / `verified conditional deduction`: the specific Cantor slices in Theorem 5.51.1 have classical logarithmic capacity at least `Q^{-2}` uniformly and the zero-dimensional transverse Cantor set has capacity at least `(2*10^6)^{-1}`. This is **not** relative Green capacity and is not an error in the original theorem.

**Scope:** all Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof-completion remains strictly **`deferred-by-user`**, neither examined, resolved nor certified. No source/body/registry/canonicalization/permanent-tag, `main`, published site, CI, build, formalization, merge or PR changes. The complete local 747-row matrix and consolidated historical ledger still require separate synchronization; prior remote history is preserved below. All remote writing in this checkpoint was to `review/mathematical-audit` only.

---

# Pome mathematical audit checkpoint — 2026-10-23 15:00 Asia/Shanghai

**Fresh reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; existing audit branch read at `c4ccdc092ac7b6da2cea58ee228a475c7b8ba4bf` before writing. Fresh main `AGENTS.md`, `documentation/proof-expansions.md`, main/branch `README.md`, existing audit `LATEST.md` and current 25-chapter/747-section table of contents checked. The inventory is **not** mathematical verification. Only selected integrated proof steps were read, in §§11.16–11.19 and 11.24–11.26 (including contextual §11.25 and §11.24 historical audit crosscheck). **No whole section certified.**

New detailed audit-only English report: [continuous Hermitian adjoint stability and projective-complement properness](reports/2026-10-23-continuous-hermitian-adjoint-stability-and-projective-properness.md), committed as `fcfd098a310608711c183542e136634e9141d5af` and independently read remotely. Small [finite-state rational resolvent check](checks/check_stationary_resolvent_matrix_analogy.py), committed as `61ed677450473e95a0143e6e676757c0cab60109`; **7 exact-rational finite-state examples executed locally**, NOT a PDE or formal proof.

- **POME-HERM-ADJOINT-C0-LP-LIPSCHITZ-001** — low / `verified conditional deduction`: unique nonnegative normalized L^{p'} adjoint density of a continuous positive Hermitian trace operator on compact connected X, locally Lipschitz in the C^0 coefficient topology for p>2n; arbitrary directed-net strong L^{p'} stability. Conditional on the full Fredholm/comparison premises of Lemma 11.24.1.
- **POME-PROJ-COMP-BASE-PROPER-001** — medium / `proof gap`: the constructed exhaustion in Theorem 11.18.2 relies on compactness of the ambient projective bundle, but compact X is not stated in its section-local hypotheses. A trivial bundle over C refutes the *claimed properness of that cutoff*, not the convexity theorem. Proposed repair: state compact X, or supply a new noncompact properness argument.
- **POME-STEIN-OKA-WEIL-INPUT-001** — medium / `external dependency`: the global Oka–Weil approximation invoked by Lemma 11.16.2 and Theorem 11.16.3 remains an explicit unproved-in-this-audit analytic input; the elementary polynomial separation Lemma 11.16.1 is internally proved.

**Scope and synchronization:** this checkpoint adds audit-only documents to `review/mathematical-audit`, not main, manuscripts, registries, tags or the published reading edition. The detailed cumulative local 747-row coverage matrix and the most recent local ledger are not yet fully synchronized; historic remote records are preserved, not overwritten. Earlier `POME-HERM-CZ-INTERNAL-001` / `POME-HERM-ABP-001` findings are unchanged and not new progress. Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss completion stay **`deferred-by-user`**, neither reopened nor certified. No project-wide tests/build, CI, formal verification, automatic merge, PR or website publication.

---

# Synchronization checkpoint — 23 October 2026

The author explicitly authorized another normal push attempt. This synchronization uses the existing `review/mathematical-audit` branch without resetting it and does not change `main`, source manuscripts, generated reading pages, registries, or permanent tags.

## Newly synchronized and independently verified

- [HN exterior-power slopes and movable tensor-semistability dependency report](reports/2026-10-23-hn-exterior-polygon-and-movable-dependency.md), committed as `b304a27f0ce6d0d58bb37f9b513949a4d15ce0fe`. The remotely read content blob `c91d66d8138c6de441ddd9ae89535cb58f6a86d9` matches the local report exactly.
- [Exact HN exterior-power consistency check](checks/check_hn_wedge_polygon.py), committed as `27b1ca9edfed4783ec27b7602f31cedfb675219c` and independently fetched after writing. It is a finite combinatorial consistency check, not a proof of analytic sheaf semistability.

The report's closing write log describes the earlier 12:53 audit checkpoint and its failed write attempt. It is preserved as history; the successful user-authorized retry recorded here supersedes that earlier report-only synchronization status.

## Mathematical status and actual coverage

The reviewed main remains `b6933b772f41b45918f7e25ed1afbbb1fd892272`, also confirmed by a fresh branch read during this synchronization. The report records selected proof inspection of §§10.106–10.107 and §9.76, with dependency-limited checks of §§9.75, 10.109 and 19.11. It does not certify those entire sections or the full project.

- `POME-CAOPAUN-HN-WEDGE-POLYGON-001`: **verified conditional deduction**. The maximum and minimum slopes of reflexive exterior powers are the sums of the largest and smallest repeated HN slopes, conditional on the stated movable-class tensor-semistability theorem.
- `POME-CAOPAUN-MOVABLE-TENSOR-INPUT-001`: **external dependency**. The Ou/Toma movable tensor-semistability input remains a genuine unproved-in-this-audit prerequisite, not a false theorem.

This synchronization does **not** upload the entire accumulated local archive. Other pending reports, the cumulative local section matrix, ledger and coverage log remain pending unless separately verified as synchronized. Their old remote versions must not be mistaken for the complete current local record.

Demailly approximation/regularization and the dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss completion programme remain **deferred-by-user**, neither resumed nor certified. No project build, CI setup, website publication, automatic merge, force push, or new mathematical review was performed by this synchronization. Historical remote text is preserved below.

---

> Integration status — 18 October 2026: the audit branch has been incorporated into `main`. Confirmed capacity and placement defects are repaired; see [the integration report](reports/2026-10-18-integrated-corrections.md). Demailly approximation and its dedicated prerequisite audit remain deferred by the author. Older priorities, branch-only restrictions, and scheduling descriptions below are historical, not current instructions. This integration does not certify the unreviewed chapters or every external dependency.

# Audit checkpoint — broad-scope review, 17 October 2026

## Current mandate (supersedes older priorities)

The author has explicitly requested that Demailly approximation be ignored and that the rest of the entire project be checked. Skip that approximation programme and its dedicated Bergman/L2/extension/multiscale prerequisite work. Do not keep returning to it under another dependency label. Existing notes remain historical, deferred-by-user, NOT resolved or certified. The old first-priority and next-unit text in README.md and the historical checkpoint below is superseded by this instruction.

The hourly schedule and authorized pushes to `review/mathematical-audit` continue. Review the other chapters in rotation, documenting mathematical errors, genuine duplicates, proof omissions, hypotheses and actual external dependencies. Hironaka remains the permitted external exception. Preserve attribution. No direct changes to main, source manuscripts or published pages, and no automatic merge, publication or CI.

## New reviewed coverage

Reviewed main: `66f8176be2a006b9404ae6db49ee15621dea5523`.
Starting audit head: `91f48c1323d7c717c53204a6bc3b3d362010b726`.

[Whole-project coverage matrix](COVERAGE.md) records all 25 current chapters; it is an initial broad-pass ledger, not a claim that those chapters have been checked.

[New report: POME-CAP-001](reports/2026-10-17-open-set-capacity-counterexample.md).

**Confirmed error:** Proposition 13.12.7, tag `D56D6D4A5E94`, asserts whole-open-set capacity convergence of monotone local psh nets. Its own Definition 13.12.6 tests all of U. On the projective line with normalized Fubini–Study theta and U the unit disc, u_j=|z|^(2j) are uniformly bounded smooth psh functions decreasing to zero, but Cap_theta({u_j>1/2})=1 for every j. The report constructs admissible global circle-mass test potentials and proves the exact capacity value. This failure already occurs for sequences; adding uniform boundedness is not a repair.

**Correction direction, not yet integrated:** distinguish local convergence on every compact subset of U from global convergence on all U. Supply the corrected net theorem separately and inspect actual downstream uses. Do not silently change the meaning of capacity convergence everywhere. Keep POME-CAP-001 open until a reviewed correction is integrated.

The mathematical body of Section 13.12 was read, including both definitions above and Theorem 13.12.8. The latter's enclosing section defers its proof to GZ17; locating an internal replacement is pending. No falsehood of that weighted current-convergence theorem is asserted. The rest of Chapter 13 has not been certified. No full project tests, build, or formal verification were run in this increment; the counterexample is justified analytically, not by a numerical test grid.

## Next broad-scope units

1. Chapter 16: envelope order, supremum regularization, model-potential limits and exact proof dependencies.
2. Chapter 7: local Bedford–Taylor/capacity statements, comparisons and limits; distinguish local from global quantifiers.
3. Chapter 17: energy, geodesic and test-curve statements, then other unreviewed chapters in COVERAGE.md, including Hermitian volume/torsion and the algebraic, toric and non-Archimedean parts.

Track applications of POME-CAP-001 alongside this rotation; do not spend all future sessions in one chain. Preserve existing unresolved items outside the excluded programme. Detailed prior reports not yet synchronized remain historical pending artifacts, not a reason to resume the excluded priority.

## Superseded checkpoint retained as history — not the current work queue

Reviewed main: `66f8176be2a006b9404ae6db49ee15621dea5523`.
Audit branch has new coverage note: [POME-DEP-009, Richberg/psh primitives](reports/2026-10-17-richberg-coverage-check.md).

Newly read integrated proofs: Theorem 3.4.12 (subharmonic convolution); Theorem 5.9.1 and Proposition 5.9.2 (positive Hessians); Lemma 6.3.2 (Fejer barrier); Lemma 6.3.3 (Richberg); Theorem 6.3.4 (strict psh exhaustion). Quantitative local bump, convex regularized-max and finite gluing steps checked; no new confirmed false theorem. A separate detailed English review and exact-rational check remain local.

Still open: POME-REG-001/002 and conditional POME-REG-009 (prescribed nonclosed continuous positivity bound); POME-XREF-001; POME-DEP-001/005–008; global duplicate and dependency ledger. Third–eighth detailed reports remain unsynced.

Next: verify lower subharmonic/distributional primitives, revisit variable-scale Bergman comparison and underlying L2 estimates. This review did not run the full project test/build nor change published material.
