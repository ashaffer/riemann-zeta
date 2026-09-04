# Sharp sparse positive-cosine antipodes

## A finite-dimensional classification theorem

**Date:** 2026-08-14  
**Status:** proved, independently hostile-audited, and replayed

This note isolates a theorem that arose from the prime-log interpolation
problem but is independent of zeta.  In an `M`-coordinate cosine dictionary,
`M` is the exact sparse scale for deepest positive representations of the
negative constant direction:

1. every feasible representation can be compressed, without losing depth,
   to at most `M` atoms;
2. away from explicit analytic determinant varieties, the deepest
   representation is unique and has exactly `M` positive atoms;
3. conversely, for every prescribed set of `M` positive integer harmonics,
   however remote or lacunary, and every `0<r<1`, there is an exact depth-`r`
   point lying inside an open strict-positive chamber;
4. for consecutive harmonics, feasibility is classified exactly by the
   signs of the Chebyshev coefficients of the nodal polynomial.

The theorem classifies the finite geometry.  It does not prove that the
specific prime-log orbit enters one of the chambers inside the available
aperture, and therefore has no zero-free-strip consequence by itself.

---

## 1. Setup

For `theta=(theta_1,...,theta_M) in (0,pi)^M`, define

```text
a_k(theta)=(cos(k theta_1),...,cos(k theta_M)),
q_0=(1,...,1).
```

Given a finite harmonic pool `H`, a positive antipode of depth `r>0` is

```text
sum_(k in H) w_k a_k(theta)=-r q_0,
w_k>=0,                    sum_(k in H)w_k=1.          (1.1)
```

Its sparsity is the number of nonzero weights.  The word *deepest* means that
`r` is maximal for the fixed phase vector and harmonic pool.

---

## 2. Main classification

### Theorem A (sharp compression)

If (1.1) is feasible at depth `r_0`, then it is feasible at some depth
`r_*>=r_0` using at most `M` harmonics.

Indeed, maximize `r` along the ray `-r q_0` inside

```text
conv{a_k(theta):k in H}.
```

The terminal point lies on a proper face.  Caratheodory's theorem in that
face uses at most `M` vertices, improving the ambient `M+1` bound by one.

### Theorem B (generic necessity and uniqueness)

There is a conull residual set `G_M subset (0,pi)^M` such that, for every
`theta in G_M`:

- every `M`-column cosine minor is nonsingular;
- every `M+1` cosine atoms are affinely independent;
- `q_0` is not in the span of fewer than `M` atoms.

Consequently, for every finite pool with at least `M` harmonics, any deepest
positive antipode that exists is unique and has exactly `M` strictly positive
weights.  The statement holds simultaneously for all finite integer
harmonic supports.

The determinant certificate is explicit.  For distinct positive `u_j` and
distinct nonnegative `k_l`,

```text
det(cos(tau u_j k_l))
 = (-1)^[m(m-1)/2] tau^[m(m-1)]
   * product_(i<j)(u_j^2-u_i^2)
   * product_(l<s)(k_s^2-k_l^2)
   / product_(n=0)^(m-1)(2n)!
   +O(tau^[m(m-1)+2]).                                (2.1)
```

Thus each forbidden minor is a nonzero real-analytic function.  Its zero set
is null and nowhere dense; a countable union covers every integer support.
For a fixed finite pool along a one-parameter dilation, the exceptional set
is locally finite.

### Theorem C (every support and every subunit depth occurs)

Let

```text
K={k_1<...<k_M},                 D=k_M,
0<r<1.
```

Choose positive weights with sum one and

```text
w_D>(1+r)/2.                                           (2.2)
```

Then

```text
G(phi)=r+sum_(k in K)w_k cos(k phi)                    (2.3)
```

has exactly one simple root in every interval

```text
(j*pi/D,(j+1)*pi/D),                0<=j<D.            (2.4)
```

At the cell endpoints the top harmonic alternates by `+/-w_D`, while the
remaining terms have total modulus at most `r+1-w_D<w_D`.  Hence all `D`
cells contain roots.  Since (2.3) is a degree-`D` polynomial in `cos(phi)`,
these are all its roots and all are simple.

The `D by M` root-frequency table

```text
(cos(k phi_j))_(j<=D,k in K)
```

has column rank `M`.  Otherwise a nonzero `K`-supported cosine polynomial
would vanish at every root and hence be proportional to `G`, which is
impossible because it has no constant term whereas `G` has constant term
`r`.  Selecting an invertible `M`-row minor gives

```text
sum_(k in K)w_k a_k(theta)=-r q_0.                    (2.5)
```

All weights are strict, and invertibility plus the sign pattern persist on
an open phase neighborhood.  The normalized weights and depth generally vary
inside that neighborhood; only its distinguished center is asserted to have
the prescribed exact depth `r`.  One explicit choice for `M>1` is

```text
w_D=(3+r)/4,
w_k=(1-w_D)/(M-1),                 k<D.
```

Thus every remote or lacunary `M`-set supports an open depth-`r` chamber.
Intersecting that chamber with the generic set in Theorem B proves that the
bound `M` in Theorem A is sharp.

---

## 3. Exact sign classification for consecutive harmonics

