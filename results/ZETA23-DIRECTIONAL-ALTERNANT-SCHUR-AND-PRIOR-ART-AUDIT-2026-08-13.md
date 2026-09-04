# Directional alternant, Schur, and prior-art audit

**Date:** 2026-08-13
**Verdict:** **the principal atomic problem has a sharper `M`-atom Elfving
reduction and an exact directional-minor formula, but neither alternation nor
ordinary Vandermonde conditioning controls that formula.  No bound deciding
`E_B` at the strip exponent is proved.**

There are three exact conclusions.

1. After quotienting duplicate absolute cosine nodes, the principal
   representation cost is a classical `c`-optimal/Elfving gauge in its
   effective dimension `M`.  An optimal signed measure exists with at most
   `M` atoms, not merely `M+1`.  The `M+1` count in the Chebyshev--Wiener
   design report concerns a different zero-barycenter residual design and
   remains correct there.
2. On an `M`-atom support, the cost is exactly the sum of the absolute
   **carrier-replacement minors** divided by the ordinary determinant.  This
   is the requested directional reduction.  A large unaugmented determinant
   alone says nothing about it.
3. On a legal arithmetic progression of high times, the common Vandermonde
   factor cancels from Cramer's rule.  One carrier coefficient is exactly a
   high-degree complete homogeneous Schur polynomial in the prime phases.
   That factor can vanish for distinct unit-circle nodes.  At the legal
   aperture its degree is at least `Y^(.235848...+o(1))`.

The actual cosine kernel also fails strict sign regularity already in order
two on the high band.  Thus the support reduction cannot be upgraded to an
ordered alternation theorem by Haar, total-positivity, or local-Haar theory.

The literature audit below finds exact names for the support/design/frame
parts of the problem.  It finds no deterministic theorem giving a
`sqrt(log(B/M)/M)` law for the actual prime-log curve.  That scale occurs in
independent-entry random-polytope geometry; the hypotheses do not hold here.

---

## 1. Setup and orientation

Use

```text
N_Y={p^k:Y*exp(-w)<=p^k<=Y*exp(w)},
u_n=log(n/Y),
a_raw(t)=(cos(t*u_n))_(n in N_Y),
q_raw=a_raw(0)=(1,...,1),
M_raw=#N_Y=Y^(1-o(1)),
H=[T,B],       T=Y^.751,       B=Y^(50/33).             (1.1)
```

There is one necessary finite-dimensional quotient.  Declare

```text
n~m  iff  |u_n|=|u_m|,
{v_1,...,v_M}={|u_n|:n in N_Y},       v_j distinct,
a(t)=(cos(t*v_j))_(j=1)^M,            q_0=(1,...,1).    (1.1a)
```

The original interpolation equation is equivalent to the reduced one,
coordinate by coordinate, and its TV cost is unchanged: coordinates in the
same class are identical functions and have the same target value `1`.
Distinct absolute nodes can fail only through

```text
|log(n/Y)|=|log(m/Y)|,       n!=m  =>  n*m=Y^2.         (1.1b)
```

If `Y^2` is not an integer there are no such pairs; otherwise their number is
at most the divisor count of `Y^2`, hence `Y^o(1)`.  Thus

```text
0<=M_raw-M<=Y^o(1),       M=Y^(1-o(1)).                 (1.1c)
```

All dimensions and matrices below use this effective `M` and reduced curve.
The possible node `v_j=0` causes no problem.

### Lemma 1.1 (full span after the absolute-node quotient)

For every nonempty open interval `J`,

```text
span_R{a(t):t in J}=R^M.                                (1.1d)
```

#### Proof

If `c` annihilates every `a(t)` on `J`, the entire function

```text
f(t)=sum_j c_j cos(t*v_j)
```

vanishes identically.  Its derivatives of orders `0,2,...,2(M-1)` at zero
give

```text
sum_j c_j (v_j^2)^k=0,       0<=k<=M-1.
```

The numbers `v_j^2` are distinct, so the Vandermonde system gives `c=0`.
QED.

The principal real atomic cost is

```text
C_*(q_0;H)
 =inf{||mu||_TV: integral_H a(t)dmu(t)=q_0}.            (1.2)
```

The companion atomic report proved the exact directional Christoffel
identity

```text
C_*^2
 =inf_(rho in Prob(H), q_0 in Ran G_rho)
    q_0^T G_rho^dagger q_0,
G_rho=integral_H a(t)a(t)^T d rho(t).                   (1.3)
```

