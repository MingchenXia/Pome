# Continuous homogeneous psh functions and projective-complement convexity

Date: 2026-11-28. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit-only; no production edits.

## Finding POME-COMPLEMENT-CONTINUOUS-HOMOGENEOUS-PSH-001

Low severity / verified conditional deduction (optional strengthening, not a false printed theorem or a demonstrated proof gap).

Anchor: docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--homogeneous-plurisubharmonic-functions-and-hopf-complements/index.html, blob 64aaae0cd5320ede513a1dfbda5bf79a80863519. Proposition 11.21.1, permanent tag 1204B7FDAE31, source non-kahler-pluripotential-theory:C8EC3706, lines 19–63. In particular the radial maximum at lines 36–54 can be retained without differentiating the homogeneous psh function.

**Claim.** Let F be a positive-rank holomorphic vector bundle on a connected compact complex manifold B of positive dimension n, let r=rank F and N=n+r. If F minus its zero section admits a positive *continuous* plurisubharmonic function G with G(cv)=|c|^2G(v), the least smooth convexity index of U_F=P(O_B ⊕ F) minus P(O_B) is N. No smoothness, fiber convexity, or strict plurisubharmonicity of G is needed.

Proof. The upper bound N is the s=0 case of 11.18.2 on the compact base (permanent B93CB03C68B7, source 9BF81039). For the lower bound, suppose a smooth exhaustion psi has at least two positive Levi eigenvalues outside a compact K. G is comparable to a fixed Hermitian squared norm by homogeneity and positivity on the compact unit sphere bundle. The set S={G=1} is compact, not necessarily a manifold. For small t>0 the sets tS lie outside K in the affine chart [1:v]. Put M(t)=max_{v in S} psi([1:tv]). Uniform bounds on the radial derivatives of psi over S on each compact positive t interval imply that M is locally Lipschitz. Moreover M(t) tends to +infinity at zero, since compact sublevel sets cannot accumulate on the removed zero section. As in the printed proof, absolute continuity gives a differentiability point t with M'(t)<0. Choose v in S attaining the maximum and p=tv. Suppress the chart [1:v] in notation. By the two-sided touching inequality M(t+h)>=psi((t+h)v), equality at h=0 gives d/dt psi(tv)=M'(t). In particular the radial derivative A=d/ds psi(sp)|_{s=1}=t M'(t)<0.

For x in a sufficiently small open neighborhood of p in F minus zero, the implicit function theorem supplies a smooth positive real function sigma(x) near 1 with psi(sigma(x)x)=psi(p). Here scalar multiplication is on fibers; the base point of x is unchanged. By shrinking, psi(sx) is strictly decreasing in s for x near p and s near 1. Continuity of G ensures that a(x)=t/sqrt(G(x)) is also near 1, and G(a(x)x)=t^2. Maximality of p on tS gives psi(a(x)x)<=psi(p)=psi(sigma(x)x). Strict decrease yields a(x)>=sigma(x), i.e.
 
    G(x) <= H(x):=t^2/sigma(x)^2,

with equality at p. Thus H is a smooth upper test for the continuous psh G at p. By the submean inequality on complex coordinate lines through p, its Levi form at p is positive semidefinite: the average of H on each small disk boundary is at least H(p), and the quadratic expansion gives the asserted sign.

Differentiating the implicit equation gives d sigma=-d psi/A at p. Consequently dH=(2t^2/A)d psi there, with c=2t^2/A<0. On the nearby smooth real hypersurface psi=psi(p), uniqueness of the implicit solution gives sigma=1 and H=t^2. The real Hessian of H-c psi therefore vanishes on pairs of tangent vectors to that hypersurface at p: its differential vanishes at p, and its restriction to the hypersurface is constant. Applying this to a tangent vector and its complex rotation gives

    Levi_H|ker(partial psi)=c Levi_psi|ker(partial psi).

Since c<0 and Levi_H>=0, Levi_psi is nonpositive on this complex hyperplane. Hence it has at most one positive eigenvalue, contradicting the exhaustion condition at p outside K. This proves the claim. No approximation or differentiation of G is involved.

Affected dependents: 11.21.2–5 and the mixed-sum bounds remain valid as written. The deduction also applies to any positive continuous homogeneous psh squared norm, and by 11.17.3 gives lower bounds from closed projective subbundles carrying such a function. It does not determine the mixed-sign Hopf interval on lines 179–185.

## Finding POME-TAUTOLOGICAL-CONTINUOUS-PSH-METRIC-IFF-001

