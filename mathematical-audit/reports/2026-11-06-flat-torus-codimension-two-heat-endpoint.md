# Codimension-two heat-mass endpoint and logarithmically slow fixed-L¹ pairings (2026-11-06)

**Stable finding:** POME-HEAT-CODIM2-LOGARITHMIC-L1-ENDPOINT-001. **Severity / status:** low / **verified conditional deduction**, not a false theorem, an established proof gap, or an applied repair.

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Integrated reading file:** docs/sections/heat-kernels-on-compact-manifolds/index.html, blob c59a1b3fab9433f1aae95db99adb4821857b5d8d.
**Current ToC:** Chapter 3, §3.10, *Heat kernels on compact manifolds*.
**Primary anchor:** Lemma 3.10.5, physical lines 85–105, source label transcendental-positive-cones:DD00B1CA, permanent tag 56A174D59425.
**Contextual anchor:** Lemma 3.10.1, lines 10–18 and its proof at lines 19–83, source transcendental-positive-cones:327DDB8B, permanent tag 126365F8EBD6. Equations 3.10.2 (C2F15A9B / 73DAD6727BB9) and 3.10.3 (AA615383 / A5D366E25358) are proof context, **not** newly certified.

## 1. The precise claim being tested

The printed Lemma 3.10.5 assumes a compact Riemannian manifold of real dimension $m\ge2$, a finite positive Radon measure $\rho$, and the *uniform* codimension-two growth condition
$$
 \rho(B_r(x))\le A r^{m-2}\qquad(x\in X,\ 0<r\le r_0).
$$
With the nonnegative Laplacian $L=d^*d$ and its mass-preserving heat semigroup $h_t=e^{-tL}$, it concludes
$$
 \|h_t\rho\|_\infty\le C(A+\rho(X))/t,\qquad
 t\int_X(h_t\rho)F\,dV\longrightarrow0
 \quad\text{for each fixed }F\in L^1_+(X).
$$
The second conclusion does **not** assert either $\|t h_t\rho\|_\infty\to0$ or a rate uniform over all $F$ in the unit ball of $L^1$.

**New sharpness result.** Both distinctions are mathematically essential, already on the unit flat torus
$$
 X=\mathbb T^{m-2}\times\mathbb T^2,\qquad
 \rho=dV_{\mathbb T^{m-2}}\otimes\delta_0.
$$
When $m=2$, take $\mathbb T^0$ to be one point. This measure has precisely the required $r^{m-2}$ local upper growth, yet
$$
 \boxed{\lim_{t\downarrow0}\|t h_t\rho\|_\infty=\frac1{4\pi}.}\tag{1}
$$
For every *fixed* nonnegative integrable $F$, the pairing still tends to zero. For a fixed $r_0\in(0,1/4)$ and any $0<\beta<2$, put
$$
 F_\beta(y,z)=\mathbf1_{\{0<|z|<r_0\}}|z|^{-\beta}.
$$
The precise asymptotic is
$$
 \boxed{t\int_X(h_t\rho)F_\beta\,dV
 =4^{-\beta/2}\Gamma(1-\beta/2)\,t^{1-\beta/2}(1+o(1)).}\tag{2}
$$
More sharply, for any fixed $p>1$ put
$$
 F_p(y,z)=\frac{\mathbf1_{\{0<|z|<r_0\}}}
 {|z|^2[\log(e/|z|)]^p}.
$$
Then $F_p\in L^1(X)$ and
$$
 \boxed{t\int_X(h_t\rho)F_p\,dV
 \sim \frac{[\log(e/\sqrt t)]^{1-p}}{2(p-1)}.}\tag{3}
$$
Thus even for this **one fixed** smooth background and **one fixed** $\rho$, there is no positive algebraic convergence rate valid for all fixed $L^1$ data.

## 2. Exact flat-torus heat-kernel proof

The measure $\rho$ is normalized $(m-2)$-volume on a flat totally geodesic subtorus. Every sufficiently small ambient ball meets this subtorus in a subset of an $(m-2)$-dimensional Euclidean ball of the same radius. Hence $\rho(B_r(x))\le C_m r^{m-2}$, including $m=2$, when any ball has mass at most one.

For the unit flat $k$-torus, periodize the Euclidean heat solution:
$$
 H_t^{(k)}(v,w)=(4\pi t)^{-k/2}
 \sum_{a\in\mathbb Z^k}
 \exp\!\left(-\frac{|v-w+a|^2}{4t}\right).
$$
The series and all its spatial derivatives converge absolutely for every $t>0$. It solves $\partial_t H=\Delta H$, has integral one, and tends distributionally to the periodic delta mass. Uniqueness of smooth heat evolution identifies it with $e^{-td^*d}$. Factorization of the product kernel, followed by the tangential mass-one integral, gives
$$
 (h_t\rho)(y,z)=H_t^{(2)}(z,0)
 =\frac1{4\pi t}\sum_{a\in\mathbb Z^2}
 e^{-|z+a|^2/(4t)}. \tag{4}
