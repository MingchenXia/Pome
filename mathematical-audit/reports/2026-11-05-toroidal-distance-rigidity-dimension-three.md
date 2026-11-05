# The dimension-two boundary of distance/subharmonicity rigidity (2026-11-05)

**Finding:** POME-PLANAR-DISTANCE-TORUS-DIMENSION-001.  
**Severity / status:** low / verified conditional deduction. No printed theorem is false, and this is neither a general proof certification nor a proposed change to the existing R^2 statements.

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Integrated reading edition:** docs/sections/planar-boundary-distance-and-convexity/index.html; main blob 25fd0fd57d3e51f9224a25341ace77584b2a1a2a.  
**Exact anchors:** Proposition 3.9.1 at physical lines 7–33 (source klimek-pluripotential-theory:79D31B13, permanent 964B6728E795); Proposition 3.9.2 at lines 38–87 (source klimek-pluripotential-theory:219D9DEC, permanent 59D258340230); Proposition 3.9.3 at lines 92–107 (source klimek-pluripotential-theory:366D2F88, permanent BBEB233BF8A4).

## Claims actually checked

The integrated propositions assert **planar** rigidity: for connected open D in R^2, subharmonicity of minus the distance to the complement characterizes convexity (3.9.1); for a nonempty proper closed F contained in a connected open G in R^2, subharmonicity of the distance to F on G implies convexity (3.9.2). Proposition 3.9.3 adds a connected-neighborhood hypothesis for the planar complement. All their R^2 dimensional qualifications are essential. Their printed proof structures were examined, particularly the genuinely two-dimensional argument at lines 60–70 of 3.9.2: a symmetric 2-by-2 Hessian with one zero eigenvalue and nonnegative trace is positive semidefinite. That linear-algebra step fails in dimension at least three.

The following **single explicit compact, smooth-boundary toroidal construction** disproves direct extensions of all three implications to every real dimension m >= 3, *even if all the stated connectedness conditions are retained*. This is a sharp dimension limitation, not a counterexample to what Pome prints.

## Construction in every m >= 3

Fix R=4, r=1, and delta=1/2. For x=(x_1,x_2,x'') in R^2 x R^(m-2) write

$$
s=(x_1^2+x_2^2)^{1/2},\qquad
q(x)=\bigl((s-R)^2+|x''|^2\bigr)^{1/2}.
$$

Let C be the circle x''=0, s=R. Then q(x)=dist(x,C), including the axis s=0. Put

$$
D=\{q<r\},\qquad F=\{q\le r\}=\overline D,\qquad
G=\{q<r+\delta\}.
$$

D is an open, bounded, connected solid tube around a circle, F is nonempty, proper, compact, and connected, and G is open, bounded, connected, and contains F. Both D and F are nonconvex: the two antipodal points (R,0,0) and (-R,0,0) lie in C and hence in D and F, whereas their midpoint is the origin, with q(0)=R>r. The boundary q=r is smooth because q>0 and s>0 there, and |grad q|=1.

**Exact distance identities.** For any x with q(x)<r, the 1-Lipschitz property of q gives dist(x,R^m\D) >= r-q(x). Let a be a nearest point of C. Moving from a through x along the normal straight segment out to distance r from C reaches the boundary in length r-q(x). The segment stays in s>0 because r<R; at q(x)=0 choose any normal direction. Therefore

$$
\operatorname{dist}(x,\mathbb R^m\setminus D)=r-q(x)\quad(x\in D).
$$

The same argument, moving inward from x to q=r for x outside F, yields

$$
\operatorname{dist}(x,F)=\max\{q(x)-r,0\}\quad(x\in G),
$$

in fact on the whole ambient Euclidean space. These equalities use no regularity or analytic theorem.

## Laplacian and the core-circle issue

Inside G we have q<3/2<R/2 and consequently s>=R-q>5/2, so cylindrical coordinates and the following smooth calculation are valid. For epsilon>0 define

$$
q_\epsilon(x)=\sqrt{(s-R)^2+|x''|^2+\epsilon^2}.
$$

Using the Euclidean cylindrical Laplacian

$$
\Delta=\partial_s^2+s^{-1}\partial_s+\Delta_{x''}
$$

and the elementary radial derivative identity in m-1 normal coordinates gives the **exact formula**

$$
\Delta q_\epsilon
=\frac{1}{q_\epsilon}
\left(m-2+\frac{\epsilon^2}{q_\epsilon^2}+\frac{s-R}{s}\right).
$$

Because |s-R|<=q<3/2 and s>5/2, the bracket is greater than or equal to (m-2)-3/5 >= 2/5 for every m>=3. Thus every q_epsilon is smooth and strictly subharmonic on G. Moreover

$$
0\le q_\epsilon-q\le\epsilon
$$

uniformly. Passing directly to the submean inequality under uniform convergence shows that q is continuous and subharmonic on G, **including at the core q=0**, without invoking an unjustified smoothness or ignoring a distributional contribution at that circle. Away from the core, the ordinary limiting formula reads

$$
\Delta q=\frac{m-2}{q}+\frac{s-R}{s q}>0.
$$

For m=2 the leading (m-2)/q term vanishes; this is precisely why the higher-dimensional construction does not contradict the planar propositions.

## Consequences for the three printed planar assertions

1. In D, minus the distance to the complement is q-r, which is subharmonic by the preceding calculation. D is connected, bounded, smooth-boundary, and nonconvex. Thus the implication of **3.9.1** fails in every m>=3 despite strong regularity and connectivity.
2. On G, the distance to the closed F equals max(q-r,0), a maximum of two continuous subharmonic functions, hence subharmonic. F and G satisfy the corresponding connectedness and containment hypotheses while F is nonconvex. Thus the putative higher-dimensional analogue of **3.9.2** fails.
3. Let Omega=R^m\F and U={r-delta/2<q<r+delta/2}. Then Omega is connected (the exterior of this solid tube), U is a connected open collar of the smooth boundary of Omega, and the same distance-to-F is subharmonic on U. This also defeats a direct m>=3 generalization of the connected-collar implication of **3.9.3**.

In each case the **printed statements are specifically for R^2 and remain correct**. No source, reader body, numbering, source attribution, tags, or canonicalization are to be changed.

## Impact and scope limits

This explicit geometric model explains the algebraic obstruction to lifting the 2D Hessian argument to m>=3. It may be used as an addendum if someone later formulates higher-dimensional analogues of §§3.9.1–3.9.3; it is **not** a repair of an erroneous theorem, and no current direct dependent is asserted without a full reference search. The exact integrated propositions and their planar proofs were selected for checking; the entire classical-potential chapter, full earlier regularity lemmas, and all of §3.9 were **not** certified.

**Dependencies:** elementary Euclidean distance geometry, cylindrical differentiation, the submean definition of subharmonicity, and stability under uniform limits and finite maxima (proved here at the relevant steps). No excluded Demailly approximation/regularization or associated Bergman/L2/OT/multiscale/positivity-loss argument is used.

**Disposition:** keep all earlier findings, permanent tags, and source versions intact. Excluded regularization-related ledger items remain deferred-by-user, not resolved. All changes in this session are audit Markdown only; no tests, builds, CI, formal verification, publication, or production-source edit.
