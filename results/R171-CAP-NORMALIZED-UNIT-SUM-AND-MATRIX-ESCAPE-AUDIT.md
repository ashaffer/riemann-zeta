# R171 cap-normalized unit-sum and matrix-escape audit

## Status

For two scalar channels, the bounded-domain collective-cofactor problem is
exactly the cap-normalized two-unit problem isolated in R169:

```text
1+G=R_1+R_2,                 R_1,R_2 units,              (0.1)
G=Z A,                       A a unit,                    (0.2)
G,R_1,R_2 -> 1 on the fixed right cap.                  (0.3)
```

There is no general Runge, Cousin, stable-rank, or `2-good` theorem which
supplies (0.1)--(0.3).  In fact, the ring of all holomorphic functions on
the disc is not `2-good`.  The known Nevanlinna counterexample does not
decide the special class (0.2), however: its translate by `-1` has an
unbounded zero divisor, whereas (0.2) has a fixed finite divisor.

One further scalar shortcut can be closed completely.  A head-normalized
function with a uniformly bounded zero divisor cannot omit even a *moving*
nonzero value which tends to zero.  Consequently a constant summand

```text
1+G=c_H+(1+G-c_H),               c_H -> 1               (0.4)
```

can never solve the normalized two-unit problem.  This obstruction is
qualitative and has no growth hypothesis, so allowing polynomial logarithmic
growth does not rescue (0.4).

Matrix units behave differently.  There is an elementary exact `2 x 2`
identity which decomposes `(1+G)I_2` into two cap-normalized matrices of
determinant one.  It even gives a matrix-valued mixed-product cofactor which
is identically safe.  Thus matrix dimension genuinely defeats the scalar
Nevanlinna obstruction at the level of `GL_2`.

It does **not** yet solve the high-girth determinant amplifier.  Matrix
invertibility is weaker than requiring every directed edge coordinate to be
a scalar unit in the exact divisor class.  The explicit matrices contain
entries which may vanish, and a generic Smith-form or Oka completion does
not preserve the edgewise constraints.  A useful coefficient-compatible
subcase remains: if `G-1=t c` is already factored into two late-supported
pieces, all nonconstant entries of the `2 x 2` split are late-supported.

```text
scalar product/two-unit equivalence                       THEOREM (R169)
generic O(D) two-good property                            FALSE
special cap-normalized two-unit problem                   OPEN
moving omitted value a_H -> 0 with fixed divisor          IMPOSSIBLE
constant-summand normalized construction                  IMPOSSIBLE
cap-normalized Blaschke/inner prescribed-fibre lift       IMPOSSIBLE
cap-normalized GL_2 two-unit split                        EXACT
matrix mixed-product safe cofactor                        EXACT
entrywise scalar-unit/high-girth realization              OPEN
polynomial logarithmic growth contradiction               NO
fixed uniform zeta zero-free strip                         NOT PROVED
```

Date: 2026-08-08.

Predecessors:
[`R155-NORMAL-FAMILY-MIXED-VALUE-INEVITABILITY-GATE.md`](R155-NORMAL-FAMILY-MIXED-VALUE-INEVITABILITY-GATE.md),
[`R165-NONLINEAR-SAFE-FIBER-AND-GLOBAL-ENTIRE-GATE.md`](R165-NONLINEAR-SAFE-FIBER-AND-GLOBAL-ENTIRE-GATE.md),
[`R167-QUANTITATIVE-NONNORMAL-RATIO-CLOUD-GATE.md`](R167-QUANTITATIVE-NONNORMAL-RATIO-CLOUD-GATE.md),
and
[`R169-TWO-UNIT-DECOMPOSITION-AND-PRODUCT-AMPLIFIER-GATE.md`](R169-TWO-UNIT-DECOMPOSITION-AND-PRODUCT-AMPLIFIER-GATE.md).

## 1. The exact scalar gate

Let `Omega` be simply connected, let `V` be a nonempty fixed open cap, and
let `Z` have a fixed finite zero divisor in `Omega`.  Suppose

```text
G=Z A_0,                         A_0 in O(Omega)^x,       (1.1)
1+G=R_1+R_2,                     R_j in O(Omega)^x.       (1.2)
```

Set

```text
F_1=G/R_2,              F_2=G/R_1,              P=G/(R_1R_2).
                                                               (1.3)
```

Then every function in (1.3) has exactly the divisor of `Z`, and

```text
1-(F_1-1)(F_2-1)=P.                                    (1.4)
```

Indeed,

```text
F_1-1=(R_1-1)/R_2,       F_2-1=(R_2-1)/R_1,             (1.5)
```

