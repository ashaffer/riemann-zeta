# Weil/global-support literature passport and recent-claim audit

**Date:** 2026-08-31  
**Literature checked through:** 2026-08-31  
**Source policy:** primary papers, official journal pages, arXiv, Zenodo, and
authors' released artifacts only.  
**Project protocol:** the Weil architecture below remains separate from the
QP/Turan strip architecture.  The Yang--Yang audit is quarantined in Section
3 because it bears on a different, zero-proportion/fourth-moment route.

## 0. Executive verdict

The literature search changes two pieces of the ledger but does not close the
first open edge.

1. Marcus Chuk's very recent preprint claims a substantially larger fixed
   window of strict Weil positivity. In project normalization it is

   ```text
   Chuk L = project physical half-window a,
   L_program = 4a = 4 L_Chuk.
   ```

   Thus Chuk's `L=0.8` is `a=0.8`, `L_program=3.2`, not `0.8` or `1.6`.
   It would move the certified seed from the formal `a=7/16`,
   `L_program=1.75`, to `a=0.8`, `L_program=3.2`. It still supplies no
   adjacent-support propagation. Its numerical certificate is plausible and
   consistent with an independent Galerkin sanity check, but the arXiv source
   contains no certificate artifact, and the theorem is presently not
   independently reproducible. Its `L^2` statement also omits the natural
   logarithmic form domain.

