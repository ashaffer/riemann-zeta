# Critical pole/main resonance and Mellin-scale filtering do not give a free escape

Status: exact pole--continuum cancellation, exact critical exponent and
same-lobe ledger, an affine reservoir criterion, and an exact Mellin-filter
residue theorem, 2026-08-12.  The deterministic pole/main pair supplies no
completed transverse power.  A raw-prime critical construction remains
possible only through the same carrier-sized centered-prime/collateral
angle already isolated elsewhere.  No zero-free strip is proved or
disproved.

## 1. Verdict

Two apparent loopholes survive a crude exponent comparison but not exact
recompletion.

First, take support `L=C log T`, lobe separation `D=d_*L`, and a hypothetical
zero of depth

```text
alpha=1/2-delta.                                     (1.1)
```

The selected cross carrier and the crude leading pole/main scale are

```text
K_zero=T^(C*d_*alpha+o(1)),
K_pm  =T^(C*d_*/2-1+o(1)).                          (1.2)
```

They tie at

```text
C*d_*delta=1                                        (1.3)
```

(`C*delta=1` when the full support separation is used).  At this equality
the pole row by itself can be transverse and sign-adjustable.  It is not,
however, an independent completed reservoir.  The `e^(y/2)` half of the
pole is exactly the continuum main term of the raw prime sum, with the
opposite sign in `Pole-Prime`.  They cancel as operators, not merely in
order of magnitude.  The remaining rational half is subpower, and on a
cross window near `D` it is exponentially decreasing.

One may instead impose cancellation of the **uncentered raw-prime** scalar
and deliberately leave the pole scalar negative.  At (1.3) this is
algebraically possible, but it is exactly the equation that the centered
actual-prime row equal minus the continuum main row at carrier scale.  No
current theorem gives the required projected lower bound, target angle, or
collateral control.  Thus equality is a genuine unresolved affine gate,
not a deterministic pole escape.

Second, a signed Mellin-scale filter acts on the selected zero residue and
on the corresponding completed arithmetic response by the **same exact
multiplier**.  A filter may kill the zeta pole while retaining every
nontrivial zero; `I-S_h` is an explicit example.  What remains is a signed
prime queue whose fixed-power bound is already zero-free-strip strength.  A
filter that annihilates the target pole of the completed arithmetic
transform has multiplier zero at that target and therefore deletes the
target residue as well.  Adaptive coefficients do not change this identity.

Consequently neither critical scaling nor scale averaging removes the
augmented actual-prime/collateral theorem.  They only repackage it.

## 2. Exact pole and continuum-main orientation

Use the repository correlation convention

```text
R_f(y)=integral f(u)*conj(f(u+y))du.                 (2.1)
```

After demodulation at the target ordinate `gamma`, write the surviving real
cross correlation on `y>0` as

```text
H(y)=Re[exp(i*gamma*y)
        *integral ell(u)*conj(r(u+y))du].            (2.2)
```

All arguments below apply before taking the real part as a complex scalar
identity.  The exact pole correlation is

```text
Pole_cross
 =4*integral H(y)*cosh(y/2)dy
 =2*integral H(y)*e^(y/2)dy
  +2*integral H(y)*e^(-y/2)dy.                      (2.3)
```

The raw prime cross term is

```text
Prime_cross
 =2*integral H(y)*e^(-y/2)d psi(e^y).               (2.4)
```

Split

```text
d psi(e^y)=e^y dy+d[psi(e^y)-e^y].                  (2.5)
```

The continuum part of (2.4) is exactly

```text
Main_cross=2*integral H(y)*e^(y/2)dy.               (2.6)
```

It is the first term of (2.3), with the same sign inside `Prime`.  Since the
completed form uses `Pole-Prime`, one obtains the operator identity

```text
Pole_cross-Prime_cross
 =Rat_cross-CenteredPrime_cross,                    (2.7)

Rat_cross
 =2*integral H(y)*e^(-y/2)dy,

CenteredPrime_cross
 =2*integral H(y)*e^(-y/2)
       d[psi(e^y)-e^y].                             (2.8)
```

Every orientation, conjugate, prime power, and both pole branches are
retained in (2.3)--(2.8).  In particular,

```text
Pole_leading-Main=0                                 (2.9)
```

exactly.  It is incorrect to treat their common upper bound as an extra
completed direction.

