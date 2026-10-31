# 2026-10-31 — Capacity-tail control of unbounded weighted Bedford–Taylor products

## Immutable source and exact review scope

- Reviewed production **main**: **b6933b772f41b45918f7e25ed1afbbb1fd892272** (not edited).
- Primary integrated reading page: **docs/sections/bedford-taylor-products-and-local-capacity--quasi-continuity-and-convergence-in-capacity/index.html**; Git blob **464778b7ca6f1a456e36b24ecb4a0c93ab6948d3**.
- Definition **7.5.5**, source **foundations-of-pluripotential-theory:F3E0CD1A**, permanent **DAD5D0809372**, physical lines **83–89**: original-net local *outer* capacity convergence.
- Lemma **7.5.7**, source **foundations-of-pluripotential-theory:39398ED2**, permanent **880C30054932**, physical lines **124–166**: uniform Borel capacity domination of trace and coefficient-variation measures, and bounded quasi-continuous weight continuity. In particular, inspect lines **127–131, 140–148, 152–166**.
- Theorem **7.5.8**, source **foundations-of-pluripotential-theory:2B1AA42A**, permanent **42828E3BDDFA**, lines **171–185**: product continuity and weights under capacity convergence, with its printed sequence hypothesis.
- Model check: **docs/sections/relative-extremals-on-bounded-hyperconvex-domains/index.html**, blob **c6560283c5ff9e2587ffe93f7f2e7ba687105243**, Proposition **7.16.1**, source **klimek-pluripotential-theory:7B045988**, permanent **11F76749E371**, physical lines **17–23, 53–61**; Theorem **7.16.5**, source **klimek-pluripotential-theory:68BF935A**, permanent **08DA18E923C1**, physical lines **111–131 and 178–184**.
- Independently checked the original-net/sequence distinction in §7.6.1–2, source **foundations-of-pluripotential-theory**, main page **docs/sections/bedford-taylor-products-and-local-capacity--increasing-limits-and-exceptional-envelopes/index.html**, blob **5e763bdc928794938c37dc3c7a51cc406472d076**, permanent **A4C45B704647** and **D865A8538D7D**, physical lines **11–57, 63–77**. No extension of its increasing-*sequence* premise is asserted.

## POME-BT-WEIGHT-CAPTAIL-001 — low / verified conditional deduction

**Mathematical status:** The integrated statements just cited are **not disproved**. The result below is a stronger sufficient condition for *unbounded* Borel weights; it is conditional on Lemma 7.5.7's uniform capacity domination and its fixed quasi-continuous weight continuity. It is neither a verification of every Bedford–Taylor construction nor a repair of a false theorem. Prior IDs **POME-BT-NET-CAP-WEIGHT-001**, **POME-BT-WEIGHT-L1-OBSTRUCT-001** and **POME-CAP-WEIGHT-UNIFORM-BOUND-SHARP-001** remain separate. They address bounded-weight net continuity, failure of Lebesgue-Lp control, and failure after dropping a uniform bound without a replacement tail condition; none states the capacity-tail criterion here.

### Statement and quantitative estimate

Let \(B\Subset\mathbb C^n\) be a ball, \(\mathcal U\subset\operatorname{PSH}(B)\) locally uniformly bounded in absolute value, and \(0\le q\le n\). Let \((S_\alpha)_\alpha\) be a directed net of Bedford–Taylor currents

\[
 S_\alpha=dd^c u_{1,\alpha}\wedge\cdots\wedge dd^c u_{q,\alpha},
 \qquad u_{\ell,\alpha}\in\mathcal U,
\]

converging weakly to a positive current \(S\) of the same bidegree. Write \(\sigma_\alpha\) for either its trace measure or any of its coefficient measures (for coefficients, use total variation). For each compact \(K\Subset B\) and nonnegative Borel \(g\), define the *capacity-tail functional*

\[
 \mathfrak C_K(g)=\int_0^\infty
      \operatorname{Cap}_B^*\bigl(K\cap\{g>t\}\bigr)\,dt
      \ \in[0,\infty].
\]

It is an ordinary Lebesgue integral in the **threshold variable** \(t\), whose integrand is decreasing, and is not a limit along the directed net.

