# The constrained sharp prime edge is a confluent Loewner problem

Status: exact structural reduction and matched-scale theorem card, 2026-08-11.
This note corrects the earlier displacement audit for the sharp Zeta23
matrix.  It proves no prime lower edge and no zero-free strip.

## 1. Verdict

The sharp critical-lattice matrix has substantially more structure than was
previously recorded.

1. After the harmless sign conjugation `(-1)^k`, the **whole** sharp matrix,
   not merely one prime constituent, is a confluent Loewner matrix.  Its
   commutator with `diag(tau_k)` has rank at most two.  This applies
   separately to the archimedean, pole, and prime densities and to their
   exact sum.
2. Compression to the endpoint-jet moment-null space retains rank-two
   displacement.  In a discrete orthogonal-polynomial basis, the compressed
   coordinate operator is a Jacobi matrix and the displacement is generated
   by one boundary vector.
3. For the prime density the entire matrix is determined by two scalar
   transition-length Dirichlet polynomials

   ```text
   A_X(tau)=sum_(n<=X) Lambda(n)/sqrt(n) sin(tau log n),
   D_X(tau)=sum_(n<=X) Lambda(n)/sqrt(n)
                         *(L-log n) cos(tau log n).       (1.1)
   ```

   The off-diagonal part is a discrete Hilbert commutator of `A_X`; the
   confluent diagonal is exactly `-2D_X(tau_k)`.  In particular, endpoint
   jets do not erase the full transition-length prime polynomial.
4. The Loewner identity gives exact determinant, Pick, and Sturm/LDL
   formulations, but no sign.  Rank-two displacement alone permits an
   arbitrary confluent diagonal, and signed smooth scalar multipliers realize
   every such finite set of Loewner data.
5. A uniform fixed-power bound for the two polynomials in (1.1) is a clean
   sufficient prime-edge input only when its saving beats the quantified loss
   in the carrier margin.  More generally, the prime lower edge must be
   `o(K)` at the actual normalized carrier scale `K`.  Existing
   first/two-moment and completed Type-II inputs do not prove such a matched
   estimate.  The moment requirements remain

   ```text
   alpha*lambda*p>1       to exclude one depth-alpha spike,
   lambda*p<2             for the unconditional diagonal range,  (1.2)
   ```

   and are disjoint for every `alpha<1/2`.

Thus the new structure is genuine and useful: it replaces a matrix-valued
mystery by a scalar confluent-Loewner/prime-polynomial target.  Its arbitrary
diagonal is also a precise obstruction.  No fixed-depth edge follows without
new arithmetic cancellation or a direct Pick-matrix inequality.

## 2. The exact sharp Loewner matrix

Let

```text
h       = 2*pi/L,
tau_k   = tau_0+k*h,                  0<=k<d,
phi     = 1_[-L/2,L/2],
g_k(t)  = phiHat(t-tau_k),
S(t)    = sin(L*(t-tau_0)/2),
eps_k   = (-1)^k,
Delta   = diag(tau_0,...,tau_(d-1)).
```

For a real smooth weight `w` satisfying

```text
w(t)=O(log(2+abs(t))),                              (2.1)
```

define the canonical sharp matrix

```text
G_w(k,l)=integral_R g_k(t)g_l(t)w(t)dt,
H_w=diag(eps_k)*G_w*diag(eps_k).                    (2.2)
```

This covers `w=mu`, `Pi_X`, `P_X`, and `nu_X`.  The individual sharp
coordinates need not be inserted into the zero-side explicit formula.  The
prime-side integral (2.2) is canonical, and its restriction to the endpoint
space `V_m`, `m>=3`, is an admissible `C_c^2` Weil compression.

### Theorem 2.1 (confluent Loewner and common rank-two displacement)

For all `k,l`, with removable values at the grid points,

```text
H_w(k,l)=4 integral_R S(t)^2 w(t)
                    /((t-tau_k)*(t-tau_l))dt.        (2.3)
```

There is a regularized real Cauchy transform

