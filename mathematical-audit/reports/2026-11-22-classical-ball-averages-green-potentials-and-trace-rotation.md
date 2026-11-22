# Classical harmonic analysis, Green kernels and selected trace functoriality: present-main mathematical audit

**Date:** 2026-11-22. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Scope:** entire current integrated §§3.3 and 3.5, and carefully delimited §20.2 items 20.2.4, 20.2.21–27. This audit neither reopens nor certifies Demailly regularization, Bergman/L²/OT, multiscale atlas or positivity-loss proof-completion.

## Direct source anchors and coverage

| Reading edition, source and permanent references | Main Git blob | Physical lines and scope |
| --- | --- | --- |
| docs/sections/classical-harmonic-analysis/index.html; source classical-potential-theory:3425B8A6; Theorem 3.3.4, permanent F549D908E93A; equation 3.3.5, source 4E47B4BE, permanent 6CEBA4319BDE | 75e982788e627af602981823a82863cbd36ee712 | Entire mathematical content lines 10–239. Specifically spherical-average differentiation 41–78, compact signed-measure selection 82–115, radial and nontangential limits 120–211, Bôcher and spherical reflection 218–239. |
| docs/sections/green-functions-and-potentials/index.html; source classical-potential-theory:C3FD3CE0 / permanent 2791D284428C (3.5.3), source 772DDE67 / permanent F3C6870EA9A8 (3.5.5), source 1CC53DC8 / permanent 977ECF0867E0 (3.5.8), source 20EFF2F0 / permanent 27ABF8BDD497 (3.5.14) | 63c74d1c4a0958633b42903a0e3a4526f42b7588 | Entire mathematical content lines 7–205. Lowerings/minorants, planar and higher-dimensional Greenian existence, exhaustion/symmetry, potentials/Riesz decomposition, pointwise continuity, generalized Laplacian and global extension. |
| docs/sections/the-trace-operator/index.html; source sgpt:8FF85CC2 / permanent 82453E358B30 (20.2.4); source sgpt:762F23ED / permanent 58627BFD2457 (20.2.22); source sgpt:FCC832C0 / permanent DDEF49346283 (20.2.24); source sgpt:B56231C4 / permanent DB90B2D3ADEB (20.2.26) | 1f3a3e4f0317a308b43bd3df53dda84c5f3fa50a | Targeted lines 105–220, 352–440, 445–543, 565–635; NOT a whole-section audit and NOT an audit of Theorem 20.2.28 (extension) or the rest of §§20.2.29 onward. |

## POME-CLASSICAL-BALL-AVERAGE-SHARP-GRADIENT-001

**Classification:** low / **verified conditional deduction** from the checked integrated differentiation identity (3.3.5). **Not a false original theorem**, not a repaired upstream dependency, and not evidence of a certified complete proof chain.

**Hypotheses and result.** Let \(d\ge2\), \(\Omega\subset\mathbb R^d\) be open, \(r>0\), \(x\in\Omega_r\), and \(f\) be real-valued and continuous on a neighborhood of \(\overline{B(x,r)}\). Put
\[
A_rf(x)=\frac1{v_dr^d}\int_{B(x,r)}f(y)\,dy,\qquad
\operatorname{osc}_{\partial B(x,r)}f=
\max_{\partial B(x,r)}f-\min_{\partial B(x,r)}f,
\]
where \(v_j\) denotes the \(j\)-dimensional unit ball volume. Then the **dimensionally sharp** pointwise estimate is
\[
\boxed{\quad
|\nabla A_rf(x)|\le
\frac{v_{d-1}}{v_d\,r}
\operatorname{osc}_{\partial B(x,r)}f .
\quad}
\]
The constant is the best possible even among smooth functions \(0<f<1\) on all of \(\mathbb R^d\). For \(d=2\), the optimal coefficient is \(2/(\pi r)\); for \(d=3\), it is \(3/(4r)\). The formulation controls **the averaged function**, not the pointwise gradient of \(f\), and imposes no global convexity assumption on \(\Omega_r\).

