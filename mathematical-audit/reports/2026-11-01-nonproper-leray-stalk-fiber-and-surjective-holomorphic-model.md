# Nonproper Leray higher-direct-image stalks need not be fiber cohomology

**Audit date:** 2026-11-01. **Production main SHA:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Finding:** POME-LERAY-NONPROPER-STALK-FIBER-001 — **low / verified conditional deduction**. This verifies the sharp necessity of the *printed warning* in Theorem 10.55.6; the theorem is **not false**, and no repair of its proof is asserted.

## Current integrated source and exact scope

- **Main HTML:** `docs/sections/spectral-sequences-support-and-cup-products--hypercohomology-and-direct-image-spectral-sequences/index.html`; Git blob `83ea6c60c0691a7e3559214e363361863f3ea2a2`.
- **Theorem 10.55.6:** source `demailly-complex-geometry:8B97C424`, permanent tag `2CFDCB1083B2`, physical statement lines **104–112** (especially **108–112**); proof lines **118–126**, and edge-map identification **131–170**.
- **Definition 10.55.5:** source heading tag `CF90123DE41C`, lines **92–100**. The printed stalk formula is
  \[
  (R^q f_*A)_y=\varinjlim_{V\ni y}H^q(f^{-1}V,A).
  \]
  The printed theorem **explicitly refrains** from identifying it with \(H^q(f^{-1}(y),A|_{f^{-1}(y)})\) without additional hypotheses. The proof correctly invokes exact filtered stalk limits; the examples below show why the limit cannot be replaced by cohomology of a single fiber.
- **Additional direct inventory only:** `docs/sections/separation-strict-exhaustions-and-coverings/index.html`, production blob `89f1c30a6df3c3df624fd05943a5cc64460824b8`, section **9.25** tag `D10F3B8AA2A1`, physical lines **1–15**. This page is navigation/citation only; it contributes **no independently reviewed mathematical theorem**.

## First explicit holomorphic countermodel: punctured disk inclusion

Let \(D=\{z\in\mathbb C:|z|<1\}\), \(D^*=D\setminus\{0\}\), and \(j:D^*\hookrightarrow D\) the open holomorphic inclusion. Take the constant sheaf \(\mathbb Z_{D^*}\).

For the cofinal neighborhoods \(D_\varepsilon=\{|z|<\varepsilon\}\) of \(0\), their inverse images \(D_\varepsilon^*\) deformation retract onto a circle. The restriction maps between any nested punctured disks preserve the standard positively oriented generator in degrees zero and one. Therefore the **actual filtered-stalk limits** give
\[
 (j_*\mathbb Z)_{0}=\varinjlim_\varepsilon H^0(D_\varepsilon^*,\mathbb Z)
 \simeq\mathbb Z,\qquad
 (R^1j_*\mathbb Z)_{0}=\varinjlim_\varepsilon H^1(D_\varepsilon^*,\mathbb Z)
 \simeq\mathbb Z,
 \quad (R^qj_*\mathbb Z)_0=0\ (q\ge2).
\]
But \(j^{-1}(0)=\varnothing\). Hence **every** sheaf-cohomology group of that fiber is zero, including \(H^0\). This directly refutes either putative fiber identification in degrees \(q=0\) or \(q=1\), without contradicting the printed theorem.

On every small disk about a point \(y\ne0\) the map \(j\) is an isomorphism, so \(R^qj_*\mathbb Z\) has zero stalk there for \(q>0\). Near \(0\), the loop class gives the canonical local generator. Thus
\[
j_*\mathbb Z_{D^*}\simeq\mathbb Z_D,\qquad
R^1j_*\mathbb Z_{D^*}\simeq i_*\mathbb Z_{\{0\}},\qquad
R^qj_*\mathbb Z_{D^*}=0\ (q\ge2),
\]
where \(i:\{0\}\hookrightarrow D\). In the first isomorphism, connected punctured neighborhoods of \(0\) ensure local constant sections extend uniquely; in the second, the stable winding class and vanishing away from \(0\) give the skyscraper sheaf. These are **sheaf** identities, not mere matching of stalk dimensions.

