# 2026-10-30: quantitative separation of smooth degenerate Monge–Ampère solutions and an empty-section inventory

**Pinned production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Audit branch: `review/mathematical-audit`. **Scope:** new selected nonexcluded §14.27 ODE argument; six unreviewed heading-only reading pages classified as navigation, *not* mathematical proofs. No Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas or positivity-loss work was attempted.

## POME-DEGENMA-ORDER-QUANT-SEPARATION-001 — low / verified conditional deduction

**Integrated sources and anchors.** `docs/sections/uniqueness-for-degenerate-equations--nonuniqueness-with-a-zero-set-of-empty-interior/index.html`, main blob `3cd83bbb6ab246cda0adae1789d7374d815529a6`. Theorem **14.27.1**, source `non-kahler-pluripotential-theory:FBA8D992`, permanent tag `E16A6F31A061`, lines **10–15**, **174–202**. Lemma **14.27.3**, source `non-kahler-pluripotential-theory:DF551C7A`, permanent tag `C96C68E6BB33`, lines **50–119**; ODE (14.27.4), source equation `3605D054`, permanent tag `FE5D8F02666F`, lines **52–55**. Smooth flat extension Lemma **14.27.7**, source `non-kahler-pluripotential-theory:B92AD5B5`, permanent tag `31CA87ECD1DF`, lines **124–170**. The coefficient formulas, density, and rank-one boundary matching appear at **22–47**, **183–195**.

