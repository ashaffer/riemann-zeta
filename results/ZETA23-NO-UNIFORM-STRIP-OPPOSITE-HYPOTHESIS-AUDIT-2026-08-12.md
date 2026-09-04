# The opposite hypothesis is stronger than disproving RH

Status: hostile theorem audit of the assertion that the Riemann zeta
function has zeros arbitrarily close to `Re(s)=1`, 2026-08-12.  The exact
prime-error equivalence and the winding-versus-universality obstruction are
proved below.  No off-critical zeta zero, and hence no failure of a uniform
zero-free strip, is proved.

## 1. Verdict

Let

```text
Theta=sup{Re(rho): zeta(rho)=0, 0<Re(rho)<1}.             (1.1)
```

The proposed opposite hypothesis is

```text
Theta=1.                                                  (1.2)
```

It is equivalent to zeros occurring arbitrarily high to the right of every
fixed line `sigma<1`.  It is **not** equivalent to the negation of RH:

```text
RH                 <=> Theta=1/2;
not RH             <=> Theta>1/2;
no uniform strip    <=> Theta=1.                          (1.3)
```

The implication `not RH => no uniform strip` is false as logic: a
hypothetical rightmost zero at `Re(rho)=0.6`, with no zeros farther right,
would disprove RH but leave a large uniform zero-free strip.

No accepted theorem presently proves even one zeta zero with real part
strictly greater than `1/2`.  Therefore every proof of (1.2) would first
disprove RH and then prove a substantially stronger statement.  The Clay
Mathematics Institute continues to list RH as an unsolved Millennium problem
in 2026.

The route audit is binary:

| proposed route | rigorous output | first missing or false step |
|---|---|---|
| standard Voronin universality | approximation of nonvanishing targets; arbitrarily small zeta values | a target with nonzero winding is excluded |
| positive-density strong universality | would force linearly many off-line zeros | false for zeta by the Bohr--Landau/Ingham zero-density theorem |
| sequence-only zero-target universality | would force sparse off-line zeros by Rouche | unproved; near `1` it is stronger than (1.2) |
| `psi(x)-x` omega theorems | power exponent `1/2`, up to logarithmic/subpower factors | an omega sequence of exponent tending to `1` |
| Mertens oscillation/resonance | power exponent `1/2`, and failure of the sharp constant-one Mertens conjecture | growth exponent `1`, not merely a larger square-root constant |
| large/small values and resonance | values of large modulus or values arbitrarily close to zero | contour winding; small nonzero values do not imply zeros |
| Riemann--von Mangoldt and zero density | total counts and upper bounds for right-hand zeros | any horizontal lower bound producing even one off-line zero |
| functional equation | reflection `beta <-> 1-beta` | no mechanism moving a critical-line zero toward `1` |
| zero repulsion | exclusions near `1`, chiefly for families of `L`-functions | it excludes zeros and does not create zeta zeros |
| random Euler products/random matrices | value heuristics, usually nonvanishing products or critical-line zeros | no deterministic transfer to the zeta divisor |
| logical independence | no independence result for RH is known | independence would not prove (1.2) in the standard complex numbers |

Thus the requested theorem has status

```text
quantifier/equivalence audit:                   PASS;
Theta=1 from any known unconditional theorem:  FAIL;
compatibility with density hypothesis:          PASS;
compatibility with RH:                          FAIL;
publishable new disproof of a uniform strip:    FAIL.      (1.4)
```

The strongest substantive conclusion of this audit is a precise no-go:
standard universality cannot supply the missing winding, while the usual
positive-density strengthening that would supply it is already incompatible
with unconditional zero density.  A sparse winding theorem remains possible
logically, but it is itself an off-line-zero theorem.

## 2. Exact quantifiers

### Proposition 2.1

The following statements are equivalent.

1. `Theta=1`.
2. For every `sigma<1`, there is a nontrivial zero `rho` with
   `Re(rho)>sigma`.
3. For every `sigma<1` and every `T_0`, there is such a zero with
   `abs(Im(rho))>T_0`.
