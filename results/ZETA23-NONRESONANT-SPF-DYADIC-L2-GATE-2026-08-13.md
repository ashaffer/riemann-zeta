# Nonresonant SPF dyadic square-function gate

**Date:** 2026-08-13  
**Status:** exact weighted square-function theorem proved; fixed-power
aggregation does not follow; a sharply scoped coherent model certifies the
missing information.

## Verdict

For the **narrow `q<Z=Y^.16` selector sector**, the new rough-gap theorem can
be used on the whole tail after the already controlled resonant `q`-group,
without following the order-dependent Eratosthenes gaps.  This includes the
one-gap/corridor scale `q=Y^.1598`; it does not include the full multi-gap
Dirichlet selector, whose denominators can reach `q<=H` with exponent about
`.248`.  After the `q<Z` group the active set is exactly the fixed universal
rough base `R_Z`.  Delete all its remaining composites simultaneously, split
the positive transport cell by cell, and label each deleted cell by its least
prime factor.  For a dyadic band `P<p<=2P` this gives the genuine theorem

```text
sum_(P<p<=2P) |R_p(a/q)|^2
   << [Y/(P log Y)] G_2(Y;Z)
   << Y^2 log Y/P,                                  (0.1)
```

uniformly in the chosen reduced `a/q`, for `Z<=Y^.16`.  The same estimate is
selector-stable: it holds for the aggregate over disjoint curvature blocks
with arbitrary blockwise reduced `(q_I,a_I)`, provided `q_I<Z` and terminal
edges crossing block boundaries have first been disposed of.  More precisely,
the weighted estimate before taking a maximum count is

```text
sum_p |R_p(a/q)|^2/N_p <= 4 G_2(R_Z).               (0.2)
```

Here `R_p` includes the sum over all selected blocks and is an exact cellwise
decomposition of the **simultaneous non-`q` tail**, not the order-dependent
sequential SPF charges.

This is the strongest coefficient-blind `L2` consequence of the new gap
input.  It does not power-save the signed band aggregate.  There are
`P^(1+o(1))` prime labels, so Cauchy gives

```text
|sum_(P<p<=2P) R_p|^2
 <=pi(2P)-pi(P) times sum_p |R_p|^2
 <<Y^(2+o(1)).                                      (0.3)
```

The `P^-1` square-function gain and the number of labels cancel exactly.  At
the largest carrier bill

```text
kappa=.01974048259...,
```

a proof by stagewise Cauchy would instead require

```text
sum_(P<p<=2P)|R_p|^2
 <<Y^(2-2kappa+o(1))/P,                             (0.4)
```

so (0.1) misses a fixed factor `Y^(2kappa)` (up to logarithms).

The finite checker constructs exact nonadjacent deletions with

```text
G_2 asymp Y log P,
N_p <<Y/(p log P),
p divides every centre labelled p,
q does not divide any deleted centre,
|sum_p R_p| asymp Y/log P.                          (0.5)
```

Thus gap energy, divisor-count caps, and pointwise nonresonance permit a
coherent `Y^(1-o(1))` aggregate.  The construction deliberately does **not**
claim to realize the actual `P`-rough set.  It is a method-level countermodel:
an arithmetic theorem about the residue distribution of the actual
gap-weighted rough deletion cells remains capable of succeeding.

No published no-go theorem rules that theorem out.  Conversely, the surveyed
large-sieve, Kloosterman, and short-interval sieve results do not state it.

## 1. Exact universal-base reorder

Fix a maximal roughness cutoff strictly above the denominators under
consideration,

```text
q<Z=Y^zeta,               zeta<=.16,
R_Z={n in the shell: every prime factor of n is >=Z}.
```

For the selected reduced fraction `a/q`, let

```text
B_q=R_Z union {composite multiples of q in the shell}.              (1.1)
```

This is the selector-stable pre-group base used by the resonant-group
argument.  It is a refinement of `R_Z`, so splitting gaps gives, up to the
fixed shell collar,

