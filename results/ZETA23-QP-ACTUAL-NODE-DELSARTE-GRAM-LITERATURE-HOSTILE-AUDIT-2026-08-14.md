# Actual-node Delsarte and projected-Gram hostile literature audit

**Date:** 2026-08-14
**Verdict:** no surveyed theorem supplies the prescribed actual-prime,
pointwise full-band, fixed-power estimate.  The general large-value theorem
does give the optimally scaled sparse packet count, but packet count is not a
Gram lower bound and not an off-packet leverage estimate.  In fact, the
suggested *uniform* projected-Gram lower bound is false: consecutive packet
centres have a universal binomial finite-difference near-null direction whose
eigenvalue is exponentially small in the cluster length, including on the
actual prime nodes.  Restricted
invertibility, Kadison--Singer/paving, spectral sparsification, vector
balancing, and positive-quadrature theorems all lose at least one required
quantifier.

One typographically easy-to-misread primary-source point matters:
Klurman--Mangerel--Teravainen Lemma 7.9 sets

```text
X=x^((log x)^(1/25)),   |t|<=X.                      (0.1)
```

The outer exponent on `x` is present in the arXiv TeX and is flattened
ambiguously by PDF text extraction.  Thus the lemma easily covers every
fixed polynomial height, including `B=Y^(50/33)`.  Its limitation here is
the logarithmic saving and natural, non-adaptive coefficient sequence, not
the height range.

Nothing here proves QP-PROMOTE, QP-KILL, or a zero-free strip.

---

## 1. Exact target, with all quantifiers visible

At the fixed active slice `d=33/50`, let

```text
u_j=|log(n_j/Y)|,       M=Y^(1-o(1)),
a(t)=(cos(tu_j))_(j<=M),
H=[Y^.01,Y^(50/33)].                                  (1.1)
```

The exact actual-node Delsarte value is

```text
A_H=sup {Q(0):
 Q(t)=1+sum_j lambda_j cos(tu_j),
 lambda_j real, Q(t)>=0 for every t in H}.            (1.2)
```

Whenever the spectral-null feasible set is nonempty,

```text
r_+(H)=1/(A_H-1).                                    (1.3)
```

Thus the positive route is killed at power `c` exactly by

```text
A_H>=1+Y^(c-o(1)).                                   (1.4)
```

A stronger positive-coefficient sufficient condition is to find

```text
lambda_j>=0,  sum_j lambda_j=1,
inf_(t in H) sum_j lambda_j cos(tu_j)
    >=-Y^(-c+o(1)).                                  (1.5)
```

For fixed `d=33/50`, `c=.019` clears the audited carrier bill.  It does not
clear the cached `d=.665` or full `d<2/3` bills; those are respectively
`.01974048258...` and `.02007514816...`.

The three non-negotiable features of (1.4) or (1.5) are:

1. the spectral coordinates are the **prescribed actual prime-power logs**;
2. the inequality is pointwise at **every** `t` in the full legal band;
3. the error is a **fixed power**, not a logarithmic or almost-everywhere
   saving.

---

## 2. What a projected-Gram repair would quantitatively require

Let `t_1,...,t_R` be one-separated bad-packet centres, put

```text
q=(1,...,1)^T,       P_q=I-qq^T/M,
v_i=P_q a(t_i),       V=[v_1 ... v_R],
G=V^T V.                                               (2.1)
```

For demands `d=(d_i)`, the minimum-norm carrier-null correction is

```text
delta=V G^(-1)d,
||delta||_2^2=d^T G^(-1)d.                            (2.2)
```

At a query `t`, define

```text
k(t)=V^T P_q a(t),
L_T(t)=k(t)^T G^(-1)k(t)/||P_q a(t)||_2^2.            (2.3)
```

Suppose, ideally, that

```text
lambda_min(G)>=gamma M,       ||d||_infinity<=D.       (2.4)
```

Then the exact Schur estimate gives

```text
|delta^T a(t)|
 <=D sqrt(R L_T(t)/gamma).                            (2.5)
```

At threshold `epsilon=Y^-c`, large-value theory permits
`R<=Y^(2c+o(1))`.  For unit-size demands, (2.5) is at most `epsilon` if

```text
L_T(t)<=gamma epsilon^2/R
       =gamma Y^(-4c+o(1))                            (2.6)
```

off the notched packets.  Packet jets are additionally needed to control
the complete unit intervals.  Demand dyadicization can weaken the
unit-demand assumption, but it does not remove either (2.4) or (2.6).

