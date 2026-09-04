# Fixed-saving Type-II theorem card

Status: independent parameter and primary-source audit, 2026-08-11.  This
report proves no new zero-free strip.  It identifies the strongest currently
applicable bound and the exact theorem still missing.

## 1. Outcome

For fixed `ell`, fixed spline order `k`, and

```text
U=V=floor(x^theta),
0<theta<=theta_k=1/2-1/[4(k+1)],
```

the strongest unconditional estimate that applies to the **completed**
Vaughan aggregate has Vinogradov--Korobov, not fixed-power, strength:

```text
abs(B_(U,V)^(k)(x)-Z_(U,V)^(k)(x))
 <<_(ell,k,theta)
 x^(1/2) exp{-c (log x)^(3/5)(loglog x)^(-1/5)}.       (1.1)
```

At the endpoint `theta=theta_k`, the Euler comparison contributes an
additional `O_(ell,k)(1)`, which is absorbed in (1.1).  Below the endpoint it
tends to zero.  On a fixed logarithmic block, (1.1) gives

```text
E_I
 <<X exp{-c' (log X)^(3/5)(loglog X)^(-1/5)}.          (1.2)
```

Thus the currently proved exponent is

```text
eta(X)=c (log X)^(-2/5)(loglog X)^(-1/5)->0,          (1.3)
```

not a fixed `eta>0`.  Neither (1.1) nor the stronger growing-order cooling
bound proves a fixed strip.

The faithful missing theorem is: for some fixed `delta>0`, prove

```text
O_full(X)<<X^(1-delta),                               (1.4)
```

where `O_full` is the complete ordinary dual defined in Section 4 below.
This would imply

```text
sup_rho Re(rho)<=1-delta/2                            (1.5)
```

and hence a uniform zero-free strip of half-width `1/2-delta/2`.  In the
pointwise normalization `delta=2 eta`.

## 2. Exact fixed-order reduction

Put

```text
a_(U,V)(n)
 =sum_(dbm=n; d>U,b>V)mu(d)Lambda(b)
 =(mu_(>U)*Lambda_(>V)*1)(n).                         (2.1)
```

The completed primitive is

```text
F_(U,V)(R)
 =sum_n a_(U,V)(n)n^(-1/2)Phi_(h,k)(R-log n)-Z(R).    (2.2)
```

Its compact coboundary is

```text
G_(U,V)(R)
 =sum_n a_(U,V)(n)n^(-1/2)W_(ell,k)(R-log n)
  -[Z(exp(R+ell))-Z(exp R)],                          (2.3)
```

up to the explicitly bounded Euler defect.  For a nonnegative block weight
`psi`, the exact physical-space dispersion form is

```text
int psi(R)abs(G_(U,V)(R))^2dR

 =sum_(m,n) a(m)a(n)/(sqrt(mn))
   int psi(R)W(R-log m)W(R-log n)dR

 -2 Re sum_n a(n)/sqrt(n)
   int psi(R)W(R-log n)conjugate(z(R))dR

 +int psi(R)abs(z(R))^2dR.                            (2.4)
```

Every unequal-product term and both center terms in (2.4) are essential.
In frequency space, if

```text
A_I(t)=sum_n a(n)n^(-1/2-it),                         (2.5)
```

with the finite active product range understood, then (2.4) is exactly

```text
1/(2pi)^2 double_integral
  psihat(u-t)What(t)conjugate(What(u))
  A_I(t)conjugate(A_I(u))dtdu

-1/pi Re integral What(t)A_I(t)
                   conjugate((psi z)^hat(t))dt

+int psi abs(z)^2.                                   (2.6)
```

For products in the compact coboundary window, `n` is comparable to `x`.
The two Vaughan variables `d` and `r=bm` lie between `x^theta` and
`x^(1-theta)` up to fixed factors, while

```text
m<<x^(1-2theta).                                     (2.7)
```

At `theta=theta_k`, the cofactor length is
`x^[1/(2(k+1))]`.  The total-product polynomial has length `x^(1+o(1))`,
whereas its balanced factors have length
`x^(1/2+O(1/k))`.

## 3. Derivation of the known complete bound

The fixed-order Vaughan theorem states

```text
C_(h,k)(log x)
 =B_(U,V)^(k)(x)-Z_(U,V)^(k)(x)
  +O_(h,k)([U^(k+1)log(2x)+(UV)^(k+1)]/x^(k+1/2)).   (3.1)
```

The classical Vinogradov--Korobov PNT remainder, in current optimal-shape
form, is

```text
Psi(y)-y
 <<y exp{-c(log y)^(3/5)(loglog y)^(-1/5)}.           (3.2)
```

Partial summation against the fixed logarithmic B-spline in `C_(h,k)` gives

```text
C_(h,k)(log x)
 <<x^(1/2)exp{-c_1(log x)^(3/5)(loglog x)^(-1/5)}.    (3.3)
```

