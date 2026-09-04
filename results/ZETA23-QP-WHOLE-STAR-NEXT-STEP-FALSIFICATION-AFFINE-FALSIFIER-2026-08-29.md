# Is whole-star RDP/line cover really the next step?

Date: 2026-08-29

## Verdict

Whole-star RDP is a sufficient endgame, but it is strictly stronger than the
anchored row-sum estimate needed by the operator and is not the best next
atomic target.  Present line-cover evidence is almost vacuous because all
measured actual-prime-power endpoint degrees are at most 15.  The actual
sharp target is the remaining generic anchored Carleson tail `(GACCT_R)` or
its cardinal shadow `(GP_R)`.  The small-height one-arm cap remains the
fastest falsifier of the line-based RDP program, not the main project node.

## 1. Why the finite cover evidence is weak

Any set of `n` points is coverable by `ceil(n/2)` affine lines simply by
pairing its points.  Compare this trivial ceiling with the exact covers in
the actual-prime-power log-window audit:

| fixture | maximum endpoint degree | trivial cover | measured maximum cover |
|---|---:|---:|---:|
| `q=11801,U=35` | 11 | 6 | 5 |
| `q=11801,U=44` | 15 | 8 | 6 |
| `q=25013,U=40` | 10 | 5 | 5 |
| `q=50021,U=40` | 10 | 5 | 5 |

Thus the two larger fixtures show literally no improvement over an arbitrary
point set.  The strict critical prime-power fixtures have residual degree
one and are even less informative.

The dominant-fan ratios are likewise not yet a dangerous-regime test.  At
three of the four fixtures the maximizing degree product is already below
`D`, so boundedness of

```text
|U||V|/(D+R_U R_V)
```

is automatic without any line theorem.  The only product above `D` is
`126=1.34D` at `q=11801,U=44`, still only constant excess.  No fixture tests
what happens when `|U||V|/D` grows polynomially.

## 2. Line cover can be polynomial without the full physical mask

The transformed determinant-strip grid in the dominant-fan reduction has

```text
|U|=|V|=h^2,       K asymp h^2,       maximum line occupancy=h.
```

Its exact minimum line cover is `h`: `h` parallel rows suffice and every
line contains at most `h` points.  Hence the cover is `K^(1/2)` and the
dominant-fan ratio grows like `K`.  Choosing the shell parameter polynomially
larger than `h` retains `K^2=o(q)`.  Consequently shell geometry, the
determinant strip, and all pointwise line-pair estimates permit polynomial
line cover.

There are two closer physical warnings:

* the width-one integer token strip at `q=200000,D=371` has 289 points,
  maximum line occupancy 18, and therefore needs at least 17 lines before
  the two hard completion diamonds are imposed;
* one exact full-integer dynamic self-orbit at the same scale decomposes into
  49 parallel affine translates.

Neither is a selected all-six-window dangerous star.  Conversely, no known
actual-prime-power or literal critical hard-window star has a polynomially
growing required cover.  That physical question is open.  It follows that
an unconditional `q^o(1)` line-cover theorem is both much stronger than the
finite evidence and unnecessary for safe stars.

## 3. Audit of the proposed one-arm square-root cap

No known fixture falsifies

```text
N_line <=sqrt(D) q^o(1)
```

for a small-height physical null line.  The strict integer null-line maxima
at `q=809,1400,3500,10000,20000` are respectively `4,3,4,7,7`, all below
`sqrt(D)`.  The largest log-window actual-prime-power line has 10 points at
`D=94`, only `1.031 sqrt(D)` with a fixed cutoff-dependent constant.  The
strict actual-prime-power scans contain no rich lines.

Thus the coefficient-one inequality `N<=sqrt(D)` is already false in one
fixed log-window fixture, but the asserted `N<<sqrt(D)q^o(1)` scale is not.
None of the data distinguishes a fixed constant from a subpower loss.

The physical affine transition grid is sharp in exponent but cannot make an
asymmetric counterexample.  In its first coordinate write

