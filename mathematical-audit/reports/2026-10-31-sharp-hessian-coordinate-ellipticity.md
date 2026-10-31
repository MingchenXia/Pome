# Sharp coordinate ellipticity for the complex Hessian linearization

**Review date:** 2026-10-31.  
**Pinned production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Stable finding:** **POME-HESS-SHARP-DIAGONAL-DERIVATIVE-001**.  
**Severity / status:** **low / verified conditional deduction** (a stronger algebraic inequality and a conditional downstream numerical improvement). **No printed theorem is shown false; no analytic theorem or external dependency is certified.**

## Exact integrated anchors and scope

1. **Chapter range / conventions.** \`docs/sections/complex-hessian-equations/index.html\`, blob \`5331b937ccdaba51f1ec006d5e72dc84f7addfbf\`, section tag \`CFD38285654D\`, introductory physical line 7: the analytic chapter concerns \`2 <= m < n\`. The algebra in the next section expressly also applies to \`m=n\`. This finding is **not** the previously withdrawn \`m=1\` scope objection.
2. **Primary result.** \`docs/sections/complex-hessian-equations--the-admissible-cone/index.html\`, blob \`925e6109ab7d800cde9bec4b0487842b2e6877a8\`, section source \`non-kahler-pluripotential-theory:97706797\`, permanent tag \`F677D35E0BD7\`. Lemma **8.2.5**, source \`non-kahler-pluripotential-theory:53FFB5F3\`, permanent tag \`7710D01DF6F5\`, **physical lines 113–130**, especially displayed line **116** and proof **123–130**. Its coordinatewise estimate is \`F_i >= f/(m! S)\`; its **separate** general-cone pairing is \`W_M >= f tr(M)/(m! S)\`.
3. **Algebraic inputs directly checked.** Same HTML: standing normalized \`sigma_j\` and Gårding/Maclaurin facts at lines **9–34**; Lemma **8.2.3**, source \`non-kahler-pluripotential-theory:42B9BB86\`, permanent \`F86594126C69\`, lines **42–74**; Lemma **8.2.4**, source \`non-kahler-pluripotential-theory:3E489B35\`, permanent \`94C4E018DD25\`, lines **76–102**; and deleted-coordinate positivity at physical **155–156**. These inputs are assumed in the chapter; this report separately proves the new algebraic inequality but does not reconstruct every Gårding theorem.
4. **Precisely affected downstream numerical step.** \`docs/sections/complex-hessian-equations--a-trace-estimate-with-a-prescribed-potential/index.html\`, blob \`3d7fe6d1867a0d8ac268042a59e112329a6c8af3\`, section \`54309E0621C2\`, Lemma **8.4.2**, source \`non-kahler-pluripotential-theory:2489DE92\`, permanent \`61C6DAF48B41\`, hypothesis at **physical lines 35–40**, proof uses of the **mixed** estimate at **59–62** and the **coordinate** estimate at **65–68**. Only the latter threshold is sharpened; the former remains unchanged.

**Additional contextual read (not new certification):** §8.2.6 (\`non-kahler-pluripotential-theory:C6051641\`, permanent \`473C52E484B0\`, physical lines 135–152), §8.3.3 and §17.15.6–7; previously recorded test-curve issues are not repeated.

## Sharp improvement and complete algebraic proof

Let \`2 <= m <= n\`, let \`lambda = (lambda_1,...,lambda_n)\` lie in the **open Gårding cone** \`Gamma_m\` (\`S_j(lambda)>0\` for \`1<=j<=m\`), and define

\[
S=\sum_{j=1}^n\lambda_j>0,\qquad
f=F(\lambda)=\left(\frac{S_m(\lambda)}{\binom nm}\right)^{1/m}>0,\qquad
F_i=\partial_{\lambda_i}F.
\]

Then, for **every** coordinate \`i\`,

\[
\boxed{\displaystyle F_i\ \geq\ \frac{f}{m\,S}.}\tag{*}
\]

This coefficient \`1/m\` is the **best uniform coefficient**, even if all eigenvalues are strictly positive.

**Proof.** Delete \`lambda_i\`, writing \`mu=(lambda_1,...,\widehat{\lambda_i},...,lambda_n)\` of length \`N=n-1\`. The deleted-coordinate Gårding positivity already stated in the reading edition gives \`mu in Gamma_{m-1}\`, so
\[
T=S_1(\mu)>0,\qquad B=S_{m-1}(\mu)>0.
\]
Write \`A=S_m(mu)\`, defining \`A=0\` if \`m>N\`. The elementary splitting identity is
\[
S_m(\lambda)=\lambda_i B+A.
\]
We claim \`A/B<=T/m\`. If \`A<=0\`, this is immediate. If \`A>0\`, necessarily \`m<=N\` and \`mu in Gamma_m\`; the normalized Newton–Maclaurin ratio inequalities applied **in dimension N** give
\[
\frac{A}{B}
=\frac{\binom Nm}{\binom N{m-1}}\frac{\sigma_m(\mu)}{\sigma_{m-1}(\mu)}
\leq \frac{N-m+1}{m}\,\sigma_1(\mu)
=\frac{N-m+1}{mN}T
\leq \frac{T}{m}.
\]
(The final inequality only uses \`N-m+1<=N\`.) Hence
\[
\frac{S_m(\lambda)}{S_{m-1}(\mu)}
=\lambda_i+\frac AB
\leq\lambda_i+\frac{T}{m}
\leq \lambda_i+T=S,
\]
because \`T>0\`. Differentiating the normalized root and cancelling its normalization gives
\[
F_i=\frac{f}{m}\frac{S_{m-1}(\mu)}{S_m(\lambda)}
\geq\frac{f}{mS}.
\]
This argument permits \`lambda_i<0\` when \`m<n\`; it never assumes positive semidefiniteness of the original Hessian. QED.

**Optimality without degeneracy.** For \`R>0\`, choose \`lambda(R)=(R,1,\ldots,1)\` with \`n-1\` unit entries and inspect \`i=1\`. Then
\[
\frac{S F_1}{f}
=\frac{(R+n-1)\binom{n-1}{m-1}}
{m\left(R\binom{n-1}{m-1}+\binom{n-1}{m}\right)}
\longrightarrow\frac1m\qquad(R\to\infty).
\]
This covers \`m=n\` by \`\binom{n-1}{n}=0\`. In particular no uniform coefficient exceeding \`1/m\` is possible, even within the positive-definite cone.

The original bound \`F_i >= f/(m! S)\` is **correct but suboptimal**. For \`m>=3\`, (*) improves its right-hand side by the factor \`(m-1)!\`; for \`m=2\` it agrees with the original.

## Precise conditional consequence for §8.4.2

The printed hypothesis on the scalar \`q\` in Lemma 8.4.2 is

\[
q\geq8,\qquad q\geq\frac{2nm!C_H}{f_0},\qquad
q^2\geq\frac{4m!C_G}{f_0}.
\]

Because \`F_i >= f_0/(mS)\`, the proof's **coordinatewise gradient penalty** (physical lines 65–68) remains absorbed when only the last hypothesis is weakened to

\[
\boxed{\displaystyle q^2\geq\frac{4mC_G}{f_0}.}
\]

Indeed, summing over \`i\` yields
\[
\frac{q^2}{4}\sum_iF_i|a_i|^2
\geq\frac{q^2f_0}{4mS}\sum_i|a_i|^2
\geq\frac{C_G}{S}\sum_i|a_i|^2.
\]

**Crucial distinction:** the *other* condition \`q>=2nm!C_H/f_0\` is used for
\[
\frac{C_H}{\lambda_1}|M_{1\bar1}|
\leq\frac{nC_H}{S}\operatorname{tr}M
\leq\frac q2 W_M,
\]
where \`M\` lies in the **full closed Hermitian m-cone**, not necessarily the positive-semidefinite cone. The sharper individual \`F_i\` bound **does not imply** a better \`W_M\` inequality for signed diagonal entries of \`M\`. Consequently, **retain** the \`m!\` coefficient in the \`C_H\` threshold and in the original mixed pairing unless an independent proof establishes an improvement. The rest of the analytic Hessian estimates are not certified by this numerical amendment.

## Reproducible spot checks actually executed

Using exact integer elementary symmetric polynomials and Python \`fractions.Fraction\`, six admissible spectra were verified to satisfy \`min_i S F_i/f >= 1/m\`. Results (dimension, degree, spectrum, exact minimum, target):

| \`n\` | \`m\` | \`lambda\` | \`min_i S F_i/f\` | \`1/m\` |
| ---: | ---: | --- | ---: | ---: |
| 3 | 2 | (5,2,1) | 12/17 | 1/2 |
| 4 | 3 | (7,2,1,1) | 55/111 | 1/3 |
| 5 | 4 | (10,2,1,1,1) | 35/96 | 1/4 |
| 4 | 2 | (5,-1,4,1) | 18/19 | 1/2 |
| 5 | 3 | (8,2,-1,2,2) | 13/22 | 1/3 |
| 6 | 5 | (20,1,1,1,1,1) | 25/101 | 1/5 |

The exact asymptotic test \`lambda=(R,1,...,1)\` also passed at \`R=10,1000,10^6\` for \`(n,m)=(3,2),(4,3),(5,4),(6,5)\`. These are spot checks, **not** a build, CI, browser test, complete mathematical validation, or formalization.

## Adjudication, proposed correction, affected dependents

**Status:** low / verified conditional deduction; **not** a false printed theorem, no mathematical duplication found, and no incomplete analytic proof declared resolved. The independent elementary proof establishes only (*), while the downstream §8.4.2 parameter improvement remains conditional on the same general-cone and background assumptions as the printed lemma.

**Proposed separately reviewable production edit (not performed):** retain both original estimates in Lemma 8.2.5, add (*) as an explicitly distinct **sharper coordinatewise estimate** with its short Newton-ratio proof and asymptotic sharpness; independently replace only the \`C_G\` bound in §8.4.2 by \`4mC_G/f_0\`, and adjust the final explanatory proof line. Preserve source attribution, stable source labels and permanent tags. Dependent locations to reconsider (without an unverified transitive assertion of improvement): §8.4.2 gradient absorption; later Chern/Hermitian trace estimates built from it.

**Coverage:** new direct algebraic proof of the coordinate coefficient step in §8.2.5 and the selected §8.4.2 gradient threshold; selected §8.2.3/.4 deleted-coordinate and symmetric-polynomial prerequisites and §8.2.6 context only. The project has 25 chapters and 747 numbered ToC sections, **none fully mathematically certified**. All previous confirmed errors, proof gaps, external inputs and unresolved/deferred statuses remain unchanged. Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remain **deferred-by-user**, not reopened. No source, registry, canonicalization, permanent-tag, main, site, CI, publication or formalization edit.