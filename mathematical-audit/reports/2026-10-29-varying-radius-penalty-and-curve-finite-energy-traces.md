# Mathematical audit — 29 October 2026: sharp constrained-radius penalty and finite-energy curve traces

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272 (read-only). **Review branch:** review/mathematical-audit. This report concerns only the integrated reading-edition statements and selected proof steps specified below. No entire section, theorem chain, or chapter has been certified.

## POME-ENVELOPE-VARYING-RADIUS-SHARP-BARRIER-001

**Status:** verified conditional deduction; **severity:** low. **Not a false theorem or a repaired error.**

**Integrated anchor:** docs/sections/envelopes-and-model-potentials--measures-on-contact-sets--a-minimum-with-a-varying-upper-radius/index.html, main blob 879fd87eacb65755ae0e7a9ffc95e71d1c262d39, physical lines 10–55; Lemma 16.18.1, source label foundations-of-pluripotential-theory:1E3A3A35; permanent tag 93E8FFBE7FEB. The theorem's hypotheses and original Schur-complement argument are intact. Previously only an inventory row was present for §16.18.

### A quantitative strengthening

Use exactly the printed hypotheses: on D, H(z,s) is smooth on a neighborhood of s ≤ b(z), H_s ≥ 0, H_{ss}>0, H is locally uniformly bounded below toward s = −∞, and c>0. Set
$$
F(z,s)=H(z,s)-cs,\quad
v(z)=\min_{s\le b(z)}F(z,s),\quad
v_\varepsilon(z)=\min_{s<b(z)}\{F(z,s)-\varepsilon\log(b(z)-s)\}.
$$
For every compact K⊂D, there are constants C_K and ε_K>0 such that
$$
\sup_{z\in K}|v_\varepsilon(z)-v(z)|
 \le C_K\varepsilon+\varepsilon\log(1/\varepsilon)
 \quad(0<\varepsilon<\varepsilon_K).
$$
This sharpens the qualitative locally uniform convergence asserted at physical lines 52–54; it does not introduce any approximation or regularization of psh functions.

**Proof.** On a compact base neighborhood the lower-bound-at-−∞ hypothesis and c>0 imply uniform coercivity of F and of F−ε log(b−s), for 0<ε≤ε_K. Thus all constrained and penalized minimizers lie in a common bounded s-strip [S,b(z)]. Choose S with a strict buffer below the unpenalized minimizers. On that strip, R_K:=sup(b(z)−s) is finite and F has a uniformly bounded s-derivative, say L_K. If s_0(z) is the unpenalized minimizer, put s'_0(z)=min{s_0(z),b(z)−ε}. Then s'_0 is feasible, differs from s_0 by at most ε, and b−s'_0≥ε. Hence
$$
v_\varepsilon(z)
 \le F(z,s'_0)-\varepsilon\log(b-s'_0)
 \le v(z)+L_K\varepsilon+\varepsilon\log(1/\varepsilon).
$$
At the penalized minimizer, b−s_\varepsilon≤R_K, hence
$$
v_\varepsilon(z)
 =F(z,s_\varepsilon)-\varepsilon\log(b-s_\varepsilon)
 \ge v(z)-\varepsilon\log R_K.
$$
Increasing C_K to absorb the fixed lower-bound constant proves the estimate. The result is uniform on K, with no interchanged limiting operations.

### Optimality of the logarithmic convergence rate

Take D any disk, b(z)=B constant, H(z,s)=e^s, Λ=0, and c>e^B. These data meet every stated hypothesis, including the joint Levi bound. The unpenalized minimum is attained at s=B. Write t_\varepsilon=B−s_\varepsilon>0. The penalized critical equation gives
$$
\frac{\varepsilon}{t_\varepsilon}
 =c-e^{B-t_\varepsilon},\qquad
t_\varepsilon=\frac{\varepsilon}{c-e^B}+O(\varepsilon^2).
$$
Consequently
$$
v_\varepsilon-v
 =(c-e^B)t_\varepsilon-\varepsilon\log t_\varepsilon
 +O(t_\varepsilon^2)
 =\varepsilon\log(1/\varepsilon)+O(\varepsilon).
