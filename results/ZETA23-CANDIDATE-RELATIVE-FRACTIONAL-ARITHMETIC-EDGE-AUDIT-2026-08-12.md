# The candidate-relative fractional arithmetic edge is a positive-reserve theorem

Status: exact scalar and operator reduction, fixed-depth exponent audit, and
sharp isolated-block obstruction, 2026-08-12.  No candidate-relative lower
edge, zero-free strip, RH statement, or new bound on a zeta zero is proved.

## 1. Verdict

Fix the first-strip band

```text
alpha=beta-1/2 in [0.49,1/2),
d=0.66,
rho=1/2+alpha+i*gamma.
```

The requested estimate

```text
Q_ar(q_rho)>=-(1-epsilon)*K_rho+o(K_rho)            (1.1)
```

does reduce to one actual-coefficient scalar.  It does **not**, however,
follow from an aggregate Schur angle, from nulling the cross-prime row, or
from a coefficient-free completion identity.

The exact obstruction is simpler and sharper.  On the selected-positive
quotient the completed explicit formula is

```text
K_ar=-N_rho+R_other,rho.                            (1.2)
```

Here `N_rho>=0` is the rank-one selected negative carrier and
`R_other,rho` is every unselected zero contribution, with all completion
terms already included through the equality.  Therefore, for a normalized
state with

```text
<q_rho,N_rho q_rho>=K_rho,
```

one has the identity

```text
Q_ar(q_rho)+K_rho
 =<q_rho,R_other,rho q_rho>.                        (1.3)
```

Consequently (1.1) is equivalent to

```text
<q_rho,R_other,rho q_rho>
   >=epsilon*K_rho+o(K_rho).                        (1.4)
```

This is the **positive-reserve identity**.  It is the exact amount of
arithmetic information missing from the current program.  In the isolated
one-pair completed block, `R_other,rho=0`, and every fixed `epsilon>0` in
(1.1) fails exactly.  Thus no argument which sees only the selected block,
functional equation, abstract Hilbert geometry, or positivity of a
covariance can prove a fractional edge.  The actual von Mangoldt
coefficients must force the positive reserve in (1.4), equivalently must
rule out the isolated self-resonant scalar described below.

There is one useful simplification.  For truly compact endpoint lobes of
diameter less than `log 2`, every same-leg prime-power translate vanishes
exactly.  The arithmetic problem is then one completed cross-leg scalar
plus power-negligible background.  This removes the same-leg bookkeeping,
but it does not remove (1.4): the completed cross row is target-aligned.

At `alpha=0.49,d=0.66`, the raw carrier is only `Y^0.01` below the generic
transition square-root scale, where `Y=X^d`.  After paying the ideal
one-product Pick bill, the retained exponent is only

```text
E_0/d=0.0180303234...                               (1.5)
```

in `Y`-units.  A coefficient-uniform square-root estimate is then larger
by `Y^(0.4819696766...-o(1))`.  Hence a sequential strategy of first paying
the entire Pick bill and then applying a generic scalar prime bound has no
quantitative chance with current inputs.  A proof must be coupled and
candidate-specific.

## 2. Exact quantifiers and normalization

Fix in advance:

```text
alpha_0=0.49,
d_0=0.66,
a=0.10076,
E_0=E_1(alpha_0,d_0,a)=0.0119000134... .            (2.1)
```

Let `A_geom` be a deterministic construction depending only on the
hypothetical candidate and its divisor geometry, with a geometry-only
tie-breaker.  It must not choose among feasible states after inspecting the
von Mangoldt value.  For every sufficiently high actual zero

```text
rho=1/2+alpha+i*gamma,
alpha in [alpha_0,1/2),                              (2.2)
```

suppose `A_geom` produces a compact normalized state `q_rho` satisfying the
selected-positive equation and

```text
<q_rho,N_rho q_rho>=K_rho,
K_rho>=X^(E_0-o(1)).                                (2.3)
```

The exact powers of `log X` are harmless for the statements below and are
absorbed in `X^o(1)`.  The operator `K_ar` is assembled after `q_rho` has
been fixed from the actual `Lambda(n)`, the pole rows, and the archimedean
multiplier.  It uses no collateral-zero list.  Only after (2.2) is assumed
may the explicit formula identify it with the zero operator and give (1.2).

For one fixed `epsilon>0`, uniformly in every candidate in (2.2), the
arithmetic target is exactly

