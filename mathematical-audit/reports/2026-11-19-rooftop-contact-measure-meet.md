# A non-overcounting contact-set measure bound for finite rooftops

**Date:** 2026-11-19  
**Finding:** POME-ROOFTOP-CONTACT-MEASURE-MEET-001  
**Classification:** low / **verified conditional deduction** (not a false printed theorem; no upstream-chain certification)  
**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`

## Exact integrated anchors and scope

- \`docs/sections/envelopes-and-model-potentials--measures-on-contact-sets/index.html\`, blob \`c3be9349468d2203c0b67f4bee2be49d1392f8ff\`, mathematical lines **7–47**. Lemma **16.12.1**, source \`foundations-of-pluripotential-theory:94C0023B\`, permanent tag **EC77D6F30D3D**, lines 23–47.
- \`docs/sections/envelopes-and-model-potentials--measures-on-contact-sets--concentration-on-the-contact-set/index.html\`, blob \`840ebcb98be09245369315fa0c0288b936040098\`, mathematical lines **7–165**. Lemma **16.13.1**, source \`foundations-of-pluripotential-theory:86AF9332\`, tag **15A418789279**, lines 11–27; Theorem **16.13.4**, source \`foundations-of-pluripotential-theory:DDE3B556\`, tag **38E18A798D6B**, lines 70–146; Corollary **16.13.5**, source \`foundations-of-pluripotential-theory:FE439A00\`, tag **7FE9391D7A51**, lines 154–165.

The two **entire current sections** were read directly; earlier historical access has not been fully reconciled. This review does not assert independent verification of every transitive prerequisite.

## Printed results inspected

Lemma 16.12.1 passes from nonnegative continuous test inequalities to inequalities between finite measures using compact inner regularity; the cutoff \(\max(0,1-kd(\cdot,K))\) decreases to \(\mathbf1_K\) for compact \(K\Subset W\). Lemma 16.13.1 uses \(\max(u,v-\varepsilon)\), plurifine locality on \(\{u>v-\varepsilon\}\), and the weak limit \(\mu_{\max(u,v-\varepsilon)}\to\mu_v\) to establish
\[
\mathbf1_{\{u=v\}}\mu_u\le\mathbf1_{\{u=v\}}\mu_v,\qquad u\le v.
\]
The analytic-pole-set reduction in Lemma 16.13.2, bounded l.s.c. obstacle replacement in Lemma 16.13.3, and the two stages of Theorem 16.13.4 were examined directly. In Theorem 16.13.4, the decreasing-capacity exceptional sets, l.s.c. majorants, local weighted bounded-product convergence, and later truncations \(v_j^M=\max(u_j,V_\theta-M)\) are **distinct** limiting operations; the proof does not justify an arbitrary interchange of them. The contact support \(\mu_w(X\setminus\{w=f\})=0\) is used as printed, *conditionally on the explicitly cited upstream results*.

The printed Corollary 16.13.5 gives, for two inputs, an upper bound that counts the overlap of contact sets twice. This is valid; it is not optimal on that overlap. Neither the theorem nor its proof is refuted.

## New finite-family domination without overlapping mass

Assume \(X\) is a connected compact Kähler manifold, \(\{\theta\}\) is big, \(r\ge2\), and \(u_1,\ldots,u_r\in\mathrm{PSH}(X,\theta)\). Let
\[
w=P_\theta\!\left(\min_{1\le j\le r}u_j\right)\not\equiv-\infty,
\quad \nu_j=\mu_{u_j},\quad \nu=\mu_w,\quad
\Lambda=\sum_{j=1}^r\nu_j.
\]
Put \(C_j=\{w=u_j\}\), Borel contact sets, and, for every nonempty subset \(I\subset\{1,\ldots,r\}\), the **exact contact stratum**
\[
E_I=\bigcap_{i\in I} C_i\ \cap\!\bigcap_{j\notin I}(X\setminus C_j).
\]
The sets \(E_I\) are disjoint and cover \(\bigcup_jC_j\). Write \(f_j=d\nu_j/d\Lambda\); these densities exist since \(\nu_j\le\Lambda\). Then
\[
\boxed{\quad
\mu_w\ \le\
\sum_{\varnothing\ne I\subset\{1,\ldots,r\}}
\mathbf1_{E_I}\left(\min_{i\in I}f_i\right)\Lambda.
\quad} \tag{*}
\]
Here each summand denotes a measure. The right side is **independent of the chosen versions** of the Radon–Nikodym densities and is equivalently
\[
\sum_{\varnothing\ne I}\mathbf1_{E_I}\,
\bigwedge_{i\in I}\nu_i,
\]
where \(\bigwedge\) is the lattice infimum of finite positive measures, given by the minimum of their densities against a common dominating measure.

**Proof.** Theorem 16.13.4 implies \(\nu(X\setminus\bigcup_jC_j)=0\). Since \(w\le u_j\), Lemma 16.13.1 implies
\[
\mathbf1_{C_j}\nu\le\mathbf1_{C_j}\nu_j\quad(j=1,\dots,r).
\]
In particular, for every Borel \(A\), partition \(A\cap\bigcup_jC_j\) by the disjoint \(E_I\), and on each \(E_I\) choose any \(i\in I\). This gives \(\nu(A)\le\Lambda(A)\), so \(g=d\nu/d\Lambda\) exists. On each \(E_I\), for **every** \(i\in I\), domination gives \(g\le f_i\) \(\Lambda\)-a.e. Taking a minimum over the **finite** set \(I\) yields \(g\le\min_{i\in I}f_i\) \(\Lambda\)-a.e. on \(E_I\). Outside their union \(g=0\). Integrating proves (*). No compactness of families, limiting selection, or interchange of weak limits with indicator functions is used. \(\square\)

For \(r=2\), writing \(C_u=\{w=u\}\), \(C_v=\{w=v\}\), the exact improvement is
\[
\mu_w\le
\mathbf1_{C_u\setminus C_v}\mu_u+
\mathbf1_{C_v\setminus C_u}\mu_v+
\mathbf1_{C_u\cap C_v}(\mu_u\wedge\mu_v).
\]
It is stronger than the printed \(\mathbf1_{C_u}\mu_u+\mathbf1_{C_v}\mu_v\), because the measure meet is bounded by each operand. It also gives the corresponding total-mass bound by evaluating the right side on \(X\).

## Sharpness and limitations

For a **Kähler** form \(\theta\) and \(u_1=\cdots=u_r=0\), the rooftop is \(w=0\), every \(C_j=X\), and \(\nu_j=\nu=\theta^n\). Bound (*) is **equality** \(\theta^n\le\theta^n\), while the printed summed bound is \(\theta^n\le r\theta^n\). Thus the non-overcounting coefficient \(1\) cannot be decreased, and the old overlap multiplicity is genuinely avoidable. This toy case only demonstrates exactness of the improved estimate; it does not identify the actual rooftop measure for arbitrary other inputs.

The measure meet is the largest possible measure dominated simultaneously by all \(\nu_i\) on a fixed stratum in the **abstract measure-order constraints**. We do **not** claim that every such measure can arise as a Monge–Ampère measure of a rooftop or that this audit proves any absent up-stream analytic theorem.

## Dependencies, severity, proposed follow-up, and affected uses

- **Status:** verified conditional deduction, **severity low**; the printed Lemma 16.12.1, Lemma 16.13.1, Theorem 16.13.4, and Corollary 16.13.5 are **not** classified as false.
- **Local reasoning checked:** Radon inner regularity, contact comparison by \(\varepsilon\)-maxima, local homogeneous replacement, capacity-exceptional sets, weighted bounded-product limits, and finite-rooftop support.
- **Uncertified mathematical inputs:** non-pluripolar-product positivity/locality/continuity (Chapter 13 and §7.5); existence of Kähler currents with analytic singularities (Proposition 10.4.6, used in Lemma 16.13.2); local homogeneous replacement (Corollary 10.3.10); quasi-continuity and envelope monotone convergence (§16.11). Some analytic-singularity existence arguments may have regularization dependencies, which remain **deferred-by-user**, not resolved; **no excluded proof programme was inspected or reopened**.
- **Proposed correction:** no source correction required. Optionally append (*) as a separately reviewable strengthening after Corollary 16.13.5, retaining its original theorem, tags, attribution, and more general versions.
- **Affected dependents:** any downstream argument estimating a finite rooftop measure by summing contact-restricted Monge–Ampère measures, especially when contact sets overlap; no downstream proof is certified by this observation.

**Coverage delta:** +2 entire current reading-edition sections directly checked (§§16.12–16.13); +0 complete transitive dependency chains; first-ever visits not inferred. No tests, builds, CI, main/source/registry/tag/site modification or publication.
