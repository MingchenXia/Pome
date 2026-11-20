# Dense polar sets cannot in general be exact superharmonic pole sets

**Finding ID:** POME-CLASS-DENSE-POLAR-GDELTA-OBSTRUCTION-001  
**Date:** 2026-11-20  
**Severity / status:** low / **verified conditional deduction**, with an explicit counterexample to a *stronger, unprinted* exact-pole assertion. **No printed theorem is false on this evidence.**

## Primary integrated mathematical record

- Reviewed production **main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
- Reading-edition file: **docs/sections/polar-sets-capacity-and-sweeping/index.html**, Git blob aa814f26482e8ed27e51c945e9202c797449158b.
- Whole numbered section **§4.3**, permanent **AEB997E884B4**, mathematical physical lines **7–131** (headers, statements, examples and proof text; trailing navigation excluded).
- **Theorem 4.3.2**, source **classical-potential-theory:E7138943**, permanent **253540032CE5**, statement physical line **8**, proof **13–21**. In particular the general assertion is *containment* in a pole locus, while an **exact** pole locus is asserted separately for compact polar sets.
- **Theorem 4.3.4**, source **classical-potential-theory:B6612815**, permanent **09FD5942CD4F**, statement **27**, proof **32–38** (polar boundary minimum).
- **Theorem 4.3.6**, source **classical-potential-theory:F84A686D**, permanent **C651523E22C3**, statement **47**, proof **52–56** (regularized reduction).
- **Theorem 4.3.7**, source **classical-potential-theory:5388371B**, permanent **ABDF7610F7B2**, statement **61–69**, proof **74–94** (admissibility, capacities, capacitability).
- **Theorem 4.3.9**, source **classical-potential-theory:1D4FC015**, permanent **39A7F7684147**, statement **100–104**, proof **109–117** (polar poles, balayage).
- **Theorem 4.3.10**, source **classical-potential-theory:FA6C8523**, permanent **C4F5D8B270EB**, statement **122**, proof **127–131** (domination for everywhere-finite Green potentials).

This proof is an **independent topological and Newtonian calculation**. It does not need any Demailly approximation, Bergman, L² or Ohsawa–Takegoshi argument.

## Precise statement and counterexample to the unprinted strengthening

Let \(d\geq3\) and \(A=\mathbb Q^d\subset\mathbb R^d\). Then:

1. \(A\) is polar. For every \(a\notin A\), there is a **finite positive Radon measure** \(\mu\) with **finite total mass** such that its positive Newtonian potential \(p=G_{\mathbb R^d}\mu\) satisfies \(p(a)<\infty\) and \(p(q)=+\infty\) for **every** \(q\in A\).
2. **No proper superharmonic function on \(\mathbb R^d\) has pole set exactly \(A\).** This is a topology-of-level-sets obstruction, not a defect of the measures in (1): a superharmonic function is lower semicontinuous, so its \(+\infty\)-locus is a \(G_\delta\) subset of the ambient space, whereas \(\mathbb Q^d\) is not \(G_\delta\).
3. In fact **every** proper superharmonic \(u\) whose poles contain \(A\) has a **comeagre, uncountable set of additional poles outside \(A\)**. Its entire pole set is nevertheless Lebesgue null (and polar). Thus a **dense \(G_\delta\) polar set** may be comeagre and still have measure zero.

Consequently Theorem 4.3.2 is correctly worded: arbitrary polar sets are **contained in** a superharmonic pole locus, whereas its **exact pole-set** construction has the extra compactness assumption. Replacing the first assertion by universal exactness would be false, and the compact clause does not justify that replacement.

## Independent proof

**Finite atomic Newtonian witness.** Enumerate \(A=\{q_j:j\ge1\}\), choose \(a\in\mathbb R^d\setminus A\), and fix the kernel \(G(x,y)=\kappa_d|x-y|^{2-d}\), where \(\kappa_d>0\) is the chosen conventional factor. Set
\[
m_j=2^{-j}\min\{1,|q_j-a|^{d-2}\}>0,\qquad
\mu=\sum_{j=1}^\infty m_j\,\delta_{q_j}.
\]
Then \(\mu(\mathbb R^d)\le1\). By positivity and Tonelli,
\[
p(a)=\kappa_d\sum_j m_j|q_j-a|^{2-d}
\le \kappa_d\sum_j2^{-j}=\kappa_d<\infty.
\]
Every \(q_j\) carries a strictly positive atom and hence \(p(q_j)=+\infty\). The increasing partial potentials have a superharmonic limit that is finite at \(a\), so \(p\) is a proper positive superharmonic Newtonian potential. There is no reliance on an unproved existence theorem for an arbitrary polar set.

