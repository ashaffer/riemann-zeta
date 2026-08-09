# The q-free ratio and the nonvanishing gate

Status: R90 exact q-free counting theorem, Mellin continuation, uniform
comparison theorem, height-dependent-`q` no-go, smoothing no-go, product
and ratio algebra, and summable logarithmic-positivity no-go.  The q-free
asymptotic gives an arbitrarily small fixed-power counting error, but zeros
are not singularities of a Dirichlet series.  In every fixed half-plane
`Re(s)>=sigma_0>1/2`, the q-free transform is just zeta times a uniformly
bounded and uniformly nonvanishing factor, for every `q>=2`.  Consequently
this route neither proves a fixed zero-free strip nor proves that no such
strip exists.

## 1. Verdict

For an integer `q>=2`, let

```text
a_q(n)=1_(n is q-free),
Q_q(x)=sum_(n<=x) a_q(n),
F_q(s)=sum_(n>=1) a_q(n)n^(-s).                              (1.1)
```

The attractive input is genuinely strong:

```text
Q_q(x)=x/zeta(q)+O(x^(1/q)),                                (1.2)
```

with an absolute implied constant that can be taken uniformly in `q`.
Nevertheless the exact Euler identity is

```text
F_q(s)=zeta(s)/zeta(qs).                                    (1.3)
```

In the region relevant to a fixed strip, `zeta(qs)` is already represented
by an absolutely convergent, nonzero Euler product.  It cannot cancel or
move a zero of `zeta(s)`.  More quantitatively, for every `sigma_0>1/2`,
every `q>=2`, and every `s` with `Re(s)>=sigma_0`,

```text
 |zeta(s)|/zeta(2sigma_0)
     <= |F_q(s)|
     <= [zeta(2sigma_0)/zeta(4sigma_0)] |zeta(s)|.           (1.4)
```

The constants do not depend on `q` or `Im(s)`.  Thus even a choice
`q=q(Im(s))` leaves exactly the same zero and near-zero obstruction.

```text
q-free fixed-power count                       EXACT
constant uniform in q                          EXACT
Mellin continuation to Re(s)>1/q               EXACT
height-uniform upper control                    O(|s|), not a lower bound
target zeros in Re(s)>1/2                       unchanged, same multiplicity
q depending on height                          no change, by (1.4)
positive q-free coefficients                   valid only before centering
finite q-products and q-ratios                  algebraically circular
summable logarithmic-positivity repair           impossible with target power
constant lower bound on 1/2<sigma<1             false by universality
fixed zero-free strip                           NOT PROVED.              (1.5)
nonexistence of a fixed zero-free strip         NOT PROVED.
```

The useful conclusion is a hard gate: q-free sparsification changes only
absolutely convergent prime-power harmonics.  A successor must control the
common first-prime harmonic, or an equivalent cross-prime phase statistic.

## 2. Exact counting and a uniform error

The elementary identity

```text
a_q(n)=sum_(d^q|n) mu(d)                                      (2.1)
```

gives, with `y=x^(1/q)`,

```text
Q_q(x)=sum_(d<=y) mu(d) floor(x/d^q).                         (2.2)
```

Subtracting `x sum_(d>=1)mu(d)/d^q=x/zeta(q)` and taking
absolute values yields

```text
|Q_q(x)-x/zeta(q)|
 <= y+x sum_(d>y)d^(-q)
 <= [1+1/(q-1)]x^(1/q)
 <= 2x^(1/q),                                  x>=1.          (2.3)
```

No cancellation in `mu` was used.  In particular, the constant in (2.3)
is uniform for every integer `q>=2`.

There is an exact Bernoulli-sawtooth version.  If

```text
psi(u)=floor(u)-u,
```

then the absolutely convergent tail interpretation gives

```text
Q_q(x)-x/zeta(q)=sum_(d>=1)mu(d)psi(x/d^q).                   (2.4)
```

For `d>x^(1/q)`, the summand is `-mu(d)x/d^q`.  Formula (2.4)
shows what the small error contains: it is a signed superposition of
discontinuous lattice phases, not a smooth positive remainder.

For `Re(s)>1`, (2.1) and absolute convergence give

```text
F_q(s)
 =sum_d mu(d)d^(-qs) sum_m m^(-s)
 =zeta(s)/zeta(qs).                                          (2.5)
```

On the other hand, Stieltjes integration gives

```text
F_q(s)=s integral_1^infinity Q_q(x)x^(-s-1) dx.               (2.6)
```

Writing `E_q(x)=Q_q(x)-x/zeta(q)`, (2.3) continues (2.6) to
the exact formula

