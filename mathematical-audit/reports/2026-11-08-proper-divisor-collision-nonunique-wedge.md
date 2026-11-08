# Proper-intersection collapse: the limiting wedge is not determined by the limiting divisors

**Finding:** `POME-CYCLE-TRANSVERSE-COLLISION-NONUNIQUE-001`  
**Date:** 2026-11-08  
**Severity/status:** low — **verified conditional deduction** (sharpness of hypotheses). No printed theorem is contradicted; no proof repair is certified.  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Integrated reading-edition file:** `docs/sections/divisors-and-logarithmic-limits-on-analytic-cycles/index.html` (main blob `dae567406b2030e550664ca57b1fe77911d956d4`).  
**Section:** 20.5, *Divisors and logarithmic limits on analytic cycles*, first selected theorem-level visit.

## Source-anchored claims actually inspected

- Lemma **20.5.2**, source `demailly-complex-geometry:72B4BF94`, permanent tag `551A781E3A1C`, HTML physical lines **10–21**: locally uniform convergence of nontrivial holomorphic functions implies local $L^1$ convergence of their logarithms.
- Theorem **20.5.5**, source `demailly-complex-geometry:D58680EB`, permanent tag `F1C928146DBC`, HTML lines **63–129**: the normalized Poincaré–Lelong divisor on an analytic cycle, with convergence under locally uniform variation where the limit is not identically zero on any component.
- Theorem **20.5.10**, source `demailly-complex-geometry:34D8935D`, permanent tag `DDB973C0C1DD`, HTML lines **132–152**: a properly intersecting tuple of effective Cartier divisors has an integral positive intersection current; all subfamily codimension hypotheses are required.
- Example **20.5.11**, source `demailly-complex-geometry:1764A64B`, permanent tag `FF4839E28893`, HTML lines **154–156**: cusp multiplicity (context only, not independently re-certified).

These are the actual integrated statements/replacement proofs, not merely source theorem numbers. The tag labels are preserved. The name of the source book does **not** authorize reopening the owner-excluded Demailly approximation programme.

## New explicit result: collapse of proper intersections is nonunique

Let \(U=\{(x,y)\in\mathbb C^2:|x|<1,\ |y|<1\}\), let \(P\in\mathbb C[y]\setminus\{0\}\), and for every \(0<|\varepsilon|<\varepsilon_0\) set
\[
 f_\varepsilon(x,y)=x,\qquad g_{\varepsilon,P}(x,y)=x+\varepsilon P(y),
 \quad D=[\operatorname{Div}(x)],\quad G_{\varepsilon,P}=[\operatorname{Div}(g_{\varepsilon,P})].
\]
All divisors here are effective Cartier divisors. Because \(f_\varepsilon\to x\) and \(g_{\varepsilon,P}\to x\) uniformly on compact sets, Lemma 20.5.2 gives
\[
 \log|f_\varepsilon|^2\to\log|x|^2,\qquad
 \log|g_{\varepsilon,P}|^2\to\log|x|^2
 \quad\text{in }L^1_{\rm loc}(U).
\]
Consequently \(D\to D\) and \(G_{\varepsilon,P}\to D\) **weakly as positive closed currents**, independently of \(P\). In particular both individual divisor currents have the same limits for all choices of \(P\).

For each \(\varepsilon\ne0\), however,
\[
 \operatorname{Supp}D\cap\operatorname{Supp}G_{\varepsilon,P}
 =\{(0,a): P(a)=0,\ |a|<1\}.
\]
If \(P\) has no roots in the unit disc this intersection is empty; otherwise it is zero-dimensional. Hence the full \(\{1\}\), \(\{2\}\), and \(\{1,2\}\) codimension requirements of Theorem 20.5.10 hold **for every nonzero \(\varepsilon\)**. Restricting the second defining function to the smooth divisor \(D\simeq\{|y|<1\}\) and using \(dd^c=(i/2\pi)\partial\bar\partial\),
\[
\begin{aligned}
 D\wedge G_{\varepsilon,P}
 &=dd^c\bigl(\log|g_{\varepsilon,P}|^2[D]\bigr)\\
 &=dd^c_D\log|\varepsilon P(y)|^2\\
 &=\sum_{\substack{P(a)=0\\|a|<1}}
          \operatorname{ord}_a(P)\,[(0,a)].
\end{aligned}
\]
The constant \(\log|\varepsilon|^2\) is killed by \(dd^c_D\). Thus **the intersection current is exactly independent of \(\varepsilon\ne0\)**, but its weak limit depends on \(P\).

