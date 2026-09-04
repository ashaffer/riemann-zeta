# Prime-translate nulling is an atomic-norm problem

Status: exact complexification, Wiener-factorization, finite linear-program
duality, and KMT dual upper bound, 2026-08-11.  The prime-only leverage is
not proved to have either constant size or a fixed-power loss.  No zero-free
strip is proved here.

## 1. Verdict

The proposed linear nulling of the cross-prime terms survives the
real-admissibility audit.  If an independently polarized complex two-lobe
packet has negative **total** completed form, one of its real or imaginary
coefficient vectors already has negative real completed form.  The prime
nulls and the negative carrier do not have to survive separately in that
one real component.

The quantitative problem is not settled by the large algebraic kernel.  In
the relative Fourier coordinates, a cross-correlation has coefficients

```text
h_k=conj(ell_k)*r_k
```

and therefore obeys the sharp factorization identity

```text
inf_(h_k=conj(ell_k)r_k) ||ell||_2*||r||_2
   =sum_k abs(h_k).                                  (1.1)
```

Thus coefficient normalization turns prime-translate nulling into a
Wiener, or atomic `l^1`, interpolation problem.  Prolate and large-sieve
arguments naturally control `l^2`.  Passing from their stable `l^2`
interpolant to (1.1) can cost the square root of the effective number of
prime constraints.  Dimension alone misses exactly this cost.

There is an exact finite dual formulation.  If `u_n=log(n/Y)`, `b_k` is the
Laplace-carrier multiplier, and

```text
(Vh)_n=sum_k h_k*exp(i*xi_k*u_n),
```

then the optimized prime-null carrier is

```text
E_Y
 =sup {abs(sum_k b_k*h_k): Vh=0, sum_k abs(h_k)<=1}
 =inf_(lambda_n) max_k
      abs(b_k-sum_n lambda_n*exp(i*xi_k*u_n)).        (1.2)
```

The second line is the distance of the continuous Laplace moment sequence
from the span of the prime-log atoms in `l^infinity`.  It is the correct
condition number.  A nonzero Hilbert-space kernel, or even a stable
`l^2` right inverse, does not bound (1.2) from below.

A natural von-Mangoldt quadrature in the dual and the published KMT estimate
give, for the fixed-width smooth cross window,

```text
E_Y << (log Y)^(-3/10).                              (1.3)
```

The low-frequency portion is supplied by the ordinary uniform PNT, and the
KMT estimate supplies the transition range.  This proves that a fixed
positive lower bound for the **optimized normalized cross carrier** is too
strong.  Equivalently, a fixed-`r` distance bound such as the proposed
condition (10.5) cannot be combined uniformly with a fixed-size evaluation
of that first lobe.  It does **not** give a fixed-power upper bound:
`(log Y)^(-3/10)=Y^(-o(1))`.  Consequently (1.3) still retains the full
exponential carrier exponent and does not close or refute the route.

In particular, no estimate

```text
E_Y << Y^(-1/2+o(1))                                (1.4)
```

is proved.  With the normalization below, (1.4) would require the centered
`n^(-1/2)` von Mangoldt polynomial to be `Y^o(1)`, a square-root power
improvement over the imported KMT bound.  That is the original arithmetic
gate in dual form.

There is a second, independent obstruction in the proportional two-lobe
proposal.  The Anthropic constant gives only a global dyadic count of
off-line positive rows.  Those rows may be locally saturated around the
selected ordinate, in which case they approximate the negative Laplace row
exponentially well on a proper lobe arc.  The explicit finite binomial
version is proved in
[`ZETA23-TWO-LOBE-PRIME-NULL-INTERPOLATION-GATE-2026-08-11.md`](ZETA23-TWO-LOBE-PRIME-NULL-INTERPOLATION-GATE-2026-08-11.md).
Even a positive resolution of the isolated prime extremal (1.2) would not
remove that zero-side gate.

## 2. Complex polarization really does descend

Let `A` be any real symmetric matrix representing one of the repository's
finite completed Weil forms on its real coefficient space.  Its Hermitian
complexification is

```text
H_C(z)=conj(z)^T*A*z.
```

Writing `z=x+i*y`, with `x,y` real, symmetry gives

```text
H_C(x+i*y)=x^T*A*x+y^T*A*y.                          (2.1)
```

Indeed the two mixed terms are pure imaginary and cancel.  The same identity
holds after summing the pole, archimedean, prime, and zero matrices, and

