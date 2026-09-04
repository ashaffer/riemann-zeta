# QP four-cycle: Peller/log-Hankel hostile audit

**Date:** 2026-08-22  
**Verdict:** scalar logarithmic coordinates do not turn the QP matrix into a
classical Hankel operator at the norm level needed for the four-cycle bound.
They turn it into a **Helson matrix on a nonuniform atomic measure**.  The
arithmetic sampling scale is smaller than the log-node spacing, and both
standard ways of replacing that atomic measure by Lebesgue measure lose a
power of `q`.

At the project scale

```text
D=q^(16/33),              epsilon=D/q^2=q^(-50/33),
log-node gap asymp 1/q,   epsilon/gap=D/q=q^(-17/33).       (0.1)
```

For one color, the exact integer matrix is a partial matching with only
`D q^o(1)` edges.  Global uniformization of the log grid fills the whole
anti-diagonal and gives fourth Schatten mass `asymp q`.  The full continuous
Hankel pulse, normalized so that its compression has unit entries, has
fourth Schatten mass at least `asymp epsilon^(-1)=q^2/D`.  Thus the natural
comparison ladder is

```text
actual sampled layer:          D q^o(1),
uniform discrete Hankel layer: q,
continuous Peller pulse:       q^2/D.                       (0.2)
```

The losses relative to the first line are respectively `q/D=q^(17/33)`
and `(q/D)^2=q^(34/33)`.  Peller's `S_4 <-> B_4^(1/4)` theorem therefore
does not prove

```text
||A_z||_S4^4 << D q^o(1) ||z||_2^4.                         (0.3)
```

Local log linearization is valid only on blocks of length `sqrt(D)`.  On
exactly that scale the merged affine/Hankel patch estimate already proves
the desired `O(D)` budget.  Summing the scattered blocks is the existing
slope-block / outer-fan gate.  No counterexample to the direct conjecture is
found here; the result is a proof-method obstruction.

---

## 1. Exact Helson form and the two microscopic scales

Put

```text
X=q^3/8,                  H asymp qD,
alpha(n)=z_c if |8*n*c-q^3|<=qD, and 0 otherwise.            (1.1)
```

All variables lie in fixed proportional `q`-shells.  For fixed `n=ab`, the
admissible interval for `c` has length `O(D/q)<1`, so `c` is unique.  Hence

```text
A_z(a,b)=alpha(a*b).                                         (1.2)
```

This is exactly a finite compression of a multiplicative Hankel (Helson)
matrix.  If

```text
x_a=log(a/q),          t_c=log(X/(c*q^2)),                   (1.3)
```

then the color-`c` support lies in

```text
|x_a+x_b-t_c| << epsilon,       epsilon=D/q^2.               (1.4)
```

But consecutive nodes obey

```text
x_(a+1)-x_a = 1/a+O(q^-2) asymp 1/q.                        (1.5)
```

Thus (1.4) is a sub-grid pulse, thinner than the mesh by `D/q`.  Calling
the grid "quasiuniform" does not remove this scale separation: the support
is decided by the fractional position inside each mesh cell.

For a fixed color and fixed row `a`, the admissible interval for `b` also
has length `O(D/q)<1`; the same holds with rows and columns exchanged.  The
color layer `P_c` is therefore a partial permutation.  Moreover its products
`n=ab` lie in an interval of `O(D)` integers, and every such integer has
`q^o(1)` divisors.  Consequently

```text
||P_c||_S4^4 = #edges(P_c) << D q^o(1).                     (1.6)
```

This is already the sharp one-color budget.

## 2. Why a global discrete Peller model loses `q/D`

For an ordinary Hankel matrix

```text
H_gamma(i,j)=gamma_(i+j),                                   (2.1)
```

take a symbol with one nonzero coefficient, `gamma_N=1`.
The finite matrix is the reversal partial permutation on the anti-diagonal
`i+j=N`, so exactly

```text
||H_gamma||_S4^4 = N+1.                                    (2.2)
```

On a global log grid there are `asymp q` mesh points.  Replacing the
nonuniform nodes (1.5) by a uniform arithmetic progression turns one thin
color pulse into an anti-diagonal of length `asymp q`; (2.2) costs `q`, not
`D`.  Peller's theorem faithfully records this: the analytic symbol with one
coefficient at height `N` has `B_4^(1/4)` norm to the fourth comparable to
`N`.  The theorem is not losing anything; the global uniformization has
filled the `q-D` crossings which integer point sampling rejects.

