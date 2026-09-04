# QP high-completion tail: hostile audit of the restricted reciprocal-height gate

**Date:** 2026-08-22  
**Verdict:** no counterexample to

```text
W_K(z)=sum_(C:K<=m(C)<2K) w_z(C)
 <<D/K*q^o(1)*||z||_2^4                            (HC_K)
```

was found on the actual prime-power support.  The affine Hankel packet
saturates its exponent, while the known multilevel and recentered models
remain below it after their completions are merged.  The Farey model
saturates the proposed reciprocal-height scale but does not violate it and
does not satisfy the actual product-window mask.

There is, however, an important correction to the phrase "after coherent
planes are removed."  Bounding the multiplicity of each primitive
three-row relation is not sufficient by itself.  One must also bound how
many residual row vertices are used collectively by all high-codegree
partners of one anchor.  The exact theorem proved below is

```text
R_(gamma,K)<<M_(gamma,K)^(1/3)*Y_(gamma,K)^2*q^o(1), (0.1)
```

where `Y_(gamma,K)` is the number of residual row vertices participating
in the restricted high-`K` triples and `M_(gamma,K)` is the largest number
of those triples having the same primitive relation vector.  Consequently,
if

```text
Y_(gamma,K)<=J*K,       M_(gamma,K)<=M,             (0.2)
```

then the factorial-triangle reduction gives the honest packet-subtracted
tail

```text
W_(K,res)(z)
 <<D/K*M^(1/3)*J^2*q^o(1)*||z||_2^4.              (0.3)
```

Thus the desired `D/K` follows when `M^(1/3)J^2=q^o(1)`.  A packet merger
naturally attacks `M`; it does not automatically prove `J=q^o(1)`.  This
is the weakest currently proved completion of `(SRH_K)` which is stable
under an explicit packet subtraction.

Without (0.2), the best unconditional consequence of the new uniform
fourth-trace theorem remains

```text
W_K(z)<<min(D,D^(5/4)/K)*q^o(1)*||z||_2^4.        (0.4)
```

The missing factor at the critical scattered endpoint is still `D^(1/4)`.

## 1. Precise packet-subtracted formulation

There is a subtle compatibility requirement.  An arbitrary assignment of
individual color-matrix completions to packets is additive in the direct
positive sum, but its residual multiplicities need not be codegrees of one
binary matrix.  The factorial identities would then be unavailable.

For the argument below, packet subtraction must occur at the incidence-edge
level.  Write

```text
B=B_packet union B_res                                  (1.1)
```

for the binary row-pair/color-pair incidence, and let

```text
r(gamma,gamma')
 =|N_(B_res)(gamma) intersect N_(B_res)(gamma')|.       (1.2)
```

The correct residual tail is

```text
W_(K,res)(z)
 =sum_(gamma!=gamma':K<=r(gamma,gamma')<2K)
      u_gamma*u_gamma'.                                (1.3)
```

Deleting incidence edges also creates packet--residual mixed completions:

```text
m_B(gamma,gamma')
 !=m_(B_packet)(gamma,gamma')+m_(B_res)(gamma,gamma')  (1.4)
```

in general.  A complete packet proof must bound the packet block and these
mixed terms separately (or recombine the packet and residual matrices by an
`S_4` triangle inequality).  Formula (0.3) is an honest theorem for the
binary residual block; by itself it is not a decomposition of the original
`W_K`.

It is also illegitimate to delete some triples from a factorial moment while
continuing to select partners using the original `m(C)`: deletion can move a
pair to a different dyadic bin.  Every codegree and every set below refers
to the single residual incidence `B_res` in (1.1).

For one residual color-pair anchor `gamma`, let

```text
X_(gamma,K)
 ={row triples X contained in gamma and in some gamma'
   with K<=r(gamma,gamma')<2K}.                    (1.4)
```

Let `Y_(gamma,K)` be the union of the row vertices occurring in these
triples.  For

```text
h(X)=primitive((a_1,a_2,a_3) cross (A_1,A_2,A_3)),
H(X)=||h(X)||_infinity,                            (1.5)
```

define

```text
M_(gamma,K)=max_h #{X in X_(gamma,K):h(X)=h},
R_(gamma,K)=sum_(X in X_(gamma,K))1/H(X).          (1.6)
```

