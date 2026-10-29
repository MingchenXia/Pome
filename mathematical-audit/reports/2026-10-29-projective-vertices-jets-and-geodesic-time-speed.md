# Pome mathematical audit — 2026-10-29: projective vertices, finite-point jets, and geodesic time speed

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Review branch at inspection:** a5580c7e0173575360c43a40e83bec3e870c06be.  
**Classification:** three low-severity **verified conditional deductions**, not confirmed false printed theorems. The exact elementary projective calculations are independent; invoking the general printed analytic theorems remains conditional on their unverified upstream inputs. No previous finding was closed or reclassified.

## POME-PROJECTIVE-VERTICES-WALDSCHMIDT-EXACT-001

**Status/severity:** verified conditional deduction / low.  
**Main reading-edition anchors:** <code>docs/sections/entire-function-growth-and-algebraic-zero-sets--refined-bounds-for-simultaneous-vanishing-orders/index.html</code>, blob <code>8ff4e22eede7fe72ba7bbceeb221ef8b2ed20cf7</code>, Definition 9.56.1 (<code>demailly-complex-geometry:4C4F1642</code>, permanent tag <code>145E38D5855C</code>, physical lines 10–20), Theorem 9.56.4 (<code>demailly-complex-geometry:711F4C56</code>, permanent tag <code>D5C665BE2BA4</code>, lines 106–115; Equation 9.56.5 tag <code>B104C3AB0116</code>), Corollary 9.56.6 (<code>demailly-complex-geometry:5BBC9BA7</code>, tag <code>A99D1189F3F3</code>, lines 176–185).

**Independent calculation.** Take $n\ge 2$, and let $S=\{e_0,\ldots,e_n\}\subset\mathbb P^n$ consist of the coordinate vertices. Then, for every integer $t\ge1$,
\[
\omega_t(S)=\left\lceil\frac{(n+1)t}{n}\right\rceil,\qquad
\Omega(S)=\frac{n+1}{n}.
\]
Indeed, for any degree-$d$ homogeneous polynomial $P$, its vanishing order at $e_i$ is the minimum of $d-a_i$ over monomials $X_0^{a_0}\cdots X_n^{a_n}$ appearing with nonzero coefficients, since distinct monomials remain distinct after passing to the affine chart $X_i=1$. If all vertex orders are at least $t$, every occurring exponent obeys $a_i\le d-t$, and hence
\[
d=\sum_{i=0}^n a_i\le(n+1)(d-t),\quad
d\ge (n+1)t/n.
\]
Conversely, at $d=\lceil(n+1)t/n\rceil$, the integer capacities $d-t\ge0$ satisfy $(n+1)(d-t)\ge d$. Distributing exactly $d$ exponent units among $n+1$ coordinates with each exponent at most $d-t$ gives a nonzero homogeneous monomial with the required orders. This proves the formula without invoking analytic extension or approximation.

**Exact equality in the printed refined estimate.** Fix $t_1=1$, take $t_2=nk$ for $k\ge1$, and use $P=(X_0\cdots X_n)^k$, which has degree $D=(n+1)k=\omega_{nk}(S)$ and order $nk$ at every vertex. The parameter of Theorem 9.56.4 is $\alpha=(t_1+n-1)/t_2=1/k$. Every irreducible coordinate-hyperplane factor of $P$ occurs to multiplicity $k$, so $\alpha k=1$, all fractional divisor coefficients $r_j$ vanish, and $\Delta=0$ has an empty nonintegrability locus (the convention is $a=0$). Thus
\[
\omega_1(S)+n-a-1=2+n-1=n+1=\alpha D,
\]
so the displayed Theorem 9.56.4 inequality and the improved zero-exceptional-locus bound in Corollary 9.56.6 are attained exactly in every dimension $n\ge2$:
\[
\frac{\omega_1(S)+n-1}{n}=\frac{n+1}{n}=\Omega(S).
\]
The algebraic calculation independently checks the normalizations and sharpness on this model. **It does not certify Theorem 9.56.4's general proof:** its analytic extension lemma and weighted $L^2$/Ohsawa–Takegoshi inputs are expressly outside this audit.

