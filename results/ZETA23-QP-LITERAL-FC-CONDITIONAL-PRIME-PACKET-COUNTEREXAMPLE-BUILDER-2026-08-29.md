# QP literal four-cycle: conditional prime-packet counterexample builder

**Date:** 2026-08-29

## Verdict

No actual or standard-prime-conjectural power counterexample was found.
There is an explicit admissible polynomial tangent chart which, under a
uniform short-box Hardy--Littlewood hypothesis, gives an actual-prime subset
`E` with

```text
R(E)/(D |E|^2) >> (log q)^(-6).                       (0.1)
```

Thus actual primes can conditionally realize a near-extremal Hankel packet;
the obstruction is not simply that prime tangent packets never occur.  But
the ratio in (0.1) is subpower, not `q^delta`.  Exact same-color
translations and a dyadic multi-slope audit both stop at `Dq^o(1)`.

The prime hypothesis used for the growing packet is stronger than
fixed-form Dickson: it asks for Hardy--Littlewood asymptotics in a box of
side `q^(8/33)`.  Fixed-form Dickson does suffice to make the four base
linear polynomials simultaneously prime.  Even after granting the stronger
short-box input, the construction does not disprove the literal four-cycle
bound.

## 1. Restricted-type target

For an ordinary-prime color subset `E`, put

```text
u_c=|E|^(-1/2) 1_(c in E).
```

If `R(E)` is the number of oriented hard-window rectangle occurrences all
of whose four colors lie in `E`, then

```text
F_+(u)=R(E)/|E|^2.                                    (1.1)
```

Hence a restricted-type counterexample requires

```text
R(E)>D |E|^2 q^delta.                                 (1.2)
```

No factorial completion multiplicity appears in (1.1).

## 2. A primitive near-cube of four admissible linear forms

Set

```text
x=100,                y=101,                z=103,
n=(xyz)^2=1,082,224,090,000,

r1=(yz)^3=1,125,837,720,827,
r2=(xz)^3=1,092,727,000,000,
r3=(xy)^3=1,030,301,000,000.                         (2.1)
```

The three ratios are

```text
r1/n=1.0403,
r2/n=1.009704930889...,
r3/n=.952021868225... .                              (2.2)
```

Thus they lie in the standard project collar `|log(t)|<.05`; the explicit
fixture below applies, in particular, to the `w=.2` literal shell used in
the computational project fixtures.

Choose

```text
a0= 7,206,685,485,100,449,
b0=-6,994,737,931,165,371,
c0=107,223.                                           (2.3)
```

These constants satisfy the exact identity

```text
a0*x^3+b0*y^3+c0*z^3=3xyz/2=1,560,450.               (2.4)
```

For an integer parameter `T`, define

```text
q(T)=4nT+1,
A(T)=2r1 T+a0,
B(T)=2r2 T+b0,
C(T)=2r3 T+c0.                                       (2.5)
```

Since `r1*r2*r3=n^3`, (2.4) gives exact cancellation of the cubic and
quadratic coefficients:

```text
deg_T(8A(T)B(T)C(T)-q(T)^3)<=1.                       (2.6)
```

All four forms in (2.5) are primitive.  Their constants are odd, so there
is no obstruction modulo `2`.  Modulo `3`, the residue `T=1` avoids all
four zero classes.  For every prime `p>=5`, four primitive linear forms
exclude at most four residues modulo `p`, hence cannot cover all residues.
Therefore the four-form tuple is admissible.  Dickson's conjecture predicts
infinitely many `T` for which

```text
q(T), A(T), B(T), C(T)
```

are simultaneously ordinary primes.  This is a genuine fixed-form prime
tuple assertion, not a relabeling of composite nodes.

## 3. Exact growing tangent chart and hard-window check

Put

```text
rho=z^3=1,092,727,
alpha=x^3=1,000,000,
beta=y^3=1,030,301,

a_i=A(T)+rho*i,
b_j=B(T)+rho*j,
c_ij=C(T)-alpha*i-beta*j.                            (3.1)
```

The leading parts cancel in both tangent directions:

```text
rho*(2r3)-alpha*(2r1)=0,
rho*(2r3)-beta *(2r2)=0.                             (3.2)
```

Consequently the two linear defects

```text
h1=rho*C(T)-alpha*A(T),
h2=rho*C(T)-beta *B(T)                               (3.3)
```

are constants independent of `T`.

The exact product expansion, valid for arbitrary integral parameters, is

```text
(A+ri)(B+sj)(C-ui-vj)-ABC
 =B(rC-uA)i+A(sC-vB)j
  -Bru i^2-Asv j^2
  +(rsC-rvB-suA)ij
  -rsu i^2j-rsv ij^2.                               (3.4)
```

Apply (3.4) with `r=s=rho`, `u=alpha`, `v=beta`, and combine it with
(2.6).  Since all displayed numerical coefficients are fixed while
`q(T)asymp T`,

```text
|8a_i b_j c_ij-q(T)^3|
 <<q(T)(1+|i|+|j|+i^2+j^2)+(|i|+|j|)^3.             (3.5)
```

Let

```text
D=q^(16/33),              L=eta sqrt(D),             (3.6)
```

where `eta>0` is a sufficiently small fixed constant depending only on the
fixture.  Because `D^(1/2)=o(q)`, equations (3.5)--(3.6) imply, for all
sufficiently large prime values `q=q(T)`,

```text
|8a_i b_j c_ij-q^3|<=qD                 (|i|,|j|<=L). (3.7)
```

Equations (2.2) and `L=o(q)` put every node in the actual project shell.
The three progressions in (3.1) are primitive:

```text
gcd(A(T),rho)=gcd(B(T),rho)=1,
gcd(C(T),alpha,beta)=1.                               (3.8)
```

Thus, unlike the old exact factorized grid, this chart has no forced common
factor in any node family.  Its color is determined by `alpha*i+beta*j`,
and `gcd(alpha,beta)=1`, so there are `asymp L` possible color values in a
box of side `L`.

## 4. Conditional ordinary-prime realization and exact exponent

Fixed-form Dickson only supplies prime base values.  To populate the
growing box, assume the following stronger uniform short-box
Hardy--Littlewood prediction along a subsequence of simultaneous prime base
values from Section 2.  Restrict `i` and `j` to suitable fixed residue
classes (in particular, even classes remove the parity obstruction); this
changes only constants:

```text
# {i:a_i prime}                         asymp L/log q,
# {j:b_j prime}                         asymp L/log q,
# {c_ij prime values}                   asymp L/log q,
# {(i,j):a_i,b_j,c_ij all prime}        asymp L^2/(log q)^3,

# prime-supported oriented rectangles  >>L^4/(log q)^8.          (4.1)
```

The final line is the corresponding finite-complexity eight-prime
correlation.  Calling this `UHL_short` makes the unproved uniformity
explicit.

Let `E` be the ordinary-prime colors from (4.1).  Then

```text
|E|asymp L/log q,
R(E)>>L^4/(log q)^8.                                 (4.2)
```

Using `L^2asymp D` in (1.1),

```text
F_+(u)=R(E)/|E|^2
      >>L^2/(log q)^6
      >>D/(log q)^6,                                 (4.3)

R(E)/(D|E|^2)>>(log q)^(-6).                         (4.4)
```

The same lower bound follows by testing the prime row-column matrix on its
two normalized all-one vectors.  All colors are ordinary primes and every
edge obeys the literal hard window (3.7).  This is a conditional physical
saturator, not a `q^delta` counterexample.

## 5. Exact same-color replication stops at the sharp scale

Colors in (3.1) depend on `alpha*i+beta*j`.  The translation

```text
(i,j)->(i+beta*h,j-alpha*h)                           (5.1)
```

therefore preserves every color exactly.  Translated boxes can be made
row/column disjoint, giving the most favorable possible block reuse.

For boxes of index side `ell`, disjointness and the curvature terms in
(3.4) imply

```text
B ell<<sqrt(D)                                        (5.2)
```

for the number `B` of translated boxes which remain in the common hard
window.  Each box has conditional fourth trace
`ell^2/(log q)^O(1)`, so