and (1.4) follows from `R_1+R_2-1=G`.  The cofactor

```text
P/Z=A_0/(R_1R_2)                                         (1.6)
```

is a unit.  If `G,R_1,R_2 ->1` on `V`, then so do
`F_1,F_2,P`.  R169 proves the converse as well, so (1.2) is not merely a
sufficient ansatz: it is the exact scalar `q=2` normal form.

Equivalently, with `q=R_1/R_2`, a solution is a pair of units `q,L`
satisfying

```text
1+q=(1+G)L,                    q,L ->1 on V.             (1.7)
```

Thus the analytic task is a prescribed-fibre problem for `1+q`, not an
ordinary additive Cousin problem.

## 2. Why ordinary `2-good` and Runge claims are insufficient

The statement that every member of `O(Omega)` is a sum of two units is
false already for the unit disc.  An explicit example, recorded by
Eremenko via the disc second main theorem, is

```text
L(z)=(1-z)^(-3),
W(z)=[1-exp L(z)]^2.                                     (2.1)
```

If `W=exp f+exp g`, then after division by one exponential the `-1` points
of `exp(f-g)` inherit the multiple-zero divisor of the square in (2.1).
The second main theorem contradicts this when the characteristic has the
growth of (2.1).  Hence `O(D)` is not `2-good`.

This is a reality check, not a counterexample to (1.1)--(1.3).  In (2.1),
`W-1` has a proliferating value divisor.  The present problem instead asks
for

```text
W=1+G,                     # distinct {W=1}=O(1).         (2.2)
```

The disc second main theorem then forces a large zero cloud of `W` whenever
its characteristic is large.  Those `W=0` points are precisely the odd
logarithmic fibres needed in a possible two-unit representation.  The known
square counterexample therefore cannot simply be imported into the fixed
divisor class.

At one bounded stage a constant outside the range gives a bare two-unit
decomposition.  It does not address the simultaneous limit of both units
to `1`.  The next theorem shows that allowing the constant to move toward
`1` cannot repair this defect.

## 3. Moving-to-zero omission rigidity

### Theorem 3.1 -- a moving small value cannot be omitted

Let `Omega` be simply connected, `V` a nonempty open subset, and fix
`rho in Omega`.  There is no sequence `G_n in Hol(Omega)` and nonzero
numbers `a_n ->0` such that

```text
G_n ->1 locally uniformly on V,
G_n(rho)=0,
a_n notin G_n(Omega),                                    (3.1)
```

while the number of distinct zeros of `G_n` in `Omega` is uniformly
bounded.

#### Proof

Because `G_n-a_n` is a unit and `Omega` is simply connected, choose a
holomorphic logarithm

```text
exp h_n=1-G_n/a_n.                                       (3.2)
```

At `rho`, the right side is one.  Change the logarithm branch so that

```text
h_n(rho)=0.                                               (3.3)
```

For the fixed lattice `Lambda=2 pi i Z`,

```text
h_n(s) in Lambda       iff       G_n(s)=0.               (3.4)
```

If `G_n` has at most `M` distinct zeros, `h_n(Omega)` meets at most `M`
distinct values of `Lambda`.  Among any fixed `M+2` nonzero lattice
values, at least two are omitted.  Passing to a subsequence, the same pair
is omitted for every `n`.  Montel's theorem makes `{h_n}` a normal family.

On compact subsets of `V`, (3.1) and `a_n ->0` give

```text
Re h_n=log|1-G_n/a_n| -> +infinity.                       (3.5)
```

Every normal limit is therefore identically infinity on `V`, and hence on
all of connected `Omega` by the meromorphic identity theorem.  This
contradicts (3.3).  QED.

### Corollary 3.2 -- constant summands are closed

There is no cap-normalized decomposition

```text
1+G_n=c_n+(1+G_n-c_n)                                   (3.6)
```

into two units when `G_n` has a uniformly bounded zero divisor and
`G_n ->1` on `V`.

Indeed, cap normalization of the first summand gives `c_n ->1`.  If
`c_n=1`, the second summand is `G_n` and is not a unit.  Otherwise its
zero-freeness says that `G_n` omits

```text
a_n=c_n-1 ->0,                                           (3.7)
```

contrary to Theorem 3.1.

The theorem has no bound on the characteristic or supremum of `G_n`.
Thus this shortcut is impossible even with an arbitrarily large polynomial
logarithmic-growth budget.

### Remark 3.3 -- what a scalar solution must do

