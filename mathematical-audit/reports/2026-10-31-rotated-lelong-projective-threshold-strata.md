# Exact projective jumping strata for weighted Lelong numbers along lines

**Date:** 2026-10-31. **Production main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Stable finding ID:** POME-ROTATED-LELONG-PROJECTIVE-STRATA-001.
**Severity:** low. **Status:** verified conditional deduction; the printed theorem is not shown false, and no repair has been integrated.

## Actual integrated passages and immutable anchors

- Main docs/sections/lelong-densities-generalized-masses-and-multiplicity--rotation-of-an-arbitrary-isolated-continuous-weight/index.html, blob 9175f1ac475bf4a9f9d9a1749037ae86beb675e8, Theorem **6.45.2**, source **demailly-complex-geometry:A05C5CFA**, permanent tag **E186C2A7FA32**, physical HTML lines **35–41**, especially Equation **6.45.3** source **demailly-complex-geometry:3D3D2464**, permanent tag **B144F857EFF6**, lines **37–39**.
- The same theorem's rotating-threshold passage, physical lines **49–53** (Equation **6.45.4**, tag **F13CFDE93F11**); averaging and origin-atom passage, lines **98–105**. These analytic steps are contextual, not independently certified.
- Lemma **6.45.1** source **demailly-complex-geometry:F7E1037D**, permanent tag **D72B7AE5B407**, same blob lines **7–30**, establishes the Haar-null condition used in the source. This report independently verifies that condition for the explicit algebraic strata below, but does not reprove the lemma in full.
- Independent cross-check only: Theorem **6.41.14**, source **demailly-complex-geometry:1B549607**, permanent tag **5BC026092C60**, main file **docs/sections/lelong-densities-generalized-masses-and-multiplicity--concurrent-slices-of-positive-currents/index.html**, blob **a851fa12c59217cbf13efd381fd44524388fcfdc**, lines **237–277**: the a.e.-plane quantifier must not silently become an every-plane assertion. The present example uses ordinary line restrictions, not the normalized concurrent-slice construction; it is *not* a new verification of the latter theorem.

## Exact model, hypotheses and conclusion

Take complex dimension \(n\ge 2\), positive real weights \(a_1,\ldots,a_n\), and a neighborhood of the origin in the unit polydisc. Set
\[
 \varphi_a(z)=\max_{1\le j\le n}\bigl(a_j\log|z_j|^2\bigr),
 \qquad a_*=\min_j a_j,
\]
with \(\log 0=-\infty\). This is an extended-continuous plurisubharmonic function with exactly one pole at \(0\), as required by Theorem 6.45.2. Write \(L_v=\mathbb Cv\) for a nonzero vector \(v=(v_1,\ldots,v_n)\) and let \(T_v=[L_v]\) be its integration current in a coordinate ball, of bidimension \((1,1)\).

The exact identities are
\[
 \nu(T_v,0)=1,\qquad
 \nu(dd^c\varphi_a,0)=a_*,
 \qquad
 \boxed{\nu(T_v,\varphi_a)=\min_{\{j:v_j\ne0\}}a_j.}
 \tag{1}
\]
Here \(dd^c=\frac{i}{2\pi}\partial\bar\partial\), so \(dd^c\log|t|^2=\delta_0\) on a complex line. In the notation of Theorem 6.45.2, this is its \(p=1\) case. In particular the printed inequality is valid and sharp for every such model.

