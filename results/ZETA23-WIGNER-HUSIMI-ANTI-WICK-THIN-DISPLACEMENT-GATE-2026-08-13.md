# Wigner--Husimi and anti-Wick gate for the theta thin-displacement detector

**Date:** 2026-08-13

**Verdict:** **SMOOTHED MONOTONICITY PROVED; POINTWISE RECOVERY DOES NOT CLOSE.**

**Strip status:** no fixed zero-free strip and no improved zero bound.

This card audits whether the signed theta slice can be replaced by a positive
phase-space object.  The answer is exact.  The slice is a Wigner distribution,
so its negative values are structural by Hudson's theorem.  Gaussian Husimi
smoothing produces a genuine positive quantity and an exact radial
monotonicity inequality, but it also reweights the two radial lines
differently.  The resulting positive common mode is quantitatively tied to
vertical localization by the uncertainty principle.  Exact recovery of the
original polarized detector is backward heat and is necessarily signed.

## 1. Exact Wigner identification

Use the convention

```text
W_f(x,T)=integral_R f(x+q/2) conjugate(f(x-q/2)) exp(-i*T*q)dq.       (1.1)
```

For the real even theta kernel `Phi`, the slice used in the full-theta
detector is

```text
h_T(p)=integral_R Phi((p+q)/2)Phi((p-q)/2)exp(-i*T*q)dq
      =W_Phi(p/2,T).                                                   (1.2)
```

Thus the previously observed negative value of `h_T(p)` is not an accidental
failure of one numerical cone.  Hudson's pure-state theorem says that an
everywhere nonnegative Wigner distribution comes only from an exponential of
a quadratic polynomial.  The theta kernel is in `L^2`, has
double-exponential tails, and is not Gaussian.  Hence `W_Phi`, and therefore
`h`, must be negative somewhere.  Hudson's theorem does not locate the
negative point and by itself says nothing about the weighted detector; it
does close the proposal `h_T(p)>=0` structurally.

Put

```text
F(z)=integral_R Phi(u)exp(z*u)du,
U_x(T)=|F(x-i*T)|^2.                                                    (1.3)
```

The change of variables `u=(p+q)/2`, `v=(p-q)/2`, whose Jacobian is `2`,
gives, for real `lambda,T`,

```text
integral_R h_T(p)cosh(lambda*p)dp=2*U_lambda(T).                         (1.4)
```

For `0<eta<=alpha`, set

```text
A=alpha+eta,  B=alpha-eta,
w_(alpha,eta)(p)=sinh(alpha*p)sinh(eta*p)
                =[cosh(A*p)-cosh(B*p)]/2.                              (1.5)
```

The exact thin-displacement detector is therefore

```text
D_(alpha,eta)(T):=integral_R w_(alpha,eta)(p)h_T(p)dp
                  =U_A(T)-U_B(T).                                      (1.6)
```

The problem is precisely a signed comparison of two radial line norms.

## 2. Husimi smoothing gives a true positive theorem

Take the normalized squeezed Gaussian

```text
g_s(x)=(pi*s^2)^(-1/4)exp(-x^2/(2*s^2)),    s>0.                        (2.1)
```

With (1.1),

```text
W_(g_s)(x,T)=2*exp(-x^2/s^2-s^2*T^2).                                  (2.2)
```

For

```text
V_g f(x,T)=integral_R f(u)conjugate(g(u-x))exp(-i*T*u)du,
Q_s(x,T)=|V_(g_s)Phi(x,T)|^2,
```

the Moyal identity gives the exact spectrogram formula

```text
Q_s(p/2,T)=1/(2*pi) double_integral_R2 h_(T-Omega)(p')
 exp(-(p-p')^2/(4*s^2)-s^2*Omega^2) dp' dOmega >=0.                    (2.3)
```

Let

```text
G_s(Omega)=s/sqrt(pi)*exp(-s^2*Omega^2),
M_s(x,T)=(G_s*U_x)(T).                                                  (2.4)
```

Integrating (2.3) against the nonnegative weight (1.5) gives the central
surviving result.

> **Theorem 2.1 (exact Husimi radial monotonicity).**  For every `s>0`, real
> `T`, and `A>=B>=0`,
>
> ```text
> e^(s^2*A^2) M_s(A,T) >= e^(s^2*B^2) M_s(B,T).                         (2.5)
> ```
>
> Equivalently,
>
> ```text
> H_s^(alpha,eta)(T):=integral_R w_(alpha,eta)(p)Q_s(p/2,T)dp
>   =G_s*[e^(s^2*A^2)U_A-e^(s^2*B^2)U_B](T) >=0.                       (2.6)
> ```

