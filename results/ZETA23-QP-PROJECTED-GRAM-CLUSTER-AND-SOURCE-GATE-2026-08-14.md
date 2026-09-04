# QP projected Gram: cluster no-go and exact source gate

**Date:** 2026-08-14
**Verdict:** the actual-prime Delsarte value is still open, but the proposed
uniform projected-Gram route has a definitive obstruction.  A bad-packet
**count** cannot imply a polynomial lower bound for every projected packet
Gramian.  Consecutive unit packets have an explicit binomial near-null
direction whose eigenvalue is exponentially small in the cluster length,
for the actual prime nodes just as for every other node set in the shell.

The obstruction does not kill all adaptive correction.  The correction data
are not arbitrary.  After quotienting the carrier, their exact cost is one
directional source quantity

```text
z_T=m_T^T G_T^(-1)m_T
   =sup_c (mean_j F_c(u_j))^2
          /sum_j |F_c(u_j)-mean_l F_c(u_l)|^2.        (0.1)
```

Thus the surviving theorem is narrower than a condition-number theorem: it
must show that no linear combination of the actual bad-packet phases is
nearly constant on all shell prime powers while retaining nonzero mean.  No
checked large-values, large-sieve, restricted-invertibility, or sparsification
theorem has this carrier-specific quantifier.

In particular:

```text
uniform lower Gram bound inferred from Guth--Maynard count alone: FALSE;
uniform arbitrary-value polynomial-cost packet correction:     FALSE;
exact demand-specific source/Schur reduction:                   PROVED;
actual-prime bound for the source quantity z_T:                 OPEN;
off-packet propagation bound for the completed correction:      OPEN;
actual-prime Delsarte value A_H at fixed-power precision:        OPEN;
QP promotion or kill:                                           NOT PROVED.
```

---

## 1. Exact target and polarity

For distinct actual nodes

```text
u_j=|log(n_j/Y)| in (0,w],       w=1/5,
a(t)=(cos(tu_j))_(j<=M),         q=(1,...,1),
H=[Y^.01,Y^(50/33)],
```

let

```text
A_H=sup {Q(0):
 Q(t)=1+sum_j lambda_j cos(tu_j)>=0 for every t in H}. (1.1)
```

The already-proved compact moment duality gives

```text
p_*=1/A_H,                  r_+=1/(A_H-1),             (1.2)
```

where `p_*` is the maximal central atom in a legal spectral-null
probability and `r_+` is the deepest positive antipode.

On the fixed `d=33/50=.66` slice,

```text
kappa_min=.018030323424358778...,
kappa_max=.018746369714728765....                      (1.3)
```

Hence promotion at depth `Y^(-kappa_min+eta)` requires

```text
A_H<=1+Y^(kappa_min-eta),                              (1.4)
```

whereas a dual kill at error `Y^(-c)` requires

```text
A_H>=1+Y^c.                                           (1.5)
```

The choice `c=.019` beats `kappa_max` only on this fixed slice.  It is not
uniform over the cached varying-`d` family.

The continuum dual is

```text
r_+(H)=inf_(y:q^T y=-1) sup_(t in H)y^T a(t).          (1.6)
```

Starting from `y_0=-q/M`, the positive violations are the negative large
values of the normalized actual-prime cosine polynomial.  Covering those
violations by packet centres suggests a projected Gram correction.  The next
section proves that a lower bound for the complete Gram spectrum cannot be
the missing theorem.

---

## 2. Consecutive-packet Gram collapse

Let arbitrary nodes satisfy `|u_j|<=w`, let `P=I-qq^T/M`, and choose
consecutive centres

```text
t_k=t_0+k h,          0<=k<=m.
```

Put

```text
V=[P a(t_0),...,P a(t_m)],       G=V^T V.              (2.1)
```

### Theorem 2.1 (universal binomial cluster obstruction)

If `0<hw<=pi`, then

```text
lambda_min(G)
 <= M [2 sin(hw/2)]^(2m) / binom(2m,m).               (2.2)
```

