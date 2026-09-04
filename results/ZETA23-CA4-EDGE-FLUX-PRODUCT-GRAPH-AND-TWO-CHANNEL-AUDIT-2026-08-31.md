# CA4 edge flux, product-graph divergence, and the minimal two-channel gate

Date: 2026-08-31

Preflight:
[zeta23_ca4_edge_flux_product_graph_preflight_v1.json](context/zeta23_ca4_edge_flux_product_graph_preflight_v1.json)

## Verdict

There is an exact and useful algebraic compression, but no new analytic
bound.

Let \(\lambda\) be the retained adjacent-gap hat probability and let
\(\eta\) be any separately passported natural prime probability on the
identical shell. Their zero-mass difference is the unique path divergence

\[
 \delta=\lambda-\eta=D^*c.
\]

Its semiprime lift is not a large scalar partition. It is one symmetric
product-graph divergence and, after evaluation, one mixed product:

\[
 \lambda\lambda^{\mathsf T}-\eta\eta^{\mathsf T}
  =\frac12(\delta s^{\mathsf T}+s\delta^{\mathsf T})
  =\operatorname{Div}_{P\mathbin{\square}P}{\cal F},
 \qquad
 M_\lambda^2-M_\eta^2=M_{D^*c}M_s,                 \tag{0.1}
\]

where \(s=\lambda+\eta\). Equivalently, with
\(r_j=\delta_j/s_j\), the ordered semiprime mask is

\[
 \frac12s_i s_k(r_i+r_k).                           \tag{0.2}
\]

Thus the missing vector theorem has only two polynomial channels and an
additive rank-two semiprime color. This is substantially more precise than
the earlier phrase “a vector-valued masked theorem.”

The compression does **not** by itself make the analytic gate smaller.
On a path, every zero-mass vector is a divergence. Product-graph cycle
freedom is a gauge: divergence-free flows pair to zero with every product
gradient and cannot change the polynomial. Standard transport, edge
square-function, and minimal \(H^{-1}\) norms do not control the high-band
mixed moment. The existing bounded-gap periodic pseudonode motif has all
of those norms tending to zero, while (0.1) has an order-one resonance at
\(T\asymp Y/\log Y\).

The honest surviving interface is an actual-prime **edge-contact mixed large
sieve** for the single exact pair \((c,s)\), at the diagonal-relative
\(Y^{1/10}\) scale. Given a matching natural theorem for \(\eta\), it would
imply CA4. It is open and is not claimed here. LTRAD remains a parallel open
edge.

## 1. The path complex and its exact transport norms

Order the shell primes by

\[
 u_1<\cdots<u_N,\qquad \Delta_j=u_{j+1}-u_j.
\]

Let \(C^0=\mathbb R^N\), \(C^1=\mathbb R^{N-1}\), and orient every path edge
to the right. The coboundary is

\[
 (Df)_j=f_{j+1}-f_j.
\]

Its adjoint is

\[
 (D^*c)_1=-c_1,\quad
 (D^*c)_j=c_{j-1}-c_j,\quad
 (D^*c)_N=c_{N-1}.                                  \tag{1.1}
\]

Because \(\sum\delta=0\), there is a unique edge flux with
\(D^*c=\delta\):

\[
 c_j=-\sum_{i\leq j}\delta_i.                       \tag{1.2}
\]

Consequently

\[
 \|c\|_\infty
  =\max_j\left|\lambda([1,j])-\eta([1,j])\right|    \tag{1.3}
\]

is the Kolmogorov discrepancy, while the one-dimensional transport identity
gives

\[
 W_{1,u}(\lambda,\eta)
   =\sum_{j<N}\Delta_j|c_j|.                        \tag{1.4}
\]

These identities are exact, including when some retained hat weights vanish.
They also give the first warning: \(\operatorname{image}(D^*)\) is the whole
zero-mass subspace. The assertion “\(\delta\) is an adjacent-edge flux”
alone restricts nothing beyond normalization.

For the exact retained hats, there is a useful cumulative formula. Write

\[
 m_j=\rho_j\int_{u_j}^{u_{j+1}}\phi(v)\,dv,\qquad
 R_j=\rho_j\int_{u_j}^{u_{j+1}}\phi(v)
           \frac{u_{j+1}-v}{\Delta_j}\,dv,\qquad
 W=\sum_jm_j,                                       \tag{1.5}
\]

where \(\rho_j\) is the retained-edge indicator. Directly summing the two
nodal shares gives

\[
 \sum_{i\leq j}\lambda_i
  =\frac{\sum_{r<j}m_r+R_j}{W}.                     \tag{1.6}
\]

