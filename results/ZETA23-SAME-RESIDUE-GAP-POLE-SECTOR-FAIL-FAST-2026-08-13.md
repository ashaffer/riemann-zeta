# Same-residue consecutive-gap pole sector: fail-fast audit

**Date:** 2026-08-13

## Verdict

The exact one-gap pole sector can be isolated without approximation.  For a
retained consecutive-prime gap `g_j=p_(j+1)-p_j`, the rational endpoint phases
coincide precisely when

```text
q | g_j.
```

At `q=Y^(b+o(1))`, the strongest unconditional **uniform positive-mass**
bound found in this audit is

```text
M_q^pole << Y^(-c_GT(b)+epsilon),
c_GT(b)=(45b-6)/65=(9/13)(b-2/15).                   (0.1)
```

This is a direct consequence of the Gafni--Tao exceptional-interval tail:
`q|g_j` forces `g_j>=q`.  At the bottom of the surviving shell,

```text
beta=1537/10000=.1537,
c_GT(beta)=141/10000=.0141,
kappa=.0180303234,
kappa-c_GT(beta)=.0039303234.                         (0.2)
```

Thus (0.1) misses the required exponent by exactly `.0039303234`.  It closes
only for

```text
b>b_*=(65*kappa+6)/45=.1593771338,                    (0.3)
```

which leaves all but the final `.0000228662` of the chosen corridor
`.1537<b<=.1594` unresolved.

Divisor sparsity gives a sharp almost-all-moduli statement:

```text
sum_(q asyp Y^b) M_q^pole <<Y^(-c_GT(b)+o(1)),

#{q asyp Y^b: M_q^pole>Y^(-kappa)}
  <<Y^(kappa-c_GT(b)+o(1)).                           (0.4)
```

At the bottom, at most `Y^(.0039303234+o(1))` moduli can be bad.  This does
not imply a pointwise estimate for the modulus selected by the phase.  A
deterministic tail allocation can concentrate all its mass on one modulus,
or can saturate the exceptional-modulus count in (0.4).

Dimension-two Brun/Selberg upper-bound sieve, Bombieri--Vinogradov or an AP
large sieve, and the fact that all blocks arise from one height do not supply
the missing power.  The exact obstruction is a nonprincipal **consecutive
transition** correlation, not an ordinary prime-in-progressions discrepancy.

This is a definitive failure of the proposed *positive-mass* proof from the
currently available inputs.  It is not a no-go theorem for signed cancellation
among the actual primes, and it is not an actual-prime counterexample.  The
precise signed theorem which would continue the route is stated in Section 8.

No zero-free strip is claimed here.

---

## 1. Exact total and signed pole masses

Work in a fixed multiplicative shell and write

```text
v_j=log(p_j/Y),
Delta_j=log(p_(j+1)/p_j),
g_j=p_(j+1)-p_j,
e_q(x)=exp(2*pi*i*x/q).
```

The tent amplitude used by the route is nonnegative.  Put

```text
w_j=(Delta_j/2)[phi(v_j)+phi(v_(j+1))]>=0.            (1.1)
```

Away from the two shell endpoints,

```text
w_j <<_phi g_j/Y,             sum_j w_j=O_phi(1).     (1.2)
```

The retained gap cutoff is

```text
G=Y^theta,                    theta=797/5000=.1594.   (1.3)
```

For a reduced rational `r/q`, define

```text
M_q^pole =sum_(g_j<=G, q|g_j) w_j,

S_q^pole(r)=sum_(g_j<=G, q|g_j) w_j e_q(r p_j).       (1.4)
```

These are respectively the normalized positive mass and its signed additive
Fourier mode.  Indeed, the exact symmetrized edge term is

```text
(Delta_j/2)[phi(v_j)e_q(rp_j)
             +phi(v_(j+1))e_q(rp_(j+1))].            (1.5)
```

If `q|g_j`, then the two exponentials in (1.5) are equal, and (1.5) is
exactly `w_j e_q(rp_j)`.  Hence

