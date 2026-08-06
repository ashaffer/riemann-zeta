# Actual-prime reflection and Euler-transfer checkpoint

Status: analytic and Arb-certified fail-fast checkpoint, 2026-08-06.  This
note does **not** prove RH.

The norm, singular-spectrum, and moving central-collar audit of the surviving
aggregate is continued in
[`MOVING-TYPE-II-NORM-CHECKPOINT.md`](MOVING-TYPE-II-NORM-CHECKPOINT.md).

## 1. Verdict

The R67 survivor has split into two exact reductions and several closed
generic engines.

1. There is an exact actual-prime ramp primitive whose boundedness is
   RH-equivalent.
2. Direct reflection positivity is false for the actual primes.  More
   strongly, the centered actual-prime reflection form is unbounded above and
   below for every fixed triangle width.
3. The prime-only Selberg Riccati equation is a zero-free holomorphic gauge of
   the original zeta equation.  Its inverse still contains `1/zeta^2`.
4. The exact Euler/Buchstab scale update has exponentially large expanding
   steps, even after any fixed triangle smoothing.  No uniformly
   `L^2`-equivalent translation-invariant metric makes it power-bounded.
5. Vaughan's identity puts the remaining difficulty into one explicit
   centered Type-II sum with both variables above `x^theta`.  This is an
   exact RH proxy, but its coefficient Dirichlet series retains every
   nontrivial-zero pole with unchanged residue.
6. Repeated logarithmic smoothing makes this proxy arbitrarily balanced:
   for every fixed `epsilon>0`, one can confine both Type-II variables to
   `[x^(1/2-epsilon),x^(1/2+epsilon)]` without changing the exact horizontal
   zero-width exponent.  Tracking the order dependence further gives an
   unconditional moving-order `x^(1/2+o(1))` arithmetic localization, though
   no moving-test RH converse.
7. Finite cofactor blocks are individually unbounded: only the full cofactor
   sum contributes the zeta factor that reduces their higher zero poles to
   the simple poles compatible with boundedness under RH.
8. The exact Euler bulk/boundary decomposition is equally inseparable.  Its
   three pieces separately have higher-order critical-zero poles; only their
   sum recovers the single-pole aggregate.

The remaining reduction is now sharply specific: prove cancellation between
the even and odd squarefree sectors **on the particular moving ramp
observable**, not on the ambient operator space.  Equivalently, control the
actual-prime primitive below by an event-specific Type-II estimate or by a
state-filtered arithmetic metric whose ramp dual norm remains uniform.

## 2. Exact actual-prime ramp primitive

Put

```text
Phi_ell(x)=min(1,max(0,x/ell)),
J_ell=4(1-exp(-ell/2))/ell,
```

and define

```text
C^p_ell(R)
 = sum_p (log p)p^(-1/2)Phi_ell(R-log p)
   -J_ell exp(R/2)+R/2.                                     (2.1)
```

The ramp identity and

```text
J_ell(exp(ell/2)-1)=M_ell^2
```

give the exact actual-prime coboundary

```text
Ptilde_ell(R)
 =C^p_ell(R+ell)-C^p_ell(R),                                (2.2)
```

where `Ptilde_ell=P_ell+ell/2` is the centered discrepancy from R66.

This primitive has the same horizontal-width exponent as the full von
Mangoldt primitive on every forward half-line.  Indeed, if `C_ell` denotes
the full von Mangoldt ramp from R66, then their difference is

```text
sum_(p,k>=2) (log p)p^(-k/2)Phi_ell(R-k log p)-R/2.          (2.3)
```

Writing

```text
A(x)=sum_(p<=x) (log p)/p,
B_1=lim_(x->infinity)[A(x)-log x]
   =-EulerGamma-sum_p (log p)/[p(p-1)],                     (2.4)
```

the square-prime part has the exact averaging form

```text
S_(2,ell)(R)=(1/ell)integral_(R-ell)^R A(exp(u/2))du.
```

Consequently the quantitative prime number theorem and partial summation
give

```text
S_(2,ell)(R)=R/2+B_1-ell/4+o(1),                            (2.5)
```

while the `k>=3` sum converges absolutely to a constant.  Hence (2.3)
converges to the explicit value

```text
kappa_ell
 =-EulerGamma-ell/4+sum_p (log p)/[sqrt(p)(p-1)].           (2.6)
```

In fact the classical zero-free-region error gives

```text
C_ell(R)-C^p_ell(R)
 =kappa_ell
  +O_ell((1+sqrt(R))exp(-c sqrt(R))+(1+R)exp(-R/6)).        (2.7)
```

This error is summable on every progression `R_0+j ell`.  R65--R66 now
imply

```text
limsup_(R->infinity) log(1+abs(C^p_ell(R)))/R=Delta,         (2.8)

RH
 <=> C^p_ell is bounded on a forward half-line
 <=> C^p_ell is subexponential there
 <=> sup_(r in [R_0,R_0+ell),N>=1)
       abs(sum_(j=0)^(N-1)Ptilde_ell(r+j ell))<infinity.    (2.9)
```

The forward-half-line qualification is necessary: the displayed definition
has `C^p_ell(R)~R/2` as `R` tends to minus infinity.

More quantitatively, set

```text
B_N=sup_(r in [R_0,R_0+ell))
    abs(sum_(j=0)^(N-1)Ptilde_ell(r+j ell)).                (2.10)
```

The intervals `[R_0+N ell,R_0+(N+1)ell)` partition the forward ray, while
`C^p_ell` is bounded on the base interval.  The exact continuous width law
therefore gives the discrete one

```text
limsup_(N->infinity) log(1+B_N)/(N ell)=Delta.              (2.11)
```

Thus RH is equivalently `B_N=O(1)`, or
`B_N=O_epsilon(exp(epsilon N ell))` for every positive `epsilon`.

Equation (2.1) is the cleanest surviving scalar target in this branch.

