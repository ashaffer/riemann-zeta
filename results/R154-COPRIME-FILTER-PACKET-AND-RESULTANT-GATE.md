# R154 coprime-filter packet and resultant gate

## Status

R153 leaves one conspicuous loophole.  A single nonlinear filter introduces
many mixed value divisors, but filters of coprime degrees have only the target
divisor in common.  Perhaps a vector, resultant, or corona operation could
retain that common zero while discarding every artificial value.

This report carries out that elimination exactly.  It works algebraically,
but it moves the full mixed-divisor complexity to infinity and to a regular
polynomial germ.  The support-amplified scalar has high-order poles at the
original denominator zeros, and its regular germ can cancel the target jet.
An unweighted argument-principle contour deletes the amplifying correction
identically; a weighted contour pays its full boundary growth.

```text
coprime packet common divisor F=0                           EXACT
consecutive-filter elimination identity                    EXACT
support shift to H^(q+1) after elimination                 EXACT
finite mixed-value poles removed                           YES
complexity transferred to F=infinity/high-order poles      EXACT
rational common-divisor scalar with no other values         MONOMIAL ONLY
unweighted contour amplification                           ZERO
weighted contour without regular-germ bill                 IMPOSSIBLE
vector/Gram generic lower bound                            FALSE LOCALLY
fixed uniform zeta zero-free strip                         NOT PROVED
zeros approaching one                                      NOT PROVED
```

Date: 2026-08-08.

Predecessor:
[`R153-NONLINEAR-SUPPORT-AMPLIFIER-AND-MIXED-VALUE-GATE.md`](R153-NONLINEAR-SUPPORT-AMPLIFIER-AND-MIXED-VALUE-GATE.md).

## 1. The coprime packet

Write

```text
F=1+U,
x=1-F=-U.                                                   (1.1)
```

For every integer `n>=2`, define

```text
P_n=1-x^n,
B_n=P_n'/P_n.                                               (1.2)
```

At an `F`-zero one has `x=1`, so every `P_n` vanishes with the
same multiplicity as `F`.  Its other zeros are the value divisors

```text
x=omega,                  omega^n=1,
F=1-omega.                                                     (1.3)
```

If `(m,n)=1`, the root sets in (1.3) intersect only at `x=1`.
In particular `P_q` and `P_(q+1)` have common zero divisor exactly `F=0`.

On the Euler side, `x=-U` has no constant term and is supported beyond `H`.
The response

```text
B_n=n x^(n-1)F'/(1-x^n)                                    (1.4)
```

starts with `n` nonconstant Dirichlet factors, so its absolute support begins
beyond `H^n`.  For even `n`, its coefficients agree with the positive filter
in R153; odd `n` retains the same absolute Cauchy bound.

## 2. Exact consecutive-degree elimination

From (1.4), a direct common-denominator calculation gives

```text
B_q-[q/(q+1)]B_(q+1)
 =q x^(q-1)F'F/[(1-x^q)(1-x^(q+1))],                        (2.1)

B_q B_(q+1)
 =q(q+1)x^(2q-1)(F')^2/[(1-x^q)(1-x^(q+1))].               (2.2)
```

Therefore

```text
B_q B_(q+1)
 ---------------------------
 B_q-[q/(q+1)]B_(q+1)

 =(q+1)x^q F'/F.                                           (2.3)
```

The left side is a packet-level rational elimination of every noncommon
root-of-unity value.  The right side makes its true cost transparent.

Put

```text
C_q=x^q F'/F.                                               (2.4)
```

At an `F`-zero of order `m`, `C_q` has a simple pole of residue `m`.
Thus the desired target survives with constant residue.  Since `x^q` supplies
`q` factors and `F'/F` supplies one more, its Dirichlet support begins beyond

```text
H^(q+1).                                                    (2.5)
```

At first sight (2.3)--(2.5) seem to remove the R153 gate entirely.

There is also an exact finite-Fourier rigidity behind the individual packet.
Let `omega` range over the `q`th roots of unity and consider a weighted
response

