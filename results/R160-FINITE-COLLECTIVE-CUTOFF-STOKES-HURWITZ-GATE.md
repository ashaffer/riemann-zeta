# R160 finite collective cutoff Stokes--Hurwitz gate

## Status

R155 and R161 show that one truncated-zeta skeleton cannot avoid its forced
mixed points.  A natural denominator-free workaround is to combine several
nearby skeletons before applying the nonlinear filter.  Put

```text
A_x(s)=product_(p<=x)(1-p^(-s)),
E_x(s)=zeta(s)A_x(s),
P_H(s)=1-sum_(j=1)^J w_j(H)[E_(H_j)(s)-1]^q,              (0.1)
```

where `q>=2` is fixed and even, `sum_j w_j(H)=1`, and

```text
H_j/H -> c_j,                 0<c_1<...<c_J.              (0.2)
```

The weights may be arbitrary complex numbers depending on `H`.  They need
not be positive, bounded, or polynomially conditioned.

Every channel in (0.1) has exactly the zeta divisor in `Re(s)>0`.  The sum
also factors exactly as

```text
P_H(s)=zeta(s) C_H(s).                                    (0.3)
```

At a fixed finite cutoff, complex weights can make `C_H` zero-free on a
prescribed disc; there is no pointwise algebraic or winding obstruction.
The cofinal statement needed by the nonlinear high-jet proof is nevertheless
false.

> **Finite collective-cutoff theorem.**  Let `Omega` be any nonempty open
> subset of `1/2<Re(s)<1`.  For fixed `J`, fixed even `q`, and fixed distinct
> ratios (0.2), there is no sequence `H -> infinity` and no choice of scalar
> weights `w_j(H)` with `sum_j w_j(H)=1` for which `C_H` is zero-free on
> `Omega`.  Equivalently, for all sufficiently large `H`, every such scalar
> combination has an artificial cofactor zero in `Omega`.

The proof is local and unconditional.  Along a vertical displacement of
size `1/log H`, the endpoint prime sum rotates through a full phase.  No one
wave in the finite expansion of `C_H` can dominate throughout that rotation,
because its first- and `q`th-power siblings exchange dominance.  At an exact
co-maximal point, rescaling by `H^(Re(s_0)-1)` produces a nonmonomial finite
exponential polynomial.  Such a polynomial has a complex zero.  Hurwitz's
theorem then contradicts zero-freeness of the cofactors.

This closes finite scalar banks of nested full cutoffs, including constant,
fixed-power, exponentially large, and exponentially small `H`-dependent
weights.  It does **not** cover a growing number of channels, growing `q`,
cutoff ratios without fixed limits, or independent signed choices at each
prime.  In particular, optional local exponents between `H` and `Y` have a
growing phase dimension and remain outside the theorem.

```text
exact common-zeta factorization                              THEOREM
arbitrary finite scalar-weight conditioning                 ALLOWED
co-maximal cutoff wave in every full phase turn             THEOREM
microscopic exponential-polynomial limit                    THEOREM
cofinal zero-free collective cofactor                       IMPOSSIBLE
finite-H zero-free weight chambers                          NOT EXCLUDED
fixed-J nested/full-cutoff scalar workaround                CLOSED
growing signed optional-prime phase family                  NOT COVERED
fixed uniform zeta zero-free strip                          NOT PROVED
zeros approaching one                                      NOT PROVED
```

Date: 2026-08-08.

Predecessors:
[`R153-NONLINEAR-SUPPORT-AMPLIFIER-AND-MIXED-VALUE-GATE.md`](R153-NONLINEAR-SUPPORT-AMPLIFIER-AND-MIXED-VALUE-GATE.md),
[`R155-NORMAL-FAMILY-MIXED-VALUE-INEVITABILITY-GATE.md`](R155-NORMAL-FAMILY-MIXED-VALUE-INEVITABILITY-GATE.md),
[`R156-MOVING-VALUE-AND-SIGNED-MIXED-PACKET-GATE.md`](R156-MOVING-VALUE-AND-SIGNED-MIXED-PACKET-GATE.md),
and
[`R158-CONDITIONED-MIXED-POINT-FAMILY-AND-SKELETON-GATE.md`](R158-CONDITIONED-MIXED-POINT-FAMILY-AND-SKELETON-GATE.md).

