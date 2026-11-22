# POME-IDEAL-PROJECTION-PROPOSITION-KIND-REF-001

Date: 2026-11-22. Production main SHA: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

**Classification:** **low / confirmed error (reference-kind transcription)**; **NOT a false theorem**, not a newly established proof gap. Target result remains correct conditionally on its listed internal dependencies.

**Path/blob:** `docs/sections/multiplier-ideal-envelopes-and-goodness--ideal-projection/index.html`, `f1979b73c857f4874dd4a5cb10b93bcc047ebbdc`.

**From:** Corollary 18.4.5, source `non-kahler-pluripotential-theory:2439DE20`, permanent tag `B853F2E6C70B`, proof physical line **105** (context 99–106), calls its premise “corollary 18.4.4.”

**To:** **Proposition 18.4.4**, source `non-kahler-pluripotential-theory:F9497834`, permanent tag `2506B7AD6F19`, physical lines **69–91**, explicitly declared as an `env-proposition`. Line 95 already uses the correct kind.

**Complete justification:** Proposition 18.4.4 explicitly proves \(P_\theta[P_\theta[u]_{\mathcal I}]=P_\theta[u]_{\mathcal I}\); Corollary 18.4.5 uses this identity to invoke the existing mass bound of Proposition 16.28.7. The mathematical dependency is correctly linked but its printed *kind* is incorrect; no new proof of the mass theorem or false mathematical assertion is inferred.

**Proposed patch, not applied:** change only “corollary” to “proposition” in Corollary 18.4.5's proof; retain its linked tag, source labels and stable anchors. Affected dependent: that proof's cross-reference and generated citation/discovery metadata. No evidence of a different target is present.

**Review scope:** whole current §18.4 directly checked; whole introductory §21.1 and problem statements §§24.7/24.9 checked; selected §22.1 and repeat §§20.6/21.3/21.6/21.7. Zero complete upstream proof-chain certifications. Entire user-excluded regularization and related programmes remain **deferred-by-user**.

[Anchored proof and coverage](../reports/2026-11-22-ideal-projection-reference-kind-and-cross-chapter-rotation.md) · [Coverage record](../coverage/2026-11-22-ideal-projection-toric-problems-na.md).
