# Mathematical audit: relative canonical positivity on products and cotangent rigidity over higher-dimensional tori

**Date:** 2026-11-08 (Asia/Shanghai).  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Pre-write audit head:** 44d0e322dc0121ab21d181d0ce5439a20b047fec.  
**Exact integrated reading file:** docs/sections/questions-on-relative-canonical-classes-and-cotangent-tensors/index.html; blob 7b2763d35ab776a5bb0a17a34e8a2e6b3546358f; relevant physical lines 5–12.

The original reading-edition objects are **Conjecture 24.12.1** (source label cao-paun-foliations:026DF33E; permanent tag 3E0B91E5DF69; physical line 9) and **Question 24.12.2** (source label cao-paun-foliations:54F33ABF; permanent tag 2C2AE81C4020; physical line 11). Their introductory conventions are at physical lines 6–7. The source-labelled entry pages docs/tag/3E0B91E5DF69/index.html (blob 7cff7662ed913aa4cb5cec71a24be738a9d88bbd) and docs/tag/2C2AE81C4020/index.html (blob b17b753a9bc2e48a11d2682ab6a8ff7a0a44b967) were checked against the integrated statements. Both general questions **remain open in the reading edition**; the results below address explicit, restricted product families only.

## Finding POME-RELK-P1-PRODUCT-PSEF-001

**Severity:** low. **Status:** verified conditional deduction (a proved special case, not a correction of a false conjecture or a proof of its general case). **Affected statement:** Conjecture 24.12.1, source/tag as above.

**Precise statement.** Let \(Y\) be a connected compact Kähler manifold of positive dimension \(q\), \(X=Y\times\mathbb P^1\), \(p=\operatorname{pr}_Y\), \(r=\operatorname{pr}_{\mathbb P^1}\), and let \(L\) be **any pseudoeffective holomorphic line bundle** on \(X\), without a splitting assumption. If the relative adjoint \(K_{X_y}\otimes L|_{X_y}\) is pseudoeffective for a (hence every) projective-line fiber, then \(K_{X/Y}\otimes L\) is pseudoeffective. In particular, Conjecture 24.12.1 holds for these product fibrations, **without using** the additional trivial-multiplier-ideal assumption. This does not address general nontrivial fibrations.

**Complete proof.** Normalize a Fubini–Study Kähler form \(\eta\) on \(\mathbb P^1\) by \(\int_{\mathbb P^1}\eta=1\). Let \(d=\deg(L|_{\{y\}\times\mathbb P^1})\), independent of \(y\) because it is a topological fiber intersection number. The fiberwise hypothesis reads \(\deg K_{\mathbb P^1}+d=d-2\ge0\), i.e. \(d\ge2\).

The real degree-two Künneth decomposition, using \(H^1(\mathbb P^1,\mathbb R)=0\), gives a unique real class \(a\in H^{1,1}(Y,\mathbb R)\) such that
\[
 c_1(L)=p^*a+d\,r^*[\eta].
\]
For a positive closed \((1,1)\)-current \(T\) in \(c_1(L)\), form the proper pushforward
\[
 S=p_*\bigl(T\wedge r^*\eta\bigr).
\]
This is a well-defined positive closed \((1,1)\)-current on \(Y\): the wedge is with a **smooth** semipositive form, so no singular product or regularization is used. Its class is exactly
\[
 [S]=p_*(c_1(L)\smile r^*[\eta])=a,
\]
since \([\eta]^2=0\) on \(\mathbb P^1\), and integration along the fiber of \(r^*\eta\) is one. Thus \(a\) is pseudoeffective. Finally
\[
 K_{X/Y}=r^*\mathcal O_{\mathbb P^1}(-2),\quad
 c_1(K_{X/Y}\otimes L)=p^*a+(d-2)r^*[\eta].
\]
The explicitly positive closed representative \(p^*S+(d-2)r^*\eta\) proves the claim.

**Risk and exact boundary:** This argument uses both the product projection and the one-dimensional fiber cohomology; it cannot be applied unchanged to a general smooth fibration (no global fiber-class decomposition), let alone a singular or non-equidimensional map. In particular it does **not** resolve the conjectural global metric-gluing step identified in the reading edition. The distinction between a pseudoeffective cohomology class and a smooth semipositive metric is respected: we only assert existence of a positive current.

**Suggested optional addition:** a separate product-case lemma under the original conjecture, retaining the conjecture, source tag, and historical attribution. No dependency on excluded Demailly approximation/regularization, Bergman kernels, weighted L2, Ohsawa–Takegoshi, multiscale atlases, or positivity-loss methods.

## Finding POME-MRC-TORUS-P1-COTENSOR-RIGIDITY-001

**Severity:** low. **Status:** verified conditional deduction. **Affected statement:** open Question 24.12.2, source/tag as above. This is **not** a duplicate of the prior POME-MRC-PROJECTIVE-CURVE-COTENSOR-001: that report treats \(\mathbb P^r\times C\) with a **curve** quotient \(C\), whereas this proof handles a torus quotient of **arbitrary complex dimension at least two** and avoids projective-bundle Picard splitting.

