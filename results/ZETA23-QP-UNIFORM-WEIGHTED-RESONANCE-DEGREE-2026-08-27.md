# Uniform weighted resonance degree for balanced-tower lanes (2026-08-27)

## Result

Fix constants `0<A<B`.  For positive integers `F,b,c`, define

```text
d_F(b,c)=lcm(b^2 c/gcd(b^2 c,F^3),
             b c^2/gcd(b c^2,F^3)).                 (0.1)
```

For every positive integer `d1` and every `b` in the shell
`A F <= b <= B F`, one has

```text
sum_(A F <= c <= B F)
 gcd(d1,d_F(b,c))/sqrt(d1 d_F(b,c))
 <= C_(A,B) 3^omega(F b d1) tau(F b d1).            (0.2)
```

Consequently, uniformly for `b` in the shell and `d1 <= F^C` with any
fixed `C`, the left side is

```text
exp(O_(A,B,C)(log F/log log(F+2))) = F^o(1).         (0.3)
```

In particular, taking `d1=1` proves the previously missing uniform
extension of the central-lane estimate:

```text
sum_(c asymp F) d_F(b,c)^(-1/2) = F^o(1)            (0.4)
```

uniformly for every `b asymp F`.  There can be no uniform negative power
of `F` in (0.4): when `b=c=F`, one has `d_F(F,F)=1`, so this single term
already equals one.

The proof below is elementary and keeps the stronger greatest-common-
divisor density occurring in the normalized principal hinge Gram matrix.

## 1. Exact local exponent

For a prime `p`, put

```text
f=v_p(F),  y=v_p(b),  z=v_p(c),  r=v_p(d1).
```

Taking the maximum of the two reduced exponents in (0.1) gives

```text
e(z):=v_p(d_F(b,c))
    =(y+z+max(y,z)-3f)_+.                            (1.1)
```

The local factor of the summand in (0.2) is therefore

```text
kappa_p(z)=p^(-|r-e(z)|/2).                          (1.2)
```

The important feature of (1.1) is

```text
e(z+1)-e(z) is in {0,1,2}.                           (1.3)
```

This remains true at the two possible hinges, where the positive part
turns on and where `z` crosses `y`.

## 2. A positive divisor expansion

Define

```text
G_p(z)=p^z kappa_p(z).
```

By (1.3) and the reverse triangle inequality,

```text
log_p G_p(z+1)-log_p G_p(z)
 =1-(|r-e(z+1)|-|r-e(z)|)/2
 >=1-(e(z+1)-e(z))/2 >=0.                            (2.1)
```

Thus `G_p` is nondecreasing.  It is eventually constant: once
`z>=y` and `y+2z-3f>=r`, (1.1) gives

```text
G_p(z)=p^((3f+r-y)/2).
```

Set

```text
A_p(0)=G_p(0),
A_p(k)=G_p(k)-G_p(k-1)  (k>=1).                     (2.2)
```

Every `A_p(k)` is nonnegative, and only finitely many increments with
`k>=1` are nonzero.  Moreover, if `p` does not divide `F b d1`, then
`e(z)=2z`, `r=0`, and `G_p(z)=1`; hence `A_p(0)=1` and all the other
increments vanish.

Let `P` be the finite set of primes dividing `F b d1`.  For an integer
`m` supported on `P`, define

```text
A(m)=product_(p in P) A_p(v_p(m)).
```

(The factors with valuation zero are included.)  Telescoping (2.2)
prime by prime gives the exact finite expansion

```text
G(c):=product_p G_p(v_p(c))
     =sum_(m|c, m supported on P) A(m),              (2.3)
```

and, by (1.2), the desired density weight is exactly

```text
gcd(d1,d_F(b,c))/sqrt(d1 d_F(b,c))=G(c)/c.          (2.4)
```

Positivity is what makes (2.3) useful; no cancellation estimate is
being inserted here.

## 3. Summing over a shell

Since `c>=A F`, equations (2.3)--(2.4) and positivity give

```text
sum_(A F<=c<=B F) G(c)/c
 <=1/(A F) sum_(c<=B F) sum_(m|c) A(m)
 <=B/A sum_m A(m)/m
 = B/A product_p L_p,                                (3.1)
```

where

```text
L_p=sum_(k>=0) A_p(k)/p^k
    =(1-1/p) sum_(z>=0) kappa_p(z).                  (3.2)
```

The identity in (3.2) follows by summation by parts; convergence is
immediate because `G_p` is eventually constant.

For a completely explicit local bound, put

```text
z0=max(y, ceil((3f-y+r)/2), 0).
```

For `z>=z0`, one has `e(z)=y+2z-3f>=r`, so successive values of
`kappa_p(z)` have ratio `p^(-1)`.  Before `z0`, use only
`kappa_p(z)<=1`.  Therefore

```text
sum_(z>=0) kappa_p(z)
 <= z0 + 1/(1-1/p)
 <= z0+2,

L_p <= z0+2 <= 3(f+y+r+1).                           (3.3)
```

For `p` outside `P`, the exact value is `L_p=1`.  Multiplying (3.3) over
`P` proves

```text
product_p L_p
 <=3^omega(F b d1) product_(p|F b d1)(f+y+r+1)
 = 3^omega(F b d1) tau(F b d1),                     (3.4)
```

which is (0.2).  The standard maximal-order divisor estimate, together
with `b asymp F` and `d1<=F^C`, gives (0.3).

## 4. Principal hinge Schur-row corollary

For a first transpose-merged packet with lanes `(a,b)`, write
`d1=d_F(a,b)`.  A principal hinge partner `(b,c)` has period
`d2=d_F(b,c)`.  The common-frequency density in its normalized Gram
entry is

```text
sqrt(d1 d2)/lcm(d1,d2)
=gcd(d1,d2)/sqrt(d1 d2).                             (4.1)
```

The normalized smooth overlap multiplying (4.1) has absolute value at
most one by Cauchy--Schwarz.  Summing (4.1) over every shell lane `c` and
using (0.2) therefore shows that the full **principal-hinge density
Schur row** is `F^o(1)`, uniformly in the shared lane `b`.

The polynomial-period hypothesis needed in (0.3) is automatic here.
Indeed, (1.1) also shows exponent by exponent that

```text
d_F(a,b) divides a b lcm(a,b),
```

and hence, for `a,b asymp F`,

```text
d1 <= a b lcm(a,b) <= a^2 b^2 << F^4.               (4.2)
```

Thus the corollary applies uniformly to every first shell packet, not
only to the central lane `b=F`.  Transpose orientations or endpoint
conventions alter the row bound by at most an absolute constant.

## 5. What this does not prove

This result closes the arithmetic weighted-degree question for the
**principal** common-frequency components.  It does not estimate, in
aggregate, the nonprincipal residue classes in the packet sums.  Those
classes are individually lower order in the fixed-period asymptotic,
but that asymptotic is not uniform as the periods and lane ratios vary
with `F`.  A proof of the full transpose-quotiented Gram bound still
requires a uniform large-sieve or summation argument for those
near-resonant nonprincipal terms.  No such estimate is claimed here.
