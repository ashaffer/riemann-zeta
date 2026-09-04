# Hostile audit: the lower-sieve minorant proves the rough-gap square bound

**Date:** 2026-08-13  
**Status:** independent parameter audit passed; theorem-grade corollary of
published estimates.

## Verdict

For

```text
R_z={n: every prime divisor of n is at least z},
X^.1537 <= z <= X^.160,
```

the lower-sieve component of Matomaki's short-interval argument, combined
with Iwaniec's Jacobsthal bound, proves

```text
G_2(X;z):=sum_(consecutive R_z gaps meeting [X,2X]) g^2
          << X (log X)^2.                            (0.1)
```

Thus the exponent in the local finite-wheel gate is `rho=0`.  At the hostile
denominator exponent `b=799/5000`, the required strict inequality is

```text
rho < b-2 kappa_max=.120319034834... ,                (0.2)
```

so (0.1) clears it by the full `.120319...` exponent margin.

The proof does **not** import a fixed-power asymptotic for the actual rough
indicator.  That stronger two-dimensional problem remains outside the cited
variance theorems.  It uses a pointwise lower minorant; empty intervals force
a large negative deviation of that minorant, and that is all the gap argument
needs.

No zero-free strip is claimed by this report.  It closes the unsigned local
rough-gap moment gate only.

---

## 1. Imported results and their exact scope

