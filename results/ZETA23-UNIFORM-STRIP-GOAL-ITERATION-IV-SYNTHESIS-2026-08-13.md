# Uniform-strip goal, iteration IV: automorphic, tau-Li, and localized-collar closure audit

Date: 2026-08-13.

Status: **no unconditional fixed zero-free strip is proved, and no known
zero-free region is improved.**  This pass attacked the three surviving
coefficient-specific statements from iteration III rather than replacing
them with new equivalent norms:

1. automorphic positivity of the complete theta/KL detector;
2. degree-uniform transport of Freitas coefficients below `tau=2`;
3. the localized Nyman collar on its critical arithmetic window.

All three now have exact closed-form decompositions and have been
cross-audited.  The required arithmetic signs remain unproved.

## 1. Complete KL detector is one Eisenstein torus period difference

Let

```text
s_T=(1+iT)/2,
lambda_T(k)=k^(-iT/2)sigma_(iT)(k),
E*(z,s)=Lambda(2s)E(z,s).                              (1.1)
```

The KL coefficient is exactly the unitary Eisenstein Hecke eigenvalue, and
on the imaginary axis

```text
E*(iy,s_T)
 =Lambda(1+iT)y^s_T+Lambda(iT)y^(1-s_T)
  +4sqrt(y)sum_(k>=1)lambda_T(k)K_(iT/2)(2pi ky).     (1.2)
```

There is no omitted cuspidal block.  With `D=d/dp`, the exact completion is

```text
L_T=[D^2-(1+iT)^2][D^2-(1-iT)^2]=A_T^*A_T.          (1.3)
```

It annihilates both Eisenstein constant terms.  The complete detector is

```text
calKhat_(alpha,eta)(T)
 =1/256 integral_R sinh(alpha p)sinh(eta p)
                    L_T E*(i e^(2p),s_T)dp.          (1.4)
```

For real `r`, the torus period evaluates exactly to

```text
J_T(r)=1/256 integral_R cosh(rp)L_T E*(i e^(2p),s_T)dp
      =1/8 |xi((1+r+iT)/2)|^2.                       (1.5)
```

Hence

```text
calKhat_(alpha,eta)(T)
 =1/16[P_T(alpha+eta)-P_T(alpha-eta)],
P_T(r)=|xi((1+r+iT)/2)|^2.                           (1.6)
```

This verifies the full modular recompletion but does not sign it: the
detector is a difference of two positive periods and a cross pairing after
`A_T`, not a squared norm.

The Fourier symbol of `L_T` is positive, yet its inverse kernel is

```text
G_T(x)=e^(-|x|)/[4(1+T^2)]
       [cos(T|x|)+sin(T|x|)/T],                      (1.7)
```

which changes sign for every `T!=0`.  Thus neither a maximum principle nor
KL/Kuznetsov quadratic positivity controls (1.4).  The exact remaining term
is the centered average, weighted by `|xi(z)|^2`, of

```text
Re xi'(z)/xi(z)
 =explicit pole/gamma terms+Re zeta'(z)/zeta(z),     (1.8)
```

away from zeros; at a zero its nonsingular form is
`Re[xi'(z)conjugate(xi(z))]`.  Equivalently, the same gate is the Mellin
moment of the generalized-divisor remainder after the two Eisenstein
residues.  Automorphy has isolated, not solved, the global arithmetic sign.

## 2. Tau-Li endpoint transport is an alternating infinite transform

Define

```text
A_tau(t)=sum_(m>=1)alpha_m(tau)t^(m-1).
```

The exact generating germ is

```text
A_tau(t)=(1-t)^(-2) xi'/xi(tau/(1-t)).               (2.1)
```

Writing `tau=2/(1+h)` gives

```text
A_tau(t)=(1+h)^2 A_2(-h+(1+h)t),                    (2.2)

alpha_m(tau)
 =(1+h)^(m+1)sum_(j>=0)(-h)^j
   binom(m+j-1,j)alpha_(m+j)(2).                    (2.3)
```

At the target `tau=1.999998`,

```text
h=10^(-6)/(1-10^(-6)),
alpha_m(tau)>=0 for all m
 iff A_2^(k)(-h)>=0 for all k.                       (2.4)
```

Every endpoint coefficient `alpha_m(2)` is positive after conjugate-zero
pairing, and

```text
sum_(m<=M)alpha_m(2)~(1/4)M^2 log M.                (2.5)
```