```text
|S_q^pole(r)|<=M_q^pole.                              (1.6)
```

There is no cosine cancellation inside one such edge.  Endpoint clipping
only changes the two boundary terms and is harmless for the exponent audit.

The definitions in (1.4) isolate the frozen rational carrier.  Passing back
to the exact logarithmic phase still requires the already-audited curvature
and rational-cell bookkeeping; this report does not silently identify the
two.

---

## 2. Strongest uniform bound: the Gafni--Tao tail

The audited local part of the Gafni--Tao envelope gives, for fixed
`2/15<=gamma<=theta`,

```text
sum_(g_j>=Y^gamma) g_j/Y
 <<Y^(-c_GT(gamma)+epsilon),

c_GT(gamma)=(45gamma-6)/65.                           (2.1)
```

Strictly, the gap-tail reduction from their exceptional-interval theorem
has a fixed threshold constant `C_gamma Y^gamma`.  This does not change
(2.1) in exponent notation.  To control a threshold `q asyp Y^b`, first use
`gamma=b-delta` with fixed arbitrarily small `delta>0`; then
`q>=C_gamma Y^gamma` for large `Y`, and the loss
`c_GT(b)-c_GT(gamma)=(9/13)delta` is absorbed by `epsilon`.  Thus every use
of (2.1) below has the displayed `+epsilon` and is uniform on a fixed dyadic
denominator shell.  No threshold constant is silently set equal to one.

Let `q asyp Y^b`, with `beta<=b<=theta`.  Since a nonzero prime gap
divisible by `q` is at least `q`, (1.2) and (2.1) imply

```text
M_q^pole
 <<sum_(g_j>=q) g_j/Y
 <<Y^(-c_GT(b)+epsilon).                              (2.2)
```

Constants such as `g_j>=2q` when parity forces an even quotient do not
alter the exponent.  Substitution gives

```text
c_GT(beta)
 =(45*(1537/10000)-6)/65
 =141/10000=.0141,                                   (2.3)

c_GT(theta)=1173/65000=.018046153846... .             (2.4)
```

Solving `c_GT(b)=kappa` gives (0.3).  Because the strip target requires a
strict exponent `c>kappa`, the endpoint `b=b_*` is not itself enough.

The older mean-square gap estimate gives only

```text
sum_(g_j>=q)g_j/Y
 <=(qY)^(-1)sum_j g_j^2
 <<Y^(.23-b+epsilon),                                 (2.5)
```

which is power-growing throughout this shell.  Thus (2.2), not the second
moment, is the strongest available uniform unsigned estimate among the
audited inputs.

---

## 3. Divisor sparsity: strong average, no selected-modulus theorem

For `Q=Y^(b+o(1))`, sum (1.4) over `Q<q<=2Q`.  Every retained gap is counted
at most `tau(g_j)=Y^o(1)` times, and only gaps `g_j>=Q` occur.  Therefore

```text
sum_(Q<q<=2Q) M_q^pole
 <=sum_(g_j>=Q)w_j tau(g_j)
 <<Y^(-c_GT(b)+o(1)).                                 (3.1)
```

Markov gives (0.4).  At `b=beta`, the bad-modulus exponent is exactly

```text
kappa-c_GT(beta)=.0039303234.                         (3.2)
```

This says that the bad moduli form a tiny proportion
`Y^(-.1497696766+o(1))` of the shell.  It does **not** say that there are no
bad moduli.

The exponent in (3.1) cannot be converted into a uniform exponent by a
deterministic argument.  Abstractly, choose `E=Y^(kappa-c_GT(b))` distinct
prime moduli `q_l asyp Y^b`, and assign positive gap mass `Y^-kappa` to
even gaps equal to `2q_l`.  Then

```text
sum_l Y^-kappa=Y^-c_GT(b),                            (3.3)
```

while all `E` moduli are bad at the target threshold.  The required number
of length-`Y^b` gaps is

```text
Y^(1-b-c_GT(b)+o(1));                                 (3.4)
```

