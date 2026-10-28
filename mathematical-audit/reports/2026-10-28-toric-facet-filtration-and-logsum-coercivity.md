# Audit: facet vanishing-order distributions and log-sum-exp coercivity (28 October 2026)

**Pinned production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Audit branch starting HEAD:** `c7a5d4213bc2dab8b3e8b35684c2425d2ec29ba0`. This report covers selected nonexcluded mathematical passages, not a whole-section or dependency-chain certification. Findings below are original-model **verified conditional deductions**, not errors in the printed statements. Previous findings and the user's excluded Demailly approximation/regularization, dedicated Bergman, weighted L2, Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss programmes remain **deferred-by-user**, not resolved.

## Finding POME-TORIC-FACET-VANISH-DH-001

**Severity:** low. **Status:** verified conditional deduction (optional quantitative corollary; no false theorem).
**Source / exact anchor:** production `docs/sections/convex-analysis-and-toric-potentials--fans-divisors-and-character-sections/index.html` (**blob `7ad2e6dbdd0ce59e1bf08cd9cb3c046e8c87ff6c`**), Proposition **21.9.2**, source `foundations-of-pluripotential-theory` (statement and proof physical lines **35–61**), permanent tag `7B4A7CC50CDC`; Theorem **21.9.5**, source `foundations-of-pluripotential-theory:BD98CC5B`, permanent tag **`69D3D97E7701`**, physical lines **139–167**. Lattice-counting dependency: `docs/sections/convex-analysis-and-toric-potentials--lattice-points-and-volume/index.html`, blob `5d209b7f4d2156c19bc3fb300303405df6321230`, Theorem **21.7.3**, source `foundations-of-pluripotential-theory:364BCD30`, tag `831AEEB7084F`, lines **58–89**. Cross-framework definitions: `docs/sections/the-theory-of-okounkov-bodies--okounkov-test-curves/index.html`, blob `20ff3089e62dd1c8349e8bcc077ec64605a9788b`, Definition **19.6.5** (test functions, lines **90–104**), Definitions **19.6.7** and **19.6.18**, source `sgpt:09132002`, tag `51940EF88F4F`, lines **113–127 / 329–334**. These are distinct statements; old chart-reference-cycle and fixed-jet findings are unchanged.

**Hypotheses and exact conclusion.** Let `P` be a full-dimensional smooth integral lattice polytope in `M_R` (the setting of §§21.8–21.9), let `rho` be a facet with primitive inward normal `u_rho`, and let `ell_rho(p)=<p,u_rho>+a_rho >=0` be its defining affine function. Let `L` and `s_0` be the line bundle and meromorphic section constructed by Theorem 21.9.5. Write `s_{k,m}=chi^m s_0^k` for `m in kP cap M`. Then
```text
ord_{D_rho}(s_{k,m}) = <m,u_rho> + k a_rho = k ell_rho(m/k).
nu_{k,rho} := k^{-n} sum_{m in kP cap M} delta_{ord_{D_rho}(s_{k,m})/k}
  --> (ell_rho)_*( 1_P dp )     narrowly as finite measures on R.
```
For every bounded continuous `f`, the convergence follows by applying the lattice Riemann-sum Theorem 21.7.3 to the continuous function `p -> f(ell_rho(p))`. The support of all these measures lies in the *fixed compact interval* `[0,max_P ell_rho]`; consequently there is no loss of mass at infinity, and even every continuous (possibly unbounded) test `f` is bounded on their common support. In particular, the normalized empirical probability distribution (divide the counting measure by `h^0(X_P,L^k)=#(kP cap M)`) converges to `(ell_rho)_*(dp/vol P)`. All moments converge by using bounded-on-support powers `f(t)=t^j`; **no** general moment convergence from vague convergence is assumed. This is conditional on the independently stated toric character basis and lattice counting, *not* a new proof of their full upstream construction.

