# R89 Mobius near-isometric fractional-flow gate

Status: exact flow-to-zero-free-strip transfer proved, followed by a
positive-density smooth-number obstruction.  Fractional overlap does evade
the allocation defects of a matching, but it does not evade absence of an
incident short edge.  For every fixed power displacement, the short
`p <-> qr` graph has linearly many isolated collar vertices.  This kills the
proposed direct bounded-congestion flow mechanism.  It does **not** prove that
zeta has no fixed zero-free strip.

Date: 2026-08-07.

## 1. Why try a fractional flow?

Let

```text
V = {n : n is odd and squarefree},
sigma(n) = mu(n) = (-1)^omega(n).
```

The exact dyadic-collar identity is

```text
M(N) = sum_(n in I_N) sigma(n),
I_N = V intersect (N/2,N].                            (1)
```

An allowed exchange edge has the form

```text
u = C p,             v = C q r,                       (2)
```

where `p,q,r` are distinct odd primes and the squarefree core `C` is
coprime to `pqr`.  It reverses the Mobius sign.

A matching asks each vertex to use one edge.  A fractional flow is much more
flexible: a vertex can split its unit supply among arbitrarily many
semiprime encodings, and different routings may overlap.  Thus the old
one-shot collision and greedy allocation objections do not apply to it.

Write an antisymmetric flow as

```text
F_N(u,v) = -F_N(v,u),
div F_N(u) = sum_v F_N(u,v),
load F_N(u) = sum_v |F_N(u,v)|.                       (3)
```

The desired identity is `div F_N(u)=sigma(u)`.  With the convention in (3),
even-rank vertices are unit sources and odd-rank vertices are unit sinks.
The flow may be signed; positivity is not needed for the transfer theorem
below.

## 2. Exact transfer theorem

**Theorem 2.1 (power-local divergence gives a fixed strip).**  Suppose there
are constants

```text
A,D,B >= 1,             alpha,beta > 0                (4)
```

such that for every sufficiently large `N` there are an antisymmetric flow
`F_N` on `V` and an exceptional set `E_N subset I_N` satisfying:

1. `F_N` is supported on the exchanges (2);
2. `load F_N(u) <= A` for every `u in I_N`;
3. every support edge incident to `I_N` obeys

   ```text
   |u-v| <= D N^(1-alpha);                            (5)
   ```

4. `div F_N(u)=sigma(u)` for `u in I_N\E_N`;
5. `#E_N <= B N^(1-beta)`.

Then, with `eta=min(alpha,beta)`,

```text
M(N) = O(N^(1-eta)).                                 (6)
```

Consequently `zeta(s)` has no zero in

```text
Re(s) > 1-eta.                                       (7)
```

The flows are allowed to depend completely on `N`.  No consistency between
different collars and no integral matching are assumed.

### Proof

On an exceptional vertex, the load bound gives

```text
|sigma(u)-div F_N(u)| <= 1+A.
```

Therefore (1) gives

```text
M(N)
 = sum_(u in I_N) div F_N(u) + O((1+A)#E_N).         (8)
```

Antisymmetry cancels every edge internal to `I_N`, so

```text
sum_(u in I_N) div F_N(u)
 = sum_(u in I_N, v notin I_N) F_N(u,v).             (9)
```

Put `R_N=D N^(1-alpha)`.  Once `R_N<N/4`, an edge in (9) can leave the
collar only if its endpoint in `I_N` lies in one of the two integer intervals

```text
(N/2,N/2+R_N]       or       (N-R_N,N].              (10)
```

There are at most `2R_N+2` such integers.  Charging every crossing edge to
its endpoint in (10) and using the absolute load bound yields

```text
|sum_(u in I_N) div F_N(u)|
 <= A(2R_N+2)
 = O(N^(1-alpha)).                                   (11)
```

Equations (8) and (11) prove (6).

For `Re(s)>1`, partial summation gives

```text
1/zeta(s) = s integral_1^infinity M(x) x^(-s-1) dx.  (12)
```

The bound (6) makes the right side holomorphic in
`Re(s)>1-eta`.  Analytic continuation from `Re(s)>1` then makes it the
reciprocal of zeta throughout that half-plane (with the usual removable
behavior at the pole `s=1`).  A zeta zero there would give a pole of the
reciprocal, contradicting holomorphy.  This proves (7).  QED.

