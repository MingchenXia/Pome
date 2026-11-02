# Zero-volume boundary of the Okounkov-body map and local \(L^p\) failure for separate-subharmonic peaks — 2026-11-02

## Exact source and scope

**Production main inspected:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **review branch at entry:** `bb71f372d7b72f60f12b3fd67f2f56d6e58459cd`. Both results below are **low / verified conditional deductions**, not errors in the printed statements, not claims of entire-section certification, and not replacements of the source. This pass is independent of Demailly approximation/regularization and of the expressly excluded Bergman, weighted-\(L^2\), Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss programmes.

- **Okounkov topology:** `docs/sections/the-theory-of-okounkov-bodies--almost-semigroups/index.html`, main blob `33212916f9ea7754f51f8194cfb76c2fcbe8efab`. The pointed cone, finite degree slices and pseudometric are on physical lines **10–29**, Equation **19.2.1**, original `sgpt:2379D50B`, permanent `A3A5C96E566B`. Continuous volume is at lines **32–45**, Equation **19.2.2**, original `sgpt:9374A1CC`, permanent `41423E2E726F`. Full-lattice semigroups are Definition **19.2.3**, original `sgpt:C5989909`, permanent `923345ACA44A`, lines **89–90**. Almost semigroups require **positive volume** in Definition **19.2.9**, original `sgpt:E4CCE4D8`, permanent `78B565EC56CF`, lines **68–70**. The continuous Okounkov-body extension is Theorem **19.2.10**, original `sgpt:870F54F8`, permanent `2534E787147E`, and Equation **19.2.11**, original `sgpt:513C2C27`, permanent `64FC27991307`, lines **73–84**. The full-lattice volume formula is Equation **19.2.6**, permanent `4E701FB8EA13`, lines **106–111**.
- **Separate-subharmonic example:** `docs/sections/polynomial-approximation-and-a-separate-subharmonic-example/index.html`, main blob `a4a17c61ef30efb6fc6e20f105baeca052bbed43`. Polynomial approximation is Proposition **3.7.1**, original `klimek-pluripotential-theory:01560C0B`, permanent `6D285B395FD0`, lines **7–16**. Its following **unnumbered** example is physical lines **21–36** under the section's permanent tag `7AF53FD9F731`; do **not** invent a separate permanent tag for this paragraph. Compare Theorem **3.6.1**, original `klimek-pluripotential-theory:F1182878`, permanent `58AAF98CC15E`, at `docs/sections/separate-harmonicity-and-subharmonicity/index.html`, main blob `1d3c9ebe0d7093f0f069dc2b25b0a47f700f907a`, lines **7–33**.

## POME-OKO-ZEROVOL-HAUSDORFF-BOUNDARY-001

**Severity low; status verified conditional deduction.** The **positive-volume** restriction in the printed Theorem 19.2.10 is genuinely necessary for a well-defined Hausdorff-continuous extension to the pseudometric completion boundary. Moreover, the Okounkov-body map, while continuous on the printed positive-volume domain, is **not uniformly continuous** there with respect to \(d_{\rm sg}\) and Hausdorff distance.