The Taylor expansion makes the largest legitimate uniform block exact.  If
`a=a_0+i`, then

```text
log((a_0+i)/a_0)=i/a_0-i^2/(2*a_0^2)+O(|i|/q^2+|i|^3/q^3). (2.3)
```

The quadratic error stays inside (1.4) only when

```text
i^2/q^2 << D/q^2,             hence |i|<<sqrt(D).            (2.4)
```

This recovers precisely the known tangent packet scale.  On a
`W`-by-`W` block with `W<=sqrt(D)`, every color is a partial matching and

```text
||A_block||_HS^2 <= W ||z_block||_2^2,
||A_block||_S4^4 <= W^2 ||z_block||_2^4 <= D||z_block||_2^4. (2.5)
```

What is missing is a `q^o(1)`-overlap merger of all such blocks.  Scalar
Peller theory does not supply it.

## 3. The full continuous pulse is even more expensive

There is a second possible transference: replace the counting measure on
the nodes by Lebesgue measure and realize the entries as a compression of an
integral Hankel operator.  The normalization is hostile.

Let `0<epsilon<1/8` and on `L^2([0,1])` consider

```text
(Gamma_epsilon f)(x)
  = integral_0^1 k_epsilon(x+y) f(y)dy,
k_epsilon(t)=epsilon^(-1) 1_(|t-1|<=epsilon).                (3.1)
```

The height `epsilon^(-1)` is forced if intervals of width at most
`epsilon` around sampled nodes are to have matrix coefficient of order one.
The positive fourth-trace formula is

```text
||Gamma_epsilon||_S4^4
 = integral k(x+y)k(x'+y)k(x'+y')k(x+y') dxdx'dydy'.        (3.2)
```

Restrict (3.2) to

```text
1/4<=x<=3/4,
|x'-x|<=epsilon/4,
|x+y-1|<=epsilon/4,
|x+y'-1|<=epsilon/4.                                        (3.3)
```

All four kernel factors in (3.2) then equal `epsilon^(-1)`.  The region
has volume `epsilon^3/16`, and therefore

```text
||Gamma_epsilon||_S4^4 >= 1/(16*epsilon).                   (3.4)
```

With (0.1), (3.4) is `q^2/(16D)`.  Compared with (1.6), the full Peller
operator has lost `(q/D)^2` up to constants and divisor factors.

Using mesh cells of width `1/q` instead does not fix this.  A thin continuum
line crosses every cell square along its anti-diagonal, whether or not it
passes within `epsilon` of the chosen lattice point.  Compression to
cell-constant functions gives the middle line of (0.2).  Using cells of
width at most `epsilon` retains the point sampling, but then the full norm
obeys (3.4).  These are the two sides of the same sampling obstruction.

## 4. Nonuniform log-Hankel matrices are Helson, not classical Hankel

The correct Hilbert space is

```text
L^2(mu_q),             mu_q=sum_(a in shell) delta_(log a), (4.1)
```

and the operator kernel is `h(x+y)` on this atomic measure.  Classical
Peller theory concerns Lebesgue measure on a half-line, or equivalently the
one-variable Hardy space with index semigroup `N_0`.  Here the index
semigroup is multiplicative.  Under the Bohr lift,

```text
n=prod_p p^(kappa_p)  <->  kappa(n) in N_0^(infinity),       (4.2)
```

so (1.2) is a small Hankel operator in countably many variables.  There is
no scalar `B_4^(1/4)` characterization of general Helson matrices.

The distinction is already finite and exact.  Choose distinct primes
`p_1,...,p_N` in the shell.  Unique factorization gives

```text
log(p_i)+log(p_j)=log(p_k)+log(p_l)
       iff {i,j}={k,l}.                                     (4.3)
```

Thus, for every symmetric `N`-by-`N` matrix `B`, a smooth one-variable
function can be interpolated at the finitely many distinct sums so that

```text
h(log p_i+log p_j)=B_ij.                                    (4.4)
```

