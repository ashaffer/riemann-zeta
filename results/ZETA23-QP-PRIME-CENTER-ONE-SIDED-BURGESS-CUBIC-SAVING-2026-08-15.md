# QP prime-center one-sided cubic theorem: Burgess saving and a density-one upgrade

**Date:** 2026-08-15  
**Verdict:** a fixed-power improvement over the `49/66` signed-cubic
barrier is proved for a restricted but actual arithmetic sector.

Let

```text
q be an odd prime,        Y=q/2,
B=Y^A,                    3/2<A<2,
H_Y=[Y^a,B],              0<a<A,
R=Y^2/B=Y^(2-A),
S_Y^+={n=p^j:Y<n<exp(w)Y},       0<w<log 2.         (0.1)
```

Only a fixed upper subband of `H_Y` is used for the smooth moment measure,
so the value of the fixed lower exponent `a` does not affect the estimates.

For arbitrary real weights on the actual prime powers in `S_Y^+`, the
mixed signed-cubic near-determinant tensor has norm

```text
<<_(w,epsilon)
 (R/q^(1/2)+R^(1/4)q^(3/32+epsilon))
 (log q)^(3/2).                                     (0.2)
```

At the active aperture `A=50/33`, (0.2) gives standardized-skew exponent

```text
4/33+3/32=227/1056                                  (0.3)
```

and, after the generic `q^(1/2+o(1))` leverage factor, transverse exponent

```text
1/2+227/1056=755/1056.                              (0.4)
```

This improves `49/66=784/1056` by

```text
29/1056.                                            (0.5)
```

The theorem is uniform over **all odd prime centers** `q`, but not over
composite centers.

There is a separate stronger corollary for a density-one set of prime
centers.  The multiplicative large sieve gives, outside
`O(Q^(1-c epsilon+o(1)))` exceptional primes `q in [Q,2Q]`,

```text
skew exponent       (2-A)/4+1/16,
transverse exponent 1/2+(2-A)/4+1/16.               (0.6)
```

At `A=50/33`, the latter is

```text
361/528.                                            (0.7)
```

These are proved one-sided/strongly-imbalanced coefficient-sector results.
They do **not** prove QP for every center, a full-shell uniform return, or a
strip theorem.

---

## 1. The hard near-determinant tensor

For subsets `A0,B0,C0` of `S_Y^+`, put

```text
E_R(A0,B0,C0)
 =#{(a,b,c) in A0 x B0 x C0:|2ab-qc|<=R}.          (1.1)
```

For coefficient vectors `x,y,z`, define

```text
T_R(x,y,z)
 =sum_(a,b,c in S_Y^+) x_a y_b z_c
   1_(|2ab-qc|<=R).                                 (1.2)
```

The raw pair-to-node Schur bound is

```text
|T_R(x,y,z)|<<_w R^(1/2)||x||_2||y||_2||z||_2.    (1.3)
```

The point of the theorem is to use the rank-one/set structure before
passing to Schur's test.

---

## 2. Character expansion and the exact restricted weak-type bound

Let `mathcal R` be the nonzero residues modulo `q` represented by integers
`r` with `|r|<=R`, and define

```text
S_q(R)=max_(chi nonprincipal mod q)
       |sum_(r in mathcal R)chi(r)|.                (2.1)
```

All nodes in `S_Y^+` lie strictly between `0` and `q`, because
`w<log 2`; hence they are nonzero residues.  Dropping the quotient
condition `c in C0` and applying multiplicative-character orthogonality
gives

```text
E_R(A0,B0,C0)
 <= (|mathcal R|/(q-1))|A0||B0|
    +S_q(R)sqrt(|A0||B0|).                          (2.2)
```

Indeed, the nonprincipal part is bounded by Cauchy--Schwarz and

```text
sum_chi |sum_(a in A0)chi(a)|^2=(q-1)|A0|.         (2.3)
```

Two elementary bounds retain information lost by dropping `c`.

First, after interchanging `A0,B0` if needed, assume
`|A0|<=|B0|`.  For fixed `(a,c)`, the interval for the integer `b` has
length `O(R/q)=o(1)`, so

```text
E_R(A0,B0,C0)<<_w |A0||C0|.                        (2.4)
```

Second, for fixed `c`, the integer `2ab` lies at one of `O(R)` values
`qc+r`.  A fixed integer has `O_w(1)` ordered representations as a product
of two shell prime powers: two distinct prime bases determine the factors
up to order, and a single base permits only `O_w(1)` exponent splits.
Therefore

```text
E_R(A0,B0,C0)<<_w R|C0|.                           (2.5)
```

Write

