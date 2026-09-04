# Theta `B_P`: full Poisson orbit, polar subtraction, and a two-crossing obstruction

**Date:** 2026-08-13  
**Status:** exact modular reduction and exact coefficient-specific sign lemma;
the proposed `S_2` one-crossing shortcut is rigorously false.  **Positive
definiteness of the actual `B_P` family remains open.  No strip is proved.**

## 1. Polar subtraction before the two-dimensional lift

Let

```text
vartheta(x)=sum_(n in Z) exp(-pi*n^2*x),
Theta(u)=exp(u)*vartheta(exp(4u)).                         (1.1)
```

Poisson summation gives `Theta(-u)=Theta(u)`.  Direct differentiation of
each positive-half theta term gives the exact identity

```text
Phi(u)=1/16*(d_u^2-1)Theta(u).                            (1.2)
```

The two homogeneous solutions in `Theta` must be removed before derivatives
are transferred to a polynomial tail.  Define

```text
R(u)=Theta(u)-2*cosh(u).                                  (1.3)
```

Then `R` is even, smooth, integrable, and

```text
R(u)=-exp(-|u|)+O(exp(|u|-pi*exp(4|u|))),
Phi(u)=1/16*(R''(u)-R(u)).                                (1.4)
```

This subtraction yields a genuine coefficient-specific sign lemma.

> **Lemma 1 (polar-subtracted theta gap).**  `R(u)<0` for every real `u`.
> Equivalently, `r=-R` is a strictly positive even kernel satisfying
>
> ```text
> (1-d_u^2)r=16*Phi,
> r=8*exp(-|.|)*Phi,                                      (1.5)
> ```
>
> where the last expression is convolution.

For `u>=0`, put `y=exp(2u)>=1`.  The stable theta expansion is

```text
exp(u)R(u)=2*y*sum_(n>=1)exp(-pi*n^2*y^2)-1.              (1.6)
```

Every function `y*exp(-pi*n^2*y^2)` decreases for `y>=1`, and

```text
2*sum_(n>=1)exp(-pi*n^2)
 <=2*exp(-pi)/(1-exp(-pi))<1.                            (1.7)
```

This proves the strict sign.  Formula (1.5) follows from (1.4) and the
positive Green kernel of `1-d_u^2`.

If

```text
Z(T)=integral_R Phi(u)exp(-i*T*u)du=xi((1-i*T)/2)/4,
```

then

```text
Rhat(T)=-16*Z(T)/(1+T^2)
 =1/2*pi^(-s/2)*Gamma(s/2)*zeta(s),
s=(1-i*T)/2.                                              (1.8)
```

The last equality includes its sign: `xi(s)=-(1+T^2)/8` times the completed
factor without `s(s-1)`.

## 2. Exact reduction to one modular Wigner cross-orbit

Put

```text
x=(w+d)/2,       y=(w-d)/2,
C(w,d)=R(x)R(y)=r(x)r(y)>0.                              (2.1)
```

Because

```text
partial_w^2-partial_d^2=partial_x*partial_y,
2*(partial_w^2+partial_d^2)=partial_x^2+partial_y^2,
```

one obtains the exact linearization

```text
Phi(x)Phi(y)=1/256*mathcal_L C(w,d),                     (2.2)

mathcal_L=(partial_w^2-partial_d^2)^2
          -2*(partial_w^2+partial_d^2)+1.
```

For

```text
g_P(d)=(|d|-P)_+^2,
A_P(w)=integral_R g_P(d)C(w,d)dd,
C_P(w)=integral_(|d|>P)C(w,d)dd,
```

the theta density from the third-tail attack is therefore

```text
B_P(w)=1/1024*{
  (partial_w^2-1)^2 A_P(w)
  -4*(partial_w^2+1)C_P(w)
  -4*partial_d C(w,P)}.                                  (2.3)
```

This follows by integrating all `d` derivatives in (2.2) onto `g_P`:

