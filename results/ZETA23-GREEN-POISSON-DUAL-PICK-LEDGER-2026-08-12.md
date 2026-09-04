# Green--Poisson duality: a sharper conditional Pick ledger

Status: exact Poisson--density dual lemma, elementary numerical certificate,
and obstruction audit, 2026-08-12.  The lemma improves the retained exponent
in the **one-effective-condition-per-phase-cell model** from
`0.0119000134...` to at least `0.0253912552...`.  It does not prove that
actual collateral rows compress to one condition per cell, a compact Pick
transfer, an arithmetic lower edge, a zero-free strip, or RH.

## 1. Verdict

There is a useful escape from the first Green-versus-Poisson comparison.
The completed logarithmic derivative need not be evaluated at
`1+o(1)+it`.  Evaluating it on the fixed line

```text
Re s=1.4
```

gives the same leading Poisson budget `L/2`, but a much better positive dual
majorant for the target Green potential.

Suppose, conditionally, that the actual collateral pairs have been reduced
to distinct actual-pair representatives, at most one in each ordinate phase
cell of width `2*pi/(dL)`.  Also suppose that the target cell, where the
Green kernel is logarithmically singular, has been handled with total
`exp(o(L))` loss.  Then, uniformly for

```text
0.49<=alpha<1/2,       d=0.66,
```

the complete one-product Green bill is at most

```text
0.2980087448...*L+o(L).                            (1.1)
```

The raw selected carrier is at least

```text
alpha*d*L>=0.49*0.66*L=0.3234*L.                  (1.2)
```

Thus this conditional ledger retains

```text
0.0253912552...*L.                                 (1.3)
```

This is more than twice the previous conditional reserve
`0.0119000134...*L`.  It also no longer treats the Riemann--von Mangoldt
background and the Bellotti--Wong discrepancy as independently
superposable measures: both are charged to the same positive Poisson
budget.

The qualification in the first sentence is essential.  The Poisson budget
alone does not compress several half-disk constraints in one phase cell.
Current depth-sensitive counts still allow a growing jet fan in that cell.
The new lemma closes the **global potential ledger after representative
reduction**; it does not prove that reduction.

## 2. Green and Poisson kernels

Use centered right-half-plane coordinates.  The selected depth is `alpha`,
an actual collateral reflected pair has depth `b`, and its ordinate relative
to the selected zero is `v`:

```text
0<b<=alpha<1/2.
```

Its one-factor target Green cost is

```text
G_(alpha,b)(v)
 =(1/2)*log{[(alpha+b)^2+v^2]/[(alpha-b)^2+v^2]}.  (2.1)
```

Evaluate the completed logarithmic derivative at centered real coordinate
`x>1/2`, meaning at `1/2+x+it`.  The two horizontal members of the pair
contribute

```text
K_(x,b)(v)
 =(x-b)/[(x-b)^2+v^2]
  +(x+b)/[(x+b)^2+v^2].                            (2.2)
```

For every fixed `x>1/2`, absolute convergence of `zeta'/zeta` gives,
uniformly at height `t` with `L=log|t|`,

```text
sum_(all off-line pair centers) K_(x,b_j)(t-gamma_j)
 <=(1/2)*L+O_x(1).                                 (2.3)
```

Critical-line zeros and any pairs not being charged have positive kernels,
so they may be discarded from the left side.  Notice the exact integral
normalizations

```text
integral_R K_(x,b)(v)dv=2*pi,
integral_R G_(alpha,b)(v)dv=2*pi*b.                (2.4)
```

The Fourier transforms explain both the opportunity and the danger.  Away
from frequency zero,

```text
Fourier[G_(alpha,b)](xi)
 =2*pi*exp(-alpha*q)*sinh(b*q)/q,

Fourier[K_(x,b)](xi)
 =2*pi*exp(-x*q)*cosh(b*q),       q=|xi|.          (2.5)
```

Thus exact translation-invariant deconvolution has multiplier

```text
exp[(x-alpha)q]*tanh(bq)/q.                        (2.6)
```

