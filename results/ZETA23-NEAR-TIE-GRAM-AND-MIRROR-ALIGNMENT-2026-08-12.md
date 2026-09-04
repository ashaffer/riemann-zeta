# Near-tie packet rows have a Hermite limit, but no carrier-scale transverse reservoir

Status: exact normalized two-row Gram formula, exact collision/Hermite limit,
four-row confluent conditioning theorem, and an exact leading mirror-alignment
no-go for separated fixed-width packets, 2026-08-12.  The last theorem applies
to the normalized two-packet Paley--Wiener/Gabor carrier class with every
collateral positive row imposed.  It does not control the actual von Mangoldt
operator or the target-only quotient, and it proves no zero-free strip.

Subsequent correction: the target-only extension is false.  A normalized
reciprocal-separation phase-flip configuration is proved in
[`ZETA23-TARGET-ONLY-PHASE-FLIP-GATE-2026-08-12.md`](ZETA23-TARGET-ONLY-PHASE-FLIP-GATE-2026-08-12.md).

## 1. Verdict

There are two corrections and one useful new theorem.

First, the previously suggested formula

```text
det G=1-|rho(Delta gamma+i Delta alpha)|^2             (1.1)
```

is not correct for normalized Fourier--Laplace rows of unequal depth.  The
mean depth is real data.  On a centered packet of width `w`, put

```text
M(s)=integral_(-w/2)^(w/2) exp(s t)dt
    =w*sinh(w*s/2)/(w*s/2).                            (1.2)
```

For the normalized row

```text
e_(alpha,gamma)(t)
 =exp((alpha-i*gamma)t)/sqrt(M(2*alpha)),              (1.3)
```

the exact answer is

```text
det G
 =1-|M(2*alpha_bar+i*Delta gamma)|^2
       /[M(2*alpha_bar-Delta alpha)
          M(2*alpha_bar+Delta alpha)].                 (1.4)
```

Second, (1.4) is perfectly collision-stable.  If both parameter differences
tend to zero symmetrically about `(alpha_bar,gamma_bar)`, then

```text
det G
 =Var_(2*alpha_bar)(t)
    *(Delta alpha^2+Delta gamma^2)
  +O((Delta alpha^2+Delta gamma^2)^2).                 (1.5)
```

The phase-aligned divided-difference row converges to the centered Hermite
row

```text
[(Delta alpha-i*Delta gamma)/|Delta|]
 *(t-mu_(2*alpha_bar))*e_(alpha_bar,gamma_bar)
 /sqrt(Var_(2*alpha_bar)(t)).                          (1.6)
```

Thus a two-pair joint restriction map loses one factor `|Delta|`, not a
fixed carrier power.  For the test gap `|Delta|=L^(-2)`, its inverse cost is
only polynomial in `L`.

Third, that benign confluent conditioning does **not** realize the malicious
abstract reservoir from the collateral audit.  A genuine reflected pair on
two fixed-width packets separated by `D=dL` has carrier-scale operator

```text
K_j,cross=U_j*V_j^*+V_j*U_j^*,                       (1.7)
```

up to relative `O(exp(-alpha_j*D))`.  If its positive row is imposed, then

```text
U_j(ell)+V_j(r)=0.                                   (1.8)
```

Consequently, for any number of pairs and any mutual angles,

```text
Re <ell,K_cross*r>
 =-sum_j |V_j(r)|^2.                                 (1.9)
```

Every summand has the same sign.  Rotating a near-tie row into a confluent
derivative direction rotates its positive and negative branches together;
it cannot make a carrier-sized transverse affine correction.  Equivalently,
the cross row lies in the span of the rows already constrained by (1.8), so
every homogeneous joint-kernel direction is orthogonal to it.

The binary conclusion, with its exact scope, is therefore:

> The abstract two-pair transverse block is **not realizable at carrier
> scale** in the normalized separated fixed-width two-packet PW/Gabor class
> after both positive rows are imposed.  Realizing its orientation requires
> promoting a same-lobe or reverse-branch term which is smaller by the fixed
> factor `exp(-alpha D)`, not merely paying the polynomial near-collision
> cost.

This removes that particular near-tie escape from the explicit packet
witness.  It does not remove collateral screening in the full proportional-
width Gabor space or in the target-only arithmetic quotient.

## 2. Exact normalized Gram determinant

Let `J=[-w/2,w/2]` and use the ordinary `L^2(J)` inner product.  Direct
integration gives

