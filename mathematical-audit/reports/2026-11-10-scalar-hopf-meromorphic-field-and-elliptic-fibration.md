# Exact meromorphic field and sectionless elliptic fibration of a scalar Hopf surface — 2026-11-10

## Source pinning, scope and dependencies

- Production **main** at **`b6933b772f41b45918f7e25ed1afbbb1fd892272`**.
- Directly inspected integrated reading-edition file `docs/sections/contracting-hopf-quotients/index.html`, blob **`d09d9bac3785b78b557ff5178ad7a52b34b20dac`**; Theorem **23.3.3**, original source **`demailly-complex-geometry:371996B7`**, permanent tag **`D81E3145A1B4`**, physical lines **8–21** (statement), **24–50** (proof, particularly the quotient and \(\pi_1=\mathbb Z\) in 44–50). Section permanent tag `20E4E5F60131`.
- Precisely bounded internal input: `docs/sections/normal-spaces-and-tube-continuation--continuation-on-normal-complex-spaces/index.html`, blob **`fa09a923ef076a99d638d038020ddd3b884afaa7`**, Theorem **9.38.5**, source **`demailly-complex-geometry:7716022D`**, permanent tag **`F35BA7139EC4`**, physical lines **89–111**: meromorphic extension over normal codimension-two analytic subsets. Its displayed proof cites an internal Remmert–Stein theorem whose entire transitive proof is **not** independently certified in this increment. Only its **special case** \(X=\mathbb C^2,A=\{0\}\) is used here.
- The previous `POME-HOPF-CHAR-MEROMORPHIC-SECTIONS-001` established only the character **existence criterion** for nonzero meromorphic sections of a particular family of line bundles; the previous `POME-HOPF-HOLOMORPHIC-TENSORS-CHARACTER-001` concerns holomorphic covariant tensors. This report **does not recount** those results as new. It identifies the **entire invariant meromorphic function field** and a **sectionless principal elliptic fibration**.
- Entirely excluded: Demailly approximation/regularization and the dedicated Bergman, weighted \(L^2\), Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss proof-completion programme. Its earlier unresolved records stay **deferred-by-user**, neither resolved nor certified.

## Finding POME-HOPF-SCALAR-MEROMORPHIC-FIBRATION-001

**Severity:** low. **Status:** verified conditional deduction. **Printed Theorem 23.3.3 is correct in the checked scalar case.** The two results below extend its structural consequences; they neither repair an error nor certify all its general triangular/diagonal cases.

Let \(0<|q|<1\), put \(U=\mathbb C^2\setminus\{0\}\), and
\[
 X_q=U/\langle z\mapsto qz\rangle .
\]
The scalar specialization of Theorem 23.3.3 makes \(X_q\) a connected compact complex surface with \(\pi_1(X_q)=\mathbb Z\).

### 1. The whole meromorphic function field is rational in the direction

There is an **exact field equality**
\[
 \mathcal M(X_q)=\mathbb C(z_1/z_2).
\]
The right-hand side is interpreted as meromorphic functions on \(X_q\), not as global holomorphic functions. Every rational function of \(z_1/z_2\) is invariant under simultaneous scalar multiplication, so the inclusion from right to left is immediate.

Conversely let \(f\in\mathcal M(X_q)\) be nonzero and pull it back to the invariant meromorphic \(f\) on \(U\), satisfying \(f(qz)=f(z)\). The meromorphic codimension-two extension Theorem 9.38.5 gives a meromorphic germ at \(0\). Write it as \(P/Q\) for nonzero holomorphic germs \(P,Q\), and let \(P_p,Q_r\) be their first nonzero homogeneous Taylor terms, of degrees \(p,r\ge0\). For any fixed sufficiently small generic \(z\) with \(P_p(z)Q_r(z)\neq0\) and \(0<|f(z)|<\infty\), Taylor expansion along the contracted orbit yields
\[
 f(z)=f(q^kz)
 =q^{k(p-r)}
   \frac{P_p(z)+O_z(|q|^k)}
        {Q_r(z)+O_z(|q|^k)}\qquad(k\to\infty).
\]
Since \(0<|q|<1\), a fixed finite nonzero left side forces \(p=r\). Passing to the limit then yields \(f(z)=P_p(z)/Q_p(z)\). This equality holds on a nonempty open set (indeed on all sufficiently small generic points), so the meromorphic identity principle extends it to \(U\). The quotient of equal-degree homogeneous polynomials in two variables is rational in \(z_1/z_2\), as claimed. Constants and the zero function are included. Therefore the algebraic dimension of \(X_q\), defined by transcendence degree of its meromorphic function field over \(\mathbb C\), is exactly **one**.

