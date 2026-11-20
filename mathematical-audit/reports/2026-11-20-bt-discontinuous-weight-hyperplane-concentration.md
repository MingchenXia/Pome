# Audit: a non-quasi-continuous fixed Borel weight defeats weighted Bedford–Taylor stability

**Date:** 2026-11-20 (Asia/Shanghai). **Baseline main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
**Classification:** \`POME-BT-NONQC-FIXED-WEIGHT-CONCENTRATION-001\` — **low / verified conditional deduction** (a precise counterexample to a *stronger unprinted assertion*, not a false theorem or a proof gap in Pome).
**Scope:** Complete direct mathematical reading of §7.5, and cross-chapter complete direct readings of §§20.5–20.7. The latter two sections already had historical full-review reports; they are not counted as first or newly full reviews. No upstream transitive proof chain is certified.

## Exact integrated-text anchors

| Section | Current main integrated file under \`docs/sections/\` | Blob SHA | Direct mathematical lines and source/permanent labels |
| --- | --- | --- | --- |
| §7.5 | \`bedford-taylor-products-and-local-capacity--quasi-continuity-and-convergence-in-capacity/index.html\` | \`464778b7ca6f1a456e36b24ecb4a0c93ab6948d3\` | 6–190; Theorem 7.5.2 \`foundations-of-pluripotential-theory:CAA09EE2 / C39FEC1AB985\`, Lemma 7.5.7 \`:39398ED2 / 880C30054932\`, Theorem 7.5.8 \`:2B1AA42A / 42828E3BDDFA\` |
| §20.5 | \`divisors-and-logarithmic-limits-on-analytic-cycles/index.html\` | \`dae567406b2030e550664ca57b1fe77911d956d4\` | 6–157; Lemma 20.5.3 \`demailly-complex-geometry:FF68839A / 323D5DA3E240\`, Theorems 20.5.5 and 20.5.10 \`:D58680EB / F1C928146DBC\`, \`:34D8935D / DDB973C0C1DD\` |
| §20.6 | \`analytic-cycles-and-cartier-cycles/index.html\` | \`d4817ac64b1365bd967d42cd474fec169f992e28\` | 7–76; Propositions 20.6.3 and 20.6.4 \`demailly-complex-geometry:02B65FA7 / FD8966432506\`, \`:BD1D45B4 / AA96C35C8290\`; Example 20.6.5 \`:E054C396 / 0C462992AB3A\` |
| §20.7 | \`meromorphic-sections-and-divisor-classes/index.html\` | \`d0c40d1e3f6f515eb13169ed1cd3fb447ca161c8\` | 7–30; Proposition 20.7.3 \`demailly-complex-geometry:00A05C89 / ACC6D09EDDD9\` |

The chapter/section paths and their current placement were checked against the actual Chapter 7 and Chapter 20 published tables of contents, not against source-book numbering.

## Finding POME-BT-NONQC-FIXED-WEIGHT-CONCENTRATION-001

**Precise claim tested.** The quasi-continuity assumption on the *limiting weight* in Lemma 7.5.7(2) and Theorem 7.5.8 cannot be deleted, **even when the weight is independent of the approximation index, and the potentials converge locally uniformly**. The published statements retain this hypothesis and are not contradicted.

**Explicit construction and full computation.** Work on the unit disc \(B\subset\mathbb C\), write \(z=x+iy\), and put, for \(\varepsilon>0\),
\[
 u_\varepsilon(z)=\tfrac12\bigl(x+\sqrt{x^2+\varepsilon^2}\bigr),\quad
 u(z)=\max(x,0),\quad
 f_\varepsilon(z)=f(z)=\mathbf1_{\{x=0\}}.
\]
All \(u_\varepsilon\) are smooth subharmonic and locally uniformly bounded, as is \(u\). Moreover
\[
 0\le u_\varepsilon-u
 =\tfrac12(\sqrt{x^2+\varepsilon^2}-|x|)\le\varepsilon/2,
 \qquad
 \partial_x^2u_\varepsilon=\frac{\varepsilon^2}{2(x^2+\varepsilon^2)^{3/2}}\ge0.
\]
Consequently the convergence is uniform (and hence locally in Monge–Ampère capacity by definition, for every directed \(\varepsilon\downarrow0\)). Under Pome's exact convention \(dd^c=\frac{i}{2\pi}\partial\bar\partial\), and with \(dx\,dy\) denoting the Euclidean volume element,
\[
 dd^cu_\varepsilon
   =\frac{\varepsilon^2}{8\pi(x^2+\varepsilon^2)^{3/2}}\,dx\,dy,\qquad
 dd^cu=\frac{1}{4\pi}\,\delta_{\{x=0\}}(dx)\otimes dy .
\]
The first measure is absolutely continuous, the second is a nonzero positive measure supported on the real diameter. The weak convergence follows directly by substituting \(x=\varepsilon t\) and dominated convergence, or by distributional continuity of \(dd^c\) under uniform convergence:
\[
 dd^cu_\varepsilon\rightharpoonup dd^cu.
\]
But \(f_\varepsilon=f\) is a bounded real Borel function with **trivial** capacity convergence \(f_\varepsilon\to f\). Since the support line has planar Lebesgue measure zero,
\[
 \boxed{ f_\varepsilon\,dd^cu_\varepsilon=0
 \text{ for every }\varepsilon>0,\qquad
 f\,dd^cu=dd^cu\ne0. }
\]
This is a failure of the *fixed-weight* conclusion if quasi-continuity of the limit weight is omitted; there is no issue about varying-base currents or a singular divisor.

**Verification that the missing hypothesis really fails.** The weight \(f=\mathbf1_{\{x=0\}}\) is not quasi-continuous for the Bedford–Taylor capacity. This can also be proved without assuming the weighted-continuity part (2) of Lemma 7.5.7. Indeed, fix a nonnegative \(\chi\in C_c(B)\) with \(\int\chi\,dd^cu>0\) and a compact \(K\Subset B\) whose interior contains its support. If \(f\) were quasi-continuous, for every \(\eta>0\) there would be open \(G\subset B\) with \(\operatorname{Cap}_B(G)<\eta\) such that \(f|_{K\setminus G}\) is continuous. Lemma 7.5.3 provides a continuous extension \(g:B\to[0,1]\) agreeing with \(f\) on \(K\setminus G\). The **independent capacity domination** in Lemma 7.5.7(1), applied to the uniformly bounded family \(\{u,u_\varepsilon\}\), bounds both \((dd^cu_\varepsilon)(G\cap K)\) and \((dd^cu)(G\cap K)\) by \(C_K\eta\). As \(f\,dd^cu_\varepsilon=0\),
\[
 \left|\int\chi g\,dd^cu_\varepsilon\right|
 \le \|\chi\|_\infty C_K\eta .
\]
Passing to the weak limit for the continuous function \(\chi g\), and then using \(g=f\) off \(G\) on \(K\), yields
\[
 0<\int\chi\,dd^cu=\int\chi f\,dd^cu
   \le 2\|\chi\|_\infty C_K\eta .
\]
Letting \(\eta\downarrow0\) is impossible. Thus non-quasi-continuity is established from capacity domination and ordinary weak convergence, not by circularly invoking the weighted theorem.

**Severity and status.** Low / verified conditional deduction. The printed Lemma 7.5.7(2) and Theorem 7.5.8 are correct in this respect; this is a documented boundary of a *hypothetical* weakening.

**Proposed action and dependents.** Keep “locally bounded and quasi-continuous” in the hypotheses of Lemma 7.5.7(2) and Theorem 7.5.8 and in every downstream application that tests a varying Bedford–Taylor product against Borel weights. If explanatory text is desired, use this example as a warning. No source or reading-edition patch is proposed in this audit branch. This example does not overturn the stronger *positive* result for varying bounded quasi-continuous weights in the earlier 2026-11-16/18 ledger entries.

## Further independent direct review: §7.5 and §§20.5–20.7

- **§7.5:** Verified the two-stage local capacity regularization argument and the exhaustion in Theorem 7.5.2; the compact-extension proof; the outer-capacity localization of Lemma 7.5.4; the distinction between local capacity and global \(\operatorname{Cap}_D\); the compact-local \(L^1\) estimate for nets; the multinomial coefficient \(n^{-n}n!(n-q)^{n-q}/(n-q)!\) in the mixed measure domination; and the weighted convergence induction. No false printed theorem was established. The local capacity comparison and Hartogs compactness inputs were inspected as *cited dependencies*, not fully re-proved here.
- **§20.5:** Checked the proper pushforward sheet-count lemma, the codimension-zero exclusion, \(\log|f_j|^2\) convergence using resolution and compact mass bounds, the zero-cycle case, and the proper-intersection induction yielding positive integer multiplicities. The normalization \(dd^c\log|f|^2=[\mathrm{Div}(f)]\) is consistent. Remmert and resolution remain explicitly documented upstream inputs; Hironaka resolution is permitted. §7.28 and §7.31 are unverified transitive symmetry prerequisites.
- **§20.6:** Checked the gluing/stalk description of cycle sheaves, generic Weil orders with singular locus of codimension at least two, and the weight contradiction on the rank-one quadric. The *already recorded* 2026-11-18 non-\(\mathbb Q\)-Cartier strengthening \`POME-CARTIER-QUADRIC-NON-Q-CARTIER-001\` was not counted again.
- **§20.7:** Checked the sign in \(dd^c\log|s|_h^2=[\mathrm{div}s]-c_1(L,h)\), the frame convention for \(\mathcal O(D)\), the inverse ratio in coefficient versus frame transitions, and the divisor connecting map. No change to these printed claims is proposed.

No mathematical duplication, incompatibility of permanent tags, or other confirmed error was established in these four direct readings. **Do not confuse this with complete certification of all upstream references.**

## Accounting and explicit exclusions

At this main SHA, the chapter inventory remains **25 chapters / 747 numbered sections**. This run directly read **four entire sections**, of which **§§7.5 and 20.5 are new whole-section upgrades** from earlier partial/legacy records and **§§20.6–20.7 are complete re-reads of HISTORIC-FULL-REPORTED sections**. Thus **+2 newly full direct-review statuses**, **2 repeated whole-section checks**, **+0 fully certified transitive proof chains**, and **no historical first-visit claim**. Preserve all older partial findings and historical coverage.

The user's excluded Demailly approximation/regularization and dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale atlas, and positivity-loss proof-completion programme remains **deferred-by-user**, **not resolved, repaired, or mathematically certified**. References outside this programme were considered only for the statements actually audited.

Only Markdown audit notes and accounting files belong in this branch. No build, CI, tests, main/source edits, registry/canonicalization changes, permanent-tag edits, or website publication were performed.