```text
g_P''=2*1_(|d|>P),
g_P''''=2*delta'(d-P)-2*delta'(d+P).                     (2.4)
```

No boundary term is hidden at infinity because `R` and its derivatives have
exponential decay.  This is precisely why the polar subtraction in (1.3) is
required.

Let

```text
c_T(d)=integral_R C(w,d)exp(-i*T*w)dw
      =W_R(d/2,T).                                       (2.5)
```

It is real and even.  Fourier transforming (2.3) gives the following exact
single-cross-orbit criterion:

```text
1024*S_3(P,T)
 =-4*c_T'(P)
  +4*(T^2-1)*integral_(|d|>P)c_T(d)dd
  +(T^2+1)^2*integral_R g_P(d)c_T(d)dd.                  (2.6)
```

Thus all-P positivity of `B_P` is equivalent to the sign of the one explicit
combination (2.6).  Lemma 1 makes the underlying configuration-space kernel
`C` positive, but it does **not** make its Wigner slice `c_T` positive.
Indeed `r` is non-Gaussian, so Hudson's theorem forces this Wigner function
to be signed.  Equation (2.6) is an exact signed remainder, not an actual
proof of `S_3>=0`.

The companion probe
`results/probe_theta_bp_modular_cross_orbit.py` checks (2.6).  For example,
at `(P,T)=(0.3,2)`, 900-point Gauss rules give

```text
direct S_3  =1.82147650843447e-6,
reduced S_3 =1.82147650808011e-6.                         (2.7)
```

The three terms on the right of (2.6), before division by `1024`, are

```text
+1.4217853578,   +1.1836033805,   -2.6035235464.          (2.8)
```

Their cancellation is another explicit warning against reading (2.6) as a
termwise positive decomposition.

## 3. Full two-dimensional Poisson orbit and its unavoidable axes

Before polar subtraction, define

```text
M(w,d)=Theta((w+d)/2)Theta((w-d)/2)
 =exp(w)*sum_(m,n in Z)
   exp(-pi*exp(2w)*(m^2*exp(2d)+n^2*exp(-2d))).          (3.1)
```

Two-dimensional Poisson summation gives

```text
M(w,d)=exp(-w)*sum_(r,s in Z)
 exp(-pi*exp(-2w)*(r^2*exp(-2d)+s^2*exp(2d)))
       =M(-w,d).                                         (3.2)
```

Together with exchange of the two one-dimensional factors, this gives the
full dihedral symmetry in `(w,d)`.

In the fundamental chamber `w>=|d|`, set

```text
theta_+=vartheta(exp(2*(w+d))),
theta_-=vartheta(exp(2*(w-d))),
A_+=theta_+-1,        A_-=theta_--1.                    (3.3)
```

The polar-subtracted product has the absolutely convergent
inclusion--exclusion expansion

```text
C(w,d)= exp(w)*A_+*A_-
        -exp(d)*A_+
        -exp(-d)*A_-
        +exp(-w).                                        (3.4)
```

These are, respectively, the interior rectangular-lattice orbit, the two
one-axis cross orbits, and the corner orbit.  In the chamber `d>=|w|`, the
same formula holds with `w` and `d` exchanged.  Globally, (3.4) and its
dihedral images are equivalent to

```text
C=M-exp(w)*(theta_++theta_-)
    -exp(-w)*(theta_tilde_++theta_tilde_-)
    +exp(w)+exp(-w)+exp(d)+exp(-d),                      (3.5)
```

where `theta_tilde_+/-=vartheta(exp(-2*(w+/-d)))`.

The negative one-axis terms in (3.4) are necessary: all four pieces together
equal the positive product `r(x)r(y)`, while neither the interior orbit nor
the axes are separately modular.  Even pairing a primal lattice orbit with
its complete Poisson reflection does not produce a positive-definite atom.
For `a>0`, the pointwise-positive pair

```text
O_a(w)=exp(w-pi*a*exp(2w))+exp(-w-pi*a*exp(-2w))          (3.6)
```

has exact Fourier transform

