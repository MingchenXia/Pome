# Sharp bounded-Lipschitz stability for local Bedford--Taylor products

**Finding ID:** `POME-BT-UNIFORM-BL-SQRT-SHARP-001`  
**Date:** 2026-11-14  
**Status:** verified conditional deduction (not an error in the printed theorem)  
**Severity:** low  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`  
**Audit branch:** `review/mathematical-audit`

## Source-anchored reading

The integrated reading edition, rather than a secondary source theorem number, was checked at these exact blobs and physical lines:

| Integrated file on main | Blob | Selected passage / source label / permanent tag |
|---|---|---|
| `docs/sections/bedford-taylor-products-and-local-capacity--bounded-potentials-and-recursive-products/index.html` | `18bd2395f3b76941b2c677079c09eb6accc5a9cb` | Definition 7.2.1, lines 16--25, `foundations-of-pluripotential-theory:DE7531DE`, `254CDCCCAB5E` |
| same | same | Proposition 7.2.2, lines 29--77, `foundations-of-pluripotential-theory:D16BD033`, `D9911E035563` |
| same | same | CLN Theorem 7.2.5, lines 98--119, `foundations-of-pluripotential-theory:103AB333`, `2A84C325AB58` |
| same | same | Proposition 7.2.6, lines 125--155, `foundations-of-pluripotential-theory:C5608495`, `2F39A3F97E8E` |
| `docs/sections/bedford-taylor-products-and-local-capacity--decreasing-continuity-and-symmetry/index.html` | `96a9e39e85fab5774ebdac0c6d9d006338a4e42c` | Theorem 7.3.7, statement lines 132--139 and symmetry argument beginning line 148, `foundations-of-pluripotential-theory:8B1F9B78`, `D87C13B3250A` |

The printed Proposition 7.2.6 asserts qualitative weak convergence for locally uniformly convergent potentials and weakly converging positive currents; it does **not** assert a quantitative rate for a varying underlying current. Here the underlying positive current is **fixed** and all potential perturbations are uniformly bounded on a common neighborhood.

## New quantitative deduction

Let `Omega` be open in `C^n`, let `T` be a positive closed current of bidimension `(r,r)`, and fix `1 <= q <= r <= n`. Choose compact sets `K subset Int(L') subset L' subset Int(L) subset Omega`. For `j=1,...,q` let `u_j,v_j` be locally bounded plurisubharmonic functions on `Omega`, and assume on `L`
[
 |u_j|,|v_j|le M,qquad |u_j-v_j|ledelta,qquad Mge1,quad 0ledeltale M.
]
Use the Euclidean Kähler form `beta=(i/2)sum dz_j wedge dbar z_j` and define positive trace measures
[
 mu_{oldsymbol u}
 = (dd^cu_1wedgecdotswedge dd^cu_qwedge T)
      wedge{eta^{r-q}over(r-q)!},
 qquad mu_{oldsymbol v} 	ext{analogously}.
]
The `dd^c=i/(2 pi) partial bar-partial` normalization is that of §7.2.

There is a constant `C=C(K,L,n,r,q)`, independent of the potentials, `T`, `M`, and `delta`, such that for every compactly supported real `C^2` test function `f` supported in `K`,
[
 left|int f,d(mu_{oldsymbol u}-mu_{oldsymbol v})ight|
 le C,|T|_L M^{q-1}delta,|D^2f|_infty. 	ag{A}
]
For every compactly supported Lipschitz test `f` supported in `K` with `|f|_infty+operatorname{Lip}(f)le1`, one has
[
 left|int f,d(mu_{oldsymbol u}-mu_{oldsymbol v})ight|
 le C,|T|_L M^{q-1/2}sqrtdelta. 	ag{B}
]
If `delta=0`, both differences vanish identically. The exponent `1/2` in (B) is **uniformly optimal**, already for smooth strictly psh functions on a fixed domain in one complex dimension. The linear exponent in (A) is likewise optimal.

### Proof of (A): one factor at a time

Write
[
 S_j=(dd^cu_1)wedgecdotswedge(dd^cu_{j-1})
       wedge(dd^cv_{j+1})wedgecdotswedge(dd^cv_q)wedge T
]
with the positive closed Bedford--Taylor product interpreted using the symmetry of Theorem 7.3.7. Multilinearity and the recursion in Definition 7.2.1 give the **identity of signed currents**
[
 mu_{oldsymbol u}-mu_{oldsymbol v}
 =sum_{j=1}^q dd^cig((u_j-v_j)S_jig)
      wedge{eta^{r-q}over(r-q)!}. 	ag{C}
]
The signed multiplication is unambiguous because the factors are bounded Borel functions on each compact neighborhood and `S_j` is an order-zero positive current. The smooth form `beta` is closed. Test (C) against `f` and integrate by parts:
[
 int f,d(mu_{oldsymbol u}-mu_{oldsymbol v})
 =sum_jint (u_j-v_j)S_jwedge
       dd^c fwedge{eta^{r-q}over(r-q)!}. 	ag{D}
]
Since the coefficient measures of a positive current are controlled by its trace mass, the absolute value of each summand is at most `C delta |D^2f|_infty |S_j|_{L'}`. The CLN estimate, Theorem 7.2.5, applied with `q-1` locally bounded psh factors and the compact pair `L' subset Int(L)`, gives
[
 |S_j|_{L'}le C_{L',L,n,r,q},|T|_L M^{q-1}.
]
Summing proves (A). In particular, no unproved interchange of Bedford--Taylor limits is used in the new estimate; the only substantive inputs are the *already printed* symmetry/positivity and CLN bounds.

### Proof of (B): one derivative gained by smoothing the test

Extend a test `f` from (B) by zero, and convolve with a fixed nonnegative smooth unit-mass mollifier of radius `h`. For `h` below the fixed separation of `K` and `Omega\setminus Int(L')`, the smooth `f_h` is supported in `L'` and obeys
[
 |f-f_h|_inftyle C h,qquad
 |D^2f_h|_inftyle C/h.
]
The same CLN bound gives
[
 mu_{oldsymbol u}(L')+mu_{oldsymbol v}(L')
 le C|T|_L M^q.
]
Apply (A), with support moved from `K` to the fixed `L'`, to `f_h`, and bound the approximation error using the two positive masses:
[
 left|int f,d(mu_{oldsymbol u}-mu_{oldsymbol v})ight|
 le C|T|_Lleft(M^{q-1}{deltaover h}+M^q hight).
]
Choose `h=asqrt{delta/M}` with a fixed small geometric `a>0` ensuring the support condition. This gives (B). For `delta=0`, identity (C) immediately gives zero.

### Sharpness on a smooth one-dimensional model

Work on `Omega=C`, set `n=r=q=1`, `T=1`, and write `z=x+iy`. Fix `0<a<4`. For integers `k>=1`, put
[
 v(z)=|z|^2,qquad
 u_k(z)=|z|^2+{aover k^2}cos(kx),qquad
 delta_k={aover k^2}.
]
Both potentials are smooth and strictly psh since
[
 (u_k)_{zar z}=1-{aover4}cos(kx)>0.
]
Their exact Bedford--Taylor density difference, with the stated `dd^c` normalization, is
[
 dd^c u_k-dd^c v=-{aover4pi}cos(kx),dx,dy. 	ag{E}
]
Choose a nonnegative nonzero `hoin C_c^infty(C)`, whose support lies in a fixed compact `K`, and set `f_k(z)=ho(z)cos(kx)/(C_0 k)`, where `C_0` is a fixed constant large enough for `|f_k|_infty+operatorname{Lip}(f_k)le1` for all `k`. Then (E) and the Riemann--Lebesgue lemma give
[
 left|int f_k,d(dd^cu_k-dd^cv)ight|
 = {aover4pi C_0k}intho(z)cos^2(kx),dx,dy
 = {aover8pi C_0k}intho,dx,dy+o(k^{-1}).
]
Thus the bounded-Lipschitz discrepancy is bounded below by `c/k=c'sqrt{delta_k}` for this fixed compact set. A stronger universal exponent than `1/2` in (B) is impossible even for smooth strictly psh functions. The same density difference has nonvanishing local total variation; that fact is **not counted as a new general TV counterexample**, since prior audits already recorded a different uniform-psh/TV phenomenon.

To see sharpness of (A), take a fixed nonconstant real `g in C_c^infty(C)`, `v=|z|^2`, and `u_t=v+t g` for sufficiently small positive `t`, so both remain strictly psh. Using the fixed `C^2` test `f=g`, exact integration by parts gives
[
 int g,d(dd^cu_t-dd^cv)
   =-{tover4pi}int_{mathbf C}|
abla g|^2,dx,dy
eq0.
]
This is order `t`, and `|u_t-v|_infty=t|g|_infty`.

## Classification, correction, and dependency boundary

* **Verified conditional deduction, low severity.** Proposition 7.2.6 is correct on the audited point; its qualitative weak convergence does not state a rate. The new result is a possible *optional quantitative corollary*, not a source correction or evidence of a false theorem.
* **Exact dependencies:** Definition 7.2.1 and Proposition 7.2.2 (bounded-product recursion and positivity); Theorem 7.2.5 (CLN mass bounds); Theorem 7.3.7 (symmetry). Their complete upstream proof chains were **not** independently recertified by this audit; these are printed internal inputs. The smooth model calculation is independent of those deep inputs.
* **Affected dependents:** any use of §7.2.6 with a fixed base current and uniform local potential errors, including compactly supported smooth or Lipschitz trace tests. The bound **does not** give a rate when `T_k	o T` is merely weak, nor imply total-variation convergence, nor handle unbounded singular potentials.
* **Proposed optional addition:** state (A)--(B) after Proposition 7.2.6 with the fixed-`T`, uniform-bound, compact-neighborhood hypotheses, and explicitly retain the distinction from its variable-`T_k` statement. Do not alter source labels, canonical variants, or numbering.
* **Excluded work:** Demailly approximation/regularization and the dedicated Bergman, `L^2`, Ohsawa--Takegoshi, multiscale-atlas and positivity-loss proof programme remain **deferred-by-user**. This note uses only basic local Bedford--Taylor products and does not reopen that programme.

## Actual coverage and verification

This session directly examined the integrated §7.2 Definition/Proposition/Theorem passages and the selected §7.3.7 symmetry statement and initial proof, with the stable anchors above. It did **not** certify all of §7.2 or §7.3, their upstream dependencies, or any complete chapter. These numbered sections were previously partly examined: **0 new first-visited sections, 0 complete-section certifications**, actual current navigation **25 chapters / 747 unique numbered sections**. A separate exploratory numerical quadrature checked the predicted `k`-scaled pairing for `k=10,20,40,80`; this is *not* a project test or mathematical proof. No build, CI, website publication, or source/body/registry/permanent-tag edits were performed.
