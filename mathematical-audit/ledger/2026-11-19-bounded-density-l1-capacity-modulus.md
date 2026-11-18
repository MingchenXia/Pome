# POME-BT-DIRICHLET-L1-CAPACITY-MODULUS-001 — 2026-11-19

**Status/severity:** low / verified conditional deduction. Neither printed §7.10.1 nor §7.10.2 is refuted. Full upstream certification remains open.

**Source:** main b6933b772f41b45918f7e25ed1afbbb1fd892272; integrated docs/sections/bedford-taylor-products-and-local-capacity--bounded-measurable-densities/index.html, blob 762b841b0cb243784dc988f04dbf2779da66c469. Lemma source foundations-of-pluripotential-theory:74804636, permanent C09E42A43E93, lines 10–35; Theorem source foundations-of-pluripotential-theory:9C25B561, permanent C9116FCEFCD2, lines 37–108; outer-capacity dependency §7.5.4 source foundations-of-pluripotential-theory:34043611, permanent 56B45ADBA326.

**Result:** If bounded psh u,v have the same continuous boundary trace and both top Monge–Ampère measures are ≤M η^n, then for every ε>0:
\[
\operatorname{Cap}_B^*(\{|u-v|>\varepsilon\})\le
\frac{(n+1)^{n+1}}{n^n}M\varepsilon^{-n-1}\int_B|u-v|\eta^n.
\]
The exponent n+1 is forced by scalar rescaling; no optimal-prefactor claim. Proof optimizes Lemma 7.10.1 in s,t and extends the thresholds in the checked proof of Lemma 7.5.4. Requires both measure bounds and matching boundary data. No arbitrary-net or excluded regularization inputs.

**Action/dependents:** propose a standalone corollary beside §7.10.1–2, potentially useful for bounded-density Dirichlet, comparison/capacity and convergence; do not change the mathematical body or canonicalization directly. Uncertified §7.3.11/7.5.2/7.5.8/7.9.2/5.10.4 remain conditional. Excluded programmes **deferred-by-user**.

[Full anchored argument](../reports/2026-11-19-bounded-density-l1-capacity-modulus.md) · [coverage increment](../coverage/2026-11-19-bounded-density-l1-capacity-modulus.md).