```text
J_w(a)=PV integral_R 4*S(t)^2*w(t)
              *(1/(t-a)-t/(1+t^2))dt                (2.4)
```

such that

```text
H_w(k,l)=(J_w(tau_k)-J_w(tau_l))/(tau_k-tau_l),
                                                    k!=l,
H_w(k,k)=J_w'(tau_k).                                (2.5)
```

Consequently

```text
[Delta,H_w]=j*1^T-1*j^T,
j_k=J_w(tau_k),
rank([Delta,H_w])<=2.                                (2.6)
```

The same statement holds for each summand of `nu_X` and for their sum; the
rank does not accumulate with the number of prime frequencies.

#### Proof

Critical spacing gives the common sine factor

```text
g_k(t)=2*(-1)^k*S(t)/(t-tau_k),                      (2.7)
```

which proves (2.3).  Its integrand is
`O(log(2+abs(t))/t^2)` at infinity and has removable grid singularities.
The subtraction in (2.4) makes the Cauchy transform absolutely convergent at
infinity; only the ordinary local principal value remains for a general
`a`.

At a grid point, `S(t)^2` has a double zero.  Thus `J_w(tau_k)` needs no
local principal value after an irrelevant common constant is fixed, and a
difference quotient at `tau_k` is dominated away from the point.  Locally,
writing `u=t-tau_k`, its integrand is `u^2 r(u)/(u-a+tau_k)` with smooth
`r`; the principal-value difference quotient tends to `r(u)`.  Hence

```text
J_w'(tau_k)=4 integral S(t)^2 w(t)/(t-tau_k)^2 dt.
```

For distinct nodes,

```text
1/(t-tau_k)-1/(t-tau_l)
 =(tau_k-tau_l)/((t-tau_k)*(t-tau_l)),
```

which proves (2.5).  Multiplying by `tau_k-tau_l` gives (2.6).  QED

For later use, the constant multiplier satisfies, up to an additive
constant,

```text
J_1(a)=2*pi*sin(L*(a-tau_0)),                         (2.8)
```

so `H_1=2*pi*L*I_d`.  Therefore

```text
H_w+kappa*I_d
```

is the confluent Loewner matrix of

```text
J_w(a)+(kappa/L)*sin(L*(a-tau_0)).                   (2.9)
```

Equation (2.9) is the exact shifted-edge scalarization.

## 3. Exact one-prime and full-prime data

Put `y=log n`, `0<y<L`, and `a_n=Lambda(n)/sqrt(n)`.  The elementary
principal-value integral behind one cosine constituent is

### Lemma 3.1 (one-prime Cauchy transform)

For real `a`, up to the common regularization convention in (2.4),

```text
C_y(a):=PV integral_R 4*S(t)^2*cos(y*t)/(t-a)dt
 =-2*pi*sin(a*y)
   +2*pi*sin(L*(a-tau_0))*cos(a*y).                  (3.1)
```

At the grid points,

```text
C_y(tau_k)   =-2*pi*sin(tau_k*y),
C_y'(tau_k) = 2*pi*(L-y)*cos(tau_k*y).               (3.2)
```

#### Proof

Use

```text
4*S(t)^2=2-2*cos(L*(t-tau_0))
```

and, for `q>0`,

```text
PV integral cos(q*t-b)/(t-a)dt=-pi*sin(q*a-b).
```

Product-to-sum on the second cosine gives

```text
pi*sin((L+y)*a-L*tau_0)
+pi*sin((L-y)*a-L*tau_0),
```

which is the second term of (3.1).  Since
`L*(tau_k-tau_0)=2*pi*k`, evaluation and differentiation give (3.2).  QED

Recall

```text
P_X(t)=-(1/pi) sum_(n<=X) a_n*cos(t*log n).          (3.3)
```

Define on the critical grid

```text
A_k=A_X(tau_k),
D_k=D_X(tau_k),                                     (3.4)
```

with `A_X,D_X` as in (1.1).  Lemma 3.1 gives the exact prime matrix

```text
H_P(k,l)=2*(A_k-A_l)/(tau_k-tau_l),                 k!=l,
H_P(k,k)=-2*D_k.                                    (3.5)
```

