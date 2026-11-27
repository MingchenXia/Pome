# Weak-Lp stability and the polar Gauduchon trace budget

Date: 2026-11-27. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit parent: c02b3eac835caa7bbdedb020cde07d53047aeb08.

## Scope and exact anchors

* Whole direct conditional §15.14, mathematical lines 7–99 of docs/sections/equations-with-prescribed-singularities--subsolutions-and-the-gauduchon-trace/index.html (blob c7c809b0cbd96e0deeece05d4aa2309527796536). Lemma 15.14.1 source non-kahler-pluripotential-theory:7537970B, permanent 869D3138741D, lines 11–50; Proposition 15.14.2 source FDEEE883, permanent 0A5580561320, lines 55–99; equation source 69A7C08E, permanent B100E71E56DE.
* Whole direct conditional §15.15, mathematical lines 7–97 of docs/sections/equations-with-prescribed-singularities--stability-above-a-strict-barrier/index.html (blob 2a884ceafcc821213e77ad5d9e70d69fe35475bb). Theorem 15.15.1 source D2956B4A, permanent 668D07ADFF44, lines 11–71; Corollary 15.15.3 source 31E24C9E, permanent 131F17206F6A, lines 76–93.
* Selected dependency §15.13 lines 14–118, docs/sections/equations-with-prescribed-singularities--comparison-above-a-strict-singular-barrier/index.html (blob db560c935a7d651803427b6243957ea1f957b468); in particular strict domination 15.13.2, permanent F71978C42841. Existence of its fixed strict analytic barrier at line 10, citing 5.36.5, is an assumed input; any excluded regularization proof remains deferred-by-user, not certified.
* Selected §5.28.7 and §5.28.13, lines 134–180 and 222–249, docs/sections/plurisubharmonic-functions-and-singularities--products-with-smooth-backgrounds/index.html (blob e2ba89b51376ba0296846221109c664a0c29b2c3), permanent 6C81352D9EE7 and D263A93C1D69. Selected Lemma 5.26.2, lines 18–42 of docs/sections/plurisubharmonic-functions-and-singularities--uniform-exponential-integrability/index.html (blob d961c0412577bb6abdb8455efc44e2f35760c55c). Skoda qualitative integrability is an external input of that proof, not re-established here. Selected 15.3.1, lines 20–63 of docs/sections/equations-with-prescribed-singularities--bounded-equations-in-a-semipositive-big-background/index.html (blob 84f49b16943ee4e0d5dcf8d8bf59cd815a1ef15f).
* Selected §15.19 lines 7–312, docs/sections/equations-with-prescribed-singularities--degenerating-semipositive-backgrounds/index.html (blob 5ed2b285e8306f0a803df40712b93ed4054851a8); read uniform bounds, differentiated trace estimate, monotonicity and small-resolution barrier, and the statement of 15.19.14. No claim of full coverage or verification of the remaining metric convergence and density proofs. Interior Evans–Krylov/Schauder and smooth existence are conditional inputs.

No historical first-visit claim. The main's actual home table of contents was parsed: 747 section numbers, and the audit matrix had exactly 747 unique corresponding rows, no missing or extra numbers.

## POME-BARRIER-STABILITY-WEAK-LP-001

Low / verified conditional deduction, not a false printed theorem or repair. Theorem 15.15.1 and its compactness corollary continue to hold for a uniform weak-L^p density bound, for every p>1, with the same strict range of stability exponents. This includes densities not in strong L^p. Here and below take the fixed strict barrier and its pole set from §15.13, and all the other hypotheses of the printed statements.

Write m=dV, and use the equivalent Banach norm on nonnegative weak-L^p functions
\[
N_p(f)=\sup_{0<m(E)<\infty}m(E)^{-1+1/p}\int_E f\,dm.
\]
Assume N_p(f)≤L. By testing E={f>s} we have m{f>s}≤(L/s)^p. For every measurable E of positive mass and every 1<q<p, layer cake and splitting at s_0=L m(E)^{-1/p} give
\[
\int_E f^q\,dm \le q\int_0^\infty s^{q-1}\min(m(E),(L/s)^p)\,ds
=\frac p{p-q}L^q m(E)^{1-q/p}.
\]
The null-set and L=0 cases are immediate. In particular f belongs to every L^q with 1<q<p, but the decisive point is the quantitative restricted estimate, which preserves the original limiting exponent p rather than substituting a smaller strong exponent.

