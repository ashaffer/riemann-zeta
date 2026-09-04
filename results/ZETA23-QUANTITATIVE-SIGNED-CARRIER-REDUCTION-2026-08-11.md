# Quantitative signed-carrier reduction

Status: exact normalization and exact signed Schur gate, with a later
carrier-rate correction, 2026-08-11.  The original statement that no allowed
near-screening family was found is superseded as follows.

1. If the distinguished pair may lie anywhere in `J_D`, a collar pair is
   suppressed at the endpoint-tail scale and can lose every fixed power; see
   [`ZETA23-ENDPOINT-JET-COLLAR-CARRIER-RATE-OBSTRUCTION-2026-08-11.md`](ZETA23-ENDPOINT-JET-COLLAR-CARRIER-RATE-OBSTRUCTION-2026-08-11.md).
2. With the distinguished pair in the core, a separated `k`-sublattice pair
   configuration gives `K<=X^(alpha*(1-1/k)+o(1))/L`.  Counts alone allow
   `k=3`, while the proved simple-critical-line density forces `k>=7` and
   leaves the rigorous zero-count-and-density loss `theta=alpha/7`; see
   [`ZETA23-CORE-SUBLATTICE-CARRIER-POWER-LOSS-2026-08-11.md`](ZETA23-CORE-SUBLATTICE-CARRIER-POWER-LOSS-2026-08-11.md).

Thus neither the whole-carrier tail-scale target nor the core
`X^(alpha-o(1))/L` target follows from the stated zero-count and density
inputs.  This
note still does not prove a zero-free strip, and the prime-side lower edge
remains a separate matched-scale input.

## 1. Verdict

The carrier problem should not be formulated using the least singular value
of the full value-interpolation matrix.  In the isolated-zero normalization,
write the compact zero form exactly as

```text
H_C = X_C^T X_C - Y_C^T Y_C.                           (1.1)
```

The rows of `X_C` are the multiplicity-weighted on-line evaluations and the
real parts of all off-line evaluations; the rows of `Y_C` are their imaginary
parts.  For `kappa>0`, the exact collision-stable gate is

```text
lambda_min(H_C) <= -kappa
  iff
||Y_C (X_C^T X_C+kappa*I)^(-1/2)||_op >= 1.            (1.2)
```

Equivalently,

```text
-lambda_min(H_C)
 = sup_(||c||_2=1) (||Y_C*c||_2^2-||X_C*c||_2^2).     (1.3)
```

Thus the missing result is a **signed confluent Schur estimate**, not a raw
Cauchy--Vandermonde estimate.  In the original formulation, the estimate
requested merely by the endpoint-tail comparison was

```text
sup_(||c||_2=1) (||Y_C*c||_2^2-||X_C*c||_2^2)
  >= exp(-o(eta^2*T/log T))                            (1.4)
```

uniformly over the allowed configurations containing a pair of depth at
least `delta`.  The collar construction cited above now disproves (1.4) when
the distinguished pair ranges over all of `J_D`.  A core version remains a
meaningful target, but the legal `k=7` sublattice shows that its power loss
cannot be smaller than `delta/7` using all current zero-count and density
inputs.  Compatibility with the separately evaluated trace, Frobenius, and
pair-correlation data is not asserted by that artificial configuration.

There are two different comparison gates and they must not be conflated:

```text
TAIL GATE:   E_remote=o(K),                            (1.5)
PRIME GATE:  P_negative=o(K),                          (1.6)
```

where `K=-lambda_min(H_C)` is in the normalized coefficient metric,
`E_remote` is the normalized remote-zero norm, and `P_negative` is the
magnitude allowed by a lower-edge theorem for the full prime-side matrix on
the same subspace.  Condition (1.4) is designed only to imply (1.5).  It says
nothing by itself about (1.6).

