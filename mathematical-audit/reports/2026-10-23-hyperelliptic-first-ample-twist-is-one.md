# Mathematical audit: the first fixed-ample twist in the hyperelliptic test is exactly one

**Checkpoint:** 2026-10-23, Asia/Shanghai. **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Review branch at start:** 7f664ec1776df5c0ebb80d9a13b21b80f5b5cf53. Audit-only note, not a patch to the mathematical source. The user-excluded Demailly regularization/Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss programme was not examined.

## Exact integrated reading and provenance

- Section 11.29: docs/sections/gauduchon-metrics-and-linear-mass--projective-first-jets-and-positive-bundle-metrics/index.html, blob 1705a4387f533f89e80775bf5de4087c04d2e91b. Lemma 11.29.1, source non-kahler-pluripotential-theory:B9ADAD84, permanent tag E495F7FE3CE6, lines 23–35: strict psh fiber-quadratic functions and negative Griffiths curvature of the metric on the dual. The fixed finite-dimensional tests and arbitrary Hermitian coefficients are at lines 54–84; Proposition 11.29.4, permanent tag 07EC0797039C, lines 88–113, gives the precise convex-hull alternative. Lemma 11.29.7, lines 144–168: selected nesting and density proof checked, not its whole elliptic/approximation dependency chain. Theorem 11.29.9, source non-kahler-pluripotential-theory:A9DCA741, tag C334EF3CAF72, lines 176–218; Corollary 11.29.10, tag A86A6F25FF07, lines 222–233.
- Section 11.30: docs/sections/gauduchon-metrics-and-linear-mass--ramified-section-tests-and-a-positive-root-metric/index.html, blob 1e52ae44b41ea9547ce2bf3f7e51b836772baf26. Lemma 11.30.1, source non-kahler-pluripotential-theory:D05FB6F6, tag 8B6FA358A78D, lines 10–41: finite double cover, complete section splitting and positive root metric; Proposition 11.30.3, source non-kahler-pluripotential-theory:AFFAD954, tag A8FAF022D4CA, lines 47–93: root-weight first success j=q−1 and lower-level ramification obstruction; Corollary 11.30.5, source non-kahler-pluripotential-theory:7459D02A, tag 9F9E99FDE392, lines 98–110: untwisted fixed-A failure and the distinction between j and m. The source's equality j=qm for fixed-A level m was checked.
- Section 11.28, docs/sections/gauduchon-metrics-and-linear-mass--holomorphic-sectional-curvature/index.html (blob 06c98914b1a3e3d43b546a52213b043ec03b4d24), was context only. An earlier audit already recorded a separate torus/curvature identity; this is not a new check of that result.

## POME-HYPERELLIPTIC-FIXED-TWIST-ONE-001

**Status:** verified conditional deduction; **severity:** low (strengthening of a specific example, NOT an error, an unconditional theorem about other bundles, or a claimed bound in the general criterion). **Prerequisites:** the explicit section decomposition in Lemma 11.30.1 and elementary Levi/Griffiths equivalence of Lemma 11.29.1. No regularization input.

**Claim.** In the exact setup of §11.30, for every n>=2, q>=2 and every choice of basis of H^0(X,A) used to define its Fubini–Study weight, where

\[
X=C\times\mathbf P^{n-1},\quad
C=\{w^2=\beta\}\subset{\rm Tot}(\mathcal O_{\mathbf P^1}(q)),
\quad L=\pi^*\mathcal O_{\mathbf P^1}(1)\boxtimes\mathcal O_{\mathbf P^{n-1}}(1),
\quad A=L^q,
\]

the **first successful fixed-ample test in Theorem 11.29.9 is m=1** (with m0=0). That is, the level m=0 has no Hermitian coefficient matrix giving a strictly psh G_{0,B}, whereas some positive-semidefinite coefficient matrix at m=1 gives a strictly psh G_{1,B} on the complement of the zero section of F=L^{-1}. This remains true as q grows; it does **not** contradict Proposition 11.30.3's distinct first root-weight level j=q−1.

**Proof.** Denote the complete section bases by (sigma_i) for H^0(X,A) and (tau_a) for H^0(X,L); let phi_A=log(sum_i |sigma_i|^2) in a local frame of A. The untwisted complete evaluation map uses only sections pulled back from P^1 on the curve factor, because q>=2. It has zero horizontal differential at every ramification point of pi. Hence the m=0 test fails, exactly as explained in Corollary 11.30.5.

We now explicitly build a level-one test, keeping the originally fixed, possibly non-product, basis (sigma_i). Every product sigma_i*tau_a is a section of L^{q+1}=E tensor A. The finite nonnegative quadratic expression

\[
G_0(v)=e^{-\phi_A}\sum_{i,a}|v(\sigma_i\tau_a)|^2
      =\sum_a|v(\tau_a)|^2
\tag{1}
\]

belongs to the allowed space of level-one tests, because the products can be expressed in any complete basis of H^0(X,L^{q+1}) and their squared norms form a positive-semidefinite Hermitian coefficient matrix. Equality (1) uses only sum_i |sigma_i|^2=e^{phi_A}, so it works for **every** fixed basis of H^0(X,A).

As q>=2, the global branch-coordinate section w of pi^*O(q) multiplies sections r_b of O_{P^1}(1) to give sections w*r_b of pi^*O(q+1). Tensor them with a complete basis (s_c) of H^0(P^{n-1},O(q+1)). The resulting sections eta_{bc}=w*r_b tensor s_c belong to H^0(X,L^{q+1}). Add the nonnegative level-one test

