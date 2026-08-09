# R94 Luroth forward-correlation and non-normal transfer gate

Status: a genuine transfer-operator lower bound is proved, but it is useful
only at bounded height.  The reverse Luroth chain is solved exactly on its
affine and polynomial modes; those modes give rational spectators rather
than the zeta carrier.  A coherent far-digit tail and exponentially accurate
future-digit martingales are also computed.  Together these results isolate
the unresolved object as a finite, forward, resonant digit sum.  They do not
prove a fixed zero-free strip and do not prove that no such strip exists.

Date: 2026-08-07.

## 1. Verdict

Write

```text
p_n=1/[n(n+1)],
phi_n(y)=1/(n+1)+p_n y=(n+y)/[n(n+1)].                (1.1)
```

For a uniform stationary Luroth orbit

```text
X_0=X,                 X_j=T^j(X),
```

the branch digit `N_1` is independent of `X_1`, has law `p_n`, and

```text
X_0=phi_(N_1)(X_1).                                   (1.2)
```

The target correlation is

```text
C_1(s)=E[X_1 X_0^(s-1)]
      =[(s-1)/(s(s+1))]zeta(s),        Re(s)>0.       (1.3)
```

The full-branch coding gives real structure, but it points in the wrong
time direction for the strip problem.

1. The Perron operator contracts Lipschitz seminorm by the exact factor

   ```text
   q=sum_n p_n^2=pi^2/3-3=0.289868... .               (1.4)
   ```

   This gives the explicit lower bound

   ```text
   abs(C_1(s))
    >=1/(2abs(s))-A_(sigma_0)abs(s-1)/12              (1.5)
   ```

   on `sigma_0<=Re(s)<=1`.  It proves a bounded-height nonvanishing
   region, but at height `t` its favorable term is of size `1/t` and its
   error is of size `t`.
2. Mixing makes the later forward correlations `C_k(s)` nonzero after only
   `O(log abs(t))` steps, but it moves them toward the independent spectator
   `1/(2s)`.  It supplies no inverse estimate back to `C_1`.
3. In the reversed direction the centered coordinate is an exact
   eigenfunction.  Every reversed affine correlation is an explicit
   rational function with no zero in `Re(s)>0`.  The forward and reversed
   two-point laws are nevertheless mutually singular, so detailed balance
   cannot compare them.
4. The digit tail beyond `N` has the exact Hurwitz-zeta expression (6.4)
   and, once `N` is much larger than `abs(s)^2`, is

   ```text
   N^(-s)/(2s)+O(abs(s)N^(-Re(s)-1)).                 (1.6)
   ```

   At a target zero the finite resonant head cancels this nonzero coherent
   tail exactly.
5. Future-digit martingales approximate `X_1` uniformly at rate `2^(-m)`.
   At a target zero their positive step-function correlations are therefore
   exponentially small.  Cone lower bounds which are stable under this
   approximation cannot work.
6. The positive nonlinear observable `X_1(1-X_1)` is an exact spectator:
   its correlation is nonzero at every nontrivial zeta zero because it
   contains `zeta(s-1)`.

Thus the useful residue of the Luroth idea is not generic mixing, a complex
cone, a martingale, time reversal, or a nonlinear positive lift.  It is the
coefficient-specific problem of phase-locking the forward digits
`n=O(abs(t)^2)` against the prescribed tail vector (1.6).

## 2. The operator and the direction containing zeta

Let `U` be the Koopman operator and `P=U^*` the Perron operator on Lebesgue
space:

```text
(Uf)(x)=f(Tx),

(Pf)(y)=sum_(n>=1) p_n f(phi_n(y)).                   (2.1)
```

The intervals `phi_n((0,1))` partition `(0,1)`, so

```text
P1=1,
integral_0^1 Pf=integral_0^1 f.                       (2.2)
```

Put `f_s(x)=x^(s-1)`.  Conditional independence gives

```text
F_s(y):=(P f_s)(y)
 =sum_(n>=1) (n+y)^(s-1)/[n^s(n+1)^s],               (2.3)

C_1(s)=integral_0^1 y F_s(y)dy.                       (2.4)
```

