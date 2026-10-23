# Singular metrics, generation and canonical systems

The `analytic-methods` contribution exports a bounded selection from the
Gerby-Literature review of Demailly's *Analytic Methods in Algebraic Geometry*.
The source book is S0050. It is distinct from S0002, the earlier *Complex
Analytic and Differential Geometry* contribution, and from the later S0120
survey. The whole-book inventory is a research record, not a claim that every
argument in the book has a complete Pome proof.

## Selected mathematics

| Packet | Placement | Exact scope |
| --- | --- | --- |
| R0300 | Nef line bundles and section growth | Kodaira dimension is at most numerical dimension for a nef line bundle on a compact Kähler manifold; smooth-center principalization is an explicit input. |
| R0301 | Sheaf cohomology; adjoint generation | Analytic Castelnuovo–Mumford generation via a Koszul complex, then a fixed twist generating every semipositive multiplier ideal. |
| R0302 | Singular metrics and square-integrable resolutions; compact vanishing | Local weighted resolution, a compact Kähler singular-metric estimate, and compact Nadel vanishing. |
| R0303 | Canonical rings and minimal singularities | A double-cover surface with finite integrability threshold whose canonical ring requires a degree-four generator. |
| R0304 | Projective division; canonical rings | Global singular-metric Skoda division and a generation bound retaining the finite-system dimension and approximation coefficient. |
| R0305 | Dolbeault spectral asymptotics | Failure of an unrestricted joint threshold limit for varying nonintegrable unitary connections. |
| R0307 | Exceptional divisors and curvature | A surface example separating negative definite intersection matrices from negative curvature metrics and computing the mixed terms explicitly. |
| R0308 | Griffiths curvature and division | A vector-valued division estimate with a Griffiths semipositive ambient bundle and one ambient determinant twist. |
| R0309 | Holomorphic Morse inequalities | A uniform random index-integral error for given rational ample/effective decompositions; no existence theorem for those decompositions or full jet-volume theorem is inferred. |
| R0310 | Adjoint generation and multiplier ideals | Transfer of prescribed jets from one sufficiently jet-generating power of a line bundle to its adjoint. |
| R0311 | Envelopes with integral normalization | Pointwise attainment, large-degree single-section approximation and finite-degree envelope comparison for a rational big line bundle with a fixed denominator and strict analytic reference metric; intrinsic densities use one tensor root. |
| R0312 | Numerical polynomials and section growth | Elementary bounds for large values of an integer-valued polynomial with positive leading coefficient. |
| R0313 | Analytic regularization; estimates along exhaustions | Neighborhood regularization, sublevel estimates, weighted Runge approximation and singular vanishing on a Kähler manifold with a smooth plurisubharmonic exhaustion. A constant curvature bound gives the stated global square-integrable estimate. |
| R0314 | Lelong numbers and multiplier ideals | Local higher-direct-image vanishing and adjoint multiplier-ideal cohomology descent for a given finite sequence of smooth blowups. |
| R0315 | General complex cohomology | Hausdorff smooth and weak-current Bott–Chern quotient topologies and their homeomorphism in every bidegree on a compact complex manifold. |
| R0316 | Diagonal logarithmic weights | An explicit finite-generator box and metric/radial-normalization supplement to the existing complete real-exponent monomial ideal criterion. |
| R0317 | Nef line bundles and section growth | Higher-cohomology growth for a metric-nef line bundle and a fixed vector bundle, with the sharper projective bound. |
| R0321 | Numerical dimension, divisor metrics and vanishing | Projective Kawamata–Viehweg type vanishing with the effective rational divisor and multiplier ideal retained, in degrees above dimension minus nef numerical dimension. |
| R0322 | Numerical polynomials and section growth | Coherent analytic Euler polynomials for all integer twists, exact support dimension and normalized positive leading coefficient, retaining nilpotent structure and generic lengths. |

R0306 is excluded: the proposed smooth weak-exhaustion vanishing theorem is
already proved in the active contribution at `E5505B695336`. Other research
candidates require a separate selection review before the adapter can accept
them. The spectral example does not alter fixed-threshold holomorphic Morse
inequalities. The surface and canonical-ring examples do not refute the
separate asymptotic cohomology or finite-generation theorems.

## Organization and reuse

The selected fragments are split only before complete statements. Compact
Nadel vanishing sits with compact vanishing, its analytic estimate and local
resolution with the complete-metric methods, and the coherent-sheaf generation
criterion with sheaf cohomology. Projective division and its canonical-ring
application likewise occupy their respective subjects. Stable source labels
produce permanent global tags; Pome generates the reader's section, statement
and equation numbers.

The proof expansion for `sgpt/lma:varphian` (`A8896460B129`) replaces its quoted
uniform-generation step with the selected theorem and its very ample twist.
The statement is unchanged. Exact statement and original-proof hashes guard
the edit. The family statement at `E61430B531F3` retains its existing proof.
The compact singular estimate remains separate from both the existing smooth
theorem and the cohomological Nadel conclusion.

