# 2026-11-23 — exact Lee-curvature energy coefficient and cross-chapter trace review

## Identity, baseline, scope, and limitations

- **Reviewed current main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Reading-edition source is **the integrated Pome HTML**, not an unintegrated source number or a private manuscript.
- **Full direct mathematical read:** `docs/sections/locally-conformally-kahler-geometry/index.html`, Git blob `6ebf8e604b45d3eb748037af506145273ca3875d`, physical lines **7–1355**: §23.2.1–72, including the LCK/Lee definitions, conformal and twisted operators, Vaisman volume uniqueness, the scalar Hopf radial ODE, Chern–Ricci/Gauduchon rigidity, Lee–Gauduchon duality, bimeromorphic invariance, and strongly Gauduchon exact-current criterion. This is an end-to-end current-edition read, not a certificate of the full transitive dependencies. The earlier §23.2.35–45 review is **re-read**, not counted as historically new.
- **Selected new nonexcluded cross-check:** `docs/sections/the-trace-operator/index.html`, Git blob `1f3a3e4f0317a308b43bd3df53dda84c5f3fa50a`, §20.2.29–37 (lines **660–821**) and the statements and nonexcluded formal algebra of §20.2.38–43 (lines **824–843, 885–940**). No claim of whole §20.2 review. **§20.2.39 Step 1, lines 850–884, relies on quasi-equisingular approximation: excluded by user; neither inspected for proof completion nor certified**.
- **New result:** `POME-LEE-CURVATURE-ENERGY-EXACT-COEFFICIENT-001`, **low / verified conditional deduction**, not a printed theorem error. No other new confirmed false original theorem and no new full upstream proof-chain certificate.
- Demailly regularization and its Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas, positivity-loss programme remain **deferred-by-user**, not resolved.

## POME-LEE-CURVATURE-ENERGY-EXACT-COEFFICIENT-001: exact Lee energy and volume-ray derivative

**Source, tags, and assumptions.** Use the explicit introductory restriction in integrated §23.2: **(X) connected compact complex, (n=dim_{mathbb C} Xgeq2)** (HTML line 8). Let (omega) be any smooth LCK Hermitian form with (domega=lambdawedgeomega), (dlambda=0), and associated Riemannian metric (g). The convention is (d^c=rac{i}{4pi}(arpartial-partial)); (lambda^c=d^cf) locally for (df=lambda). Define (kappa_lambda=d^clambda=-dlambda^c), a closed real ((1,1))-form. The inputs are **Proposition 23.2.7**, permanent tag `11EBB7AD1165`, Eq. **23.2.8**, tag `35851308DD2B`, at `docs/sections/locally-conformally-kahler-geometry/index.html` **lines 82–124**, and **Proposition 23.2.14**, permanent tag `E5F423FF7707`, lines **187–212**; original source family `non-kahler-pluripotential-theory`.