The analytic input is Kaisa Matomaki,
[*Almost primes in almost all very short intervals*](https://doi.org/10.1112/jlms.12592),
with the [arXiv source](https://arxiv.org/abs/2012.11565) used to audit the
formulas.

Only four pieces of that proof are needed.

1. Proposition 5.1 decomposes the mean square of a sharp short-interval
   divisor-sum discrepancy into `S_1+S_2+S_3+O(H^3 log^3 X)`.
2. The general Type-II estimate in Lemma 5.4 is valid for every `2<=H<=X`.
   The later `H<=X^(1/60)` hypothesis belongs to a coarse corollary, not to
   the raw estimate.
3. Sections 6.1 and 6.3 prove the coefficient bounds used for `S_1^-` and
   `S_3^-`.
4. In the reduction of equation (61), each upper or lower linear-sieve
   weight is written as an `O(1)` linear combination of well-factorable
   convolution pieces.  The standard construction permits any factorization
   of the level, so the split below is legal; it is not necessary to assert
   that the raw Rosser--Iwaniec weight is itself a single convolution.

The deterministic maximum-gap input is Iwaniec's
[*On the problem of Jacobsthal*](https://doi.org/10.1515/dema-1978-0121):

```text
J(z) << z^2,                                          (1.1)
```

where `J(z)` is the largest gap in the set with no prime factor at most `z`.
The same statement and attribution are recorded explicitly in Section 2.3
of Banks--Ford--Tao,
[*Large prime gaps and probabilistic models*](https://doi.org/10.1007/s00222-023-01199-0).
Since `R_z` is a superset if the endpoint prime `z` is omitted, (1.1) also
bounds the pre-`q` rough gaps used here.

---

## 2. Reparameterizing the lower minorant

Set

```text
d=1/3,       e=1/1000,       L=d+e=1003/3000,
D=X^d,       E=X^e,          z=X^b, b<=4/25.
```

Use Matomaki's vector lower-sieve coefficients `alpha_r^-` with the small
beta sieve at level `E` and the medium linear sieve at level `D`.  The
pointwise inequality and support are

```text
1_((n,P(z))=1) >= sum_(r|n) alpha_r^- ,
alpha_r^-=0 for r>X^L.                               (2.1)
```

The lower linear-sieve main term is positive uniformly because

```text
d/b >= (1/3)/(4/25)=25/12>2.                         (2.2)
```

After choosing the small-prime beta-sieve parameter sufficiently deeply,
the fundamental lemma gives

```text
A_z:=sum_r alpha_r^-/r >> 1/log X.                   (2.3)
```

### Dependency audit

Changing the paper's displayed `D=X^(5/9), z=D^(1/4)` to (2.2) does not
change any pointwise sieve identity.

* The lower main term uses only `d/b>2`.
* The `S_1^-` proof loses fixed powers of `log z/log w`; these are constants
  when all cutoffs are fixed powers of `X`.
* The `S_3^-` proof reduces to the same small beta-sieve divisor moment and
  is independent of the numerical choice `d=5/9`.
* The new total coefficient support `X^L` is smaller, not larger, than the
  support in the published application.

Consequently the published arguments give, for physical interval length
`H`,

```text
S_1^-+S_3^- << XH/log X.                             (2.4)
```

---

## 3. Exact Type-II frontier

Factor the level-`D` linear weight with exponents

```text
2L/3=1003/4500,
d-2L/3=994/9000,
```

and group the beta-sieve factor `E=X^(9/9000)` with the second factor.  The
two complete factors and the unfactored second copy of `alpha^-` therefore
have dyadic exponents

```text
m=2L/3=1003/4500,
n=L/3 =1003/9000,
q<=L  =1003/3000.                                   (3.1)
```

This is exactly the one-sided factorization used in the paper's reduction:
only one copy of `alpha^-` is split; the other is the bounded `Q` sequence.

For `H=X^h`, Matomaki's raw Type-II estimate is

```text
H^(1/2) X^(1/2+o(1))
[(MQ)^2
 +(HMNQ/X+N)
   {MQ(HMNQ/X+N)(Q+N^2)+H(MN)^3Q/X}]^(1/4).          (3.2)
```

If

```text
h < h_*:=1-5L/3=797/1800=.442777... ,                (3.3)
```

then `HMNQ/X<=N`, `Q+N^2<=X^L`, and both outer branches in
(3.2) have exponent

```text
C(h)=1/2+h/2+5L/6 <1.                                (3.4)
```

Choosing `h=2/5` leaves exact saving

```text
1-C(2/5)=77/3600=.021388... .                        (3.5)
```

After restoring the one factor `H` from `(H-|k|)` in `S_2`, the power
saving absorbs all logarithmic subdivisions:

```text
S_2^- << XH/log X,       H<=X^(2/5).                 (3.6)
```

The `O(H^3 log^3 X)` term in Proposition 5.1 is also bounded by the right
side of (3.6) throughout this range.  Equations (2.4) and (3.6) prove

```text
integral |E_z(x;H)|^2 dx << XH/log X,                (3.7)
2 log X <= H <= X^(2/5),
```

where

```text
E_z(x;H)=sum_r alpha_r^-
          (#{x-H<rm<=x}-H/r).
```

As a second independent exact check, at the actual Jacobsthal endpoint
`b=799/5000`, `h=2b=799/2500`, the max-plus nodes in (3.2) give

```text
C(h)=84457/90000=.938411...<1.                       (3.8)
```

---

## 4. Empty starts imply the gap square

If `(x-H,x]` contains no `z`-rough integer, the lower minorant (2.1) is at
most zero, whereas its mean is `HA_z>>H/log X`.  Chebyshev and (3.7) give

```text
B_z(H):=meas{x:(x-H,x] contains no z-rough integer}
       << X log X/H.                                 (4.1)
```

For consecutive rough gaps `g` in a fixed enlarged shell, define

```text
T_z(H)=sum_g (g-H)_+.
```

Up to endpoint conventions of measure zero, `T_z(H)` is exactly `B_z(H)`.
The layer-cake identity

```text
sum_g g^2=2 integral_0^infinity T_z(H) dH             (4.2)
```

is termwise exact.  Iwaniec gives

```text
max g << z^2 <=X^(8/25)<X^(2/5),                    (4.3)
```

so (4.1) covers every nontrivial layer.  The trivial estimate below
`2 log X`, (4.1) above it, and (4.3) yield

```text
G_2(X;z)
 << X log X
    +X log X integral_(2 log X)^(O(z^2)) dH/H
 << X(log X)^2.                                      (4.4)
```

A fixed multiplicative enlargement handles the two shell-boundary gaps;
`J(z)=o(X)` ensures that no growing number of shells is introduced.

---

## 5. Scoped conclusions

```text
lower vector minorant after D,z reparameterization:  AUDITED / VALID
arbitrary well-factorable 1:2 split:                 AUDITED / VALID
raw Type-II use beyond printed coarse H range:       AUDITED / VALID
S_1^-, S_3^- transfer:                               AUDITED / VALID
Jacobsthal coverage of every rough gap:              AUDITED / VALID
G_2(X;z)<<X log^2 X:                                 PROVED
actual rough-indicator variance asymptotic:           NOT CLAIMED
signed aggregation over all sieve stages:             NOT CLAIMED
zero-free strip from this lemma alone:                NOT CLAIMED
```

The fixed-power variance barrier in the existing rough-number literature is
therefore not a no-go theorem for this gate.  It concerns a sharper
asymptotic for the actual indicator.  The one-sided minorant has enough
structure for the empty-interval consequence.

## 6. Reproduction

```bash
PYTHONPATH=src python3 -m unittest -v \
  src/test_rough_gap_lower_sieve_frontier.py
python3 results/verify_zeta23_rough_gap_lower_sieve_frontier.py
python3 results/verify_zeta23_matomaki_rough_gap_gate.py
```

The first checker expands every max-plus node in (3.2) with exact
`Fraction` arithmetic.  The second independently checks the comfortable
`h=2/5` certificate.  Neither checker re-proves the imported analytic
theorems.
