# 2026-11-18 — Quantitative Hopf toric subgradient inversion

**Finding:** `POME-HOPF-TORIC-SUBGRAD-LOCALIZATION-001`; **low / verified conditional deduction**. Current printed Proposition 21.14.8 is correct; no claim of false theorem or completely repaired proof.

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Integrated source:** `docs/sections/hopf-fibrations-and-toric-potentials/index.html`, blob `0e83de13efbd70dfddc64a8eed40baed2d4359c5`. Eq. 21.14.7 source `non-kahler-pluripotential-theory:8E23893D` / permanent `5DB0E5246A09`, physical lines 158–163; Proposition 21.14.8 source `non-kahler-pluripotential-theory:7515BE71` / permanent `F23340CADBE0`, lines 165–201.

**Exact verified deduction:** For bounded toric \(v\in\mathrm{PSH}(\mathbb P^{n-1},k\sigma)\), every interior simplex slope \(p\) is a subgradient at some finite \(x\in H=\{\sum x_i=0\}\). Every such inverse satisfies
\[
 \operatorname{range}(x)\le\frac{k\log n+\operatorname{osc}v}{\min_i p_i}.
\]
The proof is a direct coercivity/subgradient argument applied to \(F=k\log\sum e^{x_i}+v\), with no strict positivity or differentiability. The globally continuous max-of-three-branches toric \(\mathbb P^1\) example has \(\operatorname{osc}v\le1\), unique inverse of \(p_\delta=(\delta,1-\delta)\), and inverse width \(1/(4\delta)\), proving the order cannot be improved in this class.

**Affected dependents:** quantitative toric Legendre inverse/moment-map uses in §§21.12–21.14. **Proposed optional addition:** precise bounded-potential subgradient version after Prop. 21.14.8, not a direct body change. **Limitations:** no smooth-strict optimal coefficient asserted; convex/toric positivity and established notation are conditional upstream inputs; no full-section audit.

[Full English source-anchored proof](../reports/2026-11-18-hopf-toric-subgradient-localization-sharp.md) · [coverage delta](../coverage/2026-11-18-ch21-hopf-toric-subgradient-localization.md). **Coverage:** §§21.14.7–8 new quantitative selected proof, §§21.4.2/6 semantic crosscheck, +0 first numbered sections/+0 full certifications, 25/747. Excluded Demailly/regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss work remains **deferred-by-user**. Review Markdown only; no production source, tags, main, build, CI or website modification.
