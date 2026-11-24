# Point-supported distributions: finite jets and sharp mollifier scaling

Date: 2026-11-24. Reviewed production main: b6933b772f41b45918f7e25ed1afbbb1fd892272.

## Finding POME-DISTRIBUTION-POINT-JET-MOLLIFIER-SCALE-001

Severity: low. Status: verified deduction from the stated distribution definitions and local cutoff lemma (not a false printed theorem, not a new research-priority claim). This fills a useful elementary bridge between the Dirac example and distributional mollification; the exact scale also distinguishes all nonzero point-supported order-zero distributions from derivatives of atoms. No Demailly regularization is involved.

### Anchors and actual coverage

All paths below are under docs/sections/ and end in /index.html, on the immutable main above.

- measures-and-distributions--positive-linear-functionals, blob 0562702a346f7d8f09974afe97c90bc911bf7790, lines 7–126: entire mathematical section 2.3. Metric outer measure BAEFE6D3AE3C (source foundations-of-pluripotential-theory:D4F7DBE2, lines 21–58); Riesz 0C614771FB98 (DE073A6A, lines 66–114); density 0BB807E5CBD4 (D365C9D4, lines 119–126).
- measures-and-distributions--test-functions-and-distributions, blob beb63e37cdc88e099c3e9a8314fca1219d18c0c4, lines 7–47: entire section 2.4. Definition 2.4.1, source foundations-of-pluripotential-theory:55085BC2, permanent 55085BC2, lines 26–31; support and derivative definitions lines 34–43; Example 2.4.2, source CB904650, permanent E2DD6B809EB8, line 47.
- measures-and-distributions--convolution-and-mollifiers, blob 50e1ba12fd379718b6be25a0b797e8014e1eaede, lines 7–204: entire section 2.5. Lemma 2.5.1 source E72A5743 / permanent 3C40E6BD1222 (cutoff clause 4, lines 50,86); Lemma 2.5.2 source 0682246E / permanent 677586F8712C (lines 97–110); Proposition 2.5.3 source D09EB34D / permanent 0CB24AD25DC3 (lines 127–166), especially kernel definition 117–123, derivative identity 130 and weak pairing 152–162; Corollary 2.5.5 lines 171–184; positive distributions Theorem 2.5.6 source 2B9CB0FB / permanent 6A928E70A605, lines 189–204. Source book throughout this section: foundations-of-pluripotential-theory.
- differential-operators-and-elliptic-regularity--maximal-domains-and-formal-adjoints, blob 63b73681ef8b511fff1308685388f027ead75a77, lines 7–57: entire section 2.17. Example 2.17.1 source 30DA9A92 / permanent 07CC926D8338, lines 11–28; Proposition 2.17.2 source demailly-complex-geometry:66782E9F / permanent 5AFFEC4D76E3, lines 32–57. This is ordinary differential operator calculus, not the excluded approximation programme.
- Section 2.6 (blob 45720b2399a645a1a9a8148873fdc01c634fc5d7, lines 7–102) read again for the downstream topology boundary; previously recorded signed-net/tightness results are not counted as new.

### Claim

Let Omega be open in R^d, a in Omega, and T a nonzero complex distribution supported in {a}. Let m be its actual local order on a fixed closed ball centered at a and contained in Omega (the least integer for the estimate of Definition 2.4.1). There are unique coefficients c_alpha with

    T = sum_{|alpha|<=m} c_alpha partial^alpha delta_a,

and some coefficient of degree m is nonzero. For the fixed normalized smooth kernel rho of section 2.5 and its dilates rho_e, put

    Q_j(y) = sum_{|alpha|=j} c_alpha partial^alpha rho(y).

Then for each 1<=p<=infinity (1/infinity=0), and sufficiently small e,

    e^{d+m-d/p} ||T*rho_e||_{L^p(Omega_e)}
       --> ||Q_m||_{L^p(R^d)} > 0.

The norm is over the interior domain Omega_e in the printed definition. No integration of an undefined extension through the boundary is needed. In particular, the local order can be read off from the exact rate of divergence of the L^1 norm; order zero is equivalent to bounded L^1 norm for these point-supported distributions. This last equivalence is restricted to the point-supported setting in this note.

### Proof

Choose a smooth cutoff eta identically one near zero with compact support in the unit ball, using Lemma 2.5.1(4), and put eta_e(x)=eta((x-a)/e). The support property and Lemma 2.5.2 imply T(phi)=T(eta_e phi) for each test phi: their difference vanishes on a neighborhood of a and is supported in the open complement of {a}. Choose a fixed closed ball K with a in its interior, on which the order-m estimate holds. For small e, eta_e phi is supported in K.

