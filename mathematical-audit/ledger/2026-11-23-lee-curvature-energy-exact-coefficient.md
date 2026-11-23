# POME-LEE-CURVATURE-ENERGY-EXACT-COEFFICIENT-001

- **Date:** 2026-11-23
- **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`
- **Severity / status:** **low / verified conditional deduction**, **not** a false printed theorem and not a completed transitive upstream proof certificate.
- **Exact integrated file and blob:** `docs/sections/locally-conformally-kahler-geometry/index.html`, `6ebf8e604b45d3eb748037af506145273ca3875d`, lines **8, 82–124, 187–212, 395–419**.
- **Stable original source:** `non-kahler-pluripotential-theory`; Proposition 23.2.7 tag `11EBB7AD1165`, Eq. 23.2.8 tag `35851308DD2B`, Proposition 23.2.14 tag `E5F423FF7707`.
- **Hypotheses:** compact connected complex (X), (nge2); (omega) smooth LCK with (domega=lambdawedgeomega), (dlambda=0); (g) associated to (omega), (d^c=i(arpartial-partial)/(4pi)).
- **Verified deduction:**
  [
  int_Xkappa_lambdawedgeomega^{n-1}=rac{n-1}{4pi n}int_X|lambda|_g^2omega^n,
  qquad left.rac{d}{dt}ight|_{0}int_X(omega+tkappa_lambda)^n
  =rac{n-1}{4pi}int_X|lambda|_g^2omega^n.
  ]
- **Complete additional argument:** in a (g)-orthonormal unitary coframe (omega=sum x_jwedge y_j), write (lambda=sum(a_jx_j+b_jy_j)), (lambda^c=(4pi)^{-1}sum(a_jy_j-b_jx_j)). Diagonal wedge contraction gives (lambdawedgelambda^cwedgeomega^{n-1}=|lambda|_g^2omega^n/(4pi n)). Then apply Eq. 23.2.8 and polynomial differentiation. Hopf normalization (kappa_lambda=alpha), (lambdawedgelambda^c=eta) confirms the (4pi) and (n) factors.
- **Possible improvement, not mandatory correction:** append the exact norm expression to Eq. 23.2.8's discussion. No source or reading-edition edit is authorized by this finding.
- **Dependents/impact:** strengthens the precise scale of §23.2.14's positive volume-ray derivative and the Lee pairing used at §§23.2.10–15, without changing their conclusions. No use of excluded regularization.
- **Remaining external/internal premises:** the Stokes identity in §23.2.7 is directly checked; generalized Lamari criterion 11.6.1, modification/\(\partial\bar\partial\)-lemma inputs and smooth MA existence 14.2.1 are not transitively certified.
- **Detailed dated report:** [2026-11-23 Lee energy / trace rotation](../reports/2026-11-23-lee-energy-normalization-and-trace-restricted-volume-rotation.md).
