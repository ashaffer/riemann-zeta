# R95 Luroth resonant-head and aliasing gate

Status: the R94 cutoff is reduced rigorously from `O(t^2)` to its natural
linear scale.  The nonstationary tail at a linear cutoff has an explicit
nonzero limiting symbol up to the first alias at `2 pi`.  The aliases inside
that cutoff are computed branch by branch and in stationary windows.  They
reconstruct finite pieces of the complementary Dirichlet phase
`sum k^(s-1)`, admit arbitrary finite phase configurations, and cannot be
removed by a finite polynomial change of the positive Luroth observable
without losing the zeta divisor.  This is a sharp failure of local pairing
and finite-observable filters.  No fixed zero-free strip, and no theorem
excluding every fixed strip, is proved.

Date: 2026-08-07.

## 1. Verdict

The R94 digit contribution is

```text
J_n(s)=1/[s(s+1)]
 [s n^(-s)-n^(1-s)+n(n+1)^(-s)].                    (1.1)
```

It is the discrete Euler defect

```text
s n^(-s)+n[(n+1)^(-s)-n^(-s)].                       (1.2)
```

The two terms in (1.2) cancel in the far range, where one lattice step sees
only a small phase change.  They do not cancel when

```text
t log(1+1/n) approximately 2 pi k.                   (1.3)
```

Those are exact sampling aliases.

This audit proves six coefficient-specific facts.

1. The first `N` digits collapse exactly to

   ```text
   sum_(n<=N)J_n(s)
    =[(s-1)sum_(n<=N)n^(-s)+N(N+1)^(-s)]/[s(s+1)].   (1.4)
   ```

2. If `a=N+1`, `t/a -> v`, and `0<abs(v)<2 pi`, then

   ```text
   a^(s+1) sum_(n>N)J_n(s) -> G(iv),                 (1.5)

   G(z)=[z-(1-exp(-z))]/[z^2(1-exp(-z))].            (1.6)
   ```

   The function `G(iv)` is nonzero throughout this open alias-free range.
   Thus a cutoff just above `abs(t)/(2 pi)` already has a coherent nonzero
   tail.  The `t^2` cutoff in R94 came only from taking a periodic
   Euler--Maclaurin remainder absolutely.
3. At the alias `n approximately t/(2 pi k)`, the target branch does not
   cancel.  Its exact scaling limit is

   ```text
   n^(s+1)J_n(s) -> 1/(2 pi i k).                    (1.7)
   ```

4. A stationary window of width `sqrt(t)/k` around that branch has a
   nonzero coherent contribution of order

   ```text
   t^(-sigma-1/2) k^(sigma-1).                        (1.8)
   ```

   For finitely many windows, their leading signed sum is a common factor
   times

   ```text
   sum_k k^(s-1).                                    (1.9)
   ```

   Local Luroth positivity has therefore turned into the complementary
   Dirichlet phases, not into a common cone.
5. Kronecker approximation makes any finite collection of prime-indexed
   resonance phases arbitrarily flexible.  Once enough blocks are chosen,
   their normalized signed sum can be arbitrarily small at unbounded
   heights.  Hence no blockwise lower bound or finite phase-locking rule can
   prove the strip.
6. The alias in (1.7) is the Fourier coefficient of the endpoint mismatch
   of the observable `h(y)=y`.  A real observable suppresses every integer
   alias only if it is constant, which gives the rational spectator `1/s`.
   More strongly, among all finite polynomial observables with rational
   `s`-dependent coefficients, the only one retaining the zeta carrier up
   to a rational factor is a scalar multiple of `y` itself.

The remaining problem is now smaller and sharper than R94: control one
signed forward head of length just above `abs(t)/(2 pi)`, while coupling all
of its stationary aliases globally.  Adjacent pairing, finite resonance
blocks, and finite nonlinear observable filters are closed.

## 2. Exact summation of the discrete Euler defect

Put

```text
f_n=n^(-s).
```

Then (1.1) is

