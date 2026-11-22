# Continuous nonlinear Hessian data, penalized approximants, and Gaussian kernel energy — 2026-11-23

## Baseline, actual scope

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Initial audit head:** 5636f3929942f6837f4c2af5e53cb9085f81d9e6. This run examined the integrated reading edition, not only source prose.

- Entire current §8.6: docs/sections/complex-hessian-equations--proper-equations-and-admissible-approximation/index.html, blob 841dd207876499be9d83045facf862a323e60994, mathematical physical lines 7–205. These are complex-Hessian cone approximations, *not* the user-excluded Demailly regularization programme.
- Entire current §8.8: docs/sections/complex-hessian-equations--continuous-equations-and-regularity/index.html, blob 62cace2a2bdec93860bf4b5ba9cb4653b4ed2b50, mathematical lines 5–94.
- §4.1 selected only: docs/sections/potentials-energy-and-capacity/index.html, blob 4962a7cd576a64cb47fa0955dcc80cf87c3da9d1, lines 21–241, Gaussian positive kernels, signed logarithmic energy, equilibrium minimization.
- Precisely limited dependency reads: §8.4.6 lines 188–197, blob 3d7fe6d1867a0d8ac268042a59e112329a6c8af3; §8.5.3 lines 63–116, blob fdd9225b1d778e1debaf94f75ef65175d4bd4484; §8.7.9 lines 204–222, blob 045d10eb63453837e8675d22436afa9b9d6335ad.

## POME-HESS-CONTINUOUS-NONLINEAR-DATA-SHARPC0-001

**Severity/status:** low / **verified conditional deduction**. This is **not** a false original theorem, a certification of the full smooth Hessian existence/regularity chain, or a modification of original statements.

**Anchors:** Proposition 8.8.1 (source label 3F168071, permanent tag 5D1E62F09217, reading lines 10–24); Theorem 8.8.3 (source 8B2683EB, permanent 76376AD88152, lines 64–94). Upstream Lemma 8.6.1 (source 91CAEA62, permanent 8B310CC2C1A1, lines 10–39); Lemma 8.7.9 (source F762B147, permanent F28CED8C4FAF, lines 204–222).

**Statement.** Let \(X\) be the compact Hermitian manifold of Chapter 8, \(1\le m\le n\), and \(A<B\). Suppose \(f:X\times[A,B]\to\mathbb R\) is *jointly continuous* and for some \(0<\kappa\le L<\infty\) satisfies
\[
 f(x,A)\le0\le f(x,B),\qquad
 \kappa(t-s)\le f(x,t)-f(x,s)\le L(t-s)
 \quad(A\le s\le t\le B,\ x\in X).
\]
Conditional on the already stated **continuous proper-equation solver** of Proposition 8.8.1, there is a **unique continuous admissible** \(u_f:X\to[A,B]\) satisfying \(H_m(u_f)=e^{f(x,u_f)}\omega^n\). If \(g\) satisfies the same hypotheses and constants, then
\[
 \boxed{\ \|u_f-u_g\|_{C^0(X)}
 \le \frac{1}{\kappa}\|f-g\|_{C^0(X\times[A,B])}.\ }
\]
The coefficient is sharp even for smooth exponents. Pointwise \(f\ge g\) implies \(u_f\le u_g\). **No smoothness or classical strict admissibility is asserted for merely continuous \(f\)**; Theorem 8.8.3's printed smooth conclusion remains restricted to smooth input.

**Complete conditional derivation.** Choose \(a=L\) and the closed complete interval \(\mathcal C=\{v\in C(X):A\le v\le B\}\). For \(v\in\mathcal C\), put \(H_v^f(x)=f(x,v(x))-av(x)\) and denote by \(T_f(v)\) the unique continuous proper solution from 8.8.1 of
\[
 H_m(T_f(v))=e^{aT_f(v)+H_v^f}\omega^n.
\]
The two-sided increments imply \(t\mapsto f(x,t)-at\) is nonincreasing and \((a-\kappa)\)-Lipschitz. Thus
\[
 -aB\le f(x,B)-aB\le H_v^f(x)\le f(x,A)-aA\le-aA.
\]
The proper solver's zero-order bounds imply \(T_f(v)\in\mathcal C\), and its uniform stability estimate gives
\[
 \|T_f(v)-T_f(z)\|_\infty\le q\|v-z\|_\infty,\qquad
 q=1-\kappa/a\in[0,1).
\]
Banach's contraction theorem gives exactly one fixed point \(u_f\in\mathcal C\), which solves the stated weak equation. Conversely, any admissible continuous solution in the interval is a fixed point by uniqueness for the auxiliary proper equation. The argument needs no differentiability of \(f\).

