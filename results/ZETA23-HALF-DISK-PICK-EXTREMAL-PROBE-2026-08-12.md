# The half-disk Pick extremal: exact finite SDP, sharp local tests, and the half-product signal

Status: exact affine SDP reduction, exact hostile two-node extremal, exact
half-density alternating-lattice construction, and exact five-point
affine-jet obstruction, 2026-08-12.  Floating finite-section experiments
support a half-product exponent in alternating configurations but do not
prove a uniform half-product theorem.  No zeta-zero bound or zero-free strip
is proved.

## 1. Verdict

The unrestricted causal problem is a genuine finite convex SDP.  If

```text
K_(j,k)=1/(z_j+conj(z_k)),       W=diag(w_0,...,w_M),
```

then the variable Pick condition is equivalently the **affine** LMI

```text
        [ K     W K ]
M(w) = [             ] >=0.                            (1.1)
        [ K W*   K   ]
```

The Schur complement of the lower-right `K` is

```text
K-W K W* = ((1-w_j conj(w_k))/(z_j+conj(z_k)))_(j,k). (1.2)
```

Thus maximizing a real `w_0=A` subject to

```text
Re[exp(-i theta_j)w_j]>=0                            (1.3)
```

is an ordinary real SDP after realification.  This is stronger
computationally than treating the nonlinear-looking Pick matrix directly.

Three exact tests give a fairly sharp picture.

1. One hostile conjugate pair costs only `Theta(a^-2)` when its phase is a
   half turn away.  Repeating identically oriented midpoint constraints in
   remote cells does not produce the critical exponential loss.
2. A genuinely winding, one-node-per-cell alternating lattice has an exact
   Schur solution of target size

   ```text
   1/sqrt(cosh a)=exp(-a/2+O(1)).                    (1.4)
   ```

   This is exactly the square root of the full critical-lattice Blaschke
   value `sech(a)`.  It is a rigorous positive half-product example, not a
   proof that every configuration admits such a solution.
3. A five-point cluster inside one phase cell has a positive dual dependence
   annihilating every affine analytic jet.  It forces a Schur interpolant to
   have double-zero-scale behavior at the cell center.  Therefore the literal
   rule “one occupied cell costs at most one simple Blaschke condition” is
   false unless the allowed within-cell geometry is restricted.

The surviving global conjecture is consequently subtler: real half-plane
constraints may have a half-product **total** cost after analytic sharing
between cells, even though an individual cluster can require multiplicity
two.  The present work neither proves nor falsifies that global statement.

## 2. The affine SDP and its numerical dual

Since `K>0`, (1.1) and (1.2) are equivalent.  The upper-right block is
linear in the real and imaginary parts of the `w_j`; all sign constraints
(1.3) are linear.  Convexity is therefore exact, not an artifact of a
relaxation.

For numerical conditioning, write `K=L_K L_K*` and apply the congruence
`diag(L_K^-1,L_K^-1)`.  The LMI becomes

```text
[ I  T(w) ]
[ T(w)* I ] >=0,       T(w)=L_K^-1 W L_K,           (2.1)
```

or equivalently `||T(w)||<=1`.

The companion code follows a logarithmic central path.  If `mu>0`, then

```text
Z=mu*M(w)^-1,       lambda_j=mu/h_j,
h_j=Re[exp(-i theta_j)w_j],                          (2.2)
```

are positive primal-dual variables.  The stationarity residual gives a
floating dual upper estimate as well as a strictly feasible lower estimate.
Explicitly, if the normalized affine pencil is `I+sum_i x_i A_i`, `H x>=0`,
the objective vector is `c`, and

```text
r_i=c_i+tr(Z A_i)+(H*lambda)_i,
```

then every feasible coordinate has `|x_i|<=1` (each is a real or imaginary
part of a Schur value), and weak duality gives

```text
c*x <= tr(Z)+||r||_1.                               (2.3)
```

This is the residual correction used by the code.
This is a controlled probe of the exact SDP, but it is **not** interval
arithmetic and its printed brackets are not proof certificates.

## 3. Exact hostile conjugate-pair extremal

Let the target be `z_0=x>0`, take nodes `z_+=x+iy`, `z_-=x-iy`, and impose

```text
Re w_+<=0,       Re w_-<=0.                          (3.1)
```

### Theorem 3.1

The exact maximum target value is `A_* = A(t_*)`, where

```text
A(t)= [y^2+2*x*y*t-(4*x^2+y^2)t^2]
      /[4*x^2+y^2+2*x*y*t-y^2*t^2],                 (3.2)

t_*=[-2*x^2-y^2+sqrt(4*x^4+5*x^2*y^2+y^4)]/(x*y).  (3.3)
```

