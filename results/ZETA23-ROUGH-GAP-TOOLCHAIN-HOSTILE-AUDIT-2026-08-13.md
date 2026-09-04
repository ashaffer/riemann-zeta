# Rough-gap toolchain hostile audit

**Date:** 2026-08-13  
**Binary verdict:** **PATCH**

The exact algebra and all executable certificates pass.  Two overstatements
were patched:

1. the raw normalized full-period `q`-stage is bounded by `2/q`; the sharper
   `1/(q-1)` bound is for the multiplicative-principal-subtracted mode;
2. `p=q` is the only stage resonant at **every** deleted center, not the only
   stage containing resonant centers.  If `p<q`, stage `p` can delete a
   multiple of `q` (for example `p=2`, `x=2q`), whose center phase is one.

Neither correction changes a saving exponent.  They do change the logical
description of what remains.

## 1. Audited statements

```text
single-point deletion identity:                         PASS
SPF stage-by-stage telescope:                           PASS
endpoint scope of a finite decomposition:               PATCHED
one-hole q-wheel coefficient:                           PASS
complete pre-q circular-wheel stage formula:            PASS
Bernoulli sparse renewal resolvent and normalization:    PASS
finite-wheel deletion coupling:                         PASS
raw full-period q-stage <=2/q:                           PASS
principal-subtracted full-period mode <=1/(q-1):         PASS
every pre-q stage has zero mode on a common full period: PASS
prefix-coboundary identity:                              PASS
simultaneous positive deletion transport:                PASS
local q-stage reduction to sqrt(N_q G_2):                PASS
Matomaki--Iwaniec z-rough G_2<<Y(log Y)^2:               PASS
selector-stable capped energy at Z=Y^(8/33):              PASS
arbitrary-denominator resonant-group aggregate:           PASS
claim that G_2 alone bounds the final prime mode:         FAIL / NOT MADE
actual-prime laboratory finite identities and replay:    PASS
asymptotic selected-frequency theorem:                   OPEN
zero-free strip:                                         NOT PROVED
```

The finite deletion program retains both interval endpoints.  Its final set
is therefore `{endpoints and interior primes}`; it is literally the prime set
only when both endpoints are prime.  The reports and module documentation now
state this explicitly.

## 2. Exact surviving decomposition

On a frozen physical block `I`, let

```text
S_<q  = integers with no prime factor below q,
S_<=q = integers with no prime factor at most q,
P_I   = retained endpoints and primes in I,
f(n)  = e_q(a n).
```

With `T(S;f)` the symmetrized Voronoi/trapezoid statistic, put

```text
C_<q = T(S_<q;f),
D_q  = T(S_<=q;f)-T(S_<q;f),
R_>q = T(P_I;f)-T(S_<=q;f).
```

Then the finite SPF telescope gives exactly

```text
T(P_I;f)=C_<q+D_q+R_>q.                              (2.1)
```

The simultaneous-deletion identity applies to `D_q`.  If `N_q(Y)` is the
number of deleted `q`-multiples and `G_2(Y;q)` is the adjacent pre-`q`
rough-gap square sum, including the two boundary gaps, then

```text
|D_q| << sqrt(N_q(Y) G_2(Y;q)).                     (2.2)
```

This is order-free and uses only gaps in the one fixed pre-deletion rough
sequence.  It does not use dynamically merged sequential gaps.

For `q=Y^(b+o(1))`, an upper sieve gives

```text
N_q(Y) << Y^(1-b+o(1)).                              (2.3)
```

Thus, if

```text
G_2(Y;q) << Y^(1+rho+o(1)),                          (2.4)
```

the normalized `q`-stage saves `(b-rho)/2`.  To beat a carrier bill `kappa`
with fixed room `eta>0`, the exact exponent condition is

```text
rho < b-2*kappa-2*eta.                               (2.5)
```

At the reoptimized bottom `b=.1598`, the zero-room thresholds are

```text
rho < .124755463100513...  for kappa(.47,.665),
rho < .120319034834116...  for kappa_max at alpha=.5. (2.6)
```

The older `.1537` denominator generation has the stricter corresponding
thresholds `.1186554631...` and `.1142190348...`.

## 3. Post-audit closure of the unsigned q-stage

