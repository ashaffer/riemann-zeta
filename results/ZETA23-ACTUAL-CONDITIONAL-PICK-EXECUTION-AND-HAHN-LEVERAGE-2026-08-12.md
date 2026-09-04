# Actual conditional-Pick execution and the Hahn-leverage geometry

Status: exact geometric reduction, a precise remaining Hahn-tail lemma,
deterministic completed-matrix scan, and two rigorous Arb one-state
certificates, 2026-08-12.

This is an arithmetic-admission diagnostic.  It does not prove a uniform
conditional-Pick law, exclude a zeta zero, or prove a zero-free strip.

**Subsequent exact geometric closure.**  For the target-only program the grid
may be centered at the candidate and the required jet order rounded upward
to an even integer.  Parity then gives `theta_*=1` exactly, at a cost of at
most one moment.  Thus the conditional Hahn-tail analysis below is only a
robustness problem for forced nonzero phase or odd jet order, not a necessary
gate for the candidate-centered construction.  See
[`ZETA23-CENTERED-EVEN-JET-PARITY-COMPANION-2026-08-12.md`](ZETA23-CENTERED-EVEN-JET-PARITY-COMPANION-2026-08-12.md).

## 1. Verdict

The proposed inherited-anchor companion survived the requested finite
fail-fast.

* On 1,164 completed target-conditioned matrices, every sampled
  boundary--confluent one-square value was positive even **before** the
  normalized `+1` Herglotz shift.  Every sampled strong `g^perp` compression
  was positive after that shift.
* A rational state within `2.92e-13` of the worst shifted one-square sample
  was replayed with Arb/Acb.  Its unshifted arithmetic Rayleigh interval is
  strictly positive, so this nearby carrier-rich admission is not a
  floating-point or archimedean-shift artefact.
* The inherited anchor has a simpler exact meaning than was previously
  recorded:

  ```text
  S_m intersect g^perp = W_(m+1) intersect ker(x).       (1.1)
  ```

  Thus `theta_*` is one minus a single conditional Christoffel/Hahn
  leverage.
* Without using parity, on a fixed-width equispaced aperture the desired
  robustness conclusion

  ```text
  theta_* = 1-O(1/T).                                  (1.2)
  ```

  is reduced to the explicit Uniform Weyl-Tail Estimate (3.7) below.
  Frozen-recurrence analysis predicts the estimate and its centered leading
  constant, and tridiagonal diagnostics support it, but the required
  variable-coefficient error bound has not been proved here.  The
  phase-robust geometric statement is therefore sharpened, not closed.
  For the centered even-jet target-only construction, the separate parity
  theorem gives `theta_*=1` exactly and closes the retained-carrier fraction
  geometry.  It does not by itself lower-bound the absolute carrier remaining
  after choosing or rounding the jet order.
* Fixed aperture is essential.  With only five nodes and `m=1`, the same
  leverage tends to one and `theta_*` tends to zero as the normalized depth
  grows.  There is therefore no aperture-free geometric theorem.

What remains on the centered even-jet route is arithmetic and divisor-side
isolation: prove the one completed square for the actual von Mangoldt measure
uniformly and rule out carrier-scale collateral screening.  The pointwise
`+1` completion contributes only `2*pi/L=o(kappa)` and does not control the
centered prime term.  The Hahn/Weyl tail lemma remains optional robustness.

## 2. One more endpoint moment is the exact anchor null

Let the equispaced coefficient space have coordinate multiplication
`Delta`, and let

```text
P_m = span{1,tau,...,tau^(m-1)},
W_m = P_m^perp.
```

Write `q_j` for the orthonormal discrete polynomial of degree `j`.  The
three-term Jacobi recurrence gives

```text
P_(W_m) Delta q_(m-1) = a_m q_m,    a_m != 0.       (2.1)
```

Let `x` be the selected positive row,

```text
S_m = W_m intersect ker(x),
g   = P_(S_m) q_m,                                  (2.2)
```

and suppose `g!=0`.  For `v in S_m`,

```text
<v,g>=0  iff <v,q_m>=0
         iff v in W_(m+1).
```

This proves (1.1).  In particular the strong anchored law is exactly

```text
(K+delta I)|_(W_(m+1) intersect ker(x)) >= 0,       (2.3)
```

not a new mysterious codimension-one constraint.

Let `y` be the selected negative row and

```text
a = P_(S_m)y / ||P_(S_m)y||.
```

The orthogonal splitting

```text
S_m=(W_(m+1) intersect ker(x)) direct_sum C*g
```

then gives the exact leverage identity

```text
theta_*
 =1-|<a,g/||g||>|^2
 =||P_(W_(m+1) intersect ker(x)) a||^2
 = ||P_(W_(m+1) intersect ker(x))y||^2
   /||P_(W_m intersect ker(x))y||^2.                (2.4)
```

