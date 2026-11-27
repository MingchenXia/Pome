# Rank-stratified section growth and one-function projective models

Date: 2026-11-28. Production main reviewed: b6933b772f41b45918f7e25ed1afbbb1fd892272.
Starting audit head: e06873b35d11aa8f9b6beff88014538bc02ce0bd.
The current AGENTS.md and documentation/proof-expansions.md and the audit LATEST.md, README.md, LEDGER.md and SECTION_MATRIX.md were read. The integrated docs/index.html table of contents contains 747 distinct section identifiers; their set agrees exactly with the 747 matrix rows.

## POME-SECTION-RANK-GROWTH-ALL-EFFECTIVE-DEGREES-001

Low / verified conditional deduction; not a printed error.

Integrated file `docs/sections/section-growth-and-kahler-modifications/index.html`,
blob bcaa3d33d9f662c141be1c4ed23153ae854d6e1c.
Lemma 9.66.1 (permanent ABF5E7654F82; source 40E41E76), lines 8–37,
especially the rank-stratified jet estimate at lines 18–34.
Theorem 9.66.2 (DC74B9CCEB47; source 9D28EC5D), lines 42–55.

Retain the compact connected complex n-manifold and holomorphic line bundle L.
Let V_k=H^0(X,L^k), set V_0=C, and S={k>=0: V_k is nonzero}.
If S contains no positive degree, there is nothing to prove.
Otherwise let d=max{rank(Phi_k): k>0, k in S}, where the rank is
the maximum differential rank off the base locus, as in the printed lemma.
Then there exist positive constants c,C and an integer K such that for
every k in S with k>=K,

    rank(Phi_k)=d,
    c k^d <= dim V_k <= C k^d.

For k outside S the dimension is zero. In particular the growth exponent
on effective degrees is exactly d, and the limsup exponent on all
positive degrees is also d. This does not assert existence of a limit of
k^(-d) dim V_k or nonvanishing in every degree.

Proof. The printed finite-cover Schwarz estimate with p_k<=C_0(k+1)
and the constant-rank factorization show, for every effective k,

    dim V_k <= N binom(p_k+d_k-1,d_k) <= C_1 (k+1)^d.

The constants are uniform because the coordinate balls and metric are
fixed; the choice of rank-d_k point in each ball is immaterial to the
Schwarz estimate. These are exactly lines 18–34. The estimate for d=0
is interpreted as binom(p_k-1,0)=1.

Choose a positive effective degree a realizing d. Pick s_0,...,s_d in V_a
so that s_0 is nonzero at a maximal-rank point and the d ratios
s_i/s_0 have independent differentials there. Their local image contains
an open set of C^d, by the holomorphic rank theorem. Hence every
nonzero polynomial in these ratios is a nonzero meromorphic function.

S is additive: on a connected complex manifold, two nonzero holomorphic
sections have a nonzero product (their nonvanishing open sets intersect).
For each residue r modulo a occurring in S, let b_r be its least element
in S and fix a nonzero t_r in V_(b_r), using t_0=1 when b_0=0.
Every k in S of residue r is uniquely b_r+qa for q>=0.
The finitely many b_r are fixed. The following sections of L^k are
linearly independent, for all multi-indices alpha in N^d with |alpha|<=q:

    t_r s_0^(q-|alpha|) s_1^alpha_1 ... s_d^alpha_d.

Indeed divide any linear relation on the common nonvanishing open set
by t_r s_0^q. The resulting polynomial relation among the ratios
extends meromorphically, and the open image forces all coefficients
to vanish. Thus dim V_k >= binom(q+d,d). For k sufficiently large
among effective degrees, q>=k/(2a), giving the stated uniform lower
bound; the d=0 lower bound is 1.

For q>=1 the ratios of the sections t_r s_0^q and
t_r s_0^(q-1)s_i equal s_i/s_0. Their common nonvanishing locus meets
the maximal-rank locus of the selected ratios, by connectedness
and the identity principle. The complete system Phi_k therefore has
rank at least d there, and by definition it has maximum rank at most d.
This proves eventual equality on all effective degrees, with no
finite-generation assumption on the graded section ring.

A useful further elementary consequence: the residues of S form an
additive submonoid of the finite cyclic group Z/aZ, hence a subgroup
(the negative of an element is a nonnegative multiple of it).
Each occurring residue contains every integer b_r+qa. Thus the positive
effective degrees are, beyond a finite threshold, exactly the multiples
of gcd(S), even without finite generation of the section algebra.

