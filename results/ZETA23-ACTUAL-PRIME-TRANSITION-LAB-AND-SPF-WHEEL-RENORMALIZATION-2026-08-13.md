# Actual-prime transition laboratory and SPF-wheel renormalization

**Date:** 2026-08-13

## Verdict

A reusable finite laboratory now computes the actual-prime consecutive-gap
transition without replacing it by an ordinary prime sum.  It includes the
exact logarithmic Voronoi masses, the symmetrized gap trapezoid, every
nonzero additive mode for every prime modulus in a configurable range, the
principal component, exact-pole and near-residue sectors, additive and
multiplicative Parseval energies, transition-character reconstruction, the
renewal `1/q` comparison, an intermediate `q`-rough sieve, and an optional
common-height curvature-block selector.

The computation uncovered two structural facts.

1. **Wheel-aligned near residues have macroscopic positive mass.**  A selected
   numerator can map the fixed wheel gaps `W,2W,...,R W` into phase distance
   at most `R`, independently of the size of `q`.  In the canonical shell,
   the `W=6`, `R=3` sector has mass fraction `.2919687826` for every scanned
   `q` above the maximum gap.  Thus removing the literal `q|g` pole does not
   make the unsigned near-residue sector small.
2. **The SPF deletion telescope isolates the only uniformly resonant stage.**
   At stage `p=q`, every deleted center has phase one.  Every later stage
   `p>q` is nonresonant at its deleted centers.  Earlier stages `p<q` are not
   pointwise nonresonant: for example, stage `p=2` deletes `x=2q`, whose phase
   is one.  Their aggregate target mode nevertheless vanishes on a complete
   common wheel period.  The `q`-stage is an explicit real adjacent-wheel-gap
   correlation of natural size `1/q`.  This suggests a new route: prove a
   localized pre-`q` prefix estimate, control the `q`-stage by rough-gap mass,
   and prove cancellation in the genuinely nonresonant post-`q` deletion
   tail, rather than transfer the successor-prime coefficient to a one-prime
   sum.

The second fact is a genuine reorganization of the live arithmetic target.
It is not yet a power-saving theorem on growing finite shells.  In particular,
the pre-`q` primorial is exponentially larger than the shell when
`q=Y^b`, so complete-wheel periodicity cannot simply be invoked.  No
zero-free strip is claimed.

---

## 1. Reproducible artifacts

The main implementation is

```text
src/actual_prime_transition_lab.py
```

and its independent replay entry point is

```text
src/verify_actual_prime_transition_lab.py.
```

The canonical deterministic output is

```text
results/ZETA23-ACTUAL-PRIME-TRANSITION-LAB-100K-2026-08-13.json
sha256(payload)=ccdc062f004fea661c5cfd7291e1504c45476f74b419117afd9a7d9561c092d8.
```

It is reproduced and checked by

```bash
python3 src/verify_actual_prime_transition_lab.py \
  results/ZETA23-ACTUAL-PRIME-TRANSITION-LAB-100K-2026-08-13.json
```

The SPF deletion implementation and a canonical rational diagnostic are

```text
src/prime_gap_sieve_deletion.py
results/ZETA23-SPF-DELETION-Q19-100K-2026-08-13.json.
```

The joint regression suites are

```text
src/test_actual_prime_transition_lab.py
src/test_prime_gap_sieve_deletion.py.
```

They contain fourteen tests, including segmented-sieve fixtures, exact
Voronoi partition, direct-versus-residue Fourier equality, additive and
character Parseval closure, pole reconstruction, deterministic JSON replay,
the `q`-rough mass ledger, wheel alignment, the circular one-hole wheel, and
the complete pre-`q` wheel-stage constants.

---

## 2. The three finite objects are kept distinct

Let the shell be `[Y,rho Y]`, put `v_p=log(p/Y)`, and let `phi` be the selected
window.  The exact logarithmic Voronoi mass at a prime node is

```text
lambda_p = integral_(C_p intersect [0,log rho]) phi(u) du,             (2.1)
```

where `C_p` is bounded by the logarithmic midpoints to the neighboring
primes.  The laboratory evaluates (2.1) from an analytic antiderivative.  Its
additive coefficient is

```text
V_q(a)=sum_p lambda_p e_q(ap).                                         (2.2)
```

The leading symmetrized consecutive-gap object is separately

```text
T_q(a)=1/2 sum_(p<p^+ consecutive) log(p^+/p)
       [phi(v_p)e_q(ap)+phi(v_(p^+))e_q(ap^+)].                        (2.3)
```

For a gap `g=p^+-p`, its positive edge mass is