So `1-theta_*` is the fractional carrier energy removed by the next Hahn
row, conditional on the selected row.  The executable test compares the two
projectors directly to `1e-10` and checks (2.4) to eleven decimal places.

## 3. Exact leverage reduction and the remaining Hahn-tail lemma

The favorable fixed-aperture geometry reduces to one explicit statement
about a uniform-grid Jacobi resolvent.  The leverage reduction is exact.  The
uniform tail estimate is isolated because a frozen-coefficient calculation
alone does not prove its accumulated error bound.

### Conditional Theorem 3.1 (uniform fixed-aperture leverage)

Let `d=2J+1` and use the uniform nodes `-J,...,J`.  Let `p_n` be their
orthonormal Gram/Hahn polynomials.  Put

```text
c_(q,phi)(k)=1/(k+phi+i*q),
|phi|<=1/2,
q -> infinity,       q=o(d),
m -> infinity,       m=o(d).                        (3.1)
```

Let `x,y` be any two independent real quadratures obtained from
`c_(q,phi)` by a nonzero complex scalar, as happens for the exact selected
reflected-pair row.  If the Uniform Weyl-Tail Estimate (3.7) below holds,
then, uniformly in `phi`,

```text
1-theta_* <= C*q/d,                                 (3.2)
```

for an absolute constant `C` and all sufficiently large `d`.

For the centered grid `phi=0` in the actual selected-row normalization, whose
common scalar is pure imaginary, parity gives the conditional sharper
statement

```text
theta_*=1,                         m even,
1-theta_*=(8+o(1))*q/d,            m odd.            (3.3)
```

The same conditional `O(q/d)` conclusion is expected for fixed `m`; only the
refined constant in (3.3) then depends on the finite initial Jacobi
coefficients.

### Exact reduction and the unproved uniform step

The exact Jacobi recurrence on `d` uniform nodes is

```text
k p_n(k)=a_(n+1)p_(n+1)(k)+a_n p_(n-1)(k),
a_n=(n/2)*sqrt((d^2-n^2)/(4n^2-1)).                 (3.4)
```

If

```text
b_n=<p_n,c_(q,phi)>,
```

orthogonality makes `(b_n)` the Weyl solution of the homogeneous recurrence
associated with (3.4), away from its degree-zero forcing.  On every block

```text
n=m+O(d/q)
```

under (3.1),

```text
a_n=(d/4)(1+o(1)).                                  (3.5)
```

The stable root of the frozen recurrence has modulus

```text
exp(-asinh(q/(2a_n)))
 =exp(-(2+o(1))*q/d).                               (3.6)
```

The needed **Uniform Weyl-Tail Estimate** is that backward
continued-fraction contraction selects this stable root with a uniform
accumulated error.  Concretely, one must prove, for
`0<=r<=c_0*d/q` and uniformly in `phi`,

```text
b_(m+2r)
 =(-1)^r exp(-(4+o(1))*q*r/d)*b_m
   +o(|b_m|),                                       (3.7)
```

The frozen recurrence predicts real-part phase drift
`O(|phi|/q)=o(1)` over the whole block.  A proof of (3.7) requires a
quantitative analysis of
the finite Jacobi continued fraction

```text
h_n=1/(q+a_(n+1)^2 h_(n+1)),    h_(d-1)=1/q.        (3.8)
```

The missing analysis must control variation of `a_n`, contamination by the
unstable solution selected at the far boundary, and accumulated relative
error over `O(d/q)` steps.  Those bounds are not supplied here; (3.7) is a
precise open lemma, not a consequence merely of (3.5)--(3.6).

If (3.7) holds, there are `asymp d/q` same-parity coefficients whose
magnitudes are comparable to `|b_m|`.  Put

```text
B_m=sum_(n>=m) (Re b_n,Im b_n)^T(Re b_n,Im b_n),
ell_m=(Re b_m,Im b_m) B_m^(-1)(Re b_m,Im b_m)^T,
```

and the block estimate gives

```text
ell_m=O(q/d).                                       (3.9)
```

Here is the exact passage from ordinary to conditional leverage.  Identify
the degree tail with `l^2{m,...,d-1}` and let `e_m` be its first coordinate
vector.  The hat-matrix identity says

```text
ell_m=||P_U e_m||^2,       U=span{x,y}.
```

Normalize `x_0=x/||x||` and let `a` be the normalized projection of `y` onto
`x^perp`.  Then `{x_0,a}` is an orthonormal basis of `U`.  If

```text
u=|<e_m,x_0>|^2,       v=|<e_m,a>|^2,
```

then `ell_m=u+v`.  The inherited anchor is `P_(x^perp)e_m`, and hence

