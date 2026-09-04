# QP critical defect fans: recurrence and endpoint quadruples

**Date:** 2026-08-24  
**Verdict:** at the critical flat support the Walsh/Carleson problem is now
confined to endpoint fans of effective size `H>D^(7/8)`.  Such a fan forces
`D^(3/4)` repetitions of one completion translation and
`D^(5/2)` equal-determinant four-walk collisions.  A polynomial global
trace excess also forces recurrent color matrices and a polynomial mass of
four distinct completions, so the old exact volume-plane labels really do
appear.  None of these consequences yet supplies the required global
square function: the translations, color matrices, anchor planes, and
endpoint pairs all vary.

The close-endpoint range follows from the existing theorem.  The remaining
pointwise gate is only

```text
deg(x,y)<<D^(7/8)q^o(1)                               (0.1)
```

for actual prime-power endpoints with `|x-y|>D^(3/8)`.  This weaker
codegree theorem would close the critical bin, but it is not proved here.

No new global four-cycle exponent is claimed.

## 1. Why only `H>D^(7/8)` remains

For one factor-two bin of support `M`, the refined randomized theorem is

```text
R<<D min(1,D/M)q^o(1)||z||2^4.                       (1.1)
```

The Carleson target at effective Walsh multiplicity `H` is `R_H<<D/H`.
Thus it is automatic for

```text
H<=max(1,M/D).                                        (1.2)
```

At the critical support

```text
M=D^(15/8),            R<<D^(1/8),
H_0=M/D=D^(7/8).                                      (1.3)
```

Every nonempty Walsh signature in a fixed endpoint fibre gives a distinct
nonzero defect, and there are only `O(D)` defects.  Hence the entire open
range is

```text
D^(7/8)<H<<D.                                         (1.4)
```

In particular, the old conjectural `sqrt(D)` maximum-codegree theorem is
far stronger than necessary.  The pointwise estimate (0.1) would make
(1.4) empty.

## 2. The close endpoint range is already below the threshold

The proved common-neighbor estimate for endpoint gap `g=|x-y|` is

```text
deg(x,y)
 <<(g+1)D^(1/2)+D^(13/16).                            (2.1)
```

Therefore

```text
g<=D^(3/8)  =>  deg(x,y)<<D^(7/8).                    (2.2)
```

Only the transverse range `g>D^(3/8)` is open.  There the exact reduction
is a simultaneous short-product/two-inverse problem.  If a common walk has
completion pair `(a,b)`, then

```text
h=x*a-y*b,                    0<|h|<<D,              (2.3)
```

and the common carrier is the unique prime power simultaneously completing
the two product windows.  Coprimality makes `(a,b)` unique for fixed
`(x,y,h)`, but the `O(D)` possible nonzero `h` values leave exactly the
missing `D^(1/8)` saving in (0.1).

## 3. Exact translation energy inside a high fan

Write `P_h=(a_h,b_h)` for the completion pair attached to defect `h`.
The narrow actual shell gives the exact Freiman equivalence

```text
h_i-h_j=h_k-h_l
 iff P_hi-P_hj=P_hk-P_hl.                             (3.1)
```

Indeed the difference of the two equations in (2.3) says that the two
coordinate discrepancies are an integer multiple of `(y,x)`, while twice
the shell diameter is smaller than either endpoint.

For `N>=H` fan points in an interval of `O(D)` defects, pigeonholing ordered
differences gives one nonzero translation `(alpha,beta)` represented

```text
Omega(N^2/D)>=Omega(H^2/D)                            (3.2)
```

times.  At `H>D^(7/8)`, this is `D^(3/4-o(1))`.  Every
corresponding color matrix lies in

```text
c11-c21=alpha,               c12-c22=beta.            (3.3)
```

One such plane has weighted color mass at most `||z||2^4`, but (3.2) does
not control the number of planes as the endpoint fibre varies.  Nor does a
popular difference force a long translation chain: a dense subset of a
defect interval can have its popular edges split among many short paths.

## 4. A second exact consequence: equal-determinant endpoint quadruples

For two fan points put

```text
Delta_ij=det(P_i,P_j)=a_i*b_j-b_i*a_j.               (4.1)
```

Every nondegenerate rectangle has

```text
0<|Delta_ij|<<D.                                      (4.2)
```

For a fixed signed `k`, the relation `Delta_ij=k` is a directed partial
matching.  A fixed source has at most one target, and a fixed target has at
most one source: subtracting two solutions gives a multiple of one
coprime shell pair, too long to remain inside the shell unless it is zero.
The underlying graph may contain paths, so two equal-`k` edges can share a
vertex, but only `O(r_k)` of the `binom(r_k,2)` edge pairs do so.

There are `O(D)` signed determinant values and `binom(N,2)` fan pairs.
Cauchy therefore gives

```text
sum_k #{disjoint edge pairs of determinant k}
 >>N^4/D-O(N^2).                                      (4.3)
```

At `N>D^(7/8)`, (4.3) supplies

```text
D^(5/2-o(1))                                          (4.4)
```

four-distinct-walk endpoint quadruples.  For every collision

```text
Delta_12=Delta_34=k,                                  (4.5)
```

the two-dimensional Pluecker identity becomes

```text
k^2=Delta_13*Delta_24-Delta_14*Delta_23.              (4.6)
```

This is a genuine shifted-product constraint, not merely a pigeonhole
count.  It still does not close (0.1).  Even for fixed `k`, the four other
determinants in (4.6) have `D^(2+o(1))` admissible factor labels; over the
`D` values of `k` this is a `D^(3+o(1))` label space.  The forced
`D^(5/2)` quadruples do not make one label recur.  A power saving would
require a square-function theorem across these Pluecker labels, using the
actual product completions rather than (4.6) alone.

