# 2026-10-30 — Sparse spherical obstacles and the exact logarithmic borderline in the Wiener series

**Finding:** POME-WIENER-SPARSE-BALLS-LOGLOG-001  
**Severity / disposition:** low / **verified conditional deduction**. The printed Wiener theorem is **correct** in the model. No source theorem is disproved, no missing proof of the general theorem is alleged, and no complete section is certified.  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272  
**Audit branch:** review/mathematical-audit; report-only proposal, not a change to the mathematical reading edition.

## Integrated source and exact anchors

1. **Theorem 4.4.26**, source label **classical-potential-theory:BE9DEDF9**, permanent tag **A856D11F5895**, in **docs/sections/perron-theory-and-fine-boundary-limits/index.html**, main blob **4bc2fb9317e2b6f6bb5b2d90208c677da8275eba**, physical lines **345–350** (the Helms relative-capacity Wiener statement) and **353–380** (separated-shell proof). Section 4.4 carries tag **5CFAC22DC258**.
2. **Proposition 4.1.16**, source label **foundations-of-pluripotential-theory:3D5469C4**, permanent tag **4A7451727417**, in **docs/sections/potentials-energy-and-capacity/index.html**, main blob **4962a7cd576a64cb47fa0955dcc80cf87c3da9d1**, physical lines **450–482** (Green-potential and equilibrium-mass normalization).
3. **Example 4.1.21**, source label **foundations-of-pluripotential-theory:01C621E0**, permanent tag **FC1E9D9B42F0**, same main file and blob, physical lines **628–642** (spherical Newtonian equilibrium potential and capacity); **Theorem 4.1.19**, source label **foundations-of-pluripotential-theory:AFB551A5**, permanent tag **AEE550586C10**, physical lines **560–625** (relative outer capacity). Historical citation/attribution is unaffected.

These anchors were read from the integrated reading edition. The full published proof of Theorem 4.4.26 and its fine-topology prerequisites have **not** been independently re-established in this audit; the deduction below uses that theorem explicitly.

## New model and quantified conclusion

Fix **d >= 3**, the Euclidean unit vector e_1, and Helms's radial fundamental kernel
\[
\Phi(r)=\kappa_d r^{2-d},\qquad \kappa_d>0
\]
(the normalization constant does not affect the result). Set
\[
\lambda=4^{d-2},\qquad
\rho_j=\Phi^{-1}(\lambda^{j+1/2}),\qquad
s_j=\frac{\rho_j}{20(j+1)^\alpha[\log(j+\mathrm e)]^\beta},
\qquad \alpha,\beta\ge0.
\]
Thus \(\rho_{j+1}=\rho_j/4\). For sufficiently large integer J, \(2\rho_J<1/4\). Define pairwise disjoint closed obstacles
\[
F_j=\overline{B(\rho_j e_1,s_j)},\qquad
E=\{0\}\cup\bigcup_{j\ge J}F_j,\qquad
\Omega=B(0,1)\setminus E.
\]
Then E is compact, \(\Omega\) is a bounded connected Greenian domain, and \(0\in\partial\Omega\). The following classification holds:
\[
\boxed{
\begin{array}{ll}
0\text{ is regular for }\Omega
&\Longleftrightarrow\
\alpha(d-2)<1,\ \text{or }\alpha(d-2)=1
\text{ and }\beta(d-2)\le1,\\[2mm]
0\text{ is irregular for }\Omega
&\Longleftrightarrow\
\alpha(d-2)>1,\ \text{or }\alpha(d-2)=1
\text{ and }\beta(d-2)>1.
\end{array}}
\]
In particular, equality in **both** logarithmic exponents belongs to the **regular** regime. For d=3, the first critical radius scale is \(s_j\asymp\rho_j/j\), and at that scale the second critical correction is \(1/\log j\). For d=4 the corresponding exponents are \(1/2\).

The obstacles tend to zero along one ray and contain **no exterior solid cone** with vertex 0, including in the regular regime. Thus the exterior-cone condition of Theorem 4.4.6 is sufficient but far from necessary for these domains.

## Proof

**(1) Exact shell isolation.** Since \(\Phi\) is strictly decreasing and \(\lambda^{1/(d-2)}=4\), the shell
\[
S_j=\{y:\lambda^j\le\Phi(|y|)\le\lambda^{j+1}\}
\]
is precisely the radial annulus \(\rho_j/2\le|y|\le2\rho_j\).
For \(\alpha,\beta\ge0\) and \(j\ge J\), \(s_j\le\rho_j/20\); hence every point of \(F_j\) has radius between \(19\rho_j/20\) and \(21\rho_j/20\), strictly inside \(S_j\). Since centers at successive indices differ in radius by factor four, each \(F_k\) with \(k\ne j\) lies outside \(S_j\). The isolated point 0 is in none of the shells. The complement of the unit ball is absent from the sufficiently small shells. Thus the precise Wiener set \(E_j=(\mathbb R^d\setminus\Omega)\cap S_j\) equals \(F_j\), for all sufficiently large j. All finite initial terms are irrelevant.

**(2) Uniform Green-capacity bounds, not an informal substitution of Euclidean capacity.** Put \(B_0=B(0,1/2)\). On \(B(0,1/4)\times B(0,1/4)\), the ball Green kernel satisfies
\[
G_{B_0}(x,y)=\Phi(|x-y|)-H_{B_0}(x,y),\qquad
0\le H_{B_0}(x,y)\le M_d<\infty.
\]
Indeed \(H_{B_0}(\cdot,y)\) is the harmonic extension of the boundary values \(\Phi(|\zeta-y|)\), which are uniformly bounded for \(|y|\le1/4\), since \(|\zeta-y|\ge1/4\) on \(\partial B_0\).

