# Curve-model joint metric is not a length metric; complete Kähler metrics from power boundary exhaustions

**Audit checkpoint (UTC):** 2026-10-25T00:03:40.568Z. **Fresh main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting audit head:** 6622b52999cc3ecac84707afcf359954a732382a. No production files were edited.

## Scope and reading evidence

This is a new selected proof-level inspection of integrated §§9.35, 13.28–13.30 and a selected sheaf proof check in §10.60, with §§9.31 and 13.22 used for context only. It is **not** a full-section or dependency-chain certificate.

- §13.30: source book **non-kahler-pluripotential-theory**, source heading tag **4F216BF5**, permanent section tag **F36B844DE285**. Main file: **docs/sections/volumes-under-bounded-mass--a-complete-space-over-varying-curve-backgrounds/index.html**, blob **506708195b4fbeb7c1c0ac6ebea922983a764a6b**; Eq. 13.30.1, original label **1F6BA73C**, permanent tag **8E9F949AEF0D**, physical HTML lines 15–23; Eq. 13.30.2, source label **F5836858**, permanent tag **685F813E23E8**, lines 28–38; Theorem 13.30.3 source **D0548646**, tag **C5551396F93B**, lines 43–90. Its *completeness* is an assertion about Cauchy sequences, not a length-space assertion.
- §13.29: source **non-kahler-pluripotential-theory**, source heading tag **E9844FE4**, permanent section tag **3A638A8288E0**. Main file **docs/sections/volumes-under-bounded-mass--background-changes-on-curves/index.html**, blob **94ff265434461fd6baee6532decdff369da3e177**, lines 10–36 (Proposition 13.29.1, source **405CAA19**, tag **C9C98321BEFC**) and selected transport/convergence proofs later in that file.
- §13.28: main file **docs/sections/volumes-under-bounded-mass--model-potentials-on-curves/index.html**, blob **4ec0e8d5c90ad5df4e84f17bbc03a2298415e29f**, section tag **E6AC80354EB9**, selected proofs of Lemma 13.28.1 tag **2422DD1AB3AB**, Theorem 13.28.4 tag **74646DD62F50**, and Theorem 13.28.8 tag **3F90EA1D636A**; classification and total-variation formula used only as established internal premises.
- §9.35: source **demailly-complex-geometry** (ordinary geometric section, **not** the excluded approximation programme), source heading **0EF8A13F**, permanent heading **D61A1CDB918C**. Main file **docs/sections/boundary-levi-geometry-and-holomorphic-extension--bounded-power-exhaustions-at-a-smooth-pseudoconvex-boundary/index.html**, blob **3c2f1e7af53a9f7c86ca718d47e5054679ff75a7**; Theorem 9.35.1 source label **8B2CF5E4**, permanent tag **AC8A460928B4**, statement lines 11–16, signed-distance/Oka premise line 22, Hessian inequality line 41, boundary formula lines 45–53, gluing line 70, regularity line 74.
- §10.60: source **demailly-complex-geometry**, source heading **62C023BD**, permanent section **86EF8ADD9D68**, Theorem 10.60.1 permanent **26C06F3C11FF**; **docs/sections/spectral-sequences-support-and-cup-products--neighborhood-continuity-for-a-strongly-paracompact-subspace/index.html**, blob **9ce13a2c6ba1dda798d21872c65ad1ed20d1b571**, lines 12–22. Only the flabby-to-soft restriction and filtered direct-limit dimension-shift steps were spot-checked.

## POME-CURVE-JOINT-NONMIDPOINT-001

**Severity:** low. **Status:** verified conditional deduction; **not** a false theorem. **Affected dependents:** any attempted geodesicity claim about the varying-background space of Theorem 13.30.3, despite its complete and geodesic individual fixed-background fibers.

For a fixed smooth metric on a compact connected curve and conventional induced C^k norms on real (1,1)-forms, set

$$
 b(\sigma,\tau)=\sum_{k\ge0}2^{-k-1}\min\{1,\|\sigma-\tau\|_{C^k}\},
 \quad
 D((\sigma,\mu),(\tau,\nu))=b(\sigma,\tau)+\|\mu-\nu\|_{\rm TV}.
$$

These are precisely (13.30.1)–(13.30.2), in the polar-measure coordinates furnished by Proposition 13.29.1. Choose a positive form $\sigma$ and a scalar $T>0$ with $\|T\sigma\|_{C^0}>1$. Set $\tau=(1+T)\sigma$ and consider $x=(\sigma,0)$, $y=(\tau,0)$; both are admissible and correspond to smooth bounded ordinary models (indeed $p=0$ for positive forms).

