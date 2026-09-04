# Automorphic Eisenstein interpretation of the complete KL detector

Status: **no fixed zero-free strip is proved**.  The complete theta/KL
detector is exactly a split-torus period of the completed nonholomorphic
Eisenstein series.  The completion operator is a positive quadratic operator,
but the detector is a cross pairing, not its quadratic form.  Its resolvent is
sign-changing at every nonzero spectral frequency.  The automorphic
calculation reduces the desired sign, with exact constants, to a centered
average of the completed logarithmic derivative, or equivalently to one
generalized-divisor arithmetic block after the Eisenstein residues are
removed.

Date: 2026-08-13.

## 1. Normalizations

Write

```text
Lambda(s)=pi^(-s/2) Gamma(s/2) zeta(s),
xi(s)=(1/2)s(s-1)Lambda(s).                              (1.1)
```

For `z=x+i*y`, define the completed weight-zero Eisenstein series by

```text
E*(z,s)=(1/2)pi^(-s)Gamma(s)
          sum_((c,d) in Z^2, (c,d)!=(0,0))
             y^s/|c*z+d|^(2s).                            (1.2)
```

This is initially defined for `Re(s)>1` and then meromorphically continued.
It equals `Lambda(2s)E(z,s)` in the usual primitive-pair normalization.

Fix a real KL frequency `T`, and put

```text
s_T=(1+i*T)/2,       y=exp(2p),
lambda_T(k)=k^(-i*T/2)sigma_(i*T)(k).                     (1.3)
```

The divisor identity

```text
sigma_(-i*T)(k)=k^(-i*T)sigma_(i*T)(k)                    (1.4)
```

shows that `lambda_T(k)` is the standard unitary Eisenstein Hecke
eigenvalue.  The Fourier expansion of (1.2), restricted to the imaginary
axis, is exactly

```text
E*(i*y,s_T)
 =Lambda(1+i*T)y^((1+i*T)/2)
  +Lambda(i*T)y^((1-i*T)/2)
  +4*sqrt(y) sum_(k>=1) lambda_T(k)
       K_(i*T/2)(2*pi*k*y).                               (1.5)
```

At `T=0`, the two displayed constant terms are understood together by their
meromorphic limiting value.  Formula (1.5) identifies the modular-orbit sum
in the preceding KL report as the nonconstant Fourier part of one Eisenstein
series, rather than as an unrelated Bessel expansion.  Equivalently, the
rectangular two-theta kernel is the split-torus theta lift giving this
Eisenstein series.  There is no omitted cuspidal block in this identity.

## 2. The exact completion is a positive radial operator square

Let `D=d/dp` and

```text
L_T=D^4+2(T^2-1)D^2+(T^2+1)^2
   =[D^2-(1+i*T)^2][D^2-(1-i*T)^2].                      (2.1)
```

The two factors in (2.1) are the radial annihilating factors selected by the
two constant exponents in (1.5).  On every nonconstant Bessel term they give
the exact collapse already found in the KL calculation:

```text
L_T[exp(p)K_(i*T/2)(z)]
 =16 exp(p)z^2[(z^2+9)K_(i*T/2)(z)+6z K'_(i*T/2)(z)],
z=2*pi*k*exp(2p).                                        (2.2)
```

Consequently the **complete**, not orbit-truncated, detector is

```text
Khat_(alpha,eta)(T)
 =1/256 integral_R sinh(alpha*p)sinh(eta*p)
       L_T E*(i*exp(2p),s_T) dp.                         (2.3)
```

This reproduces every constant in the earlier orbit formula: the
nonconstant part in (1.5) contributes a factor `4`, (2.2) contributes `16`,
and `4*16/256=1/4` on the full `p`-line, or `1/2` after evenness and
restriction to `p>=0`.

There is a genuine operator square.  If

```text
A_T=D^2-(1+i*T)^2,                                      (2.4)
```

then on compactly supported `L2` functions

```text
L_T=A_T^* A_T.                                           (2.5)
```

This fact does **not** sign (2.3): after cutoff and passage to the convergent
limit, (2.3) is the cross pairing of `A_T[sinh(alpha p)sinh(eta p)]` with
`A_T E*`, not the squared norm of either vector.

## 3. The torus period evaluates to a product of completed zeta values

For a complex parameter `r`, set

```text
u=(1+r)/2.                                                (3.1)
```

In its initial convergence half-plane, Mellin transformation of the
nonconstant part of (1.5), the standard Mellin integral for `K_nu`, and

```text
sum_(k>=1)lambda_T(k)k^(-u)
 =zeta(u+i*T/2)zeta(u-i*T/2)                              (3.2)
```

give

