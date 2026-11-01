# Sharp differential Harnack estimates for positive harmonic functions on a half-space

**Audit date:** 2026-11-01. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Branch:** review/mathematical-audit. **Finding:** POME-HARM-HALFSPACE-SHARP-DIFFERENTIAL-HARNACK-001.
**Severity/status:** low / **verified conditional deduction**. This is **not** a confirmed original theorem error, an applied proof repair, or a complete verification of its representation-theorem dependency chain.

## Exact integrated source and anchors

- Primary section: docs/sections/kelvin-transforms-and-half-space-potentials/index.html, main blob f2615a5393af724c3996978212162f94911ff9d9; section 3.2, permanent tag 9728BD930155.
- Theorem **3.2.6** (Half-space representation), source label **classical-potential-theory:1C8A330A**, permanent tag **6BC86EEF03A9**, physical HTML lines **65–75** (statement) and **80–132** (proof).
- Its Poisson kernel is Equation **3.2.5**, lines **57–61**; its representation and weighted measure hypothesis are Equations **3.2.7–3.2.8**, source labels classical-potential-theory:C0A46F1A / classical-potential-theory:358F89A3, permanent tags **F3ED29BBAD39** / **8F7C774A9D89**, lines **65–75**.
- Theorem **3.2.12**, source label **classical-potential-theory:BB6DAC3F**, permanent tag **9ADD2DF19642**, lines **141–180**, supplies the independent normalized bounded-density Poisson example.
- Secondary, contextual review only: docs/sections/perron-theory-and-fine-boundary-limits/index.html, main blob **4bc2fb9317e2b6f6bb5b2d90208c677da8275eba**; Theorems **4.4.11–12**, Lemmas **4.4.13, 4.4.15–16**, Theorems **4.4.17–18**, physical lines **117–251**. The exterior-sphere mean/flux transfer was examined at lines **141–147** and compactification hypotheses at lines **179–199**; these are dependency/context checks, not new proofs or certifications.

## New exact statement

Let \(d\ge 2\), \(H=\mathbb R^{d-1}\times(0,\infty)\), and \(h\ge0\) be harmonic on \(H\). If \(h\not\equiv0\), then \(h>0\) and at every \((x',t)\in H\)
\[
\boxed{\ |\nabla_{x',t} h|\le \frac{d-1}{t}\,h,\quad
  (1-d)h\le t\,\partial_t h\le h,\quad
  |\nabla_{x'}h|\le \frac{d}{2t}\,h.\ }
\tag{A}
\]
Every displayed constant is sharp **within the nonnegative harmonic class**. Consequently, for any \(0<t_1<t_2\) and fixed \(x'\),
\[
\boxed{\ \left(\frac{t_2}{t_1}\right)^{1-d}
\le\frac{h(x',t_2)}{h(x',t_1)}
\le\frac{t_2}{t_1}.\ }
\tag{B}
\]
Equivalently \(t^{d-1}h(x',t)\) is nondecreasing, and \(h(x',t)/t\) is nonincreasing. Both powers in (B) are attained by explicit positive harmonic functions.

The proof uses Theorem 3.2.6 **as an internal hypothesis**; it does not independently redo the positive-measure representation or its compactness argument.

## Complete calculation

The actual theorem supplies \(h(x',t)=ct+\int P(x',t;z)\,d\nu(z)\) with \(c\ge0\), \(\nu\ge0\), and \(\int(1+|z|^2)^{-d/2}d\nu<\infty\). The kernel is
\[
P(x',t;z)=\frac{2}{s_{d-1}}\frac{t}
          {\bigl(|x'-z|^2+t^2\bigr)^{d/2}}.
\]
For fixed \(z\), put \(R^2=|x'-z|^2+t^2\) and \(q=t^2/R^2\in(0,1]\). Direct differentiation yields
\[
\nabla_{x'}\log P=-\frac{d(x'-z)}{R^2},\qquad
t\,\partial_t\log P=1-dq.
\]
The full logarithmic-gradient norm satisfies the **exact** identity
\[
t^2|\nabla\log P|^2
  =d^2q(1-q)+(1-dq)^2
  =1+d(d-2)q\le(d-1)^2\quad(d\ge2).
\tag{C}
\]
Likewise \(1-d\le t\,\partial_t P/P\le1\). The elementary inequality \(2t|x'-z|\le |x'-z|^2+t^2\) gives
\[
|\nabla_{x'}P|\le\frac{d}{2t}P.
\tag{D}
\]
The term \(ct\) has full gradient norm \(c=(ct)/t\), vertical derivative \(c=(ct)/t\), and zero horizontal gradient, hence obeys all three claimed bounds since \(d-1\ge1\).

The theorem's weighted-integrability hypothesis and the explicit uniform derivative estimates on compact subsets of \(H\), at physical lines 125–131, justify differentiating under the **positive Radon integral**. Integrating the pointwise kernel inequalities (C)–(D), then using the Euclidean triangle inequality, proves (A) without assuming \(\nu\) has finite total mass. The strong minimum principle gives \(h>0\) unless \(h\equiv0\). Integrating \((1-d)/t\le\partial_t\log h\le1/t\) proves (B) for every pair of levels, without any sequential-compactness or moving-measure argument.

For **sharpness**, \(h(x',t)=t\) attains the upper vertical bound and the upper power in (B). For a boundary point \(z_0\), the positive harmonic \(h=P(\,\cdot\,;z_0)\) at \(x'=z_0\) is a constant multiple of \(t^{1-d}\); it attains the lower vertical bound, the lower power in (B), and the full-gradient constant \((d-1)/t\). The horizontal bound is attained by the same Dirac Poisson integral at a point with \(|x'-z_0|=t\). These examples all satisfy the exact admissible weighted measure condition of (3.2.8). For \(d=2\), the full-gradient bound has sharp constant one as well.

The **sign hypothesis is indispensable**: the signed harmonic function \(h(x',t)=x_1\) has a nonzero gradient on its zero set, so no estimate of the form \(|\nabla h|\le Ch/t\) can hold without positivity. The zero function is handled trivially without taking logarithms.

## Adjudication, scope, and proposed use

The integrated Theorems 3.2.6 and 3.2.12 were checked at the specified Poisson normalization, weighted Radon-integrability and differentiation steps; **no new confirmed statement or proof error** was found in those passages. The new bound is a sharp, optional corollary immediately after Theorem 3.2.6, preserving its source attribution, all permanent tags and the existing representation statement. It does **not** supply a new alternative proof of the representation theorem, nor certify exterior Perron/Kelvin compactification results in §4.4.11–18.

**Dependents/uses:** differential and integrated Harnack comparison on fixed half-space vertical rays; gradient bounds for positive Poisson integrals; tests of PDE normalizations and admissible boundary measures. No source/body/registry/canonicalization/permanent-tag change is applied here.

**Coverage accounting:** additional *selected proof-level* checks of already previously sampled **§3.2** (particularly 3.2.6 and 3.2.12), and *contextual only* checks of previously sampled **§4.4**. Neither is newly first-reviewed; neither theorem's entire dependency chain, nor any mathematical section, has been certified. Current main ToC remains **25 chapters / 747 numbered sections / 0 fully certified mathematical sections**. Existing confirmed errors, gaps, proposed repairs, actual duplicates and external dependencies retain their existing statuses. The Demailly approximation/regularization and all dedicated Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion work remain **deferred-by-user**, neither reopened nor certified.

No project build, tests, CI, formalization, website publication or source edits were performed in this mathematical review; only branch-scoped audit notes are proposed.
