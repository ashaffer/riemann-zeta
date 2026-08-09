# R141 nonlinear tensor and regular Frobenius gate

## Status

R140 left two genuinely coefficient-specific possibilities:

```text
a signed prime/Type-II divisor estimate;
or an exceptionally cheap Frobenius mask.                         (0.1)
```

This report pushes both, including nonlinear differential expressions,
character--height tensors, matrix compression, and high-degree Galois
representations.  It proves the following.

1.  Reciprocal curvature

    ```text
    Q=A^2+A'=(1/F)''/(1/F),       A=-F'/F,                    (0.2)
    ```

    lowers a simple denominator zero from a double pole to a simple pole
    while retaining a double pole at a zeta zero.  Its Euler coefficients,
    however, have an exact negative-prime/positive-semiprime split.
2.  This sign loss is structural.  No constant quadratic differential
    calibration of positive Boolean logarithmic derivatives can cancel the
    double pole at one, keep a double zeta-zero pole, and have one-signed
    prime and semiprime coefficients.
3.  A concrete `2,-3,1` combination of three reciprocal curvatures is an
    exact divisor-order separator: the common auxiliary numerator and the
    pole at one lose their double parts, whereas every zeta zero retains a
    nonzero double part.  It still has both signs already on the prime layer.
4.  Character--height tensoring cancels Gamma and conductor terms exactly,
    but the ordinary critical-zero cloud can pay the entire target reserve.
    A general degree identity shows that its wrong-sign auxiliary mass cannot
    be diluted below the zeta mass.  Negative height coefficients necessarily
    make the zero kernel sign-changing.
5.  Matrix compression trades the number of auxiliary zero locations
    against entrywise Fourier mass but again stops at a square-root wall.
6.  A high-degree Galois regular representation gives a new exact scalar
    mask.  If `E/Q` is totally real Galois of degree `n`, then

    ```text
    A_E=(nD_zeta-D_(zeta_E))/(n-1)                            (0.3)
    ```

    has nonnegative coefficients bounded by two, deletes every prime which
    splits completely in `E`, cancels Gamma degree, and charges only
    `log rd(E)` rather than `log D_E` or the degree.
7.  This last mechanism would prove a fixed strip from fields in which every
    `p<=X` splits, with

    ```text
    log rd(E)=o(X^kappa),                 kappa<1/2,           (0.4)
    ```

    together with local nonvanishing of `zeta_E/zeta`.  The best elementary
    construction found here has instead

    ```text
    log rd(E)<=(log 2+o(1))X/log X.                           (0.5)
    ```

    Under Dedekind GRH even (0.4) is impossible: the least nonsplit-prime
    theorem forces `log rd(E)>>sqrt(X)`.  Unconditional least-prime theorems
    do not reach that logarithmic scale.
8.  A non-Galois permutation character weakens complete splitting to
    Frobenius elements moving an exponentially small fraction of embeddings.
    This escapes least-nonsplit theorems, but no quantitative totally real
    realization with controlled root discriminant is known; Dedekind GRH
    again predicts a square-root obstruction.

Thus R141 does not prove a fixed strip and does not prove that no fixed strip
exists.  It does identify a new regular-representation reduction and an exact
nonlinear divisor separator.  Both repay their gain at a precise gate:

```text
reciprocal curvature                         EXACT
quadratic one-sign calibration               IMPOSSIBLE
2,-3,1 divisor-order separator               EXACT, SIGNED
character--height Gamma/conductor debt       REMOVED
ordinary zero-density closure                IMPOSSIBLE
regular-representation Frobenius mask        EXACT
sub-square-root split-field realization      OPEN / GRH-FALSE
local auxiliary-zero avoidance               OPEN
low-support permutation-field realization    OPEN
fixed uniform zero-free strip                NOT PROVED
zeros approaching one                        NOT PROVED
```

Date: 2026-08-08.