```text
integral_R exp(r*p) E*_(nonconstant)(i*exp(2p),s_T) dp
 =1/2 Lambda(u+i*T/2)Lambda(u-i*T/2).                     (3.3)
```

The completion polynomial is

```text
Q_T(r)=[r^2-(1+i*T)^2][r^2-(1-i*T)^2]
      =16[u^2+(T/2)^2][(u-1)^2+(T/2)^2].                 (3.4)
```

Thus (3.3), after the exact Tate/Eisenstein continuation implemented by
`L_T`, yields the ordinary rapidly convergent completed period

```text
J_T(r):=1/256 integral_R cosh(r*p)
                   L_T E*(i*exp(2p),s_T) dp
       =1/8 xi(u+i*T/2)xi(u-i*T/2).                       (3.5)
```

Indeed, directly from (1.1) and (3.4),

```text
xi(u+i*T/2)xi(u-i*T/2)
 =Q_T(r)/64 *Lambda(u+i*T/2)Lambda(u-i*T/2),              (3.6)
```

which verifies the factor `1/8` in (3.5).  For real `r` (hence real `u`),
the product in (3.5)--(3.6) is `|xi(u+i*T/2)|^2`; this is the case used
below.  For complex `r`, it must not be denoted by an absolute square.  The
colliding constant terms at `T=0` are again handled by the common limiting
value; `L_0=(D^2-1)^2` annihilates both `exp(p)` and the confluent
`p*exp(p)` term.

Since

```text
sinh(alpha*p)sinh(eta*p)
 =(1/2)[cosh((alpha+eta)p)-cosh((alpha-eta)p)],            (3.7)
```

(2.3)--(3.7) prove the exact automorphic identity

```text
Khat_(alpha,eta)(T)
 =1/16{ P_T(alpha+eta)-P_T(alpha-eta) },
P_T(r)=|xi((1+r+i*T)/2)|^2.                               (3.8)
```

For `alpha=2a`, `eta=2y`, and `T=2t`, (3.8) is precisely
`D_(a,y)(t)=16*Khat_(2a,2y)(2t)`.

Equation (3.8) is the sharp outcome of the automorphic recompletion.  Each
`J_T(r)` is a nonnegative Rankin--Selberg/Tate period, but the detector is the
**difference of two such periods**.  Automorphy has not converted that
difference into a single norm square.

## 4. Exact failure of a maximum-principle/resolvent argument

Under Fourier transformation in `p`, the symbol of (2.1) is

```text
m_T(xi)=((xi-T)^2+1)((xi+T)^2+1)>0.                       (4.1)
```

This proves quadratic-form positivity of `L_T`.  Positivity preservation is
strictly stronger and fails.  With the convention that the inverse Fourier
transform includes `1/(2*pi)`, the Green kernel of `L_T` is

```text
G_T(x)=exp(-|x|)/[4(1+T^2)]
       *[cos(T|x|)+sin(T|x|)/T],                          (4.2)
```

with the continuous value `exp(-|x|)(1+|x|)/4` at `T=0`.  For every
`T!=0`, the bracket in (4.2) changes sign.  Hence `L_T^(-1)` is not
positivity preserving and no one-dimensional maximum principle survives the
exact completion.  This is an obstruction for the complete operator, not an
artifact of separating its Bessel orbits.

Kontorovich--Lebedev Plancherel likewise gives positivity only after
integrating an absolute square over the KL parameter.  Formula (2.3) instead
fixes `T` and is linear in the Eisenstein eigenvalues `lambda_T(k)`.
Kuznetsov positivity has the same mismatch: its continuous term contains
quadratic expressions

```text
|sum_k a_k lambda_T(k)|^2,                               (4.3)
```

whereas (2.3) is the polarized `n=1` cross term.  Applying Kuznetsov merely
reexpresses that cross term together with signed Kloosterman/cuspidal terms;
it does not make it diagonal or nonnegative.

## 5. The exact remaining logarithmic-derivative gate

Put

```text
z_(r,T)=(1+r+i*T)/2,
c=alpha+eta,       d=alpha-eta.                           (5.1)
```

Differentiating the nonnegative period in (3.8) gives an identity valid even
at zeros:

```text
P_T'(r)=Re[xi'(z_(r,T))*conjugate(xi(z_(r,T)))].           (5.2)
```

Therefore

```text
Khat_(alpha,eta)(T)
 =1/16 integral_d^c
    Re[xi'(z_(r,T))*conjugate(xi(z_(r,T)))] dr.            (5.3)
```

Away from a zero, the integrand is `P_T(r)` times

```text
Re xi'(z)/xi(z)
 =Re{1/z+1/(z-1)-(1/2)log(pi)
      +(1/2)psi(z/2)+zeta'(z)/zeta(z)}.                   (5.4)
```

