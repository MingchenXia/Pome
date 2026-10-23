# Mathematical audit: radial current densities and a discontinuous Lelong-number limit

**Checkpoint:** 2026-10-23 22:48 Asia/Shanghai. **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Starting review head:** `083c6e784a6a2ece5131f3710fc4c9b08d8726e9` (preserve; never reset). This is an audit-only, optional corollary and explicit counterexample to an *unasserted* continuity inference; **not** a refutation or correction of Pome's printed theorems.

## Exact integrated mathematical sources and coverage

- `docs/sections/real-currents-submersions-and-homotopies--radial-positive-currents/index.html`, blob `994a47ced79c1995630dd32b0d9703faddf9c173`: radial forms and probability normalization lines 7–23; Theorem 5.58.3, source label `demailly-complex-geometry:2AE78FA4`, permanent tag `FB41A7CE1CEE`, lines 47–88, especially the coefficient-current classification (Eq. 5.58.4, tag `2A9B47FEBEC7`); Proposition 5.58.6, source `demailly-complex-geometry:3B4BB9CB`, tag `56D537355910`, lines 93–122 (context only); Corollary 5.58.9, source `demailly-complex-geometry:8E5FA97B`, tag `4F0954956743`, lines 127–155, especially the trace/ball formula lines 136–148.
- `docs/sections/lelong-densities-generalized-masses-and-multiplicity--lelong-densities-of-positive-currents/index.html`, blob `48bb9c525a826e4d1e337b755fac22aaa3016e66`: normalization lines 9–22; Theorem 6.33.1, source `demailly-complex-geometry:B0B6D8E5`, tag `7ACCEC6E0526`, lines 25–39 (statement and density normalization only, not its full proof).
- The only §5.60 input used is the **already printed** closed zero-extension conclusion cited at §5.58.9: its independent global Skoda–El Mir proof, relative Richberg smoothing and the rest of §5.60 were **not** reopened. This checkpoint does not enter Demailly regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas or positivity-loss proof-completion.

**Actual new selected review:** §5.58 (the radial tensor/eigenvalue reduction, distributional coefficient identity, trace normalization and extension distinction) with one dependency-only comparison to §6.33.1. This is **not** certification of all of §5.58, §6.33 or the 25 chapters / 747 indexed sections.

## POME-RADIAL-LELONG-DENSITY-JUMP-001

**Status:** `verified conditional deduction`; **severity:** low (sharp diagnosis of a limiting-operation trap, NOT a false printed theorem, missing hypothesis, or completed verification of upstream classification).

Let `n>=2` and `1<=p<n`, and put `m=n-p`. On `C^n\{0}`, write

\[
t=\log|z|^2,\quad
\theta=d^ct,\quad\beta=dd^ct,\quad
\gamma=dt\wedge\theta,\quad
\beta_0=dd^c|z|^2.
\]

Every closed positive `U(n)`-invariant `(p,p)` current in Theorem 5.58.3 has the unique monotone coefficient `u`, with

\[
T=u(t)\beta^p+(Du)(dt)\wedge\theta\wedge\beta^{p-1}.
\]

Let `\widetilde T` denote its unique closed positive zero extension to `C^n` from Corollary 5.58.9. For **every** `R>0`, the trace mass of the *open* centered ball is exactly

\[
\boxed{\int_{B(0,R)}\widetilde T\wedge\beta_0^m
=R^{2m}u((2\log R)-).}\tag{1}
\]

Consequently, in precisely the §6.33 normalization (no factorial),

\[
\boxed{\nu(\widetilde T,0)
=\lim_{t\to-\infty}u(t).}\tag{2}
\]

If `T=(dd^c\chi(t))^p` with finite convex nondecreasing `\chi`, then `u=(\chi')^p` almost everywhere, with canonical monotone representative, and thus

