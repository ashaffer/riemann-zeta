# The cross-prime cloud is one row, but that row is target-aligned

Status: exact scalarization, exact constraint count, exact augmented
projection criterion, and a hostile completion/large-support audit,
2026-08-11.  Pointwise prime-power nulling is proved unnecessary for a
single Weil witness.  No zero-free strip is proved.

## 1. Verdict

Fixing one lobe turns the **entire** cross-prime-power contribution into one
complex-linear functional of the other lobe.  Thus, for the purpose of
constructing one negative Weil direction, it is enough to impose one real
equation; one complex equation is a convenient stronger condition.  The
`O(X/L)` individual prime-translate equations used in the earlier proposal
are sufficient but not necessary.

Consequently the independent Wiener-atomic interpolation problem created by
pointwise prime nulling is not an intrinsic gate.  It should not be listed as
a second theorem which must be solved after the zero rows.

This does **not** finish the construction.  After the positive-zero rows are
imposed, the one aggregate arithmetic row can be parallel to the selected
negative row.  The explicit formula explains why this is the natural bad
case: the completed arithmetic operator and the complete zero operator are
the same operator.  In the ideal quotient in which one selected negative
pair is the only power-sized spectral term, their off-diagonal lobe blocks
are exactly the selected target rank-one block.  Cancelling the completed
aggregate cross term then cancels the two-lobe carrier itself.

The corrected missing condition is therefore one augmented target angle,
not a prime-atomic frame theorem:

```text
positive-zero rows + one aggregate arithmetic row
must leave a subpower-cost direction with the target carrier.            (1.1)
```

Neither dimension, Riemann--von Mangoldt, the current Zeta23 moments, KMT,
nor an ordinary mean square proves (1.1).  This is a major simplification of
the bookkeeping, but not yet a strip.

## 2. Exact orientation and conjugation audit

Let the disjoint physical lobes be ordered as

```text
I_- < I_+,
f=ell+r,             supp ell subset I_-,
                     supp r   subset I_+.
```

Use the exact correlation convention

```text
R_f(y)=integral f(u)*conj(f(u+y))du.                 (2.1)
```

For `y>0` in the cross-difference interval `I_+-I_-`, only the left-to-right
orientation survives:

```text
R_f(y)=R_ell(y)+R_r(y)
       +integral ell(u)*conj(r(u+y))du.              (2.2)
```

The opposite orientation is not missing.  It is exactly
`R_f(-y)=conj(R_f(y))`, and the completed prime formula already takes the
real part.  Put

```text
Lambda_(pr,r)(ell)
 =sum_(n: log n in I_+-I_-)
    Lambda(n)/sqrt(n)
      *integral ell(u)*conj(r(u+log n))du.           (2.3)
```

Every prime power is present in (2.3).  With the sign convention

```text
Q(f)=Pole(f)+Arch(f)-Prime(f),
Prime(f)=2*sum_n Lambda(n)/sqrt(n)*Re R_f(log n),    (2.4)
```

the exact cross-prime term is

```text
Q_(pr,cross)(ell,r)=-2*Re Lambda_(pr,r)(ell).        (2.5)
```

Thus `Re Lambda_(pr,r)(ell)=0` is the minimal one-real-equation
cancellation.  Imposing `Lambda_(pr,r)(ell)=0` is one complex-linear row.
No coefficientwise equation appears in (2.5).

There is one real-descent caveat.  If `ell+r` is first constructed in the
complexified real coefficient space, negativity of the **total** completed
form descends to its real or imaginary part.  The separate equation
`Lambda_(pr,r)(ell)=0` need not descend to either part: the two real parts of
the complex packet can have nonzero prime contributions which cancel only
after their total forms are added.  Thus complex polarization is legitimate
for proving a negative real direction, but it does not certify a separately
prime-null real witness.  Every estimate below is consequently an estimate
of the complex packet's total form before that final descent.

The completion has the same scalar form.  Write

