# `OD2` tensor trace: an actual low-slope theorem and the rational-carrier wall

**Date:** 2026-08-13
**Verdict:** a nonempty part of the actual bands-first/common-height `OD2`
gate is proved at the required `Y^(1+.1594+o(1))` scale.  The proof is
deterministic and uses the affine exactness of the two endpoint-Voronoi
quadratures.  It covers only a near-integer derivative wedge.  Grouping by a
general selected rational `a/q` does not extend the argument: the frozen
rational Fourier coefficient survives, and the universal residue estimate
misses by a full block factor `H`.  The complementary actual-SPF sector
remains open.

The polarity is an **upper covariance bound in one sector of the dual
antenna gate**.  It supplies neither a candidate-relative positive reserve
nor the global Pick transfer, and it does not close the complementary `OD2`
sector.  Therefore it does not promote the zero-free-strip route.

## 1. Exact object and retained inputs

Fix one common height `t`.  On a curvature block `I` centered at `x_I`, write

```text
H_I asyp Y/sqrt(t),       G=Y^(797/5000+o(1)),       G<=H_I.
```

After including the unique crossing band and summing every SPF band before
squaring, the interior measure is exactly

```text
nu_Prime-nu_(q_I).                                      (1.1)
```

Both are endpoint-trapezoid measures on nested integer node sets with the
same shell barriers.  The `q_I`-rough set contains all shell primes, so its
mesh is no larger than the prime mesh.  After the audited long-terminal-edge
deletion, both meshes are at most `G`.

Let

```text
F_I(x)=A_I(x) exp(i t log x),                           (1.2)
```

where `A_I` includes the actual curvature taper and smooth nonoscillatory
amplitude.  In the smooth version,

```text
|A_I^(j)(x)| << H_I^(-j),       j=0,1,2.               (1.3)
```

The usual tent version is piecewise of this class with `O(1)` corners.  The
literal coefficient also has the already audited block/crossing-edge
transport `E_(partial,I)`, with

```text
|E_(partial,I)|<<G.                                    (1.4)
```

Thus

```text
B_I(t)=(nu_Prime-nu_(q_I))(F_I)+E_(partial,I).          (1.5)
```

Equations (1.1)--(1.5), including (1.4), are the precise interface used
below.  No rational phase is substituted for the logarithm.

## 2. Bond dimension four is exact, but has no spectral gap

For a survivor bit `b`, the first-return transition is

```text
M(b) = ((1-b,0),(1,1)).                                (2.1)
```

For two shifted configurations the gap product is the `S tensor S`
coordinate of

```text
A(b,c)=M(b) tensor M(c),                               (2.2)
```

so the paired first-return law has exact bond dimension four.  On the paired
empty symbol put `A_00=A(0,0)`.  If `N=A_00-I`, direct multiplication gives

```text
N^2 !=0,             N^3=0,                            (2.3)

A_00^r(1,0,0,0)^T=(1,r,r,r^2)^T.                      (2.4)
```

The covariance coordinate is exactly the quadratic Jordan transient.  A
matrix large sieve which takes an operator, Hilbert--Schmidt, or state norm
before using the divisibility law therefore pays the paired gap energy; the
constant dimension alone supplies no cancellation.  This is a fail-fast
statement about norm/spectral-gap transfers, not a no-go theorem for a
matrix-valued dispersion argument that keeps the signed trace and actual SPF
inputs.

## 3. Deterministic trapezoid theorem

For a partition `S={s_j}` define

```text
Q_S(F)=sum_j (s_(j+1)-s_j)
              [F(s_j)+F(s_(j+1))]/2.                  (3.1)
```

If the mesh is at most `G`, the elementary trapezoid remainder on each edge
gives

```text
|Q_S(F)-integral F|
 <=(1/12)||F''||_infty sum_j (s_(j+1)-s_j)^3.          (3.2)
```

