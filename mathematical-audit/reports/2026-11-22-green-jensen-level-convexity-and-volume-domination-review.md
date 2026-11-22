# Green-envelope and boundary-flux review; singularity-volume comparison and domination

**Date:** 2026-11-22. **Main baseline:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Review branch:** `review/mathematical-audit`. **Finding:** `POME-GREEN-JENSEN-LEVEL-CONVEXITY-001`, low / **verified conditional deduction**, not a refutation of a printed theorem. **Complete transitive proof-chain certifications:** zero.

## Exact integrated reading-edition coverage

All mathematical prose, statements and proofs (not site chrome) in the following five current-main sections were read directly. This records current reading, **not** first-ever historical visits and **not** certification of their entire upstream proof trees.

| Section | Exact integrated file | Git blob | Mathematical lines | Section source tag |
| --- | --- | --- | --- | --- |
| §7.17 | `docs/sections/isolated-pole-green-envelopes-and-continuity/index.html` | `e82b6baaa0061f55aeea2f88ec0567d9653ecd61` | 7–146 | `3360BE3E2E50` (7.17.1); section tags via current chapter TOC |
| §7.20 | `docs/sections/green-level-measures-and-boundary-representation/index.html` | `895dbdfaa3c78ce41abe556f573644d857ab7517` | 7–132 | `1359A4B6C1D8` (7.20.1) |
| §13.17 | `docs/sections/volumes-under-bounded-mass--comparison-of-singularity-volumes/index.html` | `7d55ffb2d7cb91897029a9a2101788eb8aa70141` | 7–78 | `32986EE97902` |
| §13.18 | `docs/sections/volumes-under-bounded-mass--volume-deficits-and-relative-full-mass/index.html` | `28323e5b08b0f7e53567f641bd9e4223472bc331` | 7–111 | `E8D1B2CE6F8F` |
| §13.19 | `docs/sections/volumes-under-bounded-mass--domination-and-ordinary-envelopes/index.html` | `aa11cda5105062bb7d7b5eaaa1396940c679e097` | 7–215 | `832E0568D7C3` |

Also inspected §13.16, `docs/sections/volumes-under-bounded-mass/index.html`, lines 8–26 **only as an upstream hypotheses check**. Its lines 20–23 impose a compact connected bounded-mass manifold and a **big smooth (possibly nonclosed) background** for §§13.17–13.27. Thus the use of a strictly positive `theta+dd^c rho` in §13.17.2, lines 65–77, is supported by an inherited hypothesis and is **not** a missing-bigness error. This §13.16 visit is selected, not another full-section review.

## New mathematical finding: convexity of the radial Green–Jensen means

**ID:** `POME-GREEN-JENSEN-LEVEL-CONVEXITY-001`. **Severity/status:** low / verified conditional deduction. **Anchor:** Proposition 7.20.2, permanent tag `351C8FCB17FF`, lines **48–80**, especially the exact level-slice identity (lines **68–80**). This is a strengthening of the printed monotonicity, **not** an original theorem error, and is conditional on the existence and finite weighted integral of the mixed measure proved there.

Let $D\subset\mathbb C^n$ be bounded hyperconvex, $a\in D$, $g=g_D(\cdot,a)$, $m_n=2^{-n}$, and $v\in\mathrm{PSH}(D)\cap C(D)$. Set
\[
\nu=dd^c v\wedge(dd^c g)^{n-1},\qquad
F(r)=\int_D v\,(dd^c\max(g,r))^n,\qquad r<0.
\]
The mixed measure is understood in the **one-point full-classical** sense of §7.20.2. Then **$F$ is finite, nondecreasing, continuous and convex** on $( -\infty,0)$. Writing $H(t)=\nu(\{g<t\})$, its exact one-sided derivatives are
\[
F'_-(r)=H(r)=\nu(\{g<r\}),\qquad
F'_+(r)=H(r+)=\nu(\{g\le r\}).
\]
Consequently, as distributions/measures on the **finite-level** interval $( -\infty,0)$,
\[
\boxed{\quad F''=g_*\big(\nu|_{D\setminus\{a\}}\big)\quad}
\]
and $F'_+(r)-F'_-(r)=\nu(\{g=r\})$. No mass at $g=-\infty$ is incorrectly treated as a finite-level atom. Every nonnegative level mass is measured exactly by a jump in the slope. This adds a potentially useful second-order regularity principle to the source's first-order Jensen monotonicity.