their total physical length is only

```text
Y^(1-c_GT(b)+o(1))=o(Y).                              (3.5)
```

At the bottom of the shell, the gap count exponent in (3.4) is `.8322`.
The same allocation has square- and third-gap exponents

```text
1+b-c_GT(b)=1.1396,
1+2b-c_GT(b)=1.2933,                                  (3.6)
```

both below the currently used `1.23` and `1.300753846...` budgets.
Equations (3.3)--(3.6) are a scoped ledger countermodel, not a construction
from primes.

If a height selects a possibly different denominator on each curvature
block, divisor sparsity gives only

```text
M_selected^pole(t)
 <=sum_(g_j>=Y^beta) w_j tau(g_j)
 <<Y^(-.0141+o(1)).                                   (3.7)
```

There is no legitimate division by the number of available denominators:
the selected map can land entirely in the exceptional set of (0.4).

---

## 4. Brun/Selberg prime-pair upper bounds are power-vacuous here

Dropping consecutiveness, a standard dimension-two upper-bound sieve gives,
uniformly for even `h<=G`,

```text
#{p asyp Y: p and p+h are prime}
 << S(h)Y/(log Y)^2,                                  (4.1)
```

where `S(h)` is the prime-pair singular series and
`S(h)<<Y^o(1)` uniformly in this range.  Hence, with `K=G/q`,

```text
M_q^pole
 <<(q/(log Y)^2) sum_(m<=K)m S(mq)
 <<Y^(2theta-b+o(1))/(log Y)^2.                       (4.2)
```

At the bottom endpoint,

```text
2theta-beta=.1651>0.                                  (4.3)
```

Even at `b=theta`, (4.2) has exponent `theta>0`.  After taking the trivial
cap `M_q^pole=O(1)`, (4.2) supplies no power saving at all and is much weaker
than (2.2).

Consecutiveness means that every intermediate integer fails to be prime.
An upper-bound pair sieve cannot turn those many non-primality conditions
into the heuristic factor `exp(-h/log Y)`.  Obtaining that factor uniformly
at `h=Y^.1537` would be a major new large-gap distribution theorem, not a
routine refinement of (4.1).

---

## 5. Why AP large sieves estimate the wrong object

All shell primes are units modulo `q`.  Character orthogonality gives the
exact transition identity

```text
1_(q|g_j)
 =1/phi(q) sum_(chi mod q)
    chi(p_(j+1)) chibar(p_j).                         (5.1)
```

Consequently

```text
M_q^pole
 =1/phi(q) sum_chi sum_j
   w_j chi(p_(j+1)) chibar(p_j),                      (5.2)

S_q^pole(r)
 =1/phi(q) sum_chi sum_j
   w_j e_q(rp_j)chi(p_(j+1))chibar(p_j).              (5.3)
```

The principal term in (5.2) is `O(1/phi(q))`, hence
`Y^(-b+o(1))`, safely below `Y^-kappa`.  The obstruction is the aggregate of
the nonprincipal consecutive-transition correlations.

Bombieri--Vinogradov, Barban--Davenport--Halberstam, and the ordinary
additive or multiplicative large sieve control one-point prime marginals.
They do not control (5.2) or (5.3).  This failure is algebraic, not merely a
loss in a known exponent.  A transition matrix can have perfectly uniform
row and column marginals while its diagonal mass is arbitrary.

For an exact finite witness, take a finite residue state space, choose a set
`A` on which `e_q(ra)` lies in an arc of angular radius `pi/3`, and choose a
permutation which fixes every state in `A` and deranges its complement.  Its
permutation transition matrix has exactly uniform starting and ending
marginals, but its signed diagonal mass has modulus at least

```text
(1/2)|A|/phi(q).                                      (5.4)
```

Mixing this matrix with a fixed-point-free permutation realizes any smaller
diagonal mass while retaining exact marginal uniformity.  Thus even perfect
endpoint AP equidistribution does not imply a power bound for the pole
sector.  This is a finite transition-model nonimplication; it is not a model
of the actual prime sequence.

