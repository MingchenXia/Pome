# 2026-11-14 — An ambient-compatible embedded-resolution repair for Okounkov flag lifting

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Reviewed integrated file:** docs/sections/the-theory-of-okounkov-bodies--flags-and-valuations/index.html, blob 9190d2ae0d3e51ca0ca965000cb9b5b2ec965c85.

**Directly checked:** Definition 19.3.5 (source smooth-flag convention, physical lines 47–56); Definition 19.3.12, source sgpt:E615C683 / permanent E494C67EB4B8, lines 161–179; and Theorem 19.3.19, source sgpt:44C3D868 / permanent B00AB5301F7A, lines 311–332. The relevant printed induction is lines 319–331, especially the unsupported jump from *separate* embedded resolutions in line 323 to compatible embeddings in lines 325–331. The domination input is Theorem 9.10.8 (Hironaka's Chow lemma, permanent 3CD8BF9158DD, docs/tag/3CD8BF9158DD/index.html, line 6). No regularization or Bergman input is used.

## POME-OKO-FLAG-AMBIENT-CENTERS-REPAIR-001 — medium / verified repair proposed only

**Statement examined.** Let X be the smooth compact complex manifold of the transcendental-setting paragraph in §19.3, equipped with its smooth flag X=Y_0 ⊃ Y_1 ⊃ ... ⊃ Y_n. Let Z→X be any proper bimeromorphic morphism with Z reduced. Theorem 19.3.19 asserts that a dominating modification W→X admits a *smooth* lifted flag whose stages are bimeromorphic to the original Y_i.

**Issue in the printed argument (pre-existing candidate POME-OKO-FLAG-NESTED-RESOLUTION-001).** Independently resolving each pair (W_j,W_{i+1}) does not ensure those resolutions are compatible or form nested embeddings. This is a proof-step gap, not a counterexample to the theorem. The following gives a single compatible sequence and discharges the missing compatibility step, conditional only on the explicitly permitted Hironaka embedded-resolution theorem.

### Lemma: one blowup preserves an already smooth nested flag

Let M_0 ⊃ M_1 ⊃ ... ⊃ M_i be smooth closed complex submanifolds of a smooth complex manifold M_0, and let C⊂M_i be a smooth closed submanifold. Blow up the *ambient* M_0 along C. For each 0≤j≤i, its strict transform M_j' is canonically isomorphic to Bl_C(M_j), and is smooth; the transforms are still nested. The induced M_j'→M_j are proper bimeromorphic morphisms.

**Proof.** This is local on M_0. For each j choose holomorphic coordinates (z,w,t) with M_j={t=0} and C={w=t=0}; nested smoothness makes such coordinates possible. In the blowup along the ideal (w,t), the charts indexed by a w-coordinate contain the closure of M_j\C. On the chart where w_1 is the exceptional coordinate, w_k=w_1\xi_k and t_l=w_1\eta_l. The strict transform of M_j is exactly \eta_l=0 for every l, the corresponding w_1-chart of Bl_C(M_j). On charts indexed by a t-coordinate there is no point of the strict transform, because M_j\C has t=0. These local identifications glue and prove the assertion, including smoothness. If C is a Cartier divisor in a particular M_j, its blowup is the identity; the same description applies. □

### Repair of the induction in Theorem 19.3.19

1. By the stated Hironaka domination input, replace the original Z→X with a dominating modification M→X which is a composition of blowups with smooth centers. Because X is smooth, M is smooth. Begin with the flag consisting only of M=W_0.

2. Suppose smooth W_0⊃...⊃W_i have already been constructed, with each W_j→Y_j proper bimeromorphic. The spaces Y_j are smooth by Definition 19.3.5. The proper bimeromorphic map W_i→Y_i is an isomorphism outside a target subset of codimension at least two (the precise normal-target consequence used in printed line 321). Because Y_{i+1}⊂Y_i is an irreducible hypersurface, its generic point lies outside that exceptional subset. Hence its strict transform V⊂W_i is a *nonempty irreducible hypersurface* mapping bimeromorphically to Y_{i+1}. No arbitrary choice of a component over an exceptional stratum is needed.

3. Apply Hironaka **embedded resolution to the single pair (W_i,V)**. This produces a finite succession of blowups of W_i in smooth centers C_k lying in the successive proper transforms of V, ending with a smooth strict transform V'. Importantly, do not resolve the pairs (W_j,V) independently.

4. At each stage, perform the **same** blowup of the currently smooth ambient W_0 along C_k. The center is smooth in W_0 since C_k⊂W_i⊂...⊂W_0 are smooth embeddings. By the preceding coordinate lemma, the simultaneous proper transforms of *all* earlier W_0,...,W_i are precisely their blowups along C_k and are smooth and nested. Their morphisms to Y_j remain proper bimeromorphic. The final proper transform W_{i+1}:=V' is smooth and still maps bimeromorphically onto Y_{i+1}.

5. Repeat for i=0,...,n−1. There are finitely many flag stages and finitely many Hironaka centers at each stage. This yields a single smooth-center modification W→X dominating the original Z→X, with a smooth nested lifted flag as asserted. □

**What this repairs.** The source proof's lines 323–331 can be replaced by the single-pair embedded-resolution plus ambient-center lifting lemma above. There is no need to assume a separately unspecified simultaneous/functorial resolution of all pairs. The only deep existence inputs are Hironaka domination and embedded resolution/principalization, which are expressly allowed external exceptions. The local compatibility lemma is proved here, not quoted. The normal-target codimension-two birational-isomorphism assertion in printed line 321 is retained as the existing Zariski-main/normality input.

**Scope and mathematical classification.** Theorem 19.3.19 is not shown false. The repaired existence argument is complete *conditional on the declared Hironaka and normal-target inputs*, but it is **proposed only**: the printed reading edition still has its original unsupported compatibility sentence. The previous medium candidate is therefore *repair available, source not yet patched*, not an already integrated or fully certified result. No general current trace/pullback invariance proof, Definition 19.3.20, Lemma 19.3.22, or §19.4.7 is transitively certified by this note. Proposed source changes must go to a separate reviewable patch, never directly to production main.

**Dependents:** Theorem 19.3.19; existence aspect of Definition 19.3.20 and Lemma 19.3.22; model/flag prerequisites invoked in §19.4.7. Prior distinct findings POME-OKO-FLAG-TWO-BLOWUPS-001, POME-OKO-FLAG-TRACE-INPUT-001, POME-OKO-FLAG-PRINTED-LABEL-001 and POME-OKO-FLAG-ON-MODEL-001 are not repeated, reclassified, or certified.

**Coverage:** One new proof-repair of a previously reviewed individual theorem in §19.3; zero first-visited numbered sections, zero whole-section certificates. Actual main table of contents: 25 chapters / 747 numbered sections. No tests, build, CI, publication or edits to source/body/registry/permanent tags were performed. Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes remain **deferred-by-user**, neither resolved nor examined.
