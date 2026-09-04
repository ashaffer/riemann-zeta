# Global Euler--Poisson coercivity attempt and sparse-surgery audit

Date: 2026-09-02  
Status: exact reductions, an unconditional Euler deformation, and a
synthetic ordinary-prime countermodel; **no uniform zero-free strip and no
proof of RH**  
Passport:
[`zeta23_global_parity_typeii_strip_preflight_v1.json`](context/zeta23_global_parity_typeii_strip_preflight_v1.json)

## 0. Outcome

The attempted global coercivity argument does not prove the target

\[
 \epsilon\{B_{U,U}(x)-Z_{U,U}(x)\}
 \ge -C x^{1/2-\eta}.                                    \tag{0.1}
\]

It does produce four durable conclusions.

1. A **Chebotarev-sparse positive Euler surgery** can preserve an arbitrary
   finite zeta head, agree with zeta away from a prime set of arbitrarily
   small density, keep its Dirichlet coefficients positive and its
   generalized von Mangoldt weights nonnegative (strictly positive on prime
   powers), satisfy both natural PNTs, and make
   `Lambda_L * 1` uniformly as close to `log` as desired, while planting a
   prescribed zero pair at `1-d +/- i gamma`.  Therefore none of those
   properties, separately or together, can supply the missing coercivity.
2. A uniform coefficient discrepancy of order `p^(-k delta)` is a sharp
   worst-case pointwise sufficient threshold for divisor stability in
   `Re(s)>1-delta`.  The sparse surgery reaches its boundary sharply; this is
   not a necessary condition for every structured pair of Euler products.
3. The positive Euler--Jordan deformation

   \[
    a_z(n)=\prod_{p\mid n}(1-p^{-z}),\qquad
    \sum_n a_z(n)n^{-s}=\frac{\zeta(s)}{\zeta(s+z)},       \tag{0.2}
   \]

   has the R95 von Mangoldt ramp as its boundary derivative.  On each zero
   carrier, its apparent `x^(-z)` improvement is canceled exactly by the pole
   translation `rho -> rho-z`.  This exponent-conservation calculation does
   not by itself provide a fixed saving.
4. In the functional-equation coordinate, a strip of width `delta` is
   equivalent to positive backward-Poisson deconvolution.  The finite-cutoff
   arithmetic formula requires the jointly renormalized all-prime weights
   `Lambda(n)n^(-1+delta)`.  Positivity before deconvolution is insufficient;
   positivity after deconvolution is the target itself.

The attempted combination therefore closes several direct inferences rather
than the strip.  Any successor must use at least one **zeta-specific datum**
which the sparse surgery does not retain.  The leading candidates are exact
all-prime equality and the exact completed functional equation, possibly
coupled in one correlation theorem; the countermodel does not prove that
both are individually necessary.  Another argument using only positive
smoothing, formal Selberg identities, density-one comparison, and
fixed-interior critical estimates is not enough.

## 1. The target and the local-predecessor correction

For fixed `ell>0`, `0<theta<3/8`, and `U=floor(x^theta)`, R68 proves

\[
 C_\ell(\log x)=B_{U,U}(x)-Z_{U,U}(x)+o(1),               \tag{1.1}
\]

where

\[
 B_{U,U}(x)=\sum_{d>U}\sum_{r>U}
 \mu(d)\beta_U(r)d^{-1/2}r^{-1/2}
 \Phi_\ell\!\left(\log\frac{x}{dr}\right),              \tag{1.2}
\]

\[
 \beta_U(r)=\sum_{\substack{b\mid r\\b>U}}\Lambda(b),    \tag{1.3}
\]

and `Z` contains both the pole-scale and critical zero-mode centerings.  If
either orientation of (0.1) held with fixed `eta>0`, the audited Landau
adapter would give

\[
 \zeta(\rho)=0\quad\Longrightarrow\quad
 \Re\rho\le 1-\eta.                                      \tag{1.4}
\]

This is not a newly discovered fixed-box reduction.  R67 and R68 already
contained the fixed-box and complete Type-II coordinates.  The September 2
Jordan/filter audit correctly classified the detector as strip-equivalent,
but its original novelty table understated these local predecessors.  The
originating report, passport, context audit, and R177 registry row are
corrected together with this report.

The passport forbids precisely the simplifications which destroy (1.1):

- splitting the cofactor sum into independently bounded rectangles;
- dropping `I_0` or the moving-cutoff boundary;
- taking absolute values before all cofactor cancellations occur;
- choosing the sign or smoothing order after seeing `x`; or
- importing a fixed-power Mertens bound through an inverse-zeta norm.

## 2. Chebotarev-sparse positive Euler surgery

