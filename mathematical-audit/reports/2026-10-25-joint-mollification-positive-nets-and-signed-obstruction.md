# Joint mollification of positive Radon nets and a compactly supported signed-net obstruction

**Review date:** 2026-10-25 (Asia/Shanghai). **Integrated main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Previous audit branch head:** 17db5e9b50cd5d14568e717f95a199f8d5da1786. **Scope:** selected actual reading-edition proofs in §§2.2–2.5, incremental §§2.6.1–2.6.2 only. Neither the entire sections nor their full transitive dependencies are certified.

## Source anchors and preconditions

- Radon definition §2.2.1, permanent tag **901C72102EF9**, and regularity §2.2.2, tag **D0882F84DCFC**: main **docs/sections/measures-and-distributions--radon-measures-and-integration/index.html**, blob **f0086e0d7fa46b8d1756eebb839b0ba14e663863**, physical lines **7–51**. The printed positive-measure convention, compact exhaustions and cutoff construction were checked; product-measure and dominated-convergence passages at lines **57–203** were sampled for compatibility, not independently certified.
- Riesz theorem §2.3.3, permanent tag **0C614771FB98**, and density §2.3.5, tag **0BB807E5CBD4**: main **docs/sections/measures-and-distributions--positive-linear-functionals/index.html**, blob **0562702a346f7d8f09974afe97c90bc911bf7790**, physical lines **66–125**. In particular the metric outer-measure separation and its Carathéodory proof were read at **21–58**, not replaced.
- Distribution definition §2.4.1, permanent tag **55085BC2**: main **docs/sections/measures-and-distributions--test-functions-and-distributions/index.html**, blob **beb63e37cdc88e099c3e9a8314fca1219d18c0c4**, physical lines **10–43**. Its explicit directed-net test-functional topology is the topology used here.
- Mollifier Lemma §2.5.1, tag **3C40E6BD1222** (especially clauses (1), (3), (5)), and Proposition §2.5.3, source label **foundations-of-pluripotential-theory-D09EB34D**, permanent tag **0CB24AD25DC3**, especially clauses (1)–(2), main **docs/sections/measures-and-distributions--convolution-and-mollifiers/index.html**, blob **50e1ba12fd379718b6be25a0b797e8014e1eaede**, physical lines **7–35, 38–89, 117–165**. Equation §2.5.4 has permanent tag **3AA3C6A6F513**, lines **152–162**.
- Vague convergence of arbitrary nets §2.6, Proposition §2.6.1, source **foundations-of-pluripotential-theory-915FBB91**, permanent tag **4DFD880D9E4D**, and compact/open Portmanteau Proposition §2.6.2, permanent tag **132090FCDF4A**: main **docs/sections/measures-and-distributions--weak-convergence-of-measures/index.html**, blob **45720b2399a645a1a9a8148873fdc01c634fc5d7**, physical lines **7–53**.

The approximations below are ordinary Euclidean convolution of test functions and distributions, **not** the user-deferred Demailly approximation/regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas or positivity-loss proof programme. The latter is not touched or certified.

## POME-MEASURE-JOINT-MOLL-NET-001

**Severity:** low. **Status:** verified conditional deduction; **not** a false printed theorem.

**Precise statement.** Let Ω be open in ℝ^d, I an arbitrary directed set, and (μ_i) a net of positive Radon measures converging *vaguely* to positive Radon μ. Independently let ε_i>0 tend to zero along the same net. Write ρ_ε for the even compactly supported smooth probability mollifier defined at the beginning of §2.5 and let u_i=μ_i*ρ_{ε_i} on Ω_{ε_i}. Then

\[
u_i(x)\,dx \longrightarrow \mu \quad\text{vaguely on }\Omega.
\]

For each multi-index α, the locally defined distributional derivatives satisfy
\[
\partial^\alpha u_i \longrightarrow \partial^\alpha \mu
\quad\text{weakly in }\mathcal D'(\Omega).
\]
The same conclusion holds for a net of signed or complex locally finite measures ν_i converging against every compactly supported continuous function, **provided** for every compact K⊂Ω there is a tail on which \(\sup_i|\nu_i|(K)<\infty\). Positivity makes this tail variation condition automatic, separately for each K.

**Proof.** Fix f∈C_c(Ω), extend f by zero to ℝ^d, and let S=supp f. Choose δ>0 such that the closed δ-neighborhood K of S is compact in Ω. Let η∈C_c(Ω) satisfy η≥1 on K and η≥0; §2.2 constructs such cutoffs. Since μ_i→μ vaguely, the real numbers \(\int\eta\,d\mu_i\) converge. A convergent *net* of real numbers is bounded on some tail (not necessarily on all of I), hence μ_i(K)≤M_K on that tail. For ε_i<δ, Tonelli and evenness of ρ give
\[
\int_\Omega f(x)u_i(x)\,dx
=\int_\Omega (f*\rho_{\varepsilon_i})(y)\,d\mu_i(y).
\]
Both f and its convolution vanish outside K and
\[
\|f*\rho_{\varepsilon_i}-f\|_\infty
\le \sup_{|h|\le\varepsilon_i}\|f(\cdot-h)-f\|_\infty
\longrightarrow0.
\]
Thus
\[
\left|\int f u_i\,dx-\int f\,d\mu\right|
\le M_K\|f*\rho_{\varepsilon_i}-f\|_\infty
+\left|\int f\,d\mu_i-\int f\,d\mu\right|\to0.
\]
The proof uses directed-net convergence only, without a sequential extraction or exchanging unrelated limits. For φ∈C_c^\infty(Ω), apply the same result to \((-1)^{|\alpha|}\partial^\alpha\phi\), giving the distributional derivative assertion. The signed case is identical with μ_i(K) replaced by |ν_i|(K). QED.