Companion:
[`R161-DETERMINISTIC-SKELETON-MICROCLOUD-AND-SPECTRAL-SHIFT-GATE.md`](R161-DETERMINISTIC-SKELETON-MICROCLOUD-AND-SPECTRAL-SHIFT-GATE.md).

## 1. Exact common-divisor factorization

For even `q`, define

```text
Q_q(z)=[1-(z-1)^q]/z
      =sum_(m=1)^q d_m z^(m-1),
d_m=(-1)^(m+1) binom(q,m).                                (1.1)
```

The apparent singularity at zero is removable and

```text
Q_q(0)=q.                                                  (1.2)
```

Since the weights in (0.1) sum to one,

```text
P_H
 =sum_j w_j[1-(E_(H_j)-1)^q]
 =sum_j w_j E_(H_j)Q_q(E_(H_j))
 =zeta C_H,                                                (1.3)
```

where

```text
C_H=sum_j w_j A_(H_j)Q_q(zeta A_(H_j))
   =sum_j sum_(m=1)^q
      d_m w_j zeta^(m-1) A_(H_j)^m.                       (1.4)
```

Thus `C_H` is a finite sum of exactly `Jq` cutoff waves, after zero-weight
channels are removed.  On `Re(s)>0`, every `A_(H_j)` is nonzero.  On any
domain avoiding the pole of zeta, (1.4) is holomorphic, including at zeta
zeros.

If `rho` is a zeta zero, then

```text
C_H(rho)=q sum_j w_j A_(H_j)(rho).                         (1.5)
```

Consequently `P_H` has the same multiplicity as zeta at `rho` exactly when
the right side of (1.5) is nonzero.  If it vanishes, the common target divisor
has become more singular rather than easier to isolate.

For later use, name the individual waves

```text
T_(j,m;H)(s)
 =d_m w_j(H) zeta(s)^(m-1) A_(H_j)(s)^m.                  (1.6)
```

Then `C_H=sum_(j,m)T_(j,m;H)`.

For two channels, writing `C_H=w C_1+(1-w)C_2` shows the finite-cutoff
projective geometry explicitly.  Away from poles and zeros of the ratio,

```text
C_H(s)=0
 iff C_1(s)/C_2(s)=1-1/w.                                (1.7)
```

Choosing `w` asks one meromorphic ratio to omit one value on the chosen
disc.  This can happen at a finite cutoff.  The theorem below is therefore
an asymptotic prime-phase statement, not a formal linear-algebra obstruction.

## 2. Uniform endpoint asymptotics

Let `K` be a compact subset of `0<Re(s)<1`.  The prime number theorem and
partial summation give, uniformly on a fixed complex neighborhood of `K`,

```text
sum_(p<=x)p^(-s)
 =x^(1-s)/[(1-s)log x]
  +O_K(x^(1-Re(s))/(log x)^2)+O_K(1).                     (2.1)
```

The higher prime powers are uniformly bounded on compact subsets of
`Re(s)>1/2`.  Hence, for the branch obtained by expanding every finite Euler
factor,

```text
log A_x(s)
 =-x^(1-s)/[(1-s)log x]
  +O_K(x^(1-Re(s))/(log x)^2)+O_K(1).                     (2.2)
```

Applying Cauchy's formula on circles of radius `1/log x` contained in a
slightly larger compact set gives

```text
[log A_x]'(s)=x^(1-s)/(1-s)+o_K(x^(1-Re(s))),             (2.3)

[log A_x]''(s)=O_K(x^(1-Re(s))log x).                     (2.4)
```

Fix

```text
s_0=sigma_0+i t_0,              1/2<sigma_0<1,            (2.5)
ell=log H,
X=H^(1-sigma_0),
Y=X/ell.                                                     (2.6)
```

For bounded real `u`, put

```text
s(u)=s_0+i u/ell.                                         (2.7)
```

Equations (0.2) and (2.2) imply, uniformly on every bounded `u`-interval,

```text
log A_(H_j)(s(u))
 =-c_j^(1-s_0) H^(1-s_0)e^(-iu)/[(1-s_0)ell]+o(Y).        (2.8)
```

In particular, as `u` traverses an interval of length greater than `2 pi`,
the leading real part in (2.8) takes both signs with magnitude comparable to
`Y`.  On a zero-free neighborhood of `s_0`, `log|zeta|=O(1)`, so for every
fixed channel `j` there are bounded `u_+(j,H),u_-(j,H)` for which

