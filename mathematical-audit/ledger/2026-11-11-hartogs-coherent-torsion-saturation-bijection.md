# 2026-11-11 classification — Hartogs saturated coherent subsheaves

- **Stable ID:** POME-HARTOGS-COHERENT-TORSION-SATURATION-BIJECTION-001.
- **Status / severity:** verified conditional deduction / low.
- **False printed theorem?** No. Printed Lemma 9.72.1 is correct for its reflexive ambient; this is a genuinely stronger ambient-scope corollary.
- **Mathematical hypotheses:** smooth U, closed analytic A of complex codimension ≥2, arbitrary coherent E, saturated coherent F°⊂E|_(U\A); saturated means torsion-free quotient.
- **Result:** restriction is an inclusion-preserving bijection on saturated coherent subsheaves. The extension is π^{-1}(G), where π:E→E/T(E) and G is the unique saturated extension of F°/T(E°).
- **Independent boundary computation:** E=O_(Δ²)⊕O_(Δ²)/(z,w), A={0}, F°=0. The only saturated extension is T(E)=0⊕O/(z,w); zero itself is not saturated inside E.
- **Printed anchors:** main b6933b772f41b45918f7e25ed1afbbb1fd892272; docs/sections/projective-hartogs-extension/index.html (blob 3191443b49a20377356f519b5e98ec29259f1c7c), lemma source cao-paun-foliations:FF53288F, tag 0A2146B324EB, lines 9 and 14–18. Internal dependency: §9.38.5 tag F35BA7139EC4, main blob fa09a923ef076a99d638d038020ddd3b884afaa7, line 90.
- **Earlier ledger not duplicated:** POME-HARTOGS-TORSIONFREE-SATURATION-001 (2026-10-29) supplies the torsion-free case; POME-HARTOGS-SATURATED-NONBUNDLE-001 and POME-HARTOGS-CODIMONE-ESSENTIAL-001 (2026-10-27) remain unchanged.
- **Proposed optional correction:** additive corollary, not a change to original theorem or source attribution.
- **Affected dependents:** saturated analytic sheaves and foliation extensions §§9.72–9.75, subject to their other hypotheses; meromorphic Hartogs upstream remains conditional.
- **Excluded programme:** Demailly regularization/Bergman/L²/OT/multiscale/positivity-loss remains deferred-by-user.
- **Full proof:** [2026-11-11 report](../reports/2026-11-11-hartogs-all-coherent-saturation-bijection.md).
