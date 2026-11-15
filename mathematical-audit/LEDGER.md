# Project-wide audit ledger — pointer and status safeguards

The dated [ledger directory](ledger/) and [section coverage matrix](SECTION_MATRIX.md) remain the durable granular sources. This index is **not an exhaustive consolidation of all previous findings**; retain every pre-existing stable ID and status in its own dated ledger and report.

## Verified deductions (not errors or source repairs)

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

