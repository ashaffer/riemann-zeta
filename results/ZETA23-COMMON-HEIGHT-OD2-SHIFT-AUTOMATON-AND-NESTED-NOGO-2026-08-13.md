# Common-height `OD2`: exact shift/Type decomposition and nested-node no-go

**Date:** 2026-08-13  
**Verdict:** `OD2` remains open for the actual SPF rough-to-prime transport.
The exact object is a signed short-shift correlation of a tensor-square
first-return automaton.  A coefficient-blind theorem based only on one common
height, nested Voronoi measures, tiny gaps, tapering, and the automaton is
false by a common-log countermodel.  Actual multiplicative/SPF structure is
therefore indispensable.

No post-`q` tail estimate and no zero-free strip is proved here.

## 1. Bands first: the exact physical coefficient

Fix one legal common height `t` and one curvature block `I`.  The selected
reduced fraction is `a_I(t)/q_I(t)`.  Recombine every SPF band before taking a
square.  The unique band with

```text
P<q_I<=2P
```

is `nu_(2P)-nu_(q_I)`; all complete later bands telescope.  Once the terminal
cutoff exceeds `sqrt(2Y)`, the interior identity is simply

```text
sum_P [nu_(max(2P,q_I))-nu_(max(P,q_I))]
  =nu_Prime-nu_(q_I).                                  (1.1)
```

Prime shell barriers and the already specified crossing-edge transport are
understood on both sides.  In particular, the crossing band is not a new
error term and must not be estimated separately after squaring.

For a finite survivor set `S`, write

```text
v_S(n)=1_S(n)[g_S^-(n)+g_S^+(n)]/2,                  (1.2)
```

where `g_S^+`, `g_S^-` are the distances to the next and previous survivor.
Let

```text
rho_q(n)=1_(P^-(n)>q),
c_q(n)=v_Prime(n)-v_(rho_q)(n).                       (1.3)
```

Away from the audited boundary atoms, the full physical coefficient is

```text
d_(I,t)(n)=W_(I,t)(n)c_(q_I(t))(n),                  (1.4)
```

where, in the physical representation used below, `W` contains the taper and
smooth nonoscillatory amplitude.  In the equivalent rational-carrier
representation, the carrier and residual chirp must multiply back to the
same exact `exp(i t log n)`; they may not be counted twice.  If `e_I` denotes
the boundary/crossing-edge transport, the literal identity is `d=Wc+e_I`.
Every occurrence of `d` below includes `e_I`; proving only the `Wc-Wc` term
is not `OD2`.

The bands-first coefficient is

```text
B_I(t)=sum_n d_(I,t)(n) exp(i t log n).               (1.5)
```

Thus `q_I` still matters arithmetically through the rough endpoint measure,
even though the dyadic labels have disappeared from (1.5).

## 2. Exact positive-shift form

Put `m=n+r` in the off-diagonal part of `|B_I|^2`.  With no approximation to
the logarithm,

```text
OD2(t)
 =2 Re sum_I sum_(r>=1) sum_(n,n+r in supp I)
    d_(I,t)(n) conjugate(d_(I,t)(n+r))
    exp(-i t log(1+r/n)).                              (2.1)
```

The taper restricts `r<<H_I`.  Formula (2.1) is one-sided and signed.  An
absolute value over `r`, the blocks, or the four prime/rough pieces is a
strictly stronger assertion and loses the only visible cancellation.

The exact remaining theorem is

```text
sup_(legal t) OD2(t) <<Y^(1+theta+o(1)),
theta=797/5000=.1594.                                  (OD2)
```

Together with the proved diagonal bound, this gives the common-height `CH4`
estimate with every fixed

```text
0<delta<(8/33-4*kappa-theta)/4=.001015578... .         (2.2)
```

At the shallow endpoint the coefficient-blind scale is `Y^(1+h)`.  Hence a
proof must gain at least

```text
h-theta >=8/33-797/5000
        =13699/165000=.0830242424... .                 (2.3)
```

