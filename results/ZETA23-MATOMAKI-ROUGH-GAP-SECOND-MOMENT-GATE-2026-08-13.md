# Matomaki lower-sieve localization closes the rough-gap square gate

**Date:** 2026-08-13  
**Verdict:** **PROVED, as a corollary of published estimates**

Let

```text
R_z={n in Z: p|n implies p>=z},
```

and let `G_2(X;z)` be the sum of the squares of the consecutive gaps of
`R_z` which meet `[X,2X]`, including the two boundary gaps.  Uniformly for

```text
X^.1537 <= z <= X^.160,
```

one has

```text
G_2(X;z) << X (log X)^2.                              (0.1)
```

The implied constant is uniform on this fixed exponent interval.  Thus the
required estimate

```text
G_2(X;z) <= X^(1+rho+o(1)), rho<b-2 kappa,
```

holds with `rho=0`.  In particular it clears both numerical targets
`.1203190348...` and `.1247554631...`.

The key is to use the lower-sieve part of Matomaki's argument by itself and
to lower its linear-sieve level from `X^(5/9)` to `X^(1/3)`.  The level
`5/9` is needed for the paper's Richert `P_2` subtraction, but it is not
needed to count rough integers.  At level `1/3`, the published bilinear
estimate controls empty intervals all the way through length `X^(2/5)`,
whereas Iwaniec's unconditional Jacobsthal bound says that every `z`-rough
gap has length `O(z^2)<=O(X^.32)`.  Integrating the resulting empty-interval
tail proves (0.1).

This report spells out the parameter substitution in the published proof.
No unproved transfer from a semiprime theorem, no probabilistic rough-number
model, and no unsupported uniformity in a Dirichlet polynomial theorem is
used.

---

## 1. The imported statements

