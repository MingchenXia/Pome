# 2026-10-31 — sharp central-binomial cofactor comparison; independent nonexcluded cross-chapter checks

- **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Audit-only branch:** `review/mathematical-audit`; starting HEAD `666f7f2dd15dfa005bbc63444d43743f8d9dc7a8`.
- **Finding:** `POME-MA-COFACTOR-SHARP-CENTRAL-BINOMIAL-001` — **low / verified conditional deduction**. The printed formula is **correct but nonoptimal**. There is no false theorem or identified missing proof at this locus.
- **Coverage discipline:** selected algebraic/cofactor step in §§14.20–14.21, selected analytic-germ proof §9.5.6, and the smooth/polarization portion of §11.1.7. No full section or upstream PDE theorem is mathematically certified. No Demailly approximation, regularization, dedicated Bergman, L², Ohsawa–Takegoshi, multiscale atlas or positivity-loss programme was studied.

## Pinned integrated statements and provenance

1. `docs/sections/uniqueness-for-degenerate-equations/index.html`, **blob** `0c1c033d7a1a76b9ccf9fbd5b4bfc8321a33f208`, physical line **18**: Equation **14.20.1**, source `non-kahler-pluripotential-theory:AA4FA8E3`, permanent tag **`2EA7CA32AE91`**. The polarization is \(\mathrm{dd}^c(u-v)\wedge T=A^n-B^n\), where \(T=\sum_{j=0}^{n-1}A^j\wedge B^{n-1-j}\).
2. `docs/sections/uniqueness-for-degenerate-equations--extrema-and-density-sublevels/index.html`, **blob** `044f55457f10b2f640052854a7f5f14b8403be82`: Theorem **14.21.3**, source `non-kahler-pluripotential-theory:61B8DD0F`, tag **`6EB399397505`**, lines **28–50**, proof **133–169**; the measurable strong maximum principle **14.21.6**, source `:E67FD2CF`, tag **`96D40C4808C2`**, lines **79–102**; Equation **14.21.8**, source `:BDBE4297`, tag **`144125DEDD1C`**, line **117**; Equation **14.21.9**, source `:A73BA233`, tag **`CEEE110C45FE`**, line **124**. Equation 14.21.8 prints \(2^{-(n-1)}H^{n-1}\le T\le H^{n-1}\), in the order of positive \((n-1,n-1)\)-forms, \(H=A+B\).
3. `docs/sections/complex-spaces-and-modifications--analytic-curves-and-finite-maps/index.html`, blob `2c725646172203283ac4564bddd46213d9a75cbe`: Lemma **9.5.5**, source `foundations-of-pluripotential-theory:CB1EA559`, tag `776A532CD79E`, lines **84–101**; Proposition **9.5.6**, source `:441B06F2`, tag `0E64BF4DC7C7`, lines **104–124**. The proper finite-map surjectivity and codimension-one zero-set argument were checked only in their stated pure-dimensional / nonzerodivisor setting.
4. `docs/sections/torsion-and-the-variation-of-mass/index.html`, blob `9abec9685e33a1b40f9c0765381408eb52b325d3`: Theorem **11.1.7 (Chiose)**, source `non-kahler-pluripotential-theory:5CD99CBA`, tag `FB90FC741F25`, lines **100–135**. Checked only the smooth mass-polynomial polarization and the \(dd^c(\omega^q)\) algebra. Its bounded-potential extension invokes §5.32.1, which lies in the user-excluded programme: **dependency recorded; not audited or certified**.

## Exact theorem and proof

**Claim (sharp semipositive cofactor sandwich).** Let \(n\ge 1\), \(k=n-1\), and let \(A,B\) be arbitrary semipositive real \((1,1)\)-forms on an \(n\)-dimensional complex vector space. Write \(H=A+B\) and
\[
  T=\sum_{j=0}^{k}A^j\wedge B^{k-j},\qquad
  C_k=\binom{k}{\lfloor k/2\rfloor},\quad C_0=1.
\]
Then, as positive \((k,k)\)-forms,
\[
\boxed{\quad C_k^{-1}H^k\ \le\ T\ \le\ H^k.\quad} \tag{*}
\]
**Both universal constants are optimal, even on the class \(A^n=B^n=0\).** Also,
\[
\boxed{\quad T=(k+1)\int_0^1 \bigl(tA+(1-t)B\bigr)^k\,dt.\quad} \tag{**}
\]
All inequalities are pointwise and require no smoothness or closedness of the forms.

**Proof of the inequalities.** Every mixed wedge \(A^j\wedge B^{k-j}\) is a positive \((k,k)\)-form. The binomial identity reads
\[
H^k=\sum_{j=0}^{k}\binom{k}{j}A^j\wedge B^{k-j}.
\]
The integer coefficients obey \(1\le\binom{k}{j}\le C_k\). Subtracting \(T\) from \(H^k\), and \(H^k\) from \(C_kT\), leaves nonnegative linear combinations of positive forms. This gives (*), including the case \(k=0\).

