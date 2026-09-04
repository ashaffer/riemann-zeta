# QP selected-degree BDH: Mellin sampling and sparse mean-value gate

**Date:** 2026-08-24  
**Verdict:** a centered Mellin/Perron reduction is exact, but the ordinary
sampling large sieve and the available Heath--Brown sparse mean-value
theorem both miss the selected-degree BDH scale by polynomial factors.
At the balanced support, the optimistic ordinary route loses `D^(17/16)`
in squared norm.  Even after granting complete removal of its coherent
first term, the direct Heath--Brown route loses `D^(5/4)`.

The improved Matomaki--Teravainen mean-value lemma does not remove the
loss: at these lengths its correlation term is exactly the weighted
determinant band `|ac-a'c'|<=D`.  Thus it exposes one of the existing gates
rather than proving a new estimate.

No selected-degree BDH theorem, actual-prime counterexample, or sharp
four-cycle theorem is proved here.

## 1. Center arbitrary coefficients before every inequality

Let `S` be the full prime-power project shell, let `A subset S`, and allow
arbitrary coefficients `z=(z_c)_(c in A)`.  Use a smooth product-window
matrix

```text
T^W_(b,c)=sum_(a in S) W((8abc/q^3-1)/eta),
eta=D/q^2,                                                (1.1)
```

where `W` is fixed and supported on a bounded interval.  The sharp
selected-degree statement is

```text
||P_b T^W z||_2^2 <<D q^o(1)||z||_2^2,                  (1.2)
P_b=I-|S|^(-1)J.                                         (1.3)
```

For flat `z=1_A`, (1.2) is the centered form of

```text
sum_b d_b^2 <<M D+(D^2/q)M^2 q^o(1),    M=|A|.          (1.4)
```

Dualizing only after (1.3),

```text
||P_b T^W z||_2
 =sup_(||beta||_2=1, sum beta_b=0)
   |sum_(a,b,c) beta_b z_c W((8abc/q^3-1)/eta)|.         (1.5)
```

Thus every ledger below retains the arbitrary mask and the exact strongest
rank-one centering.  Dyadic coefficient-height decomposition reduces to
`|z_c|~||z||_2/sqrt(M)` and
`|beta_b|~1/sqrt(R)` on supports of sizes `M,R`, at a `q^o(1)` cost.

## 2. Exact Mellin formula and the under-Nyquist scale

Let

```text
P(t)=sum_(a in S) a^(-it),
Z(t)=sum_(c in A) z_c c^(-it),
B_beta(t)=sum_(b in S) beta_b b^(-it).                   (2.1)
```

Mellin inversion in (1.5) gives, up to an irrelevant unit phase,

```text
L(beta,z)
 =1/(2pi) integral_R W_eta_hat(t)
             P(t) Z(t) B_beta(t) dt,                    (2.2)

W_eta_hat(t)<<_j eta(1+eta|t|)^(-j).                    (2.3)
```

The native bandwidth is therefore

```text
T=eta^(-1)=q^2/D.                                       (2.4)
```

At `q=D^(33/16+o(1))`,

```text
T=D^(25/8+o(1)),       T/q=q/D=D^(17/16+o(1)).           (2.5)
```

There are only `q^(1+o(1))` carrier samples.  Hence (2.2) is severely
under-Nyquist: its Mellin bandwidth exceeds the reciprocal log-spacing of
the sample points by the factor in (2.5).

## 3. Exact ordinary sampling deficit

Distinct shell integers have

```text
|log b-log b'|>>1/q.                                    (3.1)
```

The standard continuous large sieve for separated samples consequently
has constant

```text
T+q~T.                                                   (3.2)
```

Apply it to the first two factors in (2.2).  Even on the optimistic ledger
where their weighted Mellin energy contains only its diagonal,

```text
integral |W_eta_hat(t)|^2 |P(t)Z(t)|^2 dt
  ~eta |S| ||z||_2^2
  =D/q *q^o(1)||z||_2^2.                                (3.3)
```