$$
At $z=0$, multiplying by $t$ gives $1/(4\pi)+O(e^{-c/t})$. Conversely, the absolutely convergent Fourier expansion
$$
 H_t^{(2)}(z,0)=\sum_{k\in\mathbb Z^2}
 e^{-4\pi^2t|k|^2}e^{2\pi i k\cdot z}
$$
and the triangle inequality imply $H_t^{(2)}(z,0)\le H_t^{(2)}(0,0)$, so (1) holds for the **actual supremum**.

At every $z\not\equiv0\pmod{\mathbb Z^2}$ the right-hand side of (4) multiplied by $t$ tends to zero exponentially. By (1) it is uniformly bounded for $0<t\le1$. The exceptional subtorus has zero ambient volume. Thus dominated convergence proves
$$
 t\int_X(h_t\rho)F\,dV\to0\qquad(F\in L^1_+(X)),
$$
independently for this model, and without an illegitimate uniform-in-$F$ inference.

## 3. Exact power and logarithmic rates

For $0<\beta<2$, polar integration shows $F_\beta\in L^1$ since $\int_0^{r_0}r^{1-\beta}dr<\infty$. On $|z|<r_0$, the nonzero lattice terms of (4) are $O(t^{-1}e^{-c/t})$; extending the zero-lattice term to all $\mathbb R^2$ adds only exponentially small error. Consequently
$$
\begin{aligned}
 t\int_X(h_t\rho)F_\beta\,dV
 &\sim\frac1{4\pi}\int_{\mathbb R^2}e^{-|z|^2/(4t)}|z|^{-\beta}\,dz\\
 &=\frac12\int_0^\infty e^{-r^2/(4t)}r^{1-\beta}\,dr\\
 &=4^{-\beta/2}\Gamma(1-\beta/2)t^{1-\beta/2}.
\end{aligned}
$$
This verifies every factor in (2), including the heat normalization $4\pi t$.

For $p>1$ the polar $L^1$ integral of $F_p$ is a constant times $\int_0^{r_0}dr/[r(\log(e/r))^p]<\infty$. Equation (4) reduces its pairing, up to $O(e^{-c/t})$, to
$$
 I_p(t)=\frac12\int_0^{r_0}e^{-r^2/(4t)}
 \frac{dr}{r[\log(e/r)]^p}.
$$
Write $L_t=\log(e/\sqrt t)$. On $(0,\sqrt t)$ replacing the Gaussian by one produces an error $O(L_t^{-p})$, using $1-e^{-r^2/(4t)}\le r^2/(4t)$. On $(\sqrt t,t^{1/4})$, substitute $r=\sqrt t\,s$: the logarithm is at least $L_t/2$ for small $t$ and $\int_1^\infty e^{-s^2/4}ds/s<\infty$, so this part is $O(L_t^{-p})$. The remaining part $(t^{1/4},r_0)$ is exponentially small in $1/\sqrt t$ times the finite tail integral. Thus
$$
 I_p(t)=\frac12\int_0^{\sqrt t}
 \frac{dr}{r[\log(e/r)]^p}+O(L_t^{-p})
 =\frac{L_t^{1-p}}{2(p-1)}+O(L_t^{-p}),
$$
which proves (3). Since $t^{-\delta}L_t^{1-p}\to\infty$ for every $\delta>0$, a universal polynomial rate fails even for a *fixed* admissible $F_p$.

## 4. Audit classification and dependents

**Status:** low / verified conditional deduction. The original Lemmas 3.10.1 and 3.10.5 remain **correct**. The model proof confirms that the printed $t^{-1}$ heat-mass bound is of optimal order and that the printed limit is **pointwise in the fixed test function**, not convergence in the operator norm from $L^1$ to $\mathbb R$.

**Proposed change, not applied:** append an optional endpoint remark after Lemma 3.10.5 explaining (1)–(3), preserving the original source attribution and permanent tags. For any downstream argument permitting $F=F_t$ to vary with the heat time, a separate uniform-integrability or stronger quantitative hypothesis is necessary; no uninspected downstream theorem is alleged false. The general compact heat existence theorem, Gaussian estimate, Nash/Moser proof and all downstream analytic dependencies remain **uncertified**.

**Actual review scope:** first selected mathematical inspection of §3.10, Lemmas 3.10.1 and 3.10.5 at the listed line anchors, with one complete flat-torus model. Not a whole-section certification. Other findings and external dependencies remain in their earlier classifications. All Demailly approximation/regularization and dedicated Bergman, weighted-L², Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof-completion work is **deferred-by-user**, not reviewed or certified. No main/source/body/registry/tag edits, project tests, CI, builds, formalization, or publication.
