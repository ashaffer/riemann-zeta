# Third theta tail: exact cone, adversarial scan, and structural no-go

Status: **not proved and not falsified for the actual theta kernel**.  The
condition `S_(3,T)(P)>=0` numerically survives a rescaled scan through
`T=1000`, but its endpoint is the global first Laguerre inequality and a
positive-inverse Laguerre--Polya countermodel proves that the condition is
theta-specific, not a generic consequence of real-rootedness or standard
Hermite--Biehler interlacing.  No zero-free strip is proved here.

Date: 2026-08-13.

## 1. Exact target and its strength

Let `Phi` be the even Rodgers--Tao theta kernel and put

```text
f_T(u)=Phi(u)exp(-i*T*u),
S_(3,T)(P)=1/2 double_integral_R2
             (|u-v|-P)_+^2 f_T(u)f_T(v)du dv.             (1.1)
```

This is the first integer tail not falsified in the preceding transport
sprint.  It satisfies

```text
S_3'(P)=-S_2(P),   S_3''(P)=S_1(P),   S_3'''(P)=-h_T(P). (1.2)
```

For `w(P)=sinh(alpha*P)sinh(eta*P)`, three integrations by parts give

```text
integral_0^infinity w(P)h_T(P)dP
 =2*alpha*eta*S_(3,T)(0)
  +integral_0^infinity w'''(P)S_(3,T)(P)dP.               (1.3)
```

Both coefficients on the right are positive.  Thus global third-tail
positivity would prove the complete theta detector, not merely a soft model
inequality.

At the endpoint,

```text
S_(3,T)(0)=Z'(T)^2-Z(T)Z''(T),
Z(T)=xi((1-i*T)/2)/4.                                    (1.4)
```

Consequently the proposal contains the global first Laguerre inequality for
the completed zeta function.  This is an RH-strength gate.  It must not be
described as an elementary consequence of positivity of `Phi`.

The certified failure `S_(2,97.2)(0)<0` is locally favorable rather than
fatal for the promoted tail: by (1.2), it says that `S_(3,97.2)` initially
increases from its positive Laguerre endpoint.  It gives no global control
after that initial interval.

## 2. A new exact positive-density formulation

Set `w=u+v` and `d=u-v` in (1.1), and define

```text
B_P(w)=1/4 integral_R (|d|-P)_+^2
       Phi((w+d)/2)Phi((w-d)/2)dd.                        (2.1)
```

Then `B_P` is even, nonnegative, and rapidly decreasing, and the change of
variables gives the exact identity

```text
S_(3,T)(P)=integral_R B_P(w)exp(-i*T*w)dw.                (2.2)
```

Therefore

> `S_(3,T)(P)>=0` for every real `T` and every `P>=0` if and only if every
> member of the explicit family `B_P` is positive definite.

At `P=0`, (2.1) is

```text
B_0(w)=1/2 integral_R (2u-w)^2 Phi(u)Phi(w-u)du,          (2.3)
```

whose Fourier transform is exactly the Laguerre expression (1.4).  The
third-tail proposal is thus a continuum of **diagonal-excised Laguerre
cones**: the known endpoint cone is only its first member.

The `P` evolution is also exact:

```text
partial_P B_P(w)=-1/2 integral_(|d|>P)(|d|-P) Phi_+ Phi_- dd,
partial_P^2 B_P(w)=1/2 integral_(|d|>P) Phi_+ Phi_- dd,
partial_P^3 B_P(w)=-Phi((w+P)/2)Phi((w-P)/2),             (2.4)
```

where `Phi_+ Phi_-` abbreviates the product in (2.1).  Thus `B_P` has the
right pointwise third-order tail monotonicity automatically.  The missing
statement is transverse to it: positive definiteness in the independent
`w` variable.  This separates the real content from the already positive
tail calculus.

This formulation also blocks a tempting generic proof.  Relative to the
quadratic difference weight at `P=0`, excision multiplies each pair by

```text
m_P(d)=(1-P/|d|)_+^2.                                    (2.5)
```

For `P>0`, this multiplier has `m_P(0)=0` but is nonzero elsewhere.  It
cannot be positive definite, since every positive-definite function obeys
`|m_P(d)|<=m_P(0)`.  Hence the passage `B_0 -> B_P` cannot be justified by a
positive-definite Schur multiplier or a standard Schoenberg mixture.  Any
proof must use a compensating identity special to the full modular theta
sum.

## 3. Exact Laguerre--Polya countermodel

The desired sign is not structurally generic, even if one assumes all the
obvious one-variable positivity properties.  Let

```text
mu = convolution_(a in {1,3,4}) (delta_(-a)+delta_a)/2.  (3.1)
```

It is a positive symmetric probability measure, with support and masses

```text
x       -8   -6   -2    0    2    6    8
mu(x)   1/8  1/8  1/8  1/4  1/8  1/8  1/8.
```

Its transform is

```text
F(T)=cos(T)cos(3T)cos(4T),                               (3.2)
```

so `F` is positive definite and belongs to the Laguerre--Polya class.  Apply
the atomic version of (1.1).  At `T=pi/2` and `P=7`, grouping by the distance
`|u-v|` gives the following exact contributions:

```text
distance       8       10       12       14       16
contribution   3/32   -9/32     25/64   -49/32    81/64.
```

Their sum is

```text
S_3^mu(pi/2,7)=-1/16.                                   (3.3)
```