```text
u=2i, v=2j+2,
(m-u-v)(m+u)(m+v)
 =m^3-m(u^2+uv+v^2)-uv(u+v).
```

Since `q=2m`, the literal hard window forces

```text
D >=4(u^2+uv+v^2)+O(uv(u+v)/m).
```

Therefore every affine side length is `O(sqrt(D))`, even after deleting the
opposite arm down to one point.  More generally, the already proved
quadratic-curvature identity gives the same conclusion for every
affinely-witnessed line.  Here is the direct one-arm argument, which makes
the asymmetry issue explicit.  Parametrize a primitive projected line by

```text
(d,E)=(d0,E0)+t(p1,p2),             x=alpha+beta*t.
```

Write `beta=a/h` in lowest terms.  Integrality of the selected witnesses
puts every selected `t` in one residue class modulo `h`, so after
`t=t0+h*n` the witness slope is the integer `a`.  If `a!=0`, at least one of

```text
x*b*d,                       x*B*E
```

is a genuine quadratic in `n`, with normalized quadratic coefficient
containing the nonzero integer `a*h*p_i`.  Since the fixed shell factor
`b` or `B` is comparable to `q`, confinement to a raw interval of length
`O(qD)` gives

```text
# selected n << sqrt(D/|a*h*p_i|)+1 <<sqrt(D)+1.
```

This remains true for a sparse set of `n`: the inverse image of a bounded
interval under a nonconstant quadratic is the union of at most two
intervals of this total scale.  If `a=0`, a varying projected coordinate
makes one product linear with coefficient comparable to `q^2`; because
`D=o(q)`, only `O(1)` lattice parameters survive.  The proof uses no point
from the opposite arm.  Consequently lengths `(L,1)` with
`L>>sqrt(D)q^o(1)` are impossible in the affine-witness class, and an
affine `(L,M)` family obeys each of `L,M<<sqrt(D)`, not merely `LM<<D`.

Any super-square-root counterexample must therefore have genuinely
non-affine remote witnesses; asymmetric deletion of the known affine grid
cannot provide it.

## 4. Most discriminating experiment for the line-based RDP route

Use the exact rational-ray parametrization underlying the literal `q=809`
remote example.  For fixed coprime small `r<s`, put

```text
b=r g-1,       B=s g-1,
c=s h-1,       C=r h-1,
d_z=s z-1,     D_z=r z-1,
e_w=r w-1,     E_w=s w-1.
```

Then, identically,

```text
b d_z-B D_z=(s-r)(g-z),
c e_w-C E_w=(s-r)(w-h),
d_z e_w-D_z E_w=(s-r)(w-z),
```

and the two line directions `(s,r),(r,s)` are null-dual with stationary
heights `h_U=s-r`, `h_V=r-s`.  Taking consecutive `r,s` produces the hardest
possible nonzero heights `+1,-1`.  The `q=809` certificate is exactly
`(r,s,g,h)=(8,9,49,50)` with selected non-affine witness hits on these rays.

The proposed experiment should scale `g,h,q`, enumerate only these two
one-dimensional rays, and apply the exact hard-completion map on the full
integer and actual-prime-power masks.  Record:

1. selected population divided by `sqrt(D)` on each ray;
2. the number of maximal affine witness runs (“bends”);
3. the two-arm product divided by `D`;
4. the dominant-fan ratio and neighborhood-degree/spectral quantities.

This is more discriminating than another broad finite graph **for the
one-line theorem**: it fixes all four coefficients at their smallest values,
directly enters the remote selected-divisor core, and costs only a
one-dimensional scan.  A family with `N/sqrt(D)>=q^delta`, or polynomially
many genuine witness bends, falsifies that local route.  A physical lift of
the transformed `h by h` grid would falsify whole-star RDP outright.

It is not, however, the most discriminating experiment for the sharp
four-cycle target.  A generic `R`-rich partner may use `R(R-1)` distinct
secants, with no three completions on a rich line.  Every rational-ray test
could therefore pass while the anchored degree sum still fails.

## 5. The strictly weaker sharp target and its finite audit

For a fixed residual anchor `gamma`, put

