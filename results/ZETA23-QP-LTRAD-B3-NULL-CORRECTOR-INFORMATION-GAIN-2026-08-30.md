# QP LTRAD B3: null-corrector information-gain audit

**Date:** 2026-08-30

## Verdict

This audit proves no zero-free strip and does not prove RH.  It does obtain
four decisive corrections to the proposed B3 source-weighted cluster route.

1. The displayed generic constraints in B3 do not imply `(7.3)`.  A single
   close reflected pair has negligible low-source leverage and polynomially
   large high-band `L1` within the stated corrector-energy allowance.  This is
   an abstract/conditional obstruction, not an asymptotic actual-prime
   counterexample: simultaneous occurrence of a long source event, a close
   pair, and a small carrier is not proved.  The missing information-bearing
   premise in the proposed derivation is

   ```text
   h_Y(y)=sup_(t in H_Y) F_y(t) <= epsilon_Y,
   epsilon_Y=Y^(-.0179+o(1)).                         (0.1)
   ```

   The energy estimate quoted in B3 was derived from `(0.1)`; it is not an
   equivalent replacement for `(0.1)`.

2. `Avg_I` is not defined in the B3 statement.  The null-corrector obstruction
   works for either natural choice, the full high band
   `H_Y=[Y^.01,B]` or its terminal half `[B/2,B]`, where
   `B=Y^(50/33)`.

3. The obstruction is not merely a synthetic frequency accident.  There are
   exact ordinary-prime shells containing two disjoint `B^-1`-close reflected
   pairs.  On their two-dimensional antisymmetric space, one scalar source
   normalization always leaves a nonzero exact source-null direction.

4. After `(0.1)` is restored, a one-pair cloud cannot be a separator.  One
   Arb-certified, fixed-`tau` three-pair synthetic control also has transverse
   return at least

   ```text
   0.592871889898960588... .                          (0.2)
   ```

   This does not prune all two- or three-cluster families, especially scalable
   families with `tau=t_0/B -> 0`.  It does show that the corrected search must
   test joint cross-cluster cancellation rather than a free-standing large
   corrector.  The next experiment should be a hostile multicluster
   semi-infinite LP, not the unrestricted B3 difference-of-convex optimization
   originally proposed.

The exact and interval checks are replayed by

```bash
python3 results/verify_zeta23_qp_ltrad_b3_null_corrector.py
```

## 1. The quantifier that was lost

The exact transverse target in the LTRAD synthesis is

```text
s_v=inf_(y:y dot v=-1) h_Y(y) >= epsilon_Y.           (1.1)
```

To prove `(1.1)` by contradiction, one assumes a vector satisfying both

```text
y dot v=-1,                  h_Y(y)<epsilon_Y.        (1.2)
```

For the canonical reflected-pair split `y=y_car+y_corr`, the existing frame
estimate then gives

```text
E_Y(y_corr)^(1/2)
  <<epsilon_Y Y^(8/33+o(1))
   =Y^(.22452424...+o(1)),                            (1.3)
```

and low-band Lipschitz suppression gives

```text
F_corr(t_0)=o(epsilon_Y).                             (1.4)
```

The proposed B3 statement retained `(1.3)--(1.4)` but dropped the hypothesis
`h_Y(y)<epsilon_Y`, and then asked for

```text
c_r H_J(y_car)
 -Avg_I|F_corr|
 -|Avg_I(F_car+F_corr)|
 >=2epsilon_Y.                                       (1.5)
```

That implication is false as a deduction from these generic constraints.  The
next section gives the explicit obstruction.
This does not contradict the original logic leading from `(1.2)` to `(1.3)`;
it shows only that the consequence `(1.3)` cannot replace its premise.

## 2. One-pair null-corrector lemma

Let a reflected pair have positive absolute-log frequencies

```text
u_- = m-delta/2,          u_+ = m+delta/2,
0<z:=B delta<=1.                                      (2.1)
```

Give the two nodes coefficients `(a,-a)` and put

```text
Q=a z.                                                (2.2)
```

Its carrier sum is zero, its scaled Newton difference jet is `2Q`, and its
real cosine polynomial is

