# Chapter 15: dyadic singular sphere measures, sharp reference regularity, and lower-mass obstruction

**Date:** 2026-11-20. **Production baseline:** `main` `b6933b772f41b45918f7e25ed1afbbb1fd892272` (rechecked immediately before this report). **Audit branch:** `review/mathematical-audit`. **Classification:** `POME-SPHERE-DYADIC-HOLDER-SPECTRUM-001`, **low / verified conditional deduction**. This is not a false printed theorem, a certified transitive proof chain, or a production patch.

## Exact direct scope and stable locators

- Full mathematical reading of `docs/sections/equations-with-prescribed-singularities--singular-measures-on-shrinking-spheres/index.html`, physical lines **7–103**, blob **`354dfdf5224fac8896103ec09aa5936351021914`**. Equation 15.26.1 (source label `non-kahler-pluripotential-theory`, source tag `938F2C76`, permanent `938F2C76C18A`, lines 10–14); Proposition 15.26.2 source label `non-kahler-pluripotential-theory-92442012`, permanent `8F3C95237950`, lines 27–65; Corollary 15.26.3 `AB5B44EC4BDD`, lines 70–80; Theorem 15.26.4 `6076D6F3256C`, lines 85–103.
- Full mathematical reading of `docs/sections/equations-with-prescribed-singularities--lower-mass-and-solvability-for-all-measures/index.html`, physical lines **7–158**, blob **`fc7d4f24f72d9b6ec898eedc961b789e65ef3e25`**. Lemma 15.27.1 permanent `CE5CA1071A3C`, lines 26–52; Lemma 15.27.2 `366F6832AB46`, lines 56–71; Theorem 15.27.3 source label `non-kahler-pluripotential-theory-59B533D4`, permanent `C7AA7377C144`, lines 76–108, equation 15.27.4 permanent `8D5EB0B8CCD7`; Corollaries 15.27.5–6 permanent `810CC86832BF`, `05B92E5A4684`, lines 112–158.
- **Selected dependencies only:** `docs/sections/plurisubharmonic-functions-and-singularities--local-products-and-capacity/index.html`, Lemma 5.27.25 lines **516–539**, blob `ddb2ac8d9de27a22152872e07e5e787d138a790e`, permanent `3242D4BA1F13`; statements/selected reasoning in Theorem 15.25.1 lines 11–19, blob `0defdec5270db7ff34625b638c9ac2a31264ca4a`, and Theorem 15.10.1 lines 11–17, blob `6240b6dc071d12eac1476ed548736d012c1a4fa2`. These checks are **not** full reviews of their enclosing sections. No Demailly regularization or excluded proof-completion programme was opened.

## POME-SPHERE-DYADIC-HOLDER-SPECTRUM-001: a full sharp Hölder-exponent family

**Hypotheses.** Let `(X,h)` be compact Hermitian, `n>=2`, and fix the coordinate ball `B`, cutoff `chi`, radii `r_j=r_0 2^{-j}`, and normalized surface probabilities `sigma_j` from printed §15.26. Let `K>=1` be **the same uniform lower-curvature constant** for its bounded global cutoff functions `psi_j`, so that `dd^c psi_j >= -K h`. Fix *any* real `0<beta<1`. Define
[
S_{n,eta}=sum_{jge1}r_j^{neta},quad
Z_eta=2Ksum_{jge1}r_j^eta,quad
d_{j,eta}=r_j^eta/Z_eta,quad
u_{eta,0}=sum_{jge1}d_{j,eta}psi_j,quad
ho_eta=S_{n,eta}^{-1}sum_{jge1}r_j^{neta}sigma_j.
]
Here (psi_j=chilogmax{|z|^2,r_j^2}+(1-chi)) in `B`, extended by 1. Put (u_eta=u_{eta,0}-sup_X u_{eta,0}).

**Exact conclusions.**
[
egin{gathered}
u_etain mathrm{PSH}(X,h)cap C^{0,eta}(X),qquad
h+dd^c u_etage h/2,\
mathrm{MA}_h(u_eta)ge k_etaho_eta,qquad
k_eta=S_{n,eta}/Z_eta^n>0,qquad
0<mathrm{MA}_h(u_eta)(X)<infty.
end{gathered}
]
Each (ho_eta) is a **singular non-pluripolar probability measure**, and the **specific explicit reference** (u_eta) fails to belong to (C^{0,gamma}) in any neighborhood of the center for every (gamma>eta). In particular, the 1/2 exponent in the explicit potential constructed by printed Proposition 15.26.2 is *sharp for that construction*. We make **no claim** that no other potential dominating the same measure might enjoy better regularity.

**Complete proof.** First, (|psi_j|_infty=O(1+|log r_j|)) and (sum_j r_j^eta(1+j)<infty), so the series for (u_{eta,0}) converges uniformly. Since (sum_j d_{j,eta}=1/(2K)), weak passage in (dd^cpsi_jge-Kh) gives (h+dd^c u_{eta,0}ge h/2).

