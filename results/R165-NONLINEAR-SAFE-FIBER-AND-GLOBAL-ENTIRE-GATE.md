# R165 nonlinear safe-fiber and global-entire gate

## Status

R164 gives an exact `z`-plane cofactor template on a proper strip.  The
next question is whether several zero-free multipliers can realize a safe
cofactor directly on the full localization bridge, or whether one can avoid
the image-chart problem by finding a global entire identity.

For `q=2`, let

```text
F_(j,H)=Z M_(j,H),             M_(j,H) zero-free,
C_H=2 sum_j w_j M_(j,H)-Z sum_j w_j M_(j,H)^2,            (0.1)
```

where the fixed weights are positive and sum to one.  The following facts
are exact.

1. A safe family with `C_H` zero-free and `F_(j,H)->1` on the right cap
   cannot have a normal family of multiplier ratios.  At least one
   `M_(j,H)/M_(1,H)` must be genuinely nonnormal.
2. Every such nonnormal unit ratio must take any prescribed nonzero value
   other than its cap limit,
   for example `-1`, an unbounded number of times.  For two channels this
   forces the weighted mean `w_1M_1+w_2M_2` to have an unbounded artificial
   zero cloud.
3. There is no global entire escape.  For no fixed finite `J`, positive
   weights, and entire `h_j,k` with `h_j(1)=0` can

   ```text
   2 sum_j w_j exp(h_j)-z sum_j w_j exp(2h_j)=exp(k)       (0.2)
   ```

   hold identically on `C`.
4. The analogous global mixed-product identity

   ```text
   1-product_j[z exp(h_j)-1]=z exp(k)                     (0.3)
   ```

   is impossible for every finite `J` as well.

The global statements follow from Borel's exponential-independence theorem
with polynomial coefficients.  The `z`-weighted quadratic terms in (0.2)
cannot form a vanishing Borel block because their coefficients have one
common sign at the normalization point.  In (0.3), parity kills odd `J`,
while for even `J` the full-subset term has a unique top polynomial degree.

These results close global entire templates and all locally normal
finite-channel sections.  They do not prove that a wildly nonnormal local
section is impossible.  Rather, they identify its unavoidable price: a
diverging ratio-value cloud and hence a diverging local outer-growth ledger.

```text
q=2 cofactor formula                                      EXACT
normal multiplier-ratio section                           IMPOSSIBLE
nonnormal unit ratio                                      NECESSARY
ratio (-1)-point cloud                                    UNBOUNDED
two-channel weighted-mean zero cloud                      UNBOUNDED
global entire q=2 identity                                IMPOSSIBLE
global entire mixed-product identity                      IMPOSSIBLE
wild nonnormal local section with polynomial growth       OPEN
prime realization of such a section                       OPEN
fixed uniform zeta zero-free strip                        NOT PROVED
zeros approaching one                                     NOT PROVED
```

Date: 2026-08-08.

Predecessors:
[`R155-NORMAL-FAMILY-MIXED-VALUE-INEVITABILITY-GATE.md`](R155-NORMAL-FAMILY-MIXED-VALUE-INEVITABILITY-GATE.md),
[`R160-FINITE-COLLECTIVE-CUTOFF-STOKES-HURWITZ-GATE.md`](R160-FINITE-COLLECTIVE-CUTOFF-STOKES-HURWITZ-GATE.md),
and
[`R164-EXPLICIT-Z-PLANE-COLLECTIVE-COFACTOR-TEMPLATE.md`](R164-EXPLICIT-Z-PLANE-COLLECTIVE-COFACTOR-TEMPLATE.md).

## 1. Exact quadratic reduction

Let `Omega` be a simply connected localization domain, let `V` be a
nonempty open right cap in `Omega`, and let `Z` be a fixed holomorphic
function with a finite nonempty zero divisor in `Omega`.  Assume the cap is
disjoint from that divisor.

For fixed positive `w_j` with `sum_j w_j=1`, put

```text
F_j=Z M_j,
P=1-sum_j w_j(F_j-1)^2.                                  (1.1)
```

Direct expansion gives

```text
P=Z C,
C=2 sum_j w_j M_j-Z sum_j w_j M_j^2.                    (1.2)
```

Choose channel `1` as a baseline and set

```text
r_j=M_j/M_1,
A=sum_j w_j r_j,
B=sum_j w_j r_j^2.                                       (1.3)
```