**Claim:** There is no metric midpoint between $x$ and $y$ in the *whole* joint model space.

**Proof.** If $z=(\xi,\nu)$ were a metric midpoint, then triangle equality must hold in

$$
 D(x,z)+D(z,y)=
 b(\sigma,\xi)+b(\xi,\tau)+2\|\nu\|_{\rm TV}\ge b(\sigma,\tau)=D(x,y).
$$

Let $a=\|\sigma-\xi\|_{C^0}$, $c=\|\xi-\tau\|_{C^0}$, and $d=\|\sigma-\tau\|_{C^0}>1$. Since $a+c\ge d>1$, if both $a,c$ are positive, then

$$
 \min(1,a)+\min(1,c)>1=\min(1,d).
$$

Thus the $k=0$ term has **strict** triangle inequality, contradicting equality of the full sum. Equality therefore requires $\xi=\sigma$ or $\xi=\tau$. For such $\xi$, the two distances to the endpoints have sum $D(x,y)+2\|\nu\|_{\rm TV}$; equality forces $\nu=0$, so $z$ is an endpoint, never a midpoint since $D(x,y)>0$. QED.

**Proposed optional clarification:** say explicitly after Theorem 13.30.3 that the total joint space is complete but need not be geodesic; the geodesic assertion in Proposition 13.29.1 applies to a fixed background only. No statement or source patch is requested.

## POME-CURVE-JOINT-NONRECTIFIABLE-001

**Severity:** low. **Status:** verified conditional deduction (stronger metric distinction, independent of a false original theorem). **Affected dependents:** intrinsic-length constructions on the joint model space, variational paths allowing smooth backgrounds to move, and comparisons between topological and length-path connectedness.

Let $\Gamma(t)=(\sigma_t,\mu_t)$ be any continuous path in the joint space for the metric $D$. For every finite $N$, the projection $t\mapsto\sigma_t$ is uniformly continuous in the finitely many $C^k$ norms, $0\le k\le N$. Choose a partition sufficiently fine that each increment has $C^k$ norm strictly less than one for all $k\le N$. Along such a partition the clipped terms are **unclipped** for $k\le N$. Thus

$$
\begin{aligned}
\operatorname{Length}_D(\Gamma)
&\ge\sum_i D(\Gamma(t_i),\Gamma(t_{i+1}))\\
&\ge\sum_{k=0}^N2^{-k-1}
       \sum_i\|\sigma_{t_{i+1}}-\sigma_{t_i}\|_{C^k}\\
&\ge\sum_{k=0}^N2^{-k-1}\|\sigma_1-\sigma_0\|_{C^k}.
\end{aligned}
$$

Taking the supremum over $N$ yields the possibly infinite lower bound

$$
\boxed{\operatorname{Length}_D(\Gamma)\ \ge\
 \sum_{k=0}^\infty 2^{-k-1}\|\sigma_1-\sigma_0\|_{C^k}.}
$$

**An explicit pair for which every connecting path has infinite length.** Take the flat elliptic curve $Y=\mathbb C/(\mathbb Z+i\mathbb Z)$, with the standard flat metric and area-one constant form $\eta$. Put

$$
\sigma_0=\eta,\qquad
\sigma_1=(1+\varepsilon\sin(2\pi x))\eta,\qquad 0<\varepsilon<1,
\qquad \mu_0=\mu_1=0.
$$

Both backgrounds are strictly positive of area one; the zero polar measures correspond to the smooth ordinary models $p_0=p_1=0$. With the **standard derivative-based $C^k$ norms induced by this flat metric**,

$$
\|\sigma_1-\sigma_0\|_{C^k}\ge c\,\varepsilon(2\pi)^k
$$

with fixed $c>0$. Hence the untruncated weighted sum diverges, while their distance $D=b(\sigma_0,\sigma_1)\le1$ is finite. No finite-length $D$-continuous path connects these points.

Nevertheless the linear interpolation $\sigma_t=(1-t)\sigma_0+t\sigma_1$ with $\mu_t=0$ is a **continuous** path of admissible smooth positive backgrounds. Therefore the joint space can be topologically path connected along these endpoints yet not rectifiably connected. This stronger example is stated for the indicated legitimate choice of derivative-based norms; the non-midpoint argument above does not depend on high-order seminorm normalization.

