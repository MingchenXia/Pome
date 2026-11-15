# 2026-11-15 — Independent multitorus homogeneous-ideal, Gauss-value, and flatness audit

**Finding:** \`POME-NA-MULTITORUS-GRADED-IDEAL-GAUSS-FLATNESS-001\` — **low / verified conditional deduction**. The one-variable Lemma 22.1.94 is correct; this report proves a genuinely new several-parameter extension, with exact limitations. This is **not** a claim that the several-parameter theorem already appears in Pome or that the global non-Archimedean comparison is certified.

**Production main reviewed:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Integrated reading-edition file:** \`docs/sections/non-archimedean-pluripotential-theory/index.html\`, blob \`8448d710690ebe1cc28040f9611d05c9d008a961\`. Direct reading: Lemma **22.1.94**, source label \`sgpt:AB6FE74C\`, permanent tag \`76252E7717AC\`, statement lines **1402–1403**, proof lines **1410–1415**; Equation **22.1.95**, \`sgpt:EC9FB89B\`, permanent tag \`6126C03E6587\`, lines **1404–1407**. Hypothesis/conclusion comparison only: Lemma **22.1.96**, \`sgpt:0D0A3D2C\`, permanent \`AF0C82DE24E9\`, lines **1418–1427**; downstream Proposition **22.1.98**, \`sgpt:4D7EEB4A\`, permanent \`6A232EAE791C\`, lines **1445–1492**, particularly ideal expansion **22.1.99**, \`sgpt:B0939F32\`, permanent \`9186BF0A5F55\`, lines **1466–1483**. No review of the analytic global-generation proof at 22.1.97 (lines 1433–1442).

## A fully proved multigraded replacement for the elementary algebraic step

Let \(R\) be a commutative Noetherian \(\mathbb C\)-algebra, \(d\ge1\), \(S=R[t_1,\ldots,t_d]\), and \(I\subseteq S\) an ideal. Suppose every coordinatewise circle rotation \(\mathbf t\mapsto (\zeta_1t_1,\ldots,\zeta_dt_d)\), \(\boldsymbol\zeta\in(S^1)^d\), sends \(I\) into \(I\); the action on \(R\) is trivial. The inverse rotations imply equality. For \(\alpha\in\mathbb N^d\), set
\[
J_\alpha=\{r\in R:r\mathbf t^\alpha\in I\},\qquad
\alpha\le\beta\ \Longleftrightarrow\ \alpha_i\le\beta_i\ \text{for all }i.
\]
Then:

1. Every coefficient is separately in the ideal: \(I=\bigoplus_{\alpha\in\mathbb N^d}J_\alpha\mathbf t^\alpha\) **as graded \(R\)-modules**, and \(J_\alpha\subseteq J_\beta\) whenever \(\alpha\le\beta\).
2. There are finitely many pairs \((\beta_j,c_j)\in\mathbb N^d\times R\), \(1\le j\le N\), such that
   \[
   I=(c_1\mathbf t^{\beta_1},\ldots,c_N\mathbf t^{\beta_N}),\qquad
   J_\alpha=\sum_{\beta_j\le\alpha}(c_j).
   \tag{A}
   \]
   Put \(J_*=\sum_j(c_j)\) and \(B_i=\max_j(\beta_j)_i\). Then \(J_\alpha=J_*\) for \(\alpha\ge B\). For \(I=0\), take all \(J_\alpha=0\) and \(J_*=0\).
3. With \(T=t_1\cdots t_d\),
   \[
   (I:T^\infty)=J_*S,\qquad
   (S/I)[T^{-1}]\simeq(R/J_*)[t_1^{\pm1},\ldots,t_d^{\pm1}].
   \tag{B}
   \]
   In particular, a product over the dense algebraic torus need **not** be flat over the affine parameter space.
4. Writing \(A=S/I\), one has the sharp criterion
   \[
   A\text{ flat over }\mathbb C[t_1,\ldots,t_d]
   \iff (t_i:A\to A)\text{ injective for all }i
   \iff J_\alpha=J_0\text{ for every }\alpha
   \iff I=J_0S.
   \tag{C}
   \]
   The equivalence involving coordinatewise injectivity holds for these *multigraded quotient algebras*; it is not asserted for arbitrary modules.

**Proof of (1) and (2).** Given \(f=\sum_{\alpha\in F}r_\alpha\mathbf t^\alpha\in I\) with finite support, choose an integer \(q\) larger than every occurring coordinate exponent. Averaging the finitely many rotated polynomials over \(\mu_q^d\subset(S^1)^d\), with character \(\boldsymbol\zeta^{-\alpha}\), gives exactly \(r_\alpha\mathbf t^\alpha\in I\). This is a finite algebraic sum, so no closure or integration in \(I\) is needed. This proves coefficient separation and monotonicity follows by multiplication by monomials. Since \(R[\mathbf t]\) is Noetherian, choose finitely many generators of \(I\), decompose each into its finitely many homogeneous monomial terms, and use these homogeneous terms as a new generating family. Coefficient comparison proves (A) and the coordinatewise threshold \(B\) proves stabilization.

**Proof of (B).** If \(f=\sum r_\alpha\mathbf t^\alpha\) and \(T^m f\in I\), then every \(r_\alpha\in J_{\alpha+m\mathbf1}\subseteq J_*\). Conversely, if all coefficients lie in \(J_*\), choose \(m\) sufficiently large that \(\alpha+m\mathbf1\ge B\) simultaneously for the finite support; then \(T^m f\in I\). This proves the saturation formula. Inverting \(T\) inverts each \(t_i\), and the equality of ideals after localization proves the stated Laurent quotient.

**Proof of (C).** Flatness over \(\mathbb C[\mathbf t]\) implies injectivity of each multiplication map by tensoring the injective multiplication map \(t_i:\mathbb C[\mathbf t]\to\mathbb C[\mathbf t]\) with \(A\). If multiplication by \(t_i\) on \(A\) is injective and \(r\in J_{\alpha+e_i}\), then \(t_i(r\mathbf t^\alpha)=0\) in \(A\), so \(r\in J_\alpha\). The reverse inclusion is automatic, hence all \(J_\alpha\) equal \(J_0\). Finally \(I=J_0S\) implies
\(A\simeq (R/J_0)\otimes_\mathbb C\mathbb C[\mathbf t]\), a free, possibly infinite-rank, \(\mathbb C[\mathbf t]\)-module after choosing a complex basis of \(R/J_0\). Thus flatness follows.

## A finite polyhedral Gauss-value formula, with an explicit three-region model

Additionally assume that \(R\) is an integral domain with a real-valued valuation \(v\) of its fraction field, nonnegative on \(R\), and take parameter weights \(w_i\ge0\). For the standard weighted Gauss valuation
\[
v_{\mathbf w}\!\left(\sum_\alpha a_\alpha\mathbf t^\alpha\right)
 =\min_{\alpha:a_\alpha\ne0}\bigl(v(a_\alpha)+\langle\alpha,\mathbf w\rangle\bigr),
\]
the graded-domain argument gives multiplicativity (the associated graded ring is a polynomial ring over the domain \(\operatorname{gr}_v(R)\)). If \(I\ne0\), (A) and nonnegativity of \(v_{\mathbf w}\) on \(S\) imply
\[
\boxed{\ v_{\mathbf w}(I)=\min_{1\le j\le N}
  \bigl(v(c_j)+\langle\beta_j,\mathbf w\rangle\bigr).\ }
\tag{D}
\]
Thus this ideal-value function is **continuous, concave, coordinatewise nondecreasing, and piecewise integral-affine in \(\mathbf w\)**. This is a valuation-level statement about a *fixed algebraic ideal*, not a proof of the analytic limiting assertions in §22.1.98.

For \(R=\mathbb C[x,y]\), take the divisorial valuation \(v=\operatorname{ord}_E\) of the exceptional divisor of the blowup at the origin, so \(v(x)=v(y)=1\), and
\[
I=(x^3t_1^2,\ y^3t_2^3,\ xy\,t_1^3t_2).
\]
Then \(J_*=(x^3,y^3,xy)\ne R\) and (D) reads
\[
v_{(w_1,w_2)}(I)=\min(3+2w_1,\ 3+3w_2,\ 2+3w_1+w_2).
\]
At \((0,10),(10,0),(0,0)\), the active terms are respectively the **first, second, and third** (exact value triples \((3,33,12)\), \((23,3,32)\), \((3,3,2)\)). Therefore the truly two-parameter formula cannot be replaced by a single linear branch. Its quotient has a fixed torus restriction by (B) but is nonflat by (C), since \(J_0=0\ne J_*\).

**Necessity of the full torus hypothesis.** If only *diagonal* \(S^1\) rotation is assumed, individual multi-degrees need not split: \(I=(t_1+t_2)\subset\mathbb C[t_1,t_2]\) is invariant under simultaneous scaling, but neither \(t_1\) nor \(t_2\) belongs to \(I\). One obtains total-degree homogeneity, not \(\mathbb N^2\)-multigrading. This counterexample refutes an unprinted overgeneralization, **not** Lemma 22.1.94.

## Comparison, provenance, and open dependencies

The printed Lemma 22.1.94 proves exactly the \(d=1\) case, with one increasing chain \(I_0\subseteq I_1\subseteq\cdots\). Its proof is mathematically correct. The previously registered **POME-NA-S1-IDEAL-TORSION-FLATNESS-001** (2026-11-02) already proves the **one-parameter** flatness/saturation criterion, and is **not** claimed again. What is new here is the \((S^1)^d\)-grading, finite *multi-index* coefficient formula, all-coordinate flatness characterization, and finite concave Gauss polyhedral formula with a three-region two-variable example.

The printed §22.1.96 gluing argument invokes GAGA and remains a separately recorded **external mathematical dependency**, not independently eliminated here. §22.1.97 invokes Siu/Matsumura global generation, which this run **does not audit** and does not use. §22.1.98 uses the **one-variable** ideal expansion, and this independent multitorus result neither repairs nor certifies its analytic/global-generation steps. Historical source attribution and both source and permanent labels must be retained.

**Proposed optional future addition (not applied):** a separate multi-parameter algebraic lemma immediately after 22.1.94, including the full torus versus diagonal torus distinction and (D), useful for possible higher-rank degeneration extensions. No printed false theorem identified; no source, registry, canonicalization or published reading-page changes.

**Coverage delta:** first direct inspection of the multitorus generalization of 22.1.94 and selected downstream dependencies, **not** a first visit to numbered §22.1, which was previously partially sampled. **+0 newly first-visited numbered sections; +0 wholly certified sections**; exact main ToC remains 25 chapters and 747 numbered sections. No project build, tests, GitHub Actions, publication or formal proof check. All user-excluded Demailly approximation/regularization and dedicated Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss programmes remain **deferred-by-user**, not resolved or certified.
