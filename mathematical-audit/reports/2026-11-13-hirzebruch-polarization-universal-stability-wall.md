# Exact universal stability chamber for nonsplit Hirzebruch extensions on \(\mathbb F_0\)

**Date:** 2026-11-13 (Asia/Shanghai).  
**Finding:** `POME-HIRZ-POLARIZATION-UNIVERSAL-STABILITY-WALL-001`.  
**Classification:** **low / verified conditional deduction**. The printed Proposition 11.14.1 is **correct**; there is no source error and no claimed repair. This is a new *polarization-variable* assertion, distinct from the previously recorded 2026-11-11 fixed-polarization slope-jump locus `POME-HIRZ-EXT-SLOPE-JUMP-001`.  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Target audit branch:** `review/mathematical-audit` (documentation only).

## Integrated reading-edition anchors and dependencies

- `docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--ample-comparison-quotients-on-hirzebruch-surfaces/index.html`, main blob `6d836a2ed19f76c26311025602fb44a56713e390`: Lemma **11.13.1**, source `non-kahler-pluripotential-theory:9A9AA541`, permanent tag `8FE2AABC7334`, physical lines **26–51**. The conventions \(S^2=-e,\ S\cdot f=1,\ f^2=0\), the effective cone and the line bundles are at **12–34, 53–59**.
- `docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--stable-extensions-approaching-the-split-comparison-bundle/index.html`, main blob `03559e82ef17c97d04258775312d994ec217e376`: Proposition **11.14.1**, source `non-kahler-pluripotential-theory:D386B065`, permanent tag `A195B6162A49`, **25–86**. The original \(P=4S+(12e+3)f\), slopes and exceptional \(e=0\) multiplication argument are at **10–22, 52–85**. Proposition **11.14.3**, source `non-kahler-pluripotential-theory:E4134CA1`, permanent tag `7215288BDF53`, **112–138**, is deformation context only.
- `docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--deforming-to-stable-ample-bundles/index.html`, main blob `08ac54c401030e52cf3001d6ddc146fc35956d54`: Lemma **11.15.3**, source `non-kahler-pluripotential-theory:E3916599`, permanent `EBF7EB73EABE`, **52–83**; Lemma **11.15.4**, source `:CAE7FA8C`, permanent `319641577F72`, **88–113**; Theorem **11.15.5**, source `:88F5B6CB`, permanent `E769519C862E`, **121–130**. These were read to delimit possible downstream applications; their entire dependency chains are **not** certified. In particular, Walter's prioritary-stack irreducibility theorem at line **117** remains an expressly quoted external input, not proved by this report.

## New precise theorem

On \(X=\mathbb F_0=\mathbb P^1\times\mathbb P^1\), let \(S,f\) be the two ruling classes, so \(S^2=f^2=0,\ S\cdot f=1\), and retain the exact bundles
\[
 L_1=\mathcal O_X(5S-f)=\mathcal O(5,-1),\qquad
 L_2=\mathcal O_X(-S+5f)=\mathcal O(-1,5).
\]
Let \(\alpha\ne0\) be any class in
\[
 W=\operatorname{Ext}^1_X(L_2,L_1)
   =H^1(X,\mathcal O(6S-6f)),\quad \dim_\mathbb C W=35,
\]
and let \(0\to L_1\to V_\alpha\to L_2\to0\) be its nonsplit extension. For **every** ample real numerical polarization \(P_{u,v}=uS+vf\), \(u,v>0\), define
\[
 \Delta_{u,v}(V_\alpha)=\mu_{P_{u,v}}(V_\alpha)
 -\sup_{\substack{M\subset V_\alpha\\M\text{ coherent torsion-free}\\\operatorname{rank} M=1}}
       \mu_{P_{u,v}}(M).
\]
Then
\[
 \boxed{
 \inf_{\alpha\in W\setminus\{0\}}\Delta_{u,v}(V_\alpha)
   =\min\{3(u-v),\,3v-2u\}.
 } \tag{1}
\]
Both terms of (1) are **attained by actual rank-one subobjects** in the appropriate extensions; no density or limiting argument is used.

