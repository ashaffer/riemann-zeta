# QP four-cycle: logical independence of the local-fan and global-allocation gates

**Date:** 2026-08-29

**Status:** proof-grade abstract dependency audit.  A whole-star residual
degree-product theorem would remove the global packet-allocation gate, but
the currently proposed theorem for each individual rich-line pair does not.
Conversely, local `O(D)` packet bounds and completion-consistent orientation
do not imply the global affine Carleson bound.  Neither countermodel below is
claimed to be an actual-prime QP counterexample; they isolate the additional
physical statements that a successful theorem must use.  Section 6 restores
the weaker exact NDS/ACCT criterion and accordingly revises the project-level
priority from whole-star RDP to excess-conditioned anchored Carleson.

## 1. The local line-pair conclusions do not imply RDP

Let `n>=2`, put `D=n^2`, and set

```text
U=V={1,...,n}^2 subset Z^2.
```

For `F(u,v)=u_1*v_1-u_2*v_2`, one has

```text
max_(u in U,v in V)|F(u,v)| <= n^2-1 < D.          (1.1)
```

Every affine line meets the integer square in at most `n` points.  Indeed, a
vertical line has at most `n` points, while on a nonvertical line each of the
`n` possible first coordinates supports at most one point.  Therefore

```text
R_U=R_V=n,                                         (1.2)
```

and, more strongly, for every pair of affine lines `ell,m`, regardless of
whether their directions are transverse or `F`-null,

```text
|U intersect ell| * |V intersect m| <=n^2=D.       (1.3)
```

Nevertheless

```text
|U|*|V|=n^4=D^2.                                   (1.4)
```

Thus even the conjunction of the Cartesian determinant strip and a sharp
`O(D)` result for *every individual line pair* does not imply the residual
degree-product estimate.  The CDLS theorem is consistent with this example:
its right side has order

```text
D*R_U*R_V=D^2.
```

The exact missing assertion is concentration or summable covering, not one
more classification of a single pair of lines.  In particular, CDLS says
that excess forces large line occupancies; it does not say that a line with
maximum occupancy carries a positive fraction of an arm.

The example deliberately omits the QP hard-window witnesses.  Consequently
it does not refute a physical concentration theorem.  It proves that those
witnesses or the prime-power mask must be used to establish concentration;
it cannot be inferred from CDLS and the line-pair bounds already proved.

## 2. A sufficient dominant-fan inverse theorem

For a residual transition edge `e`, let `U_e,V_e` be its two projected
neighbor arms.  The six-product identity gives

```text
max_(u in U_e,v in V_e)|F(u,v)| <<D.                (2.1)
```

The following is a sufficient local theorem.  For every `epsilon>0`, suppose
that, uniformly in `e`, either

```text
R_(U_e) R_(V_e) <=q^epsilon,                        (2.2)
```

or there are affine lines `ell_e,m_e` such that

```text
|U_e| |V_e|
 <=q^epsilon |U_e intersect ell_e| |V_e intersect m_e|.   (2.3)
```

Assume also that every line pair supplied by `(2.3)` satisfies

```text
|U_e intersect ell_e| |V_e intersect m_e|
 <<D q^epsilon.                                    (2.4)
```

Here `(2.4)` may be proved by the existing transverse theorem, the
affinely-witnessed curvature theorem, or the sought remote parallel-null
theorem, according to the direction and witness class.

Then RDP follows.  In case `(2.2)`, CDLS and `(2.1)` give

```text
|U_e||V_e| <<D q^epsilon.
```

In case `(2.3)`, equation `(2.4)` gives

```text
|U_e||V_e| <<D q^(2 epsilon).
```

Since `epsilon` is arbitrary, both bounds are `Dq^o(1)`.  The edge-degree
spectral lemma then proves the complete residual operator estimate.  The
already separated tangent sector can be added independently.  No affine
peel, packet orientation, or `H_aff` estimate occurs in this implication.

A slightly weaker but still sufficient replacement for `(2.3)` is a
partition of the two arms into affine-line pieces with at most `q^o(1)`
line-pair combinations, each satisfying `(2.4)`.  The identity

```text
|U_e||V_e|=sum_(i,j)|U_(e,i)| |V_(e,j)|
```