There is no zero-free hypothesis in this theorem.  All constants in (2.5)
come from the elementary Gaussian moment

```text
integral_R exp(-(p-p')^2/(4*s^2))exp(lambda*p)dp
 =2*sqrt(pi)*s*exp(s^2*lambda^2+lambda*p').                            (2.7)
```

In particular,

```text
M_s(A,T)>=exp(-4*s^2*alpha*eta)M_s(B,T).                               (2.8)
```

This is a genuine new smoothed inequality, not positivity of the original
detector (1.6).

## 3. The exact common-mode contamination

Write

```text
D=U_A-U_B,  C=U_A+U_B>=0,
c=s^2*(alpha^2+eta^2),  d=2*s^2*alpha*eta.                             (3.1)
```

Then the integrand in (2.6) splits exactly as

```text
e^(s^2*A^2)U_A-e^(s^2*B^2)U_B
 =e^c[cosh(d)*D+sinh(d)*C].                                            (3.2)
```

Consequently Husimi positivity is precisely

```text
G_s*D >= -tanh(d)*(G_s*C).                                             (3.3)
```

The second term is a positive unpolarized/common-mode offset.  It is present
for every `s>0`, `alpha>0`, and `eta>0`.  Therefore positivity of a
spectrogram does not imply `D>=0`, or even `G_s*D>=0`.

The same fact can be seen directly at symbol level.  If
`c_+(p)=cosh(alpha*p)cosh(eta*p)>=0`, spatial heat gives

```text
exp(s^2*d_p^2)w_(alpha,eta)
 =e^c[cosh(d)w_(alpha,eta)+sinh(d)c_+].                                (3.4)
```

Thus Gaussian smoothing does not preserve the polarized weight.

## 4. Sharp uncertainty/carrier ledger

In the `(p,T)` coordinates of (2.3), the normalized Gaussian has variances

```text
sigma_p^2=2*s^2,       sigma_T^2=1/(2*s^2),
sigma_p*sigma_T=1.                                                   (4.1)
```

The attenuation and contamination parameters are therefore

```text
4*s^2*alpha*eta=2*alpha*eta/sigma_T^2,
d=2*s^2*alpha*eta=alpha*eta/sigma_T^2.                                (4.2)
```

This is the clean tradeoff: sharp localization in height means small
`sigma_T`, which forces the common mode in (3.3) toward full strength.

More generally, an axis-aligned Gaussian Wigner kernel of a positive state
(equivalently, a Gaussian smoothing which is spectrogram-positive for every
input) has `sigma_p^2*sigma_T^2>=1`.  Its differential line factor is controlled by
`d=alpha*eta*sigma_p^2`, so

```text
d>=alpha*eta/sigma_T^2.                                                (4.3)
```

The pure squeezed window above is optimal.  A correlated Gaussian with
covariance `kappa` obeys

```text
sigma_p^2*sigma_T^2-kappa^2>=1.                                       (4.4)
```

Moreover, integrating an exponential `exp(lambda*p)` against that kernel
produces the factor `exp(lambda^2*sigma_p^2/2)` and shifts the two height
samples by `+/-lambda*kappa`.  Thus rotation neither reduces the line factor
nor preserves a same-height comparison.  At fixed marginal height resolution,
the aligned pure squeeze minimizes the common factor and avoids these shifted
samples; a correlated kernel could only help through additional
coefficient-specific information, not through generic positivity.

There is also an exact vertical-mode version of the ledger:

```text
G_s*cos(N*T)=exp(-N^2/(4*s^2))*cos(N*T).                               (4.5)
```

If one asks both to preserve this mode to relative loss at most
`0<epsilon<1` and to keep the common-mode coefficient at most `epsilon`,
then necessarily

```text
s^2 >= N^2/[4*(-log(1-epsilon))],
s^2 <= artanh(epsilon)/(2*alpha*eta),

alpha*eta*N^2
 <=2*artanh(epsilon)*[-log(1-epsilon)].                                (4.6)
```

For small `epsilon`, the right side is `2*epsilon^2+O(epsilon^3)`.  At the
natural height scale `N` comparable to `log T`, this generic mechanism only
sees displacements of order at most `(log T)^(-2)`, not a fixed strip.  This
last scale statement is diagnostic rather than a theorem about every theta
coefficient; the exact statement is (4.6).

## 5. Anti-Wick recovery is backward heat

Equation (2.3) is the heat operator

```text
mathsf(H)_s=exp(s^2*d_p^2+(4*s^2)^(-1)*d_T^2).                          (5.1)
```

