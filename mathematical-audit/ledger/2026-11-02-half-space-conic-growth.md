# Classified ledger increment — 2026-11-02 — half-space conical growth

## POME-HARM-HALFSPACE-CONE-GROWTH-SHARP-001

**Classification:** low severity; **verified conditional deduction**. No false theorem or missing proof identified. No source correction applied.

**Main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

**Source:** docs/sections/kelvin-transforms-and-half-space-potentials/index.html, blob f2615a5393af724c3996978212162f94911ff9d9; §3.2.6 Theorem (original Gerby tag 1C8A330A; permanent 6BC86EEF03A9) and equations 3.2.7–8 (original C0A46F1A, 358F89A3; permanent F3ED29BBAD39, 8F7C774A9D89), lines 65–75; converse lines 111–131. Contrast §3.2.12 (original BB6DAC3F; permanent 9ADD2DF19642), lines 141–145.

**Precisely reviewed assumptions:** dimension d≥2, nonnegative harmonic h, coefficient c≥0 and positive Radon boundary measure with finite weighted integral of (1+|z|²)^(-d/2); no finite-total-mass assumption.

**Verified result and sharpness:** c is the intrinsic decreasing vertical-slope limit h(x',t)/t, independently of fixed x'; convergence to c is uniform on any fixed cone |x'|≤At at large height. Conversely, every escape path with unbounded |x'|/t admits an admissible positive *atomic* boundary measure for which the ratio fails to converge to c along a subsequence. Explicit data and the full dominated-convergence proof are in [the main-pinned report](../reports/2026-11-02-half-space-growth-cones-and-escaping-boundary-mass.md). For finite boundary mass or bounded Lebesgue data, stronger global-in-x' bounds hold, so no printed theorem is contradicted.

**Proposed addition (not applied):** a short corollary after Theorem 3.2.6 with intrinsic coefficient identification, conical uniform convergence, and the sharp counterexample to unrestricted horizontal uniformity. Preserve the classical source attribution and permanent tags.

**Dependent uses:** potential later identification of the half-space linear harmonic summand or growth-at-infinity assumptions; none demonstrated erroneous.

**Actual coverage:** new selected proof calculations on *previously partly reviewed* §3.2 only. Zero newly first-reviewed sections, zero wholly mathematically certified sections. Preserve all old findings and the Demailly approximation/regularization, Bergman, weighted-L², Ohsawa–Takegoshi, multiscale and positivity-loss records as **deferred-by-user**. No build, tests, CI, main edit, formal verification, or website publication.
