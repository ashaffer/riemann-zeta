# Weighted rough-transition residue-dispersion gate

**Date:** 2026-08-13  
**Status:** exact post-`q` reduction and exact closing theorems; published
fundamental-lemma/dispersion inputs do not prove the required power.

## Verdict

The post-`q` SPF tail has a cleaner exact object than the per-prime square
function.  On every retained terminal-prime edge, let `nu_z` be the atomic
Voronoi/trapezoid mass measure of the integers with no prime factor at most
`z`.  Then, with the harmless convention that the cutoff is moved to the
next prime,

```text
sum_(P<p<=2P, p>q) D_p
   = integral e_q(a n)
       d[nu_(max(2P,q))-nu_(max(P,q))].               (0.1)
```

This identity holds **before** Cauchy, the large sieve, or a triangle
inequality.  Thus all cross-`p` covariance in a dyadic band is exactly the
residue discrepancy of one increment of rough Voronoi measures.  The
per-`p` square-function estimate loses this covariance and therefore stops
at the critical `Y^(1+o(1))` aggregate.

Deleting every `q`-multiple first does not disturb (0.1), even for composite
`q`: if `p>q` and `q|n`, then a prime divisor of `q` is below `p`, so `n` is
already absent from the `p`-rough set.  The `q`-first and ordinary SPF flows
are literally identical at every stage `p>q`.

For a curvature block `I`, reduce the signed measure in (0.1) modulo its
selected `q_I` and call the vector `Delta_(I,P)`.  Two precise sufficient
theorems now emerge.  For any fixed `delta>0`, either

```text
sum_(I,P) q_I/H_I sum_(r mod q_I)|Delta_(I,P)(r)|^2
        <<Y^(1-2 kappa-2 delta+o(1)),                 (0.2)
```

or the fourth-moment version in (5.5) proves

```text
sum_I |R_(>q_I,I)| <<Y^(1-kappa-delta+o(1)).          (0.3)
```

Here `sum_I H_I<<Y`, dyadic-band logarithms are absorbed in `Y^o(1)`, and
one may take the hostile carrier bill

```text
kappa=0.01974048259....                               (0.4)
```

The reduction is theorem-grade.  The implication from (0.2) is exact, but
(0.2) cannot hold uniformly for every arbitrary legal blockwise denominator:
the injective top-scale selector in Section 4.1 forces energy
`Y^(1-o(1))`.  A theorem restricted to the denominators actually produced
by one common height is not ruled out.  The `L4` counterpart remains the
clean live moment target.

All identities here concern the frozen constant-amplitude trapezoid rule on
the retained terminal-prime edges.  The separate smooth-amplitude,
phase-freezing, discarded-long-edge, and curvature-block-boundary ledgers
must still be reattached in the antenna argument; none is silently absorbed
into `Delta_(I,P)`.

An optimistic whole-shell fundamental-lemma calculation already has fixed

```text
s=(1-u-b)/u,      p=Y^u, q=Y^b.                      (0.5)
```

At the first band `u=b`, this ranges only from `4.50618...` at `b=.1537`
to `2.030303...` at the exact top endpoint `b=33/133=.2481203...`.  Fixed
`s` gives fixed linear-sieve upper and
lower constants, not a relative `Y^(-delta)` discrepancy.  The lower sieve
is positive only for

```text
u<(1-b)/3,
```

namely `u<.2821` at the bottom and `u<.250626...` at the top.  On an actual
critical block `H=Y^h`, fixing both `p` and one residue leaves only
`Y^(h-u-b)` cofactors, so the local parameter is `(h-u-b)/u`; it is already
negative throughout the first band when `h<=33/133` and `b>=.1537`.  Any
successful argument must therefore average in `p`, in the blocks, or both.

No published no-go theorem rules out (0.2).  The definitive negative result
here is narrower: the ordinary fundamental lemma, coefficient-blind gap
energy, and the currently published separated-coefficient dispersion
theorems do not imply it.

## 1. Why the `q`-first reorder leaves the later rough flow unchanged

Fix an arbitrary integer denominator `q>=2`, not necessarily prime.  Delete
all interior `q`-multiples from the integer lattice.  Then run the remaining
composites through increasing least-prime-factor stages.

Let `p>q` be prime.  If `q|n`, choose a prime `ell|q`.  Then

