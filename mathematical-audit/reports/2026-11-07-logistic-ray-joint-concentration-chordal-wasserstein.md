# 2026-11-07 — Joint concentration of the explicit Legendre ray and sharp chordal transport

**Finding ID:** `POME-RWN-LOGISTIC-JOINT-YOUNG-W1-001`.  
**Classification:** low severity; **verified conditional deduction** (conditional only on the explicit displayed ray formula). **No false printed theorem and no proof repair are asserted.**

## Provenance and exact scope

- **Production `main` reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Actual integrated reading-edition file:** `docs/sections/test-curves-and-legendre-duality/index.html`; blob SHA `704ed205a974fe18e2dc502b13ceaf382b4af4b3`.
- §17.17.9 setup and Fubini–Study unit-mass convention: **physical lines 184–195**; source `non-kahler-pluripotential-theory:E70193C4`, permanent subsection `58086AECC383`.
- Equation (17.17.10), test-curve obstacle: **lines 197–202**; source `non-kahler-pluripotential-theory:CB283DA0`, permanent tag `3B7363400CA2` (context only).
- Proposition 17.17.11: **lines 205–212, proof 214–242**; source `non-kahler-pluripotential-theory:42E4DFA8`, permanent tag `377F0AD20B28`.
- Equation (17.17.12), **lines 207–211, proof interpolation 235–241**: source `non-kahler-pluripotential-theory:1A6C8986`, permanent tag `9BA75154C113`.
- Note after the proposition **lines 245–246** distinguishes the bounded slices from the singular inverse transforms.

This audit reviews **only** the precise smooth model and its consequences. The original test-curve/ray correspondence, Perron maximality, nonclosed Hermitian extension, and upstream singularity-envelope results are **not** globally certified. The previous finding `POME-RWN-LOGISTIC-RAY-ENERGY-001` already computed the marginal uniform velocity law and energy; those are explicitly **not** counted as new findings here. No Demailly approximation, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas or positivity-loss argument was opened.

## Statement: a joint Young-measure limit with exact transport rate

Take \(X=\mathbb P^1\), \(\theta=dd^c\log(1+|z|^2)\), \(\int_X\theta=1\), and the explicit family printed in (17.17.12)
\[
 U_t(z)=\log\frac{1+e^t|z|^2}{1+|z|^2},\quad t>0.
\]
Put \(\mu_t=\theta+dd^cU_t\), \(v_t=\partial_tU_t\), and
\[
 \nu_t=(z,v_t(z))_*\mu_t\in\mathcal P(\mathbb P^1\times[0,1]).
\]
Use the chordal distance
\[
 \chi(z,w)=\frac{|z-w|}{\sqrt{(1+|z|^2)(1+|w|^2)}},\qquad
 \chi(z,0)=\frac{|z|}{\sqrt{1+|z|^2}}
\]
on the Riemann sphere (extended continuously at infinity), and \(d((z,a),(w,b))=\chi(z,w)+|a-b|\) on the product.

**Claim.** As \(t\to+\infty\),
\[
 \mu_t\rightharpoonup\delta_0,\qquad
 \nu_t\rightharpoonup\delta_0\otimes\mathbf1_{[0,1]}(\lambda)\,d\lambda,
 \tag{A}
\]
but for **every finite** \(t>0\),
\[
 \|\mu_t-\delta_0\|_{\mathrm{TV}}=
 \|\nu_t-(\delta_0\otimes d\lambda)\|_{\mathrm{TV}}=2.
 \tag{B}
\]
Here \(\|\cdot\|_{\mathrm{TV}}\) is the full signed-measure variation norm, twice the usual probability-TV distance. More quantitatively, writing \(W_1^\chi\) and \(W_1^d\) for 1-Wasserstein distances in the indicated metrics,
\[
 \begin{aligned}
 W_1^d(\nu_t,\delta_0\otimes d\lambda)
 &=W_1^\chi(\mu_t,\delta_0)\\
 &=\int_0^\infty\frac{2e^t r^2}{\sqrt{1+r^2}(1+e^t r^2)^2}\,dr
 =\left(\frac{\pi}{2}+o(1)\right)e^{-t/2}.
 \end{aligned}\tag{C}
\]
Thus the exponent \(1/2\) and leading constant \(\pi/2\) are sharp for the chosen chordal metric. In particular, **position collapses to a point while the velocity coordinate retains a nontrivial uniform law**.

## Direct proof

For the normalization \(dd^c=\frac{i}{2\pi}\partial\bar\partial\), the model yields on the affine chart
\[
 \mu_t=dd^c\log(1+a|z|^2)
 =\frac{a}{\pi(1+a|z|^2)^2}\,dx\,dy,\qquad
 v_t(z)=\frac{a|z|^2}{1+a|z|^2},\quad a=e^t.
 \tag{1}
\]
The formula extends smoothly to \(z=\infty\); neither \(\mu_t\) nor \(\theta\) has atoms there. Its radial probability density is \(2ar(1+ar^2)^{-2}dr\). Set \(w=\sqrt a\,z\); the pushforward of \(\mu_t\) under this scaling is the fixed \(\theta\)-probability, with density \(\pi^{-1}(1+|w|^2)^{-2}d^2w\), and
\[
 v_t(z)=V(w):=\frac{|w|^2}{1+|w|^2}.
 \tag{2}
\]
For \(0\le b<1\), the radial cumulative distribution is
\[
 \theta\{V\le b\}
 =\int_0^{\sqrt{b/(1-b)}}\frac{2r}{(1+r^2)^2}\,dr=b.
 \tag{3}
\]
Thus \(V_*\theta\) is uniform on \([0,1]\), confirming only the **previously recorded** marginal law.