Consequently, for fixed `hw<pi`,

```text
lambda_min(G)/M
 <=sqrt(pi m)(1+o(1))*sin(hw/2)^(2m).                 (2.3)
```

For the QP shell `w=1/5` and unit packet spacing `h=1`, the exponential
rate is

```text
-2 log(sin(1/10))=4.608504631138533... .              (2.4)
```

Thus a cluster of `R=m+1` packets obeys

```text
lambda_min(G)/M
 <=exp[-(4.6085046311...+o(1))R].                      (2.5)
```

#### Proof

Take

```text
c_k=(-1)^(m-k) binom(m,k).
```

At every node,

```text
sum_(k=0)^m c_k exp(i(t_0+kh)u_j)
 =exp(it_0u_j)[exp(ihu_j)-1]^m.                       (2.6)
```

The corresponding cosine sum is its real part, so its absolute value is at
most

```text
[2 sin(h|u_j|/2)]^m <=[2 sin(hw/2)]^m.                (2.7)
```

Projection cannot increase the Euclidean norm.  Therefore

```text
c^T G c=||Vc||_2^2<=M[2 sin(hw/2)]^(2m).              (2.8)
```

The Vandermonde identity

```text
||c||_2^2=sum_k binom(m,k)^2=binom(2m,m)              (2.9)
```

and the Rayleigh principle prove (2.2).  Stirling proves (2.3).  Substituting
`h=1,w=1/5` gives (2.4)--(2.5).  QED

### Corollary 2.2 (the count-only Gram hypothesis is false)

At threshold `epsilon=Y^(-.019)`, the large-value packet ledger permits

```text
R<=Y^(.038+o(1)).                                     (2.10)
```

It gives no upper bound on the length of a consecutive subcluster.  For a
legal consecutive set of the permitted size, (2.5) is smaller than every
power of `Y`.  Therefore no inference of the form

```text
#T<=Y^(.038+o(1))  ==>  G_T >= M Y^(-O(1)) I          (2.11)
```

can be true.  This conclusion holds for the actual prime-power nodes because
Theorem 2.1 uses only their already-known containment in `[-1/5,1/5]`.

This does **not** prove that an actual negative-large-value set contains a
cluster of maximal permitted length.  A theorem exploiting more than its
cardinality--for example the analytic source values carried by that set--is
not refuted.  What is refuted is the proposed passage from the published
packet count, by itself, to a uniform lower Gram spectrum.

For arbitrary prescribed centre data of unit norm, the minimum correction
energy can therefore be at least

```text
1/lambda_min(G)
 >=M^(-1) exp[(4.6085...+o(1))R].                     (2.12)
```

So an arbitrary-data polynomial right inverse is also impossible.

This is a scoped no-go.  The violation data in QP come from one analytic
prime polynomial and need not point in the worst eigenvector.  That is why
the next directional reduction remains live.

---

## 3. The exact source condition that survives

For any finite packet list `T={t_1,...,t_R}`, write

```text
A=[a(t_1),...,a(t_R)],
m=A^T q/M,
V=P A,
G=V^T V.                                               (3.1)
```

Assume `G` is nonsingular.

### Theorem 3.1 (minimum normalized centre-zeroing dual)

The minimum-norm vector satisfying

```text
q^T y=-1,             A^T y=0                         (3.2)
```

is

```text
y_*=-q/M+V G^(-1)m.                                   (3.3)
```

It has

```text
||y_*||_2^2=1/M+z_T,       z_T=m^T G^(-1)m.           (3.4)
```

Moreover

```text
z_T=sup_(c!=0) (c^T m)^2/(c^T Gc).                   (3.5)
```

If

```text
F_c(u_j)=sum_i c_i cos(t_i u_j),
bar F_c=M^(-1)sum_j F_c(u_j),
```

then (3.5) is exactly

```text
z_T=sup_c bar F_c^2/
           sum_j [F_c(u_j)-bar F_c]^2.                (3.6)
```