```text
F_corr(t)
 =a[cos(u_-t)-cos(u_+t)]
 =Q(t/B)sinc(delta t/2)sin(mt),                       (2.3)
```

up to an irrelevant global sign.  Here `sinc(x)=sin(x)/x`.

### Proposition 2.1 (large high-band mass, small source value)

Suppose `mB>=16`.  On `J=[B/2,B]`,

```text
Avg_J |F_corr|
 >=c_pair |Q|,
c_pair=sin(1/2)(2/pi-1/4)
      =.185355392602362... .                          (2.4)
```

Consequently,

```text
Avg_(H_Y)|F_corr|>=.092677696301181... |Q|.           (2.5)
```

At every low source height `t_0<=Y`,

```text
|F_corr(t_0)|<=|Q|t_0/B.                             (2.6)
```

#### Proof

For `t in J`, one has `t/B>=1/2`, `0<=delta t/2<=1/2`, and hence

```text
(t/B)sinc(delta t/2)>=sin(1/2).                      (2.7)
```

The discrepancy of the mean of `|sin(mt)|` from `2/pi` on an interval of
length `B/2` is at most `4/(mB)`.  Therefore

```text
Avg_J |sin(mt)|>=2/pi-4/(mB)>=2/pi-1/4.              (2.8)
```

Equations `(2.3)`, `(2.7)`, and `(2.8)` prove `(2.4)`.  Since `J` occupies at
least half the length of `H_Y`, `(2.5)` follows.  Finally, `|sinc|<=1` in
`(2.3)` gives `(2.6)`.  QED

At the full B3 energy scale, take

```text
|Q|<=epsilon_Y Y^(8/33+o(1)).                        (2.9)
```

Since `t_0/B<=Y^(-17/33)`, `(2.6)` gives

```text
|F_corr(t_0)|
 <=epsilon_Y Y^(-3/11+o(1))
 =o(epsilon_Y),                                      (2.10)
```

while `(2.5)` permits high-band `L1` of size
`epsilon_Y Y^(8/33+o(1))`.

Exact source-nullity is unnecessary.  If `y_0` lies wholly in the carrier
sector, `y_0 dot v=-1`, and `s=F_corr(t_0)`, then

```text
y=(1+s)y_0+y_corr                                    (2.11)
```

again satisfies `y dot v=-1`, because the antisymmetric pair has coefficient
sum zero and

```text
[(1+s)y_0+y_corr] dot v=-(1+s)+s=-1.                 (2.12)
```

The carrier jet mass changes by only `1+o(epsilon_Y)`.  Thus, for any
bounded or subpower base carrier,

```text
c_r H_J(y_car)-E_corr(y)
 <=c_r Y^o(1)-.0926|Q|,                              (2.13)
```

which violates `(1.5)` for polynomially growing `Q` allowed by `(2.9)`.

An explicit abstract base carrier may be made from one separated singleton
whose source coordinate is nonzero, with its coefficient chosen to give
`y_0 dot v=-1`; it has bounded `H_J`.  This proves:

> Source normalization, conjugate symmetry, low-source suppression, and the
> corrector-energy budget do not by themselves imply B3's displayed margin.

The vector in `(2.11)` normally has large `h_Y(y)`.  Therefore this proposition
does **not** refute the separator-qualified statement `(1.1)--(1.2)`, nor does
it refute an actual-prime asymptotic B3 statement unless the pair, source
event, and controlled carrier are shown to coexist along an unbounded family.

## 3. Genuine ordinary-prime realizations

### 3.1 One source-null actual pair

At

```text
N=3000,       Y=3000.5,       B=Y^(50/33),
p_-=2729,                     p_+=3299,              (3.1)
```

put

```text
u_-=log(Y/p_-),        u_+=log(p_+/Y).                (3.2)
```

Arb certifies

```text
B=185556.084044433194...,
B|u_--u_+|=.602857283614117...<1.                    (3.3)
```

Choose

```text
t_0=2pi*45/(u_-+u_+)
    =1490.600759460433844... .                        (3.4)
```

Then `sqrt(N)<t_0<N`, and the identity

```text
(u_-+u_+)t_0=90pi                                   (3.5)
```

makes `cos(u_-t_0)-cos(u_+t_0)=0` exactly.  The certified version of the
bound in Proposition 2.1 is

