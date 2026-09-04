# A sparse tapered `k=3` island retains only the two-thirds carrier power

Status: exact Gabor-level counterconfiguration under the standard
mesoscopic padding regime, 2026-08-11.  This note constructs an artificial
reflection-invariant zero configuration.  It is not asserted to be the zero
set of an `L`-function and makes no claim about the location of a zeta zero.

Hostile audit, 2026-08-11: **PASS**.  The audit checked the endpoint Taylor
estimate, the Gevrey Fourier scale, both conditions on `H`, and the separate
bandwidth-one Frobenius ledger.  Section 8 records the last check explicitly.

## 1. Verdict

The positive-density `k=7` screen is excluded by the evaluated Zeta23
Frobenius moment because it changes a positive proportion of the rows.  The
same moment does **not** exclude a sublinear island.

Put

```text
l       = log(T/(2*pi)),
L       = ell_1+eta = l+2*log(2)-1+eta,
X       = exp(L),
h       = 2*pi/L,
s       = 3*h=6*pi/L,
P       = 2*pi/s=L/3.
```

Fix `0<alpha<1/2`, put

```text
b=2*alpha/3,
```

and choose the island length `H` so that

```text
H*eta/L^8 -> infinity,
H*X^(4*alpha/3)=o(T).                                      (1.1)
```

For the canonical choice `eta=vartheta*log l`, `0<vartheta<1`, one may take

```text
H=X^(alpha/3).                                             (1.2)
```

Both conditions in (1.1) then hold with enormous room, since
`5*alpha/3<1`.  Condition (1.1) is recorded explicitly because this
particular choice of `H` does not cover the weakest allowed padding
`eta*T >> sqrt(T)*l`.  When `alpha<3/8`, even that weakest regime is covered
by taking `H=T^(1/2+epsilon)` with a sufficiently small fixed
`epsilon>0`.

There is an additional zeta-specific qualification.  With the fixed-shape
profile in Section 3, the power-length choice (1.2) violates Huxley's
horizontal zero-density estimate when

```text
alpha>(sqrt(577)-19)/12=0.4184020....                    (1.2a)
```

This does not affect the abstract screening theorem, but it prevents that
broad cap from modeling the actual zeta divisor in this range.  Under
canonical padding one can instead take `H=L^9/eta`, which still satisfies
(1.1), or retain a power-length terminal-depth block while narrowing the
excess-depth cap to that polylogarithmic scale.  The exact density cutoff
and the two-scale Gevrey and moment checks are in
[`ZETA23-SPARSE-ISLAND-ZETA-SPECIFIC-DENSITY-AUDIT-2026-08-11.md`](ZETA23-SPARSE-ISLAND-ZETA-SPECIFIC-DENSITY-AUDIT-2026-08-11.md).

There are configurations satisfying

1. Riemann--von Mangoldt interval discrepancy `O(1)` and the unit-window
   count `O(log T)`;
2. the proved simple-critical-line and distinct-zero density inputs (and,
   with the polylogarithmic or two-scale choice above, the quoted horizontal
   zero-density bounds);
3. the endpoint cardinal budget `#C<=dim V_m`;
4. the evaluated first and Frobenius moments up to `o(N)`, and hence the
   equivalent leading pair-correlation moment; and
5. a distinguished core pair of depth `alpha`;

for which the exact normalized endpoint-jet carrier obeys

```text
0<K=-lambda_min(H_C|V_m)
   <= X^(2*alpha/3+o(1)).                                (1.3)
```

Thus all of those inputs together do not imply the near-isolated estimate
`K>=X^(alpha-o(1))/L`.  The legal sparse island loses the fixed power
`alpha/3`.  Unlike the earlier `k=3` full-core construction, its global
off-line fraction is `o(1)`, so it is compatible with every fixed positive
lower density of simple critical-line zeros.  Unlike the `k=7` full-core
construction, its rank and Frobenius cost are `o(N)`.

