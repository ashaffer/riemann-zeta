# Sharp sparse positive-cosine antipodes

## Compression, prescribed-support realization, and exact classification

**Date:** 2026-08-14

**Status:** proved as a finite harmonic theorem and independently
hostile-audited.  Six unit tests and an independent verifier replay the root
cells, rank selection, antipode identity, and consecutive-support
classification.

**Verdict:** in an `M`-coordinate cosine dictionary, `M` is the sharp sparse
scale.

* Every positive antipode from a finite harmonic pool can be replaced by one
  of at least the same depth using at most `M` harmonics.
* Off a null meagre analytic exceptional set, the deepest positive antipode is
  unique and uses exactly `M` harmonics whenever one exists.
* Conversely, for **every prescribed set of `M` positive harmonics**, however
  sparse or remote, and every `0<r<1`, there is a phase point of exact depth
  `r` lying inside an open strict-positive-antipode chamber.  Depth varies
  continuously, and need not remain exactly `r`, across that chamber.
* On the consecutive support `{1,...,M}`, feasibility has an exact
  if-and-only-if classification by the Chebyshev coefficients of the nodal
  polynomial.

The prescribed-support construction is explicit.  If `D=max K`, put more
than `(1+r)/2` of the probability weight on `D`.  The scalar cosine
polynomial then alternates sign at the `D+1` points `j*pi/D`, has exactly one
simple root in every intervening cell, and its full root-by-frequency table
has column rank `M`.  Any invertible `M`-row minor is the desired antipode.

The accompanying palindromic polynomial has all `2D` roots simple and
unimodular.  That root-location component is a direct specialization of the
classical Lakatos--Losonczi coefficient-dominance theorem; it is included as
an exact corollary, not claimed as new.  The contribution supported here is
the transposed prescribed-support construction together with sharp generic
sparsity and the Chebyshev sign strata.  Unique finite-pool optimization is a
useful classical convex-geometric consequence of the general-position lemma,
not a separate novelty claim.  A broader expert literature review would still
be required before making a priority claim for that synthesis.

This theorem does not place an actual prime-log orbit in one of these chambers
before the QP aperture.  It proves neither QP promotion nor a zero-free strip.

---

## 1. Setup

For a phase vector

```text
theta=(theta_1,...,theta_M) in (0,pi)^M
```

and a positive integer `k`, define the cosine atom

```text
a_k(theta)=(cos(k theta_1),...,cos(k theta_M)) in R^M,
q_0=(1,...,1).                                         (1.1)
```

For a finite harmonic set `K`, a positive antipode of depth `r>0` is an
identity

```text
sum_(k in K) w_k a_k(theta)=-r q_0,
w_k>=0,                 sum_(k in K)w_k=1.             (1.2)
```

Its sparsity is the number of nonzero weights.  A strict antipode has all
weights positive.

The orientation in (1.1) is important.  Classical trigonometric moment
curves vary one phase while holding the frequency coordinates fixed.  Here
the phases are the coordinates and the harmonics are the atoms: the relevant
matrix is the transpose of the usual sampling orientation.

---

## 2. Sharp compression and the generic optimizer

### Theorem 2.1 (depth-preserving `M`-atom compression)

Let `H` be a finite harmonic pool.  If (1.2) holds at depth `r_0>0` using
harmonics from `H`, then it holds at some depth `r_*>=r_0` using at most `M`
harmonics from `H`.

#### Proof

Let

```text
C=conv{a_k(theta):k in H} subset [-1,1]^M.             (2.1)
```

The set of `r` for which `-r q_0` belongs to `C` is compact.  Choose its
largest positive element `r_*`.  The point `-r_*q_0` is on the boundary of
`C`; otherwise it could be moved a little farther down the same ray.

If `C` has affine dimension at most `M-1`, Caratheodory in its affine hull
uses at most `M` vertices.  If `C` has dimension `M`, a supporting face at
`-r_*q_0` has dimension at most `M-1`, and Caratheodory inside that face again
uses at most `M` vertices.  QED