```text
log|E_(H_j)(s(u_+))|>=a_jY,
log|E_(H_j)(s(u_-))|<=-a_jY                               (2.9)
```

with a fixed `a_j>0` and all sufficiently large `H`.

This full sign turn is the only magnitude input needed below.  Notice that
it is independent of the scalar weights.

## 3. An exact co-maximal wave

Choose `s_0` inside the prescribed open set `Omega` so that

1. zeta is finite and nonzero in a neighborhood of `s_0`; and
2. the finitely many numbers

```text
m c_j^(1-s_0),                  1<=j<=J, 1<=m<=q,          (3.1)
```

are pairwise distinct.

Such points are dense.  Zeta zeros are isolated, and for `j!=k` every
collision in (3.1) solves the nonconstant analytic equation

```text
(c_j/c_k)^(1-s)=n/m.                                      (3.2)
```

For a nonzero-weight channel define on the bounded interval from Section 2

```text
h_(j,m;H)(u)=log|T_(j,m;H)(s(u))|.                        (3.3)
```

These are finitely many continuous real functions.  Within one channel,

```text
h_(j,n;H)(u)-h_(j,m;H)(u)
 =log|d_n/d_m|+(n-m)log|E_(H_j)(s(u))|.                   (3.4)
```

Equation (2.9) now gives the crucial exchange:

- if `m<q`, the `q`th wave is larger than the `m`th wave at a positive
  endpoint phase;
- if `m=q`, the first wave is larger at a negative endpoint phase.

Thus no individual wave can maximize all the functions (3.3) throughout a
full phase turn.  If the maximum were unique at every `u`, its maximizing
index would be locally constant.  A locally constant map from a connected
interval to a finite set is constant, contradicting the preceding exchange.
We have proved:

### Lemma 3.1 -- co-maximal phase

For every sufficiently large `H` and every nonzero scalar weight vector,
there is a bounded `u_H` and at least two distinct active indices
`(j,m)!=(k,n)` such that

```text
|T_(j,m;H)(s_H)|=|T_(k,n;H)(s_H)|
 =max_(a,b)|T_(a,b;H)(s_H)|,
s_H=s_0+i u_H/log H.                                     (3.5)
```

The assertion allows any magnitude and phase for the weights.  Exponentially
small channels may disappear from the maximum; exponentially large channels
still contain their own first-to-`q`th exchange.

## 4. The microscopic entire limit

Assume for contradiction that a sequence of cofactors `C_H` is zero-free on
`Omega`.  Choose `s_H` by Lemma 3.1.  Passing to a subsequence, the same pair
of indices is co-maximal for every `H`, the bounded `u_H` converges, and the
unit complex numbers

```text
H^(-it_0)e^(-iu_H)                                       (4.1)
```

converge.

Set

```text
delta_H=H^(sigma_0-1)=1/X,
s=s_H+delta_H z.                                          (4.2)
```

For every fixed `R`, (2.3)--(2.4) give uniformly on `|z|<=R`

```text
log[T_(j,m;H)(s_H+delta_H z)/T_(j,m;H)(s_H)]
 =lambda_(j,m;H) z+o_R(1),                                (4.3)
```

where, after the chosen subsequence,

```text
lambda_(j,m;H) -> lambda_(j,m)
 =omega m c_j^(1-s_0)/(1-s_0),                            (4.4)
```

and `|omega|=1`.  The zeta logarithmic derivative contributes only
`O(delta_H)` in (4.3).  The second derivative error is

```text
O_R(delta_H^2 X log H)=O_R((log H)/X)=o_R(1).              (4.5)
```

The generic choice (3.1) makes the limiting slopes in (4.4) pairwise
distinct.

Choose one co-maximal wave `T_(j_0,m_0;H)` and divide by it.  At `s_H`, every
normalized wave coefficient has modulus at most one, and at least one other
coefficient has modulus exactly one.  Compactness of the closed unit disc and
finiteness of the wave set allow a further subsequence on which all these
coefficients converge.  Equations (4.3)--(4.4) then give locally uniformly on
the whole `z`-plane

```text
C_H(s_H+delta_H z)/T_(j_0,m_0;H)(s_H+delta_H z)
 -> G(z),                                                  (4.6)

G(z)=sum_(j,m) a_(j,m)
 exp[(lambda_(j,m)-lambda_(j_0,m_0))z].                   (4.7)
```