All terms in (5.4) except the last are explicit archimedean/pole terms.  Thus
the exact automorphic sign gate is a lower bound for the centered weighted
average of `Re zeta'/zeta` against `P_T`; pointwise positivity of (5.4) would
be sufficient but is not known in the target collar.  Formula (5.3), not a
pointwise logarithmic-derivative assertion, is the exact necessary and
sufficient centered-average condition.

For the requested values

```text
alpha=0.999998,       0<eta<0.000002,                     (5.5)
```

the real part of `z_(r,T)` ranges only through

```text
0.999998<Re z_(r,T)<1.                                    (5.6)
```

Uniform control of the final term in (5.4) throughout (5.6), for every
height, is precisely fixed-strip-strength arithmetic information.  An
off-strip zero makes the appropriate endpoint period in (3.8) vanish and
forces the detector to be nonpositive, so this gate cannot be bypassed by a
formal spectral positivity theorem.

## 6. Coefficient-specific form: the generalized divisor remainder

The same obstruction can be isolated without logarithmic derivatives.  Put
`tau=T/2` and, for `T!=0`, define

```text
A_T(x)=sum_(k<=x)lambda_T(k),
M_T(x)= zeta(1+i*T)x^(1+i*tau)/(1+i*tau)
       +zeta(1-i*T)x^(1-i*tau)/(1-i*tau),
Delta_T(x)=A_T(x)-M_T(x).                                 (6.1)
```

For each fixed `T!=0`, Dirichlet hyperbola gives
`Delta_T(x)=O_T(sqrt(x) log(2x))`, more than enough for meromorphic
continuation into the collar (5.6).  The implicit constant is not uniform as
`T->0`; that confluent case is treated separately below.  Partial summation
of (3.2) then gives, meromorphically throughout `Re(u)>1/2`,

```text
Z_T(u):=zeta(u+i*tau)zeta(u-i*tau)
 = u*zeta(1+i*T)/[(1+i*tau)(u-1-i*tau)]
  +u*zeta(1-i*T)/[(1-i*tau)(u-1+i*tau)]
  +u integral_1^infinity Delta_T(x)x^(-u-1)dx.             (6.2)
```

For `T=0`, (6.2) has the standard confluent interpretation

```text
A_0(x)=sum_(k<=x)d(k),
M_0(x)=x log x+(2*EulerGamma-1)x,                          (6.3)

zeta(u)^2
 =u/(u-1)^2+u(2*EulerGamma-1)/(u-1)
  +u integral_1^infinity [A_0(x)-M_0(x)]x^(-u-1)dx.       (6.4)
```

Finally, for real `u`,

```text
P_T(2u-1)=C_T(u) Z_T(u),
C_T(u)=(1/4)[u^2+tau^2][(u-1)^2+tau^2]
        *pi^(-u)|Gamma((u+i*tau)/2)|^2.                   (6.5)
```

The factor `C_T(u)` is explicit and positive in the target interval.  Thus
(6.2)--(6.5) give a completely coefficient-specific version of the gate:
after the two Eisenstein residues, the only remaining global block is the
Mellin moment of `Delta_T` (and its `u`-derivative).  Proving that
`C_T(u)Z_T(u)` increases across every interval corresponding to (5.5) is
exactly the required arithmetic inequality.  Absolute values or a generic
divisor-error bound lose the residue/remainder cancellation and do not sign
it uniformly in `T`.

## 7. Truth boundary

What is proved here:

1. `lambda_T(k)` is exactly the unitary Eisenstein Hecke eigenvalue, and the
   full KL orbit sum is the nonconstant Fourier expansion of (1.5).
2. The exact two-factor completion is `A_T^*A_T` and kills all Eisenstein
   constant/Tate terms.
3. The complete detector has the exact automorphic period evaluations
   (2.3), (3.5), and (3.8), with no missing cusp contribution.
4. The inverse kernel (4.2) changes sign, so neither a maximum principle nor
   resolvent positivity follows from completion.
5. KL/Kuznetsov Plancherel is quadratic in Hecke coefficients, while the
   detector is a fixed-frequency polarized linear period.
6. The remaining sign is exactly (5.3)--(5.4), equivalently the generalized
   divisor block (6.2)--(6.5).

What is not proved:

1. positivity of (5.3) for all `T` in the collar (5.5)--(5.6);
2. a uniform sign or relative bound for the `Delta_T` Mellin block;
3. any fixed zero-free strip.

The automorphic route therefore gives a sharp consolidation and a genuine
pruning result, but not a breakthrough strip: the completion has already
used all local/archimedean positivity available to it.  The unresolved sign
is the global Eisenstein scattering/Hecke arithmetic term itself.
