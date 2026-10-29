# Mathematical audit — 2026-10-29: sequential vague compactness and oscillatory mixed b-divisor intersections

**Reviewed production main:** <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code>.
**Starting audit branch:** <code>0dffae73a44fce17e2ad43c3dffdb8f8bf6bcdc6</code>.
**Scope:** selected integrated proofs in §2.7.3 and §20.1.7/.9/.10–12/.39/.40/.41/.43/.45/.47/.49. The independent measure and birational arguments below do not certify the full sections or all dependencies. The Demailly approximation/regularization programme and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale atlas and positivity-loss components remain **deferred-by-user**, not reopened or certified.

## Finding register

| Stable ID | Severity / status | Printed proposition | Proposed disposition |
| --- | --- | --- | --- |
| **POME-RADON-LOCAL-MASS-SEQUENTIAL-COMPACT-001** | low / **verified conditional deduction** | Theorem 2.7.3 correct | Optional independent sequential compactness/metrizability corollary, valid for its **positive Radon measures on a Euclidean domain with the printed common local mass bounds**. Do not generalize to arbitrary topological spaces or signed measures without suitable total-variation bounds. |
| **POME-BDIV-MIXED-OSCILLATION-POSITIVE-001** | low / **verified conditional deduction** | Proposition 20.1.47 correct | Optional two-variable example: two **big and nef Cartier** b-divisor sequences converge modelwise with **constant positive individual volumes**, but their mixed intersection oscillates. This supplements, and does not recatalogue, the printed single-volume discontinuity Example 20.1.9. |

Neither item is a false printed theorem, a proof-gap closure, a new external dependency, a certified full-section proof, or a genuine duplication.

## 1. POME-RADON-LOCAL-MASS-SEQUENTIAL-COMPACT-001

**Exact integrated location:** <code>docs/sections/measures-and-distributions--nets-and-compactness/index.html</code>, main blob <code>7e4a226a48f88a97b3db1a8dd7d8582c909aeea1</code>, physical lines **53–69** (Theorem 2.7.3 and compact product proof), supported by lines **13–51** (general net compactness and Tychonoff). **Source identifier:** <code>foundations-of-pluripotential-theory:5470287F</code>. **Permanent Pome tag:** <code>DF30CEF15D17</code>. Positive-measure convention: <code>docs/sections/measures-and-distributions--radon-measures-and-integration/index.html</code>, blob <code>f0086e0d7fa46b8d1756eebb839b0ba14e663863</code>, introductory paragraph after line 5. Internal Riesz representation: Theorem 2.3.3, permanent tag <code>0C614771FB98</code>.

**Claim with the printed hypotheses.** Let \(\Omega\subset\mathbb R^d\) be open, \(K_r\) a compact exhaustion with \(\operatorname{Int}K_r\uparrow\Omega\), \(\chi_r\in C_c(\Omega)\), \(\chi_r\ge0\), \(\chi_r=1\) on \(K_r\), and \(M_r<\infty\). Let
\[
\mathcal M=\{\mu\ge0:\mu\text{ Radon on }\Omega,\ \int\chi_r\,d\mu\le M_r\ \forall r\}.
\]
Then the vague topology on \(\mathcal M\) is metrizable. In particular, every **sequence** in \(\mathcal M\) has a vaguely convergent subsequence with limit in \(\mathcal M\), in addition to the already printed Willard-subnet compactness statement.

**Proof of countable determination.** For each \(r\), let
\[
C_{K_r}=\{f\in C_c(\Omega,\mathbb R):\operatorname{supp}f\subset K_r\}.
\]
As a closed subspace of \(C(K_r)\), it is separable for the supremum norm: \(K_r\) is a compact metric space. Fix a countable norm-dense family \(f_{r,k}\) in \(C_{K_r}\) for each \(r\), and enumerate their union as \((g_\ell)_{\ell\ge1}\). Since \(\chi_r=1\) on \(K_r\) and \(\mu\ge0\), every \(\mu\in\mathcal M\) has \(\mu(K_r)\le M_r\). For \(f,h\in C_{K_r}\) and every \(\mu\in\mathcal M\),
\[
\left|\int(f-h)\,d\mu\right|\le M_r\|f-h\|_\infty. \tag{1}
\]
Any compactly supported \(f\) belongs to some \(C_{K_r}\) by the exhaustion property. Approximation in (1) proves that convergence of integrals against the \(g_\ell\)'s is equivalent, **on \(\mathcal M\)**, to vague convergence against all of \(C_c(\Omega)\). Uniqueness of Radon measures makes the coordinate map injective. Consequently
\[
d(\mu,\nu)=\sum_{\ell\ge1}2^{-\ell}
 \min\!\left\{1,\left|\int g_\ell\,d(\mu-\nu)\right|\right\}
\]
is a metric inducing the restricted vague topology. The statement is specific to the common local bounds and the separable Euclidean base.

