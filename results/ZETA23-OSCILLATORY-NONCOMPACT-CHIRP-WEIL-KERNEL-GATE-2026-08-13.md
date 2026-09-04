# Oscillatory noncompact chirp: Weil admissibility and the translated-carrier gate

**Date:** 2026-08-13

**Binary verdict:** **valid positive-definite Weil mechanism; no fixed strip.**

An exponential chirp genuinely defeats the literal noncompact prime-tail
divergence.  With a flat onset its autocorrelation decreases faster than
every exponential while its Laplace carrier is nonzero.  It does not,
however, compact-realize a prime-null causal Pick filter for free.  The
vertical transform has an unavoidable stationary-phase alias, and translating
two copies to obtain a signed off-axis carrier recreates the exact
`exp(L/2)` prime ledger.  Exact prime or pole interpolation forces the
normalized cross carrier to zero.  Only signed von Mangoldt cancellation of
strip strength remains open.

## 1. Exact sharp-onset autocorrelation

Assume `a>0`, `theta>0`, and put

```text
q(t)=1_(t>=0) exp(-a*t+i*exp(theta*t)),
R(u)=integral_R q(t+u)conj(q(t))dt.                         (1.1)
```

Then `q` is in `L2`, `R(0)=1/(2a)`, and `R(-u)=conj(R(u))`.
For `u>=0`, setting `x=exp(theta*t)` gives exactly

```text
R(u)=exp(-a*u)/theta * integral_1^infinity
 x^(-1-2a/theta) exp(i*(exp(theta*u)-1)*x)dx.              (1.2)
```

The sign of the phase must be reversed for `u<0`; omitting that reversal
would violate Hermitian symmetry and positive definiteness.

Let `c=exp(theta*u)-1` and `nu=2a/theta`.  Integration by parts at the
lower endpoint gives

```text
integral_1^infinity x^(-1-nu)e^(i*c*x)dx
 =e^(i*c)[i/c+(1+nu)/c^2+O_(a,theta)(c^(-3))].             (1.3)
```

Consequently

```text
R(u)=i/theta * exp(-(a+theta)u)
       exp(i*(exp(theta*u)-1))*(1+O(exp(-theta*u))).       (1.4)
```

Thus the absolute bilateral Laplace integral of `R` has the sharp strip
`|Re(s)|<a+theta`.  In particular, when

```text
a<1/2<a+theta,                                             (1.5)
```

the unshifted Guinand--Weil prime sum is absolutely convergent:

```text
sum_(n>=2) Lambda(n)/sqrt(n) |R(log n)| < infinity.        (1.6)
```

Positive definiteness is not conjectural: `R` is an `L2` autocorrelation,
and its real-frequency transform is `|Q(T)|^2>=0`.

## 2. Flat onset really removes the prime tail

Choose `chi in C^infinity(R)` with

```text
chi(t)=0 for t<=0,        chi(t)=1 for t>=1,
```

so `chi` is flat at the onset, and set

```text
q_chi(t)=chi(t)exp(-a*t+i*exp(theta*t)).                    (2.1)
```

For `u>=1`, the exact autocorrelation is

```text
R_chi(u)=exp(-a*u) integral_0^infinity
 chi(t)exp(-2a*t)
 exp(i*(exp(theta*u)-1)*exp(theta*t))dt.                   (2.2)
```

Every integration by parts in the phase gains
`(exp(theta*u)-1)^(-1)`.  Flatness kills the endpoint at zero and the
exponential envelope kills infinity.  Hence, for every integer `N>=1`,

```text
|R_chi(u)|<=C_N exp(-a*u)(exp(theta*u)-1)^(-N)
           =O_N(exp(-(a+N*theta)u)),                       (2.3)
```

and Hermitian symmetry gives the same estimate at `-infinity`.  Thus
`R_chi` has every exponential moment, its bilateral Laplace transform is
entire, and (1.6) holds with arbitrary reserve.  This is a genuine escape
from the mechanical noncompact-tail divergence, not a formal continuation.

The frequency-side regularity is finite, but sufficient.  Since `chi=1`
eventually,

