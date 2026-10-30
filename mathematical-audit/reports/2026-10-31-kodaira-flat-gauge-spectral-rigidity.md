# 2026-10-31 — Sharp spectral rigidity of the Chern–Ricci-flat Kodaira gauge

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Scope:** Previously unreviewed *uniform-in-the-periodic-parameter* consequence of the integrated reading edition, not a claim that §23.2 or its prerequisites are completely verified. No regularization, Bergman, Ohsawa–Takegoshi, or their dedicated L² proof programme was examined.

## POME-KODAIRA-FLAT-GAUGE-SPECTRAL-RIGIDITY-001

**Severity/status:** Low — **verified conditional deduction**. The source's Example 23.2.53 and Theorem 23.2.47 are not alleged false; the dependence on the latter's global integrated Bianchi–Bochner identity remains conditional.

**Production file:** docs/sections/locally-conformally-kahler-geometry/index.html, blob 6ebf8e604b45d3eb748037af506145273ca3875d.
**Original source:** non-kahler-pluripotential-theory:F3D1120B; permanent tag E37387C4675B; Example 23.2.53 at physical HTML lines 906–982, especially the general metric family at lines 939–965. Theorem 23.2.47: source non-kahler-pluripotential-theory (integrated theorem), permanent tag C4981F6B1F78, physical lines 786–888, identity at lines 786–794.

### Exact hypotheses and statement

On the fixed compact Kodaira surface constructed in Example 23.2.53, let f be **any real smooth 1-periodic function** satisfying

\[
C(x)=1-f''(x)>0.
\]

Keep the source's invariant coframe, complex structure, Vaisman form
\[
\lambda_1=-e^4+f'e^1,\qquad
\eta_1=e^3+f'e^2,\qquad
\omega_1=\lambda_1\wedge\eta_1+C\,e^1\wedge e^2,
\]
and set
\[
h=C^{-1/2},\qquad \omega=h\omega_1,\qquad
\lambda=-e^4+d(f+\log h),\qquad
q=d_g^*\lambda.
\]
Then \(\omega\) is strictly LCK and Chern–Ricci flat, and the **exact** identities from the original family hold for every f:
\[
\frac{\omega^2}{2}=e^{1234}=dx\,dy\,dz\,dt,\qquad
q(x)=-h''(x).
\]
Consequently the following sharp inequality holds, with \(\bar h=\int_0^1h(x)\,dx\):
\[
\boxed{
\int_Xq^2\,d\operatorname{vol}_g
=\int_0^1 |h''|^2dx
\ge (2\pi)^4\int_0^1|h-\bar h|^2dx.
}
\tag{K1}
\]
In particular, **the Chern–Ricci-flat conformal gauge is Gauduchon if and only if f is constant**. For every nonconstant f, q is nonzero and changes sign.

Conditionally on the integrated Bianchi–Bochner theorem 23.2.47, writing
\[
S^-=\tfrac12(\nabla\lambda-(\nabla\lambda)(J\cdot,J\cdot)),
\]
we additionally obtain the sharp geometric estimate
\[
\boxed{
\int_X|S^-|_g^2\,d\operatorname{vol}_g
\ge 8\pi^4\int_0^1|h-\bar h|^2dx.
}
\tag{K2}
\]
Both constants in (K1) and (K2) are sharp **within the exact positive periodic Kodaira family**, not merely in an unrestricted function space.

### Proof (no smoothing or Bergman/L² existence results)

Example 23.2.53 computes the stated volume and co-closed Lee form for a general smooth f with C>0, **before** specializing to its displayed cosine example: see physical lines 939–965. The fundamental domain of the compact nilmanifold has coordinate volume 1; its Jacobian is 1 in the invariant coframe. Thus integrating a function of x against the flat-gauge volume reduces exactly to the integral over x in [0,1].

