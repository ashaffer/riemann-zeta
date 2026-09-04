# High-denominator consecutive-gap coherence: primary-literature audit

**Date:** 2026-08-13

**Question.** What existing theorem can control the positive prime-gap/Voronoi
measure

```text
sum_(p_j asyp Y) lambda_j exp(i t log(p_j/Y)),
lambda_j = integral_(C_j) phi(log(x/Y)) dx/x
```

after deleting the optimized local rational arcs and the exceptional large-gap
half-cells, with

```text
beta=1537/10000,          q <= Y^beta,
theta_g=797/5000,         g > C Y^theta_g,
Y^.751 <= t <= Y^(50/33),
```

with a saving strictly larger than `Y^(-.0180303234)`?

**Verdict.** No primary source located in this audit proves the required
estimate, nor does one prove a signed Fourier estimate for any comparable
consecutive-gap measure.  The literature nevertheless gives a sharp diagnosis.

1. The denominator geometry has ample room.  Classical Vaughan cancellation
   for a *global natural von-Mangoldt sum* gives at least a `Y^(-.07685)`
   relative saving once `q > Y^(1537/10000)` in the whole relevant
   denominator range.
2. The missing localization scale is

   ```text
   H_c = Y/sqrt(t) = Y^h,
   8/33 <= h <= .6245.
   ```

   The residual band begins just below the best all-interval threshold
   `H > Y^(5/8+epsilon)` for linear prime exponential sums, and ends at
   `H=Y^(8/33)`.  The all-interval polynomial-phase inverse theorem used
   below starts only above `Y^(2/3+epsilon)`.  A 2026 almost-all theorem does
   reach `Y^(1/3+epsilon)`, but only for ordinary `Lambda` and with
   logarithmic loss/exceptional set.
3. Even for a fixed modulus `d >= 3`, the one-sided statistic which weights a
   prime by its following gap has no proved main-term asymptotic.  This is
   Jaeyoon Kim's prime-running-function problem.
4. That last point is **not** evidence against the actual Voronoi measure.
   Its leading weight is the half-sum of the preceding and following gaps.
   Kim's model predicts opposite `x/log x` biases for the forward and reversed
   measures, so their Voronoi symmetrization cancels the modeled first bias.
   No theorem was found which exploits this cancellation for the actual
   primes.
5. Ordinary large sieves give strong root-mean-square bounds for most
   rational frequencies or most heights, but permit an exceptional frequency.
   Renewal theorems assume iid increments and a quantitative nonlattice
   Fourier condition; neither hypothesis is known for prime gaps, and the
   latter is essentially the desired anti-coherence statement.
6. There is one directly usable power-saving theorem for the *unsigned gap
   tail*.  Gafni--Tao's exceptional-short-interval exponent implies, at the
   selected `theta_g=797/5000`,

   ```text
   sum_(p_n asyp Y, g_n>C Y^theta_g) g_n/Y
     << Y^(-1173/65000+o(1)).
   ```

   Here `1173/65000=.0180461538...`, just clearing the required
   `.0180303234`.  This is a deduction from their theorem and Table 1, not a
   formula stated verbatim in their paper.  It controls the half-cell tail,
   not signed coherence of the retained bounded gaps.

The live literature-informed target is therefore a **short-interval,
symmetrized consecutive-gap dispersion theorem**.  Direct gap moments do not
reach it, although the exceptional-set tail theorem does dispose of the
selected `theta_g=.1594` large-gap half-cells.  Off-the-shelf renewal theory
still does not apply.

No zero-free strip is claimed here.

---

## 1. Parameter dictionary

Write

```text
t=Y^a,                    .751 <= a <= 50/33,
beta=1537/10000=.1537,
theta_g=797/5000=.1594,
alpha_x=t/(2*pi*x),
H_c=Y/sqrt(t)=Y^(1-a/2).                              (1.1)
```

The prior cache used the historical cutoff `beta_0=.1`.  The statements below
use the optimized `beta=.1537` unless explicitly labelled historical.

On a physical interval of length `H_c` around `x asyp Y`, the logarithmic
phase has bounded quadratic variation:

```text
t log(x+u)
 = constant + (t/x)u + O(t H_c^2/Y^2)
 = constant + (t/x)u + O(1).                         (1.2)
```

The exact endpoint ledger is

```text
a=.751:      H_c=Y^.6245,
a=1:         H_c=Y^.5,
a=50/33:     H_c=Y^(8/33)=Y^.242424....              (1.3)
```

Dirichlet approximation with parameter `H_c` gives coprime `r,q` such that

