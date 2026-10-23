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