```text
<e_(alpha_0,gamma_0),e_(alpha_1,gamma_1)>
 =M(alpha_0+alpha_1+i*(gamma_1-gamma_0))
   /sqrt(M(2*alpha_0)M(2*alpha_1)).                   (2.1)
```

The diagonal entries of the normalized Gram matrix are one, so its
determinant is one minus the squared modulus of (2.1).  Writing

```text
alpha_0=alpha_bar-Delta alpha/2,
alpha_1=alpha_bar+Delta alpha/2                       (2.2)
```

proves (1.4).

The correction to (1.1) matters.  Two pairs with the same
`(Delta alpha,Delta gamma)` but different mean depths have different Gram
determinants.  This is forced by the change in the tilted packet measure;
it is not a Fourier-convention artifact.

The same formula holds for a smooth packet weight `W>=0` after replacing

```text
M(s) by M_W(s)=integral W(t)exp(s t)dt.               (2.3)
```

This is the version used for compactly supported interior packets.

## 3. Collision and the Hermite row

Put

```text
K(s)=log M(s),
mu_q=K'(q),
sigma_q^2=K''(q)>0,              q=2*alpha_bar.       (3.1)
```

The positivity in (3.1) is strict because it is the variance of `t` under
the probability density proportional to `exp(qt)` on a nondegenerate
interval.  Taking logarithms in (1.4) gives

```text
log |<e_0,e_1>|^2
 =2*Re K(q+i*Delta gamma)
  -K(q-Delta alpha)-K(q+Delta alpha).                (3.2)
```

Taylor expansion about `q` yields

```text
log |<e_0,e_1>|^2
 =-sigma_q^2*(Delta alpha^2+Delta gamma^2)
  +O(|Delta|^4),                                    (3.3)
```

and (1.5) follows by exponentiation.

For the projective limit, orthogonalize the second row against the first:

```text
h_Delta
 =[e_1-<e_0,e_1>e_0]/sqrt(det G).                    (3.4)
```

Differentiating the normalized row and deleting its scalar phase gives

```text
d e
 =(Delta alpha-i*Delta gamma)*(t-mu_q)e.             (3.5)
```

Its norm is `|Delta|*sigma_q`.  Equations (3.4)--(3.5) prove (1.6), up to
the immaterial convention-dependent unit phase.

For the uniform packet, the coefficient is explicit:

```text
sigma_q^2
 =1/q^2-(w^2/4)csch^2(qw/2),
sigma_0^2=w^2/12.                                   (3.6)
```

## 4. The four reflected branches are confluent, not singular

A reflected pair uses both exponential branches.  For two nearby pairs let

```text
A_j(t)=exp(( alpha_j-i*gamma_j)t),
B_j(t)=exp((-alpha_j-i*gamma_j)t).                   (4.1)
```

At a collision with `alpha>0`, the rescaled four-row family tends to

```text
A, B,
(delta_alpha-i*delta_gamma)*t*A,
(-delta_alpha-i*delta_gamma)*t*B.                    (4.2)
```

The four functions in (4.2) are linearly independent.  Indeed they are the
standard confluent exponential family

```text
exp(lambda_+ t), t exp(lambda_+ t),
exp(lambda_- t), t exp(lambda_- t),
lambda_+-lambda_-=2*alpha !=0.                       (4.3)
```

A finite exponential polynomial with the four coefficients in (4.3) which
vanishes on an interval vanishes identically, and the two distinct
exponential-polynomial blocks then have zero coefficients.

It follows by continuity of the confluent Gram matrix that, for a fixed
packet and parameters in a compact set with `alpha>=alpha_*>0`, the four-row
synthesis has two singular values bounded above and below by constants and
two singular values comparable with

```text
sqrt(delta_alpha^2+delta_gamma^2).                   (4.4)
```

Equivalently, arbitrary inconsistent data on the two pairs have minimum
interpolation cost `O(1/|Delta|)`, while collision-compatible data remain
bounded.  Separately normalizing the divided-difference rows and forgetting
the factor `|Delta|` would be the familiar false raw-singular-value move.

This theorem is useful but not enough to create the abstract reservoir.
The missing factor there is not (4.4); it is the fixed-power imbalance
between dominant cross-lobe and suppressed same-lobe branches.

## 5. Exact two-lobe block scale

Center two copies of `J` at `-D/2` and `D/2`.  Restrict `A_j,B_j` from
(4.1) to the left and right packets.  Since `M(2alpha)=M(-2alpha)`, their
norms are

