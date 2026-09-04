# Core periodic masks and the missing grouped lower edge

Status: exact periodic-mask calculation and hostile lower-bound audit,
2026-08-11.  This note does not prove a uniform carrier lower bound and does
not prove a zero-free strip.

**Fixed-period update.**  The signed-isolation gap identified below is now
closed for every nontrivial mask of fixed minimal period at least three,
including the pure `k=7` mask.  Coefficient residue classes modulo the period
diagonalize every alias simultaneously; endpoint-jet interlacing and a trace
bound prevent count-bounded on-line fillers from screening the resulting
negative subspace.  See
`ZETA23-FIXED-PERIODIC-MASK-SIGNED-EDGE-THEOREM-2026-08-11.md`.  The warnings
below remain applicable to growing periods and aperiodic ordinates.

## 1. Verdict

The core sublattice construction has two different consequences which must
be kept separate.

1. After imposing the current zero-count and zero-density information,
   including the simple critical-line proportion

   ```text
   C_0=3/2-(1/sqrt(2))*cot(1/sqrt(2))
      =0.6725007036...,
   ```

   the first admissible pure sharp-grid sublattice is `k=7`.  Its exact
   Poisson bound gives

   ```text
   0<K <= (26/7+o(1))*X^(6*alpha/7).
   ```

   Thus the counts and line-density theorem do not imply
   `K>=X^(alpha-o(1))/L`.

2. A periodic positive mask cannot hide all of its high Poisson aliases.
   If it occupies `r` of `M` sharp-grid residue classes, an elementary
   Newton--power-sum argument produces a nonzero alias at normalized time at
   least `1-r/M`.  In the natural notation in which the off-line *point*
   fraction is `f=2r/M`, this is the candidate exponent

   ```text
   alpha*(1-f/2).                                    (1.1)
   ```

   The pure `k=7` mask attains (1.1), with `f=2/7`.  The fixed-period
   companion theorem now turns this alias into a signed edge of the same
   power.

The alias statement by itself is not a signed lower bound.  The companion
fixed-period theorem supplies the missing step by restricting coefficients
to a residue class modulo the period: all aliases then diagonalize
simultaneously, endpoint jets leave a positive-dimensional negative
subspace, and a trace bound defeats every count-bounded on-line filler.  For
arbitrary, nonperiodic zero ordinates one still needs a quantitative
power-sum/large-sieve replacement for this finite Fourier calculation.  No
grouped Paley--Wiener theorem inspected in this project supplies that
aperiodic step.

Accordingly, the periodic calculation identifies the following candidate
core target at the count-and-density level:

```text
K >= X^(alpha*(1-f/2)-o(1))/L,                        (1.2)
```

or any explicit weaker fixed-power version of it.  The calculation below
first identifies the location of the unavoidable alias; the companion
theorem proves the corresponding carrier edge for every fixed minimal
period at least three.  Formula (1.2) is not asserted from the full Zeta23
trace/Frobenius moment input: the `k=7` artificial configuration fails that
stronger moment ledger.

## 2. Audit of the simple-line constraint

For one reflected pair every `k` sharp coordinate spacings, the pair point
density is

```text
L/(k*pi),
```

whereas the total zeta-zero density is

```text
log(t/(2*pi))/(2*pi)=L/(2*pi)*(1+o(1))
```

on the dyadic carrier.  Hence the off-line point fraction is `2/k+o(1)`
and the simple on-line fraction in the construction is `1-2/k+o(1)`.
Since

```text
2/3 < C_0 < 5/7,
```

`k=6` is inadmissible and `k=7` is admissible.  Every atom in the
construction is simple and every reflected member is a distinct complex
location, so the separate distinct-zero lower density creates no further
restriction.  The collars have width `o(T)` and do not change these
proportions.

Applying Lemma 3.1 of the core-sublattice report with `k=7` gives

```text
||H_(7,infinity)|| <= (26/7)*X^(6*alpha/7).           (2.1)
```