```text
<q_rho,K_ar q_rho>+K_rho
   >=epsilon*K_rho+o(K_rho).                        (2.4)
```

Equation (2.4), rather than whole-matrix positivity, pointwise prime
nulling, or a uniform sinh-tent inequality at every depth, is the weakest
fractional theorem card for this fixed state.

## 3. The actual coefficient scalar

The centered-even route makes (2.4) one dimensional.  Let a real odd
physical packet `f` have even autocorrelation

```text
C_f(u)=integral_R f(x)*f(x+u)dx,
```

and let `K_f` be its nonnegative real-axis Fourier square.  After modulation
to height `gamma`, define the prime-minus-continuum scalar

```text
S_f(gamma)
 =sum_n Lambda(n)n^(-1/2) C_f(log n)cos(gamma log n)
  -integral_1^infinity x^(-1/2)C_f(log x)
                         cos(gamma log x)dx,         (3.1)
```

where compact support makes both expressions finite.  Put

```text
B_f(gamma)
 =2*pi*C_f(0)
  +integral_R K_f(s)*[G(gamma+s)+G(gamma-s)]/2 ds.  (3.2)
```

The exact completed arithmetic value is

```text
Q_ar(f)=B_f(gamma)-2*S_f(gamma).                    (3.3)
```

Thus the fractional edge for a state with selected carrier `K_rho` is
equivalent to the single one-sided inequality

```text
S_f(gamma)
 <=[B_f(gamma)+(1-epsilon)*K_rho]/2+o(K_rho).       (3.4)
```

No absolute value is required.  This is strictly more targeted than a
uniform norm estimate for a prime matrix.

### 3.1 Exact centered sinh-tent spelling

For the unprojected core packet

```text
f(x)=sinh(alpha*x)*1_(|x|<=L/2),
T=exp L,
s_+=rho,
s_-=1-conj(rho),                                   (3.5)
```

put `Delta P_T=P_T-I_T` and
`Delta D_T=L*Delta P_T+(Delta P_T)'`.  Then (3.1) is exactly

```text
S_(L,alpha,gamma)
 =1/4*Re{
      (T^alpha/alpha)*Delta P_T(rho)
     -(T^(-alpha)/alpha)*Delta P_T(1-conj(rho))
     -Delta D_T(rho)-Delta D_T(1-conj(rho))}.       (3.6)
```

This is the promised single scalar in actual von Mangoldt coefficients.
Finite aperture and Hahn projection replace the sinh-tent weights by an
explicit finite cosine weight, but do not restore a matrix quantifier.

Let

```text
A_(L,alpha)=C_f(0)
 =sinh(alpha*L)/(2*alpha)-L/2,

K_sel
 =2*A_(L,alpha)^2
  -2*Re K_f(2*gamma+i*alpha).                       (3.7)
```

For `gamma>sinh(alpha L)/A_(L,alpha)`, the matched-quartet theorem gives
`K_sel>0`, and the selected functional-equation quartet contributes exactly
`-K_sel`.  Combining (3.3) with the explicit formula yields the exact
actual-coefficient reserve

```text
mathfrak R_Lambda(rho;f)
 :=B_f(gamma)-2*S_f(gamma)+K_sel
  =sum_(unselected zeros rho') h_f,gamma(rho').     (3.8)
```

Multiplicity is included, and an unmarked additional copy of the selected
zero belongs to the right side.  The fractional lower edge is precisely

```text
mathfrak R_Lambda(rho;f)
   >=epsilon*K_sel+o(K_sel).                        (3.9)
```

Equation (3.8) is useful in both directions.  Its left side contains only
the actual prime, pole, gamma, and candidate parameters; its right side
shows why the scalar is self-resonant at an actual candidate.  If the
unselected response is `o(K_sel)`, then

```text
S_f(gamma)=[B_f(gamma)+K_sel]/2+o(K_sel),            (3.10)
```

and every fixed-fraction improvement in (3.4) is false.

## 4. Bipartite cross-leg spelling

The same identity survives the efficient two-leg construction.  Split a
compact packet as `q=ell+r`, with disjoint endpoint lobes, and write the
completed cross form as

```text
Q_cross(q)=2*Re <ell,P_comp r>.                     (4.1)
```

All prime powers, both pole orientations, and the archimedean integral are
inside the one operator `P_comp`.  Pointwise prime nulling is unnecessary.

On the exact selected mirror face, after the selected positive row has been
nulled, let `N_mir` be the selected carrier and put

