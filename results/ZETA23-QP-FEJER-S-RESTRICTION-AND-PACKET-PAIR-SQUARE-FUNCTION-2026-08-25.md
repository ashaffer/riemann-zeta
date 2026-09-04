# QP reciprocal strip: the completion-sum restriction theorem and packet-pair square function

**Date:** 2026-08-25  
**Verdict:** a phase-only fixed-`S` vector-valued large sieve does not separate
spatially remote reciprocal-strip points from a tangent packet.  All points
in the narrow target mask have coherent Fejer sampling vectors.  The correct
weaker norm for the fourth-trace application is instead Fourier restriction
in the **completion-sum variable** `S`.

This change gives a sharper rigorous reduction.  Plain Young convolution
already closes every squared-Fejer mask satisfying

```text
m^2*M^3>=sqrt(D),       m=min(U,V), M=max(U,V).       (0.1)
```

Thus the unresolved balanced energy core is `U,V<D^(1/10)`, rather than the
`D^(1/6)` core left by the pointwise fixed-`S` route.  The remaining theorem
is a sharp packet-pair square function.  It is not proved here, so the sharp
four-cycle bound remains open.

## 1. Why the fixed-`S` Fejer `TT*` cannot see spatial dispersion

Let `N asymp H=q/D`, and use the normalized Fejer kernel

```text
P(theta)=C_0/N^2 * |sum_(0<=r<N)e(r*theta)|^2.       (1.1)
```

One Fejer--Riesz factor has constant coefficients

```text
alpha_r=sqrt(C_0)/N,       0<=r<N.                  (1.2)
```

Put `b=alpha tensor alpha` and

```text
phi_a(r,s)=e(r*theta_1(a)+s*theta_2(a)),
theta_1(a)=C/a,       theta_2(a)=C/(S-a)  (mod 1).   (1.3)
```

Then exactly

```text
|<b,phi_a>|^2=P(theta_1(a))*P(theta_2(a)).           (1.4)
```

If both `||theta_j(a)||<=kappa/N`, for a sufficiently small fixed `kappa`,
the sine quotient gives

```text
|<b,phi_a>|^2>=c_kappa>0.                            (1.5)
```

Consequently, for **every** set `E` in the central reciprocal mask,

```text
<b,G_E*b>=sum_(a in E)|<b,phi_a>|^2>=c_kappa*|E|,
G_E=sum_(a in E) phi_a*phi_a^*.                      (1.6)
```

Since `||b||_2^2=C_0^2/N^2`, this implies

```text
||G_E||>=c*N^2*|E|.                                  (1.7)
```

The same statement holds after deleting any chosen tangent packet: replace
`E` by the residual set.  Thus spatially remote residual blocks do not become
orthogonal in this coefficient space.  Their reciprocal phases all lie in
the same `1/H` box and their sampling vectors remain coherent.

In particular, a post-subtraction estimate

```text
||G_E||<<N^2*sqrt(D)*q^o(1)                          (1.8)
```

is just the cardinality statement `|E|<<sqrt(D)*q^o(1)` in operator form.
No phase-only `TT*`, generic torus large sieve, or tangent projection proves
it.  This is a no-go for that implementation, not for Fourier analysis in a
different variable.

## 2. The actual fourth-trace norm is an `S`-aggregate

For a dyadic reciprocal mask define

```text
A_U={a in I_q:||C/a||<=c*U/H},
A_V={b in I_q:||C/b||<=c*V/H}.                       (2.1)
```

Write their indicators as `f_U,f_V`.  The fixed-sum count is the exact
ordinary additive convolution

```text
N_S(U,V)=(f_U*f_V)(S)
        =sum_a f_U(a)f_V(S-a).                       (2.2)
```

The completion energy occurring in the error-labelled fourth-moment
reduction is not `max_S N_S`; for arbitrary complex coefficients it has the
form

```text
E_(U,V)(z,y)
 =sum_S |sum_(a+b=S) z_a*y_b|^2
 =||z*y||_2^2
 =integral_0^1 |zhat(alpha)|^2|yhat(alpha)|^2 dalpha. (2.3)
```

Here `z` and `y` are supported on the corresponding reciprocal-strip
projections.  Equation (2.3) is an exact vector-valued Fourier restriction
norm in the variable dual to `S`.  It retains arbitrary selected weights;
no sign cancellation in those weights is assumed.

For `U=V=1`, the desired theorem is

```text
sum_S |sum_(a+b=S) z_a*z_b|^2
 <<sqrt(D)*q^o(1)*(sum_a |z_a|^2)^2.                 (2.4)
```

This is strictly weaker than the pointwise theorem
`N_S(1,1)<<sqrt(D)q^o(1)`, while being exactly at the missing
error-coherence scale.  A pointwise bound implies (2.4) by Cauchy--Schwarz,
but the converse need not hold.

The flat specialization of (2.4) is

```text
E^+(A(C,D))<<sqrt(D)*|A(C,D)|^2*q^o(1)
           <<D^(5/2)*q^o(1),                         (2.5)
```

