# The exact Wiener extremal remains at a square-root arithmetic gate

Status: exact actual-node square-root construction, stationary-phase audit,
aperture/moment ceiling, and finite diagnostics, 2026-08-12.  The required
lower bound

```text
E_Y >= Y^(-kappa+o(1)),   kappa<0.0180303234...
```

is **not proved**.  No zero-free strip or new bound on a zeta zero is proved.

## 1. Verdict

The signed-height escape reduces, with the correct normalization, to

```text
E_Y
 =sup {abs(sum_k b(xi_k)h_k):
       sum_k h_k*exp(i*xi_k*u_j)=0 for every j,
       sum_k abs(h_k)<=1},                           (1.1)

u_j=log(n_j/Y),
b(xi)=integral W_alpha(u)*exp(i*xi*u)du.             (1.2)
```

Here the `n_j` are the active prime powers in a fixed multiplicative window,

```text
M=#{n_j}=Y^(1+o(1))/log Y.                           (1.3)
```

At the proposed carrier parameters `Y=X^(0.66+o(1))`, the full relative
frequency aperture is

```text
B_max=X=Y^(50/33+o(1)).                              (1.4)
```

This audit found no route from (1.1) to the required exponent.  It did prove
three useful facts.

1. There is a completely explicit, actual-prime-power finite nuller with
   order-one compact carrier and Wiener norm `O(sqrt(M))`.  Thus

   ```text
   E_Y >= c_W/sqrt(M)
       =Y^(-1/2+o(1)).                               (1.5)
   ```

   This realizes, rather than merely predicts, the universal square-root
   construction on the actual integer logarithms.

2. The tempting all-integer phase

   ```text
   1-exp(2*pi*i*Y*exp(u))                            (1.6)
   ```

   has order-one carrier but Wiener norm asymptotic to `sqrt(Y)` after a
   fixed smooth localization.  Integer-polynomial and higher-harmonic
   variants do not improve this power; ordinary higher degree worsens it.

3. A `2k`-th moment separates the relevant products only at frequency
   length `H >> Y^k`.  Equation (1.4) permits only `k=1`.  In particular the
   available aperture does not even reach the `Y^2` scale at which a fourth
   moment becomes diagonally controlled.  Hypothetically granting all
   moments would give only `sqrt(k/M)`; reaching `Y^(-0.0180304)` that way
   needs `k>=M^(0.963939...+o(1))`.

Consequently higher moments, unique factorization, Montgomery--Vaughan,
prolate concentration, Turan--Nazarov, and Beurling--Malliavin density do not
close (1.1).  The live statement is an all-coefficient resonance theorem for
the actual prime logs, not another frame or density lemma.

## 2. Exact dual normalization

Let `J` be the permitted relative Fourier grid and

```text
V_(j,k)=exp(i*xi_k*u_j).
```

Finite `l^1/l^infinity` quotient duality gives

```text
E_Y
 =inf_(lambda_1,...,lambda_M) max_(k in J)
   abs(b(xi_k)-sum_j lambda_j*exp(i*xi_k*u_j)).       (2.1)
```

There are two orientation traps.

* A feasible nuller in the primal proves a **lower** bound for `E_Y`.
  It does not prove that a better nuller is impossible.
* A von-Mangoldt quadrature in the dual proves the known logarithmic
  **upper** bound

  ```text
  E_Y << (log Y)^(-3/10).                            (2.2)
  ```

  It does not imply a lower bound of any size.

The strip ledger needs a lower bound between (1.5) and (2.2), namely

```text
E_Y >= Y^(-0.0180303234...+o(1)).                    (2.3)
```

All estimates below preserve these directions.

## 3. An explicit actual-node square-root nuller

The following construction uses the actual active integers, not a generic
separated-node model.

### Theorem 3.1 (finite prime-mask nuller)

Fix `0<a<b` and a smooth compact carrier weight `W` in
`(log a,log b)`, with

```text
b_0=integral W(u)du !=0.                             (3.1)
```

