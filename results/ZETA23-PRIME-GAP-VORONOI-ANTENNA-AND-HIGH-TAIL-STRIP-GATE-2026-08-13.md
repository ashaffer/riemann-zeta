# Prime-gap Voronoi antenna and the surviving high-tail strip gate

**Date:** 2026-08-13

**Verdict:** a mean-square theorem for consecutive prime gaps gives a
strictly stronger actual-prime antenna than the maximal-gap hat rule.  A
positive nearest-prime Voronoi quadrature has Fourier error

```text
|P_Y(t)-b(t)| <<_epsilon |t| Y^(-77/100+epsilon).       (0.1)
```

Consequently the fixed-power certificate with exponent `.019` now holds
through

```text
|t| <= Y^.751,                                         (0.2)
```

not merely through `Y^.4655`.  This uses Julia Stadlmann's imported theorem

```text
sum_(p_n<=x) (p_(n+1)-p_n)^2 <<_epsilon x^(123/100+epsilon).
                                                               (0.3)
```

The proof below is deterministic after (0.3), uses the actual prime nodes,
and applies to arbitrary signed low measures through the hybrid dual lemma.
If one prefers the older `5/4` mean-square-gap exponent of Peck--Maynard,
the same argument still proves exponent `.019` through `Y^.731`.

The remaining legal tail is

```text
Y^.751 <= |t| <= Y^(50/33).                            (0.4)
```

It is not closed here.  Increasing the local interpolation order provably
makes the exponent worse when one uses only the available mean-square and
maximal-gap inputs.  The all-integer logarithmic phase has an easy saving of
at least `Y^(-8/33)`, but Vaughan's balanced Type-II phase is multiplicatively
separable and a coefficient-blind exponent-pair argument loses all of that
curvature.  A uniform complex power estimate for the natural prime weights,
with the interval and height uniformity needed by such a Vaughan theorem,
would itself imply a fixed zero-free strip by Turan's criterion.  Thus the
strict survivor is a genuinely global estimate for inverse-density/gap
weights, or an arbitrary-coefficient Chebyshev design not reducible to the
natural von-Mangoldt quadrature.

No zero-free strip is claimed.

---

## 1. Setup and the imported prime-gap input

Fix `0<w<1`, `alpha>0`, and put

```text
phi(u)=(1-|u|/w) exp(alpha u),       -w<=u<=w,
b(t)=integral_(-w)^w phi(u) cos(tu)du.                 (1.1)
```

Let

```text
p_1<...<p_J
```

be all primes in `[Y exp(-w),Y exp(w)]`, and set

```text
v_j=log(p_j/Y).                                        (1.2)
```

Proper prime-power coordinates in the larger active set are assigned
coefficient zero.

We import the following theorem.

### LIT-GAP2 (Stadlmann)

For every fixed `epsilon>0`,

```text
sum_(p_n<=x) (p_(n+1)-p_n)^2
 <<_epsilon x^(123/100+epsilon).                       (1.3)
```

