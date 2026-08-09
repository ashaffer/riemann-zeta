# R168 finite-union late support and transition-hull gate

## Status

The late-supported strict-slack construction of R163 extends from one small
conjugate pair of filled discs to any fixed finite collection of left-hand
compacta satisfying a polynomial-separation condition after

```text
lambda=1-s,                 q=exp(h lambda).              (0.1)
```

The clean target-independent condition is the following.  If `L` is the
`q`-image of the compacta in `Re(s)<1`, there must be an `r>1` such that

```text
E_r={|q|<=r} union L                                      (0.2)
```

is polynomially convex, with a fixed geometric Bernstein--Walsh
neighborhood on which the target is holomorphic.  In one complex variable,
polynomial convexity is exactly connectedness of `C\E_r`.  The disk in
(0.2) contains every `q`-image from `Re(s)>=1`; requiring approximation to
zero on this slightly enlarged disk is what makes the coefficient norm, and
not just the function error, exponentially small.

Under this hypothesis, for every bounded conjugation-symmetric analytic
target `G_M` on `L` there is a real polynomial

```text
P_M(q)=sum_(n=M)^(M+dM)c_(n,M)q^n                       (0.3)
```

such that

```text
sup_L |G_M-P_M|                  << exp(-c_1 M),
sup_(|q|<=1)|P_M|                << exp(-c_0 M),
sum_n |c_(n,M)|                  << exp(-c_0 M).          (0.4)
```

Consequently the associated length-`h` step control is supported at times
`v` comparable to `M`, has exponentially small supremum norm, cancels the
target on all the left compacta simultaneously, and tends exponentially to
zero on every right compactum in `Re(s)>=1`.

Taking `M` proportional to `log H` repairs the exact logarithmic prime
density exactly as in R163.  The actual-prime block lift remains valid on a
finite union without any new loss.  If

```text
sigma_0=inf_(s in K_left union K_right) Re(s)>7/12,       (0.5)
```

then fractional actual-prime coefficients and subsequently one sign per
prime retain every exponent

```text
c<sigma_0-7/12.                                          (0.6)
```

There is, however, a decisive transition obstruction.  A full localization
contour crossing `Re(s)=1` maps, when `q` is injective, to a Jordan curve
crossing the unit circle.  An outside arc together with the closed unit disk
encloses a bounded lens.  Its polynomial hull fills that lens.  Therefore a
sequence of polynomials which tends to zero on the disk cannot tend to a
fixed nonzero profile on the outside arc.  More generally this is impossible
whenever the proposed boundary profile does not extend holomorphically over
the polynomial hull.

This separates two statements which must not be conflated:

```text
finite separated contour patches                         WORKS
completed transition contour with a nontrivial cutoff    FAILS
```

The first statement is a genuine strengthening of R163 and survives the
actual-prime lift.  The second is exactly the statement needed to turn the
patchwise construction into a direct Rouche localization argument.  Thus
this route does not prove a fixed zero-free strip.  It proves that a
nonzero-left/zero-right analytic cutoff cannot close the contour; a viable
next construction must use boundary data compatible with the filled hull,
or introduce and explicitly account for singularities.

Date: 2026-08-08.

Predecessors:
[`R163-PRIME-BLOCK-LIFT-AND-RANDOM-SIGN-ROUNDING-GATE.md`](R163-PRIME-BLOCK-LIFT-AND-RANDOM-SIGN-ROUNDING-GATE.md),
[`R167-QUANTITATIVE-NONNORMAL-RATIO-CLOUD-GATE.md`](R167-QUANTITATIVE-NONNORMAL-RATIO-CLOUD-GATE.md).

## 1. Geometry after the exponential change of variables

Let

```text
K_< subset {Re(s)<1},          K_>= subset {Re(s)>=1}     (1.1)
```

be finite conjugation-invariant compact unions, and put

```text
Lambda_<=1-K_<,                Lambda_>=1-K_>=.           (1.2)
```

Compactness of `K_<` gives a fixed `delta_*>0` with

