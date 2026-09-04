# QP prime-power multiscale gate: nested bandwidth and illegal band switching

**Date:** 2026-08-15

**Verdict:** splitting the actual shell into the layers `p^k~Y` does not
close fixed-power QP.  The prime layer `k=1` has the largest deterministic
quadrature bandwidth; every proper-power layer has a strictly smaller one.
The high-frequency estimate for each layer remains subpower.  Convex or
signed fixed mixing cannot improve the certified error, and a
frequency-dependent switch between layer certificates leaves the prescribed
prime-power node span.

There are two exact arithmetic obstructions.

1. A two-term band switch translates every active log node by one common
   amount.  Unless the switch is constant, at most `O(log Y)` actual
   prime-power nodes survive; a dense carrier cannot.
2. For the natural layer Dirichlet series, a zeta zero `rho` produces a pole
   at `rho/k`.  In any fixed signed combination, the smallest active layer's
   sufficiently rightward zero pole cannot cancel against a higher layer.

These statements rule out the proposed *layerwise quadrature + layerwise
prime twist + band switch* proof package.  They do not rule out an arbitrary
coefficient-sensitive finite-band Delsarte antenna.  No QP bound or strip is
proved here.

---

## 1. Layer sizes and their deterministic quadrature bandwidths

For fixed `k>=1`, put

```text
U_(k,Y)={log(p^k/Y): |log(p^k/Y)|<w}.                 (1.1)
```

The underlying primes have size `X=Y^(1/k)`, so

```text
#U_(k,Y)=Y^(1/k+o(1)).                                (1.2)
```

Baker--Harman--Pintz at scale `X` gives prime-log mesh
`X^(-19/40)`.  Multiplication by `k` changes only a constant, hence

```text
h_(k,Y)<<_(k,w)Y^[-19/(40k)].                         (1.3)
```

Positive hat quadrature on this layer has the same exact second-order error
as on the prime layer:

```text
|P_(k,Y)(t)-b(t)| <<(1+t^2)h_(k,Y)^2.                (1.4)
```

To make the interpolation term at `t=Y^sigma` at most `Y^-c`, (1.4)
requires

```text
sigma <=19/(40k)-c/2.                                (1.5)
```

At the convenient target `c=.019`,

```text
k=1: sigma<=.4655,
k=2: sigma<=.228,
k=3: sigma<=.148833... .                              (1.6)
```

Thus higher prime powers do not bridge the known prime-layer endpoint to
`Y^(50/33)`; their certified bands are strictly nested inside it.  Higher
order interpolation changes the power of `t h_(k,Y)` but not the Nyquist
boundary `19/(40k)`, so it does not reverse the ordering.

The union of layers might have better *unknown* mesh than (1.3).  No claim
that (1.3) is a lower bound is made.  The exact conclusion is that the
published layerwise mesh inputs cannot extend the `k=1` theorem.

---

## 2. Proper powers need a polynomial amplification to be material

The complete proper-power population is

```text
sum_(k>=2)#U_(k,Y)=Y^(1/2+o(1)),                     (2.1)
```

whereas the prime population is `Y^(1+o(1))`.  Under any bounded comparable
per-node rule, the total proper-power mass after normalization is therefore

```text
Y^(-1/2+o(1)).                                       (2.2)
```

This is much smaller than the target error `delta=Y^(-.019)`.  To give the
`k`th layer mass `Y^-c`, its average node weight must be amplified relative
to a prime node by

```text
Y^[1-1/k-c+o(1)].                                    (2.3)
```

For squares and `c=.019`, the tax is `Y^.481`.  Such amplification is legal;
it simply means that proper powers are not a perturbative correction.  They
become a separate antenna, with the smaller bandwidth in (1.6) and its own
high-frequency prime-twist problem.

---

## 3. Fixed mixing does not implement a band switch

Let `P_k` be normalized layer antennas and suppose the separate layer
estimates in the proposed proof package give the modulus bounds

```text
|P_k(t)|<=epsilon_k                on the target band. (3.1)
```

A positive fixed mix `P=sum alpha_k P_k` has the certified floor

```text
P(t)>=-sum alpha_k epsilon_k,
alpha_k>=0,                 sum alpha_k=1.            (3.2)
```

The right side is never better than the best component error.  For a signed
mix with `sum beta_k=1`, the triangle certificate is

```text
P(t)>=-sum |beta_k|epsilon_k,                         (3.3)
```

and `sum|beta_k|>=1`.  Cross-layer cancellation could beat (3.2)--(3.3),
but proving it is a new joint arithmetic theorem; it is not supplied by the
separate layer estimates.

Choosing one layer on the low band and another on the high band would require
a frequency-dependent partition.  The next theorem shows why the simplest
such partition is not legal on the fixed node spectrum.

---

## 4. Exact one-shift band-switch obstruction

Let

```text
U_Y={log(n/Y):n=p^a, |log(n/Y)|<w},
P(t)=sum_(u in U_Y)c_u exp(itu).                       (4.1)
```

Assume `2w<log 2`, as in the project.  Hence at most one power of each prime
base occurs in the shell.

### Theorem 4.1 (a nonconstant two-term switch destroys dense support)