$$
Thus the logarithm cannot generally be replaced by an O(ε) bound.

### Sharpness of the endpoint-curvature coefficient

Take a small ball in C^n, the flat Hermitian form
$\widehat\omega=i\sum_j dz_j\wedge d\bar z_j$, choose
$b(z)=B+C_b|z|^2$, $H=e^s$, Λ=0, and ensure $c>\sup_D e^{b(z)}$.
Then $H_s<c$ on the whole constrained interval, so the minimum is at s=b(z) and
$$
v=e^{b}-cb,\qquad
i\partial\bar\partial v\big|_{z=0}
 =(e^B-c)C_b\widehat\omega\big|_{z=0}.
$$
Letting B→−∞ shows that the original lower bound
$i\partial\bar\partial v\ge-\Lambda-cC_b\widehat\omega$
has the **optimal universal coefficient c** under the printed hypotheses. In particular dropping the endpoint term for a merely plurisubharmonic (rather than plurisuperharmonic) b is unjustified. The printed theorem and its signs are correct.

**Recommendation/dependents:** Optional proof-level quantitative corollary adjacent to Lemma 16.18.1, without changing its permanent tag or original statement. Other contact-set envelope arguments that reuse a variable-radius minimum can cite the local O(ε log(1/ε)) bound. This does not certify upstream envelope or curvature smoothing inputs.

## POME-CURVE-TRACE-FINITE-ENERGY-001

**Status:** verified conditional deduction; **severity:** low. **Not a false theorem or a complete replacement of the nearby nonlinear PDE results.**

**Integrated anchor:** docs/sections/equations-with-prescribed-singularities--singular-measures-on-products-with-a-curve/index.html, main blob faaa787720a2f791dc9526724427e9b669516051, physical lines 9–23, 66–105; Lemma 15.31.4, source label non-kahler-pluripotential-theory:CF08BC57, permanent tag F5E3175FA178; formulas 15.31.5 and 15.31.6, tags DB0D4C618F78 and 79703FA8B5E7. Only Lemma 15.31.3's distributional curvature identity is used from its neighborhood; §15.31.8 and later exponential/product equations are not certified.

### A weaker sufficient trace hypothesis

On Y=P^1 with κ the mass-one Fubini–Study form, let μ be a positive Borel probability **not charging polar sets**. Define its normalized Green potential Q as in (15.31.1), so $dd^c Q=\mu-\kappa$ distributionally. If **Q∈H^1(Y)**, without requiring Q finite or continuous everywhere, smooth restriction extends uniquely to a bounded linear map
$$
\operatorname{Tr}_\mu:H^1(Y)\longrightarrow L^1(\mu),
$$
and for every h∈H^1
$$
\int\operatorname{Tr}_\mu h\,d\mu
 =\int h\,\kappa-E(h,Q),\qquad
\|\operatorname{Tr}_\mu h\|_{L^1(\mu)}
 \le \|h\|_{L^1(\kappa)}
       +E(h,h)^{1/2}E(Q,Q)^{1/2}.
$$
For κ-psh h∈H^1 the trace equals its canonical values μ-a.e.; the trace commutes with real Lipschitz compositions. This is **only** a strengthening of the trace component of Lemma 15.31.4. Its original stronger assumption Q finite and continuous remains relevant to regularity and the nonlinear equation in §15.31.8.

**Proof.** For smooth real h, $dd^cQ=\mu-\kappa$ and the Sobolev integration-by-parts pairing yield the displayed signed identity. Apply it to $\sqrt{h^2+\delta^2}$, whose Dirichlet norm is at most that of h, and let δ↓0. Positivity of μ yields the L^1 bound. By density of smooth functions in H^1, the map extends uniquely and the identity follows by continuity. For κ-psh h∈H^1, average under smooth approximate identities in SU(2), as in physical lines 91 and 105: these averages converge strongly in H^1 because rotations act isometrically, and their radial-mean representation converges pointwise to the canonical upper-semicontinuous value (including poles). The H^1 trace bound gives L^1(μ) convergence, so a subsequence identifies the trace with the canonical value μ-a.e.; non-polarity excludes mass on pole sets. The usual H^1 Sobolev chain rule and $L^1(\mu)$ Lipschitz estimate give the composition assertion. Neither step needs continuity of Q. This is a proof under the explicitly weaker assumptions, not a claim that every probability automatically has an H^1 Green potential.

