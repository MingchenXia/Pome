# Ringed-space coreflection and the two-factor Hermitian-symplectic energy landscape

**Date:** 2026-10-31. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Audit branch at start of this inspection:** a4f0563f7259bf67b24b8d4d2b7076070eaca071.

**Scope and exclusions.** This is a selected, proof-level review of the integrated reading edition, not a whole-section certification. We reviewed the sheaf-level factorization in §9.64.2–4 and, independently, the two-factor metric and completion constructions in §§11.2.22–24. Earlier §11.2.2–12 and §11.2.17–21 were consulted only to check conventions and downstream implications. The entire Demailly approximation/regularization and dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remains **deferred-by-user** and is not revisited.

## POME-RING-STRONG-COREFLECTION-001

**Severity:** low. **Status:** verified conditional deduction (complete categorical argument relative to the printed definitions; no false theorem). **Subject:** 9.64, ringed spaces and reductions.

**Exact current source:** production file [docs/sections/ringed-spaces-and-reductions/index.html](../../docs/sections/ringed-spaces-and-reductions/index.html), blob **a84cbf2134702a33dc53c3de30ff097d9cfa1c1f**. Proposition 9.64.2: source label **demailly-complex-geometry:A616BEB2**, permanent tag **ADC46EC60E54**, physical lines 13–29. Proposition 9.64.3: source label **demailly-complex-geometry:29A82276**, permanent tag **16DE5782FC00**, lines 32–56. Example 9.64.4: **demailly-complex-geometry:3F5E967D**, permanent tag **28539480EFD0**, lines 60–61. Section tag **B70DFF0046AA**.

**Claim.** Let C be the category of locally ringed spaces with their residue fields identified with a fixed field k, using local k-morphisms, exactly as defined in the reading text, and let S be its full subcategory of strongly reduced objects (the value evaluation is injective as a map of sheaves). The inclusion I:S -> C admits a **right adjoint** R, given by the strong reduction X ↦ X_st-red. Equivalently, for every strongly reduced Y and every X in C, composition with the canonical morphism ε_X:X_st-red -> X is a natural bijection

    Hom_S(Y, X_st-red)  ≅  Hom_C(Y, X).

The same universal property holds for the ordinary reduction of ringed spaces with reduced source objects (and, in the local-k subcategory, with reduced local-k source objects). Moreover,

    (X_red)_st-red ≅ X_st-red

canonically, without assuming any Hausdorff, finiteness or analytic hypotheses.