Endpoint jets make the omitted part outside `J_D` equal to `o(1)` in the
same coefficient norm.  On-line fillers are positive semidefinite, while
Cauchy--Vandermonde surjectivity keeps at least one negative direction.
This proves the displayed upper bound in Section 1.

The quantile filler construction proves distinctness after a generic
offset, but does not by itself prove a uniform lower separation for the
union of the pair and on-line ordinates.  None is needed for (2.1).  Thus
the safe description is `collision-free`, rather than uniformly separated,
unless one replaces the quantiles by an explicitly balanced selection of
unused sharp-grid cells.

## 3. Exact formula for a periodic sharp-grid mask

Put `h=2*pi/L`.  Fix an integer `M>=2` and a nonempty set

```text
B subset {0,...,M-1},       #B=r.
```

At every ordinate

```text
gamma_(b,j)=tau_c+beta+(b+j*M)*h,
b in B, j in Z,
```

place a depth-`alpha` reflected pair.  For a real coefficient vector `c`,
write

```text
F_(b,j)=F_c(gamma_(b,j)-i*alpha),
P=L/M,
A_q=sum_(b in B) exp(2*pi*i*b*q/M),
I_q(c)=integral p_c(t)*p_c(q*P-t)dt,
```

where the integral is restricted automatically to the overlap of the two
sharp support intervals.  Bilinear Poisson summation on each residue class
gives the exact identity

```text
sum_(b in B) sum_(j in Z) F_(b,j)^2
 = P*sum_(|q|<=M-1)
       A_q*exp((alpha+i*beta)*q*P)*I_q(c).             (3.1)
```

Consequently the normalized signed pair form is

```text
Q_B(c)
 = (2/(M*L))*Re sum_(|q|<=M-1)
       A_q*exp((alpha+i*beta)*q*P)*I_q(c),             (3.2)
```

and `|I_q(c)|<=L*||c||_2^2`.  Formula (3.1) is just the
one-coset sublattice identity with the residue-class phases retained.  It
remains valid after restricting `c` to `V_m`.

## 4. A high alias forced by positivity

### Lemma 4.1 (finite positive-mask power sum)

With the notation above, there is an integer `1<=j<=r` such that

```text
|A_j|>=1.                                             (4.1)
```

Since the mask lies on the `M`th roots of unity,

```text
A_(M-j)=conj(A_j).                                    (4.2)
```

Thus (3.1) contains a coefficient of magnitude at least one at an alias
`q=M-j` satisfying

```text
q/M >= 1-r/M.                                        (4.3)
```

#### Proof

Let `z_b=exp(2*pi*i*b/M)` and let `e_k` be the elementary symmetric
polynomial of degree `k` in the `r` numbers `z_b`.  Their power sums are
`A_j`.  Newton's generating identity is

```text
sum_(k=0)^r e_k*t^k
 = exp(sum_(j>=1) (-1)^(j-1)*A_j*t^j/j)
```

through degree `r`.  If `|A_j|<1` for every `1<=j<=r`, coefficientwise
majorization would give

```text
|e_r|
 < [t^r] exp(sum_(j>=1) t^j/j)
 = [t^r] (1-t)^(-1)
 = 1.
```

But `|e_r|=|product_(b in B)z_b|=1`, a contradiction.  This proves
(4.1).  Equation (4.2) follows from `z_b^M=1`, and (4.3) follows from
`j<=r`.  QED

### Corollary 4.2 (periodic-mask exponent ledger)

Let

```text
f=2r/M
```

be the off-line point fraction relative to one point per sharp grid cell.
Every periodic positive mask has in its exact bilinear Poisson expansion an
alias whose hyperbolic weight is at least

```text
exp(alpha*(1-f/2)*L).                                 (4.4)
```

Up to the harmless factor `1/M`, this is the power in (1.1).  For the pure
`k`-sublattice, `M=k`, `r=1`, and its largest alias is exactly `q=k-1`, so
(4.4) is sharp within that family.

