# Mathematical audit: finite non-Archimedean joins and torsion oscillation in semipositive section growth

**Date:** 2026-10-25 (Asia/Shanghai).  
**Pinned main commit:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Scope:** selected integrated proofs in §§22.1 and 17.15, and an independent sharpness test of §19.10. No Demailly approximation, Bergman/L2, Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss proof programme was examined. No whole section or dependent theorem chain is certified.

## POME-NA-FINITE-JOIN-ORDER-001 — low / verified conditional deduction

**Claim checked:** The finite-maximum clause of the comparison-of-operations statement, Theorem 22.1.112, has an internal order-theoretic proof, conditional on the already printed comparison bijection (Theorem 22.1.111) and the BJ maximum-closure input (Proposition 22.1.73). There is no assertion that Theorem 22.1.112 is false.

**Pinned integrated locations.**
- docs/sections/non-archimedean-pluripotential-theory/index.html, blob 8448d710690ebe1cc28040f9611d05c9d008a961: Definition 22.1.31, permanent tag B819F1A85E09, lines 504–508; Proposition 22.1.73, tag 8E1FC46DBC87, lines 1199–1200; order-reflection Lemma 22.1.105, tag CB69CB164255, lines 1544–1579; comparison Theorem 22.1.111, tag 9B811DBD89E3, lines 1679–1722; operations Theorem 22.1.112, tag CB40FF867A00 (source sgpt-851EABB9), lines 1727–1728.
- docs/sections/test-curves--operations-on-test-curves/index.html, blob 3da617be8f58713f764d49ba22f49b803149a5e8: Definition 17.15.12, tag D347D46F3537, lines 289–305, and Corollary 17.15.17, tag C8D1BA787705, lines 389–455 (existence and least-upper-bound property for the concave-envelope join).
- Same §22.1 file: constant translation Definition 22.1.27, tag D1E32864F8F0, lines 439–443; analytification formula (22.1.83), tag 45957E422015, lines 1243–1257. The earlier audit ID POME-NA-OPS-001 already established translation/scaling compatibility and is **not** being registered anew.

**Hypotheses:** Let $X$ be connected projective, $L$ a pseudo-effective rational line bundle, $\theta=c_1(L,h)$, and $\Gamma_1,\ldots,\Gamma_N\in\mathrm{PSH}^{\mathrm{NA}}(X,\theta)$, $1\le N<\infty$. The theorem is in the exact category covered by the comparison Theorem 22.1.111.

**Precise conclusion.** For all points of the Berkovich analytification, not just divisorial points,
\[
\left(\bigvee_{j=1}^{N}\Gamma_j\right)^{\mathrm{An}}
=\max_{1\le j\le N}\Gamma_j^{\mathrm{An}}.
\tag{1}
\]
Define an *extended* order distance on potentials by
\[
d_{\mathrm{ord}}(A,B)
=\inf\{c\ge0:A\le B+c,\ B\le A+c\}\in[0,+\infty],
\tag{2}
\]
where the infimum of the empty set is $+\infty$. This definition is valid for simultaneous $-\infty$ poles, whereas $|A-B|$ is not. The analytification is an isometry for (2), and finite joins satisfy the sharp estimate
\[
d_{\mathrm{ord}}\left(\bigvee_j\Gamma_j,\bigvee_j\Delta_j\right)
\le\max_jd_{\mathrm{ord}}(\Gamma_j,\Delta_j)
\tag{3}
\]
for any two finite families in the same class.

**Complete deduction.** First, for any pair $\Gamma,\Delta$, Definition 22.1.31 defines the join in every Kähler-perturbed component. Corollary 17.15.17 says that this is an upper bound of both components and is dominated by every other common upper bound. Hence $\Gamma\lor\Delta$ is the *least upper bound* in the inverse-limit order: apply the cited componentwise statement to every positive perturbation, using the definition of the order in §22.1.21. Induction gives the same property for any finite nonempty family.

