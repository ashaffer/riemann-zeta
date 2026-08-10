# Long-mollifier zero-free-strip sprint

Status: **conditional strip gate proved at the exponent-arithmetic level; exact
finite coefficient identities proved and tested; the required mollified-moment
estimate remains OPEN.**

Date: 2026-08-09.

This note does **not** prove a new zero-free strip or the Riemann Hypothesis.
It replaces the previous completed fourth-moment target by a second, graduated
target whose arithmetic input is a long reciprocal mollifier.  The point is
not that this input is known.  The point is that a mollifier only slightly
longer than the height already forces a fixed strip, and the first coefficient
barrier can be stated exactly.

## 1. The theorem card

For `y>1`, put

```text
M_y(s) = (1/log y) sum_(d<=y) mu(d)d^(-s) log(y/d),

I_y(0,T) = integral_0^T
  |zeta(1/2+it) M_y(1/2+it)|^2 dt.
```

Fix `theta>1`.  The target is

```text
LM(theta):
for every epsilon>0,

integral_1^(T^theta) I_y(0,T) dy
  <<_epsilon T^(theta+1+epsilon).                       (1.1)
```

The exponent `theta+1` is the natural scale: one power of `T` from the
critical-line mean square and `theta` powers from averaging the cutoff
`1<=y<=T^theta`.

### Conditional strip theorem

If `LM(theta)` holds, then

```text
zeta(s) != 0 when
Re(s) > (theta+1)/(2 theta)
      = 1 - (theta-1)/(2 theta).                         (1.2)
```

By the functional equation, every nontrivial zero then lies in

```text
(delta_theta <= Re(rho) <= 1-delta_theta),

delta_theta = (theta-1)/(2 theta) > 0.                  (1.3)
```

#### Proof ledger

Dong--Wattanawanichkul--Zaharescu, Theorem 1.3, states that

```text
sup_(T>=1) T^(-2 sigma theta)
  integral_1^(T^theta) I_y(0,T) dy < infinity            (1.4)
```

implies nonvanishing in `Re(s)>sigma`.  Given (1.1), choose any

```text
sigma > (theta+1)/(2 theta).
```

Then

```text
2 sigma theta > theta+1,
```

so a sufficiently small `epsilon` in (1.1) makes (1.4) hold.  Letting
`sigma` decrease to the displayed boundary gives (1.2).  Bettin--Gonek's
original proof contains the same exponent comparison; their pointwise
hypothesis on every `I_N` is stronger than the cutoff-averaged hypothesis
used here.

The Lean module

```text
RHBridge.LongMollifierStripReduction
```

formalizes this exponent arithmetic only.  It deliberately does not import
(1.1) as an axiom.

## 2. Graduation table

| `theta` | target exponent | right zero boundary | strip width `delta` |
|---:|---:|---:|---:|
| `1.01` | `2.01` | `0.995049505...` | `0.004950495...` |
| `1.10` | `2.10` | `0.954545454...` | `0.045454545...` |
| `1.25` | `2.25` | `0.9` | `0.1` |
| `1.50` | `2.50` | `5/6` | `1/6` |
| `2` | `3` | `3/4` | `1/4` |

Equivalently, a desired width `0<delta<1/2` asks for

```text
theta = 1/(1-2 delta).                                  (2.1)
```

Thus the smallest meaningful milestone is not an arbitrarily long mollifier.
It is any fixed overlength

```text
theta=1+eta,  eta>0,                                    (2.2)
```

which would give

```text
delta = eta/[2(1+eta)].                                 (2.3)
```

## 3. Exact coefficient ledger on the absolute-convergence side

For `Re(s)>1`, multiplication of the absolutely convergent Dirichlet series
gives

```text
zeta(s) M_y(s) = sum_(n>=1) c_y(n)n^(-s),               (3.1)

c_y(n) = (1/log y)
  sum_(d|n, d<=y) mu(d) log(y/d).                        (3.2)
```