The mechanism has two parts.  A finite lattice whose terminal depth is
`b` has norm at most `2X^b` by an exact sampling bound.  The excess depth is
tapered with a Gevrey-flat profile.  Its bilinear Poisson aliases at
`q=-2,...,2` have largest hyperbolic weight `X^(2alpha/3)`.  The only larger
alias is centered at the support endpoint `q=3`; Gevrey localization and
the `m` endpoint jets make that corner negligible under (1.1).

## 2. Why the tempting sparse `k=2` island is not the right model

The `k=2` lattice at the sharp spacing `2h=4*pi/L` has pair-point density

```text
L/(2*pi),                                               (2.1)
```

whereas the Riemann--von Mangoldt density is
`log(t/(2*pi))/(2*pi)`.  On an island of length `H`, its excess count is

```text
(H/(2*pi))*(L-log(t/(2*pi))) = (1+o(1))*H*eta/(2*pi).  (2.2)
```

For a polynomial-length island and the standard logarithmic padding this
is much larger than the allowed `O(log T)` discrepancy.  Boundary rounding
cannot repair a discrepancy accumulated on every long subinterval.

Changing the spacing to the exact zero density does not preserve the
half-power Poisson screen.  If `ell` denotes the local logarithmic density,
then

```text
s_exact=4*pi/ell,             P_exact=ell/2.
```

The sharp support has length `L=ell+eta+O(1)`, so the `q=2` alias now lies
inside the support:

```text
2*P_exact=ell<L,
overlap length=L-ell=eta+O(1),
hyperbolic weight=exp(alpha*ell)=X^(alpha-o(1)).       (2.3)
```

This is an intrinsic reciprocal-density alias, not a finite-section edge.
Consequently neither exact-density `k=2` nor periodic deletion of the
sharp-spacing `k=2` lattice proves an `X^(alpha/2+o(1))` upper bound.  The
minimal uniform sharp sublattice that leaves room for positive on-line
fillers is `k=3`.

## 3. The tapered island

Let `psi` be a fixed nonnegative Gevrey-2 bump such that

```text
support(psi) subset (-1/2,1/2),
0<=psi<=1,             psi(0)=1,
||psi^(r)||_infinity <= A^(r+1)*(r!)^2.               (3.1)
```

Choose `J` so that

```text
J*s=(1+o(1))*H.                                       (3.2)
```

At the ordinates

```text
gamma_j=tau_c+beta+j*s,             |j|<=J,           (3.3)
```

put reflected simple pairs of depths

```text
alpha_j=b+(alpha-b)*psi(j/J).                         (3.4)
```

Thus the distinguished center pair has depth `alpha`, the outer half of
the island has the constant depth `b`, and the excess depth is flat to every
order before the two finite-section boundaries.

For a real sharp coefficient vector `c`, write

```text
p_c(t)=sum_k c_k*exp(-i*(tau_k-tau_c)*t),

F_(j,a)(c)=integral_(-L/2)^(L/2)
 p_c(t)*exp(a*t)*exp(i*(beta+j*s)*t)dt.               (3.5)
```

The exact isolated-zero form of the island is

```text
Q_J(c)=(2/L^2)*Re sum_(|j|<=J) F_(j,alpha_j)(c)^2.    (3.6)
```

No multiplicity has been hidden in (3.6): every `j` represents exactly two
simple reflected points.

## 4. The constant terminal-depth block

Let `Q_(b,J)` be (3.6) with every depth replaced by `b`.  The following
bound is independent of the number of retained pairs.

### Lemma 4.1 (finite sampling bound)

```text
||Q_(b,J)|| <= 2*X^b.                                 (4.1)
```

#### Proof

Put `g(t)=1_[-L/2,L/2](t)*p_c(t)*exp(b*t)*exp(i*beta*t)`.
The sampling spacing is `2*pi/P`, and the time interval is the union of
three intervals of length `P`.  Periodize those three pieces onto one
fundamental interval.  Fourier-series Parseval and Cauchy--Schwarz give