2. Suzuki's arXiv:2606.09096 was revised on 2026-08-17. The current Corollary
   1.6 target is

   \[
   e^{\phi(a,z)}W(a,\theta;z)\longrightarrow
   \frac{\xi(1/2-iz)}{\xi(1/2-iz)+\xi'(1/2-iz)},
   \]

   not the `z^2 xi/xi'` target recorded in
   `STAGE3-DETERMINANT-LIMIT.md`. That repository description is now
   historically stale. The convergence remains a conditional hypothesis;
   the paper does not prove the global identification.

3. No checked primary source proves a zeta-specific implication of the form

   ```text
   positivity on support [-a,a]
       => positivity on a strictly larger adjacent support.
   ```

   The precise missing mathematics remains arithmetic identification or
   unique continuation for the *actual zeta kernel*, with quantitative
   control of old/new cross terms. Abstract positive-definite extension is
   not enough: in one dimension every continuous positive-definite function
   on an interval has at least one global positive-definite extension, usually
   nonunique.

4. The Yang--Yang 79.62% item is explicitly released as a
   `certified-candidate`, not an established theorem. Its exact-rational and
   Lean artifacts are real and reproducible, but they do not certify the
   analytic moment input. More seriously, the paper's claimed truncation of
   the Alpoge--Furman `HL*(4)` correlation barrier is invalid as written: it
   reuses a fixed global logarithmic normalization `ell_1` as an undefined
   integer cell parameter and infers a nonexistent per-cell `ell^{-k}` decay.
   The headline must not be imported.

Durable status after this audit:

```text
RH:                                      OPEN
global arithmetic Weil positivity:      OPEN / RH-equivalent
zeta-specific adjacent propagation:     OPEN
formal project seed a=7/16:              PROVED in recorded scope
Chuk seed a=0.8:                         RECENT UNREFEREED CLAIM,
                                          plausible but unverified
Yang--Yang 79.62%:                       REFUTED AS A COMPLETE PROOF
                                          in its present written form
```

## 1. Passport for the actual project edge

### 1.1 Target

Let `Q_a` denote the localized arithmetic Weil form on functions supported in
`[-a,a]`, on its intrinsic logarithmic form domain. The first open edge is not
another finite Galerkin calculation. It is a theorem which, for the actual
zeta source, controls the block extension

\[
Q_{a+\delta}=
\begin{pmatrix}Q_a&C_{a,\delta}\\ C_{a,\delta}^*&N_{a,\delta}
\end{pmatrix}
\]

strongly enough to preserve nonnegativity or a quantified floor along a
cofinal sequence of supports.

### 1.2 Preserved fields

| Passport field | Required value |
|---|---|
| arithmetic source | completed Riemann zeta explicit formula, including prime powers, pole, and archimedean terms |
| coefficient cone | all complex test functions in the localized form domain, not merely one finite basis or autocorrelation subclass |
| support normalization | physical half-window `a`; project plots often use `L_program=4a` |
| quantifiers | for every legal test function, uniformly at each support step; eventually a cofinal support sequence |
| floor | a Schur/cross-term bound relative to the rapidly collapsing local ground floor |
| resolution | cutoff-free form or a two-sided certified cutoff error smaller than the claimed floor |
| downstream adapter | cofinal positivity -> global Weil positivity -> RH, using the already imported Weil equivalence |

### 1.3 Fast falsifiers

- A theorem that merely constructs *some* global positive-definite extension
  loses the zeta source and fails the passport.
- Self-adjointness or real zeros at each finite support, without convergence
  to a zeta-specific entire function, does not propagate positivity.
- Galerkin positivity without a tail enclosure does not prove full-domain
  positivity.
- A pointwise absolute envelope which replaces the prime comb by its total
  mass cannot remain computationally useful globally.

## 2. Marcus Chuk, arXiv:2608.24827: hostile theorem and artifact audit

Primary source: Marcus Chuk, *Weil positivity in compact windows: certified
two-sided bounds and a Landau--Widom decay law*,
[arXiv:2608.24827](https://arxiv.org/abs/2608.24827),
[DataCite DOI](https://doi.org/10.48550/arXiv.2608.24827), v1, 2026-08-25.
It is a nine-page, very recent, unrefereed preprint.

### 2.1 Exact normalization

Chuk uses

\[
\widehat f(t)=\int_{\mathbb R}f(u)e^{itu}\,du,
\qquad \operatorname{supp}f\subset[-L,L],
\]

and

\[
Q(f)=2F(i/2)^2+\frac1{2\pi}\int_{\mathbb R}|F(t)|^2\Psi_L(t)\,dt,
\]
\[
\Psi_L(t)=\Re\psi\!\left(\frac14+\frac{it}{2}\right)-\log\pi
-\sum_{\log n<2L}\frac{2\Lambda(n)}{\sqrt n}\cos(t\log n).
\]

This is the project's angular-frequency normalization. The conversion is

```text
L_Chuk = a_project,
full support width of f = 2a,
full support width of f * f_tilde = 4a = L_program.
```

At `L_Chuk=0.8`:

- `a_project=0.8`;
- `L_program=3.2`;
- the active prime powers are `2,3,4` because `log n<1.6`;
- the next prime activates at
  `L_program=2 log 5=3.218875824868...`, only
  `0.018875824868...` beyond the claimed window.

Relative to the repository's formal endpoint `a=7/16`, this is an increase
by `64/35=1.828571...`. Relative to the older software-only checkpoint
`L_program=2.996` (`a=0.749`), it is an increase by about `6.81%`.

### 2.2 Exact statements under audit

**Theorem 1 (paper numbering).** For every real even
`f in L^2(R)` supported in `[-0.8,0.8]`,

\[
Q(f)\ge 8.9\cdot10^{-18}\|f\|_2^2.
\]

Consequently the form is positive on autocorrelations supported in
`[-1.6,1.6]`. Corollary 9 extends the same lower bound to all complex `f` at
that support; Theorem 8 claims the ground state is simple and even, with

\[
8.9\cdot10^{-18}\le\lambda_1^{\rm even}
\le2.523\cdot10^{-16},\quad
\lambda_2^{\rm even}\ge2.085\cdot10^{-12},
\]
\[
8.206\cdot10^{-15}\le\lambda_1^{\rm odd}
\le2.347\cdot10^{-14}.
\]

**Theorem 3 (barrier).** Put

\[
A_L=\sum_{\log n<2L}\frac{2\Lambda(n)}{\sqrt n},
\qquad T_1(L)=2\pi e^{A_L}.
\]

Every application of the paper's Theorem 7 requires
`T_sharp>T_1(L)`; the PNT gives `A_L=(4+o(1))e^L`, and the proposed matrix
size is `N asymp L T_1`. Also the finite prime comb

\[
P_L(t)=\sum_{\log n<2L}\frac{2\Lambda(n)}{\sqrt n}\cos(t\log n)
\]

has `sup_t P_L(t)=A_L`.

**Theorem 7 (one-stroke reduction).** If

\[
\beta^*=\log\frac{T^\sharp}{2\pi}-\frac1{T^\sharp}-A_L>0,
\]

then for every real even supported `f`,

\[
Q(f)\ge R(f):=2F(i/2)^2+
\frac1\pi\int_0^{T^\sharp}(\Psi_L(t)-\beta^*)|F(t)|^2dt
+\beta^*\|f\|_2^2.
\]

In the even Legendre basis, `R` is represented by
`beta^* I+2pp^T+C`. With a sufficiently late Legendre cut, a positive leading
block and explicit tail errors imply a global lower bound.

At `L=0.8` the paper reports

```text
A_L = 2.94197352522...,
T_1 = 119.086556...,
T_sharp = 200,
beta^* = 0.513466775...,
N = 200 even modes,
50-digit arithmetic.
```

It reports a second run at `T_sharp=150`, for which
`beta^*=0.224118...`.

### 2.3 Form-domain defect

The introduction defines `Q` for even real continuous compactly supported
functions, while Theorem 1 quantifies over all `L^2`. Since
`Psi_L(t)=log|t|+O(1)` at infinity, the natural closed form domain is

\[
\mathcal H_{\log,a}=
\left\{f\in L^2[-a,a]:
\int_{\mathbb R}\log(2+t^2)|\widehat f(t)|^2dt<\infty\right\}.
\]

For generic `L^2` functions the displayed integral may be `+infinity`, so
`Q(f)` is not a finite quadratic form on all of `L^2`. The lower inequality
can likely be repaired by declaring an extended-valued closed form on all
`L^2`, or by restricting to `H_log`. The min--max, ground-state, and
simplicity statements require the associated Friedrichs operator and form
domain to be stated. This is a real theorem-statement defect, although it
does not by itself refute the intended lower bound on `H_log`.

### 2.4 Artifact and reproducibility status

The official arXiv source contains only:

```text
arxiv_short.tex
weil_discrimination.png
weil_mp_verdict.png
00README.json
```

There is no code, matrix, quadrature rule or nodes, interval matrix,
Bernstein-ellipse computation, Cholesky factor, residual enclosure, or tail
error file. The paper asserts, but does not expose enough data to reproduce,

- quadrature error below `1e-42`;
- shifted verified-Cholesky residual below `1e-50`;
- block-tail errors below `1e-100`.

An independent project-side, high-precision Legendre assembly at
`L_program=3.2` gave even-sector minima

```text
m=32: 5.7499e-16
m=48: 1.7460e-17
m=64: 1.7026e-17
m=80: 1.6787e-17
```

with the next even value about `8.44e-12` and the odd minimum about
`1.59e-14` at `m=80`. This is consistent with the claimed scales and finds
no gross normalization error. It is a diagnostic, not an independent
certificate.

**Trust status:** plausible recent numerical theorem claim, but not yet
reproducible or independently verified. Do not replace the formal project
endpoint until an interval-Arb reproduction checks the full matrix and tails.

### 2.5 Correct scope of the barrier

The equality `sup P_L=A_L` is correct for a uniform constant bound on the
finite cosine comb. It does **not** prove that every pointwise or spectral
certificate must integrate to `T_1`:

- the near-maximal recurrences occur at arbitrarily late times, where the
  archimedean `log t` term is also large;
- a `t`-dependent bound on the whole symbol can exploit that correlation;
- direct interval certification on a compact transition band, followed by a
  crude bound only after the symbol is safely positive, is not excluded.

Indeed, the repository's earlier `n=4` certificate split near `S=110`, below
the corresponding crude `T_1 about 119`, and treated the transition band
directly. Thus Theorem 3 is a barrier for the paper's absolute constant-comb
envelope, not a universal no-go for all pointwise-symbol methods.

### 2.6 Passport fit

| Field | Chuk fit |
|---|---|
| source | exact completed-zeta prime/pole/archimedean source |
| coefficient cone | intended all complex localized functions; domain needs repair |
| normalization | exact match after `L_program=4L_Chuk` conversion |
| full-band floor | claimed strict `8.9e-18`, but artifact unavailable |
| downstream | improves only the local seed |
| adjacent propagation | absent |

The tiny floor and proximity to the `p=5` activation reinforce, rather than
remove, the need for an event-specific adjacent-support theorem.

## 3. Yang--Yang 79.62%: separate fourth-moment claim audit

Primary release: Hongyi Yang and Shihua Yang, *More than 79.62% of the zeros
of the Riemann zeta function are simple and on the critical line*,
[Zenodo record DOI 10.5281/zenodo.21975237](https://doi.org/10.5281/zenodo.21975237),
2026-08-17; concept DOI `10.5281/zenodo.21975236`. Public artifact:
[GitHub reproduction repository](https://github.com/JoshuaHKU/zeta-0.7947-reproduction),
audited at commit `d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`.

The release itself labels the claim `certified-candidate`, says the analytic
layer is unformalized, and notes that external review is pending.

### 3.1 Claimed theorem and provenance

The headline is

\[
\liminf_{T\to\infty}\frac{N_0^s(T,2T)}{N(T,2T)}\ge0.7962,
\qquad
\liminf_{T\to\infty}\frac{N_d(T,2T)}{N(T,2T)}\ge0.8981,
\]

with the same claim for every fixed primitive Dirichlet `L`-function. The
paper asserts normalized trace moments

\[
m_3=2,\quad m_4=13/4,\quad m_5=101/18,\quad
m_6=12809/1260,
\]

and then uses an exact degree-six Chebyshev--Markov certificate.

The values through `m_4=13/4` are exactly those in Alpoge--Furman's
conditional `HL*(4)` discussion. In
[arXiv:2608.13637, Section 7.2](https://arxiv.org/abs/2608.13637),
`HL*(4)` means the asserted trace-moment asymptotics through order four;
at `k=4` it encodes a Hardy--Littlewood-type asymptotic for

\[
\sum_m(\Lambda*\Lambda)(m)(\Lambda*\Lambda)(m+h),
\qquad |h|\le X^2/T.
\]

Alpoge--Furman explicitly say the ordinary diagonal method only covers the
Rudnick--Sarnak range `X^k <= T^(2-epsilon)` and supplies no higher moment at
`X asymp T`; `HL*(4)` would give `13/18`. Yang--Yang therefore does not avoid
the barrier by a known theorem. It claims a new averaged, truncated version
of precisely this fourth-correlation input.

### 3.2 What the artifacts really certify

The package is nontrivial and partially reproducible.

- The delivered four-module Lean 4 package builds locally with Lean 4.33.0,
  with no `sorry` and no Mathlib dependency.
- `certification/certify_lp.py` reproduces exactly

  ```text
  w0 = 829278553005924403328783 / 8140995278473611944088783
     = 0.10186451713081071...
  1-2w0 = 0.7962709657383785...
  1-w0  = 0.8981354828691893...
  ```

- Lean checks rational polynomial identities, selected finite local laws,
  and arithmetic at *assumed/pinned* moment values.

It does not formalize the prime-correlation theorem, truncation, spectral
major/minor-arc estimates, the derivation of the moments from zeta, or the
measure/counting adapter. The shipped `build.log` itself says the pinned
moments and analytic chain remain outside Lean. There are also minor package
version inconsistencies: the current checkout has four Lean roots while the
recorded log describes an earlier five-root build, and some pipeline labels
still say `0.7947`. These do not invalidate the rational certificate, but they
underline that the certificate is conditional on the analytic moments.

### 3.3 Decisive failure of the truncation discharge

The paper globally defines, once and explicitly,

\[
l=\log(T/2\pi),\qquad
\ell_1=l+2\log2-1,
\]

so `ell_1` is a single real number, used in

\[
\mu_k=\frac{\operatorname{tr}\widetilde G^k}{d\ell_1^k}.
\]

In Section 6 it silently reuses the same symbol as an alleged integer
`cell parameter`, asserting:

- cell weights `ell_1^{-k}`;
- a divisor-bound for the number of tuples with `ell_1=ell`;
- restriction to cells `ell_1 <= P`;
- the tail `P^{-(k-2)+epsilon}`.

No second definition of a cell parameter appears anywhere in the paper or
released code. The proof's line

```text
weight x mass x multiplicity
    = ell^{-k} x ell x ell^epsilon
```

has no connection to the actual trace expansion. A fixed global logarithmic
normalization cannot create decay as a cell modulus grows. In particular,
the inference

```text
unrestricted fourth correlation
    -> only moduli <= (log X)^B are consumed
```

is not proved. This is exactly the step needed to turn the open unrestricted
`HL*(4)` input into something allegedly handled by Siegel--Walfisz and
Vaughan. Consequently Theorem 7.5 and the headline do not follow.

Even if `ell_1` is charitably renamed to some intended LCM or cell modulus,
Lemmas 6.1--6.2 contain only a paragraph-level count and never derive the
claimed `ell^{-k}` coefficient from the actual restricted-product weights.
A corrected symbol alone would not repair the proof.

### 3.4 Further analytic gaps

The claimed Lemma D says, for fixed `B`, prime powers
`b_1,b_2 <= (log X)^B`, window length `Y asymp X^theta`,
`theta in (1/2,1]`, and every `A`,

\[
\sum_{k\le K}\sum_{|j|\le J}
|N_4(k,j)-\mathfrak S_4(k,j)V(k,j)|^2
\ll_{A,B}KJV^2(\log X)^{-A}.
\]

Two additional joints are not established:

1. The major-arc proof cites standard Siegel--Walfisz to obtain an error
   `O(Y log^{-A}Y)` in intervals of length `Y asymp X^theta` for every
   `theta>1/2`. The cited long-interval theorem gives an error based on `X`,
   not this short-interval bound. The paper's main endpoint uses `Y asymp X`,
   so this overstatement is not alone a refutation of that endpoint, but the
   displayed theorem is not proved over its stated range.

2. The minor/mixed leaf says the necessary summed spectral `L^2` budget,
   including image-family spacing and a hybrid large sieve, is `classical`
   and finite-face checked. That bookkeeping is the substance of the needed
   averaged fourth-correlation estimate; a pointwise Vaughan bound and finite
   experiments do not establish its asymptotic normalization. The fifth- and
   sixth-moment arguments then say the same closure transports `verbatim`,
   without proofs of the new analytic ledgers.

**Audit verdict:** the finite identities and exact certificate are useful
conditional computations. The claimed zeta moment theorem and 79.62%
conclusion are not established. This item neither proves the sharp project
four-cycle theorem nor changes a Weil/global-support edge.

## 4. Weil, screw, de Branges, spectral, Toeplitz, and Hankel imports

### LIT-W1 -- Weil/Bombieri/Yoshida positivity (`IMPORTED`, known to repo)

For the completed zeta Weil distribution `W`, RH is equivalent to

\[
W(\varphi*\widetilde\varphi)\ge0
\quad\text{for every }\varphi\in C_c^\infty(\mathbb R).
\]

Bombieri further treats the localized `L^2` minimization and proves existence
of a minimizer, while recovering Yoshida's sufficiently-small-support
positivity. Primary sources:

- Andre Weil, *Sur les formules explicites de la theorie des nombres*,
  [DOI 10.1070/IM1972v006n01ABEH001866](https://doi.org/10.1070/IM1972v006n01ABEH001866).
- Enrico Bombieri, *Remarks on Weil's quadratic functional in the theory of
  prime numbers, I*, [primary journal scan](https://www.bdim.eu/item?id=RLIN_2000_9_11_3_183_0).
- Masatoshi Suzuki's published restatement and proof interfaces in
  [JLMS 108 (2023), DOI 10.1112/jlms.12785](https://doi.org/10.1112/jlms.12785).

**Passport fit:** this is the downstream RH equivalence, not propagation.

### LIT-W2 -- Suzuki's localized screw form (`IMPORTED`, known)

Suzuki 2023 defines the zeta screw function `g=-Psi` and the localized kernel
form on `L^2(-a,a)`. His main equivalences imply:

- RH iff the global screw kernel is positive semidefinite;
- RH iff every finite localized form is nonnegative;
- RH iff every finite localized form is nondegenerate;
- for each fixed `a`, the localized integral operator is trace class.

The kernel identity under RH is

\[
G_g(t,u)=\sum_\gamma
\frac{(e^{i\gamma t}-1)(e^{-i\gamma u}-1)}{\gamma^2}.
\]

Primary source:
[Suzuki, JLMS 2023](https://doi.org/10.1112/jlms.12785), also
[arXiv:2206.03682](https://arxiv.org/abs/2206.03682).

**Passport fit:** exact zeta source and correct local forms. It packages the
equivalence but does not derive positivity at `a+delta` from positivity at
`a`.

### LIT-W3 -- shifted inner-function criterion (`IMPORTED`, known)

For

\[
\Theta_\omega(z)=
\frac{\xi(1/2-\omega-iz)}{\xi(1/2+\omega-iz)},
\]

[Suzuki, Proposition 1.2](https://arxiv.org/abs/1204.1827) states, for
`omega_0>=0`, equivalence between

\[
\zeta(s)\ne0\quad(\Re s>1/2+\omega_0)
\]

and `Theta_omega` being a meromorphic inner function in the upper half-plane
for every `omega>omega_0`. Theorem 2.2 gives, at fixed `omega`, equivalent
convolution/support conditions for innerness. Appendix Theorem A.1 gives
sufficient tail-sign or limit conditions on the inverse Mellin kernel.

**Passport mismatch:** the quantifier is still *every shift* above a
threshold. Fixed-shift innerness or an abstract canonical system does not
propagate the arithmetic Weil support. This literature does not rescue the
repository's already-falsified shifted-order shortcut.

### LIT-W4 -- 2026 Friedrichs and first-order extension framework
(`IMPORTED`, v2 update new to ledger)

[Suzuki, arXiv:2606.09096v2](https://arxiv.org/abs/2606.09096v2) proves:

- **Theorem 1.1:** the localized self-adjoint Weil operator `A_a` is the
  Friedrichs extension of `B_a=D^*G_aD`, initially on `H_0^1(-a,a)`;
- **Corollary 1.2:** the lowest eigenvalue is the infimum of the Rayleigh
  quotient over `C_c^infinity(-a,a)` in the form closure;
- **Theorem 1.3:** `a -> lambda_a` is continuous;
- **Theorem 1.4:** for sufficiently small `a`, the lowest eigenvalue is
  positive and simple, its eigenfunction is even, and

  \[
  \lambda_a=\log(1/a)+\mu_1-\log(2\pi)+\psi(2)-1+O(a);
  \]

- **Theorem 1.5:** self-adjoint extensions of a first derivative in the
  form Hilbert space have characteristic entire functions
  `W(a,theta;z)` whose zeros are precisely their spectra and are all real;
- **Corollary 1.6:** compact-local convergence, after normalization, to
  `xi/(xi+xi')` would imply RH.

**New ledger correction:** v1 had a different conditional target. The
current ratio is exactly the one displayed above. This strengthens the
operator setup and domain bookkeeping. It does not prove convergence or
adjacent-support positivity.

### LIT-W5 -- Hilbert-Weil/de Branges identification (`IMPORTED`, known)

Under RH, Suzuki identifies the completion of the Weil form with a de Branges
space associated with

\[
E_\xi(z)=\xi(1/2-iz)+\xi'(1/2-iz).
\]

Primary source:
[Suzuki, arXiv:2301.00421v3](https://arxiv.org/abs/2301.00421v3), related
[DOI 10.4153/S0008414X25101739](https://doi.org/10.4153/S0008414X25101739).
This explains the denominator in Suzuki's revised 2026 limit.

**Passport mismatch:** the Hilbert-space identification assumes RH; it cannot
serve as an unconditional propagation lemma.

### LIT-W6 -- canonical chains from unimodular functions
(`IMPORTED`, known)

[Suzuki, AIF 75 (2025), DOI 10.5802/aif.3705](https://doi.org/10.5802/aif.3705)
constructs RKHS/canonical-system chains from a unimodular function under
explicit analytic hypotheses and gives a conditional inverse construction
for the Hamiltonian.

**Passport mismatch:** inner/Hermite--Biehler positivity is an input to the
chain. The theorem transports an existing positive structure; it does not
bootstrap the zeta source from one supported window.

### LIT-W7 -- Connes--van Suijlekom real-zero theorem
(`IMPORTED`, known)

[Connes--van Suijlekom, arXiv:2511.23257, Theorem 6.1](https://arxiv.org/abs/2511.23257)
states: if the quadratic form from a real distribution on `[0,L]` defines a
lower-bounded essentially self-adjoint operator, and its spectral minimum is
a simple isolated eigenvalue with an even eigenfunction `xi`, then every zero
of the entire Fourier transform `xi-hat` is real.

**Passport mismatch:** lower boundedness, a simple isolated ground state, and
evenness are hypotheses. The conclusion is real-zero rigidity for the ground
transform, not positivity of the next support or identification with zeta.

### LIT-W8 -- Connes--Consani--Moscovici finite determinants
(`IMPORTED`, known)

[Connes--Consani--Moscovici, arXiv:2511.22755](https://arxiv.org/abs/2511.22755)
prove:

- the localized semilocal Weil form is lower-semicontinuous and closed;
- the associated operator `A_lambda` has discrete lower-bounded spectrum
  (Theorem 3.6), hence a ground state (Corollary 3.7);
- if the decreasing ground floor tends to zero as `lambda->infinity`, RH
  follows (Corollary 3.8);
- for a finite Galerkin truncation with simple even lowest eigenvector `xi`,
  a self-adjoint rank-one perturbation has

  \[
  \det_{\rm reg}(D_{\log}^{(\lambda,N)}-z)
  =-i\lambda^{-iz}\widehat\xi(z),
  \]

  and all zeros of `xi-hat` are real (Theorem 5.10).

The paper explicitly identifies two missing steps: uniform simple-even
control and convergence/identification of the ground transforms with the
Riemann Xi function.

**Passport fit:** valuable cutoff/Friedrichs and finite characteristic
machinery. **Missing:** the global identification is the theorem, not a
formal consequence of self-adjointness.

### LIT-W9 -- Groskin's exact finite dictionary and tail order
(`IMPORTED`, recent and useful)

[Groskin, arXiv:2607.02828v3](https://arxiv.org/abs/2607.02828v3), archived
at [Zenodo DOI 10.5281/zenodo.21124802](https://doi.org/10.5281/zenodo.21124802),
proves at fixed prime cutoff `c>1` and Galerkin band `N`:

- **Corollary 2.4:** finite signed sources act through exactly `2N+1`
  moments, and the resulting source-to-matrix map is injective on those
  coordinates;
- **Theorem 2.5:** every real even Galerkin vector `v` determines an explicit
  admissible, band-limited Guinand--Weil test function `g_v` with

  \[
  \langle v,Q_\infty v\rangle
  =\sum_{z:\,\zeta(1/2+iz)=0}^{*}g_v(z);
  \]

- **Corollary 2.7:** a pole-neutral subfamily survives with explicitly
  controlled dimension;
- **Theorem 3.2 / Corollary 3.3:** after the Galerkin band, the omitted
  archimedean increment is positive definite and strictly totally positive,
  and

  \[
  \lambda_j(Q_T)<\lambda_j(Q_\infty)
  \le\lambda_j(Q_T)+B_T,
  \]
  \[
  B_T=\frac{(2N+1)\rho}{\pi^2T}
  \left(\log\frac{T}{2\pi}+1\right)(1+o(1)),
  \qquad \rho=\frac{2\pi}{\log c}.
  \]

The paper ships exact, interval-Arb, checksum, and three-route artifacts.

**Passport fit:** excellent for finite certification, source retention, and
cutoff budgeting. **Missing:** it maps each finite vector to a finite test and
does not compare adjacent supports or prove cofinal positivity.

### LIT-W10 -- local positive-definite extension is non-identifying
(`IMPORTED`, new method-killer for the repo)

[Jorgensen--Niedzialomski, arXiv:1212.3047](https://arxiv.org/abs/1212.3047)
prove that a continuous positive-definite function on `Omega-Omega` extends
to all of `R^n` iff the associated symmetric derivative operators admit
strongly commuting self-adjoint extensions (Theorem 1.6). In one dimension,
Krein's theorem gives existence for every bounded interval; extensions need
not be unique. Their Section 7 characterizes the family and uniqueness.

**Project consequence:** abstract local-to-global extension cannot be the
missing adjacent-support theorem. A locally positive zeta kernel always has
some positive global completion, even if the actual globally defined zeta
continuation is not that completion. A useful theorem must prove uniqueness
under an arithmetic/source constraint or directly control the actual zeta
cross block.

### LIT-W11 -- local conductor and archimedean positivity
(`IMPORTED`, known)

- Burnol identifies all local explicit-formula terms with the conductor
  operator `log|x|+log|y|` and checks Weil positivity under a support
  condition: [arXiv:math/0101068](https://arxiv.org/abs/math/0101068),
  [DOI 10.1016/S0764-4442(00)01687-6](https://doi.org/10.1016/S0764-4442%2800%2901687-6).
- Connes--Consani prove the single archimedean-place positivity mechanism via
  compressed scaling, prolate functions, and Hermitian Toeplitz matrices:
  [arXiv:2006.13771](https://arxiv.org/abs/2006.13771),
  [DOI 10.1007/s00029-021-00689-4](https://doi.org/10.1007/s00029-021-00689-4).
- Their finite-place ratios are only quasi-inner after combination with the
  archimedean factor; the associated Hankel off-diagonal is compact, not zero:
  [arXiv:2008.10974](https://arxiv.org/abs/2008.10974).

**Passport mismatch:** these explain individual/local or archimedean
positivity and compact defects. They do not prove positivity after adding the
next finite prime contribution.

## 5. What is genuinely new to this repository audit

| Item | Novelty relative to checked repo ledger | Effect |
|---|---|---|
| Chuk `a=0.8`, `L_program=3.2` claim | new | potentially much larger local seed, pending independent interval reproduction |
| exact Chuk normalization and `p=5` distance | new | prevents a factor-two/four import error; shows next activation is only `0.01888` away |
| Chuk form-domain defect | new | theorem should be restated on `H_log` or as an extended closed form |
| limited scope of Chuk barrier | new | rules out only constant absolute comb envelopes, not all pointwise-symbol splits |
| Suzuki v2 limit target | new version correction | makes `STAGE3-DETERMINANT-LIMIT.md` stale; global convergence still open |
| Krein/Jorgensen extension nonuniqueness | new route-level framing | kills “some PD extension” as a propagation strategy |
| Yang--Yang global-`ell_1` / cell-`ell_1` collision | new decisive hostile finding | invalidates its alleged `HL*(4)` truncation and headline proof |
| Groskin finite dictionary/tail | already present, now passported exactly | supports certification, not propagation |

## 6. Route reframe and next experiments

The literature collapses the credible Weil-side search to two related but
distinct programs.

### Route A -- actual-source adjacent Schur control

At a support event, decompose the new localized form into old, cross, and new
blocks and prove an inequality of the form

\[
C_{a,\delta}^*Q_a^{-1}C_{a,\delta}
\preceq N_{a,\delta}
\]

or a relative variant that remains meaningful as the old floor collapses.
The theorem must exploit the exact new prime-power atom and archimedean
source; a norm bound using only total prime mass is too expensive. The first
focused case after a certified Chuk reproduction is the `p=5` event at
`L_program=2 log 5`, not a generic large-support theorem.

### Route B -- source-identifying continuation

Use the exact finite source quotient (Groskin), screw/Friedrichs realization
(Suzuki), and canonical/Toeplitz/Hankel structure to seek a uniqueness theorem:

```text
local positive kernel
+ exact completed-zeta source coordinates
+ compatible support nesting / differential-convolution law
    => the only global PD extension is the actual zeta continuation.
```

Krein's theorem says existence alone is vacuous; the new content must be
arithmetic uniqueness. A fail-fast finite test is to compute the dimension of
positive source-coordinate completions across one activation and see whether
the zeta continuation is exposed or lies in a positive-dimensional face.

### Immediate order of work

1. Independently reproduce Chuk's `L=0.8` theorem with cutoff-free interval
   arithmetic, a serialized matrix, explicit quadrature/tail balls, and the
   correct logarithmic form domain.
2. If it passes, promote only the local seed. Do not infer propagation.
3. Attack the adjacent `p=5` source event with a relative Schur complement,
   preserving the exact source coordinates.
4. In parallel, formulate a finite uniqueness/exposed-face falsifier for the
   source-identifying route using Groskin's `2N+1` quotient.
5. Treat Suzuki/CCM real-zero characteristic functions as a separate global
   identification route; update all work to Suzuki v2 before further tests.

No surveyed theorem licenses a percentage-of-RH claim or any promotion of a
small/fixed local support result to global Weil positivity.
