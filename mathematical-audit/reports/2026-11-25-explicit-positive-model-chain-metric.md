# Explicit quantitative chain metric on positive-volume ordinary models

Date: 2026-11-25. Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Starting review head: 57c99a772efdcde9a580bc44627ae90bc8e76c98.

## POME-MODEL-EXPLICIT-CHAIN-METRIC-001

Severity low; status **verified conditional deduction**, not a false theorem or proof gap. The printed Theorem 13.27.4 has a valid chain-metrization argument. The alternative below gives a single explicit edge weight, quantitative two-sided estimates, and the same complete uniform structures, without the recursive choice of entourages.

### Integrated anchors and inputs

- `docs/sections/volumes-under-bounded-mass--cauchy-convergence-of-model-potentials/index.html`, blob 390f280e62ce8ba01de30f6b1ed52b4aa7fb10e4: Definition 13.22.1 (non-kahler-pluripotential-theory-82BBCEC3 / A220D62C8412), lines 11–27; separation 13.22.4 (38359A611D4C), 56–90; Proposition 13.22.5 (non-kahler-pluripotential-theory-13BB878E / 412DBAD823B9), 98–134; Theorem 13.22.7 (non-kahler-pluripotential-theory-54605E21 / 62ECCE0A41E6), 139–196.
- `docs/sections/volumes-under-bounded-mass--a-complete-metric-on-positive-volume-models/index.html`, blob bf369ddac8a96939938efeca55db76faae3109c8: Proposition 13.27.2 (non-kahler-pluripotential-theory-17A47BEB / 44E1935166EC), lines 77–103; Theorem 13.27.4 (non-kahler-pluripotential-theory-B2475A61 / 126E2D85CA62), 108–181; Corollary 13.27.9 (non-kahler-pluripotential-theory-FE60915F / 5AF48DFCEE5A), 186–193.
- `docs/sections/volumes-under-bounded-mass--volume-deficits-and-relative-full-mass/index.html`, blob 28323e5b08b0f7e53567f641bd9e4223472bc331, Lemma 13.18.1 (non-kahler-pluripotential-theory-ED39D93A / 92ABF533A916), lines 11–49. Use its **strict** stretching condition, not endpoint attainment.

Hypotheses: precisely the big background and bounded-mass setting of §§13.22, 13.27, positive-lower-volume ordinary models on the connected compact X of the collection, with finite M=U(V_theta)>0. Write L=lower volume, U=upper volume, d(p,q)=2U(max(p,q))-U(p)-U(q). Use the printed monotonicity and homogeneous positive mixed-product volume estimate U((1-t)z+th) >= (1-t)^n U(z), the separation and completeness results of §13.22, and lower-volume continuity in §13.27.2. These are inputs, not newly certified transitive chains. No regularization construction is invoked in the deduction.

### Finite-join estimate

For a pair p,q put s=d(p,q), m0=min(L(p),L(q))>0, and

$$
a(p,q)=\min\{1,(s/m_0)^{1/n}\}.
$$

For any finite chain of positive-volume models p_0,...,p_N, let z_i=max(p_0,...,p_i). Then

$$
0\le U(z_N)-U(p_0)\le nM\sum_{i=1}^N a(p_{i-1},p_i).
$$

Proof: fix an edge with p=p_{i-1}, q=p_i, r=z_{i-1}, z=max(r,q), and w=max(p,q). We have U(w)-U(p)<=s and L(w)>=m0. If a=1, monotonicity and U<=M give the desired edge estimate U(z)-U(r)<=M<=nM. Otherwise, choose any a<t<1. Lemma 13.18.1 applies with b=1/t, since t^{-n}(U(w)-U(p))<m0<=L(w). Thus there exists h with (1-t)w+th<=p; in particular h<=p (at finite points, and also on the pole set by the extended inequality and w>=p, or by taking the inequality on the nonpolar finite locus and extending by the PSH comparison principle). More explicitly, the inequality yields h<=p wherever p and w are finite, hence almost everywhere, which suffices for the PSH inequality everywhere. On the same full-measure finite locus, if z=r then (1-t)z+th<=r, and if z=q then (1-t)z+th<=(1-t)w+th<=p<=r. Thus the inequality holds globally by the PSH comparison principle. Monotonicity and the mixed-product estimate give U(r)>=(1-t)^n U(z), hence U(z)-U(r)<=(1-(1-t)^n)M<=ntM. Let t decrease to a. This includes a=0 without asserting existence at the forbidden strict endpoint. Sum the edge estimates.

Reverse the chain to bound U(z_N)-U(p_N) by the same sum (the finite maximum is independent of order). Since max(p_0,p_N)<=z_N,

$$
d(p_0,p_N)\le 2nM\sum_{i=1}^N a(p_{i-1},p_i).
$$