The following is a synthetic ordinary-prime theorem.  It is not a
counterexample to a theorem about the actual zeta function and it has no
exact zeta functional equation.  It strengthens the positive Euler-product
model in Section 9.2 of the endpoint-flat Jordan report: instead of modifying
every sufficiently large prime, it modifies an arbitrarily sparse
Chebotarev class and adds the uniform divisor-identity estimate (2.3).

### Theorem 2.1

Fix

\[
 0<d<1,\qquad \gamma\ne0,
\]

a finite prime cutoff `H`, and `eta,epsilon>0`.  There are

- a set `S` of ordinary primes of natural density less than `eta`;
- a cutoff `P>=H`; and
- an ordinary Euler product `L(s)`

such that:

1. every Dirichlet coefficient `a_L(n)` is strictly positive and
   `a_L(n)<<_tau n^tau` for every `tau>0`;
2. every generalized von Mangoldt coefficient `Lambda_L(p^k)` is strictly
   positive;
3. the Euler factor equals zeta's factor for every `p<=H` and every
   `p notin S`;
4. `L` is meromorphic in a half-plane containing `1-d +/- i gamma` and has
   zeros at those two points;
5. for some `R_L>0`,

   \[
    \sum_{n\le x}\Lambda_L(n)\sim x,
    \qquad
    \sum_{n\le x}a_L(n)\sim R_Lx;                         \tag{2.1}
   \]

6. its local logarithmic weights obey

   \[
    \sup_{p,k}\frac{|\Lambda_L(p^k)-\Lambda(p^k)|}
                         {\log p}\le 2q P^{-d};            \tag{2.2}
   \]

7. and, for every integer `n>=2`,

   \[
    |(\Lambda_L*\mathbf1)(n)-\log n|
    <\epsilon\log n.                                     \tag{2.3}
   \]

Here `q` is a prime chosen larger than `eta^(-1)`.

#### Construction and proof

Choose a cyclic extension `K/Q` of prime degree `q`, and let `S` be the
unramified rational primes which split completely in `K`.  Chebotarev gives
`dens(S)=1/q<eta`.  Such extensions exist, for example as degree-`q`
subfields of suitable cyclotomic fields.  Because the Galois group has prime
order, every
unramified prime is either completely split or inert.  Thus

\[
 \zeta_K(w)=
 \prod_{p\in S}(1-p^{-w})^{-q}
 \prod_{p\notin S}^{\mathrm{unram}}(1-p^{-q w})^{-1}
 \prod_{p\mid D_K}\zeta_{K,p}(w).                        \tag{2.4}
\]

Consequently

\[
 Q_{K,P}(w):=\prod_{\substack{p\in S\\p>P}}(1-p^{-w})^q
             =\frac{B_{K,P}(w)}{\zeta_K(w)},              \tag{2.5}
\]

where explicitly

\[
 B_{K,P}(w)=
 \prod_{\substack{p\in S\\p\le P}}(1-p^{-w})^{-q}
 \prod_{p\notin S}^{\mathrm{unram}}(1-p^{-qw})^{-1}
 \prod_{p\mid D_K}\zeta_{K,p}(w).                        \tag{2.5a}
\]

The factor `B_(K,P)` is holomorphic and nonvanishing in `Re(w)>1/q`,
whereas `Q_(K,P)=B_(K,P)/zeta_K` is meromorphic there: zeros of
`zeta_K` may become poles.  At `w=1`, the simple pole of `zeta_K` gives
`Q_(K,P)` a simple zero.

Define

\[
 L(s)=\zeta(s)Q_{K,P}(s+d+i\gamma)Q_{K,P}(s+d-i\gamma).
                                                                    \tag{2.6}
\]

It is meromorphic for `Re(s)>1/q-d`.  At
`s=1-d+i gamma`, one shifted factor is `Q_(K,P)(1)=0`, while
the other is `Q_(K,P)(1+2i gamma)`, which is finite and nonzero by the
classical zero-free line for `zeta_K`.  The factor `zeta(s)` is finite there
and can only increase the zero order.  The conjugate argument handles the
other point, so both asserted points are zeros.

At a modified prime, put `zeta_p=p^(-s)` and `a=p^(-d-i gamma)`.  Its local
factor is

\[
 L_p(\zeta_p)=
 \frac{(1-a\zeta_p)^q(1-\bar a\zeta_p)^q}
      {1-\zeta_p}.                                       \tag{2.7}
\]

Choose `P` so large that

\[
 (1+P^{-d})^{2q}<2,
 \qquad
 \frac{2q P^{-d}}{1-P^{-d}}<\epsilon.                    \tag{2.8}
\]

Write the numerator of (2.7) as `sum_(j=0)^(2q)b_j zeta_p^j`.
The coefficient of `zeta_p^n` in (2.7) is

\[
 c_n=\sum_{j\le\min(n,2q)}b_j.                           \tag{2.9}
\]

For `n<2q`,

\[
 |c_n-1|\le (1+p^{-d})^{2q}-1<1,                         \tag{2.10}
\]

