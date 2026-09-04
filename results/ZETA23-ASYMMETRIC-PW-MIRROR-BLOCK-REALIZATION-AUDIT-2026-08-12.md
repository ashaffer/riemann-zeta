# The asymmetric mirror block in a normalized Paley--Wiener packet class

Status: exact two-packet compression, exact Lorentz rebalancing of the
reflected-pair rows, a growing-jet finite-grid transfer, and scope boundary,
2026-08-12.  The completed one-pair counterblock is realized in a concrete
normalized asymmetric Paley--Wiener/Gabor class.  The actual von Mangoldt
aggregate is not realized.  No zero-free strip is proved or disproved.

## 1. Verdict

The abstract mirror block used in the augmented-row counterexample is the
correct leading normalization of a genuine reflected-pair compression on
two disjoint localized packets separated by

```text
D=d_*L,             1/2<d_*<2/3.                    (1.1)
```

For equal translated real-even packets, the exact normalized pair matrix is

```text
M_pair=m_L*[[1,cosh(alpha*D)],
            [cosh(alpha*D),1]],                     (1.2)
```

where `m_L=L^(-1+o(1))>0` for a fixed-width normalized packet.  Hence

```text
M_pair
 =2*k_L*[[0,1],[1,0]]+m_L*I,

2*k_L=m_L*cosh(alpha*D),
k_L=X^(alpha*d_*-o(1)).                              (1.3)
```

The diagonal remainder is smaller than the carrier by
`X^(-alpha*d_*+o(1))`.

The raw positive and negative evaluation rows are not literally balanced
when the two packet centers have nonzero midpoint.  Their unequal weights
are an exact Lorentz boost.  Applying the inverse boost, which preserves the
difference of squares, gives rows proportional to

```text
u+v,               u-v                              (1.4)
```

with coefficient ratio `1+O(X^(-alpha*d_*))`.  Equivalently, the spectral
positive and negative rows of (1.2) are exactly `u+v` and `u-v`.

Thus the earlier pure block is not an arbitrary matrix surrogate.  It is the
carrier-scale part of a normalized asymmetric Paley--Wiener compression, and
its one-real-equation obstruction survives exactly.  The remaining gap is
arithmetic: no argument here identifies the actual raw-prime aggregate with
this completed pair block after all actual collateral zero rows are retained.

## 2. Normalized packet and reflected-pair form

Work after demodulation by the target ordinate `gamma`.  In the critical
Fourier grid convention, coefficient and physical norms satisfy

```text
norm(p_c)_2^2=L*norm(c)_2^2.                         (2.1)
```

More explicitly, the repository uses

```text
tau_j=gamma+xi_j,
f_c(t)=1_[-L/2,L/2](t)*e^(-i*gamma*t)*p_c(t),
p_c(t)=sum_j c_j*e^(-i*xi_j*t),
F_c(s)=integral f_c(t)e^(i*s*t)dt.                  (2.1a)
```

For the lower member `z=gamma-i*alpha` of the reflected pair,

```text
F_c(z)=integral p_c(t)e^(alpha*t)dt.                (2.1b)
```

On real coefficient vectors, `p_c(-t)=conj(p_c(t))`.  If
`F_c(z)=X(c)+i*Y(c)`, pairing `t` with `-t` gives exactly

```text
X(c)=integral p_c(t)cosh(alpha*t)dt,
Y(c)=-i*integral p_c(t)sinh(alpha*t)dt.             (2.1c)
```

The second identity is real-valued on the real coefficient space because
the integral is purely imaginary.  Equations (2.1b)--(2.1c), extended
complex-linearly, are the precise modulation and conjugation step behind the
kernel below.  In particular, `gamma` cancels; it is not silently replaced by
zero on the prime side, where the absolute phase remains.

Choose a nonnegative real-even function

```text
phi in C_c^infinity((-w/2,w/2)),      norm(phi)_2=1 (2.2)
```

with fixed `w>0`, and put

```text
q_j(t)=sqrt(L)*phi(t-t_j),
t_+-t_-=D.                                           (2.3)
```

Assume the translated supports are disjoint and lie strictly inside the
free and seed lobes.  Then the corresponding coefficient vectors `u,v` are
orthonormal by (2.1).

Let

```text
A_alpha=integral phi(s)e^(alpha*s)ds
       =integral phi(s)e^(-alpha*s)ds>0,             (2.4)
```

where evenness gives the equality.  For the two Laplace evaluations,

