# 2026-11-18 — sharp obstacle comparison for the Hermitian complex-Hessian penalty equation

**Finding ID:** POME-HESS-PENALTY-OBSTACLE-CONTRACTION-001  
**Classification:** low / **verified conditional deduction**, **not a confirmed error**.  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Scope:** Chapter 8, §8.6, with the §8.1 standing parameters \((X,\omega,m)\): connected compact complex \(n\)-fold, \(\omega\) a positive Hermitian form, \(2\le m<n\). This audit does **not** touch Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-gluing, or positivity-loss proof completion.

## Exact integrated anchors and dependencies

- `docs/sections/complex-hessian-equations/index.html`, §8.1 opening, source section/permanent tag `CFD38285654D`: connected compact Hermitian standing hypotheses and intermediate Hessian degree.
- `docs/sections/complex-hessian-equations--the-admissible-cone/index.html`, §8.2 opening, permanent section tag `F677D35E0BD7`: upward monotonicity of \(\Gamma_m\) under addition of semipositive Hermitian matrices and the normalized Hessian convention.
- `docs/sections/complex-hessian-equations--proper-equations-and-admissible-approximation/index.html`, **blob `841dd207876499be9d83045facf862a323e60994`**:
  - Lemma **8.6.1**, source `non-kahler-pluripotential-theory:91CAEA62`, permanent tag `8B310CC2C1A1`, physical lines **11–36**: unique smooth strictly \(\Gamma_m\)-admissible solution for \(H_m(w)=e^{aw+H}\omega^n\), maximum principle and invertible linearization.
  - Lemma **8.6.2**, source suffix `761F7FD5`, permanent tag `B8367971A40D`, lines **45–94**: an arbitrary smooth obstacle in the penalization construction, without assuming the obstacle is admissible.
  - Lemma **8.6.5**, source suffix `32B364F9`, permanent tag `DFE78235C5E9`, lines **129–169**: the same penalty problem, with its \(O((\log N)/N)\) approximation estimate for a bounded admissible function under an arbitrary smooth majorant.
  - Theorem **8.6.6**, permanent tag `68BE4F589DCE`, lines **174–201**, *context only*: decreasing admissible approximation.
- `docs/sections/complex-hessian-equations--continuous-products-envelopes-and-domination/index.html`, Proposition **8.7.1**, permanent tag `D2A0F255F625`, *dependent context only* (continuous mixed products).

We inspected the *integrated reading-edition text* at the indicated physical lines. Earlier audit notes sampled 8.6.1–2 and 8.6.6, but did **not** provide the following two-obstacle comparison with an arbitrary varying exponential prefactor. This is a new independent maximum-principle check, not a new certification of the deep smooth-PDE existence theorem.

## The exact comparison theorem

Fix a number \(N>0\). For any smooth real function \(h\) and any scalar \(b>0\), write \(W_{N,b}(h)\) for the unique smooth strictly admissible solution supplied by Lemma 8.6.1:
\[
 H_m(W_{N,b}(h))=b\exp(N(W_{N,b}(h)-h))\,\omega^n,\qquad
 H_m(v)=(\omega+dd^cv)^m\wedge\omega^{n-m}.
\]
Indeed this is the lemma with \(a=N\) and \(H=\log b-Nh\); **no admissibility is assumed of \(h\)**.

**Theorem (exact nonexpansive comparison).** For smooth \(h_1,h_2\) and \(b_1,b_2>0\), set \(w_i=W_{N,b_i}(h_i)\) and
\[
 d=h_1-h_2-\frac{1}{N}\log\frac{b_1}{b_2}.
\]
Then pointwise everywhere on \(X\)
\[
 \boxed{\min_X d\le w_1-w_2\le\max_X d.}\tag{A}
\]
Consequently \(W_{N,b}\) is order preserving, commutes exactly with addition of constants, and is **1-Lipschitz in the uniform norm**:
\[
 h_1\le h_2\Rightarrow W_{N,b}(h_1)\le W_{N,b}(h_2),\qquad
 W_{N,b}(h+c)=W_{N,b}(h)+c,
\]
\[
 \boxed{\|W_{N,b}(h_1)-W_{N,b}(h_2)\|_\infty
        \le\|h_1-h_2\|_\infty.}\tag{B}
\]
There is also the **exact prefactor covariance**
\[
 \boxed{W_{N,b_1}(h)=W_{N,b_2}(h)
              -\frac1N\log(b_1/b_2).}\tag{C}
\]
For fixed \(b_1=b_2\), (A) is stronger than (B): every pointwise difference of the solutions lies in the range of the obstacle difference, hence
\(\operatorname{osc}_X(w_1-w_2)\le\operatorname{osc}_X(h_1-h_2)\).

