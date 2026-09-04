# The `a>1/3` two-lobe gate: an exact separated theorem and the surviving local obstruction

Status: exact separated-row Paley--Wiener theorem, exact target-conditioned
algebra in the polarized endpoint model, and a Gabor-level audit of the
current bulk hypotheses, 2026-08-11.  No zero-free strip is proved.  The
artificial configurations below are not asserted to be zeta-zero sets.

## 1. Verdict

The number `1/3` is not only the exponent at which the tapered `k=3`
counterconfiguration stops contradicting the proposed two-lobe carrier.  It
is the exact Ingham period threshold for rows separated by the legal `k=3`
spacing.

Let `I` be an interval of length `aL`, and let the real frequencies
`gamma_j` satisfy

```text
abs(gamma_j-gamma_k)>=6*pi/L,       j!=k.             (1.1)
```

For every finite coefficient vector `c`,

```text
(a-1/3)*L*sum_j abs(c_j)^2
 <= integral_I abs(sum_j c_j*exp(i*gamma_j*t))^2dt
 <=(a+1/3)*L*sum_j abs(c_j)^2.                       (1.2)
```

Thus, for every fixed `a>1/3`, the zero-row sampling map has a right inverse
of constant normalized cost.  In the independently polarized endpoint
model this is already target-conditioned: solving the positive-row equation
forces the selected negative coordinate to be twice the retained right-lobe
coordinate.  This is a genuine positive theorem, not a dimension count.

It does not yet prove the desired theorem for every configuration allowed by
the current zeta inputs.  Those inputs permit a polylogarithmic, exact-density
`k=2` island.  Give that island terminal depth `alpha/2`, taper it to depth
`alpha` at the distinguished pair, and retreat the two physical lobes a
fixed distance inside the exact-density endpoints.  The same Gevrey--Poisson
calculation as for the audited `k=3` island then gives

```text
||Q_(k=2)|E_(a,delta)||
 <=X^(alpha/2+o(1)),             1/3<a<1/2.           (1.3)
```

It has bounded Riemann--von Mangoldt discrepancy, global off-line density
`o(1)`, and changes the evaluated trace, Frobenius, and pair-correlation
moments by `o(N)`.  Adding the on-line background is positive semidefinite,
so its compressed negative edge is also at most (1.3).

Consequently the current bulk inputs do **not** prove a uniform signed
carrier of scale `X^(2alpha/3-o(1))`, or of scale
`X^(alpha*(1-a)-o(1))`, even when `a>1/3`.  The first positive theorem that
would support the proposed `alpha>1/4` ledger must use a new local,
zeta-specific fact which excludes or controls `k=2`-density deep islands.
The leading global moments cannot provide that fact.

The exact outcome is

```text
k=3-separated rows at a>1/3:     stable, by (1.2);
all rows allowed by bulk inputs: not stable, by (1.3);
actual-zeta target theorem:      a local grouped/confluent gate.
```

## 2. The exact Ingham inequality at the one-third threshold

The proof needs only the separated Hilbert inequality.

### Lemma 2.1 (finite separated exponential frame)

Let `Gamma={gamma_j}` be a finite subset of the real line with separation
at least `Delta>0`.  On every interval `I` of length `ell`,

```text
(ell-2*pi/Delta)*||c||_2^2
 <=||sum_j c_j*exp(i*gamma_j*t)||_(L2(I))^2
 <=(ell+2*pi/Delta)*||c||_2^2.                       (2.1)
```

The lower bound is useful when `ell>2*pi/Delta`.

#### Proof

Write the interval as `[t_0-ell/2,t_0+ell/2]`.  Expanding the square gives
the diagonal `ell*sum abs(c_j)^2` and the off-diagonal expression

```text
sum_(j!=k)c_j*conj(c_k)*exp(i*(gamma_j-gamma_k)*t_0)
 *2*sin((gamma_j-gamma_k)*ell/2)/(gamma_j-gamma_k).  (2.2)
```

Writing the sine as the difference of its two endpoint exponentials turns
(2.2) into the difference of two separated Hilbert sums.  The Hilbert
inequality bounds each by