```text
Re(lambda)>=delta_*                 on Lambda_<.          (1.3)
```

For real `h>0`, define

```text
q_h(lambda)=exp(h lambda).                                  (1.4)
```

Then

```text
|q_h|>=exp(h delta_*)>1          on Lambda_<,
|q_h|<=1                         on Lambda_>=.             (1.5)
```

The target on the left must descend to the `q`-plane.  The simplest
checkable condition is that `q_h` be one-to-one on a neighborhood of all the
left components and that their images be pairwise disjoint.  A sufficient
global condition is

```text
h diam(Im(Lambda_<))<2 pi.                                (1.6)
```

Indeed, equality of two exponential images would make the imaginary parts
differ by an integer multiple of `2 pi/h`.  One can replace injectivity by
the weaker exact condition that the target agree on every exponential
fiber, but nothing is gained for the present application.  Taking `h`
small enough always enforces (1.6) on a fixed compact set.  Unlike the
two-disc proof in R163, the argument below does not need to send the images
far from the unit circle.

Write

```text
L=q_h(Lambda_<).                                         (1.7)
```

Choose

```text
1<r<min_(q in L)|q|                                      (1.8)
```

and define `E_r` by (0.2).  We use the following robust form of the
geometric hypothesis.

### Hypothesis BW

The compact set `E_r` is regular and polynomially convex, and it has a fixed
neighborhood `U` with these properties:

1. the component `U_0` containing `{|q|<=r}` is disjoint from the
   components `U_j` containing the pieces of `L`;
2. the target is holomorphic on every relevant `U_j`;
3. there are constants `C_BW>=1` and `0<rho<1` such that every function
   holomorphic on `U`, with independently prescribed branches on its
   components, has a degree-`D` polynomial approximant on `E_r` with error

```text
C_BW rho^D sup_U |F|.                                   (1.9)
```

This is not an extra number-theoretic assumption.  It is the standard
geometric Bernstein--Walsh approximation property.  A precise potential-
theoretic sufficient condition is that `C\E_r` be connected and regular and
that a Green-function level neighborhood of `E_r` lie in `U`.  Then (1.9)
is the Bernstein--Walsh theorem, with `rho` determined by a smaller fixed
level.  In particular Hypothesis BW holds for a finite union of separated
closed analytic Jordan domains and analytic Jordan arcs whose complement is
connected, provided the target is holomorphic on a slightly larger fixed
neighborhood.

The topological part is exact:

```text
E_r polynomially convex in C
        <=> C\E_r is connected.                          (1.10)
```

If (1.10) fails, the polynomial hull fills all bounded components of the
complement.  Approximation is then possible only for targets which have a
compatible holomorphic extension across those filled components.  Section 6
shows why a transition contour has no such extension.

All sets and neighborhoods will be conjugation invariant.  Since `h` is
real, (1.4) preserves conjugation.

## 2. The finite-union high-degree polynomial theorem

### Theorem 2.1 (finite-union delayed approximation)

Assume Hypothesis BW.  Let `G_M` be any family holomorphic on the left
components of `U` such that

```text
sup_(U\U_0)|G_M|<=1,
G_M(conjugate(q))=conjugate(G_M(q)).                     (2.1)
```

There are a fixed positive integer `d`, constants `C,c_0,c_1>0`, and real
polynomials

```text
P_M(q)=sum_(n=M)^(M+dM)c_(n,M)q^n                       (2.2)
```

for which (0.4) holds.  All constants depend only on the fixed geometry,
not on `M` or on the particular bounded target family.

### Proof

Choose the Bernstein--Walsh neighborhood in Hypothesis BW slightly smaller
if necessary and put

```text
R_-=inf_(q in U\U_0)|q|>r,
R_+=max_(q in L)|q|.                                    (2.3)
```

On the disconnected neighborhood `U`, define

```text
F_M(q)=0                         on U_0,
F_M(q)=q^(-M)G_M(q)             on U\U_0.                (2.4)
```

