# Audit: curve ideal projection, background transport, and test-curve introduction
**Date:** 2026-11-22. **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Branch:** review/mathematical-audit (notes only). No editing of original mathematical bodies or publication.

## POME-IDEAL-CURVE-PROJECTION-ONLY-CONTINUOUS-AT-ZERO-001

**Severity/status:** low / **verified conditional deduction**, not a confirmed error in a printed statement and not a complete certification of all upstream dependencies.

**Precise anchor:** current integrated Theorem 18.6.4 (source label E7B73391; permanent tag A55ADED04CFD), docs/sections/multiplier-ideal-envelopes-and-goodness--geometry-of-ideal-classes/index.html, main blob 64b1c0de9266a28727de07ca3502a13ab974f001, lines 43–86. The observation on noncontinuity at a smooth nonconstant potential appears at lines 91–104. Projection Theorem 18.4.2 (source 3A211D73; permanent 7F20FD198864), docs/sections/multiplier-ideal-envelopes-and-goodness--ideal-projection/index.html, blob f1979b73c857f4874dd4a5cb10b93bcc047ebbdc, lines 22–51.

### Exact conditional deduction

Let \(Y\) be a **compact connected Riemann surface**, \(\theta\) a smooth strictly positive real \((1,1)\)-form with \(\int_Y\theta=1\), and \(\mathrm dV\) a smooth strictly positive probability volume form. Define
\[
\mathcal K_\theta=\{u\in\operatorname{PSH}(Y,\theta):\sup_Yu=0\},
\qquad
\Pi(u)=P_\theta[u]_{\mathcal I}.
\]
With the \(L^1(Y,\mathrm dV)\) topology on \(\mathcal K_\theta\), **the normalized ideal projection \(\Pi:\mathcal K_\theta\to\mathcal K_\theta\) is continuous exactly at the zero potential**.

More strongly, for every \(u\in\mathcal K_\theta\), there are smooth \(\theta\)-psh \(s_j\) and finite-rational-atomic Green ideal models \(a_j\) such that
\[
s_j\to u,\quad a_j\to u \text{ in } L^1,\qquad
\Pi(s_j)=0,\quad\Pi(a_j)=a_j\to u.
\]
The two limiting images disagree at every \(u\ne0\).

### Proof

**Continuity at zero.** Because \(v\in\mathcal K_\theta\) is nonpositive, \(v\) is itself a competitor for \(P_\theta[v]_{\mathcal I}\); hence \(v\le\Pi(v)\le0\). Since the positive background \(\theta\) makes the zero function \(\theta\)-psh, \(\Pi(0)=0\). Consequently
\[
0\le \|\Pi(v)\|_{L^1(\mathrm dV)}
=-\int_Y\Pi(v)\,\mathrm dV
\le-\int_Yv\,\mathrm dV
=\|v\|_{L^1(\mathrm dV)}.
\]
Thus \(\Pi\) is continuous at zero. This inequality is one-point control, not global Lipschitz continuity.

**Atomic approximation.** Theorem 18.6.4 gives, for each \(u\in\mathcal K_\theta\), a sequence \(a_j\) of normalized Green potentials of finite atomic probability measures with rational weights, converging to \(u\) in \(L^1\). Its proof derives the exact identity \(\Pi(a_j)=a_j\) from multiplier-ideal equality of Lelong numbers, exhaustion of the unit curvature mass by the prescribed atoms, and connected harmonic uniqueness. Neither the rationality restriction nor the pole locations affect the \(L^1\) limit.

**Smooth approximation (independent of Demailly regularization).** The curvature measure
\[
\nu=\theta+\mathrm{dd}^{\mathrm c}u
\]
is a positive probability measure on \(Y\). Choose smooth nonnegative probability forms \(\rho_j\) converging weakly to \(\nu\). They exist by approximating \(\nu\) with finite atomic probabilities supported at points in small Borel cells, then replacing each point mass by a smooth bump of equal mass supported inside a sufficiently small coordinate disk. For each continuous test function, uniform continuity on compact \(Y\) controls the error. The classical linear Green/Poisson equation on a compact connected Riemann surface gives smooth functions \(s_j\) solving
\[
\theta+\mathrm{dd}^{\mathrm c}s_j=\rho_j,\qquad\sup_Ys_j=0.
\]
Positivity of \(\rho_j\) gives \(s_j\in\mathcal K_\theta\). Normalized \(L^1\)-compactness supplies a convergent subsequence from every subsequence. Every limit \(s\) satisfies \(\theta+\mathrm{dd}^{\mathrm c}s=\nu\), by distributional continuity, and has \(\sup_Ys=0\), by continuity of the normalized psh supremum under \(L^1\) convergence. Then \(\mathrm{dd}^{\mathrm c}(s-u)=0\), so \(s-u\) is a harmonic distribution, hence a constant on connected compact \(Y\). The normalizations force \(s=u\). Uniqueness of all cluster points proves \(s_j\to u\) in \(L^1\).

