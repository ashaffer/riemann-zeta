# PQR addendum: odd triangle-curvature charges

**Date:** 2026-08-30  
**Status:** exact theorem card and recursion audit; no PQR theorem, zero-free
strip, or proof of RH

**Subsequent `E`-defect refinement.**  The next addendum,
`ZETA23-VIBE-PQR-E-DEFECT-ROTATION-AND-ASSOCIATOR-2026-08-30.md`, proves that
`E_kji=QK_kji-d_kj d_ji` has size `O(Y^(16/33))`, is nonzero modulo four,
and has exact rank one at every middle vertex with no width restriction.  It
also records the resulting residue rotations and multiplicative associator.

## 0. Outcome

The triangle charge proposed for a same-side prime ratio shadow is genuinely
useful.  It has four rigorously proved features:

1. every charge is a **positive odd integer**;
2. every fixed-middle charge matrix has rational rank at most two;
3. on a small-curvature rectangle that rank improves exactly to one; and
4. charges at different middle vertices obey an exact cocycle identity.  In
   the rank-one regime this identity gives an affine transfer recursion.

The positivity has an immediate geometric consequence.  If an `m`-point
integer seed is transported at source period `t_0`, consecutive seed gaps
obey

```text
g_j g_(j+1) >>t_0^2/Y.
```

Therefore

```text
diam(A)>>m t_0/sqrt(Y),
physical carrier diameter >>m sqrt(Y).               (0.1)
```

At `m=Y^(.0179+o(1))`, every such prime shadow has physical width at least
`Y^(.5179-o(1))`.  In particular a near-minimal Sidon ruler cannot be
transported once `t_0>Y^(.5179+o(1))`.  This supersedes the weaker conditional
`.6961` calibration in the first PQR memo.

Combining this lower width with the determinant scale gives the global split

```text
Y^(.5179-o(1)) << W=o(Y^(25/33)):
       every fixed-middle curvature slice has rank one;

W not=o(Y^(25/33)):
       the unconditional conclusion is only rank at most two.             (0.2)
```

The charge does not yet prove polylogarithmic PQR rigidity.  Its entries are
odd integers rather than primes, so a nonzero-minor argument from unique
factorization is unavailable.  The exact transfer recursion is the new
candidate interface.

## 1. Setup

Use the same-side pointwise-clean PQR shadow from
`ZETA23-VIBE-PRIME-QUASISEPARABLE-RATIO-SHADOW-2026-08-30.md`.  Thus

```text
Y=N+1/2,                 Q=2Y=2N+1,
B=Y^(50/33),             delta=Y/B,
omega=2pi/t_0,
Y^.5<=t_0<=Y,
p_ab=Y exp[sigma omega(a_a-a_b)]+O(delta)   (a>b),  (1.1)
```

where all primes are on the same side and `sigma` is `+1` above `Y` and
`-1` below `Y`.  The seed is ordered,

```text
a_1<...<a_m,
```

and all logarithmic differences in use lie in a fixed compact shell.

For `k>j>i`, define

```text
K_kji=Q-2p_kj-2p_ji+2p_ki.                          (1.2)
```

This is an integer.  Its reference value is

```text
K*_kji
 =Q[1-exp(sigma x)-exp(sigma y)+exp(sigma(x+y))]
 =Q[exp(sigma x)-1][exp(sigma y)-1],                (1.3)
x=omega(a_k-a_j)>0,
y=omega(a_j-a_i)>0.
```

Both factors in the last product have the same sign, so `K*_kji>0` for
both choices of `sigma`.  Equation `(1.1)` gives uniformly

```text
K_kji=K*_kji+O(delta).                               (1.4)
```

## 2. Parity, sign, and size

### Proposition 2.1 -- odd positive quantization

For all sufficiently large `Y`, every charge satisfies

```text
K_kji in {1,3,5,...},
K*_kji>=1-o(1).                                     (2.1)
```

Moreover, uniformly in the fixed shell,

```text
K_kji asyp_w Y omega^2(a_k-a_j)(a_j-a_i).           (2.2)
```

#### Proof

The integer `Q` is odd and every other term in `(1.2)` is even, so `K_kji`
is odd and in particular nonzero.  Since `delta=o(1)`, equations
`K*>0` and `(1.4)` rule out every negative odd integer.  Hence `K>=1`, and
then `(1.4)` gives `K*>=1-o(1)`.

For `0<x,y,x+y<=w`,

```text
|exp(sigma x)-1|asyp_w x,
|exp(sigma y)-1|asyp_w y.
```

Use `(1.3)--(1.4)` and `K*>=1-o(1)` to obtain `(2.2)`.  QED

The word **positive** here is an exact conclusion, not merely the sign of
the reference.  It would fail without the half-integer center: parity is the
quantization mechanism.

### Corollary 2.2 -- adjacent-gap and width law

Put `g_j=a_j-a_(j-1)`.  Then

```text
g_j g_(j+1)>>t_0^2/Y.                               (2.3)
```

Consequently

```text
a_m-a_1>>m t_0/sqrt(Y).                             (2.4)
```

The corresponding physical prime carrier has diameter

