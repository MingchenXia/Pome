# Exact affine concavity deficit of Gauduchon root volume; §§12.3–12.5 direct audit

**Date:** 2026-11-20. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Scope:** the *integrated Pome reading edition*, not only its sources. No changes to mathematical statements, original source, tags, or main are made by this report.

## Source-anchored direct scope

1. **§12.3, entire mathematical lines 7–59**: docs/sections/a-gauduchon-variational-volume--the-equality-case-of-concavity-and-the-first-variation/index.html, blob d94e3fc055b0642a86495c27ad8f5af6f24f17d1. Theorem 12.3.1 source non-kahler-pluripotential-theory:6B1A74F2, permanent 2220E0C47510, statement lines 11–17 and proof 23–29. Proposition 12.3.2 source 6D3F0AB8, permanent 94AFD9E43DE0, lines 34–59.
2. **§12.4, entire mathematical lines 7–79**: docs/sections/a-gauduchon-variational-volume--second-variation-on-background-classes/index.html, blob 4992f82c6e84918ead47a972eab7e3238a147655. Proposition 12.4.1 source non-kahler-pluripotential-theory:C55D0CC4, permanent 67FDDBC10DBD, lines 23–63; grouped formulas (12.4.2)–(12.4.3) source 86F8F24F, permanent E544AEC2FDDB, lines 24–27; background Hessian metric (12.4.4) source B96CF85C, permanent 6BCEC0329DE5, lines 69–74; separate repeated display at physical line 79 source 3217D224, permanent 88A03DC67E97.
3. **§12.5, entire mathematical lines 7–48**: docs/sections/a-gauduchon-variational-volume--recovering-a-positive-class-from-its-gauduchon-derivative/index.html, blob 829d10abfa8f92c7c77fde66704adb6486ccdc93. Proposition 12.5.1 source non-kahler-pluripotential-theory:765CFEAC, permanent 4BBB232A044C, lines 23–44.
4. **Selected dependencies only**: §12.2 lines 49–80, identifying the smooth solution form, Gauduchon minimizers and equality in the arithmetic–geometric mean inequality (Theorem 12.2.3); §12.6 lines 7–62, checking the already printed radial product metric and avoiding duplicate registration; §11.23.2 (adjoint probability) and §11.40.4 (smooth implicit dependence) through the explicit references in §§12.3–12.4. The latter two are **not** newly certified end-to-end. No review of excluded Demailly programmes.

## POME-GAUD-ROOT-AFFINE-GREEN-DEFECT-001

**Status: verified conditional deduction. Severity: low.** This is an *exact quantified strengthening* of the true concavity/equality statements of §§12.3–12.4, **not a counterexample, missing-proof repair, or new proof of the upstream smooth Monge–Ampère existence theorem**.

Let \(X\) be a connected compact complex manifold of dimension \(n\ge 1\), \(\mu\) a smooth positive probability form, and \(\theta_0,\theta_1\in\mathscr P\), the cone of smooth real \((1,1)\)-backgrounds possessing a positive smooth representative. Set
\[
\theta_s=(1-s)\theta_0+s\theta_1,\quad \chi=\theta_1-\theta_0,\quad
\lambda_s=\lambda_\mu(\theta_s)>0,\qquad 0\le s\le1.
\]
Let \(\Omega_s=\theta_s+dd^c u_s\) solve \(\Omega_s^n=\lambda_s^n\mu\), with one fixed mean normalization for \(u_s\), and let \(\nu_s\) be its smooth positive adjoint probability satisfying
\[
\int_X\operatorname{tr}_{\Omega_s}(dd^cv)\,d\nu_s=0
\]
for all smooth real \(v\). Define the Hermitian endomorphism
\[
A_s=\Omega_s^{-1}(\chi+dd^c\dot u_s),\qquad
r_s=\lambda_s'/\lambda_s,\qquad
Q_s=\frac{\lambda_s}{n}
\int_X\|A_s-r_s I\|_{\Omega_s,\mathrm{HS}}^2\,d\nu_s.
\]
The *exact concavity deficit* is, for every \(t\in[0,1]\),
\[
\boxed{\displaystyle
\lambda_t-\big((1-t)\lambda_0+t\lambda_1\big)
=\int_0^1K(t,s)Q_s\,ds, \quad
K(t,s)=
\begin{cases}
s(1-t),&0\le s\le t,\\
t(1-s),&t\le s\le1.
\end{cases}}
\tag{A}
\]
In particular, letting \(q_*=\min_{0\le s\le1}Q_s\),
\[
\boxed{\lambda_t-\big((1-t)\lambda_0+t\lambda_1\big)
\ge\tfrac12q_*t(1-t).}\tag{B}
\]
If \([\theta_0]\) and \([\theta_1]\) are not proportional by a **positive** scalar modulo smooth \(dd^c\)-terms, then \(q_*>0\). Otherwise \(Q_s=0\) for all \(s\) and both sides of (A) vanish. Thus (A) is an exact integral, not just a qualitative Jensen inequality; (B) supplies a uniform strictly positive segment-dependent modulus away from a projective \(dd^c\)-ray.