```text
P^-(n)<=ell<=q<p.                                     (1.1)
```

Consequently no `q`-multiple belongs to the active `p`-rough set.  By the
time the ordinary SPF flow reaches `p`, it has removed exactly the same
`q`-multiples that were removed at the first step.  Induction through the
SPF stages gives

```text
active set before p in q-first flow
 =active set before p in ordinary SPF flow,          p>q,              (1.2)
```

and the stage transport measures are identical as well.  This is an exact
set identity, not an estimate.

The price is also exact.  The stages `p<q` are changed by the punctures and
form a separate pre-`q` prefix.  This report closes neither that prefix nor
the full prime statistic; it isolates the later tail requested here.

## 2. Canonical simultaneous SPF-stage transport

Work inside one retained short edge between permanent terminal-prime
endpoints.  Write `nu_z` for the measure after all SPF stages `ell<=z`.
Just before the stage `p`, let

```text
R_(p-)={active integers with P^-(n)>=p}.
```

At the stage labelled by `p`, delete

```text
D_p={n in R_(p-):P^-(n)=p}.
```

The survivors are the rough set at the next prime cutoff.  Consider one
maximal run of deleted nodes

```text
l<x_1<...<x_k<r,
```

where `l,r` survive.  If `T_B(f)` denotes the trapezoid rule on an ordered
set `B`, direct subtraction gives

```text
2[T_(after)-T_(before)](f)
 =(r-x_1)f(l)+(x_k-l)f(r)
  -sum_(j=1)^k (x_(j+1)-x_(j-1))f(x_j),              (2.1)
```

with `x_0=l,x_(k+1)=r`.  The two positive endpoint coefficients and the
negative centre coefficients have the same total mass.  Summing (2.1) over
all components defines positive measures `mu_p^+,mu_p^-` with

```text
nu_p-nu_(p-)=mu_p^+-mu_p^-,
mu_p^+(R)=mu_p^-(R).                                 (2.2)
```

For a singleton component, writing `A=x-l,B=r-x`, (2.1) is the familiar
exact charge

```text
D_x(a/q)
 =e_q(ax)/2 [B e_q(-aA)+A e_q(aB)-(A+B)].            (2.3)
```

Formula (2.1) is preferable to imposing nonadjacency: it remains exact when
several `p`-centres are consecutive in the rough order.

If `p>q`, every atom in (2.1) is a unit modulo `q`.  Indeed, a common prime
factor with `q` would be below `p`, contradicting membership in `R_(p-)`.

## 3. The dyadic band telescopes before any loss

Sum (2.2) over all prime stages in a dyadic interval.  Every intermediate
rough measure cancels:

```text
Sigma_(I,P)
 :=sum_(max(P,q_I)<p<=2P) (nu_p-nu_(p-))
  =nu_(max(2P,q_I))-nu_(max(P,q_I)).                  (3.1)
```

Cutoff endpoints in (3.1) mean the rough set after all primes at most
the displayed real cutoff have been deleted.  This convention removes any
ambiguity when `q_I` or `P` is not prime.

Both measures on the right have total mass equal to the retained physical
edge length.  Hence

```text
Sigma_(I,P)(R)=0.                                    (3.2)
```

Reduce (3.1) modulo `q_I`:

```text
Delta_(I,P)(r)
 =Sigma_(I,P)({n:n=r mod q_I}),
D_(I,P)(a_I)=sum_(r mod q_I)Delta_(I,P)(r)e_(q_I)(a_I r).  (3.3)
```

Then `sum_r Delta_(I,P)(r)=0`, its support lies in the unit residues, and
`D_(I,P)(a_I)` is exactly the dyadic post-`q_I` charge on `I`.  No factor
`sqrt(#p)` appears.

Equivalently, if `L_I` is the retained length and

```text
E_(I,z,q)(r)=nu_(I,z)(r)-L_I/phi(q),     (r,q)=1,     (3.4)
```

with zero mass assigned to nonunits, then

```text
Delta_(I,P)=E_(I,max(2P,q_I),q_I)
             -E_(I,max(P,q_I),q_I).                  (3.5)
```

Thus a weighted rough-number-in-AP theorem for the Voronoi measures is a
direct sufficient input.  Ordinary counts of rough centres are not the same
quantity: `nu_z` weights a centre by half the sum of its two neighboring
rough gaps.