The zeroth moment is always the elementary spectator

```text
integral_0^1 F_s(y)dy=1/s.                            (2.5)
```

At a zeta zero, therefore, `F_s` is not zero.  It has nonzero mean `1/s`
and zero first moment.  A spectral theorem about the size of `P f_s` cannot
by itself forbid this one complex orthogonality.

For later use define the forward lag correlations

```text
C_k(s)=E[X_k X_0^(s-1)]
      =integral_0^1 y(P^k f_s)(y)dy.                  (2.6)
```

Only `k=1` is (1.3).

## 3. A rigorous transfer lower bound, and its exact scale failure

Define, for `0<sigma_0<=1`,

```text
A_(sigma_0)=sum_(n>=1) 1/[n^2(n+1)^sigma_0].          (3.1)
```

For reference,

```text
A_(1/2)=1.000157...,
A_1=zeta(2)-1=0.644934... .                           (3.2)
```

**Theorem 3.1 (one-step Luroth lower bound).**  If

```text
sigma_0<=sigma=Re(s)<=1,
```

then

```text
abs(C_1(s)-1/(2s))
 <=A_(sigma_0)abs(s-1)/12,                            (3.3)
```

and hence

```text
abs(C_1(s))
 >=1/(2abs(s))-A_(sigma_0)abs(s-1)/12.                (3.4)
```

In particular `C_1(s)` is nonzero whenever

```text
A_(sigma_0)abs(s)abs(s-1)<6.                          (3.5)
```

### Proof

Differentiate (2.3).  Since

```text
phi_n(y)>=1/(n+1),
```

one has

```text
sup_(0<=y<=1) abs(F_s'(y))
 <=abs(s-1)sum_n p_n^2(n+1)^(2-sigma)
 <=A_(sigma_0)abs(s-1).                               (3.6)
```

Let

```text
h_s(y)=F_s(y)-1/s.
```

By (2.5), `integral h_s=0`.  If `h` is any complex Lipschitz function of
mean zero on `(0,1)`, and `Y,Z` are independent uniform variables, then

```text
integral_0^1 y h(y)dy
 =(1/2)E[(Y-Z)(h(Y)-h(Z))].                           (3.7)
```

Consequently

```text
abs(integral y h(y)dy)
 <=Lip(h)E[(Y-Z)^2]/2=Lip(h)/12.                      (3.8)
```

Equations (2.4), (3.6), and (3.8) prove (3.3).  The
reverse triangle inequality proves (3.4)--(3.5).  QED.

The constant `1/12` in the mean--first-moment inequality is sharp.  Indeed,

```text
F_*(y)=1/s-(6/s)(y-1/2)                              (3.9)
```

has mean `1/s`, first moment zero, and Lipschitz seminorm `6/abs(s)`.
Thus a complex function needs only `O(1/abs(t))` variation to realize the
target cancellation.  The positive transfer estimate permits `O(abs(t))`
variation, leaving precisely the factor `t^2` exposed below.

This is an actual nonvanishing theorem obtained from the coding.  Its scale
failure is equally exact.  For `s=sigma+it` at large height, (3.4) is

```text
abs(C_1(s)) >= O(1/abs(t))-O(abs(t)),                 (3.10)
```

so it becomes vacuous by a factor of order `t^2`.  Improving the constant
cannot change that mismatch.  A fixed-strip proof from this template would
need an oscillatory derivative estimate of size `o(1/t)`, not the positive
transfer estimate of size `O(t)`.

## 4. Mixing proves nonvanishing for the wrong lag

The exact Lipschitz contraction is unusually clean.

**Lemma 4.1.**  For every complex Lipschitz function `g`,

```text
Lip(Pg)<=q Lip(g),

q=sum_n p_n^2=pi^2/3-3.                               (4.1)
```

### Proof

Each inverse branch has slope `p_n`, while its weight in `P` is also
`p_n`.  Therefore

```text
abs(Pg(y)-Pg(z))
 <=Lip(g)abs(y-z)sum_n p_n^2.                         (4.2)
```

