> **2026-11-13 — new selected §16.29 cutoff / Legendre normalization proof:** [POME-ENVSYS-CUTOFF-LEGENDRE-RECOVERY-001](reports/2026-11-13-envelope-curve-cutoff-legendre-recovery.md), **low / verified conditional deduction**. Directly from normalized decreasing slices: \(\varnothing\ne\bigcap_{\tau<c}\{\Gamma_\tau=0\}=\{\Gamma_c=0\}\); for the regularized Legendre ray, \(\sup_XU_t=ct\) and \(U_t-ct\downarrow\Gamma_c\) pointwise. The usc passage uses a countable polar exceptional union, not a false exchange of limits. [Ledger](ledger/2026-11-13-envelope-curve-cutoff-legendre-recovery.md) · [precise coverage](coverage/2026-11-13-ch16-envelope-cutoff-legendre-recovery.md). Main \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`; §16.29 blob \`856e240bbc5c86058ff861873f11e87db021e1bd\`, stable tags and physical lines pinned. Already partly reviewed §16.29: **0 new first-visited numbered sections / 0 full certifications / ToC 25 chapters, 747 sections**. User-excluded regularization and dedicated Bergman/\(L^2\)/OT/multiscale/positivity-loss remains **deferred-by-user**. Audit Markdown only.

---

> **2026-11-13 new selected §11.14 variable-polarization chamber:** [`POME-HIRZ-POLARIZATION-UNIVERSAL-STABILITY-WALL-001`](reports/2026-11-13-hirzebruch-polarization-universal-stability-wall.md), **low / verified conditional deduction** (original fixed-\(P\) theorem correct). Exact worst-case nonsplit extension margin \(\min(3(u-v),3v-2u)\) and sharp universal stable region \(2u/3<v<u\) on \(\mathbb F_0\), including lower-wall fiber-section obstruction. [Ledger](ledger/2026-11-13-hirzebruch-polarization-stability-wall.md) · [precise lines, tags and selected §11.13/§11.15 context](coverage/2026-11-13-ch11-hirzebruch-polarization-wall.md). Prior fixed-polarization slope-jump finding not recounted. Main `b6933b772f41b45918f7e25ed1afbbb1fd892272`; previously partly visited numbered sections, **+0 first visits / +0 entire certifications**, unchanged 25/747 ToC. Dedicated Demailly programme **deferred-by-user**; audit Markdown only.

---

> **2026-11-12 — §9.62 sharp \(L^p\) extension over all zero-coordinate strata:** **POME-REINHARDT-LP-AXIS-REMOVABILITY-001 (low / verified conditional deduction; printed Lemma 9.62.3 and Theorem 9.62.6 remain correct).** For any nonempty open convex downward-closed logarithmic domain \(D\), a holomorphic function on \(\Omega_D^*=\widetilde\Omega_D\cap(\mathbb C^*)^n\) locally in \(L^p(\widetilde\Omega_D)\) extends uniquely to \(\widetilde\Omega_D\) if \(p\ge2\). A direct negative-Laurent-coefficient/Fubini proof handles joint holomorphy at every axis intersection; \(1/z_1\) shows **sharp failure for all \(0<p<2\)** on *each* such \(D\), and \(z^\alpha\) has the exact axis integrability thresholds \(p(-\alpha_j)<2\). This is not an unqualified Hartogs extension, not a printed source error, and not the excluded regularization/\(L^2\)-operator programme. [Full proof](reports/2026-11-12-reinhardt-lp-coordinate-axis-removability.md) · [ledger](ledger/2026-11-12-reinhardt-lp-coordinate-axis-removability.md) · [precise coverage](coverage/2026-11-12-ch9-reinhardt-lp-coordinate-axis-removability.md). Main \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`; integrated §9.62 blob \`51d14c9874a7f3ec3a4886644749db8ddb82d923\`; permanent tags and physical lines in report. **0 new first-visited sections / 0 full section certificates / current ToC 25 chapters and 747 sections.** Excluded Demailly programme stays **deferred-by-user**; audit Markdown only.

---

> **2026-11-12 additive exact coverage, §19.7 zero-volume Okounkov boundary:** [POME-OKO-ZEROVOLUME-NONEXTENSION-001](reports/2026-11-12-okounkov-zero-volume-nonextension.md) (low / verified conditional deduction, no printed theorem error) directly calculates saturated full-group semigroups approaching the same zero-volume element in d_sg while their Okounkov bodies separate in Hausdorff distance. [Exact selected IDs, source tags, physical lines](coverage/2026-11-12-ch19-okounkov-zero-volume-boundary.md); [classified ledger](ledger/2026-11-12-okounkov-zero-volume-nonextension.md). Main b6933b772f41b45918f7e25ed1afbbb1fd892272; §19.7 previously partly sampled, **+0 first section visits, +0 full certifications, 25/747 actual ToC**. Excluded regularization programme remains deferred-by-user.

---

> **2026-11-12 additive coverage (selected §18.27):** POME-IDEAL-SMALLCURV-DIFFUSE-GREEN-THRESHOLD-001 tests unbounded zero-Lelong Green residuals and proves the sharp finite-divisor threshold a>Σ_iλ_i on P¹. [Report](reports/2026-11-12-small-curvature-diffuse-green-multipole-threshold.md) · [ledger](ledger/2026-11-12-small-curvature-diffuse-green-multipole-threshold.md) · [exact scope](coverage/2026-11-12-ch18-small-curvature-diffuse-green-threshold.md). Main b6933b772f41b45918f7e25ed1afbbb1fd892272; §18.27 previously partially covered: +0 first visits, +0 full certifications; 25 chapters/747 sections. Excluded regularization remains **deferred-by-user**.

---

> Integration status — 18 October 2026: the audit branch has been incorporated into `main`. Confirmed capacity and placement defects are repaired; see [the integration report](reports/2026-10-18-integrated-corrections.md). Demailly approximation and its dedicated prerequisite audit remain deferred by the author. Older priorities, branch-only restrictions, and scheduling descriptions below are historical, not current instructions. This integration does not certify the unreviewed chapters or every external dependency.

# Broad-scope coverage ledger — 17 October 2026

## Governing scope

The author's 17 October request supersedes the Demailly priority in older README/checkpoint text. Skip Demailly approximation and its dedicated Bergman/L2/extension/atlas proof-completion programme. Retain historical work as deferred-by-user, not resolved. Audit the rest of Pome across chapters; do not remain indefinitely in one prerequisite chain. If an unrelated proof invokes regularization, log that dependency without reopening it.

The table records the NEW broad-scope pass, not a denial of historical targeted checks. Chapter names were read from the actual navigation at main `66f8176be2a006b9404ae6db49ee15621dea5523`. Queued means not yet substantively reviewed in this new pass. Reading a section is not certification of its dependencies or chapter. No entire chapter is certified.

| Chapter | Subject | New-pass coverage |
| --- | --- | --- |
| 1 | Conventions | Queued; track normalization and terminology across sources. |
| 2 | Measures, distributions, and convergence | Queued; limits, nets, tightness and testing classes. |
| 3 | Harmonic and subharmonic functions | Queued outside the deferred regularization programme. |
| 4 | Energy, capacity, and fine topology | Queued; distinguish local/global capacities. |
| 5 | Plurisubharmonic functions and positive currents | Queued outside Demailly/Bergman approximation. |
| 6 | Lelong numbers, multiplier ideals, and regularization | Dedicated approximation and prerequisite-completion work deferred; other independent material remains eligible. |
| 7 | Local Monge–Ampere theory and capacity | Queued; Bedford–Taylor products and comparison/convergence. |
| 8 | Complex Hessian equations | Queued. |
| 9 | Complex spaces and modifications | Queued. |
| 10 | Cohomology, positivity, and geometric loci | Queued. |
| 11 | Hermitian geometry, torsion, and Gauduchon duality | Queued. |
| 12 | Gauduchon variational volume | Queued. |
| 13 | Non-pluripolar measures and mass | Section 13.12 mathematical body read; POME-CAP-001 confirmed below. Remaining sections queued. |
| 14 | Monge–Ampere equations and stability | Queued. |
| 15 | Monge–Ampere equations with prescribed singularities | Queued. |
| 16 | Singularity types, envelopes, and models | Next unreviewed chapter: envelope order/limits and actual proof dependencies. |
| 17 | Energy, geodesics, rays, and test curves | Queued; endpoint assumptions and limiting operations. |
| 18 | Multiplier-ideal models and partial equilibrium | Queued outside the excluded approximation programme. |
| 19 | Sections, graded series, and Okounkov bodies | Queued. |
| 20 | B-divisors and restriction | Queued. |
| 21 | Toric and convex geometry | Queued. |
| 22 | Non-Archimedean pluripotential theory | Queued. |
| 23 | Hopf and locally conformally Kahler geometry | Queued. |
| 24 | Problems in pluripotential theory | Queued; do not confuse stated questions with proved results. |
| 25 | Historical and bibliographical notes | Queued; retain attribution, separate it from proof inputs. |

## First review unit: Section 13.12

Report: [Open-set capacity counterexample](reports/2026-10-17-open-set-capacity-counterexample.md).

- `D56D6D4A5E94`, Proposition 13.12.7: **POME-CAP-001, confirmed error**. With the printed whole-open-set capacity definition, decreasing bounded smooth local psh sequences need not converge in capacity. The report gives an explicit projective-line counterexample with every exceptional set of capacity exactly one.
- `F7490AE48EAC` and `C96BE5099B6A`: capacity-convergence and global-capacity definitions read to establish the exact scope of the counterexample.
- `272876B00528`, Theorem 13.12.8: statement read in both standalone and enclosing pages. Proof is deferred to GZ17 in the enclosing page. Internal replacement not yet located; no assertion that this theorem is false.
- Other statements of Section 13.12: body read, but replacement-proof dependencies not transitively certified.

## Carry-forward actions

Keep POME-CAP-001 open until a reviewed correction is integrated. Distinguish local convergence on compact subsets from genuine global capacity control; adding uniform boundedness does not fix this counterexample. Locate actual downstream uses without silently weakening their hypotheses. The net version of a proposed local replacement still requires proof.

Continue next with Chapter 16, then Chapter 7 and Chapter 17, while expanding the matrix to exact section/tag coverage. Other chapters remain part of the mandate. Historical findings and unsynced material remain in their existing reports; defer only the excluded programme, not the general audit. No automatic main edits, merging, website publication, or CI is authorized.