Consequently **every nonsplit extension** \(V_\alpha\) is \(P_{u,v}\)-slope-stable **if and only if**
\[
 \boxed{\qquad \frac23u<v<u.\qquad} \tag{2}
\]
At \(v=2u/3\), all these nonsplit extensions are semistable, and an extension is **not stable** exactly when its class is annihilated by multiplication by a nonzero section of \(\mathcal O_X(f)\). At \(v=u\), all are semistable but none is stable, because \(L_1\) has equal slope. Outside the closed interval \(2u/3\le v\le u\), there exists an unstable nonsplit extension (for \(v>u\), every such extension is unstable).

For the *printed* polarization \(P=4S+3f\), (1) gives \(\inf_\alpha\Delta_P(V_\alpha)=\min(3,1)=1\), consistently with the older **fixed-\(P\)** slope-jump result. Formula (1) and the sharp full chamber (2), **not** the older projectivized jumping-locus dimension, are the new claims in this report.

## Direct proof

**1. Slopes and reduction of torsion-free subobjects.** Since \(L_1\otimes L_2^{-1}=\mathcal O(6,-6)\), Künneth gives
\[
 W=H^0(\mathbb P^1,\mathcal O(6))
      \otimes H^1(\mathbb P^1,\mathcal O(-6))
\]
of dimension \(7\cdot5=35\). The intersection form gives
\[
 \mu(V_\alpha)=2(u+v),\quad
 \mu(L_1)=5v-u,\quad \mu(L_2)=5u-v.
\]
Thus \(\mu(V_\alpha)-\mu(L_1)=3(u-v)\), and \(L_1\subset V_\alpha\) shows that \(\Delta_{u,v}(V_\alpha)\le3(u-v)\) for **every** extension.

A rank-one torsion-free subsheaf \(M\subset V_\alpha\) extends to its line-bundle double dual \(M^{**}\); the map extends across finitely many points by the holomorphic Hartogs theorem in smooth local bundle frames. Since \(c_1(M)=c_1(M^{**})\), replacing \(M\) by \(M^{**}\) preserves its slope. Hence we may test line-bundle injections \(M\hookrightarrow V_\alpha\).

**2. Zero composite to \(L_2\).** If \(M\to V_\alpha\to L_2\) vanishes, \(M\to L_1\) is nonzero. Its zero divisor is effective, so \(\mu(M)\le\mu(L_1)\), or
\[
 \mu(V_\alpha)-\mu(M)\ge3(u-v). \tag{3}
\]

**3. Nonzero composite and the prohibited horizontal divisors.** If \(M\to L_2\) is nonzero, it is multiplication by a section \(s\) with effective divisor \(D=aS+bf\), \(a,b\in\mathbb Z_{\ge0}\), and \(M=L_2(-D)\). If \(D=0\), it splits the nonsplit extension, contradiction. If \(b=0\) and \(a\ge1\), the existence of its lift \(M\to V_\alpha\) would annihilate \(\alpha\) under
\[
 H^1(\mathcal O(6,-6))
 \xrightarrow{\cdot s}
 H^1(\mathcal O(6+a,-6)),
 \qquad s\in H^0(\mathcal O(a,0))\setminus\{0\}.
\]
Künneth identifies this map with multiplication by \(s\) on \(H^0(\mathbb P^1,\mathcal O(6))\), tensored with the identity on \(H^1(\mathbb P^1,\mathcal O(-6))\). It is injective: a nonzero polynomial cannot annihilate a nonzero holomorphic section. Since \(\alpha\ne0\), such a lift cannot exist. Therefore **every** line subobject with nonzero composite has \(b\ge1\), and
\[
 D\cdot P_{u,v}=av+bu\ge u,\quad
 \mu(M)=5u-v-av-bu\le4u-v.
\]
Consequently
\[
 \mu(V_\alpha)-\mu(M)\ge3v-2u. \tag{4}
\]
Equations (3) and (4) prove the lower bound
\(\Delta_{u,v}(V_\alpha)\ge\min\{3(u-v),3v-2u\}\) for **every** nonzero \(\alpha\).

