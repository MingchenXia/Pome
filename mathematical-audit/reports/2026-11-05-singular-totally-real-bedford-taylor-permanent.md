# Singular totally-real Bedford–Taylor products: sharp permanent coefficient

**Finding ID:** \`POME-BT-SINGULAR-PERMANENT-EQUALITY-001\`. **Severity/status:** low / **verified conditional deduction**. No original theorem is refuted or repaired.
**Date:** 2026-11-05. **Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. 
**Integrated reading edition:** \`docs/sections/bedford-taylor-products-and-local-capacity--mixed-products-for-a-common-measure/index.html\`, blob \`e33955e433d3d863f053dc34ed3ed38b3397671f\`, physical lines **10–20** (Theorem 7.12.1), **23–89** (proof, including common grid, Hölder and localization at **66–89**), **94–110** (Corollary 7.12.6), and **115–125** (Corollary 7.12.8).
**Source labels:** \`foundations-of-pluripotential-theory:046CCCD5\` (Theorem), \`:D5C83406\` (mixed two-factor corollary), \`:02D188DC\` (sum corollary). **Permanent tags:** \`AAD1BC0CC6C4\`, \`0B504335901F\`, \`7071C55A0E4E\`, respectively. Prior §7.12 coverage was partial; this report supplies a *new singular model*, not a repeated proof of the general theorem.

## Exact theorem for a singular common Radon measure

Let \(n\ge2\), let \(\Omega\subset\mathbb C^n\) be an open product of bounded real coordinate intervals centered at the origin, and put \(z_j=x_j+iy_j\). For a strictly positive real matrix \(A=(a_{ij})_{1\le i,j\le n}\), define
\[
 u_i(z)=\sum_{j=1}^n a_{ij}|x_j|,\qquad
 \mu_0=(2\pi)^{-n}\prod_{j=1}^n(\delta_0(x_j)\,dx_j\,dy_j).
\]
Here the second expression is the locally finite positive Radon measure with \((2\pi)^{-n}\) times Lebesgue density in the \(y\)-variables on \(L=\{x_1=\cdots=x_n=0\}\). The potentials \(u_i\) are continuous locally bounded plurisubharmonic functions: \(|x_j|=\max(x_j,-x_j)\) is PSH.

The **ordinary Bedford–Taylor products** obey the exact identities
\[
 (dd^c u_i)^n=n!\left(\prod_j a_{ij}\right)\mu_0,\qquad
 \bigwedge_{i=1}^n dd^c u_i=\operatorname{per}(A)\mu_0,\qquad
 \operatorname{per}(A)=\sum_{\sigma\in S_n}\prod_i a_{i,\sigma(i)}.
\]
Consequently the hypotheses of printed Theorem 7.12.1 hold with the **singular** common measure \(\mu=\mu_0\) and constants \(f_i=n!\prod_j a_{ij}\). Its conclusion reduces *exactly* to
\[
 \operatorname{per}(A)\ \ge\ n!\left(\prod_{i,j}a_{ij}\right)^{1/n}. \tag{*}
\]
The coefficient \(1\) in the printed mixed-product inequality is attained **even for a measure supported on an \(n\)-dimensional totally-real locus**; positivity and local boundedness do not require an ambient Lebesgue density. In the strictly positive matrix class, equality in (*) holds **if and only if \(A\) has rank one**. This equality classification is only for this model; it is *not* a proposed general equality theorem.

## Full distributional computation and legitimate limit

Define \(\phi_\epsilon(x)=\sqrt{x^2+\epsilon^2}\) and
\[
 k_\epsilon(x)=\frac{\phi_\epsilon''(x)}2
 =\frac{\epsilon^2}{2(x^2+\epsilon^2)^{3/2}}.
\]
Then \(k_\epsilon\ge0\), \(\int_{\mathbb R} k_\epsilon\,dx=1\), and \(k_\epsilon(x)\,dx\to\delta_0\) weakly: the mass outside any \((-\eta,\eta)\) tends to zero and the total mass is fixed. Also \(\phi_\epsilon\downarrow|x|\) as \(\epsilon\downarrow0\). Pome's convention \(dd^c=(i/2\pi)\partial\bar\partial\), together with \(i\,dz_j\wedge d\bar z_j=2\,dx_j\wedge dy_j\), gives
\[
 dd^c\phi_\epsilon(x_j)
 =\frac{\phi_\epsilon''(x_j)}{4\pi}\,dx_j\wedge dy_j
 =\frac{k_\epsilon(x_j)}{2\pi}\,dx_j\wedge dy_j
 =:\beta_{j,\epsilon}.
\]
Take the **elementary convex test potentials**
\(u_{i,\epsilon}=\sum_j a_{ij}\phi_\epsilon(x_j)\), which decrease to \(u_i\). Each \(\beta_{j,\epsilon}\) is a positive smooth decomposable coordinate two-form, \(\beta_{j,\epsilon}^2=0\), and all coordinate two-forms commute. Hence direct multilinear expansion yields
\[
 \begin{aligned}
 \bigwedge_i dd^c u_{i,\epsilon}
 &=\left(\sum_{\sigma\in S_n}\prod_i a_{i,\sigma(i)}\right)
      \beta_{1,\epsilon}\wedge\cdots\wedge\beta_{n,\epsilon}\\
 &=\operatorname{per}(A)(2\pi)^{-n}
       \prod_j k_\epsilon(x_j)\,dV_{2n},\\
 (dd^c u_{i,\epsilon})^n
 &=n!\left(\prod_j a_{ij}\right)(2\pi)^{-n}
       \prod_j k_\epsilon(x_j)\,dV_{2n}.
 \end{aligned}
\]
For each compactly supported continuous test function, the product kernels converge to evaluation at \(x=0\) followed by integration in the \(y\) variables. Therefore the last smooth measures converge weakly to the two displayed measures supported on \(L\). **Ordinary Bedford–Taylor decreasing continuity**, the existing Theorem 7.3.7 (source \`foundations-of-pluripotential-theory:8B1F9B78\`, permanent tag \`D87C13B3250A\`), identifies these weak limits with the actual BT measures of \(u_i\); it is an expressly **conditional upstream input**, not re-proved here. The elementary convex one-coordinate calculation is not Demailly approximation and does not touch the excluded Bergman/L²/OT/positivity-loss research programme.

Write \(b_\sigma=\prod_i a_{i,\sigma(i)}>0\). By arithmetic–geometric mean,
\[
 \operatorname{per}(A)=\sum_\sigma b_\sigma
 \ge n!\left(\prod_\sigma b_\sigma\right)^{1/n!}
 =n!\left(\prod_{i,j}a_{ij}\right)^{1/n},
\]
because each \(a_{ij}\) occurs in exactly \((n-1)!\) permutation products. Equality means all \(b_\sigma\) are equal. Comparing permutations differing only by a swap between two rows implies
\(a_{ij}a_{k\ell}=a_{i\ell}a_{kj}\) for every pair of distinct rows and columns. Thus all \(2\times2\) minors vanish, so the strictly positive matrix has rank one. Conversely \(a_{ij}=r_i c_j>0\) makes all permutation products equal. In dimension two, \(A=((1,2),(3,4))\) gives the strict inequality \(10>4\sqrt6\); \(A=((1,2),(3,6))\) attains \(12=12\). These are exact identities; no numerical test suite was run.

## Additional independent sum-inequality check

For positive vectors \(a,b\), let \(u=\sum a_j|x_j|\), \(v=\sum b_j|x_j|\). The same computation gives
\((dd^c(u+v))^n=n!\prod_j(a_j+b_j)\mu_0\). Printed Corollary 7.12.8 becomes
\[
 (\prod_j(a_j+b_j))^{1/n}
 \ge(\prod_j a_j)^{1/n}+(\prod_j b_j)^{1/n}.
\]
Set \(s=(\prod a_j)^{1/n}\), \(t=(\prod b_j)^{1/n}\), \(\alpha=s/(s+t)\). Apply weighted AM–GM to each
\(\frac{a_j+b_j}{s+t}=\alpha\frac{a_j}s+(1-\alpha)\frac{b_j}t\), and multiply over \(j\). Equality holds precisely when \(a_j/s=b_j/t\) for every \(j\), i.e. the positive coefficient vectors are proportional. The printed corollary is correct; this is its sharp **singular-measure** model and exact equality criterion.

## Classification, dependencies, coverage, proposed action

**Low / verified conditional deduction.** The printed Theorem 7.12.1 and Corollaries 7.12.6 and 7.12.8 are **not false**. The model's smooth coefficient computation, weak convergence and permanent/equality calculation are justified above, but BT identification is conditional on §7.3.7. The **general** §7.12 proof's compact-support MA existence, approximation stability and energy prerequisites (§7.11.30, §7.11.38 etc.) remain unverified, as do the general equality cases. There is no claimed new proof of these inputs. Suggested **optional editorial addition** (separate reviewable production patch only): a worked totally-real singular measure example after Corollary 7.12.8, preserving attribution and all tags. No source, body, canonicalization, proof registry, or published page is changed.

**Actual new coverage:** selected §7.12.1 model and 7.12.6/8 specialization, plus direct reading of integrated proof's common-grid coefficient and localization steps at physical **66–89**. §7.3.7 and §7.2.4 were **dependency and normalization context only**, not newly certified. The current ToC has **25 chapters, 747 numbered sections, zero complete mathematical-section certifications**. Previous confirmed errors/proof gaps/external inputs/duplicates/verified repairs unchanged. Excluded Demailly approximation/regularization, dedicated Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss work remains **deferred-by-user**, not resolved or certified.
