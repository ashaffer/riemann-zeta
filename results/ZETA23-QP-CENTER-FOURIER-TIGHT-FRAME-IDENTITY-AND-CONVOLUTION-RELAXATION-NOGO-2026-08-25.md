# QP center Fourier: exact tight-frame identity and the convolution-relaxation no-go

**Date:** 2026-08-25  
**Verdict:** Fourier transform in the physical center `b` is an exact unitary
rewriting of the **ungrouped row-pair** fourth Schatten norm.  It does not
prove the proposed center-coherent convolution estimate

```text
||sum_b f_b*f_b||_2^2 << D q^o(1)||z||_2^4.          (CCSR)
```

In fact, `(CCSR)` is too strong at the stated abstract-incidence level: a
pair-unique family violates it by an arbitrarily large factor.  A finite
literal hard-window example over every integer in the same logarithmic shell
also has `C(F)>D||z||_2^4`, while its true ungrouped row-pair norm remains
below that quantity.  The latter is a sharp-constant diagnostic, not an
asymptotic disproof of a `q^o(1)` estimate.  Both examples locate the
inflation precisely in grouping different row pairs having the same sum.

This is **not** an asymptotic counterexample on the actual prime-power shell
at the critical relation `q=D^(33/16)`.  No such physical counterexample is
claimed.  The sharp four-cycle bound remains open.  What is closed is the
automatic route from pair uniqueness, the lossless local Fejer/Airy
theorems, and center Parseval to `(CCSR)`: that implication has exact
countermodels.  A direct theorem using additional actual-shell arithmetic
is not logically ruled out.

The correct remaining statement is the original rank-one color-pair bound

```text
||H(conj(z) tensor z)||_2^2 << D q^o(1)||z||_2^4,    (0.1)
```

with the row-pair coordinate retained.  Its center-Fourier form is a fourth
frame-potential estimate.  Parseval makes the two formulations exactly
equal; a new arithmetic/vector large sieve is still needed to bound them.

## 1. Two norms which must not be conflated

Put `x_c=|z_c|` and

```text
F(a,b)=f_b(a)=sum_c x_c*kappa(a,b,c),
kappa(a,b,c)=1_(|8abc-q^3|<=qD).                     (1.1)
```

The positive ungrouped row-pair majorant is

```text
P(F)=sum_(a,a') |sum_b F(a,b)F(a',b)|^2
    =||F F^*||_(HS)^2
    =||F||_(S_4)^4.                                  (1.2)
```

The proposed convolution relaxation is

```text
G(S)=sum_b sum_(a+a'=S) F(a,b)F(a',b),
C(F)=sum_S |G(S)|^2.                                 (1.3)
```

For nonnegative `F`, expanding the square shows only

```text
P(F)<=C(F).                                          (1.4)
```

The extra terms in `C(F)` couple every two distinct row pairs
`(a,a')!=(u,u')` with the same sum.  They are not present in the fourth
trace.  The examples in Sections 4 and 5 show that their total can be a
polynomial factor larger than `P(F)`.

## 2. Exact center-Fourier identities

Zero-pad the center interval into `Z/MZ`, with no collisions among the
represented centers, and use the unitary transform

```text
Fhat_t(a)=M^(-1/2) sum_b F(a,b)e_M(tb).              (2.1)
```

Right multiplication by the DFT is unitary.  Consequently

```text
P(F)
 =sum_(t,u) |sum_a conjugate(Fhat_t(a))*Fhat_u(a)|^2.
                                                               (2.2)
```

This is the exact center-frequency fourth frame potential.  It is neither
an inequality nor a saving: (2.2) is just unitary invariance of the
Schatten norm.

The stronger convolution has a different exact identity:

```text
G=sum_t Fhat_t*Fhat_(-t).                            (2.3)
```

For the unnormalized transform `F_t=sum_b F(a,b)e_M(tb)`, this is

```text
G=M^(-1)sum_t F_t*F_(-t).                           (2.4)
```

Convexity therefore gives

```text
||G||_2^2
 <=M^(-1)sum_t ||F_t*F_(-t)||_2^2.                 (2.5)
```

Estimate (2.5) is generally lossy by one complete physical participation
degree.  It cannot be combined frequency by frequency with scalar RSR or a
fixed-lattice Airy estimate and then summed.

## 3. A one-color matching proves the frequencywise loss

