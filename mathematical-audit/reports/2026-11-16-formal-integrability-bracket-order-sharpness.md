# Formal integrability: a sharp first-jet coordinate obstruction

- **Finding:** `POME-FORMALJ-BRACKET-ORDER-OBSTRUCTION-001`
- **Classification:** low severity; **verified conditional deduction** (indeed the model calculation is self-contained). Neither Proposition 9.53.2, Lemma 9.53.5, nor Theorem 9.53.13 is refuted. No claim of full theorem proof or transitive certification.
- **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **integrated HTML blob:** `218b71104a05350a9bb37b63c64638efecbd1e42`.
- **Reading-edition file:** `docs/sections/formal-integrability-and-smooth-complex-coordinates/index.html`.
- **Section source:** `demailly-complex-geometry`, section permanent tag `736577511A67`, subsection tag `9F96757DAC7B`.
- **Exact anchors:** Proposition 9.53.2 source `demailly-complex-geometry:EF13FDD7`, permanent `7D9D38C5DA0E`, physical lines 10–40; displayed decomposition (9.53.3), source `DAF605C6`, permanent `A64B66D1EDF0`, lines 16–19; Lemma 9.53.5 source `F9963253`, permanent `30126C7FDE2C`, lines 44–75; its estimate (9.53.6), source `C1E7380D`, permanent `1F71301249BA`, lines 46–49; Theorem 9.53.13 source `96C6A00C`, permanent `58DA08F550FB`, lines 162–204.
- **Coverage:** New proof/model examination of the *necessity* of the formal-integrability hypothesis and of the minus sign in the torsion decomposition, rather than another attempt to verify the theorem's global converse. No review of the weighted-L2 proof in Lemma 9.53.8 or of its analytic prerequisites.

## Explicit structure and tensor

Work on a polydisk in ordinary real coordinates underlying `C^2`, with complex notation `z_1,z_2`. Fix a real constant `epsilon != 0`. Specify the complex rank-two subbundle `T^{0,1}_J` by

```text
bar L_1 = d/d(bar z_1) + epsilon*(bar z_2)*d/d(z_2),
bar L_2 = d/d(bar z_2).
L_1     = d/d(z_1)     + epsilon*z_2*d/d(bar z_2),
L_2     = d/d(z_2).
```

The four displayed vector fields are linearly independent over `C`: the `d/d(bar z_1)` and `d/d(z_1)` coefficients eliminate the first two, then the `d/d(bar z_2)` and `d/d(z_2)` coefficients eliminate the others. Thus `T_C=T^{0,1}_J + T^{1,0}_J` is a direct sum exchanged by conjugation, defining a smooth real almost complex structure `J` with `J^2=-1`. At `z=0`, its value is the standard complex structure.

The brackets can be computed without geometric or analytic inputs:

```text
[bar L_1,bar L_2] = -epsilon*L_2,
[L_1,L_2]         = -epsilon*bar L_2.
```

Hence the tensor of Proposition 9.53.2 satisfies

```text
vartheta(L_1,L_2) = -epsilon*bar L_2 != 0.
```

This is the intrinsic obstruction; it does not disappear under a coordinate change. The `(0,1)` covector

```text
beta = d(bar z_2) - epsilon*z_2*d(z_1)
```

is dual to `bar L_2` and annihilates `L_1,L_2,bar L_1`. Therefore

```text
d beta = epsilon*d z_1 wedge d z_2,
(d beta)^(2,0) = epsilon*d z_1 wedge
                 (d z_2 - epsilon*(bar z_2)*d(bar z_1))
               = -vartheta'(beta).
```

This directly checks **the minus sign**, and the `(2,-1)` bidegree of the torsion term in equation (9.53.3). There is no missing constant or `dd^c` normalization in this calculation.

## Exact obstruction to complex-valued local coordinates

If a smooth function `f` satisfies `d'' f=0`, then `bar L_1 f=bar L_2 f=0`. Their bracket gives

```text
0 = [bar L_1,bar L_2] f = -epsilon*d f/d z_2 .
```

Together with `bar L_2 f=d f/d(bar z_2)=0` this makes `f` independent of both real coordinates of `z_2`. The first CR equation reduces to `d f/d(bar z_1)=0`. On a connected smaller polydisk all smooth `J`-holomorphic functions are **exactly** `f(z_1,z_2)=F(z_1)` with ordinary holomorphic `F`. In particular, no pair can be a local real coordinate chart on `C^2`; the necessity assertion of Theorem 9.53.13 is verified on this model, without invoking Newlander–Nirenberg or an L2 theorem.

A stronger order statement holds. Let `w_1,w_2` be any smooth complex-valued functions vanishing at the origin for which `d''w_j=O(|z|^s)` in any smooth local frame, where `s>=2`. Evaluating on the smooth fields `bar L_a` gives `bar L_a w_j=O(|z|^s)`. Differentiation along a smooth field lowers vanishing order by at most one, so

```text
-epsilon*(d w_j/d z_2)
 = [bar L_1,bar L_2]w_j = O(|z|^(s-1)).
```

At the origin, `d w_j/d z_2=0`, while `bar L_2 w_j=0` at the origin gives `d w_j/d(bar z_2)=0`. Therefore both differentials annihilate the full real `z_2`-plane: the real differential of `(w_1,w_2)` has rank at most two and cannot define local coordinates. This proves that **the formal-integrability assumption in Lemma 9.53.5 is indispensable already at order 2**. The boundary is sharp: the original standard coordinates satisfy `d''z_1=0`, `d''z_2(bar L_1)=epsilon*bar z_2`, and `d''z_2(bar L_2)=0`, hence `d''z_j=O(|z|)` and their real Jacobian is invertible.

By taking the product with standard `C^{n-2}`, the same obstruction and sharp first-order threshold hold in all complex dimensions `n>=2`. In complex dimension one, `Lambda^{2,0}=0`, so the tensor of Proposition 9.53.2 vanishes identically; this contrasts the higher-dimensional model without claiming a fresh proof of local integrability in dimension one.

## Status, correction and dependencies

**Verdict:** Verified explicit sharpness/necessity, not a confirmed error and not a repair of a false theorem. Proposition 9.53.2 has the correct sign on the stated `(0,1)` test form. Lemma 9.53.5 explicitly assumes formal integrability; the example proves why that assumption cannot be discarded. Theorem 9.53.13's necessity direction holds for the example, but its hard converse and ancillary elliptic machinery remain **unreviewed by this finding**.

**Suggested documentation-only improvement:** Add this two-field model as an optional example immediately following Lemma 9.53.5, explaining the optimal `s=1` obstruction and the torsion sign. Do **not** change any theorem statement, proof registry, source label, or permanent tag in the audit branch.

**Affected readers/dependents:** §9.53.2, equation 9.53.3, Lemma 9.53.5, and the necessity half of Theorem 9.53.13. No claim about the sufficiency half or later complex-space theorems. No regularization, Bergman, weighted L2, Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss programme is reopened; earlier excluded notes remain **deferred-by-user**, neither repaired nor certified.

**Checks actually performed:** independent symbolic differentiation of the two bracket coefficients (SymPy on the formal independent variables `z_j,bar z_j`) gave the vectors `(0,0,-epsilon,0)` and `(0,0,0,-epsilon)`. The mathematical proof above is self-contained. No repository tests, build, CI or website publication.
