# Exact annular charge and transport scale of a truncated projective-line pole

**Date:** 2026-11-11. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Finding:** POME-NPP-CP1-TRUNCATION-SHELL-W1-001. **Severity:** low. **Status:** verified conditional deduction. The original Example 13.7.6 and Theorem 13.7.5 are correct; this is an exact quantitative refinement and a sharp test of the mass hypothesis, not an error report.

## Pinned integrated reading edition and provenance

- Main file: docs/sections/non-pluripolar-products--capacity-convergence-and-loss-of-mass/index.html, blob d66813856cb813722806ab912afdfd4815d2da97.
- Example 13.7.6: source label foundations-of-pluripotential-theory:D5678E03, permanent tag ACAEA8D8BE87, physical lines 138–140; this is the main object actually inspected.
- Lemma 13.7.3: permanent tag 274B700496A8, lines 42–67; Theorem 13.7.5: tag 67C4F7EC316E, lines 107–134; Proposition 13.7.8: tag 4B60F7F33590, lines 148–171; Corollary 13.7.9: tag D73416504271, lines 176–200 and following. These are hypothesis/dependency checks, not a certification of all their arguments.
- Background: Example 10.6.7, permanent tag 4CE1D9D7D803 (Fubini–Study normalization), and Example 13.5.6, permanent tag 3D09B5B530AA (polar charge discarded by the non-pluripolar convention), as expressly referenced in Example 13.7.6.

Throughout use the printed normalization \(dd^c=(i/2\pi)\partial\bar\partial=\Delta/(4\pi)\,dA\) on a plane, and \(\omega_{\mathrm{FS}}=(1/\pi)(1+|z|^2)^{-2}dA\) on the affine chart of \(\mathbb P^1\), with \(\int_{\mathbb P^1}\omega_{\mathrm{FS}}=1\).

## Exact statement

For any real \(k>0\), let
\[
u(z)=\log |z|^2-\log(1+|z|^2),\quad
u_k=\max\{u,-k\},\quad
\varepsilon=e^{-k},\quad
r_k=(e^k-1)^{-1/2}.
\]
Put \(\mu_k=\omega_{\mathrm{FS}}+dd^cu_k\). Let \(\sigma_{r_k}\) be normalized Euclidean arc-length probability measure on the circle \(|z|=r_k\). Then **as measures on \(\mathbb P^1\)**,
\[
\boxed{\ \mu_k=\mathbf1_{\{|z|<r_k\}}\,\omega_{\mathrm{FS}}
       +(1-\varepsilon)\sigma_{r_k}.\ }
\tag{1}
\]
In particular the interior diffuse mass is exactly \(\varepsilon\), the circular singular mass is exactly \(1-\varepsilon\), there is **no atom at \(0\)**, and \(\mu_k\) is supported in the shrinking closed disk.

Let \(d_{\mathrm{ch}}\) denote the standard chordal distance on \(\mathbb P^1\), normalized by
\(d_{\mathrm{ch}}(z,0)=|z|/\sqrt{1+|z|^2}\).
Then
\[
\boxed{\ W_{1,d_{\mathrm{ch}}}(\mu_k,\delta_0)
 =\varepsilon^{1/2}-\tfrac13\varepsilon^{3/2}.\ }
\tag{2}
\]
This is the **exact best uniform Lipschitz-test bound**:
\[
\left|\int f\,d\mu_k-f(0)\right|
\leq \operatorname{Lip}_{d_{\mathrm{ch}}}(f)
       (\varepsilon^{1/2}-\varepsilon^{3/2}/3),
\]
with equality for \(f=d_{\mathrm{ch}}(\,\cdot\,,0)\). In contrast,
\[
\boxed{\ \|\mu_k-\delta_0\|_{\mathrm{TV}}=2
 \quad\text{and}\quad
 \|\mu_k-\langle\omega_{\mathrm{FS}}+dd^cu\rangle\|_{\mathrm{TV}}=1.\ }
\tag{3}
\]
Here total variation is the variation norm of a **signed** measure, not the half-normalized probabilistic TV distance. Thus weak convergence to \(\delta_0\), extended-capacity convergence of potentials, and convergence of the associated non-pluripolar masses are genuinely different assertions.

For the smooth global test \(f(z)=d_{\mathrm{ch}}(z,0)^2=|z|^2/(1+|z|^2)\), the exact moment is
\[
\boxed{\ \int f\,d\mu_k=\varepsilon-\tfrac12\varepsilon^2.\ }
\tag{4}
\]
The \(e^{-k/2}\) rate in (2) is sharp for all 1-Lipschitz tests, while this particular smooth test has order \(e^{-k}\). No global all-smooth-test asymptotic is asserted.

## Proof of the measure decomposition