Then

```text
C=M_1[2A-F_1B].                                          (1.4)
```

If `A` and `B` are zero-free, define

```text
G=F_1 B/A.                                                (1.5)
```

Equation (1.4) becomes

```text
C=M_1 A(2-G).                                             (1.6)
```

Thus a safe cofactor turns `G` into a function which omits `2`.  If `A/B`
is a unit, `G` has exactly the fixed zero divisor of `Z`.  This is the
collective version of the R155 scalar gate.

## 2. Normal ratios are impossible

### Theorem 2.1 -- nonlinear normal-ratio gate

There is no sequence of units `M_(j,n)` on `Omega` such that

```text
Z M_(j,n) ->1 locally uniformly on V,                    (2.1)
C_n is zero-free on Omega,                               (2.2)
{M_(j,n)/M_(1,n):n>=1} is normal for every j.            (2.3)
```

#### Proof

On `V`, every ratio in (2.3) tends to one.  From any subsequence, normality
and a diagonal extraction give a further subsequence on which all ratios
converge spherically.  Their limits equal one on `V`, hence equal one on
`Omega` by the meromorphic identity theorem.  Since the limit is finite,
the convergence is locally ordinary.  It follows that the original ratio
families converge locally uniformly to one:

```text
r_(j,n)->1,
A_n->1,
B_n->1.                                                   (2.4)
```

Shrink `Omega` slightly, retaining the prescribed zeros and a nonempty cap
compactly inside it.  For all sufficiently large `n`, both `A_n` and `B_n`
are units there.  Define `G_n` by (1.5).  It has exactly the fixed zeros of
`Z`, tends to one on the cap, and omits `2` by (1.6).  This contradicts
R155, Theorem 2.1.  QED.

The theorem applies to every fixed `J`.  The fact that the normalized
coordinate hyperplane complement has nonhyperbolic directions when
`J>=3` does not by itself help: a successful section must actually enter a
nonnormal direction.  A qualitative Oka existence statement without
quantitative control of that direction would not settle the gate.

## 3. Nonnormality forces an artificial value cloud

The required nonnormality has a divisor cost.

### Lemma 3.1 -- unit-ratio lattice gate

Let `R_n` be units on a simply connected domain `Omega` and suppose
`R_n->1` locally uniformly on a nonempty open set `V`.  Fix
`a in C*\{1}`.  If the number of distinct solutions of

```text
R_n(s)=a                                                   (3.1)
```

is uniformly bounded, then `R_n->1` locally uniformly throughout `Omega`.

#### Proof

Choose the global logarithm

```text
R_n=exp(H_n)                                              (3.2)
```

whose branch tends to zero on `V`.  If `ell` is one logarithm of `a`, then

```text
R_n=a  iff  H_n in {ell+2 pi i k:k in Z}.                (3.3)
```

If (3.1) has at most `N` distinct solutions, the image of `H_n` meets at
most `N` values of the lattice in (3.3).  Among any fixed `N+2` lattice
values, at least two are omitted.  Passing to a subsequence fixes the same
omitted pair.  Montel's theorem makes that subsequence normal.  Its limit is
zero on `V`, hence zero throughout `Omega`; therefore `R_n->1`.  QED.

Combining Theorem 2.1 and Lemma 3.1 proves:

### Corollary 3.2 -- mandatory ratio cloud

Every safe fixed-channel family has indices `j` and a subsequence for which

```text
# distinct {s in Omega:M_(j,n)(s)+M_(1,n)(s)=0}->infinity. (3.4)
```

For `J=2`, take `R=M_1/M_2`.  The weighted mean vanishes exactly when

```text
w_1M_1+w_2M_2=0
iff
R=-w_2/w_1.                                               (3.5)
```

Hence every safe two-channel family must satisfy

```text
# distinct zeros of (w_1M_1+w_2M_2) ->infinity           (3.6)
```

along a subsequence.  The extra channel does not erase the scalar mixed
cloud; it exports it into the multiplier-ratio geometry.

Polynomial outer growth is compatible with `O(log H)` such points, so
(3.6) is not a full local no-go theorem.  It does rule out a bounded-divisor
or normal Oka section.

## 4. Borel's polynomial-coefficient theorem

We use the following classical form of Borel's theorem.

### Lemma 4.1 -- Borel blocks

