# R118 endpoint square-function and sparse-coordinate prime-average gate

Status: the scalar three-coordinate large sieve in `(P,Q,x)` is proved to
stop exactly at the R116 endpoint, and that failure is sharp for arbitrary
coefficient arrays.  Full endpoint Parseval does not repair a family of only
`H` short-box endpoints.  However, this padded formulation discards the
coefficient-specific identity

```text
Q=xy,                 x=h_1+h_3,       y=h_2+h_4.
```

Retaining `(P,x,y)` instead gives a sparse row frame of norm
`O(r^2 H^epsilon)` for every nonzero multiplier block of length `L<=H`.
A vector-valued one-dimensional large sieve in the long integer coordinate
`P` proves that its folded coefficient energy, averaged over primes
`r asymp R=H^2`, is `O(R H^epsilon Z^2)`.  Consequently the full translated
endpoint phase satisfies

```text
abs(sum_(r~R) T_r) << R^2 sqrt(L) H^epsilon Z.       (0.1)
```

For flat unit outer and multiplier weights the direct bound is `R^2 L Z`.
Thus (0.1) saves `L^(-1/2)H^epsilon`, in particular
`H^(-1/2+epsilon)` at `L=H`.  The endpoint phase is therefore no longer the
local prime-modulus obstruction.

This closes the R115--R117 actual-profile endpoint gate after a common BP
short-box packet has been produced.  It does not construct such packets
from the cutoff-complete R105 Vaughan tail, whose native modulus is composite
and whose two coefficient supports are full-Fourier and modular-inverse
images.  The special central matrices must also remain paired as in R112.
No fixed zero-free strip is proved here.

Date: 2026-08-07.

Companion reports:

* [`R105-QH-VAUGHAN-TAIL-NATIVE-BRIDGE-AUDIT.md`](R105-QH-VAUGHAN-TAIL-NATIVE-BRIDGE-AUDIT.md),
* [`R116-ACTUAL-PROFILE-TWISTED-FRAME-AND-ENDPOINT-RANK-GATE.md`](R116-ACTUAL-PROFILE-TWISTED-FRAME-AND-ENDPOINT-RANK-GATE.md),
* [`R117-VARYING-PRIME-VIETA-LARGE-SIEVE-GATE.md`](R117-VARYING-PRIME-VIETA-LARGE-SIEVE-GATE.md), and
* [`R119-SPARSE-VIETA-FACTOR-FRAME-THEOREM.md`](R119-SPARSE-VIETA-FACTOR-FRAME-THEOREM.md).

## 1. Exact translated block

Let

```text
R=H^2,       mathcal P(R)={r prime:R<=r<=2R}.        (1.1)
```

The harmless powers in the formal Schwartz cutoff are absorbed into every
displayed `H^epsilon`.  Let the four common, unmodulated BP
autocorrelations be `z_i`, supported on `abs(h)<<H`, and put

```text
Z=product_(i=1)^4 norm(z_i)_2.                       (1.2)
```

Their native point flatness, proved in R112, is

```text
abs(z_i(0))<<H^(-1/2+epsilon)norm(z_i)_2.            (1.3)
```

For

```text
(a,b,c,d)=(h_1,h_2,h_3,h_4),
P=abcd,       x=a+c,       y=b+d,       Q=xy,        (1.4)
```

R116 identifies the exact multiplier and endpoint dependence as

```text
e_r(-s_r kx)
 chi_r((P-kxy)(P-kxy+4k^2)).                         (1.5)
```

Here `s_r` is arbitrary and `k` is nonzero modulo `r`.  The zero multiplier
was removed before the R81 grouping and would in any case be a separate
elementary row.

Define the common integer coefficient

```text
C(P,x,y)
 =sum_(abcd=P,a+c=x,b+d=y)product_i z_i(h_i),        (1.6)
```

and its long-coordinate fold

```text
C_r(p,x,y)=sum_(P=p mod r)C(P,x,y),
E_r(C)=sum_(p mod r,x,y)abs(C_r(p,x,y))^2.           (1.7)
```

For a set `K_r` of `L` distinct nonzero multipliers, set

```text
T_r=sum_(k in K_r)a_(r,k)
 sum_(p,x,y)C_r(p,x,y)e_r(-s_rkx)
 chi_r((p-kxy)(p-kxy+4k^2)).                         (1.8)
```