The obvious critical-sinc near-screening constructions do not disprove
(1.4).  In particular, a pair shifted by half a lattice spacing cancels only
the dominant endpoint phase, while its Cauchy row changes by order `1/L` and
the exact opposite-end cross term does not alternate.  Higher finite
differences require positive binomial atom weights, hence exponential
multiplicity cost, and the unit-window count prevents taking sufficiently
high order in one cluster.

## 2. Exact normalization and budgets

Put

```text
l      = log(T/(2*pi)),
ell_1  = l+2*log(2)-1,
L      = ell_1+eta,
h      = 2*pi/L,
d      = floor(T*L/(2*pi)),
n      = dim V_m = d-m.                                (2.1)
```

For the sharp window, `a=L^(-1) integral phi^2=1`.  All matrices below use
the coefficient `ell^2` norm on `V_m` and the common normalization `1/L^2`.
If

```text
e_z(c)=F_c(z)=x_z(c)+i*y_z(c),
```

then an on-line atom of multiplicity `M` and an off-line reflected pair of
multiplicity `M` contribute, respectively,

```text
(M/L^2) e_r^T e_r,
(2M/L^2) (x_z^T x_z-y_z^T y_z).                        (2.2)
```

Consequently the rows in (1.1) are

```text
sqrt(M)*e_r/L,
sqrt(2M)*x_z/L,                 in X_C,
sqrt(2M)*y_z/L,                 in Y_C.                (2.3)
```

Repeated atoms of the same type are merged by adding their multiplicities.
This is important: duplicating a row with weight `M` means scaling one row by
`sqrt(M)`, not adding an independent direct coordinate.

Let the carrier be

```text
J_D=(T-D,2T+D].
```

Riemann--von Mangoldt, uniformly for `D=o(T)`, gives

```text
N(J_D)
 = T*ell_1/(2*pi) + D*l/pi + O(D+D^2/T+l).             (2.4)
```

Hence the actual cardinal surplus after paying for jets and the collar is

```text
n-N(J_D)
 = eta*T/(2*pi)-m-D*l/pi+O(D+D^2/T+l).                 (2.5)
```

A convenient constant-fraction allocation is

```text
m = mu*eta*T/(2*pi),
D = nu*eta*T/(2*l),
mu+nu < 1,                                             (2.6)
```

up to integer parts and a fixed slack.  Here the two fractions consume
`mu` and `nu` of the leading surplus in (2.5).

With the grid centered at its midpoint, `W=T/2+O(h)`.  The normalized remote
tail from the endpoint-jet estimate is bounded, up to fixed constants, by

```text
X^(1/2)*log(4T)*(1+(W+D)/m)*(W/(W+D))^(2m),
X=exp(L).                                              (2.7)
```

Its decisive logarithmic exponent is

```text
2m*log(1+D/W)
 = (mu*nu/pi+o(1))*eta^2*T/l.                          (2.8)
```

This records the exact comparison scale.  The admissible mesoscopic regime
remains

```text
eta*T >> sqrt(T)*l,
eta=o(l),
exp(eta)*log(l)/l -> 0.                                (2.9)
```

For example, `eta=theta*log l`, `0<theta<1`, gives exponent
`asymp T*(log l)^2/l`.

### 2.1 The second, matched scale

For a pair of fixed depth `alpha`, the full-lattice sharp edge has raw scale

```text
L*X^alpha,
```

and therefore normalized scale

```text
K_pair,full asymp X^alpha/L.                          (2.10)
```

Let

```text
B_X(T)=osc_k A_X(tau_k)+(2/L)*max_k abs(D_X(tau_k)),  (2.11)
```

using the scalar prime polynomials from the constrained sharp Loewner
report.  Its exact elementary operator estimate is

```text
lambda_min(G_prime,raw) >= -L*B_X(T),
lambda_min(G_prime,norm) >= -B_X(T)/L,                (2.12)
```

and compression to `V_m` preserves this lower bound.  Constants such as the
`2` in (2.11) are irrelevant to little-oh comparisons but are retained here
to match the raw inequality.

