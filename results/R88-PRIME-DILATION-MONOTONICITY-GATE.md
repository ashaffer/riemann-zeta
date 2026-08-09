# Prime-dilation monotonicity and the pole-annihilation gate

Status: R88 exact complete-monotonicity and prime-ray identities, two
pole-annihilation no-go theorems, and continuous and one-prime countermodels.
This route does not prove a fixed zero-free strip, and it does not prove that
no such strip exists.

## 1. Verdict

Put

```text
F(s)=-zeta'(s)/zeta(s)=sum_(n>=2) Lambda(n)n^(-s),    Re(s)>1.       (1.1)
```

The positive Laplace measure behind (1.1) has much more exact positivity than
we had used:

```text
all derivatives                         completely monotone
all forward finite differences          completely monotone
all derivative Hankel matrices           totally positive
prime-power exponent sieves              completely monotone.       (1.2)
```

None of these statements removes the pole at `s=1`.  The natural operations
which do remove it lose the positive-measure structure:

1. `(s-1)F(s)` is positive on the real axis, but is **not** completely
   monotone.  This is proved below from the atoms at `2` and `3`, without any
   unproved information about primes.
2. The aligned dilation

   ```text
   F(1+x)-aF(1+ax),                                    (1.3)
   ```

   cancels `1/x`, but for every integer `a>=2` its inverse Laplace measure
   has an explicit negative atom at `log(p^a)`.  More generally, no nonzero
   finite combination of integer dilations can both cancel the pole and have
   a nonnegative inverse measure.
3. A positive Laplace measure with a pole at `1` can hide zero-like complex
   poles of residue `-m` on `Re(s)=1-epsilon`, for every `epsilon>0`.
   The construction can even be made atomic on one genuine prime-power
   semigroup and can retain every exponent-sieve inequality.

The obstruction has a simple interpretation.  Positivity sees the dominant
`e^t` density which creates the pole at `1`.  It does not prevent a smaller
oscillation `e^((1-epsilon)t)cos(gamma t)` from being hidden underneath that
density.  Such an oscillation produces exactly a conjugate pair of
zero-residue poles at `1-epsilon +/- i gamma`.

Thus positivity, complete monotonicity, Hankel total positivity, semigroup
support, and finite prime-exponent dilation inequalities do not force any
fixed gap.  A viable successor must use the exact zeta coefficient law
`Lambda(p^k)=log p` together with cancellation **between distinct primes**.
That missing cross-prime estimate is again a fixed-power prime number
theorem input, not a free consequence of the positive cone.

## 2. The full automatic positive cone

For real `sigma>1`, let

```text
t_n=log n,
dmu(t)=sum_(n>=2)Lambda(n)delta_(t_n),
M_r(sigma)=(-1)^r F^(r)(sigma).
```

Then

```text
F(sigma)=integral_0^infinity e^(-sigma t)dmu(t),
M_r(sigma)=integral_0^infinity t^r e^(-sigma t)dmu(t)>=0.   (2.1)
```

This proves complete monotonicity.

For `h_1,...,h_q>0`, write `T_hF(sigma)=F(sigma+h)`.  Directly from
(2.1),

```text
product_(j=1)^q (I-T_(h_j))F(sigma)
 =integral e^(-sigma t)product_j(1-e^(-h_j t))dmu(t).       (2.2)
```

The right side is itself completely monotone.  This includes every ordinary
forward finite-difference sign.

The Hankel positivity is equally exact.  For any finite vector `(c_i)`,

```text
sum_(i,j)c_i conjugate(c_j)M_(i+j)(sigma)
 =integral abs(sum_i c_i t^i)^2 e^(-sigma t)dmu(t)>=0.      (2.3)
```

Every such matrix is strictly positive definite because the measure has
infinitely many support points.  More generally, all minors
`det(M_(i_a+j_b))` with increasing exponent sets are nonnegative: the
Andreief identity writes each minor as an integral of two generalized
Vandermonde determinants, which have the same sign on ordered positive
points.  Thus the derivative moment kernel is Stieltjes-Hankel totally
positive.

This is an automatic consequence of `Lambda(n)>=0`; it contains no
information about analytic continuation to the left of `Re(s)=1`.

