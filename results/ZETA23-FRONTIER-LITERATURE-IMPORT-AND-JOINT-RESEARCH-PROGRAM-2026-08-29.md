# Frontier literature import and joint research program

**Date:** 2026-08-29

**Literature checked through:** 2026-08-29

**Status:** source-checked theorem import, project dependency audit, and
falsifiable research proposal.

**Headline nonclaim:** neither the sharp four-cycle bound nor a uniform
zero-free strip is proved here.

## 0. Executive synthesis

The literature changes the research program, but it does not close either
headline gate.

1. **Sharp four-cycle:** Blomer--Pascadi has enough numerical saving in the
   correct modulus/length range, but only with a margin `q^(1/352)` after the
   project's `q^(1/66)` shortfall.  Its scalar two-frequency interface does
   not preserve the four QP masks.  Croot--Yip supplies a plausible
   local-character entropy mechanism for detecting structured exceptional
   mass, while Yao supplies a numerically aligned centered inverse-power
   estimate.  The best combined route is therefore:

   ```text
   residual branch I: mask-preserving BP interface
       -> black-box factorization and collective reconstruction; or
       -> proof-level centered chi(Delta): cancellation or bias-to-packet

   residual branch II: collective packet-free graph fourth moment

   structured terms -> entropy-weighted packet participation
   either complete residual branch + charged structured terms -> PAIR.
   ```

2. **LTRAD and the strip:** Jaming--Kellay--Saba gives the right resolved-
   frequency `L^1` lower bound, and Avdonin--Moran gives the right Newton-jet
   coordinates for unresolved clusters.  They do not connect the project's
   source normalization to surviving harmonic mass.  The best route is a
   new source-weighted, cluster-aware nonharmonic Littlewood theorem.  The
   separate positive-antenna gate `DPA_P(.019)` remains open.

3. **Project rigidity:** the finite Hankel interface of Elkies, combined
   with determinant integrality and primality, proves the new scoped project
   theorem `PHR2`: a pointwise rank-one shadow of pairwise-distinct shell
   primes at accuracy `Y^(1-A)`, `A>3/2`, has only `O(log Y)` terms.  This
   eliminates a tempting same-side near-geometric branch; it does not prove
   the inverse theorem that would create such a shadow.

The central lesson is that the missing mathematics is not another scalar
exponent improvement.  It is **dependency preservation**: masks and residual
layers for four-cycle, and source normalization plus cluster jets for
LTRAD.

## 1. Evidence labels and import rule

This file follows the repository's
[`PROOF-STANDARD.md`](../publication/PROOF-STANDARD.md).

| Label | Meaning in this file |
|---|---|
| `IMPORTED` | Displayed statement/interface checked against the cited primary source; cited source side conditions still govern. |
| `PROJECT-PROVED` | A proof exists in the linked project artifact. |
| `DERIVED` | A short deduction from imported or project-proved inputs is displayed. |
| `DIAGNOSTIC` | Exact or numerical evidence, not an infinite theorem. |
| `PROPOSAL` | A quantified or operational research target with a kill test. |
| `OPEN` | Needed implication not presently proved. |

An imported theorem is not treated as an application until its hypotheses,
normalization, coefficient class, quantifiers, and reconstruction loss all
match the project object.

## 2. The two headline targets must remain separate

### 2.1 Sharp four-cycle endpoint

At

```text
D=q^(16/33),
```

the exact positive endpoint is

```text
PAIR_epsilon:
sum_C m(C)(m(C)-1) w_z(C)
  << D q^epsilon ||z||_2^4.                           (2.1)
```

The project has proved, up to `q^o(1)`, equivalence with the signed dyadic
statement `DSP` and the Cartesian restricted-type statement

```text
CRT_epsilon:
N_cell(S_11,S_12,S_21,S_22)
  << D q^epsilon prod_(i,j)|S_ij|^(1/2).              (2.2)
```

It has also proved that reconstructing by a rootwise maximum is invalid.
The canonical record is
[`ZETA23-QP-COLLECTIVE-DYADIC-NEXT-GATE-AND-ROUTE-AUDIT-2026-08-28.md`](ZETA23-QP-COLLECTIVE-DYADIC-NEXT-GATE-AND-ROUTE-AUDIT-2026-08-28.md).

For a packet family `t` with amplitude `a_t`, the current exact abstract
participation condition is

```text
L=max_(c,d) sum_(t containing (c,d)) lambda_t,
R=max_(e,f) sum_(t containing (e,f)) a_t^2/lambda_t,
LR <= D^2 q^o(1).                                    (2.3)
```

### 2.2 Prime-only LTRAD and strip endpoint

The independent strip program needs

```text
DPA_P(.019)  and  LTRAD_P(.0189,.001).               (2.4)
```

After conditioning on the source event and writing
`y=y_car+y_corr`, the exact adapter target is

```text
sup_(t in H_Y) [F_car(t)+F_corr(t)]
  >= Y^(-.0179+o(1))                                 (2.5)
```

for every source-normalized legal dual vector satisfying the already proved
corrector bounds.  See
[`ZETA23-QP-LTRAD-FULL-RUN-SYNTHESIS-2026-08-28.md`](ZETA23-QP-LTRAD-FULL-RUN-SYNTHESIS-2026-08-28.md),
especially equations (7.1)--(7.6).

A sharp four-cycle estimate does not imply `(2.5)`: generic moment conversion
only reaches exponent `41/66=.621212...`, missing `.0179` by about
`.603312`.  The programs may share techniques, but neither is a dependency
of the other.

## 3. Imported Fourier, inverse, and cluster theorems

### LIT-F1 -- Bloom--Green inverse Littlewood structure (`IMPORTED`)

For a finite `A subset Z`, `|A|=N`, write

```text
hat(1_A)(theta)=sum_(n in A)e(-n theta),
E(B)=#{b_1+b_2=b_3+b_4},
omega[B]=E(B)/|B|^3.
```

