# Gap-minor optimized frontier and trapezoid no-go audit

**Date:** 2026-08-13

**Verdict:** the optimized Gafni--Tao tail and half-cell rational excision
leave a very narrow, but genuine, one-gap denominator corridor.  Exact
forward/reverse trapezoidal symmetry does not cancel a literal recurrence;
at recurrence it has maximal modulus.  Prime-gap size moments, the
exceptional large-gap tail, and low-denominator excision therefore do not by
themselves close the corridor.

The countermodels below are deliberately scoped.  One is an integer model
for the exact frozen additive phase but is not a set of primes.  The other is
an exact logarithmic-phase model on positive real nodes but is not integral.
They prove package nonimplication only.  They do **not** rule out cancellation
for the actual primes.

---

## 1. Exact joint exponent frontier

Put

```text
A=50/33,
kappa=.0180303234,
Q=Y^beta.
```

On the certified local branch of the Gafni--Tao zero-density envelope,

```text
s_GT(theta)=1-mu_bound(theta)
           =(45 theta-6)/65
           =(9/13)(theta-2/15).                      (1.1)
```

The binding strict conditions are

```text
s_GT(theta)>kappa,
2-A-2 beta-theta>kappa.                              (1.2)
```

The inverse-image length condition `1-A/2-beta>kappa` is slack.  Hence the
continuous boundary is

```text
theta_0=2/15+(13/9)kappa
       =796885669/5000000000
       =.1593771338,

beta_0 =29/165-(11/9)kappa
       =25363884781/165000000000
       =.153720513824242... .                         (1.3)
```

The infimum corridor width for this argument is

```text
theta_0-beta_0
 =-7/165+(8/3)kappa
 =116667787/20625000000
 =.005656619975757... .                              (1.4)
```

Strictness in (1.2) means the boundary is not attained.  The nearly optimal
interior choice used in the gap-tail gate is

```text
theta=797/5000=.1594,
beta =1537/10000=.1537.                              (1.5)
```

It has width `.0057` and exact margins

```text
s_GT(theta)-kappa
 =1028979/65000000000
 =.000015830446...,

[2-A-2 beta-theta]-kappa
 =2996639/165000000000
 =.000018161448... .                                 (1.6)
```

These margins are theorem-positive but narrow; every `Y^epsilon` loss must
be fixed below them.

---

## 2. Exact trapezoidal recurrence calculation

For a constant amplitude on one logarithmic gap `[v,v+Delta]`, set

```text
m=v+Delta/2,                    z=t Delta/2.
```

The symmetric endpoint rule and the continuum integral are exactly

```text
T_gap =Delta exp(i t m) cos z,
I_gap =Delta exp(i t m) (sin z)/z,

T_gap-I_gap
 =Delta exp(i t m)[cos z-(sin z)/z].                 (2.1)
```

At a literal recurrence `t Delta=2 pi h`,

```text
cos z=(-1)^h,                  (sin z)/z=0.
```

After the midpoint phase is included, both endpoints have the same original
phase and

```text
|T_gap|=|T_gap-I_gap|=Delta.                          (2.2)
```

Thus symmetrization is not a notch filter for the dangerous aliases.  It is
maximal there.  Zeros of `cos z` occur at half-recurrences, where the two
endpoint phases are opposite, not at the literal same-residue recurrence.

Nor does the known second moment make the corridor negligible.  For
`q=Y^rho`, `beta<rho<theta`, Stadlmann gives only

```text
sum_(g>=q) g
 <=q^(-1) sum g^2
 <<Y^(1.23-rho+epsilon),                             (2.3)
```

which is worse than the total shell mass for `rho` near `.156`.  The
Gafni--Tao tail begins at `Y^theta` and supplies no estimate below that
threshold.

---

## 3. Integer frozen-additive countermodel

Fix

```text
beta<rho<theta,
q an even integer with q asyp Y^rho,
(a,q)=1,
M>=3 fixed.
```

Repeat cycles containing

```text
one gap of length Mq;
then small positive even gaps of total length q,
split into asyp (M+1)q/log Y pieces.                 (3.1)
```

The cycle length is `(M+1)q`.  Starting from an odd node makes every node
odd.  On an interval of length comparable to `Y`, this model has

```text
#nodes asyp Y/log Y,
#(nodes in J)<<_M 1+|J|/log Y,
max gap=Mq<Y^theta,
sum g^2<<_M Yq+Y log Y<<Y^1.23.                      (3.2)
```

Its large-gap tail above `Y^theta` is empty.  At the frozen additive phase
`e(a x/q)`, all cycle starts have the same phase.  Each `Mq` gap contains an
integral number of periods, its two endpoint phases agree, its continuum
integral is zero, and its exact trapezoidal contribution is `Mq` with a
common phase.  The large gaps contain fraction `M/(M+1)` of the total
length; all small-gap trapezoidal terms have total absolute mass at most
`1/(M+1)`.  Therefore