**Proposed action/dependents:** optional self-contained sharpness example following Corollary 9.56.6. Protect the distinction between the coarse bound and the exceptional-locus refinement; affects §9.55 arithmetic vanishing and §19 graded-series/Okounkov-body comparisons. No canonicalization, source theorem, or tag change is proposed.

## POME-PROJECTIVE-JET-CRT-SHARP-001

**Status/severity:** verified conditional deduction / low.  
**Main anchors:** <code>docs/sections/jets-integral-curvature-and-projective-embeddings--compact-jet-interpolation-and-positive-line-bundles/index.html</code>, blob <code>c517f4c61b6498b988826cc428fdd260e355d5ad</code>, Theorem 10.39.1, source <code>demailly-complex-geometry:73141B3D</code>, permanent tag <code>1EAA4FEF8A05</code>, physical lines 7–21 (the printed proof begins at line 24). This is the **first directly proved, nonexcluded projective model** checked in this previously inventory-only section; the general $L^2$ proof remains deferred.

**Claim and constructive proof.** On $X=\mathbb P^n$, $L=\mathcal O(1)$, for any $N\ge1$ distinct points $x_1,\ldots,x_N$, all integers $m\ge0$ and
\[
k\ge N(m+1)-1,
\]
the canonical evaluation map
\[
H^0(\mathbb P^n,\mathcal O(k))\longrightarrow
\bigoplus_{j=1}^N J_{x_j}^m\mathcal O(k)
\]
is surjective. No analytic interpolation theorem is needed.

For each ordered pair $i\ne j$, choose a homogeneous linear form $\lambda_{ij}$ vanishing at $x_i$ but not at $x_j$, and choose a linear form $L_j$ nonzero at $x_j$. Put
\[
Q_j=\prod_{i\ne j}\lambda_{ij}^{m+1},\qquad
d_0=(N-1)(m+1),\qquad k_0=d_0+m=N(m+1)-1.
\]
The product is empty (and equals $1$) for $N=1$. Then $Q_j$ vanishes to order at least $m+1$ at all $x_i$ with $i\ne j$ and is a unit in the local ring at $x_j$. Since the polynomial sections of $\mathcal O(m)$ realize every local $m$-jet at a single point (homogenize a degree-at-most-$m$ affine Taylor polynomial using $L_j$), choose a homogeneous degree-$m$ polynomial $R_j$ such that the $m$-jet of
\[
\frac{Q_j R_j L_j^{\,k-k_0}}{L_j^{\,k}}
=\left(\frac{Q_j}{L_j^{d_0}}\right)\left(\frac{R_j}{L_j^m}\right)
\]
is the prescribed $j$th jet in the local frame $L_j^k$. This is possible because $Q_j/L_j^{d_0}$ is a unit near $x_j$. The degree-$k$ section
\[
S=\sum_{j=1}^N Q_j R_j L_j^{\,k-k_0}
\]
has precisely all the prescribed jets: every summand except $j=i$ vanishes to order $\ge m+1$ at $x_i$.

For $n=1$ this bound is **optimal for every $N,m$**: the target jet space has dimension $N(m+1)$, whereas $H^0(\mathbb P^1,\mathcal O(k))$ has dimension $k+1$, giving the necessary inequality $k\ge N(m+1)-1$. This proves the exact threshold on the projective line and a uniform sufficient bound in every higher dimension; it **does not assert optimality for $n>1$**. It independently verifies the linear-in-$m+1$ form of Theorem 10.39.1 on its standard projective model, not the general proof relying on weighted $L^2$ estimates.

**Proposed action/dependents:** optional elementary projective-model corollary illustrating explicit interpolation constants and dimension sharpness. Relevant to §10.39.5 very-ampleness, §10.41 point-jet blowups, and §19 section growth. No printed-theorem error.

## POME-GEODESIC-FULL-TIME-LIPSCHITZ-001