This is a fixed power; an arbitrary logarithmic saving does not suffice.

## 3. Exact least-prime-factor deletion form

The q-first and ordinary flows agree at every prime stage `p>q_I`.  Just
before deleting an integer

```text
x=p m,                 P^-(m)>=p,                    (3.1)
```

let its active neighbors be `x-ell` and `x+r`.  Direct subtraction of the
two endpoint-trapezoid measures gives the exact three-atom event

```text
tau_(p,m)
 =(r/2) delta_(x-ell)
  -((ell+r)/2) delta_x
  +(ell/2) delta_(x+r).                               (3.2)
```

It has zero mass and zero first moment.  Summing (3.2) in any legal deletion
order gives exactly `nu_Prime-nu_q`; no square root of the number of stages
and no extra band multiplicity occurs.

Set `F_I(n)=W_(I,t)(n)exp(i t log n)` and

```text
E_(I;p,m)
 =1/2 [r F_I(pm-ell)-(ell+r)F_I(pm)+ell F_I(pm+r)].   (3.3)
```

If `E_(partial,I)` is the specified crossing-edge/block-boundary transport,
then

```text
B_I(t)=E_(partial,I)
       +sum_(p>q_I) sum_(m:P^-(m)>=p) E_(I;p,m),      (3.4)

sum_I |B_I(t)-E_(partial,I)|^2
 =sum_I sum_(p,m) sum_(p',m')
      E_(I;p,m) conjugate(E_(I;p',m')).               (3.5)
```

Expanding the three atoms in (3.5) produces nine shifted equations

```text
p'm'-pm =s+epsilon-epsilon',                          (3.6)
```

where `|s|<<H_I` and each endpoint offset is one of the appropriate
`{-ell,0,r}`.  This is the exact interior Type-I/II interface.  The mixed
and pure boundary terms from (3.4) must be restored before claiming `OD2`.

For `p=Y^u`:

* `u>1/3` forces `m` to be prime, up to endpoint constants;
* `1/4<u<=1/3` leaves at most two prime factors in `m`;
* `q_I<p<=Y^(1/4)` is the genuinely long-cofactor Type-I range.

Even in the late prime-prime range, however, `ell` and `r` are not separated
coefficients of `p` and `m`.  They are first-return functionals of the whole
local `p`-rough configuration.  In (3.5) two such configurations, generally
at different cutoffs `p,p'`, overlap.  Replacing them by arbitrary bounded
one-variable factors invokes the already proved thin-fibre counterexample,
not a valid reduction.

## 4. The covariance automaton has bond dimension four

For survivor bits `b_j`, put

```text
M(b)=((1-b,0),(1,1)).                                 (4.1)
```

Acting on `(P,S)=(1,0)`, the ordered product updates

```text
P <- (1-b_j)P,       S <- S+P_old.                   (4.2)
```

After the first survivor, `S` is exactly its distance from the origin.  This
is the previously audited two-state/Jordan first-return automaton.

The product of two gap weights in (2.1) or (3.5) is represented exactly by

```text
M(b_j) tensor M(b'_j),                               (4.3)
```

a four-state automaton whose `S tensor S` coordinate is the paired gap
product.  Equation (4.3) is an exact compression, but not a separation: the
two bit words overlap after the shift and are generated by two SPF cutoffs.
A scalar Type-II theorem for `alpha_p beta_m` does not accept (4.3).

Truncation at the retained edge length still requires words as long as

```text
G=Y^(theta+o(1)).                                     (4.4)
```

Thus fixed-complexity nilsequence or fixed-`k` shifted-sieve estimates cannot
be applied merely by citing the constant matrix dimension; the product
length grows polynomially.

## 5. Rigorous structural no-go

### 5.1 Exact periodic finite model

On `[0,kq]`, let the fine nodes be every integer and the coarse nodes be the
multiples of `q`.  For primitive `a mod q`, put

```text
d=nu_coarse-nu_fine,       z(n)=e_q(a n).             (5.1)
```