It is exponentially unbounded.  The lemma below succeeds by combining the
Poisson budget with the phase-cell density cap, rather than by performing
this deconvolution.

## 3. The Poisson--density dual lemma

Let an effective representative list satisfy the following two asymptotic
conditions after division by `L`:

1. every representative is attached injectively to an actual reflected
   pair, so (2.3) charges it;
2. away from the isolated target cell, at most one representative lies in
   every interval of length `2*pi/(dL)`.

The second condition implies the upper-density inequality

```text
(1/L)*sum_j phi(v_j)
 <=q_d*integral_R phi(v)dv+o(1),
q_d=d/(2*pi),                                      (3.1)
```

for every fixed nonnegative continuous integrable `phi`.  The same
conclusion holds for the logarithmic majorant used below after deleting a
fixed number of target cells; its first-cell upper sum is `o(L)`.

### Lemma 3.1 (positive dual majorant)

Fix `A<=1/2`, `x>A`, and `lambda>0`.  Put

```text
g_A(v)=(1/2)*log(1+4*A^2/v^2),                    (3.2)

k_(x,A)(v)=min{
  2*x/(x^2+v^2),
  (x-A)/[(x-A)^2+v^2]
   +(x+A)/[(x+A)^2+v^2]
},                                                 (3.3)

H_(A,x,lambda)(v)
 =[g_A(v)-lambda*k_(x,A)(v)]_+.                   (3.4)
```

For every list satisfying the two conditions above, with
`0<b_j<=alpha<=A`, its total Green cost obeys

```text
(1/L)*sum_j G_(alpha,b_j)(v_j)
 <=lambda/2
   +[d/(2*pi)]*integral_R H_(A,x,lambda)(v)dv
   +o(1).                                          (3.5)
```

#### Proof

First, `G_(alpha,b)(v)` increases with `b`; at `b=alpha` it equals
`(1/2)log(1+4*alpha^2/v^2)`, which increases with `alpha`.  Hence

```text
G_(alpha,b)(v)<=g_A(v).                            (3.6)
```

Next, direct differentiation in `b^2` shows that every interior critical
point of `K_(x,b)(v)` is a maximum.  Its minimum on `0<=b<=A` is therefore
at `b=0` or `b=A`, proving

```text
K_(x,b)(v)>=k_(x,A)(v).                            (3.7)
```

Consequently, row by row,

```text
G_(alpha,b)(v)
 <=lambda*K_(x,b)(v)+H_(A,x,lambda)(v).            (3.8)
```

Sum (3.8), use (2.3) on the first term and (3.1) on the second, and obtain
(3.5).  QED

The two endpoint kernels in (3.3) cross exactly at

```text
v_*^2=(x^2-A^2)/3.                                 (3.9)
```

This makes the remaining numerical certificate one-dimensional and
elementary.

## 4. A uniform `0.99` certificate

Take the rational parameters

```text
A=1/2,       x=0.9,       lambda=0.304.            (4.1)
```

Here `x=0.9` means that (2.3) is evaluated on `Re s=1.4`.  Equations
(3.2)--(3.4) become

```text
g(v)=(1/2)*log(1+v^(-2)),

k(v)=min{
  1.8/(0.81+v^2),
  0.4/(0.16+v^2)+1.4/(1.96+v^2)
}.
                                                        (4.2)
```

The switch point and the unique positive zero of `g-0.304*k` are

```text
v_*=sqrt(0.56/3)=0.4320493798...,
r=3.2048162900....                                  (4.3)
```

The function is positive on `(0,r)` and negative on `(r,infinity)`.  This
can be checked without numerical quadrature: its derivative on either side
of `v_*` is rational after differentiating the logarithm, and the relevant
numerator polynomials have the stated sign pattern.

An antiderivative of `g` is

```text
F(v)=(v/2)*log(1+v^(-2))+atan(v).                  (4.4)
```

Antiderivatives of the two branches of `k` are

```text
K_0(v)=2*atan(v/0.9),
K_1(v)=atan(v/0.4)+atan(v/1.4).                    (4.5)
```

Therefore