Low severity / verified conditional deduction, optional strengthening. Anchor: docs/sections/gauduchon-metrics-and-linear-mass--convex-norms-and-gauduchon-degrees--strict-positivity-from-the-tautological-metric/index.html, blob 6f9d5aa919f3b4de1626f1b32cee6064393fff7c; Lemma 11.11.1 permanent 40D29F4EF95B, source F0EE457D, lines 19–39.

Every positive continuous degree-two complex homogeneous G on F minus zero corresponds to a continuous Hermitian metric on L=O_{P(F)}(1), by taking the dual of the squared tautological norm. Under this correspondence, G is psh if and only if the local weights phi of the metric h=exp(-phi) are psh (continuous semipositive curvature). In particular G need not be fiber convex.

Proof. In a holomorphic tautological frame e, write G(y,lambda e)=|lambda|^2 exp(phi(y)). If phi is psh, then phi+log|lambda|^2 is psh on lambda≠0 and exponentiation preserves psh by convex monotone composition. Conversely, fix a holomorphic disk in the base chart and a closed subdisk of its parameter domain. Let b be the harmonic extension of the continuous boundary values of the pullback of phi. On the open disk choose a holomorphic function B with real part b. The holomorphic section lambda=exp(-B/2) never vanishes. Its pullback of G is exp(phi-b), which is subharmonic. On approach to the boundary it tends uniformly to 1 because phi and b are continuous up to the boundary; no boundary extension of B is needed. The maximum principle on smaller concentric disks gives exp(phi-b)<=1 throughout the disk. At its center phi is at most the boundary mean. This holds on every such disk, so phi is psh. The local metrics patch by the ordinary dual-frame transformation rule. This also proves log G is psh on F minus zero whenever G is psh, positive and continuous homogeneous. The smooth strict statement in 11.11.1 is unchanged.

Combined with the preceding finding, a continuous semipositive metric on O_{P(F)}(1) forces least smooth convexity index N for the projective complement. This is a sufficient condition, not a converse for the convexity index. No existence assertion for such a metric from mere nefness is made.

## Direct mathematical coverage and boundaries

- Whole direct conditional §11.10, physical lines 7–157, blob 318cdba84254005afa50cbf80bb8535a72fbb800. Checked Example 11.10.1 (two quadratic branches, vanishing uniform margin); 11.10.2 (smooth cutoff patch and maximum, compact finite iteration); 11.10.3 (holomorphic shear convolution preserves both local strict margins); 11.10.4–6 (projectivized gluing, homogeneity, real-line convexity across zero, perturbation by H). All global compactness-dependent steps are read in the compact-base context of §11.9; explicitly repeating compactness in 11.10.4–5 would avoid ambiguity, not a demonstrated failure in that context. This elementary homogeneous convex smoothing is separate from the excluded Demailly approximation programme. No analytic regularization programme reopened.
- Whole direct conditional §11.11, physical lines 7–76, blob 6f9d5aa919f3b4de1626f1b32cee6064393fff7c. Checked the block Levi formula, root of pulled-back Fubini–Study metric and the direction of the dual ampleness convention. The obstruction in 11.9.4 is used conditionally, not independently recertified.
- Whole direct conditional §11.21, physical lines 7–185, blob 64aaae0cd5320ede513a1dfbda5bf79a80863519. Checked radial derivative sign, complex tangent dimension, Hopf bundle automorphy q^(2b)|a|^2=1, curvature sign -b, topology and flat restriction to elliptic fibers, direct sum and mixed lower bounds. The latest historical log already mentions selected §11.21 work; this is a present-main whole direct review, not a historical first visit.
- Selected prerequisites §11.17.3, physical lines 129–148, blob d49b7d4f2a213c8b70abfe2f337562202bb58dfb (closed submanifold restriction and dimension count); §11.18.1–2, lines 19–72, blob fab309d460a8411fefcd1ef32a094927d6feea10 (reciprocal Hessian, compact cutoff exhaustion). The earlier compact-base qualification in 11.18.2 is retained, not counted as a new finding. §11.9 contextual lines 7–45 only.
- Actual current chapter 11 TOC contains 49 unique section numbers, equal to the corresponding matrix rows. The global matrix contains 747 unique rows; no new full-TOC comparison for other chapters in this run.

Two optional deductions; zero newly demonstrated printed errors or proof gaps; zero fully verified transitive proof chains. Demailly approximation and dedicated Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss work remain deferred-by-user, neither resolved nor certified. No build, test, CI, publication, source, registry or permanent-tag changes.