Let `S_Y` be any set of `M` distinct integers in `[aY,bY]`.  Let the
relative Fourier period `P` tend to infinity and contain a fixed
neighborhood of `[log a,log b]`.  Suppose the permitted grid contains all
modes up to `3*Y^(1+eta)`, for one fixed `eta>0`.

Then, for every sufficiently large `Y`, there is a finite Fourier polynomial

```text
q_Y(u)=sum_k h_k*exp(i*xi_k*u)                       (3.2)
```

on that grid such that

```text
q_Y(log(n/Y))=0                  (n in S_Y),         (3.3)
sum_k abs(h_k)<=C_W*sqrt(M),                         (3.4)
integral W(u)q_Y(u)du=b_0+O_W(sqrt(M/Y))+o(1).       (3.5)
```

In particular, when `M=O(Y/log Y)`, the last member is bounded away from
zero and (1.5) follows.

### Proof

Choose an integer `Q` comparable with `Y`, large enough that all integers
met by a fixed enlargement of `[aY,bY]` represent distinct residues modulo
`Q`.  On `Z/QZ`, let

```text
g(r)=1 if r is the residue of an element of S_Y,
g(r)=0 otherwise,

G(x)=sum_(h mod Q) ghat(h)*exp(2*pi*i*h*x/Q).        (3.6)
```

Discrete Fourier inversion and Parseval give

```text
G(n)=1                         (n in S_Y),           (3.7)
sum_h abs(ghat(h))^2=M/Q,                           (3.8)
(1/Q)*integral_0^Q abs(G(x))^2 dx=M/Q.              (3.9)
```

Take `chi` smooth, equal to one on the carrier and active-node interval,
and supported inside the Fourier period.  Put

```text
q_infinity(u)=chi(u)*(1-G(Y*exp(u))).                (3.10)
```

Equation (3.7) proves all the exact nulls.  On the fixed `u`-support,
`x=Y exp(u)` is comparable with `Y`; (3.9), applied to at most a fixed
number of `Q`-periods, gives

```text
norm(chi(u)G(Y*exp(u)))_2 <=C*sqrt(M/Y).             (3.11)
```

Therefore Cauchy--Schwarz proves

```text
integral W*q_infinity
 =b_0+O_W(sqrt(M/Y)).                                (3.12)
```

It remains to audit the Wiener norm.  If `f(u)=chi(u)G(Y exp(u))`, the
Bernstein inequality for the trigonometric polynomial `G`, followed by the
chain rule, gives for each fixed `r`

```text
norm(f^(r))_2 <=C_r*Y^r*sqrt(M/Y).                   (3.13)
```

Split the periodic Fourier coefficients of `f` at `abs(xi)=C*Y`.  On the
central block, Cauchy--Schwarz and Parseval give

```text
sum_(abs(xi_k)<=C*Y) abs(fhat(k))
 <=C*sqrt(Y)*norm(f)_2
 <=C*sqrt(M).                                       (3.14)
```

On the complement, weighted Cauchy--Schwarz and (3.13) give

```text
sum_(abs(xi_k)>C*Y) abs(fhat(k))
 <=C_r*sqrt(M).                                     (3.15)
```

The fixed cutoff `chi` has bounded Wiener norm.  Hence

```text
norm(q_infinity)_A<=C*sqrt(M).                       (3.16)
```

This is an infinite absolutely convergent Fourier series only temporarily.
Truncate it at

```text
H=(1/4)*Y^(1+eta).                                  (3.17)
```

Using (3.13) with arbitrarily large fixed `r`, the discarded `l^1` tail is
`O_A(Y^(-A))` for any prescribed `A` after increasing `r`.  Thus the vector
of null errors at the `M` nodes has `l^2` norm `O_A(sqrt(M)Y^(-A))`.

Correct that vector on a consecutive grid block in `[2H,3H]`.  Its
normalized Gram entries obey

```text
abs(G_(j,l))<=C/(H*abs(u_j-u_l))       (j!=l).       (3.18)
```

Since distinct integer logarithms in the fixed window are `c/Y` separated,
ordering the nodes gives

```text
max_j sum_(l!=j) abs(G_(j,l))
 <=C*Y*log(M+1)/H=o(1).                              (3.19)
```