This identity is **not** permission to use (3.1) directly on the critical
line.  Any proof of (1.1) must pass through a valid approximate functional
equation, Mellin formula, or equivalent completed representation.

Define the late-divisor correction

```text
R_y(n) = sum_(d|n, d>y) mu(d) log(d/y).                  (3.3)
```

Using

```text
sum_(d|n) mu(d) log(n/d) = Lambda(n),                    (3.4)
```

one obtains, for every `n>1`,

```text
c_y(n) = [Lambda(n)+R_y(n)]/log y.                       (3.5)
```

This is the first important structural point.  The prime-power head and the
late-divisor correction form one completed coefficient.  They must not be
estimated as unrelated positive sectors.

### 3.1 The complete head

For `2<=n<=y`, no divisor is omitted, hence

```text
c_y(n)=Lambda(n)/log y.                                  (3.6)
```

### 3.2 The first overlength band

For

```text
y<n<=2y,                                                (3.7)
```

every proper divisor of `n` is at most `n/2<=y`.  The only possible omitted
divisor is `n` itself.  Therefore

```text
c_y(n)
 = [Lambda(n)+mu(n)log(n/y)]/log y.                      (3.8)
```

For non-prime-powers in this band, the coefficient is exactly a tapered
Möbius value.

### 3.3 Sharp stress model

For the sharp reciprocal truncation

```text
S_Y(s)=sum_(d<=Y)mu(d)d^(-s),
```

write

```text
zeta(s)S_Y(s)=sum_n a_Y(n)n^(-s),

a_Y(n)=sum_(d|n,d<=Y)mu(d).                              (3.9)
```

Then exactly

```text
a_Y(1)=1,
a_Y(n)=0                     (2<=n<=Y),
a_Y(n)=-mu(n)                (Y<n<=2Y).                 (3.10)
```

The sharp truncation is a **stress model**, not automatically a mollifier to
which the source theorem applies.  Its role is to expose the first arithmetic
scale without the logarithmic taper.

All identities in this section are implemented and regression-tested in

```text
src/long_mollifier_strip_gate.py
src/test_long_mollifier_strip_gate.py.
```

## 4. The first resolution barrier

A height window of length `T` resolves logarithmic frequencies at spacing
about `1/T`.  At coefficient scale `Y`, this corresponds to an additive
window

```text
H=Y/T.                                                   (4.1)
```

For `Y=T^theta`,

```text
H=T^(theta-1)
 =Y^(1-1/theta)
 =Y^(2 delta_theta).                                     (4.2)
```

Thus, in the sharp first-band stress model, the width `delta` is paired with
Möbius intervals of length `Y^(2 delta)`.

A square-root mean-square benchmark would be

```text
integral_Y^(2Y)
  |sum_(x<n<=x+H) mu(n)|^2 dx
  << Y H Y^o(1).                                         (4.3)
```

Current Matomäki--Radziwiłł technology, including Menon's 2026 refinement,
gives for Liouville and analogously for Möbius a normalized estimate of the
shape

```text
(1/Y) integral_Y^(2Y)
 |(1/H)sum_(x<n<=x+H)mu(n)|^2 dx
 << (log log H/log H)^2 + logarithmic errors.             (4.4)
```

After clearing the normalization, (4.4) is of order

```text
Y H^2 (log log H/log H)^2,                               (4.5)
```

whereas (4.3) is of order `YH`.  The missing factor is a full power of the
short length `H`, up to logarithms.  Consequently, qualitative cancellation
in almost all short intervals does not by itself cross the long-mollifier
length barrier.

This comparison is a fail-fast test for any proof that first bounds each
Möbius collar separately.  It is **not** a proof that the completed mollified
moment cannot exploit cancellation between the prime head, late-divisor
correction, approximate-functional-equation dual, and cross terms.

## 5. The completed target, not a sector bound

The target (1.1) concerns

```text
zeta(1/2+it) M_y(1/2+it)
```

as one completed object.  A correct arithmetic reduction must retain:

1. the `Lambda(n)` head in (3.5);
2. the entire late-divisor correction `R_y(n)`;
3. boundary divisors at every hyperbola cutoff;
4. both halves of a smoothed approximate functional equation;
5. all cross terms between those halves;
6. the cutoff average in `y` with its exact kernel.

The repository's previous fixed-window work found repeatedly that separating
a discrete tail from its center destroys the cancellation one is trying to
prove.  The same warning applies here.  In particular, neither (4.3) nor a
sectorwise estimate for `R_y` is the final theorem.

The next exact analytic object to freeze is a smoothed AFE/Gallagher identity
of the schematic form

```text
integral_(Y/2)^Y I_y(0,T) dy
 = diagonal + completed shifted-product form + controlled AFE remainder,
                                                               (5.1)
```

where the completed shifted-product form keeps the two AFE halves and the
cutoff kernel together.  Only after (5.1) is proved should dispersion,
large-sieve, or short-interval estimates be applied.

## 6. Immediate research program

### Gate A: completed AFE identity

Choose one fixed smooth `t/T` weight and one smooth terminal cutoff average
`y/Y`.  Derive an unconditional identity for the weighted version of (5.1),
with every contour shift, dual sum, and remainder explicit.  Do not use a
zero-free strip in the error analysis.

### Gate B: exact cutoff kernel

After expanding the two mollifiers, compute the positive cutoff Gram kernel

```text
K_Y(d,e)=integral W(y/Y)
  1_(d<=y)1_(e<=y)
  log(y/d)log(y/e)/(log y)^2 dy.                         (6.1)
```

Record its diagonal, first differences, and dyadic localization.  The
unweighted average is dominated by terminal `y`, so no large saving should be
claimed from cutoff averaging alone.

### Gate C: completed dispersion

Apply divisor switching only after combining the prime head and late-divisor
correction.  The candidate gain must be a power `T^eta`, not merely a power of
`log T`.  Any Cauchy step that replaces Möbius signs by divisor magnitudes is
to be rejected immediately.

### Gate D: first-band falsification

Before a proposed completed estimate is trusted, test it on the exact bands
(3.6)--(3.10).  A proof that implicitly requires (4.3) should state that
requirement openly; current short-interval theorems do not provide it.

### Gate E: source-theorem audit

Reprove the zeta specialization of the averaged criterion in the repository,
starting from Bettin--Gonek's Mellin argument, so that the exact smoothing,
`[0,T]` quantifier, logarithmic factors, and boundary line are frozen.  This is
a literature theorem, not the new arithmetic input.

## 7. What would count as progress

The milestones are strictly ordered:

1. **Exact reduction:** prove the completed AFE identity (5.1).
2. **Logarithmic saving:** useful diagnostically but insufficient for a fixed
   strip.
3. **Any fixed power gain:** enough to choose some `theta>1` and obtain a
   genuine fixed strip.
4. **Natural bound for unbounded theta:** would approach RH through the
   long-mollifier criterion.

At present the project is at milestone 1 for this route: the strip conversion
and finite coefficient algebra are clean, while the completed critical-line
moment estimate is open.

## 8. Primary sources

- S. Bettin and S. M. Gonek, *The theta=infinity conjecture implies the
  Riemann hypothesis*, Mathematika 63 (2017), 29--33; arXiv:1604.02740.
- A. Dong, N. Wattanawanichkul, and A. Zaharescu, *The theta=infinity
  Conjecture and the Riemann Hypothesis for Automorphic L-functions*,
  arXiv:2605.24363, 2026; especially Theorem 1.3.
- M. Radziwiłł, *Limitations to mollifying zeta(s)*, IMRN 2014;
  arXiv:1207.6583.
- K. Matomäki and M. Radziwiłł, *Multiplicative functions in short
  intervals*, Annals of Mathematics 183 (2016), 1015--1056.
- S. Menon, *Improved bounds for multiplicative functions in almost all short
  intervals*, arXiv:2607.15574, 2026.
