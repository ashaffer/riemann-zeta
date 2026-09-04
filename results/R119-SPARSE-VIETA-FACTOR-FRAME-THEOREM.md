# R119 sparse Vieta-factor frame theorem

Status: proved at the fixed-prime Blomer--Pascadi endpoint.  Replacing the
padded row coordinate `(P,Q,x)` by the coefficient-specific coordinates
`(P,x,y)`, with `Q=xy`, removes the diagonal `H` loss that blocked R116.
The row Gram matrix has norm `O(r^2 H^epsilon)` for a multiplier block of
length at most `H`, while a linear mixed Burgess bound and exact Vieta
uniqueness give

```text
sum_(P!=0,x,y)|C(P,x,y)|^2
 << H^(5/6+epsilon) product_i norm(z_i)_2^2.          (0.1)
```

Thus a block of `L=H` unit multipliers satisfies

```text
abs(T)<<r H^(11/12+epsilon) product_i norm(z_i)_2,   (0.2)
```

instead of the direct `r H product_i norm(z_i)_2`.  The zero-product and
central-matrix terms are smaller.  This is a genuine fixed-power endpoint
gain, with `delta=1/6` in the notation of R115--R116.

This report proves the local finite-field/BP theorem.  It does not by itself
prove a fixed zero-free strip.  The needed lossless representation of R105's
cutoff-complete Vaughan packet by these native profiles is not proved; R121
later shows that the available CRT/Hilbert representation spends the gain.
The R116 signed-coefficient primitive block is only a local packet, not a remaining
global gate.

Date: 2026-08-07.

**2026-09-02 successor correction (R121/R128/S0 audit).**  The
primitive-conductor block named here is only a balanced-semiprime local
packet.  R121 proves that the native CRT/Hilbert lift from the full Vaughan
packet spends the local gain, and R128 proves that faithful all-class
restoration returns the original R71 energy.  Thus this finite-field theorem
remains valid, but it is not presently attached to the global strip endpoint.

Companion reports:

* [`R115-RECIPROCAL-DISCRIMINANT-K-SUM-GATE.md`](R115-RECIPROCAL-DISCRIMINANT-K-SUM-GATE.md),
* [`R116-ACTUAL-PROFILE-TWISTED-FRAME-AND-ENDPOINT-RANK-GATE.md`](R116-ACTUAL-PROFILE-TWISTED-FRAME-AND-ENDPOINT-RANK-GATE.md),
* [`R116-VIETA-PRODUCT-ENERGY-ATTACK.md`](R116-VIETA-PRODUCT-ENERGY-ATTACK.md),
  and
* [`R112-CENTRAL-MATRIX-CORRECTION-BOUND.md`](R112-CENTRAL-MATRIX-CORRECTION-BOUND.md).

## 1. Setup and verdict

Let `r` be an odd prime and let

```text
r asymp H^2.                                         (1.1)
```

The four common, unmodulated BP autocorrelation profiles are denoted by
`z_i`.  Their supports lie in integer intervals of length `O(H r^epsilon)`.
As usual, the exponent in this formal cutoff is chosen after the requested
final epsilon; Schwartz tails outside it are negligible to arbitrary
power.  R112 gives the native point-flatness

```text
norm(z_i)_infinity
 <<H^(-1/2+epsilon)norm(z_i)_2.                      (1.2)
```

Put

```text
Z=product_(i=1)^4 norm(z_i)_2.                       (1.3)
```

For

```text
(a,b,c,d)=(h_1,h_2,h_3,h_4),
P=abcd,       x=a+c,       y=b+d,       Q=xy,        (1.4)
```

define the sparse-factor coefficient

```text
C(P,x,y)
 =sum_(abcd=P, a+c=x, b+d=y)z_1(a)z_2(b)z_3(c)z_4(d),
                                                               (1.5)
```

where the equalities are in `F_r`.  The sum coordinates inject as integers
once the harmless formal `r^epsilon` enlargement is suppressed; none of
the arguments below requires this injection except for a convenient
divisor refinement.

R116 proves that the exact dependence of the translated BP packet on the
nonzero multiplier `k` is

```text
e_r(-s k x) chi_r((P-kxy)(P-kxy+4k^2)),              (1.6)
```

where `chi_r` is the quadratic character, extended by `chi_r(0)=0`, and
`s` is the interval endpoint residue.  Thus set

