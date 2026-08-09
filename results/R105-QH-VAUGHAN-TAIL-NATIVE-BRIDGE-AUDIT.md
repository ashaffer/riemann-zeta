# R105 center-free Vaughan-tail native-bridge audit

Status: an exact finite Vaughan-tail-to-R81/Wright bridge is proved after
recombining the two large factors into their cofactor product.  Its
square-root semiprime block has full exponent-size coefficient norm, and the
top shift-product range makes Wright's recorded bound worse than the direct
absolute estimate.  Unfolding the product gives an exact fixed-modulus
Kloosterman-sum formula, but its two coefficient supports are a full Fourier
transform and a modular-inverse image rather than the two short intervals
required by Blomer--Pascadi.  Thus neither imported theorem gives a fixed
power for the complete tail through the presently available interfaces.
No fixed zero-free strip is proved.

Date: 2026-08-07.

R102--R104 predecessors:
[`R102-CENTER-ANNIHILATED-OFF-AXIS-GATE.md`](R102-CENTER-ANNIHILATED-OFF-AXIS-GATE.md)
and
[`R104-QH-FINITE-COFACTOR-SECTOR-THEOREM.md`](R104-QH-FINITE-COFACTOR-SECTOR-THEOREM.md).

## 1. Verdict

Put

```text
f_R(t)=t^(-1/2)V_Q(R-log t),
integral f_R(t)dt=0,                                  (1.1)
```

and let the active physical support be `t asymp X`.  For the retreated
Vaughan cutoffs `U,V=X^(1/2-o(1))`, define

```text
a_(U,V)(q)
 =sum_(db=q, d>U, b>V)mu(d)Lambda(b).                 (1.2)
```

Then the exact transformed tail is

```text
T_Q(R)=sum_q a_(U,V)(q)sum_(m>=1)f_R(qm).             (1.3)
```

The zero marginal in (1.1) makes (1.3) a finite nonzero-alias expansion.
Consequently the complete R81 solution-line identity and the mask-free R84
`k=j theta` grouping apply **verbatim**, with

```text
h(q)=a_(U,V)(q)/q                                     (1.4)
```

in place of `c(q)/q`.  This supplies the exact bridge which R104 Section 8
left open.

It does not put the two Vaughan factors into Wright's two denominator
variables.  Since `db=q` and `d,b>X^(1/2-o(1))`, the new coefficient is
supported on

```text
X^(1-o(1))<q<<X.                                      (1.5)
```

The top `q asymp X`, `g=1` block is substantial: products of two distinct
primes in fixed square-root intervals give

```text
sum_(q asymp X)abs[a_(U,V)(q)/q]^2=X^(-1+o(1)).       (1.6)
```

Thus the cofactor product has the same exponent-size `l2` norm as the
canonical cofactor sequence.  On the full high-mode box

```text
M=N asymp X,       J=Theta asymp X,
K_0=abs(j theta)asymp X^2,                            (1.7)
```

the recorded R84 projective ledger followed by Wright's Theorem 2.1 gives
only

```text
X^(15/8+o(1)),                                       (1.8)
```

whereas direct absolute estimation of (1.3) is `X^(1+o(1))` at the energy
level.  The imported estimate is therefore not merely short of a fixed
power on this box; it is weaker than the pre-completion bound.

There is also an exact optimistic Blomer--Pascadi conversion.  Fix the
first product modulus `c asymp X` and unfold the second product `q=db` with
`d,b asymp sqrt(c)`.  Completing `d` gives

```text
sum_(d,b)alpha_d beta_b e_c(k inverse(db))
 =c^(-1)sum_(h,n)alphahat(h) betatilde(n)S(kh,n;c),   (1.9)
```

where

```text
betatilde(n)=beta_(inverse(n))1_(inverse(n) in I_b).  (1.10)
```

Formula (1.9) is a literal fixed-modulus bilinear Kloosterman-sum form.
However, `alphahat` lives on the full Fourier residue system and
`betatilde` lives on the modular inverse of a square-root interval.  Neither
is supported on one additive interval of length `sqrt(c)`.  Splitting into
such intervals and applying the scalar theorem blockwise costs more than
the available `c^(-1/32)` gain unless the product of the two effective block
counts is `c^(<1/16)`.  No such concentration theorem is available for the
rough `mu` and `Lambda` factors, and it is not supplied by (1.1).

