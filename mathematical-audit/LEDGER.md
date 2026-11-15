- **2026-11-15 / POME-BDIV-INFINITELYNEAR-VOLUME-CHAMBERS-001:** low / verified conditional deduction. New *infinitely near* toric two-blowup rational b-divisor volume chambers; volume (1-a^2-b^2) for (b\le a), (1-(a+b)^2/2) for (b>a), exact (41/50) versus root (1) and (D^2=4/5) in a fixed example. Independent section-volume proof; analytic identification conditional on printed 21.13.45. [Report](reports/2026-11-15-infinitely-near-bdivisor-volume-chambers.md) · [ledger](ledger/2026-11-15-infinitely-near-bdivisor-volume.md) · [coverage](coverage/2026-11-15-ch20-infinitely-near-volume.md). Excluded work deferred-by-user.
- **2026-11-15 / POME-NA-MULTITORUS-GRADED-IDEAL-GAUSS-FLATNESS-001:** **low / verified conditional deduction** (printed §22.1.94 correct); full multitorus homogeneous ideal splitting, finite generators, saturation/torus fiber, exact flatness and concave Gauss value. Separate from 2026-11-02 single-circle audit; source `sgpt:AB6FE74C` / `76252E7717AC`, main `b6933b772f41b45918f7e25ed1afbbb1fd892272`, lines 1402–1415. [Report](reports/2026-11-15-multitorus-homogeneous-ideals-gauss-flatness.md), [ledger](ledger/2026-11-15-multitorus-graded-ideals.md), [coverage](coverage/2026-11-15-ch22-multitorus-graded-ideal.md). GAGA still external; §22.1.97–.98 not certified; excluded work deferred-by-user.
# Project-wide audit ledger — pointer and status safeguards

The dated [ledger directory](ledger/) and [section coverage matrix](SECTION_MATRIX.md) remain the durable granular sources. This index is **not an exhaustive consolidation of all previous findings**; retain every pre-existing stable ID and status in its own dated ledger and report.

## Verified deductions (not errors or source repairs)

- **POME-MAGNETIC-MULTIPAIR-MIDPOINT-DEFECT-001** (2026-11-15, low / verified conditional deduction): n-pair zero-field Riesz mean majorization and an all-rank quadratic field deficit bound; exact 2-pair oscillatory formula gives sharp b² exponent. Printed Lemma 2.24.6 and Proposition 2.24.8 correct. Separate from previously logged one-pair midpoint and Dirichlet-rate results. [Proof](reports/2026-11-15-magnetic-multipair-zero-field-midpoint-defect.md) · [ledger](ledger/2026-11-15-magnetic-multipair-midpoint-defect.md) · [coverage](coverage/2026-11-15-ch2-magnetic-multipair-defect.md).



- **`POME-STEIN-LEVI-QUANT-CODIM-SHARP-001`** (2026-11-15, low / verified conditional deduction): pointwise quantitative Levi summation with jointly sharp complex codimension and coercivity coefficient; first direct §9.32.2/.4 proof read, original statements correct; no global intersection-index optimality asserted. [Proof](reports/2026-11-15-stein-levi-quantitative-sharp-codimension.md) · [ledger](ledger/2026-11-15-stein-levi-quantitative-sharp-codimension.md) · [coverage](coverage/2026-11-15-ch9-stein-levi-quantitative.md).

- **`POME-CONVEX-DUAL-LINF-OSC-ROOFTOP-001`** (2026-11-15, low / verified conditional deduction): exact global norm/oscillation duality and optimal 1-Lipschitz finite dual-rooftop stability; printed statements correct. Older Wasserstein example is not recounted. [Proof](reports/2026-11-15-legendre-exact-supnorm-oscillation-rooftop.md) · [ledger](ledger/2026-11-15-legendre-supnorm-oscillation-rooftop.md) · [coverage](coverage/2026-11-15-ch21-legendre-rooftop-isometry.md).



- **`POME-CLASS-TWO-BALL-CAPACITY-INTERACTION-001`** (2026-11-15, low / verified conditional deduction): exact two-sided Newtonian capacity bounds for two separated equal balls and the sharp leading negative interaction term, as a selected conditional check of Theorems 4.3.7/4.3.10 (printed results correct). [Proof](reports/2026-11-15-two-separated-newtonian-balls-capacity-interaction.md) · [ledger](ledger/2026-11-15-separated-balls-capacity-interaction.md) · [coverage](coverage/2026-11-15-ch4-separated-balls-capacity-interaction.md).


