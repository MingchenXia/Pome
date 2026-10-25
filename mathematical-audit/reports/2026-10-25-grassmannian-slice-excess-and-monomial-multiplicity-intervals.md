# 25 October 2026 — exact Grassmannian slice-excess identity and attainable monomial multiplicity intervals

## Version, scope, and audit boundaries

- **Reviewed `main` commit:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Starting audit branch head:** `c080a549e4e5208cf8e95daa8eef2bb238d38336`.
- **Primary new selected proof-level coverage:** §6.41, specifically Lemma 6.41.1, Theorem 6.41.2, Lemma 6.41.4, Proposition 6.41.5, Lemma 6.41.7, and Proposition 6.41.9. Cross-checks in §6.33.1.
- **Incremental direct checks:** §6.47.1–2 and their §6.46.1–2 finite-map inputs; §6.43.1–2 finite-germ degree inputs. The 22 October ledger already mentions selected checks in §§6.43–6.44 and 6.46–6.48; these are **not** falsely presented as first coverage. No entire section certified.
- **Out of scope:** all dedicated Demailly regularization/approximation, Bergman, `L²`, Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof-completion work. No inference of correctness of these deferred arguments.
- The source-reader proof passages were inspected; no software build, CI, formal verification or publication was performed. Neither source bodies nor permanent tags have been edited.

## POME-GRASSMANN-SLICE-L1-EXCESS-001

**Severity:** low. **Status:** verified conditional deduction (the printed theorem is correct). **Nature:** a quantitatively useful, exact consequence of the already printed finite-radius averaging identity, stronger than its expressly stated Lelong-number inequality.

**Source:** `docs/sections/lelong-densities-generalized-masses-and-multiplicity--concurrent-slices-of-positive-currents/index.html`, main blob `a851fa12c59217cbf13efd381fd44524388fcfdc`; Proposition 6.41.9, original source label `demailly-complex-geometry-CE3E3EB2`, permanent tag `BAA80DBD5575`, HTML lines 132–159; Equation 6.41.10, tag `D71CDC8687A9`, lines 134–137. The constructed slices depend on Proposition 6.41.5, tag `F5E0CCA7AC78`, lines 67–106, and almost-everywhere slicing Theorem 6.41.2, tag `53506FB921EB`, lines 32–58.

Let \(T\) be a closed positive \((c,c)\)-current on the ball \(B(0,R)\subset\mathbb C^n\), and let \(c\leq q\leq n\). For almost every \(S\in G(q,n)\) the **specific concurrent slice constructed in §6.41.5** is a closed positive current \(T_S\) on \(S\) of bidimension \(d=q-c\). Let \(\nu_q\) be invariant probability on \(G(q,n)\), and write \(D_T(a)\) and \(D_{T_S}(a)\) for the normalized finite-radius Lelong densities used in §6.41.9. In particular, for \(a>0\),

\[
D_T(a)\geq\nu(T,0),\qquad
D_{T_S}(a)\geq\nu(T_S,0)
\]

by the Lelong–Jensen monotonicity in §6.33.1. All functions of \(S\) below are defined a.e.; the integral uses \(\nu_q\).

**Claim (exact mass defect and \(L^1\) convergence).** For every \(0<a<R\),

\[
\boxed{\displaystyle
\int_{G(q,n)}\nu(T_S,0)\,d\nu_q(S)=\nu(T,0),
}
\]

\[
\boxed{\displaystyle
\int_{G(q,n)}
\bigl[D_{T_S}(a)-\nu(T_S,0)\bigr]\,d\nu_q(S)
=D_T(a)-\nu(T,0).
}
\]

Consequently the nonnegative density excess \(E_a(S)=D_{T_S}(a)-\nu(T_S,0)\) satisfies

\[
\boxed{\ \|E_a\|_{L^1(\nu_q)}
   =D_T(a)-\nu(T,0)\longrightarrow0\quad(a\downarrow0).\ }
\]

For every \(\delta>0\),

\[
\nu_q\!\left\{S:E_a(S)>\delta\right\}
\leq\frac{D_T(a)-\nu(T,0)}{\delta}.
\]

The \(L^1\) convergence is valid along **any directed net** of radii \(a_i\to0^+\), not only along sequences. This statement is *conditional on the existence and averaging identity for the specific slices established in §§6.41.2–9*; it is not an independent full proof of those analytic inputs.

