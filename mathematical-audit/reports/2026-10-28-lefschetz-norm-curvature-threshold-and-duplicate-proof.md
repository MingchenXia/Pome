# 2026-10-28 — Lefschetz norm bounds, partial-curvature boundary examples, and one duplicated canonical proof

## Review boundary and exact source

- **Production main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Review branch starting HEAD:** `7b3b9f87f5e66dde96194ca2b3137d300b94fe8b`.
- **Author instructions freshly read:** `AGENTS.md` (main blob `eda69505b93b4782290d9cfac07c8651dedd17c5`), `documentation/proof-expansions.md` (main blob `8b37e218c74d5a93637e0f092cf5f29cc338a94d`), branch `README.md`, `mathematical-audit/LATEST.md`, `mathematical-audit/LEDGER.md`, and `mathematical-audit/SECTION_MATRIX.md`.
- **Actual fresh table of contents:** 25 subject chapters, 747 unique numbered section identifiers at this main revision. This run directly examined **selected proof-level passages of §§10.47, 10.48 and 10.49**, each previously inventory-only in the coverage matrix. §11.3 introduction and §11.5.1 supplied **context only** and have not been promoted to new proof-level coverage. No complete section or chapter was certified.
- **Excluded subject:** Demailly approximation/regularization and its dedicated Bergman, $L^2$, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss completion programme are entirely **deferred-by-user**, neither examined nor certified here. The historical source identifier `demailly-complex-geometry` below names the *nonexcluded Hodge/curvature material* in the integrated edition, not a reopening of the excluded programme.

The findings below distinguish an **integrated-edition rendering error** from two **verified conditional deductions**. Neither conditional deduction independently certifies all upstream Hodge or Bochner analytic inputs. Historical source attribution and all permanent tags must be preserved in any separately reviewable repair.

## POME-CURVATURE-CANONICAL-PROOF-DOUBLE-RENDER-001

**Status:** **confirmed error — integrated reading-edition proof placement/duplication only**, not a false mathematical theorem. **Severity:** medium.

**Exact canonical statement and proof:**
`docs/sections/hodge-theory-curvature-and-compact-vanishing--one-point-curvature-vanishing/index.html`, main blob `2e93425bed7c9a6092407b10e1a276b1f42552f9`, **lines 75–101**. Theorem **10.48.3**, source label **`demailly-complex-geometry:77A7269F`**, permanent tag **`2CCDF84C1B3C`**: one-point partial semipositivity and the corresponding vanishing on a compact connected Kähler manifold. Its complete proof is attached to that theorem at **lines 81–101**.

**Second, duplicate rendering:** `docs/sections/hodge-theory-curvature-and-compact-vanishing--partial-curvature-positivity-and-vanishing/index.html`, main blob `4b0f765b63e998da517003174a27ca7c1fce14b8`, **line 66** has a standalone “See Theorem 10.48.3” shared-entry reference. It is immediately followed by an **orphaned proof element at lines 68–88** repeating the entire proof of the canonical theorem without repeating the theorem statement there. This is within §10.49 (section source `demailly-complex-geometry:24863DEF`, section tag `3B7EBA26CB27`), not a separately numbered theorem.

**Exact reproducible text check actually performed:** extract the body of each `<article class="env-proof">...</article>` element from both main HTML files and normalize consecutive whitespace to a single space. The **fourth** extracted proof in §10.48 and the **second** in §10.49 are **identical, all 2,481 normalized characters**, including mathematical content, internal references and QED element. The duplicate is therefore real proof-body identity, not merely two similarly titled results, an additional version, or a historical attribution.

**Impact:** a reader sees an otherwise contextless repeated proof just below a reference to the existing theorem. This wastes reading space and makes the proof-body placement ambiguous, but **does not invalidate Theorem 10.48.3, Theorem 10.49.4 or Theorem 10.49.6**. No incompatible canonical statements or proof conclusions were found in these snippets.

**Proposed correction only:** in a separately reviewed canonicalization/rendering change, render the canonical proof once with canonical Theorem 10.48.3 and keep the shared-entry reference in §10.49 **without** an orphaned duplicate proof. Verify that source labels, attribution, original proof, tag `2CCDF84C1B3C`, section tag `3B7EBA26CB27`, navigation and any legitimate aliases are retained. Audit branch does **not** edit source, registry, generated HTML or permanent tags. **Affected:** the two section pages and shared-entry proof-placement/navigation generation. Tag pages and browser behavior were not independently checked.

## POME-LEFSCHETZ-HARMONIC-NORM-OPTIMAL-001

**Status:** **verified conditional deduction**; underlying printed theorems are correct. **Severity:** low.

