# R143 solvable support quotient and primitive classification

## Status

R141 replaced complete splitting by a weaker-looking condition: every small
Frobenius may move only a tiny fraction of the embeddings of a large
non-Galois field.  This report determines what that condition means at the
group-theoretic level.

There are two sharply different answers.

1.  In a solvable transitive group, all elements of support at most `L` are
    killed on a common block quotient whose degree is at least `m/(2L)`.
    In the number-field translation, the selected primes split completely in
    an intermediate field of at least that degree and no larger root
    discriminant.  Thus the solvable/monomial version of R141's approximate
    mask collapses to its exact split-field gate.
2.  In a primitive nonsolvable group, sublinear support forces a Cameron
    product action.  Fixed *absolute* support leaves only the natural
    alternating or symmetric actions in unbounded degree.  These actions are
    genuine counterexamples to the solvable block conclusion: transpositions
    generate `S_m`, and `3`-cycles generate `A_m`.

The second conclusion does not close the program.  It identifies the one
primitive family which must be treated analytically.  R144 records a new
virtual-character construction which in fact annihilates its bounded-support
classes exactly.

```text
solvable support-to-block theorem                 PROVED
uniform constant 2                               SHARP
number-field split-quotient corollary             PROVED
root-discriminant monotonicity                    PROVED
relative Dedekind quotient for solvable closure   ENTIRE
primitive sublinear-support classification        IMPORTED / APPLIED
fixed-support primitive survivor                  NATURAL A_m OR S_m
unconditional sub-square-root discriminant ban    NOT PROVED
fixed uniform zeta zero-free strip                 NOT PROVED
zeros approaching one                             NOT PROVED
```

Date: 2026-08-08.

Predecessors:
[`R141-NONLINEAR-TENSOR-AND-REGULAR-FROBENIUS-GATE.md`](R141-NONLINEAR-TENSOR-AND-REGULAR-FROBENIUS-GATE.md)
and
[`R142-GROWING-POLE-ORDER-AND-COMMON-DIVISOR-GATE.md`](R142-GROWING-POLE-ORDER-AND-COMMON-DIVISOR-GATE.md).

## 1. The support problem

Let a finite group `G` act faithfully and transitively on a set `Omega` of
size `m`.  For `g in G`, write

```text
supp(g)={omega:g omega!=omega},       ell(g)=|supp(g)|.       (1.1)
```

Let `C` be any collection of elements with

```text
0<ell=max_(c in C) ell(c),                                   (1.2)
```

and let

```text
N=<C^G>                                                       (1.3)
```

be its normal closure.  The R141 question is whether `N` must have small
orbits.  If it does, the `N`-orbits give a large quotient action on which
every element of `C` is the identity.

For arbitrary groups the answer is false.  In the natural action of `S_m`,
a transposition has support `2`, but its conjugates generate all of `S_m`.
The following theorem shows that this is intrinsically nonsolvable.

## 2. Sharp solvable support-to-block theorem

**Theorem 2.1.**  Suppose `G` in Section 1 is solvable.  Then every `N`-orbit
has size at most

```text
ell/(1-1/p)<=2ell                                             (2.1)
```

for a prime `p` arising from a primitive section of the action.  Consequently
the `N`-orbits form a `G`-invariant block system with at least

```text
m/(2ell)                                                      (2.2)
```

blocks, and every element of `C` acts trivially on that system.

If `C` contains a nonidentity and `ell<m/2`, the block system is genuinely
nontrivial.  If `C={1}`, the singleton system is the canonical degenerate
answer.

**Proof.**  Fix `omega in Omega`, let `H=G_omega`, and choose a maximal
subgroup chain

```text
H=H_0 < H_1 < ... < H_r=G.                                  (2.3)
```

The subgroup `H_i` corresponds to a block system `B_i`.  A block in `B_i`
has size

```text
a_i=[H_i:H],                                                 (2.4)
```

and contains

```text
d_i=[H_i:H_(i-1)]                                            (2.5)
```

children from `B_(i-1)`.  The action of its setwise stabilizer on those
children is primitive after quotienting by the action kernel.

A faithful primitive solvable group of degree `d` is affine.  Indeed, a
minimal normal subgroup is an elementary abelian regular group, so the
action embeds in `AGL(f,p)` with `d=p^f`.  A nonidentity affine map

```text
x -> A x+v                                                    (2.6)
```

has either no fixed point or a fixed affine subspace of size at most
`p^(f-1)`.  It therefore moves at least

```text
(1-1/p)d>=d/2                                                (2.7)
```

points.

Let `i` be least such that every `c in C` fixes every block of `B_i`.
Such an `i` exists because `B_r` consists of one block.  Since a nonidentity
member of `C` does not fix all singleton blocks, `i>=1`.  Choose `c in C`
which moves a `B_(i-1)`-block.  It fixes the containing `B_i`-block and
induces a nonidentity element on its `d_i` children.  By (2.7), it moves at
least `(1-1/p)d_i` children.  Every point of a moved child moves, and hence

