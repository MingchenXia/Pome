# Positive-harmonic Liouville fibers: exact descent criterion; unibranch, Hermitian-adjoint, and classical-potential audit (2026-11-22)

**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
**Audit-only branch:** \`review/mathematical-audit\`.
**Classification:** one low-severity **verified conditional deduction**, not a printed error; no complete transitive upstream proof-chain certification.
**Excluded scope:** Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss completion programme are **deferred-by-user**, neither resolved nor certified. Related cross-references were recorded but the excluded proofs were not audited.

## Actual integrated reading-edition anchors

| Scope | Exact main file | Git blob | Mathematical physical lines and stable labels |
| --- | --- | --- | --- |
| **Whole §3.7** | \`docs/sections/polynomial-approximation-and-a-separate-subharmonic-example/index.html\` | \`a4a17c61ef30efb6fc6e20f105baeca052bbed43\` | Lines **7–37**; Proposition 3.7.1 source \`klimek-pluripotential-theory:01560C0B\`, permanent \`6D285B395FD0\`, lines 8–17; separate-subharmonic example lines 21–36 |
| **Core §9.10, selected extension catalogue only** | \`docs/sections/pluripotential-theory-on-unibranch-spaces/index.html\` | \`6edfa6b19fa7cdbaf0c2665389fa7b3ca338cdf4\` | Mathematical core **9–230**: Theorem 9.10.5 permanent \`E707851D5DBA\`, lines 39–66; Theorem 9.10.13 source \`sgpt:59A3C1AA\`, permanent \`48473380B913\`, lines 126–136; Theorem 9.10.14 source \`sgpt:EEFC0C9A\`, permanent \`C69D2F0ABA4F\`, lines 140–211; Corollary 9.10.16 lines 216–230. Lines 233–273 (extensions catalogue) only classified as dependency claims, **not** fully certified; user-excluded regularization references not reopened |
| **Whole §11.22** | \`docs/sections/gauduchon-metrics-and-linear-mass--pluriharmonic-currents/index.html\` | \`046c12d159f8aaeff268c57d822253da11ed41ba\` | Lines **7–132**, Lemmas 11.22.1 (permanent \`D9A37BB4C36B\`, 11–36), 11.22.2 (permanent \`25BD2AAB112A\`, 44–60), 11.22.3 (permanent \`40BA141971D9\`, 68–97), **11.22.4** source \`non-kahler-pluripotential-theory:03684AFE\`, permanent \`3CD7629C6061\`, statement 105–109, proof 110–122, disk obstruction 126–132 |
| **Whole §11.23** | \`docs/sections/gauduchon-metrics-and-linear-mass--the-adjoint-measure-of-the-linearization/index.html\` | \`519e50338be6560f6b2856fddce212738f5109bc\` | Lines **7–354**, Proposition 11.23.2 permanent \`0B0003A3A873\`, 24–44; Proposition 11.23.4 permanent \`A914D4D9C6CB\`, 58–69; entropy Proposition 11.23.8 permanent \`AE4D0608184F\`, 126–154; criterion 11.23.12 permanent \`F45FF03B558B\`, 187–218; TV Proposition 11.23.16 permanent \`621E75C5A9F4\`, 297–338 |
| **Repeat reviews, no new coverage** | §3.6 \`docs/sections/separate-harmonicity-and-subharmonicity/index.html\`; §19.11 \`docs/sections/flat-twists-of-adjoint-section-envelopes/index.html\` | \`1d3c9ebe0d7093f0f069dc2b25b0a47f700f907a\`; \`f106e8f79d1a1341045f1e3c41cdeb531b5f699b\` | Already wholly reviewed in earlier audits; current rechecks **not** recorded as newly covered or as new findings |

## POME-PLURIHARMONIC-POSITIVE-LIOUVILLE-FIBER-CRITERION-001

**Severity:** low. **Status:** **verified conditional deduction** relative to Lemma 11.22.4 and its printed positivity/measure-coefficient machinery; neither a false source theorem nor an assertion that all upstream current-theoretic theorems have been independently proved.

**Exact criterion.** Let \(F\) be a connected Riemann surface. Write \(\mathrm{PHL}(F)\) for the property that **every nonnegative harmonic function on \(F\) is constant**. The following are equivalent:

1. \(\mathrm{PHL}(F)\).
2. For every complex manifold \(Y\) of positive dimension \(\ell\), every Hermitian form \(\eta\) on \(Y\), every holomorphic fiber bundle \(\pi:Z\to Y\) with fiber \(F\), and every positive real \((1,1)\)-current \(S\) on \(Z\) with
   \[
      dd^c S=0,\qquad S\wedge\pi^*\eta^\ell=0,
   \]
   there is a **unique** positive real \(dd^c\)-closed \((1,1)\)-current \(R\) on \(Y\) such that \(S=\pi^*R\). If \(S\) is closed, so is \(R\).

Moreover, in (2) it suffices for **necessity** to test the trivial bundle \(\Delta\times F\to\Delta\). Thus the positive-harmonic Liouville property is the exact fiber hypothesis for this universal descent statement. This strictly adds, for example, the fiber \(F=\mathbb C^*\) to the two cases expressly named in the printed lemma.

**Proof of sufficiency.** Work in a local holomorphic trivialization \(U\times F\). The zero vertical trace and positivity make the vertical diagonal coefficient of the Hermitian matrix of coefficient measures vanish; Cauchy–Schwarz for positive matrices makes all mixed coefficients vanish as well. Thus \(S\) has only horizontal coefficients \(s_{\alpha\bar\beta}(w,z)\). From \(dd^cS=0\), each coefficient is harmonic in the vertical variable in the distributional sense. For any horizontal vector \(v\) and nonnegative compactly supported smooth base test function \(\xi\), pair \(\sum_{\alpha,\beta}s_{\alpha\bar\beta}v_\alpha\bar v_\beta\) against \(\xi\) in the base variables. The result is a **nonnegative harmonic distribution** on the entire fiber \(F\); Weyl's lemma makes it a nonnegative harmonic function. By \(\mathrm{PHL}(F)\) it is constant along \(F\). Polarization in \(v\), and linearity in arbitrary base tests, force all \(s_{\alpha\bar\beta}\) to be independent of \(z\). They therefore descend to coefficient distributions of a positive current \(R_U\) on \(U\). Local holomorphic sections make pullback of distributions injective, so \(dd^c R_U=0\), and \(dR_U=0\) if \(dS=0\). Uniqueness glues the \(R_U\) over the base, yielding \(R\). This is precisely the printed proof of §11.22.4 with its **only** special-fiber input replaced by \(\mathrm{PHL}(F)\). It uses neither sequential compactness nor regularization.

**Proof of necessity and sharp obstruction.** If \(\mathrm{PHL}(F)\) fails, take a nonconstant nonnegative harmonic \(h:F\to[0,\infty)\). On \(Z=\Delta_w\times F_z\), with \(\pi(w,z)=w\), put
\[
  S=h(z)\frac{i}{2\pi}\,dw\wedge d\bar w .
\]
It is a smooth positive \((1,1)\)-form, \(dd^cS=0\) because \(h\) is harmonic on the fiber, and \(S\wedge\pi^*\eta=0\) for every Hermitian base form \(\eta\) by horizontal degree. But \(S\) cannot equal \(\pi^*R\) because its horizontal coefficient depends nontrivially on \(z\). Thus even the trivial bundle fails the universal descent property. The disk counterexample printed at §11.22 lines 126–132 is a special instance.

**New example \(F=\mathbb C^*\).** Any nonnegative harmonic \(h\) on \(\mathbb C^*\) pulls back under \(\exp:\mathbb C\to\mathbb C^*\) to a nonnegative harmonic function on \(\mathbb C\). The positive-harmonic Liouville theorem on the plane (from the Harnack inequality on expanding disks, or the classical positive-harmonic Liouville theorem) makes this pullback constant, hence \(h\) is constant. So descent holds for holomorphic \(\mathbb C^*\)-bundles, not only \(\mathbb C\)-bundles and compact-curve bundles.

**Precise boundary, dependent statements, optional correction.** The claim concerns **holomorphic locally trivial bundles with one-dimensional connected fibers**, and **positive** \(dd^c\)-closed \((1,1)\)-currents. It is not a descent claim for arbitrary nonproper fibrations, negative currents, or higher-dimensional fibers. An optional corollary after Lemma 11.22.4 can state the exact \(\mathrm{PHL}(F)\) criterion and \(\mathbb C^*\) example while preserving its source attribution and permanent tag. Applications in §10.10 involving elliptic fibers remain valid, and analogous legitimate \(\mathbb C^*\)-bundle applications become available. No modification to §10.10 is certified here.

## Other mathematical reviews, no new confirmed printed error

**§3.7** (whole mathematical section). The connected-complement rational-resolvent argument establishes polynomial approximation for functions holomorphic near \(K\), and the compact sectors \(K_j\) and points \(a_j\to0\) produce a finite separately subharmonic \(F(z,w)=\sum b_j(z)b_j(w)\) with \(F(0,0)=0\) but \(F(a_j,a_j)\ge j^2\). Its failure is *joint upper semicontinuity*, so it does not contradict §3.6.1, whose joint-majorant hypothesis is deliberately absent. The earlier §3.6 complete audit and its variable-obstacle real-trace finding are **not new**.

**§9.10** (unibranch core). Checked the connected-fiber contradiction using a locally irreducible punctured base, the lift after a finite ramified cover of a holomorphic disk, the maximum principle on compact resolution fibers, and the uniqueness of the usc extension. Corollary 9.10.16 uses connectedness to descend \(\theta\)-psh potentials. The existing Fornæss–Narasimhan disk criterion at §9.10.13 is an **external dependency** (already tracked as **POME-UNI-EXT-FN-001**), not a newly certified theorem or a newly discovered error. Hironaka resolution/principalization remains the allowed external exception. The broad extension-catalogue remarks at lines 233–273 are **not** certified in bulk; any reference there to the excluded regularization programme remains deferred.

**§11.22** (whole). Checked (a) the normal-coordinate measure decomposition of a positive current supported on a smooth divisor with order-zero \(dd^c\); (b) the closed pushforward Kähler test \(\Gamma=F_*(\Omega^{N-p})\) and \(dd^c\)-lemma reduction for the mass inequality; (c) the Kähler Hodge-heat preservation of \(dd^c\)-closedness and correction by \(c\epsilon_t\omega^p\); (d) the vertical-positive-harmonic coefficient reduction in Lemma 11.22.4. Existing Hodge \(dd^c\)-lemma, heat-semigroup and elliptic regularity inputs are used **conditionally** and have not been re-proved as complete transitive chains.

**§11.23** (whole). Checked the normalization \(\int\rho_u\eta^n=1\), Fredholm range and adjoint annihilator, the volume/Gauduchon persistence equivalence, the explicit three-torus nonpersistent Gauduchon metric, the \(n/M\) factor and sign in convex entropy dissipation, the \(p/(p-1)\) coefficient, and the initial-target perturbation recovering \(dd^c\omega^{n-1}\). In the flat-torus total-variation example, the first-order density difference is \(-\pi\epsilon S\); its velocity difference is \(\pi^2\epsilon S(1-KP)+O(\epsilon^2)\), giving \(D'_\epsilon(0)=4\epsilon(K/3-1)+o(\epsilon)\). The connectedness required for the equality case of entropy is supplied by **§1.1 global conventions**; no missing connectedness hypothesis is claimed. These are initial-velocity calculations, not unproved long-time flow existence assertions.

## Classification and exact coverage

- **One** new low-severity verified **conditional deduction**: the sharp positive-harmonic fiber criterion; **zero** newly confirmed false statements or proof errors; **zero** newly certified complete upstream proof chains.
- **Whole current main mathematical sections directly read**: §§**3.7**, **11.22**, **11.23**. **Core review, not whole certification**: §**9.10** through Corollary 9.10.16 and dependency listing afterward. §§3.6 and 19.11 were repeat full readings and create no new whole-section status.
- Actual current generated ToC: **25 chapters / 747 distinct sections**, not 747 theorems certified. Historical first visits remain unreconciled.
- **No builds, tests, CI, formalization, GitHub Actions, main/source/registry/tag/site edits, or publication.** Audit markdown only on the existing review branch; existing closed/merged PR #9 is not reopened or replaced.
