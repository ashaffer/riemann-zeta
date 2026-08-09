# R117 varying-prime Vieta large-sieve gate

Status: a sharp critical-aspect two-dimensional additive large sieve is
proved after removing the repeated zero frequency in the long coordinate.
The unrestricted heuristic constant `R^3+N_1N_2` is false, both for
same-prime character pairs in general ranges and, when principal characters
are retained, already on the critical Vieta rectangle.  The offending
zero/principal slice can nevertheless be estimated at the ideal scale for
the Vieta-product coefficients.  Consequently the fixed-modulus `H` loss in
R115 disappears after averaging the **untwisted common-profile** coefficient
energy over primes `r asymp R=H^2`.

The actual translated Blomer--Pascadi packet has the additional phase
`e_r(-s k(h_1+h_3))`.  Retaining this phase adds a third coordinate of length
`H`; its diagonal large-sieve cost is exactly `H`.  Thus the new average
closes the anchored/untwisted coefficient-energy problem but still reaches
the direct endpoint for the full R116 packet at a multiplier block of length
`H`.  No fixed zero-free strip is proved or disproved here.

Date: 2026-08-07.

Predecessors:

* [`R115-RECIPROCAL-DISCRIMINANT-K-SUM-GATE.md`](R115-RECIPROCAL-DISCRIMINANT-K-SUM-GATE.md),
  for the exact `(P,Q)` frame and the fixed-prime `H`-loss;
* [`R116-ACTUAL-PROFILE-TWISTED-FRAME-AND-ENDPOINT-RANK-GATE.md`](R116-ACTUAL-PROFILE-TWISTED-FRAME-AND-ENDPOINT-RANK-GATE.md),
  for the endpoint phase and its extra `x=h_1+h_3` coordinate; and
* [`R111-OUTER-PRIME-PACKET-SEPARATION-AUDIT.md`](R111-OUTER-PRIME-PACKET-SEPARATION-AUDIT.md),
  for common-profile projective separation and the still-open full-R105
  short-box lift.

## 1. Verdict and normalization

Let

```text
R=H^2,
mathcal P(R)={r prime:R<=r<=2R}.                       (1.1)
```

For an integer coefficient array `C(P,Q)`, define its reduction energy by

```text
E_r(C)
 =sum_(p,q mod r)
   abs(sum_(P=p,Q=q mod r) C(P,Q))^2.                 (1.2)
```

With

```text
Chat_r(a,b)=sum_(P,Q)C(P,Q)e_r(aP+bQ),                (1.3)
```

additive Parseval gives the exact normalization

```text
E_r(C)=r^(-2)sum_(a,b mod r)abs(Chat_r(a,b))^2.       (1.4)
```

Suppose `C` is supported in a translate of a rectangle of side lengths

```text
N_P<<R^2,                    N_Q<<R.                  (1.5)
```

Put

```text
D(Q)=sum_P C(P,Q).                                   (1.6)
```

The main large-sieve theorem is

```text
sum_(r in mathcal P(R)) E_r(C)
 <<R norm(C)_2^2+norm(D)_2^2.                        (1.7)
```

The first term comes from every nonzero additive frequency in the long
`P` coordinate.  The second is exactly its repeated zero-frequency slice.
There is no hidden prime-counting normalization in (1.7).

For the Vieta coefficients

```text
P=h_1h_2h_3h_4,
Q=(h_1+h_3)(h_2+h_4),                                (1.8)

C(P,Q)=sum_(h:(P(h),Q(h))=(P,Q))product_i z_i(h_i),  (1.9)
```

with `abs(h_i)<<H` and the native point flatness

```text
norm(z_i)_infinity
 <<H^(-1/2+epsilon)norm(z_i)_2,                       (1.10)
```

one has

```text
norm(C)_2^2<<H^epsilon Z^2,
norm(D)_2^2<<H^(2+epsilon)Z^2=R H^epsilon Z^2,
Z^2=product_i norm(z_i)_2^2.                         (1.11)
```

Therefore

```text
sum_(r in mathcal P(R))E_r(C)
 <<R H^epsilon Z^2.                                  (1.12)
```

The fixed-prime arbitrary-fiber theorem in R115 gives only
`E_r<<H^(1+epsilon)Z^2`.  Summing it row by row costs `R H Z^2` in the
power ledger.  Formula (1.12) removes that entire factor `H` on average.

## 2. Why the naive same-prime pair large sieve is false

There are two different obstructions, and they should not be conflated.

### 2.1 Even nonprincipal pairs require marginal terms in general ranges

