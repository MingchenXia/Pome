# Strong Sobolev convergence of bounded decreasing admissible potentials

**Finding:** \`POME-HESS-CAP-STRONG-H1-MONOTONE-001\`  
**Date:** 2026-11-08  
**Severity / classification:** low / **verified conditional deduction**. No printed theorem is refuted; this is an additional conclusion from the explicitly identified internal lemmas, not an independently certified PDE or approximation theorem.

## Exact reading-edition provenance

- Production \`main\` commit: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
- Integrated file: \`docs/sections/complex-hessian-equations--sobolev-capacity-and-two-hessian-factors/index.html\`, blob \`25f25433cb9b17de6715a5b05f8b3c15b95a18cd\`.
- Section context: chapter 8 assumes \`2 <= m < n\`; the relevant Sobolev Gauduchon trace is introduced at physical lines 7–28. Its multiplier \`T=rho omega^{n-1}\` satisfies \`dd^c T=0\` (lines 10–19).
- Lemma 8.10.2: source \`non-kahler-pluripotential-theory:1DDAECA7\`, permanent tag \`FFBF9CD42640\`, statement lines 59–67, proof lines 72–95. It asserts \`H^1\` bounds, positive measures and **weak**, rather than strong, \`H^1\` convergence of smooth decreasing admissible approximants (line 79).
- Lemma 8.10.3: source \`non-kahler-pluripotential-theory:8E387C3E\`, permanent tag \`A82044827575\`, lines 101–125; identifies canonical representatives and quasicontinuity.
- Proposition 8.10.4: source \`non-kahler-pluripotential-theory:C0AF8E7E\`, permanent tag \`B40742E0DD08\`, statement lines 131–135, proof lines 140–149. It gives weighted convergence \`v_j mu_{u_j} -> v mu_u\` for two bounded decreasing canonical sequences.
- Theorem 8.10.5, source \`non-kahler-pluripotential-theory:A19E0DE8\`, permanent tag \`0241EC758621\`, lines 155–177, is a possible dependent application, **not** independently certified in this run.

## Additional statement

Let \`X\` be compact, \`omega\` a Hermitian form, and \`T=rho omega^{n-1}\` the smooth strictly positive \`(n-1,n-1)\` form with \`dd^c T=0\` from §8.10. Put

\[
\mu_a=(\omega+\mathrm{dd}^{\mathrm c}a)\wedge T,\qquad
\mathcal E_T(a)=\int_X \mathrm da\wedge\mathrm d^{\mathrm c}a\wedge T.
\]

**Conditional strengthening of Lemma 8.10.2 and Proposition 8.10.4.** Assume their results, including weighted convergence, and the existence of the smooth monotone admissible approximants already invoked in their printed proofs. For bounded canonical admissible \`a,b\`, there is the exact integration-by-parts identity

\[
\boxed{\quad
\mathcal E_T(a-b)
   =\int_X(a-b)\,\mathrm d(\mu_b-\mu_a).\quad} \tag{1}
\]

Consequently, if \`u_j\downarrow u\` is **any uniformly bounded decreasing sequence of canonical admissible potentials**, then

\[
\boxed{\quad
\|u_j-u\|_{H^1}\longrightarrow0,\qquad
0\leq\mathcal E_T(u_j-u)
   \leq \int_X (u_j-u)\,\mathrm d\mu_u
   \longrightarrow0.\quad} \tag{2}
\]

Here the \`H^1\` norm is precisely that of §8.10, line 19. No assumption \`dT=0\` is used. There is **no claim** of strong convergence of complex Hessian measures or of any higher Hessian product.

## Full proof

**Step 1: smooth decreasing approximants converge strongly.** Let \`s_j\downarrow s\` be smooth admissible functions with a common uniform bound. Write \`mu_j=mu_{s_j}\`, \`mu=mu_s\`. For \`k>j\`, the difference \`w_{jk}=s_j-s_k\` is smooth and nonnegative. Since \`dd^c T=0\`, integration of \`dd^c(w_{jk}^2)\wedge T\` on the compact manifold gives

\[
\mathcal E_T(w_{jk})
 =-\int_Xw_{jk}\,\mathrm{dd}^{\mathrm c}w_{jk}\wedge T
 =\int_X(s_j-s_k)\,\mathrm d(\mu_k-\mu_j). \tag{3}
\]

The products and all four integrals here are classical. For fixed \`j\`, Lemma 8.10.2 gives weak \`H^1\` convergence \`s_k\rightharpoonup s\`, hence weak lower semicontinuity of the nonnegative gradient seminorm. Proposition 8.10.4, applied with **both** decreasing arguments equal to \`s_k\`, gives \`s_k\mu_k\rightharpoonup s\mu\`. In addition, \`mu_k\rightharpoonup mu\`; \`s_j\` is smooth and fixed; and \`s_k\to s\` boundedly pointwise, so dominated convergence applies to the smooth fixed measure \`mu_j\`. Taking \`k\to\infty\` in the right side of (3) therefore gives

\[
0\leq\mathcal E_T(s_j-s)
 \leq\int_X(s_j-s)\,\mathrm d\mu
    -\int_X(s_j-s)\,\mathrm d\mu_j
 \leq\int_X(s_j-s)\,\mathrm d\mu. \tag{4}
\]

The last step uses \`s_j\geq s\` and positivity of \`mu_j\`. The positive measure \`mu\` has finite mass \`A\` by Lemma 8.10.2. Since \`s_j-s\downarrow0\` pointwise and is uniformly bounded, dominated convergence gives the final right side of (4) tending to zero. Bounded convergence also gives \`s_j\to s\` in \`L^2(X,\omega^n)\`. Thus \`s_j\to s\` **strongly** in \`H^1\`.

**Step 2: extend the integration-by-parts identity.** Given bounded canonical admissible \`a,b\`, take bounded smooth decreasing admissible approximants \`a_\ell\downarrow a\` and \`b_\ell\downarrow b\` as already used in the integrated §8.10 proof. Step 1 proves \`a_\ell\to a\`, \`b_\ell\to b\` strongly in \`H^1\`. In the smooth identity

\[
\mathcal E_T(a_\ell-b_\ell)
  =\int_X(a_\ell-b_\ell)\,\mathrm d(\mu_{b_\ell}-\mu_{a_\ell}),
\]

the left side tends to \`E_T(a-b)\` by strong convergence. Expand the right side into four integrals. Each converges by Proposition 8.10.4, applied in the two possible orders and with equal arguments (e.g. \`a_\ell\mu_{b_\ell}\rightharpoonup a\mu_b\`). Thus its limit is the right side of (1), with the canonical Borel values specified by Lemma 8.10.3. This proves (1) with no unproved integration-by-parts extension across singular coefficients.

**Step 3: arbitrary bounded monotone sequences.** Apply (1) to \`a=u_j\`, \`b=u\` and use positivity of \`mu_{u_j}\` and the pointwise inequality \`u_j-u\geq0\`. This gives the middle inequality of (2). Since \`mu_u\` is finite and \`u_j-u\downarrow0\` pointwise with a uniform bound, the right side tends to zero by dominated convergence. Also \`u_j\to u\` strongly in \`L^2(X,\omega^n)\` by the same argument. The Sobolev norm in §8.10 is the sum of these two nonnegative terms, proving (2).

## Classification and dependency boundary

- **Classification:** verified conditional deduction, low severity. The printed weak-\`H^1\` assertion remains correct; (2) strengthens it.
- **Internal inputs not fully certified here:** the admissible smooth decreasing approximation invoked in §§8.9–8.10 and specifically §8.6.6; Lemmas 8.10.2–3; Proposition 8.10.4; the Gauduchon multiplier existence Theorem 11.4.2. Their printed statements/steps were read where specified above, but their entire analytic dependency graphs are **not** certified.
- **Excluded subject:** no attempt to prove, extend, or reopen Demailly approximation/regularization, Bergman, weighted-L², Ohsawa–Takegoshi, multiscale atlas or positivity-loss work; all such earlier notes remain **deferred-by-user**. The use of the specific pre-existing \`m\`-Hessian admissible approximation statement is a declared conditional dependency only.
- **Proposed optional addition:** insert (1)–(2) after Proposition 8.10.4 or add a remark to Lemma 8.10.2, preserving every source/permanent tag and the printed (weaker) version.
- **Affected dependents:** Theorem 8.10.5 and the subsequent §8.11 weighted-product arguments can, if appropriate, cite the stronger \`H^1\` convergence; no claim that they need a repair, and their full proofs were not verified here.
- **Actual coverage:** a new proof-level deduction from §§8.10.2–4 and the smooth two-variable energy identity. §8.10 was previously partially visited; **0 new first-visited sections, 0 full-section certifications**. Main table of contents: **25 chapters / 747 numbered sections**. No project build, test suite, CI, formal proof or publication.
