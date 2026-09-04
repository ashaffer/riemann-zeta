# Mertens Type-I/II attack: principal-band and rank-one gate

Status: exact reduction and scoped no-go theorem, 2026-08-12.  A sharper
rank-one decomposition of the short-increment energy is proved, the full
Fourier problem is reduced to one explicit principal additive band, and the
zero mode is recompleted as an exact centered `mu*(Lambda-1)` bilinear form.
The natural Type-I, pretentious, and pointwise additive-twist estimates are
then tested at the exponent needed for the line `Re(s)=0.99`.  No fixed-power
estimate, zero-free strip, or RH claim is proved.

The main new structural conclusion is narrow but useful:

```text
all frequencies ||alpha|| >= X^0.01/H       coefficient-blind power saving;
centered dispersion                          orthogonal variance only;
remaining mean projection                    weighted Mertens/PNT carrier;
componentwise Type I after centering          already fixed-strip strength.
```

Thus the smallest missing arithmetic estimate is not a generic Type-II
minor-arc theorem.  It is an **uncentered principal-band theorem**, or,
equivalently on the mean projection, a joint signed estimate for one exact
`mu(d)(Lambda(m)-1)` form.  That mean estimate by itself already gives the
strip.

## 1. Exact rank-one/variance factorization

Let `1<=H<=X/2`, put `N=X-H`, and define

```text
S_n=sum_(n<k<=n+H) mu(k),             1<=n<=N,
J(X,H)=sum_(n=1)^N |S_n|^2.                         (1.1)
```

Let

```text
w(k)=[min(N,k-1)-max(1,k-H)+1]_+,
T(X,H)=sum_(n=1)^N S_n=sum_(k<=X)mu(k)w(k).          (1.2)
```

For `X>=2H`, the weight is the exact trapezoid

```text
w(1)=0,
w(k)=k-1                       (2<=k<=H),
w(k)=H                         (H+1<=k<=N+1),
w(k)=X-k+1                     (N+2<=k<=X).          (1.3)
```

Consequently

```text
|T(X,H)-H*M(X)|<=H^2.                                (1.4)
```

Indeed, the absolute coefficient loss at `k=1` is `H`; the two triangular
edges each have total loss `H(H-1)/2`.

### Theorem 1.1 (exact ANOVA decomposition)

One has

```text
J(X,H)
 =|T(X,H)|^2/N
  +sum_(n=1)^N |S_n-T(X,H)/N|^2.                    (1.5)
```

In particular,

```text
J(X,H)>=(H^2/N)(|M(X)|-H)_+^2,                      (1.6)

|M(X)|<=H+sqrt(N*J(X,H))/H.                         (1.7)
```

This improves the harmless endpoint constant `2H` in the earlier anchored
step-Poincare argument to `H`.  More importantly, (1.5) identifies the
obstruction as an exact rank-one summand, not as an error term.

In matrix language, let `B_(n,k)=1_(n<k<=n+H)` and let
`P_0=N^(-1) 1 1^*` be projection onto constants in the start variable.  Then

```text
B^*B
 =B^*P_0B+B^*(I-P_0)B
 =w tensor w/N + K_cent,                             (1.8)

K_cent>=0,

<mu,B^*B mu>
 =|<w,mu>|^2/N+<mu,K_cent mu>.                       (1.9)
```

Any dispersion argument which centers the interval sums applies to
`K_cent`.  It says literally nothing about `<w,mu>=T`; putting that mode
back by Cauchy or a triangle inequality restores the Mertens gate.

The identities and the bound (1.4) were checked directly for every
`X<=30` and `1<=H<=X/2`.

## 2. A boundary-safe calibration for the 0.99 line

To target a strip of width `delta=0.01`, it is not necessary to take
`H=X^0.99`.  The maximal scale at which the crude full-convolution boundary
still fits the target is

```text
theta=0.98=49/50,
H=floor(X^theta),
eta=2*delta/theta=1/49=0.020408163265306122... .     (2.1)
```

Then

```text
H^eta=X^0.02,
X*H^(2-eta)=X^2.94,
H^3=X^2.94,                                          (2.2)

max(theta,1-theta*eta/2)=0.99.                       (2.3)
```

Thus the elementary full-convolution boundary cost `O(H^3)` is absorbed at
the desired energy scale: at equality it only enlarges the implied constant
in a `<<` estimate; it is not an `o(1)` error.  If a strict power cushion is
preferred, one may take `theta=0.97`, `eta=0.02/0.97`; then the target is
`X^2.92` and the boundary is `X^2.91`.  More generally, for a desired width
`delta`, put
`eta=2 delta/theta`; the full and internal energies are interchangeable at
the target scale whenever

```text
theta+2 delta<=1.                                    (2.4)
```