```text
w_g=log(p^+/p)[phi(v_p)+phi(v_(p^+))]/2.                               (2.4)
```

The pole mass is exactly the part with `q|g`.  At mode `a`, phase-distance
`k` means

```text
min(a g mod q,-a g mod q)=k.                                          (2.5)
```

No scalar transfer between (2.2), (2.3), and an ordinary `Lambda` sum is
inserted.

For each prime `q`, the code also forms the residue mass vector and its full
additive DFT, as well as the multiplicative-character DFT.  For the successor
transition it forms the histogram of

```text
p^+/p mod q.                                                          (2.6)
```

Character orthogonality reconstructs the pole mass from (2.6).  All three
Parseval/reconstruction errors in the canonical output are below `2e-10`,
and the verifier recomputes the primes and the complete JSON payload.

---

## 3. Exact wheel-alignment lemma

### Lemma 3.1 (finite wheel capture)

Let `q` be an odd prime larger than every gap in a finite list of consecutive
primes.  Let `W` be even, `(W,q)=1`, and `RW<q`.  Choose

```text
a == plus_or_minus W^(-1) mod q.                                      (3.1)
```

Then the phase-distance-`R` sector of (2.5) contains exactly the gaps

```text
W,2W,...,RW.                                                          (3.2)
```

**Proof.**  If `g=kW`, then `ag=plus_or_minus k mod q`.  Conversely,
phase distance at most `R` gives `g == plus_or_minus kW mod q` for some
`0<=k<=R`.  Since `0<g<q`, the positive sign gives (3.2).  The negative
representative is `q-kW`, which is odd, whereas every prime gap in the shell
is even.  The zero representative is excluded by `g<q`.  This proves the
identity.  The code verifies the two positive masses independently. `QED`

The canonical shell is `[100000,200000]`, has `8392` interior primes and
maximum gap `86`, and uses near radius `R=3`.  For `q>=89` the exact captures
are

| wheel `W` | captured gaps | mass fraction |
|---:|---|---:|
| 2 | `2,4,6` | `.1471889013` |
| 6 | `6,12,18` | `.2919687826` |
| 30 | `30,60,90` (when `3W<q`; the shell has no gap 90) | `.0553845281` |

The `W=6` mode is the largest positive near sector for `q=89,101,127,151`.
This is the wheel fingerprint that an unsigned argument misses.  It does not
show that the signed coefficient is large: cancellation across the starting
prime residues remains possible and is exactly the desired phenomenon.

The special near-pole from the transfer audit is also emitted explicitly.
For every `q=3 mod 4`,

```text
a=(q+1)/4,             4a=q+1,                                      (3.3)
```

so every gap-four edge lies in phase-distance one.  On the canonical shell
the positive gap-four mass fraction is `.0365`, while its signed normalized
coefficient is `.00765,.00504,.00239,.00125,.00048` at
`q=11,19,43,59,151`.  Finite data therefore exhibit substantial signed
cancellation even though the positive mass does not shrink with `q`.

---

## 4. The `q`-rough intermediate control

Before deleting multiples of `q`, define

```text
S_(<q)={n: n has no prime factor below q}.                             (4.1)
```

The laboratory constructs this sequence directly on the shell, computes its
own exact logarithmic Voronoi cells, and measures the mass on `q|n`.  It also
reports the physical rough-gap second moment.

| `q` | points in (4.1) | `q`-divisible nodes | mass fraction | fraction / `(1/q)` | fraction / `q^(-1/2)` | `E(g^2)/E(g)^2` |
|---:|---:|---:|---:|---:|---:|---:|
| 11 | 22858 | 2078 | `.0909107` | `1.0000` | `.3015` | `1.2321` |
| 19 | 18052 | 951 | `.0525069` | `.9976` | `.2289` | `1.3331` |
| 43 | 14519 | 325 | `.0223595` | `.9615` | `.1466` | `1.4297` |
| 79 | 12688 | 165 | `.0135533` | `1.0707` | `.1205` | `1.4841` |
| 151 | 10926 | 95 | `.0089069` | `1.3449` | `.1095` | `1.5391` |

The last row has only `95` selected nodes and visibly larger finite-count
noise.  Across the usable rows, the mass is organized around `1/q`, not
`q^(-1/2)`.  The normalized second moment is stable across shell rescalings
and remains below the exponential-renewal value `2`; it does not reveal a
hidden square-root mass inflation.

There is an exact periodic explanation.  Put

```text
P=product_(p<q) p.                                                     (4.2)
```