The main source is Kaisa Matomaki,
[*Almost primes in almost all very short intervals*](https://doi.org/10.1112/jlms.12592),
especially Proposition 5.1, Lemma 5.4, and Sections 6.1--6.3.  The
[author's arXiv version](https://arxiv.org/abs/2012.11565) has the same
numbering.

Only the following pieces are imported.

1. **Variance decomposition.**  Proposition 5.1 writes the mean square of a
   divisor-sum error with coefficients supported on `d<=D_0` as

   ```text
   S_1+S_2+S_3+O(H^3 log^3 X).                        (1.1)
   ```

2. **General shifted-correlation estimate.**  Lemma 5.4 is stated for every
   `X>=H>=2`, with no `H<=X^(1/60)` restriction.  For bounded coefficients
   on dyadic ranges `M,N,Q`, its left side is at most

   ```text
   H^(1/2) X^(1/2+epsilon)
   [ (MQ)^2
     +(HMNQ/X+N)
       {MQ(HMNQ/X+N)(Q+N^2)+H(MN)^3Q/X}
   ]^(1/4).                                           (1.2)
   ```

   The later Lemma 5.3 imposes `H<=X^(1/60)` only to turn (1.2), under one
   convenient coarse parameter envelope, into a fixed power saving.  We use
   (1.2) itself.

3. **The lower-weight reductions.**  Section 6.1 proves the quadratic
   coefficient estimate used for `S_1^-`; Section 6.3 proves the divisor
   second moment used for `S_3^-`.  Their proofs depend on the beta-sieve
   level, the fixed ratios of `w,z,D`, and boundedness of the sieve weights,
   not on the numerical identity `D=X^(5/9)` or `z=D^(1/4)`.

4. **Well-factorability.**  In the proof of equation (61), Matomaki invokes
   the standard finite well-factorable decomposition of the upper and lower
   linear-sieve weights: for a chosen factorization of the level, each weight
   is an `O(1)` linear combination of convolutions of bounded factors at the
   two chosen levels.  (The raw Rosser--Iwaniec weight need not itself be one
   convolution.)  The construction is available for every factorization of
   the level.  We choose a different, more balanced factorization below.

For the deterministic end of the argument, use Iwaniec's bound

```text
J(z) << z^2,                                          (1.3)
```

where `J(z)` is the largest gap between integers with no prime factor at
most `z`.  A modern explicit statement and attribution appear in Section
2.3 of Banks--Ford--Tao,
[*Large prime gaps and probabilistic models*](https://doi.org/10.1007/s00222-023-01199-0).
The original sources are Iwaniec,
[*On the error term in the linear sieve*](https://doi.org/10.4064/aa-19-1-1-30)
and
[*On the problem of Jacobsthal*](https://doi.org/10.1515/dema-1978-0121).

---

## 2. A lower minorant for the rough set

Put

```text
z=X^b,                 .1537<=b<=.160,
D=X^d,                 d=1/3,
E=X^e,                 e=1/1000,
L=d+e=1003/3000.
```

As in Matomaki's equations (14)--(16), use a beta sieve of level `E` for
primes below `w=X^delta` and well-factorable linear upper and lower weights
of level `D` for primes in `[w,z)`.  The vector-sieve combination gives
coefficients `alpha_r^-`, supported on

```text
r<=DE=X^L,                                             (2.1)
```

such that pointwise

```text
1_((n,P(z))=1) >= sum_(r|n) alpha_r^-.                (2.2)
```

Choose `delta` sufficiently small in terms of a fixed
`epsilon_0<f(25/12)/4`.  The beta fundamental lemma and the ordinary lower
linear sieve then give

```text
A_z:=sum_r alpha_r^-/r
    >= (f(d/b)-epsilon_0) V(z).                       (2.3)
```

Here `f` is the dimension-one lower-sieve function.  At the worst endpoint,

```text
d/b >= (1/3)/(.160)=25/12>2,
f(25/12)=.1368593845...>0.                            (2.4)
```

Consequently, uniformly in the target band,

```text
A_z >> 1/log X.                                       (2.5)
```

This is exactly where the rough problem differs from the Richert `P_2`
problem.  The latter subtracts an upper-sieve prime-factor integral and its
main margin becomes negative near `b=.1541848`.  The rough minorant has no
such subtraction; its only parity threshold is `d/b>2`.

For an interval ending at `x`, define

```text
E_z(x;H)=sum_(r<=X^L) alpha_r^-
          ( #{x-H<rm<=x} - H/r ).                    (2.6)
```

Then (2.2) gives

```text
#{n in (x-H,x] intersect R_z} >= H A_z+E_z(x;H).      (2.7)
```

---

## 3. The rebalanced Lemma 5.4 calculation

Decompose each level-`D` linear weight into the standard `O(1)` collection of
factorable pieces at

```text
R=X^(2L/3),
S=D/R=X^(d-2L/3).                                    (3.1)
```

Group the beta-sieve factor, of size at most `E`, with the `S` factor.  After
dyadic subdivision, exactly as in Matomaki's reduction of (61), Lemma 5.4
has parameters bounded by

```text
M <= X^(2L/3),
N <= X^(L/3),
Q <= X^L.                                             (3.2)
```

Indeed

```text
d-2L/3+e=L/3.                                        (3.3)
```

Divisor-bounded convolution multiplicities cost `X^epsilon`, already
allowed in Lemma 5.4.

Let the physical interval length satisfy `H<=X^eta`.  If

```text
eta < eta_*:=1-5L/3=797/1800=.442777777... ,          (3.4)
```

then the monomials in (1.2) have the following exact exponent ledger:

```text
HMNQ/X <= X^(L/3),
Q+N^2  <= X^L,
MQ(HMNQ/X+N)(Q+N^2) <= X^(3L),
H(MN)^3Q/X          <= X^(7L/3),
(MQ)^2               <= X^(10L/3).                   (3.5)
```

Thus the full fourth-power bracket is `O(X^(10L/3+epsilon))`, and the
shifted-correlation sum is

```text
<< X^(1/2+eta/2+5L/6+epsilon)
 = X^(1-(eta_*-eta)/2+epsilon).                       (3.6)
```

Choose the comfortable value

```text
eta=2/5.                                              (3.7)
```

The power saving in (3.6) is then exactly

```text
(eta_*-2/5)/2=77/3600=.021388888... .                 (3.8)
```

The `(H-|k|)` factor in `S_2` costs one factor `H`; the saving (3.8) absorbs
all logarithmic subdivisions and yields

```text
S_2^- << XH/log X.                                    (3.9)
```

The proofs of Matomaki's equations (49) and (69) give, with the new fixed
levels,

```text
S_1^-+S_3^- << XH/log X.                              (3.10)
```

Finally, the error in Proposition 5.1 is acceptable because

```text
H^3 log^3 X << XH/log X   for H<=X^(2/5).             (3.11)
```

Combining (1.1) and (3.9)--(3.11) proves the derived mean-square theorem

```text
integral |E_z(x;H)|^2 dx << XH/log X                 (3.12)
```

over any fixed multiplicative enlargement of `[X,2X]`, uniformly for

```text
2 log X <= H <= X^(2/5).                              (3.13)
```

The smooth cutoff in Proposition 5.1 only enlarges the shell by an absolute
factor.

Equation (3.12) answers the range question sharply enough for the target:
the printed theorem's `h<=X^.01` is not essential for the lower rough sieve.
Even retaining `D=X^(5/9)` and rebalancing the factors raises the raw range
to `eta<391/5400=.072407...`.  Lowering `D` to the level actually needed by
the rough minorant raises it to (3.4).

---

## 4. Empty intervals and the exact gap integral

If `(x-H,x]` contains no `z`-rough integer, (2.5) and (2.7) imply

```text
|E_z(x;H)| >> H/log X.
```

Chebyshev applied to (3.12) therefore gives

```text
meas{x: (x-H,x] intersect R_z is empty}
 << X log X/H                                         (4.1)
```

throughout (3.13).  In Matomaki's original notation `H=h log X`, this is
the exceptional-set estimate `O(X/h)`.

Let `g` run over the consecutive `z`-rough gaps meeting `[X,2X]`, and put

```text
T(H)=sum_g (g-H)_+.
```

For each listed gap, the starting points whose interval of length `H` lies
inside that gap have measure `(g-H)_+`; these starting-point sets are
disjoint.  They lie in a fixed enlargement of the original shell.  Thus
`T(H)` is bounded by the empty-start measure on that enlargement, and (4.1)
gives

```text
T(H) << X log X/H.                                    (4.2)
```

The layer-cake identity is exact:

```text
sum_g g^2=2 integral_0^infinity T(H) dH.              (4.3)
```

Iwaniec's Jacobsthal theorem gives

```text
max g << z^2 <= X^(8/25)=X^.32.                       (4.4)
```

This is strictly below the `X^(2/5)` ceiling in (3.13), with exponent
margin `2/25=.08`.  For `H<2 log X`, use `T(H)<<X`; for the remaining range
use (4.2); above the right side of (4.4), `T(H)=0`.  Therefore

```text
sum_g g^2
 << X log X + X log X integral_(2 log X)^(O(z^2)) dH/H
 << X (log X)^2,                                     (4.5)
```

which is (0.1).

The two boundary gaps add `O(J(z)^2)` if treated separately.  More cleanly,
include them in the empty-start measure on a fixed enlarged shell, as done
above; then (4.3) already includes them.  Since `J(z)=o(X)`, only `O(1)`
fixed shells are required.

---

## 5. Why the balanced-semiprime detour is unnecessary

A subset

```text
{pr: p in [z,cz], r prime, pr asymp X}
```

has density of order `1/log^2 X` and is contained in `R_z`.  Adding points
can only decrease the sum of squared consecutive gaps, so a sufficiently
strong Selberg integral for that subset would also prove the gate.

The published almost-prime results located do not state the required
uniform polynomial-factor theorem for `p asymp X^.16`: the factor ranges in
Matomaki--Teravainen's later almost-prime theorem are polylogarithmic, and
Matomaki's 2020/22 `P_2` theorem uses a weighted aggregate rather than this
fixed balanced slice.  Proving a new semiprime Selberg integral is therefore
an unnecessary strengthening.  The lower rough minorant is denser, has a
positive main term at level `X^(1/3)`, and is already handled by the
published shifted-correlation lemma.

Likewise, Gorodetsky's rough-number variance theorem has hypotheses which do
not cover the simultaneous polynomial regime `z=X^.16`, `H=X^.12`.  That is
not a no-go theorem for (0.1); the proof above uses well-factorable
lower-sieve coefficients and Kloosterman-fraction estimates instead of the
rough-number asymptotic in that paper.

---

## 6. Scope and remaining proof obligations

```text
ordinary q-rough lower main term at b<=.160:          PROVED
published h<=X^.01 ceiling essential for E^-:         NO
E^- variance through physical H<=X^(2/5):             PROVED BY PARAMETER SUBSTITUTION
empty-interval exceptional measure O(X log X/H):      PROVED
all rough gaps lie inside that H range:                PROVED (Iwaniec J(z)<<z^2)
G_2(X;z)<<X log^2 X:                                  PROVED
balanced-semiprime Selberg integral:                   NOT NEEDED / NOT IMPORTED
full localized prime Fourier mode:                     NOT CLAIMED
zero-free strip by itself:                             NOT CLAIMED HERE
```

This closes the unsigned local `q`-stage moment gate.  As the hostile
toolchain audit already notes, a gap square controls the simultaneous
stage-`q` deletion charge; it does not by itself control the pre-`q` rough
mode or the sum of all later SPF stages.

---

## 7. Reproducibility

The exact rational parameter ledger is

```text
python3 results/verify_zeta23_matomaki_rough_gap_gate.py
```

Expected final line:

```text
consequence: G_2(X;z) << X (log X)^2
```

The checker verifies the lower-sieve threshold, the well-factorable split,
every dominant exponent in Lemma 5.4, the correlation saving, and the
Jacobsthal coverage margin.  The analytic estimates themselves are the
published results cited in Section 1.
