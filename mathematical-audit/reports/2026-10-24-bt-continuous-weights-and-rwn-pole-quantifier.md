# 2026-10-24 — Bedford–Taylor continuous weights and a pole-set quantifier in the Ross–Witt Nyström proof

**Main actually reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Starting audit head:** 386f923cf4eabdeb753591ca90690cea03b2ae32. The audit branch was not reset. This report audits only the named integrated proof passages, not their entire chapters or upstream analytic results.

**Scope:** §§7.2–7.6 and §§17.12–17.13, with §16.21 used only as an already established explicit projective-line model. The dedicated Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss completion programme was not inspected; existing records remain **deferred-by-user**, not resolved or certified. The strong-openness input used later in §17.13.35 was *not* re-proved.

## Finding POME-BT-CONTINUOUS-WEIGHT-001 — verified conditional deduction (low)

**Exact integrated anchors:** Theorem 7.3.7, source label foundations-of-pluripotential-theory-8B1F9B78, permanent tag D87C13B3250A, and Corollary 7.3.8, source label foundations-of-pluripotential-theory-45C06B5C, permanent tag 8BD7803A393B, in

docs/sections/bedford-taylor-products-and-local-capacity--decreasing-continuity-and-symmetry/index.html

at main blob 96a9e39e85fab5774ebdac0c6d9d006338a4e42c, physical lines 134–148 and 234–265. For uniform local mass control, Theorem 7.2.5, source foundations-of-pluripotential-theory, permanent tag 2A84C325AB58, is in

docs/sections/bedford-taylor-products-and-local-capacity--bounded-potentials-and-recursive-products/index.html

at blob 18bd2395f3b76941b2c677079c09eb6accc5a9cb, physical lines 99–118.

**Statement (new, not a claim of error).** Let Ω be open in ℂⁿ, T a *fixed* closed positive current of bidimension (r,r), and 0≤q≤r. For each 1≤k≤q let u_{k,j}↓u_k, and for each 1≤a≤m let v_{a,j}↓v_a, be decreasing sequences of locally bounded plurisubharmonic functions with locally bounded plurisubharmonic limits. Let H:ℝᵐ→ℝ be *any continuous function*, with no convexity or monotonicity requirement. Put

\[
S_j=dd^c u_{1,j}\wedge\cdots\wedge dd^c u_{q,j}\wedge T,\qquad
S=dd^c u_1\wedge\cdots\wedge dd^c u_q\wedge T .
\]

Then the locally finite signed currents

\[
H(v_{1,j},\ldots,v_{m,j})S_j
 \ \rightharpoonup\
H(v_1,\ldots,v_m)S.
\]

The q=0 case is included. This strengthens the printed *polynomial-weight* Corollary 7.3.8; it does not change the Bedford–Taylor theorem and is conditional on its proved weighted convergence and the stated CLN estimate. There is no analogous assertion here for arbitrary measurable or discontinuous H.

**Complete deduction.** Fix a smooth compactly supported test form ξ in Ω and compact neighborhoods K⊂Int L⊂Ω of its support. For all j, the monotone bounds u_k≤u_{k,j}≤u_{k,1} and v_a≤v_{a,j}≤v_{a,1} furnish uniform finite sup bounds on L. All vectors (v_{1,j}(z),…,v_{m,j}(z)) and their limiting vectors lie in one compact box Q⊂ℝᵐ for z∈L. Theorem 7.2.5 bounds the masses of S_j on K uniformly in j; the positive-current coefficient estimate of Theorem 5.3.7 then gives a uniform total-variation bound for the action of S_j on ξ with bounded Borel multipliers. The same is true of S.

For every ε>0 the real Stone–Weierstrass theorem (equivalently, multivariate polynomial uniform approximation on a box) gives a polynomial P_ε with sup_Q|H−P_ε|<ε. Consequently, with a constant A_{ξ,K} independent of j and ε,