```text
P=(R/q)|A0||B0|,       N=S_q(R)sqrt(|A0||B0|),
F=R|C0|,               D=|A0||C0|.                 (2.6)
```

Equations (2.2), (2.4), and (2.5), together with

```text
min(P+N,F,D)<=min(P,F)+min(N,D),                   (2.7)
```

give, after division by
`sqrt(|A0||B0||C0|)`,

```text
min(P,F)/sqrt(|A0||B0||C0|) <= R/sqrt(q),          (2.8)

min(N,D)/sqrt(|A0||B0||C0|)
 <=min(S_q(R)/sqrt(|C0|),sqrt(|C0|))
 <=sqrt(S_q(R)).                                    (2.9)
```

Thus

```text
E_R(A0,B0,C0)
 <<_w {R/sqrt(q)+sqrt(S_q(R))}
       sqrt(|A0||B0||C0|).                         (2.10)
```

Equation (2.8) is the key principal-character check.  Omitting the
fixed-`c` fibre bound (2.5) would leave a false apparent obstruction of
size `sqrt(R)`.

---

## 3. From sets to arbitrary coefficients

The following standard restricted-weak-to-strong step is included to keep
the coefficient quantifier exact.

Order the coordinates of each vector by decreasing magnitude and split
them into rank blocks of sizes `1,2,4,...`.  On one triple of blocks,
absolute values and (2.10) give the product of the three block suprema,
the square roots of the block sizes, and the constant in braces.  For a
vector `x`, Cauchy--Schwarz gives

```text
sum_blocks sqrt(|block|) sup_block |x_i|
 <<sqrt(log(2M))||x||_2,                            (3.1)
```

where `M=|S_Y^+|`.  Summing the block triples proves

```text
|T_R(x,y,z)|
 <<_w {R/sqrt(q)+sqrt(S_q(R))}
       (log(2M))^(3/2)||x||_2||y||_2||z||_2.       (3.2)
```

This argument takes absolute values only after exploiting the arithmetic
incidence estimate.  It is valid for arbitrary real or complex
coefficients and, in particular, for the same signed vector in all three
slots.

---

## 4. Burgess gives an all-prime-center power saving

Burgess's interval-character estimate with parameter `r=2` states, for a
nonprincipal character modulo a prime,

```text
|sum_(n in I)chi(n)|
 <<_epsilon |I|^(1/2)q^(3/16+epsilon).             (4.1)
```

The symmetric residual set is a union of at most two intervals, so

```text
S_q(R)<<_epsilon R^(1/2)q^(3/16+epsilon).          (4.2)
```

Inserting (4.2) into (3.2) proves (0.2).  If
`R=q^h`, `h=2-A<1/2`, the principal term `R/sqrt(q)` is a negative power,
and the nonprincipal exponent is

```text
h/4+3/32.                                          (4.3)
```

For `h=16/33`, (4.3) is (0.3), proving the exponent ledger
(0.4)--(0.5).

---

## 5. Passage to the signed cubic moment

Let

```text
P_y(t)=sum_(n in S_Y^+) y_n exp(it log(n/Y))        (5.1)
```

and use the smooth probability at bandwidth `B`.  The mixed term
`P_y^2 conjugate(P_y)` has Fourier kernel concentrated where

```text
B |log(ab/(Yc))|<<1,
```

which is equivalent, on the fixed shell, to

```text
|2ab-qc|<<Y^2/B=R.                                 (5.2)
```

A dyadic decomposition of the Schwartz tail in (5.2), followed by (3.2)
at each residual scale `R_j=2^jR<=q/4`, preserves (0.2).  This cutoff is
important: below it the residual integer has a unique representative in the
chosen short interval modulo `q`, which is the regime used in Section 2.
For `R_j>q/4`, use the raw polynomial Schur bound (or simply
`||y||_1^3<=M^(3/2)||y||_2^3`) and the factor `2^(-jL)` from Schwartz
decay.  Since `q/R=q^(1-h+o(1))`, choosing the fixed decay order `L` large
enough makes the whole post-cutoff tail smaller than every displayed fixed
power.

The unmixed term `P_y^3` is negligible on the upper one-sided shell.  Every
integer node satisfies `n>=Y+1/2`, and hence

```text
log(abc/Y^3)>>1/Y,
B log(abc/Y^3)>>B/Y=Y^(A-1).                       (5.3)
```

Schwartz decay and `||y||_1<=sqrt(M)||y||_2` make its total contribution
smaller than every prescribed fixed power after choosing the decay order.
The conjugate terms are identical.  Expanding

```text
(Re P_y)^3=(P_y+conjugate(P_y))^3/8                (5.4)
```