Predecessor:
[`R140-DEGREE-ZERO-LOCALIZATION-AND-FROBENIUS-DICHOTOMY.md`](R140-DEGREE-ZERO-LOCALIZATION-AND-FROBENIUS-DICHOTOMY.md).

## 1. Reciprocal curvature: exact divisor and Euler algebra

Use the R138 quotient

```text
F=zeta L_(chi psi)/(L_chi L_psi),
A=-F'/F.                                                       (1.1)
```

Put `g=1/F`, so `A=g'/g`, and define

```text
Q=A^2+A'=g''/g.                                                (1.2)
```

Write

```text
a(p^v)=(log p)c_p(v),
c_p(v)=(1-chi(p)^v)(1-psi(p)^v),                              (1.3)
```

and set `a(n)=0` off prime powers.  Since

```text
A(s)=sum_(n>=2)a(n)n^(-s),                                    (1.4)
```

ordinary multiplication and differentiation give

```text
Q(s)=sum_(n>=2)q(n)n^(-s),
q(n)=(a*a)(n)-a(n)log n.                                      (1.5)
```

Consequently

```text
q(p^v)/(log p)^2
 =sum_(i=1)^(v-1)c_p(i)c_p(v-i)-v c_p(v),                    (1.6)

q(p^i q^j)
 =2(log p)(log q)c_p(i)c_q(j)>=0,          p!=q.              (1.7)
```

For the coprime quadratic pair, every active local alphabet has

```text
c_p(v)=C_p 1_(v odd),                   C_p in {2,4}.          (1.8)
```

Thus

```text
q(p^v)/(log p)^2
 =-C_p v,                         v odd;
 =(C_p^2/2)v,                     v even.                     (1.9)
```

The nonlinear operation has not destroyed arithmetic structure: it has
created an exact signed Morse boundary.  The one-prime layer is negative,
while every distinct-prime Type-II coefficient is positive.

Now let `z` be a divisor point and write

```text
g(s)=(s-z)^nu h(s),                 h(z)!=0.                  (1.10)
```

Direct differentiation gives

```text
Q(s)=nu(nu-1)/(s-z)^2
    +2nu[h'(z)/h(z)]/(s-z)+O(1).                              (1.11)
```

Therefore:

* a simple denominator zero of `F` has `nu=1`; its double pole cancels,
  although a generally nonzero simple pole remains;
* a denominator zero of multiplicity `N` leaves double coefficient
  `N(N-1)`;
* a numerator zero of multiplicity `M`, including a zeta zero, has
  `nu=-M` and double coefficient `M(M+1)`;
* at `s=1`, `nu=1`, and the remaining simple residue is `2u_1`, where

  ```text
  u_1=L'/L(1,chi)+L'/L(1,psi)-L'/L(1,chi psi)-gamma.          (1.12)
  ```

This is genuine order separation, but not complete removal of the auxiliary
divisor.

## 2. A one-sign obstruction for every quadratic calibration

The sign pattern in (1.9) is not an accident of `A^2+A'`.

Let `A_1,...,A_J` be positive Boolean logarithmic derivatives on a common
finite Galois group `G`, with class functions `phi_j>=0`.  Write

```text
Phi(x)=(phi_1(x),...,phi_J(x)),
u=|G|^(-1)sum_(x in G)Phi(x).                                 (2.1)
```

The vector `u` is both the residue vector at one and the negative residue
vector at an unshared zeta zero.  Consider the general constant quadratic
calibration

```text
P=A^T C A+b^T A'+ell^T A+holomorphic,          C=C^T.         (2.2)
```

At large unramified primes of Frobenius classes `x,y`,

```text
[p]P=-(log p)^2 b.Phi(x)+O(log p),
[pq]P=2(log p)(log q)Phi(x)^T C Phi(y),          p!=q.        (2.3)
```

Suppose these coefficients are nonnegative.  Chebotarev then forces

