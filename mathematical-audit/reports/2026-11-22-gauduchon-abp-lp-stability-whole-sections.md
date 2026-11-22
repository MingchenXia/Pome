# Direct mathematical audit: Gauduchon ansatz, ABP bound and bounded Monge–Ampère stability

- **Checkpoint:** `POME-AUDIT-GAUD-ABP-LP-STABILITY-FULL-20261122` — **coverage/dependency verification only; zero new mathematical findings**.
- **Date:** 2026-11-22. **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Branch for audit notes:** `review/mathematical-audit`. Three complete current integrated reading sections were checked. This is **not** a certificate of their complete transitive proof chains.
- **Policy:** The Demailly regularization/approximation and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programmes were **not accessed**, and remain **deferred-by-user, not resolved**.

## 1. Exact artifacts and statements checked

| Scope | Main-path and SHA | Source label / permanent tag | Physical lines |
|---|---|---|---|
| §14.10, full | `docs/sections/smooth-monge-ampere-equations--prescribing-a-gauduchon-volume-form/index.html` / `3a16d6685c70f1a5448c2a9c09b240d6fd44ed83` | source section `non-kahler-pluripotential-theory:185025DF`, tag `6950E7B1FBCB`; Theorem 14.10.1 source `3E8336C1`, tag `76AF759A4024` | 7–25 |
| §14.11, full | `docs/sections/smooth-monge-ampere-equations--bounds-for-the-gauduchon-potential/index.html` / `f3e973821ba8b04a496e4f996917ff491e3956d1` | Proposition 14.11.1 source `212AEE83`, tag `60FD5A56EE10`; Eq. 14.11.2 source `54915159`, tag `8F909795AE16` | 7–106 |
| §15.4, full | `docs/sections/equations-with-prescribed-singularities--a-quantitative-stability-estimate/index.html` / `f0c16c8d03d6175fd285bfbc1fc3a6af96cf6d8a` | Theorem 15.4.1 source `D2BDFCB4`, tag `72397EB33655`; Eq. 15.4.2 source `92E7388F`, tag `E617EAC91766`; Cor. 15.4.3 source `E87AEA7B`, tag `E429FB866D08` | 7–111 |
| prerequisites, **selected only** | `docs/tag/D716F01D638B/index.html`; `docs/tag/C67CEBABC968/index.html` | Lemma 15.3.1 tag `D716F01D638B`; Theorem 16.28.56 tag `C67CEBABC968` | selected statements and complete printed proofs, not a whole section |

### §14.10 — geometry and conventions

Assumptions in the integrated Theorem 14.10.1: connected compact complex $X$ of dimension $n\ge 2$, Hermitian initial form $\gamma_0$, Gauduchon form $\gamma$, smooth real $F$; there is a unique scalar-ansatz solution normalized by $\sup_Xu=0$. The equation is
\[
\Gamma_u=\gamma_0^{n-1}+dd^cu\wedge\gamma^{n-2}
 +\operatorname{Re}\left$\frac{i}{2\pi}\partial u\wedge\bar\partial\gamma^{n-2}\right$,
\qquad
\eta_u^{n-1}=\Gamma_u,\quad\eta_u^n=e^{F+b}\gamma^n .
\]
The printed auxiliary form $\xi_u=i\bar\partial u\wedge\gamma^{n-2}/(4\pi)$ gives
\[
\partial\xi_u+\bar\partial\overline{\xi_u}
 =dd^cu\wedge\gamma^{n-2}
 +\frac{i}{4\pi}(\partial u\wedge\bar\partial\gamma^{n-2}
 -\bar\partial u\wedge\partial\gamma^{n-2})
 =\Gamma_u-\gamma_0^{n-1},
\]
with the project's $dd^c=i\partial\bar\partial/(2\pi)$ convention; this verifies the factor and real-part sign. Consequently $dd^c\Gamma_u=dd^c\gamma_0^{n-1}$. **Only if $\gamma_0$ itself is Gauduchon** does the new metric inherit the Gauduchon condition; the text says exactly this, and does not claim that Gauduchon $\gamma$ alone suffices. The theorem's global smooth existence/uniqueness is a stated Székelyhidi–Tosatti–Weinkove input developed later in the chapter; this audit does not independently certify that PDE chain.

**Historical reconciliation, not a new finding:** the earlier `POME-GAUD-SURFACE-ADJOINT-SCALAR-001` already proves the complex-surface integrated-volume and adjoint specialization for (n=2), including the extra hypothesis $dd^c\gamma_0=0$. It must **not** be registered again as a new conditional deduction.

### §14.11 — scalar, adjoint Green kernel and contact-set ABP estimate

At a maximum/minimum of $u$, the gradient terms vanish and the sign of $dd^cu$ gives the respective order on $\Gamma_u$ and the determinant. This yields the displayed bounds for $b$ at lines 21–25, with the correct order of infimum/supremum. Taking $L u=\gamma\wedge(\Gamma_u-\gamma_0^{n-1})/\gamma^n$, positivity of $\Gamma_u$ gives $Lu\ge -C_0$. Assuming the fixed normalized adjoint Green kernel represented in lines 37–43, its sign convention
\[
v-\int v\,d\nu=-\int K Lv\,d\nu,\quad K\ge0
\]
implies at $\max u=0$ that $-\int u\,d\nu\le C$, with **no reversal of the inequality**.

