# Superoscillatory prime-gap kernels and exact spectral restitution

Status: R91 explicit ideal bump construction, explicit polynomial
construction, exact pole cancellation with fixed target reserve, degree and
coefficient-norm asymptotics, exact vertical kernel, high-harmonic decay, and
a fail-fast theorem for the full remainder.  The power-conditioned escape
left open in R90 is algebraically real: one can cancel the pole exactly while
remaining nonnegative at every prime power.  It does **not** make the zero
remainder small.  An ideal prime-invisible construction has remainder exactly
one after target normalization; every discrete-positive polynomial version
has remainder at least one if the target zero exists.  The local kernels also
have unit-sized modulus across the zero spacing, while the uncertainty
bandwidth contains power-many zeros.

Thus prime-gap interpolation supplies the desired pole/target ratio but no
independent cancellation of the spectral remainder.  Closing that remainder
would already contradict the target zero and cannot follow from support
orthogonality alone.

```text
actual prime-log gap                              AVAILABLE
smooth gap bump invisible to Lambda              EXACT
polynomial x^M((x-X)^2-h^2)                      EXACTLY discrete-positive
H_W(delta)=0, H_W(delta+e)=1                     ACHIEVABLE
degree at X=c log T                              T^(power)
factorial coefficient condition number           1+theta O(M)
local vertical kernel                            two pure phases, modulus ~1
pole/harmonic kernels at height T, c<1           rapidly decaying
absolute low-zero remainder                      power-divergent
ideal signed remainder                           exactly 1
discrete-positive signed remainder               at least 1
fixed zero-free strip                            NOT PROVED.             (1.1)
```

## 2. The general compact-weight explicit formula

The finite-polynomial formula in R90 has a useful smooth extension.  Let
`W in C_c^infinity((0,infinity))` and put

```text
H_W(z)=integral_0^infinity W(x)e^(-zx)dx,

Q_W(s)=sum_(n>=2)Lambda(n)W(log n)n^(-s).                     (2.1)
```

Pairing the distributional derivative of the classical explicit formula
with `W(x)e^(-sigma x)` gives

```text
Q_W(s)
 =H_W(s-1)
  -sum_rho H_W(s-rho)
  -sum_(j>=1)H_W(s+2j).                                      (2.2)
```

There is no boundary constant because `W` vanishes near zero.  The zero sum
is absolutely convergent because `H_W` has rapid vertical decay.  Formula
(2.2) can equivalently be obtained by smoothing first and shifting the
Mellin contour.

If

```text
W(log p^j)>=0                                                 (2.3)
```

for every prime power, then

```text
Q_W(sigma)+Re Q_W(sigma+iT)
 =sum_n Lambda(n)W(log n)n^(-sigma)[1+cos(T log n)]>=0.        (2.4)
```

This is the same positivity used in Theorem 10.1 of R90, now with enough
freedom to test the ideal localization limit before paying polynomial tails.

## 3. Actual gaps of controlled size

Let

```text
S={log(p^j):p prime,j>=1},       kappa=19/40.                  (3.1)
```

There are constants `c,C>0` such that every sufficiently large unit interval
`[Y,Y+1]` contains a gap between consecutive points of `S` whose length
`2h_Y` satisfies

```text
c Y e^(-Y)<=2h_Y<=C e^(-kappa Y).                             (3.2)
```

The upper bound is the Baker--Harman--Pintz consequence used in R90.  For the
lower bound, Chebyshev's estimate and a trivial prime-power count give

```text
#(S intersect [Y-1,Y+2])
 <=sum_(j>=1)pi(e^((Y+2)/j))
 <<e^Y/Y+Y e^(Y/2)
 <<e^Y/Y.                                                     (3.3)
```

Partitioning a unit interval by these points produces a subinterval of
length `>>Y e^(-Y)`; the containing global gap is at least that long.

We always choose such a largest gap, write it as

```text
I_X=(X-h,X+h),        I_X intersect S=empty,                  (3.4)
```

and absorb the harmless `X=Y+O(1)` into constants.  Later we take

```text
X=c_0 log T,             0<c_0<1.                             (3.5)
```

## 4. The ideal two-gap construction

This first construction deliberately grants perfect localization.  It
shows what the support loophole can buy and what the explicit formula takes
back.

Fix a nonnegative even function

```text
phi in C_c^infinity((-1,1)),       integral phi=1,             (4.1)
```