This is a useful sufficient worst-case interface, but it cannot hold
uniformly for all possible sparse packet sets.  If

```text
t_k=t_0+kh,   0<=k<=m,   0<hw<=pi,
```

and `G` is their projected cosine Gramian, the binomial vector
`c_k=(-1)^(m-k) binom(m,k)` gives the exact universal bound

```text
lambda_min(G)/M
 <=[2 sin(hw/2)]^(2m)/binom(2m,m)
 =sqrt(pi*m)(1+o(1)) sin(hw/2)^(2m).                 (2.7)
```

For `w=1/5,h=1`, this is

```text
lambda_min(G)/M<=exp[-(4.608504631...+o(1))m].        (2.8)
```

The proof is simply

```text
sum_k c_k exp(i(t_0+kh)u)
 =exp(it_0u)(exp(ihu)-1)^m,                          (2.9)
```

followed by projection and the Rayleigh principle.  A packet count allows
such a cluster and therefore cannot imply (2.4), even for the actual nodes.
The same identity makes the next omitted consecutive atom exponentially
close to the fitted span, so deleting only fitted centres does not imply
(2.6) either.

This does not refute demand-specific repair: the actual correction source may
have negligible component in the near-null direction.  The exact surviving
invariant is narrower.  Put `A=[a(t_1),...,a(t_R)]`,

```text
m=A^T q/M,   V=(I-qq^T/M)A,   G=V^T V.
```

When `G` is nonsingular, the minimum-norm carrier-normalized vector zeroing
those centres is

```text
y_*=-q/M+V G^(-1)m,
||y_*||_2^2=1/M+z_T,   z_T=m^T G^(-1)m,              (2.10)
z_T=sup_c (mean_j F_c(u_j))^2
          /sum_j |F_c(u_j)-mean_l F_c(u_l)|^2,       (2.11)
F_c(u)=sum_i c_i cos(t_i u).
```

Equivalently, if `Pi_T` projects onto the columns of `A`,
`R_T=(I-Pi_T)q`, and `R_T!=0`, then

```text
y_*=-R_T/||R_T||_2^2.                                (2.12)
```

The complete one-sided repair condition is exactly

```text
R_T^T a(t)>=-epsilon ||R_T||_2^2   for every t in H. (2.13)
```

Or, separating source and propagation, the sharp directional term is
`|m^T G^(-1)k(t)|`, not `lambda_min(G)` by itself.  No surveyed theorem
controls (2.11)--(2.13) for adaptively selected actual-prime packets.  Full
details and replay are in
[`ZETA23-QP-PROJECTED-GRAM-CLUSTER-AND-SOURCE-GATE-2026-08-14.md`](ZETA23-QP-PROJECTED-GRAM-CLUSTER-AND-SOURCE-GATE-2026-08-14.md).

---

## 3. Guth--Maynard gives the packet count, and exactly no more

