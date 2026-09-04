# Uniform-strip goal, iteration III: collar, Jensen--Li, and Speiser gates

Date: 2026-08-12.

Status: **no unconditional fixed zero-free strip is proved, and no known
zero-free region is improved.**  This third pass tested three classical
functional-analytic routes that do not begin with the Bergman reciprocal
hyperbola or the full-theta KL expansion:

1. quantitative Nyman--Beurling approximation;
2. growing Jensen/Pólya-frequency and `tau`-Li criteria;
3. Speiser and derivative-zero geometry.

Each route gives an exact reduction or obstruction.  None supplies the
required uniform arithmetic estimate.

## 1. Quantitative Nyman--Beurling collar

Let `rho(x)=x-floor(x)` and use the standard Báez-Duarte combination

```text
B_n(x)=sum_(k<=n)mu(k)rho(1/(kx))-n g(n)rho(1/(nx)),
E_n=chi_(0,1)+B_n.                                      (1.1)
```

The exact endpoint correction gives, up to the immaterial single endpoint
`x=1/n`,

```text
essential supp(E_n) subset (0,1/n),  ||E_n||_infinity<=3n (1.2)
```

for all sufficiently large `n`.  At every nontrivial zero
`rho=beta+i gamma`, Mellin evaluation gives

```text
integral_0^1 E_n(x)x^(rho-1)dx=1/rho.                 (1.3)
```

Among functions supported in `(0,1/n)`, bounded by `3n`, and with fixed
`L1` mass, the decreasing weight `x^(beta-1)` is maximized by filling the
interval next to zero.  This sharp bathtub calculation yields

```text
||E_n||_1 >= (beta/|rho|)^(1/beta)
             (3n)^[-(1-beta)/beta].                  (1.4)
```

Conversely, interpolation and the `L^p` Nyman criterion show that

```text
||E_n||_1=o(n^(-alpha))
  => no zero with Re(rho)>=1/(1+alpha).               (1.5)
```

Therefore the explicit target `Re(rho)<.99` would follow from

```text
||E_n||_1=o(n^(-1/99)).                               (1.6)
```

This is an exact collar-rate criterion, not a proved estimate.  Known
PNT/zero-free-region inputs supply decay but no fixed power.  Weighted and anisotropic
versions do not remove the exponent: the dual Mellin evaluation pays the
corresponding point-evaluation growth.  The discrete collar is the same
coefficient block in the weighted Dirichlet-space model, and its first
piece is a centered Mertens block.  Reweighting therefore returns to the
principal arithmetic mode rather than proving (1.6).

## 2. Squared xi turns a strip into a parabola

Put

```text
Y(w)=xi(1/2+w)=F(w^2),
F(z)=sum_(n>=0)gamma_n z^n/n!.                       (2.1)
```

For `z=w^2`,

```text
|z|+Re(z)=2[Re(w)]^2.                                (2.2)
```

Thus the half-strip `|Re(w)|<=a` is exactly the parabolic zero region

```text
P_a={z: |z|+Re(z)<=2a^2}.                            (2.3)
```

The base Jensen row satisfies

```text
J^(d,0)(z/d) -> F(z)                                 (2.4)
```

locally uniformly.  For each fixed `n`, derivative rows converge to
`F^(n)`, not `F`; their eventual hyperbolicity does not locate the original
zeros.

A disk-wide Rouche certificate through zeta height `T` needs at least

```text
d>=N_F(T^2)=(1/(2pi)+o(1))T log T.                  (2.5)
```

Schoenberg's sharp finite-`PF_k` sector certificate must additionally have

```text
k>=(pi/(2a)+o(1))dT,
```

and therefore, optimistically,

```text
k>=(1/(4a)+o(1))T^2 log T.                          (2.6)
```

Known simultaneous Jensen hyperbolicity wedges apply only for a large
derivative shift `n`; they do not intersect the required base edge `n=0`.
The identity

```text
(J^(d,n))'=d J^(d-1,n+1)                            (2.7)
```

cannot be integrated backwards without recovering the missing constant
`gamma_n` and verifying all critical-value inequalities.  Those constants
are exactly the coefficient-specific information the derivative wedge
discarded.