With the node labels above, the extremal values are

```text
w_+=-i t_*,       w_-=+i t_*.                        (3.3a)
```

For fixed `y` and `x -> infinity`,

```text
t_*=y/(4x)+O(x^-3),
A_*=5*y^2/(16*x^2)+O(x^-4).                         (3.4)
```

By contrast, forcing both values to zero gives

```text
A_zero=y^2/(4*x^2+y^2)=y^2/(4*x^2)+O(x^-4).         (3.5)
```

Thus sign grouping improves this first hostile pair by the factor `5/4`
at leading order, but the cost is polynomial in the scaled depth, not the
critical exponential.

#### Proof

Reflection-conjugating and averaging any feasible Schur function makes it
real symmetric without decreasing its real target value.  If the common
real part of the conjugate node values is negative, convexly mixing with
the constant function `1` increases the target until both inequalities in
(3.1) are active.  Parameterize the resulting conjugate values as
`w_+=-i t`, `w_-=+i t`, with real `t`.

Substitution in the `3 x 3` Pick determinant gives one boundary factor

```text
A[-t^2 y^2+2txy+4x^2+y^2]
 +t^2(4x^2+y^2)-2txy-y^2=0,                         (3.6)
```

which is (3.2).  On the feasible branch the determinant and the `2 x 2`
principal minors give `A<=A(t)`.  Moreover

```text
A'(t)=-8*x^2*(x*y*t^2+(4*x^2+2*y^2)*t-x*y)
       /[4*x^2+y^2+2*x*y*t-y^2*t^2]^2.              (3.6a)
```

The quadratic in (3.6a) has exactly one root in `(0,1)` and its other root
is less than `-1`; hence the root in `(0,1)` is the global maximizer on the
admissible interval.  Its equation is

```text
t^2*x*y+4t*x^2+2t*y^2-x*y=0,                        (3.7)
```

whose positive root is (3.3).  Direct substitution verifies the remaining
principal minors are nonnegative.  Expanding (3.2)--(3.3) proves (3.4).

## 4. An exact alternating Toeplitz/lattice construction

Normalize the cell width to `2*pi` and fix the vertical line `Re(s)=a`.
For every integer `j`, put one node in cell `j` at ordinate

```text
y_j = 2*pi*j + pi,       j even,
y_j = 2*pi*j,            j odd,                     (4.1)
```

with `z_j=a-i y_j` and phase `theta_j=y_j`.  The Cauchy matrix on each
uniform sublattice is Toeplitz:

```text
K_(j,k)=1/[2a-i(y_j-y_k)].                           (4.2)
```

Define

```text
B_a(s)=sinh((s-a+i*pi)/4)/sinh((s+a+i*pi)/4),        (4.3)
U_a(s)=exp(-i arg B_a(a))*B_a(s).                    (4.4)
```

### Theorem 4.1

`U_a` is a right-half-plane inner function satisfying every half-disk
constraint in (4.1), and

```text
U_a(a)=1/sqrt(cosh a).                               (4.5)
```

The denominator zeros of (4.3) all have real part `-a`, so `B_a` is
analytic in the right half-plane.  On the imaginary axis its numerator and
denominator have equal modulus.  It is `4*pi*i`-periodic and tends uniformly
to a constant of modulus `exp(-a/2)` at the right edge of a truncated
period cell.  The maximum principle on those truncated cells therefore
gives `|B_a|<=1`, with unimodular boundary values: it is inner.

The even-cell nodes are exactly its zeros.  At every odd cell, periodicity
reduces the sign check to `y=2*pi`, where direct algebra gives

```text
Re[exp(-iy)U_a(a-iy)]=(cosh a)^(-3/2)>0.             (4.6)
```

The full odd-half-cell zero lattice has target product

```text
prod_(k>=0) ((2k+1)^2*pi^2)/[4a^2+(2k+1)^2*pi^2]
 =sech(a).                                           (4.7)
```

Therefore (4.5) is exactly the square root of (4.7).  This proves that the
half-product exponent is analytically attainable in a canonical winding
case.  It does **not** prove that (4.5) is the extremum even for this case,
nor that arbitrary jitter admits the same bound.

## 5. Exact five-point affine-jet obstruction

Fix `d=2/3`, `D=dL`, and a cell center

```text
delta_c=(2m_L+1)*pi/D.                               (5.1)
```

Take

```text
x=(-pi,-pi/2,0,pi/2,pi),
lambda=(1,1,1,1,8),
z_j=alpha-lambda_j/L-i(delta_c+x_j/(dL)).            (5.2)
```

Because `D delta_j=(2m_L+1)pi+x_j`, putting `V=-U` turns the physical
constraints into