The earlier `K_(3,2)` elimination and factorial Schur bound, applied to
`B_res`, give exactly

```text
W_(K,res)(z)
 <<D/K^3*max_gamma R_(gamma,K)*q^o(1)*||z||_2^4.  (1.7)
```

## 2. Primitive-relation capacity theorem

Let `T=#X_(gamma,K)`, `Y=Y_(gamma,K)`, and `M=M_(gamma,K)`.  Plainly

```text
T<=binom(Y,3)<<Y^3.                                (2.1)
```

There are `O(H^3)` primitive integer vectors in the dyadic box

```text
H<=||h||_infinity<2H.                              (2.2)
```

Every such vector supports at most `M` triples.  The contribution of this
height block to `R_(gamma,K)` is therefore

```text
<<min(T/H,M*H^2).                                  (2.3)
```

Split at `H_0=(T/M)^(1/3)`.  Both geometric dyadic sums are dominated by
their endpoint and give

```text
R_(gamma,K)<<M^(1/3)*T^(2/3)q^o(1)
             <<M^(1/3)*Y^2*q^o(1).                (2.4)
```

This proves (0.1).  Substitution of `Y<=J*K` into (1.7) proves (0.3).
In particular, if one anchor has at most `P` residual high-`K` partners,
then `Y<=2K*P`, so

```text
W_(K,res)(z)<<D/K*M^(1/3)*P^2*q^o(1)||z||_2^4.   (2.4a)
```

Thus subpower relation multiplicity and a subpower number of high partners
already prove the sharp residual tail.  This restricted range includes all
finite actual fixtures found below.

In power notation

```text
K=D^k,       Y=D^y,       M=D^mu,                  (2.5)
```

the resulting tail exponent is

```text
1+mu/3+2y-3k.                                      (2.6)
```

The desired exponent is `1-k`, so the exact restricted closure condition is

```text
mu/3+2*(y-k)<=0.                                   (2.7)
```

At the critical `k=5/16`, this is

```text
2y+mu/3<=5/8.                                      (2.8)
```

After a subpower relation-packet merger (`mu=0`), one still needs
`Y<=K*q^o(1)`.  This is the residual partner-union theorem missing from the
current argument.

## 3. Why plane subtraction alone is insufficient

The loss in (0.3) is real at the level of the known inequalities.  Take an
anchor with a residual row reservoir of size `Y=J*K`.  A family of
`K`-subsets can cover all its row triples using `O(J^3 log Y)` partners;
declare each subset to be the common neighborhood of one partner.  As a
formal height model, inject the retained triples into the `asymp Y^3`
primitive integer vectors of height `O(Y)`.  It obeys `H<=D` when `Y<=D`,
has no repeated relation label, and the capacity in (2.4) is of order

```text
Y^2=J^2*K^2.                                       (3.1)
```

This is a formal binary-incidence/integer-label countermodel to deriving
`R_K<<K^2` from the codegree and height inequalities alone.  It respects
the pointwise three-row estimate whenever `H<=D`, but it is not claimed that
the assigned vectors are cross products of one common row set.  In
particular it is **not** an actual QP construction: the partners were
prescribed combinatorially and need not be simultaneously realized by
prime-power carriers and colors in the product window.

Thus actual arithmetic must rule out a polynomially large union of
essentially disjoint high-codegree partners, not merely merge translations
having one repeated primitive relation.

## 4. Known hostile constructions

### 4.1 One affine Hankel packet is sharp

Take an `L`-by-`L` additive Hankel grid with `D~L^2` and flat normalized
weights on its `O(L)` colors.  For a positive proportion of its color
matrices,

```text
m(C)~L,        # such C~L^3,       w_z(C)~L^(-2).
```

Therefore

```text
W_L(z)~L=D/L.                                      (4.1)
```

This proves that neither the exponent of `K` nor the exponent of `D` in
`(HC_K)` can be improved in the integer packet model.  Its repeated
second-difference relations are exactly what the packet merger removes.

### 4.2 The multilevel tangent model does not refute the tail

In the known multilevel fixture, `D=L^2`, there are `asymp L^2` displayed
color clusters with `m(C)~L`, and the spiked color vector has
`w_z(C)~L^(-3/2)`.  Hence its displayed high tail is

