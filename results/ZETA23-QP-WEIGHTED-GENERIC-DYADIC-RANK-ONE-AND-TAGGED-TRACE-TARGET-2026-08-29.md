# QP weighted generic dyadic target after the coherent peel

**Date:** 2026-08-29

## Verdict

The unweighted anchored partner bound `GACCT` is stronger than the original
rank-one problem requires.  That bound becomes natural only after the
rowwise Cauchy inequality has replaced every partner coefficient by an
anchor-diagonal degree.  If the original quartic weights are retained, the
correct positive dyadic target is a global rank-one weighted form.  Its
weighted zero-tag factorial formulation is equivalent, up to absolute
constants.  A full pair-space spectral theorem or a maximum unweighted
anchored trace is strictly stronger.

## 1. Exact rank-one expansion

Let `Gamma` be the ordered physical color-pair set and let `B` be the
binary residual row-pair/color-pair incidence.  Thus

```text
m(gamma,eta)=(B^*B)_(gamma,eta)
```

is the number of their common physical completions.  For
`gamma=(c,C)` put

```text
xi_gamma=conj(z_c)*z_C,       u_gamma=|xi_gamma|=|z_c*z_C|.
```

Then, exactly,

```text
||B xi||_2^2
 =sum_(gamma,eta) m(gamma,eta) xi_gamma conj(xi_eta),       (1.1)
sum_gamma u_gamma^2=||z||_2^4.                            (1.2)
```

Let `G_R` be any fixed, coefficient-independent symmetric collection of
the still-open generic off-diagonal pairs after the tangent and coherent
positive contributions have been assigned, with

```text
R<=m(gamma,eta)<2R.
```

Restrictions to all-distinct colors, determinant bands, or already-open
anchor ranges are included in `G_R`; since all expressions below are
nonnegative, further deletion is legal.  The exact signed contribution and
its positive majorant are

```text
E_R^gen(z)=sum_((gamma,eta) in G_R)
              m(gamma,eta) xi_gamma conj(xi_eta),          (1.3)

|E_R^gen(z)|
 <=sum_((gamma,eta) in G_R)m(gamma,eta)u_gamma u_eta
 <2R sum_((gamma,eta) in G_R)u_gamma u_eta.                (1.4)
```

Consequently the minimally robust positive theorem is the following.

> **Weighted generic dyadic rank-one tail (`WGDT_R`).**  For every
> `epsilon>0` there is `C_epsilon` such that, uniformly in every admissible
> `q,D`, every dyadic open level `R`, and every complex coefficient vector
> `z` on the actual prime-power shell,
>
> ```text
> sum_((gamma,eta) in G_R)|z_c z_C z_d z_E|
>  <=C_epsilon*(D/R)*q^epsilon*||z||_2^4,           (WGDT_R)
> ```
>
> where `gamma=(c,C)` and `eta=(d,E)`.

Equation (1.4) makes each dyadic generic energy `O(Dq^epsilon)||z||_2^4`.
The `O(log q)` dyadic levels are absorbed in `q^epsilon`; together with the
already proved diagonal/tangent/coherent positive bounds, this proves the
sharp fourth-trace estimate.  One may restrict `(WGDT_R)` to the genuinely
remaining anchored range

```text
H_gamma>>D^(1/4),
q^o(1)<<R<<min(sqrt(D),H_gamma^2/sqrt(D)),
```

after assigning the complementary ordered contributions to the existing
proofs.  The clean all-generic formulation above avoids making that
assignment part of the theorem.

The formally weakest dyadic statement is just

```text
|E_R^gen(z)|<=C_epsilon*D*q^epsilon*||z||_2^4.      (1.5)
```

It permits rank-one phase cancellation.  `(WGDT_R)` is the smallest
positive statement that composes directly with the existing positive
coherent peel.

## 2. Why unweighted `GACCT` overcontrols

Put `A_R(gamma,eta)=1_((gamma,eta) in G_R)`.  The old target is

```text
max_gamma sum_eta A_R(gamma,eta)<<D/R*q^o(1).       (2.1)
```

