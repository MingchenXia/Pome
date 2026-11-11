# Coprime plane branches: exact normalization conductor, gap symmetry, and Jacobian colength

- **Finding ID:** POME-NORM-COPRIME-PQ-SEMIGROUP-CONDUCTOR-001.
- **Date:** 2026-11-12.
- **Severity / classification:** low / **verified conditional deduction**, an explicit model computation, **not a false printed theorem or a repair of a proof gap**.
- **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
- **Integrated reading edition:** docs/sections/complex-spaces-and-modifications--reduced-spaces-and-normalization/index.html, blob 06439f43d1ce8e83d2529682c9a630bffa3d9c22.
- **Exact anchors:** Proposition 9.4.3, source foundations-of-pluripotential-theory:AC231B8D, permanent 36422A732754, physical lines 52–79 (finite conductor, weakly holomorphic integral closure); Theorem 9.4.6, source foundations-of-pluripotential-theory:7042BB57, permanent 12A47DB401E2, lines 142–159 (finite normalization and branch fibers); Example 9.4.10, source foundations-of-pluripotential-theory:680F3928, permanent 60A14C7A1845, lines 197–199 (the (2,3) cusp). These anchors identify the integrated statements, not source-era numbering.

## Claim and hypotheses

Fix coprime integers \(3\le p<q\). Consider the reduced plane-curve germ at the origin
\[
 C_{p,q}=\{(z,w)\in(\mathbb C^2,0):w^p=z^q\},
 \qquad \nu(t)=(t^p,t^q).
\]
Put \(A=\mathcal O_{C_{p,q},0}\), \(B=\mathbb C\{t\}\), \(S=\langle p,q\rangle=\{ap+bq:a,b\in\mathbb Z_{\ge0}\}\), and \(c=(p-1)(q-1)\). Then:

1. \(C_{p,q}\) is irreducible and has one normalization branch. The normalization ring is \(B\), and the map \(\nu\) is finite, bimeromorphic and one-to-one, with a single point over the origin. The projection \((z,w)\mapsto z\) has generic degree \(p\), with a cyclic \(p\)-sheeted monodromy around the origin, despite this one-point normalization fiber.
2. Precisely
   \[
   A=\mathbb C\{t^p,t^q\}
    =\bigoplus_{j=0}^{p-1}t^{qj}\mathbb C\{t^p\}.
   \]
   A convergent series \(g(t)=\sum_{k\ge0}a_kt^k\) is holomorphic on the original curve exactly when \(a_k=0\) for every \(k\notin S\); every \(g\in B\) is weakly holomorphic on the curve.
3. For \(F=pq-p-q=c-1\), the exponent gaps are symmetric:
   \[
   \forall\,0\le k\le F,\qquad
       \mathbf 1_S(k)+\mathbf 1_S(F-k)=1.
   \]
   In particular \(F\notin S\) but every integer \(k\ge c\) is in \(S\). The normalization defect is
   \[
   \delta(C_{p,q})=\dim_{\mathbb C}(B/A)
     =\#(\mathbb Z_{\ge0}\setminus S)
     =\frac{(p-1)(q-1)}2.
   \]
4. The **optimal** conductor in the normalization ring, including all its higher-order coefficients, is
   \[
   \mathfrak c=\{b\in B:bB\subset A\}=t^cB
      =(t^c,t^{c+1},\ldots,t^{c+p-1})A.
   \]
   The displayed \(p\) generators are minimal as an \(A\)-module. Furthermore
   \(\dim_{\mathbb C}(A/\mathfrak c)=\delta\) and
   \(\dim_{\mathbb C}(B/\mathfrak c)=c=2\delta\).
5. The isolated plane singularity has Jacobian-algebra length
   \[
   \dim_{\mathbb C}\frac{\mathbb C\{z,w\}}{
      (w^p-z^q,\partial_z(w^p-z^q),\partial_w(w^p-z^q))}
   =(p-1)(q-1)=2\delta.
   \]
   This last equality is an elementary monomial quotient computation; no general singularity-classification theorem is invoked.

The additional point beyond the existing double-cover family is the entire **\(p\ge3\) residue-class decomposition**, all gaps and their symmetry, the optimal conductor with **minimal \(p\) generators**, and the Jacobian colength identity. The old \(p=2,q=2m+1\) conductor and monodromy remain attributed to POME-CURVE-DOUBLE-COVER-MONODROMY-CONDUCTOR-001 (2026-11-06), not re-registered as a new discovery.

## Proof

