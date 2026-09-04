# QP four-cycle: upstream positivity and residual-block parity audit

**Date:** 2026-08-29

## Verdict

For the positive hard QP kernel and a theorem quantified over every complex
coefficient vector, the positive all-plus fourth trace is **losslessly
equivalent** to the uniform four-cycle/Schatten-four estimate.  It is not a
stronger endpoint: nonnegative coefficient vectors are already among the
vectors quantified by the desired theorem.

The earliest genuinely lossy fork lies one level higher.  If the ultimate
target is only an operator-norm estimate, replacing it by a Schatten-four
trace bound is sufficient but not necessary.  If the target under discussion
is specifically the sharp four-cycle bound, the first unjustified
strengthening came later: replacing the direct first multiplicity
`m(C)` by the factorial multiplicity `m(C)(m(C)-1)` and calling the latter
the exact endpoint.

There is also a rigorous narrower reduction.  After the proved positive
repeated-node/permutation baseline, residual-block Rademacher averaging
closes exactly the configurations whose four block labels have even
multiplicity.  With nonnegative coefficients the complementary block-odd
configurations form a positive physical sum.  Bounding that block-odd sum by
`Dq^o(1)` is the weakest presently justified positive reduction.  Comparing
it to the often much smaller randomized trace is an additional and generally
stronger unconditionality demand.

## 1. Uniform four-cycle is equivalent to all-plus

For the hard physical support put

```text
kappa(a,b,c)=1_(|8abc-q^3|<=qD),
A_z(a,b)=sum_c z_c kappa(a,b,c).                     (1.1)
```

Let `u=|z|`.  Since `kappa>=0`, every Gram entry obeys

```text
|(A_z^*A_z)(b,b')|
 <=sum_a A_u(a,b)A_u(a,b')
 =(A_u^*A_u)(b,b').                                  (1.2)
```

Squaring and summing the entries gives

```text
||A_z||_S4^4<=||A_u||_S4^4,
||u||_2=||z||_2.                                     (1.3)
```

Conversely, every nonnegative `u` is an allowed complex coefficient vector.
Therefore the optimal constants in

```text
||A_z||_S4^4<=C D q^epsilon||z||_2^4  for all complex z
```

and in its restriction to `z=u>=0` are identical.

For an oriented color rectangle

```text
C=(c11,c12;c21,c22)
```

let `Gamma(C)` be the physical occurrences
`X=(a1,a2,b1,b2)` satisfying all four hard windows, and put

```text
m(C)=|Gamma(C)|,
w_u(C)=u_c11 u_c12 u_c21 u_c22.
```

Direct expansion has no cancellation for `u>=0` and gives

```text
||A_u||_S4^4=sum_C m(C)w_u(C)=:F_+(u).              (1.4)
```

Thus

```text
uniform hard four-cycle  <=>  F_+(u)<<Dq^o||u||_2^4
                               for every u>=0.       (1.5)
```

This equivalence uses both hypotheses: the raw kernel is nonnegative and the
coefficient theorem is uniform over all complex vectors.  For a single
oscillatory kernel, a mean-zero coefficient class, or another restricted
class not containing every `|z|`, (1.3) remains a sufficient domination but
need not be reversible.

## 2. The fork above positivity: operator norm versus four-cycle

Always

```text
||A_z||_op^4<=||A_z||_S4^4.                          (2.1)
```

There is no dimension-free converse.  The repository's repeated-Latin-block
controls explicitly separate an operator target from `(FC)`: the former can
hold while the fourth trace is too large.  Consequently, if the ultimate
analytic application only needs

```text
||A_z||_op<<D^(1/4)q^o||z||_2,                      (2.2)
```

then choosing (2.1) as the proof route is the earliest decision-tree
strengthening.  It may still be strategically useful, but it is not
equivalent to (2.2).

If “sharp four-cycle bound” means the Schatten-four statement itself, this
fork has already been accepted by definition, and the passage to `F_+` in
Section 1 loses nothing further.

## 3. Exact positive exceptional-sector reduction

For `u>=0`, every literal deletion of physical rectangle occurrences is a
positive deletion.  The proved repeated-node/permutation theorem bounds the
complete sector in which two of

```text
a1,a2,b1,b2,c11,c12,c21,c22
```

coincide, together with its square-edge and permutation cases, by
`Dq^o||u||_2^4`.  Hence

```text
F_+(u)=F_exc(u)+F_ad(u),
F_exc(u)<<Dq^o||u||_2^4,                             (3.1)
```

where `F_ad` is the all-eight-distinct physical sum.  Positivity makes

```text
full four-cycle <=> F_ad(u)<<Dq^o||u||_2^4.          (3.2)
```

No factorial completion pair is needed for (3.2).

## 4. Exact even/odd residual-block decomposition

Partition the all-distinct physical triples into the proved short residual
classes `I`, and write

```text
A(u)=sum_I A_I(u).                                   (4.1)
```

Introduce independent real Rademacher signs `epsilon_I`.  One rectangle in
the fourth-trace expansion has four residual-block labels

```text
I_11,I_12,I_21,I_22.                                 (4.2)
```