In particular the diagonal is not the derivative of the bare grid
interpolant `2*A_X`: the cardinal term in (3.1) supplies the indispensable
`L*cos(tau_k*y)` correction.

Let `K_d` be the finite discrete Hilbert matrix

```text
K_d(k,l)=1/(k-l), k!=l,       K_d(k,k)=0.            (3.6)
```

The infinite convolution with kernel `1/r` has Fourier multiplier of
absolute value at most `pi`, so its finite compression satisfies

```text
norm(K_d)<=pi.                                      (3.7)
```

Writing `M_A=diag(A_0,...,A_(d-1))`, (3.5) becomes

```text
H_P=-2*diag(D_k)+(2/h)*(M_A*K_d-K_d*M_A).            (3.8)
```

Since constants commute with `K_d`, the elementary operator bound is

```text
norm(H_P)
 <=2*max_k abs(D_k)+L*osc_k(A_k),                   (3.9)

osc_k(A_k)=max_k A_k-min_k A_k.
```

Thus

```text
lambda_min(H_P)
 >=-2*max_k abs(D_k)-L*osc_k(A_k).                  (3.10)
```

This is a rigorous sufficient scalar lower-edge estimate.  It is not a
necessary condition for every possible structured proof: signs in the
diagonal and commutator may interact more favorably than the triangle
inequality in (3.9).

## 4. What endpoint compression preserves

After the sign conjugation, the endpoint space is

```text
W_m={x in C^d: sum_k x_k*tau_k^r=0, 0<=r<m}.         (4.1)
```

Let `P_m` be its orthogonal projection and put

```text
A_m=P_m*Delta*P_m |_Wm,
B_m=P_m*H_w*P_m |_Wm.                               (4.2)
```

### Theorem 4.1 (boundary-generated rank-two compression)

Let `q_(m-1)` be the unit discrete orthogonal polynomial of degree `m-1`
for the uniform measure on the nodes `tau_k`, and define

```text
r=P_m*Delta*q_(m-1),
s=P_m*H_w*q_(m-1).                                  (4.3)
```

Then

```text
[A_m,B_m]=s*r^*-r*s^*,
rank([A_m,B_m])<=2.                                  (4.4)
```

In the orthonormal-polynomial basis
`q_m,q_(m+1),...,q_(d-1)`, `A_m` is the trailing irreducible Jacobi matrix
and `r` is a nonzero multiple of its first basis vector.

#### Proof

Let `Q_m=I-P_m`.  Since `P_m*1=0`, compressing (2.6) gives

```text
P_m*[Delta,H_w]*P_m=0.                              (4.5)
```

Multiplication by `Delta` maps `W_m` into `W_(m-1)`.  The quotient
`W_(m-1)/W_m` is one-dimensional, so

```text
R=Q_m*Delta*P_m=q_(m-1)*r^*                         (4.6)
```

has rank one.  Expanding the compressed commutator and using (4.5),

```text
[A_m,B_m]
 =-P_m*Delta*Q_m*H_w*P_m+P_m*H_w*Q_m*Delta*P_m
 =-r*s^*+s*r^*.
```

The three-term recurrence for discrete orthogonal polynomials gives the
last assertion.  QED

There is an exact scalar Pick representation of (4.4).  Diagonalize
`A_m u_i=lambda_i u_i` and put

```text
rho_i=<u_i,r>,       sigma_i=<u_i,s>,
varphi_i=sigma_i/rho_i.                              (4.7)
```

Irreducibility and cyclicity of the first Jacobi vector give `rho_i!=0`.
For `i!=j`,

```text
<u_i,B_m u_j>
 =rho_i*rho_j*(varphi_i-varphi_j)/(lambda_i-lambda_j).  (4.8)
```

After congruence by `diag(rho_i)^(-1)`, the diagonal entries are free
confluent data.  Equivalently, there is a unique Hermite interpolation polynomial
`F_m` with

