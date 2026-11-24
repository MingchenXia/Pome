# Atomic trace Poisson equation: the entropy endpoint and exact bounded-potential criterion

Date: 2026-11-24. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272.

Finding **POME-ATOMIC-TRACE-POISSON-LLOG-L-ENDPOINT-001** — low / verified conditional deduction (not a false printed theorem). Proposed supplementary theorem and sharpness example; no production changes.

## Anchors and hypotheses

Integrated reading edition: docs/sections/restriction-and-intrinsic-trace-data/index.html (blob dbc3b722ceacb8232fe4c7b711e5ad98b0708f06), subsection 20.3.14 (E07C398EC98F), Theorem 20.3.15 (AFC6C3B6368C), lines 315–354, especially 319–327 and 332–353. Background: Theorem 20.3.10 (879739B42EBB), lines 226–273, in particular Green representation at 256–270; Proposition 20.3.13 (B3BE3C08418A), lines 290–310. The curve is compact, smooth and connected. Write B=theta|Y, M=int B, D=D_u, d=D(Y), eta a smooth probability volume form. Assume the atomic trace construction and its finite measure D, 0<=d<=M, are available. The Green kernel satisfies dd^c_x G(x,y)=delta_y-eta, G<=0, and has the usual uniform logarithmic diagonal expansion on a compact smooth curve. Its existence, off-diagonal smoothness and local logarithmic parametrix are scalar elliptic inputs, not newly proved here. Keep the convention dd^c=i/(2pi) partial bar-partial. Write w=G D and choose the smooth s_0 solving dd^c s_0=M eta-B. Then w+s_0 has curvature D+(M-d)eta.

## Exact extension

Let mu be any finite positive measure of mass m=M-d which charges no polar sets. There is a B-psh potential in the ordinary type of w with extended MA measure mu if and only if the nonnegative Green potential

    U_mu(x)=int_Y (-G(x,y)) dmu(y)

is bounded on Y. If it exists, the potential is unique up to a constant. In fact, a candidate is w+s_0+G mu, since

    B+dd^c(w+s_0+G mu)=D+mu.

Boundedness of G mu makes this the same ordinary type as w, and the nonpolar part is mu. Conversely, use precisely the polar-part invariance input (Corollary 5.27.15) used at lines 347–350 of 20.3.15. An ordinary-equivalent solution has curvature D+mu. Its difference from the displayed candidate is distributionally harmonic, hence constant on the connected compact curve. Ordinary equivalence bounds G mu almost everywhere (both potentials are finite almost everywhere and s_0 is bounded). The canonical quasi-subharmonic representative of G mu is then bounded everywhere: adding a local smooth background gives a subharmonic representative recovered by shrinking-ball averages. This last argument matters even at a common pole of the two potentials; subtracting their extended values there would be undefined. For m=0, mu=0 and the original zero-mass assertion is unchanged.

For f>=0 with positive integral I, the equation mu=c f dV, c>0, therefore still requires M>d and c=(M-d)/I. Beyond the mass condition, bounded logarithmic potential is the exact existence condition for arbitrary integrable densities. All these statements are conditional on the trace construction, polar-part invariance and scalar Green inputs above, not transitive certification of them.

## L log L suffices, with continuous correction

Let f satisfy int f log(e+f) dV<infty for a smooth positive dV. Put K=-G. Compactness and the logarithmic parametrix give constants C and a>0 such that uniformly in x,

    K(x,y) <= C+2 log^+(1/dist(x,y)),
    int_{dist(x,y)<r} exp(a K(x,y)) dV(y) <= C r^(2-2a)

for small r, with 0<a<1 (the constants can change). Indeed the local volume density is uniformly comparable to planar area, and integration of rho^(1-2a) gives the bound. On the complement of a small diagonal neighborhood K is bounded and continuous.

The elementary inequality t b <= t log(e+t)+exp(b) for t,b>=0 follows from the convex conjugate of t log t-t. Apply it to t=f(y), b=aK(x,y), integrate over the radius-r ball, and divide by a. The first right-hand integral tends to zero uniformly in x by absolute continuity of the integral of f log(e+f), because ball volumes tend uniformly to zero. The second tends uniformly to zero by the displayed power bound. Thus

    lim_{r downarrow 0} sup_x int_{dist(x,y)<r} K(x,y) f(y) dV(y)=0.