**Optimal lower coefficient.** Fix \(j=\lfloor k/2\rfloor\). In \(\mathbb C^n\), set \(\alpha_i=\frac{\mathrm i}{2\pi}dz_i\wedge d\bar z_i\), \(A=\alpha_1+\cdots+\alpha_j\), \(B=\alpha_{j+1}+\cdots+\alpha_k\) (empty sums are zero). Then \(A^n=B^n=0\). All \(A^\ell B^{k-\ell}\) vanish except \(\ell=j\), while the survivor is \(j!(k-j)!\alpha_1\wedge\cdots\wedge\alpha_k\neq0\). Therefore \(H^k=\binom kj T=C_kT\). No larger coefficient in front of \(H^k\) can be bounded by \(T\) universally, even subject to equal zero top determinants.

**Optimal upper coefficient.** Take \(A=0\) and \(B=\alpha_1+\cdots+\alpha_k\), with the remaining coordinate unused. Then \(A^n=B^n=0\), \(T=B^k=H^k\neq0\) when \(k>0\). The \(k=0\) case has \(T=H^0=1\). Hence no upper coefficient smaller than 1 works.

**Integral formula.** Expand the integrand:
\[
(k+1)\int_0^1\binom kj t^j(1-t)^{k-j}\,dt
=(k+1)\binom kj\frac{j!(k-j)!}{(k+1)!}=1.
\]
Each mixed wedge has coefficient one after integration, giving (**). The identity is valid for arbitrary commuting even-degree differential forms, and hence for positive \((1,1)\)-forms. \(\square\)

**Concrete dimensional comparison.** In complex dimensions \(n=2,3,4,5\), the optimal lower coefficients are \(1,\,1/2,\,1/3,\,1/6\) respectively. The printed coefficients are \(1/2,\,1/4,\,1/8,\,1/16\). Thus the published estimate is valid but can be strengthened without changing assumptions. For \(n=1\), both expressions are the scalar \(1\).

## Downstream consequences and limits

For an auxiliary Hermitian form \(\beta\), if \(H\ge c\beta\) at a point with \(c>0\), then
\[
 T\ge \frac{c^{n-1}}{\binom{n-1}{\lfloor(n-1)/2\rfloor}}\,\beta^{n-1}.
\]
Accordingly, the lower ellipticity constant of the linearized nondivergence-form cofactor \(Q\) in §14.21 (and its subsequent propagation arguments in §§14.21–14.22) can use the **sharp universal** central-binomial factor in place of \(2^{-(n-1)}\). The exact comparison does **not** assert continuity of measurable Hessians, uniqueness without the theorem's topology hypotheses, or a new solution theory for the Monge–Ampère equation.

**Proposed change, not applied:** Replace Eq. 14.21.8's lower constant by the optimal \(C_{n-1}^{-1}\), add the one-line binomial coefficient proof, and optionally give the two rank-deficient equality models. Preserve source/provenance tag `BDBE4297`, permanent tag `144125DEDD1C`, and historical attribution. This would be a separately reviewed source/reader change, never a direct audit-branch mutation of published content.

## Independent cross-chapter selected checks (no new error)

- **§9.5.6:** In the integrated proof, generic linear forms cut the zero set of a nonzerodivisor on every pure-dimensional branch to an isolated germ. Lemma 9.5.5 gives a proper finite surjective map to a small \(d\)-ball, while a hypothetical zero-set dimension \(<d-1\) would force its image in a coordinate hyperplane to have both positive \(\mathcal H^{2d-2}\) measure and measure zero by the preceding dimension/stratification estimates. This selected contradiction is consistent under the printed hypotheses. Upstream analytic stratification and the full finite-map theorem are **conditional internal dependencies**, not independently verified here. This is new selected proof reading, not a full §9.5 certification.
- **§11.1.7:** The smooth implication "mass independent of strictly positive potentials \(\Rightarrow dd^c(\omega^j)=0\)" is supported by polarization of the mass polynomial, arbitrary local Hermitian Hessians realized using cutoff quadratic functions, and separation of coefficients by complementary wedge products. The \(n=2\) case of \(d\omega\wedge d^c\omega=0\) holds by degree. No error was found in these *smooth steps*. The theorem's separate bounded-potential step cites excluded approximation; it remains a conditional/deferred dependency and is not reopened.

## Audit accounting

**New finding:** one **low / verified conditional deduction** with exact sharpness proof. **No newly confirmed false theorem**, no automatic status upgrade for older issues, no reopened deferred proof programme. Selected §14.20.1 and §14.21.8–9 plus cofactor-ellipticity use in §14.21.3; selected §9.5.6 and §11.1.7 smooth steps only. **25 chapters, 747 current numbered ToC sections, zero fully certified sections.** No software tests, project builds, CI, website publication, formal verification or source/registry/tag changes were carried out.