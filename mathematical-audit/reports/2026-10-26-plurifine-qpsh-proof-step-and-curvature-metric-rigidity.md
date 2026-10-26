# 2026-10-26: a plurifine continuity proof-step error and compact psh-metric rigidity

**Reviewed integrated reading-edition main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting audit branch:** fa67cc496e98284a33f33b40027cc40aa4455255. **Sections newly examined at proof level:** 5.15, 5.19 and the nonexcluded part of 5.20. This is not a mathematical certification of those complete sections or of their transitive prerequisites.

**Scope exclusion:** Demailly approximation/regularization and its dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss completion programme were **not audited**. In particular, Theorem 5.20.16 (the Ohsawa–Takegoshi-type statement) and Proposition 5.20.17 (the Bergman approximation) were skipped, including their proof prerequisites. Their preexisting audit records remain **deferred-by-user**, not resolved.

## POME-PLURIFINE-QPSH-OPEN-STEP-001

**Status:** **confirmed error in a proof step**, with a **verified proposed repair not integrated**. **Severity:** low to medium (the theorem is true, but the inference uses a demonstrably false Euclidean openness property).

**Source:** integrated §5.15, **Proposition 5.15.18**, SGPT source label **sgpt-53418890**, permanent entry tag **E49CF7960E4**. File:

- docs/sections/plurisubharmonic-functions--plurifine-topology/index.html
- Current-main file blob: **855febeeb3846c2e749c80b5381a5a80ca3c6e7b**.
- Statement: physical HTML lines **328–330**. Proof: lines **332–358**; defective phrase **343** and ensuing neighborhood construction **345–355**.
- The statement correctly says that a quasi-plurisubharmonic function on a complex manifold is plurifine-continuous.

**Precise faulty inference.** Locally write the quasi-psh function as \(\varphi=\psi+g\), with \(\psi\) psh and \(g\) smooth. For \(a<b\), its proof sets
\[
U=\{x:a<\varphi(x)<b\}
\]
and, for an arbitrarily fixed \(x\in U\), line 343 asserts that there exists an *open neighborhood \(V\) of \(x\) in \(U\)*. Under the subsection's explicit convention (lines 12–14), unqualified "open" is **Euclidean-open**. Such a \(V\subset U\) need not exist: the Euclidean openness of \(U\) is exactly what cannot be presumed.

**Concrete counterexample to this step, not to the proposition.** Work on the disc \(D=\{z\in\mathbb C:|z|<1/4\}\), put \(a_j=2^{-j}\) for \(j\ge3\), and define
\[
\psi(z)=\sum_{j=3}^{\infty}2^{-j^2}\log|z-a_j|.
\]
Each summand is nonpositive and subharmonic on \(D\), since \(|z-a_j|<3/8<1\). The partial sums decrease and
\[
\psi(0)=-(\log 2)\sum_{j=3}^{\infty}j\,2^{-j^2}>-\infty,
\]
so their limit is a genuine subharmonic (hence psh) function, not identically \(-\infty\). For every \(j\ge3\), \(\psi(a_j)=-\infty\), while \(a_j\to0\). Let
\[
U=\{z:\psi(0)-1<\psi(z)<\psi(0)+1\}.
\]
Then \(0\in U\), but \(U\) contains **no Euclidean-open neighborhood of 0**, since any such neighborhood contains one of the poles \(a_j\). This disproves exactly the line-343 neighborhood step, even for \(g=0\), without refuting the printed plurifine-continuity theorem.

**Complete self-contained repair, not yet applied.** The original argument is repaired by dropping the false requirement \(V\subset U\). For each \(x\in U\), continuity of \(g\) permits a sufficiently small **ambient** Euclidean-open neighborhood \(V\) of \(x\), with
\[
\sup_{y\in V}(a-g(y))<\psi(x)
  <\inf_{y\in V}(b-g(y)).
\]
The set
\[
W=\left\{z\in V:
\sup_{y\in V}(a-g(y))<\psi(z)<
\inf_{y\in V}(b-g(y))\right\}
\]
is **plurifine-open**: the plurifine topology makes \(\psi\) continuous by definition, and Euclidean-open \(V\) is plurifine-open by Proposition 5.15.2. Also \(x\in W\subset U\). Varying \(x\) proves the desired plurifine openness of \(U\). For the pole value, addition of a finite continuous function to an extended-real-valued psh function is continuous in the order topology, so the proof covers \(-\infty\) as well; alternatively the original initial reduction to the nonpole locus can be retained.

