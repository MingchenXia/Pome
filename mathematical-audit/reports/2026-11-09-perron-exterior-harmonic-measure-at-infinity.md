# Exterior-sphere Perron measure and the dimension-two polar end (2026-11-09)

**Stable finding ID:** POME-PERRON-EXTERIOR-INFINITY-ATOMIC-MASS-001  
**Severity / status:** **low / verified conditional deduction**. The original theorems are **not** false. This is an independently checked explicit Perron-model consequence, not a complete certification of compactified Perron theory.  
**Production main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **audit destination:** `review/mathematical-audit`.

## Exact integrated-reading anchors

The actual chapter-4 table of contents places this computation in **§4.4, Perron theory and fine boundary limits**. Direct reading-edition file: `docs/sections/perron-theory-and-fine-boundary-limits/index.html`, blob **`4bc2fb9317e2b6f6bb5b2d90208c677da8275eba`**.

- **Theorem 4.4.2**, source `classical-potential-theory:410B64F2`, permanent tag `09873BDAF3E0`, physical lines **10–35**: bounded-domain resolutivity/representing harmonic measures; ball Poisson formula used only as an established elementary input.
- **Theorem 4.4.12**, source `classical-potential-theory:7E1C8CAC`, permanent tag `8FA95EB71F47`, physical lines **152–166**: compactified superharmonicity and different polarity of the point at infinity in dimensions two and at least three.
- **Lemma 4.4.13**, source `classical-potential-theory:C1B6A087`, permanent tag `58BE7FB3C948`, physical lines **168–181**: Kelvin transformation and exterior harmonic functions.
- **Lemma 4.4.15**, source `classical-potential-theory:EFC4C537`, permanent tag `E0D6C3CD3750`, physical lines **184–202**: nondense compactified domains, weak barriers and regularity at infinity.
- **Lemma 4.4.16**, source `classical-potential-theory:0B575946`, permanent tag `5D12CB9707B5`, physical lines **204–224**: polar boundary exceptional sets.
- **Theorem 4.4.17**, source `classical-potential-theory:2870669A`, permanent tag `A7E357C38C8E`, physical lines **226–237**: compactified Perron resolutivity and completed harmonic measures.
- The standing Perron-class convention for the compactified case occurs immediately before Lemma 4.4.15, physical lines **184–185**: upper competitors are hyperharmonic and bounded below, with the prescribed boundary liminf.

## Exact statement

Let `d>=2`, `R>0`, and treat
\[
D_R=\{x\in\mathbb R^d:|x|>R\}
\]
as an open subset of the **one-point compactification**, with **infinity excluded from the domain**. Its compactified boundary is \(\partial B_R\sqcup\{\infty\}\); this must not be confused with including infinity as an **interior** point of an exterior domain. Let \(g\in C(\partial B_R)\), \(b\in\mathbb R\), and give the compactified boundary the continuous datum \(f=g\) on the sphere and \(f(\infty)=b\).

Write \(\sigma_{d-1}\) for the area of the **unit** \((d-1)\)-sphere and \(r=|x|>R\). The precise finite-boundary density with respect to the ordinary surface-area measure \(dS_R\) is
\[
Q_R(x,\zeta)=\frac{r^2-R^2}{\sigma_{d-1}R\,|x-\zeta|^d},
\qquad |\zeta|=R.
\tag{1}
\]
Its total mass is
\[
\int_{\partial B_R}Q_R(x,\zeta)\,dS_R(\zeta)=
\begin{cases}
1,&d=2,\\
(R/r)^{d-2},&d\ge3.
\end{cases}
\tag{2}
\]
Consequently the completed harmonic measure of **the boundary point infinity** is the **exact atom**
\[
\boxed{\omega_x(\{\infty\})=
\begin{cases}
0,&d=2,\\
1-(R/r)^{d-2},&d\ge3.
\end{cases}}
\tag{3}
\]
The Perron solution for the **entire continuous boundary datum** is
\[
\boxed{H_f(x)=
\int_{\partial B_R} Q_R(x,\zeta)g(\zeta)\,dS_R(\zeta)
+b\,\omega_x(\{\infty\}).}
\tag{4}
\]
Thus \(\omega_x\) is a probability measure with an explicitly normalized absolutely continuous spherical part and, in dimensions \(d\ge3\), an explicit **positive point mass** at infinity. The two components are not to be confused with a normalized Martin boundary kernel.

For \(d=2\), the solution **does not depend on \(b\)**; moreover,
\[
\lim_{r\to\infty}H_f(x)
=\frac{1}{\sigma_1 R}\int_{\partial B_R}g\,dS_R,
\tag{5}
\]
uniformly in the direction \(x/r\). Therefore infinity is **irregular**: a boundary value \(b\) different from this spherical average is ignored. For \(d\ge3\), \(\lim_{x\to\infty}H_f(x)=b\); infinity is **regular**, with the positive explicit barrier \((R/|x|)^{d-2}\).

## Proof with normalization and Perron quantifiers