This is an exact rational falsifier, not floating-point evidence.  Perturb
the scale `3` by a sufficiently small irrational number.  The strict
negative sign persists by continuity, while the three cosine zero sets
become disjoint and every zero of the product is simple.  Convolving the
measure with a sufficiently narrow Gaussian makes its inverse Fourier
density positive and smooth, multiplies (3.2) by a Laguerre--Polya Gaussian
factor, and again preserves (3.3) by continuity.

Thus all of the following remain insufficient for third-tail positivity:

```text
positive inverse Fourier measure,
positive definiteness of the transform,
Laguerre--Polya real-rootedness,
simple real zeros and derivative interlacing,
Gaussian smoothing.
```

In particular, `S_3(P,T)>=0` does not reduce to the standard first Laguerre
or Hermite--Biehler criterion.  Its endpoint is that criterion; the positive
`P` family is strictly additional structure.

## 4. Rescaled completed-xi scan

Direct tensor quadrature develops an absolute error floor long before the
true completed transform at large height.  The reproducible scout
`results/probe_theta_s3_fast_grid.py` instead uses the exact integrated
Turan formula

```text
S_(3,T)(P)=L(T)-(2/pi)integral_0^infinity
 [Z(T)^2-Z(T+x)Z(T-x)]sin(P*x)/x^3 dx,                   (4.1)
L(T)=Z'(T)^2-Z(T)Z''(T),
```

and rescales

```text
Ztilde(t)=exp(pi*t/8)Z(t).                               (4.2)
```

For `x<=T`, the two gamma exponentials in the product cancel the common
factor `exp(-pi*T/4)` exactly.  For `x>T`, the normalized product acquires
only

```text
exp(-pi*(x-T)/4).                                        (4.3)
```

This prevents underflow near `T=960`.  Arb evaluates the individual
completed-xi samples at 30 decimal digits; their midpoints feed a uniform
double grid and a DST-I evaluates every frequency

```text
P=k*pi/W,   W=T+45.                                      (4.4)
```

The scan used

```text
0<T<=1000,
union of two T lattices with spacing 1/4 (net offset spacing 1/8),
dx=0.025,
0<=P<=log(1+T)+3.
```

It found no scale-separated negative.  Every apparent negative was at most
about `1.4e-9` of the natural normalized scale and occurred where `S_3` had
already decayed into the subtractive quadrature floor.  Restricting to
`P<=1.2` reduced that floor to about `4e-10`; restricting to `P<=0.5` gave
strictly positive values, with the smallest sampled margin about `8.4e-7`
of the natural scale.

Representative arbitrary-precision reruns of apparent grid negatives give

```text
(T,P)=(2.5,0.739198271):
  S_3=+4.49697247217205333628287696345...e-13,

(T,P)=(2.5,1.18271723):
  S_3=+9.03750962851758189874510112...e-30,

(T,P)=(5,1.72787596):
  S_3=+5.6345931458834725212950...e-37.                  (4.5)
```

Changing cutoff and precision showed why the raw negative signs were not
credible.  No apparent negative survived to the stage at which an Arb
interval integration would be warranted.  The Arb use in the broad scan is
only for accurate transform samples; (4.4) itself is not an interval proof.

At the previously adverse second-tail height, direct high-precision values
remain positive:

```text
S_(3,97.2)(0)   =1.69196329284415989...e-29,
S_(3,97.2)(0.2)=1.7071660672...e-29,
S_(3,97.2)(0.8)=2.1993566418...e-30,
S_(3,97.2)(1.0)=5.0807658647...e-32.                    (4.6)
```

These computations establish **numerical survival only**.  They neither
prove the endpoint Laguerre inequality nor exclude a narrow negative pocket
beyond the scan.

## 5. Modular-orbit audit

The positive-density formulation (2.1) identifies exactly what a modular
proof would have to do: prove positive definiteness after deleting all theta
pairs with `|u-v|<=P` and tapering the remainder quadratically.

Finite or termwise modular grouping cannot supply this uniformly.  At
`P=0` it specializes to the previously audited Laguerre density, where the
dominant individual theta summand and the first finite swap orbits are
indefinite.  Their strict negative values persist for sufficiently small
positive `P` by continuity.  The all-order cancellation of odd boundary
jets also occurs only after the complete modular theta sum is restored.

Thus the sole modular version not already contradicted is a fully global
two-dimensional Poisson identity that factorizes the complete `B_P` family
at once.  Merely regrouping finitely many lattice pairs, invoking positivity
of `Phi`, or naming the full sum one modular orbit does not provide the
needed positive-definite square root.

## 6. Verdict and next exact gate

The attack yields a sharper description but no theorem of positivity:

```text
actual theta S_3 through T=1000       numerically survives
global proof of S_3                   OPEN
endpoint first Laguerre inequality   OPEN / RH-strength
generic LP or HB implication         EXACTLY FALSE
finite modular-orbit factorization   CLOSED
full Poisson factorization of B_P    logically open
```

The next admissible step is not another broad positivity analogy.  It is one
of the following two concrete tasks:

1. derive a full-Poisson representation of `B_P` whose Fourier transform is
   a manifest square for every `P`; or
2. use interval arithmetic on a targeted candidate generated by a
   higher-resolution, rescaled scan near a completed-zeta zero cluster.

Until one of those succeeds, `S_3>=0` should remain a high-risk exact
conjecture, not a claimed route to a strip.
