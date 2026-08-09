# Direct cutoff-complete two-shift gate

Status: exact block formula, analytic fail-fast audit, and complete finite
diagnostics; 2026-08-06.  The simple sign and leading-one shortcuts are
closed.  A fixed-exponent completed correlation estimate remains open.  This
note does **not** prove a new zero-free region or the Riemann Hypothesis.

## 1. Verdict

The full R71 energy has an exact two-frequency representation which retains
the grouped Vaughan coefficient, every unequal total product, the complete
Type-I center, and the Euler-evaluation defect.  It identifies the honest
arithmetic target, but it does not manufacture a bound.

Write

```text
E_I=D_I+X_I,                                               (1.1)
```

where `D_I` is the atomic grouped-tail diagonal and `X_I` contains every
unequal-product and center term.  The diagonal satisfies

```text
D_I=exp(o(R))                                             (1.2)
```

on every regular block.  Hence the weakest useful one-sided estimate is

```text
X_I<=exp(epsilon R)                                      (1.3)
```

for every positive `epsilon`.  Its lower side is automatic from positivity:
`X_I>=-D_I`.

This is the reality check.  Since the omitted diagonal is already
subexponential, (1.3) is exponentially equivalent to bounding the complete
energy.  For the fixed-window energy it is exactly P4/RH in off-diagonal
coordinates.  For the growing-order fixed-step schedule, the same conclusion
depends on the still-open R71 blockwise converse.  The Euler-trace audit is
now discharged by the classical-synthesis lemma in
[`publication/IMPORTED-ANALYTIC-BASELINE.md`](../publication/IMPORTED-ANALYTIC-BASELINE.md).

Four natural cheaper claims fail simultaneously in complete finite models:

1. `X_I<=0`;
2. `abs(X_I)<=D_I`;
3. the corresponding terminal-covariance inequalities; and
4. the same sign and leading-one inequalities on a genuine low-frequency
   band.

The honest graduated milestone is instead

```text
X_I<=exp((1-2eta+o(1))R),       0<eta<1/2 fixed.          (1.4)
```

After the fixed-window energy theorem, (1.4) yields the genuine zero-free
strip `Delta<=1/2-eta`.  It is not RH unless one can take every
`eta<1/2`.  This fixed-exponent version is the correct first target for a new
two-shift method.

## 2. Exact cutoff-complete field

Freeze the cutoff pair `U,V` on one regular logarithmic block `I`.  Put

```text
a_(U,V)=mu_(>U)*Lambda_(>V)*1,
h_(U,V)=mu_(<=U)*log+Lambda_(<=V)
         -mu_(<=U)*Lambda_(<=V)*1.                        (2.1)
```

Vaughan's identity is the coefficientwise completion

```text
a_(U,V)+h_(U,V)=Lambda.                                  (2.2)
```

Let `ell=kh` and normalize the compact fixed-step window by

```text
mathcal V=W_(h,k)/norm(W_(h,k))_2,
c_n=a_(U,V)(n)/sqrt(n).                                  (2.3)
```

Only finitely many products can meet the block.  Their safe Dirichlet
polynomial is

```text
A_I(t)=sum_(log n in I-supp(mathcal V)) c_n n^(-it).      (2.4)
```

This finite polynomial, not analytic continuation of the infinite
coefficient series, is the two-shift object below.

The coboundary center has the exact form

```text
z(R)=exp(R/2)(alpha+beta R)/norm(W_(h,k))_2,              (2.5)

alpha=(exp(ell/2)-1)(J_0-Q)-exp(ell/2)P ell,
beta =-(exp(ell/2)-1)P.                                  (2.6)
```

The critical-value constant `I_0` cancels.  Thus the completed block field is

```text
G_I(R)=sum_n c_n mathcal V(R-log n)-z(R).                 (2.7)
```

No cofactor, parity sector, prime power, or center term has been separated
before forming this field.

## 3. Exact two-frequency formula

Let `psi>=0` be an admissible smooth block weight: `0<=psi<=1`, supported
on one regular frozen-cutoff block, equal to one on a comparable core, and
with only subexponential derivative losses.  This normalization prevents a
rescaling of `psi` from changing the proposed estimate.  Use

```text
fhat(t)=integral_R f(R)exp(-itR)dR.                       (3.1)
```