```text
F_q(s)=s/[zeta(q)(s-1)]+H_q(s),
H_q(s)=s integral_1^infinity E_q(x)x^(-s-1) dx,               (2.7)
```

where `H_q` is holomorphic in `Re(s)>1/q` and

```text
|H_q(s)|<=2|s|/[Re(s)-1/q].                                  (2.8)
```

This is the precise payoff of the fixed-power count: analytic continuation
with polynomial vertical growth.  It is not a nonvanishing theorem.
For `|Im(s)|` large the pole term in (2.7) has size comparable to one,
whereas (2.8) grows linearly with height.  It cannot make the pole term
dominate.  More decisively, if `rho` is a zeta zero with `Re(rho)>1/q`,
then (2.5)--(2.7) force

```text
H_q(rho)=-rho/[zeta(q)(rho-1)].                              (2.9)
```

Thus the signed counting error is fully capable of cancelling the main
term at every target zero.  Bound (2.3) does not see that phase.

This is not a defect of the exponent `1/q`.  Letting `q` be arbitrarily
large makes the exponent arbitrarily small while leaving every zero of
zeta in place.  At the limiting extreme, the ordinary integer count
`floor(x)=x+O(1)` has Dirichlet series `zeta(s)` itself.  Summatory accuracy
controls poles and other singularities; a zero is not a singularity.

## 3. The uniform comparison theorem

We record the main fail-fast theorem.

**Theorem 3.1 (uniform q-free equivalence).**  Fix `sigma_0>1/2`.
For every integer `q>=2` and every `s=sigma+it`, `s!=1`, with
`sigma>=sigma_0`, the bounds (1.4) hold.  In particular,

```text
F_q(s)=0  iff  zeta(s)=0,                                    (3.1)
```

with equality of zero multiplicities.  Both assertions remain uniform if
`q` is chosen as an arbitrary function of `s`.

**Proof.**  For `a>1`, the absolutely convergent Euler product gives

```text
zeta(2a)/zeta(a) <= |zeta(a+ib)| <= zeta(a).                  (3.2)
```

The upper bound follows from `|1-p^(-a-ib)|>=1-p^(-a)`.  The
lower bound follows from `|1-p^(-a-ib)|<=1+p^(-a)` and

```text
product_p (1+p^(-a))^(-1)=zeta(2a)/zeta(a).                  (3.3)
```

Apply (3.2) with `a=q sigma>1`.  Since

```text
zeta(a) <= zeta(2sigma_0),
zeta(a)/zeta(2a)=product_p(1+p^(-a))
                <= zeta(2sigma_0)/zeta(4sigma_0),            (3.4)
```

division in (2.5) proves (1.4).  The denominator has no zero or
pole for `Re(qs)>1`, so (3.1), including multiplicity, follows.  All
constants used only the lower bound `q sigma>=2sigma_0`.  QED.

For any proposed fixed strip narrower than `1/2` (as may always be assumed
when asking only for existence), Theorem 3.1 says exactly

```text
F_q nonzero in Re(s)>1-eta
  iff
zeta nonzero in Re(s)>1-eta.                                 (3.5)
```

This is a clean equivalence, not a new route around the endpoint.

There is also a quantitative warning about the phrase “uniform lower
bound.”  For every fixed `sigma` with `1/2<sigma<1`, the classical
universality theorem implies that `zeta(sigma+it)` comes arbitrarily close
to zero as `t` varies.  Hence (1.4) gives, for every choice rule
`q(t)>=2`,

```text
inf_t |F_(q(t))(sigma+it)|=0.                                (3.6)
```

This statement is unconditional and is compatible with a zero-free
vertical line: a nonvanishing analytic function may have infimum zero.
Therefore a positive constant lower bound is too strong.  A valid
nonvanishing proof would need a height-dependent lower bound or a topological
argument which cannot be extracted from (2.3).

## 4. Why taking q large restores zeta rather than simplifying it

The first forbidden q-th power is `2^q`.  Consequently

```text
a_q(n)=1 and Q_q(x)=floor(x),              1<=x<2^q.          (4.1)
```

Thus a growing `q` agrees with the full integer staircase on an
exponentially growing initial range.  On the analytic side, for `a>1`,

```text
|1/zeta(a+ib)-1|
 <= sum_(n>=2)|mu(n)|n^(-a)
 <= zeta(a)-1
 <= 2^(-a)[1+2/(a-1)].                                      (4.2)
```

It follows uniformly in height that

```text
F_q(s)=zeta(s){1+O(2^(-q sigma)[1+1/(q sigma-1)])}.           (4.3)
```

