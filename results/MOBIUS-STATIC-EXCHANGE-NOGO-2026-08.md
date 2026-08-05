# Static boundary-exchange no-go

Status: analytic no-go theorem proved, 2026-08-04.  It rules out fixed
summable prime-template dictionaries, hence every fixed bounded-incidence
dictionary of finite sign-reversing prime-set substitutions, as well as
several wider one-shot and bounded-scale local rule classes.  An `N`-adaptive
sequential greedy rule survives finite tests.  No RH claim is made.

## 1. Setup

Recall the exact collar

```text
S_N={m:N/2<m<=N, m odd and squarefree}
```

and identity

```text
M(N)=sum_(m in S_N) mu(m).
```

A prime template is a triple of distinct odd primes

```text
tau=(p;q,r)
```

representing the sign-reversing replacement

```text
C union {p}  <->  C union {q,r}.
```

Call it scale-compatible when

```text
1/2 < p/(qr) < 2.                                  (1)
```

Condition (1) is necessary for both replaced integers ever to lie in one
dyadic collar: their ratio is `p/(qr)` or its reciprocal.

Let `T` be a fixed, finite or countable dictionary of such templates,
independent of `N`.

## 2. The no-go theorem

**Theorem (summable static dictionaries).**  Suppose

```text
sum_(tau=(p;q,r) in T) 1/(qr) < infinity.           (2)
```

Then there is a constant `c_T>0` such that

```text
#{m in S_N : no template in T applies to m}
  >= c_T N+o(N).
```

In particular, every matching or involution using only templates from `T`
leaves linearly many vertices unmatched.

**Corollary (bounded pair overlap).**  The theorem applies if there is a fixed
`D` such that every prime occurs in at most `D` of the pair roles `q,r`.
No separate bound on reuse in the singleton role is required.

### Proof

First prove the corollary's summability assertion.  Bounded incidence gives

```text
sum_(tau in T) 1/(q_tau r_tau)
 <= (1/2) sum_tau (1/q_tau^2+1/r_tau^2)
 <= (D/2) sum_(ell prime) 1/ell^2 < infinity.       (3)
```

Now assume (2).  Scale compatibility gives

```text
sum_tau 1/p < 2 sum_tau 1/(qr) < infinity.          (4)
```

Use the natural prime-divisibility law on odd squarefree integers.  Conditional
on being odd and squarefree, the indicators `X_ell=1_(ell divides m)` have, on
each finite collection of odd primes, the product distribution

```text
Pr(X_ell=1)=1/(ell+1).                              (5)
```

For completeness, this is an ordinary density calculation, not a probabilistic
model assumption.  The local density of exponent one at `ell` is
`ell^(-1)-ell^(-2)`, while the local squarefree density is `1-ell^(-2)`;
their ratio is `1/(ell+1)`.  The ratio for exponent zero is
`ell/(ell+1)`.  Multiplying these ratios for any finite set of prescribed
prime exponents and the unrestricted Euler factors for all remaining primes
proves both the finite product law and its natural-density interpretation.

For `tau=(p;q,r)`, introduce the support-pattern cylinder

```text
B_tau = {(X_p,X_q,X_r)=100 or 011}.                 (6)
```

Actual applicability to a vertex of one fixed collar also requires the
substituted target to remain in that collar.  Thus `B_tau` is a superset of
the applicability event, not always the exact event.  This is the direction
needed below: avoiding `B_tau` guarantees that no corresponding substitution
edge is available.

Writing `theta_ell=1/(ell+1)`, equations (2), (4), and (5) give

```text
sum_tau Pr(B_tau)
 <= sum_tau (theta_p+theta_q theta_r)
 <= sum_tau (1/p+1/(qr)) < infinity.                (7)
```

Choose a finite subfamily `T_0` so that the right side of (7) over the tail is
less than `1/2`.  Condition every prime appearing in `T_0` to be absent.  This
conditioning has positive probability and kills every `B_tau` in `T_0`.
Because it only forces finitely many independent indicators to zero, for each
tail template

```text
Pr(B_tau | the conditioning) <= theta_p+theta_q theta_r.
```

Indeed, forcing one of the three primes absent either kills a pattern or can
only remove one of its factors.  The conditional union bound now says that
with probability greater than `1/2`, no tail event occurs.  Hence the exact
event

```text
G = intersection_(tau in T) complement(B_tau)       (8)
```

has positive product probability.

The remaining passage from the product law to natural density can be made
quantitative.  This is recorded separately because it is the only place where
a countable dictionary requires more than finite-dimensional independence.

### 2.1 Quantitative density passage

Put

```text
a_tau=1/p_tau+1/(q_tau r_tau).
```