Expand the smooth real periodic function in its Fourier series
\[
h(x)=\sum_{k\in\mathbb Z}\widehat h_k e^{2\pi ikx}.
\]
Parseval gives
\[
\int_0^1|h''|^2dx
=(2\pi)^4\sum_{k\ne0}k^4|\widehat h_k|^2
\ge(2\pi)^4\sum_{k\ne0}|\widehat h_k|^2
=(2\pi)^4\int_0^1|h-\bar h|^2dx.
\]
Equality holds exactly when h is constant or all its nonconstant Fourier modes have |k|=1. This proves (K1). Gauduchon is equivalent to q=0 by the already integrated Proposition 23.2.7. But q=0 means h''=0; periodicity makes h constant, so C=h^{-2} is constant. The defining identity C=1-f'' and \(\int_0^1f''=0\) force C=1, f''=0, and f constant. The converse is immediate. The average of q is zero, so nonzero q has both positive and negative values.

Theorem 23.2.47 supplies \(\int_X|S^-|^2=\tfrac12\int_Xq^2\) under precisely the LCK and Chern–Ricci-flat hypotheses met here. Combining with (K1) gives (K2), **conditional on that theorem**, without pretending to have certified its complete differential-geometric proof.

For sharpness take an arbitrary \(a\) with \(0<a<1\) and set
\[
h_a(x)=(1-a^2)^{-3/4}\bigl(1+a\cos(2\pi x)\bigr)>0,\qquad C_a=h_a^{-2}.
\]
The elementary integral
\[
\int_0^1(1+a\cos(2\pi x))^{-2}dx=(1-a^2)^{-3/2}
\]
implies \(\int_0^1C_a=1\). Therefore the smooth mean-zero function \(1-C_a\) is the second derivative of a real smooth 1-periodic f_a, uniquely up to addition of a constant. It meets the source hypotheses \(C_a=1-f_a''>0\). Since \(h_a\) has only Fourier modes \(0,\pm1\), equality holds in (K1), and hence in (K2) under the already stated conditional input. Thus **neither positive constant can be increased** in these lower estimates, even when f is nonconstant.

### Finding classification, correction and dependents

This is **not** a counterexample to Example 23.2.53, an error in its chosen cosine function, or a complete independent proof of the global Chern–Ricci-flat rigidity theorem. The printed example only chooses one nonconstant f to demonstrate failure of the Gauduchon condition. The result above classifies **all** periodic f in that explicit family and adds an optimal coercivity gap. Proposed optional independent corollary following Example 23.2.53: display (K1), the equivalence “Gauduchon iff f constant”, and the conditional (K2), retaining the source's original tag/attribution.

**Potential dependents:** §23.2.47 (quantitative interpretation only; not used to infer the unconditional classification), §23.2.53 (all f in its existing explicit family), §23.2.54 (context for the Vaisman existence conjecture, no answer claimed). No source, canonicalization, registry, or published-page edits.

### Actually reviewed / negative checks

Direct reading of §23.2's integrated Lee form / volume identities (§23.2.2–24), Vaisman volume and rigidity construction (§23.2.29–32), and complete Kodaira Chern–Ricci-flat example (§23.2.47 and .53) plus selected Lee–Gauduchon/strongly Gauduchon statements (§23.2.56–72) as **contextual risk survey**; only the displayed family and its Fourier consequence were newly proved. Selected independent formula checks of §13.7 (capacity/extended-capacity convergence), §17.3 (relative energy and decreasing nets), §19.2–3 / §19.7 (Okounkov semigroups), and §20.5 (analytic cycles) yielded no new independently established error; existing ledger findings there have not been recounted. §20.4 explicitly imports excluded approximants and was **not reaudited**.

**Coverage:** 25 current chapters, 747 distinct numbered ToC sections, zero fully certified. Old ledgers' error/proof-gap/external-dependency states remain unchanged. All dedicated Demailly approximation/regularization, Bergman, Ohsawa–Takegoshi, multiscale atlas, and positivity-loss proof-completion records remain **deferred-by-user**, not solved. No build, CI, publishing, website generation, formal verification, or numerical test was conducted.