```text
F_m(lambda_i)=varphi_i,
F_m'(lambda_i)=<u_i,B_m u_i>/rho_i^2,                (4.9)
```

and the congruent matrix is the confluent Loewner matrix of `F_m`.
Adding `kappa*I` changes the derivative data in (4.9) by
`kappa/rho_i^2`.

This gives an exact LDL/Sturm/Pick test.  It does not reduce the arithmetic
to monotonicity of one ordinary scalar sequence: positivity of a Loewner
matrix is finite matrix monotonicity, and the independent derivative data in
(4.9) remain.  In the prime case those derivative data are precisely the
transformed version of `D_X`.

## 5. Difference basis, time domain, and minors

The moment-null space has a useful nonorthogonal basis.  Let `S_m` be the
`d` by `d-m` matrix whose `j`-th column has entries

```text
(S_m)_(j+r,j)=(-1)^r*binom(m,r),       0<=r<=m.       (5.1)
```

Then `range(S_m)=W_m`.  For `x=S_m b`,

```text
R_x(t)=sum_k x_k/(t-tau_k)
      =sum_j b_j*r_(m,j)(t),

r_(m,j)(t)
 =sum_(r=0)^m (-1)^r*binom(m,r)/(t-tau_(j+r))
 =(-1)^m*m!*h^m/product_(r=0)^m(t-tau_(j+r)).        (5.2)
```

The sharp transform is exactly

```text
F_x(t)=2*S(t)*R_x(t).                                (5.3)
```

If

```text
mathcal B_m=S_m^T*H_w*S_m,
mathcal M_m=S_m^T*S_m,                               (5.4)
```

then the raw lower-edge assertion on `W_m` is equivalent to

```text
mathcal B_m+kappa*mathcal M_m >= 0.                  (5.5)
```

For every index set `I={i_1,...,i_r}` of columns, Andreief gives

```text
det[(mathcal B_m+kappa*mathcal M_m)_I]
 =1/r! integral_(R^r)
      det[2*S(t_b)*r_(m,i_a)(t_b)]_(a,b<=r)^2
      product_(b=1)^r
        (w(t_b)+kappa/(2*pi*L))dt_b.                 (5.6)
```

For the uncompressed matrix and a node set `I`, the Cauchy determinant makes
this still more explicit:

```text
det[(H_w)_I]
 =Delta(tau_I)^2/r! integral_(R^r)
      Delta(t_1,...,t_r)^2
      *product_b(4*S(t_b)^2*w(t_b))
      /product_(a,b)(t_b-tau_(i_a))^2
      dt_1...dt_r.                                  (5.7)
```

For strict positivity, Sylvester's criterion applies to the leading versions
of (5.6); for semidefinite positivity, all principal minors are required.
The kernel squares in (5.6)--(5.7) are nonnegative, but `w=P_X` and
`w=nu_X` are signed.  Expanding their products retains prime products through
the full degree.  Low displacement therefore does not turn the exterior
hierarchy into one- or two-prime data.

The exact time-domain prime form says the same thing without matrices.  If

```text
X_c(z)=sum_k x_k*z^k=(1-z)^m*B(z),
f_x(u)=1_[-L/2,L/2](u)*exp(-i*tau_0*u)
       *X_c(-exp(-i*h*u)),                            (5.8)
```

then

```text
x^*H_P*x
 =-2 sum_(n<=X) a_n Re[
       exp(i*tau_0*y_n)
       *integral_(-L/2)^(L/2-y_n)
          X_c(-exp(-i*h*u))
          *conj(X_c(-exp(-i*h*(u+y_n))))du].         (5.9)
```

The factor `(1+exp(-i*h*u))^m` in (5.8) gives the endpoint jets.  The
remaining polynomial `B` has degree `d-m-1` and is adaptive.  Formula (5.9)
does not furnish a uniform correlation loss, consistently with the surviving
diagonal `D_X` in (3.5).

## 6. Exact structural obstruction

Low displacement by itself has no lower-edge content.

### Proposition 6.1 (arbitrary finite confluent data)

