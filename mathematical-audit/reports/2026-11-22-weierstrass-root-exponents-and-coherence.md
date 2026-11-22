# 2026-11-22 — Root exponents, Weierstrass division, coherence, and convex slices

## Reviewed revision and scope

- **Production `main` SHA:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Whole current integrated reading edition, directly read:** §9.1 (`docs/sections/complex-spaces-and-modifications/index.html`, blob `65a26de54d52679ab76f293f0fc75795d38a3822`, mathematical physical lines 7–16, introductory); §9.2 (`docs/sections/complex-spaces-and-modifications--division-and-finite-analytic-modules/index.html`, blob `8f776a57a63b2917689b38f5c59b677a11cecce8`, mathematical physical lines 7–187, including all displayed statements and proofs). This is a current **direct reading**, not full transitive certification of every predecessor.
- **Selected nonexcluded cross-chapter check, not an entire section:** §19.5 Lemma 19.5.32 and the convex-slice passage of its proof, physical lines 431–469, `docs/sections/the-theory-of-okounkov-bodies--transcendental-partial-okounkov-bodies/index.html`, blob `a53c6b2f80c3775e9d646f57808425823ec4a4ac`, permanent `082A647C2B55`. The cited extension/analytic-singularity approximation inputs were **not** reopened or certified.
- **Existing-coverage cross-check only:** §19.4 Proposition 19.4.7, lines 59–107, `docs/sections/the-theory-of-okounkov-bodies--algebraic-partial-okounkov-bodies/index.html`, blob `c661e264cab0995a2a344453039940028feff8e0`, permanent `632B1323B741`. This overlap with an earlier selected §19.4 review is **not** counted as a first visit.

The current chapter pages `docs/chapters/complex-spaces/index.html` and `docs/chapters/sections-okounkov/index.html` were consulted for current section identities. The established 25-chapter/747-numbered-section inventory is preserved without pretending to have freshly checked all sections.

## New classified deduction

**POME-WEIERSTRASS-COEFFICIENT-ORDER-ROOT-EXPONENT-001 — low / verified conditional deduction.** Not a printed counterexample, not an error in Pome, and not a repair to a failed theorem.

**Precise anchor:** §9.2, the source-labeled equation `foundations-of-pluripotential-theory:1F95143C`, permanent tag `667706D7A5E8`, displayed (9.2.1), physical lines 22–29; its coefficient-vanishing hypotheses are in lines 16–19 and distinguished germs in line 32. The root separation supports the Weierstrass division proof, Proposition 9.2.2, source `foundations-of-pluripotential-theory:681BB46B`, permanent `611958EF0AB8`, physical lines 36–60.

**Statement.** Let $n\ge2$, $m\ge1$ and
\[
P(z',w)=w^m+\sum_{j=1}^{m}a_j(z')w^{m-j},
\qquad a_j\in\mathcal O_{n-1},\qquad a_j(0)=0.
\]
For each nonzero coefficient put $s_j=\operatorname{ord}_0a_j\ge1$, and set
\[
\gamma(P)=\min_{\substack{1\le j\le m\\a_j\ne0}}\frac{s_j}{j}.
\]
If at least one $a_j$ is nonzero, there exist $r,C>0$ such that every root $w$ of $P(z',\cdot)$ satisfies
\[
\boxed{|w|\le C\|z'\|^{\gamma(P)}\quad (0<\|z'\|<r).}
\]
If all the $a_j$ vanish identically, all roots are zero, so the bound holds with any positive exponent. This is a *uniform root-to-the-central-fiber bound*, not a claim of single-valued Hölder-continuous branches.

