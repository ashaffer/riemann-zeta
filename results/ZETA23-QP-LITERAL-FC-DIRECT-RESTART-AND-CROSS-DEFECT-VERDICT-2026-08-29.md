# QP literal FC: direct restart and cross-defect verdict

**Date:** 2026-08-29

**Verdict:** the literal sharp four-cycle estimate is neither proved nor
disproved.  Restarting from the undeleted positive Schatten form produces a
lossless defect-layer normal form and a restricted-type theorem equivalent to
FC up to logarithms.  It also rules out all pair-marginal Holder/AM--GM
rearrangements as a source of the missing gain.  The exact residual problem is
positive coherence between different signed defect matchings.

No legal `q^delta` counterexample was found.  An explicit primitive prime
tangent chart conditionally realizes the FC scale up to logarithms, but every
tested translation or multi-slope amplification remains at most
`D q^o(1)`.

## 1. Literal target and positivity

Let

```text
S_q={p^j:(q/2)e^(-w)<p^j<(q/2)e^w},
0<w<(log 2)/3,
D=q^(16/33+o(1)),
kappa(a,b,c)=1_(a,b,c in S_q) 1_(|8abc-q^3|<=qD),
A_u(a,b)=sum_c u_c kappa(a,b,c).
```

The literal endpoint is

```text
F_+(u)=||A_u||_(S4)^4 << D q^o(1)||u||_2^4,
u>=0.                                                   (FC)
```

For complex coefficients, termwise absolute values in the fourth-trace
expansion give

```text
||A_z||_(S4)^4<=F_+(|z|).                              (1.1)
```

Thus the positive form is the correct worst case.  It counts each physical
rectangle once.  If `m(C)` is the number of carrier completions of a color
matrix `C`, its coefficient is `m(C)`, not `m(C)(m(C)-1)` or `m(C)^2`.

## 2. Exact row-pair operator

For ordered pairs put

```text
H_((a,a'),(c,c'))
  =sum_b kappa(a,b,c) kappa(a',b,c'),
v_u(c,c')=u_c u_c'.                                    (2.1)
```

The missing-coordinate interval has length `O(D/q)<1`, so every entry of
`H` is zero or one.  Direct expansion gives the lossless identity

```text
F_+(u)=||H v_u||_2^2.                                  (2.2)
```

This is an identity for the full positive hard matrix.  An arbitrary
rectangle-level deletion need not factor through `H`, so filtered
block-odd/all-distinct forms must not be substituted into (2.2).

## 3. Signed defect matchings

Label an edge of `H` by the signed integer

```text
h=ac-a'c'.                                             (3.1)
```

Subtracting the two hard residuals with common carrier `b` gives
`|h|<<D`.  Write

```text
H=H_0+sum_(0<|h|<<D) H_h.                             (3.2)
```

### Lemma 3.1

Every nonzero signed layer `H_h` is a partial matching for all sufficiently
large `q`.

**Proof.**  Since `0<|h|<<D<min S_q`, neither `a=a'` nor `c=c'` is possible.
Distinct nodes of the narrow prime-power shell have distinct prime bases and
are coprime.  If two right endpoints `(c,c')` and `(d,d')` meet the same
left endpoint in one layer, then

```text
a(c-d)=a'(c'-d').                                      (3.3)
```

Coprimality gives `(c-d,c'-d')=t(a',a)`.  The shell diameter is smaller
than `min(a,a')`, so `t=0`.  Interchanging the two sides proves column
injectivity.  QED

Consequently

```text
sum_(h!=0)||H_h v||_2^2 << D||v||_2^2.                (3.4)
```

The zero layer consists of the repeated/permutation configurations forced by
unique factorization.  The standard repeated-row/column argument bounds it at
the sharp scale: for example, if

```text
R_a=sum_b |A_u(a,b)|^2,
```

then pair uniqueness gives `R_a<=||u||_2^2`, while the color-degree bound
gives `sum_a R_a<<Dq^o(1)||u||_2^2`; hence
`sum_a R_a^2<<Dq^o(1)||u||_2^4`.  The transpose and permutation terms are
identical.  Equivalently, one may split `H=H_0+H_*` and use the triangle
inequality; positivity gives the reverse domination needed for the open
part.

For `v=v_u`, the remaining nonzero-layer mass is exactly

```text
||H_*v||_2^2
 =sum_h ||H_hv||_2^2
  +sum_(h!=k)<H_hv,H_kv>.                             (3.5)
```