Choose a finite prefix `T_0` such that, for `T_1=T\T_0`,

```text
A_1=sum_(tau in T_1) a_tau < 1.                   (D1)
```

Let `S` be the finite set of primes occurring in `T_0`.  The set of odd
squarefree integers has density

```text
delta_odd-sf = (1/2) product_(ell odd prime)(1-ell^(-2))
             = 4/pi^2.                            (D2)
```

Within this set, requiring every prime of `S` to be absent has relative
density

```text
C_S=product_(ell in S) ell/(ell+1)>0.             (D3)
```

This condition kills every prefix event.  Conditional on it, each tail event
still has probability at most `a_tau`: forcing one or more of its three primes
absent either kills one of the patterns in (6) or leaves a probability bounded
by `theta_p+theta_q theta_r`.  Hence every finite `F subset T_1` satisfies

```text
dens(odd squarefree, S absent, no B_tau for tau in F)
  >= (4/pi^2) C_S (1-sum_(tau in F) a_tau)
  >= (4/pi^2) C_S (1-A_1).                        (D4)
```

Each density in (D4) is an ordinary finite Euler-product density.  To pass to
the countable intersection, note pointwise that

```text
B_tau subset {p_tau divides n} union {q_tau r_tau divides n}.
```

For every tail `U subset T` and every `x`, the union bound for multiples gives

```text
#{n<=x : some B_tau with tau in U occurs}
 <= x sum_(tau in U) a_tau.                       (D5)
```

Terms whose divisor exceeds `x` contribute zero, so (D5) is valid for a
countable tail by monotone convergence of its finite subunions.  As the tail
of `sum a_tau` tends to zero, the finite-prefix densities form a Cauchy
sequence and squeeze the infinite intersection to a natural density `d_T`.
Equations (D4)--(D5) give the explicit lower bound

```text
d_T >= (4/pi^2) C_S (1-A_1)>0.                   (D6)
```

Therefore

```text
#{m in (N/2,N] : m odd squarefree and no template applies}
 = (d_T/2)N+o(N).                                 (D7)
```

Thus the theorem holds with `c_T=d_T/2`, and (D6) supplies a computable lower
bound after a prefix is chosen.  No independence between different templates
and no correlation inequality are used.

### 2.2 Hypertemplate extension

The proof is not special to `1 <-> 2` exchanges.  Let a normalized
hypertemplate be two disjoint finite sets of odd primes `A_t,B_t`, with

```text
a_t=product_(p in A_t) p,    b_t=product_(p in B_t) p,
|A_t|-|B_t| odd,             1/2<a_t/b_t<2.         (9)
```

It replaces `C union A_t` by `C union B_t`.  If a fixed countable family
satisfies the weighted budget

```text
sum_t (1/a_t+1/b_t) < infinity,                    (10)
```

then the same finite-prefix conditioning and tail union bound leave a
positive-density family admitting no hypertemplate.  The support-pattern
cylinder containing the applicability event has probability at most
`1/a_t+1/b_t`, because one of its two patterns requires every prime of `A_t`
and the other every prime of `B_t`.

For clarity, the countable density passage in the generalized notation is as
follows.  Choose a finite prefix whose complement has weight

```text
W_tail=sum_tail (1/a_t+1/b_t)<1.
```

Force every prime occurring in the prefix to be absent.  This finite cylinder
has positive squarefree density and kills all prefix patterns.  Conditional
on it, forcing additional primes absent can only kill a tail pattern or leave
its probability bounded by `1/a_t+1/b_t`; hence every finite tail subfamily
is avoided with conditional probability at least `1-W_tail`.  Finally, the
pattern cylinder for `t` is contained in

```text
{a_t divides n} union {b_t divides n}.
```

Consequently, for every countable subtail and every `x`, the number of
integers at most `x` in any of its cylinders is at most

```text
x sum_subtail (1/a_t+1/b_t).
```

Letting the subtail weight tend to zero squeezes the finite-prefix densities
to a positive natural density, exactly as in (D4)--(D7).  No independence
between overlapping hypertemplates is used.

Bounded prime incidence implies (10).  Condition (9) rules out an empty side;
since the cardinalities have opposite parity, one side `H_t` has size
`k_t>=2`.  Comparability and AM--GM give

```text
1/a_t+1/b_t
 <= 3/product_(p in H_t) p
 <= (3/k_t) sum_(p in H_t) 1/p^k_t
 <= (3/2) sum_(p in H_t) 1/p^2.                    (11)
```

If each prime occurs in at most `D` hypertemplates, summing (11) is bounded by
`(3D/2) sum_p 1/p^2`.  Thus no fixed bounded-incidence dictionary of finite
prime-set moves that both flips the Mobius sign and preserves the collar can
have a sublinear exceptional set.