Both the total mass and first moment of `d` vanish.  On every length-`q`
cell the coarse trapezoid applied to `z` equals `q`, while the fine unit-mesh
trapezoid equals zero.  Consequently

```text
sum_n d(n)z(n)=kq.                                    (5.2)
```

The positive off-diagonal therefore rebuilds the square of the full block
mass.  This model is nested, integral, has exact deletion atoms, and is
computed by the same first-return automaton.  It is not an SPF set.

### 5.2 Exact common-log upgrade

The local discrepancy lemma already proved in
`ZETA23-LOG-CURVATURE-TRAPEZOID-TRANSITION-AND-INTEGER-NOGO-2026-08-13.md`
applies simultaneously to two fixed phase arcs.  At

```text
t=Y^(50/33),                 H=Y^(8/33),              (5.3)
```

outside a set of `o(Y)` physical length, every interval of length
`C log Y` contains integers with `exp(i t log n)` in a small arc around `+1`
and in a small arc around `-1`.

Choose coarse endpoints from the `+1` arc with gaps `asymp log Y`, and insert
one fine node from the `-1` arc inside every coarse gap.  On a gap of length
`g`, with ideal phases `(+1,-1,+1)`, the coarse-minus-fine trapezoid is
exactly

```text
g/2(1+1)
 -[ell/2(1-1)+r/2(-1+1)] =g.                         (5.4)
```

Small fixed phase arcs and the variation of the legal taper over
`O(log Y)` preserve a fixed positive proportion of (5.4).  The optimized
low-denominator deletion removes only `o(Y)` total cell mass; block barriers
cost `O((Y/H)log Y)=o(Y)`.  Hence, summing the real parts first and then using
Cauchy over `asymp Y/H` blocks,

```text
sum_I |B_I(t)|^2 >>Y H.                               (5.5)
```

All node gaps are `O(log Y)`, so the physical diagonal is only

```text
sum_(I,n)|d_I(n)|^2 <<Y log Y.                        (5.6)
```

It follows that the signed off-diagonal itself is `>>YH`.  At (5.3) this is

```text
Y^(1+8/33-o(1)),                                     (5.7)
```

which exceeds the `OD2` allowance by the exact exponent (2.3).

This is a rigorous no-go for the implication

```text
one exact common logarithmic height
+ high-denominator/low-q geometric deletion
+ nested integral Voronoi measures with O(log Y) gaps
+ mass and affine cancellation
+ taper and bounded block overlap
+ exact two-state first-return algebra
  => OD2.                                             (5.8)
```

It does **not** make the fine set the actual `q_I`-rough integers, the coarse
set the primes, or the deletion labels genuine least prime factors.  It does
not disprove actual `OD2`.  It proves that the missing gain in (2.3) must
come from the multiplicative law tying all survivor bits to divisibility,
not from the covariance bridge or automaton compression alone.

## 6. Primary-literature boundary

The closest primary results still do not imply (2.1).