```text
1 <= q <= H_c,
|alpha_x-r/q| <= 1/(q H_c) <= 1/q^2.                 (1.4)
```

But

```text
1/(q H_c)=sqrt(t)/(Yq),                               (1.5)
```

which is exactly the width used in the cached local rational excision.
Consequently a retained block forces

```text
Y^beta < q <= H_c,       beta=1537/10000.             (1.6)
```

This exact match is why additive-prime minor-arc estimates are the natural
comparator.

---

## 2. The additive-prime comparator has enough exponent

Vaughan's identity gives the classical estimate

```text
sum_(n<=Y) Lambda(n)e(alpha n)
 << (Y/sqrt(q) + Y^(4/5) + sqrt(Yq)) (log Y)^4        (2.1)
```

when `(r,q)=1` and `|alpha-r/q| <= q^(-2)`.  The original identity is due to
R. C. Vaughan, *Sommes trigonometriques sur les nombres premiers*,
C. R. Acad. Sci. Paris A 285 (1977), 981--983; the exact modern form (2.1)
is recorded in Montgomery--Vaughan,
[*Multiplicative Number Theory II*, Chapter 17](https://personal.science.psu.edu/rcv4/Vol2/Vol2.pdf).

If `q=Y^b`, the three relative savings in (2.1) are

```text
b/2,             1/5,             (1-b)/2.            (2.2)
```

Throughout (1.6), `b>1537/10000` and `b<=.6245`, so

```text
min{b/2,1/5,(1-b)/2} >=1537/20000=.07685.             (2.3)
```

Thus a hypothetical short-block analogue of (2.1), for the actual gap
weights, would beat the required `.0180303234` by a comfortable margin.

Priyamvad Srivastav's recent primary theorem,
[*Log-free bounds on exponential sums over primes*](https://arxiv.org/abs/2505.07803),
gives, for

```text
alpha=r/q+delta/Y,
|delta| <= Y^(1/5+eta)/q,
1 <= q <= Y^(2/5-eta),
delta_0=max(1,|delta|/4),                              (2.4)
```

the explicit log-free bound

```text
|sum_(n<=Y) Lambda(n)e(alpha n)|
 <= [q/phi(q)] F_eta(u,u_0) Y/sqrt(delta_0 q).         (2.5)
```

It cannot simply be substituted here.  The Dirichlet approximant (1.4) only
guarantees

```text
|delta| <= sqrt(t)/q,                                 (2.6)
```

which is far outside (2.4) on this height band, and a finer Dirichlet
approximant need not have denominator at most `Y^(2/5-eta)`.  Equation (2.5)
is useful evidence that the `q^(-1/2)` scale is robust, not a theorem covering
all retained curvature approximants.

Most importantly, (2.1) and (2.5) concern a prefix of length `Y`.  Taking the
difference of two such prefix bounds gives an error of order `Y^.92315` at the
smallest allowed denominator, while the curvature block has length at most
`Y^.6245`.  Prefix cancellation therefore does not localize to (1.1).

---

## 3. The exact short-interval barrier

Kaisa Matomaki and Xuancheng Shao,
[*Discorrelation between primes in short intervals and polynomial phases*](https://arxiv.org/abs/1902.04708),
record that Zhan's best uniform threshold for the linear sum

```text
sum_(N<n<=N+H) Lambda(n)e(alpha n)                    (3.1)
```

is `H=N^theta`, `theta>5/8`.  The later all-interval higher-uniformity
theorem of Matomaki--Shao--Tao--Teravainen,
[*Higher uniformity of arithmetic functions in short intervals I*](https://arxiv.org/abs/2204.03754),
also takes

```text
H >= X^(5/8+epsilon)                                  (3.2)
```

for `Lambda`, giving arbitrary logarithmic saving after subtracting its
major-arc approximant, uniformly against fixed-complexity nilsequences.

At the first unresolved height, however,

```text
H_c=Y^.6245 < Y^.625=Y^(5/8).                         (3.3)
```

The miss is only `.0005` in the interval exponent at the handoff, but it
increases continuously to

```text
5/8-8/33=.3825757...                                  (3.4)
```

at the top height.  Hence the whole residual band lies below the known
all-interval linear-prime threshold.

Theorem 1.3 of Matomaki--Shao gives a useful inverse statement at the longer
scale `H=N^theta`, fixed `theta>2/3`: if, for a degree-`k` polynomial

```text
g(n)=sum_(j=1)^k alpha_j(n-N)^j,
|sum_(N<n<=N+H) Lambda(n)e(g(n))| >= H/(log N)^A,      (3.5)
```

then there is

```text
q <= (log N)^(O_k(A)),
||q alpha_j|| <= (log N)^(O_k(A))/H^j,  1<=j<=k.      (3.6)
```

For the present logarithmic phase one may take a block
`L=Y^(2/3+epsilon)` and Taylor-expand to degree four.  At the largest height,
the remainder is

```text
t(L/Y)^5
 <= Y^(50/33-5/3+5epsilon)
 =  Y^(-5/33+5epsilon),                               (3.7)
```

so it tends to zero for `epsilon<1/33`.  A large *natural-Lambda* block sum
would therefore force the first derivative `t/(2*pi*Y)` into a polylogarithmic
major arc, much narrower than the deleted arc because `L >> H_c`.

This is conceptually encouraging but does not close the target:

* (3.5)--(3.6) gives arbitrary logarithmic, not fixed-power, saving;
* its constants are for fixed `A`, so one cannot set
  `A asyp log(Y)/loglog(Y)` to manufacture `Y^(-.018)`;
* the proof's quantitative Type-I/II propositions have conditions such as
  `H >= delta^(-C) max(L,M)`, and the remaining `n^(it)` case is handled only
  at logarithmic strength;
* the coefficient is `Lambda(n)`, not a function of the preceding and
  following prime gaps;
* the rational excision leaves an irregular subset, whereas (3.5) is a full
  interval sum.

So the literature nearly touches the bottom scale but has neither the length
range nor the coefficient identity needed here.

### 3.1 A post-2020 almost-all theorem reaches `1/3`, but not the gap measure

The important update to the all-interval barrier is Theorem 1.1(ii) and
Corollary 1.2(ii) of Matomaki--Radziwill--Shao--Tao--Teravainen,
[*Higher uniformity of arithmetic functions in short intervals II: almost all
intervals*](https://arxiv.org/abs/2411.05770v2).  For

```text
X^(1/3+epsilon) <= H <= X^(1-epsilon),                (3.8)
```

their theorem gives `H/log^A X` discorrelation of `Lambda-Lambda^sharp` from
fixed-complexity nilsequences outside an `x`-set of measure
`O_A(X/log^A X)`.  Their polynomial-phase corollary says more precisely that,
for any degree-`d` polynomial `P_x`, either

```text
|sum_(x<n<=x+H) Lambda(n)e(P_x(n))| <= H/log^A X       (3.9)
```

off an exceptional set of measure `O_A(X/log^A X)`, or there is one integer

```text
q << (log X)^O_(A,d,epsilon)(1)                       (3.10)
```

for which, on an `x`-set of measure `>>X/log^A X`,

```text
max_(1<=j<=d) H^j ||q alpha_(j,x)||
  <= (log X)^O_(A,d,epsilon)(1),                       (3.11)
```

where `alpha_(j,x)` are the Taylor coefficients of `P_x(x+n)`.  The authors
state that the corollary is new already for linear phases; they also record
that the earlier `5/8` result was the best known even almost everywhere.

For `P_x(n)=t log n/(2*pi)`, Taylor expansion to degree two on a curvature
block has cubic error

```text
t(H_c/Y)^3=t^(-1/2).                                  (3.12)
```

Consequently (3.8) covers

```text
t <= Y^(4/3-2*epsilon).                               (3.13)
```

Its obstruction is a simultaneous polylogarithmic-denominator major arc.
The present deletion of denominators `q<=Y^(1537/10000)` is much larger in
denominator range, but its width is only the Dirichlet width; the
polylogarithmic widening in (3.11) must not silently be treated as deleted.

This is the only post-2020 theorem found in the audit that proves the relevant
kind of local Fourier-mode cancellation in a substantially shorter range.  It
still does not close the target: the coefficient is `Lambda`, not a preceding/
following-gap weight; the conclusion and exceptional-set bound save powers of
`log X`, not `X`; it is almost-all rather than all-block; and (3.13) leaves the
top range `t>Y^(4/3)` untouched.

---

## 4. What is actually known about gap weights in residue classes

### 4.1 Kim's one-sided statistic is open even at fixed modulus

For a reduced class `a mod d`, Jaeyoon Kim defines

```text
Phi(x;d,a)
 = sum_(p_(j+1)<=x, p_j=a mod d) (p_(j+1)-p_j)
   + endpoint error.                                  (4.1)
```

In
[*Prime Running Functions*](https://arxiv.org/abs/2006.13355),
Conjecture 2.2 is

```text
Phi(x;d,a) ~ x/phi(d).                                (4.2)
```

Kim states that, apart from `d=2`, no unconditional asymptotic of this kind
was known, nor even a lower bound `Phi(x;d,a)>c x`.  His finer Conjecture 2.3
is

```text
Phi(x;d,a)
 = x/phi(d) + R(d;a)x/log x + o(x/log x).             (4.3)
```

Theorem 4.3 proves only the analogue in a **fixed-sieve modified Cramer
model**:

```text
E Phi_tilde_Q(x;d,a)
 = x/phi(d)+R_Q(d;a)x/log x+O_Q(x/log^2 x),            (4.4)
```

and Theorem 4.5 gives

```text
Var Phi_tilde_Q(x;d,a)=O_Q(x log x).                  (4.5)
```

The model theorems are not theorems about primes.

### 4.2 The Voronoi symmetrization cancels Kim's modeled first bias

Kim's Section 6 defines the reversed statistic, which puts the residue
condition on the upper endpoint.  He writes that a similar model analysis
predicts

```text
Phi^R(x;d,a)
 = x/phi(d) - R(d;a)x/log x + o(x/log x),             (4.6)
```

with the opposite bias sign.

For the logarithmic Voronoi cell at `p_j`, put

```text
Delta_j=log(p_(j+1)/p_j).
```

Taylor expansion of the cell mass gives

```text
lambda_j
 = phi(v_j)(Delta_(j-1)+Delta_j)/2
   +O(Delta_(j-1)^2+Delta_j^2).                       (4.7)
```

Thus its leading term is exactly the half-sum of Kim's forward and reversed
gap measures, after smooth localization and division by `p_j`.  Equations
(4.3) and (4.6) predict cancellation of the entire first `x/log x` residue
bias.

This correction matters: Kim's observed one-sided bias is not a heuristic
obstruction to the positive Voronoi antenna.  Combining Theorem 4.3 with the
*predicted reversed analogue* in Section 6 says that the fixed-`Q` model's
symmetrized expectation should have no `x/log x` term.  Kim does not state or
prove a reversed expectation/variance theorem, so even this fixed-model
symmetrized assertion must be labelled a deduction from his proposed analogous
analysis, not another numbered theorem.

The scope is equally important.  Formula (4.6) is an unnumbered model
prediction, not an actual-prime theorem.  Theorem 4.5's variance
`O_Q(x log x)` is likewise a theorem only for the forward statistic in the
fixed-sieve model.  Even cancellation down to an
unspecified `o(x/log x)` would not imply a fixed power `x^(-.018)` after
normalization.  Nothing is uniform for `d>Y^(1537/10000)`, for short
intervals, or for the extra phase `exp(i t log p)`.  Searches for the exact
reversed statistic and the citation graph of Kim's paper found no later
theorem exploiting this symmetrization.

### 4.3 Consecutive residue patterns: existence, not mixing

The strongest applicable proved coherence result is Maynard's Theorem 3.3 in
[*Dense clusters of primes in subsets*](https://compositio.nl/Content/prize2018_maynard.pdf).
For fixed `epsilon>0`, uniformly for

```text
m <= c_epsilon loglog x,
q <= (log x)^(1-epsilon),
(a,q)=1,                                               (4.8)
```

it gives

```text
#{p_n<=x:
  p_n=...=p_(n+m)=a (mod q),
  p_(n+m)-p_n<=epsilon log x}
 >>_epsilon pi(x)/(2q)^(exp(Cm)).                     (4.9)
```

For fixed `m,q`, this is a positive proportion.  Shiu's
[*Strings of congruent primes*](https://doi.org/10.1112/S0024610799007863)
gives arbitrarily long constant strings for fixed `q`.

These results prove that local residue coherence genuinely occurs.  They do
not provide a shell-density lower bound for long strings at a power-size
modulus, and their moduli are far below `Y^(1537/10000)`; those arcs are
already deleted in the present construction.

Cheuk Fung Lau's revised 2026 preprint,
[*Residue Class Patterns of Consecutive Primes*](https://arxiv.org/abs/2409.12819v2),
states the current limitation explicitly: even one prescribed nonconstant
length-`m` pattern is beyond existing methods.  His theorem says that for
squarefree `q`, every prescribed sequence of at least `60m log m` reduced
classes contains, in order, an `m`-term block pattern occurring infinitely
often, with each constant block of length at most `ceil(log m)`.  If
`q >> (log m)^2`, he obtains lower bounds

```text
>> [m/(log m)^10] phi(q)^2                            (4.10)
```

and

```text
>> exp(-O(m log_2(m)/log m))
   phi(q)^(m/ceil(log m))                             (4.11)
```

for the number of patterns known to occur infinitely often.

Again these are qualitative existence theorems.  They have no count uniform
in a shell endpoint `x`, no growing-modulus equidistribution, and no Fourier
cancellation.  Lemke Oliver--Soundararajan's
[*Unexpected biases in the distribution of consecutive primes*](https://arxiv.org/abs/1603.03720)
does give precise asymptotic predictions for consecutive residue pairs, but
the derivation is explicitly conjectural and uses uniform Hardy--Littlewood
tuple conjectures and inclusion--exclusion.

No primary source was found proving a nontrivial signed correlation

```text
sum_(p_n<=x) g_n g_(n+r),
```

a characteristic-function estimate for consecutive gaps, or a Fourier-mode
estimate for the forward, reversed, or symmetrized prime-running measure.

---

## 5. Prime-pair sieve information does not encode consecutiveness

The Selberg upper-bound sieve gives, uniformly for a fixed admissible shift
set `H={h_1,...,h_k}` in its standard range,

```text
#{n<=N: n+h_i is prime for every i}
 <<_k S(H) N/(log N)^k.                               (5.1)
```

For a pair this has the familiar variable-gap form

```text
#{p<=N: p+h is prime}
 << N/(log N)^2
    product_(ell|h, ell>2) (ell-1)/(ell-2).           (5.2)
```

Green--Tao's primary paper
[*Restriction theory of the Selberg sieve, with applications*](https://arxiv.org/abs/math/0405581)
develops the corresponding Fourier restriction bounds for fixed prime
tuples.

Equations (5.1)--(5.2) are nonnegative upper bounds.  They neither provide a
sign in `e(alpha p)` nor impose that `p,p+h` are consecutive.  Exact
consecutiveness additionally requires every integer between them to be
composite.  Inclusion--exclusion then involves a tuple order growing with
`h`; truncating it loses the required sign.  Gallagher's
[*On the distribution of primes in short intervals*](https://doi.org/10.1112/S0025579300016442)
derives Poisson gap statistics only **conditionally** on sufficiently uniform
Hardy--Littlewood `k`-tuple asymptotics.

This is not a theorem that all sieve approaches must fail.  It is the exact
reason a fixed-dimensional prime-pair upper sieve cannot be quoted as a
consecutive-gap Fourier lemma.

### 5.1 The exact `8/33` prime-pair theorem averages the wrong variable

There is a striking exponent match in Matomaki--Radziwill--Tao,
[*Correlations of the von Mangoldt and higher divisor
functions I*](https://arxiv.org/abs/1707.01315), Theorem 1.3(i).  If

```text
X^(8/33+epsilon) <= H <= X^(1-epsilon),
0 <= h_0 <= X^(1-epsilon),                             (5.3)
```

then

```text
sum_(X<n<=2X) Lambda(n)Lambda(n+h)
 = S(h)X+O_(A,epsilon)(X/log^A X)                     (5.4)
```

for all but `O_(A,epsilon)(H/log^A X)` integers
`|h-h_0|<=H`.  The exponent `8/33` is exactly the smallest curvature-block
exponent in (1.3).

It is nevertheless the wrong `H`: in (5.3), `H` is the width of an **average
over shifts** `h`, while in this project it is the physical length of an
interval in the prime variable.  Typical consecutive gaps have
`h asyp log X`; the exceptional set allowed by (5.4) can contain every such
small shift.  Formula (5.4) also has no additive phase in `n`, no condition
excluding intermediate primes, and only a logarithmic error for the
`Lambda Lambda` case.  Thus the numerical exponent coincidence does not
produce consecutive-gap coherence.

The sequel's shorter shift ranges concern divisor correlations and mixed
`Lambda d_k` correlations, not `Lambda Lambda`; the first paper itself notes
that even an asymptotic for one fixed even `h` would include the twin-prime
problem.  This is a genuine open-problem boundary, not a technical omission
that can be filled by specializing (5.4).

### 5.2 A usable unconditional tail bound for the truncated gap functional

The best direct second-moment theorem located is Stadlmann,
[*On the mean square gap between primes*](https://arxiv.org/abs/2212.10867),
Theorem 1:

```text
sum_(p_n<=Y) g_n^2 <<_epsilon Y^(1.23+epsilon),
g_n=p_(n+1)-p_n.                                     (5.5)
```

It does **not** suffice at the denominators in question.  Pointwise,

```text
min(g,g^3/q^2) <= g^2/q,                              (5.6)
```

so (5.5), with `q=Y^b`, gives only `Y^(1.23-b+epsilon)`, whose exponent is
`1.0763` at the optimized `b=1537/10000` (and still `1.07` at `b=.16`).
Combining (5.5) with a maximal-gap bound to manufacture a third moment is
still weaker.  Järviniemi's primary
large-tail theorem,
[*On large differences between consecutive
primes*](https://arxiv.org/abs/2212.10965), gives

```text
sum_(p_n in [Y,2Y], g_n>=Y^(1/2)) g_n << Y^(.57+epsilon),
sum_(p_n in [Y,2Y], g_n>=Y^(.45)) g_n << Y^(.63+epsilon), (5.7)
```

but its thresholds are far above the optimized `Y^.1537`--`Y^.1594` scales.

A substantially better input comes from exceptional short intervals rather
than a raw moment.  Gafni--Tao,
[*On the number of exceptional intervals to the prime number theorem in short
intervals*](https://doi.org/10.2140/ent.2026.5.221), define `mu(theta)` so that
the set of starts `x in [Y,2Y]` where the PNT fails in an interval of length
`x^theta` has measure

```text
<< Y^[mu(theta)+o(1)].                                (5.8)
```

Their Theorem 1.4 (Theorem 1.2 in arXiv v1) proves

```text
mu(theta) <= inf_(epsilon>0)
  sup_[A(sigma)>=1/(1-theta)-epsilon]
  ((1-theta)(1-sigma)A(sigma)+2sigma-1).              (5.9)
```

This source also identifies a genuine literature pitfall: additional bounds
claimed by Bazzanella in the range `1/6<theta<=1/2` have an incomplete
argument, because the Jutila density estimate no longer gives the asserted
restriction on `sigma` below `theta=1/2`.  None of those disputed formulae is
used here.

Combining (5.9) with the unconditional zero-density bounds in their Table 1
gives the exact local envelope

```text
mu(theta) <= 1-(9/13)(theta-2/15),
2/15 <= theta <= 353/1445.                            (5.10)
```

The paper prints (5.10) for `theta=2/15+Delta` with sufficiently small
positive `Delta`.  The full stated interval in (5.10) is our finite rational
comparison of all the Table-1 branches in (5.9), not an additional claim made
verbatim by the authors; see
[`verify_zeta23_high_denominator_gap_tail.py`](verify_zeta23_high_denominator_gap_tail.py).
At the maximizing branch `sigma=7/10`, equality in this derived bound is
`mu_(2,sigma)=1-(9/13)(theta-2/15)`.  At `theta=353/1445`
it ties the threshold point from the `11/(48sigma-36)` branch; immediately
afterward that branch is larger.

Their equation (1-6) records the resulting count bound for large gaps.  The
measure definition gives the stronger total-mass consequence

```text
sum_(p_n asyp Y, g_n>Y^theta) g_n
  << Y^[mu(theta)+o(1)].                              (5.11)
```

Indeed, the interior starting points of distinct gaps are disjoint and give
empty prime intervals.  Because `theta<1/2`, such an interval contains at
most one `k`-th power for each `k>=2`, so its total prime-power contribution
to `Lambda` is `O(log^2 Y)=o(Y^theta)`.  Fixed multiplicative constants in the
gap threshold are absorbed by replacing `theta` by `theta-o(1)`.

Now put `q=Y^b` and dyadically split at `g=q`.  A bin `g asyp Y^theta<=q`
contributes at most

```text
Y^(2theta-2b) sum_bin g.                              (5.12)
```

Below `theta=2/15`, use the telescoping bound `sum g<<Y`; above it, use
(5.10)--(5.11).  Since

```text
1-(9/13)(theta-2/15)+2theta-2b                       (5.13)
```

is increasing in `theta`, the largest exponent occurs at `theta=b`; gaps
larger than `q` obey the same bound directly from (5.11).  Hence

```text
sum_(p_n asyp Y) min(g_n,g_n^3/q^2)
 << Y^[1-c(b)+o(1)],
c(b)=(9/13)(b-2/15),       3/20<=b<=4/25.             (5.14)
```

Numerically,

```text
c(.15)=3/260=.0115384615...,
c(.16)=6/325=.0184615384...,                          (5.15)
```

and `c(b)>.0180303234` precisely when

```text
b>.1593771338....                                    (5.16)
```

At the optimized rational cutoff `b=beta=1537/10000`, (5.14) saves only

```text
c(beta)=1833/130000=.0141,                            (5.17)
```

which is insufficient.  The optimized route therefore does **not** identify
the gap threshold with the rational cutoff: it separately takes
`theta_g=797/5000=.1594` and discards those large-gap half-cells, obtaining
the `1173/65000` saving in Section 9.  All of these tail estimates are unsigned
and global; they do not prove Fourier cancellation or residue mixing.

For comparison, Runbo Li's Theorem 1.1 in
[*Primes in almost all short intervals*](https://arxiv.org/abs/2407.05651v6)
puts primes in intervals of length `X^(1/21.5+epsilon)` outside only
`O_B(X/log^B X)` integer starts.  This is an impressive shorter-scale
existence theorem, but the exceptional set has logarithmic rather than fixed
power saving and the conclusion is not a PNT asymptotic.  Applied to total gap
mass it gives at best `Y/log^B Y`, not the `Y^(1-c)` needed here.

---

## 6. What the ordinary large sieve gives for the actual coefficients

The analytic large sieve of Montgomery--Vaughan,
[*The large sieve*](https://doi.org/10.1112/S0025579300004708), says that for
`delta`-separated frequencies modulo one,

```text
sum_r |sum_(M<n<=M+N) a_n e(alpha_r n)|^2
 <= (N+delta^(-1)) sum_n |a_n|^2.                    (6.1)
```

For reduced fractions with denominator at most `2Q`, one may take
`delta asyp Q^(-2)`.  Insert the gap/Voronoi coefficients at prime indices
and zero elsewhere.  Stadlmann's theorem gives

```text
sum_p lambda_p^2 << Y^(-.77+epsilon).                 (6.2)
```

For a dyadic denominator family `q asyp Q=Y^b`, (6.1) yields

```text
sum_(q asyp Q) sum_(r mod q)^*
 |sum_p lambda_p e(rp/q)|^2
 << (Y+Q^2)Y^(-.77+epsilon).                          (6.3)
```

Since there are `asyp Q^2` fractions, the root-mean-square amplitude is

```text
Y^(.115-b+epsilon)       if b<=1/2,
Y^(-.385+epsilon)        if b>=1/2.                   (6.4)
```

Thus the RMS already beats `Y^(-.0180303234)` once

```text
b>.1330303234...,                                       (6.5)
```

and is very strong for larger denominators.  At the optimized first allowed
scale `b=1537/10000`, (6.4) is already `Y^(-.0387+epsilon)`.  Thus the whole
retained denominator range is good in root mean square.  More fundamentally,
(6.3) is only an average and permits a sparse exceptional set containing the
specific approximants selected by `t/(2*pi*x)`.

The same paper's Hilbert-inequality method, or Montgomery--Vaughan,
[*Hilbert's inequality*](https://doi.org/10.1112/jlms/s2-8.1.73), gives for
the log-prime frequencies

```text
integral_I |sum_p lambda_p p^(it)|^2 dt
 << (|I|+Y) sum_p lambda_p^2.                         (6.6)
```

At `|I|=Y^(50/33)`, the mean square is excellent, but a single coherent
height is still allowed.  Neither (6.3) nor (6.6) is a pointwise theorem.

---

## 7. Why renewal theory is not an imported solution

Quantitative renewal theory starts with independent, identically distributed
increments having a fixed probability law `rho`.  A standard strong
nonlattice hypothesis is

```text
inf_(|u|>epsilon) |1-rho_hat(u)| > 0.                 (7.1)
```

Blanchet--Glynn,
[*Uniform Renewal Theory with Applications to Expansions of Random Geometric
Sums*](https://doi.org/10.1239/aap/1198177240),
obtain uniform/exponential conclusions under a uniformly strong nonlattice
condition.  Boyer,
[*The speed of convergence in the renewal theorem*](https://arxiv.org/abs/1506.07625),
uses the weaker Diophantine condition

```text
liminf_(|u|->infinity) |u|^ell |1-rho_hat(u)| > 0      (7.2)
```

and relates it to a zero-free region for `1-rho_hat(z)`.  Carlsson,
[*Estimates of the renewal measure*](https://doi.org/10.2969/jmsj/83298329),
gives sharp Fourier estimates for strongly nonlattice laws.

Consecutive prime gaps satisfy none of the entry hypotheses currently known:

* the increments are deterministic, dependent, and nonstationary;
* physical prime gaps are even integers after the initial gap, hence are
  exactly lattice at a frozen physical scale;
* logarithmic gaps remove the literal lattice but depend on the location
  `p_j` and do not have one common iid law;
* a finite-scale version of (7.1) or (7.2) through frequency
  `Y^(50/33)` is itself a quantitative anti-alias/Fourier statement.

Accordingly, renewal theory explains the *shape* of the missing lemma but
does not prove its key hypothesis.  This rules out importing a rate “for
free”; it does not rule out proving a prime-specific nonlattice theorem.

[*Maier's theorem on primes in short intervals*](https://doi.org/10.1307/mmj/1029003189)
and Granville--Soundararajan's
[*uncertainty principle for arithmetic sequences*](https://doi.org/10.4007/annals.2007.165.593)
also deserve precise scoping.  Maier proves that
for each fixed `lambda>1`, the normalized prime counts in intervals of length
`(log x)^lambda` have limsup above one and liminf below one.  This rules out a
uniform local Poisson/renewal approximation on every polylogarithmic
interval.  It does **not** rule out the shell-global Fourier cancellation
asked for here.

---

## 8. Exact open and no-go statements supported by the survey

The primary literature supports the following statements.

```text
Forward gap mass equidistribution, fixed d>=3:        OPEN (Kim).
Symmetric forward/reverse gap equidistribution:       NO THEOREM LOCATED.
Prescribed nonconstant consecutive residue pattern:   OPEN in general (Lau).
Growing q>Y^(1537/10000) shell mixing:                 NO THEOREM LOCATED.
Signed Fourier decay for consecutive gaps:             NO THEOREM LOCATED.
All-interval natural-Lambda linear threshold:           theta>5/8.
Almost-all Lambda polynomial-phase threshold:           theta>1/3 (log saving).
Present first curvature-block exponent:                .6245<5/8.
All-interval polynomial-phase inverse threshold:        theta>2/3.
Global additive-prime saving after q>Y^.1537:            at least .07685.
Required fixed saving:                                  >.0180303234.
Direct second gap moment at q=Y^.1537:                  INSUFFICIENT.
Truncated functional saving at b=.1537:                 .0141 (insufficient).
Half-cell tail at theta_g=.1594:                        .0180461538 (sufficient).
Large-sieve control on all retained q:                  RMS/AVERAGE ONLY.
Renewal Fourier decay:                                  REQUIRES MISSING HYPOTHESIS.
Literature theorem eliminating actual Voronoi target:  NONE FOUND.      (8.1)
```

The genuine no-go scopes are narrower:

1. Maier eliminates uniform Poisson behavior in every polylogarithmic
   interval, not global Fourier decay.
2. Fixed-dimensional prime-pair upper sieves do not encode the absence of
   intermediate primes or signed cancellation; this does not eliminate a
   coefficient-specific dispersion argument.
3. Large-sieve and Dirichlet-polynomial mean-square theorems do not imply a
   pointwise supremum without another structural input.
4. Renewal rates cannot be applied until a quantitative nonlattice condition
   is proved; that condition is not known to be false for logarithmic prime
   gaps.
5. Shiu--Maynard coherent strings disprove any assumption of uniformly
   bounded same-class runs, but occur only at fixed/polylogarithmic moduli and
   do not contradict high-denominator shell cancellation.

---

## 9. The sole literature-informed successor lemma

The clean missing statement is a local theorem for the **symmetrized** actual
gap measure.  A sufficient schematic form is the following.

For every `t` in the residual band and every interval `J` of length
`H_c=Y/sqrt(t)` in the fixed shell, prove on the retained minor set

```text
| sum_(p_j in J)
    phi(log(p_j/Y))
    [Delta_(j-1)+Delta_j]/2
    exp(i t log(p_j/Y)) |

 << (|J|/Y) Y^(-c),                  c>.0180303234.    (9.1)
```

The quadratic error in (4.7) is already controlled by Stadlmann.  Summing
(9.1) over `O(Y/H_c)` blocks closes the full residual antenna.

There is now a rigorous preprocessing step before (9.1).  Split every
Voronoi cell into its preceding- and following-gap half-cells, and discard
only half-cells belonging to a gap

```text
g>C Y^(797/5000).
```

Equations (5.10)--(5.11), divided by `Y`, bound their total logarithmic mass
by

```text
Y^(-1173/65000+o(1)),
1173/65000=.0180461538...>.0180303234.                (9.2)
```

The margin is only `.0000158304...`, so all losses must remain subpower.
This removes the dangerous large-gap tail; it does not control the phases of
the remaining bounded gaps.

The most plausible imported architecture is:

```text
forward/reverse symmetrization
  + a consecutive-gap dispersion or Type-II identity
  + rational approximation q in (Y^(1537/10000),H_c]
  + short-interval additive cancellation.             (9.3)
```

Kim's opposite-bias prediction says the symmetrization in (9.3) is not
cosmetic: it removes the only documented systematic residue bias of the
one-sided gap measure.  Vaughan's exponent ledger says only `.018` of the
available `.07685` saving need survive.  The hard step is to construct a
prime-specific identity that localizes below `Y^(5/8)` while retaining the
relationship between adjacent gaps; no cited theorem presently supplies it.
