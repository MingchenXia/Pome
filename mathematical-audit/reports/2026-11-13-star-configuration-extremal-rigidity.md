# Extremal-degree rigidity for projective hyperplane star configurations

**Date:** 2026-11-13  
**Finding:** `POME-STAR-EXTREMAL-RIGIDITY-001`  
**Severity:** low  
**Status:** verified conditional deduction (new strengthening, **not** a false printed theorem or a claimed full-section certificate)  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`

## Exact integrated targets and provenance

- `docs/sections/projective-vanishing-degree-configurations/index.html`, blob `8c1603d341f3dc45bf5c7124e396e9f1e8eb235c`, Theorem **9.69.2**, source label `demailly-complex-geometry:84AEA91E`, permanent tag `FB7CD3CDDE23`, physical lines **7–17** (statement) and **19–43** (integrated proof); particularly the hyperplane restriction step in **22–24**, multiplicity induction in **26–40**, and the distinct-factor divisibility argument in **24**.
- `docs/sections/entire-function-growth-and-algebraic-zero-sets--refined-bounds-for-simultaneous-vanishing-orders/index.html`, blob `8ff4e22eede7fe72ba7bbceeb221ef8b2ed20cf7`, Definition **9.56.1**, source `demailly-complex-geometry:4C4F1642`, permanent tag `145E38D5855C`, physical lines **10–20**, defining the minimum simultaneous vanishing degree `omega_t(S)`.
- This review uses the actual printed general-position assumptions, not the source theorem number as a surrogate for hypotheses.

## Exact new result

Let `n>=1`, `N>=n`, and let `H_1,...,H_N` be hyperplanes in general position in `P^n`, with linear equations `ell_i`. Let `S` be their set of `n`-fold intersection points. For `t>=1`, let

[
W_t(S)={Fin H^0(mathbf P^n,mathcal O(omega_t(S))):operatorname{ord}_p Fge tquadorall pin S}.
]

(The zero section is included in this vector space; `omega_t` is the minimum degree of a **nonzero** section.) Set `P=ell_1...ell_N`.

**Rigidity theorem.** If `N>n`, then for every `q>=1`,

[
oxed{W_{qn}(S)=mathbf C P^q.}
]

Moreover, if `n>=2` and `N>n`, then

[
oxed{dim_mathbf C W_t(S)=1quadLongleftrightarrowquad nmid t.}
]

If `N=n`, then `S` consists of a single point, `omega_t(S)=t`, and

[
dim_mathbf C W_t(S)=inom{t+n-1}{n-1}.
]

Thus the condition `N>n` for rigidity is sharp when `n>=2`. When `n=1`, the unique minimal-degree polynomial is, for every `N>=1` and `t>=1`, a scalar multiple of `P^t`.

## Complete proof of the new rigidity statement

For `n=1`, `S` is a collection of `N` distinct projective points. A degree-`Nt` binary form vanishing to order at least `t` at every point has all `ell_i^t` as factors, so is a scalar multiple of `P^t`.

Assume `n>=2`, `N>n`, and `q>=1`. The product `P^q` has degree `qN` and order exactly `qn` at every point of `S`. The printed lower bound in Theorem 9.69.2 gives `omega_{qn}(S)>=N(qn)/n=qN`, so `omega_{qn}(S)=qN`. Let `F` be any nonzero form of degree `qN` vanishing to order at least `qn` at all points of `S`.

If some `ell_i` did not divide `F`, its restriction `F|_{H_i}` would be a nonzero form of the same degree on `H_i ≅ P^{n-1}`. It would vanish to order at least `qn` at the star configuration of `N-1` hyperplanes `H_j∩H_i` in `H_i`. Applying the **printed** lower bound of Theorem 9.69.2 in dimension `n-1` gives

[
qN=deg F gerac{(N-1)qn}{n-1}
=qN+rac{q(N-n)}{n-1}>qN,
]

a contradiction. Therefore **every** `ell_i` divides `F`. Distinct linear forms are pairwise nonassociate primes in the homogeneous polynomial UFD, hence `P` divides `F`. Exactly `n` of the hyperplanes pass through each point of `S`, so `F/P` has degree `(q-1)N` and order at least `(q-1)n` at all of `S`. Induction on `q`, starting at `q=0` (constant forms), yields `F=cP^q`. This argument applies uniformly to `N=n+1`, with no generic coefficients beyond the stated hyperplane position.

To prove nonrigidity when `t` is not a multiple of `n`, write `t=qn+r`, `q>=0`, `1<=r<n`. The **previously established** exact minimum-degree formula (a separate historical audit result, **not claimed as a new discovery here**) is

[
omega_t(S)=t+(N-n)lceil t/nceil
=qN+(N-n+r).
]

For completeness its lower bound follows by the same double induction used by the printed proof: if a degree-`D` admissible form is not divisible by an `ell_i`, restriction to `H_i` gives

[
Dge t+(N-n)lceil t/(n-1)ceil
 ge t+(N-n)lceil t/nceil;
]

if all `ell_i` divide it, remove `P`, reducing both degree by `N` and order by `n` (if `t<=n`, the degree is already at least `N`). The base `n=1` is root counting. The matching upper bound uses `P^q` times any product of `N-n+r` distinct hyperplane equations.

Choose two **different** subsets `J,J'⊂{1,...,N}`, each of cardinality `N-n+r`, which is between `1` and `N-1`. The distinct products

[
P^qprod_{jin J}ell_j,qquad P^qprod_{jin J'}ell_j
]

have the minimum degree and vanish to order at least `qn+r` at every `n`-fold intersection, since an `n`-element incident set meets `J` in at least `r` elements. They are not scalar multiples (unique factorization), and therefore `dim W_t>=2`. Together with rigidity for `n|t`, this is the stated iff.

For `N=n`, the `n` independent hyperplanes meet at exactly one point. In coordinates taking it to `[1:0:...:0]`, a degree-`t` form has order at least `t` there exactly when it is a homogeneous polynomial of degree `t` in `x_1,...,x_n`. This vector space has dimension `binom(t+n-1,n-1)`, completing the boundary case.

## Classification and dependency impact

**Status:** verified conditional deduction; the printed Theorem 9.69.2 and Definition 9.56.1 are **not erroneous**. The new result classifies **the dimension-one property of the extremal-degree symbolic linear system**, not merely its initial degree or asymptotic Waldschmidt constant. In particular, minimal-degree forms are forced to contain the *entire* star divisor for multiplicities divisible by the ambient dimension, an assertion stronger than the numerical bound in the source.

**External inputs:** none beyond elementary homogeneous polynomial unique factorization, restriction of vanishing orders, and the printed theorem's dimension-induction estimate, whose relevant portion was checked directly. We do not invoke the excluded regularization programme. The auxiliary exact-`omega_t` formula was already present in the historical audit and is clearly identified as such.

**Affected dependents:** future statements concerning symbolic powers or extremal sections for hyperplane star configurations in chapter 9; no change to existing production theorem statements, permanent labels, canonicalization or references is proposed.

**Correction proposed:** none required. A separately reviewable optional corollary could be placed after Theorem 9.69.2, with the full proof above. No source/body edit is made by this audit.

## Scope and verification

Read the integrated displayed proof of **9.69.2**, with **9.56.1** for conventions. The project has **25 chapters and 747 numbered sections** in the reviewed ToC. Section 9.69 was already partially sampled in historical audit entries; this is **0 additional first-visited numbered sections and 0 whole-section/whole-project certificates**. No website/build/test/CI run, no code or production changes, and no broad mathematical verification claim. The user's excluded Demailly approximation/regularization and dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remains **deferred-by-user**, not resolved.