```text
b.Phi(x)<=0,                    Phi(x)^T C Phi(y)>=0          (2.4)
```

for all `x,y`.  Averaging yields

```text
b.u<=0,                         u^T C u>=0.                   (2.5)
```

Cancellation of the double pole at one requires

```text
u^T C u-b.u=0.                                                   (2.6)
```

Both terms in (2.6) have the same forced sign, so

```text
u^T C u=b.u=0.                                                   (2.7)
```

The double coefficient at a zeta zero is instead

```text
u^T C u+b.u,                                                     (2.8)
```

which also vanishes by (2.7).  Replacing `P` by `-P` proves the same result
for nonpositive coefficients.

### Theorem 2.1 -- quadratic one-sign obstruction

No constant quadratic differential calibration of positive Boolean
logarithmic derivatives can simultaneously

```text
have one-signed prime and semiprime coefficients;
cancel the double pole at s=1;
retain a double pole at an unshared zeta zero.                  (2.9)
```

Any successful reciprocal-curvature argument therefore needs a signed
prime-versus-Type-II estimate; algebra alone cannot restore positivity.

## 3. An exact `2,-3,1` divisor-order separator

The nonlinear construction nevertheless gives a sharper spectral object.
Take four independent pairwise-coprime even quadratic characters
`chi_1,...,chi_4`, put `theta=chi_1 chi_2 chi_3 chi_4`, and use the partitions

```text
P_2={12,34},       P_3={1,2,34},       P_4={1,2,3,4}.          (3.1)
```

Define

```text
F_m=zeta^(m-1)L_theta / product_(B in P_m)L_(chi_B),
A_m=-F_m'/F_m,
Q_m=A_m^2+A_m'.                                                (3.2)
```

Each `A_m` has the nonnegative sparse Boolean alphabet of R138.  Set

```text
calQ=2Q_2-3Q_3+Q_4.                                           (3.3)
```

For `t=m-1` the weights obey

```text
sum w_m=0,
sum w_m t(t-1)=0,
sum w_m t=sum w_m t^2=-1.                                    (3.4)
```

It follows immediately from (1.11) that

```text
pure L_theta zero:       double coefficient 0;
s=1:                     double coefficient 0;
zeta zero of order M:    double coefficient -M(M+1).         (3.5)
```

Simple denominator zeros leave only simple poles.  The remaining simple
pole at one can be removed by subtracting its symmetric principal part

```text
R[1/(s-1)-1/s],                                                (3.6)
```

without changing (3.5).  Thus `calQ` is an exact divisor-order separator.

It cannot be used with absolute positivity.  Already its prime class
function `2phi_2-3phi_3+phi_4` is `4` on the class `(1,1,-1,-1)` and `-8`
on `(-1,-1,1,1)`.  Chebotarev supplies infinitely many primes of both
types.  The required continuation is precisely a signed prime/Type-II
cancellation theorem for (1.5), not another algebraic calibration.

## 4. Character--height tensoring removes the old debt, not the zero cloud

For a nonnegative trigonometric polynomial

```text
P(theta)=a_0+sum_(k=1)^m a_k cos(k theta)>=0,                 (4.1)
```

the pair detector satisfies the exact prime inequality

```text
a_0 A_(chi,psi)(sigma)
 +sum_(k>=1)a_k Re A_(chi,psi)(sigma+ikT)>=0.                 (4.2)
```

Its completed divisor formula is

```text
Re A_(chi,psi)(s)
 =E(s)-Z_zeta(s)-Z_(chi psi)(s)+Z_chi(s)+Z_psi(s),            (4.3)
```

with no Gamma or conductor term.  Thus this tensor genuinely removes the
R88 archimedean debt.

Assume `a_k>=0`.  At `sigma=1+delta`, a hypothetical
`rho=1-epsilon+iT` contributes

```text
-a_1/(delta+epsilon)+O_P(T^(-2)),                             (4.4)
```