The sign expectation is exactly

```text
E product_(i,j) epsilon_(I_ij)
 =1  if every label in (4.2) occurs an even number of times,
 =0  otherwise.                                     (4.3)
```

Call the two physical occurrence sets `Omega_even` and `Omega_odd` in the
full fourth trace of the retained linear triple system.  Since `u>=0` and
the hard kernel is nonnegative, every rectangle coefficient is
nonnegative.  Therefore

```text
F_linear(u)=F_even(u)+F_odd(u),

F_even(u)
 =E_epsilon||sum_I epsilon_I A_I(u)||_S4^4,          (4.4)

F_odd(u)>=0.                                         (4.5)
```

Here “odd” means that at least one **residual-block label** occurs an odd
number of times.  It has nothing to do with the parity of `m(C)`, integer
carrier parity, or an ordered-pair orientation.

The Rademacher trace in (4.4) still contains even configurations belonging
to the already bounded repeated-node rectangle sector.  If
`F_even,ad,F_odd,ad` denote the restrictions to the all-eight-distinct
physical occurrences from Section 3, positivity gives

```text
F_ad=F_even,ad+F_odd,ad,
F_even,ad<=F_even.                                   (4.5a)
```

The proved weighted square-function/Rademacher theorem gives

```text
F_even(u)<<Delta q^o||u||_2^4
            <<Dq^o||u||_2^4.                        (4.6)
```

Combining (3.1), (4.4), and (4.6) yields the exact remaining target

```text
F_odd,ad(u)<<Dq^o||u||_2^4  for every u>=0.          (ODD-FC)
```

Thus `(ODD-FC)` is equivalent, up to the already proved baselines, to the
sharp hard four-cycle estimate.

Some block-odd subfamilies may already be controlled by tangent or coherent
packet theorems.  They can be removed from `(ODD-FC)` only when their exact
positive occurrence IDs and reconstruction are supplied.  A theorem in a
different transformed coordinate is not automatically such a deletion.

## 5. Why Rademacher unconditionality is stronger than necessary

Equations (4.4)--(4.6) do not require

```text
F_ad(u)<<q^o F_even(u).                              (5.1)
```

On a diffuse coefficient bin, the proved randomized estimate can be much
smaller than `D||u||_2^4`, while the desired theorem still permits the full
`D` budget.  Requiring the block-odd part to be comparable to its randomized
part therefore asks for unnecessary savings.  Exact integer tangent
fixtures also disprove raw unconditionality in the broader product-window
class.

The lossless conclusion from Rademacher averaging is only that the even
sector is closed and the odd positive sector remains.  It supplies no free
comparison between their sizes.

## 6. The factorial fork was later and lossy

The direct open source has coefficient `m(C)`.  The factorial expression

```text
PAIR(u)=sum_C m(C)(m(C)-1)w_u(C)                    (6.1)
```

is a useful sufficient bootstrap because the occupied-color mass is already
bounded, but it is not the exact endpoint and can exceed it by a factor
`asymp m(C)`.  Hence the program statement which calls `PAIR` the “exact
positive endpoint” is incorrect.

The identities

```text
m<=1_(m>0)+m(m-1)/2,

m=1_(m>0)+m(m-1)/m                                 (6.2)
```

show respectively why factorial control suffices and how reciprocal
normalization can reconstruct the first moment.  Neither identity supplies
new cancellation or arithmetic compression.

## 7. Earliest fork and weakest known reduction

The decision tree is therefore

```text
ultimate operator norm
  --strict sufficient step--> Schatten-four/four-cycle
  --lossless for the hard uniform theorem--> nonnegative all-plus F_+
  --proved positive deletion--> all-eight-distinct F_ad
  --proved Rademacher even bound--> positive block-odd F_odd
  --strict sufficient steps--> PAIR, A4, GACCT, packet inverse, ...
```

Accordingly:

* for the ultimate operator theorem, the earliest strengthening is the
  choice of a fourth-trace proof;
* within the four-cycle project, positivity is not a mistake;
* within that project, the earliest material overstrengthening was the
  promotion of factorial `PAIR` to the accepted endpoint;
* the exact weakest currently justified open reduction is `(ODD-FC)`, not a
  packet, Carleson, or unconditionality theorem.

## 8. Source locations

The raw trace and absolute domination are in
`ZETA23-QP-PHYSICAL-TENSOR-ABSOLUTE-DOMINATION-AND-CENTER-PARTICIPATION-GATE-2026-08-25.md`,
Sections 1--2.  The repeated-sector theorem is
`ZETA23-QP-FOUR-CYCLE-REPEATED-NODE-PERMUTATION-THEOREM-2026-08-15.md`.
The exact Rademacher pairing and square-function estimate are in
`ZETA23-QP-DIFFUSE-BIN-CROSS-GRAM-MULTIPLICITY-GATE-2026-08-24.md`,
Sections 2--3, and the exact block-label parity identity is in
`ZETA23-QP-WEIGHTED-UNCONDITIONALITY-HOSTILE-AUDIT-2026-08-24.md`,
Section 2.
