# QP spectral nulling: exact Delsarte dual and grouping gate

**Date:** 2026-08-14  
**Verdict:** the full actual-prime QP extremal is **not solved**, but two
apparently different escape routes can now be disposed of exactly.

First, the positive-antipode problem is literally a compact Delsarte moment
problem.  Whenever the spectral-null feasible set is nonempty, if `p_*` is
the largest possible atom at zero in such a measure, then

```text
p_*=1/A_H,                 r_+=1/(A_H-1),              (0.1)
```

where `A_H` is the largest value at zero of an actual-node cosine polynomial
with constant coefficient one which is nonnegative on the complete high
band.  Thus a Delsarte, Beurling, or prolate construction advances QP only if
it proves the already missing one-sided actual-prime antenna.  Repackaging
the problem does not weaken that theorem.

Second, there is an exact legal positive nuller with a genuine high-frequency
gap.  A node-by-node Bernoulli convolution has

```text
spectral support {0} union +/-[T,B],
all actual-node Fourier values zero,
p=2^(-M),             r=1/(2^M-1).                    (0.2)
```

For a half-integer shell centre its upper support is

```text
MT+O_w(Y log Y)<Y^(50/33)                              (0.3)
```

when `T=Y^.01`.  This repairs the low-frequency leakage in the elementary
Riesz-product construction, but its retained carrier is exponentially too
small.

More generally, every one-sided convolution architecture with `G` nonempty
nulling factors has

```text
r<=1/(2^G-1).                                          (0.4)
```

Reaching `r=Y^(-.0180303234+eta)` therefore requires only `O(log Y)`
factors, so at least one factor must jointly null

```text
Omega(M/log Y)=Y^(1-o(1))/log Y                        (0.5)
```

nodes.  Grouping bounded, fixed, or polylogarithmically many nodes does not
change the power barrier.  A macroscopic group factor is the original
growing-dimensional finite-return problem in another form.

Finally, allowing the harmonic support to be chosen *after* seeing a Haar
phase vector does not rescue the dense-root-grid construction.  For every
`K subset {1,...,D}` simultaneously, its depth-`r` feasibility probability
is at most

```text
D exp(-M r^2/2).                                       (0.6)
```

At the QP scale this is
`exp[-Y^(.9639393532+2 eta-o(1))]` for every polynomial `D`.
This is a rigorous metric no-go, not an actual-prime theorem.

---

## 1. Spectral-null formulation

Let `u_1,...,u_M` be nonzero real nodes and

```text
H=[T,B],       0<T<B,
a(t)=(cos(tu_j))_(j<=M),       q_0=(1,...,1).          (1.1)
```

Write `r_+(H)` for the largest `r` for which a probability `nu` on `H`
satisfies

```text
integral_H a(t)dnu(t)=-r q_0.                          (1.2)
```

After symmetrizing `nu`, define

```text
sigma=[r delta_0+nu]/(1+r).                            (1.3)
```

Then `sigma` is an even probability on

```text
K_H={0} union [-B,-T] union [T,B]                      (1.4)
```

and exactly

```text
hat sigma(u_j)=0,               j<=M,
sigma({0})=p=r/(1+r).                                  (1.5)
```

Conversely, deleting the atom `p delta_0` from any probability satisfying
(1.5) and renormalizing gives (1.2) with

```text
r=p/(1-p).                                             (1.6)
```

A zero node is a genuine obstruction, not a removable degeneracy:
`hat sigma(0)=1` for every probability.  The centred architecture avoids it
by choosing the shell centre away from the integer prime powers; the
half-integer choice below gives a quantitative margin.

---

## 2. Exact Delsarte value

Define

```text
A_H=sup {Q(0):
 Q(t)=1+sum_(j<=M)lambda_j cos(tu_j),
 lambda_j real,
 Q(t)>=0 for every t in H}.                            (2.1)
```

The coefficients are allowed to be signed.  Requiring positive coefficients
is a useful stronger antenna ansatz, not the exact dual problem.

### Theorem 2.1 (central-atom/Delsarte reciprocity)

Assume at least one probability satisfies the spectral-null constraints in
(1.5), and let `p_*` be the largest central atom among them.
With the usual reciprocal conventions at zero and infinity,

```text
p_*=1/A_H,                 r_+(H)=1/(A_H-1).            (2.2)
```

#### Proof

The indicator of `{0}` is continuous on the compact, disconnected set
`K_H`.  The positive-measure linear program is

```text
maximize sigma({0})
subject to integral 1 d sigma=1,
           integral cos(tu_j)d sigma=0,   j<=M,
           sigma>=0 on K_H.                               (2.3)
```

Its compact moment-cone dual minimizes `c` subject to

```text
F(t)=c+sum_j z_j cos(tu_j)>=0,       t in H,
F(0)>=1.                                                (2.4)
```

Weak duality follows by integrating `F` against `sigma`; equality follows
by finite-dimensional separation of the compact moment cone.  The
nonemptiness hypothesis is needed here; Theorem 3.1 verifies it under the
explicit aperture budget (3.3).