Only edges meeting the support of `F_I` occur.  Their total length is
`O(H_I+G)=O(H_I)`, and hence two partitions of mesh at most `G` satisfy

```text
|Q_S(F_I)-Q_R(F_I)| << H_I G^2 ||F_I''||_infty.       (3.3)
```

This is just the analytic form of the exact facts that an endpoint-Voronoi
measure integrates affine functions exactly and that the difference of two
such measures has zero mass and first moment.

Now put

```text
u_I=||t/(2 pi x_I)||,                                  (3.4)
```

and choose the nearest integer `k_I`.  Multiplication by
`exp(-2 pi i k_I n)` changes nothing at integer nodes.  For

```text
psi_I(x)=t log x-2 pi k_I x
```

on the support of `I`, curvature gives

```text
|psi_I'(x)| <<u_I+H_I^(-1),
|psi_I''(x)|<<H_I^(-2).                                (3.5)
```

Equations (1.3) and (3.5) imply

```text
||F_I''||_infty <<(u_I+H_I^(-1))^2.                   (3.6)
```

For a tent taper, insert each of its `O(1)` corners into both partitions,
apply (3.3) on the smooth pieces, and then remove the inserted nodes.  A
single insertion changes an endpoint-trapezoid measure by a three-atom event
of total variation at most `G`, so all tent corners cost only `O(G)`.  The
same charge covers (1.4).  We obtain the actual block estimate

```text
|B_I(t)|
 <<H_I G^2 (u_I+H_I^(-1))^2+G.                        (3.7)
```

This bound includes the exact logarithmic phase, smooth or tent taper, the
bands-first crossing collapse, and block-boundary transport.

## 4. The proved low-integer-slope sector

There is a useful actual-prime improvement over applying (3.7) block by
block.  The proved retained third-gap moment is

```text
d_3=1173/65000=.0180461538...,

sum_(retained prime gaps) g^3
 <<Y^(1+2 theta-d_3+o(1)),       theta=797/5000.       (4.1)
```

Every `q_I`-rough partition refines the prime partition.  Splitting an edge
can only decrease the sum of cubes, so the same bound applies to its gap
cube ledger.  If `C_I` is the sum of both cube ledgers meeting the support
of `I`, bounded block overlap and the mesh cutoff give

```text
sum_I C_I <<Y G^2 Y^(-d_3+o(1)),
max_I C_I <<H G^2                                     (4.2)
```

on an `H`-regime.  The uncompressed form of the trapezoid remainder is

```text
|B_(I,interior)(t)| <<(u_I+H^(-1))^2 C_I.             (4.3)
```

Define the sharpened threshold

```text
eta_H=Y^(d_3/4)(H G^3)^(-1/4).                        (4.4)
```

Since `G<=H`, one has `H^(-1)<=eta_H`.  If

```text
u_I<=eta_H,                                            (LS)
```

then (4.2)--(4.4) give

```text
sum_(I satisfying LS)|B_(I,interior)(t)|^2
 <<eta_H^4 (max_I C_I) sum_I C_I
 <<[Y^d_3/(H G^3)] [H G^2] [Y G^2 Y^(-d_3)]
 <<Y G Y^o(1).                                        (4.5)
```

Every boundary/tent charge is `O(G)`.  Since `G<=H` and there are
`O(Y/H)` blocks in the regime, their squared aggregate is also
`O(YG)`.  Mixed terms are absorbed by `|x+y|^2<=2|x|^2+2|y|^2`.  Therefore

```text
sum_(I satisfying LS) |B_I(t)|^2
 <<Y G Y^o(1)=Y^(1+797/5000+o(1)).                    (4.6)
```

Thus the full covariance, and therefore its signed off-diagonal part, is at
the required `OD2` scale on this sector.  This is an actual theorem for the
prime-versus-`q_I`-rough transport; it does not use an abstract node model or
an average over `t`.  Using only the mesh and total mass would give
`(HG^3)^(-1/4)`; the actual third-gap theorem enlarges the wedge by the
factor `Y^(d_3/4)`.

