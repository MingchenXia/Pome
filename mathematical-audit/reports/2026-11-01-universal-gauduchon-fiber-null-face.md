# 2026-11-01 — uniqueness of the exposed null-current face in the Gauduchon radial counterexample

**Production main reviewed:** `b6933b772f41b45918f7e25ed1afbbb1fd892272` (not modified).
**Scope:** the actual integrated reading-edition §§12.14.6, 12.14.10, 12.14.13, 24.3.2, and a separate selected check of §15.32.6; no excluded Demailly approximation, regularization, Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss chain.

## POME-GAUD-UNIVERSAL-FIBER-EXPOSED-001

**Severity:** low. **Status:** verified conditional deduction; not a false statement, not a complete upstream theorem certification, and not a production repair.

**Primary anchors:**
- `docs/sections/a-gauduchon-variational-volume--positive-volume-without-bigness/index.html`, blob `4e892ab379abdfa3b6520671db344e94bbc7a51a`: setup **lines 10–20**, Theorem **12.14.6** (source `non-kahler-pluripotential-theory:7A1559DF`, permanent tag `ECAB6BFB33FD`) **lines 100–140**, normalized explicit tests Proposition **12.14.10** (source `non-kahler-pluripotential-theory:EDD3E86A`, tag `0E9506DB4E70`) **lines 169–205**, and Proposition **12.14.13** (source `non-kahler-pluripotential-theory:4D5B675F`, tag `F8EA88FD522E`) **lines 243–274**.
- `docs/sections/problems-in-hermitian-pluripotential-theory--positive-gauduchon-volume-and-bigness/index.html`, blob `e64a919194dbc4dbd1739cd02811a5c45e252358`: Proposition **24.3.2**, source `non-kahler-pluripotential-theory:B0E460AB`, permanent `32F82EA89236`, **lines 26–68**; determinant quotient and collapse discussion **lines 71–84**.

### New assertion: every almost-null normalized Gauduchon test has the same limit

In the printed example let `m>=2`, `n=m+1`, `B=P^m`, `X=B x P^1`, and write `omega,w` for normalized Fubini–Study forms with `int_B omega^m=int_{P^1}w=1`. Set
[
 t=(m-1)/m,quad
 x([Z_0:cdots:Z_m])=rac{sum_{1}^{m}|Z_i|^2}{sum_{0}^{m}|Z_i|^2},quad
 a=x/t,quad h=omega+w,quad 	heta=omega+a,w.
]
Let `p=[1:0:...:0]` and `Z={p}xP^1`, so `int_Z h=1`. On the cone of positive `(m,m)` currents consider
[
 mathscr C={Tge0: dd^cT=0, int_X hwedge T=1}.
]
Then the **exposed zero face is exactly one point**:
[
 oxed{{Tinmathscr C: int_X	hetawedge T=0}={[Z]}.}	ag{*}
]
Consequently, for **any net** `T_alpha` in `mathscr C` with `int_X theta wedge T_alpha ->0`, one has `T_alpha -> [Z]` weakly. In particular, if `gamma_alpha` are smooth Gauduchon metrics, `int_X h wedge gamma_alpha^m=1`, and `int_X theta wedge gamma_alpha^m ->0`, then `gamma_alpha^m ->[Z]` along the **original net**. Moreover, for these smooth metrics, `D_mu(gamma_alpha)->0` conditional on the printed `lambda_mu(theta)=n^{1/n}>0`. Unlike Proposition 12.14.13, which *constructs one family*, (*) classifies **every** almost-minimizing Gauduchon family and every positive `dd^c`-closed normalized cluster current.

### Complete local argument for (*)