But (2.3) is alternating and becomes nonperturbative at `m` of order
`1/h`.  The exact differential chain has the same subtractive direction.

A four-zero, functional-equation-symmetric polynomial has every
`alpha_m(2)>0` while having infinitely many negative coefficients at any
fixed `1<tau<2`; multiplying by a centered `cosh` factor preserves order
one and the conclusion.  Therefore endpoint positivity, reality, functional
symmetry, order, and the differential chain do not supply a uniform interval
below two.  By sending the quartet height to infinity, its contribution to
any prescribed finite block of endpoint coefficients can be made arbitrarily
small while the later failure below two persists.

For actual zeta the prime formula is

```text
alpha_(n+1)(tau)
 =G_(n+1)(tau)
  -sum_q Lambda(q)q^(-tau)L_n^(1)(tau log q).        (2.6)
```

The Laguerre generating function recomposes (2.6) exactly into (2.1).  The
standard degree-uniform absolute majorant diverges for `tau<=2`, although
every fixed-degree prime sum converges for `tau>1`.  Thus a successful proof
still requires actual-prime signed cancellation uniformly in degree.

## 3. Localized Nyman collar is a short-cofactor Mertens transform

With the notation of the Nyman report, put

```text
C_n=n gamma(n),
F_n(m)=1-sum_(k<=n)mu(k)floor(m/k)
         +n g(n)floor(m/n).                          (3.1)
```

For `m>=n`, the exact harmonic-hyperbola identity is

```text
F_n(m)=sum_(j<=floor(m/n))[M(floor(m/j))+C_n].       (3.2)
```

On the critical window `m<=R=n^(1/b)`, there are only

```text
n^((1-b)/b+o(1))                                    (3.3)
```

cofactors.  Nevertheless the `j=1` term retains the centered long Mertens
mode.

For `1<=p<=2`, the localized quantity satisfies a weighted Hardy upper
bound and the necessary first-collar bound

```text
Q_(p,b)(n)^p
 >=(2n)^(-1-pb)sum_(n<=m<2n)|M(m)+C_n|^p.           (3.4)
```

For `p=2`, the first collar has the exact ANOVA decomposition

```text
sum_(n<=m<2n)|M(m)+C_n|^2
 =|L_n|^2/n
  +(1/n)sum_(0<=u<v<n)|sum_(u<j<=v)mu(n+j)|^2,      (3.5)

L_n=n^2g(n)+sum_(j<n)(n-j)mu(n+j).                  (3.6)
```

Both terms are nonnegative.  Centering the bridge cannot cancel the scalar
carrier.

The strongest unconditional full-window estimate obtained from the
Vinogradov--Korobov Mertens bound is

```text
Q_(p,b)(n)
 <<n^(1-b)exp[-c_b(log n)^(3/5)(loglog n)^(-1/5)]
 =n^(1-b-o(1)).                                      (3.7)
```

For `b=.999999`, the fixed exponent `10^(-6)` remains.  Modern almost-all
short-interval and averaged-Chowla inputs provide fixed-`A` logarithmic
amplitude savings or power savings in exceptional-set size, not the fixed
energy saving required in (3.4)--(3.5) at one selected `n`.

## 4. Binary conclusion

```text
explicit fixed delta proved                         NO
known zero-free region improved                     NO
complete automorphic KL identity                    YES
automorphic norm/maximum-principle sign             NO
endpoint tau-Li transport                           EXACT, ALTERNATING
soft endpoint/symmetry data propagate below 2       NO -- exact countermodel
localized Nyman short-cofactor collapse             YES
localized fixed-power saving                        NO
```

The three remaining statements are not independent slack sources.  They are
coefficient-specific presentations of the same kind of all-height sign:

- a generalized Eisenstein-divisor Mellin remainder;
- an all-degree signed prime-Laguerre aggregate;
- a centered Mertens scalar plus bridge energy.

No audited current theorem controls any one of them by a fixed power.

Primary artifacts:

- `ZETA23-AUTOMORPHIC-EISENSTEIN-KL-COMPLETE-DETECTOR-GATE-2026-08-13.md`;
- `ZETA23-TAU-LI-ENDPOINT-TRANSPORT-PRIME-LAGUERRE-GATE-2026-08-13.md`;
- `ZETA23-LOCALIZED-NYMAN-COLLAR-HYPERBOLA-AND-ANOVA-GATE-2026-08-13.md`.

This is an audited closure report for iteration IV, not a proof of the
requested strip.
