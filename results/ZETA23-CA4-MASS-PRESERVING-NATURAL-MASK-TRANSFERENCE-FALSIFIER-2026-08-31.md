# CA4 mass-preserving natural-mask transference falsifier

Date: 2026-08-31

Preflight:
[`zeta23_ca4_mask_transference_falsifier_preflight_v1.json`](context/zeta23_ca4_mask_transference_falsifier_preflight_v1.json)

Finite replay:
[`ca4_mask_transference_falsifier.py`](../src/ca4_mask_transference_falsifier.py)

Bounded-density pseudonode verifier:
[`ca4_gap_lambda_transference.py`](../src/ca4_gap_lambda_transference.py)

## Verdict

> **Post-audit sharpening:** the surviving joint theorem has since been
> compressed exactly to the two-channel, additive-rank-two mixed product
> `M_(lambda-eta) M_(lambda+eta)` in
> [`ZETA23-CA4-EDGE-FLUX-PRODUCT-GRAPH-AND-TWO-CHANNEL-AUDIT-2026-08-31.md`](ZETA23-CA4-EDGE-FLUX-PRODUCT-GRAPH-AND-TWO-CHANNEL-AUDIT-2026-08-31.md).
> This does not change the no-go below or prove the mixed estimate.

The proposed **scalar** transference from standard interval-localized or
bounded-variation smooth natural `Lambda*Lambda` shifted-correlation forms
to the adjacent-gap `CA4` form is refuted.  This is an adapter no-go, not a
refutation of `CA4` and not a no-go for every imaginable product-dependent
or oscillatory natural atom.

The conclusion survives a deliberately stronger grant than
Alpoge--Furman actually provide: allow a natural fourth-moment theorem, at
the ideal diagonal scale, for every consecutive factor interval in the
exact prime shell and for every mixed pair of such intervals.  Even under
that grant:

1. An exact positive combination of natural square atoms cannot equal the
   target semiprime atom unless every used prime mask is already the hat
   mask.  This is an exact rank-one cone obstruction.
2. Signed and mixed-rectangle decompositions exist, but every scalar
   decomposition has diagonal recombination norm at least

   \[
      (\log Y)^{-4}.
   \]

   `CA4(163/1000,1/10)` requires that norm to be at most

   \[
      Y^{-q+1/20+o(1)}
       =Y^{-5249/6500+o(1)},\qquad q=2787/3250.     \tag{0.1}
   \]

   A logarithmic lower bound cannot fit this fixed-power budget.

The obstruction is not just that one attempted partition was inefficient.
It follows from a dual certificate built from the discrete variation of the
actual retained nodal-hat weights.  Those weights satisfy

\[
 \sum_j|\lambda_{j+1}-\lambda_j|\gg (\log Y)^{-2}, \tag{0.2}
\]

whereas every normalized natural interval mask has variation comparable to
the square of its `ell^2` norm.  The tensor square of the variation witness
tests any signed mixed natural decomposition in this passported class and
proves the lower bound above, independently of the number of scalar terms.

There remains one credible escape: retain all decomposition signs and prove
a **joint vector-valued** shifted-correlation theorem before taking an
absolute value.  That would preserve the common translated kernel and the
resolution `H=Y^2/T`, but it is new selector-sensitive mathematics, not an
adapter to scalar `HL*(4)`.  The falsifier therefore sharpens the open target
rather than closing it.

## 1. Exact objects and exponent budget

Let

\[
 I_Y=[Ye^{-1/5},Ye^{1/5}],\qquad
 p_1<\cdots<p_N
\]

be all ordinary primes in the shell.  Put

\[
 v_j=\log(p_j/Y),\qquad
 g_j=p_{j+1}-p_j,\qquad
 \Delta_j=v_{j+1}-v_j,
\]

and

\[
 \phi(u)=(1-5|u|)e^{49u/100}
\]

and set `G=Y^(163/1000)`.  Delete both endpoint shares of every edge with `g_j>G`
and normalize the remaining nodal-hat masses once.  Explicitly, before
normalization the mass at `p_j` is