```text
A_+(f)=integral f(t)e^(t/2)dt,
A_-(f)=integral f(t)e^(-t/2)dt.
```

Since `Pole(f)=2*Re(A_+(f)*conj(A_-(f)))`, its cross term is

```text
2*Re Lambda_(pole,r)(ell),

Lambda_(pole,r)(ell)
 =A_+(ell)*conj(A_-(r))+A_-(ell)*conj(A_+(r)).       (2.6)
```

If the archimedean form is written with its real multiplier `m` as

```text
Arch(f)=integral m(xi)*abs(F_f(xi))^2 dxi,
```

then its cross term is

```text
2*Re Lambda_(arch,r)(ell),

Lambda_(arch,r)(ell)
 =integral m(xi)*F_ell(xi)*conj(F_r(xi))dxi.         (2.7)
```

Consequently all completed cross terms together are the single scalar

```text
Q_cross(ell,r)
 =2*Re Lambda_(comp,r)(ell),

Lambda_(comp,r)
 =Lambda_(pole,r)+Lambda_(arch,r)-Lambda_(pr,r).     (2.8)
```

Equivalently, if `K_comp` is the Hermitian completed operator and `P_-` is
the left-lobe projection, its Riesz row is simply

```text
g_r=P_-*K_comp*r,
Lambda_(comp,r)(ell)=<ell,g_r>.                     (2.9)
```

Equations (2.2)--(2.9) retain both orientations, conjugation, every prime
power, both pole evaluations, and the archimedean multiplier.  One may keep
the pole and archimedean cross terms as separately bounded remainders, impose
one row on each, or combine all of them into (2.8).  Even the last option is
only one complex row.

Independent complex polarization remains legitimate.  If the completed
matrix `K` is real symmetric and `z=x+i*y`, then

```text
conj(z)^T*K*z=x^T*K*x+y^T*K*y.                      (2.10)
```

Therefore a negative total form for the complex two-lobe witness yields a
negative admissible real witness, `x` or `y`.  The aggregate cancellation
need not descend separately to that real component; only the total identity
(2.10) is used.

## 3. Correct constraint count and exact augmented projection

Let `E_-` be the allowed complex free-lobe space after endpoint jets and
support/leakage restrictions.  Fix `r`.  Let

```text
A:E_- -> C^p
```

be the restrictions of the `p` off-line positive rows, and let

```text
b=-A_+*r                                               (3.1)
```

be the datum which makes every full positive coordinate of `ell+r` vanish.
Let `g` be the Riesz vector of whichever aggregate scalar is to be cancelled
(raw prime, pole-prime, or the fully completed cross scalar).  The exact
complex-linear feasible set is

```text
F_r={ell in E_-: A*ell=b, <ell,g>=0}.                (3.2)
```

Thus the count is

```text
p positive-zero rows + 1 aggregate row,             (3.3)
```

not `p+#prime-powers+O(1)`.  If only the real part in (2.5) or (2.8) is
cancelled, the last item is one real constraint rather than one complex
constraint.

There is an exact quantitative criterion.  Assume `A*ell=b` is feasible,
let `ell_0=A^dagger b` be its minimum-norm solution, and put

```text
S=ker A,                g_S=P_S*g.                   (3.4)
```

The aggregate equation is feasible precisely when either `g_S` is nonzero,
or it is zero and `<ell_0,g>=0`.  When `g_S` is nonzero, its minimum extra
norm is

```text
abs(<ell_0,g>)/norm(g_S).                            (3.5)
```

After one such correction the remaining homogeneous freedom is

```text
S_g=S intersect g^perp.                             (3.6)
```

For the free-lobe restriction `a` of the selected negative row,

```text
norm(P_(S_g)*a)^2
 =norm(P_S*a)^2
  -abs(<P_S*a,g_S>)^2/norm(g_S)^2.                  (3.7)
```