For example, \(P(y)=1\) gives \(D\wedge G_{\varepsilon,1}=0\) for every nonzero \(\varepsilon\), whereas \(P(y)=y\) gives
\[
D\wedge G_{\varepsilon,y}=[(0,0)]
\quad\text{for all }\varepsilon\ne0.
\]
Both pairs converge to exactly the same limiting pair \((D,D)\). Taking \(P(y)=y-a\), \(a\ne0\), \(|a|<1\), instead yields \([(0,a)]\). For polynomials with distinct roots in the disc the two hypersurfaces meet **transversely**: their Jacobian is
\[
 \det\begin{pmatrix}1&0\\1&\varepsilon P'(a)\end{pmatrix}
 =\varepsilon P'(a)\ne0.
\]
Thus even requiring *transversality for every approximating pair* does not determine a limiting wedge when transversality/properness fails **at the limit**. Polynomials with multiple roots yield any prescribed finite positive integral zero-cycle on \(D\) inside \(U\), using the same normalized Poincaré–Lelong computation (in that case the individual intersections need not be transverse).

The limiting pair \((D,D)\) does not satisfy the proper-intersection codimension hypothesis: its common support has codimension one, not two. Moreover \(\log|x|^2|_D\equiv-\infty\), so the usual recursive current \(\log|x|^2[D]\) is **not defined as a locally finite coefficient current**. The calculations therefore do **not** produce competing values for a well-defined printed self-intersection; they show why no weakly sequentially continuous extension determined solely by the two weak current limits is available.

## Audit disposition

**Classification:** verified conditional deduction, low severity. The printed Lemma 20.5.2 and Theorems 20.5.5/20.5.10 are consistent with this model. They separately give continuity of logarithmic potentials / divisor currents, and existence/integrality of wedge currents **only when the stated proper-intersection hypotheses hold**. There is no claim of a false theorem, mathematical duplication, or a completed dependency-chain proof.

**Proposed optional reading-edition clarification (NOT applied):** directly after Theorem 20.5.10, add a warning that local $L^1$ convergence of each divisor potential, even together with transverse proper intersection in every approximant, does not give convergence to a product of the limiting divisors when the limit loses proper intersection. The two explicit families $P=1$ and $P=y$ show nonuniqueness. Retain every original label, source attribution and theorem hypothesis.

**Affected dependents:** only arguments *if any* in Chapters 7/20 or elsewhere that attempt to pass to the limit in divisor wedges without checking the limiting codimension or another suitable uniform integrability/non-pluripolar product theorem. No particular downstream assertion was established to make such an invalid step in this run; no dependent is marked erroneous. The proof of Theorem 20.5.10 itself was read and its inductive use of the proper-intersection condition cross-checked in this concrete model, not fully re-certified.

**Scope / exclusions:** one first *selected theorem-level* visit to §20.5, with Example 20.5.11 context. No other section is counted reviewed, and **zero complete-section certifications** are claimed. ToC matrix remains 25 chapters / 747 numbered sections. Existing findings and the expressly excluded Demailly approximation/regularization, dedicated Bergman, weighted $L^2$, Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof-completion programme remain **deferred-by-user** (not resolved/certified). This report is audit-only Markdown: no source change, build, tests, CI, formal verification, publication or automatic merge.