Theorem 10.55.6 now has \(E_2^{0,0}=\mathbb Z\) and \(E_2^{0,1}=\mathbb Z\), and no other nonzero terms: the disk has \(H^{p>0}(D,\mathbb Z)=0\) and a skyscraper sheaf is flabby/acyclic. There are no possible differentials or extension ambiguities. The abutment is
\[
 H^0(D^*,\mathbb Z)=\mathbb Z,\qquad
 H^1(D^*,\mathbb Z)=\mathbb Z,\qquad
 H^{n\ge2}(D^*,\mathbb Z)=0,
\]
agreeing independently with circle retraction. Importantly, \(H^1(D,j_*\mathbb Z)=0\) while \(H^1(D^*,\mathbb Z)=\mathbb Z\): the higher-direct-image vanishing hypothesis in the printed **edge isomorphism** cannot simply be omitted.

## Stronger model: surjectivity and nonempty fibers still do not suffice

Let \(X=D^*\sqcup D\), a disconnected **pure one-dimensional complex manifold**, and define a **surjective holomorphic map**
\(f:X\to D\) by \(f|_{D^*}=j\) and \(f|_D=\mathrm{id}_D\). For the constant sheaf \(\mathbb Z_X\),
\[
f^{-1}(D_\varepsilon)=D_\varepsilon^*\sqcup D_\varepsilon,\qquad
f^{-1}(0)=\{0_D\}.
\]
The same retractions and stable restriction generators give
\[
(f_*\mathbb Z_X)_0\simeq\mathbb Z^2,\qquad
(R^1f_*\mathbb Z_X)_0\simeq\mathbb Z,
\qquad
H^0(f^{-1}(0),\mathbb Z)=\mathbb Z,\quad
H^1(f^{-1}(0),\mathbb Z)=0.
\]
Thus failure is **not explained merely by an empty fiber or a nonsurjective map**. The map is nonproper: the preimage of a closed small disk contains a punctured disk sequence tending to the omitted point of its component. No false claim is made about proper base change; its hypotheses and proof are **not** supplied by this example.

As a further spectral-sequence check, \(f_*\mathbb Z_X\simeq\mathbb Z_D\oplus\mathbb Z_D\) and \(R^1f_*\mathbb Z_X\simeq i_*\mathbb Z_{\{0\}}\). Their higher cohomology on the disk vanishes. Leray consequently gives \(H^0(X,\mathbb Z)=\mathbb Z^2\), \(H^1(X,\mathbb Z)=\mathbb Z\), exactly as the direct disjoint-union computation.

## Assessment, action, and limitations

**Status and severity:** **low / verified conditional deduction** (explicit counterexamples to a *nonasserted stronger statement*); **no confirmed theorem error, proof gap, or applied repair**. The topological calculations use only the cofinal-neighborhood definition of stalk, elementary circle deformation retract, the disk's acyclicity for constant coefficients, and skyscraper flabbiness; the Leray comparison uses the printed Theorem 10.55.6 as the named internal input. The actual stalk computations and the collapse of both displayed first-quadrant Leray pages were checked directly. No appeal to Bergman, \(L^2\), Ohsawa–Takegoshi, Demailly regularization, or any excluded proof programme occurs.

**Optional proposed source patch, not applied:** place the two elementary examples *after* the warning in Theorem 10.55.6, preserving source attribution and the permanent tag. A derived general statement identifying \(R^q f_*\) with fiber cohomology would need **new, explicit hypotheses** (e.g. an appropriate proper-base-change setting); no such statement is smuggled into the reading edition.

**Affected mathematical dependents:** §10.55.6's Leray edge and stalk interpretation; sheaf/direct-image discussions in §§9 and 10 concerning nonproper maps and modifications. There is **no defect** in the printed stalk limit or its qualified edge statement. The long-exact-sequence, Godement functor and general hypercohomology proof chains have **not** been newly certified, and §9.25 remains navigation-only.

**Actual coverage:** newly verified **specific** degree-0/1 higher-image models and the Leray $E_2$-page computation at §10.55.5–6; §10.55 was already partially reviewed and this does **not** certify the whole theorem, section, or other cited external inputs. §9.25 newly inspected as an **intro-only** page and is **not mathematical proof coverage**. Existing matrix counts remain **25 chapters / 747 numbered current ToC sections / zero entire mathematically certified sections**. All earlier confirmed errors, unresolved proof gaps, external-dependency records, duplicates, and user-deferred items retain their prior statuses. Demailly approximation/regularization and dedicated Bergman/$L^2$/OT/multiscale/positivity-loss programme remain **deferred-by-user**, not resolved. No main/source/body/registry/permanent-tag edit, build, test suite, CI, formalization, or site publication was performed.