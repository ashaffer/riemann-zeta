# Dyadic Mertens power attack: forward inverse and dispersion audit

Status: **NO FIXED-POWER BOUND AND NO ZERO-FREE STRIP PROVED**, 2026-08-12.

The main result of this attack is an exact equivalence which substantially
sharpens the earlier reduction.  Once the prime number theorem
`M(x)=o(x)` is used, the dyadic high-pass estimate

```text
integral_X^(2X) |M(x)-2M(x/2)|^2 dx << X^(3-delta)
```

is quantitatively equivalent, with the same `delta>0`, to

```text
integral_X^(2X) |M(x)|^2 dx << X^(3-delta).
```

Thus removing the literal linear-density mode does not make the
fixed-power problem weaker.  Below the cubic scale the high-pass has a
bounded forward inverse.  Its critical-scale kernel consists of normalized
log-periodic modes (with the linear-density mode as the stationary member),
and the prime number theorem sets every such surviving boundary mode to
zero for `M`.  For
`delta=0.02`, the proposed `X^2.98` high-pass estimate is exactly an
ordinary Mertens mean-square power saving in disguise.

The exact correlation expansion, Mellin--Plancherel identity, and modern
short-interval/dispersion audit below all point to the same surviving
object: the signed principal mode.  No Vaughan, Heath--Brown, Ramaré,
Matomäki--Radziwiłł, spectral, Kloosterman, large-sieve, or multiplicative-
energy input located in this attack controls that mode by a fixed power.

## 1. A bounded forward inverse below the cubic threshold

Write

```text
D(x)=M(x)-2M(x/2).
```

The useful inversion is forward in scale, not backward.  From

```text
D(2x)=M(2x)-2M(x)
```

one gets, for every integer `k>=1`,

```text
M(x)=2^(-k)M(2^k x)-sum_(j=1)^k 2^(-j)D(2^j x).       (1.1)
```

The prime number theorem is equivalent to `M(y)/y -> 0`.  Consequently the
first term in (1.1) tends to zero and

```text
M(x)=-sum_(j>=1)2^(-j)D(2^j x).                       (1.2)
```

This identity retains every signed scale.  It does not split off a head or
use a putative power-saving prime number theorem.

### Theorem 1.1 (same-exponent equivalence)

Let `0<delta<3`.  The following two assertions are equivalent:

```text
(D_delta)  integral_X^(2X)|D(x)|^2 dx <= C_D X^(3-delta)

(M_delta)  integral_X^(2X)|M(x)|^2 dx <= C_M X^(3-delta)
```

for every sufficiently large `X`.  The constants may differ, but `delta`
does not.

#### Proof that `(D_delta)` implies `(M_delta)`

Take the `L^2[X,2X]` norm in (1.2).  A change of variables gives

```text
||D(2^j .)||_(L2[X,2X])^2
 =2^(-j) integral_(2^j X)^(2^(j+1)X)|D(y)|^2dy
 <=C_D X^(3-delta) 2^(j(2-delta)).                   (1.3)
```

Minkowski's inequality and (1.2) therefore give

```text
||M||_(L2[X,2X])
 <=sqrt(C_D) X^((3-delta)/2)
   sum_(j>=1)2^(-j delta/2)
 <<_delta sqrt(C_D) X^((3-delta)/2).                 (1.4)
```

Squaring proves `(M_delta)`.

#### Proof that `(M_delta)` implies `(D_delta)`

The triangle inequality and another change of variables give

```text
||D||_(L2[X,2X])
 <=||M||_(L2[X,2X])+2 sqrt(2)||M||_(L2[X/2,X])
 <=sqrt(C_M)(1+2^(delta/2))X^((3-delta)/2).          (1.5)
```

This proves `(D_delta)`.

### 1.2 Operator form and the sharp threshold

For `r>1`, define

```text
(H_r A)(x)=A(x)-rA(x/r),       (R_r A)(x)=r^(-1)A(rx).
```