Suppose the derivatives partial^alpha phi(a) vanish for |alpha|<=m. Taylor's formula gives

    sup_{|x-a|<=e} |partial^beta phi(x)| = o(e^{m-|beta|})

for each |beta|<=m, including |beta|=m by continuity. Leibniz's formula and the scaling of derivatives of eta give, for |gamma|<=m,

    sup |partial^gamma(eta_e phi)| = o(e^{m-|gamma|}).

This is o(1) in the order-m seminorm; therefore T(phi)=0. Thus T factors through the finite vector space of m-jets at a. The jet map is surjective: a monomial (x-a)^alpha/alpha! multiplied by a cutoff identically one near a has exactly the corresponding coordinate jet. Setting c_alpha=(-1)^|alpha| times the value of T on this test gives the displayed representation, with uniqueness by the same tests. If every top coefficient vanished, the representation would give the order-(m-1) estimate, contradicting minimality (for m=0, vanishing would mean T=0). Conversely the representation provides the same order estimate on every compact neighborhood. Thus the actual order is independent of the chosen ball.

By the sign convention of Definition 2.4.1 and the kernel in Proposition 2.5.3,

    (partial^alpha delta_a)*rho_e(x) = partial^alpha rho_e(x-a).

The distributional derivative sign cancels the sign from differentiating rho_e(x-y) in y. Consequently

    e^{d+m}(T*rho_e)(a+ey)
      = Q_m(y) + sum_{j<m} e^{m-j} Q_j(y).

All Q_j are smooth and supported in the closed unit ball. The entire right-hand support corresponds to a subset of Omega_e for 2e<dist(a,R^d\Omega). For a top index beta with c_beta != 0, integration by parts gives

    integral y^beta Q_m(y) dy = (-1)^m beta! c_beta != 0,

because among the multiindices of degree m only beta can differentiate y^beta nontrivially and integral rho=1. Thus Q_m is nonzero, with no Fourier or elliptic input. The finite sum converges in all the asserted L^p norms, including the supremum norm. Changing variables gives the claimed limit. The same calculation even yields an O(e) error for the scaled norm (zero error if there are no lower-order terms). This proves sharpness of the exponent for every nonzero point-supported distribution. For m=0 the distribution is a scalar atom and the L^1 norm equals |c_0|; for m>=1 it diverges like a positive constant times e^{-m}.

### Other checks and correction proposal

- Section 2.3: the alternating-parity layer argument for metric outer measures controls the full tail by two finite sums, without countable additivity of an outer measure. Riesz construction uses finite compact-cover partitions before taking suprema; the two level-set bounds differ by O(delta) on a fixed finite-mass support. Density reduces to regular approximations of indicators. No new error identified; the underlying measure integration/cutoff inputs are not transitively certified here.
- Section 2.4: the seminorm topology, bilinear (not sesquilinear) pairing and distributional derivative sign are consistent. The printed Dirac-prime example is correct. Proposed addition after Proposition 2.5.3: insert the point-support statement and proof above, or cross-reference an equivalent internal statement if subsequently located. The finding is a supplementary deduction, not a claim that every source version lacks the classical structure theorem.
- Section 2.5: the fixed compact support in the Riemann-sum argument justifies taking the distribution pairing inside the kernel integral. The evenness of rho is used in the displayed pairing. The decomposition consequence of Lemma 2.5.2 chooses K=Supp chi anew for each chi (as its proof explicitly does); for clarity the statement could say "apply this construction to K=Supp chi" rather than suggest a single fixed family works for all chi. This is a quantifier clarification, not a refutation of the intended lemma. No new unresolved mathematical proof gap.
- Section 2.17: testing the maximal interval derivative first on compact tests and then on affine functions forces the two independent endpoint values of its adjoint domain. Formal adjoint and maximal Hilbert adjoint are kept distinct; the symbol sign (-1)^d agrees with the no-i convention. No new printed error identified.
- Section 2.6: repeat only; the earlier positive/signed measure-net distinction remains intact. No previously reported deduction counted anew.

Affected dependents: the new bridge concerns 2.4.1–2.4.2 and 2.5.3; it provides an explicit model for why distributional convergence of smooth densities alone does not control variation (the mollified derivative of an atom has the divergent norm computed here). No production theorem needs a change of hypotheses. No transitive dependency certification or global duplicate clearance is claimed.

## Status and scope

Four whole current mathematical sections directly read on legacy-unreconciled rows, one complete repeat. Historical first visits not asserted. One verified deduction, zero newly confirmed printed errors, zero unresolved local gaps, zero full transitive certificates. Actual rendered ToC and existing section matrix checked: 747 section locators, no missing or duplicate rows. The Demailly approximation/regularization and dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale and positivity-loss programmes remain deferred-by-user, not resolved or certified. No builds, software tests, CI, main, registry, permanent tag or site changes.
