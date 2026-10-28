# Integral torus polarizations: an exact Picard–Albanese index and generic nonprojectivity

**Audit date:** 2026-10-29. **Pinned production main:** <code>b6933b772f41b45918f7e25ed1afbbb1fd892272</code>. **Starting audit HEAD:** <code>f43cca0dd8e44054a3d5418767640318cb7f8f2e</code>. **Scope:** first independent proof/model-level inspection of §10.80.2–4, with §10.80.1 and §§10.79.2, 10.79.4–5, 10.79.11 used solely for the exact integral lattice and convention checks. The printed statements are correct on the models below. This is not a transitive certification of all their Hodge, Picard or projectivity inputs.

## POME-PIC-ALB-EXACT-PRODUCT-INDEX-001

**Severity:** low. **Status:** verified conditional deduction (not a false printed theorem or a repaired proof). **New inspection anchor:** §10.80.4, source <code>demailly-complex-geometry:354EFEF2</code>, permanent tag <code>183B8F4BFE57</code>, main <code>docs/sections/compact-curves-periods-and-complex-tori--projectivity-and-integral-periods/index.html</code>, blob <code>f9b42d19c3b216883c147bc8b47f7af4b22bf026</code>, physical lines 99–149, especially the Hermitian form lines 113–128 and the complex-linear Picard-to-Albanese comparison lines 133–147. **Exact internal premise:** §10.79.11, source <code>demailly-complex-geometry:E24CF274</code>, permanent tag <code>6D7C5C5A2C24</code>, <code>docs/sections/compact-curves-periods-and-complex-tori--integral-periods-picard-tori-and-albanese-maps/index.html</code>, blob <code>81ec78509629e15d648cfd3b686fe4d691437330</code>, physical lines 175–235: the curve Serre map sends the Picard integral lattice *onto* the period lattice, with its explicit wedge-order convention. This upstream lattice theorem is treated as a stated internal input, not independently proved anew.

**Hypotheses and exact conclusion.** Let \(C\) be a connected compact curve of genus \(g\ge1\), let \(n\ge2\), and set \(X=C\times\mathbb P^{n-1}\). Normalize a positive area form \(\alpha\) on \(C\) by \(\int_C\alpha=1\), and let \(\beta\) be normalized Fubini–Study curvature, \(\int_{\mathbb P^{n-1}}\beta^{n-1}=1\). For every positive integer \(k\) the form
\[
\omega=p_C^*\alpha+k\,p_{\mathbb P}^*\beta
\]
is an integral Kähler polarization of the projective \(n\)-fold \(X\). Write
\[
W=H^{0,1}(X)=H^{0,1}(C),\quad
V=H^{1,0}(X)=H^{1,0}(C),\quad
\Lambda=\operatorname{pr}^{0,1}H^1(X,\underline{\mathbb Z}),
\]
and let \(\Gamma\subset V^*\) be the loop-period lattice. For precisely the map \(B\) printed in §10.80.4,
\[
B(u)(v)=\int_Xu\wedge v\wedge\omega^{n-1},
\]
the **exact** lattice identity and index are
\[
\boxed{ B\Lambda=-k^{n-1}\Gamma,\qquad
       [\,\Gamma:B\Lambda\,]=k^{2g(n-1)}.}
\]
The minus sign is the printed wedge-order convention: §10.79.11 uses \(\mathcal S(u)(v)=\int_Cv\wedge u\), so \(B=-k^{n-1}\mathcal S\). In particular, \(B\Lambda\subset\Gamma\) is frequently *strict*; no integral unimodularity or canonical isomorphism of these two specific embedded lattices follows from the theorem.

**Complete model computation.** Since \(u,v\) are pulled back from the curve, \(u\wedge v\) has curve degree two, so all positive powers of \(p_C^*\alpha\) wedge to zero. In the binomial expansion only
\[
\omega^{n-1}\equiv k^{n-1}p_{\mathbb P}^*(\beta^{n-1})
\quad\bmod p_C^*\alpha
\]
contributes. Product integration gives \(B(u)(v)=k^{n-1}\int_Cu\wedge v\). On the curve, the internal §10.79.11 theorem asserts \(\mathcal S\Lambda=\Gamma\), hence \(B\Lambda=-k^{n-1}\Gamma\). Since \(\Gamma\) is a full rank-\(2g\) lattice, multiplication by \(k^{n-1}\) has index \(k^{2g(n-1)}\). No integral Poincaré duality of the *higher-dimensional* product is assumed.

The printed Hermitian form satisfies
\[
h_X(u,v)=-2i\int_Xu\wedge\overline v\wedge\omega^{n-1}
       =k^{n-1}h_C(u,v).
\]
Its alternating imaginary form on a symplectic integral basis of the curve lattice has polarization type \((k^{n-1},\ldots,k^{n-1})\), with \(g\) entries (equivalently, use the curve collar/current construction in §10.79.11 for the unimodular genus-\(g\) pairing). At \(k=1\) this induced polarization is principal; for \(k>1\) it is not principal, even though the underlying tori \(J(X)\) and \(A(X)\) remain projective. For \(C\) elliptic, \(n=2\), \(k=2\), the exact index is \(4\).

**Proposed addition:** optional explicit example after the finite-index sentence in §10.80.4. Preserve the existing theorem, lattice convention, permanent tags, and its proof. **Affected dependents:** integral Riemann-form arguments §10.80.2, projective Jacobian/Albanese comparison §10.80.4, the period lattice §§10.79.4–5/.11, and any proposed *principal* rather than merely *integral positive* polarization claim. Nothing here upgrades the conditional upstream Hodge, sheaf/period, or projectivity theorems to complete verification.

## POME-TORUS-INTEGRAL-H2-NONPOLARIZATION-001