and define a bump inside a gap by

```text
phi_(x,h)(u)=h^(-1)phi((u-x)/h),

Phi_(x,h)(z)=integral phi_(x,h)(u)e^(-zu)du
            =e^(-zx)J(hz),

J(w)=integral_(-1)^1 phi(v)e^(-wv)dv.                         (4.2)
```

Choose two actual gaps with centers `x_0<x_1`, both tending to infinity,
and with

```text
x_1-x_0=d+o(1),       d>0 fixed.                              (4.3)
```

Their half-widths tend to zero.  Put `Phi_j=Phi_(x_j,h_j)` and, for fixed
`delta,e>0`,

```text
A_j=Phi_j(delta+e)>0,
R_j=Phi_j(delta)/Phi_j(delta+e).                              (4.4)
```

Evenness of `phi` gives

```text
R_j=e^(e x_j)[1+O_(delta,e)(h_j^2)],

R_0/R_1=e^(-ed)+o(1)=:theta+o(1)<1.                          (4.5)
```

For all sufficiently large centers define

```text
a=[A_0(1-R_0/R_1)]^(-1),

b=R_0/[R_1 A_1(1-R_0/R_1)],

W_ideal=a phi_(x_0,h_0)-b phi_(x_1,h_1).                     (4.6)
```

Then, exactly,

```text
H_ideal(delta)=0,
H_ideal(delta+e)=1.                                          (4.7)
```

Both bumps are supported in prime-power gaps, so

```text
W_ideal(s)=0       for every s in S,
Q_(W_ideal)(s)=0   for every complex s.                       (4.8)
```

In particular this construction satisfies discrete positivity with equality.
It attains a perfect pole/target reserve `q=0`.

The target-line vertical kernel is explicitly

```text
H_ideal(delta+e+iv)

 =[ e^(-ivx_0) J(h_0(delta+e+iv))/J(h_0(delta+e))
   -theta_X e^(-ivx_1) J(h_1(delta+e+iv))/J(h_1(delta+e))]
   /(1-theta_X),                                             (4.9)

theta_X=R_0/R_1.
```

For fixed `v`, or more generally `|v| max(h_0,h_1)=o(1)`, this is

```text
H_ideal(delta+e+iv)
 =[e^(-ivx_0)-theta e^(-ivx_1)]/(1-theta)+o(1).              (4.10)
```

The ideal two-point kernel satisfies

```text
|e^(-ivx_0)-theta e^(-ivx_1)|^2
 =1+theta^2-2theta cos(v(x_1-x_0))
 >=(1-theta)^2.                                              (4.11)
```

Thus the normalized kernel has modulus at least `1-o(1)` throughout its
unresolved band.  Perfect horizontal pole cancellation has produced no
vertical damping.

## 5. Exact spectral restitution for the ideal construction

Now suppose, for contradiction, that

```text
rho_0=1-e+iT                                                   (5.1)
```

is a zeta zero.  Use the notation `E_0+E_1` of Theorem 10.1 in R90.  Equations
(4.7)--(4.8) and the exact identity there give

```text
0
 =Q_W(1+delta)+Re Q_W(1+delta+iT)
 =0-1+E_0(W)+E_1(W;T,rho_0).                                 (5.2)
```

Therefore

```text
E_0(W_ideal)+E_1(W_ideal;T,rho_0)=1.                         (5.3)
```

This is exact, not an absolute-value estimate.  The prime-invisible bump has
not made the spectrum disappear.  The complete zero and trivial-zero system
reconstructs it with normalized size one.

Consequently no orthogonality statement derived solely from the fact that
the bump lies between prime powers can prove `r<1` in Theorem 10.1.  Such a
statement would contradict (5.3) under the target hypothesis and would
already be the desired zero-exclusion theorem.

## 6. An explicit polynomial construction

The preceding phenomenon is not caused by leaving the polynomial class.
Take the actual gap (3.4), fix `K>2`, and choose an integer `M` by

```text
M+1=ceil(K X^2/h^2),

delta=(M+1)/X,          r=delta+e.                            (6.1)
```

Define

```text
V_M(x)=x^M[(x-X)^2-h^2].                                     (6.2)
```

This polynomial is negative only inside `I_X`, hence

```text
V_M(log p^j)>=0                                               (6.3)
```

for every prime power.  Its Laplace transform is exactly