If `A(x)/x -> 0`, then

```text
A=-sum_(j>=1)R_r^j H_r A.                            (1.6)
```

On the dyadic-Morrey seminorm

```text
||A||_(p,r)=sup_(X>=X_0) X^(-p/2)||A||_(L2[X,rX]),
```

the forward dilation has exact scaling

```text
||R_r A||_(p,r) <= r^((p-3)/2)||A||_(p,r).           (1.7)
```

It is a strict contraction exactly when `p<3`.  Taking `p=3-delta`
turns (1.6) into a convergent Neumann series with ratio `r^(-delta/2)`.
At `p=3`, the ratio is one and the kernel consists of functions
`A(x)=x P(log_r x)` with `P` one-periodic; `A(x)=cx` is its stationary
member.  The boundary condition `A(x)/x -> 0` kills this whole kernel.
This explains sharply why the high-pass can give an `o(X^3)`
reformulation but cannot create any fixed power saving: every subcubic
power norm already inverts the filter.

For the zero-free target `q<1`, put

```text
3-delta=1+2q,       delta=2(1-q).                    (1.8)
```

The `q=0.99` estimate has `delta=0.02` and is therefore equivalent to

```text
integral_X^(2X)|M(x)|^2dx << X^2.98.                 (1.9)
```

This is the sharpest obstruction found in this attack.

## 2. Exact arithmetic and the all-shift correlation kernel

Define

```text
b(n)=mu(n)-2 1_(2|n)mu(n/2).
```

Then

```text
D(x)=sum_(n<=x)b(n),
sum_(n>=1)b(n)n^(-s)=(1-2^(1-s))/zeta(s).            (2.1)
```

Writing `n=2^v m` with `m` odd gives the exact local values

```text
b(m)=mu(m),   b(2m)=-3mu(m),   b(4m)=2mu(m),
b(2^v m)=0  (v>=3).                                  (2.2)
```

In particular, `b` is multiplicative (though not one-bounded).  Put

```text
K_X(u)=(2X-max(X,u))_+.
```

Expanding without discarding any sign gives

```text
I_D(X):=integral_X^(2X)|D(x)|^2dx
 =sum_(m,n<=2X)b(m)b(n)K_X(max(m,n))                 (2.3)

 =sum_(n<=2X)b(n)^2K_X(n)
  +2 sum_(1<=h<2X) sum_(m<=2X-h)
       b(m)b(m+h)K_X(m+h).                           (2.4)
```

Thus the problem is an all-shift, fully signed Möbius correlation.  There
is no isolated shift whose estimate would suffice.

Let

```text
Q_o(Y)=sum_(m<=Y, m odd)mu(m)^2=4Y/pi^2+O(sqrt(Y)).
```

Equations (2.2) give

```text
sum_(n<=Y)b(n)^2
 =Q_o(Y)+9Q_o(Y/2)+4Q_o(Y/4)
 =26Y/pi^2+O(sqrt(Y)),                               (2.5)

sum_(n<=Y)|b(n)|
 =Q_o(Y)+3Q_o(Y/2)+2Q_o(Y/4)
 =12Y/pi^2+O(sqrt(Y)).                               (2.6)
```

Partial summation therefore evaluates the diagonal exactly to first order:

```text
sum_(n<=2X)b(n)^2K_X(n)
 =39X^2/pi^2+O(X^(3/2)).                             (2.7)
```

The diagonal is far below `X^2.98`; it is not the obstruction.  Conversely,
already the square `m,n<=X`, where `K_X=X`, gives the absolute off-diagonal
mass

```text
sum_(m!=n<=X)|b(m)b(n)|K_X(max(m,n))
 >=(144/pi^4+o(1))X^3.                               (2.8)
```

Hence taking absolute values, using a positive majorant, or controlling
each shift separately at its coefficient-blind size spends the entire
fixed-power budget.  The desired gain can only come from the signed
recombination in (2.4).

