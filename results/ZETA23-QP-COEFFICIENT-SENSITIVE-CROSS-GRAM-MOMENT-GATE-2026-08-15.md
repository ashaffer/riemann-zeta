# QP coefficient-sensitive cross-Gram gate: the one surviving moment term

**Date:** 2026-08-15  
**Verdict:** the actual-prime QP is **not closed**.  A genuine
coefficient-sensitive large-value theorem does improve the KMT entrywise
ledger, but it leaves one critical directional difference-correlation term.
Its maximally repeated AP model is now excluded under stable normalization;
the general adaptive term is not.  Every other fixed-power exponent already
clears the `c=.019` target.

The precise survivor is not a general higher moment.  It is a directional
correlation between

```text
the autocorrelation of the adaptively selected bad-packet coefficients
```

and

```text
the translated negative large values of the actual prime twist.          (0.1)
```

Heath--Brown's difference-set theorem gives, for any adaptive packet family,
the normalized square-sum bound

```text
sum_(i,j)|Phi(t+t_i-t_j)|^2
 <<Y^o(1)[R^2/Y + R + R^(5/4)B^(1/2)/Y].             (0.2)
```

At

```text
R=Y^(2c),          c=.019,          B=Y^(50/33),     (0.3)
```

the three exponents in (0.2) are

```text
-.924,             +.038,           -.1949242424.... (0.4)
```

After taking the Frobenius square root, the first and third terms are much
smaller than `Y^(-.019)`.  The middle term is `Y^.019`, missing the target by
exactly `Y^.038`.  In Heath--Brown's displayed theorem it includes the
literal diagonal.  That diagonal cancels in the exact covariance.  A
separate Guth--Maynard dyadic argument below bounds the remaining
off-diagonal square mass by the largest nonzero difference-cell
multiplicity, up to `Y^o(1)`.

An AP can still reproduce the whole `R` term.  There is, however, one genuine
advance: a critical AP of negative packets is incompatible with both fixed
stable normalization of its uniform square and KMT decorrelation of its
first `asymp sqrt(R)` nonzero lags.  The Fejer proof is in Section 4.  This
removes the clean AP extremizer, but not approximate progressions, mixtures,
or the adaptive coefficient vector, so QP remains open.

---

## 1. Exact square residual

Let `mu_Y` be the normalized smooth positive von Mangoldt shell measure and

```text
Phi(v)=integral exp(ivu)dmu_Y(u).                     (1.1)
```

For a packet family `T={t_1,...,t_R}` and

```text
D_a(u)=sum_i a_i exp(-it_i u),                        (1.2)
```

the nonlinear part of the square reweighting covariance at a target `t` is

```text
C_t(a)=sum_(i,j)a_i conjugate(a_j)
 [Phi(t-t_i+t_j)-Phi(t)Phi(-t_i+t_j)].                (1.3)
```

The `i=j` terms in (1.3) cancel identically.  The desired fixed-slice
positive repair would follow from the candidate-specific estimate

```text
|C_t(a)|<=Y^(-c+o(1)) Z_a           for every t in H_Y, (1.4)
```

where `Z_a` is the exact positive normalization and `a` is the coefficient
vector produced by the low-difference linear repair.  It is enough here to
remember that the critical construction has

```text
||a||_2^2=Y^o(1).                                    (1.5)
```

A full operator bound for every `a` would be stronger than necessary.  The
directional estimate (1.4) is the minimal square-filter survivor.

---

## 2. Heath--Brown supplies the first adaptive square-sum theorem

Let

```text
S_Y(v)=sum_n Lambda(n)h(n/Y)n^(iv),
W_Y=S_Y(0) asymp Y,
Phi(v)=Y^(-iv)S_Y(v)/W_Y.                             (2.1)
```

