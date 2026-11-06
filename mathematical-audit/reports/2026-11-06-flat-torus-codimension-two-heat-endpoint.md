# Sharp codimension-two heat-mass bound and arbitrarily slow fixed-L1 pairing (2026-11-06)

**Finding ID:** `POME-HEAT-CODIM2-LOGARITHMIC-L1-ENDPOINT-001` — **low / verified conditional deduction**. The printed lemmas remain correct. This is a sharpness calculation and an endpoint separation of the topologies, **not** a false theorem, a repair of a gap, or a full-section certificate.

**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Selected first-time mathematical inspection:** Chapter 3, §3.10, `docs/sections/heat-kernels-on-compact-manifolds/index.html`, main blob `c59a1b3fab9433f1aae95db99adb4821857b5d8d`. Lemma **3.10.1**, source label `transcendental-positive-cones:327DDB8B` / permanent tag `126365F8EBD6`, physical lines **10–18**, proof **19–83**; Lemma **3.10.5**, source `transcendental-positive-cones:DD00B1CA` / permanent `56A174D59425`, physical **85–105**. The compact Nash identity Eq. 3.10.2, `:C2F15A9B` / `73DAD6727BB9`, and weighted heat inequality Eq. 3.10.3, `:AA615383` / `A5D366E25358`, are **contextual proof dependencies only**, not re-certified.

## 1. Original hypotheses and the precise strengthening tested

Lemma 3.10.5 concerns a compact real (m)-manifold ((m\ge2)), a finite positive Radon measure (ho), the standard nonnegative Laplacian (L=d^*d), and its Markov heat (h_t=e^{-tL}). Its **uniform growth hypothesis** is
[
 ho(B_r(x))\le A r^{m-2},\quad 0<r\le r_0,
]
with (A,r_0>0) independent of (x). It asserts
[
 |h_tho|_\infty\le C(A+ho(X))/t\quad(0<t\le1),
 qquad t\int_X(h_tho)F\,dV\longrightarrow0
]
for each **fixed nonnegative** (F\in L^1(dV)). No rate uniform over the unit ball of (L^1), and no (L^\infty)-norm convergence of (t h_tho), is claimed.

**New sharpness theorem.** For every integer (m\ge2) both claims are simultaneously sharp on the fixed unit flat torus (X=\mathbb T^{m-2}\times\mathbb T^2), with its probability Riemannian volume. Set (ho=dV_{\mathbb T^{m-2}}\otimes\delta_0), taking (\mathbb T^0) to be a point when (m=2). Then
[
 ho(B_r(x))\le C_m r^{m-2},\quad 0<r<1/4,
 qquad \boxed{\lim_{t\downarrow0}|t h_t\rho|_\infty=1/(4\pi).} \tag{1}
]
Nevertheless (t\int(h_t\rho)F\,dV\to0) for **every fixed** (F\in L^1_+(X)).
Moreover there are *fixed* (L^1_+) functions giving every power (t^{1-\beta/2}) with (0<\beta<2), and fixed functions with **logarithmically slow** decay:
[
 \boxed{t\int (h_t\rho)F_\beta\,dV
 =4^{-\beta/2}\Gamma(1-\beta/2)t^{1-\beta/2}(1+o(1)),}
 \qquad F_\beta(y,z)=\mathbf1_{\{|z|<r_0\}}|z|^{-\beta}, \tag{2}
]
and, for (p>1),
[
 \boxed{t\int (h_t\rho)F_p\,dV
 \sim\frac{[\log(e/\sqrt t)]^{1-p}}{2(p-1)},}\qquad
 F_p(y,z)=\frac{\mathbf1_{\{0<|z|<r_0\}}}
 {|z|^2[\log(e/|z|)]^p}. \tag{3}
]
Here (r_0\in(0,1/4)) is fixed, (z\in\mathbb T^2) is represented by the Euclidean coordinate near (0), and the functions do not depend on (y). Thus **no positive algebraic rate in (t)** is valid for all fixed (L^1) data, even on this one model with fixed (ho), and the first estimate cannot be replaced by (o(t^{-1})).

## 2. Full elementary derivation

The embedded subtorus is totally geodesic. For (r<1/4), its intersection with any ambient radius-(r) ball has ((m-2))-dimensional volume at most that of a Euclidean ((m-2))-ball of radius (r). The growth hypothesis holds, including (m=2), when the mass of any ball is at most one.

