# QP mask-preserving local lift: exact finite refutation and GL(3) reciprocity audit

**Date:** 2026-08-24  
**Binary verdict:** the proposed coefficient-blind route

```text
first-Poisson CRT lift
  -> delete the coherent k=t*c rays
  -> full two-dimensional Poisson
  -> c-independent Whittaker/Hecke coefficient space
  -> sharp l2 coefficient norm
```

is **false**.  The first arrow can be made exactly isometric and the coherent
intersection can be projected exactly.  The second Poisson transform then
restores, on every nonzero dual frequency, the complete phase

```text
e_c(-a_bar*u*v).
```

Two copies therefore have the unavoidable Fourier index

```text
Delta=u*v-u'*v'.
```

The coefficient of `lambda_pi(Delta)` is an additive autocorrelation of a
product convolution.  A flat, entirely nonzero dual box has off-diagonal
coefficient energy larger than the proposed tensor norm by a factor
`>>L^2`.  This remains true after deleting `Delta=0` and after projecting
the coherent residue.

[Yang's Fourier-analytic spectral reciprocity](https://arxiv.org/abs/2512.03305)
does supply a genuine `c`-independent GL(3)/GL(2) Whittaker-Plancherel
identity, including noncuspidal GL(3).  It does **not** supply the missing
synthesis contraction from the QP mask to a GL(3) vector.  Whittaker
Plancherel preserves the large norm exhibited below, and the noncuspidal
formula contains several further degenerate and residual channels which
are not removed by the single coherent-ray projection.

This is a refutation of the proposed exact local/Plancherel mechanism.  It
is **not** a counterexample to a still stronger global theorem which uses
cancellation among the full, `c`-dependent DFI masks.  Such a theorem would
have to use precisely the arithmetic information discarded by the local
lift.

---

## 1. The universal first-Poisson Hilbert space exists

Write the fundamental residue of a long frequency as

```text
k=k_0+t*c,                    0<=k_0<c,
```

and put

```text
theta_(c,a)(r,k_0)=U*r/R-a*k_0/c  (mod 1).                 (1.1)
```

There is a `c`-independent Hilbert space

```text
H_0=ell^2((Q/Z) x Z)
```

and, for every fixed primitive `(c,a)`, an exact isometric embedding

```text
I_(c,a): e_(r,k_0,t) -> e_(theta_(c,a)(r,k_0),t).           (1.2)
```

The CRT assertion in the earlier report is exactly what proves that (1.2)
is injective.

### Lemma 1 (exact cross-modulus intersection)

Suppose `c,c',R` are pairwise coprime and `U,a,a'` are units in the
appropriate residue rings.  Then the fundamental phase ranges in (1.1)
intersect exactly in

```text
(r,k_0;r',k'_0)=(r,0;r,0),             r mod R.            (1.3)
```

**Proof.**  Equality of the two phases implies, for some integer `z`,

```text
U*(r-r')*c*c' - R*a*k_0*c' + R*a'*k'_0*c = z*R*c*c'.      (1.4)
```

Reduction modulo `c` gives `k_0=0`, and reduction modulo `c'` gives
`k'_0=0`.  The remaining equality gives `r=r' (mod R)`.  The converse is
immediate.  This proves (1.3).  `square`

Consequently the projection

```text
P_perp=1-projection onto {k_0=0}                           (1.5)
```

makes the first-Poisson ranges for pairwise coprime moduli orthogonal.  This
is the strongest positive part of the proposed construction.

It does not yet help Kuznetsov.  Keeping the resulting modulus blocks
orthogonal also keeps `c` as an external label and gives only the old
fixed-`c` Parseval bound.  To obtain the required inter-modulus saving, the
second Poisson transform and the primitive numerator sum must still be
performed.

## 2. The second Poisson transform undoes the hoped-for projection gain

The finite core of the complete two-dimensional Poisson calculation is

```text
G_(c,a)(u,v)
 =sum_(x,y mod c)e_c(a*x*y+u*x+v*y)
 =c*e_c(-a_bar*u*v).                                      (2.1)
```

The raw coherent ray `k=t*c` is the residue `y=0`.  Its exact orthogonal
deletion gives

```text
G^perp_(c,a)(u,v)
 =sum_(x mod c, y!=0 mod c)e_c(a*x*y+u*x+v*y)
 =c*[e_c(-a_bar*u*v)-1_(u=0 mod c)].                      (2.2)
```

In particular,

```text
G^perp_(c,a)(u,v)=G_(c,a)(u,v),       u!=0 (mod c).        (2.3)
```

If both zero residues are deleted, inclusion-exclusion gives

```text
G^(perp,perp)_(c,a)(u,v)
 =c*e_c(-a_bar*u*v)-c*1_(u=0)-c*1_(v=0)+1.               (2.4)
```

For `u,v!=0`, the only change is the `a`-independent `+1`.  After the
primitive numerator sum this is a Ramanujan/degenerate correction; the
nondegenerate phase in (2.1) is unchanged.

The factors `R` and `S` in the actual opposite-cusp calculation merely
rescale `u` and `v` by units modulo `c`.  Thus (2.1) is exactly the finite
core of `(2E.F7o20y)`.  Combining two copies and the delta numerator gives

```text
1/c sum_(a mod c)^* e_c(-a*h-a_bar*(R*S)^(-1)*Delta)
 =S(-h,-(R*S)^(-1)*Delta;c)/c,                            (2.5)

Delta=u*v-u'*v'.                                          (2.6)
```

Equations (2.2)--(2.6) prove that deleting the coherent ray does not change
the native nonzero spectral index.

## 3. The exact coefficient is additive, not Hecke-multiplicative

Let the two nonzero dual sequences be `p_u` and `q_v`, and define their
product convolution

```text
g(m)=sum_(u*v=m)p_u*q_v.                                  (3.1)
```

Grouping (2.6) by its integer value gives the unique natural coefficient

```text
B_Delta
 =sum_m g(m)*conj(g(m-Delta))
 =sum_(u*v-u'*v'=Delta)
      p_u*q_v*conj(p_(u')*q_(v')).                        (3.2)
```

After a standard Kuznetsov expansion, the corresponding formal spectral
coefficient is

```text
A_pi=sum_(0<|Delta|<=D) B_Delta*lambda_pi(|Delta|),        (3.3)
```

with the two signs treated by the usual parity convention.  Thus a single
Hecke polynomial does exist for one fixed completed block.  Its coefficient
norm is the obstruction.

The integer `Delta` cannot be harmlessly relabelled.  For a prime
`c>2D`, the map

```text
z -> [h -> sum_(|n|<=D)z_n*S(-h,-n;c)/c]                  (3.4)
```

is injective.  Indeed, Fourier transform in `h mod c` at a nonzero
frequency `b` gives

```text
sum_n z_n e_c(-b_bar*n).                                  (3.5)
```

If all of (3.5) vanish, the residue measure `z` is constant.  Its support
is a proper subset of `Z/cZ`, so that constant is zero.  At the balanced
scales `c asymp q^(25/33)` and `D=q^(16/33)`, the hypothesis `c>2D` holds
with a power to spare.

The lack of a physical-tuple invariant is already visible in a finite
opposite-cusp fixture.  Take

```text
R=5, S=7, U=2, V=3,                 R*V-S*U=1,
(r,r',s,s')=(1,2,1,2).
```

Using centered representatives in the two congruences from
`(2E.F7o20y)` gives

```text
c     (nu,mu;nu',mu')          Delta_c
11    ( 2,-2; -1, 3)              -1
13    ( 1,-3;  2, 1)              -5
17    (-1, 2; -2,-3)              -8
19    (-2, 1;  1, 2)              -4.                    (3.6)
```

All four dual coordinates are nonzero.  Thus the same physical Hilbert
coordinate acquires four different, injectively detectable Hecke indices
after the full transform.  The `t` coordinate in (1.2) has been consumed
by the second Fourier transform and is no longer an external invariant.

## 4. Polynomial counterexample to the sharp coefficient norm

Take

```text
p_u=q_u=1_(1<=u<=L),             L>=2, c>L^2.              (4.1)
```

Every dual coordinate in (4.1) is nonzero, so (2.3) shows that the coherent
projection does nothing to it.  Put

```text
r(m)=#{(u,v) in [1,L]^2:u*v=m}.
```

Then (3.2) is the nonnegative additive autocorrelation of `r`.  Its
off-diagonal `l1` mass is

```text
sum_(Delta!=0)B_Delta=L^4-B_0.                            (4.2)
```

Since `max_m r(m)<=L` and `sum_m r(m)=L^2`,

```text
B_0=sum_m r(m)^2<=L^3.                                    (4.3)
```

There are fewer than `2L^2` possible nonzero differences.  Cauchy applied
to (4.2), followed by (4.3), proves

```text
sum_(Delta!=0)|B_Delta|^2
 >=(L^4-L^3)^2/(2L^2)
 =L^4*(L-1)^2/2.                                          (4.4)
```

The proposed sharp tensor scale is

```text
(||p||_2^2*||q||_2^2)^2=L^4.                             (4.5)
```

Hence (4.4) exceeds (4.5) by at least

```text
(L-1)^2/2.                                                (4.6)
```

Normalizing `p` and `q` to unit norm leaves the same ratio.  At the QP
dual scale `L=sqrt(D)`, this is a full factor `asymp D`, not `D^o(1)`.
The zero difference has already been removed, and either Kuznetsov sign
sector retains a fixed fraction of (4.4).

This proves the following no-go theorem.

### Theorem 2 (no sharp coefficient-blind local lift)

There is no exact local intertwiner which

1. agrees with the complete double-Poisson phase (2.1) on nonzero dual
   frequencies;
2. removes only the coherent zero residues and the product diagonal; and
3. maps every separable pair `(p,q)` to (3.3) with

```text
sum_(Delta!=0)|B_Delta|^2
 <<D^o(1)*(||p||_2^2*||q||_2^2)^2.                        (4.7)
```

**Proof.**  Equations (2.2)--(2.6) force (3.2) on the nonzero box (4.1),
while (4.4)--(4.6) contradict (4.7).  `square`

At the balanced point the physical fan counts are `P=Q=sqrt(D)`, and the
aligned-modulus fixture in the canonical report realizes a positive
fraction of such a nonzero box through the exact congruence partial
permutations.  What has not been constructed is simultaneous flat-box
alignment for a power-sized family of DFI moduli.  That distinction is why
Theorem 2 refutes a local or coefficient-blind lift, but not every possible
global mask-sensitive estimate.

## 5. The conditional product-of-two-Hecke-polynomials identity is also false generically

The conditional identity `(2E.F7o20k)` would express every data term as a
product of two Hecke polynomials of length `Y=sqrt(D)`.  In the formal
unramified Hecke algebra,

```text
lambda(m)lambda(n)=sum_(d|(m,n))lambda(m*n/d^2).            (5.1)
```

If `p` is a prime with `Y<p<2Y`, then `lambda(p)` cannot occur on the
right of a product with `m,n<=Y`: the equality `m*n/d^2=p` would force
`p` to divide `m` or `n`.

On the other hand, the double-Poisson difference box contains `p` exactly:

```text
p=Y*2-1*(2Y-p),                                           (5.2)
```

and all four factors in (5.2) lie in `[1,Y]`.  Thus one delta mass at that
dual four-tuple contributes `lambda_pi(p)` but cannot be a product of two
length-`Y` Hecke polynomials.  This is an algebraic obstruction, separate
from the norm obstruction in Section 4.

A general single polynomial (3.3) remains possible; it is its sharp norm,
not its formal existence, that fails.

## 6. Audit of the noncuspidal GL(3) reciprocity pivot

The pivot is mathematically natural.  The shift coefficient
`lambda_pi(h)` together with two short data polynomials is a truncated
cubic GL(2) moment, and the specialization

```text
Pi_GL3 = 1 boxplus 1 boxplus 1
```

is the noncuspidal GL(3) object underlying Motohashi-type reciprocity.
Yang's Theorem A gives a genuine global identity between a GL(2) spectral
sum of GL(3) Rankin--Selberg periods and a dual Fourier expansion.  Section
3.3.4 treats unitary minimal Eisenstein data by meromorphic
regularization, and equation (9.40) uses the local GL(2)
Whittaker-Plancherel decomposition.  This is exactly the correct
representation-theoretic home for a `c`-independent space.

It does not prove the desired QP lift, for three exact reasons.

### 6.1 Plancherel is downstream of the missing synthesis estimate

Yang starts with an already constructed global GL(3) Whittaker vector
`W_phi`.  Whittaker-Plancherel decomposes that vector isometrically into
GL(2) representations.  To apply it here one must first construct

```text
(QP coefficient mask) -> W_phi                              (6.1)
```

with the sharp norm required by `(2E.F7o20i)`.  On the finite complete
cell, (6.1) is exactly the map `(p,q)->(B_Delta)`.  Theorem 2 shows that
this synthesis map has norm at least `>>L`, after squaring, on unrestricted
nonzero separable data.  Plancherel preserves that norm; it cannot erase
it.

The analytic-newvector estimates in Sections 9--10 control specially
constructed local vectors and their transforms.  They do not assert (4.7)
for an arbitrary selected QP mask.

### 6.2 One coherent ray is not the noncuspidal constant term

For minimal Eisenstein data, Theorem A contains singular, dual,
degenerate, opposite-degenerate, Eisenstein, and residue contributions.
The explicit fourth-moment specialization likewise has three Weyl
degenerate terms and residual terms.  Deleting `k=t*c` accounts for the
single correction in (2.2); it does not project all of those automorphic
constant-term channels.  Formula (4.4) is a finite witness that substantial
noncuspidal energy remains on nonzero dual frequencies.

### 6.3 The actual common carrier is Hilbert-valued, not a scalar Hecke label

Schematically, scalarizing the three-factor mask gives

```text
alpha_n=sum_(a*b*c=n) 1_S(a)1_S(b)z_c.                     (6.2)
```

Squaring (6.2) no longer forces the two triples to have the same common
carrier `b`.  The physical two-star count requires instead the
Hilbert-valued coefficient

```text
alpha_n(b)=1_S(b)*sum_(a*c=n/b)1_S(a)z_c.                  (6.3)
```

The selected-shell projection in the external `b` coordinate is exactly
the BDH/two-inverse restriction gate from the companion report.  A scalar
GL(3) Rankin--Selberg period does not supply it.  Formal Hilbert
tensorization only restates the problem because the finite local transform
and its level/cusp data depend on `b`.

Thus Yang's identity is a valuable possible *global reorganization*, but
using it would require a new mask-sensitive, Hilbert-valued synthesis
theorem.  It is not the missing theorem already present in the paper.

## 7. Finite-rank polar subtraction does not repair the norm

Deleting only `Delta=0` is not the strongest natural Eisenstein repair.
One could try to subtract the whole span of classical shifted-divisor polar
terms before applying Plancherel.  The following fixture shows exactly how
large that span would have to be.

### Theorem 3 (exact separated polar no-go)

Let `2<=L<=Y/4`, `1<=K<=Y/(4L)`, and define

```text
U={floor(Y/2),...,floor(Y/2)+L-1},
V={1,2L,4L,...,2KL}.                                  (7.1)
```

For `0<=j<L`, put

```text
p_j(u)=1_U(u)*e(j*u/L),       q(v)=1_V(v),             (7.2)
```

and form `g_j` and `B_j` as in (3.1)--(3.2).  All four dual variables are
nonzero and at most `Y`.  For every `1<=h<L`, one has the exact identity

```text
B_j(h)=(L-h)*e(j*h/L).                                 (7.3)
```

Consequently

```text
sum_(1<=h<L)|B_j(h)|^2
 =S_L:=(L-1)*L*(2L-1)/6,                              (7.4)

(||p_j||_2^2*||q||_2^2)^2=L^2*(K+1)^2.               (7.5)
```

If `E` is any fixed subspace of `C^(L-1)` of dimension `d`, and `P_E` is
orthogonal projection onto `E`, then for at least one `j`

```text
||(1-P_E)B_j||_2^2
 >=sum_(n=1)^(L-d-1)n^2.                              (7.6)
```

Here "fixed" means independent of the arbitrary modulation `j`; the
coefficients of the best subtraction inside `E` may depend on `j`.

**Proof.**  The products `vU` belonging to distinct `v` in (7.1) are
separated by more than `L`.  Within a branch `v>=2L`, two distinct products
differ by at least `2L`.  Hence a difference `0<h<L` can only come from
`v=v'=1`, where `u-u'=h`; summing (7.2) gives (7.3).  Equations (7.4) and
(7.5) follow from `|U|=L` and `|V|=K+1`.

Write `b_j=(B_j(h))_(1<=h<L)`.  Fourier orthogonality gives the exact frame
identity

```text
1/L*sum_(j=0)^(L-1)b_j*b_j^*
 =diag((L-1)^2,(L-2)^2,...,1).                        (7.7)
```

Thus the average energy captured by `P_E` is the trace of `P_E` against
the diagonal matrix in (7.7).  Ky Fan's principle bounds it by the sum of
the `d` largest eigenvalues,

```text
1/L*sum_j||P_E b_j||_2^2
 <=sum_(n=L-d)^(L-1)n^2.                              (7.8)
```

Subtracting (7.8) from (7.4) proves (7.6).  `square`

This is a no-go for every prescribed finite- or subpower-rank collection
of residues, degenerate shifted-divisor terms, or major-arc profiles.  An
orthogonal projection is already the best possible coefficient-dependent
subtraction taking values in their span.

The normalization is polynomially hostile.  For example, along a compatible
integer sequence take

```text
Y=D^(1/2),       L=D^(1/4),       K=D^(1/16).             (7.9)
```

Then (7.1) fits inside the full dual box and

```text
S_L/[L^2*(K+1)^2]=D^(1/8+o(1)).                         (7.10)
```

More precisely, let `F(m)=m(m+1)(2m+1)/6`.  If one fixed polar space is
to leave at most the tensor scale in (7.5) for every modulation, the exact
trace obstruction is

```text
F(L-d-1)<=L^2*(K+1)^2.                                 (7.11)
```

Therefore its rank must satisfy

```text
d>=L-1-max{m:F(m)<=L^2*(K+1)^2}
 >=L-1-(3L^2*(K+1)^2)^(1/3).                           (7.12)
```

For `K=L^(1/4)`, this is `d>=L-O(L^(5/6))`.  Even merely
removing a fixed fraction `1-epsilon` of (7.4) for every `j` requires

```text
d>=(1-epsilon^(1/3))*L+O(1).                           (7.13)
```

Thus the necessary effective polar rank is not just unbounded: it is
comparable with the entire length-`L` shift space.

### 7.1 The physical smooth mask does not rescue finite rank

On an interior short-shift chart where the inherited archimedean factor
obeys

```text
0<c_0<=|Psi_h|<=C_0,             1<=h<L,                (7.14)
```

the weighted frame operator is exactly

```text
diag(|Psi_h|^2*(L-h)^2).                                (7.15)
```

Its total trace is at least `c_0^2*S_L`, while a rank-`d` projection can
capture at most `C_0^2*d*(L-1)^2`.  Hence every `d=o(L)` polar space leaves
`(c_0^2/3+o(1))*L^3` energy for some modulation.  A smooth nonvanishing
diagonal `Psi` therefore does not turn the finite-rank subtraction into a
contraction.  If `Psi_h` is flat up to `1+o(1)` on the chart, the sharper
rank thresholds (7.12)--(7.13) persist up to `1+o(1)`.

This remains a completed fixed-block statement.  The companion bulk report
gives an exact aligned pullback to a quantitatively broad physical fan at
one modulus, but neither construction supplies prime-power/product-window
occupancy for one coefficient vector across the full moving-`c` DFI sum.
That is the surviving global mask-sensitive distinction.

### 7.2 What this does **not** refute: a rank-`L` Eisenstein continuum

A full continuous Eisenstein family with arbitrary inducing data is not a
finite collection of polar residues.  After restriction to `1<=h<L`, its
closed span may have effective rank comparable with `L`--and can in
principle equal all of `C^(L-1)`.  Theorem 3 does **not** refute such a
continuum.  It quantifies the price: any successful realization must have
rank at least (7.12), and hence `L-o(L)` in the hostile normalization above.

Calling that rank-`L` span "the polar part" does not by itself prove a
bound.  Projecting onto all of `C^(L-1)` removes the coefficient vector
vacuously, after which one must still estimate the equally large projected
Eisenstein contribution.  To make the continuum useful one must prove all
of the following with the original QP selector retained:

```text
* an exact synthesis map from the physical moving-c mask to inducing data;
* its correct local and global Plancherel measure;
* a tensor-scale norm bound for that synthesis map;
* control of the resulting continuous Eisenstein contribution.          (7.16)
```

Those are precisely the contents of the missing mask-sensitive,
Hilbert-valued restriction theorem.  Thus an arbitrary-inducing-data
rank-`L` continuum remains a logically open route, but it is not a free
polar subtraction or a consequence of classical finite-rank residue
extraction; without (7.16), it only restates the target estimate.

## 8. Exact remaining escape and final status

The full DFI weight

```text
H_DFI(c/C,(j*k-j'*k'-h)/C^2)                              (7.1)
```

couples the two copies, and its exact sum ranges over lower as well as top
modulus blocks.  The finite no-go above freezes one completed local block.
It remains logically possible that the `c`-dependent masks in (7.1), after
all degenerate pieces are extracted, cancel the flat-box energy across
moduli.  Such cancellation is not a local Hilbert-space isometry and is not
provided by Whittaker-Plancherel.  It would be a genuinely new global
restriction/reciprocity estimate.

The audited status is therefore

```text
universal first-Poisson Hilbert space:                 CONSTRUCTED;
cross-modulus intersection after coherent deletion:   EXACTLY ORTHOGONAL;
commutation with full second Poisson:                  NO;
nonzero complete phase after coherent deletion:       UNCHANGED;
native full-Poisson index:                             Delta=uv-u'v';
single fixed-block Hecke polynomial:                   EXISTS;
sharp l2 norm for its coefficients:                   FALSE (factor >>L^2);
product of two length-sqrt(D) Hecke polynomials:       FALSE GENERICALLY;
Yang noncuspidal GL3 reciprocity identity:             APPLICABLE IN SHAPE;
Yang supplies QP-mask synthesis contraction:          NO;
one coherent projection removes all degenerate terms: NO;
finite/subpower-rank polar subtraction repairs norm: NO;
minimum rank at tensor scale in separated fixture:       L-O(L^(5/6));
arbitrary-inducing-data Eisenstein continuum:            NOT REFUTED;
rank-L continuum supplies synthesis norm automatically: NO;
full global DFI mask-sensitive local-lift estimate:    STILL OPEN;
proposed local-Plancherel proof of that estimate:      REFUTED.
```

Executable exact checks are in
[`qp_mask_preserving_local_lift.py`](../src/qp_mask_preserving_local_lift.py)
and
[`test_qp_mask_preserving_local_lift.py`](../src/test_qp_mask_preserving_local_lift.py).