For the contact-set argument, $v(x)=u(x)+\varepsilon|x|^2$, $|p|<\varepsilon/2$, and the boundary gap force the minimizer of $v-p\cdot x$ into the interior, giving (Dv=p), $D^2v\ge0$, and $v\le M+\varepsilon/2$. The area formula gives $|B_{\varepsilon/2}|\le\int_A\det D^2v$. On $A$, $|Du|\le 5\varepsilon/2$ and $D^2u\ge-2\varepsilon I$; the fixed positive $\gamma_0^{n-1}$ yields a uniform **lower** eigenvalue bound for the ((n-1,n-1)) coefficient matrix (Q_u). The prescribed determinant yields a matching **upper** eigenvalue bound. This controls $\operatorname{tr}_{\mathbb R}D^2v$ and therefore $0\le\det D^2v\le C$. Hence $|A|\ge c>0$ and the already established $L^1$ bound forces $-M\le C$. These steps were checked at physical lines 53–106 and do not rely on sequential compactness.

**Uncertified input:** the non-selfadjoint elliptic Green kernel's existence, diagonal singularity and uniform $L^1$-kernel bound are invoked at lines 37–43 without an in-section construction; the Fredholm/adjoint density invokes §11.4.2. These are PDE/parametrix dependencies, **not a confirmed false statement** and not claimed repaired in this run. No new external-dependency ID is assigned without reconciling older selected reviews.

### §15.4 — exact stability exponent and domination hypotheses

Theorem 15.4.1 assumes a semipositive big smooth $\theta$, (p>1), uniformly bounded solution $-C_0\le u\le0$, $MA_\theta(u)=f\,dV$ with $f\in L^p$, and comparison $v\in PSH(X,\theta)$, $v\le0$, which need **not** be bounded initially. Replacing $v$ by $\max(u,v)$ legitimately reduces to bounded $v$ without changing the positive part. At lines 36–68 the scale $m_\delta=\|1_{\{u<v-\delta\}}f\|_q$, auxiliary subsolution from Lemma 15.3.1, and $t=(2m_\delta/b)^{1/n}$ give $MA_\theta(w)\ge2m_\delta/b\,MA_\theta(h)\ge2\,1_{E_\delta}MA_\theta(u)$. The order $h-v\le C_0$ implies $w\le v-\delta$; **strict** domination is used only on $\{u<w\}\subset E_\delta$. The $m_\delta=0$ and $m_\delta\ge b/2$ cases are separately covered. The printed estimate
\[
m_\delta\le L$I/\delta$^{(p-q)/(pq)},\quad
\sup_X(v-u)\le\delta+C m_\delta^{1/n}
\]
optimizes with (a=(p-q)/(npq)), $\delta=I^{a/(1+a)}$ for $0<I\le1$, giving
\[
\eta_q=\frac{a}{1+a}=\frac{p-q}{npq+p-q}
\xrightarrow[q\downarrow1]{}\frac{p-1}{np+p-1}.
\]
The proof correctly states every **strictly smaller** exponent, not the endpoint. Corollary 15.4.3 applies the same bound in both directions, with a uniform density bound, provided the purported limit **already** has an $L^p$ density. The earlier `POME-PRESMA-STABILITY-EXPONENT-SHARP-001` established exponent sharpness and was **not** relogged. This run inspected the linked proofs of Lemma 15.3.1 and Theorem 16.28.56 as selected premises, but did **not** independently certify the entire non-collapsing/background-mass dependency of §16.28 or §14.19.

## 2. Classification, effects and proposed follow-up

- **Confirmed mathematical errors this run:** none.
- **New proof gaps:** none confirmed; the two elliptic/Monge–Ampère dependency chains above remain **not fully certified**.
- **New conditional deductions / genuine duplications / verified repairs:** none. Historical surface scalar and sharp stability exponent are explicit prior results and preserved without reclassification.
- **Coverage:** **3 whole current direct sections** (§§14.10, 14.11, 15.4), **2 selected tagged premises** (§§15.3.1, 16.28.56), **0 certified transitive proof chains**. Previous coverage is additive, not reset. At the 25-chapter, 747-section live main ToC, this report does not assert historical first visits.
- **Proposed audit-only next steps:** independently trace the fixed-operator elliptic Green representation in §14.11 and its precise Fredholm/parametrix inputs; separately audit the non-collapsing hypothesis used when §15.4 calls §16.28.56, after reconciling earlier entries. In both cases defer any cited Demailly regularization programme entirely.
- **Write scope:** audit documentation only on `review/mathematical-audit`; no main/source/body/registry/canonicalization/permanent-tag/site changes, no CI, no automated publication. No project build or test was run.