So choosing `q` proportional to `log |t|` merely makes the q-free factor
polynomially close to zeta.  It pushes the first coefficient modification
past a power of the analytic conductor while retaining the full target
phase.  The small exponent in (2.3) and the closeness in (4.3) point in
opposite directions for nonvanishing: the stronger-looking count is
obtained by removing less and less of zeta.

## 5. Smoothing does not turn the upper estimate into a lower estimate

Let `W` be continuously differentiable and compactly supported in
`(0,infinity)`.  Partial summation in (2.3) gives

```text
S_q(X,t)
 :=sum_n a_q(n)W(n/X)n^(-it)

 =X^(1-it)/zeta(q) integral_0^infinity W(u)u^(-it)du
  +O_W((1+|t|)X^(1/q)).                                     (5.1)
```

Indeed, write the Stieltjes integral against
`dQ_q=dx/zeta(q)+dE_q`; differentiating
`W(x/X)x^(-it)` costs `X^(-1)+|t|x^(-1)` on the support of
`W`, while `E_q(x)=O(x^(1/q))`.

For a smooth `W`, repeated integration by parts in logarithmic coordinates
makes the main Mellin factor in (5.1) decay rapidly with `|t|`.  The
available error estimate instead pays derivatives of the oscillatory
factor.  Smoothing therefore worsens, rather than repairs, main-term
dominance at high frequency.

One can choose a height-dependent kernel

```text
W_t(u)=W(u)u^(it),                                           (5.2)
```

to eliminate that derivative loss.  But then

```text
W_t(n/X)n^(-it)=X^(-it)W(n/X),                               (5.3)
```

so the same operation eliminates the spectral probe.  This is the exact
uncertainty gate: a kernel matched strongly enough to recover the positive
counting main term has demodulated away the target ordinate.

More elaborate Riesz or Laplace smoothing does not change the algebraic
issue.  After subtraction of the density term, the measure is `dE_q`,
which is signed.  Before subtraction it is positive, but the transform is
only absolutely normalizable in `Re(s)>1`, where Euler products already
prove nonvanishing.

## 6. Ratios, products, and averages across q

The q-free ratios obey the exact semigroup law

```text
F_m(s)F_n(ms)=F_(mn)(s).                                    (6.1)
```

It is just the telescoping identity

```text
[zeta(s)/zeta(ms)][zeta(ms)/zeta(mns)]
   =zeta(s)/zeta(mns).                                      (6.2)
```

Likewise,

```text
F_q(s)/F_r(s)=zeta(rs)/zeta(qs).                             (6.3)
```

In `Re(s)>1/2`, the right side of (6.3) is automatically nonzero.  The
ratio has cancelled the target factor and therefore contains no information
about its zeros.

For a finite family and integer exponents `c_j`, put

```text
G(s)=product_(j=1)^J F_(q_j)(s)^(c_j),
C=sum_j c_j.                                                 (6.4)
```

Then

```text
G(s)=zeta(s)^C product_j zeta(q_j s)^(-c_j).                 (6.5)
```

Throughout `Re(s)>1/2`, the second factor is holomorphic and nonzero.
If `C=0`, the construction has removed zeta and is automatically nonzero.
If `C!=0`, it retains exactly `C` times the zeta divisor (zeros for
`C>0`, poles for `C<0`).  Products cannot occupy an intermediate case.

Positive linear averages do not evade the common factor either.  If
`w_j>=0`, then

```text
A(s)=sum_j w_jF_(q_j)(s)
    =zeta(s) sum_j w_j/zeta(q_j s).                          (6.6)
```

For `q_j>=Q` and `Re(s)>=sigma_0>1/2`, choose `Q` so large that
`zeta(Q sigma_0)-1<1`.  Formula (4.2) then shows that the second factor in
(6.6) lies in the open disk centered at `sum_jw_j` with radius smaller
than that center.  It is nonzero.  At the same time `A` has nonnegative
Dirichlet coefficients and its summatory function satisfies

```text
sum_(n<=x) sum_j w_j a_(q_j)(n)
 =x sum_j w_j/zeta(q_j)+O((sum_jw_j)x^(1/Q)).                (6.7)
```

Thus one can manufacture a positive-coefficient series with an arbitrarily
small counting-error exponent whose zeros in the target half-plane are
*exactly* the zeta zeros.  This directly falsifies any proposed implication
from positive coefficients plus (6.7) to nonvanishing.

## 7. The Bernoulli Euler structure and its positivity limit

For one prime, with `z=p^(-s)`,

```text
1+z+...+z^(q-1)=(1-z^q)/(1-z).                              (7.1)
```