\[
\begin{aligned}
 \omega_j={}&\mathbf 1_{g_{j-1}\le G}
  \int_{v_{j-1}}^{v_j}\phi(u)
       \frac{u-v_{j-1}}{\Delta_{j-1}}\,du\\
 &+\mathbf 1_{g_j\le G}
  \int_{v_j}^{v_{j+1}}\phi(u)
       \frac{v_{j+1}-u}{\Delta_j}\,du,\qquad
 \lambda_j=\frac{\omega_j}{\sum_i\omega_i}.       \tag{1.1}
\end{aligned}
\]

Endpoint conventions do not affect the argument.  This is the exact
positive, frequency-independent mask from the retained `HT-HAT` branch.

Let

\[
 M_\lambda(t)=\sum_j\lambda_j e^{it\log(p_j/Y)}.
\]

Unique factorization identifies its square with the semiprime coefficient
sequence

\[
 a_\lambda(n)=\sum_{p_ip_j=n}\lambda_i\lambda_j.    \tag{1.2}
\]

Equivalently, (1.2) is the symmetric factor matrix

\[
 A_\lambda=\lambda\lambda^{\mathsf T};             \tag{1.3}
\]

an off-diagonal matrix entry is counted twice in the one-dimensional
Dirichlet convolution and a diagonal entry once.  Thus the semiprime
sequence determines (1.3) exactly.

For one common smooth translated kernel,

\[
 \|M_\lambda^2\|_{L^2(T,2T)}^2
 =T\sum_{m,n}a_\lambda(m)a_\lambda(n)
       K\!\left(T\log\frac mn\right).              \tag{1.4}
\]

The kernel signs in (1.4) are essential.  Its physical resolution is

\[
 H=Y^2/T,
 \qquad H=Y^{16/33}\quad\hbox{at }T=Y^{50/33}.     \tag{1.5}
\]

The `CA4` target is

\[
 \|M_\lambda^2\|_{L^2(T,2T)}
 \ll T^{1/2}Y^{-q+1/20+o(1)}.                      \tag{1.6}
\]

Since

\[
 q-\frac1{20}
 =\frac{2787}{3250}-\frac1{20}
 =\frac{5249}{6500}=.80753846\ldots,               \tag{1.7}
\]

this is the exact scalar recombination budget in (0.1).

## 2. What was granted to the natural side

Alpoge--Furman Section 7.2 describes `HL*(4)` as the conditional input which
would evaluate shifted correlations

\[
 \sum_m(\Lambda*\Lambda)(m)(\Lambda*\Lambda)(m+h),
 \qquad |h|\le X^2/T.                              \tag{2.1}
\]

At `X=Y`, (2.1) has exactly the resolution (1.5).  It is nevertheless only
a conditional natural-weight statement, and their unconditional diagonal
range misses its `k=4` instance at the project height by
`Y^(32/33+o(1))`.

For the falsifier, grant substantially more.  For every consecutive prime
interval `J` inside `I_Y`, let

\[
 \nu_J(p)=\frac{w(p){\bf1}_{p\in J}}
                 {\sum_{r\in J}w(r)},              \tag{2.2}
\]

where either `w(p)=Lambda(p)` or the exact explicit-formula weight
`w(p)=Lambda(p)/sqrt(p)` may be used.  Prime powers are discarded, which
only makes matching the prime-only target easier.  Allow also every mixed
factor atom

\[
 A_{J,L}=\frac12
  (\nu_J\nu_L^{\mathsf T}+\nu_L\nu_J^{\mathsf T}). \tag{2.3}
\]

Finally, assume the ideal scalar estimate

\[
 \|M_{\nu_J}M_{\nu_L}\|_{L^2(T,2T)}
 \ll T^{1/2}Y^{o(1)}
       \|\nu_J\|_2\|\nu_L\|_2                    \tag{2.4}
\]

for every pair, every legal shell, and every translated window.  This
uniform shell-local mixed theorem is not in Alpoge--Furman; it is a
best-case grant designed to make the adapter as easy as possible.

Consider any signed decomposition

\[
 A_\lambda=\sum_{k=1}^K c_k A_{J_k,L_k}+E.         \tag{2.5}
\]

Applying (2.4) termwise and controlling the residual coefficientwise costs

\[
 \mathcal A(2.5):=
 \sum_{k=1}^K|c_k|\|\nu_{J_k}\|_2\|\nu_{L_k}\|_2
 +\|E\|_{\ell^1(\{1,\ldots,N\}^2)}.               \tag{2.6}
\]