## 3. The exact tau-Li criterion and its signed prime kernel

Freitas's coefficients satisfy

```text
alpha_m(tau)
 =1/tau sum_rho [1-(rho/(rho-tau))^m].               (3.1)
```

For `tau>=1/2`,

```text
alpha_m(tau)>=0 for every m
 iff zeta has no zero with Re(rho)>tau/2.             (3.2)
```

Consequently the `10^(-6)` strip target is exactly

```text
alpha_m(1.999998)>=0 for every m>=1.                 (3.3)
```

For a zero at `beta=tau/2+delta`, height `T`, the usual dominant-zero
amplifier has

```text
log |rho/(rho-tau)|=tau delta/T^2
                       +O_(tau,delta)(T^(-4)),       (3.4)
```

so its e-fold degree is `(1+o(1))T^2/(tau delta)`.  This is the exact scale
of that standard amplification mechanism, not a universal lower bound on
every cancellation-sensitive inference.

Although `tau=1.999998>1` makes the Euler series absolutely convergent, its
prime formula contains

```text
-sum_(q>=2)Lambda(q)q^(-tau)L_n^(1)(tau log q),      (3.5)
```

whose Laguerre factor changes sign.  The standard uniform majorant replaces
`q^(-tau)` by `q^(-tau/2)` and diverges for every `tau<=2`.  Its wall is
exactly the safe endpoint; endpoint continuity is nonuniform in degree.
Thus (3.3) remains an actual-prime signed-cancellation theorem, not a
corollary of coefficient positivity.

## 4. Speiser geometry does not localize the offender

For a centered functional-equation quartet at horizontal displacement `a`
and height `g`, the exact polynomial model is

```text
Q_(a,g)(z)=((z-ig)^2-a^2)((z+ig)^2-a^2),
Q'_(a,g)(z)=4z(z^2+g^2-a^2).                        (4.1)
```

When `g>a`, all three critical points of `Q` lie on the center line.  Their
near-height displacement is only

```text
g-sqrt(g^2-a^2)=a^2/(2g)+O(g^(-3)).                 (4.2)
```

Thus a symmetric off-line zero quartet does not, by Gauss--Lucas or local
critical-point geometry, force an off-axis `xi'` zero.

Speiser's theorem remains exact globally: an off-critical zeta zero implies
the existence of a `zeta'` zero left of the critical line.  But it is not a
per-zero depth-preserving map.  The Levinson--Montgomery counting relation

```text
N_1^-(T)=N^-(T)+O(log T)                              (4.3)
```

absorbs a single sparse offender in its error, and the known derivative-zero
regions allow the resulting left-half zero.  A strip proof by this route
would need a new quantitative per-zero Speiser theorem or a replication
statement; current density estimates still permit one.

## 5. Consolidated verdict

The three route packages give exact and useful reductions, but not the
missing estimates.

```text
Nyman collar        requires L1 decay n^[-delta/(1-delta)];
base Jensen row     requires height-uniform parabolic control;
tau-Li              requires all signed prime-Laguerre sums positive;
Speiser             loses per-zero horizontal depth/localization.
```

The repeated obstruction is again a principal coefficient or integration
constant: the centered Mertens collar, the missing base-row coefficient, the
signed Li prime aggregate, or the nonlocalized derivative zero.  None is
controlled by the corresponding soft Hilbert-space, derivative-row, or
counting theorem.

## 6. Binary conclusion

```text
explicit fixed delta proved                         NO
known zero-free region improved                     NO
sharp Nyman collar-rate criterion                   YES
base-Jensen parabolic criterion                     YES
tau-Li criterion at 1.999998                        YES
quantitative per-zero Speiser map                   NO
remaining input                                     coefficient-specific cancellation or per-zero localization
```

Primary artifacts:

- `ZETA23-QUANTITATIVE-NYMAN-BEURLING-COLLAR-RATE-GATE-2026-08-12.md`;
- `ZETA23-GROWING-JENSEN-TAU-LI-PARABOLIC-STRIP-GATE-2026-08-12.md`;
- `ZETA23-SPEISER-DERIVATIVE-ZERO-QUARTET-GATE-2026-08-12.md`.

This is a third audited reduction pass, not the requested strip proof.