For one fixed color, pair uniqueness makes its incidence matrix a partial
matching.  Take a matching of size `r`, with binary-distinct row labels and
distinct centers.  Then

```text
P(F)=r,                 C(F)=r.                     (3.1)
```

But exact character orthogonality gives

```text
M^(-1)sum_t ||F_t*F_(-t)||_2^2=r^2.                (3.2)
```

The `r^2` terms in (3.2) are the ordered matching pairs before the center
characters impose equality.  Their cross-frequency cancellation is exactly
what reconstructs the `r` diagonal terms in (3.1).  At a physical color
degree `r asy D`, taking absolute values or applying a separate theorem for
each `t` loses the whole factor `D`.

By contrast, the ungrouped frame potential (2.2) remains exactly `r`: the
center-frequency Gram is a rank-`r` orthogonal projection.  This is the
useful tight-frame picture, and it requires retaining both frequency
indices through the final square.

## 4. Abstract pair-unique countermodel to `(CCSR)`

Take `r` rows and `L` centers and put one occupied edge in every cell.  Give
each cell its own color with coefficient one.  This respects cell
uniqueness, and

```text
||z||_2^2=rL,
F=the r-by-L all-ones rectangle.                     (4.1)
```

The true row-pair norm is exactly

```text
P(F)=L^2 r^2=||z||_2^4.                             (4.2)
```

For rows `{0,...,r-1}`, their exact additive energy is

```text
E^+({0,...,r-1})=(2r^3+r)/3.                        (4.3)
```

Hence

```text
C(F)=L^2(2r^3+r)/3
    =[2r/3+1/(3r)]||z||_2^4.                        (4.4)
```

The convolution relaxation has manufactured a factor asymptotic to `2r/3`
although the ungrouped fourth-trace norm has no loss.  This fixture is an
abstract incidence countermodel, not a product-band or prime-power
construction.

## 5. Exact finite hard-window witness

There is also a witness using the literal hard window.  Take

```text
q=80,       D=33,
I={33,34,...,48},
z_c=1 for c in I.                                   (5.1)
```

The interval `I` is exactly the set of all integers in

```text
[(q/2)e^(-0.2),(q/2)e^(0.2)].                       (5.2)
```

Define `F` by (1.1) with rows, centers, and colors all in `I`.  Direct exact
integer enumeration gives

```text
maximum colors in one (a,b) cell:       1;
number of selected triples:            94;
||z||_2^2:                              16;
D||z||_2^4:                           8448;
P(F):                                 2310;
C(F):                                16060;
P(F), after deleting a=a':            1698;
C(F), after deleting a=a':           12572.          (5.3)
```

Thus the constant-one inequality `C(F)<=D||z||_2^4` fails by the factor
`16060/8448>1.90`, while the ungrouped positive row-pair target is safely
below the same ceiling.  The inflation survives deletion of every diagonal
row pair: `12572>8448`.

This witness uses **all integers**, has `q=80,D=33`, and does not impose the
critical asymptotic relation or actual-prime-power support.  A single finite
ratio cannot refute a bound with an unspecified absolute constant and a
`q^o(1)` loss.  It is an exact diagnostic showing that even the literal hard
window can make the convolution substantially larger than the quantity it
was introduced to majorize; it is not a physical four-cycle counterexample.

## 6. General density obstruction

The source of the failure is visible without Fourier analysis.  For a
nonnegative matrix put

```text
d_b=sum_a F(a,b),       E=sum_b d_b,
B=# centers,            R=# possible row sums.       (6.1)
```

Then exactly

```text
||G||_1=sum_b d_b^2.                                 (6.2)
```

Two applications of Cauchy give

```text
C(F)>= (sum_b d_b^2)^2/R
    >= E^4/(B^2 R).                                  (6.3)
```

On the actual shell, take `z_c=1`, let `N` be the number of colors, and let
`E` now denote the number of selected physical triples.  Since `B,R<<q`,
the proposed `(CCSR)` would force the necessary sparsity condition

```text
E << D^(1/4) q^(3/4) N^(1/2) q^o(1).                (6.4)
```

A sharper insertion of `B=N` and `R<<q` gives

```text
E^4 << D q N^4 q^o(1).                              (6.5)
```

For `N=q^(1+o(1))`, this is