Each \(s_j\) is smooth, hence has trivial multiplier ideals at all positive scales. Since \(0\in\operatorname{PSH}(Y,\theta)\), the ideal projection of a smooth \(s_j\) is zero: \(\Pi(s_j)=0\). Only classical **linear Poisson smoothing of curvature measures on a curve** is used, not any excluded Demailly/Bergman/L² approximation programme.

**Noncontinuity away from zero.** If \(\Pi\) were continuous at \(u\), the smooth sequence would give \(\Pi(u)=0\), while the atomic sequence would give \(\Pi(u)=u\). Hence \(u=0\), completing the proof.

**Proposed change:** add an optional conditional corollary after Theorem 18.6.4; retain the printed theorem, attribution, and permanent tags. **Possible dependents:** the \(L^1\) class completion and topology in §18.6, and future results that invoke continuity of ideal projection in \(L^1\). This finding neither asserts a false existing theorem nor substitutes for transitive verification of normalized compactness, the curve Green operator, or the ideal projection theorem.

## Whole current section reviews

### §18.5 — background changes and envelope mass

Current integrated file: docs/sections/multiplier-ideal-envelopes-and-goodness--changes-of-background-and-envelope-mass/index.html, main blob b1f37213571516320cd74288e4b3cbd1be2166bc, lines 7–89, section tag FD3DFA6C79CF.

- **Proposition 18.5.1**, source 41400384, permanent 07B0D783C3F0, lines 11–29: both transported competitors \(v-f+\min f\) and \(v'+f-\max f\) satisfy the new nonpositive obstacle and preserve ordinary or ideal class; verified the inequality orientations.
- **Proposition 18.5.2**, source BF2F5187, permanent 6E8985733CBC, lines 36–56: distinguished equality of the underlying current from nonclosed Hermitian background mass; checked the reduction to Example 11.1.12 and Eq. 11.1.13, but did not independently certify the original torus calculation.
- **Proposition 18.5.5**, source 47D5441C, permanent A2602BC06784, lines 77–89: checked the inference from ordinary envelope zero via Proposition 18.4.4. The infinite-mass witness is imported from Proposition 16.28.72, not independently reconstructed here.

### §18.6 — geometry of ideal classes

Current integrated file: docs/sections/multiplier-ideal-envelopes-and-goodness--geometry-of-ideal-classes/index.html, main blob 64b1c0de9266a28727de07ca3502a13ab974f001, lines 7–160, section tag 3D693DBCCBE2.

- **Proposition 18.6.1**, source C2DA1190, permanent 47A414940A74, lines 20–35: checked nondegeneracy using psh representatives, total boundedness from normalized compactness, and equivalence of smooth positive volumes.
- **Theorem 18.6.4**, source E7B73391, permanent A55ADED04CFD, lines 43–87: checked the unit curvature mass, exact Lelong atoms, weak finite atomic approximation, rational coefficient rounding, Green potential \(L^1\) convergence via compactness/harmonic uniqueness, and incompleteness witness.
- **Proposition 18.6.6**, source 5F66399A, permanent 8B21A468DD06, lines 110–140: with \(a=1-\tau\), verified
  \[
  \theta+\mathrm{dd}^{\mathrm c}(a q_j)=\tau\theta+a\nu_j,\qquad
  \mathrm{MA}_\theta(r_j)=\theta+\mathrm{dd}^{\mathrm c}r_j-a\nu_j,
  \]
  with non-pluripolar mass \(\tau\), weak measure limit \(\tau\theta\) and ordered \(d_S\) gap \((1-\tau)/2\).
- **Example 18.6.8**, source 1415C673, permanent 0F685C3DE85F, lines 151–160: checked that \(ta\) belongs to the smaller background \(t\theta\) and the scalar upper bound tends to zero as \(t\downarrow0\). No independent certification of §11.39 normalization scalar prerequisites.

### §17.11 — short test-curves introduction

Current file docs/sections/test-curves/index.html, main blob 0ece4d0eccf9c5e35e7ae6c4bc55335897e74e80, lines 7–19, permanent section tag BA6AA7598BE3. Read in full. Checked Ross–Witt Nyström historical attribution, concave/convex Legendre sign convention and references to §§17.12–17.15, 21.11 and 22.1. Reading the introduction does **not** certify the correspondence theorem or subsequent non-Archimedean arguments.

## Status, actual scope, and deferred work

**Current increment:** 2 directly read whole mathematical sections (§§18.5, 18.6), 1 complete short introduction (§17.11), 1 new low conditional deduction, 0 newly confirmed errors, and 0 completely certified upstream proof chains. Historical first-visit status remains unreconciled.

**Remaining dependencies:** the curve Green operator and normalized compactness, full projection §18.4, §11.1.12–13, §16.28.72, §11.39 and §§17.12–17.15 are not all fully independently certified. They are not silently promoted to resolved. Demailly regularization and the dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remain **deferred-by-user**.

**Operations not performed:** repository builds or tests, CI, automatic publishing, modifications to main, mathematical source/bodies, registries, canonicalization, or permanent tags.