## 3. What this kills

The theorem covers more than a finite list of hand-picked toggles.

- Any fixed collection of disjoint triples is killed.
- Any infinite fixed dictionary in which each prime is reused only boundedly
  often is killed, even if templates are prioritized adaptively.
- Replacing one prime by three, two primes by three, or allowing arbitrary
  finite prime-set substitutions does not help under fixed bounded incidence.
- Allowing a matching algorithm to inspect the whole integer does not help if
  every permitted edge still comes from that dictionary.
- Under bounded pair overlap, making `p` and `qr` arbitrarily close does not
  help: scale compatibility transfers the pair-side summability to the
  singleton side.

Thus a viable template mechanism must violate a theorem hypothesis.  It must
use at least one of

1. an `N`-dependent dictionary;
2. unbounded reuse of some primes across templates;
3. a genuinely dynamic rule creating templates from the full factorization;
4. global matching state rather than a fixed local involution.

This explains why the earlier idea of stacking independent
`{p}<->{q,r}` toggles cannot approach complete cancellation.

## 4. Two wider local obstructions

The static theorem does not exhaust the natural local rules.  Two additional
arguments eliminate classes that can use infinitely many templates.

### 4.1 Bounded dyadic locality

Write the three changed primes as `a<b<c`.  In every valid collar edge, `c`
must be the singleton and

```text
1/2 < ab/c < 2.                                    (12)
```

Indeed, if `a` or `b` were the singleton, the ratio of the two-prime side to
the singleton side would exceed `2`.

Suppose a rule requires the dyadic-bin indices of `a,b,c` to differ by at
most a fixed `L`.  If `k=floor(log_2 c)`, then

```text
ab/c >= 2^(k-2L-1).
```

Together with (12), this forces `k<2L+2`.  Thus all changed primes belong to a
fixed finite set.  The positive-density family of odd squarefree collar
integers avoiding that set has no admissible edge.  Any viable local rule must
therefore be genuinely multiscale: its bin relation has the additive shape
`k(c) approximately k(a)+k(b)`, not bounded separation.

### 4.2 Core-fiber collisions for one-shot selectors

For each common core `C`, the vertices

```text
C union {p}       and       C union {q,r}
```

form a complete bipartite fiber whenever the resulting integers lie in the
collar.  A one-shot selector whose preferred target depends only on `C`
therefore collapses the whole fiber onto one vertex.  Three exact families
show how severe this is.

- Under mutual least-neighbor selection, every prime in `(N/2,N]` has the
  same semiprime neighbor set.  At most one is mutually selected, leaving at
  least `pi(N)-pi(N/2)-1`, asymptotic to `N/(2 log N)`, unmatched.
- If every semiprime merges its two factors and inserts the least admissible
  collar prime, every odd squarefree semiprime in the collar proposes to the
  same target.  All but one of the asymptotically
  `(N/2) log log N/log N` such vertices remain unmatched.
- A fixed-palette rule that deletes the smallest factor and tries the two
  least missing primes has a positive-density obstruction.  For example,
  among even-parity squarefree collar integers avoiding every prime at most
  `29`, the proposed replacement uses `3*5/p<1/2` and leaves the collar.  This
  family has size about `0.0392 N`.

These are not a theorem against every bounded-complexity algorithm.  They
identify the common failure: simultaneous choices collide inside enormous
common-core fibers.  Sequential fallback can evade it only by remembering
which targets earlier vertices consumed.

## 5. The first survivor: value-ordered implicit greedy

The strongest simple rule tested so far is deliberately outside the theorem.
For each `N` it constructs the full collar exchange relation implicitly,
processes even-`omega` vertices in increasing value, and pairs each to the
smallest unused odd neighbor.  It does not inspect `M(N)`, either global color
count, or a maximum matching, but its candidate dictionary and used set depend
on the entire collar.

The memory-bounded script
`src/mobius_boundary_implicit_greedy.py` hashes common cores without
materializing the dense graph.  Selected exact outputs are:

| `N` | vertices | `M(N)` | greedy unmatched | excess over `|M(N)|` |
|---:|---:|---:|---:|---:|
| 10,000 | 2,029 | -23 | 23 | 0 |
| 20,000 | 4,048 | 26 | 28 | 2 |
| 50,000 | 10,133 | 23 | 27 | 4 |
| 100,000 | 20,260 | -48 | 56 | 8 |
| 200,000 | 40,527 | -1 | 27 | 26 |
| 500,000 | 101,322 | -6 | 34 | 28 |
| 1,000,000 | 202,646 | 212 | 220 | 8 |