Minkowski and (2.4) can prove (1.6) only if

\[
 \mathcal A(2.5)\ll Y^{-5249/6500+o(1)}.           \tag{2.7}
\]

The rest of the report proves that (2.7) is impossible.

## 3. Positive mass-preserving decompositions fail by rank

First restrict to literal natural square atoms and suppose

\[
 \lambda\lambda^{\mathsf T}
   =\sum_k c_k\nu_k\nu_k^{\mathsf T},
 \qquad c_k\ge0.                                   \tag{3.1}
\]

If `x` is orthogonal to `lambda`, then

\[
 0=x^{\mathsf T}\lambda\lambda^{\mathsf T}x
   =\sum_kc_k|x^{\mathsf T}\nu_k|^2.
\]

Hence every `nu_k` with `c_k>0` lies in the one-dimensional span of
`lambda`.  Since all vectors have mass one, every such `nu_k` equals
`lambda`.  Thus a positive exact decomposition does not transfer the mask:
it merely renames it.

This argument is exact and independent of exponents.  Signed coefficients,
mixed factor boxes, or a residual are the only possible escapes.  They are
covered by the quantitative dual certificate below.

## 4. Actual-prime variation theorem for the retained hats

### Theorem 4.1

For the exact weights (1.1),

\[
 V(\lambda):=\sum_{j=1}^{N-1}|\lambda_{j+1}-\lambda_j|
 \gg (\log Y)^{-2}.                                \tag{4.1}
\]

The implied constant is absolute once the fixed inner shell and profile are
chosen.

### 4.1 Local expansion

Restrict to the inner shell `|v_j|<=1/10`, where `phi` is bounded above and
below by positive constants.  On an edge with `g_j<=G`, the two barycentric
integrals in (1.1) give, by the Lipschitz property of `phi`,

\[
 \int_{v_j}^{v_{j+1}}\phi(u)
       \frac{v_{j+1}-u}{\Delta_j}\,du
 =\frac12\phi(v_j)\Delta_j+O(\Delta_j^2),          \tag{4.2}
\]

and the analogous estimate holds for the other endpoint.  Moreover,

\[
 \Delta_j=\frac{g_j}{p_j}+O(g_j^2/Y^2),\qquad
 \Delta_{j-1}=\frac{g_{j-1}}{p_j}+O(g_{j-1}^2/Y^2).
\]

The retained total mass is bounded above and below: the full tent mass is a
fixed positive constant and the deleted mass is
`O(Y^(-267/13000+o(1)))`.  Therefore, for every index whose two adjacent
edges are retained,

\[
 \lambda_j=\frac{c_Y(v_j)}Y(g_{j-1}+g_j)
             +O(G^2/Y^2),                          \tag{4.3}
\]

Here `c_Y` is uniformly positive and uniformly Lipschitz on the inner shell;
its `Y` dependence comes only from the retained normalizing factor, which is
bounded away from zero and infinity.

Put `s_j=g_{j-1}+g_j`.  If the three neighboring edges are retained and
`s_{j+1}!=s_j`, then the gaps are even integers and
`|s_{j+1}-s_j|>=2`.  Since

\[
 G^2/Y^2=Y^{-2+326/1000}=o(Y^{-1}),                \tag{4.4}
\]

the drift of `c_Y(v_j)` and the error in (4.3) are both `o(Y^(-1))`.
Consequently

\[
 |\lambda_{j+1}-\lambda_j|\gg Y^{-1}              \tag{4.5}
\]

at every such change.

### 4.2 Two-periodic gap runs are logarithmically short

The equality `s_{j+1}=s_j` is exactly

\[
 g_{j+1}=g_{j-1}.                                  \tag{4.6}
\]

Thus a consecutive run with no changes has a two-periodic gap sequence.
Each parity subsequence of its primes is an arithmetic progression with
common difference

\[
 D=g_j+g_{j+1}\le2G.                               \tag{4.7}
\]

If `m` terms of an arithmetic progression `a+rD` are primes of size
comparable with `Y`, every prime `ell<=m` divides `D`.  Otherwise one of any
`ell` consecutive terms is `0 mod ell` and is larger than `ell`, a
contradiction.  Hence