Hence the exact flux against a natural comparator is

\[
 c_j=\sum_{i\leq j}\eta_i
      -\frac{\sum_{r<j}m_r+R_j}{W}.                 \tag{1.7}
\]

Formula (1.7) has not erased the arithmetic selector. It has converted it
into a cumulative weighted-prime discrepancy plus one retained half-edge.
Even after the natural taper is chosen so that its continuous main term
matches the hat profile, classical PNT remainders give only subpower uniform
control for the cumulative error; no fixed-power norm estimate needed below
follows. A mismatched taper is worse, since it also leaves a fixed continuum
drift.

## 2. Symmetric-square lift and discrete Leibniz identities

Put

\[
 \delta=\lambda-\eta,\qquad s=\lambda+\eta.
\]

Polarization gives

\[
 A:=\lambda\lambda^{\mathsf T}-\eta\eta^{\mathsf T}
   =\frac12(\delta s^{\mathsf T}+s\delta^{\mathsf T}). \tag{2.1}
\]

There are also two one-sided discrete Leibniz formulas:

\[
 A=D^*(c\eta^{\mathsf T})+(\lambda c^{\mathsf T})D
  =D^*(c\lambda^{\mathsf T})+(\eta c^{\mathsf T})D. \tag{2.2}
\]

On the Cartesian product path define the horizontal and vertical fluxes

\[
 F^x=\frac12c s^{\mathsf T},\qquad
 F^y=\frac12s c^{\mathsf T}.
\]

Then the exact product divergence is

\[
 A=D^*F^x+F^yD.                                    \tag{2.3}
\]

In weak form, for every matrix \(f\),

\[
\begin{aligned}
 \langle A,f\rangle
 ={}&\frac12\sum_{j,k}c_js_k(f_{j+1,k}-f_{j,k})\\
   &+\frac12\sum_{i,\ell}s_ic_\ell
                (f_{i,\ell+1}-f_{i,\ell}).         \tag{2.4}
\end{aligned}
\]

If \(f\) is symmetric, the two terms in (2.4) are equal. For

\[
 z_i(t)=e^{itu_i},\qquad
 E_c(t)=\sum_{j<N}c_j(z_{j+1}(t)-z_j(t)),
\]

(1.1)--(1.2) and (2.4) give

\[
 E_c(t)=M_\delta(t),\qquad
 \langle A,z(t)z(t)^{\mathsf T}\rangle
  =E_c(t)M_s(t)
  =M_\lambda(t)^2-M_\eta(t)^2.                    \tag{2.5}
\]

There is an equivalent additive-color form. Set \(r_i=\delta_i/s_i\) on
the support of \(s\) and zero elsewhere. Positivity of \(\lambda,\eta\)
gives

\[
 |r_i|\leq1,\qquad \sum_i s_ir_i=\sum_i\delta_i=0,
\]

and

\[
 A_{ik}=\frac12s_is_k(r_i+r_k).                    \tag{2.6}
\]

Thus the semiprime discrepancy is not an arbitrary two-factor mask: it is
the lift of one bounded, \(s\)-balanced vertex color by addition. This exact
rank-two fact is the main structural gain of the calculation.

More generally, tensor powers obey the chain-homotopy identity

\[
 \lambda^{\otimes k}-\eta^{\otimes k}
 =\sum_{a=0}^{k-1}
   \lambda^{\otimes a}\otimes(D^*c)
              \otimes\eta^{\otimes(k-1-a)},        \tag{2.7}
\]

whose evaluation is the ordinary factorization of
\(M_\lambda^k-M_\eta^k\). No higher-order analytic conclusion is imported
from (2.7).

## 3. Exact semiprime diagonal

Let

\[
 d(n)=a_\lambda(n)-a_\eta(n)
     =\sum_{p_ip_k=n}\delta_i s_k.                 \tag{3.1}
\]

For \(i\neq k\), the coefficient at \(p_ip_k\) is
\(\delta_i s_k+\delta_k s_i\); on the diagonal it is \(\delta_i s_i\).
Unique factorization therefore gives

\[
 {\cal D}(\delta,s):=\sum_n|d(n)|^2
  =\|\delta\|_2^2\|s\|_2^2
      +|\langle\delta,s\rangle|^2
      -\sum_i\delta_i^2s_i^2.                     \tag{3.2}
\]

In the bounded-color coordinates of (2.6), the same diagonal is

\[
 {\cal D}
 =\left(\sum_i s_i^2r_i^2\right)\left(\sum_i s_i^2\right)
  +\left(\sum_i s_i^2r_i\right)^2
  -\sum_i s_i^4r_i^2.                              \tag{3.2a}
\]

