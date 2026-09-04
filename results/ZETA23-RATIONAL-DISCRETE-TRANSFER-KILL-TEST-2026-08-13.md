# Frozen rational discrete-transfer kill test

**Date:** 2026-08-13

## Verdict

The frozen symmetrized physical-gap mode

```text
T_X(z)=1/2 sum_j g_j(z^(p_j)+z^(p_(j+1))),
g_j=p_(j+1)-p_j,       z=e(a/q),       (a,q)=1,       (0.1)
```

does not admit a uniformly conditioned discrete-calculus transfer to the
ordinary additive prime mode.  Three exact representations were tested:

1. an edgewise geometric/cotangent transfer;
2. a central-difference Wronskian and frequency-derivative transfer;
3. a predecessor/successor, or renewal, expansion in consecutive-prime
   indicators.

The first has an actual pole: if `q|g`, the ordinary integer geometric block
is zero while the trapezoidal gap block is `g z^p`.  The second retains a
nearest-neighbor Wronskian which is not an ordinary prime sum.  The third is
exactly a growing family of consecutive-prime correlations, with multiplier
`h(1+z^h)/2`; replacing this multiplier by one is precisely the unjustified
step.

A paired gap-relocation construction makes the obstruction quantitative.
Moving a `2q` extension from one edge to another leaves every frozen node
phase, and hence the ordinary unweighted additive sum, **exactly unchanged**.
It changes (0.1) by `asymp q`.  For a deterministic smooth von-Mangoldt-like
weight it changes the normalized ordinary sum by only `O(q^2/Y^2)`, versus
`asymp q/Y` for the normalized gap mode.  Thus this direction has condition
number at least

```text
Y/q=Y^(1-b+o(1)),       q=Y^b.                       (0.2)
```

At the bottom surviving denominator `b=beta=.1537`, global Vaughan
cancellation can afford a transfer loss of only

```text
beta/2-kappa=.0588196766,
```

whereas (0.2) costs `.8463`.  Even the optimistic global ordinary-prime
estimate therefore cannot close after this transfer.  Short-block
localization is worse.

This is a definitive no-go theorem for a **black-box, frozen-frequency,
bounded-symbol reduction to the ordinary additive prime mode and its
bounded-smooth-weight variants**.  It is not an
actual-prime counterexample and not a no-go theorem for the selected
consecutive-gap estimate.  Actual primes could still forbid or cancel the
rational gap-relocation direction; proving that is exactly the live
gap-residue coherence theorem.

No zero-free strip is claimed here.

---

## 1. Exact edge transfer and its genuine pole

Let `p` and `p+g` be two adjacent integer nodes.  Put

```text
T_(p,g)(z)=g z^p(1+z^g)/2,                           (1.1)
G_(p,g)(z)=sum_(n=p)^(p+g-1) z^n
            =z^p(1-z^g)/(1-z).                      (1.2)
```

If `z^g!=1`, direct division gives the exact nonuniform-trapezoid symbol

```text
T_(p,g)(z)=m_g(z)G_(p,g)(z),
m_g(z)=g(1-z)(1+z^g)/[2(1-z^g)].                    (1.3)
```

For `z=e(a/q)`, this is the cotangent symbol

```text
m_g(z)=i g(1-z) cot(pi*a*g/q)/2,
|m_g(z)|=g |sin(pi*a/q)| |cot(pi*a*g/q)|.            (1.4)
```

The apparent singularity is real, not a removable artifact.  When `q|g`,

```text
G_(p,g)(z)=0,                 T_(p,g)(z)=g z^p !=0. (1.5)
```

There is also an exact null in the opposite direction.  If `z^g=-1`, then

```text
T_(p,g)(z)=m_g(z)=0,               G_(p,g)(z)!=0.   (1.5a)
```

This null is harmless for an upper transfer from `G` to `T`, but it shows
that the scalar symbol is not invertible in either direction.  The pole
(1.5), rather than this null, is the obstruction used below.

For odd prime `q`, the physical gap `g=2q` is even and so respects the parity
of odd prime-shaped nodes.  At a denominator `q=Y^(b+o(1))` with any fixed
`b<theta=.1594`, this gap is below the retained cutoff `Y^theta` for large
`Y`.  Current gap-tail information does not permit deleting all such gaps at
the required exponent near `b=.1537`.

Even excluding exact resonance does not condition (1.3).  For
`g=2q+d`, where `d=asymp log Y` and `a=1`, one has

```text
|m_g(e(1/q))| asyp q/d.                              (1.6)
```

Thus a lower bound on the distance of every retained successor gap from the
resonant residue classes would itself be new gap-residue information.  The
cotangent representation relocates the target; it does not solve it.

