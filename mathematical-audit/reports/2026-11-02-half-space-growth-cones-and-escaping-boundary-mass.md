# Half-space Poisson representation: intrinsic vertical slope and sharp conical growth at infinity

- **Finding:** POME-HARM-HALFSPACE-CONE-GROWTH-SHARP-001
- **Date:** 2026-11-02
- **Severity / status:** low / **verified conditional deduction** (not an incorrect printed theorem, not an applied source repair).
- **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Integrated source file:** `docs/sections/kelvin-transforms-and-half-space-potentials/index.html`, blob `f2615a5393af724c3996978212162f94911ff9d9`.
- **Section:** §3.2, permanent section tag `9728BD930155`. Original source variant: `classical-potential-theory`.
- **Direct anchors:** Theorem 3.2.6, source Gerby tag `1C8A330A`, permanent tag `6BC86EEF03A9`, physical lines **65–75**, representation equation 3.2.7 original `C0A46F1A` / permanent `F3ED29BBAD39`, lines **66–68**, weighted hypothesis (3.2.8) original `358F89A3` / permanent `8F7C774A9D89`, lines **70–73**; constructive converse and its derivative domination, lines **111–131**. Crosscheck Theorem 3.2.12, original `BB6DAC3F`, permanent `9ADD2DF19642`, lines **141–145**, and the nonuniqueness caveat at line **185**.
- **Scope:** Only the exact representation and converse hypotheses were inspected, and the additional growth/measure calculations below were independently proved. This does **not** certify Theorem 3.2.6's ball boundary-measure existence proof (lines 80–123), all Kelvin-transform dependencies, the entire §3.2, or the whole project. No Demailly approximation, Bergman, weighted L², Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss programme was opened.

## Statement with the hypotheses actually used