The Gram inverse is therefore bounded.  The standard discrete Hilbert
interpolant has coefficient `l^1` norm at most a constant times the `l^2`
norm of the error vector.  It restores (3.3) exactly and changes (3.4)--(3.5)
by `o(1)`.  This proves the theorem.  QED

For the carrier geometry, one may choose any

```text
0<eta<50/33-1=17/33,                                 (3.20)
```

so `[2H,3H]` remains inside the full aperture (1.4).

The theorem concerns the unrestricted Wiener grid in (1.1).  If both lobe
factors are required to lie in an additional endpoint-jet or projected
prolate subspace, the converse Wiener factorization need not preserve that
subspace.  The lower bound therefore does not automatically descend through
such an extra projection.

### Hostile check

Theorem 3.1 proves only (1.5).  Dividing its order-one carrier by the
`sqrt(M)` Wiener bill gives `Y^(-1/2+o(1))`, not (2.3).  The freedom to use
arbitrary complex two-leg coefficients is already included: its exact cost
is this Wiener norm.

## 4. The all-integer chirp pays the same square root

The simplest exact zero function is

```text
c_Y(u)=chi(u)*(1-exp(2*pi*i*Y*exp(u))).              (4.1)
```

It vanishes whenever `Y exp(u)` is an integer, hence at every active prime
power.  If `chi=1` on the support of `W`, nonstationary integration by parts
gives

```text
integral W(u)c_Y(u)du=b_0+O_A(Y^(-A)).               (4.2)
```

### Proposition 4.1 (exact chirp Wiener scale)

For a nonzero fixed cutoff `chi`, periodically embedded as above,

```text
norm(chi(u)*exp(2*pi*i*Y*exp(u)))_A asymp_chi sqrt(Y).
                                                               (4.3)
```

#### Proof

The Fourier integral at frequency `xi` has phase

```text
Phi_xi(u)=2*pi*Y*exp(u)-xi*u.                        (4.4)
```

For `xi` in a fixed subinterval of
`2*pi*Y*exp(supp chi)`, there is one stationary point

```text
u_xi=log(xi/(2*pi*Y)),
Phi_xi''(u_xi)=xi asymp Y.                           (4.5)
```

Uniform one-dimensional stationary phase gives

```text
abs(integral chi(u)*exp(i*Phi_xi(u))du)
 =c_chi(xi/Y)*Y^(-1/2)+O_chi(Y^(-3/2))              (4.6)
```

on a smaller interval where `chi` is bounded away from zero.  The grid has
`asymp P*Y` such modes and each periodic coefficient carries a factor
`1/P`, proving the lower bound `c*sqrt(Y)`.

For the upper bound, use Cauchy--Schwarz and Parseval on the `O(PY)` central
modes.  Repeated nonstationary integration by parts controls the two tails.
This gives `C*sqrt(Y)` and proves (4.3).  QED

Consequently (4.1), after Wiener normalization, retains only

```text
carrier asymp Y^(-1/2).                              (4.7)
```

This matches Theorem 3.1 up to logarithms.

### 4.1 Polynomial and demodulated variants

If `P` is a fixed nonconstant integer-valued polynomial of degree `d`, and
the cutoff is chosen where the leading phase derivative is one-to-one and
nondegenerate, then

```text
1-exp(2*pi*i*P(Y*exp(u)))                            (4.8)
```

still vanishes at all integer nodes.  On every fixed subinterval avoiding
the finitely many critical points of the leading phase, stationary phase
has parameter `Y^d`.  The same proof gives

```text
norm(chi*exp(2*pi*i*P(Y exp(u))))_A
 asymp Y^(d/2).                                     (4.9)
```

Thus degree one is best in this family.  Multiplication by one Fourier mode
only translates the spectral measure and leaves the Wiener norm unchanged.
It cannot remove (4.3).

A high-order stationary point also does not supply a hidden gain for a
fixed-degree integer-valued phase.  A zero of order `r` in the integer
variable becomes a phase of scale `(Y(u-u_0))^r`; its nonoscillatory core
has width `asymp 1/Y`.  Localizing to that core loses `Y^(-1)` of carrier,
which is worse than (4.7).  Localizing more broadly restores the stationary
Wiener bill.  No claim about an arbitrarily growing-degree phase is needed
or made here.

