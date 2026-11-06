# 2026-11-07 — Full radial Fourier signature of the Hopf raw-action Hessian

**Finding ID:** POME-PERRON-HOPF-FOURIER-SIGNATURE-001  
**Classification:** low / **verified conditional deduction** (additional spectral calculation, **not** a counterexample to the printed theorem).  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.  
**Review scope:** selected subsection 17.16.23–25 and equations 17.16.24, 17.16.26; geometric normalization crosscheck in 23.1.32. No complete section is certified.

## Precise source and reading-edition anchors

- Integrated reading edition: `docs/sections/perron-interpolation-and-the-geodesic-equation/index.html`, blob `dc8dc381257360c94fe1c792499bb1ddf1bf5997`; physical lines **447–497**, and numerical consistency context **502–521**.
- Subsection 17.16.23: source `non-kahler-pluripotential-theory:0A857E1B`, permanent tag `124D4C83F5E6`, physical line 447.
- Radial action equation 17.16.24: source `non-kahler-pluripotential-theory:E8F59B3B`, permanent `905CCA72845B`, lines 452–459.
- Theorem 17.16.25: source `non-kahler-pluripotential-theory:A1289B04`, permanent `944944D6FF68`, lines 466–497.
- Hessian equation 17.16.26: source `non-kahler-pluripotential-theory:5B7EC348`, permanent `F20F3B72C244`, lines 475–494.
- Geometric input: `docs/sections/unbounded-mass-on-hopf-manifolds/index.html`, blob `f53618e8d808de21687ff9166971cb9302ea8cfb`, subsection 23.1.32 at physical lines **560–577** (Hopf quotient, fiber period, mass normalization). This context was inspected, not fully proved.
- The base CAT(0) completion Theorem 17.16.19 and the unqualified global Perron assertions are **not used** in the spectral calculation, and are **not certified** here.

## Statement of the newly verified computation

Fix \(n\ge3\), \(d=n-1\), and \(c\in\mathbb R\setminus\{0\}\). On the Hopf example of subsection 23.1.32, let \(r=\log|z|^2\in\mathbb R/2\mathbb Z\), and consider smooth real perturbations
\[
u_\epsilon(t,r)=ct+\epsilon w(t,r),\quad
w(0,r)=w(1,r)=0,\quad w(t,r+2)=w(t,r).
\]
For each fixed smooth \(w\), \(\omega+\mathrm{dd}^{\mathrm c}u_\epsilon>0\) for all sufficiently small \(|\epsilon|\), because its two spatial coefficients
\(1+\epsilon w_r\) and \(1+\epsilon w_{rr}\) stay positive.

The raw-action Hessian at \(ct\), evaluated on \(w\), is
\[
Q_c[w]=\left.\frac{\mathrm d^2}{\mathrm d\epsilon^2}
                 \mathscr S(ct+\epsilon w)\right|_{\epsilon=0}
=2n\int_0^1\left\langle
 (w_t+dcw_r)^2-\lambda c^2w_r^2
\right\rangle\mathrm dt,\qquad
\lambda=\frac{d(d+1)}2.
\tag{A}
\]
Set \(s=r-dct\), \(W(t,s)=w(t,s+dct)\). Then \(W\) is 2-periodic in \(s\), vanishes at both temporal endpoints, and (A) is exactly
\[
Q_c[w]=2n\int_0^1\left\langle W_t^2-\lambda c^2W_s^2\right\rangle\mathrm dt.
\tag{B}
\]
For a finite Fourier expansion
\[
W(t,s)=a_0(t)+\sum_{k\ge1}
\bigl(a_k(t)\cos(\pi ks)+b_k(t)\sin(\pi ks)\bigr)
\]
with every coefficient vanishing at \(t=0,1\), orthogonality yields the **complete mode-by-mode quadratic-form identity**
\[
\boxed{
Q_c[w]=2n\!\int_0^1 |a_0'|^2\mathrm dt
+n\sum_{k\ge1}\int_0^1
\left(|a_k'|^2+|b_k'|^2
-\lambda c^2\pi^2 k^2(|a_k|^2+|b_k|^2)\right)\mathrm dt .
}
\tag{C}
\]
The formula extends to the natural \(H^1_0([0,1]\times(\mathbb R/2\mathbb Z))\) form domain by density; it does **not** imply compact resolvent for the resulting hyperbolic operator.

