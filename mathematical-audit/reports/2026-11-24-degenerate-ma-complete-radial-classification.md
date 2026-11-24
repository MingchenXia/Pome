# Complete bounded radial solution interval for the open-band degenerate MA example

2026-11-24; production main b6933b772f41b45918f7e25ed1afbbb1fd892272.

## POME-DEGENMA-OPEN-BAND-RADIAL-CLASSIFICATION-001

Low severity / verified conditional deduction, NOT a printed theorem error. Proposition 14.26.14 gives a continuum, and Theorem 15.20.4 gives the unique exchange-invariant radial member. We classify *all bounded block-unitary-invariant solutions*, conditional on the existing bounded-product flux lemma 15.20.5 and the C^{1,1} product identification 5.28.5, without certification of their full upstream chains.

### Immutable anchors and coverage

Paths under docs/sections/, each with suffix /index.html, on the above main; source book non-kahler-pluripotential-theory.

- uniqueness-for-degenerate-equations, blob 0c1c033d7a1a76b9ccf9fbd5b4bfc8321a33f208: entire introductory mathematics 7–32, Eq. 14.20.1 permanent 2EA7CA32AE91.
- uniqueness-for-degenerate-equations--extrema-and-density-sublevels, blob 044f55457f10b2f640052854a7f5f14b8403be82: entire mathematical lines 7–223. Theorem 14.21.3 source 61B8DD0F / permanent 6EB399397505; contact lemma 14.21.5 F0F5D947 / 59B8A4C8DA05; maximum principle 14.21.6 E67FD2CF / 96D40C4808C2; Theorem 14.21.13 A7BC9EDB / 61851D05B072. Checked Lipschitz-gradient null-set avoidance, strict comparison, contact determinant and separator-disk integration. Connectedness inherited from 14.20. Prior sharp cofactor and Holder sublevel findings not re-counted.
- uniqueness-for-degenerate-equations--smooth-nonuniqueness-for-a-degenerate-density, blob 7240d97e9192c70acf09f755ec90a5420bc11ef7: entire mathematical lines 7–280. Theorem 14.26.1 777CF1F4 / 050594389138; rank-one formulas 26–66, coefficient construction 73–113, positivity and nonclosedness 145–161, Proposition 14.26.14 BD1DFC95 / 3A73F825D91B lines 201–276; Eq. 14.26.16 BC03110E / 2EC8417EFF1E lines 250–252. Checked wedge factor 6, flat joins, sign of dR, positivity correction, absence of Hessian atoms, symmetric switching.
- equations-with-prescribed-singularities--symmetry-and-the-selected-projective-limit, blob 5939b066b23315e66c9f8ec26a97677825fa2a16: entire mathematical lines 7–241. Theorem 15.20.4 4BBFED99 / 72B88B8B1639; Lemma 15.20.5 DCDE8A82 / 5D3F7173CA27 lines 79–130, Eq. 15.20.6 1C4AC4C7 / B34A7F7705B9; exterior calculation lines 154–182; Proposition 15.20.8 39588581 / 517F0BB04B80 lines 194–237. Checked weak flux, positive upward jump integral, exterior nonvanishing and integration constant, cluster-limit selection. Scalar convolution here is not the excluded Demailly programme.

Sections 14.22–24 were fetched in a batch but not fully assessed; no upgrade. No historical first-visit claim.

### Statement

Use exactly the data x,y,z,p,z_0,a,b,r,rho of section 14.26 and choose rho even. Set Z(r)=integral_0^r z_0(s) ds and S=Z(1)>p(0)>0. For C in [-S,S] put h_C=0 outside [-1,1] and on the band

    h_C(r)=max(-p(r),min(p(r),C-Z(r))).

Let G_C be a primitive and u_C the supremum-normalized extension of G_C(r)-rho(r) to P^3. Then C -> u_C is a bijection onto the normalized bounded U(2)xU(2)-invariant solutions for the fixed density of Theorem 14.26.1. All are C^{1,1}; exactly the two endpoints are C^2 (indeed smooth). Exchange sends u_C to u_{-C}, so u_0 is the printed symmetric solution. In the uniform topology the parametrization is a homeomorphism and for C<D,

    osc_X(u_D-u_C)=integral_{-1}^1 (h_D-h_C) dr <= 2(D-C).

No classification of nonradial solutions is asserted.

### Necessity: exterior and corridor

Lemma 15.20.5 gives a continuous locally BV slope h, -x<=h<=y, dh+z dr>=0, and the printed ODE where (x+h)(y-h)>0. The endpoint-integral argument of section 15.20 lines 154–160 needs no exchange invariance: on r>1, k=xyz>0 gives strict horizontal positivity. The Fubini–Study calculation on r>=2 gives a=sigma+h in (0,1), with a(1-a)a'=sigma(1-sigma)sigma'. Boundedness of G forces lim a=1; integrating the strictly increasing primitive a^2/2-a^3/3 fixes the constant to zero. Hence h=0 on r>=2 and ODE uniqueness propagates this on r>1. Apply this to the block-exchanged solution (the data, not the given solution, are invariant), giving h=0 on r<-1. Continuity gives h(±1)=0.