```text
J_n(s)=[s f_n+n(f_(n+1)-f_n)]/[s(s+1)].              (2.1)
```

The second term sums by parts without an error.

**Lemma 2.1 (finite-head identity).**  For every positive integer `N`,

```text
H_N(s):=sum_(n=1)^N J_n(s)

 =[(s-1)S_N(s)+N(N+1)^(-s)]/[s(s+1)],               (2.2)

S_N(s)=sum_(n=1)^N n^(-s).                           (2.3)
```

### Proof

Direct index shifting gives

```text
sum_(n=1)^N n(f_(n+1)-f_n)
 =-sum_(n=1)^N f_n+N f_(N+1).                        (2.4)
```

Substitution into (2.1) proves (2.2).  QED.

This identity shows both the gain and the danger of the coefficient.  When
`n` is much larger than `abs(s)`,

```text
n(f_(n+1)-f_n)=-s f_n+O(abs(s)^2 n^(-Re(s)-1)),      (2.5)
```

and the leading terms cancel.  When the one-step phase winds by an integer
multiple of `2 pi`, `f_(n+1)` is again almost `f_n`; then the difference term
is nearly zero and the unsuppressed term `s f_n` remains.  The convergence
correction and the alias response are two sides of the same stencil.

## 3. The exact linear-cutoff tail symbol

R94 proved the exact tail formula

```text
R_N(s):=sum_(n>N)J_n(s)

 =[(s-1)zeta(s,N+1)+(N+1)^(-s)-(N+1)^(1-s)]
   /[s(s+1)].                                         (3.1)
```

The coarse absolute Euler remainder required `N` much larger than `t^2`.
The periodic remainder is oscillatory, and before its first stationary point
one can retain that oscillation.

Define

```text
G(z)=1/[z(1-exp(-z))]-1/z^2

    =[z-(1-exp(-z))]/[z^2(1-exp(-z))].               (3.2)
```

**Theorem 3.1 (linear-cutoff response).**  Fix

```text
0<sigma_0<=sigma<=1,
0<v_0<=abs(v)<=v_1<2 pi.                              (3.3)
```

Let `s=sigma+it`, let `a=a(t)` be positive integers tending to infinity,
and suppose

```text
t/a -> v.                                             (3.4)
```

Then, uniformly on compact parameter ranges as in (3.3),

```text
a^(s+1)R_(a-1)(s) -> G(iv).                           (3.5)
```

Moreover

```text
G(iv)!=0                    for 0<abs(v)<2 pi.        (3.6)
```

### Proof

Euler--Maclaurin with `p` periodic Bernoulli corrections gives

```text
zeta(s,a)
 =a^(1-s)/(s-1)+(1/2)a^(-s)

  +sum_(r=1)^p [B_(2r)/(2r)!]
    (s)_(2r-1)a^(-s-2r+1)+E_p(s,a),                 (3.7)
```

where `(s)_m=s(s+1)...(s+m-1)`.  The remainder is a constant multiple of

```text
(s)_(2p) integral_a^infinity
 Bbar_(2p)(x)x^(-s-2p)dx.                            (3.8)
```

Expand the periodic Bernoulli function in its absolutely convergent Fourier
series.  The phase in its `m`-th positive Fourier mode is

```text
2 pi m x-t log x,                                    (3.9)
```

whose derivative on `x>=a` has magnitude at least

```text
2 pi-v_1>0.                                           (3.10)
```

The negative modes have an even larger derivative.  One integration by
parts in every Fourier mode therefore improves the usual absolute remainder
by one power of `a`.  For fixed `p`, after multiplying (3.8) by the factor
in (3.1) and by `a^(s+1)`, its limiting size is bounded by

```text
C_(v_1) [v_1/(2 pi)]^(2p-1).                          (3.11)
```

This tends to zero as `p` tends to infinity.

Substitute (3.7) into (3.1).  The terms `a^(1-s)` cancel exactly.  For each
fixed `p`, multiplication by `a^(s+1)` and passage to the limit gives