**Direct model calculation.** Put `n=2` and `P=d conv{(0,0),(1,0),(0,1)}`, `d in Z_{>0}`; this is a Delzant lattice triangle and its toric model is `P^2` with `L=O(d)`. For the facet `rho={x=0}`, `ell_rho(x,y)=x`. At level `k`, the allowed lattice points are `(i,j) in Z_{>=0}^2` with `i+j<=kd`. The order `i` occurs with **exact multiplicity `kd-i+1`**:
```text
nu_{k,rho} = k^{-2} sum_{i=0}^{kd} (kd-i+1) delta_{i/k}.
```
Fubini on the triangle, with cross-section length `d-t`, yields
```text
nu_{k,rho} -> (d-t) 1_[0,d](t) dt,
total mass = d^2/2 = vol(P),
probability density = 2(d-t)/d^2,
E[t^j] = 2 d^j / ((j+1)(j+2))   (j=0,1,2,...).
```
In particular `E[t]=d/3`, `E[t^2]=d^2/6` and variance `d^2/18`. This includes the exact `n!` normalization check: `h^0(P^2,O(dk)) ~ k^2 d^2/2`, while the leading line-bundle volume is `2! vol(P)=d^2`.

**Test-curve interface (not a new general NA theorem).** The affine function `G(p)=ell_rho(p)` is a bounded upper-semicontinuous concave test function on `P` (§19.6.5); its superlevels `P_tau={p in P:G(p)>=tau}` for `tau<d` form a bounded Okounkov test curve with terminal time `d`. By Definition 19.6.18, its Duistermaat–Heckman measure is **exactly** the above limit `G_*(1_P dp)`, with mass `vol(P)`, *not* a probability measure until normalized. This is an explicit toric model useful for distinguishing DH mass and probability normalizations, and for finite-dimensional filtration consistency checks in §19.6 and §22.1. It does not repair or relitigate the already-confirmed false unbounded-terminal assertion of Proposition 19.6.16; that older ledger entry retains its status.

**Disposition and dependents:** An optional proof-contained facet-weight corollary adjacent to §21.9.5 or §19.6.18 would be legitimate after separate review. Preserve all permanent tags and source historical attribution; do not change a theorem statement, source file, or canonicalization. Directly relevant to graded section filtrations, Okounkov test curves and non-Archimedean DH models. No extra external theorem beyond the explicitly cited internal results is required.

## Finding POME-LOGSUM-RELINT-COERCIVITY-001

**Severity:** low. **Status:** verified conditional deduction (sharp strengthening/limit criterion; the printed lemma is correct).
**Source / exact anchor:** production `docs/sections/convex-analysis-and-toric-potentials--slope-bodies-and-bounded-growth/index.html`, blob `56a9a1c19e7234e2aa258d5ad1b66a5679ace190`, Lemma **21.4.6**, source **`foundations-of-pluripotential-theory:5D58DF02`**, permanent tag **`F7AECD623994`**, physical lines **109–123**. Earlier §21.4.2–4 proof checks remain separate.

**Sharp quantitative criterion.** Let `B=conv(beta_1,...,beta_m)` in `M_R`, `V=span_R{beta_i-beta_1}`, and assume **`alpha in B`**. Define
```text
H_alpha(x)=log(sum_i exp(<beta_i,x>)) - <alpha,x>
          =log(sum_i exp(<beta_i-alpha,x>)).
g_alpha(x)=max_i <beta_i-alpha,x> = h_B(x)-<alpha,x>.
```
Because `beta_i-alpha in V`, both functions descend to `Q=N_R/V^perp`; give `Q` any Euclidean norm. The elementary log-sum-exp bounds are
```text
g_alpha(x) <= H_alpha(x) <= g_alpha(x)+log m.
```
If `alpha` is in the **relative interior** of `B`, then for every nonzero `x in Q` the support gap `g_alpha(x)>0`; by continuity on the quotient unit sphere,
```text
epsilon |x| <= H_alpha(x) <= C |x| + log m
epsilon=min_{|v|=1}g_alpha(v)>0,   C=max_{|v|=1}g_alpha(v).
```
Consequently `H_alpha` is coercive on `Q`, and `exp(-H_alpha)` is integrable with respect to Euclidean Lebesgue measure on `Q`. This last assertion follows from the explicit dominating function `exp(-epsilon |x|)`; no analytic regularization, Bergman, weighted L2 or Ohsawa–Takegoshi argument enters.