```text
C=cosh(alpha*D),
c=C/(C-1)=1+O(exp(-alpha*D)).                       (4.2)
```

The selected completed cross block is exactly

```text
B_0=-c*N_mir.                                      (4.3)
```

Writing the actual completed cross operator as

```text
B_ar=B_0+R_cross,                                  (4.4)
```

a carrier state with `<q,N_mir q>=K_rho` obeys

```text
<q,B_ar q>=-c*K_rho+<q,R_cross q>.                 (4.5)
```

Once the same-leg and background forms are `o(K_rho)`, the fractional
edge again requires

```text
<q,R_cross q> >=(epsilon+o(1))*K_rho.              (4.6)
```

An aggregate Schur projection does not prove (4.6).  Exact cancellation of
the completed cross scalar would require the stronger reserve
`<q,R_cross q>=c*K_rho`.  In the isolated one-pair block
`R_cross=0`, the aggregate row is parallel to the target and both the
complex and minimal real aggregate equations erase the carrier.  Therefore
the aggregate angle and the fractional arithmetic edge are not independent
gates: both require an actual positive transverse remainder.

## 5. Same-leg prime terms can be removed exactly

There is a clean reduction which should be retained in future compact
constructions.

### Lemma 5.1 (sub-`log 2` lobe)

Let `ell` be compactly supported in an interval of diameter `w<log 2`.
Then for every prime power `n>=2`,

```text
R_(ell,ell)(log n)
 =integral ell(t+log n)*conj(ell(t))dt=0.           (5.1)
```

The same holds for the other endpoint lobe `r`.  Hence the complete
same-leg prime form vanishes exactly.

#### Proof

The supports of `ell(t+log n)` and `ell(t)` are disjoint because
`log n>=log 2>w`.  The product in (5.1) is identically zero.  QED

The macroscopic selected carrier comes from the separation `D=dL`, not
from the individual lobe diameter, so Lemma 5.1 costs no carrier power.
Pole rows are finite rank and the archimedean same-leg contribution is
polylogarithmic in the current normalization.  Thus a compact transporter
which keeps each lobe below `log 2` really does reduce the arithmetic task
to (4.1).

This lemma does not apply directly to an unrestricted causal Blaschke
extremizer: its inverse transform has a tail.  The compact Pick transfer
must preserve the sub-`log 2` support, or quantify the tail contribution,
before (5.1) may be used.

## 6. The fixed-depth exponent mismatch

Let

```text
Y=exp D=X^d.
```

Before collateral isolation, a depth-`alpha` two-lobe carrier has scale

```text
K_raw=Y^(alpha-o(1))/L.                             (6.1)
```

At `alpha=0.49`, this is `Y^(0.49-o(1))/L`.  The available
coefficient-uniform transition-scale prime estimate is at the
`Y^(1/2-o(1))/L` scale.  Thus even the raw state needs a fixed power gain

```text
Y^(-0.01+o(1))                                     (6.2)
```

over the square-root exponent.  This is already strip-strength, although
the exponent gap is small.

Under ideal global phase-cell compression and balanced one-product
splitting, the retained carrier exponent at the fixed interior parameters
is

```text
K_Pick>=X^(0.0119000134...-o(1))
       =Y^(0.0180303234...-o(1)).                  (6.3)
```

A generic square-root prime estimate is therefore larger than (6.3) by

```text
Y^(0.5-0.0180303234...-o(1))
 =Y^(0.4819696766...-o(1)).                         (6.4)
```

Equation (6.4) is not a lower bound for the tailored scalar and does not
falsify (3.4).  It is a method-level budget: KMT, a large sieve, or a
coefficient-norm Loewner bound applied **after** the full Pick loss cannot
close the edge.  The state must instead obtain a candidate-specific
one-sided cancellation, an exact cross scalar cancellation with a genuine
positive reserve, or a positive-spectral aligned mass at least

```text
Y^(-0.0180303234...+o(1)).                          (6.5)
```

The known square-root-conditioned mechanisms are far below (6.5).

## 7. Sharp obstruction and the deep-reserve dichotomy

The positive-reserve identity gives a fail-fast theorem.

### Theorem 7.1 (isolated-candidate obstruction)

Assume (2.2), and let `q_rho` be any normalized selected-positive-null state
with carrier `K_rho`.  If

```text
<q_rho,R_other,rho q_rho>=o(K_rho),                (7.1)
```

then

```text
Q_ar(q_rho)=-K_rho+o(K_rho),                       (7.2)
```