```text
||z||_2^2=||x||_2^2+||y||_2^2.                      (2.2)
```

### Corollary 2.1 (real Rayleigh descent)

If `H_C(z)<0`, then `x^T A x<0` or `y^T A y<0`.  Hence an independently
polarized complex packet is legitimate for proving the existence of a
negative real Rayleigh vector.

For a real coefficient vector, the physical packet obeys

```text
p(-t)=conj(p(t)).                                    (2.3)
```

The complex vector `z` need not obey (2.3), but both `x` and `y` do.  It is
irrelevant that a cross-prime null imposed on `z` can split into two
nonzero prime contributions for `x` and `y`: equation (2.1) is an identity
for the **total** form.  If all the bookkeeping proves `H_C(z)<0`, one real
component has the required negative total form.

This corrects the overly pessimistic admissibility warning in Section 10 of
the endpoint-packet report.  It does not provide the quantitative leverage
needed to make `H_C(z)` negative.

## 3. Fixed-lobe Hilbert projection

Let `E` be the permitted complex coefficient space for the free lobe, after
whatever endpoint jets and concentration conditions are imposed.  Fix the
other lobe `r`.  For the active prime powers put

```text
v_n=P_E U(u_n)r,             u_n=log(n/Y),            (3.1)
```

where `U(u)` is relative-frequency translation.  Add to these columns the
two projected pole rows and every positive-mate row that is to be nulled,
and call their span `S`.  For the projected negative Laplace row `a`,

```text
sup_(ell in S^perp, ||ell||=1) abs(<ell,a>)
 =||P_(S^perp)a||
 =dist(a,S).                                         (3.2)
```

This identity is exact.  It also shows why merely proving

```text
dim E > dim S                                         (3.3)
```

is insufficient: (3.3) gives a null vector but gives no angle between `a`
and `S`.

The rest of this report isolates the prime columns.  Adding positive-mate
and pole rows can only decrease the distance in (3.2).

## 4. Sharp Wiener factorization

Use an orthonormal relative Fourier basis indexed by a finite set `J`, and
write

```text
U(u)e_k=exp(i*xi_k*u)e_k.
```

For two coefficient vectors `r,ell`, their polarized cross-correlation is

```text
q_(ell,r)(u)
 =<ell,U(u)r>
 =sum_(k in J) h_k*exp(i*xi_k*u),

h_k=conj(ell_k)*r_k.                                 (4.1)
```

Cauchy--Schwarz gives

```text
||q||_A:=sum_k abs(h_k)<=||ell||_2*||r||_2.          (4.2)
```

Conversely, for any coefficient vector `h`, choose

```text
r_k=sqrt(abs(h_k)),
ell_k=conj(h_k)/sqrt(abs(h_k))                       (4.3)
```

when `h_k` is nonzero, and zero otherwise.  Then
`conj(ell_k)r_k=h_k` and

```text
||ell||_2^2=||r||_2^2=sum_k abs(h_k).                (4.4)
```

Equations (4.2)--(4.4) prove (1.1).  Thus, in the unconstrained polarized
mode space, the normalized cross-correlations are exactly the unit ball of
the finite Wiener algebra.

The Rayleigh normalization has no missing factor two here.  Because the
lobes are orthogonal, rescaling the two factors at fixed `h` gives

```text
inf_(h_k=conj(ell_k)r_k)
  (||ell||_2^2+||r||_2^2)=2*sum_k abs(h_k),           (4.4a)
```

while a Hermitian cross term is `2*Re L_alpha(q)`.  The two factors of two
cancel, so (1.2) is exactly the optimized cross contribution per unit total
coefficient norm in the unconstrained two-lobe model.

For an endpoint-jet or prolate subspace `E`, (4.2) remains a necessary
bound, but the converse factorization (4.3) need not land in `E`.  Endpoint
constraints therefore make the feasible set smaller; their codimension
does not improve its conditioning.

### 4.1 Why an `l^2` prolate theorem is not enough

Suppose an `M`-node interpolation theorem supplies coefficients with

```text
||h||_2 << D^(-1/2)*sqrt(M),                         (4.5)
```

where `D` is the local time-bandwidth dimension.  This is the expected
stable Hilbert-space scale.  The only coefficient-uniform consequence is

```text
||h||_1<=sqrt(D)*||h||_2 <<sqrt(M).                  (4.6)
```

After the factor normalization (4.4), (4.6) loses `M^(1/2)`.  For the
fixed-width prime window,

```text
M asymp Y/log Y,                                     (4.7)
```