Apply the exact construction in lines 31–61 of Theorem 15.15.1 with the selected q: replace v by max(v,u), set E_delta={u<v-delta}∩Omega, and use the auxiliary normalized density 1_E f / ||1_E f||_q in Lemma 15.14.1. The lemma requires only an L^q bound. Its reference-uniform constant b therefore applies unchanged. All cases (zero, small positive and large restricted norm) give
\[
\sup_\Omega(v-u)_+\le\delta+C_1\|\mathbf1_{E_\delta}f\|_q^{1/n}.
\]
For I=∫(v-u)_+ dm, Chebyshev and the layer-cake estimate bound the second term by C(I/delta)^a, a=(1/q-1/p)/n. For 0<I≤1 choose delta=I^{a/(1+a)}; for I>1 use the printed uniform C_0 bound, and for I=0 use canonical representatives. Thus the exponent is a/(1+a)=(p-q)/(npq+p-q). Let q>1 be sufficiently close to one for each prescribed gamma<(p-1)/(np+p-1). No claim at the limiting exponent.

For the compactness corollary fix eta and the bound N_p(f)≤L. The pairwise estimate holds in both directions, so any L^1-convergent sequence of potentials is uniformly Cauchy in differences on Omega. For each fixed 1<r<p, the density bound gives a bounded set in reflexive L^r. Along a weakly convergent subsequence, uniform local potential convergence and bounded-product continuity identify the limiting density on Omega, and neither measure charges Z. Positivity passes to the weak limit. Moreover for every measurable E, 1_E belongs to L^{r'} on the finite measure space, so ∫_E f≤L m(E)^{1-1/p} passes to the limit; this proves N_p(f)≤L with exactly the same constant, without falsely assuming lower semicontinuity of a distribution-function quasi-norm. Every weak cluster point in L^r is the same density; weak convergence of the whole sequence follows by reflexive weak compactness (or a subsequence argument). The common bounds between eta-C_0 and eta give L^1 precompactness as in the printed proof. The space of differences with the uniform metric is metric, so the sequential compactness argument suffices. This yields compactness and weak L^r convergence for every 1<r<p, not weak convergence in L^p. On a positive-dimensional coordinate ball the model f=|z|^{-2n/p} cut off inside the ball lies in weak L^p and not strong L^p, showing the density class is strictly larger (no assertion that this model has a solution in every prescribed class).

Proposed addition: a remark after 15.15.3 recording the Lorentz variant, including the precise weak norm and altered density convergence. Affected dependents: 15.15.3 directly; uses elsewhere of the strong-L^p stability theorem can adopt this variant only after their remaining existence and density hypotheses are checked.

## POME-GAUDUCHON-POLAR-TRACE-BUDGET-001

Low / verified conditional deduction, not a false printed theorem. Under Proposition 15.14.2 retain its strict barrier and local boundedness hypotheses. Define the positive finite trace measure tau_u=(theta+dd^c u)∧gamma^{n-1}; its total mass is T_gamma by Stokes, even if the background is not closed. Put P_u=tau_u(Z). The local inequality at lines 82–88 actually yields the stronger budget
\[
\int_X F^{1/n}G^{1-1/n}\,dm\le T_\gamma-P_u .
\]
Indeed integrate on Omega, using m(Z)=0 and the exact mass tau_u(Omega)=T_gamma-P_u; no product on Z is used. If a positive current S supported on Z is dominated by theta+dd^c u, then P_u≥∫S∧gamma^{n-1}. In particular prescribed effective divisorial components supported on Z reduce the available budget by their Gauduchon trace; this is conditional on the stated domination, not inferred merely from the lower barrier.

Let f≥0 be nonzero in L^p, p>1, and v normalized by sup v=0 with MA(v)=c exp(lambda v) f dm, lambda≥0, c>0, and v≥rho-C_v. Define W=f^{1/n}G^{1-1/n}, A=∫W dm>0, and the probability dσ=W dm/A. Let Y=-v≥0 a.e. and M_v=∫Y dσ. The trace inequality implies
\[
c\le ((T_\gamma-P_v)/A)^n\bigl(\mathbb E_\sigma e^{-\lambda Y/n}\bigr)^{-n}
\le ((T_\gamma-P_v)/A)^n e^{\lambda M_v},
\]
the last inequality by Jensen. The budget is positive whenever such c exists. For fixed f the moments of every finite order of Y are bounded uniformly in normalized v: dominate theta by a fixed Hermitian form and apply the normalized exponential estimate of 5.26.2, then Hölder with W in L^{np} (the smooth factor is bounded). More generally the same normalized moment bounds hold uniformly for f varying with a common L^p bound and A bounded away from zero.

As lambda→0+, Taylor's formula with remainder bounded by s^3Y^3/6 for s=lambda/n≥0 gives
\[
\mathbb E e^{-sY}=1-sM_v+\tfrac12s^2\mathbb E Y^2+O(s^3)
\]
uniformly in v. The logarithm expansion at 1, justified by the uniform first three moments, yields the sharper uniform upper estimate
\[
c\le ((T_\gamma-P_v)/A)^n
 \exp\left(\lambda M_v-\frac{\lambda^2}{2n}\operatorname{Var}_\sigma(Y)+O(\lambda^3)\right).
\]
Here O(lambda^3) is a uniformly bounded error in the *upper estimate*, not a claimed asymptotic equality for c. In particular the last assertion of Proposition 15.14.2 for lambda_j=1/j improves to c_j≤(T_gamma/A)^n exp(C/j). If P_{v_j}≥P_* uniformly, replace T_gamma by T_gamma-P_*. For fixed f the leading constant without polar subtraction is attained, for example, on a compact Kähler manifold with theta=gamma, f=G and v=0, c=1; then Z can be empty and A=T_gamma. This is sharp as a universal leading bound, not an assertion of equality in a general background.

For an unnormalized solution u with MA(u)=exp(lambda u)f dm, lambda>0, set v=u-sup u and c=exp(lambda sup u); its polar trace is unchanged. The Jensen bound gives the explicit upper bound sup u≤(n/lambda) log((T_gamma-P_v)/A)+M_v. No total Monge–Ampère mass bound, uniform lower bound on c, or existence conclusion is used.

Proposed addition: retain the stronger trace budget in 15.14.2 and add the quantitative normalized estimate. Downstream normalized equation arguments using only the original upper bound remain valid; the stronger bound does not certify capacity compactness, convergence of P_v, or uniqueness.

## Local audit checks and outstanding dependencies

* In 15.14.1 the variable of the convex function is u_1-eta≤0, so its derivative is t^{-2} and the second derivative is 2t^{-3}; the negative sign in the difference gradient cancels upon squaring. The compensating density power 2n and t≤2-rho are consistent.
* In 15.15.1 the threshold t=(2m_delta/b)^{1/n}<1 ensures the local mixed-product dominance on {u<w}; the zero-density case uses coefficient zero, and the large-density case uses the original C_0 bound. The proof of 15.15.3 correctly obtains the uniform difference estimate before identifying the limiting equation.
* In 15.13.2 the approximate minimizer is not assumed to attain an infimum of differences of quasi-psh functions. The strict barrier forces it away from Z, then the local comparison with a strictly positive bump yields the contradiction. The envelope contact theorem and mixed-product calculus are assumed dependencies, not fully certified.
* In the selected part of 15.19 the determinant/trace inequality S≤nDR^{n-1}, the sign of the logarithmic weight second derivative, the monotonicity of the normalizing constant under increasing backgrounds, and the positive base curvature dd^c log(1+|z|²) in the node resolution are consistent. No verification of the later metric convergence arguments or independent proof of the interior PDE estimates is asserted.

No new confirmed false theorem or demonstrated local proof gap in these two full sections. Both findings are conditional on the named internal inputs and the fixed barrier. Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, atlas and positivity-loss programme remain deferred-by-user, not resolved. No test, build, CI, publication, source or registry edit; no complete transitive proof-chain certificate.
