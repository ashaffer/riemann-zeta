# QP four-cycle: rank-one weighted necessity audit for generic GACCT

**Date:** 2026-08-29

**Verdict:** cardinal generic anchored Carleson `(GACCT_K)` is still
strictly stronger than the rank-one four-cycle target.  On one dyadic
completion layer, the already defined anchored factorial bounds `(AF_2)` and
`(AF_3)` are equivalent to cardinal GACCT up to absolute constants; they are
not weaker weighted formulations.  The weakest existing positive dyadic
target is `(HC_K)`, equivalently a **collective rank-one-weighted** factorial
or zero-tag tagged-trace bound.  A deterministic finite-field incidence
family makes GACCT fail by a polynomial factor while satisfying the exact
rank-one energy bound with room to spare.

The countermodel is abstract.  It preserves a binary incidence and the pure
pair-vector quantifier, but not the QP hard product windows or actual-prime
mask.  Its purpose is to settle logical necessity, not to disprove an
arithmetic GACCT theorem.

## 1. Exact rank-one energy and its positive dyadic endpoint

Let `T` be the residual row-pair/color-pair incidence and write

```text
m_(gamma,eta)=(T^*T)_(gamma,eta).
```

For `gamma=(c,C)` put

```text
xi_gamma=conj(z_c)*z_C,
u_gamma=|xi_gamma|=|z_c*z_C|.
```

The exact residual energy is

```text
E_res(z)=||T xi||_2^2
        =sum_(gamma,eta) m_(gamma,eta)
             xi_eta*conj(xi_gamma).                 (1.1)
```

Moreover

```text
sum_gamma u_gamma^2=||z||_2^4.                     (1.2)
```

For a dyadic integer `K`, let

```text
A_K(gamma,eta)
 =1_(gamma!=eta)*1_(K<=m_(gamma,eta)<2K),
W_K(z)=sum_(gamma,eta) A_K(gamma,eta)u_gamma*u_eta.
                                                            (1.3)
```

All generic, residual, and already peeled restrictions may be inserted in
`A_K`.  Absolute domination of `(1.1)` gives a layer contribution at most
`2K W_K(z)`.  The sharp positive dyadic target is therefore

```text
W_K(z) <<(D/K)q^o(1)||z||_2^4.                     (HC_K)
```

This is not merely a convenient sufficient scale.  For nonnegative `z` all
terms have the same sign.  The positive four-cycle theorem implies `(HC_K)`
by retaining one layer, while summing `(HC_K)` over `O(log q)` layers proves
the positive theorem.  Thus the family `(HC_K)` is equivalent to the
positive endpoint up to `q^o(1)`.

## 2. Weighted factorial and tagged-trace forms

Define the **collective weighted** factorial forms

```text
mathfrakF_(r,K)(z)
 =sum_(gamma,eta) A_K(gamma,eta)
      binom(m_(gamma,eta),r)u_gamma*u_eta.          (2.1)
```

For fixed `r` and `K>=r`, the dyadic restriction gives

```text
mathfrakF_(r,K)(z) asymp_r K^r W_K(z).             (2.2)
```

Consequently the following three statements are equivalent up to absolute
constants:

```text
HC_K,
mathfrakF_(2,K)(z) <<D*K*q^o(1)||z||_2^4,
mathfrakF_(3,K)(z) <<D*K^2*q^o(1)||z||_2^4.        (2.3)
```

There is an equally exact tagged-trace expression.  For a fixed anchor
`gamma`, let `S_(gamma,eta)` be its common-completion set and define on the
`K` layer

```text
F_(gamma,z)(eta,X)
 =sqrt(u_eta)*1_(X in S_(gamma,eta)).               (2.4)
```

Because its autocorrelation is nonnegative, summing the nonzero difference
slice gives

```text
||Tr_0(F_(gamma,z),F_(gamma,z))||_1
 =sum_eta u_eta*m_(gamma,eta)(m_(gamma,eta)-1).
                                                            (2.5)
```

