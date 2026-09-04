# R124 actual `Q_h` primitive Mellin sign gate

Status: the rigorously established sign information is one-sided.  At every
integer ratio the periodized kernel is an exact positive Gram square, so
every nondegenerate actual `Q_h` block has a strictly positive
near-diagonal Mellin band and no low-frequency spectral gap.  On a complete
comparable-ratio shell, floating B-spline diagnostics exhibit robust
positive and negative bands, but those computations have not been upgraded
to interval or symbolic certification.  The primitive block also has the
exact Mobius-weighted representation from R120; that representation does
not by itself prove that the actual quadratic form takes both signs.
Thus the diagnostic is not a certified negative spectral witness.
Accordingly no positive-energy comparison is known for the isolated packet,
and no fixed zero-free strip is proved or disproved.

Date: 2026-08-07.

**2026-09-02 successor correction (R128/S0 audit).**  R128 subsequently
performed the all-arity, all-conductor comparison exactly: the putative
remainder cancels rather than merely being small.  What remains is precisely
the original full positive R71 energy.  This closes the comparison question
posed in Sections 6--7, but it does not supply an upper bound.  The isolated
primitive profile is therefore not a proved standalone global surrogate for
the positive energy.  Earlier wording in this report that called its
full-shell spectral sign a theorem is withdrawn: that assertion is only a
D-rated numerical diagnostic unless an interval certificate is supplied.

Predecessors:

* [`R120-PRIMITIVE-MOBIUS-MELLIN-KERNEL-GATE.md`](R120-PRIMITIVE-MOBIUS-MELLIN-KERNEL-GATE.md)
  for the inverse-Poisson formula and signed-coefficient Mellin
  diagonalization;
* [`R116-SIGNED-JOINT-TYPEII-ATTACK.md`](R116-SIGNED-JOINT-TYPEII-ATTACK.md)
  for the proper-conductor square-root theorem on balanced semiprimes; and
* [`R102-CENTER-ANNIHILATED-OFF-AXIS-GATE.md`](R102-CENTER-ANNIHILATED-OFF-AXIS-GATE.md)
  for the actual three-translate `Q_h` window and its zero response.

The reproducible floating diagnostic is
[`r124_actual_qh_primitive_mellin_probe.py`](../src/r124_actual_qh_primitive_mellin_probe.py),
with regression tests in
[`test_r124_actual_qh_primitive_mellin_probe.py`](../src/test_r124_actual_qh_primitive_mellin_probe.py).

## 1. Verdict

For the real actual window put

```text
f_R(t)=t^(-1/2)V_Q(R-log t),
L(t,u)=int psi(R)f_R(t)f_R(u)dR,                       (1.1)

Phi(x)=sum_(nu,ell in Z)L(ell-nu x,nu).               (1.2)
```

The sum is locally finite.  The exact sign facts are

```text
Phi(x+1)=Phi(x),
int_0^1 Phi(x)dx=0,

Phi(j)=int psi(R)abs[sum_(n>=1)f_R(n)]^2dR>=0
                                      for every j in Z. (1.3)
```

On every active nondegenerate block the last quantity is strictly positive.
Thus `Phi` is positive at the integer-ratio diagonal and, because its
additive mean is zero, negative somewhere else in each period.

For a real even fixed-ratio shell cutoff `chi(u)`, the actual Hermitian
kernel and multiplier are

```text
k_H(u)=chi(u)/2 [exp(-u/2)Phi(exp u)
                  +exp(u/2)Phi(exp(-u))],             (1.4)

lambda_P(tau)=int_R k_H(u)cos(tau u)du.               (1.5)
```

There are three conclusions.

1. A sufficiently narrow shell about `u=0` has

   ```text
   lambda_P(tau)>0
   ```

   on a nonempty interval about `tau=0`.  Hence the actual primitive
   spectrum has no forced low-frequency gap.
2. On the whole comparable shell `1/2<=n/c<=2`, floating evaluations of
   `lambda_P` change sign for the tested B-spline profiles.  Its sampled
   zero-frequency sign also varies with the permitted B-spline order and
   `Q_h` step.  There is no certified parameter-uniform primitive sign
   theorem.
3. Even on a frequency interval where `lambda_P>=0`, the `g=1`
   coprimality projector gives

   ```text
   sum_d mu(d)abs B_d(tau)^2,                          (1.6)
   ```

   so positivity is not manifest term by term.  This identity alone does
   not prove that the constrained actual form is indefinite.