The equation \(u=-k\) is equivalent to
\[
s(z):=\frac{|z|^2}{1+|z|^2}=\varepsilon,
\qquad |z|=r_k.
\]
On the interior disk, \(u_k=-k\), so \(\mu_k=\omega_{\mathrm{FS}}\). Outside the closed disk, \(u_k=u\); the printed \( \omega_{\mathrm{FS}}+dd^cu=\delta_0\) gives \(\mu_k=0\) there, since \(0\) is inside. At the interface, the outward radial derivative jumps from \(0\) to
\[
u'(r_k)=\frac{2}{r_k(1+r_k^2)}.
\]
The distributional radial Laplacian therefore contributes
\[
\frac{u'(r_k)}{4\pi}\,ds
=\frac{1}{1+r_k^2}\,\sigma_{r_k}
=(1-\varepsilon)\sigma_{r_k},
\]
where \(ds\) is Euclidean arc length. There are no further interface terms and no atom at the origin because \(u_k\) is constant in a neighborhood of it. Independently,
\(\int_{|z|<r_k}\omega_{\mathrm{FS}}=r_k^2/(1+r_k^2)=\varepsilon\),
so the total mass is \(1\), matching the printed bounded-potential mass theorem. This proves (1), including the possible boundary-charge issue.

For any measurable radial function \(F(s)\), the Fubini–Study radial coordinate \(s=|z|^2/(1+|z|^2)\) has density \(ds\) on \([0,1]\). Equation (1) consequently gives the exact one-dimensional identity
\[
\int_{\mathbb P^1}F(s)\,d\mu_k
=\int_0^\varepsilon F(s)\,ds+(1-\varepsilon)F(\varepsilon).
\tag{5}
\]
In particular, insert \(F(s)=\sqrt{s}\) to obtain (2) and \(F(s)=s\) to obtain (4). Since the other measure in the Wasserstein coupling is the point mass \(\delta_0\), the transport plan is unique and its cost is exactly the first moment of \(d_{\mathrm{ch}}(\cdot,0)\). Formula (1) also shows \(\mu_k(\{0\})=0\), hence \(\mu_k\perp\delta_0\), proving the first variation norm in (3). The original example identifies the limiting current \(\omega_{\mathrm{FS}}+dd^cu=[0]\) whose non-pluripolar product is zero; \(\|\mu_k-0\|_{\mathrm{TV}}=1\) proves the second identity.

## Quantified failure without conservation of non-pluripolar mass

Let \(\chi_k=\mathbf1_{\{|z|\leq r_k\}}\), a global Borel weight on \(\mathbb P^1\), and let \(\chi\equiv0\), which is continuous (hence quasi-continuous). Then \(\chi_k\to0\) **locally in capacity**: the support is a shrinking disk around a polar singleton. For an explicit local bound, if \(0\leq v\leq1\) is subharmonic on the fixed coordinate disk \(B_{1/2}\), denote its circular mean by \(m_v(r)\). Jensen's identity gives
\[
m_v(R_0)-m_v(R)=2\int_R^{R_0}
       (dd^cv)(B_t)\,\frac{dt}{t}
\geq2(dd^cv)(B_R)\log(R_0/R)
\]
for fixed \(R_0<1/2\) and \(R<R_0\). The left side is at most 1. Taking the supremum over the Bedford–Taylor capacity competitors and then slightly enlarging \(R\) for the closed disk gives
\(\operatorname{Cap}_{B_{1/2}}(\overline B_R)
=O(1/\log(1/R))=O(k^{-1})\)
at \(R=r_k\). Chart comparison (printed Lemma 13.7.1) transfers local convergence to the other projective charts, where the supports are eventually absent or contained in a fixed coordinate neighborhood.

Despite this capacity convergence, (1) gives
\[
\int\chi_k\,d\mu_k=1,\qquad
\int\chi\,d\langle\omega_{\mathrm{FS}}+dd^cu\rangle=0.
\tag{6}
\]
Thus the **mass-conservation assumption** of Corollary 13.7.9 cannot be deleted even when the limiting test weight is continuous and the varying bounded Borel weights converge to it in capacity. This is a different obstruction from the pre-existing finding POME-NPP-ROUGH-WEIGHT-CIRCLE-001, which concerns the necessity of *quasi-continuity of the limiting weight under conserved mass*. Formula (6) does **not** contradict the original corollary, since its mass hypothesis explicitly fails: \(1\nrightarrow0\).

## Classification, suggested change, and boundaries

**Classification:** low / verified conditional deduction; no erroneous printed theorem, no missing proof of Example 13.7.6, and no replacement of its permanent tag. The local distributions, explicit masses and transport identities are direct calculations. The interpretation of the limit as a non-pluripolar product and the capacity comparison use the printed definitions and named internal results, whose whole dependency chains are **not** separately certified here.

**Suggested optional mathematical-body patch, not applied:** add a concise remark after Example 13.7.6 giving (1) and its boundary shell mass, plus (2)–(3) to distinguish weak topology, transport, total variation and non-pluripolar mass; optionally include (6) as an exact warning for the mass condition in Corollary 13.7.9. Affected dependents: interpretation of Theorem 13.7.5 and Corollary 13.7.9, and any quantitative use of this projective-line truncation as a benchmark.

**Actual scope:** newly checked the exact charge distribution and sharp transport of Example 13.7.6, and only the listed mass/weight hypotheses in Theorem 13.7.5 and Corollary 13.7.9. Section 13.7 was already partially visited; **zero new first section visits, zero whole-section certifications**. Main remains at the SHA above; current ToC has 25 chapters and 747 numbered sections. No excluded Demailly approximation/regularization, dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas or positivity-loss programme was touched; every such prior audit item stays **deferred-by-user**, not resolved. No project build, CI, formal verification, publication, source or registry modification is claimed.