Here is an exact full-lattice countermodel requiring no semigroup asymptotic theorem. Work with \(n=1\) and the admissible fixed cone
\[
C=\{(x,k)\in\mathbb R^2: k\geq0,\ 0\leq x\leq k\}.
\]
For each integer \(N\geq3\), define **saturated semigroups**
\[
S_N^{L}=\{(x,k)\in C\cap\mathbb Z^2:0\leq x\leq k/N\},\qquad
S_N^{R}=\{(x,k)\in C\cap\mathbb Z^2:(1-1/N)k\leq x\leq k\}.
\]
They are additively closed, include \(0\), and generate the **whole** \(\mathbb Z^2\): \(S_N^{L}\) contains \((0,1),(1,N)\), a unimodular pair, while \(S_N^{R}\) contains \((1,1),(N-1,N)\), also a unimodular pair. Thus **both lie in the original \(\mathcal S'(C)\)**, not merely in a relaxed finite-index class.

For every positive integer \(k\), both degree slices have exactly \(\lfloor k/N\rfloor+1\) elements. Consequently, directly from the printed Equation 19.2.1 and the degree-slice definition,
\[
\operatorname{vol}S_N^L=\operatorname{vol}S_N^R=\frac1N,\qquad
\Delta(S_N^L)=[0,1/N],\quad\Delta(S_N^R)=[1-1/N,1].
\]
For \(N\geq3\), the two positive-degree slices are disjoint. Hence
\[
d_{\rm sg}(S_N^L,S_N^R)
=\lim_{k\to\infty}\frac{2(\lfloor k/N\rfloor+1)}k
=\frac2N\longrightarrow0,
\qquad
d_{\rm H}(\Delta(S_N^L),\Delta(S_N^R))
=1-\frac1N\longrightarrow1.
\]
The Hausdorff distance formula follows by comparing the two interval endpoints; it does not rely on a continuity theorem. This proves the failure of **global uniform** continuity. It does **not** contradict the existing continuity assertion at each positive-volume almost semigroup.

Let \(S_0=\{(0,0)\}\in\mathcal S(C)\). Since it has no positive-degree slices,
\[
d_{\rm sg}(S_N^L,S_0)=d_{\rm sg}(S_N^R,S_0)=1/N\to0.
\]
Thus both full-lattice families converge in \(d_{\rm sg}\) to the **same** zero-volume element, whereas their bodies converge in Hausdorff distance to the **different** singleton sets \(\{0\}\) and \(\{1\}\). Even enlarging the codomain to *all* nonempty compact convex subsets of \([0,1]\) cannot yield a unique continuous extension of \(\Delta\) across this point. If \(\mathcal K_1\) is restricted to positive-length convex bodies, the singleton limits are also outside its codomain.

Finally, \((S_N^L)\) is \(d_{\rm sg}\)-Cauchy by the triangle inequality through \(S_0\). It cannot have a limit within the positive-volume almost-semigroup domain: the volume function is \(1\)-Lipschitz (Equation 19.2.2) and its volumes \(1/N\to0\). This gives an **explicit incompleteness witness** for that positive-volume metric quotient.

**Scope/proposed note:** append a short zero-volume-boundary remark after Theorem 19.2.10 or Equation 19.2.11, explicitly distinguishing continuity on the positive-volume locus from uniform continuity and extension at volume zero. Preserve Theorem 19.2.10 and all existing definitions unchanged. **Affected dependents:** any attempted use of global Hausdorff-uniform control for nearly vanishing semigroups, completion of the positive-volume quotient, or extrapolation of Theorem 19.7.32 to zero volume. This finding is separate from the earlier `POME-OKO-SYMDIFF-ISOMETRY-001`, which concerns symmetric-difference measure and is not re-registered here.

## POME-SEPARATE-PEAK-LOCAL-LP-DIVERGENCE-001

**Severity low; status verified conditional deduction.** The **specific printed** finite nonnegative separately subharmonic \(F\) in §3.7 is jointly **lower semicontinuous and Borel**, but is **not locally \(L^p\)** for **any \(p\geq1\)** near \((0,0)\). This is a direct, quantitative proof of the failure of the locally integrable-majorant hypothesis in Theorem 3.6.1, rather than inferring it only by contradiction from that theorem. The existing example and theorem remain correct.

Use the printed data \(a_j=j^{-1}e^{i/(j+1)}\), \(b_j=\max(|P_j|-1,0)\), \(F(z,w)=\sum_jb_j(z)b_j(w)\). From \(P_j(a_j)=j+1\) we have \(b_j(a_j)=j\); each \(b_j\) is continuous nonnegative subharmonic, and for each **fixed** point only finitely many \(b_j\) are nonzero. Each finite partial sum of \(F\) is continuous and nonnegative, so its increasing supremum \(F\) is lower semicontinuous/Borel (although the printed diagonal peak already shows it is not jointly upper semicontinuous).

Fix an arbitrary \(\rho>0\). For all sufficiently large \(j\), \(|a_j|<\rho/2\), so \(D(a_j,\rho/2)\subset D(0,\rho)\). For every \(p\geq1\), \(b_j^p\) is subharmonic because \(t\mapsto t^p\) is convex and increasing on \([0,\infty)\). Its submean inequality gives
\[
\int_{D(0,\rho)}b_j(z)^p\,dA(z)
\ \geq\ \int_{D(a_j,\rho/2)}b_j^p\,dA
\ \geq\frac{\pi\rho^2}{4}\,b_j(a_j)^p
=\frac{\pi\rho^2}{4}j^p.
\]
For nonnegative \(t_j\) and \(p\geq1\), \((\sum_jt_j)^p\geq\sum_jt_j^p\) (first for finite sums and then by monotone convergence). Tonelli therefore applies *without presupposing joint integrability* and yields
\[
\begin{aligned}
\int_{D(0,\rho)^2}F^p\,dA(z)dA(w)
&\geq \sum_{j\geq J}
 \left(\int_{D(0,\rho)}b_j^p\,dA\right)^2\\
&\geq\left(\frac{\pi\rho^2}{4}\right)^2\sum_{j\geq J}j^{2p}
=+\infty.
\end{aligned}
\]
Every neighborhood of \((0,0)\) contains such a bidisk. In particular \(F\) itself is not locally integrable there, and no locally integrable *pointwise* majorant can exist. This proof only uses the printed peak interpolation and elementary submean/Tonelli, **not** the separate-subharmonic-to-joint theorem it illustrates.

**Scope/proposed note:** optionally add the explicit \(L^p\)-divergence observation to the §3.7 example; preserve its original version and its source attribution. **Affected dependents:** use of separate subharmonicity with presumed joint measurability or local integrability, and precise hypothesis transport into Theorem 3.6.1. The 2026-10-29 `POME-SEPARATE-SMOOTH-SUBHARM-PEAK-001` concerned smooth individual slices and a contradiction-based majorant observation; this independent direct integral lower bound for the **printed** example is not a new registration of that finding.

## Coverage, prior statuses, and verification boundary

**Actual new checks:** direct degree-slice counting, full-lattice-group determinants, \(d_{\rm sg}\)/Hausdorff topology and zero-volume boundary in **§19.2.1/.3/.9–10**; direct subharmonic-power, Tonelli and Borel regularity checks of the **unnumbered §3.7 peak example**, with a narrowly scoped comparison to **§3.6.1**. Both §19.2 and §3.7 were **previously partially reviewed**, so this adds **no first-reviewed mathematical section and no complete-section mathematical certification**. The existing current-ToC baseline is **25 chapters, 747 numbered sections, zero fully certified sections**; this run did not rederive the global count from scratch. Earlier confirmed errors, proof gaps, genuine external dependencies, earlier related findings, and user-deferred material retain their statuses.

No claim of a project build, test suite, formal proof, GitHub Actions, site publication, main-branch/source edit, canonicalization/tag change, or complete dependency-chain verification is made.