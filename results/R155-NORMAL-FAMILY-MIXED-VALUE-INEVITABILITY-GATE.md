# R155 normal-family mixed-value inevitability gate

## Status

R153 left a target-local mixed-`a`-point estimate as the last condition in
its nonlinear support amplifier.  That condition can now be decided in the
direction relevant to the proposed proof: simultaneous mixed-value avoidance
is not merely unavailable in the literature.  It is impossible along a
growing deleted head which retains a fixed zeta zero.

There are two levels of the obstruction.

1. A holomorphic family which omits two fixed values is normal.  Head
   deletion makes it converge to `1` on the part of the target domain in
   `Re(s)>1`, so normality and the identity theorem make it converge to `1`
   everywhere.  It therefore cannot retain a zero.
2. Omitting even the single value `2` is impossible when the number of zeros
   in the target domain stays bounded.  The logarithmic lift
   `h=Log(2-F)` can meet the lattice `log 2+2 pi i Z` only at zeros of `F`.
   Boundedly many zeros leave two fixed lattice values omitted, returning to
   Montel's theorem.

The second statement closes the natural repeated-pole workaround which
collapses all artificial values to `F=2`.  A direct Jensen--Nevanlinna audit
also shows why ordinary family moments point the wrong way: the deterministic
head-truncated zeta skeleton has polynomially large characteristic and
polynomially many mixed points.

```text
two-fixed-value avoidance with a retained zero             IMPOSSIBLE
one-fixed-value avoidance with bounded zero divisor         IMPOSSIBLE
R153 all-mixed-factor zero-free hypothesis                  IMPOSSIBLE
repeated-pole one-value amplifier                           CLOSED
truncated-zeta mixed-value characteristic                   POLYNOMIAL
existing conductor-uniform fixed-window a-point estimate   NOT KNOWN
signed estimate including the forced mixed points           OPEN
fixed uniform zeta zero-free strip                          NOT PROVED
zeros approaching one                                       NOT PROVED
```

Date: 2026-08-08.

Predecessors:
[`R153-NONLINEAR-SUPPORT-AMPLIFIER-AND-MIXED-VALUE-GATE.md`](R153-NONLINEAR-SUPPORT-AMPLIFIER-AND-MIXED-VALUE-GATE.md)
and
[`R154-COPRIME-FILTER-PACKET-AND-RESULTANT-GATE.md`](R154-COPRIME-FILTER-PACKET-AND-RESULTANT-GATE.md).

## 1. The two-value normal-family theorem

Let `Omega` be a connected domain, let `V` be a nonempty open subset of
`Omega`, and fix `rho in Omega`.

### Theorem 1.1 -- two omitted values cannot bridge the head

There is no sequence `F_j in Hol(Omega)` such that

```text
F_j -> 1 locally uniformly on V,
F_j(rho)=0,
a,b notin F_j(Omega)                                      (1.1)
```

for two fixed distinct complex numbers `a,b`.

#### Proof

A family of holomorphic functions omitting two fixed finite values is normal
by Montel's theorem.  Pass to a locally spherically convergent subsequence.
On `V` its limit is the finite function `1`; hence the convergence is locally
ordinary there.  The meromorphic identity theorem makes the limit identically
`1` on `Omega`.  Local convergence at `rho` then gives

```text
0=lim_j F_j(rho)=1,                                        (1.2)
```

a contradiction.  QED.

The assertion is qualitative but uniform in every auxiliary arithmetic
parameter.  It needs no conductor estimate and no value-distribution theorem.

## 2. One omitted value forces zero proliferation

For one omitted value the functions themselves need not be normal.  The
fixed zero divisor supplies the missing rigidity.

Assume now that `Omega` is simply connected.

### Theorem 2.1 -- logarithmic-lattice rigidity

There is no sequence `F_j in Hol(Omega)` satisfying

```text
F_j -> 1 locally uniformly on V,
F_j(rho)=0,
2 notin F_j(Omega),                                       (2.1)
```

while the number of distinct zeros of `F_j` in `Omega` remains bounded.

#### Proof