Then

```text
E_psi(G_I)=integral psi(R)abs(G_I(R))^2dR                 (3.2)
```

is exactly

```text
1/(2pi)^2 double_integral
  psihat(u-t) Vhat(t)conjugate(Vhat(u))
  A_I(t)conjugate(A_I(u)) dt du

-1/pi Re integral
  Vhat(t)A_I(t)conjugate((psi z)^hat(t))dt

+integral psi(R)abs(z(R))^2dR.                           (3.3)
```

Formula (3.3) is genuinely two-shift: the block multiplier
`psihat(u-t)` couples a continuum of `t,u`, while the last two lines retain
the complete center.

The center transforms are elementary.  Put

```text
J_psi(lambda)=integral psi(R)exp(lambda R)dR.             (3.4)
```

Then

```text
(psi z)^hat(t)
 =[alpha J_psi(1/2-it)+beta J_psi'(1/2-it)]
   /norm(W_(h,k))_2,                                     (3.5)

integral psi abs(z)^2
 =[alpha^2 J_psi(1)+2alpha beta J_psi'(1)
   +beta^2 J_psi''(1)]/norm(W_(h,k))_2^2.                (3.6)
```

For `Re(s)>1`, the untruncated tail series factors as

```text
sum_n a_(U,V)(n)n^(-s)
 =(1-zeta(s)M_U(s))[-zeta'(s)/zeta(s)-L_V(s)].            (3.7)
```

Using (3.7) directly at `Re(s)=1/2` is inadmissible: its zero poles are the
carrier that (3.3) is meant to bound.

## 4. Exact completion and Euler defect

Define the signed Type-I evaluation defect by

```text
epsilon(R)
 =mathcal L_R(h_(U,V))-[I_pol(R)+I_0].                   (4.1)
```

If `D_I^full` denotes the normalized complete von Mangoldt coboundary, then

```text
D_I^full=G_I+e_I,
e_I(R)=[epsilon(R+ell)-epsilon(R)]/norm(W_(h,k))_2.       (4.2)
```

Consequently the full energy has the exact completion

```text
E_psi(D_I^full)=E_psi(G_I)
 +2 Re integral psi G_I conjugate(e_I)+E_psi(e_I),        (4.3)
```

and in particular

```text
abs(sqrt(E_psi(D_I^full))-sqrt(E_psi(G_I)))
 <=norm(sqrt(psi)e_I)_2.                                 (4.4)
```

For `U=V=x^(1/2-c/k)`, periodic Euler summation proves, up to polynomial
normalization,

```text
norm(e_I)_infinity
 <=exp(-(2c-1/2)R+O_h(k^2+k log k)).                     (4.5)
```

Thus `k^2=o(R)` makes the defect negligible at exponential scale.  The
uniform constant and support ledger are proved in Section 9 of
[`FULL-FIELD-VK-SUBPOWER-BOUND.md`](FULL-FIELD-VK-SUBPOWER-BOUND.md).

To keep frozen cutoffs inside the `1/2+O(1/k)` collar, take blocks of length
`O(R/k)`.  A dyadic logarithmic interval then needs only `O(k)` blocks, a
subexponential count.

## 5. Why the diagonal is harmless

Define

```text
D_I=sum_n abs(c_n)^2
  integral psi(R)abs(mathcal V(R-log n))^2dR.             (5.1)
```

The elementary divisor bound

```text
abs(a_(U,V)(n))<=tau_3(n)log n                           (5.2)
```

and standard divisor-sum estimates give (1.2).  Let `X_I` be all the terms
in (3.3) except (5.1).  Then

```text
E_psi(G_I)=D_I+X_I,
X_I>=-D_I.                                               (5.3)
```

For the proved fixed-window energy law, subtracting (5.1) does not change
the exponential width carrier.  In particular, the positive part of `X_I`
has the same positive exponential rate as the full energy whenever
`Delta>0`.  Therefore calling (1.3) an “off-diagonal estimate” does not make
it weaker than RH.

A comparison of the form

```text
E_psi(G_I)<=R^A[1+D_I]                                  (5.4)
```

would be a clean, strong version of (1.3).  The additive `1` is necessary:
near activation of a tail profile, `D_I` can approach zero while the smooth
center energy remains nonzero.  No universal estimate `E_I<=C D_I` can hold
on all finite blocks.