### 1.1 Continuous quadrature has the same obstruction

With `omega=2*pi*a/q`, the exact integral over the edge is

```text
I_(p,g)=z^p(z^g-1)/(i*omega).
```

For `z^g!=1`, the trapezoid-to-integral symbol is

```text
T_(p,g)/I_(p,g)=(omega*g/2) cot(omega*g/2).          (1.7)
```

It again has poles at the rational gap returns.  Peano/trapezoidal error is
small only when `|omega|g` is small on the chosen branch.  A high denominator
does not imply this: the reduced numerator `a` is selected and can be of size
`q`.  Hence ordinary nonuniform-quadrature estimates do not add a missing
power here.

---

## 2. Central differences, Wronskians, and frequency derivatives

Write `X_j=z^(p_j)`.  Including the two half-weighted block endpoints,
(0.1) is exactly

```text
T_X(z)=sum_j w_j X_j,
w_0=g_0/2,
w_j=(g_(j-1)+g_j)/2,
w_N=g_(N-1)/2.                                      (2.1)
```

Expanding `g_j=p_(j+1)-p_j` gives the discrete Wronskian identity

```text
T_X(z)=1/2 [p_N X_N-p_0 X_0
 +sum_(j=0)^(N-1)(p_(j+1)X_j-p_j X_(j+1))].         (2.2)
```

Thus central summation by parts does not produce `sum p_j X_j`.  It produces
the skew predecessor/successor pairing in (2.2).

There is also an exact frequency-derivative form.  With
`D=z d/dz`, `D_j(z)=z^(p_(j+1))-z^(p_j)`, and
`c_j=(p_j+p_(j+1))/2`,

```text
g_j[X_j+X_(j+1)]/2=(D-c_j)D_j(z).                   (2.3)
```

Summing the derivative terms telescopes only to
`D(z^(p_N)-z^(p_0))`; the remaining sum is
`sum c_j D_j(z)`, which is again the Wronskian in (2.2).  At `q|g_j`, the
value `D_j(z)` is zero but its derivative is `g_j z^(p_j)`.  Consequently a
formula using only the frozen values of an ordinary additive sum necessarily
loses this direction.  Adding frequency derivatives can see the direction,
but it introduces midpoint/neighbor moments not covered by the ordinary
Vaughan estimate and is not a bounded scalar transfer.

### 2.1 Abel comparison with `Lambda` is strip-strength

For actual prime nodes, put `ell_j=log p_j`, `d_j=w_j-ell_j`, and
`D_k=sum_(j=0)^k d_j`.  Ordinary Abel summation gives exactly

```text
sum_j d_j X_j
 =D_N X_N+sum_(j=0)^(N-1)D_j(X_j-X_(j+1)).          (2.4)
```

For `k<N`, the prefix is

```text
D_k=p_k-p_0+g_k/2-sum_(j=0)^k log p_j.              (2.5)
```

Up to the explicit endpoint terms, (2.5) is `x-vartheta(x)`.  The factor
`X_j-X_(j+1)=z^(p_j)(1-z^(g_j))` is not power-small uniformly.  A
fixed-power bound on all prefixes in (2.4) is already a fixed-power prime
number theorem, hence zero-free-strip strength.  Formula (2.4) is exact but
circular as a black-box route.  It does not exclude a frequency-specific
actual-prime argument.

---

## 3. Exact predecessor/successor and renewal expansions

Let `P(n)` be the prime indicator on a finite block and define

```text
R_h(n)=P(n)P(n+h) product_(1<=r<h)[1-P(n+r)].        (3.1)
```

Away from the two block boundaries, `R_h(n)` is exactly the indicator that
`n,n+h` are consecutive primes.  Hence

```text
T_X(z)=1/2 sum_(h>=1) h(1+z^h)
                     sum_n R_h(n)z^n.               (3.2)
```

By contrast,

```text
sum_n P(n)z^n=sum_(h>=1)sum_n R_h(n)z^n             (3.3)
```

up to the last node.  The exact transfer from (3.3) to (3.2) replaces the
constant coefficient `1` by

```text
K_h(z)=h(1+z^h)/2.                                  (3.4)
```

This multiplier vanishes when `z^h=-1`, has size `h` when `z^h=1`, and is
not a deterministic smooth function of `n`.  Vaughan's identity decomposes
`Lambda(n)`; it does not decompose the nonlinear no-intermediate-prime
product in (3.1).

Equivalently, using `h=sum_(r=1)^h 1`, the forward half is the exact renewal
survival expansion