This is a single holomorphic function on the disconnected open set `U` and

```text
sup_U |F_M|<=R_-^(-M).                                  (2.5)
```

For `D=dM`, (1.9) supplies a polynomial `Q_M` of degree at most `D` with

```text
epsilon_M:=sup_(E_r)|F_M-Q_M|
       <=C_BW R_-^(-M)rho^(dM).                         (2.6)
```

Symmetrizing by

```text
[Q_M(q)+conjugate(Q_M(conjugate(q)))]/2                 (2.7)
```

makes its coefficients real without increasing the degree or error.
Define

```text
P_M(q)=q^M Q_M(q).                                      (2.8)
```

This has exactly the delayed support (2.2).  On `L`, equations
(2.4), (2.6), and (2.8) give

```text
|G_M-P_M|
 <=R_+^M epsilon_M
 <=C_BW [(R_+/R_-)rho^d]^M.                            (2.9)
```

Choose `d` once and for all so that

```text
(R_+/R_-)rho^d<1.                                      (2.10)
```

This proves the first estimate in (0.4).

It remains to prove coefficient slack.  Write

```text
Q_M(q)=sum_(k=0)^(dM)a_(k,M)q^k.                        (2.11)
```

Because `F_M=0` on `{|q|<=r}`, (2.6) and Cauchy's
coefficient estimate on the circle `|q|=r` give

```text
|a_(k,M)|<=epsilon_M r^(-k).                            (2.12)
```

Consequently

```text
sum_k |a_(k,M)|
 <=epsilon_M/(1-r^(-1))
 <<[R_-^(-1)rho^d]^M.                                  (2.13)
```

Multiplication by `q^M` only shifts coefficient indices, so (2.13) is the
third estimate in (0.4).  It also implies the second estimate there on the
closed unit disk.  QED.

Two aspects of the proof are worth isolating.

First, merely applying Mergelyan to `L` would control the function on `L`
but would give no useful coefficient norm.  Adding the disk of radius
`r>1`, prescribing zero there, and using Cauchy's estimate is the entire
coefficient-slack mechanism.

Second, no minimum distance much larger than one is needed.  If `L` lies
close to the unit circle, `R_-/r` and the Bernstein--Walsh rate deteriorate,
but increasing the fixed ratio `d=D/M` restores (2.10).  The construction
therefore works for every fixed positive separation from `Re(s)=1`; it is
not uniform as that separation tends to zero.

## 3. Finite-union causal Laplace control

Put

```text
kappa_h(lambda)=[exp(h lambda)-1]/lambda,                (3.1)
```

with the removable value `kappa_h(0)=h`.  It is nonzero on the left
neighborhood after injectivity is imposed, because `|q|>1` there.

### Theorem 3.1 (left cancellation and right extinction)

Assume the geometry of Section 1.  Let `f_M` be a uniformly bounded family
holomorphic near `Lambda_<`, respecting conjugation.  Then there is a real
step function `a_M` such that

```text
support(a_M) subset [Mh,(M+dM+1)h],
||a_M||_infinity<<exp(-c_0M),                            (3.2)
```

and

```text
sup_(lambda in Lambda_<)
 |f_M(lambda)+integral_0^infinity
                 a_M(v)exp(lambda v)dv|
       <<exp(-c_1M),                                    (3.3)

sup_(lambda in Lambda_>=)
 |integral_0^infinity a_M(v)exp(lambda v)dv|
       <<exp(-c_0M).                                    (3.4)
```

### Proof

On the left `q`-images, apply Theorem 2.1 to

```text
G_M(q)=-f_M(lambda(q))/kappa_h(lambda(q)).               (3.5)
```

The inverse branches are defined separately on the disjoint left
components.  The hypotheses make (3.5) bounded, holomorphic, and
conjugation symmetric.  If the resulting polynomial is

```text
P_M(q)=sum_n c_(n,M)q^n,                                (3.6)
```

set

```text
a_M(v)=c_(n,M)             for nh<=v<(n+1)h.             (3.7)
```