4. There is a sequence of nontrivial zeros `rho_n` for which
   `abs(Im(rho_n))->infinity` and `Re(rho_n)->1`.
5. No `delta>0` makes the half-strip `Re(s)>1-delta` zero-free.

#### Proof

The implications `4 => 3 => 2 => 1` and `1 <=> 5` are immediate.  From
`1`, choose a zero `rho_n` with `Re(rho_n)>1-1/n`.  Zeta has only finitely
many zeros in each bounded rectangle and has no zero on `Re(s)=1`, so this
sequence has a subsequence with unbounded ordinates.  That subsequence gives
`4`.  The same finiteness proves `2 => 3`: otherwise all zeros to the right
of one fixed line would lie in a compact rectangle, whose finite set has a
maximum real part strictly below one.  QED

This compactness step is why the phrase "a zero to the right of every fixed
line" really does mean arbitrarily high zeros, even if height is omitted.

### Relation to standard conjectures

RH gives `Theta=1/2`, so (1.2) directly contradicts RH.  The density
hypothesis

```text
N(sigma,T) <<_epsilon T^(2*(1-sigma)+epsilon)             (2.1)
```

is only an upper bound.  For every fixed `sigma<1` its right side tends to
infinity, so it permits an arbitrarily sparse infinite sequence of zeros to
the right of `sigma`.  Hence (1.2) does **not** contradict the density
hypothesis.  It likewise does not contradict an asymptotic statement that 100 percent
of zeros lie on the critical line: a zero-density exceptional sequence can
still have real parts tending to one.

## 3. The exact prime-error and Mobius growth targets

Put

```text
E_psi(x)=psi(x)-x,       M(x)=sum_(n<=x) mu(n).            (3.1)
```

The exponent identities already proved and sourced in
`R98-QUASI-RH-BOOTSTRAP-GATE.md` can be stated as follows.

### Theorem 3.1 (generalized Littlewood exponent identity)

```text
Theta
 =inf{a: for every epsilon>0,
          E_psi(x)=O_epsilon(x^(a+epsilon))}
 =inf{a: for every epsilon>0,
          M(x)=O_epsilon(x^(a+epsilon))}.                 (3.2)
```

Equivalently,

```text
Theta=limsup_(x->infinity) log(1+abs(E_psi(x)))/log x
     =limsup_(x->infinity) log(1+abs(M(x)))/log x.         (3.3)
```

For the first identity, the two directions are especially transparent.  In
`Re(s)>1`, partial summation gives

```text
-zeta'(s)/zeta(s)-s/(s-1)
 =s*integral_1^infinity E_psi(x)*x^(-s-1) dx.             (3.4)
```

An upper bound of power `a` makes the right side holomorphic in `Re(s)>a`.
A zeta zero there would give the left side a pole, so no such zero exists.
Conversely, if `Theta<1`, the truncated explicit formula gives

```text
E_psi(x)
 =-sum_(abs(Im(rho))<=x) x^rho/rho+O(log^2 x)
 =O(x^Theta*log^2 x).                                    (3.5)
```

The standard good-height interpretation handles values of `x` at jumps.
This proves the first equality in (3.2).  For Mobius,

```text
1/zeta(s)=s*integral_1^infinity M(x)*x^(-s-1) dx          (3.6)
```

proves the easy zero-free implication, and the generalized Littlewood
criterion gives `M(x)=O_epsilon(x^(Theta+epsilon))` when `Theta<1`.
Trivial `O(x)` bounds cover `Theta=1`.  This proves (3.2); the elementary
relation between infimal power order and logarithmic limsup gives (3.3).

### Exact omega theorem needed for the opposite hypothesis

Theorem 3.1 turns (1.2) into either of the equivalent arithmetic statements

```text
abs(psi(x)-x)=x^(1-o(1)) along a sequence,                (3.7)

abs(M(x))=x^(1-o(1)) along a sequence.                    (3.8)
```

These are the exact missing omega statements.  A fixed logarithmic or
subpower multiplier of `sqrt(x)` still has logarithmic power exponent
`1/2`, not `1`.