The improvement from the ambient `M+1` Caratheodory bound to `M` comes from
maximizing along a fixed ray and landing on a proper face.  This is classical
convex geometry, closely aligned with Elfving's directional-design picture.

### Theorem 2.2 (generic full spark and unique deepest antipode)

There is a conull residual set `G_M subset (0,pi)^M` with the following
properties.

1. Every square cosine minor

   ```text
   (cos(k theta_j))_(j<=M,k in K),       #K=M,          (2.2)
   ```

   is nonsingular.

2. Every `M+1` harmonic atoms are affinely independent.

3. For every harmonic set `S` with `#S<M`,

   ```text
   q_0 notin span{a_k(theta):k in S}.                    (2.3)
   ```

Consequently, fix `theta in G_M` and a finite pool `H` with `#H>=M`.  If a
positive antipode exists, its maximum possible depth is attained by a unique
antipode, and that antipode has exactly `M` positive weights.

The same generic lower bound holds against **all** finite integer-harmonic
supports at once: no exact signed representation of a nonzero multiple of
`q_0` can use fewer than `M` harmonics.

#### Proof

Each determinant in (2.2) is real analytic in `theta` and is not identically
zero.  One direct certificate is the generalized-Vandermonde expansion.  For
pairwise distinct positive `u_j` and distinct nonnegative frequencies `k_l`,

```text
det(cos(tau u_j k_l))
 = C(u,k) tau^(m(m-1))+O(tau^(m(m-1)+2)),              (2.4)

C(u,k)=(-1)^(m(m-1)/2)
       product_(i<j)(u_j^2-u_i^2)
       product_(i<j)(k_j^2-k_i^2)
       / product_(ell=0)^(m-1)(2ell)! !=0.             (2.5)
```

This proves (1).  For affine independence in (2), append the row of ones and
interpret it as evaluation at the additional node `u=0`; (2.4)--(2.5) still
apply.  For (3), use frequencies `{0} union S`, where frequency zero is the
carrier column, and any `#S+1` phase rows.  Thus every failure locus is the
zero set of a nonzero real-analytic function.  Taking the countable union over
integer harmonic sets leaves a null meagre set.

Now let `x_*=-r_*q_0` be the terminal ray point from Theorem 2.1.  If
`#H=M`, square full spark makes its representation unique, while (2.3)
forces all `M` weights to occur.  If `#H>=M+1`, affine full spark makes the
polytope `C` simplicial.  Were `x_*` in a proper face below facet dimension,
that simplex would represent it with fewer than `M` vertices, contradicting
(2.3).  Hence `x_*` lies in the relative interior of a unique simplicial
facet.  That facet has exactly `M` vertices and unique strictly positive
barycentric coordinates.  QED

The generic statement is stronger than a numerical rank observation: its
exceptional set is explicitly a countable union of proper determinant
varieties.

---

## 3. Every prescribed support has a chamber of every subunit depth

### Theorem 3.1 (dominant-top prescribed-support realization)

Let

```text
K={k_1<...<k_M},              D=k_M.                   (3.1)
```

Choose `0<r<1` and strictly positive weights `w_k` satisfying

```text
sum_(k in K)w_k=1,
w_D>(1+r)/2,          equivalently r<2w_D-1.           (3.2)
```

Then the cosine polynomial

```text
G(theta)=r+sum_(k in K)w_k cos(k theta)                (3.3)
```

has exactly one simple root in every interval

```text
(j*pi/D,(j+1)*pi/D),             0<=j<D.               (3.4)
```

Let these `D` roots be `phi_1,...,phi_D`.  The `D` by `M` matrix

```text
A_all=(cos(k phi_j))_(j<=D,k in K)                     (3.5)
```

has column rank `M`.  Therefore one can choose `M` of the roots so that the
corresponding square matrix is invertible.  For that phase vector,