```text
H_V(z)=M! z^(-M-1) B_M(z),

B_M(z)
 =(M+1)(M+2)/z^2-2X(M+1)/z+X^2-h^2
 =(M+1)/z^2+[(M+1)/z-X]^2-h^2.                              (6.4)
```

Put

```text
K_X=(M+1)h^2/X^2>=K.                                         (6.5)
```

At the pole rate,

```text
B_M(delta)=h^2(K_X^(-1)-1)<0.                                (6.6)
```

At the target rate,

```text
(M+1)/r=X/[1+eX/(M+1)],                                     (6.7)
```

and hence, uniformly for fixed `e,K`,

```text
B_M(r)=-h^2[1-K_X^(-1)+O_(e,K)(h^2)]<0.                     (6.8)
```

Write

```text
G_delta=-H_V(delta)>0,       G_r=-H_V(r)>0.                  (6.9)
```

Choose a fixed

```text
0<alpha<1,

m+1=nearest integer to r alpha X,

U_m(x)=x^m.                                                  (6.10)
```

The two horizontal amplification ratios are

```text
R_U=H_U(delta)/H_U(r)=(r/delta)^(m+1),

R_V=G_delta/G_r
    =(r/delta)^(M+1)|B_M(delta)/B_M(r)|.                     (6.11)
```

Therefore

```text
log R_U=e alpha X+o(X),
log R_V=e X+O_(e,K)(1),

theta_X:=R_U/R_V
 =exp[-e(1-alpha)X+O_(e,K)(1)]<1                             (6.12)
```

for large `X`.  Set

```text
C_X=H_U(delta)/G_delta,

P_X(x)=U_m(x)+C_X V_M(x),

A_X=H_(P_X)(r)=H_U(r)(1-theta_X)>0,

W_X(x)=P_X(x)/A_X.                                          (6.13)
```

Every quantity is explicit in `X,h,M,alpha,delta,e`.  The construction has

```text
W_X(log p^j)>=0,

H_(W_X)(delta)=0,

H_(W_X)(delta+e)=1.                                         (6.14)
```

This is the requested power-conditioned polynomial with a perfect fixed
reserve.

## 7. Degree and coefficient norm

The gap bounds (3.2) and (6.1) give

```text
c_K X^2 e^(2 kappa X)<=M+1<=C_K e^(2X).                      (7.1)
```

At `X=c_0 log T`,

```text
T^(19c_0/20) polylog(T)
 <<M
 <<T^(2c_0).                                                  (7.2)
```

Thus the construction really occupies the power-conditioned branch left
open by R90.

Raw monomial coefficients are basis-dependent and badly scaled.  The
explicit-formula norm is the factorial Laplace norm

```text
||P||_(r,fac)
 =sum_j |lambda_j|j!r^(-j-1),
        P(x)=sum_j lambda_jx^j.                               (7.3)
```

It majorizes `|H_P(r+iv)|` for every real `v`.  From the four nonzero
coefficients in (6.13), one obtains the exact condition number

```text
||W_X||_(r,fac)

 ={1+theta_X A_abs(r)/|B_M(r)|}/(1-theta_X),                 (7.4)

A_abs(r)
 =(M+1)(M+2)/r^2+2X(M+1)/r+X^2-h^2.                         (7.5)
```

Since

```text
A_abs(r)=4X^2[1+o(1)],
|B_M(r)|=h^2[1-K^(-1)+o(1)],                                 (7.6)
```

we have

```text
||W_X||_(r,fac)
 = [1+theta_X O_K(X^2/h^2)]/(1-theta_X)
 = [1+theta_X O_K(M)]/(1-theta_X).                           (7.7)
```

The leading monomial coefficient itself is

```text
C_X/A_X
 =R_U/[M!delta^(-M-1)|B_M(delta)|(1-theta_X)],               (7.8)
```

so Stirling gives

```text
log(C_X/A_X)
 =M(1-log X)+O_e(X+log M+|log h|).                           (7.9)
```

Its small raw size does not mean good conditioning: multiplication by
`M!r^(-M-1)` restores the factor `theta_X M` in (7.7).

## 8. Exact vertical kernel and local zero spacing

Define

```text
u_m(v)=[r/(r+iv)]^(m+1),

v_M(v)=[r/(r+iv)]^(M+1) B_M(r+iv)/B_M(r).                   (8.1)
```

The normalized target-line kernel is exactly

```text
H_(W_X)(r+iv)
 =[u_m(v)-theta_X v_M(v)]/(1-theta_X).                       (8.2)
```