For any solution of (1.2), the ratio `q=R_1/R_2` cannot be a normal family.
If it were, cap convergence would force `q ->1` throughout `Omega`.  Then
`1+q` would be a unit on each smaller fixed domain for large `n`, and (1.7)
would make `1+G` a unit.  This would make `G` omit `-1`, contradicting the
R155 logarithmic-lattice theorem for a fixed finite divisor.

Consequently `q` must create an unbounded value cloud, including an
unbounded divisor of `q=-1`, equivalently of `1+G=0`.  R167 quantifies the
associated outer-growth tax.  That tax is a fixed power when the cap error
is a fixed power, so it fits rather than contradicts the allowed polynomial
budget.

The exact divisor identity in (1.7) is

```text
div(1+q)=div(1+G),                                       (3.8)
```

because `L` is a unit.  On fixed nested coordinate discs `K_0 compactly in
K_1`, with the center chosen in the cap, Jensen's formula gives

```text
# distinct {q=-1 in K_0}
 <=C_K[log^+ sup_(K_1)|q|+1].                            (3.9)
```

The cap normalization keeps `|1+q|` bounded below at that center.  Thus a
polynomial supremum permits `O(log H)` such points, while the weaker ledger
`log sup|q|=O(H^lambda)` permits `O(H^lambda)`.  Scalar necessity only says
that this number tends to infinity.  It does not overrun either budget.

### Theorem 3.4 -- the exact Blaschke prescribed-fibre formula

There is a clean conditional solution which exposes what a bounded inner
construction would have to do.  Work in disc coordinates.  Let

```text
W=1+G=B S,                                                (3.10)
```

where `B` is a Blaschke product with exactly the zero divisor of `W` and
`S` is a unit.  Put

```text
q=exp[i pi(1-B)],
J(zeta)=[1-exp(-i pi zeta)]/zeta,       J(0)=i pi.        (3.11)
```

Since `|B|<1`, the only zero of `1-exp(-i pi B)` occurs at `B=0`.
Moreover,

```text
1+q=1-exp(-i pi B)=B J(B).                               (3.12)
```

The function `J` has no zero on `|zeta|<=1`: its nonzero zeros would be
the points `2k`, `k in Z\{0}`.  Therefore

```text
L=J(B)/S,
R_2=L^(-1)=S/J(B),
R_1=qL^(-1)=qS/J(B)                                      (3.13)
```

are units and satisfy

```text
R_1+R_2=W.                                                (3.14)
```

If along a sequence

```text
B_H ->1,                 W_H ->2                         (3.15)
```

on the cap, then `S_H=W_H/B_H ->2`, while

```text
q_H ->1,                 J(B_H)->J(1)=2.                 (3.16)
```

Thus both units in (3.13) tend to one.  The functions
`q_H`, `J(B_H)`, and their inverses are bounded by absolute constants.
Consequently the symmetric logarithmic growth of `R_1,R_2` is, up to
`O(1)`, exactly that of `S_H` and `1/S_H`.

This gives a complete scalar solution under the two concrete hypotheses

```text
normalized Blaschke factor B_H ->1 on the cap,
zero-free quotient S_H^(+/-1) inside the power budget.   (3.17)
```

The first hypothesis looks natural but is incompatible with the retained
fixed divisor.

### Corollary 3.5 -- the normalized Blaschke lift cannot occur here

Let `G_H` have a uniformly bounded zero divisor including a fixed zero
`rho`, and let `G_H ->1` on the fixed cap.  There is no sequence of bounded
holomorphic functions `B_H`, `|B_H|<=1`, such that

```text
div B_H=div(1+G_H),                  B_H ->1 on the cap.  (3.18)
```

#### Proof

Choose a fixed relatively compact simply connected inner bridge `D` which
contains `rho` and a nonempty cap open set.  R155's one-value
logarithmic-lattice theorem, applied on `D`, says that `G_H` cannot omit
`-1` there for all large `H`.  Hence there is

```text
xi_H in D,                  1+G_H(xi_H)=0.               (3.19)
```

After shrinking the outer bridge slightly, the points `xi_H` lie in a
fixed compact set.

On the other hand, the bounded family `{B_H}` is normal.  Its cap limit is
one, so every subsequential limit is identically one on the connected
bridge by the identity theorem.  Thus `B_H ->1` locally uniformly
throughout the bridge.  This contradicts

```text
B_H(xi_H)=0.                                               (3.20)
```

QED.

Theorem 3.4 is still useful as a structural test: it proves that matching
the zero divisor is easy once a normalized bounded inner factor exists.
Corollary 3.5 shows that the needed scalar section cannot be bounded/inner.
It must place the matched `-1` fibre in a genuinely unbounded, nonnormal
factor.  Canonical Blaschke products, by themselves, do not supply the
escape.