The current primary large-value theorem of
[Guth--Maynard](https://arxiv.org/abs/2405.20552), Theorem 1.1, states that
if `|b_n|<=1`, the points `t_r in [0,T]` are one-separated, and

```text
|sum_(N<n<=2N)b_n n^(it_r)|>=V,
```

then

```text
R<=T^o(1){N^2 V^-2+N^(18/5)V^-4+T N^(12/5)V^-4}.     (3.1)
```

For a prime-supported polynomial, `N~Y`,
`V=Y^(1-c-o(1))`, and `T=Y^(50/33)`, the three powers are

```text
Y^(2c+o(1)),
Y^(-2/5+4c+o(1)),
Y^(50/33-8/5+4c+o(1)).                               (3.2)
```

At `c=.019`, the last two exponents are negative, so (3.1) gives precisely

```text
R<=Y^(.038+o(1)).                                    (3.3)
```

This is genuine and useful.  It does not imply (2.4): the theorem bounds the
cardinality of the value set, not the smallest singular value of its
evaluation matrix.  It does not imply (2.6): it contains no query-versus-
packet Schur complement.  It also discards the sign of the large value.

The first term `N^2V^-2` is the natural large-value scale and is attained by
general Dirichlet-polynomial examples discussed in the same paper.  Thus no
formal manipulation of (3.1) can turn `R<=Y^(2c)` into `R=0`.  Any such
upgrade must use additional actual-prime structure.

---

## 4. Restricted invertibility selects columns; QP must retain all packets

The Spielman--Srivastava form of the
[Bourgain--Tzafriri restricted-invertibility theorem](https://arxiv.org/abs/0911.1114)
selects a well-invertible column subset whose size is proportional to the
stable rank

```text
sr(V)=||V||_F^2/||V||_op^2.                           (4.1)
```

It does not lower-bound the Gramian of a prescribed column set.  Applied to
the packet matrix, it may discard exactly the packet constraints that must
be repaired.  Iterating on discarded packets does not solve this: every new
correction is governed by the off-span leverage (2.3), which restricted
invertibility does not bound.

Nor is the stable-rank input free.  From column norms `asymp sqrt(M)` alone,
the trivial operator bound permits `sr(V)=1`.  A bound
`||V||_op^2=Y^o(1)M` strong enough to make `sr(V)~R` is already a collective
actual-prime large-sieve/Gram theorem for those adversarial packet centres.

The direction mismatch is therefore definitive:

```text
restricted invertibility:  choose a good subset of constraints;
QP packet repair:           solve every bad constraint and control all
                            queries outside their span.             (4.2)
```

---

## 5. Kadison--Singer and sparsification assume the missing frame

The Marcus--Spielman--Srivastava
[Kadison--Singer theorem](https://arxiv.org/abs/1306.3969) partitions an
isotropic small-norm vector family into pieces with controlled **upper**
frame operators.  To put the packet columns into isotropic position one
must whiten by their frame operator.  That requires the invertibility and
conditioning whose quantitative content is (2.4).  Paving then gives no
off-packet estimate of the form (2.6).

[Batson--Spielman--Srivastava sparsification](https://arxiv.org/abs/0808.0163)
selects positive weighted rank-one terms which approximate an already known
positive semidefinite sum.  It preserves the condition number of that sum;
it does not improve a singular packet Gramian.  If applied on the node side,
it may compress an established frame, but it supplies neither the carrier
normalization nor the one-sided sign of (1.2).  If applied on the packet
side, it again drops interpolation constraints.

Consequently neither theorem repairs all sparse packets.  Whitening is not a
workaround; it assumes a frame lower bound which (2.7) shows is false for
general clustered packet lists.  The only still-live version is the
directional source/residual condition (2.11)--(2.13).

---

## 6. Vector balancing cannot create the carrier-aware fractional solution

[Spencer's theorem](https://doi.org/10.1090/S0002-9947-1985-0784009-0),
[Banaszczyk's Gaussian vector-balancing theorem](https://doi.org/10.1002/%28SICI%291098-2418%28199807%2912%3A4%3C351%3A%3AAID-RSA3%3E3.0.CO%3B2-S),
and constructive partial coloring such as
[Lovett--Meka](https://arxiv.org/abs/1203.5747) choose signs or round a
fractional vector while controlling finitely many linear discrepancies.
Banaszczyk's original theorem permits an arbitrary convex body, not merely a
centred symmetric one, but requires that body to have standard Gaussian
measure at least `1/2` (up to the universal dilation in the usual
normalization).

For positive coefficients a grid of polynomial cardinality would be enough:
`|P_lambda'(t)|<=w` when `lambda` is a probability.  The obstruction is not
the continuum net.  It is the affine carrier and the source correlation.

1. A balanced sign vector has carrier `sum_j epsilon_j` only of square-root
   scale.  After normalizing that carrier to one, its square-root discrepancy
   is order one, not `Y^-c`.
2. An affine target can formally be encoded by translating the convex body,
   but Gaussian measure is not translation invariant.  Repairing a
   systematic bad packet asks the signed sum to move a macroscopic distance
   in its source-correlated direction while retaining fixed-power tolerance.
   The corresponding translated one-sided body has no available
   `gamma_R(K)>=1/2` bound; at the critical scaling its target lies far beyond
   the Gaussian fluctuation scale.  Banaszczyk therefore gives no such
   prescribed correction.
3. Rounding a positive fractional vector preserves its existing transform
   up to a small discrepancy.  It cannot remove a systematic bad packet of
   the fractional transform.  One must first exhibit a fractional vector
   satisfying (1.5), which is exactly the Delsarte problem.
4. Appending the carrier as one more discrepancy row controls its absolute
   error near zero; it does not force the large nonzero affine value needed
   for normalization.

Thus discrepancy theory can discretize or round an antenna already known to
exist.  It does not manufacture the required carrier-aware one-sided
antenna from the actual nodes.

This is not just a failure to optimize constants.  There are abstract
bounded-entry matrices at the critical count `R=epsilon^-2` whose packet
columns are perfectly orthogonal and all have uniform mean `-epsilon`, yet
their carrier lies exactly in the packet span and the finite-set minimax
value is exactly `epsilon`.  One construction takes as rows all sign vectors
`x in {-1,1}^R` with `sum_i x_i=-sqrt(R)` (for even `sqrt(R)`).  Then

```text
A^T A=M I,       A^T q/M=-epsilon q_R,
A(q_R/R)=-epsilon q,
inf_(q^T y=-1) max_i a_i^T y=epsilon.                (6.1)
```

A regular-Hadamard subfamily realizes the same identities with `M=R` and
allows arbitrary row repetition.  This is not an actual-prime cosine
matrix; it proves that sharp packet count, bounded atoms, negative source
means, and even ideal unprojected orthogonality do not suffice for a
balancing theorem.  Actual phase structure must enter.

---

## 7. Positive quadrature chooses nodes or stops at the Nyquist scale

[Tchakaloff's theorem](https://arxiv.org/abs/math/0207065) produces a
positive quadrature of prescribed finite degree, but its quadrature nodes
are selected as part of the conclusion.  The discrete version can compress
an already valid quadrature to a subset of its support.  It does not assert
that a prescribed prime-log set represents the continuum tent moments.
That prescribed-support statement is precisely the convex-hull feasibility
in (1.5).

Marcinkiewicz--Zygmund and scattered-data positive-quadrature theorems need
sampling density at the function-space resolution.  For bandwidth `D`, the
one-dimensional condition is of Nyquist form

```text
(fill distance)*D=O(1).                              (7.1)
```

The published prime mesh is `h_Y<<Y^(-19/40)`, so this mechanism reaches
only `D<Y^(19/40-o(1))`, exactly the already proved truncated antenna.  At
the full aperture,

```text
B h_Y=Y^(50/33-19/40)=Y^(1373/1320),                 (7.2)
```

and no prescribed-node positive-quadrature theorem applies.  Uniform meshes
have exact aliases beyond their Nyquist scale, so (7.1) is a genuine scope
condition rather than a technical defect.

There is also a dimensionally exact no-go for **full exact** positive
quadrature.  If an `M`-atomic positive measure integrates every circle mode
`|k|<=n` exactly, its Toeplitz moment matrix on indices `0,...,n` is the
identity of rank `n+1`, while its Vandermonde factorization has rank at most
`M`.  Hence `M>=n+1`.  Here `M=Y^(1+o(1))` and exactness through the aperture
would require `n~B=Y^(50/33)`.  Kunis's
[*Positive quadrature and mobile sampling of multivariate trigonometric
polynomials*](https://arxiv.org/abs/2608.11915), Theorem 3.3 and Remark
3.4(i), gives the complementary covering-radius necessity for positive exact
quadrature.  Neither result rules out the much weaker one-sided inequality
(1.5).

A polarity-correct countermodel does rule out deriving (1.5) from the
currently cached *geometric* prime package alone.  Take a thinned odd
half-period grid

```text
u_j=(2k_j+1)pi/B,
k_(j+1)-k_j~B log(Y)/(2pi Y).                         (7.3)
```

It has `M~Y/log Y`, physical gaps `~log Y`, the corresponding gap-square and
local-density bounds, and can be perturbed invisibly so that
`{2pi,u_1,...,u_M}` is rationally independent.  Nevertheless

```text
cos(Bu_j)=-1+o(1)   for every j,                     (7.4)
```

so every positive probability weighting fails maximally at the legal top
height.  This is not a prime counterexample.  It proves that mesh, gap
moments, low-denominator deletion, and qualitative nonlattice information do
not imply (1.5); an actual multiplicative-arithmetic input is indispensable.
The exact construction and deletion ledger are in
[`ZETA23-QP-ACTUAL-PRIME-POSITIVE-WEIGHT-BARRIER-2026-08-14.md`](ZETA23-QP-ACTUAL-PRIME-POSITIVE-WEIGHT-BARRIER-2026-08-14.md).

---

## 8. Natural prime twists: corrected range and strip-strength boundary

The primary statement of Klurman--Mangerel--Teravainen,
[*Multiplicative functions in short arithmetic progressions*](https://arxiv.org/abs/1909.12280),
Lemma 7.9, is, for a smooth fixed cutoff and small `epsilon`,

```text
|sum_n Lambda(n)chi(n)n^(-it)h(n/x)|
 <<_h epsilon log^3(1/epsilon)x
      +x/(log x)^(.3)+x/(t^2+1),                     (8.1)
```

uniformly for (0.1).  Remark 7.2 permits a sharp cutoff, replacing the last
term by `x/(|t|+1)`.  Since `x^((log x)^(1/25))` exceeds every fixed power of
`x`, this includes `B`.  Even with optimized `epsilon`, however, the middle
term is only logarithmically small, and the coefficients are the natural
von-Mangoldt/character coefficients rather than adaptive Delsarte weights.
The result therefore supplies neither a fixed-power antenna nor the
projected-Gram estimates (2.4)--(2.6).

For the natural unweighted or von-Mangoldt prime polynomial, a uniform
fixed-power theorem is not an innocuous exponential-sum lemma.  Turan's
localization criterion, as reproduced and used by
[Weber](https://arxiv.org/abs/1005.3932), turns suitable uniform local prime
Dirichlet-polynomial bounds into a zero-free region.  Hence such a theorem
cannot be imported as prior technology for this strip project.

This does **not** prove that the adaptive actual-node Delsarte antenna is
equivalent to a strip.  Its coefficients may be signed or geometry-adapted,
so it has fewer arithmetic quantifiers than the natural prime twist.  It
does show that replacing (1.5) by a uniform equal-weight modulus bound asks
for essentially the theorem the architecture is intended to prove.

---

## 9. Quantitative Kronecker and discrepancy retain the same denominator

Quantitative Kronecker theorems bound a first hit from above after imposing
lower bounds for every short integer linear form in the log nodes.  In the
growing dimension `M=Y^(1-o(1))`, the explicit constants are factorial and
linear-form lower bounds contain products of `M` logarithmic heights.  They
are far beyond the polynomial aperture.

The primary statements checked here are
[Gonek--Montgomery](https://doi.org/10.1016/j.indag.2016.02.002),
[Maksimova](https://arxiv.org/abs/2405.07051), and
[Matveev's explicit logarithmic-form bound](https://www.mathnet.ru/eng/im314).
For example, Maksimova's displayed transference constant already contains
`2^(M-2)/(M(M!)^2)` before the needed linear-form separation is inserted.

Erdos--Turan--Koksma discrepancy has the same small denominators
`||h dot u||` in its Fourier error.  It gives neither a deterministic
avoidance theorem nor the one-sided Delsarte polynomial.  Almost-everywhere
metric versions cannot exclude the one actual prime-log orbit.

The generic remote countermodel in the companion audit further shows that
excellent mesh, Q-independence, full spark, and incommensurate legal atoms
are jointly compatible with a fixed-depth promoter.  Any successful theorem
must use more actual arithmetic than these hypotheses encode.

---

## 10. Binary literature disposition

```text
Guth--Maynard sparse bad-packet count:              APPLIES;
sign or emptiness of every bad packet:              NOT PROVIDED;
prescribed packet Gram lower bound:                 NOT PROVIDED;
off-packet Schur leverage Y^(-4c):                  NOT PROVIDED;
count-only uniform packet Gram lower bound:          FALSE BY (2.7);
arbitrary-value polynomial packet right inverse:     FALSE BY (2.7);
demand-specific carrier source/residual bound:       OPEN;
Bourgain--Tzafriri restricted invertibility:        DROPS CONSTRAINTS;
Kadison--Singer/MSS paving:                         ASSUMES FRAME/UPPER ONLY;
BSS spectral sparsification:                       PRESERVES KNOWN FRAME;
Spencer/Banaszczyk/partial coloring:                ROUNDS, NO AFFINE CARRIER;
Tchakaloff positive quadrature:                     CHOOSES NODES;
prescribed-node MZ quadrature:                      STOPS AT NYQUIST;
full exact positive quadrature through B:            DIMENSIONALLY FALSE;
gap/mesh-only positive-weight implication:           FALSE BY HALF-GRID;
KMT pointwise prime twist:                          FULL HEIGHT, LOG SAVING;
natural fixed-power uniform prime twist:            TURAN STRIP-STRENGTH;
quantitative Kronecker/discrepancy:                 SUPERPOLYNOMIAL LOSS;
actual-node Delsarte value A_H at fixed power:       OPEN;
QP-PROMOTE or QP-KILL:                              OPEN.
```

The weakest honest next result is one of:

1. prove (1.4) directly for the actual node set;
2. prove the stronger positive antenna (1.5);
3. for every adaptively produced, cluster-merged actual bad-packet jet set,
   prove the carrier-source bound (2.11) and the one-sided residual condition
   (2.13), or the corresponding directional propagation estimate.

No theorem located in the primary literature supplies any of these three
statements.
