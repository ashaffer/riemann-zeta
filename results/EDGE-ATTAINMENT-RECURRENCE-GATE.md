# Edge-attainment recurrence gate

Status: conditional recurrence theorem proved, attained-width clustered
countermodel rejected, non-attained-edge abstract countermodel proved, and
almost-all transfer audited; 2026-08-06.  This note does **not** prove a new
zero-free strip or the Riemann Hypothesis.

## 1. Verdict

The proposed implication

```text
one off-line zero
  => completed R71 energy is exponentially large on a positive-density
     set of logarithmic scales
```

splits at one exact quantifier.

1. If the supremal horizontal displacement `Delta` is attained by a zero,
   the implication is true for every fixed-order exact-head detector.  In
   fact the large-scale set has positive **right lower Banach density**.
2. The sparse clustered divisor from R5 does not defeat this theorem when
   all displaced nodes lie on the attained outer line.  Its edge trace is a
   nonzero absolutely convergent Bohr series, so its diagonal mean cannot be
   cancelled.
3. An arbitrary off-line zero does not imply that the edge is attained.
   Without attainment, a symmetric absolutely summable exponential series
   can cancel on intervals occupying asymptotically all of selected long
   initial segments while retaining a fixed off-line carrier.  Thus absolute
   convergence, zero symmetries, the exact energy abscissa, and every fixed
   Sobolev bound do not by themselves prove the desired density statement.
4. The abstract countermodel does not impose Riemann--von Mangoldt local
   counting or the exact zeta multiplier at every node.  A zeta-specific
   recurrence theorem in the non-attained case remains open.
5. Even under edge attainment, current almost-all arithmetic results do not
   finish the fixed-strip argument.  Their logarithmic or `o(1)` savings
   have energy exponent `1`, whereas a fixed strip needs an exponent strictly
   below `1` in the exact completed norm.

The fail-fast result is therefore neither a proof nor a total rejection.
Positive-density recurrence is now a theorem in the attained-edge case and
an explicitly false generic principle in the non-attained-edge case.  Any
continuation must use a specifically zeta/Riemann--von Mangoldt property of
the moving record carriers.

## 2. The conditional theorem

### Theorem 2.1 (attained-edge recurrence)

Let, on the positive half-line,

```text
G(R)=sum_j c_j exp((delta_j+i gamma_j)R)+r(R),            (2.1)
sum_j abs(c_j)<infinity,       delta_j<=Delta,            (2.2)
```

where equal pairs `(delta_j,gamma_j)` are grouped before their coefficient
is tested.  Assume

1. some grouped coefficient on `delta_j=Delta` is nonzero; and
2. the remainder satisfies

```text
sup_(R>=T) exp(-Delta R)abs(r(R)) ->0.                    (2.3)
```

Write

```text
b_gamma=sum_(j:delta_j=Delta,gamma_j=gamma)c_j,
P(R)=sum_gamma b_gamma exp(i gamma R),
S_1=sum_gamma abs(b_gamma),
S_2=sum_gamma abs(b_gamma)^2>0.                           (2.4)
```

For any fixed nonnegative, nonzero compactly supported weight `w`, put

```text
E_w(R)=integral w(u)abs(G(R+u))^2du,
K_w=integral w(u)exp(2Delta u)du.                        (2.5)
```

Then

```text
lower_Banach_density^+{
 R:E_w(R)>=(K_w S_2/4)exp(2Delta R)
}
 >= S_2/(2S_1^2-S_2)>0.                                 (2.6)
```

Consequently, for every `d<Delta`,

```text
lower_Banach_density^+{R:E_w(R)>=exp(2dR)}>0.            (2.7)
```

Here right lower Banach density means

```text
liminf_(T->infinity) inf_(A>=0)
 measure(S intersect [A,A+T])/T.                         (2.8)
```

#### Evidence and scope

This is an analytic theorem.  Its only imported input is the elementary
uniform-mean theory of absolutely convergent Bohr almost-periodic series.
For the exact triangular or fixed-order coboundary zeta detector, the
zero expansion is absolutely summable, a repeated zero contributes its
multiplicity to one grouped coefficient, and the off-axis multiplier is
nonzero.  The pole and archimedean remainder satisfies (2.3) when
`Delta>0`.

