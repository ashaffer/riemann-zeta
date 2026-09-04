# QP fixed defects: the `SL_2` BSG quotient-collision barrier

**Date:** 2026-08-24  
**Verdict:** the fixed-defect matrix encoding is exact, but the proposed
noncommutative Balog--Szemeredi--Gowers step cannot start from the centred
`h`-square function, even after arbitrary fixed high-moment amplification.

For a wedge, put

```text
G=[[a,a'],[c',c]],             det G=a*c-a'*c'=h.        (0.1)
```

After choosing one base matrix on a nonzero `h`-level, the relative matrices
really do lie in `SL_2(Q)`.  However,

```text
sum_h |<K_h z,z>|^2
```

only pairs matrices having the same **scalar determinant**.  Noncommutative
BSG needs many collisions of the full three-dimensional quotient

```text
G_1*G_2^(-1)=G_3*G_4^(-1).                            (0.2)
```

There is no implication between the two.  An exact centred star family
simultaneously attains every moment forced by a hypothetical
`D^epsilon` norm excess, while every nonidentity quotient on every
determinant level is distinct.  Its multiplicative energy is the minimum

```text
E_x=2*N^2-N,                                           (0.3)
```

so Tao's BSG theorem returns only `O(1)` points.  The first three matrices
are not contained in a translated Borel or torus packet.

This star family is an integer fixed-defect/operator countermodel, not an
actual QP counterexample: it does not obey the prime shell or cubic product
window.  A literal actual-prime audit is nevertheless hostile to the same
step.  On six prime parameters through `q=1,000,003`, all 772 populated
signed defect levels are quotient-Sidon.  The largest level has 76 literal
oriented wedges and energy `11,476=2*76^2-76`.  Thus the physical mask does
not automatically manufacture quotient collisions.  None of these finite
examples has the required asymptotic operator excess.

Even if a new mask-sensitive theorem supplied near-maximal quotient energy,
the characteristic-zero `SL_2` classification would produce unipotent or
torus cosets.  Only the unipotent affine-line outcome resembles the proved
tangent/Hankel merger.  A general torus outcome is the still-open
multiplicative/concurrent packet, and neither outcome controls the physical
carrier cells without an additional pullback theorem.

No sharp four-cycle bound is proved.

---

## 1. Exact `SL_2` normalization

Let `Omega_h` be the literal ordered wedges of defect `h!=0`, including
their common carrier and both original product-window edges.  For

```text
G,G_0 in Omega_h
```

define

```text
g_G=G*G_0^(-1)=h^(-1)*G*adj(G_0).                     (1.1)
```

Then, exactly,

```text
det(g_G)=1,             g_G in SL_2(Q).                (1.2)
```

No square root of `h` and no passage to a real approximate determinant is
needed.  Quotient equality is checked integrally:

```text
G_1*G_2^(-1)=G_3*G_4^(-1)
 iff G_1*adj(G_2)=G_3*adj(G_4),                        (1.3)
```

because all four determinants equal the same nonzero `h`.

For the physical coefficient vector, write

```text
kappa_h=<K_h z,z>=sum_(G in Omega_h) omega_G.          (1.4)
```

Here `omega_G` contains the two edge weights and
`z_c*conjugate(z_c')`.  It retains the actual common carrier.  The opposite
ray satisfies `kappa_(-h)=conjugate(kappa_h)`.

## 2. What a norm excess really gives

After the diagonal, permutation, and already-peeled coherent pieces are
removed, suppose a unit centred vector satisfies

```text
Re sum_(0<|h|<<D) kappa_h >=D^(1+2*epsilon).           (2.1)
```

There are only `D^(1+o(1))` defect values.  Cauchy and power mean give,
for every fixed integer `m>=1`,

```text
sum_h |kappa_h|^2
 >=D^(1+4*epsilon-o(1)),                               (2.2)

sum_h |kappa_h|^(2m)
 >=D^(1+4*m*epsilon-o(1)),                             (2.3)

max_h |kappa_h|>=D^(2*epsilon-o(1)).                   (2.4)
```