```text
sum_j g_j z^(p_j)
 =sum_(r>=1)sum_n P(n)z^n
       product_(1<=s<r)[1-P(n+s)].                  (3.5)
```

The reverse half has the analogous predecessor product.  Expanding these
products is growing-order inclusion--exclusion.  No finite Vaughan or
Heath--Brown decomposition turns (3.5) into an ordinary prime sum.

---

## 4. Exact `2q` relocation null direction

The preceding poles can be expressed without division.  Fix odd prime `q`,
an even `d<q`, and `H=2q`.  Start with a mesh

```text
y_j=y_0+j d.
```

Choose two mesh edges `k<l`.  Form configuration `A` by adding `H` to edge
`k`, i.e. shifting all later nodes by `H`.  Form configuration `B` by adding
the same `H` to edge `l`.  Past edge `l` the configurations coincide, and
for every corresponding node

```text
p_j^A=p_j^B       or       p_j^A=p_j^B+H.
```

Since `z^H=1`, exactly

```text
z^(p_j^A)=z^(p_j^B) for every j,
sum_j z^(p_j^A)=sum_j z^(p_j^B).                    (4.1)
```

Nevertheless, direct subtraction of the two edge sums gives

```text
T_A(z)-T_B(z)
 =H(1+z^d)(z^(y_k)-z^(y_l))/2.                      (4.2)
```

Take `a=1`, `k=0`, and `l=floor(q/(2d))`.  Then

```text
|1+z^d|=2+o(1),       |1-z^(ld)|=2+o(1),
|T_A-T_B|=(2+o(1))H asyp q.                         (4.3)
```

Thus the frozen ordinary additive value has an exact null direction on
which the gap functional is order `q`.

### 4.1 The logarithmic weight does not repair the condition number

Place the gadget in `[Y,2Y]`.  Between edges `k` and `l`, the two positions
differ by `H`; elsewhere they agree.  For any deterministic coefficient
`F` with

```text
sup_[Y,2Y] |F'(x)| <<log(Y)/Y,                       (4.4)
```

the normalized ordinary additive sums obey

```text
1/Y |sum_j F(p_j^A)z^(p_j^A)
       -sum_j F(p_j^B)z^(p_j^B)|
 <<(l-k)H log(Y)/Y^2
 <<q^2/Y^2,                                         (4.5)
```

because `l-k<<q/d` and `d=asymp log Y`.  This includes a dyadically smooth
version of `F(x)=log x`.  Prime powers in the ordinary von Mangoldt sum are
separately `O(Y^(-1/2+o(1)))` after normalization.

On the other hand, (4.3) gives

```text
|T_A-T_B|/Y asyp q/Y.                               (4.6)
```

The ratio of (4.6) to (4.5) is at least

```text
Y/q=Y^(1-b+o(1)).                                   (4.7)
```

So allowing a smooth deterministic `Lambda` weight changes an exact null
direction into an extremely ill-conditioned direction; it does not produce
a usable transfer.

The same estimate applies to the actual frozen logarithmic Voronoi edge
coefficient, not only to the physical normalization.  On a fixed interior
subshell put

```text
h(x)=phi(log(x/Y))/x,          h(x) asyp 1/Y,
|h'(x)|<<1/Y^2.                                      (4.7a)
```

Replacing a physical edge `g/Y` by
`log(1+g/x)` and inserting the two smooth endpoint amplitudes costs
`O(g^2/Y^2)` on that edge.  Across the `O(q/d)` shifted small edges of one
gadget, smooth relocation costs

```text
O((q/d)*d*q/Y^2)=O(q^2/Y^2),                         (4.7b)
```

and the two special edges have the same error.  Therefore the exact frozen
logarithmic symmetrized gap functional changes by

```text
asymp q/Y+O(q^2/Y^2)=asymp q/Y.                      (4.7c)
```

This robustness still does not impose the global `t log x` curvature; the
construction remains a frozen-rational transfer countermodel.

### 4.2 Scaling the pair to the target while retaining every known gap budget

Choose the already audited interior exponent

```text
b=39/250=.156,       q=Y^(b+o(1)),
M=Y^(1-b-kappa+o(1)).                               (4.8)
```

Use disjoint gadgets with the same starting residue modulo `q`, so the
differences in (4.2) have one complex direction.  A gadget can be closed
after physical length `4q`: use even `d`-mesh gaps totaling `2q`, add the
`2q` extension on one of the two selected edges, and merge the final even
remainder into its preceding small gap.  All nodes can therefore be odd,
all ordinary phases agree pairwise, and the two configurations have the same
endpoints and node count.  The total special length is