In the inner ball (chi=1), put (t=|z-z'|). The precise estimate used in the printed proof is
[
|psi_j(z)-psi_j(z')|le 2log(1+t/r_j).
]
For (r_jge t), (log(1+t/r_j)le t/r_j) and the dyadic geometric sum gives (tsum_{r_jge t}r_j^{eta-1}=O(t^eta)) since (eta<1). For (r_j<t), grouping (r_j) into shells (r_jasymp t2^{-ell}) yields
[
sum_{r_j<t}r_j^etalog(1+t/r_j)
le C_eta t^etasum_{ellge0}2^{-etaell}(1+ell)
=O(t^eta).
]
The transition annulus is a single fixed smooth function, independent of `j`; hence a finite-coordinate-cover argument gives global (C^{0,eta}). At the center, (sum_jr_j^eta|log r_j|<infty) ensures (u_{eta,0}(0)>-infty).

On the inner ball all (dd^cpsi_j) are positive closed. For the finite sum (u_{eta,N}=sum_{jle N}d_{j,eta}psi_j), positivity of mixed bounded Bedford–Taylor products and the smooth positive (h) imply
[
(h+dd^c u_{eta,N})^nge
sum_{jle N}d_{j,eta}^n(dd^cpsi_j)^n
=sum_{jle N}d_{j,eta}^nsigma_j.
]
The last identity is the **actually checked** spherical Lemma 5.27.25 under (dd^c=i(2pi)^{-1}partialarpartial); its proof integrates the radial shell and obtains total mass 1, so no extra (n!) appears. Uniform convergence of the bounded potentials gives weak convergence of Bedford–Taylor products; retain any fixed finite subset, test by nonnegative compactly supported functions, and then let its size grow. Because the sphere supports are contained in the inner ball, the resulting measure inequality extends globally. Each sphere probability is non-pluripolar by Lemma 5.27.25; a countable positive sum stays so. The union of spheres has zero smooth volume; thus (ho_etaperp dV). Finiteness of the total Monge–Ampère mass follows from local bounded-product estimates on finitely many charts; positivity follows from the displayed lower bound.

For the **sharpness**, choose any Euclidean unit vector (e), let (q=2^{-eta}), and evaluate on the original dyadic radii. In the region (chi=1),
[
egin{aligned}
u_eta(r_ke)-u_eta(0)
&=rac{2}{Z_eta}sum_{j>k}r_j^etalog(r_k/r_j)\
&=rac{2log 2}{Z_eta}r_k^eta
sum_{ellge1}ell,2^{-etaell}
=rac{2log 2}{Z_eta}rac{q}{(1-q)^2}r_k^eta.
end{aligned}
]
This coefficient is strictly positive and independent of (k). Dividing by (r_k^gamma) diverges for every (gamma>eta), so no local higher Hölder estimate is possible for this *constructed* potential. More precisely, on each (r_{k+1}le r=tr_kle r_k), (tin[1/2,1]),
[
u_eta(re)-u_eta(0)
=rac{2r_k^eta}{Z_eta}
left(rac{q}{1-q}log t+
rac{qlog2}{(1-q)^2}ight).
]
Thus the radial coefficient divided by (r^eta) has a nonconstant dyadic log-periodic profile, rather than a universal constant radial leading term. This finishes the independent explicit calculation.

**Consequences, conditional on existing theorems:** (
ule Mho_eta), (M<infty), implies (
ule (M/k_eta)mathrm{MA}_h(u_eta)); if (
u
e0), printed Theorem 15.25.1 supplies a Hölder continuous normalized homogeneous solution up to a positive scale, and printed Theorem 15.10.1 supplies the unique **bounded** exponential solution for every (lambda>0). These are applications of existing inputs, **not** independent reproofs of their existence or of the excluded regularization behind any input.

**Severity/status:** low / verified conditional deduction. **Proposed change:** optional explanatory remark after Proposition 15.26.2 indicating the general (0<eta<1) family and exact dyadic regularity of the explicit reference; preserve the original fixed-(ho) theorem, chart convention, permanent tags, and attributions. **Affected dependents:** only optional sharper reference families for Corollary 15.26.3 and Theorem 15.26.4; no printed statement needs correction.

## Full direct review of §15.27 (no new error finding)

- **Lemma 15.27.1, lines 26–52:** the strict domination application genuinely needs (a>c_h(q)), making (0<	au=c_h(q)/a<1); translating the *bounded* solution (v+A) for arbitrary (A) forces a contradiction at any finite point of (u). The deductions (qle rRightarrow c_h(q)ge c_h(r)) and (c_h(tq)=t^{-1}c_h(q)) preserve the inequality direction. The **upstream strict domination theorem 15.2.2 is a declared dependency**, not fully recertified.
- **Lemma 15.27.2, lines 56–71:** the positive lower scalar bound comes from Theorem 14.19.19 and uniform (|q_j|_{L^p}), while the Gauduchon trace bounds the scalar from above because (q_j^{1/n}	o q^{1/n}) in (L^n). Compactness is applied to subsequences, not to an arbitrary nonsequential net; the final subsequence criterion is valid for this sequence. Theorem 14.19.21 remains an upstream dependency.
- **Theorem 15.27.3, lines 76–108:** the weights (2^{-j}) have total mass one; (fge rac12min_X f_1>0); and the contradiction (a,2^{-j}le c_h(f_j)le2^{-2j}) is correct. The identification (v_-(h)=inf c_h(
u)) depends on Theorems 12.15.4 and 12.2.3 and was not transitively recertified.
- **Corollaries 15.27.5–6 and qualifications, lines 112–158:** the relative envelope-class equivalence depends on Theorem 15.37.4; the (L^p) exclusion is for (p>1) and follows by the continuous solvability result; mixing with (t f) gives (L^1) density of nonsubsolvable data because of domination by (tmu). The printed warning **does not** exclude unbounded exponential solutions and is preserved.

**Outcome:** no newly confirmed false theorem or distinct printed proof gap found in either fully read section. Zero transitive upstream proof chains certified. In particular this audit does **not** reopen the user-excluded Demailly/Bergman/(L^2)/Ohsawa–Takegoshi/multiscale/positivity-loss programme.

## Reproducibility and safety

All formulas above are finite geometric-series identities and the stated bounded-current identities; no build, website rendering, automated test, CI, publication, or full mathematical formalization was run. The only proposed production edit is an **audit-only recommendation**. No private source scans or credentials are reproduced.
