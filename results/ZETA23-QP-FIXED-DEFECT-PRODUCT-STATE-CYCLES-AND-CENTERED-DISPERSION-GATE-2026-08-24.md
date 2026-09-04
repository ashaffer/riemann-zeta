# QP fixed-defect graph: product-state cycles and the centered dispersion gate

**Date:** 2026-08-24  
**Binary verdict:** the fixed-defect graph has an exact two-point
product-state fold and its complete `4`-/`2k`-cycle identities are proved
below.  They do **not** prove the desired centered `sqrt(D)` norm.  No
faithful asymptotic prime-power counterexample was found either.

The useful structural conclusion is that `sqrt(D)` is the sharp **raw
folded-graph** scale allowed by the present structural information.  A
one-sided star of `d` abstract product blocks already has norm

```text
sqrt(2(d+1)),                                           (0.1)
```

while a dangerous two-sided core is exactly a centered shifted-semiprime
dispersion problem.  On collision-free equality-pattern strata the cycle
identities pin only one final shell label; reused-label strata need not do
so.  In either case they do not supply the independent savings needed by a
high-trace proof.
Positive upper-bound sieve also keeps the principal cycle population which
centering is meant to remove.

Thus the surviving input is a mask-sensitive fixed-determinant BDH/expander
estimate, not another uncentered cycle count.

---

## 1. Exact fixed-ray kernel

Put

```text
Q=q^3,       rho(a,b,c)=8abc-Q,       |rho|<=H<<qD.      (1.1)
```

Let `E` be the retained actual prime-power triples, with weights
`kappa(a,b,c)`.  For `h!=0`, define

```text
(K_h)_(c',c)
 =sum_(b,a,a': ac-a'c'=h)
    kappa(a,b,c) conjugate(kappa(a',b,c')),              (1.2)
```

with both original product windows retained.  Then

```text
K_(-h)=K_h^*.                                            (1.3)
```

For one carrier and one product state put

```text
u_(b,n)(c)=sum_(a: ac=n) conjugate(kappa(a,b,c)).        (1.4)
```

Multiplicative Sidonicity of the narrow prime-power shell implies

```text
#supp u_(b,n)<=2.                                        (1.5)
```

The two entries, when present, are just the two orientations of the unique
unordered factor pair of `n`.  Directly regrouping (1.2) proves the exact
fold

```text
K_h=sum_(b,n) u_(b,n-h) u_(b,n)^*.                      (1.6)
```

Only states for which both vectors are physical are included.  Hence the
unfolded map

```text
(b,n) -> (b,n-h)                                        (1.7)
```

is a partial matching.  All difficulty comes from folding its two-point
factor vectors back to the colour coordinate.

This also explains the unavoidable internal rectangle.  If

```text
n=a*c,                  n-h=a'*c',                      (1.8)
```

with four distinct shell nodes, the one state shift contributes the rank-one
`2 by 2` block between `{a,c}` and `{a',c'}`.  This internal orientation
rectangle is not a reduced cycle.

For fixed `(c,c',h)`, all integer solutions of

```text
c*a-c'*a'=h                                             (1.9)
```

differ by `(c',c)`.  The shell diameter is smaller than both step sizes, so
there is at most one shell lift.  The remaining interval for `b` has length
`O(D/q)<1`.  Thus every fixed-ray matrix entry has multiplicity at most one
in the all-distinct actual-prime sector.  In particular two distinct product
blocks cannot share both a source factor and a target factor.

### Tangent-peel qualification

The existing tangent peel assigns pair incidences, not necessarily original
`T` edges.  A post-peel mask may therefore cut through one rank-one block in
(1.6).  Formula (1.6) applies before that cut; all identities below still
apply term by term afterward, but the regular remainder must not silently be
refactorized as a new physical carrier matrix.

---

## 2. Exact `2k` trace-cycle identity

Write

```text
u_s=u_(b,n),       v_s=u_(b,n-h),
K_h=sum_s v_s u_s^*.                                    (2.1)
```