```text
V_k(P,x,y)
 =e_r(-s k x)chi_r((P-kxy)(P-kxy+4k^2)).             (1.7)
```

The restriction `k!=0` is essential in the diagonal calculation.  A
possible zero multiplier is a separate elementary row and is not part of
the BP Kloosterman multiplier block.

The key observation is that `(P,x,y)` retains precisely one more sparse
Vieta factor than `(P,Q,x)`.  Its coefficient energy is power-smaller than
the generic enlarged energy, while its row Gram matrix still costs only
`r^2`, not `r^2H`.

## 2. The sparse-factor Gram theorem

Let `X,Y` be the actual sets of possible sum coordinates.  Thus

```text
#X,#Y<<H r^epsilon.                                  (2.1)
```

For distinct nonzero multipliers `k,l`, put

```text
R_(k,l)(q)
 =sum_(P mod r) chi_r(
   (P-kq)(P-kq+4k^2)(P-lq)(P-lq+4l^2)).             (2.2)
```

### Theorem 2.1 (sparse Vieta-factor row frame)

Let `K subset F_r^*` contain `L<=H r^epsilon` distinct multipliers.  Then
the Gram matrix of the rows (1.7), on `F_r times X times Y`, satisfies

```text
G_(k,k)=(r-2)#X#Y,                                   (2.3)

abs(G_(k,l))<<r^(3/2+epsilon),        k!=l,           (2.4)

norm(G)_op<<r^2 H^epsilon.                           (2.5)
```

Consequently, for arbitrary complex `alpha_k`,

```text
sum_(P,x,y)abs(sum_(k in K)alpha_k V_k(P,x,y))^2
 <<r^2 H^epsilon sum_k abs(alpha_k)^2.               (2.6)
```

#### Proof: diagonal

For fixed `(x,y)` the two roots in `P` are

```text
P=kxy,             P=kxy-4k^2.                      (2.7)
```

They are distinct because `r` is odd and `k!=0`.  Therefore

```text
sum_P chi_r((P-kxy)(P-kxy+4k^2))^2=r-2,             (2.8)
```

which proves (2.3).

#### Proof: all quartic degeneracies

Write `q=xy`.  The four roots of the polynomial in (2.2), with
multiplicity, are

```text
kq,       kq-4k^2,       lq,       lq-4l^2.         (2.9)
```

Each same-multiplier pair consists of distinct roots.  Hence the quartic
is a square if and only if the two unordered root pairs agree.  There are
exactly two possible matchings.

The same-orientation matching gives

```text
l=-k,                   q=0.                         (2.10)
```

The crossed matching gives

```text
k^2+l^2=0,              q=4k^2/(k-l).               (2.11)
```

Conversely, (2.10) or (2.11) makes the quartic a square.  These cases are
mutually exclusive for odd `r`.  Thus for a fixed pair `(k,l)` there is at
most one square-degenerate value of `q`.

For every other `q`, the Weil bound, after discarding any even root
multiplicity, gives

```text
abs(R_(k,l)(q))<=3 sqrt(r).                          (2.12)
```

This includes every one-root sharing and the nonsquare `q=0` cases.  On a
square-degenerate fiber the trivial bound `abs(R)<=r` suffices.

For a fixed nonzero `q`, each `x` determines at most one residue `y`; for
`q=0`, the fiber is contained in `x=0` or `y=0`.  Hence in either case

```text
#{(x,y) in X times Y:xy=q}<<H r^epsilon.             (2.13)
```

If integer lifts are used for nonzero `q`, the divisor bound improves
this to `H^epsilon`; the weaker uniform estimate (2.13) is already enough.
The endpoint phase has modulus one, so (2.12)--(2.13) give

```text
abs(G_(k,l))
 <=3 sqrt(r)#X#Y+r max_q #{(x,y):xy=q}
 <<sqrt(r)H^2 r^epsilon+rH r^epsilon
 <<r^(3/2+epsilon).                                 (2.14)
```

Finally, the diagonal is `O(rH^2r^epsilon)=O(r^2r^epsilon)`, and every
row has at most `L` off-diagonal entries.  Since `L<=H r^epsilon` and
`H asymp sqrt(r)`, Schur's test gives (2.5).  This proves the theorem.
QED.

The proof did not need cancellation in the endpoint phase.  In
particular it is uniform in `s`, including `s=0`.

## 3. Imported linear mixed Burgess estimate