\[
|\langle[H(v_j)-P_\epsilon(v_j)]S_j,\xi\rangle|
\le A_{\xi,K}\epsilon,\quad
|\langle[H(v)-P_\epsilon(v)]S,\xi\rangle|
\le A_{\xi,K}\epsilon.
\]

For the *fixed* polynomial P_ε, Corollary 7.3.8 gives

\[
P_\epsilon(v_j)S_j\rightharpoonup P_\epsilon(v)S.
\]

The triangle inequality yields limsup_j|⟨H(v_j)S_j−H(v)S,ξ⟩|≤2A_{ξ,K}ε. Let ε↓0. No interchange of two uncontrolled limits occurs: j is taken to infinity **with the polynomial fixed**, and only then ε→0. Uniform local bounds are essential and are supplied by the monotone hypotheses; no assumption of sequential compactness of a space of currents is added.

**Proposed optional integration:** a short corollary after 7.3.8, preserving the polynomial statement, its tag, and the existing historical attribution. **Dependents:** local bounded-product convergence with nonlinear continuous observables, contact-set calculations and local variational formulas using scalar functions of several monotone psh weights. This does **not** extend the theorem to moving arbitrary base currents or unbounded weights.

## Finding POME-RWN-POLE-QUANTIFIER-001 — proof gap (low); local a.e. correction verified, theorem not shown false

**Exact integrated anchors:** Proposition 17.13.35 (He–Testorf–Wang), source sgpt-5698E0B2, permanent tag E6915C7339CD, especially **Step 1, physical lines 707–740**, in

docs/sections/test-curves--ross-witt-nystrom-correspondence/index.html

at blob bdfe4175ffeeb4d1b3decf4dbaace0738c4c2b09. The relevant formula is 17.13.14 (physical lines 268–272), and its duality is Proposition 17.13.5, source sgpt-B7A24A26, tag 1F48BF7602CA, lines 42–56. The explicit source of the example is Example 17.12.13, source sgpt-C293066A, permanent tag 1A17E2EECB2D, in

docs/sections/test-curves--the-notion-of-test-curves/index.html

at blob 6dfdfc2b5e599eb3a19a9558a9c963e79df71dc7, physical lines 166–170. The previously derived P¹ model-envelope free-boundary formula is recorded in mathematical-audit/reports/2026-10-24-projective-line-singularity-envelope-contact-free-boundary.md and is used *only* to certify its pole at the origin.

**Precise faulty intermediate assertion.** Step 1 says: “Given any y∈X, it follows from (17.13.14) that there is t₀>0 with ℓ*_{τ}(y)+1≥ℓ_{t₀}(y)−t₀τ.” This is valid when ℓ*_{τ}(y)>−∞, but fails at poles where ℓ*_{τ}(y)=−∞ and every finite-time ℓ_t(y) is finite. It is an **intermediate pointwise quantifier**, not a false assertion of Proposition 17.13.35 itself.

**Concrete admissible model.** Take X=ℙ¹, θ=ω_FS normalized, φ=V_θ=0, fix 0<a<1 and

\[
\varphi(z)=a\log\frac{|z|^2}{1+|z|^2}.
\]

Use Example 17.12.13:

\[
\Gamma_\sigma=
\begin{cases}
0,&\sigma\le-1,\\
P_\omega[(1+\sigma)\varphi],&-1<\sigma<0,
\end{cases}
\quad \Gamma_{\max}=0.
\]

For −1<σ<0 the model envelope has a logarithmic pole at z=0, since its explicit ℙ¹ formula has Lelong coefficient a(1+σ)>0. Thus Γ_σ(0)=−∞ on (−1,0), while Γ_σ(0)=0 for σ≤−1. Its Legendre ray ℓ=Γ* belongs to the declared ray class by Lemma 17.13.11, and pointwise

\[
\ell_t(0)=\sup_{\sigma<0}(t\sigma+\Gamma_\sigma(0))=-t
\quad(t>0).
\]

For τ=−1/2 (<ℓ*_{max}=0),