This is a bound for chains of arbitrary finite length, with no loss growing exponentially in the number of edges. It uses the printed finite-max argument of 13.22.5/7 but allows arbitrary chains, not just a fast subsequence.

### Explicit complete metric and bounds

Define the edge cost c(p,q)=a(p,q)+|1/L(p)-1/L(q)|. Let rho(p,q) be the infimum of total costs over all finite chains in M_+ from p to q (single-edge chains are permitted). Then

$$
\frac{d(p,q)}{2nM}+\left|\frac1{L(p)}-\frac1{L(q)}\right|
\le \rho(p,q)
\le \min\{1,(d(p,q)/\min(L(p),L(q)))^{1/n}\}
+\left|\frac1{L(p)}-\frac1{L(q)}\right|.
$$

The lower estimate holds for every chain separately by the finite-join estimate and the real triangle inequality, so it survives the infimum. The upper estimate uses the single edge. Costs are finite and symmetric; concatenation and infimum give the triangle inequality. Constant chains have zero cost; the lower bound and positive-volume separation imply rho(p,q)=0 only for p=q. This proves rho is a metric.

For a fixed p, rho(p_j,p)->0 implies d(p_j,p)->0. Conversely d(p_j,p)->0 gives L(p_j)->L(p)>0 by Proposition 13.27.2, hence the explicit upper bound gives rho->0. The same proof applies to nets: if a scalar limit fails, a sequence can be selected from the bad tails with d<1/j, contradicting the printed sequential continuity at p. No countable cofinality is assumed.

If a sequence is rho-Cauchy, it is d-Cauchy and the reciprocals 1/L(p_j) are Cauchy by the lower bound. They are bounded and positive, so a tail has L>=delta>0. By Theorem 13.22.7 the sequence converges for d to an element of M_delta, hence for rho. Conversely d-Cauchy and Cauchy reciprocals give rho-Cauchy by the upper bound and a common positive lower bound on a tail. This proves completeness and the same Cauchy criterion as the printed theorem.

For p,q in M_delta, the single-edge upper estimate and (13.27.3) imply

$$
\rho(p,q)\le
\min\{1,(d(p,q)/\delta)^{1/n}\}
+\frac{nM}{\delta^2}\min\{1,(2d(p,q)/\delta)^{1/n}\}.
$$

Together with d<=2nM rho, this proves quantitative uniform equivalence on every M_delta. Its completeness follows from the fixed-stratum theorem. Every Cauchy net in a complete metric space converges: choose increasing indices from successive 1/j Cauchy tails, obtain a Cauchy sequence, and use the tail condition to show the original net converges to the sequence's metric limit. This is a selection from tails, not a claim that the directed set has a countable cofinal subset.

The metric is not asserted bounded by 1 or equal to the printed chain metric. If a bounded version is wanted, min(1,rho) is complete with the same convergence and Cauchy nets. Neither a triangle inequality for d itself nor sharpness of the quantitative exponents is claimed.

### Affected results / proposed supplement

Keep Example 13.27.1, Proposition 13.27.2, Theorem 13.27.4 and its current proof. The explicit alternative can be added after Theorem 13.27.4; Corollary 13.27.9 also holds with rho **conditional on** the characterization in 13.24.5. Its analytic approximation input 13.24.3 is not reopened and remains deferred-by-user insofar as it invokes the excluded programme. The new metric is independent of that density claim.

### Actual coverage

- §13.22 entire mathematical text, lines 7–217: normalization, projection invariance, positive-volume separation, quasi-triangle estimate, fast-subsequence completeness, and the strict-stratum curve counterexample. Historical partial coverage exists; not a first-ever visit.
- §13.27 entire mathematical text, lines 7–193: the two-line blowup example (mixed intersections and 2a² triangle defect), lower-volume modulus, recursive entourage triple composition, dyadic finite-chain induction (strict half-cost split), completeness, and conditional ideal-model corollary. Historical partial coverage exists.
- §13.18.1 lines 7–49: selected repeat of the strict stretch hypothesis and proof. Not a transitive certification.
- §8.1 `docs/sections/complex-hessian-equations/index.html`, blob 5331b937ccdaba51f1ec006d5e72dc84f7addfbf, section tag CFD38285654D: complete four-paragraph introduction, reviewed as exposition only; no equation theory certified here.
- Current actual table of contents `docs/chapters/index.html`, blob c0c07abf4d8f7575b54cff2ec694fcf987f51cf8: parsed section hyperlinks and checked exactly 747 distinct numbered rows against SECTION_MATRIX, no missing or extra numbers.

No new confirmed printed error, demonstrated proof gap, or complete upstream proof-chain certificate. No tests, build, CI, production edits, or website publication. Existing excluded programme records remain deferred-by-user.