so this is a fixed half-power loss, up to logarithms.  A proof may exploit
more structure and beat (4.6), but a prolate dimension count by itself
cannot do so.

## 5. Exact finite `l^1`/`l^infinity` duality

Let the active node matrix and the carrier vector be

```text
V_(n,k)=exp(i*xi_k*u_n),
b=(b_k)_(k in J).                                    (5.1)
```

The physical cross-lobe Laplace functional is diagonal in these
correlation coefficients:

```text
L_alpha(q)=sum_k b_k*h_k.                            (5.2)
```

For a compact cross window with weight `W_alpha`, one may take

```text
b_k=integral W_alpha(u)*exp(i*xi_k*u)du.             (5.3)
```

Prime nulling is exactly `Vh=0`.  Finite-dimensional quotient duality,
using the bilinear pairing `sum_k b_k*h_k` in (5.2), gives

```text
sup_(Vh=0, ||h||_1<=1) abs(<b,h>)
 =inf_lambda ||b-V^T*lambda||_infinity.              (5.4)
```

This is (1.2).  One proof is to restrict the `l^1` functional `<b,->` to
`ker V`.  Its dual norm is the quotient norm of `b` in

```text
l^infinity / (ker V)^circ,
```

where `(ker V)^circ=range(V^T)` is the annihilator for this bilinear
pairing.  Equivalently, one may conjugate `b` and use the Hermitian pairing;
the displayed plus-sign atomic vectors and the value of the extremal are
unchanged.

Equation (5.4) identifies the exact missing lemma.  It is neither the
smallest singular value of `V` in `l^2` nor the dimension of `ker V`.  It is
a uniform approximation of the continuous Laplace moment sequence by a
signed atomic measure supported on the actual prime-power logarithms.

## 6. The KMT quadrature bound and its exact normalization

Let `W` be the fixed bounded-variation cross weight, supported in a fixed
interval, and put

```text
b(xi)=integral W(u)*exp(i*xi*u)du.                   (6.1)
```

For every active prime power `n`, choose the dual weight

```text
lambda_n=Lambda(n)*W(log(n/Y))/n.                    (6.2)
```

Then the residual in (5.4) is the exact centered quadrature error

```text
R_Y(xi)
 =b(xi)-sum_n lambda_n*exp(i*xi*log(n/Y))

 =-Y^(-1/2)*S_(Y,W_tilde)(xi),

W_tilde(u)=exp(-u/2)*W(u),                           (6.3)
```

up to the harmless sign convention in the definition of the centered
polynomial.  Here

```text
S_(Y,W_tilde)(xi)
 =sum_n Lambda(n)/sqrt(n)*W_tilde(log(n/Y))
       *exp(i*xi*log(n/Y))
  -the matching continuum.                           (6.4)
```

Every prime power and the continuum are present in (6.3)--(6.4).

For transition frequencies `abs(xi)asymp Y`, the imported KMT consequence
and bounded-variation partial summation give

```text
S_(Y,W_tilde)(xi)
 <<_W sqrt(Y)/(log Y)^(3/10).                        (6.5)
```

The sharp-prefix source is uniform in the larger range needed here and also
contains a `Y/(1+abs(xi))` term.  On
`abs(xi)>=(log Y)^A`, take `A>3/10` and combine that term with (6.3).  On
`abs(xi)<=(log Y)^A`, the ordinary PNT with its standard zero-free-region
error, applied after the same smooth partial summation, compares (6.2)
directly with (6.1).  Consequently

```text
sup_(abs(xi)<=C*Y) abs(R_Y(xi))
 <<_(C,W) (log Y)^(-3/10).                           (6.6)
```

Sampling (6.6) at the permitted grid frequencies and using (5.4) proves
(1.3).

The normalization is decisive.  To improve (6.6) to
`Y^(-1/2+o(1))`, equation (6.3) requires

```text
S_(Y,W_tilde)(xi)<<Y^o(1)                            (6.7)
```

uniformly on the transition range.  KMT proves the much larger right side
in (6.5).  Thus KMT does not prove (1.4).

Also note what (6.6) does and does not say.  It shows that the proposed
fixed constant in

```text
dist(a_alpha,S)^2>=c*L*Y^alpha                       (6.8)
```