**Proof.** The printed Equation 6.41.10 gives, at each fixed radius,
\(\int_{G(q,n)}D_{T_S}(a)\,d\nu_q=D_T(a)<\infty\).
Choose \(a_0<R\) and any sequence \(a_j\downarrow0\) with \(a_j\leq a_0\). For almost every \(S\), the positive closed slice has Lelong–Jensen monotonicity, hence
\(D_{T_S}(a_j)\downarrow\nu(T_S,0)\) and
\(0\leq D_{T_S}(a_j)\leq D_{T_S}(a_0)\).
The latter is integrable by 6.41.10. Dominated convergence gives

\[
\int\nu(T_S,0)\,d\nu_q
=\lim_j\int D_{T_S}(a_j)\,d\nu_q
=\lim_j D_T(a_j)=\nu(T,0).
\]

The exact excess identity follows by subtraction from 6.41.10; nonnegativity makes its integral its \(L^1\) norm. Lelong–Jensen on \(T\) makes the right side tend to zero. Markov's bound follows. The resulting estimate is pointwise in **every** radius \(a\), so it applies directly to any net \(a_i\to0\) without extracting a subnet. \(\square\)

**Relationship to the source:** the final sentence of the printed proof (line 158) itself observes that dominated convergence gives equality of the Lelong-number averages, although the displayed conclusion of Proposition 6.41.9 only states \(\leq\). The new contribution recorded here is the exact finite-scale \(L^1\) excess and the uniform-in-radius quantitative tail bound; **neither observation signals a false theorem or a missing proof**.

**Proposed action:** optional explicitly tagged corollary after Proposition 6.41.9, without altering source numbering, original attribution or permanent tags. **Affected dependents:** any argument turning almost-everywhere concurrent slice density into average Lelong-number bounds, including later estimates that can benefit from an exact \(L^1\) error modulus. The existence/positivity of slices and the incidence normalization remain upstream, independently un-certified in full.

## POME-MONOMIAL-MULTIPLICITY-INTERVAL-001

**Severity:** low. **Status:** verified conditional deduction, strengthening sharpness to **attainment of every intermediate value**, not a counterexample to the printed inequalities.

**Sources:**
- `docs/sections/lelong-densities-generalized-masses-and-multiplicity--monomial-maps-and-the-sharp-directional-comparison/index.html`, main blob `bad5cd9bb63a90871462700f5c1f7080c597ee99`; Proposition 6.47.1, original `demailly-complex-geometry-F608EF8B`, tag `0A17C5BE0625`, lines 7–31, and Corollary 6.47.2, original `demailly-complex-geometry-9E33C486`, tag `240191846A51`, lines 33–47.
- `docs/sections/lelong-densities-generalized-masses-and-multiplicity--proper-direct-images-and-finite-map-upper-bounds/index.html`, blob `1f44c5feb546ecfe43ec1bc752d3fd0bff501613`; Theorems 6.46.1–2, tags `86EB492BC979` and `751F9003E019`, lines 7–64.
- `docs/sections/lelong-densities-generalized-masses-and-multiplicity--finite-germs-and-their-actual-integer-degree/index.html`, blob `e2a86c5438c7770a8766f6bedf779e1879ead4c0`; Proposition 6.43.1 tag `AD7655D0958A`, Lemma 6.43.2 tag `B1AA1442D441`, lines 7–55.

Let \(1\le p\le n\), \(1\le s_1\le\cdots\le s_n\) be integers and \(F(z)=(z_1^{s_1},\ldots,z_n^{s_n})\). Put \(A=\prod_{j=1}^{p}s_j\), \(B=\prod_{j=n-p+1}^{n}s_j\). Define the set of normalized pushforward ratios over local closed positive currents of bidimension \(p\) with \(\nu(T,0)>0\):

\[
\mathcal R_p(F)=
\left\{\frac{\nu(F_*T,0)}{\nu(T,0)}:
       T\ge0,\ dT=0,\ \operatorname{bidim}T=(p,p),\ \nu(T,0)>0
\right\}.
\]

Theorem 6.46.1–2 and Proposition 6.47.1 give \(\mathcal R_p(F)\subseteq[A,B]\). **In fact**

\[
\boxed{\mathcal R_p(F)=[A,B].}
\]

The same full-interval assertion holds for the directional numbers in Corollary 6.47.2: for \(0<\lambda_1\le\cdots\le\lambda_n\), and \(\rho_\lambda(z)=\max_j\lambda_j\log|z_j|^2\),

\[
\boxed{\left\{\frac{\nu(T,\rho_\lambda)}{\nu(T,0)}:
T\ge0,\ dT=0,\ \operatorname{bidim}T=(p,p),\ \nu(T,0)>0\right\}
=
\left[\prod_{j=1}^p\lambda_j,\ \prod_{j=n-p+1}^n\lambda_j\right].}
\]