Multiplying by `u_gamma` and summing the anchors yields

```text
sum_gamma u_gamma
  ||Tr_0(F_(gamma,z),F_(gamma,z))||_1
 =2*mathfrakF_(2,K)(z).                             (2.6)
```

Thus the collective rank-one-weighted tagged-trace estimate with right side
`D*K*q^o(1)||z||_2^4` is exactly `(HC_K)`.  If one wants a theorem among the
existing `AF/SRH/tagged-trace` interfaces, `(2.6)` is the weakest interface
which retains precisely the necessary weights.

## 3. Why anchored AF and SRH are stronger

The previously defined anchored factorial quantities are

```text
F_(r,K)(gamma)
 =sum_eta A_K(gamma,eta)binom(m_(gamma,eta),r),
P_gamma(K)=sum_eta A_K(gamma,eta).                 (3.1)
```

On one dyadic layer,

```text
F_(r,K)(gamma) asymp_r K^r P_gamma(K).             (3.2)
```

It follows immediately that, for `K>=3`,

```text
GACCT_K: max_gamma P_gamma(K) <<D/K*q^o(1),
AF_2:    max_gamma F_(2,K)(gamma) <<D*K*q^o(1),
AF_3:    max_gamma F_(3,K)(gamma) <<D*K^2*q^o(1)
```

are mutually equivalent up to constants and `q^o(1)`.  The unweighted
anchored indicator tagged trace is twice `F_(2,K)(gamma)`, so it is in the
same equivalence class.

Each of them implies `(HC_K)`: GACCT bounds the maximum row sum of the
nonnegative symmetric matrix `A_K`, Schur gives

```text
<u,A_K u><=(D/K)q^o(1)||u||_2^2,
```

and `(1.2)` finishes the implication.  The converse is false by Section 4.

The selected reciprocal-height theorem is stronger still as a formal
sufficient condition.  The proved height lemma gives

```text
F_(3,K)(gamma) <<D*R_(gamma,K).
```

Hence `(SRH_K)`, namely `R_(gamma,K)<<K^2q^o(1)`, implies `AF_3`, GACCT,
and HC.  Neither GACCT nor AF formally implies SRH.  For example, take
`D/K` partners with disjoint `K`-point completion sets and give every
participating row triple height one.  GACCT and AF hold at their target
scale, while

```text
R_(gamma,K) asymp (D/K)*K^3=D*K^2,
```

which exceeds the SRH target by `D`.  This is again an abstract ledger; it
shows that SRH is a useful arithmetic sufficient theorem, not a necessary
reformulation.

The implication hierarchy is therefore

```text
SRH_K => AF_3 <=> AF_2 <=> GACCT_K
                              => weighted HC_K,
```

and both displayed arrows can be strict.

## 4. Deterministic countermodel to necessity of GACCT

Let `s` be a prime, and set

```text
K=s^2,                 D=s^4.                      (4.1)
```

Take the rows to be the `D` points of `F_s^4`.  Take one column for every
affine hyperplane

```text
H_(a,t)={x in F_s^4:a dot x=t},
```

where `a` runs through the projective normal directions and `t in F_s`.
There are

```text
N=s*(s^3+s^2+s+1)=s^4+s^3+s^2+s                  (4.2)
```

columns.  Let `T_(x,H)=1_(x in H)`.  Every column has `s^3` rows.  Distinct
parallel hyperplanes are disjoint, whereas hyperplanes with distinct
normals meet in an affine two-plane of exactly `s^2=K` points.

Therefore every column has

```text
P_H(K)=N-s=s^4+s^3+s^2                            (4.3)
```

partners on the exact `K` layer.  GACCT permits only

```text
D/K=s^2,
```

so it fails by a factor asymptotic to `s^2=K`.