```text
integral_R [g(v)-0.304*k(v)]_+ dv
 =2*{
   F(v_*)-0.304*K_0(v_*)
   +F(r)-F(v_*)
   -0.304*[K_1(r)-K_1(v_*)]
 }
 =1.3889415384...<1.39.                            (4.6)
```

Insert (4.6) into (3.5).  At `d=0.66`,

```text
S/L
 <=0.304/2+[0.66/(2*pi)]*1.39+o(1)
 =0.2980087448...+o(1).                            (4.7)
```

Combining (4.7) with (1.2) proves the conditional reserve (1.3).
More generally, the rounded certificate is positive whenever

```text
d>0.152/[0.49-1.39/(2*pi)]
 =0.5655295684....                                  (4.8)
```

Thus it leaves substantial room inside the packet requirement
`1/2<d<2/3`.

If one optimizes the exact dual function

```text
Phi(v)=sup_(0<=b<=alpha)
       [G_(alpha,b)(v)-lambda*K_(x,b)(v)]_+         (4.9)
```

instead of separating the extrema as in (3.6)--(3.7), numerical quadrature
suggests a reserve near `0.06*L`.  That sharper number is only an
optimization diagnostic here.  The elementary rounded theorem is (4.7).

## 5. What the depth and Bellotti constraints add

The earlier ideal phase-cell ledger, using the Bellotti--Wong cumulative
mass constraint, had bill

```text
0.3234-0.0119000134=0.3114999866.                  (5.1)
```

Thus (4.7) is strictly stronger at the fixed `0.99` parameters.  It replaces
the independently overlaid background-plus-discrepancy model by the one
Poisson resource (2.3).  Intersecting the two feasible sets could only
improve the number further, but is not needed for positivity.

The depth-sensitive microscopic count does not improve the
one-representative measure at leading order.  Near depth `b`, one actual
cell may contain

```text
(1/4-b/2+o(1))*L                                   (5.2)
```

rows, whereas the compressed ledger keeps only one.  Its role is instead
to delimit the unresolved multiplicity problem before compression.

## 6. Why Poisson alone is insufficient

There is no finite pointwise constant comparing the two kernels.  For fixed
`x>alpha`,

```text
G_(alpha,b)(0)->infinity       as b->alpha,
K_(x,b)(0)->1/(x-alpha)+1/(x+alpha).               (6.1)
```

Hence a single near-tie row has bounded Poisson charge and arbitrarily large
exact-zero Green cost.

Allowing all shifted Poisson budgets does not remove this singularity by a
positive averaging argument.  If a positive measure `omega` majorizes
`G_(alpha,alpha)(v)` by translates of `K_(x,alpha)` outside only
`|v|<c/L`, then evaluation at `v=c/L` gives

```text
||omega||
 >=G_(alpha,alpha)(c/L)/K_(x,alpha)(0)
 =(log L+O(1))/K_(x,alpha)(0).                     (6.2)
```

Thus the mass of such a dual majorant diverges.  The density term in Lemma
3.1, plus explicit isolation of the singular target cell, is essential.

There is also a direct Pick warning.  Put one collateral node at the same
depth as the target and at phase `D*delta=pi`.  If a Schur function has
target value `U(alpha)=A_0>=0`, the half-disk condition at that node is
`Re U<=0`.  Schwarz--Pick gives

```text
A_0
 <=delta/sqrt(4*alpha^2+delta^2)
 =pi/(2*alpha*d*L)+O(L^(-3)).                      (6.3)
```

The Poisson cost of this row is `O(1)`.  Equation (6.3) proves that the
Poisson budget alone cannot give a height-independent Pick amplitude.  Its
loss is only polynomial, however, so it does not by itself destroy a fixed
carrier exponent.

## 7. The unresolved multiplicity/jet charge

A companion audit has since supplied the first fully quantitative growing
screen.  Two interlaced binomial chains with `K/L->c` force every scalar
Schur solution to lose at least

```text
F_(alpha,d)(c)
 =c*log[alpha*d/(2*pi*c)].                          (7.1)
```

