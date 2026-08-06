# A fixed-box Weil width spectrometer

## Status and verdict

This note proves an unconditional analytic reduction from the classical
Guinand--Weil explicit formula.  It does **not** prove RH.

For every one fixed length `ell>0`, a single translated triangular test
detects the full horizontal width of the nontrivial zeta divisor.  More
precisely, an explicitly normalized fixed-log-width von Mangoldt discrepancy
`D_ell(R)` satisfies

```text
limsup_(R->infinity) log(1+|D_ell(R)|)/R
  = sup_rho |Re(rho)-1/2|.                                   (0.1)
```

Consequently, for any fixed `ell>0`,

```text
RH
  <=> D_ell(R) is bounded for R>=R_0
  <=> D_ell(R) has subexponential growth.                     (0.2)
```

The point of the result is compression, not an RH proof: the all-test Weil
criterion is reduced to one elementary prime discrepancy, but proving that
discrepancy bounded is still RH-equivalent.  The argument is a direct
fixed-kernel refinement of the translated-cross-correlation pole method in
`QUANTITATIVE-WEIL-FLOOR-DIVERGENCE.md`.  No novelty claim is made without a
broader prior-art review.

This is also the precise survivor of the triangular-packet cone no-go.  The
diagonal values of individual interval packets do not determine a Toeplitz
form, but one separated-box cross term already retains every off-line zero.
The subsequent prime-only, coboundary, refinement, and `2 x 2` positivity
audit is in
[`FIXED-BOX-PRIME-TRANSFER-CHECKPOINT.md`](FIXED-BOX-PRIME-TRANSFER-CHECKPOINT.md).

## 1. Normalization and the one fixed test

Use

```text
fhat(z) = integral_R f(x) exp(i z x) dx,
z_rho   = (rho-1/2)/i.
```

If `rho=beta+i gamma`, then

```text
z_rho=gamma-i(beta-1/2),
|Im z_rho|=|beta-1/2|.
```

Write

```text
Delta = sup_rho |Re(rho)-1/2|.                               (1.1)
```

Zeros are counted with analytic multiplicity `m_rho`.  Fix `ell>0` and set

```text
g_ell(x) = ell^(-1/2) 1_[-ell/2,ell/2](x),
w_ell(u) = (g_ell * g_ell_tilde)(u)
         = (1-|u|/ell)_+.
```

Their entire transforms are

```text
G_ell(z) = 2 sin(ell z/2)/(sqrt(ell) z),
H_ell(z) = G_ell(z)^2
         = 4 sin^2(ell z/2)/(ell z^2),                        (1.2)
```

with the removable values `G_ell(0)=sqrt(ell)` and
`H_ell(0)=ell`.  Every zero of `G_ell` or `H_ell` is real:

```text
z=2 pi k/ell,       k in Z\{0}.                               (1.3)
```

For `R>=0`, define the oriented separated-box cross correlation

```text
B_ell(R) = W(w_ell(.+R))
         = Q_W(T_(-R/2)g_ell,T_(R/2)g_ell).                   (1.4)
```

The opposite orientation is its Hermitian conjugate and has the same
absolute value.  The low-regularity issue is harmless here: `g_ell` belongs
to the logarithmic form domain, while `w_ell` is compactly supported and
piecewise linear.  Its transform has quadratic decay.

The explicit formula therefore gives the absolutely convergent zero-side
identity

```text
B_ell(R)
  = sum_rho m_rho H_ell(z_rho) exp(-i z_rho R).                (1.5)
```

Indeed, uniformly in the zeta strip,

```text
|H_ell(x+i y)| <= C_ell/(1+x^2),       |y|<=1/2,              (1.6)
```

and Riemann--von Mangoldt counting makes the right side of (1.5) absolutely
convergent.

## 2. Exact width theorem

### Theorem 2.1

For every fixed `ell>0`,

```text
limsup_(R->infinity) log(1+|B_ell(R)|)/R = Delta.              (2.1)
```

### Proof: upper bound

By (1.6) and zero counting,

```text
C_ell^* = sum_rho m_rho |H_ell(z_rho)| < infinity.             (2.2)
```

