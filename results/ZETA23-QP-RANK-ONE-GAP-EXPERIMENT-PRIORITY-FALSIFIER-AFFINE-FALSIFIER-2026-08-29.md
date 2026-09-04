# The physical rank-one-gap experiment is not the next step

Date: 2026-08-29

## Verdict

The proposed experiment comparing cardinal generic GACCT with the pure
rank-one norm on a growing physical power-rich generic block is not the
right next experiment.  It is a valid one-sided counterexample search, but
its prerequisite is almost the same unknown physical configuration that the
theorem is supposed to control.  Current fixtures cannot enter its intended
range, and a negative numerical result would have no asymptotic force.

Direct weighted packet participation is materially more falsifiable because
the positive terms and exact A4 primal/dual interface already exist.  The
cheapest decisive test for a fixed packet extractor is the point-pair A4
dual overload, not a global rank-one optimization.

## 1. Why the rank-one-gap experiment is presently circular

The desired comparison was

```text
C_row(R)=maximum generic anchored row sum,
C_op(R)=full pair-space norm,
C_pure(R)=sup_z <conj(z) tensor z,A_R(conj(z) tensor z)>.
```

It presupposes all of the following.

1. A physical block with power-rich codegree `R` must first be found.  The
   four materialized actual-prime-power graphs have maximum off-diagonal
   codegrees `4,4,6,4`; every maximizing dyadic bin has `R=1`.  They lie in
   the already harmless bounded-`R` range.
2. The word “generic” is not currently a stored edge label.  Forming the
   post-coherent kernel requires a completion-consistent weighted peel and
   an exact assignment of every term.  That assignment is one of the open
   packet/Carleson problems.  Different provisional peels can change
   `C_pure`.
3. Constructing a power-rich **actual-prime** generic family by hand requires
   simultaneously solving the unique-completion, six-window, prime-power,
   and cyclic-consistency constraints.  This is essentially the existence
   side of the arithmetic problem under investigation.  Failure to find a
   family is not evidence for a uniform theorem.

The abstract directed-parabola and affine-hyperplane examples have already
answered the only cheap logical question: cardinal GACCT can exceed the
rank-one target by a power.  Repeating them with more color relabelings does
not test the physical mask.

## 2. Sample complexity and certification problems

The exact `q=50021,U=40` graph already has roughly `602000` pair vertices and
one million edges, yet maximum codegree four.  Increasing `q` enlarges the
pair state space much faster than it guarantees a rare high-codegree block.
There is no empirical sample-size law converting a cutoff or a number of
anchors into a chance of seeing `R=q^delta`.

Even if a candidate block is found, `C_pure` is a nonconvex positive quartic
optimization in the original color variables.  Multistart optimization and
Cartesian cuts give rigorous lower bounds only.  An apparent pass cannot be
certified at large shell dimension; exhaustive or interval branch-and-bound
scales exponentially.  Replacing `C_pure` by `C_op` restores an easy spectral
calculation but returns to a strictly stronger pair-space theorem.

Finally, a finite sequence cannot distinguish a fixed constant, a power of
`log q`, and `q^delta` over the accessible range.  The experiment can kill
the weighted theorem if it finds a certified violation, but cannot provide
meaningful positive evidence.  Its expected information per unit of
computation is therefore low.

## 3. Why direct packet participation is more testable

The A2 v1 interface already retains on the materialized `q=25013,U=40`
source:

```text
5604 positive factorial atoms, 308 signed cells,
physical ordered supports and four masks,
exact rational allocations and remainder,
packet amplitudes and replayable Schur bounds.
```

The exact-secant baseline has 5596 nearly singleton packets and exact worst
A4 value `4`, against `D^2=18225`.  This pass is also asymptotically weak:
the source has no certified post-A1 excess and almost no compression.  The
important difference is falsifiability.  For any fixed candidate extractor,
A4 failure has a short exact dual certificate and closes that packet family
without first constructing a generic high-codegree residual block.

Packet participation still does not solve A2.  A safe A4 value says nothing
about whether packets capture a polynomial fraction of a common dual excess,
and an existential extractor can change its decomposition.  The packet
class and stopping rule must be frozen before the test is theorem-decisive.

## 4. Cheapest decisive falsifier: the point-pair dual

For packets with supports `L_t,R_t` and certified amplitudes `a_t`, define

```text
B=max_(u,v) sum_(t:u in L_t and v in R_t) a_t.      (4.1)
```

In the exact A4 dual take

```text
alpha=delta_u,       beta=delta_v,
s_t=a_t on packets containing both u and v,
s_t=0 otherwise.
```

Then

```text
inf_lambda L(lambda)R(lambda) >=B^2.               (4.2)
```

Thus one pair with

```text
B>D q^c
```

falsifies the target `LR<=D^2q^o(1)` by a fixed power.  The certificate is
local, exact, and independent of convex-solver tolerance.  It can be found
with inverted packet-support lists; it does not require Gram construction,
generic classification, or optimization over `z`.  When `a_t^2` rather than
`a_t` is rational, rational lower slacks give the same certified test.

The current serialized baseline has `B=2`, and `(4.2)` is the existing exact
lower certificate `4`.  That is a sanity check, not a stress result.

If `(4.1)` passes, the next cheapest dual search uses uniform probability on
small rectangles `U_0 x V_0`:

```text
p_t=|L_t intersect U_0|/|U_0|,
r_t=|R_t intersect V_0|/|V_0|,
lower=(sum_t a_t sqrt(p_t r_t))^2.                 (4.3)
```

Greedy sizes `2,4,8` followed by rational slack certification probe diffuse
overload before running the full convex optimizer.

## 5. Most informative immediate controls

Apply `(4.1)--(4.3)` to the same term IDs under two predeclared packet rules:

1. one packet for every naive maximal affine completion line;
2. the canonical common-plane/fixed-direction merger.

The scalable multilevel tangent fixture is the cheapest hostile control.  It
is already known that the first rule creates polynomial Carleson overload
while the second can merge the same geometry.  A point-pair dual identifies
whether that overload is visible directly at A4.  The materialized actual
source then tests the same frozen rules with literal prime-power masks.

A failure kills the specified packet rule.  It does not kill an existential
A2 theorem allowed to choose a different packetization.  Conversely, a pass
does not prove participation asymptotically; it merely justifies proceeding
to the more expensive captured-excess and remainder tests.

## 6. Correct experimental order

```text
1. Freeze a candidate physical packet rule and serialize its exact output.
2. Run point-pair dual overload (4.1).
3. Run tiny-rectangle duals (4.3).
4. Only then solve the full A4 primal/dual problem.
5. Add R,Y and captured operator excess to test A2 extraction.
6. Reserve physical rank-one-gap scans for a power-rich block found
   independently; do not make such a block a prerequisite for progress.
```

This ordering attacks a concrete sufficient mechanism with exact negative
certificates.  The rank-one-gap experiment attacks an endpoint-equivalent
quantity on data that do not yet exist.