\[
\ell^*_\tau(0)=\inf_{t>0}(-t-t\tau)
=\inf_{t>0}(-t/2)=-\infty.
\]

But for every finite t₀>0, ℓ_{t₀}(0)−t₀τ=−t₀/2 is finite. Hence **no** t₀ satisfies the displayed Step-1 inequality at y=0. This is not a counterexample to the integrated multiplier-ideal identity: that identity is about local integrability with respect to a smooth volume measure.

**Verified local correction.** Replace “Given any y∈X” in Step 1 by “For any y outside the pluripolar set {ℓ*_{τ}=−∞}.” The θ-psh potential ℓ*_{τ} is nonidentically −∞ for τ<ℓ*_{max}, so its pole set is pluripolar and has measure zero for the smooth Kähler measure ωⁿ. At every remaining y, the infimum in (17.13.14) is a finite real number, so one may choose t₀=t₀(y)>0 with

\[
\ell^*_\tau(y)+1\ge \ell_{t_0}(y)-t_0\tau .
\]

The monotonicity argument in printed lines 718–728 then yields, **for almost every y**,

\[
e^{-\ell^*_\tau(y)}
\le
e^{\,1+\ell^*_{\max}-\tau}
\int_{0}^{\infty} e^{-\ell_t(y)+t\tau}\,dt .
\]

Pointwise selection of t₀ needs no measurable-selection theorem: the resulting bound uses the *full* time integral and is independent of the chosen t₀. Integrating over a neighborhood U and ignoring the null pole set justifies lines 731–743. This repairs **only Step 1**. The converse direction's strong-openness input, the full proposition, and any excluded regularization machinery were not re-audited or certified.

**Proposed patch:** replace the universal pointwise quantifier by the a.e. statement above and state explicitly that smooth volume measure ignores the pole set; preserve He–Testorf–Wang attribution, formula 17.13.36 and permanent tag. **Affected dependents:** the Step-1 integrability implication in Proposition 17.13.35 and any later use of its multiplier-ideal characterization. The conclusion's truth is not challenged.

## Additional selected passages and limits of coverage

- §7.2.2/.5/.6: recursive positivity/closedness, CLN cutoff mass estimate and locally uniform-weight convergence, **selected steps only**, at blobs 18bd2395f3b76941b2c677079c09eb6accc5a9cb, physical lines 30–77 and 99–155.
- §7.3.3/.7/.8/.10/.11: smooth-vs-bounded integration by parts, induction with fixed collar, polynomial polarization, Borel maximum locality and comparison telescoping, **selected steps only**, blob 96a9e39e85fab5774ebdac0c6d9d006338a4e42c, lines 40–69, 134–228, 234–273, 279–362. No incorrect result found in these sampled steps.
- §7.5.2/.4/.6/.7/.8: quasi-continuity via capacity cutoff, outer capacity of quasi-continuous level sets, local capacity convergence, polynomial capacity domination and convergence of bounded products, **selected steps only**, blob 464778b7ca6f1a456e36b24ecb4a0c93ab6948d3, lines 15–36, 63–79, 93–119, 125–185. No capacity theorem certified in full.
- §7.6.1: decreasing collar comparison in the *increasing-potential* theorem and capacity passage, lines 10–58, blob 5e763bdc928794938c37dc3c7a51cc406472d076. Selected proof reading; not a general-net theorem.
- §17.13.5/.11/.15/.21/.35/.38: Legendre definitions, selected endpoint limits, inverse correspondence and pointwise contact-set equivalence; only Proposition 17.13.35 Step 1 received a confirmed local quantifier finding. The full Ross–Witt Nyström theorem and strong-openness prerequisite are **not** certified.

**Verification actually performed:** direct symbolic/analytic argument, explicit projective-line pole construction and physical-line/tag crosschecks against the specified main blobs. **Not performed:** project build/test suite, CI, site publication, formal proof checking, numeric scripts, PR/merge/issue operations, changes to mathematical bodies, source repositories, tags, registries or main. This adds **partial** coverage, not a section-level certificate.