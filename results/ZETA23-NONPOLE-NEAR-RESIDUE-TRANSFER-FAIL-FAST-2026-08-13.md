# Nonpole near-residue transfer: fail-fast audit

**Date:** 2026-08-13

## Verdict

For the legal wider-strip calibration

```text
kappa=.017522268449743408...,
theta=.1588,                 beta=.1598,
```

the inequality `beta>theta` removes every **exact** retained one-gap
recurrence.  It does not make the remaining edge calculus uniformly
conditioned.  Residue-one near recurrences survive, including ones attached
to a fixed physical gap.

On the odd lattice, take an odd prime `q=3 (mod 4)` and

```text
g=4,             a=(q+1)/4,             z=e(a/q).
```

Then `q>g`, `(a,q)=1`, and `ag=1 (mod q)`, so there is no pole.  Nevertheless
the exact trapezoid-to-odd-block multiplier has size

```text
|m_4^(2)(z)|=4 cos(pi/(2q)) cot(pi/q)
             =(4/pi+o(1))q.                         (0.1)
```

The standard global Vaughan bound at `q=Y^(b+o(1))` supplies saving `b/2`
in this range.  At the bottom shell it can afford transfer loss

```text
beta/2-kappa=.06237773155025659...,
```

whereas (0.1) costs `beta=.1598`; the exponent overrun is

```text
beta-(beta/2-kappa)
 =beta/2+kappa=.097422268449743408....                (0.2)
```

The renewal representation avoids division by the small geometric block,
but then the `g=4` sector is the actual cousin-prime exponential sum.  For
primes above `3`, `p,p+4` prime automatically means that they are consecutive.
Thus this is an **actual-prime coefficient reduction**, not a countermodel;
it is a two-prime correlation rather than an ordinary one-prime Vaughan sum.

Consequently the lower-alpha reoptimization closes the literal one-gap pole,
but it does **not** revive a black-box transfer to ordinary prime sums.  This
is a definitive no-go only for coefficient-blind frozen-rational
scalar/block transfers and ordinary Vaughan input.  It is not a no-go theorem
for an actual-prime-only transfer that exploits the sparsity or possible
eventual absence of gap four, for cancellation in the actual cousin-prime
sector, for the full consecutive-gap sum, or for a common-height argument
using more structure.

No zero-free strip is claimed.

---

## 1. Exact nonpole multiplier

This section is exact for the frozen **physical additive** edge after its
common `1/Y` normalization has been removed; restoring that normalization
does not change the condition number.  Passing from the unfrozen `t log x`
edge to this physical edge is the separate curvature/rational-cell
approximation already present in the route.  For fixed `g=4` its Taylor error
is power-smaller than the target throughout the present aperture.  Thus
(1.1) is not being advertised as an exact identity for the unfrozen
logarithmic phase.

Let `s|g` and sum the lattice points of spacing `s` on one physical edge:

```text
G_(p,g)^(s)(z)=sum_(0<=j<g/s) z^(p+s*j)
              =z^p(1-z^g)/(1-z^s),

T_(p,g)(z)=g z^p(1+z^g)/2.
```

If `z^g!=1`, exact division gives

```text
T_(p,g)=m_g^(s)(z)G_(p,g)^(s)(z),

m_g^(s)(z)=g(1-z^s)(1+z^g)/[2(1-z^g)].              (1.1)
```

For `z=e(a/q)` this has magnitude

```text
|m_g^(s)(z)|
 =g |sin(pi*a*s/q)| |cot(pi*a*g/q)|.                (1.2)
```

When `q` is prime and `g<q`, the least nonzero residue of `ag` has magnitude
at least one, so

```text
|m_g^(s)(z)| <=g cot(pi/q).                          (1.3)
```

This upper bound is asymptotically sharp even for fixed `g`.  Put `s=2`,
`g=4`, `q=3 (mod 4)`, and `a=(q+1)/4`.  Then `4a=q+1`, and (1.2) is exactly
(0.1).  Equivalently,

```text
G_(p,4)^(2)=z^p(1+z^2)          has size asyp 1/q,
T_(p,4)  =2z^p(1+z^4)          has size asyp 1.
```

The same construction works for every fixed lattice spacing `s`: take
`g=2s`, a prime `q=-1 (mod 2s)`, and `a=(q+1)/(2s)`.  Thus passing from the
integer lattice to any fixed presieved lattice cannot supply uniform
conditioning.  The odd-lattice case already suffices for the actual primes.

---

## 2. Why the low-denominator cover misses it

The near-pole rational is

```text
a/q=1/4+1/(4q).                                      (2.1)
```

At height `t`, write `eta_t=sqrt(t)/Y`.  The marked cell around `1/4` has
radius `eta_t/4`, so (2.1) is outside that cell exactly when

```text
q*eta_t<1.                                           (2.2)
```

At the top aperture of the new calibration,

```text
1/eta_t=Y^(1-A/2),       1-A/2=33/133=.2481203007...,
```

while the live denominators begin at `Y^.1598`.  Hence every fixed exponent

```text
.1598<b<.2481203007...
```

has `q*eta_t=o(1)`.  Farey separation gives the same conclusion for every
other marked denominator: for a distinct reduced `c/q'`,
`|a/q-c/q'|>=1/(q q')`, whereas its marked radius is `eta_t/q'`.  The top
aperture has the largest `eta_t`, so noncapture there implies noncapture at
every lower height in the aperture.  The cover removes residue zero; it
supplies no positive lower bound on a nonzero residue in this range.