## 3. Actual-prime reflection positivity is false

On `[0,infinity)`, let

```text
E_p
 =sum_p (log p)p^(-1/2)delta_(log p)
  +(1/2-exp(t/2))dt                                         (3.1)
```

and

```text
H_(ell,R)(E_p)
 =integral integral w_ell(u+v-R)dE_p(u)dE_p(v).             (3.2)
```

Writing `a_p=(log p)/sqrt(p)` and `h(t)=1/2-exp(t/2)`, one has

```text
H_(ell,R)
 =sum_(p,q) a_p a_q w_ell(log(pq)-R)
  +2sum_p a_p K_ell(R-log p)+B_ell(R),                      (3.3)

K_ell(x)=integral_0^infinity w_ell(v-x)h(v)dv,
B_ell(R)=integral_0^infinity w_ell(t-R)
  [(t-2)exp(t/2)+t/4+2]dt.                                 (3.4)
```

For `x>=ell`,

```text
K_ell(x)=ell/2-M_ell^2 exp(x/2).                            (3.5)
```

Thus every value is a finite prime sum plus elementary
exponential-polynomial integrals.

### Certified counterexample

At `ell=1` and `R=10`, only primes below `exp(11)` occur.  Arb interval
arithmetic gives

```text
prime--prime              1129.937012250409901388599455014...
prime--background        -2359.484493007528281285455216559...
background--background    1229.323129608218211429465909886...

H_(1,10)(E_p)
 = -0.224351148900168467389851658447247...
```

with enclosure radius below `7e-34`.  Removing the positive diagonal
`p=q` terms makes the value still smaller.  The certificate is
`src/actual_prime_reflection_falsifier.py`.

### Two-sided unboundedness

The finite counterexample is a shadow of a stronger theorem.

#### Theorem 3.1

For every fixed `ell>0`,

```text
sup_R H_(ell,R)(E_p)=+infinity,
inf_R H_(ell,R)(E_p)=-infinity.                             (3.6)
```

#### Proof

Let

```text
A_p(s)
 =Prime(s+1/2)-1/(s-1/2)+1/(2s),
W_ell(s)=4sinh^2(ell s/2)/(ell s^2).                        (3.7)
```

For `Re(s)>1/2`, Fubini gives the bilateral Laplace identity

```text
integral_(-ell)^infinity exp(-sR)H_(ell,R)dR
 =W_ell(s)A_p(s)^2.                                        (3.8)
```

Möbius inversion of the Euler product continues `A_p` meromorphically to
`Re(s)>0`.  Its pole at `s=1/2` is canceled by the continuous prime main
term, and its square-prime pole at `s=0` is canceled by `1/(2s)`.  It is
therefore holomorphic on the nonnegative real axis.

If `rho=1/2+i gamma` is a critical-line zero of multiplicity `m`, then

```text
A_p(s)=-m/(s-i gamma)+O(1).                                 (3.9)
```

At every nonresonant ordinate,

```text
W_ell(i gamma)=4sin^2(ell gamma/2)/(ell gamma^2)>0,          (3.10)
```

so (3.8) has a genuine double pole at `i gamma`.