At least two coefficients in (4.7) are nonzero, and their exponents are
distinct.  Therefore `G` is neither zero nor a single exponential.

The rescaling domain exhausts the plane: for every fixed `R`, the physical
disc `|s-s_H|<=R delta_H` lies in `Omega` for large `H`.  The denominator in
(4.6) is nonzero there because zeta was chosen zero-free near `s_0`, every
finite Euler factor is nonzero in `Re(s)>0`, and the selected weight is
nonzero.

## 5. A nonmonomial exponential polynomial has a zero

### Lemma 5.1 -- zero-free exponential sums are monomials

Let

```text
G(z)=sum_(nu=1)^N a_nu exp(lambda_nu z),                  (5.1)
```

where the `lambda_nu` are distinct and at least two `a_nu` are nonzero.
Then `G` has a complex zero.

#### Proof

The function in (5.1) is entire of exponential type and hence of order at
most one.  If it were zero-free, Hadamard factorization for a zero-free
entire function of finite order would give

```text
G(z)=exp(az+b).                                            (5.2)
```

Linear independence of exponentials with distinct exponents then forces all
but one coefficient in (5.1) to vanish.  This contradicts the hypothesis.
QED.

The lemma applies to (4.7), so `G` has a zero.  But the left side of (4.6)
is zero-free on every fixed `z`-disc for all sufficiently large `H` under the
contradiction hypothesis.  Hurwitz's theorem says that its locally uniform
limit is either zero-free or identically zero.  Equation (4.7) is neither.
This contradiction proves the main result.

### Theorem 5.2 -- finite collective-cutoff Stokes--Hurwitz theorem

Let `q>=2` be fixed and even, let `J` be fixed, and suppose

```text
H_j(H)/H -> c_j,                 0<c_1<...<c_J.            (5.3)
```

For every `H`, let the complex scalar weights satisfy only

```text
sum_(j=1)^J w_j(H)=1.                                    (5.4)
```

Define `P_H` and `C_H=P_H/zeta` by (0.1)--(1.4).  Then for every nonempty
open set

```text
Omega compactly contained in {1/2<Re(s)<1},               (5.5)
```

`C_H` has a zero in `Omega` for every sufficiently large `H`.

Equivalently, there is no cofinal sequence of finite scalar cutoff banks for
which the only zeros of `P_H` in `Omega` are the zeta zeros.

#### Quantifiers

The threshold in Theorem 5.2 is uniform over the weights.  Otherwise one
could choose arbitrarily large cutoffs and offending weight vectors, obtain
an infinite zero-free sequence, and run the compactness proof above.

The compact-containment wording in (5.5) is only to leave rescaling room.
Every nonempty open subset of the strip contains such a smaller open set, so
the theorem applies to an arbitrary fixed target localization disc through
any interior subdisc lying in `1/2<Re(s)<1`.

### Corollary 5.3 -- local cofactor count diverges

For every fixed nonempty open `Omega` compactly contained in the strip,

```text
N(Omega,C_H=0) -> infinity                                (5.6)
```

uniformly over the scalar weights, with multiplicity allowed.

Indeed, for any fixed `M`, choose `M` pairwise disjoint open subdiscs of
`Omega` and apply Theorem 5.2 to each.  Taking the maximum of their finitely
many cutoff thresholds gives at least one cofactor zero in every subdisc.
This argument is qualitative; unlike the single-skeleton theorem R161, it
does not give a polynomial rate for the collective count.

## 6. Exact first-layer coefficient conditioning

The Stokes--Hurwitz proof does not require a bound on the weights.  There is
also an independent arithmetic reason that large cancelling weights cannot
be hidden inside an absolute Euler estimate.

In `Re(s)>1`, put

```text
U_j(s)=E_(H_j)(s)-1
      =sum_(n>1, P^-(n)>H_j)n^(-s),
V(s)=sum_j w_j U_j(s)^q,
P_H=1-V.                                                   (6.1)
```

Here `P^-(n)` is the least prime factor.  Let

```text
W_l=sum_(j<=l)w_j,
I_l=(H_l,H_(l+1)],                                       (6.2)
```

and append any `H_(J+1)~c_(J+1)H` with `c_(J+1)>c_J`.
If

```text
n=p_1...p_q,                                               (6.3)
```