```text
E << D^(1/4)q^(5/4+o(1)).                           (6.6)
```

The density heuristic `E=Dq^(1+o(1))` would violate (6.6) by the fourth-root
of `D^3/q`; at `q=D^(33/16)`, the underlying fourth-power gap is
`D^(15/16)`.  No lower bound of the required strength for the actual
prime-power shell is proved here, so this is a rigorous necessary condition
and a warning, not an asymptotic physical disproof.

## 7. Why the Fejer/Stinespring and Airy theorems do not repair this step

The supported harmonic in the exact Stinespring lift is

```text
e(h theta_(a,b,c)),
theta_(a,b,c)=q^3/(8ac)-b.                           (7.1)
```

Because `h` and `b` are integers,

```text
e(h theta_(a,b,c))=e(h q^3/(8ac)).                  (7.2)
```

Thus the Fejer harmonic phase itself contains no center character.  The
center remains encoded in the hard support and bounded Stinespring
amplitude.  Fourier transform in `b` is a second, independent unitary
coordinate; it is not supplied by the Fejer phase.

The fixed-normal-lattice Airy theorem is lossless for one retained lattice,
but (3.2) shows that estimating each center frequency separately and then
summing repeats a one-color packet `r` times.  Airy vector Plancherel cannot
undo a convexity step already taken in (2.5).  Moreover, the Fourier
variable dual to the completion sum `S=a+a'` is not the center-frequency
variable dual to `b`; identifying them would conflate (1.2) and (1.3).

Accordingly the existing lossless Fejer and Airy results remain valid local
theorems, but they do not imply `(CCSR)` and should not be assembled through
the global positive convolution.

## 8. Correct center-frequency theorem

For complex coefficients define the original matrix

```text
A_z(a,b)=sum_c z_c*kappa(a,b,c)                     (8.1)
```

and its unitary center transform

```text
V_t(a)=M^(-1/2)sum_b A_z(a,b)e_M(tb).               (8.2)
```

The correct mask-free target is exactly

```text
sum_(t,u) |<V_t,V_u>|^2
 <<D q^o(1)||z||_2^4.                               (8.3)
```

By (2.2), (8.3) is equivalent to the desired fourth Schatten estimate.  In
the second-incidence notation it is (0.1), with

```text
H_((a,a'),(c,c'))
 =sum_b kappa(a,b,c)kappa(a',b,c').                 (8.4)
```

A useful new large sieve must therefore do more than invoke Parseval: it
must estimate the complete two-frequency frame potential while preserving
the row-pair coordinate, the rank-one color tensor, and any physical
deletion mask.  No completion-sum grouping may be inserted before the
square.

One equivalent operator formulation is especially terse.  For each color,
let `P_c(a,b)=kappa(a,b,c)`.  Pair uniqueness makes `P_c` a partial
permutation matrix, and the matrices have disjoint cell support.  The
remaining theorem is

```text
||sum_c z_c P_c||_(S_4)^4
 <<D q^o(1)sum_(c,c')|z_c z_c'|^2.                  (8.5)
```

Right multiplication by the center DFT changes neither side.  The needed
breakthrough is arithmetic almost-orthogonality among these physical
partial permutations, not another Fourier normalization.

## 9. Binary status

```text
center DFT preserves the ungrouped row-pair norm:          EXACT;
center DFT reconstructs the same-center convolution:      EXACT;
frequencywise convexity can lose one color degree:        PROVED;
abstract pair-unique CCSR:                                 FALSE;
all-integer hard-window constant-one target:              FALSE (finite);
critical all-integer asymptotic CCSR:                      NOT REFUTED HERE;
critical actual-prime-power CCSR:                          NOT REFUTED HERE;
CCSR from current local/tight-frame inputs:                FALSE;
critical actual-prime-power CCSR with new arithmetic:      OPEN;
correct row-pair/frame-potential theorem:                  OPEN;
sharp four-cycle bound:                                    NOT PROVED.
```

All finite identities, the matching loss, the repeated-row model, the
density inequalities, and the exact hard-window witness are replayed in

```text
src/qp_center_fourier_large_sieve_audit.py
src/test_qp_center_fourier_large_sieve_audit.py
```

The repeated-row ratio, critical density-gap exponent, and exact finite
integer comparisons are also certified by Lean in

```text
lean/weilcert/QPCenterFourierNoGo.lean
```
