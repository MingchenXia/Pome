# Directed increasing Bedford–Taylor limits via a Choquet lower sequence

**Finding ID:** POME-BT-DIRECTED-INCREASING-MIXED-NET-001  
**Date:** 2026-11-18  
**Severity / classification:** low / **verified conditional deduction**. No printed theorem is asserted false, and this is not a verification of the whole Bedford–Taylor theory.  
**Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\` (unchanged since October 23).  
**Branch:** \`review/mathematical-audit\`.  
**Scope:** newly audited directed-net extension of the *sequential* Theorems 7.6.1 and 7.5.8; the proof of the former and Choquet extraction in §5.10.2 were checked directly. No Demailly regularization, Bergman, L², Ohsawa–Takegoshi, multiscale, or positivity-loss steps were consulted.

## Exact integrated anchors and provenance

- \`docs/sections/bedford-taylor-products-and-local-capacity--increasing-limits-and-exceptional-envelopes/index.html\`, blob \`5e763bdc928794938c37dc3c7a51cc406472d076\`: Theorem **7.6.1**, source \`foundations-of-pluripotential-theory:36787F42\`, permanent \`A4C45B704647\`, physical lines **10–60** (statement 11–15; selected proof 20–60). It is explicitly **sequence**-indexed. Corollary **7.6.2**, source \`foundations-of-pluripotential-theory:2ACED3F4\`, permanent \`D865A8538D7D\`, lines **62–80**, uses a countable subfamily and capacity zero.
- \`docs/sections/plurisubharmonic-functions--limits-envelopes-and-local-integrability/index.html\`, blob \`9bd1ad642d1253391b0a925233014473503fd037\`: Theorem **5.10.2**, source \`foundations-of-pluripotential-theory:1E761457\`, permanent \`D32A2FB94F6B\`, lines **37–49**. It provides countable Choquet extraction on a second-countable complex manifold and equality of the raw envelope with its upper regularization almost everywhere.
- \`docs/sections/bedford-taylor-products-and-local-capacity--quasi-continuity-and-convergence-in-capacity/index.html\`, blob \`464778b7ca6f1a456e36b24ecb4a0c93ab6948d3\`: Lemma **7.5.7**, source \`foundations-of-pluripotential-theory:39398ED2\`, permanent \`880C30054932\`, physical lines **125–169**; Theorem **7.5.8**, source \`foundations-of-pluripotential-theory:2B1AA42A\`, permanent \`42828E3BDDFA\`, lines **172–190**. The theorem explicitly treats sequences with local capacity convergence and bounded quasi-continuous weights.

The published theorems are not changed. This result deliberately goes beyond the existing §7.6 coverage ledger, which recorded that the printed theorem had **not** been extended to arbitrary nets.

## Proposition (net-level mixed and weighted continuity)

Let \(D\subset\mathbb C^n\) be a domain, \(I\) a nonempty directed set, \(0\le q\le n\), and for each \(\ell=0,\ldots,q\) let \((u_{\ell,\alpha})_{\alpha\in I}\) be an **increasing** net (pointwise order) of locally bounded plurisubharmonic functions on \(D\). Suppose
\[
 u_\ell:=\left(\sup_{\alpha\in I}u_{\ell,\alpha}\right)^*
\]
is locally bounded and plurisubharmonic for every \(\ell\). Then on the **original net**, not merely along a selected subnet,
\[
 u_{\ell,\alpha}\longrightarrow u_\ell
 \quad\text{locally in Bedford--Taylor outer capacity},
\]
and
\[
 \bigwedge_{\ell=1}^{q}dd^c u_{\ell,\alpha}
 \ \rightharpoonup\
 \bigwedge_{\ell=1}^{q}dd^c u_\ell,\qquad
 u_{0,\alpha}\bigwedge_{\ell=1}^{q}dd^c u_{\ell,\alpha}
 \ \rightharpoonup\
 u_0\bigwedge_{\ell=1}^{q}dd^c u_\ell.
\]
For \(q=0\), the first current is the constant current \(1\), and the weighted assertion is ordinary \(L^1_{\mathrm{loc}}\) / distributional convergence.

More generally, if \(f_\alpha\) are real Borel functions **uniformly bounded on compact sets**, locally converging in capacity to a locally bounded **quasi-continuous** real Borel \(f\), then
\[
 f_\alpha \bigwedge_{\ell=1}^{q}dd^c u_{\ell,\alpha}
 \ \rightharpoonup\
 f \bigwedge_{\ell=1}^{q}dd^c u_\ell .
\]
No countable cofinal subset of \(I\) is assumed; one must not replace this assertion by an illicit net version of dominated convergence. If the \(u_{\ell,\alpha}\) increase only almost everywhere, uniqueness of psh representatives gives pointwise order, provided the monotonicity holds for every comparable pair.

### Proof, part 1: one common Choquet lower sequence

Every \(u_{\ell,\alpha}\le u_\ell\) pointwise, since it is dominated by the upper-semicontinuous regularization of the supremum. Theorem 5.10.2 yields, for each of the **finitely many** indices \(\ell\), a countable collection of original net indices \(J_\ell\subset I\) such that
\[
 \left(\sup_{\alpha\in J_\ell}u_{\ell,\alpha}\right)^*=u_\ell .
\]
Choose recursively \(\beta_k\in I\) such that \(\beta_k\ge\beta_{k-1}\) and \(\beta_k\) dominates the first \(k\) indices of every \(J_\ell\). Directedness permits each **finite** upper bound. The sequence \(u_{\ell,\beta_k}\) is increasing, bounded above by \(u_\ell\), and its supremum has upper regularization \(u_\ell\). By the almost-everywhere envelope statement of Theorem 5.10.2,
\[
 u_{\ell,\beta_k}\uparrow u_\ell \quad\text{almost everywhere on }D
\]
for every \(\ell=0,\ldots,q\), simultaneously.

Theorem 7.6.1 **now applies only to this genuinely sequential family** and proves \(u_{\ell,\beta_k}\to u_\ell\) locally in capacity. No new unproved net integration or compactness principle has been used.

### Proof, part 2: transfer from the selected sequence to the full directed net

Fix a compact \(K\Subset D\) and \(\delta>0\). For every \(\alpha\ge\beta_k\),
\[
 0\le u_\ell-u_{\ell,\alpha}\le u_\ell-u_{\ell,\beta_k}.
\]
Consequently
\[
 \operatorname{Cap}_D^*\!\left(K\cap
  \{|u_{\ell,\alpha}-u_\ell|>\delta\}\right)
 \le
 \operatorname{Cap}_D^*\!\left(K\cap
  \{u_\ell-u_{\ell,\beta_k}>\delta\}\right).
\]
The right side tends to zero as \(k\to\infty\); hence the original net converges locally in capacity. The exceptional failure of the raw supremum to equal \(u_\ell\) **pointwise** is not discarded: outer capacity, rather than literal pointwise convergence, is exactly the correct conclusion.

For any chosen \(\alpha_0\), on the cofinal tail \(\alpha\ge\alpha_0\) the inequalities
\(u_{\ell,\alpha_0}\le u_{\ell,\alpha}\le u_\ell\)
supply **uniform bounds on every compact**, because both endpoints are locally bounded. Thus no global uniform boundedness for the initial, discarded indices is being assumed.

### Proof, part 3: sequential contradiction forces weak convergence of the original net

Write \(S_\alpha=\bigwedge_{\ell=1}^qdd^cu_{\ell,\alpha}\) and \(S=\bigwedge_{\ell=1}^qdd^cu_\ell\). Suppose, for a test form \(\varphi\), that \(S_\alpha(\varphi)\not\to S(\varphi)\). There exist \(\varepsilon>0\) and **arbitrarily late** indices with absolute discrepancy at least \(\varepsilon\). Recursively choose an increasing sequence \(\alpha_k\) such that
\[
 \alpha_k\ge\alpha_{k-1},\quad \alpha_k\ge\beta_k,\quad
 |(S_{\alpha_k}-S)(\varphi)|\ge\varepsilon.
\]
Then \(u_{\ell,\beta_k}\le u_{\ell,\alpha_k}\le u_\ell\) and Theorem 7.6.1's capacity conclusion imply \(u_{\ell,\alpha_k}\to u_\ell\) locally in capacity. All selected potentials are uniformly locally bounded, by the cofinal-tail observation above. The **sequential** Theorem 7.5.8 therefore forces \(S_{\alpha_k}\rightharpoonup S\), contradicting the chosen fixed test. This proves unweighted convergence of the original net.

The same argument works for \(u_{0,\alpha}S_\alpha\): the same common \(\beta_k\) controls the weight \(u_{0,\alpha_k}\) in capacity, its limit \(u_0\) is quasi-continuous by Theorem 7.5.2, and Theorem 7.5.8 again contradicts any persistent discrepancy. Thus the weighted limit holds on the original net.

For the more general \(f_\alpha\), choose a compact exhaustion \(K_k\Subset D\), and by **the assumed net capacity convergence** choose \(\gamma_k\in I\) so that for every \(\alpha\ge\gamma_k\),
\[
 \operatorname{Cap}_D^*(K_k\cap\{|f_\alpha-f|>1/k\})<1/k.
\]
In the contradiction extraction require also \(\alpha_k\ge\gamma_k\). This guarantees that \(f_{\alpha_k}\to f\) locally in capacity **even though** an increasing chosen sequence of net indices need not be cofinal. Apply the weighted clause of Theorem 7.5.8 to the uniformly locally bounded factors and weights; contradiction. The stated general result follows.

### A directed index set with no countable cofinal sequence (scope check)

Let \(I\) be the finite subsets of an uncountable set \(A\), ordered by inclusion. No sequence can be cofinal: the union of countably many finite subsets misses some \(a\in A\). On the unit disc, the net
\[
 v_F(z)=\max\left\{\frac{\log|z|}{|F|+1},-1\right\}
\]
is increasing and locally bounded psh; its raw supremum is \(0\) for \(z\ne0\) and \(-1\) at \(0\), while its upper regularization is identically \(0\). Its one-dimensional \(dd^c\) measures converge weakly to zero on the **entire** directed set (the circular-shell masses are \(1/[2(|F|+1)]\) under \(dd^c=\frac{i}{2\pi}\partial\bar\partial\)). This reindexes the familiar logarithmic example solely to stress that **Choquet lower sequences are not cofinal sequences**; the elementary shell calculation is not counted as a separate mathematical finding.

## Diagnosis, dependencies, and proposed disposition

**Verified conditional deduction:** the sequential printed Theorem 7.6.1 is correct in the checked use, and the stated net extension follows from Theorems 5.10.2, 7.6.1 and 7.5.8. This is a *new scope extension*, not a counterexample, not a repair of a false theorem, and not a full certification of any upstream Bedford--Taylor continuity/capacity theorem. In particular, the deep step establishing Theorem 7.6.1's sequential weighted convergence and the foundational capacity/Choquet assertions are recorded as **internal conditional inputs**, not freshly certified in full.

**Suggested optional addition:** place a separate corollary immediately after Theorem 7.6.1, stating the directed-net version with the precise upper-regularized envelope hypothesis and its (possibly exceptional) raw supremum; cite the Choquet selection plus Theorems 7.6.1 and 7.5.8. Do not silently change the original theorem's sequence quantifier or its source/permanent tag. The arbitrary-capacity-convergent bounded Borel-weight extension may be a second paragraph.

**Potential users:** monotone Bedford--Taylor constructions, exceptional psh envelopes in §7.6.2, and later envelope/Monge--Ampère arguments that genuinely require directed limiting families. No previously valid conclusion or cited dependency was refuted. Do **not** substitute this for non-pluripolar convergence under unbounded potentials without additional hypotheses.

**Coverage delta:** direct selected review in §§7.6, 7.5, 5.10; all three were previously partially visited, so **0 newly first-visited numbered sections, 0 whole-section certificates**. Current main ToC still has 25 chapters and 747 sections. No tests, build, CI, production-body, tag, registry, main-branch, or website changes. Every named user-excluded regularization/Bergman/L²/OT/multiscale/positivity-loss programme remains **deferred-by-user**, neither resolved nor audited.
