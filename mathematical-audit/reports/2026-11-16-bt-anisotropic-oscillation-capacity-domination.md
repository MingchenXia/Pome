# Independent oscillation and capacity domination for mixed Bedford–Taylor products

**Date:** 2026-11-16. **Stable ID:** \`POME-BT-INDEPENDENT-OSCILLATION-CAP-DOMINATION-001\`. **Severity:** low. **Status:** verified conditional deduction. **Not a confirmed error.** The printed Lemma 7.5.7 remains true; the strengthening below has not been inserted into the mathematical body.

## Immutable source and scope

- Main commit: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
- Integrated reading section: \`docs/sections/bedford-taylor-products-and-local-capacity--quasi-continuity-and-convergence-in-capacity/index.html\`, blob \`464778b7ca6f1a456e36b24ecb4a0c93ab6948d3\`. Lemma 7.5.7(1), physical lines **124–146**, source \`foundations-of-pluripotential-theory:39398ED2\`, permanent tag \`880C30054932\`; Lemma 7.5.7(2), lines **148–166**. For context, Theorem 7.5.8, lines **171–185**, source \`foundations-of-pluripotential-theory:2B1AA42A\`, permanent tag \`42828E3BDDFA\`. Theorem 7.5.8 is **not** asserted with weaker hypotheses here.
- Capacity comparison: \`docs/sections/bedford-taylor-products-and-local-capacity--weighted-estimates-and-monge-ampere-capacity/index.html\`, blob \`801a6ce8d25a6db19202cbc295937a135a9a208e\`, Proposition 7.4.3(4), physical lines **98–115**, source \`foundations-of-pluripotential-theory:DE1E4FA5\`, permanent tag \`97EFDB6FDEE3\`.
- Conditional internal inputs: positive mixed Bedford–Taylor products and symmetry (7.2.2/7.3.7), local comparison of Bedford–Taylor capacities (7.4.3(4)), coefficient variation bounded by positive-current trace (5.3.7), and elementary compact-set continuous extension (7.5.3). No external analytic theorem and no Demailly regularization programme are invoked.

## Precise improvement

Let \(B=B(a,R)\subset\mathbb C^n\), \(0\le q\le n\), \(K\Subset B'=B(a,R')\Subset B\). Write
\(\beta=(i/2)\sum_j dz_j\wedge d\bar z_j\), and use Pome's \(dd^c=(i/2\pi)\partial\bar\partial\).
For locally bounded \(u_i\in\operatorname{PSH}(B)\), set
\(M_i=\operatorname{osc}_{B'}u_i=\sup_{B'}u_i-\inf_{B'}u_i\), assumed finite.
For \(0\le q\le n\), define
\[
c_{n,q}=\frac{n!}{n^n(n-q)!}(n-q)^{n-q},\quad 0^0=1,\qquad
C_{K,B',B}=\sup_{\substack{E\subset K\\E\text{ Borel}\\\operatorname{Cap}_B(E)>0}}
\frac{\operatorname{Cap}_{B'}(E)}{\operatorname{Cap}_B(E)}<\infty.
\]
The latter constant is finite by printed Proposition 7.4.3(4), and can be replaced by any constant furnished by that proposition. Then, for every Borel \(E\subset K\),
\[
\boxed{\quad
\int_E dd^cu_1\wedge\cdots\wedge dd^cu_q\wedge\beta^{n-q}
\le C_{K,B',B}\,
\frac{(\pi R'^2)^{n-q}}{c_{n,q}}\,
\left(\prod_{i=1}^q M_i\right)\operatorname{Cap}_B(E).
\quad}
\tag{A}
\]
The empty product is 1. For \(q\ge1\), if any \(M_i=0\), the entire mixed current is zero on \(B'\), so (A) also holds. Formula (A) is *separately* homogeneous in the oscillation of each potential, and is invariant under independent additions \(u_i\mapsto u_i+C_i\). No optimality of its numerical coefficient is asserted.

### Full proof of (A)

Suppose first that every \(M_i>0\). Set
\[
v_i=\frac{u_i-\inf_{B'}u_i}{M_i},\qquad
\phi(z)=\frac{|z-a|^2}{R'^2},\qquad
F=\frac{v_1+\cdots+v_q+(n-q)\phi}{n}.
\]
Each \(v_i\) and \(\phi\) is psh and takes values in \([0,1]\) on \(B'\); hence \(F\) is a competitor for \(\operatorname{Cap}_{B'}\). Positivity and symmetry of mixed bounded Bedford–Taylor products permit expansion of \((dd^cF)^n\). Retaining just the nonnegative terms containing each \(dd^cv_i\) once and \(dd^c\phi\) precisely \(n-q\) times gives
\[
(dd^cF)^n\ge
\frac{n!}{(n-q)!}\,\frac{(n-q)^{n-q}}{n^n}\,
dd^cv_1\wedge\cdots\wedge dd^cv_q\wedge(dd^c\phi)^{n-q}.
\]
Indeed, there are \(n!/(n-q)!\) ordered assignments of the \(q\) separately labeled \(v_i\) to the \(n\) factors; the remaining factors contribute \((n-q)^{n-q}\). This formula remains valid for \(q=0\) and \(q=n\), interpreting \(0^0=1\). Since \(dd^c\phi=\beta/(\pi R'^2)\) and \(dd^cu_i=M_i\,dd^cv_i\) on \(B'\), integrate on \(E\) and use \(\int_E(dd^cF)^n\le\operatorname{Cap}_{B'}(E)\le C_{K,B',B}\operatorname{Cap}_B(E)\). If \(M_i=0\) the corresponding \(u_i\) is constant on the connected ball \(B'\), so its Bedford–Taylor derivative vanishes there. This proves (A), including the zero-oscillation and \(q=0\) cases.

## Net-weighted stability with only oscillation control

Let \(\Lambda\) be any directed set. Suppose that, for each \(i=1,\ldots,q\), \(u_{i,\lambda}\in\operatorname{PSH}(B)\cap L^\infty_{\mathrm{loc}}(B)\) and
\(\sup_{\lambda}\operatorname{osc}_{B'}u_{i,\lambda}<\infty\) for every relatively compact concentric ball \(B'\Subset B\). **Do not assume** the additive normalizations are uniformly bounded. Suppose *separately* that
\[
S_\lambda=dd^cu_{1,\lambda}\wedge\cdots\wedge dd^cu_{q,\lambda}
\rightharpoonup S
\]
as currents. Let \(f_\lambda\) be real Borel functions uniformly bounded on every compact subset of \(B\), converging there in \(\operatorname{Cap}_B\) to a locally bounded, quasi-continuous Borel \(f\). Then
\[
\boxed{ f_\lambda S_\lambda\rightharpoonup fS }
\tag{B}
\]
as currents, for the **entire original net**. This assertion does not claim that oscillation control alone implies convergence of \(S_\lambda\).

**Proof.** Fix the compact support of a test form in \(K\Subset B'\Subset B\). The bound (A) yields a uniform capacity bound on the trace measures of the \(S_\lambda\) over Borel subsets of \(K\). Positivity of each \(S_\lambda\) gives uniform bounds for the total variations of every coefficient measure by a dimensional multiple of the trace. The weak limit \(S\) is positive. For any relatively compact open \(G\) in the interior of a slightly larger \(K\), the lower-semicontinuity of positive-measure mass on open sets under vague convergence (also valid for nets) gives the same capacity domination for the trace of \(S\); coefficients of \(S\) are controlled by this trace. By taking open supersets, the bound extends to the outer capacity needed for exceptional Borel sets.

For a fixed \(f\), choose, by quasi-continuity, an open \(G\) of arbitrarily small capacity such that \(f\) is continuous on \(K\setminus G\). Extend its bounded restriction continuously to a neighborhood, using Lemma 7.5.3. Integrals of the extension converge by weak convergence of \(S_\lambda\); replacing it with \(f\) costs at most a constant times \(\operatorname{Cap}_B(G)\), uniformly in \(\lambda\) and for \(S\). Let that capacity tend to zero, obtaining \(fS_\lambda\rightharpoonup fS\).

Finally, for any \(\delta>0\), split the weighted error over
\(A_{\lambda,\delta}=K\cap\{|f_\lambda-f|>\delta\}\). The total variation estimate gives
\[
\left|\langle(f_\lambda-f)S_\lambda,\chi\rangle\right|
\le \|\chi\|_\infty\,C_K\bigl(\delta\,\operatorname{Cap}_B(K)
+2M_K\operatorname{Cap}_B^*(A_{\lambda,\delta})\bigr),
\]
with a constant \(C_K\) independent of \(\lambda\) and \(M_K\) a common bound for \(f_\lambda,f\) on \(K\). The second capacity tends to zero along the original net; then \(\delta\downarrow0\). The proof holds coefficientwise for each test form and establishes (B). It uses no sequential compactness or changed limit order.

### Strictly broader normalization class

Take fixed bounded smooth psh \(v_i\) on \(B\) and \(u_{i,k}=v_i+k\), \(k\ge1\). Their mixed currents and oscillations do not depend on \(k\), but the family violates the uniform absolute \(L^\infty_{\mathrm{loc}}\) bound in the printed Lemma 7.5.7. Formulae (A) and (B) still apply whenever weights satisfy the hypotheses. This distinguishes the improvement from the earlier bounded-family directed-net and integrated-capacity-tail findings; it does not refute or replace their conclusions.

## Audit status and dependents

- **Verified conditional deduction:** (A) from positivity/polarization and printed local capacity comparison, plus (B) from (A), positive-current coefficient control and quasi-continuity. The arithmetic identity for \(c_{n,q}\) and its reciprocal was checked for all \(1\le n\le7,\,0\le q\le n\) (35 pairs); the general proof above, not these finite checks, is the justification.
- **Not a proof-gap claim:** printed Lemma 7.5.7 and Theorem 7.5.8 are not false; original hypotheses still suffice. Stronger (B) explicitly retains an independent weak-convergence hypothesis. No assumption that capacity-convergent potentials generate convergent mixed currents without normalized bounds is made.
- **Proposed correction:** optionally add (A) as a normalization-invariant remark after 7.5.7(1) and (B) as a bounded-oscillation net corollary after 7.5.7(2), not a direct edit to the reading edition.
- **Affected dependents:** possible use in capacity-weighted Bedford–Taylor convergence (§7.5.8), local non-pluripolar truncations (§13.2) and the weighted non-pluripolar capacity limits (§13.7); those downstream deductions and their broader hypotheses have **not** been verified in this run.
- **Coverage:** only listed paragraphs of §7.5 and contextual §7.4.3(4); both previously sampled. Newly first-visited numbered sections **0**, entirely mathematically certified sections **0**. Current ToC **25 chapters / 747 numbered sections**. No project tests, build, CI, publication, source body, registry, canonicalization, or permanent-tag changes.
- **User exclusion:** all Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss completion remains **deferred-by-user**, not resolved or certified.
