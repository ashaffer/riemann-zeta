# Endpoint-jet collar obstruction to a uniform carrier rate

Status: exact counterconfiguration to a carrier estimate uniform on the whole
collared interval `J_D`, 2026-08-11.  This is not a counterexample to a
carrier estimate whose distinguished off-line pair is required to lie in the
modulation core.  In a zero-free-strip argument a fixed zero can be recentered
into such a core, so the core carrier problem remains open.

## 1. Verdict

The signed Schur estimate in the quantitative carrier reduction is false if
the distinguished pair may occur anywhere in

```text
J_D=(T-D,2T+D].
```

Indeed, put the distinguished pair halfway into the left collar and put all
remaining atoms on the line.  The endpoint jets suppress the pair evaluation
by

```text
(W/(W+D/2))^m.
```

Positive on-line atoms cannot make the least eigenvalue more negative.
Consequently there are reflection-invariant configurations satisfying the
Riemann--von Mangoldt discrepancy and unit-window bounds for which

```text
0 < K=-lambda_min(H_C)
  <= 2*X^alpha*(W/(W+D/2+O(h)))^(2m).                 (1.1)
```

For the constant-fraction allocation

```text
m = (mu+o(1))*eta*T/(2*pi),
D = (nu+o(1))*eta*T/(2*l),
mu>0, nu>0, mu+nu<1,
```

this becomes

```text
K <= 2*X^alpha
       *exp(-(mu*nu/(2*pi)+o(1))*eta^2*T/l).          (1.2)
```

In particular, for every fixed `A>0`, eventually

```text
K <= X^(alpha-A)/L.                                   (1.3)
```

Thus no estimate `K >= X^(alpha-theta+o(1))/L` with fixed
`theta`, and not even the tail-scale estimate
`log(1/K)=o(eta^2*T/l)`, can hold uniformly for a distinguished pair in the
whole `J_D` from the stated counting inputs.

This obstruction is specifically a **collar obstruction**.  It does not
settle the relevant recentered target

```text
gamma in [T,2T]
```

or, more robustly, `gamma in [T+cD,2T-cD]` or in a fixed interior interval
such as `[1.1T,1.9T]`.  The quantitative carrier theorem should state such a
core hypothesis on the distinguished pair while retaining all other collar
zeros in `H_C`.

## 2. Parameters and exact normalization

Put

```text
l      = log(T/(2*pi)),
ell_1  = l+2*log(2)-1,
L      = ell_1+eta,
X      = exp(L),
h      = 2*pi/L,
d      = floor(T*L/(2*pi)),
n      = d-m.
```

Use the standard sharp modulation grid of length `T`, with midpoint
`tau_c`, and write

```text
omega_k=tau_k-tau_c,
W=max_k abs(omega_k)=T/2+O(h).
```

Let `V_m` be the real coefficient space satisfying the first `m` endpoint
jet conditions, with its inherited coefficient `ell^2` norm.  The isolated
zero normalization is exactly `1/L^2`.  Thus an off-line pair of
multiplicity one at `z=gamma-i*alpha` contributes

```text
H_z=(2/L^2)*(x_z^T*x_z-y_z^T*y_z),
F_c(z)=x_z(c)+i*y_z(c).                                (2.1)
```

This keeps the collision weight and coefficient normalization used in the
quantitative signed-carrier reduction.  The construction below has no
collisions and every atom has multiplicity one.

## 3. Exact collar evaluation lemma

### Lemma 3.1

For `z=gamma-i*alpha`, `0<alpha<1/2`, and every `c in V_m`,

```text
abs(F_c(z))
 <= L*X^(alpha/2)*(W/abs(z-tau_c))^m*||c||_2
 <= L*X^(alpha/2)*(W/abs(gamma-tau_c))^m*||c||_2.     (3.1)
```

#### Proof

Write

```text
p_c(t)=sum_k c_k*exp(-i*omega_k*t).
```

The endpoint conditions give

```text
p_c^(j)(+-L/2)=0,             0<=j<m.
```

After modulating by `tau_c` and integrating by parts `m` times,

```text
F_c(z)
 =(-i*(z-tau_c))^(-m)
   *integral_(-L/2)^(L/2) p_c^(m)(t)*exp(i*(z-tau_c)*t)dt.
```

Exact orthogonality at spacing `2*pi/L` gives

```text
||p_c^(m)||_2^2
 = L*sum_k abs(c_k)^2*abs(omega_k)^(2m)
 <= L*W^(2m)*||c||_2^2.
```

Hence `||p_c^(m)||_1<=L*W^m*||c||_2`.  Finally,
`abs(exp(i*z*t))=exp(alpha*t)<=exp(alpha*L/2)=X^(alpha/2)`.
This proves (3.1).  QED

