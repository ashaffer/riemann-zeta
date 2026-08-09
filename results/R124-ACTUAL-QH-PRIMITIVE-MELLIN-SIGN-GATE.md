# R124 actual `Q_h` primitive Mellin sign gate

Status: the sign of the actual primitive kernel is now determined as far as
the available structure permits.  At every integer ratio its periodized
kernel is an exact positive Gram square.  Consequently every nondegenerate
actual `Q_h` block has a strictly positive near-diagonal Mellin band; there
is no low-frequency spectral gap.  On a complete comparable-ratio shell,
however, the Hermitian Mellin multiplier is not sign-definite.  Exact
fixed-step B-spline computations exhibit robust positive and negative
bands, and even the sign at zero frequency varies with legal smoothing
parameters.  The primitive block also retains the coprimality Mobius sign
from R120.  Thus neither primitive positivity nor primitive negativity gives
an upper bound.  Proper conductors cannot erase the positive band on the
balanced-semiprime scale, but their proved square-root bound is not global
enough to compare the primitive block with the isolated zeta-zero carrier.
No fixed zero-free strip is proved or disproved.

Date: 2026-08-07.

Predecessors:

* [`R120-PRIMITIVE-MOBIUS-MELLIN-KERNEL-GATE.md`](R120-PRIMITIVE-MOBIUS-MELLIN-KERNEL-GATE.md)
  for the inverse-Poisson formula and signed Mellin diagonalization;
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
2. On the whole comparable shell `1/2<=n/c<=2`, `lambda_P` changes sign for
   the tested exact B-spline profiles.  Its zero-frequency sign itself can
   be positive or negative as the permitted B-spline order and `Q_h` step
   vary.  There is no parameter-uniform primitive sign theorem.
3. Even on a frequency interval where `lambda_P>=0`, the `g=1`
   coprimality projector gives

   ```text
   sum_d mu(d)abs B_d(tau)^2,                          (1.6)
   ```

   so the arithmetic primitive form is not positive.

The sign route therefore closes as a shortcut:

```text
near-diagonal primitive low mode                  POSITIVE / NONZERO;
full-shell primitive spectral weight              SIGNED;
coprimality spectral weight                       SIGNED AGAIN;
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
of unity retains this near-diagonal member and adds the other signed
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

for all `u`.  The standard actual profile below violates (3.4) by a factor
about `6.50`, independently certifying that a globally nonnegative
multiplier is incompatible with the sampled kernel.  The direct cosine
transform locates both signs.

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

The probe uses the rectangular outer ratio shell.  This does not make the
sign conclusion a boundary artifact: replacing its indicator by a smooth
cutoff changes every sampled multiplier by at most

```text
norm[(chi_smooth-chi_rect)k_H]_1.                     (4.6a)
```

Smooth cutoffs arbitrarily close in this norm are legal, while the two sign
margins in (4.3) are about `0.04` and `0.05`.  Hence a genuine smooth
fixed-ratio partition with both signs follows by continuity.  This proves
existence of legal signed actual profiles; it does not claim that every
possible smooth partition has identical zero locations.

Other legal actual profiles show that even `lambda_P(0)` has no fixed sign:

```text
(a,k,h)          Phi(1)       lambda(0)      min lambda     max lambda
(0.2,4,0.3)      0.244761      0.0236315      -0.0403741     0.0867192
(0.1,8,0.2)      0.00777302   -0.0322878      -0.0815385     0.0907176
(0.04,1,0.08)    0.996352     -0.00502137     -0.0465268     0.134284.
                                                               (4.7)
```

All displayed profiles use a genuine positive-width output localizer.  The
table is a D-rated numerical sign audit, not an interval proof.  The exact
positive statement needed for the conclusion is Theorem 2.1/Corollary 2.2;
the numerical margins only reject a universal full-shell sign conjecture.

The regression command is

```text
python3 src/test_r124_actual_qh_primitive_mellin_probe.py
```

and currently passes all three tests.

## 5. Coprimality prevents a positivity shortcut even on positive bands

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

Thus Corollary 2.2 does not make the arithmetic form positive: the
common-divisor sieve has its own signed spectral weight.  Summing every
exact gcd sector removes this second sign only if their scaled kernels are
identical.  In R81 they depend on `g` through `L(u+gj,u)`, so all
fixed-ratio/g profiles must first be retained.

Conversely, a negative band in (4.3) cannot be discarded when seeking an
upper bound.  It is repaired by some combination of other primitive
profiles and proper-conductor terms when the full positive Gram kernel is
reconstructed.  Bounding only its positive part would be a stronger
Mertens theorem, not a free consequence of positivity.

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
global, the sign/gap route would be decisively closed for the near-one
zeros relevant to failure of a fixed strip.

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

as though they belonged to the same decomposition.  Establishing the
global remainder estimate in Lemma 6.1 would itself be major new progress.

## 7. What this means for the fixed-strip attack

The actual sign computation rules out both hoped-for easy outcomes.

1. The primitive spectrum is not absent at low Mellin frequency.  Theorem
   2.1 gives an exact positive low-mode witness.
2. The full primitive spectrum is not nonnegative, so it cannot be bounded
   above by dropping negative bands or by treating it as a Gram norm.
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
actual whole comparable-shell multiplier          BOTH SIGNS;
actual `g=1` arithmetic spectral form              BOTH SIGNS;
balanced-semiprime proper conductors               X^(1/2+epsilon);
balanced-semiprime background after Q_h            X^(1-o(1)) energy;
global all-arity proper-conductor saving            OPEN;
global fixed-power R71 bound                        OPEN.              (7.1)
```

The next valid sign-based target is therefore very specific: prove a global
operator comparison in which all cofactor arities are present and the sum
of every proper-conductor spectral correction is `O(X^(1/2+epsilon))` (or
any `O(X^(1-delta))`) **after** the pole background cancels.  Lemma 6.1
would then force primitive positivity on every near-one zero carrier.  It
would not yet give the upper bound, but it would eliminate spectral sign
cancellation as an escape.  No such global comparison is presently proved.