then gives RDP directly.  What is not sufficient is an unrestricted number
of individually bounded line pairs, as Section 1 proves.

A compact sufficient target is the dominant-fan inequality

```text
|U_e||V_e| <<q^o(1) (
    D + max_(physical parallel-null ell,m)
        |U_e intersect ell| |V_e intersect m|
).                                                  (2.5)
```

Together with the remote parallel-null line theorem, `(2.5)` removes the
global allocation gate altogether.  This is the precise strength at which
the direct local route becomes logically self-contained.

## 3. Local packet bounds and orientation do not imply global Carleson

Fix one color `c`.  For `1<=i<=N`, introduce three colors unique to `i` and
one required packet profile

```text
t_i: ((c,1),(a_i,1),(b_i,1),(d_i,1)).              (3.1)
```

The profiles may be taken to host pairwise disjoint completion occurrences,
so completion consistency is automatic.  For every `t_i`,

```text
L_i=1,       M_i=4,       mu_i=min(L_i,M_i)=1.     (3.2)
```

Thus every packet separately has local trace coefficient and maximum color
charge equal to `1`, hence is `O(D)` for every `D>=1`.  Globally, however,

```text
H_aff(c)=sum_i mu_i*l_(i,c)=N.                     (3.3)
```

Taking `N>>Dq^o(1)` violates the desired Carleson estimate.  Giving each
occurrence several endpoint-centered hosts does not repair the example if
every admissible host necessarily contains the same physical color `c` and
charges it by at least one: every assignment still has `c`-load at least
`N`.

This is the key distinction from ordinary graph orientation.  Orienting a
transition chooses its host and prevents double assignment, but it does not
move the colors appearing in that transition.  Hence it does not by itself
distribute the vector of color charges.  The literal `q=11801,U=44` audit,
where one color lies in 32 selected plane geometries and the canonical load
is `288>D=94`, is a finite physical warning of the same overlap phenomenon,
though not an asymptotic counterexample to a better geometric extractor.

## 4. Exact fractional-allocation dual

The vector-valued nature of the missing theorem can be made exact.  Let `I`
be a finite set of completion items.  Item `i` has a finite set `A_i` of
admissible packet hosts, and choosing host `h` incurs a nonnegative color
charge vector

```text
a_(i,h)=(a_(i,h,c))_(c in C).
```

Allow a fractional assignment `x_(i,h)>=0` with
`sum_(h in A_i)x_(i,h)=1`, and define the optimal maximum color load

```text
Lambda = min_x max_c sum_(i,h) x_(i,h) a_(i,h,c).  (4.1)
```

Let `Delta_C` be the probability simplex on the colors.  Since the maximum
coordinate of a vector `L` is

```text
max_(y in Delta_C) <y,L>,
```

finite-dimensional minimax gives the exact dual identity

```text
Lambda
 =max_(y in Delta_C) sum_i min_(h in A_i)<y,a_(i,h)>.
                                                            (4.2)
```

Indeed, the objective is bilinear in the product of the assignment
simplices and `Delta_C`; after exchanging `min` and `max`, minimization
separates independently over the items, producing the right side of
`(4.2)`.

Consequently a fractional allocation of load at most `B` exists if and only
if, for every nonnegative mask `y`,

```text
sum_i min_(h in A_i)<y,a_(i,h)>
 <=B sum_c y_c.                                    (4.3)
```

Integral allocation may require additional rounding control, so `(4.3)` is
only a lower gate for the desired integral extractor.  It is already a
mask-sensitive vector-valued Carleson theorem.  In the common-color example,
take `y` concentrated on `c`; the left side is `N` and `(4.3)` fails.
Therefore no support-blind orientation lemma can derive the desired global
bound merely from the fact that every available packet is locally `O(D)`.

## 5. Dependency verdict

There are two valid ways to collapse the decision tree, but each requires a
strictly stronger theorem than the corresponding current statement.

1. Prove a dominant-fan, subpower-cover, or whole-star physical RDP theorem
   such as `(2.5)`.  Then the residual spectral lemma closes the argument and
   the global affine allocation gate disappears.