```text
q_chi^(m) in L2(R)    iff    m*theta<a.                    (2.4)
```

The real spectral density nevertheless decreases like
`T^(-1-2a/theta)`, which is integrable for every `a>0`.  One may choose
`a` close to `1/2` and `theta` small enough to meet any fixed finite
regularity requirement while retaining (1.5), or pass from compact smooth
cutoffs to (2.1).  Thus regularity does not kill the proposal.

## 3. The Laplace carrier is nonzero

Write

```text
F(s)=integral_0^infinity q(t)exp(s*t)dt.                    (3.1)
```

It converges absolutely for `Re(s)<a`, conditionally for
`Re(s)<a+theta`, and repeated integration by parts supplies its entire
continuation.  For the sharp onset,

```text
F(s)=1/theta * integral_1^infinity
 x^(-1-(a-s)/theta)exp(i*x)dx.                             (3.2)
```

At the envelope boundary,

```text
F(a)=1/theta *[-Ci(1)+i*(pi/2-Si(1))] !=0.                (3.3)
```

A flat onset changes (3.2) by an entire compact-interval term.  Nonvanishing
is not automatic for every possible `chi`, but it persists for flat onsets
chosen sufficiently close to the sharp one.

Initially by Fubini, and then by analytic continuation, the autocorrelation
carrier is exactly

```text
K(s)=integral_R R(u)exp(s*u)du
    =F(s)conj(F(-conj(s))).                                 (3.4)
```

There is no hidden square: for real nonzero `s`, (3.4) need not be
`|F(s)|^2`.  It is nonetheless nonzero in the sharp model throughout
`|s|<a+theta`.  Indeed, for `mu=(a-s)/theta>-1`,

```text
integral_1^infinity x^(-1-mu)e^(i*x)dx
 =e^i/Gamma(1+mu) * integral_0^infinity
   t^mu e^(-t)*(t+i)/(t^2+1)dt.                            (3.5)
```

The last integral lies strictly in the first quadrant.  The common `e^i`
phase cancels between the two legs of (3.4), so

```text
Re K(s)>0       for real |s|<a+theta.                      (3.6)
```

Thus the centered chirp retains a carrier, but its carrier has the positive
sign; a translation or polarization is needed to turn it into a negative
test.

## 4. Stationary phase conserves a remote spectral alias

For fixed real `s` and `T->+infinity`, the phase in `F(s-i*T)` has its
stationary point at

```text
t_T=theta^(-1)log(T/theta).
```

Since `chi(t_T)=1`, ordinary one-dimensional stationary phase gives

```text
F(s-i*T)
 =sqrt(2*pi/(theta*T))*(T/theta)^(-(a-s)/theta)
   exp(i*Phi_T+i*pi/4)*(1+o(1)),                            (4.1)

Phi_T=T/theta-(T/theta)log(T/theta).
```

The conjugate autocorrelation leg has the opposite depth.  Therefore the
depth powers cancel exactly:

```text
K(s-i*T)
 =2*pi/(theta*T)*(T/theta)^(-2a/theta)*(1+o(1))>0.         (4.2)
```

The flat onset has made `R` superexponentially small but has not made its
vertical spectrum rapidly decreasing.  Equation (4.2) is the unavoidable
stationary alias and is another form of (2.4).  It is summable and hence does
not invalidate the Weil test; it does show that the apparent depth gain of
one leg is paid exactly by the other autocorrelation leg.

## 5. Translation recreates the half-power prime barrier

Let `T_L q(t)=q(t-L)` and form two causal lobes

```text
f=q+c*T_L q.                                               (5.1)
```

Their autocorrelation and Laplace transform factor are exactly

```text
R_f(u)=(1+|c|^2)R(u)+cR(u-L)+conj(c)R(u+L),                (5.2)
F_f(s)=F(s)(1+c*exp(sL)).                                  (5.3)
```

Since `R(L)` is negligible, the normalized cross coefficient is

```text
d=c/(1+|c|^2)+o(1).                                       (5.4)
```