```text
1/(2z)+sum_(r=1)^p [B_(2r)/(2r)!]z^(2r-2),

z=iv.                                                 (3.12)
```

The Bernoulli generating function, valid for `abs(z)<2 pi`, gives

```text
1/(2z)+sum_(r>=1)[B_(2r)/(2r)!]z^(2r-2)

 =1/[z(1-exp(-z))]-1/z^2=G(z).                       (3.13)
```

Equations (3.11)--(3.13) prove (3.5).

For `z=iv`, the numerator in the second expression in (3.2) is

```text
cos(v)-1+i[v-sin(v)].                                (3.14)
```

For `0<abs(v)<2 pi` it cannot vanish, and the denominator is also nonzero.
This proves (3.6).  QED.

### 3.1 A finite expansion with a rigorous nonstationary remainder

The same proof, stopped after the first Bernoulli correction, gives whenever

```text
a>=kappa abs(t),                kappa>1/(2 pi),       (3.15)
```

the expansion

```text
R_(a-1)(s)
 =a^(-s)/(2s)
  +(s-1)a^(-s-1)/[12(s+1)]
  +O_(sigma_0,kappa)((1+abs(s))a^(-sigma-2)).        (3.16)
```

More Bernoulli terms give a full asymptotic series in `s/a`.  In particular,
on every closed subinterval of

```text
0<abs(t)/a<2 pi,                                     (3.17)
```

the tail is nonzero for all sufficiently large `abs(t)` and has size

```text
asymp a^(-sigma-1).                                  (3.18)
```

The radius `2 pi` is not a technical constant.  At `abs(t)/a=2 pi`, the
`m=1` phase in (3.9) acquires a stationary point at the endpoint.  The pole
of `G` at `2 pi i` records exactly that alias.

### 3.2 Consequence for a hypothetical zero

Fix any

```text
0<v<2 pi,
a=round(t/v),
N=a-1.                                                (3.19)
```

If `C_1(s)=0`, then Theorem 3.1 and Lemma 2.1 force

```text
[(s-1)S_N(s)+N(N+1)^(-s)]/[s(s+1)]

 =-a^(-s-1)G(iv)+o(a^(-sigma-1)).                    (3.20)
```

Thus the genuinely unresolved head has length `O(t)`, and it can be taken
arbitrarily close to `t/(2 pi)` from above.  This is a strict improvement of
the `O(t^2)` R94 cutoff, not a zero-free theorem.

## 4. A single branch passes every integer alias

It is useful to allow a general real observable `h` on the future
coordinate.  Define

```text
J_(n,h)(s)
 =p_n integral_0^1 h(y)phi_n(y)^(s-1)dy.             (4.1)
```

The target has `h(y)=y`.

**Theorem 4.1 (alias--Fourier correspondence).**  Fix a nonzero positive
integer `k`, fix `sigma` in a compact subset of `(0,infinity)`, and let

```text
s_t=sigma+it,
n_t=nearest_integer(t/(2 pi k)).                     (4.2)
```

For every `h in L^1(0,1)`,

```text
n_t^(s_t+1)J_(n_t,h)(s_t)
 ->integral_0^1 h(y)exp(2 pi i k y)dy.                (4.3)
```

For the actual Luroth observable,

```text
n_t^(s_t+1)J_n_t(s_t)->1/(2 pi i k).                 (4.4)
```

### Proof

Write

```text
phi_n(y)=n^(-1)[1-(1-y)/(n+1)].                      (4.5)
```

Then the integrand after multiplication by `n^(s+1)` is

```text
[n/(n+1)]h(y)
 [1-(1-y)/(n+1)]^(s-1).                              (4.6)
```

Under (4.2), `(s_t-1)/n_t ->2 pi i k`, so (4.6) tends pointwise to

```text
h(y)exp[-2 pi i k(1-y)]
=h(y)exp(2 pi i k y).                                (4.7)
```

