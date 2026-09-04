# Prime-log Riesz products: the torus theorem and the polynomial-orbit barrier

Status: focused theorem and mechanism audit, 2026-08-12.  The positive
prime-power moment problem is solved after removing the upper spectral cap.
Unique factorization then gives exact Wiener and `L^2` condition numbers for
the natural Riesz-product and exponential-tilt realizations.  Those numbers
give a full-power barrier for the audited bounded-degree/absolute-Wiener
transfer and a square-root barrier for the audited bounded-degree
`L^2`/stably Gram-corrected transfer.  This is a theorem about those
mechanisms, not an upper bound for every possible high-degree absolute
estimate or for the unrestricted finite-band convex program.  No zero-free
strip is claimed.

## 1. Verdict

Let

```text
u_n=log(n/Y_c),                                      (1.1)
```

where the active `n=p^k` are the prime powers in a fixed logarithmic window
about `Y_c`.  The desired noncentral probability measure is required to obey

```text
integral cos(xi*u_n) dnu(xi)=-r                     (1.2)
```

for every active prime power.  Mixing it with

```text
w_0*delta_0,             w_0=r/(1+r),               (1.3)
```

makes all of the moments zero.

There are four exact conclusions.

1. **Positivity and prime-power relations are not the obstruction.**  If no
   upper bound is placed on `xi`, there is an even finitely atomic `nu`
   supported outside any prescribed interval `(-R,R)` which satisfies
   (1.2) with

   ```text
   r >= c/log Y_c.                                  (1.4)
   ```

   For a multiplicatively generic center, `r` may be a fixed constant.  The
   logarithmic version also handles a polynomial-height rational center when
   no active character is one of the degeneracies `n=Y_c` or `n=Y_c^2`;
   this includes the half-integer centering used in the finite LP.  It
   includes all active prime powers, not only primes.

2. **The missing hypothesis is the polynomial upper type.**  The proof of
   (1.4) uses the density of a scalar Kronecker orbit in the full
   prime-coordinate torus.  It gives no bound of the form

   ```text
   abs(xi)<=T=Y_c^(1/d).                             (1.5)
   ```

   Thus the exact finite-band problem is a quantitative early-return
   theorem for the actual prime-log orbit, rather than an abstract moment or
   positivity problem.

3. **The natural transfers are exponentially ill-conditioned at subpower
   `r`.**  If `M` is the number of active prime powers, the variable
   prime-factor part of the product density which proves the torus theorem
   has

   ```text
   Wiener norm = exp(Theta(r*M)),
   squared L2 norm = exp(Theta(r^2*M)).              (1.6)
   ```

   Here `M=Y_c^(1+o(1))`.  Consequently the finite-degree
   absolute-Wiener transfer audited below is confined to
   `r=Y_c^(-1+o(1))`, while its bounded-degree `L^2` or stably
   Gram-corrected counterpart is confined to

   ```text
   r <= M^(-1/2)*Y_c^o(1)
     =Y_c^(-1/2+o(1)).                              (1.7)
   ```

   The fixed center factor changes the logarithms of the full norms by
   `O(1)`.  The same formulas hold for exponential tilting.  This rigorously
   explains the square-root scale seen in the finite LP, but does not prove
   that the LP optimum has that scale.

4. **A modulated compact positive-definite base can harvest a noncentral
   atom.**  The compact-transfer carrier is not intrinsically tied to
   `w_0`.  Optimizing the modulation gives exactly a smoothed convolution
   maximum.  An isolated atom, or a cluster on which the convolution kernel
   has coherent sign, can therefore be harvested at the resolution of the
   compact base.  This changes the remaining convex problem from a central
   radial depth to a best-antipode/best-resolvable-cluster depth.
   Caratheodory alone guarantees only an atom of weight
   `1/(M+1)=Y_c^(-1+o(1))`; it does not guarantee isolation or prevent
   cancellation inside the smoothed cluster.  The modulation must also
   retain a strict margin inside the available frequency aperture.

The useful new separation is therefore