Consider the proposed multiplicative inequality

```text
sum_(r in mathcal P(R))sum_(chi,psi mod r; nonprincipal)
 abs(sum_(m,n)A_(m,n)chi(m)psi(n))^2

 <<R^epsilon(R^3+N_1N_2)norm(A)_2^2,                 (2.1)
```

for an arbitrary array in an `N_1` by `N_2` rectangle.  Characters are
extended by zero on multiples of `r`.

Fix one prime `r_0 in [R,2R]`, put `N_2=1`, and support `A` on

```text
(m,n)=(1+t r_0,1),             0<=t<M,
M asymp N_1/R.                                      (2.2)
```

Every pair of nonprincipal characters modulo `r_0` takes the value one on
this support.  The single `r_0` row is therefore

```text
>>(r_0-2)^2 M^2,                                    (2.3)
```

while `norm(A)_2^2=M`.  The operator ratio is

```text
>>R^2M asymp R N_1.                                 (2.4)
```

Taking `N_1=R^(2+delta)`, `0<delta<1`, contradicts (2.1).  Thus a
coefficient-uniform theorem in arbitrary aspect ratios needs at least the
marginal terms `R N_1+R N_2`.  At `N_1=R^2`, (2.4) is exactly `R^3`; this
example saturates, rather than contradicts, the critical long-coordinate
scale used below.

### 2.2 Principal characters fail already on the critical rectangle

If the principal characters are included, there is a stronger coherent
axis.  Put

```text
A_(m,1)=1,                  1<=m<=N_1=R^2.            (2.5)
```

For each prime `r`, choose the principal character in the first coordinate
and sum over all characters in the second.  Apart from `O(N_1/r)` omitted
multiples of `r`, the inner sum is `N_1`.  Hence

```text
LHS>>(sum_(r in mathcal P(R))r)N_1^2
    >>R^2 N_1^2/log R.                               (2.6)
```

Since `norm(A)_2^2=N_1`, the operator ratio is
`>>R^2N_1/log R=R^4/log R`, whereas `R^3+N_1` is only `O(R^3)`.

The additive version is even more transparent.  For

```text
A(P,0)=1,                  1<=P<=R^2,                 (2.7)
```

the frequency `a=0` gives the value `R^2` for all `b mod r` and for every
prime row.  The full two-dimensional additive family therefore also has
operator norm `>>R^4/log R`, not `R^3`.

This is the precise defect in the heuristic “number of points is `R^3`, so
the large-sieve constant is `R^3`.”  The point `(0,b/r)` has a first
coordinate which is identical for every modulus.  In multiplicative
language this is the principal-character axis.

## 3. Critical-aspect nonzero-frequency theorem

The repeated axis is the only obstruction needed at the Vieta aspect
ratio.

**Theorem 3.1 (same-denominator two-dimensional large sieve).**  Let
`C(P,Q)` be supported in two integer intervals of lengths `O(R^2)` and
`O(R)`.  Then

```text
sum_(r in mathcal P(R))
 sum_(a mod r;a!=0)sum_(b mod r)abs(Chat_r(a,b))^2
 <<R^3 norm(C)_2^2.                                  (3.1)
```

The implied constant depends only on the fixed support constants.

As a corollary, at this critical aspect ratio the pair-character bound

```text
sum_(r in mathcal P(R))
 sum_(chi,psi mod r; nonprincipal)
 abs(sum_(P,Q)C(P,Q)chi(P)psi(Q))^2
 <<R^3 norm(C)_2^2                                   (3.2)
```

is valid.  Indeed, Gauss inversion expresses each nonprincipal character
through the nonzero additive frequencies, with Gauss norm `sqrt(r)`.
The two factors `r^(-1/2)` give a product factor `r^(-1)`; after squaring,
Plancherel in the two character variables bounds the fixed-`r` left side
of (3.2) by

```text
sum_(a,b mod r;a b!=0)abs(Chat_r(a,b))^2,             (3.3)
```

which is contained in (3.1).

### Proof of Theorem 3.1

The cross-prime near-collisions are the only nonstandard point, so the
Schur calculation is given in full.

By duality, choose coefficients `lambda_(r,a,b)` on

```text
X={(r,a,b):r in mathcal P(R), 1<=a<r, 0<=b<r}.       (3.4)
```

Majorize the two physical support intervals by fixed smooth cutoffs of
lengths `asymp R^2` and `asymp R`.  Their periodic Fourier kernels satisfy,
for every fixed `A>3`,