Now assign every hyperplane `H` a disjoint ordered pair of color labels
`(a_H,b_H)`, and let `T` vanish on all other color-pair columns.  Put

```text
v_H=conj(z_(a_H))*z_(b_H).
```

Disjointness and AM--GM give

```text
sum_H |v_H|
 <=(1/2)sum_H(|z_(a_H)|^2+|z_(b_H)|^2)
 <=(1/2)||z||_2^2.                                 (4.4)
```

For every row `x`,

```text
|sum_(H containing x)v_H|<=sum_H|v_H|.
```

Summing over the `D` rows proves the exact pure-pair estimate

```text
||T(conj(z) tensor z)||_2^2
 <=(D/4)||z||_2^4.                                 (4.5)
```

Likewise the positive weight on the exact `K` layer satisfies

```text
W_K(z)
 <=(sum_H|v_H|)^2
 <=(1/4)||z||_2^4,                                 (4.6)
```

which is much stronger than the required `(D/K)||z||_2^4=s^2||z||_2^4`.
Thus the exact rank-one residual target and HC hold uniformly, while GACCT,
AF2, AF3, and the unweighted anchored tagged trace all fail polynomially.

The construction can be assigned arbitrary generic color labels.  It has no
claim to satisfy the QP reciprocal windows, but it proves that neither the
word `generic` nor binary pair uniqueness creates a logical implication from
the rank-one target to a cardinal anchored tail.  Any arithmetic GACCT proof
would establish genuinely more than the sharp four-cycle estimate needs.

## 5. Correct next theorem and experiment

The main target should be the generic, post-coherent restriction of
`(HC_K)`, or equivalently the collective weighted tagged trace `(2.6)`, in
the remaining dyadic range.  It may also be stated in the Cartesian
restricted-type form already developed for the factorial kernel.  The
weights `u_(c,C)=|z_cz_C|` must remain attached throughout; replacing them by
an arbitrary pair vector or taking a maximum anchor returns to the stronger
GACCT/AF theorem.

This is the weakest correct endpoint, not automatically an easier
intermediate lemma: Section 1 shows that proving all of its dyadic instances
is equivalent to proving the positive four-cycle bound.  Merely renaming HC
as a weighted tagged trace therefore makes no progress unless the statement
is paired with a genuinely more structured sufficient mechanism.

The most promising proof mechanism remains weighted packet participation:
extract actual mergeable packets, prove the two-sided participation product
bound, and prove mask-stable unconditionality on the complement.  The new
coefficient-large null theorem is a possible local classifier inside that
program, but its pointwise line bound does not supply the collective weighted
sum.

Before another long theorem attack, run one focused falsifier on the actual
post-coherent dyadic kernels.  For every tested `K`, compare

```text
C_row(K)=max_gamma sum_eta A_K(gamma,eta),
C_op(K)=||A_K||_(2->2),
C_pure(K)=sup_(z>=0, ||z||_2=1)
          <z tensor z,A_K(z tensor z)>.             (5.1)
```

The decisive target ratio is `K*C_pure(K)/D`.  Multistart positive-quartic
optimization and Cartesian-cut searches give rigorous lower bounds, so any
polynomial target violation falsifies weighted HC immediately.  A growing
gap between `C_row` and `C_pure`, as in Section 4, would validate abandoning
GACCT but would not prove HC.  Small supports can additionally use exhaustive
or interval branch-and-bound certification.

Accordingly the immediate action should be this inexpensive rank-one-gap
experiment, followed--if it survives--by a theorem stated as weighted HC or
collective weighted tagged trace.  Do not invest further in cardinal GACCT,
anchored AF, or SRH as though they were necessary endpoints.

## 6. Replay

The exact finite-field incidence and the universal disjoint-pair energy
ledger are implemented in

```text
src/qp_rank_one_gacct_countermodel.py
src/test_qp_rank_one_gacct_countermodel.py.
```

The focused replay is

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_rank_one_gacct_countermodel.py
```