All terms in the second sum are nonnegative.  The first sum is already
`O(D||u||_2^4)` by (3.4).  Thus the earliest unproved assertion is

```text
sum_(h!=k)<H_h(u tensor u),H_k(u tensor u)>
  <<Dq^o(1)||u||_2^4.                                 (XDC)
```

This is the residual literal FC mass, not a stronger arbitrary-vector or
factorial surrogate.

## 4. A restricted-type theorem equivalent to FC

For a color subset `E subset S_q`, define the full ordered count

```text
R(E)=||A_(1_E)||_(S4)^4.                              (4.1)
```

### Theorem 4.1

Up to a factor `(1+log |S_q|)^2=q^o(1)`, FC is equivalent to

```text
R(E)<<Dq^o(1)|E|^2             for every E.            (RT)
```

**Proof.**  FC implies RT by taking `u=1_E`.  Conversely, order the
coordinates so that `u_1>=...>=u_N>=0`, set `u_(N+1)=0`,

```text
delta_k=u_k-u_(k+1),       E_k={1,...,k}.
```

Then `u=sum_k delta_k 1_(E_k)`.  Linearity and the Schatten triangle
inequality give

```text
||A_u||_(S4)
 <<D^(1/4)q^o(1) sum_k delta_k sqrt(k).               (4.2)
```

Summation by parts and Cauchy--Schwarz yield

```text
sum_k delta_k sqrt(k)
 =sum_k u_k(sqrt(k)-sqrt(k-1))
 <=sqrt(1+log N)||u||_2.                              (4.3)
```

Taking fourth powers proves FC with a logarithmic-square loss.  QED

Let `d_E(alpha)` be the number of `E^2`-colored nonzero-defect wedges at
row pair `alpha`.  The matching layers prove the first moment

```text
sum_alpha d_E(alpha)<<D|E|^2.                         (4.4)
```

Modulo the controlled zero layer, RT is exactly

```text
sum_alpha d_E(alpha)(d_E(alpha)-1)
  <<Dq^o(1)|E|^2.                                    (4.5)
```

Equation (4.5) is therefore a clean set-theoretic version of XDC.  It
allows isolated high stars and is weaker than a maximum-row-sum/NDS theorem.

### 4.1 Hostile test of fixed-diagonal serialization

A stronger sufficient theorem would be

```text
N_(c,d):=#{physical rectangles with c_11=c and c_22=d}
          <<Dq^o(1)                                   (FDS)
```

uniformly in the two opposite colors.  Indeed, opposite-pair AM--GM and
orientation symmetry would give

```text
F_+(u)
 <=(1/2)sum_rectangles[(u_(c11)u_(c22))^2
                       +(u_(c12)u_(c21))^2]
 <<Dq^o(1)||u||_2^4.                                  (4.6)
```

The direct attempt does not prove FDS, but it identifies its first exact
gap.  Define the color link matching

```text
L_c={(a,b) in S_q^2: |8abc-q^3|<=qD}                 (4.7)
```

and let `M(x,y)` be one if the unique integer `z` in the missing-coordinate
window exists and lies in `S_q`.  Product-interval length and unique
factorization give

```text
L_c is a partial matching,       |L_c|<<Dq^o(1).       (4.8)
```

Losslessly,

```text
N_(c,d)=sum_((a,b) in L_c) sum_((A,B) in L_d)
           M(a,B)M(A,b).                              (4.9)
```

Thus FDS is a two-reciprocal correlation of two `D`-edge link matchings.
UFD proves (4.8), but it does not bound the correlation (4.9).  In shift
coordinates, writing `e=c12`, `f=c21`, and

```text
u=bc-Be,  v=ae-Ad,  w=Bd-bf,  t=Af-ac,
k=cd-ef,
```

all four shifts and `k` are `O(D)`, and

```text
k b=d u+e w,       k B=f u+c w,
k a=-d t-f v,      k A=-e t-c v,
a u+B v+A w+b t=0.                                  (4.10)
```

For fixed `k`, divisor bounds leave `q^o(1)` choices for `(e,f)`, but the
known completion estimate is still only `m(C)<<sqrt(D)q^o(1)`; no shift in
(4.10) is globally injective as `k` varies.  This is the exact aggregation
loss, before any conic or factorial lift.