The theorem applies directly to a fixed-order detector with the exact
Type-I head.  It does not automatically apply to a growing-order schedule,
because `P`, `S_1/S_2`, and its equilibration length then vary with the
block.  It also does not apply to an evaluated approximate center unless its
Euler defect satisfies (2.3) at the selected carrier scale.

### Proof

Absolute summability and dominated convergence give, uniformly on every
tail `R>=T`,

```text
exp(-Delta R)G(R) -> P(R).                               (2.9)
```

Indeed, each term strictly left of the edge contains
`exp(-(Delta-delta_j)R)`, while the edge terms form `P` and (2.3) removes
the remainder.  It follows uniformly that

```text
exp(-2Delta R)E_w(R) ->
J_w(R):=integral w(u)exp(2Delta u)abs(P(R+u))^2du.       (2.10)
```

The function `J_w` is nonnegative and Bohr almost periodic.  Grouping equal
frequencies before Parseval gives its uniform mean and supremum bound

```text
M(J_w)=K_w S_2,
sup_R J_w(R)<=K_w S_1^2.                                 (2.11)
```

Bohr means converge uniformly in the origin of the averaging interval.  On
the superlevel set `J_w>=K_w S_2/2`, the elementary mean-versus-supremum
inequality therefore gives

```text
lower_Banach_density^+
 >=(K_w S_2-K_w S_2/2)/(K_w S_1^2-K_w S_2/2)
 =S_2/(2S_1^2-S_2).                                     (2.12)
```

Uniform convergence in (2.10) lowers the threshold from `K_w S_2/2` to
`K_w S_2/4` for all sufficiently large `R`, proving (2.6).  Since
`Delta-d>0`, the fixed factor `K_w S_2/4` eventually dominates
`exp(-2(Delta-d)R)`, proving (2.7).

The uniform-in-origin mean is essential for the Banach-density conclusion.
A Cesaro mean starting only at zero would prove ordinary lower density, not
the stronger statement in (2.6).

## 3. Transfer to regular completed blocks

For a continuously translated fixed-shape completed weight, Theorem 2.1 is
already the desired block statement.  For a regular family with a core on
which `psi_I>=c_0>0`, it transfers in either of two standard ways.

* If the cores have fixed width and their start points range continuously
  (or on a sufficiently fine bounded-gap mesh), every recurrence start whose
  fixed interval lies in a core gives the same positive-density family of
  large block energies.
* If the core lengths tend to infinity and every core lies at
  `R_I+o(R_I)`, right lower Banach density gives at least a fixed positive
  proportion of recurrence points in every sufficiently long core.  Hence
  the core energy is `exp((2Delta-o(1))R_I)`.

An adversarial sparse discrete schedule can miss a positive-measure set, and
a growing-`k` schedule changes the almost-periodic function itself.  Neither
case is silently covered by the theorem.

## 4. The clustered-divisor stress test

The R5 countermodel moves selected consecutive quantile nodes to symmetric
quartets at one fixed displacement `Delta`, preserving the counting
staircase to `O(1)`.  For the triangular detector

```text
H_ell(z)=4 sin(ell z/2)^2/(ell z^2),                     (4.1)
```

Riemann--von Mangoldt counting and `H_ell(z)=O((1+abs(z))^-2)` make the
coefficients absolutely summable.  Its completed trace splits exactly as

```text
B(R)=exp(Delta R)A(R)+C(R)+exp(-Delta R)D(R),            (4.2)
```

where `A` is a nonzero absolutely convergent Bohr series.  Therefore

```text
exp(-Delta R)B(R)->A(R)                                 (4.3)
```

uniformly.  If `M_carrier` is the squared coefficient mass of one fixed
quartet and `S=sum abs(a_gamma)`, then

```text
M(abs(A)^2)=sum abs(a_gamma)^2>=M_carrier,               (4.4)
```

and

```text
lower_density{abs(A)^2>=M_carrier/2}
 >=[M(abs(A)^2)-M_carrier/2]/[S^2-M_carrier/2]>0.        (4.5)
```

The same calculation after integration over a fixed block proves positive
density for the normalized completed block energy.  Thus clustering
ordinates does not defeat recurrence when the horizontal edge itself is
attained.

The finite D-rated probe
[`src/clustered_divisor_recurrence_probe.py`](../src/clustered_divisor_recurrence_probe.py)
constructs the quantile divisor, verifies its exact symmetries and counting
discrepancy, evaluates the upper/critical/lower decomposition, and compares
the analytic density floor with sampled densities.  Its default 80-node run
gives