Nonuniform sampled "Hankel" structure alone therefore imposes no matrix
norm restriction at all.  The interpolation Besov norm must carry the
entire difficulty, and sub-grid interpolation incurs the costs in Sections
2--3.

This agrees with the general Helson literature.  Brevig--Miheisi prove that
the natural Hilbert--Schmidt projection onto Helson matrices is unbounded on
every Schatten `S_p` with `p!=2`, in particular on `S_4`; see
<https://arxiv.org/abs/1908.04521>.  Their tensor-product counterexamples
are not QP-shell counterexamples, but they rule out importing the bounded
one-variable Hankel projection as a dimension-free black box.  Peller's
classical criterion itself is stated, for example, in
<https://arxiv.org/abs/2402.09853>.

## 5. What survives discretely

The failure of scalar Peller transference does leave two useful discrete
statements.

### 5.1 A rigorous color-degree stratification

Let `P_c` be the color-`c` layer and let `m_c` be its number of entries.
Every `P_c` is a partial permutation.  On a dyadic class

```text
M/2 < m_c <= M,
A_M=sum_c z_c P_c,                                  (5.1)
```

the disjoint entry supports and the triangle inequality give

```text
||A_M||_HS^2 <= M||z_M||_2^2,
||A_M||_op   <= ||z_M||_1.                          (5.2)
```

Consequently

```text
||A_M||_S4^4
 <=||A_M||_op^2||A_M||_HS^2
 <=M||z_M||_2^2||z_M||_1^2.                        (5.3)
```

There are only `O(log q)` nonempty classes.  Applying the `S_4` triangle
inequality and `(sum x_j)^4<=r^3 sum x_j^4` proves the unconditional profile

```text
||A_z||_S4^4
 <<q^o(1) sum_M M||z_M||_2^2||z_M||_1^2.           (5.4)
```

Thus one dyadic class satisfies the target whenever

```text
M * (||z_M||_1^2/||z_M||_2^2) <= D q^o(1).         (5.5)
```

This simultaneously covers one high-degree color and one
`sqrt(D)`-color tangent packet.  It does not close a vector flat on `D`
colors each having degree `D`; (5.3) then gives `D^2`.  Mixing all degrees
before taking `||A||_op^2||A||_HS^2` is also invalid as a proof principle:
a disjoint union of a high-degree one-color matching and a lower-degree
tangent packet can have its Hilbert--Schmidt norm controlled by the former
and its operator norm controlled by the latter.  The two pieces separately
obey the desired fourth-trace budget while their unstratified product can be
polynomially larger.

### 5.2 Approximate fixed-slope packets cannot repeat too often

There is a sharp packing fact beyond the previously recorded exact
stationary-chart uniqueness.  Consider a centered affine row slice

```text
a_i=A+P*i,       b_i=B,       c_i=C-S*i,       |i|<=L,        (5.6)
```

and suppose the three products at `i=0,+L,-L` all lie in a common target
window `|abc-X|<=H`, where `H asymp qD` and `A,B,C asymp q`.
The exact endpoint increments are

```text
(A+P*L)B(C-S*L)-ABC
 =B[L(PC-AS)-PSL^2],
(A-P*L)B(C+S*L)-ABC
 =B[-L(PC-AS)-PSL^2].                               (5.7)
```

Subtracting and adding (5.7) prove

```text
|PC-AS| << D/L,              P*S*L^2 <<D.           (5.8)
```

Here is the precise packing statement, including the distinction between
interval-disjoint and merely node-disjoint packets.

> **Approximate fixed-slope packet lemma.**  Let `X,H,B_min>0` and fix
> positive integers `P,S,L,C`.  Suppose a collection of pairs `(A_nu,B_nu)`
> has `B_nu>=B_min`, all displayed factors are positive, and
>
> ```text
> |(A_nu+P*i) B_nu (C-S*i)-X|<=H,
>                         i=-L,0,L.                 (5.9)
> ```
>
> Then every packet obeys
>
> ```text
> |P*C-A_nu*S| <=2H/(B_min*L),
> P*S*L^2      <=2H/B_min.                         (5.10)
> ```
>
> If the convex hull intervals
> `[A_nu-P*L,A_nu+P*L]` are pairwise disjoint, their number `N` satisfies
>
> ```text
> N*L^2 <=4H/(B_min*P*S).                          (5.11)
> ```
>
> If only the arithmetic-progression node sets
> `{A_nu+P*i:|i|<=L}` are pairwise disjoint, then
>
> ```text
> N*L^2 <=4H/(B_min*S).                            (5.12)
> ```