Since `2-F_j` is nonvanishing and `Omega` is simply connected, choose a
holomorphic logarithm

```text
2-F_j=exp(h_j).                                             (2.2)
```

The branch can be normalized so that `h_j -> 0` on `V`, because
`2-F_j -> 1` there.  Put

```text
Lambda={log 2+2 pi i k:k in Z}.                             (2.3)
```

Then

```text
h_j(s) in Lambda  iff  F_j(s)=0.                            (2.4)
```

If every `F_j` has at most `M` distinct zeros, then `h_j(Omega)` meets at
most `M` distinct values of `Lambda`.  Among any fixed `M+2` lattice values,
at least two are omitted.  There are only finitely many pairs in this fixed
set, so a subsequence omits the same pair.  Montel makes that subsequence of
`h_j` normal.  Its limit is zero on `V`, hence zero throughout `Omega`.

But `F_j(rho)=0` gives `h_j(rho) in Lambda`, and `Lambda` has a uniformly
positive spherical distance from zero.  This contradicts local spherical
convergence to zero at `rho`.  QED.

Thus a holomorphic function can omit `2`, retain a zero, and look like `1`
on a separated open set only by creating an unbounded number of additional
zeros.  This hypothesis is sharp in kind.  In disc coordinates, with the
target at `u=a` and a control disc `|u|<=kappa<|a|`,

```text
F_n(u)=2-exp[log(2)(u/a)^n]                                 (2.5)
```

omits `2`, vanishes at `a`, and tends exponentially to `1` on the control
disc, while its zero count grows with `n`.

## 3. Arithmetic application

Consider first the quadratic quotient

```text
F_chi(s)=zeta(s)/L(s,chi),                                  (3.1)
```

where `chi` is even, real, and

```text
chi(p)=1 for every p<=H.                                   (3.2)
```

In every fixed half-plane `Re(s)>=1+epsilon`, its Euler product gives,
uniformly in `chi`,

```text
log F_chi(s)
 =sum_(p>H,v>=1)[1-chi(p)^v]/[v p^(vs)]
 =O_epsilon(H^(-epsilon)),                                 (3.3)

F_chi(s)=1+O_epsilon(H^(-epsilon)).                         (3.4)
```

The harmless logarithmic improvement from the prime number theorem is not
needed.  The same conclusion holds for the fixed-degree cubic and
class-character quotients in R148--R153: exact head deletion and a uniform
local Euler-factor bound imply convergence to `1` on compact subsets of
`Re(s)>1`.

Let `Omega` be a fixed simply connected localization disc containing a
hypothetical zeta zero `rho` and a nonempty open cap in `Re(s)>1`.  If the
denominator of (3.1) is zero-free in `Omega`, then `F_chi` is holomorphic
there and its distinct zeros are the fixed finite set of zeta zeros in the
disc.  Theorem 2.1 therefore proves:

### Corollary 3.1 -- forced quadratic mixed point

For all sufficiently large `H`, every character satisfying (3.2) has at
least one of

```text
L(s,chi)=0,
zeta(s)-2L(s,chi)=0                                        (3.5)
```

in `Omega`.

This conclusion is not caused by a shortage of quadratic characters.  Let
`Y=H^A`, prescribe arbitrary signs `epsilon_p` for every odd `p<=Y`, with
`epsilon_p=1` for `p<=H`, and put

```text
M=8 product_(3<=p<=Y)p.                                    (3.6)
```

The residue classes `a mod M` satisfying

```text
a=1 mod 8,             (a/p)=epsilon_p                     (3.7)
```

occupy the exact proportion `2^(-pi(Y)+O(1))` of the reduced
classes.  Taking `X=M^B`, `B>2`, squarefree counting in this union gives

```text
#{d<=X:d squarefree and chi_d(p)=epsilon_p for p<=Y}
 >> X/[2^pi(Y) log Y]=X^(1-o(1)).                           (3.8)
```

