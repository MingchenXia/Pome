# Mathematical audit: exponential-measure order and the optimal transcendental Morse coefficient

**Date:** 2026-10-28 (Asia/Shanghai). **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
**Audit branch:** `review/mathematical-audit`. **Coverage:** selected printed statements and proofs in §§10.31 and 10.98, with the upstream order lemma §13.19 checked only for this inference. Neither complete section nor the upstream analytic existence theory is certified.

## POME-EXP-MEASURE-LOGRATIO-LINF-SHARP-001

**Severity:** low. **Status:** verified conditional deduction; printed theorem correct. **Proposed action:** optional corollary after Theorem 10.31.44; no change to its tag or hypotheses.

**Precise integrated locations.**
- `docs/sections/big-backgrounds-under-bounded-mass/index.html`, blob `0cc1ca66dd13369d9ae3f4aa43bb3bb074c05571`: §10.31 standing hypotheses and mass interval at physical lines 7–48; Theorem 10.31.44 at lines 1023–1123, source label `non-kahler-pluripotential-theory:14E81064`, permanent tag `D5758568A543`. Its uniqueness conclusion explicitly cites Corollary 13.19.3 at line 1122.
- `docs/sections/volumes-under-bounded-mass--domination-and-ordinary-envelopes/index.html`, blob `aa11cda5105062bb7d7b5eaaa1396940c679e097`: Corollary 13.19.3 at lines 45–57, source label `non-kahler-pluripotential-theory:25AC6489`, permanent tag `85CE662E8010`. The proof establishes exponential-weight order using Theorem 13.19.1; it is an **assumed internal dependency** here.

**Hypotheses.** Let (X,	heta,arphi,mathcal E_arphi) satisfy the standing assumptions of §10.31: (X) compact connected complex with the bounded mass property, (	heta) a smooth big real (1,1)-form (not necessarily closed), and (arphi) an ordinary model with positive lower volume. Fix (lambda>0). Let (mu,
u) be nonzero finite non-pluripolar measures and (mle M) real constants with
[
e^mmule
ule e^Mmu
]
in the order of measures. Let (u=u_mu) and (v=u_
u) be the unique relative-full-mass solutions of Theorem 10.31.44:
[
mathrm{MA}_	heta(u)=e^{lambda u}mu,qquad
mathrm{MA}_	heta(v)=e^{lambda v}
u.
]

**Conclusion (exact ordered data estimate).**
[
oxed{u-rac{M}{lambda} le v le u-rac{m}{lambda}.}
]
The inequalities are pointwise inequalities between extended-valued psh functions, so no undefined subtraction of two values (-infty) is used. In particular (e^{-a}mule
ule e^amu) implies (|u-v|le a/lambda) wherever both are finite, and hence the same (L^infty) bound almost everywhere for their difference. If (mule
u), then (vle u).

**Proof.** Constants do not change (mathrm{MA}_	heta), and (mathcal E_arphi) is invariant under adding constants. Define (w_-=u-M/lambda) and (w_+=u-m/lambda). The original equation gives
[
e^{-lambda w_-}mathrm{MA}_	heta(w_-)=e^Mmu
 ge 
u=e^{-lambda v}mathrm{MA}_	heta(v).
]
Apply the *weighted exponential-order* implication in Corollary 13.19.3 with its first argument (v) and second argument (w_-); conclude (vge w_-). Likewise
[
e^{-lambda w_+}mathrm{MA}_	heta(w_+)=e^mmu
 le
u=e^{-lambda v}mathrm{MA}_	heta(v).
]
Apply that corollary with first argument (w_+) and second (v); conclude (w_+ge v). These two inequalities give the claimed two-sided bound. No continuity or density of the measures was used.

**Optimality and limitations.** When (
u=e^tmu), the exact solution is (v=u-t/lambda), by the equation and uniqueness. Thus *both* coefficient (1/lambda) and the one-sided signs are sharp, even for smooth strictly positive measures in a Kähler class. This is a conditional corollary of the **printed** existence/uniqueness and exponential-order theorems, not a new proof of them. It controls the effect of a bounded logarithmic measure ratio; it asserts nothing when the measures are mutually singular or have an unbounded ratio. It is distinct from earlier fixed-reference (L^1)-density stability and weak-versus-TV findings. **Affected dependents:** optional stability remark following §10.31.44 and comparisons of measure-dependent solutions in §§10.31/15.37. No contradiction with any printed statement is alleged.

## POME-TRANS-MORSE-COEFF-N-SHARP-001

**Severity:** low. **Status:** verified conditional deduction and independent exact intersection check; printed theorem correct. **Proposed action:** optional sharpness example after Theorem 10.98.2; do not alter the theorem's historic attribution or normalizations.

**Precise integrated location.** `docs/sections/transcendental-morse-inequalities/index.html`, blob `8c3b365abcfd969b94e36611e28d6b87dfddc45b`: Theorem 10.98.2, source label `transcendental-positive-cones:6BC489CE`, permanent tag `DE32EEA596CD`, at physical lines 17–23; displayed inequality (10.98.3), source `transcendental-positive-cones:8CA0AB71`, permanent tag `74CB0E2B99CA`, at lines 19–21. The selected determinant/trace argument is at lines 69–95, weak-limit/determinant and nef-limit steps at lines 97–137.