Fix \(d\ge 2\), \(H=\mathbb R^{d-1}\times(0,\infty)\), \(\kappa_d=2/s_{d-1}\), and a **nonnegative harmonic** \(h\) on \(H\). Use exactly the printed representation in Theorem 3.2.6:
\[
h(x',t)=ct+\kappa_d t\int_{\mathbb R^{d-1}}
       (|x'-z|^2+t^2)^{-d/2}\,d\nu(z),\quad c\ge0,
\tag{1}
\]
where \(\nu\) is a positive Radon measure and
\[
\int_{\mathbb R^{d-1}}(1+|z|^2)^{-d/2}\,d\nu(z)<\infty.
\tag{2}
\]
In particular, the theorem **does not assume finite total mass** of \(\nu\).

**New conditional corollary.** Under (1)–(2):

1. For each fixed \(x'\), \(t\mapsto h(x',t)/t\) is nonincreasing, strictly decreasing if \(\nu\ne0\), and
\[
  c=\lim_{t\to\infty}\frac{h(x',t)}t
   =\inf_{t>0}\frac{h(x',t)}t.
\tag{3}
\]
Thus \(c\) is intrinsic to \(h\) and independent of the selected representation.

2. More strongly, for every **fixed** \(A<\infty\),
\[
 \boxed{\ \lim_{t\to\infty}\sup_{|x'|\le At}
   \left|\frac{h(x',t)}t-c\right|=0.\ }
\tag{4}
\]
No bound on \(\nu(\mathbb R^{d-1})\) is needed.

3. The cone restriction is **sharp for an assertion uniform over all allowable \(\nu\)**. For any curve \(x'=\gamma(t)\) satisfying \(\limsup_{t\to\infty}|\gamma(t)|/t=\infty\), there is a positive Radon measure satisfying (2) and an associated nonnegative harmonic \(h\) with \(c=0\) such that
\[
  \limsup_{t\to\infty}\frac{h(\gamma(t),t)}t\ge\kappa_d>0.
\tag{5}
\]
In particular, the unrestricted assertion \(h(x',t)/t\to c\) as \(t\to\infty\) **uniformly in every horizontal location \(x'\)** is false for the class (1)–(2). This is a counterexample **only to an unprinted strengthening**, not to Theorem 3.2.6 or 3.2.12.

## Detailed proof

### A. Vertical slope and strict monotonicity

Divide (1) by \(t>0\):
\[
 R(x',t):=\frac{h(x',t)}t-c
     =\kappa_d\int_{\mathbb R^{d-1}}
       (|x'-z|^2+t^2)^{-d/2}\,d\nu(z)\ge0.
\tag{6}
\]
For every \(z\) the integrand strictly decreases as \(t\) increases, and its integral is finite by (2). Hence \(R(x',t)\) is nonincreasing; it is strictly decreasing for a nonzero positive \(\nu\), because the difference of any two kernels is strictly positive at every \(z\). Its limit is zero by the cone estimate below (for a fixed \(x'\), take any \(A\ge |x'|\) and \(t\ge1\)). Equation (3) follows immediately. In particular, the coefficient of the linear harmonic summand cannot be changed without changing \(h\), regardless of whether uniqueness of the measure \(\nu\) is established separately.

### B. Uniform conical convergence by a common weighted majorant

Fix \(A\ge0\). For \(t\ge1\) and \(|x'|\le At\),
\[
 |z|^2\le2|z-x'|^2+2|x'|^2
        \le2|z-x'|^2+2A^2t^2,
\]
and therefore
\[
 1+|z|^2\le C_A(|z-x'|^2+t^2),
 \qquad C_A:=\max\{2,1+2A^2\}.
\]
Consequently
\[
 \sup_{|x'|\le At} (|x'-z|^2+t^2)^{-d/2}
 \le C_A^{d/2}(1+|z|^2)^{-d/2}.
\tag{7}
\]
The right-hand side is \(\nu\)-integrable **precisely under (2)**. For every fixed \(z\), the left-hand side of (7) is at most \(t^{-d}\to0\). Since the kernels are nonnegative,
\[
 0\le\sup_{|x'|\le At}R(x',t)
 \le\kappa_d\int\sup_{|x'|\le At}
       (|x'-z|^2+t^2)^{-d/2}\,d\nu(z)\to0
\]
by dominated convergence, proving (4). This argument passes the supremum **outside** the integral using positivity; it never interchanges unrelated limits or assumes that a bounded-mass exhaustion of \(\nu\) is uniform in \(x'\).

### C. A universal sharpness construction for every non-conical escape path

Suppose \(\limsup_{t\to\infty}|\gamma(t)|/t=\infty\). Choose strictly increasing \(t_j\to\infty\) with \(|\gamma(t_j)|/t_j\ge2^j\); put \(z_j=\gamma(t_j)\) and
\[
  \nu=\sum_{j=1}^{\infty}t_j^d\,\delta_{z_j}.
\tag{8}
\]
Since \(|z_j|\ge2^jt_j\to\infty\), the atoms escape every compact set and (8) is a Radon measure. Also
\[
 \int(1+|z|^2)^{-d/2}\,d\nu(z)
 =\sum_j\frac{t_j^d}{(1+|z_j|^2)^{d/2}}
 \le\sum_j2^{-jd}<\infty.
\tag{9}
\]
By the **converse** in the printed Theorem 3.2.6, (8) defines a smooth, finite, nonnegative harmonic function on \(H\) with \(c=0\). At \((z_j,t_j)\), retain only the \(j\)-th nonnegative term:
\[
 \frac{h(z_j,t_j)}{t_j}
 \ge\kappa_d\,\frac{t_j^d}
                     {(0+t_j^2)^{d/2}}
 =\kappa_d.
\tag{10}
\]
Thus (5) follows. A concrete fixed family is
\[
 t_j=2^j,\qquad z_j=(2^{2j},0,\ldots,0),\qquad
 \nu=\sum_j2^{jd}\delta_{z_j}.
\]
The weighted total mass is summable as in (9), but \(\nu\) has infinite ordinary total mass. Along the vertical line \(x'=0\), (3) gives \(h(0,t)/t\to0\); along the escaping points (10) it does not. No boundary regularity or boundedness was assumed in Theorem 3.2.6.

### D. Contrasts with stronger hypotheses and the printed bounded-data theorem

If additionally \(\nu(\mathbb R^{d-1})<\infty\), equation (6) directly yields the genuinely global horizontal estimate
\[
 0\le\sup_{x'\in\mathbb R^{d-1}}R(x',t)
 \le\kappa_d\,\nu(\mathbb R^{d-1})\,t^{-d}.
\]
Likewise Theorem 3.2.12 assumes *bounded Lebesgue boundary data* \(f\), rather than arbitrary weighted Radon boundary measure; its normalization gives \(|u(x',t)/t-c|\le\|f\|_\infty/t\) uniformly in \(x'\). The atomic construction above **does not satisfy** either stronger condition. Thus the two printed theorems are compatible and correct on the portions checked.

## Audit disposition and dependents

- **Status:** verified conditional deduction, **not** a confirmed error, proof gap, genuine duplication or certification of the upstream boundary representation. The calculation independently verifies the use of positivity and the weighted integrability normalization in equations 3.2.7–8.
- **Suggested nonintrusive change:** a **proposed** corollary immediately after Theorem 3.2.6 identifying \(c\) by (3), proving (4), and warning against dropping the conical restriction for infinite weighted boundary mass; retain the source attribution and original tags. No published/source/registry edit is authorized here.
- **Affected uses:** any later argument identifying the linear Martin/Poisson-at-infinity coefficient, passing to large-height limits, or replacing a weighted boundary measure by bounded boundary data. No specific downstream source assertion was shown false, and no reader-level canonicalization or proof replacement is applied.
- **Coverage:** a new proof-level increment in the **previously partly audited** §3.2 only, on lines 65–75, 111–131 and 141–145; not a newly first-audited section, not a whole-section theorem certificate, and not an inference of full project coverage.
- **Project state:** actual ToC at reviewed main: **25 chapters / 747 numbered sections / zero completely certified mathematical sections**. All earlier confirmed errors, proof gaps, duplicates, genuine external inputs and deferred-by-user entries retain their classifications. No CI, tests, build, formal verification, automatic publication, or production-main change was performed in this audit.