1. **Compactness without sequential assumptions.** Positivity and the fixed `h`-trace mass imply a uniform bound for all coefficient measures of each `(m,m)` current. Weak-* compactness of the mass-one positive-current set gives cluster points for arbitrary nets; positivity, the linear trace, and the `dd^c`-closure identity pass under weak convergence. The set `mathscr C` is weakly compact and Hausdorff.
2. **Support and tangency.** `	heta` is semipositive and **strictly positive away from** `Z`; at points of `Z` it has rank `m` with one-dimensional kernel equal to the vertical tangent `T(P^1)`. If `T>=0` and `int theta wedge T=0`, then the positive measure `	hetawedge T` vanishes. Thus `T` is supported on `Z` (on every compact set outside `Z`, `	heta>=c h` for some `c>0`). On `Z`, its positive coefficient matrix has zero contraction with the horizontally strictly positive form `omega`. Nonnegative diagonal measures and the Cauchy–Schwarz inequalities for a positive matrix of measures show that every horizontal and mixed tangent coefficient vanishes. Only its **vertical** tangent coefficient remains, so `T=i_*
u` for a positive finite measure `
u` on `Z=P^1`, interpreted by `T(eta)=int_Z(eta|_Z/w),d
u` for smooth test `(1,1)` forms `eta`.
3. **Harmonic rigidity rather than a closed-current assumption.** Since `dd^cT=0`, for every smooth real function `f` on `P^1` and its smooth extension to `X`,
[
 0=T(dd^cwidetilde f)
   =int_Zrac{dd^cf}{w},d
u.
]
For every smooth zero-`w`-mean function `g` on `P^1`, the ordinary compact Riemann-surface Poisson equation solves `dd^cf=g,w` after the harmless fixed normalization of `dd^c`. Hence `int g,d
u=0`, implying `
u=cw`. The trace normalization gives `1=int hwedge T=
u(Z)=c`, and so `T=[Z]`. This uses only the elementary Poisson solvability on `P^1`, positive-current coefficient bounds and `dd^c)-closure; **it never replaces Gauduchon by balanced or `dd^c)-closed by `d)-closed**.
4. **Net convergence.** Every cluster point of `T_alpha` has zero `	heta`-pairing and so equals `[Z]`; weak compactness plus uniqueness of all cluster points implies the entire original net converges. For smooth Gauduchon powers, the original definition of `lambda_mu(	heta)>0` gives `lambda_mu(	heta)D_mu(gamma_alpha)leint	hetawedgegamma_alpha^m`, proving the stated determinant collapse.

### Exact quantitative concentration estimate and sharpness

For any `0<r<t`, on `{xge r}` one has `	heta=omega+(x/t)wge(r/t)(omega+w)=(r/t)h`. Therefore every positive `(m,m)` current `T` satisfies
[
 oxed{int_{{xge r}}hwedge T le rac{t}{r}int_X	hetawedge T.}	ag{**}
]
The constant `t/r` is **sharp** already among positive closed `(m,m)` currents: for `qin B` with `x(q)=r`, take `T=[{q}	imes P^1]`; both trace and the right-hand side of (**) equal `1`. It is also asymptotically sharp among **smooth balanced powers**, not just singular currents: choose `q_epsilon	o q` with `x(q_epsilon)>r` and nonnegative smooth probability densities `f_epsilonomega^m` on `B`, supported in `{x>r}` near `q_epsilon`. Put
[
 Gamma_epsilon=rac{f_epsilonomega^m+epsilon h^m}{1+nepsilon}.
]
This is smooth, strictly positive and `d`-closed with `int hwedgeGamma_epsilon=1`; the positive-root theorem used at §12.14.13 supplies a smooth balanced `b_epsilon` with `b_epsilon^m=Gamma_epsilon`. As `epsilondownarrow0`, its mass over `{xge r}` tends to `1`, while `int	hetawedgeGamma_epsilon	o r/t`. Hence the ratio tends to `t/r`, verifying sharpness without assuming arbitrary singular currents are balanced metric powers.

### Mathematical classification and affected dependents

Theorem 12.14.6, Proposition 12.14.13 and Proposition 24.3.2 **remain correct as stated** in the checked passages. The new result is an optional strengthening of the **uniqueness of the normalized null-test limit**, together with a sharp off-fiber concentration bound. The `D_mu` consequence remains conditional on the printed root-volume value; the exposed-face calculation itself does **not** use any approximation/regularization or the volume-minimizer construction. Affected interpretation: the §12.14.10–13 distinction between volume-minimizing and bigness-threshold-minimizing tests, §24.3.2 denominator-collapse discussion, and the Gauduchon-current compactness context of §11.6. No source theorem is proposed for deletion, no permanent tags or source attributions are altered.

**Separately selected crosscheck, no new verdict:** §15.32.6, `docs/sections/equations-with-prescribed-singularities--stability-of-the-subsolution-threshold/index.html` blob `903ae0ce7173604063a833295dd94e971b18fd72`, source `non-kahler-pluripotential-theory:500DB50B`, permanent `C926F63790E3`, **lines 103–129**: checked the converse norm-completeness construction's `L^1` embedding, positive partial sums and `L^n` obstruction as a selected proof step. The equivalence with infinite upper volume still uses the indicated §§12.15.4 and 12.2.3 inputs and is not recertified. This was historically sampled (§15.32); it is **not** first reviewed or certified here.

**Coverage accounting:** additional selected proof-level examination of §24.3.2 (previously directly sampled on 2026-10-29), plus fresh §12.14.6/.10/.13 proof-step examination and §15.32.6 contextual check; **no entire numbered mathematical section or transitive proof chain certified**. The actual current main ToC remains **25 chapters / 747 sections / zero complete certifications**. Previous confirmed errors, proof gaps, external inputs and proposed-but-unapplied repairs are unchanged; all user-deferred Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss work remains **deferred-by-user, not resolved**.

**Operations:** audit Markdown only, intended for `review/mathematical-audit`; no main, source/body, canonicalization, registry, tag, built docs, CI, formalization, mathematical software tests or website publication changes.