Applying a character large sieve directly to (5.3) would require a theorem
for the ratios `p_(j+1)/p_j mod q` with consecutive-gap weights.  That is
already the missing transition theorem in different notation.  Treating
`chi(p_(j+1))` as a fixed coefficient in a standard prime-character sum is
invalid because it varies with both `chi` and the successor map.

---

## 6. Common-height incidence supplies no extra power

For one height `t`, let `(r_I,q_I)` be the rational selected on curvature
block `I`.  The exact pole submass is supported on

```text
q_I | g_j,                 q_I>Y^beta.                (6.1)
```

Equation (3.7) is the strongest conclusion obtained by forgetting the
phases.  The fact that all `q_I` arise from one `t` does not turn the
almost-all-modulus statement (0.4) into a uniform statement: a deterministic
selector may hit an exceptional modulus, and one exceptional height is
enough to defeat the desired supremum.

The previously verified common-height incidence audit shows quantitatively
that the rational cells have positive height width and that blockwise large
sieve/Markov bounds permit one selected bad fraction on every block.  Its
integer model is **not** an exact `q|g` model, so it is used here only for
that incidence calculation, not advertised as a counterexample to (6.1).

A genuine improvement from common height would have to prove a new
actual-prime incidence estimate coupling all three conditions

```text
q|g_j,
|t/(2*pi*x_I)-r/q|<=1/(qH_I),
and the phase e_q(rp_j),                              (6.2)
```

uniformly in `t`.  No primary source located contains such a result.

---

## 7. Primary-literature boundary

