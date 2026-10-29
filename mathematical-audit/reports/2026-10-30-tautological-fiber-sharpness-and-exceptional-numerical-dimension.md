# Mathematical audit — 30 October 2026: a sharp tautological fiber threshold and an exceptional-divisor numerical dimension test

**Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Audit branch:** `review/mathematical-audit` (parent HEAD `bba3ba534a2cb6f3aea42bd3931eaecd19cfaaec` before this checkpoint). This is a selected mathematical review, **not** a certification of any whole section, external theorem, build, or published page.

## Scope, evidence and exclusions

New independent calculations in the *integrated reading edition* of §§10.108.1 and 10.109 (previously only partly reviewed), plus the first substantive selected cross-check of previously inventory-only §24.5. The current chapter/section inventory still comprises **25 chapters and 747 numbered sections**, with **zero sections completely certified**. All existing findings and their resolved/unresolved/candidate statuses remain unchanged.

In accordance with the owner's explicit scope change, this audit **does not examine Demailly approximation or regularization, nor its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss proof-completion programme**. Any cited input falling in those areas remains **deferred-by-user**, *not* resolved or independently certified. The present proofs use explicit algebraic metrics, divisor intersections, and positive-current restrictions, not excluded methods. Hironaka is allowed as an external exception but is not needed in either new calculation.

## POME-TAUT-FIBER-N-OPTIMAL-001

**Status:** low / **verified conditional deduction**; printed Lemma 10.108.1 remains correct. This is a sharpness example, **not a repair or a false theorem**.

**Reading-edition location:** `docs/sections/tautological-metrics-and-maximal-slopes/index.html`, production blob `313098e0ab266ca5696a16775bc5277539dfe889`; Lemma **10.108.1**, source label `C1E90EFE`, permanent tag `C0B465266C15`, physical lines **12–16**, integrated proof lines **20–23**. Its dependent Theorem **10.108.2** has source label `E0E0E4DB` and permanent tag `9CD904E0945C`, lines **28–88**. The existing candidate **POME-TAUT-MODEL-METRIC-EXT-001** regarding a different open-to-compact metric extension remains *unresolved*; this calculation neither revisits nor closes it.

**Precisely tested hypotheses:** let \(r\ge2\), \(m\ge1\), \(\theta=c_1(\mathcal O_{\mathbf P^{r-1}}(1),h_{\rm FS})\), and let \(h\) be a singular metric on \(\mathcal O(1)\) with \(c_1(\mathcal O(1),h)\ge-\epsilon C\theta\) and \(m\epsilon C\le1\). The lemma gives a nonzero section of \(K_{\mathbf P^{r-1}}\otimes\mathcal O(m+N)\otimes\mathcal I(h^m)\) when \(N\ge r+1\).

**Sharpness proof.** Choose a smooth hyperplane \(H=(s_H=0)\) and put
\[
  \lambda=1+\frac1m,\qquad
  h=h_{\rm FS}\exp\!\left(-\lambda\log|s_H|_{h_{\rm FS}}^2\right).
\]
The Poincaré–Lelong identity gives
\[
 c_1(\mathcal O(1),h)
 =\theta+\lambda([H]-\theta)
 =\left(1+\frac1m\right)[H]-\frac1m\theta
 \ \ge -\frac1m\theta .
\]
Thus the curvature hypothesis holds **at the endpoint** \(m\epsilon C=1\), by choosing \(\epsilon C=1/m\). In a chart with \(H=\{z_1=0\}\), the weight of \(h^m\) has polar part \((m+1)\log|z_1|^2\). A local holomorphic monomial \(z_1^\ell\) has integrable squared norm if and only if
\[
  \int_0^1 t^{2\ell-2(m+1)+1}\,dt<\infty
  \quad\Longleftrightarrow\quad \ell\ge m+1.
\]
Consequently
\[
 \mathcal I(h^m)=\mathcal O(-(m+1)H).
\]
With \(K_{\mathbf P^{r-1}}=\mathcal O(-r)\), the exact sheaf in the lemma becomes
\[
 K_{\mathbf P^{r-1}}\otimes\mathcal O(m+N)
       \otimes\mathcal I(h^m)
   \simeq\mathcal O(N-r-1).
\]
Therefore its global sections vanish for **every \(N\le r\)** and are one-dimensional for \(N=r+1\). In particular replacing \(N\ge r+1\) by \(N\ge r\) is generally false, even though the printed lemma is true. This is a sharpness statement for *singular* metrics at the allowed curvature-error endpoint; it says nothing about lowering \(N\) under a strictly stronger curvature or smoothness hypothesis.