Second, Theorem 22.1.111 makes analytification an order-preserving **and order-reflecting bijection**. Every order isomorphism sends an existing least upper bound to the least upper bound of the images. On the Boucksom–Jonsson side, Proposition 22.1.73 ensures that the pointwise maximum of two psh metrics is again a psh metric. Being pointwise the smallest common upper bound, it is the least upper bound in the pointwise order. Consequently the two least upper bounds coincide. This proves (1) by induction on $N$. Equality first follows in the ordered psh-metric category and therefore holds at all analytic points; there is no illicit extension from an arbitrary dense set.

Third, translation compatibility of analytification was separately proved under the existing ID POME-NA-OPS-001 from the Legendre variable change in (22.1.83). Thus the defining two inequalities in (2) are equivalent before and after analytification by the order isomorphism; this proves the isometry statement, including infinite distances. For any real $c$ strictly greater than the right side of (3), each $\Gamma_j\le\Delta_j+c$ and $\Delta_j\le\Gamma_j+c$. Monotonicity of finite joins and their commutation with common translation give the two inequalities for the joins. Let $c$ decrease to the right-hand side (no countability or limit of potentials is used). When the right-hand side is infinite, the estimate is automatic. The constant 1 is sharp: choose all $\Gamma_j=G$ and all $\Delta_j=G+c$, $c>0$. Then the joins differ by $c$; $d_{\mathrm{ord}}(G,G+c)=c$ because their values at the trivial valuation differ by $c$ and are finite (22.1.104).

**Boundary / disposition:** This internally replaces only the **finite maximum** compatibility sentence otherwise referred to [Xia23Operations] after Theorem 22.1.112. It does not claim an internal proof of every addition, trace, arbitrary supremum, or external BJ approximation theorem. The existence and order-isomorphism inputs retain their previously logged dependencies. No source edit is made. Suggested optional insertion: after Theorem 22.1.112, record (1) and the order-theoretic proof; (2)–(3) are a useful corollary for perturbation estimates.

## POME-SEMIPOS-TORSION-OSCILLATION-001 — low / verified conditional deduction

**Claim checked:** Corollary 19.10.1's leading $k^n$ growth formula is correct as used, but semipositivity and vanishing top curvature mass do **not** imply a second asymptotic coefficient of order $k^{n-1}$, or even an $o(k^{n-1})$ remainder.

**Pinned integrated location:** docs/sections/section-growth-of-semipositive-line-bundles/index.html, blob 41526a319c45c861a8303776f155096d1f36614a, source demailly-complex-geometry, Corollary 19.10.1, tag F31884F26A29 (source environment identifier 4B096A2D), lines 8–19; Equation 19.10.2, tag 2B3916324C79 (source equation identifier 15584614), lines 9–11. The cited weak/strong holomorphic Morse inequalities in the original proof were **not** independently audited in this run; no L2 or regularization proof was opened.

**Explicit construction and complete proof.** Fix integers $n\ge1$ and $q\ge2$. Let
\[
E=\mathbb C/(\mathbb Z+\tau\mathbb Z),\quad \operatorname{Im}\tau>0,
\quad \chi(1)=e^{2\pi i/q},\quad \chi(\tau)=1.
\]
The unitary character $\chi:\mathbb Z+\tau\mathbb Z\to\mu_q$ defines a flat holomorphic line bundle $T$ on $E$, obtained by quotienting the trivial bundle on $\mathbb C$ with deck factors $\chi$. The constant Hermitian norm descends to a flat metric, so $i\Theta_T=0$, and $T^q$ is holomorphically trivial.

For every $k\ge1$, holomorphic sections of $T^k$ are entire functions $f$ with
\[
f(z+\lambda)=\chi(\lambda)^k f(z).
\]
Their absolute values are lattice-periodic and hence bounded. Liouville's theorem makes $f$ constant; a nonzero constant exists exactly when $\chi^k$ is trivial. Therefore
\[
h^0(E,T^k)=\begin{cases}1,&q\mid k,\\0,&q\nmid k.\end{cases}
\tag{4}
\]

