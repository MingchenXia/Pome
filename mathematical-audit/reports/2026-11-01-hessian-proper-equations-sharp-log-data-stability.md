# Exact logarithmic-data stability for proper complex Hessian equations

**Audit date:** 2026-11-01.  
**Reviewed production `main`:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Finding:** **POME-HESS-PROPER-SHARP-LOG-DATA-001** — **low / verified conditional deduction** (the printed results were not falsified or repaired).  
**First newly selected proof-level section in this session:** **§8.7**, with supporting direct checks in §§8.6 and 14.11. No entire section or general upstream analytic result is certified.

## Exact integrated anchors, hypotheses and dependence

* Standing setting: `docs/sections/complex-hessian-equations/index.html`, blob `5331b937ccdaba51f1ec006d5e72dc84f7addfbf`, **line 7**, fixes connected compact complex $X$, smooth positive Hermitian $\omega$, and **$2\le m<n$**. The latter restriction is material: historical findings about unqualified $m=1$ algebraic lemmas must **not** be treated as new errors in the intermediate-Hessian PDE chain.
* Smooth existence/uniqueness: Lemma **8.6.1**, source `non-kahler-pluripotential-theory:91CAEA62`, permanent `8B310CC2C1A1`; `docs/sections/complex-hessian-equations--proper-equations-and-admissible-approximation/index.html`, blob `841dd207876499be9d83045facf862a323e60994`, **lines 10–42**. Its statement is $H_m(w)=e^{aw+H}\omega^n$, $a>0$, $H$ smooth real.
* Continuous mixed product and contact comparison: Proposition **8.7.1**, source `non-kahler-pluripotential-theory:81F79DFF`, permanent `D2A0F255F625`, **lines 10–41**; Lemma **8.7.2**, source `:5F73B4ED`, permanent `21F540C3F7D1`, **lines 43–61**.
* Nonvanishing and domination: Lemma **8.7.6**, source `:B21B6104`, permanent `E7EA08EFFDE7`, **lines 116–149**; Proposition **8.7.7**, source `:820C9E95`, permanent `7E8FF9A60609`, **lines 155–177**; Proposition **8.7.8**, source `:0EE901D4`, permanent `103D0E7E46B0`, **lines 179–201**; Lemma **8.7.9**, source `:F762B147`, permanent `F28CED8C4FAF`, **lines 204–223**. All are in `docs/sections/complex-hessian-equations--continuous-products-envelopes-and-domination/index.html`, blob **`045d10eb63453837e8675d22436afa9b9d6335ad`**.
* Linear Green input: equation **8.7.5**, source equation `non-kahler-pluripotential-theory:9A213454`, permanent `5451B220B0B1`, **lines 100–113** of that same file. Related existing internal proof template: §14.11.1 in `docs/sections/smooth-monge-ampere-equations--bounds-for-the-gauduchon-potential/index.html`, blob `f3e973821ba8b04a496e4f996917ff491e3956d1`, **lines 30–52**; positive adjoint measure in Theorem 11.4.2. The Green-kernel parametrix and uniform integral bounds remain an analytic input, not a newly certified internal theorem.

## New exact deduction (smooth and continuous versions)

Write $H_m(w)=(\omega+dd^c w)^m\wedge\omega^{n-m}$, with $X,\omega,m$ as above and $a>0$. Let $H,K\in C^\infty(X,\mathbb R)$, and let $u_H,u_K$ be the unique smooth strictly admissible solutions asserted by Lemma 8.6.1:
$$
H_m(u_H)=e^{a u_H+H}\omega^n,\qquad
H_m(u_K)=e^{a u_K+K}\omega^n.
$$
Then the sharp **pointwise, two-sided** estimate is
$$
\boxed{\quad
\frac{\inf_X(K-H)}{a}\le u_H-u_K
\le\frac{\sup_X(K-H)}{a}\quad\text{on }X.\quad}
$$
In particular,
$$
\|u_H-u_K\|_{L^\infty(X)}
\le a^{-1}\|H-K\|_{L^\infty(X)},
$$
and the solution map $H\mapsto u_H$ is **order-reversing**. No Kähler or $d\omega=0$ assumption is used.

**Direct smooth proof, independent of the nonlinear domination results.** Let $x_+$ be a global maximum of $u_H-u_K$. At $x_+$,
$dd^c u_H\le dd^c u_K$ in the Hermitian semidefinite order. Both associated forms lie in the admissible open $m$-cone. Gårding monotonicity under positive-semidefinite additions (recorded in §8.2) therefore yields
$$
e^{a u_H(x_+)+H(x_+)}
\le e^{a u_K(x_+)+K(x_+)},
\quad a\max_X(u_H-u_K)\le K(x_+)-H(x_+).
$$
At a global minimum $x_-$ the matrix order and resulting scalar inequality reverse, so $a\min_X(u_H-u_K)\ge K(x_-)-H(x_-)$. These give precisely the boxed bounds; no limiting operation occurs.