```text
(pi/Delta)*sum_j abs(c_j)^2.
```

The absolute value of (2.2) is therefore at most
`(2*pi/Delta)*||c||_2^2`, proving both sides of (2.1).  QED

Put

```text
Delta=6*pi/L,       ell=aL.                           (2.3)
```

Then `2*pi/Delta=L/3`, and (2.1) is exactly (1.2).  For the exact arithmetic
lattice the conclusion at equality `a=1/3` is even sharper: integration over
one period gives `L/3` times the coefficient norm.  The strict inequality in
(1.2) is what survives arbitrary separated perturbations.

By contrast, exact-density `k=2` rows have spacing `4*pi/ell_0`, with
`ell_0/L=1+o(1)`.  Their Ingham threshold is

```text
2*pi/(4*pi/ell_0)=ell_0/2=(1/2+o(1))*L.              (2.4)
```

No fixed lobe width `a<1/2` crosses (2.4).  This is the elementary local
reason that the `k=2` geometry survives the `a>1/3` dimension ledger.

## 3. Exact target-conditioned algebra after a frame bound

This section isolates what (1.2) really proves, without replacing a
right-hand side by a worst singular vector.

Let `A_-:E_- -> C^p` and `A_+:E_+ -> C^p` be the two endpoint sampling maps
for all positive off-line rows.  Fix a right-lobe seed `r`.  The positive
row equations are

```text
A_-*ell=-A_+*r.                                      (3.1)
```

Suppose

```text
A_-*A_-^* >=A*I,             ||A_+||^2<=B.           (3.2)
```

Then (3.1) is soluble, and its minimum-norm solution obeys

```text
||ell||<=sqrt(B/A)*||r||.                            (3.3)
```

This is the Moore--Penrose formula, not a dimension argument.  For the
separated unweighted endpoint rows in Section 2,

```text
A=(a-1/3)*L,
B=(a+1/3)*L,
sqrt(B/A)=sqrt((a+1/3)/(a-1/3)).                    (3.4)
```

The selected reflected pair has endpoint-polarized coordinates

```text
positive: A_-*ell+A_+*r,
negative: A_-*ell-A_+*r.                            (3.5)
```

Consequently every solution of (3.1) satisfies, in the selected coordinate,

```text
(A_-*ell-A_+*r)_0=-2*(A_+*r)_0.                     (3.6)
```

Thus a frame estimate controls the actual inhomogeneous data and retains the
actual target.  Equations (3.3)--(3.6) are the target-conditioned statement
which a least-singular-value warning by itself does not supply.

There are two important limits to this theorem.  First, the exact
hyperbolic endpoint rows carry depth-dependent multipliers.  Absorbing a
common multiplier into a Hilbert norm is harmless only when the two lobe
maps remain uniformly equivalent in the original coefficient norm.  Second,
clusters must be represented by normalized divided differences before a
separated theorem can be applied.  Neither uniform equivalence is implied by
the present trace and Frobenius moments.

For fixed-size clusters and a uniformly conditioned local divided-difference
basis, (3.2) follows from Lemma 2.1 by a compact perturbation argument.  The
actual unit-window bound permits cluster order `O(L)`, however; allowing that
order with no local condition number is precisely the unresolved confluent
case.

## 4. The exact `alpha>1/4` conditional ledger

The separated theorem explains the proposed numerical target cleanly.  Put
a target packet at physical coordinate

```text
t_*=ell_0/3+O(1),                                    (4.1)
```

inside each proportional endpoint lobe.  For `a>1/3` this point lies in the
lobe with fixed room after an `o(L)` retreat.  A depth-`alpha` reflected pair
has squared hyperbolic response

```text
exp(2*alpha*t_*)=X^(2*alpha/3-o(1)).                 (4.2)
```

The same-lobe prime term for a lobe of length `aL` is at most

```text
X^(a/2+o(1)).                                       (4.3)
```

If the grouped zero rows, cross-prime translates, and pole rows all obeyed
the target-conditioned `X^o(1)` analogue of (3.2)--(3.6), then (4.2) would
dominate (4.3) when