**4. Attaining the second bound with a genuine nonsplit extension.** Choose a nonzero section \(s_f\in H^0(\mathbb P^1,\mathcal O(1))\), regarded as a section of \(\mathcal O_X(f)\). Multiplication induces
\[
 W\simeq H^0(\mathcal O(6))\otimes H^1(\mathcal O(-6))
 \xrightarrow{\operatorname{id}\otimes(\cdot s_f)}
 H^0(\mathcal O(6))\otimes H^1(\mathcal O(-5)).
\]
The second-factor map is surjective with a **one-dimensional kernel**: under Serre duality its transpose is the injective multiplication
\(H^0(\mathbb P^1,\mathcal O(3))\xrightarrow{\cdot s_f}H^0(\mathbb P^1,\mathcal O(4))\).
Thus the map on \(W\) has a **seven-dimensional kernel**. Pick \(0\ne\alpha\) in this kernel. The pullback of its extension along multiplication \(L_2(-f)\xrightarrow{\cdot s_f}L_2\) splits, giving a genuine injection \(L_2(-f)\hookrightarrow V_\alpha\). Its slope is \(4u-v\), so
\(\Delta_{u,v}(V_\alpha)\le3v-2u\). Together with the always-present subbundle \(L_1\), this forces equality in the lower bound for this particular nonsplit \(V_\alpha\), proving (1).

**5. Walls and semistability.** For **all** nonsplit classes, stability holds precisely when the universal lower bound in (1) is positive: this is (2); if either term is nonpositive, the actual subbundle \(L_1\), or the just-constructed special nonsplit class with \(L_2(-f)\), witnesses failure of universal stability. At \(v=2u/3\), (3) is strict and (4) is nonnegative. Equality in (4) requires \(av+bu=u\), hence \(D=f\) (not \(D=aS\), already excluded); the lift exists exactly when the extension class belongs to \(\ker(\cdot s_f)\) for some nonzero \(s_f\). This gives the asserted precise lower-wall classification. At \(v=u\), (3) is equality for \(L_1\), and (4) is strictly positive for the other type, giving semistability but not stability for **every** nonsplit class.

## Audit decision, dependency boundary and suggested action

- **Status/severity:** `verified conditional deduction / low`. There is no false theorem and no missing proof found in the *printed fixed-polarization statement*. The calculation is self-contained once the standard projective-line cohomology, the Künneth isomorphism, Serre duality, Hartogs extension and the effective cone proved/recorded internally in §11.13 are admitted. It does not use the excluded Demailly approximation programme or any \(L^2\)/Bergman/Ohsawa–Takegoshi proof.
- **Suggested optional production patch (not applied):** a short remark after Proposition 11.14.1 stating the universal chamber (2), the minimum formula (1), and the lower-wall multiplication criterion, with the proof above as a reviewable separate change. Preserve the original statement, all permanent tags and the 2026-11-11 fixed-polarization slope-jump result.
- **Downstream:** Lemma 11.15.3 and Theorem 11.15.5 fix the printed polarization and remain correct; the new calculation alone does **not** establish simultaneous ample-stable approximation for every varying polarization. Walter's irreducibility input in §11.15.5 is a separate **external dependency**, not silently discharged here.
- **Coverage:** detailed new \(e=0\) polarization-variable subobject/multiplication argument for Proposition 11.14.1, and a limited hypothesis/proof-step comparison of Lemma 11.15.3–4 and Theorem 11.15.5. Both numbered sections were previously partly sampled: **zero first-visit credits, zero complete-section certifications**. Current unchanged main ToC: **25 chapters / 747 numbered sections**.
- **Deferred:** all dedicated Demailly approximation/regularization, Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof completion remains **deferred-by-user**, neither resolved nor certified. No build, tests, CI, formal verification or publication performed in this audit.