**Sharpness and normalization.** For any constant $c\in\mathbb R$,
$u_{H+c}=u_H-c/a$: adding the constant $-c/a$ does not change $H_m$ and exactly changes the exponential on the right. Therefore neither $1/a$ nor either endpoint of the boxed estimate can be improved uniformly. In particular, for constant $H=c$, $u_H=-c/a$ is an explicit solution on every Hermitian $X$, since $H_m(0)=\omega^n$.

**Continuous extension, conditional on printed domination.** If $H,K$ are continuous (indeed bounded Borel data suffice for the measure-order part) and continuous admissible $u_H,u_K$ satisfying the displayed equations in the sense of the printed continuous Hessian product are *given*, the same boxed bounds follow from Lemma 8.7.9. Set $d_+=\sup_X(K-H)/a$. Apply that lemma with its first variable $u_K+d_+$ and second $u_H$:
$$
 e^{-a u_H}H_m(u_H)=e^H\omega^n
 \ge e^{K-ad_+}\omega^n
 =e^{-a(u_K+d_+)}H_m(u_K+d_+).
$$
This gives $u_K+d_+\ge u_H$. Set $d_-=\inf_X(K-H)/a$, reverse the variables and use $e^{K-ad_-}\ge e^H$ to get $u_H\ge u_K+d_-$. **This is conditional on the pre-existing construction and domination theorem; it is not a new existence theorem for arbitrary Borel data.**

## Actual additional audit of §§8.6–8.7 (not new claims of full certification)

1. **Order and sign:** checked the exponential direction in 8.6.1 and 8.7.9; the order-reversing conclusion above follows consistently from both. At extrema the Hermitian form order gives exactly the needed sign. The $m=1$ printed algebra errors already in the ledger are **not** repeated as fresh findings; the PDE chapter explicitly fixes $2\le m<n$.
2. **Local-product input:** read 8.7.1 and 8.7.2. Their telescoping proof explicitly keeps $d\omega$ and $d^c\omega$ torsion terms and uses fewer than $m$ admissible factors after integration by parts; positivity/locality and contact inequality are therefore being *used as printed*, not silently replaced by closed Kähler form Stokes arguments.
3. **Positive-mass step:** checked 8.7.6's truncation $w=\max\{u,\min_X u+s\}$. On the open nonempty $U=\{u<\min_Xu+s\}$, $\sigma_w=\omega$, hence $\mu_0=\omega^n$. Its displayed absorption estimate, **if** the preceding absolute mixed-form bound and uniform torsion variation estimate hold, forces all $int_Umu_q=0$ for sufficiently small $s$, contradicting the positive volume of $U$. This verifies the final conditional deduction and its dependence, **not** all preliminary current estimates.
4. **Noncircular route:** the relevant explicit chain is 8.6.1 → 8.6.2/8.6.5 → 8.7.1/8.7.2/8.7.3 → 8.7.6 → 8.7.7 → 8.7.8 → 8.7.9. The $L^1$ Green estimate 8.7.5 is an additional linear-elliptic input to 8.7.7. The related Green argument in §14.11.1 provides an internal cross-reference candidate for the *same analytic mechanism*, but does **not** certify its local-parametrix assertion. The existing Green-input audit elsewhere remains unresolved.
5. **Proposed optional change:** add the sharp two-sided estimate as a corollary or short note after 8.7.9, with the direct maximum-principle proof for smooth solutions and the dominated-measure proof for continuous solutions. Add a precise cross-reference to the §14.11.1 Green-kernel argument near 8.7.5, without removing historical attribution, source labels, tags, or pretending the local Green parametrix is self-contained.

**Affected dependents:** smooth proper Hessian uniqueness/stability (§8.6.1), continuous proper Hessian comparisons and envelopes (§§8.7–8.8), and possible parameter continuity for smoothly varying log densities. This adds a sharp data-perturbation estimate; it **does not** repair or refute any printed theorem.

**Coverage status:** first substantive selected proof check in previously unreviewed **§8.7**; supporting reread of specific §§8.6.1/.2/.5, §8.2 cone order, and the Green paragraph in §14.11. The previously recorded $m=1$ issues, all other unresolved/deferred statuses, and the explicit user-deferred Demailly approximation/regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme remain untouched. Actual ToC still **25 chapters / 747 numbered sections / zero complete mathematical-section certifications**. No build, test suite, CI, formal verification, publication, source/body/registry/tag modification or alteration to production `main`.
