# Quantitative Kähler-background mass continuity and a familywise minimax identity

Date: 2026-11-19. Reviewed production **main**: `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Review branch: `review/mathematical-audit`.

## Scope and source anchors

**New finding `POME-NA-BACKGROUND-MASS-LIPSCHITZ-MINIMAX-001`** — severity **low**; status **verified conditional deduction**, **not** a printed false theorem and **not** a complete upstream proof-chain certificate.

- Direct reading-edition source: `docs/sections/non-archimedean-pluripotential-theory/index.html`, blob `8448d710690ebe1cc28040f9611d05c9d008a961`; Definition **22.1.7**, source `sgpt:6F37B588`, permanent `A92D6DFAC0CF`, physical lines **118–123**; Proposition **22.1.39**, source `sgpt:20714EEA`, permanent `15E20104530B`, equation `AA5696D80091`, physical lines **614–674**, especially **647–671**. We also read §22.1.21–24 and §22.1.34–38 at **347–409 and 538–612** to inspect the order, regularized supremum, and dependency context, **not** the entire very long §22.1.
- Internal supporting statements independently located and checked **at statement level only**: Proposition **17.12.19**, source `sgpt:129B6722`, permanent `724BF0CAE002` (background projection and left endpoint), and Theorem **13.13.11**, source `sgpt:00CC32E0`, permanent `0E5F6133B048` (mixed non-pluripolar mass monotonicity). The existing §22.1.39 proof also uses the standard multilinearity with smooth semipositive forms and the transfer of ordinary P-singularity types. These remain **conditional upstream inputs**. None involves the user-excluded regularization proof-completion programme.
- The earlier 2026-11-18 **cofinal Kähler ray / inverse-limit** result is retained as earlier work, **not** logged as new here. Today's increment concerns a **uniform quantitative modulus in the perturbation form** and a **familywise inf–sup identity without order or countability assumptions**.

## Proposition (uniform scalar mass modulus)

Let `X` be a connected compact Kähler manifold of dimension `n>=1`, `theta` a smooth closed real `(1,1)`-form with pseudo-effective class, and `omega_0` a fixed Kähler form. For any `Gamma in PSH^NA(X,theta)` and Kähler form `alpha`, set

\[
M_\Gamma(\alpha):=\int_X\left\langle
(\theta+\alpha+dd^c\Gamma^{\theta+\alpha}_{-\infty})^n
\right\rangle.
\]

Choose a Kähler form `Omega` with `Omega >= theta+(A+1)omega_0` and `A>0`. For any **Kähler** `alpha,beta` satisfying `alpha,beta <= A omega_0` and any `0<=epsilon<=1` such that
\[-\epsilon\omega_0\leq\alpha-\beta\leq\epsilon\omega_0,\]
we have **uniformly in every `Gamma`**
\[
\boxed{\left|M_\Gamma(\alpha)-M_\Gamma(\beta)\right|
\leq\sum_{k=1}^n{n\choose k}\epsilon^k
\int_X\Omega^{n-k}\wedge\omega_0^k
\leq C_\Omega\epsilon,}\qquad
C_\Omega=\int_X[(\Omega+\omega_0)^n-\Omega^n].
\]

For a single shrinking ray `0<s<t<=1`, with `Omega >= theta+omega_0`, the stronger exact polynomial identity is
\[
\boxed{M_\Gamma(t\omega_0)-M_\Gamma(s\omega_0)
=\sum_{k=1}^n{n\choose k}(t-s)^k
\int_X\left\langle T_s^{n-k}\right\rangle\wedge\omega_0^k,}
\]
where `T_s=theta+s omega_0+dd^c Gamma^{theta+s omega_0}_{-infty}`.
In particular, passing to the decreasing limit **through positive `s`**, without treating a possibly non-big `theta` as a positive background,
\[
\boxed{0\leq M_\Gamma(t\omega_0)-\operatorname{vol}\Gamma
\leq C_\Omega t\quad(0<t\leq1).}
\]
This estimate is uniform over the *whole* NA space, not merely an increasing or bounded-above family.

### Proof

The comparison in printed §22.1.39, lines 659–668, applies to any two Kähler forms `beta <= gamma`: the inverse-limit transition and §17.12.19 show that the two left-endpoint potentials represent the same ordinary P-singularity in the larger class. Thus the larger endpoint mass can be computed with the smaller-class potential:
\[
M_\Gamma(\gamma)=\int_X\left\langle
(T_\beta+\gamma-\beta)^n\right\rangle,
\quad
T_\beta:=\theta+\beta+dd^c\Gamma^{\theta+\beta}_{-\infty}.
\]
Multilinearity with a smooth semipositive form, and the mixed-mass monotonicity §13.13.11 used in the printed proof, give
\[
0\leq M_\Gamma(\beta+\epsilon\omega_0)-M_\Gamma(\beta)
=\sum_{k=1}^n{n\choose k}\epsilon^k
\int_X\langle T_\beta^{n-k}\rangle\wedge\omega_0^k
\leq\sum_{k=1}^n{n\choose k}\epsilon^k
\int_X\Omega^{n-k}\wedge\omega_0^k.
\]
For the last bound one may use the smooth form `Omega-(theta+beta)>=0` and compare with a smooth `Omega`-psh potential (zero), precisely the mixed-mass upper estimate in printed lines 668–671. The hypothesis `beta+epsilon omega_0<=(A+1)omega_0` makes the same constant valid for all choices of `beta` and `Gamma`.

Now `alpha<=beta+epsilon omega_0`, and `beta<=alpha+epsilon omega_0`. Background monotonicity (also recorded immediately after Definition 22.1.7) gives
\[
M_\Gamma(\alpha)-M_\Gamma(\beta)
\leq M_\Gamma(\beta+\epsilon\omega_0)-M_\Gamma(\beta)
\]
and the symmetric bound after exchanging `alpha,beta`. This proves the two-sided estimate **without** comparing two potentially noncomparable currents directly. On the ray `s<t`, take `gamma=t omega_0`, `beta=s omega_0` in the exact multilinear expansion. Since `(t-s)^k <= t-s` for `t-s<=1`, obtain `0<=M(t)-M(s)<=C_Omega(t-s)`. As `s` decreases to zero, Definition 22.1.7 gives `M(s)->vol Gamma` by monotonicity; the displayed bound survives the limit. QED.

**Sharp exponent.** If `theta=omega_0` is Kähler and `Gamma` is the trivial zero-level test-curve metric, each left endpoint is zero, so
\[
M_\Gamma(t\omega_0)=(1+t)^n\int_X\omega_0^n,
\qquad
M_\Gamma(t\omega_0)-\operatorname{vol}\Gamma
=nt\int_X\omega_0^n+O(t^2).
\]
No universal `o(t)` modulus can replace the linear order, even with completely smooth positive backgrounds. The example does not claim the displayed coarse constant `C_Omega` itself is optimal.

## Corollary (exact arbitrary-family inf–sup interchange)

For any **nonempty, arbitrarily indexed** family `F subset PSH^NA(X,theta)`, with **no** monotonicity, upper bound on the maximal test-curve parameter, sequence hypothesis, or countable subfamily requirement,
\[
\boxed{
\inf_{\alpha\in\mathrm{K\ddot ah}(X)}
\sup_{\Gamma\in F}M_\Gamma(\alpha)
=
\sup_{\Gamma\in F}\operatorname{vol}\Gamma.
}
\]
Indeed, every `M_Gamma(alpha)>=vol Gamma`. Conversely for the single fixed ray `alpha=t omega_0`, the preceding **same** constant gives
\[
\sup_{\Gamma\in F}M_\Gamma(t\omega_0)
\leq\sup_{\Gamma\in F}\operatorname{vol}\Gamma+C_\Omega t.
\]
Take `t\downarrow0`. This is a valid **uniform** exchange of scalar `sup` and background `inf`; it is **not** an exchange of non-pluripolar products, convergence of measures, or a statement about the existence of a supremum potential for arbitrary `F`. The absence of such an existence claim matters.

This refines the scalar uniformity step in the proof of Proposition 22.1.39 (lines 635–671): that theorem still needs its *separate* positive-volume fixed-background monotone-net argument, so we do not claim to have certified its entire upstream proof chain.

## Classification, correction scope, dependents

- **Status:** verified conditional deduction. **Severity:** low. **Printed Proposition 22.1.39 remains correct** on the directly tested argument; we have found no confirmed error in the inspected lines. One may add the quantitative proposition/corollary as a **proposed** auxiliary lemma near §22.1.39; **no production patch** is part of this audit.
- **Directly affected readers:** the uniform-background step of §22.1.39, NA volume comparisons as `omega->0`, and future arbitrary-family mass estimates. No change to permanent labels, legacy conventions, or historical attribution.
- **Limitations:** the internal mass monotonicity, P-singularity transfer and NPP smooth-factor multilinearity are accepted as explicit dependencies, **not re-proved from their full upstream chains**. No conclusion about weak convergence, masses of arbitrary signed currents, or positivity-loss regularization is asserted.
- **Coverage:** one **selected substantive proof** in §22.1 (Definition 22.1.7 and Proposition 22.1.39, plus related order/supremum context), **+0 whole sections**, **+0 full upstream-chain certifications**, **+0 claimed first visits**. Existing earlier reports for §22.1 remain intact.
- **Policy:** excluded Demailly approximation/regularization, dedicated Bergman, `L^2`, Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof-completion programmes remain **deferred-by-user**, neither resolved nor certified. No tests/builds/CI or publication were executed.