In fact, an even shorter repair is available: locally \(\psi\) is plurifine-continuous by the *definition* of that topology; \(g\) is Euclidean-continuous and hence plurifine-continuous; their extended-real sum \(\psi+g\) is plurifine-continuous. No smoothing, approximation, or external analytic input is needed.

**Related integrated dependencies and consequences:** Proposition 5.15.2 (tag **0E4FD8AF1256**, lines 22–38), the shared Definition 5.47.14 (tag **09A00D4B8096**, referred to at 5.15.1, lines 7–12), Corollary 5.15.19 (tag **030D740FC9C6**, lines 360–380) and Corollary 5.15.21 (tag **31032260EF62**, lines 401–420) use plurifine continuity for comparison or quasi-extrema. The theorem **remains true**, so these dependents are not shown false; a clean local replacement of the proof would close this proof-step defect. No integrated source, permanent tag, or proof registry was changed.

## POME-PSH-METRIC-CURVATURE-RIGIDITY-001

**Status:** **verified conditional deduction** (optional corollary, **not** an existing false theorem); **severity:** low.

**Sources:** §5.20, Definition 5.20.3 (source **sgpt-41CAE7BB**, permanent tag **293669D813B8**, lines **47–67**), Definition 5.20.8 (source **sgpt-E8691D70**, permanent tag **A43467D63B4A**, lines **112–131**) and the local Chern-potential formula (lines **63–66**), in:

- docs/sections/plurisubharmonic-functions--plurisubharmonic-metrics-on-line-bundles/index.html
- Current-main file blob: **0fd91c7a6a8228fef2ac1328a80f40c4609b5e0f**.

Definition 5.19.2 (tag **AE4F30A1999E**, lines 19–22), Remark 5.19.5 (source **sgpt-8E42F9ED**, tag **877B9D0BDD26**, lines 47–54), and the fixed-current local-potential theory in §5.4 (Theorem 5.4.3, tag **2408CCC1B5A0**) supply comparison context; the §5.19 file blob is **b197a4fa4c063c10f1a65cde5b09a34dddc8df86**.

**Sharp proposition.** Let \(X\) be a **compact connected Kähler manifold** and \(L\) a holomorphic line bundle. Let \(h_1,h_2\) be genuine psh metrics on \(L\) in the sense of Definition 5.20.8 (their local weights are not identically \(-\infty\)). If
\[
c_1(L,h_1)=c_1(L,h_2)
\quad\text{as currents},
\]
then there is a **single positive constant** \(c\) such that
\[
h_1=c\,h_2
\]
**pointwise on every fiber**, including the singular fibers. Conversely positive constant rescaling preserves the Chern current.

**Proof.** Choose one smooth reference metric \(h_0\) on \(L\) and write \(h_i=h_0e^{-\varphi_i}\), where \(\varphi_i\) is a globally defined \(\theta\)-psh potential and \(\theta=c_1(L,h_0)\). Equality of Chern currents implies
\[
dd^c(\varphi_1-\varphi_2)=0
\]
as distributions. Since quasi-psh functions are locally \(L^1\), the difference is a well-defined distribution. In each holomorphic coordinate chart the distributional \(\partial\bar\partial\)-Hessian vanishes; taking its flat trace gives \(\Delta(\varphi_1-\varphi_2)=0\). By the Weyl lemma, the difference has a **smooth real-valued harmonic representative**, and the original distributional equation makes it pluriharmonic. Its local representatives glue, because they agree almost everywhere on overlaps. A smooth pluriharmonic function on a compact connected complex manifold is constant (take the Kähler-metric trace and apply the maximum principle). Thus \(\varphi_1-\varphi_2=C\) almost everywhere, for some real constant \(C\).

