# Audit: dual Griffiths curvature sign and nonnegative maximal-slope foliation criterion (2026-10-31)

- **Production main inspected:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
- **Branch receiving audit notes only:** review/mathematical-audit.
- **Scope:** new selected checks of §10.104.1 (one proof sentence) and §10.106.2 / §10.107.1–2 (HN filtration and bracket). This is an *increment* on the distinct 2026-10-23 HN exterior-polygon audit, not new certification of any complete section.
- **Explicit exclusions:** no Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale atlas, or positivity-loss proof completion. Their previous findings remain deferred-by-user.

## POME-DET-DUAL-GRIFFITHS-SIGN-001 — low / confirmed error (proof wording, not lemma)

**Target.** Production file **docs/sections/determinants-of-singular-bundle-metrics/index.html**, Git blob **901d6104f4a5ba01b188270bd6e2377ee4baeb9d**, source label **cao-paun-foliations:2FBA7F63**, permanent tag **EC118288B440**, Lemma §10.104.1, statement physical lines 8–9, proof paragraph **line 17**. The exact asserted intermediate sentence is: “Their smooth dual metrics therefore have positive Griffiths curvature”.

**Hypotheses.** A holomorphic bundle G has a Hermitian metric finite and positive definite almost everywhere, and the logarithmic squared norm of each holomorphic section of G* is plurisubharmonic. This is the *Griffiths-semipositive* convention for **G**, equivalently Griffiths seminegative for **G*** (on the smooth locus). The printed lemma concludes positivity of the determinant of G and is **not refuted**.

**Decisive smooth compact countermodel to the intermediate assertion.** Put G=O(1) on P¹ with the Fubini–Study metric. In affine coordinate z, in the standard local frame,
\[
H=(1+|z|^2)^{-1},\qquad H^*=1+|z|^2 .
\]
Every holomorphic dual section f e* has
\[
\log\|f e^*\|^2_{H^*}
=\log|f|^2+\log(1+|z|^2),
\]
which is subharmonic. Nevertheless the curvature of the **dual** line metric is
\[
\Theta_{G^*}=-\partial\bar\partial\log H^*
=-\partial\bar\partial\log(1+|z|^2)<0,
\]
whereas \(\Theta_G=+\partial\bar\partial\log(1+|z|^2)>0\). Thus “positive Griffiths curvature” for the *dual* metrics reverses the sign. The subsequent displayed inequality \(dd^c\log\det H^*_\varepsilon\ge0\) is the **correct** sign: it is the determinant curvature of the **primal** metric, not of the dual one.

**Precise correction.** Replace only that erroneous clause by “Their smooth primal metrics consequently have Griffiths-semipositive curvature (equivalently, the dual metrics have Griffiths-seminegative curvature); taking the trace gives \(dd^c\log\det H^*_\varepsilon\ge0\).” Retain the remaining proof, attribution, source label and permanent tag. The algebraic sign is already visible at smooth rank one; no regularization theorem was reviewed or repaired here.

**Status boundary and dependents.** A **confirmed local proof-sign sentence error**, not a counterexample to Lemma 10.104.1 and not a proof that the singular convolution/limit steps are valid. Any future invocation of determinant semipositivity must use the primal/dual distinction. No transitive dependency audit or production patch is claimed.

## POME-FOL-HN-NONNEGATIVE-BRACKET-001 — low / verified conditional deduction

**Targets.** Production **docs/sections/degrees-and-maximal-slopes/index.html**, blob **b824fc476c0cecf64bc52f2178c90344dfb3e7ab**: Theorem §10.106.2, source **cao-paun-foliations:E126ED45**, permanent **469F76790780**, physical lines **43–72**. Production **docs/sections/tensor-products-and-involutivity/index.html**, blob **b0939c7452c9ef74f49bd7751c8c728c251199d4**: the standing Kähler/movable tensor-semista\-bility input at line **8**, Proposition §10.107.1 source **cao-paun-foliations:8DCECA93**, permanent **BB9ADDF87BD1**, lines **11–25**, and Corollary §10.107.2 source **cao-paun-foliations:F67243E2**, permanent **1BF160484066**, lines **29–43**.

**Hypotheses and noninternal premise.** X is compact Kähler, \(\alpha\) is a movable real test class for the slope, and \(\mathcal F\subset T_X\) is saturated and involutive. Let \(\mathcal G\subset\mathcal F\) be its largest HN maximal-slope subsheaf and set \(s=\mu_\alpha(\mathcal G)\). The *external movable-class reflexive tensor-product semistability theorem* quoted at §10.107 line 8 remains a **genuine unverified input**, already tracked as **POME-CAOPAUN-MOVABLE-TENSOR-INPUT-001**. No new proof of that input is claimed.

