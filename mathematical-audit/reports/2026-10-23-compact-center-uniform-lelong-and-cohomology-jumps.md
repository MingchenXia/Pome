# Mathematical audit: compact-center Lelong propagation, flat twists, and geometric cycle inputs

**Date:** 2026-10-23, Asia/Shanghai. **Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Audit branch at initial reading:** \`c83a006d9e4e7f9e94e69b7be7f0e6db4051e45e\`. Current table of contents: 25 chapters / 747 numbered sections, *inventory only*.

**Required freshly read files:** \`main/AGENTS.md\` blob \`eda69505b93b4782290d9cfac07c8651dedd17c5\`; \`main/documentation/proof-expansions.md\` blob \`8b37e218c74d5a93637e0f092cf5f29cc338a94d\`; \`main/docs/chapters/index.html\` blob \`c0c07abf4d8f7575b54cff2ec694fcf987f51cf8\`; audit \`README.md\` blob \`7967ffabeccea69fd80a5ec5d364e0a8e6bca137\` and \`mathematical-audit/LATEST.md\` blob \`efc9ac79873f738cf8b6985bca7d7dd04aad0bc4\`.

**Actual first selected proof review:** §§6.56, 9.74, 9.77, 10.103, 10.104. Only specific preceding lemmas in §§9.72 and 9.76 consulted for dependencies. **No whole section or project certified.** Completely excluded by the author's 17 October scope change: Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale and positivity-loss proof-completion. Neighboring §6.55 and analytic L²/direct-image steps in §10.108 were deliberately *not* reviewed. Historical records retain \`deferred-by-user\`, not verified or resolved.

## Source anchors

- \`docs/sections/singularities-along-a-compact-center/index.html\`, blob \`e2174cb28e3fdf0ce5c7b63ec4bdd6f774b55516\`: Proposition 6.56.1 (source \`cao-paun-foliations:6F802F01\`, permanent tag \`4E92E37E64AC\`, lines 11–16); proof lines 19–74; Equation 6.56.2 (source \`cao-paun-foliations:05182F8F\`, tag \`3683A52A8C25\`, lines 68–70). Examined the compact normal-bundle model (24–30), fiber volume normalization (32), positive global residual construction/cohomological class (34–63), and Lelong/mass comparison (66–73).
- \`docs/sections/from-local-leaves-to-a-meromorphic-fibration/index.html\`, blob \`285a6dbc3d2aeddc105f931a2377cc90d2d101de\`, section source \`cao-paun-foliations:A7CD555C\`, permanent tag \`6374AD3A13A2\`, lines 7–27. Examined Frobenius normal quotient (12–18), closure-dimension implication (21), and cited Barlet/Ou cycle argument (24–27).
- \`docs/sections/deformation-of-the-canonical-pseudo-effective-cone/index.html\`, blob \`3acd67247638c32f4b4f98f4f5311f0ff554eda1\`, Corollary 9.77.1, source \`cao-paun-foliations:73704007\`, tag \`11B2C808741A\`, statement/proof lines 11–20, external Fujiki theorem lines 7–9.
- \`docs/sections/euler-characteristics-under-flat-twists/index.html\`, blob \`99c65b6051fef34b6ec0b8822c973ab5470bb30a\`, Lemma 10.103.1, source \`cao-paun-foliations:885C5EE8\`, tag \`E897B72A71BA\`, lines 8–18.
- \`docs/sections/determinants-of-singular-bundle-metrics/index.html\`, blob \`901d6104f4a5ba01b188270bd6e2377ee4baeb9d\`, Lemma 10.104.1, source \`cao-paun-foliations:2FBA7F63\`, tag \`EC118288B440\`, lines 8–20.
- Dependency-only: §9.72 Lemma 9.72.1 (tag \`0A2146B324EB\`, lines 8–18, blob \`3191443b49a20377356f519b5e98ec29259f1c7c\`) and §9.76 Corollary 9.76.2 (tag \`8876081BAAEC\`, lines 31–58, blob \`88c8dc4651dc7d9cd21609d3d453521f97e0190d\`).

## POME-CAOPAUN-CENTER-UNIFORM-LELONG-001

**Classification:** \`verified conditional deduction\`, severity **low**; a stronger consequence of a correct proposition, **not** a theorem counterexample or a complete certification of restricted-current existence.

**Hypotheses:** *All* hypotheses of Proposition 6.56.1, particularly compact connected Kähler \(X\), compact connected smooth center \(C\), \(C_0=C\setminus A\) with \(\operatorname{codim}_C A\ge2\), smooth locally closed \(S\supset C_0\), and a globally \(\omega\)-psh potential whose restriction to \(S\) has **defined analytic singularities** (or the stated defined residual condition). Put \(a=\nu(\varphi|_S,C_0)\ge0\). For fixed geometry, the proposition's estimate may be made *uniform over all* \(y\in C_0\):
\[
\boxed{\sup_{y\in C_0}\nu(\varphi|_S,y)\le A_1a+A_2,}
\]
with \(A_1,A_2\ge0\) independent of both \(y\) and \(\varphi\).

**Exact normalization and proof.** Suppose \(d=\dim C\ge1\) and \(q=\dim S-\dim C\ge1\); set \(\ell=q-1\). Retain the proof's fixed compact smooth model \(p_E:E\to C\) of the exceptional projective bundle, \(j:E\to\widehat X\), the closed Kähler form \(\widehat\omega\) normalized on fibers of \(E_0\to C_0\), and the smooth Chern form \(\theta_D\). Define the fixed closed real \((1,1)\)-current
\[
\Xi=(p_E)_*\big(j^*\theta_D\wedge(j^*\widehat\omega)^\ell\big).
\]
The proper pushforward \(D_0=(p_E)_*(j^*\widehat\omega)^\ell\) is a **closed \((0,0)\)-current** on connected \(C\), hence a constant distribution. Its restriction to the dense open \(C_0\) is the smooth normalized fiber integral \(1\) (printed line 32), so \(D_0=1\) *on all* \(C\), with no assumption of countable cofinality or illicit limit exchange. As \(\pi\circ j=i_C\circ p_E\), projection formula yields
\[
\boxed{Q_a=(p_E)_*\big(j^*(\pi^*\omega-a\theta_D)
       \wedge(j^*\widehat\omega)^\ell\big)
       =\omega_C-a\Xi.}
\]
The published construction supplies one positive closed \(P=Q_a+dd^c\Phi\) on compact \(C\); it is formed from the **global restriction and generic Lelong coefficient \(a\)**, without choosing \(y\). Thus
\[
[P]=[\omega_C]-a[\Xi],\qquad
M(P):=\int_C P\wedge\omega_C^{d-1}=V-aH
\]
where \(V=\int_C\omega_C^d>0\) and \(H=\int_C\Xi\wedge\omega_C^{d-1}\in\mathbb R\) depend only on fixed geometry. By finitely many uniform coordinate-ball applications of monotonicity for closed positive \((1,1)\)-currents on compact Kähler \(C\), a constant \(B_C>0\) satisfies
\[
\sup_{y\in C}\nu(P,y)\le B_C\,M(P).
\]
For **every** \(y\in C_0\) Equation 6.56.2 gives
\(\nu(\varphi|_S,y)\le a+\nu(P,y)\).
Consequently
\[
\boxed{\sup_{C_0}\nu(\varphi|_S,\cdot)
 \le a+B_C(V-aH)
 \le (1+B_C|H|)\,a+B_CV.}
\]
This is a complete derivation *conditional on the prior residual-restriction construction*. If \(\dim C=0\), \(a=\nu(\varphi|_S,y)\). If \(\dim C=\dim S\), the restriction is a globally defined \(\omega_C\)-psh potential and \(a=0\), so direct compact-center Lelong mass bounds apply. Thus the stated uniform assertion covers those edge cases.

**Correction:** optional corollary immediately following Proposition 6.56.1; preserve its exact analytic-singularity/residual hypotheses, original source/permanent tags, and historical attribution. **Dependents:** strengthens selection of generic points in Theorem 9.73.1. Its previous pointwise version is correct, not redundant with this uniform statement.

## POME-CAOPAUN-PIC0-HODGE-JUMPS-001

**Classification:** \`verified conditional deduction\`, **low**; *not* a false Euler-characteristic theorem. **Input:** Lemma 10.103.1 plus standard smoothly parameterized elliptic Hodge Laplacians and spectral-projection perturbation.

For any holomorphic vector bundle \(F\) on smooth projective \(Z\), \(\rho\mapsto h^q(Z,F\otimes\rho)\) is **upper semicontinuous** on \(\operatorname{Pic}^0(Z)\); in particular, for every directed net \(\rho_\alpha\to\rho\),
\[
\limsup_\alpha h^q(Z,F\otimes\rho_\alpha)\le h^q(Z,F\otimes\rho).
\]
Locally trivialize the smooth topologically trivial twist and vary its \(\bar\partial_\rho\)-operator smoothly. Each nonnegative selfadjoint Dolbeault Laplacian \(\Box_{q,\rho}\) has discrete spectrum and compact resolvent. Fix \(0<\delta\) below the first positive eigenvalue at \(\rho_0\). Nearby spectral projection rank for eigenvalues \(<\delta\) is constant and equals \(h^q(Z,F\otimes\rho_0)\); each nearby kernel is contained in that spectral subspace. This proves upper semicontinuity without sequential assumptions. The alternating sum \(\chi(F\otimes\rho)\) stays constant by the original index proof, but individual dimensions can jump.

**Sharp example:** on an elliptic curve \(Z\), \(F=\mathcal O_Z\), a nontrivial \(\rho\in\operatorname{Pic}^0 Z\) has no nonzero section (degree zero would force a nowhere-vanishing trivialization), hence \(h^0(\rho)=0\). Since printed Lemma 10.103.1 gives \(\chi(\rho)=0\), also \(h^1(\rho)=0\). At the trivial twist \(h^0=h^1=1\). Thus termwise cohomology constancy is **false**, whereas the printed Euler characteristic lemma is correct. **Patch:** optional caveat and example after Lemma 10.103.1; do not rewrite its actual statement.

## POME-CAOPAUN-FOLIATION-CYCLE-INPUT-001

**Classification:** \`external dependency\`, **medium** for self-containment, **not** a false theorem. §9.74 explicitly cites **Ou2025 Lemma 7.5**. The Frobenius relation tangent pairs \((v,w)\) satisfy \(w-v\in\mathcal F\), so quotient by the diagonal tangent indeed gives normal bundle \(\mathcal F\) (lines 12–18). Contraposition of §9.73.1 gives the dimension equality *conditionally on that separate theorem*. But the ensuing global quotient requires: generic analytic family of compact cycles for the proper relation projection; proper pushforward of cycles to compact Kähler \(X\); compactness of the relevant Barlet component; and bimeromorphic evaluation of the reduced universal incidence family. These are admitted external analytic cycle-space inputs, not proved by dimension equality alone. **Patch:** isolate a precise internal cycle-space/analytic-graph quotient statement and openly retain the Barlet/Bishop/Ou inputs and attribution. **Dependent:** §9.75 foliation-integrability applications.

## POME-CAOPAUN-FUJIKI-DEFORMATION-INPUT-001

**Classification:** \`external dependency\`, **medium** for self-containment, **not** a false theorem. §9.77 lines 7–9 explicitly cite **Fujiki1981 Proposition 2.3** for deformation invariance of uniruledness in the stated proper smooth Kähler family. Corollary 9.77.1 then correctly uses the *two-way* equivalence of uniruledness with canonical non-pseudo-effectivity in §9.76.2; its contrapositive deduction checks out. Relative cycle-space compactness/deformation is a real additional input and **does not follow from openness of free rational curves alone**. **Patch:** retain the historical citation and register a separate precise prerequisite. **Dependent:** special-fiber to all-fiber canonical pseudo-effectivity.

## Additional checks and limits

The §10.104 proof's determinant sign is consistent: \(dd^c\log\det H^*\) is the curvature of \(\det G\), not of its dual; radial averages of a Griffiths-dual log-psh matrix decrease in Loewner order and the finite-positive-a.e. assumption prevents an identically \(-\infty\) determinant limit. The coefficient \(\operatorname{rk}G\) in the lower-bound curvature is correct. This is **a selected argument check**, not a full independent metric or analytic direct-image theorem certification.

No new numerical check was run just to replay old arithmetic. No full project tests, build, CI, formalization, website publication, source manuscript/registry/permanent-tag/main modification, merge, or new PR. Every deferred-by-user finding remains deferred, not silently resolved. The local cumulative coverage matrix and resolved/unresolved/deferred ledger are separately retained; a report-only remote commit does *not* mean those large indexes are already synchronized.