For `c>0`, normalize `Q=F/c`.  Conversely, every admissible `Q` in (2.1)
gives `F=Q/Q(0)` in (2.4), with constant coefficient `1/Q(0)`.  Taking the
infimum in (2.4) and the supremum in (2.1) gives `p_*=1/A_H`.  Equation
(1.6) gives the second identity.  QED

The exact exponent polarity is now transparent:

```text
PROMOTE at r>=Y^(-kappa+eta)
  requires A_H<=1+Y^(kappa-eta);

positive-QP KILL at r<=Y^(-c)
  follows from A_H>=1+Y^c.                              (2.5)
```

Thus a prolate or continuous Delsarte extremizer helps only after its
spectrum has been transferred to the **prescribed actual nodes** while
retaining nonnegativity on every point of `[T,B]`.  That transfer is the
one-sided high-tail antenna itself.

---

## 3. An exact gapped Bernoulli nuller

For each nonzero node choose the smallest odd half-period above the lower
edge:

```text
s_j=(2m_j+1)pi/|u_j|>=T,
s_j<T+2pi/|u_j|.                                       (3.1)
```

Set

```text
eta_j=(delta_0+delta_(s_j))/2,
eta=eta_1*...*eta_M,
sigma=(eta+check eta)/2.                               (3.2)
```

Here `check eta(E)=eta(-E)`.

### Theorem 3.1 (exact finite-aperture Bernoulli construction)

If

```text
MT+2pi sum_j 1/|u_j|<=B,                               (3.3)
```

then `sigma` is an even probability on `K_H`,

```text
hat sigma(u_j)=0                         for all j,
sigma({0})=2^(-M),
r=1/(2^M-1).                                           (3.4)
```

#### Proof

The Fourier transform of `eta` contains, at node `u_j`, the factor

```text
[1+exp(i s_j u_j)]/2=0.                                (3.5)
```

Symmetrization takes the real part and preserves every zero.  All `s_j`
are positive.  Hence the empty subset is the unique subset sum equal to
zero, so its mass is exactly `2^-M`; every nonempty subset sum is at least
`T`.  The largest subset sum is `sum s_j`, bounded by (3.3).  Equations
(1.5)--(1.6) finish the proof.  QED

### Corollary 3.2 (actual half-integer shell budget)

Let `Y=N+1/2`, and take any subset of the integers in
`[Y exp(-w),Y exp(w)]`, in particular every prime power there.  Then

```text
sum_j 1/|log(n_j/Y)|<<_w Y log Y.                      (3.6)
```

Indeed, throughout the fixed shell

```text
|log(n/Y)|>>_w |n-Y|/Y,                                (3.7)
```

and the half-integer distances are `1/2,3/2,5/2,...`; comparison with the
harmonic series proves (3.6).  Since `M=O_w(Y)`, with

```text
T=Y^.01,             B=Y^(50/33),                      (3.8)
```

the left side of (3.3) is

```text
O_w(Y^1.01+Y log Y)=o(B).                              (3.9)
```

Thus (3.4) is a genuinely legal high-gap nuller.  Unlike the symmetric
factor-by-node product, it has no accidental low noncentral subset sums.
Its only failure is quantitative: `2^-M` is vastly below every power of
`Y`.

---

## 4. Grouping cannot be a small-block repair

The preceding construction suggests replacing one factor per node by one
factor per group.  There is an exact limit on that architecture.

### Lemma 4.1 (half-atom bound for every nonempty null factor)

If

```text
rho=p delta_0+(1-p)rho_1
```

is a probability and `hat rho(u)=0` at one nonzero node, then

```text
p<=1/2.                                                (4.1)
```

This is immediate from

```text
p=(1-p)|hat rho_1(u)|<=1-p.                            (4.2)
```

Equality holds only when `exp(itu)=-1` almost surely under `rho_1`.  If one
factor nulls two nodes with irrational ratio, equality is impossible:
simultaneous odd aliases would make their ratio rational.  This strictness
has no uniform finite-aperture margin; late Kronecker recurrence can approach
equality.

### Theorem 4.2 (group-product barrier)

Partition the nodes into `G` nonempty groups.  For each group let `rho_g` be
a one-sided probability on `{0} union [T,L_g]` which nulls every node of that
group.  Convolve all factors and symmetrize.  Then its central atom and depth
obey

```text
p=product_g p_g<=2^(-G),
r<=1/(2^G-1).                                          (4.3)
```

The support remains gapped and has upper edge at most `sum_g L_g`.

The proof is Lemma 4.1 plus the fact that nonnegative one-sided supports
cannot cancel back to zero.

For the promotion depth

```text
r_Y=Y^(-kappa+eta),       kappa=.0180303234,            (4.4)
```

(4.3) permits at most

```text
G<=log_2(1+1/r_Y)
  =[(kappa-eta)/log 2]log Y+O(1).                      (4.5)
```

Consequently one group has at least

```text
M/G>>M/log Y=Y^(1-o(1))/log Y                         (4.6)
```

