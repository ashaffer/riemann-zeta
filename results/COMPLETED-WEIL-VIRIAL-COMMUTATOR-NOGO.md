# Completed-Weil virial commutator: derivation and fail-fast verdict

Status: the spectral-projection Mourre test and geometric dilation are pruned.
The same conclusion for the real transport class `G_v` follows from the
localized high-frequency commutator asymptotic displayed in Section 4; that
standard pseudodifferential step is presently a referee-facing proof
obligation rather than a Lean theorem.  Other local generators, a genuinely
nonlocal mixed estimate, or a singular generator with its full boundary
defect retained are not ruled out.  The singular survivor is a
boundary/collar inequality rather than an ordinary positive-commutator
argument.

## 1. The operator and its form domain

Write `H_a=L2([-a,a])`, using zero extension to the real line, and use angular
Fourier frequency `r=2*pi*xi`.  On its logarithmically weighted form domain,
the arithmetic Weil form is

```text
Q_a(f) = pole_a(f)
       + integral m_arch(r) |fhat(r)|^2 dr/(2*pi)
       - sum_(log n < 2a) c_n Corr_(log n)(f),

m_arch(r) = Re psi(1/4 + i r/2) - log pi,
c_n       = 2 Lambda(n)/sqrt(n).
```

Equivalently, apart from the rank-two pole term, the completed multiplier is

```text
m_a(r) = m_arch(r) - sum_(log n < 2a) c_n cos(r log n).
```

This is exactly the normalization in
[`GeneralZetaWeilForm.lean`](../lean/rhbridge/RHBridge/GeneralZetaWeilForm.lean).
At the analytic layer, the closed-form representation theorem supplies an
associated lower-semibounded self-adjoint operator with compact resolvent.  That
unbounded operator is not constructed in `GeneralZetaWeilForm.lean`.  There
is no Dirichlet or Neumann boundary condition: sharp support is imposed by
zero extension.

That distinction is decisive.  `C_c^infty((-a,a))` is a form core, but a
geometric dilation need not preserve the operator domain of the sharp-support
realization.

## 2. The completed first-order form commutator

Let

```text
G_v f = v f' + v' f/2,
R_u(f) = integral f(x) f(x+u) dx,
f_s = exp(s G_v) f.
```

For a smooth real vector on the interior core, direct differentiation and
one integration by parts give

```text
dot R_(u,v)(f)
 = d/ds R_u(f_s)|_(s=0)
 = integral f(x) [
       (v(x+u)-v(x)) f'(x+u)
       + (v'(x+u)-v'(x)) f(x+u)/2
   ] dx.
```

Write `l_+=l_(1/2)` and `l_-=l_(-1/2)`.  The completed commutator form

```text
C_(a,v)(f) = d/ds Q_a(f_s)|_(s=0)
```

then separates exactly as

```text
C_pole
 = -l_- integral (v+v') f exp(x/2) dx
   -l_+ integral (v'-v) f exp(-x/2) dx,

C_arch
 = -integral_(0,infinity)
      [2 exp(-u/2)/(1-exp(-2u))] dot R_(u,v)(f) du,

C_prime
 = -sum_(log n<2a) c_n dot R_(log n,v)(f),

C_(a,v) = C_pole+C_arch+C_prime.
```

The archimedean line follows from the Gauss/digamma difference-kernel
representation; its norm-only constant has zero derivative under this
unitary flow.  The last line uses `c_n=2 Lambda(n)/sqrt(n)`, fixing the factor
and sign relative to Section 1.  If `D_v=-iG_v`, this derivative is the form
of the usual self-adjoint commutator `i[A_a,D_v]` whenever the operator-domain
products exist.

### Geometric dilation

On a smooth vector supported strictly inside the interval, set

```text
(U_t f)(x) = exp(t/2) f(exp(t)x).
```

Then

```text
Fourier(U_t f)(r) = exp(-t/2) fhat(exp(-t)r),
```

so differentiation at zero gives the exact multiplier contribution

