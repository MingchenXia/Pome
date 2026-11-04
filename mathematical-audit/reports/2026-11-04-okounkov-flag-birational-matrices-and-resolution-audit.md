# 2026-11-04 — Okounkov flags: birational correction matrices and simultaneous-resolution audit

**Production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Integrated section:** docs/sections/the-theory-of-okounkov-bodies--flags-and-valuations/index.html, main blob 9190d2ae0d3e51ca0ca965000cb9b5b2ec965c85.
**New direct reading:** §19.3.12–19, physical lines 161–179, 183–236, 241–305, 311–332; related §19.3.20–22 and §19.4.7 are contextual checks only. No whole-section or complete dependency certification.

## POME-OKO-FLAG-TWO-BLOWUPS-001 — low / verified conditional deduction

Test Definition 19.3.12 (source sgpt:E615C683, permanent E494C67EB4B8), correction Equation 19.3.13 (source sgpt:827D77FC, permanent 63511F34173E), Proposition 19.3.14 (source sgpt:DD7439A2, permanent D094DD00A592), Proposition 19.3.17 (source sgpt:6A0E92BC, permanent 8D2910CD1CEC), and Equation 19.3.18 (source sgpt:E051E414, permanent 1C158885A628).

Let X=P², with affine coordinates (x,y), and take the flag Y₁={x=0}, Y₂=p=(0,0). Every nonzero rational function f can be written near the generic point of Y₁ as f=x^a g, a∈Z, with g(0,y)=y^b times a unit at p, b∈Z. Thus ν_Y(f)=(a,b).

Blow up p, in the chart x=uv, y=v. The strict-transform flag is W₁={u=0}, W₂={u=v=0}, and the exceptional curve E₁={v=0}. Removing the generic order a along W₁ leaves v^a g(0,v), hence

\[
\nu_W(\pi_1^* f)=(a,a+b)=(a,b)\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]

The geometric correction is E₁|_{W₁}=[W₂], because π₁^*[Y₁]=[W₁]+[E₁]. In particular the sign is **positive**, the correction is **upper unitriangular** for **row** valuations, and the transform multiplies on the **right**. The divisors {x=0} and {y=0} yield the direct checks (1,0)↦(1,1) and (0,1)↦(0,1).

Blow up W₂ again. Use u=u₂v₂, v=v₂, so (x,y)=(u₂v₂²,v₂), with lifted flag W₁'={u₂=0}, W₂'={u₂=v₂=0}. The same computation gives ν_{W'}((π₁∘π₂)^*f)=(a,2a+b). Both individual matrices are G=[[1,1],[0,1]], so their product G²=[[1,2],[0,1]] is exactly the correction for the composition in (19.3.18). This holds for **every nonzero rational function** with the flag valuation defined above, not just monomials. It tests the birational convention without asserting the printed propositions for all positive currents.

**Decision:** original valuation/correction propositions not refuted; this is a reproducible local model, not a full repair or certification. Optional proposed addition: include the two-chart calculation after Proposition 19.3.17.

## POME-OKO-FLAG-NESTED-RESOLUTION-001 — medium / candidate proof gap (not a false theorem)

Theorem 19.3.19, source sgpt:44C3D868, permanent B00AB5301F7A, lines 311–332, asserts the existence of a dominating smooth-center modification carrying a smooth lift of a nested flag. Its proof cites Theorem 9.10.8 (Hironaka's Chow lemma, permanent 3CD8BF9158DD) to dominate the bimeromorphic morphism. Lines 323–331 then **choose embedded resolutions for pairs (W_j,W_{i+1}) for each j** and directly assert **canonical compatible embeddings** W_i'⊂...⊂W₀'.

The existence of separate embedded resolutions does **not by itself** furnish morphisms and nested strict-transform embeddings between independently resolved ambient pairs. The quoted Theorem 9.10.8 is the domination statement; it does not state compatibility of nested resolutions. The missing step is a **single ambient-compatible sequence** of permissible blowups (or a precise simultaneous/functorial embedded-resolution theorem) whose strict transforms preserve smoothness of the earlier W_j while resolving the next W_{i+1}, and whose restrictions remain birational over each Y_j. Hironaka embedded resolution is a permitted input, but the compatible form must be stated or the induction arranged.

**Decision:** possible **proof-step gap**, not a counterexample to the theorem. Severity medium because the existence of lifted flags enters Definition 19.3.20 and Lemma 19.3.22, with §19.4.7 as downstream context. Resolution requires checking whether the author's intended Hironaka theorem contains the simultaneous nested-centre assertion; do not reclassify the existing separate §19.4.7 finding POME-OKO-FLAG-ON-MODEL-001.

## POME-OKO-FLAG-TRACE-INPUT-001 — low / candidate notation/type issue

The paragraph following Equation 19.3.13, lines 176–179 (source context sgpt:E615C683 / E494C67EB4B8), writes Tr_{W₁}((π^*[Y₁]−[W₁])|_{W₁}). But the §20.2 trace operator has an **ambient** potential/current as input and the restricted current **on W₁** as output (see docs/sections/the-trace-operator/index.html, main blob 1f3a3e4f0317a308b43bd3df53dda84c5f3fa50a, lines 49–71). The displayed argument appears already restricted before applying Tr_{W₁}. This looks ill-typed or redundant unless an additional convention is stated.

**Proposed clarification:** Tr_{W₁}(π^*[Y₁]−[W₁]) as the trace of the **ambient** residual divisor, agreeing with its classical restriction to W₁; do not change the matrix or permanent tags. The two-blowup model independently checks the intended restriction. This is not a proof that a valuation assertion is false.

## POME-OKO-FLAG-PRINTED-LABEL-001 — low / confirmed error in reader locator only

The untagged numbered equation inside Proposition 19.3.14 (source sgpt:DD7439A2 / permanent D094DD00A592), physical lines 183–188, visibly has equation label **10.14** even though its integrated reading location is §19.3 and the adjacent tagged equations have reader locators 19.3.13, 19.3.15, 19.3.16, 19.3.18. This is a source-era number displayed as a current reader locator, contrary to the integration numbering contract in AGENTS.md.

**Proposed correction:** use the generator's current-section numbering or leave the untagged identity unnumbered, preserving any source original number in provenance. Do not mint a tag or change the mathematical formula. This is a confirmed **editorial locator** error, **not** a false mathematical theorem.

## Coverage, external inputs and exclusions

Precisely performed: explicit one- and two-blowup valuation calculations; matrix and sign checks; inspection of the proof step in §19.3.19 and its quoted Hironaka domination statement (docs/tag/3CD8BF9158DD/index.html, main blob d18c8ad0d4a849626e9cf982293e9eb0266915af); trace-input comparison; exact rendered equation-label comparison. General positive-current transformations, all trace operators, all nested Hironaka resolutions and the entire §19.3 dependency chain are **not** certified. Existing main has 25 chapters and 747 numbered ToC sections, zero completely mathematically certified sections.

Demailly approximation/regularization, Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion remain **deferred-by-user**, with all old notes preserved, not resolved or revisited. All old error/gap/duplicate/external classifications remain unchanged. No build, test, formal verification, GitHub Actions CI, website publication, production main/source/registry/canonicalization/tag change.
