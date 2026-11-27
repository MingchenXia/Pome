# Sharp separated-potential mass gap for scaled elliptic quotient metrics

Date: 2026-11-28. Production main: `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Audit base: `e458a9f3b5c9801703a8e39e63988fb6b522471f`.

Finding **POME-ELLIPTIC-SCALED-SEPARATED-MASS-GAP-001** — low / verified conditional deduction (not a false printed theorem). It strengthens Proposition 12.19.20, not the unrestricted lower-mass theorem.

## Exact anchors and direct coverage

- `docs/sections/a-gauduchon-variational-volume--vanishing-lower-mass/index.html`, blob `c1477be8a0df1e32c391b51dae5b7e157df3ccfd`, mathematical lines 7–491. Theorem 12.19.1 (source non-kahler-pluripotential-theory:C504D1D4, permanent 38D9206B1A2F); Lemma 12.19.4 (C0F79A8C, 669B72559DF9, 73–104); Lemma 12.19.10 (DF3A79AE, 40DB573E7C1E, 177–207); Lemma 12.19.13 (D56ADE63, BD9C00A32F59, 231–279); Proposition 12.19.18 (CC2145C0, 94417AD14985, 365–405); Proposition 12.19.20 (73E21B50, 3290D6E85075, 412–465), Equation 12.19.21 (87EE58E6037C); Proposition 12.19.22 (2E8355DD, 69BB70EA26D9, 469–490). Read directly throughout, except the proof of bounded-potential regularization cited in 12.19.18 is deferred-by-user; no reopening of that proof.
- `docs/sections/a-gauduchon-variational-volume--orders-of-degeneration-at-the-nef-boundary--positive-current-subtraction-and-divisorial-residuals/index.html`, blob `8c1eb4eba5af6cc9331b103ed5156251091acce7`, whole mathematical lines 7–98. Proposition 12.24.1 (EAC70D2C, 7CE9EDC18591, 11–33); Proposition 12.24.3 (4F58A738, D15FEB2692E7, 41–73); Corollary 12.24.5 (08FA52E9, 9860E4D04E6C, 81–98).

Both rows were LEGACY-UNRECONCILED; this is current direct coverage, not proof of historical first visits. No upstream dependency chain is certified.

## A two-parameter sharp result

Keep the compact elliptic quotient X, fibration pi, normalized forms alpha,beta, D=dt wedge d^c t, and circle length L=4 pi of Section 12.19. For constants A,C>0 define the Hermitian form

    h = A(alpha+beta)+C D.

For smooth real separated potentials u=f(t)+pi^*v with f periodic of period L and h+dd^c u>0, set R=min(2A,CL). The exact infimum of their masses is

    6 C ( A^2 L - L R^2/4 + R^3/(6 C) ).

It is positive, is not attained by any smooth strictly admissible separated potential, and is approached with v=0. In particular, it equals 8 A^3 when 2A<=CL, and equals 6 C A^2 L - C^3 L^3/2 when 2A>=CL. At A=C=1 the printed value 8 is recovered. This assertion concerns only separated potentials; the unrestricted lower mass is zero by 12.19.1, conditional on its inputs.

### Proof

Write p=f', with mean zero on the period. Since dd^c t=beta-alpha and D is zero on ker(partial t),

    h+dd^c u = (A-p)alpha+(A+p)beta+pi^*dd^c v+(C+p')D.

The positive vertical direction gives p'>-C. The restriction to ker(partial t) identifies with the positive base form H_s=(A-p(s))alpha_B+(A+p(s))beta_B+dd^c v for every s modulo L, because every fiber attains every such s. Integrating over each ruling yields |p|<A. Conversely when v=0 these two strict conditions suffice by the direct sum splitting. The argument uses only the fibration in the printed section, not regularization.

For each s, by Stokes on the closed base, integral_B H_s^2=2(A^2-p(s)^2). Only 3 H_t^2(C+p')D contributes to the third power. In each fiber, integral_E F(t)D=integral_0^L F(s) ds by the explicit normalization verified in 12.19.18. Thus fiber integration followed by base integration gives

    M(u)=6 integral_0^L (A^2-p^2)(C+p') ds
        =6 C (A^2 L - integral_0^L p^2 ds).

The p' contribution is the integral of the derivative of A^2 p-p^3/3, hence zero. No assumption about closure of h is used.

If p is nonzero, let m+=max p, m-=-min p, r=m++m-. Then r<2A, and r<CL because a forward max-to-min interval of length at most L has p'>-C. Hence r<R. Set G(z)=(m+-z)(z+m-). It is nonnegative on the range. Integrate G(p) >= -G(p)p'/C on a forward max-to-min interval I. Its right integral is exactly r^3/(6C) even if p is nonmonotone there, by the primitive of G. On the whole period the mean-zero condition gives

    integral p^2 <= L m+ m- - r^3/(6C)
                  <= L r^2/4 - r^3/(6C).

The final expression is strictly increasing for 0<r<CL, its derivative being r(L-r/C)/2. Thus the integral is strictly less than L R^2/4-R^3/(6C), also true for p=0 since R>0. The formula for the mass gives the claimed strict bound.

For sharpness put b=(L-R/C)/2>=0. On the circle choose the piecewise profile p0 equal to R/2 for time b, descending at speed C for time R/C, then equal to -R/2 for time b; close the period by the positive jump R. The construction also works if b=0. Its mean is zero, |p0|<=A, and the distributional derivative is >=-C. Its squared integral is

    (L-R/C) R^2/4 + R^3/(12C)
      = L R^2/4 - R^3/(6C).

For nonnegative smooth periodic approximate identities rho_e, the functions p_e=(1-e)(p0*rho_e), 0<e<1, have mean zero, |p_e|<A, p_e'>=-C(1-e)>-C and converge in L^2 to p0. Their primitives are smooth periodic f_e. Taking v=0 gives admissible potentials and the desired limiting mass. No smoothing of quasi-PSH functions or excluded programme is involved.

The formula is positive: R<=2A implies A^2 L-LR^2/4>=0, and R^3/(6C)>0. The two closed-form branches agree at CL=2A. The change of regime comes from the period constraint r<CL, which is inactive in the original A=C=1 proof. The proposed addition is optional, and no correction to 12.19.20 is required. No downstream result needs a change.

## Direct review observations and remaining inputs

- The quotient strip is compact because both homogeneous coordinate blocks are bounded away from zero in the normalized sphere; the deck action is free. The stated elliptic periods follow from q=e^(2pi), and with the printed dd^c normalization the vertical integral of D is 4pi. In 12.19.4 the hyperplane H_0 intersected with Omega is a projective plane minus two points and is irreducible. Its translates give distinct zeros accumulating in a chart, forcing the analytic Lelong locus to be all of Omega. This step is conditional on the Gauduchon separation theorem 11.6.1, compactness 5.25.2 and Siu analyticity 5.34.2 (no proof of Siu or approximation undertaken).
- In 12.19.10 |a-bu|>=5/8 follows from the support bounds. At z_1!=0, u and a vary the two w-coordinates independently, while at z_1=0, tau and b do; the point parameter supplies the remaining coordinate. Fiber integration of compactly supported parameter densities is smooth for epsilon>0. The proof takes epsilon to zero for each fixed j, not uniformly over the concentrating sequence. The Schur complement is positive, and Q=2 det(H)H^(-1) gives det(Q)=8 det(H)^2 and 6 det(H)=(3/sqrt(2))sqrt(det Q). The lower root-volume estimate cancels the delta^2 thickness exactly. Conversion to actual small smooth equation masses is conditional on Theorem 12.2.3. Products use only the binomial wedge expansion plus the metric comparison; upper-mass statements also use 13.14.15 and the Hopf example.
- For 12.19.18, dd^c D=-(beta-alpha)^2=2 alpha beta, and d(omega^2)=0. The bounded-potential upper-mass passage via 12.15.4 is deferred-by-user; the smooth identity and the no-pluriclosed/no-closed-Kähler-current contradiction are checked independently. The equivalence with Fujiki class C remains an upstream input.
- In 12.24.1 distributional pairing of dd^c phi against the smooth dd^c-closed Gauduchon power vanishes; dividing the two positive-volume logarithms by log epsilon<0 reverses their order. The flat-torus factorial and blowup intersection obstruction in 12.24.3 are correct. Its fractional/oscillatory examples retain 12.21.4–5 as inputs. The last ruled-surface example uses 16.29.16, 16.29.18 and the closed-nef formula after 12.11.1 conditionally; the two expansions follow from theta^2=B^2=0 and integral theta B=1. Removing a particular current's divisor is correctly distinguished from subtracting minimal multiplicities defined by perturbed backgrounds.
- No new confirmed printed error or demonstrated proof gap in the read portions. No transitive proof certificate. All Demailly/regularization/Bergman/L2/OT/multiscale/positivity-loss programme work is deferred-by-user, not resolved. No tests, builds, CI, publication or production edits performed.