Littlewood's classical oscillation theorem for `pi(x)-li(x)` is at the
square-root power (with iterated-log amplification).  The disproof by
Odlyzko and te Riele of `abs(M(x))<=sqrt(x)` changes a constant-scale
Mertens assertion, not the power exponent.  Neither supplies even one zero
with `Re(rho)>1/2`.  Modern resonance results producing unusually large
zeta or Mobius-related values remain on a square-root/subpower scale and do
not approach (3.7)--(3.8).

There is also a polarity trap.  The Vinogradov--Korobov zero-free region
implies an **upper** estimate of the rough form

```text
E_psi(x) << x*exp(-c*(log x)^(3/5)*(loglog x)^(-1/5)).    (3.9)
```

Its logarithmic power exponent is still one.  It gives no lower sequence
like (3.7), and the corresponding zero-free boundary shrinks toward
`Re(s)=1`; it is not a fixed strip in either direction.

## 4. Universality: the exact winding obstruction

Voronin universality applies on a compact `K` in
`1/2<Re(s)<1`, with connected complement, to a target that is continuous
on `K`, holomorphic in its interior, and nonvanishing.  Effective versions
make the set of good shifts have positive lower density.  The
nonvanishing hypothesis is decisive, not cosmetic.

Approximating a tiny constant shows, for every fixed
`1/2<sigma<1`, that

```text
inf_t abs(zeta(sigma+i*t))=0.                            (4.1)
```

It does not show the infimum is attained.  A holomorphic nonvanishing
function can be arbitrarily small.  This observation alone is enough to
dispose of the small-value and resonance route.

### Proposition 4.1 (a winding target would force a zero)

Let

```text
D={s:abs(s-sigma_0)<=r},
1/2<sigma_0-r<sigma_0+r<1.                               (4.2)
```

If, for some real `tau`,

```text
max_(s in D) abs(zeta(s+i*tau)-(s-sigma_0))<r,            (4.3)
```

then zeta has a zero in `D+i*tau`.

#### Proof

On the boundary of `D`, the target `s-sigma_0` has modulus `r`.  Rouche's
theorem says it and `zeta(s+i*tau)` have the same number of zeros in `D`,
namely one.  QED

If (4.3) were available for arbitrarily high shifts and for discs whose
left endpoints approach one, it would prove (1.2).  This is often called a
zero-target or strong-universality heuristic.  It is not standard Voronin
universality.

### Proposition 4.2 (positive-density winding universality is false)

For a fixed disc (4.2), let `A(T)` be the set of `tau in [0,T]` satisfying
(4.3).  Then

```text
meas(A(T))=o(T).                                          (4.4)
```

In particular, the usual positive-lower-density form of strong
universality with the target `s-sigma_0` is unconditionally false for the
Riemann zeta function.

#### Proof

By Proposition 4.1, every `tau in A(T)` lies within `r` of the ordinate of
a zero with real part at least `sigma_0-r`.  A single zero covers at most an
interval of `tau`-length `2r`.  Hence

```text
meas(A(T))
 <=2*r*N(sigma_0-r,T+r)+O(1).                            (4.5)
```

Ingham's density estimate, or the weaker Bohr--Landau theorem, gives

```text
N(sigma,T)=o(T)       for every fixed sigma>1/2.          (4.6)
```

Equations (4.5)--(4.6) prove (4.4).  QED

Thus there is no continuum of missing zero-producing shifts waiting to be
extracted from ordinary universality.  Only a sparse sequence-only version
escapes (4.4), and proving that version already proves sparse off-line
zeros.

Andersson's removal of the nonvanishing hypothesis for compact sets with
empty interior does not evade this obstruction.  Such a compact set with
connected complement cannot contain a Jordan contour: a contained Jordan
curve would separate the complement, while empty interior leaves points on
both sides.  Therefore the theorem supplies no closed winding contour on
which to apply Rouche or the argument principle.