Pairing a nonnegative anti-Wick symbol `a` with `Q_s=mathsf(H)_s h` is
positive and corresponds, on the Wigner side, to the smoothed Weyl symbol
`mathsf(H)_s a`.  To represent the point detector

```text
b(p,tau)=w_(alpha,eta)(p)delta(tau-T),                                 (5.2)
```

one would need

```text
a=mathsf(H)_s^(-1)b.                                                    (5.3)
```

This cannot be a nonnegative symbol.  Already its spatial factor is negative
at the origin:

```text
[exp(-s^2*d_p^2)w_(alpha,eta)](0)
 =[exp(-s^2*A^2)-exp(-s^2*B^2)]/2 <0.                                 (5.4)
```

The inverse heat multiplier for the height delta grows like
`exp(xi^2/(4*s^2))`, so (5.3) is not even a tempered positive measure.
Anti-Wick positivity therefore cannot exactly recover (1.6); doing so is the
same ill-posed reverse-heat step encountered in the Jensen/Hermite audit.

## 6. Positive banks and signed spectrograms

Positive mixtures of squeeze parameters cannot cancel the common mode in
(3.4), because its coefficient is strictly positive at every `s>0`.  The
only zero-contamination endpoint is `s=0`, where the height variance in
(4.1) is infinite.

A signed difference can cancel it algebraically, but then positivity is
lost.  For `0<s_1<s_2`, put

```text
d_j=2*s_j^2*alpha*eta,
S_j=e^(-s_j^2*(alpha^2+eta^2))*exp(s_j^2*d_p^2)w
   =cosh(d_j)w+sinh(d_j)c_+.                                           (6.1)
```

The unique two-resolution reconstruction is

```text
w=lambda_1*S_1+lambda_2*S_2,
lambda_1= sinh(d_2)/sinh(d_2-d_1)>0,
lambda_2=-sinh(d_1)/sinh(d_2-d_1)<0.                                  (6.2)
```

Its coefficient cost is

```text
|lambda_1|+|lambda_2|
 =[sinh(d_1)+sinh(d_2)]/sinh(d_2-d_1),                                (6.3)
```

which diverges as `d_2-d_1` tends to zero with `d_1` bounded away from zero.
Taking both `d_j` to zero at comparable rates can avoid this coefficient
blowup only by sending both height variances to infinity.  In addition, the
two spectrograms have different height heat kernels.  Formula (6.2) only
reconstructs the spatial symbol; pointwise reconstruction in `T` still
requires signed deconvolution/backward heat.  A multiscale bank therefore
recreates, rather than removes, the reverse-heat instability.

## 7. The exact live sufficient condition

The Husimi theorem does leave one coefficient-specific route.  If a
hypothetical outer-line zero `F(A-i*T_0)=0` could be shown to imply, for some
admissible `s`,

```text
M_s(A,T_0)<exp(-4*s^2*alpha*eta)M_s(B,T_0),                             (7.1)
```

then (2.8) would give an immediate contradiction.  Thus the missing input is
a **zero-localization reverse estimate**: the Gaussian average of the outer
line norm around its zero must be uniformly smaller than the inner-line
average by the uncertainty cost in (7.1).

Generic Wigner/Husimi positivity, analyticity, and zero density do not supply
(7.1).  A proof would have to use special theta/zeta coefficient structure
to beat backward heat.  This is a sharply isolated sufficient inequality,
not a proved strip criterion.

## 8. Truth boundary

```text
h_T(p)=W_Phi(p/2,T)                         EXACT
pointwise Wigner positivity                 STRUCTURALLY FALSE (Hudson)
Gaussian-smoothed radial monotonicity       PROVED, equation (2.5)
uncertainty/common-mode ledger              PROVED, equations (4.1)--(4.6)
squeezed/rotated generic same-height escape  CLOSED within positive Gaussians
positive multiscale Husimi cancellation     IMPOSSIBLE
signed spectrogram reconstruction           POSSIBLE but loses positivity/backward-heat costly
coefficient-specific estimate (7.1)         OPEN
uniform zeta zero-free strip                 NOT PROVED
```

The reusable result is Theorem 2.1.  The phase-space import does not prove a
fixed strip, but it converts the vague objection that "smoothing loses the
sign" into the exact contamination factor `tanh(alpha*eta/sigma_T^2)` and
the exact reverse-heat target (7.1).

## Reference

[R. L. Hudson, *When is the Wigner quasi-probability density non-negative?*,
Reports on Mathematical Physics **6** (1974), 249--252](https://www.sciencedirect.com/science/article/pii/003448777490007X),
doi:10.1016/0034-4877(74)90007-X.
