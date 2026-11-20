# Numbered-section mathematical audit coverage matrix

**Inventory baseline:** `main` `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Chapter and section ranges were freshly read from the published `docs/chapters/*/index.html` table of contents on 2026-11-19, totaling **25 chapters and 747 numbered sections**. This is a **coverage accounting register**, not a mathematical certification of all 747 sections. The 2026-11-19 complete direct §17.2 review uses blob 5779ef1a17a52e02052c7485a7aa04adf606aace; the earlier direct §17.18 review uses blob `5d989cf765f5471ce1e2278ef39e2c69979eeb92`.

Statuses: **CURRENT-PARTIAL** means a named result/proof was checked in the current run without whole-section or upstream certification; it can coexist with **LEGACY-UNRECONCILED**. **THIS-RUN-FULL** means the current run directly read every mathematical paragraph of that section, not all its dependencies. **HISTORIC-FULL-REPORTED** and **HISTORIC-PARTIAL-REPORTED** refer only to past recorded audits (see `README.md`, `COVERAGE.md` and dated reports); they are *not* freshly re-certified. **LEGACY-UNRECONCILED** does **not** mean unreviewed: previous partial or full status has not been reconciled from every historical report. No row certifies an entire upstream proof chain. The user-excluded Demailly regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme stays **deferred-by-user**, *not* resolved or certified; the exclusion is at programme/proof level, not a blanket assertion that every Chapter 6 section is excluded. This matrix retains the older ledgers instead of overwriting their findings.

**2026-11-20 direct Chapters 7 and 20 rotation:** §7.5 and §20.5 newly completed as entire direct readings; §§20.6–20.7 rechecked as already historical-full, not newly counted. `POME-BT-NONQC-FIXED-WEIGHT-CONCENTRATION-001` proves the quasi-continuity hypothesis is essential for fixed-weight Bedford–Taylor convergence; [proof](reports/2026-11-20-bt-discontinuous-weight-hyperplane-concentration.md), [exact scope](coverage/2026-11-20-ch7-capacity-ch20-divisors.md). **+2 newly whole direct sections / 2 repeats / +0 full dependency certifications.** No prior findings repeated; excluded programmes deferred-by-user.

**2026-11-19 further broad rotation:** §11.5 (Gauduchon conserved trace mass) is directly reviewed end-to-end (three printed statements and proofs); verified a sharp square-root anisotropy remainder strengthening Equation 11.5.6, with precise equality and closed/Kähler rigidity. [Full proof](reports/2026-11-19-gauduchon-trace-quantitative-amgm-deficit.md). **+1 whole direct section, +0 fully verified transitive chains;** the legacy first-visit status remains unreconciled. No deferred-by-user analytic programme is reopened.

**2026-11-19 targeted Chapter 20 rotation:** §20.3.44 and a selected downstream use were checked; the sharp Jacobian-step budget and fixed-level ramified multiplier-ideal carry are new *conditional deductions*, not printed errors or a whole-section audit. [Proof](reports/2026-11-19-divisorial-extraction-jacobian-and-ramified-multiplier-ideals.md). +1 selected partial section; +0 full sections / +0 complete dependency chains; earlier rows, 25/747 inventory and deferred exclusions preserved.

**2026-11-19 Chapter 23 direct rotation:** all of §23.3's current mathematical text and printed proof were read; a Lyapunov ellipsoid-flow cross-section proves the stronger smooth product (S^3\times S^1) and no-symplectic conclusion, with no printed error claimed. [Anchored report](reports/2026-11-19-hopf-quotient-lyapunov-smooth-topology.md). **+1 whole direct section; +0 complete upstream chains; old partial visits retained.** The user-excluded regularization programmes remain deferred-by-user.

**2026-11-19 Chapter 19 new proof audit:** §19.2 now directly checked end-to-end; selected §19.7 Theorem 19.7.20 receives an elementary complete audit-only replacement for the general Kaveh–Khovanskii counting/existence input, including the precise generated-lattice index. The earlier 2026-11-05 conductor is reused, **not rediscovered**. [English proof](reports/2026-11-19-full-semigroup-volume-lattice-index-proof.md). **+1 whole direct section (§19.2), +1 partial section (§19.7), +0 fully certified transitive downstream chains**; historical first visits unreconciled; exclusions deferred-by-user.

**2026-11-19 Chapter 16 contact-support rotation:** §§16.12–16.13 were each directly reviewed in full, including local Radon-order tests, ordered-potential contact comparison, bounded/l.s.c. obstacle replacements, quasi-continuous capacity limit, and finite rooftop. New verified conditional deduction `POME-ROOFTOP-CONTACT-MEASURE-MEET-001` removes overlap double counting by a lattice-meet measure on exact Borel contact strata; the printed corollary remains true. [Proof](reports/2026-11-19-rooftop-contact-measure-meet.md). **+2 full direct sections; +0 complete upstream-chain certificates.** Historical first visits remain unreconciled; excluded regularization work remains deferred-by-user.

**2026-11-19 Chapter 22 selected rotation:** Proposition 22.1.39 lines 614–674 was directly checked and strengthened by a background-form equi-Lipschitz bound and arbitrary-family scalar minimax, with a sharp linear example; [new report](reports/2026-11-19-na-background-mass-uniform-lipschitz-minimax.md). +1 selected partial review, +0 whole sections or fully verified chains; prior §22.1 partial visits and deferred exclusions retained.

**2026-11-19 Chapter 21 new direct rotation:** complete §21.8 directly read; selected §21.9.5 section-basis proof checked. Exact fixed-point jet threshold [report](reports/2026-11-19-toric-fixed-point-jet-edge-threshold.md) and [coverage](coverage/2026-11-19-toric-fixed-point-jet-edge-threshold.md). **+1 whole section, +1 selected partial, +0 completed transitive chains**; deferred-by-user programme unchanged.

**2026-11-19 Chapter 9 broad rotation:** directly read all of §9.18 and found a sharp supporting-half-plane log-boundary inequality, with properness and geodesicity consequences (no false printed claim). [Proof](reports/2026-11-19-convex-kobayashi-boundary-distance-proper-geodesic.md). **+1 whole direct section, +0 certified upstream chains**; previously excluded programme untouched.

**2026-11-19 Chapter 7 renewed broad direct review:** all of §7.13 read in the current integrated edition, including both Sobolev lemmas and two contact-product propositions. New exact Hall–Rado rank support criterion [proof](reports/2026-11-19-bt-contact-mixed-discriminant-hall-rank.md). **+1 whole section directly reviewed, +0 transitive proof certificates**; earlier partial work retained, no first-ever claim; Demailly and associated exclusions remain deferred-by-user.

**2026-11-19 Chapter 13 full direct rotation:** mathematical §13.2 lines 7–165 read end-to-end. **New:** exact total-variation rate for *canonical level-k truncations*, \(Ck^{-(1-a-b)/\max(a,b)}\), and sharp critical/supercritical growth, [proof](reports/2026-11-19-mixed-npp-truncation-tv-rate.md). **Correction:** the mixed integrability threshold itself was already established in the 2026-11-11 **POME-NPP-MIXED-POWER-SUM-THRESHOLD-001**; the preliminary 2026-11-19 threshold note was withdrawn as duplicate, [correction](reports/2026-11-19-mixed-power-nonpluripolar-threshold.md). **+1 whole direct section, +0 fully certified upstream chains, no first-ever visit claim;** excluded programmes deferred-by-user.

**2026-11-19 new Chapter 17 rotation:** §17.4 (continuity and compactness) fully read directly; smooth strictly \(\omega_{\rm FS}\)-psh sequences realize every prescribed finite loss of Monge–Ampère energy despite weak convergence of their positive Monge–Ampère measures, with exact atomic Dirichlet-energy concentration. [Proof](reports/2026-11-19-smooth-psh-energy-defect-spectrum.md) · [coverage](coverage/2026-11-19-smooth-psh-energy-defect-spectrum.md). **+1 whole direct section, +0 transitive dependency certifications**; historic first-visit unverified, excluded programme still deferred-by-user.

**2026-11-20 direct section rotation:** All mathematical content of §9.4 (normalization; physical lines 7–199) was freshly reviewed. The new **POME-NORM-NORMAL-LOCUS-LIFTING-001** establishes a unique normal-source lifting through finite normalization when the preimage of the nonnormal locus is nowhere dense, with a nodal constant-disc counterexample to unconditional uniqueness. [Detailed proof](reports/2026-11-20-normal-locus-lifting-through-normalization.md). **+1 whole direct section, +0 fully certified transitive chains; previous §9.4 visits not recounted**. Excluded Demailly and dedicated analytic work remains deferred-by-user.

**2026-11-20 complete §3.9 rotation:** directly reviewed all three planar distance–convexity propositions and full printed proofs, adding a complete standalone proof of the unlinked closed-connected-locally-convex lemma in §3.9.2 and proving firm projection nonexpansivity. [Report](reports/2026-11-20-planar-distance-local-convexity-and-firm-projection.md). **+1 directly read whole section, +0 transitive proof-chain certificates, no first-visit assertion**; excluded programmes remain deferred-by-user.

**2026-11-20 Chapter 8 addition:** full direct §8.2 and §8.12 reading, special `m=2` self-contained Lorentz cone proof and sharp negative coefficient interval. [Dated report](reports/2026-11-20-hessian-two-cone-lorentz-locality.md). **+2 full directly read sections, +0 certified upstream chains.** Earlier partial visits remain; deferred-by-user programme unchanged.

**2026-11-20 broad Bedford–Taylor rotation:** full direct §§7.2 and 7.33, selected §7.4.4 only. Net continuity and a divisorial failure of capacity continuity are [proved here](reports/2026-11-20-bt-divisorial-capacity-collapse-and-net-stability.md). +2 entire sections, +1 selected input, +0 complete upstream chains; no historical first-visit claim. Excluded analytic programmes deferred-by-user.

**2026-11-20 Chapter 19 direct rotation:** §19.3 fully reviewed (lines 7–387) with new positive-current blowup valuation \((a,b)\mapsto(a,b-ra)\); §19.10 wholly reread (prior HISTORIC-FULL-REPORTED) without reopening analytic Morse proofs. [Detailed report](reports/2026-11-20-positive-current-flag-blowup-negative-valuations.md). **+1 newly full direct section, 1 repeat whole section, +0 complete upstream chains.** Excluded proof programmes remain deferred-by-user.

## Verified current table-of-contents chapter counts

| Chapter (live TOC) | Sections | Exact numbered range |
| --- | ---: | --- |
| **[1. Conventions](../../docs/chapters/orientation/)** | 1 | §1.1–§1.1 |
| **[2. Measures, distributions, and convergence](../../docs/chapters/measures-distributions/)** | 24 | §2.1–§2.24 |
| **[3. Harmonic and subharmonic functions](../../docs/chapters/classical-potentials/)** | 10 | §3.1–§3.10 |
| **[4. Energy, capacity, and fine topology](../../docs/chapters/capacity-fine-topology/)** | 5 | §4.1–§4.5 |
| **[5. Plurisubharmonic functions and positive currents](../../docs/chapters/psh-positive-currents/)** | 66 | §5.1–§5.66 |
| **[6. Lelong numbers, multiplier ideals, and regularization](../../docs/chapters/singularities-regularization/)** | 56 | §6.1–§6.56 |
| **[7. Local Monge–Ampère theory and capacity](../../docs/chapters/local-monge-ampere/)** | 33 | §7.1–§7.33 |
| **[8. Complex Hessian equations](../../docs/chapters/complex-hessian-equations/)** | 13 | §8.1–§8.13 |
| **[9. Complex spaces and modifications](../../docs/chapters/complex-spaces/)** | 77 | §9.1–§9.77 |
| **[10. Cohomology, positivity, and geometric loci](../../docs/chapters/positivity-cohomology/)** | 109 | §10.1–§10.109 |
| **[11. Hermitian geometry, torsion, and Gauduchon duality](../../docs/chapters/hermitian-torsion/)** | 49 | §11.1–§11.49 |
| **[12. Gauduchon variational volume](../../docs/chapters/gauduchon-variational-volume/)** | 36 | §12.1–§12.36 |
| **[13. Non-pluripolar measures and mass](../../docs/chapters/non-pluripolar-mass/)** | 32 | §13.1–§13.32 |
| **[14. Monge–Ampère equations and stability](../../docs/chapters/monge-ampere-equations/)** | 29 | §14.1–§14.29 |
| **[15. Monge–Ampère equations with prescribed singularities](../../docs/chapters/singular-monge-ampere-equations/)** | 37 | §15.1–§15.37 |
| **[16. Singularity types, envelopes, and models](../../docs/chapters/envelopes-models/)** | 44 | §16.1–§16.44 |
| **[17. Energy, geodesics, rays, and test curves](../../docs/chapters/energy-geodesics/)** | 18 | §17.1–§17.18 |
| **[18. Multiplier-ideal models and partial equilibrium](../../docs/chapters/ideal-goodness/)** | 47 | §18.1–§18.47 |
| **[19. Sections, graded series, and Okounkov bodies](../../docs/chapters/sections-okounkov/)** | 11 | §19.1–§19.11 |
| **[20. B-divisors and restriction](../../docs/chapters/divisors-restriction/)** | 8 | §20.1–§20.8 |
| **[21. Toric and convex geometry](../../docs/chapters/toric-convex/)** | 14 | §21.1–§21.14 |
| **[22. Non-Archimedean pluripotential theory](../../docs/chapters/non-archimedean/)** | 1 | §22.1–§22.1 |
| **[23. Hopf and locally conformally Kähler geometry](../../docs/chapters/hopf-lck/)** | 3 | §23.1–§23.3 |
| **[24. Problems in pluripotential theory](../../docs/chapters/problems-history/)** | 13 | §24.1–§24.13 |
| **[25. Historical and bibliographical notes](../../docs/chapters/historical-notes/)** | 11 | §25.1–§25.11 |

**2026-11-19 next rotation:** §2.21 whole integrated section directly checked (Proposition 2.21.2, Theorem 2.21.3, Corollary 2.21.5), +1 direct complete reading, +0 certified upstream chains. [Curvature/orthogonality proof](reports/2026-11-19-metric-connection-curvature-orthogonality.md). Previously deferred-by-user items remain deferred.

**2026-11-19 incremental rotation:** §4.5 selected direct review only (Theorems 4.5.2/4/6 and Example 4.5.5), +0 whole sections, +0 transitive proofs. See [dated proof](reports/2026-11-19-nested-compact-balayage-energy-continuity.md). The matrix is not a certification of the entire collection.

**2026-11-20 whole direct Chapter 4 rotation:** §4.3 mathematical lines 7–131 directly read, with an independent dense-polar-set / G_delta pole-locus Baire obstruction (POME-CLASS-DENSE-POLAR-GDELTA-OBSTRUCTION-001). All original printed statements remain unrefuted; [proof](reports/2026-11-20-classical-dense-polar-gdelta-obstruction.md), [exact coverage](coverage/2026-11-20-ch4-dense-polar-gdelta-obstruction.md). **+1 direct whole section, +0 complete upstream chains, no first-ever visit claim.** Earlier §4.3 partial reports remain; user-excluded Demailly-related programmes stay deferred-by-user.

**2026-11-20 rotation:** entire §§13.7 and 17.9 read directly, with a non-pluripolar extended-capacity and quasi-continuously weighted **directed-net** stability deduction, [proof](reports/2026-11-20-npp-directed-capacity-nets-and-long-segment-review.md). §17.9 yielded no new finding. **+2 entire directly read sections / +0 transitive proof certificates; historical first visits unreconciled.** User-excluded regularization programmes deferred-by-user.

## Per-section status register (all 747 numbers)

These numbers come from the contiguous reader numbering on the individual current chapter index pages. Titles and permanent tags are resolved from the linked chapter/section pages; important new line/tag anchors are recorded in the dated report. Treat a status of LEGACY-UNRECONCILED as **unknown coverage**, not proof that a section has never been visited.

| Reader section | Coverage status | Evidence/notes |
| --- | --- | --- |
| §1.1 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §2.1 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §2.2 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §2.3 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §2.4 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §2.5 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §2.6 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §2.7 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §2.8 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §2.9 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §2.10 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §2.11 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §2.12 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §2.13 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §2.14 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §2.15 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §2.16 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §2.17 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §2.18 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §2.19 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §2.20 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §2.21 | THIS-RUN-FULL; LEGACY-UNRECONCILED | **2026-11-19, POME-CONN-CURVATURE-ORTHOGONALITY-IFF-FLAT-001**: complete direct reading of lines 7–103, [report](reports/2026-11-19-metric-connection-curvature-orthogonality.md), [coverage](coverage/2026-11-19-ch2-metric-connection-curvature-orthogonality.md); +0 transitive certificates; legacy first-visit unverified |
| §2.22 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §2.23 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §2.24 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §3.1 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §3.2 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §3.3 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §3.4 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §3.5 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §3.6 | HISTORIC-FULL-REPORTED | See existing dated reports and COVERAGE.md |
| §3.7 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §3.8 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §3.9 | THIS-RUN-FULL; HISTORIC-PARTIAL-REPORTED; LEGACY-UNRECONCILED | **2026-11-20: direct complete mathematical lines 7–107**, blob `25fd0fd57d3e51f9224a25341ace77584b2a1a2a`; self-contained local-convexity geodesic repair `POME-PLANAR-DISTANCE-LOCAL-CONVEX-GEODESIC-001`, [report](reports/2026-11-20-planar-distance-local-convexity-and-firm-projection.md), [coverage](coverage/2026-11-20-planar-distance-local-convexity-and-firm-projection.md); no full upstream certification and no historic first-visit claim |
| §3.10 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §4.1 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §4.2 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §4.3 | THIS-RUN-FULL; HISTORIC-PARTIAL-REPORTED; LEGACY-UNRECONCILED | **2026-11-20: complete §4.3 mathematical lines 7–131**, blob aa814f26482e8ed27e51c945e9202c797449158b; new conditional deduction **POME-CLASS-DENSE-POLAR-GDELTA-OBSTRUCTION-001** (arbitrary polar containment does not imply exact poles); [proof](reports/2026-11-20-classical-dense-polar-gdelta-obstruction.md), [scope](coverage/2026-11-20-ch4-dense-polar-gdelta-obstruction.md). No printed theorem refuted, no fully certified upstream chains, no first-ever visit claim; previous §4.3 partial reports retained |
| §4.4 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §4.5 | CURRENT-PARTIAL; LEGACY-UNRECONCILED | **2026-11-19, POME-CLASSICAL-NESTED-COMPACT-SWEEP-ENERGY-001:** directly checked Theorems 4.5.2, 4.5.4, 4.5.6 and Example 4.5.5, printed lines 17–88; [new energy-sweep result](reports/2026-11-19-nested-compact-balayage-energy-continuity.md), [coverage](coverage/2026-11-19-ch4-nested-compact-green-sweeping.md); Martin items 4.5.8–13 and upstream chains not certified; prior history remains unreconciled |
| §5.1 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.2 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.3 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.4 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.5 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.6 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.7 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.8 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.9 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.10 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.11 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.12 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.13 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.14 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.15 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.16 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.17 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.18 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.19 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.20 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.21 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.22 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.23 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.24 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.25 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.26 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.27 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.28 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.29 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.30 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.31 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.32 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.33 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.34 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.35 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.36 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.37 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.38 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.39 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.40 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.41 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.42 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.43 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.44 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.45 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.46 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.47 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.48 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.49 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.50 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.51 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.52 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.53 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.54 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.55 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.56 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.57 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.58 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.59 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.60 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.61 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.62 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.63 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.64 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.65 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §5.66 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.1 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.2 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.3 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.4 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.5 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.6 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.7 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.8 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.9 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.10 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.11 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.12 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.13 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.14 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.15 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.16 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.17 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.18 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.19 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.20 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.21 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.22 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.23 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.24 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.25 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.26 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.27 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.28 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.29 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.30 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.31 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.32 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.33 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.34 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.35 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.36 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.37 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.38 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.39 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.40 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.41 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.42 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.43 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.44 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.45 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.46 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.47 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.48 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.49 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.50 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.51 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.52 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.53 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.54 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.55 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §6.56 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.1 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.2 | THIS-RUN-FULL; LEGACY-UNRECONCILED | **2026-11-20 complete direct**, math lines 5–159, blob `18bd2395f3b76941b2c677079c09eb6accc5a9cb`; two new verified conditional deductions ([proof](reports/2026-11-20-bt-divisorial-capacity-collapse-and-net-stability.md)); +0 transitive chains, historical first visit unreconciled |
| §7.3 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.4 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.5 | THIS-RUN-FULL; LEGACY-UNRECONCILED | **2026-11-20 full direct mathematical lines 6–190**, blob `464778b7ca6f1a456e36b24ecb4a0c93ab6948d3`, essential quasi-continuous weight restriction demonstrated by `POME-BT-NONQC-FIXED-WEIGHT-CONCENTRATION-001` ([report](reports/2026-11-20-bt-discontinuous-weight-hyperplane-concentration.md)); prior §7.5 partial audits preserved, +0 full transitive chains |
| §7.6 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.7 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.8 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.9 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.10 | HISTORIC-FULL-REPORTED | See existing dated reports and COVERAGE.md |
| §7.11 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.12 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.13 | THIS-RUN-FULL; HISTORIC-PARTIAL-REPORTED | **2026-11-19 / POME-BT-CONTACT-MIXED-DISCRIMINANT-HALL-RANK-001:** complete lines 7–138; [report](reports/2026-11-19-bt-contact-mixed-discriminant-hall-rank.md), [coverage](coverage/2026-11-19-bt-contact-mixed-discriminant-hall-rank.md); prior 2026-11-10 critical-L^n work preserved; +0 certified transitive chains and no first-visit claim |
| §7.14 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.15 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.16 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.17 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.18 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.19 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.20 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.21 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.22 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.23 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.24 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.25 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.26 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.27 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.28 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.29 | HISTORIC-PARTIAL-REPORTED | See existing dated reports and COVERAGE.md |
| §7.30 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.31 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.32 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §7.33 | THIS-RUN-FULL; LEGACY-UNRECONCILED | **2026-11-20 complete direct**, math lines 5–81, blob `a859ac5637379266fa191831656f214c51676ca1`; exact separated product factor confirmed, [coverage](coverage/2026-11-20-bt-divisorial-capacity-collapse-and-net-stability.md); prior findings not recounted, +0 transitive chains |
| §8.1 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §8.2 | THIS-RUN-FULL; LEGACY-UNRECONCILED | **2026-11-20 complete direct** lines 6–269, [Lorentz proof](reports/2026-11-20-hessian-two-cone-lorentz-locality.md); previous selected §8.2.5/7 audits preserved; +0 transitive certificates, no first-visit claim |
| §8.3 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §8.4 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §8.5 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §8.6 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §8.7 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §8.8 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §8.9 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §8.10 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §8.11 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §8.12 | THIS-RUN-FULL; LEGACY-UNRECONCILED | **2026-11-20 complete direct** lines 6–170, [proof audit](reports/2026-11-20-hessian-two-cone-lorentz-locality.md); previous 2026-11-19 §8.12.4 partial [report](reports/2026-11-19-hessian-mixed-mass-uniform-lipschitz.md) retained; §8.11 dependencies not certified |
| §8.13 | CURRENT-PARTIAL; LEGACY-UNRECONCILED | §8.13.1 mixed mass and §8.13.4–5 context checked in 2026-11-19 [report](reports/2026-11-19-hessian-mixed-mass-uniform-lipschitz.md); past partial checks retained |
| §9.1 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.2 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.3 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.4 | THIS-RUN-FULL; LEGACY-UNRECONCILED | **2026-11-20**, entire integrated mathematical lines 7–199, [report](reports/2026-11-20-normal-locus-lifting-through-normalization.md); +0 transitive chains, no historic first-visit claim; previous normalization/conductor/gluing findings retained |
| §9.5 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.6 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.7 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.8 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.9 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.10 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.11 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.12 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.13 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.14 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.15 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.16 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.17 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.18 | THIS-RUN-FULL; LEGACY-UNRECONCILED | **2026-11-19 `POME-CONVEX-KOBAYASHI-LOG-BOUNDARY-PROPER-GEODESIC-001`:** directly reviewed all §9.18 lines 10–95, new sharp log-boundary-distance/proper-geodesic conditional deduction; [proof](reports/2026-11-19-convex-kobayashi-boundary-distance-proper-geodesic.md), [coverage](coverage/2026-11-19-convex-kobayashi-boundary-distance-proper-geodesic.md); +0 certified upstream chains; historical first visit unreconciled |
| §9.19 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.20 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.21 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.22 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.23 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.24 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.25 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.26 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.27 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.28 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.29 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.30 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.31 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.32 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.33 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.34 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.35 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.36 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.37 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.38 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.39 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.40 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.41 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.42 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.43 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.44 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.45 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.46 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.47 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.48 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.49 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.50 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.51 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.52 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.53 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.54 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.55 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.56 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.57 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.58 | HISTORIC-FULL-REPORTED | See existing dated reports and COVERAGE.md |
| §9.59 | HISTORIC-FULL-REPORTED | See existing dated reports and COVERAGE.md |
| §9.60 | HISTORIC-FULL-REPORTED | See existing dated reports and COVERAGE.md |
| §9.61 | HISTORIC-FULL-REPORTED | See existing dated reports and COVERAGE.md |
| §9.62 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.63 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.64 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.65 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.66 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.67 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.68 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.69 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.70 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.71 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.72 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.73 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.74 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.75 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.76 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §9.77 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.1 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.2 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.3 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.4 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.5 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.6 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.7 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.8 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.9 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.10 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.11 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.12 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.13 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.14 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.15 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.16 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.17 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.18 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.19 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.20 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.21 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.22 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.23 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.24 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.25 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.26 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.27 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.28 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.29 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.30 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.31 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.32 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.33 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.34 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.35 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.36 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.37 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.38 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.39 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.40 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.41 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.42 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.43 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.44 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.45 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.46 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.47 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.48 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.49 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.50 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.51 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.52 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.53 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.54 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.55 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.56 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.57 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.58 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.59 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.60 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.61 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.62 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.63 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.64 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.65 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.66 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.67 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.68 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.69 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.70 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.71 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.72 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.73 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.74 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.75 | HISTORIC-FULL-REPORTED | See existing dated reports and COVERAGE.md |
| §10.76 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.77 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.78 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.79 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.80 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.81 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.82 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.83 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.84 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.85 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.86 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.87 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.88 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.89 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.90 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.91 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.92 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.93 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.94 | THIS-RUN-FULL; LEGACY-UNRECONCILED | **2026-11-19, POME-KAHLER-METRIC-QUADRATIC-JET-MINIMAX-001**: whole mathematical text lines 7–77, blob `4fd58352bd134c2715fc4cbf1e0074a42a7e0657`; [proof](reports/2026-11-19-kahler-metric-curvature-optimal-quadratic-jet.md), [coverage](coverage/2026-11-19-ch10-kahler-normal-metric-jet.md); no transitive certification or historical first-visit claim |
| §10.95 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.96 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.97 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.98 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.99 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.100 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.101 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.102 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.103 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.104 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.105 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.106 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.107 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.108 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §10.109 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.1 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.2 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.3 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.4 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.5 | THIS-RUN-FULL | **2026-11-19:** entire mathematical lines 5–82 directly audited; integrated blob `34af83ff391b5e5590cd9cb10ca4cd2b3faff02c`, main `b6933b772f41b45918f7e25ed1afbbb1fd892272`; [sharp trace deficit/equality theorem](reports/2026-11-19-gauduchon-trace-quantitative-amgm-deficit.md), [ledger](ledger/2026-11-19-gauduchon-trace-quantitative-amgm-deficit.md). +1 whole direct section, +0 upstream chains; historical first visit unresolved. |
| §11.6 | HISTORIC-FULL-REPORTED | See existing dated reports and COVERAGE.md |
| §11.7 | THIS-RUN-FULL; LEGACY-UNRECONCILED | **2026-11-20:** complete §11.7 mathematical lines 5–76 directly checked, main `b6933b772f41b45918f7e25ed1afbbb1fd892272`, blob `31d17f258f2ff178bf52be3d3f92d5a995878d3a`, permanent tags `155386134D9E`, `A97DA8CE2358`; [exact slopes and weak superdifferential](reports/2026-11-20-gauduchon-threshold-superdifferential.md) · [coverage](coverage/2026-11-20-ch11-gauduchon-threshold-superdifferential.md). +1 whole direct section, +0 transitive certificates; prior historical visit remains unreconciled and excluded topics deferred-by-user |
| §11.8 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.9 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.10 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.11 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.12 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.13 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.14 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.15 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.16 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.17 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.18 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.19 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.20 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.21 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.22 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.23 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.24 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.25 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.26 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.27 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.28 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.29 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.30 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.31 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.32 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.33 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.34 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.35 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.36 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.37 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.38 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.39 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.40 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.41 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.42 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.43 | HISTORIC-PARTIAL-REPORTED | See existing dated reports and COVERAGE.md |
| §11.44 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.45 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.46 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.47 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.48 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §11.49 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.1 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.2 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.3 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.4 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.5 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.6 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.7 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.8 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.9 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.10 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.11 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.12 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.13 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.14 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.15 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.16 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.17 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.18 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.19 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.20 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.21 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.22 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.23 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.24 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.25 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.26 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.27 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.28 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.29 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.30 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.31 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.32 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.33 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.34 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.35 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §12.36 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §13.1 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §13.2 | THIS-RUN-FULL; LEGACY-UNRECONCILED | **2026-11-19** complete direct lines 7–165, integrated blob `81be8c5acc360c96bd3c5acba05a3cdb5fafaf4c`, Lemma `D59675D9F6D8`, Example `6F4C920FEDCA`. **New:** POME-NPP-MIXED-TRUNCATION-TV-RATE-001 exact level-k cutoff rate, [proof](reports/2026-11-19-mixed-npp-truncation-tv-rate.md), [coverage](coverage/2026-11-19-mixed-npp-truncation-tv-rate.md). Preliminary POME-NPP-MIXED-POWER-CROSS-THRESHOLD-001 withdrawn as duplicate of Nov 11 [original](reports/2026-11-11-mixed-nonpluripolar-power-sum-threshold.md). +0 fully certified transitive chains; no first-ever visit claim |
| §13.3 | THIS-RUN-FULL; LEGACY-UNRECONCILED | **2026-11-20** full direct mathematical lines 7–50, Theorem 13.3.1 tag `8A125B338F90`; [audited proof + new analytic-excision deduction](reports/2026-11-20-analytic-set-excision-and-divisorial-npp-mass.md). No transitive proof-chain certification; historical first visit unknown |
| §13.4 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §13.5 | HISTORIC-PARTIAL-REPORTED | See existing dated reports and COVERAGE.md |
| §13.6 | THIS-RUN-FULL; HISTORIC-PARTIAL-REPORTED | **2026-11-20** full direct mathematical lines 7–57, tags `BEC54934FC2C` / `0811FFDF15B7`; new divisorial NPP invariance and cohomological discrepancy [proof](reports/2026-11-20-analytic-set-excision-and-divisorial-npp-mass.md). Earlier partial visits retained; no upstream-chain certificate |
| §13.7 | THIS-RUN-FULL; HISTORIC-PARTIAL-REPORTED; LEGACY-UNRECONCILED | **2026-11-20** whole direct lines 7–209, main blob `d66813856cb813722806ab912afdfd4815d2da97`, new verified conditional `POME-NPP-CAPACITY-DIRECTED-NET-WEIGHTED-001` ([full proof](reports/2026-11-20-npp-directed-capacity-nets-and-long-segment-review.md); [coverage](coverage/2026-11-20-ch13-directed-capacity-nets-ch17-long-segments.md)); no printed error or full transitive certificate; previous partial reports retained, no first-visit assertion |
| §13.8 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §13.9 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §13.10 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §13.11 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §13.12 | HISTORIC-FULL-REPORTED | See existing dated reports and COVERAGE.md |
| §13.13 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §13.14 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §13.15 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §13.16 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §13.17 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §13.18 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §13.19 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §13.20 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §13.21 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §13.22 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §13.23 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §13.24 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §13.25 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §13.26 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §13.27 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §13.28 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §13.29 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §13.30 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §13.31 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §13.32 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §14.1 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §14.2 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §14.3 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §14.4 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §14.5 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §14.6 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §14.7 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §14.8 | THIS-RUN-FULL; HISTORIC-PARTIAL-REPORTED | **2026-11-20** full direct lines 5–70, theorem C611B2CA264A, blob 34526fcac6d5f30e71a98cadc88a4c76817546c4; new general-Hermitian trace-free variance identity [proof](reports/2026-11-20-ma-scalar-variance-hopf-fiber-hessian.md). Existing 2026-11-06 Kähler-only result and duplicate retained, not new; upstream not certified |
| §14.9 | THIS-RUN-FULL; HISTORIC-UNRECONCILED | **2026-11-20** full direct lines 5–105, tags CA9F2EF1D149/BFCF1480CC8B/9CEA8A3A68F0, blob a0c390cff1768118798824a64318c416636b9b91; Hopf scalar/fiber variance balance and independent visible equation duplicate [proof](reports/2026-11-20-ma-scalar-variance-hopf-fiber-hessian.md); historic first visits not established, no upstream certification |
| §14.10 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §14.11 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §14.12 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §14.13 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §14.14 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §14.15 | HISTORIC-FULL-REPORTED | See existing dated reports and COVERAGE.md |
| §14.16 | HISTORIC-FULL-REPORTED | See existing dated reports and COVERAGE.md |
| §14.17 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §14.18 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §14.19 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §14.20 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §14.21 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §14.22 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §14.23 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §14.24 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §14.25 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §14.26 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §14.27 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §14.28 | THIS-RUN-FULL | **2026-11-19:** complete current mathematical lines 7–157 directly read (blob 7a70517262563acf523940c261daa8ec11a8cb55); [even-order ODE proof](reports/2026-11-19-even-order-degenerate-density-nonuniqueness.md). +1 direct full section, +0 complete transitive chains; first-visit status unreconciled. Original theorem stands; all user-excluded programmes deferred-by-user |
| §14.29 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.1 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.2 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.3 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.4 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.5 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.6 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.7 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.8 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.9 | HISTORIC-FULL-REPORTED | See existing dated reports and COVERAGE.md |
| §15.10 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.11 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.12 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.13 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.14 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.15 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.16 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.17 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.18 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.19 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.20 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.21 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.22 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.23 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.24 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.25 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.26 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.27 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.28 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.29 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.30 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.31 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.32 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.33 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.34 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.35 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.36 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §15.37 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.1 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.2 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.3 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.4 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.5 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.6 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.7 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.8 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.9 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.10 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.11 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.12 | THIS-RUN-FULL | **2026-11-19:** full current mathematical lines 7–47 (blob c3be9349468d2203c0b67f4bee2be49d1392f8ff); [contact measure report](reports/2026-11-19-rooftop-contact-measure-meet.md). +1 direct full section, no transitive certification; historic first visit unreconciled |
| §16.13 | THIS-RUN-FULL | **2026-11-19:** full current mathematical lines 7–165 (blob 840ebcb98be09245369315fa0c0288b936040098); prior partial reviews retained. [Measure lattice meet proof](reports/2026-11-19-rooftop-contact-measure-meet.md). +1 direct full section, no transitive certification; historic first visit unreconciled |
| §16.14 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.15 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.16 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.17 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.18 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.19 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.20 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.21 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.22 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.23 | HISTORIC-FULL-REPORTED | See existing dated reports and COVERAGE.md |
| §16.24 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.25 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.26 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.27 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.28 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.29 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.30 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.31 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.32 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.33 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.34 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.35 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.36 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.37 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.38 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.39 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.40 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.41 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.42 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.43 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §16.44 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §17.1 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §17.2 | THIS-RUN-FULL | **2026-11-19:** entire current integrated section directly read (blob 5779ef1a17a52e02052c7485a7aa04adf606aace); [anchored report](reports/2026-11-19-bounded-qpsh-difference-dirichlet-seminorm.md), [ledger](ledger/2026-11-19-bounded-qpsh-difference-dirichlet-seminorm.md). Full upstream chain not certified; legacy first-visit status unknown |
| §17.3 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §17.4 | THIS-RUN-FULL; LEGACY-UNRECONCILED | **2026-11-19, POME-ENERGY-SMOOTH-L1-DEFECT-SPECTRUM-001**: entire integrated §17.4 lines 7–242, [proof](reports/2026-11-19-smooth-psh-energy-defect-spectrum.md), [coverage](coverage/2026-11-19-smooth-psh-energy-defect-spectrum.md); +0 transitive-chain certifications; historic first visit unverified |
| §17.5 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §17.6 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §17.7 | HISTORIC-PARTIAL-REPORTED | See existing dated reports and COVERAGE.md |
| §17.8 | THIS-RUN-FULL; HISTORIC-PARTIAL-REPORTED; LEGACY-UNRECONCILED | **2026-11-20:** §17.8 full direct lines 7–112, blob `8d9b7af925289346c96df751c67049e90c9dfe1d`, POME-GEO-SUBGEODESIC-ENERGY-CURVATURE-001; [proof](reports/2026-11-20-subgeodesic-energy-curvature-measure.md), [exact coverage](coverage/2026-11-20-subgeodesic-energy-curvature-measure.md); earlier selected visits preserved, +0 complete upstream chains |
| §17.9 | THIS-RUN-FULL; HISTORIC-PARTIAL-REPORTED; LEGACY-UNRECONCILED | **2026-11-20** whole direct lines 7–75, main blob `023e78b3da0fd8f33d39177dba02f410b10f376c`; both printed propositions/proofs checked, no new finding; [coverage](coverage/2026-11-20-ch13-directed-capacity-nets-ch17-long-segments.md); previous slope results preserved, +0 full transitive certificates |
| §17.10 | HISTORIC-PARTIAL-REPORTED | See existing dated reports and COVERAGE.md |
| §17.11 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §17.12 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §17.13 | HISTORIC-PARTIAL-REPORTED | See existing dated reports and COVERAGE.md |
| §17.14 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §17.15 | HISTORIC-PARTIAL-REPORTED | See existing dated reports and COVERAGE.md |
| §17.16 | HISTORIC-PARTIAL-REPORTED | See existing dated reports and COVERAGE.md |
| §17.17 | HISTORIC-PARTIAL-REPORTED | See existing dated reports and COVERAGE.md |
| §17.18 | THIS-RUN-FULL | [2026-11-19 report](reports/2026-11-19-legendre-two-branch-mixed-mass.md), physical lines 7–63 |
| §18.1 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.2 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.3 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.4 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.5 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.6 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.7 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.8 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.9 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.10 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.11 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.12 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.13 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.14 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.15 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.16 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.17 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.18 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.19 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.20 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.21 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.22 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.23 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.24 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.25 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.26 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.27 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.28 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.29 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.30 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.31 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.32 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.33 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.34 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.35 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.36 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.37 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.38 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.39 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.40 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.41 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.42 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.43 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.44 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.45 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.46 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §18.47 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §19.1 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §19.2 | THIS-RUN-FULL; LEGACY-UNRECONCILED | **2026-11-19, POME-OKO-GENERAL-LATTICE-INDEX-COUNTING-001:** directly read all mathematical lines 7–134; [general graded-lattice volume proof](reports/2026-11-19-full-semigroup-volume-lattice-index-proof.md) and [exact coverage](coverage/2026-11-19-ch19-full-semigroup-counting.md); +0 complete downstream-chain certifications; prior first visit unreconciled |
| §19.3 | THIS-RUN-FULL; LEGACY-UNRECONCILED | **2026-11-20 entire mathematical lines 7–387**; [positive-current model valuation](reports/2026-11-20-positive-current-flag-blowup-negative-valuations.md); older partial review retained, +0 full transitive chains |
| §19.4 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §19.5 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §19.6 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §19.7 | CURRENT-PARTIAL; HISTORIC-PARTIAL-REPORTED | **2026-11-19:** directly reviewed Theorem 19.7.20 and selected adjacent lines 299–341, 369–412; audit-only [general counting proof](reports/2026-11-19-full-semigroup-volume-lattice-index-proof.md) builds on previously verified **2026-11-05** interior-conductor proof (not counted anew); rest of §19.7 not fully audited |
| §19.8 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §19.9 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §19.10 | HISTORIC-FULL-REPORTED; THIS-RUN-FULL | **2026-11-20 whole repeat** lines 7–22, conditional Morse proof step; [coverage](coverage/2026-11-20-positive-current-flag-blowup-negative-valuations.md); no newly unique section |
| §19.11 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §20.1 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §20.2 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §20.3 | CURRENT-PARTIAL; LEGACY-UNRECONCILED | **2026-11-19:** selected §20.3.44 full local divisor-extraction proof (lines 841–909), and selected §20.3.48 application (lines 938–945); [Jacobian-step bound and multiplier-ideal ramification carry](reports/2026-11-19-divisorial-extraction-jacobian-and-ramified-multiplier-ideals.md), [exact coverage](coverage/2026-11-19-ch20-divisorial-extraction-ramification.md). +0 full sections and upstream-chain certificates; historical first-visit status remains unreconciled |
| §20.4 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §20.5 | THIS-RUN-FULL; LEGACY-UNRECONCILED | **2026-11-20 full direct mathematical lines 6–157**, blob `dae567406b2030e550664ca57b1fe77911d956d4`; proper pushforward/logarithm limit/intersection multiplication checked, prior 2026-11-16 partial retained; [coverage](coverage/2026-11-20-ch7-capacity-ch20-divisors.md); +0 complete upstream chains |
| §20.6 | HISTORIC-FULL-REPORTED; THIS-RUN-FULL-RECHECK | **2026-11-20 repeated full direct lines 7–76**, blob `d4817ac64b1365bd967d42cd474fec169f992e28`; verified cycle sheaves / Cartier obstruction, previously recorded non-Q-Cartier cone not new; [coverage](coverage/2026-11-20-ch7-capacity-ch20-divisors.md); +0 new whole statuses |
| §20.7 | HISTORIC-FULL-REPORTED; THIS-RUN-FULL-RECHECK | **2026-11-20 repeated full direct lines 7–30**, blob `d0c40d1e3f6f515eb13169ed1cd3fb447ca161c8`; divisor Chern-form sign and frame/cocycle convention checked; [coverage](coverage/2026-11-20-ch7-capacity-ch20-divisors.md); +0 new whole statuses |
| §20.8 | HISTORIC-PARTIAL-REPORTED | See existing dated reports and COVERAGE.md |
| §21.1 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §21.2 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §21.3 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §21.4 | THIS-RUN-FULL; LEGACY-UNRECONCILED | **2026-11-20** whole mathematical lines 7–123, blob `56a9a1c19e7234e2aa258d5ad1b66a5679ace190`; **POME-TORIC-SLOPE-ENERGY-BOUNDARY-THRESHOLD-001**, [proof](reports/2026-11-20-toric-slope-energy-boundary-threshold.md), [coverage](coverage/2026-11-20-toric-slope-energy-boundary-threshold.md); +1 whole direct section, no fully certified transitive chain or historical first-visit claim; deferred-by-user programme unchanged |
| §21.5 | HISTORIC-PARTIAL-REPORTED | See existing dated reports and COVERAGE.md |
| §21.6 | THIS-RUN-FULL | **2026-11-19:** entire mathematical lines 5–47 freshly checked (blob b3b4e34fff767a717df812a381f905589b257fb3); [full report](reports/2026-11-19-compact-index-convex-envelope-closure.md), [ledger](ledger/2026-11-19-compact-index-convex-envelope-closure.md). Previously partial, +0 first visits; §21.3.3/§21.5.2 and all upstream chains not fully certified |
| §21.7 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §21.8 | THIS-RUN-FULL; LEGACY-UNRECONCILED | **2026-11-19, POME-TORIC-VERTEX-JET-EDGE-THRESHOLD-001**: entire §21.8 lines 5–155; exact torus fixed-point jet threshold, [report](reports/2026-11-19-toric-fixed-point-jet-edge-threshold.md), [coverage](coverage/2026-11-19-toric-fixed-point-jet-edge-threshold.md); +0 certified upstream chains; historical first visit unresolved |
| §21.9 | CURRENT-PARTIAL; LEGACY-UNRECONCILED | **2026-11-19** selected Theorem 21.9.5 lines 138–167 checked as the lattice-section basis dependency for POME-TORIC-VERTEX-JET-EDGE-THRESHOLD-001; [report](reports/2026-11-19-toric-fixed-point-jet-edge-threshold.md); §21.9 not audited in full |
| §21.10 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §21.11 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §21.12 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §21.13 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §21.14 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §22.1 | CURRENT-PARTIAL; HISTORIC-PARTIAL-REPORTED | **2026-11-19 POME-NA-BACKGROUND-MASS-LIPSCHITZ-MINIMAX-001**: directly audited Def. 22.1.7 (118–123) and Proposition 22.1.39 proof (614–674), with order/supremum context; [uniform Kähler-background mass and arbitrary-family minimax](reports/2026-11-19-na-background-mass-uniform-lipschitz-minimax.md), [coverage](coverage/2026-11-19-na-background-mass-uniform-lipschitz-minimax.md). Existing older partial notes preserved; +0 whole sections and upstream chains; no new first-visit claim |
| §23.1 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §23.2 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §23.3 | THIS-RUN-FULL; LEGACY-UNRECONCILED | **2026-11-19 POME-HOPF-CONTRACTION-LYAPUNOV-S3S1-001**: direct reading all mathematical lines 5–53, Theorem 23.3.3 and proof; [Lyapunov smooth-topology report](reports/2026-11-19-hopf-quotient-lyapunov-smooth-topology.md), [exact coverage](coverage/2026-11-19-ch23-hopf-lyapunov-topology.md); +1 whole direct section, +0 upstream-chain certificates; previous §23.3 partial audits and first-visit uncertainty preserved |
| §24.1 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §24.2 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §24.3 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §24.4 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §24.5 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §24.6 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §24.7 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §24.8 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §24.9 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §24.10 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §24.11 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §24.12 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §24.13 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §25.1 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §25.2 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §25.3 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §25.4 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §25.5 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §25.6 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §25.7 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §25.8 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §25.9 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §25.10 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |
| §25.11 | LEGACY-UNRECONCILED | Prior reports not fully reconciled |

**Precise 2026-11-19 delta:** §17.18 +1 entire directly read section; +0 fully verified transitive chains; historical first-visit increment unasserted. Next sessions should reconcile legacy statuses one section at a time, without converting unknown into unreviewed or reopening deferred work.