1. Gafni--Tao,
   [*On the number of exceptional intervals to the prime number theorem in
   short intervals*](https://arxiv.org/abs/2505.24017), gives (2.1).  It is
   an unsigned exceptional-interval theorem and contains no divisor- or
   phase-conditioned transition estimate.
2. Montgomery--Vaughan,
   [*The large sieve*](https://doi.org/10.1112/S0025579300004708), and
   Bombieri,
   [*On the large sieve*](https://doi.org/10.1112/S0025579300005313), average
   ordinary linear residue/Fourier statistics.  They do not estimate the
   successor ratio in (5.2).
3. Maynard's Selberg-sieve framework,
   [*Small gaps between primes*](https://doi.org/10.4007/annals.2015.181.1.7),
   contains the relevant upper-bound-sieve technology.  At the present
   scales its dimension-two consequence is only (4.2).
4. Shiu,
   [*Strings of Congruent Primes*](https://doi.org/10.1112/S0024610799007863),
   proves arbitrarily long same-class strings for each fixed modulus.
   Freiberg,
   [*Strings of congruent primes in short intervals*](https://arxiv.org/abs/1005.4703),
   fixes `a,q,epsilon` before taking the prime height to infinity.  Maynard,
   [*Dense clusters of primes in subsets*](https://arxiv.org/abs/1405.2593),
   Theorem 3.3, is stronger: it is uniform for
   `q<=(log Y)^(1-epsilon)` and for a stated growing range of the string
   length.  This is still far below `q=Y^b`.  All three are occurrence
   results, not upper bounds for the gap-weighted mass.
5. Lau,
   [*Residue Class Patterns of Consecutive Primes*](https://arxiv.org/abs/2409.12819),
   proves that many residue patterns are attainable infinitely often when
   the pattern parameters and modulus are fixed before the prime height
   tends to infinity.  It is an existence theorem, not a theorem uniform for
   `q=Y^b` and not transition mixing; it is therefore neither the needed
   lemma nor a no-go theorem.
6. Lemke Oliver--Soundararajan,
   [*Unexpected biases in the distribution of consecutive primes*](https://arxiv.org/abs/1603.03720),
   explicitly emphasize that one-point equidistribution does not settle
   consecutive residue patterns.  Their distribution formulas are
   Hardy--Littlewood-based conjectures, not unconditional growing-`q`
   estimates.
7. Kim,
   [*Prime Running Functions*](https://arxiv.org/abs/2006.13355), notes that
   even the main term for the one-sided gap-weighted residue statistic is
   conjectural for each fixed modulus `d>=3`.  The symmetric diagonal
   statistic here is different, but no growing-modulus power theorem for it
   was found.

The existence results in items 4--5 do not refute a growing-modulus upper
bound: their modulus is fixed before the prime height tends to infinity.
Conversely, they warn against treating diagonal transition mixing as a
formal consequence of the prime number theorem in progressions.

No literature no-go theorem for the actual-prime signed pole sector was
found.  The only definitive negative statements here are the explicit
method/ledger nonimplications in Sections 3--6.

---

## 8. Exact theorem needed

The common-height selector can use a different denominator on each curvature
block.  A closing statement must therefore retain the block normalization,
not merely bound the full-shell mass for each fixed `q`.  For a block `I`,
put

```text
m_I=sum_(j in I)w_j <<H_I/Y
    (and m_I asyp H_I/Y on interior positive-amplitude blocks),
M_(I,q)^pole=sum_(j in I, q|g_j)w_j.                 (8.0)
```

There are two clean continuation targets.

### 8.1 Strong positive-mass version

For `q=Y^(b+o(1))`, uniformly in the blocks and all dyadic scales
`beta<=b<=b_*`, prove

```text
M_(I,q)^pole
 <<m_I Y^(-c_GT(b)-eta(b)+epsilon),

inf_(beta<=b<=b_*)[c_GT(b)+eta(b)]>kappa.             (8.1)
```

At `b=beta`, this needs an additional exponent strictly larger than
`.0039303234`.  The uniform infimum is essential because the first dyadic
shell has exponent `beta+o(1)`, not one fixed `b>beta`.  Summing (8.1) over
the blocks uses `sum_I m_I=O(1)` and closes the selected positive pole mass.
An equally valid, weaker selector-specific replacement is the direct
common-height estimate

```text
sum_I M_(I,q_I)^pole <<Y^(-kappa-eta)                (8.1a)
```

for every legal selector arising from one height.  A full-shell estimate for
each fixed `q` alone is not sufficient when `q_I` varies with `I`.  Both
(8.1) and (8.1a) are stronger than necessary because they take no signed
cancellation.

### 8.2 Exact signed transition version

For a local block define

```text
T_(I,q,r)=1/phi(q) sum_(chi nonprincipal) sum_(j in I)
  w_j e_q(rp_j)chi(p_(j+1))chibar(p_j).
```

It is enough to prove, with some fixed `eta>0`,

```text
|T_(I,q,r)| <<m_I Y^(-kappa-eta),                    (8.2)
```

uniformly for the phase-selected reduced `(r,q)` and the relevant smooth
physical blocks.  The principal term on `I` is
`O(m_I/phi(q))=O(m_I Y^(-beta+o(1)))`, so summing (8.2) over the blocks
closes the pole sector.  A weaker but still sufficient version directly
bounds the true common-height aggregate of the `T_(I,q_I,r_I)`, including
its block phase factors, by `Y^(-kappa-eta)`.

Equivalently, one may prove a common-height version of (8.2) after inserting
the selector and curvature conditions (6.2).  Ordinary AP equidistribution,
an average over unselected moduli, or a fixed-modulus occurrence theorem is
not a substitute for (8.2).

The fail-fast conclusion is therefore sharp:

```text
current unconditional uniform pole-mass exponent:  .0141;
required exponent:                                  .0180303234;
unproved extra exponent at the bottom:              .0039303234.
```

---

## 9. Reproduction and scope

The rational exponent ledger, average-modulus count, sieve exponent, moment
compatibility, and a finite uniform-marginal/diagonal-transition witness are
checked by

```bash
python3 results/verify_zeta23_same_residue_gap_pole_sector.py
```

The checker verifies algebra and finite linear identities.  It does not
reprove the imported analytic theorems, convert a transition model into
primes, or prove a zero-free strip.
