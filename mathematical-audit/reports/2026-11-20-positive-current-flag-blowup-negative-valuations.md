# 2026-11-20 — Flag-valuations of positive currents on iterated blowups

**Production baseline:** main \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Whole integrated §19.3:** \`docs/sections/the-theory-of-okounkov-bodies--flags-and-valuations/index.html\`, blob \`9190d2ae0d3e51ca0ca965000cb9b5b2ec965c85\`, all mathematical lines **7–387** directly checked: algebraic flags, analytic valuation via traces, comparison/additivity, birational correction and cocycle, flag-lifting and model-valuations. **Whole §19.10 also rechecked:** \`docs/sections/section-growth-of-semipositive-line-bundles/index.html\`, blob \`41526a319c45c861a8303776f155096d1f36614a\`, lines **7–22**, one corollary and proof; historically this section was already recorded as whole-reviewed. The inventory is 25 chapters / 747 sections, **not** a book-wide proof certification.

## POME-OKO-POSITIVE-CURRENT-UNBOUNDED-NEGATIVE-FLAG-001

**Severity:** low. **Classification:** verified conditional deduction, **not** a false printed theorem. **Primary anchors:** Definition 19.3.12 source \`sgpt:E615C683\` / permanent \`E494C67EB4B8\`, lines 162–179; equation (19.3.13), source \`sgpt:827D77FC\` / permanent \`63511F34173E\`, lines 163–175; Proposition 19.3.14, source \`sgpt:DD7439A2\` / permanent \`D094DD00A592\`, lines 183–237; Proposition 19.3.17 and equation (19.3.18), source \`sgpt:6A0E92BC\` / permanent \`8D2910CD1CEC\` and \`1C158885A628\`, lines 241–305; Definition 19.3.20, source \`sgpt:3E9C7256\` / permanent \`0887D96E8350\`, lines 336–346; normalization equation (19.3.21) permanent \`9DE3455479DE\`; Lemma 19.3.22, source \`sgpt:B8D45D42\` / permanent \`24E66EB949E4\`, lines 350–376.

### Exact example and complete calculation

Let \(X=\mathbb P^2\), with an affine chart \((x,y)\), and fix the smooth flag \(Y_\bullet=(X\supset C\supset\{p\})\) where \(C=\{x=0\}\), \(p=(0,0)\). Blow up \(p\), then blow up the intersection of the strict transform of \(C\) with the newest exceptional curve, repeating **\(r\ge1\)** times. Write \(\pi_r:Z_r\to X\), \(C_r\subset Z_r\) for the strict transform, \(E_r\) for the newest exceptional curve, and \(q_r=C_r\cap E_r\). The lifted smooth flag is \(W_\bullet=(Z_r\supset C_r\supset\{q_r\})\).

Use the blowup chart \(x=u_1v_1,\ y=v_1\). At each subsequent center use \(u_{j-1}=u_jv_j,\ v_{j-1}=v_j\). Induction gives local equations at the final flag point
\[
 x=u_rv_r^{\,r},\qquad y=v_r,\qquad C_r=\{u_r=0\},\quad E_r=\{v_r=0\}.
\]
The total pullback \(\pi_r^*[C]\) is locally the divisor of \(u_rv_r^r\). Therefore it has generic order \(1\) along \(C_r\) and residual order \(r\) on \(C_r\) at \(q_r\). By the geometric definition (19.3.13), or by the cocycle (19.3.18), its **row-vector** correction matrix is precisely
\[
 G_r=\operatorname{cor}(Y_\bullet,\pi_r)=
 \begin{pmatrix}1&r\\0&1\end{pmatrix},\qquad
 G_r^{-1}=\begin{pmatrix}1&-r\\0&1\end{pmatrix}.
\]
These are lexicographic order automorphisms. The inverse is **not** order-preserving componentwise, which matters for extended model valuations.

Take any **real** \(a,b\ge0\) and the positive closed current
\(S_{r,a,b}=a[C_r]+b[E_r]\) on the smooth projective surface \(Z_r\).
The first flag value is \(a\). After subtracting \(a[C_r]\), the residual positive divisor \(b[E_r]\) restricts classically to \(b[q_r]\) on \(C_r\), because the intersection is transverse. Thus its **upstairs** flag valuation is
\[
  \nu_{W_\bullet}(S_{r,a,b})=(a,b).
\]
Definition 19.3.20 allows choosing \(h=\mathrm{id}_{Z_r}\), since \(Z_r\) already has the lifted flag. With equation (19.3.21) the **model-normalized** valuation is
\[
 \boxed{\nu_{Y_\bullet}(S_{r,a,b})=(a,b)G_r^{-1}=(a,b-ra).}
\]
In particular, for the *effective* current \(S_r=[C_r]\),
\[
 \boxed{\nu_{Y_\bullet}([C_r])=(1,-r),\qquad
        \pi_{r*}[C_r]=[C].}
\]
The **second coordinate is unbounded below** across these smooth birational models even though every pushforward is the *same* fixed effective divisor current. More generally \(\pi_{r*}S_{r,a,b}=a[C]\), while the extended valuation is \((a,b-ra)\), making the discarded exceptional coefficient explicit. By contrast, the pullback current \(\pi_r^*[C]\) has upstairs valuation \((1,r)\), so
\[
  \nu_{Y_\bullet}(\pi_r^*[C])=(1,r)G_r^{-1}=(1,0)
       =\nu_{Y_\bullet}([C]).
\]
This checks the direction and sign of **pullback invariance** (Lemma 19.3.22) and shows why it cannot be replaced by a claim of general **pushforward invariance**. No printed theorem asserts the latter.

**Novelty boundary.** The 2026-11-04 \`POME-OKO-FLAG-TWO-BLOWUPS-001\` already established the two-step matrix shear for **rational functions**. That calculation is *not* a new finding here. The present new deduction concerns **positive current valuations extended to model currents**, all \(r\), arbitrary nonnegative real coefficients, arbitrarily negative normalized coordinates and fixed pushforward. The printed remark after (19.3.21) already correctly states that negative entries *can* occur, so this is an explicit quantitative illustration, **not** a contradiction.

**Proposed change (audit only):** optionally add the example \(\nu_{Y_\bullet}([C_r])=(1,-r)\) immediately after Definition 19.3.20, retaining the permanent tags and attribution. **Affected dependents:** interpretation of Definition 19.3.20, Lemma 19.3.22, and §19.4.7's model-valuations. This is not a proof of the full trace theory.

## Remaining direct review of §19.3

All statements and supplied arguments in §19.3 were read (lines 7–387). Algebraic flag valuations and changes of local units (Definition 19.3.2) have the expected lexicographic convention; Remark 19.3.3's converse classification is an attributed **external input**, not certified here. The current-valued constructions, \(\mathcal I\)-comparison and additivity in Propositions 19.3.7/9 are conditional on the precise trace hypotheses; the \(r\)-fold current example checks their sign and normalization **only in this analytic-divisor case**. Propositions 19.3.14/17 respect right multiplication for row vectors; there is no additional coefficient/factorial.

The prior **medium candidate** \`POME-OKO-FLAG-NESTED-RESOLUTION-001\` for the *printed proof* of Theorem 19.3.19 (source \`sgpt:44C3D868\` / permanent \`B00AB5301F7A\`, lines 319–331) remains unresolved **in production**: independently chosen embedded resolutions do not automatically give compatible inclusions. The 2026-11-14 \`POME-OKO-FLAG-AMBIENT-CENTERS-REPAIR-001\` supplies an **audit-only conditional repair**, not yet incorporated. The permitted deep inputs are Hironaka's domination/embedded resolution, with attribution preserved. The prior §19.3 trace typing question and visible equation label \`10.14\` remain **previously logged**, not re-registered as new findings or fixed in the reading edition.

Selected §20.2 prerequisite checks: \`docs/sections/the-trace-operator/index.html\`, blob \`1f3a3e4f0317a308b43bd3df53dda84c5f3fa50a\`, Proposition 20.2.8 lines 237–245, Proposition 20.2.21 lines 355–381, Lemma 20.2.24 lines 564–596. Only these statements and relevant links were checked. Their deeper analytic proofs have dependencies in the user's excluded programme and were **not reopened or certified**.

## Complete repeat reading of §19.10, without re-running its Morse programme

For \`docs/sections/section-growth-of-semipositive-line-bundles/index.html\`, entire mathematical lines 7–22, the permanent Corollary 19.10.1 tag is \`F31884F26A29\` (source \`demailly-complex-geometry:4B096A2D\`); displayed equation (19.10.2) tag \`2B3916324C79\` (source \`demailly-complex-geometry:15584614\`). The printed conclusion for a semipositive Hermitian line bundle is **conditionally** deduced from the quoted weak degree-zero and strong degree-one Morse inequalities: writing \(I_0=\int_X\Omega_L^n/n!\),
\[
 \limsup_{k\to\infty}k^{-n}h^0(X,L^k)\le I_0,\quad
 \liminf_{k\to\infty}k^{-n}(h^0-h^1)\ge I_0.
\]
The degree-one negative-curvature integral is zero. As \(h^1\ge0\), both inequalities force \(k^{-n}h^0\to I_0\), including the curve endpoint. Smooth semipositivity plus strict positivity at one point makes \(I_0>0\). This verifies the **printed deduction only**; the Morse inequalities themselves are not newly proved or certified, and the user's excluded Bergman/L²/regularization proof programme is untouched. No new printed §19.10 error; prior torsion-oscillation sharpness result not re-reported.

## Coverage and exclusions

**Two** whole sections directly read this session (§19.3 and §19.10); **one** newly advanced from historical partial to current whole direct reading (§19.3); §19.10 previously had \`HISTORIC-FULL-REPORTED\` status and is only a repeat; **three** selected §20.2 inputs; **zero** fully certified upstream proof chains. Historical first visits are *not* inferred. No tests, builds, CI, website publication or modifications to main, source/body, registry, canonicalization, or permanent tags. Demailly approximation/regularization and the dedicated Bergman, L², Ohsawa–Takegoshi, multiscale atlas and positivity-loss proof-completion programme remains **deferred-by-user**, not resolved or certified.