```text
positive prime-power moments on the Bohr torus:     SOLVED;
compact factorization after a finite-band solution: SOLVED;
polynomial-time scalar-orbit realization:           OPEN;
Riesz/tilt plus stable Gram correction:              FIXED-POWER ONLY.
                                                               (1.8)
```

## 2. An exact unrestricted-frequency theorem

Let the active logarithmic window be a fixed compact interval `U`, and put

```text
K_p={k>=1: log(p^k/Y_c) belongs to U},
s_p=abs(K_p),
s_*=max_p s_p.                                      (2.1)
```

Since successive powers of `p` are separated by `log p`,

```text
s_* <= 1+diam(U)/log 2.                             (2.2)
```

In particular, multiplicities belonging to one base prime are uniformly
bounded.  If a prefix of all powers `1<=k<=K_p` is imposed instead, the same
argument below works with `s_*<<log Y_c`; this is the source of the
logarithmic rather than constant torus scale in that stronger problem.

### 2.1 The prime-coordinate construction

First suppose that the center coordinate is independent of the active
prime coordinates.  Write `z_0` for that coordinate and `z_p` for the
coordinate belonging to `log p`.  Fix `c=1/4` and give the center coordinate
the strictly positive density

```text
g_0(theta_0)=1+2*c*cos(theta_0),
E[conj(z_0)]=c.                                     (2.3)
```

For every active base prime put, with normalized Haar measure on the circle,

```text
f_p(theta)
 =1-2*(r/c)*sum_(k in K_p) cos(k*theta).             (2.4)
```

If

```text
0<r<c/(2*s_*),                                      (2.5)
```

then `f_p` is a strictly positive probability density.  Orthogonality of
circle characters gives

```text
integral z_p^k*f_p(z_p) dz_p=-r/c
                         for every k in K_p.         (2.6)
```

Taking the product over `p`, and recalling that the node character is

```text
chi_(p,k)(z)=z_p^k*conj(z_0),                       (2.7)
```

proves (1.2) with a fixed `r` on the compact torus.  All coordinate
densities are strictly positive, a fact used in the scalar-orbit descent
below.

There is an equivalent atomic version.  The probability measure uniform on
the nonidentity `(K+1)`-st roots of unity has moments `-1/K` for
`1<=k<=K`.  Mixing it with Haar gives any common moment in that range.
The center factor then rescales it as above.  Formula (2.4) is more
convenient because it is strictly positive and its condition numbers can be
computed exactly.

### 2.2 Rational centers

Now let

```text
Y_c=A/B,             gcd(A,B)=1,                    (2.8)
```

with `A,B` of polynomial height in `Y_c`; this includes `Y+1/2`.  Introduce
one circle coordinate for every prime which divides `AB` or occurs as an
active base, and let

```text
w(z)=product_q z_q^(v_q(A)-v_q(B)).                 (2.9)
```

Then `w` is the center character and

```text
chi_(p,k)=z_p^k*conj(w).                           (2.10)
```

Call a base prime exceptional if it divides `AB`, and let `E` be the number
of distinct active exceptional characters, with inverse duplicates counted
once.  On the exceptional-coordinate torus use

```text
g(z)=1+2*c*Re(w(z))
        -2*r*sum_(chi in E) Re(chi(z)),             (2.11)
```

where `c=1/4`.  Away from the degenerate cases `n=Y_c` and `n=Y_c^2`, which
are avoided by the half-integer fixed-window centering, the displayed
characters are distinct from `1,w,w^(-1)`.  Character orthogonality gives

```text
integral conj(w)*g=c,
integral chi*g=-r             (chi exceptional).   (2.12)
```

Moreover

```text
g>=1-2*c-2*r*E>=0             if r<=1/(4*E).        (2.13)
```

For each nonexceptional `p`, use (2.4), with its parameter `r/c=4r`.  The product
of these densities and `g` then has

```text
E[z_p^k*conj(w)]
 =E[z_p^k]*E[conj(w)]
 =(-r/c)*c=-r                                      (2.14)
```

for nonexceptional bases, while (2.12) handles the exceptional ones.
It is positive provided

```text
r < min(1/(8*s_*),1/(4*E)).                        (2.15)
```

The elementary bounds