#### Proof

The two summands in (3.3) are orthogonal.  Also `q^T V=0` and

```text
A^T(-q/M)=-m,            A^T V=V^T V=G,
```

which proves (3.2)--(3.4); the normal equations prove minimality.  Formula
(3.5) is Cauchy--Schwarz in the `G` metric, with equality at
`c=G^(-1)m`.  Finally `c^Tm=bar F_c` and
`c^TGc=||P A c||^2`, giving (3.6).  QED

There is an equivalent augmented Schur formula.  Let

```text
h_T=q^T A(A^T A)^(-1)A^T q/M                          (3.7)
```

be the normalized leverage of the carrier in the unprojected packet span.
The rank-one identity `A^T A=G+Mmm^T` gives

```text
z_T=h_T/[M(1-h_T)].                                   (3.8)
```

Thus ordinary packet conditioning is not the right invariant.  The exact
question is whether the distinguished carrier lies too close to the packet
span.  A tiny eigenvalue of `G` is harmless when `m` has a commensurately
tiny component in that eigendirection; it is fatal only when the source
loads that direction.

Formula (3.8) also gives the weakest leverage gaps for norm control, without
hidden constants:

```text
existence of a centre-zeroing normalized dual: h_T<1;
z_T<=Y^C/M for some fixed C:               1-h_T>=Y^(-C+o(1));
z_T<=Y^o(1)/M:                             1-h_T>=Y^(-o(1));
z_T<<1/M:                                  h_T<=1-delta
                                             for some fixed delta>0.       (3.8a)
```

These statements concern only correction norm.  None controls what the
corrected polynomial does between or beyond the fitted packets.

Equivalently, the carrier gap is the exact prime-sampling approximation
error

```text
1-h_T=M^(-1) min_c sum_(p^k in shell)
       |1-sum_(t_i in T)c_i cos(t_i log(p^k/Y))|^2.   (3.8b)
```

So even the weakest subpower source theorem already says that no
data-dependent sparse high-frequency cosine packet approximates the constant
function on the complete actual prime-power shell more accurately than
`Y^(-o(1))` in normalized square mean.  This is a lower sampling theorem,
not a large-values upper theorem.

### Theorem 3.2 (carrier-residual form and binary endpoint)

Let

```text
Pi_T=A(A^T A)^(-1)A^T,
R_T=(I-Pi_T)q,
h_T=||Pi_T q||^2/M.                                   (3.9)
```

If `h_T<1`, the vector in Theorem 3.1 is equivalently

```text
y_T=-R_T/||R_T||^2,          ||R_T||^2=M(1-h_T).      (3.10)
```

It is the unique minimum-norm normalized dual vanishing on `T`.  At every
query frequency,

```text
y_T^T a(t)=-R_T^T a(t)/[M(1-h_T)].                    (3.11)
```

Therefore this correction is a full-band kill at level `epsilon` if and
only if

```text
R_T^T a(t)>=-epsilon M(1-h_T)       for every t in H. (3.12)
```

If `h_T=1`, the carrier lies in the packet span and no normalized dual can
vanish on all of `T`.

#### Proof

`R_T` is the orthogonal projection of `q` onto `ker(A^T)`.  The minimum-norm
vector in that kernel having inner product `-1` with `q` is therefore
`-R_T/(q^TR_T)`.  Orthogonal projection gives

```text
q^T R_T=||R_T||^2=M-||Pi_Tq||^2=M(1-h_T),
```

which proves (3.10)--(3.11).  Equation (3.12) is exactly the inequality
`y_T^Ta(t)<=epsilon`.  If `R_T=0`, every vector in `ker(A^T)` is orthogonal
to `q`, proving the last assertion.  QED

This gives the binary endpoint.  A carrier-leverage bound by itself does
**not** complete the correction.  The weakest exact remaining condition is
the one-sided residual antenna (3.12).  Moreover

```text
Q_T(t)=1-y_T^T a(t)/epsilon                           (3.13)
```