There is also an important terminology gate.  Complete monotonicity on the
positive real axis does not make `F(1+x)` a Stieltjes *function* of `x`.
A Stieltjes function is holomorphic off the negative real axis.  The known
nonreal zeros of zeta give nonreal poles of `F(1+x)`, so such a representation
is unconditionally impossible.  The Hankel moment statement in (2.3) is the
valid one; promoting it to global Stieltjes analyticity would silently erase
the zeta divisor.

## 3. What the exact prime dilations give

Euler expansion gives the prime-ray decomposition

```text
F(s)=sum_p log(p)/(p^s-1)
    =sum_p log(p)sum_(r>=1)p^(-rs).                    (3.1)
```

For every integer `k>=2`,

```text
F(s)-F(ks)
 =sum_p log(p)sum_(r>=1, k does not divide r)p^(-rs). (3.2)
```

Consequently (3.2) is completely monotone on `s>1`.  It is an exact positive
prime-exponent sieve.  It does not cancel the pole at `s=1`, because `F(ks)`
is regular there.

If

```text
P(s)=sum_p log(p)p^(-s),
```

then

```text
F(s)=sum_(r>=1)P(rs),
P(s)=sum_(r>=1)mu(r)F(rs).                            (3.3)
```

The inverse identity is signed, and `P` retains the pole at `1`.  Moreover,

```text
F(s)-P(s)=sum_p log(p)sum_(r>=2)p^(-rs)               (3.4)
```

is absolutely holomorphic for `Re(s)>1/2`.  Since the search for *some*
fixed strip may harmlessly restrict to width below `1/2`, (3.4) shows that
all higher powers are already analytic throughout the relevant region.  The
entire strip problem is concentrated in the cross-prime first layer `P(s)`.
No within-prime exponent sieve can estimate that layer.

Forward differences have the same issue.  In (2.2), the multiplier tends to
`1` as `t` tends to infinity, so it preserves the `e^t` tail and hence the
residue at `1`.  Repeating the difference never changes this conclusion.

## 4. Multiplying by the distance to the pole does not preserve the cone

Set

```text
f(x)=F(1+x)=sum_(n>=2)(Lambda(n)/n)e^(-x log n),
H(x)=x f(x).                                           (4.1)
```

Since `f(x)=1/x-gamma+O(x)` at zero, `H` removes the pole and has `H(0)=1`.
It is positive for `x>0`.  Real-axis positivity, however, is far weaker than
complete monotonicity.

### Theorem 4.1 (the pole-cancelled product is not completely monotone)

There are arbitrarily large integers `r` and positive `x` for which

```text
(-1)^r H^(r)(x)<0.                                    (4.2)
```

#### Proof

Differentiating (4.1) gives

```text
(-1)^r H^(r)(x)
 =sum_(n>=2)(Lambda(n)/n)e^(-x log n)(log n)^(r-1)
    (x log n-r).                                      (4.3)
```

Choose a constant `c` satisfying

```text
 log(log(3)/log(2))/log(3/2) < c < 1/log(2).          (4.4)
```

The interval is nonempty; its endpoints are approximately `1.13588` and
`1.44270`.  Put `x=cr`.  The `n=2` term in (4.3) is negative.  Every term
with `n>=3` is positive once `c>1/log(3)`, as follows already from (4.4).

The absolute exponential rate of the first positive term relative to the
negative `n=2` term is

```text
exp(r[log(log(3)/log(2))-c log(3/2)]),                (4.5)
```

which decays exponentially by (4.4).  The whole tail has the same bound.
Indeed `Lambda(n)<=log n`, and for large `r` the function

```text
(log u)^(r+1)u^(-1-cr)
```

is decreasing for `u>=3`.  The integral test followed by `v=log u` bounds
the tail by a constant times

```text
(log 3)^(r+1)3^(-cr).
```

Its ratio to the `n=2` magnitude tends to zero by (4.5).  Therefore (4.3) is
negative for all sufficiently large `r`.  This proves (4.2).  QED

The same calculation closes derivative variants such as
`-(d/dx)[xf(x)]`: if the latter were completely monotone, integrating it
from `x` to infinity would make `H` completely monotone as well.