Lemma 7.5.7(1), monotonicity of outer capacity, and the layer-cake formula give a constant \(C_K\), independent of \(\alpha\), \(q\), and the selected coefficient, such that

\[
 \boxed{\quad
 \int_K g\,d|\sigma_\alpha|
    \le C_K\,\mathfrak C_K(g).
 \quad}\tag{A}
\]

A finite number of such estimates also controls pairing with any fixed compactly supported smooth test form.

Let \(f:B\to\mathbb R\) be **locally bounded and quasi-continuous** for \(\operatorname{Cap}_B\). Let each \(f_\alpha:B\to\mathbb R\) be finite Borel, without any uniform bound. Suppose

\[
 \boxed{\quad
 \mathfrak C_K(|f_\alpha-f|)\longrightarrow0
 \quad\text{on its original directed set for every }K\Subset B.
 \quad}\tag{B}
\]

Then \(f_\alpha S_\alpha\) is locally a well-defined order-zero current on a cofinal tail, and

\[
 \boxed{\qquad f_\alpha S_\alpha\rightharpoonup fS.\qquad}\tag{C}
\]

The same assertion holds for trace measures and individual coefficient measures. This permits locally unbounded amplitudes \(f_\alpha\) so long as their *integrated capacity tails*, rather than simply their fixed-threshold capacities, vanish.

### Proof, with the directed-net quantifier explicit

Fix a compact \(K\Subset B\). For any positive finite measure \(\mu\), Tonelli gives the exact identity

\[
 \int_K g\,d\mu=\int_0^\infty\mu(K\cap\{g>t\})\,dt.
\]

For \(\mu=|\sigma_\alpha|\), Lemma 7.5.7(1) gives \(\mu(E)\le C_K\operatorname{Cap}_B(E)\le C_K\operatorname{Cap}_B^*(E)\) for every Borel \(E\subset K\). Integrate this pointwise-in-\(t\) bound to prove (A). Since \(f\) is bounded on \(K\), condition (B) proves local \(L^1(|\sigma_\alpha|)\) integrability of each \(f_\alpha\) eventually: by the definition of convergence to zero, on some tail its functional is finite. Condition (B) also implies local capacity convergence: for every \(\delta>0\), monotonicity of the threshold superlevel sets yields

\[
 \delta\operatorname{Cap}_B^*(K\cap\{|f_\alpha-f|>\delta\})
 \le \int_0^\delta\operatorname{Cap}_B^*(K\cap\{|f_\alpha-f|>t\})\,dt
 \le\mathfrak C_K(|f_\alpha-f|).
\]

For fixed test form \(\eta\) supported in \(K\), estimate (A) for each of the finitely many coefficient-variation measures gives

\[
 |\langle(f_\alpha-f)S_\alpha,\eta\rangle|
    \le C_{\eta,K}\mathfrak C_K(|f_\alpha-f|)\longrightarrow0.
\]

By Lemma 7.5.7(2), the fixed locally bounded quasi-continuous weight satisfies \(fS_\alpha\rightharpoonup fS\). Its *fixed-weight* argument also works for an arbitrary directed net: choose the exceptional open set **first**, with capacity \(<\varepsilon\); extend \(f\) continuously off this set; use the weak convergence of \(S_\alpha\) for that continuous extension; control the exceptional part uniformly by \(C_K\varepsilon\); then let \(\varepsilon\downarrow0\). No subsequence compactness or sequential dominated-convergence argument is required. Add the two terms to obtain (C).

For comparison, if \(|f_\alpha|,|f|\le M_K\) on \(K\), the same functional obeys for \(0<\delta<2M_K\)

\[
 \mathfrak C_K(|f_\alpha-f|)
 \le\delta\operatorname{Cap}_B(K)
 +(2M_K-\delta)\operatorname{Cap}_B^*
          (K\cap\{|f_\alpha-f|>\delta\}).
 \tag{D}
\]

Thus the *printed bounded-weight hypothesis plus local capacity convergence* implies (B) **along the original net**: take a limsup in (D) for fixed \(\delta\), then \(\delta\downarrow0\). This is a quantitative refinement of the old one-threshold error estimate, not a repeated proof of the already registered net theorem.

### Exact threshold and obstruction on a disc

