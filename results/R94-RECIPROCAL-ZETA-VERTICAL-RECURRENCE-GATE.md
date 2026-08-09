# R94 reciprocal-zeta vertical-recurrence gate

## Status

The tempting contradiction does **not** follow from a fixed zero-free strip.
The precise obstruction is now theorem-level.

If

```text
zeta(s) != 0                    (Re(s)>theta),          (0.1)
```

for some `theta<1`, then the Mobius Dirichlet series for `1/zeta` does
converge compact-locally in that half-plane.  That convergence is not
uniform under vertical translation.  In fact its abscissa of uniform
convergence is exactly `1`, independently of (0.1).  Finite Mobius
polynomials can recur vertically near their phase at height zero, but the
conditional tail is then forced to anti-recur by an order-one amount on
every Rouche circle around the simple zero of `1/zeta` at `s=1`.

There is also a sharp normal-family formulation.  Along any sequence on
which every prime phase returns to `1`, the translated functions

```text
s -> 1/zeta(s+i tau_j)                                    (0.2)
```

cannot be locally bounded on a disc around `1` lying in the hypothetical
strip.  If they were, Montel, dominated convergence in `Re(s)>1`, the
identity theorem, and Hurwitz would copy the zero at `1` to a high zero of
`1/zeta`; but the only zero of `1/zeta` is the point corresponding to the
unique pole of zeta.

Thus this route gives neither a strip nor a proof that no strip exists.
It identifies the exact additional input which would prove the latter:
control the conditional Mobius tail on a prime-phase return sequence.  A
height-uniform tail estimate is more than unavailable--it is false by an
exact Kronecker sign-alignment theorem below.

## 1. The proposed contradiction

Write

```text
F(s)=1/zeta(s),
P_N(s)=sum_(n<=N) mu(n)n^(-s).                          (1.1)
```

At the pole of zeta,

```text
F(s)=(s-1)+O((s-1)^2),                                 (1.2)
```

so `F` has a simple zero at `1`.  Suppose (0.1), and give `F(1)` its
removable value zero.  Then `F` is holomorphic in `Re(s)>theta` and has no
other zero there.  Indeed zeros of the reciprocal are poles of zeta, and
zeta has only its simple pole at `1`.

The seductive argument is:

1. use (0.1) to continue the series in (1.1) left of `1`;
2. choose `tau` so that `n^(-i tau)` is close to `1` for the relevant
   integers;
3. infer `F(s+i tau)` is close to `F(s)` around `s=1`;
4. apply Rouche and obtain an impossible high zero of `F`.

Step 3 is invalid.  Step 1 supplies compact-local convergence for one
fixed vertical translate, whereas Step 3 needs convergence uniform in a
translate whose height is chosen only after the cutoff.

## 2. Exactly what a fixed strip gives

We use the standard zero-free-half-plane/Mertens equivalence already
imported and proved in the needed form in R90.  Under (0.1), for every
`alpha>theta`,

```text
M(x):=sum_(n<=x)mu(n) <<_alpha x^alpha.                 (2.1)
```

Conversely, one such fixed-power estimate continues `1/zeta` to the
corresponding half-plane.  The harmless epsilon between `theta` and
`alpha` absorbs possible boundary behavior.

Partial summation gives, whenever `Re(w)>alpha`,

```text
R_N(w):=F(w)-P_N(w)
 =-M(N)N^(-w)+w integral_N^infinity M(x)x^(-w-1)dx.    (2.2)
```

Consequently

```text
abs(R_N(w))
 <<_alpha [1+abs(w)/(Re(w)-alpha)]
             N^(alpha-Re(w)).                         (2.3)
```

For every fixed compact `K subset {Re(s)>theta}`, choose
`alpha<min_(s in K)Re(s)`.  Equation (2.3) proves

```text
P_N -> F                 uniformly on K.              (2.4)
```

This is the valid compact-local conclusion.

It is crucial that a translated compact is not fixed.  For bounded `s`
and arbitrary real `tau`, (2.3) becomes

```text
abs(R_N(s+i tau))
 <<_(K,alpha) (1+abs(tau))
                 N^(alpha-Re(s)).                     (2.5)
```

The factor `1+abs(tau)` comes from differentiating `x^(-i tau)` in
partial summation.  A fixed strip does not remove it.  Sections 5 and 6
show that some height dependence is logically compulsory: on phase-return
sequences the tails cannot even remain a locally bounded family.

## 3. The uniform-convergence abscissa is exactly one

The failure of height-uniform convergence can be made coefficient-exact.