### Complete derivation

The positive-representative cone \(\mathscr P\) is convex, since convex combinations of positive representatives remain positive. Smooth dependence follows from Proposition 12.3.2 along the compact affine segment; in particular \(\lambda_s,u_s,\Omega_s,\nu_s\), and \(Q_s\) are smooth in \(s\). Differentiating
\(\log(\Omega_s^n/\mu)=n\log\lambda_s\) yields, pointwise on \(X\),
\[
\operatorname{tr}A_s=n r_s.
\]
Differentiating once more, using the *affine* assumption \(\ddot\theta_s=0\) and the inverse-matrix derivative, yields
\[
\operatorname{tr}_{\Omega_s}(dd^c\ddot u_s)
-\operatorname{tr}(A_s^2)
=n\big(\lambda_s''/\lambda_s-r_s^2\big).
\]
Integration against the **fixed-at-\(s\)** adjoint probability \(\nu_s\) kills only the \(dd^c\ddot u_s\) term; we do not differentiate \(\nu_s\) or interchange limiting measures. Consequently
\[
-\lambda_s''=\frac{\lambda_s}{n}
\left(\int_X\operatorname{tr}(A_s^2)\,d\nu_s-nr_s^2\right)
=\frac{\lambda_s}{n}\int_X\|A_s-r_sI\|^2\,d\nu_s
=Q_s\ge0.
\]
The norm identity uses that \(A_s\) is Hermitian, its trace is the constant \(nr_s\), and \(\nu_s\) is a probability. This reproduces the established Proposition 12.4.1 with its *exact* normalization \(1/n\).

Put \(h(t)=\lambda_t-(1-t)\lambda_0-t\lambda_1\). Then \(h(0)=h(1)=0\) and \(-h''(t)=Q_t\). The Dirichlet Green kernel for \(-d^2/dt^2\) on \((0,1)\) is \(K(t,s)\) above: it is continuous, piecewise affine, vanishes at \(t=0,1\), and its first derivative has a jump \(-1\) at \(t=s\). Integrating the scalar ODE therefore proves (A) without additional regularity or compactness input. Since \(\int_0^1 K(t,s)\,ds=t(1-t)/2\), (B) follows.

For rigidity, if \(Q_{s_0}=0\), the strictly positive smooth density of \(\nu_{s_0}\) and continuity of the integrand force \(A_{s_0}=r_{s_0}I\) everywhere. Proposition 12.4.1 (or its displayed equality proof, physical lines 54–60) then implies \(\chi=r_{s_0}\theta_{s_0}+dd^cf\). On the quotient by smooth \(dd^c\)-terms, \([\chi]=r_{s_0}([\theta_0]+s_0[\chi])\). Since \([\theta_0]\neq0\) (it pairs positively with a Gauduchon metric), \(1-r_{s_0}s_0\neq0\), and hence \([\theta_1]\) is proportional to \([\theta_0]\). Because both classes are positive, the factor is strictly positive. Conversely positive proportionality modulo \(dd^c\) makes \(\lambda_s\) affine by homogeneity and gauge invariance, and \(Q_s=0\) by the identity. This establishes \(Q_s>0\) for *every* \(s\) if the endpoints are projectively distinct; compactness of \([0,1]\) then gives \(q_*>0\).

