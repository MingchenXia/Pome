# 2026-10-24 — Gauduchon matrix estimates, malformed split equations, and strict adjoint-measure monotonicity

## Provenance, scope, and boundaries

- **Reviewed branch and immutable main commit:** \`main\` at \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
- **Reading edition actually inspected:** \`docs/sections/smooth-monge-ampere-equations--the-matrix-structure-of-the-gauduchon-equation/index.html\` (§14.13), \`--the-largest-eigenvalue-estimate\` (§14.14), \`--a-liouville-theorem-for-the-limiting-cone\` (§14.15), \`--the-gradient-bound-by-rescaling\` (§14.16), \`--existence-for-the-gauduchon-ansatz\` (§14.17), and \`--normalization-for-the-gauduchon-equation\` (§14.18), with the common \`docs/sections/smooth-monge-ampere-equations\` path prefix. The fully qualified paths and blob hashes are in the table below.
- **Cross-checked prerequisites, without re-certifying them:** connectedness and smooth existence in Theorem 14.10.1 (source \`non-kahler-pluripotential-theory-3E8336C1\`, permanent tag \`76AF759A4024\`); the one-dimensional adjoint kernel and positive probability measure in Proposition 14.12.1 (source \`non-kahler-pluripotential-theory-1A082A94\`, tag \`706EB82AB6A2\`).
- **Review method:** read the integrated current mathematical statements and displayed proofs; compare complete displays with standalone permanent-tag displays, inspect the exact TeX tokens, verify the matrix/linearization implications algebraically, and run exact-string checks against freshly fetched main blobs. This is **selected proof review**, not full certification of Evans–Krylov, the full largest-eigenvalue proof, the Liouville induction, the continuity-method chain, or any chapter.
- **Excluded:** all Demailly approximation/regularization, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion material is **deferred-by-user**, not certified, reopened, or claimed resolved. No unpublished source material is reproduced here.

| Section | Integrated HTML blob SHA | Inspected paragraph/line anchors |
| --- | --- | --- |
| §14.13, section tag \`53E844FE515C\` | \`6e1faedde219b856c0bf5ecaf566403ae999772e\` | lines 10–35, 38–49, 54–105, 113–155, 159–178, 180 |
| §14.14, section tag \`148E6041EC3F\` | \`52e695d43ee0597b675b7a5edff336d5610d5729\` | lines 13–55, 58–93, 95–127, 130–183, 185–256, 257–277, 281 |
| §14.15, section tag \`D4DE203BE3BF\` | \`2a5f42ad68db1f5091a0c2e0c5a29e2c3887cdec\` | lines 13–46, 51–153 |
| §14.16, section tag \`40669ABC11F8\` | \`4081db05fb0a989451c4e536f8e285501c399e81\` | lines 10–19, 24–73 |
| §14.17, section tag \`6904C64D5831\` | \`cc78a3bf05b3a384737ab0bfac89c68e594400e8\` | lines 10–54, 59–73 |
| §14.18, section tag \`9C1043361EBF\` | \`07303e817cd642d6f34b8ff2c1b876a4b299c4ac\` | lines 10–18, 22–77 |

## POME-GAUD-ALIGN-SPLIT-001 — confirmed reading-edition error; duplicated, incomplete permanent-tag formulae

**Severity: medium. Status: confirmed error in integration/permalink rendering; mathematical theorem status unaffected.**

Three displayed multi-line formulae occur **completely in the containing mathematical proof** but are separately exported again as an **incomplete trailing continuation**, each wrapped as
\`\[\begin{aligned}\begin{align} ... \end{align}\end{aligned}\]\`.
The inner alignment environment is incorrectly nested, and the content begins with \`& +\` or \`& -\`, missing the left-hand side and the first row. Thus the individually addressable equation tags do not contain the complete equation; the section view also contains a spurious second fragment.

1. **Equation 14.13.3.** The full, two-line expression for \`2(n-1)Z_{i\bar j}\` occurs at \`docs/sections/smooth-monge-ampere-equations--the-matrix-structure-of-the-gauduchon-equation/index.html:40–43\` (source Lemma \`non-kahler-pluripotential-theory-57B6169B\`, permanent tag \`6168D5D4EF96\`). At physical **line 180** another reading chunk \`entry-A6EC7DDEACFB\` gives only the conjugate-gradient second row, without \`2(n-1)Z_{i\bar j}\` or the first row. It carries source label \`non-kahler-pluripotential-theory-8A591D0B\`; standalone permanent page \`docs/tag/A6EC7DDEACFB/index.html\` has blob \`9f64527b257bb380c10a060d75d1cac71ab684ec\` and contains only that malformed fragment.
2. **Equation 14.14.5.** The full largest-eigenvalue second-derivative inequality occurs at \`docs/sections/smooth-monge-ampere-equations--the-largest-eigenvalue-estimate/index.html:88–91\`. Another chunk at physical **line 281**, \`entry-143977813E90\`, source \`non-kahler-pluripotential-theory-400F3D73\`, consists only of the second alignment line, beginning with \`& +\`. The independent permalink \`docs/tag/143977813E90/index.html\` (blob \`452aa95b9de38ed3a7ed87ef56af5db57af8b077\`) reproduces this fragment.
3. **Equation 14.14.10.** The complete two-line inequality occurs at \`docs/sections/smooth-monge-ampere-equations--the-largest-eigenvalue-estimate/index.html:155–160\`, but \`entry-D807F632DAD7\` at **line 281**, source \`non-kahler-pluripotential-theory-988193F6\`, exports only the negative error term. The independent permalink \`docs/tag/D807F632DAD7/index.html\` (blob \`340c4cc41e4ab63a9ee9cbfbba0ab0ed24c28429\`) reproduces that malformed tail.

**Reproduction:** on the pinned HTML blobs, locate respectively \`id="entry-A6EC7DDEACFB"\`, \`id="entry-143977813E90"\`, \`id="entry-D807F632DAD7"\`; each contains \`\[\begin{aligned}\begin{align}\` and only the last row. Independently inspect the earlier complete \`align\` in each section. The accompanying small read-only Python check reproduces the exact three pairs and the derivative-glyph defect below. In-memory assertions of these source features were actually performed; no browser MathJax build has been run.

**Precise proposed repair (not applied):** attach all three stable source labels/permanent tags to the **complete** corresponding displays, expose those complete displays on their \`/tag/\` pages, and remove the three redundant tail-only reading chunks. Preserve original source labels, canonical full formulae and all incoming permalinks; do **not** erase the tags or assume this is a duplicate mathematical theorem. Check the underlying split-alignment extraction logic for other sources before any integrator patch. Affected dependents are the individual formula permalink views and reference readers of §§14.13–14.14; no conclusion that the PDE theorem itself is false.

## POME-GAUD-SECOND-DERIV-GLYPH-001 — confirmed second-derivative notation defect

**Severity: low. Status: confirmed error in printed TeX/notation, not a false inequality.**

At \`docs/sections/smooth-monge-ampere-equations--the-largest-eigenvalue-estimate/index.html:90\` in **Equation 14.14.5**, the displayed symbols are literally \`\phi ”|V_k|^2+\psi ”|v_k|^2\`, using a Unicode right double quotation mark \`U+201D\` after \`\phi\` and \`\psi\`, **not** the expected second derivatives \`\phi''\` and \`\psi''\`. At physical **line 190** in §14.14.12 there is also \`-2\delta\phi ”\sum_{k\in I}\cdots\` where \`-2\delta\phi''\` is required. The partial duplicate at line 281 repeats the first defect but does not constitute a third independent proof line.

The interpretation is forced by §14.14 line 37 (\`\phi''=2(\phi')^2\`), the second-derivative expansion, the cancellation at lines 187–199, and the correctly written \`\phi''\` in the first row of line 190. **Repair:** replace those three erroneous instances with the exact second-derivative tokens; separately cure the fragment duplication in the previous finding. These are source/reading-edition patch recommendations only, not performed in this audit.

## POME-GAUD-ADJOINT-GRADIENT-MONO-001 — strictly monotone normalized adjoint measures

**Severity: low. Status: verified conditional deduction; not a printed error.**

Assume the standing hypotheses of Theorems 14.10.1 and 14.18.2: a **connected** compact complex manifold \`X\` of dimension \`n>=2\`, fixed smooth Hermitian \`\gamma_0\`, fixed smooth **Gauduchon** \`\gamma\`, and arbitrary smooth real functions \`F,G\`. The smooth solution exists uniquely up to additive normalization. Write \`b(F)=b_\gamma(F)\` and \`\mu_F=\mu_{u_F}^\gamma\` for the probability measure of Proposition 14.12.1. Put \`H=G-F\`, \`F_t=F+tH\`, and let \`Q_t>0\` be the §14.13 matrix of the solution at \`F_t\`.

Set
\[
\mathcal K(t)=\frac{1}{n-1}\int_X
\operatorname{tr}\bigl((Q_t^{-1}\dot Q_t)^2\bigr)\,d\mu_{F_t}\geq0.
\]
Theorem 14.18.2, source label \`non-kahler-pluripotential-theory-67056566\`, permanent tag \`F90961841CA0\`, at \`docs/sections/smooth-monge-ampere-equations--normalization-for-the-gauduchon-equation/index.html:31–61\`, gives
\[
\frac{d}{dt}[-b(F_t)]=\int_XH\,d\mu_{F_t},
\qquad
\frac{d^2}{dt^2}[-b(F_t)]=\mathcal K(t).
\]
Integrating the second identity yields the **exact monotonicity and Bregman identities**
\[
\boxed{\int_X H\,d(\mu_G-\mu_F)
=\int_0^1\mathcal K(t)\,dt,}
\]
\[
\boxed{-b(G)+b(F)-\int_X H\,d\mu_F
=\int_0^1(1-t)\mathcal K(t)\,dt.}
\]
The right sides vanish if \`H\` is constant, and are **strictly positive whenever \`H\` is nonconstant**. Indeed, at any parameter \`t\`, if \`\mathcal K(t)=0\`, positivity of \`\mu_{F_t}\` and smoothness force \`\dot Q_t=0\`. Differentiation of the defining equation then gives \`\mathcal L_{u_t}\dot u_t=0\`. The maximum principle/adjoint-kernel statement of Proposition 14.12.1 makes \`\dot u_t\` constant, so \`H+\dot b(F_t)=0\` on connected \`X\`; hence \`H\` must be constant. Thus for nonconstant \`H\`, \`\mathcal K(t)>0\` at every \`t\`.

**Consequences:** the map \`F -> \mu_F\` is **injective modulo constants**: \`\mu_F=\mu_G\` implies \`F-G\` constant, and conversely adding a constant to \`F\` only changes \`b\` and leaves the solution and the adjoint probability unchanged. The functional \`A(F)=-b(F)\` has a strictly positive Bregman divergence on the quotient \`C^\infty(X,R)/R\`. This is not a claim of quantitative uniform convexity in a fixed norm or of existence for nonsmooth \`F\`.

As a sign/normalization cross-check, for \`n=2\` Example 14.18.3 gives \`d\mu_F=e^F\gamma^2/\int e^F\gamma^2\`; the derivative of \`\int H\,d\mu_{F_t}\` equals the variance of \`H\` and is strictly positive for nonconstant \`H\`, agreeing with the general identity.

**Proposed optional corollary:** add the gradient-map injectivity and Bregman identity near Theorem 14.18.2 (reviewable separately; do not modify main/registry here). Dependent areas: smooth Gauduchon normalization and convex dual descriptions of adjoint probability measures. No regularization theorem is needed.

## Additional proof-level checks, genuine dependencies, and coverage limits

- **§14.13:** verified the algebraic self-adjointness of \`P_\gamma\`, \`\sum_i f_i\lambda_i=n\`, \`\sum_i f_i\chi_{i\bar i}=\sum_i t_i(Q_0)_{i\bar i}\`, and the eigenvalue-order/coercivity argument in Lemma 14.13.5. Inspected the torsion missing-index computation and its derivative exclusions, but did not independently rederive every Chern-frame antisymmetrization coefficient. The detached mathematical tag display is the separate **confirmed integration defect** above.
- **§14.14:** inspected the exact test function \`H=log lambda_1+phi(|dv|^2)+psi(v)\`, simple-eigenvalue perturbation, equations 14.14.5, 14.14.8–11 and the two cases 14.14.12–15. The potential dependence on the full torsion cancellation and nonlinear eigenvalue commutator chain **remains conditional**; no full second-order estimate is certified. The glyph error is not a counterexample to the intended estimate.
- **§14.15:** checked the cone map \`P_n\`, dimension reduction, viscosity maximality comparison, spherical-mean limit for bounded subharmonic \`v,v^2\`, directional-energy alternative, and construction of a strict admissible comparison. The translated compactness uses an actual subsequence of globally uniformly Lipschitz functions, not an unjustified arbitrary-net reduction. The complete Liouville theorem still relies on the printed differential/viscosity proof and earlier bounded-PSH Liouville input, not independently re-certified here.
- **§14.16:** checked gradient blowup scaling: background terms become \`O(A_j^-2)\`, first-order terms \`O(A_j^-1)\`, and \`det(A_j^-2Q_j)->0\`; the contradiction requires \`C^1\` local compactness from elliptic \`W^{2,p}\` estimates. These *standard* analytic estimates were not reproved here.
- **§14.17:** inspected the eigenvalue compactness from upper bounds and determinant lower bound; the infimum of tangent \`log det\` planes gives a concave uniformly elliptic extension on real symmetric matrices, after the positive complex-Hessian projection. The Evans–Krylov and Schauder estimates invoked at lines 45–53 are **genuine external analytic inputs until internally certified/replaced**; their mention is not a new assertion that the displayed proof is false. The internal \`section 25.6\` locator appearing there warrants content-based checking because chapter 25 is currently historical notes; do not silently equate an old source locator with a current Pome theorem number.
- **§14.18:** directly checked first and second derivatives of \`log det\`, the adjoint integration identity, strictness modulo constants, \`1\`-Lipschitz dependence of \`b\` on \`F\`, and the dimension-two mass formula. Smoothness of solution families depends on §§14.10, 14.12, 14.17 and the corresponding standard elliptic machinery.

The **whole six-section scope has not been certified**, and no result from the excluded user-deferred approximation programme was reopened. No source, mathematical body, registry, canonicalization, permanent tag, publication, or main branch was edited. No Python/JavaScript project tests, full build, UI rendering check, GitHub Actions, or formal verifier were run; the in-memory text assertions above are the only checks performed.