### An explicit sharp threshold family

Choose a local affine coordinate z on P^1, r=|z|, a smooth radial cutoff χ supported in r<e^(−3) and equal to 1 for r≤e^(−4), and for p>1 set
$$
d\mu_p(z)=A_p\frac{\chi(r)}{r^2(\log(1/r))^p}\,dA(z)
$$
(with A_p chosen for probability mass one). Each μ_p is absolutely continuous with respect to area and therefore charges no polar set. In the inner disk,
$$
M_p(r):=\mu_p(\{|z|<r\})
 =\frac{2\pi A_p}{p-1}(\log(1/r))^{1-p}.
$$
The exact chordal Green kernel in this chart is
$G(z,w)=\log|z-w|^2-\log(1+|z|^2)-\log(1+|w|^2)+1$.
Angular averaging gives
$$
Q_p'(r)=\frac{2M_p(r)}r-\frac{2r}{1+r^2}.
$$
Its Dirichlet energy near zero has the same finiteness criterion as
$$
\int_0^{e^{-4}}\! \frac{M_p(r)^2}{r}\,dr
 \asymp \int_4^\infty t^{2(1-p)}\,dt.
$$
The potential is locally square-integrable for every p>1 (its growth is at most polynomial in log(1/r)). Therefore
$$
Q_p\in H^1(Y)\quad\Longleftrightarrow\quad p>\tfrac32.
$$
At the origin, $Q_p(0)=-\infty$ whenever $p\le2$, because the radial integral of $|\log r|$ against μ_p diverges. Thus for **3/2<p≤2**, the trace conclusion holds for a genuinely unbounded Green potential: its continuity hypothesis is not necessary.

The threshold **p=3/2 is sharp for bounded H^1→L^1(μ_p) extension**. If such an extension existed for 1<p≤3/2, then for all smooth h the functional $h\mapsto\int h\,d\mu_p$ would be bounded on H^1 (by the L^1 norm inequality). Hence $\mu_p-\kappa\in H^{-1}$; solving the mean-zero weak Poisson equation on the compact curve would produce a Green potential in H^1, contrary to the explicit divergent Dirichlet integral. This sharp negative result pertains to the trace extension under the family of densities, **not** to the original theorem, which assumes a continuous Q.

**Recommendation/dependents:** Optional conditional trace corollary stating non-polarity plus $Q\in H^1$ as an alternative hypothesis for only the trace/chain-rule clauses of Lemma 15.31.4; the explicit family distinguishes the trace threshold from pointwise continuity. Do not weaken the continuity hypotheses of Theorem 15.31.8 or the product Monge–Ampère results on the basis of this corollary.

## Actual coverage and limitations

New direct proof/model review: §16.18.1 (variable-upper-radius infimum, boundary curvature and penalty) and previously unverified §15.31.4 (measure trace under an explicit weaker hypothesis). The §15.31.3 curvature identity, the original SU(2) average and Sobolev density are selected internal inputs only, not full certifications. §5.53 was consulted for current sign conventions but nothing there is claimed as new; §15.5–6, which invoke the user-excluded Chern-connection Demailly regularization programme, were **not audited**. The collection's actual ToC retains **25 chapters and 747 numbered sections; zero sections fully certified**. Old findings and statuses remain unchanged.

The user's excluded Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss completion work remains **deferred-by-user**, neither resolved nor certified. No source text, permanent tag, proof registry, production main, website, GitHub Actions, or publication is changed. No builds, browser tests, software tests, or formal verification were run for these mathematical arguments.
