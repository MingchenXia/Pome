# 2026-11-05 — optimal planar Robin/fixed-ball comparison constant

**Finding:** `POME-ROBIN-PLANAR-UPPER-CONSTANT-TWO-001` — **low / verified conditional deduction**. This is a quantitative strengthening, **not a counterexample** to the printed theorem. It is distinct from `POME-CUBE-ROBIN-EXACT-001`, which concerned real cubes and sharpness of the *lower* coefficient.

**Production main actually read:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Integrated reading edition:** `docs/sections/robin-capacity-and-its-quantitative-comparison/index.html`, main blob `525f388094d0efb6b9ef9f8701d8ac459fd22814`. Section conventions and Robin definitions: physical lines **7–13**. Theorem **16.37.3**: lines **79–85**, original proof **87–111** (the needed equilibrium-support assertion is explicitly invoked at **104**). Stable source `klimek-pluripotential-theory:DAE157DD`; permanent Pome tag `27353237EC80`. Only this selected case of that theorem was newly proved; the rest of §16.37 was not re-certified.

## Precise improvement

Work in complex dimension **one** with
\[
 dd^c=\frac{i}{2\pi}\partial\bar\partial,\qquad
 m_1=\frac12,\qquad \mathcal L^+=\{u\in\operatorname{SH}(\mathbb C):
 \log^+|z|-C\leq u(z)\leq\log^+|z|+C\}.
\]
For a nonpolar compact `K` inside the closed Euclidean disk of radius `0<rho<=1`, let `u=V_K^*`, `gamma(K)=limsup_{|z|->infinity}(u(z)-log|z|)`, `c(K)=exp(-gamma(K))`, and `alpha(K)=exp(-sup_{|z|<=1}u(z))`, exactly as defined in the reading edition.

Then
\[
 \boxed{\quad \alpha(K)\le c(K)\le(1+\rho)\alpha(K).\quad} \tag{1}
\]
For each fixed `rho in (0,1]`, the constant `1+rho` is optimal **uniformly over nonpolar compact subsets of the closed disk of radius rho**. In particular, the smallest admissible constant in the printed Theorem 16.37.3 for **n=1**, with no smaller support disk specified, is exactly
\[
 \boxed{C_1^{\mathrm{opt}}=2}. \tag{2}
\]
For a polar compact `K`, both capacities vanish by the theorem's convention, and (1) holds trivially. Nothing here improves the printed multidimensional exponent `1/n` for `n>1`.

## Independent proof of the upper bound (with named internal inputs)

The existing equilibrium-support theorem, explicitly used at line 104 of §16.37, gives that `dd^c u` is supported on `K`. The standard full-growth normalization, also used in that proof, gives `int_C dd^c u = m_1=1/2`. Set
\[
 \nu=2\,dd^c u.
\]
Thus `nu` is a **probability measure supported on K**; the factor two is essential with the project's `dd^c` convention. Distributionally,
\[
 dd^c\log|z-w|=\tfrac12\delta_w.
\]
Consequently, the logarithmic potential
\[
 U_\nu(z)=\int_K\log|z-w|\,d\nu(w)
\]
has `dd^c U_nu=dd^c u`. By Weyl's lemma, `h=u-U_nu` is harmonic on all of `C` in the distributional sense (and hence has its smooth harmonic representative). Because `nu` is compactly supported and has mass one,
\[
 U_\nu(z)=\log|z|+O(1/|z|)\qquad(|z|\to\infty),
\]
with an error uniform in argument. Since `u in L^+`, `h` is bounded outside a compact disk and therefore bounded everywhere. Harmonic Liouville gives `h\equiv A`. Taking the limit at infinity identifies `A=gamma(K)=-log c(K)`:
\[
 \boxed{u(z)=\int_K\log|z-w|\,d\nu(w)-\log c(K).} \tag{3}
\]
This is an equality of the subharmonic representatives, not merely an identity away from the support. In particular, locally bounded `u` rules out any pointwise minus-infinity ambiguity; one can equivalently first read the equality distributionally and then use the upper-semicontinuous representative.