```text
normalized modulus >=(M-1)/(M+1)+o(1).               (3.3)
```

This rational is genuinely outside the marked `q'<=Y^beta` arcs.  For every
distinct reduced `a'/q'`, Farey separation gives

```text
|a/q-a'/q'|>=1/(q q')>eta_t/q'                       (3.4)
```

throughout the aperture, because

```text
rho<theta<8/33 <= log_Y(1/eta_t).
```

The model satisfies integer parity, density-shaped upper counts, all the
used gap-size estimates, the optimized tail, the low-`q` excision, and the
exact symmetric additive formula.  It is **not a prime set**, and it does
not model the accumulated global curvature error of `t log x`.

---

## 4. Exact-logarithmic real-node countermodel

There is a complementary global model.  At the top legal height
`t=Y^(50/33)`, place positive real nodes on

```text
u=log(x/Y)=2 pi k/t.                                  (4.1)
```

Choose the integer lattice jumps so that the physical gaps alternate between
prime-density-sized gaps and sparse gaps of size `Y^rho`, in the proportions
of Section 3.  The physical lattice mesh is `asymp Y/t=o(1)`, so these target
gaps can be realized with negligible relative error.  The count, local upper
bound, maximal gap, second moment, and empty `Y^theta` tail from (3.2) are
stable.

Every node in (4.1) has logarithmic phase exactly one.  Hence its positive
Voronoi antenna is exactly its total mass.  The optimized low-`q` cell cover
removes only

```text
O(Q sqrt(t)/Y)+O((t/Y)Q^2 Y^theta/Y)=o(1),            (4.2)
```

so the retained normalized antenna is `1-o(1)`.

This model treats the global logarithmic phase exactly, but its nodes are
not integers and hence not primes.  Sections 3 and 4 intentionally separate
the two missing structures; neither may be advertised as an actual-prime
counterexample.

---

## 5. What the literature does and does not rule out

1. Gafni--Tao,
   [*On the number of exceptional intervals to the prime number theorem in
   short intervals*](https://arxiv.org/abs/2505.24017), proves the
   exceptional-set framework underlying (1.1).  It gives no retained-gap
   phase cancellation.
2. Stadlmann,
   [*On the mean square gap between primes*](https://arxiv.org/abs/2212.10867),
   supplies the second moment in (2.3), which is phase blind.
3. Shiu,
   [*Strings of Congruent Primes*](https://doi.org/10.1112/S0024610799007863),
   rigorously proves arbitrarily long strings of actual consecutive primes
   in one residue class for each fixed modulus.  Shiu's theorem itself gives
   neither the needed weighted mass nor a theorem for `q=Y^rho`; it is not a
   counterexample here.
4. Maynard,
   [*Dense clusters of primes in subsets*](https://arxiv.org/abs/1405.2593),
   gives positive-proportion refinements for fixed string length and fixed
   modulus.  Its quantifiers do not provide a weighted transition theorem
   uniform at `q=Y^rho`.
5. Lemke Oliver--Soundararajan,
   [*Unexpected biases in the distribution of consecutive
   primes*](https://arxiv.org/abs/1603.03720), gives a Hardy--Littlewood-based
   conjectural explanation of strong fixed-modulus transition biases.  It is
   not an unconditional growing-modulus theorem.
6. Kim,
   [*Prime Running Functions*](https://arxiv.org/abs/2006.13355), isolates the
   relevant forward gap-weighted residue marginals.  Their fixed-modulus main
   term is conjectural for `q>=3`, and the paper contains no uniform
   `q=Y^rho` Fourier estimate.

These results do not supply a literature no-go theorem for the actual-prime
route.  Shiu and the bias papers instead warn that same-residue transition
mixing cannot be assumed without proof.

---

## 6. Precise survivor

What remains is a sign-sensitive theorem for the actual primes: control the
weighted same-residue/consecutive-gap transition Fourier mode for growing
denominators in the one-gap corridor

```text
Y^.1537<q<<Y^.1594,                                  (6.1)
```

and, separately, control multi-gap recurrences whose denominators can extend
to the curvature scale `Y/sqrt(t)`.  Any proof must use arithmetic information
absent from both countermodels, such as growing-modulus residue-transition
mixing coupled to the actual logarithmic curvature.

The verified package nonimplication is only

```text
gap sizes/tails + positivity + exact trapezoidal symmetry + low-q excision
  do not imply the required cancellation abstractly.

actual-prime positive gap antenna
  remains open and is not ruled out.                                  (6.2)
```

The exponent ledger is independently checked by

```bash
python3 results/verify_zeta23_high_denominator_gap_tail.py
```

which audits both the chosen rational pair and the continuous boundary.  It
does not reprove the imported analytic theorems.