Termwise integration gives the exact identity

```text
integral_0^infinity a_M(v)exp(lambda v)dv
       =kappa_h(lambda)P_M(exp(h lambda)).               (3.8)
```

The coefficient estimate in (0.4) proves (3.2).  Equation (3.3) follows
from left approximation and the boundedness of `kappa_h`.  On
`Lambda_>=`, (1.5), (0.4), and (3.8) prove (3.4).  Notice that (3.1) remains
bounded at `lambda=0`; points on `Re(s)=1` cause no singularity.  QED.

The right target may therefore be any family `e_M` with
`||e_M||_(K_>=)->0`; the total right error is

```text
||e_M||_(K_>=)+O(exp(-c_0M)).                            (3.9)
```

If it is power-small after `M` is tied to `log H`, the complete error is
power-small.  If it is only `o(1)`, the theorem honestly gives only `o(1)`
on the right.

## 4. Exact logarithmic density and power accuracy

Let

```text
T=log H,                    lambda=1-s.                  (4.1)
```

Suppose `A_H` is analytic near the finite compact union.  On the left
assume the normalized heads

```text
f_H(lambda)=T H^(-lambda)A_H(1-lambda)                  (4.2)
```

are uniformly bounded on the fixed larger neighborhoods required above.
On the right assume, for some `A_0>0`,

```text
sup_(s in K_>=)|A_H(s)|<=H^(-A_0).                      (4.3)
```

Apply Theorem 3.1 with

```text
M=ceil(BT)                                                (4.4)
```

and define

```text
b_H(v)=(T+v)a_M(v)/T.                                   (4.5)
```

The support in (3.2) has length `O_B(T)`, while the amplitude of `a_M`
is `O(H^(-c_0B))`.  Hence, for every fixed `B` and all sufficiently large
`H`,

```text
||b_H||_infinity<=1/2.                                  (4.6)
```

With

```text
Y=H exp((M+dM+1)h)=H^kappa                              (4.7)
```

for a fixed `kappa=kappa(B)>1`, the exact density identity is

```text
integral_H^Y b_H(log(x/H))x^(-s)dx/log x
 =H^lambda/T integral_0^infinity
                     a_M(v)exp(lambda v)dv.             (4.8)
```

There is no frozen-logarithm error.  On the left, the factor `H^lambda` in
(4.8) costs at most a fixed power of `H`, which can be beaten by increasing
`B`.  On the right, `|H^lambda|<=1`.  Thus, for every prescribed `A>0`,
`B` can be chosen so that

```text
sup_(s in K_<)
 |A_H(s)+integral_H^Y b_H(log(x/H))x^(-s)dx/log x|
       <=H^(-A),                                        (4.9)

sup_(s in K_>=)
 |A_H(s)+integral_H^Y b_H(log(x/H))x^(-s)dx/log x|
       <<H^(-min(A,A_0)).                               (4.10)
```

The same proof works if the left normalized family is bounded by a fixed
power of `H`; one simply increases `B`.  Uniform boundedness is the natural
form needed for the exact prime head in R163.

There is an important application boundary.  The exact head

```text
S_H(s)=sum_(p<=H)p^(-s)                                 (4.11)
```

satisfies the left normalization (4.2), but it does **not** satisfy (4.3).
At `s=1` it has size asymptotic to `log log H`, and for fixed real `s>1`
it tends to a nonzero limit.  Therefore the theorem does not cancel the
exact prime head on the left while magically making that same head vanish
on a right contour.  A proposed outer-contour target must independently
possess the right extinction in (4.3).

There is also a useful limiting profile on every fixed left compactum.
Uniformly for `lambda` in a compact subset of `Re(lambda)>0`, partial
summation and the prime number theorem give

```text
sum_(p<=H)p^(lambda-1)
       =(1+o(1))H^lambda/(lambda log H).                 (4.12)
```

Consequently

```text
f_H(lambda)->1/lambda,
G_H(q)=-lambda f_H(lambda)/(q-1)->-1/(q-1).              (4.13)
```

