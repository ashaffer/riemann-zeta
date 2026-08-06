# An explicit trace-class companion for completed xi

## Status and verdict

This note gives an unconditional trace-class operator whose Fredholm
determinant is the centered completed xi-function.  It yields the exact
equivalence

    RH  <=>  every nonzero eigenvalue of the companion is positive real.

The construction is rigorous but is not a Hilbert--Polya realization.  It is
a universal companion construction for entire functions of order below one;
the operator is highly nonnormal, and its spectral-sign statement merely
repackages the original zero-location problem.  The route should continue
only if an arithmetic property of this particular companion can force its
spectrum to be positive without using the zeros.  The natural leading-section
version is already pruned by certified failures in dimensions two and six.

## 1. A general low-order entire companion

Let

    f(w)=1+sum_(n>=1) a_n w^n

be entire of order `rho<1`.  Fix

    1 < alpha < 1/rho.

On `l2(N_0)` with standard basis `e_n`, define

    S e_n = (n+1)^(-alpha) e_(n+1),                              (1.1)
    ell_n = (-1)^n a_(n+1) (n!)^alpha.                           (1.2)

Let `L` be the linear functional with `L(e_n)=ell_n`, and use the explicit
rank-one convention

    (e_0 tensor L)(x)=L(x)e_0.

Set

    K_f = S + e_0 tensor L.                                      (1.3)

### Theorem 1.1

The sequence `ell` belongs to `l2`, the operator `K_f` is trace class, and

    det(I+w K_f)=f(w)                                            (1.4)

for every complex `w`.

### Proof

Choose `beta` with

    rho < beta < 1/alpha.

The definition of entire order and Cauchy's estimate, optimized in the
circle radius, give eventually

    |a_n| <= (e beta/n)^(n/beta).                                (1.5)

Stirling's formula therefore gives

    log(|a_(n+1)|(n!)^alpha)
      <= -(1/beta-alpha)n log n + O(n).                          (1.6)

The coefficient in front of `n log n` is strictly negative, so `ell` is
rapidly decreasing and belongs to `l2`.  Hence `e_0 tensor L` is rank one.

The singular values of `S` are `(n+1)^(-alpha)`, so

    ||S||_1=sum_(n>=1)n^(-alpha)<infinity.                       (1.7)

Moreover,

    ||S^n||=(n!)^(-alpha),                                      (1.8)

which makes `S` quasinilpotent and makes

    (I+wS)^(-1)=sum_(n>=0)(-wS)^n                               (1.9)

converge in operator norm for every `w`.  Thus `det(I+wS)=1`.  The trace-class
rank-one determinant lemma now gives

    det(I+wK_f)
      = 1+w L((I+wS)^(-1)e_0)
      = 1+w sum_(n>=0)(-w)^n(n!)^(-alpha)ell_n
      = 1+sum_(n>=0)a_(n+1)w^(n+1)
      = f(w).                                                    (1.10)

This proves the theorem and fixes the otherwise easy-to-miss sign in (1.2).

## 2. Specialization to completed xi

Define

    X(w)=xi(1/2+sqrt(w))/xi(1/2).                                (2.1)

The functional equation makes `z -> xi(1/2+z)` even, so (2.1) is a
single-valued entire function of `w`.  It has real Taylor coefficients,
`X(0)=1`, and order `1/2`.  Hence Theorem 1.1 applies for every

    1 < alpha < 2.                                               (2.2)

Write the resulting operator as `K_xi,alpha`.  Its determinant is

    det(I+w K_xi,alpha)=X(w).                                    (2.3)

A nontrivial zero `rho` of zeta gives a zero

    w_rho=(rho-1/2)^2                                           (2.4)

of `X`.  The functional-equation pair `rho,1-rho` maps to the same value in
(2.4), with the original multiplicity rather than twice that multiplicity.
There is no exceptional zero at `rho=1/2`.

For a trace-class operator, `w_0` is a zero of `det(I+wK)` exactly when
`-1/w_0` is a nonzero eigenvalue of `K`, and the zero order is its algebraic
multiplicity.  Therefore

    RH
      <=> every zero of X is negative real
      <=> spectrum(K_xi,alpha) minus {0} is contained in (0,infinity).
                                                                    (2.5)

Repeated zeta zeros cause no logical problem in (2.5); they appear as
algebraic multiplicity and possible Jordan chains.

## 3. Leading finite sections fail immediately

