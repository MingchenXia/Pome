# Mathematical audit — 2026-10-29: lower-semicontinuous Bedford–Taylor densities and divergent weak circle energies

**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
**Starting audit branch:** \`7f56dc9b075c505d2ada70d5bcbc35e1c0725795\`.
**Scope:** selected integrated proof/statement passages in §§7.8.1–4, 7.8.6–8, 4.1.1–7, with a consistency check of the precise locality and compact-cutoff steps in §§7.6.1–2. This is **not** a whole-section or upstream proof-chain certification. All user-excluded Demailly approximation/regularization and its dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof programme remain **deferred-by-user**, not resolved. The work below contains no such programme.

## Findings at a glance

| Stable ID | Severity / status | Printed result | Requested disposition |
| --- | --- | --- | --- |
| **POME-BT-LSC-VISCOSITY-EXTENSION-001** | low / **verified conditional deduction** | Proposition 7.8.3 remains correct | Optional separate proof expansion: extend the continuous-density equivalence to any nonnegative locally integrable **lower-semicontinuous** density. Do not replace it with a statement for arbitrary Borel pointwise representatives; the point-spike counterexample below shows that would be false. |
| **POME-CLASS-CIRCLE-WEAK-ENERGY-DIVERGENCE-001** | low / **verified conditional deduction** | Theorem 4.1.7 remains correct | Optional sharpness example: weak convergence of even atomless finite-energy probabilities on a fixed smooth circle does **not** imply bounded energies. Retain only the lower-semicontinuity needed in the existing equilibrium-measure existence proof. |

Neither finding is a false printed theorem, a closed historical error, a completed proof of a conditional upstream input, or a genuine duplication.

## 1. POME-BT-LSC-VISCOSITY-EXTENSION-001

**Integrated anchor:** \`docs/sections/bedford-taylor-products-and-local-capacity--density-lower-bounds-and-mixed-products/index.html\`, **main blob** \`0284d93a0ac26e28746e95afda5e6875f9feaba3\`, physical lines **114–181**, especially original Proposition 7.8.3 at 114–129, the upper-test/comparison argument at 133–156, distributional and convolution arguments at 158–178. **Source identifier:** \`foundations-of-pluripotential-theory:183E5B3C\`; **permanent Pome tag:** \`EB2AFC8FB17C\`. Supporting original Lemmas 7.8.1–2: source \`2844C025\` / tag \`BB19C89586B1\` (lines 22–63) and source \`2D6E0212\` / tag \`1BE242B641AA\` (lines 65–97). Mixed-corollary dependencies: 7.8.4 \`EADDEAF9FAD9\`, 7.8.6 \`91F43DBA51F0\`, 7.8.8 \`142C8110B540\`.

**Exact extension.** Let \(\Omega\subset\mathbb C^n\) be open, \(u\in\operatorname{PSH}(\Omega)\cap L^\infty_{\mathrm{loc}}(\Omega)\), and let \(f:\Omega\to[0,\infty)\) be finite, lower semicontinuous and locally integrable. Put \(\eta=\mathrm{dd}^{\mathrm c}|z|^2\), \(\mathcal H(q)=(q_{j\bar k})\), and \(L_Bq=\operatorname{tr}(B\mathcal H(q))\), \(B>0\), \(\det B=1\). Then the following are equivalent:

1. \((\mathrm{dd}^{\mathrm c}u)^n\ge f\,\eta^n\) as measures;
2. every \(C^2\) upper test \(q\) for \(u\) at every \(x\in\Omega\) satisfies \(\det\mathcal H(q)(x)\ge f(x)\);
3. \(L_Bu\ge n f^{1/n}\) distributionally for every \(B>0\) with \(\det B=1\).

Moreover, for every standard nonnegative compactly supported convolution kernel \(\rho_\varepsilon\), the conclusion of Proposition 7.8.3 remains valid:
\[
  \det\mathcal H(u*\rho_\varepsilon)
    \ \ge\ (f^{1/n}*\rho_\varepsilon)^n\quad\text{on }\Omega_\varepsilon .
\]
Here the final inequality is only at those interior points where the convolution is defined; it is *not* a claim that the density itself is continuous.

**Proof (reduction to the actual integrated continuous-density theorem).** For integers \(j\ge1\), set
\[
  f_j(x):=\inf_{y\in\Omega}\{f(y)+j|x-y|\}.
\]
Nonnegativity and finiteness of \(f\) give \(0\le f_j(x)\le f(x)\). Each \(f_j\) is \(j\)-Lipschitz, and \(f_j\uparrow f\) pointwise: if \(y_j\) almost minimizes the infimum then
\(j|x-y_j|\le f(x)+1\), hence \(y_j\to x\), and lower semicontinuity forces
\(f(x)\le\liminf f(y_j)\le\liminf(f_j(x)+j^{-1})\).
For each \(j\), *the printed* Proposition 7.8.3 applies to the continuous \(f_j\).

From (1), its measure inequality for each \(f_j\) gives (2) and (3) for \(f_j\); let \(j\uparrow\infty\). In (3), monotone convergence is justified since \(f^{1/n}\in L^1_{\mathrm{loc}}\). Conversely, (2) or (3) for \(f\) implies the corresponding assertion for every \(f_j\), and the printed proposition gives \((\mathrm{dd}^{\mathrm c}u)^n\ge f_j\eta^n\); monotone convergence against nonnegative compact tests gives (1). Finally the printed convolution inequality for every \(f_j\), followed by monotone convergence of \(f_j^{1/n}*\rho_\varepsilon\), gives the asserted mollification inequality. Nothing requires a decreasing approximation of psh singularities or any user-excluded programme.

**Pointwise representative obstruction, independent of all PDE estimates.** On any nonempty domain choose \(x_0\), let \(u\equiv0\), and let \(f=\mathbf1_{\{x_0\}}\). This \(f\) is bounded, Borel, and even **upper semicontinuous**, but not lower semicontinuous. Both the measure inequality (1) and every distributional inequality (3) hold because \(f=0\) almost everywhere. The constant upper test \(q=0\) at \(x_0\) has \(\det\mathcal H(q)=0<f(x_0)=1\), so (2) fails. Thus a theorem with unrestricted Borel/USC **pointwise** \(f\) would be false; the printed continuous version is correct, and the proved lsc version is a genuine extension.

**Dependencies/affected results.** Uses Proposition 7.8.3 and its conditional internal Bedford–Taylor comparison, test/distribution, and decreasing-continuity inputs. It does not reverify those dependencies. The lower-semicontinuous-density extension could optionally be quoted by §§7.8–7.9, §§8.8–8.13 and §14.24 for viscosity versus measure subsolutions; use only after checking any additional hypotheses there. No amendment to source, registry, canonical entries, or permanent tags is made.

## 2. POME-CLASS-CIRCLE-WEAK-ENERGY-DIVERGENCE-001

**Integrated anchor:** \`docs/sections/potentials-energy-and-capacity/index.html\`, **main blob** \`4962a7cd576a64cb47fa0955dcc80cf87c3da9d1\`, physical lines **21–47** (kernel and energy normalization), **187–239** (Theorem 4.1.7 and the proof of existence/uniqueness), especially lines 198–220 (weak convergence and lower-semicontinuity). **Source:** \`foundations-of-pluripotential-theory:A35EEAC5\`; **permanent tag:** \`AA43DD93EFE4\`. The positive-definite finite-energy signed-pairing input is Proposition 4.1.5, source \`DF3A6DB5\`, tag \`09A0D05A868F\`, physical lines 98–184. This calculation is separate from the earlier polar-Cantor weak/TV model finding: *all approximants here are atomless and have individually finite logarithmic energy; their energies diverge*.

**Exact model.** Fix \(R>0\), \(K=\{z\in\mathbb C:|z|=R\}\), and the printed logarithmic scale \(D>2R=\operatorname{diam}K\). Write
\[
  k_D(z,w)=\frac1{2\pi}\log\frac D{|z-w|},
  \qquad I_D(\mu)=\iint_{K^2}k_D(z,w)\,\mathrm d\mu(z)\,\mathrm d\mu(w).
\]
The normalized arclength \(\mu=\frac{\mathrm d\theta}{2\pi}\) on \(K\) has
\[
  V_D(K)=I_D(\mu)=\frac1{2\pi}\log\frac DR,\qquad
  \operatorname{Cap}(K)=D e^{-2\pi V_D(K)}=R.
\]
The equality \(I_D(\mu)=(2\pi)^{-1}\log(D/R)\) follows by integrating
\(\log|e^{i\theta}-e^{i\varphi}|\) in \(\varphi\): its mean is zero. The circle measure is the unique equilibrium measure by rotational invariance and the uniqueness in Theorem 4.1.7 (or directly by the zero-total-mass energy inequality in Proposition 4.1.5).

For each \(N\ge2\), put \(\delta_N=e^{-N^2}\). Around each angle \(2\pi j/N\), \(0\le j<N\), take the uniform *probability* \(\nu_{j,N}\) on the short circle arc
\(|\theta-2\pi j/N|\le\delta_N\), and put
\(\mu_N=N^{-1}\sum_{j=0}^{N-1}\nu_{j,N}\).
Each \(\mu_N\) is **atomless and has finite energy**, because logarithmic diagonal singularities are integrable against bounded arclength densities on these finitely many arcs. For any continuous \(h\) on \(K\),
\[
 \left|\int h\,\mathrm d\mu_N-\frac1N\sum_{j=0}^{N-1}h(Re^{2\pi i j/N})\right|
 \le \omega_h(R\delta_N)\longrightarrow0,
\]
and the equal-spaced sums converge to \(\int h\,\mathrm d\mu\). Thus \(\mu_N\rightharpoonup\mu\) weakly.

However, for \(z,w\) on the same short arc,
\(|z-w|\le2R\delta_N\). The kernel is nonnegative on all \(K^2\) because \(D>2R\), while the total product mass of pairs lying on the same one of the \(N\) arcs is \(N(1/N)^2=1/N\). Consequently
\[
 I_D(\mu_N)\ \ge\
 \frac1{2\pi N}\log\frac{D}{2R\delta_N}
 =\frac{N}{2\pi}+\frac1{2\pi N}\log\frac D{2R}
 \longrightarrow+\infty .
\]
**The quantitative obstruction:** weak convergence of *finite-energy, atomless* probabilities on a fixed compact nonpolar support does not imply an energy upper bound, energy convergence, or convergence in the energy norm. The printed direct-method proof only uses \(I_D(\mu)\le\liminf_j I_D(\mu_j)\) for a sequence already assumed to have bounded energy; that is correct and cannot be strengthened to continuity under arbitrary weak convergence.

**Dependencies/affected results.** The exact equilibrium identification uses Theorem 4.1.7's uniqueness and the explicit logarithmic kernel; existence can alternatively be checked directly. It highlights the topology needed in classical §4.1 equilibrium variational problems and §4.2 balayage, and warns against replacing energy control with weak compactness in §7 capacity or §17 geodesic arguments. This is an optional example, not a proposed correction of a true theorem.

## Coverage and disposition

New direct proof-level examination in the **previously only partly sampled** §4.1 (kernel normalization, Theorem 4.1.7, Proposition 4.1.5 as an input) and renewed selected §7.8 (Lemma 7.8.1/2 and Proposition 7.8.3, with statements of 7.8.4/6/8 and their mixed-discriminant proof paths). The selected §7.6.1 increasing-limit proof was read for quantifier/local collar checks; no new finding or net extension is claimed there. No whole section or whole chapter is certified. The underlying current ToC inventory is **25 chapters / 747 unique numbered sections / zero complete-section certifications**; it has not been redefined by this selected work.

Statuses of all old confirmed errors, proof gaps, external inputs, resolved historical repairs, and deferred-by-user records are unchanged. In particular, the old non-Archimedean concave-tail production error remains unresolved despite its separately verified finite-recursion repair. No test/build/formal verification/CI/website publication/main/source/registry/permanent-tag change was performed.