**Hypotheses.** Keep the exact smooth nonclosed background and the fixed flat density of Theorem 14.27.1, with (0<s<1), (p(r)=C\exp[-1/(1-r^2)]) on ((-1,1)), extended by zero, and the smooth coefficient functions (x,y,z,k_s) printed in §14.27. The scalar ODE on ((-1,1)) is
[
 h'=F_s(r,h):=\frac{k_s(r)}{(x(r)+h)(y(r)-h)}-z(r),\quad
 h_\eta(0)=sp(0)-\eta,
]
on the admissible open strip (-x(r)<h<y(r)). By the printed Lemmas 14.27.3 and 14.27.7, for (0<\eta<\eta_0) the solution is smooth, admissible, and extends flatly by zero at both endpoints. Write (u_\eta=G_\eta(r)-\rho-\sup_X(G_\eta(r)-\rho)) with (G'_\eta=h_\eta).

**New rigorous deduction (distinct from the previously logged smooth nonisolation).** Let (0<\eta_1<\eta_2<\eta_0) and (Delta=\eta_2-\eta_1>0). The interval ((-x,y)) is convex, and the right-hand side is smooth there. Put (H=h_{\eta_1}-h_{\eta_2}). By the fundamental theorem of calculus in the (h)-variable,
[
 H'(r)=a(r)H(r),\quad
 a(r)=\int_0^1
 \frac{k_s(r)[x(r)-y(r)+2(h_{\eta_2}(r)+tH(r))]}
 {\bigl[(x(r)+h_{\eta_2}(r)+tH(r))(y(r)-h_{\eta_2}(r)-tH(r))\bigr]^2}\,dt .
]
Because (H(0)=Delta), the *exact* difference formula is
[
 H(r)=\Delta\exp\left(\int_0^r a(t)\,dt\right)>0
 \qquad(-1<r<1).\tag{1}
]
Thus no two distinct branch slopes cross, not merely at (r=0) but at any interior level. Their difference vanishes outside the band by the flat extension. The difference (u_{\eta_1}-u_{\eta_2}), whose derivative as a function of (r) is (H>0), is therefore constant on each of the two outer components and strictly increasing on the middle band, independent of the additive sup normalizations. In particular,
[
 \boxed{\operatorname{osc}_X(u_{\eta_1}-u_{\eta_2})
  =\int_{-1}^{1}H(r)\,dr
  =\Delta\int_{-1}^{1}
      \exp\left(\int_0^r a(t)\,dt\right)dr>0.}\tag{2}
]
This identifies the precise locations of the maximum and minimum (right and left outer components, respectively); none can occur strictly inside the middle band.

For a **uniform quantitative separation**, choose (b>0) with ([-b,b]subset(-1,1)), and shrink the admissible parameter interval to (0<\eta<\eta_*<\eta_0) so that continuous ODE dependence keeps every solution on ([-b,b]) inside a common compact subset of the strip (-x<h<y). Then (|\partial_hF_s|\le L_b<\infty) there, uniformly in the parameters. Equation (1) gives (H(r)\ge\Delta e^{-L_b b}) for (|r|\le b), so
[
 \operatorname{osc}_X(u_{\eta_1}-u_{\eta_2})\ge
 2b e^{-L_b b}|\eta_2-\eta_1|,\qquad
 \boxed{\|u_{\eta_1}-u_{\eta_2}\|_{L^\infty(X)}
 \ge b e^{-L_b b}|\eta_2-\eta_1|.}\tag{3}
]
The last step uses (\operatorname{osc}(w)\le2\|w\|_\infty). This is a lower bound, **not** a global Lipschitz upper estimate near the flat endpoints. Local differentiation in the parameter additionally yields (\partial_\eta h_\eta(r)=-\exp(\int_0^r\partial_hF_s(t,h_\eta(t))dt)) on compact subintervals.

**Disposition.** Theorem 14.27.1 and both ODE lemmas are correct in the checked comparison argument. This does not supply an independent proof of the entire background construction, global smooth extension, or bounded-mass assertion; those remain inputs. This sharpens the geometry of the already known uncountable family; it does not re-register the prior `POME-DEGENMA-CINF-NONISOL-001` finding concerning convergence to a base solution. No production patch needed; an optional explanatory corollary could follow the proof of Theorem 14.27.1. **Affected dependents:** normalization and pairwise distinction in Theorem 14.27.1 and comparisons with §14.28; no change to either statement or its permanent tags.

## Actual previously unreviewed ToC entries classified as navigation-only

Direct inspection of the following exact main HTML reading pages shows a subject heading, navigation links and citation UI, but **no theorem, lemma, equation or mathematical argument in the section body**. Consequently a coverage matrix cannot truthfully award these pages proof-level coverage; mathematical claims begin in their linked following sections.

| Number | Exact main reading file | Blob SHA | Classification |
| --- | --- | --- | --- |
| 2.11 | `docs/sections/open-maps-nuclear-spaces-and-inverse-limits/index.html` | `99adde997e94fb2b2265f34f30ed566a3ceaa45c` | navigation only |
| 5.52 | `docs/sections/real-currents-submersions-and-homotopies/index.html` | `a16972987b525c05330c76f30b60181865986d1c` | navigation only |
| 9.37 | `docs/sections/normal-spaces-and-tube-continuation/index.html` | `01a93b78d1e2085f407db1f6f073445e3738383b` | navigation only |
| 9.48 | `docs/sections/convex-neighborhoods-and-coherent-vanishing/index.html` | `d4122041dbf4d7fc2b712e475af5d903fed3f7e9` | navigation only |
| 10.53 | `docs/sections/spectral-sequences-support-and-cup-products/index.html` | `ab6d205468700bcac45daab8cd763377fa2e60c1` | navigation only |
| 10.76 | `docs/sections/compact-curves-periods-and-complex-tori/index.html` | `f19750ab7bab07f32873dcd297f2332b3f461129` | navigation only |

This is **structural inventory coverage**, not mathematical verification or evidence of a duplication. We did not infer the following theorems from a parent heading or source number.

## Coverage and open ledger

Direct new mathematical checks were limited to the order, the exact difference equation, normalization invariance, and the uniform compact-interior constant for §14.27.3/.7 and Theorem 14.27.1. Six previously unreviewed section headers were classified as navigation-only. No full theorem dependency chain or section was certified. The live table of contents remains **25 chapters and 747 numbered section entries**, with **zero fully mathematically certified sections**. Existing confirmed errors, proof gaps, candidates, historical attribution and external dependencies are unchanged. Demailly approximation/regularization and the dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remain **deferred-by-user**, never resolved or certified.

No source, body, proof registry, canonicalization, permanent tag, production main, website, CI, full build or formal verification was changed or run. This report records only verified audit notes on the dedicated review branch.