```text
maximum counting discrepancy       1
analytic density lower bound        0.2333295...
sampled top-profile density         0.665167...
```

The sampled values illustrate the theorem; they are not evidence for zeta.

## 5. Why non-attainment is a real obstruction

### 5.1 Energy abscissa and Sobolev control are insufficient

Fix `0<delta<1/2`, let `R_n=2^(2^n)`, and choose a nonzero smooth bump
`phi` supported in `(-1/4,1/4)` with `norm(phi)_2=1`.  Put

```text
f(R)=sum_n exp(delta R_n)phi(R-R_n).                     (5.1)
```

The supports are disjoint.  For every fixed derivative order `q`,

```text
abs(f^(q)(R))<=C_q exp(delta R),                         (5.2)
```

and

```text
limsup_(T->infinity)
 log(1+integral_0^T abs(f(R))^2dR)/(2T)=delta.           (5.3)
```

Moreover, the weighted `L2` abscissa is exactly `delta`.  Nevertheless, for
every fixed block length `L` and every `d<delta`, the large-block set is
contained in

```text
union_n [R_n-L-1/4,R_n+1/4],                            (5.4)
```

whose measure below `T` is `O_L(log log T)`.  Its lower density and lower
Banach density are zero.  This kills any recurrence proof using only the
R71 energy-abscissa theorem plus fixed Sobolev estimates.  It is not a
zero-side exponential-series model.

### 5.2 A symmetric `l1` exponential-series countermodel

The failure persists inside a broad zero-expansion class.  Fix

```text
0<d<delta_0<Delta<1/2                                  (5.5)
```

and a block length `L`.  There is a real-even function

```text
G(R)=sum_j c_j exp((delta_j+i gamma_j)R),
sum_j abs(c_j)<infinity,                                 (5.6)
```

with full quartet symmetry, one untouched carrier at `delta_0`, distinct
nonzero frequencies, and displacements `delta_j` increasing to but never
attaining `Delta`, for which

```text
lower_density{
 R:integral_R^(R+L)abs(G(u))^2du>=exp(2dR)
}=0.                                                     (5.7)
```

Here is the construction.  Begin with

```text
P_0(R)=2 cosh(delta_0 R)cos(gamma_0 R).                  (5.8)
```

Choose `delta_k` increasing to `Delta`.  Inductively, after constructing the
finite real-even quartet polynomial `P_(k-1)`, take a very large `A_k`, put
`a_k=A_k/k>A_(k-1)+2L`, and choose a real-even cutoff `chi_k` supported on
the two mirrored intervals

```text
[-A_k,-a_k] union [a_k,A_k],                            (5.9)
```

equal to one away from their endpoints.  Define

```text
h_k(R)=-chi_k(R)P_(k-1)(R)/(2cosh(delta_k R)).           (5.10)
```

If `delta_(k-1)` is the largest previous displacement, then

```text
norm(h_k)_(W^(2,1))
 <=C_k exp(-(delta_k-delta_(k-1))a_k).                  (5.11)
```

Taking `A_k` large makes this arbitrarily small.  Fourier inversion and
symmetric finite quadrature give a real-even trigonometric polynomial

```text
q_k(R)=sum_m b_(k,m)cos(gamma_(k,m)R)                   (5.12)
```

whose coefficient `l1` norm is arbitrarily small and which approximates
`h_k` on `[-A_k,A_k]` to any prescribed accuracy.  The nodes can avoid zero
and every frequency used earlier.  Set

```text
Q_k(R)=2cosh(delta_k R)q_k(R),
P_k=P_(k-1)+Q_k.                                        (5.13)
```

Each cosine in (5.13) contributes four equal real coefficients at
`+/-delta_k+/-i gamma_(k,m)`.  Choose the approximation error so that

```text
abs(P_k(R))<2^-k on [a_k+1,A_k-1]                       (5.14)
```

and choose every future layer to be below `2^-l` on all earlier compact
intervals.  The coefficient budgets can be made summable.  Hence

```text
G=P_0+sum_(k>=1)Q_k                                     (5.15)
```

converges absolutely on compact sets and is smaller than `2^(1-k)` on the
interior of the `k`-th interval.  Since `a_k/A_k=1/k`, those intervals
occupy proportion `1-o(1)` of `[0,A_k]`.  Fixed-length large-energy starts
therefore have lower density zero, proving (5.7).