## 4. An exact cap-normalized `GL_2` split

The scalar obstruction disappears as soon as “unit” means an invertible
matrix.

### Theorem 4.1 -- elementary matrix two-unit identity

Let `G in Hol(Omega)`, put

```text
a=G-1,                         W=1+G=2+a,                (4.1)
```

and let `t` be any nonzero complex number, or more generally any
holomorphic unit.  Define

```text
      [ 1      t ]                 [ 1+a    -t ]
U  =  [          ],          V  =  [           ].        (4.2)
      [ a/t  1+a ]                 [ -a/t    1 ]
```

Then

```text
U+V=W I_2,          V=U^(-1),          det U=det V=1.    (4.3)
```

In particular `U,V in GL_2(Omega)` for every `G`; no scalar value of `G`
has to be omitted.

#### Proof

The sum in (4.3) is immediate, and

```text
det U=(1+a)-a=1,
det V=(1+a)-a=1,
UV=I_2.                                                   (4.4)
```

QED.

If on the cap

```text
sup_V |a|<=epsilon<=1                                   (4.5)
```

and `t=sqrt(epsilon)`, then

```text
sup_V (||U-I||+||V-I||) << sqrt(epsilon).                (4.6)
```

For a fixed outer compact set `K`, put

```text
B=max(1,sup_K|a|).                                       (4.7)
```

The entrywise size obeys

```text
log^+ sup_K(||U||+||V||)
 <<1+log B+(1/2)log(1/epsilon).                          (4.8)
```

Thus `epsilon=H^(-mu+o(1))` and polynomial logarithmic growth of `B`
give polynomial logarithmic growth for the matrix units, with only an
additional `O(log H)` tax.

This explicit result is consistent with the general ring-theoretic facts:
the holomorphic function ring on an open Riemann surface is an elementary
divisor domain, and Henriksen proved that `M_d(R)`, `d>1`, is `2-good` when
`R` is an elementary divisor ring.  The formula (4.2) is stronger for this
particular scalar matrix because it supplies the cap normalization and the
growth ledger directly.

## 5. Exact matrix mixed-product lift

There is more than an additive identity here.  Since

```text
V=U^(-1)=W I_2-U,                                        (5.1)
```

the matrices `U` and `V` commute.  Define matrix-valued channels

```text
X_1=G V^(-1),                    X_2=G U^(-1).            (5.2)
```

Then

```text
X_1-I=(U-I)V^(-1),        X_2-I=(V-I)U^(-1),             (5.3)
```

and commutativity gives the exact identity

```text
I-(X_1-I)(X_2-I)=G(UV)^(-1)=G I_2.                       (5.4)
```

Thus every channel is `G` times an invertible matrix and the output is
exactly the scalar matrix `G I_2`.  If `G ->1` and `U,V ->I_2` on the cap,
then `X_1,X_2` and the output tend to `I_2`.  This is a complete analytic
matrix analogue of the scalar safe-cofactor construction.

Taking determinants multiplies the scalar divisor by the matrix dimension:

```text
det X_j=G^2,             det[G(UV)^(-1)]=G^2.             (5.5)
```

One may divide a trace logarithmic derivative by two if only the residue
normalization is at issue.  Coefficientwise positivity and late support do
not follow from (5.2).

## 6. Why this does not yet solve the edgewise determinant gate

The high-girth construction asks for scalar edge functions of the form

```text
F_e=1+A_e/w_e=P M_e,              M_e a scalar unit,     (6.1)
```

while the determinant output remains in the same exact divisor class.
Theorems 4.1--5.1 only say that whole matrices are invertible.

The distinction is concrete in (4.2):

```text
t,              a/t,              1+a                  (6.2)
```

are matrix entries.  The entry `a/t` vanishes at every `G=1` point, and a
constant choice of `t` contributes a head coefficient.  Neither property is
allowed by an assertion that every edge coordinate is itself a prescribed
scalar unit with deleted head.

Similarly, Smith reduction or the Oka flexibility of `GL_d` can construct

```text
B=L diag(P,1,...,1) R,                                   (6.3)

```

with `det B=P` times a unit.  Matrix multiplication in (6.3) turns entries
into sums.  It does not preserve

```text
[B_ij-(I+W)_ij]/P = -w_ij M_ij in O(Omega)^x.            (6.4)

```

For a single directed `q`-cycle, the determinant is exactly

```text
1-product_(e in cycle)(F_e-1),                           (6.5)

```

so matrix notation merely recovers the scalar mixed-product gate.  Extra
matrix dimension helps only if multiple cycles or blocks create new freedom
without reintroducing short support paths.

