# The centered sinh-tent square: exact completion and a functional-equation no-go

Status: exact scalar normalization and analytic obstruction, 2026-08-12.
No finite scan is used.  No sign for the actual zeta square, zero-free strip,
or improved zero bound is proved.

## 1. Verdict

The centered odd carrier admits a completely explicit scalar normalization.
In the physical normalization

```text
f(x)=sinh(alpha*x) 1_(|x|<=L/2),
C(u)=integral_R f(x)f(x+u)dx,
F(z)=integral_R f(x)e^(i*z*x)dx,
K(z)=F(z)F(-z),
```

the exact completed one-square is an archimedean integral minus twice the
two-abscissa prime--continuum discrepancy.  The factor `2` and every
`2*pi` are fixed below.

The functional equation does simplify the complementary logarithmic
derivatives, but not to a modulus square.  It gives a signed curvature
functional

```text
2*[(cosh(alpha*L)/alpha)*d_alpha log|Xi(1/2+alpha+i*gamma)|
   -d_alpha^2 log|Xi(1/2+alpha+i*gamma)|].
```

Symmetry supplies no sign for this expression.

More decisively, the exact sinh-tent Weil kernel assigns a strictly negative
total value to a functional-equation-symmetric zero quartet at the matched
depth and height, once `gamma` exceeds an explicit threshold.  Multiplying
any real symmetric order-one completed function by the corresponding
positive-on-the-critical-line polynomial preserves its functional equation,
reality, order, and critical-line phase, while adding an arbitrarily large
negative multiple of this quartet contribution.  Therefore no sign proof
for this carrier can follow from those coefficient-free structures alone.
Euler/von Mangoldt input is indispensable.

## 2. Exact physical and arithmetic normalization

Fix `L,alpha>0`.  Direct integration gives, for `0<=u<=L`,

```text
C(u)=sinh(alpha*(L-u))/(2*alpha)
     -(L-u)*cosh(alpha*u)/2,                        (2.1)
```

extended evenly and by zero outside `[-L,L]`.  With the Fourier convention
in Section 1,

```text
F(z)=2*i*[alpha*sin(z*L/2)*cosh(alpha*L/2)
          -z*cos(z*L/2)*sinh(alpha*L/2)]
          /(alpha^2+z^2),                          (2.2)

integral_R C(u)e^(i*z*u)du=K(z).                   (2.3)
```

The apparent singularities in (2.2) are removable.  Since `f` is real and
odd,

```text
F(-z)=-F(z),
K(-z)=K(z),
K(t)=|F(t)|^2>=0                  (t real).         (2.4)
```

Put `T=e^L`,

```text
P_T(s)=sum_(n<=T) Lambda(n)n^(-s),
I_T(s)=integral_1^T x^(-s)dx,
Delta P_T=P_T-I_T,
Delta D_T=L*Delta P_T+(Delta P_T)',
s_+=1/2+alpha+i*gamma,
s_-=1/2-alpha+i*gamma.                             (2.5)
```

Expansion of (2.1), with no estimate, gives

```text
S_(L,alpha,gamma)
 :=sum_(n<=T) Lambda(n)n^(-1/2)
       C(log n)cos(gamma*log n)
   -integral_1^T x^(-1/2)C(log x)cos(gamma*log x)dx

 =1/4*Re{
      (e^(alpha*L)/alpha)*Delta P_T(s_+)
     -(e^(-alpha*L)/alpha)*Delta P_T(s_-)
     -Delta D_T(s_+)-Delta D_T(s_-)}.              (2.6)
```

This independently recovers the two-abscissa identity in
`centered_even_cosine_gate.py`.

For the completed multiplier, write

```text
G(t)=[Re psi(1/4+i*t/2)-log pi]/(2*pi)
     +1/[2*pi*(1/4+t^2)],

E_T(t)=sum_(n<=T)Lambda(n)n^(-1/2+i*t)
       -integral_1^T x^(-1/2+i*t)dx,

nu_T(t)=G(t)-(1/pi)*Re E_T(t).                     (2.7)
```

Define the unnormalized centered square

```text
Q_(L,alpha,gamma)
 =integral_R K(s)*
   {1+[nu_T(gamma+s)+nu_T(gamma-s)]/2}ds.           (2.8)
```

Fourier inversion in the convention (2.3) says

