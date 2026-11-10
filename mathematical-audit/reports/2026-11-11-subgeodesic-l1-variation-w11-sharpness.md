# Exact L1 time variation of subgeodesics and the sharp W^{1,1} endpoint

**Finding:** POME-GEO-SUBGEO-L1-VARIATION-W11-SHARP-001  
**Date:** 2026-11-11  
**Severity / status:** low / verified conditional deduction. **No error is alleged in the printed statements.**  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.

## Exact integrated reading-edition anchors

- **File:** docs/sections/geodesic-rays-in-the-space-of-potentials/index.html; **Git blob:** 52bf9e459a0dfb1c8afe79556db037450be06bb3.
- Standing compact-connected-Kähler, big-class setting, **physical line 23**; Definition **17.10.2**, source **sgpt:9287531D**, permanent tag **8699FCF63094**, **lines 27–56** (subgeodesic complexification and L1 endpoints).
- Proposition **17.10.7**, source **sgpt:DBC4F9ED**, permanent tag **1880C1FBD88F**, **lines 88–140** (convexity of each time section; the lower envelope is theta-psh).
- Corollary **17.10.9**, source **sgpt:B35F3B4F**, permanent tag **C645EE3517E1**, **lines 144–174** (pointwise endpoint equality *quasi-everywhere*). Corollary **17.10.11**, source **sgpt:9B844C56**, permanent tag **E31D1E7DDF87**, **lines 176–191** (qualitative L1 continuity).
- These are distinct from the previously registered §17.10.13 supremum/endpoints analysis, abstract rooftop completeness (§17.10.59), and radial ray metric checks (§17.10.82–94).

## New precise result

Let X be a connected compact Kähler manifold, theta a smooth closed real (1,1)-form in a big class, and let (u_t)_{0<=t<=1} be any subgeodesic in PSH(X,theta) in the exact sense of Definition 17.10.2. Fix **any** smooth positive volume measure dV, without normalizing its total mass. Set

\[
m(x)=\inf_{0<t<1}u_t(x), \qquad A(x)=\max\{u_0(x),u_1(x)\}.
\]

By Proposition 17.10.7, m belongs to PSH(X,theta); hence m, u_0 and u_1 are integrable and A-m is a nonnegative L1 function (modulo a pluripolar null set). Then:

1. The map \(t\mapsto u_t\) belongs to the **Bochner Sobolev space** \(W^{1,1}([0,1];L^1(X,dV))\). The pointwise convex-time derivative \(g(t,x)=\partial_tu_t(x)\), defined for a.e. \((t,x)\), represents its Bochner derivative.
2. There is an **exact total-variation identity**
   \[
   \boxed{\quad \operatorname{Var}_{L^1(X,dV)}(u_\bullet)
       =\int_0^1\|\dot u_t\|_{L^1(dV)}\,dt
       =\int_X\bigl(u_0+u_1-2m\bigr)\,dV.\quad}
   \]
   In particular this is at most \(2\int_X(A-m)\,dV\). The factor 2 is sharp.
3. For every \(0<\delta<1/2\) and \(s,t\in[\delta,1-\delta]\),
   \[
   \boxed{\quad \|u_t-u_s\|_{L^1(dV)}
       \le \frac{|t-s|}{\delta}\int_X(A-m)\,dV.\quad}
   \]
   The coefficient \(1/\delta\) cannot be uniformly decreased at fixed \(\delta\).
4. Neither a universal global \(W^{1,p}\)-conclusion for any \(p>1\), nor global Lipschitz continuity in L1, follows, **even with smooth endpoints and spatially constant relative potentials**.

The result is conditional only on the specific printed convexity, lower-envelope and quasi-everywhere endpoint assertions above. It is **not** a transitive certification of their underlying pluripotential proofs.

## Complete proof (no regularization)

**Finite scalar convexity and endpoints.** By Proposition 17.10.7, for every x the time section is extended-valued convex; its infimum m is theta-psh and m<=min(u_0,u_1). Since theta-psh functions on compact X are L1 and not identically -infinity, outside a volume-null set all of m,u_0,u_1 are finite. For each such x, m(x)<=u_t(x)<= (1-t)u_0(x)+tu_1(x)<=A(x), so every interior time value is finite. The endpoint equality in Corollary 17.10.9 holds quasi-everywhere and hence dV-almost everywhere, so the scalar convex function extends **continuously** to t=0,1 with values u_0(x),u_1(x). This last step is indispensable: convexity alone on a closed interval permits a downward jump at an endpoint.

**Exact scalar variation.** A finite convex function f continuous on [0,1] is absolutely continuous: its one-sided derivative is monotone on (0,1), integrable since the decrease to a minimum and subsequent increase have finite sums, and its integral reconstructs f, including endpoints by continuity. A convex function decreases up to its minimum interval and increases thereafter. Consequently
\[
\int_0^1|f'(t)|\,dt=\operatorname{Var}_{[0,1]}(f)
=f(0)+f(1)-2\min_{[0,1]}f.
\]
For the a.e. x above, \(\min f_x=m(x)\). Apply this identity to \(f_x(t)=u_t(x)\).

