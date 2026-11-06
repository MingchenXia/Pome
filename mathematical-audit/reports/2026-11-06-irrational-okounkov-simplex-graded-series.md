# An irrational Okounkov simplex from a non-finitely generated full-lattice graded section algebra (6 November 2026)

**Finding:** `POME-OKO-IRRATIONAL-GRADED-SIMPLEX-001`  
**Severity/status:** low / **verified conditional deduction** (the specific example is proved directly; the general published results and their external counting input are not certified).  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`, unchanged.  
**Integrated reading page:** `docs/sections/flags-convex-bodies-and-section-growth/index.html`, main blob `83557f0e15275253661fe679c75407e6636d497c`.  
**First selected scope in this run:** §19.9.5 (physical lines 105–133), Proposition 19.9.6 (135–152), Corollary 19.9.7 (160–170), and Theorem 19.9.9 (194–231), with Lemma 19.9.2 and Proposition 19.9.10 as limited context. The cited semigroup result Theorem 19.7.20 was read at `docs/sections/almost-semigroups/index.html`, blob `33898b2963ad0f8b7e30bf414276642f60925b74`, lines 299–319, **as an external counting dependency, not re-proved**.

## Exact stable identifiers

| Current reading object | Source label | Permanent tag | Page physical lines |
| --- | --- | --- | --- |
| §19.9.5, graded section algebra | `non-kahler-pluripotential-theory:B9A34270` | `E9A3FA804369` | 105–133 |
| Proposition 19.9.6, upper volume bound | `non-kahler-pluripotential-theory:A4601CA4` | `E6B4502ECB3B` | 135–152 |
| Corollary 19.9.7, full-lattice count | `non-kahler-pluripotential-theory:8930F62C` | `071721B08FC2` | 160–170 |
| Theorem 19.9.9, intrinsic lattice/period formula | `non-kahler-pluripotential-theory:4EE23942` | `CC2BF9294FA3` | 194–231 |
| Lemma 19.9.2, distinct valuations count sections | `non-kahler-pluripotential-theory:EAA5A841` | `2B103C3B777A` | 29–57 |
| Theorem 19.7.20, Kaveh–Khovanskii | `sgpt:282DA4DD` | `85641516C8CA` | §19.7, 299–319 |

The integrated source variant containing Theorem 19.7.20 identifies `data-gerby-book="sgpt"`, so its exact source label is `sgpt:282DA4DD` and its permanent tag is `85641516C8CA`. Its general counting proof remains an external dependency. No original source texts, private records, or tags were changed.

## Hypotheses and construction

Let \(n\geq1\) and fix an **irrational** real number \(\alpha\in(0,1)\). Put \(X=\mathbb P^n\), \(L=\mathcal O_{\mathbb P^n}(1)\), and choose the standard smooth complete coordinate flag at \(p=[1:0:\cdots:0]\); in affine coordinates \(z_i=Z_i/Z_0\), its valuation reads the lexicographically least monomial exponent. For every integer \(m\geq0\), define
\[
 W_m=\operatorname{span}_{\mathbb C}
 \bigl\{Z_0^{m-|a|}Z_1^{a_1}\cdots Z_n^{a_n}:
 a\in\mathbb N^n,\quad |a|=\sum_{i=1}^na_i\leq\lfloor\alpha m\rfloor\bigr\}
 \subset H^0(\mathbb P^n,\mathcal O(m)).
\]
In particular, \(W_0=\mathbb C\) and \(W_m\ne0\) for every \(m\), as \(Z_0^m\in W_m\). This is a **multiplicative graded algebra**: if \(|a|\leq\lfloor\alpha m\rfloor\) and \(|b|\leq\lfloor\alpha k\rfloor\), then \(|a+b|\leq\lfloor\alpha(m+k)\rfloor\). Consequently the valuation semigroup, with its degree in the last coordinate, is exactly
\[
 S=\{(a,m)\in\mathbb N^n\times\mathbb N:\ |a|\leq\lfloor\alpha m\rfloor\}.
 \tag{1}
\]
Indeed each monomial has valuation \(a\), and the lexicographically smallest monomial of any nonzero section in \(W_m\) is one of the listed exponents.

## Complete direct checks

**1. The semigroup generates the full lattice.** The group \(G=\langle S\rangle_{\mathbb Z}\) contains \((0,1)\). Choose \(M\) so that \(\lfloor\alpha M\rfloor\geq1\). Then it contains \((e_i,M)\) for every coordinate unit vector \(e_i\). Subtracting \(M(0,1)\) gives \((e_i,0)\), so
\[
 G=\mathbb Z^{n+1},\qquad e=1,\qquad\Lambda=\mathbb Z^n,\qquad d=n.
 \tag{2}
\]
Thus the **full-lattice** assumption of Corollary 19.9.7 is genuinely satisfied, rather than tacitly replaced by finite generation.

**2. The Okounkov body is an irrational simplex.** Define
\[
 \Delta_\alpha=\{x\in\mathbb R_{\geq0}^n:\ \textstyle\sum_i x_i\leq\alpha\}.
 \tag{3}
\]
Every normalized valuation \(a/m\), \(m>0\), lies in \(\Delta_\alpha\). Conversely, for arbitrary \(x\in\Delta_\alpha\), let \(a_i(m)=\lfloor mx_i\rfloor\). Since
\[
 \sum_i\lfloor mx_i\rfloor\leq
 \left\lfloor m\sum_i x_i\right\rfloor
 \leq\lfloor\alpha m\rfloor,
\]
the vectors \(a(m)/m\) belong to \(m^{-1}S_m\) and converge to \(x\). Consequently the *closure of normalized valuations itself*, even without convexification, is \(\Delta_\alpha\). The intrinsic and Euclidean volumes coincide by (2):
\[
 \operatorname{vol}_{\Lambda}(\Delta_\alpha)
 =\operatorname{vol}_{\mathbb R^n}(\Delta_\alpha)
 =\frac{\alpha^n}{n!}.
 \tag{4}
\]

**3. Exact dimensions and growth.** Counting weak compositions of size at most \(N_m=\lfloor\alpha m\rfloor\) into \(n\) parts gives
\[
 \dim W_m=\binom{N_m+n}{n}
 =\frac{\alpha^n}{n!}\,m^n+O_{n,\alpha}(m^{n-1})
 \qquad(m\to\infty).
 \tag{5}
\]
Therefore
\[
 \lim_{m\to\infty}\frac{\dim W_m}{m^n}
 =\frac{\alpha^n}{n!}
 =\operatorname{vol}_{\Lambda}(\Delta_\alpha).
 \tag{6}
\]
This *direct* binomial computation verifies equality in Proposition 19.9.6 and the stated limit of Corollary 19.9.7 and Theorem 19.9.9 **for this concrete example**, without invoking Kaveh–Khovanskii or any approximation/regularization theorem.

**4. The graded algebra is not finitely generated.** Suppose that finitely many homogeneous elements generate it. For each nonconstant homogeneous generator \(f_j\in W_{m_j}\), its largest affine total monomial degree satisfies \(\deg_z f_j\leq\lfloor\alpha m_j\rfloor<\alpha m_j\), where the strict inequality follows from irrationality of \(\alpha\). Set \(\beta=\max_j\deg_z(f_j)/m_j<\alpha\); degree-zero constants do not affect \(\beta\). Products of generators of total line-bundle degree \(m\) have affine polynomial degree at most \(\beta m\), and the same bound holds for finite sums. But \(W_m\) contains the monomial with \(|a|=\lfloor\alpha m\rfloor\), for which \(\lfloor\alpha m\rfloor/m\to\alpha>\beta\); contradiction. If an algebra is finitely generated by nonhomogeneous elements, their finitely many homogeneous components also generate it, so this covers that case.

In particular, the limiting facet \(\sum_i x_i=\alpha\) of (3) contains **no normalized valuation** at a finite degree \(m\): \(|a|/m\) is rational, while \(\alpha\) is irrational. Its full lattice-volume coefficient nevertheless arises exactly in (6). Finite generation, eventual stabilization of the outer facet, and attainment of the endpoint are *not* premises of the printed counting conclusions.

**5. Section-ratio field.** With the same \(M\) as above, \(Z_0^M\) and \(Z_iZ_0^{M-1}\) both belong to \(W_M\). Their ratios generate \(\mathbb C(z_1,\ldots,z_n)\), while all section ratios are rational functions on \(\mathbb P^n\). Hence \(K(W_\bullet)=\mathbb C(z_1,\ldots,z_n)\) and its transcendence degree is exactly \(n=d\), as expected from Proposition 19.9.10. This also checks that no hidden loss of growth dimension occurs for irrational/non-Noetherian data.

## Classification, correction, dependencies

- **Classification:** low / **verified conditional deduction**. Original Proposition 19.9.6, Corollary 19.9.7, Theorem 19.9.9 and Proposition 19.9.10 remain **correct in this tested model**; no false theorem or gap is asserted. The new fully calculated example checks a genuinely *non-finitely generated*, *full lattice* algebra with an irrational supporting facet. It is mathematically distinct from the earlier **period-two/even-valuation** example (`POME-OKO-PERIOD-LATTICE-NORMALIZATION-001`), which addresses lattice index and period.
- **No production correction needed.** Optional explanatory addition to the reading edition: mention (1)–(6) after §19.9.8 to show that finite generation/rational polyhedrality is unnecessary and that endpoint normalized valuations need not exist.
- **Affected dependents (conditional only):** Theorem 19.9.16 (intrinsic growth via a point blowup), Proposition 19.9.10 (ratio fields), Theorem 19.9.13 (full-dimensional-body contrapositive) and subsequent section-growth applications inherit the distinction between finite-generation arguments and semigroup-volume arguments. No complete dependent proof was rechecked.
- **Outstanding genuine external input:** Theorem 19.7.20 cites Kaveh–Khovanskii, and the general asymptotic semigroup counting result still requires independent internal proof or precise external-dependency classification. One explicit example does **not** resolve that dependency.
- **Excluded scope:** No Demailly approximation/regularization, Bergman, weighted \(L^2\), Ohsawa–Takegoshi, multiscale or positivity-loss proof-completion programme was opened. Existing corresponding notes remain **deferred-by-user**.
- **Audit boundary:** No whole section, all 747 sections, tests/build/CI, source contents, permanent tags or website is certified by this calculation.