Finally

```text
sum_n p_n^2
=sum_n [1/n-1/(n+1)]^2
=2zeta(2)-3=pi^2/3-3.                                 (4.3)
```

QED.

**Theorem 4.2 (later-lag spectator bound).**  Under the hypotheses of
Theorem 3.1, for every integer `k>=1`,

```text
abs(C_k(s)-1/(2s))
 <=q^(k-1)A_(sigma_0)abs(s-1)/12.                    (4.4)
```

Thus `C_k(s)` is nonzero as soon as

```text
q^(k-1)A_(sigma_0)abs(s)abs(s-1)<6.                  (4.5)
```

At height `t`, a lag `k=O(log(2+abs(t)))` always suffices.

### Proof

Apply Lemma 4.1 `k-1` times to `F_s=P f_s`, then apply (3.7)--(3.8) to

```text
P^(k-1)F_s-1/s.
```

Its mean is zero by invariance.  QED.

At a target zero, (4.4) says only

```text
C_1(s)=0,
C_k(s)->1/(2s).                                      (4.6)
```

This is ordinary decorrelation: `X_k` forgets `X_0` and acquires mean
`1/2`.  It changes the observable whose vanishing matters.

There is no inverse contraction argument.  The operator `P` has an
infinite-dimensional kernel.  For example, let `g` be constant on the first
three branch intervals with values

```text
g=1 on phi_1((0,1)),
g=-3 on phi_2((0,1)),
g=0 on all remaining branches.                        (4.7)
```

Then

```text
Pg=p_1-3p_2=1/2-3/6=0.                               (4.8)
```

Hence nonvanishing after transfer cannot be propagated backward by any
bounded operator estimate.  Complex-cone contraction after several steps
has exactly this defect.

## 5. Time reversal is explicitly soluble and is a spectator

The coordinate function is an exact eigenmode after centering.

**Theorem 5.1 (affine reverse regression).**  Put

```text
q=pi^2/3-3.
```

Then

```text
(P x)(y)=1/2+q(y-1/2),                                (5.1)
```

and, for every `m>=1`,

```text
E[X_0|X_m=y]=1/2+q^m(y-1/2).                          (5.2)
```

Consequently the time-reversed Mellin correlation is

```text
B_m(s):=E[X_0 X_m^(s-1)]

 =1/(2s)+q^m[1/(s+1)-1/(2s)]

 =[(1+q^m)s+(1-q^m)]/[2s(s+1)].                      (5.3)
```

Its only numerator zero is

```text
s=-(1-q^m)/(1+q^m)<0.                                 (5.4)
```

### Proof

Since `phi_n(y)=1/(n+1)+p_ny`, the coefficient of `y` in `Px` is
`sum p_n^2=q`.  Invariance gives `integral Px=integral x=1/2`, which fixes
the constant term and proves (5.1).  Iteration proves (5.2).  Integrating
(5.2) against `y^(s-1)dy` proves (5.3).  QED.

Compare the two orientations:

```text
E[X_1 X_0^(s-1)] =[(s-1)/(s(s+1))]zeta(s),

E[X_0 X_1^(s-1)] =[(1+q)s+(1-q)]/[2s(s+1)].          (5.5)
```

The arithmetic is entirely in the forward orientation.

This extends to all polynomial reverse modes.  The operator `P` preserves
polynomials of degree at most `d`, and on `y^d` its leading coefficient is

```text
lambda_d=sum_n p_n^(d+1).                             (5.6)
```

The numbers

```text
1=lambda_0>lambda_1>lambda_2>...>0                   (5.7)
```

are distinct.  Triangularization therefore gives a unique monic polynomial
`Q_d` satisfying

```text
P Q_d=lambda_d Q_d.                                  (5.8)
```

Every reverse polynomial--Mellin correlation is then

```text
E[Q_d(X_0)X_m^(s-1)]
 =lambda_d^m integral_0^1 Q_d(x)x^(s-1)dx,           (5.9)
```

a rational function of `s`.  The explicitly diagonalizable polynomial
sector contains no zeta divisor.