There is one algebraic exception which also explains the positivity issue.
If a signed matrix `W` has rank one and its only nonzero eigenvalue is `-1`,
then the matrix determinant lemma gives

```text
det[I+(1-P)W]=P.                                         (6.6)

```

This is an exact safe cofactor with all diagonal multipliers equal to one.
A nonnegative rank-one matrix cannot have the nonzero eigenvalue `-1`.
For an irreducible nonnegative matrix with peripheral eigenvalue `-1`,
Perron--Frobenius also supplies the positive peripheral eigenvalue `+1`;
the diagonal ansatz consequently retains an additional factor (for a
two-cycle it is `2-P`).  Independent edge multipliers are then needed, and
their safe selection is again a nonnormal value-fibre problem.

### 6.1 A coefficient-compatible subcase

Formula (4.2) nevertheless suggests a concrete block mechanism.  If

```text
a=G-1=t c                                                   (6.7)
```

with both `t` and `c` late-supported, then every nonconstant entry of
`U-I` and `V-I` belongs to

```text
{t,c,tc}.                                                 (6.8)
```

The scalar head error `a` is a product, while the matrix units remain
exactly invertible.  In fact, for elementary unipotent matrices,

```text
U=E_21(c)E_12(t),                 V=U^(-1).               (6.8a)
```

A Dirichlet-monomial choice of the unit `t` makes the
division `a/t` literal, but it shifts coefficient indices and can destroy
the required support unless `a` has the matching divisibility.  The signs
in (4.2) also prevent an immediate coefficientwise-positive trace expansion.

There is a sharp causal ledger hidden in (6.7).  To make the off-diagonal
entries of `X_j-I` genuinely head-deleted, both

```text
t                         and                         c=a/t             (6.9)
```

must be tails.  If their least Dirichlet supports exceed `H`, unique
factorization/convolution gives

```text
least support(a)=least support(tc)>H^2.                  (6.10)
```

Thus the two-step gain has already been assumed in `G-1=a` before the
matrix split is made.  Moreover (5.5) gives

```text
[det output]'/[det output]=2G'/G,                        (6.11)
```

whose first Dirichlet support is the first support of `G-1`; the `GL_2`
identity does not amplify it again.  Conversely, if `t` is the small scalar
constant used in (4.6), it is a zero-length edge.  Short closed walks using
that entry reappear in the trace expansion, so directed girth no longer
forces a product of two late factors.

The `GL_2` construction therefore proves analytic matrix safety, but by
itself it only *repackages* a pre-existing support factorization.  Turning
it into a causal amplifier requires a graph in which every closed walk pays
new late factors without first putting their full product into `G-1`.

Accordingly, the next useful lemma is not another abstract `GL_d` or
stable-rank theorem.  It is a graph- and coefficient-specific realization
of (6.7)--(6.8), or a higher-girth analogue, in which

1. every differentiated cycle contains the desired number of late factors;
2. the signed off-diagonal entries combine into a nonnegative trace series;
3. every required scalar edge quotient in (6.1) is a unit; and
4. the entrywise logarithmic characteristic stays inside the polynomial
   optional-prime budget.

## 7. Decision

The scalar bounded-domain existence gate has not been proved or disproved.
It has reduced to a special cap-normalized two-unit problem for which the
generic ring theorem is false and the known Nevanlinna counterexample lies
outside the fixed-divisor class.  Theorem 3.1 closes the simplest remaining
constant/near-zero workaround, but a successful scalar solution may still
use the mandatory growing `1+G=0` cloud and fixed-power nonnormality.

Matrix dimension is a real analytic escape, not just a slogan: (4.2) and
(5.4) are exact and quantitatively cap-normalized.  What remains is the
arithmetic-combinatorial lift from matrix invertibility to edgewise scalar
units with high-girth late support.  Neither outcome establishes a fixed
zeta zero-free strip by itself.

## References

- A. Eremenko, answer to *Sums of zero-free entire functions and its
  siblings on the disk*, MathOverflow (2017), using the disc second main
  theorem; see also W. K. Hayman, *Meromorphic Functions*, Chapter 2.
- M. Henriksen, *Two classes of rings generated by their units*, Journal of
  Algebra **31** (1974), 182--193.
- A. K. Srivastava, *A survey of rings generated by units*, Annales de la
  Faculte des Sciences de Toulouse **19** (2010), 203--213, especially
  Theorem 0.2.
- O. Helmer, *Divisibility properties of integral functions*, Duke
  Mathematical Journal **6** (1940), 345--356, together with the standard
  elementary-divisor theorem for holomorphic function rings on open
  Riemann surfaces.