```text
C_dil,a(f) = integral r m_a'(r) |fhat(r)|^2 dr/(2*pi)
             + differentiated pole term,

r m_a'(r)
  = r tau_(1/4)(r)
    + sum_(log n < 2a) c_n (log n) r sin(r log n),
```

where `tau_(1/4)` is the positive trigamma slope.  Its positive series is
formalized in `Glide.DigammaMonotone`, and its unconditional identification
with the derivative is completed in `Glide.GammaUniformQuarter`.

If

```text
l_s(f) = integral f(x) exp(sx) dx,
j_s(f) = integral x f(x) exp(sx) dx,
```

the differentiated pole term is

```text
-2 l_(1/2)(f) l_(-1/2)(f)
-  j_(1/2)(f) l_(-1/2)(f)
+  l_(1/2)(f) j_(-1/2)(f).
```

### Exact high-frequency obstruction

Already in the certified prime-2 window, let

```text
A = sqrt(2) log 2,
u_2 = log 2,
r_k = (3*pi/2 + 2*pi*k)/u_2.
```

At `r_k`, `sin(u_2 r_k)=-1` and `cos(u_2 r_k)=0`.  Standard digamma asymptotics
give

```text
r tau_(1/4)(r) = 1 + O(1/r),
m_arch(r)      = log |r| + O(1).
```

Consequently, for every fixed `kappa >= 0`, the multiplier of
`C_dil,a + kappa Q_a` satisfies

```text
r_k m_a'(r_k) + kappa m_a(r_k)
  = -A u_2 r_k + O(kappa log r_k + 1) -> -infinity.
```

Choose a nonnegative smooth interior bump `b` with
`R_(log 2)(b)>0`, and set `f_k(x)=b(x) cos(r_k x)`.  Stationary oscillatory
terms decay, while direct differentiation of the autocorrelation gives

```text
C_prime(f_k)
 = c_2 (log 2) r_k sin(r_k log 2) R_(log 2)(b)/2 + O(1).
```

The pole moments tend to zero and the archimedean contribution is `O(1)`
after normalization.  Thus these are genuine fixed-support form vectors, not
an appeal to pointwise multiplier negativity alone, and

> `C_dil,a + kappa Q_a` is not nonnegative on the smooth core for any fixed
> `kappa` in the prime-2-only window.

This kills the canonical global comparison that would infer positivity of
`Q_a` from a dilation commutator.  It does not claim that the Weil form is
negative.

The same conclusion holds at every fixed support having at least one active
prime power.  Because the active set is finite and every active shift is
strictly below `2a`, choose one nonnegative smooth interior bump `b` with
`R_(log n)(b)>0` for every active `n`.  List the underlying rational primes
as `p_1,...,p_d`, and let `K` be the largest active exponent.  Choose
`epsilon>0` with `K epsilon<pi/2` and target every phase `r log p_j` near
`2*pi-epsilon`.  Rational independence of the prime logarithms and Kronecker
approximation give an unbounded sequence of such `r`.  On a small fixed
target neighborhood,

```text
sin(r log(p_j^k)) = sin(k r log p_j) <= -delta < 0
```

for every active `p_j^k`, with one common `delta>0`.  Applied to
`b(x) cos(r x)`, the leading prime commutator is therefore at most `-B r` for
some `B>0`, while the archimedean commutator is `O(1)` and
`kappa Q_a=O(kappa log r)`.  This proves the same unbounded negative conclusion
for each fixed larger support; no cancellation from the additional active
prime powers repairs it.

There is also a finite-frequency symbol witness.  At `a=7/16`, where only
prime 2 is active, set

```text
r_0 = 3*pi/(2 log 2).
```

The archimedean slope obeys `r_0 tau_(1/4)(r_0)<4`, whereas the prime-2
contribution is exactly `-3*pi*log(2)/sqrt(2)`.  Hence

```text
r_0 m_a'(r_0) < 4 - 3*pi*log(2)/sqrt(2) < 0.
```

The bound is not a numerical fit: it follows from the positive derivative
series

```text
r tau_(1/4)(r)
 = (r^2/2) sum_(k>=0)
     (k+1/4)/(((k+1/4)^2+r^2/4)^2)
```

and a sum--integral estimate for its nonnegative unimodal summand.

