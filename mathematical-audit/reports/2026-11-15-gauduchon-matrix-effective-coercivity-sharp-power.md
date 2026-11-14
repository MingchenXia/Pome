# 2026-11-15 — Effective Gauduchon matrix coercivity and the sharp growth exponent

**Finding:** `POME-GAUD-MATRIX-EFFECTIVE-COERCIVITY-POWER-001`  
**Classification:** low / **verified conditional deduction** (not a false printed theorem and not a repair to the printed proof).  
**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**Integrated reading edition:** `docs/sections/smooth-monge-ampere-equations--the-matrix-structure-of-the-gauduchon-equation/index.html`, blob `6e1faedde219b856c0bf5ecaf566403ae999772e`.  
**Source label:** `non-kahler-pluripotential-theory:DDF2A98C`.  
**Permanent labels:** Lemma 14.13.5 = `DBC2334A4FC0`; equation (14.13.6) = `051408386360`; equation (14.13.7) = `2B456F0E5D2B`.  
**Exact physical anchors:** lemma and hypotheses at lines 113–128; proof at lines 131–155 (particularly 140–154). Nearby definition of `P_gamma` and `Q_0`: lines 10–35. No separate source text was needed.

## New quantitative consequence

Work at one Hermitian unitary point, in complex dimension `n >= 2`. Let `g` be Hermitian (not assumed positive), `Q=P_gamma(g)>0`, `Q_0>=tau gamma` with `tau>0`, and `det_gamma Q <= D` with `D>0`. Write the decreasing eigenvalues of `g` as `lambda_1 >= ... >= lambda_n`; `mu_i=(sum_{j != i}lambda_j)/(n-1)>0` are the increasing eigenvalues of `Q`. Set `t_i=1/mu_i`, `f_i=(sum_{j != i}t_j)/(n-1)`, `mathcal F=sum_i f_i=sum_i t_i`. Let `chi=(tr_gamma Q_0) gamma-(n-1)Q_0`.

For `L=lambda_1>0` define `c_n=(n-1)^((n-2)/(n-1))`. Then the following **effective version** of the coercivity inequality in Lemma 14.13.5 holds:
\[
 \mathcal F\ge c_n\left(\frac{L}{D}\right)^{1/(n-1)},\qquad
 \sum_i f_i(\chi_{i\bar i}-\lambda_i)\ge
 \left[\tau-\frac{n}{c_n}\left(\frac DL\right)^{1/(n-1)}\right]\mathcal F.
\]
In particular the printed conclusion (14.13.7) follows whenever
\[
 L\ \ge\ D\left(\frac{2n}{\tau c_n}\right)^{n-1}.
\]
This is a sufficient **explicit** threshold; no claim is made that its numerical constant is optimal. The exponent `1/(n-1)` in the universal growth bound for `mathcal F`, and equivalently in the displayed relative-error scale, **cannot be improved** under the printed pointwise hypotheses.

## Complete proof

Because `lambda_1=sum_{j=2}^n mu_j-(n-2)mu_1` and `0<mu_1<=...<=mu_n`, one has `L<= (n-1)mu_n` (valid also for `n=2`). Thus
\[
 \prod_{i=1}^{n-1}\mu_i
 =\frac{\det Q}{\mu_n}
 \le \frac D{\mu_n}\le \frac{(n-1)D}{L}.
\]
Applying the arithmetic–geometric mean inequality to the **first n−1 reciprocals** gives
\[
 \mathcal F=\sum_{i=1}^n\frac1{\mu_i}
 \ge (n-1)\left(\prod_{i=1}^{n-1}\mu_i\right)^{-1/(n-1)}
 \ge (n-1)^{(n-2)/(n-1)}(L/D)^{1/(n-1)}.
\]
At the diagonalizing point the linear operator `P_gamma` is self-adjoint for the trace pairing and `P_gamma(chi)=Q_0`. Therefore
\[
 \sum_i f_i\chi_{i\bar i}=\operatorname{tr}(Q^{-1}Q_0)\ge\tau\operatorname{tr}(Q^{-1})=\tau\mathcal F.
\]
The identity `sum_i f_i lambda_i=n` is explicitly derived in the printed lines 133–138: indeed
\[
 \sum_i f_i\lambda_i
 =\sum_j t_j \frac{\sum_{i\ne j}\lambda_i}{n-1}
 =\sum_j t_j\mu_j=n.
\]
Subtracting and using the new lower bound on `mathcal F` proves the effective inequality and the stated sufficient threshold. Only elementary matrix algebra and AM–GM were used. The separate printed bound `mathcal F>=nD^{-1/n}` remains valid, but is not re-registered as a new result.

## Sharpness of the *power*, with an explicit admissible family

Fix `n>=2` and `D>0`. For all sufficiently large `L`, put
\[
 \varepsilon=(D/L)^{1/(n-1)},\qquad
 Q_L=\mathrm{diag}(\underbrace{\varepsilon,\ldots,\varepsilon}_{n-1},L).
\]
Then `Q_L>0`, `det Q_L=D`, and `g_L=P_gamma^{-1}(Q_L)` has eigenvalues
\[
 \lambda_1=\cdots=\lambda_{n-1}=L,\qquad
 \lambda_n=(n-1)\varepsilon-(n-2)L.
\]
Hence its largest eigenvalue is exactly `L`, whereas
\[
 \mathcal F_L=(n-1)(L/D)^{1/(n-1)}+L^{-1}.
\]
Consequently there is **no** universal bound `mathcal F >= C L^a` for any `a>1/(n-1)` and constant `C>0` independent of `L`, under the same hypotheses. This family can be realized pointwise by taking `gamma` Euclidean, `Q_0=tau gamma` (equivalently `gamma_0=tau^{1/(n-1)}gamma`), and a real quadratic `v` with complex Hessian `g_L-tau gamma`; then `Z=0`. For `n>=3`, `g_L` is generally indefinite, which is permitted in the printed lemma. Choosing `chi=tau gamma` moreover gives `sum_i f_i(chi_{i\bar i}-lambda_i)/mathcal F=tau-n/mathcal F`, so even the **order** `L^{-1/(n-1)}` of the relative correction cannot be improved in general.

As an auxiliary algebraic sanity check only, the displayed inverse-eigenvalue identities and determinant were tested symbolically for `n=2,3,4,5,6`; this is neither a project test nor a substitute for the proof above.

## Audit disposition and dependencies

- **Printed Lemma 14.13.5 is correct.** The change is an optional explicit quantitative strengthening, not a source correction. No new confirmed error or proof gap is claimed.
- Downstream **§14.14 largest-eigenvalue estimate** may use the explicit threshold if its other hypotheses match; the global second-order estimate, the full Gauduchon PDE existence theorem in §14.17, and the preceding torsion-derivative identity §14.13.2 have **not** been transitively certified by this calculation.
- The example explains why one must not add the unstated requirement `g>0`; the natural positivity assumption is `P_gamma(g)>0`. No change to tags, canonicalization, theorem statements or source bodies is proposed. Attribution is unchanged.
- User-excluded Demailly regularization and its Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss programme remain **deferred-by-user**, not solved.
- Precise new proof-level coverage: just Lemma 14.13.5 and equations (14.13.6)–(14.13.7) in §14.13; **0** first-visits of numbered sections, **0** entire-section certificates. No project build, test suite, CI, publication, or main-branch edit.