The resulting ledger is

```text
finite Vaughan tail                         EXACT
tail cofactor-product Poisson expansion      EXACT / ABSOLUTE
tail R81 solution-line identity              EXACT
tail R84 scalar Wright interface             EXACT
top semiprime coefficient norm               NATURAL SIZE
high-k Wright all-box bound                  FAILS SCALE TEST
factor-unfolded fixed-c Kloosterman form      EXACT
two BP short-interval supports                ABSENT
complete tail fixed power                     OPEN
fixed zeta zero-free strip                    NOT PROVED.             (1.11)
```

## 2. Exact finite alias theorem for the Vaughan tail

The support of `f_R` and `m>=1` imply `q<<X` in (1.3), while `d>U,b>V`
imply `q>UV`.  Hence every sum in this section is finite.  For each `q`,
Poisson summation and (1.1) give

```text
sum_(m>=1)f_R(qm)
 =q^(-1)sum_(a in Z-{0})fhat_R(a/q).                  (2.1)
```

The usual spline smoothing, or the seminorm estimate R104 (2.6) with
order greater than one, makes the alias sum absolute.  Therefore

```text
T_Q(R)
 =sum_(UV<q<<X)h(q)sum_(a!=0)fhat_R(a/q),
h(q)=a_(U,V)(q)/q.                                    (2.2)
```

Let

```text
L_Q(t,u)=integral psi(R)f_R(t)conjugate[f_R(u)]dR.    (2.3)
```

Squaring (2.2) and using Fubini gives the exact finite quadratic form

```text
E_T
 =sum_(q_1,q_2)h(q_1)conjugate[h(q_2)]
    sum_(a,b!=0)Lhat_Q(-a/q_1,b/q_2).                 (2.4)
```

There is no conditional cofactor tail, primitive mask, or zero-frequency
term in (2.2)--(2.4).

### Theorem 2.1 (exact tail-to-Wright bridge)

Write

```text
q_1=gr,       q_2=gs,       (r,s)=1,
theta=a s-b r.                                         (2.5)
```

On every finite signed dyadic box with `j theta!=0`, the R81
solution-line Poisson identity followed by the R84 Mellin separation and
the grouping `k=j theta` rewrites (2.4) as a finite sum of forms

```text
integral_t sum_((r,s)=1,k)
 [h(gr)r^(-it)] [conjugate(h(gs))s^(-it)]
 nu_(g,t)(k)e(k inverse(s)/r)dt.                      (2.6)
```

For fixed `(g,t)` and a fixed sign of `k`, (2.6) is Wright's scalar
trilinear Kloosterman-fraction form.

#### Proof

The proof of R81 (6.2)--(6.4) uses only the coefficient product attached to
`q_1,q_2`; it does not use the formula `c(q)=-mu(q)log q`.  The solutions of
`a s-b r=theta` form one affine line, and Poisson summation along that line
gives the phase `e(j theta inverse(s)/r)`.  R84 Proposition 4.1 likewise
uses the two arbitrary one-variable sequences `h(gr)` and `h(gs)`.  Its
Mellin inversion separates the ratio amplitude, and grouping all
factorizations of `k=j theta` costs only the stated divisor factor.  Since
(2.2) is finite, all rearrangements here are unconditional.  Substitution
of (1.4) proves (2.6).  QED.

This theorem corrects a narrow gap in R104: an exact bridge exists, but it
exists in the product variable `q=db`.  It does not identify `d` and `b`
with Wright's denominator variables.

## 3. The top product coefficient has natural size

The elementary upper bound

```text
abs[a_(U,V)(q)]<=tau(q)log q                          (3.1)
```

and the standard fixed-moment divisor bound give, on any fixed-ratio top
interval,

```text
sum_(q asymp X)abs[a_(U,V)(q)]^2<=X^(1+o(1)),
sum_(q asymp X)abs[h(q)]^2<=X^(-1+o(1)).              (3.2)
```