is nonnegative on `H` exactly when (3.12) holds, and then

```text
Q_T(0)=1+1/epsilon.                                   (3.14)
```

Conversely, any feasible Delsarte polynomial with value `1+1/epsilon` at
zero gives a normalized dual with supremum at most `epsilon` by reversing
(3.13).  Thus

```text
there exists y with q^Ty=-1 and sup_H y^Ta<=epsilon
  <==> A_H>=1+1/epsilon
  <==> r_+(H)<=epsilon.                               (3.15)
```

For a *prescribed* packet set, (3.12) is a sufficient subclass of the duals
in (3.15), not a claim that every Delsarte extremizer must arise by zeroing
that set.  But proving termination of the adaptive residual construction is
exactly a proof of the original Delsarte KILL inequality; source algebra
does not make the final arithmetic statement weaker.

### Corollary 3.3 (precise actual-prime theorem still needed)

A successful centre correction must prove a power-uniform version of

```text
sup_c |mean_(p^k in shell) F_c(log(p^k/Y))|^2
      /sum_(p^k in shell)|F_c-mean F_c|^2 <<Y^(-delta) (3.16)
```

for every packet family produced by the adaptive large-value cover, with
enough reserve to sum the successive off-packet errors.  The coefficients
`c` are arbitrary and data-dependent.  Pointwise bounds for each original
prime polynomial do not imply (3.16).

### Theorem 3.4 (sharp count plus ideal orthogonality can have `h_T=1`)

For every even integer `s>=2`, put

```text
R=s^2,             epsilon=1/s=R^(-1/2).
```

Let the rows of an `M by R` matrix `A` be all sign vectors
`x in {-1,1}^R` satisfying

```text
sum_i x_i=-s.
```

Then

```text
A^T A=M I_R,
A^T q/M=-epsilon q_R,
A(-q_R/s)=q,
A(q_R/R)=-epsilon q.                                  (3.16a)
```

Thus every column has the critical negative mean `-epsilon`, the packet
count saturates `R=epsilon^(-2)`, and the unprojected columns are perfectly
orthogonal, yet the carrier leverage is exactly `h_T=1` and the projected
Gramian is singular.  The last identity is a positive antipode of depth
`epsilon`.  In fact the finite-set minimax value is exactly `epsilon`.

#### Proof

Permutation symmetry gives `E x_i=-s/R=-1/s`.  For `i!=j`, symmetry and

```text
(sum_i x_i)^2=R+2 sum_(i<j)x_ix_j=s^2=R
```

give `E x_ix_j=0`.  These are the first two identities in (3.16a).  The row
sum identity gives the last two.  If `q^Ty=-1`, then

```text
-1=q^Ty=-(1/s)sum_i a_i^Ty,
```

so the average of the `R` dual values is `s/R=epsilon`; hence their maximum
is at least `epsilon`.  The uniform dual `-q/M` has every value exactly
`epsilon`, proving equality in the finite-set minimax.  QED

This is an abstract bounded-entry matrix, not an actual-prime cosine curve.
It proves a precise theorem-class obstruction: a sharp `R<=epsilon^(-2)`
large-value count, individual negative means, bounded atoms, and even ideal
unprojected orthogonality do not imply any carrier gap or a strict kill below
the critical depth.  Actual-prime phase structure would have to be used
beyond all four summaries.

The row count in this countermodel need not be combinatorially large.  On the
subsequence `R=4^n`, start from the regular Hadamard matrix

```text
H_4=2I_4-J_4
```

and take a signed tensor power `H_4^(tensor n)` whose row sums are all
`-sqrt(R)`.  It has exactly `M=R` rows and satisfies (3.16a); repeating every
row `K` times gives `M=KR` with the same normalized identities.  Thus the
obstruction persists when the ambient dimension is arbitrarily larger than
the critical packet count, as in the QP exponent ledger.

There is also an exact scalar sufficient condition if one insists on
separating source energy and propagation.  For