```text
Mq=Y^(1-kappa+o(1))=o(Y),                           (4.9)
```

so the remainder of the shell can be filled with even gaps `asymp log Y`.
Both paired configurations then have prime-shaped density and the same exact
unweighted selected-`q` residue histogram.

The accumulated normalized differences satisfy

```text
gap mode:           asyp Mq/Y=Y^(-kappa+o(1)),
smooth Lambda mode: << Mq^2/Y^2=Y^(-1+b-kappa+o(1)). (4.10)
```

The special gap square and mass are

```text
Mq^2=Y^(1+b-kappa+o(1))=Y^(1.1379696766...+o(1)),
Mq  =Y^(1-kappa+o(1)).                               (4.11)
```

Thus Stadlmann's `Y^(1.23+epsilon)` gap-square budget holds.  Also
`b<theta=.1594`, so no gap is deleted.  On the Gafni--Tao envelope used in
the optimized audit,

```text
c_GT(b)=(9/13)(b-2/15)=51/3250=.01569230769...
       <kappa,                                       (4.12)
```

so the mass in (4.11) is allowed.  This strengthens the earlier marginal
countermodel: even a smooth ordinary `Lambda`-like frozen mode can be
power-smaller while the gap mode sits at the critical exponent.

The cached truncated third-gap ledger is also respected:

```text
sum special g^3
 <<M q^3
 =Y^(1+2b-kappa+o(1))
 =Y^(1.2939696766...+o(1))
 <Y^(84549/65000+o(1)).                              (4.13)
```

Here (4.11)--(4.13) mean that this nonprime construction satisfies the
**numerical inequalities** imported from the prime-gap theorems.  Stadlmann
and Gafni--Tao make no assertion about the constructed odd integers.

The construction consists of odd integer, prime-density-shaped nodes, not
actual primes.  It does not impose global logarithmic curvature or
simultaneous distribution at every modulus.  Its conclusion is exactly the
claimed nonimplication and no more.

---

## 5. Vaughan exponent ledger and the killed route

For an ordinary von Mangoldt sum of global length `Y`, Vaughan's estimate at
`alpha=a/q+O(q^-2)` is

```text
sum_(n<=Y) Lambda(n)e(alpha*n)
 <<[Y/sqrt(q)+Y^(4/5)+sqrt(Yq)] log^4 Y.             (5.1)
```

If `q=Y^b`, its relative saving is

```text
d_V(b)=min(b/2,1/5,(1-b)/2).                         (5.2)
```

Throughout the surviving denominator shell, the worst saving is

```text
d_V(beta)=beta/2=.07685.                             (5.3)
```

To retain the required `kappa=.0180303234`, a transfer from (5.1) may lose
at most

```text
rho_max=beta/2-kappa=.0588196766.                    (5.4)
```

But the exact relocation direction requires a condition loss at least

```text
1-b>=1-theta=.8406                                  (5.5)
```

on this shell, and the geometric transfer is literally infinite at (1.5).
This is a gap of more than `.78` in exponent.  Therefore none of the tested
bounded-symbol, scalar-multiplier, Abel-prefix, cotangent-resolvent, or
bounded-smooth ordinary-`Lambda` transfers can combine with black-box
Vaughan to prove the target.  This statement does not cover an arbitrarily
chosen bank of frequency derivatives or weights engineered from the gaps;
those already contain neighbor information beyond the ordinary Vaughan
input.

The conclusion is deliberately scoped.  A theorem ruling out the relocation
direction for actual consecutive primes, a direct estimate for (3.2), or a
selected-frequency cancellation across the gap classes would survive this
audit.  Each is a form of the same live high-denominator consecutive-gap
coherence problem, not an ordinary additive-prime estimate.

---

## Primary sources used for the quantitative inputs

- R. C. Vaughan, *The Hardy--Littlewood Method*, 2nd ed., especially the
  classical prime exponential-sum estimate; [Cambridge University Press
  DOI](https://doi.org/10.1017/CBO9780511470929).
- R. C. Vaughan, *Sommes trigonometriques sur les nombres premiers*, C. R.
  Acad. Sci. Paris Ser. A-B **285** (1977), A981--A983.
- A. Stadlmann, [*On the mean square gap between primes*](https://arxiv.org/abs/2212.10867).
- A. Gafni and T. Tao, [*On the number of exceptional intervals to the prime
  number theorem in short intervals*](https://arxiv.org/abs/2505.24017), for
  the tail envelope imported from the preceding project audit.

The transfer pole, Wronskian, renewal expansion, and paired relocation
theorem above are finite algebraic identities; they do not depend on a
quadrature or renewal heuristic from the literature.