Expansion gives

```text
tr((K_h K_h^*)^k)
 =sum_(s_i,t_i)
   product_i <u_(s_i),u_(t_i)>
             <v_(t_i),v_(s_(i+1))>,                    (2.2)
```

where `s_(k+1)=s_1`.  Expand each inner product into its shared-factor
monomials.  For a nonzero reduced factor-level term, write

```text
s_i=(b_i,n_i),              t_i=(d_i,m_i).              (2.3)
```

Choose the shared source and target factors `x_i,y_i`.  There are shell
labels `alpha_i,A_i,B_i,beta_(i+1)` such that

```text
n_i       =x_i alpha_i,       m_i       =x_i A_i,
m_i-h     =y_i B_i,           n_(i+1)-h =y_i beta_(i+1). (2.4)
```

### Theorem 2.1 (additive closure)

Every reduced factor-level monomial in (2.2) satisfies exactly

```text
sum_i [x_i(alpha_i-A_i)+y_i(B_i-beta_(i+1))]=0.          (2.5)
```

**Proof.**  The summand is

```text
(n_i-m_i)+(m_i-n_(i+1)),                                (2.6)
```

and the sum telescopes. `square`

### Theorem 2.2 (multiplicative closure)

Every reduced factor-level monomial in (2.2) also satisfies exactly

```text
 product_i(alpha_i B_i)          product_i n_i(m_i-h)
-------------------------  =  ---------------------------
 product_i(A_i beta_i)           product_i m_i(n_i-h)

                            h(m_i-n_i)
 =product_i (1+ --------------------------------).       (2.7)
                         m_i(n_i-h)
```

**Proof.**  Divide the two equalities in each column of (2.4), multiply in
`i`, and cyclically relabel the `beta` factors.  The last equality follows
from

```text
n_i(m_i-h)-m_i(n_i-h)=h(m_i-n_i).                       (2.8)
```

` square`

The carrier and residual dependence remains completely explicit.  If

```text
8b_i n_i=Q+r_i,              8d_i m_i=Q+s_i,             (2.9)
```

then the `i`th factor on the right of (2.7) is

```text
(Q+r_i)(Q+s_i-8d_i h)
-----------------------------.                           (2.10)
(Q+s_i)(Q+r_i-8b_i h)
```

No common carrier or endpoint mask has been completed away.

### Corollary 2.3 (near label-product identity)

For fixed `k`, all products being at the project scale,

```text
|product_i(alpha_i B_i)-product_i(A_i beta_i)|
 <<_k |h| q^(2k-4) sum_i |m_i-n_i|
 <<_k |h| q^(2k-2).                                  (2.11)
```

If every paired carrier difference `|b_i-d_i|` is at most `L`, then

```text
|m_i-n_i|<<qL+D                                       (2.12)
```

and (2.11) sharpens to

```text
<<_k |h|(L q^(2k-3)+D q^(2k-4)).                     (2.13)
```

For `k=2`, writing the four shared factors explicitly gives

```text
x_1(alpha_1-A_1)+y_1(B_1-beta_2)
+x_2(alpha_2-A_2)+y_2(B_2-beta_1)=0,                  (2.14)

 alpha_1 alpha_2 B_1 B_2
-------------------------
 A_1 A_2 beta_1 beta_2

 n_1 n_2 (m_1-h)(m_2-h)
=---------------------------.                         (2.15)
 m_1 m_2 (n_1-h)(n_2-h)
```

These are the exact fixed-defect four-cycle identities requested.

---

## 3. Why high trace does not close

The global version of (2.11) gives an interval of length

```text
O_k(|h| q^(2k-2))                                      (3.1)
```

for one product of `2k` shell labels.  On a collision-free equality-pattern
stratum in which a chosen shell label occurs exactly once on one side and
does not recur on the other, freezing the remaining labels leaves derivative
`asymp q^(2k-1)`.  That chosen label then lies in an interval of length