**Complete justification.** Proposition 7.20.2 proves
\[
F(r)=m_n v(a)+\int_{-\infty}^{r}\nu(\{g<t\})\,dt.
\]
For any $r<R<0$, its finite weighted integral on $B(R)=\{g<R\}$ bounds $\nu(B(r))$ by
$(R-r)^{-1}\int_{B(R)}(R-g)\,d\nu<\infty$. Hence $H$ is finite and locally bounded. It is nondecreasing and *left-continuous* because $\{g<t\}\uparrow\{g<r\}$ as $t\uparrow r$. Continuity from above for finite measures on $B(R)$ gives $H(r+)=\nu(\{g\le r\})$. Integral averages from the left and right now yield the asserted one-sided derivatives. For a compactly supported test $\phi$ in $(-\infty,0)$, the distributional derivative of $H$ is the pushforward of $\nu$ under the measurable map $g$ restricted to finite levels, establishing the identity. Monotonicity of $H$ proves convexity. This uses genuine measure-theoretic continuity and never assumes absence of level-set atoms, smoothness of $g$, or sequential compactness of currents.

**Exact sharp kink example.** Take $n=1$, $D=\mathbb D$, $a=0$, $g(z)=\log|z|$, and $v(z)=\max(\log|z|,c)$ with $c<0$. It is continuous subharmonic. The level measure $\beta_r$ has mass $m_1=1/2$, supported uniformly on $|z|=e^r$, and therefore
\[
F(r)=\tfrac12\max(r,c),\qquad \nu=dd^cv=\tfrac12\sigma_{|z|=e^c}.
\]
Thus $F''=\tfrac12\delta_c=g_*\nu$, proving that one cannot generally strengthen $F\in C^0\cap\mathrm{Convex}$ to $C^1$, or assume that the boundary Jensen means have no slope jumps. The factor $1/2$ is exactly the project's $dd^c=i\partial\bar\partial/(2\pi)$ normalization.

**Correction:** none to the printed statement. **Optional addition:** after §7.20.2 record the convexity, distributional second derivative and one-sided slope formulas, with the disc kink as a sharpness example. **Affected dependents:** Jensen boundary representation §7.20.3, the ball/polydisc kernels §7.20.4, and any deductions from Green level sets; this is an optional strengthening, not a defect in these dependents.

## Other independent proof checks, preserving existing hypotheses

**§7.17.1–2** (permanents `3360BE3E2E50`, `7B9EA3C07531`, lines 11–48): inner/outer logarithmic pole bounds come from linewise subharmonic maximum principles; shrinking/removing a relatively closed pluripolar subset uses PSH removability. A possibly unbounded balanced gauge does not silently acquire boundedness: the source proves the pointwise upper estimate before claiming equality under the extra PSH condition on `log h`. The nonconvex balanced-domain witness is an independent geometric example.

**§7.17.3–5** (permanents `2CC830293978`, `5A3A24549BAA`, `518349DA23E4`, lines 53–117): the proper-map Green estimates use the **joint** single-fiber and growth assumptions for the stated exponents, with the reverse implication recovered by local logarithmic asymptotics. The hyperconvex continuity proof squeezes $g$ between $B h_\delta$ and $A h_\delta$, and its $O(1/A)$ local bound uses $B-A=\log(R/r)$, independent of $\delta$. The pole-variable comparison is on the complement of a chosen neighborhood; diagonal continuity is into the extended-real topology. Decreasing Green envelopes on an increasing domain exhaustion are checked using a fixed local pole bound.

