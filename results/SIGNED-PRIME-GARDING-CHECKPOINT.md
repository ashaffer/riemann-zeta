# Signed prime Gårding checkpoint for localized zeta Weil forms

## Status and verdict

This note does **not** prove RH.  It identifies the exact arithmetic inequality
left after the prime main term is cancelled against the zeta pole, and it
separates three statements which should not be conflated:

1. the minimal compressed endpoint estimate is RH-equivalent when the strip
   width is zero;
2. at the zero-width/subexponential endpoint, a positive logarithmic-energy
   reserve is stronger and forces a new little-`o` bound on consecutive zero
   gaps;
3. the corresponding pointwise endpoint estimate is false at the required
   scale, even though its Paley--Wiener compression may be positive.

The main useful reduction is a one-sided relative bound for one explicit
oscillatory von Mangoldt discrepancy.  Ordinary prime-counting error and
Selberg smoothing do not prove it.  This is a sharper stopping point than the
earlier statement that Abel summation merely loses a half derivative.

## 1. Exact completed multiplier and the pole sign

Put

```text
U = 2a,   X = exp(U),
F(t) = integral_R f(x) exp(-itx) dx,
supp(f) subset (-a,a).
```

The localized zeta Weil form is

```text
Q_a(f) = (1/(2 pi)) integral_R |F(t)|^2 Omega_U(t) dt,           (1.1)
```

where

```text
Omega_U(t)
  = Re psi(1/4+it/2) - log pi
    - 2 sum_(log n<U) Lambda(n)n^(-1/2) cos(t log n)
    + p_U(t),                                                    (1.2)

p_U(t)
  = 4 integral_0^U cosh(u/2) cos(tu) du
  = [2 sinh(U/2) cos(tU)+4t cosh(U/2) sin(tU)]/(t^2+1/4).        (1.3)
```

The sign in (1.3) is positive.  This follows directly from the pole part of
the Weil functional,

```text
integral c_f(u)(exp(u/2)+exp(-u/2)) du,
```

and from Fourier inversion.  It also follows from equation (205) of Suzuki's
2026 preprint, where the remainder enters as `-r''`.  The displayed plus sign
in that paper's equation (207) is inconsistent with both equation (205) and
the subsequent calculation

```text
Fourier(r_1'') = -Re psi(1/4+it/2)+log|t|-log 2:
```

