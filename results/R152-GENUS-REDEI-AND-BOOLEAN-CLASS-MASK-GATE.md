# R152 genus, Redei, and Boolean class-mask gate

## Status

R151 leaves open the possibility that the head quotient

```text
C_H=Cl(F)/Gamma_H
```

is supplied cheaply by genus theory or by a large elementary `2`-quotient.
This report computes that possibility exactly.  The computation is useful,
but it does not produce a fixed zeta zero-free strip.

1. Ordinary genus characters are the solutions of an explicit binary linear
   system formed from one infinity-sign row, the split head-prime rows, and
   the relevant Redei rows.
2. Ramified-prime conditions can be made cheap.  Extra Redei nullity, or
   narrow `4`-rank, supplies additional genus characters, subject to at most
   one ordinary-sign constraint.
3. Every ordinary genus character detector is exactly the biquadratic R138
   quotient

   ```text
   zeta(s)L(s,chi_D)/[L(s,chi_delta1)L(s,chi_delta2)].
   ```

   Thus genus theory does not create a new analytic species.
4. For `H`-rough `D`, complete head deletion is avoidance of the single
   `(-- )` Frobenius class in a biquadratic field.  Its external density is
   `1/4`, independently of the Redei rank.
5. The general elementary-`2` complement interpolant has exact Fourier
   `l2` cost `sqrt(h/(N-h))` and absolute `l1` cost at most
   `sqrt((N-1)h/(N-h))`.  For an unstructured head this is the same strict
   square-root wall as R138--R140.
6. Under GRH, effective Chebotarev would find the missing biquadratic class
   by `O(log^2 D)`, contradicting the required sub-square-root conductor
   regime.  No unconditional theorem at that scale is known.

```text
ordinary genus-character parametrization                 EXACT
split-head and ramified Redei linear system               EXACT
ramification/Redei engineering                            CHEAP
genus detector equals R138 biquadratic detector           EXACT
external missing-class density                            1/4
elementary-2 complement Fourier ledger                    EXACT
generic complement fixed-strip closure                    CLOSED
exceptional least-V4-Frobenius sequence                   OPEN
fixed uniform zeta zero-free strip                        NOT PROVED
zeros approaching one                                     NOT PROVED
```

Date: 2026-08-08.

Predecessor:
[`R151-CLASS-CHARACTER-HEAD-QUOTIENT-GATE.md`](R151-CLASS-CHARACTER-HEAD-QUOTIENT-GATE.md).

## 1. Ordinary genus characters

Let

```text
D=product_(i=1)^t d_i>0
```

be an odd fundamental discriminant written as a product of prime
discriminants

```text
d_i=p_i^*=(-1)^((p_i-1)/2)p_i.
```

Put

```text
b_i=1_(d_i<0) in F_2.                                      (1.1)
```

A genus factorization is indexed by `x in F_2^t`.  The two complementary
factorizations define the same character, so

```text
x~x+1.                                                     (1.2)
```

The associated character is ordinary, rather than narrow with a nontrivial
infinity type, precisely when both factor discriminants are positive.  Since
`D>0`, this is the single condition

```text
b.x=0.                                                     (1.3)
```

Consequently the ordinary genus-character group is

```text
b^perp/<1>.                                                (1.4)
```

The classes `x=0,1` give the trivial character.  The ordinary genus rank is
therefore `t-1` when every `d_i>0`, and `t-2` otherwise.  The infinity row is
essential here: a negative-negative factorization defines a narrow character
ramified at infinity and does not retain R151's Gamma cancellation.

## 2. Exact split and ramified head equations

For `p` not dividing `D` and split in `F=Q(sqrt(D))`, define

```text
a_p=(1_(chi_(d_i)(p)=-1))_(i=1)^t in F_2^t.                (2.1)
```

The genus character indexed by `x` is trivial on a prime ideal above `p`
exactly when

```text
a_p.x=0.                                                   (2.2)
```

Define the Redei matrix `R` by

```text
(-1)^(R_(ji))=chi_(d_i)(p_j),             i!=j,
R_(jj)=sum_(i!=j)R_(ji).                                    (2.3)
```

At the ramified prime ideal `P_j` above `p_j`, the character value is

```text
eta_x(P_j)=(-1)^((Rx)_j).                                  (2.4)
```

Thus a ramified rational prime `p_j<=H` is completely deleted precisely when

```text
(Rx)_j=0.                                                   (2.5)
```

Let `M_H` be the binary matrix obtained by stacking

```text
b;
a_p for split p<=H;
the jth row of R for every p_j<=H.                          (2.6)
```

The exact head genus bank is

```text
B_H^(genus)=ker(M_H)/<1>,                                   (2.7)

dim B_H^(genus)=t-rank(M_H)-1.                              (2.8)
```

This is the genus-theory specialization of the abstract class quotient in
R151, with no hidden analytic condition.

## 3. What Redei nullity buys

If every ramified prime lies below `H`, the ramified constraints give

```text
(ker R intersect b^perp)/<1>.                              (3.1)
```

Classically,

```text
dim ker R-1=r_4(Cl^+(F)).                                  (3.2)
```

Hence maximal Redei rank kills all narrow genus survivors.  Extra narrow
`4`-rank supplies survivors, and the ordinary-sign row can remove at most one
dimension.

This is not the hard scale obstruction.  One may choose every discriminant
prime `p_i>H`, in which case no ramified row occurs at all while `log D` can
remain logarithmic in the chosen primes.  Redei singularity can likewise be
engineered through congruence conditions.  These choices do not control the
external split-prime rows (2.1), which are the dominant head constraints.