\[
 \prod_{\substack{\ell\le m\\ \ell\ \mathrm{prime}}}\ell\mid D.
\]

Chebyshev's bound for the primorial gives `exp(c m)<=D<=2Y^theta`, so

\[
 m\ll\log Y.                                      \tag{4.8}
\]

This uses actual primality; a density-only pseudonode set would not license
the conclusion.

### 4.3 Counting changes

There are `asymp Y/log Y` actual primes in the fixed inner shell by the prime
number theorem.  At most

\[
 O(Y/G)=O(Y^{1-163/1000})                           \tag{4.9}
\]

edges can have length above `G`, simply because their disjoint physical
lengths sum to `O(Y)`.  Removing a bounded neighborhood of every such edge
leaves `asymp Y/log Y` good indices in at most `O(Y/G)` blocks.

By (4.8), a block of `L` good indices contains `gg L/log Y` changes, up to
one endpoint loss.  Summing over the blocks gives

\[
 \#\{j:s_{j+1}\ne s_j\}
 \gg \frac{Y}{(\log Y)^2}-O(Y/G)
 \gg \frac{Y}{(\log Y)^2}.                         \tag{4.10}
\]

Combining (4.5) and (4.10) proves (4.1).

## 5. The signed mixed-atom dual certificate

Let `D` be the first-difference matrix and choose

\[
 \epsilon_j=\operatorname{sgn}((D\lambda)_j),
 \qquad b=D^{\mathsf T}\epsilon.                  \tag{5.1}
\]

Then

\[
 \|b\|_\infty\le2,
 \qquad b^{\mathsf T}\lambda=V(\lambda).          \tag{5.2}
\]

For a natural interval probability (2.2), its nonzero entries are monotone
and mutually comparable.  If the interval contains `n_J` primes, then

\[
 V(\nu_J)\ll n_J^{-1}
 \asymp\|\nu_J\|_2^2.                              \tag{5.3}
\]

The same estimate holds for a standard one-bump smooth localization with
uniform derivative bounds.  Equations (5.1)--(5.3) give

\[
 |b^{\mathsf T}\nu_J|\le V(\nu_J)
 \ll\|\nu_J\|_2^2\le\|\nu_J\|_2.                 \tag{5.4}
\]

Use the matrix test `B=bb^(T)`.  On the target,

\[
 \langle B,A_\lambda\rangle
  =(b^{\mathsf T}\lambda)^2=V(\lambda)^2.          \tag{5.5}
\]

On every mixed natural atom,

\[
 |\langle B,A_{J,L}\rangle|
 =|b^{\mathsf T}\nu_J|\,|b^{\mathsf T}\nu_L|
 \ll\|\nu_J\|_2\|\nu_L\|_2.                    \tag{5.6}
\]

Finally `|B_ij|<=4`, so `|<B,E>|<=4||E||_1`.  Applying `B` to
(2.5), then using (4.1), yields the promised universal bound

\[
 \mathcal A(2.5)\gg V(\lambda)^2
 \gg(\log Y)^{-4}.                                \tag{5.7}
\]

This proves that (2.7) cannot hold.  It permits arbitrary signs, arbitrary
mixed consecutive factor boxes, arbitrary `K`, and an approximate
coefficientwise residual.  For square atoms `J=L`, the nonsquared test
obtained by symmetrizing `b 1^(T)` improves (5.7) to
`mathcal A \gg (log Y)^(-2)`, but the weaker mixed-atom bound already refutes
the required power budget.

## 6. Why the obvious decompositions do not evade the certificate

### 6.1 The tautological one-form representation

On primes, set

\[
 c(p)=\lambda_p/\Lambda(p).
\]

Then

\[
 a_\lambda=(\Lambda c)*(\Lambda c).                \tag{6.1}
\]

This uses one form and preserves every sign and resolution, but it has not
removed the mask: `c(p)` contains the two adjacent prime gaps and the edge
deletion.  A theorem uniform in (6.1) is precisely a masked `HL*(4)` theorem,
not the natural one.

### 6.2 Singleton intervals

Every probability has the exact positive decomposition

