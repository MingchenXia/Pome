# Mathematical audit: pluriclosed surface mass, a continuum of ideal-equivalent polar types, and nonreversibility of mixed Monge–Ampère bounds

**Date:** 2026-10-27. **Pinned reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Review branch:** review/mathematical-audit. **Classification:** three low-severity, verified conditional deductions. None is a confirmed false theorem, a proof completion of the author's excluded regularization programme, or a certificate for the upstream results.

## Scope and source identification

The *actual integrated main reading edition*, not the contributing source repository, was inspected at the following immutable main blobs and physical HTML lines:

1. §12.1, *A Gauduchon variational volume*, source variant non-kahler-pluripotential-theory:538AA05F, permanent section tag 881C26425D7A, docs/sections/a-gauduchon-variational-volume/index.html, blob 408aced882e04bc8578f9ab6f68bdc2c1aa1d7fa, lines 5–20 (especially 8 and 11). §12.1 contains explanatory material, not a numbered theorem proof. Its compactness, positivity, background and normalization conventions were compared against selected §§12.2–12.3 results already recorded in the historical audit.
2. §13.4, *Bounded factors and the first-degree product*, docs/sections/non-pluripolar-products--bounded-factors-and-the-first-degree-product/index.html, blob d234ab96e33bfd24ad1d53d29332b2c021cddeff. Directly read Lemma 13.4.1, source foundations-of-pluripotential-theory:920E6561 (lines 11–68); Lemma 13.4.2, permanent 5D93FCFBA57F (73–94); Proposition 13.4.3, permanent 90E0E28D9A95 (99–126); first-degree Proposition 13.4.7, source D1BF7EF2, permanent 3553558C2E27 (195–250); Proposition 13.4.10, source A7D5A0E9, permanent FB5ACFB46DB8 (255–282); and Example 13.4.11, source E3C53B02, permanent E9D7DF5798B0 (287–295). The one-variable potential and polar-measure existence cited there remain explicitly conditional internal inputs.
3. §13.5, *Global finiteness and bounded cohomological mass*, docs/sections/non-pluripolar-products--global-finiteness-and-bounded-cohomological-mass/index.html, blob 943517743538820940559eae8469ce98ecf5fcd5. Directly read Proposition 13.5.1 (11–27), Lemma 13.5.2 (32–80), Theorem 13.5.4, permanent 3783DE0B4D00 (85–123), Proposition 13.5.8, source foundations-of-pluripotential-theory:13A73596, permanent A93A2F4C95C2 (133–175); Corollary 13.5.10, permanent 7FDDF6925B80 (180–195), and Corollary 13.5.11, permanent 43C93EF28279 (200–216). The general bounded Bedford–Taylor density inequality is an internal input, not newly certified here.
4. §16.7, *Comparison of singularities*, docs/sections/comparison-of-singularities/index.html, blob 65883f4ebc5ac5e3612212dceda85467eeb84d7b, definition 16.7.1, source sgpt:410CBDE6, permanent 3E4D57445698 (5–19). This was a *first selected definition/convention comparison*, not a theorem-proof certification. Compared §§16.8.2 (P-preorder, source D4B3E008, permanent 4E959BD934C4, lines 15–24), 16.8.10 (ideal preorder, source 534FD2DC, permanent 5C5512F45CC2, line 238), and **preexisting** Example 16.8.19 (source 65A23FEC, permanent 325A49CBCF74, 401–403) in docs/sections/comparison-of-singularities--the-p-and-mathcal-i-preorders/index.html, blob 99e301ceb84460dc9bfeff03280d517dc8890ea5. Compared P-envelope mass preservation, §16.3.9, permanent E58386609911, docs/sections/the-envelope-operators--p-envelopes--rooftop-operator-and-the-definition-of-the-p-envelope/index.html, blob 97681f31628eb362950837daaadde67d10507a2f (135–141).

All statements below are limited to their exact displayed hypotheses. In particular, none invokes Demailly approximation, its Bergman/L2/Ohsawa–Takegoshi/multiscale machinery, or any positivity-loss proof.

