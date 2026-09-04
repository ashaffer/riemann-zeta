# QP four-cycle: collective dyadic gate and hostile route audit

**Date:** 2026-08-28
**Status:** exact reduction and route correction; **the sharp four-cycle bound
is not proved**.

## 0. Verdict

The proposed signed-dyadic determinant theorem survives as an exact
localization, but it fails the test for being a genuinely easier next lemma.
It is equivalent, up to `q^o(1)`, to the full positive completion-pair
endpoint.

The audit also falsifies the old rootwise reconstruction.  A bound for one
root, followed by a maximum over roots, does not control the collective
positive mass.  A rooted approach remains possible only if it supplies a
weighted square-function or direct-sum reconstruction theorem.

The corrected route ranking is therefore:

1. retain the rank-one Cartesian color masks and attack the factorial
   secant form directly;
2. use peeling only to extract a genuinely dangerous two-sided core;
3. classify that core into tangent/scattered packets and prove **weighted
   packet participation**, not a bound for the number of packets;
4. use a rooted or capacitary theorem only after its collective
   reconstruction is part of the statement.

Signed dyadic bucketing is useful bookkeeping inside this program.  It is
not itself the missing mathematics.

## 1. Exact positive endpoint

Let `C=(c11,c12;c21,c22)` run over the generic oriented color matrices and
let `X(C)` be its actual-shell carrier completions

```text
X=(a1,a2,b1,b2).
```

Write

```text
w_z(C)=|z_c11 z_c12 z_c21 z_c22|,
m(C)=|X(C)|.
```

After the proved diagonal and repeated-coordinate reductions, the missing
positive quartic is

```text
P(z)=sum_C m(C)(m(C)-1) w_z(C)
    << D q^epsilon ||z||_2^4                         (PAIR_epsilon)
```

for every positive `epsilon`.  This implies the sharp four-cycle estimate
by the already proved quadratic bootstrap.

For an ordered pair `X != X'`, define the signed carrier secants

```text
A(X,X')=a1*a2'-a2*a1',
B(X,X')=b1*b2'-b2*b1'.                              (1.1)
```

The generic reductions prove

```text
1 <= |A(X,X')|, |B(X,X')| <= C*D                    (1.2)
```

for an absolute shell constant `C`.

## 2. The frozen signed-dyadic theorem

For signs `sigma,tau` in `{+1,-1}` and integers `j,k>=0`, put

```text
C_(sigma,tau,j,k)
 ={(C,X,X'):
     X,X' in X(C), X!=X',
     2^j <= sigma*A(X,X') < 2^(j+1),
     2^k <= tau*B(X,X') < 2^(k+1)}.                 (2.1)
```

The precise proposed theorem was

```text
sum_((C,X,X') in C_(sigma,tau,j,k)) w_z(C)
  <= C_epsilon D q^epsilon ||z||_2^4                (DSP_epsilon)
```

uniformly in the two signs and two levels.

This statement has the right variables, signs, weights, and generic-sector
quantifiers.  In particular, it does not use the undefined `P_t` notation
from the preliminary multiroute report.

## 3. DSP is equivalent to PAIR, not a strict intermediate theorem

The implication `PAIR_epsilon => DSP_epsilon` is immediate: every term is
nonnegative and one cell is a subsum of `P(z)`.

Conversely, (1.2) gives at most

```text
N_cells <= 4*(1+floor(log_2(C*D)))^2                (3.1)
```

nonempty cells.  They form a disjoint partition of all generic ordered
completion pairs, so

```text
P(z)=sum_(sigma,tau,j,k) P_(sigma,tau,j,k)(z).       (3.2)
```

Apply `DSP_(epsilon/2)` to every cell.  Since `D` is polynomially bounded in
`q`,

```text
P(z) <= N_cells*C_(epsilon/2)*D*q^(epsilon/2)||z||_2^4
     <= C'_epsilon*D*q^epsilon||z||_2^4.            (3.3)
```

Thus, in the `q^o(1)` regime used by the project,

```text
DSP  <=>  PAIR.                                     (3.4)
```

This is the main falsification found in this pass.  Proving DSP would prove
the four-cycle bound, but calling DSP a smaller arithmetic lemma would only
rename the final obstacle.

## 4. Why the rooted replacement fails

Suppose a cell is further written as a positive sum over roots,

```text
P_cell=sum_r P_(r,cell),       P_(r,cell)>=0.        (4.1)
```

There is no inequality of the form

```text
sum_r P_(r,cell) <= q^o(1)*max_r P_(r,cell)          (4.2)
```