```text
W>>m sqrt(Y).                                       (2.5)
```

#### Proof

Apply `(2.1)--(2.2)` to `(k,j,i)=(j+1,j,j-1)` and use
`omega=2pi/t_0`.  This proves `(2.3)`.  Pair consecutive gaps and apply
AM--GM:

```text
g_(2r-1)+g_(2r)>=2sqrt(g_(2r-1)g_(2r))
                     >>t_0/sqrt(Y).
```

Summing proves `(2.4)`.  In a fixed logarithmic shell, exponentiation is
bi-Lipschitz up to constants, so

```text
W asyp_w Y omega(a_m-a_1).
```

The support contains the largest difference `a_m-a_1`, while one adjacent
gap is at most `(a_m-a_1)/(m-1)`; hence its log-frequency diameter is
comparable to `omega(a_m-a_1)`.  Equation `(2.5)` follows.  QED

At the project value `m=Y^(.0179+o(1))`, `(2.5)` is
`W>>Y^(.5179-o(1))`.  For a near-minimal Sidon ruler
`diam(A)=Y^(.0358+o(1))`, equation `(2.4)` is impossible as soon as

```text
t_0>Y^(.5+.0179+o(1))=Y^(.5179+o(1)).               (2.6)
```

A more widely spaced ruler can satisfy `(2.4)`; `(2.6)` is not a global PQR
contradiction.  Also, the lower width `(2.5)` fits inside a fixed shell
because `.5179<1`.

## 3. Fixed-middle determinant collapse

Fix `j` and regard

```text
K^(j)=(K_kji)_(k>j,i<j)                              (3.1)
```

as a matrix.  Its reference is the outer product

```text
K*^(j)_ki
 =Q A^(j)_k B^(j)_i,
A^(j)_k=exp[sigma omega(a_k-a_j)]-1,
B^(j)_i=exp[sigma omega(a_j-a_i)]-1.                 (3.2)
```

### Proposition 3.1 -- exact rank at most two

Every `3 x 3` minor of `K^(j)` is zero for sufficiently large `Y`; hence

```text
rank_Q K^(j)<=2.                                    (3.3)
```

#### Proof

The reference `(3.2)` has rank one, its entries are `O_w(Y)`, and the
entrywise perturbation in `(1.4)` is `O(delta)`.  In a cubic determinant the
zero- and one-error terms vanish.  Therefore

```text
|det K^(j)_3x3|
 <<Y delta^2+delta^3
 <<Y^3/B^2
 =Y^(-1/33)=o(1).                                   (3.4)
```

The determinant is an integer and so vanishes.  QED

This is genuinely stronger than applying the previous ordered-cut rank-two
theorem term by term: `(1.2)` is a sum of constant, row, column, and
prime-block pieces, for which naive rank subadditivity gives only rank five.

### Proposition 3.2 -- local exact rank one

On a fixed-middle rectangle suppose the reference charges are bounded by
`S`.  If

```text
S delta=o(1),                                       (3.5)
```

then every `2 x 2` minor vanishes and that rectangle has rank one.

If its left and right logarithmic spans are `U` and `V`, respectively, a
sufficient form of `(3.5)` is

```text
Y^2 U V/B=o(1),                                     (3.6)
```

or, in physical widths `W_L=YU`, `W_R=YV`,

```text
W_L W_R=o(B).                                       (3.7)
```

#### Proof

A quadratic determinant of a rank-one matrix perturbed entrywise by
`O(delta)` is `O(S delta+delta^2)`.  Under `(3.5)` this integer has magnitude
`o(1)` and is zero.  Equations `(1.3)` and
`|exp(sigma z)-1|asyp_w z` give `S<<YUV`, proving the sufficient forms.
QED

Unlike the prime matrix, a charge matrix can have zero quadratic minors:
its entries are odd composite integers and unique factorization does not
make the four labels independent.  Thus Proposition 3.2 is a factorization
opportunity, not a contradiction.

### Corollary 3.3 -- global width phase split

Let `W` be the physical diameter of the whole same-side carrier.  Then

```text
max_(k>j>i) K*_kji <<W^2/Y.                          (3.8)
```

Consequently, if

```text
W=o(sqrt(B))=o(Y^(25/33)),                           (3.9)
```

every fixed-middle slice has exact rank one.  Without `(3.9)`, Proposition
3.1 still gives rank at most two.

#### Proof

Every left and right log span is `O_w(W/Y)`.  Equation `(1.3)` therefore
gives `(3.8)`.  With `S=W^2/Y`, the determinant error in Proposition 3.2 is

```text
S delta <<(W^2/Y)(Y/B)=W^2/B=o(1).
```

This proves `(3.9)`.  Combining it with Corollary 2.2 gives `(0.2)`.  QED

## 4. Exact compatibility across middle vertices

Define the odd edge variable

```text
q_ab=2p_ab-Q.                                       (4.1)
```

Then `(1.2)` is the exact additive curvature identity

```text
K_kji=q_ki-q_kj-q_ji.                               (4.2)
```

### Proposition 4.1 -- curvature cocycle

For every `l>k>j>i`,