On the circular `P`-periodic wheel, any local Voronoi weight is `P`-periodic.
Over `qP`, multiplication by `q` permutes the residues modulo `P`, so the
weighted mass on `q|n` is exactly `1/q` of the total mass.  The displayed
finite logarithmic/tapered shell is not a complete wheel period, so the table
is evidence about localization, not an invocation of this periodic identity.

---

## 5. Additive and transition energies

After subtracting the uniform-unit principal contribution

```text
- total_mass/(q-1),                                                    (5.1)
```

the canonical symmetrized-gap spectra give

| `q` | selected maximum | additive RMS | RMS / `(1/q)` | transition-character RMS | pole fraction |
|---:|---:|---:|---:|---:|---:|
| 11 | `.01441` | `.00915` | `.101` | `.05309` | `.054273` |
| 19 | `.01914` | `.01243` | `.236` | `.04599` | `.015359` |
| 43 | `.01602` | `.01050` | `.452` | `.02815` | `.001142` |
| 79 | `.01943` | `.00956` | `.755` | `.01927` | `0` |
| 101 | `.01761` | `.00968` | `.978` | `.01834` | `0` |
| 127 | `.03011` | `.00945` | `1.200` | `.01907` | `0` |
| 151 | `.02125` | `.00988` | `1.492` | `.01648` | `0` |

Because the maximum shell gap is `86` and every gap is even, `q|g` forces
`g>=2q`; hence the exact pole vanishes for every `q>=47` in this fixture.
The near sectors do not vanish, by Lemma 3.1.

At fixed `q=151`, auxiliary deterministic shells starting at `10^4,10^5,10^6`
contain `1033,8392,70435` primes and give additive RMS

```text
.029063, .009884, .003289,
```

so `sqrt(N)*RMS=.934,.905,.873`.  The crossing above the `1/q` line in the
small canonical shell is therefore a finite-sample floor, not evidence for
an asymptotic obstruction.  These numerics neither prove the `1/q` law nor
exclude a sparse selected-frequency anomaly.

---

## 6. Exact SPF-stage telescope

For an ordered active integer set `S` and arbitrary complex data `f`, put

```text
T(S;f)=1/2 sum_(x<y consecutive in S)(y-x)[f(x)+f(y)].                 (6.1)
```

Deleting an interior point `x`, whose active neighbors are `l<x<r`, changes
the trapezoid by the exact local charge

```text
D_x=1/2[(r-x)f(l)+(x-l)f(r)-(r-l)f(x)].                               (6.2)
```

Deleting interior composites in increasing least-prime-factor stages gives

```text
T({retained endpoints and primes};f)
  =T(integers;f)+sum_p D_p.                                           (6.3)
```

When the two retained endpoints are prime, the left side is literally the
prime trapezoid.  Otherwise it is the endpoint-augmented prime trapezoid used
by the finite ledger.

This is the sought Abel/telescoping localization: the code now reports the
complex contribution and cumulative sum before, at, and after any chosen
stage, together with neighboring stage phases, `L1/L2` ledgers, and exact
closure errors.

Take `f(n)=e_q(an)`.  Immediately before stage `q`, the active infinite wheel
is the set of residues coprime to `P` in (4.2).  Over one circular length
`qP`, its coefficient vanishes exactly because

```text
sum_(j=0)^(q-1)e_q(a jP)=0.                                           (6.4)
```

At stage `q`, every deleted center has phase one.  If `L_x,R_x` are the
adjacent gaps of the pre-`q` wheel, multiplication by `q` permutes its
residues and (6.2) becomes the exact complete-wheel constant

```text
D_q^wheel(a)
 =1/(2qP) sum_(x mod P, (x,P)=1)
   [R_x e_q(-aL_x)+L_x e_q(aR_x)-(L_x+R_x)].                           (6.5)
```

Reflection of the wheel swaps `L` and `R` and conjugates the summand.  Thus
(6.5) is real.  The checker enumerates the wheel for feasible primorials and
independently evaluates the reflected cosine formula.  At the gap-four mode,

```text
D_11^wheel(3)=-.11687480550763536,
D_19^wheel(5)=-.06710677778852056.                                    (6.6)
```

On the physical prime shell `[100003,199999]`, the exact finite telescope is

| `q,a` | cumulative before `q` | stage `q` | aggregate after `q` | final | `q*|final|` | `|D_q|/max_(p!=q)|D_p|` |
|---|---:|---:|---:|---:|---:|---:|
| `11,3` | `.000049` | `.116791` | `.008271` | `.109468` | `1.204` | `54.75` |
| `19,5` | `.001096` | `.066904` | `.014274` | `.055155` | `1.048` | `26.34` |
| `43,11` | `.003955` | `.027616` | `.003928` | `.033881` | `1.457` | `11.42` |
| `59,15` | `.000798` | `.019617` | `.003827` | `.018785` | `1.108` | `8.51` |
| `151,38` | `.008129` | `.011117` | `.003331` | `.006895` | `1.041` | `2.72` |