Every local zero lies on `|z|=1`, so every local factor is nonzero for
`Re(s)>0`.  Its logarithm is

```text
log[(1-z^q)/(1-z)]
 =sum_(m>=1) [1-q 1_(q|m)] z^m/m.                           (7.2)
```

The coefficient of the first harmonic `z` is exactly `1`, independently
of `q`.  All q-specific changes start at harmonic `q`.  Initially in
`Re(s)>1`, and then locally by continuation away from the divisor, one has

```text
log F_q(s)=log zeta(s)-log zeta(qs),                         (7.3)
```

and the second term has an absolutely convergent Euler expansion whenever
`q Re(s)>1`.  The common first-prime harmonic is precisely the part whose
conditional continuation carries the zeta divisor.

There is a positivity no-go hidden in (7.2).  First let

```text
G(s)=product_(q in S)F_q(s)^(c_q),
C=sum_(q in S)c_q,                                          (7.4)
```

where `S` is finite and the `c_q` are real.  The coefficient of
`p^(-ms)/m` in the local logarithm is

```text
B(m)=C-sum_(q in S,q|m)q c_q.                               (7.5)
```

Suppose one tries to prove nonvanishing by making every `B(m)>=0`, so that
the logarithm has a positive prime-power exponential measure.  The function
`B(m)` is periodic modulo `lcm(S)`, and its mean over a period is

```text
mean B=C-sum_q q c_q(1/q)=C-sum_q c_q=0.                    (7.6)
```

If all `B(m)` are nonnegative, (7.6) forces all of them to vanish.  But
`B(1)=C`.  Hence

```text
B(m)>=0 for every m  ==>  C=0.                              (7.7)
```

Every finite logarithmically positive combination therefore deletes the
target zeta power.  This closes the natural infinite-divisibility/Euler-
exponential certificate.  It is not asserted that logarithmic coefficient
positivity is necessary for every conceivable positive-definiteness
argument.

The same conclusion holds for every normally summable infinite product.
Suppose

```text
sum_(q>=2)q|c_q|<infinity,       C=sum_(q>=2)c_q,             (7.8)
```

and define `B(m)` by the convergent version of (7.5).  Its Cesaro mean is
again zero, since dominated convergence gives

```text
lim_(N->infinity) (1/N)sum_(m<=N)B(m)
 =C-sum_q q c_q(1/q)=0.                                    (7.9)
```

If `B(m)>=0`, then `C=B(1)>=0`.  Were `C>0`, choose a finite set
`S` with

```text
sum_(q notin S)q|c_q|<C/4
```

and put `L=lcm(S)`.  On every progression point `m=1 mod L`, no
`q in S` divides `m`, and hence

```text
B(m)>=C-sum_(q notin S)q|c_q|>3C/4.                         (7.10)
```

This positive-density progression contradicts the zero mean (7.9), because
all other values are nonnegative.  Therefore `C=0`.  Any infinite product
outside the summability condition must use conditionally convergent weights;
then rearrangement, branch, and uniform-convergence issues become part of
the desired theorem rather than a positivity shortcut.

For completeness, ordinary positive definiteness is available in the
wrong half-plane.  When `sigma>1`,

```text
F_q(sigma+it)/F_q(sigma)
```

is the characteristic function of the probability distribution assigning
mass proportional to `a_q(n)n^(-sigma)` at `log n`.  Equivalently, the
prime exponents are independent truncated geometric random variables.
The normalization diverges at and to the left of `sigma=1`.  Subtracting
the density to continue the transform replaces the positive measure by the
signed discrepancy `dE_q`.  Thus positive definiteness proves the already
known Euler-product region and stops exactly where the nontrivial problem
begins.

## 8. Disposition

The q-free route supplies a useful negative result, not a verdict on the
existence of a fixed strip.

1. The power `1/q` in the q-free count can be made arbitrarily small with
   no effect on zeta zeros.
2. The full high-frequency obstruction is visible in the signed sawtooth
   error and in the factor `zeta(s)` common to every `F_q`.
3. Choosing `q` or a smoothing kernel as a function of height does not help:
   uniform comparison (1.4) preserves near-zeros, while phase-matched
   smoothing removes the ordinate being tested.
4. Ratios cancel the target, products either cancel it or retain its exact
   divisor, and finite logarithmic positivity can occur only in the
   target-cancelled case.

The surviving requirement is not a sharper q-free counting theorem.  It is
a signed, height-sensitive estimate for the common first-prime harmonic,
or an equivalent cross-prime cancellation theorem.  In the target strip,
such an estimate must be strong enough to give a nonzero height-dependent
lower bound for `zeta(s)` itself.  No such estimate is proved here.
