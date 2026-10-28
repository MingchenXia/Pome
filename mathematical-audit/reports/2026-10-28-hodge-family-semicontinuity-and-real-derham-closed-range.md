# 2026-10-28 — Compact elliptic-complex families and the real de Rham closed-range hypothesis

## Checked version, reading edition and exclusions

- **Production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; audit branch parent before this write: `6086d6374afc442a6ba5dfed05ef182301b544b1`.
- Author contract freshly read from `AGENTS.md` (main blob `eda69505b93b4782290d9cfac07c8651dedd17c5`), `documentation/proof-expansions.md` (main blob `8b37e218c74d5a93637e0f092cf5f29cc338a94d`), and the audit branch `README.md`, `mathematical-audit/LATEST.md`, `LEDGER.md` and `SECTION_MATRIX.md`.
- The **current main table of contents was re-enumerated from all 25 rendered chapter index pages**: 747 distinct numbered sections, no duplicate section IDs. This session first read precisely selected proofs in **§§10.46, 10.57 and 10.59**, formerly inventory-only. §10.70.3 is a conditional dependency crosscheck, **not new first-time coverage**. No complete section/chapter or upstream analytic theorem is certified.
- **Scope:** This note does not examine Demailly approximation/regularization, its dedicated Bergman, weighted $L^2$, Ohsawa–Takegoshi, multiscale-atlas or positivity-loss proof-completion programme. Historical work on them stays **deferred-by-user**, neither resolved nor verified. The identifier `demailly-complex-geometry` below denotes *nonexcluded* Hodge, topology and cohomology source statements only.

## POME-HODGE-HARMONIC-UPPER-SEMICONT-001

**Severity:** low. **Status:** **verified conditional deduction** (not a false printed theorem or a complete new proof of elliptic regularity).

**Integrated source:** `docs/sections/hodge-theory-curvature-and-compact-vanishing--compact-hodge-theory-and-analytic-duality/index.html`, main blob `b7001303a35ddd5c91f40e81cfc93523e8d6b8ab`. Lemma **10.46.1**, source `demailly-complex-geometry:273AE86C`, permanent tag `2EE58CB34CD0`, lines **10–104** (compact $H^1\hookrightarrow L^2$ at line 47 and Gårding estimate (10.46.3) at lines 58–70). Theorem **10.46.4**, source `demailly-complex-geometry:7CE52240`, tag `BD1EEDFB2146`, lines **108–139**; compact Hermitian Dolbeault application **10.46.6**, source `demailly-complex-geometry:C2407F7C`, tag `AEB699DDD0FF`, lines **152–164**. The exact kernel/Green decomposition and signs were checked at the displayed steps; the preceding Sobolev/Gårding foundational proofs remain conditional inputs.

**New precise statement.** Fix a compact boundaryless manifold $M$, smooth Hermitian bundles $V_q$ with *fixed* metrics, and a finite family of complexes $D_{q,t}:C^\infty(V_q)\to C^\infty(V_{q+1})$ for $t$ near $0$, with $D_{q+1,t}D_{q,t}=0$. Assume the coefficients of each first-order $D_{q,t}$ tend to those of $D_{q,0}$ in $C^1$, and the Hodge Laplacians $P_{q,t}=D_{q,t}^*D_{q,t}+D_{q-1,t}D_{q-1,t}^*$ have **uniformly positive scalar principal symbols** in the sense of Lemma 10.46.1. Then for each fixed $q$,
\[
\boxed{\dim H^q(D_t)=\dim\ker P_{q,t}\ \leq\ \dim\ker P_{q,0}\quad\text{for all sufficiently small }|t|.}
\]
Thus harmonic dimensions are **upper semicontinuous**. Equality, continuity or a canonical identification of harmonic spaces is **not** asserted.

