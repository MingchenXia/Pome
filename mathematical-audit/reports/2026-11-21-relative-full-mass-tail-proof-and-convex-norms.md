# Direct mathematical audit: relative full-mass energy and convex-norm obstructions

**Date:** 2026-11-21.
**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Classification:** one low-severity verified proof-step repair and one medium-severity external dependency; neither is a false theorem. No fully transitive upstream proof chain is certified.

## Scope and reading-edition anchors

1. Complete mathematical reading of **§16.5, Relative full mass classes**, `docs/sections/the-envelope-operators--p-envelopes--relative-full-mass-classes/index.html`, Git blob `9c17814a07f78694a858dc941e6a76d2f3cc989f`, physical HTML lines 5–1305, beginning with Definition 16.5.1 and ending at Corollary 16.5.59 / equation 16.5.60. Directly checked the relative full-mass definitions, the mixed comparison argument, the energy cocycle, finite-energy truncation, both monotone-net continuity arguments, rooftop stability and the stated equation-solvability inputs. Source book: `sgpt`.
2. Complete mathematical reading of **§11.9, Convex norms and Gauduchon degrees**, `docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees/index.html`, blob `673557db39b7768592ef7ccfadaa3eee71a73505`, mathematical HTML lines 5–191. Section source `non-kahler-pluripotential-theory:0FAE63D7`, permanent `93399AABE3EC`. Included the curvature-normalizing Fredholm equation, localized fiber-axis norm estimates, horizontal Chern Hessian averaging, and stability under nearby integrable Dolbeault structures.
3. Selectively revisited prior complete audits §11.5 (Gauduchon trace mass) and §11.7 (weak Gauduchon currents) to check relevant normalization, not as new whole-section coverage and not as new findings. Their **already recorded** sharp AM–GM deficit `POME-GAUDUCHON-TRACE-AMGM-SQRT-DEFICIT-001` (2026-11-19) and weak threshold superdifferential (2026-11-20) must **not** be recounted as novel results.

Excluded Demailly regularization/approximation and all dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programmes remain **deferred-by-user**, neither resolved nor certified.

## Finding POME-RELENERGY-HALF-LEVEL-TAIL-REPAIR-001

**Severity/status:** low / **verified repair of an incompletely justified proof step**, NOT a false theorem. Exact location: §16.5 Proposition 16.5.30 (source `sgpt:ABE17BA7`, permanent `4280CB108A7E`, line 545), in the proof of equation 16.5.35 (source `sgpt:653816BA`, permanent `F913F2DBE96C`, lines 592–621), particularly the penultimate displayed estimate at line 618.

**Hypotheses:** \(\varphi,\psi\in\mathcal E^1(X,\theta;\phi)\) as in §16.5.30, with the proof normalized so \(\varphi\le\phi\). The non-pluripolar measure \(\mu=\theta_\varphi^n\) has finite mass, and \(\int_X(\phi-\varphi)\,d\mu<\infty\), by the relative finite-energy hypothesis.

The printed proof reaches a quantity bounded by \(2^{n-k}C\,\mu\{\varphi\le\phi-C/2\}\). It then writes
\[
\limsup_{C\to\infty}C\mu\{\varphi\le\phi-C/2\}
\le 2\limsup_{C\to\infty}\int_{\{\varphi\le\phi-C\}}(\phi-\varphi)\,d\mu=0.
\]
**The limits on both sides really are zero under the given hypothesis.** Nevertheless, the displayed passage leaves the crucial implication unjustified: the natural pointwise Markov bound with threshold \(C/2\) is NOT bounded by the integral over the *smaller* set with threshold \(C\). As an elementary check, for a nonnegative integrable random variable \(A\equiv3C/4\), one has \(C\mu(A\ge C/2)>0\) whereas \(\int_{\{A\ge C\}}A\,d\mu=0\). This example refutes only the unspoken fixed-\(C\) comparison, **not** the source's limiting assertion or Proposition 16.5.30.

**Complete elementary repair (no new analytic input):** for \(A=\phi-\varphi\ge0\) \(\mu\)-almost everywhere,
\[
0\le C\mu\{A\ge C/2\}
\le 2\int_{\{A\ge C/2\}}A\,d\mu
\underset{C\to\infty}{\longrightarrow}0
\]
by integrability and dominated convergence for the decreasing tail sets. This supplies the precise required result in equation 16.5.35. All preceding mixed comparison and mixed-mass equalities remain unchanged. A proposed source-only correction, for a separate patch/PR, is to replace the final integral's threshold \(C\) by \(C/2\) and invoke integrability. **No source change is made in this audit branch.**