```text
1-theta_*=v/(1-u)
            <=ell_m/(1-ell_m).                     (3.9a)
```

Together with (3.9), this proves (3.2) conditional on (3.7).

For `phi=0` in the actual pure-imaginary common-factor normalization, `x` is
even and `y` is odd.  If `m` is even, the anchor is even and (2.4) gives
`theta_*=1` exactly.  If `m` is odd, only the odd subsequence occurs.
Conditional on (3.7), summing its geometric squares gives

```text
1-theta_*
 =1-exp(-(8+o(1))*q/d)
 =(8+o(1))*q/d,                                     (3.10)
```

which yields (3.3).  The constant `8` is algebraically forced by the squared
two-step stable-root ratio and is confirmed by independent tridiagonal
resolvent diagnostics, but it is not a theorem here until (3.7) is proved.
An arbitrary complex rotation of the quadratures preserves the conditional
`O(q/d)` conclusion, not this even/odd labeling.

### Conditional Corollary 3.2 (the Zeta23 endpoint scale)

For critical spacing `h=2*pi/L`, fixed aperture fraction `A>0`, and fixed
depth `alpha>0`,

```text
q=alpha/h=alpha*L/(2*pi),
d=(A/pi+o(1))*T*L.                                  (3.11)
```

The mesoscopic endpoint budget has

```text
m=O(eta*T),       eta=o(L),
```

so `m/d=o(1)`.  The Uniform Weyl-Tail Estimate would give

```text
theta_*=1-O(alpha/(A*T)).                           (3.12)
```

At `phi=0` in the actual normalization and odd `m`, the predicted leading
loss is

```text
1-theta_*=(4*alpha/A+o(1))/T.                       (3.13)
```

Thus proving (3.7) would show that the inherited companion reaches every
fixed carrier fraction below one for all sufficiently large `T` in the
fixed-aperture endpoint regime.

## 4. Why aperture cannot be omitted

Take the five symmetric nodes `k=-2,-1,0,1,2`, `m=1`, and `phi=0`.  The
inherited anchor is proportional to `k`, while the carrier is proportional
to

```text
k/(k^2+q^2).
```

Therefore, exactly,

```text
theta_*(q)
 =1-[sum k^2/(k^2+q^2)]^2
    /[(sum k^2)*(sum k^2/(k^2+q^2)^2)].             (4.1)
```

Writing

```text
A_2=sum k^2=10,  A_4=sum k^4=34,  A_6=sum k^6=130
```

gives

```text
theta_*(q)
 =[A_6/A_2-(A_4/A_2)^2]/q^4+O(q^-6)
 =1.44/q^4+O(q^-6).                                 (4.2)
```

For example `q=30` gives `theta_*=1.77147e-6`.  A shrinking aperture with a
fixed node count can therefore destroy the companion geometry.  This does
does not contradict the proposed Uniform Weyl-Tail Estimate, whose hypothesis
`q=o(d)` is exactly the missing width condition.

## 5. Completed-matrix execution

The scan used the actual completed finite matrix

```text
K_ar=(H_arch+H_pole-H_prime)/L^2                    (5.1)
```

with every active prime power, the exact phase-dependent selected row, the
inherited anchor, and the selected-depth derivative as the confluent
tie-breaker.  The exact `+1` completion is

```text
delta=2*pi/L.                                       (5.2)
```

The three batches were:

| batch | `T` | `gamma/T` | phase | aperture | jets | depths | valid |
|---|---|---|---|---|---|---|---:|
| low | 16,32,64 | 1.25,1.5,1.75 | -.49,0,.49 | .2,.32 | 1,3,5 | .2,.4,.49 | 588 |
| middle | 128,256 | 1.3,1.5,1.7 | -.49,0,.49 | .2,.32 | 1,5,7 | .4,.49 | 432 |
| high | 512 | 1.3,1.5,1.7 | -.49,0,.49 | .2,.32 | 1,7 | .4,.49 | 144 |

Each geometry was tested at
`theta/theta_* in {.5,.9,1}`.  There were 1,164 valid rows and 124 skipped
requests.  All 1,164 passed the shifted strong compression, the shifted
one-square test, and the unshifted one-square test at tolerance `1e-10`.

The extrema were:

| quantity | minimum | parameters |
|---|---:|---|
| `theta_*` | .3468380793 | `T=16`, center 1.5, phase 0, aperture .32, `m=1`, `alpha=.49` |
| shifted `lambda_min(K|g^perp)/kappa` | .4098242980 | `T=512`, center 1.5, phase 0, aperture .32, `m=1`, `alpha=.49` |
| shifted one-square / `kappa` | .6739718902 | `T=512`, center 1.3, phase 0, aperture .2, `m=1`, `alpha=.49`, `theta=.9 theta_*` |
| unshifted one-square / `kappa` | .2374452879 | `T=32`, center 1.5, phase .49, aperture .32, `m=1`, `alpha=.49`, `theta=.5 theta_*` |