The exponent in (3.2) is sharp.  Choose a fixed interval
`P_X=[lambda sqrt(X),mu sqrt(X)]` whose pairwise products lie inside the
active top `q` block.  On every canonical retreated schedule, the constants
may be chosen so that every `p in P_X` is larger than `U` and `V` for all
large `X`.  If `p!=r` are primes in `P_X`, then for `q=pr` the only
admissible factorizations in (1.2) are

```text
(d,b)=(p,r),(r,p),
a_(U,V)(pr)=-log p-log r=-log(pr).                    (3.3)
```

The prime number theorem supplies `X^(1+o(1))` distinct such semiprimes
(more precisely, order `X/log^2 X`).  Hence

```text
sum_(q=pr; p,r in P_X,p<r)abs[h(q)]^2
 asymp [X/log^2 X]*(log^2 X/X^2)
 =X^(-1+o(1)).                                       (3.4)
```

Almost every ordered pair of these semiprimes is coprime: pairs sharing a
prime have one fewer free square-root prime and are lower by
`X^(-1/2+o(1))`.  Thus the `g=1` sector in (2.6) retains the natural norm;
it is not an artifact of a large common divisor.

## 4. Exact Wright exponent ledger on the forced top box

Take the `g=1` top block in (2.6):

```text
r,s asymp X,       M=N asymp X.                       (4.1)
```

By (3.2)--(3.4), the product of the two denominator-sequence `l2` norms is

```text
norm(alpha)_2 norm(beta)_2=X^(-1+o(1)).               (4.2)
```

For `K_0=abs(k)` and `Theta<=X`, the favorable form of the R84 kernel
ledger is

```text
integral norm(nu_t)_2dt
 <=X^o(1)K_0^(1/2)(1+Theta/X)^(1/2).                  (4.3)
```

Thus, throughout `Theta<=X`, Wright's displayed theorem gives

```text
B_(K_0)
 <<X^o(1) K_0
   [X^(-1/8)+X^(-1/20)K_0^(-1/20)
     +X^(-1/20)K_0^(-3/20)].                         (4.4)
```

The omitted displayed branches are no larger in this balanced range.  If
`K_0=X^kappa`, the exponent in (4.4) is

```text
19kappa/20-1/20,          0<=kappa<=3/2,
kappa-1/8,                3/2<=kappa<=2.              (4.5)
```

In particular, at `J asymp Theta asymp X`, so that `K_0 asymp X^2`,

```text
B_(X^2)<<X^(15/8+o(1)).                               (4.6)
```

By contrast, (1.3), (3.1), `q>X^(1-o(1))`, and
`m<<X/q=X^o(1)` give pointwise

```text
abs[T_Q(R)]<=X^(1/2+o(1)),
integral psi(R)abs[T_Q(R)]^2dR<=X^(1+o(1)).           (4.7)
```

Thus (4.6) loses `X^(7/8-o(1))` against the elementary energy estimate.
It cannot be summed into a fixed-power result.

The high box cannot be deleted by window smoothness.  With fixed-ratio
coordinates one has

```text
L_Q(Xx,Xy)=X^(-1)mathcal L_Q(x,y),                    (4.8)
```

where `mathcal L_Q` is a fixed compact profile.  The R81 amplitude on
`r,s asymp X`, `j=X sigma`, `theta=X tau` is therefore

```text
integral mathcal L_Q(y+sigma,y)
  e[tau y/((r/X)(s/X))]dy,                            (4.9)
```

with no negative power of `X`.  Since the diagonal profile is nonzero,
continuity gives fixed nonzero `sigma,tau` boxes on which (4.9) has natural
size.  Marginal nullity says that an integral over the **whole** shift
profile vanishes; it does not make each fixed-ratio high-shift box small.

## 5. Exact factor-unfolded Blomer--Pascadi formula

There is one optimistic way to recover square-root variables.  Fix a
modulus `c asymp X` from the first top cofactor product and unfold the second
one as `q=db`, with `d,b asymp sqrt(c)`.  A typical reciprocal slice is

