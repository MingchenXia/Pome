# A rational logarithmic pole with an explicit maximal Hartogs domain

**Date:** 2026-11-03. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Finding:** POME-HARTOGS-RATIONAL-LOG-NATURAL-BOUNDARY-001 — **low / verified conditional deduction**. This is an independent explicit family verifying the printed proposition, **not** a false theorem, a proof-gap repair, or a certification of its general proof.

## Integrated statement and exact anchors

- Reading edition on main: docs/sections/complete-hartogs-domains-and-taylor-coefficients/index.html, blob 641a66c419e4a1f7207cd301b51f27f3a6efd6f9.
- Proposition 9.15.1: source label klimek-pluripotential-theory:7CA9E7D7; permanent tag 202C805DC8A2; hypotheses and conclusions on physical lines **8–16**, integrated proof on **21–27**.
- Section 9.15: source klimek-pluripotential-theory:1253F321, permanent section tag F6F3F90BB780 (line 5).
- The relevant assumptions are that D is open, R:D→(0,+∞] is lower semicontinuous, H={(z,w):z∈D, |w|<R(z)} is complete Hartogs, and f is a holomorphic function for which H is a domain of existence. Its coefficient conclusion uses the *upper-semicontinuous regularization* of the limsup. We do not change these assumptions.

## Self-contained family, including the polar base fiber

Fix arbitrary integers p,q≥1, take D=ℂ and define
$$
u(z)=\frac pq\log|z|,\qquad
R(z)=
\begin{cases}
 |z|^{-p/q},&z\ne0,\\
 +\infty,&z=0.
\end{cases}
$$
Here u(0)=-∞. The radius is lower semicontinuous in the extended positive sense, and u is subharmonic. The exact Hartogs domain is
$$
H_{p,q}=\{(z,w)\in\mathbb C^2:|z|^p|w|^q<1\}.
$$
It contains **the entire vertical fiber over z=0**, not just a punctured piece, and is connected. It is pseudoconvex without invoking the statement under audit: the smooth function
$$
\Phi(z,w)=|z|^2+|w|^2-\log\bigl(1-|z^pw^q|^2\bigr)
$$
is plurisubharmonic on H; it is strictly psh because of the Euclidean summand. It is a proper exhaustion, since on a bounded sequence approaching any finite boundary point the logarithmic term tends to +∞, and the Euclidean term tends to +∞ at infinity.

Define the explicit holomorphic function
$$
F(s)=\sum_{k=1}^\infty s^{2^k}\quad(|s|<1),\qquad
f(z,w)=F(z^pw^q)
      =\sum_{k=1}^\infty z^{p2^k}w^{q2^k}.
$$
Normal convergence on H follows directly from the compact-uniform bound |z^pw^q|≤r<1. Its fiberwise Taylor coefficients are exactly
$$
c_j(z)=
\begin{cases}
z^{p2^k},&j=q2^k,\ k\ge1,\\
0,&\text{otherwise}.
\end{cases}
$$
Consequently, for every z≠0 and every nonzero coefficient,
$$
\frac1{q2^k}\log|c_{q2^k}(z)|
   =\frac pq\log|z|=u(z).
$$
Every other term is -∞, by the convention log 0=-∞. At z=0 **all** coefficients of positive degree vanish, so the limsup is -∞=u(0). Thus in this singular family the stronger *pointwise* identity already holds:
$$
\boxed{\displaystyle
\limsup_{j\to\infty}\frac{\log|c_j(z)|}{j}
  =u(z)\quad\text{for every }z\in\mathbb C.}
$$
The regularized limsup in Proposition 9.15.1 therefore also equals u, including at the infinite-radius fiber.

## Proof of maximality / domain of existence without a gap theorem

If ζ is a root of unity of order 2^N, then along s=rζ with 0<r↑1,
$$
F(r\zeta)=
\sum_{k=1}^{N-1}r^{2^k}\zeta^{2^k}
+\sum_{k\ge N}r^{2^k}.
$$
The first sum stays bounded. The second is nonnegative and tends to +∞: for each fixed M the first M terms in the tail tend to one, so its liminf is ≥M, with M arbitrary. Therefore F has no holomorphic continuation across any dyadic root of unity. These roots are dense in the circle (the mesh 2π/2^N tends to zero), hence no neighborhood of *any* unit-circle point admits continuation of F. This is elementary and does not invoke Hadamard's gap theorem or another external result.

Every finite boundary point (z0,w0) of H satisfies |z0^pw0^q|=1, so z0w0≠0. The holomorphic map s(z,w)=z^pw^q is a submersion there: ∂s/∂w=qz^pw^{q-1}≠0. There is a local holomorphic section of s taking s0=z0^pw0^q to (z0,w0). If f extended across that boundary point, composing the extension with this section would extend F across s0, a contradiction. Thus f extends across **no** boundary point of H; H is a domain of existence of this particular f. This rules out the rational-function pitfall in which the coefficients have the correct growth but f nonetheless extends across some boundary patches.

The model also checks the logarithm/sign convention geometrically: away from the coordinate axes the Reinhardt logarithmic image is the half-space p log|z|+q log|w|<0; the fiber log-radius is -(p/q)log|z|, so the coefficient growth has the *positive* value +(p/q)log|z| = -log R. No missing factor q or 2 occurs.

## Classification, originality, downstream scope, proposal

**Severity low; status verified conditional deduction.** Proposition 9.15.1 is correct in this family. It proves the maximal-continuation and coefficient-growth conclusions **by explicit construction for every positive rational logarithmic slope**, including a nontrivial polar base point with an entire vertical fiber. It does not certify the general pseudoconvexity/Stein domain-of-existence input used for arbitrary psh weights, nor the general plurisubharmonic Hartogs lemma in the printed proof.

This is distinct from the existing POME-HARTOGS-USC-LIMSUP-NECESSARY-001 (a constant-radius bidisk where the raw limsup fails at a point) and POME-HARTOGS-EQUALITY-WITHOUT-EXISTENCE-001 (a rational function whose coefficient identity holds without maximal continuation). Here **both** properties hold simultaneously with a nonconstant logarithmic pole and noncompact entire fiber. Do not reclassify those earlier results or replace them with this one.

**Proposed optional addition:** an explicit example after Proposition 9.15.1 showing H_{p,q}, f=F(z^pw^q), the exact coefficient slopes and the dyadic-root proof of maximality. This is only a proposed separate reviewable patch; do not alter the integrated text, source provenance, registry, canonicalization, or permanent tag. The only directly reviewed dependent is the local coefficient representation clause of Proposition 9.15.1; §9.62's Reinhardt/convex conventions are a possible application, **not** a newly verified theorem. Historical attribution remains untouched.

**Coverage:** targeted re-review of §9.15.1, physical lines 8–16 and 21–27, using an independent rational-pole family and elementary natural-boundary proof. This §9.15 was already partly sampled on 2026-10-30 and 2026-11-02, so no new first-covered ToC row and **no whole section certification**. Current inventory remains **25 chapters / 747 numbered sections / zero entire mathematical section certifications**. Previous errors, gaps, externals and all owner-excluded Demailly approximation/regularization/Bergman/weighted L²/Ohsawa–Takegoshi/multiscale/positivity-loss work stay unchanged and **deferred-by-user** where applicable. No tests, builds, CI, formal verification, or website publication were performed.