### What “controlled congestion” must mean

The absolute load in hypothesis 2 is essential to this direct argument.
Controlling only the signed sum at a boundary vertex permits arbitrarily
large cancelling traffic across the cut.  One could replace hypotheses 2--3
by a direct power bound on total absolute flow crossing both collar
boundaries, but proving that bound is already the needed cancellation input.

## 3. The short-edge graph has a linear isolated set

The transfer theorem identifies a clean target.  Unfortunately the target
is incompatible with the arithmetic geometry of bounded-size factor
exchanges.

**Theorem 3.1 (smooth isolation).**  Fix `D>=1` and `0<alpha<1`.  Form the
scale-`N` graph using the exchanges (2), retaining only edges incident to
`I_N` for which

```text
|u-v| <= D N^(1-alpha).                              (13)
```

There is a constant `c_alpha>0` such that this graph has at least

```text
c_alpha N+o(N)                                      (14)
```

isolated vertices in `I_N`.  More precisely, one may take

```text
c_alpha = 2 rho(2/alpha)/pi^2,                       (15)
```

where `rho` is the Dickman function.  The constant factor `D` does not alter
the main density.

### 3.1 The elementary isolation argument

Set

```text
y_N = (N^alpha/(8D))^(1/2).                          (16)
```

Consider any `n in I_N` all of whose prime factors are at most `y_N`.
Suppose an exchange edge joins it to `m`.

If `n=Cp`, put `a=p`.  If `n=Cqr`, put `a=qr`.  In either case `C=n/a`, and
because every prime factor of `n` is at most `y_N`,

```text
a <= y_N^2.                                         (17)
```

For the singleton case this uses only `p<=y_N<=y_N^2`, valid for large
`N`.  Equations (13), (17), and `n>N/2` now imply

```text
1 <= |p-qr|
   = |n-m|/C
   = |n-m| a/n
   <= 2D a N^(-alpha)
   <= 1/4.                                          (18)
```

This is impossible.  In fact both `p` and `qr` are odd and distinct, so
their difference is at least `2`; the weaker first inequality in (18)
already suffices.  Thus every odd squarefree `y_N`-smooth collar integer is
isolated.

The obstruction has a simple interpretation.  Even the smallest nonzero
factor-level error is magnified by the common core:

```text
|Cp-Cqr| = C |p-qr| >= C = n/a.                     (19)
```

A displacement at most `N^(1-alpha)` therefore requires the changed factor
block `a` to have size at least a constant multiple of `N^alpha`.  A smooth
integer for which every two-prime block is smaller has no first step.  Extra
semiprime choices cannot repair the absence of that step.

### 3.2 Why there are linearly many such vertices

For completeness, the squarefree and odd restrictions do not turn the
smooth family into a thin set.  Let

```text
Psi(x,y) = #{n<=x : P^+(n)<=y},
Q(x,y)   = #{n<=x : n odd, squarefree, P^+(n)<=y}.   (20)
```

The classical Dickman theorem says that, for fixed `u>0`,

```text
Psi(x,x^(1/u)) ~ rho(u)x.                            (21)
```

Here a harmless fixed multiplier in `y` has no effect.  Mobius
inclusion-exclusion for squarefreeness and the bijection between even smooth
integers and twice a smooth integer give the exact identity

```text
Q(x,y)
 = sum_(d odd, P^+(d)<=y) mu(d)
     [Psi(x/d^2,y)-Psi(x/(2d^2),y)].                 (22)
```

Take `y=y_N` and `x=lambda N` for fixed `lambda>0`.  For each fixed `d`,
the ratio of logarithms in both smooth counts tends to `2/alpha`.
Equation (21) makes the bracket in (22) asymptotic to

```text
(rho(2/alpha)/2) x/d^2.                              (23)
```

The contribution of `d>L` is bounded absolutely by

```text
x sum_(d>L) d^(-2) = O(x/L),                         (24)
```

so truncation followed by `L -> infinity` is legitimate.  Since