The issue is therefore directional: how far `q_0` is from the ranges built
by legal high-time atoms, with the correct coefficient norm.  Average rank,
an unaugmented determinant, or a common singular-value bound does not answer
it.

---

## 2. The sharp Elfving-face reduction

### Theorem 2.1 (`M` atoms suffice for the principal cost)

Suppose a compact set `A subset R^M` spans `R^M`, and let

```text
gamma_A(q)=inf{||mu||_TV: integral_A x dmu(x)=q},
q!=0.                                                   (2.1)
```

Then an optimal measure exists and one exists with at most `M` atoms.
Applied to the reduced `A={a(t):t in H}`, which spans by Lemma 1.1, this
gives

```text
q_0=sum_(i=1)^r c_i a(t_i),
sum_i |c_i|=C_*(q_0;H),
r<=M.                                                   (2.2)
```

Moreover the polar design

```text
rho=sum_i (|c_i|/C_*) delta_(t_i)                       (2.3)
```

is an optimizer in (1.3).  Thus the directional Christoffel infimum also
has an optimal design with at most `M` support points.

#### Proof

Put

```text
K=conv(A union -A).                                     (2.4)
```

Then `gamma_A` is the gauge of the compact centrally symmetric body `K`.
Since `A` spans, `K` has interior.  The point

```text
x_*=q/gamma_A(q)                                        (2.5)
```

lies on `partial K`; otherwise the ray through `q` could be extended inside
`K`, lowering the gauge.  Choose a supporting hyperplane and let `F` be the
exposed face containing `x_*`.  Its affine dimension is at most `M-1`.
Every representing convex combination of `x_*` uses, after deleting points
off the supporting hyperplane, signed atoms from

```text
F intersect (A union -A).
```

Caratheodory in `aff(F)` uses at most `M` such atoms.  Rescaling their convex
weights by `gamma_A(q)` proves (2.2).  The atoms can be chosen affinely
independent in the supporting hyperplane.  Since that hyperplane does not
contain zero, they are also linearly independent.

For (2.3), polarization gives leverage at most `C_*^2`.  If it were strictly
smaller, the canonical `L^2(rho)` density in (1.3), followed by
Cauchy--Schwarz, would give a representation of TV strictly below `C_*`.
Hence equality holds.  QED.

### Why this does not contradict the `M+1` design support

The continuous Chebyshev--Wiener saddle has a signed zero-barycenter
condition

```text
sum_l w_l s_l a(t_l)=0,       sum_l w_l=1.             (2.6)
```

Zero need not lie on a proper exposed face of
`conv{+-a(t)}`.  Ordinary Caratheodory in `R^M` therefore gives `M+1`, and
that bound is generically sharp.  In (2.2), by contrast, minimality puts the
nonzero radial boundary point `q_0/C_*` on a proper exposed face, saving one
atom.  Conflating the two convex programs obscures this distinction.

### Corollary 2.2 (exact carrier-replacement-minor formula)

For `t=(t_1,...,t_M)` let

```text
A(t)=[a(t_1) ... a(t_M)],
A_i(t;q_0)=A(t) with column i replaced by q_0.          (2.7)
```

Then

```text
C_*(q_0;H)
 =min_(t in H^M, det A(t)!=0)
   sum_(i=1)^M |det A_i(t;q_0)|/|det A(t)|.            (2.8)
```

#### Proof

Every nonsingular configuration represents `q_0` uniquely, and Cramer's
rule gives the displayed cost.  Conversely, take the support in Theorem
2.1 with the linear independence supplied by its proof, then extend those
support columns to a basis using atoms from `A`.  The new coefficients are
zero, so the same optimal cost occurs in (2.8).  QED.

Formula (2.8) is the finite directional theorem that an unaugmented-volume
argument misses.  It asks for the ratios of all carrier-replacement minors,
not the size of `det A` by itself.

---

## 3. Ordered alternation fails on the actual prime nodes

### Theorem 3.1 (failure of order-two strict sign regularity)

For all sufficiently large `Y`, there are actual prime coordinates `p,q` in
the shell with

```text
0<c_w<=u_p<u_q<=w-c_w,
u_q-u_p>=c_w.                                           (3.1)
```

For these coordinates the carrier-augmented order-two minor is