The statement is Theorem 1 of Julia Stadlmann,
[*On the mean square gap between primes*](https://arxiv.org/abs/2212.10867).
The paper states the exponent as `1.23`.  This is an imported literature
theorem; its 71-page Harman-sieve proof is not reproduced here.

For comparison, replacing `123/100` by `5/4` gives the earlier
Peck--Maynard theorem; see James Maynard,
[*On the difference between consecutive primes*](https://arxiv.org/abs/1201.1787).

For consecutive primes in one fixed multiplicative shell,

```text
log(p_(n+1)/p_n)
 <=(p_(n+1)-p_n)/p_n
 <<_w (p_(n+1)-p_n)/Y.                                (1.4)
```

Therefore (1.3) gives

```text
sum_(p_j,p_(j+1) in shell) (v_(j+1)-v_j)^2
 <<_(w,epsilon) Y^(-77/100+epsilon).                   (1.5)
```

The Baker--Harman--Pintz maximal-gap theorem also puts a prime within
`O_w(Y^(21/40))` of either multiplicative endpoint.  In logarithmic
coordinates the two endpoint distances are consequently

```text
d_-,d_+ <<_w Y^(-19/40).                              (1.6)
```

Only (1.6), not a maximal-gap bound throughout the shell, is needed below.

---

## 2. Nearest-prime Voronoi quadrature

Partition `[-w,w]` into logarithmic Voronoi cells `C_j`: an interior
boundary between `v_j` and `v_(j+1)` is their midpoint, and the first and
last cells are truncated at `-w` and `w`.  Define the positive actual-node
weights

```text
lambda_j=integral_(C_j) phi(u)du,
P_Y(t)=sum_j lambda_j cos(t v_j).                      (2.1)
```

Let `v(u)=v_j` on `C_j` and define the transport cost

```text
D_Y=integral_(-w)^w phi(u)|u-v(u)|du.                  (2.2)
```

### Lemma 2.1 (mean-square-gap transport bound)

For every fixed `epsilon>0`,

```text
D_Y <<_(w,alpha,epsilon) Y^(-77/100+epsilon).          (2.3)
```

#### Proof

On the two halves of an interior gap of logarithmic length `Delta_j`,

```text
integral phi(u)|u-v(u)|du
 <=||phi||_infinity Delta_j^2/4.                       (2.4)
```

Summing (2.4) and using (1.5) gives (2.3) away from the endpoints.

At the left endpoint write `u=-w+x`, `0<=x<=d_-`.  Since `phi` vanishes
linearly at `-w`,

```text
phi(-w+x)<<x,
integral_0^(d_-) x(d_--x)dx <<d_-^3.                  (2.5)
```

The right endpoint is identical.  Equation (1.6) makes their total
`O(Y^(-57/40))`, smaller than (2.3).  QED

### Theorem 2.2 (actual-prime Voronoi Fourier error)

Uniformly for real `t`,

```text
|P_Y(t)-b(t)|
 <<_(w,alpha,epsilon) |t|Y^(-77/100+epsilon).          (2.6)
```

#### Proof

It is slightly cleaner to use the complex transforms.  By (2.1),

```text
sum_j lambda_j exp(i t v_j)-integral phi(u)exp(i t u)du
 =integral phi(u)[exp(i t v(u))-exp(i t u)]du.         (2.7)
```

The elementary inequality

```text
|exp(ix)-exp(iy)|<=|x-y|                               (2.8)
```

and Lemma 2.1 prove the complex version of (2.6).  Taking real parts proves
the displayed assertion.  QED

This estimate is exact at `t=0`: the weights have total mass
`integral phi`.  It does not replace primes by a random model or by all
integers.

---

## 3. The improved hybrid power antenna

The compact tent `phi` has distributional second derivative a finite
measure and vanishes at both endpoints.  Hence

```text
|b(t)|<<_(w,alpha)(1+t^2)^(-1).                        (3.1)
```

Let

```text
L_Y=[0,Y^tau],
H_Y^0=[Y^tau,Y^sigma],
0<tau<sigma<77/100.                                   (3.2)
```

In the notation of the hybrid dual lemma from
`ZETA23-PRIME-LOG-HYBRID-ANTENNA-CHRISTOFFEL-FRONTIER-2026-08-13.md`,
Theorem 2.2 gives

```text
eta_(L_Y)(lambda)
 <<_epsilon Y^[-(77/100-tau)+epsilon],

epsilon_(H_Y^0)(lambda)
 <<Y^(-2tau)+Y^[-(77/100-sigma)+epsilon].             (3.3)
```

Consequently

```text
C_(L_Y,H_Y^0)
 >>_epsilon Y^[d-epsilon],

d=min{77/100-tau, 2tau, 77/100-sigma}.                (3.4)
```

### Corollary 3.1 (the `.019` band reaches `Y^.751`)

Take

```text
tau=.01,          sigma=.751.                          (3.5)
```

Then

```text
d=min(.76,.02,.019)=.019>.0180303234.                  (3.6)
```

Thus the explicit positive actual-prime coefficients (2.1) prove the
required fixed-power hybrid lower cost against **arbitrary signed low
measures** throughout `[0,Y^.751]`.

More generally, the upper endpoint can approach

```text
sigma<.77-.0180303234=.7519696766.                     (3.7)
```

The conservative rational choice (3.5) leaves enough room to absorb the
`epsilon` in the imported gap theorem.

With only the older `5/4` mean-square-gap exponent, replace `.77` by `.75`.
Then `tau=.01`, `sigma=.731` again give `d=.019`.  Hence a substantial
extension beyond `.4655` does not depend on the newest exponent.

---

## 4. Higher local reconstruction moves the wrong way

It is tempting to replace nearest-node quadrature by degree-`r` local
polynomial interpolation.  The available gap inputs give a precise no-go
for that **absolute Peano-remainder strategy**.

Let

```text
Delta_max <<Y^(-19/40),
sum_j Delta_j^2 <<_epsilon Y^(-77/100+epsilon).        (4.1)
```

A degree-`r` local rule has a standard pointwise remainder bounded by a
constant times

```text
|t|^(r+1) Delta^(r+1).                                (4.2)
```

After integration over the cells, (4.1) gives

```text
error_r(t)
 <<_(r,epsilon)
 |t|^(r+1) sum_j Delta_j^(r+2)

 <=|t|^(r+1) Delta_max^r sum_j Delta_j^2

 <<|t|^(r+1)
   Y^[-(77/100+(19/40)r)+epsilon].                    (4.3)
```

The corresponding zero-loss frequency exponent is

```text
beta_r=[77/100+(19/40)r]/(r+1)
      =19/40+(59/200)/(r+1).                          (4.4)
```

It is strictly decreasing in `r`:

```text
beta_0=.77,
beta_1=.6225,
beta_2=.573333...,
beta_r downarrow .475.                                (4.5)
```

Thus nearest-node transport (`r=0`) is optimal within this imported-gap,
cellwise-absolute family.  Higher order suppresses the contribution of a
fixed small gap but lets the sparse largest gaps control the absolute
remainder.  This theorem does not rule out a global signed rule exploiting
cancellation between different gaps.

---

## 5. Curvature would solve the tail on all integers

The phase itself is not too weak.  For a fixed smooth weight `W` and

```text
S_Y(t)=sum_(n asymp Y) W(n/Y) exp(i t log(n/Y)),        (5.1)
```

one has

```text
|f''(x)| asymp |t|/Y^2,
f(x)=t log x.                                         (5.2)
```

The second-derivative estimate, with routine partial summation for `W`,
gives

```text
|S_Y(t)|/Y
 <<_W |t|^(1/2)/Y+|t|^(-1/2).                         (5.3)
```

If `|t|=Y^a` and

```text
.751<=a<=50/33,
```

the saving in (5.3) is

```text
min{a/2,1-a/2}>=8/33=.242424... .                     (5.4)
```

This is more than thirteen times the required `.0180303234`.  So the
remaining obstruction is not lack of one-variable curvature; it is the
transfer from all integers to the actual prime-supported, low-carrier
quadrature.

---

## 6. Why Vaughan and Heath--Brown do not transfer (5.3)

On a balanced Type-II rectangle, the height phase factorizes exactly:

```text
exp(i t log(mn))=m^(it)n^(it).                         (6.1)
```

Therefore

```text
sum_(m,n) a_m b_n (mn)^(it)
 =[sum_m a_m m^(it)] [sum_n b_n n^(it)]               (6.2)
```

when the rectangle has no product cutoff; smooth partitions give a short
sum of the same tensors.  Any estimate which remembers only coefficient
moduli or `L2` norms has no curvature left: the legal choices

```text
a_m=m^(-it),       b_n=n^(-it)                        (6.3)
```

saturate the trivial bound.  This is an exact counterexample to a
coefficient-uniform Type-II exponent-pair transfer.

The actual Vaughan coefficients are not adversarial arbitrary sequences,
so (6.3) is not a no-go for every coefficient-specific proof.  But using
their Möbius or von-Mangoldt signs pointwise is precisely the missing
arithmetic cancellation.  The Voronoi weights (2.1), which depend on
neighboring prime gaps, do not possess a finite Vaughan or Heath--Brown
convolution identity.  Expanding the condition that a gap contains no prime
produces a growing sieve inclusion--exclusion and returns the parity/global
cancellation problem.

Thus the two available structures remain complementary rather than
composable:

```text
Voronoi/gap weights:   power-accurate low carrier through Y^.751,
                       no known global high-t twist theorem;

Lambda/log weights:   exact Vaughan arithmetic,
                       only logarithmic pointwise saving unconditionally.
                                                               (6.4)
```

---

## 7. The natural complex estimate is quantitatively strip-strength

This section concerns the **natural prime weights and their usual interval
uniformity**, not the optimized arbitrary coefficients in H1.

Turan's criterion, in the formulation quoted in
`ZETA23-SCALAR-PRIME-POLYNOMIAL-FIXED-SAVING-AUDIT-2026-08-11.md`, assumes
for every prime interval in a power-wide family

```text
|sum_(N_1<=p<=N_2) p^(-i tau)|
 <=c N(log N)^10/T^beta                              (7.1)
```

on a local height window, with

```text
T^[D(1-beta^(1/6))] <=N<=2N<=T^[D(1+beta^(1/6))].    (7.2)
```

It concludes that the corresponding height parallelogram contains no zeta
zero with

```text
Re(s)>1-beta^2.                                       (7.3)
```

Suppose a Vaughan/exponent-pair theorem supplied, with the interval and
height uniformity in (7.1)--(7.2),

```text
|sum_(N_1<=p<=N_2) p^(-i tau)|
 <<N^(1-eta)(log N)^C,

eta=.0180303234.                                     (7.4)
```

At the transition `D=1`, take explicitly

```text
beta=.009.                                            (7.5)
```

Then

```text
beta^(1/6)=.4560793596...,

eta[1-beta^(1/6)]
 =.0098070650... >.009=beta.                          (7.6)
```

The logarithms in (7.4) are absorbed by the strict margin in (7.6), so
(7.4) implies (7.1) for large `T`.  Turan then gives the explicit fixed
strip

```text
Re(s)>1-.009^2=1-.000081.                             (7.7)
```

This does not prove (7.4), and the one fixed-window arbitrary-weight H1
statement does not automatically imply all the quantifiers in (7.4).
It does show sharply why a routine natural-weight Vaughan estimate at the
requested exponent is unavailable: in its standard uniform form it is
already a solution of the fixed-strip problem, not a weaker imported lemma.

---

## 8. Exact renewal transform and its conductor barrier

The consecutive-gap weights do have an exact telescoping transform.  It
explains both the gain `.77` and why analytic continuation of that transform
alone stops at the same frequency.

Write

```text
x_n=log p_n,
Delta_n=x_(n+1)-x_n=log(p_(n+1)/p_n),

A(z)=sum_(n>=1) Delta_n p_n^(-z),       Re(z)>0.       (8.1)
```

The coefficients telescope in logarithmic measure.  Hence the natural
continuum comparison is

```text
I(z)=integral_(log 2)^infinity exp(-zu)du=2^(-z)/z.   (8.2)
```

### Theorem 8.1 (renewal continuation)

Put `q=77/100`.  The difference

```text
H(z)=A(z)-2^(-z)/z                                   (8.3)
```

extends holomorphically to

```text
Re(z)>-q.                                             (8.4)
```

On every fixed vertical line in (8.4),

```text
H(sigma+it)<<_sigma 1+|t|.                            (8.5)
```

For every `0<=r<q` and every `epsilon>0`,

```text
H(-r+it)<<_(r,epsilon)(1+|t|)^(r/q+epsilon).          (8.6)
```

#### Proof

Initially in `Re(z)>0`, telescope the continuum integral gap by gap:

```text
H(z)
 =sum_n integral_(x_n)^(x_(n+1))
   [exp(-z x_n)-exp(-zu)]du.                          (8.7)
```

On a compact subset of `Re(z)>-q`, the `n`-th summand is at most

```text
C |z| Delta_n^2 p_n^(-Re(z)).                         (8.8)
```

The factor `exp(|Re(z)|Delta_n)` implicit in the mean-value bound is
uniformly bounded after finitely many initial gaps.  From (1.3)--(1.4), on
every dyadic prime shell,

```text
sum_(p_n asymp X) Delta_n^2
 <<_epsilon X^(-q+epsilon).                           (8.9)
```

Thus (8.7) converges normally whenever `Re(z)>-q`, proving (8.4) and
(8.5).

On `Re(z)>=epsilon>0`, the defining series for `A` converges absolutely and
is bounded in `t`, so

```text
H(epsilon+it)<<_epsilon 1.                            (8.10)
```

Apply Phragmen--Lindelof in the strip from
`Re(z)=-q+epsilon` to `Re(z)=epsilon`, using (8.5) on the left and (8.10)
on the right.  At `Re(z)=-r` this gives exponent
`(r+epsilon)/q`.  Letting the auxiliary epsilon shrink proves (8.6), with
an arbitrarily small exponent loss.  QED

The same theorem has an exact shell consequence.  Let `W` be a fixed
smooth compactly supported multiplicative weight and define

```text
S_(Y,W)(t)
 =sum_n Delta_n W(p_n/Y)(p_n/Y)^(it),

J_(Y,W)(t)
 =integral_0^infinity W(x/Y)(x/Y)^(it) dx/x.          (8.11)
```

Mellin inversion and (8.3) give exactly

```text
S_(Y,W)(t)-J_(Y,W)(t)
 =Y^(-it)/(2 pi i) integral_(c-i infinity)^(c+i infinity)
   W_hat(s)Y^s H(s-it)ds.                             (8.12)
```

Shift to `Re(s)=-r` and use the rapid decay of `W_hat` with (8.6):

```text
|S_(Y,W)(t)-J_(Y,W)(t)|
 <<_(W,r,epsilon)
 Y^(-r)(1+|t|)^(r/q+epsilon),

0<=r<q.                                               (8.13)
```

If `|t|=Y^a`, the power in (8.13) is

```text
-r+a*r/q+epsilon*a.                                  (8.14)
```

For `a<q`, taking `r` near `q` recovers the transport saving
`Y^[-(q-a)+o(1)]`.  For

```text
a>=q=.77,                                             (8.15)
```

the coefficient of every positive `r` in (8.14) is nonnegative.  The best
bound furnished by renewal continuation and Phragmen--Lindelof is then the
line `r=0`, which has no fixed negative power.

This is a sharp no-go for the **bare telescoping/analytic-continuation
mechanism**, not for the actual gap sum.  A stronger boundary estimate for
`H(-r+it)` using signed correlations between different gaps could cross
(8.15), but (1.3) and absolute convergence do not provide one.

The higher-order ledger in Section 4 has the same analytic meaning.  A
degree-`k` local cancellation continues the error farther left, by
`q+(19/40)k`, but its boundary growth becomes `|t|^(k+1)`.  Their ratio is
exactly `beta_k` in (4.4), so higher-order renewal subtraction cannot evade
the conductor barrier either.

The connection with the exact Voronoi cells can be made without a heuristic.
For an interior node, Taylor's theorem gives

```text
lambda_n
 =phi(v_n)(Delta_(n-1)+Delta_n)/2
  +O_(phi)(Delta_(n-1)^2+Delta_n^2).                 (8.16)
```

The total coefficient error on a shell is `O(Y^(-q+epsilon))`, uniformly
in `t`, by (8.9).  The right-renewal series

```text
sum_n Delta_n p_(n+1)^(-z)                           (8.17)
```

differs from `A(z)` by a series whose terms are
`O(|z|Delta_n^2 p_n^(-Re(z)))`; it therefore has the same continuation and
growth ledger.  Averaging the left and right series gives the leading term
in (8.16).  A fixed smooth localization `phi(log(x/Y))` is inserted by the
Mellin formula (8.12).  The actual tent is piecewise smooth with two
integrations of Fourier decay, which is enough for the polynomial growth
in (8.6); equivalently one may split it at zero.

Thus the renewal barrier applies to the exact Voronoi-gap route at the
exponent level, while preserving the possibility of a new global signed
estimate for the continued boundary values.

---

## 9. Large-sieve supremum conversion and density-only discrepancy fail

The Voronoi weights have a favorable quadratic norm:

```text
L_2(Y)=sum_j lambda_j^2
 <<_epsilon Y^(-q+epsilon),       q=77/100.           (9.1)
```

Indeed each cell mass is bounded by a constant times the sum of its two
adjacent logarithmic gaps, so (9.1) follows from (8.9).  Nevertheless the
ordinary large-sieve/high-moment route cannot turn this into a supremum
power.

### Proposition 9.1 (weighted moment exponent barrier)

Let

```text
P(t)=sum_j lambda_j exp(i t v_j),
sum_j |lambda_j|=O(1),
sum_j |lambda_j|^2<=Y^(-q+o(1)),                      (9.2)
```

with distinct prime nodes in a fixed multiplicative shell.  The bound
obtained by applying the ordinary Dirichlet-polynomial mean-value theorem
to `P^k` and then converting the moment to a supremum by the Lipschitz
bound is

```text
[sup_I |P|]^(2k+1)
 <<_k (|I|+Y^k)Y^(-qk+o(1)).                          (9.3)
```

On the full interval `|I|=Y^A`, `A=50/33`, its formal power exponent is

```text
[max(A,k)-qk]/(2k+1).                                 (9.4)
```

It is positive for every integer `k>=1` when `q=77/100`.  Even under the
ideal mean-square-gap scale `q=1`, it is merely nonnegative and supplies no
fixed-power saving.

#### Proof

Expand

```text
P(t)^k=sum_n a_k(n) exp(i t log(n/Y^k)).               (9.5)
```

Unique factorization groups two ordered prime tuples only when their
multisets agree.  If a multiset has permutation count `R<=k!`, its squared
coefficient is `R^2` times the product of the corresponding
`|lambda_p|^2`; comparison with the `R` copies in
`(sum |lambda_p|^2)^k` gives

```text
sum_n |a_k(n)|^2<=k![L_2(Y)]^k.                        (9.6)
```

The mean-value theorem now gives the right side of (9.3) for the `2k`-th
moment.  Since all `v_j` lie in a fixed compact interval,

```text
sup_t |P'(t)|<<sum_j |lambda_j|<<1.                   (9.7)
```

At a point of height `B=sup_I|P|`, the modulus stays at least `B/2` on a
one-sided interval of length `gg B`; hence the moment is `gg_k B^(2k+1)`.
This proves (9.3).  For `A=50/33`, the numerator in (9.4) is `A-q>0` at
`k=1` and `k(1-q)>0` at every `k>=2`.  QED

This proposition is scoped to ordinary moments plus a derivative
conversion.  It does not prove that the true supremum is large; it proves
that the favorable gap `L2` norm is still on the wrong side of the exact
conductor ledger.

There is also a deterministic reason that a discrepancy theorem using only
node count and mesh cannot work.  Take `M` equally spaced nodes

```text
u_j=-w+jh,              h=2w/(M-1).                   (9.8)
```

For **every** signed coefficient vector and every integer `m`,

```text
P(2 pi m/h)=exp(-2 pi i m w/h)P(0),

|P(2 pi m/h)|=|P(0)|.                                 (9.9)
```

Thus any quadrature which retains a constant carrier at zero has a
constant alias at its first recurrence `2 pi/h asymp M`.  With
`M asymp Y/log Y`, that recurrence lies far inside the legal aperture
`Y^(50/33)`, even though this countermodel has a much smaller maximal mesh
than the actual prime set.

Equation (9.9) rules out a universal Banaszczyk/Spencer, large-sieve, or
frame theorem based only on density, separation, and fill distance.  A
successful deterministic discrepancy construction must quantitatively use
the **nonlattice arithmetic of the actual prime logarithms** and rule out
their polynomial-height approximate aliases.  Existing KMT control gives
only a logarithmic bound for the natural unweighted direction; it does not
control every coefficient direction required by such a theorem.

---

## 10. Exact remaining gate

The theorem-grade advance is

```text
actual-prime power antenna through Y^.751:             PROVED;
required exponent on that band:                        .019;
arbitrary signed low measures included:                YES;
higher local Peano interpolation from known gaps:      WORSE;
all-integer curvature through full aperture:           EASY, >=8/33;
coefficient-blind Vaughan/Type-II transfer:             FALSE;
natural uniform complex fixed-power theorem:           STRIP-STRENGTH;
full H1 antenna through Y^(50/33):                      OPEN;
renewal transform continuation to Re(z)>-.77:           PROVED;
renewal/PL power beyond t=Y^.77:                        NO;
ordinary weighted large-sieve/moment supremum:          NO POWER;
density/mesh-only deterministic discrepancy:            FALSE;
full H1 antenna through Y^(50/33):                      OPEN;
uniform zeta zero-free strip:                           NOT PROVED.       (10.1)
```

After this advance, the unresolved statement is confined to

```text
Y^.751 <=|t|<=Y^(50/33).                               (10.2)
```

A valid successor must do at least one of the following.

1. Prove a uniform signed exponential-sum theorem for the inverse-density
   prime-gap weights (2.1), retaining cancellation between distinct gaps.
2. Construct different actual-prime coefficients which retain the low
   carrier and prove their full-band Chebyshev norm directly.
3. Prove the natural uniform complex prime estimate (7.4), thereby proving
   a zero-free strip outright rather than treating it as an intermediate
   lemma.

Lebesgue large values, higher local reconstruction, an all-integer exponent
pair, or a coefficient-blind Type-II estimate does not supply any of these
three statements.

The exact rational exponent and Turan arithmetic can be replayed with

```text
python3 results/prime_gap_voronoi_exponent_audit.py
```