without a bound on the number or effective participation of the roots.
The exact finite countermodel is `R` disjoint roots of mass one: the two
sides before the `q^o(1)` factor are `R` and `1`.

The issue is not repaired by retaining signs.  The endpoint is positive;
the signs label cells but do not create cancellation between them.

An actual-support diagnostic reinforces the warning.  For the natural
first-completion root on the generic `q=25013`, `U=40` support:

```text
ordered nonzero-(A,B) secants:       5,604
distinct active roots:               5,468
largest root mass:                       3
sum / largest-root ratio:             1,868
```

This is not an asymptotic counterexample, and a different rooted theorem may
carry a nontrivial measure.  It does show that the historical maximum-root
bridge is not even reflected in the first hostile actual fixture.

## 5. Attack from the strongest proved local inputs

### 5.1 Exact `(A,B)` layers do not sum

For each fixed nonzero signed pair `(A,B)`, the existing Schur argument
proves

```text
sum_C nu_(A,B)(C) w_z(C)
  << D q^o(1) ||z||_2^4.                            (5.1)
```

A cell contains `O(2^(j+k))` possible exact pairs.  Positive summation of
(5.1) therefore gives only

```text
P_(sigma,tau,j,k)(z)
  << D*2^(j+k)*q^o(1)||z||_2^4,                     (5.2)
```

which is useless at the large scales.  Across all possible `(A,B)` it can
lose `D^2`.  Grouping by `A*B` does not help: the actual fixture

```text
(A,B)=(1440,5320),       |A*B|=7,660,800 > D=15,509.94
```

rules out the tempting stronger premise `|A*B|<<D`.

### 5.2 Fixed-energy matching also does not sum automatically

The fixed-`(E,det C)` color kernel is a partial matching.  Different layers
can nevertheless occupy the same master edge.  Cotlar or orthogonality
therefore requires an overlap theorem; it is not a formal consequence of
the fixed-layer matching.

### 5.3 Dyadic cells need not disperse a structured family

In a full-integer translation family, many ordered pairs lie in one signed
dyadic cell.  The exact 323-completion fixture has 104,006 ordered
off-diagonal pairs, and one cell contains 14,351 of them.  Hence no proof can
rely only on the number of occupied cells or on an assertion that each cell
is automatically sparse.  Actual prime-power rigidity must exclude or
control the corresponding coherent families.

There is one unconditional positive consequence of the fixed-layer theorem:
(5.2) closes every cell for which

```text
2^(j+k)=q^o(1).                                      (5.3)
```

The hard range is therefore genuinely the medium/large determinant cells;
this is a small strict reduction, not the desired global estimate.

The finite actual scan points in the same direction:

```text
generic ordered secants:              5,604
occupied signed dyadic cells:           308
largest cell:                            186
sum / largest-cell ratio:              30.129...
distinct exact signed (A,B):           5,596
largest exact-(A,B) multiplicity:           2
```

Exact layers are almost all singletons in this fixture, while their dyadic
aggregation is not.  This is diagnostic evidence only, but it identifies
aggregation across varying secants—not fixed-layer multiplicity—as the
correct place to look.

Nor can one assume that every repeated actual fiber lies on one determinant
ray.  The three-completion all-prime fixture at `q=11801`, `U=35` has

```text
(A,B)=(942,-444), (-432,320), (-1554,676)
```

up to orientation.  These are three distinct rays and give six oriented
signed cells.  Only a quantitative *high-mass* inverse theorem can remain
plausible.

## 6. A more useful equivalent acceptance theorem

Although DSP is not easier, it has a set-valued form that is better suited
to hostile testing and peeling.  Let

```text
n_cell(C)=#{(X,X') in the chosen cell},
N_cell(S11,S12,S21,S22)
 =sum_(C: cij in Sij for every i,j) n_cell(C).       (6.1)
```

The Cartesian restricted-type statement is

```text
N_cell(S11,S12,S21,S22)
 << D q^epsilon product_ij |Sij|^(1/2).             (CRT_epsilon)
```

It is again equivalent to DSP up to `q^o(1)`, but it exposes the exact
rank-one masks and avoids the stronger demand of testing arbitrary sets of
ordered color pairs.

To see `DSP => CRT`, assume the four sets are nonempty and take

```text
z=sum_ij |Sij|^(-1/2) 1_(Sij).
```

Then `||z||_2<=4`, and every desired color tuple has weight at least
`product_ij |Sij|^(-1/2)`.  Thus DSP gives CRT with an absolute factor at
most `4^4=256`.