```text
D_(p,q)(t)
 =det [[1,cos(t*u_p)],[1,cos(t*u_q)]]
 =cos(t*u_q)-cos(t*u_p)
 =-2 sin(t*(u_p+u_q)/2) sin(t*(u_q-u_p)/2).            (3.2)
```

It has `asymp_w B` zeros in `H` and does not have a fixed strict sign there.
Consequently:

* `{1,cos(tu_p),cos(tu_q),...}` is not a Haar/Chebyshev system on `H`;
* the kernel `(u,t) -> cos(ut)`, even after adjoining the carrier row at
  `t=0`, is not strictly sign regular on the legal band;
* the optimal support signs in Theorem 2.1 or in the `M+1` residual design
  need not alternate in the order of the times.

#### Proof

The prime number theorem supplies primes in two fixed disjoint
multiplicative subwindows above `Y`, proving (3.1).  The first family of
zeros

```text
t=2*pi*k/(u_q-u_p)                                     (3.3)
```

already contributes `asymp_w B` points in `H`.  Equation (3.2) also gives
simple sign-changing zeros from one of its two sine grids.  A nonzero
function in a two-dimensional subspace therefore has far more than one
zero, and a strict order-two minor vanishes repeatedly.  QED.

Any interval on which this particular order-two minor can retain a strict
sign has length `O_w(1)`.  By contrast, an `M`- or `M+1`-point support spread
over the full band has average gap

```text
B/M=Y^(17/33+o(1))*log Y.                              (3.4)
```

Thus partitioning into local-Haar cells gives no coupling between typical
successive extreme points.  This is an exact obstruction to the proposed
global alternant proof, not merely a numerical lack of alternation.

---

## 4. Arithmetic-progression supports expose the missing Schur factor

It is useful first to complexify the curve:

```text
v^C(t)=(exp(i*t*v_j))_(j=1)^M.                         (4.1)
```

This does not replace the real problem; Section 4.3 records the real-cosine
counterpart.  The complex form makes the directional factor completely
explicit.

### 4.1 A legal high block

Choose any

```text
Delta in [(B-T)/(2M),(B-T)/M],       N=ceil(T/Delta),
tau_r=(N+r)Delta,           0<=r<=M-1.                 (4.2)
```

outside the finite resonance set in this bounded interval on which
`Delta*(v_j-v_k)` or `Delta*(v_j+v_k)` is an integer multiple of `2*pi`
for some `j!=k`.

For large `Y`, every `tau_r` lies in `[T,B]`, and

```text
Delta=Y^(17/33+o(1)),
N=Y^(.751-17/33+o(1))
 =Y^(7783/33000+o(1))
 =Y^(.23584848...+o(1)).                               (4.3)
```

Put

```text
z_j=exp(i*Delta*v_j).                                  (4.4)
```

The phases `z_j`, and also the cosine nodes `cos(Delta*v_j)`, are distinct by
the choice of `Delta`.  Such a choice always exists because each nonzero sum
or difference contributes only finitely many resonant values in the compact
interval in (4.2).  Also
`N*Delta>=T` and
`(N+M-1)Delta<T+M*Delta<=B`, so the entire block is legal.

### Theorem 4.1 (carrier-augmented Schur factorization)

For distinct nonzero complex numbers `z_1,...,z_M`,

```text
det [1,z_j^N,z_j^(N+1),...,z_j^(N+M-2)]_(j=1)^M

 =V(z)*(prod_j z_j)^(N-1)*h_(N-1)(z_1^(-1),...,z_M^(-1)),       (4.5)
```

where

```text
V(z)=prod_(i<j)(z_j-z_i)                               (4.6)
```

and `h_k` is the complete homogeneous symmetric polynomial of degree `k`.

#### Proof

The exponent set is

```text
0,N,N+1,...,N+M-2.                                    (4.7)
```

The generalized alternant formula factors its determinant as `V(z)` times
the Schur polynomial for the partition

```text
lambda=((N-1) repeated M-1 times,0).                   (4.8)
```

Complementing this partition in the `(N-1) by M` rectangle gives

```text
s_lambda(z)=(prod_j z_j)^(N-1) h_(N-1)(z^(-1)),        (4.9)
```

which proves (4.5).  QED.

### Corollary 4.2 (Vandermonde cancellation in Cramer's rule)

Let

```text
V_AP=[v^C(N*Delta),v^C((N+1)*Delta),...,
      v^C((N+M-1)*Delta)].                             (4.10)
```