\[
 \lambda=\sum_j\lambda_j\delta_{p_j},
 \qquad
 \lambda\lambda^{\mathsf T}
   =\sum_{i,j}\lambda_i\lambda_j
       \delta_{p_i}\delta_{p_j}^{\mathsf T}.       \tag{6.2}
\]

Singletons are natural interval measures in the most generous sense and
(6.2) preserves total mass one.  Its scalar diagonal norm is also exactly
one, however, rather than the `Y^(-5249/6500)` required by (2.7).  It loses a
factor `Y^(5249/6500+o(1))` before any analytic estimate is used.

### 6.3 Approximation by one natural shell mask

Let

\[
 \nu(p)=\frac{\Lambda(p)/\sqrt p}
              {\sum_{r\in I_Y}\Lambda(r)/\sqrt r}.
\]

Monotonicity gives `V(nu)=O(log Y/Y)`.  Since variation is at most twice
the `ell^1` norm,

\[
 \|\lambda-\nu\|_1
 \ge\frac12|V(\lambda)-V(\nu)|
 \gg(\log Y)^{-2}.                                \tag{6.3}
\]

At the prime-polynomial level, a coefficientwise transfer would require

\[
 \|\lambda-\nu\|_1
 \ll Y^{-q/2+1/40+o(1)}
 =Y^{-5249/13000+o(1)}.                            \tag{6.4}
\]

Thus even the unsquared approximation already fails its power budget.

### 6.4 Prefix/interval Abel decompositions

Discrete Abel summation can represent any mask by signed natural prefixes.
The representation is exact, but applying scalar prefix theorems charges
the total variation of the density ratio.  The witness (5.1) is the dual of
that Abel norm and proves that no rearrangement into consecutive intervals
can make its scalar semiprime cost smaller than (5.7).

### 6.5 Density-ratio truncation also misses the budget

Give the natural shell probability the same fixed taper and write
`lambda_p=nu_p rho_p`.  Up to `Y^o(1)`, `nu_p=Y^(-1)` and the retained-gap
cutoff gives `rho_p<=Y^theta`, where `theta=163/1000`.  Since

\[
 \sum_p\lambda_p^2\ll Y^{-q+o(1)},
 \qquad q=\frac{2787}{3250},
\]

the information currently proved bounds the high-ratio mass only by

\[
 \sum_{\rho_p>Y^\beta}\lambda_p
 \ll Y^{1-q-\beta+o(1)}.                           \tag{6.5}
\]

Thus retaining `1-o(1)` mass needs

\[
 \beta>1-q=\frac{463}{3250}=.142461\ldots,
\]

and making the discarded mass `O(Y^(-.019))` needs

\[
 \beta\ge\frac{2099}{13000}=.161461\ldots .       \tag{6.6}
\]

Even granting the fictitious comparison cost `Y^(4 beta)`, the natural
diagonal and the CA4 loss allow only

\[
 4\beta\le2(1-q)+\frac1{10},
 \qquad \beta\le\frac{1251}{13000}=.096230\ldots . \tag{6.7}
\]

There is no overlap.  At the full retained cutoff this optimistic ledger
already misses by `434/1625=.267076...`.  In reality the translated Gram
matrix is positive semidefinite but entrywise signed, so diagonal
reweighting is not monotone; replacing it by absolute values returns the
generic conductor deficit `16/33-1/10=127/330`.

This rules out the `ell^2`-tail-plus-supremum repair.  It does not rule out a
theorem whose right side tracks the actual weighted diagonal jointly.

### 6.6 Bounded absolute continuity is not enough

There is also a sharp proof-class countermodel.  Repeat the periodic node
motif

\[
 \{0,1,2,3,4,5,6,8,16\}\pmod {18}.
\]

Its gaps are `(1,1,1,1,1,1,2,8,2)`, and its cyclic Voronoi masses are
`(3/2,1,1,1,1,1,3/2,5,5)`.  Relative to uniform natural weights, the
density ratio lies exactly in `[1/2,5/2]`.  Nevertheless the natural cell
Fourier factor vanishes at harmonics `2,3,4`, while the hat factor at
harmonic `2` has modulus `.4454189...`.

