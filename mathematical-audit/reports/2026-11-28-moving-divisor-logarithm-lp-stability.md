# Moving divisorial logarithms: finite-Lp stability and normalization review

Date: 2026-11-28. Reviewed production main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit only; no production patches.

## Finding POME-MOVING-DIVISOR-LOGARITHM-LP-STABILITY-001

Severity low; status **verified conditional deduction**, not a false printed theorem or a demonstrated proof gap. Theorem 11.41.3 (source B7148C83, permanent BF6A67E9A40E, physical lines 59–74) states L1 convergence of moving divisorial references and normalized solutions. In its exact hypotheses, both converge in every finite Lp, 1 <= p < infinity. Moreover their extended Monge–Ampère measures converge in full signed total variation. The original L1 result is sufficient for its stated purposes; the following optional strengthening does not depend on a regularization or Bergman construction.

### Uniform logarithmic tails (direct local proof)

Fix one limiting nonzero section s and its sequence s_j, with fixed smooth metric h. Work on connected X as in the surrounding smooth normalization theory. Put delta_j = sup_X |s_j-s|_h. On a trivializing chart containing a point of the zero set, choose a complex line through that point on which the local holomorphic function f representing s is not identically zero. Such a direction exists by the first nonzero homogeneous term of the local power series. Write coordinates (z,w) with z on this line. Choose R>0 small so f(z,0) has exactly m>=1 zeros, counted with multiplicity, in |z|<R and no zero on the boundary. Shrink the transverse polydisc so |f(z,w)| is uniformly bounded below on |z|=R for all its w. Uniform convergence on the closed product gives the same lower bound, up to a factor two, for all sufficiently large j. The boundary winding number is constant under the straight homotopy between f_j and f(z,0), because it avoids zero. The argument principle gives exactly m roots a_{j,l}(w) in the disc, counted with multiplicities (the same holds for f). No measurable or holomorphic choice of their ordering is needed.

For each fixed w, divide f_j(z,w) by the monic polynomial prod_{l=1}^m(z-a_{j,l}(w)). The quotient is holomorphic and nowhere zero in the disc, extends through the roots, and on the boundary its modulus is at least the common boundary lower bound divided by (2R)^m. The minimum principle applied to its reciprocal gives the same lower bound throughout the disc. Hence for some c>0 uniform in j,w,

|f_j(z,w)| >= c prod_l |z-a_{j,l}(w)|.

If |f_j|<r, at least one factor is <(r/c)^(1/m). The planar area of the sublevel set is at most m*pi*(r/c)^(2/m). The set itself is open, so Fubini applies without choosing or integrating a root labeling. Integrate over w and absorb the bounded metric and volume coefficients. On a finite cover of the limiting divisor, use the largest of the finitely many local orders M>=1. On the complementary compact set the sections are uniformly bounded away from zero, so no tail arises there. For s and all sufficiently large j, for 0<r<r_0,

dV{|s_j|_h<r} <= C r^(2/M).

There is also a common upper bound for |s_j|_h. Consequently for L_j=log|s_j|_h^2 (values on zero sets ignored in the Lebesgue integrals),

dV{L_j<-T} <= C exp(-T/M)

for all large T. The layer-cake formula gives a uniform bound in every finite Lq, and the same holds for L=log|s|_h^2. Local uniform convergence off the limiting zero set then implies finite-Lp convergence. This is an elementary one-variable argument applied fiberwise, not an application of strong openness, Demailly approximation, or an L2 extension theorem.

### An explicit, nonoptimal modulus

For 0<delta_j<1 sufficiently small, on {|s|_h >= sqrt(delta_j)} the ratio of the two norms is in [1-sqrt(delta_j),1+sqrt(delta_j)]. Therefore |L_j-L| <= C sqrt(delta_j). On its complement the above sublevel estimate gives volume <= C delta_j^(1/M); Holder with the uniform L^(2p) bound gives

||L_j-L||_p <= C_p (delta_j^(1/2)+delta_j^(1/(2Mp))).

If delta_j=0 the difference vanishes. Constants and M may depend on the limiting section, charts, metric, reference volume and p, and this is not asserted to be the optimal exponent. If the limiting section is nowhere zero, the uniform logarithmic Lipschitz estimate applies directly.

For the finite family in 11.41.3, write L_{jr}=log|s_{jr}|^2 and use

||t_{jr}L_{jr}-t_r L_r||_p <= |t_{jr}-t_r| ||L_{jr}||_p + t_r ||L_{jr}-L_r||_p.

Thus phi_j -> phi in Lp. The mean-zero residuals v_j converge uniformly in either regime of 11.41.3 (smoothly in the first), and the supremum normalization constants C_j= sup_X(phi_j+v_j) converge by its proof. The normalized u_j=phi_j+v_j-C_j therefore converge in Lp. No L-infinity conclusion for the full singular potentials is possible in general: on P^1 a moving zero of a nonzero linear section, different from the limiting zero, gives an unbounded logarithm difference on punctured neighborhoods of that zero, even after adding bounded residuals and constants.

### Exact measure consequence