where the `p_i` are distinct primes in `I_l`, then every factorization of
`n` into `q` nonunit `H_j`-rough factors assigns one prime to each factor.
There are exactly `q!` assignments.  Therefore

```text
[n^(-s)]V=q! W_l.                                         (6.4)
```

The logarithmic response is

```text
B_H=P_H'/P_H=-V'/(1-V).                                   (6.5)
```

Every term involving a positive power of `V` has at least `2q` nonunit
prime factors.  Thus the same squarefree `q`-prime layer in (6.5) is exact:

```text
[n^(-s)]B_H=q! W_l log n.                                 (6.6)
```

Since `w_j=W_j-W_(j-1)`, with `W_0=0` and `W_J=1`,

```text
max_(0<=l<=J)|W_l| >=(1/2)max_j|w_j|.                     (6.7)
```

For fixed real `sigma>1`, the prime number theorem gives

```text
sum_(p in I_l)p^(-sigma)
 asymp H^(1-sigma)/log H.                                 (6.8)
```

The repeated-prime diagonals are lower order, so restricting the absolute
Dirichlet norm of (6.5) to (6.3) yields

```text
sum_n |[n^(-s)]B_H|n^(-sigma)
 >>_(q,c,sigma)
 max_j|w_j| H^(-q(sigma-1))(log H)^(1-q).                 (6.9)
```

If the formal reciprocal series is not absolutely convergent at the chosen
`sigma`, the left side of (6.9) is interpreted as infinity; the exact
coefficient statement (6.6) is independent of convergence.

Thus an exponentially ill-conditioned signed bank cannot be made cheap by
regrouping its first Euler layer.  Equation (6.9) is an absolute-coefficient
statement; it does not forbid pointwise complex cancellation on one vertical
arc.  The weight-uniform analytic obstruction is Theorem 5.2.

## 7. Consequence for the nonlinear strip program

The exact logarithmic identity is

```text
B_H=P_H'/P_H=zeta'/zeta+C_H'/C_H.                         (7.1)
```

The nonlinear Euler side still begins at the `q`-fold rough layer.  If
`C_H` were zero-free on the localization disc, (7.1) would contain only the
fixed zeta divisor there and the R153 high-jet comparison could close after
choosing `q` large enough.  Theorem 5.2 proves that this premise fails for
every finite bank of comparable full cutoffs: `C_H'/C_H` necessarily has an
artificial local pole for all large cutoffs.

Ordinary absolute zero counting cannot erase that diverging pole cloud.  On
a compact set whose left edge is `sigma_L<1`, (2.2) only gives

```text
log^+|P_H|
 << log^+(1+sum_j|w_j|)
    +q H^(1-sigma_L)/log H.                               (7.2)
```

With `H=exp(beta k)`, this ledger is much larger than the bounded local
divisor count needed by the high-jet Turan step.  The mandatory cofactor zeros
must therefore be included in a signed joint reciprocal-power estimate; a
finite scalar cutoff bank does not remove them.

This result proves neither that zeta has a fixed zero-free strip nor that
zeros approach `Re(s)=1`.  It closes one proposed denominator-free route to
the strip.

## 8. Scope and the live escape

The proof uses three finite-dimensional facts:

1. there are only `Jq` waves;
2. their cutoff derivative slopes converge to the fixed finite set
   `m c_j^(1-s_0)`; and
3. each scalar channel carries all powers `m=1,...,q` with one common weight.

It does not apply when the number of independent prime controls grows with
`H`.  One explicit family outside the theorem is

```text
F_epsilon(s)
 =E_H(s) product_(H<p<=Y)(1-p^(-s))^(epsilon_p),
epsilon_p in {+1,-1}.                                    (8.1)
```

At a prime in `(H,Y]`, the total local factor is respectively

```text
1                         if epsilon_p=+1,
(1-p^(-s))^(-2)           if epsilon_p=-1.                (8.2)
```

Thus (8.1) retains nonnegative coefficients and exact head deletion, while
its logarithm has genuinely independent signed prime controls.  Its phase
space grows with the number of optional primes and does not converge to the
fixed slope set used in (4.4).  R160 therefore supplies no no-go theorem for
a Pechersky-style signed optional-prime construction or for a signed joint
estimate built from it.

The distinction is sharp:

```text
fixed finite full-cutoff scalar bank             CLOSED by Theorem 5.2;
growing independent optional-prime phase bank    OPEN arithmetic route.
```