**Pass to L1 without illicit limit exchange.** Let \(g(t,x)\) be the pointwise a.e. derivative, selected as the limit of measurable difference quotients and set to zero on the joint null set. Tonelli's theorem applied to the nonnegative |g| gives
\[
\int_0^1\int_X|g(t,x)|\,dV\,dt
=\int_X[u_0(x)+u_1(x)-2m(x)]\,dV<\infty.
\]
For any \(0\le s\le t\le1\), scalar absolute continuity followed by Fubini yields
\[
u_t-u_s=\int_s^t g(\tau,\cdot)\,d\tau
\quad\text{in }L^1(X,dV).
\]
Thus the path is Bochner absolutely continuous and belongs to W^{1,1}, with derivative g a.e.

For completeness, equality with **metric** total variation does not follow merely by interchanging a supremum and an integral. Let \(\mathcal P_N=\{j2^{-N}:0\le j\le2^N\}\). Its scalar variation sums increase pointwise with N and, by scalar convex continuity, tend to \(u_0+u_1-2m\) for almost every x. Monotone convergence therefore gives
\[
\lim_N\sum_{j=0}^{2^N-1}
 \|u_{(j+1)2^{-N}}-u_{j2^{-N}}\|_{L^1}
 =\int_X(u_0+u_1-2m)\,dV.
\]
The reverse bound for **every** partition follows from integrating the scalar total variation. This proves the metric variation equality independently. Its equality with the integral of the Bochner derivative also follows from the preceding absolute-continuity representation.

**Sharp interior bound.** For a.e. x the monotone one-sided slopes of the convex function obey
\[
\frac{u_t(x)-u_0(x)}{t}
 \le \partial^-_t u_t(x)
 \le \partial^+_t u_t(x)
 \le \frac{u_1(x)-u_t(x)}{1-t}.
\]
At every differentiability time \(t\in[\delta,1-\delta]\), both the positive and negative derivative magnitudes are bounded by \((A(x)-m(x))/\delta\). Integrate the derivative from s to t and then over X. No uniform upper or lower bound on the individual psh functions is needed.

## Sharpness and scope boundaries

Take any compact Kähler X, theta=omega Kähler, and spatial base potential 0. Every continuous convex real function f(t) defines the valid subgeodesic \(u_t(x)=f(t)\): its complexification is subharmonic in the strip variable and is spatially constant.

- For \(f(t)=|2t-1|\), the endpoints are 1, the minimum is 0, \(A-m=1\), and
  \[
  \operatorname{Var}_{L^1}(u_\bullet)=2\,\operatorname{Vol}(X)
  =2\int_X(A-m)\,dV.
  \]
  The factor 2 in the general upper bound is optimal.
- For \(0<\delta<1/2\), choose \(\varepsilon>0\) with \(\delta+\varepsilon<1-\delta\) and
  \(f_\varepsilon(t)=\max\{1-t/(\delta+\varepsilon),0\}\).
  The endpoint gap A-m is 1. For \(t=\delta\) and \(s=\delta+\varepsilon/2\), the L1 difference quotient divided by \(\int_X(A-m)\,dV\) equals \(1/(\delta+\varepsilon)\), approaching \(1/\delta\). The coefficient in the interior estimate is therefore sharp.
- Fix any \(p>1\) and choose \(0<\alpha\le1-1/p\). The convex continuous function \(f(t)=-t^\alpha\) has smooth spatial endpoints 0 and -1 and
  \[
  |f'(t)|=\alpha t^{\alpha-1}\in L^1(0,1)\setminus L^p(0,1).
  \]
  The associated spatially constant subgeodesic is not in \(W^{1,p}([0,1];L^1(X,dV))\), and is not L1-Lipschitz at t=0. Thus the W^{1,1} endpoint is optimal in the stated generality.

## Audit decision and dependents

- **Printed Proposition 17.10.7, Corollaries 17.10.9 and 17.10.11:** no error found in the selected uses. The new statement is a **verified conditional deduction**, not a claimed repair, and is not a statement that every preceding internal analytic dependency has been proved.
- **Proposed optional main-text addition only:** after Corollary 17.10.11, add an L1-time-variation corollary with the exact identity and the two sharpness examples. Do **not** modify body/registry/source/tag directly.
- **Affected use sites:** quantitative time estimates for §17.10 subgeodesics, §17.13 Ross–Witt Nyström correspondence and §17.17 Legendre constructions may use it when the same endpoint hypotheses hold. No downstream theorem is recertified and no new interchange of time/Monge–Ampère limits is asserted.
- **Comparison with recorded work:** previous §17.10.13 findings studied supremum envelopes and lack of a family-uniform **endpoint modulus**; previous §17.10.59 findings studied rooftop metric completeness. The exact global Bochner W^{1,1}/variation identity and optimal fixed-path interior constant are separate.
- **Actual coverage:** selected physical lines 23–56, 88–191 of the integrated §17.10 file; no full-section or transitive proof certification. Already sampled §17.10: **0 new first visits, 0 complete section certifications**. Current ToC: **25 chapters, 747 numbered sections**, as checked from docs/chapters/index.html and the existing matrix.
- **Owner exclusion:** Demailly approximation/regularization and its dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale and positivity-loss proof programme remain **deferred-by-user**; nothing from that programme is used or reopened. No software build, test, CI, publication or source change is claimed.