while the pole at one contributes `a_0/delta+O_P(1)`.  Since positivity of
`P` gives `a_1<=2a_0`, the largest target-minus-pole reserve is

```text
<=a_0(sqrt(2)-1)^2/epsilon.                                  (4.5)
```

But a denominator `L`-function whose zeros all obey `Re rho<=alpha<1`
still has Poisson mass

```text
Z_(chi,sigma)(T)=1/2 log(q_chi T)+O_sigma(1).                 (4.6)
```

Its ordinary critical cloud can therefore pay (4.5).  Averaging over pairs
multiplies the target and this bulk by the same factor.

There is also an exact degree obstruction.  For a normalized Boolean
detector

```text
A_phi=sum_S c_S D_(chi_S),       c_empty=1,       sum_S c_S=0, (4.7)
```

put `B_+=sum_(S!=empty,c_S>0)c_S` and
`B_-=sum_(c_S<0)|c_S|`.  Then

```text
B_-=1+B_+>=1.                                                   (4.8)
```

The wrong-sign auxiliary degree can never be diluted below the replicated
zeta degree, regardless of graph sparsity or Boolean arity.

Allowing negative height coefficients does not repair this.  A zero at
vertical displacement `y` is sampled through

```text
W_d(y)=sum_(k=0)^m a_k d/[d^2+(y-kT)^2].                      (4.9)
```

For fixed degree, `a_j<0` makes `W_d(jT)<0` for large `T`.  More generally,
if `W_d>=0` pointwise even with growing degree, a disjoint-cell Poisson-mass
argument gives

```text
B_- << (d/T)B_+.                                               (4.10)
```

Hence coefficients capable of cancelling a comparable smooth zero bulk
necessarily make the zero kernel sign-changing.  Marginal zero density no
longer controls it.

## 5. Haar doubling and the return to zeta

Haar averaging a quadratic pair gives exactly

```text
E_(chi,psi) A_(chi,psi)(s)
 =D_zeta(s)-D_zeta(2s)=:B(s).                                 (5.1)
```

Therefore the height tensor obeys

```text
F_P(sigma,T)>=F_P(2sigma,2T).                                 (5.2)
```

The apparent child zeros at height `2T` are sampled at real part
`2sigma>2`; an ordinary critical zero there has weight `O(1/epsilon)` and
can pay for a near-one parent.  It does not seed a stronger next generation.

The full cascade is exact.  Put

```text
B_j(s)=B(2^j s)=D_zeta(2^j s)-D_zeta(2^(j+1)s).               (5.3)
```

The `B_j` have disjoint prime-power supports, classified by
`v_2(v)=j`.  Thus `sum_j c_jB_j` has nonnegative prime coefficients exactly
when `c_j>=0`.  Cancelling every intermediate child requires constant
`c_j`, and then

```text
sum_(j=0)^J B_j(s)=D_zeta(s)-D_zeta(2^(J+1)s),
sum_(j>=0)B_j(s)=D_zeta(s).                                   (5.4)
```

The infinite tensor merely reconstructs classical zeta positivity.
Cancelling the pole requires `c_0=0`, which simultaneously deletes the
target.

## 6. Matrix compression and its rank dichotomy

For quadratic characters define

```text
A_ij=D_zeta+D_(chi_i chi_j)-D_(chi_i)-D_(chi_j).              (6.1)
```

At a prime power its coefficient matrix is

```text
u_p u_p^T,                    u_(p,i)=1-chi_i(p)^v.            (6.2)
```

Let `W` be the orthogonal complement of the span of the head vectors
`u_p`, and let `P_W` be its projection.  Then the trace after compression
has nonnegative scalar coefficient

```text
phi_p=u_p^T P_W u_p,                                           (6.3)
```

which vanishes throughout the head.  Its zeta source coefficient is