## Finding POME-GAUD-SURFACE-MASS-PLURICLOSED-001

**Severity/status:** low / **verified conditional deduction**. **Affected dependents:** §12.1 introductory observation about potential-dependent normalization for nonclosed backgrounds; §12.2.3 smooth Gauduchon equation normalization; Hermitian mass-conservation discussions. **Suggested change:** optional precise two-dimensional qualification after §12.1, not alteration of the valid general observation.

**Hypotheses.** Let \(X\) be a compact complex surface without boundary, and let \(\theta\) be a smooth real (1,1)-form. No assumption of \(d\theta=0\) is needed.

**Exact identity.** For every smooth real \(v\),
\[
  \int_X(\theta+dd^cv)^2
  =\int_X\theta^2+2\int_X v\,dd^c\theta.
  \tag{A}
\]
Indeed, \(dd^cv\) is \(d\)-closed, and \((dd^cv)^2=dd^c(v\,dd^cv)\). Its integral vanishes by Stokes. Applying Stokes twice to \(\theta\wedge dd^cv\) gives \(\int_X\theta\wedge dd^cv=\int_Xv\,dd^c\theta\). Neither integration by parts assumes \(d\theta=0\). The convention is Pome's \(dd^c=\frac{i}{2\pi}\partial\bar\partial\).

**Exact iff assertion.** Suppose additionally \(\theta>0\) is Hermitian. Then the total mass is independent of **all admissible smooth potentials** \(v\), \(\theta+dd^cv>0\), if and only if \(dd^c\theta=0\). Sufficiency is (A). For necessity, fix any real smooth test \(h\). Since \(\theta>0\), \(\theta+t\,dd^ch>0\) for all sufficiently small positive and negative \(t\). Constancy forces the coefficient \(2\int_Xh\,dd^c\theta\) to vanish. Arbitrary \(h\) forces \(dd^c\theta=0\) as a current, hence as a smooth form. Consequently in the smooth Monge–Ampère equation \((\theta+dd^cu)^2=c\mu\) with \(\int_X\mu=1\), a pluriclosed \(\theta\) forces \(c=\int_X\theta^2\), even if \(\theta\) is **not closed**.

**Nonclosed example, no external existence theorem.** Let \(X=(\mathbb C/(\mathbb Z+i\mathbb Z))^2\), \(\omega_0=\frac{i}{2}\sum_{j=1}^2dz_j\wedge d\bar z_j\), \(f(z_1)=\cos(2\pi\operatorname{Re}z_1)\) and \(\beta=f\,d\bar z_2\). Put
\[
  \eta=\partial\beta+\overline{\partial\beta},\qquad
  \theta_\varepsilon=\omega_0+\varepsilon\eta.
\]
The form \(\eta\) is real of type (1,1). It satisfies \(\partial\bar\partial\eta=0\) because each term is respectively \(\partial\)-exact or \(\bar\partial\)-exact. Yet \(\bar\partial\partial\beta=(\partial_{z_1}\partial_{\bar z_1}f)\,d\bar z_1\wedge dz_1\wedge d\bar z_2\ne0\) on an open set, so \(d\eta\ne0\). For sufficiently small nonzero real \(\varepsilon\), compactness guarantees \(\theta_\varepsilon>0\). Thus this is an explicit *nonclosed* Hermitian background with invariant Monge–Ampère total mass.

**Boundary:** This is a surface-specific iff; no analogous unrestricted equivalence is claimed for \(n\ge3\). The original chapter correctly says mass *can* vary on a nonclosed background, not that it always does. No original theorem is false.

## Finding POME-POLAR-I-TYPE-MASS-CONTINUUM-001

**Severity/status:** low / **verified conditional deduction**. **Affected dependents:** §§13.4.10–11 and 16.7–16.8 comparison of singularity notions, and warnings about determining non-pluripolar mass from multiplier ideals. **Suggested change:** optional quantitative family following existing Example 16.8.19; retain that example and its historical attribution. This is an extension, **not a newly discovered pairwise counterexample**.