**Proposed correction:** no correction to Theorem 13.30.3 (completeness is correct); optionally add a warning that the truncated Fréchet metric is not a length metric and often yields infinite lengths for smooth background variations. Retain its fixed-background metric geometry separately.

## POME-PSH-BOUNDARY-COMPLETE-METRIC-001

**Severity:** low. **Status:** verified conditional deduction from the integrated boundary theorem and its **already cited** Oka/Richberg geometric inputs; no counterexample or false original theorem. **Affected dependents:** complete Kähler metrics on smoothly bounded pseudoconvex domains, the comparison with §9.31, and quantitative boundary-distance estimates.

Assume additionally that the bounded pseudoconvex domain $\Omega\subset\mathbb C^n$ has **C^\infty** boundary. Take the smooth strictly psh power exhaustion $u$ constructed by Theorem 9.35.1 and put

$$
\Phi=-\log(-u).
$$

The function $\Phi$ is smooth strictly psh and proper: since $u<0$ and approaches zero at the boundary, $-\log(-u)\to+\infty$; furthermore the scalar map $t\mapsto-\log(-t)$ is increasing and convex for $t<0$.

On the explicit inner collar of the *actual proof* of 9.35.1, the regularized maximum deletes the interior branch and gives

$$
u=-\delta^\eta\exp(-\eta K|z|^2),\qquad
\Phi=\eta[-\log\delta+K|z|^2]=\eta\psi.
$$

The integrated line-41 Hessian estimate yields

$$
\boxed{
H_\Phi(\xi)\ge\frac\eta2
  \frac{|\partial\delta(\xi)|^2}{\delta^2}
  +\eta|\xi|^2
}
$$

throughout a smaller collar. Define the associated real Riemannian metric by $g_\Phi(v,v)=2H_\Phi(v)$. For any piecewise smooth curve $\gamma$ within that collar,

$$
\|\dot\gamma\|_{g_\Phi}
\ge\sqrt{\eta}\,\frac{|\partial\delta(\dot\gamma)|}{\delta}
\ge\frac{\sqrt\eta}{2}\,
    \frac{|(\delta\circ\gamma)'|}{\delta}.
$$

Thus its length is at least $(\sqrt\eta/2)$ times the total variation of $\log\delta\circ\gamma$. Every curve escaping every compact subset of a bounded domain must approach the boundary along a subsequence, so its $g_\Phi$-length is infinite. Equivalently, metric Cauchy sequences cannot reach the boundary at finite distance, while on compact interior sets the smooth metric is equivalent to Euclidean. The associated Kähler metric is **complete**. For merely $C^2$ boundary, the same computation gives a complete *continuous positive Hessian metric*, but we make no unwarranted claim of smooth Kähler regularity in that case.

This is an **explicit quantitative** boundary-completeness deduction, not the same statement as §9.31.1 (whose direction is complete Kähler $\Rightarrow$ pseudoconvex under the regular-open hypothesis). No additional Demailly approximation, Bergman, $L^2$, Ohsawa–Takegoshi, multiscale or positivity-loss programme is involved. The Oka boundary-distance input (tag **EA195CC9592D**) and Euclidean Richberg maximum (tag **52930869627B**) were used as existing cited geometric inputs, not audited afresh.

## Additional selected proof inspection, limitations and proposed next coverage

- **§13.28:** checked the polar-measure/ordinary-model classification and the total-variation derivation in selected passages. **§13.29:** checked the smooth gauge, polar-measure and area-scaling steps, including the positive-area condition. **§13.30:** checked the product-metric Cauchy argument and uniqueness of the ideal nearest-point pair; the path-geometry examples above do not attack them. The necessary upstream envelope/Green-kernel results are not independently certified.
- **§9.35:** checked signs and constants in the collar computation: the integrated $\eta<1/8$ and $\eta<1/(4K^2R^2)$ ensure positivity of the stated Hessian; the explicitly separated regularized maximum matches the collar branch. This is not an independent proof of Oka's criterion or Richberg smoothing. **§10.60:** checked the stated induction from degree zero through flabby/soft acyclicity and exact filtered colimits as a *selected* step, without certifying the strong-paracompactness interface or the whole derived-functor chain.
- **No new false theorem** is established in this checkpoint. No full build, Python/JS tests, CI, browser check, automatic publication, formal verification, source/body/registry/canonicalization/permanent-tag changes, or main-branch writes were performed.
- Entire dedicated Demailly approximation/regularization and Bergman/$L^2$/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof-completion programme is **deferred-by-user**, not reopened, solved or certified. Historical ledger records remain intact.

