# QP packet-free broad rectangles: the error-labelled spectral coherence gate

**Date:** 2026-08-24  
**Verdict:** labelling every retained point by its individual product error
gives an exact two-frequency fourth-moment decomposition, but it does not by
itself give the missing square-root.  Low one-error codegrees control only
individual fibres.  Even an assumed `O(1)` pair-cell codegree controls only
the tagged Hilbert--Schmidt mass; the desired completion energy is the
coherent zero error-frequency slice.

The exact surviving factor is an error-coherence Rayleigh quotient.  The
required theorem is that this quotient is `D^(1/2+o(1))` on the physical,
post-peeling broad kernel.  Cotlar--Stein, an ordinary nonbacktracking trace,
entropy decrement, and the graph-weighted Yao identity all leave this same
factor untouched.

No packet-free reciprocal-energy theorem or sharp four-cycle theorem is
proved here.

## 1. The physical post-peeling operator

Fix an endpoint and write

```text
C=T/x asymp q^2,
P_0={(a,v):a,v in I_q, |a*v-C|<=c_0*D}                (1.1)
```

for the points left after the already justified affine/Hankel packet peel.
Replace `C` by a nearest integer `N_0` only in the label and put

```text
epsilon(a,v)=a*v-N_0 in Z,       |epsilon|<<D.         (1.2)
```

This fixed translation does not change any equality between sums of two
errors.  For an ordered pair `pi=(i,j)` of retained points define

```text
n(pi)=a_i+a_j,             eta(pi)=epsilon_i+epsilon_j. (1.3)
```

If `pi=(00,11)` and `rho=(10,01)` have the same completion sum, put

```text
r=a_10-a_00,      s=a_01-a_00,
a_11=a_00+r+s.                                      (1.4)
```

The definition of `|r*s|` is unchanged by either ordering of the two
diagonals.  On ordered-pair space the broad rectangle kernel is

```text
K_br(pi,rho)
 =1_(n(pi)=n(rho)) 1_(|r*s|>=c*q)                    (1.5)
```

with the peeled pairs removed.  If `w_(i,j)=z_i z_j`, the desired weighted
broad estimate follows from the square-root restricted-type bound

```text
<w,K_br w><<D^(1/2)q^o(1)||z||_2^4.                  (1.6)
```

For flat weights and `|P_0|=H<=D`, (1.6) is the required
`D^(5/2+o(1))` count.  The proved reciprocal mixed-difference lemma disposes
of the complement `|r*s|<c*q` in `O(D^2 log q)`, so (1.6) is exactly the
remaining broad scale, not a replacement of the physical product bands.

The error difference across a rectangle is

```text
delta=eta(pi)-eta(rho)
     =epsilon_00+epsilon_11-epsilon_10-epsilon_01.    (1.7)
```

Writing `t=v_00+v_11-v_10-v_01`, direct expansion gives the exact identity

```text
delta=a_00*t
      +r*(v_11-v_10)+s*(v_11-v_01).                  (1.8)
```

For a broad rectangle the three terms on the right can each be large and
cancel down to `O(D)`.  Thus broad separation does **not** create separation
of the error blocks.  Any Cotlar decay in `|delta|` would need a new
arithmetic argument.

## 2. Exact tagged fourth moment and the surviving quotient

For flat weights first put

```text
B(n,eta)=#{(i,j):n(i,j)=n, eta(i,j)=eta}.             (2.1)
```

Then the uncut completion energy and the error-tagged energy are exactly

```text
E_a       =sum_n   (sum_eta B(n,eta))^2,
E_tag     =sum_n,eta B(n,eta)^2.                      (2.2)
```

The broad energy is obtained from the first expression by deleting the
narrow and peeled pair-of-pair terms.  Since those deleted terms are already
controlled, it is enough to understand why the full error decomposition
does not automatically improve (2.2).

Let `b_eta=(B(n,eta))_n` and let

```text
G_(eta,eta')=<b_eta,b_eta'>.                          (2.3)
```

Thus

```text
E_a=1^*G1,             E_tag=tr(G),
C_err:=E_a/E_tag.                                     (2.4)
```

`C_err` is the exact error-coherence quotient.  Equivalently,

```text
E_a=E_tag
    +sum_n sum_(eta!=eta') B(n,eta)B(n,eta').         (2.5)
```

The second term in (2.5), restricted to broad post-peeling rectangles, is
the surviving norm term.

Let

```text
mu_2=max_(n,eta) B(n,eta).                            (2.6)
```

Since `sum B=H^2`, one has

```text
E_tag<=mu_2 H^2,
E_a<=C_err*mu_2 H^2.                                 (2.7)
```