```text
||A_-||=exp(-alpha*D/2)*sqrt(M(2alpha)),
||B_-||=exp( alpha*D/2)*sqrt(M(2alpha)),
||A_+||=exp( alpha*D/2)*sqrt(M(2alpha)),
||B_+||=exp(-alpha*D/2)*sqrt(M(2alpha)).              (5.1)
```

Up to the common positive explicit-form normalization, the pair operator is

```text
K=A*B^*+B*A^*.                                      (5.2)
```

Its dominant block between the two packets is

```text
B_-*A_+^*+A_+*B_-^*,
||B_-*A_+^*||=exp(alpha*D)M(2alpha).                 (5.3)
```

The reverse cross block has norm `exp(-alpha D)M(2alpha)`.  Every same-lobe
rank-one product has norm `M(2alpha)`, and hence

```text
||K_same||/||K_cross||=O(exp(-alpha D)),
||K_reverse||/||K_cross||=O(exp(-2alpha D)).         (5.4)
```

For `D=dL`, fixed `d,alpha>0`, this is a fixed power of the carrier.  A
polynomial loss from (4.4) cannot bridge it.

The positive/negative factorization of the leading block is

```text
X_j=(U_j+V_j)/sqrt(2),
Y_j=(U_j-V_j)/sqrt(2),
K_j,cross=X_j X_j^*-Y_j Y_j^*
          =U_j V_j^*+V_j U_j^*.                     (5.5)
```

Here `U_j` is the dominant left row and `V_j` the dominant right row.  The
directions can depend arbitrarily on `j`; in particular, near-tie divided
differences may rotate `U_j` into any legal confluent direction.

## 6. Mirror-alignment theorem

Let the free and seed coefficient spaces be `F` and `S`, let
`ell in F`, `r in S`, and let any finite family of carrier cross blocks be

```text
K_cross=sum_j c_j(U_j V_j^*+V_j U_j^*),
c_j>0.                                               (6.1)
```

Impose every corresponding positive row:

```text
U_j(ell)+V_j(r)=0.                                   (6.2)
```

Then direct substitution gives

```text
Re <ell,P_F K_cross r>
 =sum_j c_j Re[conj(U_j(ell))*V_j(r)]
 =-sum_j c_j |V_j(r)|^2.                             (6.3)
```

This proves (1.9).  No separation among the ordinates, no lower Gram bound,
and no independence of the `U_j` is used.  At an exact collision the terms
simply merge with their multiplicities.  If `h` lies in the homogeneous
joint kernel of the positive rows, then

```text
<h,P_F K_cross r>=0.                                 (6.4)
```

Thus a transverse confluent direction may make the affine positive-row
system expensive, but it cannot change its leading cross value.

The exact packet rows differ from (6.1)--(6.2) by the weak branches in
(5.4).  Let `E_weak` denote their **aggregate** contribution after all pair
weights, multiplicities, and coefficient conditioning have been included.
Assume the explicit aggregate estimate

```text
||E_weak||=o(kappa)                                  (6.5)
```

on the normalized states under consideration, together with a retained
seed carrier

```text
sum_j c_j|V_j(r)|^2 >=kappa*X^(-o(1))*||ell+r||^2.   (6.6)
```

Then (6.3) remains strictly negative at carrier scale.  A sufficient version
of (6.5) is that the maximum ratio in (5.4), multiplied by the total weighted
uncompressed pair-block scale and the relevant conditioning factor, is
`o(kappa)`.  Merely saying that the number of pairs is polynomial is not
enough: an unrestricted polynomial degree or total multiplicity can consume
the fixed-power saving.  Cancelling (6.3) by the weak block without (6.5)
is outside this theorem; under (6.5), doing so requires amplification beyond
the admitted normalized scale and forfeits the retained carrier.

## 7. Why the abstract reservoir violates the invariant

The collateral audit's second pair used, with `u,w in F` and `v in S`,

```text
x_1=a(u+v),
y_1=a(w-v).                                         (7.1)
```

Its free-free block is

```text
P_F[2(x_1x_1^*-y_1y_1^*)]P_F
 =2a^2(uu^*-ww^*).                                  (7.2)
```

The norm in (7.2) is the same order as its cross block.  But (5.4) says that
for every genuine separated fixed-width reflected pair, the free-free block
is smaller than the cross carrier by `O(exp(-alpha D))`.  Consequently
(7.1) cannot be the carrier-scale compression of such a pair.  Its
transverse negative direction was purchased by inserting exactly the
same-lobe carrier term forbidden by (5.4).