## 5. Aligned dilations cancel the pole but create negative atoms

An apparently better idea is to align the poles before taking a difference.
For an integer `a>=2`, define

```text
G_a(x)=f(x)-a f(ax).                                  (5.1)
```

Both terms have principal part `1/x`, so (5.1) is regular at zero.  Let

```text
dnu(t)=sum_(n>=2)(Lambda(n)/n)delta_(log n).
```

The unique inverse Laplace measure of (5.1) is

```text
dnu-a(D_a)_*dnu,          D_a(t)=at.                  (5.2)
```

At `t=log(p^a)`, its mass is

```text
log(p)/p^a-a log(p)/p<0.                              (5.3)
```

Thus (5.2) is not positive and `G_a` is not completely monotone.  This is
not a numerical sign test; uniqueness of Laplace transforms makes (5.3) a
complete obstruction.

There is a useful finite-semigroup strengthening.

### Theorem 5.1 (no positive finite pole-cancelling dilation)

Let `A` be a finite set of positive integers and

```text
G(x)=sum_(a in A)c_a a f(ax).                         (5.4)
```

If the pole at zero cancels and the inverse Laplace measure of `G` is
nonnegative, then every `c_a=0`.

#### Proof

The pole cancels exactly when

```text
sum_(a in A)c_a=0.                                    (5.5)
```

At the atom `log(p^a)`, the mass in (5.4) is

```text
log(p)sum_(b in A, b divides a)c_b b p^(-a/b).        (5.6)
```

As the prime `p` tends to infinity, the `b=a` term is `c_a a log(p)/p`;
all proper-divisor terms are `O(log(p)/p^2)`.  Nonnegativity of (5.6) for
all large primes therefore forces `c_a>=0` for every `a in A`.  Equation
(5.5) then forces all coefficients to vanish.  QED

So the integer dilation semigroup offers an exact dichotomy:

```text
retain coefficientwise positivity  => retain the pole,
cancel the pole                     => introduce signed prime atoms.   (5.7)
```

## 6. Positive-measure countermodels with zero-like poles near one

The preceding failures are not artifacts of the chosen annihilator.  The
whole structural axiom set is too weak.

### Theorem 6.1 (continuous positive Laplace countermodel)

Fix `epsilon>0`, `gamma!=0`, and a positive integer `m`.  Put

```text
rho=1-epsilon+i gamma
```

and choose

```text
T>=log(2m)/epsilon.
```

For `t>=T`, the density

```text
w(t)=e^t-2m e^((1-epsilon)t)cos(gamma t)              (6.1)
```

is nonnegative.  Its Laplace transform is

```text
F_*(s)
 =e^(-(s-1)T)/(s-1)
  -m e^(-(s-rho)T)/(s-rho)
  -m e^(-(s-conjugate(rho))T)/(s-conjugate(rho)).     (6.2)
```

Therefore `F_*` is completely monotone on the real interval `s>1`, every
finite-difference and Hankel inequality from Section 2 holds, and yet its
meromorphic continuation has

```text
res_(s=1)F_*=+1,
res_(s=rho)F_*=res_(s=conjugate(rho))F_*=-m.          (6.3)
```

These are exactly the logarithmic-derivative residues of one simple pole and
zeros of multiplicity `m`.  The difference between (6.2) and its three
principal parts is entire.  Hence there is a meromorphic function `Z_*`
with

```text
F_*=-Z_*'/Z_*,
```

a simple pole at `1`, and zeros of multiplicity `m` at `rho` and its
conjugate.

The construction permits any finite set of such pairs at once: take `T`
large enough that the sum of all subleading oscillations is bounded by
`e^t`.  In particular, a functional-equation-symmetric quartet of prescribed
zero locations can be hidden under the same positive density.  Since
`epsilon` is arbitrary, these axioms imply no uniform gap at all.

### Theorem 6.2 (one-prime semigroup countermodel)

The same phenomenon survives an atomic multiplicative skeleton.  Fix a
genuine prime `p` and the same `rho`.  Set

```text
b_k=p^k-p^(k rho)-p^(k conjugate(rho))
   =p^k-2p^(k(1-epsilon))cos(k gamma log p).           (6.4)
```

