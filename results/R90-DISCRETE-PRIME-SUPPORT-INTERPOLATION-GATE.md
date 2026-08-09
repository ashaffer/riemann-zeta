# Discrete prime-support interpolation and the superoscillation gate

Status: R90 exact explicit-formula formulation, exact prime-log mesh
theorem, exact cancellation-reserve lemma, and a quantitative
degree/variation/amplitude dichotomy.  Requiring a derivative weight to be
nonnegative only at the actual prime powers is a genuine loophole in the
continuous Laplace argument.  It is **not** a free loophole.  At the
`x asyp log T` scale needed to distinguish ordinates a prime-log gap is at
most a fixed negative power of `T`.  A fixed amount of negative Laplace mass
hidden in such gaps therefore forces power-sized variation or amplitude (and,
under a stable-sup hypothesis, power-sized degree).  Every tempered
interpolation scheme is ruled out.

Arbitrary superoscillatory polynomials are not ruled out.  For them the exact
remaining task is a signed, target-conditioned estimate for all the other
zero kernels.  Section 10 gives a sufficient theorem which records that task
without suppressing any norm or tail dependence.  No fixed strip, and no
nonexistence of a fixed strip, is proved here.

```text
continuous positivity W(x)>=0                         pole dominates target
discrete positivity W(log p^j)>=0 only                genuine larger cone
prime-log mesh at x=X                                 << exp(-19X/40)
negative mass hidden above X                          variation cost exp(19X/40)
degree-M negative set                                 at most M+1 prime gaps
tempered M, amplitude, or variation at X~log T        CANNOT cancel the pole
untempered interpolation                              survives algebraically
finite-type canonical product over all prime logs     IMPOSSIBLE
exact remainder estimate needed for a strip           isolated in Theorem 10.1
fixed zero-free strip                                 NOT PROVED.             (1.1)
```

## 2. What analytic object a weight represents

Let

```text
W(x)=sum_(1<=m<=M) lambda_m x^m,       lambda_m real,              (2.1)
```

so in particular `W(0)=0`.  Put

```text
H_W(z)=integral_0^infinity W(x)e^(-zx)dx
      =sum_(1<=m<=M)lambda_m m! z^(-m-1),       Re z>0,            (2.2)

Q_W(s)=sum_(1<=m<=M)lambda_m Q_m(s)
      =sum_(n>=2)Lambda(n)W(log n)n^(-s),       Re s>1.            (2.3)
```

Here `Q_m=(-1)^m D^(m)` is the differentiated logarithmic derivative
from R89.  Since the smallest allowed derivative order is one,
`H_W(u+iv)=O_W((1+|v|)^(-2))` on every half-plane `u>=u_0>0`.
Consequently the zero sum below is absolutely convergent:

```text
Q_W(s)
 =H_W(s-1)
  -sum_rho H_W(s-rho)
  -sum_(j>=1)H_W(s+2j).                                    (2.4)
```

This is the exact explicit-formula combination represented by `W`; it is not
merely a formal interpolation polynomial.

If

```text
W(log n)>=0 whenever Lambda(n)>0,                            (2.5)
```

then for every nonnegative trigonometric polynomial `P`,

```text
sum_k a_k Re Q_W(sigma+i kT)
 =sum_(n>=2)Lambda(n)W(log n)n^(-sigma)P(T log n)>=0,         (2.6)
```

with the usual interpretation of the cosine coefficients.  In particular,
using `P(theta)=1+cos theta`,

```text
Q_W(sigma)+Re Q_W(sigma+iT)>=0.                              (2.7)
```

The exclusion of a constant term in (2.1) is substantive.  A `lambda_0`
term reintroduces the undifferentiated gamma/conductor contribution of size
`|lambda_0| log T`.  It can be included, but it must then appear explicitly
in every remainder bound.  Nothing below silently discards it.

For a nonpolynomial weight, minimum necessary replacement conditions are:

```text
sum_n Lambda(n)|W(log n)|n^(-sigma)<infinity,
integral_0^infinity |W(x)|e^(-u x)dx<infinity,
H_W(u+iv)=O((1+|v|)^(-2-epsilon))                            (2.8)
```

uniformly in the half-plane used in the zero sum, together with a valid
explicit-formula approximation/limiting argument for that test function.
Usually the last condition is obtained from two integrable derivatives and
vanishing boundary terms.  Conditions (2.8) by themselves are not asserted
to be a general Weil explicit-formula theorem.  An interpolation or
canonical product which does not even verify (2.8) cannot define the
differentiated explicit formula being proposed here.