```text
sum_(nu<=B)F_+(P_nu)
 <<B ell^2 q^o(1)
 <<sqrt(D) ell q^o(1)
 <=Dq^o(1).                                           (5.3)
```

At `ell=sqrt(D)` there is one saturating packet.  Making the packet smaller
permits more orthogonal translates, but their total never gains a power.

## 6. Dyadic multi-slope Farey audit

For a general local chart write

```text
a=A+r i,              b=B+s j,
c=C-u i-v j.                                           (6.1)
```

If all four direction coefficients have dyadic height `R`, the physical
width of an index box of side `ell` is

```text
W=R ell.
```

The curvature terms in (3.4) force

```text
W<<sqrt(D).                                           (6.2)
```

For fixed `(r,u)`, the linear defect allows `A` to range through an interval
of length only `O(D/W)`; after row-disjointness this gives at most
`O(D/W^2)` translations.  The same is true on the other side.

Fix the color directions `(u,v)`.  The two slope approximations and the
base hard product force `rs` into an interval of length

```text
O(uv D/(Wq))
 <=O(WD/q)
 <=O(D^(3/2)/q)=O(q^(-3/11)).                        (6.3)
```

Thus at most one integer value of `rs` occurs, with only `q^o(1)` factor
pairs.  There are `O(R^2)` dyadic choices of `(u,v)`.

If coefficient mass is spread through the common color interval of length
`W`, one chart has fourth-trace scale at most `W^2/R^4`.  Hence the total
regular-chart capacity is

```text
(R^2q^o(1))(D/W^2)(W^2/R^4)
 <<D R^(-2)q^o(1).                                   (6.4)
```

If the color image is the smaller progression arising from
`g=gcd(u,v)`, the individual bound grows by `g^2`; the elementary estimate

```text
sum_(u,v~R)gcd(u,v)^2<<R^3q^o(1)
```

changes (6.4) to `O(D/R)`, still below the target.  `UHL_short` prime
thinning changes only logarithmic factors.

This is a capacity calculation for regular affine charts, not a theorem
classifying every physical rectangle family as such a chart.  It does show
that filling every approximate Farey-slope packet with the conjecturally
correct number of primes does not create a power counterexample.

## 7. Generic anchor density also predicts a deficit

For physical width `W`, the two center windows have length `D/W`.  A
generic center pair hits the remaining product aperture with probability
`D/q`.  Uniform prime/equidistribution heuristics therefore give

```text
# anchors per slope pair
  asymp D^3/(qW^2)(log q)^(-2).                       (7.1)
```

Relative to the `D/W^2` disjoint translation slots, this is the fraction

```text
D^2/q=q^(-1/33).                                     (7.2)
```

Thus standard prime-tuple behavior predicts a small deficit.  The major arc
of Sections 2--4 overcomes that deficit and reaches the `D` scale, but its
same-color replication spends the curvature budget in (5.2).

## 8. Surviving counterexample profile

A genuine `q^delta` restricted-type counterexample must be more singular
than the conditional construction above.  It needs:

1. ordinary-prime coefficient colors;
2. polynomially many row/column-orthogonal pieces reusing essentially the
   same color mass;
3. no containment in one `sqrt(D)` translation collar;
4. no charge by the regular Farey packet capacity (6.4); and
5. a polynomial surplus over both the generic aperture density (7.2) and
   the `UHL_short` prime counts.

This is precisely a sparse, nonaffine, recurrent system spread over moving
one-/two-point secants.  Standard Hardy--Littlewood conjectures do not
produce it.  Assuming such a polynomial surplus directly would merely
rename the desired counterexample.

```text
primitive admissible four-linear-form near-cube:    EXACT;
literal qD tangent-box check:                       EXACT;
simultaneously prime base nodes:                    DICKSON-CONDITIONAL;
growing ordinary-prime tangent packet:              UHL_short-CONDITIONAL;
restricted ratio R(E)/(D|E|^2):                    (log q)^(-6);
same-color translated q^delta excess:               NO;
regular multi-slope Farey q^delta excess:            NO;
actual q^delta literal-FC counterexample:            NOT FOUND.
```
