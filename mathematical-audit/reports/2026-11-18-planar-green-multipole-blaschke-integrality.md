# 2026-11-18 — Planar multipole Green functions, finite Blaschke maps and integral pole weights

**Finding ID:** POME-PLANAR-MULTIPOLE-BLASCHKE-INTEGRALITY-001  
**Classification:** low / **verified conditional deduction**, not a false printed theorem or a repaired proof gap.  
**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Integrated reading-edition source:** `docs/sections/planar-green-functions-and-conformal-maps/index.html`, blob `bfee348bb5f4bbfaa4515e5c9333789a13dae861`.

## Exact anchors and scope

- §3.8 introductory normalization, main HTML line 7: positive Green kernel has singularity \(-\log|z-a|\), so \(-\Delta G_D(\cdot,a)=2\pi\delta_a\).
- Theorem 3.8.1, source `klimek-pluripotential-theory:B1C110E2`, permanent tag `E2B11E803D94`, HTML lines 11–13, proof lines 19–48. Especially the harmonic conjugate and map construction (26–32), proper-degree argument (34–40) and reduction to bounded domains (42–48).
- Proposition 3.8.2, source `klimek-pluripotential-theory:886FBC1A`, permanent `3F05222ECC9E`, lines 54–69, and Example 3.8.3, source `klimek-pluripotential-theory:02455EF4`, permanent `FADCC209A003`, lines 74–83, were read **only for boundary-value conventions**. The unbounded-component equilibrium and polar-boundary arguments were *not* certified here.
- Section permanent tag `7528EC445E3A`. No inference from source theorem numbering was used.

## Precise new conditional theorem

Let \(D\Subset\mathbb C\) be a bounded simply connected domain, \(a_1,\ldots,a_s\) distinct points of \(D\), and \(t_1,\ldots,t_s>0\). Define on \(D\setminus\{a_j\}\)
\[
U(z)=\sum_{j=1}^s t_j G_D(z,a_j),
\]
where \(G_D\) is the positive Green function with logarithmic coefficient \(1\) in Theorem 3.8.1.

Then the following are equivalent:

1. There is a nonzero holomorphic function \(B:D\to\mathbb D\) such that \(-\log|B|=U\) on \(D\setminus\{a_j\}\).
2. Every coefficient \(t_j\) is a strictly positive integer.

When these conditions hold, \(B\) is **proper** of degree \(N=\sum_j t_j\), is unique up to multiplication by a constant of modulus one, and is an explicit finite Blaschke product in any Riemann map \(f:D\to\mathbb D\):
\[
 B(z)=e^{\mathrm i\vartheta}
 \prod_{j=1}^s
 \left(\frac{f(z)-f(a_j)}{1-\overline{f(a_j)}f(z)}\right)^{t_j}.
 \tag{1}
\]
Conversely, **every** proper holomorphic map \(B:D\to\mathbb D\) is of this form, with its \(a_j\) the distinct zeros and its \(t_j\) their zero multiplicities. In particular,
\[
-\Delta U=2\pi\sum_{j=1}^s t_j\delta_{a_j}
\tag{2}
\]
in distributions, with the normalization of printed line 7; a prescribed *nonintegral* point mass cannot be the logarithmic divisor of a single-valued holomorphic disc map.

## Proof

By Theorem 3.8.1, choose a biholomorphism \(f:D\to\mathbb D\). For \(\alpha=f(a)\), the automorphism \(\phi_\alpha(w)=(w-\alpha)/(1-\bar\alpha w)\) maps \(\alpha\) to zero. The function
\(-\log|\phi_\alpha(f(z))|\) is positive harmonic on \(D\setminus\{a\}\), has the exact coefficient \(-\log|z-a|+O(1)\) at \(a\), and tends to zero at every boundary point. The same uniqueness argument behind Theorem 3.8.1, or applying its Green identity after composing \(f\) with \(\phi_\alpha\), gives
\[
G_D(z,a)=-\log|\phi_{f(a)}(f(z))|.
\tag{3}
\]
For positive integral weights the product (1) is holomorphic, maps into the unit disc and, by (3), has the required modulus. Its zeros are exactly the \(a_j\) with respective orders \(t_j\). Since \(|f(z)|\to1\) as \(z\) leaves every compact subset of \(D\), each finite Blaschke factor has modulus tending to \(1\); hence \(B\) is proper. The proper-degree argument in printed lines 34–40 identifies its degree as the multiplicity of its fiber over \(0\), namely \(N\).