**New exact sufficient criterion.** Whenever
\[
\mu_{\alpha,\max}(\mathcal F/\mathcal G)<2s,
\]
the saturated HN term \(\mathcal G\) is involutive. In particular it suffices to assume
\[
\boxed{\mu_\alpha(\mathcal G)\ge0}
\]
rather than the printed corollary's strictly positive condition; at the endpoint \(s=0\), its separate conclusion must be \(\mu_{\alpha,\min}(\mathcal G)=0\), **not** a strictly positive minimum slope.

**Proof.** If \(\mathcal F/\mathcal G=0\), the conclusion is immediate; if \(\operatorname{rk}\mathcal G=1\), the bracket obstruction vanishes identically. Otherwise §10.106.2 gives the semistability of \(\mathcal G\), its saturation, and
\[
\mu_{\alpha,\max}(\mathcal F/\mathcal G)<s.
\]
The tensor-semista\-bility input used in §10.107.1 implies \((\bigwedge^2\mathcal G)^{**}\) is semistable of slope \(2s\), hence
\[
\mu_{\alpha,\min}((\bigwedge^2\mathcal G)^{**})=2s.
\]
On the common bundle locus, the Levi bracket modulo \(\mathcal G\) is \(\mathcal O_X\)-linear and induces
\[
\beta:\bigwedge^2\mathcal G\longrightarrow\mathcal F/\mathcal G .
\]
Because \(\mathcal G\) is saturated in \(T_X\), the relevant sheaves agree with their reflexive hulls away from codimension at least two; the map extends there to the reflexive hull of the target. Taking reflexive hulls does not change slopes, since any quotient added is supported in codimension at least two. Thus the Hom vanishing criterion of §10.106.3 applies to the strict numerical hypothesis \(\mu_{\max}(\mathcal F/\mathcal G)<2s\), forcing \(\beta=0\). The torsion-free target then gives involutivity everywhere. The HN inequality \( \mu_{\max}(\mathcal F/\mathcal G)<s\) automatically implies the numerical hypothesis when \(s\ge0\); no strict positive margin is needed at \(s=0\).

**Realized endpoint (rank two, not just the automatic rank-one case).** On \(X=E_1\times E_2\times C\), with elliptic curves \(E_i\), a genus \(g(C)\ge2\) curve C and any product Kähler class, put \(\mathcal F=T_X\) and \(\mathcal G=T_{E_1\times E_2}\) pulled back to X. The rank-two G is holomorphically trivial, so its slope is zero; the quotient \(p_C^*T_C\) has strictly negative slope. Thus G is the maximal HN term, and its involutivity is manifest. The printed \(s>0\) hypothesis excludes this natural valid endpoint.

**Status, correction, dependents.** This is a **verified conditional deduction**, not a false original corollary: its conclusion under \(s>0\) remains correct conditional on the external movable tensor theorem. Add an optional remark after §10.107.2 with the \(s\ge0\) endpoint and the more general \(2s>\mu_{\max}(\mathcal F/\mathcal G)\) criterion; keep external attribution and all tags. This supplies a sharper conditional input for slope-based foliation/leaf constructions (notably the downstream foliation argument around §9.75), but **does not** certify the external semistability theorem or the foliation quotient machinery.

## Actual review and verification boundary

- Read current main, AGENTS.md, documentation/proof-expansions.md, audit-branch LATEST.md and README.md, and the ToC/section-matrix rows; all claims pinned to main **b6933b772f41b45918f7e25ed1afbbb1fd892272**.
- New proof-level *increment* only: §10.104.1 line 17 primal/dual curvature sign; §10.106.2 HN gap; §10.107.1–2 exterior semistability and bracket, with §10.106.3 Hom vanishing checked as a direct downstream premise. Earlier 2026-10-23 full HN exterior polygon finding is retained and not re-counted.
- No whole mathematical section certified. The existing current inventory remains **25 chapters, 747 numbered ToC sections, zero whole-section certifications**.
- No numerical experiments, Python tests, project build, CI, website publication, formalization, main/source/registry/tag edit, or proof certification of external inputs.
- Demailly approximation/regularization and its dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof-completion programme stays **deferred-by-user**, never reopened.
