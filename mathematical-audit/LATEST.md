# Pome mathematical audit — 2026-10-23: subfamily singularity intersections and sharp CLN collar loss

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`, with fresh required AGENTS.md, documentation/proof-expansions.md, current integrated ToC (25 chapters / **747 inventory-only sections**), audit branch README.md and prior LATEST.md; initial review-branch head `e54b793736c6e9e926e1e2acdfc5c2580ffa5ba2` preserved, never reset.

**New substantive, specifically limited proof inspection:** §7.28 Theorem 7.28.1 (all-subfamily pole-locus Hausdorff condition, weighted product integrability), §7.30 Proposition 7.30.3 / Eq. 7.30.4 (intersection-dimension bounds, selected cutoff estimates), §7.32 Corollary 7.32.2 (collar-depth mass estimate). §§7.29/7.31 consulted **only as contextual dependencies**. Theorem 7.28.1's full continuity induction, cutoff intricacies and nonexcluded external dependencies remain unverified; no entire section is certified. All precise paths, source labels, permanent tags and physical line anchors: [complete dated English proof](reports/2026-10-23-complete-intersection-pole-mass-and-sharp-cln-collar.md).

- **POME-BT-HAUSDORFF-SUBFAMILY-SHARP-001:** low / `verified conditional deduction`, **not an original-theorem error**. Normal-crossing coordinate logarithms satisfy every Hausdorff subfamily test and have unit classical intersection mass, but NPP product zero; repeated coordinate divisor satisfies singleton tests yet makes the weighted product nonintegrable, demonstrating the importance of the higher-intersection tests.
- **POME-CLN-COLLAR-INVDELTA-OPT-001:** low / `verified conditional deduction`, **not an original-theorem error**. On the unit disc, `u=log|z|²`, `ψ=|z|²−1` gives `||uT||=||T||=1`, collar `Mδ=−log(1−δ)`, hence `δ/Mδ→1`. Therefore Corollary 7.32.2's `δ^{-1}` **exponent** is optimal; the printed numerical constant is not claimed sharp.

**Actual finite software validation:** `checks/check_bt_subfamilies_collar.py` executed **352 integer codimension identities and 500,500 exact rational collar inequalities**, all passed. This is **not** a proof of psh theory. No full project tests or build, GitHub Actions CI, website publication, formal verification, source/body/registry/permanent-tag edits, merge, force push or PR change. The new report, small check, selected section rows of SECTION_MATRIX.md and two finding rows of LEDGER.md were submitted to **review/mathematical-audit only**, with the audit branch unchanged except for normal forward commits; complete remote verification must be checked separately.

**Excluded as requested:** all Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss work remains **`deferred-by-user`**, not reexamined, resolved or certified. In particular §7.31.1's general smoothing is a dependency boundary, not an audit task. Historical records and unchanged findings remain intact.

---

# Pome mathematical audit — 2026-10-23: anisotropic MA limits and pluripolar Haar nullity

**Precisely reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **existing audit branch preserved** from 102b599aeb30be2eef2d3ecc9df5a350eae489e0 (never reset). Fresh required main AGENTS.md, documentation/proof-expansions.md, current 25-chapter/747-section HTML ToC, and review-branch README.md and LATEST.md were read. The section count is **inventory only**, not mathematical certification.

**Direct first-time nonexcluded proof review:** Lemma 6.55.1 and smooth fixed-m part of Proposition 6.55.2 (only lines 31–70); independent Lemma 6.45.1 on Haar-null intersection of pluripolar sets and totally-real slices. The detailed source blob SHAs, source labels, permanent tags, paragraph/line anchors, hypotheses, complete derivations, and affected dependents are in [dated report](reports/2026-10-23-anisotropic-restricted-ma-noncommuting-limits.md). Previously reviewed §6.56 and §9.74 appeared solely as de-duplication crosschecks; prior findings are **not** presented again as new coverage.

- **POME-CAOPAUN-MA-ANISOTROPIC-ITERLIMIT-001** — low, **verified conditional deduction**, **not** a source theorem error. Exact Cauchy-powered-coordinate tail epsilon/(epsilon+r^(2m)); complete family of nontrivial torus weak limits as m→∞, epsilon_m↓0; the two iterated m/epsilon measure limits do **not** commute. Original §6.55.2 takes epsilon↓0 with m fixed, hence remains unrefuted.
- **POME-TOTALLY-REAL-PLURIPOLAR-NULL-001** — low, **verified conditional deduction**, **not** a source theorem error. Maximal real-analytic totally-real submanifolds are locally pluripolar-null in smooth induced volume by holomorphic complexification and real-cube Riesz/Fubini. This properly generalizes the U(n) lemma under exact hypotheses.

**Actual checks:** executed checks/check_anisotropic_ma_limit_order.py in the local Python runtime: **630 exact rational finite identities and bounds PASSED**. This is not a formal proof or a validation of the limiting argument. **Not run:** full project tests or build, CI, browser rendering, website publication, mathematical formal verification. No source/body/registry/canonical-tag/main changes or PR manipulation. The new report, small reproducible checker, matrix and ledger changes were committed on the audit branch; final remote-commit verification follows separately, and successful commit SHAs must not be guessed.

**Strict exclusion remains:** Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof completion **deferred-by-user** (neither reopened, resolved nor certified). In particular §6.55.2 from line 72 and §6.45.2's smoothing/current-product programme were not audited. All historical finding statuses remain intact.

---

# Pome mathematical-audit checkpoint — 2026-10-23 19:07 Asia/Shanghai

**Current main read:** b6933b772f41b45918f7e25ed1afbbb1fd892272; **review branch preserved** (starting SHA 408d3e0816e2b72756c8bf27a5ae3eae54ecc51c). Freshly read main AGENTS.md, documentation/proof-expansions.md, the 25-chapter/747-section actual ToC, and review-branch README.md and this LATEST.md. Section counts remain inventory, not mathematical certification. The new Markdown report, one exact script, three changed section-matrix rows and three new ledger IDs are on the audit branch, subject to independent final remote verification.

**New, actually selected proof/model review:** §19.1 (graded partial Okounkov series), §10.105.1 (intrinsic/extrinsic submean proof), and the metric-extension boundary of §10.108.2. Precise source labels, permanent tags, physical HTML line anchors, hypotheses, complete proofs/diagnostic and proposed changes: [dated report](reports/2026-10-23-divisorial-okounkov-floor-and-minimal-submanifold-defect.md). §§19.2 and 19.4 were consulted solely to align definitions; §§9.77 and 10.103–104 were already covered and were only rechecked, **not counted as new coverage**.

- **POME-OKO-DIV-FLOOR-SERIES-001** — low, **verified conditional deduction**, not a false theorem: exact P¹ Hilbert/valuation floors, iff-integral literal semigroup closure, pseudometric-zero equivalent ceiling semigroup, partial body [c,d] and non-pluripolar mass d−c for 0≤c<d.
- **POME-REL-MINIMAL-SUBMEAN-DEFECT-001** — low, **verified conditional deduction**, not an error: exact nonnegative monotonicity defect and equality rigidity for nonnegative subharmonic functions on complex submanifolds of Euclidean space, plus curved graph sharpness.
- **POME-TAUT-MODEL-METRIC-EXT-001** — medium **candidate**, not a confirmed theorem error: §10.108.2 passes from an open-locus curvature-bound metric to a compact-resolution multiplier ideal without an explicit controlled extension lemma. The punctured-disc diagnostic shows lower curvature alone is insufficient, but does not refute existence of a better choice of metric.

**De-duplication:** The Fujiki deformation input encountered again in §9.77 was **already logged** as POME-CAOPAUN-FUJIKI-DEFORMATION-INPUT-001 in the prior 2026-10-23 compact-center/cohomology-jumps report. It is not entered anew. The previously checked §§10.103–104 likewise remain historical rechecks.

**Actually executed:** checks/check_divisorial_okounkov_and_submean.py: 266,539 exact rational Hilbert/carry cases, 2,184 nonintegral carry witnesses, seven flat symbolic radial identities and one curved-graph derivative identity passed. These are sanity checks, not formal proofs or a project-wide validation. No whole section certified, no full build, CI, website publication, main/source/permanent-tag changes, new PR, merge, force push or deletion.

**Hard exclusion unchanged:** Demailly approximation/regularization and the dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remain **deferred-by-user**, without any reinspection or resolution. Separate L²/relative Bergman inputs in §§10.105/10.108 were explicitly not followed. Historical audit ledgers are preserved below and in LEDGER.md.

---

# Pome mathematical audit checkpoint — 2026-10-23 18:05 Asia/Shanghai

**Freshly confirmed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. Existing audit branch before writes: 05da6df6c5968380c550de3cadd22dca975a7fd8. Read current main AGENTS.md, documentation/proof-expansions.md, main ToC, audit-branch README.md and audit-branch mathematical-audit/LATEST.md; actual inventory is 25 chapters / 747 numbered sections (**inventory, not mathematical certification**).

**Substantive selected new proof review:** §22.1.54–60 (DH moments, finite-energy tails, monotone volume convergence) and §20.4.19–24 (Gauduchon-normalized positive-current decomposition and net topology). Dependencies §19.5.26(1), §19.6.18–19, §11.31.3 directly crosschecked, not fully certified. Stable tags, current-main blobs, exact integrated line anchors and full proofs: [dated English report](reports/2026-10-23-dh-volume-profile-wasserstein-and-gauduchon-net-continuity.md).

- **POME-NA-DH-W1-PROFILE-001**, low / **verified conditional deduction**: in the common positive-mass left-end model and finite-first-moment setting, W1 of normalized DH measures equals L1 difference of their cumulative level-volume profiles divided by mass. Ordered curves specialize to first-moment difference / mass. Exact terminal-atom formula included. Distinct from prior nonquantitative stochastic-order finding.
- **POME-BC-GAUD-NET-L1-001**, low / **verified repair**: validates the weak-current-to-L1-potential continuity claim in Lemma 20.4.20 for arbitrary directed nets by uniform qpsh L1 compactness and uniqueness of all subnet limits; original statement not shown false.

**Independent arithmetic check:** 22,251 exact rational finite-atom W1/survival-profile cases passed, not a proof of NA analytic facts. New check script: [checks/check_dh_w1_profile.py](checks/check_dh_w1_profile.py). Updated 747-row [SECTION_MATRIX.md](SECTION_MATRIX.md) and historic [LEDGER.md](LEDGER.md) without resetting prior findings. The existing §19.6.16 false statement and §22.1.88 concave-envelope issue remain unresolved; neither reclassified nor repeated as new progress.

**Scope:** Demailly approximation/regularization and the dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale and positivity-loss proof-completion programme remain entirely **deferred-by-user**, not reexamined, resolved or certified. No source/body/canonicalization/permanent-tag change, main write, website publication, GitHub Actions CI, PR/issue creation, merge, full-project tests/build, or formal verification was performed. Remote commit outcome should be verified separately after this checkpoint update.

---

# Pome mathematical audit checkpoint — 2026-10-23 17:37 Asia/Shanghai

**Freshly confirmed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; existing review branch before writes: `f3435da74f5eb748d1d15529b04f3f600ceec4f8`. Re-read main `AGENTS.md`, `documentation/proof-expansions.md`, current main and 25-chapter / **747-section** ToC, and review branch `README.md` / `mathematical-audit/LATEST.md`. The 747 sections are inventory, **not mathematical certification**.

**Actual new inspection:** first selected integrated proof review of §§13.14–13.15; contextual checks of Lemma 5.26.2 and Eq. 5.27.9 only. The `§13.15.2` regularization citation is **deferred-by-user**, not followed. Full assumptions, exact tags, HTML anchors, complete arguments and limitations are in [the dated English report](reports/2026-10-23-root-integrable-weights-and-lr-mass-concentration.md).

- `POME-NPP-WEIGHT-ROOTCAP-001`, **verified conditional deduction / low**: root-integrable weight composition yields *linear* capacity domination; for polynomial weights `(1-u)^(-q)`, `q>n`, this improves the existing sublinear power capacity bound, retaining its broader `q>n-2` range. Conditional upon internal Bedford–Taylor/chain-rule inputs; no source result refuted.
- `POME-HERM-EXP-LR-001`, **verified conditional deduction / low**: the smooth prescribed-mass family has quantitative `O(epsilon_j)` convergence in every fixed finite `L^r` for potentials and `exp(-p w_j)-1`; an unbounded infinite-mass family enjoys analogous `L^r` convergence. This does not imply control of MA mass.

**GitHub synchronization:** verified English report commit `7ac66a8c5d3a6b9617850296f30528a4c0b942c1`, small check script commit `145a407364103b86b51e9b385d835bdfd1005bae`, cumulative 747-row `SECTION_MATRIX.md` update `537b648750eb2e63ab3e0af61aa7fb904eb0751c` (preserving previous entries), cumulative `LEDGER.md` update `1aa7e87cbf80c3c44e925fec3c3de2fdf7cecdbe` (historical statuses preserved). **175 exact scalar SymPy consistency cases passed** (not a formal proof). Remote file/head verification is recorded after this checkpoint. No complete project build, CI, publication, main, source, permanent tag or registry change.

**Strict user exclusion:** dedicated Demailly approximation/regularization, Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss proof-completion remains `deferred-by-user`, not reopened, resolved or certified. Many sections remain inventory-only or partially reviewed; keep rotating.

---

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
