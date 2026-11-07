# Critical heat-trace duality: sharp $L^p$ operator rate versus fixed-test little-o (2026-11-08)

**Stable finding ID:** `POME-HEAT-CRITICAL-LP-DUAL-RATE-001`. **Severity/status:** **low / verified conditional deduction**. No printed theorem is refuted; this is neither a proof-gap resolution nor a complete certification of heat-kernel theory.

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (freshly checked).
**Integrated reading edition:** `docs/sections/heat-kernels-on-compact-manifolds/index.html`, Git blob `c59a1b3fab9433f1aae95db99adb4821857b5d8d`.
**Section:** Chapter 3, §3.10, section permanent tag `B8A97FFD89FE`, provenance section `transcendental-positive-cones:FD9C3E46`.
**Direct printed anchors:** Lemma 3.10.5, source `transcendental-positive-cones:DD00B1CA` / permanent tag `56A174D59425`, **physical HTML lines 83–105**, especially statement 85–92 and annular/truncation proof 98–105. Supporting Lemma 3.10.1, source `transcendental-positive-cones:327DDB8B` / permanent `126365F8EBD6`, physical lines 10–13 and Gaussian-estimate proof 19–79. The printed nonnegative heat semigroup is `h_t=e^{-t d^*d}` with Riemannian volume `dV`.

## Statement and scope

Let `(X,g)` be a compact smooth real `m`-manifold, `m>=2`, and let `rho` be a finite positive measure satisfying precisely the hypothesis of printed Lemma 3.10.5:
```math
\rho(B_r(x))\le A r^{m-2}\quad\text{for all }x\in X,\quad 0<r\le r_0.
```
Write `M=rho(X)` and `B=C_{g,r_0}(A+M)`. In the convention `g_t=t h_t rho`, the printed estimate and heat-mass conservation are
```math
0\le g_t\le B,\qquad \int_X g_t\,dV=tM,\qquad 0<t\le1.
```
The following additional assertion is exact: for each `1<p<infinity`, write `q=p/(p-1)`. Then
```math
\boxed{\sup_{\|F\|_{L^p}\le 1}\left|t\int_X F(h_t\rho)\,dV\right|
=\|g_t\|_{L^q}
\le B^{1/p}M^{1-1/p}t^{1-1/p}.}\tag{A}
```
For **every fixed, possibly signed** `F in L^p(X,dV)`, the strictly stronger statement holds:
```math
\boxed{t\int_X F(h_t\rho)\,dV=o(t^{1-1/p})\qquad(t\downarrow0).}\tag{B}
```
However the small-o is **not uniform** on the unit ball of `L^p`. The exponent `1-1/p` in (A) is universally optimal even for a fixed smooth compact background and one fixed critical-growth measure. Endpoints must be distinguished: at `p=1`, Lemma 3.10.5 only gives `O(1)` dual operator norm and fixed-test `o(1)`; at `p=infinity`, the operator norm is **exactly `tM`**, so fixed-test `o(t)` is false for `F=1` if `M>0`.

## Proof of (A) and (B): one-line interpolation plus a fixed-test density argument

Since `g_t>=0`,
```math
\int_X g_t^q\,dV
\le \|g_t\|_\infty^{q-1}\int_X g_t\,dV
\le B^{q-1}tM.
```
Taking the `q`th root gives the bound in (A), because `(q-1)/q=1/p` and `1/q=1-1/p`. The **equality of the dual norm** follows from `L^p\!\!-​L^q` duality; explicitly, if `g_t\ne0`, equality is achieved at
```math
F_t=\frac{g_t^{q-1}}{(\int_X g_t^q\,dV)^{1/p}},\quad
\|F_t\|_p=1,\quad
\int_X F_t g_t\,dV=\|g_t\|_q.
```
For (B), take bounded truncations `F_N` of a **fixed** `F\in L^p` with `\|F-F_N\|_p\to0`. Then
```math
\begin{aligned}
t^{-1/q}\left|\int_X Fg_t\,dV\right|
&\le t^{-1/q}\|F_N\|_\infty tM+
t^{-1/q}\|F-F_N\|_p\|g_t\|_q\\
&\le M\|F_N\|_\infty t^{1/p}
+B^{1/p}M^{1/q}\|F-F_N\|_p.
\end{aligned}
```
With `N` fixed, let `t\downarrow0`; then send `N\to\infty`. This proves (B) for every finite `1<p<infinity`, without assuming sequential compactness of measures, pointwise heat-kernel asymptotics, or uniform-in-`F` convergence. Positivity was used to convert heat conservation into the exact `L^1` norm of `g_t`.

