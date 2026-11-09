# Classified audit ledger — flat-density logarithmic tails (2026-11-09)

**Stable finding ID:** POME-DEGENMA-FLAT-DENSITY-LOGTAIL-001  
**Classification:** low / **verified conditional deduction**. Not a false printed theorem, not a confirmed proof gap, not a complete replacement of its PDE existence proof.  
**Production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Destination:** review/mathematical-audit.

## Precise source anchors

Theorem 14.27.1: source **non-kahler-pluripotential-theory:FBA8D992**, permanent **E16A6F31A061**, physical line 11, integrated file **docs/sections/uniqueness-for-degenerate-equations--nonuniqueness-with-a-zero-set-of-empty-interior/index.html**, blob **3cd83bbb6ab246cda0adae1789d7374d815529a6**. Fixed density Eq. 14.27.2: source **non-kahler-pluripotential-theory:72DF4377**, permanent **42198F5D282A**, physical lines 18–49. Lemma 14.27.3: source **non-kahler-pluripotential-theory:DF551C7A**, permanent **C96C68E6BB33**, lines 51–118; Lemma 14.27.7: source **non-kahler-pluripotential-theory:B92AD5B5**, permanent **31CA87ECD1DF**, lines 125–179.

The determinant input is Equation 14.26.4 (source **non-kahler-pluripotential-theory:7BBBEE11**, permanent **71DFC7D0861C**) in **docs/sections/uniqueness-for-degenerate-equations--smooth-nonuniqueness-for-a-degenerate-density/index.html**, blob **7240d97e9192c70acf09f755ec90a5420bc11ef7**. Comparison only: Equation 14.29.16, source **non-kahler-pluripotential-theory:5D15E8A7**, permanent **C72BCF7334A2**, lines 199–206 of **docs/sections/uniqueness-for-degenerate-equations--a-real-analytic-density/index.html**, blob **2f00a81edc49855971bb3a6d774603ee5bbf40db**.

[Full proof](../reports/2026-11-09-degenerate-ma-flat-density-logarithmic-sublevels.md) · [Exact coverage](../coverage/2026-11-09-ch14-flat-density-logarithmic-sublevels.md).

## Findings with explicit hypotheses

Take the **specific smooth nonuniqueness model of Section 14.27** on \(\mathbf P^3\), \(r=\log(|A|^2/|B|^2)\), \(p=C\exp[-1/(1-r^2)]\) on \((-1,1)\), \(q=p'\), parameter \(0<s<1\), and \(g\omega_X^3=(\omega_0+sH)^3\). Write \(\delta=1-|r|\) tending to zero **from inside** \((-1,1)\) and \(S=\sigma'(\pm1)=e/(1+e)^2\). The rank-one determinant formula and printed endpoint coefficients yield the exact asymptotic
\[
\boxed{g(r)\sim\frac{(1-s^2)C^2e^{-1/2}}{2S^2}\delta^{-2}e^{-1/\delta}.}
\]
As a consequence **all inverse positive powers** \(g^{-\alpha}\), \(\alpha>0\), fail to belong to \(L^1(X,\omega_X^3)\), despite the zero set consisting of two measure-zero real hypersurfaces. For normalized Fubini–Study volume \(\nu\), the exact pushforward \(d\nu_r=6\sigma'(r)^2dr\) gives
\[
\lim_{\lambda\downarrow0}\log(1/\lambda)\,
\nu\{-1<r<1,\ 0<g\le\lambda\}=12S^2.
\]
The same **central-band-only** density has logarithmic moment \(\int[\log^+(1/g)]^\beta d\nu<\infty\) iff \(0<\beta<1\). Outer sides of the zero hypersurfaces depend on a separate flat gluing function in Section 14.26, so NO exact *global* logarithmic tail is claimed. All steps and constants are justified in the linked report.

## Status, downstream and proposed action

This **does not refute Theorem 14.27.1** or Lemmas 14.27.3/7. The existence, positivity, and smooth gluing of the background and continuum of potentials still depend on the upstream printed construction; those whole proof chains are not certified. The prior **POME-DEGENMA-ORDER-QUANT-SEPARATION-001** concerns slopes of distinct solutions, not density sublevels or integrability. The §14.29 analytic example has genuinely different quadratic zeros and \(f_*^{-\alpha}\in L^1\iff\alpha<1/2\). Preserve both results, their hypotheses, source labels, permanent tags and attribution.

**Proposed, not applied:** append an optional Remark after Theorem 14.27.1 or Lemma 14.27.7 stating the one-sided flat-density asymptotic and global inverse-power divergence; if including a quantitative small-sublevel law, explicitly restrict it to the central band. **Potential dependent inference ruled out:** this §14.27 model cannot support any assertion of nonuniqueness *under an integrable inverse-density power*; no actual printed downstream misuse was identified.

**Coverage:** §14.27 new selected determinant/flat-tail/radial-pushforward proof, previously already partially reviewed; §§14.26 and 14.29 context only. **0 first-section visits / 0 full-section certifications; 25 chapters, 747 numbered sections.** Prior classifications unchanged; owner-excluded Demailly regularization, Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale atlas, positivity-loss programmes remain **deferred-by-user**, not solved. No production/source, registry, permanent tags, canonicalization, tests, build, CI, formalization or website edits.