Then `b_k>=0` for all sufficiently large `k`.  Choose finitely many
corrections `c_k>=0` so that

```text
a_k=b_k+c_k>=0                                        (6.5)
```

for every `k`, and define

```text
Z_p(s)
 =exp(sum_k c_k p^(-ks)/k)
   (1-p^(rho-s))(1-p^(conjugate(rho)-s))/(1-p^(1-s)). (6.6)
```

Only finitely many `c_k` are nonzero.  Direct differentiation gives

```text
-Z_p'(s)/Z_p(s)
 =log(p)sum_(k>=1)a_k p^(-ks),        a_k>=0.         (6.7)
```

Thus the logarithmic derivative is a positive Dirichlet-Laplace measure
supported on the genuine semigroup

```text
p,p^2,p^3,... .                                       (6.8)
```

It has abscissa `1`, pole residue `+1` at `1`, and zero residue `-1` at
`rho` (together with the unavoidable lattice translates of this one-prime
model).

The corrections can additionally be chosen so that

```text
a_(kr)>=a_r             for every k>=2 and r>=1.      (6.9)
```

Indeed, replace each early `b_j` by the maximum of zero and the already
chosen proper-divisor coefficients.  Since `b_j=p^j(1+o(1))`, this changes
only finitely many terms.  Under (6.9), every exact exponent sieve

```text
F_p(s)-F_p(ks)
```

again has nonnegative coefficients.  Therefore even positive prime-power
support plus all finite exponent-dilation inequalities does not force a
strip.

What this model deliberately lacks is zeta's rigid local weight
`Lambda(p^k)=log p` and the collective production of the pole by infinitely
many distinct primes.  Those are precisely the structures a successful new
argument would have to exploit.

## 7. What input would actually be sufficient

In the pole-centered variable, define

```text
dnu(t)=sum_(n>=2)(Lambda(n)/n)delta_(log n),
f(x)-1/x=integral_0^infinity e^(-xt)(dnu(t)-dt).       (7.1)
```

A zeta zero `rho` is a pole of (7.1) at `x=rho-1`.  Thus a fixed zero-free
strip is exactly a fixed left half-strip without such poles.

If one could transform the signed discrepancy `dnu-dt` into a nonnegative
measure `domega`, with a Laplace multiplier that does not vanish at any
candidate zero, then a bound

```text
integral e^(eta t)domega(t)<infinity                  (7.2)
```

would give a zero-free strip of width `eta`.  Positivity alone does not give
(7.2).  For a positive measure, (7.2) is precisely the extra exponential
tail information needed to evaluate its Laplace transform at `x=-eta`.

Sections 4 and 5 show that the elementary pole annihilators do not even
produce `domega>=0`.  Section 6 shows that all of the remaining abstract
positive inequalities are compatible with subleading oscillations of every
exponent `1-epsilon`.

The only unpruned input is therefore coefficient-specific and global:

1. use `Lambda(p^k)=log p` to remove the already-holomorphic higher-power
   layer;
2. prove a signed cross-prime inequality for

   ```text
   sum_p log(p)p^(-s)-1/(s-1);                        (7.3)
   ```

3. retain enough cancellation to obtain a fixed exponential rate, rather
   than taking absolute values or reverting to the automatic positive cone.

This is a useful reality check for R71--R87.  Prime dilation does not supply
a new cancellation mechanism for the completed energy.  It either preserves
the pole inside a positive cone or cancels the pole by recreating the signed
prime discrepancy whose fixed-power control is the desired theorem.

## 8. Final gate

```text
raw von Mangoldt Laplace positivity                 EXACT
finite-difference/Hankel total positivity           EXACT
positive prime-exponent sieves                      EXACT
pole cancellation by multiplication                NOT completely monotone
pole cancellation by finite aligned dilations      NO positive measure
abstract positive-measure implication of a strip   FALSE
one-prime semigroup implication of a strip          FALSE
fixed zero-free strip                               NOT PROVED
nonexistence of a fixed zero-free strip             NOT PROVED.       (8.1)
```

The route is closed as an abstract positivity argument.  It can be revived
only with an independently proved, fixed-power, cross-prime estimate which
is absent from the complete-monotonicity and dilation axioms.