The proved facts delimit, but do not close, the sign route:

```text
near-diagonal primitive low mode                  POSITIVE / NONZERO;
full-shell primitive spectral weight              BOTH SIGNS NUMERICALLY;
coprimality representation                        SIGNED COEFFICIENTS;
all-conductor completed kernel                    POSITIVE;
proper conductor global square-root comparison    NOT PROVED;
fixed strip                                        STILL OPEN.          (1.7)
```

## 2. Exact integer-ratio Gram theorem

### Theorem 2.1

Let `V_Q` be the real R102 window, let `psi>=0`, and let `L,Phi` be
(1.1)--(1.2).  Then for every integer `j`,

```text
Phi(j)=int psi(R)abs S_Q(R)^2dR,
S_Q(R)=sum_(n>=1)n^(-1/2)V_Q(R-log n).                (2.1)
```

In particular `Phi(j)>=0`.  If `S_Q` is not identically zero on the
positive-measure support of `psi`, then `Phi(j)>0`.

### Proof

At an integer `j`, put `k=ell-nu j`.  For each fixed positive integer
`nu`, translation by `nu j` is a bijection of `Z`, so

```text
Phi(j)=sum_(nu,k in Z)L(k,nu).                         (2.2)
```

The physical support is bounded away from zero, hence only `k,nu>=1`
remain.  Insert the Gram formula (1.1) and interchange the finite sums:

```text
Phi(j)
 =int psi(R)[sum_k f_R(k)][sum_nu f_R(nu)]dR
 =int psi(R)abs[sum_n f_R(n)]^2dR.                    (2.3)
```

This proves the theorem.  QED.

The strict nondegeneracy is the correct hypothesis.  It can fail on a
deliberately inactive cofactor block containing no physical samples, and a
particular cell should be checked rather than declared nondegenerate by
terminology alone.  It holds for the standard R105/R116 profile evaluated
in Section 4.  More invariantly, `S_Q` cannot vanish on every output
interval: its Laplace transform would make the nonzero compact multiplier
of `V_Q` annihilate the integer Dirichlet series identically.  If one
isolated cell vanishes, the translation/dilation bank still contains
nonzero cells; no assertion about the immediately adjacent cell is needed.

### Corollary 2.2 (positive actual low Mellin band)

Assume `Phi(1)>0`.  By continuity there is `epsilon_0>0` such that the
untruncated Hermitian kernel in (1.4) is positive for
`abs(u)<epsilon_0`.  Let `chi_epsilon` be any nonzero even nonnegative
cutoff supported there, with `epsilon<epsilon_0`.  Then

```text
lambda_(P,epsilon)(tau)>0
       whenever abs(tau)epsilon<pi/2.                 (2.4)
```

Indeed every factor in

```text
int chi_epsilon(u)k_H(u)cos(tau u)du                  (2.5)
```

is then nonnegative and is positive on a set of positive measure.  This is
an analytic, actual-window positive witness.  It uses no generic-profile
countermodel and no floating calculation.

Keeping all fixed-ratio shells does not remove the witness.  A partition
of unity retains this near-diagonal member and adds the other shell
members.  The scalar sum can cancel it, but there is no identity which
makes the member itself zero.

## 3. Why the full-shell multiplier has no forced sign

R120 proved the exact inverse formula

```text
Phi(x)=sum_(nu,ell)L(ell-nu x,nu)                     (3.1)
```

and the additive coboundary identity.  If `Psi'=Phi` is the periodic
zero-mean primitive, then

```text
exp(-u/2)Phi(exp u)
 =d/du[exp(-3u/2)Psi(exp u)]
  +(3/2)exp(-3u/2)Psi(exp u).                         (3.2)
```

After all shell cutoffs are added, their internal boundary terms cancel,
but the second term in (3.2) remains.  Hence the additive `Q_h` nullity does
not impose `lambda_P(0)=0` or an odd/antisymmetric Mellin kernel.

There is also a sharp positivity test.  If

```text
lambda_P(tau)>=0 for every tau,                       (3.3)
```

then Fourier inversion makes `k_H` positive definite.  Every two-by-two
principal minor must be nonnegative, so

```text
abs k_H(u)<=k_H(0)                                    (3.4)
```

for all `u`.  The floating diagnostic below violates (3.4) by a factor
about `6.50`, strong evidence that a globally nonnegative multiplier is
incompatible with the sampled kernel.  It is not an independent rigorous
certificate, because neither that inequality nor the cosine-transform
values are enclosed by validated intervals.

