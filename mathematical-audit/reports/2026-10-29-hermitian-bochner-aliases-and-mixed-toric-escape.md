# Audit report — mixed real Monge–Ampère mass escape and a historical Hermitian-Bochner recheck

**Date:** 2026-10-29. **Pinned production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Audit branch:** review/mathematical-audit. **Scope:** an **incremental mathematical calculation** in the previously visited §21.5.1–4, plus a recheck of already-audited §11.48 defects and contextual selected §11.5.1/.3/.4 Stokes/AGM identities. The Hermitian equation-alias and double-prime defects were **already recorded on 2026-10-25**; they are not counted as new findings or new coverage here. This is not a full-section certification. No Demailly approximation, regularization, Bergman, L², Ohsawa–Takegoshi, multiscale or positivity-loss proof programme was reopened: all are **deferred-by-user**.

## Integrated reading-edition anchors

1. **Hermitian Bochner §11.48:** production path **docs/sections/hermitian-torsion-and-the-bochner-identity/index.html**, blob **4656b430de6ec989ef121eca550afda0be407222** (257 physical HTML lines). Source book **demailly-complex-geometry**, used here only for *Hermitian Bochner calculus*, not the excluded approximation programme. Theorem 11.48.3 original source label **7F72B02B**, permanent tag **9C30D850C771**, line 24; its displayed Eq. 11.48.5 is on **line 27** and contains a malformed double prime. Theorem 11.48.15 original label **72367915**, tag **E96E372480D4**, line 155; Eq. 11.48.18 is on **line 162** and has another malformed double prime. The formula-alias reading chunks at **lines 247–248** separately reproduce malformed equations 11.48.5, .11, .12, .17 and .18 as nested display environments. The original labels/permanent equation tags are, respectively: **7260AD37 / 1E5D7A00D2DA**, **B4C8D316 / CE84427B9DD6**, **E94D683F / 727926BD3A70**, **B4698684 / 5FE7DC3167AF**, **BC7541CC / CC4EDB6E65CB**. Independently inspected production standalone pages: **docs/tag/1E5D7A00D2DA/index.html** (blob **983b4838ab7ba053d6c92d77000d43a763b4ba8c**), **docs/tag/CE84427B9DD6/index.html** (blob **5a22e530414c6303dbc8d7ed77794ed8b0a66f2b**), **docs/tag/727926BD3A70/index.html** (blob **95596acf78cbb756eb101acf0e52a564a40eaf2a**), **docs/tag/5FE7DC3167AF/index.html** (blob **a8a9f3099376487adb7a7f935817d7cb64034b93**), **docs/tag/CC4EDB6E65CB/index.html** (blob **cdf89845b6e94b267d1e7a456661ed8551655fc9**).
2. **Real toric Monge–Ampère §21.5:** production **docs/sections/convex-analysis-and-toric-potentials--the-real-monge-ampere-measure/index.html**, blob **7089aa41ae2422b1bd6b5094e46668cbc8ed37be** (170 HTML lines). Theorem 21.5.1 source **foundations-of-pluripotential-theory:4A0FAEB3**, tag **409656CC47D4**, lines 11–42 (Alexandrov subgradient-volume measure). Theorem 21.5.2 source **6403CF44**, tag **F4072D9ED060**, lines 44–85 (vague continuity). Example 21.5.3 source **87E8B742**, tag **6BCC82ADB7C7**, lines 90–97 (the one-dimensional mass-escape example). Proposition 21.5.4 source **EAD83A50**, tag **5D8A7A7D734E**, lines 99–158, and polarization Eq. 21.5.5 original label **24CC29A7**, permanent tag **D38381F0AC43**, lines 143–148.
3. **Gauduchon trace context §11.5:** **docs/sections/gauduchon-metrics-and-linear-mass--conservation-of-the-trace-mass/index.html**, blob **34af83ff391b5e5590cd9cb10ca4cd2b3faff02c**; Proposition 11.5.1 tag **828FAD1A35BF**, Corollary 11.5.3 tag **A9609E0AE7B9**, Proposition 11.5.4 tag **BFC1330527CA**. Its selected distributional Stokes and pointwise arithmetic–geometric-mean steps were checked separately and found consistent; no complete dependency certification is implied.

## Historical recheck only — POME-HERM-BOCHNER-EQUATION-ALIASES-001 and POME-HERM-BOCHNER-DOUBLEPRIME-001 (both previously logged)