The current comparison uses Pome `da63fcd770fb06e0bc58db7e6754d17b53dcc9a8`,
including the Cao–Păun source pinned at
`a6e5b1149b8e20e8312bbc335156182b7a416697`. All 727 files in the eight older
active source graphs were checked against the prior comparison and are
unchanged. That byte comparison preserves the prior bounded reviews; it is
not a new full mathematical review of every source proof. All formal
statements in the twelve newly included Cao–Păun packets were compared, and
the complete proofs at the two overlapping interfaces were read.

Compact singular-metric Nadel vanishing is already canonical at
`4F4355678C85`. The equivalent R0302 corollary and its heading merge into that
current subject. The existing Cao–Păun statement and proof remain preferred;
both exact source variants and their permanent labels remain available.
R0302's local resolution and sharp estimate remain independent entries.

The complete real-exponent full-germ monomial criterion is already proved at
`F8F1C7EFDAD8`. R0316 therefore exports its additional explicit finite box of
generators and convention calculation as a corollary and remark using that
criterion. Its original research theorem and full proof are preserved in
Gerby-Literature. The rational integral-normalized envelope results remain
separate from flat-twist adjoint-envelope invariance; the exact Euler
polynomial remains separate from flat-twist Euler-characteristic invariance.

Six source history notes are incorporated into the existing project-wide
history sections on positivity, sections, singularities, envelopes and
cohomology.
Their original rendered HTML is hash guarded in
`reading/history/registry.json`. Major attribution appears in those connected
historical discussions; individual proof steps link to their internal inputs.

## Export contract

The source entry point is `contributions/analytic-methods-public.tex`. The
adapter reads `integrations/S0050/source-manifest.json`, which selects exactly
24 content files:

- the article and its bibliography;
- nineteen portable proof fragments under `contributions/analytic-methods/`;
- the section layout, canonical-reference map and project history under
  `integrations/S0050/`.

The manifest itself is the twenty-fifth control file. Selection acceptance,
per-packet review evidence, research-to-portable proof hashes, canonical-input
reviews, content hashes and complete label coverage are checked. A nested
input, changed file, unreviewed dependency link, escaping symlink or additional
packet fails before publication. The scans, source dossiers, audit records and
unselected proof attempts cannot enter through this adapter.

The manifest records exact research and portable hashes and describes every
transformation. Most fragments change only subject headings, complete-statement
section boundaries and position-independent reference wording. R0316 is the
explicitly narrowed canonical supplement described above. In R0322, the three
unchanged preliminary lemmas precede the unchanged main theorem, which is
placed immediately before its own unchanged proof. This binds the web proof
to the correct statement. The original research order remains archived.

The larger R0311, R0313, R0321 and R0322 packets have deliberate boundaries
between complete statements. Their proofs are not split. The source order is
independent of the shared chapter order.

Standalone pages retain exact native introductory conventions, including the
Bott–Chern quotient topologies, quadratic metric weights and the definition
of nef numerical dimension. The subject layout binds each copied prefix to
both its native and rendered hashes and lists its targets. Copies retain
links but remove equation identifiers and number owners. Whole original
sections already contain their introductions; only later reviewed subject
splits receive an extra contextual copy. Proof HTML, statement TeX, permanent
tags and formal kinds are unchanged by this reader-context operation.

## Building the selection

Use a real clean Git checkout at the source revision registered in
`books.json`, with `ANALYTIC_METHODS_SOURCE_DIR` pointing to that checkout.
The five older Gerby-Literature adapters can share a separate clean checkout
of their registered `main` revision. The build records actual Git commits;
a plain materialized directory cannot supply edition provenance.

The normal Python and Node test suites, complete build, link validation and
reader checks apply. The source-specific tests also exercise exact selection,
hash changes, input order, path containment and canonical dependency changes.
The local native article provides an additional check of the split proof
layout; it does not replace the rendered Pome checks or mathematical review.

Publication remains a separate explicit action. No formal proof mapping is
added by this integration.

## Reconstructed thirty-five-packet candidate — 23 October 2026

The preceding nineteen-packet description is the retained earlier scope.
This candidate additionally exports R0318–R0320 and R0323–R0335 from the
accepted source commit `392d68b7998206c324edb34a217dff98944e624c`.
The exact source manifest now contains 40 public content files and 166
canonical interfaces. Its 311 labels include two retained paragraph headings.
The adapter names those existing implicit labels explicitly and preserves
both permanent tags. Separate section contexts keep R0329's five modules
and their hypotheses apart; every native and rendered prefix hash remains
checked. Ten additional history passages join the existing subject history
with exact original-prose fingerprints. The source proof bytes are unchanged.

This is a new reconstruction from current Pome main and the retained
nineteen-packet patch, not a recovery of an unavailable local destination
commit. Fresh Python and JavaScript checks pass. The complete ordinary
build, desktop/mobile review, subsequent eight private proof packets and
whole-volume closure remain separate gates. Resolution, principalization
and the quoted Kähler elimination existence inputs retain their admitted
external status. No source merge, public publication or inclusion is claimed.
