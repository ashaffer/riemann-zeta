# Husimi reverse localization: the local zero jet cannot pay the uncertainty cost

**Date:** 2026-08-13

**Verdict:** the strict coefficient-specific Husimi hypothesis remains open,
but a zero and its finite multiplicity do not supply the required reverse
inequality.  In the exact monomial zero model the reverse estimate is
impossible whenever `2*m*eta<=alpha`.  Any surviving proof must use global
variation of the nonzero theta/zeta cofactor, hence information from the rest
of the divisor or the complete coefficients.

No zero-free strip is proved.

## 1. The exact reverse target

Use the normalized height Gaussian

```text
G_s(Omega)=s/sqrt(pi)*exp(-s^2*Omega^2),
E_s[Omega^2]=1/(2*s^2).                                 (1.1)
```

For an entire function `F`, put

```text
U_x(T)=|F(x-i*T)|^2,
M_s(x,T_0)=integral_R G_s(Omega)U_x(T_0+Omega)dOmega.    (1.2)
```

The exact theta Husimi theorem gives, with

```text
A=alpha+eta,       B=alpha-eta,
```

the unconditional forward inequality

```text
M_s(A,T_0)>=exp(-4*s^2*alpha*eta)M_s(B,T_0).             (1.3)
```

Thus a zero-free contradiction would follow if a hypothetical outer-line
zero forced the strict reverse of (1.3).  The question here is whether the
local zero jet alone can do that.

## 2. Exact multiplicity theorem

Let

```text
z_0=A-i*T_0,
F_m(z)=C*(z-z_0)^m,       m>=1, C!=0.                   (2.1)
```

Then

```text
M_s(A,T_0)=|C|^2 E_s[Omega^(2m)],
M_s(B,T_0)=|C|^2 E_s[(Omega^2+4*eta^2)^m].              (2.2)
```

> **Theorem 2.1 (local-zero Husimi no-go).**  For every `s>0`,
>
> ```text
> M_s(A,T_0)/M_s(B,T_0)>=exp(-8*m*eta^2*s^2).            (2.3)
> ```
>
> Consequently, if
>
> ```text
> 2*m*eta<=alpha,                                       (2.4)
> ```
>
> then the candidate reverse inequality
>
> ```text
> M_s(A,T_0)<exp(-4*s^2*alpha*eta)M_s(B,T_0)             (2.5)
> ```
>
> fails for every smoothing scale `s`.

### Proof

Write `v=1/(2s^2)`.  Gaussian moments give

```text
E_s[Omega^(2k)]=(2k-1)!!*v^k.                           (2.6)
```

Expanding the denominator of (2.2),

```text
M_s(B,T_0)/M_s(A,T_0)
 =sum_(j=0)^m binom(m,j)(4*eta^2)^j
   v^(-j)*(2m-2j-1)!!/(2m-1)!!.                        (2.7)
```

Every double-factorial ratio in (2.7) is at most one.  Hence

```text
M_s(B,T_0)/M_s(A,T_0)
 <=(1+4*eta^2/v)^m
 =(1+8*eta^2*s^2)^m
 <=exp(8*m*eta^2*s^2),                                  (2.8)
```

which proves (2.3).  Under (2.4),

```text
exp(-8*m*eta^2*s^2)>=exp(-4*alpha*eta*s^2),             (2.9)
```

so (2.5) is impossible.  QED.

For a simple zero the ratio is exactly

```text
M_s(A,T_0)/M_s(B,T_0)=1/(1+8*eta^2*s^2).                (2.10)
```

Thus the quadratic horizontal gain from a simple zero loses to the linear
`alpha*eta` Husimi cost throughout the thin-displacement regime
`2*eta<=alpha`.

## 3. The exact cofactor price

Now write locally

```text
F(z)=(z-z_0)^m G(z).                                    (3.1)
```

Suppose, as a deliberately strong model assumption, that on both complete
Gaussian sampling lines

```text
0<g_-<=|G(x-i*(T_0+Omega))|<=g_+<infinity
for x in {A,B}, Omega in R,                              (3.2)
K=g_+/g_-.
```

The same comparison gives

```text
M_s(A,T_0)/M_s(B,T_0)
 >=K^(-2)exp(-8*m*eta^2*s^2).                           (3.3)
```

When `alpha>2*m*eta`, the reverse target (2.5) therefore requires

```text
log K>2*eta*(alpha-2*m*eta)*s^2.                        (3.4)
```

Equation (3.4) is the exact escape bill in this bounded-cofactor model.  The
nonzero factor must vary exponentially on the same horizontal/vertical tube
at the rate missing from the zero jet.

Assumption (3.2) is not asserted for `xi`: other zeros can make its global
lower bound vanish, and its gamma factor creates substantial height
variation.  The point of (3.4) is logical.  Once the pure zero factor is
removed, any reverse-localization proof must control a relative global
cofactor norm.  That is coefficient/divisor information, not a consequence
of the candidate equation or multiplicity alone.

## 4. Disposition of H3

For the first strip scale `alpha` is about `.49`, while the thin displacement
`eta` is at most about `.01` and may be arbitrarily smaller.  A simple zero,
and more generally every fixed multiplicity once `eta` is small enough,
falls in (2.4).  Optimizing the Gaussian scale cannot repair this mismatch.

The evidence therefore closes the following forms:

```text
outer zero alone => Husimi reverse estimate:             FALSE;
finite multiplicity alone => reverse estimate:           FALSE in (2.4);
generic local Taylor/maximum-modulus argument:            INSUFFICIENT.
```

The strict surviving hypothesis is narrower:

```text
a hypothetical outer zero plus the complete theta/zeta cofactor
forces the relative variation needed to beat (3.4).       OPEN.          (4.1)
```

This is not contradicted by the theorem, but it is no longer a local-zero or
generic phase-space route.  It is a global coefficient-specific inequality,
and must be judged against the same finite-head nonidentifiability and
same-state tests as the other surviving arithmetic gates.