Conversely, if `alpha` belongs to the **relative boundary** of `B` and `dim V>=1`, the finite-dimensional separation theorem gives a unit vector `v in Q` with `g_alpha(v)=0`. Then `0<=H_alpha(tv)<=log m` for every `t>=0`, so `H_alpha` is not coercive. More strongly, if `w` ranges over a bounded set in a hyperplane perpendicular to `v`, then
`H_alpha(tv+w) <= log m + max_i <beta_i-alpha,w>`, uniformly in `t>=0`; hence `exp(-H_alpha)` has a positive lower bound on an infinite-volume half-cylinder, and its integral over `Q` diverges. In quotient dimension one the transverse "cylinder" is simply a half-line. The degenerate case `dim V=0` is consistent: `Q` is a point and `H_alpha=log m`; its zero-dimensional integral is finite.

Thus, for `alpha in B`, **relative interior of the Newton polytope is equivalent to coercivity and to integrability of `e^{-H_alpha}` on the effective quotient**. This is *strictly stronger* than the original lemma's bounded-below criterion `alpha in B`, and does not claim integrability in the unreduced ambient space when `V^perp` is nontrivial.

**One-dimensional exact sharpness check.** With `beta_1=0`, `beta_2=b>0`, `alpha=a`, 
```text
e^{-H_a(x)}=e^{a x}/(1+e^{b x}).
```
At `x -> -infinity`, integrability requires `a>0`, while at `x -> +infinity` it requires `a<b`. Therefore `integral_R e^{-H_a} dx < infinity` iff `0<a<b`. The endpoint `a=0` or `a=b` is bounded below in the original Lemma 21.4.6 but has divergent integral. At the symmetric interior point `a=b/2`, the elementary substitution `t=e^{bx/2}` gives the exact value
```text
integral_R e^{bx/2}/(1+e^{bx}) dx
  = (2/b) integral_0^infinity dt/(1+t^2) = pi/b.
```
This verifies the threshold and its finite normalization without quoting any external special-function identity.

**Disposition and dependents:** An optional statement clarifying interior-versus-boundary Newton exponent integrability could be added as a separate reviewable patch. It is relevant to toric convex weights and monomial quotient growth (§§21.4, 21.9), but is **not** an audit of analytic multiplier ideal regularization. No original lemma is false, and this is not a proof-gap repair.

## Scope and pending items

- **New selected direct mathematical proof work:** §21.4.6, its relative-interior coercivity criterion, and §§21.9.2/.5, the exact facet vanishing-order filtration and DH measure. **Incremental only** (earlier §21.4/21.9 passages were reviewed); §19.6.5/.7/.18 and §21.7.3 read as explicitly named definitions/conditional internal dependencies and **not** counted as first or whole-section certification.
- Current production table of contents remains **25 chapters and 747 distinct numbered sections**. None was fully mathematically certified in this session. The older §19.6.16 confirmed error, toric chart cross-reference cycle, and any proof gaps, external dependencies and genuine duplicate assessments remain unchanged, and are *not* new findings.
- The entire user-excluded Demailly approximation/regularization, dedicated Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss work is **deferred-by-user**; no proofs or prerequisites in that programme reopened.
- No main/source/body/registry/canonicalization/permanent-tag/site edits, no website publication, no GitHub Actions CI, no tests, builds, automation changes or formal verification. The algebra and limits are checked by the displayed finite-dimensional arguments, not by external computation.