**Severity:** low. **Status:** verified conditional deduction, not an error in Theorem 10.80.2. **Anchor:** §10.80.2, source <code>demailly-complex-geometry:4A5F6AF1</code>, permanent tag <code>826013CCAFEC</code>, same §10.80 main HTML blob and physical lines 37–60. Background exact two-period criterion §10.65.1 (integrality versus \(J\)-invariance) is an identified internal premise; the linear-algebra/Baire argument below is independent of any regularization or analytic vanishing theorem.

**Precise assertion.** There exist complex two-dimensional tori \(T_J=(\mathbb R^4,J)/\mathbb Z^4\) for which none of the six linearly independent constant integral two-period forms represents a nonzero class of type \((1,1)\). In fact the complex structures with
\[
H^{1,1}(T_J,\mathbb R)\cap\operatorname{im}H^2(T_J,\mathbb Z)=\{0\}
\]
form a dense \(G_\delta\) in each orientation component of the manifold of constant linear complex structures \(J^2=-I\). Such tori are not projective, despite possessing many nonzero integral degree-two classes. Thus the **integrality condition alone** cannot replace the joint positivity/type-\((1,1)\) requirements in §10.80.2.

**Proof (with the nontrivial properness step).** For each nonzero \(E\in\bigwedge^2(\mathbb Z^4)^*\), let
\[
F_E=\{J\colon J^2=-I,\ E(Jv,Jw)=E(v,w)\ \forall v,w\in\mathbb R^4\}.
\]
This is a closed real-analytic subset of the manifold \(\mathcal J\cong GL(4,\mathbb R)/GL(2,\mathbb C)\) of linear complex structures, consisting exactly of those \(J\) for which the constant real two-form \(E\) has type \((1,1)\).

It is proper in *each* orientation component. Indeed choose independent \(v,w\) with \(E(v,w)\ne0\). Extend them to a basis \(v,w,e_3,e_4\). We can find an \(E\)-isotropic plane \(U\) complementary to \(\langle v,w\rangle\): take
\[
u=e_3+a v,\qquad t=e_4+d w.
\]
The expression \(E(u,t)=E(e_3,e_4)+aE(v,e_4)+dE(e_3,w)+adE(v,w)\) vanishes for a suitable \(a,d\): first choose \(a\) making the coefficient of \(d\) nonzero, then solve uniquely for \(d\). The graph plane spanned by \(u,t\) is automatically complementary to \(\langle v,w\rangle\). Define \(Jv=u,\ Ju=-v,\ Jw=t,\ Jt=-w\). Then \(J^2=-I\), but \(E(Jv,Jw)=E(u,t)=0\ne E(v,w)\). Reversing \(u\) in the definition of \(J\) provides the opposite complex-orientation component, with the same inequality. Thus \(F_E\) has no interior in either component (a nonidentically-zero real-analytic equation on a connected real-analytic component has nowhere dense zero set).

There are countably many nonzero integral \(E\). By the Baire theorem, their union of closed nowhere dense sets cannot cover either component of \(\mathcal J\), and its complement is dense \(G_\delta\). For a \(J\) in that complement, the exact torus-period result §10.65.1 and averaging §10.65.2 identify all real integral degree-two classes with constant integral two-forms; none can be \(J\)-invariant apart from zero. Any projective embedding would pull back an integral positive \((1,1)\) class, contradiction. This is also exactly the necessity direction of the printed Riemann-form criterion.

**Sign sanity check, not a separate finding.** For the elliptic torus \(\mathbb C/(\mathbb Z+\tau\mathbb Z)\), \(\operatorname{Im}\tau>0\), the linear-first Hermitian form \(h(z,w)=z\overline w/\operatorname{Im}\tau\) has \(\operatorname{Im}h(1,\tau)=-1\), so \(-\operatorname{Im}h(1,\tau)=+1\). This matches §10.80.2's choice \(\omega=-\operatorname{Im}h\); no normalization/sign defect was found.

**Proposed addition:** optional sharpness remark explaining why positive-definite Hermitian, type-\((1,1)\), and integral lattice conditions cannot be independently dropped. **Affected dependents:** §§10.65, 10.80.1–2, Picard/Albanese integral polarization; not an assertion about any specific explicit rational period matrix. The standard Baire theorem is the only elementary topological input in the genericity step; the stated exact period theorem and averaging identify integral classes, rather than a new proof of all integral-cohomology comparison.

## Precise review coverage and nonclaims

- **First direct selected proof/model review:** the printed Riemann-form criterion and its sign conventions §10.80.2 (physical lines 37–60), integer trace Lemma §10.80.3 (lines 65–94; statement and section-cutting mechanism checked), and Picard/Albanese §10.80.4 (lines 99–149; full displayed polarization and lattice comparison read). §10.80.1 (lines 11–33) is hypothesis/conclusion context, **not** a separate proof certification.
- **Supporting comparison only:** §10.79.11 exact curve lattice map (lines 175–235) and §§10.79.2/.4/.5, §10.65.1–2. No entire theorem dependency chain, section, or chapter is certified.
- The existing ToC coverage ledger remains **25 chapters / 747 unique numbered sections / zero certified complete sections**; this run upgrades a selected portion of §10.80 from dependency-only to direct proof/model coverage, not the entire section.
- Both items are newly proved mathematical examples/refinements, **not confirmed errors** and **not claimed proof repairs**. Previously recorded false theorems, missing proofs, external inputs, duplicate/integration defects, and other finding IDs keep their recorded states.
- All dedicated Demailly approximation/regularization plus Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss proof-completion work remains **deferred-by-user** and was not reviewed or changed. This report contains no private manuscripts or unpublished source scans. No production reading HTML, source repositories, body, registry, canonicalization, tags, tests, build, CI, formalization, PR merge or website publication was changed or performed.