**(1) Equation and one-branch normalization.** The polynomial \(w^p-z^q\) is monic of degree \(p\) in \(w\). Weierstrass division represents any class in \(\mathbb C\{z,w\}/(w^p-z^q)\) uniquely as
\(\sum_{j=0}^{p-1}a_j(z)w^j\).
Under \(z=t^p,w=t^q\), these terms become
\(\sum_{j=0}^{p-1}t^{qj}a_j(t^p)\).
Their exponent classes \(qj\bmod p\) are pairwise distinct by \(\gcd(p,q)=1\), so their sum can vanish only if each \(a_j=0\). Thus the map into \(B\) is injective, the defining equation is reduced and irreducible, and the image is exactly the direct sum in the claim. In particular, the curve has one irreducible branch.

Every \(g(t)\in B\) can be decomposed uniquely as \(\sum_{j=0}^{p-1}t^jb_j(t^p)\), and the ring \(B\) is thus a finite \(A\)-module. The parameter \(t\) is integral over \(A\) via \(T^p-z=0\), while \(B\) is the integrally closed smooth one-variable ring. On the punctured curve both \(z\) and \(w\) are nonzero. Bézout integers \(\alpha,\beta\) with \(p\alpha+q\beta=1\) give the holomorphic inverse \(t=z^\alpha w^\beta\) there; negative exponents are allowed on this punctured locus. Hence \(\nu\) is an isomorphism away from the origin, finite, and the desired normalization. The normalized fiber is \(\{0\}\). By contrast, for fixed \(z\neq0\), the equation \(t^p=z\) has \(p\) solutions, permuted cyclically by a circuit around \(z=0\); each yields a different \(w=t^q\) because \(q\) is prime to \(p\). This proves the generic-degree/branch distinction.

**(2) Exact semigroup support including convergence.** Every exponent of \(t^{qj}a_j(t^p)\) has the form \(qj+pa\) with \(a\ge0\), hence is in \(S\). Conversely, any \(ap+bq\in S\) can be rewritten \(qj+p(a+\ell q)\) with \(0\le j<p\) by writing \(b=j+\ell p\). A series with coefficients only at exponents in \(S\) decomposes by these finitely many residue classes into convergent series \(t^{qj}a_j(t^p)\): convergence follows from the Cauchy bounds on the original convergent power series after passing to a smaller disc. Thus the characterization applies to actual analytic germs, not merely formal semigroup rings. Every \(g\in B\) descends to a bounded holomorphic function on the punctured smooth curve via the inverse above, and is therefore weakly holomorphic. A gap monomial \(t^k\), such as \(t\), is weakly holomorphic but cannot belong to \(A\).

**(3) Exact gap symmetry and conductor threshold.** Given any integer \(k\), there is a unique residue representative \(j\in\{0,\ldots,p-1\}\) and an integer \(a\) such that
\(k=qj+pa\). The semigroup criterion just established gives
\(k\in S\iff a\ge0\). For \(F=q(p-1)-p\),
\[
 F-k=q(p-1-j)+p(-a-1).
\]
The second residue representative lies again between \(0\) and \(p-1\), so
\(F-k\in S\iff -a-1\ge0\), the exact logical complement of \(a\ge0\).
For \(0\le k\le F\), this proves the asserted symmetry. For \(k=F\), the unique representation is \(j=p-1,a=-1\), so \(F\notin S\). If \(k>F\) and \(k\notin S\), symmetry would force \(F-k\in S\), impossible because \(F-k<0\). Hence every \(k\ge F+1=c\) lies in \(S\) and the threshold is optimal.

Since \(c=(p-1)(q-1)\) is even, \(F=c-1\) is odd. The involution \(k\leftrightarrow F-k\) pairs the \(c\) nonnegative integers below \(c\) without fixed points; exactly one in every pair is a gap. Therefore there are exactly \(c/2\) gaps. By the direct-sum expansion and the analytic convergence argument, the corresponding gap monomials give a genuine vector-space basis of \(B/A\), proving its precise finite length \(\delta=c/2\).

**(4) Exact conductor and minimal generators.** Because all powers \(t^k\) for \(k\ge c\) belong to \(A\), the entire ideal \(t^cB\) lies in \(A\) (including convergent sums). It is visibly stable under multiplication by \(B\), hence lies in \(\mathfrak c\). Conversely, take a nonzero \(b\in B\) of order \(r<c\) and leading coefficient \(b_rt^r\). Multiplication by \(t^{F-r}\in B\), valid since \(r\le F\), produces a germ of order \(F\notin S\), which cannot lie in \(A\). Thus \(b\notin\mathfrak c\), establishing \(\mathfrak c=t^cB\) and its optimality even against possible cancellation in nonmonomial elements.

