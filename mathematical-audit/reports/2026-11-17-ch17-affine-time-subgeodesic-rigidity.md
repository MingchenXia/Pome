# 2026-11-17: Affine-time subgeodesics are necessarily scalar translations

**Finding ID:** \`POME-GEO-TIME-AFFINE-SUBGEODESIC-RIGIDITY-001\`  
**Classification:** low / **verified conditional deduction**; not a false theorem, proof repair or full theorem-chain certification.  
**Reviewed main SHA:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`  
**Integrated reading-edition path:** \`docs/sections/relative-energy-and-perron-segments--subgeodesics-and-perron-segments/index.html\`  
**Blob:** \`662f60d73fc585b6ea3b710f2a3472bac1de8a7c\`

**Direct anchors.** Introduction (physical lines 7–10), source \`foundations-of-pluripotential-theory:E622ECE7\`, permanent tag \`4C4B950F1CFF\`; Definition 17.7.1 (lines 14–19), source \`foundations-of-pluripotential-theory:15664095\`, permanent tag \`B0604A42ABDF\`. Context only: Lemma 17.7.5 (lines 141–147), source \`foundations-of-pluripotential-theory:A9FC390C\`, tag \`F4AAE999A6C4\`; Theorem 17.7.8 (lines 185–208), source \`foundations-of-pluripotential-theory:108758A0\`, tag \`2FECBE87C487\`.

## Exact assertion

Let \(X\) be a **connected** complex manifold, let \(\theta\) be a smooth **closed real** \((1,1)\)-form, and let \(u_0,u_1\in\operatorname{PSH}(X,\theta)\) be genuine (not identically \(-\infty\)) potentials. The literal affine interpolation
\[
 u_t=(1-t)u_0+t u_1,\qquad 0<t<1,
\]
has jointly \(p^*\theta\)-psh complexification
\[
 U(x,\zeta)=(1-\operatorname{Re}\zeta)u_0(x)
             +(\operatorname{Re}\zeta)u_1(x),
 \qquad S=\{0<\operatorname{Re}\zeta<1\}
\]
**if and only if** \(u_1=u_0+c\) for some global real constant \(c\).

On disconnected \(X\), replace one constant by a constant on each connected component. No bigness, model-potential hypothesis, compactness, Kähler positivity or smoothness of either potential is needed for this *joint positivity equivalence*. When \(X\) is compact, the affine family automatically has the required \(L^1\) endpoint limits and is a subgeodesic in the exact sense of Definition 17.7.1.

A nonconstant-difference weak geodesic from Theorem 17.7.8 therefore cannot itself be affine in the time variable. This is **not** a claim that the existence theorem for weak geodesics has been reproved.

## Proof, valid even with singular potentials

Since \(\theta\) is smooth and closed, locally it has a smooth potential. Work on a coordinate ball \(D\subset X\), where \(\theta=dd^c h\), and let
\[
 f=u_1-u_0\in L^1_{\mathrm{loc}}(D,\mathbb R).
\]
This difference is defined almost everywhere and is used as a distribution; no expression subtracting the values \(-\infty\) at common poles is used.

Joint positivity says that \(H=h\circ p+U\) is psh on \(D\times S\); hence its complex Hessian is a positive Hermitian matrix of measure coefficients. Distributionally,
\[
 H=h+u_0+(\operatorname{Re}\zeta)f,\qquad
 \partial_\zeta\partial_{\bar\zeta}H=0,\qquad
 \partial_{z_j}\partial_{\bar\zeta}H
     =\frac12\partial_{z_j}f.
\]
The local smooth \(h\) contributes neither mixed term nor transverse term. The proportionality factor defining \(dd^c\) does not affect the argument.

**Positive-current zero-diagonal lemma.** Suppose \(T=(T_{\alpha\bar\beta})\) is a positive Hermitian matrix of complex Radon measures with \(T_{\zeta\bar\zeta}=0\). For every nonnegative compactly supported smooth test function \(\chi\), positivity makes
\[
 \big(\langle T_{\alpha\bar\beta},\chi\rangle\big)_{\alpha,\beta}
\]
a positive semidefinite Hermitian matrix. Cauchy–Schwarz yields
\[
 \left|\langle T_{j\bar\zeta},\chi\rangle\right|^2
 \le \langle T_{j\bar j},\chi\rangle
     \langle T_{\zeta\bar\zeta},\chi\rangle=0.
\]
By linearity and decomposition of arbitrary real test functions into differences of nonnegative tests, the mixed measure is zero as a distribution.

Applying the lemma to \(dd^c H\) shows \(\partial_{z_j}f=0\) distributionally on \(D\) for every \(j\). Because \(f\) is real, \(\bar\partial f=0\) as well. Thus \(df=0\), so \(f\) is a constant almost everywhere on each connected chart. Constants agree on overlaps. Connectedness gives one global \(c\). Since \(u_0\) and \(u_1\) are \(\theta\)-psh representatives and \(u_1=u_0+c\) almost everywhere, the identity holds everywhere as an identity of extended-valued psh functions.

Conversely, if \(u_1=u_0+c\), then
\[
 U(x,\zeta)=u_0(x)+c\operatorname{Re}\zeta.
\]
The second term is pluriharmonic. Therefore
\[
 p^*\theta+dd^c U=p^*(\theta+dd^c u_0)\ge0.
\]
This proves the equivalence.

## Sharp comparison with the printed smooth example

Let \(X\) be compact Kähler, \(\theta\) Kähler, and \(g\) a nonconstant real smooth function. For sufficiently small \(\varepsilon>0\), \(\theta+t\varepsilon dd^c g>0\) for every \(t\in[0,1]\). Thus \(u_0=0\), \(u_1=\varepsilon g\) yield a family \(u_t=t\varepsilon g\) with all slices \(\theta\)-psh and each function \(t\mapsto u_t(x)\) affine. Yet the family is not a subgeodesic, since \(u_1-u_0\) is not constant. This verifies and generalizes the introductory source example, without providing a counterexample to any printed result.

## Classification, dependencies, and coverage

- **Status and severity:** low / **verified conditional deduction**. This is a self-contained implication of joint positive-current definitions, conditional only on their standing hypotheses. It is **not** a general geodesic existence proof.
- **Source status:** the printed introductory example, Definition 17.7.1, Lemma 17.7.5 (which preserves **scalar** affine shifts), and Theorem 17.7.8 remain correct under this check. No source theorem has been refuted.
- **Optional proposed addition (not applied):** append this criterion after the introductory smooth mixed-Hessian computation, to prevent incorrect replacement of Perron geodesics by literal endpoint interpolation.
- **Potential downstream audit targets:** §§17.7–17.9, where geodesic energy affinity must not be confused with pointwise affine interpolation. No existing downstream theorem is declared erroneous.
- **Actual coverage:** §17.7 introductory mixed-Hessian argument and Definition 17.7.1 directly inspected and independently extended; Lemma 17.7.5 and Theorem 17.7.8 consulted for hypotheses only. Prior selected §17.7 review is preserved. Newly first-visited numbered sections **0**; fully certified sections **0**.
- **Excluded scope:** dedicated Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale atlas and positivity-loss proof-completion work remains **deferred-by-user, not resolved or certified**; no excluded premise was used.
- **Not performed:** project build, test suite, CI, formal verification, main/source/registry modification, or website publication.
