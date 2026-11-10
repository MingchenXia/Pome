# Exact restriction of toric character sections to orbit closures

**Date:** 2026-11-10  
**Stable ID:** `POME-TORIC-FACE-RESTRICTION-EXACT-001`  
**Classification:** **low / verified conditional deduction**. The finite-degree restriction calculation is complete under the integrated toric chart, orbit and character-basis results; it does **not** certify those upstream theorems in full, nor any general analytic restricted-volume theorem. **No printed result refuted.**

**Production main (reviewed without modification):** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

## Reading-edition anchors and scope

- `docs/sections/convex-analysis-and-toric-potentials--fans-divisors-and-character-sections/index.html`, blob `7ad2e6dbdd0ce59e1bf08cd9cb3c046e8c87ff6c`. Proposition **21.9.1**, source `foundations-of-pluripotential-theory:4C5E5EB3`, permanent `9FD0EEED0DBF`, physical lines **10–30**: face/normal-fan correspondence. Proposition **21.9.2**, source `:86CCC496`, permanent `7B4A7CC50CDC`, lines **34–62**: torus orbits, coordinate vanishing and orbit closures. Proposition **21.9.3**, source `:43543C56`, permanent `C62B8871AA1C`, lines **69–102**: chart transition monomials. Lemma **21.9.4**, source `:D75B0BB2`, permanent `00432B20A966`, lines **112–134**: Laurent uniqueness/convergence. Theorem **21.9.5**, source `:BD98CC5B`, permanent `69D3D97E7701`, lines **138–167**: character basis of all global sections of \(L^k\).
- `docs/sections/convex-analysis-and-toric-potentials--smooth-lattice-polytopes-and-projective-charts/index.html`, blob `f442a7b663689b97a9b89689b8b7ae8b366a53fe`. Lemma **21.8.2(4)**, source `foundations-of-pluripotential-theory:86BADE82`, permanent `41C54729DBFD`, lines **24–55**: primitive edge coordinates and dual inward normals. Theorem **21.8.3**, source `:0F7315B0`, permanent `E49F0370E203`, lines **107 onward**: smooth toric vertex charts.
- The already printed §21.9.5 restricts its final lattice count to \(X_P\). The result below supplies **simultaneous face-wise finite-degree restriction ranks**, not the previously audited facet *vanishing-weight distribution*, star-subdivision jet model, invariant-divisor formula, or polytope-translation character shift.

## Proposition: exact image, kernel and restricted volume for every face

Let \(M\cong\mathbb Z^n\), let \(P\subset M_\mathbb R\) be a full-dimensional **smooth lattice polytope**, and use precisely the projective \(X_P,L\) of §§21.8–21.9. For a nonempty face \(Q\subseteq P\), set \(d=\dim Q\), let \(O_Q\) be the torus orbit of Proposition 21.9.2, and let \(V(Q)=\overline{O_Q}\). For **every integer \(k\ge0\)**, the restriction
\[
\operatorname{res}_{Q,k}:H^0(X_P,L^k)\longrightarrow
H^0(V(Q),L^k|_{V(Q)})
\]
is **surjective**, with
\[
\boxed{\begin{aligned}
\ker\operatorname{res}_{Q,k}
 &=\bigoplus_{m\in(kP\cap M)\setminus(kQ\cap M)}
     \mathbb C\,\chi^m s_0^k,\\
H^0(V(Q),L^k|_{V(Q)})
 &\cong\bigoplus_{m\in kQ\cap M}\mathbb C\,
           (\chi^m s_0^k)|_{V(Q)},\\
\operatorname{rank}\operatorname{res}_{Q,k}
 &=\#(kQ\cap M).
\end{aligned}}
\tag{R}
\]
Here \(0Q=\{0\}\), and its unique lattice point gives the constant section at \(k=0\). The affine lattice relevant to growth is \(M_Q=M\cap\operatorname{span}_{\mathbb R}(Q-v)\) for any vertex \(v\in Q\); it has rank \(d\).

For \(d\ge1\) the exact ranks yield
\[
\operatorname{rank}\operatorname{res}_{Q,k}
=\operatorname{vol}_{M_Q}(Q)\,k^d+O(k^{d-1}),
\qquad
\boxed{\operatorname{vol}_{X_P|V(Q)}(L)
=d!\operatorname{vol}_{M_Q}(Q),}
\tag{V}
\]
where the volume on the left is defined **section-theoretically** by the asymptotic restricted-image ranks \(d!\limsup_{k\to\infty}k^{-d}\operatorname{rank}\). The volume on the right uses fundamental covolume one in \(M_Q\), and the \(0\)-dimensional convention is \(\operatorname{vol}_{X_P|V(Q)}(L)=1\).

### Proof: exact restrictions, without normal-generation assumptions

Choose a vertex \(v\in Q\). The affine chart \(U_v\simeq\mathbb C^n\) has coordinates \(w_i=\chi^{e_i}\), with the \(e_i\) a basis of \(M\). By the explicit orbit description in Proposition 21.9.2, the orbit closure is the coordinate subspace
\[
 V(Q)\cap U_v=\{w_i=0:i\in I_{v,Q}\}\simeq\mathbb C^d,
\]
where \(I_{v,Q}\) indexes precisely the facets through \(v\) containing \(Q\). The remaining \(d\) edge directions span the **saturated** lattice \(M_Q\), since they are a subset of a \(\mathbb Z\)-basis of \(M\). Vertex charts with \(v\in Q\) cover \(V(Q)\): a vertex \(v\notin Q\) has \(Z_v=0\) throughout \(V(Q)\), so its chart does not meet that orbit closure.