**Proof.** For each \(p\)-element subset \(J\subset\{1,\ldots,n\}\), let \(V_J\) be the coordinate \(p\)-plane with nonzero coordinates exactly those indexed by \(J\). The closed positive integration current \([V_J]\) has \(\nu([V_J],0)=1\), by the normalized Euclidean Lelong density. The finite map induced by \(F\) on \(V_J\) is a product of one-variable powers with degree \(d_J=\prod_{j\in J}s_j\). Holomorphic covering-degree counting away from coordinate hyperplanes, together with the zero coefficient mass of proper analytic exceptional sets, gives

\[
F_*[V_J]=d_J[V_J],\qquad
\nu(F_*[V_J],0)=d_J.
\]

Choose \(J_-=\{1,\ldots,p\}\) and \(J_+=\{n-p+1,\ldots,n\}\), yielding \(d_{J_-}=A\), \(d_{J_+}=B\). For any \(t\in[A,B]\), if \(A<B\) take \(\theta=(t-A)/(B-A)\) and

\[
T_\theta=(1-\theta)[V_{J_-}]+\theta[V_{J_+}].
\]

Then \(T_\theta\) is closed positive, \(\nu(T_\theta,0)=1\), and \(\nu(F_*T_\theta,0)=t\), by linearity of ordinary densities. If \(A=B\) use either plane. This proves the first assertion, including \(p=n\); \(p=0\) gives the singleton \(\{1\}\) by the measure convention.

For the directional claim, the restriction of \(\rho_\lambda\) to \(V_J\) is
\(\max_{j\in J}\lambda_j\log|z_j|^2\). If the coefficients are positive integers, this differs by a bounded quantity from
\(\log\sum_{j\in J}|z_j|^{2\lambda_j}\).
The isolated coordinate complete-intersection degree (Lemma 6.43.2) thus gives its top pole mass as \(\prod_{j\in J}\lambda_j\). Positive homogeneity gives the same for positive rationals; coordinatewise weight comparison and a two-sided \((1\pm\varepsilon)\) squeeze give continuity for positive reals (the same argument as Corollary 6.47.2). Hence

\[
\nu([V_J],\rho_\lambda)=\prod_{j\in J}\lambda_j.
\]

Linearity of the weighted generalized number in the positive current and the same two-plane convex combination realize every number between the smallest and largest products. Corollary 6.47.2 supplies the universal upper/lower bounds, so no values outside the interval occur. \(\square\)

**Proposed action:** optional one-paragraph remark strengthening the sharpness sentence of Corollary 6.47.2 and Proposition 6.47.1. No change to existing theorem statements, tags or attributions. **Affected dependents:** comparisons of ordinary and directional Lelong numbers under finite monomial mappings; one cannot impose stronger pointwise ratio restrictions without further geometric hypotheses on the current.

## Selected proof checks and unresolved boundaries

1. **§6.41.1–2:** the real Hodge-type local current decomposition \(A=U+dV\) uses locally integrable kernels; the stated almost-everywhere restriction relies on a countable family of fiber tests and an \(L^1\) subsequence. The proof does **not** claim full-sequence almost-everywhere convergence. This has been checked as a specific dependency, not a universal slicing theorem.
2. **§6.41.4–5:** the unitary/dilation invariant form classification, the punctured incidence-fiber integration, zero extension across the zero section and the optional \(\nu(T,0)[E]\) term for \(q=c\) have been read and their dimensional roles checked. Full Skoda–El Mir and dimension-principle prerequisites are left conditional.
3. **§6.41.7, 6.41.9:** the identity \(\alpha^{p-d}\wedge\beta^d=d(\rho^d d^c\log\rho\wedge\alpha^{p-1})\) and endpoint \(d>0\) remove the inner boundary term, while \(d=0\) requires the explicitly added zero-section term. Equation 6.41.10 is used exactly as printed.
4. **§§6.43, 6.46–6.47:** generic sheet multiplicities, the proper-image zero coefficient condition, the finite-map exponent \(\sigma\) and upper/lower bounds have been read in the *integrated edition*, not just matched by old source numbering. Their complete analytic proof chain, including generalized weight comparison and classical unbounded Bedford–Taylor product existence, has not been independently certified.
5. **No new confirmed error or proof gap** was established in this bounded selection of claims. Prior 22 October normal-fiber atom jump `POME-FIBER-ATOM-JUMP-001` and all earlier findings are historical and **are not** re-entered as novel results. Demailly's dedicated approximation/regularization programme remains **deferred-by-user**, not repaired, not certified.

This is evidence of **selected passages only**. The chapter coverage inventory counts 747 current sections but does not certify them.