If the simple-line input gives `f<=1-C_0+o(1)`, (4.4) has exponent at least

```text
alpha*(1+C_0)/2 = 0.8362503518...*alpha.              (4.5)
```

The legal pure `k=7` construction uses the smaller fraction `f=2/7` and
has exponent `6*alpha/7=0.857142...*alpha`.

Corollary 4.2 is deliberately phrased as an alias statement.  The companion
fixed-period theorem proves the implication

```text
large coefficient in (3.1)
  => lambda_min(H_C|V_m) <= -X^(q*alpha/M-o(1))/L     (4.6)
```

for every nontrivial fixed mask of minimal period at least three.  It remains
open in the growing-period and aperiodic regimes.

## 5. What remains beyond the fixed-period proof

The following were the three gaps in the alias-only calculation.  The first
two are now closed for fixed periods by simultaneous residue-class
diagonalization, but they reappear when the period grows; the third is the
main aperiodic obstruction.

1. **Signed isolation.**  An alias term is a reflected-overlap bilinear
   form.  A negative test vector has to localize near its fixed point
   `t=qP/2`, choose the unfavorable phase, and make all other overlap terms
   smaller.  A triangle inequality proves an upper norm, as in the
   sublattice counterconfiguration, but cannot prove this negative lower
   edge.

2. **Endpoint-jet accessibility.**  The test vector must lie in `V_m`.
   When the relevant overlap approaches an endpoint on the scale `m/T`, the
   jets can suppress it exponentially; this is exactly the collar
   obstruction.  For a fixed periodic mask such as `k=7`, the `q=6`
   overlap is a fixed fraction of the support and is safely accessible, but
   a uniform quantitative concentration lemma for growing periods has not
   been established.

3. **Aperiodic ordinates and collisions.**  Riemann--von Mangoldt counting
   does not put pair ordinates on the sharp grid or make their type pattern
   periodic.  Collision grouping repairs qualitative inertia, but the
   standard divided-difference interpolation theorems either give no
   explicit constant in this varying regime or impose an additional
   generating-function/Muckenhoupt condition.  They do not turn the
   positive-mask power-sum argument into the regularized signed Schur bound

   ```text
   ||Y_C*(X_C^T*X_C+K*I)^(-1/2)||_op >= 1.
   ```

In particular, a density gap for the full direct-node set cannot by itself
distinguish the positive on-line rows from the hyperbolic rows.  The `k=7`
configuration is already collision-free and shows that this distinction
costs a fixed carrier power.

## 6. The next aperiodic theorem

A useful next count-and-density lemma beyond fixed periods would be a
**signed Turan--concentration theorem**.
In one possible formulation, let `f_T` be the off-line point fraction in the
carrier and assume `f_T<=1-C_0+o(1)`.  For a distinguished core pair of
depth `alpha`, prove uniformly through collision strata that

```text
-lambda_min(H_C|V_m)
 >= X^(alpha*(1-f_T/2)-o(1))/L.                       (6.1)
```

A weaker fixed exponent in place of `1-f_T/2` would already be genuine
progress.  The proof would have to combine:

```text
positive power sums / a large-sieve substitute for irregular ordinates;
an endpoint-jet packet localized on the selected reflected overlap;
regularized confluent grouping below the trial scale K;
and a Bessel bound for the on-line positive rows.
```

Neither the Riemann--von Mangoldt discrepancy nor the known simple-line
proportion currently supplies that theorem.  Conversely, this audit found
no count-and-density-compatible periodic sharp-grid mask that screens beyond
the exponent predicted by (6.1).  More irregular masks, growing periods, and
depth variation remain the hostile cases.  The full trace/Frobenius moment
constraints are a separate, stronger input and may exclude these artificial
masks; they are not encoded in (6.1).

Even (6.1) would close only the carrier side.  A zero-free strip would still
need the prime-side lower edge to be `o(K)` at this reduced, matched scale.
