# Exact-alias and principal-resonance theorems for the critical tower

**Date:** 2026-08-27
**Binary verdict:** two previously open positive sectors of the balanced
tower admit lossless, mask-sensitive estimates: exact reciprocal aliases and
exact principal linear resonances.  The nonprincipal near-resonant sector is
not proved, so neither DRPLS nor the sharp four-cycle theorem follows.

## 1. Exact model

Put

```text
F=N^8, R=N^25, q=2FR, D=F^2, T=q^3/8=F^3R^3,
z(m,n)=(Rm-n,(R+1)m-n),  t(z)=m-Fn.
```

The explicit balanced rectangle has `m` in a fixed interval of `Theta(F)`
integers and `0<=n<F`.  A cell in an ordered lane pair `(m,m')` has product

```text
w=(Rm-n)((R+1)m'-n')
```

and reciprocal phase `e(T/w)`.  The actual top band is
`K=floor(R/F)`, `K<h<=2K`; the arguments below apply throughout
`K<=q/D=2R/F`.

## 2. Exact reciprocal-phase theorem

For a positive integer `w`, set

```text
g=gcd(w,T), d=w/g, s=T/g,
kappa_T(w)=(d, s mod d),
```

where the residue is chosen in `[0,d)` and `0/1` is the zero convention.
Since `gcd(s,d)=1`, this is precisely the reduced fraction representing
`T/w` modulo one.  Therefore

```text
e(T/w)=e(T/w')  iff  kappa_T(w)=kappa_T(w').       (2.1)
```

For a fixed key `(d,a)`, every possible product has the form `w=dg` with
`g|T`.  More precisely its product fibre is

```text
{dg: g|T, gcd(d,T/g)=1, T/g == a (mod d)}.         (2.2)
```

Thus one phase key contains at most `tau(T)=q^o(1)` products.  Both physical
coordinate projections are injective on the complete canonical shell, and a
fixed product has at most `tau(w)=q^o(1)` factor realizations.  Consequently
every exact phase fibre contains

```text
Delta_q <= tau(T) max_(w<<q^2) tau(w)=q^o(1)       (2.3)
```

cells, uniformly in `N`.

Let `c_alpha` be arbitrary complex cell coefficients.  The exact-alias
matrix is a disjoint union of all-one blocks, one for each key.  Hence

```text
K sum_theta |sum_(kappa_T(w_alpha)=theta)c_alpha|^2
 <= K Delta_q sum_alpha |c_alpha|^2.               (2.4)
```

In lane-pair coordinates, if `r_P(theta)` is the number of cells of packet
`P` in a phase fibre, its positive exact Gram is

```text
E_(P,Q)=K sum_theta r_P(theta)r_Q(theta).
```

Every packet has `O(F^2)` cells, so

```text
sup_P sum_Q E_(P,Q) << K F^2 q^o(1),               (2.5)
||E||_(2->2)       << K F^2 q^o(1),
sum_(P,Q)E_(P,Q)   << K F^4 q^o(1)
                    <= (q^2/K)q^o(1).              (2.6)
```

This proves the required sharp scale for exact aliases, including arbitrary
signs and masks.  It does not estimate distinct keys separated by `O(1/K)`.

## 3. Equal-product classification

For balanced representatives with lane and internal coordinates `O(F)`,

```text
w=R^2 mm' + R(mm'-mn'-m'n) + n(n'-m').            (3.1)
```

Since `R/F^2=N^9`, equality of two such products forces equality of all
three signed base-`R` coefficients; negative digits cannot carry.  Put

```text
alpha=n/m, beta=n'/m'-1.
```

Then

```text
w=mm'(R-alpha)(R-beta),
```

and two balanced cells have the same product exactly when

```text
mm'=MM' and {n/m,n'/m'-1}={u/M,u'/M'-1}.           (3.2)
```

The second ordering is the factor-swap branch; there is no hidden third
branch.  In particular, transposed cells differ by the exact identity