```text
G_2(B_q)<=G_2(R_Z)<<Y(log Y)^2.                      (1.2)
```

Delete all `q`-multiples simultaneously, as in the universal-base resonant
group theorem.  Because `q<Z`, every multiple of `q` has a prime factor below
`Z`; hence

```text
B_q \ {q-multiples}=R_Z.                              (1.3)
```

Now delete all composite centres of `R_Z` simultaneously.  The survivors are
exactly the terminal primes.  Every centre in this second group is
pointwise nonresonant modulo `q`, again because `R_Z` contains no `q`-multiple.
Thus the exact order is

```text
B_q --delete q-multiples--> R_Z
    --delete all rough composites simultaneously--> terminal primes. (1.4)
```

The first arrow has the proved `q^(-1/2)`-type resonant-group saving; the
second is the tail studied here and uses `G_2(R_Z)` directly.  There is no
approximation and no dependence on the ordinary SPF deletion order.

This order is also selector-stable.  Work separately inside the retained
terminal-prime edges wholly contained in each curvature block.  Although the
phase `e_(q_I)(a_I n)` changes from block to block, the post-group active set
on every one of them is the same `R_Z`.  The retained components have
disjoint interiors, so their incident gap-square ledgers sum to at most the
one global `G_2(R_Z)` ledger.

The hypothesis `q<Z` is essential to this clean compatibility.  If `q>=Z`,
the post-group set is generally `R_Z\qZ`, whose merged-gap square is not
bounded by (1.2).  One can put the non-`q` deletion first and retain a fixed
refinement, but then the resonant group changes.  This report makes no claim
that the two separately favorable orders can be mixed for `q>=Z`.  The
one-gap/corridor choice `q=Y^.1598`, `Z=Y^.16` lies strictly in the proved
regime.  The full retained multi-gap selector may use `q` as large as
`Y^.248`; no reduction of all those selectors to `q<Z` has been proved.

## 2. Cellwise transport decomposition

Let `B` be any finite ordered set, let `D subset B` be deleted
simultaneously, and put `S=B\D`.  Write `nu_B` and `nu_S` for their atomic
Voronoi cell-mass measures.  The positive transport identity is

```text
nu_S-nu_B=eta_D-nu_B|_D,       eta_D>=0,
eta_D(R)=nu_B(D).                                      (2.1)
```

There is a canonical cellwise refinement of (2.1).  Partition the original
Voronoi cell of each `x in D` according to the final nearest survivor.  If
`eta_x` is the resulting positive mass at the final centres and

```text
m_x=nu_B({x})=[g_-(x)+g_+(x)]/2,
```

then

```text
eta_D=sum_(x in D) eta_x,       eta_x(R)=m_x,
sigma_x=eta_x-m_x delta_x,
nu_S-nu_B=sum_(x in D)sigma_x.                         (2.2)
```

For every `|f|=1`,

```text
|integral f d sigma_x|<=2m_x=g_-(x)+g_+(x).           (2.3)
```

Give the deleted centres any labels.  For label `p` define

```text
D_p={x in D: label(x)=p},
N_p=#D_p,
R_p(f)=sum_(x in D_p) integral f d sigma_x.            (2.4)
```

Cauchy and `(u+v)^2<=2u^2+2v^2` give

```text
|R_p(f)|^2
 <=N_p sum_(x in D_p)[g_-(x)+g_+(x)]^2.               (2.5)
```

Every base gap is incident to at most two deleted centres.  Consequently

```text
sum_p sum_(x in D_p)[g_-(x)+g_+(x)]^2
 <=4 sum_(g gap of B)g^2=4G_2(B),                     (2.6)
```

and therefore

```text
sum_p |R_p(f)|^2/N_p <=4G_2(B).                       (2.7)
```

Zero-count labels are omitted.  Equations (2.2)--(2.7) are finite exact
statements.  They neither assume independence nor lose control through
sequentially merged gaps.

