# Universal vanishing of the Hermitian geodesic-action torsion defect

**Finding:** `POME-GEO-UNIVERSAL-TORSION-KAHLER-001`  
**Severity/status:** low / verified conditional deduction (and a direct algebraic audit of the printed first-variation formula); **not** a false printed theorem, a repaired proof, or a claim that the two geodesic solution sets coincide.  
**Date:** 2026-11-02. **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

## Exact integrated anchors

1. `docs/sections/perron-interpolation-and-the-geodesic-equation/index.html`, main blob `dc8dc381257360c94fe1c792499bb1ddf1bf5997`: Proposition **17.16.9** (permanent `5885FD8F9550`; product Schur complement at lines 167–183); Theorem **17.16.12** (source `non-kahler-pluripotential-theory:983F8C01`, permanent `7A7AE56CA513`, lines 214–247, equation **17.16.13** permanent `DCC8DA6D179E`, lines 216–219); Corollary **17.16.14** (source `non-kahler-pluripotential-theory:8881F196`, permanent `BE24BBA15991`, lines 252–262).
2. `docs/sections/gauduchon-metrics-and-linear-mass--the-adjoint-measure-of-the-linearization/index.html`, blob `519e50338be6560f6b2856fddce212738f5109bc`: Proposition **11.23.4**, source `non-kahler-pluripotential-theory:B9B9F692`, permanent `A914D4D9C6CB`, lines 58–73; Example **11.23.5**, source `non-kahler-pluripotential-theory:324594DA`, permanent `28F39F2B7C2C`, lines 77–100.
3. `docs/sections/torsion-and-the-variation-of-mass/index.html`, blob `9abec9685e33a1b40f9c0765381408eb52b325d3`: Theorem **11.1.7** (Chiose), source `non-kahler-pluripotential-theory:5CD99CBA`, permanent `FB90FC741F25`, lines 100–159, and integration-by-parts Lemma **11.1.2** (permanent `3B0A8DD950AD`, lines 15–25).

## The exact criterion (smooth pointwise operator identity, not existence)

Let (X) be a compact complex manifold of complex dimension (n\ge2), and let (omega>0) be any smooth Hermitian form. Put
[
\mathcal H_omega=\{u\in C^\infty(X,\mathbb R):\eta_u:=\omega+dd^c u>0\},\quad T_u=\eta_u^{n-1}.
]
For a real smooth instantaneous velocity (f), define precisely the discrepancy between the right sides of the stationary-action equation (17.16.13) and the product homogeneous Monge–Ampère equation (17.16.10):
[
\boxed{\mathfrak T_{\eta_u}(f)
=n f\big(df\wedge d^cT_u-d^c f\wedge dT_u\big)
+\frac n2 f^2dd^cT_u.}
]
For each fixed (u), **this smooth top-degree form vanishes for every real smooth (f) if and only if** (d(\eta_u^{n-1})=0), i.e. (\eta_u) is **balanced**, a strictly stronger algebraic requirement than Gauduchon in general. Moreover the following *universal* conditions are equivalent:

- (omega) is Kähler, i.e. (d\omega=0).
- Every (\omega+dd^cu>0) is balanced.
- For every (u\in\mathcal H_omega) and every smooth real instantaneous speed (f), (\mathfrak T_{\eta_u}(f)=0) pointwise.

Thus a non-Kähler background always has some smooth admissible potential and some smooth real speed for which the **two displayed differential operators differ**. This is an operator-level assertion: it does **not** construct a path solving one but not the other, nor assert that either equation has a smooth solution with arbitrary endpoints. The historical Chiose attribution in Theorem 11.1.7 is retained; its previously printed equivalence concerns universal **Gauduchon** persistence and mass, whereas the present stronger first-order criterion concerns **balanced** persistence and the full speed-dependent torsion defect.

## Proof

**(A) At one fixed (\eta).** Set (T=\eta^{n-1}) and assume (\mathfrak T_\eta(f)=0) for every real smooth (f). In particular (f\equiv1) gives (dd^cT=0). At a fixed point (x), for arbitrary real (g) with (g(x)=0), use (f=1+s g) and compare the coefficients of (s) at (x); the contribution of (f^2dd^cT) has already vanished, yielding
[
(dg\wedge d^cT-d^c g\wedge dT)_x=0\quad\text{for every }dg_x.
]
Writing (d^c=c_i(\bar\partial-\partial)) with the nonzero purely imaginary normalization constant (c_i), the expression equals
[
2c_i(\partial g\wedge\bar\partial T-\bar\partial g\wedge\partial T).
]
If (\partial T\ne0), the natural wedge pairing of a ((1,0))-covector with the conjugate ((n-1,n))-form is nonzero for some covector. Real functions permit arbitrary complex first derivatives (\partial g_x), including multiplication by (i); testing both phases contradicts the displayed identity. Hence (\partial T=\bar\partial T=0), i.e. (dT=0). Conversely (dT=0) also implies (d^cT=dd^cT=0), so (\mathfrak T_\eta(f)=0) for every (f). This proves the fixed-potential equivalence without using any PDE existence theorem.

