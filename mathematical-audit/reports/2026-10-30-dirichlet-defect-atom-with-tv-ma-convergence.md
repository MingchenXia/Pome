# A concentrated Dirichlet defect despite total-variation convergence of smooth Monge–Ampère measures

**Audit date:** 2026-10-30.  
**Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Write scope:** audit Markdown only on `review/mathematical-audit`.  
**Stable ID:** `POME-ENERGY-DIRICHLET-DEFECT-ATOM-001`.  
**Severity / status:** **low / verified conditional deduction**. **Not** a false theorem, repaired proof, or certification of an entire section.

## Exact integrated source and what was read

- `docs/sections/relative-energy-and-perron-segments--continuity-and-compactness/index.html`, production blob `6fd38d5ff9d0037e9d0d347814a95ad97331715f`, **Example 17.4.11**, permanent tag `27DF9596E862`, original source `foundations-of-pluripotential-theory:68158160`, physical lines **226–241** (especially lines 227–240). The example proves scalar Dirichlet-energy noncontinuity under `L^1` convergence.
- Same file, **Proposition 17.4.4**, tag `2FF0E77E9188`, lines **95–114**: only upper semicontinuity of the relative energy is asserted. Its statement is consistent with this calculation; its complete upstream dependencies were not certified.
- `docs/sections/relative-energy-and-perron-segments--relative-monge-ampere-energy/index.html`, Example **17.3.16**, tag `6EAA0093766C` (curve energy/Stokes normalization), checked as a conditional internal comparison.
- `docs/sections/conventions/index.html`, section **1.1**, permanent tag `DE921263`, source label `foundations-of-pluripotential-theory:DE921263`, production blob `ef778e54d8d7413242387e95c52269b3c7d42cae`, physical **line 47**, `dd^c=(i/2π)∂\bar∂`. This is the first direct *selected* §1.1 convention check, **not** full coverage of §1.1.

## Exact new measure-level deduction

Let \(\omega=dd^c\log(1+|z|^2)\) be the mass-one Fubini–Study form on \(X=\mathbf P^1\), and let \(a\downarrow0\). Choose \(0<\varepsilon_a<1/2\) such that
\[
  a^2\log(1/\varepsilon_a)\longrightarrow\Lambda\in[0,\infty).
\]
Define the globally smooth potentials and positive forms
\[
 u_a(z)=a\log\frac{|z|^2+\varepsilon_a}{1+|z|^2},\qquad
 \mu_a=\omega+dd^c u_a,\qquad
 \eta_a=du_a\wedge d^c u_a.
\]
Then **all** the following hold:

1. \(\mu_a\) is a smooth strictly positive probability \((1,1)\)-form; \(u_a\to0\) in \(L^1(X)\).
2. The Monge–Ampère probabilities **converge in total variation**:
   \[
      \|\mu_a-\omega\|_{\mathrm{TV},*}\le 2a\longrightarrow0.
   \]
   Here \(\|\sigma\|_{\mathrm{TV},*}=\sup_{|f|\le1}|\int f\,d\sigma|\), not half that norm.
3. The positive **gradient-energy measures instead concentrate**:
   \[
      \boxed{\eta_a\rightharpoonup\Lambda\,\delta_{[1:0]}}
      \quad\text{narrowly on }\mathbf P^1,
   \]
   where \([1:0]\) denotes \(z=0\) in the chosen affine chart (or simply the point \(z=0\) if different homogeneous-coordinate naming conventions are used). More precisely,
   \[
       \eta_a(X)=a^2\big(\log(1/\varepsilon_a)+O(1)\big)\to\Lambda,
       \qquad
       \eta_a(X\setminus\{|z|<\rho\})=O_\rho(a^2)
   \]
   for every fixed \(0<\rho<1\). The \(O(1)\) bound is uniform in \(a,\varepsilon_a\).
4. If \(\Lambda>0\), the convergence in (3) **cannot** be strengthened to total variation: each \(\eta_a\) is atomless, and
   \[
       \|\eta_a-\Lambda\delta_0\|_{\mathrm{TV},*}
         =\eta_a(X)+\Lambda\longrightarrow2\Lambda.
   \]
5. For the concrete choice \(\varepsilon_a=\exp(-\Lambda/a^2)\), \(\Lambda>0\), the scalar energy formula (already known in the audit) gives \(E_\omega(u_a)\to-\Lambda/2\). The **new** result is the complete measure-level localization (3) together with the strong measure convergence in (2), **not** a repetition of this scalar defect.

The same calculation shows that if \(a^2\log(1/\varepsilon_a)\to\infty\), then \(\eta_a\) has diverging mass in **every** fixed neighborhood of \(z=0\), even though \(\mu_a\to\omega\) in total variation. This is a limit variant, not another independent finding.

### Proof: curvature, total variation, and \(L^1\)