Since `|Im z_rho|<=Delta`, (1.5) gives, for `R>=0`,

```text
|B_ell(R)| <= C_ell^* exp(Delta R).                            (2.3)
```

This proves that the left side of (2.1) is at most `Delta`.

### Proof: lower bound

For `Im z>1/2`, termwise integration in (1.5) gives

```text
integral_0^infinity B_ell(R) exp(i z R) dR
  = i sum_rho m_rho H_ell(z_rho)/(z-z_rho).                   (2.4)
```

The right side is meromorphic, normally convergent away from the zero nodes.
Let `z_0` be a node with `Im z_0>0`.  It is nonreal, so (1.3) implies

```text
H_ell(z_0) != 0.                                              (2.5)
```

Thus (2.4) has a genuine pole at `z_0`; multiplicity multiplies its nonzero
residue and cannot cancel it.

If

```text
limsup_(R->infinity) log(1+|B_ell(R)|)/R < Im z_0,             (2.6)
```

then the integral on the left of (2.4) would extend holomorphically to a
half-plane containing `z_0`.  Meromorphic uniqueness would make the pole in
(2.4) removable, a contradiction.  Hence the limsup is at least
`Im z_0`.

The functional equation and conjugation symmetry put a node of positive
imaginary part at every positive horizontal displacement of a zeta zero.
Taking the supremum over such nodes gives the lower bound `Delta`, proving
(2.1).  No rightmost zero is required.  QED.

### Corollary 2.2

For every fixed `ell>0`, the following are equivalent:

1. RH;
2. `B_ell` is bounded on the positive half-line;
3. for every `epsilon>0`, `B_ell(R)=O_epsilon(exp(epsilon R))`.

Under RH the stronger boundedness statement follows directly from (2.2),
because every `z_rho` is real.  Conversely either growth condition and
Theorem 2.1 gives `Delta=0`.

## 3. Exact prime-side spelling

Put

```text
M_ell = 4 sinh(ell/4)/sqrt(ell).                              (3.1)
```

Thus `M_ell^2=16 sinh^2(ell/4)/ell`, equivalently
`8(cosh(ell/2)-1)/ell`.

For `R>ell`, the translated triangle in (1.4) is supported strictly on the
negative half-line and vanishes at zero.  Substitution into the
normalization-matched Weil formula gives

```text
B_ell(R)
 = M_ell^2 (exp(R/2)+exp(-R/2))
   - sum_n Lambda(n)n^(-1/2) w_ell(log n-R)
   - G_ell^arch(R),                                           (3.2)

G_ell^arch(R)
 = integral_(R-ell)^(R+ell)
     w_ell(u-R) e^(u/2)/(e^u-e^(-u)) du.                      (3.3)
```

Only integers with `exp(R-ell)<n<exp(R+ell)` contribute to the sum.
The plus sign of the pole term in (3.2) is essential.  Its coefficient is
checked directly by

```text
integral_(-ell)^ell w_ell(v)e^(v/2)dv
  = G_ell(-i/2)^2
  = M_ell^2.                                                   (3.4)
```

Define the pole-cancelled triangular von Mangoldt discrepancy

```text
D_ell(R)
 = sum_n Lambda(n)n^(-1/2)w_ell(log n-R)
   - M_ell^2 exp(R/2).                                        (3.5)
```

Equivalently, with `psi(x)=sum_(n<=x)Lambda(n)`,

```text
D_ell(R)
 = integral x^(-1/2)w_ell(log x-R) d(psi(x)-x).               (3.6)
```

Equations (3.2)--(3.5) say

```text
B_ell(R)
 = M_ell^2 exp(-R/2)-D_ell(R)-G_ell^arch(R).                  (3.7)
```

For fixed `ell`, the two correction terms on the right are
`O_ell(exp(-R/2))`.  Therefore Theorem 2.1 is equivalently the prime-side
identity announced in (0.1):

```text
limsup_(R->infinity) log(1+|D_ell(R)|)/R = Delta.              (3.8)
```