```text
W_L(z)~L^(1/2)=D^(1/4)<<D/L=D^(1/2).              (4.2)
```

Its `D^(5/4)` quantity is the pair-of-completions energy
`sum m(C)(m(C)-1)w_z(C)`, not `W_K` and not the direct form.  The whole
cross-level patch has direct mass `O(D)` after Hankel merger.

### 4.3 Farey matching saturates `SRH`, but is not actual

For the existing Farey volume-plane fixture, an order-`N` matching has
`K~N^2` completions.  Direct enumeration gives the following values; the
last column deletes every primitive relation vector occurring more than
once.

| order `N` | `K` | raw `R/K^2` | unique-relation `R/K^2` |
|---:|---:|---:|---:|
| 12 | 22 | .330 | .089 |
| 20 | 62 | .394 | .101 |
| 30 | 138 | .439 | .094 |
| 48 | 354 | .574 | .098 |

Thus the exponent `K^2` in `(SRH_K)` is sharp even after the most aggressive
literal deletion of repeated relation labels.  The fixture has four
pairwise-coprime prime-power colors, but its row and carrier coordinates are
not shell prime powers and do not satisfy the QP product window.  It is a
method barrier, not a counterexample to `(HC_K)`.

## 5. Actual-prime finite audit

Generic all-eight-distinct rectangles were enumerated with the exact
prime-power shell and smooth cutoff.  The table reports the maximum raw
`R_(gamma,K)/K^2`; repeated primitive relations were absent at the maximizing
anchors.

| `q` | cutoff | maximum generic `m(C)` | maximum scanned `R/K^2` |
|---:|---:|---:|---:|
| 25,013 | 40 | 4 | .00962 |
| 50,021 | 40 | 4 | .03572 |
| 100,003 | 40 | 4 | .00136 |
| 200,003 | 24 | 2 | 0 |

The first genuine scattered fixture occurs already at `q=25,013`.  One
oriented color matrix is

```text
C=(13103,12659;10799,10433),        det C=-942,     (5.1)
```

with the four completions

```text
(10903,13229,13693,14173),
(11483,13933,13001,13457),
(11681,14173,12781,13229),
(11743,14249,12713,13159).                          (5.2)
```

They have affine rank three in `Z^4`; hence no affine line contains three
of them.  Their four row triples have distinct primitive relation vectors
and heights

```text
215, 301, 482, 725.                                (5.3)
```

Consequently their reciprocal-height mass is

```text
1/215+1/301+1/482+1/725=.0114274...<<4^2.         (5.4)
```

This proves on the actual mask that "four completions imply one dominant
tangent line" is false.  It does not threaten `(SRH_K)`.

Projected positive-quartic searches on the same scans also found

```text
max K*W_K/D_geometric <3.8*10^(-5).                (5.5)
```

These finite values are diagnostics only; bounded observed multiplicity is
not an asymptotic theorem.

## 6. Exact unconditional and conditional status

The new uniform direct theorem gives

```text
K*W_K(z)<=sum_C m(C)w_z(C)
          <<D^(5/4)q^o(1)||z||_2^4.               (6.1)
```

The determinant-band mass bound independently gives `W_K<<Dq^o`.  Together
they prove (0.4).  The dominant-line theorem gives the sharp `D/K` on every
fiber with a `K*q^(-o(1))` line, and the occupied-line curvature theorem
gives `D*sqrt(J)/K` when at most `J` lines are present above the baseline.

For the genuinely scattered packet-subtracted remainder, (0.3) is now the
sharpest proved structural statement:

```text
dominant/rich coherent packet tail D/K:             PROVED;
primitive-relation capacity R<=M^(1/3)Y^2:          PROVED;
residual tail D*M^(1/3)J^2/K:                       PROVED;
subpower relation multiplicity after assignment:   A PACKET HYPOTHESIS;
residual partner union Y<=K*q^o:                    OPEN;
actual finite counterexample to SRH_K or HC_K:       NONE FOUND;
integer Farey violation of the K^2 exponent:         NO (IT SATURATES);
uniform HC_K and literal four-cycle bound:           OPEN.
```

The distinction is decisive: an actual proof must establish both a
relation-packet merger and a Bessel/union estimate across the remaining
partners.  Either one without the other leaves a polynomial loss.