If the cross-difference window is concentrated at `y=D+O(w)`, then

```text
abs(Rat_cross)
 <=2*e^(-D/2+O(w))*integral abs(H(y))dy.            (2.10)
```

Even without localization, `abs(Rat_cross)` is bounded by a polynomial
norm of the packet.  It cannot match the fixed-power carrier in (1.2).
The archimedean cross term is likewise polynomial at absolute frequency
`gamma asymp T` under the audited endpoint hypotheses.

## 3. What raw-prime cancellation means at the critical scale

Write

```text
Prime_cross=Main_cross+CenteredPrime_cross.         (3.1)
```

If one imposes the one-real equation

```text
Prime_cross=0,                                      (3.2)
```

then exactly

```text
CenteredPrime_cross=-Main_cross,                    (3.3)

Pole_cross-Prime_cross
 =Rat_cross+Main_cross.                             (3.4)
```

Thus a negative `Main_cross` can indeed remain as a negative pole cross
after the raw-prime term has been canceled.  There is no sign prohibition:
the pole form `2*Re(A_+*conj(A_-))` is indefinite, and the real part of a
nonzero pole cross row can be changed in either direction by changing one
packet quadrature.

But (3.3) is not supplied by the deterministic continuum.  It is a
carrier-sized assertion about the **actual centered von Mangoldt row**.
The completed explicit formula gives

```text
Rat-CenteredPrime+Arch
 =SelectedZero+CollateralZero.                      (3.5)
```

Combining (3.3)--(3.5), any retained selected carrier is balanced by
`Main_cross` plus the collateral.  To use the main row as the carrier one
must separately prove that the collateral is subcarrier; otherwise it may
perform the entire balance itself.  Critical equality removes the power
inequality between the two rows, but proves neither their projected angle
nor the sign/cost of the collateral.

## 4. Exact affine pole-reservoir criterion

The critical issue can be stated without estimates.  Fix a seed `r` and let
`E_-` be the free-lobe space after endpoint and support restrictions.  Let

```text
A*ell=b                   positive-zero equations,
a                         selected target row,
g_pm                      projected pole/main row.  (4.1)
```

Choose one solution `ell_0` of the positive equations and require a
correction not to change the selected target value.  Put

```text
S=ker A,
H=S intersect a^perp,
p_H=P_H*g_pm.                                      (4.2)
```

For complex cancellation, a prescribed pole/main correction `Delta` is
possible while preserving both the positive nulls and the target exactly
if and only if

```text
p_H!=0.                                             (4.3)
```

The minimum added norm is

```text
abs(Delta)/norm(p_H).                               (4.4)
```

For the minimal one-real equation, (4.3)--(4.4) hold in the realification
with the corresponding real Riesz projection.  Its sign is free whenever
that projection is nonzero.

In the unconstrained Paley--Wiener space the target and pole rows are
genuinely different exponentials.  In demodulated coordinates their
functionals have kernels

```text
target:       e^(+-alpha*t),
pole:         e^((+-1/2-i*gamma)*t).                (4.5)
```

For `gamma!=0` they are linearly independent on every nonempty interval.
For a seed with a nonzero pole row, finite interpolation therefore gives
`p_H!=0` before quantitative packet, jet, and positive-row restrictions.
This proves that no universal sign or algebraic alignment no-go exists at
the critical scale.

The needed statement is quantitative.  At (1.3), a subpower-cost correction
requires

```text
norm(p_H)>=K_zero*T^(-o(1))                         (4.6)
```

in the actual coefficient normalization.  Existing pole estimates give
only an **upper** bound of this order before projection.  They do not give
(4.6), and projection through endpoint jets and all positive rows can make
`p_H` arbitrarily smaller.  This is the same augmented-angle gate in a
rank-two pole coordinate system.

For the actual raw-prime equation one must replace `g_pm` by

```text
g_raw=g_main+g_centered.                             (4.7)
```

The same projection formula is exact with `P_H*g_raw`, including its affine
offset at `ell_0`.  A lower bound for `P_H*g_pm` does not give a lower bound
for `P_H*g_raw`: the centered actual-prime row can cancel or align with it.
Thus (4.6) is necessary for using the deterministic pole/main direction at
subpower cost, but it is not sufficient for raw-prime cancellation.

