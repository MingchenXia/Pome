# Flat-density endpoint and logarithmic sublevel law (2026-11-09)

**Stable finding:** POME-DEGENMA-FLAT-DENSITY-LOGTAIL-001  
**Classification:** low / **verified conditional deduction**. This proves a new quantitative consequence of the printed smooth nonuniqueness construction; it **does not** identify an incorrect theorem, prove the whole existence construction, or certify any PDE dependency.  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Audit branch:** review/mathematical-audit.

## Exact reading-edition scope and provenance

- Direct primary source: docs/sections/uniqueness-for-degenerate-equations--nonuniqueness-with-a-zero-set-of-empty-interior/index.html; production blob **3cd83bbb6ab246cda0adae1789d7374d815529a6**. Theorem **14.27.1**, source label **non-kahler-pluripotential-theory:FBA8D992**, permanent tag **E16A6F31A061**, physical line 11 and following. The fixed-bump definition and the equation defining the density occur at **lines 18–49**, especially Equation **14.27.2**, source **non-kahler-pluripotential-theory:72DF4377**, permanent **42198F5D282A**. Lemma **14.27.3** (source **DF551C7A**, permanent **C96C68E6BB33**), its ODE **14.27.4** (source **3605D054**, permanent **FE5D8F02666F**) and one-sided coefficient formulas are at **lines 51–118**; Lemma **14.27.7** (source **B92AD5B5**, permanent **31CA87ECD1DF**) and the flat extension proof are at **lines 125–179**; the completed existence argument and final flat-vanishing observation are at **lines 180–203**. Source-label prefixes in the shorter references here are all non-kahler-pluripotential-theory.
- Direct determinant and background crosscheck: docs/sections/uniqueness-for-degenerate-equations--smooth-nonuniqueness-for-a-degenerate-density/index.html; blob **7240d97e9192c70acf09f755ec90a5420bc11ef7**, Section 14.26.2, Eq. **14.26.4** (source **non-kahler-pluripotential-theory:7BBBEE11**, permanent **71DFC7D0861C**, approximately lines **38–50**) and Eq. **14.26.6** (source **non-kahler-pluripotential-theory:C78CE2C9**, permanent **DE71ED12948B**, approximately lines **58–65**). The normalized Fubini–Study form and radial rank-one coefficients are used exactly as printed.
- Separate nonidentical comparator: docs/sections/uniqueness-for-degenerate-equations--a-real-analytic-density/index.html; blob **2f00a81edc49855971bb3a6d774603ee5bbf40db**, Theorem **14.29.1** (source **non-kahler-pluripotential-theory:3ADFF2BE**, permanent **DD001DBBE659**, line **11**) and Eq. **14.29.16** (source **non-kahler-pluripotential-theory:5D15E8A7**, permanent **C72BCF7334A2**, physical lines **199–206**). This is **context only**; no §14.29 theorem is recertified.
- These are present reader statements and replacement proofs, not inferred source-number matches. Historical attribution and both different nonuniqueness models are preserved. No Demailly approximation or related excluded proof programme is involved.

## Precise new statement

Use the specific Section 14.27 construction on X = P(C² ⊕ C²) = P³. Fix the printed s with 0 < s < 1 and let

\[
r=\log\frac{|A|^2}{|B|^2},\quad
\sigma(r)=\frac{e^r}{1+e^r},\quad
S=\sigma'(1)=\sigma'(-1)=\frac{e}{(1+e)^2}.
\]

On -1 < r < 1 set

\[
p(r)=C\exp[-1/(1-r^2)],\qquad q=p',\qquad
\int_{-1}^1p\,dr=1,\quad C>0,
\]

and let g be the *same* smooth, nonnegative density of Equation 14.27.2, defined by
\[
g\omega_X^3=(\omega_0+sH)^3.
\]

Let δ = 1 - |r| tend to zero **from inside the central band** (-1,1). The following exact, common one-sided asymptotic holds at **both** r = -1 and r = 1:

\[
\boxed{\lim_{\delta\downarrow0}
 g(r)\,\delta^2 e^{1/\delta}
 =\frac{(1-s^2)C^2e^{-1/2}}{2S^2}>0.}
\tag{A}
\]

