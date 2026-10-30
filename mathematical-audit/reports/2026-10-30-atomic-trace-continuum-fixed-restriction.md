# 2026-10-30 — A full continuum of atomic trace masses with the same ordinary restriction

**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
**Finding:** \`POME-TRACE-ATOMIC-INTERPOLATION-001\` — **low / verified conditional deduction**, not a false printed theorem and not a proof-gap allegation.
**Scope:** a self-contained compact projective product model, explicit multiplier-ideal stalk computations, and selected integrated implications in §§20.3 and 20.4. No full section or general approximation theorem is certified.

## Pinned reading-edition evidence

- \`docs/sections/restriction-and-intrinsic-trace-data/index.html\`, main blob \`dbc3b722ceacb8232fe4c7b711e5ad98b0708f06\`:
  - §20.3 opening hypotheses, **physical lines 7–16**, and restricted image ideal \`I(tu) O_Y\`, **23–32**.
  - Theorem **20.3.2**, source \`non-kahler-pluripotential-theory:BF417B5C\`, permanent tag **\`7CD874C73EC9\`**, **36–67**; limiting trace formula Eq. 20.3.3, source \`2D477734\`, permanent **\`66AFB7F7397B\`**, **36–41**.
  - Proposition **20.3.6**, source \`non-kahler-pluripotential-theory:04472093\`, permanent **\`FE94B20EED19\`**, **129–160**; its existing single strict local example, **165–177**.
  - Theorem **20.3.10**, source \`non-kahler-pluripotential-theory:C5D10418\`, permanent **\`879739B42EBB\`**, **226–272**; mass Eq. 20.3.11 tag **\`29F47A0F8A5D\`** and Poisson Eq. 20.3.12 tag **\`57C6BC849EC1\`**.
  - Proposition **20.3.13**, permanent **\`B3BE3C08418A\`**, **290–309**: dominated total-variation convergence and ordinary restriction comparison.
- \`docs/sections/divisorial-currents-on-compact-modifications/index.html\`, main blob \`79d6e21f9d3784bf3761846f77f90ad075253644\`: §20.4.1, **30–47**, Theorem **20.4.2**, source \`non-kahler-pluripotential-theory:E6DD8E29\`, permanent **\`A67FA9DFB4BC\`**, **51–82**, and mass Eq. 20.4.3 permanent **\`B7771456202C\`**, **51–58**.

## Model and exact statement

Let \`X = P^1_z × P^1_w\`, \`Y = {z=0} × P^1_w\`, and \`p=(0,0) ∈ Y\`.
Use Fubini–Study forms \`omega_z, omega_w\` on the respective factors, each normalized to integral one on its projective line. Let
\[
\phi_z=\log\frac{|z|^2}{1+|z|^2},\qquad
\phi_w=\log\frac{|w|^2}{1+|w|^2},
\qquad \theta=\omega_z+\omega_w,
\]
globally interpreted as logarithms of the Fubini–Study squared norms of the corresponding hyperplane sections. Thus
\[
dd^c\phi_z=[z=0]-\omega_z,\qquad
dd^c\phi_w=[w=0]-\omega_w.
\]
Define the increasing convex \`C^1\` function \`F:(-\infty,0]\to\mathbb R\` by
\[
F(t)=
\begin{cases}
-\log(-t), & t\le -2,\\
-\log 2+(t+2)/2, & -2\le t\le0.
\end{cases}
\]
It has \`0 ≤ F' ≤ 1/2\`, \`F(-\infty)=-\infty\`. Put \`h=\max\{\phi_w,F(\phi_z)\}\` and, for **every** \`s∈[0,1]\`, \`u_s=s\phi_w+(1-s)h\` (with the obvious endpoint definitions).

Then:
1. Each \`u_s ∈ PSH(X,theta)\`, its generic Lelong number along \`Y\` is zero, and its *ordinary restriction is literally identical* for all parameters:
   \[
   u_s|_Y=\phi_w,\qquad \nu(u_s|_Y,p)=1.
   \]
2. Writing \`D_w={w=0}⊂X\`, for **every real** \`t>0\` the complete ambient multiplier ideal is
   \[
   \boxed{\mathcal I(tu_s)=\mathcal O_X(-\lfloor st\rfloor D_w).}
   \]
   Its image on \`Y\` is \`\mathcal O_Y(-\lfloor st\rfloor p)\`. Consequently
   \[
   \boxed{\tau_{Y,u_s}(p)=s,\quad \tau_{Y,u_s}(q)=0\ (q\ne p),\quad D_{u_s}=s\delta_p.}
   \]
   All atomic masses \`0≤s≤1\` are realized **with the same restriction**.
3. With \`\eta=\omega_w|_Y\`, the canonical atomic-trace potential of Theorem 20.3.10 can be chosen **exactly**
   \[
   v_s=s\phi_w|_Y,\qquad
   \theta|_Y+dd^cv_s=s\delta_p+(1-s)\omega_w|_Y.
   \]
   The extended/non-pluripolar curve measure is \`(1-s)omega_w|_Y\`, the total trace mass is \`s\`, and the §20.4 divisorial current on the identity curve model is \`S_Y(u_s;Y)=s[p]\`.
4. At finite integer level \`m≥1\`, \`D_{m,Y}=(\lfloor ms\rfloor/m)\delta_p\`, with **exact** dual total-variation error
   \[
   \|D_{m,Y}-D_{u_s}\|_{\mathrm{TV}}=s-\frac{\lfloor ms\rfloor}{m}\in[0,1/m).
   \]
   The constant \`1\` in this uniform \`1/m\` bound is optimal over \`s∈[0,1]\` for every fixed \`m\`: take \`s=(1-\varepsilon)/m\`.

## Direct proof, including the endpoint and all-real-weight integrability

The identity \`dd^c\phi_z=[z=0]-\omega_z\` is the ordinary Poincaré–Lelong identity with the project's \`dd^c=(i/2\pi)\partial\bar\partial\` convention; likewise for \`\phi_w\`. Since \`F\` is increasing and convex with slope at most \`1/2\`, \`dd^c F(\phi_z)\ge -(1/2)\omega_z\` in the sense of currents (one may use smooth convex approximants to the elementary piecewise-\`C^1\` function \`F\`; no analytic-singularity approximation or Bergman construction is involved). Both \`\phi_w\` and \`F(\phi_z)\` are therefore \`\theta\`-psh, as is their maximum \`h\`; convex combinations with \`\phi_w\` preserve the same common lower bound. The generic point of \`Y\` has \`w\ne0\`, and there \`F(\phi_z)\to-\infty\` as \`z\to0\`, so \`h=\phi_w\` in a neighborhood. Hence \`u_s\` is smooth near generic \`Y\` and its restriction is \`\phi_w\` everywhere, including the pole \`p\`.

Write \`k=\lfloor st\rfloor\`. Away from \`D_w\` all \`u_s\` are locally bounded; away from \`z=0\` on \`D_w\`, the function \`h\` is locally bounded near \`w=0\`, so \`u_s=s\log|w|^2+O(1)\`. One-variable polar integration gives the local ideal \`(w^k)\`, *including when \`st\` is an integer*, because integrability requires strictly \`j+1>st\`.

It remains to check the crossing point \`p=(0,0)\`. There
\[
e^{-tu_s}=e^{-st\phi_w}e^{-t(1-s)h}
 \le C|w|^{-2st}\bigl(-\phi_z\bigr)^{t(1-s)}
 \le C'|w|^{-2st}(1+|\log|z|^2|)^{t(1-s)}
\]
on a sufficiently small product chart, using \`h≥F(\phi_z)\`. For the generator \`w^k\`, its squared modulus times this weight is locally integrable: the \`w\` radial exponent satisfies \`k-st>-1\` and
\[
\int_0^\varepsilon r\,(1+|\log r^2|)^q\,dr<\infty
\quad(q\ge0).
\]
Thus \`(w^k)\subseteq\mathcal I(tu_s)\` at \`p\`. Conversely, if a holomorphic germ at \`p\` had a nonzero coefficient of \`w^j\` for any \`j<k\`, that coefficient would remain nonzero for generic nearby \`z\ne0\`. Along the smooth part of the divisor \`D_w\`, where \`h\` is bounded, the same one-variable integral would diverge. Therefore every ideal germ is divisible by \`w^k\` at \`p\`. This proves the **global sheaf equality** for every \`t>0\`, without invoking any regularization theorem or external extension estimate.

Restriction of the principal ideal gives exactly \`(w^k)\mathcal O_Y\`, so \`b_t(p)=\lfloor st\rfloor\`, \`b_t(q)=0\` for other \`q\`. Division by \`t\` proves the trace formula directly; there is no exchange of limits or sequential-compactness assumption. The curve identity \`dd^c\phi_w=\delta_p-\omega_w\` proves the Poisson formula and its positivity for every \`s∈[0,1]\`. For \`s>0\` the atom lies on the polar set of \`v_s\` and is discarded by the extended measure, while for \`s=0\` there is no atom. The finite-level formula follows from the same exact integer part. For any fixed \`m\` and \`0<\varepsilon<1\`, \`s=(1-\varepsilon)/m\` makes \`ms<1\`, giving defect \`(1-\varepsilon)/m\`, and establishes optimality.

## Audit disposition and dependencies

The printed inequality \`\tau_{Y,u}(E)\le\nu(u|_Y\circ\pi,E)\` (Prop. 20.3.6) is **correct**, and its existing local \`s=0\`-type example already shows strictness. This new compact family is **not** a restatement of that example: it realizes every intermediate trace mass with one and the same ordinary restriction, identifies the **complete ambient ideal at each real weight**, computes the canonical curve trace and residual Monge–Ampère measure, and gives the sharp exact finite-level error. It also tests the curve case of Thm. 20.4.2: \`\int_Y S_Y=s\le\int_Y\theta=1\`, with equality at \`s=1\`. These are only **model checks** of the cited general statements, not transitive proofs of them.

**Proposed optional addition:** after the strict example at physical lines 165–177 of §20.3, add a compact global interpolation remark referencing the exact \`\lfloor st\rfloor\` ideal formula, and cross-reference the explicit Green/Poisson representative after Eq. 20.3.12. **Affected interpretations:** §20.3.6 ordinary restriction vs intrinsic divisorial trace; §20.3.10/.13 atomic trace measures and finite-level convergence; §20.4.2 mass normalization; downstream §20.2 trace constructions. No change to the original statements, historical attribution or permanent tags is required.

**Excluded scope:** this argument uses only standard convex composition, the displayed Poincaré–Lelong identity and elementary polar integrals. The existing §20.3 proofs refer to analytic approximants; those dependencies are **deferred-by-user** and are neither opened nor certified here. The dedicated Demailly regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remains wholly excluded. No source/body/registry/main/site modifications; no build, CI, formal proof or publication.