**Complete independent proof of the sharpening.** By the audited (3.3.5), for each unit vector \(e\),
\[
D_eA_rf(x)=\frac1{v_dr}\int_{S^{d-1}}f(x+r\theta)(e\cdot\theta)\,dS(\theta).
\]
Write \(m,M\) for the boundary minimum and maximum. Since \(\int_{S^{d-1}}(e\cdot\theta)dS=0\), subtract the constant \((M+m)/2\) in the integrand. Its absolute value is at most \((M-m)/2\). Projection of each open hemisphere onto the unit ball in \(e^\perp\) gives
\[
\int_{S^{d-1}}|e\cdot\theta|\,dS(\theta)=2v_{d-1}.
\]
It follows that \(|D_eA_rf(x)|\le v_{d-1}(M-m)/(v_dr)\), uniformly in the unit direction. Take the supremum over \(e\).

For sharpness fix \(x=0\), \(e=e_1\) and let
\[
 f_\varepsilon(z)=\tfrac12\bigl(1+\tanh(z_1/\varepsilon)\bigr).
\]
These are smooth, take values strictly between zero and one, and their boundary oscillations tend to one. The same exact boundary integral and dominated convergence give
\[
D_{e_1}A_rf_\varepsilon(0)
=\frac1{2v_dr}\int_{S^{d-1}}
\tanh(r\theta_1/\varepsilon)\,\theta_1\,dS
\longrightarrow\frac{v_{d-1}}{v_dr}.
\]
Thus no smaller constant works. No sequential compactness, approximation theorem, or numerical test is needed.

**Proposed disposition:** optional standalone corollary adjacent to Theorem 3.3.4; audit-only, **no main/source/canonicalization change**. The result is compatible with Theorems 3.3.9–14 (Poisson boundary limits). No source theorem, provenance, permanent tag or distinct variant should be merged or modified because of this sharpening. It is not a claim about arbitrary bounded measurable boundary values without choosing a suitable almost-everywhere derivative interpretation.

## Entire §3.3 proof checks, with no new printed error

- **3.3.2–5 (lines 10–78):** compact-parameter differentiation needs joint continuity of the integrand, not just its \(x\)-derivatives. The repaired factor \(1/(v_dr)\) in (3.3.5) agrees with the sphere area scaling and yields derivative one on \(f(z)=z_i\). This correction already exists in main: **not re-registered as a new issue**.
- **3.3.7 (86–110):** diagonal extraction uses a countable dense family of \(C(X)\), then the \(2M\) bound extends the limit to every continuous test. Compact *metric* is material; this does not assert sequential compactness of an arbitrary weak-* dual ball.
- **3.3.9/11/12/14 (120–211):** the cap-density hypothesis, bounded signed Fubini, fine-covering disjoint selection, local cube differentiation, singular measure null-density and nontangential annular estimate are distinct stages. The aperture-independent full-measure set is supported by density conditions independent of the aperture; no interchange of boundary/tangential limits is assumed. The fine-cover proof uses the separation of each newly chosen set's diameter-neighborhood from the earlier finite union; without this property its compactness contradiction would not follow.
- **3.3.16–17 (218–239):** the Bôcher coefficient has the correct \(c_d=(d-2)s_{d-1}\) in dimension \(d\ge3\) and \(2\pi\) in \(d=2\); harmonic reflection reduces to planar odd reflection under inversion, and the possible inversion-center singularity is removed by the one-sided bound plus the interior zero limit. The local Riesz decomposition and compact sphere reflection premises are not re-proved transitively here.

## Entire §3.5 proof checks, with no new printed error