```text
L_+(q_j)=sqrt(L)*A_alpha*e^(alpha*t_j),
L_-(q_j)=sqrt(L)*A_alpha*e^(-alpha*t_j).             (2.5)
```

The repository's isolated-pair normalization is

```text
B_alpha(p)
 =(2/L^2)*(abs(X_alpha(p))^2-abs(Y_alpha(p))^2),

X_alpha(p)=integral p(t)cosh(alpha*t)dt,
Y_alpha(p)=integral p(t)sinh(alpha*t)dt,             (2.6)
```

where the factor `-i` in (2.1c) has unit modulus.  Its Hermitian integral
kernel is

```text
(2/L^2)*cosh(alpha*(t-s)).                           (2.7)
```

Indeed, for complex-polarized `p`, expansion of the two squared moduli gives

```text
B_alpha(p)
 =(2/L^2)*integral integral
     p(t)*conj(p(s))*cosh(alpha*(t-s))dt ds,         (2.7a)
```

because `cosh t cosh s-sinh t sinh s=cosh(t-s)`.

Taking the matrix of (2.7) on `span{u,v}` and using (2.4)--(2.5) gives

```text
<u,M_pair*u>=<v,M_pair*v>=m_L,
<u,M_pair*v>=m_L*cosh(alpha*D),

m_L=2*A_alpha^2/L.                                  (2.8)
```

This proves (1.2) with every normalization factor displayed.  A different
Fourier convention changes only the common positive `m_L=X^o(1)` and not
the matrix ratio or any power exponent.

In particular, the pure-block parameter in (1.3) is exactly

```text
k_L=(A_alpha^2/L)*cosh(alpha*d_*L)
   =(A_alpha^2/(2*L))
      *(X^(alpha*d_*)+X^(-alpha*d_*)).              (2.9)
```

Thus the negative eigenvalue of the full normalized packet compression is

```text
lambda_-=2*A_alpha^2/L*(1-cosh(alpha*d_*L))
        =-2*k_L+2*A_alpha^2/L.                      (2.10)
```

These identities distinguish the exact `1/L` normalization from the
harmless exponent notation `X^(alpha*d_*-o(1))`.

## 3. The midpoint imbalance is exactly a Lorentz boost

Put

```text
m=(t_-+t_+)/2,              h=D/2.                  (3.1)
```

After removing the common factor in (2.5), the raw positive and negative
row restrictions are

```text
x=(cosh(alpha*t_-), cosh(alpha*t_+)),
y=(sinh(alpha*t_-), sinh(alpha*t_+)).                (3.2)
```

For an asymmetric placement, `m` is generally nonzero.  Therefore (3.2) is
**not** of the form `c(1,1),c(1,-1)`.  Replacing it by balanced rows without
an explanation would be a normalization error.

Apply the hyperbolic rotation

```text
[x']   [ cosh(alpha*m)  -sinh(alpha*m)] [x]
[y'] = [-sinh(alpha*m)   cosh(alpha*m)] [y].         (3.3)
```

The matrix in (3.3) preserves `diag(1,-1)`, so exactly

```text
x*x^*-y*y^*=x'*x'^*-y'*y'^*.                        (3.4)
```

The addition formulas give

```text
x'=cosh(alpha*h)*(1,1),
y'=sinh(alpha*h)*(-1,1).                            (3.5)
```

Thus the physical midpoint imbalance is a pure choice of hyperbolic row
coordinates; it does not alter the pair operator.  Moreover,

```text
cosh(alpha*h)/sinh(alpha*h)
 =1+O(exp(-alpha*D))
 =1+O(X^(-alpha*d_*)).                              (3.6)
```

Equations (3.5)--(3.6) produce the balanced abstract rows at carrier scale.

The same statement follows directly from (1.2).  With

```text
e_+=(u+v)/sqrt(2),       e_-=(u-v)/sqrt(2),          (3.7)
```

the exact eigenvalues are

```text
lambda_+=m_L*(1+cosh(alpha*D)),
lambda_-=m_L*(1-cosh(alpha*D)).                      (3.8)
```

Hence a spectral difference-of-squares factorization has positive row
`sqrt(lambda_+)*e_+` and negative row
`sqrt(-lambda_-)*e_-`.  Both have size
`X^(alpha*d_*/2-o(1))`, and their relative squared-size discrepancy is
`1/cosh(alpha*D)`.

In the countermodel convention `M_pair=2*(x_T*x_T^*-y_T*y_T^*)`, the exact
rows are