```text
abs(K_1(t))<<_A R^2 sum_(ell in Z)
                   (1+R^2 abs(t-ell))^(-A),

abs(K_2(t))<<_A R sum_(ell in Z)
                   (1+R abs(t-ell))^(-A).            (3.5)
```

After expanding the dual square, its Gram entry between `(r,a,b)` and
`(s,c,d)` is bounded by

```text
abs(K_1(a/r-c/s)K_2(b/r-d/s)).                       (3.6)
```

It suffices by Schur's test to prove that every absolute row sum is
`O(R^3)`.

For `s=r`, sampling (3.5) on the `1/r` grid gives

```text
sum_(c mod r)abs(K_1((a-c)/r))<<R^2+r<<R^2,

sum_(d mod r)abs(K_2((b-d)/r))<<R+r<<R.              (3.7)
```

Thus the same-modulus row is `O(R^3)`.

Now let `s!=r`.  Extending the residue sums to their periodic integer
lifts, put

```text
A_s=sum_(c mod s)abs(K_1(a/r-c/s)),
B_s=sum_(d mod s)abs(K_2(b/r-d/s)).                  (3.8)
```

Because `rs asymp R^2`, (3.5) gives

```text
A_s
 <<R^2 sum_(t in Z)(1+abs(as-rt))^(-A).              (3.9)
```

Let

```text
delta_s=min_(t in Z)abs(as-rt).                      (3.10)
```

Successive `t` change `as-rt` by `r`, so

```text
A_s<<R^2{(1+delta_s)^(-A)+R^(-A)}.                   (3.11)
```

The condition `a!=0 mod r` is now decisive.  As `s` runs through the
integer interval `[R,2R]`, multiplication by `a` makes `as mod r` run
through distinct residues up to a bounded endpoint multiplicity.  Hence

```text
sum_(R<=s<=2R) (1+delta_s)^(-A)<<1,

sum_(R<=s<=2R) A_s<<R^2.                             (3.12)
```

No equidistribution of primes is used; the prime set is simply enlarged to
all integers in this upper bound.

For the short coordinate, again using `rs asymp R^2`,

```text
B_s
 <<R sum_(t in Z)(1+abs(bs-rt)/R)^(-A)
 <<R.                                                (3.13)
```

The last sum is bounded because its arguments are spaced by
`r/R asymp1`.  This remains valid when `b=0`.  Combining (3.12)--(3.13),

```text
sum_(s in mathcal P(R);s!=r)A_sB_s<<R^3.             (3.14)
```

Equations (3.7) and (3.14) give the required Schur row bound.  Duality
proves (3.1).  QED.

If `a=0`, then `delta_s=0` for every `s`, so (3.12) becomes `O(R^3)`
instead of `O(R^2)` before multiplication by `B_s`.  The row bound is then
`R^4`, exactly as the counterexample in Section 2 predicts.

## 4. Proof of the general energy inequality

Split (1.4) into `a!=0` and `a=0`.  Theorem 3.1 and `r asymp R` give

```text
sum_r r^(-2)sum_(a!=0,b)abs(Chat_r(a,b))^2
 <<R norm(C)_2^2.                                    (4.1)
```

For the zero slice, (1.6) gives

```text
Chat_r(0,b)=sum_Q D(Q)e_r(bQ).                       (4.2)
```

One-dimensional Parseval yields

```text
r^(-2)sum_(b mod r)abs(Chat_r(0,b))^2
 =r^(-1)sum_(q mod r)
   abs(sum_(Q=q mod r)D(Q))^2.                       (4.3)
```

The `Q` support has length `O(R)`, while `r asymp R`; every residue class
therefore has `O(1)` integer lifts.  Fiberwise Cauchy gives

```text
sum_(q mod r)abs(sum_(Q=q mod r)D(Q))^2
 <<norm(D)_2^2.                                      (4.4)
```

Since `#mathcal P(R)<=R`, summing (4.3) costs at most `O(norm(D)_2^2)`.
Together with (4.1), this proves (1.7).

## 5. Vieta-specific integer energies

Assume

```text
supp(z_i) subset [-C H,C H],
abs(z_i(0))<<H^(-1/2+epsilon)norm(z_i)_2.             (5.1)
```

Only the displayed point estimate, rather than the full supremum version,
is needed below.  Define `C` by (1.8)--(1.9).

### 5.1 Full two-coordinate energy

On `P!=0`, fixing the integer `P` fixes a nonzero four-factor product.
The number of ordered signed factorizations