**Suggested disposition and affected dependents:** add this explicit hyperplane-pole example as an optional remark after Lemma 10.108.1; retain all tags, original statement, and historical attribution. In Theorem 10.108.2 (especially the relative ample choice around lines 34–46) the fiber nonvanishing condition is an actual dependency. No proof of the full theorem, its extension inputs, or its Nadel-vanishing argument is claimed here.

## POME-NUMDIM-EXCEPTIONAL-POSPRODUCT-001

**Status:** low / **verified conditional deduction** under the printed analytic-current/positive-product convention. This is a numerical test of the **correct** definition, not an error in Lemma 10.109.1 or Theorem 10.109.2.

**Reading-edition location:** `docs/sections/numerical-dimension-and-cotangent-quotients/index.html`, production blob `85538a5ba880030f432282e302a446a230ae15ec`; \(\nu(a)\) and the \(\varepsilon\)-boundary convention, physical lines **8–23**; analytic-current supremum, lines **26–32**. Lemma **10.109.1**, source label `5A937EA0`, permanent tag `636609E49628`, lines **36–49**; Theorem **10.109.2**, source label `71F4321F`, permanent tag `7E716F90C084`, lines **54–69**, considered only as a downstream numerical-dimension user. The source labels of the two linked external-to-this-pass positive-mass/approximation inputs remain unaltered.

**Exact surface model and cohomology.** Let
\[
 X=\operatorname{Bl}_p\mathbf P^2,\quad
 H=\pi^*c_1(\mathcal O_{\mathbf P^2}(1)),\quad
 E=\text{exceptional }(-1)\text{-curve}.
\]
The intersection matrix is
\[
 H^2=1,\qquad H\cdot E=0,\qquad E^2=-1 .
\]
For \(0<d<1\), choose a Kähler form in the class \([\omega]=H-dE\). Then
\[
 E\cdot[\omega]=d>0,\qquad
 [\omega]^2=1-d^2>0,
\]
so the *ordinary* degree-one intersection of the pseudo-effective class \([E]\) with \([\omega]\) is strictly positive.

**Independent analytic-current upper bound.** Fix \(0<\varepsilon<1/d\), and let \(T\in[E]\) be **any** closed real \((1,1)\)-current with \(T\ge-\varepsilon\omega\), in particular any admissible current with analytic singularities in the printed supremum at lines 26–32. Set \(S=T+\varepsilon\omega\ge0\). Its Siu divisorial decomposition along the smooth curve \(E\) is
\[
 S=a[E]+R,\qquad R\ge0,\qquad a=\nu(S,E),
\]
with \(R\) having no generic divisorial component along \(E\). Because \(R\) has local plurisubharmonic potentials not identically \(-\infty\) on \(E\), its restriction \(R|_E\) is a well-defined positive current. Its total mass is nonnegative; in cohomology this reads \(R\cdot E\ge0\). But
\[
 R\cdot E
 =(E+\varepsilon\omega-aE)\cdot E
 =-1+\varepsilon d+a ,
\]
so necessarily
\[
 a\ge 1-\varepsilon d>0 .
\]
The residual positive mass satisfies the *exact universal bound*
\[
 \int_X R\wedge\omega
 =\bigl((1-a)E+\varepsilon[\omega]\bigr)\cdot[\omega]
 =(1-a)d+\varepsilon(1-d^2)
 \le\varepsilon.
\]
Since \(a>0\), the pole set of \(T\) contains \(E\). The ordinary locally bounded product on the complement of that pole set loses its \(a[E]\) term, and positivity gives
\[
 0\le
 \int_{X\setminus\operatorname{Pole}(T)}
       (T+\varepsilon\omega)\wedge\omega
 \le \int_X R\wedge\omega
 \le\varepsilon .
\]
Taking the supremum over **all** eligible analytic-singularity currents and then \(\varepsilon\downarrow0\) yields the claimed degree-one positive-product value
\[
 \langle[E]\rangle\cdot[\omega]=0,\qquad \nu([E])=0,
\]
where the zero-th positive product is positive by convention. This is compatible with, but fundamentally different from, the **ordinary** pairing \(E\cdot\omega=d>0\) and self-intersection \(E^2=-1\). The proof works uniformly for all admissible \(T\) and is not merely a computation with the particular current \([E]\).