**Theorem 3.1 (exact vertical sign alignment).**  For real `sigma` and
integers `1<=N<M`,

```text
sup_(t in R)
 abs(sum_(N<n<=M)mu(n)n^(-sigma-it))
 =sum_(N<n<=M)mu(n)^2 n^(-sigma).                     (3.1)
```

The same supremum is obtained as a limit along arbitrarily large values of
`abs(t)`.

### Proof

The upper bound is the triangle inequality.  The numbers `log p`, with
`p` ranging over the finitely many primes at most `M`, are linearly
independent over the rationals: an integer relation between them would be
a nontrivial equality between two prime factorizations.  Kronecker's
theorem therefore gives arbitrarily large `t` for which

```text
p^(-it) -> -1                 for every p<=M.          (3.2)
```

If `n` is squarefree, then

```text
n^(-it)=product_(p|n)p^(-it) -> (-1)^omega(n)=mu(n),  (3.3)
```

and hence

```text
mu(n)n^(-it) -> mu(n)^2.                              (3.4)
```

Nonsquarefree integers have Mobius coefficient zero.  The finite sum in
(3.1) therefore tends to its triangle-inequality upper bound.  QED.

Let `sigma_u` denote the abscissa of uniform convergence of the Mobius
Dirichlet series.  Since squarefree integers have density `6/pi^2`, partial
summation gives, for fixed `sigma<1`,

```text
sum_(N<n<=2N)mu(n)^2n^(-sigma) asymp_sigma N^(1-sigma), (3.5)
```

while at `sigma=1`,

```text
sum_(N<n<=2N)mu(n)^2/n -> (6/pi^2)log 2.              (3.6)
```

The uniform Cauchy criterion and (3.1) rule out uniform convergence on
every line `Re(s)=sigma<=1`.  Absolute convergence gives uniform
convergence in every half-plane `Re(s)>=1+epsilon`.  Therefore

```text
sigma_u=1.                                             (3.7)
```

This statement is unconditional.  Even if a fixed zero-free strip exists,
the value at `t=0` can enjoy the power cancellation (2.1) while a suitable
vertical phase turns every nonzero summand in the same finite block
positive.  In particular, ordinary convergence of
`sum mu(n)/n=0` at `s=1` does not come close to uniform convergence on the
line `Re(s)=1`.

There is a second terminology trap here.  A normally convergent series of
holomorphic functions is absolutely and uniformly convergent on compacta.
For the Mobius series this would require, on a compact reaching
`Re(s)=sigma`, convergence of

```text
sum_n abs(mu(n))n^(-sigma)=sum_n mu(n)^2n^(-sigma),    (3.8)
```

which also stops exactly at `sigma=1`.  The compact-local convergence in
(2.4) is conditional, not normal convergence in this sense.

## 4. Finite heads do recur

The failure is not in the finite-dimensional Kronecker step.

**Lemma 4.1 (diagonal prime-phase returns).**  There are
`tau_j->infinity` such that

```text
p^(-i tau_j)->1                      for every prime p. (4.1)
```

Consequently, for every fixed `N`,

```text
P_N(s+i tau_j)->P_N(s)                               (4.2)
```

uniformly on compact `s`-sets.

### Proof

For the first `j` primes, apply Kronecker recurrence with error `1/j` and
choose a return larger than `j`.  A diagonal choice gives (4.1).  Every
fixed integer is a product of finitely many fixed primes, so (4.2) follows
term by term in a finite sum.  QED.

The invalid interchange is now visible:

```text
first N->infinity, then choose a return for that head       valid;
control the tail at the resulting, N-dependent height       missing. (4.3)
```

The return time supplied by a finite torus can be enormous as the number
of active primes and requested accuracy grow.  Estimate (2.5) deteriorates
at precisely that height.

## 5. Rouche forces exact tail anti-recurrence

Fix

```text
0<r<1-theta,
D_r={s:abs(s-1)<r},
C_r=boundary D_r.                                      (5.1)
```

Since `F` has exactly one simple zero in `D_r` and none on `C_r`, put

```text
m_r=min_(s in C_r)abs(F(s))>0.                         (5.2)
```

**Theorem 5.1 (nonrecurrence on the Rouche circle).**  If
`abs(tau)>r`, then

```text
max_(s in C_r)abs(F(s+i tau)-F(s)) >= m_r.             (5.3)
```

### Proof

The function `s -> F(s+i tau)` is holomorphic and zero-free on `D_r`.
Its only possible reciprocal-zeta zero would occur at
`s=1-i tau`, outside the disc.  If the left side of (5.3) were smaller
than `m_r`, Rouche's theorem would give `F(s+i tau)` the same number of
zeros in `D_r` as `F(s)`, namely one.  This is a contradiction.  QED.