For the converse, use the exact layer-cake identity

```text
z_c=integral_(t>0) 1_(z_c>t) dt                    (6.2)
```

for `z>=0`.  Tonelli and CRT give

```text
P_cell(z)
 <= D q^epsilon
    (integral_(t>0) |{c:z_c>t}|^(1/2) dt)^4.        (6.3)
```

If the shell has `n` colors, sorting the coordinates and applying
Cauchy--Schwarz yields

```text
integral_(t>0) |{c:z_c>t}|^(1/2) dt
 <= sqrt(1+log n) ||z||_2.                          (6.4)
```

Therefore CRT implies DSP with only `O(log^2 n)=q^o(1)` loss.  This exact
reformulation is the useful output of the localization pass: any proposed
arithmetic mechanism can now be tested on Cartesian cuts before it is
promoted to the weighted quartic.

## 7. The first genuinely new gate

The next lemma must do more than localize.  The best surviving candidate is
an actual-mask inverse theorem, implemented through weighted packet
participation and packet-free unconditionality.

### 7.1 Exact weighted packet mechanism

For a packet `t`, let `L_t,R_t` be its ordered-color-pair supports and put,
for `x_c=|z_c|^2`,

```text
U_t(x)=sum_((c,d) in L_t) x_c*x_d,
V_t(x)=sum_((e,f) in R_t) x_e*x_f.                  (7.1)
```

The local hypothesis need only retain rank one:

```text
P_t(z) <= a_t*sqrt(U_t(x)*V_t(x)).                  (7.2)
```

A full local operator bound is sufficient for (7.2), but is not required.
Assume also that these nonnegative packet pieces cover the relevant cell
form.  For arbitrary balancing parameters `lambda_t>0`, weighted
Cauchy--Schwarz gives

```text
sum_t P_t(z)
 <=[sum_t lambda_t U_t(x)]^(1/2)
   [sum_t a_t^2/lambda_t V_t(x)]^(1/2).             (7.3)
```

Consequently it is sufficient to prove

```text
L=max_(c,d) sum_(t:(c,d) in L_t) lambda_t,
R=max_(e,f) sum_(t:(e,f) in R_t) a_t^2/lambda_t,
L*R <= D^2 q^o(1).                                  (7.4)
```

Indeed each factor in (7.3) is then bounded by `L^(1/2)||z||_2^2`
or `R^(1/2)||z||_2^2`.  The symmetric choice `lambda_t=a_t` recovers the
simpler rule that the two maximum weighted packet-participation loads have
product at most `D^2 q^o(1)`.

This is strictly softer than bounding the total number of packets.  In
particular, arbitrarily many pairwise vertex-disjoint packets make only one
packet's contribution to each maximum in (7.4).

### 7.2 Precise arithmetic inverse target

The prior residual-block work proves the sharp randomized `O(D)` budget and
proves sharp estimates for a certified merged affine/Hankel packet.  It also
gives an exact full-integer counterexample to raw all-plus/Rademacher
unconditionality, with a polynomial `sqrt(D)` gap.  The counterexample is
itself a coherent affine/Hankel packet.

The correct remaining theorem is therefore:

> Polynomial all-plus excess in an actual signed determinant cell implies a
> quantitatively large mergeable affine/Hankel (or certified polynomial-arc)
> packet.  The extracted packets satisfy (7.4), and after their removal the
> exact QP cell mask satisfies packet-free `S_4` unconditionality.

In the residual-block notation, the last clause has the form

```text
||sum_I A_I^gen(z)||_(S_4)^4
 <=q^o(1) E_epsilon ||sum_I epsilon_I A_I^gen(z)||_(S_4)^4,  (7.5)
```

with the joint `(A,B)` cell and post-peeling masks retained on both sides.
The randomized right side already has the target `D q^o(1)` bound.

Equivalently, (7.5) can be approached contrapositively as an
**excess-implies-mergeable-packet** theorem.  The genuinely arithmetic open
part is the global packing/participation of sparse actual-prime packets and
the mask-stable estimate on their complement.

### 7.3 Quantifier trap

Bicore pruning does not preserve Cartesian structure.  Starting from
`S11 x S12` and `S21 x S22`, ordinary peeling can leave arbitrary subsets
of ordered pairs.  Declaring a theorem for every such abstract bicore would
silently upgrade the problem to the stronger full pair-operator estimate.

Peeling is therefore safe only while the parent Cartesian masks or the
original rank-one weights remain attached to every charge.  For the
factorial kernel the weighted minimum-degree-product threshold is `D^2`,
not `D`; the latter belongs to the underlying incidence operator.