**Proof.** Let f:Y -> X be a local k-morphism, with Y strongly reduced. Write e_X:R_X -> F_X for the residue-value evaluation, K_X=ker(e_X), and similarly e_Y,K_Y for Y. These are the precise sheaves used in Proposition 9.64.3. By naturality of residue evaluation (the equation in its lines 49–53),

    e_Y(f#s) = (e_X s)∘f

as local functions, for each local section s of R_X. Thus if s belongs to K_X then e_Y(f#s)=0; since Y is strongly reduced, K_Y=0 and f#s=0. This kills the inverse image of K_X in R_Y, so f# uniquely factors through the quotient R_X/K_X=R_X^val. The induced stalk map remains local: if a value-germ vanishes at f(y), its lift has residue zero and hence its image lies in the maximal ideal at y; a nonvanishing value-germ is a unit locally. Therefore the factorization is a morphism of locally ringed k-spaces Y -> X_st-red. It is unique because the quotient sheaf map is surjective locally. Conversely, any such morphism composed with ε_X gives a map Y -> X. These two operations are inverse, natural in X and Y, proving the claimed right adjoint (a *coreflection*, not a reflection).

For ordinary reduction, replace K_X by its nilradical N_X; homomorphisms to reduced stalks annihilate nilpotents, giving the identical universal factorization. Finally, the residue-value evaluation of R_X/N_X has the same image as that of R_X because N_X is already in K_X. Thus the strong reduction of X_red has the same value sheaf and the same underlying topological space as X_st-red. The one-point k[t]_(t) instance in printed Example 9.64.4 demonstrates that ordinary and strong reduction need not themselves coincide; it is a contextual example, **not** a new finding.

**Proposed addition and affected dependents.** An optional universal-property paragraph after Proposition 9.64.3 could state the right-adjoint property and the canonical (X_red)_st-red identity. The correction is *expository*: none of Propositions 9.64.2–3 or Example 9.64.4 is false, no canonicalization/tag replacement is justified, and no unrelated sheaf-theoretic or analytic theorem is certified. This also clarifies the direction of reduction maps when used in §9.58–9.60 or §9.67.

## POME-HERM-TORUS-PRODUCT-SADDLE-001

**Severity:** low. **Status:** verified conditional deduction (fully checked algebra for this explicit smooth family, conditional on the integrated norm and Aeppli conventions); not a false printed theorem.

**Exact current source:** production file [docs/sections/monge-ampere-energy-and-torsion/index.html](../../docs/sections/monge-ampere-energy-and-torsion/index.html), blob **fe1ca06167b8f5bc9868e9a9876397afad4e7ff5**. Section §11.2.22: source variant non-kahler-pluripotential-theory, permanent tag **EF1FC602D899**, source heading tag **D6BDDB5B**, physical lines **345–374**. Example §11.2.23: source label **non-kahler-pluripotential-theory:CC0FA29C**, permanent tag **ACA94D5D202C**, lines **376–398**. Example §11.2.24: source label **non-kahler-pluripotential-theory:4189BCA9**, permanent tag **F9D5DB66D92A**, lines **401–416**. Conditional supporting Proposition §11.2.17 tag **AE6CE389C569**, lines 253–284; §11.2.19 tag **04BD04D6C676**, lines 287–341.

**Claim.** Let S=(C/(Z+iZ))^2 be the square complex two-torus, let η, α_s, v_s, ρ_s and μ_0=η²/2 be exactly as in the integrated §11.2.22, and put V_0=∫_S μ_0. For 0<s,t<1, set on X=S×S

    ω_{s,t}=pr_1^*α_s + pr_2^*α_t.

Each ω_{s,t} is positive Hermitian symplectic, lies in one fixed Aeppli class, and has canonical completion pr_1^*ρ_s+pr_2^*ρ_t. Its entire **two-parameter** completion-energy/volume landscape is

    F(ω_{s,t})/V_0² = s²(1-t²)+(1-s²)t² = s²+t²-2s²t²,
    V(ω_{s,t})/V_0² = (1-s²)(1-t²),
    (F+V)(ω_{s,t})/V_0² = 1-s²t².

The only stationary point for F in the open (s,t)-square is (1/√2,1/√2). Its Hessian in these legitimate Aeppli directions is

    Hess_{s,t}(F)|_(1/√2,1/√2) = V_0² [[0,-4],[-4,0]],

with eigenvalues ±4V_0². Thus it is a **strict saddle in an explicit two-dimensional Aeppli subspace**, even though Example 11.2.23 correctly states that the same metric is stationary under *all* Aeppli variations. This supplies a finite-dimensional quantitative check, distinct from Theorem 11.2.19's infinite positive/negative *potential-direction* index.

**Proof.** The Hermitian eigenvalues of α_s are 1±s, while ρ_s=∂v_s is a completion, so positivity and closedness of ω_{s,t}+ρ_s+barρ_s+ρ_t+barρ_t follow for 0<s,t<1. The Aeppli differences are ∂(bar v_s-bar v_{s_0})+bar∂(v_s-v_{s_0}) on each factor; hence the entire family lies in one Aeppli class.

Every holomorphic 2-form on a compact complex torus has constant coefficients (pull back to a bounded periodic entire coefficient function and use Liouville). The pairing of ∂v_s with a holomorphic 2-form is zero by Stokes, and the product metric is block diagonal, so pure-factor and mixed holomorphic 2-forms are orthogonal. Therefore pr_1^*ρ_s+pr_2^*ρ_t is orthogonal to *all* holomorphic 2-forms on X. It is exactly the canonical minimizer in §11.2.14, not merely some completion.

By bidegree and factor dimension, cross terms ρ_s∧barρ_t in the canonical energy wedge vanish. The printed identities α_s²/2=(1-s²)μ_0 and ρ_s∧barρ_s=s²μ_0 give

    F(ω_{s,t})= ∫_X (ρ_s∧barρ_s∧α_t²/2 + α_s²/2∧ρ_t∧barρ_t)
                = [s²(1-t²)+(1-s²)t²] V_0².

Since only the term containing two factors from each torus contributes to ω_{s,t}⁴, its normalized fourth-power volume is (1-s²)(1-t²)V_0². This proves the three formulas. Differentiation gives

    ∂_s(F/V_0²)=2s(1-2t²),   ∂_t(F/V_0²)=2t(1-2s²),

so there is precisely one critical point in the positive open square. The Hessian has entries 2(1-2t²), 2(1-2s²), and mixed entry -8st; evaluation yields the displayed saddle matrix. Both eigen-directions remain in the positive-metric region for sufficiently small signed variations.

At t=0 (the smooth limiting member with α_0=η), these expressions reduce to Example 11.2.24's F=s²V_0² and V=(1-s²)V_0². At s=t=1/√2, they give F=V_0²/2 and V=V_0²/4, in agreement with Example 11.2.23. Thus no source formula was contradicted.

**Reproducible local check.** SymPy was used on the polynomial F/V_0²=s²+t²-2s²t²: its exact symbolic gradient, the critical Hessian [[0,-4],[-4,0]], and rational samples (s,t)=(1/3,2/5), giving F/V_0²=53/225 and V/V_0²=56/75, and (3/5,4/5), giving 337/625 and 144/625, matched the source-factored forms. These are polynomial checks, not a test of the analytic theory. No project tests/build/CI/formal verification were run.

**Proposed addition and dependents.** An optional short two-parameter illustration after Example 11.2.24 would illuminate why the critical non-Kähler Example 11.2.23 cannot be a local minimum of F. It does **not** claim all critical points of F in an Aeppli class are of this form, does **not** prove the general Bochner/complex Hessian results, and makes no change to the original theorem text, source attributions, permanent tags, or website.

## Coverage and integrity ledger

This session newly checks the **unreviewed §§11.2.22–24 two-factor completion calculations and Aeppli saddle**, and proves the **previously unrecorded universal factorization** implicit in selected §9.64.2–4. The historical §9.64 proof inspection and §11.2.1–21 checks are *not* counted as new inspections; their earlier statuses are preserved. Neither whole §9.64 nor whole §11.2, nor their external/internal dependency closure, is certified.

The actual current table of contents still has **25 chapters and 747 uniquely numbered sections**, with **zero whole mathematical-section certifications**. No existing false-theorem, gap, candidate, external-dependency, duplication, verified-repair or deferred-by-user ledger status changes. No source, project main, proof registry, permanent tags, GitHub Actions, site publication or formalization files are changed. This audit consists only of new English notes and the pre-existing durable ledgers/matrix.
