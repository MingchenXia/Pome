# Finding `POME-LEGENDRE-TWO-BRANCH-MIXED-MASS-001`

- **2026-11-19, §17.18, severity:** low.
- **Classification:** **verified conditional deduction**. Printed Lemma 17.18.1 is not refuted; no confirmed source error.
- **Main SHA / file blob:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` / `5d989cf765f5471ce1e2278ef39e2c69979eeb92`.
- **Location:** `docs/sections/partial-legendre-transforms-and-monge-ampere-mass/index.html`, lines 7–63, lemma source `transcendental-positive-cones:676C0E65`, permanent tag `C12669D1EC3D` (statement lines 14–22), proof 27–62; section tag `12D395D414C1`.
- **Exact result:** for locally bounded psh `\varphi,\psi` and real `a<b`, `V=\max(\varphi+a\log|\tau|^2,\psi+b\log|\tau|^2)` satisfies
\[
(\pi_U)_*(dd^cV)^{n+1}=(b-a)\sum_{k=0}^n(dd^c\varphi)^k\wedge(dd^c\psi)^{n-k}.
\]
The formula holds as a locally finite Radon measure, without `\varphi\le\psi`, and the coefficient follows from exact Legendre endpoints and a beta integral.
- **Dependencies still open:** the general printed Kiselman input (tag `2C1A82803889`), bounded Bedford–Taylor monotone mixed-product continuity and local mass bounds, general dyadic fiber-tail passage, and arbitrary-singularity NPP extension. These are conditional dependencies, **not** new proof gaps in the printed theorem.
- **Proposed correction:** none required; optional separate corollary/test identity, without altering existing source variants, tags or historic attribution.
- **Potential dependents:** test curves and Legendre Monge–Ampère identities in Chapter 17; no dependent incorrectly stated on evidence reviewed.
- **Coverage:** one complete direct-section reading; zero complete transitive-chain certifications; first historical visit unresolved. User-excluded programme remains deferred-by-user.
- [Full report](../reports/2026-11-19-legendre-two-branch-mixed-mass.md) · [Coverage delta](../coverage/2026-11-19-ch17-legendre-two-branch-mixed-mass.md).