Every displayed `q`-stage is negative-real up to a small boundary imaginary
part.  For `q=11,19`, the finite values differ from (6.6) by less than
`3e-4`.  The uniformly resonant stage is the largest individual stage, while
the final answer remains on the `1/q` scale through substantial cancellation
with the other stages.  Only the post-`q` stages are pointwise nonresonant;
the pre-`q` aggregate is a localized boundary term whose complete-period
mean is zero.

For comparison, deleting residue zero from the otherwise complete circular
`q`-wheel has exact normalized coefficient

```text
[-1+cos(2 pi a/q)]/q.                                                  (6.7)
```

At `q=3 mod 4`, `a=(q+1)/4`, its magnitude is

```text
[1+sin(pi/(2q))]/q,                                                    (6.8)
```

which supplies the finite-`q` correction to the informal `1/q` benchmark.

Equations (6.3)--(6.6) are exact finite/circular identities.  The assertion
that their localized boundary and post-`q` tail are uniformly `O(1/q)` on
growing actual-prime blocks remains conjectural.

---

## 7. Common-height selector

For optional height `t`, the laboratory partitions the shell at the
curvature scale

```text
H=.5 Y/sqrt(t),                                                        (7.1)
```

selects the prime modulus and nonzero numerator minimizing

```text
q H |t/(2 pi x_I)-a/q|,                                               (7.2)
```

and compares the aligned rational edge coefficient with the true
`t log x` coefficient block by block.  The canonical scan gives

| `t` | blocks | block length | fraction satisfying the rational-cell inequality | normalized aggregate difference |
|---:|---:|---:|---:|---:|
| `10^5` | 633 | `157.978` | `.4060` | `.001360` |
| `10^6` | 2000 | `50` | `.7770` | `.000425` |

The modulus range was only `11<=q<=151`, so the failed-cell fraction is not a
failure of Dirichlet approximation.  This module verifies selector geometry
and phase linearization; it supplies no supremum estimate in `t`.

---

## 8. New continuation target

On a frozen constant-amplitude physical block, (6.3) gives the exact
three-part decomposition

```text
T_prime(q,a)=C_(<q)(q,a)+D_q(q,a)+R_(>q)(q,a),                         (8.1)
```

where `C_(<q)` is the cumulative pre-`q` rough-wheel mode, `D_q` is the unique
stage resonant at every deleted center, and `R_(>q)` is the sum of genuinely
nonresonant later stages.
Since the live denominator satisfies `q>=Y^.1537` while the carrier only
needs saving `Y^-.0181`, a uniform

```text
D_q << m_I q^(-1+o(1))                                                 (8.2)
```

would be far stronger than needed.  The genuinely new theorem to seek is

```text
|C_(<q)|+|R_(>q)| << m_I Y^(-kappa-eta),                              (8.3)
```

or a direct common-height aggregate version, together with the transfer from
the physical frozen block to the logarithmic tapered block.

This target has three advantages over the old ordinary-Vaughan transfer:

1. it preserves the exact successor geometry through the deletion charges;
2. it isolates `p=q` as the only **uniformly** resonant SPF stage and shows
   that its natural size is harmless;
3. every `p>q` deleted center carries a genuinely oscillating rational phase.

The pre-`q` term still contains some phase-one deleted centers and must be
controlled as a localized rough-wheel prefix; complete-period cancellation
does not supply that estimate on a physical shell.

Its unresolved liabilities are equally explicit:

1. neighboring charges in (6.2) depend on the evolving sieve history;
2. triangle-summing the later stages loses all cancellation;
3. complete primorial periods are unavailable at growing `q`;
4. the current circular formula is physical and constant-amplitude, while the
   route needs localized logarithmic weights and a common-height selector.

The laboratory therefore changes the research frontier but does not close
it.  The next fail-fast test should attack (8.3) by dyadic SPF-stage energy:
measure and then seek an inequality for

```text
sum_(P<p<=2P)|D_p(q,a)|^2                                             (8.4)
```

with the resonant stage `p=q` removed.  If (8.4) cannot beat its raw `L2`
scale after exploiting the center phases, this new route fails cleanly.  If
it can, the exact telescope provides a path around the previously fatal
trapezoid-to-one-prime transfer pole.