The scalar heat on a unit flat (k)-torus is given, directly from periodization of the Euclidean fundamental solution, by
[
 H_t^{(k)}(v,w)=(4\pi t)^{-k/2}
 \sum_{a\in\mathbb Z^k}\exp[-|v-w+a|^2/(4t)].
]
The sum converges absolutely with all spatial derivatives at every positive time; it solves (\partial_t H=\Delta H), has total integral one and tends to the periodic Dirac distribution. Hence uniqueness of the smooth heat solution identifies it with (e^{-t d^*d}). The product kernel factorization and Markov normalization on (\mathbb T^{m-2}) yield the **exact** identity
[
 (h_t\rho)(y,z)=H_t^{(2)}(z,0)
 =\frac1{4\pi t}\sum_{a\in\mathbb Z^2}
 e^{-|z+a|^2/(4t)}. \tag{4}
]
At (z=0) the right-hand side, multiplied by (t), tends to (1/(4\pi)). The Fourier expansion
(H_t^{(2)}(z,0)=\sum_{k\in\mathbb Z^2}e^{-4\pi^2t|k|^2}e^{2\pi i k\cdot z})
shows (H_t^{(2)}(z,0)\le H_t^{(2)}(0,0)) by the triangle inequality (the kernel is positive). Thus the maximum occurs at (z=0), proving (1). For each (z\ne0) modulo (\mathbb Z^2), the series in (4) times (t) tends exponentially to zero. The family (tH_t^{(2)}\) is uniformly bounded on (X\times(0,1]); the exceptional subtorus is volume-null. Dominated convergence proves
[
  t\int_X(h_t\rho)F\,dV\to0\qquad(F\in L^1_+(X)).
]
This gives an independent exact-model check of the topology used in the printed proof, without asserting uniform convergence on the (L^1) unit ball.

For (0<\beta<2), the function (F_\beta\) is integrable because (\int_0^{r_0}r^{1-\beta}dr<\infty). On (|z|<r_0) the nonzero-lattice summands in (4) are exponentially small. Extending the zero-lattice Gaussian integral to (\mathbb R^2) incurs another exponentially small error. In polar coordinates,
[
 \begin{aligned}
 t\int_X(h_t\rho)F_\beta\,dV
 &\sim \frac1{4\pi}\int_{\mathbb R^2}e^{-|z|^2/(4t)}|z|^{-\beta}\,dz\\
 &=\frac12\int_0^\infty e^{-r^2/(4t)}r^{1-\beta}\,dr
 =4^{-\beta/2}\Gamma(1-\beta/2)t^{1-\beta/2},
 \end{aligned}
]
which proves (2), **including the normalization constant**.

For (p>1), (F_p\in L^1) since (\int_0^{r_0}dr/[r\log(e/r)^p]<\infty). Its leading pairing is
[
 I_p(t)=\frac12\int_0^{r_0}
 e^{-r^2/(4t)}\frac{dr}{r[\log(e/r)]^p}
 +O(e^{-c/t}).
]
Put (L_t=\log(e/\sqrt t)). Replacing the exponential by (1) on (0<r<\sqrt t) makes an error (O(L_t^{-p})), since (1-e^{-r^2/(4t)}\le r^2/(4t)). The tail (\sqrt t<r<r_0) is (O(L_t^{-p})): on (r\le t^{1/4}), change variables (r=\sqrt t s) and use (\log(e/r)\ge L_t/2) for small (t); above (t^{1/4}), the Gaussian is super-exponentially small. The main integral is **exactly**
[
 \frac12\int_0^{\sqrt t}\frac{dr}{r[\log(e/r)]^p}
 =\frac{L_t^{1-p}}{2(p-1)},
]
proving (3) with a relative error (O(1/L_t)).

## 3. Status and implications

**Classification:** `POME-HEAT-CODIM2-LOGARITHMIC-L1-ENDPOINT-001`, severity **low**, **verified conditional deduction**. The flat-torus computations are self-contained, conditional only on the standard interpretation of scalar heat already established in the printed Lemma 3.10.1. **No original theorem is false, and no original proof gap is established.** The original argument's (|t h_t\rho|_\infty\le C) plus (L^1) truncation is mathematically compatible with (1)–(3); its limit is a *strong (L^1)-pairing limit*, not an (L^\infty) operator norm limit. An optional proposed explanatory note after Lemma 3.10.5 could include the torus example and the logarithmic rate boundary while preserving its source label, permanent tag and attribution.

**Affected dependents:** any use of Lemma 3.10.5 to pass to a heat-smoothed trace current against a **fixed** integrable density is consistent. A proof that chooses a density (F=F_t) depending on the heat time, or that asserts a universal polynomial convergence rate, needs a separate uniform-integrability or quantitative integrability hypothesis. No specific uninspected downstream theorem is declared false. The full spectral/elliptic construction and Gaussian bound proof of Lemma 3.10.1, and all downstream applications, remain **unverified**; only the stated section passage and this exact model were reviewed.

**Exclusions and scope:** No Demailly approximation/regularization or dedicated Bergman, weighted-(L^2), Ohsawa–Takegoshi, multiscale-atlas or positivity-loss proof-completion programme was examined. All prior audit statuses, including **deferred-by-user**, remain unchanged. No source/body/registry/canonical/tag modifications, tests, builds, CI or website publication were performed.