Consequently the sufficient spectral statement is

```text
C_err*mu_2<<D^(1/2)q^o(1).                           (2.8)
```

The physical one-error fibre does satisfy

```text
#{(a,v) in P_0:epsilon(a,v)=e}
 <=tau(N_0+e)=q^o(1).                                (2.9)
```

But (2.9) neither bounds the two-product cell (2.6) nor the off-diagonal
sum in (2.5).  More importantly, even granting the stronger hypothesis
`mu_2=O(1)`, Cauchy only gives `C_err<<D`, producing `D^3`.  The missing
square root is precisely the improvement `C_err<<sqrt(D)q^o(1)`.

The weighted version replaces `B(n,eta)` by

```text
B_z(n,eta)
 =sum_(i,j) z_i z_j 1_(n(i,j)=n)1_(eta(i,j)=eta).     (2.10)
```

For a uniform coefficient theorem one may majorize by `B_|z|`.  No
oscillation in the original coefficients can be assumed.

## 3. The centered two-frequency identity

Choose an auxiliary prime `p asymp q` large enough that the completion and
error sums do not wrap.  Set

```text
S(xi,theta)
 =sum_(i in P_0) z_i e_p(xi*a_i+theta*epsilon_i).     (3.1)
```

Two applications of additive orthogonality give

```text
(1/p^2) sum_(xi,theta)|S(xi,theta)|^4=E_tag(z),
(1/p)   sum_xi        |S(xi,0)|^4=E_a(z).             (3.2)
```

Removing the completion zero mode gives the exact centered identity

```text
(1/p)sum_(xi!=0)|S(xi,0)|^4
 =E_a(z)-|sum_i z_i|^4/p.                            (3.3)
```

At `p asymp q=D^(33/16)` and `H<=D`, the flat baseline is at most

```text
H^4/p<=D^(31/16),                                    (3.4)
```

far below `D^(5/2)`.  Centering therefore does not remove (2.5).

Equation (3.2) shows the polarity exactly: orthogonality controls the
average over `theta`, whereas the physical energy is the exceptional slice
`theta=0`.  Restriction of a trigonometric polynomial with `O(D)` error-sum
frequencies gives only

```text
E_a<=O(D) E_tag,                                     (3.5)
```

which is the `D^3` ledger when `mu_2=O(1)`.  A
`sqrt(D)` restriction gain at `theta=0` is a new theorem, not a consequence
of the centered identity.

## 4. Audit of the four proposed mechanisms

### 4.1 Cotlar--Stein

Decomposing (1.5) by `eta` produces blocks
`P_eta K_br P_eta'`.  One-error codegrees control the sizes of the diagonal
fibres, but Cotlar--Stein needs a summable cross-block norm.  In the positive
flat case its cross-Gram contribution is exactly the second term of (2.5).
There is no proved decay with `|eta-eta'|`; (1.8) explains why broad
curvature alone supplies none.  The Cotlar row sum is therefore the missing
coherence bound (2.8) in another notation.

### 4.2 Nonbacktracking trace

View `B` as the weighted incidence matrix between completion sums `n` and
error sums `eta`.  The quantity `E_a` counts pairs of length-two walks with
the same left endpoint.  A high-degree left star contributes its degree
squared and has no nonbacktracking cycle.  Removing literal backtracks
leaves the off-diagonal pairs in that same star.  Global constant
subtraction leaves the variance of the left-degree vector, which can still
be cubic.  A trace argument must therefore first prove a physical
degree-covariance estimate; high trace does not manufacture it.

### 4.3 Entropy decrement

Let two ordered retained points be chosen independently and put

```text
X=a_1+a_2,                Y=epsilon_1+epsilon_2.      (4.1)
```

For two independent copies,

```text
Pr(X=X')=E_a/H^4,
Pr((X,Y)=(X',Y'))=E_tag/H^4.                          (4.2)
```

Hence `C_err` is the ratio of these collision probabilities, a conditional
Renyi-coherence factor.  High conditional entropy of `Y` given `X` makes
this ratio larger, not smaller: the physical count adds all `Y` coherently.
An entropy decrement can locate a scale of weak mutual information, but it
cannot turn positivity at the fixed zero error-frequency into cancellation.
It closes only if supplemented by the very bound (2.8) being sought.

### 4.4 Weighted Yao identity

Modulo `p`, the product relation reads

```text
a=(N_0+epsilon)*v^(-1).                              (4.3)
```

