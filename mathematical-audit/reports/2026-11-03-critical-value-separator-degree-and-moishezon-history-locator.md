# Audit: critical-value separators for section maps and a missing Moishezon-history locator
**Date:** 2026-11-03. **Production main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Scope:** selected mathematical proof and provenance checks in §§19.9 and 25.9. **No whole-section or transitive-dependency certification.**

## POME-SECTIONMAP-CRITICAL-SEPARATOR-DEGREE-001
**Severity / status:** low / verified conditional deduction (the new model is proved directly; the downstream curvature-rank theorem is *not* newly certified). **Disposition:** optional explanatory example; **no error in the printed Proposition 19.9.19**.

**Source:** \`docs/sections/flags-convex-bodies-and-section-growth/index.html\`, current-main blob \`83557f0e15275253661fe679c75407e6636d497c\`, §19.9.19 source \`non-kahler-pluripotential-theory:77A30A69\`, permanent tag \`C8B2CB1B6819\`, physical lines **394–426**, especially critical-image filtering at **404–426**. Section permanent tag \`926A00196D5E\`.

**Printed hypothesis and use.** On a compact connected complex manifold with a smooth Hermitian line bundle \(L\), for a nonzero \(W\subset H^0(X,L^p)\), the proof principalizes the base ideal and obtains a proper holomorphic map \(f\). If its maximal differential rank is \(d\), the critical image \(T=f(\{\operatorname{rank}df<d\})\) has dimension at most \(d-1\). The proof chooses a homogeneous polynomial \(P\), of some degree \(a\), vanishing on \(T\) but not on \(f(Y)\). Its final sentence correctly says that \(a\) may depend on \(p,W\) and *no bound is needed*. This proof also invokes proper-image/Chow facts; those prerequisites have **not** been newly proved here. Principalization is an allowable Hironaka input.

**New exact degree-sharpness model.** Fix *once and for all* \(X=\mathbf P^1\), \(L=\mathcal O_{\mathbf P^1}(1)\) and the standard smooth Fubini–Study metric (positive, rank-one curvature). For each integer \(p\ge2\) let
\[
W_p=\operatorname{span}\{s_0=Z_0^p,\quad s_1=Z_1^p+Z_1Z_0^{p-1}\}\subset H^0(\mathbf P^1,\mathcal O(p)).
\]
The two sections have no common zero: if \(Z_0=0\), then \(s_1=Z_1^p\ne0\), while if \(Z_0\ne0\), then \(s_0\ne0\). The associated morphism to \(\mathbf P(W_p^*)\simeq\mathbf P^1\) has, in \(z=Z_1/Z_0\) and target coordinate \(w=s_1/s_0\),
\[
f_p(z)=z^p+z.
\]
It is finite, surjective, and generically rank one. Its \(p-1\) finite critical points are the distinct roots of
\[
p z^{p-1}+1=0.
\]
For each such \(c\), \(c^p=-c/p\), hence \(f_p(c)=(1-1/p)c\). These \(p-1\) critical values are pairwise distinct and finite. At infinity the local target coordinate is
\[
\frac1{f_p(1/\zeta)}=\frac{\zeta^p}{1+\zeta^{p-1}},
\]
which has vanishing derivative at \(\zeta=0\) for \(p\ge2\). Thus infinity is one further critical point with critical value infinity. Therefore the critical-image set \(T_p\subset\mathbf P^1\) contains **exactly \(p\) distinct points**, and the full image is \(\mathbf P^1\).

A nonzero homogeneous separator \(P(U,V)\) of degree \(a\), regarded as a section of \(\mathcal O_{\mathbf P^1}(a)\), has total zero multiplicity \(a\). If \(P\) vanishes on \(T_p\), then \(a\ge p\). Conversely, the product of the \(p\) distinct linear equations of these points is a degree-\(p\) homogeneous separator. Thus
\[
\boxed{\min\{a:\;0\ne P\in H^0(\mathbf P^1,\mathcal O(a)),\ P|_{T_p}=0\}=p.}
\]
For \(p=2\), the critical values are \(-1/4\) and \(\infty\), already requiring \(a=2\). The exact linear growth holds for all \(p\ge2\), with **fixed \(X,L,\dim W_p=2\), fixed positive-curvature rank, and fixed map rank \(d=1\)**.

**Consequence and proposed correction:** The printed existence proof and its last qualification are sound in this respect. Do **not** replace the cutoff by a separator with a degree bounded independently of \(p\), the chosen section subspace, or the map's branch complexity. Optionally add the explicit \(f_p\) example after §19.9.19. The example does not contradict, nor independently certify, Corollary 19.9.20; that corollary and the dependent §§19.9.21–24 still use the printed argument and their previous proof-input status.

## POME-OKO-MOISHEZON-HISTORY-LOCATOR-001
**Severity / status:** low / confirmed error **of internal bibliographic/provenance locator only** (not a false mathematical theorem and not a proof that Moishezon's theorem fails). **Disposition:** proposed text/reference repair; not applied to production content.

**Source:** same current-main \`docs/sections/flags-convex-bodies-and-section-growth/index.html\`, blob \`83557f0e15275253661fe679c75407e6636d497c\`, §19.9.11, heading source \`non-kahler-pluripotential-theory:C4509F9F\`, permanent heading tag \`F8F1527B70F2\`, physical lines **273–275**. The sentence invokes the Moishezon theorem in the form “an irreducible compact complex space of dimension \(n\) with \(n\) algebraically independent meromorphic functions admits a modification from a smooth projective manifold” and says that **the source for this form is given in §25.9**. The invocation is used again at §19.9.13, physical lines **302–313**, source \`non-kahler-pluripotential-theory:B609DF1D\`, permanent theorem tag \`0F8B7237A1BA\`.

**Actual referenced destination:** \`docs/sections/history--sections-convexity-and-non-archimedean-geometry/index.html\`, main blob \`5b186b1cb452407218e73d4a733652d22ac63bf2\`, §25.9 permanent tag \`482A6169B3A6\`, source variant \`foundations-of-pluripotential-theory:5CFAA9E4\`, physical lines **5–12**. The text lists historical works on graded sections, convex bodies, toric geometry, b-divisors and non-Archimedean geometry but does **not** name Moishezon or give a source for the projective-modification theorem. The independently opened §25.5 history page (\`docs/sections/history--cohomology-curves-and-complex-geometry/index.html\`, blob \`4b54a9392d29716c18ac4bc41c84c8ec2d1bd586\`, lines 5–13) likewise did not supply that name/reference; this is not an exhaustive search of the bibliography.

**Exact defect:** The claim that a specific historical source is *given at the linked location* is false in the current integrated reading edition. This is not evidence against Moishezon's theorem itself. Its use remains an **external mathematical input**, and historical attribution is separately required, rather than silently erased.

**Proposed correction:** Supply an explicit, bibliographically verified reference and the precise projective-modification formulation in §25.9, preserving its existing Okounkov, Kaveh–Khovanskii and other historical attributions; or change the §19.9.11 pointer to another *verified* location that already contains the appropriate source. Do not invent a reference. Affected provenance: §19.9.11, Theorem 19.9.13, and the last assertion of Corollary 19.9.17 (§19.9.365–380). No modification to their mathematical statements is proposed.

## Coverage / status
This is **first direct historical-reference-content inspection** of §25.9 (not a proof), and a **new selected critical-image polynomial step / explicit branching model** in the previously partly audited §19.9.19. The remainder of §19.9, the complete Remmert–Chow dependency chain and all of §25.9's historical claims have not been exhaustively certified. Project's actual table of contents still has **25 chapters, 747 numbered sections, zero whole mathematical sections certified**. Prior ledger findings remain unresolved/resolved/deferred as recorded; in particular the excluded Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale atlas and positivity-loss programme remains **deferred-by-user**, not solved or reopened.

The audit inspected actual current integrated HTML and the stated reference target; no project build, test suite, CI, formalization, website publication or production/source/registry/tag change was carried out.