Indeed, the first inequality in (5.10) confines every possible center `A`
to an interval of length

```text
R=4H/(B_min*S*L).                                    (5.13)
```

For convex-hull-disjoint packets the centers are separated by at least
`2PL`, so

```text
N<=1+R/(2PL).                                        (5.14)
```

Multiplying by `L^2` and using the curvature inequality in (5.10) proves
(5.11).  Merely node-disjoint progressions can interleave in `P` residue
classes.  Inside each fixed class modulo `P`, disjoint centers are separated
by `(2L+1)P`.  Hence

```text
N<=P+R/(2L+1),                                      (5.15)
```

and (5.12) follows the same way.  The second statement is weaker by the
unavoidable residue factor `P`; this is important when specifying a packet
cover.

The same argument applies on the carrier axis.  In the project shell,
`H/B_min=O(D)`.  Therefore (5.11) says that the dangerous repeated-Latin
pattern cannot be built from convex-hull-disjoint **approximate** affine
packets having the same canonical slope/color data: shorter packets may
repeat more often, but exactly in inverse proportion to their local
`S_4` budget.

There is no hidden polynomial loss in the step summation.  Once
`D/L=o(q)` (automatic here), (5.10) and `A,C asymp q` force `P asymp S`.
For one comparable dyadic step scale `R<=P,S<2R`, exactly

```text
sum_(P,S) 1/(P*S)
 =(sum_(R<=n<2R)1/n)^2 <=1.                        (5.16)
```

Curvature restricts the number of scales to `O(log D)`.  Thus the right
side of (5.11), summed over all comparable dyadic `(P,S)`, is
`O(D log D)`.  This summation applies to the convex-hull-disjoint canonical
packet sector.  For interleaved node-disjoint packets only (5.12) is
available; those residue classes must first be merged or separately charged.

Combining the lemma with the already proved same-base short-direction
uniqueness gives a rigorous extension of the closed affine sector under
explicit cover hypotheses.  Fix the canonical color center/progression.
If its coherent component is decomposed into row-and-column
convex-hull-disjoint centered affine packets, their matrices are direct
blocks; the local merged-Hankel estimate costs `O(L^2)` per packet, and
(5.11)--(5.16) sum all approximate repeats to `D q^o(1)`.  Exact
stationarity is no longer required.  Distinct color centers may also be
summed when their color supports have `q^o(1)` overlap, because the local
bound is quadratic in the color `L^2` mass.

This is a **sector theorem**, not a new global exponent.  Same-base
uniqueness assigns a direction only after a base pair is fixed.  It does
not prove bounded overlap of the resulting color centers, produce a cover
of the scattered reciprocal-rounding array, or control cross terms between
overlapping/interleaved packets and different bases.

This is not yet a global proof.  One still needs an inverse/cover theorem
which assigns every coherent part of the reciprocal-rounding array to
canonical packets of the form (5.6), and an almost-orthogonal merger for
overlapping packets and cross terms.  Peller theory proves neither step.

## 6. Exact status

```text
exact Helson/log representation:                    PROVED;
sub-grid pulse ratio epsilon/(1/q)=D/q:             PROVED;
one-color actual layer S4^4 << D q^o:               PROVED;
global uniform Hankel one-color cost asymp q:        PROVED;
normalized continuum pulse cost >= q^2/(16D):       PROVED;
valid scalar-Hankel chart radius sqrt(D):            PROVED;
local merged chart S4^4 << D||z||_2^4:              PROVED;
dimension-free Peller/Helson transference:           FALSE GENERALLY;
degree-stratified bound (5.4):                       PROVED;
fixed-slope approximate packet packing (5.11):       PROVED;
QP scattered-chart merger / slope-block theorem:    OPEN;
full-integer direct multiplicative-Hankel conjecture: OPEN;
uniform four-cycle bound:                            OPEN.
```

The scale identities and finite anti-diagonal checks are replayed by
`src/qp_peller_log_hankel_audit.py` and
`src/test_qp_peller_log_hankel_audit.py`.