In particular,

\[
 0\leq{\cal D}(\delta,s)
 \leq2\|\delta\|_2^2\|s\|_2^2.                    \tag{3.3}
\]

For any natural shell probability with
\(\sum\eta_i^2=Y^{-1+o(1)}\), the proved hat bound gives

\[
 \|\delta\|_2^2,\ \|s\|_2^2
 \ll Y^{-q+o(1)},\qquad
 {\cal D}(\delta,s)\ll Y^{-2q+o(1)},\qquad
 q=\frac{2787}{3250}.                              \tag{3.4}
\]

Thus the diagonal itself is affordable. The open content is the translated
off-diagonal contact.

## 4. Double divergence of the translated kernel

Let \(\psi\) be one common smooth nonnegative window and put

\[
 K(x)=\int_{\mathbb R}\psi(v)e^{ivx}\,dv,\qquad
 U_{ik}=u_i+u_k.
\]

Then

\[
 Q_T(A):=\int\psi(t/T)|M_\delta(t)M_s(t)|^2\,dt
 =T\sum_{x,y}A_xA_yK(T(U_x-U_y)).                  \tag{4.1}
\]

Using (2.3) twice moves both divergences onto the kernel. If \(e,e'\) are
oriented product edges, with logarithmic increments
\(\ell_e,\ell_{e'}\), the corresponding edge-edge kernel is exactly

\[
 {\cal K}_T(e,e')
 =\int\psi(t/T)e^{it(U_e^--U_{e'}^-)}
       (e^{it\ell_e}-1)(e^{-it\ell_{e'}}-1)\,dt.    \tag{4.2}
\]

Equivalently, (4.2) is the alternating sum of \(T K\) at the four pairs of
edge endpoints. With the product flux from (2.3),

\[
 Q_T(A)=\langle{\cal F},{\cal K}_T{\cal F}\rangle.  \tag{4.3}
\]

The elementary finite-difference estimate is

\[
 |{\cal K}_T(e,e')|
 \ll T\,m_T(\ell_e)m_T(\ell_{e'}),\qquad
 m_T(x)=\min(1,T|x|).                              \tag{4.4}
\]

A horizontal product edge replaces \(p_jp_k\) by \(p_{j+1}p_k\). Its
physical displacement and its size relative to the contact resolution are

\[
 L_e=g_jp_k\asymp Yg_j,\qquad
 \frac{L_e}{H}\asymp\frac{Tg_j}{Y}\asymp T\Delta_j,
 \qquad H=Y^2/T.                                  \tag{4.5}
\]

Thus (4.3) is an edge-edge crossing form for the boundary of the near-product
contact region. It preserves the common signed kernel and exact resolution.
It does not automatically save a power: once \(T\Delta_j\geq1\), (4.4) has
no small factor.

## 5. The precise conditional two-channel theorem

The CA4 integral budget is

\[
 T Y^{-2q+1/10+o(1)}
   =T Y^{-5249/3250+o(1)},                          \tag{5.1}
\]

or, after taking a square root,

\[
 T^{1/2}Y^{-q+1/20+o(1)}
   =T^{1/2}Y^{-5249/6500+o(1)}.                    \tag{5.2}
\]

The exact new interface can be stated as follows.

> **PG-EF(1/10) (open).** For the exact actual-prime flux \(c\) from
> (1.7), \(s=\lambda+\eta\), every legal translated window, and the common
> kernel,
> \[
> Q_T(A)\ll T Y^{1/10+o(1)}{\cal D}(\delta,s).      \tag{5.3}
> \]

By (3.4), (5.3) gives (5.1) for the discrepancy. If, independently,

\[
 \int\psi(t/T)|M_\eta(t)|^4dt
 \ll T Y^{-2q+1/10+o(1)},                          \tag{5.4}
\]

then (2.5) and Minkowski imply CA4 for \(\lambda\).

This is a two-channel, additive-color, diagonal-relative mixed large sieve.
It is narrower than an arbitrary-coefficient four-cycle theorem and is
stronger than the direct discrepancy target whenever
\({\cal D}(\delta,s)\) is smaller than its worst currently proved scale.
The weaker statement
\[
 Q_T(A)\ll T Y^{-2q+1/10+o(1)}                     \tag{5.5}
\]
is, once (5.4) is granted, equivalent up to constants to CA4 for
\(\lambda\), by the triangle inequality in both directions. Thus (5.5) is
an exact interface rather than progress, while (5.3) is a clean
diagonal-relative strengthening with a narrower coefficient passport but
no proof. The algebraic compression alone does not show that either
analytic statement is easier.

## 6. Exponent ledger and the failure of generic mean values

The ordinary product-length mean-value theorem gives only

\[
 Q_T(A)\ll (T+Y^2)Y^{o(1)}{\cal D}(\delta,s).       \tag{6.1}
\]

Relative to (5.3), it must replace the conductor \(Y^2\) by
\(T Y^{1/10}\). At \(T=Y^\alpha\) the missing saving is

\[
 Y^{2-\alpha-1/10}.                                \tag{6.2}
\]

At the two endpoints this is

\[
 \begin{array}{c|c}
 \alpha=1049/1250 & Y^{663/625}\\
 \alpha=50/33 & Y^{127/330}.
 \end{array}                                       \tag{6.3}
\]

Even if the heuristic diagonal were the stronger
\({\cal D}(\delta,s)=Y^{-2+o(1)}\), (6.1) is only \(Y^{o(1)}\).
At the upper endpoint the actual CA4 target is

\[
 Y^{-10717/107250+o(1)},                           \tag{6.4}
\]

so a fixed \(Y^{.099925\ldots}\) gap remains.

The adjacent-edge multiplier aligns with the already-closed transition,
not with the open high band. At the lower CA4 endpoint and the retained
cutoff \(\theta=163/1000\),

\[
 T\Delta_j\ll Y^{1049/1250+163/1000-1}
             =Y^{11/5000}.                         \tag{6.5}
\]

Cutting instead at
\(\theta_0=1-1049/1250=201/1250\) merely makes the largest edge
subresolution by a constant. Its tail saving is

\[
 s(\theta_0)=\frac{309}{16250}=.01901538\ldots .    \tag{6.6}
\]

After retaining the required \(.019\) tail reserve, the greatest uniform
fixed-power multiplier saving available at that single endpoint is only
\(Y^{-1/45000}\). Immediately higher in the band it disappears. At the top,
even a physical prime gap of \(2\) has
\(T\Delta\gg Y^{17/33}\), so no uniform small-increment upper bound is
available.

## 7. Candidate flux norms and their exact thresholds

### 7.1 Logarithmic transport

Summation by parts gives

\[
 |M_\delta(t)|
 \leq |t|\sum_j\Delta_j|c_j|
 =|t|W_{1,u}(\lambda,\eta).                        \tag{7.1}
\]

Using only \(|M_s|\leq2\), this route would need

\[
 W_{1,u}(\lambda,\eta)
 \ll T^{-1}Y^{-5249/6500+o(1)}.                    \tag{7.2}
\]

The required exponents are \(53519/32500=1.646738\ldots\) at the lower
endpoint and \(498217/214500=2.322689\ldots\) at the upper endpoint.
Nothing close to (7.2) is proved.

### 7.2 Phase-weighted edge square function

Define

\[
 {\cal C}_T(c)^2
  =\sum_{j<N}|c_j|^2\min(1,T\Delta_j)^2.            \tag{7.3}
\]

An ideal no-loss edge/vertex decoupling

\[
 Q_T(A)\ll T Y^{o(1)}{\cal C}_T(c)^2\|s\|_2^2     \tag{7.4}
\]

would meet CA4 from current information only if

\[
 {\cal C}_T(c)^2\ll Y^{-q+1/10+o(1)}
  =Y^{-1231/1625+o(1)}.                             \tag{7.5}
\]

No such actual-prime bound is known. More importantly, (7.4) itself is
false for the bounded-gap pseudonode class in Section 9, even when (7.5)
holds with room. Edge-square size does not prevent coherent aliases.

### 7.3 Product-graph \(H^{-1}\) energy

Let \(L_\square\) be the combinatorial Laplacian on
\(P_N\mathbin{\square}P_N\) and define

\[
 {\cal H}_{-1}(A)
  =\langle A,L_\square^+A\rangle
  =\inf_{\operatorname{Div}F=A}\|F\|_2^2.          \tag{7.6}
\]

The explicit flux (2.3) gives

\[
 {\cal H}_{-1}(A)
 \leq\frac12\|c\|_2^2\|s\|_2^2.                   \tag{7.7}
\]

For \(z_i=e^{itu_i}\), however,

\[
 \|D_\square(z\otimes z)\|_2^2
   =2N\sum_{j<N}|e^{it\Delta_j}-1|^2,              \tag{7.8}
\]

and Cauchy--Schwarz only yields

\[
 |M_\delta(t)M_s(t)|^2
 \leq {\cal H}_{-1}(A)
       \|D_\square(z\otimes z)\|_2^2.              \tag{7.9}
\]

The phase energy in (7.8) can be of order \(N^2\). A small
negative-Sobolev norm is therefore canceled by a large high-frequency
gradient and supplies no high-band saving by itself.

## 8. Product cycles are gauge, not cancellation resources

The product graph has many four-cycles, so (2.3) is not the unique flow with
divergence \(A\). This freedom does not create a new analytic degree of
freedom. If \(Z\) is divergence-free, then for every product test function
\(f\),

\[
 \langle Z,D_\square f\rangle
  =\langle\operatorname{Div}Z,f\rangle=0.          \tag{8.1}
\]

In particular, adding a circulation changes neither (2.5) nor (4.3). The
double-difference Gram operator annihilates the cycle space. Hodge
projection may reduce the displayed Euclidean norm of a representative,
but the compensating phase-gradient factor remains. Optimizing over cycle
flows is therefore a gauge choice, not an unaccounted source of CA4
cancellation.

## 9. Fast falsifier: the bounded-gap periodic hat motif

Reuse the exact \(N=4M\) pseudonode motif from the hostile mask audit. With
natural mass \(\eta_j=1/N\), the cyclic hat weights repeat

\[
 \lambda_j=\frac1N(5/4,5/4,3/4,3/4),\qquad
 \delta_j=\frac1{4N}(1,1,-1,-1).                  \tag{9.1}
\]

The cumulative flux repeats

\[
 c_j=\frac1{4N}(-1,-2,-1,0),                       \tag{9.2}
\]

up to the harmless terminal path convention. Hence

\[
 \|c\|_\infty=\frac1{2N},\qquad
 \|c\|_2^2=\frac3{32N}+O(N^{-2}),\qquad
 W_{1,u}(\lambda,\eta)\asymp N^{-1}.              \tag{9.3}
\]

Also

\[
 \|s\|_2^2=\frac{65}{16N},\qquad
 {\cal H}_{-1}(A)\ll N^{-2},                       \tag{9.4}
\]

and the exact semiprime diagonal is

\[
 {\cal D}(\delta,s)
 =\frac{33}{128N^2}-\frac{65}{256N^3}.             \tag{9.5}
\]

Choose the motif spacing and height so that the node phases are \(++--\).
Then

\[
 M_\eta(t_0)=0,\qquad M_\lambda(t_0)=\frac14,\qquad
 M_\delta(t_0)M_s(t_0)=\frac1{16}.                \tag{9.6}
\]

The peak persists on an interval of fixed width. With
\(N\asymp Y/\log Y\), one has \(t_0\asymp Y/\log Y\) inside the CA4 band,
all gaps are retained, and

\[
 T Y^{1/10}{\cal D}(\delta,s)=Y^{-.9+o(1)}\to0.    \tag{9.7}
\]

Thus the pseudonode model refutes each of the following soft implications:

1. small transport distance implies the required mixed band norm;
2. small phase-weighted edge \(\ell^2\) size implies (7.4);
3. small minimal product-graph \(H^{-1}\) energy implies (5.3);
4. bounded gaps, prime-scale density, positivity, normalization, and the
   chain-complex identity imply the edge-contact large sieve.

This is not an actual-prime counterexample. Its role is to force any proof
of (5.3) to use an actual-prime non-aliasing or selector-correlation theorem,
not just graph topology or transport norms.

## 10. Decision-tree update

| Statement | Status |
|---|---|
| \(\delta=D^*c\) with (1.2) | **EXACT IDENTITY** |
| symmetric product divergence (2.1)--(2.5) | **EXACT IDENTITY** |
| additive rank-two selector (2.6) | **EXACT IDENTITY** |
| cycle-flow optimization creates new cancellation | **REFUTED: gauge only** |
| transport / edge-square / \(H^{-1}\) norms alone close the mixed moment | **REFUTED in the licensed pseudonode proof class** |
| actual-prime PG-EF(1/10) | **OPEN** |
| natural comparator estimate (5.4) | **INDEPENDENT OPEN/CONDITIONAL PREMISE** |
| CA4(163/1000,1/10) | **OPEN** |
| LTRAD_P(.0189,.001) | **OPEN independently** |
| uniform strip / RH | **OPEN** |

The algebra recommends a narrower research object: study the edge-edge
contact Gram matrix only on the rank-one symmetric flux
\((c\otimes s+s\otimes c)/2\), with \(c\) given by the exact cumulative
formula (1.7). It does not justify another scalar partition, an \(H^{-1}\)
shortcut, or a claimed bound.