Thus (3.1) is a graph-weighted ratio sum whose numerator varies with the
selected carrier.  Yao's Cartesian fourth-moment saving uses one common
numerator set for every denominator.  That common-dilate energy is absent
for the physical matching `(epsilon,v)`.  The weighted centering identity
itself remains true--it is (3.2)--but its saving controls the two-frequency
average, not the zero error-frequency slice.  Applying Yao after Cartesian
completion again loses much more than the required square root.

## 5. A method fixture, not a physical-shell counterexample

The following construction is deliberately limited to the hypotheses seen
by the four mechanisms above.  It keeps an exact common product centre and
individual integer product bands, has optimal one- and two-error
codegrees, and can be made packet-free in the `(a,v)` projection.  It does
**not** put `a` and `v` in one common `q`-shell and does not use prime powers.
It therefore cannot refute the physical theorem.

Let `N>=4`, let

```text
L=product_(prime l<=N) l,             a_j=1+jL,       (5.1)
```

and choose a prime `p` with `2N<p<4N`.  Let `epsilon_j` be the centered
integer representative of `j^2 (mod p)`.  The `a_j` are pairwise coprime:
a common prime divisor would divide `(i-j)L`; primes at most `N` divide
`L`, while primes larger than `N` cannot divide `i-j`.

The Chinese remainder theorem supplies

```text
C ==-epsilon_j (mod a_j)       for every j.           (5.2)
```

Putting

```text
v_j=(C+epsilon_j)/a_j                                  (5.3)
```

gives positive integers with

```text
a_j v_j-C=epsilon_j,           |epsilon_j|<2N.        (5.4)
```

The CRT solution may be shifted by multiples of `product_j a_j`.  Each
triple excludes at most one shift from being collinear in `(a,v)`, because
the coefficient of `C` is the nonzero divided difference of the strictly
convex function `1/a`.  Avoiding finitely many shifts makes the fixture
packet-free in that projection.  Reduction modulo `p` also shows that no
three `(a_j,epsilon_j)` are collinear.

Nevertheless the completions form an arithmetic progression, so

```text
E_a=(2N^3+N)/3.                                      (5.5)
```

If two ordered pairs have both the same completion sum and the same error
sum, reduction modulo `p` fixes their sum and sum of squares, hence fixes
the unordered pair.  Therefore

```text
max_e #{j:epsilon_j=e}=1,
mu_2=2,
E_tag=2N^2-N,                                        (5.6)

C_err=(2N^3+N)/(3(2N^2-N))=N/3+O(1).                (5.7)
```

Thus low codegrees, two-frequency orthogonality, no three collinear points,
and even the bare equations `a_jv_j=C+epsilon_j` permit full `D` coherence
when `N asymp D`.  What fails is exactly the physical common-shell relation

```text
a_j asymp v_j asymp q,              C asymp q^2.      (5.8)
```

Indeed the CRT centre is at least a product of all the `a_j`, so the
carriers are vastly larger than the completions.  The fixture is faithful
as a no-go for methods that discard (5.8), and nothing more.

The exact construction and identities are replayed in
`src/qp_error_labelled_spectral_gate.py` and
`src/test_qp_error_labelled_spectral_gate.py`.

## 6. Stronger shell-only theorem: plausible, but still open

The spectral discussion suggests testing the stronger statement before any
packet peel.  For fixed `C asymp q^2`, put

```text
A(C,D)={a in I_q:there is v in I_q with |a*v-C|<=D}. (6.1)
```

Since `q>>D`, the admissible `v` is unique for each `a`.  Also

```text
|A(C,D)|
 <=sum_(integer n:|n-C|<=D) tau(n)
 <<D*q^o(1).                                         (6.2)
```

Thus the uniform conjecture

```text
E^+(A(C,D))<<D^(5/2)q^o(1)                           (6.3)
```

would imply the packet-free projection theorem immediately.  No power
counterexample to (6.3) was found.

### 6.1 What convexity does and does not give

On occupied points

```text
v(a)=C/a+O(D/q).                                     (6.4)
```

The reciprocal graph is strictly convex, and its mixed second and third
differences give the proved rectangle/cube rounding laws.  But the energy
in (6.3) is the energy of the **first-coordinate projection**.  Classical
`|A|^(5/2)` convex-sequence energy bounds apply when the values whose sums
are counted have strictly monotone gaps.  They do not apply to arbitrary
first coordinates merely because `(a,v(a))` lies near a convex curve.  The
continuous model with consecutive `a` and `v=C/a` already has cubic
first-coordinate energy.  Integrality and the width-`D` product strip are
therefore indispensable.

Known short-arc results for exact lattice points on one hyperbola likewise
do not count additive quadruples drawn from the union of the `O(D)` nearby
levels `a*v=C+e`.  They control a different statistic.

### 6.2 The genuine tangent resonance is subcritical

