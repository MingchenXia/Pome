# §17.18: Exact mixed-mass formula for a two-branch partial Legendre envelope

- **Finding:** \`POME-LEGENDRE-TWO-BRANCH-MIXED-MASS-001\`
- **Severity and status:** low; **verified conditional deduction**. This does **not** refute the printed Lemma 17.18.1 and is **not** a proof of all of its upstream analytical inputs.
- **Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
- **Integrated file:** \`docs/sections/partial-legendre-transforms-and-monge-ampere-mass/index.html\`, blob \`5d989cf765f5471ce1e2278ef39e2c69979eeb92\`, physical lines **7–63** (entire mathematical section).
- **Stable provenance:** section source \`transcendental-positive-cones:17B5480E\`, permanent tag \`12D395D414C1\`; Lemma 17.18.1 source \`transcendental-positive-cones:676C0E65\`, permanent tag \`C12669D1EC3D\`, printed lines **14–22**. Kiselman internal entry/permanent tag \`2C1A82803889\` at line 10. Smooth Schur-complement identity lines **27–40**, piecewise-affine segment and smoothing lines **42–58**, noncompact-fiber tail and non-pluripolar extension lines **60–62**.

## New precise corollary (local bounded case)

Let \`U\subset\mathbb C^n\` be open, let \`\varphi,\psi\in\mathrm{PSH}(U)\cap L^\infty_{\rm loc}(U)\`, and let \`a<b\` be real. On \`U\times\mathbb C^*\` put \`y=\log|\tau|^2\` and

\[
V(z,\tau)=\max\{\varphi(z)+ay,\;\psi(z)+by\}.
\]

Then \`V\` is locally bounded, rotation-invariant and plurisubharmonic, and the following equality holds **as positive Radon measures on the base**:

\[
\boxed{\quad
(\pi_U)_*(dd^c V)^{n+1}
=(b-a)\sum_{k=0}^{n}
(dd^c\varphi)^k\wedge(dd^c\psi)^{n-k}.
\quad} \tag{*}
\]

The right-hand side uses the classical bounded Bedford–Taylor mixed products, including the zeroth-power convention. No order relation between \`\varphi\` and \`\psi\` is needed. The pushforward is well defined despite nonproper \`\pi_U\`: (*) proves local finiteness and the proof controls mass at both fiber ends.

### Proof with all parameter and normalization factors

For every fixed \`z\`, the two branches intersect at \`y_0(z)=(\varphi(z)-\psi(z))/(b-a)\`. Taking the infimum directly gives

\[
\widehat V_\lambda(z)=
\begin{cases}
\displaystyle \frac{b-\lambda}{b-a}\varphi(z)
+\frac{\lambda-a}{b-a}\psi(z), &a\le\lambda\le b,\\
-\infty,&\lambda\notin[a,b].
\end{cases}
\]

Indeed, on either side of \`y_0\` the expression \`V-\lambda y\` is affine in \`y\` and is minimized at the joining point precisely when \`a\le\lambda\le b\`; outside this interval one affine tail tends to \`-\infty\`. At \`\lambda=a,b\` the displayed values still hold, so the **closed-endpoint local boundedness** assumed by Lemma 17.18.1 is verified, rather than silently omitted. The family is locally uniformly bounded in \`z\` over the whole parameter interval.

Apply the printed Lemma 17.18.1, set \`s=(\lambda-a)/(b-a)\`, and use the Bedford–Taylor multilinearity of locally bounded psh potentials:

\[
\begin{aligned}
(\pi_U)_*(dd^cV)^{n+1}
&=(n+1)(b-a)\int_0^1
\big((1-s)dd^c\varphi+s\,dd^c\psi\big)^n\,ds\\
&=(n+1)(b-a)\sum_{k=0}^n
{n\choose k}\left(\int_0^1(1-s)^k s^{n-k}\,ds\right)
(dd^c\varphi)^k\wedge(dd^c\psi)^{n-k}.
\end{aligned}
\]

For integers \`0\le k\le n\`, the beta integral is \`k!(n-k)!/(n+1)!\`; its product with \`{n\choose k}\` equals \`1/(n+1)\`. Hence every mixed term has coefficient **exactly \`b-a\`**, proving (*). This is a finite polarization argument, with no interchange of a net or passage through a non-pluripolar singular locus.

A separate smooth check is available by replacing the maximum with a convex log-sum-exp of the two harmonic-in-\`y\` branches. Its vertical slope varies monotonically from \`a\` to \`b\`; the Schur-complement determinant from lines 27–40 gives the same integral after \`d\lambda=V_{yy}\,dy\`. The bounded Bedford–Taylor monotone limit recovers the nonsmooth maximum and the printed tail control prevents fiber escape. This check does not independently certify the general Kiselman theorem or the entire dyadic reconstruction of Lemma 17.18.1.

### Normalization and geometric calibration

- In complex base dimension \`n=0\`, take \`\varphi=\psi=0\`. Then \`dd^c\max\{ay,by\}\` is carried by the circle \`|\tau|=1\` and has total mass \`b-a\`, consistent with \`d^cy=d\arg\tau/(2\pi)\` at integrated line 7.
- For \`n=1\` and smooth locally bounded psh branches, (*) becomes \`(b-a)(dd^c\varphi+dd^c\psi)\`, with no binomial factor 2 left over.
- With a smooth closed real \`(1,1)\` form \`\theta\` on a compact Kähler \`X\` and globally bounded \`\theta\`-psh \`\varphi,\psi\`, the same local-potential calculation gives
\[
(\pi_X)_*(\pi_X^*\theta+dd^cV)^{n+1}
=(b-a)\sum_{k=0}^n(\theta+dd^c\varphi)^k
\wedge(\theta+dd^c\psi)^{n-k}.
\]
Integrating over \`X\` and using Stokes for bounded Bedford–Taylor products yields the total mass \`(n+1)(b-a)\int_X\theta^n\`. The displayed global conclusion is **restricted to bounded potentials**, not the arbitrary-singularity non-pluripolar extension in printed line 22.

## Direct audit of the printed §17.18 proof

1. **Lines 7–10, 14–22:** checked the \`dd^c\` and angular normalization, closed parameter interval, finite transforms and forbidden outside slopes. The two-branch example satisfies every hypothesis explicitly.
2. **Lines 27–40:** the Schur complement accounts for the mixed \`z,y\` derivatives, and the coefficient \`n+1\` agrees with both base dimension zero and (*) for all \`n\`.
3. **Lines 42–58:** the smooth concave-segment computation has matching first derivatives at the region interfaces. The finite mesh argument relies on bounded Bedford–Taylor continuity. This is an **upstream dependency**, not a newly confirmed defect.
4. **Lines 60–62:** the proof explicitly deals with possible mass escape to \`y=\pm\infty\`; the parameter-end interval estimate is needed before pushing forward. The extension by zero across the common analytic set is about **non-pluripolar** products, not classical products with retained polar mass.

**Original verdict:** no confirmed false theorem or independent proof gap found in the one printed lemma. The corollary (*) is new *audit-level coverage* of this exact elementary two-branch instance, not a replacement proof of the full general lemma. The Kiselman minimum principle (tag \`2C1A82803889\`), the local Bedford–Taylor mixed monotone convergence and uniform local mixed-mass bounds remain unverified as complete upstream proof chains. The historical/source attribution is preserved.

**Dependents and proposed action:** add (*) as an optional, separately reviewable corollary near Lemma 17.18.1 if desired, retaining the existing lemma, its permanent tag and both classical-versus-non-pluripolar variants. It can be used as a test identity for test-curve/Legendre Monge–Ampère pushforwards; no specific downstream statement is asserted broken. No change to source, body, registry or canonicalization is requested.

**Actual coverage:** the entire integrated §17.18 mathematical content (physical lines 7–63, one lemma) directly read this run; **+1 complete direct section reading, +0 fully certified upstream chains**. Whether this is the first historical visit cannot be certified from the unreconciled older audits. The inventory still contains **25 chapters and 747 numbered sections**; no other section receives new whole-section status. The user-excluded Demailly regularization/Bergman/L²/OT/multiscale/positivity-loss programmes remain **deferred-by-user**, neither resolved nor reopened. No build, tests, CI, publication, main or permanent-tag modification performed.