A psh function is its canonical upper-semicontinuous representative of its local \(L^1\)-class. Applied in local frames, this uniqueness promotes \(\varphi_1=\varphi_2+C\) to **pointwise** equality, including polar points. Hence \(h_1=e^{-C}h_2\) fiberwise; at singular fibers multiplication by a finite positive constant preserves the prescribed singular form. The converse follows immediately from the local Chern formula.

**Necessity of compactness for a *constant* ratio:** on \(X=\mathbb C\) with \(L\) trivial, the smooth psh metrics \(h_1=1\) and \(h_2=e^{-\operatorname{Re}z}\) have the same zero Chern current, but their ratio is nonconstant. In the noncompact case the correct local statement is a ratio \(e^{-H}\), where \(H\) is smooth real pluriharmonic. Connectedness rules out independent constants on different components.

**Proof dependencies and status boundary.** This derivation uses the internal local-current calculus, Weyl's lemma, the psh canonical-representative uniqueness and compact maximum principle. These are cited as *conditional inputs*, not re-certified transitively. Proposed as an optional uniqueness corollary near Definition 5.20.8; it is distinct from the previously recorded fixed-flat-chart **same-trace** current finding POME-TRACE-POTENTIAL-RIGIDITY-001 (here one requires *equal whole Chern currents*, not merely equal Euclidean trace, and obtains a global metric-ratio conclusion). It can clarify normalized line-bundle psh metrics and comparison of singularity types in subsequent envelope and model sections.

## Other direct checks (no distinct new error)

- **§5.15:** Proposition 5.15.6 (Bedford–Taylor global thinness barrier), tag **80A580DBD009**, lines **81–180**: the logarithmic collar maximum, the decreasing psh sum, the finite value at the distinguished point and the local boundedness away from it were individually inspected; its source normalization \(\sum 2^{-j}\) and the role of the radii \(\delta_j,\gamma_j\) were checked. Lemma 5.15.9 (tag **D3F2BF3D82BD**, lines **182–204**), Theorem 5.15.10 (tag **458C93F5F6CD**, lines **206–247**), Theorem 5.15.11 (tag **4388B85DDD67**, lines **249–274**), Corollary 5.15.15 (tag **C94ADCA6E19D**, lines **286–304**) and Corollary 5.15.16 (tag **DF37542BAB03**, lines **306–322**) received selected assumption/proof checks. No wholesale certification.
- **§5.19:** Definitions 5.19.1–6 and 5.19.8–17 received selected statement, positivity, current-versus-weight and normalization checks; in particular Remark 5.19.5 (tag **877B9D0BDD26**) compares global singularity-type quotients, not equality of individual currents. Several deeper divisorial-cohomological theorems and their upstream inputs remain unchecked.
- **§5.20:** Nonexcluded Definitions 5.20.1–15, Proposition 5.20.4 (Lelong–Poincaré, tag **0C02CD3B5D59**, lines **70–80**), Example 5.20.6 (Fubini–Study normalization, lines **81–109**) and Example 5.20.20 (nonconvex Kiselman fibers, lines **287–325**) were checked at the displayed formula/proof level. **No** review of §5.20.16–17 or their dedicated analytic prerequisites; these remain **deferred-by-user**.

## Coverage, remedies and verification limits

The three prior **inventory-only** section rows **5.15, 5.19, 5.20** were updated to *selected* proof-level or supporting checks. All previous inventory rows and findings are retained; no theorem chain or entire section is certified. One newly confirmed **proof-step** error and one separate conditional consequence are recorded with stable IDs, precise anchor paths/tags, counterexample/complete proof, affected dependents and proposed edits. This audit submits **notes only**; source changes would require a separately reviewable patch, not an edit here. There was no project test suite, site build, CI, mathematical formalization or publication. The author-excluded Demailly programme remains **deferred-by-user** in its existing record, neither reopened, repaired nor certified.
