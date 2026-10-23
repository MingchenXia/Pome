# Mathematical audit: Harder–Narasimhan exterior-power slopes and movable semistability

**Checkpoint:** 2026-10-23 12:53 Asia/Shanghai, scheduled reading session. **Precisely verified main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; audit branch `review/mathematical-audit` at `f11b70144d62874c748ffdf9ba0d225fe28afd82`. This report is an audit-only proposal and has not been merged or published. **No Demailly regularization, Bergman, L², Ohsawa–Takegoshi or positivity-loss proof-completion was investigated.**

The following current-main files and descriptions were freshly read through the GitHub connector: `AGENTS.md` (blob `eda69505b93b4782290d9cfac07c8651dedd17c5`), `documentation/proof-expansions.md` (`8b37e218c74d5a93637e0f092cf5f29cc338a94d`), `docs/chapters/index.html` (`c0c07abf4d8f7575b54cff2ec694fcf987f51cf8`) and `review/mathematical-audit/{README.md,mathematical-audit/LATEST.md}` (the latter blob `7d09901d60b16f9cfdf6801b10473f7eb16f1127`). The current published inventory contains 25 chapters and 747 numbered sections; that is **not** a verification count.

## Actual proof reading and precise sources

- **First direct nonexcluded proof inspection, §10.106:** `docs/sections/degrees-and-maximal-slopes/index.html`, blob `b824fc476c0cecf64bc52f2178c90344dfb3e7ab`: Lemma 10.106.1, source label `cao-paun-foliations:26EDBAD1`, permanent tag `21D47D6E39D1`, lines 17–39 (maximum for an additive rank-monotone degree); Theorem 10.106.2, source `cao-paun-foliations:E126ED45`, tag `469F76790780`, lines 43–73 (HN filtration); Lemma 10.106.3, source `cao-paun-foliations:3D33031A`, tag `B72C1D61D638`, lines 77–89 (slope duality). Checked additivity, saturation, the sign in the monotonicity argument for the directed real parameter `t`, and the fact that no sequence extraction is needed: finite ranks force eventually constant saturated sheaves in the *nested* family. This is not a full certification of the upstream degree theory.
- **First direct nonexcluded proof inspection, §10.107:** `docs/sections/tensor-products-and-involutivity/index.html`, blob `b0939c7452c9ef74f49bd7751c8c728c251199d4`: opening exact external semistability input, lines 8–9; Proposition 10.107.1, source `cao-paun-foliations:8DCECA93`, tag `BB9ADDF87BD1`, lines 11–25 (tensor slopes; semistable exterior powers; explicit warning that arbitrary exterior power need not have slope `q μ_max(E)`); Corollary 10.107.2, source `cao-paun-foliations:F67243E2`, tag `1BF160484066`, lines 29–43 (bracket involutivity). Checked the generic bundle-locus filtration and determinant/saturation accounting. The cited movable-class tensor semistability theorem is **not** proved internally here: see dependency record below.
- **Cross-check of actual new geometric dependents:** `docs/sections/holomorphic-forms-and-positive-foliations/index.html`, blob `5279e4ea52ab1eb2662dd83802bc132671729c1b`, Lemma 9.75.2 lines 20–28; Theorem 9.75.3 source `cao-paun-foliations:D94BC8B0`, tag `CDF6A16B105C`, lines 32–72; Corollary 9.75.4 tag `745947D9E1A8`, lines 76–84. Only the slope-to-bracket steps and the *listed* geometric external dependencies were checked, not the Campana/GHS/Fujiki/BDPP existence theorems. `docs/sections/tangent-slopes-and-covering-rational-curves/index.html`, blob `88c8dc4651dc7d9cd21609d3d453521f97e0190d`, Lemma 9.76.1 source `cao-paun-foliations:AA1A5BE2`, tag `4F2E71913C12`, lines 11–27 and Corollary 9.76.2 source `cao-paun-foliations:0B126172`, tag `8876081BAAEC`, lines 31–58. Independently checked the determinant map `O_{P^1}(2) -> det f^* T_X` at a generic submersive point and the curve pairing argument; the bound `-K_X·α>=2` is already printed and **not** counted as a new finding.
- **Additional dependency/boundary cross-check:** `docs/sections/numerical-dimension-and-cotangent-quotients/index.html`, blob `85538a5ba880030f432282e302a446a230ae15ec`, Theorem 10.109.2 source `cao-paun-foliations:71F4321F`, tag `7E716F90C084`, lines 54–69; the normalizations `c1((Ω_X^1)^{⊗m})=m n^{m-1}c1(K_X)` and the sheaf/slope deduction were checked. The §10.109 numerical dimension paragraph invoking *same-class simultaneous approximation* at lines 26–32 belongs to an excluded upstream regularization programme and was deliberately **not** audited. `docs/sections/flat-twists-of-adjoint-section-envelopes/index.html`, blob `f106e8f79d1a1341045f1e3c41cdeb531b5f699b`, Theorem 19.11.1 source `cao-paun-foliations:24E1B42B`, tag `1D4EB7891AC1`, lines 8–59: sampled the factorization `u_k=s^{ℓ-1}v_k`, the fixed weight exponent `-2(k_0-1)/k_0`, and the normalized-psh limit. Its cited Nadel vanishing/L² and related dedicated arguments were *not* reopened or certified.