### 5.1 Why detailed balance cannot transfer (5.3) to (1.3)

The failure is stronger than non-self-adjointness.

**Theorem 5.2 (forward and reverse pair laws are mutually singular).**  Let
`mu_F` be the law of `(X_0,X_1)` and `mu_R` the law of `(X_1,X_0)`.  Then

```text
mu_F perpendicular mu_R.                              (5.10)
```

### Proof

The forward law is supported on the graph

```text
Gamma={(x,T(x)):0<x<1},                               (5.11)
```

and the reverse law on its transpose `Gamma^T`.  Their intersection consists
of points satisfying

```text
T(x)=y,                 T(y)=x.                       (5.12)
```

For each ordered pair of branch indices, the two affine equations have at
most one solution.  Thus `Gamma intersection Gamma^T` is countable.  Both
marginals are nonatomic, so each pair law gives this intersection measure
zero.  Removing it from `Gamma` gives a full `mu_F` set and a zero `mu_R`
set.  QED.

There is therefore no Radon--Nikodym comparison, bounded entropy-production
factor, or reversible-sector inequality capable of bounding the forward
correlation by the rational reverse one.  The Bernoulli property coexists
with maximal two-point time asymmetry.

## 6. Conditional phases and the exact coherent digit tail

Condition on the first digit.  Its contribution to (1.3) is

```text
J_n(s)=p_n integral_0^1 y phi_n(y)^(s-1)dy.           (6.1)
```

Direct integration gives the exact formula

```text
J_n(s)=1/[s(s+1)]
 [s n^(-s)-n^(1-s)+n(n+1)^(-s)].                     (6.2)
```

Although the three displayed series in (6.2) do not separately converge in
the full half-plane, their combination satisfies

```text
J_n(s)=1/2 n^(-s-1)[1+O((1+abs(s))/n)]               (6.3)
```

when `n` is larger than a fixed multiple of `1+abs(s)`.

There is also an exact summed form.  Let `zeta(s,a)` denote the Hurwitz zeta
function and put `a=N+1`.

**Theorem 6.1 (exact digit-tail formula).**  For `Re(s)>0`, with removable
values interpreted by continuation,

```text
R_N(s):=sum_(n>N)J_n(s)

 =[(s-1)zeta(s,N+1)+(N+1)^(-s)-(N+1)^(1-s)]
   /[s(s+1)].                                         (6.4)
```

Uniformly for `sigma_0<=Re(s)<=1`,

```text
R_N(s)=(N+1)^(-s)/(2s)
       +O_(sigma_0)((1+abs(s))(N+1)^(-Re(s)-1)).      (6.5)
```

In particular, if

```text
N+1>=K_(sigma_0)(1+abs(s)^2),                         (6.6)
```

with `K_(sigma_0)` sufficiently large, then

```text
abs(R_N(s))>=(N+1)^(-Re(s))/(4abs(s)).                (6.7)
```

### Proof

Initially take `Re(s)>2` and sum (6.2).  Shifting the last sum by one gives

```text
sum_(n>N)[-n^(1-s)+n(n+1)^(-s)]
 =-(N+1)^(1-s)-zeta(s,N+2).                           (6.8)
```

Using

```text
zeta(s,N+2)=zeta(s,N+1)-(N+1)^(-s)                   (6.9)
```

proves (6.4).  The left side converges normally for `Re(s)>0`, so analytic
continuation proves the identity there.

Euler--Maclaurin gives, uniformly in the indicated strip,

```text
zeta(s,a)
 =a^(1-s)/(s-1)+(1/2)a^(-s)
  +(s/12)a^(-s-1)
  +O_(sigma_0)(abs(s(s+1))a^(-Re(s)-1)).             (6.10)
```

The final exponent in the error is intentionally not optimized; it follows
from the bounded periodic Bernoulli remainder and suffices here.  Substitution
in (6.4) cancels the `a^(1-s)` terms and proves (6.5).  Comparing its error
with the main term proves (6.7).  QED.

The phase on a single `n`-th inverse branch varies by exactly