In particular, **every inverse positive power is nonintegrable** for the smooth normalized Fubini–Study volume:
\[
\boxed{g^{-\alpha}\notin L^1(X,\omega_X^3)
\quad\hbox{for every }\alpha>0.}
\tag{B}
\]
This is true although the zero locus M_-∪M_+ is a pair of smooth real hypersurfaces, hence of measure zero and empty interior.

Write ν = ω_X³ / ∫_X ω_X³. For the **central open band only**, the small-density sublevel set satisfies the exact logarithmic law
\[
\boxed{\lim_{\lambda\downarrow0}
 \log(1/\lambda)\;
 \nu\{-1<r<1,\ 0<g\le\lambda\}
 =12 S^2.}
\tag{C}
\]
Furthermore, for every β>0, the positive logarithmic moment of the central-band density obeys
\[
\int_{\{-1<r<1\}}[\log^+(1/g)]^\beta\,d\nu<\infty
\quad\Longleftrightarrow\quad 0<\beta<1.
\tag{D}
\]
The integral in (D) does not include the outer sides of the two zero hypersurfaces. Those sides involve the freely chosen smooth flat function s(r) in §14.26.7 (distinct from the fixed scalar parameter s here), so **no global exact asymptotic (C) or global logarithmic-moment threshold is asserted**. In particular the valid global consequence of (C) is only a corresponding lower bound for the full sublevel measure.

## Self-contained computation, including constants