This proves (0.2).  Under RH, pairing the nodes `gamma` and `-gamma` also
shows that `D_ell` is, up to an exponentially decaying correction, an
absolutely and uniformly convergent cosine series.  In particular it is
asymptotically Bohr almost periodic.

The same identity can be written with the repository's archimedean
multiplier

```text
A_infinity(t)=Re psi(1/4+it/2)-log pi:

-G_ell^arch(R)
  = (1/(2 pi)) integral_R A_infinity(t)|G_ell(t)|^2 cos(tR)dt. (3.9)
```

This gives an independent Fourier/time-domain normalization check.

## 4. What the checkpoint does and does not solve

The packet-cone implication proposed in
`SIGNED-PRIME-GARDING-CHECKPOINT.md` is false.  Even all widths, positions,
and modulations of interval packets leave uncontrolled cross terms; exact
countermodels are in `TRIANGULAR-PACKET-CONE-NOGO.md`.

The present theorem identifies the smallest useful missing cross datum:

```text
one fixed box + arbitrary separation
    -> one fixed triangular prime discrepancy
    -> exact horizontal zero width.                            (4.1)
```

This is stronger as a detector than the diagonal Selberg tests, but not an
independent positivity mechanism.  Proving `D_ell=O(1)` by the zero-side
formula is circular; it is RH.  A genuine continuation must derive that
bound from an arithmetic structure not equivalent to merely restating the
explicit formula.  The next fail-fast question is whether (3.5) has a
prime-side renewal, positivity, or bounded-coboundary representation whose
boundedness follows independently.  Standard PNT error estimates are too
coarse, even though the triangular logarithmic smoothing is exactly strong
enough for absolute zero-side summability.

That fail-fast audit is now complete.  Prime powers are bounded lower-order
terms, the natural coboundary is itself RH-equivalent, scale refinement has
no spectral gap, and uniform two-box positivity is exactly the target.  The
remaining question is a power-bounded transfer or signed bilinear identity
coupling distinct actual primes; see the successor report linked above.

The result also does not settle the reverse exponent for the *localized
spectral floor*.  A single observable has summable coefficients, so its upper
rate is immediate.  The floor takes a support-dependent infimum over all
tests, where clustered divisors and changing witnesses create the separate
uniformity obstruction analyzed in
`QUANTITATIVE-WEIL-FLOOR-DIVERGENCE.md`.

## 5. Trust and literature boundary

The proof uses only the following standard inputs:

1. the normalization-matched Guinand--Weil explicit formula for compactly
   supported piecewise-smooth tests;
2. the functional equation and conjugation symmetries of zeta zeros;
3. the critical-strip bound `|Im z_rho|<1/2`;
4. Riemann--von Mangoldt local counting, sufficient for (2.2).

The explicit Weil formula and conventions agree with Masatoshi Suzuki,
[*On the Hilbert space derived from the Weil
distribution*](https://arxiv.org/abs/2301.00421),
and with the repository's `GuinandWeilLiterature` boundary.  The exact-width
identity is a short synthesis of those classical inputs and the elementary
nonreal-zero-free property of `sinc`; it has not been formalized in Lean.
The cone countermodels and their scalar algebra are separate and partially
Lean-checked.

## 6. Lightweight normalization check

The diagnostic `src/fixed_box_width_spectrometer.py` evaluates (3.2) and can
compare it with a truncated critical-line zero series.  It is not used in the
proof.  Run it serially with

```text
cd src
env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
    MKL_NUM_THREADS=1 NUMEXPR_NUM_THREADS=1 \
    python3 fixed_box_width_spectrometer.py \
      --length 1 --separation 4 --zeros 100
```

The normalization anchor is

```text
pole coefficient       1.021007721651046
pole                    7.682461701917364
prime                   7.529409927282216
archimedean             0.1382529972687704
arithmetic cross        0.01479877736637814
first 100 zero pairs    0.01479605589715290
```

The residual `-2.72e-6` is the truncated zero tail.  This checks the pole
sign, the absence of a spurious factor two in the polarized prime term, and
the time/Fourier orientation at one point.  The deterministic algebra tests
are

```text
python3 -m unittest test_fixed_box_width_spectrometer.py
```