The inequality is strict exactly when the boundary is lower by a fixed
power.

This calibration removes an avoidable endpoint obstruction while keeping
exactly the required `0.99` conclusion.

## 3. Every nonprincipal frequency is already power-saved

Extend `mu(k)1_(1<=k<=X)` by zero and put

```text
J^*(X,H)=sum_(n in Z)|sum_(n<k<=n+H)mu(k)|^2,
A_X(alpha)=sum_(k<=X)mu(k)e(k alpha),
D_H(alpha)=sum_(j=1)^H e(j alpha).                   (3.1)
```

Parseval gives

```text
J^*(X,H)=integral_0^1 |A_X(alpha)|^2|D_H(alpha)|^2dalpha.
                                                               (3.2)
```

There are exactly `X+H-1` nonzero windows in (3.1), and every coefficient
`mu(k)` occurs in exactly `H` of them.  Therefore

```text
sum_n sum_(n<k<=n+H)mu(k)=H*M(X),

J^*(X,H)>=H^2|M(X)|^2/(X+H-1).                      (3.3)
```

Fix `delta>0` and set

```text
R=X^delta/H,
mathfrak_M={alpha: ||alpha||<R}.                     (3.4)
```

For `alpha` outside `mathfrak_M`,

```text
|D_H(alpha)|<=1/(2||alpha||)<=H/(2X^delta).
```

Since `integral |A_X|^2=sum_(k<=X)mu(k)^2<=X`, this proves the
coefficient-blind estimate

```text
integral_(alpha notin mathfrak_M)
 |A_X(alpha)|^2|D_H(alpha)|^2dalpha
 <=(1/4)X H^2 X^(-2 delta).                         (3.5)
```

If `H=X^theta` and `eta=2 delta/theta`, the right side of (3.5) is exactly
the target scale `X H^(2-eta)`.  Hence **all of the missing power lies in**

```text
C(X,H;delta)
 =integral_(||alpha||<X^delta/H)
   |A_X(alpha)|^2|D_H(alpha)|^2dalpha.              (3.6)
```

At the boundary-safe calibration (2.1), the desired internal estimate is,
up to absolute constants, equivalent to

```text
C(X,X^0.98;0.01)<<X^2.94.                            (3.7)
```

Indeed, (3.5) controls the complement, while
`0<=J^*-J<2H^3=O(X^2.94)`.  Conversely, (3.3) and (3.5) give the explicit
zero-mode imprint

```text
C(X,H;delta)
 >=H^2|M(X)|^2/(X+H-1)
   -(1/4)X H^2 X^(-2 delta).                         (3.8)
```

Thus a hypothetical value `|M(X)|>=X^(1-delta+epsilon)` forces the
principal-band target to fail by `X^(2 epsilon)` along that sequence.

Equations (3.5)--(3.8) are the useful frequency triage: a generic minor-arc
improvement cannot help, because the complement of the principal band is
already below budget without using Mobius cancellation.

## 4. Exact centered Type-I/II recompletion

For `n>1`, the convolution identities

```text
(mu*Lambda)(n)=-mu(n)log n,
(mu*1)(n)=0                                             (4.1)
```

give an exact bilinear representation of the rank-one carrier:

```text
T(X,H)
 =-sum_(dm>=2) mu(d)(Lambda(m)-1)
                  w(dm)/log(dm).                     (4.2)
```

No approximation, Perron truncation, or endpoint term occurs in (4.2).
The identity was checked directly for all `X<=30`, `H<=X/2`.

The energy target implies, by (1.5),

```text
|T(X,H)|<<H X^(1-delta)                              (4.3)
```

when `H^eta=X^(2 delta)`.  Conversely, if (4.3) holds for all large `X`
and `H<=X^(1-delta)`, then (1.4) gives

```text
M(X)<<X^(1-delta),                                   (4.4)
```

and hence `zeta(s)!=0` for `Re(s)>1-delta`.  Therefore (4.3), the smallest
necessary estimate on the mean projection, already has fixed-strip
strength even before the centered variance in (1.5) is estimated.

### Theorem 4.1 (the centered Type-I head is already a PNT gate)

The `d=1` summand of (4.2) is

```text
B_1(X,H)
 =-sum_(m=2)^X (Lambda(m)-1)w(m)/log m.              (4.5)
```

Put

```text
R_Lambda(x)=sum_(2<=m<=x)(Lambda(m)-1)/log m.         (4.6)
```

Because `w/H=1` away from the two edge intervals of total length less than
`2H`, and

```text
|Lambda(m)-1|/log m=O(1),
```

one has

```text
B_1(X,H)/H=-R_Lambda(X)+O(H).                        (4.7)
```

Consequently, a componentwise Type-I estimate

```text
|B_1(X,H)|<<H X^(1-delta),
H<=X^(1-delta),                                      (4.8)
```

