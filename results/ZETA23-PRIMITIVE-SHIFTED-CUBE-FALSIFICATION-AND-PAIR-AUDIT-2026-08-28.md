# Primitive shifted cubes: falsification, continued fractions, and pair energy

**Date:** 2026-08-28  
**Verdict:** no counterexample and no proof of the sharp primitive estimate were
found.  The strongest fully licensed uniform estimate remains

```text
N_prim(P) <<_epsilon P^(17/24+epsilon).                 (0.1)
```

The desired exponent is `9/16`.  The frequently quoted exponent `5/8` is
only conditional on an unchecked application of Huxley IV to the integral
cubic.  It must not be cited as an unconditional theorem.

The audit does produce two exact structural facts.  Every putative primitive
solution is a convergent to a reduced rational cube whose next partial
quotient is `>>P^2`, independently of `gcd(u,P)`.  Also, no characteristic-zero
polynomial parametrization can have exactly the critical degree pattern
`(deg A,deg B,deg u,deg P,deg D)=(9,9,16,16,7)`.  These facts explain the
computational sparsity, but neither currently supplies the required aggregate
bound.

The proposed off-diagonal pair-energy replacement is a credible sufficient
gate, but no primary theorem located in this audit proves it.  Its target
order is sharp because fixed rational resonances already contribute a constant
multiple of `P^(9/8)`.

## 1. Frozen primitive problem

Put

```text
T=P^(9/16),                  H=P^(7/16),                 T*H=P
```

and define

```text
N_prim(P)=#{(A,B,u) in Z_(>0)^3:
  T<=A,B<2T, P<=u<2P, gcd(A,B)=1,
  0<|A*u^3-B*P^3|<=H}.                                 (1.1)
```

The proposed estimate is

```text
N_prim(P) <<_epsilon T*P^epsilon=P^(9/16+epsilon).       (1.2)
```

Every point in (1.1) automatically has `u^3<2P^3+H/T`; in particular,
apart from an immaterial endpoint it lies in

```text
P<=u<2^(1/3)*P.                                         (1.3)
```

All constants below remain valid for fixed enlargements of these dyadic
shells.

## 2. Exact `gcd(u,P)` decomposition

For a solution, write

```text
d=gcd(u,P),              u=d*v, P=d*p, gcd(v,p)=1,
D=A*u^3-B*P^3=d^3*E.                                  (2.1)
```

Thus

```text
d^3|D,                  0<|E|<=H/d^3,
d<=H^(1/3)=P^(7/48).                                   (2.2)
```

In particular `p=P/d>=P^(41/48)`.  There are only `P^epsilon` possible
divisors `d`; no hidden sum over all integers up to `H^(1/3)` occurs.

Fix `d` and `A`, and put

```text
h=gcd(A,p^3),             n=p^3/h.                     (2.3)
```

The equation `A*v^3-B*p^3=E` implies `h|E`, and after writing
`A=h*A_1`, `E=h*e` it gives

```text
v^3=A_1^(-1)*e (mod n),       gcd(A_1,n)=1.            (2.4)
```

For every nonzero integer `e`, the standard prime-power calculation gives

```text
rho_3(e;n)=#{x mod n:x^3=e (mod n)}
          <<_epsilon n^epsilon*gcd(e,n)^(2/3).          (2.5)
```

Since `n>=p^3/(2T)>>p`, each residue class contains at most one admissible
`v`.  Moreover, for `Y>=1`,

```text
sum_(1<=e<=Y) gcd(e,n)^(2/3)
 <= sum_(r|n) r^(2/3)*floor(Y/r)
 <<_epsilon Y*n^epsilon.                               (2.6)
```

Consequently the number of solutions for fixed `(d,A)` is

```text
<<_epsilon (H/(d^3*h))*P^epsilon,                      (2.7)
```

with the expression interpreted as zero when `H/(d^3h)<1`.  Large common
factors of `A` and `p^3` therefore suppress this elementary count.  Highly
composite `P` does not create an extra power through this gcd channel; the
potentially worst slice is essentially the coprime one.

## 3. Every solution is a giant-partial-quotient event

Because `(A,B)=1`, the fraction `B/A` is reduced.  From (2.1),

```text
|(v/p)^3-B/A|=|E|/(A*p^3).                             (3.1)
```

Also

```text
2*A*|E| <=4*T*H/d^3=4P/d^3 < P^3/d^3=p^3             (3.2)
```

for `P>2`.  Hence (3.1) is less than `1/(2A^2)`, and Legendre's
continued-fraction criterion shows that `B/A` is a convergent of the reduced
rational number

```text
x=v^3/p^3.                                             (3.3)
```

Let `q_n=A` be its denominator and `q_(n+1)` the next convergent denominator.
The convergent inequalities for a nonterminal convergent give