- **3.5.2–3 (11–30):** finite harmonic lowerings are monotone, a ball repeated cofinally yields a decreasing harmonic subsequence, and a harmonic lower bound excludes the \(-\infty\) alternative. The greatest-minorant operation is additive only in the stated finite/harmonic-minorant regime; no claim of boundary superharmonicity of the unregularized limit is introduced.
- **3.5.5–6 (39–82):** domain monotonicity and the factor \(c\ge1\) of the minimal pole are consistent with \(\Phi=\log(1/r)\) in dimension two and \(\Phi=r^{2-d}\) otherwise. The proof that \(c=1\) divides the nonnegative infimum by \(c\), and componentwise Green kernels vanish across components. Symmetry depends on the greatest-minorant construction and Harnack, rather than title-level canonicalization.
- **3.5.8–9 (91–134):** check \(-\Delta G_\Omega(\cdot,y)=c_d\delta_y\) and the sign of the distributional Fubini identity. The \(\mu\)-potential identity is first established under local integrability; Tonelli is reserved for nonnegative kernels. The global Riesz decomposition assumes a **nonnegative** superharmonic function, while the local decomposition on \(W\Subset\Omega\) uses the lower bound on \(\overline W\); do not silently erase this distinction.
- **3.5.11–12 (140–171):** at finite potential points, the local singular contribution is controlled by the nearest-point comparison. For \(d\ge3\), the radial layer-cake estimate is exactly \(\tfrac12s_{d-1}R^2\), \(R=(|E|/v_d)^{1/d}\); it bounds small-volume tails uniformly in the pole. The stated planar boundedness and connectedness qualifications are retained.
- **3.5.14–16 (176–205):** the sphere mean of the fundamental kernel and the factor \(2d/r^2\) give \(-c_df(x)\) for continuous densities, and the strict generalized-supermean comparison supports the harmonic converse. The last global extension uses classical harmonic lowering/reduction and reflection, **not the user-excluded Demailly approximation programme**. The classical reduction and reflection prerequisites remain dependencies, not newly certified complete chains.

## Targeted §20.2 trace/restriction checks and explicit exclusion boundary

Within the compact connected Kähler hypothesis at §20.2 line 65, Proposition 20.2.4 uses a \(d_S\)-comparison of two *given* quasi-equisingular sequences; Proposition 20.2.21 preserves separate \(\mathcal I\) and \(P\) equivalence, including the scaling of background classes. In Proposition 20.2.22 the reduction from a failed **net** convergence to a bad increasing chain of indices is valid because the claimed topology is already expressed by a metric: choose indices successively both beyond prior indices and within the \(j^{-1}\) distance threshold, while retaining the fixed trace-distance failure. This is **not** a blanket appeal to sequential compactness. For Lemma 20.2.24 the precise setting is bimeromorphic \(W\to Y\) and trace on the normalizations, not arbitrary inverse images; Proposition 20.2.26 assumes **smooth \(Y\)** and uses restriction of multiplier ideals only under that hypothesis.

The next proof steps cite §5.18.9, §16.9.47/49/59, §18.1.14/15 and other approximation/model inputs. They are recorded as **conditional dependencies** and were not expanded or certified. The dedicated §20.2.28 global Ohsawa–Takegoshi extension proof and any regularization/Bergman/L²/multiscale/positivity-loss completion were **intentionally not audited**, even where adjacent.

## Status and outstanding work

- **New findings:** one low / verified conditional deduction, no new confirmed false theorem or proof gap, no new genuine duplication. Previously published boundary Poisson Hölder rates, Green polar deletion, and heat-kernel radius uniformity findings were checked against the ledger and **not** repeated as new progress.
- **Actual direct coverage:** two **entire current substantive mathematical sections** (§§3.3 and 3.5); targeted selected passages in **one additional section** (§20.2), not its whole proof, and no historical first-visit claim. **Zero complete transitive upstream proof-chain certifications.**
- **Deferred-by-user:** all prior Demailly regularization/Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss notes stay deferred, **not solved or certified**.
- **Still open:** full upstream proof certification for local Riesz/Harnack/regularized reduction, and the nonexcluded trace dependencies and remainder of §20.2. No Python or JS tests, project build, CI, permanent-tag mutation, source or main editing, or website publication.