**Input and hypotheses.** Use exactly the atom-free probability measure \(\mu\) carried by a compact polar \(K\subset\mathbb C\subset\mathbb P^1\) and its nonpositive \(\omega_{\rm FS}\)-psh potential \(q\) from §§13.4.10–11:
\[
  \omega_{\rm FS}+dd^cq=\mu,\quad q=-\infty \ \text{on }K,
  \quad\nu(q,x)=0\ \text{for all }x.
\]
Set \(q_t=tq\), \(0\le t\le1\), with \(q_0=0\). (Any additive normalization of the \(q_t\) is harmless.)

**Exact non-pluripolar masses.** The positive current
\[
 T_t=\omega_{\rm FS}+dd^cq_t=(1-t)\omega_{\rm FS}+t\mu
\]
has ordinary cohomological mass 1, while the degree-one non-pluripolar restriction formula §13.4.7 gives
\[
  \langle T_t\rangle=(1-t)\omega_{\rm FS},
  \qquad
  \int_{\mathbb P^1}\langle T_t\rangle=1-t.
  \tag{B}
\]
For \(t>0\), the polar set of \(q_t\) contains \(K\), hence kills the \(t\mu\) summand; it carries no smooth Fubini–Study mass. For \(t=0\), the formula is immediate. Other poles of \(q\), if any, are also polar and thus invisible to \(\omega_{\rm FS}\). This proves *every* non-pluripolar mass in the interval \([0,1]\) occurs within this one family.

**The three levels of singularity comparison.** All Lelong numbers of \(q_t\) are zero. By the one-dimensional exponential-integrability implication already used in §13.4.11, \(\mathcal I(sq_t)=\mathcal O_{\mathbb P^1}\) for every \(s>0\), so all \(q_t\) have the **same I-type**. For \(t>s\), \(q_t\preceq q_s\) since \(q\le0\), but \(q_s\not\preceq q_t\) because \((s-t)q\) is unbounded above near \(K\); hence their **ordinary singularity types** differ. To compare P-types without relying on a zero-mass definition at \(t=1\), fix any \(\delta>0\) and the larger Kähler background \(\theta=(1+\delta)\omega_{\rm FS}\). Then every \(q_t\) is \(\theta\)-psh of *positive* non-pluripolar mass
\[
 \int_{\mathbb P^1}\langle\theta+dd^cq_t\rangle=1+\delta-t>0.
 \tag{C}
\]
If \(q_s\sim_P q_t\), their common \(\theta\)-P-envelope would have the same mass as both inputs by §16.3.9, contradicting (C) for \(s\ne t\). Thus the family contains continuum-many pairwise P-inequivalent ordinary types inside one I-equivalence class, even though all non-pluripolar masses are explicitly computable.

**Boundary:** The preexisting §16.8.19 already distinguishes P and I at the two extremal types. This entry registers only the entire continuous mass spectrum, strict ordering, and positive-mass background treatment, not the old endpoint example as new. Existence of \(\mu\), degree-one restriction and mass preservation are recorded conditional internal dependencies; no multiplier-ideal regularization argument is used.

## Finding POME-MIXED-MA-NONREVERSE-KAHLER-001

**Severity/status:** low / **verified conditional deduction**. **Affected dependents:** Proposition 13.5.8 and Corollaries 13.5.10–11, in particular the directional nature and coefficient of the geometric-mean mixed-density lower bound. **Suggested change:** optional sharpness/nonconverse remark following Proposition 13.5.8; no correction to its true assertion.

**Hypotheses.** Fix \(n\ge2\) and let \(X=(\mathbb P^1)^n\). Write \(\omega_j\) for the pullback of the unit-mass Fubini–Study form by the \(j\)-th projection, \(\Omega=\sum_j\omega_j\), and \(\nu=\omega_1\wedge\cdots\wedge\omega_n\), a probability measure.