The proposed scale is sharp even for the full-integer hard window.  A
translation/tangent family with width `L asymp sqrt(D)` can keep both
opposite diagonal colors fixed and supplies `asymp D` rectangles.  It is not
an actual-prime-power counterexample, but it rules out an `o(D)` FDS target.

## 5. Direct routes that do not close XDC

### 5.1 Pair-marginal Holder and AM--GM

For each pair `S` of the four color positions, let

```text
P_S(u)=sum_rectangles product_(i in S) u(c_i)^2.
```

Every fractional pair-marginal Holder cover satisfies

```text
theta_12=theta_34, theta_13=theta_24, theta_14=theta_23,
theta_12+theta_13+theta_14=1/2.
```

Hence its feasible polytope is the convex hull of the three perfect
matchings, and its best possible conclusion is

```text
min{sqrt(P_12 P_34),sqrt(P_13 P_24),sqrt(P_14 P_23)}. (5.1)
```

These are precisely the three previously known gap-fibre bounds.  On
`u=1_E/sqrt(|E|)`, per-rectangle AM--GM is equality in every orientation.
Thus no adaptive Cauchy orientation proves RT.

### 5.2 Coarse logarithmic planes

For `1<=R<=D`, the injective coordinate

```text
n_R(x)=floor((q^2/R) log(2x/q))
```

places hard triples on `O(D/R)` additive planes.  But a fixed quantized pair
relation is a union of `O(R)` exact determinant matchings.  The complexity is

```text
(D/R)*R=D.                                             (5.2)
```

At `R=D` one has only `O(1)` coarse planes but `D` coherent internal
layers.  Quantization relabels XDC; it does not reduce it.

### 5.3 Matching structure alone

A complete bipartite graph decomposed into `D` cyclic perfect matchings has
the same layer axioms and admits a flat Cartesian tensor for which all
cross-layer terms cohere.  This abstract model is nonphysical, but proves
that partial matchings plus the tensor-square input cannot establish XDC.
The four simultaneous cubic product masks must be used.

## 6. Counterexample audit

No legal fixed-power `q^delta` violation of RT was found.

One exact primitive admissible four-linear-form near-cube produces a tangent
box of side

```text
L asymp sqrt(D).
```

Dickson's conjecture makes its four base forms simultaneously prime.  A
stronger uniform short-box Hardy--Littlewood hypothesis populates the box
with ordinary primes and gives

```text
R(E)/(D|E|^2) >> (log q)^(-6).                         (6.1)
```

Thus physical prime tangent packets can conditionally saturate FC up to
subpowers.  They do not violate it.  Exact same-color translations obey
`B*ell<<sqrt(D)`, so their total contribution is `O(Dq^o(1))`.  A dyadic
Farey/multi-slope capacity calculation gives `O(D/R^2)` at direction height
`R`, or `O(D/R)` for gcd-rich color progressions.  Generic anchors have the
additional occupancy deficit

```text
D^2/q=q^(-1/33).                                      (6.2)
```

The counterexample branch therefore ends at a sharp conditional saturator,
not a disproof.

## 7. What is proved and what remains

```text
complex-to-positive reduction:                         PROVED;
literal row-pair identity (2.2):                        PROVED;
signed nonzero defect layers are partial matchings:     PROVED;
diagonal defect mass O(D||u||_2^4):                     PROVED;
FC <=> restricted-type RT up to log^2:                  PROVED;
all pair-marginal Holder improvements exhausted:        PROVED;
proper-power coefficient colors removable:             PROVED ELSEWHERE;
conditional ordinary-prime tangent saturation:          CONSTRUCTED;
legal q^delta counterexample:                           NOT FOUND;
cross-defect coherence XDC / RT:                        OPEN;
literal sharp four-cycle bound:                         OPEN.
```

The next honest theorem is (4.5), or an arithmetic sufficient mechanism for
it.  Proving an arbitrary-pair operator norm, a cardinal maximum-degree
bound, or a factorial completion estimate would be strictly stronger and
should not again be substituted for the literal target.

Companion artifacts:

```text
results/ZETA23-QP-LITERAL-FC-DISPROOF-AUDIT-AND-PROPER-POWER-COLOR-ELIMINATION-2026-08-29.md
results/ZETA23-QP-LITERAL-FC-CONDITIONAL-PRIME-PACKET-COUNTEREXAMPLE-BUILDER-2026-08-29.md
results/verify_zeta23_qp_literal_fc_conditional_prime_packet_builder.py
```
