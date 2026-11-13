# The sharp full-Gårding-cone mixed-trace coefficient

**Date:** 2026-11-13. **Finding:** \`POME-HESS-MIXED-CONE-SHARP-001\`.  
**Severity / classification:** low / **verified conditional deduction**; printed lemmas are correct but their mixed coefficient is not optimal for \(m\ge3\). This is a new full-cone assertion, not the earlier coordinatewise \(F_i\) estimate.

## Exact production reading-edition anchors

- Pinned production \`main\`: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
- \`docs/sections/complex-hessian-equations--the-admissible-cone/index.html\`, Git blob \`925e6109ab7d800cde9bec4b0487842b2e6877a8\`; section source \`non-kahler-pluripotential-theory:97706797\`, permanent \`F677D35E0BD7\`. Conventions and classical Gårding assumptions: physical lines 5–16.
- Lemma **8.2.4**, source \`non-kahler-pluripotential-theory:3E489B35\`, permanent \`94C4E018DD25\`, lines **76–100**, statement lines 77–81, iterative \(1/m!\) proof lines 86–99.
- Lemma **8.2.5**, source \`non-kahler-pluripotential-theory:53FFB5F3\`, permanent \`7710D01DF6F5\`, lines **113–131**, especially full-matrix estimate line 116 and derivative reduction line 124.
- \`docs/sections/complex-hessian-equations--a-trace-estimate-with-a-prescribed-potential/index.html\`, Git blob \`3d7fe6d1867a0d8ac268042a59e112329a6c8af3\`; Lemma **8.4.2**, source \`non-kahler-pluripotential-theory:2489DE92\`, permanent \`61C6DAF48B41\`, statement/hypotheses physical lines **35–46**, mixed \(C_H\)-term absorption lines **59–62**, coordinate \(C_G\)-term absorption lines **65–68**.
- The actual chapter introduction \`docs/sections/complex-hessian-equations/index.html\`, blob \`5331b937ccdaba51f1ec006d5e72dc84f7addfbf\`, physical line 7 has analytic standing range \(2\le m<n\); the algebraic lemma is expressly also stated for \(m=n\).

## Exact sharpening of Lemma 8.2.4

Let \(2\le m\le n\), let \(\omega\) be positive Hermitian at a point, and let \(\alpha,\gamma\in\Gamma_m(\omega)\), **without a simultaneous eigenbasis or a semipositivity assumption**. Then
\[
\boxed{\quad
\frac{\alpha^{m-1}\wedge\gamma\wedge\omega^{n-m}}{\omega^n}
\frac{\alpha\wedge\omega^{n-1}}{\omega^n}
\ \ge\ \frac1m
\frac{\alpha^m\wedge\omega^{n-m}}{\omega^n}
\frac{\gamma\wedge\omega^{n-1}}{\omega^n}.\quad}
\tag{A}
\]
It extends to \(\gamma\in\overline{\Gamma_m(\omega)}\) by continuity. The factor \(1/m\) is **optimal even among strictly positive-definite \(\alpha,\gamma\)**. Thus (A) improves the valid printed factor \(1/m!\) by \((m-1)!\) when \(m\ge3\), and agrees when \(m=2\).

### Proof for arbitrary, possibly noncommuting Hermitian forms

Write
\[
P(t)=\frac{(\alpha+t\gamma)^m\wedge\omega^{n-m}}{\omega^n},
\qquad
S=\operatorname{tr}_\omega\alpha,\quad T=\operatorname{tr}_\omega\gamma.
\]
Both traces are strictly positive. We explicitly use the **hyperbolicity-direction part of Gårding's classical algebraic theorem**: the \(m\)-th elementary symmetric polynomial on Hermitian matrices is hyperbolic in the identity direction, \(\Gamma_m\) is its corresponding connected hyperbolicity cone, and **every** \(\gamma\in\Gamma_m\) is again a hyperbolicity direction. Consequently \(P\), as a degree-\(m\) polynomial in \(t\), has \(m\) real roots counted with multiplicity. By cone convexity, \(\alpha+t\gamma\in\Gamma_m\) for \(t\ge0\), so none of these roots is nonnegative. Write
\[
P(t)=P(0)\prod_{j=1}^m(1+t/r_j),\qquad r_j>0.
\]
Put \(\tau=\min_jr_j\). For \(0\le t<\tau\), the connected path \(\alpha-t\gamma\) cannot leave the component \(\Gamma_m\) of \(\{P>0\}\) before meeting \(\{P=0\}\). Therefore \(\alpha-\tau\gamma\in\overline{\Gamma_m}\), and its first symmetric polynomial is nonnegative:
\[
S-\tau T\ge0,\qquad \tau\le S/T.
\]
Logarithmic differentiation now yields
\[
\frac{P'(0)}{P(0)}
=\sum_{j=1}^m\frac1{r_j}
\ \ge\ \frac1\tau\ \ge\ \frac{T}{S}.
\tag{B}
\]
The exact polarization identities
\[
P'(0)=m\frac{\alpha^{m-1}\wedge\gamma\wedge\omega^{n-m}}{\omega^n},
\quad P(0)=\frac{\alpha^m\wedge\omega^{n-m}}{\omega^n},\quad
\frac TS=\frac{\gamma\wedge\omega^{n-1}/\omega^n}{\alpha\wedge\omega^{n-1}/\omega^n}
\]
turn (B) into (A), including its **factor \(1/m\)**. Notice that no order of limits is interchanged, no eigenvector sharing is presumed, and no analytic regularization occurs.

The generalized-direction real-root property is a **genuine classical Gårding algebraic input** (beyond the short list of its consequences stated on lines 15–16). This report establishes (A) fully *conditional on that explicitly identified input*; it does **not** falsely certify a complete internal proof of hyperbolicity-direction invariance.

### Optimality and genuinely full-cone scope

For \(L>0\) take
\[
\alpha_L=\operatorname{diag}(L,1,\ldots,1),\qquad
\gamma_\varepsilon=\operatorname{diag}(1,\varepsilon,\ldots,\varepsilon),\quad\varepsilon>0.
\]
Both are **strictly positive definite**, hence in the open cone. Let \(R(L,\varepsilon)\) denote the ratio of the left side of (A) to the right side **without** its coefficient. At each fixed \(L\), continuity as \(\varepsilon\downarrow0\) gives
\[
R(L,0)=\frac{(L+n-1)\binom{n-1}{m-1}}
{m\bigl[L\binom{n-1}{m-1}+\binom{n-1}{m}\bigr]}.
\]
Here \(\binom{n-1}{n}=0\) for \(m=n\). Taking **first** \(\varepsilon\downarrow0\) at fixed \(L\) and **then** \(L\to\infty\) gives \(R\to1/m\). Therefore no larger uniform constant works even in the strictly Kähler subclass. This sequential limiting argument proves an infimum, not attainment at a degenerating endpoint.

The prior \`POME-HESS-SHARP-DIAGONAL-DERIVATIVE-001\` established the **coordinatewise** bound \(F_i\ge f/(mS)\), which tests only rank-one positive-semidefinite \(\gamma\). That coordinate argument alone cannot imply (A) for general closed \(m\)-cone forms with negative eigenvalues. The new hyperbolic-direction argument controls **every** such \(\gamma\), even without simultaneous diagonalization.

## Conditional, exactly localized consequence for Lemmas 8.2.5 and 8.4.2

Let \(f=\sigma_m(\alpha)^{1/m}>0\), \(S=\operatorname{tr}_\omega\alpha\), and let \(M\) be an arbitrary Hermitian matrix in the **closed** \(m\)-cone. Differentiate \(f\) in the direction \(M\), using \(M+\delta I\) for the open-cone argument and letting \(\delta\downarrow0\). By (A),
\[
\boxed{\qquad W_M=DF_\alpha(M)\ \ge\ \frac{f}{mS}\operatorname{tr}M.\qquad}
\tag{C}
\]
This strengthens the **full-matrix** \(1/m!\) bound printed in Lemma 8.2.5; it is independent of any simultaneous diagonalization. The rank-one case of (C) agrees with the existing, previously audited sharp coordinate inequality.

In the proof of Lemma 8.4.2, \(S\le n\lambda_1\) and \(|M_{1\bar1}|\le\operatorname{tr}M\) yield
\[
\frac{C_H}{\lambda_1}|M_{1\bar1}|
 \le\frac{nC_H}{S}\operatorname{tr}M
 \le \frac q2 W_M
\]
as soon as \(q\ge 2nm C_H/f_0\). Thus, **subject to the same hypotheses as the printed scalar lemma**, its proof remains valid with the sharpened sufficient conditions
\[
q\ge8,\qquad q\ge\frac{2nm C_H}{f_0},\qquad
q^2\ge\frac{4m C_G}{f_0}.
\tag{D}
\]
The \(C_G\) change in (D) was **already proved** in \`POME-HESS-SHARP-DIAGONAL-DERIVATIVE-001\`; it is **not** being counted as a new finding. The new contribution is the full-cone \(C_H\) improvement. This establishes the selected algebraic absorption step only; it does **not** certify the entirety of the trace maximum principle, PDE solution, or later estimates.

## Classification, dependencies, and proposed patch

**Status:** low / verified conditional deduction. The original Lemmas 8.2.4, 8.2.5 and 8.4.2 have **not** been refuted. Their sufficient numerical conditions are valid, but the mixed coefficients can be sharpened. **Outstanding external dependency:** the generalized-direction real-root Gårding theorem for the Hermitian \(m\)-Hessian polynomial. No circular use of Lemma 8.2.5 was made in establishing (A).

**Proposed separately reviewable source patch (not applied):** append the root-factor proof as a sharpened clause to Lemma 8.2.4; append (C) as a full-cone strengthening of Lemma 8.2.5 (preserving the rank-one version); and conditionally replace the two sufficient \(m!\) coefficients in Lemma 8.4.2 by \(m\), with explicit attribution to both independent sharpening reports. Preserve the original source labels, permanent tags, conventions and all historical attribution. Affected dependents: Lemma 8.4.2 \(C_H\) trace absorption and any estimates using its chosen \(q\); the analytic chain is **not transitive-certified** here.

**Actual incremental coverage:** only selected §8.2.4 mixed inequality, §8.2.5 full-matrix derivative, §8.4.2 \(C_H\)-absorption; §8.2.3, §8.1 and the previously checked coordinate step are background comparisons. Sections **8.2 and 8.4 were already partially visited**: **zero** new first-numbered-section visits and **zero** newly certified whole sections. Current ToC remains **25 chapters / 747 numbered sections**. No builds, tests, CI, publication, full-project verification or production edits were performed. Demailly approximation/regularization and dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof programmes remain **deferred-by-user**, neither reopened nor resolved.