**Exact conclusion.** In this normalization,
[
oxed{quadint_Xkappa_lambdawedgeomega^{n-1}
=rac{n-1}{4pi n}int_X|lambda|_g^2,omega^n.quad}
]
For the real polynomial (V(t)=int_X(omega+tkappa_lambda)^n), this gives the **exact initial slope**
[
oxed{quad V'(0)=rac{n-1}{4pi}int_X|lambda|_g^2,omega^n.quad}
]
Both identities use the same unnormalized top power (omega^n); if one instead uses the Riemannian volume (omega^n/n!), multiply the right-hand integrals by (n!). In particular, (V'(0)>0) precisely when the Lee form is not identically zero, in the indicated LCK setting.

**Self-contained proof of the extra coefficient (conditional only on the printed Stokes identity).** At any point choose a real (g)-orthonormal unitary frame (e_j,Je_j) with real coframe (x_j,y_j), so that (omega=sum_j x_jwedge y_j). Write (lambda=sum_j(a_jx_j+b_jy_j)). The displayed (d^c) normalization means
[
lambda^c=rac1{4pi}sum_j(a_jy_j-b_jx_j).
]
When wedged with (omega^{n-1}), only the diagonal pairs in (lambdawedgelambda^c) survive. Thus, **pointwise**,
[
lambdawedgelambda^cwedgeomega^{n-1}
=rac{sum_j(a_j^2+b_j^2)}{4pi n},omega^n
=rac{|lambda|_g^2}{4pi n},omega^n.
]
Substitute into the exact Stokes identity (23.2.8),
(int_Xkappa_lambdawedgeomega^{n-1}=(n-1)int_Xlambdawedgelambda^cwedgeomega^{n-1}).
Differentiation of a finite wedge polynomial yields (V'(0)=nint_Xkappa_lambdawedgeomega^{n-1}). No approximation, limit interchange, regularity theorem, or elliptic existence theorem is used by this additional argument.

**Independent normalization sanity check.** In the §23.2.24 scalar Hopf Vaisman normalization (lines 395–419), (omega=alpha+eta), (kappa_lambda=alpha), (lambdawedgelambda^c=eta), and (eta) is the rank-one radial term. The preceding formula gives (|lambda|_g^2=4pi) and (V'(0)=(n-1)int_Xomega^n), agreeing with the direct polynomial (int_X((1+t)alpha+eta)^n=(1+t)^{n-1}int_Xomega^n). This checks the sign, factor (n), and (4pi) in the actual integrated conventions.

**Status and proposed correction.** **Low / verified conditional deduction**: the printed Propositions 23.2.7 and 23.2.14 are correct as checked here. An optional small supplemental sentence after Eq. 23.2.8 may state the exact coefficient; no source/body/registry patch has been made. **Affected interpretation/dependents:** the positive initial-volume slope used at §23.2.14–15 and the Lee-pairing obstruction at §23.2.10–11; their original conclusions are unaffected. This does **not** certify the upstream Kähler modification criterion or generalized Lamari theorem.

## Other direct checks and dependencies

1. **§23.2.2–10 (lines 23–167):** the global (nge2) hypothesis is explicitly in the section introduction at line 8. The Lee form is unique in this range; applying statements to dimension one would be illegitimate and is **not** logged as an error. Checked sign (kappa_lambda=d^clambda=-dlambda^c), conformal gauge, Stokes orientation, and the distinction between nonzero de Rham-exact Bott–Chern class and pseudoeffectivity.
2. **§23.2.14–17 (lines 191–314):** the constant least-relative-eigenvalue argument uses positivity of (V'), continuity to the first degenerate form, and zero top integral of the de Rham-exact (kappa_lambda). The explicit scalar Hopf family permits an indefinite representative without contradicting the separate semipositive-representative assertion. No new incorrect sign or limit identified.
3. **§23.2.20–45 (lines 325–775):** (D_lambda=exp(f)dd^cexp(-f)), and twisted constants are **not** gauge-free. The transverse mass identity (23.2.31) uses horizontal degree (2(n-1)+1) vanishing; the scalar radial ODE has a positive periodic solution and an ordered Lee-period parameter. Earlier radial checks are rechecks only. Existence/uniqueness of the smooth Hermitian MA equation used by Theorem 23.2.29 remains **an un-certified internal dependency** (14.2.1), not a theorem newly proved here.
4. **§23.2.47–72 (lines 786–1355):** traced the integrated Bianchi/Bochner cancellation (Eqs. 23.2.48–51), the Kodaira quotient illustration, finite-dimensional separation for Lee–Gauduchon duality (23.2.60), bimeromorphic (H^1)-comparison (23.2.63), strongly Gauduchon separation (23.2.69), and positive exact-current mass criterion (23.2.70). The generalized Lamari criterion (11.6.1), $partialarpartial$-lemma on the Kähler modification, and nontrivial positive-current compactness are upstream inputs **not transitively certified**.
5. **§20.2.29–37 and §20.2.38–43 selected:** checked that the restricted-volume definitions distinguish the non-Kähler locus from the non-nef locus, and that Eq. 20.2.36 is a *diagonal* choice of (epsilon_j<j^{-1}), followed by two-sided mass inequalities and monotonicity, rather than an unjustified swap of limits. The proof of Theorem 20.2.39 contains expressly excluded quasi-equisingular approximation and was **not** reopened. Internal mass-continuity inputs (20.2.17, 16.9.30), monotonicity (13.13.11), and restricted-volume continuity (the cited Matsumura Cor. 4.11) are **not re-proved/certified in this session**; this is not a claim of a confirmed gap.

## Scope accounting

- **1 whole integrated mathematical §23.2** read directly; its earlier partial visit is preserved, *not* counted as historically new without reconciliation.
- **1 selected nonexcluded §20.2**, not whole and not a new regularization audit.
- **1 low / verified conditional deduction**, **0 new confirmed original-theorem errors**, **0 resolved external inputs**, **0 fully certified transitive proof chains**.
- No mathematical-body, source-registry, canonicalization, tag, main, site, CI, test, or build changes. The old deferred items remain **deferred-by-user**.