the projected reciprocal-energy gate already isolated in the earlier
error-coherence audit.  For a theorem uniform in all original coefficients,
the hereditary weighted form (2.4), or its post-peeling analogue, is the
clean statement; a bound only for the full unweighted set does not by itself
control an adversarial weighted subset.

## 3. The sharp mask-sensitive restriction theorem

Put `m=min(U,V)`.  The natural vector-valued statement is

> **Conjectural reciprocal-strip restriction theorem (RSR).** Uniformly in
> the physical shell, the centre `C`, the dyadic widths, and arbitrary
> complex sequences supported as in (2.1),
>
> ```text
> ||z*y||_2^2
>  <<sqrt(D*m)*q^o(1)*||z||_2^2*||y||_2^2.           (3.1)
> ```

The dependence on the narrower mask is necessary.  At the symmetric centre
`C=Q^2`, the strip contains the tangent intervals

```text
a=Q+h,       v=Q-h,       |h|<<sqrt(D*U).            (3.2)
```

For a normalized flat vector on an interval of length `L`, one has exactly

```text
||z*z||_2^2=(2*L^3+L)/(3*L^2)
            =2*L/3+1/(3*L).                         (3.3)
```

Thus (3.1) is saturated, up to constants, when the smaller tangent interval
has length `L asymp sqrt(D*m)`.

For flat indicators, (3.1) gives the mixed energy estimate

```text
sum_S N_S(U,V)^2
 <<D^(5/2)*U*V*sqrt(m)*q^o(1),                       (3.4)
```

because the one-product divisor count gives

```text
|A_U|<<D*U*q^o(1),       |A_V|<<D*V*q^o(1).         (3.5)
```

Equation (3.1), rather than a uniform operator bound for the reciprocal
Fejer sampling vectors, is the precise mask-sensitive vector-valued theorem
suggested by the fourth-trace norm.

There is an equivalent hereditary flat formulation, up to logarithms.  For
every `B subset A_U` and `E subset A_V`, require

```text
||1_B*1_E||_2^2
 <<sqrt(D*m)*|B|*|E|*q^o(1).                         (3.6)
```

Indeed, decompose `|z|` and `|y|` into dyadic amplitude levels.  Minkowski
followed by (3.6) gives

```text
||z*y||_2
 <<(D*m)^(1/4)
   [sum_j 2^(-j)*sqrt(#B_j)]
   [sum_k 2^(-k)*sqrt(#E_k)]*q^o(1).
```

Cauchy--Schwarz over the `O(log q)` nonempty levels recovers (3.1).  The
reverse implication follows by taking indicator coefficients.  Therefore a
bound only for the full sets `A_U,A_V` is insufficient; the theorem must
survive arbitrary subset selection.  This is exactly the uniformity demanded
by the original coefficients.

## 4. The concrete Fejer coefficients close under (RSR)

Let

```text
p(a)=W(a)*P(C/a),       0<=W<=1.                    (4.1)
```

The squared fixed-sum Fejer majorant is

```text
sum_S |(p*p)(S)|^2=integral_0^1 |phat(alpha)|^4 dalpha. (4.2)
```

Dyadically, `p` is majorized by

```text
sum_(U dyadic) U^(-2)*1_(A_U).                       (4.3)
```

Assume (3.1).  Minkowski, (3.4), and (3.5) give, for `m<=M`,

```text
||1_(A_m)*1_(A_M)||_2
 <<D^(5/4)*m^(3/4)*M^(1/2)*q^o(1).                  (4.4)
```

After the two Fejer weights, one dyadic term is

```text
<<D^(5/4)/(m^(5/4)*M^(3/2))*q^o(1).                 (4.5)
```

The dyadic double sum converges geometrically.  Therefore

```text
||p*p||_2<<D^(5/4)*q^o(1),
sum_S |(p*p)(S)|^2<<D^(5/2)*q^o(1).                 (4.6)
```

This is the desired completion-energy scale.  It does not prove the
pointwise bound `p*p(S)<<sqrt(D)` and does not need to.

## 5. An unconditional energy-tail improvement

Even without (RSR), Young's inequality and (3.5) give, for `m<=M`,

```text
sum_S N_S(m,M)^2
 <=min(|A_m|^2*|A_M|, |A_M|^2*|A_m|)
 <<D^3*m^2*M*q^o(1).                                (5.1)
```

After the squared Fejer weight `m^(-4)M^(-4)`, this is

```text
<<D^3/(m^2*M^3)*q^o(1).                             (5.2)
```

Hence every mask with

```text
m^2*M^3>=sqrt(D)                                    (5.3)
```

already contributes at most `D^(5/2)q^o(1)` to the squared Fejer norm.
There are only logarithmically many masks.  The remaining energy core is

```text
m^2*M^3<sqrt(D).                                    (5.4)
```

Consequences at the exponent level are:

```text
balanced m=M:       U,V<D^(1/10),
most unbalanced m=1: M<D^(1/6).                     (5.5)
```

This is a strict contraction from the pointwise Fejer core
`m*M^2<sqrt(D)`, whose balanced endpoint is `D^(1/6)` and most unbalanced
endpoint is `D^(1/4)`.