**Independent sequential compactness proof.** Given \((\mu_j)\subset\mathcal M\), the real sequence \(\int g_\ell\,d\mu_j\) is bounded for each \(\ell\), by (1) with \(h=0\). The elementary diagonal-subsequence argument extracts \(j_k\) such that every test coordinate converges. Estimate (1) then shows that \(\int f\,d\mu_{j_k}\) is Cauchy for *every* \(f\in C_c(\Omega,\mathbb R)\), without making any sequential-compactness assertion for the ambient uncountable product. Set \(L(f)=\lim_k\int f\,d\mu_{j_k}\). The functional \(L\) is positive and linear; on \(C_{K_r}\) it is bounded by \(M_r\|f\|_\infty\), hence it is locally bounded. The **internal** positive Riesz representation theorem (2.3.3) gives a positive Radon measure \(\mu\) representing \(L\). As the original \(\chi_r\) are compactly supported test functions,
\[
\int\chi_r\,d\mu=\lim_k\int\chi_r\,d\mu_{j_k}\le M_r,
\]
so \(\mu\in\mathcal M\) and \(\mu_{j_k}\to\mu\) vaguely. This is an exact elementary diagonal argument, conditional only on the stated internal representation theorem.

**Boundary and affected dependents.** Theorem 2.7.3 is fully consistent with the proof: its uncountable product/Willard-subnet proof is correct, but stronger **sequential** compactness happens to hold in the specific locally bounded Radon-measure case. An extension to signed measures would require uniform **total variation** bounds, not merely signed values on the positive cutoff tests. This refinement can simplify subsequent positive current and measure diagonal extractions when local mass bounds are already available, but no downstream result is automatically certified.

## 2. POME-BDIV-MIXED-OSCILLATION-POSITIVE-001

**Exact integrated location:** <code>docs/sections/the-theory-of-b-divisors/index.html</code>, main blob <code>4a793dfd462badcb351f54a36cb030cde14a399b</code>. Definitions 20.1.5/10–12, lines **39–53 and 123–145**; Definition 20.1.39, lines **737–743**; Lemma 20.1.40, lines **746–796**; Proposition 20.1.43, lines **809–851**; diagonal volume Proposition 20.1.45, lines **880–899**; upper-semicontinuity Proposition 20.1.47, lines **916–960**; decreasing-net continuity Proposition 20.1.49, lines **962–975**. The printed distinct one-variable comparison is Example 20.1.9, lines **100–120**.

**Source identifiers and permanent tags:** Definition 20.1.39 <code>sgpt:6AA949A3</code> / <code>BFB26AC5F975</code>; Lemma 20.1.40 <code>sgpt:456D590A</code> / <code>DFC2368D5436</code>; Proposition 20.1.43 <code>sgpt:5189BD1D</code> / <code>AEC81016D4BC</code>; Proposition 20.1.47 <code>sgpt:125DC222</code> / <code>754B050BFA6C</code>; Example 20.1.9 <code>sgpt:048A0D73</code> / <code>7AF528B0FB3B</code>.

**Construction.** Let \(X=\mathbb P^2\), \(H=c_1(\mathcal O_{\mathbb P^2}(1))\), and \(0<a,b<1\) be fixed. Choose two disjoint sequences of distinct closed points \((p_j)\), \((r_j)\) of \(X\). Put \(q_j=p_j\) for even \(j\), \(q_j=r_j\) for odd \(j\). For a point \(p\), let \(\pi_p:X_p=\operatorname{Bl}_pX\to X\) and \(E_p\) its exceptional curve. Define nef Cartier b-divisors \(\mathbb D_j\) and \(\mathbb F_j\) as the Cartier closures of the respective nef classes
\[
 \pi_{p_j}^*H-a[E_{p_j}],\qquad
 \pi_{q_j}^*H-b[E_{q_j}].
\]
These classes are in fact Kähler. If \(F_p:X_p\to\mathbb P^1\) is the resolved pencil of lines through \(p\), then \(F_p^*[\omega_{\rm FS}]=\pi_p^*H-[E_p]\) and
\[
\beta_{p,a}=(1-a)\pi_p^*\omega_{\rm FS}
       +aF_p^*\omega_{\rm FS}
\]
is a smooth positive definite form: the two maps separate tangent directions. Its class is \(\pi_p^*H-a[E_p]\). Thus both Cartier b-divisors are **big and nef** and have positive volumes
\[
\operatorname{vol}\mathbb D_j=1-a^2,\qquad
\operatorname{vol}\mathbb F_j=1-b^2.
\]
Every root class is \(H\).