If the actual normalized carrier margin is written

```text
K=(X^alpha/L)*r_T,                                    (2.13)
```

then the scalar route closes the prime gate only under the matched estimate

```text
B_X(T)=o(X^alpha*r_T).                                (2.14)
```

The bare scalar statement `B_X=o(X^alpha)` does not imply (2.14) when the
carrier loses an unspecified factor `r_T -> 0`.  Two useful specializations
are:

```text
r_T >= X^(-o(1))  and  B_X <= X^(alpha-sigma+o(1))
                                      for fixed sigma>0;       (2.15)

r_T >= X^(-theta+o(1))  and
B_X <= X^(alpha-sigma+o(1)),          requiring sigma>theta.  (2.16)
```

Thus a fixed-saving scalar prime theorem naturally requires at least the
power-scale carrier bound

```text
K >= X^(alpha-o(1))/L,                               (2.17)
```

unless the exponent loss is quantified as in (2.16).  Alternatively, a
direct constrained Pick/Loewner theorem may bypass `B_X`, but its normalized
negative lower-edge error must still be `o(K)` at the **actual** carrier
scale.  Any separately estimated pole or archimedean negative remainder has
the same requirement.

## 3. Exact block leverage and why the one-row version is insufficient

Let

```text
A_kappa=X_C^T X_C+kappa*I.
```

Then

```text
H_C+kappa*I=A_kappa-Y_C^T Y_C.                         (3.1)
```

Since `A_kappa` is positive definite, the ordinary Schur-complement/Douglas
criterion gives

```text
H_C+kappa*I >= 0
  iff
Y_C*A_kappa^(-1)*Y_C^T <= I
  iff
||Y_C*A_kappa^(-1/2)||_op <= 1.                        (3.2)
```

This proves (1.2).  Formula (1.3) is the Rayleigh principle applied directly
to (1.1).

There is a useful but nonuniform one-row corollary.  If `u` is one row of
`Y_C`, then, after discarding all other negative rows,

```text
H_C <= X_C^T X_C-u^T u.
```

Projection onto `ker X_C` therefore yields

```text
lambda_min(H_C)
 <= -dist(u,rowspan(X_C))^2.                           (3.3)
```

For distinct direct nodes, Cauchy--Vandermonde surjectivity says that `u` is
not in `rowspan(X_C)`.  Thus (3.3) is a clean exact signed reduction for a
separated configuration.

It is not a separation-free estimate.  If two pair locations approach one
another, two rows of `X_C` have the form

```text
x(z), x(z+epsilon)=x(z)+epsilon*x'(z)+O(epsilon^2).
```

For every nonzero `epsilon` their row span can approach
`span{x(z),x'(z)}`, even though their contribution to `X_C^T X_C` converges
to the single merged atom `2*x(z)^T*x(z)`.  The small derivative direction
has weight `O(epsilon^2)`.  Replacing the weighted Gram matrix by its row
span loses precisely that scale.  The negative rows have the same confluent
hierarchy, and the full form has a nonzero merged negative edge.  This is why
the regularized block criterion (3.2), rather than (3.3), is the correct
compactified object.

## 4. Confluent formulation of the missing estimate

For a cluster lying along one local parameter direction,
`z_j=z_0+epsilon_j`, real-analytic Taylor expansion gives

```text
x(z_j)=sum_(q>=0) epsilon_j^q*x^(q)(z_0)/q!,
y(z_j)=sum_(q>=0) epsilon_j^q*y^(q)(z_0)/q!.           (4.1)
```

For a general two-parameter cluster `(gamma_j,alpha_j)`, (4.1) is replaced
by the corresponding multi-index expansion; nothing here treats `x` and
`y` as holomorphic functions separately.

The positive and negative cluster Gram matrices therefore carry the same
Hankel moment scales

```text
sum_j M_j*epsilon_j^(q+r).                             (4.2)
```