For every \(\varepsilon>0\), all
\[
 T_{i,\varepsilon}=\omega_i+\varepsilon\Omega,\qquad i=1,\ldots,n,
\]
are smooth **Kähler forms**. Since \(\omega_j^2=0\),
\[
 T_{i,\varepsilon}^{\,n}
 =n!(1+\varepsilon)\varepsilon^{\,n-1}\nu.
 \tag{D}
\]
But direct multilinear expansion yields
\[
 T_{1,\varepsilon}\wedge\cdots\wedge T_{n,\varepsilon}
 =\left[\sum_{k=0}^n\binom nk k!\,\varepsilon^k\right]\nu.
 \tag{E}
\]
Indeed, choose \(k\) factors from which to take \(\varepsilon\Omega\). The remaining \(n-k\) factors prescribe distinct \(\omega_j\), and the selected \(\Omega^k\) contributes exactly \(k!\) times the wedge of the \(k\) complementary factors. Thus the ratio of the mixed-density coefficient to the geometric mean of the pure top-degree coefficients is
\[
 \frac{\sum_{k=0}^n\binom nk k!\varepsilon^k}
 {n!(1+\varepsilon)\varepsilon^{\,n-1}}
 \longrightarrow+\infty\quad(\varepsilon\downarrow0).
 \tag{F}
\]
For smooth forms the non-pluripolar products are simply the ordinary products, so (D)–(F) show that **no dimension-only reverse inequality** of the form
\(\langle T_1\wedge\cdots\wedge T_n\rangle
 \le C_n(\prod f_i^{1/n})\nu\)
holds when \(f_i\) are the *exact* densities of their pure top-degree products, even in the smooth Kähler setting. At \(\varepsilon=0\), each \(T_i^n=0\) while the mixed product is \(\nu\), but the stronger counterexample uses strictly positive \(\varepsilon\).

Conversely, the **coefficient 1 of the valid lower inequality is optimal**: for any Kähler form \(\Omega\), let \(T_i=\lambda_i\Omega\), \(\lambda_i>0\), and \(\nu=\Omega^n\). Then \(f_i=\lambda_i^n\) and equality holds:
\[
 T_1\wedge\cdots\wedge T_n
 =\Bigl(\prod_i f_i^{1/n}\Bigr)\nu.
\]
Therefore the internal mixed determinant result is genuinely one-sided, with optimal coefficient. This does not claim a reverse inequality under additional uniform ellipticity bounds (which may depend on those bounds).

**Boundary:** The finite permanent identity in (E) was additionally checked by a standalone elementary permutation calculation for \(n=2,3,4,5\) at \(\varepsilon=0,0.1,0.5\). This is *not* a build, CI run, formal verification, or a proof of the earlier general Bedford–Taylor comparison theorem. No source statement was found false.

## Exact scope, outstanding work and disposition

- New direct selected proof-level review: §§13.4 and 13.5 (the specific theorem and lemma ranges above), previously only contextual/dependency entries. First substantive **introductory/convention** review of §§12.1 and 16.7, which contain no separately proved new theorem at the quoted passages. §§16.3/16.8 were previously reviewed and only cross-checked as dependencies here; no duplicate coverage or finding registration.
- Actual collection size remains the same **747 unique section identifiers** from the established ToC matrix; neither these four rows nor their dependencies are certified in full. No exhaustive review is asserted.
- Verified three new conditional deductions and **zero newly established false printed theorems**. The earlier Example 16.8.19 is preserved, not marked as new or erroneous. No historical unresolved/resolved/deferred item is converted to another status.
- The author's excluded Demailly approximation/regularization and dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme were not consulted or worked on. The corresponding historical ledger remains **deferred-by-user**, neither resolved nor certified. The valid polar-mass argument here uses the *existing public reading edition* of ordinary potential theory.
- This audit does not update main, underlying source texts, manuscript registries, canonicalization, permanent tags, published docs, or any GitHub Actions or website deployment. Only review-branch Markdown records are proposed here.
