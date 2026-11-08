# 9 November 2026 — finite germs with a fixed quadratic jet and unbounded degree

## Version and exact scope

- **Finding:** POME-FINITE-GERM-FIXED-JET-UNBOUNDED-DEGREE-001.
- **Severity / status:** low / **verified conditional deduction** (sharp boundary example). **No printed proposition or lemma is false.**
- **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
- **Primary integrated edition:** docs/sections/lelong-densities-generalized-masses-and-multiplicity--finite-germs-and-their-actual-integer-degree/index.html, blob e2a86c5438c7770a8766f6bedf779e1879ead4c0. Proposition 6.43.1, original source label demailly-complex-geometry:F459CB6C, permanent tag AD7655D0958A, physical lines 8–32. Lemma 6.43.2, original source label demailly-complex-geometry:E27EA362, permanent tag B1AA1442D441, physical lines 38–54.
- **Contextual cross-check:** docs/sections/lelong-densities-generalized-masses-and-multiplicity--monomial-maps-and-the-sharp-directional-comparison/index.html, blob bad5cd9bb63a90871462700f5c1f7080c597ee99; Proposition 6.47.1, original demailly-complex-geometry:F608EF8B, permanent tag 0A17C5BE0625, physical lines 8–28. The classical proper divisor product in Theorem 20.5.10, permanent tag DDB973C0C1DD, is used only for the displayed local intersection.
- §§6.43 and 6.47 had already received **selected** earlier audits (22 and 25 October); this is new mathematical content but **not a first section visit or a section certification**.
- Exclude entirely the owner-deferred Demailly regularization, Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme. None of that programme is used here.

## Claim and exact calculation

For each integer \(k\geq3\), consider the plane holomorphic germ
\[
H_k:(\mathbb C^2,0)\longrightarrow(\mathbb C^2,0),
\qquad H_k(x,y)=\bigl(x^2,\;xy+y^k\bigr).
\]
Its common zero set is exactly \(\{(0,0)\}\) as a germ, because \(x^2=0\) forces \(x=0\), and then \(y^k=0\). Thus it is finite at the origin and satisfies the **actual** hypotheses of Proposition 6.43.1 and Lemma 6.43.2.

All these finite germs have the **same 2-jet**
\[
j^2H_k=(x^2,xy),
\]
and each coordinate function has vanishing order precisely 2, independent of \(k\). Nonetheless their local mapping degrees, equivalently their retained classical Monge–Ampère pole masses, are
\[
\boxed{\quad d(H_k,0)=
 \bigl((dd^c\log|H_k|^2)^2\bigr)(\{0\})=2k.\quad}
\]
Consequently \(d(H_k,0)/(\operatorname{ord}_0H_{k,1}\operatorname{ord}_0H_{k,2})=k/2\) is unbounded as \(k\to\infty\). The printed theorem gives an integer; it **does not** claim that this integer is determined by low-order Taylor data or by the individual vanishing orders. This example rules out those tempting, unprinted strengthenings.

### Direct proper divisor-intersection proof

Using the normalization \(dd^c=i\partial\bar\partial/(2\pi)\), Poincaré–Lelong gives
\[
dd^c\log|x^2|^2=2[x=0],\qquad
dd^c\log|xy+y^k|^2=[y=0]+[x+y^{k-1}=0].
\]
The two divisor intersections with \([x=0]\) are proper at the origin. The first has intersection multiplicity 1. The second has multiplicity \(k-1\), since on \(x=0\) its defining function is \(y^{k-1}\). Hence
\[
dd^c\log|x^2|^2\wedge dd^c\log|xy+y^k|^2
 =2(1+k-1)[0]=2k[0].
\]
Lemma 6.43.2 identifies this coefficient with \(d(H_k,0)\). This local computation has no need for regularization of singular Hermitian metrics and uses **classical** proper divisor intersection, not the non-pluripolar product (which would discard these atoms).

### Independent generic-sheet check

For a generic small target value \((a,b)\) with \(a\neq0\), the equation \(x^2=a\) has two distinct small roots \(x_\pm=\pm\sqrt a\). For either fixed \(x_\pm\), the second equation is
\[
y^k+x_\pm y-b=0.
\]
Choose a small fixed disk \(|y|<r\). For all sufficiently small \(a,b\), Rouché's theorem on \(|y|=r\) gives precisely \(k\) roots counted with multiplicity, since \(|x_\pm|r+|b|<r^k\). Generic \((a,b)\) makes the discriminants nonzero, hence there are \(2k\) distinct points in the source bidisk. The map has no zeros on the chosen bidisk boundary for small enough target values, so this is the actual generic local sheet number, independently confirming the intersection calculation.

### Optional local-algebra check

In the local analytic algebra \(A_k=\mathbb C\{x,y\}/(x^2,xy+y^k)\), the relations \(xy=-y^k\) and \(x^2=0\) imply \(y^{2k-1}=0\). A Gröbner calculation (lexicographic order \(x>y\)) has leading monomials \(x^2,xy,y^{2k-1}\), leaving the \(2k\) standard monomials
\[
1,y,\ldots,y^{2k-2},x.
\]
Thus \(\dim_{\mathbb C}A_k=2k\), a third independent computation. This algebra check is not needed to establish the divisor intersection or the generic sheet number.

## Mathematical interpretation and dependency status

- **Printed Proposition 6.43.1 and Lemma 6.43.2 remain correct** in the inspected case; the example is a positive test of their local degree/intersection normalization.
- The initial quadratic forms \((x^2,xy)\) have a non-isolated common zero set. Consequently, higher Taylor terms can change the isolated intersection multiplicity dramatically, even without altering the quadratic jet. An equality with the product of individual orders would need an extra condition, e.g. proper intersection already at the leading homogeneous level. No such claim appears in the integrated lemma.
- This is **not** the earlier diagonal monomial multiplicity interval finding POME-MONOMIAL-MULTIPLICITY-INTERVAL-001: here both component orders and the complete quadratic jet are fixed, while the actual two-dimensional sheet degree is unbounded.
- **Proposed correction:** no correction to a printed mathematical statement. Optionally add a separately tagged Example immediately following Lemma 6.43.2 to prevent erroneous finite-jet/product-of-orders inference. Preserve both original source labels, attribution and permanent tags.
- **Affected dependents:** applications of finite-germ degree and proper divisor intersection, including §6.47 and finite-map multiplicity comparisons, only if they attempt to substitute a product of vanishing orders for the actual isolated intersection degree. No currently printed dependent is shown false.
- **Unresolved:** the general analytic product/weight-comparison and proper-image dependency chains are not certified here. No unrelated theorem, full section or full chapter is certified.
