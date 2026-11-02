# Mathematical audit — nested monomial-ideal traces and genuinely new exceptional corrections (2026-11-03)

**Finding ID:** POME-BDIV-NESTED-MONOMIAL-EXCEPTIONAL-001. **Severity:** low. **Classification:** verified conditional deduction (explicit local/global model verified; the whole printed trace theory is NOT recertified). **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Scope:** a new direct finite-level multiplier-ideal and three-blowup calculation for Theorem 20.4.26, distinct from the previously checked ordinary point ideal and its single blowup in POME-POINT-IDEAL-BDIVISOR-NONBASE-CARTIER-001. No printed theorem is refuted or repaired.

## Pinned integrated reading sources

- <code>docs/sections/divisorial-currents-on-compact-modifications/index.html</code>, main Git blob <code>79d6e21f9d3784bf3761846f77f90ad075253644</code>. Section 20.4 permanent tag <code>D53B61AD71E9</code>, standing assumptions lines **7–28**; Theorem 20.4.18 source <code>non-kahler-pluripotential-theory:BA4B812E</code>, permanent <code>0AD88DBD3706</code>, lines **340–361**; Theorem 20.4.26 source <code>non-kahler-pluripotential-theory:4D5BC429</code>, permanent <code>400A4F39FD56</code>, lines **489–539**; its current identity (20.4.27) source <code>non-kahler-pluripotential-theory:4109312C</code>, permanent <code>D5C95521E68E</code>, lines **489–493**, and cocycle (20.4.28), permanent <code>398DC29813C5</code>, lines **494–497**. The finite-ideal correction and total-variation claim are lines **499–508, 524–538**.
- <code>docs/sections/restriction-and-intrinsic-trace-data/index.html</code>, blob <code>dbc3b722ceacb8232fe4c7b711e5ad98b0708f06</code>: Theorem 20.3.2, source <code>non-kahler-pluripotential-theory:BF417B5C</code>, permanent <code>7CD874C73EC9</code>, lines **23–41, 46–67**; definition of the restricted ideal and valuation. Here the ambient manifold equals its submanifold, X=Y, so restriction does not alter the ideal.
- <code>docs/sections/plurisubharmonic-functions-and-singularities--multiplier-ideals-and-logarithmic-poles/index.html</code>, blob <code>9256668b88735f821d06b0919466a6a8cba777ed</code>: weighted-integrability convention is <code>|f|^2 exp(-mu)</code>, as in Lemma 5.37.1. This is a convention crosscheck, NOT an audit of any excluded Bergman, extension, or regularization argument.

## Fixed compact analytic-singularity model

Let X=Y=P², p=[1:0:0], and normalize the Fubini–Study form by [ω_FS]=c1(O(1)) and dd^c=(i/2π)∂bar∂. Let three sections of O(3) be
\[
 F_1=Z_0Z_1^2,\qquad F_2=Z_2^3,\qquad F_3=Z_1^3.
\]
Their sole common zero is p. With \(\|Z\|^2=\sum_{j=0}^2|Z_j|^2\), define
\[
 u([Z])=\log\frac{|F_1(Z)|^2+|F_2(Z)|^2+|F_3(Z)|^2}{\|Z\|^6},
 \qquad \theta=3\omega_{\rm FS},\qquad T=\theta+dd^cu.
\]
This is a global θ-psh potential with analytic singularities and generic Lelong number zero on Y=X. The current T is the pullback of ω_FS by the associated rational map away from p. In the chart Z0=1, x=Z1/Z0, y=Z2/Z0, the base ideal is exactly I=(x²,y³), since x³ is redundant, and
\[
 u=\log(|x|^4+|y|^6)+O(1).
\]
The bounded term changes no multiplier ideal.

## Exact finite-weight ideals and divisorial valuations

For an integer m≥1, a monomial x^i y^j belongs to \(\mathcal I(mu)_p\) precisely when
\[
 \frac{i+1}{2}+\frac{j+1}{3}>m,
 \qquad\text{equivalently}\quad 3i+2j\ge 6m-4.
\tag{*}
\]
**Proof:** Up to harmless constants, its weighted norm is
\(\int_0^\epsilon\int_0^\epsilon s^it^j(s^2+t^3)^{-m}\,ds\,dt\), with \(s=|x|^2,t=|y|^2\). Split into t³≤s² and t³≥s². The two elementary one-variable power integrals converge exactly when \(i+1+(2/3)(j+1)>2m\). Angular integration and orthogonality of monomials show that any weighted-integrable holomorphic germ has only monomials satisfying (*); conversely the finitely generated monomial ideal defined by (*) consists of integrable germs. This directly establishes (*) without appeal to the excluded analytic approximation programme.

Blow up p with \(\pi_1:X_1\to X\). In the chart x=yt the pulled-back ideal is \(y^2(t^2,y)\); thus the first exceptional divisor E1 has valuation
\(\operatorname{ord}_{E_1}(x,y)=(1,1)\), with residual base ideal (t²,y) at q=(t,y)=0 on E1.

Blow up q with \(\pi_2:X_2\to X_1\). In the chart y=tv the ideal becomes \(t^3v^2(t,v)\). Thus on X2 the strict transform E1' has coefficient two and the new exceptional divisor E2 has coefficient three; the remaining ideal (t,v) is supported at the transverse intersection E1'∩E2. Along E2 the valuation of (x,y) is (2,1).