and `c_n` is real.  For `n>=2q`,

\[
 c_n=|1-a|^{2q}>0.                                       \tag{2.11}
\]

This proves positivity of every local and global Dirichlet coefficient;
also `c_n<2`, so `a_L(n)<=2^(omega(n))<<_tau n^tau`.

Logarithmic differentiation gives, at modified primes,

\[
 \frac{\Lambda_L(p^k)}{\log p}
 =1-2q p^{-kd}\cos(k\gamma\log p),                       \tag{2.12}
\]

and gives `1` elsewhere.  Bernoulli's inequality and (2.8) give
`2qP^(-d)<1`, so (2.12) is positive and proves (2.2).

Set

\[
 R_L=Q_{K,P}(1+d+i\gamma)Q_{K,P}(1+d-i\gamma)
    =|Q_{K,P}(1+d+i\gamma)|^2>0.                          \tag{2.12a}
\]

For `Re(s)>1`, the identities

\[
 L(s)=\sum_{n\ge1}\frac{a_L(n)}{n^s},\qquad
 -\frac{L'}{L}(s)=\sum_{n\ge1}\frac{\Lambda_L(n)}{n^s}  \tag{2.12b}
\]

converge absolutely; the local estimates above give `a_L(n)<<_tau n^tau`
and `0<=Lambda_L(p^k)<<_q log p`.  On `Re(s)=1` the two shifted `Q`
factors are absolutely convergent and nonvanishing, and their
logarithmic-derivative series converge absolutely.  Therefore
`L(s)-R_L/(s-1)` extends continuously across that line.  The classical
zero-free line for `zeta` also makes
`-L'(s)/L(s)-1/(s-1)` continuous there.  Wiener--Ikehara, applied
separately to the two nonnegative coefficient systems, proves (2.1).

Finally, `Lambda*1=log` and (2.12) imply

\[
\begin{aligned}
 |((\Lambda_L-\Lambda)*\mathbf1)(n)|
 &\le 2q\sum_{\substack{p^k\mid n\\p\in S,\ p>P}}
       (\log p)p^{-kd}\\
 &\le \frac{2q P^{-d}}{1-P^{-d}}\sum_{p\mid n}\log p
 \le \frac{2q P^{-d}}{1-P^{-d}}\log n,
\end{aligned}                                             \tag{2.13}
\]

which is (2.3).

### Corollary 2.2: what this falsifies

Let `b_L` denote the Dirichlet-convolution inverse of `a_L`.  The following
data do not imply a positive strip width uniformly over this model class:

\[
\begin{gathered}
 a_L(n)>0,\quad \Lambda_L(n)\ge0,\quad
 \Lambda_L(p^k)>0,\quad
 \text{both PNT normalizations},\\
 \text{an arbitrarily long exact zeta head},\quad
 \text{density-}(1-\eta)\text{ exact prime agreement},\\
 |\Lambda_L*1-\log|\le\epsilon\log,\quad
 a_L*b_L=\delta_1,\quad \Lambda_L*a_L=a_L\log,
\end{gathered}                                             \tag{2.14}
\]

even when all are imposed together.  Indeed, for any proposed width
`Delta>0`, choose `0<d<Delta`.  The model also retains the formal
self-relative Selberg identities and positivity of convolution powers.
This rules out proof mechanisms using only those inputs.  It does not rule
out exact zeta arithmetic or the completed functional equation.

## 3. A sharp worst-case pointwise coefficient-stability threshold

### Proposition 3.1

Let `delta>0`, and let `L_1,L_2` be nonzero meromorphic functions in
`Re(s)>1-delta` whose Euler logarithmic-derivative expansions hold in
`Re(s)>1`.  If

\[
 |\Lambda_{L_1}(p^k)-\Lambda_{L_2}(p^k)|
 \le C(\log p)p^{-k\delta},                               \tag{3.1}
\]

then `L_1` and `L_2` have the same zero/pole divisor in
`Re(s)>1-delta`.

#### Proof

The coefficient bound makes the series

\[
 -\frac{L_1'}{L_1}(s)+\frac{L_2'}{L_2}(s)
 =\sum_{p,k}\frac{\Lambda_{L_1}(p^k)-\Lambda_{L_2}(p^k)}
                    {p^{ks}},                             \tag{3.2}
\]

holomorphic because `Re(s)+delta>1`.  In `Re(s)>1` it equals the displayed
difference of logarithmic derivatives.  The meromorphic identity theorem
extends that equality to the full half-plane.  Hence the difference is
holomorphic there, and equality of logarithmic-derivative residues gives
equality of divisors.

The exponent-to-half-plane relation is sharp in the strip-relevant range.
Indeed, for any `0<d<delta<1`, choose the degree `q` large enough that the
model continues throughout `Re(s)>1-delta`, and choose `gamma` outside the
countable set for which `zeta(1-d+i gamma)=0`.  Theorem 2.1 then has
discrepancy `O((log p)p^(-kd))` but a genuinely new zero at
`1-d+i gamma`, strictly inside `Re(s)>1-delta`.  At `d=delta` the same
construction saturates the boundary `Re(s)=1-delta`.  Thus (3.1) is a
sharp worst-case pointwise sufficient threshold, not a characterization:
larger structured discrepancies can cancel without changing a divisor.

Separately, if two such functions continue meromorphically to
`Re(s)>1/2`, have exactly the same prime layer, and both satisfy
`|Lambda_L(p^k)|<<log p` for `k>=2`, their logarithmic-derivative difference
over `k>=2` converges absolutely in `Re(s)>1/2`; their divisors agree there.
This is useful discrimination, but it does not provide a comparison
function with known divisor and zeta's exact prime layer.

## 4. The functional-equation coordinate is backward Poisson flow

Put

\[
 p_a(t)=\frac{a}{\pi(a^2+t^2)},\qquad p_0=\delta_0,        \tag{4.1}
\]

and use the Fourier convention
`hat(f)(u)=integral f(t)e^(-itu)dt`, so `hat(p_a)(u)=e^(-a|u|)`.
Here

\[
 \xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

The Hadamard expansion, with zeros repeated by multiplicity, and the
classical theorem `zeta(s) \ne 0` on `Re(s)=1` give the locally absolutely
convergent positive sum

\[
 P(t):=\frac1\pi\Re\frac{\xi'}{\xi}(1+it)
      =\sum_\rho p_{1-\beta}(t-\gamma)>0,                 \tag{4.2}
\]

where `rho=beta+i gamma`.

### Theorem 4.1: Poisson factorization criterion

For fixed `0<delta<1/2`, the following are equivalent:

1. every nontrivial zero obeys `beta<=1-delta`;
2. there is a positive Radon measure `Q_delta` satisfying

   \[
    \int_{\mathbb R}\frac{dQ_\delta(u)}{1+u^2}<\infty     \tag{4.3}
   \]

   and

   \[
    P=p_\delta*Q_\delta.                                  \tag{4.4}
   \]

If the strip holds, one may take

\[
 Q_\delta=
 \sum_{\substack{\rho\\1-\delta-\beta>0}}
 p_{1-\delta-\beta}(t-\gamma)\,dt
 +\sum_{\substack{\rho\\1-\delta-\beta=0}}\delta_\gamma.
                                                                    \tag{4.5}
\]

Functional-equation symmetry also gives `beta>=delta`, so the strictly
positive Cauchy widths in the first sum lie in `(0,1-2delta]`; the zero
widths are the atoms in the second sum.  The identity

\[
 \int_{\mathbb R}\frac{p_a(t-\gamma)}{1+t^2}\,dt
 =\frac{1+a}{(1+a)^2+\gamma^2}                            \tag{4.5a}
\]

and the standard zero count `N(T)=O(T log T)` prove the weighted finiteness.

Conversely, the convolution in (4.4) is holomorphic for
`|Im(z)|<delta`.  But the complexification

\[
 {\cal P}(z)=\frac1{2\pi}
 \left\{\frac{\xi'}{\xi}(1+iz)+
             \frac{\xi'}{\xi}(1-iz)\right\}              \tag{4.6}
\]

has, for a zero of multiplicity `m` with `beta>1-delta`, a pole at

\[
 z=\gamma+i(1-\beta),                                     \tag{4.7}
\]

inside that strip, with residue `m/(2 pi i)`.  The second term in (4.6) is
evaluated there at `2-beta-i gamma`, in `Re(s)>1`, so it is holomorphic and
cannot cancel the pole.  This proves the reverse implication.

This is a Herglotz/Poisson form of known xi-positivity and shifted-Weil
criteria, not a claimed literature novelty.

### Exact finite-cutoff arithmetic identity

For `epsilon>0`, let

\[
 P_\epsilon(t)=\pi^{-1}\Re\frac{\xi'}{\xi}
                              (1+\epsilon+it).
\]

Then `P_epsilon=p_epsilon*P`.  Fix real even smooth functions `chi,theta`
with values in `[0,1]`, where `chi=1` on `[-1,1]`, `chi=0` outside
`[-2,2]`, `theta=0` on `[-1,1]`, and `theta=1` outside `[-2,2]`.  Put

\[
 \chi_R(u)=\chi(u/R)\theta(Ru),\qquad
 m_{a,R}(u)=\chi_R(u)e^{a|u|}.                           \tag{4.7a}
\]

Thus `chi_R` is uniformly bounded, is supported in `|u|<=2R`, vanishes in
`|u|<=1/R`, equals one when `2/R<=|u|<=R`, and tends to one at every
nonzero frequency.  The symbol `m_(a,R)` is smooth and compactly supported.
Let `T_(a,R)` be its Fourier multiplier (equivalently, convolution with its
Schwartz inverse Fourier transform).  Since `D=-i d/dt` has Fourier symbol
`u`, one may also write `T_(a,R)=chi_R(D)e^(a|D|)`.  Define

\[
 Q_{\delta,R}:=T_{\delta+\epsilon,R}P_\epsilon
               =T_{\delta,R}P.                            \tag{4.8}
\]

Write `s=1+epsilon+it` and define the exact pole/gamma-factor contribution

\[
 A_\epsilon(t)=\Re\left[
 \frac1s+\frac1{s-1}-\frac12\log\pi
 +\frac12\frac{\Gamma'}{\Gamma}(s/2)\right].              \tag{4.9}
\]

The Euler series gives

\[
 \boxed{
 \pi Q_{\delta,R}
 =\chi_R(D)e^{(\delta+\epsilon)|D|}A_\epsilon
 -\sum_{n\ge2}\Lambda(n)n^{-1+\delta}
        \chi_R(\log n)\cos(t\log n).}                     \tag{4.10}
\]

For each finite `R`, both terms in (4.10) are tempered, but for `delta>0`
their separate `R -> infinity` limits are not: the prime-comb mass up to
frequency `U` grows like `e^(delta U)`, and the completed archimedean term
has the compensating growth.  Only their joint renormalization is meaningful.

The finite-cutoff objects `Q_(delta,R)` need not themselves be positive.
To recover Theorem 4.1 one must also control the shrinking zero-frequency
hole and prove convergence to a positive measure in a topology controlling
the weight `(1+t^2)^(-1)`, together with the limiting identity
`P=p_delta*Q_delta`.  Mere distributional convergence is
insufficient: `R^2 delta_R -> 0` in tempered distributions, while
`p_delta*(R^2 delta_R)(t) -> delta/pi` at each fixed `t`.  Mass can escape to
infinity while retaining a nonzero Poisson trace.  With this weighted
tightness and identity, positive convergence is
exactly the strip assertion.  Unconditional positivity of `P` does not
propagate backward.  Even a symmetric off-strip zero quartet has `P>0` on
the line `Re(s)=1` but no positive `delta`-deconvolution.

## 5. The positive Euler--Jordan deformation

For real `z>0`, define

\[
 a_z(n)=\sum_{d\mid n}\mu(d)d^{-z}
       =\prod_{p\mid n}(1-p^{-z})
       =\frac{J_z(n)}{n^z}.                               \tag{5.1}
\]

Then `0<a_z(n)<=1` and

\[
 Q_z(s):=\sum_{n\ge1}\frac{a_z(n)}{n^s}
         =\frac{\zeta(s)}{\zeta(s+z)},\qquad \Re s>1.    \tag{5.2}
\]

It has the cocycle law

\[
 Q_{z+w}(s)=Q_z(s)Q_w(s+z),                               \tag{5.3}
\]

equivalently

\[
 a_{z+w}(n)=\sum_{d\mid n}a_z(n/d)d^{-z}a_w(d).           \tag{5.4}
\]

At the boundary,

\[
 a_0(n)=\mathbf1_{n=1},\qquad
 \left.\partial_z a_z(n)\right|_{z=0}
 =-\sum_{d\mid n}\mu(d)\log d=\Lambda(n).                \tag{5.5}
\]

The identities (5.1)--(5.5) are classical Jordan-totient algebra.

### Theorem 5.1: explicit unconditional summatory remainder

Let

\[
 A_z(x)=\sum_{n\le x}a_z(n),\qquad c_z=\frac1{\zeta(1+z)}.
\]

Then

\[
 A_z(x)-c_zx
 =-\sum_{d\le x}\mu(d)d^{-z}\{x/d\}
  -x\sum_{d>x}\mu(d)d^{-1-z}.                             \tag{5.6}
\]

Consequently, for every real `x>=1`,

\[
 |A_z(x)-c_zx|\le
 \begin{cases}
  2+x^{1-z}\left(z^{-1}+(1-z)^{-1}\right),&0<z<1,\\
  3+\log x,&z=1,\\
  \zeta(z)+1+z^{-1},&z>1.
 \end{cases}                                              \tag{5.7}
\]

Equation (5.6) follows by expanding (5.1), interchanging the finite divisor
sum, and completing `sum mu(d)d^(-1-z)` to `1/zeta(1+z)`.
The bounds use only `|mu|<=1`, so (5.7) is unconditional.

## 6. The exact R95 boundary tangent

Put

\[
 w(y)=2y-1,\qquad
 I(x)=\int_1^xw(u/x)\,du=1-x^{-1},                        \tag{6.1}
\]

and

\[
 E_z(x)=\sum_{n\le x}a_z(n)w(n/x)-c_zI(x).                \tag{6.2}
\]

Since `c_z=z+O(z^2)` at zero, (5.5) gives

\[
 \left.\partial_zE_z(x)\right|_{z=0}
 =R(x):=\sum_{n\le x}\Lambda(n)(2n/x-1)-1+x^{-1}.        \tag{6.3}
\]

This is exactly the bounded one-front R95 ramp.

Let

\[
 K(y)=\sum_{m\le y}w(m/y).
\]

For `M=floor(y)`, direct summation gives

\[
 K(y)=\frac{M(M+1-y)}y=\frac{M(1-\{y\})}{y},
 \qquad 0\le K(y)\le1.                                  \tag{6.4}
\]

Expanding `a_z` in (6.2) yields

\[
 E_z(x)=\sum_{d\le x}\mu(d)d^{-z}K(x/d)-c_zI(x),         \tag{6.5}
\]

and differentiation yields the exact Möbius form

\[
 \boxed{
 R(x)=-\sum_{d\le x}\mu(d)\log d\,K(x/d)-I(x).}         \tag{6.6}
\]

Thus the desired one-sided R95 theorem is literally one-sided weighted
Möbius cancellation against a fixed positive sawtooth kernel.  The identity
does not create that cancellation.

The Mellin transform, initially for `Re(s)>1`, is

\[
 \int_1^\infty E_z(x)x^{-s-1}\,dx
 =H(s)\left\{\frac{\zeta(s)}{\zeta(s+z)}
              -\frac{c_z}{s-1}\right\},
 \qquad H(s)=\frac{s-1}{s(s+1)}.                          \tag{6.7}
\]

### Theorem 6.1: exact fixed-`z` strip adapter

Define the countable difference set

\[
 {\cal D}=\{\rho-\rho'\in\mathbb R_{>0}:
              \zeta(\rho)=\zeta(\rho')=0\}.              \tag{6.8}
\]

Thus only pairs of zeros on the same horizontal line contribute to
`{\cal D}`.  Fix `0<z<1` with `z notin {\cal D}`.  If there are fixed
`q>=0`, `C<infinity`, and `X` such that either

\[
 E_z(x)\ge-Cx^q\qquad\hbox{or}\qquad E_z(x)\le Cx^q       \tag{6.9}
\]

holds for every `x>=X`, then

\[
 \zeta(\rho)=0\quad\Longrightarrow\quad
 \Re\rho\le q+z.                                         \tag{6.10}
\]

Indeed, `z notin {\cal D}` ensures that a zero `rho` gives a pole of (6.7) at
`rho-z`.  For the lower orientation, `E_z(x)+Cx^q` is eventually
nonnegative; for the upper orientation, use `Cx^q-E_z(x)`.  Changing either
density on a compact interval adds an entire function.
Landau's theorem would force a real singularity if a pole had real part
larger than `q`, but (6.7) is regular at every real `s>0`: the centering
cancels the pole at `s=1`, the ratio `Q_z` vanishes at `s=1-z` so the full
centered transform is regular there, and zeta has no real zero in `(0,1)`.
The elementary bound below gives finite
exponential order, so Landau applies.

The quantifier is important.  If an estimate is proved only at one
preselected `z in {\cal D}`, (6.10) follows only for zeros not canceled at
`rho-z`; one may not change `z` after proving the estimate.

Directly from (6.5) and `0<=K<=1`,

\[
 |E_z(x)|\le1+\sum_{d\le x}d^{-z}
 \le2+\frac{x^{1-z}}{1-z}.                               \tag{6.11}
\]

This has only the critical exponent `q=1-z`, which makes (6.10) the trivial
`beta<=1`.  The conclusion yields a positive strip precisely when
`q+z<1`; a fixed reserve below `1-z` is exactly the missing information.

## 7. The zero boundary layer and exponent conservation

Suppose `rho` is a zero of multiplicity `m` and, on an isolating disk around
`rho`,

\[
 \zeta(s)=(s-\rho)^mh(s),\qquad h(\rho)\ne0.              \tag{7.1}
\]

For an arbitrary fixed real `z`, put `s=rho-z+v`.  The exact local Laurent
form at `v=0` is

\[
 H(s)Q_z(s)=\frac{F_z(v)}{v^m},\qquad
 F_z(v)=H(\rho-z+v)
        \frac{\zeta(\rho-z+v)}{h(\rho+v)}.                \tag{7.1a}
\]

If `zeta(rho-z) \ne 0`, the coefficient of `v^(-k)` is
`F_z^((m-k))(0)/(m-k)!`.  If the numerator has a zero of multiplicity `r`,
the pole order falls to `max(m-r,0)`.  This is the arbitrary-`z`
noncancellation statement used in Theorem 6.1.

Take `z>0` small enough that both `rho-z+v` and `rho+v` stay in that disk,
put `s_0=rho-z`, and write `v=s-s_0`.  Then

\[
 Q_z(s_0+v)
 =\left(\frac{v-z}{v}\right)^m
   \frac{h(\rho-z+v)}{h(\rho+v)}.                         \tag{7.2}
\]

If

\[
 G_z(v)=H(\rho-z+v)\frac{h(\rho-z+v)}{h(\rho+v)},         \tag{7.3}
\]

the coefficient of `v^(-k)` in `H(s)Q_z(s)` is

\[
 D_{k,z}=\sum_{j=k}^m {m\choose j}(-z)^j
             \frac{G_z^{(j-k)}(0)}{(j-k)!}.               \tag{7.4}
\]

Hence

\[
 D_{k,z}={m\choose k}(-z)^kH(\rho)+O_\rho(z^{k+1}),       \tag{7.5}
\]

and in particular

\[
 \operatorname*{Res}_{s=\rho-z}H(s)Q_z(s)
 =-mzH(\rho)+O_\rho(z^2).                                \tag{7.6}
\]

Under a licensed inverse-Mellin contour shift across this pole, its principal
part contributes the residue polynomial

\[
 x^{\rho-z}\sum_{k=1}^mD_{k,z}
              \frac{(\log x)^{k-1}}{(k-1)!}.             \tag{7.7}
\]

For this one fixed zero, differentiating at `z=0` restores
`-mH(rho)x^rho`, precisely its zero mode in the R95
logarithmic-derivative transform.  The constants in (7.5) are not uniform in
the height of `rho`, and this local calculation does not justify
differentiating or summing a global explicit formula term by term.

The scalar carrier

\[
 {\cal B}_{\beta,\gamma}(z,x)
 =z x^{\beta-z}\cos(\gamma\log x+\phi)                   \tag{7.8}
\]

makes the no-go transparent.  For every fixed `z>0` and `beta<=1`,

\[
 |{\cal B}_{\beta,\gamma}(z,x)|\le z x^{1-z},            \tag{7.9}
\]

but

\[
 \left.\partial_z{\cal B}_{\beta,\gamma}(z,x)
 \right|_{z=0}
 =x^\beta\cos(\gamma\log x+\phi).                        \tag{7.10}
\]

Therefore the critical estimate `z x^(1-z)`, considered in isolation, does
not control the boundary tangent, even though the exact Euler--Jordan family
which motivated it has positive coefficients.  A sufficient reserve would
have the fully uniform form: there are
fixed `C,eta,z_0,X>0` such that, for every `x>=X` and `0<z<=z_0`,

\[
 E_z(x)-E_0(x)\ge-Cz x^{1-\eta}                           \tag{7.11}
\]

or the reverse inequality.  With these quantifiers, dividing by `z` and
sending `z` to zero gives the desired R95 estimate.  If `C` or `X` depends
on `z`, that inference is invalid.  Equation (7.11) is therefore not an
easier consequence of positivity.

This is the precise scope of the boundary-layer no-go: critical fixed-`z`
bounds alone do not pass to a subcritical tangent bound.  The scalar carrier
(7.8) is sign-changing and does not itself obey the Euler cocycle, so it does
**not** refute every conceivable argument combining coefficient positivity
with the full cocycle law.  Such an argument remains admissible only if it
exploits aggregate constraints absent from the scalar carrier.  No such
constraint produced a subcritical bound in this attempt.

## 8. Why the audited direct Type-II parity transports stop

The product-preserving and product-changing parity templates recorded in the
current passport were tested against the R67--R74 ledgers.  The conclusions
below are scoped to those audited templates, not to every conceivable parity
transport.

1. A transport preserving the total product `d r` acts fiberwise and leaves
   the common Laurent mode with eigenvalue one.  It cannot damp (1.2).
2. In the audited product-changing templates, the transport creates the
   coherent prime--prime collar and the moving-cutoff boundary.  Their tested
   completions either restore the original aggregate or require a one-sided
   fixed-power estimate for a Möbius sum of the form (6.6).
3. Independent dyadic or cofactor estimates remove the zeta factor which
   reduces the zero singularity to a simple pole; the separated pieces have
   higher-order zero poles and are strictly harder.
4. The exact polar and `I_0` centers are not optional.  Dropping `I_0` would
   imply a false holomorphic continuation of `1/zeta` through known critical
   zeros.

Thus no new inequality for `B-Z` was obtained.  The exact identities merely
map the Type-II target to the same boundary-tangent obstruction.

## 9. Corrected decision tree

```text
uniform zero-free strip
|
+-- R68 complete centered Type-II aggregate
|     `-- one-sided fixed-power cancellation OPEN
|
+-- R95 fixed signed ramp
|     `-- one-sided weighted Mobius cancellation (6.6) OPEN
|
+-- Euler--Jordan interior deformation
|     +-- positivity and x^(1-z) bound PROVED
|     `-- any fixed reserve below 1-z OPEN / strip-strength
|
+-- completed xi / Poisson flow
|     +-- P>0 on Re(s)=1 PROVED
|     `-- positive backward deconvolution OPEN / strip-equivalent
|
+-- generic positive-Euler coercivity
|     `-- REFUTED by sparse surgery in its stated hypothesis class
|
+-- QP/Turan
|     +-- DPA_P(.019) OPEN
|     `-- LTRAD_P(.0189,.001) OPEN
|
`-- Weil architecture
      `-- zeta-specific adjacent-support propagation OPEN
```

There is no justified percentage of completion and no unique proved next
route.  Within the route attempted here, an admissible successor must turn at
least one discriminator absent from Theorem 2.1 into a nonlocal one-sided
inequality.  The most concrete discriminators are:

1. exact all-prime coefficients, with Proposition 3.1 identifying the
   `p^(-k delta)` stability scale;
2. the exact completed zeta functional equation; or
3. another target-conditioned zero/prime correlation not retained by the
   sparse surgery.

The countermodel licenses this disjunction, not the claim that all three are
necessary.  A candidate which simply asserts positivity of (4.8), (6.6), or
(0.1) has renamed the strip target.

## 10. Provenance and novelty labels

- The Jordan-totient identities (5.1)--(5.5) are `IMPORTED/CLASSICAL`.
  Generalized von Mangoldt derivatives are treated explicitly by
  [Banks--Sinha](https://arxiv.org/abs/2209.11768).
- The R95 tangent, multiplicity calculation, and exponent-conservation
  packaging are `PROJECT_SYNTHESIS`, with local predecessors in R67, R68,
  R95, and the reciprocal/Mertens audits.  No literature novelty is claimed.
- The Poisson factorization is `PROJECT_SYNTHESIS` overlapping the xi and
  shifted-Weil positivity literature, especially
  [Lagarias](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/en/publishing-house/journals-and-series/acta-arithmetica/all/89/3/110751/on-a-positivity-property-of-the-riemann-function),
  [Bombieri--Lagarias](https://www.sciencedirect.com/science/article/pii/S0022314X99923922),
  and [Suzuki](https://doi.org/10.48550/arXiv.1204.1827).
- Partial and cropped Euler products are established subjects; relevant
  predecessors include
  [Jurzak](https://arxiv.org/abs/math/0202273),
  [Takloo-Bighash](https://homepages.math.uic.edu/~rtakloo/euler-product.pdf),
  and
  [Gonzalez--Jimenez--Lario](https://arxiv.org/abs/1002.4373).
- The exact coefficient-side rigidity is elementary logarithmic-derivative
  continuation and is aligned with
  [Soundararajan's strong-multiplicity-one work](https://arxiv.org/abs/math/0210299).
- Theorem 2.1 has a `LOCAL_PREDECESSOR` in the endpoint-flat report's
  all-tail positive Euler model.  Its sparse Chebotarev upgrade and uniform
  estimate (2.3) were not found as an exact bundle in the bounded
  primary-source search.  Their conservative label is
  `PROJECT_SYNTHESIS / NOVELTY_UNRESOLVED`, not `CANDIDATE_NEW`.  Failure to
  find a source cannot certify novelty.
- Current weighted-PNT sign and converse work, such as
  [Han](https://arxiv.org/abs/2505.23795),
  [Suzuki](https://arxiv.org/abs/2411.07436), and
  [Han's 2026 Liouville/Riesz criterion](https://arxiv.org/abs/2608.27130),
  reinforces the status of these one-sided estimates as zero detectors; it
  does not supply the missing estimate.

The dated search scope, queries, identifiers, and limitations are recorded
in
[`zeta23_global_euler_poisson_literature_audit_v1.json`](context/zeta23_global_euler_poisson_literature_audit_v1.json).

## 11. Trust and replay

The finite convolution identities, local coefficient inequalities, Mellin
multiplier calculations, and JSON artifacts are exactly replayable.  The
Landau, Chebotarev, zero-free-on-`Re(s)=1`, and Wiener--Ikehara inputs are
standard imported theorems.  The written analytic synthesis is unrefereed
and is not Lean-formalized.

No finite numerical trend is used to infer a strip.  The terminal status is

```text
Chebotarev-sparse Euler falsifier:       PROJECT-PROVED SYNTHETIC MODEL
Euler--Jordan summatory theorem:         PROJECT-PROVED / CLASSICAL ALGEBRA
Poisson factorization criterion:         PROJECT SYNTHESIS / TARGET-EQUIVALENT
one-sided R95 fixed-power estimate:      OPEN
one-sided complete Type-II estimate:     OPEN
uniform zero-free strip:                 OPEN
RH:                                      OPEN
```

Replay the finite identities with

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_global_euler_jordan_coercivity.py
```