### 4.1 Exactly what selector space is new

Write `H_I=Y^(h+o(1))` and `G=Y^(theta+o(1))`, with

```text
theta=797/5000=.1594.
```

Then

```text
eta_H=Y^(-gamma(h)+o(1)),
gamma(h)=(h+3 theta-d_3)/4.                           (4.7)
```

At the shallow endpoint,

```text
gamma(8/33)=150703/858000=.1756445221...,              (4.8)
```

strictly beyond the old denominator exponent `.1537`.  Retained minor arcs
also have `u_I>1/H_I`, so the genuinely new physical wedge is

```text
H_I^(-1)<u_I<=Y^(d_3/4)(H_I G^3)^(-1/4).              (4.9)
```

If the selected approximation is

```text
t/(2 pi x_I)=integer+a_I/q_I+epsilon_I,
|epsilon_I|<=1/(q_I H_I),                             (4.10)
```

then a sufficient selected-data version of `(LS)` is

```text
min(a_I,q_I-a_I)/q_I+1/(q_I H_I)<=eta_H.              (4.11)
```

Since the reduced numerator is nonzero, (4.9) forces
`q_I>=Y^(gamma(h)-o(1))`.  Under the imposed cap
`q_I<=min(H_I,Y^(33/133))`, this wedge is nonempty only when

```text
h<=4(33/133)-3(797/5000)+1173/65000
 =460197/864500=.5323273569....                        (4.12)
```

For

```text
8/33<=h<=.532327356...,
```

the newly covered selected wedge has denominator exponents

```text
gamma(h)<=b<=min(h,33/133)                            (4.13)
```

and endpoint numerators

```text
min(a_I,q_I-a_I) <<q_I Y^(-gamma(h)).                 (4.14)
```

This describes a geometric wedge; it does not assert that a positive
proportion of actual blocks lies in it.  For `h>.532327356...`, the wedge is
incompatible with the capped selected denominator and (4.4) adds no block.

## 5. Why rational detrending fails

It is tempting to replace `u_I` in (3.7) by the much smaller residual
`|epsilon_I|` in (4.8).  This is invalid: unlike an integer carrier,
`exp(-2 pi i a_I n/q_I)` is not one on integer nodes.

Group the exact coefficient by residues,

```text
D_I(r)=sum_(n == r mod q_I) d_(I,t)(n).                (5.1)
```

Freezing the residual phase leaves the main term

```text
hat D_I(a_I)=sum_(r mod q_I)e_(q_I)(a_I r)D_I(r),     (5.2)
```

which is precisely the unresolved selected rough-Voronoi Fourier
coefficient.  Residual smoothness only controls the error around (5.2).

The exact coefficient-blind residue ledger is

```text
|hat D_I(a_I)|^2
 <=q_I sum_r |D_I(r)|^2
 <=q_I(ceil(H_I/q_I)+O(1)) sum_n|d_(I,t)(n)|^2
 <<H_I sum_n|d_(I,t)(n)|^2,                           (5.3)
```

because `q_I<=H_I`.  The first inequality costs `q_I`; the `H_I/q_I`
occupancy cancels it.  With the proved global diagonal

```text
sum_(I,n)|d_(I,t)(n)|^2<<Y G Y^o(1),                  (5.4)
```

(5.3) gives only `Y H G` on an `H`-regime, a full factor `H` above `OD2`.
Thus residue grouping does not extend (4.4) beyond the near-integer wedge.
Any successful rational extension must estimate (5.2) arithmetically; bond
dimension four and the Dirichlet residual do not do so.

## 6. Primary-literature boundary for automatic/matrix weights

The following primary papers are the closest located inputs.

