# A hyperplane-current model attaining the full non-pluripolar comparison deficit

**Finding ID:** \`POME-NPP-COMPARISON-DEFICIT-OPTIMAL-001\`  
**Date:** 2026-11-08  
**Severity/status:** **low / verified conditional deduction** (sharpness of an existing theorem, not a false statement or a certified proof repair).  
**Production main read:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Integrated reading file:** \`docs/sections/non-pluripolar-products--maximal-mass-and-comparison/index.html\`, blob \`adbc9c739b3694725aa176e8013ac7f3077f035e\`.  
**Scope:** first selected theorem-level examination of §13.9; specifically Proposition 13.9.5 and the hypothesis boundary of Corollary 13.9.6. No entire-section verification.

## Precise printed anchors

- Definition 13.9.1: source \`foundations-of-pluripotential-theory:65F4E5E2\`, permanent \`4F64B29C315E\`, physical lines 9–17. In top degree the volume is the maximal non-pluripolar mass.
- Proposition 13.9.2: source \`foundations-of-pluripotential-theory:5364CD2E\`, permanent \`44F242B6965F\`, lines 19–45. Every positive current in the class has non-pluripolar mass at most the class volume.
- Proposition 13.9.5: source \`foundations-of-pluripotential-theory:D16465F8\`, permanent \`FEA17FAE6BAA\`, lines 77–101. For \(\mu_a=\langle(\theta+dd^c a)^n\rangle\),
  \[
    \mu_v(\{u<v\})\leq \mu_u(\{u<v\})
       +\operatorname{vol}(\{\theta\})-\mu_u(X).
  \]
  Its extra term can be omitted under a full-mass or relative-boundedness assumption.
- Corollary 13.9.6: source \`foundations-of-pluripotential-theory:5F5C5397\`, permanent \`D91589CC5A89\`, lines 105–121. The domination transfer requires \(u\geq v-O(1)\) and \(u\geq\rho-O(1)\).
- Definition 13.2.4 of the non-pluripolar product: source \`foundations-of-pluripotential-theory:9D8E4DD8\`, permanent \`D79952D7E272\`, in \`docs/sections/non-pluripolar-products--truncation-and-plurifine-locality/index.html\`, blob \`81be8c5acc360c96bd3c5acba05a3cdb5fafaf4c\`, lines 57–63. This is a **definition cross-check**; §13.2 was previously partially reviewed, not re-certified here.

## Exact all-dimensional model and proof

Fix any integer \(n\geq1\). On \(X=\mathbb P^n\), take the Fubini–Study form \(\omega=c_1(\mathcal O(1),h_{\mathrm{FS}})\) with the project's \(dd^c=\tfrac{i}{2\pi}\partial\bar\partial\) convention and let
\[
 V=\int_X\omega^n=\operatorname{vol}(\{\omega\})=1.
\]
The argument also works without making the last normalization, using \(V>0\) throughout. Write \(H=\{Z_0=0\}\) and set
\[
 \ell([Z_0:\cdots:Z_n])
 =\log\frac{|Z_0|^2}{|Z_0|^2+\cdots+|Z_n|^2}\leq0,
 \qquad
 u_\lambda=\lambda\ell,\quad v=0,\quad 0<\lambda\leq1.
\]
The ratio is invariant under scalar change of homogeneous coordinates, so \(\ell\) is globally defined as an extended-valued function, smooth off \(H\) and with logarithmic poles on \(H\). The Poincaré–Lelong identity with this convention is
\[
 dd^c\ell=[H]-\omega,\qquad
 T_\lambda=\omega+dd^c u_\lambda=(1-\lambda)\omega+\lambda[H]\geq0.
\]
Thus both \(u_\lambda,v\in\mathrm{PSH}(X,\omega)\) for every \(0<\lambda\leq1\). The singular set \(H\) is pluripolar. On \(X\setminus H\), \(T_\lambda=(1-\lambda)\omega\) is smooth, and the non-pluripolar construction restricts there to its ordinary wedge. Its extension places **no mass on \(H\)**, so without a hidden divisorial term,
\[
 \mu_{u_\lambda}
 =\langle T_\lambda^n\rangle
 =(1-\lambda)^n\,\omega^n,\qquad
 \mu_v=\omega^n.
\]
Here the equality is global as measures: the right-hand smooth measure also gives zero mass to \(H\). In particular,
\[
 \mu_{u_\lambda}(X)=(1-\lambda)^nV,\qquad
 V-\mu_{u_\lambda}(X)
   =\bigl[1-(1-\lambda)^n\bigr]V.
\]

The strict comparison set has a particularly simple form:
\[
 A_\lambda=\{u_\lambda<v\}
          =X\setminus\{[1:0:\cdots:0]\}.
\]
Indeed \(\ell=0\) exactly at that one point; on \(H\), \(\ell=-\infty<0\). Since \(n\geq1\), the single excluded point has zero \(\omega^n\)-measure. Consequently
\[
 \mu_v(A_\lambda)=V,\qquad
 \mu_{u_\lambda}(A_\lambda)=(1-\lambda)^nV
\]
and the printed comparison inequality is **an equality**:
\[
 \boxed{\mu_v(A_\lambda)
 =\mu_{u_\lambda}(A_\lambda)
   +V-\mu_{u_\lambda}(X).}
\]
More generally each desired mass fraction \(m/V\in[0,1)\) occurs on this family by choosing \(\lambda=1-(m/V)^{1/n}\). For \(0<\lambda<1\), the absolutely continuous part of \(T_\lambda\) is strictly positive, so sharpness is not an artifact confined to the pure divisor endpoint.

The coefficient of the mass deficit in Proposition 13.9.5 is therefore **optimal**: replacing it by a universal constant \(c<1\), while leaving the other term unchanged, would require
\[
 V\leq (1-\lambda)^nV+c\bigl[1-(1-\lambda)^n\bigr]V,
\]
which is false for every \(\lambda>0\). Omitting the deficit altogether also fails for all \(\lambda>0\).

## Exact failure if the domination hypotheses are dropped

Set \(\lambda=1\), \(\rho=v=0\), and \(u=u_1=\ell\). Then \(T_1=[H]\) and **\(\mu_u=0\)**, whereas \(\mu_\rho=\omega^n\). Hence \(u\geq v\) holds vacuously \(\mu_u\)-almost everywhere, but \(u<v\) on a set of full \(\mu_\rho\)-measure (indeed outside one point). Thus the conclusion of Corollary 13.9.6 would be false **without** its relative-singularity assumption \(u\geq v-O(1)\) or an equivalent replacement. That assumption is violated here: \(u\to-\infty\) along \(H\), while \(v=0\). Likewise \(u\geq\rho-O(1)\) fails. This is a sharpness check, **not** a counterexample to the printed corollary.

## Classification, proposed action and dependents

**Classification:** low / **verified conditional deduction**. Proposition 13.9.5 and Corollary 13.9.6 are both mathematically compatible with the example; no false theorem or unjustified proof step has been established. The computations use only the standard Poincaré–Lelong identity, the printed non-pluripolar truncation convention, smooth wedge products away from a divisor, and the top-degree volume of the Fubini–Study class. Neither Demailly regularization nor its excluded Bergman, weighted-\(L^2\), Ohsawa–Takegoshi, multiscale atlas, or positivity-loss programme is used.

**Suggested optional editorial addition (NOT made to production):** place this hyperplane model after Proposition 13.9.5 to demonstrate the necessary and optimal coefficient \(1\), and cite its pure-divisor endpoint as a caution following Corollary 13.9.6. Retain original statements, attribution, tags and conventions.

**Affected dependents to monitor, not condemned:** subsequent comparison and domination arguments that attempt to drop the relative-singularity/full-mass hypothesis or to reduce the mass deficit coefficient. No specific downstream printed error is claimed. The full dependency chains behind the general mass comparison, plurifine locality and positive products remain **unverified** by this single model. Existing findings and owner-deferred items retain their previous status.

**Actual work:** selected definition, theorem and proof inspection in §13.9; a single cross-check of §13.2's product definition; one new exact proof and counterexample to **unprinted strengthened assertions**. No builds, tests, CI, formal verification or website publication.