```text
r_gamma(eta)=#{p:p~gamma and p~eta},
P_gamma(R)=#{eta:R<=r_gamma(eta)<2R}.
```

The operator only needs the dyadic anchored Carleson estimate

```text
R*P_gamma(R) <<Dq^o(1),
```

and the coherent/parabolic weighted high tail is already closed.  The exact
remaining main node is its generic/scattered part `(GACCT_R)` (cardinally
`(GP_R)`) in

```text
deg(gamma)>>D^(1/4),
q^o(1)<<R<<min(sqrt(D),deg(gamma)^2/sqrt(D)).
```

This target permits double stars on which edgewise RDP fails by a power.
Thus neither a one-arm cap nor a whole-star degree product is necessary.

An exact sparse-Gram audit of the four materialized actual-prime-power graphs
shows that the current finite evidence is also vacuous for this sharper
question:

| fixture | max off-diagonal codegree | max `W(gamma)/D` | best dyadic `R` |
|---|---:|---:|---:|
| `q=11801,U=35` | 4 | `39/94=.415` | 1 |
| `q=11801,U=44` | 4 | `63/94=.670` | 1 |
| `q=25013,U=40` | 6 | `37/135=.274` | 1 |
| `q=50021,U=40` | 4 | `33/189=.175` | 1 |

Every maximizing dyadic bin is in the already harmless bounded-`R` range.
The large full-integer central fixture has `W/D` near `.8`, but all its mass
is coherent on reflected parallel token lines and belongs to the already
closed weighted branch.  Neither family probes generic power-rich partners.

The highest-information next experiment is therefore a growing **generic
weighted-chain stratification**, not another cover count:

1. form all `r_gamma(eta)` and retain only the unresolved dyadic `R` range;
2. apply the exact successive-minima dichotomy and remove the certified
   coherent/parabolic contribution;
3. for every remaining partner, enumerate ordered completion secants and
   record distinct-secant count, maximum secant multiplicity, pinned tag,
   reciprocal height, and physical factorial weight;
4. measure both `R*P_gamma^gen(R)/D` and the corresponding weighted
   `(AF_2)/(AF_3)` or `(SRH_R)` chain load;
5. target the hostile Sidon regime with `asymp R^2` distinct secants and no
   rich line, scaling until `R` itself is a power rather than at most six.

The ambient width-one token strip with 289 points and 344 directions is a
better seed for this search than a single ray: impose both hard diamonds,
then optimize the surviving generic anchored tail.  A physical family with
`R P_gamma^gen(R)/D>=q^delta` falsifies the sharp route directly.  Conversely,
uniform decay after the coherent peel supplies evidence at the exact missing
quantifier.

## 6. Corrected ranking

1. **Main project node: generic anchored Carleson/weighted-chain tail.**
   Attack `(GACCT_R)/(GP_R)` or its tagged-trace square-function equivalent
   on growing power-rich fixtures.  This is the weakest known sufficient
   theorem and exactly matches the unclosed operator sector.
2. **Parallel fast falsifier: small-height rational rays.**  They remain the
   quickest way to kill the useful one-arm lemma, but success there does not
   control scattered Sidon partners and cannot close the proof.
3. **Fallback: mask-sensitive translate-Bessel/tagged-trace theorem.**  This
   can exploit orthogonality among polynomially many secants, which a line
   cover discards; it is naturally aligned with the weighted generic tail.
4. **Deprioritize whole-star RDP and unconditional line cover.**  They impose
   an unnecessary edgewise quantifier, are not supported by the bounded
   finite data, and still bundle the selected-divisor and aggregation gates.
5. **Deprioritize global affine-Carleson allocation.**  It retains the known
   host, overlap, and completion-consistent rounding problems.

So the rational-ray experiment outranks a broad cover scan as a local kill
test, but it does **not** outrank a properly targeted, growing
`(GP_R)`/weighted-chain stratification for progress toward the sharp bound.

Finite anchored-tail replay:

```text
python3 results/verify_zeta23_qp_gp_tail_finite_affine_falsifier.py
```