Its modulus is dominated by a fixed multiple of `abs(h(y))`.  Dominated
convergence proves (4.3).  Finally

```text
integral_0^1 y exp(2 pi i k y)dy=1/(2 pi i k).       (4.8)
```

QED.

This is the coefficient-level reason adjacent pairing fails.  At an alias,
the shift phase has returned to one, so the discrete correction in (2.1)
does not oppose the term `s f_n`.  It passes it at full first order.

## 5. Stationary windows reconstruct the complementary Dirichlet phases

A single alias is not an isolated digit.  Neighboring digits align on the
stationary scale.

For fixed `k>=1` and `c>0`, put

```text
n_k=t/(2 pi k),

W_(k,c)(t)={n in positive integers:
            abs(n-n_k)<=c sqrt(t)/k},                (5.1)

B_(k,c)(s)=sum_(n in W_(k,c)(t))J_n(s),              (5.2)

I_c=integral_(-c)^c exp(2 pi^2 i u^2)du.             (5.3)
```

**Theorem 5.1 (stationary alias block).**  Fix `k`, `c`, and
`0<sigma_0<=sigma<=1`.  As `t` tends to positive infinity,

```text
B_(k,c)(sigma+it)

 =(2 pi)^sigma I_c/i
  t^(-sigma-1/2)
  exp(i[t-t log(t/(2 pi))])
  k^(sigma-1+it)

  +o_(k,c,sigma_0)(t^(-sigma-1/2)).                  (5.4)
```

If, for example,

```text
0<c<1/sqrt(8 pi),                                    (5.5)
```

then `I_c!=0`; hence every fixed alias block has a genuine lower bound of
order (1.8).

### Proof

Theorem 4.1 is uniform when

```text
n=n_k+O(sqrt(t)/k),                                  (5.6)
```

and gives

```text
J_n(s)=n^(-s-1)[1/(2 pi i k)+O(t^(-1/2))].           (5.7)
```

Write

```text
u=k(n-n_k)/sqrt(t).
```

Taylor expansion yields, uniformly on the window,

```text
exp[-it log(n/n_k)]
 =exp(it)exp(2 pi^2 i u^2)[1+O(t^(-1/2))].           (5.8)
```

Here the linear term is

```text
exp[-2 pi i k(n-n_k)]
=exp(-2 pi i k n)exp(2 pi i k n_k)
=exp(it),                                             (5.9)
```

so integer sampling removes it exactly.  The remaining sum is a Riemann sum
with mesh `k/sqrt(t)` and tends to `(sqrt(t)/k)I_c`.  Substitution of

```text
n_k^(-s-1)
 =(t/(2 pi k))^(-sigma-1)
  exp[-it log(t/(2 pi))]k^(it)                       (5.10)
```

proves (5.4).  Under (5.5), the phase of the integrand in (5.3) remains in
an open quadrant, so `I_c` cannot vanish.  QED.

For a finite set `K` of fixed resonance indices, the windows are disjoint
for large `t`, and (5.4) gives

```text
sum_(k in K)B_(k,c)(s)

 =common_nonzero_factor
  *sum_(k in K)k^(s-1)
  +o(t^(-sigma-1/2)).                                (5.11)
```

This is not an analogy with the functional equation.  It is the direct
stationary-phase output of the actual positive Luroth coefficients.  The
local block signs have become the dual Dirichlet phases.

## 6. Finite resonance phase-locking is impossible

The phases in (5.11) have enough arithmetic freedom to defeat every fixed
blockwise cone.

**Theorem 6.1 (finite prime-block cancellation).**  Fix `c` satisfying
(5.5), and fix

```text
0<sigma<=1
```

and choose sufficiently many distinct primes `p_1,...,p_m`.  There are
arbitrarily large heights `t` for which

```text
abs(sum_(j=1)^m B_(p_j,c)(sigma+it))
=o(t^(-sigma-1/2))                                   (6.1)
```