\[
\boxed{\nu(\widetilde T,0)
=\bigl(\lim_{t\to-\infty}\chi'_+(t)\bigr)^p.}\tag{3}
\]

**Proof of (1)–(3).** Corollary 5.58.9 computes
`T\wedge\beta_0^m=e^{mt}(mu(t)dt+Du(dt))\wedge\sigma`, with `\int\sigma=1`. Its scalar measure is precisely `D(e^{mt}u)`, by the distributional BV product rule. The monotone function `u` is bounded on every left half-line, so `e^{mt}u(t)\to0` as `t\to-\infty`. Integrating to the **strict** bound `t<2\log R` yields the left representative `u((2\log R)-)`, accounting exactly for possible shell atoms. The zero extension has no mass supported at the origin because `p<n`. Divide (1) by `R^{2m}` and take `R\downarrow0`, using the definition in §6.33. Finally Theorem 5.58.3 gives `u=(\chi')^p`; convexity and nonnegative monotone derivative make the left-end derivative limit finite and identify (3). QED.

**Exact limiting-operation counterexample.** For every integer `j>=1`, define the globally locally bounded psh potential

\[
\phi_j(z)=\max\{\log|z|^2,-j\},\qquad
T_j=(dd^c\phi_j)^p,\qquad r_j=e^{-j/2}.
\]

The potentials decrease pointwise to `\log|z|^2`, including value `-\infty` at the origin, but each `T_j` is identically zero on `B(0,r_j)`. On the puncture its radial coefficient is `u_j(t)=\mathbf1_{[-j,\infty)}(t)`, hence

\[
T_j=\mathbf1_{\{t>-j\}}\beta^p
+\delta_{-j}(dt)\wedge\theta\wedge\beta^{p-1}
\quad\text{on }\mathbb C^n\setminus\{0\}.
\]

The shell `|z|=r_j` has trace mass **exactly** `r_j^{2m}`; the interior contributes zero. From (1) the entire normalized centered-ball density is

\[
\boxed{
D_{T_j}(0,R)=
\begin{cases}
0,&0<R\le r_j,\\
1,&R>r_j.
\end{cases}}\tag{4}
\]

For the weak limit `T_\infty=\widetilde{\beta^p}`, the density is exactly `D_{T_\infty}(0,R)=1` at every `R>0`. Moreover, `T_j=T_\infty` off the closed ball of radius `r_j`; both trace measures of that closed ball equal `r_j^{2m}`. Positivity and coefficient-measure domination thus imply, for each fixed smooth compactly supported test form `\eta`,

\[
|\langle T_j-T_\infty,\eta\rangle|
\le C_\eta r_j^{2m}=C_\eta e^{-mj}\to0.
\]

This proves **weak convergence on the entire ambient space**, not merely on the puncture. Nevertheless,

\[
\nu(T_j,0)=0\quad\text{for every }j,
\qquad \nu(T_\infty,0)=1.
\]

Hence the two limits of the density do not commute:

\[
\boxed{
\lim_{j\to\infty}\lim_{R\downarrow0}D_{T_j}(0,R)=0,
\qquad
\lim_{R\downarrow0}\lim_{j\to\infty}D_{T_j}(0,R)=1.}
\]

This is compatible with the usual upper-semicontinuity of Lelong numbers under weak positive-current convergence. It disproves only the **unasserted** stronger claim of continuity, even for currents arising as classical Bedford–Taylor powers of a decreasing sequence of locally bounded psh functions. There is no need to interchange Bedford–Taylor products for unbounded limits or to use any excluded approximation programme.

**Proposed optional addition:** after Corollary 5.58.9 give formulas (1)–(3) as a sharp density corollary, with example (4) as a warning before using weak convergence in later Lelong-number/current arguments. Keep existing source wording, permanent tags, and general density Theorem 6.33.1 unchanged. Affected potential dependents: §6.33 density semicontinuity, any later singular-current limits in §5.60 / Chapters 6–7; this example does not invalidate their printed statements.

## Verification, exclusions and publication

The displayed flux identity was derived directly from the **printed** distributional radial representation, normalized sphere integral, and open-ball convention; the shell mass and the two limits were independently checked symbolically. This checkpoint does **not** rerun the upstream invariant-distribution smoothing proof, Skoda–El Mir or other deep analytical inputs. A new small exact-rational shell accounting script is only a finite consistency check, not a theorem proof. No complete Pome build, Python/JS test suite, CI, formal verification, public-site publishing, mathematical source editing, canonicalization, tag editing, branch reset or main merge. All dedicated Demailly approximation/regularization, Bergman/L²/OT/multiscale/positivity-loss work remains `deferred-by-user`, without reinspection or certification.
