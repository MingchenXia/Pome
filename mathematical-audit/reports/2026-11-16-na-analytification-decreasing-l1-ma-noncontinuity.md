# Analytification is not continuous under decreasing smooth psh limits, even at fixed Monge–Ampère mass

**Finding ID:** POME-NA-AN-DEC-L1-MASS-NONCONTINUITY-001  
**Date:** 2026-11-16  
**Classification:** **low / verified conditional deduction**: sharp explicit counterexample to an *unasserted* limiting inference. Definition 22.1.79, equation 22.1.80, and the printed results cited below remain valid. This does **not** claim any printed Pome theorem is false or that a proof of the full comparison theorem has been certified.

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272  
**Reading edition:** docs/sections/non-archimedean-pluripotential-theory/index.html, blob 8448d710690ebe1cc28040f9611d05c9d008a961.  
**Direct anchors:** §22.1.77 projective/closed-form hypotheses, physical lines 1217–1220, subsection tag 5CF97BFE6BF8; Definition 22.1.79, source sgpt:39357F73 / permanent 322D4668B967, line 1224; equation 22.1.80, source sgpt:F01F6B39 / permanent 2CFF9C7C56DB, lines 1225–1229; dyadic equation 22.1.81, source sgpt:55DCD9DC / permanent DFFDD4E75B4D, lines 1233–1241; Definition 22.1.82, source sgpt:4500974E / permanent 866728488224, line 1243, and its 22.1.83 formula, source sgpt:1865D623 / permanent 45957E422015, lines 1244–1257.  
**Direct upstream comparison:** Proposition 5.16.15, source sgpt:597608EC / permanent 8EFDC4A2C19E, equation 5.16.16, source sgpt:A3467871 / permanent DAEF62372440 (integrated tag page docs/tag/8EFDC4A2C19E/index.html). Proposition 22.1.84, source sgpt:2904C1F5 / permanent A87B7BF0C3D5, physical lines 1261–1283, was inspected for its stated fixed-curve hypotheses, **not** independently reproved.

## Exact statement

There exist a smooth polarized projective curve (in fact X = P^1), a smooth Kähler representative θ of degree one, a sequence of **smooth strictly θ-psh** global potentials u_j and a singular θ-psh potential u such that:

1. u_j decreases pointwise to u and converges in L^1(X) to u; the u_j are uniformly bounded above;
2. all currents θ + dd^c u_j are smooth Kähler forms with total mass 1, and converge weakly as currents (hence as measures) to the positive current θ + dd^c u = [p], also of total mass 1;
3. at the divisorial valuation v = ord_p, **u_j^An(v) = 0 for every j**, but **u^An(v) = -1**.

Thus even the joint package “decreasing smooth θ-psh potentials + L^1 convergence + positive-current weak convergence + preservation of total Monge–Ampère mass” does **not** make the operation in 22.1.80 continuous from above. In particular, one cannot commute this limit with the multiplier-ideal singularity limit. The failure is pointwise at a divisorial valuation, not a mere failure of a stronger topology.

## Fully explicit proof

Use homogeneous coordinates [Z_0:Z_1] on X=P^1 and let p=[1:0]. Let s=Z_1 be the section of O(1) vanishing at p, with the Fubini–Study metric h, and θ=ω_FS=c_1(O(1),h) normalized by ∫_X θ=1. Put

\[
 u=\log |s|_h^2,\qquad
 u_\epsilon=\log\bigl(|s|_h^2+\epsilon\bigr),\quad
 0<\epsilon\le1 .
\]

These are globally defined functions (with u=-∞ at p). On the chart z=Z_1/Z_0 containing p, write \(\rho(z)=\log(1+|z|^2)\). Then
\[
 |s|_h^2=\frac{|z|^2}{1+|z|^2},\qquad
 \theta=dd^c\rho,\qquad
 \rho+u_\epsilon
 =\log\bigl(\epsilon+(1+\epsilon)|z|^2\bigr).
\]
With the Pome convention \(dd^c=(i/2\pi)\partial\bar\partial\), a direct complex derivative gives
\[
 \theta+dd^c u_\epsilon
 =\frac{i}{2\pi}
   \frac{\epsilon(1+\epsilon)}
        {(\epsilon+(1+\epsilon)|z|^2)^2}\,
   dz\wedge d\bar z >0 .
 \tag{1}
\]
On the other chart w=Z_0/Z_1, the local metric potential plus u_ε is
\(\log(1+\epsilon+\epsilon|w|^2)\), again strictly subharmonic. Hence every u_ε is **smooth and strictly θ-psh globally**, with no appeal to a general approximation theorem.