```text
abs(t)log(1+1/n).                                    (6.11)
```

Thus individual branches enter a narrow complex cone only for
`n` larger than a constant multiple of `abs(t)`.  Formula (6.5) is stronger:
beyond `N` of order `t^2`, the whole infinite tail has one explicit nonzero
resultant vector.

This still does not prove nonvanishing.  If `C_1(s)=0`, then for every such
`N`,

```text
sum_(n<=N)J_n(s)=-R_N(s)

=-(N+1)^(-s)/(2s)
 +O_(sigma_0)(abs(s)(N+1)^(-sigma-1)).               (6.12)
```

The resonant head has total absolute mass of order one and is fully capable
of matching the much smaller vector in (6.12).  Positivity of the far tail
does not constrain that match.  The missing theorem is a signed estimate for
the finite forward sum, not another tail cone.

## 7. Future-digit martingales approach the target zero

Let `D_2,D_3,...` be the Luroth digits of `X_1`, and define

```text
H_m=E[X_1|D_2,...,D_(m+1)].                           (7.1)
```

Each cylinder inverse is affine.  Conditional on its first `m` digits,
`X_1` is uniform on an interval of length

```text
ell_m=product_(j=2)^(m+1)p_(D_j)<=2^(-m).             (7.2)
```

Therefore `H_m` is the midpoint of that interval and

```text
norm(X_1-H_m)_infinity<=2^(-m-1).                    (7.3)
```

**Theorem 7.1 (martingale smallness at a target zero).**  If `Re(s)>0` and
`C_1(s)=0`, then

```text
abs(E[H_m X_0^(s-1)])<=2^(-m-1)/Re(s).               (7.4)
```

### Proof

At the zero,

```text
E[H_m X_0^(s-1)]
=E[(H_m-X_1)X_0^(s-1)].                               (7.5)
```

Use (7.3) and

```text
E[abs(X_0^(s-1))]=integral_0^1 x^(Re(s)-1)dx=1/Re(s).
```

QED.

The `H_m` are bounded positive finite-depth dynamical observables.  Their
correlations can be exponentially close to zero at the target.  Hence a
complex-cone or finite-cylinder theorem with a depth-uniform positive lower
bound is false.  Any useful lower bound must deteriorate at least as fast as
the cylinder resolution, and recovering the limit reinstates the exact
correlation (1.3).

## 8. Nonlinear positive observables immediately become spectators

The first three conditional moments are

```text
M_0(s)=E[X_0^(s-1)]=1/s,

M_1(s)=E[X_1 X_0^(s-1)]
      =[(s-1)/(s(s+1))]zeta(s),

M_2(s)=E[X_1^2 X_0^(s-1)]
      =[(s-1)/(s(s+1))]zeta(s)
       -[2(s-2)/(s(s+1)(s+2))]zeta(s-1).             (8.1)
```

The affine cone is already rigid.  For `h(y)=a+by`,

```text
E[h(X_1)X_0^(s-1)]=a/s+bC_1(s).                      (8.2)
```

At a target zero it vanishes only if `a=0`.  Among nonnegative affine
functions this leaves only the original ray `h(y)=by`, `b>=0`.

The simplest genuinely nonlinear positive observable goes the other way.

**Theorem 8.1 (positive nonlinear spectator).**  Put

```text
h(y)=y(1-y)>=0.
```

Then

```text
E[h(X_1)X_0^(s-1)]
 =[2(s-2)/(s(s+1)(s+2))]zeta(s-1).                   (8.3)
```

If `rho` is any nontrivial zeta zero, the value in (8.3) is nonzero.

### Proof

Subtract `M_2` from `M_1` in (8.1).  For a nontrivial zero,

```text
-1<Re(rho-1)<0,
Im(rho-1)!=0.
```

The zeta function has no zero there: its only zeros in `Re(s)<0` are the
negative even integers.  All rational factors in (8.3) are also nonzero.
QED.

The analytic moment matrix therefore does not lose rank at the target.  In
fact