Finally, Bagchi-type **strong recurrence** must not be renamed strong
universality.  Strong recurrence approximates zeta by its own shifts and is
equivalent to RH in the standard formulation.  It points toward
nonvanishing in `Re(s)>1/2`; it does not permit the zero target in (4.3).

## 5. Density, symmetry, and zero-free regions permit a sparse edge

Riemann--von Mangoldt counts all zeros by height but supplies no horizontal
lower bound.  Ingham, Huxley, Guth--Maynard, and the density hypothesis give
upper bounds on right-hand zeros.  An upper bound cannot prove that even one
such zero exists.

The compatibility can be made explicit at the level of every constraint in
this paragraph.  Consider the abstract quartet sequence

```text
Gamma_n=exp(exp(n^2)),
rho_n=1-1/n+i*Gamma_n,                 n>=3,              (5.1)
```

together with conjugates and functional-equation reflections, and add a
critical-line background with the Riemann--von Mangoldt count.  Then

```text
Re(rho_n)->1,
#{n:Gamma_n<=T}=O(sqrt(loglog T))=T^o(1).                 (5.2)
```

This exceptional set satisfies every fixed-`sigma` density upper bound,
including (2.1).  It also respects the Vinogradov--Korobov exclusion: at
height `Gamma_n` the forbidden distance from one is exponentially smaller
than `1/n`.  Functional symmetry holds by construction.

This is not claimed to be the divisor of an Euler product.  Its sole role
is logical: Riemann--von Mangoldt, functional symmetry, classical
zero-free regions, and global density upper bounds are jointly compatible
with (1.2).  A proof for actual zeta needs a new zeta-specific lower or
replication mechanism.

The functional equation itself only maps a nontrivial zero at `beta+i*gamma`
to zeros at `1-beta+i*gamma` and the conjugate ordinates.  It cannot move a
known critical-line zero toward one.  Trivial zeros at negative even
integers do not furnish reflected zeta zeros to the right of one: the
gamma/sine factors in the functional equation account for them.

Classical zero repulsion has the same polarity.  The zeta zero-free region
excludes points near one.  Deuring--Heilbronn repulsion is triggered by an
exceptional real zero in a varying family of Dirichlet `L`-functions; it
does not create a complex off-line zero of the fixed Riemann zeta function.

## 6. Almost periodicity, random models, and logic

### Bohr almost periodicity and resonance

In `Re(s)>1`, the absolutely convergent Euler product is nonzero, and its
almost-periodic vertical behavior is therefore a model of recurrence
without zeros.  In the critical strip, universality and resonance prove
rich value distribution, but large values, small values, and phase
recurrence at isolated points do not determine the argument change on a
closed contour.  The first exact new statement required is one of:

```text
a winding-one contour approximation as in (4.3), or
a horizontal lower bound N(sigma;T,2T)>=1 on arbitrarily high blocks.   (6.1)
```

For every `sigma>1/2`, either assertion already proves an off-critical
zero.

### Random Euler products and random matrices

Random Euler-product models are value-distribution models.  Where the
random product converges it is an exponential of a random logarithm and is
nonzero.  Random-matrix characteristic-polynomial models place their
model zeros on the symmetry locus corresponding to the critical line.
Random Mobius heuristics predict square-root cancellation.  These common
heuristics therefore do not predict (1.2); if anything, they align with RH.
No almost-sure theorem for a random model transfers a zero to the fixed
deterministic zeta function.

### Logical or model-theoretic independence

No independence of RH from ZFC is known.  Even a future independence
theorem would not prove (1.2) in the standard complex numbers.  Moreover,
`not RH` and `Theta=1` are different sentences: a model could satisfy an
off-line zero while still having `Theta<1`.  Beurling generalized-prime
systems and other zeta-like countermodels likewise establish only what
coarse axioms fail to determine, not where the zeros of Riemann zeta lie.

## 7. The first genuinely new theorem that would be sufficient

There are three exact, non-circular promotion gates.

1. **Near-linear prime oscillation.**  Prove (3.7), equivalently

   ```text
   limsup log(1+abs(psi(x)-x))/log x=1.                  (7.1)
   ```