implies `R_Lambda(X)<<X^(1-delta)`.  Abel summation then gives

```text
psi(X)-X
 =R_Lambda(X)log X-integral_2^X R_Lambda(t)dt/t+O(1)
 <<X^(1-delta)log X.                                 (4.9)
```

The usual Mellin continuation of `-zeta'/zeta` now excludes zeros in
`Re(s)>1-delta`.  Thus estimating even the centered `d=1` Type-I piece
separately with the required power already proves the desired strip.

This leaves only one possible Type-I/II escape: retain signed cancellation
between the `d=1` PNT carrier and every other `d` before taking absolute
values.  Exact recompletion (4.2) shows that the result of doing so is the
weighted Mertens carrier `T`, not a lower-strength remainder.

## 5. Quantitative ceilings for three natural inputs

These are scoped no-go statements for the named inputs, not impossibility
theorems for every arithmetic argument.

### 5.1 Pretentious distance

For every real `t`,

```text
D(mu,n^(it);X)^2
 =sum_(p<=X)(1+cos(t log p))/p
 <=2 log log X+O(1).                                 (5.1)
```

Hence a Halasz/pretentious gain depending on this distance through
`exp(-c D^2)`, with fixed `c>0`, can supply at best a fixed power of
`1/log X`.  The required gain is `X^(-0.02)` in energy.  A new input must
therefore use more than Euler-prime distance or standard pretentious
noncorrelation.

### 5.2 Exact small-prime parity conditioning

Let `g_z(n)` retain only the local Mobius factors for primes `p<=z`: at one
prime it is `1` if `p` does not divide `n`, `-1` if `p||n`, and `0` if
`p^2|n`.  Its exact mean over a period is

```text
mean(g_z)
 =product_(p<=z)(1-2/p+1/p^2)
 =product_(p<=z)(1-1/p)^2
 asymp 1/(log z)^2.                                  (5.2)
```

Even taking `z=X^c` therefore gives only logarithmic bias cancellation.
Large-prime joint cancellation could go further, but a sieve or parity
argument which stops after independent small-prime conditioning cannot
produce `X^(-delta)`.

### 5.3 Log-free additive-twist bounds

As a current primary-source comparator, Theorem 1 of Srivastav,
[*Log-free bounds on exponential sums over primes*](https://arxiv.org/abs/2505.07803),
gives in the `q=1`, `alpha=t/X` range relevant here a bound of the shape

```text
|A_X(t/X)|<<X/sqrt(max(1,|t|))                       (5.3)
```

with a bounded exponent-dependent factor, throughout the present band
`|t|<=X^(1+delta-theta)=X^0.03`.  Even granting (5.3) in its strongest
displayed form, direct integration gives only

```text
integral_(|alpha|<=1/H)|A_X(alpha)|^2H^2dalpha
 <<X H^2 log(1+X/H),                                 (5.4)

integral_(1/H<=|alpha|<=X^delta/H)
 |A_X(alpha)|^2/alpha^2 dalpha
 <<X H^2.                                            (5.5)
```

This misses (3.7) by the fixed factor `X^0.02` (up to logarithms).  The
decay in the nonzero phase `t` is real, but the bounded-`t` principal sector
retains full scale.  Classical Davenport logarithmic uniformity has the
same exponent-level limitation.

## 6. The smallest new theorem that would actually close the route

The exact decomposition separates two tasks:

```text
(A) |sum_(dm>=2)mu(d)(Lambda(m)-1)w(dm)/log(dm)|
      <<H X^0.99,                                    (6.1)

(B) <mu,K_cent mu><<X H^2 X^(-0.02).                (6.2)
```

At `H=X^0.98`, (6.1)--(6.2) imply

```text
J(X,H)<<X H^(2-1/49),
M(X)<<X^0.99,
zeta(s)!=0 for Re(s)>0.99.                           (6.3)
```

But (6.1) alone already implies the last two conclusions by (1.4).
Therefore no proof architecture should advertise (6.2), a centered
large-sieve estimate, as the decisive strip step.  The decisive new input is
one of the equivalent uncentered statements:

1. the principal-band estimate (3.7);
2. the signed all-`d` bilinear mean estimate (6.1); or
3. the weighted Mertens estimate `T(X,H)<<H X^0.99`.

Taking absolute values by Type-I/II block fails twice: before centering it
leaves continuum main terms, and after centering its `d=1` block is the PNT
fixed-strip carrier of Theorem 4.1.  Pretentious distance, independent
small-prime parity, and current log-free phase decay all stop at a
logarithmic or full-scale bounded-phase remainder.

The search space is therefore pruned to a genuinely joint theorem which
keeps the mean projection and all Type-I/II blocks signed until the end.
No such fixed-power theorem is proved here.