- **`POME-OKO-CURVE-UNIFORM-PIC0-SHARP-RATE-001`** (2026-11-15, low / verified conditional deduction): exact sharp curve bound sup_{T in Pic^0} d_H(Delta_{k,T}(L),[0,d])=g/k for kd>=2g, with a fixed elliptic twist showing 1/k sharp; original Proposition 19.4.12 correct. [Proof](reports/2026-11-15-curve-uniform-pic0-okounkov-rate.md) · [ledger](ledger/2026-11-15-curve-uniform-pic0-okounkov-rate.md) · [coverage](coverage/2026-11-15-ch19-curve-uniform-pic0-okounkov-rate.md).

- **`POME-TORIC-BIG-LATTICEFREE-STABLE-BASE-EFFECTIVE-001`** (2026-11-15, low / verified conditional deduction): exact all-vertex-denominator bound $\operatorname{Bs}|qD|=\mathbf B(D)$ for integral big divisors on smooth projective toric varieties, with an explicit lattice-free degree-one/two big divisor on a smooth projective toric surface; original §§21.13.8 and 21.13.10 correct. [Full proof](reports/2026-11-15-toric-big-lattice-free-effective-stable-base.md) · [classified ledger](ledger/2026-11-15-toric-big-lattice-free-stable-base.md) · [coverage](coverage/2026-11-15-ch21-toric-big-stable-base-effective.md).

- **\`POME-BT-ENERGY-CAPACITY-OPTIMAL-EXPONENT-001\`** (2026-11-15, low / verified conditional deduction): optimized universal Bedford–Taylor \(p\)-energy-to-capacity modulus with precise coefficient; explicit bounded \(n=1\) \(\mathcal E_0\) family proves exponent \(p/(p+1)\) optimal but does not prove optimality in higher dimensions or of the coefficient. [Proof](reports/2026-11-15-optimized-bt-energy-capacity-exponent.md) · [classified ledger](ledger/2026-11-15-bt-energy-capacity-optimal-exponent.md) · [coverage](coverage/2026-11-15-ch7-bt-energy-capacity-sharpness.md). Printed §7.11.19 correct; upstream BT input conditional.

- **`POME-GAUD-MATRIX-EFFECTIVE-COERCIVITY-POWER-001`** (2026-11-15, low): explicit pointwise coercivity threshold and optimal growth exponent, in [report](reports/2026-11-15-gauduchon-matrix-effective-coercivity-sharp-power.md), [ledger](ledger/2026-11-15-gauduchon-effective-coercivity.md) and [coverage](coverage/2026-11-15-ch14-gauduchon-effective-coercivity.md). Original Lemma 14.13.5 correct.

- **`POME-ADJOINT-ENTROPY-EXPLICIT-LOGMODULUS-001`** (2026-11-15, low): explicit uniform-in-model-reference logarithmic `L1` stability bound derived from §11.38.5 entropy and §11.36.1 supporting probabilities. Sharp entropy-sublevel **mechanism**, not PDE sharpness; earlier 2026-10-24 implicit modulus retained and distinguished. [Full proof](reports/2026-11-15-adjoint-entropy-explicit-log-modulus.md) · [ledger](ledger/2026-11-15-adjoint-entropy-explicit-log-modulus.md) · [coverage](coverage/2026-11-15-ch11-adjoint-entropy-modulus.md). PDE upstream conditional; original theorem correct.

## Unresolved known examples, not claimed repaired

- `POME-CAP-001`: original global/open-set capacity assertion; prior confirmed error and proposed local correction remain separately recorded.
- `POME-PROJ-COMP-BASE-ESCAPING-COMPACT-FIBERS-001`: earlier confirmed noncompact-base counterexample; compact-base correction proposed, not applied to main.
- Any other unresolved dated findings remain in their original reports; this brief index must not be treated as a closed-list certification.

## Deferred by user (not certified)

Demailly approximation/regularization and dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion work have been expressly excluded since 2026-10-17. Retain their earlier notes as **deferred-by-user**; do not infer their results from unrelated audits.