The proposed moment input is no longer open.  The independently audited
lower-sieve specialization in
[`ZETA23-ROUGH-GAP-LOWER-SIEVE-HOSTILE-AUDIT-2026-08-13.md`](ZETA23-ROUGH-GAP-LOWER-SIEVE-HOSTILE-AUDIT-2026-08-13.md)
proves, uniformly for a fixed exponent band `.1537<=b_0<=.160`,

```text
G_2(Y;z) << Y(log Y)^2,       z=Y^b_0.               (3.1)
```

This uses only Matomaki's pointwise vector lower minorant, the general
Type-II estimate in her Lemma 5.4, and Iwaniec's `J(z)<<z^2` theorem.  In
particular, the exceptional-start estimate is integrated by the exact
empty-start layer-cake identity, so (3.1) holds on every prescribed dyadic
shell rather than only on a favorable subsequence.

For any target prime `q>=z`, the finite telescope may be reordered exactly:

```text
S_<z  --delete q-->  S_<z\{q-multiples}  --delete all remaining composites-->
P_I.
```

Put

```text
C_<z    =T(S_<z;f),
D_(q|z) =T(S_<z\{q-multiples};f)-T(S_<z;f),
R_rest  =T(P_I;f)-T(S_<z\{q-multiples};f).
```

Then

```text
T(P_I;f)=C_<z+D_(q|z)+R_rest.                        (3.2)
```

The same simultaneous-transport argument, now with the `z`-rough gaps,
gives

```text
|D_(q|z)| << sqrt(N_q(Y;z)G_2(Y;z))
          << Y q^(-1/2)(log Y)^O(1).                 (3.3)
```

Here the upper sieve gives `N_q(Y;z)<<Y/(q log z)`; logarithms are harmless.
Once `q` has been deleted, no later deleted center is a multiple of `q`, so
every later center is pointwise nonresonant.  This fact alone supplies no
cancellation for their aggregate.

### 3.1 Selector-stable and composite-denominator upgrade

The broader audit in
[`ZETA23-SELECTOR-STABLE-TRUNCATED-ROUGH-GAP-ENERGY-2026-08-13.md`](ZETA23-SELECTOR-STABLE-TRUNCATED-ROUGH-GAP-ENERGY-2026-08-13.md)
also passes after repairing an initially hidden prime-denominator
assumption.  Put

```text
Z=Y^(8/33),       G=C_w Y^(797/5000),
phi_G(g)=g min(g,G).
```

The fixed `C_w` is the constant from the Gafni--Tao terminal-gap cutoff and
does not change an exponent.

Using `D=Y^(5/9)`, `E=Y^(1/1000)`, and the same fixed balanced split in
Matomaki's raw Lemma 5.4 gives empty-window control through every fixed
`eta<391/5400`.  At one scale this implies

```text
Phi_G(R_Z)=sum_g phi_G(g)
 <<Y^(1+1468/16875+epsilon).                         (3.4)
```

The functional `phi_G` is superadditive.  Hence every family of disjoint
local gap partitions refining `R_Z` has total capped energy at most (3.4),
apart from the audited `O(KG^2)` block-boundary ledger.  This is a
deterministic selector statement; no union over the blockwise denominators
is taken.

For an arbitrary reduced denominator `Y^(799/5000)<=q_I<Y`, including a
composite one, define on the block

```text
B_(q_I)=R_Z union {composite multiples of q_I}.
```

Obtain it by first deleting every composite outside `R_Z` which is not a
`q_I`-multiple.  Then delete all `q_I`-multiples simultaneously, and finally
delete the remaining composites.  This is an exact reordering of the finite
deletion telescope; every target multiple was deliberately retained and has
phase one.  Since `B_(q_I)` contains `R_Z`, its gap partition refines the
single partition controlled by (3.4).

After removing the already-audited Gafni--Tao long terminal prime edges and
the `O(K)` short edges crossing block boundaries, the two surviving prime
endpoints of each edge are permanent barriers.  Thus every intermediate
candidate gap on that edge is at most `G`.  Two Cauchy inequalities and

```text
sum_I N_I <<Y^(1-799/5000)
```

give the selector-uniform aggregate

```text
Y^-1 sum_I |D_(q_I,I)|
 <<Y^(-9829/270000+epsilon),                         (3.5)
```

a saving `.0364037...`.  This proves the exact resonant **q-multiple group**
on all selected short terminal edges.  It neither estimates the candidate
mode before that group nor the nonresonant deletion tail after it.