2. **Near-linear Mobius oscillation.**  Prove (3.8), equivalently the
   analogous limsup for `M(x)`.

3. **Sparse winding near one.**  For every `sigma<1`, find a disc contained
   in `sigma<Re(s)<1` and arbitrarily high shifts satisfying a
   winding-one approximation such as (4.3).

Each gate proves `Theta=1`; none follows from a known theorem.  Gate 3 is
stronger than the bare existence claim because a zero need not carry a
prescribed local linear profile.  Gates 1 and 2 are exact reformulations of
the divisor edge through generalized Littlewood theory, not easier
corollaries of the known omega theorems.

The earliest unavoidable barrier is even simpler:

```text
prove one zero rho of zeta with Re(rho)>1/2.              (7.2)
```

No audited route crosses (7.2).  Failure to prove a fixed strip is not
evidence for (1.2), just as failure to prove RH is not evidence for an
off-line zero.

## 8. Novelty and publishability

The card supplies a useful exact synthesis and the short proof that
positive-density winding universality is impossible for zeta.  That proof
is a standard corollary of Rouche plus Bohr--Landau/Ingham density, not a
new research result.  The growth identities (3.2)--(3.3) are classical
generalized Littlewood theory and were already recorded in R98.

Accordingly:

```text
mathematical correctness as a no-go/exponent card: likely publishable
                                                     only as exposition;
novel theorem about actual zeta zeros:               none;
claim Theta=1 or failure of every fixed strip:        not publishable;
new research target isolated with exact quantifiers: yes.              (8.1)
```

## Primary literature and status anchors

* [S. M. Voronin, *Theorem on the universality of the Riemann
  zeta-function*](https://www.mathnet.ru/eng/im2037), Math. USSR-Izv. 9
  (1975), 443--453.
* [Y. Lamzouri, S. Lester, and M. Radziwill, *An effective universality
  theorem for the Riemann zeta-function*](https://arxiv.org/abs/1611.10325),
  which states the nonvanishing-target and positive-density clauses
  explicitly.
* [J. Andersson, *Lavrentiev's approximation theorem with nonvanishing
  polynomials and universality of zeta-functions*](https://arxiv.org/abs/1010.0386),
  for removal of nonvanishing only on compact sets without interior.
* [T. Nakamura, *The generalized strong recurrence for non-zero rational
  parameters*](https://arxiv.org/abs/1006.1778), for the distinction
  between strong recurrence and strong universality and the RH equivalence.
* [A. E. Ingham, *On the estimation of
  N(sigma,T)*](https://doi.org/10.1093/qmath/os-11.1.201), Quart. J. Math.
  os-11 (1940), 201--202, for a density bound implying (4.6).
* [L. Guth and J. Maynard, *New large value estimates for Dirichlet
  polynomials*](https://arxiv.org/abs/2405.20552), for modern zero-density
  bounds; these remain upper bounds and permit sparse edge zeros.
* [K. Ford, *Zero-free regions for the Riemann zeta
  function*](https://arxiv.org/abs/1910.08205), for an explicit
  Vinogradov--Korobov region.  Its boundary tends to one and is not a fixed
  strip.
* [G. H. Hardy and J. E. Littlewood, *Contributions to the theory of the Riemann
  zeta-function and the theory of the distribution of
  primes*](https://doi.org/10.1007/BF02422942), Acta Math. 41 (1916),
  119--196, for the classical square-root-power oscillation theorem.
* [A. M. Odlyzko and H. J. J. te Riele, *Disproof of the Mertens
  conjecture*](https://doi.org/10.1515/crll.1985.357.138), J. Reine Angew.
  Math. 357 (1985), 138--160.  This does not disprove RH.
* [K. Soundararajan, *Partial sums of the Mobius
  function*](https://arxiv.org/abs/0705.0723), J. Reine Angew. Math. 631
  (2009), 141--152, for RH-conditional square-root/subpower upper behavior.
* [Clay Mathematics Institute, Millennium Prize Problems](https://www.claymath.org/millennium-problems/),
  for the current unresolved status of RH.