The last two checkpoints were run with an explicit large-memory opt-in.  The
table is diagnostic only.  It is consistent with a square-root unmatched
bound, but selected finite values cannot distinguish that from a remote
failure.

Reproduce the guarded default range with

```text
python3 src/mobius_boundary_implicit_greedy.py
```

### 5.1 A cleaner lexicographic edge order fails its first mechanism

A second sequential rule orders every edge `Cp <-> Cqr`, necessarily with
`q<r<p`, by the tuple `(q,r,p,C)` and accepts it if both endpoints are still
free.  It initially appeared to saturate the smaller parity and leave only a
terminal prime or semiprime block.  An every-rank adversarial audit kills both
claims:

| `N` | `M(N)` | unmatched | excess over `|M(N)|` | unmatched ranks |
|---:|---:|---:|---:|---|
| 10,000 | -23 | 23 | 0 | `{1:23}` |
| 20,000 | 26 | 26 | 0 | `{2:25,4:1}` |
| 30,000 | 18 | 40 | 22 | `{2:27,3:11,4:2}` |
| 50,000 | 23 | 53 | 30 | `{2:36,3:15,4:2}` |

At `N=20,000`, the rank-`4` exception is
`18183=3*11*19*29`; at `N=30,000` and `50,000`, the rule no longer saturates
the smaller parity.  Its unmatched span also grows far beyond a square-root
terminal collar.  This does not disprove an eventual sublinear total-defect
bound, but it removes the only observed structural reason to expect one.  A
streaming implementation can use `O(N)` state, although it must still examine
every candidate edge (over 13 million at `N=50,000`).

Reproduce the guarded streaming audit with

```text
python3 src/mobius_boundary_lex_edge_greedy.py 10000 20000 30000
```

## 6. Correct next kill gate

The next precise question is no longer “find a local involution.”  That class
is too weak.  It is:

> Can one prove directly, without an occurrence of `M(N)` on the right,
> `R_greedy(N)=O(N^(1-delta))` for some fixed `delta>0`?  Or can one construct
> an infinite family of collars on which `R_greedy(N)=N^(1-o(1))`?

An approximation bound of the form
`R_greedy<=|M(N)|+O(N^theta)` has no analytic leverage because the unknown
Mertens term remains on its right.  In contrast, any direct sublinear bound
would be a new cancellation theorem and a new zero-free half-plane; the
RH-scale `O_epsilon(N^(1/2+epsilon))` bound would imply RH.  Before larger
scans, the useful work is to characterize the alternating paths missed by
value-order greedy and decide whether their obstruction can be counted by an
unsigned sieve argument.

## 7. Topological and literature boundary

Björner's factor-`2` matching is already a perfect discrete-Morse matching:
its critical cells are exactly the collar cells counted by the Betti numbers,
so the Morse inequalities prevent further cancellation in that category.
Pakianathan and Winfree recover the same logarithmic shell in the quota-complex
language.  The `p <-> qr` endpoints are incomparable, so this audit concerns
sign cancellation of the Euler characteristic, not Forman cancellation of
homology.

The topology behind the collar is from
[Björner, *A cell complex in number theory*](https://arxiv.org/abs/1101.5704);
see also [Pakianathan--Winfree, *Threshold complexes and connections to number
theory*](https://arxiv.org/abs/1104.4324) and [Forman, *Morse theory for cell
complexes*](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/forman5.pdf).
A targeted search found no published collar involution or bounded-local-rule
obstruction matching the statements above, but that is not a priority or
novelty claim.  The sieve parity problem is relevant background, not a theorem
against these exact exchange rules.

## 8. Subsequent audit of the value-ordered survivor

The proposed blocker-forest checkpoint has now been completed.  If `R_g` is
the greedy unmatched count, then exactly

```text
R_g(N)=|M(N)|+2D_g(N),
```

where `D_g` is the smaller-side unmatched count.  Dependency forests,
alternating paths, and Hall expansion control only `D_g`.  At the selected
checkpoints through `N=200000`, explicit vertex-disjoint length-three paths
remove all of `D_g` and leave precisely `|M(N)|`.

There is also an exact polynomial compression: every matched consecutive-rank
pair contributes a positive multiple of `1+z`, while the unmatched rank
enumerator still takes the value `M(N)` at `z=-1`.  This identifies the
matching route with the same singular endpoint as the squarefree fugacity
polynomial.  The blocker-forest mechanism is therefore parked; a revival
needs an independently sparse unsigned set containing every majority-side
residual.  See
`results/MOBIUS-GREEDY-DEPENDENCY-VERDICT-2026-08.md`.