**Exact anchors:** `docs/sections/hodge-theory-curvature-and-compact-vanishing--hodge-structure-and-lefschetz-decomposition/index.html`, blob `2d268e8c6e34c11d84aba09163e6334ba037b46f`:
- Lemma **10.47.1**, source **`demailly-complex-geometry:5C1E4B1C`**, tag **`99F7CD84D262`**, lines **10–30**; its norm formula **10.47.5**, source **`demailly-complex-geometry:22E81F1A`**, tag **`A1C2A0FF7C70`**, lines **25–28**.
- Harmonic Kähler commutation Lemma **10.47.7**, source `demailly-complex-geometry:634E3178`, tag `EDA0CE6758F1`, lines **77–105**.
- Hard Lefschetz Theorem **10.47.15**, source **`demailly-complex-geometry:B6E59468`**, tag **`9F95F07CA33F`**, lines **212–249**, notably its harmonic summand proof at **241–248**.

**New exact statement:** if $(X,\omega)$ is a compact Kähler manifold of complex dimension $n\ge1$, $v$ is an $L^2$-normalized or arbitrary harmonic complex-valued $k$-form with $0\le k\le n$, $s=n-k$, and $m=\lfloor k/2\rfloor$, then
\[
\boxed{s!\,\|v\|_{L^2}\ \le\ \|\omega^{n-k}\wedge v\|_{L^2}\ \le\ \frac{(s+m)!}{m!}\,\|v\|_{L^2}.}
\]
These are **optimal universal constants at fixed $n,k$**, including the endpoint $k=n$ where both equal one. The estimate is a sharpened *norm* statement, not a replacement for Hard Lefschetz.

**Complete deduction from the displayed internal algebra:** by the orthogonal decomposition in Theorem 10.47.15,
\[
v=\sum_{r=0}^{m}L^r v_r,\qquad v_r\text{ primitive of degree }k-2r,
\]
with some summands possibly zero. By (10.47.5), on the $r$-th summand
\[
\|L^s(L^r v_r)\|_{L^2}=\frac{(r+s)!}{r!}\|L^r v_r\|_{L^2}.
\]
The respective image summands are orthogonal. If $s\ge0$, the factor
$a_r=(r+s)!/r!=s!\binom{r+s}{s}$ is nondecreasing in $r$ (constant at $s=0$), and so lies between $s!$ and $(s+m)!/m!$. Squaring and summing the orthogonal terms proves both inequalities. **No switching of nonlinear limits, net compactness, or regularization is used.**

**Equality models:** on a flat complex $n$-torus with its translation-invariant Kähler form, nonzero constant-coefficient $k$-forms of pure holomorphic type $(k,0)$ are primitive ($\Lambda v=0$) and harmonic, realizing the **lower** factor $s!$. For the **upper** factor take $v=\omega^m$ when $k=2m$ and $v=\omega^m\wedge dz_1$ when $k=2m+1$, with a fixed nonzero translation-invariant holomorphic one-form $dz_1$. Both have only the top $r=m$ Lefschetz summand and are harmonic, realizing $(s+m)!/m!$. The cases $k=0$ and $s=0$ follow without change.

**Action/dependents:** optional sharp operator-norm/condition-number remark near (10.47.5) or Theorem 10.47.15. It depends on the printed primitive-chain formula and the harmonic commutations, which were checked here at the indicated passages but **not independently re-proved through the full elliptic Hodge theory chain**. No false original statement, missing proof or mandatory repair claimed.

## POME-PARTIAL-CURVATURE-BOUNDARY-SHARP-001

**Status:** **verified conditional deduction**, not an error in either printed vanishing theorem. **Severity:** low.

**Exact anchors:** `docs/sections/hodge-theory-curvature-and-compact-vanishing--partial-curvature-positivity-and-vanishing/index.html`, blob `4b0f765b63e998da517003174a27ca7c1fce14b8`. Eigenvalue formula **10.49.1**, source **`demailly-complex-geometry:3E846E97`**, tag **`6BAE998D8301`**, lines **7–14**; Girbau vanishing Theorem **10.49.4**, source **`demailly-complex-geometry:105B7EBC`**, tag **`876EBA05B64C`**, lines **90–114**; the printed dense-open failure example **10.49.5**, tag **`00E6A77FAC15`**, lines **117–145**; asymptotic $q$-vanishing Theorem **10.49.6**, source **`demailly-complex-geometry:B5D095E7`**, tag **`C7B9CDDC2DB1`**, lines **147–195** and following conclusion.

**New sharpness construction, all $n\ge1$, $1\le s\le n$:** put $r=n-s+1\ge1$, $d=s-1\ge0$ and let
\[
X=\mathbf P^r\times T^d,\qquad
L=p_1^*\mathcal O_{\mathbf P^r}(r+2),
\]
where $T^d$ is a flat complex $d$-torus (a point if $d=0$). Equip the projective factor with the Fubini–Study metric and the torus with a flat Kähler metric. The Chern curvature of $L$ is semipositive and has **exactly $r=n-s+1$ strictly positive eigenvalues at every point**, with exactly $d=s-1$ null directions.

