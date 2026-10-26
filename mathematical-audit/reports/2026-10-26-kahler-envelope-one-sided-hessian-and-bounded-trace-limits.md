# Kähler obstacle Hessian estimates and the limits of complex-trace regularity — 26 October 2026

- **Reviewed current `main` SHA:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Audit branch at start:** `8a1aecc48d156a13e3120e53eef8bdf20e3be5de`.
- **UTC checkpoint:** 2026-10-26T09:12:21Z (time taken from the executing host).
- **Scope:** a first selected, non-Demailly proof-level pass on §§16.16 and 16.19 of the *integrated reading edition*. This is NOT a complete verification of either section or its PDE dependencies. No source, permanent-tag, proof registry or website changes proposed for automatic application.
- **Explicit exclusion:** §6.17.1 gentle analytic-singularity regularization used in §16.19.1 is cited as an author-deferred dependency. Its construction, Bergman/L²/Ohsawa–Takegoshi steps, multiscale atlas and positivity-loss proofs were not examined.

## Finding POME-ENVELOPE-SOFTMIN-ONESIDED-SHARP-001

**Severity:** low. **Status:** verified conditional deduction / exact sharpness diagnostic, **not a printed theorem error**.

**Source:** `docs/sections/envelopes-and-model-potentials--measures-on-contact-sets--real-hessian-bounds-for-kahler-envelopes/index.html`, current-main blob `011d45c646798edaf993db9e1dc2821d756b4161`. Lemma 16.16.1, source `foundations-of-pluripotential-theory-C7639230`, permanent tag `C8D21E3D949A`, statement physical lines 34–41 and proof lines 47–207. Theorem 16.16.7, source `foundations-of-pluripotential-theory-6355DEDC`, permanent tag `4B6432E0991B`, lines 212–242, particularly its soft-min formula and variance identity at 229–241.

**Claim (precise).** The one-sided upper bound for the *real* Hessian in Lemma 16.16.1 is structurally essential to the smooth soft-min route in Theorem 16.16.7: even for two fixed smooth obstacles with uniform values, gradients and two-sided Hessian bounds, their soft minima can have uniformly bounded **upper** real Hessian while the **lower** real Hessian diverges as `-1/δ`. No δ-independent two-sided Hessian bound holds for these approximating obstacles.

**Complete calculation.** Let `X=ℙ¹` with an arbitrary fixed smooth Riemannian metric, and set
[
arphi([z_0:z_1])=rac{|z_0|^2-|z_1|^2}{|z_0|^2+|z_1|^2}.
]
This is a smooth global function; its zero set is a regular equator, so `dφ≠0` at every point of that equator. Set `f_1=φ`, `f_2=-φ`, and
[
F_delta=-deltalog(e^{-arphi/delta}+e^{arphi/delta})
          =-deltalog(2cosh(arphi/delta)).
]
For every tangent vector `Y`, ordinary covariant differentiation gives
[
dF_delta=-	anh(arphi/delta),darphi,qquad

abla^2F_delta=-	anh(arphi/delta),
abla^2arphi
-delta^{-1}operatorname{sech}^2(arphi/delta),darphiotimes darphi.
]
Consequently `|Fδ|+|∇Fδ|` is bounded uniformly for `0<δ≤1` and
[

abla^2F_delta(Y,Y)le |
abla^2arphi|_infty |Y|^2
]
for all `Y`, because the second summand is negative semidefinite. But at any equatorial point `x` and a unit vector `Y` with `dφ_x(Y)≠0`,
[

abla^2F_delta(Y,Y)=-delta^{-1}|darphi_x(Y)|^2	o-infty.
]
Moreover `-lvertarphivert-deltalog2le F_deltale-lvertarphivert`, so the soft minima uniformly approximate the exact obstacle minimum. The two-sided Hessian bound on `Fδ` thus fails **even though both original obstacles are smooth and fixed**.

This verifies the negative-variance sign printed in Theorem 16.16.7, lines 235–241, and explains why Lemma 16.16.1 assumes only an **upper** obstacle-Hessian bound. It does **not** show that the *envelope* lacks a two-sided Hessian bound; the cited theorem asserts precisely the opposite.

**Proposal/dependents:** retain the one-sided hypothesis in any shortened or canonicalized proof, and optionally place this `ℙ¹` example alongside the soft-min argument. Depends only on elementary differentiation. Relevant to §§16.15–16.16 and envelope obstacles, not to analytic regularization.

## Finding POME-TRACE-COMPLEX-HESSIAN-NOT-C11-001

**Severity:** low. **Status:** verified conditional deduction / counterexample to an *unprinted* strengthening; **not a false theorem, not an envelope counterexample**.

**Source:** `docs/sections/envelopes-and-model-potentials--measures-on-contact-sets--big-class-envelopes-on-the-ample-locus/index.html`, current-main blob `6a522c402451a0d8fd0a8ee1aa47da3317688eed`. Theorem 16.19.1, source `foundations-of-pluripotential-theory-8E4CD211`, permanent tag `2F8D75599A90`, statement physical lines 10–19, proof final implication from bounded complex coefficients to `W^{2,p}_{loc}` and `C^{1,γ}_{loc}` at lines 196–214.