```text
sum_(j in Z) abs(F_(j,b)(c))^2
 <=3*P*integral abs(g(t))^2dt
 = L*integral abs(g(t))^2dt
 <=L^2*X^b*||c||_2^2.                                (4.2)
```

Therefore

```text
abs(Q_(b,J)(c))
 <=(2/L^2)*sum_(|j|<=J) abs(F_(j,b)(c))^2
 <=2*X^b*||c||_2^2.
```

QED

With `b=2alpha/3`, this already has the required power.  In particular, a
hard finite-section boundary at depth `b` cannot restore the full
`X^alpha` scale.

## 5. Bilinear Poisson bound for the excess depth

Write

```text
R_J=Q_J-Q_(b,J).
```

For `xi=t+u`, define

```text
S_J(xi)=sum_(j in Z)
 [exp(alpha_j*xi)-exp(b*xi)]*exp(i*j*s*xi),           (5.1)
```

where the bracket is set to zero outside `|j|<=J`.  Because `psi` is
supported in `(-1/2,1/2)`, this agrees with (3.4) and is smooth across the
finite-section boundaries.  Expanding the two integrals in (3.5) gives the
exact identity

```text
R_J(c)=(2/L^2)*Re integral integral
 p_c(t)*p_c(u)*exp(i*beta*(t+u))*S_J(t+u)dtdu.         (5.2)
```

The next elementary estimate is the quantitative reason for using a flat
taper.

### Lemma 5.1 (Gevrey alias localization)

Uniformly for `|xi|<=L`,

```text
abs(S_J(xi))
 <=C*J*exp(alpha*max(xi,0))
   *sum_(q in Z)
     exp(-c*sqrt(H*abs(xi-q*P)/L)).                   (5.3)
```

Changing the constants in (5.3) absorbs the exponentially smaller aliases
outside the nearest reciprocal cells.

#### Proof

For fixed `xi`, set

```text
f_xi(x)=exp((b+(alpha-b)*psi(x))*xi)-exp(b*xi).
```

This is compactly supported.  Closure of the Gevrey-2 class under analytic
composition, or directly Faa di Bruno's formula and (3.1), gives

```text
||f_xi^(r)||_1
 <=C*exp(alpha*max(xi,0))*(C*L)^r*(r!)^2.             (5.4)
```

After integrating its Fourier transform by parts `r` times and optimizing
at `r` comparable with `sqrt(abs(y)/L)`, (5.4) gives

```text
abs(f_xi_hat(y))
 <=C*exp(alpha*max(xi,0))*exp(-c*sqrt(abs(y)/L)).     (5.5)
```

Poisson summation for `f_xi(j/J)` places its Fourier peaks at
`J*(s*xi-2*pi*q)`.  Since `P=2*pi/s` and `J*s` is comparable with `H`,
(5.5) is exactly (5.3).

QED

Put

```text
rho=L^6/H.                                            (5.6)
```

Outside the `rho`-neighborhoods of the aliases `qP`, (5.3) is
`exp(-c*L^(5/2))` times the crude exponential scale.  Its contribution to
(5.2) is therefore negligible.  In the neighborhoods with
`-2<=q<=2`,

```text
exp(alpha*max(xi,0))
 <=X^(2*alpha/3)*exp(alpha*rho)
 =X^(2*alpha/3+o(1)).                                (5.7)
```

The Schur integral of the kernel over those five neighborhoods is at most
`C*J*rho` times (5.7).  Since

```text
J*rho/L=L^O(1),                                      (5.8)
```

exact orthogonality `||p_c||_2^2=L||c||_2^2` shows that their contribution
to the coefficient-norm operator is

```text
X^(2*alpha/3+o(1)).                                  (5.9)
```

Only the endpoint alias `q=3`, centered at `xi=L`, remains.

## 6. Endpoint jets remove the `q=3` corner