Formula (3.7) is the exact replacement for the Wiener-atomic extremal.  One
new row can remove **all** homogeneous target leverage when
`P_S*a` is parallel to `g_S`.  A large value of `dim S` gives no lower bound
for the angle in (3.7), and it gives no lower bound for the denominator in
(3.5).  The same conclusion holds for the minimal real constraint: an
all-real selected-pair model makes that one real row exactly the carrier
quadrature.

## 4. Why completion makes target alignment natural

Let `K_zero` be the complete zero-side operator in the same finite packet
space.  The explicit formula is the operator identity

```text
K_comp=K_zero.                                      (4.1)
```

In hyperbolic pair coordinates it has the schematic exact decomposition

```text
K_zero=K_on+2*sum_j (x_j*x_j^*-y_j*y_j^*),          (4.2)
```

where `x_j` is the positive row and `y_j` the negative row of the reflected
off-line pair.  Splitting every row between the two lobes gives

```text
P_-*K_comp*r
 =P_-*K_on*r
  +2*sum_j [x_j^-*conj(<r,x_j^+>)
            -y_j^-*conj(<r,y_j^+>)].                (4.3)
```

For the selected pair `j=0`, (4.3) contains the rank-one vector

```text
-2*y_0^-*conj(<r,y_0^+>),                           (4.4)
```

which is exactly parallel to the selected target row and has exactly the
two-lobe carrier scale.

This supplies a sharp hostile model.  Quotient out the positive rows and
suppose the selected negative pair is the only power-sized remaining zero
term.  Then (4.3) is, at that scale, just (4.4).  The completed aggregate
condition `<ell,P_-K_comp r>=0` is the condition that the selected negative
cross carrier vanish.  In the literal one-pair model the alignment is exact,
not merely an ill-conditioned possibility.

Cancelling only the raw prime scalar at the additive edge is still a
legitimate operation.  There the pole and archimedean cross terms are
power-negligible under the already audited absolute-frequency and endpoint
hypotheses.  But (4.1) then says that the raw prime row differs from the
target-aligned zero row only by those small completed rows.  Their smallness
makes the alignment sharper; it does not produce an independent reservoir.

Other on-line zeros belong to the positive Gram block and may in principle
act as a reservoir, but their count gives neither the generalized leverage
nor the target angle needed to show that they do so at subcarrier cost.
They cannot simply be declared negligible; charging their positive Gram
energy leads to the same augmented Schur quotient.  Other off-line rows can
also be power-sized, but using them is exactly the unresolved
signed/confluent screening problem.  Thus the possible escape in (3.7) is
not a free prime-side dimension fact.

## 5. The tempting mean-square reservoir does not certify the angle

In relative Fourier coordinates the aggregate cross scalar is diagonal:

```text
Lambda_(comp,r)(ell)
 =sum_k E_Y(tau_k)*conj(ell_k)*r_k,                  (5.1)
```

up to the harmless convention for conjugating all three factors.  Here
`tau_k` is the **absolute** prime phase.  The target core has relative
frequency near zero but absolute phase `tau_k` near the hypothetical zero
ordinate `gamma`.  In the Zeta23 carrier all permitted absolute phases stay
in `[T,2T]` (or a fixed comparable interval).

This kills the most attractive two-mode argument.  The coherent value at
absolute phase zero is not an admissible reservoir.  Moreover, after pole
centering that coherent main term is cancelled by the continuum anyway.

For the asymmetric additive-edge geometry `Y=T^d`, `d<1`, the ordinary
Montgomery--Vaughan mean square on a legal interval of length comparable to
`T` gives only the root-mean-square scale

```text
(1/T)*integral_T^(2T) abs(E_Y(t))^2dt asymp log Y,   (5.2)
```

for a fixed smooth prime window (the continuum is negligible there).  Thus
it certifies a legal value of size at least `sqrt(log Y)`, not `sqrt(Y)`.
At the target phase the audited pointwise input gives only

```text
abs(E_Y(gamma)) << sqrt(Y)/(log Y)^(3/10).           (5.3)
```