```text
x_T=sqrt(k_L+m_L/2)*e_+,
y_T=sqrt(k_L-m_L/2)*e_-.                            (3.9)
```

Since `e_+=(u+v)/sqrt(2)` and `e_-=(u-v)/sqrt(2)`, these equal

```text
sqrt(k_L/2)*(u+v),       sqrt(k_L/2)*(u-v)          (3.10)
```

with relative error `O(m_L/k_L)=O(X^(-alpha*d_*))`.  This is the precise
sense in which the requested pure mirror rows are realized with subcarrier
error; the full matrix itself remains exactly (1.2).

## 4. Exact positive null and the one-real aggregate

Write a two-packet test as

```text
f=t*u+s*v.                                           (4.1)
```

Nulling the exact positive spectral row in (3.7)--(3.8) gives

```text
t=-s.                                               (4.2)
```

The completed pair cross vector from the seed into the free packet is

```text
P_-*M_pair*(s*v)=m_L*cosh(alpha*D)*s*u.              (4.3)
```

Therefore every positive-null packet satisfies

```text
2*Re <t*u,P_-*M_pair*(s*v)>
 =-2*m_L*cosh(alpha*D)*abs(s)^2.                    (4.4)
```

It cannot satisfy the minimal aggregate equation

```text
Re <t*u,P_-*M_pair*(s*v)>=0                         (4.5)
```

unless `s=0`.  But `s=0` and (4.2) delete the packet and its carrier.

The full pair value is

```text
<f,M_pair*f>
 =2*m_L*(1-cosh(alpha*D))*abs(s)^2
 =-X^(alpha*d_*-o(1))*abs(s)^2.                     (4.6)
```

The difference between (4.4) and (4.6) is only the diagonal
`2*m_L*abs(s)^2=X^o(1)*abs(s)^2`.  Thus the exact normalized PW block has
the same fixed-power affine obstruction as the pure matrix block.

The Lorentz row (3.5) gives the same conclusion without diagonalizing:
its positive coordinate is proportional to `t+s`, while its negative
coordinate is proportional to `-t+s`.

## 5. Finite Gabor grid and endpoint conditions

The packets in (2.3) are supported strictly inside the physical support.
As genuine compactly supported Paley--Wiener tests, they satisfy every
physical endpoint jet exactly.  To transfer them uniformly to the finite
Gabor grid, including a growing jet order, reserve part of the relative
Fourier aperture for one common endpoint-flat cutoff.

Let the available relative trigonometric degree be `J asymp T*L`, let the
required jet order be `M`, and assume the audited mesoscopic budget

```text
M=O(T*eta),              eta=o(L).                  (5.1)
```

Choose fixed fractions `R,Q asymp J` with `R+Q<J`, and put

```text
r=ceil(M/2),
u_0(t)=(1+cos(2*pi*t/L))/2,
C_(R,r)(t)=sum_(j=r)^R binom(R,j)u_0(t)^j
                              *(1-u_0(t))^(R-j).    (5.2)
```

This is a trigonometric polynomial of degree `R`, lies in `[0,1]`, and has
a zero of order at least `2r>=M` at both endpoints.  Hence multiplying by
`C_(R,r)` imposes all `M` endpoint jets exactly.  The binomial Chernoff bound
also gives

```text
1-C_(R,r)(t)<=exp(-R*u_0(t)/8)                      (5.3)
```

whenever `R*u_0(t)>=2r`.

For the free packet, the distance from both physical endpoints is a fixed
positive multiple of `L`, so the right side of (5.3) is `exp(-c*T*L)`.  The
seed packet is a distance `asymp bL` from the right endpoint.  The condition
already present in the asymmetric ledger,

```text
bL/sqrt(eta*L)->infinity,
equivalently b^2*L/eta->infinity,                   (5.4)
```

implies `R*u_0(t)/r->infinity` uniformly on its fixed-width support.  Thus
(5.3) is `exp(-c*T*L*b^2)` there.

Let `q_(j,Q)` be the degree-`Q` Fourier truncation of the smooth packet
`q_j`.  Define

```text
p_j=C_(R,r)*q_(j,Q).                                (5.5)
```

Then `p_j` lies in the available degree-`J` grid and satisfies all growing
endpoint jets exactly.  Smooth compact support gives, for every prescribed
`A`, an `O_A(T^(-A))` error in norm and in every fixed Sobolev norm.  After
multiplication by the largest Laplace weight `exp(alpha*L/2)`, one still gets
`O_A(T^(-A))` by first increasing the truncation exponent.  Equations
(5.3)--(5.4) show that the common cutoff contributes a still smaller error.
The two original supports are disjoint, so normalization and Gram--Schmidt
change the two packets and every pair-matrix entry by `O_A(T^(-A))`.