**Sharpness statement.** For every integer (nge1), the coefficient (n) in
[
operatorname{Vol}(a-b)ge a^n-n,a^{n-1}!cdot b
]
cannot be replaced uniformly by a smaller real number, **even when both (a) and (b) are Kähler**.

**Exact example and full proof.** Take (X=(mathbf P^1)^n) and let (h_iin H^{1,1}(X,mathbb R)) be the pullbacks of the positive generator, normalized to (int_{mathbf P^1}h_i=1). Then (h_i^2=0) and (int_Xh_1cdots h_n=1). Fix (0<t<1), put (a=sum_{i=1}^n h_i) and (b=t h_1). The class (a-b=(1-t)h_1+sum_{i=2}^n h_i) is Kähler and (b) is nef. Ordinary product expansion gives
[
a^n=n!,qquad a^{n-1}cdot b=t(n-1)!,qquad
operatorname{Vol}(a-b)=(a-b)^n=n!(1-t).
]
Consequently equality holds *exactly* in the displayed Morse inequality for (t>0). If the coefficient (n) were replaced by (c<n), the proposed right-hand side would exceed the actual volume by ((n-c)t(n-1)!>0). To obtain **both inputs Kähler**, put (b_arepsilon=t h_1+arepsilon a) with (0<arepsilon<1-t). Then (b_arepsilon) and (a-b_arepsilon) are Kähler, and both the actual volume ((a-b_arepsilon)^n) and the putative right-hand side vary continuously with (arepsilon). Their strictly positive discrepancy for (c<n) at (arepsilon=0) survives for all sufficiently small positive (arepsilon). This proves sharpness without a non-Kähler analytic input. For (n=1) the same calculation reads (operatorname{Vol}(a-b)=a-b).

**Independent selected proof-step check, not upstream certification.** In the printed proof for (nge2), let (	au_j) be a smooth Kähler representative of (b), (gamma_j) one of (a), and let (0<lambda_1lecdotslelambda_n) be the eigenvalues of (gamma_j) relative to (	au_j). Set (P=lambda_2cdotslambda_n), (q=(	au_jwedgechi^{n-1})/	au_j^n), (m_j=int_{U_j}q,	au_j^n), and (delta=nC/A) with (C=int a^{n-1}b), (A=int a^n). The determinant identity and smooth MA right-hand side imply (lambda_1Pge(delta A/B)q); positivity gives
[
gamma_jwedgechi^{n-1}gelambda_1q,	au_j^n
ge(delta A/B)(q^2/P),	au_j^n.
]
As the elementary symmetric polynomial identity yields (P	au_j^nle ngamma_j^{n-1}wedge	au_j), Cauchy–Schwarz yields
[
m_j^2leleft(int_{U_j}rac{q^2}{P}	au_j^night)
            left(int_{U_j}P	au_j^night)
le nCint_{U_j}rac{q^2}{P}	au_j^n.
]
Therefore (int_{U_j}gamma_jwedgechi^{n-1}ge m_j^2/B), precisely the printed coefficient at (10.98.7). The comparison of the cohomological intersections in the final nef passage is valid because adding the *same* (arepsilon w) to (a,b) leaves (a-b) fixed. No continuity of (operatorname{Vol}) is needed at that step.

**Excluded input and exact boundary:** printed line 37 of §10.98 invokes the null-support construction *and its regularization*, Theorem 5.64.2 and Corollary 5.64.4. That input, and the dedicated Demailly/Bergman/L²/OT/multiscale/positivity-loss proof-completion programme, are **deferred-by-user**, not repaired, certified or reopened. The proof's separate smooth-MA existence, weak closedness (Lemma 10.97.1), cone extraction (Proposition 10.97.4), and volume inequality (10.98.1) are also treated as conditional upstream inputs, not independently proved in this session. This report certifies only the displayed elementary eigenvalue/integral algebra, the final nef-limit step, and the sharp projective model. **Affected dependents:** any use of the numerical coefficient (n) in transcendental Morse estimates and optional sharpness discussion; no false printed theorem.

## Actual coverage and carry-forward

Freshly read current `main` and `AGENTS.md`, `documentation/proof-expansions.md`, review-branch `README.md` and `mathematical-audit/LATEST.md`. The **two previously inventory-only sections** §§10.31 and 10.98 are upgraded *only* to the precisely anchored selected proof inspections above. Supporting §13.19.3 was inspected to apply the exponential order lemma, not declared a new full-section audit. The existing **747 unique section inventory** is preserved and **no complete section or chapter is certified**. All existing confirmed-error, unresolved and resolved ledger statuses remain unchanged; historical excluded work remains **deferred-by-user**. No mathematical body, source repository, registry, canonical tags, published site, pull request, CI, build or formal verification has been changed or run.
