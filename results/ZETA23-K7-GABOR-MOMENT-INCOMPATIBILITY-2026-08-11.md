# The density-legal `k=7` carrier fails the Zeta23 second moment

Status: exact Gabor-level no-go card, 2026-08-11.  This note tests the
`k=7` core-sublattice counterconfiguration against the *evaluated* first and
second matrix moments in the Anthropic Zeta23 argument.  The configuration
survives all current counting and density inputs, and its first matrix trace
can be completed correctly, but no choice of on-line filler can make its
Frobenius moment have the Zeta23 size.  This is a statement about an explicit
Gabor-row model, not merely an abstract spectrum.  It is not an assertion
that such a zero configuration comes from the zeta function.

The external normalization and moment formulas used below are from the
[Zeta23 paper](https://www-cdn.anthropic.com/564f962e60643842f5fcb4a17c9dbc8f608f1c37.pdf),
especially (2.19)--(2.21), Lemma 2.2, Theorem 5.8, Remark 5.10, and
Theorem D.

## 1. Verdict

Put

```text
l       = log(T/(2*pi)),
L_plus  = ell_1+eta = l+2*log(2)-1+eta,
X_plus  = exp(L_plus),
h_plus  = 2*pi/L_plus.
```

The core obstruction places a reflected depth-`alpha` pair every seven
`h_plus` spacings.  Its pair-point fraction is `2/7+o(1)`, so its on-line
fraction is `5/7+o(1)`.  This is compatible with the exact Zeta23 lower
density

```text
C_0 = 3/2-(1/sqrt(2))*cot(1/sqrt(2))
    = 0.6725007036... < 5/7.                         (1.1)
```

It is not compatible with the full Zeta23 moment package.  Probe the same
configuration with the legal bandwidth-one Montgomery--Taylor compression,
whose physical support length is `L_0=l`.  If `Q_7` is the normalized matrix
of the depth-`alpha` pair lattice and `P_on>=0` is *any* matrix made from
on-line Gabor atoms, then, for every fixed `0<alpha<1/2`,

```text
tr(P_on+Q_7) = O(d_0)
    ==>
||P_on+Q_7||_F^2
    >= kappa(alpha)*d_0*X_plus^(12*alpha/7)          (1.2)
```

for all sufficiently large `T`, where

```text
d_0=floor(T*L_0/(2*pi))=(1+o(1))*N(T,2T)             (1.3)
```

and `kappa(alpha)>0`.  In fact the proof gives a constant independent of
`alpha` once `alpha` is fixed and `T` is beyond an `alpha`-dependent
threshold.

Zeta23 instead evaluates, in the same normalization,

```text
tr Ghat       = (1+o(1))*N(T,2T),
||Ghat||_F^2  = (c_*^(-1)+o(1))*N(T,2T),              (1.4)

c_* = 2*tan(1/sqrt(2))/(sqrt(2)+tan(1/sqrt(2)))
    = 0.7532960...,
c_*^(-1)=1/2+(1/sqrt(2))*cot(1/sqrt(2))
         =1.3274992....                               (1.5)
```

Equations (1.2) and (1.4) contradict one another because
`X_plus^(12*alpha/7)->infinity`.  Thus the `k=7` construction is a valid
obstruction to a theorem using counts and simple-line density only, but it
is **not** a counterconfiguration once the evaluated Zeta23 Frobenius/pair-
correlation moment is imposed.

The first trace and the pair-correlation language should not be counted as
three independent restrictions.  Remark 5.10 of Zeta23 identifies the
zero-side pair-correlation sum with `||Ghat||_F^2`; the new exclusion comes
from that second moment.

## 2. Why a separate bandwidth-one probe is necessary

The endpoint-jet construction uses `L_plus>l`.  Zeta23's unconditional
prime-side second-moment evaluation is proved only for bandwidth
`lambda<=1`; it is not legal to substitute `L_plus` directly into Theorem
5.8.  Instead use the same hypothetical zero configuration in the
Montgomery--Taylor family with

```text
L_0=l,       h_0=2*pi/L_0,       d_0=floor(T/h_0).    (2.1)
```

A genuine zeta-zero configuration would have to satisfy the explicit
formula for this second test family as well.  The pair spacing and its dual
period are

```text
s=7*h_plus=14*pi/L_plus,
P=2*pi/s=L_plus/7.                                   (2.2)
```

Since `L_plus/L_0->1` and `eta=o(l)`, eventually

```text
6P<L_0<7P.                                           (2.3)
```

Consequently the extreme nonzero alias in the bandwidth-one probe is still
`q=6`, and it carries the exact exponential weight

```text
exp(6*alpha*P)=X_plus^(6*alpha/7).                   (2.4)
```

This is the same power found in the sharp carrier calculation.  No
bandwidth-greater-than-one prime estimate is being assumed.

## 3. Exact Gabor realization and bilinear Poisson formula

Let `phi_T` be the endpoint-mollified Montgomery--Taylor window used in
Theorem D, and put

```text
a_T = L_0^(-1)*integral phi_T(u)^2 du.
```

Away from fixed-width endpoint ramps,

```text
phi_T(L_0*x)^2 -> v_*(x)=cos(sqrt(2)*x),
a_T -> a_*:=integral_(-1/2)^(1/2)v_*(x)dx
          =sqrt(2)*sin(1/sqrt(2)).                   (3.1)
```

For coordinates `tau_n=tau_0+n*h_0`, write

```text
p_c(u)=sum_(0<=n<d_0)c_n*exp(-i*n*h_0*u).
```

Choose the lattice offset so that a pair occurs at `3T/2`, and write its
lower member as

```text
z_j=tau_0+beta+j*s-i*alpha.
```

Its Gabor evaluation is the actual Zeta23 row

```text
F_j(c)=integral_(-L_0/2)^(L_0/2)
          phi_T(u)*p_c(u)*exp(alpha*u)*exp(i*(beta+j*s)*u)du.  (3.2)
```

One reflected pair contributes `2*Re(F_j(c)^2)` before the common
normalization.  Dirac-comb Poisson summation in `j` gives the exact identity

```text
sum_j F_j(c)^2
 =P*sum_(q in Z) exp(alpha*q*P)*exp(i*beta*q*P)
       *integral phi_T(u)*phi_T(q*P-u)
          *p_c(u)*p_c(q*P-u)du.                     (3.3)
```

Only `|q|<=6` occurs by (2.3).  Thus this is an explicit sum of matrices
built from the genuine Gabor evaluations (3.2), not an independently
prescribed eigenvalue model.

For completeness, center the overlap in (3.3) at `qP/2` and set

```text
B_(q,r)=integral phi_T(qP/2+x)*phi_T(qP/2-x)
                 *cos(r*h_0*x)dx.                   (3.4)
```

The `q`-alias matrix in Zeta23's isolated-zero normalization
`1/(a_T*L_0^2)` has entries

```text
(Q_q)_(nm)
 = (2P/(a_T*L_0^2))*exp(alpha*q*P)*B_(q,n-m)
     *cos(theta_q-q*h_0*P*(n+m)/2),                 (3.5)
```

where `theta_q` depends only on the lattice offset.  This displays both the
hyperbolic factor `2*Re` and every normalization used below.

## 4. The `q=6` alias has extensive Frobenius mass

Parseval for the coordinate Fourier series gives

```text
sum_(r in Z) B_(6,r)^2
 = L_0*integral [phi_T(u)*phi_T(6P-u)]^2 du
 = L_0^2*(I_7+o(1)),                                (4.1)
```

where the exact limiting overlap is

```text
I_7
 = integral_(5/14)^(1/2)
      cos(sqrt(2)*x)*cos(sqrt(2)*(6/7-x))dx
 = cos(6*sqrt(2)/7)/14+sin(sqrt(2)/7)/(2*sqrt(2))
 = 0.09601337217... >0.                             (4.2)
```

For fixed `r=n-m`, the phase in (3.5) advances by `q*h_0*P` as
`m` advances, so the doubled phase in the `cos^2` sum advances by
`2*q*h_0*P`.  Since

```text
q*P/L_0 -> 6/7 notin (1/2)*Z,
```

the geometric sum of the doubled phases is uniformly bounded.  Hence the
mean of the squared cosine over the `d_0-|r|` available entries is
`1/2+o(1)`.  The fixed-width `C^2` ramps give sufficient Fourier decay to
sum this statement over `r`.  Substitution in (3.5) yields

```text
||Q_6||_F^2
 = (2*I_7/(49*a_*^2)+o(1))*d_0*X_plus^(12*alpha/7), (4.3)

2*I_7/(49*a_*^2)=0.00464295228....                  (4.4)
```

Every other alias is down by at least
`exp(-alpha*P)=X_plus^(-alpha/7)`.  Indeed Parseval and
`0<=phi_T<=1` give

```text
||Q_q||_F=O(sqrt(d_0)*exp(alpha*q*P)),               (4.5)
```

uniformly for `-6<=q<=6`.  Therefore, for the full infinite lattice matrix
`Q_infty=sum_q Q_q`,

```text
||Q_infty||_F^2
 = (2*I_7/(49*a_*^2)+o(1))*d_0*X_plus^(12*alpha/7). (4.6)
```

There is also a direct operator bound.  Exact orthogonality of the
coordinate exponentials gives `integral |p_c|^2=L_0*||c||_2^2`; applying
Cauchy--Schwarz to each overlap in (3.3) gives

```text
||Q_infty||op
 <= (2P/(a_T*L_0))*sum_(q=-6)^6 exp(alpha*q*P)
 = O(X_plus^(6*alpha/7)).                            (4.7)
```

Finally, the `q=0` alias contributes `2P/L_0=2/7+o(1)` to every diagonal
entry.  The trace of each nonzero alias is a bounded geometric sum in the
coordinate index, so

```text
tr Q_infty=(2/7+o(1))*d_0+O(X_plus^(6*alpha/7))
            =O(d_0).                                (4.8)
```

The last equality uses `alpha<1/2`, so
`X_plus^(6*alpha/7)=o(d_0)`.

## 5. Finite carrier and the on-line filler cannot repair the moment

The infinite lattice in Section 4 is only a device for evaluating the
finite carrier.  Retain the pair rows in a collar containing

```text
(T-sqrt(T),2T+sqrt(T)].                              (5.1)
```

The actual core construction uses a still wider collar under its parameter
assumptions.  Twice integrating the compactly supported `C^2` window gives

```text
|phihat_T(r-i*alpha)|
 <= C*X_plus^(alpha/2)/|r|^2.                        (5.2)
```

For an omitted pair at distance `R` from the modulation band, its normalized
rank-two trace norm is consequently

```text
O(X_plus^alpha*R^(-3)/L_0).
```

There are `O(L_0)` lattice ordinates per unit interval.  Summing outside
distance `D_0=sqrt(T)` gives

```text
||Q_infty-Q_7||_1
 =O(X_plus^alpha/D_0^2)=O(T^(alpha-1+o(1)))=o(1).    (5.3)
```

Thus (4.6)--(4.8) hold for the finite, count-compatible carrier `Q_7`.

Now use the Schatten inequality

```text
||Q_7||_1 >= ||Q_7||_F^2/||Q_7||op.                 (5.4)
```

Equations (4.6)--(4.8) imply, with
`W=X_plus^(6*alpha/7)`,

```text
tr((Q_7)_-)
 =(||Q_7||_1-tr Q_7)/2
 >= c*d_0*W                                           (5.5)
```

for some `c>0` and all sufficiently large `T`.

Let `P_on` be any sum of on-line Gabor atoms.  It is positive semidefinite.
If the first trace in (1.4) is to hold, (4.8) forces

```text
tr P_on=O(d_0).                                      (5.6)
```

This includes the quantile filler from the core construction; more
specifically, a single on-line atom has normalized trace at most one by
Zeta23's full-grid Poisson identity, and there are `(5/7+o(1))*d_0` such
points in the dyadic band.

For Hermitian `H` and `P>=0`, the variational formula for the negative trace
gives

```text
tr((H+P)_-) >= tr(H_-)-tr P.                         (5.7)
```

Applying this to (5.5)--(5.6), then using Cauchy--Schwarz on at most `d_0`
negative eigenvalues, gives

```text
tr((P_on+Q_7)_-) >= (c/2)*d_0*W,
||P_on+Q_7||_F^2
 >= tr((P_on+Q_7)_-)^2/d_0
 >= (c^2/4)*d_0*X_plus^(12*alpha/7).                 (5.8)
```

This proves (1.2).  It also explains the mechanism: the `k=7` Poisson
screening lowers the *operator edge* from `X_plus^alpha` to
`X_plus^(6alpha/7)`, but it creates that scale on a positive proportion of
the Gabor directions.  Their total negative trace is too large for an
`O(d_0)`-trace positive filler.

## 6. Exact scope of the no-go

What is now closed is the proposed **positive-density, fixed-depth,
regular-sublattice** counterconfiguration after all current Zeta23 input is
enforced.  It cannot be used to show that the carrier edge may genuinely be
as small as `X_plus^(6alpha/7)` for an actual zeta-zero configuration.

What is not closed is the uniform-strip problem:

1. The calculation uses `asymp d_0` regularly spaced off-line pair rows.
   A single pair, or `o(d_0)` exceptional pairs, changes the normalized first
   two moments by too little to be excluded this way.
2. The Zeta23 moments still do not give a quantitative lower edge for one
   exceptional hyperbolic block.  They rule out this extensive screening
   mechanism, not all possible screening mechanisms.
3. No zero set has been constructed from an Euler product or an explicit
   formula.  Conversely, no claim is made that the artificial filler is a
   possible zeta-zero set.
4. The count-only statement in the core-sublattice report remains correct:
   counts plus the `C_0` simple-line density alone permit `k=7`.  This note
   shows precisely which additional arithmetic datum removes it.

The next carrier audit should therefore target **sparse** screening: can one
fixed-depth pair be hidden by an otherwise on-line configuration while the
bandwidth-one trace and Frobenius moments retain (1.4)?  The present argument
does not answer that question, and a positive answer at the level of moments
would still not amount to an actual zeta realization.