For every bounded continuous \(F\) on \(X\times[0,1]\),
\[
 \int F\,d\nu_t
 =\int_X F(a^{-1/2}w,V(w))\,d\theta(w).
 \tag{4}
\]
For \(\theta\)-almost every \(w\ne\infty\), \(a^{-1/2}w\to0\), and bounded convergence plus (3) gives (A). The same proof with \(F\) independent of the second coordinate gives \(\mu_t\rightharpoonup\delta_0\). Notice that \(v_t(z)\to1\) for every fixed \(z\ne0\), whereas \(v_t(0)=0\). Substitution of either pointwise limit into a limiting position measure would incorrectly erase the nontrivial velocity law; equation (4) is the necessary **joint** limit statement.

For each finite \(t\), (1) shows \(\mu_t\{0\}=0\) and hence \(\mu_t\perp\delta_0\). Similarly \(\nu_t\bigl(\{0\}\times[0,1]\bigr)=0\), whereas the target joint law is supported there. Mutual singularity proves (B).

Any coupling of \(\mu_t\) to \(\delta_0\) is forced to transport each \(z\) to \(0\), so \(W_1^\chi(\mu_t,\delta_0)=\int\chi(z,0)\,d\mu_t(z)\). Any coupling of the joint laws costs at least this much because projection onto \(X\) is 1-Lipschitz; conversely the explicit coupling
\[
 (z,v_t(z))\longmapsto (0,v_t(z))
\]
has the correct target law by (3) and cost precisely \(\int\chi(z,0)d\mu_t\). The two distances therefore coincide **exactly**, not merely asymptotically.

Using (1) and the substitution \(s=\sqrt a\,r\),
\[
 W_1^\chi(\mu_t,\delta_0)
 =\int_0^\infty \frac{2s^2}{(1+s^2)^2\sqrt{a+s^2}}\,ds.
 \tag{5}
\]
After multiplication by \(\sqrt a\), the integrand is bounded by \(2s^2/(1+s^2)^2\in L^1(0,\infty)\) and converges pointwise to it. Dominated convergence and \(s=\tan\alpha\) give
\[
 \lim_{t\to\infty}e^{t/2}W_1^\chi(\mu_t,\delta_0)
 =2\int_0^\infty \frac{s^2}{(1+s^2)^2}\,ds
 =2\int_0^{\pi/2}\sin^2\alpha\,d\alpha
 =\frac{\pi}{2}.
 \tag{6}
\]
This proves (C) with no input from smoothing, singular Monge–Ampère continuity, or the general Perron correspondence.

## Mathematical classification and dependents

- **What is verified:** exact joint position–slope weak convergence, failure of TV convergence, and sharp chordal \(W_1\) for this one **smooth explicitly printed** projective-line ray. All limits use a fixed reference probability and an explicit domination argument; no moving-measure dominated-convergence shortcut is used.
- **Not a false theorem:** Proposition 17.17.11 and equation (17.17.12) remain valid; the example does not repair or invalidate them.
- **No hidden generalization:** nothing is proved for arbitrary envelope rays, singular metric backgrounds, non-pluripolar products, or general infinite-energy test curves. The scalar momentum marginal and \(E_\theta(U_t)=t/2\) were already established in `POME-RWN-LOGISTIC-RAY-ENERGY-001` and are not reclassified.
- **Proposed correction:** no edit to production mathematics. If presenting geodesic mass limits near §17.17.11/17.17.12 or transporting slopes in §§17.8/17.13, distinguish weak joint convergence from total variation and do not replace a varying integration measure by its weak limit before accounting for the velocity.
- **Affected dependents:** explanatory uses of the exact ray in §17.17, the normalization example in §17.8, and any inference from weak convergence of ray Monge–Ampère measures to a pointwise-limit slope distribution. **No affected printed theorem has been shown false.**
- **Remaining gaps:** the general Perron/geodesic/test-curve theorem chains and their internal envelope dependencies remain unverified; existing error/gap/external-dependency statuses remain unchanged. Owner-excluded Demailly approximation/regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss work stays **deferred-by-user**, neither resolved nor certified.
- **Precise new coverage:** selected smooth-model consequence of §§17.17.9–11, especially equation (17.17.12) and the mass-one normalization. This section was **already partially audited**; **0 new first section visits and 0 complete mathematics-section certifications**. Collection inventory remains **25 chapters, 747 numbered sections, 0 fully certified sections**.

This is an audit note only. No production source, permanent tag, registry, publication, CI job, build or formal verification was changed or claimed.