```text
sum_(k in K)w_k a_k(theta)=-r q_0.                    (3.6)
```

It is a strict positive antipode, unique on the prescribed support `K`, and
strict positivity persists throughout an open phase neighborhood (with the
normalized weights and depth varying continuously from `w` and `r`).

#### Proof

At the endpoints of the cells (3.4),

```text
G(j*pi/D)=(-1)^j w_D
          +r+sum_(k<D)w_k cos(kj*pi/D).                (3.7)
```

The absolute value of the second line is at most

```text
r+sum_(k<D)w_k=r+1-w_D<w_D.                            (3.8)
```

Thus the signs in (3.7) alternate strictly.  Every cell contains a root.
But `G(theta)=g(cos theta)` for a real algebraic polynomial `g` of degree
`D`; it has at most `D` roots in `(0,pi)`, counted with multiplicity.  The
`D` roots already found are consequently the only roots and are all simple.

Suppose a cosine polynomial supported on `K`,

```text
Q(theta)=sum_(k in K)b_k cos(k theta),                 (3.9)
```

vanished at all `D` roots.  As polynomials in `x=cos theta`, `Q=lambda G`
because both have degree at most `D` and share `D` distinct roots.  The
constant Chebyshev coefficient of `Q` is zero, whereas that of `G` is
`r>0`; hence `lambda=0`.  This proves full column rank in (3.5).  Selecting
an invertible minor gives (3.6).

At that minor,

```text
A^(-1)q_0=-w/r<0.                                     (3.10)
```

Invertibility and all strict signs persist under small phase perturbations,
which proves the open-chamber assertion.  QED

### Corollary 3.2 (universal optimally sparse chambers)

For every `K` in (3.1) and every `0<r<1`, weights satisfying (3.2) exist.  If
`M>1`, one explicit choice is

```text
w_D=(3+r)/4,
w_k=(1-w_D)/(M-1),              k<D.                  (3.11)
```

For `M=1`, take `w_D=1`.  Hence every prescribed support, including every
arbitrarily remote or lacunary support, has a phase point of exact depth `r`
in an open strict-positive chamber.  This does not assert that the entire
open chamber is an exact-depth level set.

By Theorem 2.2, the conull residual part of that open chamber has global
minimum exact sparsity `M`, even when competing supports may use arbitrary
positive integer harmonics.  Thus the upper bound in Theorem 2.1 is sharp.

For example, every translated block

```text
K={L,L+1,...,L+M-1}                                  (3.12)
```

supports a depth-`1/2` chamber uniformly in both `L` and `M`; the entire
support may be moved arbitrarily far from the origin.  Here "uniformly" refers
to the attained depth and the explicit weight rule, not to a phase-neighborhood
radius independent of `L` or `M`.

### Corollary 3.3 (sparse palindromic unimodular-root polynomial)

Under Theorem 3.1, define

```text
P(z)=z^(2D)+1+(2r/w_D)z^D
     +sum_(k in K,k<D)(w_k/w_D)(z^(D+k)+z^(D-k)).      (3.13)
```

Then `P` has positive coefficients exactly on the prescribed symmetric
support

```text
{0,2D,D} union {D-k,D+k:k in K,k<D},                  (3.14)
```

is palindromic, and has `2D` distinct roots, all on the unit circle.  More
precisely, its roots are `exp(+-i phi_j)` for the roots in (3.4).

#### Exact normalization and simplicity check

For `z=exp(i theta)`,

```text
P(z)=(2/w_D)z^D G(theta).                             (3.15)
```

Theorem 3.1 supplies `D` distinct simple roots in `(0,pi)`, so (3.15)
supplies the `2D` distinct roots `exp(+-i phi_j)`.  This exhausts the degree.
Differentiating (3.15) at a root shows `P'` is nonzero because `G'` is
nonzero, so all roots are simple.

Moreover,