cannot be the faithful asymptotic target after optimizing the normalized
two-lobe carrier, unless the first lobe's own Laplace evaluation is allowed
to carry the compensating logarithmic loss.  The bound does not exclude a
constant fixed-`r` distance for a seed whose own carrier evaluation is
small.  A logarithmic loss still gives `Y^(alpha-o(1))`, however, so it is
harmless at the exponent level.  A lower bound matching any negative power
of `log Y` would remain strong enough for the prime part of a strip proof.

## 7. Two exact geometry countermodels

No theorem using only node count, separation, and time-bandwidth can decide
(5.4).  The following two unitary-translate models have the same qualitative
dimension ledger and opposite leverage behavior.

### 7.1 Many nulls with full carrier

Take two modes of frequencies `0` and `Omega`, put

```text
r=(1,1)/sqrt(2),
ell=(1,-1)/sqrt(2),
a=(1,0),

q(u)=<ell,U(u)r>=(1-exp(i*Omega*u))/2.               (7.1)
```

At every node `u_j=2*pi*j/Omega`,

```text
q(u_j)=0,
||q||_A=1,
abs(<r,a><ell,a>)=1/2.                               (7.2)
```

Over any union of complete periods, the mean of `q` is `1/2`.  The translate
columns at the nodes are all equal to `r`, and

```text
dist(a,span{U(u_j)r})=1/sqrt(2).                     (7.3)
```

By increasing `Omega`, this gives arbitrarily many separated nulls inside a
fixed interval while retaining a full carrier.

### 7.2 The square-root coherent-spike model

Let `a,u_1,...,u_M` be orthonormal, and let a sampled unitary translation
orbit fix `a` and cyclically permute the `u_j`.  Put

```text
r=c*a+sqrt(1-c^2)*u_1,
v_j=U_j*r=c*a+sqrt(1-c^2)*u_j.                       (7.4)
```

Direct orthogonal projection gives

```text
dist(a,span{v_1,...,v_M})
 =sqrt(1-c^2)/sqrt(1+(M-1)c^2).                     (7.5)
```

The retained product is therefore

```text
c*dist(a,span{v_j})
 <=1/(sqrt(M)+1),                                    (7.6)
```

with equality at `c^2=1/(sqrt(M)+1)`.

Equations (7.2) and (7.6) prove that neither a universal constant lower
bound nor a universal square-root upper bound follows from abstract
time-bandwidth geometry.  The actual logarithms of prime powers, the actual
carrier vector, and the atomic norm in (5.4) are essential.

## 8. The canonical integer-log chirp has square-root Wiener cost

There is a useful exact continuous model for the square-root scale.  Fix a
nonzero `chi in C_c^infinity((u_0,u_1))` and define

```text
g_Y(u)=chi(u)*exp(2*pi*i*Y*exp(u)),
q_Y(u)=chi(u)-g_Y(u).                                (8.1)
```

If `Y*exp(u)=n` is an integer, then

```text
q_Y(u)=0.                                            (8.2)
```

For every fixed smooth weight `w`, integration by parts in the phase gives

```text
integral w(u)q_Y(u)du
 =integral w(u)chi(u)du+O_A(Y^(-A))                 (8.3)
```

for every fixed `A`.  Thus this exact all-integer-log annihilator retains
its continuous carrier.

Its Wiener cost is

```text
||Fourier(q_Y)||_1 asymp_chi sqrt(Y).                (8.4)
```

For completeness, write

```text
Fourier(g_Y)(xi)
 =integral chi(u)*exp(i*(2*pi*Y*exp(u)-xi*u))du.
```

The second derivative of the phase is bounded below by `c_chi*Y`, so van
der Corput gives

```text
||Fourier(g_Y)||_infinity<<Y^(-1/2).                 (8.5)
```

Plancherel and

```text
||F||_1>=||F||_2^2/||F||_infinity
```

give the lower bound in (8.4).  The same second-derivative estimate on the
stationary range, followed by integration by parts off that range, gives
the upper bound.  Adding the fixed `Fourier(chi)` changes the norm by only
`O_chi(1)`.

After (1.1), normalizing this annihilator loses `Y^(1/2)`.  It is a rigorous
explanation for the recurrent square-root scale.  It is **not** a universal
lower bound for all prime-only annihilators, and the compactly supported
chirp is not itself a finite endpoint-jet packet.  Truncating it and then
restoring every pointwise zero has exactly the conditioning problem (5.4).

## 9. Same-lobe, endpoint, pole, and archimedean ledger

Prime nulling applies only to the cross-lobe term.  The other pieces remain
as follows.

1. For fixed-width lobes, the same-lobe prime powers have bounded logarithmic
   size and are power-negligible after coefficient normalization.