**Dependents:** finite-energy cocycle Proposition 16.5.30, the energy bound Proposition 16.5.36, and finite-energy monotone continuity and rooftop arguments in the rest of §16.5 that invoke the cocycle. This is a local verified step repair, conditional on the previously stated non-pluripolar locality and comparison results; it is NOT a complete proof-chain certification.

## Finding POME-RELATIVE-FULL-MASS-DDNL-SOLVABILITY-EXTERNAL-001

**Severity/status:** medium / **genuine external dependency** (not a proof error). §16.5 Theorem 16.5.8, source `sgpt:4D0318F8`, permanent `6F1A42885C28`, physical line 140, asserts existence and normalized uniqueness of a relatively full-mass \(\theta\)-psh solution of the prescribed non-pluripolar Monge–Ampère equation for a measure of the correct positive total mass. Theorem 16.5.9, source `sgpt:5A0069A8`, permanent `0E437FB98B97`, lines 147–157, asserts unique exponential Monge–Ampère solvability and the appropriate subsolution domination for \(\lambda>0\), \(\mu(X)>0\). The paragraph at line 157 explicitly says their proofs are not supplied in this part of the book and cites **DDNL19log**. The historical citation is appropriate and must be preserved.

**Precise missing step:** the integrated §16.5 argument does not derive solvability, normalization, full relative mass and exponential comparison for arbitrary non-pluripolar data from its preceding comparison/energy estimates. Those properties are the inputs needed to construct \(\gamma_j\) in Lemma 16.5.40 (source `sgpt:E3FA9734`, permanent `4C2A27A8F97A`, lines 753–802). That construction propagates into Proposition 16.5.49 (source `sgpt:279EC696`, permanent `AAD590A053BB`, lines 963 onwards) and the finite-energy rooftop closure chain. For independent certification one would need an internally established version of the two solvability theorems with precisely these singularity and measure hypotheses; no such replacement is certified here. Do **not** infer the cited theorem is false or that mere historical attribution is a defect. Retain DDNL19log as a mathematical input, and investigate only the non-excluded existence/uniqueness chain in future audits, without reopening any expressly deferred programme.

## Other §16.5 and §11.9 checks

- Relative full-mass comparison §16.5.5 uses plurifine locality together with equality of mixed mass, and the strict/sublevel distinction is handled by shifting by a positive constant. No further confirmed error in these steps was found.
- Proposition 16.5.20 extracts a *noncofinal* increasing sequence of indices from decreasing nets only as an auxiliary witness after \(L^1\) convergence, then bounds the full net's monotone energy limit against that sequence. Proposition 16.5.37 uses Choquet's lemma to select a countable supremum-determining subfamily before constructing an increasing sequence, and similarly controls the original net via monotonicity. These are not illicit sequential compactness arguments.
- §11.9.1 chooses constant curvature density with the Gauduchon trace and uses the Fredholm index and elliptic regularity input from §11.4. These are **external/previously stated** PDE inputs for this review, not newly proved here.
- §11.9.2 uses the triangle inequality to bound both the fiber norm and the directional derivatives of its square; the fixed-sphere weights localize to each line summand. §11.9.3's horizontal-Hessian sign agrees with the curvature convention \(R_k=-dd^c\log k\).
- §11.9.4, source `non-kahler-pluripotential-theory:5A4D8636`, permanent `C222D1BB3C65`, lines 123–183, integrates the horizontal Hessian and transfers derivatives of arbitrary candidate norms to the coefficients of a fixed adjoint second-order operator. The perturbation estimate is genuinely norm-independent; no new printed error was confirmed. The following §11.10 on homogeneous convex regularization was **not** reviewed.

## Outcome and limitations

**+2 complete present-main sections directly read, +2 previously fully reviewed sections selectively rechecked, +0 fully certified transitive upstream chains.** The baseline is the 747-section collection matrix; this does not assert these were their historical first reviews. One locally repaired proof step and one actual uneliminated external theorem input are newly logged. Neither is a false mathematical statement. No software tests, builds, CI, publication, main, source, registry, canonicalization or permanent-tag edits were performed.