The rest of the report proves the prime-averaged estimate for (1.8).

## 2. The padded three-dimensional large sieve is sharply insufficient

It is useful first to close the tempting black-box route.  Let an arbitrary
array `B(P,Q,x)` be supported in a rectangle of side lengths

```text
N_P<<R^2,             N_Q<<R,             #X<<H,    (2.1)
```

and write `Bhat_r(alpha,beta,gamma)` for its additive Fourier transform.
For arbitrary endpoints `s_r` and multiplier sets `K_r` of size at most
`H`, R117 Theorem 3.1 and Cauchy in `x` give

```text
sum_(r in mathcal P(R))sum_(alpha mod r;alpha!=0)
 sum_(k in K_r)
 abs(Bhat_r(alpha,-alpha k,-s_r k))^2
 <<R^3 H norm(B)_2^2.                                (2.2)
```

Indeed, for fixed `x`, the map

```text
(alpha,k)|->(alpha,-alpha k)                         (2.3)
```

is injective because `alpha!=0`.  Its rows are a subset of the two-
dimensional family in R117.  If `B_x(P,Q)=B(P,Q,x)`, then

```text
abs(sum_x e_r(-s_rkx)Bhat_(r,x)(alpha,-alpha k))^2
 <=H sum_x abs(Bhat_(r,x)(alpha,-alpha k))^2.        (2.4)
```

Summing (2.4), applying R117 separately to every `x`, and then summing `x`
proves (2.2).

The factor `H` cannot be removed for arbitrary arrays.  Fix one row
`(r_0,alpha_0,k_0)` and take, on the whole rectangle,

```text
B(P,Q,x)=e_(r_0)(-alpha_0P+alpha_0k_0Q+s_(r_0)k_0x).
                                                               (2.5)
```

The selected Fourier coefficient has modulus `N_P N_Q #X`, while
`norm(B)_2^2=N_P N_Q #X`.  Hence the operator ratio is

```text
N_P N_Q #X asymp R^3H.                               (2.6)
```

Thus the diagonal physical volume alone rules out any
coefficient-uniform improvement in (2.2).  After additive inversion of the
quadratic character, Parseval for its Fourier coefficients gives the
corresponding scalar estimate

```text
abs(T_nonzero)<=R^(3/2)H^(1/2)norm(B)_2
                    (sum_(r,k)abs(a_(r,k))^2)^(1/2). (2.7)
```

For unit weights, `L=H`, and `#mathcal P(R)<=R`, (2.7) is `H^5 norm(B)_2`,
exactly the separated direct scale.  The long `P` coordinate does not repay
an independent rectangular `x` coordinate.

This sharp counterexample concerns the padded coefficient class.  It does
not apply to (1.6), because there `Q` and `x` are not independent.

## 3. What endpoint Parseval does and does not buy

There is a second natural attempt.  For a prime `r` and an arbitrary array
`A(k,x)`, put

```text
F(s)=sum_(k,x)A(k,x)e_r(-skx).                       (3.1)
```

Grouping by the product residue and applying Parseval gives the exact
identity

```text
sum_(s mod r)abs(F(s))^2
 =r sum_(n mod r)abs(sum_(kx=n mod r)A(k,x))^2.      (3.2)
```

If `0<abs(k),abs(x)<<H` and `r asymp H^2`, every product fiber in (3.2) has
`H^epsilon` integer lifts by the divisor bound.  Hence

```text
sum_(s mod r)abs(F(s))^2
 <<r H^epsilon sum_(k,x)abs(A(k,x))^2.               (3.3)
```

The slice `x=0` is coherent for every endpoint and must be returned to the
untwisted R117 estimate; it is not canceled by (3.2).

Formula (3.3) is real cancellation if all `r` endpoint residues are
averaged.  A disjoint critical short-box partition has only `O(H)`
endpoints.  Restricting (3.3) to such a set and dividing by its cardinality
costs

```text
r/H asymp H                                           (3.4)
```

per endpoint, exactly the scalar Cauchy cost.  This is also sharp for an
arbitrary array: for one selected endpoint `s_0`, choosing
`A(k,x)=e_r(s_0kx)` makes its row coherent.  Consequently full endpoint
orthogonality, by itself, does not improve the uniform `H`-endpoint block.