Because `r asyp X/h^2`, for fixed `v`,

```text
u_m(v)=e^(-i alpha Xv)[1+O_(K,alpha)(h^2v^2)],

v_M(v)=e^(-iXv)[1+O_(K,e)(h^2(1+v^2))].                     (8.3)
```

More generally these approximations remain uniform in a fixed small
multiple of the uncertainty band `|v|<=c/h`, with Gaussian-size envelopes
rather than `o(1)` errors.

Since `theta_X->0` for fixed `alpha<1`,

```text
|H_(W_X)(r+iv)|=1+o(1)                                      (8.4)
```

for every fixed `v`.  At the local zero spacing

```text
v=u/log T,
X=c_0 log T,                                                 (8.5)
```

one gets

```text
H_(W_X)(r+iu/log T)=e^(-i alpha c_0u)+o(1),                  (8.6)
```

again with unit modulus.  If instead `X-alpha X` is kept fixed so that
`theta_X` tends to a fixed number in `(0,1)`, (8.2)--(8.3) reduce to the
two-point kernel (4.10), whose modulus is at least one by (4.11).

The conclusion does not depend on which horizontal layout is chosen:

```text
prime-gap localization width             h
vertical uncertainty bandwidth            1/h
zero spacing                              1/log T
normalized kernel on that spacing         unit-sized.         (8.7)
```

## 9. High harmonics really do disappear

The failure is not caused by the pole at `delta+iT` or by the trivial zeros
at harmonic height.  From (8.1),

```text
|u_m(T)|
 =[1+(T/r)^2]^(-(m+1)/2).                                   (9.1)
```

The factor in `v_M(T)` has the same exponential envelope, up to the rational
factor `B_M(r+iT)/B_M(r)`.  The lower gap bound in (3.2) gives

```text
r asyp X/h^2<<e^(2X)/X.                                     (9.2)
```

If `r<=T`, the exponent in (9.1) is already `>>rX`.  If `r>T`,

```text
-(log |u_m(T)|)
 >>XT^2/r
 >>X^2T^2e^(-2X).                                           (9.3)
```

For `X=c_0 log T` with `c_0<1`, the last expression tends to infinity as a
positive power of `T`, up to logarithms.  It absorbs the rational factor in
`v_M`.  The same argument applies at every fixed nonzero harmonic `kT`.

Thus the high pole, high trivial-zero terms, and separated harmonics can be
made superpolynomially small.  What survives is the broad local/low-zero
band forced by the tiny physical gap.

## 10. The absolute remainder is power-large

To test the strongest favorable setting, select `rho_0` rightmost, or within
`O(1/X)` of the supremum of real parts, so every other zero has

```text
d_rho:=1-beta>=e-O(1/X).                                    (10.1)
```

Fix a small `eta_0>0`.  Uniformly for

```text
|gamma|<=eta_0/h                                             (10.2)
```

the monomial part at the zero-frequency point has magnitude

```text
|H_U(delta+d_rho-i gamma)/H_U(r)|

 =exp[-(d_rho-e)alpha X
      -alpha X gamma^2/(2r)+O_(K,alpha)(1/X)]

 >=c_(K,alpha,eta_0)e^(-(1-e)alpha X).                       (10.3)
```

For `d_rho>=e-O(1/X)`, the `V_M` part is smaller relative to the monomial
part by

```text
O_K(theta_X e^(-(d_rho-e)(1-alpha)X}),                       (10.4)
```

after decreasing `eta_0` if necessary.  Hence it cannot cancel (10.3) for
large `X`.

The Riemann--von Mangoldt formula supplies

```text
# {rho:0<gamma<=eta_0/h}
 asyp h^(-1)log(1/h).                                        (10.5)
```

It follows that the termwise absolute estimate for the zero-frequency part
of `E_0` is at least

```text
sum_(0<gamma<=eta_0/h)
 |H_(W_X)(delta+d_rho-i gamma)|

 >>h^(-1)log(1/h)e^(-(1-e)alpha X).                          (10.6)
```

Using `h<<e^(-kappa X)`, choose

```text
0<alpha<min(1,kappa/(1-e)).                                  (10.7)
```

Then (10.6) grows at least like

```text
X exp[(kappa-(1-e)alpha)X],                                  (10.8)
```