```text
1/[A*(A+q_(n+1))] < |x-B/A| < 1/[A*q_(n+1)].          (3.4)
```

Using the left inequality and (3.1),

```text
q_(n+1)>p^3/|E|-A.                                    (3.5)
```

If `a_(n+1)` is the next partial quotient, then
`q_(n+1)=a_(n+1)A+q_(n-1)` with `q_(n-1)<A`.  Therefore

```text
a_(n+1)>p^3/(A*|E|)-2
        >=P^3/(2*T*H)-2
        =P^2/2-2.                                     (3.6)
```

The cancellation of `d^3` in (3.6) is important: every gcd slice demands
the same `P^2`-sized partial quotient.  Thus (1.2) reduces to bounding the
subset of these exceptionally large-quotient events that also obeys the
coefficient and residual shells.  The converse without those retained shell
conditions is not asserted.  No known uniform theorem located here aggregates
the relevant events sharply enough.

## 4. Licensed analytic bound, and the correction to `5/8`

For fixed `d`, (3.1) has the uniform error

```text
|(v/p)^3-B/A| <= H/(T*P^3),                            (4.1)
```

independent of `d`.  Applying Theorem 2 of Huxley,
[*The rational points close to a curve II*](https://matwbn.icm.edu.pl/ksiazki/aa/aa93/aa9331.pdf),
to the cubic on an interval of length `p=P/d`, with denominators `A~T`, gives

```text
N_d <<_epsilon
 [p*(H*T/P^3)^(1/4)+(p*T^2)^(1/3)]P^epsilon.           (4.2)
```

Since `H*T=P`, the two terms are at most `P^(1/2)/d` and
`P^(17/24)/d^(1/3)`.  Summing only over divisors `d|P` proves (0.1).
This is uniform in arbitrary, including highly composite, `P`.

Huxley III is also directly checkable for the integral cubic, but its two
relevant terms specialize to `P^(5/8)` and `P^(19/24)`; the latter dominates,
so it is weaker than (4.2).

The original text of Huxley IV, *The rational points close to a curve IV*,
Bonner Math. Schriften 360 (2003), was not available in a checkable online
copy.  The accessible specialization in Blomer--Schobel,
[*Twins of powerful numbers*](https://doi.org/10.7169/facm/2013.49.2.12),
explicitly assumes that its power exponent is **not an integer**.  It therefore
does not license substituting the cubic exponent `3`.  If the original
determinant theorem is eventually checked and does admit this cubic, its
top-slice calculation would give

```text
N_prim(P) <<_epsilon P^(5/8+epsilon),                  (4.3)
```

still a factor `P^(1/16)` short of (1.2).  Until that source check is made,
(4.3) is conditional; the fully licensed gap is

```text
17/24-9/16=7/48.                                      (4.4)
```

Konyagin's smooth fractional-parts theorem does not improve (0.1).  In the
form printed as Theorem 6 of Trifonov,
[*Integer points close to a smooth curve*](https://www.math.bas.bg/serdica/1998/1998-319-338.pdf),
which cites Konyagin's primary paper
[*Estimates of the least prime factor of a binomial coefficient*](https://doi.org/10.1112/S0025579300007555),
specializing `F(u)=u^3/6`, interval length `P`, denominator cap `T`, and
vertical tolerance `H/T=P^(-1/8)` produces terms exceeding `P`; after the
trivial cap it yields only `O(P)`.

## 5. Parametric-family falsification

The obvious algebraic constructions fail for structural reasons.  Exact
rational rays make `D=0`, while perturbing either the coefficient ratio or
the input ratio by one integer unit normally changes `A*u^3-B*P^3` by a
quantity of order at least `P^3` or `T*P^2`, far larger than `H`.

There is also a rigorous function-field obstruction to a scale-exact
polynomial family.  Let `k>=1`, work over a characteristic-zero field, and
suppose nonzero polynomials satisfy

```text
A*u^3-B*P^3=D!=0,
deg A=deg B=9k, deg u=deg P=16k, deg D<=7k.            (5.1)
```

Put `X=A*u^3`, `Y=B*P^3`, `G=gcd(X,Y)`, and `g=deg G`.  Since `G|D`, the
three polynomials `X/G`, `Y/G`, and `D/G` are pairwise coprime.  The roots of
the first two are contained among the roots of `A*B*u*P`, while
`deg(D/G)<=7k-g`.  Hence

```text
deg rad((X/G)*(Y/G)*(D/G))
 <=9k+9k+16k+16k+(7k-g)=57k-g.                        (5.2)
```

But Mason--Stothers applied to `X/G-Y/G=D/G` says

```text
deg(X/G) <=deg rad((X/G)*(Y/G)*(D/G))-1.               (5.3)
```

The left side is `57k-g`, contradicting (5.2).  Thus no polynomial identity
has the critical degree pattern, even after allowing arbitrary common
content.  This rules out the most natural parametric counterexample, not
sporadic integer families.

## 6. Computational adversarial audit

An exact continued-fraction scan used Section 3 rather than looping over all
`A,B`.  For each `P,u`, it reduced `u/P=v/p`, generated every convergent of
`v^3/p^3`, retained denominators in the exact dyadic `A` shell, and tested
the integer residual and all endpoint conditions.  The scan found no
primitive nonzero solution for any integer

```text
2<=P<=20,000.                                          (6.1)
```

It also found none in targeted highly composite, primorial, prime, and
perfect-power cases through `P=16,777,216`.  This is falsification evidence,
not a proof.  It is consistent with the random-volume heuristic: the `~TP`
pairs `(A,u)` hit a residual window of relative width `H/P^3`, giving expected
size

```text
T*P*H/P^3=T*H/P^2=P^(-1).                             (6.2)
```

The exact arithmetic may of course differ from that heuristic; the purpose
of the scan was to find structured exceptions, and none appeared.

## 7. The off-diagonal transition-pair energy

Let `C=P^(9/8)` and freeze, for definiteness,

```text
E(P,C)=sum_(C<=c<2C) w(c)
  #{P<=u,v<2^(1/3)P, u!=v:
    ||c*(u^3-v^3)/P^3||<=P^(-2)},                     (7.1)
```

where `w(c)` is nonnegative and divisor-bounded.  The desired estimate is

```text
E(P,C) <<_epsilon C*P^epsilon.                         (7.2)
```

Equivalently, after choosing the nearest integer `m`, the indicator in (7.1)
is

```text
|c*(u^3-v^3)-m*P^3|<=P.                               (7.3)
```

The order `C` in (7.2) cannot be improved.  If `4|P`, take

```text
u=P,                    v=5P/4.
```

Then `u,v` lie in the shell and

```text
(u^3-v^3)/P^3=-61/64.                                 (7.4)
```

Every `c` divisible by `64` makes (7.4) an integer.  Consequently even the
single ordered pair contributes `C/64+O(1)` to the unweighted count.  Any
proof of (7.2) must retain these arithmetic resonances rather than assume
generic equidistribution.

No off-the-shelf primary theorem found in this search proves (7.2):

* Kerr--Mohammadi--Shparlinski,
  [*Additive energy of polynomial images*](https://arxiv.org/abs/2306.10677),
  controls four-variable additive congruences for `f(I)` modulo `m`.  It does
  not control a variable dilate `c`, a shrinking target, and a fixed highly
  composite modulus `P^3` in the form (7.1).
* Kerr--Mohammadi,
  [*Points on polynomial curves in small boxes modulo an integer*](https://arxiv.org/abs/1803.10373),
  gives single polynomial-box bounds.  Applied after fixing parameters, its
  available box scale loses more than the elementary root count and gives no
  aggregation over `c`.
* Welsh,
  [*Spacing and a Large Sieve Type Inequality for Roots of a Cubic Congruence*](https://arxiv.org/abs/1809.05211),
  studies roots while the modulus varies; it is not a fixed-`P^3` cubic-image
  pair theorem.
* Metric pair-correlation results for `alpha*n^k` average over, or impose
  Diophantine hypotheses on, a fixed real `alpha`.  Here
  `alpha=c/P^3` is rational, varies with `c`, and has the exact resonances
  (7.4).
* Large-sieve theorems for square or power moduli average over the moduli and
  numerators.  They do not imply the required fixed-modulus weighted
  incidence estimate.

Thus (7.2) should be recorded as a new mask-sensitive/fixed-modulus theorem
to prove, not as an invocation of an existing large sieve.  The literal
closing lemma is:

> Uniformly for every integer `P`, `C~P^(9/8)`, and every divisor-bounded
> nonnegative weight `w`, the off-diagonal count (7.1) is
> `O_epsilon(C P^epsilon)`.

The resonance (7.4) shows both why the statement needs a `P^epsilon` arithmetic
allowance and why a merely metric theorem cannot close it.

## 8. Bottom line

The primitive shifted-cube estimate survived the counterexample search, but
it remains unproved.  The best unconditional exponent is `17/24`; `5/8` is
conditional on a source check and is not currently licensed.  The strongest
new deterministic formulation is the `P^2` next-partial-quotient gate (3.6).
The transition-pair estimate (7.2) is another plausible closure mechanism,
is sharp in order of magnitude, and presently appears to require genuinely
new fixed-modulus arithmetic rather than an existing pair-correlation theorem.