At `theta_k`, the second error in (3.1) has exponent zero:

```text
2 theta_k(k+1)-k-1/2=0.                              (3.4)
```

The first error is power-decaying.  Equations (3.1)--(3.4) prove (1.1).
Bellotti's current PNT transfer gives the optimal error associated with a
given zero-free boundary; Lee--Leong give the corresponding explicit
Mertens-shaped bound.  Their exponents remain subpower:

- [Bellotti, zero density and PNT error](https://arxiv.org/abs/2508.02041)
- [Bellotti, published Vinogradov--Korobov region](https://doi.org/10.1016/j.jmaa.2024.128249)
- [Lee--Leong, explicit Mertens and reciprocal-zeta bounds](https://arxiv.org/abs/2208.06141)

For growing fixed-step order, zero-shell optimization improves the saving
in the **moving** energy to

```text
X exp{-c(log X)^(4/5)(loglog X)^(-3/5)}.              (3.5)
```

That detector changes with `X`; (3.5) is not admissible in the fixed-order
Laplace-pole converse and does not improve `eta` in (1.3).

## 4. Exact recompletion: the endpoint is a Mobius--log energy

The later conductor audit changes the interpretation of reciprocal-phase
estimates.  The complete finite chirp identity is

```text
sum_(j,theta in Z) W(j/c,theta/c)e_c(j theta inverse(z))
 =c sum_(m,nu in Z)What(m,nu)e_c(-m nu z).            (4.1)
```

It holds for every positive integer `c` and unit `z mod c`.  Recombining
all residue/conductor classes therefore cancels the proper-divisor
Ramanujan correction exactly.  There is no remaining conductor error to
estimate.

After both Vaughan variables and all three heads are restored, the
coefficient is

```text
C(n)=(mu*Lambda)(n)=-mu(n)log n,                     (4.2)
C*1=Lambda.                                          (4.3)
```

The complete ordinary dual is consequently

```text
O_full
 =sum_(q_1,q_2)C(q_1)C(q_2)
    sum_(m_1,m_2>=1)L(q_1m_1,q_2m_2)

 =int psi(R)
   abs[sum_q C(q)sum_m f_R(qm)]^2dR
 =E_R71>=0.                                           (4.4)
```

Thus the reciprocal/Kloosterman description is an exact coordinate change
of the original positive energy once completion is respected.  A frozen
ordinary-dual component is signed; positivity belongs only to the full sum
in (4.4).

For a fixed smooth dyadic weight, the scalar Mellin polynomial is

```text
B_(X,w)(tau)
 =sum_n -mu(n)log(n)n^(-1/2)w(n/X)n^(i tau).          (4.5)
```

Since its Dirichlet series is `(1/zeta)'`, Vinogradov--Korobov gives,
uniformly on fixed `tau` intervals,

```text
B_(X,w)(tau)
 <<X^(1/2)exp{-c(log X)^(3/5)(loglog X)^(-1/5)}.      (4.6)
```

Squaring and recombining yields (1.2).  A bound
`B_(X,w)<<X^(1/2-eta)` for a separating bank, or equivalently (1.4) for the
complete positive family, is already fixed-strip-strength because a zero
of real part `beta` contributes energy `X^(2beta-1)`.

The project identities used in this section are audited in
[`R120-PRIMITIVE-MOBIUS-MELLIN-KERNEL-GATE.md`](R120-PRIMITIVE-MOBIUS-MELLIN-KERNEL-GATE.md)
and
[`R128-ALL-ARITY-PROPER-CONDUCTOR-GATE.md`](R128-ALL-ARITY-PROPER-CONDUCTOR-GATE.md).
Their exact connection to the PNT error and reciprocal Mertens recurrence is
proved in
[`MOBIUS-LOG-FLOOR-RECURRENCE-OBSTRUCTION-2026-08-11.md`](MOBIUS-LOG-FLOOR-RECURRENCE-OBSTRUCTION-2026-08-11.md):
`S_C(N)-1=sum_(k<=N)mu(k)R(floor(N/k))`, and `S_C` has the
same power-growth exponent as `M`.  Thus neither refolding nor a generic
higher-tail bound for the inverse floor operator lowers the fixed-power
difficulty.
They are internal analytic claims, not externally refereed theorems.

## 5. Primary-source applicability matrix

### Montgomery--Vaughan mean value

For frequencies `log n`, the spacing term gives

```text
integral_0^T abs(sum_(n<=N)c_n n^(-it))^2dt
 <<(T+N)sum_n abs(c_n)^2.                             (5.1)
```

Here `T=O(1)` for a fixed window and `N=x^(1+o(1))` for the grouped
polynomial.  Bilinearizing replaces one length `x` by two lengths
`x^(1/2+O(1/k))`, but Cauchy multiplies the costs back to `x^(1+o(1))`.
This proves only `delta=0`.

Primary source: [Montgomery--Vaughan](https://doi.org/10.1112/jlms/s2-8.1.73).

### Guth--Maynard large values

Their theorem counts one-separated large values of a Dirichlet polynomial.
The R71 carrier needs exclusion of one completed peak in a bounded or
subpower frequency window.  The first term in their count remains positive
through the relevant threshold, and the theorem does not control the
rank-two center or exclude one exceptional value.

Primary source: [Guth--Maynard, Annals 2026](https://doi.org/10.4007/annals.2026.203.2.6).

### Shifted correlations and almost-all Type II

Matomaki--Radziwill--Tao control almost all **additive** shifts, with
arbitrary logarithmic rather than fixed-power saving.  MRSTT control
`Lambda-Lambda^sharp` against nilsequences on almost all starts for
`H>=X^(1/3+epsilon)`, again with logarithmic saving.  The rational major-arc
approximant, exceptional starts, Mobius cofactor, and complete center remain.
An exceptional set of logarithmic density still contributes
`X/log^A X` at the trivial energy scale, so it cannot yield (1.4).

Primary sources:

- [Matomaki--Radziwill--Tao, shifted correlations](https://arxiv.org/abs/1707.01315)
- [Matomaki--Radziwill--Shao--Tao--Teravainen, higher uniformity](https://arxiv.org/abs/2411.05770)

### Wright's trilinear Kloosterman fractions, current v2

Wright's Theorem 2.1 gives a real fixed-power saving for its native
**nonzero reciprocal-phase** form.  In the ideal balanced regime

```text
M=N=x^(1/2+o(1)),  R_0,A=x^o(1),                    (5.2)
```

the slowest displayed term gives the nominal gain

```text
M^(-1/20+o(1))=x^(-1/40+o(1)).                       (5.3)
```

The theorem assumes a nonzero integer phase numerator and does not include
the axes/ordinary dual.  Equation (4.1) shows that, after those missing
classes are restored, the surviving primitive component is (4.4)--(4.5),
not a nonzero Kloosterman phase.  Hence (5.3) is a valid local budget but
not an applicable bound for the completed energy.

As a schematic fixed-order check, take

```text
M=N=x^theta,
R_0=x^(1-2theta),
theta=1/2-epsilon,
A=x^o(1).                                             (5.4)
```

The slow term in current Theorem 2.1 has remaining gain

```text
theta/20-(1-2theta)/4
 =1/40-11 epsilon/20.                                 (5.5)
```

At the Vaughan endpoint `epsilon=1/[4(k+1)]`, this is

```text
(2k-9)/[80(k+1)],                                    (5.6)
```

positive for `k>=5` (only `1/480` at `k=5`).  This calculation is a
parameter calibration, not a bridge theorem: the exact complete object
still contains the ordinary dual.

Primary source, revised 2026-08-07:
[Wright, arXiv:2604.25177v2](https://arxiv.org/abs/2604.25177v2).

### Mobius in all short intervals

Matomaki--Teravainen prove `o(H)` for every interval of length
`H=x^theta`, `theta>0.55`.  This is genuine all-start cancellation but has
no fixed-power rate, uses a different interval geometry, and does not
retain the von Mangoldt factor and center.  It does not imply (1.4).

Primary source:
[Matomaki--Teravainen](https://arxiv.org/abs/1911.09076).

## 6. Precise missing theorem and research disposition

The minimal faithful theorem card is:

> There exist `delta>0` and a complete, nondegenerate fixed-order
> dilation/modulation bank such that, uniformly on every sufficiently large
> regular block, the all-profile, all-gcd, all-orientation, all-head ordinary
> dual (4.4) is `O(X^(1-delta))`.

It must include:

1. the low log-Mellin modes of (4.5);
2. all common-divisor sectors;
3. both conjugate orientations;
4. the exact Type-I/Vaughan heads; and
5. a bank with no common zero at a zeta zero.

A theorem only for a signed frozen component can win by spectral sign
cancellation and need not control the positive energy.  A theorem only for
nonzero reciprocal phases omits the ordinary dual.  A theorem averaged over
starts or shifts leaves a possible exceptional carrier.  These are logical
scope failures, not missing epsilon bookkeeping.

Focused primary-source search through 2026-08-11 found no theorem satisfying
this card.  This is not a proof of literature-wide nonexistence or priority.
It does establish the correct allocation decision: further
conductor-by-conductor Kloosterman estimates cannot close the present route,
because the exact all-conductor comparison is already equality.  Any next
analytic iteration must act on the complete low-Mellin Mobius--log energy
before Cauchy or absolute values.  The subsequent floor-transform audit cited
in Section 4 proves that the most direct reciprocal weak-tail bootstrap is
itself equivalent in power strength to this endpoint.