Fix \(B=\mathbb D\), \(j\in\mathbb N\), \(\beta>0\), and put \(r_j=e^{-j^\beta}\). The relative extremal of the closed disc \(E_j=\{|z|\le r_j\}\) and its (normalized) Bedford–Taylor measure are

\[
 u_j(z)=\max\{-1,j^{-\beta}\log|z|\},\qquad
 dd^c u_j={1\over2j^\beta}\,\lambda_{r_j},
 \qquad
 \operatorname{Cap}_{\mathbb D}(E_j)={1\over2j^\beta},
\]

where \(\lambda_r\) is normalized angular probability on the circle \(|z|=r\); these factors follow from \(dd^c\log|z|^2=\delta_0\). The potentials are uniformly bounded in \([-1,0]\) and tend to zero locally in capacity, while \(dd^c u_j\rightharpoonup0\). For the unbounded Borel weights

\[
 f_j(z)=j\,\mathbf 1_{E_j}(z),\qquad f=0,
\]

the capacity of each fixed-threshold exceptional set tends to zero. For every fixed \(K\Subset\mathbb D\) containing a neighborhood of \(0\), however,

\[
 \mathfrak C_K(|f_j|)
 =j\,\operatorname{Cap}_{\mathbb D}(E_j)
 ={1\over2}\,j^{1-\beta},\qquad
 f_j\,dd^cu_j
 ={1\over2}\,j^{1-\beta}\lambda_{r_j}.
\]

Hence **\(\beta>1\)** gives unbounded weights satisfying (B) and weighted convergence to zero. At **\(\beta=1\)**, local capacity convergence still holds but the tail functional remains \(1/2\) and \(f_jdd^cu_j\rightharpoonup\frac12\delta_0\ne0\). For \(0<\beta<1\), the weighted masses diverge. This is an *exact*, nonarithmetic threshold for the new sufficient condition, not a claim that the condition is logically necessary for all weighted convergence problems. The model is distinct from earlier fixed-smooth-factor examples because the moving bounded Bedford–Taylor potential itself supplies exactly the small capacity mass.

A separate **net trap**: index finite subsets \(F\) of \([0,1]\) by inclusion, and take \(g_F=\mathbf1_{[0,1]\setminus F}\). Then \(0\le g_F\le1\) decreases pointwise to zero along the directed net, yet \(\int_0^1g_F\,dx=1\) for **every** \(F\). Thus *pointwise convergence of a bounded net* does not justify exchanging net limits and integrals by a sequential dominated-convergence theorem. The proof above uses the stronger capacity-tail hypothesis and an explicit uniform \(\delta\)-estimate instead.

### Status, repair proposal, dependencies and exact coverage

- **Status:** low / **verified conditional deduction**. No false Pome theorem is asserted, and no proof gap in the cited printed lemma is claimed. The condition (B) is sufficient, not asserted necessary.
- **Proposed nonproduction addition:** after Lemma 7.5.7, optionally state (A) and the tail-vanishing extension (B)–(C), with the \(\beta=1\) warning. Preserve the existing lemma, its hypotheses, source labels, attribution, and permanent tags.
- **Affected dependents only subject to checking their hypotheses:** the weighted conclusion of Theorem 7.5.8, local weighted energy/measure limits in Chapter 7, quasi-continuous weighted limits in §13.12, and any coefficientwise weighted-current argument using Lemma 7.5.7. **No** statement of these dependents is newly certified.
- **Actually reviewed this session:** the capacity and variation bounds in §7.5.7, original-net capacity definition §7.5.5, sequence-only §7.5.8, the specific comparison of §7.6.1, and the one-dimensional extremal/capacity normalization in §7.16.1/.5. These pages were previously sampled; this is **new quantitative proof-level work**, not a first-time whole-section review.
- **Remaining gaps:** existence and full dependency verification of all general Bedford–Taylor products, complete Borel-capacity theory, unbounded signed-weight integrability without (B), full downstream theorems and global models. No arbitrary-net increasing BT theorem is inferred.
- **Project accounting:** 25 actual current chapters, 747 numbered sections, **zero fully mathematically certified sections**. Existing unresolved, confirmed, conditional and deferred ledger statuses remain unchanged. The author-excluded Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion program remain **deferred-by-user**, not examined.
- **No claim of execution:** no project build, tests, numerical script, CI, formal proof, publication or production/source/tag change was performed for this report.
