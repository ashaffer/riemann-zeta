# High-order mollifier shift audit

Status: **exact coefficient and exponent ledgers proved; a tempting
high-order shortcut is refuted by a newly exposed central Mellin pole.  No
zero-free strip or RH proof is claimed.**

Date: 2026-08-09.

## 1. Verdict

A proportional-order logarithmic taper initially appears to bypass the usual
long-mollifier length barrier.  That appearance is false.

For an integer `k>=1`, define

```text
M_(Y,k)(s)
 =sum_(d<=Y) mu(d)d^(-s)
   [log(Y/d)/log Y]^k.                                  (1.1)
```

If

```text
k=alpha log Y+O(1),                                     (1.2)
```

then the terminal coefficients are strongly damped and the mollifier alone
has a much shorter effective mean-value length.  A first calculation also
seems to make an off-line zero produce an amplified residue.

The missing term is decisive: the exact Mellin transform of (1.1) has a pole
factor `(w-1)^(-(k+1))`.  Reusing the first-order Bettin--Gonek auxiliary
kernel leaves a new pole at `w=1` of order `k-1`.  Its polynomial residue is a
completed center term and cannot be discarded.  Removing it by altering the
auxiliary kernel exponentially attenuates the target-zero residue.

Thus proportional-order tapering does not give a free zero-free strip.  The
failed shortcut is useful because it identifies an exact completed object:

> any viable high-order mollifier argument must retain and exploit the joint
> cancellation between the target-zero carrier and the full central
> `(w-1)` residue polynomial.

## 2. Coefficient shift

Write

```text
w_(Y,k)(d)
 =1_(d<=Y)[1-log d/log Y]^k.                             (2.1)
```

For `k=ceil(alpha log Y)` and fixed `d`,

```text
w_(Y,k)(d) -> d^(-alpha).                               (2.2)
```

Moreover, for every `d<=Y`,

```text
w_(Y,k)(d) <= d^(-alpha).                               (2.3)
```

Indeed `log(1-x)<=-x` for `0<=x<1`, and
`k>=alpha log Y`.

For `alpha>1/2`, (2.3) makes the mollifier uniformly absolutely bounded on
the critical line:

```text
|M_(Y,k)(1/2+it)|
 <=sum_d d^(-1/2-alpha)<infinity.                       (2.4)
```

This observation creates an important fail-fast test.  Any purported
high-order zero detector which combines (2.4) with the classical zeta second
moment to prove RH must have lost a compensating Mellin term.  Section 4
identifies that term exactly.

## 3. Mollifier-alone effective length

The Montgomery--Vaughan mean-value error for the mollifier alone is governed
by

```text
sum_(d<=Y) w_(Y,k)(d)^2.                                (3.1)
```

Put `d=Y^r`.  At exponential scale the contribution near `r` is

```text
Y^[r+2 alpha log(1-r)+o(1)].                            (3.2)
```

For `0<alpha<1/2`, the exponent is maximized at

```text
r_*=1-2 alpha,                                          (3.3)
```

and the resulting effective-support exponent is

```text
chi(alpha)
 =1-2 alpha+2 alpha log(2 alpha).                       (3.4)
```

For `alpha>=1/2`, the maximum moves to `r=0` and the power exponent is zero.
Thus, at the mollifier-only level, nominal length `Y=T^theta` is compatible
with the natural `T` scale when

```text
theta chi(alpha)<=1.                                    (3.5)
```

This is genuine coefficient damping.  It is not yet a bound for
`zeta M_(Y,k)` and not a zero-free criterion.

## 4. Exact high-order Mellin transform

For fixed `k`, Perron's identity gives

```text
(1/(2 pi i)) integral_(c-i infinity)^(c+i infinity)
 y^z dz/z^(k+1)
 = [log y]^k/k!             (y>1).                      (4.1)
```

Consequently

```text
M_(x,k)(1/2+it)[log x]^k
 =k!/(2 pi i) integral_(1-i infinity)^(1+i infinity)
   x^z/[z^(k+1) zeta(1/2+it+z)] dz.                    (4.2)
```

Taking the same Mellin transform in `x` used by Bettin--Gonek yields

```text
H_(t,k)(w)
 :=integral_1^infinity
   M_(x,k)(1/2+it)[log x]^k x^(-w)dx

 =k!/[(w-1)^(k+1) zeta(w-1/2+it)].                     (4.3)
```

For `k=1`, this is the published factor

```text
1/[(w-1)^2 zeta(w-1/2+it)].                             (4.4)
```

The Bettin--Gonek auxiliary function contains a factor

```text
(w-1)^2 zeta(w-1/2+it),                                 (4.5)
```

chosen so that (4.4) cancels completely while a hypothetical target zero is
left as a simple pole.

For `k>1`, multiplying (4.3) by the unchanged auxiliary function instead
leaves

```text
k!/(w-1)^(k-1).                                         (4.6)
```

Therefore the shifted contour contains, in addition to the target pole,

```text
a pole at w=1 of order k-1.                             (4.7)
```

Its residue is a polynomial in `log x` of degree `k-2`.  It is not a small
error and it is not optional.  It is the exact term omitted by the apparent
shortcut.

## 5. The false carrier and exact exponent repayment

If the central pole (4.7) is incorrectly discarded, Stirling's formula gives
the normalized target carrier rate