For `M` repeated cells, the normalized repetition factor is a Dirichlet
kernel.  The three natural cell zeros cancel every resonance in the dyadic
band from harmonics `2` through `4`, giving natural fourth moment
`O(M^(-3))`; the surviving hat resonance gives fourth moment `Omega(1)`.
Both coefficient diagonals are `asymp M^(-1)`.  Taking
`M asymp Y/log Y` puts all pseudogaps below `Y^(163/1000)` and the resonant
height `T asymp Y/log Y` inside the CA4 band, while the CA4 right side is
`Y^(-1999/3250+o(1))`.

This refutes transference based only on density, retained gaps, coefficient
diagonals, and even uniform two-sided absolute continuity.  The nodes are
not asserted to be primes, so the construction does not refute actual-prime
CA4.  The finite cell identities are checked by the bounded-density
pseudonode verifier linked above.

## 7. Sign, resolution, and the only surviving route

An exact identity (2.5), inserted into (1.4) **before** estimating, preserves
the common translated kernel and therefore preserves the scale `H=Y^2/T`.
It also preserves the algebraic signs of the coefficients `c_k`.

Scalar `HL*(4)` information does not estimate that joint sum.  To use a
scalar bound for each term, one must take an absolute value in the component
index, producing (2.6); (5.7) then violates the budget.  Fejer positivity or
a nonnegative majorant cannot restore the lost inter-component signs.

Suppose instead that an exact, residual-free decomposition and a future
theorem supply perfect `ell^2` recombination across `K` components.  From
(5.7), its recombination norm is
still at least

\[
 \frac{(\log Y)^{-4}}{\sqrt K}.                    \tag{7.1}
\]

Every `K=Y^(o(1))` decomposition therefore remains too large.  To reach
(0.1) by orthogonality alone would require at least

\[
 K\ge Y^{2(5249/6500)-o(1)}
   =Y^{5249/3250-o(1)},                            \tag{7.2}
\]

together with a square-function theorem for all of their cross-correlations.
That theorem would be substantially stronger than scalar `HL*(4)` and would
already contain the missing selector-sensitive cancellation.

Accordingly the honest surviving target is:

> Prove a vector-valued, mask-sensitive shifted-semiprime theorem for the
> whole signed decomposition at once, with diagonal norm tied to
> `sum lambda_p^2`, while retaining the common translated kernel.

That is new mathematics.  Calling it a natural-mask transference adapter
would hide the open edge rather than remove it.

## 8. Frozen finite replay

The accompanying script was run only at the four centers already frozen by
the HT-HAT preregistration.  It recomputed (1.1), the natural
`Lambda(p)/sqrt(p)` shell vector, the witness (5.1), and the exact budget
exponent `5249/6500`.

| `Y` | primes | retained support | `V(lambda)` | `V(nu)` | `V(lambda)^2 / Y^(-5249/6500)` |
|---:|---:|---:|---:|---:|---:|
| 512.5 | 33 | 12 | .99595 | .003986 | 152.99 |
| 1024.5 | 59 | 18 | .65835 | .002408 | 116.95 |
| 2048.5 | 104 | 38 | .73350 | .001357 | 254.05 |
| 4096.5 | 198 | 76 | .86694 | .000767 | 621.07 |

The identity `b^T lambda=V(lambda)` held to at worst
`2.3e-16`, with `||b||_infinity=2`.  These values are diagnostics only.  The
asymptotic conclusion comes from Theorem 4.1 and the dual proof (5.1)--(5.7),
not from the finite trend.

## 9. Decision-tree update

| Claim | Status |
|---|---|
| exact positive natural-square decomposition | **REFUTED except for the tautological hat atom** |
| signed/mixed scalar natural-form adapter within the `Y^.1` budget | **REFUTED by (5.7)** |
| black-box scalar import of Alpoge--Furman-style `HL*(4)` through interval/smooth atoms | **REFUTED** |
| vector-valued selector-sensitive shifted correlation | **OPEN; not ruled out** |
| `CA4(163/1000,1/10)` | **OPEN** |
| `DPA_P(.019)` and `LTRAD_P(.0189,.001)` | **OPEN, independently** |
| contemplated uniform strip / RH | **OPEN** |

The maximum-information conclusion is therefore decisive but narrow:
natural `Lambda*Lambda` correlations are not a plug-compatible input.  The
next theorem must see the adjacent-gap mask jointly; no scalar partition can
hide that requirement within the available fixed-power budget.