**Precise statement.** Let \(A\) be a compact complex torus of dimension \(q\ge2\), let \(X=A\times\mathbb P^1\), and let \(L\) be a pseudoeffective line bundle admitting a nonzero morphism of coherent sheaves
\[
 L\longrightarrow(\Omega_X^1)^{\otimes m},\qquad m\ge1.
\]
Then **\(L\simeq\mathcal O_X\)**. The projection \(X\to A\) is the maximal rationally connected quotient, so the proposed inequality of Question 24.12.2 holds with equality:
\[
 \nu(X,L)=0=\nu(A,K_A).
\]
A nonzero morphism from a line bundle to a locally free sheaf is an injection of sheaves on this connected smooth manifold, so the morphism formulation is equivalent here.

**Complete proof.** Every holomorphic one-form on a complex torus is translation invariant, hence \(\Omega_A^1\simeq\mathcal O_A^{\oplus q}\). On \(X\),
\[
 \Omega_X^1\simeq\mathcal O_X^{\oplus q}\oplus r^*\mathcal O_{\mathbb P^1}(-2),
\]
and the tensor-power decomposition has summands
\[
 r^*\mathcal O_{\mathbb P^1}(-2j)^{\oplus {m\choose j}q^{m-j}},
 \qquad j=0,\ldots,m.
\]

Let \(d=\deg L|_{\{a\}\times\mathbb P^1}\). Since \(L\) is pseudoeffective, pick a positive closed current \(T\in c_1(L)\). With a Kähler form \(\omega_A\) on \(A\), positivity of the smooth semipositive test form gives
\[
 0\le\int_X T\wedge p^*(\omega_A^q)
  =d\,\int_A\omega_A^q,
\]
so \(d\ge0\); no restriction of the possibly singular \(T\) to a fiber is invoked. For \(j\ge1\), every component of the morphism into \(r^*\mathcal O(-2j)\) is a section of \(L^{-1}\otimes r^*\mathcal O(-2j)\). Its restriction to every projective-line fiber belongs to
\[
 H^0\bigl(\mathbb P^1,\mathcal O(-d-2j)\bigr)=0.
\]
Hence **all components with \(j\ge1\) vanish globally**. Nonvanishing forces a component into one of the \(j=0\) trivial summands, which is a nonzero global holomorphic section \(s\in H^0(X,L^{-1})\).

Let \(D=\operatorname{div}(s)\) be its effective Cartier divisor (possibly empty). Poincaré–Lelong gives \([D]=-c_1(L)\), while \(T\) positively represents \(c_1(L)\). On the compact Kähler manifold \(X\), with any Kähler form \(\omega_X\),
\[
 0=\int_X(T+[D])\wedge\omega_X^q.
\]
Both contributions are nonnegative. Every nonzero effective divisor has strictly positive \(\omega_X\)-volume, so \(D=\varnothing\). A holomorphic line-bundle section cannot have a nonempty zero set of codimension at least two; its zero set, when nonempty, is divisorial. Thus \(s\) is nowhere vanishing and \(L^{-1}\simeq\mathcal O_X\).

Every holomorphic image of \(\mathbb P^1\) in \(A\) is constant: the map lifts to the universal cover \(\mathbb C^q\), where its coordinate functions are constant by compactness. All rational curves in \(X\) therefore lie in the projective-line fibers, and each such fiber is rationally connected; the projection is the MRC quotient. Both \(K_A\) and \(L\) are trivial, so both numerical dimensions are zero in the reading edition's positive-intersection convention. This verifies the stated special case only.

**Risk and exact boundary:** The proof uses the trivial cotangent bundle of the **torus**, not just \(K_A\simeq\mathcal O_A\); it cannot be transported unchanged to Calabi–Yau bases with nontrivial cotangent or to arbitrary MRC maps. No assertion about all compact Kähler manifolds or general numerical dimensions is made. The old \(\mathbb P^r\times C\) result and its permanent labels remain untouched.

**Suggested optional addition:** one high-dimensional torus-base example below Question 24.12.2, with explicit cross-reference to the previous projective-curve model, not a duplicate theorem registration.

## Coverage, classification and dependence

- **Actually inspected:** the complete two printed conjecture/question statements and their introductory conventions in integrated §24.12, exact lines 5–12; the two corresponding tag pages for source labels; the previous 2026-10-28 projective-curve cotensor report to check for genuine novelty.
- **Not inspected or certified:** proofs of general MRC quotient theory, general relative canonical positivity, any nonsplit fibration, unrelated chapters, or every mathematical statement in §24.12. No false printed theorem identified; both statements remain explicitly open in general.
- **Established internal primitives used:** positive-current representation of pseudoeffectivity, smooth-form wedge and proper pushforward, Poincaré–Lelong, Kähler volume positivity, and standard product cohomology. These short arguments are written explicitly above; there is no new deep external analytic input. The MRC terminology is only used to identify the elementary product quotient.
- **Classification:** both new IDs are low / verified conditional deduction, not verified repairs of a theorem, not a proof-gap closure, not a general conjecture solution. All earlier confirmed errors, proof gaps, external dependencies, and **deferred-by-user** exclusions keep their existing statuses.
- **Whole-project count:** the pre-existing current-main matrix inventories 25 chapters, 747 numbered sections, and 0 completely mathematically certified sections. §24.12 was already first sampled on 2026-10-28, so this is **0 new first-section visits**, **0 newly certified whole sections**, with new selected proof cases added for both printed questions.
- **No production writes:** proposed future reading additions only; no main/source/registry/permanent-tag changes, builds, tests, formal verification, CI, PR merge, or website publication.
