# Bounded-\(L^1\) stability of supporting probabilities, with a sharp unbounded-spike obstruction

**Date:** 2026-11-02. **Production main examined:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Finding:** **POME-SUPPORT-BOUNDED-L1-GRAPH-001**.  
**Severity:** low. **Status:** verified conditional deduction (with a counterexample to dropping a hypothesis); **not** a false Pome theorem or an applied repair.  
**Scope:** nonexcluded scalar-functional and probability-duality steps only. No Demailly approximation/regularization, Bergman, \(L^2\) or Ohsawa–Takegoshi, multiscale atlas, or curvature-loss proof-completion was inspected.

## Exact integrated reading-edition anchors

The following are current production-main HTML files, **not** source-book theorem-number lookups:

| Pome locator | Main HTML file and Git blob | Source label and permanent tag | Physical line anchors |
| --- | --- | --- | --- |
| §11.32 ambient standing hypotheses | docs/sections/normalization-and-weak-adjoint-measures/index.html; 031b5d62d25d7ff03d95e4a14988399527cc946a | non-kahler-pluripotential-theory:75571769; 7091FEDB43F0 | 5–12 (orientation/definitions only) |
| Proposition 11.33.2 | docs/sections/normalization-and-weak-adjoint-measures--the-scalar-functional/index.html; fff86de757578ed2be369ba752123f62f3d31044 | non-kahler-pluripotential-theory:6D175DAF; 2770AB03C0D2 | 26–55 (normalization and monotone translation bounds) |
| Theorem 11.33.5 | same §11.33 HTML and blob | non-kahler-pluripotential-theory:D502EBBF; 5E3583383688 | 88–120 (bounded \(L^1\) scalar convergence) |
| Theorem 11.34.2 | docs/sections/normalization-and-weak-adjoint-measures--supporting-probability-measures/index.html; a8afa97be049b56b6c7d18302499364022feaa39 | non-kahler-pluripotential-theory:97DE633E; 86A7D85266AA | 17–50 (support existence, compactness, absolute continuity) |
| Proposition 11.34.3 | same §11.34 HTML and blob | non-kahler-pluripotential-theory:AE3FA53A; CB2DC1F2B712 | 51–69 (printed **uniform**-convergence stability) |
| Proposition 11.35.2 and Eq. 11.35.3 | docs/sections/normalization-and-weak-adjoint-measures--a-convex-functional-on-probability-measures/index.html; 9a4ba5a98abd3273a6872c68beccf764e936d3f0 | non-kahler-pluripotential-theory:A1D8D375; 0C21983AC42D; equation source 86EF99CC, tag 88A1B49C1D77 | 20–42 (Fenchel equality for supports) |
| Theorem 11.35.4 / Eq. 11.35.5 | same §11.35 HTML and blob | non-kahler-pluripotential-theory:9F623A72; 6830F8DE9750; equation source 3339FE17, tag FA8EC628AEAE | 43–84 (uniform absolute continuity of bounded dual sublevels and weak \(L^1\) consequence) |

No numbered mathematical theorem occurs in §11.32; its premise is an orientation-only check. The fresh proof below concerns the **joint** consequence of the already integrated §§11.33–11.35, rather than a claim of first proof-level coverage of those whole sections.

## New precise deduction: the support graph is sequentially closed under bounded \(L^1\) variations

Retain the standing nonclosed-background setting of §11.32: connected compact complex \(X\), a smooth positive \(\mathrm dV\), a semipositive big real \((1,1)\) background \(\theta\), a fixed model type \(\varphi\) satisfying the stated smaller-background envelope hypothesis, and the scalar \(B_\varphi(F)=\log c_\varphi(F)\) with support set \(\mathcal A_\varphi(F)\subset\mathcal P(X)\) as in Eq. 11.34.1. Do **not** suppose \(\theta\) closed or that supports are unique.

**Proposition (conditional on the printed results above).** Suppose \(F_j,F\in C(X,\mathbb R)\), there is a common \(M<\infty\) with \(\|F_j\|_\infty\le M\), and
\[
 \|F_j-F\|_{L^1(\mathrm dV)}\longrightarrow 0.
\]
Choose any \(\nu_j\in\mathcal A_\varphi(F_j)\). Then:

