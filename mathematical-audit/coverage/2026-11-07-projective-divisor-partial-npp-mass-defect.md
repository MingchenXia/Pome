# Additive precise section coverage — 2026-11-07 — partial non-pluripolar mass loss

**Production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **ToC baseline:** 25 chapters, 747 numbered sections, zero whole mathematical sections certified. §13.7 was previously partially audited; this work adds a distinct exact model, **not first coverage**.

| Section | Integrated main blob | Actually inspected anchors / mathematical scope |
| --- | --- | --- |
| §13.7 | docs/sections/non-pluripolar-products--capacity-convergence-and-loss-of-mass/index.html · d66813856cb813722806ab912afdfd4815d2da97 | 41–67 extended capacity/monotone convergence; 106–134 Theorem 13.7.5 lower inequality and mass guard (source foundations-of-pluripotential-theory:AB4EBE3B / tag 67C4F7EC316E); 138–140 original Example 13.7.6 (D5678E03 / ACAEA8D8BE87). New POME-NPP-PROJECTIVE-DIVISOR-PARTIAL-DEFECT-001 **low / verified conditional deduction**, not a false theorem. |
| §13.5 | docs/sections/non-pluripolar-products--global-finiteness-and-bounded-cohomological-mass/index.html · 943517743538820940559eae8469ce98ecf5fcd5 | 10–32 bounded BT mass identity §13.5.1, source 4EE18BE1 / tag 06A36B9354A5; 123–124 Example 13.5.6. Conditional dependency; not general proof certification. |
| §13.2 | docs/sections/non-pluripolar-products--truncation-and-plurifine-locality/index.html · 81be8c5acc360c96bd3c5acba05a3cdb5fafaf4c | 57–64 pole-discarding Definition 13.2.4, source 9D8E4DD8 / tag D79952D7E272; dependency, not full proof certification. |
| §10.6 | docs/sections/global-potentials-and-positive-cohomology-classes--curvature-and-metrics-defined-by-sections/index.html · ff56aa13950da3423135bb0bbaf40bcc980c21a1 | 108–113 FS curvature/normalization Example 10.6.7, source E51945FB / permanent 4CE1D9D7D803; crosscheck only. |

**Verified explicit addition:** all fractional deficits $1-(1-\alpha)^n$ occur for decreasing bounded $\omega_{\rm FS}$-psh truncations, and the weak residual on the pole hyperplane is exactly $[1-(1-\alpha)^n][H]\wedge\omega^{n-1}$, not a permitted singular NPP product. [Proof](../reports/2026-11-07-projective-divisor-partial-npp-mass-defect.md) · [ledger](../ledger/2026-11-07-projective-divisor-partial-npp-mass-defect.md).

**Unverified remainder:** general §§13.2/13.5/13.7 proof chains, weighted continuity in §13.7.9, and other dependent sections. All previous ledger classifications unchanged. All owner-excluded Demailly regularization, Bergman, weighted L², OT, multiscale and positivity-loss work remains **deferred-by-user**, not completed. No production edits, project tests/build, CI, formalization or publication.