Finally blow up this intersection with \(\pi_3:X_3\to X_2\). In the chart v=tw, the ideal is \(t^6w^2\), with no remaining basepoint; the complementary chart t=vw gives \(v^6w^3\). The new exceptional E3 has valuation (3,2), and the principal ideal divisor on X3 is
\[
 D=2E_1''+3E_2'+6E_3.
\]

The valuation of a monomial along E1,E2,E3 is respectively i+j, 2i+j, 3i+2j. Minimizing these three weights subject to (*) gives the **exact** orders
\[
 \boxed{b_m(E_1)=2m-1,\qquad b_m(E_2)=3m-2,\qquad b_m(E_3)=6m-4.}
\]
Indeed \(i+j\ge(3i+2j)/3\) yields b_m(E1)≥2m−1, attained by x^(2m−1); \(2i+j\ge(3i+2j)/2\) yields b_m(E2)≥3m−2, attained by y^(3m−2); the third minimum is exactly the threshold 6m−4, attained by the same y-monomial. All are valid for m=1 as well. Thus τ(E1)=2, τ(E2)=3, τ(E3)=6 by direct limits b_m/m, independently testing Theorem 20.3.2 in this case.

## Two successive exceptional corrections and the finite-m endpoint

Since there is no divisorial component on X, \(S_X=0\). On the three successive models:
\[
 S_{X_1}=2[E_1],\quad
 S_{X_2}=2[E_1']+3[E_2],\quad
 S_{X_3}=2[E_1'']+3[E_2']+6[E_3].
\]
Because \(\pi_2^*E_1=E_1'+E_2\), the *new* correction is
\(S_{X_2}-\pi_2^*S_{X_1}=[E_2]\), not zero. Similarly \(\pi_3^*E_1'=E_1''+E_3\) and \(\pi_3^*E_2=E_2'+E_3\), so
\(S_{X_3}-\pi_3^*S_{X_2}=[E_3]\).
The cocycle identity (20.4.28) gives for the composite \(X_3\to X\) the divisor D, and the direct calculation gives exactly the same result.

The stronger finite-m computation gives
\[
 E_{m,\pi_2}=(1-1/m)E_2,\qquad E_{m,\pi_3}=(1-1/m)E_3.
\]
At m=1 these **both vanish**, while the limiting corrections are nonzero. In the exact positive trace-variation norm against a fixed Gauduchon metric γ on the respective target model,
\[
 \big\|[E_{m,\pi_j}]\wedge\gamma-
        [E_{\pi_j}]\wedge\gamma\big\|_{\rm TV}
 =m^{-1}\int_{E_j}\gamma,\qquad j=2,3.
\]
For complex surfaces γ^(r−1)=γ. This provides an explicit rate for this one model only, not a uniform rate for arbitrary singularities or modifications.

## Nef Cartier model and a numerical check

On X3 the ideal generated by the three pulled-back sections of O(3) is the invertible ideal O(−D). Dividing all sections by its local generator produces three globally basepoint-free sections of \(L=\pi^*O(3)\otimes O(-D)\), hence a holomorphic map \(\Phi:X_3\to\mathbb P^2\). Poincaré–Lelong applied in each principalizing chart yields
\[
 \pi^*T=[D]+\Phi^*\omega_{\rm FS}.
\]
The residual current is smooth and semipositive; L is therefore nef and realizes the Cartier b-divisor predicted by Theorem 20.4.18, without reusing its analytic regularization proof. The first and second blowups are not principalizing models; the third is.

For an independent intersection-number check, denote by F1,F2,F3 the *total transforms* of the three successive exceptional classes. Then
\(D=2F_1+F_2+F_3\), and
\[
 c_1(L)=3H-2F_1-F_2-F_3,\quad
 c_1(L)^2=9-4-1-1=3.
\]
Here H²=1, F_i²=−1, H·F_i=F_i·F_j=0 for i≠j, **only in this total-transform basis**. Confusing these classes with strict transforms would produce a wrong square. The nefness is independently established by the map Φ; positivity of the displayed square is not being substituted for a nefness proof.

## Adjudication, affected statements, and limitations

**Original printed Theorems 20.4.18 and 20.4.26: correct on the tested model; no new confirmed error or demonstrated global proof gap.** Their full proofs and all of §20.4 are not certified. This calculation specifically tests the effective correction (20.4.27), cocycle (20.4.28), finite-m correction and total-variation claim; it also distinguishes the one-point ordinary ideal example previously audited from **nested nonprincipal monomial ideals**, where exceptional corrections appear at TWO further centers. The model is a candidate explanatory example immediately after Theorem 20.4.26; no source or reading-body edit is requested/applied.

**Dependencies:** the calculation uses only explicit blowup charts, elementary monomial weighted integrals, the Poincaré–Lelong normalization, and Fubini–Study positivity. It does not construct general trace envelopes; it **does not** validate the Corollary 5.36.2 analytic approximant/curvature-loss input in the standing assumptions and Theorem 20.4.2. That dependency remains **deferred-by-user**, as do all dedicated Bergman, weighted L², Ohsawa–Takegoshi, multiscale atlas, and positivity-loss proof-completion tasks. This example is a self-contained check of the selected claimed formulas, not a replacement proof of the excluded input, and Hironaka's theorem is not required for these three explicit blowups.

**Coverage:** an independent proof-level finite-weight and three-model test of §20.4.26, with hypothesis-only §§20.3.2 and 5.37.1 convention crosschecks. This extends a previously partly reviewed §20.4, not a new first-reviewed numbered section; **25 chapters / 747 numbered sections / zero entire-section mathematical certifications**. No project test suite, build, CI, formal verification, website publication or production changes were made.
