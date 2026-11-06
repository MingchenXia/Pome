# 2026-11-07 — A countable increasing finite-join realization of non-Archimedean Choquet suprema

**Finding:** \`POME-NA-CHOQUET-FINITE-JOIN-EXHAUSTION-001\`  
**Classification:** low / **verified conditional deduction** (the printed statements are not false).  
**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Scope:** precisely Proposition 22.1.37 and its finite-join/supremum inputs, with the test-curve Choquet input checked at Proposition 17.15.31. This is **not** certification of either complete section.

## Integrated source and permanent anchors

- \`docs/sections/non-archimedean-pluripotential-theory/index.html\`, blob \`8448d710690ebe1cc28040f9611d05c9d008a961\`: Definition 22.1.31 / Proposition 22.1.32 at physical lines **504–521**; Definition 22.1.34 / Proposition 22.1.36 at **539–561**; Proposition **22.1.37** and its proof at **566–591**. Main source label **\`sgpt:284D07DA\`**, permanent tag **\`21737B0303A5\`** (Proposition 22.1.37).
- \`docs/sections/test-curves--operations-on-test-curves/index.html\`, blob \`3da617be8f58713f764d49ba22f49b803149a5e8\`: Definition 17.15.25 at physical lines **592–613**, Proposition **17.15.31** at **662–719**. Source label **\`sgpt:6B576942\`**, permanent tag **\`4B67ABC0083D\`**.
- The conditional upstream input is local Choquet selection for \(\theta\)-psh families (Proposition 5.14.3) together with the integrated test-curve comparison and compatibility lemmas cited in 17.15.31 and 22.1.36. No approximation/regularization programme is used or reviewed.

## Precise strengthened consequence

Let \(X\) be a connected compact Kähler manifold, \(\theta\) a smooth representative of a pseudo-effective class, and \((\Gamma^i)_{i\in I}\) a nonempty family in \(\mathrm{PSH}^{\mathrm{NA}}(X,\theta)\) with \(M:=\sup_i\Gamma^i_{\max}<+\infty\), as in Definition 22.1.34.

**Claim.** There exists a sequence \(i_1,i_2,\ldots\) of indices (repetitions permitted) and an **increasing sequence of finite joins**
\[
F_N:=\Gamma^{i_1}\lor\cdots\lor\Gamma^{i_N}
\]
such that, in the **defined upper-regularized non-Archimedean supremum sense**,
\[
\operatorname*{sup}_{N\ge1}{}^{*}F_N
=\operatorname*{sup}_{i\in I}{}^{*}\Gamma^i. \tag{1}
\]
Moreover, fix a Kähler form \(\omega_0\). For every pair \((m,q)\) with \(m\in\mathbb N_{>0}\) and \(q\in\mathbb Q\), \(q<M\), the increasing sequence of \((\theta+m^{-1}\omega_0)\)-psh functions
\[
\bigl(P_{\theta+m^{-1}\omega_0}[F_N]_{\mathcal I}\bigr)_q
\]
has upper-regularized pointwise supremum equal to the \(q\)-level of the corresponding component of the right-hand side of (1). In each such coordinate and level, the pointwise increasing limit equals that upper-regularized value **outside a locally pluripolar set**. One locally pluripolar exceptional set works **simultaneously for all these countably many coordinate/level pairs**. No claim is made of everywhere convergence, of convergence for all uncountably many real levels, or of sequential compactness of the underlying inverse-limit space.

### Proof

1. Choose \(\omega_0\). The forms \(\omega_0/m\) are **cofinal for the required inverse-limit direction**: for every Kähler \(\omega'\), compactness and positive definiteness give \(\omega'\ge\omega_0/m\) for some \(m\). In each positive-volume component \(\theta+\omega_0/m\), the genuine test-curve Choquet Proposition 17.15.31 selects a countable \(I_m\subset I\) reproducing its upper-regularized supremum. Set \(I'=\bigcup_m I_m\).
2. For \(\omega'\ge\omega_0/m\), apply the *verified formula being assumed* in Proposition 22.1.36: the \(\mathcal I\)-envelope transition commutes with the defined upper-regularized supremum. Its use is in this direction only, from the smaller Kähler perturbation \(\omega_0/m\) to the larger \(\omega'\). Hence the \(I'\)-supremum and the \(I\)-supremum agree in **every** Kähler coordinate, so they agree as inverse-limit objects. This reproduces the key logical step of printed Proposition 22.1.37 rather than positing a convergent subnet.
3. Enumerate \(I'\) with repetitions when finite, as \(i_1,i_2,\ldots\). By associativity and monotonicity of finite joins (Propositions 22.1.32–33), \(F_N\le F_{N+1}\). The upper-regularized supremum of these finite joins is exactly the supremum of the countable family, by Definition 22.1.34 (or its finite-subset definition). This proves (1).
4. For each \(m,q\), the projected \(q\)-level is an increasing family of \((\theta+\omega_0/m)\)-psh functions. The local Choquet/monotone-psh lemma gives equality of the pointwise limit with its upper-semicontinuous regularization outside a locally pluripolar exceptional set \(E_{m,q}\). The union \(\bigcup_{m,q}E_{m,q}\) is locally pluripolar by the local countable-union property. This establishes the simultaneous **countable** level assertion without any invalid interchange with an uncountable collection of \(\tau\)-levels.

### Finite-stage nonattainment is genuine

Take \(X=\mathbb P^1\) with its normalized Fubini–Study Kähler form \(\theta\). For \(j\ge2\), put \(a_j=1-1/j\) and use the elementary constant model test curve
\[
\Gamma^{(j)}_\tau=
\begin{cases}
0,&\tau\le a_j,\\
-\infty,&\tau>a_j.
\end{cases}
\]
These are valid \(\mathcal I\)-model test curves: every finite level is the zero model potential, the maximal parameter is \(a_j\), and \(\operatorname{vol}(\theta)>0\). Every finite join of members has maximal parameter \(\max_{j\in J} a_j<1\), whereas the upper-regularized supremum of the entire family has maximal parameter \(1\) and is the same constant model curve with threshold \(1\). For any chosen finite \(J\) and any \(\max_{j\in J}a_j<\tau<1\), the finite join has level \(-\infty\) while the full supremum has level \(0\). Therefore **no finite stage can realize the full supremum**, despite exact countable determination.

There is also a **sharp endpoint warning**. With the extension convention of Remark 17.12.3, the supremum curve has level (0) at its new endpoint (	au=1) (the infimum of all levels with (	au<1)), while each individual curve, extended by (-infty) for arguments exceeding its own maximum, satisfies (Gamma^{(j)}_1equiv-infty). Thus
\[
\left(\operatorname*{sup}_{j\ge2}{}^{*}\Gamma^{(j)}\right)_1=0
\quad\text{but}\quad
\left(\sup_{j\ge2}\Gamma^{(j)}_1\right)^*=-\infty.
\]
The Choquet assertion is an assertion **in the category of test curves with their own maxima**, not an unwarranted exchange between the supremum and endpoint extension at a moving maximal parameter.

 This is a model illustrating a necessary distinction between *countably generated* and *finitely generated* upper suprema; it does not refute the printed Choquet statement.

## Disposition and affected results

- **No false theorem, proof gap, or unconditional repair has been established.** The proposed optional explanatory addition to Proposition 22.1.37 is the explicit finite-join exhaustion and the simultaneous *countable-coordinate* quasi-everywhere statement.
- The pointwise-to-USC regularization operation remains indispensable. The proof does **not** upgrade increasing-level convergence to arbitrary nets/levels, and does not assert continuity of volume, Duistermaat–Heckman measures, or trace under this operation. Downstream consumers of NA suprema (especially 22.1.39, 22.1.50 and 22.1.60) must continue to check their own hypotheses.
- All prior ledger classes and user-deferred Demailly regularization/Bergman/L²/OT/multiscale/positivity-loss work remain unchanged. **No section is certified in full.**