This statement has no growing-conditioning hypothesis.  The same companion
audit integrates the reflected-pair Poisson sum over the screen's whole
fixed ordinate interval.  At `(alpha,d)=(.49,.66)` it restricts an
actual-count-compatible member of this family to

```text
c<=0.00465416431...,
F_(.49,.66)(c)<=0.0111851228....                    (7.2)
```

Thus this first rigorous growing obstruction is smaller than the new
conditional margin (1.3) by `0.0142061324...`.  This does **not** prove that
all multirow lists fit the margin: (7.1) is a forced lower loss for one
explicit adversarial family, not a universal upper construction.  See
[`ZETA23-GLOBAL-HALFDISK-PICK-BINOMIAL-AND-POISSON-AUDIT-2026-08-12.md`](ZETA23-GLOBAL-HALFDISK-PICK-BINOMIAL-AND-POISSON-AUDIT-2026-08-12.md).

The exact continuum fixture makes the remaining obstruction precise.  Fix
`d>0` and `lambda_0>0`.  For `-pi<x<pi`, put

```text
h(x)=-lambda_0+(2/d)*log cos(x/2)-i*x/d.           (7.3)
```

Then, for every integer `k>=0`,

```text
integral_(-pi)^pi exp(-i*x)*h(x)^k dx=0.           (7.4)
```

Indeed,

```text
exp(-i*x)dx
 =i*d*exp[(d/2)*(h+lambda_0)]dh,                  (7.5)
```

up to the harmless fixed positive normalization.  Closing the `h` contour
to `Re h=-infinity` turns (7.4) into the integral of
`exp(dh/2)h^k`; the closing segment vanishes exponentially.  Positive
Tchakaloff quadrature consequently gives a finite positive moment-null
quadrature for every fixed jet order.

This fixture is compatible with the Poisson budget: any `r=o(L)` rows in
one microscopic cell cost only `o(L)` in (2.3), and the depth cap (5.2)
still permits them.  What is **not** proved is a quantitative growing-order
quadrature with controlled maximal scaled depth and conditioning.  It is
therefore not a proved fixed-power counterexample to global Pick
compression.

There is a useful corrected distinction:

* fixed-order fixtures repeated in `K=L/log L` distinct consecutive cells
  do **not** cost `K log L`; their Green sum is

  ```text
  sum_(j<=K) log(L/j)
   =K*log(L/K)+O(K)
   =o(L);                                           (7.6)
  ```

* a fixed-power obstruction must instead obtain growing jet order inside
  one or a few cells, or prove that fixed local losses multiply across a
  positive-density family of cells.

Neither statement is currently available.  Thus the `0.02539*L` reserve
absorbs every presently proved sublinear distinct-cell jet bill, but no
uniform multiplicity theorem follows from the present inputs.

## 8. Exact next theorem

The global geometric task can now be narrowed to this form.

> Reduce every actual occupied phase cell to one distinct actual-pair
> representative, with total extra logarithmic loss `o(L)` (or less than
> `0.02539*L`), including the singular target cell; then realize the
> resulting causal Pick factors compactly.

Once that theorem is proved, Lemma 3.1 supplies a positive global carrier
ledger without any separate Bellotti discrepancy payment.  The arithmetic
candidate-relative lower edge remains an independent gate.

## 9. Truth table

| assertion | verdict |
|---|---|
| fixed-line logarithmic derivative gives the pair Poisson budget (2.3) | **proved** |
| Poisson plus one-per-cell density gives the dual bound (3.5) | **proved** |
| the rounded integral is below `1.39` | **proved by elementary one-variable calculation** |
| conditional one-representative bill is at most `0.298008745*L` | **proved** |
| conditional retained exponent at `(0.49,0.66)` is at least `0.025391255` | **proved** |
| Poisson budget alone controls Green cost | **false** |
| depth-sensitive count forces one representative per cell | **false** |
| an explicit count-compatible growing screen exceeds the new margin | **no for the proved binomial screen**; `0.01118513<0.02539126` |
| all extra rows have total `o(L)` jet charge | open |
| compact global Pick realization | open |
| arithmetic lower edge | open |
| uniform zero-free strip or RH | **not proved** |