1. [Mauduit--Rivat, *Sur un probleme de Gelfond: la somme des chiffres des
   nombres premiers*](https://doi.org/10.4007/annals.2010.171.1591) proves
   equidistribution of fixed-base digit-sum weights along primes.  Its digital
   carry structure is a fixed radix recursion, not a local SPF survivor word.

2. [Mullner, *Automatic sequences fulfill the Sarnak
   conjecture*](https://arxiv.org/abs/1602.03042) proves a prime number theorem
   for an appropriate strongly connected fixed automaton.  The output is a
   fixed automatic sequence read from the base expansion of `n`; it is not a
   cutoff- and shift-dependent pair of first-return configurations.

3. [Drappeau--Mullner, *Exponential sums with automatic
   sequences*](https://arxiv.org/abs/1710.01091) obtains cancellation against
   rational-fraction exponentials in the Polya--Vinogradov range by reducing
   to two-point correlations of a fixed automatic sequence.  It assumes the
   correlation input which is exactly missing here and does not supply prime
   or semiprime short-block covariance for (2.2).

4. [Byszewski--Konieczny--Mullner, *Gowers norms for automatic
   sequences*](https://arxiv.org/abs/2002.09509) decomposes fixed automatic
   sequences into structured and Gowers-uniform parts.  The present cocycle
   reads `Y^.1594` physical SPF bits, has the neutral Jordan tower (2.3), and
   changes with the cutoff, shift, and block.  It is not an instance of their
   fixed digit automaton.

5. [Drmota--Mullner--Spiegelhofer, *Primes as sums of Fibonacci
   numbers*](https://arxiv.org/abs/2109.04068) proves level of distribution one
   for a fixed Fibonacci digit weight and then treats Type I/II sums.  This is
   strong evidence that a matrix representation becomes useful only after a
   weight-specific carry/correlation theorem; it provides no such theorem for
   overlapping least-prime-factor words.

The survey found no primary theorem for a polynomial-length, unbounded
first-return matrix output inside pointwise short semiprime sums, nor a
short-shift theorem accepting the paired SPF cocycle (2.2).  The distinction
is structural: the input here is the local divisibility environment
`rho_p(n+j)`, not the digits of `n`, and the covariance coordinate grows as
`r^2` on an empty word.  Calling it “automatic” does not import the digital
prime theorems.

## 7. New exact successor

The remaining target can now exclude the proved sector:

```text
sup_(legal t) sum_(I: ||t/(2 pi x_I)||>eta_(H_I))
 |B_I(t)|^2 <<Y^(1+797/5000+o(1)),

eta_(H_I)=Y^[(1173/65000)/4]
          [H_I Y^(3*797/5000)]^(-1/4),                (7.1)
```

with only blocks compatible with the selected high-denominator cap retained.
Any continuation through a rational carrier must bound the frozen arithmetic
term (5.2), preferably by retaining cancellation among the prime-prime,
prime-rough, and rough-rough tensor traces.  Estimating only the residual
chirp repeats the false step isolated in Section 5.

## 8. Truth boundary and reproduction

```text
paired first-return bond dimension four:             EXACT
empty-pair Jordan length three / r^2 state:          EXACT
actual low-integer-slope covariance (4.6):           PROVED
boundary, crossing band, smooth/tent taper:          INCLUDED
rational residual may replace integer slope:         FALSE
automatic-sequence literature proves remaining OD2:  NO
actual complementary SPF OD2:                        OPEN
candidate-relative reserve / global Pick transfer:   NOT ADDRESSED
zero-free strip:                                     NOT PROVED
```

```bash
PYTHONPATH=src python3 -m unittest -v \
  src/test_od2_tensor_trace_gate.py
python3 results/verify_zeta23_od2_tensor_trace_gate.py
```

The executable certificate checks the four-state tensor product, its exact
Jordan nilpotency and quadratic state, affine quadrature exactness, the sharp
single-edge trapezoid constant, every selector-wedge fraction, the sharpened
threshold monomial
`[Y^d/(HG^3)] [HG^2] [YG^2Y^(-d)]=YG`, and the
`q * ceil(H/q)` rational-grouping loss.  It does not assert (7.1).