```text
Avg_(H_Y)|F_corr|/|a|>.0955507634303859,
Avg_(H_Y)|F_corr|/(2|a|z)>.0792482450054854.          (3.6)
```

Moreover its positive high-band supremum is at least
`.0476617351578145|a|`.  Thus restoring `(0.1)` really does block this
unqualified witness; the source condition alone does not.

### 3.2 An exact two-pair polynomial fixture

There is a useful exact construction.  For an integer `m` and odd `k`, put

```text
Y=m^2+1/2,                   r_k=(k^2+1)/2,
p_k=m^2-km+r_k,              q_k=m^2+km+r_k.          (3.7)
```

Direct multiplication gives

```text
p_k q_k-Y^2=r_k^2-1/4.                               (3.8)
```

For fixed `k` and sufficiently large `m` (in particular `m>k/2`), whenever
`p_k,q_k` are prime they straddle `Y`, lie in the fixed shell, and form a
reflected pair with

```text
B |log(p_kq_k/Y^2)|
  asymp (r_k^2-1/4)Y^(-16/33),                       (3.9)
```

so the pair is much closer than `B^-1` in log frequency for fixed `k` and
large `m`.

For `m=3339`, all four numbers from `k=1,3` are prime:

```text
(p_1,q_1)=(11145583,11152261),
(p_3,q_3)=(11138909,11158943),
Y=11148921.5.                                        (3.10)
```

Their exact product offsets are `3/4` and `99/4`; their certified scaled log
gaps are respectively

```text
.000287224240697831...,
.009478399943027536... .                             (3.11)
```

A second exact fixture occurs at `m=1002924`, `Y=1005856549776.5`:

```text
(1005855546853,1005857552701),
(1005853541009,1005859558553).                       (3.12)
```

The replay script proves primality by deterministic trial division and
checks `(3.8)` over the integers.

The four quadratic polynomials from `k=1,3` are admissible.  The residue
`m=0` is safe modulo `2,3,7`, and `m=1` is safe modulo `5`.  For every prime
`ell>=11`, their degree-eight product has at most eight roots modulo `ell`, so
some residue is safe.  This removes a local congruence obstruction but, of
course, does not prove simultaneous prime values infinitely often.

For `K` reflected pairs, let `d_i` be the pure antisymmetric pair vector and

```text
ell_i=d_i dot v=F_(d_i)(t_0).                        (3.13)
```

The `D q_P` term vanishes because every `d_i` has coefficient sum zero.
The source restriction on the `K`-dimensional pair space is therefore only
one linear functional, so

```text
dim(span{d_i} intersection v^perp)>=K-1.             (3.14)
```

For two pairs, `(ell_2,-ell_1)` is an exact source-null corrector direction
when the two `ell_i` are not both zero; if both vanish, either pair direction
is already source-null.
If their dimensionless center separation is at least `64` and each center is
at least `64/B`, a direct weighted-Gram estimate gives, for half-jet norm
`R_Q=(sum_i |Q_i|^2)^(1/2)` (the full difference-jet norm is `2R_Q`),

```text
Avg_(H_Y)|F_corr|>=.0592001402526152 R_Q.             (3.15)
```

For completeness, put `g_i(t)=(t/B)sin(m_i t)`.  Scaling `J` to
`x in [1/2,1]` and integrating `x^2 cos(kx)` explicitly gives

```text
Avg_J g_i^2>=53/192,
|Avg_J g_1 g_2|<=3/64.                               (3.16)
```

The Gram matrix therefore gives

```text
Avg_J |sum_i Q_i g_i|^2 >=(11/48)R_Q^2.             (3.17)
```

Its supremum is at most `sqrt(2)R_Q`, so
`L1>=L2^2/Linf` gives `11R_Q/(48sqrt(2))`.  Replacing each `g_i` by the
corresponding sinc-weighted pair mode costs at most

```text
(3sqrt(2)/4)[1-2sin(1/2)]R_Q.                       (3.18)
```

The difference is `.118400280505230...R_Q` on `J`; passage to `H_Y` loses at
most a factor two and proves `(3.15)`.  The replay script certifies the final
constant and the geometric hypotheses; `(3.16)--(3.18)` are the analytic
part of the proof rather than sampled quadrature.