and (1.1) fails for every fixed `epsilon>0`.

#### Proof

Substitute (7.1) into the exact identity (1.2).  QED

This theorem applies in particular to the exact isolated one-pair
completed block.  It is not an Euler-product counterexample and does not
assert that zeta has such an isolated zero.  It proves that the missing
actual-coefficient input cannot merely bound errors: it must produce a
positive term of the same carrier scale.

On the normalized raw two-lobe carrier slice, the proved shallow-depth
reduction says that on-line rows and collateral pairs of depth

```text
alpha'<=alpha*d-epsilon_0                          (7.3)
```

have total operator norm `o(K_raw)`.  At the first-strip parameters,

```text
alpha*d=0.49*0.66=0.3234.                           (7.4)
```

Subject to the separately stated remote and completion tail estimates,
(1.4) therefore forces a carrier-aligned positive contribution from the
deep remainder

```text
alpha'>0.3234-epsilon_0,
equivalently Re rho'>0.8234-epsilon_0.              (7.5)
```

Existence of such a zero is not enough; its compressed orientation must
make the quadratic remainder positive by at least `epsilon*K_raw`.  Thus
the exact dichotomy is

```text
deep positive collateral reservoir of carrier size,
or
actual prime scalar saturates the selected self-resonance and the
fractional edge fails under the candidate.          (7.6)
```

Current zero-density theorems give upper counts and do not force the first
branch.  Current prime-twist bounds do not rule out the second branch.

There is a new coefficient-specific **upper** count which sharpens this
statement but does not reverse it.  The completed logarithmic derivative at
`1+L^(-1/2)+it` gives, in one ordinate cell of width `C/L`,

```text
#{rho:Re rho>=sigma_0}
 <=[(1-sigma_0)/2+o(1)]*L.                          (7.7)
```

Thus the first-strip cell contains at most `0.005L+o(L)` zeros with
`Re rho>=0.99` and at most `0.0883L+o(L)` with
`Re rho>=0.8234`.  The constants and sign are audited in
`ZETA23-DEPTH-SENSITIVE-MICROSCOPIC-ZERO-COUNT-2026-08-12.md`.
This is materially better geometry, but (7.7) is an upper bound.  It neither
forces the positive reserve in (1.4) nor excludes a growing depth fan of
distinct collaterals in one phase cell.  Treating it as a lower-edge theorem
would reverse its logical direction.

## 8. Research decision

The fractional arithmetic edge remains open.  This audit prunes three
routes in their uncoupled forms:

```text
pointwise cross-prime nulling without a positive completed reserve;
an aggregate Schur angle treated independently of target alignment;
a generic square-root prime estimate applied after the full Pick bill.
```

The smallest live actual-coefficient target is now the following scalar:

> For the deterministic compact Pick state attached to every hypothetical
> `alpha in [0.49,1/2)`, prove
>
> ```text
> mathfrak R_Lambda(rho;q_rho)
>  :=Q_ar(q_rho)+K_rho
>  >=epsilon*K_rho+o(K_rho)                         (8.1)
> ```
>
> for one fixed `epsilon>0`, where `Q_ar` is evaluated by (3.3), or by the
> explicit two-abscissa scalar (3.6) in the unprojected core.

The most promising formulation is **coupled**, not sequential: construct
the compact state while tracking both its Pick attenuation and the sign of
the one scalar (8.1).  Any proposed proof should fail fast on the exact
isolated block and must identify the zeta-specific mechanism which supplies
the positive reserve.  Merely renaming that mechanism an angle, a
transverse inradius, or an arithmetic admission does not advance the edge.

Primary dependencies:

- `ZETA23-LOGICAL-STRENGTH-OF-PICK-PRIME-AND-SINH-GATES-2026-08-12.md`;
- `ZETA23-CENTERED-SINH-TENT-FUNCTIONAL-EQUATION-NOGO-2026-08-12.md`;
- `ZETA23-CENTERED-COSINE-ONE-SQUARE-ARITHMETIC-GATE-2026-08-12.md`;
- `ZETA23-BIPARTITE-BLASCHKE-ARITHMETIC-COUPLING-GATE-2026-08-12.md`;
- `ZETA23-HIGH-HEIGHT-CARRIER-SLICE-ANALYTIC-REDUCTION-2026-08-12.md`;
- `ZETA23-MULTIWITNESS-MULTISCALE-AGGREGATE-CANCELLATION-AUDIT-2026-08-12.md`.