## 5. Global FC excess forces recurrent color matrices

Let

```text
W=sum_C w(C),                    F=sum_C m(C)w(C).     (5.1)
```

The determinant-layer theorem gives `W<<D||z||2^4`.  Cauchy yields the
exact recurrence lower bound

```text
sum_C (m(C))_2 w(C)
 >=F^2/W-F.                                            (5.2)
```

Also the color matrices with `m(C)<=2` contribute at most `2W`; hence

```text
sum_(m(C)>=3)m(C)w(C)>=F-2W.                           (5.3)
```

Thus a genuine polynomial violation cannot be supported on singleton or
doubleton color matrices.  Recurrent `m(C)>=3` mass is quantitatively
forced globally, even though it is not forced inside any one endpoint fan.

There is a four-completion consequence.  Put `lambda=F/W`.  If
`lambda>=8`, the matrices with `m(C)>=lambda/2` carry at least half of `F`.
On that part,

```text
(m)_4>=lambda^3*m/128.
```

Therefore

```text
sum_C (m(C))_4 w(C)>=lambda^3 F/256.                  (5.4)
```

If `F>=D^(1+eta)||z||2^4`, then `lambda>=D^(eta-o(1))`
and (5.4) is at least

```text
D^(1+4eta-o(1))||z||2^4.                              (5.5)
```

Each term in (5.4) has the old exact four-completion volume label.  After
an anchor triangle is chosen, its plane index satisfies

```text
|t|<<D^3/q=D^(15/16+o(1)).                            (5.6)
```

Pigeonholing (5.5) over `t` gives a large fixed-index submass, but a fixed
`t` does **not** fix the anchor normal, color matrix, or affine plane.
Consequently the existing fixed-plane theorem cannot be summed from this
statement alone.

The numerical mismatch is revealing:

```text
open fan threshold       D^(7/8),
four-completion t labels D^(15/16),
difference               D^(1/16).                   (5.7)
```

The local plane-label family is still larger by precisely a sixteenth
power.  A plane square function saving that `D^(1/16)`, or an injection
which also fixes the anchor normal at subpower cost, would close this
particular route.

### 5.1 Scalar plane-label orthogonality is not that square function

Fix one anchor triangle and let `r_t` be the number of further completions
in its exact volume plane `t`.  Independent signs on the scalar plane
labels give the exact identity

```text
E_epsilon |sum_t epsilon_t*r_t|^2=sum_t r_t^2,          (5.8)
```

whereas the all-plus square is

```text
(sum_t r_t)^2
 =sum_t r_t^2+sum_(t!=u)r_t*r_u.                        (5.9)
```

Thus fixed-plane estimates see only the first term.  If `N=sum_t r_t` and
`R=max_t r_t`, then

```text
(sum_t r_t)^2/(sum_t r_t^2)>=N/R.                       (5.10)
```

In particular, proving a divisor bound in every fixed plane makes the
label-only unconditionality ratio potentially polynomial rather than
subpower.  At the critical exponents the problem is even visible before
any inequality:

```text
N>D^(7/8),                  # available t labels D^(15/16),
# labels / N =D^(1/16).                                  (5.11)
```

The scalar labels can therefore be injective on a threshold-size fan.
No fixed-anchor pigeonhole forces two fourth completions into one plane.

This failure is sharp in the integral split-quadric category.  The exact
Farey matching from the weighted-secant audit, after the determinant-one
change of normal to the four pairwise-coprime prime powers

```text
(64,71,73,81),
```

has `N=R^(2+o(1))` further completions, `R^(2-o(1))` occupied volume
labels, and

```text
max_t r_t<=tau(bc)*tau(bc-1)=R^o(1).                    (5.12)
```

Consequently its ratio in (5.10) is `R^(2-o(1))`.  Every same-fibre secant
is invertible.  The transformed carriers are not actual shell prime
powers, so this is a theorem-method obstruction, not an FC counterexample.
It proves the precise no-go needed here:

> the required `D^(1/16)` cannot come from scalar `t` orthogonality plus
> fixed-volume-plane conic bounds.

Moreover, equal `t` values belonging to different anchor triangles do not
fix one plane: the plane equation also contains the moving homogeneous
normal `N_T`.  A viable square function must therefore use the full label
`(N_T,t)` and prove bounded weighted anchor-normal overlap from the actual
product mask, or estimate the cross term in (5.9) directly.  That
mask-sensitive statement remains open.

## 6. What is and is not proved

```text
flat-bin random budget at critical support:       D^(1/8), PROVED;
automatic Walsh range:                            H<=D^(7/8), PROVED;
close endpoint gaps g<=D^(3/8):                  CLOSED;
popular translation in a high fan:               H^2/D, PROVED;
equal-determinant four-walk collisions:           H^4/D, PROVED;
polynomial FC excess => m(C)>=3 recurrence:       PROVED;
polynomial FC excess => four-completion mass:     PROVED;
scalar t-label square function closes D^(1/16):   FALSE (Farey no-go);
transverse actual-prime max codegree D^(7/8):     OPEN;
Pluecker-label square function:                   OPEN;
anchor-normal/plane Carleson packing:             OPEN;
sharp four-cycle theorem:                         NOT PROVED.
```

Executable replay:

```text
src/qp_weighted_unconditionality_audit.py
src/test_qp_weighted_unconditionality_audit.py
src/qp_residual_walsh_defect_inverse.py
src/test_qp_residual_walsh_defect_inverse.py
```
