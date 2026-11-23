# POME-WEIGHTED-MA-LOGSUMEXP-SEMIGROUP-001 — 2026-11-23

**Severity/status:** low / **verified conditional deduction**, not a false printed theorem, complete upstream certificate, or regularization result.

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

**Main integrated source and anchors:** docs/sections/equations-with-prescribed-singularities--adding-weighted-monge-ampere-measures/index.html, blob 0bc4468db8261e5203d311a2181bde8acf16c1df, Theorem 15.11.1 source non-kahler-pluripotential-theory:382EF8B0, permanent tag 7A54D08FEB18, statement physical lines 10–20, proof 22–100. Supporting uniqueness reference Corollary 15.2.3; bounded-subsolution, mass and convergence dependencies §15.10.1, §16.28.55, §15.9.3, §13.15.2.

**Exact hypotheses:** semipositive big θ, reference φ∈PSH(X,θ) with P_{δθ}(φ) nontrivial for some 0<δ<1, λ>0, and u∼φ with finite weighted measure Mλ(u)=e^{−λu}MAθ^{ext}(u). Restrict the operation to this finite-measure class.

**Verified conditional deduction:** Theorem 15.11.1 and uniqueness furnish a closed commutative associative cancellative addition u⊞λv determined by Mλ(u⊞λv)=Mλ(u)+Mλ(v). Constant shifts give Mλ(u+t)=e^{−λt}Mλ(u), so for arbitrary c_i,
\[
 (u+c_1)\boxplus_\lambda\cdots\boxplus_\lambda(u+c_k)
 =u-\lambda^{-1}\log\sum_i e^{-\lambda c_i}.
\]
In particular u⊞λu=u−(log2)/λ and the soft-min shift lies between min c_i−(log k)/λ and min c_i, with sharp equality/limiting cases. Associativity and cancellation use the *same ordinary-type uniqueness*, not title matching or sequential compactness. Complete derivation in the linked report.

**Affected dependents/proposed correction:** optional explanatory structural corollary after §15.11.1, relevant to mass-deficit addition in §15.12; **no amendment needed** to the original theorem. No body/registry/tag edit is authorized on the audit branch.

**Other actual coverage:** §15.13 full direct (blob db560c935a7d651803427b6243957ea1f957b468, lines 6–120; strict c<1 has an explicit Kähler constant-shift countermodel at c=1, but the printed theorem is correct as stated); §16.21 full direct (blob 8d55c95795ea2a0a3cf5cb81bd4abb4ba867a16a, lines 6–81; mass/contact support conditional on §13.8.8–9 and §16.13.5). Selected §15.9.3/16.28.55 only, no entire upstream chains.

**Unresolved/deferred:** bounded solver, capacity continuity, polynomial mass tail, strict barrier existence and mixed non-pluripolar limit inputs not transitively certified; Demailly regularization/Bergman/L²/OT/multiscale/positivity-loss dedicated work **deferred-by-user**, not solved or reviewed.

[Full English proof and audit](../reports/2026-11-23-weighted-ma-logsumexp-and-envelope-support.md) · [precise coverage](../coverage/2026-11-23-weighted-ma-barrier-and-singularity-envelopes.md).
