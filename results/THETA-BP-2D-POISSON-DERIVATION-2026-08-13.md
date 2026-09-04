# The diagonal-excised theta density: full 2D Poisson formula and orbit obstruction

Status: exact analytic derivation.  This note gives a convergent polar
subtraction, the full two-dimensional Poisson formula, and an exact no-go for
the natural orbitwise Gram interpretation.  It does **not** decide whether the
complete density is positive definite.

Date: 2026-08-13.

## 1. Normalization and polar subtraction

Use the Fourier convention

```text
fhat(T)=integral_R f(u) exp(-i*T*u)du
```

and put

```text
theta(t)=sum_(n in Z) exp(-pi*n^2*t),
Theta(u)=exp(u) theta(exp(4u)).                          (1.1)
```

Jacobi inversion gives `Theta(-u)=Theta(u)`.  The Rodgers--Tao kernel is

```text
Phi(u)=(Theta''(u)-Theta(u))/16
      =sum_(n>=1) [2*pi^2*n^4*exp(9u)-3*pi*n^2*exp(5u)]
                    exp(-pi*n^2*exp(4u))                 (1.2)
```

for `u>=0`, extended evenly.  Define the polar-subtracted theta function

```text
R(u)=Theta(u)-2*cosh(u).                                 (1.3)
```

Then `R` is even and smooth, and every derivative is `O(exp(-abs(u)))`.
Moreover

```text
Phi=(D^2-1)R/16.                                        (1.4)
```

If

```text
f(T)=Phihat(T)=xi((1-i*T)/2)/4,
s=(1-i*T)/2,
```

then the exact Fourier transform of the subtraction is

```text
Rhat(T)=-16*f(T)/(1+T^2)
       =(1/2) pi^(-s/2) Gamma(s/2) zeta(s).              (1.5)
```

The second equality uses `s(s-1)=-(1+T^2)/4`.  In particular, the polar
subtraction has introduced no unspecified constant or contact term.

## 2. A safe differential representation of `B_P`

Set

```text
x=(w+d)/2,             y=(w-d)/2,
C(w,d)=R(x)R(y),
g_P(d)=(abs(d)-P)_+^2.                                  (2.1)
```

Since `partial_x=partial_w+partial_d` and
`partial_y=partial_w-partial_d`, (1.4) gives

```text
Phi(x)Phi(y)=(1/256) L C(w,d),                           (2.2)

L=[1-(partial_w+partial_d)^2][1-(partial_w-partial_d)^2]
 = (partial_w^2-partial_d^2)^2
   -2(partial_w^2+partial_d^2)+1.                       (2.3)
```

Consequently

```text
B_P(w)=(1/1024) integral_R g_P(d) L C(w,d)dd.            (2.4)
```

Unlike the unsubtracted product `Theta(x)Theta(y)`, `C` and all of its
derivatives decay in `d`, so integrations by parts in (2.4) are legitimate.
Let

```text
A_P(w)=integral_R g_P(d)C(w,d)dd,
E_P(w)=integral_(abs(d)>P) C(w,d)dd.                     (2.5)
```

The distributional identities

```text
g_P''=2*1_(abs(d)>P),
g_P''''=2[delta'_P-delta'_(-P)]                          (2.6)
```

and the evenness of `C` in `d` yield the exact formula

```text
B_P(w)=(1/1024){
          (partial_w^2-1)^2 A_P(w)
          -4(partial_w^2+1)E_P(w)
          -4 partial_d C(w,P)
        }.                                              (2.7)
```

At `P=0`, the last term vanishes.  For `P>0` it is the irreducible excision
edge term

```text
partial_d C(w,P)
 =(1/2)[R'((w+P)/2)R((w-P)/2)
          -R((w+P)/2)R'((w-P)/2)].                      (2.8)
```

Thus even after the polar bulk is regularized, the truncation leaves an
exact Wronskian-type cross term rather than a square.

## 3. Full two-dimensional theta and Poisson formula

The unsubtracted product is the determinant-one rectangular theta series

```text
M(w,d)=Theta((w+d)/2)Theta((w-d)/2)
      =exp(w) sum_(m,n in Z)
         exp{-pi*exp(2w)[m^2 exp(2d)+n^2 exp(-2d)]}.     (3.1)
```

Two-dimensional Poisson summation, with determinant `exp(4w)`, gives

```text
M(w,d)=exp(-w) sum_(r,s in Z)
         exp{-pi*exp(-2w)[r^2 exp(-2d)+s^2 exp(2d)]}
      =M(-w,d).                                         (3.2)
```

There is no missing power of `pi` in (3.2).  Write