## 6. Analytic fail-fast gates

### 6.1 The Ward value lies outside the faithful frequency scale

At a distinct semiprime, the ratio-twisted connected coefficient is

```text
2log(p)log(q)cos(t log(p/q)).                             (6.1)
```

The ordinary Ward coefficient is its value at `t=0`.  Edge pairs in the
near-square collar have

```text
abs(log(p/q)) asymp R/k.                                 (6.2)
```

Keeping (6.1) in one positive lobe would require `abs(t)<<k/R`.  But the
compact B-spline multiplier is still of full exponential strength at
`abs(t)~1/k` (indeed its natural central bandwidth is larger).  The faithful
schedule has `k^2=o(R)`, hence

```text
1/k >> k/R.                                              (6.3)
```

The relevant band necessarily crosses many factor-ratio phase changes.
Replacing the twist by `t=0`, or by a uniformly positive small-`t` Taylor
term, is incompatible with the schedule that preserves an off-line mode.

### 6.2 A coefficient-blind large sieve pays an exponential spacing loss

For `n~X`, adjacent frequencies `log n` are separated by `asymp 1/X`.
The Montgomery--Vaughan Hilbert/mean-value bound therefore carries a term of
size `X` when the `t` interval is short.  The fixed-step passband is short and
even narrows with `k`; it cannot diagonalize exponentially many adjacent log
frequencies.  Near-square bilinearization can reduce the generic loss only to
the square-root scale, still exponential in `R`.

This is a structural mismatch, not a missing optimization.  A successful
bound must use the actual Mobius coefficient and center jointly.  The
classical Hilbert-inequality source is Montgomery--Vaughan,
<https://doi.org/10.1112/jlms/s2-8.1.73>.

### 6.3 Sectorwise absolute values are exponentially too large

The central semiprime assignments have the same sign.  Their `L1` amplitude
on one regular block is of square-root-exponential size before the Type-I
center is restored.  Squaring separate cofactor, semiprime, dyadic, or center
sectors therefore loses an exponential factor.  Completion must occur at the
field level in (2.7), not after a norm estimate.

### 6.4 Hardy, de Branges, and scattering positivity are endpoint proxies

For

```text
E_sigma(z)=xi(1/2+sigma-iz),                              (6.4)
```

Hermite--Biehler/Schur positivity excludes exactly the zeros whose horizontal
displacement exceeds `sigma`.  Taking `sigma=c/k` to zero is RH, not weaker
scaffolding.  Boundary unitarity alone is blind to a symmetric all-pass
factor carrying an off-axis pole.

The most interesting exotic attempt is to realize (3.3) as a mixed parameter
derivative of a truncated Eisenstein family and apply the Maass--Selberg
inner-product relation.  It fails two immediate gates:

1. the standard symmetric divisor twist has zero first parameter derivative
   at the central parameter and its second derivative measures divisor-ratio
   squares; it does not reproduce the hard coefficient
   `mu_(>U)*Lambda_(>V)*1` at `pq` and `p^2`;
2. Maass--Selberg positivity uses unitary scattering, which is compatible
   with off-axis resonances.  An additional Hardy/causal orientation would
   return to (6.4).

Thus Arthur truncation is an interesting identity dictionary, but not yet an
estimate mechanism.  A conventional example of Maass--Selberg truncation in
an arithmetic estimate is <https://arxiv.org/abs/1602.07256>.

### 6.5 Probabilistic and graph lifts lose the completion

Independent prime-geometric ensembles have positive Fisher-information and
Stein identities, and squarefree occupancy laws suggest negatively dependent
models.  Hard logarithmic-mass conditioning plus Mobius parity destroys that
positive product measure.  Restoring it canonically inserts `zeta` or
`1/zeta`, as in R67--R68.

A divisor-hypergraph or nonbacktracking lift faces the same boundary.  Fiber
chains do not couple unequal total products, while adding scale edges leaves
the approximate characters `n^(it)` with eigenvalue near one.  A uniform
conditioned spectral gap would be a valid new theorem, but after completion
it is already (1.3).