Let \(F=\overline{B(c,s)}\subset B(0,1/4)\) be any of the small obstacles and let \(\mu\) be any probability supported on F. The diameter bound implies
\[
I_{B_0}(\mu)\ge\kappa_d(2s)^{2-d}-M_d.
\]
For the normalized surface probability \(\sigma\) on \(\partial F\), the spherical Newtonian potential calculation in Example 4.1.21 gives
\[
I_{B_0}(\sigma)\le \kappa_d s^{2-d}.
\]
By the Green equilibrium variational principle (equivalently, the mass-one normalization of the equilibrium measure in Proposition 4.1.16), \(C_{B_0}(F)^{-1}\) is the minimum Green energy of a probability supported on F, up to any fixed convention constant. For sufficiently small s the two inequalities therefore imply uniform constants \(0<c_d<C_d<\infty\) with
\[
c_d s^{d-2}\le C_{B_0}(F)\le C_d s^{d-2}.
\]
Compact capacitability yields \(C^*_{B_0}(F)=C_{B_0}(F)\). All constants are independent of j, \(\alpha\), and \(\beta\), once the obstacles lie in the fixed interior quarter ball.

**(3) Critical series.** The radius equation gives \(\lambda^j \rho_j^{d-2}=\kappa_d\lambda^{-1/2}\), hence
\[
\lambda^j C^*_{B_0}(E_j)
\asymp
\lambda^j s_j^{d-2}
\asymp
(j+1)^{-\alpha(d-2)}
[\log(j+\mathrm e)]^{-\beta(d-2)}.
\]
The Cauchy condensation/integral test for the positive series
\(\sum_{j\ge J}j^{-A}(\log j)^{-B}\)
says that it converges if and only if \(A>1\), or \(A=1\) and \(B>1\). Theorem 4.4.26 identifies convergence with thinness of \(\mathbb R^d\setminus\Omega\) at 0 and hence **irregularity** of 0. Divergence gives regularity. This proves the boxed classification, including the two exact boundary equalities.

The domain is connected because removing a countable sequence of pairwise disjoint closed balls accumulating only at 0 from a Euclidean ball in dimension at least two still permits paths to be locally detoured around each ball; away from 0, a compact path meets only finitely many obstacles. The origin is approached from directions outside the obstacle ray. No solid cone based at 0 is contained in E because the radial intervals occupied by the obstacles have open gaps arbitrarily near 0.

## Audit disposition and consequences

- **Verified conditional deduction (low):** the exact two-stage logarithmic threshold is newly calculated for the printed Wiener normalization. It is a model consequence of Theorem 4.4.26, not a new proof or certification of that general theorem.
- **Proposed optional addition:** append this model as an illustrative corollary or example after Theorem 4.4.26, with the explicit warning that convergence of the Wiener series means *irregularity*, not regularity. Do not edit source, generated docs, or permanent tags in the audit branch.
- **Affected uses:** §§4.4.20–26 fine-boundary tests, the sufficiency-only geometric exterior cone criterion in §4.4.6, and applications distinguishing sparse nonpolar obstacles from regular boundary geometry. Existing potential-theoretic prerequisites and their historical attribution remain intact.
- **No repeated finding:** the older §4.4 Wiener/Perron pass only inspected selected dependencies. The earlier §4.5 sphere balayage calculation concerns inward sweeping and loss of mass, not sparse-hole Wiener regularity.
- **Remaining gaps:** no independent reconstruction of the entire Helms fine-topology/Perron theorem, no general higher-dimensional obstacle classification, no full §4.4 or chapter certificate. The d=2 logarithmic kernel has a different radial shell scale and was not asserted here.

## First-reading inventory outside the primary model

Freshly inspected integrated explanatory §§5.1, 5.7 and 5.21 at main; these are **expository subject introductions with mathematical orientation and historical pointers**, not mathematical theorem-proof certifications. Exact files/blobs:

- §5.1, tag **4DEEEF894245**, source **foundations-of-pluripotential-theory:1490D738**, **docs/sections/complex-differential-forms-and-positive-currents/index.html**, blob **fec3c3e220607b33de74642b64e444ac8f21b41e**, physical lines **7–16**.
- §5.7, tags **7B39B08A9568**, **3DA7635DF422**, sources **foundations-of-pluripotential-theory:2E0A1A61** and **sgpt:881F502D**, **docs/sections/plurisubharmonic-functions/index.html**, blob **bc8a7baa7d35967c7d56a357c4d9022ff36a51d9**, physical lines **7–30**.
- §5.21, tag **EDB5A2485B58**, source **non-kahler-pluripotential-theory:710BAAFB**, **docs/sections/plurisubharmonic-functions-and-singularities/index.html**, blob **1b0067104a17b95c283a89791721bb9b04edad39**, physical lines **7–11**.

The conceptual claims and referenced downstream theorems were **not** transitively certified. No Bergman/L2/OT/positivity-loss proof was opened in this pass; the user-excluded Demailly approximation and regularization programme continues as **deferred-by-user**, not resolved.

**Coverage accounting:** current 25 chapters, 747 numbered ToC sections, **zero entirely certified sections**. One selected new explicit theorem model (§4.4.26, with §4.1.16/.21 normalization crosschecks) and three first direct expository inventories (§§5.1,5.7,5.21) only. All older error/gap/duplication/external/deferred ledger dispositions remain unchanged. No build, CI, publication, website edit, or formal verification was performed.