```text
Ohat_a(T)=Re[(pi*a)^(-(1-i*T)/2)*Gamma((1-i*T)/2)].       (3.7)
```

Stirling's formula makes its phase unbounded and eventually monotone, so
(3.7) changes sign infinitely often.  Therefore no coefficientwise Gram
proof can stop at a finite interior orbit, an axis orbit, or even a complete
primal/dual reflection pair.  A manifest square, if it exists, must mix the
axis and two-dimensional orbits globally and infinitely.

As a normalization audit, the full two-dimensional Fourier transform is

```text
C_hat(T,xi)=2*Rhat(T+xi)*Rhat(T-xi)
 =512*Z(T+xi)Z(T-xi)
   /[((T+xi)^2+1)*((T-xi)^2+1)].                         (3.8)
```

The symbol of `mathcal_L` is exactly the denominator in (3.8), so (2.2)
returns

```text
[Phi(x)Phi(y)]_hat(T,xi)=2*Z(T+xi)Z(T-xi),               (3.9)
```

the previously derived divided-Turan product.  This independently checks
every factor in the reduction.

## 4. The proposed `S_2` one-crossing shortcut is false

Let

```text
f_T(u)=Phi(u)exp(-i*T*u),
A_T(x)=integral_x^infinity f_T(u)du.                      (4.1)
```

Since `f_T(-u)=conjugate(f_T(u))`, Fubini gives the exact reflection overlap

```text
S_2(P,T)=2*integral_R A_T(x+P)conjugate(A_T(-x))dx.       (4.2)
```

Also `S_3'(P,T)=-S_2(P,T)` and `S_3(infinity,T)=0`.  It was therefore
tempting to seek an at-most-one-crossing theorem for `S_2`, necessarily from
negative to positive.  Such a theorem, together with `S_3(0,T)>=0`, would
force `S_3(P,T)>=0`.

It is false for the actual theta kernel.  The script
`results/probe_theta_s2_crossings.py` found a positive--negative--positive
profile at `T=152.7`.  The separate interval script
`results/certify_theta_s2_two_crossings.py` proves

```text
S_2(0,152.7)
 in [1.1621814838606866e-48, 1.1782091877698846e-48],

S_2(0.0794535,152.7)
 in [-9.286426841490660e-50, -7.683656450570963e-50],

S_2(0.12,152.7)
 in [8.614149294433841e-49, 8.774426333525810e-49].       (4.3)
```

Continuity forces at least two sign changes.  The certificate uses Arb
analytic quadrature on `[10^(-8),300]`, a Cauchy origin estimate, and a
gamma-recurrence/Euler--Maclaurin product-tail bound with the near-optimal
recurrence depth `N=65`.

This result kills only the proposed variation-diminishing shortcut.  It does
**not** falsify `S_3>=0` or positive definiteness of `B_P`: a positive
`S_2`, then negative pocket, then positive tail can still have all of its
remaining integrals `S_3(P)=integral_P^infinity S_2(Q)dQ` nonnegative.

## 5. Binary verdict and remaining lemma

```text
polar-subtracted sign R<0                         PROVED
2D Poisson/inclusion-exclusion expansion          PROVED
finite or paired-orbit coefficientwise Gram       CLOSED
single-cross-orbit identity (2.6)                 PROVED
pointwise sign of that Wigner cross-orbit          STRUCTURALLY FALSE
S_2 at-most-one-crossing route                     RIGOROUSLY FALSE
positive definiteness of every actual B_P          OPEN / logically untouched
uniform zero-free strip                            NOT PROVED
```

The strongest exact remaining lemma is now sharply isolated:

> Prove that the **specific signed combination** of the polar-subtracted
> theta Wigner orbit in (2.6) is nonnegative for every `P>=0` and real `T`.

Neither Lemma 1 nor the Poisson expansion supplies this sign by itself.  A
successful proof must mix infinitely many rectangular and one-axis modular
orbits; pointwise tail positivity, finite Poisson pairing, and an index-one
crossing law have all been removed.