1. The entire family \(\{\nu_j\}\) lies in the **single** dual sublevel
\[
 \mathcal K_{B_\varphi(0)+2M}
 =\{\nu:H_\varphi(\nu)\le B_\varphi(0)+2M\}.
\]
In particular its densities are uniformly integrable in \(L^1(\mathrm dV)\).
2. Every weak-* cluster probability \(\nu\) of \(\nu_j\) lies in \(\mathcal A_\varphi(F)\). Along any such convergent subsequence, the densities converge **weakly in \(L^1(\mathrm dV)\)**, not merely as measures.
3. If \(\mathcal A_\varphi(F)=\{\nu_F\}\), the **whole sequence** of densities \(\mathrm d\nu_j/\mathrm dV\) converges weakly in \(L^1(\mathrm dV)\) to \(\mathrm d\nu_F/\mathrm dV\). Equivalently,
\[
  \int_X g\,\mathrm d\nu_j\longrightarrow \int_Xg\,\mathrm d\nu_F
 \quad\text{for every fixed bounded measurable }g.
\]

The first conclusion is a uniform-integrability statement, not a claim of total-variation or strong \(L^1\) convergence. There is no assumption that \(F_j\to F\) in the uniform norm.

### Complete proof from declared internal inputs

Because \(F\) is continuous and \(F_j\) are uniformly bounded, \(L^1\) convergence implies \(\|F\|_\infty\le M\) (the smooth positive volume charges every nonempty open set). The printed Proposition 11.33.2 gives
\[
 B_\varphi(F_j)\le B_\varphi(0)+M .
\]
For a support \(\nu_j\), the equality clause of Proposition 11.35.2 yields
\[
 H_\varphi(\nu_j)
   = B_\varphi(F_j)+\int_X F_j\,\mathrm d\nu_j
   \le B_\varphi(0)+2M.
\]
Theorem 11.35.4 therefore places every \(\nu_j\) in one weakly compact, uniformly absolutely continuous dual sublevel. It follows directly, rather than by a false assertion of uniformly bounded densities, that for every \(\varepsilon>0\) there is \(\delta>0\) with
\[
 \mathrm dV(E)<\delta\Longrightarrow
 \sup_j \nu_j(E)<\varepsilon
\]
for all Borel sets \(E\).

For any fixed \(a>0\), let \(E_{j,a}=\{|F_j-F|>a\}\). Markov's estimate gives \(\mathrm dV(E_{j,a})\le a^{-1}\|F_j-F\|_{L^1(\mathrm dV)}\to0\). Since \(|F_j-F|\le2M\),
\[
 \int_X |F_j-F|\,\mathrm d\nu_j
 \le a+2M\,\nu_j(E_{j,a}).
\]
Uniform absolute continuity implies \(\limsup_j\int|F_j-F|\,\mathrm d\nu_j\le a\); let \(a\downarrow0\). Thus
\[
 \int_X(F_j-F)\,\mathrm d\nu_j\longrightarrow0. \tag{*}
\]
This step is **not** justified by ordinary weak convergence of probabilities alone; (*), and hence the stronger result, needs the common dual-sublevel estimate.

By compactness, pass to a weakly convergent subsequence \(\nu_{j_k}\rightharpoonup\nu\). For each \(G\in C(X)\), the printed support inequality says
\[
 B_\varphi(G)
 \le B_\varphi(F_{j_k})-\int_X G\,\mathrm d\nu_{j_k}
                   +\int_XF_{j_k}\,\mathrm d\nu_{j_k}.
\]
Theorem 11.33.5 gives \(B_\varphi(F_{j_k})\to B_\varphi(F)\). The middle term converges weakly because \(G\) is continuous; for the final term use (*) and then weak convergence against the fixed continuous \(F\). Therefore
\[
 B_\varphi(G)\le B_\varphi(F)-\int_X(G-F)\,\mathrm d\nu.
\]
As this holds for all continuous \(G\), \(\nu\in\mathcal A_\varphi(F)\) by Eq. 11.34.1. Theorem 11.35.4 supplies weak \(L^1\) convergence of densities within the common dual sublevel.

If \(\mathcal A_\varphi(F)\) is a singleton, every subsequence has the same weak cluster point by the previous argument. Compactness forces \(\nu_j\rightharpoonup\nu_F\) without extraction, and the final clause of Theorem 11.35.4 upgrades this convergence to weak \(L^1\) convergence of the densities. This proves all three assertions.

### Sharp obstruction: omitting the common \(L^\infty\) bound is impossible even on \(\mathbb P^1\)