Decompose both terms in (5.3) at a finite cutoff.  With

```text
H_N(tau)=max_(s in C_r)abs(P_N(s+i tau)-P_N(s)),        (5.4)
```

one can translate prime-phase accuracy directly into this norm.  If

```text
max_(p<=N)abs(p^(-i tau)-1)<=epsilon,                   (5.5)
```

then, for squarefree `n<=N`,

```text
abs(n^(-i tau)-1)<=omega(n)epsilon
                  <=epsilon log(N)/log(2).             (5.6)
```

Since `Re(s)>=1-r` on `C_r`, it follows that

```text
H_N(tau)<<_r epsilon N^r log N.                        (5.7)
```

Thus an accuracy `epsilon=o(N^(-r)/log N)` is sufficient to make the
finite head recur uniformly on this circle.  Kronecker supplies any fixed
finite accuracy, but does not supply it at the small height required by
the tail estimate below.

the triangle inequality gives the exact tail ledger

```text
max_(s in C_r)abs(R_N(s+i tau))
 >=m_r-H_N(tau)-max_(s in C_r)abs(R_N(s)).             (5.8)
```

Under the strip hypothesis the last term tends to zero.  Thus, for all
large `N`, every sufficiently accurate finite-head return satisfying

```text
H_N(tau)<=m_r/4                                        (5.9)
```

must obey

```text
max_(s in C_r)abs(R_N(s+i tau))>=m_r/2.               (5.10)
```

This is the missing cancellation mechanism in its most economical form:
the distant conditional tail must undo the recurring finite head by an
order-one amount.

There is also a useful quantitative compatibility check.  Choose

```text
theta<alpha<1-r,
d=1-r-alpha>0.                                        (5.11)
```

Combining (2.5) with (5.10) shows that every return satisfying (5.9), for
large `N`, has

```text
abs(tau) >= c_(r,alpha) N^d.                          (5.12)
```

Therefore a theorem producing accurate returns with
`tau=o(N^d)` would disprove the fixed-strip hypothesis.  Ordinary
simultaneous approximation gives nothing close to this growing-dimensional
requirement; its returns are typically vastly larger than any fixed power
of `N`.

## 6. The normal-family version

The same obstruction is even cleaner without choosing a cutoff.

**Theorem 6.1 (phase recurrence forces reciprocal nonnormality).**
Assume (0.1), choose `r` as in (5.1), and let `tau_j->infinity` satisfy
(4.1).  Then the family

```text
F_j(s)=F(s+i tau_j)                                    (6.1)
```

is not locally bounded, and hence is not a normal family, on `D_r`.

### Proof

Suppose it were locally bounded.  Montel's theorem would provide a
subsequence converging uniformly on compact subsets of `D_r` to a
holomorphic function `G`.

On the nonempty open set

```text
D_r intersect {Re(s)>1},                               (6.2)
```

the Dirichlet series is absolutely convergent.  Equation (4.1) and
dominated convergence therefore give, locally uniformly there,

```text
F(s+i tau_j)
 =sum_n mu(n)n^(-s)n^(-i tau_j)
 ->sum_n mu(n)n^(-s)=F(s).                             (6.3)
```

Hence `G=F` on (6.2), and the identity theorem gives `G=F` throughout
`D_r`.  But each `F_j` is zero-free on `D_r`, whereas `F` has a simple zero
at `1`.  Hurwitz's theorem says that a locally uniform limit of zero-free
holomorphic functions is either zero-free or identically zero.  Since
`F` is neither, this is impossible.  QED.

Thus a hypothetical fixed strip forces reciprocal-zeta spikes during every
full diagonal finite-prime return process.  More explicitly, local
boundedness fails somewhere in each such disc, so along a subsequence

```text
sup_(s in K)abs(1/zeta(s+i tau_j))->infinity            (6.4)
```

for some compact `K subset D_r`.  Equivalently, zeta takes arbitrarily
small nonzero values there.  Zero-freeness gives no uniform minimum
modulus, and Theorem 6.1 says that the required uniform minimum modulus is
incompatible with the phase recurrence inherited from `Re(s)>1`.

## 7. Growth and minimum modulus

A fixed horizontal distance from every zero gives only a height-dependent
minimum-modulus estimate.  Standard logarithmic-derivative estimates, or
integration of `zeta'/zeta` horizontally from `Re(s)=2`, give on every
smaller closed strip