```text
1 > (r+1-w_D)/w_D
  = (1/2)sum_(ell=1)^(2D-1)|[z^ell]P(z)|,              (3.16)
```

which is precisely the strict Lakatos--Losonczi dominance condition.  Thus
the root-location corollary is independently covered by their 2004 theorem.

---

## 4. Exact classification on `{1,...,M}`

The universal existence theorem does not by itself classify a given phase
vector.  Consecutive frequencies admit a complete answer.

Let the phases be distinct and put

```text
x_j=cos(theta_j),
R(x)=product_(j=1)^M(x-x_j)=sum_(k=0)^M r_k T_k(x),    (4.1)
```

where `T_k(cos theta)=cos(k theta)`.  Since `R` is monic,

```text
r_M=2^(1-M)>0.                                        (4.2)
```

### Theorem 4.1 (Chebyshev-sign if-and-only-if theorem)

For the support `K={1,...,M}`:

1. if `r_0=0`, the constant carrier is not in the span of the `M` cosine
   atoms;
2. if `r_0!=0`, its unique signed representation is

   ```text
   q_0=sum_(k=1)^M c_k a_k(theta),
   c_k=-r_k/r_0;                                      (4.3)
   ```

3. a nonnegative positive antipode exists if and only if

   ```text
   r_0>0,            r_k>=0 for every 1<=k<=M;         (4.4)
   ```

4. it is strict if and only if every coefficient in (4.4) is strictly
   positive, and then

   ```text
   w_k=r_k/sum_(ell=1)^M r_ell,
   r=r_0/sum_(ell=1)^M r_ell
    =r_0/[R(1)-r_0].                                  (4.5)
   ```

Thus `r_0=0` is an infeasible singular stratum, while `r_k=0` for `k>=1`
is exactly a support-dropping boundary stratum.

#### Proof

Any degree-at-most-`M` polynomial vanishing at all `x_j` is a multiple of
`R`.  If `r_0=0`, then `R` itself is a nontrivial dependence among
`T_1,...,T_M`.  Were a no-constant polynomial `Q` equal to one at every
`x_j`, then `Q-1=lambda R`; comparison of `T_0` coefficients gives
`-1=0`, a contradiction.

If `r_0!=0`, write the interpolant as `Q-1=lambda R`.  Its zero `T_0`
coefficient forces `lambda=-1/r_0`, proving (4.3) and uniqueness.  A positive
antipode is equivalent to every `c_k<=0`.  Because `r_M>0`, these signs force
`r_0>0`, and they are then exactly (4.4).  Normalizing the coefficients gives
(4.5).  QED

The theorem is directional: an ordinary Vandermonde or Gram determinant
detects invertibility but does not determine the signs in (4.4).

---

## 5. Literature boundary

The following division between classical ingredients and the present
synthesis is essential.

### Classical or directly subsumed components