```text
K_lki+K_kji=K_lkj+K_lji.                            (4.3)
```

#### Proof

Substitute `(4.2)`.  Both sides reduce to

```text
q_li-q_lk-q_kj-q_ji.
```

QED

Thus the fixed-`j` rank constraints are not independent slices.

### Proposition 4.2 -- affine transfer in the rank-one regime

Suppose the relevant fixed-middle slices have rank one and choose nonzero
factorizations

```text
K_kji=A^(j)_k B^(j)_i.                              (4.4)
```

For every `k>j` with nonempty overlaps, there is a rational scalar `c_kj`
such that, throughout those overlaps,

```text
A^(j)_l-A^(j)_k=c_kj A^(k)_l          (l>k),
B^(k)_i-B^(k)_j=c_kj B^(j)_i          (i<j).        (4.5)
```

The zero value `c_kj=0` is allowed.

#### Proof

Insert `(4.4)` into `(4.3)` and rearrange:

```text
A^(k)_l [B^(k)_i-B^(k)_j]
 =[A^(j)_l-A^(j)_k] B^(j)_i.                        (4.6)
```

This is equality of two nonzero outer products on the overlap.  Therefore
their factors agree up to one scalar, giving `(4.5)`.  If both difference
vectors vanish, take `c_kj=0`.  QED

Equation `(4.5)` is the promised recursion: after adjoining a constant
coordinate, successive factor vectors propagate by rational `2 x 2` affine
transfer matrices.  In a full-rank-two slice the analogous compatibility is
matrix-valued, subject to the usual nondegeneracy of the overlapping row and
column spans.

### 4.1 Classification audit

On one fixed-middle rectangle, rank one gives the exact local chart

```text
q_ki=q_kj+q_ji+A^(j)_k B^(j)_i.                     (4.7)
```

This contains both familiar models:

```text
multiplicative ratio: q_ki=Q(r_k/r_i-1),
additive tangent:     q_ki=c(s_k-s_i)^2,
```

whose curvatures factor respectively as multiplicative increments and as
`2c(s_k-s_j)(s_j-s_i)`.

It would be incorrect to claim that the cocycle plus slice rank one already
gives a global dichotomy between only those two models.  Even on a
rectangular chart the general zero-diagonal form

```text
q_ki=A_k+B_i+C_kD_i,
A_i+B_i+C_iD_i=0,                                   (4.8)
```

has

```text
K_kji=(C_k-C_j)(D_i-D_j).                           (4.9)
```

The sequences in `(4.8)` may vary freely before the prime,
near-exponential, and overlap constraints are imposed.  On the ordered
triangular domain no single middle vertex sees all pairs; different charts
are glued by the potentially nonconstant transfer scalars in `(4.5)`.
Thus the proved output is a nonautonomous projective/affine transfer chain.
Reducing it to constant diagonal (ratio) or unipotent (tangent) transfer
requires an additional commutation or height-rigidity theorem.

## 5. Does this terminate PQR?

Not yet.  The exact implications are

```text
prime ratio shadow
    -> positive odd K charges
    -> broad-carrier law W>>m sqrt(Y)
    -> fixed-middle rank <=2
    -> local rank 1 when W_L W_R=o(B)
    -> affine transfer recursion on overlapping rank-one regions.        (5.1)
```

Three gaps remain.

1. A fixed shell easily accommodates width `Y^.5179`; the broadness law is
   not a contradiction.
2. In the intermediate range
   `Y^.5179<<W=o(Y^(25/33))` every curvature slice is rank one, but its
   transfer scalars may still vary.  At `W not=o(Y^(25/33))`, global
   rectangles may contain charges large enough that only cubic determinants
   collapse.
3. Rank-one odd integer matrices do not inherit the prime-entry UFD
   obstruction.  The transfer scalars may vary with the middle vertex, so
   `(4.5)` is not yet one constant recurrence to which PHR2 applies.

The most precise next theorem card is therefore:

> **Curvature-transfer rigidity.**  In a PQR shadow of length
> `m=Y^(.0179+o(1))`, use positivity, the cocycle `(4.3)`, local rank-one
> patches, and the bounded prime Pluecker minors to prove either
>
> 1. a constant rational transfer on a run longer than `C log Y`, hence a
>    PHR2-type recurrence contradiction; or
> 2. enough independent transfer variation to force total logarithmic span
>    beyond the fixed shell.

This statement is open.  It is narrower than PQR because the new parity and
recursion are now proved inputs rather than desired conclusions.

```text
reference factorization and O(Y/B) error:             PROVED
K positive odd and K*>=1-o(1):                        PROVED
adjacent-gap / broad-carrier law W>>m sqrt(Y):         PROVED
fixed-middle rank at most two:                         PROVED
small-curvature local rank one:                        PROVED
global split at W=sqrt(B)=Y^(25/33):                  PROVED
four-vertex cocycle and rank-one affine transfer:      PROVED
ratio/tangent global classification from rank one:     NOT PROVED
constant-transfer or span-growth dichotomy:            OPEN
PQR / PQR+G:                                          OPEN
uniform zero-free strip:                              NOT PROVED
RH:                                                   NOT PROVED
```
