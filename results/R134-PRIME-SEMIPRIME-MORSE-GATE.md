# Prime--semiprime Morse gate

Status: fail-fast theorem proved, 2026-08-08.  A prime can be replaced by an
extremely nearby semiprime with a power-saving relative error, so geometric
boundary motion is not the first obstruction.  The obstruction is
recognition.  Every background-independent first-active codebook of
`p <-> qr` rewrites has support components of size at most two.  A uniform
sieve then leaves a positive proportion of the odd squarefree collar with no
available rewrite, even when the codebook depends on `N`.  This closes that
precise codebook/discrete-Morse-style class, not arbitrary stateful sequential
matchings and not the fixed-strip problem.

## 1. Target and predecessor boundary

Put

```text
S_N={m:N/2<m<=N, m odd and squarefree}.
```

The exact collar identity is

```text
M(N)=sum_(m in S_N) mu(m).                          (1)
```

If a deterministic involution pairs all but `R(N)` members of `S_N` and every
pair has opposite Mobius sign, then

```text
|M(N)|<=R(N).                                      (2)
```

Thus `R(N)=O(N^(1-delta))` would give a fixed zero-free half-plane, and the
RH-scale `R(N)=O_epsilon(N^(1/2+epsilon))` would imply RH.  Maximum matching
does not estimate `R(N)`: after the smaller parity class is saturated, its
deficiency is exactly `|M(N)|`.  This is the boundary established in
`MOBIUS-BOUNDARY-EXCHANGE-GATE-2026-08.md` and
`MOBIUS-GREEDY-DEPENDENCY-VERDICT-2026-08.md`.

The present question is narrower and constructive:

> Can a hierarchical dictionary of near-identity rewrites replace a prime
> `p` by two primes `q,r`, with `qr/p` extremely close to one, in a way that
> is recognizable from both endpoints and leaves only a power-saving
> boundary?

The answer below is no for the natural raw first-active codebook class.
The word “Morse” here means a prioritized sign-cancellation rule only.  As in
the predecessor audit, `{C,p}` and `{C,q,r}` are incomparable faces, so these
are not Forman discrete-Morse pairs.

## 2. Near semiprimes are plentiful enough for the geometric step

A template is an ordered triple of distinct odd primes

```text
tau=(p;q,r),
```

representing

```text
C p  <->  C q r,                                   (3)
```

where the common squarefree core `C` is coprime to `pqr`.  It is
scale-compatible when

```text
1/2<p/(qr)<2.                                      (4)
```

At the level of one requested prime, there is no serious pointwise supply
problem.  Baker--Harman--Pintz proved
that every sufficiently large interval of the form
`[x-x^0.525,x]` contains a prime.  Apply this with `x=p/3`.  For every large
prime `p` there is a prime `r` such that

```text
3r=p+O(p^0.525),
|3r/p-1|=O(p^(-0.475)).                            (5)
```