Pointwise sign change of `Phi` alone would not prove spectral sign change;
a positive-definite function may be negative at some points.  Criterion
(3.4) and the direct transform are therefore both recorded.

## 4. Actual fixed-step B-spline diagnostic

The probe uses exactly

```text
V(x)=Phi_(a,k)(x+ka)-Phi_(a,k)(x),

V_Q(x)=V(x+2h)-2exp(h/2)V(x+h)+exp(h)V(x),             (4.1)
```

the polynomial output localizer

```text
psi(R) proportional to (1-(R/B)^2)^2_+,
```

and all ratios `1/2<=x<=2`.  It forms (1.1)--(1.5)
directly; no arithmetic coefficients are sampled.  With

```text
a=0.2, k=4, h=0.2, B=0.03,                            (4.2)
```

the `1001`, `2001`, and `4001` ratio-node runs give respectively

```text
lambda_P(0)       0.0041023794   0.0041022702   0.0041022429;
min near tau=22.6  -0.041154567   -0.041154442   -0.041154410;
max near tau=12.8   0.054424745    0.054424952    0.054425004. (4.3)
```

The independent exact-normalization check is

```text
Phi(1)=integer Gram=0.0258067307011,                  (4.4)
```

to displayed precision.  Moreover

```text
max_u abs k_H(u)/k_H(0)=6.4968...,                    (4.5)
```

so (3.4) fails with a large margin.  The sampled sign changes lie in

```text
(1.2,1.4), (7.2,7.4), (18.6,18.8).                   (4.6)
```

The probe uses the rectangular outer ratio shell.  Replacing its indicator
by a smooth cutoff changes every sampled multiplier by at most

```text
norm[(chi_smooth-chi_rect)k_H]_1.                     (4.6a)
```

Smooth cutoffs arbitrarily close in this norm are legal, while the two
sampled sign margins in (4.3) are about `0.04` and `0.05`.  Conditional on
an interval or symbolic validation of those margins, continuity would give
a genuine smooth fixed-ratio partition with both signs.  Until then, this
only says that smoothing would preserve a *certified* margin; it does not
upgrade the present floating calculation into a sign theorem.

Other sampled legal actual profiles indicate that even `lambda_P(0)` may
have no fixed sign:

```text
(a,k,h)          Phi(1)       lambda(0)      min lambda     max lambda
(0.2,4,0.3)      0.244761      0.0236315      -0.0403741     0.0867192
(0.1,8,0.2)      0.00777302   -0.0322878      -0.0815385     0.0907176
(0.04,1,0.08)    0.996352     -0.00502137     -0.0465268     0.134284.
                                                               (4.7)
```

All displayed profiles use a genuine positive-width output localizer.  The
table is a D-rated numerical sign audit, not an interval proof.  The exact
positive statement is Theorem 2.1/Corollary 2.2; the numerical margins only
provide evidence against a universal full-shell sign conjecture.

The regression command is

```text
python3 src/test_r124_actual_qh_primitive_mellin_probe.py
```

and currently passes all three tests.

## 5. Coprimality obstructs manifest positivity even on positive bands

After exact two-sided Vaughan recompletion, set

```text
C(n)=-mu(n)log n,
b_X(n)=C(n)n^(-1/2)w(n/X).                            (5.1)
```

For the unrestricted ordered pair, (1.5) diagonalizes as

```text
1/(2pi)int lambda_P(tau)
 abs[sum_n b_X(n)n^(i tau)]^2d tau.                   (5.2)
```

The actual `g=1` primitive block has `(c,n)=1`.  Mobius inversion gives
R120's exact formula

```text
1/(2pi)int lambda_P(tau)
 sum_(d>=1)mu(d)abs[sum_a b_X(da)a^(i tau)]^2d tau.   (5.3)
```

Thus Corollary 2.2 does not prove the arithmetic form positive: the
common-divisor sieve has its own signed spectral coefficients.  Summing every
exact gcd sector removes this second sign only if their scaled kernels are
identical.  In R81 they depend on `g` through `L(u+gj,u)`, so all
fixed-ratio/g profiles must first be retained.

