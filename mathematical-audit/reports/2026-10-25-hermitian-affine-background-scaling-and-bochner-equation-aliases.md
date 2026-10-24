# 2026-10-25 — exact Hermitian affine-background scaling and Bochner equation aliases

**Reviewed current main:** b6933b772f41b45918f7e25ed1afbbb1fd892272 (2026-10-23 main publication). **UTC work checkpoint:** 2026-10-24T22:00:23Z. **Starting review branch:** a39f45b7822dae58363717e50b38d6872e9eba8f. Documentation reviewed: main AGENTS.md and documentation/proof-expansions.md, review README.md, LATEST.md, LEDGER.md, SECTION_MATRIX.md. All work below concerns the actual integrated main reading edition, not source-number guesses.

**Actual selected coverage (new, not complete section certifications):** §§11.37–11.40 (entropy variational formula, Hermitian mass/entropy dual bounds, ordinary-type comparison and weak supporting-measure stability, background change), and §11.48 (selected Hermitian-torsion algebraic commutator and curvature-energy formulas, **not** a complete proof). Context-only: §11.42 (closed-class mass and distinct divisorial reference examples). No other section is newly marked proof-reviewed. Existing 747-entry main ToC remains the inventory. In particular, no dedicated Demailly approximation/regularization, Bergman, L2, Ohsawa–Takegoshi, multiscale atlas, or positivity-loss proof-completion work was reopened; historical records remain deferred-by-user.

## POME-HERM-BOCHNER-EQUATION-ALIASES-001 — medium / confirmed error in reading integration

**Source and location:** docs/sections/hermitian-torsion-and-the-bochner-identity/index.html, main blob 4656b430de6ec989ef121eca550afda0be407222; underlying source namespace demailly-complex-geometry; Theorem 11.48.3 permanent tag 9C30D850C771, Lemma 11.48.9 tag A9F492A7F5C3, Theorem 11.48.15 tag E96E372480D4. The complete grouped displays are in physical HTML lines 24–28 (Eqs. 11.48.4–5; canonical grouped tag 8C926C4A6B4A), 98–106 (Eqs. 11.48.10–12; grouped tag CE861F2B34DA), and 155–163 (Eqs. 11.48.16–18; grouped tag 2F5B471E480A).

At physical line 247, **five additional independent permanent-tag entries** are emitted in duplicate: Eq. 11.48.5 tag 1E5D7A00D2DA, Eq. 11.48.11 tag CE84427B9DD6, Eq. 11.48.12 tag 727926BD3A70, Eq. 11.48.17 tag 5FE7DC3167AF, Eq. 11.48.18 tag CC4EDB6E65CB. Their display payloads begin with an invalid nested pair of TeX environments: begin-aligned immediately enclosing begin-align, with end-align inside end-aligned and enclosing display delimiters. One duplicate also retains a terminal alignment line break despite having only one row. The full mathematical equation rows already occur earlier under their containing statements; the second set is neither a new theorem nor a mathematically different version.

**Disposition:** confirmed erroneous stand-alone mathematical rendering/canonicalization, not a false Bochner identity. **Proposed correction (not applied):** preserve all five permanent entry tags, the grouped tags, source provenance and original theorem formulas; map each independent tag to its exact full canonical equation row or provide a valid stand-alone single-row display. Suppress only duplicate malformed reading chunks after checking navigation/link targets and original attribution. **Dependents:** MathJax rendering, row-level permalinks, permanent tag navigation, and source-to-reader alignment. This is a new group of five observed instances of the previously recorded general exporter defect; existing Gauduchon and classical-product findings are not counted as new here.

## POME-HERM-BOCHNER-DOUBLEPRIME-001 — low / confirmed notation error

