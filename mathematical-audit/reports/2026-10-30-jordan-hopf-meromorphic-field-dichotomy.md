# Mathematical audit: meromorphic-function fields of triangular Hopf quotients

**Date:** 2026-10-30. **Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Review branch:** `review/mathematical-audit`. This is a selected new mathematical deduction, not a verification of the full printed dependency chain or a claim that any printed theorem is false.

## Source anchors and scope

- `docs/sections/contracting-hopf-quotients/index.html`, production blob `d09d9bac3785b78b557ff5178ad7a52b34b20dac`: §23.3.2–3, source `demailly-complex-geometry:371996B7`, permanent theorem tag `D81E3145A1B4`; hypotheses and conclusion at **physical lines 9–22**, proof at **26–52**, triangular iteration Eq. 23.3.4 permanent tag `436562DE848D` at **29–33**. The printed theorem asserts compactness, fundamental group and non-Kählerness, *not* algebraic dimension.
- `docs/sections/projective-hartogs-extension/index.html`, production blob `3191443b49a20377356f519b5e98ec29259f1c7c`: §9.72.1, source `cao-paun-foliations:FF53288F`, permanent lemma tag `0A2146B324EB`, statement **line 9**, proof **lines 12–18**. Its internal input, the normal meromorphic codimension-two extension theorem (tag `F35BA7139EC4`), is treated as **conditional**, not newly proved or independently certified here.
- Previously logged `POME-HOPF-TRIANGULAR-LINEARIZATION` observation for `p>=2` is reused; it is *not* repeated as a new finding. Previously logged smooth-topology conclusions are also unchanged. The source identifier's occurrence of “Demailly” is a bibliographical book label; **no Demailly regularization/approximation or dedicated excluded analytic programme was inspected**.

## POME-HOPF-JORDAN-MEROMORPHIC-FIELD-001

**Severity:** low. **Status:** verified conditional deduction (conditional only on the stated §9.72.1 meromorphic extension input). Neither a false printed theorem nor a claimed proof repair.

**Claim.** Let `0<|lambda|<1`, `p` a positive integer, and let

```text
F_p(z,w) = (lambda*z, lambda*w + z^p),
X_p = (C^2 \ {0}) / <F_p>.
```

Theorem 23.3.3 ensures that `X_p` is a compact complex surface. Its meromorphic-function field is

```text
M(X_1) = C.
M(X_p) = C(T_p)  for every p >= 2,
T_p(z,w) = (w + z^p/(lambda-lambda^p))/z.
```

Consequently the **algebraic dimension** is precisely zero in the linear Jordan case `p=1`, and precisely one for every `p>=2`. These statements concern the concrete triangular family, not arbitrary Hopf surfaces, and do not imply that the `p=1` and `p>=2` manifolds are non-diffeomorphic.

**Proof, part I: reduce to meromorphic germs.** A meromorphic function `f` on the quotient pulls back to an `F_p`-invariant meromorphic function on `C^2\{0}`. By §9.72.1 with `A={0}` and target `P^1`, it extends *meromorphically* across the origin; denote its germ by `f=g/h`, where `g,h` are nonzero holomorphic germs. Conversely, an invariant meromorphic function on the punctured space descends by the quotient covering in §23.3.3.

Write `d=ord_0(g)`, `e=ord_0(h)`, and `G_d,H_e` for their nonzero lowest homogeneous parts. The initial homogeneous rational function `R=G_d/H_e` has degree `k=d-e`. When the germ is invariant under a **linear** contraction `F`, the identity `g(F)h=g h(F)` at lowest total degree implies `R(F(z,w))=R(z,w)`.

**Part II: the linear Jordan case `p=1`.** On `z!=0`, any rational homogeneous `R` of integer degree `k` has the shape `z^k r(t)` with `t=w/z` and `r` a nonzero rational function in one variable. Here `F_1` sends `z` to `lambda*z` and `t` to `t+1/lambda`, so invariance gives