## 4. Genus characters are exactly the R138 pair detector

Let `x` be nontrivial and ordinary.  It determines a factorization

```text
D=delta_1 delta_2,
delta_1,delta_2>1,                                          (4.1)
```

into coprime positive fundamental discriminants.  Genus induction gives

```text
Ind_F^Q eta_x=chi_(delta_1)+chi_(delta_2),                  (4.2)

L_F(s,eta_x)=L(s,chi_(delta_1))L(s,chi_(delta_2)).          (4.3)
```

Therefore R151's quotient becomes

```text
F_(eta_x)(s)
 =zeta(s)L(s,chi_D)
   /[L(s,chi_(delta_1))L(s,chi_(delta_2))].                 (4.4)
```

Its virtual character is

```text
1+chi_D-chi_(delta_1)-chi_(delta_2)
 =(1-chi_(delta_1))(1-chi_(delta_2)).                       (4.5)
```

Equation (4.5) is exactly the R138 biquadratic detector.  In particular all
of R140's analytic gates apply verbatim: an abnormally cheap complete head
mask forces a near-one zero of at least one of

```text
L(s,chi_(delta_1)), L(s,chi_(delta_2)), L(s,chi_D).          (4.6)
```

## 5. The external missing-class problem

Assume `D` is `H`-rough.  At a prime `p<=H`, complete deletion of (4.5) fails
only when

```text
chi_(delta_1)(p)=chi_(delta_2)(p)=-1.                       (5.1)
```

Thus the head condition is exactly

```text
there is no p<=H in the (-- ) Frobenius class              (5.2)
```

of the biquadratic field `Q(sqrt(delta_1),sqrt(delta_2))`.
That class has Chebotarev density `1/4`.  Redei relations concern the
discriminant primes and do not change this external density.

Under GRH, effective Chebotarev gives

```text
P_(--)(delta_1,delta_2)<<log^2 D.                           (5.3)
```

Consequently `P_(--)>H` would force `log D>>sqrt(H)`, which is incompatible
with the high-jet requirement

```text
log D=o(H^kappa),                 kappa<1/2.                (5.4)
```

This conditional incompatibility is a reality check, not an unconditional
no-go theorem.  Available unconditional least-prime estimates are only
polynomial in the discriminant and do not imply (5.3).

## 6. General elementary-2 class masks

Let `E` be an elementary `2`-quotient of `Cl(F)`, with `N=|E|`.  Let

```text
phi:E->R_(>=0),             phi(1)=0,
phi=sum_(eta in E^) a_eta eta.                              (6.1)
```

Then

```text
A_phi(s)=sum_eta a_eta[-L_F'/L_F(s,eta)]                    (6.2)
```

has nonnegative rational prime-power coefficients.  More precisely:

```text
split p, odd v:      2 phi([P]);
inert p:             0;
ramified p, odd v:   phi([P]);
even v:              0.                                    (6.3)
```

Since `sum a_eta=phi(1)=0`, the signed degree, Gamma factors, and conductor
cancel.

Suppose the observed identity, split, and ramified head classes form a set
`H_E subset E` of size `h`.  The normalized complement interpolant is

```text
phi_H=N/(N-h) 1_(E\H_E).                                   (6.4)
```

Fourier orthogonality gives the exact ledgers

```text
a_1=1,
sum_(eta!=1)|a_eta|^2=h/(N-h),                              (6.5)

sum_(eta!=1)|a_eta|
 <=sqrt((N-1)h/(N-h)).                                     (6.6)
```

For an unstructured prime head, `h` is of order `H/log H` until saturation.
The absolute cost in (6.6) is therefore at least on the square-root scale
relevant to R138--R140, while Cauchy localization has exponent strictly below
`1/2`.  Enlarging the elementary quotient does not create a surplus.

Low-Fourier exceptions merely restate missing-class conditions.  A single
factor `1-eta` avoids one `V_4` class; a product of `m` such factors avoids the
all-minus Hamming vertex but pays Fourier cost `2^m`; the sparse `phi_star`
detector avoids Hamming weight at least two but leaves a fixed positive-density
bad set.  Redei rank changes the available dimension, not these external
densities.

## 7. Consequence for the fixed-strip program

Genus and Redei theory solve the ramified bookkeeping exactly and sometimes
cheaply.  They do not solve the external least-Frobenius problem.  The
surviving arithmetic alternative is now precise:

```text
construct an unconditional sequence of positive discriminants D and
ordinary genus characters with P_(--)>H and log D=o(H^kappa), kappa<1/2,
while retaining the required local auxiliary nonvanishing.              (7.1)
```

GRH predicts that (7.1) is impossible.  Present unconditional theorems prove
neither its existence nor its impossibility, so neither side of the zeta
fixed-strip dichotomy follows.

Primary genus references include Ibukiyama,
[*Genus character L-functions of quadratic orders*](https://arxiv.org/abs/2303.14983),
and Koymans--Pagano,
[*On Stevenhagen's conjecture*](https://arxiv.org/abs/2005.12899), for modern
Redei-rank formulations.

Successor:
[`R153-NONLINEAR-SUPPORT-AMPLIFIER-AND-MIXED-VALUE-GATE.md`](R153-NONLINEAR-SUPPORT-AMPLIFIER-AND-MIXED-VALUE-GATE.md).