The high-frequency sequence is still needed for the stronger conclusion
that adding any fixed multiple of `Q_a` cannot repair the sign.

## 3. Why a spectral Mourre estimate supplies no independent test

Let `A` be bounded below and self-adjoint with compact resolvent, and let `G`
be a regular conjugate operator whose commutator products are defined on the
eigenvectors under discussion.  If `A psi=lambda psi`, then

```text
<psi, [A,G] psi> = 0.
```

Therefore

```text
P_- i[A,G] P_- >= c P_-,        c>0,
P_- = 1_(-infinity,0](A),
```

can hold only when `P_-=0`.  For this bounded-below compact-resolvent operator,
this is not a numerically testable estimate on a near-null sector: every
actual eigenvector, positive or negative, has zero commutator expectation.
The estimate is a certificate that the forbidden spectral subspace is already
empty.

A Mourre estimate modulo a compact remainder is weaker still.  The lower
bound makes `(-infinity,0]` effectively a bounded spectral interval, so `P_-` has
finite rank.  An arbitrary discrepancy on that projection can therefore be
absorbed into the compact remainder.  Without semiboundedness, compact
resolvent alone would not make this half-line projection finite rank.

At finite dimension,

```text
trace([H,G])=0.
```

Hence a pure Galerkin commutator cannot be positive definite.  Lean proves the
eigenvector identity, trace obstruction, and the two-state leakage control in
[`VirialCommutatorNoGo.lean`](../lean/rhbridge/RHBridge/VirialCommutatorNoGo.lean).

There is also a domain-safe form version.  Let `V` be a Hilbert form domain,
let `j:V->H` be its continuous pivot embedding, put `J=j^*j`, and let `B` be
the bounded Hermitian Riesz representative of the form.  If

```text
B u = lambda J u,                 G^*J+JG=0,
```

then

```text
< (G^*B+BG)u,u >_V = 0.
```

This statement never asserts that `u` or `Gu` belongs to the operator domain
of the unbounded operator represented by the form.  It is Lean-checked in
[`FormDomainVirial.lean`](../lean/rhbridge/RHBridge/FormDomainVirial.lean).
It closes the regular bounded form-domain version of the proposed shortcut;
an unbounded or singular support-moving generator remains outside its scope.

## 4. Compression and the boundary defect

For an idempotent projection `P` and `R=I-P`, exact algebra gives

```text
P[H,X]P = [PHP,PXP] + PHRXP - PXRHP.
```

The internal commutator has trace zero.  Any apparent positive compressed
trace comes from the two off-block leakage terms and is balanced outside the
compression.  The Lean control

```text
H = [[0,1],[1,0]],       X = (1/2)[[0,-1],[1,0]]
```

has

```text
[H,X] = diag(1,-1).
```

Keeping only the first coordinate manufactures positivity by discarding the
compensating negative boundary channel.

The infinite-dimensional prototype is the Dirichlet Laplacian.  Formal
dilation says `i[H,G]=2H`, but dilation does not preserve the Dirichlet
operator domain.  On an eigenfunction, the omitted endpoint flux is exactly
the negative of the displayed bulk expectation, restoring the virial identity.

Nor do boundary-preserving first-order fields give a global escape.  Let

```text
G_v = v(x) d/dx + v'(x)/2,             v in C-infinity,
v(-a)=v(a)=0.
```

This is the skew first-order generator of a unitary flow preserving the fixed
interval.  If `v` is nonzero, then `integral v'=0`, so `v'<0` on some open
subinterval.  Choose a smooth bump `h` there whose support has width less than
`log 2`, and modulate it at frequency `T`.  All prime correlations, including
their differentiated terms, vanish identically because every prime shift is
at least `log 2`.  The differentiated pole moments tend to zero.  The required
localized high-frequency commutator lemma for the digamma multiplier gives,
after normalizing the packet,

```text
C_arch(h exp(i T x)) ->
  (integral v'(x) |h(x)|^2 dx) / (integral |h(x)|^2 dx) < 0.
```

