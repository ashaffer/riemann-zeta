# Selected transition: finite-group thresholds and the gap-four gate

**Date:** 2026-08-13  
**Status:** exact finite-group moment thresholds and an exact near-quarter
gap-four reduction are proved; no published theorem located supplies the
required fixed-power prime-pair cancellation.

## Verdict

After deleting the selected `q`-multiples first, the remaining signed
transition has an exact residue vector.  For one curvature block of length
`H=Y^h`, modulus `q=Y^b`, and target bill

```text
kappa=kappa_max=.0197404825829...,
.1537<=b<=min(h,.2481203...),
```

the all-frequency `L2` and `L4` sufficient thresholds are, in the repository's
**twice-mass** normalization,

```text
sum_r |v(r)|^2
    <=4 H^2 Y^(-2 kappa)/q,                          (0.1)

sum_s |sum_r v(r) conjugate(v(r+s))|^2
    <=16 H^4 Y^(-4 kappa)/q.                         (0.2)
```

Either estimate forces the selected coefficient to be at most
`H Y^(-kappa)`.  These thresholds are exact consequences of finite Fourier
orthogonality; they do not use a heuristic numerator average.

The most dangerous elementary fixed-gap test does simplify.  If
`q=3 (mod 4)` and `a=(q+1)/4`, then, up to `O(H/q+1)`, the gap-four part of
the exact nonresonant transition is

```text
2i(1+e(1/q))
 sum_(p,p+4 prime in I) chi_4(p)e(p/(4q)).            (0.3)
```

Every prime pair `p,p+4>3` is automatically consecutive, since `p+2` is
divisible by `3`.  Thus this sector avoids the unbounded-order
inclusion--exclusion problem: it is exactly a twisted cousin-prime
discrepancy.  Unfortunately, it lands on a fixed-shift parity boundary.
Selberg restriction controls frequency averages, and the strongest located
prime-pair theorems average the shift or the modulus.  None gives a
pointwise power bound for the fixed shift `4` and the height-selected `q`.

The underlying cousin-prime support was already isolated in
[`ZETA23-NONPOLE-NEAR-RESIDUE-TRANSFER-FAIL-FAST-2026-08-13.md`](ZETA23-NONPOLE-NEAR-RESIDUE-TRANSFER-FAIL-FAST-2026-08-13.md).
What is new here is its exact normalization inside the q-first signed
transition, the harmless `O(H/q+1)` puncture error, and its integration with
the finite-group `L2/L4` thresholds.

A clean sufficient new theorem would be

```text
sup_(I,q) |sum_(p,p+4 prime in I) chi_4(p)e(p/(4q))|
   << H q^(-delta)Y^o(1),

delta>kappa/.1537=.1284351502....                    (0.4)
```

The often plausible `q^(-1/8)` saving is **not quite enough** at the lower
denominator endpoint: it misses by the `Y`-exponent

```text
kappa-.1537/8=.00052798259....                       (0.5)
```

Equation (0.4) would settle this one fixed-gap sector, not the entire signed
tail.  For the whole tail, (0.1), (0.2), or a direct selected-frequency
analogue remains the minimal coefficient-specific input.

No zero-free strip is claimed.

---

## 1. Exact block normalization

Let `I` be a physical block and perform the exact telescope

```text
integers -> integers with q-multiples removed -> terminal primes.
```

Fold twice the signed mass of the second arrow modulo `q` and call the
result `v_I(r)`.  For the frozen additive character,

```text
R_I(a/q)=1/2 sum_(r mod q)v_I(r)e_q(ar).              (1.1)
```

The factor `1/2` is essential: `v_I` stores twice each trapezoid coefficient
so that the vector is integral before adding a smooth taper.  In the
untapered finite transport, `sum_r v_I(r)=0`, because the initial and final
Voronoi measures have the same total mass.  The moment identities below do
not require this zero-mass fact.

The architecture has `K asyp Y/H` curvature blocks and may select a different
reduced `(a_I,q_I)` on every block.  A sufficient local target is

```text
|R_I(a_I/q_I)|<=H Y^(-kappa).                        (1.2)
```

Summing (1.2) gives the global `Y^(1-kappa)` bill.  More generally, the
aggregate thresholds in Section 2 permit nonuniform block energies.