```text
F_c(k)
 =sum_(d in I_d,b in I_b;(db,c)=1)
    alpha_d beta_b e_c(k inverse(db)),                (5.1)
```

where smooth product weights can first be separated by Mellin inversion.
The arithmetic parts of `alpha,beta` are `mu` and `Lambda`.

Extend `alpha` by zero to `Z/cZ` and put

```text
alphahat(h)=sum_(d mod c)alpha_d e_c(-hd).             (5.2)
```

Fourier inversion followed by completion over the units gives

```text
F_c(k)
 =c^(-1)sum_(h mod c,b in I_b)
   alphahat(h)beta_b S(h,k inverse(b);c).              (5.3)
```

If `(k,c)=1`, the elementary scaling identity for Kloosterman sums gives

```text
S(h,k inverse(b);c)=S(kh,inverse(b);c).                (5.4)
```

After `n=inverse(b) mod c`, define

```text
betatilde(n)=beta_(inverse(n))
              1_(inverse(n) in I_b).                  (5.5)
```

Then

```text
F_c(k)
 =c^(-1)sum_(h,n mod c)
   alphahat(h)betatilde(n)S(kh,n;c).                  (5.6)
```

This is exactly the Blomer--Pascadi bilinear Kloosterman form, not merely a
phase analogy.

The range mismatch is equally exact.  Their critical gain applies when
both coefficient variables are supported on additive intervals of length

```text
N=sqrt(c).                                            (5.7)
```

But (5.2) is the full discrete Fourier transform of a rough interval
sequence, and (5.5) is supported on the modular inverse image of an
interval, not on that interval.

Partition the two residue systems into intervals of length `sqrt(c)`.  If
`L_h,L_n` denote the numbers of blocks retained in an attempted scalar
application, Parseval gives

```text
norm(alphahat)_2=sqrt(c)norm(alpha)_2.                 (5.8)
```

Theorem 1.1 at (5.7), followed by Cauchy over the scalar blocks, yields

```text
abs[F_c(k)]
 <<c^(15/32+o(1))(L_h L_n)^(1/2)
   norm(alpha)_2 norm(beta)_2.                        (5.9)
```

The direct coefficient-uniform bound for (5.1) is

```text
abs[F_c(k)]
 <=c^(1/2+o(1))norm(alpha)_2 norm(beta)_2.            (5.10)
```

Consequently the blockwise imported argument is nontrivial only if

```text
L_h L_n<c^(1/16-o(1)).                                (5.11)
```

Neither scalar theorem gives (5.11).  Fourier transformation of the rough
`mu` factor has no short-interval support theorem, while inversion sends a
square-root interval through the whole residue system.  Proving a suitable
joint square-function estimate across these blocks would be a new theorem,
not an application of Blomer--Pascadi.  Applying their theorem with the
single covering interval `N=c` is also impossible: it is outside their
nontrivial range `c^(13/28+epsilon)<N<c^(7/12-epsilon)`.

## 6. The direct inverse-product literature isolates a composite resonance