```text
theta_+       =theta(exp( 2(w+d))),
theta_-       =theta(exp( 2(w-d))),
theta_tilde_+ =theta(exp(-2(w+d))),
theta_tilde_- =theta(exp(-2(w-d))).                     (3.3)
```

Expanding the two polar subtractions in `C=R(x)R(y)` and applying the
one-dimensional Jacobi formula to the cross terms gives the full
primal/dual inclusion--exclusion identity

```text
C(w,d)=M(w,d)
 -exp(w)[theta_+ + theta_-]
 -exp(-w)[theta_tilde_+ + theta_tilde_-]
 +exp(w)+exp(-w)+exp(d)+exp(-d).                         (3.4)
```

The terms in (3.4) must be kept together: individually they have polar
growth, whereas their displayed combination decays.

For example, in the primal chamber `w>=abs(d)`, (3.4) becomes the absolutely
convergent formula

```text
C(w,d)= exp(w)(theta_+-1)(theta_--1)
        -exp(d)(theta_+-1)
        -exp(-d)(theta_--1)
        +exp(-w).                                       (3.5)
```

This displays, in order,

```text
nonzero-by-nonzero 2D orbit     coefficient +1,
first one-axis cross orbit      coefficient -1,
second one-axis cross orbit     coefficient -1,
polar corner                    coefficient +1.         (3.6)
```

In the outer chamber `d>=abs(w)`, put

```text
a=(d+w)/2, b=(d-w)/2,
U_a=theta(exp(4a))-1, U_b=theta(exp(4b))-1.
```

Then the corresponding formula is

```text
C(w,d)=exp(d)U_a U_b-exp(w)U_a-exp(-w)U_b+exp(-d).       (3.7)
```

Equations (3.5) and (3.7) isolate the exact cross-orbit obstruction.  The
negative one-axis sectors are not optional estimates; they are the
inclusion--exclusion terms that make the full modular completion finite.

For fixed `d`, let

```text
Q_d(m,n)=m^2 exp(2d)+n^2 exp(-2d),
Z_d(s)=sum_((m,n) != (0,0)) Q_d(m,n)^(-s).               (3.8)
```

The polar-subtracted two-dimensional series has the exact Mellin--Fourier
form

```text
integral_R [M(w,d)-2cosh(w)]exp(-i*T*w)dw
 = (1/2) pi^(-s) Gamma(s) Z_d(s),
s=(1-i*T)/2,                                            (3.9)
```

where the right side is the analytically continued completed Epstein zeta
function.  Indeed, after `t=exp(2w)`, the left side is

```text
(1/2) integral_0^infinity
 t^(s-1)[theta_Q(t)-1-t^(-1)]dt.                        (3.10)
```

The exponent `Re(s)=1/2` is not an absolutely summable lattice exponent in
dimension two.  Hence (3.9) cannot be rearranged freely into positive
lattice pieces; the polar and one-axis terms in (3.4) are part of the
regularization.

## 4. Absolutely convergent theta series for `B_P`

For `a>=0`, define the individual positive-index summand

```text
phi_n(a)=pi*n^2*exp(5a)[2*pi*n^2*exp(4a)-3]
          exp(-pi*n^2*exp(4a)).                         (4.1)
```

Then `Phi(a)=sum_(n>=1)phi_n(a)`.  Evenness in `d` and in `Phi` gives the
fully convergent double-theta representation

```text
B_P(w)=(1/2) sum_(m,n>=1) integral_P^infinity (d-P)^2
  phi_m(abs(w+d)/2) phi_n(abs(w-d)/2)dd.                 (4.2)
```

This formula is safe for termwise numerical or analytic work.  It is not a
Gram decomposition.  In fact every `phi_n(a)` in (4.1) is positive for
`a>=0`, but positive pointwise summands do not imply positive definiteness in
`w`.  The even extension of an individual summand has a cusp at zero: with
`z=pi*n^2`,

```text
phi_n'(0)=z(-8z^2+30z-15)exp(-z),                       (4.2a)
```

which is nonzero.  More generally, if the first nonzero odd boundary jet of
a finite theta grouping is `a=psi^(2k+1)(0)`, its cosine transform has

```text
H(T)=2*(-1)^(k+1)*a*T^(-2k-2)+O(T^(-2k-4)),
H'(T)^2-H(T)H''(T)
 =-(2k+2)[2a]^2*T^(-4k-6)+O(T^(-4k-8))<0.              (4.2b)
```

Thus finite theta-orbit groupings cannot furnish even the `P=0` Gram unless
all odd boundary jets cancel.  That cancellation is an infinite modular
cross-orbit identity.