**1. Kelvin pullback of the ordinary ball Poisson kernel.** Set \(I(x)=R^2x/|x|^2\). The inside-ball Poisson kernel, with respect to \(dS_R\), is
\[
P_R(y,\zeta)=\frac{R^2-|y|^2}{\sigma_{d-1}R|y-\zeta|^d},
\quad |y|<R,\quad|\zeta|=R,
\qquad \int_{\partial B_R}P_R(y,\zeta)dS_R=1.
\]
For \(d\ge3\), the Kelvin transform of a harmonic function on the ball is \((R/r)^{d-2}h(I(x))\); for \(d=2\) it is \(h(I(x))\). The elementary identities
\[
R^2-|I(x)|^2=\frac{R^2(r^2-R^2)}{r^2},\qquad
|I(x)-\zeta|=\frac Rr|x-\zeta|
\]
give exactly
\[
(R/r)^{d-2}P_R(I(x),\zeta)=Q_R(x,\zeta)
\]
in every integer dimension \(d\ge2\), with exponent zero in dimension two. This explicitly checks the factors \(R,\sigma_{d-1}\) and the surface measure convention. Integration proves (2). The function
\(A_g(x)=\int Q_R(x,\zeta)g(\zeta)dS_R(\zeta)\)
is harmonic, bounded, and tends to \(g\) at each point of the inner sphere.

**2. Higher-dimensional boundary point.** For \(d\ge3\), the harmonic function
\[
p_\infty(x)=1-(R/r)^{d-2}
\]
has zero boundary values on \(\partial B_R\) and limit one at boundary infinity. Hence \(A_g+b p_\infty\) is bounded harmonic and has all the prescribed compactified boundary values, so it belongs to both the Perron upper and lower classes. Compactified comparison (the printed Theorem 4.4.12) identifies the solution, establishing (3)–(4) in this case. The positive harmonic function \((R/r)^{d-2}\to0\) at infinity is a local weak barrier, establishing regularity without relying on a putative identification of Martin kernels with Perron probabilities.

**3. The two-dimensional point is polar, not a hidden Dirichlet condition.** For \(d=2\), \(A_g\) is bounded harmonic on \(D_R\) and extends continuously to the finite sphere. For each \(\varepsilon>0\), set
\[
U_\varepsilon(x)=A_g(x)+\varepsilon\log(r/R),\qquad
L_\varepsilon(x)=A_g(x)-\varepsilon\log(r/R).
\]
Both are harmonic and respectively **bounded below** and **bounded above** on \(D_R\). At the finite boundary they tend to \(g\); at boundary infinity, \(U_\varepsilon\to+\infty\) and \(L_\varepsilon\to-\infty\), regardless of the finite prescribed number \(b\). Hence \(U_\varepsilon\) is a legitimate compactified Perron **upper** competitor and \(L_\varepsilon\) a legitimate **lower** competitor, using precisely the class convention before Lemma 4.4.15. It follows pointwise that
\[
A_g-\varepsilon\log(r/R)\le\underline H_f
\le\overline H_f\le A_g+\varepsilon\log(r/R).
\]
Letting \(\varepsilon\downarrow0\) at each fixed finite point yields \(\underline H_f=\overline H_f=A_g\), proving resolutivity and complete **independence of \(b\)** without an interchange of a parameter limit with an unproved measure limit. Taking \(g\equiv0\), \(b=1\) proves \(\omega_x(\{\infty\})=0\) directly from the indicator's continuous-data representation in Theorem 4.4.17.

**4. The actual far-field law in dimension two.** In \(d=2\), formula (1) obeys
\[
Q_R(x,\zeta)\longrightarrow(\sigma_1R)^{-1}
\]
uniformly for \(\zeta\in\partial B_R\) and the direction \(x/r\) as \(r\to\infty\), because \(|x-\zeta|^2/r^2\to1\) uniformly. This proves (5). For \(d\ge3\), the spherical kernel is \(O(r^{2-d})\) uniformly on the inner sphere, so its contribution vanishes and (3) tends to one. No claim about irregularity is inferred merely from the size of the **Martin** kernel.

## Findings, action and exact coverage

- **Mathematical classification:** low / **verified conditional deduction**, not a false printed theorem, not an established proof gap, not an applied repair. The explicit Poisson/Kelvin computation and the two-dimensional upper/lower Perron sandwich are independently proved. General bounded-domain Poisson theory and compactified comparison/representation are retained as clearly stated **internal conditional inputs**; the general theories themselves are not certified.
- **Difference from old audit:** `POME-MART-EXTERIOR-BALL-INFINITY-001` (2026-11-02) computed **normalized Martin boundary kernels** and their minimality, rather than the **Perron probability law** for arbitrary continuous spherical data, its **atomic mass**, or the two-dimensional **logarithmic upper/lower class proof**. These statements must not be conflated or entered as a mathematical duplication.
- **Suggested production change (not applied):** add an optional example after Theorem 4.4.17 giving (1)–(5) and clarifying the distinction between *infinity as boundary point* and *infinity as interior point* (Theorem 4.4.11). Retain all source attribution, permanent tags and existing statements.
- **Affected dependent arguments:** compactified Perron and harmonic-measure use in §§4.4–4.5; any application transporting exterior-end Martin data into a compactified Dirichlet boundary condition. No downstream printed theorem is declared false.
- **Actual incremental review:** §4.4.12–17 selected hypotheses, Kelvin normalization, all-dimensional spherical measure and Perron boundary quantifiers. Earlier §4.4.11 and §4.5 Martin audit used only for comparison; not re-counted. **§4.4 was already partly visited: zero first visits, zero fully certified mathematical sections.** Existing project baseline: **25 chapters, 747 numbered sections, 0 fully certified mathematical sections**. Historical error, gap, external dependency and user-deferred ledgers remain unchanged; Demailly regularization, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale and positivity-loss completion remain **deferred-by-user**.
- **Repository restrictions:** audit Markdown notes only on `review/mathematical-audit`; no source/main edits, no canonicalization/tag changes, no CI/build/test/formal certification/automatic publication.