Thus the exact-head target on a separated left island has a stable,
nonzero limiting `q`-profile.  It is not a target which quietly disappears
as `H` grows.  Formula (4.12) is not uniform up to `Re(lambda)=0`; the loss
of that uniformity is part of the transition problem, rather than a way to
obtain (4.3).

## 5. Lift to actual primes

Let

```text
K=K_< union K_>=,
sigma_0=inf_(s in K)Re(s).                              (5.1)
```

Disconnectedness causes no change in the block-normalization proof of
R163: all kernel variation estimates are uniform on an arbitrary compact
set.  If

```text
sigma_0>7/12                                             (5.2)
```

and `7/12<theta<sigma_0`, Theorem 2.1 of R163 turns the control in
(4.8) into actual coefficients `c_p in [-1,1]` with error

```text
O(H^(theta-sigma_0)/log H)                               (5.3)
```

uniformly on the whole finite union.  The strict slack (4.6) is much
stronger than the fixed slack needed there.  The random Bergman rounding
theorem of R163 can then be applied in one bounded domain in
`Re(s)>1/2` containing all the compact components, and gives one sign per
prime at the smaller error scale

```text
O(H^(1/2-sigma_1)/sqrt(log H)).                          (5.4)
```

The block error (5.3) remains limiting.  After making the continuum error
arbitrarily small via `B`, every exponent

```text
c<sigma_0-7/12                                           (5.5)
```

is available.  Therefore the passage

```text
finite-union continuum control
 -> actual fractional primes
 -> one sign at each prime                               (5.6)
```

retains fixed-power accuracy.  No new arithmetic obstruction appears at
the finite-union stage.

## 6. The polynomial-hull obstruction

The polynomial convexity condition in Section 1 is not a technical
convenience.  It is exactly what prevents independently prescribed pieces
from becoming incompatible after a contour is filled.

Recall that the polynomial hull of a plane compactum `E` is

```text
hat(E)={z: |p(z)|<=sup_E|p| for every polynomial p}.     (6.1)
```

It is `E` together with all bounded components of `C\E`.

### Proposition 6.1 (hull compatibility is necessary)

Let `E` be compact and let polynomials `P_n` converge uniformly on `E` to
`F`.  Then they converge uniformly on `hat(E)` to a continuous function
`F_tilde` which is holomorphic in `int(hat(E))` and extends `F`.

If a connected component `V` of `int(hat(E))` meets an open set on which
`F_tilde=0`, then `F_tilde` vanishes identically on `V`.

### Proof

For every polynomial `p`, the definition of the hull gives

```text
sup_(hat(E))|p|=sup_E|p|.                                (6.2)
```

Apply (6.2) to `P_n-P_m`.  A uniformly Cauchy sequence on `E` is uniformly
Cauchy on the hull, so it has a continuous limit there.  Local uniform
convergence makes the limit holomorphic in the interior.  The last
assertion is the identity theorem.  QED.

Here is the elementary transition configuration.

### Corollary 6.2 (unit-disk plus outside-arc obstruction)

Let `gamma` be a simple Jordan arc whose distinct endpoints lie on the unit
circle and whose remaining points lie strictly outside the closed unit
disk.  If `g` is continuous on `gamma` and is not identically zero, there
are no polynomials `P_n` such that

```text
sup_(|q|<=1)|P_n(q)| ->0,
sup_(q in gamma)|P_n(q)-g(q)| ->0.                       (6.3)
```

The same conclusion holds for a varying `g_n` if some subsequence converges
uniformly on `gamma` to a nonzero `g`.

### Proof

The arc `gamma`, together with either of the corresponding unit-circle
arcs, bounds a lens.  For

```text
E={|q|<=1} union gamma,                                  (6.4)
```