```text
tr(P_W)+||P_W 1||^2.                                          (6.4)
```

For a collision-free or Sidon character family, a product-character zero is
locally low rank, but its remote scalar weights are `2(P_W)_ij`.  A generic
dense projection has

```text
||P_W||_(entry,1)<=m||P_W||_F asymp m^(3/2),                 (6.5)
```

against source size `asymp m`.  The square-root loss returns.  A full,
collision-rich character group recombines (6.3) into the complement mask,
but a single product-character zero then acts by a permutation and becomes
full rank.  Finally, a sparse `O(m)` entrywise projection requires repeated
or shortly dependent head signatures.  Two repeated signatures already
give a nontrivial quotient character equal to `+1` at every head prime --
exactly the exceptional least-Frobenius mask.

Determinants and exterior powers inherit the same smallest-singular-value
gate.  Rank compression changes its language, not its exponent.

## 7. The high-degree regular-representation mask

Let `E/Q` be totally real Galois of degree `n>1`.  Write
`D_K=-zeta_K'/zeta_K`, and define

```text
H_E=zeta_E/zeta,
A_E=(nD_zeta-D_E)/(n-1)
   =D_zeta-(1/(n-1))D_(H_E).                                  (7.1)
```

The Aramata--Brauer theorem makes `H_E` entire.  At an unramified prime
with Frobenius `g_p`, the regular-character trace gives

```text
[A_E]_(p^v)
 =n/(n-1)[1-1_(g_p^v=1)]>=0.                                 (7.2)
```

The analogous ramified coefficient is also nonnegative because it is `n`
minus the trace on inertia invariants.  In particular

```text
0<=[A_E]_(p^v)<2,                                             (7.3)
```

and if `p` splits completely in `E`, every power `p^v` disappears.

For irreducible Artin representations `rho`,

```text
chi_reg=1+sum_(rho!=1)(dim rho)chi_rho.                        (7.4)
```

Thus the normalized Fourier weights are

```text
a_1=1,                 a_rho=-(dim rho)/(n-1),                (7.5)
```

and

```text
sum_(rho!=1)|a_rho|dim rho=1.                                 (7.6)
```

The conductor--discriminant formula similarly gives

```text
sum_(rho!=1)|a_rho|log q(rho)
 =log D_E/(n-1)
 =n/(n-1)log rd(E).                                           (7.7)
```

Total reality cancels all Gamma factors in (7.1).  The remaining conductor
term is constant and disappears after differentiation.  The normalized
zero ledger through height `T` is

```text
asymp log rd(E)+log(T+3),                                     (7.8)
```

independently of the degree.  This is the essential gain over taking many
individual characters.