## POME-CAOPAUN-HN-WEDGE-POLYGON-001

**Status:** `verified conditional deduction`; **severity:** low (new precise consequence, **not** a false theorem or a repair). **Source:** §§10.106–10.107 and precise tags above. **Prerequisite:** the Kähler/movable tensor-semistability input explicitly quoted before Proposition 10.107.1; use only the parts of that proposition concerning semistable tensor and exterior powers and the internal HN theorem. The conclusion is exact, including arbitrary nonsemistable torsion-free sheaves.

**Claim.** Let `X` be a compact Kähler manifold and `α` a movable real degree class. Let `E` be a nonzero torsion-free coherent sheaf of rank `r`, with HN filtration

\[
0=E_0\subsetneq E_1\subsetneq\cdots\subsetneq E_\ell=E,
\qquad Q_i=E_i/E_{i-1},\quad r_i=\mathrm{rk}\,Q_i,
\quad \mu_1>\cdots>\mu_\ell.
\]

Write `λ_1 >= ... >= λ_r` for the HN slopes repeated `r_i` times. Then for every `1 <= q <= r`, with reflexive hull understood,

\[
\boxed{\displaystyle
\mu_{\alpha,\max}((\Lambda^q E)^{**})=\sum_{j=1}^q\lambda_j,
\qquad
\mu_{\alpha,\min}((\Lambda^q E)^{**})=\sum_{j=r-q+1}^r\lambda_j.
}\tag{1}
\]

In particular the upper value is at most `q μ_{α,max}(E)`, with equality exactly when the first `q` HN slopes equal the top slope. The analogous sharp lower bound uses the bottom HN slopes.

**Proof.** Remove one analytic subset of complex codimension at least two where `E`, all `E_i`, and all `Q_i` cease to be locally free. This is possible on a smooth manifold for torsion-free coherent sheaves and saturated HN subsheaves. On the resulting `U`, the HN filtration is a filtration by subbundles. The standard exterior filtration of `Λ^q E|_U` has associated graded bundles

\[
\bigotimes_{i=1}^\ell\Lambda^{q_i}Q_i|_U,
\quad 0\le q_i\le r_i,\quad\sum_i q_i=q.
\]

Each factor has slope `q_i μ_i` and is semistable by the quoted exterior-power part of Proposition 10.107.1. Their tensor product is semistable with slope `\sum_i q_i μ_i`, **conditionally on the quoted movable tensor-semistability input**. Every subsheaf of `Λ^q E` can be intersected with this finite filtration; determinants and slopes are unchanged by reflexive extension across the codimension-two complement. Additivity of degrees in the resulting torsion-free exact sequences bounds its slope above by

\[
\max_{\sum q_i=q}\sum_i q_i\mu_i
  =\sum_{j=1}^q\lambda_j,
\]

because the greedy allocation of the `q` slots to the highest HN slopes maximizes the sum. This proves the *upper* bound for `μ_max`.

For the lower bound choose the index `j` with `R_{j-1}<q\le R_j`, `R_j=\sum_{i\le j}r_i`, and put `k=q-R_{j-1}`. On `U`, exterior multiplication defines a **generically injective** bundle map

\[
\det E_{j-1}\otimes\Lambda^k Q_j
\longrightarrow \Lambda^q E_j \longrightarrow \Lambda^q E.
\]

Indeed, after a local vector-bundle splitting `E_j=E_{j-1}\oplus Q_j`, the map identifies the first factor with the summand containing all `R_{j-1}` first-block vectors; thus it is injective. Its coherent image, extended as a torsion-free subsheaf of `(Λ^q E)^{**}`, has slope

\[
\deg_\alpha(E_{j-1})+k\mu_j
  =\sum_{i<j}r_i\mu_i+k\mu_j
  =\sum_{i=1}^q\lambda_i.
\]