Write
\[
   \omega_\varepsilon=dd^c\log(|z|^2+\varepsilon).
\]
It extends to a smooth positive form on \(\mathbf P^1\): near \(w=1/z=0\), its local potential is \(\log(1+\varepsilon|w|^2)\). Its integral is exactly one (equivalently, it represents \(c_1(\mathcal O(1))\)). Hence
\[
   \mu_a=(1-a)\omega+a\omega_{\varepsilon_a}\ge(1-a)\omega>0,
   \qquad
   \|\mu_a-\omega\|_{\mathrm{TV},*}
     =a\|\omega_{\varepsilon_a}-\omega\|_{\mathrm{TV},*}\le2a.
\]
The global smoothness of \(u_a\) at infinity follows in the \(w\)-chart from
\(u_a=a\log[(1+\varepsilon_a|w|^2)/(1+|w|^2)]\). On \(\mathbf C\) one has
\[
     a\log\frac{|z|^2}{1+|z|^2}\le u_a(z)\le0.
\]
The left-hand side is \(a\) times an integrable function independent of \(\varepsilon_a\), proving \(L^1\) convergence.

### Proof: exact radial density and atomic concentration

For \(z\ne0,\infty\), set \(s=\log|z|^2\) and
\[
   H_\varepsilon(s)=\frac{e^s}{e^s+\varepsilon}
                    -\frac{e^s}{1+e^s}.
\]
Then \(0\le H_\varepsilon\le1\), \(\partial u_a=aH_{\varepsilon_a}(s)\,dz/z\), and under the printed \(dd^c\) convention,
\[
    \boxed{\displaystyle
    \eta_a=\frac{a^2}{2\pi}H_{\varepsilon_a}(s)^2\,ds\,d\vartheta,
    \qquad z=e^{s/2+i\vartheta}.}
\]
Thus \(\eta_a(X)=a^2\int_{\mathbf R}H_{\varepsilon_a}(s)^2ds\). On \([\log\varepsilon,0]\),
\[
  1-H_\varepsilon(s)
     =\frac{\varepsilon}{e^s+\varepsilon}
       +\frac{e^s}{1+e^s}
     \le \varepsilon e^{-s}+e^s,
  \quad
  0\le1-H_\varepsilon^2\le2(1-H_\varepsilon).
\]
The integral of the last bound is at most \(4\). For \(s<\log\varepsilon\), \(H_\varepsilon(s)\le e^s/\varepsilon\); for \(s>0\), \(H_\varepsilon(s)\le e^{-s}\). Each squared tail integral is at most \(1/2\). Consequently
\[
     \left|\int_{-\infty}^{\infty}H_\varepsilon(s)^2\,ds
                 -\log(1/\varepsilon)\right|\le5
     \qquad(0<\varepsilon<1/2).
\]
Fix \(0<\rho<1\). On \(s\ge2\log\rho\) we bound \(H_\varepsilon^2\le1\) until \(s=0\), then use \(H_\varepsilon^2\le e^{-2s}\). Therefore
\[
  0\le\eta_a\big(X\setminus\{|z|<\rho\}\big)
       \le a^2\big(2\log(1/\rho)+1/2\big)\to0.
\]
Since the total masses tend to \(\Lambda\), testing against any continuous function and splitting at \(\{|z|<\rho\}\) gives narrow convergence to \(\Lambda\delta_0\). For \(\Lambda>0\), smoothness makes \(\eta_a\perp\delta_0\), yielding the exact total-variation formula in (4). If the total masses instead diverge, the off-disc bound shows that the mass inside any fixed neighborhood diverges.

## Status, nonduplication, proposed use, and dependencies

**Printed Example 17.4.11 and Proposition 17.4.4 are mathematically consistent.** This finding is a **verified conditional deduction** obtained by direct calculation; it does not repair a false statement, supply missing external elliptic inputs, or certify a full energy/compactness theorem. There is **no new proof gap** established.

The earlier **`POME-ENERGY-L1-SHARP-001`** (2026-10-22) already establishes scalar energy defects for similar smooth \(\mathbf P^1\) potentials and is preserved unchanged. The contribution here is the **narrow atomic limit of the positive Dirichlet-energy measures while the smooth Monge–Ampère probabilities converge in total variation**, including the exact uniform localization and TV obstruction. An optional non-destructive editorial example after Example 17.4.11 could emphasize this difference. This matters when applying §17.4 semicontinuity or §17.5 variational compactness: small error in the Monge–Ampère measure does not by itself control the distribution of gradient energy, unless extra estimates are imposed.

**Actual new coverage:** selected mathematical check of the explicit §17.4.11 radial model and §1.1 normalization; §17.3.16 and §17.4.4 only for precise conditional context. Independently inspected `docs/sections/differential-operators-and-elliptic-regularity/index.html`, blob `1d365c77d3f0306ab0fac8e87c65c2f5781d32aa`, section **2.15**, tag `73E021597E92`: the present page is **navigation-only**, without a proof or statement. This is structural inventory, not proof verification. **25 current chapters, 747 distinct numbered sections, no completely certified mathematical section.**

**Scope boundary:** Demailly approximation/regularization and its dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remain **deferred-by-user**, neither reaudited nor certified. No source manuscripts, mathematics body, registry, permanent tags, production main, website, build, CI or formalization were changed; no project tests or builds were run.