## Exact sharpness and the maximizing moving test

On the **unit flat torus** `X=T^{m-2} x T^2`, choose
```math
\rho=dV_{T^{m-2}}\otimes\delta_0.
```
For `m=2`, regard `T^0` as a single point. The measure has `\rho(B_r(x))\le C_m r^{m-2}`, as checked in the earlier critical-endpoint report. By the product heat kernel and conservation of tangential volume,
```math
g_t(y,z)=t h_t\rho(y,z)
=\frac1{4\pi}\sum_{a\in\mathbb Z^2}
\exp\left(-\frac{|z+a|^2}{4t}\right).
\tag{C}
```
Choose the centered fundamental square `[-1/2,1/2]^2`. The sum over nonzero `a` in (C) is uniformly `O(e^{-c/t})` there (including the boundary, since nonzero image distances are at least `1/2`). Integrating the leading Gaussian after the substitution `z=\sqrt t\,u` gives, for every fixed finite `q>1`,
```math
\begin{aligned}
\|g_t\|_q^q
&=(4\pi)^{-q}\int_{T^2}
\exp\left(-\frac{q|z|^2}{4t}\right)\,dz
+o(t)\\
&=\frac{4\pi}{q(4\pi)^q}\,t+o(t).
\end{aligned}
```
The `T^{m-2}` factor has unit volume. Consequently,
```math
\boxed{\lim_{t\downarrow0}t^{-1/q}\|g_t\|_q
=\frac1{4\pi}\left(\frac{4\pi}{q}\right)^{1/q}>0.}\tag{D}
```
For example, at `p=q=2`, this constant is `1/(2\sqrt{2\pi})`. The family `F_t=g_t^{q-1}/(\int g_t^q)^{1/p}` is **smooth, nonnegative, depends on time**, and attains the exact operator norm. Thus there is no estimate with exponent strictly larger than `1-1/p`, and no uniform little-o at the same exponent, even on this single admissible example. There is **no contradiction** with the fixed-test little-o in (B), because `F_t` changes with `t`.

## Classification, related prior findings, and dependents

**New content compared with the existing heat reports:** The 2026-11-03 report `POME-HEAT-FROSTMAN-CRITICAL-QUANTIFIERS-001` establishes the general Frostman exponent, a.e. vanishing, and failure of uniform `L^1` convergence. The 2026-11-06 report `POME-HEAT-CODIM2-LOGARITHMIC-L1-ENDPOINT-001` establishes exact `L^1`-test power and logarithmic examples. **This report instead determines the entire `1<p<infinity` dual operator scale, proves its sharp exponent and constant, and distinguishes fixed-test little-o from moving-test optimality.** Neither previous finding is restated as newly discovered.

**Status:** low / verified conditional deduction, conditional on the **printed** Lemma 3.10.5 heat bound and semigroup conservation, with the flat model directly derived from periodized Euclidean heat. The original Lemmas 3.10.1 and 3.10.5 are **not refuted** and their full elliptic/Nash/Davies prerequisites are **not independently certified**. No proof repair is applied.

**Proposed correction (not applied):** optionally append an `L^p`-pairing remark to §3.10.5 giving (A), (B), and the flat-torus sharpness (D), with the existing source labels, historical attribution, permanent tags, and heat normalization retained. Any downstream use with a **moving** `L^p` coefficient may employ only the uniform `O` rate absent separate compactness; one may not substitute the fixed-test small-o. No downstream theorem is alleged false without checking its actual proof.

**Precise coverage:** new selected mathematical proof of the `L^p` statement at §3.10.5 and a Gaussian model crosscheck of §3.10.1; **§3.10 was already partially visited**, hence **0 first visits / 0 complete section certifications**. Project inventory is 25 chapters / 747 numbered sections / zero entire mathematical-section certifications. Existing confirmed errors, proof gaps, candidates, external dependencies and repairs are unchanged. The owner's excluded Demailly approximation/regularization, Bergman, weighted `L^2`, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remains **deferred-by-user**, not resolved or certified. No tests, builds, GitHub Actions CI, formal verification, publication, or source/body/registry/canonicalization changes were made.