Optional addition after Lemma 9.66.1. No source correction required.
The printed maximal-rank conclusion follows when d=n. The downstream
Theorem 9.66.2 retains its original analytic section-growth input
19.10.1 and external elimination input 9.65.8; neither is proved here.
The former analytic asymptotic input is not reopened as part of this audit.

## POME-PROJECTIVE-MODEL-SINGLE-SEPARATING-FUNCTION-001

Low / verified conditional deduction; not a printed error.

Integrated file `docs/sections/projective-models-and-kahler-modifications/index.html`,
blob 93218ce36b6e7b33cbe899e60ecff632a8c09964.
Lemma 9.65.2 (5174706A0D80; E6B9E346), lines 23–40;
Lemma 9.65.3 (4F31DD82134A; 604640B3), statement line 45 only;
Theorem 9.65.5 (B6FE85A67BE1; BF5E34E4), lines 104–121.

Conditional on the existing sheet-separating functions in Lemma 9.65.3,
the target in the proof of Theorem 9.65.5 can be reduced from
P^n x (P^1)^e to P^n x P^1, regardless of the covering degree e.

Indeed, with the notation of 9.65.3, choose pairwise distinct complex
numbers lambda_1,...,lambda_e and set g=sum_i lambda_i g_i.
Then g is globally meromorphic, holomorphic over U, and
g(x_j)=lambda_j. On a sufficiently small ball around the chosen b,
each local sheet is a graph of the corresponding holomorphic branch
of g and their values remain pairwise distinct (finitely many pairs).
The denominator-ideal principalization at line 118 for this single
meromorphic function gives a smooth modification on which (f,g) is
holomorphic. Its centers are away from the inverse image of U:
there g is holomorphic, so both the denominator ideal and the product
ideal in that proof are unit ideals. Thus no new points appear over
the chosen ball. The graph argument at line 120 shows the map has
degree one onto its irreducible analytic image. Remmert and the Segre
embedding plus the algebraicity assertion in 9.65.1 make this image
projective; the same generic-sheet argument as in the printed proof
makes the map bimeromorphic. This is conditional on the same existing
geometric inputs, not a substitute for the excluded weighted estimate.

Optional proof simplification, not a correction. Theorem 9.65.9 and
Theorem 9.66.2 may use the resulting projective model without changing
their hypotheses. No claim that the projective model is smooth or that
the external elimination theorem follows from this construction.

## Direct review scope and dependencies

- §9.66: entire mathematical text, lines 8–55. Checked the radii R/2
  and 3R/4, the metric factor exp(Ak), the choice p_k linear in k,
  the finite jet injection, maximal-rank density and common nonzero
  denominator, the rank-zero endpoint, and the positive curvature
  integral deduction (conditional on the cited asymptotic theorem).
- §9.65 selected lines 7–45 and 104–166. Checked the cone/Noetherian
  argument (9.65.1, 24EDDE45E392 / 90AE6AF0), finite unbranched
  covering and Chern curvature signs (9.65.2), projective projection
  and fractional denominator ideal products, the blowup curvature
  positivity argument (9.65.6, F5A67B2A1F82 / 66071A4B), strict
  transform of a reduced irreducible analytic subspace
  (9.65.7, 107F4EEFA84C / AC13E619), and the final composition
  (9.65.9, 1D3242230662 / E2B6E348).
- Lemma 9.65.3's weighted L2 proof (lines 50–99) is not reviewed:
  the dedicated weighted/regularization programme is deferred-by-user.
  No claim of independent verification of its existence premise.
- 9.65.8 (9CA80A318258 / 6C9DB22E, lines 153–154) is explicitly
  quoted external elimination, distinct from the stated Hironaka
  resolution and principalization inputs; remains open as an external
  dependency of 9.65.9 and 9.66.2. Remmert–Stein, proper-image,
  dimension, Noetherianity and coherence are internal dependencies,
  not transitive certificates here.
- No newly confirmed printed errors, demonstrated gaps, or full
  upstream-chain certifications. Previous historical coverage remains
  unreconciled; no historical first-visit assertion. No tests, build,
  CI, publication, main, source, registry or permanent-tag changes.