## 3. Mellin--Plancherel identifies the analytic endpoint

For `Re(s)>1`, partial summation gives

```text
F(s):=integral_1^infinity D(x)x^(-s-1)dx
 =(1-2^(1-s))/(s zeta(s)).                           (3.1)
```

If

```text
I_D(X)<<X^(1+2q),                                    (3.2)
```

then for every `sigma>q`, dyadic summation gives

```text
integral_1^infinity |D(x)|^2x^(-2sigma-1)dx
 <<1/[1-2^(-2(sigma-q))]
 <<1/(sigma-q).                                      (3.3)
```

Mellin--Plancherel now yields the exact identity

```text
integral_1^infinity |D(x)|^2x^(-2sigma-1)dx
 =1/(2pi) integral_(-infinity)^infinity
   |1-2^(1-sigma-it)|^2
   /(|sigma+it|^2 |zeta(sigma+it)|^2) dt,            (3.4)
```

where the right side is understood as the Mellin transform continued from
`Re(s)>1` through the holomorphic half-plane supplied by (3.2).  Merely
integrating the meromorphic expression on an isolated line to the left of
a zero is not enough; holomorphy in the whole half-plane is essential.

This gives a precise Hardy/Laplace obstruction.  Bound (3.2) puts the
reciprocal-zeta transform in a half-plane class whose vertical `L^2` norm
may grow only as `O((sigma-q)^(-1))`.  Since
`1-2^(1-rho)` is nonzero at every zeta zero with `Re(rho)<1`, any zero to
the right of `q` is forbidden.

There is also a sharp boundary-multiplicity statement.  If
`rho=q+i gamma` has multiplicity `m`, its local contribution to (3.4) as
`sigma` decreases to `q` is

```text
gg (sigma-q)^(1-2m).                                 (3.5)
```

The allowed growth in (3.3) is `(sigma-q)^(-1)`.  A simple boundary zero
has exactly that order and is not excluded by exponent bookkeeping alone;
every boundary zero of multiplicity at least two is excluded.  This is the
sharp pole budget of the proposed dyadic estimate.

By Theorem 1.1, (3.4) is not a new route around ordinary Mertens
mean-square cancellation.  It is its reciprocal-zeta Hardy formulation.

## 4. Why modern short-interval input does not close the bound

### 4.1 Matomäki--Radziwiłł controls exceptions around a retained mean

The power savings in Matomäki--Radziwiłł's *Multiplicative functions in
short intervals II* concern the size of the exceptional set.  Their short
average is compared with a long average; for real-valued functions the
main term remains

```text
(1/X) sum_(X<n<=2X)f(n).
```

See arXiv:2007.04290, especially (1) and Theorem 1.7:
<https://arxiv.org/html/2007.04290v1>.

This distinction is decisive.  For equal short blocks with sums `S_j`,
the exact ANOVA identity is

```text
sum_j |S_j|^2
 =sum_j|S_j-S_bar|^2+K|S_bar|^2,
K S_bar=sum_j S_j.                                   (4.1)
```

The almost-all theorem controls the centered behavior and the exceptional
set.  It does not power-save the second term.  When the long means on the
two adjacent dyadic scales are recombined with coefficients `1,-2`, the
uncancelled main term is exactly `D`, not an error.  Moreover, the explicit
short-average tolerance contains logarithmic terms such as
`log log h/log h`; the power occurs in exceptional-set cardinality, not as
an `X^(-0.01)` amplitude bound for the long mean.

### 4.2 All-short-interval comparison ends at a long Möbius sum

Matomäki--Teräväinen's *On the Möbius function in all short intervals*
uses Ramaré and Heath--Brown decompositions to obtain a comparison of the
form

```text
sum_(x<n<=x+H)mu(n)
 =(H/y_1)sum_(x<n<=x+y_1)mu(n)
  +O(H log(P)/log(Q)),                               (4.2)
```