```text
ell >= a_(i-1)(1-1/p)d_i
    = (1-1/p)a_i.                                            (2.8)
```

Thus `a_i<=ell/(1-1/p)<=2ell`.  The kernel of the action on `B_i` is normal
in `G` and contains `C`, so it contains `N`.  Every `N`-orbit is therefore
contained in a `B_i`-block and has size at most `2ell`.  Normality of `N`
and transitivity of `G` make all its orbits equal-sized blocks.  This proves
the theorem.  QED.

Equivalently, with

```text
J=HN,                                                        (2.9)
```

the orbit of `omega` is `J/H`, and

```text
[J:H]=[N:N intersect H]<=2ell,
[G:J]>=m/(2ell).                                             (2.10)
```

## 3. Sharpness

The uniform constant `2` cannot be improved.  Let

```text
G=S_4 wr C_t                                                  (3.1)
```

act imprimitively on `4t` points, and let `C` be the full conjugacy class of
a transposition in one base coordinate.  The group is solvable, every member
of `C` has support `ell=2`, and

```text
N=<C>=S_4^t.                                                  (3.2)
```

The `N`-orbits are the blocks of size `4=2ell`.  Any block-action kernel
which kills `C` contains `N`, so no finer killed quotient is possible.

The factor `2` comes only from characteristic `2` in the affine primitive
section.  Formula (2.1) retains the sharper factor `1/(1-1/p)` when that
prime is known.

## 4. Number-field translation

Let `K/Q` have degree `m` and solvable Galois closure `E/Q`.  Put

```text
G=Gal(E/Q),              H=Gal(E/K).                          (4.1)
```

Because `E` is the Galois closure, the action on `G/H` is faithful.  Let `S`
be a set of rational primes unramified in `E`, and assume every Frobenius
class at a prime in `S` moves at most `L<m/2` cosets in `G/H`.  Let `C` be
the union of those classes, form `N=<C>`, put `J=HN`, and set

```text
F=E^J.                                                       (4.2)
```

Theorem 2.1 gives

```text
[K:F]=[J:H]<=2L,
[F:Q]=[G:J]>=m/(2L).                                        (4.3)
```

If `C` contains a nonidentity then

```text
Q proper-subset F proper-subset K.                           (4.4)
```

If `C={1}`, take `F=K`.  Every selected Frobenius lies in the kernel of the
action on `G/J`, so every `p in S` splits completely in `F`.  If `K` is
totally real, so is `F`.

The tower discriminant formula gives

```text
D_K=D_F^[K:F] N_(F/Q)(D_(K/F)),
rd(K)=rd(F) N_(F/Q)(D_(K/F))^(1/m)>=rd(F).                   (4.5)
```

Thus the exact split field is never more expensive in root discriminant
than the proposed approximate field.

For a ramified rational prime, one Frobenius representative is not enough.
Complete splitting in `F` follows if its entire decomposition group,
including inertia, is put into `C` and hence killed on `G/J`.

## 5. Artin formalism and the auxiliary quotient

The block-constant subspace gives an actual representation decomposition

```text
C[G/H]=C[G/J] direct-sum V,
Ind_H^G 1=Ind_J^G 1+chi_V.                                  (5.1)
```

Artin formalism yields

```text
zeta_K/zeta=(zeta_F/zeta)L(s,V),
L(s,V)=zeta_K/zeta_F.                                       (5.2)
```

The normal closure of `K/F` has Galois group

```text
J/core_J(H),                                                 (5.3)
```