```text
lambda^k r(t+1/lambda) = r(t).
```

A nonzero rational function satisfies `r(t+c)/r(t) -> 1` at infinity for every fixed nonzero `c`; hence `lambda^k=1`. Because `0<|lambda|<1`, `k=0`. A rational function invariant under a nonzero translation is constant: otherwise a finite pole produces infinitely many translated poles, and a nonconstant polynomial cannot be periodic. Thus **every nonzero invariant meromorphic germ has homogeneous degree zero and constant initial rational function `R=C`.** For an invariant nonconstant germ `f`, subtract this constant `C`. The resulting invariant germ is either zero or has numerator `g-Ch` with order strictly greater than `e=d`, so its initial rational function has strictly positive homogeneous degree. This contradicts the preceding conclusion. Therefore `f` is constant. Analytic continuation on the connected punctured space gives `M(X_1)=C`.

**Part III: the nonlinear cases `p>=2`.** Set `c=1/(lambda-lambda^p)`, a well-defined constant because `0<|lambda|<1`. The global polynomial automorphism `H(z,w)=(z,w+c z^p)` fixes zero and satisfies, by direct substitution,

```text
H(F_p(z,w))
 = (lambda*z, lambda*w+(1+c*lambda^p)*z^p)
 = (lambda*z, lambda*(w+c*z^p))
 = (lambda*Id)(H(z,w)).
```

Thus `X_p` is biholomorphic to the scalar Hopf quotient of `(lambda z,lambda w)`. For this scalar map, the initial homogeneous rational function `R` of any invariant meromorphic germ satisfies `lambda^{d-e}R=R`, hence `d=e` and `R` is homogeneous of degree zero. Every such rational function is a rational function of `w/z`. Since `R` itself is invariant, `f-R`, if nonzero, would have initial homogeneous degree strictly positive; scalar invariance forbids this. Hence `f=R`, and **every** invariant meromorphic function is rational in `w/z`. Conversely all rational functions of `w/z` descend, so the scalar quotient's field is precisely `C(w/z)`. Transporting it by `H` proves `M(X_p)=C(T_p)`. Since `T_p` is nonconstant, its transcendence degree is one. QED.

**Mathematical adjudication and proposed placement.** Theorem 23.3.3 is **correct in the tested family**; the stronger field calculation is an optional corollary after it, retaining its original book attribution and permanent tag. The proof is self-contained modulo the specific §9.72.1 meromorphic Hartogs extension, which is *recorded as an internal dependency*, not certified here; it does not invoke the user-excluded approximation programme. The result sharpens the distinction between conjugate scalar and Jordan triangular dynamics; relevant dependents include §§9.67, 9.72 and the algebraic-reduction interpretation of §23.3. It does not assert full classification of diagonal contractions or of general non-Kähler surfaces.

## Additional selected checks and coverage

- Directly read the full integrated §23.3.3 statement and proof including contraction, proper discontinuity, quotient compactness, fundamental group, Betti-number argument and exact triangular iteration. The printed results were **not** found false in this pass; no full certification of all topological inputs.
- Inspected the §9.72.1 meromorphic-extension statement and named internal dependency (statement/anchor only); that dependency **was not independently proved**.
- Read §§23.2.14–17 and 23.2.20, 23.2.25–29 as context and checked their formulas and proof structure only; **no new claim about them**, no previous finding re-registered. §8.13.4–8.13.8 selected comparisons and §21.7–10 toric calculations were likewise context/prior-findings crosschecks only.
- The extant table-of-contents inventory remains **25 chapters / 747 unique numbered sections / zero entire-section certifications**. This audit is selective and does not certify all of chapter 23 or the Hartogs extension chain.

**Deferred-by-user:** all Demailly approximation/regularization and their dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion items retain that exact status, not resolved. No main/source/body/registry/canonicalization/tag/site change, no CI, build, publication, paid service or formal verification. No test run is claimed.