```text
sum_(d odd) mu(d)/d^2
 = product_(p odd) (1-p^(-2))
 = 8/pi^2,                                          (25)
```

we obtain

```text
Q(lambda N,y_N)
 ~ (4/pi^2) rho(2/alpha) lambda N.                  (26)
```

Subtracting the cases `lambda=1` and `lambda=1/2` proves that the number in
the collar is

```text
Q(N,y_N)-Q(N/2,y_N)
 ~ (2/pi^2) rho(2/alpha) N.                         (27)
```

The Dickman function is positive at every finite argument, so (27) is a
genuine positive linear density, however small its constant may be.  This
proves Theorem 3.1.  QED.

## 4. Consequence for fractional Hall and Markov constructions

**Corollary 4.1.**  The hypotheses of Theorem 2.1 cannot hold for any fixed
`alpha,beta>0` when the flow is supported on `p <-> qr` edges.

Indeed, divergence at an isolated vertex is zero for every flow, including a
signed fractional flow with unlimited overlap.  Every vertex counted by
(27) must therefore lie in `E_N`.  Hence

```text
#E_N >= c_alpha N+o(N),                              (28)
```

contradicting `#E_N=O(N^(1-beta))`.

For a nonnegative source-to-sink transport, the same fact is the strongest
possible Hall obstruction.  If `S_N` is the smooth set in (27), then its
neighbor set in the short-edge graph is empty:

```text
Gamma(S_N)=emptyset.                                 (29)
```

Thus neither a fractional perfect matching, a max-flow construction, a
Markov redistribution kernel, nor unbounded reuse of semiprime targets can
start.  This is distinct from the static-dictionary no-go: the dictionary
may be fully `N`-adaptive and every eligible edge may be reused with arbitrary
fractional weights.

There is also a weighted version which does not require declaring vertices
exceptional.  If an exact-divergence flow is allowed to use long edges, put

```text
L_N = sum_(u in I_N) sum_(|u-v|>D N^(1-alpha))
        |F_N(u,v)|.                                  (30)
```

At every smooth vertex counted by (27), all incident edges are long, while
`|div F_N(u)|=1` forces incident absolute mass at least one.  Hence

```text
L_N >= (2/pi^2) rho(2/alpha)N+o(N).                  (31)
```

So the long-edge defect cannot have subpower *total weight* either.  Any
successful use of those edges must prove cancellation among linearly much
long traffic at the collar cut.

### 4.1 Fractional one-factors and symmetric Markov kernels

There is no hidden distinction among the natural positive formulations.
Write

```text
V_+ = {n in V : sigma(n)=+1},
V_- = {n in V : sigma(n)=-1}.                        (32)
```

On any finite bipartite exchange graph, the following data are equivalent.

1. A nonnegative flow directed from `V_+` to `V_-` with divergence
   `sigma` at every vertex.
2. Edge weights `w(e,o)>=0` satisfying

   ```text
   sum_o w(e,o)=1       for every e in V_+,
   sum_e w(e,o)=1       for every o in V_-.           (33)
   ```

3. A fractional perfect matching, or fractional `1`-factor.
4. A symmetric stochastic kernel supported on exchange edges, obtained by

   ```text
   P(e,o)=P(o,e)=w(e,o).                              (34)
   ```

Indeed, (33) is simultaneously the divergence condition, the fractional
degree-one condition, and the row-sum-one condition for (34).  Conversely,
restricting a symmetric stochastic kernel to the `V_+`-to-`V_-` orientation
recovers (33).  The same equivalence holds on a countable graph whenever the
displayed sums converge; finite truncations are enough for the collar
argument.

Moreover, on a finite bipartite graph the fractional `1`-factor polytope is
integral.  Thus fractional feasibility is equivalent to Hall's condition and
to existence of an ordinary perfect matching.  Fractionalization can repair
a poor greedy allocation, but it cannot weaken the underlying cut
conditions.

Thus replacing a matching by a Markov chain adds convex flexibility but no
new way through an isolated vertex.  The smooth set violates even the
singleton Hall inequalities.

### 4.2 The prefix-cut identity and why unrestricted edges are circular

Suppose, just for this paragraph, that a global fractional one-factor `w`
does exist, with no displacement restriction.  For any finite set `A subset
V`, cancellation of internal transported mass gives the exact cut identity

