# Coverage delta — 2026-11-17 — arbitrary directed nets of positive-volume almost semigroups

**Finding:** `POME-OKO-DIRECTED-SG-POSVOL-NET-001` (low / verified conditional deduction; original sequence lemma correct).

**Pinned main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Integrated reader:** `docs/sections/almost-semigroups/index.html`, blob `33898b2963ad0f8b7e30bf414276642f60925b74`.

| Coverage level | Stable source / permanent tags | Current physical lines | Scope and result |
| --- | --- | --- | --- |
| Direct statement and proof | Lemma 19.7.29 `sgpt:688D7503` / `B63FC87B8DDF` | 477–525 | Checked sequence statement and cone intersection/volume proof; proved arbitrary directed net extension at positive infimum of volumes, with exact pseudometric convergence and a non-countably-cofinal polygon-to-disk example |
| Direct dependency check | Eq. 19.7.17 `sgpt:A996EEF7` / `642E2D6850DF`; Lemma 19.7.19 `sgpt:58F9B6C0` / `680A0890C1EE` | 213–230; 261–295 | Graded symmetric difference and intersection Lipschitz inequality; no interchange of grading and directed limits |
| Targeted dependency check | Theorem 19.7.20 `sgpt:282DA4DD` / `85641516C8CA`, Lemma 19.7.25 `sgpt:4791A323` / `E41D68AC6F7C`, Definition 19.7.26 `sgpt:56C14254` / `0270FA2C03BD`, Lemma 19.7.27 `sgpt:C3725EB6` / `B1ED8431B1B9` | 299–319; 372–389; 393–396; 425–439 | Cone/volume and lattice saturation interfaces only; KK12 general counting remains conditional |
| Statement/dependency context only | Theorem 19.7.32 `sgpt:ED83BFDD` / `1551B679B8B7` | 535–655 | Positive-volume closure; no entire proof or all external prerequisites independently certified |

**Inventory delta:** §19.7 was already partially proof-reviewed in previous runs, so **+0 first-visited numbered sections** and **+0 entire-section certifications**. Previously counted 25 chapters and 747 numbered sections retained; no global recount asserted. The new proof is not the earlier sharp Okounkov-body Hölder estimate, zero-volume countermodel, or convex-slice modulus result.

**Files:** [complete report](../reports/2026-11-17-directed-decreasing-almost-semigroup-nets.md), [classification ledger](../ledger/2026-11-17-directed-net-semigroup-monotone.md).

**Excluded scope:** Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss completion remain deferred-by-user. Mathematical lattice-cone saturation here is distinct. No code/build/tests, CI, main/source/body/registry/permanent tags, or website changes.
