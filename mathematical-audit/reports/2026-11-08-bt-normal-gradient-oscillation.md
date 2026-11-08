# A monotone smooth PSH approximation with oscillating normal traces: the Bedford–Taylor energy seminorm is essential

**Stable finding ID:** POME-BT-NORMAL-TRACE-GRADIENT-OSCILLATION-001  
**Severity / classification:** low / verified conditional deduction (sharpness example). **No printed theorem is false.**  
**Date:** 2026-11-08. **Production main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Starting audit head:** `698bbdcd81a1f957375261543e41ab5b09d40ad4`.

**Actual integrated reading edition:** `docs/sections/bedford-taylor-products-and-local-capacity--gradients-against-positive-currents/index.html`, blob `520e13d0d2cc8e4a23e43bba61b940d7c5c1f8b2`. Chapter 7, §7.14 *Gradients against positive currents*, permanent section tag `166A7FDE3C64`. Formula **(7.14.1)**, source `foundations-of-pluripotential-theory:DEE3D747`, permanent tag `9148FE66924C`, physical lines 25–32; **Lemma 7.14.3**, source `foundations-of-pluripotential-theory:3CDA1967`, permanent tag `8B33E7CC2E18`, lines 48–64 and proof lines 69–133 (especially Step 1, lines 71–84, and Step 2, lines 85–100). Formula **(7.14.4)** source `foundations-of-pluripotential-theory:7591087E`, permanent tag `F48E1DFF8563`, lines 50–54.

## Precise new statement

There are an open bidisk (U\subset\mathbb C^2), a positive closed current (\Theta) of bidimension ((1,1)), and **one decreasing sequence** of smooth plurisubharmonic functions (v_k\downarrow v\in\mathrm{PSH}(U)\cap L^\infty_{\mathrm{loc}}(U)), even converging uniformly on compact sets, such that

1. (H^{1/2}\partial v_k=0) identically (\mu)-almost everywhere, where (\mu=\Theta\wedge\beta) and (H) is exactly the coefficient matrix defined in the integrated §7.14;
2. for every compact disk (K\) contained in the support of (\Theta) with (\mu(K)>0), the unweighted ambient gradients (\partial v_k) are **not Cauchy** in (L^2(K,\mu;\mathbb C^2)); their normal coefficients alternate between two distinct constants.

This shows why the printed convergence conclusion of Lemma 7.14.3 **must retain the weight (H^{1/2})**. No unconditional (L^2(\Theta\wedge\beta)) trace of the full ambient gradient can be inferred, even from monotone smooth approximants and locally uniform convergence.

## Complete construction and verification

Work in (U=\{(z,w)\in\mathbb C^2:|z|<1,|w|<1\}), take (L=\{w=0\}), and let (\Theta=[L]) be its integration current. With (\beta=(i/2)(dz\wedge d\bar z+dw\wedge d\bar w)), the trace (\mu=[L]\wedge\beta) is ordinary Euclidean area on the (z)-disk. In the ordered frame ((dz,dw)), §7.14's definition

[
\frac{i}{2\pi}\,dz_j\wedge d\bar z_i\wedge\Theta=h_{ij}\mu
]

gives (H=\operatorname{diag}(1/\pi,0)), (\mu)-almost everywhere: the (dz\wedge d\bar z) term is ((1/\pi)\mu), while any term containing (dw) vanishes after restriction to (L).

Let (m_k=4^k), (t=\operatorname{Re}w), and choose integers
[
(a_k,b_k)=
\begin{cases}
(1,3),&k\text{ odd},\\
(3,1),&k\text{ even}.
\end{cases}
qquad
v_k(z,w)=\frac1{m_k}\log\!\left(e^{a_k}+e^{b_k+m_k t}\right).
]

Every (v_k) is smooth and PSH: it is the composition of (t=\operatorname{Re}w), a pluriharmonic function, with the convex function (s\mapsto m_k^{-1}\log(e^{a_k}+e^{b_k+m_k s})). Its second derivative is nonnegative, so (dd^cv_k\ge0). Moreover,
[
\max\left\{\frac{a_k}{m_k},t+\frac{b_k}{m_k}\right\}
\le v_k\le
\max\left\{\frac{a_k}{m_k},t+\frac{b_k}{m_k}\right\}+\frac{\log2}{m_k}.
]
Consequently (v_k\to v(z,w)=\max\{0,\operatorname{Re}w\}) **locally uniformly**.