```text
k(t)=V^T P a(t),
L_T(t)=k(t)^TG^(-1)k(t)/||P a(t)||^2,
```

the zeroing increment is `delta=VG^(-1)m` and

```text
|delta^T a(t)|
 <=sqrt[z_T L_T(t)] ||P a(t)||
 <=sqrt[h_T L_T(t)/(1-h_T)].                          (3.17)
```

Thus a worst-case propagation reserve `epsilon` follows from

```text
L_T(t)<=epsilon^2(1-h_T)/h_T.                         (3.18)
```

At the fixed-slice target `epsilon=Y^(-.019)`, a constant carrier gap still
requires `L_T(t)<<Y^(-.038)` off the merged packet set.

The genuinely weakest directional requirement is the unsquared identity

```text
|m^T G^(-1)k(t)|<=epsilon,                            (3.19)
```

which can be much better than (3.18) if source and query are favorably
aligned.  Neither a bound `h_T<=1-delta` nor a Gram lower bound alone implies
(3.18) or (3.19).

---

## 4. Off-packet leverage also sees clusters

Let the first `R` consecutive projected atoms span `E_R`, and let
`v_R=P a(t_0+Rh)` be the next atom.  The same finite-difference identity,
now of order `R`, gives

```text
dist(v_R,E_R)<=sqrt(M)[2 sin(hw/2)]^R.                (4.1)
```

If `||v_R||^2>=gamma M`, its normalized leverage satisfies

```text
L_T(t_0+Rh)
 =||Proj_(E_R)v_R||^2/||v_R||^2
 >=1-gamma^(-1)[2 sin(hw/2)]^(2R).                   (4.2)
```

Hence deleting only the fitted centres cannot yield a uniform leverage gap
at an adjacent omitted packet.  One can merge consecutive packets and use a
confluent/jet basis, but then the theorem required is a demand-specific
Hermite/source estimate for the whole merged block.  Renaming the basis does
not supply (3.16).

---

## 5. Why the surveyed tools do not fill (3.16)

The scopes below were checked against the primary statements.