with `y_1` almost as long as `x`, and then invokes the
Vinogradov--Korobov prime number theorem for the long sum.  See their
formula (4.4): <https://arxiv.org/html/1911.09076>.

Thus the Type I/II and spectral work controls the difference from the long
mode.  Retaining all dyadic signs and applying (4.2) on adjacent scales
returns the corresponding long high-pass.  Iteration has eigenvalue one on
the missing principal sector; it does not produce a fixed-power
contraction.

## 5. Exact prime extraction and the zero-frequency sector

The strongest elementary convolution identity for `b` is

```text
b*1=delta_1-2delta_2,                                (5.1)
```

which is just (2.1) multiplied by `zeta(s)`.  Logarithmic differentiation
also gives the coefficientwise identity

```text
b(n)log n
 =-(b*Lambda)(n)
  -2(log 2)1_(2|n)mu(n/2).                           (5.2)
```

These formulas were tested as starting points for Vaughan,
Heath--Brown, Ramaré, and dispersion decompositions.  They expose rather
than eliminate the obstruction:

1. retaining every divisor sector leaves `b` itself in (5.2), hence the
   same reciprocal-zeta pole;
2. completing (5.1) reconstructs `(1-2^(1-s))/zeta(s)` exactly;
3. at additive frequency zero, a rectangular bilinear block factorizes as

   ```text
   sum_(d,m)a_d c_m=(sum_d a_d)(sum_m c_m),          (5.3)
   ```

   so Type II oscillation is absent;
4. Poisson, Voronoi, Kloosterman, and large-sieve gains apply to nonzero
   additive or nonprincipal character sectors.  The zero/principal sector
   left after their recombination is the long sum in (4.2), equivalently
   the forward-invertible high-pass of Theorem 1.1.

Splitting off one divisor head would demand a power-saving prime number
theorem.  Keeping every head signed gives (5.1)--(5.2) and returns the
original object.  No intermediate exponent closes.

## 6. Best unconditional consequence and exponent ledger

The Vinogradov--Korobov zero-free region gives, for some `c>0`,

```text
M(x)<<x exp{-c (log x)^(3/5)(log log x)^(-1/5)}.      (6.1)
```

Consequently

```text
I_D(X)
 <<X^3 exp{-c' (log X)^(3/5)(log log X)^(-1/5)}.     (6.2)
```

This is a strong subexponential saving but remains `X^(3-o(1))`, not
`X^(3-delta)` for any fixed `delta>0`.  The same is true of the ordinary
Mertens energy by Theorem 1.1.

The complete ledger is therefore

```text
desired high-pass gain                 X^(-0.02)
forward inverse ratio per dyadic scale 2^(-0.01)
equivalent ordinary Mertens exponent   X^2.98
exact diagonal                         (39/pi^2)X^2+O(X^1.5)
absolute offdiagonal                   >=(144/pi^4+o(1))X^3
known unconditional gain               exp{-c log^(3/5)X(loglog X)^(-1/5)}
MR/MR-II power gain                     exceptional-set size, mean retained
Type I/II spectral gain                 nonzero modes, principal sum retained
fixed-power full signed gain            NOT PROVED
```

## 7. Verdict and search-space update

No modern dispersion estimate found in this attack supplies a fixed power
for the complete signed kernel (2.4).  More importantly, Theorem 1.1 proves
that the dyadic high-pass is not a genuinely weaker target at any
subcubic exponent.  It is ordinary Mertens mean-square cancellation under
a bounded change of variables.

Accordingly, this branch should be pruned as an independent escape.  It can
remain as a clean equivalent criterion or as a diagnostic for a future
signed principal-mode theorem, but standard centered short-interval,
exceptional-set, large-sieve, or Kloosterman improvements cannot be
expected to cross the gap.  A proof of `X^2.98` here would already be the
requested zero-free-strip breakthrough, not a preparatory estimate that
current dispersion machinery nearly reaches.