* **Boundary compression.**  Caratheodory's theorem and the supporting-face
  argument give the `M`-atom upper bound.  Elfving's theorem places
  directional optimal design on the boundary of a symmetric regression
  hull: G. Elfving,
  [*Optimum Allocation in Linear Regression Theory*](https://doi.org/10.1214/aoms/1177729442),
  *Ann. Math. Statist.* 23 (1952), 255--262.

* **Unimodular roots under endpoint dominance.**  The inequality (3.16) is
  exactly within P. Lakatos and L. Losonczi,
  [*Self-inversive polynomials whose zeros are on the unit circle*](https://publi.math.unideb.hu/paper/985),
  *Publ. Math. Debrecen* 65 (2004), 409--420,
  [DOI 10.5486/PMD.2004.3250](https://doi.org/10.5486/PMD.2004.3250).
  Their theorem already gives unimodularity, simplicity under strict
  inequality, and angular localization.  Lalin--Smyth later generalized
  Cohn-type criteria:
  [*Unimodularity of zeros of self-inversive polynomials*](https://arxiv.org/abs/1201.0774).

* **Special positive-coefficient families.**  A. Dubickas,
  [*Some Polynomials with Unimodular Roots*](https://epublications.vu.lt/object/elaba%3A141849052/MAIN),
  *Bull. Korean Math. Soc.* 59 (2022), 1269--1277,
  [DOI 10.4134/BKMS.b210728](https://doi.org/10.4134/BKMS.b210728),
  proves recursive positive self-reciprocal families whose roots are all
  unimodular and whose arguments become equidistributed.  This reinforces
  that coefficient positivity does not prohibit a full unit-circle root
  pattern.

* **Trigonometric optimal design and orbitopes.**  Dette--Melas study
  coefficient-specific optimal designs for fixed Fourier regression models:
  H. Dette and V. Melas,
  [*Optimal Designs for Estimating Individual Coefficients in Fourier Regression Models*](https://doi.org/10.1214/aos/1065705122),
  *Ann. Statist.* 31 (2003), 1669--1692.  Sanyal--Sottile--Sturmfels study
  convex hulls of trigonometric moment curves and their facial geometry:
  [*Orbitopes*](https://arxiv.org/abs/0911.5436).

### What the surveyed sources did not state

No surveyed primary source states the following combined transposed theorem:

```text
every prescribed integer harmonic support K
  -> for every r<1, an exact depth-r point inside an open positive chamber
  -> exactly one root in each explicit top-frequency cell
  -> a full-column-rank root table
  -> generic global minimum sparsity exactly M
  -> unique deepest optimizer for every finite pool,
```

together with the exact Chebyshev coefficient classification (4.4)--(4.5).
The individual tools are elementary or classical, and the palindromic root
corollary is explicitly prior art.  The safe claim is therefore a potentially
new synthesis and transposed application, not a priority claim.

### Why the fixed-gap cyclotomic candidate is not the headline

For prime `q`, let `zeta_q` be primitive and let integer residue counts be
`A_0,...,A_(q-1)`.  The exact implication

```text
sum_r A_r zeta_q^r=0
iff A_0=A_1=...=A_(q-1)                               (5.1)
```

follows immediately from the irreducibility of
`Phi_q(x)=1+x+...+x^(q-1)`.  If two locally forbidden fixed-gap classes have
count zero, the only vanishing vector is the zero vector.  The algebraic norm
also gives, for total mass `N=sum A_r`,

```text
0<|sum_r A_r zeta_q^r| >= N^(-(q-2)).                 (5.2)
```

This is an exact energy-level/nonvanishing theorem, but (5.1) is classical
cyclotomic algebra and (5.2) is exponentially weak in `q`.  It supplies no
power saving for FGF4.  Its prior-art risk is therefore much higher and its
standalone analytic significance much lower than Theorems 2.2--4.1.  It is a
useful lemma, not the recommended headline theorem.

---

## 6. Exact disposition

```text
depth-preserving compression to <=M atoms:          PROVED;
generic square full spark:                           PROVED;
generic affine full spark:                           PROVED;
generic no representation with <M harmonics:         PROVED;
generic unique deepest finite-pool antipode:          PROVED;
arbitrary prescribed support K:                      PROVED;
every prescribed depth 0<r<1:                        PROVED;
one simple root in every top-frequency cell:         PROVED;
root-table full column rank:                          PROVED;
open strict positive chamber:                        PROVED;
sparse palindromic simple unimodular roots:           PROVED / CLASSICAL ROOT LEMMA;
consecutive Chebyshev sign iff:                       PROVED;
actual prime-log return before the QP aperture:       OPEN;
QP promotion or zero-free strip:                      NOT PROVED.
```

## 7. Replay

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_sparse_cosine_antipode_classification.py
python3 results/verify_sparse_cosine_antipode_classification.py
python3 src/sparse_cosine_antipode_classification.py
```

The current replay is `6 passed`; the independent verifier prints `PASS`.