The coefficient `c_(M-1)` in the unique representation

```text
V_AP*c=q_0                                             (4.11)
```

is

```text
c_(M-1)
 =(-1)^(M-1)*(prod_j z_j)^(-1)
   h_(N-1)(z_1^(-1),...,z_M^(-1)).                    (4.12)
```

#### Proof

The ordinary high-block determinant is

```text
det V_AP=(prod_j z_j)^N V(z).                          (4.13)
```

Replacing its last column by `q_0` and moving that column to the front gives
`(-1)^(M-1)` times (4.5).  Divide by (4.13).  QED.

Thus the ordinary Vandermonde cancels **exactly** from this directional
coefficient.  Separation-based lower singular-value estimates do not touch
the remaining quantity.

The obstruction is real, not an artifact of possible repeated nodes.  For
`M=2`, if `z_2/z_1` is a nontrivial `N`th root of unity, then

```text
h_(N-1)(z_1^(-1),z_2^(-1))=0                          (4.14)
```

although `z_1!=z_2` and `V(z)!=0`.  Such ratios can have angular separation
`2*pi/N`, so even fine deterministic spacing does not give a uniform lower
bound for the directional factor.  This is a countermodel to a
Vandermonde-only theorem; it is not a claim that the actual prime phases
satisfy (4.14).

### 4.3 Exact real-cosine form

Put

```text
x_j=cos(Delta*v_j)
```

and let `T_k` denote the Chebyshev polynomial.  Alternation of a determinant
in the `x_j` gives the exact factorization

```text
det[1,T_N(x_j),T_(N+1)(x_j),...,T_(N+M-2)(x_j)]
 =V(x)*Psi_(N,M)(x),                                   (4.15)
```

where `Psi_(N,M)` is a symmetric polynomial of total degree

```text
(M-1)(N-1).                                            (4.16)
```

It is the real orthogonal-character analogue of the Schur factor in (4.5).
Already for `M=2`,

```text
Psi_(N,2)(x_1,x_2)
 =[T_N(x_2)-T_N(x_1)]/(x_2-x_1),                      (4.17)
```

which has zeros with `x_1!=x_2`.  Therefore the directional-factor issue
persists in the exact real cosine geometry.

### 4.4 Arithmetic meaning and limitation

At the legal aperture, (4.3) turns the missing factor into a symmetric
prime-phase sum of growing degree at least

```text
N-1=Y^(.235848...+o(1)).                               (4.18)
```

Explicitly,

```text
h_(N-1)(z^(-1))
 =sum_(k_1+...+k_M=N-1)
   exp(-i*Delta*sum_j k_j*v_j).                        (4.19)
```

This is an arithmetic target involving products of `N-1` shell nodes.  It
is far beyond every fixed-moment conductor available in the current proof
packet.  Qualitative nonlattice information only says that certain exact
equalities are absent; it supplies no lower bound for (4.19).

This AP theorem does **not** decide the global cost.  To lower-bound `C_*`
one must control all legal configurations in (2.8), not one AP.  To build a
cheap AP representation one must control all Cramer coefficients, not only
(4.12).  Its value is diagnostic and exact: it identifies the missing
directional arithmetic invariant and proves that ordinary Vandermonde
conditioning cannot replace it.

---

## 5. Primary-source prior-art audit

The scope column is deliberately narrow.  A paper is not counted as solving
the present problem merely because its vocabulary contains “optimal design,”
“Christoffel,” “frame,” or “prolate.”