```text
O_k(|h|/q)<1.                                          (3.2)
```

Thus the cycle identity pins one final label only on these collision-free
strata.  Reused-label strata may make the product identity partly or wholly
tautological and must be handled by the repeated/permutation analysis.  Even
on the collision-free strata, a `2k`-trace proof of `sqrt(D)` needs roughly
one independent `D`-saving per pair of nonbacktracking steps.  Pinning only
the closing label leaves the same cross-cell branching which was present
before the trace was opened.

There is a second, more fundamental issue.  At the heuristic prime density,
one fixed source colour has

```text
about D/(log q)^2                                      (3.3)
```

physical `(a,b)` states, and the shifted value `ac-h` has two shell-prime
factors with density about `(log q)^(-2)`.  Hence a typical fixed-ray degree
is expected on the scale

```text
d_h about D/(log q)^4.                                (3.4)
```

This is polynomial in `D`, not subpower.  A positive high-trace or
upper-bound-sieve count therefore contains a large principal cycle
population.  The desired assertion is about its **centered fluctuation**.
Taking absolute values before the principal/tangent subtraction discards the
only possible saving.

The exact square-function target is of the form

```text
||P_C (K_h-Pi_h) P_C||_(2->2)^2
  <<D q^o(1),                                          (FD-BDH)
```

where `Pi_h` contains the certified constant/degree/tangent channels and is
defined with the same physical mask.  Expanding the off-diagonal of
`K_h^*K_h` gives two fixed-defect equations

```text
a_1 c_1-a'_1 c'=h,
a_2 c_2-a'_2 c'=h,                                    (3.5)
```

and hence

```text
a_1 c_1-a_2 c_2=c'(a'_1-a'_2),                        (3.6)
```

together with the two independent rounded common-carrier conditions.  A
positive sieve bounds (3.6), but does not subtract its degree main term.
Character or Poisson completion produces the same moving reciprocal
sampling.  An entrywise complete Kloosterman bound lives at `q^(1/2)`, while
the requested norm scale is

```text
sqrt(D)=q^(8/33+o(1));                                 (3.7)
```

the carrier sparsity must therefore remain inside an averaged dispersion
argument.  This is precisely the selected reciprocal gate, now with `h`
frozen; freezing `h` does not make the mask separable.

---

## 4. The raw star face is exactly sharp

Take `d` product blocks with one common source factor, one private second
source factor per block, and two private target factors per block.  In the
corresponding bases the folded matrix is

```text
K=[ 1 1 0 ... 0 ]
  [ 1 1 0 ... 0 ]
  [ 1 0 1 ... 0 ]
  [ 1 0 1 ... 0 ]
  [       ...     ].                                  (4.1)
```

Direct diagonalization gives

```text
||K||^2=2(d+1).                                       (4.2)
```

If source and target vertices are disjoint in the common colour universe,
the numerical radius of the square embedding is `||K||/2`.  Orthogonality
to the global constant can be enforced by spreading the compensating mass
over unused colours; when the universe has `N>>d`, its squared norm cost is
`O(d/N)`.  Thus neither mean zero nor absence of reduced cycles can improve
the natural `sqrt(d)` star scale.

This is an algebraic obstruction to a `q^o(1)` theorem for the raw folded
block class, but not an actual-prime or post-tangent counterexample.
Realizing polynomially many blocks simultaneously requires all four shell
factors and every isolated rounded carrier to be prime powers.  No such
asymptotic construction is known.  Nor has it been proved that this star
survives the data-dependent principal/degree/tangent projection `Pi_h` in
`(FD-BDH)`.

A norm larger than `sqrt(D)q^o(1)` would instead require a two-sided core.
The reduced alternating cycles in Section 2 are exactly the witnesses of
such a core.  The missing statement is that their centered, mask-weighted
population has square-root size.

---

## 5. Literal finite data

The exact prime-power matrix