**Proposed addition and affected dependents:** optional corollary to §2.6.1 cross-referencing §2.5.3. It legitimizes coupled parameter limits for positive Radon measures and weak current approximations; it **does not** justify coupled singular-psh regularization or unverified Bedford–Taylor products.

## POME-SIGNED-NET-NONUNIFORM-MOLL-001

**Severity:** low. **Status:** verified conditional deduction with explicit counterexample to a *hypothetical strengthening*; Proposition §2.5.3(2) and §2.6.1 remain correct.

**Claim.** On ℝ there is an arbitrary directed net of **finite signed atomic Radon measures**, all supported in one fixed compact interval K, with ν_i→0 against **every** C_c(ℝ) function, together with ε_i↓0 in the net sense, such that for one fixed real nonnegative ψ∈C_c^\infty(ℝ),
\[
\int_\mathbb R\psi(x)(\nu_i*\rho_{\varepsilon_i})(x)\,dx=1
\quad\text{for all }i.
\]
Consequently one cannot extend §2.5.3(2)'s fixed-distribution mollifier limit to simultaneous *arbitrary signed measure nets* merely from vague convergence, even with uniformly compact supports. Local uniform variation on a common tail is an actual extra restriction.

**Construction and proof.** Choose ψ≥0, ψ∈C_c^\infty(ℝ), with \(\int\psi>0\), and K=[−R−1,R+1] containing the closed 1-neighborhood of supp ψ. For 0<e<1 set \(g_e=\psi*\rho_e\); each g_e is supported in K.

**Linear independence of all distinct radii.** Suppose \(\sum_{j=1}^m a_j g_{e_j}=0\) for pairwise distinct 0<e_j<1. With the Fourier transform on ℝ,
\[
\widehat\psi(\xi)\sum_j a_j\widehat\rho(e_j\xi)=0.
\]
As \(\widehat\psi(0)>0\), it is nonzero in a neighborhood of zero. The compactly supported even probability kernel has an entire Fourier transform and Taylor expansion
\[
\widehat\rho(z)=\sum_{k\ge0}
\frac{(-1)^k z^{2k}}{(2k)!}
\int x^{2k}\rho(x)\,dx,
\]
with every displayed even moment strictly positive. Equating coefficients for k=0,…,m−1 therefore yields \(\sum_j a_j e_j^{2k}=0\). The Vandermonde determinant in the distinct numbers e_j² is nonzero, so all a_j=0. In particular \(\{g_e:0<e<1/N\}\) is infinite-dimensional when restricted to K for every N.

Let I consist of pairs (F,N), where F is any **finite subset** of C_c(ℝ,ℝ) and N≥2 an integer, ordered by inclusion in F and increasing N. This is a directed set. For each i=(F,N), choose \(0<\varepsilon_i<1/N\) such that \(g_{\varepsilon_i}|_K\) is outside the finite-dimensional span of the restrictions of functions in F. The latter choice is possible by the preceding independence.

Let W be the finite-dimensional real vector space on K spanned by \(F|_K\) and \(g_{\varepsilon_i}|_K\). The linear functional ℓ on W that vanishes on \(F|_K\) and takes value 1 on \(g_{\varepsilon_i}|_K\) is well-defined. Point evaluations on K span W*: otherwise a nonzero element of W would vanish at every point of K. Hence ℓ is a finite real linear combination of point evaluations: there are x_{i,j}∈K and real a_{i,j} with
\[
\nu_i=\sum_j a_{i,j}\delta_{x_{i,j}},\qquad
\int f\,d\nu_i=0 \ (f\in F),\qquad
\int g_{\varepsilon_i}\,d\nu_i=1.
\]
For each fixed f∈C_c(ℝ,ℝ), on the tail F⊃{f} one has \(\int f\,d\nu_i=0\); linearity handles complex f. Thus ν_i→0 in the usual weak topology tested by C_c. The radii tend to zero because ε_i<1/N. Finally, since ρ is even, Fubini for each *finite atomic measure* gives
\[
\int\psi(x)(\nu_i*\rho_{\varepsilon_i})(x)\,dx
=\int(\psi*\rho_{\varepsilon_i})(y)\,d\nu_i(y)=1.
\]
The smoothed net therefore does not converge even in distributions. This is a genuine directed-net obstruction: it relies on the absence of any single common variation-bound tail, not on non-Radon measures, escaped support, or a false fixed-T approximation claim. QED.

**Proposed addition and affected dependents:** a concise caution following §2.5.3(2) or §2.6.1: positivity or eventual local uniform variation controls simultaneous weak-limit/mollifier scales. Do not use the fixed-T theorem as if it implied arbitrary joint weak-net continuity. This matters wherever signed distributions or current coefficients are approximated with two moving indices; it establishes **no** error in those dependent arguments without individual examination.

## Other actual checks and limitations

The selected printed proofs of §2.2.2 (local compactness and regularity), §2.3.2–3 (metric outer-measure/Riesz reconstruction), §2.4.1 (LF test-function seminorms), §2.5.1 (uniform-on-compact mollifier convergence), §2.5.3 (fixed-distribution proof via common-compact test functions), and §2.6.1–2 (positive vague-net bounds) were inspected for the precise hypotheses used above. No new false original theorem or confirmed existing proof error was established. Neither the full product-measure construction nor the general theory of locally convex inductive limits nor all §§2.2–2.6 results were fully checked.

Only an **audit-only proposed report**, cumulative ledger, checkpoint and coverage inventory are changed on review/mathematical-audit. No original section HTML, source repository, proof registry, permanent tag, published site, CI, formalization or main branch is changed. The old dedicated Demailly programme remains deferred-by-user, not solved.