If a negative band indicated by (4.3) is interval- or symbolically
certified, it cannot simply be discarded when seeking an upper bound.
Positivity of the complete reconstructed Gram kernel would then require
aggregate compensation from the other primitive profiles and
proper-conductor terms; the present floating diagnostic does not locate or
certify that compensation.  Bounding only a putative positive part would
be a stronger Mertens theorem, not a free consequence of positivity.

## 6. The proper-conductor comparison and the `beta>3/4` test

There is a useful conditional sign lemma.

### Lemma 6.1

Suppose a modulation isolates a zero `rho=beta+i gamma` and an exact global
conductor decomposition has

```text
E_rho(X)=P_rho(X)+R_rho(X),

E_rho(X)=A_rho X^(2beta-1)(1+o(1)),       A_rho>0,
R_rho(X)<<X^(theta+epsilon).                          (6.1)
```

If `2beta-1>theta`, then

```text
P_rho(X)=A_rho X^(2beta-1)(1+o(1))>0.                 (6.2)
```

This is immediate from (6.1).  With `theta=1/2`, every zero with
`beta>3/4` would force a positive primitive carrier of the full expected
size.  In particular, if R116's square-root proper-conductor theorem were
global in the exact decomposition assumed by the lemma, it would remove
this isolated-carrier sign ambiguity for the near-one zeros relevant to
failure of a fixed strip.  It would not by itself supply the required
global upper bound.

The current theorem does **not** meet the global hypothesis.  R116 proves
`theta=1/2` after restricting the outer cofactor modulus to balanced
semiprimes.  That restricted principal Gram subenergy is positive, but it
is not the isolated zeta-zero carrier.  It retains a much larger uncancelled
semiprime background.

Indeed, there are `X/log^2 X` balanced distinct semiprimes `q=pr`, and

```text
C(q)/sqrt(q)asymp log X/sqrt(X).                      (6.3)
```

Their one-point field therefore has main size

```text
sqrt(X)/log X.                                        (6.4)
```

Applying `Q_h` does not make (6.4) power-small.  For example

```text
(tau_h-exp(h/2))^2 [exp(R/2)/R]
       asymp_h exp(R/2)/R^3.                          (6.5)
```

The exponential exponent remains `1/2`, so the restricted energy remains
of exponent one even on RH.  Cancellation of this background uses the
alternating signs of **all** squarefree cofactor arities in `-mu(q)log q`.
Those are exactly the moduli for which R116 has not power-saved every
near-primitive proper conductor.

Consequently one may not combine

```text
full all-conductor zero positivity
```

with

```text
balanced-semiprime proper-conductor error
```

as though they belonged to the same decomposition.  This was the historical
open comparison in this report; R128 subsequently superseded it by proving
that the complete all-class remainder is exactly zero, while the restored
object is R71.

## 7. What this means for the fixed-strip attack

The exact and numerical sign audit separates the two hoped-for easy
outcomes, but rigorously rules out only the first.

1. The primitive spectrum is not absent at low Mellin frequency.  Theorem
   2.1 gives an exact positive low-mode witness.
2. The full primitive spectrum is numerically sign-changing, but actual
   indefiniteness is not yet certified.  In either case no theorem presently
   licenses treating the isolated form as a positive Gram norm or using it
   as an order-reflecting surrogate for the complete energy.
3. Proper conductors are square-root-small on balanced semiprimes, but that
   subfamily has an uncancelled natural-size background.  The estimate does
   not transfer to the global pure-zero response.
4. Once all cofactor arities and conductor classes are restored, positivity
   is exactly the original R71 energy.  Its low-mode size is governed by
   the Mobius-log polynomials of R120.

The resulting exponent ledger is

```text
actual integer-ratio primitive value              POSITIVE GRAM;
actual narrow-shell low Mellin band               POSITIVE;
actual whole comparable-shell multiplier          BOTH SIGNS / D-RATED NUMERIC;
actual `g=1` arithmetic spectral form              SIGNED REPRESENTATION;
balanced-semiprime proper conductors               X^(1/2+epsilon);
balanced-semiprime background after Q_h            X^(1-o(1)) energy;
all-arity/all-conductor restoration (R128)           EXACT, REMAINDER ZERO;
restored global object                               ORIGINAL R71 ENERGY;
global fixed-power R71 bound                        OPEN.              (7.1)
```

The successor calculation removes the proposed comparison target: R128
already restores every class, with zero remainder, and returns R71.  The
valid next target is therefore a fixed-power upper bound for that complete
energy (or a genuinely lossless reduction of it), not another estimate for
the isolated primitive sign profile.
