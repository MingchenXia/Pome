# Projective automorphisms: constant roots, jumping exceptional b-divisor trace, and lost NPP mass

**Finding:** \`POME-BDIV-EXCEPTIONAL-TRACE-L1-JUMP-001\`  
**Severity / status:** low / **verified conditional deduction (sharp hypothesis boundary)**. No printed theorem is disproved; no source or canonicalization change has been applied.  
**Reviewed production main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Audit baseline:** \`review/mathematical-audit\` at \`91b9c93ae8000a1d707953d02e146b5a0288c9ac\`.  
**Reading-edition file:** \`docs/sections/the-theory-of-b-divisors/index.html\`, blob \`4a793dfd462badcb351f54a36cb030cde14a399b\`.

## Exact internal anchors and scope

- Definition **20.1.14**, source \`sgpt:CB2E09F0\`, permanent tag \`165D43352903\`, HTML physical lines **149–167**: \(\mathbb D(T)_Y=\{\operatorname{Reg}\pi^*T\}\).
- Proposition **20.1.19** and equation **20.1.20**, source \`sgpt:91114C12\` and \`sgpt:A6C4C90C\), permanent tags \`87D0CCEB6DF9\` and \`64E2A79320D9\`, physical lines **265–319**: continuity of \(\mathbb D\) under **\(d_S\)** convergence, with a genuine net quantifier.
- Definition **20.1.6**, source \`sgpt:0B20B6FE\`, permanent \`E6F6681E7170\`, lines **56–63**; Lemma **20.1.7**, source \`sgpt:54FCB4C1\`, permanent \`F5B2C1F1E318\`, lines **66–98**, give the b-divisor volume and a separate *coefficientwise b-divisor* upper semicontinuity assertion.
- Theorem **20.1.15**, source \`sgpt:A0644B2C\`, permanent \`6EB1B4E1D222\`, physical lines **183–259**: its NPP-volume equality is context **only**; its excluded approximation input in Step 3 (lines 209ff.) was **not** audited or extended.

This is a newly inspected **specific hypothesis boundary of 20.1.19**, rather than a full proof verification of the proposition or the section. It also tests the meaning of the word "regular part" in 20.1.14. The projective-automorphism family below is an elementary algebraic degeneration and is not part of the author-excluded Demailly approximation/Bergman/\(L^2\)/extension/positivity-loss program.

## Statement: even a constant root does not prevent an exceptional trace jump

Let \(X=\mathbf P^2\), \(p=[1:0:0]\), \(H=c_1(\mathcal O_X(1))\), and let \(\omega=\omega_{\mathrm{FS}}\) represent \(H\), normalized so that \(\int_X\omega^2=1\). In the convention
\[
 dd^c=\frac{i}{2\pi}\partial\bar\partial,
\]
write
\[
 S([Z_0:Z_1:Z_2])=\frac{|Z_1|^2+|Z_2|^2}
 {|Z_0|^2+|Z_1|^2+|Z_2|^2},\qquad
 \varphi_\varepsilon=\log(S+\varepsilon),\quad
 \varphi=\log S.
\]
For \(0<\varepsilon<1\), put \(T_\varepsilon=\omega+dd^c\varphi_\varepsilon\) and \(T=\omega+dd^c\varphi\).

**All of the following hold simultaneously.**
1. Each \(T_\varepsilon\) is a **smooth Kähler form** in \(H\), \(\varphi_\varepsilon\searrow\varphi\) in \(L^1(X)\), and \(T_\varepsilon\rightharpoonup T\) as positive currents.
2. \(T\) has one isolated logarithmic pole at \(p\), with no divisorial component on \(X\). Thus **every root is identical**:
\[
 \mathbb D(T_\varepsilon)_X=\mathbb D(T)_X=H.
\]
3. For the blowup \(\pi:Y=\mathrm{Bl}_pX\to X\) with exceptional curve \(E\), the smooth currents have
\[
 \mathbb D(T_\varepsilon)_Y=\pi^*H,
\]
whereas
\[
 \mathbb D(T)_Y=\pi^*H-[E].
\]
The difference \([E]\neq0\) is visible only on the higher model.
4. Their top-degree masses behave in the strongest possible way:
\[
 \int_X T_\varepsilon^2=1,\qquad
 T_\varepsilon^2\rightharpoonup\delta_p,\qquad
 \int_X\langle T^2\rangle=0.
\]
Correspondingly, the Cartier b-divisors \(\mathbb D(T_\varepsilon)\) have volume \(1\), while \(\mathbb D(T)\) has volume \(0\).

Consequently **weak convergence of positive currents, even accompanied by decreasing \(L^1\) convergence of their global potentials and equality of all root classes, does not imply convergence of their b-divisors**. The \(d_S\) hypothesis of Proposition 20.1.19 cannot be replaced by those weaker conditions.

## Proof

### A. Smooth positivity and the current limit

For each \(\varepsilon>0\), consider the projective automorphism
\[
 A_\varepsilon[Z_0:Z_1:Z_2]
 =[\sqrt\varepsilon\,Z_0:\sqrt{1+\varepsilon}\,Z_1:
   \sqrt{1+\varepsilon}\,Z_2].
\]
Directly comparing homogeneous Fubini–Study potentials yields
\[
 T_\varepsilon=A_\varepsilon^*\omega_{\mathrm{FS}}.
\]
Hence \(T_\varepsilon\) is smooth and strictly positive, with class \(H\) and top self-intersection \(1\). This can also be checked on \(Z_0\neq0\), with coordinates \(z=Z_1/Z_0,w=Z_2/Z_0\):
\[
 T_\varepsilon=dd^c\log\!\bigl(\varepsilon+
                (1+\varepsilon)(|z|^2+|w|^2)\bigr).
\]
Writing \(a=1+\varepsilon\), \(r^2=|z|^2+|w|^2\), \(Q=\varepsilon+ar^2\), its Hermitian Hessian has tangential eigenvalue \(a/Q>0\) and radial eigenvalue \(a\varepsilon/Q^2>0\). Thus there is no hidden loss of positivity for fixed \(\varepsilon>0\).

Since \(S\ge0\) vanishes only at \(p\), the functions \(\varphi_\varepsilon\) decrease pointwise to \(\varphi\), a logarithmic quasi-psh function with isolated singularity. Near \(p\), \(\varphi=\log(r^2)-\log(1+r^2)\), whose absolute value is Lebesgue-integrable in real dimension four. Monotone convergence of the nonnegative differences \(\varphi_{\varepsilon_0}-\varphi_\varepsilon\), together with the local integrable limit, proves \(\|\varphi_\varepsilon-\varphi\|_{L^1(X)}\to0\). Distributional \(dd^c\) continuity therefore gives \(T_\varepsilon\rightharpoonup T\).

On \(X\setminus\{p\}\), the rational map
\[
 f:X\dashrightarrow\mathbf P^1,\qquad
 [Z_0:Z_1:Z_2]\mapsto[Z_1:Z_2]
\]
is holomorphic, and the same potential identity gives
\[
 T|_{X\setminus\{p\}}=f^*\omega_{\mathrm{FS},\mathbf P^1}.
\]
The current \(T\) is positive, and there is **no prime divisor in its singular set on \(X\)**. Its Siu divisorial part on \(X\) is therefore zero, proving the equality of roots in item 2.

### B. The exact exceptional coefficient

The blowup resolves \(f\) to a morphism \(\rho:Y\to\mathbf P^1\). In the blowup chart \((z,w)=(t,t\xi)\),
\[
 (\log(|z|^2+|w|^2))\circ\pi
 =\log|t|^2+\log(1+|\xi|^2).
\]
Poincaré–Lelong with the stated \(dd^c\) convention therefore gives the exact current identity
\[
 \pi^*T=[E]+\rho^*\omega_{\mathrm{FS},\mathbf P^1}.
\]
The second summand is a smooth semipositive form, so its **Siu regular part** is exactly itself. Since
\[
 \rho^*\mathcal O_{\mathbf P^1}(1)
 \simeq\pi^*\mathcal O_{\mathbf P^2}(1)\otimes\mathcal O_Y(-E),
\]
we get \(\mathbb D(T)_Y=\pi^*H-[E]\). Each \(\pi^*T_\varepsilon\) is smooth, so \(\operatorname{Reg}(\pi^*T_\varepsilon)=\pi^*T_\varepsilon\) and \(\mathbb D(T_\varepsilon)_Y=\pi^*H\). The exceptional class is nonzero because \(E^2=-1\). This proves item 3 without relying on any general approximation theorem.

### C. The mass escape is concentrated precisely at the pole

The pullback \(f^*\omega_{\mathrm{FS},\mathbf P^1}\) has rank at most one; thus \(T^2=0\) on the smooth locus \(X\setminus\{p\}\). The *non-pluripolar* product \(\langle T^2\rangle\) assigns no mass to the point \(p\), and hence is identically zero. On the other hand, \(T_\varepsilon\) is smooth in class \(H\), so \(\int_XT_\varepsilon^2=H^2=1\). On every compact subset of \(X\setminus\{p\}\), \(T_\varepsilon\to T\) smoothly, hence \(T_\varepsilon^2\to0\) there. Nonnegativity, fixed total mass and compactness of \(X\) imply \(T_\varepsilon^2\rightharpoonup\delta_p\).

The b-divisor of each \(T_\varepsilon\) is Cartier already on \(X\), with volume \(H^2=1\). The b-divisor of \(T\) is Cartier on \(Y\), with nef realizing class \(\rho^*H_{\mathbf P^1}=\pi^*H-[E]\) and square
\[
 (\pi^*H-[E])^2=H^2+E^2=1-1=0.
\]
Thus its b-divisor volume equals zero. This volume calculation uses the elementary geometry of the blowup; it does **not** invoke the excluded regularization step in the general proof of Theorem 20.1.15.

## Mathematical classification and proposal

The printed Proposition 20.1.19 only asserts continuity under \(d_S\), **not** under weak current convergence or \(L^1\) convergence of potentials. The family cannot converge in \(d_S\), since its explicitly computed trace at \(Y\) would contradict that proposition. Nothing in this model refutes the proposition, Definition 20.1.14, or Theorem 20.1.15. The nearby b-divisor-volume Lemma 20.1.7 also has a distinct premise—**coefficientwise convergence on every model**—which fails here. In particular, the limit of smooth Monge–Ampère measures has a point atom, while the NPP product of the singular limit deliberately discards that pluripolar atom; these are different operations.

**Proposed nonproduction change:** add this optional illustrative example **after Proposition 20.1.19**, explicitly contrasting (i) \(L^1\) / weak-current convergence, (ii) fixed root classes, (iii) exceptional-model trace convergence, and (iv) loss of NPP mass. Affected readers/dependents: 20.1.14–19, 20.1.24 and subsequent root-versus-b-divisor comparisons, and any use of weak convergence to pass to NPP volume. No proof of those later results is changed or certified.

**Actual coverage:** new proof/model-level inspection of Definition 20.1.14, Proposition 20.1.19's *hypotheses and conclusion* and the limiting-quantifier comparison with Lemma 20.1.7; Theorem 20.1.15 is dependency context only. §20.1 had prior selected audits, so this is **not a first-reviewed section or a complete-section certification**. Theorem 20.1.19's internal smoothing/envelope prerequisites are **not** reopened. The full collection still has **25 actual ToC chapters, 747 numbered sections, zero fully mathematically certified sections**.

**Independent structural inventory in this run:** \`docs/sections/problems-in-hermitian-pluripotential-theory/index.html\`, blob \`6f5551ea2240aedfcb4283c349dc7b46c51aaabc\`, physical lines 5–17, was opened for the first time as §24.1. It is a roadmap and contains **no numbered theorem or mathematical proof**. Count **orientation only**, not mathematical certification.

**Execution:** no test suite, CI, build, formalization, public-page publication, source/body/registry/permanent-tag modifications, or original-main edits. All original errors, candidate gaps and external inputs remain independently classified; Demailly approximation/regularization and dedicated Bergman/\(L^2\)/Ohsawa–Takegoshi/multiscale/positivity-loss work remain **deferred-by-user**, neither verified nor resolved.