The same conclusion follows with real cosine packets.  Subject to that
asymptotic lemma, every nonzero real transport generator of the displayed
form whose flow preserves the interval has negative completed commutator
directions at high frequency.  The prime-support and pole-limit reductions
are explicit above; a self-contained proof still has to state the symbol
class, uniform remainder, and form-domain passage for the archimedean lemma.
Accordingly this transport conclusion is Amber and is not among the finite
algebraic claims checked by Lean.

This leaves genuinely nonlocal generators, as well as singular or
support-moving generators with their full boundary/collar defect retained.

## 5. Prime-5 diagnostic

The reproducible finite diagnostic uses the Legendre Weil matrix `Q`, the
coordinate matrix `X`, and the velocity-adapted construction

```text
V = i[Q,X],
D = (XV+VX)/2,
C = i[Q,D].
```

For a positive finite matrix, define

```text
kappa_crit = max(0, -lambda_min(Q^(-1/2) C Q^(-1/2))).
```

It is the least scalar making `C+kappa Q` positive semidefinite, conditional
on the already observed strict positivity of `Q`.  The meaningful strict
statement

```text
there exists kappa>0 with C+kappa Q positive definite
```

is equivalent in finite dimension to `Q` being positive definite: test the
forward implication on a `Q`-eigenvector and use the virial identity.  Merely
allowing a semidefinite repair at `kappa=0` would not be equivalent.

At program support `L=3.27`, where prime 5 has just activated, the results are

| modes | Galerkin minimum | maximum eigenstate commutator diagonal | `kappa_crit` |
|---:|---:|---:|---:|
| 12 | `5.83e-9` | `1.67e-16` | `1.90e1` |
| 16 | `5.53e-11` | `2.01e-16` | `4.58e2` |
| 20 | `1.39e-12` | `1.50e-16` | `2.27e3` |
| 24 | `1.81e-14` | `1.93e-16` | `3.42e4` |

The commutator diagonal is zero up to floating error, exactly as the theorem
requires.  The scalar repair deteriorates rapidly with refinement rather than
revealing an independent gap.  The complete table is
[`virial-commutator-prime5.csv`](virial-commutator-prime5.csv), generated by
[`virial_commutator_falsifier.py`](../src/virial_commutator_falsifier.py).
The CSV records the analytically exact trace as zero; direct floating
evaluation leaves residuals of order `1e-17`.

## 6. Verdict and explicit survivors

Pruned:

- a regular strict Mourre estimate treated as an independently testable
  low-sector inequality;
- a positive finite Galerkin matrix made only from a commutator;
- geometric dilation plus any fixed nonnegative multiple of the Weil form,
  once at least one prime power is active;
- subject to the localized pseudodifferential lemma in Section 4, every
  nonzero real transport generator `G_v=v d/dx+v'/2` whose flow preserves the
  fixed support interval;
- dropping the compression or support-boundary leakage term;
- a Mourre estimate whose arbitrary compact remainder absorbs the entire
  finite-rank spectral question.

Not pruned:

> A genuinely nonlocal conjugate operator entering a new global mixed
> inequality; a regular local generator outside the displayed real transport
> class; completion of the localized archimedean packet lemma if the
> transport claim is to be used as a theorem; or a singular/support-moving
> operator whose exact boundary defect is retained and whose completed
> prime--archimedean--pole flux has a zeta-specific sign.

The singular/support-moving survivor is not an ordinary positive-commutator
shortcut.  It is the boundary-flux/collar problem in a new coordinate.  The
previous boundary-jump and Hodge falsifiers therefore apply to it immediately;
any revival must first show precisely which hypothesis of those
counterexamples it escapes.

No statement here proves or disproves RH, or proves that every conceivable
commutator method must fail.

## 7. Evidence boundary

The new Lean module proves only the finite/eigenvector algebra in Sections 3
and 4.  Operator existence, compact resolvent, smooth form-core density,
differentiation under the digamma-kernel integral, and the Kronecker
realization are analytic inputs or arguments, not consequences of
`GeneralZetaWeilForm.lean`; they require conventional referee review.  The
transport packet asymptotic additionally needs the explicit symbol/remainder
lemma named in Section 4 and remains Amber rather than A-rated.