In particular, the two real modes
\[
w_{\ell,k}^{\cos}(t,r)=\sin(\ell\pi t)
            \cos\bigl(\pi k(r-dct)\bigr),\qquad
w_{\ell,k}^{\sin}(t,r)=\sin(\ell\pi t)
            \sin\bigl(\pi k(r-dct)\bigr)
\]
for integers \(\ell,k\ge1\) each satisfy
\[
\boxed{Q_c[w_{\ell,k}^{\cos}]
       =Q_c[w_{\ell,k}^{\sin}]
       =\frac{n\pi^2}{2}\left(\ell^2-\lambda c^2k^2\right).}
\tag{D}
\]
The spatially constant mode \(\sin(\ell\pi t)\) instead has \(Q_c=n\pi^2\ell^2>0\). Relative to the \(L^2\)-inner product \(\int_0^1\langle WW'\rangle\,\mathrm dt\), the nonzero-spatial-frequency modes have eigenvalues
\(2n\pi^2(\ell^2-\lambda c^2k^2)\); the constant-spatial-frequency modes have \(2n\pi^2\ell^2\).

Thus the restricted Hessian has **both infinite positive and infinite negative index**, and its Rayleigh quotients are unbounded above and below. The mode \((\ell,k)\) is negative exactly when \(\ell^2<\lambda c^2k^2\), positive exactly when the inequality is reversed, and an individual neutral Fourier mode occurs precisely at equality. If \(\sqrt\lambda |c|\) is rational, there are infinitely many independent exact zero-eigenvalue modes as well. A fixed temporal frequency and \(k\to\infty\) gives negative eigenvalues tending to \(-\infty\); a fixed spatial frequency and \(\ell\to\infty\) gives positive eigenvalues tending to \(+\infty\).

This sharpens the printed Theorem 17.16.25, which establishes an infinite negative subspace using the specific temporal mode \(\ell=1\), by diagonalizing **all** smooth radial variations and locating both signs and resonances. The printed theorem remains correct.

## Proof, including coefficients and normalization

The integrated radial density (17.16.24) is
\[
\mathscr S(u)=n\int_0^1
 \left\langle u_t^2(1+u_r)^d(1+u_{rr})\right\rangle\mathrm dt,
\quad \langle F\rangle=\tfrac12\int_0^2 F(r)\mathrm dr .
\]
Here \(\omega=\alpha_n+\beta_n\), \(\alpha_n^n=\beta_n^2=0\),
\(\int_{\mathbb P^d}\kappa^d=1\), and
\(\int_{\pi^{-1}(y)}\beta_n=2\), so \(\int_X\omega^n=2n\).
No extra volume factor is introduced.

The coefficient of \(\epsilon^2\) in the action at \(ct\) equals
\[
n\int_0^1\left\langle
w_t^2+2cw_t(dw_r+w_{rr})
+c^2\Bigl(\tfrac{d(d-1)}2w_r^2+dw_rw_{rr}\Bigr)
\right\rangle\mathrm dt.
\]
Periodicity gives \(\langle w_rw_{rr}\rangle=0\). Integrating
\(\langle w_t w_{rr}\rangle=-\langle w_{tr}w_r\rangle\)
over time gives \(-\tfrac12[\langle w_r^2\rangle]_0^1=0\).
Twice the remaining quadratic coefficient is
\[
2n\int\bigl\langle w_t^2+2dcw_tw_r
+\tfrac{d(d-1)}2c^2w_r^2\bigr\rangle
=2n\int\bigl\langle(w_t+dcw_r)^2
-\tfrac{d(d+1)}2c^2w_r^2\bigr\rangle,
\]
which proves (A) independently from the displayed Hessian. The first derivative vanishes because \(w\) vanishes at both temporal endpoints and \(\langle w_r\rangle=\langle w_{rr}\rangle=0\).

The change of variables \(s=r-dct\) preserves the period-two normalized integral, and
\(\partial_t W=w_t+dcw_r,\ \partial_sW=w_r\), proving (B).
Since \(\langle\cos^2(\pi ks)\rangle
=\langle\sin^2(\pi ks)\rangle=1/2\), Fourier orthogonality gives (C).
Integrating \(\sin^2(\ell\pi t)\) and
\(\cos^2(\ell\pi t)\) over \([0,1]\) gives \(1/2\) each, so (D) follows.
Smooth Fourier sums with endpoint-zero temporal coefficients are dense
in the indicated form domain. Exact negative-mode subspaces consist of finite
linear combinations with \(k\) large and \(\ell=1\); positivity persists for
sufficiently small perturbation amplitudes individually.

As a normalization check, \(n=3,d=2,c=1,\lambda=3,\ell=k=1\) gives
\(Q=-3\pi^2\), hence the second-order **action** coefficient is
\(-3\pi^2/2\), exactly the coefficient in the printed equation 17.16.27.
A separate finite-difference quadrature at \(n=3,c=1\) for
\((k,\ell)=(1,1),(1,2),(3,1)\) reproduced respectively
\(-29.6088132,\ 14.8044066,\ -384.9145716\) for \(Q\);
this was a small independent check only, **not** a project test or build.

## Audit judgment and dependencies

- **Severity:** low. **Status:** verified conditional deduction. No false theorem or missing proof was established; the extra diagonalization uses the radial density of 17.16.24 and the crosschecked (not independently certified) Hopf geometry of 23.1.32.
- **Affected mathematics:** refines the interpretation and strength of Theorem 17.16.25; distinguishes strict radial-action instability from the completed **basic** CAT(0) metric in Theorem 17.16.19. It neither proves that the unrestricted raw length infimum is zero nor verifies the general CAT(0) completion or all Perron existence claims.
- **Optional proposed improvement (separate future source review only):** add (B)–(D) as a compact spectral corollary, with explicit caveat about the domain of the indefinite Hessian, *without* changing the original theorem's hypotheses, permanent tags, or attribution.
- **Coverage and deferrals:** only the listed source-pinned paragraphs were independently checked. All earlier unresolved findings remain unresolved. Demailly approximation/regularization and its dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas, and positivity-loss programme remain **deferred-by-user** and were not opened.