**Convergence on every model.** Fix any modification \(\rho:Y\to\mathbb P^2\). Its failure-of-isomorphism locus in the smooth target is contained in finitely many points; the disjoint sequences eventually avoid them. Over each such \(p_j\) or \(q_j\), passing through the common blowup and then pushing the exceptional class down to \(Y\) gives exactly \(\rho^*H\). Consequently the traces of both \(\mathbb D_j\) and \(\mathbb F_j\) on this **fixed** \(Y\) equal \(\rho^*H\) for all large \(j\). Thus
\[
\mathbb D_j\to\overline H,\qquad
\mathbb F_j\to\overline H
\]
modelwise, even eventually constantly on each fixed model. Here \(\overline H\) is the Cartier closure of \(H\) on \(X\).

**Mixed intersections.** On the common blowup of the two points, compute using
\(H^2=1,\ H\cdot E_p=0,\ E_p^2=-1\), and \(E_p\cdot E_q=0\) for \(p\ne q\). The mixed intersection of the Kähler-realized nef Cartier b-divisors agrees with their ordinary cohomological intersection on the common model by the mixed-volume definition and the smooth representatives just constructed. Therefore
\[
(\mathbb D_j,\mathbb F_j)=
\begin{cases}
1-ab,&j\text{ even},\\
1,&j\text{ odd}.
\end{cases}
\]
In contrast, \((\overline H,\overline H)=1\). Thus both marginal volumes stay fixed **strictly positive**, and both b-divisor sequences converge modelwise, while their mixed intersections have **no limit**:
\[
 \liminf_j(\mathbb D_j,\mathbb F_j)=1-ab
 \quad<\quad \limsup_j(\mathbb D_j,\mathbb F_j)=1.
\]
This is consistent with, and makes sharp, the upper-semicontinuity inequality of Proposition 20.1.47; it does not violate Proposition 20.1.49, which additionally requires decreasing nets.

**Distinction from prior material and dependencies.** Printed Example 20.1.9 instead uses the boundary class \(H-E_{p_j}\) with **zero individual volume** and demonstrates failure of one-variable volume continuity. Here \(0<a,b<1\) forces strictly positive constant volumes and exhibits genuinely **two-variable mixed-product oscillation**, including infinitely many terms reaching the upper-semicontinuity bound. No earlier b-divisor domain error (including the unresolved \(\lambda=0\) issue in Lemma 20.1.40(3)) is reclassified or claimed repaired. The only mathematical inputs are elementary blowup intersection theory, positivity of \(\beta_{p,a}\), and the printed Definition 20.1.39 for Kähler-realized b-divisors. Do not change the canonical version, source or tags; an optional counterexample note could be placed near Proposition 20.1.47 after separate review.

## Coverage, limitations and dispositions

The audit inspected **new selected proof-level details** of §§2.7.3 and 20.1.7/.9/.10–12/.39/.40/.41/.43/.45/.47/.49, with the relevant positivity and modelwise quantifiers checked. The previously inventory-only §16.1, §16.2, §16.10 and §9.25 section pages were also opened and found to be **navigation/introductory pages without statement proofs**; this is **navigation-level only**, not mathematical proof coverage. Source text elsewhere was not needed. We certify **no full section** and **no complete dependency chain**; 25 chapters / 747 unique ToC sections / zero full-section certifications remains the inventory.

All earlier confirmed errors, conditional repairs, proof gaps, candidates, genuine duplications and unresolved/external dependencies retain their existing ledger statuses, especially the known b-divisor zero-scaling defect and non-Archimedean finite-concave-tail error. All author-excluded Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss work remains strictly **deferred-by-user**, neither resolved nor checked. No source/body, registry, canonicalization, permanent-tag, main, generated-site, CI, build, or formalization changes are proposed or performed here.