## 5. Critical same-lobe prime cost

Let the active free-lobe diameter be `aL`, while the selected lobe
separation is `d_*L`.  The elementary square-root same-lobe prime scale is

```text
K_same=T^(C*a/2+o(1)).                              (5.1)
```

At criticality `C*d_*delta=1`,

```text
K_zero
 =T^(C*d_*/2-1+o(1)).                              (5.2)
```

The selected carrier has a strict power margin over (5.1) exactly when

```text
C*d_*alpha>C*a/2

iff a<2*alpha*d_*=d_*(1-2*delta)

iff C*(d_*-a)/2>1.                                 (5.3)
```

Thus the critical resonance does not automatically lose to the same-lobe
prime cost.  In the asymmetric range `a>1/2`, `d_*<2/3`, a nonempty limiting
window requires

```text
delta<1/8                                           (5.4)
```

as `a` tends down to `1/2` and `d_*` tends up to `2/3`.  Equality has no
power margin.  This recovers the formal `7/8` threshold but does not prove
it: (4.6), the actual centered-prime equation (3.3), and the collateral/full
form cost are still missing.  For larger `C`, the transition-range KMT and
ordinary separated-frequency mean-square inputs used at `X=T^(1+o(1))`
also no longer apply automatically.

## 6. Exact Mellin multiplier for scale filters

On logarithmic scale let

```text
M=sum_(n>=2) Lambda(n)*delta_(log n),
P=e^u du,
nu=M-P.                                             (6.1)
```

For `h>=0`, define the pole-normalized shift

```text
S_h=e^h*tau_h.                                      (6.2)
```

Its Laplace transform is

```text
L(S_h mu)(s)=e^((1-s)h)*L(mu)(s).                  (6.3)
```

Let `a` be any finite signed or complex measure of scale shifts and put

```text
A_a=integral S_h da(h),
m_a(s)=integral e^((1-s)h)da(h).                   (6.4)
```

Then exactly

```text
L(A_a M)(s)=m_a(s)*[-zeta'(s)/zeta(s)],

L(A_a nu)(s)
 =m_a(s)*[-zeta'(s)/zeta(s)-1/(s-1)].              (6.5)
```

For a finite filter, `m_a` is the exponential polynomial

```text
m_a(s)=sum_j a_j*e^((1-s)h_j).                     (6.6)
```

If `rho` is a zero of multiplicity `m_rho`, the residue at `rho` in (6.5)
is multiplied by exactly

```text
m_a(rho).                                           (6.7)
```

This proves the promised same-factor statement.  The factor multiplying
the selected spectral residue is the factor multiplying its completed
arithmetic pole.  It is not affected by whether the coefficients in `a`
were chosen in advance or adaptively after fixing `T` or `rho`.

### Theorem 6.1 (filter alternative)

For every scale filter (6.4) and target zero `rho`, exactly one of the
following holds:

1. `m_a(rho)=0`; the filter deletes that target residue.
2. `m_a(rho)!=0`; the filtered completed arithmetic transform retains a
   pole at `rho` with residue multiplied by `m_a(rho)`.

In the second case, any bound that makes the filtered prime--pole transform
holomorphic in a half-plane containing `rho` is impossible.  Quantitatively,
a uniform cumulative bound `O(e^(sigma U))` with
`sigma<Re(rho)` would analytically continue its Laplace transform through
`rho`, contradicting (6.7).  Such a bound is therefore already
zero-free-strip strength.

## 7. Pole-killing filters retain the zero but not a small prime side

The uncentered zeta pole is killed exactly by

```text
m_a(1)=integral da(h)=0.                             (7.1)
```

This condition need not kill a nontrivial zero.  For example,

```text
A=I-S_h,
m(s)=1-e^((1-s)h),             h>0.                 (7.2)
```

satisfies `m(1)=0`.  If `rho` is nontrivial with `Re(rho)<1`, then

```text
abs(e^((1-rho)h))=e^((1-Re(rho))*h)>1,              (7.3)
```

so `m(rho)!=0`.  It faithfully retains every nontrivial zero.

The continuous exponential-delay filter gives another exact example:

```text
m_lambda(s)=(s-1)/(s+lambda-1),       lambda>1.      (7.4)
```