As ε decreases to zero, u_ε decreases pointwise to u. Since u is locally integrable and u_1-u is integrable, dominated convergence applied to the nonnegative differences gives \(\|u_\epsilon-u\|_{L^1}\to0\). The distributional identity \(dd^c u_\epsilon\to dd^c u\) follows, and the local logarithmic Poincaré–Lelong calculation gives
\[
 \theta+dd^c u=[p].
 \tag{2}
\]
Alternatively, the density of (1) with respect to \(dx\,dy\) is
\[
 \frac{\epsilon(1+\epsilon)}
 {\pi(\epsilon+(1+\epsilon)|z|^2)^2};
\]
the substitution \(r=|z|^2\) shows directly that its total mass on the affine chart is
\(\int_0^\infty \epsilon(1+\epsilon)(\epsilon+(1+\epsilon)r)^{-2}\,dr=1\),
and that the mass concentrates at z=0. Every current (1) represents [θ], so its global integral equals 1, agreeing with the limiting point mass in (2). This is the one-dimensional Monge–Ampère mass, not merely a comparison of cohomology classes.

For every fixed ε>0, u_ε is smooth and bounded. For **each positive integer k**, its multiplier ideal is therefore \(\mathcal I(ku_\epsilon)=\mathcal O_X\), and at v=ord_p
\[
 -\frac1k v(\mathcal I(ku_\epsilon))=0,
 \qquad u_\epsilon^{\mathrm{An}}(v)=0.
 \tag{3}
\]
On the other hand u=log|z|^2−log(1+|z|^2) near p. For a holomorphic germ f=z^a g with g(0)≠0, the local integrability test for \(|f|^2e^{-ku}\) is that
\[
 \int_0^\delta r^{2a-2k+1}\,dr<\infty,
 \quad\text{equivalently }a\ge k.
\]
Thus \(\mathcal I(ku)=\mathcal O_X(-kp)\) **for every positive integer k**, so
\[
 -\frac1k v(\mathcal I(ku))=-1,
 \qquad u^{\mathrm{An}}(v)=-1.
 \tag{4}
\]
All statements follow. If v=c\,ord_p with c>0, the discrepancy is 0 versus −c. Away from p both analytifications vanish.

The example also proves the *fixed-k* discontinuity
\[
 \mathcal I(ku_\epsilon)=\mathcal O_X\quad(\epsilon>0),
 \qquad
 \mathcal I(k\lim_{\epsilon\downarrow0}u_\epsilon)
 =\mathcal O_X(-kp).
\]
This is not a claim that iterated numerical limits of the **fixed** ideals in (3) differ; rather the nonlinear assignment \(\varphi\mapsto\mathcal I(k\varphi)\) cannot be passed through the decreasing limit. The values in (3) remain exactly 0 for every ε and every k.

## Mathematical interpretation, boundaries, and dependencies

- **Not a counterexample to the reading edition:** Definition 22.1.79 is a well-defined fixed-potential valuation formula. Equation 22.1.81 is a fixed-potential dyadic infimum. Proposition 22.1.84 concerns the complexification of a fixed admissible non-Archimedean test curve. Neither states decreasing-L^1 continuity of analytification, and neither proof is invalidated by this example.
- **No mass defect:** unlike non-pluripolar mass loss phenomena, total mass here stays exactly one on the curve, so an extra assumption of *mere conservation of total Monge–Ampère mass* cannot repair the false continuity inference.
- **No uniform ellipticity:** for fixed z≠0 the density in (1) tends to zero. The example does not exclude a continuity statement under additional strong uniform differential or singularity-type controls.
- **Established inputs:** only the local definitions of psh, multiplier ideals and a direct one-variable integrability calculation, the Fubini–Study metric, and the elementary Poincaré–Lelong identity. The general approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss programme excluded by the user was **not opened**. We did not invoke it as a hidden prerequisite. Full proofs of the global Boucksom–Jonsson comparison and the analytic non-Archimedean extension are **not** thereby certified.
- **Affected argument patterns, not a proven affected theorem:** any attempted inference in §22.1.79–.100 or a future downstream proof that replaces a fixed psh potential by a decreasing/L^1-convergent sequence *and then passes 22.1.80 through that limit* must be separately justified or strengthened to convergence of the divisorial singularity data. No specific existing printed downstream theorem has been shown to make that invalid inference.

**Proposed correction (audit-only):** add a short caution following the valuation definition: “Analytification is not continuous with respect to decreasing L¹ convergence, even for smooth strictly θ-psh approximants with constant total mass; see the P¹ model.” Any future continuity theorem should specify control of the limiting singularity/divisorial valuations or an equivalent sufficient hypothesis. No source, registry, permanent tag, or main-branch changes have been made.

## Precise coverage and status

The **new** proof-level passage read is Definition 22.1.79 and equations 22.1.80–81 (main physical lines 1224–1241); Definition 22.1.82 and formula 22.1.83 (1243–1257) and Proposition 22.1.84 (1261–1283) are **comparison/context only**. Proposition 5.16.15 and equation 5.16.16 were inspected from their actual integrated tag page; their general divisorial statement is not independently re-proved. §22.1 is already partially visited; this adds **zero first-visited numbered sections and zero full-section mathematical certificates**. The current main table of contents was independently counted at **25 chapters and 747 unique numbered sections** (docs/chapters/index.html, blob c0c07abf4d8f7575b54cff2ec694fcf987f51cf8).

**Outcome:** verified, explicit failure of a tempting limiting operation; printed results not refuted. No project build, tests, CI, publication, or whole-section verification claimed. All expressly excluded work stays **deferred-by-user**, not resolved.