**Source and location:** the same main blob, physical lines 27 and 162; independently duplicated at line 247. In the displayed second commutator of Eq. 11.48.5, the right side contains literal Unicode U+201D after a delta symbol (TeX text delta followed by a right double quotation mark) where the formal adjoint delta with a double prime is required. In Eq. 11.48.18, the last Laplacian is likewise written Delta followed by U+201D. The *same* theorem uses properly TeX-encoded double-prime operators in Eqs. 11.48.4, 11.48.16 and 11.48.17 and throughout the adjacent proof. In particular Eq. 11.48.18 is the decomposition of the full twisted Laplacian into the twisted primed and untwisted double-primed Laplacians; a quotation mark cannot denote the latter.

**Disposition:** two confirmed incorrect mathematical glyphs in the canonical reading equation, not a counterexample to their intended identities. **Proposed correction (not applied):** replace the right-double-quotation character after delta and Delta by their respective TeX double primes in both canonical rows and their stand-alone aliases, retaining all original tags. **Dependents:** exact meaning, MathJax/search output, and later proof references to the Kähler-type identities.

## POME-HERM-BACKGROUND-AFFINE-SCALING-001 — low / verified conditional deduction, not a false statement

**Source and location:** Theorem 11.40.1 and Eq. 11.40.2, source as integrated in docs/sections/normalization-and-weak-adjoint-measures--varying-positive-backgrounds/index.html, main blob 7ad25146c373ced93115f4a239f2312d645fcfe1, physical lines 20–37; permanent theorem tag 133439CA2DC1 and formula tag 2E9A16E3BAFF. Context: dual/scalar discussion of §§11.37–11.39, especially Proposition 11.38.3 (tag A3720120A48C, docs/sections/normalization-and-weak-adjoint-measures--entropy-bounds/index.html, main blob d124ce19af09af2d0a65d655fe611e7b45804c3d, physical lines 60–90) and Eq. 11.40.5 (tag B7921C3AB602, main blob above, lines 89–96).

**Precise statement.** Let X be compact and connected of complex dimension n >= 1, fix a smooth positive reference volume dV, and let beta and beta' be positive smooth Hermitian (1,1)-forms related by

\[
\beta'=c\,\beta+dd^c h,\qquad c>0,\quad h\in C^\infty(X,\mathbb R).
\]

For every bounded real measurable F, assuming the existing existence/uniqueness of the normalized bounded Hermitian Monge–Ampère equation, the scalar functional obeys the **exact** identity

