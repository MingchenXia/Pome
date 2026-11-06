# Exact Gauduchon multipliers and adjoint probabilities for one-variable diagonal Hermitian tori

**Date:** 2026-11-06. **Finding:** \`POME-GAUD-ONEVARIABLE-DIAGONAL-CONFORMAL-BALANCED-001\`. **Severity:** low. **Status:** verified conditional deduction (standalone exact model, not a proof of Gauduchon's theorem in general). **Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.

## Integrated mathematical anchors

- \`docs/sections/gauduchon-metrics-and-linear-mass--conformal-gauduchon-metrics/index.html\` at main blob \`ecb4bf9e593dfb25f1644f0561d1aa65bf096b10\`, physical lines **11–15** (Definition 11.4.1, source \`non-kahler-pluripotential-theory:DD74A88E\`, permanent tag \`70139B6ABDC2\`) and **20–58** (Theorem 11.4.2, source \`non-kahler-pluripotential-theory:F1B1A709\`, permanent tag \`3978AEB15BD7\`; especially displayed equation line 22 and the adjoint equation lines 33–56).
- \`docs/sections/gauduchon-metrics-and-linear-mass--conservation-of-the-trace-mass/index.html\` at main blob \`34af83ff391b5e5590cd9cb10ca4cd2b3faff02c\`, physical lines **11–30** (Proposition 11.5.1, source \`non-kahler-pluripotential-theory:0D4A42C8\`, permanent tag \`828FAD1A35BF\`) as a *contextual* trace-mass comparison; it is not used to prove the model.
- \`docs/sections/conventions/index.html\`, blob \`ef778e54d8d7413242387e95c52269b3c7d42cae\`: global connected compact convention; \`dd^c=i/(2π)∂\bar∂\`. Chapter 11 assumes complex dimension \(n\ge2\). No smoothing or Demailly results are invoked.

## Exact statement

Let \(n\ge2\) and
\[
 X=(\mathbb C/(\mathbb Z+i\mathbb Z))^n,\qquad
 \beta_j=\frac{i}{2\pi}\,dz_j\wedge d\bar z_j,\qquad
 \Omega=\beta_1\wedge\cdots\wedge\beta_n.
\]
Write \(z_j=x_j+iy_j\). For arbitrary strictly positive smooth one-periodic real functions \(a_1,\ldots,a_n\) of **only \(x_1\)**, put
\[
 \eta=\sum_{j=1}^n a_j(x_1)\beta_j,\qquad
 A(x_1)=\prod_{j=2}^n a_j(x_1),\qquad
 \rho_0(x_1)=A(x_1)^{-1}.
\]
Then:

1. The *only* smooth positive solutions of \(dd^c(\rho\eta^{n-1})=0\), **without assuming that \(\rho\) depends on \(x_1\)**, are \(\rho=C\rho_0\) for constants \(C>0\).
2. The resulting conformal Gauduchon metric \(\gamma_0=\rho_0^{1/(n-1)}\eta\) is actually **balanced**: \(d(\gamma_0^{n-1})=0\). The original \(\eta\) is not in general Gauduchon or closed.
3. The normalized positive generator of the formal adjoint kernel for \(Lv=n\,dd^cv\wedge\eta^{n-1}/\eta^n\) has probability measure
\[
 \nu=\frac{\rho_0\eta^n}{\int_X\rho_0\eta^n}
     =\frac{a_1(x_1)\Omega}{\int_Xa_1(x_1)\Omega}.
\]
In particular, the adjoint probability is completely **independent** of \(a_2,\ldots,a_n\); if \(a_1=1\) it is Haar measure even when the background has nonzero torsion.

These are explicit realizations and an independent uniqueness calculation for the restricted family, *not* counterexamples to Theorem 11.4.2. The word “conditional” in the ledger reflects that the reviewed general theorem and its entire elliptic Fredholm prerequisite chain are not certified by this model.

## Proof and normalization checks

Since all two-forms \(\beta_j\) commute and \(\beta_j^2=0\),
\[
 \eta^{n-1}=(n-1)!\sum_{k=1}^n
    \left(\prod_{j\ne k}a_j\right)
    \beta_1\wedge\cdots\widehat{\beta_k}\cdots\wedge\beta_n.
\]
The prescribed \(dd^c\) convention gives, for any smooth \(f=f(x_1)\),
\[
 d^cf=\frac{f'(x_1)}{4\pi}\,dy_1,\qquad
 dd^cf=\frac{f''(x_1)}4\,\beta_1.
\]
Consequently, every \(k\ne1\) term in \(dd^c(\rho_0\eta^{n-1})\) vanishes because it already contains \(\beta_1\); the \(k=1\) term gives
\[
 dd^c(\rho_0\eta^{n-1})
 =\frac{(n-1)!}{4}\,(\rho_0 A)''\Omega=0.
\]
More strongly,
\[
 d(\rho_0\eta^{n-1})
 =(n-1)!(\rho_0 A)'\,dx_1\wedge\beta_2\wedge\cdots\wedge\beta_n=0.
\]
Thus the conformal representative is balanced.

For **arbitrary** smooth positive \(\rho\), let \(s=\rho/\rho_0\). If also \(dd^c(\rho\eta^{n-1})=0\), write \(B=\rho_0\eta^{n-1}=\gamma_0^{n-1}\). As \(B\) is closed and has pure bidegree \((n-1,n-1)\), both \(dB\) and \(d^c B\) vanish, so
\[
 0=dd^c(sB)=dd^cs\wedge B.
\]
The scalar operator \(s\mapsto n\,dd^cs\wedge\gamma_0^{n-1}/\gamma_0^n\) is real uniformly elliptic with positive definite principal symbol and zero zeroth-order term. On the **connected compact** torus, its maximum principle forces \(s\) to be constant. This proves uniqueness among all positive multipliers, with no symmetry assumption and no invocation of the general adjoint-kernel theorem.

For the probability claim,
\[
 \eta^n=n!\,a_1 A\,\Omega,\qquad
 \rho_0\eta^n=n!\,a_1\Omega.
\]
Furthermore, Stokes applied to the closed \(B\) yields
\[
 \int_X \rho_0 Lv\,\eta^n
    =n\int_Xdd^cv\wedge B=0
\]
for every smooth \(v\). Therefore the normalized measure \(\nu\) above is an invariant adjoint probability. The same ratio argument proves uniqueness of the strictly positive adjoint density. No integration sign or \(n!\) discrepancy remains in the normalized probability.

As an explicit nonclosed family, take \(a_1=1\), \(a_2=2+\cos(2\pi x_1)\), and \(a_j=1\) for \(j\ge3\). Then
\[
 d\eta=a_2'(x_1)\,dx_1\wedge\beta_2\ne0,\quad
 dd^c(\eta^{n-1})=\frac{(n-1)!}{4}a_2''\Omega\not\equiv0,
\quad \rho_0=a_2^{-1}.
\]
Here \(\nu=\Omega/\int_X\Omega\). When \(n=2\), \(\gamma_0=\beta_2+a_2^{-1}\beta_1\) is Kähler. When \(n\ge3\), \(\gamma_0\) is balanced but not Kähler: the coefficients of \(\beta_j\) for \(j\ge3\) are \(a_2^{-1/(n-1)}\) and their \(x_1\)-derivatives contribute nonzero terms to \(d\gamma_0\).

## Classification, correction, and dependents

**Finding \`POME-GAUD-ONEVARIABLE-DIAGONAL-CONFORMAL-BALANCED-001\`: low / verified conditional deduction.** The printed theorem and its uniqueness and positivity hypotheses are compatible with this family; **no mathematical error was found** here. The recommended correction is **none**. An optional independently reviewable exposition could record this one-variable diagonal formula after Theorem 11.4.2, preserving its provenance and existing permanent tags. The example can act as a consistency test for Gauduchon duality and for the probability normalization in §§11.23–11.25; those sections, the general Fredholm argument, and their analytic dependencies are *not* certified by this calculation. All prior ledger classifications and deferred-by-user exclusions remain intact.

**Actual coverage:** first model-specific inspection of Definition 11.4.1 and Theorem 11.4.2, with only a contextual read of Proposition 11.5.1 and the global conventions. Did not review the whole §11.4 or §11.5, test software, build the project, perform browser rendering, or publish anything. No regularization/Bergman/weighted-L²/OT/multiscale/positivity-loss proof work was undertaken.