These are genuine consequences, but they are scalar determinant moments.
They are not multiplicative energies.

To see the distinction exactly, on one level define the quotient
correlation

```text
r_h(x)=sum_(G*G'^(-1)=x) omega_G*conjugate(omega_G').  (2.5)
```

Then

```text
|kappa_h|^2=sum_(x in SL_2(Q)) r_h(x).                 (2.6)
```

The weighted multiplicative energy needed by an inverse theorem is instead

```text
sum_x |r_h(x)|^2.                                      (2.7)
```

For indicator weights it is

```text
E_x(X_h)
 =#{(G1,G2,G3,G4) in X_h^4:
       G1*G2^(-1)=G3*G4^(-1)}.                         (2.8)
```

Thus (2.6) is the total mass of the quotient correlation, while (2.7) asks
that this mass concentrate on repeated quotients.  It may instead spread
over `asymp |X_h|^2` different points.  Raising (2.6) to the `m`th power
merely takes `m` independent quotient variables; it inserts no delta
condition equating any of them.  This is the exact quotient-collision gap.

## 3. The BSG exponent ledger

[Tao's noncommutative BSG theorem, Theorem 5.2](https://arxiv.org/abs/math/0601431)
starts from

```text
E_x(A,B)>=|A|^(3/2)*|B|^(3/2)/K.                       (3.1)
```

For `|A|=|B|=N`, it extracts subsets of size at least

```text
N/(8*sqrt(2)*K),       N/(8*K),                        (3.2)
```

whose product set has size `O(K^8*N)`.  Standard product-set conversion
then produces a `K^O(1)` approximate group.

The characteristic-zero rank-two classification is particularly strong.
The Helfgott theorem recorded in
[Breuillard--Green--Tao, Section 2](https://arxiv.org/abs/1005.1881)
says that a `K`-approximate subgroup of `SL_2(C)` is `K^C`-controlled by an
abelian `K^C`-approximate subgroup, for an absolute `C`.  Equivalently, a
successful chain ends in a unipotent group or a split/nonsplit torus, up to
polynomially many translates.

For the existing sharp packet ledger, a robust sufficient input would be

```text
E_x(X_h)>=|X_h|^3*D^(-o(1)).                            (QE)
```

It gives `K=D^o(1)`, so the extracted fraction and number of controlling
cosets remain subpower.  More generally, if an input only gives
`K<=D^(theta*epsilon)` and all classification plus physical pullback costs
`K^C_total`, the ray gain survives only if

```text
theta*C_total<2.                                      (3.3)
```

No usable `C_total` exists because the physical pullback theorem is itself
open.  The current moment ledger gives no finite `theta` at all.  In the
exact star below it gives `theta=4`; already the explicit BSG subset bound
(3.2), before classification, is only `O(1)`.

## 4. Exact centred high-moment obstruction

Fix `h!=0` and, for `1<=i<=N`, put

```text
x_i=i,       y_i=i+1,

G_(h,i)=[[h+x_i*y_i,x_i],[y_i,1]].                    (4.1)
```

Then

```text
det G_(h,i)=h.                                         (4.2)
```

All wedges share the source colour `c=1` and have private target colours
`c'=y_i`.  Their fixed-ray colour operator is therefore one directed
`N`-star.  It has singular norm `sqrt(N)` and numerical radius
`sqrt(N)/2`.

The quotients are nevertheless Sidon.  With `d=y_i-y_j`, direct
multiplication gives

```text
G_(h,i)*adj(G_(h,j))
 =[[h+x_i*d, h*(x_i-x_j)-x_i*x_j*d],
   [d,       h-x_j*d]].                                (4.3)
```

For `i!=j`, the bottom-left entry gives `d`, and then

```text
x_i=(q_11-h)/d,             x_j=(h-q_22)/d.            (4.4)
```

Thus the quotient determines the ordered pair `(i,j)`.  The identity
quotient has multiplicity `N`, and all `N*(N-1)` other quotients have
multiplicity one.  Hence

```text
E_x({G_(h,i)})=N^2+N*(N-1)=2*N^2-N,                   (4.5)

K_BSG=N^3/(2*N^2-N)=N/2+O(1).                         (4.6)
```

This is also a centred, one-vector obstruction.  Give the central colour
raw amplitude `1`, every leaf amplitude `1/sqrt(N)`, and add `L` isolated
colour coordinates of amplitude

```text
-(1+sqrt(N))/L.                                        (4.7)
```

The vector sums exactly to zero.  Its squared norm and normalized ray
quadratic are

```text
Z^2=2+(1+sqrt(N))^2/L,
<K_h z,z>=sqrt(N)/Z^2.                                 (4.8)
```

Taking `L=N^2` makes (4.8) at least `sqrt(N)/4`.  Use the same source and
target colours for every `1<=h<=H`; only the top-left entry in (4.1)
changes.  The same centred vector then works on every level.  With

```text
H asymp D,                 N asymp D^(4*epsilon),       (4.9)
```

one gets simultaneously

```text
sum_h <K_h z,z>             >>D^(1+2*epsilon),
sum_h |<K_h z,z>|^2         >>D^(1+4*epsilon),
sum_h |<K_h z,z>|^(2m)      >>D^(1+4*m*epsilon).        (4.10)
```

Every determinant level still has the minimal energy (4.5), independently
of `m`.

Nor is the family secretly one algebraic packet.  Anchor at `G_(h,1)` and
write `A_i=G_(h,i)G_(h,1)^(-1)`.  Another direct calculation gives

```text
tr([A_2,A_3])=2-4/h^3 !=2.                             (4.11)
```

The reducibility criterion for two `SL_2(C)` matrices says that trace two
is necessary and sufficient for simultaneous triangularization.  Thus the
first three matrices do not lie in one translated Borel; in particular they
do not lie in one translated torus or unipotent subgroup.

Equations (4.1)--(4.11) show that determinant equality, separable colour
weights, exact centring, norm excess, and all scalar high moments still do
not imply the BSG hypothesis.  The construction deliberately has `c=1`
and no cubic carrier mask, so it is a method obstruction rather than a QP
counterexample.  It is also not claimed to survive the project's physical
degree and tangent peels.  Its exact role is to refute an inference whose
input consists only of the centred `h`-moments; a theorem using the extra
broad-degree and cubic-mask hypotheses would be a genuinely new inverse
statement.

## 5. What classification would give if `(QE)` were proved

Suppose a new physical inverse theorem extracted from (2.1) a literal
subset `X_h subset Omega_h` which

```text
* retains D^(-o(1)) of the ray quadratic;
* satisfies (QE);
* retains each original common carrier and both product windows.         (5.1)
```

Then noncommutative BSG plus the characteristic-zero `SL_2` theorem would
cover the retained matrices by `D^o(1)` translates of an abelian subgroup.
There are two infinite outcomes.

1. **Unipotent.**  After fixed left and right changes of basis the packet is

   ```text
   P*[[1,t],[0,1]]*Q.                                  (5.2)
   ```

   This is an affine matrix line with rank-one direction.  It is the only
   outcome that directly resembles an affine/tangent/Hankel packet.

2. **Torus.**  In the split case the packet is

   ```text
   P*diag(t,t^(-1))*Q;                                 (5.3)
   ```

   the nonsplit case is a rational quadratic-torus analogue.  This is a
   multiplicative/concurrent packet.  The project has not proved a
   carrier-weighted merger for it; the affine-group audit identified
   precisely this missing Helson-type branch.

If one instead reduces modulo a finite prime and uses the finite-field
classification, its exceptional alternative is a solvable/Borel packet.
A Borel coset has the form

```text
P*[[t,s],[0,t^(-1)]]*Q,                               (5.4)
```

which imposes only one rank-one linear equation on the four wedge entries.
It is two-dimensional and is broader than one merged affine line.

Thus even the ideal group-theoretic conclusion is not synonymous with the
already proved merger.  Only (5.2), after a further physical alignment
argument, belongs to the known line packet.

## 6. Projection back to the actual mask

The map (0.1) forgets the most important external label: the carrier `b`.
For an original wedge it can be reattached from

```text
|8*b*a*c-q^3|<=q*D,
|8*b*a'*c'-q^3|<=q*D,                                 (6.1)
```

but products and controlling cosets created by BSG contain no such label.
Three further gaps remain even after a structured subset of original
matrices is retained.

* A unipotent or torus coset may meet the actual mask once in each of
  `q/sqrt(D)>>D` different carrier cells.  The proved merger needs three
  physical incidences on one short line, or a dominant physical completion
  plane.  Group control does not provide that occupancy.
* Characteristic-zero classification gives no useful height bound for the
  conjugating matrices `P,Q` or their invariant rational/quadratic lines.
  The existing gap-token estimates are height-sensitive.
* Reduction modulo `q` is not a repair.  It preserves `det G=h (mod q)` but
  aliases the size-`q^2` numerators in (1.3), forgets the real inequality
  (6.1), and can return a modular Borel whose invariant line has no small
  rational lift.

Consequently the missing theorem is not merely “large energy implies an
approximate subgroup.”  It must be a **mask-sensitive quotient-energy and
physical-pullback theorem**.

## 7. Literal prime-power audit

The executable audit constructs the exact matrix

```text
1_(|8*a*b*c-q^3|<=q*floor(q^(16/33)))                  (7.1)
```

on the width-`.2` prime-power shell, folds every ordered common-carrier
wedge by its integer defect, restores all factor orientations, and counts
the integer numerators in (1.3).  No box completion is used.

```text
q          D     signed h levels   max blocks   max wedges   energy there
25,013     135          2               1            4             28
50,021     189         14               1            4             28
100,003    265         52               6           24          1,128
200,003    371        110               6           24          1,128
500,009    579        222               8           32          2,016
1,000,003  811        372              19           76         11,476
```

Every populated level in this table is exactly quotient-Sidon:

```text
energy=2*N^2-N.                                        (7.2)
```

For the largest level, the BSG parameter is

```text
K=76^3/11,476=38.2516... .                             (7.3)
```

The scan is faithful evidence for the quotient-collision gap, but not a
counterexample to the desired estimate.  Large unnormalized support mass is
not the same as a `D^epsilon` normalized ray or global operator excess, and
the previously reported global centred norms remain below `sqrt(D)` on
these examples.

## 8. Exact remaining inverse statement

A viable `SL_2` route now needs the following new implication, with the
coefficient and carrier data present before any absolute values are taken:

```text
centred norm excess D^(1/2+epsilon)
  => a physical h-level and weighted subset X_h
     retaining a power of <K_h z,z>
  => E_x(X_h)>=|X_h|^3*D^(-o(1))
  => D^o(1) unipotent/torus cosets
  => one coset retains the actual b/residual mask
  => unipotent line merger or a new torus merger.       (INV_SL2)
```

The first two arrows are not consequences of BSG or high moments; they are
the quotient-collision theorem refuted in the abstract category by Section
4 and unsupported by the actual data in Section 7.  The last two arrows are
also new in the torus and scattered-carrier branches.

```text
fixed-defect matrix normalization into SL_2(Q):         EXACT;
norm excess => centred h-square/high moments:           EXACT;
h-square => multiplicative quotient energy:             FALSE ABSTRACTLY;
high moments repair the implication:                    FALSE ABSTRACTLY;
centred separable star obstruction:                     EXPLICIT;
star lies in one Borel/torus packet:                     NO;
near-max quotient energy needed for sharp BSG ledger:   QUANTIFIED;
char-zero approximate-group outcome:                    UNIPOTENT/TORUS;
all such outcomes covered by current merger:            NO;
literal actual-prime levels quotient-Sidon in audit:    772/772;
faithful asymptotic prime counterexample:                NOT FOUND;
mask-sensitive quotient inverse `(INV_SL2)`:             OPEN;
uniform sharp four-cycle bound:                         OPEN.
```

Exact replay:

```text
src/qp_fixed_defect_sl2_bsg.py
src/test_qp_fixed_defect_sl2_bsg.py
```