At exact collision only the zeroth moment remains and the multiplicities
add.  Any quantitative proof must retain these matched weights; separately
normalizing the divided-difference rows recreates the false raw singular-
value obstruction.

The precise missing lemma for **tail closure** can be stated without choosing
a clustering algorithm.

> **Signed confluent Schur lemma required.**  Uniformly for configurations
> in `J_D x {|Im z|<=1/2}` with total point multiplicity at most `n`, the
> Riemann--von Mangoldt discrepancy and unit-window bound, and at least one
> pair of depth `>=delta`, prove for some explicit `K(T,L,m,D,delta)>0`
> that
>
> ```text
> ||Y_C*(X_C^T X_C+K*I)^(-1/2)||_op >= 1,              (4.3)
> ```
>
> with
>
> ```text
> log(1/K)=o(eta^2*T/l).                               (4.4)
> ```

The available counting information is

```text
#C cap [x,x+1] <= A_0*l,
#C cap [x,x+R]
 = integral_x^(x+R) log(t/(2*pi))/(2*pi) dt+O(l),      (4.5)
```

in the height range in question.  Thus every unit cluster has order
`O(l)`, while the type surplus is `eta/(2*pi)`.  For a logarithmic Cauchy
kernel whose pole remains a fixed distance from the real carrier, Stieltjes
integration of the discrepancy term in (4.5) gives the scalar bound
`O(l*log T)=O(l^2)`; it does not intrinsically cost the full dimension
`n asymp T*l`.  This limited calculation is the concrete reason an
`exp(-polylog T)` bound remains plausible.  It is not yet a bound for the
matrix in (4.3).  Turning it into such a bound, uniformly through all
collision strata, is the unproved step.

The complete-interpolation theorem with a discrete Muckenhoupt condition is
not a substitute for (4.3).  The present sequence has a strict type surplus,
and the required object is a one-sided signed block estimate, not an
isomorphism at critical density.  Conversely, density alone does not provide
the quantitative constant.  No Muckenhoupt hypothesis is assumed here.

## 5. Critical-sinc adversarial checks

This section tests only the explicit adversarial families described below.
Its estimates neither give a universal carrier lower bound nor exclude a
different near-screening construction.

### 5.1 Full lattice

One reflected pair at every spacing `h=2*pi/L` has point density `L/pi`,
twice the available leading zeta density `ell_1/(2*pi)`.  Its exact positive-
semidefinite screening identity therefore violates the cardinal hypothesis
by a factor asymptotic to two.  Keeping every second pair repairs the count
scale, but loses the exact identity and leaves a substantial indefinite
block; it is not a counterexample to (4.3).

### 5.2 Half-step cancellation

For the sharp transform write

```text
F_c(z)=2*S(z)*R_c(z),
S(z)=sin(L*(z-tau_0)/2),
R_c(z)=sum_k (-1)^k*c_k/(z-tau_k).                     (5.1)
```

Let `s=pi/L=h/2`.  Then

```text
S(z+s)^2=cos(L*(z-tau_0)/2)^2=1-S(z)^2.               (5.2)
```

At depth `alpha>0`, `|S(z)|^2 asymp exp(alpha*L)`, so the leading endpoint
phase changes sign with relative error `exp(-alpha*L)`.  However
`R_c(z+s)-R_c(z)=O(s)` as a row-valued analytic function.  Consequently two
equal-multiplicity pair forms at `z` and `z+s` retain a leading remainder of
relative order `1/L`, and (5.2) also leaves a nonalternating cross-endpoint
term.  On the full coefficient lattice a single normalized pair has scale
`asymp exp(alpha*L)/L`, so this calculation does not make its absolute
operator remainder small.  Restriction to `V_m` can only reduce row norms;
the calculation therefore supplies no lower bound there, but equally it
does not furnish the operator-norm upper bound needed for a counterexample.

