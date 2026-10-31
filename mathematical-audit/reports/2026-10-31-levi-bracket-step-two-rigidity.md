# A pointwise step-two bracket criterion for the Levi distribution

Date: 2026-10-31. Reviewed production main: **b6933b772f41b45918f7e25ed1afbbb1fd892272**. Review-only proposed corollary; no alteration to the reading edition.

## New finding: POME-LEVI-STEP2-BRACKET-001

**Status:** low / **verified conditional deduction** (in fact self-contained once the defining Levi/bracket conventions are adopted). **Not a false theorem, not a claim of certification of a whole section.**

**Integrated reading edition:** docs/sections/boundary-levi-geometry-and-holomorphic-extension--boundary-levi-geometry/index.html, blob **fe5ebfa26a59b083027a10b66fcc13bddad8acbc**. Proposition **9.34.1**, source label **demailly-complex-geometry:412412EC**, permanent tag **07D51E96DD30**, physical lines **16–41**, particularly normalized Levi equation at lines **8–10**, bracket identity at **17–20**, and the differential-form verification at **27–39**. Section tag **E8FB727B5227** (source **demailly-complex-geometry:637DAA63**). Related normal-form Proposition **9.34.3**, source **demailly-complex-geometry:3AA79440**, permanent tag **B4D5FDB2BE18**, lines **92–113**; boundary-pseudoconvexity Theorem **9.34.2**, source **demailly-complex-geometry:3D6302E9**, permanent tag **8F39CE9F0DBB**, lines **46–88**, is contextual, not re-proved.

**Hypotheses and precise new statement.** Let M be a C² real hypersurface in Cⁿ, n >= 2, with complex tangent real distribution D = TM ∩ JTM of real rank 2n−2. At p in M, let [D,D]_p denote the real vector span of values of brackets [X,Y](p) of C¹ local sections X,Y of D. Then

\[
 D_p+[D,D]_p=T_pM \quad\Longleftrightarrow\quad L_p\not\equiv0,
\]

where L is the normalized Hermitian Levi form of Proposition 9.34.1. Thus a *single nonzero* Levi eigenvalue already gives step-two bracket generation at p; neither strict pseudoconvexity nor any sign condition is needed. Conversely, when L_p=0, every first bracket at p is tangent to D_p. In particular, on an open patch where L does not vanish at any point, every C² real function whose differential annihilates D is locally constant. This last conclusion concerns first integrals only and does not use a global Chow theorem.

**Complete proof.** Use the outward unit normal ν, and the one-form α on M from Proposition 9.34.1, satisfying D=ker α and α(v)=g(v,Jν). For C¹ local D-sections X,Y, the printed identity (verified independently below) gives

\[
 \alpha_p([X,Y])=4\operatorname{Im}L_p(X_p,Y_p).
\]

If L_p=0, the right-hand side is zero for all X,Y, so the brackets have no component in the one-dimensional quotient T_pM/D_p. If L_p≠0, Hermitian polarization gives ξ∈D_p with L_p(ξ,ξ)≠0. Extend ξ to a C¹ section X of D, and set Y=JX; J preserves D. Hermitian sesquilinearity gives

\[
 L_p(\xi,J\xi)=-iL_p(\xi,\xi),\qquad
 \alpha_p([X,JX])=-4L_p(\xi,\xi)\ne0.
\]

Thus [X,JX]_p supplies the missing normal-to-D tangent direction, proving the claimed equality. For a C² first integral F on a patch, X(F)=Y(F)=0 for every D-section, whence [X,Y](F)=0; the spanning result gives dF=0, hence local constancy. At n=1, D=0 and the nonzero-Levi alternative never occurs.

**Independent sign/factor check.** In C² let z=x+iy, w=u+iv and ρ=Re w+λ|z|², with λ a nonzero real number. The hypersurface is u=−λ(x²+y²). The real tangent and D-sections

\[
 X=\partial_x-2\lambda x\partial_u+2\lambda y\partial_v,\qquad
 Y=\partial_y-2\lambda y\partial_u-2\lambda x\partial_v
\]

satisfy dρ(X)=dρ(Y)=0 and β(X)=β(Y)=0 for β=dv+2λ(x\,dy-y\,dx), corresponding to α in the printed proof. Their Lie bracket is exactly [X,Y]=−4λ∂_v. At the origin JX=Y, the outward normal is ∂_u and L_0(X,JX)=−iλ, yielding 4 Im L_0(X,JX)=−4λ, in full agreement with the printed identity. The calculation holds for λ>0 and λ<0, explicitly distinguishing the bracket property from Levi semipositivity. A local SymPy exact symbolic check of dρ, β, and [X,Y] was executed; outputs were 0, 0, 0, 0, and the vector (0,0,0,−4λ).

**Adjudication and proposed change.** Proposition 9.34.1 is **not disproved**: its sign and coefficient were corroborated. An *optional corollary after Proposition 9.34.1* may state the pointwise step-two criterion and first-integral rigidity. Preserve the existing source tag, permanent tags and historical attribution. The proposed corollary does not infer pseudoconvexity, local holomorphic extension, finite-type estimates, or global controllability, and is not a repair of Theorem 9.34.2 or Proposition 9.34.3. These are only possible conceptual dependents.

## Separate selected proof-risk comparison: scalar Monge–Ampère functional

Inspected, but found **no new error**: docs/sections/normalization-and-weak-adjoint-measures--the-scalar-functional/index.html, production blob **fff86de757578ed2be369ba752123f62f3d31044**. Proposition **11.33.2** source **non-kahler-pluripotential-theory:6D175DAF**, permanent **2770AB03C0D2**, physical **27–50**, uses the strict singular domination principle for monotonicity and a constant shift for the sharp L∞ comparison. Theorem **11.33.4** source **non-kahler-pluripotential-theory:547E9FD9**, permanent **8810E18F852C**, physical **62–83**, uses the mixed extended-MA lower bound plus strict domination. Theorem **11.33.5** source **non-kahler-pluripotential-theory:D502EBBF**, permanent **5E3583383688**, physical **89–117**, invokes a uniform relative L∞ barrier and capacity continuity. The reductions follow the stated hypotheses **conditionally**; the upstream singular domination, mixed-product theory, barriers, existence and capacity-continuity inputs have not been independently certified here. No new stable finding or whole-section verification is assigned to this contextual cross-chapter inspection.

## Coverage, dependencies and boundaries

Actual *new mathematical proof/model* is Proposition 9.34.1's pointwise bracket geometry and quadratic model, with Proposition 9.34.3 normal-form and Theorem 9.34.2 checked only as context. §9.34 had already appeared as a selected/inventory hybrid in the coverage matrix, so this is an **incremental** proof-level check, not a first inspection of the entire subject. The separate selected §11.33.2/.4/.5 comparison is explicitly conditional and does not count as an independently verified theorem. The current ToC contains **25 chapters and 747 numbered sections**, with **zero entire mathematical sections certified**. No project build, CI, formal proof, publication, source manuscript, permanent tag, or production-main edit was performed. Earlier confirmed errors, proof gaps, external dependencies and repaired statuses retain their existing ledger entries.

All dedicated Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion tasks remain expressly **deferred-by-user**, neither reopened nor certified. The boundary Levi geometry reviewed here is mathematically independent of that excluded programme.