Let `K={1,...,M}`, put `x_j=cos(theta_j)`, and expand the nodal polynomial in
the Chebyshev basis:

```text
R(x)=product_(j=1)^M(x-x_j)=sum_(k=0)^M r_k T_k(x),
r_M=2^(1-M)>0.                                         (3.1)
```

Then:

- if `r_0=0`, the constant carrier is not in the span of the `M` atoms;
- if `r_0!=0`, its unique signed representation is

  ```text
  q_0=sum_(k=1)^M (-r_k/r_0)a_k(theta);
  ```

- a positive antipode exists exactly when

  ```text
  r_0>0 and r_k>=0 for every 1<=k<=M;                 (3.2)
  ```

- it is strict exactly when all inequalities are strict, in which case

  ```text
  w_k=r_k/sum_(l=1)^M r_l,
  r=r_0/sum_(l=1)^M r_l=r_0/[R(1)-r_0].              (3.3)
  ```

Hence `r_0=0` is the infeasible singular stratum, while `r_k=0`, `k>=1`, is
precisely a support-dropping boundary stratum.

---

## 4. Signed TV and stability

For distinct positive nodes `u_j`, a finite pool `H`, and any regular
dilation `tau`, put

```text
A_H(tau)=[cos(k tau u_j)]_(j,k),
C_TV=min{||c||_1:A_Hc=q_0}.
```

For each `M`-subset `K subset H`, let `c^K=A_K^(-1)q_0`.  Then

```text
C_TV=min_(|K|=M)||c^K||_1.                            (4.1)
```

Every extreme minimizer has exactly `M` atoms.  If

```text
y_K=A_K^(-T)sign(c^K),
```

then `c^K` is optimal exactly when

```text
|a_l^T y_K|<=1                  for all l outside K,  (4.2)
```

and is unique exactly when every inequality is strict.  The strict dual
slack also gives a quantitative concentration estimate for every
near-minimizer.  The positive problem has the analogous hostile-sign Cramer
classification and dual certificate; the complete formulas and proofs are
in the theorem report linked below.

---

## 5. Palindromic corollary and prior art

The construction in Theorem C yields

```text
P(z)=z^(2D)+1+(2r/w_D)z^D
     +sum_(k<D)(w_k/w_D)(z^(D+k)+z^(D-k)),             (5.1)
```

with the sum restricted to `k in K`.  It has positive coefficients on the
prescribed symmetric support and all `2D` roots are simple and unimodular.
This root-location consequence is covered by the strict coefficient-
dominance theorem of Lakatos and Losonczi; it is not claimed as new.

The ingredients divide as follows.

- The boundary compression is classical Caratheodory/Elfving geometry.
- Full-spark terminology and generic-minor methods are classical.
- Dominant-coefficient unimodular-root criteria are classical.
- The potentially new part is the combined *transposed* synthesis:
  prescribed arbitrary support and depth, explicit root cells, full-rank
  root table, generic sharp sparsity and unique finite-pool optimization,
  together with the exact Chebyshev sign strata.  No broad priority claim is
  made without a wider expert review.

Primary comparisons are [Elfving's directional-design theorem](https://doi.org/10.1214/aoms/1177729442),
[Lakatos and Losonczi's self-inversive root theorem](https://doi.org/10.5486/PMD.2004.3250),
and the [modern full-spark framework](https://arxiv.org/abs/1110.3548).

---

## 6. Exact scope and replay

The theorem proves that sparse exact positive representations have a rigid
generic classification, while also proving that every prescribed remote
support has genuine open positive chambers.  For harmonic-AP supports, the
unresolved issue is finite-aperture first return.  That is only one sufficient
QP subroute: the full optimizer may choose `M` arbitrary incommensurable
atoms.  Spectral-null/Delsarte duality identifies the full remaining scalar
as the one-sided actual-node value `A_H`, with optimal depth
`r_+=1/(A_H-1)`.  Thus finite-dimensional existence and sparsity are closed,
while deterministic actual-prime control of `A_H` remains open.

Full proofs and the stronger finite-pool TV/stability classification:

- [`ZETA23-SHARP-SPARSE-POSITIVE-COSINE-ANTIPODE-CLASSIFICATION-2026-08-14.md`](../results/ZETA23-SHARP-SPARSE-POSITIVE-COSINE-ANTIPODE-CLASSIFICATION-2026-08-14.md)
- [`ZETA23-QP-SPARSE-TV-CLASSIFICATION-THEOREM-2026-08-14.md`](../results/ZETA23-QP-SPARSE-TV-CLASSIFICATION-THEOREM-2026-08-14.md)
- [`ZETA23-QP-SPECTRAL-NULL-DELSARTE-AND-GROUPING-GATE-2026-08-14.md`](../results/ZETA23-QP-SPECTRAL-NULL-DELSARTE-AND-GROUPING-GATE-2026-08-14.md)

Replay:

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_sparse_cosine_antipode_classification.py \
  src/test_qp_sparse_tv_classification.py
python3 results/verify_sparse_cosine_antipode_classification.py
python3 results/verify_zeta23_qp_sparse_tv_classification.py
```

The replay checks the root cells, rank selection, antipode identities,
Chebyshev signs, determinant asymptotics, LP dual signs, uniqueness, and
stability inequalities.
