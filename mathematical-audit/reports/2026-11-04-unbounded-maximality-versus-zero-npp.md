# Unbounded maximality is strictly stronger than vanishing top non-pluripolar mass

**Audit date:** 2026-11-04. **Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (unchanged). **Finding:** `POME-MAX-NPP-ZERO-NONCONVERSE-001`, **low / verified conditional deduction**, not a false printed theorem or a repair.

## Integrated statements and provenance

1. `docs/sections/relative-energy-and-perron-segments--energy-along-weak-geodesics/index.html`, blob `8d9b7af925289346c96df751c67049e90c9dfe1d`, physical lines **7, 11–37**. Lemma **17.8.1**, source `foundations-of-pluripotential-theory:9DEC569D`, permanent tag `950F051CF55A`: maximal PSH, without boundedness, implies that the top non-pluripolar product is locally finite and zero. The integrated proof uses balayage and weighted Bedford–Taylor capacity continuity; those general prerequisites are *not* certified in this increment.
2. `docs/sections/bedford-taylor-products-and-local-capacity--the-homogeneous-dirichlet-problem-and-balayage/index.html`, blob `928f3d3e36f2d03a42623b91487ecec7d189e6c7`, physical lines **160–174**. Definition **7.7.6**, source `foundations-of-pluripotential-theory:4A1DBBE1`, tag `FD8547B922C9`, defines maximality by compactly supported comparison. Theorem **7.7.7**, source `foundations-of-pluripotential-theory:5C75D8E4`, tag `BCFDDA1FCB7A`, explicitly requires **local boundedness** for the equivalence with vanishing *Bedford–Taylor* top mass.
3. `docs/sections/non-pluripolar-products--truncation-and-plurifine-locality/index.html`, blob `81be8c5acc360c96bd3c5acba05a3cdb5fafaf4c`, physical lines **7–13, 35–63**. Definition **13.2.4**, source `foundations-of-pluripotential-theory:9D8E4DD8`, tag `D79952D7E272`, takes the increasing limit of truncated Bedford–Taylor products restricted to the **strict** sets where all original potentials exceed the truncation level. This discards pluripolar contributions.

## Explicit countermodel in every complex dimension

Fix `n >= 1`, let `B={z in C^n: |z|<1}`, and put
```text
h(z) = log |z|^2 for z != 0,   h(0) = -infinity.
```
This is a plurisubharmonic function on `B`, unbounded only at the origin. On `B\{0}`, the Hermitian matrix of its complex Hessian is
```text
h_(j bar k) = delta_jk / |z|^2 - (bar z_j z_k) / |z|^4.
```
It has eigenvalue `0` along the radial complex direction and eigenvalue `|z|^{-2}` with multiplicity `n-1`. Thus
```text
(dd^c h)^n = 0 on B\{0}
```
as an ordinary smooth top-degree form, using the collection convention `dd^c=(i/2pi)partial barpartial`. For `n=1`, the same assertion is simply harmonicity away from the pole.

For each positive integer `k`, set `h_k=max(h,-k)` and `O_k={h>-k}={|z|>exp(-k/2)}`. On `O_k`, the function `h_k` agrees locally with the smooth `h`. Bedford–Taylor locality therefore gives **exactly**
```text
1_(O_k) (dd^c h_k)^n = 1_(O_k) (dd^c h)^n = 0.
```
Every non-pluripolar truncation current is zero, not merely small. By Definition 13.2.4, the non-pluripolar product is locally finite and
```text
< (dd^c h)^n > = 0 on B.
```
There is no interchange of limits, hidden sequential compactness, or regularization argument here: the defining truncated currents are individually zero. In dimension one the contrast is especially transparent: Poincaré–Lelong gives `dd^c log|z|^2 = delta_0` as an ordinary current, while its *non-pluripolar first-degree product* is zero.

Nevertheless `h` is **not** maximal in the sense of Definition 7.7.6. Given any fixed `0<R<1`, set
```text
v_R(z) = max{ log|z|^2, log R^2 }.
```
The maximum of two PSH functions is PSH, `v_R=h` whenever `|z|>=R`, but `v_R(0)=log R^2 > -infinity=h(0)`, and in fact `v_R>h` throughout `|z|<R`. The set where `v_R` may exceed `h` has closure contained in the compact ball `{|z|<=R}Subset B`. Hence `v_R<=h` outside a compact subset yet `v_R\nleq h` on `B`, violating maximality.

**Conclusion:** even in every complex dimension and even for a standard isolated logarithmic pole, `< (dd^c h)^n >=0` does **not** imply maximality. The local boundedness condition in the separate Bedford–Taylor equivalence, Theorem 7.7.7, cannot be omitted merely by replacing its ordinary top mass with the non-pluripolar top mass.

## Status, correction policy, downstream and limitations

- **Status:** low / verified conditional deduction; all displayed model calculations and the explicit competitor are complete. The printed forward-only Lemma 17.8.1, bounded equivalence Theorem 7.7.7, and Definition 13.2.4 remain correct. In particular **no false theorem** and **no proof gap** is asserted in any of these printed statements.
- **Proposed nonproduction clarification:** if the reading edition discusses a reverse implication near Lemma 17.8.1 or in applications to homogeneous Monge–Ampère equations, explicitly distinguish zero *non-pluripolar* mass from maximality and give this radial countermodel. No body change made.
- **Affected dependents to watch:** arguments using Lemma 17.8.1 in the weak-geodesic energy proof, §17.8.3, may use its forward direction; reversing it without extra hypotheses would be invalid. The audit did **not** find such a reverse use in the selected lines 59–111, and it does not certify that entire energy proof or other distant dependents.
- **Coverage actually performed:** independently read and checked the model against §17.8.1, §7.7.6–7 and §13.2.4, including the local truncation definition and the local-boundedness qualifier. All three sections have earlier partial coverage and none is fully certified. The actual current ToC remains **25 chapters / 747 numbered sections / zero complete mathematical-section certifications**.
- **Scope:** no Demailly approximation/regularization, Bergman, weighted-L², Ohsawa–Takegoshi, multiscale-atlas or positivity-loss proof programme. These existing notes stay **deferred-by-user**, not resolved. No build, test, formal verification, CI, publication, source, registry, tag or production-main changes.