For `c in V_m`, the first `m` derivatives of `p_c` vanish at `L/2`.  If
`W=max_k abs(tau_k-tau_c)`, Taylor's integral formula, Cauchy--Schwarz, and
exact frequency orthogonality give

```text
integral_(L/2-rho)^(L/2) abs(p_c(t))^2dt
 <=L*(e*W*rho/m)^(2*m)*||c||_2^2.                   (6.1)
```

The same statement holds at the other endpoint.  The `q=3` neighborhood in
(5.2) has

```text
t=L/2-x,       u=L/2-y,       x>=0, y>=0,
x+y<=rho.                                              (6.2)
```

Using the crude bound `|S_J|<=C*J*X^alpha`, Schur's test on this corner and
(6.1) bound its normalized contribution by

```text
C*(J*rho/L)*X^alpha*(e*W*rho/m)^(2*m).               (6.3)
```

In the endpoint budget,

```text
m=(mu+o(1))*eta*T/(2*pi),       W=T/2+O(h).
```

Equations (1.1) and (5.6) imply

```text
e*W*rho/m=O(L^6/(H*eta))=o(1).                       (6.4)
```

Thus (6.3) is smaller than every fixed power of `X`.  The `q=-3` corner has
the decaying weight at most `exp(-b*L)` (up to a polynomial factor) and is
harmless without this argument.

Combining (4.1), (5.9), and (6.3) proves

```text
||Q_J|V_m|| <=X^(2*alpha/3+o(1)).                    (6.5)
```

This is an operator upper bound, not merely one small Rayleigh quotient.

## 7. Count, density, and qualitative negativity

The pair-point density inside the island is

```text
2/s=L/(3*pi).                                        (7.1)
```

Uniformly on the dyadic core,

```text
sigma_T(t)
 =(1/(2*pi))*log(t/(2*pi))-L/(3*pi)>0                (7.2)
```

for large `T`.  Put simple on-line atoms at quantiles of `sigma_T` in the
island, and use quantiles of the full Riemann--von Mangoldt density outside
it.  Cumulative rounding at the two island boundaries gives, for every
interval in the carrier,

```text
#(C intersect I)
 =integral_I log(t/(2*pi))/(2*pi)dt+O(1),             (7.3)

#(C intersect [x,x+1])=O(log T).                     (7.4)
```

Generic offsets make every atom distinct.  The local off-line point
fraction is `2/3+o(1)`, but the island occupies only `O(H)` of a length-`T`
core.  Hence the global off-line fraction is

```text
O(H/T)=o(1),                                         (7.5)
```

and the global simple-line fraction is `1-o(1)`.  Every point is simple, so
the distinct-zero density is one.

The total point count is still the Riemann--von Mangoldt count.  The usual
endpoint-jet and collar budget therefore gives `#C<=dim V_m`.  Sharp
Cauchy--Vandermonde surjectivity then preserves one negative direction for
every reflected pair, in particular

```text
K>0.                                                  (7.6)
```

All on-line atoms give a positive-semidefinite matrix `P_on`.  Consequently

```text
lambda_min(Q_J|V_m+P_on)>=lambda_min(Q_J|V_m),
K<=||Q_J|V_m||.                                      (7.7)
```

Equations (6.5)--(7.7) prove (1.3).

If a single global artificial configuration is desired, choose the island
heights to grow sufficiently rapidly and make the corresponding core
intervals disjoint.  Continue the on-line quantile sequence through the
gaps.  The discrepancy added at each pair of island boundaries is bounded,
while `H_n/T_n -> 0`; choosing the heights superexponentially makes the
cumulative rank and moment errors below `T_n` equal to `o(N(T_n))`.  Thus
the construction is not dependent on reusing one ordinate at incompatible
depths for different values of `T`.

## 8. First and Frobenius moments

The island contains

```text
r=O(H*L)                                              (8.1)
```

reflected pairs, so its matrix has rank `O(HL)`.  From (6.5),