```text
sum_(omega^q=1)c_omega F'/[F-(1-omega)].                    (2.6)
```

With `U=F-1`, expansion at the Euler point gives

```text
1/(U+omega)
 =sum_(n>=0)(-1)^n omega^(-(n+1))U^n.                      (2.7)
```

Vanishing the powers `U^0,...,U^(q-2)` is therefore equivalent to

```text
sum_omega c_omega omega^(-j)=0,             1<=j<=q-1.     (2.8)
```

Discrete Fourier inversion forces every `c_omega` to be equal.  Thus the
uniform residues on the target and all `q-1` mixed values are uniquely forced
by exact `H^q` support.  Giving the target a larger positive weight
immediately restores a lower Euler power.

## 3. The regular polynomial germ

The identity

```text
x^q=(1-F)^q                                                (3.1)
```

shows that

```text
C_q=F'/F+d/ds R_q(F),                                      (3.2)
```

where

```text
R_q'(z)=[(1-z)^q-1]/z,

R_q(z)=sum_(j=1)^q (-1)^j binom(q,j) z^j/j.                 (3.3)
```

Thus `C_q` is the logarithmic derivative of

```text
F exp(R_q(F)).                                               (3.4)
```

The exponential factor is nonzero wherever finite, so (3.4) has exactly the
finite zeros of `F`.  But it is an essential singularity at every pole of
`F`.  Equivalently, if `F` has a pole of order `m`, then `C_q` has a pole of
order

```text
mq+1.                                                       (3.5)
```

The finite mixed values have not disappeared for free.  Their `q` units of
complexity have moved to the value `F=infinity`.

The second term in (3.2) is analytic at the target.  Its Taylor jet is not
controlled by the target divisor and can cancel the jet of `F'/F` to any
prescribed finite order.  This is precisely R142's regular-Laurent
conditioning, now produced by an exact resultant identity rather than an
arbitrary countermodel.

## 4. Rational common-divisor rigidity

There is a short algebraic reason the packet cannot produce a rational
zero-only scalar with the same support gain.

### Lemma 4.1 -- two-point divisor rigidity

If a nonzero rational function `Phi(z)` on the Riemann sphere has its divisor
supported only at `0` and `infinity`, then

```text
Phi(z)=c z^m                                                (4.1)
```

for some nonzero constant `c` and integer `m`.

#### Proof

After multiplying by a suitable power of `z`, the function has no zero or
pole anywhere on the sphere and is therefore constant.  QED.

Consequently, any rational scalar functional calculus which removes every
nonzero finite value divisor and retains `F=0` has logarithmic derivative

```text
mF'/F.                                                      (4.2)
```

This has only the original first-order head support.  To obtain (2.5), the
packet must multiply (4.1) by a nonvanishing transcendental unit such as
`exp(R_q)`, and that unit is exactly the uncontrolled regular germ in (3.2).

There is no bounded corona inversion hidden in the vector packet.  Near
`U=0`,

```text
B_n/F'=n(-U)^(n-1)/[1-(-U)^n].                              (4.3)
```

Every bounded holomorphic combination of degrees `n>=q` remains
`O(U^(q-1))`.  Recovering `F'/F`, which is nonzero to first order there,
requires a corona coefficient of size at least `|U|^(-(q-1))`.  This inverse
condition number repays exactly the support gain.

The elementary Bezout identities display both choices:

```text
P_(q+1)-xP_q=1-x=F,                                        (4.4)

P_(q+1)-P_q=x^q(1-x)=x^qF.                                 (4.5)
```

Equation (4.4) isolates the target but loses the head shift.  Equation (4.5)
retains the head shift but adds the high-multiplicity `F=1` divisor.  Taking
the nonlinear logarithmic combination (2.3) trades that divisor for the
infinity cost (3.5).

## 5. Contour conservation

Let `Gamma` be a closed contour avoiding all divisors.  Since a derivative of
a meromorphic function has zero residue at every pole, (3.2) gives