Arbitrary-mask unconditionality is already false.  Equation (7.5) must use
the actual joint QP mask; separating the two modular lifts or replacing that
mask by an arbitrary bounded one destroys the proposed advantage.

### 7.4 Abstract full-operator specialization

Here is the elementary functional mechanism.  Suppose a bipartite kernel is
decomposed into packet kernels `T_t`, supported on vertex sets `L_t x R_t`,
and

```text
||T_t||_(2->2) <= a_t.
```

Put

```text
A_L=max_x sum_(t:x in L_t) a_t,
A_R=max_y sum_(t:y in R_t) a_t.                    (7.6)
```

Weighted Cauchy--Schwarz gives the exact bound

```text
||sum_t T_t||_(2->2) <= sqrt(A_L*A_R).              (7.7)
```

Consequently arbitrarily many vertex-disjoint packets are harmless.  A
`q^o(1)` bound for the *number* of packets, as demanded by the earlier PAC
formulation, is unnecessarily strong.

## 8. Updated route ranking

1. **Weighted excess-implies-packet plus mask-stable remainder.**  This uses
   the proved randomized budget and the proved individual packet estimates,
   and asks for exactly the missing actual-mask inverse principle.
2. **Cartesian factorial restricted type plus weighted packet
   participation.**  This is the cleanest positive formulation and the
   right acceptance test for any proposed packet theorem.
3. **Slope-block/PAC.**  Several local ranges and `PAC => SB` are proved,
   but absolute packet counting should be replaced by (7.4).
4. **DRPLS/translate Bessel.**  This is concrete and scale-sensitive, but
   remains a stronger analytic surrogate whose reconstruction must be
   checked against the Cartesian endpoint.
5. **Primitive shifted-cube aggregation.**  It is a precise downstream
   subproblem, not presently the highest unresolved branch.

DSP is omitted from the ranking.  It is a localization and acceptance test,
not a reduction in difficulty.

## 9. Falsification and demotion criteria

The weighted-packet route should be demoted if any of the following occurs:

1. the packet decomposition is valid only after taking absolute values that
   erase the QP-generated dependency;
2. restricting a Cartesian cut to packets forces a theorem for arbitrary
   pair masks with a polynomial loss;
3. one actual or legally enlarged tangent family has polynomial weighted
   participation in both vertex classes beyond the bound in (7.4);
4. the peeled contribution cannot be charged in the same factorial weight
   as (6.1);
5. the purported packet theorem merely restates CRT or DSP with new labels;
6. a competing route supplies a strictly weaker theorem with a proved
   reconstruction to PAIR.

The rooted route has an additional kill criterion: without an explicit
weighted reconstruction over roots, a rootwise estimate is not a candidate
proof component.

## 10. What was proved and what remains open

```text
signed (A,B) cells partition the pair endpoint:      PROVED (ELEMENTARY)
number of cells is O(log^2 q):                       PROVED
DSP <=> PAIR up to q^o(1):                           PROVED
DSP <=> Cartesian restricted type up to q^o(1):     PROVED
maximum-root reconstruction:                         REFUTED
fixed-(A,B) cell summation by positivity:            INSUFFICIENT
weighted packet-overlap functional lemma:            PROVED (ABSTRACT)
arithmetic weighted packet participation:            OPEN
Cartesian residual-core classification:              OPEN
sharp four-cycle bound:                              OPEN
```

The exact finite bookkeeping is implemented in
`src/qp_collective_dyadic_gate.py`, with regression tests in
`src/test_qp_collective_dyadic_gate.py`.  Those routines verify the
partition, factorial multiplicity, nonnegative-weight hypothesis, and the
root-maximum countermodel, as well as the abstract balanced packet-overlap
ledger and the 323-completion cell-concentration fixture.

The focused verification command was

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_collective_dyadic_gate.py \
  src/test_qp_four_cycle_pair_energy_audit.py \
  src/test_qp_self_orbit_dynamic_packets.py \
  src/test_qp_post_peel_mask_stability.py \
  src/test_qp_rank_one_h_tangent_residual.py \
  src/test_qp_two_star_interval_peeling_barrier.py \
  src/test_qp_weighted_unconditionality_audit.py \
  src/test_qp_weighted_triangle_packet_inverse.py
```

It produced `55 passed`.  These tests do not verify DSP, CRT, arithmetic
packet participation, packet-free unconditionality, or the four-cycle
bound.