**Proof, including the compactness point.** The integration-by-parts argument for (10.46.3), with continuous principal and first-order coefficients and a uniform ellipticity lower bound, provides $C$ independent of $t$ close to zero:
\[
\|v\|_{H^1}^2\le C(\|D_{q,t}v\|_2^2+
\|D_{q-1,t}^*v\|_2^2+\|v\|_2^2).
\]
If upper semicontinuity failed, choose $t_j\to0$ and $m+1$ $L^2$-orthonormal harmonic vectors $h_{j,a}$, where $m=\dim\ker P_{q,0}$. The estimate uniformly bounds all $h_{j,a}$ in $H^1$. The compact $H^1\hookrightarrow L^2$ embedding in Lemma 10.46.1 supplies, after a common subsequence, strong $L^2$ limits $h_a$ preserving pairwise inner products. As $D_{q,t_j}h_{j,a}=0$ and $D_{q-1,t_j}^*h_{j,a}=0$, the operator differences, which tend to zero in $H^1\to L^2$ norm (the adjoint coefficients need the assumed $C^1$ convergence), imply $D_{q,0}h_{j,a}\to0$ and $D_{q-1,0}^*h_{j,a}\to0$ in $L^2$. Weak $H^1$ limits and closedness of the first-order kernels give $D_{q,0}h_a=D_{q-1,0}^*h_a=0$. Elliptic regularity from 10.46.1 makes these $h_a$ smooth harmonic sections, contradicting $dim\ker P_{q,0}=m$. No sequential compactness is claimed in any nonmetrizable setting: this argument is a sequence in the compact $H^1\to L^2$ Hilbert embedding, for a one-parameter family.

**Strictness / exact sharp example.** On $M=S^1=\mathbb R/(2\pi\mathbb Z)$ with trivial unitary line bundle take the flat Hermitian connection $D_t=d+it\,dx$ (the 1-dimensional twisted de Rham complex). The Fourier mode $e^{ikx}$ has covariant derivative $i(k+t)e^{ikx}\,dx$. Hence $H^0(D_0)\cong H^1(D_0)\cong\mathbb C$, whereas both groups are zero for every sufficiently small nonzero real $t$. Every $P_{q,t}$ has the same positive scalar principal symbol. The drop in dimension shows that “upper semicontinuous” cannot be strengthened to “locally constant” without additional hypotheses.

**Proposed addition and dependents:** an optional corollary after Theorem 10.46.4, useful for smooth families of Dolbeault/Hodge complexes and bundle-valued de Rham operators (10.46.6/10). Keep fixed metrics, coefficient convergence and the uniform ellipticity premise explicit. No body, registry, source label or permanent-tag patch was made.

## POME-DE-RHAM-PERIOD-CLOSED-RANGE-001

**Severity:** low. **Status:** **verified conditional deduction** from the standard period form of the de Rham comparison; the ordinary noncompact *real* statement is correct with stronger hypotheses than strictly needed. This does **not** assert automatic closed range for the holomorphic Dolbeault complex.

**Integrated source:** `docs/sections/spectral-sequences-support-and-cup-products--integration-contraction-and-precise-duality-scope/index.html`, main blob `55412114272bdaf8f2b79ad36d829454862b32c9`. Lemma **10.59.2**, `demailly-complex-geometry:557D9B2C`, tag `42254A734333`, lines **26–40** (closed-range Fréchet dual argument); Corollary **10.59.3**, `demailly-complex-geometry:66861AB4`, tag `CFEFE5F704F2`, lines **44–63**. Compact-supported form/current comparison: `docs/sections/spectral-sequences-support-and-cup-products--compact-supported-forms-currents-and-compact-duality/index.html`, blob `b7aa363efc0c0104512b4291b9a0adb88e349fdb`, Corollary **10.57.1** `demailly-complex-geometry:5AC46646`, tag `A9627E651E13`, lines **7–25**, and compact pairing **10.57.2** tag `12F3669A5BAA`, lines **28–44**. Conditional comparison input §10.70.3, `demailly-complex-geometry:223C7EB2`, tag `9E4C37619D42`, `docs/sections/spectral-sequences-support-and-cup-products--local-systems-and-a-singular-comparison-with-supports/index.html`, blob `66ca556aac90cacad01dec69e61943398c888865`, lines **71–103**; this comparison is not independently certified here.