```text
det [[M_0(rho),M_1(rho)],
     [M_1(rho),M_2(rho)]]

=-2(rho-2)zeta(rho-1)/[rho^2(rho+1)(rho+2)] !=0.     (8.4)
```

Real-axis moment positivity becomes a complex spectator determinant, not a
nonvanishing certificate for `M_1`.

## 9. The complementary zero adds no reversible equation

With the usual factor `chi(s)` in the zeta functional equation, (1.3)
satisfies

```text
C_1(s)=chi(s)
 [(1-s)^2(2-s)/(s^2(s+1))]C_1(1-s).                  (9.1)
```

Thus an off-line zero gives the paired forward correlation zero at
`1-conjugate(s)`.  This is exactly the two-positive-tilt formulation proved
in `R93-COMPLEMENTARY-POSITIVE-CARRIER-FUNCTIONAL-EQUATION-GATE.md`.

The Bernoulli coding does not turn the mate into an independent reverse
constraint.  The actual reverse correlations at both exponents are the
nonzero rational functions (5.3), while Theorem 5.2 prevents any detailed
balance comparison with the two forward zeros.  The positive three-atom and
smooth countermodels in the complementary-carrier report already show that
positivity plus the paired functional equation cannot locate the zeros.

In coding language, the two target equations use the same forward graph but
two different complex Mellin tilts.  Full-branch independence concerns the
random inverse choice conditioned on the future.  It does not symmetrize the
forward graph, and so it supplies no third equation.

## 10. Exact surviving finite theorem

The transfer, martingale, nonlinear, and time-reversal routes all fail for
different exact reasons.  Formula (6.12) leaves a concrete coefficient-level
survivor.

Fix `0<sigma_0<1` and choose

```text
N(s)=ceil(K(1+abs(s)^2))                              (10.1)
```

with `K` large enough for (6.5).  A sufficient fixed-strip theorem would be:
for some `eta>0`, uniformly on

```text
1-eta<Re(s)<1,
abs(Im(s))>=t_0,                                     (10.2)
```

prove

```text
abs(
 sum_(n<=N(s)) J_n(s)+(N(s)+1)^(-s)/(2s)
)

>C abs(s)(N(s)+1)^(-Re(s)-1)                         (10.3)
```

with `C` exceeding the Euler--Maclaurin constant in (6.5).  Then (6.5)
would force `C_1(s)!=0`.

This is not advertised as an easier equivalent of the strip theorem.  It
states exactly what a new Luroth mechanism must accomplish: the first
`O(t^2)` *forward* branch phases must avoid one prescribed vector at their
natural tail accuracy.  Absolute values, an ordinary spectral gap, or a
reverse martingale do not see that information.

Possible admissible inputs would have to exploit correlations between the
adjacent exact coefficients in (6.2), or phase-lock the resonant digit blocks
before summation.  Replacing the finite sum by its total variation costs the
entire desired fixed power.

## 11. Disposition

This audit establishes the following reusable facts.

1. Luroth transfer gives the explicit local nonvanishing bound (3.4), but
   its error misses the high-height scale by `t^2`.
2. The exact spectral gap makes a later correlation nonzero after
   `O(log t)` iterates while changing the target to the independent
   spectator `1/(2s)`.
3. The reversed affine chain and all reverse polynomial modes are explicitly
   soluble and arithmetic-free.
4. Forward and reversed pair laws are mutually singular, so reversibility
   cannot import the rational reverse nonvanishing into the zeta direction.
5. The full far-digit tail is coherent and nonzero, but an assumed zeta zero
   forces the resonant head to cancel it exactly.
6. Positive finite-depth martingale approximants can have exponentially
   small target correlations.
7. Affine perturbations lose the zero unless they remain on the original
   ray, and the first nonlinear positive lift is a nonzero `zeta(s-1)`
   spectator.
8. The functional-equation mate remains a second forward zero, not an
   independent reverse constraint.

No fixed zero-free strip, and no failure of every fixed zero-free strip, is
proved.  The Luroth reformulation has nevertheless reached a sharp endpoint:
the only unclosed route in this coding is the signed resonant-head estimate
(10.3), which is coefficient-specific and forward in time.