**Topological obstruction.** If \(u\) is lower semicontinuous, then
\[
\{u=+\infty\}=\bigcap_{n\ge1}\{u>n\},
\]
an intersection of open sets. If it contains the dense set \(A\), each open set \(\{u>n\}\) is dense, and the pole locus \(P\) is a **dense \(G_\delta\)**, hence comeagre. The rational lattice \(A\) is countable and meagre. Therefore \(P\setminus A\), the intersection of \(P\) with the comeagre set \(\mathbb R^d\setminus A\), is itself comeagre and in particular uncountable, by Baire's theorem. This also proves independently that \(A\) cannot itself be a \(G_\delta\).

**Nullity and compatibility with polarity.** A proper superharmonic function is locally integrable; thus \(\{u=+\infty\}\) has Lebesgue measure zero, although it can be comeagre. Since \(P\) is a proper superharmonic pole locus, \(P\) is polar by the classical definition, and all its subsets (including \(P\setminus A\)) are polar. The finite prescribed point \(a\) is compatible with the existence of a dense \(G_\delta\) pole locus: a residual set need not be all of \(\mathbb R^d\).

**Compact exact-pole clause.** No contradiction arises with the second part of Theorem 4.3.2: a compact polar \(K\) is closed, hence is a \(G_\delta\) in the metric ambient space, and the printed decreasing-neighborhood/capacitary-potential construction has exactly the topological freedom needed for its stronger conclusion. The present argument neither independently certifies all the capacity steps at lines 18–20 nor claims that being \(G_\delta\) is *sufficient* for exact polarity.

## Full direct §4.3 audit scope and dependency ledger

The entire mathematical section was directly read, not just Theorem 4.3.2: the planar/unbounded boundary argument in 4.3.4 (27–38); regularized reduction, exceptional sets and compact-potential claim in 4.3.6 (43–56); admissible-domain equilibrium mass and Choquet extension in 4.3.7 (61–94); polar removal and Perron pasting in 4.3.9 (100–117); and domination with the Lusin compact-restriction stage in 4.3.10 (122–131). **No further confirmed printed false theorem or independently verified complete repair is asserted in this run.**

The integrated proof of 4.3.2 still cites a checked **Foundations polar-globalization** input for arbitrary bounded polar sets (line 14). The other printed proofs use the checked Foundations envelope/polar discrepancy, the polar boundary principle, the Choquet capacitability argument, Perron comparison, and the Lusin/support-continuity decomposition. These are **selected or declared external/internal inputs**, **not certified transitive proof chains** by rereading §4.3. Earlier §4.3 reports on two-ball capacity interaction (2026-11-15) and everywhere-finite domination (2026-11-17) remain distinct, unchanged, and are not presented as discoveries here.

**Correction / recommendation:** retain **every original statement, mathematical hypothesis, attribution, source label and permanent tag**. An optional supplementary remark after 4.3.2 should distinguish containment from exact pole sets and exhibit the \(A=\mathbb Q^d\) obstruction above. This is an **audit-only proposed addition**: there is no production edit.

**Affected dependents:** any use of 4.3.2 or 4.3.9 requiring **the exact pole set of an arbitrary (not necessarily compact) polar subset** would need an additional topological hypothesis and proof; the printed reductions and capacity formulas are **not** found false here. This is a guard against overstrengthening, not a claim that a specific named downstream theorem already contains the mistake.

**Coverage accounting:** **+1 whole numbered section directly read** (§4.3, physical lines 7–131), **0 newly certified complete upstream chains**, **0 claim of first-ever visit** (past §4.3 partial reviews retained). Present 25-chapter / 747-section inventory unchanged. No software builds, tests, CI, website publication or changes to main, source, registry or permanent tags.

**Explicit exclusion:** Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remain **deferred-by-user** (neither certified nor repaired).