```text
integral_Gamma C_q(s) ds
 =integral_Gamma F'(s)/F(s) ds.                             (5.1)
```

Thus an unweighted argument-principle count sees exactly the original
divisor and none of the support amplification.

For a holomorphic weight `phi`, integration by parts gives

```text
integral_Gamma phi C_q ds
 =integral_Gamma phi F'/F ds
  -integral_Gamma phi' R_q(F) ds.                           (5.2)
```

Any weight capable of localizing the target therefore pays the degree-`q`
boundary value `R_q(F)`.  The ordinary contour cannot simultaneously retain
the `H^(q+1)` gain and discard the regular-germ bill.

## 6. A sharp local vector countermodel

The failure is visible before scalar elimination.  Let

```text
F(s)=1+(s-z_*)/d,
x(s)=-(s-z_*)/d.                                            (6.1)
```

Then `F` has a simple zero at `rho=z_*-d`, while `x(z_*)=0`.  Formula (1.4)
shows that

```text
B_n^(k)(z_*)=0,                    0<=k<=n-2.               (6.2)
```

Both components of the consecutive packet `(B_q,B_(q+1))` therefore have
zero jets through order `q-2`, despite their common target pole at distance
`d`.  Common-divisor data alone gives no lower bound below the packet
resolution scale.

There is also an exact Hardy-circle calculation.  Put `t=R/d<1`.  On
`|s-z_*|=R`,

```text
(1/2pi)integral_0^(2pi)|B_n(z_*+Re^(i theta))|^2 dtheta
 =n^2/d^2 * t^(2n-2)/(1-t^(2n)).                            (6.3)
```

For every fixed `R<d`, (6.3) is exponentially small in `n`, even though the
target logarithmic derivative alone has size of order `1/d`.  One must move
the circle to `R=d(1-O(1/n))`, where the mixed packet is resolved.  Positive
Gram, Fejer, or contour-energy operations therefore do not recover the target
at fixed geometry.

The model (6.1) is local rather than an Artin Euler product.  Its role is
precise: it disproves any packet lower bound based only on a common divisor,
holomorphy, and favorable residues.  A successful arithmetic theorem would
have to add genuinely new information about the actual mixed `a`-points.

In fact every fixed finite packet can be flattened to arbitrary order.  Pick
a value `c` avoiding all of its root values.  Let `T_N` be the Taylor
polynomial at `z_*`, through degree `N+1`, of

```text
log c-log(s-rho),                                           (6.4)
```

and put

```text
F_N(s)=(s-rho)exp(T_N(s)).                                  (6.5)
```

This entire function has exactly the simple zero `rho`, while

```text
F_N(s)=c+O((s-z_*)^(N+2)).                                  (6.6)
```

Every packet response is consequently `O((s-z_*)^(N+1))`, so all of its jets
through order `N` vanish.  Finite Gram and Hankel constructions cannot obtain
a common-divisor lower bound without controlling the exponential unit.  The
universal boundary-growth form of that payment is R153, equation (6.6).

## 7. Consequence

Coprime filters do isolate the target algebraically.  There are only three
ways to turn that fact into a scalar response:

```text
use the rational gcd F:             lose H^q support;
retain a finite mixed-value divisor: return to R153;
remove all finite mixed values:     acquire exp(R_q(F)) and order-q infinity
                                    growth.                 (7.1)
```

The packet/resultant route therefore does not prove a fixed strip.  It closes
the most direct algebraic workaround to R153, while leaving the same genuinely
arithmetic possibility: a target-local joint theorem for the actual value
divisors, strong enough to beat their varying Turan dimension.

Successor:
[`R155-NORMAL-FAMILY-MIXED-VALUE-INEVITABILITY-GATE.md`](R155-NORMAL-FAMILY-MIXED-VALUE-INEVITABILITY-GATE.md),
which proves that zero-free mixed-value selection is impossible and replaces
it by a signed forced-divisor target.