therefore transfers (0.2) to the signed third moment.  Mean-centering
contributes only the already controlled smooth mean terms.

This is where the theorem differs from the false absolute-`L3` shortcut:
the signed Fourier expansion retains character cancellation.

---

## 6. Cubic endpoint and the restricted transverse/radial theorem

Here is the geometric bridge suppressed by an exponent ledger alone.  Let
`rho_B` be the smooth probability used above, supported in a fixed upper
subband of the legal height interval, and put

```text
m_y=int F_y rho_B,       Z_y=F_y-m_y,
V_y=int Z_y^2 rho_B.                                  (6.1)
```

Distinct integers in the fixed shell have logarithmic gap `>>_w1/Y`.
On the one-sided shell every frequency also has distance `>>1/Y` from zero.
Consequently the difference- and sum-frequency off-diagonal row sums in the
smooth cosine Gram matrix are `o(1)`: for every fixed `L`, they are bounded
by a constant times

```text
sum_(k>=1)(1+c_wBk/Y)^(-L)=O_(w,L)(Y/B).             (6.2)
```

The same Schwartz estimate and Cauchy--Schwarz give

```text
V_y asyp_w ||y||_2^2,
|m_y|<<_(w,L)sqrt(M)(Y/B)^L||y||_2.                  (6.3)
```

Thus centering changes the cubic by only a negligible fixed power.  If

```text
gamma_y=(int Z_y^3 rho_B)/V_y^(3/2),
kappa=h/4+3/32,                 h=2-A,               (6.4)
```

Sections 3--5 give `gamma_y>=-q^(kappa+o(1))`.  For any mean-zero real
random variable `Z`, variance `V`, and upper endpoint `H=ess sup Z`, the
pointwise inequality `(H-Z)(Z+V/H)^2>=0` gives

```text
H/sqrt(V)>=(gamma+sqrt(gamma^2+4))/2.                (6.5)
```

In particular, `gamma>=-K` implies `H>=sqrt(V)/(K+1)`.  Equations
(6.3)--(6.5), with the negligible mean restored, prove the genuine
one-sided support estimate

```text
h_Y^+(y):=sup_(t in H_Y)y dot a^+(t)
          >=q^(-kappa-o(1))||y||_2.                 (6.6)
```

For the restricted transverse vector

```text
v=a^+(t_0)+D(1,...,1),       0<=t_0<=B, 0<D<=1,
```

point evaluation gives

```text
[-y dot v]_+<=2sqrt(M)||y||_2,
M=|S_Y^+|<=q^(1+o(1)).                              (6.7)
```

Homogeneity in (6.6), followed by compact support-function separation,
therefore places `-s v` in `conv{a^+(t):t in H_Y}` for

```text
s_v^+>=q^(-1/2-kappa-o(1)).                         (6.8)
```

The radial dual normalization `F_y(0)=-1` likewise implies
`||y||_2>=M^(-1/2)`, so the same argument proves

```text
r_+(H_Y;S_Y^+)>=q^(-1/2-kappa-o(1)).                (6.9)
```

At `A=50/33`, `kappa=227/1056`, and (6.8)--(6.9) have exponent
`755/1056`.  These are restricted one-sided convex-body statements, not
claims about the full balanced shell.

---

## 7. Density-one prime-center upgrade

This subsection is a separate corollary, not part of the all-prime Burgess
claim.

Fix `h<1/2`, put `X=Q^h`, and for a nonprincipal character modulo a prime
`q in [Q,2Q]` write

```text
D_X(chi)=sum_(1<=r<=X)chi(r).                       (7.1)
```

Since

```text
D_X(chi)^4=sum_(n<=X^4)d_(4,X)(n)chi(n),            (7.2)
```

the multiplicative large sieve and the classical divisor-square bound give

```text
sum_(Q<=q<=2Q) sum_(chi primitive mod q)
 |D_X(chi)|^8
 <<(Q^2+X^4)sum_(n<=X^4)d_4(n)^2
 <<Q^(2+o(1))X^4.                                  (7.3)
```

Here `X^4<Q^2` is exactly the condition `h<1/2`.  Every nonprincipal
character modulo a prime is primitive.

For any fixed `epsilon>0`, a prime modulus for which some character has

```text
|D_X(chi)|>X^(1/2)Q^(1/8+2epsilon)                 (7.4)
```

contributes more than `X^4Q^(1+16epsilon)` to (7.3).  Hence the number of
such prime moduli is

```text
<<Q^(1-16epsilon+o(1)).                             (7.5)
```