For completeness, the outer chamber has a closed incomplete-gamma form.
For `w>=0`, put

```text
D=max(P,w),
Q_mn(w)=m^2 exp(2w)+n^2 exp(-2w),
J_k(Q;D,P)=integral_D^infinity (d-P)^2 exp(kd)
                              exp(-pi*Q*exp(2d))dd.      (4.3)
```

Then

```text
J_k(Q;D,P)
 =(1/8)[(partial_s-2P)^2
        {(pi*Q)^(-s) Gamma(s,pi*Q*exp(2D))}]_(s=k/2),   (4.4)
```

and the `d>=D` contribution to (4.2) is

```text
(1/2) sum_(m,n>=1) {
  4*pi^4*m^4*n^4 J_9
 -6*pi^3[m^4*n^2 exp(2w)+m^2*n^4 exp(-2w)]J_7
 +9*pi^2*m^2*n^2 J_5
}.                                                       (4.5)
```

All `J_k` in (4.5) have the common first argument `Q_mn(w)` and the common
last arguments `(D,P)`.  If `P<w`, the remaining finite interval `P<d<w`
is an incomplete Bessel integral with exponent

```text
-pi*exp(2w)[m^2 exp(2d)+n^2 exp(-2d)],                  (4.6)
```

on which the 2D Poisson identity (3.2) acts directly.

## 5. Exact Fourier geometry and why it is not a square

The two-dimensional Fourier transform of the regularized product is

```text
F_(w,d) C(T,lambda)
 =2 Rhat(T+lambda)Rhat(T-lambda).                        (5.1)
```

The multiplier of `L` is

```text
[1+(T+lambda)^2][1+(T-lambda)^2].                       (5.2)
```

Using (1.5), the polar denominators cancel exactly and yield

```text
F_(w,d){Phi((w+d)/2)Phi((w-d)/2)}
 =2 f(T+lambda)f(T-lambda).                             (5.3)
```

Thus, in tempered-distribution notation,

```text
Bhat_P(T)=(1/(4*pi)) <ghat_P(lambda),
                         f(T+lambda)f(T-lambda)>.        (5.4)
```

For `lambda != 0`, the exact transform of the tail weight is

```text
ghat_P(lambda)=4 sin(P*lambda)/lambda^3.                 (5.5)
```

At `P=0`, `ghat_0=-2*pi*delta_0''`, and (5.4) gives

```text
Bhat_0(T)=f'(T)^2-f(T)f''(T).                            (5.6)
```

For `P>0`, (5.5) changes sign on every other half-period.  The terms at
`lambda=0` supply the canonical finite-part/contact regularization and turn
(5.4) into

```text
Bhat_P(T)=f'(T)^2-f(T)f''(T)
 -(2/pi) integral_0^infinity
   [f(T)^2-f(T+x)f(T-x)] sin(Px)/x^3 dx.                 (5.7)
```

Equations (5.4)--(5.7) exhibit two separate failures of the naive Gram
reading:

1. `ghat_P` is a signed distribution, not a positive measure;
2. away from `T=0`, the factor is the cross-frequency product
   `f(T+lambda)f(T-lambda)`, not a modulus square.

These are exact identities, not inferences from pointwise signs.

## 6. A sharp Poisson-orbit no-go

Even pairing a nonzero primal orbit with its full Poisson reflection does not
produce a positive-definite summand.  For `A>0`, define

```text
O_A(w)=exp(w)exp(-pi*A*exp(2w))
      +exp(-w)exp(-pi*A*exp(-2w)).                       (6.1)
```

This function is positive, even, and integrable.  Direct Mellin integration
gives

```text
Ohat_A(T)=Re{(pi*A)^(-(1-i*T)/2)
                    Gamma((1-i*T)/2)}.                  (6.2)
```

By Stirling's formula, the phase in (6.2) has derivative

```text
-(1/2)log[T/(2*pi*A)]+o(1),                             (6.3)
```

so it traverses infinitely many half-periods.  Therefore (6.2) takes both
signs infinitely often.  A pointwise-positive primal/dual Poisson orbit is
not a positive-definite or Gram summand.

Together, (3.5), (3.9), and (6.2) give the precise no-go:

> No coefficientwise or orbitwise square follows from two-dimensional
> Poisson summation.  Any Gram representation of the actual `B_P`, if one
> exists, must mix infinitely many nonzero 2D orbits with both one-axis
> sectors and the excision edge term.  It cannot be obtained by declaring
> each positive Gaussian orbit, or even each complete Poisson-reflection
> orbit, to be a square.

This does not rule out an unknown fully global theta-specific factorization.
It isolates exactly what such a factorization would still have to cancel.