1. [Gorodetsky, *The variance of integers without small prime factors in
   short intervals*](https://arxiv.org/abs/2111.00853), Theorem 1.1, treats
   the unweighted rough indicator averaged continuously over interval
   origins.  With his `y=Y^b` and `H=Y^h`, condition (1.7) has left side
   asymptotic to `h log Y/loglog Y` and right side bounded by `(1-epsilon)/b`.
   It therefore fails for every fixed live `b>=.1537`.  His fixed-`k`
   shifted-sieve Lemma 1.4 also does not accept first-return words of length
   `Y^.1594`, Voronoi weights, or the selected logarithmic chirp.

2. [Matomaki--Radziwill--Tao, *Correlations of the von Mangoldt and higher
   divisor functions I*](https://arxiv.org/abs/1707.01315) proves the expected
   prime and divisor correlations for almost all shifts in a range beginning
   at `Y^(8/33+epsilon)`, with arbitrary logarithmic average saving.  The
   live shallow endpoint is exactly `Y^(8/33)`, its coefficient is not
   `c_q`, and (2.3) requires a fixed power even in the ranges where their
   theorem applies.

3. [Matomaki--Shao--Tao--Teravainen, *Higher uniformity ... I*](https://arxiv.org/abs/2204.03754)
   reaches all intervals for `Lambda` only from exponent `5/8`; every live
   curvature block has exponent at most `.5797`.  [Part II](https://arxiv.org/abs/2411.05770)
   reaches almost all intervals from `1/3`, but misses the shallow blocks,
   permits exceptions, saves logarithms, and has no first-return coefficient.

4. [Matomaki--Radziwill--Tao, *An averaged form of Chowla's
   conjecture*](https://arxiv.org/abs/1503.05121) averages interval origins or
   shifts for bounded multiplicative functions and has logarithmic decay.
   The Voronoi first-return weight is neither multiplicative nor bounded
   independently of `Y` before normalization.

5. [Matomaki, *Almost primes in almost all very short
   intervals*](https://arxiv.org/abs/2012.11565) and
   [Matomaki--Teravainen II](https://arxiv.org/abs/2207.05038) provide strong
   Type-II inputs for existence and almost-all interval results.  They do not
   give a pointwise-in-one-height signed covariance of two overlapping
   first-return configurations.

6. Bazin's [product-of-primes Bombieri--Vinogradov
   theorem](https://arxiv.org/abs/2607.15137) has enough whole-shell exponent
   for a separated late semiprime surrogate.  Its localization remains on
   the `Y` scale, and its factors do not include the block-dependent tensor
   automaton in (4.3).  The thin-fibre no-go forbids replacing that automaton
   by an arbitrary local bounded factor.

No located primary theorem simultaneously supplies polynomial short-shift
saving, the exact first-return/Voronoi coefficient, blocks down to
`Y^(8/33)`, and a supremum over one common height.

## 7. Smallest honest continuation

The live lemma should be attacked without splitting its signed pieces:

```text
sup_(legal t) 2 Re sum_(r>=1) sum_I sum_n
 [W_I c_(q_I)+e_I](n)
 conjugate([W_I c_(q_I)+e_I](n+r))
 exp(-i t log(1+r/n))
 <<Y^(1+797/5000+o(1)).                               (7.1)
```

A viable proof must do at least one genuinely arithmetic thing not present in
the no-go model:

* derive cancellation in the tensor renewal law directly from divisibility;
* obtain a power-accurate low-rank separation of the paired first-return
  weights before invoking Type I/II dispersion; or
* prove cancellation between the prime-prime, prime-rough, and rough-rough
  pieces and between SPF ranges.  Bounding those pieces absolutely is not a
  valid surrogate.

The first fail-fast subproblem is the late-late sector `p,p'>Y^(1/3)`, where
both cofactors are prime but the paired first-return weights remain.  A
short-block theorem there must gain at least `Y^(-.083024...)` at the shallow
endpoint.  If even that tensor-weighted prime-product sector cannot be
localized, existing dispersion technology cannot prove full `OD2`.

## 8. Truth boundary and reproduction

```text
bands-first collapse to nu_Prime-nu_q:               EXACT
positive-shift identity (2.1):                       EXACT
least-prime-factor three-atom form:                  EXACT
paired first-return bond dimension:                  4, EXACT
generic nested/common-log package implies OD2:       FALSE
actual SPF/common-height OD2:                        OPEN
published shifted-correlation theorem proves OD2:    NONE FOUND
zero-free strip:                                     NOT PROVED
```

```bash
PYTHONPATH=src python3 -m unittest -v \
  src/test_common_height_od2_gate.py
python3 results/verify_zeta23_common_height_od2_gate.py
```

The nine tests certify trapezoid mass and affine exactness, the deletion
telescope, the exact logarithmic shift expansion, the two- and four-state
automata, the periodic nested obstruction, and every rational exponent in
the no-go ledger.  They do not assert the actual SPF theorem.