2. Prove a joint geometric extractor which both supplies admissible hosts
   for remote parallel-null fans and verifies the mask inequalities `(4.3)`,
   followed by integral completion-consistent rounding.  Such a theorem
   absorbs the local fan gate, but it is not a general graph-orientation
   result; it contains the missing local lift and global Carleson mathematics.

With the present per-line theorem and present local packet estimates, neither
gate implies the other.  The cleaner route to removing one gate is the first:
strengthen the remote analysis to a dominant-fan/whole-star estimate and
bypass packet allocation rather than attempting to globalize overlapping
local packets.

## 6. Re-audit against the weaker exact NDS/ACCT closure

The last recommendation above is correct as a comparison of the two RDP
routes, but it is not the optimal node in the full proof tree.  The residual
operator only needs

```text
W(gamma)=sum_(p~gamma) deg(p) <<Dq^o(1),            (NDS)
```

not `deg(gamma)deg(p)<<Dq^o(1)` on every edge.  The distinction is material.
Take an abstract double star in which `gamma` has `H` neighbors, one of those
neighbors has degree `M`, and every other neighbor has degree one.  Then

```text
max_(p~gamma) deg(gamma)deg(p)=H*M,
W(gamma)=M+H-1.                                    (6.1)
```

For `H,M` both of order `D`, RDP is excessive by a factor of order `D`, while
NDS still has the correct linear order.  Thus a bare selected-divisor theorem
which bounds every local line-population product can prohibit configurations
which the desired operator inequality is allowed to retain.

The exact next project node should instead be the already identified anchored
Carleson tail.  For the unresolved generic sector and the only unproved
dyadic range, prove

```text
#{eta : R<=r_gamma(eta)<2R, eta generic/unresolved}
 <<(D/R)q^epsilon,                                  (6.2)
```

uniformly for

```text
deg(gamma)>D^(1/4)q^o(1),
q^o(1)<R<min(sqrt(D),deg(gamma)^2/sqrt(D)).          (6.3)
```

Equivalently, after dyadic summation one may prove directly

```text
sum_eta r_gamma^unresolved(eta)<<Dq^epsilon.        (6.4)
```

This is excess-conditioned: an isolated neighbor of very large degree is
charged only by the paths it actually contributes, rather than by its degree
times all `H` anchor neighbors.  Equations `(6.2)--(6.4)` imply NDS directly
and require neither an affine packet host nor global `H_aff` allocation.

The new coefficient-large parallel-null theorem does not, by itself, permit
the word `unresolved` in `(6.2)` to be replaced by `small-coefficient`.
It bounds one line pair pointwise.  ACCT sums chains over potentially many
line pairs, and Section 1 proves that individual `O(D)` bounds do not provide
that summation.  One must first prove a canonical weighted transfer

```text
sum_eta r_(gamma,coefficient-large)(eta)<<Dq^o(1). (6.5)
```

If the previously established coherent high-tail theorem supplies `(6.5)`
after an exact identification of its packets with the coefficient-large
fans, then `(6.2)` may legitimately be restricted to
`0<max(|lambda|,|mu|,|gamma_0|,|eta_0|)<sqrt(K)`.
Without that identification, the coefficient-large chains remain inside the
weighted target despite their local theorem.

This gives the revised priority order.

1. Prove the excess-conditioned generic ACCT estimate `(6.2)`, restricted to
   small coefficients only after the weighted transfer `(6.5)` is proved.
2. Treat the physical selected-divisor product `(3.3)` as a useful local
   lemma or falsifier inside that attack, not as the main closure theorem.
3. Pursue whole-star concentration only if the sharper anchored route fails;
   it restores the unnecessarily strong RDP quantifier and still needs the
   small-coefficient line theorem.
4. Defer the LP-dual mask inequality.  Its host menu is undefined for the
   nonaffine remote fans, its charges depend on packet grouping, and its
   fractional solution still requires integral completion-consistent
   rounding.  At the present node it packages both missing gates rather than
   separating them.

Accordingly, the narrowest theorem aligned with the sharp target is weighted
small-coefficient ACCT, not pointwise selected-divisor RDP, provided `(6.5)`
has first made the coefficient split honest.  Otherwise the correct statement
is weighted generic ACCT with both coefficient strata retained.
