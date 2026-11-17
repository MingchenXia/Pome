# Cyclic quotient surface: exact local Cartier index of a Weil divisor

- **Finding:** `POME-CARTIER-CYCLIC-QUOTIENT-INDEX-001`
- **Date:** 2026-11-17
- **Severity / status:** low / **verified conditional deduction** (not a false printed theorem, not a claimed repair to one).
- **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Integrated reading edition:** `docs/sections/analytic-cycles-and-cartier-cycles/index.html`, blob `d4817ac64b1365bd967d42cd474fec169f992e28`.
- **Stable provenance:** subsection 20.6.1 permanent `0F9AFEB5C512`; Definition 20.6.2 source `demailly-complex-geometry:AFD209B1`, permanent `BE0C86A8DD65`, physical line 8; Proposition 20.6.3 source `demailly-complex-geometry:02B65FA7`, permanent `FD8966432506`, lines 13–25; Proposition 20.6.4 source `demailly-complex-geometry:BD1D45B4`, permanent `AA96C35C8290`, lines 28–43; Example 20.6.5 source `demailly-complex-geometry:E054C396`, permanent `0C462992AB3A`, lines 46–75.
- **Scope:** direct review of these cycle definitions, Cartier criterion and worked non-Cartier quadric example, plus a new independent normal-surface family. The previously reviewed threefold quadric non-Cartier argument is retained, not repeated as a new finding.

## Statement and exact hypotheses

Let (k\ge2) be an integer and consider the analytic surface germ
[
 X_k=\{(x,y,z)\in\mathbf C^3:xy=z^k\},\qquad o=(0,0,0).
]
Let (D=\{x=z=0\}\subset X_k) and (E=\{y=z=0\}\subset X_k), with the reduced irreducible Weil-divisor coefficients. Then (X_k) is a reduced **normal** surface, smooth outside (o), and for every integer (m)
[
 \boxed{\quad mD\text{ is Cartier at }o\quad\Longleftrightarrow\quad k\mid m.\quad}
]
In particular (D) is a Weil but not a Cartier divisor, while (kD=\operatorname{div}(x)) and (D+E=\operatorname{div}(z)). Thus (D) is (\mathbf Q)-Cartier of **exact local Cartier index (k)**. This is not a claim that the entire divisor class group has been independently computed.

## Proof

1. **Finite quotient model and normality.** Let (\zeta\) be a primitive (k)th root of unity, and let (\mu_k) act on (\mathbf C^2) by
[
 (u,v)\longmapsto(\zeta u,\zeta^{-1}v).
]
The map (\pi(u,v)=(u^k,v^k,uv)) maps onto (X_k). On convergent local power series, invariance means that a monomial (u^av^b) can occur only if (a-b\in k\mathbf Z). For (a\ge b), it is (x^{(a-b)/k}z^b); for (b>a), it is (y^{(b-a)/k}z^a). The split sums remain convergent when (|x|,|y|,|z|) are sufficiently small, by the coefficient majorant of the original convergent (u,v) series. Together with the relation (xy=z^k), the unique normal forms identify
[
 \mathcal O_{X_k,o}\simeq\mathbf C\{u,v\}^{\mu_k}.
]
The invariant ring is integrally closed: an invariant rational fraction integral over it is integral over the normal domain (\mathbf C\{u,v\}), hence lies in that domain, and remains invariant. The gradient of (xy-z^k) is ((y,x,-kz^{k-1})), which vanishes on (X_k) exactly at (o). This proves normality and smoothness off (o).

2. **Principal multiples.** At a generic point of (D), (y\ne0) and (z) is a transverse local parameter; the equation gives (x=z^k/y). Thus (\operatorname{ord}_D(x)=k). There is no other codimension-one component of (\{x=0\}), so (\operatorname{div}(x)=kD). Likewise (\operatorname{div}(y)=kE), while (z) vanishes to order one on each of (D,E), giving (\operatorname{div}(z)=D+E).

3. **The obstruction for all other multiples.** Suppose (mD) is Cartier as a **cycle** at (o). By the local characterization in Proposition 20.6.4, it is the divisor of a meromorphic germ (F=g/h) on (X_k), with (g,h) nonzero holomorphic germs. The quotient map is unramified in codimension one: the cyclic action is free on (\mathbf C^2\setminus\{(0,0)\}). The pullback (F\circ\pi) therefore has divisor (m\{u=0\}), and no other irreducible divisorial component in (\mathbf C^2). Unique factorization in (\mathbf C\{u,v\}) (the local smooth hypersurface factorization used by the printed Proposition 20.6.4 / Example 20.6.5) gives
[
 F\circ\pi=u^m e(u,v)
]
with (e\) a holomorphic unit at the origin. This also holds for negative (m), interpreted meromorphically. Since (F\circ\pi) is (\mu_k)-invariant,
[
 u^m e(u,v)=\zeta^m u^m e(\zeta u,\zeta^{-1}v).
]
Cancel (u^m) as meromorphic germs and evaluate at the origin. Since (e(0)\ne0), one obtains (\zeta^m=1), hence (k\mid m). Conversely (m=k\ell) makes (mD=\operatorname{div}(x^\ell)) for any (\ell\in\mathbf Z). This proves the exact index.

The proof distinguishes the **geometric divisor** (D), the Cartier condition on a *cycle*, and the possible principal multiple. It does not rely on Demailly approximation, Bergman estimates, (L^2), Ohsawa–Takegoshi, or smoothing programmes.

## Consequences, references and limitations

This family gives a sharp complementary contrast to printed Example 20.6.5: that example is a threefold quadric with a non-Cartier Weil divisor; here every (k\ge2) gives a **normal isolated surface singularity** with an arbitrarily large finite Cartier index. It explicitly demonstrates why Proposition 20.6.4 limits the universal Weil-to-Cartier assertion to **smooth** complex manifolds. No existing printed result is refuted. One possible future *proposed* expository addition after Example 20.6.5 is the family above and the distinction between Weil, Cartier and (\mathbf Q)-Cartier.

Downstream claims in §§20.1 (divisorial/b-divisor pullbacks), 20.7 (meromorphic sections and divisor classes), and 20.8 (restricted volumes) should retain their own hypotheses whenever a Weil cycle is converted to a Cartier object. **No downstream theorem is labelled false by this example**; none of those full proofs was reverified in this pass. The local factoriality input for the smooth cover and the quotient-germ identification are explicitly stated/proved above, but the general sheaf-of-cycles and proper-image chains are not transitively certified.

## Actual coverage and exclusions

Directly inspected integrated §20.6.2–5 including proof paragraphs on lines 13–25, 28–43 and 46–75; new cyclic quotient model and exact local index established. Section 20.6 was previously partially audited: **0 first-time numbered sections, 0 whole-section certifications**. Current generated main ToC independently counted as **25 chapters and 747 numbered sections** using `docs/chapters/index.html` (blob `c0c07abf4d8f7575b54cff2ec694fcf987f51cf8`). No project-wide software build/tests, CI, formal verification, or website publication was performed. All user-excluded approximation/regularization and dedicated Bergman, (L^2), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof work remains **deferred-by-user**, neither resolved nor certified.