## 3. The loophole is real

Write

```text
S={log(p^j): p prime, j>=1}.                                  (3.1)
```

Condition (2.5) says only `W>=0` on `S`.  A polynomial may be negative in a
component of `[0,infinity)\S` while all its prime coefficients remain
nonnegative.  Therefore the continuous implication

```text
H_W(delta+e)<=H_W(delta)                                     (3.2)
```

is false as a theorem about the discrete cone.  Here is an exact example:

```text
W(x)=x(x-1/30)(x-13/20).                                     (3.3)
```

Its only negative interval on the positive axis is contained in
`(0,log 2)`, so `W(log p^j)>=0` for every prime power.  On the other hand,

```text
H_W(r)
 =r^(-4)[6-(41/30)r+(13/600)r^2],                            (3.4)

H_W(60)=2/60^4>0,
H_W(61)=(651/200)/61^4>H_W(60).                              (3.5)
```

The last inequality is equivalent to
`651*60^4>400*61^4`.  Thus (3.2) fails with `delta=60,e=1`.
This example is far from a useful high-ordinate kernel, but it proves that
replacing discrete positivity by continuous positivity would assume away the
only new feature.

There are nevertheless two severe restrictions.

First, every connected component of `{x:W(x)<0}` is contained in one gap of
`S`.  Second, a degree-`M` real polynomial has at most `M+1` such components.
Thus using many gaps consumes either degree or variation.  The rest of this
report quantifies the statement at the scale relevant to zeros.

## 4. Prime powers give an exponentially fine logarithmic mesh

For `X>0`, let

```text
Delta(X)=sup{v-u: u<v are consecutive points of S and v>=X}.  (4.1)
```

It is enough to use the subset `{log p}`.  Baker--Harman--Pintz prove that,
for all sufficiently large `y`, `[y-y^(21/40),y]` contains a prime.  Applied
to consecutive primes and then taking logarithms, this gives

```text
Delta(X)<=C exp(-kappa X),
kappa=1-21/40=19/40.                                         (4.2)
```