### 4.2 Fixed harmonic averaging does not alter the power

One can replace the single branch in (4.1) by

```text
F(exp(2*pi*i*Y*exp(u))),
F(1)=0.                                              (4.10)
```

For every fixed nonzero trigonometric polynomial `F`, a sufficiently narrow
fixed cutoff leaves an edge subband in which its first nonzero harmonic is
the unique stationary contribution.  Proposition 4.1 then again gives a
`sqrt(Y)` lower bound, with a constant depending on `F`.  If the number of
harmonics grows with `Y`, stationary phase instead produces a new Dirichlet
polynomial in the harmonic index; controlling cancellation in that
polynomial is another arithmetic problem.  No uniform growing-harmonic
lower bound is asserted here.

## 5. Why higher moments stop at the second moment

Let a dual candidate in (2.1) be

```text
P_lambda(t)=sum_j lambda_j*exp(i*t*log(n_j/Y)).      (5.1)
```

If its residual is at most `epsilon`, the low mode gives

```text
sum_j lambda_j=b_0+O(epsilon),                       (5.2)
```

while on a high block the smooth target `b(t)` is negligible.  A
Montgomery--Vaughan mean square on a block of length much larger than `Y`
therefore gives

```text
epsilon^2 >=c*sum_j abs(lambda_j)^2
             >=c*abs(sum_j lambda_j)^2/M,            (5.3)
```

which is the square-root floor.

For a higher moment, write

```text
P_lambda(t)^k
 =sum_(N asymp Y^k) A_k(N)*exp(i*t*log(N/Y^k)).      (5.4)
```

Distinct product integers near `Y^k` can have logarithmic separation only
`asymp Y^(-k)`.  A coefficient-uniform Montgomery--Vaughan separation, or
the equivalent long mean-value theorem for (5.4), needs

```text
H >> Y^k.                                           (5.5)
```

The actual aperture (1.4) satisfies

```text
Y^(50/33+o(1))<Y^2.                                 (5.6)
```

Thus only `k=1` is legal.  In a formal fourth-moment expansion below the
scale (5.5), the near-product offdiagonal terms have no sign and cannot be
dropped.  Unique factorization classifies exact equalities; it does not
control these unresolved near equalities.

Even in the optimistic diffuse-prime case, if (5.5) were granted for
arbitrary `k`, the multiset diagonal improves the second-moment floor only
to the scale

```text
sup_t abs(P_lambda(t))
 >=c*sqrt(k)*norm(lambda)_2
 >=c*sqrt(k/M).                                     (5.7)
```

To make the right side at least `Y^(-kappa)`, with `M=Y^(1+o(1))`, requires

```text
k>=Y^(1-2*kappa+o(1))
  =M^(1-2*kappa+o(1)).                              (5.8)
```

At `kappa=0.0180303234...`, this is

```text
k>=M^(0.9639393532...+o(1)),                         (5.9)
```

and (5.5) would demand a super-polynomially larger aperture.  Higher moments
therefore cannot supply (2.3) in the present geometry.

## 6. Other proposed functional-analytic escapes

### Turan--Nazarov and Logvinenko--Sereda

For an exponential polynomial with `M` independent terms, the relevant
Remez/Turan constants depend exponentially on `M`.  Applied in the direction
needed here, they give exponentially small guarantees, much weaker than
`Y^(-0.018)`.  Treating the full frequency grid as one band does not remove
the `M`-term dependence.

### Beurling--Malliavin and Bernstein interpolation

Density below a band limit can produce a bounded entire function vanishing
on a separated set.  The required norm in (1.1), however, is the total
variation of its representing spectral measure.  The bounded Bernstein
norm does not control this Fourier--Stieltjes/Wiener norm.  Passing through
`L^2` and then to spectral `l^1` costs the square root of the effective
number of constraints.  Theorem 3.1 realizes that cost on the actual nodes.

### Prolate/Riesz/large-sieve bounds