```text
theta+delta<=Re(s)<=2,
abs(1/zeta(s)) <= (2+abs(Im(s)))^C_delta.               (7.1)
```

A coarser finite-order bound would already make the same point.  Polynomial
growth in height does not make the translates in (6.1) locally bounded.
It also does not let one pass from (6.3), where convergence has no useful
rate relative to `tau_j`, to compact convergence across the line
`Re(s)=1`.

By contrast, any one of the following would be strong enough for the
normal-family contradiction:

```text
sup_j sup_(s in K)abs(1/zeta(s+i tau_j))<infinity       (7.2)
```

for every compact `K subset D_r`; or a uniform lower bound

```text
inf_j inf_(s in K)abs(zeta(s+i tau_j))>0;               (7.3)
```

or a uniform local `L^p` bound for `1/zeta` on slightly larger discs,
which implies (7.2) by the analytic mean-value inequality.  None follows
from absence of zeros.  Theorem 6.1 actually proves that, under the strip
hypothesis, such a bound must fail.

## 8. Topology ledger

```text
notion                              under a fixed strip       copies F(1)=0?
compact-local conditional series   yes, by (2.1)--(2.4)       no
normal/absolute series convergence only for Re(s)>1          yes where valid
uniform vertical convergence       abscissa exactly 1        yes where valid
Bohr uniform almost periodicity    only right of sigma_u=1    yes
Besicovitch/mean recurrence         may ignore sparse spikes   no point control
Montel normality of return shifts   forced to fail by Thm 6.1 yes
polynomial height growth           compatible with failure    no
```

Theorem 6.2 of R91 and Theorem 7.1 of R92 copy a pole-cancelling zero
because their coefficient hypotheses provide normal convergence to the
left of `1`.  The conditional multiplier

```text
sum_n mu(n)n^(-s)=1/zeta(s)                            (8.1)
```

is exactly outside that class.  Treating compact-local convergence as if
it were normal convergence erases the load-bearing distinction.

## 9. Minimal sufficient theorems

The least padded version of the missing result is the following.

**Theorem 9.1 (recurrence-tail criterion for no fixed strip).**  Suppose
(0.1), and choose `r` as in (5.1).  If there are `N_j->infinity` and
`tau_j->infinity` such that

```text
max_(s in C_r)
 abs(P_(N_j)(s+i tau_j)-P_(N_j)(s)) ->0,               (9.1)

max_(s in C_r)
 abs(F(s+i tau_j)-P_(N_j)(s+i tau_j)) ->0,             (9.2)
```

then (0.1) is false.

### Proof

The unshifted tail tends to zero by compact-local convergence.  Equations
(9.1)--(9.2) would make `F(s+i tau_j)->F(s)` uniformly on `C_r`, violating
Theorem 5.1; equivalently, Rouche would create a zero of the translated
reciprocal in `D_r`.  QED.

Condition (9.1) is finite-dimensional and follows from sufficiently
accurate prime-phase recurrence.  Condition (9.2) is the entire hard
problem.  Useful equivalent or stronger targets are:

1. prove (9.2) along one diagonal prime-phase return sequence;
2. prove local boundedness (7.2) along such a sequence, allowing Montel to
   replace the explicit tail estimate;
3. for `d` in (5.11), prove returns satisfying (5.9) with
   `tau=o(N^d)`, so the existing estimate (2.5) gives (9.2);
4. prove a zeta-specific twisted-tail estimate which is small at the
   positive-phase returns, not uniformly over all twists.

A bound uniform over every `tau` is not an admissible target: Theorem 3.1
falsifies it before any zero theory enters.  The needed estimate must be
conditioned specifically on near-`+1` prime phases and must retain the
growing tail rather than treating it independently.

## 10. Disposition

The proposed shortcut is closed:

```text
fixed strip
 -> power Mertens bound
 -> compact-local convergence of sum mu(n)n^(-s)       VALID

compact-local convergence
 -> vertical Bohr recurrence around s=1                FALSE
```

What survives is a rigorous no-strip attack surface.  Under a fixed strip,
every accurate return of the finite Mobius head forces an order-one
conditional-tail correction, and diagonal prime-phase returns force
`1/zeta` to be nonnormal and arbitrarily large somewhere near the
translated pole disc.  Proving that the actual Mobius tail cannot sustain
that correction would prove that no fixed zero-free strip exists.  No
known estimate in the repository controls this recurrence-conditioned
tail, and ordinary Mertens bounds, minimum-modulus bounds with polynomial
height loss, or mean-square almost periodicity do not do so.

No fixed-strip or no-fixed-strip theorem is claimed here.
