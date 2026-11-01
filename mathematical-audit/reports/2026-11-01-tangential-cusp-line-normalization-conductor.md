# Tangential cusp–line normalization, conductor, and finite-map multiplicity

**Date:** 2026-11-01. **Reviewed production \`main\`:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Finding:** \`POME-NORM-TANGENTIAL-CUSP-LINE-CONDUCTOR-001\`; **severity:** low; **status:** verified conditional deduction (explicit analytic local-ring computation, **not** a false printed theorem or a completed general normalization proof). This is additional selected analysis of previously sampled §§9.4–9.5; it is not a claim of first coverage or of full-section certification.

## Exact integrated anchors and scope

- \`docs/sections/complex-spaces-and-modifications--reduced-spaces-and-normalization/index.html\`, production blob \`06439f43d1ce8e83d2529682c9a630bffa3d9c22\`: Lemma **9.4.2** (line 38, source \`foundations-of-pluripotential-theory:09E2DDFD\`, permanent \`26BA2ABFD727\`); Proposition **9.4.3** (line 56, source \`foundations-of-pluripotential-theory:AC231B8D\`, permanent \`36422A732754\`, proof lines 61–84); Theorem **9.4.6** (line 142, source \`foundations-of-pluripotential-theory:7042BB57\`, permanent \`12A47DB401E2\`, proof lines 146–163); Example **9.4.10** (line 197, source \`foundations-of-pluripotential-theory:680F3928\`, permanent \`60A14C7A1845\`). The main section tag is \`C16A2F5D9879\`.
- \`docs/sections/complex-spaces-and-modifications--analytic-curves-and-finite-maps/index.html\`, production blob \`2c725646172203283ac4564bddd46213d9a75cbe\`: Proposition **9.5.1** (line 11, source \`foundations-of-pluripotential-theory:7EBE91CF\`, permanent \`A3A9384DC317\`) and Proposition **9.5.6** (line 104, source \`foundations-of-pluripotential-theory:441B06F2\`, permanent \`0E64BF4DC7C7\`). These are the actual integrated reading-edition assertions, not similarly numbered source theorems.
- Underlying source scans/private notes were **not** accessed. No excluded Demailly approximation/regularization or dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss arguments were read or used.

## An infinite family, not just a cusp or a transverse node

Fix coprime integers \`2 <= p < q\`. At the origin of the complex plane put
\[
 X_{p,q}=\{\,y(y^p-x^q)=0\,\},\qquad
 A=\mathbb C\{x,y\}/\bigl(y(y^p-x^q)\bigr).
\]
The defining equation has two distinct reduced irreducible branches: the smooth line \`L=\{y=0\}\` and the singular branch \`C=\{y^p=x^q\}\`, tangent to \`L\` at the origin. Their intersection number is **exactly \`q\`**, since
\[
 \mathbb C\{x,y\}/(y,y^p-x^q)\simeq\mathbb C\{x\}/(x^q).
\]
The explicit normalization is the disjoint union of two discs, with maps
\[
 \nu_C(t)=(t^p,t^q),\qquad \nu_L(s)=(s,0).
\]
Indeed, \`R=\mathbb C\{t^p,t^q\}\` is a one-dimensional domain with normalization \`\mathbb C\{t\}\`: \`t\` is integral via \`t^p=x\`, the extension is finite, and the target is a normal discrete valuation ring; coprimality gives the common fraction field. The line has normal ring \`S=\mathbb C\{s\}\`. Thus
\[
 B=\overline A=\mathbb C\{t\}\oplus\mathbb C\{s\},\quad
 x\mapsto(t^p,s),\quad y\mapsto(t^q,0).
\]
The two inverse images of the origin are distinct. Away from the origin both branches are smooth, disjoint, and the map is biholomorphic. This explicitly checks the **branch count** and finite bimeromorphic behavior in Theorem 9.4.6; it is not a replacement proof of that theorem for arbitrary reduced spaces.

### Fiber-product and exact normalization defect

Let \`Q=\mathbb C\{x\}/(x^q)\`. The two branch rings map onto \`Q\` by \`t^p\mapsto x,\ t^q\mapsto0\` and \`s\mapsto x\`. Their fiber product is exactly \`A\`:
\[
 0\longrightarrow A\longrightarrow R\oplus S
    \xrightarrow{(\rho_R-\rho_S)} Q\longrightarrow0.
\]
The kernel assertion follows directly from the ideal identity
\((y)\cap(y^p-x^q)=(y(y^p-x^q))\) in the regular local ring \(\mathbb C\{x,y\}\); surjectivity follows from the line factor. This accounts for the length-\`q\` **interbranch gluing defect**.

For \(\gcd(p,q)=1\), the numerical semigroup \(\langle p,q\rangle\) has conductor
\[
 c=(p-1)(q-1)
\]
and exactly \(c/2\) gaps. For completeness: modulo \(p\), the least semigroup element in the residue class of \(bq\) is \(bq\) for \(0\le b<p\); counting the excluded smaller nonnegative elements gives
\(\sum_{b=0}^{p-1}\lfloor bq/p\rfloor=(p-1)(q-1)/2\).
The largest gap is \(pq-p-q=c-1\), seen by the same residue-class description. Consequently
\[
 \dim_{\mathbb C}\bigl(\mathbb C\{t\}/R\bigr)=c/2.
\]
Using the two exact inclusions \`A ⊂ R⊕S ⊂ B\`, the total local normalization defect is
\[
 \boxed{\delta(X_{p,q},0)=\dim_{\mathbb C}(B/A)
       =q+\frac{(p-1)(q-1)}{2}.}
\]
In particular, the singular branch's own delta invariant does **not** account for the tangential intersection contribution.

### Exact conductor on both normalization branches

The conductor of \`A\` in \`B\` is
\[
 \mathfrak c_{B/A}=\{\,b\in B: bB\subset A\,\}.
\]
Because the two summands of \`B\` can be multiplied independently, \((u(t),v(s))\in\mathfrak c_{B/A}\) iff
\[
 u\,\mathbb C\{t\}\subset \ker(R\to Q)=(t^q)R,
 \qquad v\,\mathbb C\{s\}\subset (s^q)S.
\]
The exponent set of \((t^q)R\) is \(q+\langle p,q\rangle\), whose conductor in the nonnegative integers is \(q+c\). Hence its largest \(\mathbb C\{t\}\)-ideal is precisely \(t^{q+c}\mathbb C\{t\}\). The second condition is exactly \(v\in s^q\mathbb C\{s\}\). Therefore
\[
 \boxed{\mathfrak c_{B/A}
       =t^{q+(p-1)(q-1)}\mathbb C\{t\}
        \ \oplus\ s^q\mathbb C\{s\}.}
\]
This computation uses the **full** normalization conductor, not merely the branchwise cusp conductor \(t^c\). The tangential gluing forces the stronger \(t^{q+c}\) vanishing on the cusp normalization.

For the smallest case \((p,q)=(2,3)\), the total delta is \(3+1=4\), the normalization has two points above the origin, and the conductor is \(t^5\mathbb C\{t\}\oplus s^3\mathbb C\{s\}\). Seven small coprime pairs were separately checked by exact numerical-semigroup enumeration: \((2,3),(2,5),(3,4),(3,5),(4,5),(4,7),(5,7)\). These finite checks are corroboration, **not** a proof of the general family.

### Independent finite-map and nonzerodivisor checks (§9.5)

The coordinate function \(x\) is nonzero on **both** branches, hence a nonzerodivisor in \(A\). Its local zero scheme has length
\[
 \dim_{\mathbb C}A/(x)
 =\dim_{\mathbb C}\mathbb C\{y\}/(y^{p+1})=p+1.
\]
For a generic sufficiently small nonzero \(x_0\), the finite map \(x:X_{p,q}\to\mathbb C\) has exactly \(p\) points on the cusp and one on the line (all simple). Thus the local length and generic degree both equal \(p+1\), in agreement with the finite-map framework of Proposition 9.5.1 and the pure codimension-one zero-set hypothesis in Proposition 9.5.6.

By contrast, \(y\) vanishes identically on the line branch, so it is a zerodivisor; its zero set has an entire one-dimensional component. This shows **why the nonzerodivisor/on-every-branch hypothesis in 9.5.6 is indispensable**, not that the proposition fails.

## Verdict, proposal, and dependency boundary

**Verdict:** **verified conditional deduction / low**, a new exact family of local models. No false statement, missing hypothesis, or proved gap in the cited integrated propositions was found in these selected steps. The printed normalization and finite-map assertions are consistent with this family. No general normalization uniqueness, conductor-coherence, finite-map theorem, or arbitrary analytic-space theorem is certified here; earlier \`POME-NORM-COUNTABLE-COVER-001\` and every other open ledger entry keep their previous status.

**Suggested *separate*, optional addition:** a short example or remark after Example 9.4.10 giving the fiber product, \(\delta\), and conductor formulas, retaining all existing source attribution, equations, source labels and permanent tags. It is **not** a proposed direct edit to production or a repair to main. Affected mathematical dependents include the branchwise weak-holomorphic decomposition in Lemma 9.4.2, integral closure/denominators in Proposition 9.4.3, the fiber statement of Theorem 9.4.6, curve normalization in Proposition 9.5.1 and the nonzerodivisor hypothesis of Proposition 9.5.6.

**Precise coverage:** additional explicit proof-level checks of §§9.4.2/.3/.6/.10 and §§9.5.1/.6 only, all historically sampled. **No full numbered section or complete upstream dependency chain certified.** Current ToC remains 25 chapters / 747 numbered sections / zero fully certified mathematical sections. No build, unit tests, CI, formalization, publication, website, source, registry or main changes.
