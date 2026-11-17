# 2026-11-17: Affine-time subgeodesics are necessarily scalar translations

**Finding ID:** `POME-GEO-TIME-AFFINE-SUBGEODESIC-RIGIDITY-001`  
**Classification:** low; **verified conditional deduction** (not a false printed theorem, not a repair, not a full proof-chain certification).  
**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`  
**Integrated reading-edition file:** `docs/sections/relative-energy-and-perron-segments--subgeodesics-and-perron-segments/index.html`  
**Integrated blob:** `662f60d73fc585b6ea3b710f2a3472bac1de8a7c`  
**Direct anchors:** §17.7 introduction, physical lines 7–10, source `foundations-of-pluripotential-theory:E622ECE7`, permanent tag `4C4B950F1CFF`; Definition 17.7.1, physical lines 14–19, source `foundations-of-pluripotential-theory:15664095`, tag `B0604A42ABDF`; Lemma 17.7.5, lines 141–147, source `foundations-of-pluripotential-theory:A9FC390C`, tag `F4AAE999A6C4`; Theorem 17.7.8, lines 185–208, source `foundations-of-pluripotential-theory:108758A0`, tag `2FECBE87C487` (downstream context only).

## Statement and precise scope

Let (X) be a **connected** complex manifold and (	heta) any smooth **closed real** ((1,1))-form such that (operatorname{PSH}(X,	heta)) contains two potentials (u_0,u_1), neither identically (-infty). Suppose the affine interpolation
[
 u_t=(1-t)u_0+t u_1,quad 0<t<1,
]
is a subgeodesic in the joint sense: its complexification
[
 U(x,zeta)=(1-operatorname{Re}zeta)u_0(x)
             +(operatorname{Re}zeta)u_1(x)
]
is (p^*	heta)-plurisubharmonic on (X	imes S), (S={0<operatorname{Re}zeta<1}).
Then
[
 oxed{u_1=u_0+cquad	ext{on }X	ext{ for a real constant }c.}
]
Conversely, every pair differing by a real constant gives such an affine subgeodesic. On a disconnected space the conclusion holds with one constant on each connected component. The result needs neither compactness, bigness, Kähler positivity, model singularity types, nor smoothness of the potentials.

If a weak geodesic of §17.7.8 is affine in the time variable in precisely this sense, its endpoints differ by a constant. This is a *necessary condition* for time-affinity, not a claim that arbitrary linear interpolation is jointly psh.

## Direct proof (including unbounded singular potentials)

All arguments are local in the (X)-variable. Work on a coordinate ball (D) on which (	heta=dd^c h) with (h) smooth, and put (f=u_1-u_0in L^1_{mathrm{loc}}(D,mathbb R)) (an a.e.-defined distribution). The function (H=hcirc p+U) is psh on (D	imes S), so (dd^cH) is a positive Hermitian matrix of measure-valued ((1,1))-coefficients. No smoothing of singular potentials is used.

As a distribution, (U=u_0+(operatorname{Re}zeta)f). The transverse entry of its complex Hessian vanishes:
[
 partial_zetapartial_{arzeta}H=0.
]
For each local coordinate (z_j), the mixed entry is
[
 partial_{z_j}partial_{arzeta}H
       =	frac12partial_{z_j}f
       quad 	ext{in }mathcal D'(D	imes S).
]
The (h)-term contributes no mixed derivative.

Here is the measure-theoretic positivity step, rather than an unjustified pointwise matrix calculation. If (T=(T_{alphaareta})) is any positive Hermitian matrix of complex Radon measures and (T_{zetaarzeta}=0), then (T_{jarzeta}=0). Indeed for every compactly supported nonnegative test function (chi), the finite matrix ((langle T_{alphaareta},chiangle)) is positive semidefinite; Cauchy–Schwarz gives
[
 |langle T_{jarzeta},chiangle|^2
 leq langle T_{jar j},chiangle
       langle T_{zetaarzeta},chiangle=0.
]
By testing real and imaginary parts against differences of nonnegative functions, the mixed measure vanishes as a distribution. (The common normalization factor in (dd^c) is immaterial.)

It follows that (partial f=0) in (mathcal D'(D)). Since (f) is real, also (arpartial f=0); therefore (df=0), and (f) is a constant almost everywhere on (D). The constants agree on overlapping charts and, by connectedness, define a global constant (c). Since (u_0,u_1) are (	heta)-psh representatives, equality (u_1=u_0+c) almost everywhere implies equality everywhere as extended-valued psh functions (locally add a common smooth potential and use uniqueness of the psh representative).

Conversely (u_1=u_0+c) gives (U=p^*u_0+coperatorname{Re}zeta). The second summand is pluriharmonic; hence (p^*	heta+dd^cU=p^*(	heta+dd^cu_0)geq0). The obvious endpoint (L^1) convergence also holds on compact (X), completing the equivalence in Definition 17.7.1.

## Strict distinction from separately psh affine slices

Take any compact Kähler (X), a smooth real nonconstant (g), and (arepsilon>0) sufficiently small that (	heta+arepsilon dd^cg>0). For (u_0=0), (u_1=arepsilon g), each (u_t=tarepsilon g) is (	heta)-psh and pointwise affine in (t); nevertheless it is **not** a subgeodesic, because (u_1-u_0) is nonconstant. This extends the *smooth* local countercheck in the printed introductory paragraph (lines 7–10) to arbitrary singular endpoint pairs, without making a counterexample to any printed proposition.

## Audit classification and dependents

- **Status:** verified conditional deduction; **severity:** low. The statement is proved under the explicit joint-current positivity premise defining a subgeodesic; general existence of geodesics is **not** part of this proof.
- **Printed results:** no error found in the introductory example, Definition 17.7.1, Lemma 17.7.5 or Theorem 17.7.8; the latter is a downstream use only.
- **Suggested optional reading-edition addition (NOT applied):** append the general affine-time rigidity criterion after the introductory smooth mixed-Hessian example. It prevents an invalid substitution of affine interpolation for the Perron subgeodesic in arguments using §17.7.8 and §17.8 energy affinity.
- **Affected dependents for future checks:** §§17.7–17.9 (weak geodesics, energy affinity and slope arguments); no specific existing downstream proof has been shown false.
- **Inputs:** distributional characterization of positive psh currents and uniqueness of psh representatives; no Demailly regularization, Bergman, L², Ohsawa–Takegoshi, multiscale atlas, or positivity-loss proof programme.
- **Coverage:** direct selected scrutiny of §17.7's opening mixed-Hessian argument and Definition 17.7.1, with Lemma 17.7.5 / Theorem 17.7.8 read for compatibility only. The earlier §17.7 selected proofs are preserved. **0 newly first-visited sections; 0 entire sections certified.** Other sections, all unresolved historical findings, and deferred-by-user notes retain their existing statuses.
- **Not performed:** no project build, software test suite, CI, formal verification, source/body/registry update, or publication.