For the actual residual length `R(q)asymp Q^h`, enlarge the **positive
incidence window** to one common length `Xasymp Q^h` before applying the
character expansion.  This is monotonicity of the incidence count; it does
not assert that a shorter character sum is bounded by a longer one.
For Schwartz tails, repeat (7.3) on the `O(log Q)` common dyadic residual windows
up to `Q^(1/2)` and use Schwartz decay plus the raw Schur bound beyond that
point.  The union of the exceptional sets only changes `Q^o(1)`.

Thus, for a density-one set of prime centers,

```text
effective tensor constant
 <<R^(1/4)q^(1/16+o(1)).                           (7.6)
```

Equations (3.2), (7.6), and the endpoint/support argument in Section 6
prove (0.6), including the density-one restricted depths.  At `h=16/33`,

```text
h/4+1/16=4/33+1/16=97/528,
1/2+97/528=361/528,                                (7.7)
```

as claimed.

---

## 8. A full-shell strongly imbalanced coefficient sector

The pure lower-shell tensor satisfies the same theorem: all its nodes are
nonzero modulo `q`, and its unmixed cubic is separated from `Y^3` on the
opposite side.  Split a full-shell vector as

```text
y=y_++y_-,
epsilon_side=min(||y_+||_2^2,||y_-||_2^2)/||y||_2^2. (8.1)
```

Pure-side cubic terms obey (0.2).  Every cross-side term contains at least
one minority vector.  Every conjugation/sign pattern has the same integer
product row-sum bound, so the raw three-vector Schur estimate (1.3) gives

```text
cross cubic <<R^(1/2)sqrt(epsilon_side)||y||_2^3.  (8.2)
```

Strong imbalance also repairs the possible reflected cross covariance.
Indeed the separate one-sided centered functions satisfy
`||Z_+||_(L2)asymp||y_+||_2` and
`||Z_-||_(L2)asymp||y_-||_2`; hence the reverse triangle inequality gives

```text
||Z_++Z_-||_(L2)
 >=c_w||y_major||_2-C_w||y_minor||_2
 asyp_w||y||_2                                      (8.3)
```

whenever `epsilon_side=o_w(1)`.  Thus the variance lower bound required by
the cubic endpoint survives arbitrary cross covariance in the sector below.

Consequently the all-prime one-sided exponent remains valid on the genuine
full-shell coefficient sector

```text
epsilon_side
 <=(R^(1/4)q^(3/32))^2/R
 =q^(3/16-h/2+o(1)).                               (8.4)
```

At `h=16/33`, (8.4) is

```text
epsilon_side<=q^(-29/528+o(1)).                    (8.5)
```

For the density-one corollary, the analogous threshold is

```text
epsilon_side<=q^(1/8-h/2+o(1))
             =q^(-31/264+o(1)).                    (8.6)
```

Combining (8.3) with the endpoint argument proves the corresponding
full-shell support estimate for every coefficient vector in this sector.
For a restricted transverse ray whose separating duals all lie in the
sector, support separation gives the same depth exponent.  This is **not**
a full-shell radial theorem: the radial dual infimum ranges over balanced
vectors as well.  Balanced two-sided vectors remain the obstruction to the
full QP game.

---

## 9. Scope, tests, and sources

```text
all odd prime centers, one-sided signed saving:      PROVED;
all-prime transverse ledger 755/1056:                PROVED IN RESTRICTED GAME;
density-one prime-center ledger 361/528:             PROVED IN RESTRICTED GAME;
full-shell strongly imbalanced dual support sector:  PROVED;
unconditional full-shell radial/transverse floor at new exponent: NOT PROVED;
balanced full-shell vectors:                         OPEN;
composite centers:                                   OPEN;
QP for every center, QP-to-strip, uniform strip:     NOT PROVED.
```

Executable exact checks:

```bash
python3 -m pytest -q \
  src/test_qp_prime_center_burgess_cubic_gate.py
```

The finite test reconstructs the product-residue count from all
multiplicative characters for a small prime, and the ledger tests verify
every displayed rational exponent.

Primary imported sources:

1. D. A. Burgess,
   [*On character sums and L-series*](https://doi.org/10.1112/plms/s3-12.1.193),
   Proc. London Math. Soc. (3) 12 (1962), 193--206, and
   [Part II](https://doi.org/10.1112/plms/s3-13.1.524),
   Proc. London Math. Soc. (3) 13 (1963), 524--536.
2. H. L. Montgomery and R. C. Vaughan,
   [*The large sieve*](https://doi.org/10.1112/S0025579300004708),
   Mathematika 20 (1973), 119--134 (multiplicative large sieve).

The incidence interpolation, the fixed-fibre argument, and the application
to the actual prime-power tensor are proved in this report.
