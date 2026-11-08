# Square-zero Banach ideals: exact subnuclearity dichotomy for finite-dimensional character modules

**Stable finding ID:** POME-RELNUC-SQUAREZERO-CHARACTER-DICHOTOMY-001  
**Severity / classification:** low / verified conditional deduction. This is an extension of a correct printed example, NOT a false theorem or a complete certification of upstream nuclear-space theorems.  
**Production main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting audit branch head:** 8eaecc1cfecc5f179d31392311ed9db757607725.

**Integrated reading edition:** docs/sections/relative-nuclear-maps-and-composition/index.html, blob b426cb8cb38d4c1b66611ac9f8cb87b35406aca9. Section 9.68 has permanent tag 054AFF2CD121. Its definition is at physical line 7. Proposition 9.68.1, source label demailly-complex-geometry:FCE8E21F, permanent tag DB4C2E622157, is at lines 10–26. Example 9.68.2, source label demailly-complex-geometry:E95AA863, permanent tag FECBDA82D7CC, is at lines 30–64.

## The new precise statement

Let B be ANY complex Banach space, including zero. Form the unital commutative square-zero Banach algebra A = C ⊕ B, with product (c,b)(d,e) = (cd, ce+db), norm |c|+||b||, and character q(c,b)=c. Fix integers m,r >= 1, and let S=C^m and F=C^r be A-modules via a·v=q(a)v.

**Dichotomy:** An A-linear map T:S -> F is A-subnuclear, using precisely the definition at integrated §9.68 line 7, **if and only if** B is finite-dimensional OR T=0.

When B is infinite-dimensional and T is nonzero, there are an A-subnuclear f:E -> F, with the NON-nuclear Fréchet A-module E=A ⊕ S, and a continuous A-linear inclusion u:S -> E, such that f∘u=T. Thus failure of arbitrary precomposition persists for every infinite-dimensional complex Banach square-zero ideal and every positive finite rank, not only the one-dimensional character-module case with B=ell^2 printed in Example 9.68.2.

## Complete proof

**1. Infinite-dimensional Banach B cannot be nuclear Fréchet.** For a Banach topology, all defining seminorms are bounded by a constant times its Banach norm; conversely, continuity of the Banach norm in the same Fréchet topology bounds it by some late defining seminorm. Hence sufficiently late defining seminorm completions are isomorphic to B. A nuclear system of defining seminorms would make an identity map between equivalent Banach norms nuclear and hence compact by internal Lemma 2.13.1. The identity of an infinite-dimensional Banach space cannot be compact: inductively choose separated unit vectors outside finite-dimensional spans by the elementary Riesz-lemma argument. In particular, by internal Theorem 2.13.3, a nuclear Fréchet space cannot have a closed subspace linearly homeomorphic to B.

**2. Obstruction to nonzero character coefficients.** Suppose B is infinite-dimensional, N is a nuclear Fréchet A-module, and ξ:N -> A is continuous and A-linear. If q(ξ(v))=c != 0 for some v in N, define L:B -> N by L(b)=(0,b)·v. Joint continuity of the module action makes L bounded/continuous. Square-zero multiplication and A-linearity give ξ(L(b))=(0,cb). The continuous map R=c^(-1) pr_B∘ξ:N -> B is a left inverse to L. Consequently LR is a continuous projection with closed range L(B), and L(B) is homeomorphic to the infinite-dimensional Banach space B. This contradicts the nuclear closed-subspace permanence used in step 1. Therefore q∘ξ=0 for every such coefficient map.

**3. Subnuclear maps with finite-dimensional nuclear source.** Every A-nuclear map from nuclear N to a character module F is zero: write its series as a summable combination of vectors multiplied by A-linear coefficient maps ξ_j:N -> A; every term acts through q∘ξ_j=0, by step 2. If T:S -> F were A-subnuclear and S is finite-dimensional nuclear, the *extra covering clause* in §9.68 line 7 would require an open surjective covering p:N -> S with nuclear N, and Tp A-nuclear. Hence Tp=0, forcing T=0 because p is surjective. Conversely, zero T has the identity S -> S as a nuclear covering and is plainly A-subnuclear.

**4. All finite-rank character maps are subnuclear for finite B.** If B is finite-dimensional, A^m is itself finite-dimensional nuclear. The coordinatewise character projection p:A^m -> S is continuous, open and surjective, with a continuous linear right inverse. For the standard basis e_i of S and a=(a_1,...,a_m), the composite Tp has the exact finite A-nuclear expansion Tp(a)=sum_i a_i·T(e_i). Each coefficient map a -> a_i is A-linear, equicontinuous as a finite family, and the target vectors are bounded. The source of the cover is nuclear, so T is A-subnuclear.

**5. Sharp failure of composition for every infinite B and nonzero T.** For infinite B, set E=A ⊕ S with its module direct-sum action. It contains B as a closed linear subspace and is nonnuclear. Define f(a,s)=T(s), u(s)=(0,s), and the A-linear surjection p:A ⊕ A^m -> E by p(a,a_1,...,a_m)=(a,(q(a_i))_i). A continuous linear section shows p is open; no A-linear section is claimed. The composite fp is the finite A-nuclear map fp(a,a_1,...,a_m)=sum_i a_i·T(e_i). Since E is nonnuclear, its subnuclear cover is NOT required to be nuclear, so f is A-subnuclear. Yet f∘u=T, which is not A-subnuclear by step 3 for T != 0.

This finishes the exact dichotomy and all-rank composition counterexamples. No claims about arbitrary non-square-zero Fréchet algebras are made.

## Internal dependencies, affected results, and scope boundaries

The only non-elementary analytic inputs are internal Lemma 2.13.1 (nuclear-to-compact) and Theorem 2.13.3 (nuclear-Fréchet closed-subspace permanence), read at docs/sections/open-maps-nuclear-spaces-and-inverse-limits--nuclear-spaces-and-completed-tensor-products/index.html, blob ecbf01a4ed81461ba32f1e0c88c6a550ebaa8135, physical lines 17 and 77. Their stable source/permanent labels are demailly-complex-geometry:A13EE630 / 67761F6CDA64 and demailly-complex-geometry:054FCEA1 / A46D09531259. Their full transitive proofs are NOT newly certified here.

The proof verifies, and does not refute, the necessity of the *covering-nuclearity* qualifier of Proposition 9.68.1, and strengthens the correct Example 9.68.2. Any later use of precomposition closure must supply the actual extra witness or nonnuclear-source assumption; no specific downstream printed theorem is currently asserted false. **Optional proposed correction:** add the dichotomy as a remark after Example 9.68.2; preserve original statement, source attribution and tags. There is no direct change to source/reading edition/registry or main.

Although the source-label prefix names a Demailly bibliography, this section is functional analysis, NOT Demailly approximation/regularization. The owner-excluded Demailly approximation, Bergman, weighted L2, OT, multiscale and positivity-loss programme is entirely untouched and remains deferred-by-user, neither resolved nor certified.

**Actual coverage:** first selected theorem-level examination of §9.68 (line 7, Proposition 9.68.1, Example 9.68.2) and only selected prerequisite statements in §2.13. This does NOT certify §9.68, §2.13 or any whole section. No tests, builds, CI, formalization or publication were conducted.