```text
Re[exp(-i x_j)V(z_j)]>=0.                            (5.3)
```

Write `z_c=alpha-i delta_c`, `h_j=-lambda_j-i x_j/d`, and linearize

```text
V(z_c+h_j/L)=P+C h_j+O(L^-2),
P=V(z_c),       C=V'(z_c)/L.                        (5.4)
```

The five real affine-jet normals are

```text
n_j=(cos x_j,
     sin x_j,
     -lambda_j cos x_j-(x_j/d)sin x_j,
      (x_j/d)cos x_j-lambda_j sin x_j).              (5.5)
```

### Theorem 5.1

They have the exact positive dependence

```text
sum_j omega_j n_j=0,
omega=(1,14/(3*pi),2,14/(3*pi),1),                  (5.6)
```

while

```text
det(n_1,n_2,n_3,n_4)=9*pi^2/4 !=0.                  (5.7)
```

Consequently, if `delta_c` stays in a fixed compact set and `U` is Schur
and satisfies (5.3), then

```text
V(z_c)=O(L^-2),       V'(z_c)=O(L^-1).               (5.8)
```

If

```text
rho_c=|(alpha-z_c)/(alpha+conj(z_c))|
     =|delta_c|/sqrt(4alpha^2+delta_c^2),            (5.9)
```

two applications of Schwarz--Pick give

```text
|U(alpha)|<=rho_c^2+O(L^-1).                        (5.10)
```

#### Proof

Equations (5.6)--(5.7) are direct exact arithmetic.  Uniform Cauchy bounds
make every remainder in (5.4) `O(L^-2)`.  If all five exact margins are
nonnegative, (5.6) first bounds their affine parts on both sides by
`O(L^-2)`; (5.7) then gives `(P,C)=O(L^-2)`.  This is (5.8).  Apply the
Schur algorithm at `z_c`: the first normalized Schur remainder has value
`O(L^-1)` at `z_c`, so a second Schwarz--Pick step bounds the value at the
target by the square of the pseudohyperbolic distance, plus `O(L^-1)`.

Thus one phase cell can force two local Schur degrees.  The obstruction is
stable under sufficiently small inward phase perturbations because positive
spanning is open.  It rules out a universal *simple-root-per-cluster*
compressor, not a global half-product theorem that shares analytic degrees
between cells.

## 6. Floating finite-section evidence

For symmetric reflected lists with positive-cell offsets alternating between
`pi` and `0.03`, with `n=a` positive cells and their reflections, the SDP
probe gives:

| `a` | primal `A` | floating dual upper | all-zero product | `-log(A)/a` |
|---:|---:|---:|---:|---:|
| 4 | .10652265 | .10652850 | .03451617 | .55985 |
| 6 | .03183708 | .03184741 | .00462573 | .57452 |
| 8 | .01065029 | .01066116 | .00065813 | .56777 |
| 10 | .00403103 | .00403770 | .00009701 | .55137 |

These are not the exact asymmetric lattice of Section 4.  They are a more
hostile reflected/jittered test, and their observed exponent drifts toward
`1/2`, not `1`.  Random phase searches at the same sizes found comparable
or weaker losses.  Repeating the same odd midpoint in every cell was much
easier: the optimum remained close to the nearest-pair value of Section 3.

For the five-point fixture with `alpha=.45`, fixed `delta_c=.7`, and
`L=(2m+1)pi/(d delta_c)`, the predicted limit is

```text
rho_c^2=.3769230769....                               (6.1)
```

The primal SDP amplitudes at `L=33.66,60.59,114.44,222.16` were respectively

```text
.51207, .45078, .41787, .39827,                       (6.2)
```

consistent with the proved `rho_c^2+O(1/L)` law.

The numerical message is therefore coherent but not dispositive:

```text
identically oriented cells       much cheaper than exponential;
maximally winding cells           approximately half-product;
one internally rich cell         can force a double local zero. (6.3)
```

## 7. What remains open

The strongest plausible next statement is a global real-codimension
interpolation theorem:

> For any target-local list obeying the relevant occupancy/count budget,
> the half-disk Pick optimum is bounded below by the exponential of one half
> of the appropriate full complex interpolation potential, up to
> subexponential loss, with local multiplicities allocated by the real Pick
> dual rather than by one representative per cell.

Section 4 shows the factor `1/2` is natural and attainable.  Section 5 shows
that a proof cannot simply retain one representative from every occupied
cell.  A valid proof must control the rank/multiplicity of positive dual
dependencies across the entire list and then survive the finite-support
Gram transfer.  Neither step is presently proved.

Code and tests:

- `src/pick_halfdisk_probe.py`,
- `src/test_pick_halfdisk_probe.py`.
