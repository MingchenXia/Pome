# Findings — 2026-11-23 Okounkov divisor arithmetic and toric Newton operations

Reviewed main **b6933b772f41b45918f7e25ed1afbbb1fd892272**. See [the full report](../reports/2026-11-23-toric-newton-max-roof-and-okounkov-denominator-check.md).

## POME-OKOUNKOV-ANALYTIC-RESIDUE-DIVISIBILITY-001
- **Status:** proof gap. **Severity:** low. Not a false theorem.
- **Text:** docs/sections/the-theory-of-okounkov-bodies--algebraic-partial-okounkov-bodies/index.html, Lemma 19.4.43, source sgpt-10EC43BE, tag FD338F03BE48, physical lines 632–678, especially 646 and 659.
- **Missing step:** ND integral and Nε integral do not imply N(1−ε)D integral, yet Proposition 19.4.12 is invoked for the corresponding line bundle.
- **Countermodel to the arithmetic implication:** D=E/2, ε=1/2, N=2.
- **Proposed repair:** choose N clearing both D and (1−ε)D, in addition to any retained requirement on ε. All cited twisted line bundles then exist.
- **Dependents:** Lemma 19.4.43 → Theorem 19.4.41. Local integrality correction only; other analytic inputs unverified.

## POME-TORIC-NEWTON-MAX-ROOF-CONVEX-LATTICE-001
- **Status:** verified conditional deduction. **Severity:** low. Not an original theorem error.
- **Text:** docs/sections/toric-pluripotential-theory-on-ample-line-bundles/index.html; Theorem 21.12.13 (sgpt-E09727EF, tag 8B5B73657BF7, line 238), Proposition 21.12.21 (sgpt-E2F47062, tag 419A1D9F18A9, lines 390–413), Proposition 21.12.23 (sgpt-A47B98F5, tag 73034E124A9A, lines 443–465), Proposition 21.12.24 (sgpt-D3D075B2, tag 725063C1ED05, lines 466–520).
- **Hypotheses:** compact smooth polarized toric variety of §21.12; toric ω-psh u,v; define K(w)=closure dom G_w.
- **Proved identities:** K(max(u,v))=conv(K(u)∪K(v)); rooftop nontrivial iff dom G_u∩dom G_v is nonempty. When nontrivial, K(rooftop)=closure(dom G_u∩dom G_v), and the mass is n! times vol(K(u)∩K(v)). Mass of max is n! times volume of the convex hull.
- **Sharp model:** P¹ with G_u=indicator [0,a], G_v=indicator [b,1], 0<a<b<1. Individual masses a,1−b; rooftop −∞; max has full mass 1. Explicit independent Lelong mass obstruction included in the report.
- **Dependents and limits:** toric mass/rooftop interpretation, §21.13 comparison with Newton bodies; relies on §21.12.13 and 21.12.24 as inputs, so not a full upstream certification.
- **Proposed use:** optional explanatory note in a separately reviewable source patch only; no current source change.

Excluded user-deferred analytic programmes remain **deferred-by-user**.