At depth `0<alpha<1/2`, the growing selected cross carrier has size
`|d|exp(alpha*L)`.  On the prime side, the translated bump in (5.2) gives

```text
sum_n Lambda(n)/sqrt(n) |d*R(log n-L)|
 =(1+o(1))|d|exp(L/2)
   integral_R exp(y/2)|R(y)|dy                              (5.5)
```

at the continuum scale.  The integral is finite by (1.5), and by (2.3) in
the flat model.  Thus absolute estimation loses the exact factor
`exp((1/2-alpha)L)` that the construction was intended to remove.

Pointwise interpolation is worse.  The prime number theorem supplies
`p_L` with `log(p_L)-L=o(1)`.  If the complex row
`R_f(log p_L)` is forced to vanish, (5.2), `R(0)>0`, and (2.3) imply

```text
|d|=O_N(exp(-(a+N*theta)L))       for every N.             (5.6)
```

For the actual Hermitian prime row only the real part must vanish.  Choose
two fixed offsets `y_1,y_2` for which `R(y_1),R(y_2)` are not real-collinear,
and use primes at `L+y_j+o(1)`.  Such offsets exist: if `R` were real, its
spectral density would be even, contradicting the stationary tail (4.2) on
one frequency half-axis and rapid nonstationary decay on the other.  The
resulting real `2 x 2` system again gives (5.6).  Hence exact all-prime
interpolation kills the target cross carrier.

The pole rows impose the familiar sharp loss even without primes.  Put

```text
C(s)=1+c*exp(sL).
```

Either exact factor null at `s=1/2` or `s=-1/2` forces
`c=-exp(-L/2)` or `c=-exp(L/2)`, respectively.  In both cases

```text
|c|/(1+|c|^2)=1/(2*cosh(L/2)) asymp exp(-L/2),             (5.7)
```

so the depth-`alpha` cross is only
`O(exp(-(1/2-alpha)L))`.  Phase-only cancellation can retain a large `d`,
but then the signed prime remainder in (5.5) is untouched.

## 6. Why chirping cannot be bolted onto a causal Pick filter

There is a separate exact product obstruction.  Suppose a causal filter `g`
already carries a desired Pick zero set, and one convolves it with a chirped
packet `c` so that

```text
q=c*g,        Q(s)=C(s)G(s).                               (6.1)
```

This preserves the zeros of `G`, but Wiener--Khinchin gives

```text
R_q=R_c*R_g,
Laplace[R_q](s)=Laplace[R_c](s)Laplace[R_g](s).            (6.2)
```

If the slow boundary tail of `R_g` is represented by a pole or nonzero
boundary singularity at `s=lambda`, and the chirp factor is nonzero there
(as required to retain that carrier), (6.2) inherits the same singularity
and hence the same slow tail.  Accelerating it requires the chirp factor to
vanish to the needed order at `lambda`, which cancels or attenuates the
boundary carrier itself.  Conversely, pointwise chirp modulation can speed
an autocorrelation as in Section 2, but it does not preserve the Laplace
zeros of `G`.  One cannot obtain both operations for free.

## 7. Truth boundary

The exponential chirp is a legitimate and useful noncompact positive-
definite Weil kernel.  Flat onset really gives arbitrary prime-side decay,
and the boundary value (3.3) shows that this need not erase the carrier.

What fails is the proposed closure:

```text
prime-tail divergence                         REMOVED;
positive-definite Weil admissibility          PASSED;
nonzero boundary Laplace carrier              PASSED for explicit choices;
rapid vertical spectral decay                 FALSE by stationary phase;
absolute translated-prime closure             FAILS at exp(L/2);
exact prime or pole interpolation              KILLS the carrier;
target-conditioned signed von Mangoldt bound  OPEN and strip-strength;
uniform zero-free strip                        NOT PROVED.
```

This is a scoped no-go for flat-chirp tail acceleration plus ordinary
translation/interpolation.  It does not rule out a new signed arithmetic
identity that cancels (5.5) without absolute values; supplying that identity
is precisely the remaining hard theorem.