**(B) Uniformity in all potentials.** Since (d(dd^c u)=0),
[
d(\omega+dd^c u)^{n-1}
=(n-1)d\omega\wedge(\omega+dd^c u)^{n-2}.
]
At any fixed (x\in X), arbitrary sufficiently small real Hermitian ((1,1))-form Hessian jets (Q=(dd^cu)_x) are realized by compactly supported smooth real functions, keeping (\omega+dd^cu>0). If all potential perturbations are balanced, the polynomial
[
Q\longmapsto d\omega_x\wedge(\omega_x+Q)^{n-2}
]
vanishes on an open set of Hermitian (Q), hence identically. Its homogeneous term of degree (n-2) gives (d\omega_x\wedge Q^{n-2}=0) for every Hermitian (Q). Polarization and elementary complex exterior algebra show that this annihilates every ((2,1)) and ((1,2)) coefficient of (d\omega_x): products of ((1,1))-covectors span the complementary test wedges. (For (n=2), the displayed equation is simply (d\omega_x=0).) Thus (d\omega=0) everywhere. The reverse implication is immediate because (d\eta_u=d\omega). Combining (A) and (B) proves all equivalences.

**(C) Fully explicit balanced, non-Kähler witness already present in Pome.** Example 11.23.5 works on (E^3) with (\eta_j=dx_j\wedge dy_j), (b=e^{\cos(2\pi x_1)}), (c=b^{-1}), and
[
\omega=\eta_1+b\eta_2+c\eta_3.
]
In fact, the printed form is **balanced**, not merely Gauduchon: because (bc=1) and (db,dc) are multiples of (dx_1),
[
\omega^2=2b\eta_1\wedge\eta_2+2c\eta_1\wedge\eta_3+2\eta_2\wedge\eta_3,\qquad d\omega^2=0.
]
But (d\omega=db\wedge\eta_2+dc\wedge\eta_3\not\equiv0), so this is a balanced non-Kähler background. Choose the exact printed (v=\cos(2\pi x_2)) and (dd^cv=h\eta_2), (h=-\pi\cos(2\pi x_2)). For (0<|s|<1/(\pi e)), (\omega_s=\omega+sdd^cv>0). Direct differentiation (using (dh\wedge\eta_2=0)) gives the **new exact first-order torsion formula**
[
\boxed{d\omega_s^2=2s h\,dc\wedge\eta_2\wedge\eta_3.}
]
At (x_1=1/4, x_2=0), one has (h=-\pi) and (dc=2\pi dx_1), hence
[
d\omega_s^2=-4\pi^2s\,dx_1\wedge\eta_2\wedge\eta_3\ne0.
]
By (A), for this perturbed metric there exists a smooth velocity whose stationarity torsion term is nonzero. The printed Example 11.23.5 already shows the perturbed metric is not Gauduchon; the stronger new observation is that the *unperturbed* metric is actually balanced, while the arbitrarily small perturbation loses even balancedness.

## Scope and proposed documentation change

This is a checked **conditional deduction from the printed smooth variational Euler–Lagrange formula**, plus self-contained exterior-algebra and explicit torus calculations. Equation (17.16.13) itself was directly rechecked by differentiating (\frac12\int \dot u^2\eta^{n}\) and using the smooth integration-by-parts identity: the coefficient of (dd^cT) is (n/2), and the two first-order torsion signs match the Leibniz expansion. No incorrect statement or complete mathematical proof-chain certification is asserted. Proposed optional standalone corollary after Theorem 17.16.12, with a note after Example 11.23.5 that the starting metric is balanced. No published source, tags, or canonical entries changed. Affected interpretations: §§17.16.9–14, 11.1.7–8, 11.23.4–5, and formal comparison of the Mabuchi action with Perron/HCMA paths. Excluded approximation, Bergman, L², Ohsawa–Takegoshi, multiscale and positivity-loss programmes are **deferred-by-user** and untouched.

**Actual coverage:** first direct algebraic audit of the *full speed-dependent* torsion terms in Theorem 17.16.12 and their universal pointwise null condition; additional direct exterior-derivative check of Example 11.23.5 and the Chiose universal-mass distinction. §§17.16, 11.23 and 11.1 were already partly audited; no first-covered section or fully certified mathematical section is newly claimed. Overall main ToC: 25 chapters, 747 sections, zero whole mathematical sections certified. No tests, builds, CI, formalization or publishing were run.