```text
E<=s_* * omega(AB)<<_U log Y_c                     (2.16)
```

prove (1.4).  Using the standard maximal-order estimate for `omega` improves
the last denominator to `log Y_c/log log Y_c`, but the crude logarithmic
bound already has the required subpower size.

### 2.3 Return to a scalar spectral measure

For a rational center, unique factorization says that the real numbers
`log p`, over the distinct primes occurring in the active nodes or the
center, are linearly independent over the rationals.  Hence the continuous
orbit

```text
xi -> (exp(i*xi*log p))_p                          (2.17)
```

is dense in the full prime-coordinate torus, and the center phase is the
character `w` of those coordinates.  For the independent-center construction
of Section 2.1, include the additional coordinate
`exp(i*xi*log Y_c)`; the multiplicative-genericity hypothesis is exactly the
rational independence needed for density in this enlarged torus.  Every
positive tail of either orbit is dense as well.

Take `r` strictly inside the relevant bound (2.5) or (2.15).  The density
constructed above is strictly positive, and its moment vector `-r*1` is in
the relative interior of the
convex hull of the torus character map.  A standard finite-dimensional
convexity argument now applies: express the point in the interior of a
simplex, approximate the simplex vertices by tail-orbit points, and adjust
the barycentric weights.  Thus, for every prescribed `R`, there are
finitely many

```text
xi_l>=R,       a_l>0,       sum_l a_l=1            (2.18)
```

such that

```text
sum_l a_l*cos(xi_l*u_n)=-r                         (2.19)
```

for every active node.  Symmetrizing the atoms gives an even measure.
Caratheodory permits at most `M+1` noncentral atoms.

This proves the unrestricted-frequency claim.  Density of the orbit gives
no useful upper bound for the largest `xi_l`.  In particular, (2.18) does
not put the atoms below `T=Y_c^(1/d)`.

## 3. Exact Riesz-product condition numbers

The same construction shows why pulling the torus density back to a short
scalar orbit is expensive.  For clarity begin with `M` independent
characters and

```text
P_r(theta_1,...,theta_M)
 =product_(j=1)^M [1-2*r*cos(theta_j)].              (3.1)
```

Unique factorization makes every distinct exponent vector a distinct Bohr
frequency.  Therefore the Wiener norm and squared `L^2` norm are exactly

```text
||P_r||_A=(1+2*r)^M,
||P_r||_2^2=(1+2*r^2)^M.                            (3.2)
```

For the grouped prime-power factor of (2.4), with its displayed parameter
written here simply as `r`, the exact formulas are

```text
||P_r||_A=product_p (1+2*s_p*r),
||P_r||_2^2=product_p (1+2*s_p*r^2).                (3.3)
```

The center constructions change only absolute factors: their nonexceptional
prime factors use `r/c=4r`, while the independent center density or the
exceptional factor contributes one additional bounded trigonometric
polynomial.  Thus (3.3) gives for the variable prime-factor part, whenever
`r=o(1)`,

```text
log ||P_r||_A=Theta(r*M),
log ||P_r||_2^2=Theta(r^2*M).                       (3.4)
```

For the full density the two right sides are `O(1)+Theta(r*M)` and
`O(1)+Theta(r^2*M)`, respectively.  The additive constants are immaterial
in the barrier regimes below.

The prime number theorem, with the higher powers estimated trivially,
gives for a nonempty fixed logarithmic shell

```text
M=Theta(Y_c/log Y_c)+O(sqrt(Y_c)*log Y_c)
  =Y_c^(1+o(1)).                                    (3.5)
```

Thus the torus-scale choice `r=1/log Y_c` has

```text
||P_r||_2
 =exp(Theta(Y_c/(log Y_c)^3)),                      (3.6)
```

already before paying for localization of the center coordinate.  It is
far beyond polynomial conditioning.

### 3.1 Degree mass and what unique factorization actually controls

Count the degree of a Fourier monomial by the number of nonconstant
base-prime factors used.  The generating polynomials for its absolute
Wiener mass and squared Fourier mass are

```text
product_p (1+2*s_p*r*z),
product_p (1+2*s_p*r^2*z),                          (3.7)
```