---

## 2. Exact `L2` and `L4` threshold theorem

For an arbitrary complex vector `v` on `Z/qZ`, put

```text
F(a)=1/2 sum_r v(r)e_q(ar),
C(s)=sum_r v(r) conjugate(v(r+s)).                   (2.1)
```

Finite Fourier orthogonality gives

```text
sum_(a mod q)|F(a)|^2 =q/4 sum_r |v(r)|^2,           (2.2)

sum_(a mod q)|F(a)|^4 =q/16 sum_s |C(s)|^2.          (2.3)
```

Since the selected reduced numerator is one of the frequencies on the left,
(0.1) or (0.2) implies (1.2).  Including imprimitive and principal
frequencies makes these sufficient estimates stronger, never weaker; no
unproved transfer from an average to a selected numerator is hidden here.

If `H=Y^h` and `q=Y^b`, the corresponding power thresholds are

```text
L2 residue energy exponent:       2h-b-2kappa,
L4 correlation energy exponent:   4h-b-4kappa.       (2.4)
```

At the top-aperture block exponent `h=33/133=.24812030075...`:

| selected denominator | `L2` exponent | `L4` exponent |
|---|---:|---:|
| `b=.1537` | `.303059636324...` | `.759819272648...` |
| `b=h` | `.208639335572...` | `.665398971896...` |

There is also an exact aggregate version.  Hölder and (2.2)--(2.3) show

```text
sum_I |R_I|
 <=(K/4 sum_I q_I sum_r |v_I(r)|^2)^(1/2),           (2.5)

sum_I |R_I|
 <=(K^3/16 sum_I q_I sum_s |C_I(s)|^2)^(1/4).        (2.6)
```

Consequently it suffices to prove

```text
sum_I q_I sum_r |v_I(r)|^2
 <=4Y^(2-2kappa)/K,                                  (2.7)

sum_I q_I sum_s |C_I(s)|^2
 <=16Y^(4-4kappa)/K^3.                               (2.8)
```

When `K=Y/H`, the right-side exponents, with constants suppressed, are

```text
1+h-2kappa,             1+3h-4kappa.                 (2.9)
```

At `h=33/133` these are `1.208639335572...` and
`1.665398971896...`, respectively.  Equations (2.7)--(2.8) are the exact
family targets if a future dispersion theorem naturally averages the
blockwise vectors before the selected numerators are inserted.

---

## 3. Exact near-quarter gap-four reduction

Let `q>4`, `q=3 (mod 4)`,

```text
a=(q+1)/4,             z=e_q(a)=i e(1/(4q)).         (3.1)
```

Consider a terminal prime edge `[p,p+4]` that contains no interior multiple
of `q`.  Its prime trapezoid is

```text
2(z^p+z^(p+4)),
```

whereas its integer trapezoid is

```text
z^p{(1+z^4)/2+z+z^2+z^3}.
```

Hence its nonresonant transition charge is

```text
z^p K_4(z),
K_4(z)=3/2(1+z^4)-(z+z^2+z^3).                      (3.2)
```

The integer-edge polynomial

```text
B_4(z)=(1+z^4)/2+z+z^2+z^3                         (3.3)
```

satisfies `B_4(i)=0` and `|B_4'(z)|<=8` on the unit circle.  Since
`|z-i|<=pi/(2q)`,

```text
K_4(z)=2(1+z^4)+O(1/q).                              (3.4)
```

An edge containing an interior `q`-multiple has the explicit punctured
integer base instead.  There are `O(H/q+1)` such disjoint terminal edges,
and deleting one integer cell changes its unit-modulus trapezoid by at most
`2`.  Summing (3.4) therefore gives

```text
R_(I,4)(a/q)
 =2(1+z^4) sum_(p,p+4 consecutive in I) z^p
  +O(H/q+1).                                         (3.5)
```

For `p>3`, primality of `p` and `p+4` forces `p+2` to be the member of
`p,p+2,p+4` divisible by `3`; it is composite.  Thus the word
`consecutive` in (3.5) may be removed exactly.  Also, for odd prime `p`,

```text
z^p=i chi_4(p)e(p/(4q)),        z^4=e(1/q).           (3.6)
```

Equations (3.5)--(3.6) prove (0.3).  The multiplier has modulus