The required literature input is considerably more standard than the
nonlinear polynomial-character estimate rejected in R115.

### Lemma 3.1 (linear mixed Burgess, explicit exponent)

Let `rho` be a nonprincipal multiplicative character modulo the prime
`r`.  If `I` is an interval of length at most `O(H)` with `H asymp sqrt(r)`,
then, uniformly in the position of `I` and in `t mod r`,

```text
abs(sum_(n in I)rho(n)e_r(tn))
 <<H r^(-1/24+epsilon).                              (3.1)
```

The same holds for a union of a fixed number of intervals.

#### Source and exponent audit

Heath-Brown and Pierce prove, for every real linear polynomial `f`, every
nonprincipal character modulo a prime, and every integer `nu>=2`,

```text
abs(sum_(N<n<=N+H)e(f(n))rho(n))
 <<_(nu,epsilon) H^(1-1/nu)
    r^(1/[4(nu-1)]+epsilon),                        (3.2)
```

uniformly in `N`; their admissible upper range contains `H asymp sqrt(r)`.
Take `f(n)=tn/r` and `nu=3`.  The right side is

```text
H^(2/3)r^(1/8+epsilon)
 <<H r^(-1/24+epsilon),                             (3.3)
```

which proves (3.1).  See D. R. Heath-Brown and L. B. Pierce,
[*Burgess bounds for short mixed character sums*](https://arxiv.org/abs/1404.1677),
Theorem 1.4 (published in J. London Math. Soc. 91 (2015)).
Chang's earlier general mixed theorem would supply an unspecified fixed
power here, but (3.2) makes the power ledger explicit.

For a formal BP support length `H r^vartheta`, use (3.2) directly.  Its
upper condition for `nu=3` is `H r^vartheta<r^(5/8)`, which holds after
choosing the tail-cutoff exponent `vartheta>0` sufficiently small.  Every
result below then acquires `r^(O(vartheta))`, absorbed into the displayed
epsilon.

Here is the unsuppressed ledger.  Put

```text
B=H r^vartheta.                                      (3.4)
```

Then the proof below gives

```text
norm(G)_op<<r B^2+L(sqrt(r)B^2+rB),                 (3.5)

N_*<<B^6/r+B^(13/3)r^(1/4+epsilon),                 (3.6)

E_*<<[r^(6vartheta)
       +H^(5/6)r^(13vartheta/3+epsilon)]Z^2,         (3.7)

E_(P=0)<<r^(vartheta+epsilon)Z^2.                    (3.8)
```

For `L<=H r^vartheta`, (3.5) is `r^(2+O(vartheta))`.
Given a requested final epsilon, choose `vartheta` smaller than a fixed
multiple of that epsilon.  Equations (3.5)--(3.8) then become the displayed
epsilon-loss bounds, while the fixed powers `1/6` and `1/12` are unchanged.
Thus the formal cutoff is not being silently identified with the effective
flatness scale.

No weighted mixed-character theorem is needed.  A direct partial-summation
argument would cost the total variation of the weight, and point-flatness
alone does not control that seminorm.  Instead Section 5 first proves an
unweighted collision bound for the containing support boxes and then uses
(1.2).  This avoids a hidden bounded-variation hypothesis on the actual
autocorrelation profiles.  Endpoint modulation also creates no seminorm:
it has already been extracted exactly as the phase in (1.7).

## 4. Opposite-pair energy identities

For two support intervals `I_1,I_3`, define, for a multiplicative character
`rho mod r`,

```text
S_13(rho)
 =sum_x abs(sum_(a+c=x; a,c!=0)
       1_(I_1)(a)1_(I_3)(c)rho(ac))^2.              (4.1)
```

Define `S_24(rho)` analogously.

### Lemma 4.1 (nonprincipal opposite-pair saving)

For every nonprincipal `rho`,

```text
S_13(rho)<<H^3 r^(-1/12+epsilon).                    (4.2)
```

#### Proof

Put

```text
A_rho(t)=sum_(a in I_1)rho(a)e_r(ta),
C_rho(t)=sum_(c in I_3)rho(c)e_r(tc).                (4.3)
```

Additive Parseval for the convolution in (4.1) gives

```text
S_13(rho)=1/r sum_(t mod r)
                 abs(A_rho(t))^2 abs(C_rho(t))^2.   (4.4)
```

By Lemma 3.1,

```text
max_t abs(A_rho(t))^2
 <<H^2 r^(-1/12+epsilon),                           (4.5)
```

while additive Parseval gives

```text
sum_t abs(C_rho(t))^2<=rH.                          (4.6)
```

Equations (4.4)--(4.6) prove (4.2).  QED.

### Lemma 4.2 (exact Vieta first moment)

One has

```text
sum_(rho mod r)S_24(rho)<<rH^2.                      (4.7)
```

#### Proof

Multiplicative orthogonality turns the left side into `r-1` times the
number of quadruples satisfying

```text
b+d=b'+d',             bd=b'd',
bd b'd'!=0.                                             (4.8)
```

Both equations are in `F_r`.  The unordered pairs `{b,d}` and `{b',d'}`
are roots of the same monic quadratic

```text
T^2-(b+d)T+bd.                                      (4.9)
```

Thus `{b,d}={b',d'}` and there are at most two ordered choices for the
second pair.  The count in (4.8) is `O(H^2)`, proving (4.7).  QED.

This exact first moment is the decisive asymmetry.  Multiplying two
pointwise Burgess bounds would waste a power; one uses (4.2) for only one
opposite pair and (4.7) for the other.

## 5. Nonzero-product coefficient energy

Let `N_*` be the collision energy of the map `(a,b,c,d)->(P,x,y)` on the
four unweighted support boxes, restricted to `P!=0`.

### Theorem 5.1 (unweighted sparse-factor collision bound)

At `r asymp H^2`,

```text
N_*<<H^(29/6+epsilon)=H^(5-1/6+epsilon).             (5.1)
```

#### Proof

Multiplicative orthogonality in the single coordinate `P=(ac)(bd)` gives
the exact identity

```text
N_*=1/(r-1) sum_(rho mod r)S_13(rho)S_24(rho).       (5.2)
```

For the principal character,

```text
S_13(1),S_24(1)<<H^3,                               (5.3)
```

so its contribution to (5.2) is `O(H^6/r)=O(H^4)`.

For all nonprincipal characters together, Lemmas 4.1 and 4.2 give

```text
1/(r-1) sum_(rho!=1)S_13(rho)S_24(rho)

 <=[max_(rho!=1)S_13(rho)]
   [1/(r-1)sum_rho S_24(rho)]

 <<H^3 r^(-1/12+epsilon) H^2
 =H^5 r^(-1/12+epsilon)
 <<H^(29/6+epsilon).                                (5.4)
```

This dominates the principal term and proves (5.1).  QED.

### Corollary 5.2 (native flat coefficient energy)

For the actual flat profiles,

```text
E_*:=sum_(P!=0,x,y)abs(C(P,x,y))^2
 <<H^(5/6+epsilon)Z^2.                              (5.5)
```

#### Proof

Expand the square in `E_*` and take absolute values.  Every surviving
collision has weight at most

```text
product_i norm(z_i)_infinity^2
 <<H^(-4+epsilon)Z^2                                (5.6)
```

by (1.2).  Multiply (5.1) by (5.6).  QED.

Thus the proposed `delta=4 eta` ledger is correct with

```text
eta=1/24,                 delta=1/6.                 (5.7)
```

Here `eta` is the power of `r` in the one-dimensional mixed sum; squaring
it in Parseval and using `r=H^2` produces the factor `H^(-1/6)`.

## 6. The `P=0` energy is smaller

The multiplicative-character identity (5.2) deliberately excluded zero.
The missing axes admit a direct tensor factorization.

Define

```text
A(x)=sum_(a+c=x)z_1(a)z_3(c),
A_0(x)=sum_(a+c=x, ac=0)z_1(a)z_3(c),               (6.1)
```

and define `B(y),B_0(y)` from `(z_2,z_4)`.  Inclusion-exclusion gives

```text
C(0,x,y)=A_0(x)B(y)+A(x)B_0(y)-A_0(x)B_0(y).        (6.2)
```

Young's inequality and support length give

```text
norm(A)_2<<H^(1/2+epsilon)norm(z_1)_2norm(z_3)_2.   (6.3)
```

Since `ac=0` means `a=0` or `c=0`, point-flatness gives

```text
norm(A_0)_2
 <<H^(-1/2+epsilon)norm(z_1)_2norm(z_3)_2.          (6.4)
```

The analogous estimates hold for `B,B_0`.  Taking the tensor `l^2` norm
in (6.2) now proves

```text
sum_(x,y)abs(C(0,x,y))^2<<H^epsilon Z^2.             (6.5)
```

Consequently the full coefficient energy obeys the same bound as (5.5):

```text
sum_(P,x,y)abs(C(P,x,y))^2
 <<H^(5/6+epsilon)Z^2.                              (6.6)
```

This also shows why merely applying an unweighted collision count on the
axes would be wasteful: the native point evaluations are essential there.

## 7. Endpoint block bound

Let

```text
T=sum_(k in K)alpha_k sum_(P,x,y)C(P,x,y)V_k(P,x,y).
                                                               (7.1)
```

Cauchy--Schwarz, (2.6), and (6.6) give the fixed-prime theorem

```text
abs(T)
 <<r H^(5/12+epsilon)norm(alpha)_2 Z.               (7.2)
```

For `L` unit-size coefficients,

```text
abs(T)<<r H^(5/12+epsilon)sqrt(L)Z.                  (7.3)
```

At the transition `L=H`, this is

```text
abs(T)<<r H^(11/12+epsilon)Z.                        (7.4)
```

The separated direct estimate is

```text
abs(T)<<L H^2 Z=rHZ                 when L=H.        (7.5)
```

Thus (7.4) saves the fixed factor

```text
H^(-1/12+epsilon)=r^(-1/24+epsilon).                (7.6)
```

This is exactly the overlap that the padded `(P,Q,x)` frame in R116 could
not produce.

## 8. Central matrices and transition-scale audit

The ordinary quadratic character in (1.7) vanishes at discriminant zero,
whereas the BP `SL_2(F_r)` character has the special central value recorded
in R112.  It must not be inferred from (1.7).

For each fixed nonzero `k`, absorb the endpoint modulation into

```text
z_(1,k)(a)=e_r(-ska)z_1(a),
z_(3,k)(c)=e_r(-skc)z_3(c).                          (8.1)
```

These modulations preserve both `l^2` norms and point-flatness.  R112's
exact central classification and universal-profile estimate therefore
give a central coefficient of size

```text
<<H^(-1+epsilon)Z                                   (8.2)
```

before the special character factor `r`.  Summing a multiplier block gives

```text
abs(T_cent)
 <<r H^(-1+epsilon)norm(alpha)_1 Z
 <<r H^(-1+epsilon)sqrt(L)norm(alpha)_2 Z.           (8.3)
```

For unit coefficients and `L=H`, this is `rZ`, up to epsilon powers.  It
is smaller than the newly proved main bound `rH^(11/12)Z`, not merely
smaller relative to its own axis direct estimate.  Ramified or zero
multipliers are excluded by `K subset F_r^*`; if the global decomposition
produces one, it is handled separately.

## 9. What was proved, and what remains

The following parts of the proposed breakthrough survive audit:

```text
sparse (P,x,y) Gram norm, L<=H              PROVED;
all shared-root and square-quartic fibers    CLASSIFIED;
mixed-character exponent eta=1/24           IMPORTED EXPLICITLY;
unweighted nonzero-P energy H^(29/6+eps)     PROVED;
native energy H^(5/6+eps)Z^2                PROVED;
P=0 energy                                  IDEAL SCALE;
central correction at full transition       LOWER ORDER;
fixed-prime L=H gain H^(-1/12+eps)          PROVED.
```

One proposed justification required correction: partial summation for the
actual smooth weights is not automatic from point-flatness, because it
would require a bounded-variation seminorm.  The support-majorization
argument in Corollary 5.2 removes that hypothesis completely.

The remaining global interfaces are not finite-field gaps in this theorem:

1. R105 must supply the full cutoff-complete R71/Vaughan high-mode packet
   as a controlled sum of common native BP profiles with a genuine
   nonzero multiplier block of length at most `H`.
2. The cost of the short-box partition and any projective separation must
   be checked against the `H^(1/12)` gain; an `H^epsilon` cost is harmless,
   an unrecorded fixed power is not.
3. The primitive-conductor smooth Möbius carrier isolated by R116 is a local
   packet only.  The global arithmetic gate is the complete R128/R71 energy;
   no lossless adapter from that energy to this BP endpoint is proved.

Accordingly, (7.4) is a real new cancellation theorem and invalidates the
claim that the actual endpoint phase necessarily forces equality with the
direct bound.  It does not yet decide the existence of a fixed zero-free
strip.