```text
2*alpha/3>a/2,
equivalently alpha>3*a/4.                            (4.4)
```

Letting `a` decrease to `1/3` gives exactly

```text
alpha>1/4.                                           (4.5)
```

This is still conditional.  Lemma 2.1 proves the zero-row part only after a
separated/grouped hypothesis.  The cross-prime part additionally lives in
the Wiener atomic norm and requires its own subpower target estimate.

## 5. A bulk-compatible inward `k=2` island

The obstruction can be made sparse enough that every currently evaluated
bulk statistic is blind to it.

Let `t_c` lie in the dyadic core and put

```text
ell_0=log(t_c/(2*pi)),
s=4*pi/ell_0,             P=ell_0/2,
b=alpha/2,                X_0=exp(ell_0).             (5.1)
```

Choose a large fixed `B` and set

```text
H=L^B,            J*s=(1+o(1))*H.                   (5.2)
```

Let `psi` be the same Gevrey-2 bump used in the tapered `k=3` construction,
and put reflected simple pairs at

```text
gamma_j=t_c+beta+j*s,
alpha_j=b+(alpha-b)*psi(j/J),       abs(j)<=J.        (5.3)
```

The center pair has depth `alpha`; before each finite boundary the depth is
the constant `b`.

Fix `delta>0` and `1/3<a<1/2`.  Retreat the two physical lobes to

```text
I_+=[ell_0/2-delta-aL, ell_0/2-delta],
I_-=-I_+.                                             (5.4)
```

For large `T`, the inner endpoint of `I_+` is positive.  The retreat costs
only `o(N)` in the proportional time--bandwidth ledger because
`L-ell_0=o(L)`.  Standard finite Fourier concentration supplies a
conjugation-stable lobe space `E_(a,delta)` of dimension `(a-o(1))*N` per
polarized lobe, after the `o(N)` endpoint jets, with leakage outside (5.4)
smaller than `X^-A` for every prescribed fixed `A`.  Equivalently, one may
first prove the next estimate for exactly supported physical packets and
then transfer it to this prolate section.

For a real coefficient vector write

```text
p_c(t)=sum_k c_k*exp(-i*(tau_k-t_c)*t),

F_(j,u)(c)=integral p_c(t)*exp(u*t)
                         *exp(i*(beta+j*s)*t)dt.      (5.5)
```

The exact pair form is

```text
Q_J(c)=(2/L^2)*Re sum_(abs(j)<=J)F_(j,alpha_j)(c)^2. (5.6)
```

## 6. The two-lobe operator cap

### Proposition 6.1 (inward sparse `k=2` cap)

For the construction in Section 5,

```text
||Q_J|E_(a,delta)||<=X^(alpha/2+o(1)).               (6.1)
```

#### Proof

First replace every depth by `b`.  The sampling period is `P=ell_0/2`, and
the support (5.4) lies in an interval of length strictly less than `2P`.
Periodizing at most two pieces and applying Fourier-series Parseval gives

```text
sum_(j in Z)abs(F_(j,b)(c))^2
 <=C*P*integral abs(p_c(t))^2*exp(2*b*t)dt
 <=C*L^2*X_0^b*||c||_2^2.                           (6.2)
```

Thus the finite terminal-depth block has norm `O(X_0^b)`.

For the excess depth define, with `xi=t+u`,

```text
S_J(xi)=sum_j [exp(alpha_j*xi)-exp(b*xi)]
                         *exp(i*j*s*xi).              (6.3)
```

The Gevrey Poisson estimate is

```text
abs(S_J(xi))
 <=C*J*exp(alpha*max(xi,0))
   *sum_(q in Z)exp(-c*sqrt(H*abs(xi-q*P)/L)).        (6.4)
```

This is Lemma 5.1 of the audited tapered-island proof with the new spacing;
its proof is unchanged.  On the lobe sum-support,

```text
abs(xi)<=ell_0-2*delta.                              (6.5)
```

Hence the `q=+-2` aliases at `+-ell_0` are a fixed distance away.  Taking
`B` large makes their contribution, including the initial factor
`X_0^alpha` and every polynomial prefactor, smaller than every power of
`X_0`.  The only positive interior reciprocal alias is `q=1`, and there