respectively.  After normalization, these are Poisson-binomial laws with
means

```text
Theta(r*M),              Theta(r^2*M).              (3.8)
```

Consequently, for every fixed degree `q`:

```text
r*M -> infinity
 => the degree<=q part carries o(1) of the Wiener mass;

r^2*M -> infinity
 => the degree<=q part carries o(1) of the squared L2 mass.       (3.9)
```

This is an exact mass statement, not a heuristic about random phases.

For the finite-interval descent, now specialize to the polynomial-height
rational-center case of Section 2.2, which includes the half-integer setup.
The generic-center theorem of Section 2.1 has no analogous Diophantine lower
bound from unique factorization alone.  Average the pulled-back product on a
scalar interval of length `H=T=Y_c^(1/d)`.  A nontrivial degree-`q` character
is `exp(i*xi*log(A'/B'))` with rational height at most `Y_c^O(q)`.
Unique factorization gives

```text
abs(log(A'/B')) >= Y_c^(-O(q)),                     (3.10)
```

and hence

```text
abs[H^(-1)*integral_I exp(i*xi*log(A/B)) dxi]
 <=min(1,2/(H*abs(log(A'/B')))).                    (3.11)
```

For fixed `d`, (3.11) gives uniform diagonal control only through a fixed
degree depending on `d`.  Equations (3.9)--(3.11) prove the following
mechanism barrier.

### Theorem 3.1 (finite-degree Riesz transfer barrier)

For the prime-power Riesz product on a polynomial interval at such a
rational center:

1. the bounded-degree part can carry a fixed fraction of the total Wiener
   mass only if `r*M=O_d(1)`;
2. the bounded-degree part can carry a fixed fraction of the total squared
   `L^2` mass only if `r^2*M=O_d(1)`;
3. even the more permissive requirement that the full `L^2` norm and its
   Gram/inverse-function conditioning be at most polynomial in `Y_c` forces
   `r^2*M=O_d(log Y_c)`.

In particular these proof modes give at best

```text
r=Y_c^(-1+o(1))                  (Wiener/absolute),
r=Y_c^(-1/2+o(1))                (L2/Gram).          (3.12)
```

The theorem does not assert that high-degree near-relational terms cannot
cancel in the actual scalar orbit.  It asserts that exact multiplicative
independence plus a stable low-degree correction does not prove that
cancellation.  Controlling it would be the new arithmetic early-return
theorem.

## 4. Exponential tilting has the same barrier

The most favorable independent-coordinate exponential tilt is

```text
Q_lambda(theta)
 =exp(-lambda*cos(theta))/I_0(lambda).               (4.1)
```

Its first moment is

```text
integral exp(i*theta)Q_lambda(theta)dtheta
 =-I_1(lambda)/I_0(lambda)=:-r_lambda.               (4.2)
```

The Bessel expansion gives the exact one-coordinate norms

```text
||Q_lambda||_A=e^lambda/I_0(lambda),
||Q_lambda||_2^2=I_0(2*lambda)/I_0(lambda)^2.        (4.3)
```

As `lambda->0`,

```text
r_lambda=lambda/2+O(lambda^3),
log ||Q_lambda||_A=2*r_lambda+O(r_lambda^2),
log ||Q_lambda||_2^2=2*r_lambda^2+O(r_lambda^4).     (4.4)
```

For `M` independent nodes the logarithms in (4.4) multiply by `M`.  Under
the same rational-center finite-degree descent as in Theorem 3.1,
exponential tilting followed by an inverse-function or Gram correction with
subpower conditioning again forces

```text
r_lambda<=Y_c^(-1/2+o(1)).                          (4.5)
```

Allowing separate parameters `lambda_j` replaces `M*r^2` by
`sum_j r_j^2`; it does not improve a common negative moment.  Products
`1-epsilon*cos` have the identical Wiener/`L^2` dichotomy.  Thus the three
suggested positive constructions all meet the same exact conditioning
wall.

## 5. Modulated positive-definite bases and the heaviest-cluster gate

Let

```text
mu=sum_j w_j*delta_(xi_j),
phi(u)=integral exp(i*xi*u)dmu(xi),                  (5.1)
```

