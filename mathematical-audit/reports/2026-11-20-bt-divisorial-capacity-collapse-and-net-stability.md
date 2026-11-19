# 2026-11-20: Bedford–Taylor net stability and divisorial capacity collapse

## Source, coverage, and classification

Production main SHA: **b6933b772f41b45918f7e25ed1afbbb1fd892272**. The integration rules in AGENTS.md and proof-expansions.md and both audit LATEST.md and README.md were freshly read. No source-body or permanent-tag changes are proposed here.

- **Complete §7.2 direct reading:** docs/sections/bedford-taylor-products-and-local-capacity--bounded-potentials-and-recursive-products/index.html, blob **18bd2395f3b76941b2c677079c09eb6accc5a9cb**, mathematical lines **5–159**. Reading-edition source \`foundations-of-pluripotential-theory\`. Definition 7.2.1 source/permanent **DE7531DE/254CDCCCAB5E**, lines 16–27; Proposition 7.2.2 **D16BD033/D9911E035563**, lines 29–83; CLN Theorem 7.2.5 **103AB333/2A84C325AB58**, lines 98–122; Proposition 7.2.6 **C5608495/2F39A3F97E8E**, lines 125–157; determinant formula permanent **706A589A680C**, lines 84–95.
- **Complete §7.33 direct reading:** docs/sections/separated-maximum-monge-ampere-products/index.html, blob **a859ac5637379266fa191831656f214c51676ca1**, mathematical lines **5–81**. Source \`isolated-plurisubharmonic-singularities\`. Lemma 7.33.1 **C4DA57C3/11B8D65C2D19**, lines 10–36; Theorem 7.33.3 **DE8582D3/F8604F30C7C6**, lines 39–81.
- **Selected §7.4 dependency only:** docs/sections/bedford-taylor-products-and-local-capacity--weighted-estimates-and-monge-ampere-capacity/index.html, blob **801a6ce8d25a6db19202cbc295937a135a9a208e**, Proposition 7.4.4 permanent **815E5BBFC34A**, lines **144–165**. Not a complete §7.4 audit.
- Two new findings below; **neither is an original printed theorem error**. The listed upstream §§5.3, 5.9, 7.3, and 7.4 have not been certified as full dependency chains.

## POME-BT-JOINT-NET-STABILITY-001

**low / verified conditional deduction.** Proposition 7.2.6 remains true after replacing its sequence index with an **arbitrary directed set**, provided its original topologies and continuity assumptions remain unchanged.

Precisely, on \(\Omega\subset\mathbb C^n\), suppose \(T_\alpha\rightharpoonup T\) is a net of positive closed currents of fixed bidimension \((r,r)\), \(u_{j,\alpha}\in\operatorname{PSH}(\Omega)\cap L^\infty_{\rm loc}\) converge locally uniformly to continuous \(u_j\) for \(j=1,\ldots,q\), and locally bounded Borel \(w_\alpha\) converge locally uniformly to continuous \(w\), with \(0\le q\le r\). Then the \(q\)-fold recursive products converge weakly, as do their products with \(w_\alpha\). The \(q=0\) statement includes weighted weak convergence of \(w_\alpha T_\alpha\). The continuous \(u_j\) are psh by passing each complex-disc submean inequality through local uniform convergence, without extracting a sequence.

**Proof of the net multiplier lemma.** Let \(S_\alpha\rightharpoonup S\) be positive currents and \(v_\alpha\to v\) locally uniformly with \(v\) continuous. On any compact \(K\) eventual trace-mass bounds for \(S_\alpha\) follow by evaluating the net on a smooth cutoff equal to one near \(K\); weak convergence makes those scalar pairings eventually bounded. The coefficient total variations are dominated by the trace measures. For a test form \(\phi\) on \(K\), choose a smooth \(v_\varepsilon\) uniformly within \(\varepsilon\) of \(v\) on \(K\) and write
\[
 v_\alpha S_\alpha-vS=(v_\alpha-v)S_\alpha
 +(v-v_\varepsilon)S_\alpha
 +v_\varepsilon(S_\alpha-S)+(v_\varepsilon-v)S.
\]
The first term tends to zero by the local uniform bound, the second/fourth are \(O(\varepsilon)\) *eventually*, and the third tends to zero by weak convergence. Directedness supplies one final index for the finite list of inequalities. Let \(\varepsilon\downarrow0\), proving \(v_\alpha S_\alpha\rightharpoonup vS\) on the original net. Induct on the \(q\) factors using §7.2.2 positivity/closedness, apply this multiplier lemma with \(u_{1,\alpha}\), then apply the weakly continuous operator \(dd^c\). Finally apply the multiplier lemma to \(w_\alpha\). This yields the asserted joint continuity for all nets, without an unjustified cofinal-sequence reduction.

**Proposed audit-only addition:** optional net corollary to §7.2.6. **Affected dependents:** applications with genuinely directed weak positive-current and locally uniform bounded-potential limits. It makes no claim for mere \(L^1\) or capacity convergence.

## POME-BT-DIVISOR-CAPACITY-COLLAPSE-001

**low / verified conditional deduction (explicit counterexample to an unprinted strengthening).** Replacing local uniform convergence in Proposition 7.2.6 by **local Bedford–Taylor capacity convergence**, while allowing a fixed arbitrary positive closed base current, is invalid even for uniformly bounded smooth psh functions.

Take the bidisc \(\Omega=\Delta_{1/2}^2\) with coordinates \((z,w)\), the divisor \(H=\{z=0\}\), and \(T=[H]\), a positive closed current of bidimension \((1,1)\). Define
\[
 u_k(z,w)=\frac1k\log\!\left(|z|^2+e^{-k}(1+|w|^2)^k\right),\quad k\ge1. \tag{1}
\]
By \((1+|w|^2)^k=\sum_{j=0}^k\binom kj|w|^{2j}\), the logarithm is the log squared norm of the nowhere-vanishing holomorphic vector with components \(z\) and \(e^{-k/2}\sqrt{\binom kj}\,w^j\). Hence **every \(u_k\) is smooth psh**. Further,
\[
 -1\le u_k(z,w)\le \frac{\log(5/4)}{k}\quad\text{on }\Omega. \tag{2}
\]
The lower bound follows from the \(e^{-k}\) term, and the upper from \(|z|^2<1/4\) and \(e^{-k}(1+|w|^2)^k\le (5/(4e))^k<1\). Away from \(H\), \(u_k\to0\) pointwise. Consequently (2) implies convergence in \(L^1_{\rm loc}\) and weak convergence \(dd^cu_k\rightharpoonup0\).

**A quantitative capacity estimate, without a hidden absolute-continuity assumption.** Let \(K\Subset\Omega\), \(K\subset\operatorname{Int}L\Subset\Omega\), and \(\delta>0\). For large \(k\), \(\sup u_k<\delta\). Since \(u_k\ge(2/k)\log|z|\) off \(H\),
\[
 K\cap\{|u_k|>\delta\}\subset
 K\cap\{\log|z|<-k\delta/2\}.
\]
The pole function \(V=\log|z|\) belongs to \(\operatorname{PSH}(\Omega)\cap L^1(L)\). Applying exactly Proposition 7.4.4 (tag **815E5BBFC34A**) yields
\[
 \operatorname{Cap}_\Omega^*\bigl(K\cap\{|u_k|>\delta\}\bigr)
 \le\frac{2C_{K,L}}{k\delta}\|\log|z|\|_{L^1(L)}
 =O_{K,L,\delta}(k^{-1})\longrightarrow0. \tag{3}
\]
Thus \(u_k\to0\) **locally in capacity**, with an explicit upper rate.

**Yet the divisor-supported products do not converge.** On \(H\), identically in \(k\),
\[
 u_k(0,w)=-1+\log(1+|w|^2).
\]
The smooth case of the recursive product (§7.2.2) therefore gives the exact nonzero current
\[
 \boxed{dd^cu_k\wedge[H]
 =[H]\wedge dd_w^c\log(1+|w|^2)
 =[H]\wedge\frac{i\,dw\wedge d\bar w}{2\pi(1+|w|^2)^2}\ne0}
 \quad\text{for every }k. \tag{4}
\]
By contrast \(dd^c0\wedge[H]=0\). In fact \(u_k[H]=[-1+\log(1+|w|^2)][H]\) already fails to converge to \(0[H]\) as a weighted current.

This does **not** refute §7.2.6, because (1) fails local uniform convergence along \(H\). It does **not** refute §7.5.7, whose capacity-dominated ambient Bedford–Taylor product measures are different from an inserted integration current \([H]\), which charges a pluripolar set of capacity zero. Source §7.4.4 itself gives this zero-capacity property. The gap is in an **unprinted extrapolation**, not in the printed theorems.

**Proposed audit-only warning:** capacity convergence cannot replace compact-open convergence for arbitrary divisor-supported base currents without separate uniform trace-measure control on small-capacity sets. **Potential dependents:** future uses of §§7.2.6, 7.5.7 or 13.4 with analytic-cycle current bases; no currently printed application is asserted false.

## Checks of remaining printed arguments

In the complete §7.2 text, checked the recursive one-factor positivity induction, current multiplication and biholomorphic pullback, the \(n!/\pi^n\) Monge–Ampère determinant factor under \(dd^c=i(2\pi)^{-1}\partial\bar\partial\), the nested-compact CLN cutoff with factorial conventions, and the source's sequential varying-base proof. No confirmed original error or independent proof gap identified.

In §7.33, directly checked that locality gives \((h-f)C^k=(h-f)B^k\) for bounded current coefficient measures, hence \(C^{k+1}=A C^k+C B^k-A B^k\). In total dimension \(p+q\), exactly two positive terms and one negative survive. Their support restrictions on \(\{f=0\}\) and \(\{g=0\}\) make each positive term equal \(A^pB^q\), so the final coefficient is **1**, not a binomial coefficient; the tensor identity is justified by separated smooth tests and bounded masses. The earlier §7.33 power-interface and multi-block results in the historical ledger are not new results of this run.

## Actual coverage and exclusions

**+2 complete direct sections (§§7.2 and 7.33); +1 selected §7.4 input; +0 full transitive upstream proof-chain certificates.** Do not infer historical first-ever review. All specified Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programmes remain **deferred-by-user**, neither resolved nor certified. No builds, tests, CI, source/main/registry/permanent-tag/site edits or publication.