Sections 2--3 fail for the same reason: they treat `x` as an independent
degree of freedom.  The correct repair is algebraic rather than a stronger
Fourier inequality.

## 4. Sparse `(P,x,y)` row frame

For fixed `r`, define

```text
V_k(p,x,y)=e_r(-s_rkx)
 chi_r((p-kxy)(p-kxy+4k^2)).                         (4.1)
```

Let `X,Y` be the actual sets of possible sum coordinates, so
`#X,#Y<<H`.  The following estimate is uniform in the endpoint `s_r`.

### Theorem 4.1 (endpoint-retaining sparse frame)

If `K subset F_r^*` has `L<=H` distinct elements, then

```text
norm((<V_k,V_l>)_(k,l in K))_op<<r^2H^epsilon.      (4.2)
```

Equivalently,

```text
sum_(p,x,y)abs(sum_(k in K)alpha_kV_k(p,x,y))^2
 <<r^2H^epsilon sum_k abs(alpha_k)^2.                (4.3)
```

#### Proof

For fixed `(x,y)` and nonzero `k`, the two roots in `p` are distinct, so

```text
<V_k,V_k>=(r-2)#X#Y<<rH^2<<r^2.                    (4.4)
```

For `k!=l`, put `q=xy`.  The four roots in the complete `p`-sum are

```text
kq,       kq-4k^2,       lq,       lq-4l^2.         (4.5)
```

The quartic is a square precisely when the two unordered root pairs agree.
The same-orientation and crossed matchings give, respectively,

```text
l=-k,        q=0;                                    (4.6)

k^2+l^2=0,  q=4k^2/(k-l).                           (4.7)
```

These exhaust the square cases.  If some but not all roots coincide, the
even multiplicities may be discarded and the remaining polynomial is still
nonsquare.  Thus outside (4.6)--(4.7), the complete character sum is
`O(sqrt(r))`; on a square fiber it is `O(r)`.

There are `O(H)` pairs `(x,y)` with `xy=0`.  For a fixed nonzero residue
`q`, the integer ranges `abs(x),abs(y)<<H` and `r asymp H^2` reduce
`xy=q mod r` to a bounded number of fixed integer products, so the divisor
bound gives `H^epsilon` pairs.  The endpoint phase has modulus one.
Consequently

```text
abs(<V_k,V_l>)
 <<sqrt(r)H^2+rH
 <<r^(3/2)H^epsilon,                 k!=l.           (4.8)
```

Schur's test, `L<=H`, and `H asymp sqrt(r)` now give

```text
rH^2+Lr^(3/2)<<r^2,                                 (4.9)
```

which proves (4.2)--(4.3).  QED.

The diagonal in (4.4) is `rH^2`, not the `r^2H` diagonal of the padded
`(P,Q,x)` frame.  This is the exact recovered factor.

## 5. Integer sparse-factor energy

The coefficient (1.6) satisfies two bounds needed for the prime average.

### Lemma 5.1

Under (1.3),

```text
norm(C)_2^2<<H^epsilon Z^2,                          (5.1)

norm(D)_2^2<<H^(2+epsilon)Z^2,
D(x,y)=sum_P C(P,x,y).                               (5.2)
```

#### Proof

For `P!=0`, fixing the integer product `P=abcd` leaves only
`H^epsilon` signed factorizations in the support.  Imposing `x=a+c` and
`y=b+d` can only reduce the fiber.  Fiberwise Cauchy therefore gives

```text
sum_(P!=0,x,y)abs(C(P,x,y))^2<<H^epsilon Z^2.       (5.3)
```

For `P=0`, define the opposite-pair convolutions

```text
A(x)=sum_(a+c=x)z_1(a)z_3(c),
A_0(x)=sum_(a+c=x,ac=0)z_1(a)z_3(c),                (5.4)
```

and define `B,B_0` from `z_2,z_4`.  Inclusion--exclusion gives exactly

```text
C(0,x,y)=A_0(x)B(y)+A(x)B_0(y)-A_0(x)B_0(y).        (5.5)
```

Young's inequality and (1.3) give

```text
norm(A)_2<<H^(1/2)norm(z_1)_2norm(z_3)_2,
norm(A_0)_2<<H^(-1/2+epsilon)
                  norm(z_1)_2norm(z_3)_2,           (5.6)
```