Take $X=E\times\mathbb P^{n-1}$ (with $\mathbb P^0$ a point when $n=1$), and
\[
L=p_E^*T\otimes p_{\mathbb P}^*\mathcal O_{\mathbb P^{n-1}}(1)
\]
with the product of the flat and Fubini–Study metrics. Then $X$ is smooth compact Kähler and $i\Theta_L\ge0$. Its curvature form is pulled back from a space of dimension $n-1$, so
\[
\int_X\Omega_L^n=0.
\tag{5}
\]
If $q\nmid k$, every section of $L^k$ restricts on each $E$-fiber to a section of $T^k$, and therefore vanishes identically. If $q\mid k$, then $T^k$ is trivial, and compactness of $E$ implies that sections of $p_{\mathbb P}^*\mathcal O(k)$ are exactly pullbacks of sections on $\mathbb P^{n-1}$. Counting homogeneous monomials gives the **exact** formula
\[
h^0(X,L^k)=
\begin{cases}
\binom{k+n-1}{n-1},&q\mid k,\\
0,&q\nmid k .
\end{cases}
\tag{6}
\]
Consequently,
\[
\liminf_{k\to\infty}\frac{h^0(X,L^k)}{k^{n-1}}=0,
\qquad
\limsup_{k\to\infty}\frac{h^0(X,L^k)}{k^{n-1}}=\frac1{(n-1)!}.
\tag{7}
\]
For $n=1$ this simply means an oscillating sequence of zeros and ones. Equations (5)–(7) are compatible with (19.10.2), since $h^0(X,L^k)=O(k^{n-1})=o(k^n)$. They exclude a general next-order asymptotic coefficient and show the top-volume-zero remainder need not be $o(k^{n-1})$. No external analytic result is needed for the example.

**Boundary / disposition:** The printed Corollary 19.10.1 is not a false theorem; the example concerns a stronger, *unprinted* possible inference. Suggested optional remark after (19.10.2): torsion flat factors create periodic order-$k^{n-1}$ oscillation even for smooth semipositive curvature on a projective manifold. An improvement requires extra hypotheses about twists or passage to specified arithmetic subsequences. This does not repair the original weak/strong Morse proof or certify its external premises.

## Coverage and dependency ledger checkpoint

- **Actual newly examined proof steps:** §22.1.31 (finite join definition), §22.1.73 (maximum closure as a cited premise), §22.1.105 (order reflection), §22.1.111 (the comparison isomorphism as a premise), §22.1.112 (operations claim and its actual external-reference boundary), and §17.15.12–17 (least-upper-bound argument). §19.10.1–2 were re-read and independently stress-tested with the exact flat-torsion family. §22.1.113–116 were inspected only for scope and not certified.
- **Earlier findings retained, not claimed anew:** POME-NA-OPS-001 (translation and scaling); POME-NA-CONCAVE-TAIL-001 (a separate confirmed concave-envelope construction defect); POME-NA-MINIMAX-001 and POME-NA-TRIV-001 (earlier comparison proof qualifications). The current two stable IDs were checked for nonduplication against the historical ledger.
- **Still unverified here:** the full Boucksom–Jonsson projective psh-metric existence/approximation theorem, other compatibility operations cited to [Xia23Operations], all source Morse inequalities, global dependencies of the projective comparison theorem and the rest of both sections.
- **Deferred by user, not resolved/certified:** the entire dedicated Demailly approximation/regularization and Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme. Neither of the present findings relies on opening that programme.
- **Operations actually performed:** source reads and written mathematical deductions only; no build, CI, formalization, publication or source/registry/tag/main modification. Coverage-matrix rows are selective passage records, never whole-section certification.