```text
(aR-n)(b(R+1)-n')-(bR-n')(a(R+1)-n)=a n'-b n.     (3.3)
```

The algebra in (3.1) and (3.3) is machine-checked in
`lean/weilcert/QPSelfOrbitTowerCubicSurvival.lean`.

## 4. A mask-sensitive theorem for exact principal resonances

For an ordered lane pair `(a,b)`, the two leading internal linear
frequencies are

```text
lambda_(a,b)=F^3/(a^2b),  mu_(a,b)=F^3/(ab^2).
```

Their least simultaneous integral period is

```text
d_F(a,b)=lcm(a^2b/gcd(a^2b,F^3),
             ab^2/gcd(ab^2,F^3)).                  (4.1)
```

The carrier introduces no new congruence: for `a=alpha F`, `b=beta F`,

```text
C_(a,b)=F(R-1)/(alpha beta)
       =a(R-1)lambda_(a,b)=b(R-1)mu_(a,b).         (4.2)
```

Hence `d_F(a,b)|h` kills the carrier and both linear characters exactly.

There are only `q^o(1)` principal packets at any one frequency.  Indeed, if
`d_F(a,b)=d`, then

```text
a^2b | dF^3 and ab^2 | dF^3.                       (4.3)
```

Thus both `a` and `b` divide `dF^3`, giving at most
`tau(dF^3)^2=q^o(1)` lane pairs for fixed `d`.  If `d|h`, there are only
`tau(h)=q^o(1)` choices for `d`.  Therefore

```text
# {(a,b): d_F(a,b)|h}=q^o(1).                      (4.4)
```

Define the principal projection

```text
G_P^0(h)=1_(d_F(P)|h) G_P(h).
```

Pointwise Cauchy--Schwarz using (4.4), followed by summation in `h`, proves
for arbitrary packet coefficients `z_P`

```text
sum_(h~K)|sum_P z_P G_P^0(h)|^2
 <=q^o(1) sum_P |z_P|^2 sum_(h~K)|G_P^0(h)|^2.     (4.5)
```

This is a genuine vector-valued, mask-sensitive two-inverse large-sieve
theorem for the exact principal sector.  It retains both lane indices and
does not rely on cancellation between coefficients.

Since a packet has at most `F^2` cells,

```text
sum_(h~K)|G_P^0(h)|^2 <= K F^4,
K F^4 asymp q^2/K.                                  (4.6)
```

Thus `(4.5)` is itself at the sharp dyadic scale, up to `q^o(1)`.
The stronger hinge-by-hinge density statement is proved in
`ZETA23-QP-UNIFORM-WEIGHTED-RESONANCE-DEGREE-2026-08-27.md`.

## 5. What remains

The transpose quotient has an explicit quadratic scaling limit.  Rational
three-lane hinges persist because their periods have common multiples; the
families with periods `(49,49)`, `(81,243)`, and `(25,100)` have observed
nonzero limiting correlations.  These are compatible with (4.5): each fixed
period fibre is divisor-controlled.

The unresolved terms are nonprincipal near resonances, where neither linear
frequency is exactly integral but both lie within the `1/F` Fejer window.
On the critical gcd slice, the diagonal specialization contains the
**primitive** near-cubic condition

```text
A u^3-BF^3=Delta,
gcd(A,B)=1,
A,B~F^(9/16), 0<|Delta|<=F^(7/16).                 (5.1)
```

Indeed, if the unreduced multiplier and nearest integer are `h=cB` and
`t=cA`, then `c=gcd(h,t)` and division by `c` gives `(5.1)`.  Thus a raw
nonprimitive formulation omits a genuine condition of the reduction.
No bound at the required `F^(9/16+o(1))` primitive scale is proved here.
Consequently

```text
exact reciprocal-alias sector:             PROVED at sharp scale;
equal-product/factor-swap classification:   PROVED;
exact principal-resonance vector theorem:   PROVED;
nonprincipal near-resonant aggregation:     OPEN;
full DRPLS:                                 OPEN;
sharp four-cycle bound:                     NOT PROVED.
```