Let \(\eta=\|f-g\|_\infty\). For each \(v\), Proposition 8.8.1 supplies \(\|T_f(v)-T_g(v)\|_\infty\le\eta/a\). Hence
\[
 \|u_f-u_g\|_\infty\le q\|u_f-u_g\|_\infty+\eta/a,
 \qquad
 \|u_f-u_g\|_\infty\le\eta/\kappa.
\]
The proper solver is order-reversing in its datum \(H\), by maximum comparison and uniform approximation as in 8.8.1. As \(H_v^f\) decreases with \(v\), \(T_f\) is order-preserving. If \(f\ge g\), then \(T_f(v)\le T_g(v)\) for each \(v\). Starting the order-preserving \(T_f\) iteration at \(u_g\) produces a decreasing sequence converging uniformly to \(u_f\), proving \(u_f\le u_g\).

For sharpness take any \(c,d\in[A,B]\), and set \(f_c(x,t)=\kappa(t-c)\), \(g_d(x,t)=\kappa(t-d)\), with \(L=\kappa\). The corresponding unique solutions are constants \(u_{f_c}=c\) and \(u_{g_d}=d\), since \(H_m(c)=\omega^n\). Here \(\eta=\kappa|c-d|\), so equality holds.

**Proposed correction / affected dependents:** this is an optional additional *continuous-data corollary* to 8.8.3, after independent editorial scrutiny; it is not a request to repair or replace the printed smooth theorem. Later continuous proper Hessian equations may reuse it with its explicit solver dependency. No direct source, canonicalization, registry, permanent tag or production edit is authorized by this finding.

## Independent proof-step review

**§8.6, entire current text.** At the maximum of \(\varphi-(1+N^{-1})w_N\), the smooth positive \((n-1,n-1)\)-form \(T_N=(\omega+dd^cw_N)^{m-1}\wedge\omega^{n-m}\) permits a linear viscosity upper-test argument even for merely continuous/distributional admissible \(\varphi\). The sign and Gårding normalization give
\[
 (N+1)d_N\ge \omega\wedge T_N/\omega^n\ge d_N^{(m-1)/m},
 \quad d_N=H_m(w_N)/\omega^n,
\]
hence the stated \(E_N=(m\log(N+1)+\log b)/N\); this is not an unjustified evaluation of \(dd^c\varphi\) at a maximum. In Theorem 8.6.6, compactness of \(X\) selects one obstacle index from an increasing open cover; the decrease is by at least \(\varepsilon_{j-1}/4\). The global existence solver in 8.6.1 remains conditional on its elliptic upstream inputs.

**§8.8, entire current text.** Proposition 8.8.1's smooth maximum comparison has the correct sign; uniform approximation of continuous data uses 8.7.1 for product convergence, and 8.7.9 for uniqueness. In 8.8.2, the fixed smooth comparison potential for 8.4.6 is important: its constants do not require derivatives of the varying admissible \(v_j\). Theorem 8.8.3's contraction ratio is exactly \(1-\kappa/a\). No false printed result was confirmed.

**§4.1, selected only.** Lemma 4.1.3 (source 37766360, permanent 21858171114B, physical lines 63–96) correctly factors the Gaussian kernel with coefficient \((4t/\pi)^{d/2}\) and signed Fubini. Proposition 4.1.5 (source DF3A6DB5, permanent 09A0D05A868F, lines 98–176) cancels the logarithmic-scale term **only** for total-mass-zero signed measures after mutual-energy integrability. Theorem 4.1.7 (source A35EEAC5, permanent AA43DD93EFE4, lines 187–241) uses compact-metric support to get weakly convergent equilibrium measures and product-measure convergence by a finite continuous partition; truncated nonnegative kernels give lower semicontinuity and strict energy positivity uniqueness. Lines 242–876 are **not reviewed** in this increment.

## Dependencies and limits

8.8.1 depends on smooth solver 8.6.1, product convergence 8.7.1, and comparison 8.7.9. Smoothness in 8.8.2 depends additionally on §8.4.6 and §8.5.1/.3/.4; §8.5, lines 101–116 explicitly invokes the external **Evans–Krylov–Caffarelli interior estimate**, a genuine analytic input and not merely historical attribution. No upstream transitive chain is certified. This new continuous-data argument requires the continuous proper solver, but not new independent regularity.

**Count:** two whole current mathematical sections directly read, one selected partial section and three selected upstream checks; one conditional deduction, zero newly confirmed printed errors, zero complete transitive proof-chain certificates. Historic first visits are unreconciled. The 25-chapter/747-section inventory is unchanged.

**Excluded and not certified:** Demailly approximation/regularization and the dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas, positivity-loss proof-completion programmes remain **deferred-by-user**. No tests, build, CI, website publication, formal-verification claims, or main/source/registry/tag edits.