## 4. Exact selector-stable `L2` closing theorem

Finite Parseval gives

```text
sum_(a mod q_I)|D_(I,P)(a)|^2
 =q_I sum_(r mod q_I)|Delta_(I,P)(r)|^2.              (4.1)
```

Therefore the selected numerator satisfies the same right-side upper bound.
There are `O(log Y)` dyadic SPF bands, so

```text
|R_(>q_I,I)|^2
 <<Y^o(1) sum_P q_I sum_r|Delta_(I,P)(r)|^2.          (4.2)
```

Weighted Cauchy over the curvature blocks yields

```text
sum_I |R_(>q_I,I)|
 <=(sum_I H_I)^(1/2)
   [sum_I |R_(>q_I,I)|^2/H_I]^(1/2).                 (4.3)
```

Since `sum_I H_I<<Y`, (0.2) implies (0.3).  The exponent calculation is
exact:

```text
1/2 + [1-2 kappa-2 delta]/2=1-kappa-delta.           (4.4)
```

A slightly stronger but perhaps more recognizable sufficient hypothesis is

```text
sum_(I,P) q_I/H_I sum_(r units)
  ( |E_(I,max(2P,q_I),q_I)(r)|^2
   +|E_(I,max(P,q_I),q_I)(r)|^2 )
 <<Y^(1-2 kappa-2 delta+o(1)).                        (4.5)
```

It implies (0.2) by `(x-y)^2<=2x^2+2y^2`.

This is the exact weighted rough-number-in-AP theorem that would close the
finite-group `L2` route.  It is selector-stable: the denominator and
numerator may vary arbitrarily from block to block inside the legal range.

### 4.1 The selector-uniform `L2` input is false at the injective endpoint

The implication above is useful bookkeeping, but its hypothesis is too
strong as a theorem uniform over **arbitrary** legal selectors.  Take

```text
h=33/133,             q=floor(Y^h),                 (4.6)
```

at the top curvature scale `T=Y^(200/133)`, for which
`H=Y/sqrt(T)=Y^h`.  Thus `q` is range-legal (`Y^beta<q<=H`), but this
choice alone does **not** show that `q` is the reduced Dirichlet denominator
selected on any block by that height.  Partition the shell into half-open
blocks containing `q` consecutive
integer sites, so `H_I=q+O(1)`.  Use the already audited convention which
discards terminal-prime edges crossing a block boundary.  Every atomic site
of a retained edge in one block then has a distinct residue modulo `q`.
Consequently residue reduction is injective and, for the physical
coefficient sequence `c_(I,P)` of a band increment,

```text
sum_(r mod q)|Delta_(I,P)(r)|^2
 =sum_(n in I)|c_(I,P)(n)|^2.                       (4.7)
```

Every centre deleted between the two band cutoffs has negative coefficient
equal to its mass in the initial Voronoi measure.  Its two active-neighbor
distances are positive integers, so that mass is at least one.  Hence

```text
sum_(I,P)||Delta_(I,P)||_2^2
 >=#{retained post-q composite centres}.            (4.8)
```

The right side is `>>Y/log Y`.  For example, restrict to semiprimes `pr` with

```text
Y^.30<p<=Y^.31,       Y<pr<=2Y,                     (4.9)
```

and `r` prime.  The prime number theorem and the prime reciprocal sum give
`>>Y/log Y` such integers; both factors exceed `q`, and each is deleted in
exactly one post-`q` band.  The Gafni--Tao long-edge removal covers only

```text
O(Y^(63827/65000+epsilon))=o(Y/log Y)                (4.10)
```

integer sites.  The `O(Y/H)` crossing edges cover at most

```text
O(Y^(1-h+797/5000))=O(Y^(.911280...))=o(Y/log Y).   (4.11)
```

Thus (4.8) survives the exact retained-edge convention.  Since `q/H_I=1+o(1)`,
the left side of (0.2) is `>>Y/log Y`, whereas even at `delta=0` its proposed
right side is

```text
Y^(1-2kappa+o(1))=Y^(.96051903482...+o(1)).          (4.12)
```