2. For proportional lobes of width `aL`, the normalized same-lobe prime
   cost is

   ```text
   X^(a/2+o(1))/L,                                   (9.1)
   ```

   while the center-separation carrier has scale

   ```text
   X^(alpha*(1-a)-o(1))/L.                           (9.2)
   ```

   Hence the formal exponent gate is

   ```text
   alpha*(1-a)>a/2.                                  (9.3)
   ```

3. The two pole rows can be inserted among the linear constraints.  This is
   only finite codimension.

4. Endpoint jets are also linear conditions, but their `o(TL)` codimension
   says nothing about the target angle.  The factorization converse in
   (4.3) does not automatically preserve them.

5. The archimedean term cannot be pointwise nulled by (5.1).  On the dyadic
   mode band its completed contribution is only polylogarithmic after the
   repository's normalization, as in the endpoint-packet audit.  It is
   power-negligible compared with (9.2), provided the carrier loses only
   `X^o(1)`.

6. Same-lobe and cross-lobe pieces must be assembled into one complex
   packet before applying Corollary 2.1.  Nulling only the polarized cross
   form is useful only if the resulting **total** Hermitian form is shown
   negative.

## 10. The separate local positive-row obstruction

For reference, the formal global count uses

```text
C_0=0.672500703679...,
r_0=(1-C_0)/2=0.163749648160... .                    (10.1)
```

An `aL` lobe has dimension `(a+o(1))N`, while the global number of off-line
positive rows is at most `(r_0+o(1))N`.  If stable interpolation followed
from `a>r_0`, then (9.3) would suggest the conditional threshold

```text
alpha>r_0/[2*(1-r_0)]
      =(1-C_0)/[2*(1+C_0)]
      =0.0979071... .                                (10.2)
```

The implication from global count to stable interpolation is false.  A
permitted block of reflected-pair positive rows may occupy consecutive legal
pair-center spacings near the selected ordinate.  Put

```text
Delta=4*pi/ell,       ell=log(T/(2*pi)),
```

and, on a lobe `I` of length `aL`, set `z=exp(i*Delta*t)`.  For every fixed
`a<1/2`, `z(I)` is a proper circular arc once `L/ell=1+o(1)`.  Positive and
negative mate rows of a common depth differ, after a harmless common
factor, by

```text
exp(2*alpha*t)=z^(-2*i*alpha/Delta).                 (10.3)
```

The right side is analytic in a fixed neighborhood of that proper arc.
Polynomial approximation on an arc therefore gives, for degree `M`,

```text
dist(target, span of M consecutive positive rows)
 <=exp(O_alpha(L)-c_a*M).                            (10.4)
```

With `M asymp r_0*T*L`, (10.4) is exponentially small even though the
global lobe dimension `a*T*L` exceeds `M`.  The companion report proves an
explicit binomial version with all finite constants and also shows that the
sparse tapered `k=3` counterconfiguration is compatible with the current
global count and moment ledgers.

Thus there are two independent missing theorems:

```text
prime side:  a lower bound for the atomic extremal (5.4)
             of size Y^(-o(1));

zero side:   a local/grouped target-retention theorem for the
             off-line positive rows, or a signed carrier theorem
             which avoids row-by-row nulling.                        (10.5)
```

Neither is proved by the current density, moment, KMT, prolate, or
time-bandwidth inputs.  The complexification issue is closed; the two
quantitative leverage gates are not.

## 11. Exploratory finite probe

The script
[`prime_translate_atomic_lp_probe.py`](prime_translate_atomic_lp_probe.py)
solves the real-cosine restriction of (5.4) and solves its dual separately.
It is deliberately smaller than the admissible complex polarized problem.

At width `0.2`, depth `0.2`, and bandwidth `Y`, representative outputs were

```text
Y       prime-power nodes    modes     E_Y (cosine restriction)
1000    61                   1100      0.00584093
3000    151                  3823      0.01067022.                    (11.1)
```

The primal and dual agreed to the displayed numerical precision and the
pointwise null residuals were below `6*10^(-15)`.  At bandwidth `Y/2`, the
same small instances were numerically indistinguishable from zero.  These
figures are sensitive to the finite bandwidth threshold and are not
monotone at smaller `Y`.

This is evidence that the exact norm and the full aperture matter.  It is
not evidence for a positive asymptotic constant, a logarithmic lower bound,
or a fixed-power upper bound.  The rigorous content is (1.1)--(1.3), not
the finite table.