\[
B_{\beta'}(F)=B_\beta(F)+n\log c.
\]

Consequently, for every probability measure nu, including the infinite-value cases,

\[
H_{\beta'}(\nu)=H_\beta(\nu)+n\log c,
\]

and for every F the supporting-probability sets are identical:

\[
\mathcal A_{\beta'}(F)=\mathcal A_\beta(F).
\]

The sup-uniform scalar distance of §11.40 is therefore exactly n|log c|, whereas the probability support map cannot distinguish the two backgrounds. The lower/upper bounded-potential masses satisfy, with extended values allowed,

\[
v_-(\beta')=c^n v_-(\beta),\qquad v_+(\beta')=c^n v_+(\beta).
\]

**Complete argument independent of regularization.** If u is any bounded beta-psh solution with positive current Omega=beta+dd^c u, define u'=cu-h. Then u' is bounded and

\[
\beta'+dd^c u'=c(\beta+dd^c u)=c\Omega,
\qquad
(\beta'+dd^c u')^n=c^n\Omega^n.
\]

Thus a solution with right-hand side exp(B_beta(F)+F)dV maps to one with exp(B_beta(F)+n log c+F)dV. Subtracting a constant from u' if a zero-mean or supremum normalization is imposed does not affect the equation or its ordinary bounded class. The uniqueness of the normalization scalar yields the claimed equality of B. In the dual definition H(nu)=sup_G(B(G)+integral G dnu), the scalar shift passes outside the supremum; the definition of supporting probability as equality in H(nu)-integral F dnu >= B(F) then shows the sets are identical. Finally, u -> cu-h is a bijection of bounded positive-potential competitors, and its inverse is (u'+h)/c; every Monge–Ampère total mass is multiplied by c^n, proving both mass identities even when their extrema are zero or infinite. The exact scalar distance follows by taking the uniform supremum of a constant.

**Significance and boundaries.** This is an exact *affine dd^c gauge plus scale* statement for possibly **nonclosed** Hermitian backgrounds, not an assumption that background mass is cohomological. It demonstrates sharpness of both endpoints of Eq. 11.40.2 (take h=0 and c=1+-epsilon for the applicable endpoint) and is consistent with §11.38.3's mass/entropy dual extremal formula. In the special case c=1 the entire scalar, dual and supporting-data collection is unchanged, even for nonidentical positive representatives. A proposed optional corollary after Theorem 11.40.1 is justified, conditional only on the already printed existence/uniqueness theory; no main/source/body/tag change was made.

## Independent selected proof checks and limits

- **§11.37 (entropy):** directly inspected Lemma 11.37.1 tag 2E4E82F8C3FC, physical lines 20–49, source main HTML blob 0710d0732ae7ef81de3d3d62206a0f9c6b5d321f. Its singular-measure continuous cutoff and finite/infinite entropy truncation passages were checked in the stated compact setting. Proposition 11.37.3, tag 33DF3CE1122A, lines 65–86, uses the closed-background fixed-mass premise conditionally; not independently certified.
- **§11.38 (entropy bounds):** inspected Proposition 11.38.1 tag 170451FB65CB, lines 11–47, and Proposition 11.38.3 tag A3720120A48C, lines 60–90. The dual lower/upper inequalities and smooth Gibbs/adjoint sharpness argument were checked conditionally on the printed bounded-density scalar estimate, the fixed trace estimate, and the smooth approximation-to-mass statement; none of these inputs was reopened as an excluded approximation program.
- **§11.39 (types and supports):** inspected Proposition 11.39.1 tag 675DA440E964, lines 11–39; Proposition 11.39.4 tag 7DD0741AE5AA, lines 56–75; Proposition 11.39.5 tag 80C599ADD5CB, lines 80–100; source docs/sections/normalization-and-weak-adjoint-measures--changing-the-prescribed-singularities/index.html, blob e603564ec54844bb2af8483249f427266ef5d83b. The strict-domination and uniform-integrability premises were used only in their declared scopes. No claim of whole-section or upstream PDE certification.
- **§11.40 (positive-background changes):** independently reconstructed the affine scaling proof above and inspected Theorem 11.40.1, Corollary 11.40.3 and Proposition 11.40.4 at lines 20–96. The implicit-function/Fredholm and elliptic regularity claims are upstream inputs, not newly proved here.
- **§11.48 (torsion algebra):** inspected grouped §11.48.3, Lemma 11.48.9, Theorem 11.48.15, Corollaries 11.48.20–21 (physical lines 24–28, 98–149, 155–221, 227–244), recording only the two confirmed rendering/notation defects above. Separately an **exact 16-by-16 exterior-algebra matrix check for n=2** (not a full proof in arbitrary dimension) used creation/contraction operators, Lambda=-i sum(bar-iota_j iota_j), and a=(theta1 theta2 bar-theta1)+(2+i)(theta1 theta2 bar-theta2). It verified both [L,tau]=3a and [Lambda,tau]=-2i bar-tau-adjoint, with tau=[Lambda,a]. This is evidence about those **selected algebraic instances only**, not a claim of a complete Hermitian Bochner, elliptic or L2 proof. The dedicated excluded L2/Ohsawa–Takegoshi programme was not continued.

**Status distinctions and permissions:** the two medium/low confirmed defects are mathematical **reading/rendering defects**; the affine scaling is a fully justified **conditional deduction**, not a missing-proof or false-theorem allegation. All prior issues, including deferred-by-user approximation items, remain unchanged. Proposed source/renderer repairs are **not applied**. No CI, publication, website edit, source-repository edit, full build, formalization or complete section theorem verification was performed.