On (-1,0], y=p; on [0,1), x=p. On [-1,-1/3], chi=0 and z_0=p', so dh+p' dr>=0 implies h+p is nondecreasing from zero. On [-1/3,0], a=0 gives the lower bound directly. On [0,1/3], b=0 gives the upper bound; on [1/3,1], z_0=-p', so h-p is nondecreasing to zero. Thus -p<=h<=p everywhere, using distributional monotonicity, not assuming h absolutely continuous.

### Necessity: exact clipping

Set L=Z-p, U=Z+p. Both are continuous nondecreasing, since z_0>=|p'|, and L<U on the open band. Put H=h+Z. On E={L<H<U} both horizontal coefficients are strictly positive, and the zero-density ODE gives h'=-z_0, so H is constant on every component.

A component (i,j) with i>-1 cannot enter from L: H=L(i) on the component contradicts monotonicity of L. Similarly it cannot exit at U if j<1. After touching L at an interior point it cannot depart to the right: a component of {H>L} starting from a lower contact lies strictly below U near its left endpoint by continuity, and the initial interior segment has H constant at L(contact), a contradiction. The reverse-time argument forbids departure from U to the left. Thus E is either empty or a single interval. If empty, continuity and L<U force h=p everywhere or h=-p everywhere. If nonempty, H=C there, H=U before it and H=L after it, by the two no-departure arguments. Since L(-1)=U(-1)=-S, L(1)=U(1)=S, one has -S<C<S. Monotonicity identifies H with max(L,min(U,C)), proving the clipping formula. This also excludes singular-continuous slopes.

### Sufficiency

For -S<C<S, the interior set {L<C<U} is nonempty: Z takes value C at an interior point where p>0. It is an interval by monotonicity. The clipped slope is Lipschitz, zero at ±1 and outside the band. Its primitive extends across the omitted projective lines because it is constant near the ends. On the interior branch h'=-z_0, so the radial coefficient vanishes. On h=p, all coefficients are nonnegative: if b=0 the Q coefficient vanishes; otherwise r>1/3, chi=0 and z_0=-p', so the radial coefficient vanishes. On h=-p, if a=0 the P coefficient vanishes; otherwise r<-1/3 and z_0=p', so the radial coefficient vanishes. These derivative identities hold almost everywhere on the equality sets of Lipschitz functions, even on plateaus. The same check applies to the pure endpoints. Outside the band all forms equal omega_0. Eq. 14.26.16 and Proposition 5.28.5 give exactly the required measure by the rank-one wedge formula. Continuous slopes preclude additional hypersurface Hessian atoms.

The endpoints C=-S,S give -p,p respectively. For an interior C choose r with Z(r)=C and p(r)>0; h_C(r)=0, while every other parameter gives a nonzero slope there. The two endpoint slopes also differ. Equality of normalized potentials implies equality of slopes, proving bijectivity.

### Regularity, symmetry and topology

For an interior C the transition interval (i,j) satisfies -1<i<j<1, since at -1 C>U(-1) and at 1 C<L(1). The slope is p before i, C-Z on (i,j), and -p after j. If i<=0, p'(i)>=0 but -z_0(i)<0, giving different one-sided derivatives at i. If i>0 then j>0, and -p'(j)>0 while -z_0(j)<0, giving different derivatives at j. A smooth transverse r-curve proves failure of second differentiability there. Only the two original endpoints are C^2; no assertion of two kinks for every parameter.

Z is odd, p even, so h_{-C}(r)=-h_C(-r); even rho gives exchange symmetry. Clipping is monotone and 1-Lipschitz in C. The primitive difference for D>C is nondecreasing, constant on the ends, hence has oscillation equal to the claimed integral. Supremum normalization does not change oscillation; the normalized difference has minimum <=0<=maximum, so its uniform norm is at most its oscillation. Compactness of the parameter interval and Hausdorffness of the uniform topology give the inverse continuity.

### Proposed addition and dependencies

Add this classification after Lemma 15.20.5 to avoid forward dependence, preserving existing statements and tags. The symmetric uniqueness part of 15.20.4 is recovered as the unique fixed point; positive-exponent convergence still depends on the existing PDE compactness and uniqueness. No circular use of the symmetric conclusion. Bounded Bedford–Taylor continuity and 5.28.5 remain internal premises, not fully certified. No new confirmed printed error or local proof gap. All excluded Demailly/Bergman/L2/OT/multiscale/positivity-loss programmes remain deferred-by-user. No builds, tests, CI or production edits.