Every such `d=1 mod 8` is a positive fundamental discriminant and
`log d=O(Y)`.  A fixed-window real-character zero-density bound has exceptional
count `O(X^(a(sigma)+epsilon))`, where `a(sigma)<1` for every fixed
`sigma>1/2`.  Hence every prescribed complete sign pattern through `Y` has,
for large `Y`, a realization whose quadratic `L`-function is zero-free on the
fixed localization disc.  Corollary 3.1 then forces that realization to have
an `F_chi=2` point.  Finite sign entropy and denominator selection succeed;
the obstruction is the connected analytic transition across `Re(s)=1`.

The cubic statement is identical after also excluding the varying numerator
zeros.  If all auxiliary numerator and denominator factors are zero-free in
`Omega`, the zeros of the quotient are again the fixed zeta divisor, so a
point `F=2` is forced.

Equivalently, there is an `epsilon_0>0`, depending only on the fixed domain,
cap, and zeta divisor, such that every nonvanishing `g in Hol(Omega)` for
which `zeta-2g` is also nonvanishing satisfies

```text
sup_(s in V)|zeta(s)/g(s)-1|>=epsilon_0.                    (3.9)
```

Otherwise a sequence violating (3.6) would contradict Theorem 2.1.  Thus
there is no admissible universality target whose quotient has the required
vanishing head on the right cap and omits `2` on the full connected domain.

## 4. R153's fixed-value condition is impossible

For the R153 root-of-unity filter, the artificial values are

```text
F=1+omega,             omega^q=1, omega!=-1.                (4.1)
```

When `q>=4` is even, this set contains at least two fixed distinct values.
Theorem 1.1 rules out simultaneous avoidance as `H -> infinity`, provided
the quotient is holomorphic and retains the fixed zeta zero.

The only even case with one artificial value is `q=2`, but it cannot meet
R153's localization inequalities.  In the notation of that report, a
necessary condition would be

```text
r log(R/d)>log(2d/r).                                      (4.2)
```

Yet `R<r+eta`, `d=r+delta`, and `0<delta<eta<1/2` give

```text
r log(R/d)<R-d<eta-delta<1/2<log 2<log(2d/r).               (4.3)
```

Thus every root-of-unity amplifier strong enough to cross the exponent gate
has at least two values and is covered by Theorem 1.1.  The conditional
hypothesis in R153 Theorem 3.1 is internally incompatible with retaining the
source zero along `H -> infinity`.

## 5. The repeated-pole one-value workaround

There is a real algebraic loophole in the distinct-value count.  For even
`q`, put `U=F-1` and

```text
A_q(s)=2^(q-1)(-U'(s))U(s)^(q-1)
       /[(1+U(s))(1-U(s))^(q-1)].                           (5.1)
```

Since

```text
1/[(1+x)(1-x)^(q-1)]
 =1/[(1-x^2)(1-x)^(q-2)],                                  (5.2)
```

the Taylor coefficients in (5.1) are nonnegative.  If `U` has Dirichlet
support beyond `H`, then `A_q` has support beyond `H^q`.  Its residue at an
`F`-zero is `+1`, and its only artificial finite value is `F=2`.

The price is that `F=2` is a pole of order `q-1`, not a logarithmic pole.
Writing `C=2^(q-1)`, partial fractions give

```text
A_q=F'/F+(C-1)F'/(F-2)+d[S_q(F)]/ds,                        (5.3)
```

where `S_q` is rational, regular at `0` and infinity, and has a pole of
order `q-2` at `2` when `q>2`.  Ordinary zero counting controls the first
two logarithmic derivatives, but not the high jet of the exact-derivative
term.  More decisively, if the value `2` is avoided so that (5.1) has no
artificial pole in the localization disc, Theorem 2.1 contradicts the fixed
zeta zero divisor.  Hence collapsing the artificial values does not restore
the R153 closure.

This also explains why multiplicity is not a free substitute for distinct
logarithmic divisors.  A true logarithmic derivative of `(F-2)^m` is only
`mF'/(F-2)` and supplies one Taylor condition.  Higher Taylor cancellation
at the same value requires the non-logarithmic pole in (5.3), whose regular
germ is uncontrolled.