```text
integral_R K(s)ds=2*pi*C(0),
integral_R K(s)cos(s*u)ds=2*pi*C(u).                (2.9)
```

Consequently the exact completion ledger is

```text
Q_(L,alpha,gamma)
 =2*pi*C(0)
  +integral_R K(s)*[G(gamma+s)+G(gamma-s)]/2 ds
  -2*S_(L,alpha,gamma).                             (2.10)
```

Thus the prime--continuum scalar in (2.6) enters with coefficient `-2`.
More precisely, with

```text
h=2*pi/L,       q=alpha/h,       r=(t-gamma)/h,
```

the sharp synthesis in `centered_even_cosine_gate.py` obeys

```text
Phi_(q,h)(r)=[i*pi/sinh(pi*q)]*F(t-gamma).          (2.11)
```

Hence its real-axis square is the positive constant
`pi^2/sinh(pi*q)^2` times `K(t-gamma)`.  Finite aperture and Hahn endpoint
projection change the kernel; (2.10) is the exact unprojected core model,
not a transfer theorem for the projected carrier.

## 3. What the functional equation actually gives

Let `Xi` be a completed function obeying

```text
Xi(s)=Xi(1-s),
Xi(conj(s))=conj(Xi(s)),                            (3.1)
```

and put `A=Xi'/Xi` away from its zeros.  Differentiating (3.1) gives

```text
A(s_-)=-conj(A(s_+)),
A'(s_-)=conj(A'(s_+)).                             (3.2)
```

Apply to `A` the same two-abscissa differential expression as in (2.6):

```text
L_(L,alpha,gamma)[A]
 :=Re{
      (e^(alpha*L)/alpha)*A(s_+)
     -(e^(-alpha*L)/alpha)*A(s_-)
     -L*A(s_+)-A'(s_+)
     -L*A(s_-)-A'(s_-)}.                           (3.3)
```

Equations (3.2) yield the exact collapse

```text
L_(L,alpha,gamma)[A]
 =2*(cosh(alpha*L)/alpha)*Re A(s_+)
  -2*Re A'(s_+).                                   (3.4)
```

Equivalently, for

```text
u(alpha)=log|Xi(1/2+alpha+i*gamma)|,
```

one has

```text
L_(L,alpha,gamma)[A]
 =2*[(cosh(alpha*L)/alpha)*u'(alpha)-u''(alpha)].   (3.5)
```

The functional equation says only that `u` is even.  Evenness supplies no
inequality between `u'` and `u''`.  Moreover `Delta P_T` in (2.6) is a
truncated discrepancy and does not itself satisfy (3.2).  Replacing it by a
completed logarithmic derivative must restore the tail/zero remainder; that
remainder is the original arithmetic problem.  Hence (3.5) is a useful
reorganization, but not a monotonicity or modulus-square identity.

## 4. Exact negative response of a symmetric zero quartet

The obstruction can be stated directly for the actual special kernel.
Modulate the autocorrelation by the center height and define

```text
g_gamma(u)=C(u)cos(gamma*u),
h_gamma(z)=integral_R g_gamma(u)e^(i*z*u)du
          =[K(z-gamma)+K(z+gamma)]/2.               (4.1)
```

On the real axis `h_gamma>=0`.  It is nevertheless negative on a matched
off-axis functional-equation orbit.

### Theorem 4.1 (matched-quartet negativity)

For every `L,alpha>0`, set

```text
A_(L,alpha)=C(0)
 =sinh(alpha*L)/(2*alpha)-L/2>0.                   (4.2)
```

Let

```text
O_(alpha,gamma)
 ={1/2+alpha+i*gamma, 1/2-alpha+i*gamma,
   1/2+alpha-i*gamma, 1/2-alpha-i*gamma}.           (4.3)
```

Then the exact spectral contribution of this quartet is

```text
sum_(rho in O_(alpha,gamma))
 h_gamma((rho-1/2)/i)

 =-2*A_(L,alpha)^2
   +2*Re K(2*gamma+i*alpha).                       (4.4)
```

Furthermore

```text
|K(2*gamma+i*alpha)|
 <=sinh(alpha*L)^2/gamma^2.                        (4.5)
```

In particular the quartet contribution is strictly negative whenever

```text
gamma>sinh(alpha*L)/A_(L,alpha).                   (4.6)
```

#### Proof

At the matched imaginary displacement,

