# Sharp determinant-to-cofactor ellipticity for equal Monge–Ampère measures

- **Finding ID:** \`POME-MA-POLARIZED-COFACTOR-OPTIMAL-001\`
- **Date:** 2026-11-14
- **Classification:** low / **verified conditional deduction** (a complete pointwise algebraic supplement, conditional only when used downstream in the PDE arguments). **No printed theorem or proof is refuted.**
- **Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
- **Scope:** precise selected proof/algebraic interface in §§14.20–14.22, not complete-section certification; Demailly approximation, regularization, Bergman, weighted L², Ohsawa–Takegoshi, multiscale and positivity-loss programmes are **deferred-by-user** and not used here.

## Original integrated statements and exact anchors

1. \`docs/sections/uniqueness-for-degenerate-equations/index.html\` (main blob \`0c1c033d7a1a76b9ccf9fbd5b4bfc8321a33f208\`), physical lines **10–23**: \`T = sum_{j=0}^{n-1} A^j wedge B^{n-1-j}\` and equation **14.20.1**, source label \`non-kahler-pluripotential-theory:AA4FA8E3\`, permanent tag \`2EA7CA32AE91\`.
2. \`docs/sections/uniqueness-for-degenerate-equations--extrema-and-density-sublevels/index.html\` (main blob \`044f55457f10b2f640052854a7f5f14b8403be82\`), lines **10–24**: equal determinant condition (equation **14.21.1**, source \`non-kahler-pluripotential-theory:84F3F379\`, permanent \`93A49A38E101\`); lines **27–43**: Theorem **14.21.3**, source \`non-kahler-pluripotential-theory:61B8DD0F\`, permanent \`6EB399397505\`; lines **109–131**: equations **14.21.7**, **14.21.8**, **14.21.9**, source labels \`445DEDC5\`, \`BDBE4297\`, \`A73BA233\`, permanent tags \`57588F1C3107\`, \`144125DEDD1C\`, \`CEEE110C45FE\`; lines **165–170**: use of the qualitative cofactor ellipticity estimate.
3. \`docs/sections/uniqueness-for-degenerate-equations--polarized-cofactors-and-propagation/index.html\` (main blob \`56645140ee2a5e1f97f3288e31ad9a48161e73e5\`), lines **13–29**: Theorem **14.22.1** (source \`non-kahler-pluripotential-theory:DC121A4C\`, permanent \`919310C73DBE\`), lines **79–105**: symbol equations **14.22.9–10** (source \`500F61C6\`, \`9A3B77CC\`; permanent \`04DC9E828E52\`, \`7A7369E544A8\`). This page is used only to identify a dependent; its propagation proof is not certified here.

## Statement (sharp universal coefficient)

Let \(\beta\) be a positive Hermitian \((1,1)\)-form on a complex vector space of dimension \(n\ge2\). Let \(A,B\) be semipositive Hermitian \((1,1)\)-forms with
\[
 A^n=B^n=F\,\beta^n,\qquad 0\le A,B\le L\beta,\qquad L>0,
\]
where \(F\ge0\) is the *relative determinant*, and put \(T=\sum_{j=0}^{n-1} A^j\wedge B^{n-1-j}\), with **no binomial coefficients**. Then, for every \((1,0)\)-covector \(\alpha\),
\[
\boxed{\quad
 \frac{\mathrm i\,\alpha\wedge\bar\alpha\wedge T}{\beta^n}
 \ \ge\ \frac{F}{L}\,|\alpha|_\beta^2 .
 \quad} \tag{*}
\]
The coefficient **1** is optimal in every dimension \(n\ge2\), including for \(A=B>0\). The power **one in \(F\)** is optimal as \(F\downarrow0\) with \(L\) fixed.

This is a new quantitative supplement to the printed qualitative comparison in (14.21.8–9), *not* a correction to it.

## Complete pointwise proof

When \(F=0\), every mixed product in \(T\) is nonnegative, so (*) is immediate. Suppose \(F>0\), hence \(A,B\) are positive definite. Fix \(\alpha\ne0\). In a \(\beta\)-unitary frame take \(\alpha=|\alpha|_\beta\,dz_1\), and denote by \(A_E,B_E\) the positive definite \((n-1)\times(n-1)\) principal compressions on the complementary coordinate hyperplane. Put \(d=n-1\). The complementary principal-minor identity (Schur complement or the inverse-matrix cofactor formula) gives
\[
 \det A_E=\det A\,(A^{-1})_{11}
 \ge F/L,\qquad
 \det B_E=\det B\,(B^{-1})_{11}\ge F/L.
\]
Indeed \(\det_\beta A=\det_\beta B=F\) and \(A^{-1},B^{-1}\ge L^{-1}I\).

For \(0\le j\le d\), define the *normalized* mixed determinant by
\[
 \det(B_E+tA_E)=
 \sum_{j=0}^d {d\choose j}D_j(A_E,B_E)t^j.
\]
Diagonalize \(B_E^{-1/2}A_E B_E^{-1/2}\), with eigenvalues
\(\lambda_1,\ldots,\lambda_d>0\). Then
\[
 D_j(A_E,B_E)=\det B_E\,
 \frac{e_j(\lambda_1,\ldots,\lambda_d)}{{d\choose j}}.
\]
The elementary arithmetic–geometric mean inequality on the \({d\choose j}\) positive \(j\)-fold products gives
\[
 \frac{e_j(\lambda)}{{d\choose j}}
 \ge\bigl(\lambda_1\cdots\lambda_d\bigr)^{j/d},
\]
since each \(\lambda_i\) occurs in exactly \({d-1\choose j-1}\) products. For \(j=0\), this is equality by convention. Consequently
\[
 D_j(A_E,B_E)
 \ge (\det A_E)^{j/d}(\det B_E)^{(d-j)/d}
 \ge F/L. \tag{1}
\]
No external mixed-discriminant or Alexandrov–Fenchel theorem is invoked.

The coefficient comparison in
\(\mathrm i\alpha\wedge\bar\alpha\wedge(B+tA)^d\)
and
\(\det(B_E+tA_E)\) gives the **exact normalization**
\[
 \frac{\mathrm i\alpha\wedge\bar\alpha\wedge A^j B^{d-j}}
      {\beta^n}
 =\frac{|\alpha|_\beta^2}{n}\,D_j(A_E,B_E);
\]
the factor \(1/n=(n-1)!/n!\) arises from the unnormalized wedge powers. Summing the \(n=d+1\) terms and applying (1) proves (*).

To see *sharpness*, take \(\beta=\mathrm i\sum_{k=1}^n dz_k\wedge d\bar z_k\),
\(A=B=\mathrm i(\varepsilon\,dz_1\wedge d\bar z_1+
L\sum_{k=2}^n dz_k\wedge d\bar z_k)\) with \(0<\varepsilon\le L\), and take \(\alpha=dz_2\). Here \(F=\varepsilon L^{n-1}\), \(T=nA^{n-1}\), and a direct wedge calculation yields
\[
 \frac{\mathrm i\,dz_2\wedge d\bar z_2\wedge T}{\beta^n}
 =\varepsilon L^{n-2}=F/L.
\]
Thus constant \(1\) cannot be increased, nor can the linear dependence on \(F\) be replaced by a better universal vanishing exponent. The forms are smooth and locally realized as \(\omega+\mathrm{dd}^{\mathrm c}u=\omega+\mathrm{dd}^{\mathrm c}v=A\) by choosing suitable quadratic potentials; **no global compact solution is asserted**.

## Consequence and exact limitations

With the original condition \(A^n=B^n=f\,\mathrm dV\), one has \(F=f\,(\mathrm dV/\beta^n)\). If on a relatively compact chart the measurable \(C^{1,1}\) Hessians obey \(A,B\le L\beta\) a.e. and \(F\ge F_0>0\), then
\[
 Q_\beta(\xi)=
 \frac{\mathrm i\,\xi^{1,0}\wedge\overline{\xi^{1,0}}\wedge T}{\beta^n}
 \ge (F_0/L)|\xi^{1,0}|_\beta^2
\]
a.e. This makes the *local lower ellipticity constant explicit* in the positivity region used by Theorem 14.21.3. The real-coordinate symbol of (14.22.9–10) differs by its fixed \(dd^{\mathrm c}\)-normalization factor; no quantitative Harnack or global uniqueness estimate follows without further hypotheses.

At \(F=0\), (*) is only \(Q\ge0\). The **previously recorded** complementary-rank example \`POME-MA-COFACTOR-ZERO-DENSITY-001\` can still have strictly positive \(Q\) at zero determinant; the present sharp lower bound neither repeats nor contradicts that example. It also does not assert TV convergence, higher regularity or uniform ellipticity across a degenerate zero set.

**Dependents and proposed action:** retain the original correct Theorem 14.21.3 and equations 14.21.7–9; optionally add the sharp estimate as a separately reviewable mathematical supplement to the proof of \(U\subset E_{\rm unif}\), and as a quantitative context note for §14.22.1/.9–10. No source/body/registry/permanent-tag edit made.

**Certification boundary:** the matrix inequalities above are proved completely; Theorem 14.21.3's upper-contact and measurable strong-maximum-principle proof, and Theorem 14.22.1's propagation theorem and global dependency graph, are **not** transitively certified. No project builds, tests, CI, website publication, or formal proof checks were run.