Consequently (1.2)--(4.6) transfer to the full growing-jet finite Gabor
space with exact endpoint jets and an error smaller than every fixed power
of `T`.  In particular the error is

```text
o(m_L*cosh(alpha*D))
 =o(X^(alpha*d_*)/L),                               (5.6)
```

so it cannot affect the carrier exponent or the one-real affine
obstruction.  The target ordinate may be placed in the dyadic core and the
fixed aperture fractions chosen so that all absolute frequencies remain in
the prescribed band.

For the asymmetric intervals

```text
I_-=[-L/2,-L/2+aL],
I_+=[L/2-bL,L/2],                                   (5.7)
```

the seed condition `bL->infinity` leaves room for a fixed-width packet in
`I_+`.  The assumed geometric placement of the reduced target supplies a
point in `I_-` at distance `D=d_*L`; fixed-width inward shifts alter `D` by
only `O(1)` and hence change the carrier by a constant factor.

Independent complex lobe polarization causes no real-admissibility gap.  For
the real symmetric completed matrix, the usual identity

```text
Q(x+i*y)=Q(x)+Q(y)                                  (5.8)
```

descends a negative complex value to one real component.

## 6. What has and has not been upgraded

The audit proves the following concrete statement.

> Within the normalized compact-support two-packet Paley--Wiener subspace of
> the stated asymmetric lobes, the completed reflected-pair compression is
> exactly (1.2).  In the full growing-jet finite Gabor space the binomial
> cutoff construction realizes the same matrix up to `O_A(T^(-A))` for every
> fixed `A`.  Its carrier-scale part is the pure mirror block, its positive
> row forces equal and opposite packet coefficients, and even one-real
> completed cross cancellation removes the carrier.

The two-dimensional compression can be embedded without sacrificing the
ambient dimension.  In the finite jet space let `x_raw,y_raw` be the two
selected-pair Riesz rows and put

```text
W={u,v}^perp intersect ker(x_raw) intersect ker(y_raw).  (6.1)
```

Then `codim W<=4`, and on `span{u,v} direct_sum W` the selected pair is the
matrix (1.2) direct-summed with zero.  Thus arbitrarily many unused Gabor
directions may be retained exactly; the realization is not merely a
standalone two-dimensional Hilbert-space model.

There are two distinct scope boundaries.

1. **The raw rows are Lorentz-boosted.**  Before (3.3), writing them directly
   as equal `u+v,u-v` rows is false when the packet midpoint is nonzero.  The
   legitimate correction is the `J`-unitary boost or the spectral
   factorization.  Both preserve the completed pair operator and recover the
   balanced rows exactly up to the explicit diagonal remainder.
2. **The actual prime row is not constructed.**  The explicit formula says
   that the full completed arithmetic cross block equals the full zero cross
   block, including on-line and collateral off-line rows.  This audit realizes
   the selected completed pair block, not a positive atomic sum over the
   actual weights `Lambda(n)/sqrt(n)`.  Actual collateral rows could in
   principle supply a transverse aggregate reservoir.  Proving or excluding
   that at subpower cost is still the actual-zeta, strip-strength question.

Allowing the entire high-dimensional lobe spaces does not change the exact
one-pair projection identity

```text
P_(ker x_-)*(P_-K_pair*r)
 =-2*conj(<r,y_+>)*P_(ker x_-)*y_-.                 (6.2)
```

It does allow arithmetic and collateral-zero components outside the
two-packet plane.  Current bulk moments do not control their angle.  Thus the
PW realization strengthens the abstract countermodel but does not turn it
into an Euler-product counterexample.

The finite-dimensional source block and its logical scope are recorded in
[`ZETA23-AUGMENTED-ROW-SEVEN-EIGHTH-COUNTERMODEL-2026-08-12.md`](ZETA23-AUGMENTED-ROW-SEVEN-EIGHTH-COUNTERMODEL-2026-08-12.md)
and
[`ZETA23-CONDITIONAL-SEVEN-EIGHTHS-LOGIC-AUDIT-2026-08-12.md`](ZETA23-CONDITIONAL-SEVEN-EIGHTHS-LOGIC-AUDIT-2026-08-12.md).