```text
|2(1+e(1/q))|=4|cos(pi/q)|asymp 1.                  (3.7)
```

Since `q>=Y^.1537` and `.1537>kappa`, the error `H/q+1` is below the
required local target throughout the retained range (with the usual
nondegenerate block convention).  The gap-four problem is therefore the
twisted cousin-prime sum in (0.4), up to harmless constants.

This reduction is useful precisely because it is not another generic
successor-gap reformulation: gap four is a fixed two-prime correlation, and
the rational phase has become a mod-`4` character times a slow phase of
period `4q`.

---

## 4. Fail-fast tests of standard prime machinery

### 4.1 Selberg sieve and restriction

The upper-bound sieve gives only

```text
#{p in I:p,p+4 prime} << H(log Y)^(-2)Y^o(1).        (4.1)
```

This is logarithmically, not power, below `H`.  More importantly, a positive
Selberg majorant cannot be inserted through a complex sign to bound (0.4)
with cancellation.

Green and Tao's
[*Restriction theory of the Selberg sieve, with applications*](https://arxiv.org/abs/math/0405581),
Theorem 1.1, proves for a prime-pair exponential sum an `L^p` frequency
bound of the natural size for every fixed `p>2`.  Even granting the ideal
localized analogue

```text
||S_I||_p << H^(1-1/p)(log Y)^(-2)Y^o(1),            (4.2)
```

Bernstein localization of a degree-`H` trigonometric polynomial costs
`H^(1/p)` and returns only `H(log Y)^(-2)Y^o(1)`.  The theorem controls how
many frequencies are large; the height rule is allowed to select one such
frequency.  It does not prove (0.4).

### 4.2 Vaughan and Heath--Brown identities

For one natural `Lambda` coefficient, Vaughan's classical global minor-arc
bound has ample saving in the retained denominator range.  It does not
survive either required operation here:

1. differencing global prefixes produces a bound larger than the physical
   block when `H` is short;
2. inserting the second prime condition leaves, in a Type-I piece, a
   coupled coefficient such as `Lambda(mn+4)`, and in Type II a shifted
   bilinear incidence rather than two separated coefficient sequences.

Applying Heath--Brown identities to both prime factors is exact, but the
constraint that the two reconstructed products differ by `4` is the fixed
shifted prime-pair problem.  Cauchy before exploiting that constraint loses
the phase; Cauchy after it asks for the same shifted correlation.  No
available identity supplies a fixed `q`-power saving by itself.

At the special numerator (3.1), this failure is especially transparent:
the quarter-frequency factor becomes `chi_4(p)`, leaving the discrepancy
between cousin pairs with lower member `1 mod 4` and `3 mod 4`, modulated by
the slow phase `e(p/(4q))`.  Ordinary prime equidistribution modulo `4` says
nothing about this two-prime discrepancy.

### 4.3 Dispersion theorems average the wrong variable

Mikawa's
[*On prime twins in arithmetic progressions*](https://tsukuba.repo.nii.ac.jp/record/16157/files/8.pdf)
proves a Bombieri--Vinogradov-type theorem for prime-pair errors averaged
over the shift and modulus.  It is strong evidence that dispersion is the
right language, but it permits the fixed shift `4` and a height-selected
modulus to be exceptional.

Matomaki--Radziwill--Tao's
[*Correlations of the von Mangoldt and higher divisor functions I*](https://arxiv.org/abs/1707.01315),
Theorem 1.3, proves the expected `Lambda(n)Lambda(n+h)` asymptotic for
almost all shifts in a window of length at least `Y^(8/33+epsilon)`.  It has
no additive twist and again may discard the single shift `h=4`.

Murty--Vatwani's
[*Twin primes and the parity problem*](https://mast.queensu.ca/~murty/TwinPrimes-Parity.pdf)
is a useful warning about scope: it formulates additional shifted-prime
equidistribution precisely to cross the parity barrier.  The needed
equidistribution is conjectural, not a consequence of Bombieri--Vinogradov.

Ford--Maynard's
[*On the theory of prime producing sieves*](https://arxiv.org/abs/2407.14368)
gives sharp results and counterexamples for nonnegative sequences satisfying
specified Type-I/Type-II axioms.  It does not state a no-go theorem for the
specific signed twisted cousin-pair sum (0.4).  It therefore cannot be used
to declare this route impossible; it does rule out treating unspecified
Type-I information as if it already contained the missing parity-sensitive
estimate.

### 4.4 Well-factorable exponential-sum and transference inputs

Matomaki's
[*A Bombieri--Vinogradov type exponential sum result with applications*](https://doi.org/10.1016/j.jnt.2009.01.010)
is genuinely relevant to the near-quarter phase, but only for a sieve
surrogate.  Her Theorem 1 bounds

```text
sum_(d asyp D) lambda_d
 sum_(n asyp Y, n=-4 mod d) Lambda(n)e(alpha n)        (4.3)
```

for every well-factorable `lambda` of level `D`, where `alpha` has a rational
approximant of denominator `q_alpha`.  Taking the exact
`alpha=a/q=(q+1)/(4q)`, `K=1`, and `D=Y^(2/5)`, the theorem's displayed bound
has exponent

```text
1-min(b/4,1/20)+O(eta),       q=Y^b.                 (4.4)
```

Indeed the largest exponent inside its fourth root is
`max(1-b,4/5)`.  Thus the worst global-model saving in the retained range is
`.1537/4=.038425`, which is larger than `kappa`.  This confirms that the
linear phase itself is not the obstruction.

It does not prove (0.4), for two exact reasons.  First, (4.3) is a full
dyadic sum of length `asymp Y`; no stated short-interval version has error on
the curvature-block scale `H=Y^h`, and differencing full prefixes leaves an
error much larger than `H`.  Second, the divisor weight

```text
w(n+4)=sum_(d|n+4) lambda_d
```

is a linear/Chen-sieve model, not `1_(n+4 prime)`.  An upper-bound weight
`w^+>=1_prime` cannot be passed through a complex phase: in general

```text
|sum u_n 1_prime(n+4)| <= |sum u_n w^+(n+4)|
```

is false for `|u_n|=1`.  The valid triangle inequality discards the phase and
returns only the positive twin-sieve mass `H(log Y)^(-2)Y^o(1)`, which is not
a fixed-power saving.  Equivalently, writing the prime indicator as the
majorant minus its excess leaves an excess of natural sieve size, not a
power-small `L1` error.  Producing a factorable signed approximation with a
power-small selected Fourier error is precisely the missing parity-sensitive
input; Matomaki's theorem does not produce it.

Grimmelt--Teravainen's
[*The exceptional set in Goldbach's problem with almost twin primes*](https://arxiv.org/abs/2207.08805)
makes this sign boundary explicit.  Proposition 6.5 proves pointwise Fourier
transference, uniformly in the frequency, for **model functions**
`Lambda(n) omega_1(n+a) omega_2(n+a)` on `[1,N]`, with `omega_2` an
admissible main sieve of level `N^(1/2-epsilon)`.  It does not put the exact
shifted-prime indicator in that model class.  Moreover, Section 2.1 notes
that an order inequality transfers through a convolution only when the
other function is nonnegative; their nonnegative-model architecture is what
avoids a vector-sieve constant loss.  Our test function
`chi_4(n)e(n/(4q))1_I(n)` is signed/complex, so that order step is unavailable.
Their conclusions concern almost-twin additive convolutions outside an
exceptional set, not a single exact cousin-pair Fourier coefficient on every
short block.  This is therefore a conditional model transfer, not a theorem
for (0.4).

Bazin's 2026 preprint
[*A Bombieri--Vinogradov theorem for exponential sums over products of k
primes*](https://arxiv.org/abs/2607.15137), Theorem 2, treats the unshifted
sequence `1_(Omega(n)=k)` on the full prefix `n<=x`, averaged over all
denominators `q<=Q`, with

```text
Q<=x^(1/3)(log x)^(-B),
|lambda|<=Q^(-3)(log x)^(-B),                        (4.5)
```

and a logarithmic aggregate error.  It contains neither the joint shifted
factor `1_prime(n)1_prime(n+4)` nor curvature-block localization.  The
tempting identity `Omega(n(n+4))=2` for a cousin pair does not help: the
paper sums linearly over the product variable, whereas the required support
is the thin quadratic set `m=n(n+4)` and the phase is linear in `n`, not in
`m`.  Bazin's theorem is therefore inapplicable to (0.4), rather than a
hidden fixed-gap estimate.

In short:

```text
Matomaki 2009:              CONDITIONAL TRANSFER TO A SIEVE MODEL ONLY
Grimmelt--Teravainen 2022:  CONDITIONAL TRANSFER TO NONNEGATIVE MODELS ONLY
Bazin 2026:                 INAPPLICABLE TO THE SHIFTED JOINT SUPPORT
direct published theorem for (0.4):                  NONE
```

---

## 5. The precise minimal new estimates

There are two differently scoped targets.

### 5.1 Whole signed transition

For every selected block, prove (0.1), (0.2), or directly

```text
|1/2 sum_r v_I(r)e_(q_I)(a_I r)|
    <<H Y^(-kappa-epsilon).                          (5.1)
```

The family versions (2.7)--(2.8) are enough if a dispersion argument first
averages over blocks.  This is the estimate that would close the whole
signed q-first tail.

### 5.2 Fixed-gap falsification target

For the gap-four sector alone, (0.4) is sufficient.  If the new theorem is
of the scale `Hq^(-delta)Y^o(1)`, its worst denominator is
`q=Y^.1537`, and hence

```text
delta>.01974048259/.1537=.1284351502....             (5.2)
```

is the exact uniform-kill threshold.  A direct `H Y^(-kappa-epsilon)`
estimate is equivalent for present purposes.  The estimate must be uniform
on the physical blocks and at the selected individual modulus; averaging
only over shifts, moduli, or numerators does not meet the quantifiers.

Proving (5.2) does not count cousin primes and does not imply their
infinitude: the sum could be small because the pair set is empty.  Calling it
"the twin-prime conjecture" would therefore overstate the barrier.  It is,
however, a genuinely new fixed-shift, parity-sensitive Fourier theorem.

---

## 6. Exact finite audit

The existing tool
[`src/universal_q_reorder_transport.py`](../src/universal_q_reorder_transport.py)
computes the integer-to-no-`q`-multiples-to-primes telescope, the exact
twice-mass residue vector, Parseval and fourth moments, and the actual-prime
gap sectors.  Its test suite and the companion SPF residue tests pass.

On `[100003,199999]`, at the near-quarter numerators:

| `q` | `a=(q+1)/4` | full nonresonant tail / block length | gap-four sector / block length |
|---:|---:|---:|---:|
| 43 | 11 | `.00980679` | `.00105010` |
| 59 | 15 | `.00413298` | `.00036011` |
| 83 | 21 | `.01658823` | `.00123611` |

There are `919` actual gap-four edges in each scan.  The new verifier checks
their automatic consecutiveness, reconstructs their q-punctured transition
charge edge by edge, and certifies (0.3) with the explicit error from
`B_4(z)` and the q-punctured edges.

These are frozen finite diagnostics.  The broad contribution of other gap
sectors means the data neither prove the gap-four estimate nor reduce the
whole tail to gap four.

Run:

```bash
PYTHONPATH=src python3 -m unittest -v \
  src/test_universal_q_reorder_transport.py \
  src/test_spf_residue_transport.py
python3 results/verify_zeta23_selected_transition_fixed_gap_gate.py
```

---

## 7. Truth boundary

```text
twice-mass Parseval identity (2.2):                  EXACT
twice-mass fourth-moment identity (2.3):             EXACT
per-block L2/L4 sufficient thresholds:               PROVED
selector-varying aggregate thresholds:               PROVED
gap-four pairs automatically consecutive:            PROVED
near-quarter twisted cousin reduction (0.3):          PROVED
q^(-1/8) sufficient at the lower endpoint:            NO
Selberg restriction gives selected pointwise power:   NO
Mikawa/MRT cover fixed shift 4 and selected q:         NO
Matomaki controls the full-shell factorable model:     YES
Matomaki transfers through exact cousin support:       NO
Grimmelt--Teravainen transfers the complex order step: NO
Bazin treats the shifted cousin-pair support:           NO
published no-go eliminating the twisted estimate:     NOT FOUND
twisted cousin-pair power estimate (0.4):             OPEN
whole signed nonresonant transition:                  OPEN
full antenna / zero-free strip:                       NOT CLAIMED
```