Let `K_N` be the `N`-dimensional compression to
`span(e_0,...,e_(N-1))`.  The same nilpotent rank-one calculation gives

    det(I+wK_N)=p_N(w)=sum_(j=0)^N a_j w^j.                      (3.1)

This natural approximation does not inherit the desired positive spectrum.
In dimension two,

    K_2 = [[a_1,-a_2],[1,0]],
    characteristic(K_2)(lambda)=lambda^2-a_1 lambda+a_2.         (3.2)

A 768-bit FLINT/Arb calculation certifies

    a_1 = 0.0231049931154189707889338104303390140...,
    a_2 = 0.0002483340537891441757238564452088177...,
    a_1^2-4a_2
      = -0.0004594955082930186652828466279458948... < 0.        (3.3)

Thus the first nontrivial section already has a nonreal conjugate eigenvalue
pair.  In particular:

* no positive metric can make this section self-adjoint;
* positive diagonal symmetrization fails because the product of the two
  off-diagonal entries is `-a_2<0`;
* its Hermitian part is indefinite, with determinant
  `-(1-a_2)^2/4`;
* raw coefficient Hankel positivity also fails, since
  `a_2-a_1^2=-0.0002855066530744...<0`.

Even the weaker proposal that all leading sections be accretive fails.  For
the degree-six section, the third Hurwitz determinant is

    Delta_3
      = a_3 a_4 a_5-a_2 a_5^2-a_3^2 a_6+a_1 a_5 a_6
      = -1.9788076285166548894... * 10^(-27) < 0.              (3.4)

The certified Hurwitz signs are

    Delta_1, Delta_2 > 0,
    Delta_3, Delta_4, Delta_5, Delta_6 < 0.                     (3.5)

The Routh sign count therefore gives two roots of `p_6` in the open right
half-plane, hence two eigenvalues of `K_6` in the open left half-plane.

The reproducible certificate is
[`xi_companion_failfast.py`](../src/xi_companion_failfast.py).  Its strict
sign assertions use rigorous Arb balls with one thread.  This computation is
not Lean-checked and is a finite-section result only.  Taylor sections are
not Jensen polynomials; their spurious roots may escape to infinity, which
corresponds to the offending companion eigenvalues collapsing to zero.

## 4. Why this is a gate rather than a solution

The construction uses only the Taylor coefficients of xi and never inserts
its zeros.  That makes it a legitimate root-free operator realization.
However, the realization is universal: the same proof works for every
normalized entire function of order below one.  No positivity enters.

The matrix of `K_xi,alpha` has a weighted subdiagonal and a dense first row.
It is not self-adjoint, normal, or visibly similar to a positive operator.  A
diagonal similarity cannot make it self-adjoint because diagonal similarity
preserves its asymmetric zero pattern.  Thus (2.5) is not Hilbert--Polya in
disguise.

A noncircular continuation needs an independently checkable arithmetic
property forcing spectral positivity, for example:

1. an explicit positive metric with a proved bounded inverse and
   `G K=K^* G`;
2. a genuine oscillation or total-positivity theorem for the weighted
   Hessenberg matrix;
3. a canonical normal dilation whose compression retains the determinant;
4. a sign-regular resolvent kernel derived from the theta integral for the xi
   coefficients.

The first target is stronger than RH for this companion: a bounded positive
metric would make the operator similar to a self-adjoint one and hence
semisimple, while a multiple zero produces a Jordan chain.  It would therefore
also prove simplicity of the nontrivial zeros.  This makes it an honest but
more ambitious fail-fast checkpoint, not an equivalent reformulation.

Merely fitting such a metric after computing the spectrum, or restating
hyperbolicity of all finite characteristic polynomials, would be circular.
The fail-fast test for this branch is therefore to derive one of the four
structures directly from coefficient formulas; absent that, the companion is
best kept as a concise global reformulation.

The most obvious coefficient structure is already known to be the full
problem.  The sequence `(a_n)` is a Polya-frequency sequence of infinite
order exactly when its infinite Toeplitz matrix is totally nonnegative.  The
[Aissen--Edrei--Schoenberg--Whitney classification](https://doi.org/10.1073/pnas.37.5.303),
together with the fact that `X` is entire of order `1/2`, then forces

    X(w)=product_j (1+beta_j w),   beta_j>=0.                    (4.1)

Conversely, RH gives precisely such a product.  Hence full `PF_infinity`,
all-degree Jensen hyperbolicity, and RH are equivalent in this setting.
Finite coefficient positivity or low-order Turan inequalities are only
finite shadows.  Without a new arithmetic theorem implying the complete
structure, total positivity does not provide an easier continuation.