```text
F(i*alpha)
 =integral_(-L/2)^(L/2)sinh(alpha*x)e^(-alpha*x)dx
 =-A_(L,alpha),

F(-i*alpha)=A_(L,alpha),
K(i*alpha)=-A_(L,alpha)^2.                         (4.7)
```

The four spectral parameters `(rho-1/2)/i` are
`+/-gamma+/-i*alpha`.  Using the evenness and conjugation symmetry of `K`
in (4.1) gives (4.4).

For (4.5), write

```text
F(2*gamma+i*alpha)
 =integral_(-L/2)^(L/2)b(x)e^(2*i*gamma*x)dx,
b(x)=sinh(alpha*x)e^(-alpha*x).
```

The function `b` is increasing, and one integration by parts gives

```text
|F(2*gamma+i*alpha)|
 <=[|b(-L/2)|+|b(L/2)|+integral|b'(x)|dx]/(2*gamma)
 =sinh(alpha*L)/gamma.                             (4.8)
```

Since `K=-F^2`, (4.5) follows.  Equations (4.4)--(4.6) are immediate.

## 5. A coefficient-free functional-equation countermodel

The quartet in Theorem 4.1 is realized by the polynomial

```text
H_(alpha,gamma)(s)
 =[(s-1/2)^2-(alpha+i*gamma)^2]
  *[(s-1/2)^2-(alpha-i*gamma)^2].                  (5.1)
```

It satisfies

```text
H(s)=H(1-s),
H(conj(s))=conj(H(s)),

H(1/2+i*t)
 =|-t^2-(alpha+i*gamma)^2|^2>0       (t real).     (5.2)
```

Thus, if `Xi_0` is any real symmetric order-one completed entire function,
then, after an irrelevant positive normalization,

```text
Xi_N(s)=Xi_0(s)*H_(alpha,gamma)(s)^N               (5.3)
```

has the same functional equation, reality symmetry, order, and
critical-line phase as `Xi_0`.  It adds exactly `N` copies of the quartet
(4.3).  Under (4.6), its `h_gamma` zero sum therefore changes by

```text
N*[-2*A_(L,alpha)^2+2*Re K(2*gamma+i*alpha)]<0.    (5.4)
```

Letting `N` grow makes the change arbitrarily negative.  This proves:

> No nonnegative representation of the centered sinh-tent square can be a
> consequence solely of the functional equation, reality, order-one growth,
> critical-line phase, and the carrier's autocorrelation structure.

The countermodel is deliberately not an Euler product and says nothing
negative about the actual zeta square.  Its role is to locate the missing
hypothesis exactly: an actual proof must use coefficient-specific
Euler/von Mangoldt information or an equivalent zero-location input.

## 6. Herglotz and de Branges do not bypass the gate

Put

```text
X(z)=Xi(1/2+i*z).
```

If `-X'/X` is Herglotz on the upper half-plane, it is analytic there and
therefore `X` has no zero there.  Reality then excludes nonreal zeros in the
lower half-plane as well.  Thus the Herglotz hypothesis already contains the
zero-location conclusion which the centered square is meant to prove.
The analogous Hermite--Biehler/de Branges input has the same logical
boundary.  The polynomial (5.1) makes this visible: it preserves the
critical-line phase but inserts nonreal spectral zeros, so its logarithmic
derivative cannot be Herglotz.

For actual von Mangoldt coefficients, the independent Arb certificate in
`ZETA23-CENTERED-COSINE-ONE-SQUARE-ARITHMETIC-GATE-2026-08-12.md` also
refutes the weaker pointwise evenized-multiplier route.  The theorem here is
stronger in a different direction: it is exact, scan-free, and rules out any
functional-equation-only sign argument for the special carrier itself.

## 7. Exact remaining target

The only unresolved sign in this card is the actual coefficient-specific
inequality (2.10), or its finite-aperture Hahn-projected analogue.  The
functional equation reduces its completed logarithmic-derivative component
to (3.5), but supplies no curvature sign.  Theorem 4.1 shows why: the kernel
is an explicit detector of a matched off-critical quartet.

Accordingly the viable direct route is now sharply stated:

```text
prove the actual prime--continuum estimate (2.6), with the explicit
gamma/rational term in (2.10), strongly enough to defeat the negative
matched-quartet response, and then control the Hahn endpoint transfer.
```

That is arithmetic content, not a missing formal completion identity.