Fix \(X=\mathbb P^1\) with its unit-mass Fubini–Study area \(\omega=\mathrm dV\), \(\theta=\omega\), and the smooth reference \(\varphi=0\). The \(n=1\) Stokes identity, also recorded in the proof of Theorem 11.34.9, gives
\[
 B_0(G)=-\log\int_Xe^G\,\mathrm dV,\qquad
 \mathcal A_0(G)
 =\left\{\frac{e^G\,\mathrm dV}{\int_Xe^G\,\mathrm dV}\right\}.
\]
Pick \(x_0\in X\). Choose radii \(r_j\downarrow0\) so that \(\mathrm dV(B(x_0,r_j))\asymp e^{-j/2}\), and smooth cutoffs \(0\le\chi_j\le1\) equal to one on \(B(x_0,r_j/2)\), supported in \(B(x_0,r_j)\). Set \(F_j=j\chi_j\). Then
\[
 \|F_j\|_{L^1(\mathrm dV)}
 \le j\,\mathrm dV(B(x_0,r_j))
 =O(je^{-j/2})\longrightarrow0.
\]
But, because on a smooth surface the smaller concentric ball has volume comparable to the larger,
\[
 Z_j:=\int_Xe^{F_j}\,\mathrm dV
 \ \ge e^j\,\mathrm dV(B(x_0,r_j/2))
 \ \gtrsim e^{j/2}\longrightarrow\infty.
\]
The unique supporting probability \(\nu_j=Z_j^{-1}e^{F_j}\,\mathrm dV\) satisfies
\[
 \nu_j(X\setminus B(x_0,r_j))
 \le Z_j^{-1}\longrightarrow0,
\]
and consequently \(\nu_j\rightharpoonup\delta_{x_0}\). In contrast, \(\mathcal A_0(0)=\{\mathrm dV\}\), so its graph does **not** remain closed for arbitrary unbounded \(L^1\)-convergent logarithmic densities. Also \(B_0(F_j)=-\log Z_j\to-\infty\) whereas \(B_0(0)=0\). The spike is continuous (indeed smooth) for every \(j\). This is a counterexample to dropping the hypothesis of the **new** statement, not to the printed bounded-density Theorem 11.33.5 or uniform-convergence Proposition 11.34.3.

## Audit disposition, dependencies, and coverage

- **Mathematical status:** low / **verified conditional deduction**. Neither Proposition 11.34.3 nor Theorems 11.33.5 and 11.35.4 is contradicted. The new conclusion is stronger than the uniform-convergence graph statement under the alternative bounded-\(L^1\) hypothesis. The counterexample proves that the boundedness requirement cannot simply be deleted.
- **Precise dependencies:** the printed scalar existence and uniqueness for fixed ordinary type (Theorem 15.12.1); bounded \(L^1\) scalar continuity (11.33.5); supporting probabilities and Fenchel equality (11.34.2, 11.35.2); uniform absolute continuity and weak-\(L^1\) consequences for dual sublevels (11.35.4). These are internal dependencies **used conditionally**, not newly certified, and their unrelated approximation/proof inputs were not reopened. The spike calculation on \(\mathbb P^1\) uses only dimension-one Stokes and normalized densities, with no smoothing/regularization programme.
- **Suggested separately reviewable textual improvement:** optional corollary after Proposition 11.34.3, with the exact uniform-\(L^\infty\), \(L^1\), and singleton qualifiers above; link its proof to 11.33.5, 11.35.2, and 11.35.4. Do not silently replace Proposition 11.34.3's hypotheses.
- **Affected downstream statements:** potential stability uses of supporting probabilities and entropy (§§11.35–11.40) and vanishing-exponent selection (§11.44). No downstream theorem is claimed repaired or certified.
- **Actual review scope:** new joint proof of an upper-hemicontinuity principle in already partly examined §§11.33–11.35; directly revisited §§11.33.2/.5, 11.34.1–3, 11.35.1–5 and dimension-one Stokes in §11.34.9. §11.32 was read for **standing hypotheses only**, not a theorem review. The previous 25-chapter/747-ToC-section inventory remains unchanged, and **zero whole mathematical sections** are certified.
- **Excluded topic:** Demailly regularization/approximation and the specifically excluded Bergman, \(L^2\), OT, multiscale-atlas and positivity-loss programme remain **deferred-by-user**, not solved or audited.
- **Operations:** review-branch Markdown documentation only. No edits to production main, canonicalized statements, source manuscripts, registered tags, site, CI, builds, tests, or formalization.