```text
h_1h_2h_3h_4=P,             abs(h_i)<<H,             (5.2)
```

is `O(H^epsilon)` by the divisor bound.  Imposing `Q` can only reduce this
fiber.  Fiberwise Cauchy therefore gives

```text
sum_(P!=0,Q)abs(C(P,Q))^2<<H^epsilon Z^2.            (5.3)
```

For `P=0`, decompose into the fifteen disjoint strata specified by the
nonempty set of zero coordinates.  Consider first the stratum with exactly
`h_1=0`.  For `Q!=0`,

```text
Q=h_3(h_2+h_4).                                      (5.4)
```

There are `H^epsilon` choices of the divisor `h_3` and `O(H)` pairs with a
fixed sum, so the fiber has size `O(H^(1+epsilon))`.  The factor
`abs(z_1(0))^2` in (5.1) cancels this `H`.

At `Q=0`, a raw fiber count would be too large, but the coefficient
factorizes:

```text
z_1(0)
 (sum_(h_3!=0)z_3(h_3))
 (sum_(h_2!=0)z_2(h_2)z_4(-h_2)).                   (5.5)
```

Cauchy and (5.1) bound the square of (5.5) by `H^epsilon Z^2`.
The other one-zero strata are identical.

If two zeros lie in the same opposite pair, for example
`h_1=h_3=0`, then `Q=0` and the coefficient is

```text
z_1(0)z_3(0)(sum z_2)(sum z_4).                     (5.6)
```

The two point-flatness factors cancel the two `l^1/l^2` factors.  If the
two zeros lie in different opposite pairs, `Q` is the product of the two
remaining variables and the divisor bound applies.  Three- and four-zero
strata are smaller by the same estimates.  Since the number of strata is
fixed,

```text
sum_Q abs(C(0,Q))^2<<H^epsilon Z^2.                  (5.7)
```

Combining (5.3) and (5.7) proves the first estimate in (1.11).

### 5.2 The repeated-frequency marginal

Put

```text
A(x)=sum_(h_1+h_3=x)z_1(h_1)z_3(h_3),
B(y)=sum_(h_2+h_4=y)z_2(h_2)z_4(h_4).                (5.8)
```

Then the marginal (1.6) is exactly

```text
D(Q)=sum_(xy=Q)A(x)B(y).                             (5.9)
```

Fiberwise Cauchy for additive convolution gives

```text
norm(A)_2^2<<H norm(z_1)_2^2norm(z_3)_2^2,
norm(B)_2^2<<H norm(z_2)_2^2norm(z_4)_2^2.           (5.10)
```

For `Q!=0`, the integer product fiber `xy=Q` has `H^epsilon` elements, so

```text
sum_(Q!=0)abs(D(Q))^2
 <<H^epsilon norm(A)_2^2norm(B)_2^2
 <<H^(2+epsilon)Z^2.                                 (5.11)
```

At zero,

```text
D(0)=A(0)sum_y B(y)+B(0)sum_x A(x)-A(0)B(0).         (5.12)
```

Here `abs(A(0))` is at most
`norm(z_1)_2norm(z_3)_2`, while
`abs(sum_x A(x))=abs((sum z_1)(sum z_3))` is at most
`H norm(z_1)_2norm(z_3)_2`; similarly for `B`.  Thus

```text
abs(D(0))^2<<H^2Z^2.                                 (5.13)
```

Equations (5.11)--(5.13) prove the second estimate in (1.11).  Notice that
this marginal estimate does not need point flatness; flatness is needed only
for the `P=0` part of the full two-coordinate energy.

## 6. Divisor-switching interpretation

Expanding the left side of (1.12) before Fourier transformation gives

```text
sum_(h,h')W(h)conjugate(W(h'))
 # {r in mathcal P(R):
      r | P(h)-P(h'),
      r | Q(h)-Q(h')}.                               (6.1)
```

For a fixed nonzero difference `P(h)-P(h')`, only `O(1)` primes of size
`R=H^2` can divide it, because its height is `O(H^4)=O(R^2)`.  This
observation alone is useless after summing the `H^8` pairs.

The exact aliases

```text
P(h)=P(h'),             Q(h)=Q(h')                   (6.2)
```

contribute at most

```text
#mathcal P(R) norm(C)_2^2<<R H^epsilon Z^2.          (6.3)
```