It has no zero in `Re(s)>0` except `s=1`.  Its arithmetic output is a
bounded signed Riesz ramp, not zero.  A fixed-power one-sided bound for that
ramp implies the corresponding zero-free half-plane.  Hence pole removal is
possible, but simultaneous removal of the prime difficulty is not free.

Finite filters can also have arbitrarily small vertical response because
of simultaneous phase recurrence.  If an adaptive filter normalizes such
a near-zero response back to one at `rho`, its coefficient variation or
inverse condition number grows by `1/abs(m_a(rho))`; this cost must be
included in the same-lobe and endpoint ledger.

## 8. Signed scale averages versus coherent filtered witnesses

Two operations must not be conflated.

### 8.1 Signed averages of Weil forms

A formal sum

```text
sum_j a_j Q(f_j)                                    (8.1)
```

with some `a_j<0` may cancel pole and prime terms.  Its negativity does not
imply that any `Q(f_j)` is negative.  It is not a Weil witness.  With all
`a_j>=0`, it is a PSD ensemble and falls under the multi-witness SDP; the
aligned completed mirror carriers have one sign and cannot cancel.

### 8.2 One coherent scale-filtered witness

Let

```text
F=sum_j a_j T_(h_j)f.                               (8.2)
```

Then all quadratic cross-scale terms are present.  If `T_a` denotes the
linear filter on the packet space, the completed operator identity becomes

```text
T_a^* K_comp T_a=T_a^* K_zero T_a.                 (8.3)
```

On a scale-eigen evaluation row at `rho`, the residue amplitude is
multiplied by `m_a(rho)` and its square contribution by
`abs(m_a(rho))^2` (with the reflected member carrying its corresponding
reflected multiplier).  The arithmetic side receives the identical
congruence.  Therefore a coherent filter cannot annihilate the completed
arithmetic operator while leaving an unmatched selected block.  If the
selected block survives and the filtered arithmetic scalar cancels, other
zero blocks or boundary terms must cancel it at the same scale.

Adaptive cancellation at one cutoff is not an exception.  It is one scalar
equation at one `U`; if `m_a(rho)!=0`, the exact explicit formula says that
the retained target exponential is balanced there by other zeros or a
boundary/collateral term.  Uniformly bounding those terms is precisely the
missing augmented theorem.

## 9. Focused no-go and remaining live statement

The exact conclusions are:

1. The critical pole and continuum main rows cancel identically in the
   completed form.  Their common scale at `C*d_*delta=1` is not a free
   transverse completed reservoir.
2. Raw-prime cancellation can leave the pole/main scalar as the negative
   carrier only if the actual centered-prime row satisfies (3.3) at
   carrier scale.  Its subpower-cost affine criterion is (4.6), and its
   same-lobe margin is (5.3).
3. Every Mellin-scale filter multiplies a target residue and its completed
   arithmetic pole by the same `m_a(rho)`.  Killing one kills the other.
4. Killing only the zeta pole while retaining the target is possible, but
   the surviving signed prime estimate is itself strip-strength.
5. Signed averages with negative coefficients are not negative-witness
   certificates; coherent filters retain all cross terms and return to the
   operator identity.

The only live critical-scale theorem is therefore zeta-specific: prove a
uniform carrier-scale lower bound for the projected actual centered-prime
row together with a favorable target angle and subcarrier collateral/full
form cost.  This is not implied by the equality of exponents, and no current
repository result proves it.

Related exact inputs:
[`ZETA23-AGGREGATE-CROSS-PRIME-ROW-AUDIT-2026-08-11.md`](ZETA23-AGGREGATE-CROSS-PRIME-ROW-AUDIT-2026-08-11.md),
[`ZETA23-ENDPOINT-PACKET-PRIME-FORM-THEOREM-CARD-2026-08-11.md`](ZETA23-ENDPOINT-PACKET-PRIME-FORM-THEOREM-CARD-2026-08-11.md),
[`ZETA23-MULTIWITNESS-MULTISCALE-AGGREGATE-CANCELLATION-AUDIT-2026-08-12.md`](ZETA23-MULTIWITNESS-MULTISCALE-AGGREGATE-CANCELLATION-AUDIT-2026-08-12.md),
and
[`R95-SIGNED-MULTISCALE-QUEUE-CYCLE-GATE.md`](R95-SIGNED-MULTISCALE-QUEUE-CYCLE-GATE.md).
