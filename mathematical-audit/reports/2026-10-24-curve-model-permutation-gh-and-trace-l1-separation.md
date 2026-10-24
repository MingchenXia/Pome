# Curve-model metric audit: permutation couplings and a trace–\(L^1\) separation

**Date:** 2026-10-24 (Asia/Shanghai). **Current reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
**Initial audit branch:** \`1a8b9876f7ad5d0a5f7df5afc106d535b50107ed\`.
**Scope:** newly selected integrated proof passages of §§18.17, 18.18, and 18.22; contextual dependency checks in §§18.16, 13.28–13.29, 5.43 and 15.19. No section, chapter, complete proof dependency chain, or user-deferred regularization result is certified.

## Sources pinned to current integrated reading edition

1. §18.17, “Varying the curve coefficients,”
   [actual HTML](../../docs/sections/multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--varying-the-curve-coefficients/index.html),
   Git blob \`d2dc367592df2da185f8d679aabf5df4e68a4a6a\`.
   Lemma 18.17.1, permanent tag **9040CE491D09**, original source **non-kahler-pluripotential-theory-8DC6813D**, physical lines 25–43;
   Proposition 18.17.3, tag **4A625E059F4C**, source **non-kahler-pluripotential-theory-B88D2016**, lines 57–85;
   equation 18.17.2, tag **AB4DC460D46E**, lines 47–52;
   Proposition 18.17.5, tag **25F2A9E20F21**, source **non-kahler-pluripotential-theory-C2C06FA3**, lines 100–129;
   equation 18.17.6, tag **E8AFCE9DFA82**, lines 100–106.
2. §18.18, “Arbitrary curve backgrounds,”
   [actual HTML](../../docs/sections/multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--arbitrary-curve-backgrounds/index.html),
   blob \`7e89dabe6cc08855d3a0f89a1f2faed9e5ae791d\`.
   Lemma 18.18.1, tag **7EF34A8A42E5**, source **non-kahler-pluripotential-theory-39C82453**, lines 25–70;
   Proposition 18.18.3, tag **347997EB7F21**, source **non-kahler-pluripotential-theory-7BBFA972**, lines 85–114;
   equation 18.18.4, tag **657599C0AEFD**, lines 87–92;
   Corollary 18.18.5, tag **15AC4263456B**, source **non-kahler-pluripotential-theory-7524C08C**, lines 118–130.
3. §18.22, “Models over a curve,”
   [actual HTML](../../docs/sections/multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--models-over-a-curve/index.html),
   blob \`5eda7a473def5f1a58bd23c4d2a1a88e4b52313c\`.
   Lemma 18.22.1, tag **717F85615B2A**, source **non-kahler-pluripotential-theory-1C54E58D**, lines 19–42;
   Lemma 18.22.2, tag **4A14B90776C1**, source **non-kahler-pluripotential-theory-36C4D938**, lines 61–81;
   Proposition 18.22.3, tag **AD848996B76C**, source **non-kahler-pluripotential-theory-FA6BA0A7**, lines 97–124;
   Corollary 18.22.4, tag **DFA6018C6C86**, lines 128–135.
4. Context checked, not recertified: §18.16 Lemma 18.16.1, tag **D9950FF0BE1C**, and Proposition 18.16.2, tag **9E5A9E7C5770**, blob \`93e080ea9c15c5ec03b28c2ec51eb469c769603b\`, lines 22–117; Lemma 13.28.1, tag **2422DD1AB3AB**; Proposition 13.29.1, tag **C9C98321BEFC**; Lemma 5.43.10, tag **633794C1EFC2**; Lemma 15.19.20, tag **022849340F28**. These have independent earlier histories. Referencing them here does not claim a fresh complete audit of their proofs.

## Finding POME-CURVE-GH-PERMUTATION-001

**Status:** verified conditional deduction. **Severity:** low. Neither a false theorem nor a correction to a printed proof. The published upper bound remains true.

**Hypotheses.** Let \(C_1,\ldots,C_m\), \(m\ge2\), be the compact connected Riemann surfaces of §18.17. Let \(\eta_i\) be smooth positive area forms, \(A_i=\int_{C_i}\eta_i>0\). Given coefficients \(a_i,b_i\ge0\), let \(\mathcal S_a,\mathcal S_b\) be the exact separated ordinary-model loci equipped with the polar total-variation sum metrics in equation 18.17.2. Let \(\Pi\) be any set of permutations \(\pi\in S_m\) for which each \(C_i\) is biholomorphic to \(C_{\pi(i)}\). The identity permutation always lies in \(\Pi\).

**Claim.** One may sharpen the original coordinatewise correspondence estimate to
\[
\boxed{\quad
 d_{\rm GH}(\mathcal S_a,\mathcal S_b)
 \le \min_{\pi\in\Pi}\sum_{i=1}^m
       |a_i A_i-b_{\pi(i)} A_{\pi(i)}| .
 \quad}
\tag{A}
\]
The same estimate holds for the ideal-model subspaces \(\mathcal I_a,\mathcal I_b\). In §18.18, with arbitrary smooth curve forms \(\sigma_i,\sigma'_i\) of nonnegative areas \(B_i,B'_i\), the analog is
\[
\boxed{\quad
 d_{\rm GH}(\mathcal S_\sigma,\mathcal S_{\sigma'})
 \le\min_{\pi\in\Pi}\sum_{i=1}^m|B_i-B'_{\pi(i)}|.
 \quad}
\tag{B}
\]
Again the ideal subspaces satisfy (B). The biholomorphisms need not preserve the chosen area forms; these metric spaces depend on the forms only through their total areas. No identification of the ambient potentials on \(M\) is asserted.

**Proof.** On \(C_i\), Proposition 13.29.1 identifies ordinary normalized curve models with positive polar measures \(\mu_i\) of mass at most \(A_i\), with distance \(\|\mu_i-\nu_i\|_{\rm TV}\); ideal models correspond exactly to atomic polar measures. For a zero coefficient the entire coordinate is omitted, which amounts to multiplying this distance by zero. Work instead with normalized measures \(m_i=\mu_i/A_i\), with mass at most one. A biholomorphism \(h_i:C_i\to C_{\pi(i)}\) sends polar sets to polar sets, defines a bijection of these normalized polar measures, preserves total variation, and sends atomic measures to atomic measures. Consequently the maps
\[
 (m_i)_i\longmapsto\bigl(h_{i*}m_i\bigr)_{\pi(i)}
\]
provide a bijection of auxiliary measure tuples, and hence a correspondence between the two model loci (they need not define a map on actual potentials in a common background).

For two tuples let \(d_i=\|m_i-n_i\|_{\rm TV}\in[0,2]\). Their distances in the paired spaces are respectively \(\sum_i a_i A_i d_i\) and \(\sum_i b_{\pi(i)}A_{\pi(i)}d_i\). Thus the correspondence has distortion at most
\[
 2\sum_i|a_iA_i-b_{\pi(i)}A_{\pi(i)}|.
\]
The correspondence inequality of §15.19.20 (tag 022849340F28) divides distortion by two, proving (A). Restriction to atomic measures proves the ideal assertion. For the arbitrary curve backgrounds, normalize each polar measure by its background area \(B_i>0\); zero-area coordinates are singleton factors and can be represented by zero measure. Proposition 13.29.1 identifies each such locus with the same unit-mass polar-measure space, multiplied by \(B_i\). The identical argument proves (B). All steps are finite products and correspondences; no sequential compactness or limiting interchange is invoked.

**Strict improvement / test example.** Suppose \(C_1=C_2=C\), \(\eta_1=\eta_2\), and \(A_1=A_2=A>0\). Put \(a=(t,0)\), \(b=(0,t)\) with \(t>0\) (additional zero coordinates permitted). The two metric spaces, and separately their ideal subspaces, are **isometric by swapping the active curve factor**, whence
\[
d_{\rm GH}(\mathcal S_a,\mathcal S_b)
=d_{\rm GH}(\mathcal I_a,\mathcal I_b)=0.
\]
The printed upper estimate \(\sum_i|a_i-b_i|A_i=2tA\) remains valid but is strict. Both spaces have diameter \(2tA\), and the original lower bound based on diameter difference is zero, consistent with exact isometry. This makes clear why coordinatewise coefficient distance is not an intrinsic metric of the abstract model spaces.

**Action / dependents.** Optional separate observation following Proposition 18.17.5 and the area comparison in Proposition 18.18.3; retain their statements, permanent tags, historical attributions, and sharp ordered-coefficient case. Affects only proposed quantitative parameter-space GH comparisons, not the established model-envelope or ideal-projection results. No changes to reader body, canonicalization or source repository are part of this audit.

## Finding POME-CURVE-TRACE-L1-NONCONVERSE-001

**Status:** verified conditional deduction. **Severity:** low. Not a counterexample to Proposition 18.22.3, which states the forward implication from polar metric convergence to \(L^1\) convergence, not its converse.

**Hypotheses.** Let \(p:X\to C\) be the surjective holomorphic map with connected (possibly critical) fibers of §18.22, with \(\dim_{\mathbf C} X=n\ge2\), \(X\) connected and compact, \(\beta\) any smooth real \((1,1)\)-form on \(C\) of positive total area \(A>0\), and \(\theta=p^*\beta\). Fix a Gauduchon form \(\gamma\) on \(X\). Choose pairwise distinct points \(s_j\to s\) on \(C\), with no \(s_j=s\).

**Claim.** Let \(v_j\) and \(v\) be the *normalized ordinary curve models* corresponding under Proposition 13.29.1 to polar curvature measures \(A\delta_{s_j}\) and \(A\delta_s\), respectively; set \(U_j=v_j\circ p\), \(U=v\circ p\). Then each \(U_j,U\) is a normalized ordinary model and
\[
\boxed{\quad U_j\longrightarrow U\text{ in }L^1(X,dV)
       \quad\text{for every smooth positive volume form }dV,\quad}
\tag{C}
\]
but for **every** \(j\)
\[
\boxed{\quad \rho_\theta(U_j,U)
       =\|A\delta_{s_j}-A\delta_s\|_{\rm TV}=2A.\quad}
\tag{D}
\]
Moreover the Gauduchon first-polar-trace measures converge weakly (as currents) while
\[
\|\lambda_{U_j}^{\gamma}-\lambda_U^\gamma\|_{\rm TV}
=2\kappa_\gamma A.
\tag{E}
\]
The multiplicities of critical fiber divisors are included in \(\lambda^\gamma\) and do not alter (C)–(E).

**Proof.** For the given area \(A\), write \(\beta=A\eta+\mathrm{dd}^{\rm c}h\) for a smooth area-one \(\eta>0\) and smooth \(h\). The mean-zero Green solutions \(q_j,q\) of
\[
 \mathrm{dd}^{\rm c}q_j=A(\delta_{s_j}-\eta),\qquad
 \mathrm{dd}^{\rm c}q=A(\delta_s-\eta)
\]
converge in \(L^1(C)\). Indeed the normalized logarithmic Green kernel is smooth in the pole parameter off its diagonal, and its local \(\log|z-s_j|^2\) singularity is uniformly integrable as \(s_j\to s\). Equivalently, the compactness–uniqueness argument in the proof of Lemma 18.22.2, lines 74–76, applies to \(\delta_{s_j}\rightharpoonup\delta_s\). Up to smooth gauge \(h\), these are potential representatives of curvature \(A\delta_{s_j}\) and \(A\delta_s\). Normalizing their supremum to zero changes each by a constant converging to the limiting constant: normalized quasi-subharmonic compactness and Hartogs' upper bound show all subsequential supremum limits equal the supremum of the \(L^1\) limit (the same reasoning used in Lemma 5.43.10, tag 633794C1EFC2). Since a full-mass point-pole representative has no diffuse positive residual curvature, it is already the unique normalized ordinary model of its type, by the curve classification; hence \(v_j\to v\) in \(L^1(C)\).

Lemma 5.43.10 permits pulling \(L^1\) convergence through \(p\), including its critical fibers, proving (C). The polar measure metric identity in Proposition 18.22.3, lines 105–111, proves (D): two distinct Dirac probability masses are mutually singular, so their total-variation distance is two. For (E), the Borel restriction, exact signed total-variation norm, and point-mass fiber identities of Lemma 18.22.2, lines 62–80, yield
\[
\lambda_{U_j}^{\gamma}=A\,L_\gamma(\delta_{s_j}),
\quad \lambda_U^{\gamma}=A\,L_\gamma(\delta_s),
\quad \|\lambda_{U_j}^{\gamma}-\lambda_U^{\gamma}\|_{\rm TV}
= \kappa_\gamma A\|\delta_{s_j}-\delta_s\|_{\rm TV}.
\]
The Green \(L^1\) convergence gives weak convergence of the associated pullback curvature currents and hence their smooth Gauduchon traces. At critical values the equation \(p^*\delta_t=[F_t]\) means the scheme-theoretic multiplicities are automatically incorporated, not dropped.

**Consequences and limitations.** The identity
\[
 (\mathcal M(\theta),\rho_\theta)\longrightarrow
 (\mathcal M(\theta),L^1(dV))
\]
is sequentially continuous by the printed proposition but its inverse on this image is not. Already the ideal subspace has an infinite \(2A\)-separated family parametrized by distinct point poles, so it is not totally bounded in \(\rho_\theta\), although the particular converging sequence is \(L^1\)-precompact. This is *not* a failure of trace-current weak continuity, nor an error in the strong polar metric statement. The argument is insensitive to the fixed Gauduchon choice after the normalization factor \(\kappa_\gamma\) is removed. No general assertion for arbitrary weak limits of polar measures is needed.

**Action / dependents.** Optional caution following Proposition 18.22.3, preserving its metric and attribution. Relevant to any future choice of topologies on ordinary/ideal model spaces and trace measures; no claimed deficiency in §18.22.3's proof. It also warns that weak current convergence alone cannot justify total-variation convergence. The existence/classification and pullback \(L^1\) results listed above are explicit conditional upstream dependencies; these have not been independently certified as entire theorems here.

## Verification boundary and future coverage

The actual fresh proof checks were: §18.17 scaling and active-set case in Lemma 18.17.1, product norm/completeness and ideal measures in Proposition 18.17.3, and correspondence distortion/diameter proof in Proposition 18.17.5; §18.18 gauge and zero-area cases and its metric comparison; §18.22 descended zero-top-mass model structure, positive fiber-trace normalization and Jordan-part separation, and the isometry/convergence proof. §18.16 plus curve measure classification were checked only to the extent cited above. Neither all statements of these sections nor their transitive analytical prerequisites were verified. No project tests, full build, CI, formal proof verification, numerical scripts, website publication, PR or merge were run. Main, reading-edition bodies, source repositories, permanent tags, and registry remain unchanged.

**Explicit user exclusion:** Demailly approximation/regularization and the dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme were **not examined**. Historical records remain **deferred-by-user**, not resolved, repaired, or certified. Next audit should rotate away from these three sections to unrelated unreviewed nonexcluded areas.