and the analogous estimates for `B,B_0`.  Taking tensor norms in (5.5)
proves an `H^epsilon Z^2` bound for the `P=0` energy.  Together with
(5.3), this proves (5.1).

Finally, summing (1.6) over `P` removes the product condition and gives

```text
D(x,y)=A(x)B(y).                                    (5.7)
```

The two first estimates in (5.6) for `A,B` imply (5.2).  QED.

The point-flatness is used only to prevent the zero-product axes from
reintroducing a power.  No smoothness or bounded-variation hypothesis on
the profiles is present.

## 6. Vector-valued long-coordinate prime average

The sparse frame folds only the long integer coordinate `P`; `(x,y)` stay
as Hilbert-space coordinates.  This is the prime-average mechanism which
replaces the fixed-prime mixed-Burgess energy in R119.

### Theorem 6.1 (Hilbert-valued folded-`P` large sieve)

Let `C(P,x,y)` be supported on an integer `P` interval of length `O(R^2)`
and on arbitrary finite `(x,y)` sets.  With (1.7),

```text
sum_(r in mathcal P(R))E_r(C)
 <<R norm(C)_2^2+norm(D)_2^2,                        (6.1)
```

where `D(x,y)=sum_P C(P,x,y)`.

#### Proof

For every fixed `(x,y)`, additive Parseval gives

```text
E_r(C)
 =r^(-1)sum_(alpha mod r)
   sum_(x,y)abs(sum_P C(P,x,y)e_r(alpha P))^2.       (6.2)
```

For `alpha!=0`, the fractions `alpha/r` are reduced.  The classical
additive large sieve, applied separately to each Hilbert coordinate and
then summed over `(x,y)`, gives

```text
sum_(r in mathcal P(R))sum_(alpha!=0)
 sum_(x,y)abs(sum_P C(P,x,y)e_r(alpha P))^2
 <<R^2 norm(C)_2^2.                                 (6.3)
```

The usual constant is `R^2+N_P`, and `N_P<<R^2` here.  Since `r asymp R`,
the nonzero part of (6.2) is at most `R norm(C)_2^2`.

At `alpha=0`, the inner Hilbert vector is exactly `D`.  Hence

```text
sum_(r in mathcal P(R))r^(-1)norm(D)_2^2
 <<norm(D)_2^2.                                     (6.4)
```

Equations (6.2)--(6.4) prove (6.1).  QED.

Combining Theorem 6.1 with Lemma 5.1 gives the actual-profile estimate

```text
sum_(r in mathcal P(R))E_r(C)
 <<R H^epsilon Z^2.                                 (6.5)
```

The repeated zero frequency in `P` is not discarded: it is exactly the
rank-one opposite-pair tensor (5.7), whose norm is already at the allowed
`RZ^2` scale.

## 7. Endpoint-complete prime-averaged bound

Theorem 4.1 and Cauchy in the coefficient space give, for every prime,

```text
abs(T_r)^2
 <<r^2H^epsilon E_r(C)sum_(k in K_r)abs(a_(r,k))^2. (7.1)
```

Therefore, for arbitrary outer weights `omega_r`, (6.5) gives

```text
abs(sum_r omega_rT_r)
 <<R^(3/2)H^epsilon Z
   [sum_r abs(omega_r)^2
          sum_(k in K_r)abs(a_(r,k))^2]^(1/2).       (7.2)
```

For `abs(omega_r),abs(a_(r,k))<=1`, `#K_r<=L`, and the elementary bound
`#mathcal P(R)<=R`, this becomes

```text
abs(sum_r omega_rT_r)<<R^2 sqrt(L)H^epsilon Z.       (7.3)
```

On the other hand, `norm(product_i z_i)_1<=H^2Z`, so the separated direct
bound is

```text
sum_(r,k)H^2Z<<R L H^2Z=R^2LZ.                     (7.4)
```

Thus the relative factor in (7.3) is

```text
L^(-1/2)H^epsilon.                                  (7.5)
```

At the exact R114--R116 transition `L=H`, (7.5) is
`H^(-1/2+epsilon)`.  The endpoint phase has been retained throughout;
there is no anchored-interval qualification.

There is also a projective common-profile version.  Suppose

```text
C_r=sum_nu Omega_nu(r)C_nu                           (7.6)
```

and every `C_nu` is built from native-flat profiles as above, with scale
`Z_nu`.  Applying (7.2) term by term gives