There is more information than merely a strict-inequality example. For any real threshold \(c\), the jumping locus of line directions is exactly
\[
 \boxed{\left\{[v]\in\mathbb P^{n-1}:
      \nu(T_v,\varphi_a)\ge c\right\}
 =\mathbb P\!\left(\operatorname{span}\{e_j:a_j\ge c\}\right),}
 \tag{2}
\]
with the convention that the projectivization of the zero space is empty. The right side has dimension \(\#\{j:a_j\ge c\}-1\), when nonempty. For \(c>a_*\) it is a proper projective linear subspace, hence is null for invariant probability on \(\mathbb P^{n-1}\).

For any fixed \(v\ne0\) and \(g\in\mathrm{GL}_n(\mathbb C)\),
\[
 \nu(T_v,\varphi_a\circ g)
  =\min_{\{j:(gv)_j\ne0\}}a_j.
 \tag{3}
\]
For \(c>a_*\), the superlevel subset of \(\mathrm{GL}_n\) is the intersection with a **proper linear algebraic condition**
\[
 (gv)_j=0\quad\text{for every }j\text{ with }a_j<c.
 \tag{4}
\]
It is either empty or a proper complex algebraic subvariety. Thus the source's locally pluripolar threshold locus is explicitly algebraic in this family. The inverse image under the unitary action of the proper projective subspace (2) has Haar measure zero, and consequently
\[
 \boxed{\int_{\mathrm U(n)}\nu(T_v,\varphi_a\circ g)\,dg
      =a_*=\nu(T_v,0)\nu(dd^c\varphi_a,0).}
 \tag{5}
\]
This verifies the theorem's average identity and almost-everywhere quantifier in a nonradial, nonsmooth example, without invoking an approximation theorem.

## Complete elementary proof

A maximum of finitely many plurisubharmonic functions is plurisubharmonic. The maximum is finite and continuous away from the origin: at every nonzero point at least one coordinate is nonzero, while terms with zero coordinate tend to \(-\infty\). For \(|z|=r<1\), all \(a_j\log|z_j|^2\le a_*\log r^2\). Equality is attained at \(z=re_k\) whenever \(a_k=a_*\). Hence
\[
 \sup_{|z|=r}\varphi_a(z)=a_*\log r^2,
\]
which by the defining spherical-growth characterization gives \(\nu(dd^c\varphi_a,0)=a_*\). The same estimate shows uniform convergence of \(\varphi_a\) to \(-\infty\) near zero, so this is indeed its only pole.

Parameterize the line \(L_v\) by \(t\mapsto tv\). Since \(v\ne0\), the restricted potential is finite off \(t=0\) and
\[
 \varphi_a(tv)=\max_{j:v_j\ne0}
 \left(a_j\log|t|^2+a_j\log|v_j|^2\right)
 =a(v)\log|t|^2+O_v(1),
 \quad a(v)=\min_{j:v_j\ne0}a_j.
\]
The \(O_v(1)\) term is bounded near zero, and the restricted function is subharmonic. Its Riesz measure has atom \(a(v)\delta_0\), by \(dd^c\log|t|^2=\delta_0\) and the standard bounded-perturbation invariance of Lelong number on a curve. The classical proper restriction of the degree-one product to the smooth curve \(L_v\) coincides with this one-variable Riesz measure. This proves (1). The integration current of a smooth complex line has Lelong number one.

Now (1) implies \(a(v)\ge c\) exactly when every nonzero component of \(v\) has weight at least \(c\). This is (2), including the equal-weight and empty cases. Replacing \(v\) by \(gv\) proves (3) and (4). A unitary image of any fixed line is uniformly distributed over the projective directions, and a proper projective linear subspace has invariant measure zero. Therefore (3) equals \(a_*\) almost everywhere and is bounded between \(a_*\) and \(\max_j a_j\), giving (5) by direct integration. No sequential compactness, interchange of singular-current limits, Bergman kernel, \(L^2\) argument, Ohsawa–Takegoshi theorem, or Demailly approximation is used.

## Sharpness, failed stronger assertion, and exact scope

For \(n=2\) and \(0<a_1<a_2\), take \(T=[z_1=0]\). Then
\[
 \nu(T,\varphi_a)=a_2>a_1
  =\nu(T,0)\nu(dd^c\varphi_a,0).
\]
But on every line with \(v_1\ne0\), equality holds. The ratio \(a_2/a_1\) is unbounded within the stated assumptions. Hence neither a universal **pointwise equality** in place of the printed lower bound nor a uniform upper comparison of the two sides is possible, even for a single smooth linear integration current and a continuous isolated toric pole. No printed assertion claims either false strengthening.

For weights \((1/2,3/2,5,5)\), all 15 nonempty coordinate supports and thresholds \(1/2,1,3/2,2,5,6\) were exhaustively checked with exact rational arithmetic. The allowed-projective-support counts were respectively \(15,7,7,3,3,0\), matching (2); this is a small **model check**, not a software build or formal mathematical verification.

**Proposed separately reviewable addition:** one compact explicit example after Equation 6.45.4 describing (1)–(2), and the strict directional example. Retain the original theorem, historical attribution, source IDs and permanent tags. **Affected dependents:** the interpretation of the Haar-a.e. qualifier in Theorem 6.45.2 and the locally pluripolar threshold sets invoked from §6.39.8. **Not affected:** the full \(p>1\) theorem, which still depends on the printed weighted-product, cutoff and averaged-primitive arguments; those inputs are **not certified by this example**. The earlier standalone Lemma 6.45.1 finding remains separate and unchanged. No false theorem, genuine duplicate or global proof repair is asserted.

**Exclusion boundary:** The proof's relative Richberg smoothing and all Demailly approximation/regularization, Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion tasks were **not examined or extended**. They remain deferred-by-user, not resolved or certified. No source/body/registry/canonicalization, site, CI, publication, or production-main change is proposed here.