There is a nonresonant critical zero for every fixed `ell`: the resonance
lattice has only `O_ell(T)` points, whereas Heath-Brown's refinement of
Selberg gives `>>T log T` **distinct** critical-line zeros of odd
multiplicity.  See D. R. Heath-Brown,
[*Zeros of the Riemann Zeta-function on the critical
line*](https://ora.ox.ac.uk/objects/uuid%3Aec8e7c42-38f7-47e9-9485-2398f2819459).

Suppose first that `H_(ell,R)<=C` eventually.  The nonnegative tail
`C-H_(ell,R)` has a Laplace transform with no singularity on the positive
real axis.  Landau's theorem moves its abscissa of convergence to at most
zero.  Positivity then gives, as `sigma` decreases to zero,

```text
abs(G(sigma+i gamma))<=G(sigma)=O(1/sigma).                 (3.11)
```

But the double pole in (3.8) makes the left side
`asymp 1/sigma^2`, a contradiction.  Applying the same argument to the
nonnegative tail `H_(ell,R)+C` rules out an eventual lower bound.  This proves
(3.6).  QED.

Consequently raw reflection parity, bounded odd excess, diagonal deletion,
and any fixed finite completion unable to cancel the divisor-indexed double
poles are closed.

## 4. Prime-only Riccati transfer is a zeta gauge

Initially for `Re(z)>1`, define

```text
P_0(z)=sum_p p^(-z),
Prime(z)=sum_p (log p)p^(-z)=-P_0'(z),
B_p(z)=Prime(z)^2-Prime'(z).                                (4.1)
```

The coefficients of `B_p` are nonnegative: they are the prime-log-square
and ordered semiprime terms.  Put

```text
G_2(z)=sum_(k>=2) P_0(kz)/k.                                (4.2)
```

This is holomorphic for `Re(z)>1/2`, and the Euler product gives

```text
Z_p(z):=exp(P_0(z))=zeta(z)exp(-G_2(z)).                    (4.3)
```

The right side supplies the meromorphic continuation.  Its second factor is
holomorphic and nowhere zero, so `Z_p` has exactly the zeta divisor in this
half-plane.  Moreover,

```text
Prime=-Z_p'/Z_p,
B_p=Z_p''/Z_p.                                              (4.4)
```

The linearization `f=2Prime*h-h'` factors as

```text
f=-Z_p^(-2)(Z_p^2 h)',
h(z)=Z_p(z)^(-2) integral_z^infinity Z_p(u)^2 f(u)du.        (4.5)
```

Thus

```text
h(z)=zeta(z)^(-2)exp(2G_2(z))
 integral_z^infinity zeta(u)^2exp(-2G_2(u))f(u)du.          (4.6)
```

Prime-power stripping has only conjugated the inverse by a zero-free analytic
factor.  Unique factorization produces an elegant exact ODE
`Z_p''=B_p Z_p`, but no new critical-half-plane contraction.

## 5. Exact rough-number transfer and its obstruction

Let

```text
y_R=exp((R+ell)/2),
P(y)=product_(p<=y)p,
E_y=sum_(d|P(y)) mu(d)d^(-1/2)delta_(log d),
N_c=sum_(m>=1)m^(-1/2)delta_(log m).                        (5.1)
```

For `R>3ell`, the triangle support lies in `(y_R,y_R^2]`.  Every
`y_R`-rough integer there is prime, so inclusion--exclusion gives the exact
actual-prime identity

```text
sum_p (log p)p^(-1/2)w_ell(log p-R)
 =sum_(d|P(y_R)) mu(d) sum_m
   [log(dm)/sqrt(dm)]w_ell(log(dm)-R).                      (5.2)
```

Under `R -> R+ell`, the roughness cutoff changes by
`y -> qy`, where `q=exp(ell/2)`, and

```text
E_(qy)=B_(y,q)*E_y,
B_(y,q)=convolution_(y<p<=qy)
  [delta_0-p^(-1/2)delta_(log p)].                          (5.3)
```

Its Fourier multiplier is

```text
b_(y,q)(xi)=product_(y<p<=qy)(1-p^(-1/2-i xi)).             (5.4)
```

Kronecker independence gives

```text
norm(B_(y,q))_(2->2)=product_(y<p<=qy)(1+p^(-1/2)),
log norm(B_(y,q))
 ~2(sqrt(q)-1)sqrt(y)/log y.                                (5.5)
```

Fixed triangle smoothing does not repair this.  For fixed nonzero `xi`, the
prime number theorem and partial summation give

```text
log abs(b_(y,q)(xi))
 =-[sqrt(y)/log y] Re[
    exp(-i xi log y)
    (q^(1/2-i xi)-1)/(1/2-i xi)]
  +o(sqrt(y)/log y).                                       (5.6)
```

Choose `xi` with `W_ell(i xi)!=0` and `xi ell/(4 pi)` irrational.  Along the
actual geometric cutoffs, the phase in (5.6) is dense.  Infinitely many
one-step updates expand by

```text
exp(c_(ell,xi)sqrt(y)/log y),                               (5.7)
```

and infinitely many contract comparably.  Multiplication by the fixed
nonzero number `W_ell(i xi)` cannot change this conclusion.

The parity-sector mean squares expose the same obstruction:

```text
norm(E_y^+)_B2^2, norm(E_y^-)_B2^2
 = (1/2)[product_(p<=y)(1+1/p)
         +/- product_(p<=y)(1-1/p)]
 ~[3 exp(EulerGamma)/pi^2]log y.                            (5.8)
```

The two large parity sectors must cancel.  Their ambient `B^2` norms, used
separately with a triangle inequality, cannot produce the required
fixed-ramp estimate for Buchstab, Vaughan, or Heath--Brown pieces; the
infinite inverse is again

```text
sum_d mu(d)d^(-1/2-s)=1/zeta(1/2+s).                        (5.9)
```

Equations (5.5)--(5.7) close every generic translation-invariant contraction
or uniformly `L^2`-equivalent metric for the natural scale update.  They do
not rule out cancellation on the particular state `E_y*N_c`, nor a singular
or non-translation-invariant arithmetic metric.

### State-adapted diagonal metrics

The most natural state-dependent metrics can also be classified.  On the
prime shell torus put

```text
B_(y,q)(z)=product_(y<p<=qy)(1-p^(-1/2)z_p),
norm(f)_y^2=integral abs(f(z))^2 w_y(z)dm(z).               (5.10)
```

If the weights are positive and integrable on a common torus, and
multiplication by `B_(y,q)` is an exact isometry for every `f`, localization
forces the unique Doob update

```text
w_(qy)(z)=w_y(z)/abs(B_(y,q)(z))^2.                         (5.11)
```

The condition number of the one-step relative weight `w_(qy)/w_y` is

```text
kappa_(y,q)
 =[product_(y<p<=qy)(1+p^(-1/2))/(1-p^(-1/2))]^2,

log kappa_(y,q)
 ~8(sqrt(q)-1)sqrt(y)/log y.                               (5.12)
```

So the canonical exact-isometric weighted-Bohr update is exponentially
ill-conditioned.  Mere contractivity allows smaller target weights, but then
loses two-sided coercivity; the earlier expanding modes exclude uniform
`L^2` equivalence.  The same normalization obstruction appears
probabilistically.  Under the regularized Dirichlet law

```text
Prob_sigma(n)=n^(-1-2sigma)/zeta(1+2sigma),
```

the likelihood of having no prime factor at most `y`, normalized to mean
one, has squared `L^2` norm

```text
product_(p<=y)(1-p^(-1-2sigma))^(-1).                      (5.13)
```

It tends to `zeta(1+2sigma)` as `y` tends to infinity; at the formal critical
endpoint its finite-cutoff size is asymptotic to
`exp(EulerGamma)log y`.  Contractivity survives only after losing the
normalization needed to cancel the pole main term.

There is also an exact scalar cohomology classification.  Write

```text
Ecal_y(s)=product_(p<=y)(1-p^(-1/2-s)),
Scal_y(s)=Ecal_y(s)zeta(s+1/2).                             (5.14)
```

Every scalar Doob factor satisfying

```text
h_(qy)(s)[Ecal_(qy)(s)/Ecal_y(s)]=h_y(s)
```

has the form `h_y=C/Ecal_y`, and hence

```text
h_y(s)Scal_y(s)=C(s)zeta(s+1/2).                           (5.15)
```

Normalizing the moving state to one requires
`C=1/zeta(s+1/2)`.  Apart from the known pole normalization, absence of a pole
of this factor in `Re(s)>0` is exactly the zero-free half-plane equivalent to
RH.  Thus uniformly `L^2`-equivalent diagonal ambient metrics, the canonical
normalized divisibility martingale, exact-isometric weighted-Bohr updates,
and scalar normalizers do not realize the remaining arithmetic cancellation.
This does not classify every possible degenerate diagonal contraction.  A
proof based on one of these contractions must add control of the centered
ramp functional that the product calculation alone does not provide.

There is an important filtered exception.  If old functions are restricted
to the sigma-algebra generated by primes at most `y`, exact isometry requires
only

```text
E_shell(abs(B_(y,q))^2 w_(qy) | F_y)=w_y.                  (5.16)
```

It is not unique.  In particular,

```text
c_(y,q)=integral abs(B_(y,q))^2dm
       =product_(y<p<=qy)(1+1/p),
w_(qy)=w_y/c_(y,q)                                        (5.17)
```

is an exact isometry on the old-state subspace with shell condition number
one.  Iteration makes the scalar weight decay like `1/log y`, so uniform
coercivity is lost.  This does **not** by itself rule the construction out:
the remaining question is whether the centered ramp functional has uniformly
bounded dual norm in such a filtered metric.  Equations (5.11)--(5.15) close
the full-ambient and scalar-normalizer shortcuts, not every filtered or
non-scalar martingale.

The scalar filtered choice can, however, be closed at that dual-norm gate.
Put

```text
C_y=product_(p<=y)(1+1/p)
   ~[6exp(EulerGamma)/pi^2]log y,
norm(a)_y^2=C_y^(-1)sum_(d|P(y))abs(a_d)^2.                (5.18)
```

Then the Euler state with coefficients `a_d=mu(d)/sqrt(d)` has norm one.
Moreover every **scalar Haar weight** making all shell updates isometric is
`constant/C_y` along each geometric orbit.

For the exact triangle identity (5.2), define

```text
L_R(a)=sum_(d|P(y_R)) a_d G_R(d),
G_R(d)=sum_m [log(dm)/sqrt(m)]w_ell(log(dm)-R).             (5.19)
```

Its dual norm satisfies

```text
norm(L_R)_(y_R,*)^2
 =C_(y_R)sum_(d|P(y_R))abs(G_R(d))^2.                      (5.20)
```

Already the `d=2` tangent coefficient gives, with `x=exp(R)`,

```text
G_R(2)
 =sqrt(x/2)[M_ell^2 R+U_ell]+O_ell(x^(-3/2)R),

U_ell=integral_(-ell)^ell u exp(u/2)w_ell(u)du.            (5.21)
```

Since `log y_R=(R+ell)/2`, (5.20)--(5.21) imply

```text
norm(L_R)_(y_R,*) >>_ell exp(R/2)R^(3/2).                  (5.22)
```

Subtracting the pole main term `M_ell^2 exp(R/2)` as an affine constant does
not change a Lipschitz dual norm, and the `d=2` direction remains tangent to
the natural affine space `a_1=1`.  Encoding the pole linearly in the vacuum
coefficient therefore leaves (5.22) unchanged.

Even subtracting the whole coefficientwise continuum vector does not rescue
this scalar metric.  Define

```text
Pi_R(a)=sqrt(x)[M_ell^2 R+U_ell]
        sum_(d|P(y_R)) a_d/sqrt(d).                         (5.23)
```

Fix `max(1,exp(ell)/2)<r<exp(ell)`, close enough to `exp(ell)`, so that

```text
w_ell(log r)-M_ell^2/sqrt(r)!=0.
```

The prime number theorem supplies products `d=pq~r x` with `p,q<=y_R`.
Only `m=1` contributes near such a coefficient, and hence

```text
[G_R(d)-sqrt(x/d)(M_ell^2 R+U_ell)]/R
 ->w_ell(log r)-M_ell^2/sqrt(r).                           (5.24)
```

Thus `norm(L_R-Pi_R)_(y_R,*)>>_ell R sqrt(C_(y_R))`, which
still grows like `R^(3/2)`.  A more general pole representative
`N_y(E_y)=1` must have dual norm at least of this order to cancel the
obstruction.  Allowing an arbitrary unbounded representative makes the
minimization tautological: its optimal residual is the unknown centered
prime discrepancy itself.

Thus the canonical scalar filtered isometry cannot prove the centered prime
bound by a Hilbert-space dual estimate.  Nonconstant solutions of the
conditional equation (5.16) are not classified here, but they must solve
this explicit observable problem rather than mere state normalization.

## 6. Exact balanced Vaughan reduction

The particular-state survivor can be made into a genuine Type-II statement.
Put `x=exp(R)` and

```text
F_x(n)=n^(-1/2)Phi_ell(log(x/n)),
H_ell(s)=(1-exp(-ell s))/(ell s^2),
J_ell=H_ell(1/2),
K_ell=H_ell'(1/2)
     =4[((ell+4)exp(-ell/2))-4]/ell.                        (6.1)
```

For hard cutoffs `U,V`, write

```text
M_U(s)=sum_(d<=U) mu(d)d^(-s),
L_V(s)=sum_(b<=V) Lambda(b)b^(-s),
beta_V(r)=sum_(b|r,b>V) Lambda(b).                          (6.2)
```

The following form of Vaughan's identity is exact:

```text
Lambda
 =mu_(<=U)*log+Lambda_(<=V)-mu_(<=U)*Lambda_(<=V)*1
  +mu_(>U)*Lambda_(>V)*1.                                  (6.3)
```

It follows directly from `Lambda=mu*log`, `log=Lambda*1`, and
`mu*1=epsilon`.  The last term contributes the balanced bilinear form

```text
B_(U,V)(x)
 =sum_(d>U,r>V) mu(d)beta_V(r)F_x(dr).                      (6.4)
```

To evaluate the other three terms, elementary Euler summation gives,
uniformly for large `Y`,

```text
sum_m m^(-1/2)Phi_ell(log(Y/m))
 =J_ell sqrt(Y)+zeta(1/2)+O_ell(Y^(-3/2)),

sum_m (log m)m^(-1/2)Phi_ell(log(Y/m))
 =sqrt(Y)[J_ell log Y+K_ell]-zeta'(1/2)
  +O_ell(Y^(-3/2)log(2Y)).                                 (6.5)
```

The extra power is real: the ramp is one logarithmic average of a sharp
cutoff, and the leading periodic Bernoulli endpoint term has mean zero.  An
integration by parts across `[Y exp(-ell),Y]` cancels it, leaving the
periodic `B_2` correction of order `Y^(-3/2)`.

Define the explicit Type-I polar and zero-mode centerings

```text
I_pol(x;U,V)
 =sqrt(x){M_U(1)[J_ell log x+K_ell]
          +J_ell[M_U'(1)-M_U(1)L_V(1)]},

I_0(U,V)
 =-zeta'(1/2)M_U(1/2)+L_V(1/2)
  -zeta(1/2)M_U(1/2)L_V(1/2),                              (6.6)

Z_(U,V)(x)=J_ell sqrt(x)-I_pol(x;U,V)-I_0(U,V).             (6.7)
```

Substitution in (6.3), using only Chebyshev's bound for the error, proves

```text
C_ell(R)
 =B_(U,V)(x)-Z_(U,V)(x)
  +O_ell([U^2 log(2x)+(UV)^2]/x^(3/2)),                    (6.8)
```

provided `UV<=x exp(-ell)`.  Here `C_ell` is the full von Mangoldt ramp of
R66.  Choose

```text
U=V=floor(x^theta),   0<theta<=3/8.                         (6.9)
```

The error in (6.8) is bounded, and tends to zero when `theta<3/8`.  On the
support of (6.4), both `d` and `r` then lie between `x^theta` and
`x^(1-theta)`.  Since Section 2 proves that `C_ell-C^p_ell` tends to a
constant, (6.8) gives the exact Type-II width law

```text
limsup_(x->infinity)
 log(1+abs(B_(U,V)(x)-Z_(U,V)(x)))/log x=Delta.             (6.10)
```

In particular,

```text
RH <=> B_(U,V)(x)-Z_(U,V)(x)=O_ell(1).                     (6.11)
```

This is an aggregate estimate.  Bounding its dyadic blocks separately is a
strictly stronger request and is not part of the equivalence.

### Why both centerings are mandatory

The `I_0` term is not a disposable Euler--Maclaurin constant.  If
`I_0(U,U)=O(1)`, the prime number theorem gives
`L_U(1/2)~2sqrt(U)` and (6.6) forces

```text
M_U(1/2)=1/zeta(1/2)+O(U^(-1/2)).                           (6.12)
```

Abel summation would then continue
`sum mu(n)n^(-1/2-w)=1/zeta(1/2+w)` holomorphically throughout
`Re(w)>-1/2`, contradicting the known critical-line zeros.  Thus a proposed
estimate that subtracts only the pole-scale term is provably malformed: the
Type-II form must cancel the unbounded critical zero-mode as well.

### The balanced series retains the divisor

For fixed finite `U,V` and `Re(z)>1`, the coefficient Dirichlet series of
(6.4) factors exactly as

```text
sum_(d>U,r>V) mu(d)beta_V(r)/(dr)^z
 =(1/zeta(z)-M_U(z))zeta(z)[-zeta'(z)/zeta(z)-L_V(z)]
 =(1-zeta(z)M_U(z))[-zeta'(z)/zeta(z)-L_V(z)].              (6.13)
```

At a zeta zero `rho` of multiplicity `m`, its principal part is therefore

```text
-m/(z-rho),                                                 (6.14)
```

exactly the principal part of `-zeta'/zeta`.  Finite Type-I removal has
relocated every nontrivial-zero pole into the balanced term without changing
its residue.  The ramp factor `H_ell(rho-1/2)` cannot cancel an off-critical
zero because all nonzero zeros of `H_ell` lie on the imaginary axis.

Equation (6.11) is consequently a cleaner arithmetic attack surface, but not
a spectral simplification.  Progress must come from a direct moving-cutoff
bilinear cancellation theorem, not from ordinary Mellin continuation of
(6.13).

### Arbitrarily balanced fixed-order hierarchy

The `3/8` endpoint is not intrinsic.  Let `k>=1` be fixed, put `h=ell/k` so
that the total transition width stays `ell`, and define the logarithmic
averaging operator and its `k`-fold ramp by

```text
(A_h f)(t)=(1/h)integral_0^h f(t-u)du,
Phi_(h,k)(t)
 =(1/h^k)vol{u in [0,h]^k: u_1+...+u_k<t}.                 (6.15)
```

Thus `Phi_(h,k)=A_h^k 1_(t>=0)`.  Its Perron kernel is

```text
H_(h,k)(s)
 =(1/s)[(1-exp(-hs))/(hs)]^k
 =(1-exp(-hs))^k/[h^k s^(k+1)].                            (6.16)
```

Write the corresponding full von Mangoldt ramp as

```text
C_(h,k)(R)
 =sum_n Lambda(n)n^(-1/2)Phi_(h,k)(R-log n)
  -H_(h,k)(1/2)exp(R/2).                                  (6.16a)
```

The required fixed-order Euler estimate is the following lemma.  It is stated
uniformly in a complex neighborhood because the log-weighted version is
obtained by differentiation.

#### Lemma 6.1 (logarithmic B-spline Euler summation)

Fix `h>0`, an integer `k>=1`, and a compact set `K` contained in
`0<Re(a)<1`.  Uniformly for `a in K` and large `X`,

```text
sum_n n^(-a)Phi_(h,k)(log(X/n))
 =X^(1-a)H_(h,k)(1-a)+zeta(a)
  +O_(K,h,k)(X^(-Re(a)-k)).                                (6.17)
```

Moreover, on every smaller compact subset of the same strip, the derivative
of the remainder with respect to `a` is

```text
O_(K,h,k)(X^(-Re(a)-k)log X).                              (6.17a)
```

#### Proof

Put

```text
P_a(X)=sum_(n<=X)n^(-a),
(mathcal A_h F)(X)=(1/h)integral_0^h F(X exp(-u))du.
```

Finite-sum interchange gives the exact identity

```text
mathcal A_h^k P_a(X)
 =sum_n n^(-a)Phi_(h,k)(log(X/n)).                         (6.17b)
```

The convention at an integer endpoint is irrelevant to the integral.  Let
`Bbar_r(X)=B_r({X})` denote the periodic Bernoulli function, with the
right-continuous convention for `Bbar_1`.  Periodic Euler summation gives,
for any fixed integer `N>=1`,

```text
P_a(X)
 =zeta(a)+X^(1-a)/(1-a)
  -sum_(r=1)^N [(a)_(r-1)/r!]Bbar_r(X)X^(-a-r+1)
  +O_(K,N)(X^(-Re(a)-N)).                                 (6.17c)
```

Here `(a)_j` is the rising factorial.  One proof first applies periodic
Euler summation to the tail for `Re(a)>1`.  The final integral contains the
bounded function `Bbar_(N+1)(t)` times a constant multiple of
`t^(-a-N-1)`.  Explicitly, the remainder after the displayed `N` terms is

```text
R_N(a,X)
 =-[(a)_N/(N+1)!]Bbar_(N+1)(X)X^(-a-N)
  +[(a)_(N+1)/(N+1)!]
     integral_X^infinity Bbar_(N+1)(t)t^(-a-N-1)dt.       (6.17c')
```

This expression converges and is analytic for `Re(a)>-N`; its uniform bound
on `K` proves (6.17c) there without relying on a big-O analytic-continuation
argument.

It remains to record the cancellation supplied by logarithmic averaging.
If `q` is periodic of mean zero and has a bounded periodic `j`-fold
primitive, then, uniformly for `b` in a compact set,

```text
mathcal A_h^j[X^(-b)q(X)]
 =O_(h,j,b)(X^(-Re(b)-j)).                                 (6.17d)
```

Indeed, write `mathcal A_h^j` using the normalized order-`j` B-spline
density `kappa_(h,j)` on `[0,jh]` and change variables `t=exp(-u)`.  The
left side of (6.17d) becomes

```text
X^(-b) integral_(exp(-jh))^1 W_(b,h,j)(t)q(Xt)dt,
W_(b,h,j)(t)=kappa_(h,j)(-log t)t^(-b-1).                  (6.17e)
```

Extend `W` by zero.  Its `j`th distributional derivative is a finite
measure: `kappa_(h,j)` is the `j`-fold convolution of
`h^(-1)1_[0,h]`, whose `j`th derivative is
`h^(-j)(delta_0-delta_h)^(convolution j)`.  Composition with `-log t` and
multiplication by the smooth factor `t^(-b-1)` preserve a finite-measure
`j`th derivative on `[exp(-jh),1]`.  If `Q_j` is a bounded periodic
primitive with `Q_j^(j)=q`, distributional integration by parts `j` times
in (6.17e) gives the extra factor `X^(-j)` and proves (6.17d).  For
`q=Bbar_r`, one may take

```text
Q_j=[r!/(r+j)!]Bbar_(r+j).
```

For fixed compact `b`-sets, the preceding product and chain rules give the
explicit finite bound

```text
norm(D_t^j W_(b,h,j))_TV
 <=C_(b,j) exp(C_b jh)(1+h^(-1))^j.                       (6.17e')
```

Apply `mathcal A_h^k` to (6.17c) with `N=k`.  The averaged remainder keeps
the order `X^(-Re(a)-k)`, while (6.17d) makes the `r`th periodic term
`O(X^(-Re(a)-k-r+1))`.  Finally,

```text
mathcal A_h^k[X^(1-a)/(1-a)]
 =X^(1-a)H_(h,k)(1-a).
```

This proves (6.17).  The remainder is analytic in `a`.  Given nested compacts
`K_0` contained in the interior of `K`, Cauchy's estimate on a circle of
radius comparable to `1/log X`, still inside `K`, proves (6.17a) uniformly
on `K_0`.  Since every compact in the strip admits such an enlargement, this
is the stated local-uniform derivative estimate.  In particular,

```text
sum_n (log n)n^(-a)Phi_(h,k)(log(X/n))
 =X^(1-a)[log X H_(h,k)(1-a)+H_(h,k)'(1-a)]-zeta'(a)
  +O_(K,h,k)(X^(-Re(a)-k)log X).                           (6.17f)
```

QED.

At `a=1/2`, Lemma 6.1 lets the Vaughan calculation above repeat with

```text
J_(h,k)=H_(h,k)(1/2),
K_(h,k)=H_(h,k)'(1/2),                                    (6.18)
```

the same critical zero-mode `I_0`, and Type-I error

```text
O_(h,k)([U^(k+1)log(2x)+(UV)^(k+1)]/x^(k+1/2)).            (6.19)
```

For `U=V=floor(x^theta)`, this is bounded at

```text
theta_k=(k+1/2)/[2(k+1)]
       =1/2-1/[4(k+1)],                                    (6.20)
```

and tends to zero below that endpoint.  Both bilinear variables then lie in

```text
[x^(1/2-1/[4(k+1)]), x^(1/2+1/[4(k+1)])]
```

up to the harmless integer endpoints.  Hence, for every fixed positive
`epsilon`, choosing `k` large enough gives an RH-equivalent aggregate
Type-II estimate with both variables in
`[x^(1/2-epsilon),x^(1/2+epsilon)]`.

This sharpening does not erase the obstruction.  The only nonzero zeros of
`H_(h,k)` lie on the imaginary axis, so its fixed-width growth exponent is
still exactly `Delta`; the coefficient series is still (6.13), and `I_0` is
unchanged because `H_(h,k)` has residue one at zero.  The argument is uniform
only for each **fixed** `k`.  It does not by itself justify `k=k(x)` or the
exact endpoint `theta=1/2`; in particular, Lemma 6.1 as stated makes no
uniform-in-`k` claim about its implied constant.  The next proposition
supplies the constant bound, while its corollary keeps the missing
moving-test converse explicit.

#### Proposition 6.2 (uniform smoothing-order constant)

The constant can in fact be traced.  Fix `ell>0` and a compact set `K`
inside `0<Re(a)<1`.  Put `h=ell/k`.  There is a constant `C_(ell,K)` such
that the remainder `mathcal R_k(a,X)` in (6.17) satisfies

```text
abs(mathcal R_k(a,X))
 <=exp(C_(ell,K) k log(k+2))X^(-Re(a)-k).                 (6.20a)
```

On an inner compact set, its `a` derivative satisfies the same bound with
the additional factor `1+log X`.

To see this, use the classical Fourier bound

```text
norm(Bbar_n)_infinity<=4n!/(2pi)^n,       n>=2.            (6.20b)
```

For the normalized B-spline
`kappa_(h,k)=(h^(-1)1_[0,h])^(convolution k)`, convolution
differentiation gives, for `0<=q<=k`,

```text
norm(D_u^q kappa_(h,k))_TV<=(2/h)^q=(2k/ell)^q.           (6.20c)
```

For the `r`th periodic Euler term, set `b=a+r-1` and use the weight `W` in
(6.17e).  Under `t=exp(-u)`,

```text
D_t^k=(-1)^k exp(ku)D_u(D_u+1)...(D_u+k-1).
```

Together with (6.20c), the product rule on `0<=u<=ell` gives

```text
norm(D_t^k W_(b,h,k))_TV
 <=exp(C_(ell,K)k log(k+2)),       1<=r<=k.                (6.20d)
```

The bounded `k`-fold primitive of `Bbar_r` is

```text
[r!/(r+k)!]Bbar_(r+k),
```

whose norm is at most `4r!/(2pi)^(r+k)` by (6.20b).  After multiplication
by the Euler coefficient `(a)_(r-1)/r!`, (6.20d) bounds each averaged
periodic term by the right side of (6.20a), with an additional
`X^(-r+1)` when `r>1`.  Summing `r<=k` preserves the same exponential
class.  Formula (6.17c') and (6.20b) give the same bound for the sharp
remainder; averaging over a total logarithmic shift `kh=ell` costs only
`exp(O_ell(k))`.  Cauchy's estimate proves the derivative statement.  QED.

#### Corollary 6.3 (moving-order arithmetic localization)

Let `k=k(x)` be integer-valued with

```text
k->infinity,        k log(k+2)=o(log x),
```

fix `c>1/4`, and put

```text
h=ell/k,
U=V=floor(x^(1/2-c/k)).                                   (6.20e)
```

Then the support condition holds for all sufficiently large `x`, and the
Vaughan identity has the unconditional form

```text
C_(h,k)(log x)
 =B_(U,V)^(k)(x)-Z_(U,V)^(k)(x)
  +O_ell(x^(-(2c-1/2)+o(1))).                             (6.20f)
```

Every contributing bilinear variable lies in

```text
[x^(1/2-c/k+o(1)),x^(1/2+c/k+o(1))],
```

and, after writing `r=bm`, every cofactor satisfies

```text
m<=x^(2c/k+o(1))=x^o(1).                                  (6.20g)
```

This proves an `x^(1/2+o(1))` **arithmetic localization**, not an
RH-equivalent moving-test criterion.  Because the kernel now changes with
`x`, the fixed-transform Laplace-pole proof of the converse no longer
applies.  A bounded or subpower residual in (6.20f) must not be claimed to
imply RH without a separate varying-test oscillation theorem.

### Cofactor blocks are individually worse

There is a precise reason not to split the aggregate (6.4) by the cofactor in
`r=bk`.  For a fixed nonempty finite set `mathcal K` put

```text
Q_mathcalK(z)=sum_(k in mathcal K) k^(-z).                  (6.21)
```

At fixed `U,V`, the coefficient series of the corresponding cofactor block
is

```text
D_mathcalK(z)
 =Q_mathcalK(z)[1/zeta(z)-M_U(z)]
                  [-zeta'(z)/zeta(z)-L_V(z)].              (6.22)
```

If `rho` is a zeta zero of multiplicity `m` and `Q_mathcalK(rho)!=0`, then
`D_mathcalK` has a pole of order `m+1`.  In contrast, summing over **all**
cofactors inserts

```text
sum_(k>=1)k^(-z)=zeta(z),                                  (6.23)
```

which cancels exactly `m` orders and leaves the permissible simple pole in
(6.13).

This distinction is unconditional, not heuristic.  A nonzero finite
Dirichlet polynomial `Q_mathcalK` has only `O_mathcalK(T)` zeros in a fixed
vertical strip, and the triangle resonance lattice has `O_ell(T)` points.
The distinct critical-line odd zeros used in Theorem 3.1 number
`>>T log T`, so some critical zero is neither a zero of `Q_mathcalK` nor a
ramp resonance.  Subtract the block's ordinary polar and constant centerings,
or any centering whose transform is regular or at most simple at that
critical ordinate.  If the resulting block were bounded, its Laplace
transform would be `O(1/sigma)` at `sigma+i gamma`; (6.22) instead gives
order `sigma^(-m-1)`.  Hence every fixed nonempty finite cofactor block
remains unbounded after those centerings, whereas the **centered**
all-cofactor aggregate `B_(U,V)-Z_(U,V)` is bounded under RH.

Thus termwise cofactor estimates are not merely stronger than (6.11): at the
fixed-truncation level they are false.  The factor `zeta(z)` generated by the
entire cofactor sum is the exact global cancellation that a viable Type-II
argument must retain.  This theorem does not by itself refute moving dyadic
blocks whose cutoffs change with `x`; it says such a proof cannot freeze and
bound those pieces independently.

### The Euler boundary layer is also inseparable

There is a second exact way to expose the same globality.  For the
`k`-fold smoothing in (6.15), define

```text
a_(U,V)(n)=sum_(db=n, d>U, b>V) mu(d)Lambda(b),
S_k(Y)=sum_m m^(-1/2)Phi_(h,k)(log(Y/m)),
E_k(Y)=S_k(Y)-J_(h,k)sqrt(Y)-zeta(1/2),                    (6.24)
```

and put `A_alpha(x)=sum_(n<x)a_(U,V)(n)n^(-alpha)`.  Expanding
`r=bm` in (6.4) gives the exact bulk/boundary split

```text
B_(U,V)(x)
 =J_(h,k)sqrt(x)A_1(x)+zeta(1/2)A_(1/2)(x)+R_k(x),

R_k(x)=sum_(n<x) a_(U,V)(n)n^(-1/2)E_k(x/n).              (6.25)
```

Equation (6.17) gives `E_k(Y)=O_(h,k)(Y^(-k-1/2))` for
`Y>=1`.  Chebyshev summation therefore yields

```text
R_k(x)<<_(h,k) sqrt(x)[1+log(x/(UV))].                    (6.26)
```

More importantly, the part with `n<=x exp(-T)` is smaller by
`exp(-(k+1)T)`, up to the same logarithmic factor.  Thus `R_k` is a genuine
growing hyperbola-boundary correlation.  Localization alone, however, does
not make it an easier independent target.

Indeed, for fixed `U,V` the coefficient series before the cofactor sum is

```text
A_(U,V)(z)
 =[1/zeta(z)-M_U(z)][-zeta'(z)/zeta(z)-L_V(z)].            (6.27)
```

In the logarithmic Laplace variable `s`, the multipliers of the three terms
in (6.25) are respectively

```text
J_(h,k)/(s-1/2),   zeta(1/2)/s,
Ehat_k(s)=zeta(s+1/2)H_(h,k)(s)
          -J_(h,k)/(s-1/2)-zeta(1/2)/s.                  (6.28)
```

Let `rho=1/2+i gamma` be a nontrivial zero of multiplicity `m`.  The series
`A_(U,V)` has a pole of order `m+1` at `rho`.  All three multipliers in
(6.28) are nonzero at `s=i gamma`.  For the last one this follows without a
zero-spacing assumption: after multiplication by `s(s-1/2)`, its value has
real part `zeta(1/2)/2`, which is nonzero.  Consequently each Euler piece,
after ordinary pole and constant centerings, still has an order-`m+1`
critical-zero pole and cannot be bounded.  Their sum has multiplier
`zeta(s+1/2)H_(h,k)(s)`; this is precisely the cofactor factor that cancels
`m` pole orders and restores the simple pole of the RH-equivalent aggregate.

Thus neither fixed cofactor blocks nor the exact Euler bulk and boundary
pieces can be bounded separately.  A surviving proof must capture their
joint cancellation with moving cutoffs.  This fixed-cutoff obstruction does
not preclude such a joint estimate.

## 7. Remaining reduction

The next theorem must be tailored to (5.2), rather than to its ambient
operator.  One equivalent target is still

```text
sup_(R>=R_0) abs(C^p_ell(R))<infinity.                      (7.1)
```

The new information is what a proof of (7.1) cannot use:

* not raw reflection positivity, since (3.6) is two-sided unbounded;
* not coefficient positivity of `B_p`, since (4.3) preserves the zeta
  divisor;
* not a fixed Fourier/ramp norm for the Euler update, since (5.7) expands;
* not separate estimates on the two squarefree parity sectors, since both
  have logarithmically divergent mass.

Within the reflection, Euler-transfer, and ambient-metric constructions
tested here, the smallest surviving mechanism is the centered, moving-cutoff
estimate (6.11), or any fixed-order arbitrarily balanced version
(6.15)--(6.20), proved by a cancellation method that sees the aggregate
Type-II form rather than bounding its blocks or Euler boundary pieces
separately.  In
rough-number coordinates it is the event-specific, ramp-smoothed cancellation
between the two parity sectors on `E_y*N_c`, coupled to the pole and `I_0`
centerings.

The metric alternative has narrowed as well.  A uniformly coercive ambient
metric is closed, and the scalar filtered isometry (5.17) fails the centered
ramp dual-norm test by (5.22).  Nonconstant solutions of the conditional
isometry (5.16), or non-diagonal arithmetic metrics, remain possible only if
they control that observable directly.  Any proposal should be tested
against the expanding modes in (5.6), the scalar cohomology obstruction
(5.15), and the lower bound (5.22).

These are the smallest survivors of this transfer branch, not a claim that
all other possible routes to RH have been logically excluded.

## 8. Evidence and nonclaim

Sections 2, 4, 5, and 6 are analytic identities using Euler summation, the
prime number theorem, Euler product, Vaughan and Möbius inversion, Kronecker
approximation, and elementary partial summation.  Theorem 3.1 additionally
uses Landau's theorem and the distinct critical-line zero result linked
there.  These arguments are not formalized in Lean.

The finite sign certificate uses Python FLINT/Arb and a one-byte prime sieve;
it enumerates 6,048 primes and 28,613 ordered prime pairs, with no broad
numerical build.  It is a machine-checked interval calculation, not a Lean
kernel proof.  The focused reproduction command is

```text
PYTHONPATH=src python3 -m unittest -v \
  src/test_actual_prime_reflection_falsifier.py
python3 src/actual_prime_reflection_falsifier.py
```

The 2026-08-06 audit used Python 3.12.3, `python-flint 0.9.0`, FLINT 3.6.0,
and 40 decimal digits.  A release must additionally bind these commands to a
committed source hash.  None of the results bounds (2.1), proves (7.1), or
proves RH.