Logarithmically averaged two-point Chowla does not directly supply the needed
input: it treats fixed affine shifts of a bounded multiplicative function,
whereas (3.3) has moving multiplicative ratios, von Mangoldt weights, a hard
Vaughan cutoff, and an explicit rank-two center.  The comparison theorem is
<https://arxiv.org/abs/1509.05422>.

## 7. Complete finite gate

The diagnostic
[`src/r71_two_shift_bound_probe.py`](../src/r71_two_shift_bound_probe.py)
uses the cutoff-complete B-spline/Vaughan field and tests raw energy,
terminal covariance, retained energy, and completed low-frequency modes.

The smallest simultaneous counterexample in the documented integer/step
grid is

```text
X=59, Y=4=floor(X^(3/8)), h=0.04, j=m=1.                 (7.1)
```

The active grouped products are exactly `55,56,60`, and the central
semiprime is `55=5*11`.  For raw block energy,

```text
D                 0.00519612453160
unequal products +0.00170851298560
center completion +0.00501854282240
X_I              +0.00672705580800
E_I               0.0119231803396
X_I/D             1.29462944.                             (7.2)
```

The corresponding remainder ratios are

```text
terminal covariance   X_I/D=1.19672208,
retained zero mode     X_I/D=1.45315920.                  (7.3)
```

At frequencies `0,0.25,0.5,1`, the completed spectral remainder ratios are
approximately

```text
1.453159, 1.453175, 1.453222, 1.453410.                  (7.4)
```

Thus the low-band failure is not confined to one point.  Larger and
higher-order configurations reproduce it.  Near activation, ratios can be
much larger: `X=127,Y=6,h=0.03` has retained energy/diagonal about `13.4`,
and `X=128,Y=6,h=0.02` has about `94.8`.  These large ratios arise as the
tail diagonal becomes small while the center remains active; the absolute
energies remain small.

The signs and all decompositions are stable under Gaussian quadrature orders
`8` through `24`.  These are D-rated floating diagnostics, not interval
certificates or asymptotic evidence.  They close sign, leading-one,
diagonal-only, and pointwise low-band shortcuts.  They do not refute (1.3),
(1.4), (5.4), long-block averaging, or a Mobius-specific theorem.

Focused tests are in
[`src/test_r71_two_shift_bound_probe.py`](../src/test_r71_two_shift_bound_probe.py).

## 8. Surviving research target

The branch remains alive, but only in a deliberately narrow form.

1. Work with the finite polynomial (2.4) and the exact center (3.5)--(3.6).
   Do not use the critical-line continuation of (3.7).
2. Target the fixed-exponent milestone (1.4) first.  Even one positive
   `eta` would prove a new fixed zero-free strip and would validate the
   cancellation architecture before attempting RH scale.
3. Permit a polynomial or `exp(o(R))` loss and include `1+D_I`; constant-one
   diagonal domination is false.
4. Average over regular blocks of length `O(R/k)`.  Pointwise microblock
   signs are false, while `O(k)` blocks still preserve the exponent.
5. Any proposed input must control the Mobius-specific ratio twist jointly
   with the explicit center.  A theorem for separate sectors, untwisted Ward
   coefficients, or arbitrary coefficient vectors has already failed the
   appropriate gate.
6. In the growing-order route, finish the blockwise off-line isolation before
   calling a subexponential prime-side estimate an RH equivalence.  The R71
   Euler trace is an imported lemma, not part of this open gate.

The sharp next lemma is therefore:

```text
For one fixed `0<eta<1/2`, uniformly on every regular frozen-cutoff block
and its admissible weights,

X_I<=exp((1-2eta+o(1))R),                                (8.1)

with X_I defined by the complete formula (3.3) minus only the atomic
diagonal (5.1).
```

This is neither a sign conjecture nor a generic large-sieve bound.  It is a
direct, cutoff-complete, two-shift arithmetic correlation theorem.  Failure
of a proposed proof engine should be measured against (8.1), not mistaken
for failure of the statement itself.

The subsequent coefficient-specific attack is
[`MOBIUS-TWO-SHIFT-RENORMALIZATION-GATE.md`](MOBIUS-TWO-SHIFT-RENORMALIZATION-GATE.md).
It closes local cutoff martingales and the nonlinear Selberg--Riccati
recursion, improves the unconditional fixed-step calibration, and leaves
only the genuinely global estimate (8.1).