**Precisely conditional boundary.** The last step uses *the equivalence asserted at lines 26–32* between the positive mixed-product boundary convention and that analytic-current supremum. The present review independently proves the stated upper bound **within this surface model**, but **does not review or certify** the general simultaneous-approximation argument cited in that paragraph; it remains outside this session and, insofar as it belongs to the excluded regularization programme, **deferred-by-user**. There is no claim of a new proof of the general numerical-dimension definition.

**Suggested disposition and affected dependents:** optional warning/example by the §10.109 definition: **do not replace its non-pluripolar positive intersection by the classical cup product** for non-nef classes. Any numerical-dimension monotonicity, cone duality or cotangent-quotient consequence must retain the printed positive-product convention. Historical attributions and permanent tags are unchanged.

## First direct selected coverage: §24.5, without solving an open problem

**Location:** `docs/sections/problems-in-hermitian-pluripotential-theory--closed-and-twisted-classes/index.html`, main blob `eed47dda4235b5db713fe1c6c6fcea777ee9b674`, section tag `B3F20D9F0DB0`; physical line **10** contains the fixed-error, zero-class mass warning, referencing Proposition 10.15.1 (permanent tag `FCA1263B1141`). Other paragraphs at lines **13–34** were scanned only for the broad dependency map, not theorem proofs.

**Verified local calculation:** if a Hermitian \(\omega\) has an unbounded smooth positive-potential mass family \(\int_X(\omega+dd^cu_j)^n\to\infty\), then at each fixed \(\varepsilon>0\), the smooth closed **exact** currents \(T_j=\varepsilon dd^cu_j\) satisfy \(T_j+\varepsilon\omega\ge0\) and
\[
 \int_X(T_j+\varepsilon\omega)^n
 =\varepsilon^n\int_X(\omega+dd^cu_j)^n\to\infty .
\]
This checks the scaling used in the printed fixed-error warning *conditional on the cited existence of the unbounded family*; that existence is not reproved.

**Contrasting Stokes calculation:** if \(d\omega=0\) the same integral is always \(\varepsilon^n\int_X\omega^n\). On a **compact complex surface** the same equality holds for any *Gauduchon* \(\omega\) with \(dd^c\omega=0\), even when \(d\omega\ne0\), since
\(\int_X\omega\wedge dd^cu=\int_Xu\,dd^c\omega=0\) and \(\int_X(dd^cu)^2=0\). This contrast neither proves any of §24.5's open geometric converses nor certifies its other references. **New coverage only**, not separately entered as a novel error finding.

## Coverage, statuses and repository discipline

- **New full selected computations:** Lemma 10.108.1 fiber threshold, §10.109 exceptional divisor degree-one positive mass; existing larger theorem chains remain conditional.
- **First substantive selected check:** §24.5 line 10 fixed-error identity and the closed/Gauduchon surface comparison, without declaring the section reviewed in full.
- **No new false theorem / no direct editing of mathematical source.** Two new low-severity **verified conditional deductions**; no historical issues were closed. Previous `POME-TAUT-MODEL-METRIC-EXT-001` candidate remains a candidate.
- **Unreviewed or deferred:** the rest of the 747 numbered sections beyond their precisely recorded excerpts, general positive-product equivalence and movable-slope external dependencies, all expressly deferred Demailly approximation/regularization and its Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme.
- **Checks actually done:** read the integrated HTML text at pinned production blob SHAs, independently derive the listed algebra and measure inequalities, compare with existing stable ledger entries, and check the 747-section inventory. **Not done:** project build, Python/JavaScript tests, browser tests, GitHub Actions CI, source/registry/canonicalization/tag edits, main merge, website publication or formal proof verification.