Every exponent \(m\ge c\) has the unique form \(c+j+pk\) with \(0\le j<p\) and \(k\ge0\); since \(z=t^p\in A\), the claimed \(p\) generators generate the conductor as an \(A\)-ideal. They are minimal: the maximal ideal of \(A\) is \(\mathfrak m_A=(t^p,t^q)A\), and because \(q>p\),
\(\mathfrak m_A\mathfrak c=t^{c+p}B\).
Thus \(\dim_{\mathbb C}(\mathfrak c/\mathfrak m_A\mathfrak c)=p\), with representatives \(t^c,\ldots,t^{c+p-1}\), and the standard generator-counting argument modulo the maximal ideal forces at least \(p\) generators. Finally, \(B/t^cB\) has basis \(1,t,\ldots,t^{c-1}\), while \(A/t^cB\) has one basis monomial for each non-gap exponent below \(c\), hence dimension \(c-\delta=\delta\).

**(5) Exact Jacobian colength.** For \(f=w^p-z^q\), the partial derivatives are \(\partial_z f=-qz^{q-1}\), \(\partial_w f=pw^{p-1}\). Modulo these two derivatives the original equation \(f\) already vanishes, since \(p,q\ge2\). The quotient is therefore \(\mathbb C\{z,w\}/(z^{q-1},w^{p-1})\), with basis \(z^aw^b\) for \(0\le a<q-1\), \(0\le b<p-1\); its dimension is \((p-1)(q-1)=2\delta\).

**Numerical anchor (outside the previously treated double cover).** For \(p=3,q=5\), \(S=\langle3,5\rangle\) has gaps exactly \(\{1,2,4,7\}\), \(\delta=4\), \(c=8\), and \(\mathfrak c=(t^8,t^9,t^{10})A\); the projection to the \(z\)-axis has a three-cycle of generic sheets, but only one normalization point over the cusp. A finite integer enumeration checked the gaps, the involution and the threshold also for \((p,q)=(4,7),(5,6),(3,7),(2,9)\); this is a reproducible arithmetic sanity check, **not** a formal certification of the analytic theorem.

## Audit interpretation, dependencies and affected statements

- **Not a confirmed error:** the printed Proposition 9.4.3, Theorem 9.4.6 and Example 9.4.10 predict the correct finite normalization, integral closure and branch behavior in this family. There is no source-body or canonicalization patch to apply.
- **Verified conditional deduction:** all novel semigroup, conductor, Jacobian and monodromy calculations are proved within this explicit analytic model. We used the elementary monic Weierstrass division theorem and analytic one-variable power-series calculus; the general existence/uniqueness proof of Theorem 9.4.6 and all its upstream finiteness/coherence prerequisites are **not** thereby certified.
- **Downstream interpretative constraint:** §§9.5, 9.9, 20.5 and other finite-normalization / divisorial restriction arguments must distinguish (i) the generic degree \(p\) of a coordinate projection, (ii) a single normalization branch, (iii) the normalization defect \(\delta\), and (iv) its **optimal conductor exponent \(c\)**. None is interchangeable. The exact p-generator result warns against extrapolating the two-generator conductor presentation in a quadratic cusp to all plane branches.
- **Prior-report de-duplication:** POME-CURVE-DOUBLE-COVER-MONODROMY-CONDUCTOR-001 already computed the quadratic family \(w^2=z^{2m+1}\), the two-branch comparison, its conductor and monodromy on 2026-11-06. Only the new arbitrary-coprime \(p\ge3\) residue-class/gap-symmetry/conductor-minimal-generator and Jacobian results are newly registered here. Earlier normalization countability defects remain unresolved and are not modified.
- **No excluded programme:** No Demailly approximation, regularization, dedicated Bergman/L²/OT/multiscale/positivity-loss proof step was read or used. Existing excluded notes remain **deferred-by-user**, neither resolved nor certified.
- **Exact coverage:** a fresh selected theorem-level crosscheck of Proposition 9.4.3, Theorem 9.4.6 and Example 9.4.10 at the original physical anchors; no first-time numbered section visit (the §9.4 row already had proof-level review), and **zero complete-section mathematical certifications**. The main table of contents has 25 chapters and 747 numbered sections; no global transitive verification is claimed.
- **Execution boundary:** This audit does not run a project build, tests, formal verification, GitHub Actions CI or website publication. Only additive review-branch audit Markdown is proposed.
