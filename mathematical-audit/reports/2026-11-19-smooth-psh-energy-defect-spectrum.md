# Audit of §17.4: continuity, compactness, and the complete smooth energy-defect spectrum

Date: 2026-11-19
Finding ID: **POME-ENERGY-SMOOTH-L1-DEFECT-SPECTRUM-001**
Classification: **low / verified conditional deduction** (strengthening of an existing example, **not** a false theorem or an asserted repair)
Review baseline: production \`main\` **b6933b772f41b45918f7e25ed1afbbb1fd892272**.
Integrated section: \`docs/sections/relative-energy-and-perron-segments--continuity-and-compactness/index.html\`; blob **6fd38d5ff9d0037e9d0d347814a95ad97331715f**, mathematical text and proofs on physical lines **7–242** (whole section).
Source: \`foundations-of-pluripotential-theory\`; Example 17.4.11 source label \`68158160\`, permanent tag **\`27DF9596E862\`** (lines 226–242).
Internal energy identity: \`docs/sections/relative-energy-and-perron-segments--relative-monge-ampere-energy/index.html\`, blob \`16fdcc4c6a6f0cc75e69ba267bd7da2b2d7922a1\`; Example 17.3.16 source label \`0C651973\`, permanent tag **\`6EAA0093766C\`** (lines 220–226, selected identity only).
Related whole-section result tags: Proposition 17.4.1 **\`049F75F5547D\`** (lines 10–76), Lemma 17.4.3 **\`369EDE8DEEC5\`** (79–92), Proposition 17.4.4 **\`2FF0E77E9188\`** (95–113), Corollary 17.4.5 **\`85CFF04E2CEC\`** (116–135), Proposition 17.4.7 **\`1A67C7F5BE56\`** (150–169).

## New precise deduction

Normalize \(\omega=dd^c\log(1+|z|^2)\) on \(X=\mathbb P^1\), with \(\int_X\omega=1\) and \(dd^c=\frac{i}{2\pi}\partial\bar\partial\). For **every prescribed** \(\ell\in[0,\infty)\), there are smooth, strictly \(\omega\)-psh potentials \(u_a\), indexed by \(a\downarrow0\), with
\[
\sup_Xu_a=0,\quad u_a\le0,\quad u_a\longrightarrow0\text{ in }L^1(X),\quad
\omega+dd^cu_a\rightharpoonup\omega,
\]
yet
\[
E_\omega(u_a)\longrightarrow-\ell,\qquad
du_a\wedge d^cu_a\rightharpoonup 2\ell\,\delta_0
\quad\text{as positive Radon measures.}
\]
There is also such a sequence with \(E_\omega(u_a)\to-\infty\), while the other assertions except the finite Dirichlet-measure limit remain valid. The defect \(\ell=\tfrac12\) is the already printed Example 17.4.11; the **whole prescribed spectrum, weak Monge–Ampère convergence, and precise Dirichlet-energy concentration** are the present deduction. We do not count the printed example itself as newly discovered.

### Complete elementary calculation

For \(0<a<1\), \(0<\varepsilon<1\), put
\[
u_{a,\varepsilon}(z)=a\log\frac{|z|^2+\varepsilon}{1+|z|^2}.
\]
This extends smoothly over infinity with value \(0\), is nonpositive with \(\sup_Xu_{a,\varepsilon}=0\), and
\[
\omega+dd^cu_{a,\varepsilon}
=(1-a)\omega+a\,dd^c\log(|z|^2+\varepsilon)>0
\]
where the second term is the positive smooth form associated with the scaled Fubini–Study potential, expressed in the affine chart. The \(L^1\) squeeze
\[
a\log\frac{|z|^2}{1+|z|^2}\ \le u_{a,\varepsilon}\le0
\]
holds uniformly in \(0<\varepsilon<1\). The left-hand logarithm is integrable against \(\omega\); hence \(u_{a,\varepsilon(a)}\to0\) in \(L^1\) for *any* choice of \(\varepsilon(a)\in(0,1)\). For smooth test \(f\), Stokes gives \(\int f\,dd^cu_a=\int u_a\,dd^cf\to0\). Positivity and unit total mass then give the claimed weak convergence of the Monge–Ampère measures against all continuous tests.

Set \(r=\log|z|^2\), \(F_\varepsilon(r)=\log(e^r+\varepsilon)-\log(1+e^r)\). The angular integration with the above \(dd^c\) convention yields
\[
\int_Xdu_{a,\varepsilon}\wedge d^cu_{a,\varepsilon}
=a^2\int_{-\infty}^{\infty}\left[
\frac{e^r}{e^r+\varepsilon}-\frac{e^r}{1+e^r}
\right]^2dr.
\]
For \(0<\varepsilon<1/2\), the explicit estimates of Example 17.4.11 give, **with an absolute \(O(1)\) independent of \(\varepsilon\)**,
\[
\int_{\mathbb R}(F'_\varepsilon)^2dr=-\log\varepsilon+O(1).
\]
Indeed on \([\log\varepsilon,0]\), \(0\le F'\le1\), \(1-F'\le\varepsilon e^{-r}+e^r\), the integral of the last two terms is at most \(2\), and the squared tail integrals on \((-\infty,\log\varepsilon)\) and \((0,\infty)\) are each at most \(1/2\). The exact energy identity from Example 17.3.16 is
\[
E_\omega(u)=\int_Xu\,\omega-\tfrac12\int_Xdu\wedge d^cu.
\]

For prescribed finite \(\ell\), take
\[
\varepsilon(a)=\exp\left(-\frac{2\ell}{a^2}-\frac1a\right).
\]
The uniform error estimate gives
\[
\int_Xdu_a\wedge d^cu_a
=a^2\bigl(2\ell/a^2+1/a+O(1)\bigr)\longrightarrow 2\ell;
\]
also \(\int_Xu_a\omega\to0\), so \(E_\omega(u_a)\to-\ell\).
For the infinite defect, take \(\varepsilon(a)=\exp(-a^{-3})\), which gives total Dirichlet mass \(a^{-1}+O(a^2)\to\infty\) and energy tending to \(-\infty\).

For finite \(\ell\), the nonnegative measures \(\sigma_a=du_a\wedge d^cu_a\) also have an **exact spatial concentration**. If \(R>0\) is fixed, the part outside \(\{|z|<R\}\) has radial integral over \(r\ge2\log R\); using \(0\le F'\le1\) for \(r\le0\) and \(F'(r)\le e^{-r}\) for \(r\ge0\), this is at most \(C_Ra^2\to0\), independently of \(\varepsilon(a)\). Since \(\sigma_a(X)\to2\ell\), every weak limit is \(2\ell\,\delta_0\). No unproved exchange of non-pluripolar products or weak-limit nonlinearities is used.

## Audit of the printed integrated arguments

- **17.4.1, lines 10–76:** checked bounded-difference truncation, capacity absolute continuity, weak measure convergence, local capacity convergence, the uniform energy-tail estimate (17.4.2), and the final **net** step. The extracted increasing sequence is only envelope-determining, **not assumed cofinal** in the original directed set; comparing energy suprema is the necessary and correct argument. This relies conditionally on the cited internal 5.10.2, 7.6.1, 13.8.9, 16.27.17–18, and 17.2.2.
- **17.4.3–17.4.5, lines 79–135:** checked Hartogs tail-envelope argument, stability of \(u\preceq\phi\) in \(L^1\), upper semicontinuity of energy, and both compactness assertions. The compactness of the normalized set \(K_\phi\) **does not imply** a uniform lower bound on energy: the smooth family above is an explicit sharp distinction.
- **17.4.6–17.4.10, lines 138–224:** checked upper-envelope class stability, mass comparison and contact-set estimate for rooftops, the singularity-envelope identity, polynomial affine-path derivative, and ordered tangent/cocycle bounds. In particular the rooftop finite-energy assertion uses the original nonnegative-contact inequality, not a presumed equality on overlapping contacts. Dependence on §16.13 is retained; no excluded approximation proof is revisited.
- **17.4.11, lines 226–242:** verified Fubini–Study normalization, smooth positive curvature, the \(r=\log|z|^2\) radial factor, and the **uniform** \(O(1)\) tail bound. The printed \(E\to-1/2\) follows; the displayed new spectrum is a strictly stronger conclusion.

**Classification and resolution.** **Verified conditional deduction, low severity**; no confirmed false statement and no new independent printed proof gap found in this direct reading. The exact result can be added after Example 17.4.11, or preserved as a cross-reference in a future separately reviewed source/body patch. No integrated mathematical body, tag, or registry was edited.

**Dependencies / unresolved scope.** The proof of the new example itself uses only positivity of the explicit forms, Stokes, the radial integral and the known curve-energy definition. A *fully certified transitive proof audit* of the current theorem chain 5.10.2 → 17.4.1, local capacity convergence, and roof-contact measure statements has **not** been performed in this run. Some other proofs in the collection cite user-excluded regularization; such dependencies, if encountered, remain **deferred-by-user**, neither repaired nor certified. No scripts, project tests, builds, CI, publication or full-repository verification were performed.