Multiplication by the sampling constant (3.2) yields

```text
||P_b T^W z||_2^2
 <<q q^o(1)||z||_2^2,                                   (3.4)
```

instead of `D||z||_2^2`.  The exact squared-norm deficit is

```text
q/D=D^(17/16+o(1)).                                     (3.5)
```

Centering the output as in (1.3) deletes one sample-space direction.  It
does not change the separation constant `T+q` and therefore does not alter
(3.5).  A proof by this route requires a product-sensitive sampling theorem
which replaces `T` by `q` after centering.

## 4. What the improved sparse mean lemma actually produces

Put

```text
gamma_n=sum_(ac=n) z_c,
C(t)=P(t)Z(t)=sum_(n~q^2) gamma_n n^(-it).               (4.1)
```

The narrow prime-power shell has one node per prime base, so

```text
|gamma_n|<=2 max_c|z_c|.                                 (4.2)
```

Lemma 3.3 of Matomaki--Teravainen states that for a polynomial of length
`N`,

```text
integral_(-T)^T |C(t)|^2 dt
 <<T sum_n|gamma_n|^2
   +T sum_(0<|h|<=N/T) sum_n|gamma_n gamma_(n+h)|.       (4.3)
```

Their result is an explicit sparse refinement of the usual mean-value
theorem; see [Almost primes in almost all short intervals II,
Lemma 3.3](https://arxiv.org/abs/2207.05038).

Here

```text
N=q^2,              N/T=D.                              (4.4)
```

Consequently, after expanding the absolute values, the second term in
(4.3) is bounded by

```text
sum_(0<|h|<=D)
 sum_(ac-a'c'=h) |z_c z_(c')|,                          (4.5)
```

the weighted determinant-band correlation.  For nonnegative data with
unique ordered product representations this expansion is an equality; for
arbitrary complex data it is the natural absolute majorant.  This is not an error term
known to have the required arbitrary-mask size.  Flat actual-prime data
also have a genuine positive volume contribution in this band.  Thus the
improved theorem routes the calculation back to the previously isolated
determinant-energy gate.

Even if (4.5) is discarded for an impossibly favorable audit, the sampling
loss (3.5) remains.  The two problems are logically independent:

```text
pair-product near collisions,          and
under-Nyquist selection at b in S.                          (4.6)
```

## 5. Direct Heath--Brown sparse theorem: exact scale translation

The sparse mean-value estimate used as Lemma 3.4 in the same
Matomaki--Teravainen paper comes from Heath--Brown's large-values theorem.
In its relevant notation, if a sparse polynomial has `R` terms at length
`q`, the other polynomial has length `N=q^2`, and the integration length is
`T`, then on the `1`-line it gives

```text
integral |M(1+it)|^2 |C(1+it)|^2 dt
 <<(R/q)^2
   +(q^2 T)^epsilon [R T/q^4
                     +R^(7/4)T^(3/4)/q^4]
```

times the maximum squared coefficient of `C`.  Since

```text
N=q^2>=T^(2/3),                                          (5.1)
```

the theorem deletes the last `R^(7/4)` term.  This is precisely the
favorable branch of the cited result.  The original source is
[Heath--Brown's large-values paper](https://doi.org/10.1112/jlms/s2-20.1.8).

Take a dual coefficient block of `R` entries of size `R^(-1/2)`.  Moving
the sparse length-`q` factor and the length-`q^2` factor from the `1`-line
to the `0`-line multiplies the integral by `q^6`; the beta normalization
divides it by `R`.  The theorem therefore gives the exact scale ledger

```text
integral_(-T)^T |B_beta(t)C(t)|^2 dt
 <<q^o(1)[R q^4+T q^2] max_n|gamma_n|^2.                (5.2)
```

Mellin Cauchy in (2.2) costs the window factor `eta=1/T`, so (5.2) becomes

```text
|L(beta,z)|^2
 <<q^o(1)[R q^2 D+q^2] max_n|gamma_n|^2.                (5.3)
```

The first term is the coherent/density term.  The condition
`sum beta_b=0` is not part of the sparse theorem, so it does not
automatically disappear.  Grant its complete removal anyway.  For flat
unnormalized `z=1_A`, (4.2) then leaves

```text
|L(beta,1_A)|^2<<q^2 q^o(1).                            (5.4)
```

BDH requires `M D`.  Hence this direct theorem closes the target only if

```text
M>=q^2/D=T.                                              (5.5)
```

At the balanced broad face,

```text
M=D^(15/8),             T=D^(25/8),                     (5.6)
```

and the surviving deficit is

```text
q^2/(M D)=T/M=D^(5/4).                                  (5.7)
```

For normalized flat data `z_c=M^(-1/2)`, both (5.4) and the desired bound
divide by `M`, so the same ratio (5.7) remains.  The nonpolar term in (5.2)
is independent of `R`; even a centered two-spike dual vector does not
change this ledger.

Thus centering might repair the theorem's first term, but it cannot repair
the second.

## 6. Why this is an obstruction rather than a counterexample

The estimates above audit existing **positive mean-value architectures**.
They do not lower-bound the actual centered operator.  In particular,
failure of Cauchy plus a mean-value theorem to see cancellation in the
linear Perron integral is not a faithful product-window counterexample.

Nor does the audit rule out every possible use of sparse large-values
technology.  A new argument could decompose the `t`-set by simultaneous
large values and retain the sign of the Perron integral.  What the ledger
proves is that neither

```text
ordinary separated-sample large sieve,
Matomaki--Teravainen Lemma 3.3 followed by positive correlation bounds,
nor the direct favorable branch of Heath--Brown sparse Lemma 3.4          (6.1)
```

has the required exponents for arbitrary `A,z,beta`, even after centering
is imposed before the inequalities.

## 7. The exact missing sampling theorem

Let `R_eta` denote the Mellin synthesis in (2.2), restricted to the actual
carrier points.  The desired new input is a joint statement of the form

```text
||P_b R_eta(P*Z)||_(ell^2(S_b))^2
 <<D q^o(1)||z||_2^2,                                   (7.1)
```

which must simultaneously:

1. beat the generic sampling constant by `T/q=q/D`;
2. exploit the product convolution `gamma=1_S *_times z`;
3. control rather than discard the shifts `|ac-a'c'|<=D`;
4. retain the actual centered product window.

Equation (7.1) is the mask-sensitive two-inverse/selected-degree BDH
theorem in Mellin language.  Existing sparse mean values do not imply it;
they identify exactly why it is new.

## 8. Balanced exponent ledger

With exponents measured relative to `D`,

```text
q:                                      33/16;
T=q^2/D:                                25/8;
M:                                      15/8;
desired squared norm M D:               23/8;
ordinary optimistic squared norm q M:   63/16;
ordinary deficit:                        17/16;
HB nonpolar squared norm q^2:            33/8;
HB nonpolar deficit:                     5/4.
```

```text
centered Mellin/Perron formula:                     EXACT;
ordinary sampling route at BDH scale:               FAILS BY D^(17/16);
improved sparse mean shift range:                    EXACTLY D;
its shift correlation:                              DETERMINANT-BAND GATE;
HB third sparse term in this range:                 DELETED;
HB coherent first term after centering:             NOT AUTOMATICALLY DELETED;
HB nonpolar term even after fantasy deletion:       FAILS BY D^(5/4);
selected-degree BDH from these theorems:             NOT PROVED;
faithful actual-prime counterexample:                NOT FOUND;
sharp four-cycle theorem:                            NOT PROVED.
```

The executable rational-exponent ledger is in
`src/qp_selected_degree_mellin_bdh_gate.py`, with regressions in
`src/test_qp_selected_degree_mellin_bdh_gate.py`.