Let `v!=0` and `z!=0`.  If

```text
(1+z exp(ivt))P(t)                                   (4.2)
```

has all its Fourier frequencies in `U_Y`, then every active node `u_n`
satisfies

```text
u_n+v in U_Y.                                        (4.3)
```

If `exp(v)` is irrational, `P=0`.  If `exp(v)=a/b` in lowest terms, then

```text
#supp(P)<=omega(ab)=O(log Y).                         (4.4)
```

#### Proof

The shifted frequency `u+v` in (4.2) has coefficient `z c_u`.  Shift is
injective, so if `u+v` is not an original node there is no other term which
can cancel it.  This proves (4.3).

Writing `u_n+v=u_m` gives

```text
m/n=exp(v).                                          (4.5)
```

The left side is rational, proving the irrational case.  In the rational
case write `n=p^r`, `m=q^s`.  Every prime valuation outside `ab` is the same
on the two sides of `bm=an`.  If `p` did not divide `ab`, this forces
`p=q` and `r=s`, hence `a/b=1`, contrary to `v!=0`.  Therefore the base of
every active `n` divides `ab`.  The narrow shell contains at most one power
of each such base, proving (4.4).  If one pair exists, `a` and `b` divide
shell integers of size `O(Y)`, so the final logarithmic bound is uniform.
QED

For the cosine span, symmetrize the spectrum to `+/-U_Y`.  A translated
frequency can then return with either sign.  Besides `m/n=exp(v)` and its
reciprocal, the only new equations are

```text
mn=Y^2 exp(v)       or       mn=Y^2 exp(-v).          (4.6)
```

For rational half-integer `Y`, existence of a solution again forces
`exp(v)` to be rational.  In (4.6), every active prime-power base divides
the numerator or denominator of one fixed rational of height `Y^O(1)`;
the narrow-shell one-power property again leaves only `O(log Y)` nodes.  A
real two-sided switch, which generates both shifts `+v` and `-v`, imposes
both overlap conditions.

A switch with continuum Fourier spectrum leaves the finite node span
immediately.  More complicated finite switches require a multi-shift
overlap theorem, but Theorem 4.1 and (4.6) already kill the elementary
partition-of-unity multiplier needed to glue two layer certificates without
paying their uncontrolled bands.

---

## 5. Scaled zero poles do not cancel across fixed layers

Put

```text
P_prime(s)=sum_p (log p)p^(-s).                       (5.1)
```

Möbius inversion of the Euler logarithmic derivative gives, initially for
`Re(s)>1`,

```text
P_prime(s)=sum_(m>=1)mu(m)[-zeta'/zeta(ms)].          (5.2)
```

The natural `p^k` layer has Dirichlet series `P_prime(ks)`.  A zeta zero
`rho` therefore produces its leading layer singularity at

```text
s=rho/k.                                             (5.3)
```

Consider any finite fixed signed combination

```text
F(s)=sum_(k=k_0)^K alpha_k P_prime(ks),
alpha_(k_0)!=0.                                      (5.4)
```

### Proposition 5.1 (rightward zero-pole separation)

If `rho=beta+i gamma` is a zeta zero with

```text
beta>k_0/(k_0+1),                                    (5.5)
```

then the pole contributed by the `k_0` layer at `rho/k_0` cannot be
cancelled by any `k>k_0` term in (5.4).

Indeed a singularity of the `m`th term in (5.2) for layer `k` at the same
point would require a zeta zero with real part

```text
m k beta/k_0 >1,                                    (5.6)
```

which is impossible.  The pole at one cannot occur there for the same
strict inequality.  Thus the coefficient of the pole is the nonzero
`k_0`-layer coefficient alone.

Compact log-shell smoothing multiplies this residue by a Mellin transform.
For the positive tent at exact ordinate resonance that factor is positive,
so it does not remove the pole.  Therefore fixed signed prime-power-layer
combinations do not algebraically cancel a hypothetical sequence of zeros
approaching `Re(s)=1`.  Any contour-shift proof of a fixed power still meets
a zero-free-strip obstruction, now at the scaled locations (5.3).

This proposition is scoped to natural layer Dirichlet series.  Arbitrary
scale-dependent Delsarte coefficients need not possess (5.1)--(5.4), so it
is not a no-go theorem for full QP.

---

## 6. Binary disposition

```text
prime-layer fixed-power quadrature through Y^.4655:      PROVED (PRIOR);
proper-power layer extends that endpoint:                NO;
layerwise KMT/VK high-tail saving:                       SUBPOWER;
bounded natural proper-power mass at QP scale:           NEGLIGIBLE;
material proper-power reweighting:                       COSTS Y^.481 (k=2);
convex/signed mixing improves separate certificates:     NO;
two-term frequency-dependent band switch stays legal:    NO, O(log Y) SUPPORT;
fixed natural layer combination cancels near-1 zeros:    NO;
joint coefficient-sensitive cross-layer cancellation:    OPEN;
full-band fixed-power QP or uniform strip:                NOT PROVED.
```

Executable replay:

- `src/qp_prime_power_multiscale_gate.py`;
- `src/test_qp_prime_power_multiscale_gate.py`.