Both explicit fixtures satisfy these hypotheses.  Thus finite
primality-and-shell geometry does not forbid exact source-null directions.

This is still not an asymptotic LTRAD counterexample.  No theorem guarantees
two close pairs at every center supporting a hypothetical long negative
source event.  Infinitely many simultaneous prime values of the four
quadratics in `(3.7)` are also unproved.  The fixtures establish only that
pair absence is not a local or congruence-level feature one may assume.

## 4. What changes when the separator premise is restored

### 4.1 A one-cluster separator is impossible

For one pair, write its coefficients in sum/difference form

```text
y_-=(p+d)/2,             y_+=(p-d)/2.                (4.1)
```

In scaled time `s=t/B`, its polynomial is

```text
F(s)=p cos(Omega s)cos(zs/2)
    +d sin(Omega s)sin(zs/2),                        (4.2)
```

up to signs, where `Omega=mB`.  The source constraint is

```text
p[cos(Omega tau)cos(z tau/2)+D]
 +d sin(Omega tau)sin(z tau/2)=-1,
tau=t_0/B.                                           (4.3)
```

Under the corrector budget `|zd|<<epsilon_Y Y^(8/33)` and
`tau<=Y^(-17/33)`, the `d` term in `(4.3)` is

```text
O(epsilon_Y Y^(-3/11))=o(epsilon_Y).                 (4.4)
```

The coefficient of `p` has magnitude at most `2`, so

```text
|p|>=1/2-o(epsilon_Y).                               (4.5)
```

For ordinary-prime half-integer shells, `Omega>>B/Y=Y^(17/33)`.  If
`s_L=Y^.01/B`, choose an integer `k` of the parity matching the sign of `p`
such that

```text
s_*=k pi/Omega in [s_L,s_L+2pi/Omega].              (4.6)
```

Then `s_*=o(1)`, the difference term in `(4.2)` vanishes exactly, and
`cos(zs_*/2)=1-o(1)`.  Therefore

```text
h_Y(y)>=1/2-o(1).                                    (4.7)
```

This is much larger than `epsilon_Y`.  A corrected counterexample needs at
least two cluster centers and cross-cluster cancellation.

### 4.2 A certified three-pair control

One hostile-looking six-node model was tested exactly.  Put

```text
tau=1/500,                  z_1=z_2=z_3=1,
phi=(pi-2/5, pi+2/5, 7/10),
Omega_j=[phi_j+2pi(2j+1)]/tau,
omega_(j,+/-)=Omega_j+/-1/2.                         (4.8)
```

The cluster-center gaps exceed `4861>144pi`.  Calibrate `D` on the first four
nodes and set

```text
v_i=cos(omega_i tau)+D.                              (4.9)
```

The verifier constructs six high-band points `s_k` and positive weights
`w_k` satisfying, with Arb intervals,

```text
sum_k w_k=1,
sum_k w_k cos(omega_i s_k)=-r v_i      for every i,
r=.592871889898960588... .                           (4.10)
```

The seven-by-seven determinant is certified larger than `7.36*10^-5`; all
six weights are strictly positive.  Hence every source-normalized vector
obeys

```text
sum_k w_k F_y(s_k)=-r(y dot v)=r,
sup_s F_y(s)>=r>.5928.                               (4.11)
```

This cloud has no separator at the target scale, irrespective of corrector
energy.  It is one rigorous fixed-`tau` control, not a uniform three-cluster
theorem and not an asymptotically legal `tau=t_0/B -> 0` family.  Its
calibrating four-node source is also not asserted to be a contiguous
actual-prime interval.

## 5. Ordinary-prime cluster simplification

On either side of `Y`, distinct prime log nodes have spacing

```text
|log(q/Y)-log(p/Y)|=log(q/p)>=1/q>>1/Y.              (5.1)
```

Since `B^-1=Y^(-50/33)=o(Y^-1)`, every fixed-constant `B^-1` cluster contains
at most one lower prime and at most one upper prime for sufficiently large
`Y`.  More explicitly, use close edges at the chosen fixed multiple of
`B^-1`; same-side spacing is eventually more than twice that threshold, so
each node has at most one opposite-side neighbor.  The close-reflection graph
is a matching, and its connected components are singletons or pairs.  Thus
the prime-only LTRAD application needs only singleton and pair jets; triple
Newton jets are not needed unless proper powers or repeated modes are
reintroduced.