This contradiction is unconditional for the range-uniform, frozen
hard-block statement.  It rules out (0.2) as an arbitrary-selector theorem,
not its deterministic implication and not a version restricted to the
denominators actually produced by one common height.  Nor does the argument
as written prove the same lower bound after an arbitrary smooth/tent taper:
that would require a semiprime lower bound on a region where the taper is
bounded below.  It also does not rule out the fourth-moment route: the fourth
moment can distinguish a diffuse family of Fourier coefficients from one
exceptional coefficient, whereas the full `L2` energy pays for all physical
diagonal mass.

## 5. Exact `L4` alternative

For a residue vector `Delta` define its cyclic correlation

```text
C_Delta(s)=sum_(r mod q)Delta(r) conjugate(Delta(r+s)).                (5.1)
```

Finite Fourier expansion gives

```text
sum_(a mod q)|Delta_hat(a)|^4
 =q sum_(s mod q)|C_Delta(s)|^2.                     (5.2)
```

Weighted Holder over the physical blocks gives

```text
sum_I |R_(>q_I,I)|
 <=(sum_I H_I)^(3/4)
   [sum_I |R_(>q_I,I)|^4/H_I^3]^(1/4).               (5.3)
```

Band recombination costs only `O(log^3 Y)`.  Hence the fourth-moment theorem

```text
sum_(I,P) q_I/H_I^3
 sum_(s mod q_I)|C_(Delta_(I,P))(s)|^2
 <<Y^(1-4 kappa-4 delta+o(1))                         (5.4)
```

also proves (0.3), because

```text
3/4+[1-4 kappa-4 delta]/4=1-kappa-delta.             (5.5)
```

This is not a consequence of the gap square.  It is an additive-energy
theorem for a signed, gap-weighted residue vector.  The coherent deletion
model in the companion nonresonant-SPF report shows that near-linear gap
energy and correct per-`p` count caps can coexist with a macroscopic selected
Fourier coefficient.

### 5.1 Exact coefficient-blind benchmark and closure deficit

Write the atomic coefficient sequence of `Sigma_(I,P)` as `c_(I,P)(n)`, so
that `Delta_(I,P)` is obtained by summing `c_(I,P)` in residue classes.  Its
support has length at most `H_I`.  Since `q_I<=H_I`, Cauchy inside each
residue class gives the complete-modulus large-sieve bound

```text
q_I ||Delta_(I,P)||_2^2
 <=(H_I+q_I)||c_(I,P)||_2^2
 <=2H_I||c_(I,P)||_2^2.                              (5.6)
```

Every retained terminal-prime edge has length at most

```text
G=Y^theta,                  theta=797/5000=.1594.     (5.7)
```

On an edge of length `g<=G`, the atoms of either positive Voronoi measure
have mass at most `g` and total mass `g`.  Its squared atomic mass is
therefore at most `g^2<=Gg`.  Taking the difference of the two measures and
summing the bounded-overlap terminal edges and the `O(log Y)` bands gives

```text
sum_(I,P)||c_(I,P)||_2^2 <<YG Y^o(1)
                              =Y^(1+theta+o(1)).      (5.8)
```

Thus (5.6) proves only

```text
sum_(I,P) q_I/H_I ||Delta_(I,P)||_2^2
 <<Y^(1+theta+o(1)).                                  (5.9)
```

For the fourth moment, `||c_(I,P)||_1<=2H_I`.  Hence

```text
sum_a |Delta_hat_(I,P)(a)|^4
 <=||c_(I,P)||_1^2 sum_a|Delta_hat_(I,P)(a)|^2
 <=8H_I^3||c_(I,P)||_2^2.                            (5.10)
```

Together with (5.2), this bounds the left side of the desired `L4`
hypothesis (5.4) by the same `Y^(1+theta+o(1))`.

The currently proved coefficient-blind full-tail estimates therefore miss
the closing inputs by the exact exponent gaps

```text
L2: theta+2kappa=.19888096518...,
L4: theta+4kappa=.23836193036....                    (5.11)
```

The new near-linear rough-gap square improves (5.8) in the early cutoff
range where both moving rough sets are covered, but not throughout the full
tail.  Even optimistically granting
`sum ||c_(I,P)||_2^2=Y^(1+o(1))` for every band, coefficient-blind large
sieves still miss the targets by

```text
2kappa=.03948096518... in L2,
4kappa=.07896193036... in L4.                        (5.12)
```

This is the fixed-power deficit which genuine residue dispersion must repay.

## 6. Fundamental-lemma frontier