**Proof.** Let \(x_{\max}\) maximize \(w_1-w_2\). The real \((1,1)\)-forms satisfy
\[
 \omega+dd^cw_1\le\omega+dd^cw_2 \quad\text{at }x_{\max},
\]
because the complex Hessian of the difference is negative semidefinite there. Both forms are strictly \(\Gamma_m\)-admissible. The upward monotonicity of \(\sigma_m\) in the Gårding cone gives
\[
 b_1e^{N(w_1-h_1)}(x_{\max})
 =\frac{H_m(w_1)}{\omega^n}(x_{\max})
 \le \frac{H_m(w_2)}{\omega^n}(x_{\max})
 =b_2e^{N(w_2-h_2)}(x_{\max}).
\]
Taking logarithms yields \(w_1-w_2\le d(x_{\max})\le\max_Xd\). At a minimum of \(w_1-w_2\), reverse the semipositive order to obtain \(w_1-w_2\ge\min_Xd\). This proves (A). Equations (B) and the order assertion follow immediately. The constant-shift and prefactor transformations follow by substitution into the PDE and uniqueness. Nothing here requires \(\omega\) to be closed, a continuous Hessian-product construction, or an interchange of limits.

**Sharpness.** For constant obstacles \(h\equiv c\), the exact solution is
\[
 W_{N,b}(c)=c-\frac{\log b}{N},
\]
since \(H_m(\mathrm{constant})=\omega^n\). Therefore the coefficient 1 in (B), the coefficient \(1/N\) in (A) and (C), and both constant-shift equalities are sharp. This is valid in every admissible dimension and degree, including the stated range \(2\le m<n\).

## Strict-obstacle refinement and linearization

If the smooth obstacle itself is *strictly* admissible, define
\[
 a_h=\min_X H_m(h)/\omega^n>0,\qquad
 A_h=\max_X H_m(h)/\omega^n<\infty.
\]
For any \(b>0\) the exact comparison at a maximum and minimum of \(w-h\) gives the independent improvement
\[
 \boxed{\frac1N\log(a_h/b)\le W_{N,b}(h)-h
                         \le\frac1N\log(A_h/b).}\tag{D}
\]
At a maximum of \(w-h\), \(H_m(w)\le H_m(h)\le A_h\omega^n\); at a minimum the reverse inequality and \(a_h>0\) hold. Taking logarithms proves (D). The constant obstacle achieves equality in both bounds. **This \(O(N^{-1})\) conclusion requires strict admissibility of \(h\)**; it does not replace the more general \(O((\log N)/N)\) estimate of Lemma 8.6.5 for arbitrary smooth majorants.

For a smooth one-parameter family \(h_t\) and fixed \(N,b\), the implicit-function theorem using the invertible linearization stated at lines 30–36 of Lemma 8.6.1 gives differentiable \(w_t=W_{N,b}(h_t)\). With \(L_w\) as printed there,
\[
 (N-L_{w_t})\dot w_t=N\dot h_t,\qquad
 \min_X\dot h_t\le\dot w_t\le\max_X\dot h_t.\tag{E}
\]
The inequalities follow from the elliptic maximum principle, not from differentiation of any nonsmooth envelope. Formula (E) checks the infinitesimal consistency of the sharp finite-difference comparison (A). This part is **conditional on the smooth PDE solvability and IFT invoked by the printed Lemma 8.6.1**; we did not recertify the global Evans–Krylov/Schauder estimates.

## Classification, correction, dependent use, and exact scope

- **Severity/status:** **low / verified conditional deduction**; **no printed false theorem established**. The new order and supnorm bounds are fully proved *assuming the already stated smooth strictly admissible existence/uniqueness and the elementary Gårding monotonicity*.
- **Optional proposed insertion:** after Lemma 8.6.5, add the two-obstacle bound (A), exact covariance (C), and the separate strict-reference refinement (D). **Do not** replace Lemma 8.6.5 by the \(O(1/N)\) claim without the strict-admissibility hypothesis. No change to original source, main, reading edition, registry, or permanent tags is made.
- **Affected logical dependents:** Lemmas 8.6.2 and 8.6.5 (stability under changing majorants or prefactors); Theorem 8.6.6 (comparison of finite smooth stages, **not** a shortcut to its decreasing selection proof); Proposition 8.7.1 (uniformly approximated mixed Hessian products, conditional). The user-excluded Demailly programme is *not* among the dependencies checked.
- **Coverage exactly performed:** new proof-level comparison for Lemma 8.6.1's two-input family and Lemma 8.6.5's penalty; statement/proof lines 11–36, 45–94, 129–169 inspected; contextual §§8.1, 8.2, 8.7.1 and Theorem 8.6.6. **Previously partially reviewed section §8.6: +0 first-visited numbered sections, +0 entirely certified sections.** The current main ToC remains 25 chapters / 747 sections.
- **Unresolved/not certified:** general continuity-method PDE a priori estimates (8.3–8.5); the whole-section collection and all transitive dependencies; any assertion for non-smooth obstacles *as input to the smooth penalty problem*, or uniformly in \(N\) with moving obstacle without the hypotheses used above. No project build, tests, CI, or site publication was performed.
- All Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss work remains **deferred-by-user**, not resolved.
