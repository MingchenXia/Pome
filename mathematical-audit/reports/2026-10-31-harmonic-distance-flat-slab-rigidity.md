# Harmonic-distance rigidity: classification by parallel slabs

**Reviewed:** 2026-10-31. **Production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Stable ID:** POME-DIST-HARMONIC-SLAB-RIGIDITY-001. **Severity:** low.
**Status:** verified conditional deduction; the original printed results are not shown false, and no integrated repair is claimed.

## Exact reading-edition anchors

Main **docs/sections/planar-boundary-distance-and-convexity/index.html**, blob **25fd0fd57d3e51f9224a25341ace77584b2a1a2a**:
- Proposition **3.9.2**, source **klimek-pluripotential-theory:219D9DEC**, permanent **59D258340230**, physical lines **37–39** (planar subharmonic distance criterion), **44–68** (nearest-point geometry, eikonal formula, semiconcavity, weak Hessian), and **70–86** (global convexity).
- Proposition **3.9.1**, source **klimek-pluripotential-theory:79D31B13**, permanent **964B6728E795**, lines **7–32** (interior negative distance; different hypothesis).
- Proposition **3.9.3**, source **klimek-pluripotential-theory:366D2F88**, permanent **BBEB233BF8A4**, lines **91–106** (the connected-neighborhood assumption; compared contextually).

Selected independent cross-chapter proof audit: main **docs/sections/envelopes-and-model-potentials--measures-on-contact-sets--concentration-on-the-contact-set/index.html**, blob **840ebcb98be09245369315fa0c0288b936040098**. Lemma **16.13.1**, source **foundations-of-pluripotential-theory:86AF9332**, permanent **15A418789279**, lines **10–26**; Lemma **16.13.3**, source **foundations-of-pluripotential-theory:F155A867**, permanent **175BA4BB6A7C**, lines **43–64**; Theorem **16.13.4**, source **foundations-of-pluripotential-theory:DDE3B556**, permanent **38E18A798D6B**, lines **69–145**. Read specifically the shrinking-capacity bad sets (85–94), decreasing lower-semicontinuous obstacle construction (97–105), and weighted convergence/truncation passage (108–145), with no full certification. Its big-class analytic-singularity input through §§16.13.2/10.4.6 remains conditional: the excluded regularization programme was not inspected.

## Complete new theorem

Let m >= 1, let F be a nonempty proper closed subset of real Euclidean space R^m, and define d(x)=dist(x,F). Then:

**d is harmonic on all of R^m minus F if and only if F is a hyperplane, a closed parallel slab, or a closed half-space.**

Equivalently, there exist a unit vector a and a nonempty proper closed interval I of the real line, with possibly infinite endpoints or a singleton, such that

\[
 F=\{x\in\mathbb R^m:\langle a,x\rangle\in I\}.
\]

No convexity of F is assumed. The statement requires harmonicity **everywhere outside F** and does not assert an all-dimensional version of the printed *subharmonic* criterion, which is specific to R^2.

## Proof, with no external regularization input

Put Omega=R^m\F. The nearest-point distance is attained at every x in Omega by compactness of a bounded minimizing sequence. Since d is harmonic, it is smooth there. If p is any closest point to x, then the smooth function z -> |z-p| majorizes d and touches it at x. Differentiability therefore gives

\[
 \nabla d(x)=(x-p)/|x-p|,\qquad |\nabla d(x)|=1. \tag{1}
\]

For each connected component C of Omega, elementary harmonic calculus yields

\[
 0=\Delta\!\left(\tfrac12|\nabla d|^2\right)
   =\sum_{i,j}(\partial_{ij}d)^2+\nabla d\cdot\nabla(\Delta d)
   =|D^2d|^2. \tag{2}
\]

Hence d is affine on C: d(z)=<a,z>+b with |a|=1. Choose x in C, put r=d(x)>0 and p=x-ra in F. The affine expression is exactly

\[
 d(z)=\langle a,z-p\rangle>0\quad(z\in C). \tag{3}
\]

For all t >= 0 the ray x+ta remains in C: up to its hypothetical first exit time T, (3) gives d(x+ta)=r+t, which at the exit would be positive by continuity, contradicting that it had reached F. Along the full ray,

\[
 d(x+ta)=r+t=|x+ta-p|.
\]

Thus p remains a nearest point at x+ta. For any q in F and all t >= 0,

\[
 (r+t)^2\le |(r+t)a-(q-p)|^2
 =(r+t)^2-2(r+t)\langle a,q-p\rangle+|q-p|^2.
\]

Let t increase without bound. It follows that <a,q-p> <= 0 for every q in F. Consequently F lies in the closed half-space H^-={z:<a,z-p><=0}. The open half-space H^+={z:<a,z-p>>0} is disjoint from F, connected and contains x, so H^+ is contained in C. Formula (3) gives the opposite inclusion. Hence **every connected component of Omega is itself an entire open half-space**. The bounding hyperplane belongs to F by continuity of the distance.

Two disjoint open half-spaces must have parallel, oppositely oriented normals; in particular, more than two pairwise disjoint open half-spaces cannot exist. The complement Omega therefore consists either of one half-space or two oppositely facing half-spaces. The closed set F is respectively the other closed half-space, or the closed slab left between the two parallel boundary hyperplanes, including the zero-width hyperplane case.

Conversely, for F={alpha <= <a,x> <= beta}, with unit a and extended real endpoints (omitting infinite-endpoint terms), its distance is

\[
 d(x)=\max\{\alpha-\langle a,x\rangle,0,\langle a,x\rangle-\beta\}. \tag{4}
\]

On every component of its complement, this expression is affine; hence d is harmonic. QED.

## Model check, classification, correction and limitations

For the closed ball F=closure(B(0,R)) in R^m, m>=2, the exterior distance is d(x)=|x|-R and Delta d=(m-1)/|x|>0. It is subharmonic but **not** harmonic. An exact small symbolic check gave the radial Laplacians 1/r, 2/r, 4/r in dimensions 2,3,5, plus three rational slab-distance sanity points; this is not a project build, software test suite or formal verification.

**Mathematical status:** new verified conditional deduction, not a false printed theorem, a purported complete proof of Proposition 3.9.2, or a repair requiring integration. The new stronger **harmonic** rigidity is proved independently. Prior POME-DIST-CURVE-CODIM-001 and POME-TUBE-RADIUS-SHARP-001 concern higher-dimensional **subharmonic** tubular distances and remain distinct, unchanged. Proposed separately reviewable action: append an optional all-dimensional harmonic-distance corollary after Proposition 3.9.2, preserving all existing permanent tags, original provenance and hypotheses. Affected interpretation: flat distance models in §§3.9 and 9.19. No source/body/registry/canonicalization/main/tag edit is authorized by this report.

**Actual mathematical coverage:** §3.9.2 eikonal/semiconcavity/Hessian passage and §3.9.3 connectedness compared directly; an independent full rigidity theorem is proved. §§16.13.1/.3/.4 selected capacity/obstacle/contact-limit steps were inspected only contextually, with no new source error established. In particular §16.13.2's analytic-singularity input is **conditional**, not certified. Neither audited area has been wholly mathematically verified with all dependencies. Overall ToC remains **25 chapters, 747 numbered sections, zero entire mathematically certified sections**. Old unresolved, resolved and deferred statuses remain unchanged; no project build, tests, CI, formalization, publication or production writes. The Demailly approximation/regularization and dedicated Bergman/L2/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof-completion programmes remain strictly **deferred-by-user**.