```text
abs(sum_r T_r)
 <<R^(3/2)H^epsilon
 sum_nu Z_nu
 [sum_r abs(Omega_nu(r))^2
          sum_k abs(a_(r,k))^2]^(1/2).               (7.7)
```

Hence the `H^o(1)` projective common-profile decompositions in R111 spend
only `H^o(1)` of the fixed `H^(-1/2)` reserve.  Arbitrary outer scalars are
allowed through the displayed weighted `l^2` norm.

## 8. Zero-product and central transition audit

The `P=0` and special-central pieces are not hidden in the comparison with
the off-axis main term.

On `P=0`, Lemma 5.1 gives

```text
sum_(x,y)abs(C(0,x,y))^2<<H^epsilon Z^2.            (8.1)
```

Every restricted row has modulus at most one on `X times Y`, which has
`O(H^2)=O(r)` points.  Bounding every off-diagonal Gram entry trivially and
using `L<=H` gives restricted Gram norm `O(rL)`.  Therefore

```text
abs(T_(r,P=0))
 <<(rL)^(1/2)H^epsilon Z
      (sum_k abs(a_(r,k))^2)^(1/2).                  (8.2)
```

If

```text
mathcal A_2^2
 =sum_r abs(omega_r)^2sum_k abs(a_(r,k))^2,          (8.3)
```

then Cauchy over at most `R` prime rows yields

```text
abs(sum_r omega_rT_(r,P=0))
 <<R sqrt(L)H^epsilon Z mathcal A_2.                 (8.4)
```

For the special central correction, fix a nonzero `k` and absorb the
endpoint modulation into `z_1,z_3`.  This preserves their `l^2` norms and
point flatness.  R112's exact `g=plusminus I` classification then bounds
the coefficient before the special character factor by

```text
<<H^(-1+epsilon)Z.                                  (8.5)
```

The special character contributes `r`.  Summing in `k`, using
`norm(a_r)_1<=sqrt(L)norm(a_r)_2`, and then applying outer Cauchy gives
the same scale as (8.4):

```text
abs(sum_r omega_rT_(r,cent))
 <<R sqrt(L)H^epsilon Z mathcal A_2.                 (8.6)
```

Because the main estimate (7.2) is
`R^(3/2)H^epsilon Z mathcal A_2`, both (8.4) and (8.6) are smaller by

```text
sqrt(L/R)<=H^(-1/2)             when L<=H.           (8.7)
```

For flat unit weights and `L=H`, the two exceptional contributions are
`O(R^2H^epsilon Z)`, while (7.3) is
`O(R^2H^(1/2+epsilon)Z)`.  Thus neither the zero-product axis nor the
special central value spends the transition gain.  Nonzero `k` also means
that the R112 central word is unramified; a separately introduced zero
multiplier remains outside this statement.

## 9. Scope and the surviving bridge

The result changes the endpoint ledger as follows.

```text
padded (P,Q,x) scalar large sieve                SHARP / NO GAIN;
H-endpoint Parseval alone                        NO GAIN;
sparse (P,x,y) row frame, L<=H                   norm << r^2H^epsilon;
prime-averaged folded sparse coefficient energy  << R H^epsilon Z^2;
translated BP transition gain, L=H              H^(-1/2+epsilon);
fixed zero-free strip                            NOT YET PROVED.      (9.1)
```

The character in (1.5) is the ordinary noncentral Legendre contribution.
Trace `plusminus2` is not synonymous with the special central matrices
`plusminus I`; Section 8 is the required separate transition-scale audit.

Most importantly, (1.8) begins with a genuine prime-modulus BP short box
whose profiles have already been made common across the outer prime.
R105's exact cutoff-complete Vaughan-tail formula instead has

```text
modulus             c=db, composite and of size X;
first support       a full Fourier residue system;
second support      an inverse image of a sqrt(c)-interval.           (9.2)
```

No theorem in this report turns (9.2) into a subpower projective family of
the packets (1.8).  The signed-coefficient primitive-conductor dual isolated in R116 is
another formulation of the same **balanced-semiprime local** bridge, not the
global endpoint.  R128 later restores all omitted classes and returns the
original R71 energy.  What has changed
is precise: once that native packet is available, neither the translated
endpoint phase nor the `L=H` multiplier transition consumes the power.
