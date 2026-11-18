# Modification pullback of Gauduchon tests: two-sided bounds and sharp necessity of dd^c-closedness

- **Date:** 2026-11-18
- **Finding ID:** POME-GAUD-MODIF-TEST-DDC-CLOSEDNESS-SHARP-001
- **Severity / classification:** low / **verified conditional deduction** (a new precise boundary test, not a false printed theorem or a complete certification of the source's external dependencies).
- **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
- **Primary integrated file:** docs/sections/a-gauduchon-variational-volume--orders-of-degeneration-at-the-nef-boundary--comparison-under-an-arbitrary-modification/index.html (blob 2752af2181f07f54695112f0007173b9e4dad128).
- **Crosschecked integrated file:** docs/sections/a-gauduchon-variational-volume--orders-of-degeneration-at-the-nef-boundary--strict-changes-under-one-blowup/index.html (blob 44644097cffbe33a98a2984623353827b8298fcd).
- **Stable primary source/permanent anchors:** non-kahler-pluripotential-theory:9F4393DE / 0A017BFF9468 (Lemma 12.22.1, physical lines 14–27); non-kahler-pluripotential-theory:AAF8E58D / 51797AE0DE1F (Lemma 12.22.3, lines 33–50); non-kahler-pluripotential-theory:249AEE03 / 8AB4DFD2719F (Proposition 12.22.5, lines 56–107).
- **Crosscheck anchors:** non-kahler-pluripotential-theory:F3889ABB / 1E30136A67F6 (Proposition 12.23.1, lines 14–95); equation 12.23.2 source D2C0DDD8 / permanent 48EE58E16325 (lines 40–51); equation 12.23.5 source 1C89ABAB / permanent FE92C82454E6 (lines 79–85); equation 12.23.6 source 836D3D8F / permanent 85080CF9B131 (lines 86–94).

## Exact claims

Let π:Y→X be a modification of connected compact complex manifolds of dimension n≥2, and fix positive smooth Hermitian (1,1)-forms h_X and h_Y. For every **smooth semipositive dd^c-closed** (n−1,n−1)-form Ψ on X, there are constants a,K>0 depending only on the map and the metrics, but **not on Ψ**, such that

\[
 a\int_X h_X\wedge\Psi
 \leq \int_Y h_Y\wedge\pi^*\Psi
 \leq K\int_X h_X\wedge\Psi. \tag{A}
\]

The upper bound is the printed Lemma 12.22.3 (which states it for strictly positive Gauduchon tests). Its proof applies without change to semipositive smooth dd^c-closed Ψ. The lower bound is an additional, elementary deduction. In an explicit point blowup of the projective plane, **equality with exact factor 2** holds for every such Ψ.

Crucially, the assumption dd^c Ψ=0 cannot be discarded from the upper estimate: there is a sequence of smooth **strictly positive** (1,1)-forms Ψ_j on P² with

\[
 \int_{\mathbf P^2}H\wedge\Psi_j=2,\qquad
 \int_{\operatorname{Bl}_0\mathbf P^2}(H+L)\wedge\pi^*\Psi_j
 \longrightarrow +\infty. \tag{B}
\]

Thus an attempt to extend Lemma 12.22.3 to arbitrary positive tests by positivity alone would be **false**. The printed lemma and Proposition 12.22.5 explicitly require Gauduchon/ dd^c-closed tests and are **not refuted**. This is a boundary counterexample, not an identified error in Pome.

## Proof of (A), including the dependency boundary

Since π^*h_X is smooth and semipositive and h_Y is positive definite on compact Y, choose M>0 such that π^*h_X≤M h_Y pointwise. Positivity of π^*Ψ yields

\[
 \int_Y h_Y\wedge\pi^*\Psi
 \ge M^{-1}\int_Y\pi^*(h_X\wedge\Psi)
 =M^{-1}\int_X h_X\wedge\Psi,
\]

where the last equality is the degree-one change-of-variables identity for smooth top forms; exceptional analytic subsets have zero smooth top-degree volume.

For the upper bound, recall the specific geometric steps verified in the printed Lemmas 12.22.1 and 12.22.3. The permitted Hironaka elimination input supplies Z and maps p:Z→X, F:Z→Y such that p=π∘F, where p is a composition of smooth-center blowups. Relative positivity of O(−E) along blowup fibers produces a positive Hermitian form h_Z=C₀p^*h_X−η_D for an effective exceptional real divisor D. By compactness, h_Z≥b F^*h_Y for some b>0. Consequently

\[
 b\int_Yh_Y\wedge\pi^*\Psi
 \le C_0\int_Xh_X\wedge\Psi
       -\int_Z\eta_D\wedge p^*\Psi.
\]

The Poincaré–Lelong formula and **dd^c p^*Ψ=0** imply
\[
 \int_Z\eta_D\wedge p^*\Psi=\int_Dp^*\Psi=0.
\]
Indeed every component of D maps by p into an analytic subset of complex codimension at least two in X; the pullback of an (n−1,n−1)-form to its regular locus is zero by rank. Therefore K=C₀/b works. The argument uses neither strict positivity of Ψ nor any analytic regularization programme. It does use dd^c-closedness in the Poincaré–Lelong integration-by-parts step: that hypothesis cannot be silently dropped.

For a chain of modifications π₁:Y→X and π₂:Z→Y, the same argument applies successively, because π₁^*Ψ is still smooth semipositive and dd^c-closed. Thus the two constants can be multiplied for the composite, with an arbitrary fixed intermediate Hermitian form. No claim of uniform constants over arbitrary modification chains is made.

## Exact model: sharp factor 2 and failure without closedness

Let π:\(\widetilde B=\operatorname{Bl}_{[1:0:0]}\mathbf P^2\to B=\mathbf P^2\). Let H be the normalized Fubini–Study form on B, also denoting π^*H upstairs; let ρ:\(\widetilde B\to\mathbf P^1\) be the incidence direction map and L=ρ^*ω_FS. Then h_Y=H+L is Kähler, H² has total mass 1 and L²=0. The exceptional divisor E gives the cohomological relation [L]=[H]−[E]. Since a smooth dd^c-closed Ψ permits integration by parts against a global potential for cohomologous curvature forms, and π|_E is constant,

\[
 \int_{\widetilde B}L\wedge\pi^*\Psi
 =\int_{\widetilde B}(H-[E])\wedge\pi^*\Psi
 =\int_B H\wedge\Psi.
\]

The bracket [E] in this display denotes the current of integration, not an equality of pointwise smooth forms. In particular,

\[
 \boxed{\int_{\widetilde B}(H+L)\wedge\pi^*\Psi
       =2\int_BH\wedge\Psi.} \tag{C}
\]

So for these fixed metrics the upper and lower comparison constants are both exactly 2 on the dd^c-closed positive cone. This is a concrete calibration of the printed estimate and does not imply an optimal universal constant for general modifications.

We now keep the same map and metrics but remove dd^c-closedness. In the affine chart near the blown-up point write s=|z|² and u(s)=s/(1+s). The **exact radial mass formulas** checked independently from Equation 12.23.2 (m=2) are

\[
 \int_{\{|z|^2<s\}}H^2=u(s)^2,\qquad
 \int_{\{\pi^{-1}(|z|^2<s)\}}(H+L)^2=2u(s)+u(s)^2.
\]

Because L²=0, subtraction gives the exact cumulative measure
\[
 \int_{\{\pi^{-1}(|z|^2<s)\}}H\wedge L=u(s).
\]
Thus for nonnegative smooth radial test functions supported at 0<s<r, the ratio of radial shell densities is

\[
 \frac{d\mu_{HL}}{d\mu_{H^2}}(s)
 =\frac{du(s)}{d(u(s)^2)}
 =\frac1{2u(s)}
 \ge \frac1{2u(r)}. \tag{D}
\]

For each small r>0, choose a nonnegative smooth radial bump f_r on B, supported in an annulus 0<|z|²<r, normalized so that \(\int_B f_rH^2=1\). This is possible, and the bump extends by zero smoothly to the whole B. Put \(\Psi_r=(1+f_r)H\). It is smooth and **strictly positive** on B but generally not dd^c-closed. Then

\[
 \int_B H\wedge\Psi_r=2,
\]

whereas (D) and \(\int_{\widetilde B}H\wedge L=1\) give

\[
 \begin{aligned}
 \int_{\widetilde B}(H+L)\wedge\pi^*\Psi_r
 &=2+\int_{\widetilde B}(1+f_r\circ\pi)H\wedge L\\
 &\ge 3+\frac1{2u(r)}.
 \end{aligned}
\]

The ratio of the two integrals is at least
\[
 \frac32+\frac1{4u(r)}
 =\frac32+\frac{1+r}{4r}\longrightarrow+\infty.
\]
This proves (B) and shows why no constant K for all arbitrary smooth positive Ψ can be inferred from the fixed map and metrics. The failure arises from angular amplification by the exceptional divisor and is unrelated to Demailly/Bergman/L² regularization.

## Inspection of the printed dependent arguments

- **Lemma 12.22.1, lines 14–27:** the relative curvature construction and codimension-two image condition provide exactly the exceptional-divisor form needed for the upper estimate; Hironaka elimination is the declared, permitted external geometric input.
- **Lemma 12.22.3, lines 33–50:** the upper inequality uses dd^c Ψ=0 at the integration-by-parts step, not merely positivity. Equation (B) proves that this dependency is mathematically essential. The printed lemma has the necessary hypothesis.
- **Proposition 12.22.5, lines 56–107:** Step 2 uses Γ_δ^{n−1}=π^*(γ^{n−1})+δγ₀^{n−1}; both summands are dd^c-closed. Hence the upper test-mass estimate is applied only in its valid scope. The denominator limit is taken for each fixed test γ before the infimum; no uniformity over varying γ is established or used. The nef pullback and the limit on the exceptional locus remain conditional on the printed supporting results.
- **Proposition 12.23.1, lines 14–95:** checked the n=2 specialization of the cumulative radial formula, the identity L²=0, the determinant/cofactor normalization in the smooth product equation, and the log/power threshold in Equation 12.23.6. The present new result is the unbounded non-dd^c-closed-test ratio, **not** a recount of the older rational jump or Beta-prefactor calculations.

## Status, correction recommendation and scope

**Status:** verified conditional deduction. No printed theorem was shown false. A tempting hypothesis-free extension of printed Lemma 12.22.3 is explicitly refuted by a strict-positive smooth counterexample. The two-sided bound on the stated dd^c-closed cone and exact factor 2 are proved. Suggested **optional** documentation-only clarification: after Lemma 12.22.3 note that the upper comparison generally fails for smooth strictly positive tests without dd^c-closedness; keep the Gauduchon hypothesis in any downstream use. Any such modification would be a separately reviewable proposal, not a direct source change.

**Affected dependents:** Proposition 12.22.5, specifically Step 3 and its pullback tests; any proposed extension of the fixed-metric estimate to arbitrary smooth positive test forms; comparisons of blowup tests in Chapter 12. Neither the printed volume-order comparison nor the one-blowup example is invalidated. The global smooth Monge–Ampère equation used in §12.23 and the full general Hironaka setup are not independently re-proved here.

**Coverage delta:** selected additional proof-level check of §§12.22 and 12.23 already recorded as partially reviewed in SECTION_MATRIX.md (earlier 2026-10-25 blowup report). **0 first numbered sections; 0 entire-section proof certificates.** Current 25-chapter/747-section inventory retained. No build, tests, CI, public website, main, source body, registry, tags, or canonicalization edits. All user-excluded Demailly approximation, Bergman, L², Ohsawa–Takegoshi, multiscale atlas, and positivity-loss programmes remain **deferred-by-user**.