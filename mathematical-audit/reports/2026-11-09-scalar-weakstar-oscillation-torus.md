# Exact weak-star homogenization obstruction for the normalization scalar (2026-11-09)

- **Finding:** `POME-SCALAR-WEAKSTAR-HOMOGENIZATION-001`
- **Classification:** low / **verified conditional deduction** (sharpness of the printed topology; **not** a false printed theorem or a proof repair).
- **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Integrated loci:** `docs/sections/normalization-and-weak-adjoint-measures--the-scalar-functional/index.html`, blob `fff86de757578ed2be369ba752123f62f3d31044`, Theorem **11.33.5**, source `non-kahler-pluripotential-theory:D502EBBF`, permanent tag `5E3583383688`, physical lines **88–121** (notably 88–91 and the compactness proof 94–121); and `docs/sections/normalization-and-weak-adjoint-measures--entropy-and-the-closed-case/index.html`, blob `0710d0732ae7ef81de3d3d62206a0f9c6b5d321f`, Eq. **11.37.2**, source `non-kahler-pluripotential-theory:65FF799F`, permanent tag `803909FECEC0`, physical lines **50–61**, particularly 56–59.
- **Proposed change:** an optional counterexample/remark after Theorem 11.33.5; leave its L¹ hypothesis, the underlying theorem, all tags and historical attribution unchanged.

## Statement of the boundary phenomenon

Let (E=\mathbb C/(\mathbb Z+i\mathbb Z)), with (z=x+iy), (omega=\tfrac i2\,dz\wedge d\bar z=dx\wedge dy), so (\int_E\omega=1). Choose the Kähler background (	heta=omega), the smooth reference model (arphi=0) and (dV=omega). The standing positive-volume model assumptions hold, including the nontrivial smaller-background envelope (zero is an admissible competitor).

Fix (a>0). For every positive integer (j), define
[
 F_j(z)=a\cos(2\pi jx),\qquad
 J(a)=\int_0^1 e^{a\cos(2\pi t)}\,dt>1,\qquad
 \rho_j(z)=\frac{e^{F_j(z)}}{J(a)}.
]
The strict inequality (J(a)>1) follows from strict Jensen, since (\int_0^1a\cos(2\pi t)dt=0) and the cosine is nonconstant.

**Exact conclusions.** All (F_j) are smooth and bounded by (a), and (F_j\rightharpoonup^*0) in (L^\infty(E,dV)). Nevertheless,
[
 B_0(F_j)=-\log J(a)<0=B_0(0)
 \quad\text{for every }j.
]
This failure persists although the normalized smooth Monge–Ampère solution potentials converge **uniformly** to zero at the explicit rate (O(j^{-2})), and their Monge–Ampère measures and unique supporting probabilities converge **weakly** to (dV). The latter convergence cannot be promoted to total variation.

Thus uniform (L^\infty) boundedness plus weak-star convergence of logarithmic densities, even augmented by uniform convergence of the normalized solutions and weak convergence of the corresponding normalized measures, is insufficient to replace the **strong (L^1)** premise of printed Theorem 11.33.5. Nothing contradicts that theorem.

## Proof, independent of the general existence theorem

For this background (\mathrm{MA}_\omega(u)=\omega+dd^cu) in dimension one, with the project's convention (dd^c=\tfrac{i}{2\pi}\partial\bar\partial). For a real function (h=h(x)),
[
 dd^ch=\frac{h''(x)}{4\pi}\,\omega.
]
The smooth periodic function (q(x)=e^{a\cos(2\pi x)}/J(a)-1) has integral zero. Consequently there exists a smooth real 1-periodic (v) with
[
 v''(x)=4\pi q(x);
]
its additive constant is immaterial. Set
[
 u_j(x+iy)=j^{-2}\big(v(jx)-\max_{\mathbb R/\mathbb Z}v\big).
]
These functions are globally defined, smooth, and (\sup_Eu_j=0). Direct differentiation gives
[
 \omega+dd^c u_j
 =\bigl(1+q(jx)\bigr)\omega
 =\rho_j\omega>0.
]
Thus (u_j) are genuine smooth (\omega)-psh solutions of
[
 \mathrm{MA}_\omega(u_j)=c_j e^{F_j}dV,\qquad
 c_j=J(a)^{-1}.
]
The normalization is forced by integrating over (E) (Stokes gives (\int_Edd^c u_j=0)). Similarly (u_0=0) solves the (F=0) equation with (c_0=1). Hence (B_0(F_j)=\log c_j=-\log J(a)), in exact agreement with the integrated closed-background formula (11.37.2). Moreover,
[
 \|u_j\|_{C^0(E)}
 =\frac{\max v-\min v}{j^2}\longrightarrow0.
]

For every (g\in L^1(E,dV)), the Riemann–Lebesgue lemma applied to its (x)-marginal gives
[
 \int_Eg F_j\,dV\longrightarrow0.
]
This proves weak-star (L^\infty) convergence. It is not (L^1) convergence: the integral is exactly
[
 \int_E|F_j|dV=\frac{2a}{\pi}>0.
]
For any continuous (g), approximate the (x)-dependence by trigonometric polynomials (or partition into the (j) equal periods) to obtain
[
 \int_Eg\rho_j dV\longrightarrow\int_Eg\,dV,
]
because (\int_0^1e^{a\cos(2\pi t)}dt/J(a)=1). Equation (11.37.2) also identifies the unique supporting probability at (F_j) as (\rho_jdV), so these supporting probabilities converge weakly to the unique supporting probability (dV) at zero.

However their full signed (L^1) discrepancy is constant:
[
 \int_E|\rho_j-1|\,dV
 =\int_0^1\left|\frac{e^{a\cos(2\pi t)}}{J(a)}-1\right|dt>0.
]
The inequality is strict because the density is nonconstant. In the half-(L^1) convention, total-variation distance is one half of this display. This completes all assertions without employing any excluded approximation or (L^2)/OT machinery.

## Logical assessment and dependencies

- **Printed Theorem 11.33.5 is correct as stated**: it assumes **strong (L^1(dV))** convergence of uniformly bounded (F_j), which fails here. The difference between (F_j\rightharpoonup^*0) and (e^{F_j}\rightharpoonup^*J(a)) is the essential nonlinear obstruction.
- Formula **11.37.2** is used for the supporting probability and crosschecked against the independent explicit Poisson construction above; no general singular Monge–Ampère solvability theorem is needed for this example.
- **Affected downstream usage:** any attempted extension of the normalization-scalar stability or supporting-probability convergence steps (notably §§11.34–11.36) that substitutes weak-star (L^\infty) control for (L^1) control requires further hypotheses, such as convergence of the exponential densities with the correct total integrals. No existing downstream printed theorem is declared false or fully verified.
- **Coverage:** direct theorem/equation and model proof check only in previously partly reviewed §§11.33 and 11.37; no complete-section certification. This is distinct from earlier exact KL/Fenchel formulas and TV/L¹ Lipschitz estimates: here the normalized solutions converge **uniformly** while the scalar has a fixed nonzero gap and the logarithmic densities converge only weak-star.
- **Other entries:** older resolved/unresolved findings stay untouched. The owner-excluded Demailly regularization/Bergman/weighted-(L^2)/Ohsawa–Takegoshi/multiscale/positivity-loss programme remains **deferred-by-user**, neither certified nor reopened. No source/registry/main/tag/canonicalization changes, builds, CI, formalization or publication.