First discard localization and pretend one fixed denominator is used on the
whole `Y`-shell.  A deleted centre at stage `p=Y^u` has

```text
x=pm,       m asyp Y^(1-u),       P^-(m)>=p.          (6.1)
```

Fixing `x=r mod q`, `q=Y^b`, fixes `m` to one residue modulo `q`.  The
cofactor progression has `Y^(1-u-b)` candidates.  The largest elementary
sieve level therefore gives

```text
s_shell=(1-u-b)/u.                                   (6.2)
```

At `u=b`:

| `b` | `s_shell=1/b-2` | lower-sieve range `u<(1-b)/3` |
|---:|---:|---:|
| `.1537` | `4.5061808718...` | `u<.2821` |
| `33/133=.2481203007...` | `67/33=2.0303030303...` | `u<100/399=.2506265664...` |

The dimension-one lower linear-sieve function is positive only for `s>2`;
the usual upper-sieve range starts at `s>1`.  More importantly, the
fundamental lemma gives a relative `1+o(1)` only when `s` tends to infinity.
Here `s` is a fixed number.  The gap between the upper and lower sieve
functions is therefore a fixed proportion, never the `Y^(-2kappa)`-scale
information demanded by (0.2).

Localization is worse.  In a block `H=Y^h`, after fixing `p` and a residue,
the cofactor progression has only

```text
H/(pq)=Y^(h-u-b)                                      (6.3)
```

candidates, with formal parameter

```text
s_block=(h-u-b)/u.                                   (6.4)
```

For `h<=33/133`, `u>=b`, and `.1537<=b<=33/133`, this is negative already in
the first band; at the two extreme first-band points it ranges from
`-.385684...` to `-1`.  Thus one cannot apply a blockwise one-`p`, one-residue
fundamental lemma at all.  The target must exploit an average over the many
`p` labels, the many disjoint blocks, or the exact band telescope (3.1).

Finally, even an optimal theorem for the **unweighted** count in (6.1) would
not imply (4.5).  The Voronoi weight at `n` is

```text
[g_-(n;z)+g_+(n;z)]/2,                               (6.5)
```

and its residue records the first rough survivor on both sides.  Expanding a
gap as a sum of empty-prefix indicators turns (6.5) into correlated shifted
sieve conditions of growing length.  Standard one-dimensional fundamental
lemmas do not control that joint first-return law with a signed power error.

## 7. What the primary literature actually supplies

The following audit used theorem statements and source, not title-level
analogy.