**§7.17.6–8** (permanents `B016253F39B4`, `465EA6ED94FB`, `34EFBF9EA39F`, lines 122–146): the planar Green sign and $2\pi$ convention are consistent with the two upstream normalizations, while uniqueness is a two-sided maximality comparison with strict boundary perturbations. The $p=5/2$ complex-norm example only disproves an unjustifiably general *smoothness* claim, not continuity of the Green function on a bounded hyperconvex domain; that repair already appears in the integrated text and is **not** a newly registered error.

**§7.20.1–4** (permanents `1359A4B6C1D8`, `351C8FCB17FF`, `EC62871F80C4`, `438C4583CB39`, lines 11–132): the regular-level coefficient $n(F_\epsilon')^{n-1}F_\epsilon''$ integrates to one, so there is no missing factor $n$; with outward level orientation the flux is positive. The mixed classical measure is obtained by polynomial interpolation followed by compact-support Stokes, not by an unjustified interchange of a moving-level weak limit. The boundary representation has factor $2^n=m_n^{-1}$ and the correct sign because $g<0$. The ball Poisson–Szegő density has $n$-th power, while the polydisc density is a product of one-dimensional kernels; neither is a spherical *harmonic* Poisson formula in higher dimensions.

**§13.17** (permanents `D7019DA65027`, `1C00C4C5A656`, lines 20–77): lower volume monotonicity uses a rooftop $P_{\theta_1}(u_1+t,v_2)$ and shrinking pole-level error; upper volume uses $\max(v_1,u_2-t)$. The added-current monotonicity compares obstacles by $P_\theta(w-v)$. The shared bigness hypothesis is **inherited** from §13.16 (lines 20–23), not missing in the proposition.

**§13.18** (permanents `92ABF533A916`, `169DBA6BAF3B`, `D73DFBAE1EC1`, lines 11–111): when $b^nD<\delta$, bounded-mass estimates on $w_j\sim v$ and the lower mass $\delta$ contradict collapse of the stretched envelopes. The modification Lelong bound uses a fixed $C_\pi$ and a limit $b\uparrow(\delta/D)^{1/n}$; $D=0$ requires $b\to\infty$ separately. The zero upper-volume deficit implies the relative envelope condition only under positive lower-volume hypotheses. Its converse does not need that positivity.

**§13.19** (permanents `B390F0847B3A`, `50A87754E163`, `CB29AE1DFDA3`, `C0F29EF85157`, `B0CCD40EE4B7`, lines 11–215): domination uses a stretched contact set with coefficient $(1-b^{-1})^n>c$, not a naive strict comparison of masses everywhere. The relative obstacle envelope's vanishing measure off contact follows from weighted quasi-continuous tests. The ordinary-envelope volume equality retains positive lower-volume hypotheses. The isolated Hausdorff-zero pole-set result distinguishes local full products at the pole from the non-pluripolar mass off it; uniform lower-degree current trace bounds and subsequential uniqueness are needed, rather than an unproved top-degree weak convergence alone. The unreviewed entire upstream theorem 7.28.1 and the full bounded-product/capacity proof trees remain dependencies, not completed certificates.

## Classifications and outstanding work

**New:** one low / verified conditional deduction only. **Confirmed new false theorems:** zero. **Confirmed new proof gaps:** zero. **Potential open upstream proof-tree checks:** the precise one-point classical full-product §7.28.1, capacity-continuity lemmas §5.29.19/§13.14.8, and the nonclosed-background contact theorem §15.8.6. No claim that these external/internal inputs have been completely independently certified here. Comparison of hypotheses rather than titles showed that the tempting §13.17.2 bigness objection is invalid because §13.16 imposes bigness explicitly.

**Actual increment:** 5 complete current direct integrated section readings; 1 selected prerequisite (§13.16); 1 new conditional deduction; 0 complete transitive proof-chain certifications; no claim of historical first visits. Current TOC denominator remains 747 distinct reader sections. All Demailly approximation/regularization and the dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programmes are **deferred-by-user**, neither resolved nor certified. No builds/tests/CI, main, source, registry, body, permanent-tag or website mutations.