**Claim (precise).** Local boundedness of *all coefficients of the complex Hessian* of a psh function, even with a **uniform positive** complex Hessian lower bound, does **not** by itself imply bounded real Hessian or `C^{1,1}`. Thus Theorem 16.19.1's final regularity inference through scalar Laplacian/`W^{2,p}` is of the correct logical type; strengthening it to `C^{1,1}` requires a new envelope-specific estimate.

**Complete local example.** On a small disc, put `r=|z|`, `z=x+iy`, and define
[
u(z)=2|z|^2+operatorname{Re}(z^2)log|z|quad(z
e0),qquad u(0)=0.
]
The second summand is `r² log r cos(2θ)`. In polar coordinates,
[
Delta (r^2log rcos 2	heta)=4cos2	heta,
quad	ext{and hence}quad
Delta u=8+4cos2	hetain[4,12]quad(r>0).
]
There is **no atom at zero** in the distributional Laplacian: `u=O(r²|log r|)` and `|
abla u|=O(r|log r|)`, so the circle-boundary terms in integration by parts tend to zero. Therefore `u` is subharmonic on the whole disc, with its complex Hessian represented by an `L^infty` density satisfying `1le u_{zar z}le3` almost everywhere. Along the real axis,
[
u(x,0)=2x^2+x^2log|x|,qquad
partial_{xx}u(x,0)=7+2log|x|	o-infty,
]
so the real Hessian is unbounded. Its weak real Hessian grows at most like `C(1+|log r|)`, hence is in every finite `L^p`; the function is `C^{1,alpha}` for every `0<α<1` but **not** `C^{1,1}`. In dimension `n>1`, add `sum_{j=2}^n|z_j|^2`; its full complex Hessian remains bounded and strictly positive while the same real-Hessian obstruction persists.

**Logical limit:** this is a local psh function, **not asserted to be an envelope**, and therefore does not prove that the precise envelope conclusion of Theorem 16.19.1 is optimal. It rules out a shortcut from its *established complex-Hessian/trace bound alone* to `C^{1,1}`.

**Proposal/dependents:** no correction to the printed theorem. Retain `C^{1,gamma}` rather than deducing `C^{1,1}` solely from bounded `dd^c u`; extra real-Hessian arguments would be necessary. Relevant to §§16.16/16.19 and any downstream argument using complex-vs-real second derivatives. No external input needed for the countermodel.

## Actual independent proof scrutiny and deferred inputs

1. **§16.16.1** (physical lines 50–59): with `g₀=2 Σ_i(dx_i²+dy_i²)` at normal coordinates, `tr_{g₀}∇²b=2 Σ_i b_{iar i}`, confirming equation 16.16.2's factor 2. The largest real eigenvalue reduction uses the lower trace bound `2tr_kG−2n≥−2n`. Selected inequalities 16.16.3–6 (lines 61–207) were inspected for the upper-only obstacle-Hessian requirement and for the positive/negative terms `U+R−N`; no defect independently established. The full nonlinear third-order estimate and all of 16.15.20 were **not** formally certified.
2. **§16.16.7** (lines 222–242): the log-sum-exp Hessian is `Σ p_j∇²f_j−δ^{-1} Var_{p}(df_j)`; the negative variance is the precise reason the lower Hessian cannot be propagated to smooth approximants. Uniform obstacle convergence plus the `Pκ` sup-norm Lipschitz estimate permits the weak-Hessian limit without invoking sequential compactness of unrelated potentials. The final theorem remains conditionally reliant on the nonlinear estimate 16.16.1 and §16.15.
3. **§16.19.1** (lines 27–45): compared the reduction `Pθ(f)=Pθ(min f_j)` with the two competitor inclusions, and the isomorphism over the ample locus. **Dependency only, deferred-by-user:** the proof at physical line 29 calls §6.17.1's gentle analytic singularities/regularization; neither that theorem nor its prerequisites were reviewed. Hironaka principalization §9.6.7 is the separately permitted external existence input.
4. **§16.19.1** (lines 148–214): checked the algebra of the moving-radius infimum, the sign choice `ν=C₀/(1+a+C₀)`, and `(1+a)α+dd^c W≥0` at lines 164–177. The quadratic smoothing estimate (16.19.12) is then converted to bounded **complex** Hessian coefficients and to `W^{2,p}` by a local Poisson/fundamental-solution argument; the latter does not bound the full real Hessian in `L^infty`. The joint smoothing lemma §§16.17–16.18 remains a **conditional, nonexcluded** upstream input, not independently certified here.

**Coverage accounting:** only the selected proofs in previously inventory-only §§16.16 and 16.19 were examined; the chapter has not been fully certified. The existing 25-chapter, 747-section matrix is an *inventory*. No project tests, builds, CI, formalization or publication were run. The author-deferred Demailly/regularization/Bergman/L²/OT/multiscale/positivity-loss programme remains excluded and neither resolved nor certified.