**Precise strengthening.** If $M$ is any Hausdorff second-countable smooth manifold, the image of
\[
d:\mathcal A^{k-1}(M;\mathbb R)\to\mathcal A^k(M;\mathbb R)
\]
is **closed in the standard compact-open $C^\infty$ Fréchet topology**, for every $k$. For oriented boundaryless $M$ of real dimension $d$, both closed-range premises in the *real* clause of 10.59.3 are therefore automatic; conditional on the standard de Rham period identification and the existing supported-current comparison, its conclusion strengthens to
\[
\boxed{H_c^{d-k}(M,\mathbb R)\simeq
(H^k_{\mathrm{dR}}(M,\mathbb R))'_{\mathrm{continuous}}.}
\]
No corresponding unrestricted holomorphic duality is inferred.

**Proof / exact conditional input.** Integration over each finite piecewise-smooth singular $k$-cycle $c$ is a continuous functional $I_c$ on the Fréchet space of smooth $k$-forms, since the finitely many simplex images are compact and require only coefficient $C^0$ seminorms. By Stokes, $I_c$ annihilates exact forms. The standard de Rham period comparison (obtainable by combining the local Poincaré resolution with smooth-singular/singular comparison as in §§10.43.11, 10.70.3) says a closed smooth form with all cycle periods zero is exact. Hence
\[
\operatorname{im}d_{k-1}=
\ker d_k\cap\bigcap_{c\in Z_k^{\mathrm{sm}}(M)}\ker I_c,
\]
an intersection of closed linear subspaces. This proves closed range for **nets as well as sequences**, without a sequential-closure shortcut. The *specific identification of smooth periods with the internal singular comparison* is taken as the stated standard input, not an independent verification of the entire proof of §10.70.3. Apply Lemma 10.59.2 and Corollaries 10.57.1/10.59.3. The given theorem's original closed-range hypothesis is mathematically correct, just redundant **in its real de Rham clause**.

**Why continuous, not full algebraic dual.** Take $M=\coprod_{j\ge1}S^1$ (countably many compact components), $d=1,k=0$. Direct componentwise calculation gives
\[
H^0_{\mathrm{dR}}(M;\mathbb R)=\prod_{j\ge1}\mathbb R
\quad\text{with the product Fréchet topology},\qquad
H_c^1(M;\mathbb R)=\bigoplus_{j\ge1}\mathbb R.
\]
The continuous dual of the product is exactly the algebraic **direct sum**: continuity at zero forces a functional to vanish on all but finitely many coordinate factors. The **full algebraic dual is larger**: choose a linear functional vanishing on $c_{00}$ but taking value $1$ on $(1,1,1,\ldots)$, then extend to a Hamel basis. This functional is algebraic but discontinuous. This is a dual-topology precision check, not a replacement of the ordinary-product finding already recorded in §10.71 or the Ext-product findings in §10.68.

**Proposed addition and dependents:** qualify Corollary 10.59.3 with an optional note that the real $d$-range hypotheses follow from the de Rham period criterion. Preserve the explicit hypotheses for its Dolbeault/vector-bundle clause, which has not been independently analyzed for automatic closedness. The period-comparison input is a genuine dependency, not a historical citation. No new original statement is declared false.

## Additional selected inspection, coverage, and verification limits

- **§10.46:** directly checked the distributional inverse, the Fredholm/Hodge orthogonal splitting, the closed smooth images, the scalar-principal Dolbeault symbol and the Hodge-dual signs in selected lines **39–103**, **123–163**, **178–227**. There was **no newly confirmed defect**. The full local elliptic regularity construction, all spectral dependencies and every theorem in the section are **not certified**.
- **§10.57:** the form/current compact-supported comparison and its dependence on soft sheaves, compact-support acyclicity, and compact Hodge pairings at **lines 7–44** were directly checked for their hypotheses. Upstream §10.43/10.56 remain conditional, not re-reviewed.
- **§10.59:** the actual Fréchet quotient, Hahn–Banach extension and closed-image argument of Lemma 10.59.2 plus the current/transposed differential steps of Corollary 10.59.3 were directly inspected at **lines 26–63**. The complex sign in Corollary 10.59.1 is taken from printed §10.58.12, not independently rederived from all spectral-sequence conventions.
- **Coverage matrix:** exactly **three** previously inventory-only §10.46/10.57/10.59 rows are advanced to **selected-passages only**. **747** unique numbered current-main ToC sections were re-counted; **zero** entire sections/chapters are certified. Previously logged resolved/unresolved/deferred cases remain unchanged.
- No Python/JS project tests, website/browser check, full build, CI, formal verification or publication ran. No source, generated HTML, canonical registry, stable tags or `main` files were changed. This report is an audit-only proposal. The author-excluded approximation/regularization and dedicated Bergman/$L^2$/Ohsawa–Takegoshi/multiscale/positivity-loss programme stays **deferred-by-user**, untouched.