The series still has exact upper growth exponent `Delta`: absolute
summability gives the upper bound, while the unchanged nonzero carrier on
every line `delta_k` gives the matching limsup after taking `k->infinity`.
Thus the construction separates growth exponent from recurrence density,
not merely nontriviality from recurrence.

This countermodel deliberately does **not** impose Riemann--von Mangoldt
local frequency counting, nor does it require every coefficient to equal
the zeta detector's prescribed multiplier at its node.  It proves logical
insufficiency of symmetry, `l1` convergence, and an unattained spectral edge;
it does not prove that zeta realizes the bad case.

## 6. Almost-all arithmetic transfer

For the current primary-source theorem statements and their exact R71
normalization, use
[`publication/IMPORTED-ANALYTIC-BASELINE.md`](../publication/IMPORTED-ANALYTIC-BASELINE.md).

Under edge attainment, an arithmetic theorem outside an exceptional set of
vanishing logarithmic density would be enough in principle.  To prove
`Delta<=a`, the required matching statement is

```text
E_I<=exp((2a+o(1))R_I)                                  (6.1)
```

for logarithmic-density one of the exact completed blocks.  If `Delta>a`
were attained, Theorem 2.1 would put `E_I>=exp(2dR_I)` on a set of fixed
positive lower density for any `a<d<Delta`, a contradiction.

A theorem with exceptional `dx`-measure `o(X)` uniformly in every dyadic
shell `[X,2X]` also gives exceptional `dR=dx/x` measure `o(1)` there, so the
measure conversion is not the main obstruction.  Current results miss the
gate on the object and exponent:

| Input | What it supplies | Why it does not give (6.1) |
|---|---|---|
| Matomaki--Radziwill--Tao, long shift ranges | almost-all additive shifts with arbitrary log-power saving | averages the shift variable, not the complete scale block; no fixed power |
| Matomaki--Radziwill--Shao--Tao--Teravainen, almost-all intervals | `H log^(-A)X` control for `Lambda-Lambda^sharp` when `H>=X^(1/3+epsilon)` | retains a structured approximant and has exponent `H^(1+o(1))`; after critical normalization the energy exponent is still `1` |
| Generic Dirichlet-polynomial large values and zero density | bounds the number of separated exceptional values | does not retain every Vaughan cofactor and center term, and does not exclude the required completed carrier |

The relevant primary sources are
[Matomaki--Radziwill--Tao](https://arxiv.org/abs/1707.01315),
[Matomaki--Radziwill--Shao--Tao--Teravainen](https://arxiv.org/abs/2411.05770),
and the reverse zero-density/large-value comparison of
[Matomaki--Teravainen](https://arxiv.org/abs/2403.13157).

A logarithmic saving has the form

```text
exp(R)/R^A=exp((1-o(1))R),                               (6.2)
```

not `exp((1-2eta)R)` for a fixed `eta>0`.  Positive-density recurrence would
repair the exceptional-set quantifier under edge attainment, but it would
not manufacture the missing fixed exponent or the exact completed norm.

## 7. Exact next gate

There are now only two honest ways to continue this recurrence branch.

1. Prove a zeta-specific moving-edge theorem: Riemann--von Mangoldt local
   counting together with the prescribed triangular/coboundary coefficient
   must prevent the superoscillatory cancellation in Section 5.2.  The
   theorem must cover a non-attained supremum and quantify its density
   uniformly over record carriers.
2. Prove a fixed-power almost-all estimate in the **complete** R71 energy or
   moment norm.  Logarithmic savings for separated factors are insufficient.

The first is the genuinely new recurrence problem.  The second is the
fixed-strip arithmetic theorem in density-one form.  Neither is presently
proved.

## 8. Reproduction and nonclaims

Run the focused diagnostic and tests with

```text
PYTHONPATH=src python3 src/clustered_divisor_recurrence_probe.py
PYTHONPATH=src python3 -m pytest -q \
  src/test_clustered_divisor_recurrence_probe.py
```

The analytic recurrence theorem and countermodels are not formalized in
Lean.  The Python probe checks only the finite clustered model.  This report
does not prove edge attainment for zeta, positive-density recurrence in the
non-attained case, a fixed-power almost-all theorem, a zero-free strip, or
RH.
