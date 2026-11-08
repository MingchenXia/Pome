# Mathematical audit — connected nonconvex fibers defeat a strictly plurisubharmonic Kiselman infimum

**Date:** 2026-11-09 (Asia/Shanghai).  
**Production main reviewed:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Audit branch pre-write commit:** \`5515c3ea8aa7f4feb59c1b42c4d0d369acc0b1e8\`.  
**Exact integrated reading edition:** \`docs/sections/plurisubharmonic-functions--kiselman-s-minimum-principle/index.html\`; blob \`e26179ee7cbb45fe10f7b4aabb9057ca33739a87\`, 140 physical lines.

**Finding ID:** \`POME-KISELMAN-NONCONVEX-CONNECTED-TUBE-001\`.  
**Severity:** low. **Status:** **verified conditional deduction** (sharpness counterexample to a *hypothetical weakened hypothesis*; **not** a false printed theorem, a repair of its proof, or a claim of transitive proof certification).

## Mathematically identifiable source and scope

- **Corollary 5.12.2**, source label \`foundations-of-pluripotential-theory:B6D5E591\`, permanent tag \`2C1A82803889\`, physical **lines 99–105**. Its printed product-tube hypothesis explicitly requires a nonempty **open convex** real set \`V\`; it concludes that an imaginary-translation-invariant plurisubharmonic \`u\` has a plurisubharmonic or identically \`-infinity\` fiber infimum, and permits subtracting any real affine functional.
- **Theorem 5.12.1**, source label \`foundations-of-pluripotential-theory:90492B74\`, permanent tag \`1F87EF4FCF69\`, physical **lines 20–28**: *both* convex real fibers and a proper invariant plurisubharmonic exhaustion are assumed. Its smooth Schur-complement step is visible at lines 33–62. We check these hypotheses to avoid an invalid inference from the corollary.
- **Section 5.12**, permanent tag \`53A48113C242\`, original section tag \`foundations-of-pluripotential-theory:12F6C9C4\`, integrated physical lines 5–16 define the fiber/translation conventions. Previously selected §5.12 proof checks remain in the durable matrix; no first visit is claimed here.

## Explicit strictly PSH counterexample with a connected real fiber

Let
\[
 D=\{z\in\mathbb C:|z|<1/4\},\qquad
 V=\{t\in\mathbb R^2:1<|t|<2\}.
\]
Then \`V\` is **bounded, connected, open, and has smooth boundary**, but it is **not convex**. Put \(\Omega=D\times(V+\mathrm i\mathbb R^2)\). This is a **connected** domain invariant under arbitrary imaginary translations in the last two complex coordinates. For \(w=(w_1,w_2)\), let \(t=(\operatorname{Re}w_1,\operatorname{Re}w_2)\) and \(a(z)=(\operatorname{Re}z,\operatorname{Im}z)\). Define
\[
 u(z,w)=|t-a(z)|^2+|z|^2+|t|^2
       =[\operatorname{Re}(w_1-z)]^2
        +[\operatorname{Re}(w_2+\mathrm iz)]^2
        +|z|^2+(\operatorname{Re}w_1)^2+(\operatorname{Re}w_2)^2.
\]
The function is smooth and independent of \(\operatorname{Im}w_j\). For tangent \((\xi,\eta_1,\eta_2)\in\mathbb C^3\), its Levi form, using the standard \(\partial\bar\partial\) convention, is **exactly**
\[
 \mathcal L_u(\xi,\eta_1,\eta_2)
 =\tfrac12|\eta_1-\xi|^2
  +\tfrac12|\eta_2+\mathrm i\xi|^2
  +|\xi|^2+\tfrac12(|\eta_1|^2+|\eta_2|^2).
\]
It is strictly positive for every nonzero tangent vector (the \(|\xi|^2\) and \(|\eta_j|^2\) terms already force this). Thus \(u\) is **globally smooth and strictly plurisubharmonic** on the connected tube; the failure below cannot be blamed on weak regularity or a disconnected fiber.

For \(r=|z|<1/4\), the fiberwise expression is
\[
 u(z,t)=2|t|^2-2\,a(z)\cdot t+2r^2.
\]
For each fixed \(\rho=|t|\in(1,2)\), the smallest dot-product term is \(-2r\rho\), attained by orienting \(t\) parallel to \(a(z)\) when \(z\ne0\). Hence
\[
 \inf_{\substack{t\in V\\|t|=\rho}}u(z,t)
       =2\rho^2-2r\rho+2r^2.
\]
The derivative with respect to \(\rho\) is \(4\rho-2r>0\) for \(\rho>1\), so the infimum over the open annulus is approached as \(\rho\downarrow1\):
\[
 \boxed{\,v(z):=\inf_{t\in V}u(z,t)=2-2|z|+2|z|^2.\,}
\]
The formula also holds at \(z=0\) (any angular direction has the same infimum). In particular \(v\) is finite and continuous, **not identically \(-\infty\)**.

The value \(v(0)=2\) is a **strict local maximum**: for \(0<|z|<1/4\), \(v(z)=2-2r+2r^2<2\). Consequently \(v\) cannot be subharmonic, hence is not plurisubharmonic. Independently, away from \(z=0\) the classical radial Laplacian gives
\[
 \Delta v(r)=v''(r)+\frac{v'(r)}{r}
           =8-\frac2r<0\qquad(0<r<1/4).
\]
Thus a smooth strictly PSH function on a **single connected tube with a connected smooth real fiber** can have a non-subharmonic fiberwise infimum. The nonattainment of the infimum on an open annulus does not invalidate the model: the printed corollary explicitly takes an infimum, not a minimum.

## Mathematical disposition, dependency boundaries and possible correction

**Original Corollary 5.12.2 is correct as stated.** This construction disproves only the *unprinted* extension that replaces "convex" by "connected" for its real fiber, even if all other product-tube assumptions and stronger strict PSH/smoothness hold. Choosing the permitted affine function \(\ell=0\) already defeats the corresponding affine-infimum weakening. It shows **connectedness, boundedness, and smoothness of \(V\) cannot substitute for convexity**.

The full Theorem 5.12.1 additionally requires a proper imaginary-translation-invariant **PSH exhaustion \(\psi\)**. We do **not** assert our annular tube has that exhaustion, nor that the theorem fails if convexity alone is removed while retaining its exhaustion condition. Theorem 5.12.1's original statement and proof remain unrefuted. This is a sharpness check of the corollary, not a general-purpose characterization of admissible nonconvex fibers.

**Proposed change (reviewable only):** optionally add a separate explanatory remark after Corollary 5.12.2 with the explicit two-real-dimensional annulus and the formula \(2-2|z|+2|z|^2\); do **not** modify the statement, source/permanent labels, historical attribution, or canonicalization. **Affected dependents:** any attempted use of the Kiselman fiber infimum with merely connected rather than convex real fibers (for instance hypothetical extensions of envelope/test-curve arguments). No actual later printed theorem is declared invalid or completely certified here.

No external mathematical theorem beyond elementary real/complex Hessian computations and the elementary subharmonic maximum principle is used. This check does **not** inspect or extend the dedicated Demailly approximation/regularization, Bergman, weighted-L², Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss program, all previously marked **deferred-by-user**. There is no completion of the other §5.12 proof dependencies.

## Precise coverage and operational boundary

- **Direct new mathematical coverage:** §5.12, Corollary 5.12.2 real-fiber convexity and its affine-zero case; Theorem 5.12.1 convexity/**extra exhaustion** distinction; opening real-fiber conventions. Independently derived the strictly PSH counterexample and radial Laplacian.
- **Not reviewed/certified:** full Theorem 5.12.1 proof chain, general Kiselman infimum with arbitrary nonconvex fibers, general pluripotential envelope results, any downstream theorem, and excluded proof-completion topics. Previously **partly** audited §5.12, so **0 new first visits**, **0 complete mathematical-section certifications**; current full ToC matrix remains **25 chapters / 747 numbered sections / 0 entire mathematical sections certified**.
- This note is an **audit proposal** only. No source, registry, published reading edition, main branch, historical attribution, CI, tests, formal verification or website publication is changed or claimed.