The constant and starting point are irrelevant here; what matters is a fixed
positive `kappa`.  The source is R. C. Baker, G. Harman, and J. Pintz,
[*The difference between consecutive primes, II*](https://doi.org/10.1112/plms/83.3.532),
Proc. London Math. Soc. 83 (2001), 532--562.

At the resolving scale

```text
X=c log T,                                                     (4.3)
```

(4.2) becomes

```text
Delta(X)<<T^(-19c/40).                                        (4.4)
```

So an interpolating weight does not have intervals of fixed width in which
to hide.  It has prime-log gaps of power-small width.

## 5. Exact cancellation reserve

Put

```text
sigma=1+delta,       delta>0,
rho_0=1-e+iT,        e>0,
A=H_W(delta+e).                                             (5.1)
```

Assume `A>0`.  Define the negative pole-weighted mass

```text
N_delta(W)=integral_0^infinity W_-(x)e^(-delta x)dx,
W_-=max(-W,0).                                                (5.2)
```

### Lemma 5.1 (pole cancellation needs real negative mass)

If, for some `q<1`,

```text
H_W(delta)<=q A,                                              (5.3)
```

then

```text
N_delta(W)>=(1-q)A.                                          (5.4)
```

#### Proof

Since `e^(e x)-1>=0`,

```text
H_W(delta)-H_W(delta+e)
 =integral W(x)e^(-(delta+e)x)(e^(e x)-1)dx
 >=-integral W_-(x)e^(-delta x)dx.                            (5.5)
```

Combine (5.3) with `H_W(delta+e)=A`.

Thus the discrete construction cannot cancel the pole by a formal
coefficient identity alone.  It must hide at least a fixed fraction of the
target response as negative `L^1` mass between prime powers.

## 6. Two exact mesh inequalities

Let

```text
N_delta(X;W)=integral_X^infinity W_-(x)e^(-delta x)dx,

V_delta(X;W)
 =integral_(X-Delta(X))^infinity |W'(x)|e^(-delta x)dx,

B_delta(X;W)
 =sup_(x>=X) W_-(x)e^(-delta x).                              (6.1)
```

The harmless convention is that the lower endpoint in `V_delta` is replaced
by zero if necessary.

### Theorem 6.1 (prime-mesh variation bound)

For all sufficiently large `X`,

```text
N_delta(X;W)
 <=Delta(X)e^(delta Delta(X)) V_delta(X;W).                   (6.2)
```

#### Proof

Every negative component meeting `[X,infinity)` is contained in a
prime-power gap of length at most `Delta(X)`.  At an endpoint of that
component `W=0`.
The fundamental theorem of calculus bounds `W_-(x)` by the integral of
`|W'|` from the nearer endpoint.  Integrating once more over a component
costs its length.  Moving the exponential weight across that component costs
at most `exp(delta Delta(X))`.  Sum the disjoint components.

The same proof can be read as a positive discrete quadrature.  Partition the
tail into cells around points `s in S`, replace `W(x)` by `W(s)>=0`, and
bound the quadrature error by the right side of (6.2).  This is the precise
point at which interpolation condition number enters.

There is also a tempting exact-moment formulation.  If positive numbers
`omega_j` and nodes `s_j in S intersect [0,R]` satisfied

```text
integral_0^R x^m e^(-delta x)dx
 =sum_j omega_j s_j^m,             0<=m<=M,                  (6.2a)
```

then the truncated Laplace integral of every degree-`M`
discrete-positive polynomial would equal
`sum_j omega_jW(s_j)>=0`.  But by finite-dimensional separation/Farkas
duality, existence of (6.2a) is equivalent to the absence of a degree-`M`
polynomial which is nonnegative on that finite support and has negative
truncated integral.  Thus assuming such an exact quadrature would be
circular.  The cell quadrature above is non-circular because it exposes its
derivative error explicitly.

### Theorem 6.2 (degree-amplitude bound)

If `deg W<=M`, then

```text
N_delta(X;W)<=(M+1)Delta(X)B_delta(X;W).                      (6.3)
```

#### Proof

The negative set has at most `M+1` components, each is contained in one gap
of length at most `Delta(X)`, and the weighted height on every component is
at most `B_delta(X;W)`.

Combining Lemma 5.1 with either theorem gives the central dichotomy.  Put

```text
L_delta(X;W)
 =A^(-1)integral_0^X W_-(x)e^(-delta x)dx.                    (6.4)
```

Then fixed-reserve cancellation (5.3) implies

```text
1-q
 <=L_delta(X;W)
   +[Delta(X)e^(delta Delta(X))/A]V_delta(X;W),                (6.5)

1-q
 <=L_delta(X;W)
   +(M+1)Delta(X)B_delta(X;W)/A.                              (6.6)
```

In particular, if `L_delta(X;W)<=(1-q)/2`, then

```text
V_delta(X;W)/A
 >>exp(kappa X-delta Delta(X)),                               (6.7)

B_delta(X;W)/A
 >>exp(kappa X)/(M+1).                                       (6.8)
```

At `X=c log T`, with `delta Delta(X)=o(1)`, these costs are respectively
`T^(19c/40)` and `T^(19c/40)/(M+1)`.

### Definition 6.3 (tempered high-scale interpolation)

A family `W_T`, normalized by `H_(W_T)(delta+e)=1`, is tempered above
`X_T` if

```text
integral_0^X_T (W_T)_-(x)e^(-delta x)dx=o(1),

log^+ V_delta(X_T;W_T)=o(X_T),

delta Delta(X_T)=o(1).                                       (6.9)
```

It is amplitude-tempered if the second condition is replaced by

```text
log^+[(M_T+1)B_delta(X_T;W_T)]=o(X_T).                        (6.10)
```

### Corollary 6.4

No tempered high-scale interpolation can satisfy
`H_W(delta)<=qH_W(delta+e)` with a fixed `q<1` and `X_T->infinity`.

This is a genuine no-go theorem.  It covers bounded-variation and
polynomial-in-`X_T` (hence polylogarithmically-in-`T`) conditioned
interpolation at `X_T asyp log T`.  It does not cover superoscillation whose
norm is a fixed power of `T` or larger.

## 7. What degree and Remez/Markov theory add

The amplitude alternative in (6.8) is not an artifact of using `L^1`.
Suppose a negative component `J` of length `ell` contains a point `x_0`
with `W(x_0)=-D`, and a zero of `W` is at distance at most `ell`.  The mean
value theorem gives

```text
sup_J |W'|>=D/ell.                                            (7.1)
```

On any fixed-length interval `I` containing `J`, Markov's inequality gives

```text
sup_I |W'|<<M^2 sup_I |W|.                                   (7.2)
```

Therefore, if the spike is stable in the sense

```text
sup_I |W|<=C D,                                               (7.3)
```

then

```text
M>>_C ell^(-1/2).                                             (7.4)
```

For a prime-log gap at height `X`, (4.2) makes this

```text
M>>_C exp(kappa X/2).                                        (7.5)
```

At `X=c log T`, a stable spike already needs power-sized degree.  If the
degree is smaller, (7.2) says that the sup norm somewhere else must be much
larger than the hidden spike.  That is exactly the amplitude-conditioning
branch of (6.8).

Remez inequalities give the same qualitative conclusion for a spike hidden
on a union of tiny gaps: either the degree resolves the total exceptional
set, or the norm on the full interval is exponentially larger than the norm
on its complement.  They do not give an unconditional impossibility,
because an algebraic polynomial is allowed to have that enormous norm.
The relevant conclusion is the dichotomy, not a claim that interpolation
cannot be written down.

Weighted Laguerre Markov inequalities can replace (7.2) when the natural
norm is `L^2(e^(-delta x)dx)`.  Their constants grow linearly with degree;
see G. Nikolov and A. Shadrin,
[*Markov L2-inequality with the Laguerre weight*](https://arxiv.org/abs/1705.03824).
Combined with the cell proof of Theorem 6.1 they again turn the mesh factor
`exp(-kappa X)` into a degree-or-condition-number loss.  No choice of
`L^1`, `L^2`, or stable sup norm removes that loss.

## 8. Why a canonical product does not provide a finite-cost shortcut

There are already

```text
#(S intersect [0,R])>=pi(e^R) asyp e^R/R                    (8.1)
```

prime logarithms below `R`.  An entire function of finite exponential type
has only `O(R)` zeros in `|z|<=R`; more generally a finite-order entire
function has at most polynomially many zeros there.  Hence no nonzero
finite-type or finite-order canonical product can vanish at every point of
`S`.

In Beurling-density language, `S` has infinite upper density in the
logarithmic coordinate, whereas the real zeros of a nonzero Cartwright-class
function of finite exponential type have finite density.  Thus a
finite-bandwidth product cannot encode a prescribed zero at every prime
logarithm; allowing infinite bandwidth is the same non-tempered branch
already exposed by (6.7)--(6.8).

A product which installs a double zero at every prime logarithm, so that it
can be negative between essentially all of them while remaining
nonnegative on `S`, necessarily has infinite order.  It is then outside the
finite differential operator (2.1), and neither the prime Dirichlet series
nor the vertical decay in (2.8) follows.  Verifying (2.8) for such a product
is part of the problem, not a technical afterthought.

Finite interpolation up to `R` has the same count explicitly.  Installing
zeros or separate sign islands at a positive proportion of the prime logs
below `R` costs degree `>>e^R/R`.  Its Laplace tail and coefficient norm must
then be retained in (2.2)--(2.4).  Truncating the product before estimating
that tail is not a valid explicit-formula argument.

## 9. The scale comparison and the remaining superoscillatory escape

The vertical zero spacing at height `T` is of order `1/log T`.  For a kernel
with bounded first-moment condition number, a Fourier kernel

```text
H_W(u+iv)=integral_0^infinity W(x)e^(-u x)e^(-ivx)dx          (9.1)
```

acquires order-one phase separation on that spacing only from logarithmic
locations

```text
x asyp log T.                                                 (9.2)
```

This elementary uncertainty calculation is the general-weight version of
the R89 condition `m/delta asyp log T`.  An unbounded condition number can
superoscillate and is deliberately treated separately below.

For a continuously nonnegative weight, moving horizontally from `delta` to
`delta+e` attenuates mass at (9.2) by

```text
e^(-e x) asyp T^(-e).                                        (9.3)
```

Retaining a constant fraction forces `e log T=O(1)`, the R89 moving-strip
barrier.

Discrete positivity offers exactly one way not to pay (9.3): place a very
deep negative spike in a prime-log gap near `x asyp log T`.  Under the pole
weight it cancels positive mass; under the target weight it is attenuated by
`T^(-e)`.  Theorems 6.1--6.2 show the exact price:

```text
weighted variation or (degree x amplitude)
                         >>T^(19c/40)                         (9.4)
```

for a spike at `c log T`.

This does not create a contradiction by itself.  Exact algebra permits
power-sized and even much larger coefficients.  But all the other kernels
in (2.4) inherit the same superoscillatory weight.  Termwise absolute bounds,
ordinary zero density, and estimates with constants polynomial in the
weight norm are then much too expensive.  A survivor must prove a signed
joint estimate before taking absolute values.

Low-lying gaps do not pay (9.4), but their Fourier contribution varies only
on a fixed vertical scale.  Quantitatively,

```text
|H_W(u+i(v+h))-H_W(u+iv)|
 <=|h| integral_0^infinity x|W(x)|e^(-u x)dx.                 (9.5)
```

Thus a bounded first-moment condition number supported at `x=o(log T)`
cannot be the mechanism which distinguishes ordinates `1/log T` apart.
One may combine a low cancellation component with a high resolving
component, but then the high component again falls under (6.7)--(6.8).

The conclusion is deliberately narrower than an impossibility theorem:

```text
tempered discrete interpolation                         KILLED
finite-type canonical-product interpolation             KILLED
superoscillatory, target-conditioned interpolation      OPEN             (9.6)
```

## 10. Exact sufficient theorem for the surviving route

The open requirement can be stated without heuristic words.  Suppose
`rho_0=1-e+iT` is a nontrivial zero.  For a weight satisfying (2.1) and
(2.5), set `sigma=1+delta`, `A=H_W(delta+e)>0`, and define

```text
E_0(W)
 =-sum_rho H_W(sigma-rho)
  -sum_(j>=1)H_W(sigma+2j),                                  (10.1)

E_1(W;T,rho_0)
 = Re H_W(delta+iT)
   -sum_(rho!=rho_0) Re H_W(sigma+iT-rho)
   -sum_(j>=1) Re H_W(sigma+2j+iT).                           (10.2)
```

Zeros are counted with multiplicity; (10.2) removes one copy of `rho_0`.
Absolute convergence follows from Section 2.

### Theorem 10.1 (discrete-weight fixed-reserve criterion)

If there are constants `q,r>=0`, independent of `T`, such that

```text
H_W(delta)<=qA,

|E_0(W)+E_1(W;T,rho_0)|<=rA,

q+r<1,                                                        (10.3)
```

then the assumed zero `rho_0` cannot exist.

#### Proof

Apply (2.4) at `sigma` and `sigma+iT`, separating the one target copy.  The
exact identity is

```text
Q_W(sigma)+Re Q_W(sigma+iT)
 =H_W(delta)-A+E_0(W)+E_1(W;T,rho_0).                         (10.4)
```

The right side is negative by (10.3), while the left side is nonnegative by
(2.7).

### Corollary 10.2 (what would actually prove a fixed strip)

Fix `eta>0`.  If, for every sufficiently high putative zero with
`e=1-beta<eta`, one can choose `delta` and a discrete-positive `W` for which
(10.3) holds with one common margin `1-q-r>0`, then

```text
zeta(s)!=0       for Re s>1-eta'                              (10.5)
```

for some fixed `eta'>0`.  Indeed, compactness and the classical zero-free
line give a positive bounded-height gap, and one takes its minimum with
`eta`.  If the bounded range is separately verified to contain no zero with
`e<eta`, then one may take `eta'=eta`.  Uniformity is essential: weights
whose omitted constants grow with `T` do not establish (10.5).

The first line of (10.3) is precisely where discrete interpolation could
beat continuous Laplace domination.  The second line is the full signed
joint estimate that must survive the power-sized norm in (9.4).  Proving
only the first line is not progress to a strip if the second line is bounded
term by term.

## 11. Decision

The coefficient-specific loophole has been reduced to a sharp gate.

1. A polynomial weight is a finite differentiated explicit formula only
   when its constant term, vertical decay, and Laplace tail are accounted
   for as in Section 2.
2. Discrete nonnegativity genuinely permits negative intervals between
   prime powers, so continuous Laplace domination cannot simply be quoted.
3. Prime logarithms have mesh `<<exp(-19X/40)` at height `X`.
4. Fixed-reserve pole cancellation hidden above `X` forces either negative
   mass below `X`, variation `>>exp(19X/40)`, or degree times amplitude of
   that size.
5. At the resolving scale `X asyp log T`, every tempered interpolation is
   therefore impossible; a survivor is necessarily power-conditioned.
6. Many gaps, high-degree interpolation, Markov/Remez localization, and
   finite-type canonical products do not remove this price.
7. Arbitrary superoscillatory weights are not disproved.  Their required
   signed remainder estimate is exactly (10.3), and no such estimate is
   currently in the repository or in the imported literature.

Accordingly this branch has not proved a fixed zero-free strip and has not
proved that one cannot exist.  It has identified the only coefficient-
specific escape from the R89 pole-resolution wall: a power-conditioned
prime-gap interpolant together with a norm-uniform, target-conditioned
signed estimate for the complete zero remainder.