There is a more direct imported theorem than (5.6), but its modulus
hypothesis fails in exactly one place.  Mohammadi's Theorem 1 in
[*Bilinear Kloosterman Sums over Small Boxes*](https://arxiv.org/abs/2608.01203)
states, for a finite field of size `Q=p^n`,

```text
sum_(x in B_1,y in B_2)alpha(x)beta(y)
 psi(a xy+b inverse(xy))
 <<p^(-delta)abs(B_1)abs(B_2),                        (6.1)
```

uniformly for bounded weights, `b!=0`, and
`abs(B_1)abs(B_2)>=Q^(1/2+epsilon)`.  The parameter `a` may be zero.  Thus,
for a **prime** fixed modulus `c`, (6.1) would apply directly to (5.1),
without the Fourier and inverse-support losses of Section 5.

The tail modulus cannot be prime:

```text
c=q_1=d_1b_1,             d_1>U, b_1>V.              (6.2)
```

Both factors are nontrivial and have square-root size.  A finite field of
cardinality `c` therefore does not represent the additive character and
inversion modulo `c`.  Passing to a prime divisor by the Chinese remainder
theorem leaves the other prime-divisor phase coupled through the same
product `xy`; it cannot be absorbed into two one-variable weights.

Bourgain--Garaev's Theorem 3 in
[*Kloosterman sums in residue rings*](https://arxiv.org/abs/1309.1124)
covers arbitrary composite `c`, bounded weights, the exact phase in (5.1),
and initial intervals `[1,N_1]`, `[1,N_2]`.  Even granting a
dyadic-translation extension most favorable to the present application,
its displayed moment bound is resonant at

```text
abs(I_d)=abs(I_b)=sqrt(c).                             (6.3)
```

Indeed every choice of its moment parameters leaves one of the factors

```text
N^(k-1)/sqrt(c)+sqrt(c)/N^k                           (6.4)
```

of order at least one when `N=sqrt(c)`.  Their Corollary 1 explicitly
excludes neighborhoods of `c^(1/(2l))`; (6.3) is the first excluded point
`l=1`.  Hence the general-modulus predecessor gives no power on the exact
Vaughan scale, while the 2026 finite-field theorem does not cover the
forced modulus.

There is also an unavoidable conductor qualification.  A
coefficient-uniform composite-modulus estimate is false for arbitrary
nonzero `k`.  If `c` is even and `k=c/2`, then for every unit `x y mod c`,

```text
e_c(k inverse(xy))=-1.                                (6.5)
```

Thus (5.1) has no oscillation at all.  More generally the useful conductor
is `c/(k,c)`, not `c`.  The R81 product `k=j theta` runs through all these
conductors.  Integer `k=0` was removed in R104, but the modular low-conductor
classes in (6.5) were not.

This identifies a sharper possible new input:

```text
a Mohammadi-strength critical inverse-product theorem over the
Vaughan-generated composite moduli, with an explicit conductor factor,
plus an l2 summation of the low-conductor folded k classes.              (6.6)
```

Neither cited theorem supplies (6.6).  A scalar uniform-in-`k` bound cannot
do so because of (6.5).

## 7. Why another choice of modulus does not repair the scale

The possible native modulus choices have a short exhaustive scale ledger.

1. **Product modulus `c=q asymp X`.**  The two Vaughan factors have the
   critical length `sqrt(c)`, but the exact conversion is (5.6), with the
   full-Fourier and inverse-image supports just described.

2. **One-factor modulus `c=d` or `c=b`, of size `sqrt(X)`.**  The other
   large Vaughan variables have length `sqrt(X)asymp c`, not `sqrt(c)`.
   This lies outside the Blomer--Pascadi nontrivial interval.  Subdivision
   into critical blocks introduces a positive power cost much larger than
   `c^(-1/32)`.

3. **Small retained-cofactor modulus `c=m`.**  Here `m=X^o(1)` on the
   retreated schedule.  Even a hypothetical `c^(-delta)` gain is only
   `X^(-o(1))` and cannot produce a fixed zero-free strip.

The substantive `g=1` semiprime family of Section 3 prevents a large common
divisor from moving the entire tail into a fourth, favorable regime.

## 8. Disposition

The exact tail bridge is useful because it removes one uncertainty from
R104: no new algebra is needed to put the finite transformed tail into the
R81/R84 reciprocal coordinates.  The failure is now quantitative and
localized:

```text
q=db recombined:     Wright variables have length X and high k reaches X^2;
q=db unfolded:       BP variables have the right cardinality but the wrong
                     additive supports.                              (8.1)
```

A successful continuation must therefore add at least one genuinely new
ingredient:

* a coefficient-specific all-`k` Wright estimate which beats (4.4) on
  `K_0 asymp X^2`;
* a vector/square-function Blomer--Pascadi theorem that sums the Fourier and
  inverse-image blocks in (5.6) without the factor in (5.9); or
* a signed recombination of the high boxes before either scalar theorem is
  applied.

The center-free transformation makes all three logically sufficient: the
old one-axis contact no longer has to be reconstructed.  It does not prove
any of them.  Therefore this audit establishes neither a fixed zero-free
strip nor the nonexistence of one.