At the worst shifted one-square point,

```text
theta_*                       = .9767924312750377
theta                         = .8791131881475339
kappa                         = 2.45038288232663
delta                         = 1.0071911426282654
Herglotz background budget   = 1.7546152603869027
centered arithmetic value    =-.1031260775927299
shifted one-square           = 1.6514891827941730
unshifted one-square         = .6442980401659075.   (5.3)
```

Thus the centered prime term is genuinely negative at this state, but the
unshifted completed background still wins in this finite fixture.

## 6. Rigorous rational replay near the worst state

The worst shifted state in (5.3) was rationalized in the exact endpoint RREF
basis, and that nearby rational state was rebuilt from scratch with Arb/Acb
at 160 bits:

```text
T=512, gamma/T=13/10, aperture=1/5, phase=0,
alpha=49/100, m=1, required carrier fraction=87/100.
```

The certified intervals, displayed at machine-output precision, are

```text
carrier fraction  [0.8791131881475414, 0.8791131881475414]
unshifted Rayleigh [0.6442980401658188, 0.6442980401658188]
kappa              [2.450382882326588,  2.450382882326588].             (6.1)
```

The rationalized physical-state residual was `2.92e-13`.  The lower
Rayleigh endpoint is strictly positive and the lower carrier endpoint
exceeds `.87`.  This is a rigorous finite arithmetic-admission witness in
dimension 201 on a 203-node grid.

The worst normalized unshifted sample was independently replayed at 192
bits:

```text
T=32, gamma/T=3/2, aperture=8/25, phase=49/100,
alpha=49/100, m=1, required carrier fraction=49/100,
carrier fraction  =.49367917790634397...,
unshifted Rayleigh =.09599163540788075... >0.       (6.2)
```

These certify the displayed rational states.  They do not interval-certify
the irrational floating companion construction itself, exact anchor
orthogonality of the rationalization, parameter neighborhoods, or an
asymptotic theorem.

## 7. The `+1` completion and the exact truth boundary

The pointwise gamma/rational estimate

```text
mu+r_0+1 >=0
```

proves that the background contributes a positive Herglotz matrix after the
shift (5.2).  But at fixed target depth

```text
delta/kappa asymp 2*pi/T^alpha ->0.                 (7.1)
```

Hence `+1` is the correct subcarrier error allowance; it is not a
carrier-scale positive lower bound.  It says nothing by itself about the
sign of the centered von Mangoldt square.  Equation (5.3) exhibits that
distinction numerically.

There is also an important logical boundary around the strong law.  By
(1.1), strong positivity on `g^perp` is precisely restricted completed-Weil
positivity after one more endpoint moment.  It is **not** equivalent to
``no off-line zero survives W_(m+1)``:

1. an off-line pair can be invisible to the restricted test space;
2. its negative row can be screened by other divisor contributions; and
3. positivity of one finite compression does not recover the global Weil
   criterion.

If every divisor contribution meeting the support is on the critical line,
then the zero-side form is positive and (2.3) follows.  The converse fails
for the reasons above.  Only positivity over a dense exhaustion of the full
Weil test class with vanishing error approaches RH-strength.  Therefore the
strong `g^perp` route is substantially stronger than the needed one-square
law and must not be advertised as a free consequence of the anchor identity.

For the direct carrier program, the useful remaining target is exactly the
minimal boundary--confluent square:

```text
<z_theta,(K_ar+2*pi/L)z_theta> >=0                 (7.2)
```

uniformly in the candidate geometry.  Proving the Uniform Weyl-Tail Estimate
(3.7) would supply its carrier fraction in the fixed-aperture endpoint
regime without the parity design.  On the centered even-jet target-only route,
the exact parity theorem supplies the full carrier fraction instead.  No
current estimate proves the arithmetic sign in (7.2), and divisor-side target
isolation is still a separate necessary lemma before any zero exclusion
follows.

## 8. Reproducibility

Implementation:

* [`conditional_pick_actual_scan.py`](../src/conditional_pick_actual_scan.py)
  builds the inherited anchor, boundary--confluent state, strong compression,
  one-square balance, and rational replay coordinates.
* [`conditional_pick_companion.py`](../src/conditional_pick_companion.py)
  implements the exact anchored companion.
* [`subfull_direct_q_failfast.py`](../src/subfull_direct_q_failfast.py)
  rebuilds the rational state and completed matrix with Arb/Acb.

Focused verification:

```text
PYTHONPATH=src python3 -m pytest -q \
  src/test_conditional_pick_actual_scan.py \
  src/test_conditional_pick_companion.py \
  src/test_subfull_direct_q_failfast.py
```

Result: `14 passed`.