```text
sum_(n in A) sigma(n)
 = w(V_+ intersect A, V_-\A)
   - w(V_+\A, V_- intersect A).                      (35)
```

Taking `A=I_N` makes the left side exactly `M(N)`.  Consequently

```text
|M(N)| <= total w-mass crossing the boundary of I_N. (36)
```

With power-short edges, geometry restricts that mass to the thin boundary
collars (10), which is precisely why Theorem 2.1 works.  With unrestricted
edges, every one of the `asymp N` collar vertices may send mass across the
cut, and bounded load gives only the trivial `O(N)` estimate.

It is not enough here that `p` and `qr` are close *relative to their own
size*.  The endpoint gap is `C|p-qr|`; a large common core can magnify even a
unit factor-level gap into an order-`N` jump.  Relative near-value edges are
therefore unrestricted for the additive collar cut unless a lower bound on
the changed factor block is also enforced.

Max-flow/min-cut or Hall expansion can certify that the required mass can be
routed, but (35) says that the *net* amount which must be routed across the
prefix cut is already its unknown Mobius discrepancy.  Therefore a claim
that unrestricted Hall routing itself makes the crossing mass small is
circular.  One needs either geometric locality or a separate signed estimate
for the long-edge traffic; the latter is the new cancellation theorem, not a
consequence of fractional feasibility.

## 5. Bounded-arity extension

The obstruction is not special to one-prime-for-two-prime moves.  Suppose an
edge replaces one product of at most `k` distinct primes by another product
of at most `k` distinct primes, with a common squarefree core, and the two
products differ.  For fixed `k`, set

```text
y_N = (N^alpha/(8D))^(1/k).                          (37)
```

Every changed factor block of a `y_N`-smooth vertex is at most
`N^alpha/(8D)`.  Repeating (18) shows that the vertex is isolated from every
edge of displacement at most `D N^(1-alpha)`.  The argument around
(20)--(27), now with Dickman parameter `k/alpha`, gives the more precise
collar count

```text
(2/pi^2) rho(k/alpha) N+o(N).                        (38)
```

In particular, the exceptional density is positive for every fixed `k`.

Therefore every fixed bounded-arity prime-set exchange graph fails the same
power-local divergence target.  To avoid this specific obstruction, the
arity must grow with the smoothness depth, or the mechanism must allow
power-long edges.

## 6. Reality check and surviving directions

The attempted implication was sound:

```text
bounded local divergence
    -> power-small collar-boundary flux
    -> M(N)=O(N^(1-eta))
    -> a fixed zero-free half-plane.                 (39)
```

The failure is earlier and arithmetic, not an allocation artifact:

```text
positive-density smooth vertices
    -> no power-short bounded-arity exchange edge
    -> linear divergence exceptions.                (40)
```

Fractionalization therefore does not rescue the direct near-isometric
exchange route.  The viable ways around Theorem 3.1 are materially different
problems:

1. allow displacement `N^(1-o(1))`; this loses the fixed power in the
   boundary estimate and cannot by itself give a fixed strip;
2. allow bounded-arity long edges but prove a power bound for their *total
   boundary flux* by signed cancellation rather than geometric locality;
3. allow factor moves of arity growing with the smoothness depth, then find a
   uniform congestion theorem for that much larger hypergraph;
4. abandon pointwise divergence and prove a directly averaged identity whose
   defect on the smooth sector already has cancellation.

Items 2--4 are not consequences of Hall expansion.  Each asks for a new
signed estimate on precisely the sector that the local geometry cannot
move.

## 7. Verdict

The R89 branch yields a useful exact theorem and a decisive kill gate:

- a bounded-load, fixed-power-local fractional divergence would indeed prove
  a fixed zero-free strip;
- such a flow cannot exist on the `C p <-> C q r` graph outside a sublinear
  exceptional set;
- the obstruction is a positive-density family, not a finite-template or
  integral-matching defect.

This is a no-go for the proposed mechanism, **not** evidence that a fixed
zero-free strip itself is false.  Proving that no fixed strip exists would
mean proving zeros with real parts tending to `1`, a statement far beyond
anything established here.