Finite Paley--Wiener interpolation does not evade this conclusion.  Section
4 says one can prescribe the four branch values at cost `O(1/|Delta|)`, but
prescribing the suppressed branch at the dominant-branch size costs the
additional factor `exp(alpha D)`.  Completing norms with common-kernel
vectors then scales the purported reservoir below the carrier by the same
fixed power.

## 8. Endpoint jets and finite Gabor transfer

For the continuous Paley--Wiener model, choose a smooth packet factor

```text
phi in C_c^infinity(J),
W=|phi|^2.                                           (8.1)
```

Every packet vector and its Hermite derivative is supported strictly inside
the global physical endpoints, so every endpoint jet vanishes exactly.
Equations (2.1)--(4.4) remain valid with `M_W` from (2.3).

For the finite critical Gabor grid, use the common binomial endpoint-flat
cutoff and smooth Fourier truncation constructed in
[`ZETA23-ASYMMETRIC-PW-MIRROR-BLOCK-REALIZATION-AUDIT-2026-08-12.md`](ZETA23-ASYMMETRIC-PW-MIRROR-BLOCK-REALIZATION-AUDIT-2026-08-12.md),
Section 5.  It approximates each of the finite family

```text
phi exp((+/-alpha-i gamma)t),
t phi exp((+/-alpha-i gamma)t)                       (8.2)
```

in every required weighted norm by `O_A(T^(-A))` for arbitrary fixed `A`,
while imposing all growing endpoint jets exactly.  Hence:

1. the collision/Hermite theorem transfers uniformly for polynomially small
   gaps, including `L^(-2)`;
2. in the exact collision topology, transfer (8.2) directly rather than
   subtracting two nearly equal floating rows; and
3. the fixed-power block gap (5.4) and mirror sign (6.3) are stable under the
   transfer.

No lower spacing between distinct zeta zeros is asserted.  If a gap is
smaller than every controlled approximation error, the correct object is
the confluent row itself, not a separately normalized raw difference.

## 9. Reproducible checks

The companion implementation is
[`near_tie_packet_gram.py`](../src/near_tie_packet_gram.py), with tests in
[`test_near_tie_packet_gram.py`](../src/test_near_tie_packet_gram.py).
It checks:

1. the closed moment and correlation formulas against Gauss quadrature;
2. the dependence on mean depth;
3. the variance coefficient in (1.5);
4. convergence of (3.4) to the Hermite row;
5. the two quadratic small eigenvalues of the four-branch Gram;
6. (6.3) for adversarial complex row orientations; and
7. the exponential same-lobe/cross-lobe scale in (5.4).

Run:

```text
PYTHONPATH=src python3 -m pytest -q src/test_near_tie_packet_gram.py
PYTHONPATH=src python3 src/near_tie_packet_gram.py
```

The tests are floating verification of exact elementary formulas, not
interval certificates or evidence about actual zero locations.

## 10. Exact scope and next gate

What is now proved:

| statement | status |
|---|---|
| exact normalized two-row determinant | proved, with mean-depth correction |
| collision-stable Hermite/divided-difference limit | proved |
| four reflected branches cost only `O(1/|Delta|)` | proved on a fixed packet |
| abstract block (7.1) realized at separated-packet carrier scale | **excluded** |
| exclusion survives growing endpoint jets | proved for the finite packet family |

What is not proved:

1. The full proportional-width lobe space need not satisfy the fixed-width
   gap (5.4); a same-lobe separation can itself be proportional to `L`.
2. The direct arithmetic carrier slice imposes only the selected positive
   row.  Formula (6.3) uses every collateral positive row whose pair is in
   (6.1).
3. The actual prime/pole/gamma operator is not a positive sum of the
   cross-pair blocks in (6.1).
4. Localization tails, shallow rows, and the passage from a packet witness
   to a uniform all-height theorem remain separate estimates.

The next divisor-side target is therefore narrower than the earlier
``normalized reservoir realization'' question:

> Extend the mirror-alignment estimate from the separated packet subspace to
> the precise carrier-retaining states used by the direct `q_eta` theorem,
> or exhibit a legal proportional-width state for which the same-lobe block
> reaches carrier scale after only the selected positive row is imposed.

The first alternative would materially strengthen target isolation.  The
second would identify the genuine, normalized near-tie escape.  Neither is
settled here, and no numerical zeta bound is changed.