1. Maynard's [*Primes in arithmetic progressions to large moduli II:
   Well-factorable estimates*](https://arxiv.org/abs/2006.07088), Lemma 5.4,
   gives a consequence of the fundamental lemma for numbers free of primes
   below

   ```text
   z_0=x^(1/(loglog x)^3),
   ```

   uniformly when the progression contains a power margin.  This is exactly
   the `s->infinity` regime.  It does not cover the fixed-power cutoff
   `p=Y^u` in (6.1).  The paper's main estimates average well-factorable
   modulus weights and use separated convolution coefficients.

2. Maynard's [*Primes in arithmetic progressions to large moduli III:
   Uniform residue classes*](https://arxiv.org/abs/2006.08250) is genuinely
   uniform in the residue classes inside its modulus averages.  Its main
   Type-II propositions have separated coefficients `alpha_n beta_m` and
   sum over factorizable moduli; its rough-number lemma is an unlocalized
   Buchstab asymptotic, and its separation lemma removes finitely many
   product inequalities.  None retains the neighboring-gap/first-survivor
   weight (6.5), and a supremum over residue classes inside an average over
   moduli is not a pointwise theorem for the blockwise selected modulus.

3. Bombieri--Friedlander--Iwaniec,
   [*Primes in arithmetic progressions to large moduli II*](https://doi.org/10.1007/BF01458321),
   and the later well-factorable refinements are dispersion theorems for
   modulus averages with factorable arithmetic coefficients.  They are
   useful after a bilinear separation has been proved.  The matrix assigning
   a centre to its two nearest rough neighbors is not such a separation.

4. Bettin--Chandee,
   [*Trilinear forms with Kloosterman fractions*](https://arxiv.org/abs/1502.00769),
   permits arbitrary one-dimensional sequences in a product
   `alpha_m beta_n nu_a`.  “Arbitrary” does not mean an arbitrary joint
   coefficient `c_(p,m)` determined by both neighboring rough gaps.  The
   April 2026 preprint of Wright,
   [*Trilinear Kloosterman fractions I: partially fixed moduli and unbalanced
   convolutions*](https://arxiv.org/abs/2604.25177), improves the fixed-factor
   and unbalanced ranges but retains the same separated-convolution and
   modulus-average architecture.  It does not state (0.2).

5. Friedlander--Iwaniec,
   [*On the Bombieri--Davenport large sieve inequalities*](https://doi.org/10.4171/RLM/1079)
   (published February 2026), improves the large-sieve constant for special
   restricted-support or almost-prime coefficients.  Its Theorem 2.2 gains a
   factor of order `1/log(N/Q^2)` under a local small-prime energy condition
   and averages all characters/moduli in range, under the additional
   hypothesis `8Q^2<=N`.  On one target curvature block, `N asymp H=Y^h`
   and `Q asymp q=Y^b`, while `2b>h` everywhere in the legal range, so this
   theorem is not even in range.  Even if that range mismatch were removed,
   its gain is logarithmic, not the fixed `Y^(-2kappa)` gain in (0.2), and
   the required local energy for the signed Voronoi-transition coefficients
   has not been proved.

6. Montgomery--Vaughan's
   [*The large sieve*](https://doi.org/10.1112/S0025579300004708) controls an
   average over separated frequencies.  Equations (4.1) and (5.2) are the
   exact finite-group versions relevant here.  A height selector may choose
   an exceptional numerator, so frequency averaging alone is not a uniform
   selected-coefficient theorem.

7. Matomaki's
   [*Almost primes in almost all very short intervals*](https://arxiv.org/abs/2012.11565)
   is the input behind the proved rough-gap second moment.  It controls
   empty intervals and prescribed vector-sieve remainders.  It does not
   resolve rough Voronoi masses into residue classes modulo a varying
   selected `q`.

8. Xuan's
   [*Integers free of small prime factors in arithmetic progressions*](https://doi.org/10.1017/S0027763000007212)
   records two especially relevant boundaries.  First, it quotes Wolke's
   [Bombieri--Vinogradov theorem for sifted counts](https://doi.org/10.1007/BF01433411):

   ```text
   sum_(q<=x^(1/2)log^(-B)) max_((a,q)=1) max_(z<=x)
     |Phi(z,y;a,q)-Phi_q(z,y)/phi(q)| <<x log^(-A).    (7.1)
   ```

   This is uniform in the unweighted rough-count numerator and interval
   prefix, but averages the moduli and saves only logarithms.  Even if every
   selected block used a distinct denominator, `Y log^(-A)` is larger than
   `Y^(1-kappa)` for every fixed `A` once `Y` is large.  Repeated selected
   denominators only add a multiplicity loss.  At the top curvature scale
   there are `K=Y^(100/133+o(1))` blocks but only
   `O(H)=Y^(33/133+o(1))` possible denominators, so reuse cannot be removed
   by choosing primitive fractions.  More fundamentally, (7.1)
   does not contain the Voronoi weight (6.5), so partial summation does not
   turn it into (4.5).

   Second, Xuan's individual character/AP theorems allow only

   ```text
   q<=exp(c log y/log_2 x)=x^o(1)                    (7.2)
   ```

   at a fixed-power roughness cutoff, and explicitly retain a possible
   exceptional-real-character term before the polylogarithmic-modulus
   corollary.  Thus they do not reach
   `q=Y^b`, `.1537<=b<=33/133=.2481203...`.  The common-height or primitive
   moment selector does not upgrade either the logarithmic saving in (7.1)
   or the subpolynomial range in (7.2) to the fixed-power, gap-weighted
   theorem (0.2).  Wolke averages each modulus once and takes a maximum over
   its numerators; it supplies no sum over the many disjoint blocks or over
   the primitive numerator--block pairs sharing one denominator.

9. Bazin's July 2026 preprint,
   [*A Bombieri--Vinogradov theorem for exponential sums over products of
   k primes*](https://arxiv.org/abs/2607.15137), is stronger in one relevant
   surrogate.  His Theorem 8 and Lemma 10 imply, for a separated dyadic
   semiprime convolution at an exact rational and `q=Y^b`, a global
   modulus-average power saving

   ```text
   min{b/2,(u-b)/2,(1-3b)/2}>=17/399=.0426065...,
   ```

   when `p=Y^u`, `u>=1/3`, and `b<=33/133`.  This exceeds the carrier bill,
   so the late separated semiprime surrogate is not exponent-starved.
   Bazin's theorem nevertheless concerns whole prefixes and separated
   Dirichlet convolutions.  Fourier localization to a block of length `H`
   invokes his term `YQ^(3/2)H^(-1/2)`.  The nearest-survivor coefficient is
   globally joint; on the unique-large-factor range `u<=1-h` it can actually
   be anchored and absorbed into one block-dependent factor `beta_I(r)`.
   Bazin's global terms then remain far above the required
   `H Y^(-kappa)` block scale.  The exact ledger and applicability audit are in
   `ZETA23-LATE-BUCHSTAB-SEMIPRIME-DISPERSION-GATE-2026-08-13.md`.

These are all useful ingredients.  None is a theorem for (4.5), and none is
a no-go theorem against it.

## 8. Strongest live continuation

The exact reduction suggests a fail-fast order.

1. **Attack the band increment, not individual primes.**  Work directly with
   `nu_(2P)-nu_P`; any proof which first takes absolute values in `p` has
   already discarded the only visible route around the square-function
   barrier.
2. **Start with multiplicative-character energy.**  Because all atoms are
   units modulo `q`, (4.5) is equivalent, up to the standard `q/phi(q)`
   factor, to a mean square over nonprincipal characters of the two rough
   Voronoi measures.  This is the native interface for dispersion.
3. **Separate the first-return weight or prove it is low rank.**  A viable
   lemma would approximate (6.5), after dyadic gap decomposition, by a
   bounded sum of factorable `p,m,h` coefficients with total squared error
   `Y^(-2kappa-delta)`.  A merely logarithmic or fixed-relative error cannot
   close the route.
4. **Exploit the late Buchstab simplification.**  For `u>1/3` the cofactor
   `m` in (6.1) is prime; for `1/4<u<=1/3` it has at most two prime factors.
   Bazin's explicit estimate proves that the separated late-band surrogate
   has enough global exponent.  The live tests are now sharply identified:
   short-block localization and a power-accurate low-rank separation of the
   first-return weight.  The early band remains the true fixed-`s`
   obstruction.
5. **Keep the pre-`q` prefix separate.**  Even a proof of (0.2) settles only
   `R_(>q)`.  The punctured `p<q` prefix created by the q-first order still
   needs its own estimate or cancellation with another exact term.

## 9. Truth boundary

```text
q-first and ordinary SPF flows coincide for p>q:      PROVED
simultaneous component transport formula (2.1):       PROVED
dyadic band telescope (3.1):                          PROVED
finite Parseval and fourth-moment identities:         PROVED
selector-stable L2 implication (0.2)=>(0.3):          PROVED
L2 input (0.2) uniformly for arbitrary selectors:    FALSE
L2 input restricted to actual common-height choices: OPEN
selector-stable L4 implication (5.4)=>(0.3):          PROVED
coefficient-blind full-tail exponent 1+theta:         PROVED
current L2/L4 closure deficits (5.11):                EXACT
whole-shell fixed-s frontier (6.2):                   PROVED
critical per-block fundamental-lemma level:           ABSENT
fundamental lemma alone gives a fixed power:          FALSE
published dispersion accepts the exact gap matrix:    FALSE AS SCOPE
published no-go theorem rules out (0.2):              NONE FOUND
weighted rough-Voronoi selector-uniform L2 theorem:   RULED OUT
weighted rough-Voronoi L4 theorem:                    OPEN
post-q SPF tail power saving:                          CONDITIONAL ON THAT THEOREM
punctured pre-q prefix:                                OPEN
full antenna / zero-free strip:                        NOT CLAIMED
```

## 10. Reproduction

```bash
PYTHONPATH=src python3 -m unittest -v src/test_weighted_rough_transition_gate.py
python3 results/verify_zeta23_weighted_rough_transition_gate.py
```

The checker verifies the exact component formula, adjacent-deletion runs,
q-first invariance for every finite stage `p>q`, the dyadic telescope, mass
balance, finite `L2/L4` identities, both closure exponents, and the rational
linear-sieve frontiers.