Using (5.2) as the denominator for (5.3) can therefore cost a fixed
half-power.  If the hypothetical zero itself makes the target-phase value
of order `Y^alpha`, the same correction costs `Y^alpha` up to logarithms.
Neither estimate is subpower.

There are two further losses.  A single absolute Fourier mode is not a
physical endpoint lobe, and projecting the reservoir through the endpoint
space and `ker A` can only decrease its norm.  Current mean-square inputs do
not show that any fixed portion of (5.2) survives that projection.  The
reservoir proposal therefore does not prove either denominator or angle in
(3.5)--(3.7).

## 6. A larger support does not bypass the completed row

Dropping the individual prime constraints makes it natural to try

```text
L=C*log T,             X=T^C,                       (6.1)
```

with a free lobe of fixed physical width `A*log T` and a short seed.  The
formal ledger is attractive: a pair of depth

```text
alpha=1/2-delta
```

has cross residue of size

```text
X^alpha=T^(C/2-C*delta),                             (6.2)
```

whereas the same-lobe prime support costs only `T^(A/2+o(1))`.  Increasing
`C` can also dominate some fixed-order or `C^q` confluent costs.

The pole/main cross scale at phase `gamma asymp T`, before an exact pole
null, has the standard absolute bound

```text
X^(1/2)/T=T^(C/2-1).                                 (6.3)
```

The ratio of (6.2) to (6.3) is

```text
T^(1-C*delta).                                      (6.4)
```

This gives a useful no-free-parameter dichotomy.

1. If `C*delta>1`, the available absolute pole budget is larger than the
   target, so raw-prime cancellation plus a separate crude pole bound does
   not close.
2. If `C*delta<1`, the target can dominate that pole budget.  After the
   collateral zero rows have been quotiented out or controlled, however,
   the raw prime row equals the target-aligned completed zero row up to a
   smaller pole/archimedean correction.  Without that collateral control,
   those rows are themselves the unresolved screening term.  In either
   formulation the augmented angle (3.7), not the support exponent, is
   decisive.
3. At `C*delta=1` there is no power margin.

One can impose exact pole cancellation instead of using (6.3), but that
only adds a finite row.  Imposing both the raw-prime and pole cross nulls
makes the completed cross null (up to the separately treatable archimedean
row), and (4.1)--(4.4) return verbatim.  It cannot be justified by counting
dimensions while retaining the selected carrier.

The arithmetic reservoir also worsens under (6.1).  For `C>1` the prime
length exceeds the ordinate aperture.  The separated-frequency lower
mean-square regime used in (5.2) is no longer available, and the KMT
transition estimate audited at `X=T^(1+o(1))` does not extend to this range.

Thus a large `C` may still be useful inside a future **coupled** zero-row and
aggregate-row theorem, but it does not by itself prove that theorem.  The
exact point at which the argument becomes circular is the assertion that
the completed row in (4.3) has a target-neutral reservoir of sufficient
size: after all smaller zero terms are controlled, its leading vector is
the target (4.4).

## 7. Corrected conditional theorem card

Fix an asymmetric two-lobe geometry and a seed `r`.  Suppose uniformly at
every hypothetical deepest pair that:

1. the positive-row system `A*ell=b` has a collision-stable solution of
   subpower cost;
2. after adjoining the single raw-prime aggregate row (and any separately
   exact pole row), the augmented system remains feasible at subpower cost;
3. the affine target value and the homogeneous leverage in (3.7) retain the
   required negative carrier up to a subpower factor; and
4. same-lobe prime, pole, archimedean, on-line, and remote terms are
   little-o of that retained carrier.

Then the earlier exponent comparison gives the corresponding conditional
zero-free edge.  This statement uses one aggregate arithmetic row and no
individual prime-power nulls.

Items 2--3 are not an independent Wiener-atomic conjecture.  Together with
item 1 they are one target-conditioned augmented Schur/Hermite theorem.
The operator identity (4.1) shows why proving them is already genuinely
zeta-specific.  No current result in the repository proves these items, so
no unconditional edge follows.