No effective divisorial alteration can decrease the slope upon saturation because `α` is nonnegative on effective divisors. This proves equality for `μ_max`. Applying the same reasoning to the dual HN filtration, with reversed slopes `-λ_r,...,-λ_1`, and using the internal duality Lemma 10.106.3, gives the asserted minimum-slope identity. All arguments take place on a single fixed codimension-two bundle locus; no weak compactness, approximating sequence, or interchange of limits is involved. **QED.**

**Sharp and diagnostic example.** On `X=P^1` let `E=O(2)⊕O(-1)⊕O(-3)` and `q=2`. Then

\[
\Lambda^2 E\simeq O(1)\oplus O(-1)\oplus O(-4).
\]

Thus `μ_max(Λ²E)=1=2+(-1)` and `μ_min(Λ²E)=-4=(-1)+(-3)`, whereas the invalid naive value `2μ_max(E)=4` is not the answer. For `q=r`, (1) reduces to the determinant degree identity. For semistable `E`, (1) recovers the printed Proposition 10.107.1, so those two versions should be **kept as distinct statements**, rather than mis-canonicalized.

**Proposed patch:** an additional independent corollary following Proposition 10.107.1, with this exact conditionality and proof; no edit to existing source label, permanent tag, generated HTML or the main branch. **Affected dependents:** exact exterior-power estimates in Corollary 10.107.2 (where the semistable specialization suffices), Lemma 9.75.2, and any later determinant/tensor argument replacing the incorrect `q μ_max(E)` heuristic. The latter heuristic is *already correctly warned against* by the printed text.

## POME-CAOPAUN-MOVABLE-TENSOR-INPUT-001

**Status:** `external dependency` (not an independently established false statement, and **not** classified as a missing step once the quoted theorem is admitted). **Severity:** medium for the author's self-contained preference because it is a central transitive input.

**Location:** the initial paragraph of §10.107, `docs/sections/tensor-products-and-involutivity/index.html:8–9` (blob and tags above), explicitly states the needed theorem: on a compact Kähler manifold, reflexive tensor product of torsion-free movable-slope-semista­ble sheaves remains semistable, with additive slopes. It cites **Ou2025, Lemma 4.4**, and **the Toma appendix to CP11, Proposition 6.1/Theorem 6.2**, and explicitly retains Hermite–Einstein existence and polarization-variation steps as deep prerequisites. The printed article is transparent about these external inputs; attribution should remain.

**Exact proof boundary:** Internal HN existence in §10.106 does not itself prove semistability of tensor products for *an arbitrary boundary movable class*. The semistable-graded filtration upper bounds in Proposition 10.107.1, the newly derived formula (1), the bracket criterion in Corollary 10.107.2, the foliation result §9.75, and the cotangent quotient conclusion §10.109 depend on that separate theorem. One cannot replace it by tensor additivity of the **degree** (true for all bundles) or by semistability only for a fixed ample/Kähler polarization without justifying passage to the chosen movable class. The boundary class may be non-Kähler; simply approximating polarizations would require a proof that the HN slopes and semistability persist under the relevant limit.

**Proposed correction:** retain and identify the exact quoted input and dependency graph in the audit register; if a later genuinely independent internal proof becomes available, integrate that proof *outside the author's excluded regularization/L² programme*. Do **not** present Ou/Toma's external proof as independently verified here; do not erase scholarly attribution. Do not relabel the downstream propositions as false or certified.

## Verification and limits

A small deterministic exact-integer script `checks/check_hn_wedge_polygon.py` tests all greedy-allocation identities for a grid of ordered integer slope vectors and the direct-sum `P^1` example. Such combinatorial checks do **not** prove the semistability input, the filtration on analytic sheaves, or any project theorem. This session made no complete Pome build, CI run, formal check, website publication, source/registry edit, or main-branch change. §9.75's external geometric existence theorems and §19.11's analytic Nadel and L² dependencies were not audited. Prior excluded Demailly-related ledger items remain **`deferred-by-user`**, neither resolved nor verified.

## GitHub write and remote verification

One ordinary single-file UTF-8 `create_file` attempt on `review/mathematical-audit` for the report path `mathematical-audit/reports/2026-10-23-hn-exterior-polygon-and-movable-dependency.md` was denied with the **exact** tool response:

`This tool call was blocked by OpenAI's safety checks. Please double check what you are sending.`

There was **no** retry, alternate encoding, split payload, alternate write route, forced ref update or other remote mutation. A separate read-only check subsequently confirmed review-branch HEAD unchanged as `f11b70144d62874c748ffdf9ba0d225fe28afd82`; fetching that report from the branch returned HTTP 404. Accordingly **zero commits were pushed** in this checkpoint. Existing audit PR #9 is **already closed and merged**, so no new PR was opened. This detailed report and ledger/matrix/checks remain in the local pending archive only.