the final `+Re psi` formula requires subtracting this transform.  Thus the
safe normalization is (1.2)--(1.3), independently checked by the plus-signed
rank-two pole term.  (That rank-two form is itself indefinite.)  See Suzuki,
[*Weil's quadratic form via the screw function*](https://arxiv.org/abs/2606.09096).

## 2. Exact prime-main cancellation

Let

```text
A_infinity(t) = Re psi(1/4+it/2)-log pi,
m_U(t) = 2 integral_0^U exp(u/2) cos(tu) du,
b_U(t) = 2 integral_0^U exp(-u/2) cos(tu) du.                    (2.1)
```

Then `p_U=m_U+b_U` and `|b_U|<=4`.  With

```text
Psi(x) = sum_(n<=x) Lambda(n),
R(x) = Psi(x)-x,
r_U(t) = 2 Re integral_(1-)^X x^(-1/2-it) dR(x),                (2.2)
```

the prime multiplier is exactly `m_U+r_U`.  Therefore

```text
Omega_U = A_infinity + b_U - r_U.                               (2.3)
```

This identity keeps the exponentially large prime and pole pieces together;
separate absolute values erase the cancellation.

Define the logarithmic energy

```text
E(f) = (1/(2 pi)) integral log(1+t^2)|F(t)|^2 dt.                (2.4)
```

The classical vertical-line digamma estimates give

```text
A_infinity(t) = (1/2)log(1+t^2)+O(1)                            (2.5)
```

with a uniform two-sided `O(1)`.  Consequently, for fixed `c>=0`,

```text
Q_a(f) >= c E(f)-C_eta X^(Delta+eta)||f||_2^2                   (2.6)
```

is equivalent, after changing only bounded constants, to

```text
(1/(2 pi)) integral r_U(t)|F(t)|^2 dt
  <= (1/2-c)E(f)+C_eta X^(Delta+eta)||f||_2^2                   (PG)
```

for every `F` in `PW_(U/2)`.  In time coordinates this is

```text
2 Re integral_0^U c_f(u) exp(-u/2) d(Psi(exp u)-exp u)
  <= (1/2-c)E(f)+C_eta X^(Delta+eta)||f||_2^2.                  (PG-time)
```

This is the exact prime-only gate.  It is a compressed multiplier inequality;
a pointwise inequality for `r_U` or `Omega_U` is sufficient but not necessary.

## 3. The endpoint is RH-equivalent

At `Delta=0` and `c=0`, write the endpoint as

```text
(1/(2 pi)) integral r_U |F|^2
  <= (1/2)E(f)+C_eta X^eta||f||_2^2                             (PG_0)
```

for every `eta>0`, every `U`, and every `F in PW_(U/2)`, with `C_eta`
independent of `U` and `F`.

### Proposition 3.1

`(PG_0)` is equivalent to RH.

### Proof

Under RH, Weil positivity gives `Q_a>=0`.  Equations (2.3), (2.5), and
`|b_U|<=4` give `(PG_0)` with an `O(1)` remainder.

Conversely, `(PG_0)` and the lower half of (2.5) give

```text
Q_a(f) >= -C_eta exp(eta U)||f||_2^2.
```

Since `U=2a` and `eta` is arbitrary, the localized negative floors are
subexponential in `a`.  The quantitative two-bump/cardinal-interpolation
theorem in `QUANTITATIVE-WEIL-FLOOR-DIVERGENCE.md` says that any off-line zero
would force exponential floor decay.  Hence RH follows.  QED.

This proposition is a quantifier audit, not a proof of `(PG_0)`.  It shows
that the missing one-sided prime-discrepancy estimate contains exactly the RH
barrier at its endpoint.

For a positive actual strip width `Delta`, the analogous endpoint estimate
is the minimal target for the reverse floor exponent.  A strict reserve
`c>0` is unnecessary for that purpose.

## 4. The triangular Selberg gate

Take the normalized modulated interval

```text
f_(tau,U)(x)=U^(-1/2) exp(i tau x) 1_[-U/2,U/2](x).
```

It belongs to the logarithmic form domain and

```text
c_f(u)=(1-|u|/U)_+ exp(-i tau u),
E(f_(tau,U))=log(1+tau^2)+O(1),                                 (4.1)
```

uniformly in `tau` and `U>=1`.  Thus `(PG)` necessarily implies

```text
2 Re [
  sum_(n<X) Lambda(n)n^(-1/2-i tau)(1-log n/U)
  - integral_1^X x^(-1/2-i tau)(1-log x/U) dx]
 <= (1/2-c)log(1+tau^2)+C_eta X^(Delta+eta).                    (4.2)
```

This is a concrete scalar fail-fast test.  The standard strip consequence

```text
R(x)=O_eta(x^(1/2+Delta+eta))
```

still yields only

```text
O_eta((1+|tau|)X^(Delta+eta))                                   (4.3)
```

by Abel summation: differentiating the oscillatory Mellin factor costs
`|tau|`.  Higher-order cutoffs do not remove that derivative by themselves.

Selberg's logarithmically weighted explicit formula makes the sign more
visible.  Its zero kernel, in a compatible convention, is

```text
K_U(z)=1/z+(1-exp(Uz))/(U z^2).                                 (4.4)
```

On RH, `z=iy` and

```text
Re K_U(iy)=[cos(Uy)-1]/(U y^2) <= 0.                            (4.5)
```

This proves the endpoint coefficient for the triangular tests *under RH*;
it does not prove RH or lift automatically to every Paley--Wiener vector.
Off-line symmetric pairs make (4.5) sign-indefinite, with an
`exp(Delta U)` factor and a local horizontal-displacement remainder.  Current
global zero-density estimates control its mean but not its worst unit window.

The kernel and normalization can be read from Lemma 1 of Soundararajan,
[*Moments of the Riemann zeta function*](https://annals.math.princeton.edu/wp-content/uploads/annals-v170-n2-p17-p.pdf).
Simonič's
[*Explicit zero density estimate near the critical line*](https://arxiv.org/abs/1910.08274)
is global and does not supply the missing local signed bound.  The audited
Selberg-moment, de la Vallee Poussin, and Stechkin variants either assume RH,
mix other abscissae/heights, or lose the needed leading coefficient.

## 5. Why the pointwise endpoint is the wrong target

At the already certified support `a=7/16`, only the prime power `2` is active
and direct evaluation gives

```text
Omega_(7/16)(0) = -2.73971447387.                               (5.1)
```

Nevertheless, the existing unrestricted certificate proves that the
`PW_(7/16)` form floor is greater than `2.2699e-5`.  Thus pointwise
nonnegativity of this natural multiplier is decisively false while the
compressed form is positive.

There is also an exact asymptotic obstruction.  Put

```text
B_a=2 sum_(log n<2a) Lambda(n)n^(-1/2).
```

The logarithms of the finitely many active primes are rationally independent.
Kronecker recurrence therefore gives `t_j->infinity` for which every active
prime phase tends to zero.  Since `p_(2a)(t_j)->0` and

```text
A_infinity(t)-(1/2)log(1+t^2) -> -log(2 pi),
```

we obtain

```text
Omega_(2a)(t_j)-(1/2)log(1+t_j^2)
  -> -B_a-log(2 pi).                                            (5.2)
```

The prime number theorem gives `B_a~4 exp(a)`.  Hence any pointwise endpoint
bound with the full principal coefficient `1/2` needs an exponentially large
remainder, even under RH.  Paley--Wiener compression is load-bearing, not a
technical nuisance.

A one-thread numerical scout is provided in
[`signed_garding_failfast.py`](../src/signed_garding_failfast.py).  It uses the
plus pole sign and chunks the finite prime-power phases.  Some sampled
values are:

| `a` | `B_a` | `p_(2a)(0)` | `Omega_(2a)(0)` |
|---:|---:|---:|---:|
| `0.4375` | `0.9803` | `3.6127` | `-2.7397` |
| `1` | `5.8525` | `9.4016` | `-1.8230` |
| `2` | `24.3833` | `29.0149` | `-0.7406` |
| `3` | `75.1905` | `80.1430` | `-0.4197` |
| `4` | `213.5475` | `218.3193` | `-0.6004` |
| `5` | `588.0245` | `593.6257` | `0.2290` |

Sparse frequency scouts find deeper negative values, but they are diagnostics,
not global minima or certificates.  Subleading pointwise inequalities with
coefficient strictly below `1/2` survive this particular recurrence test;
proving one would require a new uniform large-values theorem for the prime
Dirichlet polynomial.

## 6. A strict reserve forces a new zero-gap theorem

At the `Delta=0` endpoint, the originally proposed target included a fixed
`c>0`.  That reserve is not a harmless convenience.

### Theorem 6.1

Suppose there is `c>0` such that, for every `epsilon>0`,

```text
Q_a(f) >= c E(f)-C_epsilon exp(epsilon a)||f||_2^2              (6.1)
```

for all compactly supported smooth `f`.  Then RH holds and, for consecutive
positive zero ordinates counted with multiplicity,

```text
(gamma_(n+1)-gamma_n) log log gamma_n -> 0.                     (6.2)
```

### Proof

The endpoint part of (6.1) implies RH by Proposition 3.1, so

```text
Q_a(f)=sum_gamma m_gamma |F(gamma)|^2.                           (6.3)
```

Assume that gaps of length `H>=h/log log T` occur at arbitrarily large
midpoints `T`, for some `h>0`.  Fix a unit `L2` bump `phi` supported in
`(-1,1)`, put `W=|phihat|^2`, choose `K>1`, and set

```text
a=2K/H,
f_(T,a)(x)=a^(-1/2) phi(x/a) exp(iTx).                           (6.4)
```

The central Fourier region `|a(t-T)|<K` lies in the zero-free gap.  If

```text
A(K)=integral_(|y|>=K) W(y)dy,
V(K)=W(K)+W(-K)+integral_(|y|>=K)|W'(y)|dy,
```

then Stieltjes integration against the Riemann--von Mangoldt formula and the
RH bound `S(T)=O(log T/log log T)` gives

```text
Q_a(f_(T,a))
 <= log T [A(K)/(2 pi)+(2 C_S K/h)V(K)]+o(log T).               (6.5)
```

Only the Schwartz tail outside the gap is integrated, so the `S`-term costs
`aV(K)`, not the variation of the whole packet.  Choose `K` so that the
bracket in (6.5) is less than `c`.  On the other hand,

```text
E(f_(T,a))=2 log T+O(1),
a<=(2K/h)log log T.                                             (6.6)
```

Choose a fixed `epsilon<h/(2K)`.  Then the error in (6.1) is `o(log T)`,
so (6.1) and (6.6) give `Q_a>=2c log T-o(log T)`, contradicting
(6.5).  This excludes every fixed `h>0` and proves (6.2).  QED.

The `S(T)` input is available from Carneiro, Chandee, and Milinovich,
[*Bounding S(t) and S_1(t) on the Riemann hypothesis*](https://arxiv.org/abs/1309.1526).
The theorem does not logically separate (6.1) from RH: RH might imply (6.2)
by an unknown argument.  It does show that `c>0` adds a genuine sampling/gap
problem beyond the minimal endpoint, improving the standard RH consequence
`gap=O(1/log log T)` to little-`o`.

## 7. Revised target and completed packet-cone checkpoint

For the reverse floor exponent, the minimal target is now

```text
(1/(2 pi)) integral r_U |F|^2
 <= (1/2)E(f)+C_eta X^(Delta+eta)||f||_2^2,                     (7.1)
```

on `PW_(U/2)`.  At `Delta=0` it is exactly RH-equivalent.  A proof must use
one of two genuinely new inputs:

1. a signed Toeplitz/Paley--Wiener domination that lifts the Selberg zero
   kernel without replacing the compression by a pointwise bound; or
2. a strict subleading pointwise estimate proved by a uniform large-values
   theorem for the completed prime Dirichlet polynomial.

The first possibility has now passed through its proposed fail-fast test, and
the generic lift is **false**.  Positivity on every modulated interval packet,
even for every width and position, does not imply positivity of the full
compressed Toeplitz form.  The failure occurs already for a `3 x 3` Toeplitz
matrix, for a shifted-atom convolution operator, and for a real-even entire
rank-three kernel.  The exact countermodels and the Lean-checked scalar
algebra are in `TRIANGULAR-PACKET-CONE-NOGO.md` and
`RHBridge.SelbergPacketConeNoGo`.

The missing datum is coherent interference between separated packets.  A
particularly clean zeta-specific survivor is obtained from one fixed box

```text
g_ell=ell^(-1/2)1_[-ell/2,ell/2].
```

Its translated cross correlation has sinc-squared zero coefficients.  Those
coefficients are absolutely summable and vanish only at real nodes.  Hence

```text
limsup_(R->infinity)
  log(1+|Q_W(T_(-R/2)g_ell,T_(R/2)g_ell)|)/R
    = sup_rho |Re(rho)-1/2|.                                  (7.2)
```

Equivalently, RH is the boundedness of one explicit fixed-log-width
triangular von Mangoldt discrepancy.  The theorem, exact prime-side formula,
and proof are in `FIXED-BOX-WEIL-WIDTH-SPECTROMETER.md`.  This is a sharper
scalar reduction, not a proof of the required bound.  The next arithmetic
checkpoint is whether that discrepancy has an independently bounded renewal,
coboundary, or completed-positive representation.  Testing more diagonal
triangles cannot supply it.

## 8. Reproduction

The lightweight audit uses no zero tables and no RH assumption:

```text
cd src
env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
    MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1 \
    python3 -m unittest test_signed_garding_failfast.py

cd ..
env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
    MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1 \
    python3 src/signed_garding_failfast.py --supports 0.4375,1,2
```

The tests check the pole normalization, the first prime window, the negative
pointwise value (5.1), and scalar/vector agreement.  Sampled minima remain
diagnostic only.  The exact reductions, RH equivalence, recurrence theorem,
and zero-gap implication are analytic arguments requiring conventional
review; they are not certified by the script.