Conversely suppose the modulus equation holds for some nonzero holomorphic \(B\). Fix \(j\), take a disc about \(a_j\) containing no other prescribed pole, and write
\[
U(z)=-t_j\log|z-a_j|+h_j(z),
\]
with \(h_j\) harmonic near \(a_j\). Thus
\[
\log|B(z)|=t_j\log|z-a_j|-h_j(z).
\]
The right-hand side tends to \(-\infty\), so \(B(a_j)=0\). Local holomorphic factorization gives
\(B(z)=(z-a_j)^{m_j}b_j(z)\), \(m_j\in\mathbb N\), \(b_j(a_j)\ne0\). Comparing the coefficients of \(\log|z-a_j|\) forces **\(t_j=m_j\)**. This also proves (2) with the exact \(2\pi\) sign and factor. No regularization or interchange of limits is involved.

If \(B_1,B_2\) have the same prescribed modulus, they have the same zeros with the same multiplicities. Hence \(B_1/B_2\) extends holomorphically, nonvanishingly across all \(a_j\), and has constant modulus \(1\); the open mapping theorem makes it a constant unimodular factor.

Finally let \(B:D\to\mathbb D\) be any proper holomorphic map. Properness and the open mapping theorem imply surjectivity. The compact discrete zero fiber is finite; list its distinct zeros \(a_j\) with multiplicities \(m_j\). Construct the product \(P\) in (1) using these \(m_j\). The quotient \(Q=B/P\) extends holomorphically and nonvanishingly across the zeros. For every sequence leaving all compact subsets of \(D\), properness gives \(|B|\to1\) and properness of \(f\) gives \(|P|\to1\); thus \(\log|Q|\to0\) at the entire boundary. This harmonic function is bounded on \(D\), since it is bounded near the boundary and is continuous on the remaining compact set. The maximum principle applied to \(\pm\log|Q|\) on an exhaustion gives \(\log|Q|\equiv0\), hence \(Q=e^{\mathrm i\vartheta}\). This gives the converse classification.

## Sharp diagnostic and relationship to the printed material

For \(D=\mathbb D\), one pole at \(0\), and weight \(t=2\), \(U(z)=-2\log|z|\) comes from \(B(z)=z^2\), a proper degree-two map. For \(t=1/2\), the candidate modulus \(|B(z)|=|z|^{1/2}\) cannot arise from a single-valued holomorphic function, since zero multiplicities are integral. This is a local, exact obstruction, not a mere failure of the chosen formula.

Theorem 3.8.1 is **not refuted**: its simple Green pole has coefficient one, precisely the degree-one case above. Example 3.8.3 discusses positive harmonic additions with exceptional boundary behavior, not exact finite Green sums, so it is neither a duplicate nor a counterexample. No global analytic continuation across arbitrary multiply connected domains is asserted; there periods give additional obstructions. No finite Blaschke theorem is assumed externally—the product, properness and classification are derived using the integrated Riemann map and elementary local holomorphic factorization.

**Suggested source/body change (proposal only):** after Theorem 3.8.1, add an optional corollary on finite Green sums and integrality/degree. Preserve attribution, source tags and existing permanent tags; no production files are changed in this audit.

**Dependencies:** the integrated bounded-domain Riemann mapping/Green representation Theorem 3.8.1 (its planar-continuum boundary regularity and Dirichlet/Green existence inputs remain conditional as upstream results), the argument principle/holomorphic local factorization, and the elementary harmonic maximum principle. This report does not certify the upstream chain. Possible dependent applications: finite proper disc coverings and multi-pole Green representations; no existing printed statement was identified as invalid.

## Actual coverage and exclusions

New direct proof-level deduction at **§3.8.1** (lines 7, 11–13, 19–48); §§3.8.2–3 context only. §3.8 was **already partially visited**: **0 first-reviewed numbered sections**, **0 fully certified sections**, total current table of contents **25 chapters / 747 numbered sections** (unchanged). This is not a whole-section or formal proof certificate. No build, tests, CI, publishing, source/registry/tag/canonicalization writes. All Demailly approximation/regularization, Bergman, dedicated \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof completion remain **deferred-by-user**, neither resolved nor revisited.
