# Restricted section divisors: simultaneous trace domination and saturation

Date: 2026-11-25. Reviewed main: `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Audit parent: `2a6b1f1384d182d2874d4d95d68d215df91e1e03`.

## POME-RESTRICTED-SECTION-SIMULTANEOUS-TRACE-SATURATION-001

Severity: low. Status: **verified conditional deduction**, not a false printed theorem, not a proof of the multiplier-ideal or approximation inputs.

### Anchors and premises

The integrated file `docs/sections/holomorphic-sections-and-hermitian-mass/index.html`, blob `5f00431e7986d899dc833c89175686b75f09371d`, §19.8.6, physical lines 150–213, Theorem 19.8.7 (permanent tag 165328A043C0; source tag 7C3569E2), proves pseudoeffectivity and the Gauduchon degree bound after subtraction of any finite set of divisorial trace coefficients. In particular lines 179–194 give the effective divisor subtraction and lines 197–205 take a normalized limit. Retain every hypothesis: compact connected complex manifold, connected compact submanifold Y of dimension r>=1, generic Lelong number of u along Y zero, V_m the image of the weighted section restriction, V_m nonzero in arbitrarily large degrees, fixed smooth compact modification pi:Z→Y, and Gauduchon form gamma on Z. Write B=pi*(beta|Y), D=integral B wedge gamma^(r-1), a_m=I(mu) O_Y and tau(E)=tau_{Y,u}(E).

The precise inputs are the limit assertion of Theorem 20.3.2, tag 7CD874C73EC9 / source BF417B5C, equation 20.3.3 tag 66AFB7F7397B, `docs/sections/restriction-and-intrinsic-trace-data/index.html`, blob dbc3b722ceacb8232fe4c7b711e5ad98b0708f06, lines 36–41, and normalized compactness Theorem 5.25.2, tag FC59B7D406A3 / source D9A05B95, `docs/sections/plurisubharmonic-functions-and-singularities--normalized-compactness/index.html`, blob d7ff8eafea43197c77de4bfd335bed0764ab4f69, lines 32–47. Poincare–Lelong and Gauduchon integration by parts are used exactly as in 19.8.7. No new proof of trace-limit input, multiplier-ideal subadditivity, or excluded regularization is claimed.

### Strengthening

On the fixed Z, the family of positive trace coefficients is at most countable. The series

    S = sum_{E prime on Z} tau(E)[E]

converges as a closed positive current, with total gamma-trace mass <= D. For *any* sequence m_j→infinity of admissible degrees and *any* choices of nonzero s_j in V_{m_j}, the normalized divisors

    T_j = [div(pi*s_j)]/m_j

have weakly convergent subsequences, and every weak cluster current T in the class [B] satisfies T >= S. In fact T-S is positive closed in [B]-[S], where [S] denotes the Bott–Chern class of the convergent current. If sum_E tau(E) integral_E gamma^(r-1) = D, then all T_j converge weakly to S, independently of choices. The convergence holds for nets of such divisors indexed by degrees tending to infinity, without any countable cofinality premise.

### Proof

For each T_j, Poincare–Lelong writes T_j=B+dd^c w_j with w_j quasi-PSH; subtract its supremum. A fixed smooth Hermitian form dominates B, so 5.25.2 gives subsequential L1 compactness and T_j→B+dd^c w weakly along a subsequence. Each T_j is closed positive with trace mass D by Gauduchon integration by parts; hence D>=0. This reasoning also gives that any weak limit of such currents is closed positive and has mass D. More explicitly the normalized potentials lie in a compact L1 family for the fixed dominating form, and the continuous distributional map w↦B+dd^c w has compact image. Thus no sequential compactness of a general inverse limit is assumed.

For any finite set F of distinct prime divisors on Z, divisibility of the restricted section by the pulled-back ideal gives

    T_j >= sum_{E in F} (ord_E a_{m_j}/m_j)[E].

Taking the limit against each smooth strongly positive test form gives T >= sum_F tau(E)[E]. Crucially the subsequence was chosen for T_j *before* choosing F; no diagonal extraction over an uncountable set of divisors is needed. This argument applies to a weak cluster net as well because every individual coefficient converges as its degree tends to infinity.

Set c_E=integral_E gamma^(r-1)>0. Pairing the finite inequalities with gamma^(r-1) gives sum_F tau(E)c_E <= D. For each integer k>=1 there are at most kD coefficients with tau(E)c_E>=1/k, and their union contains all positive coefficients. Enumerate that countable support (or use the finite partial sum net). Positivity bounds the absolute action of each summand on any smooth test form by a constant depending on the form and gamma times its trace mass; therefore the series converges absolutely as a current. Its distributional derivative is zero and its trace mass is the sum of the scalar masses. Pass the finite inequalities to this limit, obtaining T-S>=0. The residual is closed and has the stated class, using Bott–Chern cohomology of currents. The argument needs no Siu decomposition or regularization theorem.

If the degree bound saturates, T-S is positive with zero gamma-trace mass, so it vanishes. For every test form, failure of weak convergence along degrees tending to infinity would supply a sequence of arbitrarily large admissible degrees and choices violating a fixed test tolerance. Normalized L1 compactness would give a subsequence with cluster current S, contradicting that tolerance. Hence the convergence is uniform over choices in the weak neighborhood sense, which implies the claimed arbitrary-net statement. In particular in the saturated case S itself represents [B] (one convergent sequence suffices). Without saturation, uniqueness of cluster currents is not asserted.

### Proposed addition and affected dependents

Retain Theorem 19.8.7 verbatim; add a corollary following its proof on the fixed modification. This strengthens finite-subset degree obstructions to simultaneous trace domination and provides a criterion for canonical weak convergence of normalized section divisors. It does not assert a converse existence of sections or convergence of potentials in a stronger topology. The flat irrational elliptic-bundle counterexample at line 213 continues to rule out the converse. Related §20.3 trace data remain inputs, not newly certified; §19.9 bounded section algebra is a different construction. No global compatible pullback statement across all modifications is asserted.

## Actual coverage

- §19.8 selected nonexcluded complete subsections 19.8.4, 19.8.6, 19.8.8, lines 104–251 of the above blob. Degree sign, divisor positivity and torsion conclusion (connectedness supplied globally), finite subtraction, common Hermitian domination, irrational flat elliptic counterexample, the 3/5 integrability threshold (radial integral exponent 2k−2m(3/5)+1 > -1), and bounded weighted multiplication were checked. Earlier curve-count subsection not repeated; Bergman constructions and dedicated approximation/extension inputs not reopened. In particular no whole §19.8 claim.
- §9.32 Convexity and Stein spaces, entire mathematical lines 7–248, `docs/sections/separation-strict-exhaustions-and-coverings--convexity-and-stein-spaces/index.html`, blob 169e9d3bc872e9fd89d5135e69204e33fccd3783. Direct conditional check: embedding graph-lift Levi codimensions and positivity (9.32.2); flattened exhaustion and reciprocal sublevels (9.32.3); finite-intersection compactness and exceptional-set qualification (9.32.4); intrinsic powers and open quotient control (9.32.6, equation 9.32.7); compact hull annuli and controlled ambient square series (9.32.8); local strict patches with locally finite modification supports and convergent ambient series (9.32.10); full jet interpolation including nilpotents, ambient inverse function argument (9.32.11); implication cycle and finite products/intersections (9.32.12–13). The coherent topology, vanishing and neighborhood theorem inputs 9.51.5/13/14, 9.49.1/8 are assumed as printed, not transitive certifications. In particular the 9.51.13 vanishing proof is not re-audited or reopened.
- §5.21 introductory mathematical paragraphs 7–10, `docs/sections/plurisubharmonic-functions-and-singularities/index.html`, blob 1b0067104a17b95c283a89791721bb9b04edad39. Distinction between local corrections, singularity order and multiplier equivalence read; no mathematical proof or analytic-approximation certification.
- Selected dependency statements §§20.3.2 and 5.25.2 only, anchored above.

Totals: one whole conditional mathematical section, one whole introductory section, one selected principal section and two selected dependency statements; one new conditional deduction, zero newly confirmed printed errors, zero newly demonstrated proof gaps, zero complete transitive proof-chain certificates. Historical first visits are not asserted. Demailly approximation/regularization and dedicated Bergman, L2, OT, multiscale and positivity-loss programmes remain deferred-by-user, not resolved. No tests, builds, CI, source/registry/tag/site edits.