Set c_j=exp B_{beta_j}(F_j), c=exp B_beta(F). Theorem 11.41.1 identifies the extended measures with c_j exp(F_j)dV and c exp(F)dV, respectively. In the first regime scalar convergence follows from 11.40.4; in the second it follows from 11.33.5. With a common L-infinity bound M_F for F_j,F,

||MA_ext_{theta_j}(u_j)-MA_ext_theta(u)||_TV
<= exp(M_F) (Vol_dV(X)|c_j-c| + c ||F_j-F||_1) -> 0.

Here TV is the full signed total variation norm, not half of it. Moving background and moving divisors cause no extra mass term: the measures vanish on the analytic polar sets by the printed removal identity. This is not a claim about general singularity types or arbitrary varying backgrounds and densities.

## Direct audit and dependencies

All three integrated mathematical sections below were read at the pinned main. Source tags and permanent tags are retained. Physical line numbers refer to raw HTML, not rendered page lines.

- **11.39 Changing the prescribed singularities**, docs/sections/normalization-and-weak-adjoint-measures--changing-the-prescribed-singularities/index.html, blob e603564ec54844bb2af8483249f427266ef5d83b, lines 7–120. 11.39.1 (03A2FF32 / 675DA440E964, 11–40): direction of strict domination and the (1-epsilon)^n residual coefficient are consistent; the nonpluripolar truncation and smooth-volume null polar-set premises remain dependencies. 11.39.4 (08C88746 / 7DD0741AE5AA, 56–75): both finite-entropy domains must agree, and the supporting minimizer is chosen for the reference on the appropriate side; translation by the smooth volume log-ratio is bijective. 11.39.5 (A3DB6DC1 / 80C599ADD5CB, 80–101): the two scalar/dual comparison errors give the stated 2delta defect; uniformly integrable densities justify varying bounded tests, not merely weak measure convergence. 11.39.6 (2690C659 / FCFB63397013, 109–116) is the stated specialization.
- **11.40 Varying positive backgrounds**, docs/sections/normalization-and-weak-adjoint-measures--varying-positive-backgrounds/index.html, blob 7ad25146c373ced93115f4a239f2312d645fcfe1, lines 7–96. 11.40.1 (72F3F602 / 133439CA2DC1, 20–38): maximum/minimum Hessian order yields the correct determinant bounds and dd^c changes are absorbed by potential translation. 11.40.3 (EF89353C / 9B8101BC6CE4, 43–62) uses the same dual sublevel estimate. 11.40.4 (79F56B44 / 1A47D2E8B6D5, 70–85): derivative in (potential, log scalar) is Delta_Omega h-q, so q=-integral g dmu is the required sign; Fredholm compatibility and uniqueness are essential. The path integration in 11.40.5 (B7921C3AB602, 89–96) retains the additive constant at zero.
- **11.41 Divisorial types and moving sections**, docs/sections/normalization-and-weak-adjoint-measures--divisorial-types-and-moving-sections/index.html, blob 59a70ec4e6bcd48d1a3ea3221427584624796d3a, lines 7–212. 11.41.1 (37CD7A01 / 7281EDB812F1, 20–48): removal of all generic divisorial coefficients and equality off the analytic set are distinct steps; canonical representatives avoid subtracting infinities. 11.41.3 (B7148C83 / BF6A67E9A40E, 59–74): uniform residual convergence, common Hessian lower bound and evaluation at a finite maximum prove normalization convergence. 11.41.5 (5957D177 / CC6718D255AC, 98–134): the uniform positive-part integral controls the residual supremum by local submean; the smaller-background condition follows from positivity of beta-(1-epsilon)theta. 11.41.6 (0A60D53E / C87E852ED386, 139–165): strict loss uses ellipticity of the mixed positive form, an interior maximum away from a nonempty divisor, and connectedness; no positivity of its smooth curvature representative is required. Corollary 11.41.7 (1483E1DE / 39C3764F36BD, 170–183) uses a small effective divisor multiple, not the whole divisorial current. The product example 11.41.8 (121EF09A28A5, 191–212) has the correct binomial factor and projective factor exponent k.

Selected dependency read: docs/sections/gauduchon-metrics-and-linear-mass--the-adjoint-measure-of-the-linearization/index.html (blob 519e50338be6560f6b2856fddce212738f5109bc), lines 7–43, Proposition 11.23.2 permanent 0B0003A3A873. Its Fredholm range and Gauduchon multiplier remain conditional inputs. Theorem 11.33.5 (D502EBBF / 5E3583383688, scalar-functional section blob fff86de757578ed2be369ba752123f62f3d31044, line 89 statement) identified as the scalar-continuity premise. Bounded equation existence, stability, nonpluripolar removal, dual entropy compactness, strict domination, and the smooth adjoint chain are not transitively certified in this run. No affected printed theorem needs correction; optional strengthening belongs after 11.41.3, and may be used in applications requiring convergence against finite-Lq test densities or TV convergence of these equation measures.

Coverage: three whole current direct conditional section readings; selected dependency inspection only; historical first visits not asserted. Chapter 11 actual 49 section identifiers agree with its 49 matrix rows, and the complete matrix has 747 unique numbered rows. No new confirmed printed errors, new demonstrated proof gaps, or complete upstream certificates. All user-excluded regularization/Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss programmes remain deferred-by-user. No tests, builds, CI, publication, or production edits.