For fixed distinct nodes `tau_0,...,tau_(d-1)`, the linear map from real
compactly supported smooth signed multipliers `w` to

```text
(J_w(tau_k)-J_w(tau_0))_(1<=k<d),
(J_w'(tau_k))_(0<=k<d)                               (6.1)
```

is surjective onto `R^(2d-1)`.

#### Proof

The corresponding `2d-1` kernel functions, after dividing by the common
nonzero factor `4*S(t)^2` off the grid, are

```text
1/(t-tau_k)-1/(t-tau_0),       1<=k<d,
1/(t-tau_k)^2,                 0<=k<d.               (6.2)
```

They are linearly independent by uniqueness of partial fractions: the
double-pole coefficients vanish first, followed by every simple-pole
coefficient.  Therefore there are `2d-1` real points away from the grid for
which their evaluation matrix is invertible.  Narrow smooth bumps about
those points retain invertibility, and solving for their real weights
realizes arbitrary data.  QED

In particular one may set all Loewner values equal and choose the derivative
data arbitrarily; the resulting matrix is any prescribed diagonal matrix.
The same conclusion follows abstractly from Hermite interpolation.  Thus
neither (2.6), (4.4), scalar-measure origin, nor full matrix rank can imply a
lower edge.  The special arithmetic values (3.5), especially `D_X`, must be
used.

## 7. Matched-depth arithmetic card and the `p*lambda<2` barrier

Write

```text
X=exp(L)=T^(lambda+o(1)).                            (7.1)
```

A full-lattice pair at fixed depth `alpha` has negative edge, in the raw
sharp normalization,

```text
K_alpha asymp_alpha L*exp(alpha*L)
                    =L*X^alpha.                     (7.2)
```

Define the exact scalar control quantity

```text
B_X(T)=osc_(0<=k<d) A_X(tau_k)
       +(2/L)*max_(0<=k<d) abs(D_X(tau_k)).           (7.3)
```

If the actual carrier margin in the isolated-zero normalization is

```text
K=(X^alpha/L)*r_T,
```

then (3.10) gives normalized prime lower-edge error at most `B_X/L`, so the
scalar route closes the prime gate only under the matched estimate

```text
B_X(T)=o(X^alpha*r_T).                              (7.3a)
```

Equivalently, the normalized prime lower-edge error must be `o(K)`.
The tail-rate carrier target
`log(1/K)=o(eta^2*T/log T)` does not imply that `r_T` is bounded below, or
even that it loses only a fixed power of `X`.  Thus that target and the bare
fixed-saving estimate `B_X=o(X^alpha)` do **not** automatically combine.  One
must either prove (7.3a) at the actual Schur margin or prove a matching
power-scale carrier bound, for example `K>=X^(alpha-o(1))/L`.  More generally, if
`r_T>=X^(-theta+o(1))` and `B_X<=X^(alpha-sigma+o(1))`, one needs
`sigma>theta`.

This matched scalar bound is sufficient, not logically necessary: a direct
constrained Pick inequality from (5.5) could exploit cancellation between
the diagonal and commutator without separately bounding them.  Its normalized
negative lower-edge error must still be `o(K)` at the same actual carrier
scale.

The trivial estimates give size `X^(1/2+o(1))` for `B_X`.  If `r_T` stays
bounded below, the sufficient card at depth `alpha_0` asks for a fixed saving
greater than `1/2-alpha_0`; a decaying `r_T` requires a correspondingly larger
saving.  Vaughan decomposition of the complex polynomial

```text
Z_X(tau)=sum_(n<=X) Lambda(n)n^(-1/2+i*tau)          (7.4)
```

must preserve both its imaginary oscillation and the completed derivative

```text
Re sum_(n<=X) Lambda(n)n^(-1/2+i*tau)*(L-log n).     (7.5)
```

Separating Type-I heads, the balanced Type-II term, or the cutoff derivative
and then taking absolute values does not prove (7.3a); all pieces have to be
recombined into (7.4)--(7.5), or directly into the Pick matrix (5.5).

The closest completed fixed-order Type-II theorem currently audited in this
repository has only Vinogradov--Korobov strength,