### 5.3 Higher finite differences and the positivity cost

At the level of a row-span approximation, a `K`th finite difference may use
arbitrary coefficients on only `K+1` rows.  Those coefficients cannot be
inserted into the signed zero form: every zero multiplicity is a positive
integer.  Realizing the alternating binomial coefficients through the
half-step phase requires positive atom weights

```text
binom(K,0),...,binom(K,K),
```

of total weight `2^K` (and twice that point multiplicity for reflected
pairs).  Moreover, the exact `1` in (5.2) makes the nonalternating remainder
grow with the same positive weights; canceling only the dominant endpoint
term is not an operator-norm cancellation of the full pair form.

All locations in this construction lie in an interval of length
`K*pi/L`.  The unit-window bound therefore restricts a local realization to

```text
2^K <= O(l), hence K=O(log l),                          (5.3)
```

as long as that interval has bounded length.  For rows whose depth is at
least a fixed `delta`, the Cauchy derivative bound gives a nominal dominant-
endpoint remainder factor on the scale

```text
(C*K/(delta*L))^K=exp(-Theta((log l)^2))               (5.4)
```

when `K` is a fixed positive multiple of `log l`.  This cannot overcome the
initial full-lattice `exp(alpha*L)` scale for fixed `alpha` as `T` tends to
infinity; the exact cross-endpoint operator remainder also accumulates the
positive binomial weights.
Using the global `O(T*l)` point budget in one block violates (4.5), while
spreading the rows destroys the common finite-difference expansion.

Thus this natural family supplies no counterexample at the scale
`exp(-c*eta^2*T/l)`.  This is not a proof that no more elaborate adversarial
family exists.

## 6. Outcome and next theorem

The quantitative carrier-versus-tail question is reduced to (4.3)--(4.4).
A successful proof should combine:

1. clusters of order at most `O(l)` represented by the matched positive and
   negative confluent moment matrices (4.1)--(4.2);
2. a strict-density interpolation estimate between distinct clusters, using
   the surplus `eta/(2*pi)` and the discrepancy `O(l)`;
3. the regularized Schur scale `K`, so that derivative directions of weight
   below `K` are merged rather than normalized; and
4. conversion back to the fixed coefficient norm and `1/L^2`
   normalization of (2.2).

What has not been proved is exactly the uniform lower bound in item 2 after
it is coupled to the signed cluster matrices in items 1 and 3.  Ordinary
confluent Vandermonde bounds, complete-interpolation theorems with an
unverified Muckenhoupt condition, and the full critical lattice identity do
not fill this gap.

The matched closure cards are therefore:

```text
TAIL CLOSURE:
  prove (4.3) with log(1/K)=o(eta^2*T/l);
  then the endpoint-jet remote norm is o(K).

SCALAR PRIME CLOSURE AT DEPTH alpha:
  prove K=(X^alpha/L)*r_T and B_X=o(X^alpha*r_T);
  a fixed-saving B_X<=X^(alpha-sigma+o(1)) is enough only when
  r_T>=X^(-theta+o(1)) with theta<sigma.

DIRECT PICK ALTERNATIVE:
  prove the normalized constrained prime matrix has lower edge -o(K)
  at the actual K, without separately bounding A_X and D_X.
```

In particular, (4.4) and the bare scalar estimate `B_X=o(X^alpha)` do **not**
combine to prove a strip: (4.4) permits a carrier margin far below the power
scale `X^alpha/L`.  A zero-free strip would require one of the matched prime
comparisons above, on the same endpoint-jet subspace, as well as tail
closure.  No strip claim follows from the carrier reduction alone.  The
arithmetic edge is reduced to exact scalar Loewner data in
[`ZETA23-CONSTRAINED-SHARP-LOEWNER-PRIME-EDGE-2026-08-11.md`](ZETA23-CONSTRAINED-SHARP-LOEWNER-PRIME-EDGE-2026-08-11.md).
