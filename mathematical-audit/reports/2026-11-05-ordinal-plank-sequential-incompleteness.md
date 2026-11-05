# Ordinal-plank restriction: a **sequence**, not merely a net, witnesses incompleteness (2026-11-05)

**Finding:** \`POME-LCS-ORDINAL-PLANK-SEQUENTIAL-DEFECT-001\` — **low / verified conditional deduction**. This is a strengthening of a correct example, **not** a false theorem or a completed transitive proof certification.

**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
**Integrated reading edition:** \`docs/sections/completions-and-locally-convex-quotients/index.html\`, main blob \`e2c6d25d35020ccefa739f04aa893e173f73c17e\`, physical lines **49–100**, especially the ordinal plank, edge topology, nonextension and original net at lines **53–93**.
**Stable original source label / permanent Pome tag:** Lemma 2.23.3 \`demailly-complex-geometry:69616994\` / \`5F1410BEA2F7\`. Relevant dependent Example 2.23.4: \`demailly-complex-geometry:8F41A0A7\` / \`B0973308F142\` (lines **95–107**). The previously established open-map and complete-source premises of Lemma 2.23.3 were checked as dependencies, **not recertified here**.

## Precise statement

Let \(\omega\) be the first infinite ordinal and \(\omega_1\) the first uncountable ordinal, each with the order topology, and use **exactly** the printed spaces
\[
P=[0,\omega_1]\times[0,\omega],\quad
X=P\setminus\{(\omega_1,\omega)\},\quad
H=[0,\omega_1)\times\{\omega\},\quad
V=\{\omega_1\}\times[0,\omega),\quad A=H\cup V.
\]
Let \(E=C_k(X)\), and \(F=r(E)\subset C_k(A)\), with **the subspace compact-open topology**, where \(r\) is restriction to \(A\). Define \(b\in C_k(A)\) to be \(1\) on \(H\) and \(0\) on \(V\), as in the printed proof.

There exists a **countable sequence** \(f_N\in F\), not merely a directed net, such that for every compact \(K\subset A\), \(f_N|_K=b|_K\) for all sufficiently large \(N\). Consequently \((f_N)_{N\ge1}\) is a Cauchy **sequence** in \(F\) with no limit in \(F\): \(F\) is **not sequentially complete**. The associated completed projective tensor counterexample of Example 2.23.4 also has an explicit sequentially approximable missing image point.

## Complete elementary proof of the new claim

For every positive integer \(N\), define a continuous scalar function on the **entire compact ordinal interval** \([0,\omega]\) by
\[
\phi_N(k)=
\begin{cases}
0,&k<N,\\
1,&N\le k<\omega,
\end{cases}
\qquad \phi_N(\omega)=1.
\]
Every finite ordinal \(k<\omega\) is isolated; near the limit ordinal \(\omega\), \(\phi_N\) is eventually constantly \(1\). Hence \(\phi_N\) is continuous. Put
\[
h_N(\alpha,s)=\phi_N(s),\qquad (\alpha,s)\in X,
\quad\text{and}\quad f_N=r(h_N)\in F.
\]
Indeed \(h_N\) is the restriction to \(X\) of the continuous projection-pullback \(\phi_N\circ\mathrm{pr}_2\) on the **whole product \(P\)**. On \(H\), \(f_N\equiv1=b\); on \(V\), \(f_N(\omega_1,k)=\mathbf1_{\{k\ge N\}}\).

For any compact \(K\subset A\), the set \(K\cap V\) is finite: \(V\) is clopen in \(A\) and its order topology is discrete, so \(K\cap V\) is compact and discrete. Choosing \(N\) larger than every finite ordinal appearing in \(K\cap V\), we obtain \(f_N=b\) **identically on \(K\)**. Thus \(f_N\to b\) in every compact-open seminorm \(p_K\) of \(C_k(A)\). The induced subspace topology on \(F\) makes \((f_N)\) Cauchy there.

For completeness, the obstruction \(b\notin F\) can be checked directly without any net-compactness assumption. If an extension \(g\in C(X)\) existed, \(g(\omega_1,k)=0\) for each finite \(k\); continuity at that point gives a countable ordinal \(\beta_k<\omega_1\) beyond which \(|g(\alpha,k)|<1/3\). Since the supremum of countably many countable ordinals is still below \(\omega_1\), choose \(\alpha_*<\omega_1\) larger than all \(\beta_k\). We would then have \(|g(\alpha_*,k)|<1/3\) for **all** finite \(k\), contrary to continuity at \((\alpha_*,\omega)\in H\), where \(g(\alpha_*,\omega)=1\). Hence \(b\notin F\).

If \((f_N)\) converged in \(F\), it would also converge to its \(F\)-limit in the Hausdorff ambient space \(C_k(A)\); uniqueness of limits forces this limit to be \(b\), contradiction. Thus \(F\) is not sequentially complete.

Finally Example 2.23.4 identifies the scalar projective tensor map with \(r:E\to\widehat F\), and \(\widehat F\) with \(C_k(A)\) in this model (the latter identification is an existing internal dependency). The **same sequence** \(r(h_N)\) explicitly approaches the missing point \(b\in\widehat F\setminus r(E)\). No claim about arbitrary projective tensor products of complete Fréchet spaces follows.

## Classification and proposed addition

**Status:** verified conditional deduction — the new sequential-Cauchy construction and nonextension are proved completely above; the broader printed open-quotient and completion identifications are retained as existing internal inputs. **Severity:** low (useful strengthening, no false source statement).

**Suggested non-invasive body addition:** After the final transfinite-net paragraph of Lemma 2.23.3, append the explicit \(\phi_N\circ\mathrm{pr}_2\) construction and conclude that its quotient target is not even sequentially complete. Keep the valid original \(\omega_1\)-indexed net (it illustrates non-first-countability); do not rewrite it as a sequence or claim it has a countable cofinal subnet. Example 2.23.4 can point to the sequential witness. Preserve the printed source attribution and permanent tags.

**Affected dependents:** Lemma 2.23.3 (precise completeness boundary), Example 2.23.4 (explicit failure of completed projective-tensor surjectivity), and general comparisons with Proposition 2.23.5 (Fréchet hypotheses remain essential but this is **not** a proof of that proposition).

**Coverage honesty:** only the indicated model and downstream scalar-tensor identification were independently rechecked. Lemma 2.23.1, Example 2.23.2, Proposition 2.23.5 and their long upstream dependency chains were **not** re-certified. No mathematical claim is made about any Demailly approximation/regularization theorem or the owner-excluded Bergman/weighted-\(L^2\)/OT/multiscale/positivity-loss programme.