along a suitable sequence of heights.  Consequently no positive lower
bound of the natural block scale can hold uniformly for a fixed finite
collection of actual prime-indexed resonance windows.

### Proof

The positive lengths

```text
w_j=p_j^(sigma-1)                                    (6.2)
```

can be chosen so that the largest is no greater than the sum of the others:
add primes until the remaining weights exceed the first.  Thus there are
unit complex numbers `omega_j` with

```text
sum_j w_j omega_j=0.                                  (6.3)
```

Unique factorization implies that

```text
log p_1,...,log p_m
```

are linearly independent over the rationals.  Kronecker's approximation
theorem therefore supplies arbitrarily large `t` for which

```text
p_j^(it) ->omega_j                                   (6.4)
```

simultaneously along a sequence.  Insert (6.3)--(6.4) into (5.4) and sum
over `j`.  QED.

For `sigma=1`, two blocks already exhibit the issue: along

```text
t=(2m+1)pi/log 2,
```

the leading phases of the `k=1` and `k=2` blocks are opposite and have equal
magnitude.  Below `sigma=1`, more blocks form the required weighted polygon.

The theorem does not say the complete resonant head vanishes at those
heights.  It proves the sharper methodological statement needed here:
strict lower bounds for separate stationary blocks, followed by finite
phase-locking or a triangle inequality, cannot control the complete signed
head.

## 7. Why smoothing the future observable loses the divisor

The alias coefficient in Theorem 4.1 has a simple endpoint interpretation.
If `h` is absolutely continuous, integration by parts gives

```text
integral_0^1 h(y)exp(2 pi i k y)dy

 =[h(1)-h(0)]/(2 pi i k)
  -[1/(2 pi i k)]
    integral_0^1 h'(y)exp(2 pi i k y)dy.             (7.1)
```

For `h(y)=y`, the interior integral is zero.  Every alias in (4.4) is pure
endpoint mismatch.  Making `h(0)=h(1)` removes that leading boundary term,
but changes the carrier.  If a real `L^1` observable annihilates all nonzero
integer aliases, Fourier uniqueness makes it constant almost everywhere;
its correlation is then the spectator `1/s`.

There is an exact finite-polynomial rigidity theorem as well.  Put

```text
M_d(s)=integral_0^1 T(x)^d x^(s-1)dx.                (7.2)
```

Expanding on each branch shows that `M_d` is a rational combination of

```text
1,zeta(s),zeta(s-1),...,zeta(s-d+1),                 (7.3)
```

and its lowest shifted value has the nonzero coefficient

```text
[(-1)^(d-1)d!(s-d)]/[s(s+1)...(s+d)]
 *zeta(s-d+1).                                       (7.4)
```

For completeness, the branch expansion behind this assertion is

```text
p_n integral_0^1 y^d phi_n(y)^(s-1)dy

 =[n(n+1)]^(-s)
  sum_(j=0)^d binomial(d,j)(-n)^(d-j)
  [(n+1)^(s+j)-n^(s+j)]/(s+j).                       (7.5)
```

Shift the second endpoint by one and expand the resulting degree-`d`
polynomials.  Their degree-`d` terms cancel.  Direct coefficient extraction,
using the elementary binomial partial-fraction identity, gives the
degree-`d-1` coefficient in (7.4).  Lower powers give only the higher shifts
listed in (7.3) and an endpoint rational function.

**Lemma 7.1 (shift independence).**  The functions

```text
1,zeta(s),zeta(s-1),...,zeta(s-r)                    (7.6)
```

are linearly independent over the rational-function field `C(s)`.

### Proof

Suppose a rational relation exists and clear denominators, leaving
polynomial coefficients.  On a far-right real half-line, insert the
absolutely convergent Dirichlet series.  The coefficient of `n^(-s)` is a
polynomial in `s` whose coefficients are polynomials in `n`.