nodes.  Every fixed-size, bounded-size, or polylogarithmic grouping remains
superpolynomially weak.  To do better, one factor must solve a macroscopic
simultaneous positive-null problem inside the same polynomial aperture.
That is not amplification; it is the original obstruction concentrated in
one block.

The one-sided hypothesis is intentional.  With two-sided factors, different
nonzero support choices can cancel to zero and artificially enlarge the
central atom.  Controlling those additive coincidences is another global
coupling and is not covered by (4.3).

---

## 5. Dense harmonic root grids do not cover generic phases

Let `theta_1,...,theta_M` be independent Haar phases and

```text
a_k(theta)=(cos(k theta_j))_(j<=M).                    (5.1)
```

### Theorem 5.1 (adaptive-support metric exclusion)

For every `D>=1` and `0<r<1`,

```text
P{there are K subset {1,...,D}, weights w_k>=0,
   sum w_k=1, and r'>=r with
   sum_(k in K)w_k a_k(theta)=-r' q_0}
 <=D exp(-M r^2/2).                                    (5.2)
```

#### Proof

Pair a feasible identity with `q_0`.  Some used harmonic must obey

```text
sum_(j<=M)cos(k theta_j)<=-r'M<=-rM.                   (5.3)
```

For each fixed nonzero integer `k`, the summands are independent, mean-zero,
and lie in `[-1,1]`.  Hoeffding gives `exp(-Mr^2/2)`; union over the `D`
individual harmonics proves (5.2).  Notice that there is no union over
supports: (5.3) has already compressed every adaptive support to one of the
`D` negative-peak events.  QED

At the audited scales

```text
M=Y^(1-o(1)),
r=Y^(-kappa+eta),
D=Y^O(1),                                               (5.4)
```

the logarithm of (5.2) is

```text
-Y^(1-2kappa+2eta-o(1)),
1-2kappa=.9639393532.                                  (5.5)
```

Thus increasing the top harmonic `D` polynomially, selecting the root cells
after seeing the phases, and selecting `K` adaptively cannot make the union
of positive chambers generically large.  This conclusion does not require a
universal upper bound on an individual chamber's persistence radius.

For the actual prime-log flow, (5.3) becomes the already isolated
sign-resolved prime large-value event.  Metric rarity cannot exclude one
arithmetically exceptional actual step.

---

## 6. Literature and exact boundary

The continuous interval tent and sinc-squared extremizers belong to the
classical positive-definite Turan problem; a primary modern treatment is
Kolountzakis--Revesz,
[*On a problem of Turan about positive definite functions*](https://arxiv.org/abs/math/0204086).
They prescribe a continuous spectrum, not a quadrature on the actual
prime-log nodes.

Prolate concentration, beginning with Slepian--Pollak,
[*Prolate Spheroidal Wave Functions, Fourier Analysis and Uncertainty -- I*](https://doi.org/10.1002/j.1538-7305.1961.tb03976.x),
optimizes `L2` time-frequency concentration.  It does not imply the
one-sided pointwise constraint in (2.1) after the spectrum is restricted to
the actual finite node set.

The probability estimate in Theorem 5.1 is the bounded-variable inequality
of Hoeffding,
[*Probability Inequalities for Sums of Bounded Random Variables*](https://doi.org/10.1080/01621459.1963.10500830).

The broader quantitative-Kronecker, logarithmic-form, Littlewood,
Turan--Nazarov, nonharmonic-frame, and actual-prime large-value audit is in
`ZETA23-QP-FINITE-APERTURE-QUANTITATIVE-TOOLS-REFEREE-2026-08-14.md`.
None of those primary results evaluates `A_H` for the actual growing node
set.

The exact disposition is therefore

```text
spectral-null / positive-antipode equivalence:       PROVED;
exact Delsarte reciprocal value (0.1):               PROVED;
gapped Bernoulli nuller inside legal aperture:       PROVED;
its retained depth 1/(2^M-1):                        EXPONENTIALLY SMALL;
bounded/polylog grouped convolution repair:          KILLED;
macroscopic grouped factor:                          ORIGINAL GATE;
polynomial high-D adaptive harmonic cover, metric:   KILLED;
actual-prime one-sided Delsarte value A_H:            OPEN;
full positive QP PROMOTE or KILL:                     OPEN;
full signed low/high QP:                              OPEN;
uniform zeta strip:                                   NOT PROVED.
```

The highest-value next theorem is now unambiguous: estimate `A_H` in (2.1)
for the actual nodes.  A promoter must upper-bound it at
`Y^(kappa_promote-eta)`; a positive-route killer must exhibit one admissible
polynomial with value at least `Y^c`, `c>kappa_promote`.  Neither small-block
grouping nor a continuum prolate extremizer changes this binary target.

---

## 7. Replay

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_spectral_null_grouping_gate.py
PYTHONPATH=src python3 \
  results/verify_zeta23_qp_spectral_null_grouping_gate.py
```

Current replay: `7 passed`; independent verifier: `PASS`.  The verifier also
solves a finite primal/dual fixture and checks `r_+=1/(A_H-1)` independently.
