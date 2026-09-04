# Generalized-divisor Voronoi attack on the complete detector

Status: **no unconditional monotonicity interval and no fixed strip are
proved**.  Exact Voronoi dualization preserves a signed, polarized Bessel
transform.  The strongest elementary remainder estimate obtained here is
absolute and conductor-dependent; it cannot control the relative sign at all
heights, especially near a possible zero.

Date: 2026-08-13.

## 1. Exact functional equation and residues

Put

```text
tau=T/2,
lambda_T(n)=n^(-i*tau)sigma_(2i*tau)(n),
D_T(s)=sum_(n>=1)lambda_T(n)n^(-s)
      =zeta(s+i*tau)zeta(s-i*tau).                         (1.1)
```

The completed product

```text
Lambda_T(s)=pi^(-s)Gamma((s+i*tau)/2)Gamma((s-i*tau)/2)D_T(s)
```

satisfies `Lambda_T(s)=Lambda_T(1-s)`.  The two poles of `D_T` are
`1+i*tau` and `1-i*tau`, with residues `zeta(1+i*T)` and
`zeta(1-i*T)`.

For `f` smooth and compactly supported in `(0,infinity)`, the corresponding
untwisted Voronoi formula is

```text
sum_(n>=1)lambda_T(n)f(n)
 =zeta(1+i*T) integral_0^infinity f(x)x^(i*tau)dx
  +zeta(1-i*T) integral_0^infinity f(x)x^(-i*tau)dx
  +sum_(n>=1)lambda_T(n)(V_T f)(n),                        (1.2)

(V_T f)(n)=integral_0^infinity f(x)
                    B_T(4*pi*sqrt(n*x))dx,                 (1.3)

B_T(z)=pi*i/[sinh(pi*T/2)]*[J_(i*T)(z)-J_(-i*T)(z)]
       +4*cosh(pi*T/2)K_(i*T)(z).                          (1.4)
```

The apparent singularity in (1.4) is removable.  At `T=0`, (1.2)--(1.4)
become the classical divisor formula with

```text
B_0(z)=-2*pi*Y_0(z)+4*K_0(z),                              (1.5)
```

and the two residue integrals coalesce to
`integral f(x)(log x+2*EulerGamma)dx`.  Thus all residues and gamma factors
used in the automorphic report are retained; no axis or Tate term has been
dropped.

## 2. Exact signed obstruction after dualization

The dual transform is not positive.  Already at `T=0`,

```text
Y_0(z)=sqrt(2/(pi*z))*sin(z-pi/4)+O(z^(-3/2)),              (2.1)
```

while `K_0(z)` decays exponentially.  Hence `B_0` has infinitely many
positive and negative lobes.  Nonnegative smooth functions supported inside
successive lobes make the individual transforms `(V_0 f)(n)` take either
sign, even though `lambda_0(n)=d(n)>0`.  For `T!=0`, both the real
`J_(iT)-J_(-iT)` combination and `lambda_T(n)` add further oscillation.

This is a rigorous obstruction to a termwise-positive Voronoi or Motohashi
pairing.  The transform is the functional-equation involution, not a positive
operator.  Taking absolute values removes precisely the cancellation between
the `J/Y` and `K` sectors which reconstructs the completed zeta product.

## 3. Strongest elementary remainder bound reached here

For `T!=0`, let

```text
A_T(x)=sum_(n<=x)lambda_T(n),
M_T(x)=zeta(1+i*T)x^(1+i*tau)/(1+i*tau)
      +zeta(1-i*T)x^(1-i*tau)/(1-i*tau),
Delta_T(x)=A_T(x)-M_T(x).                                 (3.1)
```

At the confluent point define instead

```text
A_0(x)=sum_(n<=x)d(n),
M_0(x)=x*log(x)+(2*EulerGamma-1)*x,
Delta_0(x)=A_0(x)-M_0(x).                                 (3.1a)
```

Dirichlet hyperbola plus Euler summation gives, for each fixed real `T`,
the safe estimate

```text
Delta_T(x)<<_T sqrt(x)*log(2*x).                           (3.2)
```

At `T=0`, (3.2) has the usual confluent divisor main term and follows from
the classical Dirichlet hyperbola estimate.  Effective uniform versions
retain dependence on the spectral parameter; no particular polynomial
exponent in `T` is needed or asserted here.  In particular, for
`Re(u)>1/2`,

```text
D_T(u)
 =u*zeta(1+i*T)/[(1+i*tau)(u-1-i*tau)]
  +u*zeta(1-i*T)/[(1-i*tau)(u-1+i*tau)]
  +u integral_1^infinity Delta_T(x)x^(-u-1)dx.             (3.3)
```

The continuous `T=0` value of this identity is

```text
zeta(u)^2
 =u/(u-1)^2+u*(2*EulerGamma-1)/(u-1)
  +u integral_1^infinity Delta_0(x)x^(-u-1)dx.             (3.3a)
```

Estimate (3.2) bounds the last integral and its first `u` derivative by an
absolute quantity depending on `T`.  Known uniform versions are still
absolute and conductor-dependent.  They supply neither a sign nor a
relative bound against `D_T(u)=|zeta(u+i*tau)|^2`, which can be arbitrarily
small and would vanish at an offending zero.

## 4. Binary monotonicity gate

From the audited automorphic identity, with

```text
C_T(u)=(1/4)[u^2+tau^2][(u-1)^2+tau^2]
       *pi^(-u)|Gamma((u+i*tau)/2)|^2,                     (4.1)
```

the complete period is

```text
P_T(2u-1)=C_T(u)D_T(u)=|xi(u+i*tau)|^2.                   (4.2)
```

For `alpha=0.999998` and `0<eta<0.000002`, positivity is exactly

```text
P_T(alpha+eta)>P_T(alpha-eta) for every real T.            (4.3)
```

Substitution of (3.3) into (4.2) is the coefficient-specific Mellin ledger
for this question.  Applying (1.2) to smooth truncations of its remainder
gives the corresponding Voronoi-dual ledger, whose Bessel transform is
signed by Section 2; (3.3) by itself is not that dualization.  Moreover, if
`zeta(u_0+i*tau_0)=0` in the target collar, then (3.3) forces exact
cancellation of its two residue terms by the `Delta_(2tau_0)` Mellin moment,
and (4.2) vanishes there.  More explicitly, put

```text
r_0=2*u_0-1,       eta=r_0-alpha.
```

Then `0<eta<0.000002`, `P_(2tau_0)(alpha+eta)=0`, and the strict inequality
(4.3) fails.  Therefore any **relative** Voronoi remainder estimate strong
enough to force (4.3) already excludes that zero and is itself the desired
fixed-strip theorem in arithmetic form.

The absolute estimate (3.2), the standard stationary-phase estimates for
the two signed pieces of (1.4), and KL/Kuznetsov Plancherel do not provide
that relative control: they retain absolute/conductor-dependent losses,
whereas the comparison value in (4.2) has no unconditional positive lower
bound.

## 5. Verdict

Binary result: **NO STRIP**.

The exact Voronoi formula has been carried through with both residues, all
gamma factors, and the continuous `T=0` limit.  It exposes no hidden positive
dual square.  A fixed strip would require a new coefficient-specific,
relative estimate for the complete signed remainder in (3.3); present
absolute divisor bounds and spectral norms are structurally unable to sign
it.