## 4. What is still sufficient, and what is not

A sufficient remaining theorem package can now be stated edgewise.  On each
selected short terminal edge, write

```text
T_prime=C_(B_q)+D_q+R_(B_q->prime).
```

The aggregate of `D_q` is (3.5).  It therefore remains sufficient to prove

```text
|sum_I [C_(B_(q_I),I)+R_(B_(q_I)->prime,I)]|
                         <<Y^(1-kappa-eta),           (4.1)
```

uniformly for the selected `(q,a)` and blocks, followed by the already
identified physical-to-logarithmic taper and common-height transfer.  Separate
bounds for the two displayed terms are sufficient but not necessary.

The proved rough-gap/capped-energy estimates control only the resonant group.
They do not imply (4.1):

- `C_(B_q)` is a localized additive mode of the entire candidate sequence.  A gap
  square moment alone does not force its residues modulo `q` to mix.
- `R_(B_q->prime)` is the reordered later deletion charge.  Its centers are
  genuinely
  nonresonant because a number divisible by `q` has already disappeared, but
  triangle summation still loses all useful cancellation.

Likewise, complete-period cancellation of every pre-`q` stage proves a mean
identity, not a short-prefix bound when the primorial period is exponentially
larger than the shell.

## 5. Shell quantifier and polarity

Write

```text
r(Y)=-log E_Y/log Y.
```

The commonly stated all-scale lower bound

```text
E_Y>=Y^(-kappa+o(1)) for every sufficiently large Y
```

is equivalent to `limsup r(Y)<=kappa`.  A dual estimate
`E_(Y_j)<=Y_j^(-c+o(1))`, `c>kappa`, on one unbounded subsequence disproves
that **uniform formulation**.

It does not close the prime-null mechanism.  The contradiction construction
against one fixed hypothetical off-line zero can be run along any unbounded
sequence on which the carrier lower bound and the already-uniform transfer
errors hold.  Consequently a different subsequence with
`E_(Y_j)>=Y_j^(-kappa+o(1))` can still promote the route.  To kill the route
without a separate scale-stability theorem, one needs an eventual upper
bound with exponent `c>kappa` for all scale centers (equivalently
`liminf r(Y)>=c`), not merely a small-`E_Y` subsequence.

For one fixed `Y`, the dual antenna is a supremum-in-height statement across
the legal aperture.  The curvature decomposition does **not** logically need
a good estimate on each block separately: a direct common-height signed
aggregate over all selected blocks is sufficient.  It does, however, need
that aggregate for every legal height, or another argument controlling the
full supremum.

An almost-all-in-translation theorem therefore has only the following direct
consequences:

1. for fixed auxiliary parameters it can produce many good block starts and,
   after choosing centers, an unbounded good subsequence;
2. it does not control a prescribed shell or the blocks selected by an
   adversarial height;
3. exceptional sets may depend on height, modulus, and block scale, so a
   fixed-parameter almost-all statement cannot be intersected over the
   polynomial-size height/modulus net without a quantitative union bound;
4. an exceptional proportion of logarithmic size contributes only a
   logarithmic saving under unsigned disposal, not the required fixed power.

Thus existing almost-all translation results can support diagnostics or a
subsequence theorem for one fixed parameter bank.  They do not prove the
uniform common-height antenna, do not by themselves control all three terms
in (2.1), and do not close the dual route.  A power-small exceptional set
strong enough for the full selector net, a direct signed aggregate theorem,
or a scale-stability principle could change this conclusion.

## 6. Reproduction

```text
python3 src/test_prime_gap_sieve_deletion.py
python3 -m pytest -q src/test_finite_wheel_transfer_operator.py
python3 results/verify_zeta23_finite_wheel_transfer_operator.py
python3 -m pytest -q src/test_actual_prime_transition_lab.py
python3 src/verify_actual_prime_transition_lab.py \
  results/ZETA23-ACTUAL-PRIME-TRANSITION-LAB-100K-2026-08-13.json
PYTHONPATH=src python3 -m unittest -v \
  src/test_rough_gap_lower_sieve_frontier.py
python3 results/verify_zeta23_rough_gap_lower_sieve_frontier.py
python3 results/verify_zeta23_matomaki_rough_gap_gate.py
python3 results/verify_zeta23_selector_stable_rough_gap_energy.py
```

All commands passed in this audit.