Let `p_nu` be nonzero polynomials and `g_nu` entire functions.  If

```text
sum_nu p_nu(z)exp(g_nu(z))=0                              (4.1)
```

identically, the indices can be partitioned into nonempty blocks such that
within each block

```text
g_mu-g_nu is constant,                                   (4.2)
sum_(nu in block) p_nu exp(g_nu)=0.                       (4.3)
```

After one exponential is factored from (4.3), the remaining relation is an
ordinary polynomial identity.

This is the polynomial-coefficient exponential-independence theorem of
Borel.  One reference giving precisely the needed statement is Eremenko--
Rubel, *On the zero sets of certain entire functions*, Proc. AMS 124
(1996), 2401--2404, p. 2402:
[`paper`](https://www.math.purdue.edu/~eremenko/dvi/rubel.pdf).
Their stated consequence is that a linearly dependent collection
`p_nu exp(g_nu)` contains two exponentials with constant ratio.  Applying
that result recursively to minimal vanishing subsums gives the block form
above.

## 5. No global entire quadratic identity

### Theorem 5.1 -- global `q=2` entire gate

Let `J>=1`, let `w_j>0` with `sum_j w_j=1`, and let `h_j,k` be entire.
If

```text
h_j(1)=0                                                   (5.1)
```

for every `j`, then the identity

```text
2 sum_j w_j exp(h_j)
-z sum_j w_j exp(2h_j)
=exp(k)                                                   (5.2)
```

is impossible.

#### Proof

Move the right side to the left.  This is a Borel sum whose terms are

```text
2w_j exp(h_j),
-w_j z exp(2h_j),
-exp(k).                                                  (5.3)
```

Consider the Borel block containing any quadratic term
`-w_j z exp(2h_j)`.  After an exponential is factored out, the coefficient
of `z` in the resulting polynomial identity is

```text
-sum_(ell in I) w_ell exp(2h_ell-2h_j),                  (5.4)
```

where `I` is the nonempty set of quadratic terms in that block.  Every
exponent difference in (5.4) is constant.  Evaluating it at `z=1` and using
(5.1) shows that each exponential in (5.4) equals one.  The coefficient is
therefore

```text
-sum_(ell in I)w_ell<0,                                  (5.5)
```

contradicting the polynomial identity.  Every term must belong to a Borel
block, so (5.2) cannot hold.  QED.

Positivity is used only in the last line.  With complex weights, exact
isotropic cancellations can occur.

## 6. No global entire mixed-product identity

### Theorem 6.1 -- global mixed-product gate

For no finite `J>=1` and entire `h_1,...,h_J,k` is

```text
1-product_(j=1)^J[z exp(h_j)-1]=z exp(k)                 (6.1)
```

an identity on `C`.

#### Proof

At `z=0`, the left side is `1-(-1)^J`.  Thus odd `J` is impossible.

Let `J` be even.  For `S subset {1,...,J}`, put

```text
H_S=sum_(j in S)h_j.                                     (6.2)
```

Expanding the product, canceling the constant empty-subset term, and
dividing by `z` gives

```text
exp(k)
+sum_(nonempty S)(-1)^(J-|S|) z^(|S|-1)exp(H_S)=0.       (6.3)
```

Apply Lemma 4.1.  The term corresponding to the full set `S={1,...,J}`
has polynomial degree `J-1`.  It is the unique term of that degree.  In its
Borel block, factoring an exponential therefore leaves a polynomial whose
top coefficient is nonzero and has no other term which can cancel it.  This
contradicts (4.3).  QED.

## 7. Consequence for the strip program

The strongest chart-free templates are now excluded:

```text
global entire individual-square cofactor                 FALSE;
global entire mixed-product cofactor                      FALSE. (7.1)
```

On a fixed bounded localization domain, the remaining escape is much
narrower.  It must use a nonnormal multichannel section whose unit ratios
generate an unbounded value cloud.  A merely qualitative Oka construction,
normal corona solution, or fixed entire-curve template cannot supply the
needed quantitative control.  To remain useful for the high-jet argument,
such a section would also
need an arithmetic prime realization and an outer-growth exponent small
enough to fit below the amplified support gain.

R165 proves neither existence nor nonexistence of that last wild local
section.  It proves neither a fixed zero-free strip nor zeros approaching
`Re(s)=1`.