which is solvable.  The Uchida--van der Waall theorem on Dedekind's
conjecture for solvable normal closure therefore makes `L(s,V)` entire.
The primary sources are Uchida,
[*On Artin L-functions*](https://doi.org/10.2748/tmj/1178241036), and
van der Waall,
[*On a conjecture of Dedekind on zeta-functions*](https://doi.org/10.1016/1385-7258(75)90019-0).

Entireness is not zero-freeness.  What it does show is that any local
nonvanishing package assumed for `zeta_K/zeta` transfers to both factors in
(5.2).  The solvable approximate mask therefore supplies no analytic escape
which is absent from the exact field `F`.

For `b=[F:Q]`, the R141 detector

```text
A_F=(b D_zeta-D_(zeta_F))/(b-1)                              (5.4)
```

has nonnegative coefficients, deletes every prime in `S` at all powers,
and costs only `O(log rd(F))<=O(log rd(K))` after normalization.

## 6. Primitive nonsolvable groups

Write `mu(G)` for the minimal support of a nonidentity element of a
primitive permutation group of degree `m`.  The Liebeck--Saxl
classification implies the following dichotomy:

```text
mu(G)>=m/3,                                                   (6.1)
```

or `G` is a Cameron group

```text
A_t^ell normal-subgroup G <= S_t wr S_ell,                  (6.2)
m=binom(t,j)^ell,                                            (6.3)
```

where `S_t` acts on the `j`-subsets and the wreath product uses product
action.  See Liebeck--Saxl,
[*Minimal Degrees of Primitive Permutation Groups*](https://doi.org/10.1112/plms/s3-63.2.266),
especially Theorem 6.1 and its `m/3` corollary.

In the full wreath product, a transposition in one base coordinate moves

```text
mu_2=2 binom(t-2,j-1) binom(t,j)^(ell-1)                     (6.4)
```

points, so

```text
mu_2/m=2j(t-j)/[t(t-1)]>=j/(t-1).                           (6.5)
```

If the base contains only alternating groups, a `3`-cycle gives a slightly
larger support.  Thus (6.5) is a valid lower scale for every Cameron case.

Suppose the R141 support fraction is

```text
L/m=X^(-theta+o(1)),             theta>0.                    (6.6)
```

A nonidentity head Frobenius then forces

```text
t >> j X^theta,
m >> X^(theta j ell).                                      (6.7)
```

The unique degree-cheapest survivor is

```text
j=ell=1,                                                     (6.8)
```

the natural action of `A_t` or `S_t`.  A transposition forces the symmetric
case, while Jordan's theorem puts a primitive group containing a `3`-cycle
into the alternating/symmetric case.

The conclusion is even sharper for fixed absolute support.  Unless
`j=ell=1`, the quantity in (6.4) tends to infinity in every unbounded-degree
Cameron family.  Therefore:

**Corollary 6.1.**  Up to finitely many degrees, an unbounded family of
primitive groups containing a nonidentity element of support bounded by an
absolute constant must use the natural `A_m` or `S_m` action.

This is the exact primitive remainder.  Solvability cannot be omitted from
Theorem 2.1 because the transpositions of natural `S_m` have support `2` and
normal closure `S_m`; the `3`-cycles give the analogous statement for
`A_m`.

## 7. Conditional and heuristic reality checks

For any degree-`m` field whose unramified Frobenius at every `p<=X` fixes at
least `m-L` embeddings,

```text
psi_K(X)>= (m-L)psi(X)+lower-prime-power corrections.        (7.1)
```

Under GRH for `zeta_K`, an explicit prime-ideal theorem gives

```text
|psi_K(X)-X| << sqrt(X)[log D_K+m log X].                    (7.2)
```

After division by `m`, (7.1)--(7.2) imply

```text
log rd(K) >> (1-L/m)sqrt(X)-O(log X).                        (7.3)
```

This contradicts the R141 requirement `log rd(K)=o(X^kappa)` for every
`kappa<1/2`.  A suitable explicit source is Grenie--Molteni,
[*Explicit versions of the prime ideal theorem for Dedekind zeta
functions under GRH*](https://arxiv.org/abs/1312.4463).

Unconditionally, the Poitou--Odlyzko explicit formula gives only a
`log rd(K) >> log X` consequence of almost-complete splitting.  That is a
real lower bound, but it is compatible with every positive power `X^kappa`.
The square-root obstruction is therefore conditional, not a proved no-go.

For the natural symmetric group, the proportion of permutations moving at
most a fixed `L` is

```text
delta_(m,L)
 =sum_(j<=L) D_j/[j!(m-j)!]
 =exp[-(1+o(1))m log m],                                    (7.4)
```

where `D_j` is the number of derangements on `j` letters.  Treating local
Frobenius conditions as independent and combining (7.4) with a uniform
Malle law predicts

```text
log rd(K) >= pi(X)log m.                                    (7.5)
```

If `m>=X^theta`, this is of order `X`; even for fixed `m` it is of order
`X/log X`.  This is a strong reality check, not a theorem uniform in the
growing group.

Known Grunwald--Hilbert and quantitative specialization theorems do not
approach the required scale.  They establish qualitative realization of
finitely many local classes, but their discriminants grow at least on an
`X` scale in the available quantitative forms.  Polynomial specialization
also meets a basic index obstruction when `m-L>p`: a degree-`m` polynomial
over `F_p` cannot have more than `p` distinct linear factors even though a
nonmonogenic degree-`m` field can have more than `p` degree-one primes.

## 8. Verdict

The solvable branch is closed exactly:

```text
small support in a solvable closure
        -> large killed block quotient
        -> large completely split intermediate field
        -> no larger root discriminant.                      (8.1)
```

The nonsolvable branch does not close.  Primitive-group classification
reduces it to natural alternating/symmetric actions, and both GRH and local
field-count heuristics say that the required prescribed-Frobenius fields
should be far too expensive.  Neither statement is unconditional at the
sub-square-root scale needed here.

Most importantly, classification suggests a new move rather than a final
no-go: natural `A_m/S_m` has only finitely many bounded-support cycle types.
R144 replaces the linear fixed-point defect by a nonnegative virtual
character which vanishes on all of them.  That construction removes the
old `L/m` error exactly and exposes the next analytic gate: a signed
auxiliary divisor attached to the virtual representation.

Neither a fixed zeta zero-free strip nor zeros approaching one follows from
R143.