| Primary source | Exact theorem scope | Consequence here |
|---|---|---|
| Gustav Elfving, [*Optimum Allocation in Linear Regression Theory*](https://doi.org/10.1214/aoms/1177729442), Ann. Math. Stat. 23 (1952), 255–262 | Geometric characterization of `c`-optimal linear-regression designs by the boundary of the symmetric convex hull now called the Elfving set. | This is the classical home of Theorem 2.1.  Exposed-face Caratheodory gives at most `M` atoms for the principal directional cost.  It gives no ordered signs or arithmetic lower bound. |
| J. Kiefer and J. Wolfowitz, [*The Equivalence of Two Extremum Problems*](https://doi.org/10.4153/CJM-1960-030-4), Canad. J. Math. 12 (1960), 363–366 | For a compact real regression range, maximizing the information determinant is equivalent to minimizing the maximum variance `f(x)^T M(xi)^(-1)f(x)`; the optimum maximum is the parameter dimension. | This is the `D`/`G` equivalence and the standard nondirectional Christoffel/variance function.  It does not provide the carrier-specific infimum (1.3) or a `q_0` angle. |
| W. J. Studden, [*Elfving's Theorem Revisited*](https://doi.org/10.1016/j.jspi.2003.05.004), J. Statist. Plann. Inference 130 (2005), 85–94 | Shows explicitly that Elfving's theorem is equivalent to a special approximation theorem and develops related Elfving-type statements. | Confirms that the design and minimax formulations are established prior art.  The arithmetic estimate remains separate. |
| Charles B. Dunham, [*Chebyshev Approximation with the Local Haar Condition*](https://doi.org/10.1137/0708068), SIAM J. Numer. Anal. 8 (1971), 749–753 | Gives a local-best criterion and an alternation theorem on an interval under a local Haar condition. | The hypothesis fails globally by Theorem 3.1.  Local cells cannot be stitched across gaps of size (3.4). |
| H. Dette and V. B. Melas, [*Optimal Designs for Estimating Individual Coefficients in Fourier Regression Models*](https://doi.org/10.1214/aos/1065705122), Ann. Statist. 31 (2003), 1669–1692 | Solves many `c`-optimal design problems for individual coefficients in the classical integer-harmonic trigonometric model on a fixed symmetric arc `[-a,a]`, reducing cosine cases to polynomial regression; the support changes with the arc length. | This is the closest specialized `c`-optimal Fourier prior art.  Its commensurate harmonics, fixed arc, fixed regression order, and coordinate carrier are absent from the growing noncommensurate prime-log problem. |
| H. Dette, V. B. Melas and P. Shpilev, [*Optimal Designs for Estimating the Coefficients of the Lower Frequencies in Trigonometric Regression Models*](https://doi.org/10.1007/s10463-006-0068-2), Ann. Inst. Statist. Math. 59 (2007), 655–673 | Gives analytic `c`-optimal designs for lower-frequency coefficients in the common Fourier model, using an alternative `c`-optimal characterization and Chebyshev approximation. | It completes a fixed integer-frequency problem posed by Dette--Melas; it gives no estimate uniform in a growing irregular frequency set or growing aperture. |
| R. Sanyal, F. Sottile and B. Sturmfels, [*Orbitopes*](https://doi.org/10.1112/S002557931100132X), Mathematika 57 (2011), 275–314 | Studies convex hulls of compact group orbits.  For `SO(2)` integer-weight representations, Caratheodory orbitopes are convex hulls of periodic trigonometric moment curves and are projected spectrahedra with Toeplitz/nonnegative-trigonometric-polynomial duality. | This identifies the exact convex object in the commensurate full-circle model.  Prime logarithms are not integer weights of one `SO(2)` representation, and `[T,B]` is a finite growing orbit segment, so the spectrahedral/face description does not decide (2.8). |
| Y. de Castro, F. Gamboa, D. Henrion, R. Hess, J.-B. Lasserre, [*Approximate Optimal Designs for Multivariate Polynomial Regression*](https://doi.org/10.1214/18-AOS1683), Ann. Statist. 47 (2019), 127–155 | Relates polynomial `D`-optimal design, moment/SOS relaxations, and a Christoffel-polynomial dual certificate on compact semialgebraic domains. | It concerns polynomial feature spaces and `D`-optimality.  It neither covers the oscillatory prime-log features nor supplies a directional `c`-optimal power bound. |
| R. J. Duffin and A. C. Schaeffer, [*A Class of Nonharmonic Fourier Series*](https://doi.org/10.1090/S0002-9947-1952-0047179-6), Trans. AMS 72 (1952), 341–366 | Introduces Hilbert frames in the nonharmonic Fourier setting and proves sufficient density/frame conditions for separated exponential systems. | These are `L^2` synthesis/observability statements.  They do not estimate the `L^1` gauge of one distinguished finite-dimensional carrier. |
| A. E. Ingham, [*Some Trigonometrical Inequalities with Applications to the Theory of Series*](https://doi.org/10.1007/BF01180426), Math. Z. 41 (1936), 367–379 | Gives two-sided `L^2` inequalities for nonharmonic exponential sums under a frequency-gap condition on a sufficiently long interval. | Since prime-log spacing is `gg 1/Y` and `B gg Y`, it gives long-block `L^2` conditioning.  After carrier normalization this recovers only a square-root-scale floor, not the exponent `.018...` directional result. |
| H. L. Montgomery and R. C. Vaughan, [*Hilbert's Inequality*](https://doi.org/10.1112/jlms/s2-8.1.73), J. London Math. Soc. 8 (1974), 73–82 | Sharp weighted Hilbert inequalities and resulting mean-value/large-sieve bounds for separated frequencies. | Again this controls a common Gram spectrum, not the carrier-replacement ratios in (2.8). |
| C. Aubel and H. Bölcskei, [*Vandermonde Matrices with Nodes in the Unit Disk and the Large Sieve*](https://arxiv.org/abs/1701.02538), ACHA 47 (2019), 53–86, DOI `10.1016/j.acha.2017.07.006` | Bounds extremal singular values and condition numbers of rectangular Vandermonde matrices from separation and radial data. | The bound concerns the common unaugmented matrix.  Corollary 4.2 shows exact cancellation of that Vandermonde in a carrier coefficient. |
| D. Batenkov, L. Demanet, G. Goldman, Y. Yomdin, [*Conditioning of Partial Nonuniform Fourier Matrices with Clustered Nodes*](https://arxiv.org/abs/1809.00658), SIAM J. Matrix Anal. Appl. 41 (2020), 199–220, DOI `10.1137/18M1212197` | Sharp lower bounds for the smallest singular value in the clustered/superresolution regime, with exponent controlled by maximal cluster size. | This is still an `L^2` common singular-value theorem.  It does not bound the Schur/orthogonal-character factor of the carrier direction. |
| H. J. Landau, [*Necessary Density Conditions for Sampling and Interpolation of Certain Entire Functions*](https://doi.org/10.1007/BF02395039), Acta Math. 117 (1967), 37–52 | Necessary Beurling-density conditions for stable sampling and interpolation in bandlimited entire-function spaces. | It identifies a density threshold, but only for stable `L^2` sampling/interpolation.  Near-quantile density of prime logs does not imply the `L^infinity/L^1` directional minimax bound. |
| D. Slepian, [*Prolate Spheroidal Wave Functions, Fourier Analysis, and Uncertainty—V: The Discrete Case*](https://doi.org/10.1002/j.1538-7305.1978.tb02104.x), BSTJ 57 (1978), 1371–1430; H. Landau and H. Widom, [*Eigenvalue Distribution of Time and Frequency Limiting*](https://doi.org/10.1016/0022-247X(80)90241-3), JMAA 77 (1980), 469–481 | Spectral concentration for uniform time/frequency limiting.  The eigenvalue transition is centered at the time-bandwidth dimension and has logarithmic width asymptotically. | This is the right analogy for the numerical aperture transition near one-prime conductor.  The operator is a uniform prolate concentration operator, not the irregular finite prime-log curve with distinguished vector `q_0`; no theorem transfers the transition to (2.8). |
| A. E. Litvak, A. Pajor, M. Rudelson, N. Tomczak-Jaegermann, [*Smallest Singular Value of Random Matrices and Geometry of Random Polytopes*](https://doi.org/10.1016/j.aim.2004.08.004), Adv. Math. 195 (2005), 491–523 | Independent-entry rectangular random matrices; high-probability singular-value estimates and asymptotically sharp geometric parameters of their absolute convex hulls. | A genuine random dictionary can have the logarithmically improved inradius scale.  The prime phase curve is deterministic and one-parameter. |
| Shahar Mendelson, [*On the Geometry of Random Polytopes*](https://arxiv.org/abs/1902.01664) (2019) | For independent-coordinate random rows and `N>=c n`, proves with high probability `c(B_infinity^n intersect sqrt(log(eN/n))B_2^n) subset absconv(X_1,...,X_N)` under minimal variance/tail/small-ball hypotheses. | This is the closest exact source for the `sqrt(log(N/n)/n)` heuristic scale after polarity.  The rows `a(t)` have maximally dependent coordinates driven by one scalar `t`; neither independence nor the required uniform small-ball structure has been proved. |

### What the frame results actually give

For the one-sided complex features, take a consecutive integer block of
length `L asyp B`.  The prime-power logarithms are separated by `gg 1/Y`
inside a fixed interval of length below `2*pi`.  Ingham or the
Montgomery--Vaughan large sieve therefore gives, schematically,

```text
sum_(m=m_0)^(m_0+L-1)
 |sum_j c_j exp(i*m*u_j)|^2
 >=(L-O(Y))*sum_j |c_j|^2.                             (5.1)
```

If `sum_j c_j=1`, then `sum|c_j|^2>=1/M`, so some high integer sample has
size `gg M^(-1/2)`.  This is rigorous in the separated complex model, but it
is only the familiar `L^2` square-root floor.  It is far below
`Y^(-.0180303...)` and does not resolve the real reflected-node or
directional atomic problem.  This is why importing a nonharmonic frame
theorem does not answer item 1.

### Status of the proposed logarithmic law

No audited primary source proves

```text
E_B asyp_or_leq sqrt(log(B/M)/M)                       (5.2)
```

for deterministic near-quantile nodes, for the actual prime-log nodes, or
for an arbitrary one-parameter Fourier curve.  The two closest bodies of
work have incompatible scopes:

```text
prolate/Landau theory:  deterministic but uniform and L2 spectral;
random-polytope theory: correct logarithmic convex scale but independent rows.
                                                               (5.3)
```

Deriving (5.2) for the actual curve would itself require a new deterministic
small-ball/inradius theorem or a direct bound for the directional minors in
(2.8).  Mere node density, separation, or a prolate eigenvalue count is not
such a theorem.

---

## 6. Hostile audit of the rational-alias localization card

The new report
`ZETA23-PRIME-VORONOI-RATIONAL-ALIAS-LOCALIZATION-GATE-2026-08-13.md`
was checked independently at the three requested points.

For

```text
omega_t(x)=t/(2*pi*x),
eta=sqrt(t)/Y,
Q=Y^(1/10),                                             (6.1)
```

the range of `omega_t` has length `O(t/Y)`.  At a fixed denominator `q`
there are `O(qt/Y)` relevant numerators, while the inverse image of

```text
|omega_t-a/q|<=eta/q
```

has physical length

```text
O(eta*Y^2/(q*t))=O(Y/(q*sqrt(t))).                     (6.2)
```

Therefore

```text
|M_t(Q)|<<Q*sqrt(t),
R_t(Q)<< (t/Y)*Q^2.                                    (6.3)
```

Both counts are correct.

Enlarging a union of `R` physical intervals to all meeting log-Voronoi
cells adds only `O(R)` boundary cells.  With

```text
sum g_j^2 <<Y^(123/100+epsilon),                       (6.4)
```

Cauchy--Schwarz and division by `Y` give boundary coefficient mass

```text
sqrt(R)*Y^(123/200+epsilon)/Y
 <<Q*sqrt(t)*Y^(-177/200+epsilon).                     (6.5)
```

At `t=Y^(50/33)` this is

```text
Y^[1/10+25/33-177/200+epsilon]
 =Y^(-181/6600+epsilon).                               (6.6)
```

The exponent ledger is correct.

Finally, the Voronoi weights are positive:

```text
lambda_j=integral_(C_j) phi(log(x/Y)) dx/x >=0.         (6.7)
```

Hence deleting every marked cell changes the complex antenna, and therefore
its cosine part, by at most the deleted coefficient mass.  There is no
unrecorded quadrature-error term in that deletion step.

The hostile caveat is conceptual rather than algebraic: the card proves a
small-mass excision only.  It proves no cancellation on the retained
high-denominator set, and it does not prove that the chosen curvature-width
major arcs are an analytically optimal or exhaustive obstruction.  Calling
them “stationary neighborhoods” does not by itself supply a Weyl estimate.

---

## 7. Surviving theorem card

The strongest exact finite target is now (2.8): prove, uniformly over every
legal nonsingular high-time configuration,

```text
sum_i |det A_i(t;q_0)|/|det A(t)|
 >=Y^(delta-o(1))                                      (7.1)
```

for a useful `delta`, or construct one configuration for which the same
ratio is subpower, depending on which side of the strip-route dichotomy is
being pursued.

The AP calculation shows what an arithmetic proof must see: after common
Vandermonde factors cancel, it must control high-degree Schur/orthogonal
characters of the actual prime phases.  The alternation calculation shows
what it cannot assume: there is no global ordered sign pattern to turn those
characters positive.

This explicitly bypasses the cached failures based on average rank,
unaugmented determinants, qualitative nonlattice, divided differences, and
norm-controlled local boosting.  It still does not decide `E_B`.