Take an integer `Q asymp q` and `C=Q^2`.  For every integer
`|h|<=L=floor(sqrt(D))`,

```text
a_h=Q+h,          v_h=Q-h,
a_h*v_h-C=-h^2.                                    (6.5)
```

All points remain in one fixed shell when `L=o(Q)`.  Hence `A(C,D)` can
contain a consecutive block of length `asymp sqrt(D)`, and this block has

```text
E^+ asymp L^3 asymp D^(3/2).                         (6.6)
```

It is exactly the affine tangent packet `a+v=2Q`, so the packet peel removes
it.  More importantly for the stronger theorem, (6.6) is a full power
below the proposed `D^(5/2)` ceiling.  Divisor multiplicities can change
this by `q^o(1)`, not by a fixed power.  Thus the obvious resonant centres
explain sharp local square-root clusters but do not refute (6.3).

### 6.3 Exact remaining autocorrelation

Let

```text
R(r)=#{a:a,a+r in A(C,D)}.                            (6.7)
```

Then

```text
E^+(A)=sum_r R(r)^2,             sum_r R(r)=|A|^2.   (6.8)
```

The tangent example has `R(r)asymp sqrt(D)` for its short shifts.  Thus the
natural pointwise estimate

```text
R(r)<<sqrt(D)q^o(1),             r!=0,               (6.9)
```

would be sharp and would prove (6.3), after the diagonal.  It is not
currently proved.

If `p=v(a+r)-v(a)` and the two individual errors differ by `d`, the exact
secant equation is

```text
a*p+r*v(a)+r*p=d,                |d|<=2D.             (6.10)
```

For fixed `(r,p)` this confines bases to a branch of length `O(1+D/|r|)`,
but there are `asymp |r|` possible carrier steps.  Summing the branches
restores `O(D)`.  Repeated edges may be disjoint, so packet-freeness alone
does not improve that sum.  Equation (6.10), or an averaged version of
(6.9), is the exact stronger shell-only gate.

## 7. Broad cubes and `U^3` do not yet close

For positive directions define

```text
c(r,s)=#{a:a,a+r,a+s,a+r+s in A(C,D)}.               (7.1)
```

Then rectangle energy is `sum_(r,s)c(r,s)`, whereas the number of translated
three-dimensional cubes with those first two directions is

```text
sum_(r,s)c(r,s)^2.                                   (7.2)
```

The diagonal in (7.2) already contributes the original rectangles.  There
is no lower bound for **nontrivial** translated cubes if the broad
rectangles are distributed with `c(r,s)=1`.  Even Cauchy over the ambient
`O(q^2)` direction pairs gives only

```text
sum c(r,s)^2 >=E_br^2/q^2.                           (7.3)
```

At `E_br=D^(5/2)` and `q=D^(33/16)`, the right side is merely
`D^(7/8)`, weaker than the unavoidable diagonal contribution.  Thus the
formal monotonicity from `U^2` to `U^3` supplies no recurrence.

The exact product-error cube theorem says that for a broad rectangle of
mixed carrier label `t asymp |r*s|/q`, two bases separated by `u` obey

```text
|u|<<D/|t|        or        |u*r*s|>>q^2.             (7.4)
```

The first alternative is not forbidden.  At the balanced scale
`|r*s|asymp q`, all repeated bases may lie in one interval of length
`O(D)`; this can support `c(r,s)` as large as `D` without producing a
broad cube or a `3 x 2` extension in the original side directions.  A
`U^3` argument therefore reaches the already isolated recurrence gate:
one still needs to show that too much rectangle mass cannot be packed into
these allowed short base clusters.

## 8. Binary status

```text
physical error-labelled broad operator:                FORMULATED;
one-error divisor codegree q^o(1):                     PROVED;
one-error codegree controls pair cells mu_2:           NO;
tagged two-frequency identity:                         PROVED;
centered zero-completion-mode subtraction:             PROVED, TOO SMALL;
Cotlar cross-error summability:                        OPEN / SAME GATE;
nonbacktracking trace removes left-star covariance:    NO;
entropy decrement controls positive zero slice:        NO;
Yao Cartesian saving survives graph matching:          NO;
exact surviving term: broad part of (2.5);
required new input: C_err*mu_2<<sqrt(D)q^o(1);
stronger shell-only energy theorem (6.3):             OPEN, PLAUSIBLE;
tangent resonance gives a power counterexample:      NO, ONLY D^(3/2);
broad-cube volume plus U^3 closes recurrence:         NO;
packet-free reciprocal energy D^(5/2+o(1)):            OPEN;
sharp four-cycle theorem:                              NOT PROVED.
```