```text
exp(alpha*xi)<=exp(alpha*(P+o(1)))
                 =X_0^(alpha/2+o(1)).                (6.6)
```

The `q=0,-1` aliases are no larger.  Localize (6.4) to neighborhoods of
radius `rho=L^6/H`; Schur's test costs only the polynomial factor
`J*rho/L=L^O(1)`.  Equations (6.2)--(6.6), with `b=alpha/2`, prove (6.1) for
exactly supported packets.

The unrestricted island has operator norm at most `X^(alpha+o(1))` by the
same finite sampling bound.  The `X^-A` physical leakage of the prolate
section therefore changes (6.1) by `o(1)` after choosing `A` large.  This
transfers the estimate to `E_(a,delta)`.  QED

Every on-line zero contributes a positive-semidefinite matrix `P_on`.
Compression and the variational principle give

```text
max(0,-lambda_min((Q_J+P_on)|E_(a,delta)))
 <=||Q_J|E_(a,delta)||
 <=X^(alpha/2+o(1)).                                 (6.7)
```

Further cross-prime, pole, or jet constraints only compress the space and
cannot invalidate this upper bound.

## 7. Count and moment audit

The pair-center density is `ell_0/(4*pi)`, and each center contributes two
points.  Thus the point density inside the island is exactly

```text
ell_0/(2*pi),                                        (7.1)
```

the local Riemann--von Mangoldt density.  Since `H=L^B`, replacing the slowly
varying density by (7.1) creates interval discrepancy

```text
O(1+H^2/T)=O(1).                                     (7.2)
```

Count rounding at the two boundaries is bounded.  Put every point outside
the island simply on the critical line.  The global off-line fraction is
`O(H/T)=o(1)`, all points are simple and distinct, reflection is exact, and
the unit-window count is `O(L)`.

For the independent legal bandwidth-one Zeta23 moment probe, the same
spacing has reciprocal period `P=ell_0/2`; its endpoint mollifier removes
the `q=2` boundary, while `q=1` has scale `X_0^(alpha/2)`.  Repeating the
operator estimate gives

```text
rank Q_J^(0)=O(HL),
||Q_J^(0)||op<=X^(alpha/2+o(1)),
||Q_J^(0)||F^2<=H*L*X^(alpha+o(1))=o(N).             (7.3)
```

The trace is also `o(N)`.  Replacing the same `O(HL)` on-line background
points costs Frobenius square `O(HL^3)=o(N)`.  Cauchy--Schwarz with the
background then shows that both evaluated leading moments change by `o(N)`.
The pair-correlation expression is the same Frobenius moment.  Thus (6.7)
is compatible with every bulk input currently used in this branch.

## 8. The remaining positive theorem

The all-configuration statement requested by the two-lobe strategy is false
on the present abstract input class, but the positive route has become more
specific rather than disappearing.

A sufficient new zeta-side package is:

1. after discarding rows of depth too small to compete with
   `X^(2alpha/3)`, partition the remaining local rows into collision groups;
2. prove that the group centers have effective upper density strictly below
   `L/(6*pi)` on every scale from `L^B` to `T`;
3. put each group in a collision-stable divided-difference basis and prove a
   subpower bound for the resulting local confluent condition number; and
4. prove the coupled Wiener-atomic subpower estimate for the cross-prime and
   pole rows.

Items 2--3 upgrade Lemma 2.1 to the exact maps in (3.1).  Equations
(3.3)--(3.6) then retain the selected target, and (4.2)--(4.5) give the
conditional right edge `3/4+epsilon`.

The current Riemann--von Mangoldt discrepancy, global simple-line density,
horizontal zero-density estimates, and leading trace/Frobenius identities
do not imply item 2 on polylogarithmic islands.  Proposition 6.1 is an exact
witness.  Therefore the next useful arithmetic input is a **localized deep-
pair correlation or higher-moment theorem**, not another global first or
second moment.

This is the precise surviving gate.  No conclusion about an actual zeta
zero, and no zero-free strip, follows from the results in this note alone.