```text
T_(b,c)=sum_a 1_(|8abc-q^3|<=qD),
D=floor(q^(16/33)),                                    (5.1)
```

was grouped by `(b,n)` and then by fixed nonzero `h`.  A reduced cycle means
an alternating cycle between **different** product blocks; the internal
orientation `2 by 2` rectangle is removed.

| `q` | `D` | fixed rays | blocks | max blocks/ray | max colour degree | max block component | reduced-cycle rays | max `||K_h||` |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 25,013 | 135 | 2 | 2 | 1 | 2 | 1 | 0 | `2` |
| 50,021 | 189 | 14 | 14 | 1 | 2 | 1 | 0 | `2` |
| 100,003 | 265 | 52 | 96 | 6 | 4 | 2 | 0 | `sqrt(6)` |
| 200,003 | 371 | 110 | 184 | 6 | 2 | 1 | 0 | `2` |
| 500,009 | 579 | 222 | 554 | 8 | 4 | 2 | 0 | `sqrt(6)` |
| 1,000,003 | 811 | 372 | 1,890 | 19 | 4 | 2 | 0 | `sqrt(6)` |

This is strong finite sparsity, but it is not asymptotic evidence for
bounded degree: the density ledger (3.3)--(3.4) predicts that fixed-ray
degrees eventually grow polynomially.  The data support the `sqrt(D)`
centered target and provide no counterexample to it.

For comparison, the literal **integer** shell at `q=1013` already has
reduced alternating cycles.  The executable certificate extracts one and
checks (2.5) and (2.7) with exact integer arithmetic.  Thus the cycle
identities are not contradiction identities even before primality is
imposed.

There is also a literal **all-prime** warning if only the finite cutoff is
widened.  At

```text
q=100003,          H=q*20000,          h=4242,           (5.2)
```

the following four product blocks form a reduced cycle:

```text
b=42349:  48989*60257  -> 52937*55763,
b=47417:  43753*60257  -> 44701*58979,
b=50131:  44059*56599  -> 42281*58979,
b=49177:  44059*57697  -> 45587*55763.                  (5.3)
```

Every displayed factor and carrier is prime, every arrow subtracts `4242`,
and all eight products obey the two literal windows in (5.2).  The exact
cycle certificate verifies (2.5) and (2.7).  This is **not** an
active-aperture counterexample: `20000` is far larger than
`floor(q^(16/33))=265`.  It does prove that actual primality and the common
carrier mask do not make a reduced fixed-ray cycle algebraically impossible;
the active theorem must use quantitative sparsity/dispersion.

---

## 6. Consequence for the global sharp bound

Even a proof of `(FD-BDH)` for every `h` would not by itself allow absolute
summation over `O(D)` rays: individual norm `sqrt(D)` gives raw sum
`D^(3/2)`, losing `sqrt(D)` against the desired Gram norm `D` (or `D` after
squaring that norm comparison).  The sharp global
argument needs either

1. a vector-valued square function in `h`, with the tangent/principal modes
   removed coherently; or
2. an inverse theorem showing that any coherent alignment of many fixed-ray
   fluctuations is one of the already controlled tangent/product charts.

The present work supplies the exact state space and all cycle constraints
for such a theorem, but not the required dispersion estimate.

```text
fixed-defect product-state fold (1.6):              PROVED;
two-point prime factor support:                     PROVED;
fixed-entry uniqueness:                            PROVED;
exact 4-/2k-cycle identities:                      PROVED;
one-final-label pinning, collision-free strata:    PROVED;
sqrt(D) raw-star scale in the folded graph class:  PROVED;
faithful actual-prime polynomial star/core:         NOT FOUND;
centered fixed-ray sqrt(D) theorem:                 OPEN;
vector-valued aggregation over h:                  OPEN;
sharp four-cycle theorem from this route:          NOT PROVED.
```

Executable certificates:

- `src/qp_fixed_defect_graph_cycles.py`;
- `src/test_qp_fixed_defect_graph_cycles.py`.