For `|z|<=1` and `w in K`, `|z-w|<=1+rho`. Formula (3) and the fact that `nu` is a probability measure imply
\[
 u(z)\le\log(1+\rho)-\log c(K),
\quad M:=\sup_{|z|\le1}u(z)\le\log\frac{1+\rho}{c(K)}.
\]
Exponentiating `-M` yields `alpha(K)>=c(K)/(1+rho)`, the upper inequality in (1). The lower inequality `alpha(K)<=c(K)` is already proved at lines 90–96 of the original Theorem 16.37.3 by the norm-ball bound `gamma(K)<=M`; it is not claimed as new.

**Input accounting:** This proof uses the established *compact support and total mass* of the planar equilibrium measure. It independently checks the logarithmic normalization, removes the printed proof's unspecified compactness constant in dimension one, and does **not** independently reprove the general equilibrium-support theorem or the full multidimensional comparison. Accordingly its status is **verified conditional deduction**, not full upstream certification.

## Exact sharpness family, including a radius-restricted version

Fix `0<rho<=1`. For `0<r<rho` let
\[
 K_r=\{z\in\mathbb C:|z-(\rho-r)|\le r\}.
\]
This is a closed disk contained in `\overline B(0,rho)`. The elementary translated-disk extremal is
\[
 V_{K_r}^*(z)=\log^+\frac{|z-(\rho-r)|}{r}.
\]
Its growth at infinity is `log|z|-log r+o(1)`, while its maximum over the *unit* disk occurs at `z=-1`. Therefore
\[
 c(K_r)=r,\qquad
 \sup_{|z|\le1}V_{K_r}^*(z)=\log\frac{1+\rho-r}{r},
 \qquad
 \alpha(K_r)=\frac{r}{1+\rho-r}.
\]
It follows that
\[
 \frac{c(K_r)}{\alpha(K_r)}=1+\rho-r\longrightarrow1+\rho
 \qquad(r\downarrow0).
\]
Every `K_r` is a **nonpolar** disk of positive capacity. The limit therefore proves the asserted optimality without using polar/degenerate examples or appealing to an unattained endpoint. Taking `rho=1` gives the optimal coefficient two in (2). Centered disks instead have `alpha=c=r`, checking sharpness of the separate lower coefficient one, already treated in the earlier real-cube audit.

## Scope, classification and proposed placement

- **Type:** low / verified conditional deduction, with a complete elementary *model and upper-bound calculation* conditional only on the named equilibrium-support and mass statements. **No printed theorem is false.**
- **Proposed correction/addition:** append a dimension-one quantitative corollary after Theorem 16.37.3: `C_1=2` is best possible; with `K subset closed B(0,rho)`, the sharp factor is `1+rho`. Keep the original theorem, original mathematical attribution, source labels and permanent tags unchanged.
- **Affected dependents:** planar quantitative use of the `alpha/c` comparison, including logarithmic-extremal normalization and capacity estimates. Theorem 16.37.5's general decreasing-compact continuity and Proposition 16.37.8's higher-dimensional exponent are **not** reproved or modified.
- **Coverage:** selected theorem statement, proof, and equilibrium-measure normalization in **§16.37.3** only. §16.37 was previously *partly* reviewed in `POME-CUBE-ROBIN-EXACT-001`; this is genuinely different **upper-constant** work. No full-section certificate; project inventory remains **25 chapters / 747 numbered sections / zero fully mathematically certified sections**.
- **Explicit exclusions:** no Demailly approximation/regularization or dedicated Bergman, weighted-L², Ohsawa–Takegoshi, multiscale-atlas or positivity-loss proof-completion work. Those standing items remain **deferred-by-user**.
- **Checks actually performed:** direct inspection of the current main integrated §16.37 statement and proof, normalization of the logarithmic fundamental solution, distributional harmonic-remainder argument, and exact closed-disk asymptotics. No build, tests, CI, formal verification or website publication; no main/source/registry/tag changes.