**Previously recorded statuses (unchanged):** **POME-HERM-BOCHNER-EQUATION-ALIASES-001** — medium / confirmed integration error; **POME-HERM-BOCHNER-DOUBLEPRIME-001** — low / confirmed glyph error. Both were fully identified in the existing [2026-10-25 report](2026-10-25-hermitian-affine-background-scaling-and-bochner-equation-aliases.md). **No new error or repair is claimed from this recheck.** These are not false mathematical theorems and remain open/unrepaired in production.

**Previously documented exact defects, rechecked without new status.** In the original *continuous* section HTML the second contraction identity in Eq. 11.48.5 reads
\[
[\Lambda,D']=\mathrm i(\delta\,\text{”}+\bar\tau^*),
\]
where the literal U+201D quotation mark has replaced the required **two prime marks** of \(\delta''\). Equation 11.48.18 similarly ends with \(\Delta\,\text{”}\) instead of \(\Delta''\). The first identity in Eq. 11.48.5 contains the correct \(\delta'\), and Eqs. 11.48.16–17 print the correct \(\Delta''\); consequently the two malformed strings cannot denote an intentional additional operator. The same literal errors persist on their independently checked permanent-tag pages.

There is also a separate **invalid display-environment composition** on each of the five named permanent equation pages: they print \(\backslash[\backslash\mathrm{begin}\{aligned\}\backslash\mathrm{begin}\{align\}\ldots\backslash\mathrm{end}\{align\}\backslash\mathrm{end}\{aligned\}\backslash]\). An align environment cannot be nested in an aligned environment inside display math. The continuous chapter appends those alias fragments after the main, otherwise complete source block, so the affected lines are duplicated as invalid formula blocks. The historical §11.48 report **already listed these exact five aliases and both U+201D corruptions**. The also-previously-recorded **POME-GAUD-SECONDVAR-EQ-ALIAS-NESTED-001** concerns a separate §12.4 occurrence of the same alias-container defect. Do not create repeated findings, issues, or PRs.

**Mathematical verification of the intended operator symbols (conditional on the printed graded identities).** The uncorrupted first contraction/wedge formulas give
\[
[\Lambda,D']=\mathrm i(\delta''+\bar\tau^*).
\]
Indeed it is the formal adjoint of \([\delta',L]=-\mathrm i(D''+\bar\tau)\), accounting for \(\Lambda=L^*\). It is not a new theorem or a repair of unrelated proofs. The mixed commutators established in Eq. 11.48.11 and their adjoints give \([D'+\tau,\delta'']=0=[D'',\delta'+\tau^*]\). Expanding the definition
\[
\Delta_\tau=[D'+D''+\tau,\,\delta'+\delta''+\tau^*]
\]
therefore yields precisely \(\Delta_\tau=\Delta'_\tau+\Delta''\), the intended Eq. 11.48.18.

As an independent **non-Kähler sign/normalization spot check**, on a coordinate ball set \(\omega=e^\varphi\omega_0\), \(\omega_0=\mathrm i\sum dz_j\wedge d\bar z_j\). Then \(a=\partial\varphi\wedge\omega\) and
\[
\tau(1)=\Lambda(\partial\varphi\wedge\omega)=(n-1)\partial\varphi.
\]
By integrating the \(\bar\partial\)-adjoint against a compactly supported \((1,0)\)-form, using \(\omega^n=e^{n\varphi}\omega_0^n\), one obtains
\[
\delta''(f\omega)=\mathrm i\bigl(\partial f+(n-1)f\partial\varphi\bigr),
\]
which matches Eq. 11.48.4 on functions and fixes the plus sign of the torsion term. This checks only this model and the algebraic symbol corrections, **not** the full Bochner–Kodaira proof or its analytic vanishing corollaries.

**Unchanged proposed correction and dependents, summarized for context only.** Restore the literal \(\delta''\) and \(\Delta''\) strings in the published reading-body formulas (and inspect the guarded upstream proof/export source before assigning the origin of the character substitution). For the five permanent equation aliases, emit one valid display environment rather than wrapping an existing align in aligned/display math; preserve all original source labels, permanent tags, statement/equation numbers, cross-references, distinct parent formulas, and historical attribution. Regenerate the complete and alias HTML in a **separate, reviewed source/rendering PR** with actual MathJax/browser verification before any publication. Affected: §11.48.3/.15, Eqs. 11.48.5/.11/.12/.17/.18, subsequent energy formula 11.48.19 and vanishing corollaries 11.48.20–21 **as reader-facing dependents**, not as mathematically disproved results. No source, registry, HTML, tags, or site was changed here.

## POME-TORIC-MIXED-ESCAPE-001

**Severity:** low. **Status:** **verified conditional deduction** from the explicit Alexandrov measure and polarization formulas in §21.5; **no printed theorem is false**. This extends the printed one-variable Example 21.5.3 to all dimensions and shows loss of narrow continuity with **all but one mixed-MA argument fixed**.

**Exact calculation.** Fix \(n\ge2\), positive \(a_1,\ldots,a_n\), and real \(c_1,\ldots,c_n\). In lattice coordinates \(x=(x_1,\ldots,x_n)\) put
\[
F_i(x)=a_i(x_i-c_i)_+,\qquad (t)_+=\max(0,t).
\]
These are finite convex functions. For each subset \(J\subset\{1,\ldots,n\}\), the subgradient of \(F_J=\sum_{i\in J}F_i\) is contained in the coordinate box \(\prod_{i\in J}[0,a_i]e_i\), so if \(J\ne\{1,\ldots,n\}\), its \(n\)-dimensional slope volume is zero on *every* Borel set and \(\operatorname{MA}_{\mathbb R}(F_J)=0\).

For the full sum \(F=\sum_iF_i\), each coordinate subgradient is \([0,a_i]\) at \(x_i=c_i\) and a singleton elsewhere. Consequently the full-dimensional slope image appears only at \(c=(c_1,\ldots,c_n)\), where it is the whole box \(\prod_i[0,a_i]\); the Alexandrov measure is
\[
\operatorname{MA}_{\mathbb R}(F)=n!\left(\prod_{i=1}^na_i\right)\delta_c.
\]
There is no missing face measure, because all lower-dimensional boxes have zero \(n\)-dimensional Lebesgue volume. Equation 21.5.5 (polarization) then gives the **exact mixed measure**
\[
\boxed{\operatorname{MA}_{\mathbb R}(F_1,\ldots,F_n)
=\left(\prod_{i=1}^na_i\right)\delta_c.}
\]
This independently checks the printed \(1/n!\) polarization factor against the \(n!\)-normalized diagonal measure.

**Escaping a single argument.** Fix \(c_i=0\) for \(i<n\), and write \(F_{n,j}(x)=a_n(x_n-j)_+\) with \(j\to+\infty\). The first \(n-1\) factors are independent of \(j\); the final factor tends to \(0\) locally uniformly. Yet
\[
\operatorname{MA}_{\mathbb R}(F_1,\ldots,F_{n-1},F_{n,j})
=\left(\prod_{i=1}^na_i\right)\delta_{(0,\ldots,0,j)}
\rightharpoonup0
=\operatorname{MA}_{\mathbb R}(F_1,\ldots,F_{n-1},0).
\]
The total mass stays \(\prod_i a_i>0\), so convergence **fails against the bounded continuous function 1**. This violates no continuity claim: Proposition 21.5.4 demands only **vague** convergence, and its polarization proof handles exactly this situation. Unlike the original one-dimensional example, this example treats the genuinely mixed \(n\)-linear operator and freezes \(n-1\) arguments.

**Suggested optional addition/dependents.** Add a cross-dimensional mixed example after §21.5.3, or use this as a test of an eventual strengthened theorem involving total mass/tightness. Do **not** replace vague convergence by narrow convergence without controlling escape of mixed mass. Relevant: §21.5.1–4, Eq. 21.5.5, and later toric/convex mixed-volume applications. No canonicalization, permanent-tag or source change is warranted.

## Coverage and limitations

**Actual new mathematics:** the polyhedral mixed real-MA computation and escaping-one-argument family in the **previously partly reviewed** §21.5.1–4 with Eq. .5. **Rechecks only (no new coverage credit):** the two previously logged Hermitian §11.48 formula errors, their five permalink aliases, and the already available torsion identities. §11.5.1/.3/.4 Stokes and AGM steps are **contextual selected checks only**. These are **not complete section certifications** and do not certify all Hermitian torsion Jacobi derivations, arbitrary convex MA mixed continuity, or the downstream elliptic estimates. **25 current chapters, 747 numbered ToC sections, zero full section certificates**; historic resolved/unresolved records unchanged. All dedicated Demailly approximation/regularization, Bergman, L²/OT, multiscale-atlas and positivity-loss work stays **deferred-by-user**.

**Actions:** audit Markdown only on the review branch. No source/body/proof-registry/tag/canonicalization edits, no merge, no build, no CI, no website publication, no MathJax browser test, and no formal verification.