More generally, if `ag=kq+r`, then

```text
|a/q-k/g|=|r|/(gq).                                  (2.3)
```

For a fixed gap and a cotangent condition `asymp q/|r|`, Vaughan would need

```text
|r| >=Y^[b-(b/2-kappa)]=Y^(b/2+kappa).               (2.4)
```

At `b=beta`, the required residue exponent is the `.0974222684...` in
(0.2).  Condition (2.2) does not even exclude `|r|=1`.

---

## 3. The exact actual-prime sector after avoiding division

Let `R_h(n)` be the indicator that `n,n+h` are consecutive primes.  The
frozen physical gap sum has the exact renewal expansion

```text
T(z)=1/2 sum_h h(1+z^h) sum_n R_h(n)z^n.             (3.1)
```

For `h=4` and `n>3`, divisibility by `3` forces the midpoint `n+2` to be
composite whenever `n,n+4` are prime.  Therefore

```text
R_4(n)=1_(n prime) 1_(n+4 prime),       n>3.         (3.2)
```

On a constant-amplitude block, its exact contribution is

```text
2(1+z^4) sum_(n,n+4 prime) z^n,                     (3.3)
```

with the physical `1/Y` normalization restored afterward.  Smooth endpoint
amplitudes retain the same exact pair support.  Formula (3.3) is not
`sum Lambda(n)z^n`; replacing (3.2) by a one-prime coefficient discards the
load-bearing successor condition.

An upper-bound sieve gives only logarithmic absolute savings for (3.3), far
larger than `Y^-kappa`.  The closest primary theorem located was Green--Tao,
[*Restriction theory of the Selberg sieve, with applications*](https://www2.math.ethz.ch/EMIS/journals/JTNB/2006-1/article09.pdf),
Theorem 1.1.  Applied to `F(n)=n(n+4)`, it gives sharp `L^p` bounds over the
frequency variable for every fixed `p>2`; it does not give the selected-point
power saving needed here.  The standard Nikolskii conversion from that
`L^p` bound back to a supremum loses the compensating `Y^(1/p)` and returns
only the sieve-size bound.  Likewise, a pointwise majorant for the pair
indicator gives a triangle bound but does not dominate the modulus of its
complex Fourier coefficient by the modulus of the majorant's coefficient.

For comparison, the current primary one-prime result
[*Log-free bounds on exponential sums over primes*](https://arxiv.org/abs/2505.07803)
has the same `q^-1/2` power at an exact rational throughout this modulus
range.  It verifies the `b/2` one-prime input above but contains no
successor-prime coefficient.

No unconditional primary theorem was located that supplies the required
pointwise growing-denominator cancellation in (3.3).  This is a literature
boundary, not an assertion that such a theorem is impossible.

Infinitude of cousin primes is itself unknown.  Accordingly, (3.2) does not
prove that a gap-four contribution occurs on arbitrarily high actual-prime
shells.  It proves the sharper method statement: whenever this permitted
actual-prime sector occurs, avoiding the small divisor exposes a genuine
two-prime coefficient that ordinary one-prime Vaughan estimates do not
control.  A proof that the sector is absent or sufficiently sparse would also
dispose of it and lies outside this no-go.

---

## 4. Even the optimistic gap-size split fails

Suppose, more favorably than the algebra permits, that every gap-conditioned
short part up to `Y^lambda` inherited the ordinary Vaughan saving with only
the scalar loss `Y^lambda`.  Its saving would be at most

```text
b/2-lambda.                                          (4.1)
```

The current positive Gafni--Tao tail branch starts at `lambda=2/15`.  At the
bottom denominator,

```text
beta/2-2/15=-.0534333333...<0.                       (4.2)
```

Thus no cutoff on the proved positive-tail branch can leave the required
positive saving.  The formal balance with
`s(lambda)=(9/13)(lambda-2/15)` occurs at

```text
lambda=.1017590909...<2/15,
```

outside the range where that tail is power-saving.  The actual renewal
coefficient in (3.1) is harder than this optimistic scalarization.

---

## 5. Exact surviving target and scope

The route now needs a direct selected-frequency transition estimate.  For a
smooth shell/block weight `W_(I,h)` supported on `n asyp Y`, one schematic
block-normalized version is

```text
1/Y * |sum_(h<=Y^theta) h(1+e_q(ah))/2
       * sum_(n asyp Y) W_(I,h)(n)R_h(n)e_q(an)|
 <<Y^(-kappa-epsilon),                               (5.1)
```

or a common-height aggregate that proves the same cancellation without
bounding each block separately.  It would be enough to prove (5.1) only for
the near-residue sectors left by (2.3), combined with an acceptably
conditioned estimate for the complement.

The `g=4` calculation proves that a coefficient-blind uniformly conditioned
transfer cannot delete those sectors or convert them to ordinary Vaughan
sums.  It does not assert that cousin primes occur infinitely often, that
they make (5.1) large, that the carrier selects (2.1) at a bad height, or that
actual-prime cancellation fails.  Since increasing the candidate depth only
increases `kappa` and decreases the allowable transfer loss `b/2-kappa`, the
displayed shallow-slice failure is already the most favorable case for this
particular transfer.

Replay the algebra and exponent ledger with

```bash
python3 results/verify_zeta23_nonpole_near_residue_transfer.py
```

The checker also verifies on actual finite prime lists that the `g=4` pair
support equals the consecutive-gap support above `3`.  It is not a numerical
test of the asymptotic cancellation in (5.1).