1. Since $K_{\mathbf P^r}=\mathcal O_{\mathbf P^r}(-r-1)$, there is a nonzero holomorphic $L$-valued $(r,0)$-form $\sigma$ on $\mathbf P^r$, corresponding to a section of $K_{\mathbf P^r}\otimes\mathcal O(r+2)=\mathcal O(1)$. On $T^d$, choose a nonzero translation-invariant holomorphic $d$-form $\Omega$ (for $d=0$ take $\Omega=1$). The exterior product $p_1^*\sigma\wedge p_2^*(\Omega\wedge\overline{\Omega})$ is a **nonzero Dolbeault-harmonic $L$-valued $(n,d)$-form** for the product Hermitian metrics: $\sigma$ is $\bar\partial$-closed and automatically $\bar\partial^*$-closed in antiholomorphic degree zero; the flat torus top form is harmonic; the product $\bar\partial$-Laplacian is the sum of factor Laplacians on pullback bundles. Thus
\[
H_{\bar\partial}^{n,s-1}(X,L)\ne0,\qquad n+(s-1)=n+s-1.
\]
Consequently Theorem 10.49.4's inequality $p+q\ge n+s$ cannot uniformly be weakened to $p+q\ge n+s-1$, **even under the exactly stated everywhere-rank curvature hypothesis**. This is different from the original §10.49.5 example, which only relaxes the curvature rank hypothesis to a dense-open locus.
2. For every integer $k\ge1$, choose a nonzero $s_k\in H^0(\mathbf P^r,\mathcal O(k(r+2)))$. Then $p_1^*s_k\otimes p_2^*\overline\Omega$ is a nonzero harmonic $(0,d)$-form with values in $L^k$ (or, equivalently, its restriction to a torus fiber where $s_k\ne0$ represents the nonzero torus top Dolbeault class). Therefore
\[
H^{s-1}(X,L^k)\ne0\quad\text{for **all** }k\ge1.
\]
Taking $F=\mathcal O_X$ proves the lower bound $q\ge s$ of Theorem 10.49.6 cannot be weakened to $q\ge s-1$, no matter how large the tensor power $k$ is.

**Action/dependents:** optional single product example after Theorem 10.49.6 referencing both endpoints while keeping their **different** hypotheses: Theorem 10.49.4 requires semipositivity and a Kähler background; Theorem 10.49.6 allows arbitrary curvature signs but needs sufficiently many positive eigenvalues *everywhere*, and works on compact complex manifolds. Do not merge the statements or their source labels. The degree/rank and product calculations are self-contained; the printed theorems' respective Bochner–Kodaira, Hermitian torsion, spectral calculus and Dolbeault Hodge prerequisites remain conditional, not certified. No excluded analytic regularization was inspected.

## Other selected checking, precise coverage and open work

- §10.47: Lemma 10.47.1's primitive chain and commutator algebra, Theorem 10.47.15's harmonic decomposition, plus the displayed $(\partial,\bar\partial)$-lemma proof at 10.47.9 (lines 110–139) and Kähler commutations at 10.47.7 (77–105). The selected identities and norm scaling are consistent. The full compact elliptic Hodge construction of §10.46 remains an unverified upstream input.
- §10.48: Theorem 10.48.3's actual statement and full proof placement, crosschecked against §10.49, and its use of one-point positivity/holomorphic continuation. The full vector-bundle curvature and Serre-duality chains were not independently certified.
- §10.49: eigenvalue coefficient formula, matrix functional calculus Lemma 10.49.2, Girbau Theorem 10.49.4 eigenvalue count and constant choices, Example 10.49.5, asymptotic curvature Theorem 10.49.6 fixed-metric approach (the visible portion) and proof-duplication check. Any uninspected remainder of §10.49 remains unreviewed.
- §11.3 introductory Gauduchon pairing, blob `02d635e918120c4026c38d14119db9377eefe61f`, lines 7–10, checked only as background against §11.5.1, source `non-kahler-pluripotential-theory:0D4A42C8`, tag `828FAD1A35BF`, blob `34af83ff391b5e5590cd9cb10ca4cd2b3faff02c`, lines 10–29. No extra first-coverage count or novel finding.
- Actual coverage change: **only three previously inventory-only ToC rows (§§10.47–10.49)** to “selected passages”; **747** unique section rows retained, **zero** complete-section certifications. Resolved/unresolved/deferred historical findings remain unchanged.
- No project tests, Python/JavaScript build, CI, browser render, formalization, source or production modifications are claimed. The only independent programmatic check in this run was the normalized **2481-character exact duplicate proof comparison**, alongside direct mathematical derivations and current-main GitHub source reading.

**Audit-only proposal:** retain the canonical theorem/proof/tags and historical attribution; make any body, source, registry, or website repair in a separately reviewed patch/PR, not here. Keep all Demailly approximation/regularization and dedicated Bergman/$L^2$/Ohsawa–Takegoshi/multiscale/positivity-loss research **deferred-by-user** without changing their historical status.