a fixed power of `T` at `X=c_0 log T`.  Ordinary zero counts, zero density,
and absolute values therefore give not merely `r>=1`, but a bound diverging
as a power.

This is the sharp uncertainty exchange:

```text
narrow prime gap h       permits horizontal pole cancellation,
narrow prime gap h       forces vertical bandwidth 1/h,
bandwidth 1/h            imports power-many low zeros.       (10.9)
```

Only a signed exponential-sum estimate across those zeros could continue the
argument.

## 11. Why support orthogonality cannot supply that signed estimate

For the normalized polynomial (6.13), suppose again that `rho_0` is a zero.
The exact R90 identity is

```text
Q_(W_X)(1+delta)+Re Q_(W_X)(1+delta+iT)

 =-1+E_0(W_X)+E_1(W_X;T,rho_0).                              (11.1)
```

The left side is nonnegative by discrete prime positivity.  Therefore

```text
E_0(W_X)+E_1(W_X;T,rho_0)>=1.                                (11.2)
```

In particular every valid estimate

```text
|E_0+E_1|<=r                                                 (11.3)
```

under the target hypothesis necessarily has

```text
r>=1.                                                        (11.4)
```

For the ideal gap-supported bump equality holds, by (5.3).  For the
polynomial, the nonnegative prime side accounts for any excess over one.

This observation is logically simple but decisive for the proposed
orthogonality shortcut.  Prime-gap support plus the explicit formula cannot,
by itself, prove a remainder smaller than the target: it gives the exact
opposite identity if the target exists.  To establish `r<1` one must add a
genuine theorem about the signed zero sum (or equivalently about the exact
von Mangoldt coefficients) which is strong enough to contradict (11.2).
The interpolation construction does not manufacture that theorem.

At local ordinates the required sum has the model shape

```text
sum_rho e^(-[1-beta-e]alpha X)e^(i gamma alpha X),            (11.5)
```

over a band of length `1/h`, together with its second phase at `X`.
Neither the gap condition nor Fejer positivity makes the phases in (11.5)
orthogonal.  It is a target-conditioned zero exponential sum with
power-many terms--strictly stronger than the signed joint estimate already
isolated in R89--R90.

## 12. Numerical scout

The following values use the largest actual prime-power logarithm gap found
in `[Y,Y+1]`, with `K=4`, `e=0.1`, and `alpha=0.4`.  They are diagnostics only;
all conclusions above use the exact formulas and asymptotic gap bounds.

```text
Y    center X    gap 2h       M          delta       theta     fac. cond.
3    3.53833     1.452e-1     9,503      2.686e3     .809      5.36e4
4    4.53167     8.607e-2    44,349      9.787e3     .762      1.89e5
5    5.32258     5.855e-2   132,209      2.484e4     .727      4.69e5
6    6.15901     2.537e-2   942,878      1.531e5     .691      2.81e6
8    8.09711     8.524e-3    14.4e6      1.783e6     .615      3.08e7
```

The degree and factorial condition number become enormous before the
asymptotic regime is remotely high.  Direct coefficient expansion is
numerically meaningless; (6.4), (6.11), and (8.2) are the stable evaluation
formulas.

## 13. Decision

The surviving R90 branch has now been executed rather than merely named.

1. Smooth prime-invisible bumps and explicit algebraic polynomials both
   achieve `H(delta)=0`, `H(delta+e)=1` while preserving every prime-side
   coefficient inequality.
2. An explicit polynomial uses degree
   `M asyp X^2/h^2`, between `e^(2kappa X)` and `e^(2X)` for a selected
   actual gap.
3. Its natural coefficient condition number is
   `[1+theta O(M)]/(1-theta)`.
4. High harmonics can be annihilated when `X=c_0 log T`, `c_0<1`.
5. The target-line kernel remains unit-sized at local zero spacings and has
   bandwidth `1/h`.
6. That bandwidth imports power-many low zeros; every absolute remainder
   bound diverges as a power after choosing `alpha` as in (10.7).
7. Exact support invisibility gives signed remainder `1`; general discrete
   positivity gives signed remainder at least `1` under the target
   hypothesis.

Therefore the coefficient-specific superoscillatory mechanism succeeds at
pole cancellation and fails at spectral cancellation.  Its only continuation
is a new signed theorem for the power-many-zero sum (11.5).  Nothing in the
prime-gap interpolation itself supplies that theorem, so this route does not
prove a fixed strip and does not prove that no fixed strip exists.