```text
abs(tr Q_J)
 <=O(HL)*X^(2*alpha/3+o(1))
 =o(TL),                                             (8.2)

||Q_J||_F^2
 <=O(HL)*X^(4*alpha/3+o(1))
 =o(TL),                                             (8.3)
```

Here the second estimate is exactly the second condition in (1.1), and the
first is weaker.  With the canonical choice (1.2), their displayed upper
sizes are respectively `L*X^(alpha+o(1))` and
`L*X^(5alpha/3+o(1))`.

These displays concern the endpoint-compressed sharp matrix.  For the legal
bandwidth-one Montgomery--Taylor/Zeta23 moment probe one repeats, rather than
infers, the operator estimate.  Its physical support length is
`L_0=ell_1<L`; hence the `q=3` reciprocal peak is outside that support by
`eta`.  Lemma 5.1 and (1.1) make its contribution

```text
O(J*X^alpha*exp(-c*sqrt(H*eta/L)))=X^(-A)
```

for every fixed `A`, without endpoint jets.  The largest remaining alias is
again `q=2`, and the periodization argument for the depth-`b` block still
uses at most three fundamental cells.  After the Zeta23 normalization, the
separate moment-probe matrix `Q_J^(0)` therefore satisfies

```text
rank Q_J^(0)=O(HL),
||Q_J^(0)||op<=X^(2*alpha/3+o(1)),
||Q_J^(0)||F^2<=H*L*X^(4*alpha/3+o(1))=o(N).         (8.4)
```

The fixed smooth ramps change only powers of `L`, already absorbed in the
`o(1)` exponent.

Start with any on-line artificial background having the evaluated leading
trace and Frobenius moments.  Replace the `O(HL)=o(N)` background points in
the island by the pairs and residual on-line quantiles above.  The removed
and inserted on-line blocks have trace `O(HL)` and operator norm `O(L^2)` by
the unit-count sampling bound.  Hence each has Frobenius square at most

```text
O(L^2)*O(HL)=O(H*L^3)=o(N).                          (8.5)
```

Together with (8.4), their total matrix difference `E` satisfies
`||E||_F=o(sqrt(N))`.  Since the background has Frobenius norm
`O(sqrt(N))`, Cauchy--Schwarz gives
`abs(tr(G_background*E))=o(N)`.  Thus

```text
tr G_new=tr G_background+o(N),
||G_new||_F^2=||G_background||_F^2+o(N).              (8.6)
```

The Zeta23 pair-correlation expression is the same Frobenius moment, so it
is not an additional obstruction.  This is the key difference from the
positive-density `k=7` lattice, whose amplified Frobenius mass was of main
order or larger.

## 9. Scope and the surviving gate

The theorem is an obstruction to deriving a near-full carrier power from
the currently imposed count, density, and two-moment ledgers.  It is not a
zeta-zero construction: an Euler product or the complete explicit formula
could impose additional non-bulk correlations which forbid the island.
For the fixed-profile choice (1.2), horizontal density already forbids the
high-depth cap above the cutoff (1.2a); the polylogarithmic and two-scale
repairs are the surviving configurations relevant to that stronger ledger.

There is also a real parameter boundary.  The proof uses
`H*eta >> L^O(1)` to separate the Gevrey `q=3` peak from the distance on
which the endpoint jets force smallness, while the moment ledger requires
`H*X^(4alpha/3)=o(T)`.  It covers the standard logarithmic mesoscopic
padding for every `alpha<1/2`.  It also covers the weakest admissible
padding when `alpha<3/8`, by the alternative following (1.2).  For
`3/8<=alpha<1/2` at that extreme padding, these two inequalities leave no
common power-length `H`; the finite-section corner remains unresolved by
this construction.

Within the standard regime the revised abstract carrier target can be no
stronger than

```text
K >= X^(2*alpha/3-o(1))/L,                            (9.1)
```

unless a genuinely zeta-specific input excludes sparse off-line islands.
Any prime-side theorem must be matched to the actual carrier scale in
(1.3), not to the isolated-pair scale `X^alpha/L`.