**Affected dependents / proposed edit:** A self-contained *optional corollary* after §12.4.1 can record (A)–(B) as a quantitative interpretation of §§12.3.1 and 12.4.1; it can inform stability estimates for affine families of Gauduchon backgrounds, but it does not replace existence, uniqueness, or PDE regularity in §§11.40/12.2/14.2. No existing source statement requires correction. No claim of a universal modulus over the whole infinite-dimensional cone: \(q_*\) depends on the chosen compact segment.

## POME-GAUD-SECOND-VARIATION-VISIBLE-DUPLICATE-001

**Status: genuine duplication (display/canonicalization only). Severity: low.** In the *same integrated §12.4 page*, equation (12.4.3)
\[
-\frac{d^2}{dt^2}\log\lambda_\mu(\theta_t)
=\frac1n\int_X\operatorname{tr}(A_\chi^2)\,d\nu_\Omega
\]
appears first as the second line of the two-line numbered align at physical lines 24–27 (source 86F8F24F, permanent E544AEC2FDDB), and again as a standalone separately tagged displayed equation at **physical line 79** (source 3217D224, permanent 88A03DC67E97). These are identical mathematical content with the same visible number (12.4.3), not two distinct hypotheses or two legitimate theorem variants. The standalone line is retained as an independent reading chunk after the §12.4 explanatory prose. This is *not* a false equation and does not license deletion of any permanent tag or historical source label.

**Proposed future production patch (not applied):** render the mathematical formula once, preserve both source/permanent identities as stable anchors/aliases and provenance, and make both incoming links resolve to the canonical visible equation; inspect numbering and citation panels before integration. Affected displayed duplicate and any backlinks to both tags, but not Proposition 12.4.1's proof or Hessian-metric formula (12.4.4).

## Further direct-review checks

- In §12.3, the equality case is obtained from a *common Gauduchon minimizer* and pointwise equality of the trace–determinant inequality. The common solution forms become proportional by a constant because their top powers have fixed constant ratios relative to \(\mu\); no unjustified pointwise-to-global proportionality is used.
- The first-variation formula in §12.3.2 correctly normalizes the denominator \(D_\mu(\gamma)\), not \(\int\gamma^n\). The smooth potential's \(dd^c\)-term disappears only after multiplying by the Gauduchon conformal factor and integrating.
- In §12.4, the second-variation formula requires the direction \(\chi\) to be affine in \(t\); for an arbitrary curved background path there would also be a term involving \(\ddot\theta_t\). The adjoint measure is frozen **at the differentiation parameter**.
- In §12.5, the positive \((n-1)\)-root of \(\Xi_\theta\) is used only for \(n\ge2\), the quantity \(D_\mu\) scales by degree \(n-1\), and the reconstruction of \(\Omega_\theta\) correctly uses \(\lambda_\mu(\theta)\), not its \(n\)th power. The \(n=1\) case is separately addressed.
- The radial metric product in §12.6.1 is *already printed*, so it is not registered as new. Whole §§12.2 and 12.6, and their upstream existence/adjoint proofs, are **not** certified in this run.

## Accounting and restrictions

**New complete direct section readings:** three (§§12.3, 12.4, 12.5), with prior first visits not presumed. **Selected upstream/adjacent checks:** §12.2.3 and §12.6.1 plus the cited §11.23.2/§11.40.4 interfaces; **complete transitive proof-chain certificates:** zero. **New findings:** one verified conditional deduction and one genuine duplicate display. **Confirmed false printed mathematical statements:** zero. No builds, tests, CI, publication, or modifications to main, source bodies, registry, permanent tags, or website.

Demailly approximation/regularization and all dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programmes remain **deferred-by-user, neither resolved nor certified**.