Primary sources for entireness are Aramata,
[*Zur Theorie der Dedekindschen Zetafunktionen*](https://doi.org/10.3792/pia/1195580866)
(1933), and Brauer,
[*On Artin's L-series with general group characters*](https://doi.org/10.2307/2371847)
(1947).

## 8. Exact conditional strip criterion

Suppose

```text
rho=1-delta+i gamma,       z_*=1+r+i gamma,       d=r+delta.  (8.1)
```

Choose

```text
d<R<r+1/2,
lambda>1,
lambda-1-log lambda>log(d/r),                                 (8.2)
```

and let `k` run over the bounded-gap useful orders supplied by the
nearest-pole power-sum lemma.  Put

```text
X_k=exp(lambda k/r).                                          (8.3)
```

Assume that for every useful `k` there is a totally real Galois field `E_k`
such that

```text
every p<=X_k splits completely in E_k;
H_(E_k) has no zero in closed B(z_*,R);
1+log rd(E_k)+log(|gamma|+3)=o((R/d)^k).                       (8.4)
```

Then `rho` cannot exist.

Indeed, with

```text
J_(E,k)=(-1)^k A_E^(k)/k!,                                   (8.5)
```

the divisor expansion and (8.4) give

```text
|J_(E,k)(z_*)|
 >=c d^(-k-1)
  -O([1+log rd(E)+log(|gamma|+3)]R^(-k-1)).                  (8.6)
```

The deleted head, (7.3), and the standard incomplete-Gamma tail estimate
give

```text
|J_(E,k)(z_*)|
 <=r^(-k+o(k))
   exp[-k(lambda-1-log lambda)].                              (8.7)
```

Equations (8.2), (8.4), (8.6), and (8.7) contradict one another.  In terms
of `X_k`, the root-discriminant condition is

```text
log rd(E_k)=o(X_k^kappa),
kappa=(r/lambda)log(R/d).                                     (8.8)
```

The geometry imposes the strict wall

```text
kappa<(r/lambda)log[(r+1/2)/r]
     <1/(2lambda)<1/2.                                       (8.9)
```

This is the fixed-strip theorem the regular mask reduces the problem to.

## 9. How cheaply can an initial split segment be built?

There is a useful elementary improvement over direct CRT.

### Theorem 9.1 -- an `X/log X` quadratic construction

For every sufficiently large `X`, there is a real quadratic field `E_X` in
which every rational prime `p<=X` splits completely and

```text
log rd(E_X)<=(log 2+o(1))pi(X)
            =(log 2+o(1))X/log X.                             (9.1)
```

#### Proof

For each auxiliary prime `q in (Y,2Y]`, attach the signature

```text
(q mod 8, ((q/p))_(3<=p<=X)).                                 (9.2)
```

There are at most `4*2^(pi(X)-1)` signatures.  If

```text
Y=exp[(log 2+epsilon)pi(X)],                                  (9.3)
```

the prime number theorem supplies more primes in `(Y,2Y]` than signatures.
Choose distinct `q_1,q_2` with the same signature.  Then

```text
d=q_1q_2=1 mod 8,              (d/p)=1 for every p<=X.        (9.4)
```

The squarefree positive integer `d` is a fundamental discriminant, so
`E_X=Q(sqrt d)` has the required splitting.  Finally

```text
log rd(E_X)=1/2 log d<=log(2Y),                                (9.5)
```

and let `epsilon` tend to zero.  QED.

This is substantially cheaper than the direct CRT cost `O(X)`, but it is
still larger than `X^kappa` for every fixed `kappa<1`, hence much larger than
(8.9).

The gap is not a routine construction problem.  Murty proved under GRH for
`zeta_E` that the least nonsplit prime satisfies

```text
p_ns << [log D_E/n]^2 asymp [log rd(E)]^2.                    (9.6)
```

Thus a field splitting every `p<=X` must obey

```text
log rd(E)>>sqrt(X)                                             (9.7)
```

under Dedekind GRH.  In particular the strict requirement (8.9) would be
false under the expected zero distribution of the auxiliary field.

Unconditionally, Zaman's Theorem 1.1 and Corollary 1.2 imply, for a suitable
positive polynomial `P`,

```text
p_ns <<_(epsilon,P)
 D_E^((1+epsilon)/(4A(n,P)(n-1)))
 =rd(E)^(n(1+epsilon)/(4A(n,P)(n-1))),                        (9.8)
```

where for `P=x+x^2`, `A(n,P)>=1-2n^(-2/3)`.  This rules out a
bounded-root-discriminant tower covering growing initial segments, but only
forces a polynomial lower bound on `rd(E)`, not the square-root lower bound
on `log rd(E)` needed here.

Sources: V. K. Murty,
[*The least prime which does not split completely*](https://eudml.org/doc/141752),
Forum Math. 6 (1994); and A. Zaman,
[*The least nonsplit prime in Galois extensions of Q*](https://arxiv.org/abs/1704.03451),
Forum Math. 30 (2018), Theorem 1.1 and Corollary 1.2.

## 10. Why split towers and forced auxiliary zeros do not close the gap

An unramified split tower preserves root discriminant, but it can only add
degree after its bottom field already splits the prescribed rational primes:
complete splitting descends through every subfield.  The construction of
Hajir--Maire--Ramakrishna produces an infinite bounded-root-discriminant
extension with infinitely many completely split primes, but those primes are
chosen with Frobenius elements at increasing Zassenhaus depth; it does not
accept the prescribed interval `p<=X`.  Maire--Sankara permit a prescribed
finite set after changing the base by tame extensions, without a quantitative
discriminant bound, and their intermediate construction makes those primes
inert rather than making the original rational primes split completely.

Primary sources: Hajir--Maire--Ramakrishna,
[*Cutting towers of number fields*](https://doi.org/10.1007/s40316-021-00156-8),
Theorem 2.8; and Maire--Sankara,
[*On S-split p-Hilbert class field towers with prescribed Galois groups*](https://doi.org/10.1142/S1793042126501290)
(2026).

The split head itself forces a right-edge zero of `H_E`.  A smooth explicit
formula, normalized by `n-1`, gives a zero `rho_H=beta_H+i tau_H` with

```text
beta_H >=1-
 [log(2+log rd(E)+log(|t|+3))+O_(t,w)(1)]/log X              (10.1)
```

for a polynomially bounded height after choosing a fixed smooth weight with
nonzero Mellin transform at `1-it`.  This is a global right-edge conclusion;
it does not put `rho_H` in `B(z_*,R)`.

Nor does Deuring--Heilbronn reverse the obstruction.  Suppose that `H_E`
has a real zero `beta_1=1-delta`, and put

```text
M=log[D_E(|gamma|+2)^n].                                     (10.2)
```

Ahn--Kwon's explicit theorem gives, for every nontrivial zeta zero
`beta+i gamma`,

```text
1-beta >=[1/(77M)]log[8.1168*10^(-4)/(delta M)]              (10.3)
```

when the logarithm is positive.  Repulsion by a fixed `eta` consequently
requires

```text
delta <=[8.1168*10^(-4)/M]exp(-77 eta M).                    (10.4)
```

Formula (10.1) may produce a complex zero and is enormously weaker than
(10.4).  Heilbronn's descent itself does not require the exceptional
window: any *simple real* Dedekind-zeta zero of a normal field descends to a
quadratic subfield.  The ultrathin window is what guarantees uniqueness and
simplicity.  Passing to that quadratic field replaces `M` by
`log[D_F(|gamma|+2)^2]`, but (10.4) still demands a zero polynomially tiny
in `D_F`, far beyond the forced bound.

There is also a sign mismatch.  For an exceptional quadratic character,

```text
Psi_-(x)=1/2[psi(x)-psi(x,chi)]
        =1/2[x+x^(beta_1)/beta_1]+error.                       (10.5)
```

The exceptional zero enhances nonresidue primes; it does not explain a
missing nonsplit head.

Sources: Ahn--Kwon,
[*Some explicit zero-free regions for Hecke L-functions*](https://doi.org/10.5802/aif.3274),
Theorem 7.3, and Heilbronn,
[*On real zeros of Dedekind zeta-functions*](https://doi.org/10.4153/CJM-1973-090-3).

## 11. Approximate splitting via permutation characters

There is one genuine escape from the least-*nonsplit*-prime formulation.
Let `K/Q` be totally real of degree `m>1`, not necessarily Galois, and put

```text
A_K=(mD_zeta-D_(zeta_K))/(m-1).                              (11.1)
```

At an unramified prime, let `g_p` act on the `m` embeddings of `K`.  The
permutation-character identity gives

```text
[A_K]_(p^v)
 =[m-Fix(g_p^v)]/(m-1) in [0,m/(m-1)].                       (11.2)
```

Positivity, total-real Gamma cancellation, and the normalized conductor
cost

```text
log D_K/(m-1)=m/(m-1)log rd(K)                               (11.3)
```

all survive.  If `g_p` moves at most `L` embeddings, every power `g_p^v`
moves at most `L`, so the whole local prime-power defect is at most
`L/(m-1)`.  Hence, for `X_k=exp(lambda k/r)`,

```text
|J_(K,k)(1+r+i gamma)|
 <=r^(-k+o(k))[L_k/m_k+exp(-k I(lambda))],
I(lambda)=lambda-1-log lambda.                               (11.4)
```

The high-jet contradiction therefore needs only

```text
I(lambda)>log(d/r),
L_k/m_k=o((r/d)^k),                                          (11.5)

1+log rd(K_k)+log(|gamma|+3)=o((R/d)^k),                     (11.6)
```

plus entireness and local nonvanishing of `zeta_K/zeta`.  A transposition
has defect `2/(m-1)` even though the prime is nonsplit, so Murty--Zaman
least-nonsplit bounds do not rule out (11.5).

Transitive iterated-wreath `2`-groups provide an algebraically compatible
test class: their natural actions contain leaf transpositions, and finite
`2`-groups are monomial, so the relevant nontrivial Artin factors reduce to
Hecke `L`-functions.  What is missing is a quantitative totally real
realization in which

```text
supp(g_p)<=L_k                         for every p<=X_k,
m_k/L_k>>(d/r)^k,
log rd(K_k)=o(X_k^kappa).                                    (11.7)
```

Known local and inverse-Galois existence theorems do not control the
discriminant on this scale.  Under GRH for `zeta_K`, the explicit formula
applied to (11.2) again gives

```text
log rd(K)>=X^(1/2-o(1))                                      (11.8)
```

whenever every `p<=X` moves `o(m)` points.  Thus any successful realization
must manufacture systematic off-GRH auxiliary zeros, not merely evade the
word “nonsplit.”

## 12. Verdict and next gate

R141 has produced three real advances:

```text
a nonlinear object which separates divisor order exactly;
a high-degree mask whose entire conductor ledger is log rd(E);
an approximate permutation mask which replaces splitting by tiny support. (12.1)
```

It has also located their failures sharply.  The nonlinear object needs a
signed one-prime/Type-II theorem.  The regular mask needs a split field on a
scale which Dedekind GRH predicts cannot exist, plus local avoidance of the
very auxiliary zeros forced by the split head.

The next plausible escape must therefore change an exponent, rather than
optimize a constant.  Three candidates survive this audit:

1. use a growing nonlinear tensor so that a zeta zero shared by many
   detectors has higher pole order than every auxiliary-only zero; or
2. realize the low-support permutation pattern (11.7), or prove that its
   solvable/monomial group structure forces an expensive split quotient; or
3. find a genuinely signed correlation in the exact coefficient formulae
   (1.5)--(1.9), strong enough to replace their absolute zero ledger.

Both require a new theorem.  Neither the fixed strip nor its negation follows
from the present reductions.

**Successor update (R143--R144).**  The solvable/monomial version of item 2
does force a completely split intermediate field of degree at least
`m/(2L)`, so that branch is closed.  Primitive classification leaves natural
`A_m/S_m`; there the new virtual character `(m-Fix)_q` annihilates bounded
support exactly and removes condition (11.5).  Its unavoidable negative
representation mass replaces (11.5) by a target-conditioned signed-divisor
noncancellation condition.  See
[`R143-SOLVABLE-SUPPORT-QUOTIENT-AND-PRIMITIVE-CLASSIFICATION.md`](R143-SOLVABLE-SUPPORT-QUOTIENT-AND-PRIMITIVE-CLASSIFICATION.md)
and
[`R144-BOUNDED-SUPPORT-VIRTUAL-CHARACTER-ANNIHILATOR.md`](R144-BOUNDED-SUPPORT-VIRTUAL-CHARACTER-ANNIHILATOR.md).