For \(m\in kP\cap M\), the local coefficient of the global character section \(s_m=\chi^m s_0^k\) relative to the nonvanishing frame \(s_v^k\) is
\[
 g_{m,v}=\prod_{i=1}^{n} w_i^{\langle m-kv,u_i\rangle},
 \qquad\langle m-kv,u_i\rangle\ge0
\]
by Theorem 21.9.5. Restricting to \(V(Q)\cap U_v\) annihilates this monomial if and only if one of the exponents with \(i\in I_{v,Q}\) is positive. All such exponents vanish if and only if \(m\) lies on every supporting facet containing \(Q\), equivalently \(m\in kQ\), since \(Q\) is the intersection of these facets (Proposition 21.9.1). Thus sections with \(m\notin kQ\) restrict to zero, while those with \(m\in kQ\) restrict to nonzero monomials on the dense orbit \(O_Q\). At \(v\) their exponents along its \(d\) free coordinates are distinct, so their restrictions are linearly independent. This proves the proposed kernel **provided there are no additional sections on \(V(Q)\)**.

To prove spanning (and hence surjectivity) without assuming that the homogeneous coordinate ring is generated in degree one, fix a vertex \(v_0\in Q\), and restrict any \(t\in H^0(V(Q),L^k|_{V(Q)})\) to the dense \(d\)-dimensional orbit. There the frame \(s_{v_0}^k\) writes \(t=f\,s_{v_0}^k\), with \(f\) holomorphic on \((\mathbb C^*)^d\). Lemma 21.9.4 (in the rank-\(d\) character lattice \(M_Q\)) gives a unique normally convergent Laurent expansion
\[
 f=\sum_{\lambda\in M_Q}c_\lambda\chi^\lambda .
\]
For every vertex \(v\in Q\), changing the frame to \(s_v^k\) sends the character term to
\(\chi^{\lambda+k(v_0-v)}\), whose exponents on the free chart coordinates are
\(\langle kv_0+\lambda-kv,u_j\rangle\), \(j\notin I_{v,Q}\). Since \(t\) extends holomorphically to the full coordinate space \(V(Q)\cap U_v\simeq\mathbb C^d\), Laurent uniqueness forces \(c_\lambda=0\) unless **all** these exponents are nonnegative at **every** vertex of \(Q\). They are precisely the tangent-cone inequalities of \(Q\) at its vertices. Their intersection is \(kQ\): every facet inequality of \(Q\) occurs among the tangent-cone inequalities at a vertex of that facet, and the reverse inclusion is immediate. Hence the only surviving exponents correspond to
\(m=kv_0+\lambda\in kQ\cap M\). The sum is finite and gives a linear combination of the restrictions of the global \(s_m\). This proves both surjectivity and (R). For a point face \(d=0\), the same argument has only one Laurent exponent; for \(Q=P\), it is exactly the original global character-basis argument.

### Face-volume growth and explicit independent small check

Use a lattice basis of \(M_Q\) to identify the affine span of \(Q\) with \(\mathbb R^d\) and \(Q-v_0\) with a full-dimensional integral polytope. Cubes of side \(1/k\) centered at \(k^{-1}M_Q\) give a Riemann-sum estimate: the symmetric difference between their union over \(Q\cap k^{-1}M_Q\) and \(Q\) lies in a fixed \(O(1/k)\)-neighborhood of the finitely many facets of \(\partial Q\), whose \(d\)-volume is \(O(1/k)\). Therefore the count equals \(k^d\operatorname{vol}_{M_Q}(Q)+O(k^{d-1})\). This argument uses no analytic volume comparison and proves (V).

For \(P=[0,2]\times[0,3]\), \(Q=\{0\}\times[0,3]\), direct enumerations of all integer pairs for \(k=0,1,2,3,4,5\) give
\[
\#(kP\cap\mathbb Z^2)=1,12,35,70,117,176,\qquad
\#(kQ\cap\mathbb Z^2)=1,4,7,10,13,16;
\]
the exact formulas are \((2k+1)(3k+1)\) and \(3k+1\). The face restriction kernel has dimension \(2k(3k+1)\). This bounded combinatorial enumeration was executed, **not** a repository test or formal verification.

## Disposition and coverage boundaries

- **No false theorem or newly established proof gap.** Theorem 21.9.5 already gives all character sections globally; (R) is a new exact orbit-closure restriction consequence. It illustrates a **genuine distinction**: surjectivity of the restriction \(H^0(X_P,L^k)\to H^0(V(Q),L^k|_{V(Q)})\) does **not** assert projective normality or surjectivity of \(\operatorname{Sym}^k H^0(X_P,L)\to H^0(X_P,L^k)\).
- **Proposed addition, not applied:** a Corollary after Theorem 21.9.5 spelling out the restriction exact sequence and the affine-face lattice normalization. Preserve the provenance and historical attribution of the existing results. The section-theoretic model can be referenced from the general divisor-restricted-volume discussion (§20.8), without treating the general analytic volume comparison as proved.
- **Dependencies:** the displayed toric atlas in §21.8.3, orbit/face correspondence §21.9.2, Laurent theorem §21.9.4 and global character basis §21.9.5 remain established *internal inputs*, not re-certified in their full proof chains. No Hironaka input needed. No regularization/approximation, Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas or positivity-loss work opened.
- **Actual coverage:** new exact finite-\(k\) restriction and rank arguments for **§§21.9.2–5** with §21.8.2/.3 coordinate crosscheck; these sections were previously partially inspected, so **zero first proof-level numbered-section visits and zero complete-section certifications**. The current ToC remains **25 chapters / 747 numbered sections**. No older findings are reclassified or repeated.
- **Repository scope:** audit Markdown only, on `review/mathematical-audit`. No production main, source/body, permanent tags, canonicalization, source repositories, CI, build, formalization or website publication.