The **monotonicity** is not an assumption: set
[
\Phi_T(A,B;t)=T\log(e^{A/T}+e^{(t+B)/T}).
]
It is increasing in (A) and (B). For fixed (A,B,t), direct differentiation shows
[
\frac{\partial\Phi_T}{\partial T}
=-p\log p-(1-p)\log(1-p)\ge0,qquad
p=\frac{e^{(t+B)/T}}{e^{A/T}+e^{(t+B)/T}}.
]
At stage (k) use (T_k=1/m_k, A_k=a_k/m_k,B_k=b_k/m_k). Since (1\le a_k,b_k\le3) and (m_{k+1}=4m_k), **all three** parameters (T_k,A_k,B_k) strictly decrease. Thus (v_{k+1}=\Phi_{T_{k+1}}(A_{k+1},B_{k+1};t)\le\Phi_{T_k}(A_k,B_k;t)=v_k) at every point.

There is no tangential derivative: (\partial_zv_k=0), and
[
\partial_wv_k(z,0)=\frac12\frac{e^{b_k}}{e^{a_k}+e^{b_k}}=
\begin{cases}
\frac12\frac{e^2}{1+e^2},&k\text{ odd},\\
\frac12\frac1{1+e^2},&k\text{ even}.
\end{cases}
]
Therefore, on every positive-area compact disk (K\subset L\cap U),
[
\|\partial v_{k+1}-\partial v_k\|_{L^2(K,\mu)}
=\frac{\tanh1}{2}\,\mu(K)^{1/2}>0
]
for all (k). On the other hand, (H^{1/2}\partial v_k=0) on (L) **for every (k)**. In fact (v_k|_L=m_k^{-1}\log(e^{a_k}+e^{b_k})) is constant, so its relative gradient measure (dv_k\wedge d^cv_k\wedge[L]) vanishes exactly. The limit (v|_L=0) also has zero relative gradient energy by the printed definition and monotone-continuity lemma.

Hence the energy-seminorm convergence asserted in Lemma 7.14.3 holds (trivially here), while the stronger unweighted full-gradient convergence fails along a **single** monotone smooth approximation sequence. All constants and the alternating lower bound are exact.

## Logical classification, dependencies and follow-up

- **Verified conditional deduction / sharpness, low.** The integrated Lemma 7.14.3 and formula (7.14.1) are **not refuted**. No proposed correction to either statement is required.
- **Optional addition:** a short warning after the convergence clause of Lemma 7.14.3, or near its first use in Theorem 13.3.1, that the current may have zero response to normal gradients and that even monotone smooth approximants need not converge in the unweighted trace-(L^2) norm.
- **Affected dependents:** §13.3.1 (closedness of non-pluripolar products), and any cutoff/product proof that would silently replace (H^{1/2}\partial v_k\to H^{1/2}\partial v) by unweighted ambient-gradient convergence. This report does **not** establish that any such invalid strengthening actually appears in a downstream proof.
- **Inputs:** the concrete integration current of a complex line, elementary log-sum-exp convexity/entropy identity, and the exact matrix/energy definitions from §7.14. No Demailly approximation/regularization, Bergman, weighted-(L^2), Ohsawa–Takegoshi or positivity-loss programme is used. The full dependency chain of Lemma 7.14.3 and Theorem 13.3.1 remains **not certified**.
- **Coverage:** first directly documented theorem-level review of §7.14 in the current broad-scope ledger; selected lines and one sharpness claim, **not an entire section**, not a chapter, and not a proof-chain certification. Main ToC 25 chapters / 747 numbered sections / 0 fully mathematically certified sections.
- **Change boundary:** proposed audit commentary only. No main/source bodies, registries, canonicalization, permanent tags, CI/builds, formalization, website or source attribution changed. All owner-excluded approximation work remains **deferred-by-user**, not resolved.