1. **Guth--Maynard.**  [Theorem 1.1](https://arxiv.org/html/2405.20552v2#S1.Thmtheorem1)
   bounds the number `R` of one-separated large values.  In their singular-
   value reduction, [Lemma 4.1](https://arxiv.org/html/2405.20552v2#S4.Thmlemma1)
   controls those values by the **largest** singular value `s_1(M_W)`.
   Neither statement bounds the smallest projected singular value, the
   carrier leverage (3.7), or the source quotient (3.6).  The consecutive
   cluster in Theorem 2.1 is compatible with their hypotheses.

   The exact exponent substitution confirms the mismatch.  For the original
   prime indicator, take `N=Y`, `T=Y^(50/33)` and
   `V=Y^(1-c-o(1))`.  Their three terms become

   ```text
   N^2 V^-2              =Y^(2c+o(1)),
   N^(18/5)V^-4          =Y^(-2/5+4c+o(1)),
   T N^(12/5)V^-4        =Y^(50/33-8/5+4c+o(1)).      (5.1)
   ```

   At `c=.019`, the last two exponents are `-.324...` and
   `-.008848...`; only the packet count `Y^(.038+o(1))` remains.

   For the adaptive residual `R_T`, normalizing coefficients to meet
   `|b_n|<=1` changes the large-value threshold to

   ```text
   V_T=epsilon ||R_T||_2^2/||R_T||_infinity.          (5.2)
   ```

   Recovering the same substitution already requires the additional
   flatness theorem

   ```text
   ||R_T||_2^2/||R_T||_infinity=Y^(1-o(1)).           (5.3)
   ```

   A leverage gap `h_T<=1-delta` controls the numerator in (5.3), but not
   the infinity norm.  Even assuming both (5.3) and the leverage gap,
   Guth--Maynard again supplies only a count, not (3.12), (3.18), or (3.19).

2. **Montgomery--Vaughan / Halasz--Montgomery.**  The primary
   [Hilbert inequality](https://doi.org/10.1112/jlms/s2-8.1.73) gives
   large-sieve/mean-value upper bounds under frequency separation.  It does
   not reverse a clustered Gramian, and it does not single out `q`.  Applying
   it after discarding close centres loses the discarded interpolation
   constraints.

3. **Clustered Fourier conditioning.**  Batenkov--Demanet--Goldman--Yomdin
   prove that the smallest singular value deteriorates with the maximal
   cluster size in their partial nonuniform Fourier model
   ([primary preprint](https://arxiv.org/abs/1809.00658)).  This is consistent
   with (2.2).  Their theorem is an unaugmented `L^2` condition-number result,
   not an actual-prime carrier-source estimate.

4. **Spectral sparsification.**  Batson--Spielman--Srivastava sparsify an
   already-given positive semidefinite sum while preserving its quadratic
   form ([Theorem 3.1](https://arxiv.org/abs/0808.0163)).  It preserves an
   existing bad direction as well as the good ones; it cannot manufacture a
   lower bound absent from `G`.  Sparsifying packet columns instead drops
   packet constraints and supplies no off-packet theorem.

5. **Restricted invertibility.**  Bourgain--Tzafriri-type theorems select a
   large well-conditioned subset of columns.  The conclusion is not an
   interpolant for the omitted columns, and no carrier-source or sign
   condition is part of the theorem.  The missing step is again (3.16) plus
   propagation, not subset selection.

6. **The available principal prime-twist estimate.**  Klurman--Mangerel--
   Teravainen, [Lemma 7.9 and Remark 7.2](https://doi.org/10.1112/plms.12546),
   sets `X=x^((log x)^(1/25))` and is uniform for `|t|<=X`; this range does
   contain the polynomial aperture `Y^(50/33)`.  The theorem nevertheless
   gives only a logarithmic saving `x/(log x)^(.3)` for the principal twist
   (with the stated sharp/smooth endpoint distinction).  It supplies neither
   the required fixed power nor an estimate for the data-dependent residual
   coefficients in (3.12).  The superscript in its definition of `X` is
   essential; reading it as multiplication would incorrectly shrink the
   published range.

These are theorem-scope failures, not claims that the cited results are
weak.  They answer different spectral quantifiers.

---

## 6. Disposition and next admissible attack

The Gram branch has now failed fast in its strongest advertised form:

```text
bad-packet count -> uniform Gram lower bound:          refuted exactly;
Gram lower bound -> arbitrary correction control:      algebraically valid
                                                        but unavailable;
demand-specific source control (3.16):                 not refuted;
source control + off-packet iteration:                 conditional only.
```

The next admissible projected-Gram theorem is therefore not
`lambda_min(G_T)>>M Y^(-O(1))`.  It is the actual-prime directional statement

> For every adaptively produced, cluster-merged bad family, bound the carrier
> leverage `h_T` away from one, or equivalently bound `z_T` in (3.6), in the
> natural confluent basis; then prove that the corresponding minimum-source
> correction has summable leverage on the complement.

This must exploit multiplicative arithmetic.  Packet count, additive energy,
generic rank, graph sparsification, and unaugmented large-sieve bounds do not
have the necessary quantifier.  Proving the scalar equal-weight estimate
instead would bypass this gate, but the audited uniform fixed-power version
is adjacent to a fixed zero-free strip and is not supplied by current prime
Dirichlet-polynomial results.

## 7. Replay

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_qp_projected_gram_cluster_gate.py
PYTHONPATH=src python3 src/qp_projected_gram_cluster_gate.py
PYTHONPATH=src python3 \
  results/verify_zeta23_qp_projected_gram_cluster_gate.py
```

The replay verifies the finite-difference identity, exact central-binomial
normalization, Rayleigh bound, fixed-shell exponential rate, next-packet
distance bound, minimum zeroing dual, Schur formula, and variational source
identity.