```text
X^(1/2)*exp(-c*(log X)^(3/5)*(loglog X)^(-1/5)),     (7.6)
```

for its scalar normalization, equivalently a saving exponent tending to
zero.  It concerns a completed fixed-window aggregate and does not by itself
instantiate the adaptive grid bound (7.3a).  Even a lossless transfer of
(7.6) would remain `X^(1/2-o(1))`, too large for every fixed
`alpha<1/2`.  See
[`TYPEII-FIXED-SAVING-THEOREM-CARD-2026-08-11.md`](TYPEII-FIXED-SAVING-THEOREM-CARD-2026-08-11.md).

The higher-moment obstruction is now visible already in the scalar data.
For even `p`, expanding a `p`-th moment of (7.4) produces two product blocks
of length `X^(p/2)`.  The unconditional diagonal/Rudnick--Sarnak range is

```text
lambda*p<2.                                          (7.7)
```

To exclude one grid-scale peak of size `X^alpha` from a bulk moment of size
`T^(1+o(1))`, even allowing the standard Bernstein-width conversion, one
needs

```text
X^(alpha*p)>T^(1+o(1)),
alpha*lambda*p>1.                                   (7.8)
```

No `p` satisfies (7.7)--(7.8) when `alpha<1/2`.  The boundary second moment
at `lambda=1` does not change the strict inequality.  Logarithmic weights in
`D_X` and endpoint finite differences do not shorten the product length;
the confluent diagonal in (3.5) is the fail-fast witness.

An almost-all formulation must also keep its quantifiers straight.  It would
suffice to remove an `o(T)` set of **base heights** while proving (7.3a) for
every grid coordinate at each remaining height, because a zero of ordinate
`gamma` belongs to `[T,2T]` for all `T in [gamma/2,gamma]`.  A mean theorem
for most ordinates or most pairs `(T,k)` does not supply this maximum: the
exceptional coordinate and the minimizing vector may depend on `T`.

## 8. Final theorem card

The exact constrained prime-edge problem is now:

```text
NECESSARY AND SUFFICIENT EDGE FORM:
  prove S_m^T*(H_nu+kappa*I)*S_m >= 0,
  equivalently B_m+kappa*M_m >= 0 in the raw coefficient metric,
  or the signed Andreief minors (5.6) have the required Pick sign.

EXACT PRIME DATA:
  off diagonal = discrete Hilbert commutator of A_X;
  confluent diagonal = -2 D_X;
  endpoint compression has boundary-generated displacement rank <=2.

MATCHED SUFFICIENT ARITHMETIC OPTION:
  write K=(X^alpha/L)*r_T for the actual normalized carrier margin and prove
  B_X=osc(A_X)+(2/L)*max(abs(D_X))=o(X^alpha*r_T)
  uniformly on the whole critical grid (or in the precise base-height
  almost-all sense above).

DIRECT PICK ALTERNATIVE:
  prove that the normalized constrained prime matrix has negative lower-edge
  error o(K) at that same actual carrier scale, without separately bounding
  A_X and D_X.

NOT SUPPLIED BY CURRENT INPUTS:
  displacement rank, Toeplitz positivity before twisting, endpoint jets,
  Andreief, the first two moments, the range lambda*p<2, or the currently
  audited completion-preserving Type-II estimates.
```

The Loewner correction materially narrows the missing arithmetic theorem,
but the arbitrary confluent diagonal prevents a structural sign argument.
Here `kappa` is a raw eigenvalue scale for `G`; conversion to the
isolated-zero normalization divides by `a*L^2`.
There is no claim here of a prime lower edge, a stable carrier margin, or a
zero-free strip.  The coupled carrier-rate and tail theorem card is
[`ZETA23-QUANTITATIVE-SIGNED-CARRIER-REDUCTION-2026-08-11.md`](ZETA23-QUANTITATIVE-SIGNED-CARRIER-REDUCTION-2026-08-11.md).
Its tail-scale target alone does not supply the matched prime comparison in
Section 7.