Theorem 3.1 is the required weighted divisor switch for all remaining
aliases.  It combines the Farey permutation `as mod r` in the nonzero
`P` frequency with critical-length sampling in the `Q` frequency, rather
than counting the pairs individually.  The only part at which the
long-product congruence is absent is the additive frequency `a=0`; this is
exactly the `Q`-marginal handled by (5.9)--(5.13).  Thus both the exact and
nonexact product aliases are at the ideal average scale.  There is no
residual `H^8` term hidden in (1.12).

## 7. What the average buys in the untwisted R115 frame

Suppose a common-profile, untwisted R115 block has `L<=r` distinct
multipliers and coefficients satisfying

```text
sum_k abs(a_(r,k))^2<<L.                             (7.1)
```

R115's exact `(P,Q)` Gram matrix gives

```text
abs(T_r)^2<<r^2 L E_r(C).                            (7.2)
```

For unit-size outer weights, (1.12) and Cauchy in `r` imply

```text
abs(sum_(r in mathcal P(R))T_r)
 <<(sum_r E_r)^(1/2)(sum_r r^2L)^(1/2)
 <<R^2 sqrt(L) H^epsilon Z.                          (7.3)
```

The separated direct bound is

```text
<<R^2 L Z.                                           (7.4)
```

Thus the varying-prime coefficient energy supplies the relative factor

```text
L^(-1/2)H^epsilon.                                   (7.5)
```

At the former transition `L=H`, this is a genuine `H^(-1/2+epsilon)`
gain.  This is the precise sense in which averaging removes the fixed-`r`
Vieta loss.

The theorem also survives a projective common-profile decomposition

```text
C_r=sum_nu omega_nu(r)C_nu                           (7.6)
```

with the square of the projective norm
`(sum_nu sup_r abs(omega_nu(r)))^2`.  Hence the `H^o(1)` smooth
outer-prime separations proved in R111 do not spend the power in (7.5),
provided the block has first been reduced to common untwisted profiles.

## 8. Why the actual endpoint phase still stops at equality

For a translated Blomer--Pascadi interval, R116 proves that the odd packet
contains

```text
e_r(-s k x),                 x=h_1+h_3.              (8.1)
```

The common coefficient must then retain

```text
C(P,Q,x),                    abs(x)<<H.               (8.2)
```

The diagonal physical volume in a three-dimensional large sieve is

```text
(R^2)(R)(H)=R^3H.                                    (8.3)
```

Equivalently, R116's exact twisted Gram matrix has diagonal

```text
H r(r-2).                                            (8.4)
```

Even granting the ideal averaged enlarged energy

```text
sum_r sum_(P,Q,x)abs(C(P,Q,x))^2<<R H^epsilon Z^2,  (8.5)
```

the analogue of (7.3) is only

```text
<<R^2 sqrt(HL)H^epsilon Z.                           (8.6)
```

Relative to (7.4), this is

```text
sqrt(H/L)H^epsilon,                                  (8.7)
```

which has no fixed saving at `L=H`.  Applying the Schur proof in one more
coordinate gives exactly the same factor `H`; its diagonal term alone
prevents a better coefficient-uniform theorem.  Averaging the primes does
not make the endpoint coordinate free.

The anchored case `s=0` is the genuine exception and is covered by Section
7.  Generic translated boxes require an estimate which keeps the endpoint
and multiplier coefficients together before scalar Cauchy--Schwarz.  In
the notation of R116, the next theorem must control

```text
sum_(r,s,k)b_(r,s)(k)
 sum_h W_s(h)e_r(-s k[h_1+h_3])chi_r(D_h(k))         (8.8)
```

as a vector/square function in `(s,k)`, with a fixed gain over (8.6).
Separating each endpoint or each multiplier first recreates the diagonal
`H` in (8.3).

Finally, R105 still supplies a composite modulus with one full Fourier
support and one modular-inverse image, not the two native short intervals
to which (8.8) would apply.  Thus the rigorous ledger is

```text
generic R^3+N_1N_2 pair theorem             FALSE;
critical nonprincipal/nonzero-frequency part PROVED;
Vieta zero-frequency marginal                 IDEAL SCALE;
sum_(r~H^2) E_r for common native profiles    <<R H^epsilon Z^2;
untwisted R115 transition gain at L=H          H^(-1/2+epsilon);
translated endpoint phase                     BACK TO EQUALITY;
full R105 short-box lift                       OPEN;
fixed zero-free strip                          NOT PROVED.            (8.9)
```

The varying-prime Vieta average is therefore a real new cancellation
mechanism, but its useful continuation must be a joint endpoint--multiplier
square-function theorem or a direct unpartitioned R105 correlation, not a
stronger scalar collision estimate for `(P,Q)` alone.