## 6. Quantitative truncated-zeta reality check

The normal-family theorem decides avoidance.  The deterministic common mode
also quantifies what typical quotients do instead.  Set

```text
E_H(s)=zeta(s) product_(p<=H)(1-p^(-s))
       =1+sum_(n>H)u_H(n)n^(-s),       u_H(n)>=0.            (6.1)
```

Let

```text
c=1+r+i gamma,
d<R_0<R_1<r+eta,
alpha_0=R_0-r>0,                                            (6.2)
```

with fixed radii chosen away from the fixed zeta divisor.  On the left arc
`s=c+R_0 exp(i theta)`, the prime number theorem gives, uniformly on the
Laplace-scale neighborhood of `theta=pi`,

```text
sum_(p<=H)p^(-s)
 =H^(1-s)/[(1-s)log H]
  +O(H^(1-Re(s))/(log H)^2).                                (6.3)
```

The amplitude is concentrated on an angular interval of width
`(log H)^(-1/2)`, while its phase oscillates at speed comparable to `log H`.
Integrating the positive part over that arc yields

```text
m_c(R_0,E_H)
 >>_(geometry,gamma) H^(alpha_0)/(log H)^(3/2).              (6.4)
```

The assertion is an integrated lower bound, not a pointwise bound, and is
not uniform as `gamma` varies.  Radius slack is essential.  A corresponding
upper bound at `R_1`, followed by the disc second main theorem, shows that
for any three fixed distinct nonzero values `a_1,a_2,a_3`,

```text
sum_(j=1)^3 Nbar_c(R_1,a_j;E_H)
 >> H^(alpha_0)/(log H)^(3/2).                              (6.5)
```

Here `Nbar` is the reduced distinct-point count.  Since `E_H ->1` on the
right control disc, fixed mixed values different from `1` contribute no
central points for large `H`; (6.5) is genuine outer mixed-point abundance.

Every R148 cubic quotient factors exactly as

```text
F_K=E_H R_(K,H),
R_(K,H)=L(s,chi_D)/
        [L(s,Std_K) product_(p<=H)(1-p^(-s))].              (6.6)
```

If `F_K` omitted three fixed values on the larger disc, normality would give
bounded characteristic on every compactly smaller disc.  The product and
reciprocal characteristic inequalities would then force

```text
T_c(R_0,R_(K,H))
 >> H^(alpha_0)/(log H)^(3/2).                              (6.7)
```

Thus avoidance would require the residual factor to cancel a polynomially
large deterministic characteristic.  Equation (6.7) is a characteristic
statement; it does not by itself count residual zeros or poles.  The usual
mean-zero Frobenius model instead predicts `R_(K,H)` is typically close to
`1` on compacta in `Re(s)>1/2`.  That last prediction is heuristic until a
growing-head conditioned family-moment theorem is proved, but it correctly
warns that ordinary moment selection preserves rather than cancels the
truncated-zeta skeleton.

## 7. Literature and the surviving target

The separate audit
[`experts/mixed-apoint-literature-audit.md`](experts/mixed-apoint-literature-audit.md)
finds no conductor-aspect theorem which controls zeros of

```text
N_K-cD_K                                                   (7.1)
```

in a prescribed fixed-height disc after the growing no-inert head.  Artin
zero density applies to the genuine Euler denominator.  Righetti's theorem
does apply to (7.1), but is a height-aspect theorem for each fixed field, with
field-dependent thresholds; it proves global abundance, not fixed-window
uniformity.

R155 sharpens the interpretation of that gap.  A theorem selecting all mixed
factors to be zero-free cannot exist under the retained-zero hypothesis.  A
successful continuation must instead include the forced mixed points and
prove a signed joint estimate showing that their weighted reciprocal powers
cannot cancel the target contribution.  Equivalently, it must exploit
arithmetic correlation in the actual mixed divisor, not absolute divisor
counting, ordinary family moments, or another scalar value-avoidance filter.

This is a decisive closure of the R153--R154 avoidance program.  It is not a
proof that zeta has, or does not have, a fixed zero-free strip.