```text
Phi(delta,alpha)
 =delta+alpha[log(alpha/delta)-1]                        (5.1)

 =alpha[delta/alpha-1-log(delta/alpha)]>=0,              (5.2)
```

where

```text
delta=Re(rho)-1/2>0.                                    (5.3)
```

The nonnegativity in (5.2) is the elementary inequality
`log x<=x-1`.  It does **not** make (5.1) a valid isolated lower bound,
because (4.7) is still present.

There is nevertheless an exact and revealing identity.  For
`0<alpha<1/2`,

```text
2 Phi(1/2,alpha)=chi(alpha).                             (5.4)
```

The high-order weight therefore repays its entire mollifier-only effective
length at the outer edge of the critical strip.

Suppose (3.5) holds.  On the interval

```text
alpha<=delta<=1/2,                                      (5.5)
```

`Phi(delta,alpha)` is increasing.  Hence

```text
2 theta Phi(delta,alpha)
 <=2 theta Phi(1/2,alpha)
 =theta chi(alpha)
 <=1.                                                    (5.6)
```

The ordinary Bettin--Gonek exponent comparison needs strict surplus beyond
`1`.  Thus even the **naive**, incomplete carrier has no exponent overlap
with the elementary mollifier-only mean-value range in the outer interval
(5.5).

This corrects the earlier false impression that there was a nonempty
high-order exponent corridor.

## 6. Why full kernel compensation does not repair it

One can remove (4.7) algebraically by replacing the original auxiliary ratio

```text
(w-1)^2/(w+1)^2
```

with a matching high-order ratio such as

```text
(w-1)^(k+1)/(w+1)^(k+1).                                (6.1)
```

Then the central pole disappears, but at `t=Im rho` the target residue pays
the denominator `(w_rho+1)^(k+1)`.  At exponent scale the resulting carrier
has the schematic rate

```text
Psi(delta,alpha)
 =delta+alpha[log(alpha/(2+delta))-1],                   (6.2)
```

which is strictly smaller than (5.1).

Equation (6.2) is not asserted to be an optimal auxiliary-kernel theorem.  It
shows why exact cancellation of the new center is not free: the analytic
factor used to remove it also suppresses the target.

More generally, partially cancelling (4.7) merely interpolates between:

1. retaining a large central residue polynomial which can cancel the target;
2. paying an exponentially small target multiplier.

Any claimed improvement must exhibit structure beyond this generic analytic
tradeoff.

## 7. Apparent paradox for `alpha>1/2`

For `alpha>1/2`, (2.4) and the classical second moment of zeta give a trivial
upper bound of natural size for `zeta M_(Y,k)`, uniformly in nominal
polynomial length.  If a direct extension of the first-order mollifier
criterion were valid without extra terms, this would prove RH immediately.

The paradox is resolved by (4.7): the first-order criterion is tied to the
linear logarithmic taper.  Its Mellin cancellation is exact only for `k=1`.
For growing `k`, the central residue polynomial changes with `T` and carries
the missing mass.  The published first-order theorem cannot be applied to
(1.1) merely by replacing the weight.

This is a useful sanity check for every future changing-order detector.

## 8. Surviving research direction

The proportional-order route is closed as a generic shortcut, but it leaves
a sharply defined coefficient-specific question.

Let

```text
P_(k,t)(log x)                                           (8.1)
```

be the complete residue polynomial generated at `w=1`, and let

```text
Z_(rho,k,t)(x)                                           (8.2)
```

be the target-zero carrier.  A new proof would have to establish a completed
estimate for

```text
Z_(rho,k,t)(x)+P_(k,t)(log x)+remaining contour,         (8.3)
```

not for `Z_(rho,k,t)` alone.

The next admissible tests are:

1. compute `P_(k,t)` exactly for small symbolic `k` and identify its generating
   function;
2. determine whether a fixed signed scale combination can annihilate the
   central polynomial without paying linear logarithmic support;
3. test that combination against the scale-filter support-cost no-go already
   present in the repository;
4. if it survives, derive its complete mollified second moment before any
   absolute values or sectorwise bounds are taken.

A generic finite-difference annihilator is expected to pay back its gain
through support or target attenuation.  Only an arithmetic identity coupling
`P_(k,t)` to the Möbius coefficients would constitute a new mechanism.

## 9. Implementation

The finite algebra and regression checks are in

```text
src/high_order_mollifier_shift.py
src/test_high_order_mollifier_shift.py.
```

The Lean file

```text
lean/rhbridge/RHBridge/HighOrderMollifierObstruction.lean
```

records the entropy nonnegativity and exact outer-edge repayment without
importing a zero-free theorem.

## 10. Literature boundary

The published Bettin--Gonek criterion and its 2026 automorphic extension use
the **linear** logarithmic mollifier

```text
1-log n/log N.                                          (10.1)
```

Their Mellin transform contains `(w-1)^(-2)`, exactly matching the auxiliary
factor `(w-1)^2`.  This note derives the higher-order transform (4.3) but does
not import a high-order zero-free criterion from the literature, because no
such criterion has been established here.

Primary references:

- S. Bettin and S. M. Gonek, *The theta=infinity conjecture implies the
  Riemann hypothesis*, Mathematika 63 (2017), 29--33.
- A. Dong, N. Wattanawanichkul, and A. Zaharescu, *The theta=infinity
  Conjecture and the Riemann Hypothesis for Automorphic L-functions*,
  arXiv:2605.24363, 2026.