**Self-contained proof.** Fix a small Euclidean ball on which the coefficient power series converge. The first nonzero homogeneous term of each nonzero $a_j$ has degree $s_j$, so absolute convergence on a slightly larger ball gives $|a_j(z')|\le C_j\|z'\|^{s_j}$ for a common sufficiently small radius. If $P(z',w)=0$ and $|w|>2\max_j|a_j(z')|^{1/j}$, then
\[
1\le\sum_{j=1}^m\frac{|a_j(z')|}{|w|^j}
 <\sum_{j=1}^m2^{-j}<1,
\]
a contradiction. Consequently
\[
|w|\le2\max_j C_j^{1/j}\|z'\|^{s_j/j}
 \le 2\max_j C_j^{1/j}\|z'\|^{\gamma(P)}
\]
for $0<\|z'\|<\min(r,1)$, omitting zero coefficients. This proves the bound directly from the triangle inequality as well as by (9.2.1).

**Sharpness in the universal class.** For each integer $m,s\ge1$, take $P(z',w)=w^m-z_1^s$. Here $\gamma(P)=s/m$ and for $z'=(t,0,\ldots,0)$ every root has modulus $|t|^{s/m}$. No larger uniform exponent is valid for this polynomial. In particular, the general Weierstrass-polynomial hypothesis guarantees the exponent at least $1/m$, and this baseline is optimal (take $s=1$).

**Proposed optional correction/addition:** a short supplementary quantitative observation following (9.2.1), without changing the existing equation, numbering, source attribution, or tags. There is no required repair. **Affected mathematical use:** the shrinking-root and polydisc selection step in Proposition 9.2.2 (lines 54–58) and removable-extension proof of Lemma 9.2.9 (lines 176–182), with potential use for local finite-map estimates of §9.3. No full successor proof chain is certified.

## Other direct mathematical checks and unresolved inputs

1. **§9.2.2, Weierstrass division (36–60).** Checked the Cauchy integral quotient and remainder identities, their independence of the intermediate radius, degree bound, the bounded-operator estimate using the annulus outside the roots, and uniqueness via roots counted with multiplicity. The degree-zero polynomial is treated by the evident $P=1$ case. No confirmed new error.
2. **§9.2.4, Noetherianity (69–77).** Division by a distinguished polynomial reduces remainders to an $\mathcal O_{n-1}$-submodule of rank $m$; the induction does not rely on finite generation of stalks alone for sheaf assertions. No confirmed new error.
3. **§9.2.5–9.2.7, finite factors and coherence (86–148).** Checked monic factorization using uniqueness of division, the separate distinction between stalkwise and neighborhood generators, the syzygy reduction to degree-$\mu$ polynomials, and the finite holomorphic coefficient matrix. The preparatory Weierstrass theorem 5.5.2 remains an **internal upstream dependency**, not independently re-certified here.
4. **§9.2.8–9.2.9, analytic sets and normality (155–187).** Checked the connectedness hypothesis, empty-interior argument, vertical-fiber removability via an auxiliary distinguished polynomial, and the monic-equation bounded quotient argument for integrally closed $\mathcal O_n$. No confirmed new error.
5. **§19.5.32 selected (431–469).** The passage from positive slices to the zero slice is sound at the convex-geometric level: for $K$ compact and convex with minimum first coordinate $0$ and a point $b$ having $b_1>0$, each $x\in K_0$ can be approximated by $(1-t/b_1)x+(t/b_1)b\in K_t$; compactness supplies the reverse upper-limit inclusion. This checks that *specific* limiting operation, not its geometric slice formula. The printed proof **explicitly treats Theorem 19.5.4 as an external black box** and calls the extension theorem 5.18.16. These inputs remain unverified here, and no excluded extension/L²/regularization programme was opened.
6. **§19.4.7 selected repeat (59–107).** Checked the degree-normalized valuation bounds and the $m$ versus $m+1$ section-degree lattice-generation argument in the printed proof. The full flag-reduction prerequisites and earlier review history were not re-certified; this repetition contributes no new coverage count.

**Classification/accounting:** one low verified conditional deduction; zero newly confirmed false theorems or proof gaps; §9.2 one whole direct substantive mathematical reading, §9.1 one whole introductory reading, §19.5 one selected partial reading; §19.4 selected repeat only. Zero complete transitive proof-chain certifications. Previous confirmed, unresolved, and deferred records are unchanged.

**Scope exclusion:** Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion remain **deferred-by-user**, not solved or certified. No tests, builds, GitHub Actions CI, website publication, source/registry/canonicalization/tag/main changes were performed.