the polynomial hull fills the bounded lens components.  Its interior has a
connected component containing the open unit disk and abutting `gamma`.
If (6.3) held, the polynomials would converge on `E` to the function which
is zero on the disk and `g` on `gamma`.  Proposition 6.1 and the identity
theorem force its hull extension, and hence its trace on `gamma`, to be
zero.  This contradicts the choice of `g`.  The subsequential statement is
identical.  QED.

The statement remains true if the unit disk is replaced by any filled
right-hand compactum and the outside arc creates a bounded complementary
component whose filled interior connects to an open zero set.  Conversely,
when the hull has no such connection, approximation may still be possible;
the exact requirement is holomorphic compatibility on the filled hull.

## 7. Why completing the outer contour changes the answer

Suppose a Jordan localization contour in the `s`-plane crosses
`Re(s)=1`, and choose `h` so that (0.1) is injective on the contour and its
interior.  Its `q`-image is again a Jordan curve.  The portions from

```text
Re(s)<1              map to |q|>1,
Re(s)>=1             map to |q|<=1.                     (7.1)
```

An outside component joining two transition points is precisely an arc of
the type in Corollary 6.2.  Thus a polynomial control cannot converge to

```text
nonzero prescribed profile on the outside/left arc,
zero profile on the inside/right part.                  (7.2)
```

The obstruction can also be stated directly on the full contour.  Uniform
polynomial approximation on a Jordan curve is not arbitrary contour-only
approximation: the limit must be the boundary trace of a function
holomorphic in the filled interior.  A trace which vanishes on a nontrivial
analytic boundary arc but is nonzero on another arc is not such a trace.
This is the same hull obstruction in its Rouche-relevant form.

There is also a basic compactness warning.  A compact subset strictly in
`Re(s)<1` has a positive distance from the transition line.  It can
therefore be treated by Theorems 2.1--3.1, but it cannot by itself include
all points of a connected contour up to a crossing of `Re(s)=1`.  Closing
the missing transition pieces either destroys the fixed separation used in
(1.8), or creates the filled lens just described.  Letting the separation
tend to zero with `H` makes `r-1`, the Bernstein--Walsh rate, and the degree
ratio `d` nonuniform; no fixed-power theorem follows from the present
estimates.

This explains the exact difference between the two approximation tasks:

```text
isolated patches or filled islands outside the unit disk
    complement connected; arbitrary local analytic data are shapeable;

one closed transition contour
    hull fills the localization domain; boundary data must be globally
    holomorphically compatible.                           (7.3)
```

Rouche's theorem needs the second task, not merely the first.  Therefore a
proof which covers many small contour patches independently but does not
verify hull compatibility has not constructed a localization contour.

## 8. Consequences for the fixed-strip program

The finite-union extension settles the local analytic-control question as
far as this mechanism can settle it:

```text
one conjugate filled-disc pair                            R163
finitely many separated conjugate compacta               THEOREM
exponentially small coefficient ell^1 norm                THEOREM
right extinction in Re(s)>=1                              THEOREM
exact logarithmic density                                 THEOREM
actual-prime lift for sigma_0>7/12                        THEOREM
one sign per actual prime                                 THEOREM
nontrivial left / zero right completed contour            HULL NO-GO
fixed uniform zero-free strip                             NOT PROVED
nonexistence of a fixed zero-free strip                   NOT PROVED
```

The obstruction is to this localization mechanism, not to a zero-free
strip for zeta.  It leaves three logically possible escape routes:

1. prescribe one globally holomorphic, hull-compatible target instead of a
   left/right analytic cutoff;
2. use rational or meromorphic controls with poles in the filled holes and
   include their divisor contribution explicitly in the argument principle;
3. avoid transition extinction and prove a lower bound for the full
   collective cofactor directly on the completed contour.

The first route cannot use a function that is identically zero on an open
right region and nonzero on the connected filled domain, by the identity
theorem.  The second changes the divisor ledger and so is not available from
prime Dirichlet polynomials alone.  The third is the remaining route most
compatible with R164--R167: the local prime shaping is now strong enough on
any separated finite skeleton, but the global cofactor and its winding must
be controlled without an analytic cutoff.