\[
G_\varepsilon(v)=G_0(v)+\varepsilon e^{-\phi_A}
                       \sum_{b,c}|v(\eta_{bc})|^2,\qquad\varepsilon>0.
\tag{2}
\]

A sum of squared evaluations is again represented by one Hermitian coefficient matrix B_epsilon; no requirement that the displayed section families be linearly independent is needed.

Write G_epsilon(v)=H_epsilon(x)|v|^2 in local frames of F. Since L's complete sections are pulled back from the Segre embedding of P^1 times P^{n-1}, the base curvature of log H_0 is the sum of the pullback Fubini–Study forms on the two factors. It is semipositive everywhere, positive definite off the ramification locus R times P^{n-1}, and its null space over that locus is exactly the one-dimensional tangent direction along the ramified curve C.

Put f=(H_epsilon-H_0)/(epsilon H_0). It is a smooth nonnegative global scalar function, independent of epsilon. Along the branch locus w=0, both f and df vanish. In the local branch coordinate t=w on C (Lemma 11.30.1 ensures dt!=0), one has z=z_0+O(t^2) on P^1. In local product coordinates (t,zeta) around (R,P^{n-1}),

\[
f(t,\zeta)=c(\zeta)|t|^2+O(|t|^3),
\quad
c(\zeta)=\frac{e^{-\phi_A(0,\zeta)}
               \bigl(\sum_b|r_b(z_0)|^2\bigr)
               \bigl(\sum_c|s_c(\zeta)|^2\bigr)}
              {H_0(0,\zeta)}>0
\tag{3}
\]

with the local positive frame factors understood consistently. Basepoint-freeness of the two section systems gives positivity. Thus (i partial bar partial f) is strictly positive on the null line of i partial bar partial log H_0 at every branch point, while all mixed t/zeta coefficients of that first-order perturbation vanish there.

The curvature of log H_epsilon is

\[
i\partial\bar\partial\log H_\varepsilon
=i\partial\bar\partial\log H_0
 +i\partial\bar\partial\log(1+\varepsilon f)
=\omega_0+\varepsilon\,i\partial\bar\partial f+O(\varepsilon^2)
\tag{4}
\]

uniformly in the C^0 norm on compact X. The positive coefficient in (3), the compact branch locus, and continuity give a fixed neighborhood U of the branch locus where the t/t Hermitian coefficient of i partial bar partial f is uniformly positive, while the transverse (P^{n-1}) block of omega_0 has a uniform positive lower bound. In product coordinates omega_0 has no t/zeta mixed block; by the Schur complement the t/t block after subtracting the small mixed correction remains >=epsilon*c_1 -C*epsilon^2>0 for sufficiently small epsilon. On X\U, omega_0 is uniformly strictly positive and the perturbation is O(epsilon), so the curvature remains positive there too. Therefore for all sufficiently small epsilon>0, the metric H_epsilon has strictly positive i partial bar partial log H_epsilon everywhere. For a line bundle F this is precisely strictly negative Griffiths curvature; Lemma 11.29.1 implies G_epsilon is strictly psh off its zero section.

Consequently m=1 succeeds and m=0 fails. This establishes the exact minimum m=1. The root-weight family used by Proposition 11.30.3 has levels j with weight e^{-j phi_A/q}; its j=q−1 success is **not** itself an admissible m=1 construction because the fixed family has j=qm. Equation (2) is an independent valid construction at j=q. QED.

**A convenient coordinate check, not a restriction on the theorem.** Choose tensor-product binomial/multinomial bases. In affine frames put Z=1+|z|^2 and Q=1+sum|zeta_i|^2. Then e^{phi_A}=(Z^q+|w|^2)Q^q. A positive diagonal coefficient matrix with the w*O(1) subspace weighted by lambda>1 yields, at m=1,

\[
G_{1,B_\lambda}(v)=|v|^2 ZQ\,
                \frac{Z^q+\lambda|w|^2}{Z^q+|w|^2}.
\tag{5}
\]

At any branch point t=w=0, the coefficient of i dt wedge dbar t in the log of the curve factor is precisely (lambda−1)/Z(z_0)^q >0, whereas the baseline pullback of FS has zero coefficient there. For lambda sufficiently close to 1, compactness and the same Schur-complement argument give global strict positivity. Formula (5) is an optional easily reproduced sanity check; the general proof (1)–(4) does not prescribe the original basis.

**Disposition:** Optional corollary/example after Corollary 11.30.5, preserving that theorem's root-level j=q−1 statement and Theorem 11.29.9's arbitrary-bundle qualitative equivalence. This is not a genuine duplicate: the existing text explicitly says that the root-weight count by itself does not determine the fixed-A count; the above proof computes the latter for this particular geometric example. No source/body, canonicalization, permanent tag, main or published page is modified.

**Verification boundary:** The finite-dimensional coefficient-matrix algebra, ramification order, positivity-on-null-space and compact Schur-complement steps have been checked directly. This does not verify the entire §11.29 C^2 density argument, every global Hermitian positivity theorem, or any other §11.30 example. No full project test, build, CI, publication or formal verification was run. The Demailly approximation/regularization and dedicated Bergman/L2/OT/multiscale/positivity-loss programme remains deferred-by-user, not reopened or certified.