Thus `(p;3,r)` is an exact-prime/exact-semiprime template with power-saving
relative displacement.  See Baker--Harman--Pintz,
[The difference between consecutive primes, II](https://doi.org/10.1112/plms/83.3.532).
Results on exact `E_2` numbers in almost all much shorter intervals give even
denser average supply, but “almost all centers” is not a worst-case matching
statement; see Teravainen,
[Almost primes in almost all short intervals](https://arxiv.org/abs/1510.06005).

The elementary geometric bookkeeping is worth recording.

**Boundary-motion lemma.**  Suppose a global exchange (3) satisfies

```text
|qr/p-1|<=epsilon<1/4.
```

If exactly one of `Cp,Cqr` lies in `(N/2,N]`, the endpoint in the collar lies
in intervals of total length `O(epsilon N)` adjacent to `N/2` and `N`.
Consequently at most `O(epsilon N+1)` integers are lost solely because this
exchange crosses the collar boundary.

Indeed, with `Cqr=Cp(1+theta)` and `|theta|<=epsilon`, crossing the upper
endpoint forces `Cp>N/(1+epsilon)`, while crossing the lower endpoint forces
`Cp<N/(2(1-epsilon))`.  Both are intervals of the asserted total length.

Combining (5) with a distinguished factor `p>=Y` would therefore give the
formal boundary estimate

```text
R_boundary(N;Y) << N Y^(-0.475).                   (6)
```

This is a real gain.  What fails is turning the many candidates (5) into one
two-sided recognizable involution.

## 3. Raw priority codebooks

Let `P` be the set of odd primes and let `A` be a finite subset of `P`, the
prime support of an odd squarefree integer.  For a template
`tau=(p;q,r)`, set

```text
V_tau={p,q,r}.
```

The raw applicability cylinder is

```text
E_tau(A) iff A intersect V_tau is {p} or {q,r}.    (7)
```

When (7) holds, the rewrite is simply

```text
T_tau(A)=A symmetric_difference V_tau.             (8)
```

It interchanges the two patterns in (7) and flips the parity of `|A|`.

Given an ordered codebook `T`, the most natural deterministic rule chooses
the first applicable template and applies (8).  The central recognition
problem is that, after the toggle, a different earlier template can become
applicable.  Then the reverse step does not select the original template and
the rule is not an involution.

Here is the natural condition which prevents that problem without hidden
state or context-dependent guards.

**Definition (background-independent recognizability).**  A codebook is
recognizable if, for every two distinct templates `sigma,tau` and every
finite support `A` satisfying `E_tau(A)`,

```text
E_sigma(A) iff E_sigma(T_tau(A)).                  (9)
```

Under (9), toggling `tau` leaves the entire set of applicable templates
unchanged.  Hence the first-active rule selects `tau` in both directions and
is an exact sign-reversing involution on every support having an active
template.  The definition allows an arbitrary hierarchy/order and allows the
codebook itself to depend on `N`.

Condition (9) is stronger than logically necessary for a specially shielded
priority program.  That remaining loophole is stated explicitly in Section
8.  It is, however, exactly the raw dictionary architecture in which a
rewrite is supposed to recognize itself from its two local endpoint
patterns.

## 4. Exact overlap classification

The recognition condition has a surprisingly rigid truth table.

**Lemma 1 (two-template classification).**  Let `sigma,tau` be distinct raw
templates with scale-compatible supports.  Then (9) holds precisely in one
of the following cases:

1. their supports are disjoint;
2. their supports meet in two primes, and exactly one of their two designated
   singleton primes belongs to the intersection.

They can never meet in exactly one prime.  Equal supports give the same
template.

**Proof.**  On its three bits, `E_tau` consists of a word and its bitwise
complement, and `T_tau` complements all three bits.  For two supports meeting
in two bits, direct restriction to the four union bits gives

| singleton of `sigma` shared? | singleton of `tau` shared? | (9) |
|---|---|---|
| no | no | fails |
| no | yes | holds |
| yes | no | holds |
| yes | yes | fails |

For a one-bit intersection, choose the other two `sigma` bits so that
flipping the shared bit enters one of the two words defining `E_sigma`; the
other `tau` bits can always be chosen to make `tau` active.  This violates
(9).  Disjoint toggles plainly preserve applicability.

If the supports coincide, complementing all three bits preserves every
oriented cylinder.  But in a scale-compatible triple the singleton is forced
to be the largest prime: if `a<b<c` and `a` or `b` were the singleton, its
ratio to the product of the other two would be less than `1/2`.  Hence equal
supports have the same designated singleton and are duplicate templates.
This proves the classification. `square`

The crucial point is already visible in the tempting construction (5).
Different templates `(p;3,r)` normally share exactly the one anchor prime
`3`.  Lemma 1 says that these local rewrites cannot coexist in a
background-independent recognizable codebook.  Making the semiprimes closer
does not repair the recognition collision.

## 5. A component theorem: every recognizable hierarchy is tiny

Let the support hypergraph of a codebook have one three-element hyperedge
`V_tau` for every template, with components defined by nonempty overlap.

**Lemma 2 (component bound).**  Every component of the support hypergraph of
a background-independent recognizable scale-compatible codebook contains at
most two templates.  In particular, every prime occurs in at most two
templates.

**Proof.**  Lemma 1 says that two distinct intersecting supports meet in
exactly two elements.  An elementary three-set lemma says that a connected
family of distinct three-subsets, no two of which meet in exactly one
element, is of one of two forms:

1. a star: every support contains one fixed two-set;
2. a tetrahedral family: all supports are three-subsets of one fixed
   four-set.

To see this, start with `{a,b,c}` and `{b,c,d}`.  A third set meeting the
second in two elements and not meeting the first in one either contains the
common pair `{b,c}`, or is `{a,b,d}` or `{a,c,d}`.  In the latter case every
further connected set is confined to `{a,b,c,d}`; in the former case the
same alternative either preserves the common pair or enters that same
four-set.

In a star, label a support `0` when its singleton is its unique vertex and
`1` when its singleton lies in the common pair.  Lemma 1 requires the labels
of every two supports to differ.  There can therefore be at most two.

For the tetrahedral case, order its four possible primes as `a<b<c<d`.
Every face containing `d` has designated singleton `d`, because scale
compatibility forces the largest prime to be the singleton.  Two such faces
intersect in `d` and therefore have both singletons in their intersection,
contrary to Lemma 1.  At most one face containing `d` can occur.  There is
only one remaining face, `{a,b,c}`, so again the component has at most two
supports. `square`

This is the promised hierarchy collapse.  Overlap sufficient to reuse a
small anchor creates a recognition failure; overlap compatible with
recognition can only form isolated components of at most two rewrites.

## 6. Uniform positive-density no-go, including `N`-adaptive codebooks

The preceding bounded-incidence conclusion can be combined with a sieve in a
way that is uniform in the codebook.  This is stronger than merely applying
the static-dictionary theorem from
`MOBIUS-STATIC-EXCHANGE-NOGO-2026-08.md`, because here the dictionary may be
rebuilt separately for every `N`.

**Theorem (recognizable prime--semiprime codebook no-go).**  There is an
absolute constant `c>0` with the following property.  For every sufficiently
large `N` and every possibly `N`-dependent background-independent
recognizable codebook of scale-compatible `p <-> qr` templates,

```text
#{m in S_N : no codebook template is raw-applicable to m} >= c N.  (11)
```

Consequently no first-active involution from this class has even a sublinear
exceptional set.  “Raw-applicable” means (7), before checking the collar;
therefore a vertex counted in (11) certainly has no collar-valid codebook
edge.

**Proof.**  Only finitely many templates can be relevant to `S_N`, so discard
irrelevant ones.  In each template order the pair factors as `q<r`; the
singleton is `p`, the largest support prime.  By Lemma 2 every prime occurs
in at most two templates.

Fix a large constant `z`, to be chosen at the end.  Call a template low when
`q<=z`, and let `P_0` be the union of the prime supports of all low
templates.  Requiring every prime in `P_0` to be absent kills every low
template.  Scale compatibility gives `p>qr/2`; since `r>=3`,

```text
1/p+1/q+1/r < 2/(qr)+1/q+1/r <= 8/(3q).            (12)
```

At most two templates can be charged to a given `q`, so, with `16/3`
harmlessly rounded up to `6`,

```text
sum_(ell in P_0) 1/ell <= 6 sum_(3<=q<=z, q prime) 1/q.  (13)
```

The density of odd squarefree integers avoiding `P_0` is

```text
d(P_0)=(4/pi^2) product_(ell in P_0) ell/(ell+1)
      >= d_z:=(4/pi^2)
          exp(-6 sum_(3<=q<=z, q prime)1/q)>0.      (14)
```

This density estimate is uniform in the actual primes in `P_0`.  Indeed,
Mobius-square expansion followed by finite inclusion--exclusion gives, when
`|P_0|=O_z(1)`,

```text
#{N/2<n<=N:n odd,squarefree,(n,product P_0)=1}
 = (d(P_0)/2)N+O_z(sqrt(N)).                        (15)
```

Now count all integers on which a high template can be active.  Its support
pattern is contained in `{p divides n} union {qr divides n}`, so (12) and a
union bound give

```text
# high-active n<=N
 <= N sum_high (1/p+1/(qr))
 < 3N sum_high 1/(qr).
```

Using `1/(qr)<=(1/2)(1/q^2+1/r^2)` and incidence at most two,

```text
# high-active n<=N
 <= 3N sum_(ell>z, ell prime) 1/ell^2.              (16)
```

Mertens' theorem and partial summation give

```text
d_z >> (log z)^(-6),
sum_(ell>z, ell prime)1/ell^2 << 1/(z log z).
```

Choose the fixed `z` large enough that the coefficient in (16) is less than
`d_z/4`.  Subtracting (16) from (15) leaves at least
`(d_z/4)N+O_z(sqrt(N))` collar integers admitting neither a low nor a high
template.  Decreasing the constant handles the error and proves (11).
`square`

No estimate for `M(N)` entered this proof.  The loss is genuinely unsigned
and linear.  The theorem also does not use how close `p` is to `qr`; imposing
the much stronger relation (5) only shrinks the allowed codebook.

## 7. Why a large-factor/smooth-number split does not rescue the method

One could try to avoid the overlap theorem by using (5) only at a single
large distinguished factor and declaring integers with no such factor
exceptional.  This has an exact scale tradeoff.

Suppose the distinguished factor must satisfy `p>=Y`.  Formula (6) gives the
available worst-case boundary estimate

```text
N Y^(-0.475).                                      (17)
```

To make (17) at most `N^(1-delta)`, one needs

```text
Y>=N^(delta/0.475).                                (18)
```

But for every fixed `alpha>0`, the collar contains

```text
>>_alpha N/(log N)^k,  k=ceil(1/alpha),             (19)
```

odd squarefree integers all of whose prime factors are at most `N^alpha`.
For an elementary proof, choose `k` distinct primes in a fixed interval

```text
a N^(1/k)<p_j<b N^(1/k),
```

where `1/2<a^k<b^k<1`.  The prime number theorem gives
`>>N/(log N)^k` distinct products in the collar, and `1/k<=alpha` makes every
factor `N^alpha`-smooth.  Thus the proposed smooth exceptional set is
`N^(1-o(1))`, not `O(N^(1-delta'))` for any fixed `delta'>0`.

Conversely, taking `Y=N^o(1)` can reduce the smooth set, but (17) is then only
`N^(1-o(1))`.  Hence

```text
short-gap boundary + discard Y-smooth vertices
```

cannot by itself prove a fixed power saving.  A successful construction
would have to recurse through the smooth vertices.  The theorem of Section 6
shows why a raw recognizable hierarchy of the same local rewrites cannot do
that: recognizability collapses its overlap graph to bounded components.

Almost-all short-interval `E_2` theorems do not change this conclusion.  They
do not furnish a worst-case injective allocation, and a thin exceptional set
of semiprime centers can be amplified by many common cores `C` in (3).

## 8. Injection, shielding, and the exact surviving loophole

It is important not to overstate the no-go.

The following ideas are closed by the theorem when local recognition is
required in the background-independent sense (9):

- a fixed or `N`-adaptive list of raw `p <-> qr` codewords;
- choosing the least/first active codeword at any hierarchy level;
- reusing anchors while requiring every local rewrite to be recognizable
  from its two endpoint patterns independently of the background;
- disjoint codebooks, bounded-overlap codebooks, and the only pairwise
  compatible two-prime overlaps;
- improving prime or semiprime gaps while leaving that recognition model
  unchanged.

The construction `(p;3,r(p))` also exposes all three practical defects:

1. **overlap:** almost every codeword contains `3`, and one-prime overlaps
   violate Lemma 1;
2. **recognition:** toggling one word can activate a higher-priority word, so
   the reverse endpoint chooses a different move;
3. **injection:** different primes can request the same `r`, and one target
   support can receive many proposals.

A sequential matching with a used-target table can repair injection by
state.  Context-dependent guards can also shield every bad overlap witness.
Neither is covered by background-independent recognizability.  But then the
reverse move is certified by global allocation state, not by the factor set
alone.  This returns exactly to the value-ordered greedy survivor already
audited in `MOBIUS-GREEDY-DEPENDENCY-VERDICT-2026-08.md`:

```text
R_g(N)=|M(N)|+2D_g(N),                             (20)
```

where stateful allocation and augmenting paths can control `D_g` but leave
the majority-sign residual `|M(N)|` untouched.

There is a logically possible class between the two results:

> a factor-determined, priority-dependent guarded rewrite system in which
> earlier guards shield every overlap collision, the same guard is
> recoverable after the toggle, and the guarded exceptional set has an
> independent power-saving count.

The present theorem does not rule that out.  A candidate in this class must
state its guards explicitly and prove all four items below before any scan is
evidence:

1. the selected rewrite is identical from both endpoints;
2. no two sources choose one target;
3. collar crossing has a power-saving unsigned bound;
4. the no-guard/no-rewrite set has a power-saving unsigned bound that does
   not contain `M(N)` on the right.

## 9. Verdict

The off-wall prime--semiprime idea separates cleanly into geometry and
combinatorics.

```text
prime/E2 short gaps  ->  power-small multiplicative motion       [works]
raw overlapping codebook -> two-sided recognizable involution    [fails]
large-factor only + smooth discard -> fixed-power exceptions      [fails]
stateful allocation -> bounds the Mobius majority residual         [open]
```

The new theorem is the exact obstruction requested for a substantial and
natural construction class: every background-independent recognizable
prime--semiprime Morse/codebook hierarchy leaves linearly many collar
vertices unmatched, uniformly even for `N`-adaptive dictionaries.  It does
not prove that a fixed zero-free strip does not exist.  It says the next
attempt must use genuinely context-dependent guarded recognition or a new
arithmetic invariant for the majority residual; closer semiprimes alone
cannot supply the missing cancellation.