Logarithmic factors from `Lambda` and the fixed smooth cutoff are `Y^o(1)`.
The difference-set theorem of Heath--Brown, in the form reproduced as
Theorem 1.6 of
[Guth--Maynard](https://arxiv.org/html/2405.20552v2#S1.Thmtheorem6), says
that for every one-separated `T` in an interval of length `B` and every
coefficient sequence bounded by `B^o(1)`,

```text
sum_(i,j)|sum_(n asyp Y)b_n n^(i(t_i-t_j))|^2
 <<B^o(1)[R^2Y+RY^2+R^(5/4)B^(1/2)Y].                (2.2)
```

Multiplying `b_n` by `n^(it)` preserves its modulus.  Thus (2.2) applies
with every adaptive shift `t` and gives exactly (0.2) after division by
`W_Y^2`.

This is materially stronger than applying KMT to `R^2` entries.  It retains
the complete coefficient-sensitive difference geometry and is uniform in
the adaptively selected packet family.

### Fixed-slice exponent ledger

Write `A=50/33`.  Inserting `R=Y^(2c)` into (0.2) gives

```text
R^2/Y:                 exponent 4c-1,
R:                     exponent 2c,
R^(5/4)B^(1/2)/Y:      exponent (5/2)c+A/2-1.         (2.3)
```

For `c=.019`, these are (0.4).  Cauchy--Schwarz yields

```text
|sum_(i,j)a_i conjugate(a_j)Phi(t-t_i+t_j)|
 <=||a||_2^2 [sum_(i,j)|Phi(t-t_i+t_j)|^2]^(1/2).    (2.4)
```

The corresponding Frobenius exponents are

```text
-.462,                 +.019,            -.0974621212.... (2.5)
```

The required exponent is `-.019`.  Therefore the dispersive pair-count and
top-aperture terms already win by `.443` and `.078462...`, respectively.
Only the square root of `R` loses, by exactly

```text
.019-(-.019)=.038=2c.                                (2.6)
```

The second product in (1.3) is lower rank but still contains the same
adaptive difference autocorrelation; scalar KMT does not improve (2.6).
Thus (2.6), rather than the aperture, is the exact higher-moment obstruction.

### Literal diagonal versus nonzero multiplicity

For the shifted square sum, the literal `i=j` contribution is exactly

```text
R |Phi(t)|^2.                                        (2.7)
```

It is improved by scalar KMT and cancels identically when the two terms of
(1.3) are kept together.  One may not simply subtract `R` from the right
side of Heath--Brown's inequality: that right side is an upper bound, not a
termwise identity.

There is a rigorous replacement.  Divide nonzero differences into unit
cells and put

```text
mu(T)=max_(I not containing 0)
       #{(i,j): i!=j and t_i-t_j in I}.              (2.8)
```

Choose in each occupied cell a difference maximizing the shifted modulus;
color the cells into `O(1)` one-separated families.  Guth--Maynard Theorem
1.1, after normalization by `W_Y`, gives for the number of distinct selected
values of size at least `v`

```text
N(v)<=Y^o(1)[v^-2+C_Y v^-4],
C_Y=Y^-2/5+B Y^-8/5.                                (2.9)
```

If there are `K<=R^2` selected cells, dyadic summation gives

```text
sum_(distinct cells) sup_I |Phi(t-v)|^2
 <=Y^o(1)[1+sqrt(C_Y K)].                            (2.10)
```

Indeed `v^-2` contributes `O(1)` on each dyadic level, while the crossover
between `K v^2` and `C_Y v^-2` contributes `sqrt(C_YK)`.  At (0.3),

```text
log_Y(C_Y R^2)
 <=50/33-8/5+4c=-.00884848... .                     (2.11)
```

Consequently

```text
sum_(i!=j)|Phi(t-t_i+t_j)|^2 <=mu(T)Y^o(1).         (2.12)
```

The same estimate applies to high nonzero differences in the product term
of (1.3).  Formula (2.12) is the exact residual-multiplicity quantification:
an AP has `mu(T) asyp R` and recovers the old square-root loss.  It is not by
itself a closure theorem.  Even `mu(T)=1` gives only an `O(Y^o(1))` square
sum, whereas (1.4) needs a directional `Y^-c` bound.  Thus multiplicity is
one localized survivor, but signed candidate-specific cancellation remains
necessary even after multiplicity is small.

---

## 3. Why the `R` term is a real additive resonance

Take an arithmetic progression

```text
t_i=t_0+i d,              i=0,...,R-1.               (3.1)
```

For constant coefficients `a_i=a`, grouping (1.3) by the difference lag
gives the exact autocorrelation coefficient

```text
r_a(ell d)=(R-|ell|)|a|^2,       |ell|<R.            (3.2)
```

At critical square energy `R|a|^2=1`, every fixed lag has

```text
r_a(ell d)=1+O(|ell|/R).                             (3.3)
```

Consequently a single translated actual-prime value

```text
Phi(t+ell d)                                            (3.4)
```

survives in the nonlinear square with no `1/R` dilution.  This is exactly
what the middle term in (0.2) must allow.  In the most elementary resonance,
choose `t=d`; the `ell=-1` pairs make `t+ell d=0`, and `R-1` off-diagonal
pairs contribute the exact value `Phi(0)=1`.  Multiplicative binning avoids
that zero-frequency example, but it does not avoid the same mechanism at a
nonzero translated large value.

If scalar KMT only says `|Phi(v)|<=eta`, (3.3) leaves an error of size `eta`,
not `eta/R`.  At `eta=(log Y)^(-3/10)` this is still much larger than every
fixed power `Y^(-c)`.

This example does not assert that the actual negative bad packets form the
AP (3.1).  It proves the exact scope: the `R` term cannot be removed for an
arbitrary adaptive family.  A successful improvement must correlate the
additive multiplicities of the **actual negative-large-value family** with
the signs and depths of its translated prime twists.

---

## 4. A Fejer test rules out the exact stable critical AP

The Dirichlet-kernel test becomes decisive only when stable normalization is
retained.  The following statement is abstract and exact.

### Proposition 4.1 (stable critical AP versus decorrelated lags)

Let `mu` be any probability measure, `Phi(s)=integral exp(isu)dmu(u)`,
`L=delta^-2`, and

```text
t_j=t_0+jd,                 0<=j<L,
-2delta<=Re Phi(t_j)<=-delta.                        (4.1)
```

Put

```text
S(u)=sum_(j<L)exp(i t_j u),
Z=integral |1+delta conjugate(S(u))|^2 dmu(u).       (4.2)
```

For `M=floor(sqrt(L)/8)`, if `Z<=K` with fixed `K`, then, for all sufficiently
large `L`, necessarily

```text
max_(1<=k<M)|Phi(kd)|+1/M >=1/[pi^2(K+3)].           (4.3)
```

In particular, a KMT bound `|Phi(kd)|<=eta_Y=o(1)` on these nonzero lags is
incompatible with (4.1)--(4.2) for large `Y`.

#### Proof

Write `D_L(theta)=sum_(j<L)exp(ij theta)`.  From (4.1),

```text
integral |D_L(du)|dmu(u)>=|integral S dmu|>=sqrt(L). (4.4)
```

Expanding (4.2), and using
`-2sqrt(L)<=Re integral S dmu<=-sqrt(L)`, gives

```text
integral |D_L(du)|^2dmu(u)<=(K+3)L.                 (4.5)
```

Paley--Zygmund applied to `|D_L|` puts mass at least `1/[4(K+3)]` on
`|D_L(du)|>=sqrt(L)/2`.  The elementary Dirichlet-kernel bound places this
event in

```text
dist(du,2pi Z)<=2pi/sqrt(L).                         (4.6)
```

On (4.6), the normalized Fejer kernel
`F_M(theta)=|D_M(theta)|^2/M` is at least `4M/pi^2`.  Hence

```text
integral F_M(du)dmu(u)>=M/[pi^2(K+3)].               (4.7)
```

Its nonnegative Fourier expansion gives

```text
integral F_M(du)dmu(u)
 =1+2 Re sum_(1<=k<M)(1-k/M)Phi(kd)
 <=1+M max_(1<=k<M)|Phi(kd)|.                        (4.8)
```

Equations (4.7)--(4.8) prove (4.3).  QED

Without the upper normalization in (4.2), Cauchy stops at
`L delta<=integral |D_L(du)|`; both sides have scale `sqrt(L)`.  KMT alone
only gives `integral |D_L|^2<=L+eta_YL^2`, also insufficient.  Stable
normalization first restores the sharp `O(L)` second moment, and Fejer then
detects the forced phase concentration.

For cluster-merged packets, (4.3) applies whenever `d,2d,...,Md` all lie in
the KMT high-frequency range; a low-step chain belongs to the separate
low-difference cluster.  This excludes the exact critical AP as a stable
counterexample.  It does not promote a general high-energy set to an AP of
length `L`, and it does not cover nonuniform adaptive coefficients or a
positive mixture of several squares.

---

## 5. Existing additive-energy control saturates at the same scale

At depth

```text
delta=Y^(-d),                                        (5.1)
```

the Guth--Maynard count permits the critical cardinality

```text
R_delta=delta^(-2)=Y^(2d).                           (5.2)
```

On subapertures where the standard Heath--Brown energy corollary applies,
an AP of length `L` has energy `asymp L^3`, while the large-value energy
bound has the schematic two terms

```text
L^3 Y^(-1+2d) + L^2Y^(2d).                          (5.3)
```

At `L=Y^(2d)`, the second term has exponent

```text
4d+2d=6d,                                           (5.4)
```

exactly the exponent of `L^3`.  The first term is negligible for the present
small `d`.  Thus the known energy theorem allows a critical AP without any
power saving.  Weighted BSG can classify such a set after the fact, but it
does not make (3.4) small or preserve the candidate source equation; this is
the same mass/direction loss already isolated in the pair-energy audit.

The full aperture is slightly beyond the simplest `Y>B^(2/3)` energy
corollary.  This only strengthens the negative disposition: even in the
subrange where that corollary is strongest, it is exactly saturated at the
needed cardinality.  No full-band conclusion is being inferred from the
restricted corollary.

---

## 6. The minimal new inequality

Partition the negative natural-prime large values dyadically:

```text
T_delta={t in H_Y, one-separated:
          -2delta<=Re Phi(t)<=-delta}.               (6.1)
```

Let `a_delta` be the actual coefficient vector selected by the normalized
linear packet repair, including cluster merging, and let

```text
r_delta(v)=sum_(t_i-t_j in the unit packet at v)
              a_i conjugate(a_j).                    (6.2)
```

After the already-proved diagonal cancellation, the missing statement is
the directional translated-correlation bound

```text
sup_(t in H_Y)
 |sum_v r_delta(v)
   [Phi(t-v)-Phi(t)Phi(-v)]|
 <=Y^(-c+o(1)) Z_delta,                              (6.3)
```

summed over the dyadic depth classes, with `c>.0187463697...` on the fixed
slice.  It is enough to prove (6.3) for the candidate vectors; an operator
bound for arbitrary coefficients is unnecessary.

Heath--Brown's pair-count and aperture terms clear the fixed-power ledger.
After the diagonal split, (2.12) localizes the worst residual to nonzero
multiplicity, but its distinct-cell square mass is only `Y^o(1)`, not the
needed `Y^-2c`.  What remains is a fixed-power directional saving for the
actual candidate coefficients.  Proposition 4.1 supplies it only for the
uniform exact-AP extremizer.  Existing large-value count and energy estimates
do not promote a general adaptive family to that case.

This is more precise than asking for a vector-valued KMT theorem: it names
the term, its polarity, its multiplicity, and the exact power gap.

---

## 7. Disposition

```text
Heath--Brown shifted difference-square estimate:          APPLIES;
pair-count term at c=.019:                                CLEARS target;
top-aperture term at c=.019:                              CLEARS target;
repeated-difference R term:                               MISSES by Y^.038;
generic removal of R term:                               FALSE (AP resonance);
existing large-value energy excludes critical AP:         NO, SATURATED;
stable uniform critical AP plus KMT lags:                  EXCLUDED (Prop. 4.1);
promotion of general high multiplicity to Prop. 4.1:       NOT PROVED;
candidate-specific negative additive-correlation saving:  OPEN;
actual-prime square residual / cross-Gram inequality:      OPEN;
positive QP-KILL or signed Delsarte closure:               NOT PROVED;
zero-free strip:                                           NOT PROVED.
```

Executable exponent replay:

- `src/qp_cross_gram_moment_gate.py`;
- `src/test_qp_cross_gram_moment_gate.py`;
- `results/verify_zeta23_qp_cross_gram_moment_gate.py`.
