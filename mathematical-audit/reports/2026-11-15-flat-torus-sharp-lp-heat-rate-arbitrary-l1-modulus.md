# Sharp heat-testing operator norms and arbitrarily slow fixed-L1 convergence on a flat torus (2026-11-15)

**Finding:** \`POME-HEAT-SHARP-LP-ARBITRARY-L1-MODULUS-001\`  
**Severity/status:** low / **verified conditional deduction**, not a false printed result and not a source-proof repair.  
**Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Integrated file:** \`docs/sections/heat-kernels-on-compact-manifolds/index.html\`, blob \`c59a1b3fab9433f1aae95db99adb4821857b5d8d\`.  
**Section:** 3.10, *Heat kernels on compact manifolds*, source \`transcendental-positive-cones:FD9C3E46\`, permanent tag \`B8A97FFD89FE\`.  
**Relevant statements:** Lemma 3.10.1, source \`transcendental-positive-cones:327DDB8B\`, permanent \`126365F8EBD6\`, physical lines 11–13 (Gaussian inequality), 19–79 (proof); Lemma 3.10.5, source \`transcendental-positive-cones:DD00B1CA\`, permanent \`56A174D59425\`, physical lines 85–105 (growth hypothesis, $t^{-1}$ estimate, fixed-$L^1$ convergence and truncation proof).

## Precise relation to the integrated statements

Lemma 3.10.5 assumes a finite positive measure $\rho$ with $\rho(B_r(x))\le A r^{m-2}$, $m\ge2$, and asserts
\[
 t\int_X (h_t\rho)(x)F(x)\,dV(x)\longrightarrow0
 \qquad(F\ge0,\ F\in L^1(X,dV)\text{ fixed}).
\]
The printed proof uses the Gaussian estimate of Lemma 3.10.1, critical Frostman growth, heat conservation and truncation of a *fixed* $F$. No rate depending only on $\|F\|_1$ is asserted. We now quantify precisely which stronger statements are true and false in the simplest admissible model. This is separate from the earlier 2026-11-06 codimension-two logarithmic *individual-profile* calculations: neither their $L^\infty$ endpoint observation nor their power/log examples is re-registered.

## Model and exact operator norm

Let $X=\mathbb R^2/\mathbb Z^2$ with Euclidean area $dV$ of total volume one, let $o=[0]$, and set $\rho=\delta_o$. Since $m=2$, $\rho(B_r(x))\le1=A r^{m-2}$ for every $x,r$; $\rho$ satisfies the exact hypothesis of Lemma 3.10.5. With the nonpositive scalar Laplacian convention for the heat generator, the periodized Gaussian is
\[
 h_t(o,y)=\frac1{4\pi t}\sum_{k\in\mathbb Z^2}
       \exp\!\left(-\frac{|y+k|^2}{4t}\right).
 \tag{1}
\]
The series and its derivatives converge normally for $t>0$, solve the heat equation, have integral one on the torus, and converge to $\delta_o$ as $t\downarrow0$; uniqueness follows, for example, by Fourier coefficients. Thus (1) is the actual scalar heat kernel, not merely a comparison model.

Define the functional
\[
 I_t(F)=t\int_X (h_t\rho)F\,dV
       =t\int_X h_t(o,y)F(y)\,dy.
 \tag{2}
\]
For $1\le p\le\infty$ and the Hölder conjugate $q$ ($q=\infty$ at $p=1$), positivity and Hölder duality give the **exact** norm identity
\[
 \|I_t\|_{L^p(X)\to\mathbb R}=t\,\|h_t(o,\cdot)\|_{L^q(X)}.
 \tag{3}
\]
For $1<p<\infty$, equality follows using the normalized nonnegative function proportional to $h_t(o,\cdot)^{q-1}$; the $p=1$ norm is its essential supremum and the $p=\infty$ norm its integral.

On the fundamental square $[-1/2,1/2]^2$ the $k\ne0$ terms of (1) are $O(t^{-1}e^{-c/t})$ uniformly for some $c>0$. Consequently, for each fixed $1\le q<\infty$,
\[
 \int_X h_t(o,y)^q\,dy
 =\frac{1+o(1)}{(4\pi t)^q}
   \int_{\mathbb R^2}e^{-q|y|^2/(4t)}\,dy
 =\frac{1+o(1)}q(4\pi t)^{1-q}.
 \tag{4}
\]
For $q=\infty$, (1) attains its maximum at $o$ (by the elementary theta Fourier expansion, or Cauchy–Schwarz and semigroup symmetry) and
\[
 \|h_t(o,\cdot)\|_\infty=(4\pi t)^{-1}(1+O(e^{-c/t})).
 \tag{5}
\]
Combining (3)–(5), with $q^{-1/q}=1$ for $q=1,\infty$, yields the **sharp full family**
\[
 \boxed{\ \|I_t\|_{L^p\to\mathbb R}
   =(4\pi)^{-1/p}q^{-1/q}\,
      t^{\,1-1/p}(1+o(1)),
       \qquad1\le p\le\infty.\ }
 \tag{6}
\]
At $p=\infty$ the norm equals $t$ exactly. Thus for every $p>1$ the uniform exponent $1-1/p$ and its leading constant are optimal; at $p=1$ the operator norms do **not** tend to zero. The latter endpoint fact is already implicit in the earlier 2026-11-06 audit and is recorded here only as the necessary boundary case of the new complete $L^p$ norm calculation.

## No prescribed rate even for one fixed normalized $L^1$ test

The strictly stronger new endpoint observation is that **even a fixed** $F\ge0$ of $L^1$ norm one may converge to zero more slowly, along a sequence, than *any prescribed positive modulus* $\omega(t)\to0$. Precisely, for every function $\omega:(0,1]\to(0,\infty)$ with $\lim_{t\downarrow0}\omega(t)=0$, there are $F\ge0$, $\int F\,dV=1$, and $t_j\downarrow0$ such that
\[
 \frac{I_{t_j}(F)}{\omega(t_j)}\longrightarrow+\infty.
 \tag{7}
\]

Choose $t_j\downarrow0$, $r_j=\sqrt{t_j}<1/8$, recursively so that $r_{j+1}<r_j/4$ and $\omega(t_j)\le16^{-j}/j^2$. Let
\[
 A_j=\{y\in X:r_j/2\le|y|\le r_j\},\quad
 a_j=j\omega(t_j),\quad
 F_j=\frac{a_j}{|A_j|}\mathbf1_{A_j}.
\]
The annuli are disjoint and $\sum_j a_j\le\sum_j16^{-j}/j<1$. Choose a nonnegative bump $G$ supported away from $o$ with integral $1-\sum_j a_j$, and put $F=G+\sum_jF_j$. Then $F\in L^1_+(X)$ and $\|F\|_1=1$. For all $y\in A_j$, the $k=0$ term in (1) gives
\[
 t_j h_{t_j}(o,y)\ge\frac{e^{-1/4}}{4\pi}=:c_0>0.
\]
Hence
\[
 I_{t_j}(F)\ge c_0\int_{A_j}F\,dV
 =c_0j\,\omega(t_j),
\]
which proves (7). Each $F$ is fixed once the modulus is specified; the construction does **not** change $F$ with time. Lemma 3.10.5 nevertheless gives $I_t(F)\to0$, so no contradiction arises.

## Classification, dependencies, and proposed documentation

- **Status:** verified conditional deduction; **no confirmed error** in Lemma 3.10.1 or 3.10.5. The heat kernel (1) and all calculations (2)–(7) are explicit on the flat torus; the general compact-manifold heat existence and the full upstream Gaussian/Nash proof are not transitively certified by this increment.
- **Novelty relative to 2026-11-03 and 2026-11-06:** the exact *entire* $L^p\to\mathbb R$ operator-norm asymptotic with leading constants and the fixed-$F$ diagonal construction defeating **every** prescribed vanishing modulus. Earlier codimension-two power/logarithmic test examples and the already observed $p=1$ norm obstruction remain historical, not counted anew.
- **Affected uses:** any attempt to replace the fixed-$F$ statement of Lemma 3.10.5 by a uniform $L^1$-unit-ball convergence or a universal fixed-test rate. Such upgrades require extra integrability/equi-integrability or concentration control; no particular uninspected downstream theorem is declared false.
- **Proposed correction:** optionally add a remark after Lemma 3.10.5 distinguishing sharp uniform $L^p$, $p>1$, from unrestricted fixed-$L^1$ convergence with no modulus. Do not alter the original theorem's hypotheses, attribution, source labels, or permanent tags. No source/body/registry edits are made here.
- **Actual coverage:** selected direct rereading of §3.10.1 (Gaussian statement, selected norm-estimate steps) and §3.10.5 (hypotheses, conclusion and truncation argument), plus independent torus calculation. Section 3.10 was already partially inspected in the broad-scope audit; **0 newly first-visited numbered sections, 0 completely certified sections**. Current ToC: **25 chapters / 747 numbered sections**. No project build, test suite, CI, site update, or formal verification was performed. Excluded regularization/Bergman/L²/OT/multiscale/positivity-loss programmes remain **deferred-by-user**.