By Schur and (1.2), (2.1) implies `(WGDT_R)`.  The converse fails even at
the level of abstract rank-one weights.  Take one central pair whose two
colors are disjoint from the colors of `P` leaf pairs, and make `A_R` the
symmetric star.  If `||z||_2=1`, put `s` for the squared `z`-mass on the
two central colors.  Then

```text
u_center<=s/2,
sum_leaves u_leaf<=(1-s)/2,
sum_(gamma,eta) A_R(gamma,eta)u_gamma u_eta
 <=s(1-s)/2<=1/8.                                  (2.2)
```

The rank-one weighted form is bounded independently of `P`, whereas the
maximum row sum is `P` and the full pair-space spectral norm is `sqrt(P)`.
This is a logical separation, not an asserted actual-prime counterexample.
It explains why harmless stars may defeat an unweighted theorem while
contributing little to the original quartic.

There is no contradiction with the earlier equivalence `WNDS~NDS`.
`WNDS` is the diagonal form produced *after* rowwise Cauchy,

```text
sum_gamma W(gamma)u_gamma^2.
```

It can detect one large `W(gamma)` by concentrating on the two anchor
colors.  The exact off-diagonal form (1.3) also requires weight on the
partner colors; rowwise Cauchy erased precisely that distinction.

## 3. Equivalent weighted factorial/tagged-trace form

For `R>=2`, define

```text
WF_(2,R)(z)
 =sum_((gamma,eta) in G_R)
    binom(m(gamma,eta),2)u_gamma u_eta.             (3.1)
```

On the dyadic support,

```text
(R^2/4) sum_G u_gamma u_eta
 <=WF_(2,R)(z)
 <2R^2 sum_G u_gamma u_eta.                         (3.2)
```

Hence `(WGDT_R)` is quantitatively equivalent to

```text
WF_(2,R)(z)<<D*R*q^o(1)||z||_2^4.                  (WAF_2,R)
```

There is an exact zero-tag realization.  Let `S_(gamma,eta)` be the common
completion set.  For fixed `gamma`, tag by `eta` and give each
`alpha in S_(gamma,eta)` the amplitude

```text
F_(gamma,R,z)(eta,alpha)=sqrt(u_gamma*u_eta)
```

on `G_R`, and zero elsewhere.  Its off-diagonal same-tag trace satisfies

```text
sum_gamma sum_eta sum_(alpha!=beta in S_(gamma,eta))
 |F_(gamma,R,z)(eta,alpha)F_(gamma,R,z)(eta,beta)|
 =sum_G m(gamma,eta)(m(gamma,eta)-1)u_gamma u_eta
 =2WF_(2,R)(z).                                     (3.3)
```

With an injective product-state encoding of completions, (3.3) is exactly
the `E!=0` mass of the usual zero-tag trace.  Otherwise (3.3), with the
off-diagonal completion labels retained, is the definition that avoids a
hidden injectivity assumption.

Thus a **globally weighted** tagged-trace theorem with right side
`D R q^o(1)||z||_2^4` is not stronger than `(WGDT_R)`; it is an equivalent
proof interface.  By contrast, the old unweighted anchored assertion

```text
max_gamma sum_eta binom(m(gamma,eta),2)<<D*R*q^o(1)
```

is a Schur majorant and is strictly stronger.

## 4. Correct hierarchy and next node

For the generic dyadic adjacency one has

```text
maximum anchored row (`GACCT`)
    => full ell^2 pair-space spectral bound
    => positive rank-one weighted tail (`WGDT_R`)
    => exact signed rank-one dyadic bound (1.5).            (4.1)
```

The first two implications can be strict by (2.2).  The complete-positive
`S_1->S_2` channel norm is losslessly equivalent to the *unsplit full*
rank-one theorem, but a generic pairwise dyadic restriction need not remain
completely positive.  It therefore does not make a pair-space spectral
bound necessary.

The corrected project node is `(WGDT_R)`, preferably attacked through its
equivalent weighted tagged-trace/factorial form `(3.3)`.  An unweighted
partner count, an unweighted per-anchor trace, or an arbitrary-coefficient
pair-space spectral theorem should be treated as optional stronger routes,
not as the theorem the sharp four-cycle bound logically requires.