[Bloom--Green, Theorem 1.2](https://doi.org/10.1093/qmath/haag016)
states that, for `N` sufficiently large, `delta in (0,1/2]`, and

```text
||hat(1_A)||_1 <= K log N,
```

there is an initial segment `A' subset A` such that

```text
|A'| >> N^(1-delta),              omega[A'] >> (delta/K)^2. (3.1)
```

Corollary 1.3 gives an arithmetic progression `P` of length at least
`N^(c_K)` with `|A intersection P|>=c_K|P|`.  A bounded signed decomposition
of the whole indicator into progression indicators is only their Conjecture
6.1.

**Exact project adapter.**  Use normalized Haar measure on the full period.
If `A=-A`, `0 notin A`, and `g=hat(1_A)` is real with mean zero and `g>=-H`, then
`||g||_1<=2H`.  More generally, for `G=c hat(1_A)+R`,

```text
c||hat(1_A)||_1 <= 2H+||R||_1                        (3.2)
```

when `c>0`, `G` is real, mean zero, and `G>=-H`.  Bloom--Green becomes
available only after extracting a commensurate approximately
equal-coefficient layer, controlling `R`, and verifying the literal threshold

```text
(2H+||R||_1)/c <= K log N.                            (3.2a)
```

**Nonapplication.**  The theorem uses integer frequencies, a full period,
and indicator coefficients.  Its conclusion concerns a large structured
subset, not pointwise organization of all weighted real frequencies.

### LIT-F2 -- Bedert polynomial Chowla bounds (`IMPORTED`)

[Bedert, Theorem 1.1, v3](https://arxiv.org/html/2509.05260v3) proves that
for every `A subset N`, `|A|=n`,

```text
min_(x in [0,2pi]) sum_(a in A) cos(ax)
  <= -n^(1/5-o(1)).                                  (3.3)
```

Theorem 1.2 says that for each fixed finite
`S subset R\{0}` there are `c_S,c'_S>0` such that every finite symmetric
`A subset Z\{0}` with coefficients `s_a in S`, `s_a=s_(-a)`, obeys

```text
min_x sum_(a in A)s_a e(ax) <= -c'_S n^(c_S).        (3.4)
```

**Derived obstruction.**  A normalized equal-weight carrier on `n` distinct
integer frequencies, tested on the full period, has minimum at most
`-n^(-4/5-o(1))`, much deeper than the Fejer scale `-1/n`.  Within that
commensurate model, a Fejer-shallow floor must escape the equal/fixed-alphabet
case, for example through growing coefficient complexity or cancellation by
another component.  This deduction says nothing directly about an arbitrary
real finite-band carrier.

**Nonapplication.**  The alphabet in `(3.4)` must be fixed as `n` grows.
After normalizing the Fejer cosine weights to sum to one, their largest size
is `Theta(1/n)` and their smallest is `Theta(1/n^2)`, across about `n` levels.
The theorem has no arbitrary-real finite-band or inverse-structure conclusion.

### LIT-F3 -- Belov--Konyagin growing-alphabet construction (`IMPORTED`)

Let `M_Z^downarrow(n)` be the least constant coefficient `a_0` for which

```text
T_n(x)=a_0+sum_(k=1)^n a_k cos(kx)>=0,
a_1>=...>=a_n>=1,              a_k in Z.
```

[Belov--Konyagin, Corollary 5.4](https://www.mathnet.ru/eng/im95) gives

```text
M_Z^downarrow(n) <= 31000(1+log n)^3.                (3.5)
```

Fourier positivity also gives `a_k<=2a_0`.  Normalizing by
`S_n=sum a_k>=n` therefore produces an AP-supported positive-weight carrier
with

```text
min_x sum_(k=1)^n (a_k/S_n)cos(kx)
  >= -31000(1+log n)^3/n.                            (3.6)
```

**Import verdict.**  This explains why a fixed-alphabet Bedert theorem cannot
handle near-positive carriers.  It is a candidate coefficient template for
`DPA_P`, not an actual-prime construction.

**Nonclaim.**  `(3.6)` is not sharp at constant `1/n`, and it neither proves
nor refutes Fejer stability.  It says nothing about transferring AP
frequencies to prime logarithms.

### LIT-NH1 -- Jaming--Kellay--Saba nonharmonic Littlewood (`IMPORTED`)

Let `lambda_1<...<lambda_N` be distinct real numbers and `a_k in C`.
[Jaming--Kellay--Saba, Theorem 1.1](https://arxiv.org/html/2303.10919v2)
gives

```text
lim_(T->infinity) 1/T int_(-T/2)^(T/2)
  |sum_k a_k exp(2pi i lambda_k t)| dt
  >= (1/26) sum_k |a_k|/(k+1).                       (3.7)
```

If `|lambda_k-lambda_l|>=|k-l|`, then for every `T>=72` the corresponding
finite mean is at least

```text
(1/122) sum_k |a_k|/(k+1).                           (3.8)
```

For `F(t)=sum a_k exp(iu_kt)` on a physical band of length `B`, ordered gaps
at least `gamma` and `gamma B>=144pi` give `(3.8)` after rescaling.

For any real `F`, normalized interval averaging gives the elementary relation

```text
max(sup F,0) >= (Avg|F|+Avg F)/2=Avg(F_+).            (3.9)
```

Thus, whenever its right side is bounded positively, a JKS `L^1` lower bound
plus control of the boundary mean yields the positive excitation required in
`(2.5)`.

**Nonapplication.**  Reflected or otherwise near-coincident frequencies
violate the separation hypothesis.  JKS is scalar and resolved-frequency;
it does not see intracluster cancellation jets, the source atom, or QP masks.

### LIT-CL1 -- Avdonin--Moran divided-difference coordinates (`IMPORTED`)

Let `Lambda` lie in a horizontal strip and be relatively uniformly discrete,
choose the paper's cluster radius `r<r_0`, and assume
`T>2pi D^+(Lambda)`.  Under these hypotheses,
[Avdonin--Moran, Theorem 3(ii)](https://matwbn.icm.edu.pl/ksiazki/amc/amc11/amc1143.pdf)
says that the cluster generalized-divided-difference family is an `L`-basis
in `L^2(0,T)` and can be extended to a Riesz basis.  If all `lambda_n` are
simple and this DD family is an `L`-basis, Proposition 1 gives

```text
||sum_(lambda in Lambda)a_lambda exp(i lambda t)||_2^2
  asymp sum_(clusters) G_cluster.                     (3.10)
```

For an ordered cluster `{lambda_1,...,lambda_n}`, its exact
Newton-coordinate energy is

```text
|sum_(k=1)^n a_k|^2
+sum_(m=2)^n
 |sum_(k=m)^n a_k prod_(j=1)^(m-1)(lambda_k-lambda_j)|^2. (3.11)
```

In particular, a pair contributes

```text
|a_1+a_2|^2+|a_2(lambda_2-lambda_1)|^2,              (3.12)
```

and a triple contributes the sum of its zeroth, first, and second Newton
jets.

**Exact project scaling.**  On an interval of length `B`, set
`tilde u_k=Bu_k`.  Clusters have physical diameter `O(B^(-1))`, and their
dimensionless jets are

```text
J_0=sum a_k,
J_(m-1)=sum_(k=m)^n a_k prod_(j<m)B(u_k-u_j).         (3.13)
```

This validates the project's reflected-pair sum/difference norm, up to a
uniform triangular change of coordinates.  For higher multiplicity it
supplies natural **ordering-dependent** Newton coordinates; different
enumerations are interchangeable only after the corresponding triangular
changes are proved uniformly conditioned.

**Nonapplication.**  Published constants depend on the global sequence and
frame hypotheses.  Proposition 1's displayed plain-exponential estimate also
assumes simple frequencies; repeated points require derivative or
polynomial-exponential modes.  Arbitrary finite `Y`-dependent prime-log
clouds still need uniform multiplicity, separation, density, and
conditioning.  The theorem is scalar `L^2`, not one-sided `L^1` or
source-weighted.

### LIT-POS1 -- positive trigonometric support constants (`IMPORTED` + `DERIVED`)

[Gorbachev--Manoshina](https://arxiv.org/html/math/0312320) define
`delta(K)` as the infimum of the constant coefficient `T_0` over nonnegative
trigonometric polynomials supported on `{0} union (+/-K)` and normalized by
`T(0)=1`.  Their basic identities include

```text
delta({1,...,q-1})=1/q,
delta(qK)=delta(K),
delta(K_1)delta(K_2)<=delta(K_1 union K_2).           (3.14)
```

If

```text
f(x)=sum_(k in K)w_k cos(2pi kx),
sum w_k=1,                        f>=-epsilon,
```

then `T=(f+epsilon)/(1+epsilon)` is admissible.  Therefore

```text
epsilon >= delta(K)/(1-delta(K)).                    (3.15)
```

The consecutive-support case recovers the exact Fejer floor `1/(q-1)`.  The
union-product inequality points in the **obstructive** direction:

```text
epsilon >= delta(K_1)delta(K_2)
           /(1-delta(K_1)delta(K_2))                 (3.16)
```

for any carrier on `K_1 union K_2`.  It does not construct a multiblock
polynomial or upper-bound the floor on the union.  Such a construction must
be supplied separately; multiplying two block polynomials generally creates
sum-and-difference frequencies outside the union.

## 4. Imported modular and recurrence theorems

### LIT-KL1 -- Blomer--Pascadi bilinear Kloosterman bound (`IMPORTED`)

For `1<=N<=c`, intervals `|I|,|J|<=N`, arbitrary complex coefficients, and
`a` invertible modulo `c`,
[Blomer--Pascadi, Theorem 1.1](https://arxiv.org/html/2607.24311) bounds

```text
sum_(m in I,n in J,(m,n,c)=1) alpha_m beta_n S(am,n;c)
```

by

```text
||alpha||_2||beta||_2 N c^(1/2+o(1))
 [c^(13/32)N^(-7/8)
  +c^(5/16)N^(-11/16)
  +c^(1/9)N^(-1/3)].                                 (4.1)
```

The result is valid for composite moduli; their Theorem 5.5 is asymmetric.
At `N=D=c^(16/33)`, the three relative factors are

```text
c^(-19/1056),            c^(-1/48),            c^(-5/99). (4.2)
```

The following exponent specialization is `DERIVED`.  The dominant saving
exceeds the project's `c^(-1/66)` local shortfall by
only

```text
19/1056-1/66=1/352.                                  (4.3)
```

There is also an exact project-derived fixed-layer Fourier identity

```text
sum_(x mod m)^* f(x)g(lambda inverse(x))
 =m^(-2)sum_(h,n mod m)hat(f)(h)hat(g)(n)S(h,nlambda;m). (4.4)
```

But a physical point mass has full additive-frequency support.  Cutting one
full side into length-`D` blocks costs

```text
sqrt(m/D)=q^(17/66+o(1)),                             (4.5)
```

where only `q^(1/352)` is affordable.  The exact direct-bridge audit is
[`ZETA23-QP-FOUR-CYCLE-BLOMER-PASCADI-EXACT-BRIDGE-ATTEMPT-2026-08-15.md`](ZETA23-QP-FOUR-CYCLE-BLOMER-PASCADI-EXACT-BRIDGE-ATTEMPT-2026-08-15.md).

**Import verdict.**  The exponent is strong enough; the interface is not.
In the prime-modulus discriminant reduction, a quadratic solution count has
the form `1+chi(Delta)`.  After centering, the useful object is the complete
signed character sum `chi(Delta)`: nonzero squares and nonsquares are the two
signs whose cancellation proves the bound.  They cannot be separated into a
positive exceptional square locus and a generic nonsquare locus.  Only
`Delta=0`, nonunit, and boundary terms are algebraically exceptional.

The required object is a QP-specific vector-valued, all-layer square function
that retains the joint four-completion mask and loses at most
`q^(1/352-o(1))`.

### LIT-RI1 -- Yao inverse-power fourth moment and fivefold asymptotic (`IMPORTED`)

For fixed `s>=1`, `M subset F_p^*`, `|M|=M`, and a shifted interval
`X subset F_p^*` of length `H`, put

```text
S_(M,X)(a)=sum_(m in M,x in X)e_p(amx^(-s)),
mu=min(M,sqrt(p)).
```

[Yao, Theorem 1.1](https://arxiv.org/html/2608.15458) proves

```text
sum_(a!=0)|S_(M,X)(a)|^4
  <<_s p H^2 M^2(H+mu)^2 p^o(1).                     (4.6)
```

Fix `epsilon>0`.  For `1<=i<=5`, let
`M_i subset F_p^*`, `|M_i|=M`, and let
`X_i=L_i+{1,...,H} subset F_p^*`.  If `H<=sqrt(p)` and

```text
H^27 M^26 > p^(14+epsilon)(H+mu)^24.                 (4.7)
```

[Yao, Theorem 1.2](https://arxiv.org/html/2608.15458) states that some
`delta=delta(s,epsilon)>0` gives, uniformly in `lambda in F_p`,

```text
T_5(lambda)=H^5M^5/p (1+O(p^(-delta))).              (4.7a)
```

In the balanced case Corollary 1.3 has threshold
`H=M=N>p^(14/29+epsilon)`.  The following project-scale specialization is
`DERIVED`:

```text
16/33-14/29=2/957>0,
p^(7/6+o(1))D^(-29/12)=p^(-1/198+o(1)).              (4.8)
```

This numerical alignment is genuine.

**Nonapplication.**  Yao has five independent Cartesian pairs, `D^2` points
per summand, positive indicator counts, and prime modulus.  A QP layer is a
weighted graph/matching of `O(D)` tied points with four completions and, in
the full shell, prime-power rows.  Cartesian completion gives `D^6`, while
the packet-free graph target is `D^(5/2+o(1))`.

The exact `PROJECT-PROVED` centering identity survives graph restriction, but the
saving does not.  For pairwise-distinct, injective carriers `v_k` indexed by
a set `K` with `|K|<=D`, the graph bound

```text
(1/p)sum_(a!=0)|sum_k c_k e_p(av_k)|^4
  <= D||c||_2^4                                      (4.9)
```

is sharp for the project-tested parabola graph.  See
[`ZETA23-QP-YAO-GRAPH-WEIGHTED-CENTERING-ADDENDUM-2026-08-24.md`](ZETA23-QP-YAO-GRAPH-WEIGHTED-CENTERING-ADDENDUM-2026-08-24.md).

### LIT-ENT1 -- Croot--Yip local quadratic entropy (`IMPORTED`)

Let `p=3 (mod 4)`.  For a probability measure `nu` on `F_p`, let

```text
W(nu)=p sum_y nu(y)^2-1.
```

If `W(nu)>0`,
[Croot--Yip, Proposition 4.1](https://arxiv.org/html/2607.15311) produces a
sign and a probability measure `lambda` for which

```text
Z(y)=sum_s lambda(s)(1+epsilon chi(y-s)) >= 1/2,
sum_y nu(y)log Z(y)
  >> min(W(nu),W(nu)^(1/2)p^(-1/2)).                 (4.10)
```

Proposition 5.1 multiplies compatible local gains over a finite set of primes
`p=3 (mod 4)`, assuming one common sign and

```text
Delta=prod p <= floor(sqrt(N))/2,                    (4.10a)
```

to find a quadratic image carrying enhanced mass.  These constraints permit
only a subpolynomial enhancement in the paper's application.  Theorem 1.5,
under the paper's half-residue hypotheses, gives

```text
|A intersection q(Z)|
  >> L^(-1) exp(c sqrt(log N)/loglog N),
L=max(1,sqrt(N)/|A|).                                (4.11)
```

At `N=q`, `|A|=D=q^(16/33)`, one has `L=q^(1/66)`, so `(4.11)` is
`q^(-1/66+o(1))<1` and is asymptotically vacuous.  The two-set Theorem 1.9
also requires `L` to be polylogarithmic, which fails here.

**Import verdict.**  The global theorem does not apply.  The local logarithmic
gain in `(4.10)` is a useful analogy because local gains add after taking
logs, but the literal product mechanism gives only `N^o(1)` enhancement and
cannot supply the polynomial mass demanded by A2.  A weighted QP version with
polynomial amplification would be new.  A weighted extension of the paper's
product argument is itself an inference from its proof, not an imported
stated theorem.

### LIT-H1 -- finite Hankel rank and finite recurrence (`IMPORTED`)

For a finite sequence `x_0,...,x_n` over a field and `0<=2m<=n+1`, Elkies
defines a degree-`m` relation by

```text
sum_(i=0)^m a_i x_(i+j)=0              (0<=j<=n-m),  (4.12)
```

with the `a_i` not all zero.  Equations (1)--(2) of
[Elkies](https://nyjm.albany.edu/nyjm/j/2002/8-5.pdf) identify this with rank
at most `m` of the `(m+1) x (n-m+1)` Hankel matrix.  Proposition 1 and its
following corollary give the minimal-relation/rank statement.  This is not
Elkies's numbered Theorem 1, which concerns a different finite-field result.

**Project consequence (`PROJECT-PROVED`).**  The companion artifact
[`ZETA23-PRIME-SHADOW-HANKEL-RIGIDITY-2026-08-29.md`](ZETA23-PRIME-SHADOW-HANKEL-RIGIDITY-2026-08-29.md)
proves that a pairwise-distinct shell-prime block satisfying

```text
|p_j-Yr^j|<=K Y^(1-A),                 A>3/2,        (4.13)
```

has length `O(log Y)`.  The Hankel algebra is classical; the finite prime
specialization appears unrecorded in the targeted search.  Boyd's
[nonrecurrent Pisot sequences](https://doi.org/10.4064/aa-32-1-89-98) show
why generic rounding-to-nearest-geometric heuristics cannot replace the
uniform shadow and integer-minor proof.

## 5. Literature-to-project crosswalk

| Input | What transfers exactly | What does not transfer | Assigned role |
|---|---|---|---|
| Bloom--Green | Small full-period `L^1` gives a large high-energy/AP-rich integer subset | Real frequencies, arbitrary weights, all-support rigidity | Late inverse diagnostic after quantization |
| Bedert | Equal/fixed-alphabet integer carriers have polynomially deep negative values | Growing alphabets, clusters, arbitrary real frequencies | Exclude overly simple LTRAD/DPA models |
| Belov--Konyagin | Growing positive integer weights permit polylogarithmically shallow AP floors | Prime-log transfer and sharp floor | Candidate DPA coefficient family |
| JKS | Resolved real frequencies give finite-band harmonic-weighted `L^1` | Clusters, source normalization, vector masks | Analytic backbone of LTRAD adapter |
| Avdonin--Moran | Ordering-dependent Newton jets and cluster `L^2` coordinates | Uniform finite-cloud `L^1` and one-sided excitation | Cluster coordinate system after conditioning |
| Gorbachev--Manoshina | Exact support floor and union-product lower obstruction | A union-support construction or prime-log realization | DPA obstruction ledger |
| Blomer--Pascadi | Enough scalar Kloosterman saving at `D=q^(16/33)` | Four masks, full frequencies, residual layers | Residual cancellation after a new vector adapter |
| Yao | Centering identity and a numerically aligned `p^(-1/198)` fivefold gain | Graph support, four tied variables, weights | Model for packet-free centered theorem |
| Croot--Yip | Local character bias gives additive log-entropy gain | Polynomial mass and compatible paired packets at QP density | Analogy for a new structured-locus detector and weight design |
| Elkies | Finite Hankel rank iff finite relation | Prime classification or approximate-to-exact threshold | Algebraic core of PHR2 and higher-rank program |

No row in this table can be promoted to a project theorem by deleting its
third column.

## 6. Research Program A -- close the sharp four-cycle bound

### A0. Fixed acceptance target

The only accepted endpoint is `PAIR_epsilon`, or the already proved
equivalent `CRT_epsilon`.  A renamed large sieve, a rootwise maximum, a
Cartesian completion with a fixed-power loss, or an unweighted graph theorem
is not closure.

### A1. Choose and complete a mask-preserving BP interface (`PROPOSAL`, priority 1)

There are two distinct interfaces; a proof must choose one rather than mix
them.

**A1-black-box.**  Apply `(4.1)` only after proving that an actual QP cell is
a controlled sum of forms with:

- one fixed modulus `c=q^(1+o(1))` and one unit parameter `a` per form;
- two interval variables of length `N=D=c^(16/33+o(1))<=c`;
- factorized coefficients `alpha_m beta_n` and the theorem's gcd support;
- a nuclear/factorization norm compatible with rank-one Cartesian tests; and
- collective reconstruction over all rows, residual layers, and four colors.

It must also directly estimate every gcd-excluded, zero-frequency,
nonfactorizable, and boundary piece within the `CRT` budget.  Merely removing
those pieces from the BP form is not a charge.

**A1-proof-level.**  Reopen the Blomer--Pascadi Hölder/Cauchy argument and
prove that the QP masks survive until its discriminant count.  At prime or
appropriate squarefree modulus, preserve the **unsplit** centered character
`chi(Delta)` on `Delta!=0`, while separating only `Delta=0`, nonunit, and
boundary terms.  Prime-power/depth rows do not automatically have this
Legendre-character interface; this route must either reduce them to prime
rows without a power loss or prove the required depth-aspect analogue.
The same deliverable must bound `Delta=0`, nonunit, and boundary terms within
the project target, or map them to a separately quantified packet extractor
whose full union is admissible for A4.

**Deliverable A1.**  A literal transformation, its factorization/nuclear-norm
ledger, and its row/layer reconstruction ledger.  If the current BP exponent
is the sole saving, their total loss must be at most `q^(1/352-o(1))`.

**Kill test A1.**  Certify that the infimum conversion cost over every allowed
factorization is a fixed power larger than `1/352`, or that an unavoidable
prime-power channel has no depth-aspect substitute.  Either finding closes
the current BP branch.  The known blockwise triangle conversion already
costs `q^(17/66)` and fails by `q^(269/1056)`.

### A2. Large aggregate discriminant-character bias implies a compatible packet (`OPEN`)

Fix the admissible physical packet class before stating the theorem.  On each
cell, normalize the common dual test by `||Y||_HS=1` and define

```text
V(R,Y)=||R^*Y||_op/D^(1/2)                            (6.0a)
```

for the current residual map `R`.  Prove an exact stopping-time
decomposition.  Whenever `V(R,Y)>=q^delta`, output a compatible physical
packet submap `P` and `R'` such that

```text
R=P+R',
||P^*Y||_op >= q^(-theta(delta)+o(1))||R^*Y||_op,
V(R',Y) <= q^(-kappa(delta))V(R,Y),                   (6.0b)
```

with explicit `0<=theta(delta)<delta`, `kappa(delta)>0`, and a stated
`O_(delta,epsilon)(1)` step bound to reach `V<=q^epsilon`.  Across all steps,
the **union** of packet submaps must have one physical packet presentation
whose amplitudes/incidences satisfy the A4 hypothesis with only `q^o(1)`
reconstruction loss.  Per-step load bounds that accumulate a fixed power do
not qualify.

At termination, the exact sum of all packet maps and the final residual is
the input to A4 and A3 respectively.

The packet must live in the physical variables, not merely in an auxiliary
quadratic label.  Its left and right parameterizations must be compatible.
An unspecified "polynomial fraction" is insufficient: it can consume the
entire `q^delta` excess before A4 is applied.

**Literature mechanism.**  Equation `(4.10)` shows locally how collision
variance creates a quadratic-character weight with positive log gain.  Its
published product theorem pays a `|E|/sqrt(N)` baseline and gives only
subpolynomial enhancement here, so polynomial extraction, the physical lift,
and two-sided compatibility are all new mathematics.

**Kill test A2.**  Exhibit a legal sequence of post-A1 residuals for which

```text
V(R,Y)>=q^eta                                         (6.0c)
```

for fixed `eta>0`, while no predeclared packet family retains the mass
required by `(6.0b)` or satisfies the global A4-load condition.  Merely
observing `o(log q)` Croot--Yip gain only kills that mechanism, not the
dichotomy, unless the residual also violates A3 as in `(6.0c)`.

### A3. QP vector-valued Blomer--Pascadi square function (`OPEN`)

For one common dual test `Y`, let `Y_res` be its coordinate projection onto
the final residual codomain selected by the exact A2 partition; require
`||Y_res||_HS<=q^o(1)||Y||_HS`.  Let `Phi_res` be the corresponding actual CP
map, retaining the full centered character form on `Delta!=0`.  Prove an
all-layer theorem that square-sums additive-frequency blocks instead of
applying blockwise triangle inequality.  A sufficient restricted-channel
endpoint is

```text
||Phi_res^*(Y_res)||_op
  << D^(1/2)q^o(1)||Y_res||_HS.                       (6.1)
```

The theorem must preserve the four masks and allow the residual parameter to
vary with the layer.  Generic full-frequency strengthening is false; QP
dependency is an essential hypothesis.

A separate exact, per-test reconstruction lemma must use that same `Y` and
partition to prove

```text
B(Y,X)=B_alg(Y_alg,X)+B_packets(Y_packets,X)
       +B_res(Y_res,X),
sum_* ||Y_*||_HS^2 <= q^o(1)||Y||_HS^2.              (6.1a)
```

Here the partition may depend on `Y`, but it must remain a literal partition
of the original contribution; the first two terms are charged by A1/A4.
Without `(6.1a)`, `(6.1)` is only a restricted estimate and does not imply
the full CP or four-cycle target.

**Kill test A3.**  The direct falsifier is a legal packet-free family with the
ratio in `(6.0c)` at least `q^eta`.  Frequency-block concentration is only a
diagnostic unless it lower-bounds the infimum over every allowed
factorization/decomposition in A1.  For a current-BP black-box adapter, a
certified minimum conversion cost above `q^(1/352)` separately exhausts the
available exponent.

### A4. Entropy-weighted packet participation (`OPEN`)

For packets produced by A2, choose positive weights `lambda_t` satisfying
`(2.3)`.  In logarithmic variables `x_t=log lambda_t`, optimize the convex
potential

```text
Phi(x)=log max_(c,d) sum_(t containing (c,d))exp(x_t)
      +log max_(e,f) sum_(t containing (e,f))a_t^2 exp(-x_t). (6.2)
```

The target is

```text
inf_x Phi(x) <= 2log D+o(log q).                      (6.3)
```

Croot--Yip suggests, by analogy, constructing `x_t` from sums of local log
gains instead of assigning packets independently.  Its theorem supplies
neither the polynomial gain nor `(6.3)`.

**Kill test A4.**  Exact or certified convex optimization on a growing legal
fixture with `inf Phi>=2logD+c logq` closes this packet family unless A2
produces a different decomposition.

### A5. Alternative collective packet-free graph route (`OPEN`, priority 2)

After removing all certified packets with their charges intact, first prove
the normalized local ingredient

```text
(1/p)sum_(a!=0)|sum_k c_k e_p(a v_k)|^4
  << D^(1/2+o(1))||c||_2^4                           (6.4)
```

for each **actual injective residual completion graph**.  Flat coefficients
with `||c||_2^2=D` give the `D^(5/2+o(1))` scale.  The mask-blind bound `(4.9)`
is larger by `D^(1/2)` and is sharp on the parabola control, so
packet-freeness must do real work.

The local lemma is not enough.  Prove a collective direct-sum reconstruction
over every root, residual layer, four-color mask, and factorial weight that
bounds the residual contribution to each `DSP/CRT` cell.  Taking a rootwise
maximum is forbidden by the existing counterexample.  The graph branch also
needs its own inverse clause: a fixed-power failure of the collective bound
must extract an A4-chargeable packet with subpower loss.

Finally, `(6.4)` is a prime-field statement.  Full-shell closure needs an
additional **A5-depth** node: either reduce every prime-power row to its prime
field with `q^o(1)` total loss while preserving the masks, or prove the
corresponding centered graph theorem over `Z/p^aZ`.  Without A5-depth, this
branch proves only the prime-row subproblem.

Any actual noninjective carrier channel must likewise be coalesced and
charged as an algebraic/packet term, or handled by a separate collective
theorem; `(6.4)` does not apply to it.

Yao's centered proof is a guide, not an import.  If an adapter relies solely
on the balanced fivefold gain in `(4.8)`, its exact reconstruction ledger
must lose less than `p^(1/198)`; this is not a universal budget for other
graph arguments.  Pinning a dummy fifth pair does not preserve the averaging
and does not qualify.

**Kill test A5.**  A packet-free actual family satisfying

```text
[(1/p)sum_(a!=0)|sum_k c_k e_p(av_k)|^4]/||c||_2^4
  >= D^(1/2+eta)                                      (6.4a)
```

for fixed `eta>0` falsifies the local claim.  Independently, failure of the
collective direct-sum reconstruction kills this route even if every local
graph obeys `(6.4)`.  The parabola graph remains a mandatory hostile control:
the packet definition must either detect its structure or explain why actual
QP masks exclude it.

### A6. Closure dependency

There are three alternative, not cumulative, residual branches:

```text
BP black-box branch:
  A1-black-box + scalar BP + direct bounds for every non-BP term
  + exact collective reconstruction
  => CRT_epsilon.

BP proof-level branch:
  A1-proof-level + A2 character-bias inverse + A3 residual estimate
  + A4 packet participation + exact collective reconstruction
  => CRT_epsilon.

Graph branch:
  exact collective graph reduction + A5-depth
  + A5 graph inverse/residual theorem
  + A4 packet participation + A5 direct-sum reconstruction
  => CRT_epsilon.

Either branch + project-proved CRT_epsilon <=> PAIR_epsilon
  => sharp four-cycle bound.                          (6.5)
```

The best current bet is the A1--A4 BP/character-entropy hybrid.  A5 is a
fallback branch, not an additional undefined remainder required on top of
A3.

## 7. Research Program B -- source-weighted cluster Littlewood for LTRAD

### B1. Uniform finite prime-log cluster decomposition (`PROPOSAL`)

At resolution `B^(-1)`, partition the symmetric prime-log frequencies into
clusters of uniformly bounded multiplicity, and use `(3.13)` as the
coordinate vector.  Prove a finite, uniform version of the divided-difference
frame estimate for the actual `Y`-dependent cloud.

**Acceptance conditions.**  State the dependence on maximum multiplicity,
intercluster gap, interval length, and Newton change-of-basis condition
number.  Boundary truncation must be explicit.

**Kill test B1.**  An actual sequence with unbounded local multiplicity or
polynomially ill-conditioned Newton basis at scale `B^(-1)` invalidates a
uniform bounded-cluster formulation.

### B2. Jet-valued finite-band JKS theorem (`OPEN`)

Order the clusters `C_1,C_2,...` by increasing frequency and require
set-to-set separation at least `144pi/B` between every two distinct
clusters.  Define their jet vectors `J(C_n)` by `(3.13)` after fixing an
internal ordering, and put

```text
rho_n=1+sum_(j<n)|C_j|.
```

Prove a bound of the schematic but falsifiable form

```text
1/B int_I |F(t)|dt
  >= c_r sum_n ||J(C_n)||/(rho_n+1),                  (7.1)
```

where `r` is the maximum cluster size and different internal orderings give
uniformly equivalent norms under the B1 conditioning hypotheses.  For
bounded `r`, `rho_n+1` is comparable to `n+1` with `r`-dependent constants.
For singleton clusters this must reduce to JKS `(3.8)`; for pairs it must
retain both sum and scaled difference modes.

This is the analytic portion of the missing theorem.  It is plausibly
separable from zeta arithmetic and is the cleanest theorem-prover target
after PHR2.

**Kill test B2.**  Search finite clusters of size two and three for coefficient
vectors whose Newton mass is fixed but whose band `L^1` tends to zero.  Any
such family falsifies the proposed norm or identifies a missing jet weight.

### B3. Source normalization forces weighted surviving jet mass (`OPEN`, hard)

Restrict to the conjugate-symmetric legal duals for which `F_car`, `F_corr`,
and their sum are real.  Define

```text
H_J(y_car)=sum_n ||J(C_n;y_car)||/(rho_n+1),
E_corr(y)=Avg_I|F_corr|+|Avg_I(F_car+F_corr)|.         (7.2)
```

For every legal decomposition `y=y_car+y_corr` with `y dot v=-1` and the
known pointwise source-phase corrector bounds, prove the genuinely new global
estimate

```text
c_r H_J(y_car)-E_corr(y)
  >= 2Y^(-.0179+o(1)).                                (7.3)
```

This is where the actual prime mask, source atom, and carrier/corrector
noncancellation enter.  The existing estimate for `F_corr(t_0)` does **not**
control `Avg_I|F_corr|`, so `(7.3)` contains a new corrector obligation.
Neither JKS nor Avdonin--Moran contains this implication.

**Fast falsifier B3.**  On exact prime clouds, treat the margin
`c_r H_J-E_corr` as a global difference-of-convex optimization subject to
source normalization, the permitted corrector energy, conjugate symmetry,
and all carrier constraints.  A discretized search must include a rigorous
quadrature/Lipschitz error for the interval averages; otherwise it is only a
diagnostic.  A certified polynomially smaller feasible value produces a
countermodel, while certified relaxations may suggest the correct analytic
inequality.

### B4. One-sided conversion and LTRAD closure

By B2 and the triangle inequality,

```text
Avg_I|F_car+F_corr|
  >= c_r H_J-Avg_I|F_corr|.
```

Combining this with `(3.9)` and `(7.3)` gives `(2.5)`, hence
`LTRAD_P(.0189,.001)` through the already audited transverse-mixing step.
Without the averaged corrector term in `(7.3)`, B2 only locates a large
carrier phase at which the corrector could still cancel it.

The project theorem PHR2 is a branch terminator here.  It applies only if an
inverse argument produces a contiguous superlogarithmic block of
pairwise-distinct primes in one fixed shell, with the pointwise estimate
uniform in every index:

```text
|log(p_j/Y)-jh|<<mathcal_B^(-1),
mathcal_B=Y^(50/33).                                  (7.4)
```

PHR2 contradicts it.  Therefore a successful proof must exploit genuine
cluster jets, nonlocal correction, or growing coefficient complexity rather
than a single literal near-Fejer prime block.

## 8. Research Program C -- the independent positive antenna `DPA_P(.019)`

This program is constructive and must not be folded into LTRAD.

### C1. Multiblock positive carrier design (`PROPOSAL`)

Use the extremal support constant `(3.14)--(3.16)` as an obstruction ledger
and Belov--Konyagin weights as candidate within-block profiles.  An explicit
nonnegative polynomial on the proposed union support is still required.
Because PHR2 rules out any **pointwise-transferred**, superlogarithmic
prime-log AP satisfying its fixed-shell hypotheses at project resolution,
prioritize many short blocks rather than one such long block:

```text
short prime-log blocks
  -> positive/growing-alphabet profiles within blocks
  -> explicit union-support construction
  -> check against the union-product lower obstruction
  -> cross-block phase and source normalization audit
  -> DPA_P(.019).                                     (8.1)
```

### C2. Structural diagnostics

- Apply Bedert to any commensurate equal- or fixed-alphabet layer; a shallow
  floor forces that layer to be small or cancelled.
- Apply Bloom--Green only after quantization and residual control.  Its
  AP-rich subset is a diagnostic, not whole-support rigidity.
- In the exact commensurate full-period model, compare every candidate floor
  to `delta(K)/(1-delta(K))`; positivity cannot beat that support extremal
  constant.  Re-establish the comparison after any real-frequency finite-band
  transplantation.

### C3. Kill tests

1. Transfer the proposed integer support to actual prime logs and compute the
   complete phase-error term; any fixed-power loss larger than `.019` kills
   that schedule.
2. Retain the prime-only source normalization and all boundary terms.  A
   positive abstract polynomial without that transfer is not DPA.
3. Test whether cross-block interactions destroy the proposed floor.  The
   union-product inequality is only a lower obstruction for `delta`; it does
   not construct a polynomial on the union and gives no automatic stability
   under approximate real-frequency transplantation.

## 9. Cross-cutting higher-rank Hankel program

Fix an integer `m>=1`, constants `K,C_0>0`, and a real `A>1`.  For each
sufficiently large `Y`, let `L>=2m+1`, let `x_0,...,x_(L-1)` be integers,
and allow `alpha,r>0` to depend on the block.  Suppose

```text
g_j=alpha r^j,                 |g_j|<=C_0Y,
|x_j-g_j|<=E=K Y^(1-A)         (0<=j<L),             (9.0)
```

with `K,C_0,A,m` fixed uniformly in `j,L,Y`.  Form the `(m+1)x(L-m)`
Hankel matrix `(x_(i+j))` with `0<=i<=m` and
`0<=j<L-m`.  In any `(m+1)x(m+1)` minor, at least `m` columns must come from
the error:

```text
|det| <<_m Y E^m+E^(m+1)
      << Y^(m+1-mA)+Y^((m+1)(1-A)).                  (9.1)
```

Thus

```text
A>1+1/m                                               (9.2)
```

forces every integer minor to vanish for all sufficiently large `Y` and gives
finite Hankel rank at most `m` through Elkies.  This is a valid higher-minor
amplification of the cubic threshold.

It does **not** prove that a rank-`m` prime block is logarithmically short.
For `m>=3` the missing mathematics splits into:

1. rank-drop localization when consecutive top Hankel minors vanish;
2. unimodular denominator/height rigidity for a rational companion map; and
3. a unit-spectrum prime obstruction for roots of unity and confluent/Jordan
   components.

For fixed integers `R,s>=1`, a genuine rank-`R` exponential-polynomial
reference whose entries are at most `C_0Y` has a different exponent ledger.
In a `k=R+s` minor, at most `R` reference columns survive, giving, with an
implicit constant depending on `R,s,C_0`,

```text
|det| << Y^R E^s,
A>1+R/s.                                              (9.3)
```

Forcing rank at most `R` from `(R+1)`-minors would require `A>R+1`, not
`1+1/R`.  More generally, `k=R+s` only gives rank at most `k-1`, not rank
`R`.  This distinction prevents an attractive but false confluent-rank
generalization.

Higher rank is therefore a secondary program.  First formalize PHR2; then
search for order-three countermodels before proposing `PR_3` as a theorem.

## 10. Ordered execution plan

### Phase I -- cheap decisive tests

1. Complete A1 on one exact actual QP cell: either exhibit the black-box
   factorization and nuclear-norm ledger, or carry the masks through BP's
   proof-level reductions and preserve the unsplit centered character while
   isolating zero, nonunit, and boundary loci.
2. Implement the convex optimizer `(6.2)` on existing packet fixtures.
3. Implement the B3 finite source/jet minimization on actual prime clouds.
4. Test pair and triple cluster versions of `(7.1)` symbolically and
   numerically.
5. Freeze and independently review PHR2.

Each item can falsify a major route before a long proof attempt.

### Phase II -- theorem construction

1. If A1-black-box passes, prove its collective reconstruction.  If
   A1-proof-level passes, prove A2 and A3 in parallel and feed A2 packets
   immediately into A4.
2. If B2's finite tests pass, prove the analytic jet-valued JKS theorem
   independently of the source arithmetic.
3. Use the B3 optimization dual to formulate the actual source-weighted
   inequality.
4. Build multiblock DPA candidates only after their exact real-frequency
   transfer ledger is fixed.

### Phase III -- reconstruction and adversarial review

1. Reconstruct one complete residual branch from A6 to `CRT`, then use the
   already proved `CRT<=>PAIR` bridge without changing masks or packet
   charges.  Do not combine A3 and A5 as undefined overlapping remainders.
2. Reconstruct B2--B4 to `(2.5)`, then to `LTRAD_P`; combine with DPA only
   after `DPA_P(.019)` is independently proved.
3. Run separate mathematical and artifact reviews under the repository proof
   standard.  No red node may disappear into prose.

## 11. Priority and stop rules

| Rank | Workstream | Why it is credible | Immediate stop rule |
|---:|---|---|---|
| 1 | A1--A4 discriminant/packet/entropy hybrid | BP clears the exact exponent gap; Croot--Yip suggests a local-gain mechanism | Every mask-preserving BP conversion costs `>q^(1/352)`, or a normalized A3 failure has no packet of the required mass |
| 2 | B1--B3 cluster-aware source Littlewood | JKS and Avdonin--Moran supply the two analytic halves | Source-normalized finite LP has a stable smaller-power countermodel |
| 3 | A5 Yao-style packet-free remainder | Yao is numerically in range and project centering is exact | Normalized residual energy exceeds `D^(1/2+eta)||c||_2^4` |
| 4 | C1 multiblock DPA construction | BK and support extremals show growing-alphabet positivity is plausible | Prime-log transfer or cross-block terms consume `.019` |
| 5 | Higher-rank prime Hankel | The determinant amplification is exact | Order-three finite search exposes long bounded-shell countermodels or no usable denominator rigidity |

This ranking is about expected information gain, not a claimed probability
of proof.

## 12. What would count as genuinely new mathematics

The literature audit leaves four precise novelty candidates.

1. **Mask-sensitive vector-valued quadratic-discriminant large sieve:** A3,
   with the exact four QP masks and all residual layers.
2. **Entropy-to-compatible-packet inverse theorem:** A2--A4, turning local
   quadratic bias into one physical two-sided packet with controlled loads.
3. **Source-weighted cluster Littlewood theorem:** B2--B3, combining Newton
   jets, harmonic `L^1`, and an adaptive source normalization.
4. **Finite prime-shadow rigidity:** PHR2, already proved in its scoped
   pointwise order-two form; higher-order versions remain open.

Bloom--Green, Bedert, JKS, Avdonin--Moran, Blomer--Pascadi, Yao, Croot--Yip,
and Elkies are antecedents or modules.  Reproving any one of them in project
notation is dependency verification, not closure of a headline gate.

## 13. Claim ledger

| Claim | Status |
|---|---|
| Source-checked theorem interfaces in Sections 3--4 | `IMPORTED`; source side conditions control |
| `PAIR <=> DSP <=> CRT` up to `q^o(1)` | `PROJECT-PROVED` in the linked collective audit |
| Rootwise maximum reconstruction is invalid | `PROJECT-PROVED` in the linked collective audit |
| General graph centering identity; injective-carrier `D||c||_2^4` bound | `PROJECT-PROVED` in the linked Yao audit |
| PHR2 finite prime-shadow rigidity | `PROJECT-PROVED`; independent review/formalization pending |
| Sharp four-cycle bound | `OPEN` |
| A1 mask-preserving BP interface (black-box or proof-level) | `OPEN` |
| A2 compatible packet inverse theorem | `OPEN` |
| A3 vector-valued BP theorem | `OPEN` |
| A4 entropy-weighted load theorem | `OPEN` |
| A5 packet-free `D^(5/2)` graph theorem | `OPEN` |
| A5 prime-power/depth adapter | `OPEN` |
| A5 collective direct-sum reconstruction | `OPEN` |
| B2 jet-valued JKS theorem | `OPEN` |
| B3 source/carrier/corrector margin `(7.3)` | `OPEN` |
| `LTRAD_P(.0189,.001)` | `OPEN` |
| `DPA_P(.019)` | `OPEN` |
| Uniform zero-free strip from this program | conditional on the preceding two open gates |

The research program should be judged by how quickly these red nodes are
proved or falsified, not by how many equivalent reformulations are produced.