For example, K_L=min(K,L) extends continuously across the diagonal (K tends uniformly to infinity there). The support of K-K_L lies in a uniform shrinking diagonal neighborhood by the upper logarithmic bound. Consequently the continuous functions int K_L(x,y) f(y)dV(y) converge uniformly to U_{f dV}. The latter is bounded and continuous. The exact criterion above proves the original existence, ordinary type, constant c, and uniqueness assertions with L log L replacing L^p, p>1. No multiplier-ideal regularization or approximation theorem is used for this new Poisson step. The original L^p theorem remains correct; L^p embeds into L log L on this finite-volume space.

## Sharpness among logarithmic Orlicz powers

Take Y=P^1, B a smooth positive form, and ambient u=0 (one may take Y=X); thus D=0, d=0, M>0 and the atomic trace has bounded ordinary type. In a coordinate disk centered at p choose a nonnegative density, supported in |z|<e^-2, with respect to planar area,

    F(z)=1/(|z|^2 (log(1/|z|))^2).

Define f relative to dV by f dV=F dx dy on the disk, zero outside. Smooth positive dV has bounded positive density there, so the integrability claims are equivalent. With t=log(1/r), the total mass is proportional to int_2^infty t^-2 dt, finite and positive. Moreover, for each 0<=gamma<1,

    int f (log(e+f))^gamma dV < infty,

because log(e+f) is O(t) and int_2^infty t^(gamma-2) dt converges. At gamma=1 that integral diverges (log f is comparable to t for large t). The Green potential at p has U(p)=infty: K(p,z)=2t+O(1), and the corresponding radial integral dominates a positive multiple of int_2^infty t^-1 dt. The canonical potential cannot be essentially bounded, by the same shrinking-average recovery of subharmonic representatives. Hence no bounded-type solution exists for this density with any positive c, despite the mass condition M>d and absolute continuity. The example is atomless and nonpolar. It proves sharpness within the scale L(log L)^gamma, not necessity of L log L for every individual density.

## Other checked steps and actual coverage

- In 20.3, read mathematical lines 13–486. Checked the nonnegative superadditive real-weight Fekete argument (47–59, with the zero remainder handled directly), the ideal-order monotonicity/homogeneity/max comparisons (99–106), the restricted-ideal example (165–177), the SNC floor formula (199–207), the finite-subsum mass bound (248–254, conditional on the supplied approximants), the Green representation and smooth-gauge independence (256–273), dyadic coefficient order and dominated total-variation/L1 convergence (300–309), the Poisson argument (332–353), the ordered-distance calculation and ideal-envelope/atomic-measure correspondences (363–481). Their local deductions are consistent with stated inputs. The pre-existing coarse 1/96 distance lower bound is not recorded as an error or as a new result. Dependencies on approximation at 16, 61–67, 108–120, 148–160, 248–251, 374 and 390, and any excluded prerequisite of the other statements, are deferred-by-user, not reopened or certified. The external scalar Green kernel, elliptic Poisson theory and the polar-part identity remain explicit inputs. No full section or transitive certification claimed; remainder of 20.3 not read in this run.
- In 20.8 (docs/sections/divisorial-restricted-volumes/index.html, blob 8eb1127568e77d6d045098361c366ceeb846b909), read Lemma 20.8.1 (7E82D2724E2F), lines 11–30; the nonexcluded continuity proof at 19–25 follows by the two positive-current mixtures with a common strict margin, given the maximal-mass assertion. The factor (1-s)^q in both directions gives local multiplicative control. Its exact-class approximation premise at line 17 is deferred-by-user. Also inspected statements and initial geometry at 34–97 and formulas/conditional Legendre setup at 99–134, without certifying the rest of the differentiability theorem 20.8.3 (8DC7DAC31FB7); its regularization-dependent inputs are deferred. No new claim about the full differentiability proof.
- Actual rendered table of contents docs/chapters/index.html (blob c0c07abf4d8f7575b54cff2ec694fcf987f51cf8) has 747 unique section locators, exactly matching the 747 formal matrix rows. Historic first visits remain unreconciled.

Affected dependents: Theorem 20.3.15 can be supplemented by the exact bounded-logarithmic-potential condition and continuous entropy endpoint; the ordinary trace construction of 20.3.10 and the ideal-distance results of 20.3.17–22 are unchanged. No new downstream failure established. Counts: two selected sections, zero newly complete sections, one conditional deduction, zero confirmed printed theorem errors, zero unresolved new proof gaps, zero complete transitive certificates. No build/test/CI or main/source/registry/tag/site edit. All excluded programmes remain deferred-by-user.