These supply a stable Hilbert inverse.  For an order-one vector at `M`
nodes, its Hilbert interpolation bill is `sqrt(M)`, and the exact two-leg
factorization converts that bill to the Wiener norm, not to its square.
No prolate eigenvalue changes the `l^1` quotient norm without an additional
target-angle theorem.

### Multiscale and random signs

Arbitrary complex signs are already admitted in (1.1).  A random or generic
`M`-node model has minmax scale `M^(-1/2)` up to logarithms.  Consequently a
generic-node argument points in the wrong direction: (2.3) needs a special
arithmetic resonance shared by every dual coefficient vector.

## 7. Finite full-aperture diagnostics

The existing script `prime_translate_atomic_lp_probe.py` solves only the
real-cosine restriction of (1.1).  With triangular width `0.2` and
`alpha=0.49`, the following runs were recomputed:

```text
Y      M    bandwidth B       E_cos          E_cos/b(0)   1/sqrt(M)
300    23   Y                  3.606e-5       1.802e-4     0.2085
300    23   18.9 Y             0.0553955      0.2768       0.2085
1000   61   Y                  0.00584795     0.02922      0.1280
1000   61   35.1 Y             0.0404608      0.2021       0.1280
3000   151  Y                  0.0106743      0.05333      0.08138
                                                               (7.1)
```

The multipliers `18.9` and `35.1` are the finite values of
`Y^(17/33)`, so those two rows use the full power aperture
`B=Y^(50/33)`.

At full aperture the last two finite ratios are consistent with a constant
multiple of `M^(-1/2)`.  This is not an asymptotic theorem.  Moreover the
cosine primal is a strict subset of the complex polarized primal, so a small
`E_cos` is **not** an upper bound for the true `E_Y`.  The computations are
conditioning diagnostics only.

The very small first and third-column-transition values at smaller
bandwidth are also not asymptotic evidence: the finite LP has a sharp rank
threshold as modes are added.  Primal/dual agreement in the displayed
stable runs was between `10^(-14)` and `10^(-10)`, and exact-null residuals
were at most `4*10^(-13)`.

## 8. The exact surviving theorem

Because `b(t)` is rapidly decreasing on a high block, (2.3) would follow
from the following actual-prime-log resonance statement.

> For every complex coefficient vector `lambda` on the active prime powers
> which matches the compact low-frequency moments of `W`, there is a
> permitted relative frequency `t`, `abs(t)<=Y^(50/33+o(1))`, for which
> the centered exponential sum differs from `b(t)` by at least
> `Y^(-kappa+o(1))`, with some `kappa<0.0180303234...`.

This is an **all-coefficient lower resonance theorem**.  It is not the KMT
estimate: KMT gives an upper bound for one explicit von-Mangoldt quadrature.
It is not a large-sieve theorem: the latter gives the mean-square floor
`M^(-1/2)`.  It is not a consequence of unique factorization within the
available aperture, by Section 5.

Conversely, an explicit signed prime-power quadrature with uniform residual
`O(M^(-1/2+o(1)))` on the full grid would rigorously close this route in the
negative direction.  No such actual-prime quadrature is proved here.  The
finite diagnostics make it plausible, but promoting them would itself need
a new uniform flattening theorem for arbitrary prime-log weights.

The honest endpoint is therefore:

```text
actual-node exact nuller at Y^(-1/2+o(1)):          PROVED;
single/integer-polynomial phase beats square root:  NO;
higher moments available beyond k=1:                NO;
generic functional analysis reaches Y^(-0.018):     NO;
required actual-prime all-coefficient resonance:    OPEN;
uniform zero-free strip:                            NOT PROVED.       (8.1)
```

Primary dependencies:

- `ZETA23-SIGNED-HEIGHT-FILTER-LAPLACE-CARRIER-GATE-2026-08-12.md`;
- `ZETA23-PRIME-TRANSLATE-NULLSPACE-ATOMIC-GATE-2026-08-11.md`;
- `ZETA23-MINIMAL-PADDING-ODD-PRIME-RIESZ-AUDIT-2026-08-11.md`;
- `ZETA23-CANDIDATE-RELATIVE-FRACTIONAL-ARITHMETIC-EDGE-AUDIT-2026-08-12.md`.