This proof does **not** claim a classification of meromorphic sections of arbitrary line bundles or of all non-scalar Hopf surfaces. It uses meromorphic, not just holomorphic, Hartogs extension.

### 2. A canonical holomorphic elliptic fibration with no continuous section

The map
\[
 \pi:X_q\longrightarrow\mathbb P^1,\qquad[z_1,z_2]\longmapsto[z_1:z_2]
\]
is well-defined, surjective and holomorphic. On either standard affine chart of \(\mathbb P^1\), a nonzero point on the tautological line has a unique expression \(z=\lambda s(t)\), \(\lambda\in\mathbb C^*\), for a holomorphic nonvanishing local frame \(s(t)\) of \(\mathcal O_{\mathbb P^1}(-1)\). Quotienting the fiber coordinate by \(\lambda\sim q^k\lambda\) gives the same compact complex Lie group on every chart,
\[
 E_q=\mathbb C^*/q^\mathbb Z
 \simeq\mathbb C/(2\pi i\mathbb Z+(\log q)\mathbb Z).
\]
Because \(\Re\log q=\log|q|\ne0\), the indicated rank-two additive subgroup is a genuine lattice; \(E_q\) is an elliptic curve. Overlaps multiply the fiber coordinate by nonzero holomorphic functions, and multiplication commutes with \(q^\mathbb Z\); hence \(\pi\) is a **holomorphic principal \(E_q\)-bundle**.

There is **no continuous section**, and consequently no holomorphic section. Indeed, a section of a principal topological \(E_q\)-bundle would trivialize it by
\[
  (b,e)\longmapsto s(b)\cdot e.
\]
It would give \(X_q\simeq\mathbb P^1\times E_q\) as topological spaces and therefore \(\pi_1(X_q)\simeq\mathbb Z^2\), contradicting the verified scalar instance \(\pi_1(X_q)=\mathbb Z\) of Theorem 23.3.3. This step uses the **principal bundle** structure; a section of an arbitrary genus-one fibration need not provide the same trivialization.

Thus the meromorphic algebraic reduction is explicitly \(\pi\), with one-dimensional elliptic fibers and nontrivial bundle topology. In particular a compact complex surface can have algebraic dimension one and a holomorphic elliptic fibration despite being non-Kähler; the latter follows independently from Theorem 23.3.3.

## Adjudication, correction and propagation

**Theorem 23.3.3: no confirmed mathematical error.** Both deductions use the scalar diagonal specialization only; extending them to nonresonant diagonal or triangular contractions requires distinct arguments. Recommended **optional supplementary Corollary** after Theorem 23.3.3: for scalar contraction \(qI\), the meromorphic field is \(\mathbb C(z_1/z_2)\) and the direction map is a principal, sectionless elliptic bundle over \(\mathbb P^1\). No change to source theorem, provenance, or permanent tags is proposed.

**Affected dependent themes:** meromorphic algebraic reductions (§9, §23.3), divisor-to-Picard scope (§20.7), compact non-Kähler examples, and improper inferences that a holomorphic family of elliptic curves must have a section. This does **not** alter existing Hopf character-line-bundle findings.

**Unresolved/external input ledger:** the general proof chain of Theorem 9.38.5 (notably the cited Remmert–Stein extension) is an **internal dependency whose transitive verification remains open**, not a user-deferred Demailly task and not evidence of a false assertion. The topological fundamental-group computation in §23.3.3 is used as printed and directly inspected, not fully recertified across all upstream topology.

**Coverage:** Incremental direct scalar-case proof check of Theorem 23.3.3 plus precisely delimited meromorphic-extension input Theorem 9.38.5. Both numbered sections were previously selected for proof-level review: **zero first-visit sections, zero entire-section certifications**. Current table of contents: **25 chapters, 747 distinct numbered sections**. No project tests, build, CI, formalization, website publication, source-body or registry/canonicalization modifications were performed.
