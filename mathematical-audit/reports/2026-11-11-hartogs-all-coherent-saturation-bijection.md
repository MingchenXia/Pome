# 2026-11-11 — Hartogs saturation for arbitrary coherent ambient sheaves

**Finding ID:** POME-HARTOGS-COHERENT-TORSION-SATURATION-BIJECTION-001  
**Severity:** low. **Status:** verified conditional deduction (a strengthening, not an error or repair of the printed theorem).  
**Production main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Exact integrated reading edition:** docs/sections/projective-hartogs-extension/index.html, main blob 3191443b49a20377356f519b5e98ec29259f1c7c.  
**Section:** §9.72; source section cao-paun-foliations:FB4ADF9D, permanent section tag 08184FDD8900.  
**Printed Lemma 9.72.1:** original source cao-paun-foliations:FF53288F, permanent tag 0A2146B324EB, physical line 9 (both conclusions), lines 14–18 (replacement proof), particularly line 17 (coherence and saturation through a meromorphic kernel).  
**Conditional internal input:** Theorem 9.38.5, source demailly-complex-geometry:7716022D, permanent tag F35BA7139EC4, docs/sections/normal-spaces-and-tube-continuation--continuation-on-normal-complex-spaces/index.html, blob fa09a923ef076a99d638d038020ddd3b884afaa7, line 90 (meromorphic Hartogs across codimension at least two). The projective case is already the first assertion of printed Lemma 9.72.1.

## New assertion, distinct from the pre-existing torsion-free extension audit

Let U be a complex manifold, A a closed analytic subset of codimension at least two, and E **any coherent analytic sheaf**, possibly containing nonzero torsion supported along divisors or in codimension at least two. Restriction gives an **order-preserving bijection** between

1. saturated coherent subsheaves F of E on U, and
2. saturated coherent subsheaves F° of E° = E|_(U\A).

Here saturated means that the quotient is torsion-free over the local integral analytic rings. In particular, every such F° has a unique saturated coherent extension to E, without any torsion-free, reflexive, or locally free condition on the ambient E.

The 2026-10-29 finding POME-HARTOGS-TORSIONFREE-SATURATION-001 already proves this when the *ambient sheaf itself is torsion-free*. The **new content of this finding** is the arbitrary coherent (potentially torsion-containing) ambient, the canonical poset bijection, and the forced torsion in every extension. The old ID is retained and is not counted again as a new result.

## Complete reduction to the torsion-free result

Since U is smooth, its local rings are Noetherian integral domains. Let T(E) be the coherent torsion subsheaf: locally its sections are those killed by some nonzero holomorphic germ. It is coherent, for instance as the kernel of the canonical morphism E → E**; the kernel is exactly torsion (the bidual map is generically injective and, over a domain, torsion-free modules inject into their double dual). Write

\[
0\longrightarrow T(E)\longrightarrow E
\xrightarrow{\ \pi\ } E_{\mathrm{tf}}\longrightarrow0,
\qquad E_{\mathrm{tf}}:=E/T(E).
\]

The quotient is coherent and torsion-free by construction. Restriction to U°=U\A is exact and satisfies T(E)|_(U°)=T(E°).

Let F° ⊂ E° be coherent and saturated. Every local torsion section t of E° maps to torsion in E°/F°; since that quotient is torsion-free, the image vanishes. Hence

\[
T(E^\circ)\subseteq F^\circ .
\]

Consequently F°/T(E°) is a coherent saturated subsheaf of E_tf|_(U°), because

\[
(E_{\mathrm{tf}}|_{U^\circ})/(F^\circ/T(E^\circ))
\simeq E^\circ/F^\circ
\]

is torsion-free. Apply the **previously established torsion-free ambient** extension argument of POME-HARTOGS-TORSIONFREE-SATURATION-001: its meromorphic Grassmannian continuation uses printed Lemma 9.72.1 and Theorem 9.38.5 as conditional internal inputs. We obtain a unique saturated coherent subsheaf G ⊂ E_tf whose restriction is F°/T(E°). Define

\[
F:=\pi^{-1}(G).
\]

Preimages of coherent subsheaves under a coherent sheaf morphism are coherent (equivalently, F is the kernel of E → E_tf/G). Moreover,

\[
E/F\simeq E_{\mathrm{tf}}/G
\]

is torsion-free, so F is saturated, and exact restriction shows F|_(U°)=F°. This is existence.

For uniqueness, let F_1,F_2⊂E be two saturated extensions of the same F°. Both contain T(E), by the same torsion argument. Their quotients F_i/T(E)⊂E_tf are saturated and agree off A. Uniqueness in the torsion-free case gives F_1/T(E)=F_2/T(E), so F_1=F_2. Equivalently the canonical extension is the inverse image under π of the torsion-free saturation extension. The construction respects inclusions; restriction also respects inclusions, giving the asserted order isomorphism. No sequential compactness, limiting interchange, projective resolutions, or Demailly/L²/OT machinery is used.

## Strict test of the new ambient scope

On U=Δ² with A={(0,0)}, let m=(z,w) and

\[
E=\mathcal O_U\oplus(\mathcal O_U/m).
\]

This is a coherent sheaf **with nonzero torsion** concentrated at A, so it is neither torsion-free nor reflexive. On U° the second summand disappears and E°≅O_(U°). The zero subsheaf F°=0 is saturated in E°. Its unique saturated extension is

\[
F=0\oplus(\mathcal O_U/m)=T(E),
\qquad E/F\simeq\mathcal O_U .
\]

The seemingly natural extension F=0 is **not** saturated: E/F=E has a nonzero torsion skyscraper at the origin. Thus the torsion preimage is essential and cannot be obtained by merely asserting that the ambient torsion sheaf vanishes globally.

More generally, if a coherent E has torsion supported on a divisor meeting U°, every saturated F° already contains that torsion on U°. The construction above includes its entire extension as well.

## Scope, correction, dependents

The printed Lemma 9.72.1 is **correct as written**; it assumes reflexive E, hence a torsion-free E. The 2026-10-29 torsion-free extension and the 2026-10-27 nonbundle/codimension-one examples are **pre-existing findings**, not repairs or discoveries of this run. The codimension-two Hartogs input still matters, and this note does not assert an analogous conclusion on arbitrary nonnormal bases, nor coherent extension of an unsaturated subsheaf.

**Proposed optional change (not applied):** state the above all-coherent, torsion-compatible order-isomorphism as a separate corollary after Lemma 9.72.1, retaining the reflexive formulation, original attribution, permanent tag, and all historical source records. Potential dependents are saturated-sheaf and foliation extensions in §§9.72–9.75 when their ambient coherent sheaves have torsion. Their other geometric hypotheses and the full upstream meromorphic Hartogs proof are not newly certified.

**Coverage:** one incremental, selected proof-level visit to §9.72.1 and one conditional check of the statement of §9.38.5; **0 newly first-visited numbered sections, 0 fully certified sections**. Current actual ToC **25 chapters and 747 numbered sections**, as recorded in SECTION_MATRIX.md. All earlier confirmed errors, proof gaps, dependencies and deferred-by-user records remain unchanged. The dedicated Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remains **deferred-by-user, neither resolved nor certified**. No changes to source/body/registry/canonicalization/main/published site; no build, CI, formal verification or website publication.