This settles the multiplicity part of B1.  It does not by itself settle the
uniform conditioning of arbitrarily tiny pair gaps or prove the B2 `L1`
constant.

## 6. Corrected decision tree

```text
deduction from source + energy alone
`-- abstract null-corrector obstruction: CLOSED AS INSUFFICIENT

separator-qualified B3
+-- one pair/one cluster: no separator, analytically CLOSED
+-- one fixed-tau three-pair fixture: no separator, CERTIFIED CONTROL
+-- adversarial two/few-cluster families with tau->0: OPEN
`-- uniform adversarial multicluster cloud: OPEN

actual-prime LTRAD_P(.0189,.001): OPEN
prime-supported DPA_P(.019):     independently OPEN
uniform strip / RH:              NOT PROVED
```

The next maximum-information experiment is now narrower.  Start with every
legal two-cluster phase configuration, then two calibrated event clusters plus
one external carrier cluster, before increasing the number of centers.  The
inner problem is best posed as separator feasibility:

```text
y dot v=-1,
h_Y(y)<=epsilon_Y,
||(z_j d_j)_j||_2<=C epsilon_Y Y^(8/33).             (6.1)
```

Use exchange to generate candidate extremizers and certify every continuum
upper or lower bound by interval derivative guards.  The outer search should
adversarially vary the calibrated event phases, pair gaps, and external
carrier phases while enforcing `tau=t_0/B -> 0`.

The decisive outcomes are:

1. a scalable synthetic family satisfying `(6.1)` kills the proposed
   axiomatic B3 mechanism; killing actual-prime LTRAD additionally requires
   actual prime nodes, a legal contiguous long source event, and every mask
   constraint;
2. a uniform positive dual measure like `(4.10)`, with constants surviving an
   arbitrary number of clusters, supplies the missing source-weighted theorem;
3. failure only because of a specific actual-prime constraint identifies the
   arithmetic invariant the theorem must exploit.

Only after an extremal separator is found should one evaluate the B2--B3
constant compatibility.  Optimizing `c_r H_J-E_corr` over vectors which are
not separators recreates the false statement closed in Section 2.

Finally, finite positive results cannot validate the asymptotic adapter: the
benchmark long source event is numerically unavailable below fantastically
large scales.  Finite runs are decisive only when they yield a scalable
countermodel or an analytic/interval-certified dual pattern.

## 7. Scope ledger

```text
generic displayed constraints imply the B3 margin:             DISPROVED;
actual-prime asymptotic B3 statement:                           OPEN;
Avg_I in the displayed B3 statement:                            UNDEFINED;
actual ordinary-prime close-pair fixtures:                      CERTIFIED;
source-null dimension K-1 for K reflected pairs:                PROVED;
one-cluster separator at epsilon_Y scale:                       EXCLUDED;
one six-node three-pair separator:                              EXCLUDED;
uniform multicluster separator theorem:                         OPEN;
LTRAD_P(.0189,.001):                                            OPEN;
DPA_P(.019):                                                    OPEN;
zero-free strip or RH:                                          NOT PROVED.
```

## 8. Dependencies

This audit refines, rather than supersedes, the exact transverse reduction in

- [`ZETA23-QP-LTRAD-FULL-RUN-SYNTHESIS-2026-08-28.md`](ZETA23-QP-LTRAD-FULL-RUN-SYNTHESIS-2026-08-28.md),
- [`ZETA23-QP-LTRAD-PRIME-ONLY-AND-REFLECTED-DIFFERENCE-REDUCTION-2026-08-28.md`](ZETA23-QP-LTRAD-PRIME-ONLY-AND-REFLECTED-DIFFERENCE-REDUCTION-2026-08-28.md), and
- [`ZETA23-FRONTIER-LITERATURE-IMPORT-AND-JOINT-RESEARCH-PROGRAM-2026-08-29.md`](ZETA23-FRONTIER-LITERATURE-IMPORT-AND-JOINT-RESEARCH-PROGRAM-2026-08-29.md).