First let real `s` tend to infinity.  The `n=1` polynomial must be
exponentially small and hence is identically zero.  Remove it, multiply by
`2^s`, and repeat; the `n=2` polynomial must vanish.  Induction gives
vanishing for every integer `n`.  A polynomial in `n` which vanishes at all
positive integers has every coefficient zero.  The separate rational term
then vanishes as well.  QED.

**Theorem 7.2 (finite polynomial carrier rigidity).**  Let

```text
h_s(y)=sum_(d=0)^D a_d(s)y^d,
```

where all `a_d(s)` are rational functions.  If, identically as a meromorphic
function,

```text
integral_0^1 h_s(Tx)x^(s-1)dx=R(s)M_1(s)             (7.7)
```

for a rational function `R`, then

```text
h_s(y)=R(s)y.                                         (7.8)
```

### Proof

If a coefficient of degree `D>=2` were nonzero, (7.4) would make
`zeta(s-D+1)` occur in the left side of (7.7).  No lower moment contains that
shift.  Lemma 7.1 forces its coefficient to vanish, a contradiction.
Descending induction leaves only degrees zero and one.  The constant moment
is `M_0(s)=1/s`, so Lemma 7.1 forces its coefficient to vanish as well; the
coefficient of `M_1` must be `R`.  QED.

Thus no finite polynomial nonlinear observable can both suppress the
endpoint aliases and preserve the zeta zero set through a known rational
multiplier.  The positive lift `y(1-y)` from R94 is the first example: it
improves endpoint behavior but becomes a nonzero `zeta(s-1)` spectator at
every target zero.

## 8. The exact surviving signed theorem

Choose a fixed

```text
0<v<2 pi,
a(s)=nearest_integer(abs(t)/v),
N(s)=a(s)-1.                                         (8.1)
```

Theorem 3.1 gives a fully explicit tail vector.  A sufficient fixed-strip
result would now be a signed estimate proving, for some `eta>0`,

```text
abs(
 [(s-1)S_N(s)+N(N+1)^(-s)]/[s(s+1)]
 +a^(-s-1)G(i t/a)
)

 >epsilon_(v) a^(-sigma-1)                          (8.2)
```

throughout

```text
1-eta<sigma<1,
abs(t)>=t_0,                                         (8.3)
```

after including the `o(a^(-sigma-1))` error in Theorem 3.1.

The point of (8.2) is not another formal equivalence.  The preceding
theorems have audited its internal mechanisms.

1. The tail is already signed and nonzero; no further smoothing is needed.
2. Its first obstruction occurs sharply at the lattice alias `2 pi`.
3. Each alias block is individually coherent, so cancellation cannot be
   obtained inside a small adjacent window.
4. Different blocks carry the flexible phases `k^(it)`, so individual block
   lower bounds do not globalize.
5. A finite change of the Luroth observable either retains the same alias or
   loses the zeta divisor.

Any successor must therefore couple an unbounded collection of resonance
indices using their multiplicative relations.  That is a genuinely global
arithmetic input; transfer contraction, local phase cones, finite
martingales, and finite polynomial filters no longer qualify.

## 9. Disposition

This report proves the following advances and no-go results.

1. The far Luroth tail has the explicit linear-scale symbol `G`; it remains
   nonzero all the way to the first sampling alias.
2. The unresolved head is shortened rigorously from `O(t^2)` to just above
   `t/(2 pi)`.
3. The actual target coefficient passes every fixed integer alias with the
   nonzero response `1/(2 pi i k)`.
4. A coherent stationary window is evaluated asymptotically and produces
   the exact dual phase `k^(s-1)`.
5. Finite collections of prime-indexed blocks have arbitrarily flexible
   phases and admit arbitrarily small normalized signed sums.
6. All-alias suppression forces a real observable to be constant, while
   finite polynomial carrier preservation forces it to remain a scalar
   multiple of the original `y`.

No fixed zero-free strip and no failure of every fixed strip is proved.  The
survivor is now the global multiplicative coupling of all stationary alias
blocks in the linear resonant head.  Every local or finite-dimensional
version of that coupling tested here is rigorously closed.