Apply them to the second arrow in (1.4), with `B=R_Z` and the label equal to
the actual least prime factor of the deleted rough composite.  In the
blockwise version, use the phase selected on the unique block containing the
cell and sum the charges with label `p` over all blocks.  Inequality (2.3)
only uses modulus one, and all retained components are disjoint, so
(2.5)--(2.7) are unchanged.  For one block,

```text
sum_p R_p(e_q(a .))
=T(primes)-T(R_Z),                                    (2.8)
```

exactly.

For many blocks, (2.8) is summed over `I`, with `T` restricted to the retained
edges of `I`.  In particular, no union bound over the possible denominators
appears in (2.7).

## 3. The dyadic square-function theorem

If `x` has least prime factor `p`, write `x=pm`.  Summed over all disjoint
blocks, an ordinary upper-bound sieve (or Brun's sieve at the upper end)
gives, uniformly in polynomial dyadic bands `Z<=P<=sqrt(2Y)`,

```text
N_p<<Y/(p log Y)<<Y/(P log Y),       P<p<=2P.          (3.1)
```

The logarithms `log p` and `log(Y/p)` are comparable in this range.  For
`p>sqrt(2Y)` there are no composite shell integers with least prime factor
`p`.

Insert (3.1) into (2.5), sum over the band, and use (2.6) and the rough-gap
theorem:

```text
sum_(P<p<=2P)|R_p(e_q(a .))|^2
 <<Y/(P log Y) G_2(R_Z)
 <<Y^2 log Y/P.                                      (3.2)
```

This proves (0.1).  It is uniform in `a` because only `|f|=1` was used.  It
also remains valid when `P>Y^.16`: the gaps belong to the fixed base `B_q`
at cutoff `Z`, not to the unavailable moving rough set `R_P`.  This point is
essential.  The theorem `G_2(Y;P)<<Y log^2Y` itself has only been proved here
for `P<=Y^.16`; (3.2) does not silently extend that moving-cutoff theorem.

By the prime number theorem, or just a standard upper-bound sieve for the
number of labels,

```text
# {p:P<p<=2P}<<P/log P.                                (3.3)
```

Cauchy applied to (3.2) yields

```text
|sum_(P<p<=2P)R_p|^2
 <<[P/log P][Y^2 log Y/P]
 <<Y^2,                                               (3.4)
```

up to harmless fixed-exponent logarithmic ratios.  No fixed power of `Y` is
saved.

If `P=Y^(c+o(1))`, the power ledger is

| quantity | exponent |
|---|---:|
| `N_p` | `1-c` |
| proved dyadic energy | `2-c` |
| number of labels | `c` |
| squared aggregate after Cauchy | `2` |
| required energy for aggregate `Y^(1-kappa)` | `2-c-2kappa` |

At `kappa=.01974048259...`, the missing energy saving is

```text
2kappa=.03948096518....                               (3.5)
```

This is a fixed-power gap, not a logarithmic optimization issue.

## 4. Finite-group formulation of the missing input

For each label define its signed residue vector

```text
v_p(r)=sigma_p({centres congruent to r mod q}),
R_p(a/q)=sum_(r mod q)v_p(r)e_q(ar).                  (4.1)
```

Each `v_p` has total mass zero.  Parseval gives the exact identities

```text
1/q sum_(a mod q)|sum_p R_p(a/q)|^2
   =sum_(r mod q)|sum_p v_p(r)|^2,                   (4.2)

1/q sum_a sum_p |R_p(a/q)|^2
   =sum_p sum_r |v_p(r)|^2.                          (4.3)
```

The gap theorem controls total cell mass and the incident square ledger in
(2.6).  It does not bound the right side of (4.2) after cancellation of its
uniform component.  In particular, mass-zero and `r!=0` support permit a
vector concentrated on two nonzero residues.  Such a vector has a
macroscopic coefficient at a selected numerator.

An `L4` average does not repair this information loss.  For a scalar residue
weight `w`,

```text
1/q sum_a |w_hat(a)|^4
 =sum_s |sum_(r+t=s mod q)w(r)w(t)|^2.                (4.4)
```

Thus an `L4` bound is an additive-energy theorem for the gap-weighted residue
vector.  Neither `G_2` nor the SPF count caps control that energy.  The
checker exhibits a selected coefficient more than ten times its all-frequency
RMS and more than three times its fourth-mean root, while satisfying every
method-level certificate listed in (0.5).

The precise missing theorem can be stated in either of two equivalent useful
forms.

1. **Selected residue dispersion.**  Uniformly for every selected `(q,a)`
   and dyadic band,

   ```text
   |sum_(P<p<=2P)sum_r v_p(r)e_q(ar)|
       <<Y^(1-kappa-epsilon)(log Y)^(-A).             (4.5)
   ```

2. **Power-saving dyadic square function plus label decorrelation.**  Prove
   (0.4) and a summation inequality which does not reinsert the full
   `sqrt(P/log P)` loss.

There is a second, potentially more economical target.  Let `C_Z(a/q)` be
the localized Fourier mode of the fixed rough base before the simultaneous
tail.  Then

```text
C_Z(a/q)+sum_p R_p(a/q)=T(primes;e_q(a .)).           (4.6)
```

One may seek a direct residue-dispersion theorem for the left side of (4.6),
allowing cancellation between the rough-base mode and the tail.  Neither
(2.7) nor the classical large sieve controls the cross term.  In residue
language it requires dispersion of `u_Z(r)+sum_p v_p(r)`, not merely separate
norm bounds for `u_Z` and the `v_p`.

Ordinary equidistribution of the **unweighted** SPF centres is insufficient:
`v_p(r)` contains both the Voronoi cell mass and its final transport
destination.  The theorem must retain those weights or prove an explicit
comparison replacing them by separable arithmetic coefficients with a
power-saving error.

## 5. Coherent exact-deletion model

The model uses lattice nodes

```text
x_j=x_0+jL,              L=2 mod 4,
```

and a prime `q=3 mod 4` with

```text
a=(q+1)/4.                                             (5.1)
```

For an isolated deletion at `x_j`, both neighboring gaps equal `L`, so the
exact trapezoid change is

```text
Delta_j
=L[cos(2 pi aL/q)-1]e_q(a x_j).                       (5.2)
```

Since `L=2 mod 4` and `L=o(q)`, the real multiplier in brackets tends to
`-2`.  Select pairwise nonadjacent centres whose phases lie in a fixed arc
around `1`, exclude residue zero modulo `q`, and label a centre by its least
prime divisor inside `(P,2P]`.  The deterministic checker imposes

```text
#D_p<=C Y/(p log P).                                   (5.3)
```

There are `asymp Y/(log P)^2` selected centres, their individual charge has
size `asymp log P`, and all charges lie in a common half-plane.  Hence

```text
|sum_p Delta_p|>>Y/log P.                             (5.4)
```

Because the deletions are isolated,

```text
G_2(after)=G_2(before)+2 #D L^2=O(Y log P).           (5.5)
```

Moreover a stage has `#D_p asymp Y/(p log P)` coherent cells, so

```text
sum_(P<p<=2P)|Delta_p|^2 asymp Y^2/(P log P),         (5.6)
```

while Cauchy across the nonempty labels is nearly sharp and returns (5.4).
This demonstrates that even an energy slightly better by a logarithm than
(3.2) need not give a power.

### Exact scope

The construction certifies all of the following simultaneously:

- the literal trapezoid deletion identity;
- pairwise nonadjacent simultaneous deletions;
- near-linear initial and final gap squares;
- `p|x` and least-divisor-in-the-band labels;
- `q` does not divide any deleted centre;
- upper-sieve-shaped per-label count caps;
- a coherent selected Fourier coefficient;
- Parseval `L2` and additive-energy `L4` diagnostics.

Its undeleted lattice mode is only a boundary-sized geometric sum, while its
final mode contains the coherent deletion charge.  Thus it also obstructs a
coefficient-blind inference for the combined expression in (4.6), not just
for the tail considered separately.

It does **not** certify that the undeleted lattice is `P`-rough, that every
actual `P`-rough multiple in the shell is present, or that the label is the
absolute smallest prime factor.  Those omitted facts are exactly where a new
arithmetic dispersion theorem may enter.  Therefore (5.4) is not a
counterexample to (4.5) for actual rough integers and is not a no-go theorem
for the route itself.

## 6. Published-theorem boundary

The literature survey found useful inputs but no theorem matching (4.5).

1. Montgomery and Vaughan's
   [*The large sieve*](https://doi.org/10.1112/S0025579300004708), Theorem 1,
   bounds the sum of squared values of one trigonometric polynomial over a
   separated family of frequencies by `(N+delta^-1)` times coefficient
   energy.  Equations (4.2)--(4.3) are its finite-group shadow here.  It
   controls an average over numerators; the height rule is allowed to select
   an exceptional numerator, and the checker shows that this exception is
   compatible with the available norms.
2. Matomaki's
   [*Almost primes in almost all very short intervals*](https://arxiv.org/abs/2012.11565)
   supplies the rough-gap input through a pointwise vector-sieve minorant,
   well-factorable sieve weights, and her bilinear remainder lemma.  Its
   coefficients are prescribed divisor convolutions.  The signed vector
   `v_p(r)` in (4.1) depends jointly on the deleted centre, both neighboring
   gaps, the final surviving destination, and the selected block.  It is not
   one of the paper's sieve remainders.
3. Bettin and Chandee's
   [*Trilinear forms with Kloosterman fractions*](https://arxiv.org/abs/1502.00769)
   treats sums with separated coefficient sequences
   `alpha_m beta_n nu_a`.  The arbitrary-coefficient statement means each
   one-dimensional sequence is arbitrary; it does not permit an arbitrary
   joint matrix `c_(p,m)` carrying the Voronoi-neighbor rule.  No
   factorization or low-rank approximation of that matrix with a
   power-saving remainder has been proved here.
4. The Deshouillers--Iwaniec
   [spectral/Kloosterman large-sieve machinery](https://eudml.org/doc/142975)
   used behind the short-interval sieve similarly acts after a bilinear or
   well-factorable separation.  Applying it to (4.1) would first require the
   missing coefficient comparison, so citing the spectral theorem does not
   establish (4.5).

These are scope failures, not published impossibility theorems.  A successful
next step should attack the actual weighted residue vector, perhaps by proving
that its gap/destination dependence has low bilinear rank on average over
`p`, or by a dispersion estimate which keeps the two endpoint residues until
after the prime average.

## 7. Reproduction

Run

```bash
PYTHONPATH=src python3 -m unittest -v src/test_spf_tail_large_sieve_gate.py
python3 results/verify_zeta23_nonresonant_spf_tail_gate.py
```

The verifier checks the exact exponent deficit, prime divisibility and
nonresonance, count caps, direct trapezoid identity, gap-square identity,
phase coherence, stagewise near-saturation, and the selected-frequency
`L2/L4` diagnostics.

## 8. Truth boundary

```text
q<Z universal-base order (1.4):                       EXACT
all retained selectors reduce to q<Z:                 NOT PROVED / FALSE AS SCOPE
fixed-rough-base cellwise transport decomposition:    EXACT
weighted label square function (2.7):                 PROVED
dyadic SPF energy Y^(2+o(1))/P:                       PROVED
power-saving band aggregate from Cauchy:              FALSE AS AN INFERENCE
MV large sieve controls every selected numerator:     FALSE
Bettin--Chandee accepts arbitrary joint gap weights:   FALSE
coherent method-level finite countermodel:             EXACT
countermodel realizes the actual rough set:           FALSE / NOT CLAIMED
actual weighted SPF-residue dispersion (4.5):          OPEN
direct rough-base plus tail dispersion (4.6):          OPEN
post-q tail with a fixed power saving:                 OPEN
zero-free strip from this gate:                        NOT CLAIMED
```