### Corollary 3.2

Let `P` be any positive semidefinite sum of normalized on-line atom forms,
and set `H_C=P+H_z`.  Then

```text
lambda_min(H_C)
 >= -2*X^alpha*(W/abs(gamma-tau_c))^(2m).              (3.2)
```

#### Proof

For every unit coefficient vector `c`,

```text
c^T*H_C*c
 >= -(2/L^2)*y_z(c)^2
 >= -(2/L^2)*abs(F_c(z))^2.
```

Apply Lemma 3.1.  QED

Notice the normalization in (3.2): relative to the optimistic matched
scale `X^alpha/L`, the resulting factor is

```text
r_T <= 2*L*(W/abs(gamma-tau_c))^(2m).                 (3.3)
```

The prefactor is `2L`, not `2/L`; it is negligible compared with the
exponential jet factor.

## 4. A legal counting configuration

Fix constants `mu,nu>0` with `mu+nu<1`, and take integer parts in

```text
m = mu*eta*T/(2*pi),
D = nu*eta*T/(2*l).                                   (4.1)
```

Assume the mesoscopic hypotheses from the quantitative carrier reduction:

```text
eta*T >> sqrt(T)*l,
eta=o(l),
exp(eta)*log(l)/l -> 0.                               (4.2)
```

On `J_D`, put

```text
rho_T(t)=(1/(2*pi))*log(t/(2*pi)).
```

Choose the quantiles `u_j` of this density: for a fixed offset
`0<theta<1`, let

```text
integral_(T-D)^(u_j) rho_T(t)dt=j+theta
```

for every integer for which the right side lies below the total mass.
For every interval `I subset J_D`, this multiset satisfies

```text
abs(#({u_j} cap I)-integral_I rho_T(t)dt) <= 2.        (4.3)
```

It also has `O(l)` points in every unit interval.  A generic choice of
`theta`, followed if necessary by arbitrarily small perturbations, avoids
unused sharp sine-grid points.

Set

```text
gamma=T-D/2.                                          (4.4)
```

Remove the two quantile atoms closest to `gamma`, replace them by the two
members of one reflected off-line pair of depth `alpha`, and leave every
other atom on the line.  Counts include point multiplicity, so the total
count is unchanged.  The modification changes the discrepancy in (4.3) by
at most four and changes every unit-window count by at most two.  Therefore
the resulting configuration obeys, uniformly for intervals in `J_D`,

```text
#C cap I = integral_I rho_T(t)dt+O(1),
#C cap [x,x+1] = O(l).                                 (4.5)
```

These are stronger than the stated `O(l)` Riemann--von Mangoldt discrepancy
and unit-window inputs.  The quantile construction can be continued outside
`J_D` if a global artificial counting function is desired.

Its total multiplicity `M_T` is

```text
M_T
 = T*ell_1/(2*pi)+D*l/pi+O(D+D^2/T+1).
```

On the other hand,

```text
n-M_T
 = (1-mu-nu+o(1))*eta*T/(2*pi)>0.                     (4.6)
```

Thus `M_T<=dim V_m` eventually.  Cauchy--Vandermonde surjectivity shows that
the normalized form has one negative direction, so `K=-lambda_min(H_C)>0`.
All other atoms are on line and contribute the positive semidefinite matrix
`P` in Corollary 3.2.

Since

```text
abs(gamma-tau_c)=W+D/2+O(h),
```

Corollary 3.2 proves (1.1).  Moreover,

```text
2m*log(1+D/(2W)+O(h/W))
 = (mu*nu/(2*pi)+o(1))*eta^2*T/l,                     (4.7)
```

which proves (1.2).

Finally, (4.2) implies

```text
eta^2*T/l^2
 = (eta*T/(sqrt(T)*l))^2 -> infinity.
```

For every fixed `A>0`, the negative exponent in (1.2) therefore dominates
`A*L+log(2L)`, proving (1.3).

## 5. Corrected carrier target

The failed formulation is

```text
uniformly for a distinguished depth-alpha pair anywhere in J_D.
```

A strip-relevant formulation may instead require

```text
gamma in [T+cD,2T-cD]               for fixed c>0,
```

or, more simply after recentering the dyadic interval,

```text
gamma in [1.1T,1.9T].
```

All other zeros in the collars must still remain in the compact form and in
the cardinal budget.  The collar construction above then becomes a positive
addition to the form rather than the distinguished source of negativity.
It gives no counterexample to a power-scale margin for a core pair.

Accordingly the exact conclusions are:

```text
proved false from counts alone:
  a tail-scale or power-scale carrier margin uniform for the
  distinguished pair on all of J_D;

still open:
  the signed confluent Schur rate for a distinguished pair in a fixed core,
  with the full count-compatible collar configuration retained.
```