**Status/severity:** verified conditional deduction / low.  
**Main anchors:** <code>docs/sections/relative-energy-and-perron-segments--subgeodesics-and-perron-segments/index.html</code>, blob <code>662f60d73fc585b6ea3b710f2a3472bac1de8a7c</code>, Theorem 17.7.8 source <code>foundations-of-pluripotential-theory:108758A0</code>, permanent tag <code>2FECBE87C487</code>, statement physical lines 186–190 and interval replacement proof line 206; Proposition 17.7.9 source <code>foundations-of-pluripotential-theory:470B93BF</code>, tag <code>DD04D189A4D3</code>, clauses (5) and (6) lines 229–236 and proof line 250.

**Deduction.** Assume the printed standing hypotheses: $\theta$ is a smooth closed big real $(1,1)$-form, $\phi$ is a positive-mass model potential, and $u_0,u_1\in\mathcal E(X,\theta,\phi)$ satisfy $|u_1-u_0|\le C$ quasi-everywhere for some $C\ge0$. Write $u_t=G_t(u_0,u_1)$ for the printed weak geodesic. Then for all $s,t\in[0,1]$,
\[
|u_t(x)-u_s(x)|\le C|t-s|
\]
**on the common finite locus**, with the evident endpoint convention. This is stronger than the two fixed-endpoint inequalities printed in Proposition 17.7.9(5).

For $0\le s<t\le1$, the printed endpoint estimate yields $|u_1-u_s|\le C(1-s)$ quasi-everywhere. Theorem 17.7.8 identifies the restricted segment on $[s,1]$ with the weak geodesic between $u_s$ and $u_1$. In the normalized time variable $\tau=(t-s)/(1-s)$, Proposition 17.7.9(5) gives
\[
|u_t-u_s|\le \tau\,C(1-s)=C(t-s).
\]
Interchanging $s$ and $t$ gives the asserted two-sided bound. On the common finite locus the differences are well-defined; no subtraction of two $-\infty$ values is claimed. For $u_1=u_0+C$, the printed affine-translation identity Proposition 17.7.9(6) gives $u_t=u_0+Ct$, so **the constant $C$ is sharp**.

**Dependency boundary:** this is a complete algebraic deduction from the exact printed interval-restriction and endpoint estimates; the underlying full-mass existence, rooftop and geodesic proof chains were *not* transitively verified here. No quantitative energy derivative, ray conclusion, or stronger polar-set assertion is claimed.

**Proposed action/dependents:** optional time-Lipschitz corollary after Proposition 17.7.9. It is relevant to §17.8 energy along weak geodesics, §17.9 long segments and §17.13 test-curve/Legendre constructions, but does not verify those dependents.

## Precise coverage, unresolved items, and exclusions

- **New selected nonexcluded mathematics:** explicit finite-point jet construction testing the statement of §10.39.1, not its analytic proof.
- **Additional selected independent calculations:** §§9.56.1, 9.56.4, 9.56.6 on projective coordinate vertices; §§17.7.8–9 on time reparametrization. §9.56 had earlier partial coverage; §17.7 had earlier partial coverage. Neither section is newly certified in full.
- **Navigation only:** §9.54 <code>docs/sections/entire-function-growth-and-algebraic-zero-sets/index.html</code>, blob <code>ec4e258d279d6ebbfdaa68a903b4907ef0fab372</code>, tag <code>17232821A098</code>; and §10.38 <code>docs/sections/jets-integral-curvature-and-projective-embeddings/index.html</code>, blob <code>dd0421ce051f8f9862dfae4a6e4ab80716c860e8</code>, tag <code>E8563C05DEDF</code>. Both are subject/section-navigation containers, not mathematical proof certifications.
- **Explicitly not reviewed:** §10.39.1's weighted $L^2$ proof; §9.56.3's $L^2$/OT extension; §§15.5–15.6 dedicated Chern-regularization smoothing, plus all Demailly approximation/regularization and dedicated Bergman/L²/OT/multiscale/positivity-loss completion work. Keep all prior records **deferred-by-user**, neither resolved nor certified. Other preexisting open errors and dependencies remain unchanged.
- **Inventory:** retain 25 chapters, 747 distinct numbered ToC sections, and **zero complete-section certifications**. Nothing in this report establishes full theorem-chain verification. No tests, builds, CI, formalization checks, main/source/body/registry/permanent-tag edits, or website publication were performed.

All three proposed mathematical additions are **proposals only**, not changes to the integrated reading edition.