be any positive atomic solution of the zero constraints.  Let `B` be a
fixed smooth compact positive-definite base and let `sigma` be any
probability measure.  The modulated base

```text
B_sigma(u)=B(u)*integral exp(i*eta*u)d sigma(eta)    (5.2)
```

is again positive definite.  Put

```text
K_alpha(s)=integral B(u)*exp(alpha*u+i*s*u)du.       (5.3)
```

The off-axis carrier of `B_sigma*phi` is exactly

```text
C_(mu,sigma)(alpha)
 =integral integral K_alpha(xi+eta)
                    dmu(xi)d sigma(eta).             (5.4)
```

Products preserve every prime zero of `phi`.  Since (5.4) is linear in the
probability measure `sigma`,

```text
sup_sigma abs C_(mu,sigma)(alpha)
 =sup_eta abs integral K_alpha(xi+eta)dmu(xi),       (5.5)
```

when complex modulation is allowed.  For a real even modulation, replace
the right side by the corresponding symmetrization at `eta` and `-eta`.

Equation (5.5) is the exact answer to the modulation question.  Because
`K_alpha` is rapidly decreasing, it is a smoothed local-mass functional,
with the phase and possible cancellation of `K_alpha` retained.  If an atom
of weight `h` is separated from the other atoms by a growing distance,
choosing `eta=-xi_j` gives

```text
C_(mu,delta_(-xi_j))(alpha)
 =h*K_alpha(0)+O_A(gap^(-A)).                       (5.6)
```

More generally (5.5) harvests a cluster only when its `K_alpha`-weighted
contributions have coherent sign; the exact convolution in (5.5), rather
than unsigned cluster mass, is the invariant statement.  The central atom
is only the special isolated cluster at zero.

For a chosen atom `xi_*`, define

```text
v(xi)=(cos(xi*u_n))_n,
K=conv{v(xi):Y_c<=abs(xi)<=T}.                       (5.7)
```

The largest possible weight `h(xi_*)` of that atom in a zero-moment
probability measure is equivalently

```text
h(xi_*)=r_*/(1+r_*),
r_*=sup{r>=0:-r*v(xi_*) belongs to K}.              (5.8)
```

Thus modulation replaces the central ray `-r*1` by the best antipodal ray
`-r*v(xi_*)`.  It is a real enlargement of the search space.  It is not an
automatic subpower theorem:

```text
Caratheodory => max_j w_j>=1/(M+1)=Y_c^(-1+o(1)),   (5.9)
```

and no stronger lower bound for the actual prime-log curve is proved here.

There is also an aperture condition.  Modulation shifts the spectral
centers, and multiplication convolves them.  To descend to the finite
Gabor packet without overflow, the selected cluster and all material
convolution frequencies must remain a growing margin inside the allowed
`[-T,T]` aperture.  A solution whose atoms sit at the endpoint `T` does not
automatically have that margin.

## 6. What remains

The positive spectral route is now narrower than a generic moment problem.
The exact unresolved statement is one of the following genuinely
quantitative alternatives:

```text
(A) -Y_c^(-o(1))*1 belongs to
    conv{v(xi):Y_c<=abs(xi)<=T};                    (6.1)

(B) some xi_* with aperture margin has
    -Y_c^(-o(1))*v(xi_*) in the same convex hull;   (6.2)

(C) a resolvable spectral cluster of a zero-moment
    measure has K_alpha-smoothed carrier Y_c^(-o(1)).             (6.3)
```

The torus theorem proves all analogues after deleting the upper bound
`abs(xi)<=T`.  The norm identities and bounded-degree analysis prove that the
audited absolute-Wiener or subpower-conditioned Gram implementations of
Riesz products, products `1-epsilon*cos`, and exponential tilting cannot
transfer that theorem at subpower `r`.  This does not exclude a new
high-degree absolute estimate.  An escape must obtain additional control of
the high-degree near-relations of the actual prime-log orbit, whether by
coherent cancellation or by a stronger absolute estimate.  That is precisely
the arithmetic content which unique factorization alone does not provide.

No zeta zero bound is changed by this report.