**1. Exact local determinant.** By §14.26.4, P²=Q²=R²=0 and
\((xP+yQ+zR)^3=6xyz\,P\wedge Q\wedge R\). By §14.26.6,
\[
\omega_X^3=6[\sigma'(r)]^2P\wedge Q\wedge R.
\]
Thus, with the actual Section 14.27 coefficients,
\[
g(r)=\frac{k_s(r)}{[\sigma'(r)]^2},\quad
 k_s=(x+sp)(y-sp)(z+sq).
\tag{1}
\]
The printed coefficient identities specialize on fixed interior neighborhoods of the respective endpoints to
\[
\begin{array}{ll}
r\downarrow-1:\quad
(x,y,z)=(1+p,p,q),&
k_s=(1-s^2)\,[1+(1+s)p]\,p\,q,\\[2mm]
r\uparrow1:\quad
(x,y,z)=(p,1+p,-q),&
k_s=(1-s^2)\,[1+(1-s)p]\,p\,(-q).
\end{array}
\tag{2}
\]
The factors are strictly positive inside the band. The ODE solution used to produce the uncountably many different potentials does **not** alter the common k_s: the same g is shared by all those solutions.

**2. Exact flatness asymptotic.** Differentiation gives
\[
q(r)=-\frac{2r}{(1-r^2)^2}p(r).
\]
On the corresponding one-sided neighborhoods \(|r|\to1\), equations (1)–(2) therefore give
\[
g(r)=\frac{2(1-s^2)|r|C^2}{(1-r^2)^2[\sigma'(r)]^2}
 [1+O(p(r))]\exp[-2/(1-r^2)].
\tag{3}
\]
Here \(1-r^2=2\delta-\delta^2\), and consequently
\[
\frac{2}{1-r^2}=\frac1\delta+\frac12+O(\delta),
\qquad
\frac{2|r|}{(1-r^2)^2}=\frac{1+O(\delta)}{2\delta^2}.
\]
Also \(\sigma'(r)\to S>0\). Substituting these **one-sided** expansions into (3) proves (A), with no unspecified finite leading coefficient.

**3. All inverse powers diverge.** The smooth positive measure ω_X³ in a tubular neighborhood of either regular hypersurface r=±1 has a smooth density bounded above and below by positive constants relative to \(dr\) times tangential volume. Equivalently the pushforward formula below provides an explicit positive radial density. Formula (A) gives \(g(r)^{-\alpha}\ge c_\alpha \delta^{2\alpha}\exp(\alpha/\delta)\) for sufficiently small δ>0, and
\[
\int_0^{\delta_0}\delta^{2\alpha}e^{\alpha/\delta}\,d\delta=\infty
\quad(\alpha>0).
\]
This proves (B); measure zero of the vanishing set does not prevent divergence near it.

**4. Exact Fubini–Study radial probability and small sublevels.** On the unit sphere of C⁴, the squared lengths of the independent two-component blocks A and B have two-dimensional complex polar volume exponents \(t^{2-1}\) and \((1-t)^{2-1}\). The Hopf projection induces the normalized Fubini–Study probability, so \(T=|A|^2/(|A|^2+|B|^2)\) has density \(6t(1-t)\,dt\) on (0,1), since \(\int_0^1 6t(1-t)\,dt=1\). Under \(t=\sigma(r)\), \(dt=\sigma'(r)\,dr\), this becomes
\[
d(\nu\circ r^{-1})=6[\sigma'(r)]^2\,dr.
\tag{4}
\]
From (A),
\[
\log\frac1{g(r)}=\frac1\delta+2\log\delta+O(1).
\tag{5}
\]
Fix any 0<ε<1 and set L=log(1/λ). As L→∞, (5) sandwiches the inner-band set \(0<g\le\lambda\), near **each** endpoint, between collars of widths \((1-\varepsilon)/L\) and \((1+\varepsilon)/L\). On a closed subinterval away from the endpoints, g has a strictly positive minimum, so no other small sublevel components occur. Equation (4) gives for either collar radial mass \(6S^2(1+o(1))/L\). Sum the two sides and let ε→0 to prove (C). This is a statement **relative to the central band**; the exterior collar contributions are not silently discarded or assumed negligible.

**5. Logarithmic-moment threshold.** Formula (5) shows \(\log^+(1/g)\asymp \delta^{-1}\) near each endpoint from the inside. Equation (4) supplies upper and lower positive finite density bounds there. Thus the integral in (D) behaves like a positive multiple of \(\int_0^{\delta_0}\delta^{-\beta}\,d\delta\), finite precisely when β<1. Away from the endpoints it is bounded. No convergence theorem is applied across a moving, unquantified family.

## Classification, distinction, proposed text and actual coverage

**Status:** low / verified conditional deduction, conditional only on the *printed existence* of the radial background and its smooth coefficient gluing in §14.26 and on standard Fubini–Study volume normalization. Equations (A)–(D) and the one-sided estimates are independently derived from actual integrated coefficients. Theorem 14.27.1 and Lemmas 14.27.3/7 remain **correct as reviewed**, not declared false; this report does not turn their ODE/existence proofs into a whole-section certificate. The other analytic inputs and the model-background normalization remain incompletely audited.

**Distinct from earlier work:** the recorded §14.27 slope-order and compact-interior separation result POME-DEGENMA-ORDER-QUANT-SEPARATION-001 treats the **solutions**, not the inverse-density integrability or sublevel-distribution tail. The §14.29 analytic example has **quadratic** zeros and \(f_*^{-\alpha}\in L^1\iff\alpha<1/2\) (Equation 14.29.16), while this **infinitely flat** example has no integrable inverse power. Preserve both valid examples; do not merge by title, zero-set topology, or the existence of nonuniqueness.

**Proposed non-applied correction:** an optional Remark after Theorem 14.27.1 or following the endpoint Lemma 14.27.7 should state (A)–(B), and (C) if a quantitative comparison with §14.29 is desired. Keep original theorem wording, proof, historical attribution, permanent tags, and source revisions unchanged. **Affected dependents:** any attempt to use the §14.27 model as evidence for nonuniqueness under a condition \(g^{-\alpha}\in L^1\) with α>0 is invalid; the quantitative integrability/sharpness comparisons in §§14.21 and 14.29 are distinct. Nothing shows an actual downstream theorem makes that invalid inference.

**Actual selected coverage:** newly proved endpoint determinant, radial mass, inverse-power and log-sublevel calculations in §14.27, plus hypothesis-only checks in §§14.26 and 14.29. §14.27 was previously partially checked; **zero first-visited sections; zero completely certified sections** in this run. At reviewed main, the inventory remains **25 chapters / 747 numbered sections**; no other ledger entry is reclassified. User-excluded Demailly approximation/regularization and Bergman, L², Ohsawa–Takegoshi, multiscale atlas, positivity-loss proof completion all remain **deferred-by-user**, not solved/certified. No source, registry, canonicalization, main, build, test, CI, formalization, or publication change was made.