The improvement is specific to the norm actually needed: squaring and
summing in `S` lets Young use the full completion-sum aggregate.  It says
nothing pointwise about an exceptional `S`.

## 6. What averaging in `S` proves, and what it does not

The first moment is even simpler:

```text
sum_S N_S(U,V)=|A_U|*|A_V|<<D^2*U*V*q^o(1).         (6.1)
```

Therefore

```text
#{S:N_S(U,V)>sqrt(D*m)}
 <<D^(3/2)*sqrt(m)*M*q^o(1).                        (6.2)
```

In the pointwise core `m*M^2<sqrt(D)`, the right side is at most

```text
D^(7/4)*q^o(1)=q^(28/33+o(1)).                      (6.3)
```

For the full Fejer weight, the one-strip estimate

```text
sum_a P(C/a)<<D*q^o(1)                              (6.4)
```

gives

```text
sum_S (p*p)(S)<<D^2*q^o(1),
#{S:(p*p)(S)>sqrt(D)}<<D^(3/2)*q^o(1).              (6.5)
```

Thus any failure of the pointwise theorem is confined to a power-sparse set
of completion sums.  This does not close a theorem with arbitrary selected
weights: the weights may concentrate on the exceptional sums.  Likewise,
integrating the weak first-moment tail only recovers the cubic Young ceiling,
not the required `D^(5/2)` energy.  A weak-`ell^2` improvement in the upper
tail, or (RSR) directly, is still necessary.

For example, in the central flat mask put `N_S=N_S(1,1)`.  A dyadic layer-
cake argument shows that the required energy follows from

```text
#{S:N_S>=T}<<D^(5/2)*T^(-2)*q^o(1),
sqrt(D)<=T<=D.                                      (6.6)
```

The first moment (6.1) gives only `D^2/T`.  The ratio between this and (6.6)
is exactly `T/sqrt(D)`.  At the entrance `T=sqrt(D)` there is no loss; the
whole missing square root is an upper-tail concentration problem.  This is
another precise, unweighted formulation of the packet-pair inverse theorem,
but it is not a substitute for the hereditary weighted estimate (3.1).

## 7. Packet-pair square function: the exact new-mathematics target

The local determinant theorem partitions each short `q^(1/3)` completion
block into at most one affine reciprocal packet plus two atoms.  A packet in
the `U` mask has the form

```text
a=a_0+R*t,       v=v_0-P*t,
#packet<<1+sqrt(D*U/(R*P))<=1+sqrt(D*U).             (7.1)
```

Write `z=sum_i z_i` and `y=sum_j y_j` according to these packets.  Suppose
one could prove the packet-pair square function

```text
||sum_(i,j) z_i*y_j||_2^2
 <<q^o(1)*sum_(i,j)||z_i*y_j||_2^2.                 (7.2)
```

Young on each pair gives

```text
||z_i*y_j||_2^2
 <=min(#P_i,#Q_j)*||z_i||_2^2*||y_j||_2^2
 <<sqrt(D*m)*||z_i||_2^2*||y_j||_2^2.               (7.3)
```

Summing (7.3) proves (RSR).  More elementarily, (7.2) follows if at every
output sum only `q^o(1)` packet-pair sumsets overlap.  Pointwise Cauchy then
gives the same result.

This identifies the genuine major/minor-arc split:

* the major arc is the internal convolution of one affine tangent packet,
  paid sharply by its `sqrt(D*m)` length;
* the minor-arc theorem is almost orthogonality of **different packet-pair
  completion sums**, in the Fourier variable dual to `S`;
* a large overlap must be classified arithmetically and merged into an
  already controlled affine/Hankel component.

An abstract family of remote singleton blocks can violate (7.2), so generic
Fourier decoupling by spatial location is insufficient.  The proof must use
the reciprocal product bands to show that high packet-pair overlap forces a
common tangent chart, or else produces cancellation in the `S`-Fourier
extension operator.  This is precisely where new arithmetic restriction
theory is needed.

## 8. Fixed `S` versus `S`-average: binary status

```text
fixed-S phase-only Fejer orthogonality after tangent deletion: FALSE;
central-mask coherence lower bound (1.6)--(1.7):       PROVED;
completion count as additive convolution (2.2):        EXACT;
weighted completion energy as S-Fourier restriction:   EXACT;
(RSR) with sharp sqrt(D*m) constant:                    OPEN;
one tangent packet saturates (RSR):                     PROVED;
(RSR) implies Fejer energy D^(5/2):                     PROVED;
Young energy masks m^2*M^3>=sqrt(D):                   CLOSED;
balanced unresolved energy mask range:                 U,V<D^(1/10);
bad fixed sums in pointwise core:                       <=D^(7/4+o(1));
bad fixed sums may carry arbitrary selected weights:    YES;
packet-pair square function (7.2):                      OPEN;
sharp four-cycle bound:                                 NOT PROVED.
```

The finite Fejer identity, interval saturation, convolution identity,
bounded-overlap packet lemma, and exponent ledger are replayed in

```text
src/qp_fejer_s_restriction_gate.py
src/test_qp_fejer_s_restriction_gate.py
```
