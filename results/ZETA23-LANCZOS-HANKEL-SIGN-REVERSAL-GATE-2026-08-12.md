# The Lanczos carrier gate is a shifted-Hankel sign-reversal problem

Status: exact moment/localizer theorem, exact completion-preserving
prime--pole--gamma correlation expansion, and a nondegenerate sharp-Loewner
countermodel, 2026-08-12.  The signed cubic correlation isolated below is
not proved for the actual von Mangoldt data.  No zero-free strip or improved
bound for a zeta zero is proved.

## 1. Verdict

The first arithmetic Lanczos plane has a complete moment-theoretic
description, but ordinary Hamburger moment positivity points in the wrong
direction in the only case where transverse rescue is needed.

Let `K=K*` be the actual completed arithmetic compression, let `a` be its
unit carrier direction, and put

```text
m_j=<a,K^j a>,                 j=0,1,2,3,
m_0=1,
sigma^2=m_2-m_1^2.                                      (1.1)
```

When `sigma>0`, the first Lanczos compression is

```text
J_2=[[m_1,sigma],[sigma,d]],
d=(m_3-2*m_1*m_2+m_1^3)/sigma^2.                      (1.2)
```

The two Hankel matrices

```text
H_0=[[1,m_1],[m_1,m_2]],
H_1=[[m_1,m_2],[m_2,m_3]]                              (1.3)
```

play opposite roles.  `H_0` is a Gram matrix and is positive for **every**
Hermitian `K`, including a negative-definite one.  By contrast, `H_1` is the
matrix of the signed form `K` on `span{a,Ka}`.  Precisely,

```text
det H_0=sigma^2,
det J_2=(m_1*m_3-m_2^2)/sigma^2.                     (1.4)
```

Suppose that the full-carrier scalar is negative, `m_1<0`.  This is the only
case in which a sub-full plane can improve the sign.  Then:

```text
the Lanczos plane contains a nonnegative vector
    iff m_1*m_3-m_2^2<=0.                             (1.5)
```

Thus the desired event is not shifted-Hankel positivity.  It is the
**sign reversal** of the first shifted Hankel determinant.  Moreover (1.5)
is not enough at a prescribed carrier fraction.  If

```text
Delta_H=m_2^2-m_1*m_3>=0,
s_0=(-m_1)/(sigma+sqrt(Delta_H)/sigma),
theta_*=1/(1+s_0^2),                                 (1.6)
```

then the exact carrier-fraction criterion is

```text
max {<z,Kz>: ||z||=1, z in span{a,Ka},
                  |<a,z>|^2>=theta} >=0
    iff theta<=theta_*.                              (1.7)
```

At equality the witnessing state has zero completed energy.  Formula (1.7)
is stronger than checking only the boundary value: when the transverse
diagonal is negative, the boundary can have passed through the positive
interval even though an interior carrier-rich state remains nonnegative.

The actual arithmetic target can equivalently be written with the third
central spectral moment

```text
tau_3=m_3-3*m_1*m_2+2*m_1^3:

F_theta
 =m_1+(1-theta)*tau_3/sigma^2
      +2*sqrt(theta*(1-theta))*sigma.                (1.8)
```

Here `F_theta` is the phase-optimized boundary energy.  Consequently the
only genuinely new input available from `m_1,m_2,m_3` is a **one-sided
signed cubic completed correlation**.  The nonnegative quantity
`sigma^2` is useful coupling data, but its sum-of-squares proof supplies no
sign for `tau_3` or for (1.5).

There is one useful uniform consequence.  The single odd-moment sign

```text
m_1<0  and  m_3>=0                                  (1.8a)
```

already guarantees `theta_*>=8/9`, and the constant `8/9` is sharp among
all Hermitian moment triples.  Thus a proof of nonnegativity of the actual
completed cubic moment on the negative-full-carrier branch would give a
nonnegative first-Lanczos witness retaining **eight ninths of the carrier**.
This is a much smaller statement than positivity of the whole shifted
Hankel matrix, but it is still an unproved signed cubic arithmetic theorem.

This disposes of the proposed automatic Hankel escape:

```text
ordinary moment/Hankel positivity:        automatic and insufficient;
shifted localizer positivity:             opposite to transverse rescue;
shifted determinant sign reversal:        exact new criterion;
actual completed cubic sign theorem:      open.                       (1.9)
```

## 2. Exact Lanczos--Hankel theorem

### Theorem 2.1 (localizer congruence and carrier threshold)

Let `K` be a Hermitian operator on a finite-dimensional complex Hilbert
space and let `a` be a unit vector.  Define (1.1), and assume `sigma>0`.
Set

```text
e_0=a,
e_1=(K-m_1)*a/sigma.                                 (2.1)
```

Then `e_0,e_1` are orthonormal, the matrix of `K` on their span is (1.2),
and for

```text
C: C^2 -> H,       C(u,v)=u*a+v*K*a,                (2.2)
```

one has exactly

```text
C* C=H_0,              C* K C=H_1.                 (2.3)
```

If `m_1<0`, define `theta_*` by (1.6) when `Delta_H>=0`.  If
`Delta_H<0`, set `theta_*=0`.  Then (1.7) holds for every `0<theta<=1`.

If `sigma=0`, `a` is an eigenvector and the first Lanczos space is the
carrier line; its constrained value is simply `m_1`.

#### Proof

Equation (2.1) and

```text
||(K-m_1)a||^2=m_2-m_1^2=sigma^2                  (2.4)
```

give orthonormality.  Direct expansion gives (1.2).  Equation (2.3) follows
by evaluating its four entries.  Taking determinants and using
`det H_0=sigma^2` proves (1.4).

Every phase-optimized unit vector in the Lanczos plane can be parametrized
by a slope `s>=0`:

```text
z_s=(e_0+s*e_1)/sqrt(1+s^2),
|<a,z_s>|^2=1/(1+s^2),
<z_s,Kz_s>=(m_1+2*sigma*s+d*s^2)/(1+s^2).           (2.5)
```

Because `m_1<0`, the numerator starts negative.  It reaches zero for some
`s>=0` exactly when

```text
sigma^2-m_1*d>=0
 iff m_2^2-m_1*m_3>=0.                              (2.6)
```

The smallest nonnegative root is

```text
s_0=-m_1/(sigma+sqrt(sigma^2-m_1*d))
   =-m_1/(sigma+sqrt(Delta_H)/sigma).                (2.7)
```

This formula also covers `d=0` and the double-root case.  A nonnegative
state with carrier at least `theta` exists exactly when

```text
s_0<=sqrt((1-theta)/theta),                          (2.8)
```

which is (1.6)--(1.7).  Finally, expanding `d=m_1+tau_3/sigma^2` in the
boundary value gives (1.8).  QED

### Corollary 2.2 (spectral mixing identity)

Let `mu_a` be the positive spectral probability measure of `K` at `a`, so
that `m_j=integral lambda^j dmu_a(lambda)`.  Then

```text
sigma^2
 =1/2 integral integral (lambda-xi)^2
                  dmu_a(lambda)dmu_a(xi),

m_1*m_3-m_2^2
 =1/2 integral integral lambda*xi*(lambda-xi)^2
                  dmu_a(lambda)dmu_a(xi).           (2.9)
```

Hence ordinary moment positivity sees dispersion but not its spectral sign.
Pairs on the same side of zero contribute positively to the shifted
determinant; opposite-sign pairs contribute negatively.  In the decisive
case `m_1<0`, Lanczos rescue requires the opposite-sign spectral mixing to
dominate the same-sign dispersion, quantitatively enough to satisfy (1.6).

#### Proof

Expand the two symmetric integrands and use `m_0=1`.  QED

### Corollary 2.3 (all ordinary Hankel squares are tautological)

For every `r>=0`, the ordinary Krylov Hankel matrix

```text
H_0^(r)=[m_(i+j)]_(0<=i,j<=r)                       (2.10)
```

is positive semidefinite, because it is the Gram matrix of
`a,Ka,...,K^r a`.  The shifted matrix

```text
H_1^(r)=[m_(i+j+1)]_(0<=i,j<=r)                     (2.11)
```

is the matrix of `K` on the same Krylov space.  Therefore proving (2.11)
positive is exactly proving positivity of the original completed form on
that space; it is not an independent moment theorem.  At `r=1`, the useful
negative-full-carrier alternative is instead that (2.11) be indefinite.

### Corollary 2.4 (sharp eight-ninths rescue from one odd-moment sign)

Assume `m_1<0`, `sigma>0`, and `m_3>=0`.  Then the threshold in (1.6)
satisfies

```text
theta_*>=8/9.                                      (2.12)
```

Moreover `d>0`, so the fixed boundary state

```text
z=sqrt(8/9)*e_0+(1/3)*e_1                         (2.12a)
```

itself has nonnegative completed energy; no interior maximization is needed.
The constant is best possible over Hermitian operators and unit carrier
vectors with these three hypotheses.

#### Proof

Put

```text
u=(-m_1)/sqrt(m_2),          0<u<1.                 (2.13)
```

Since `m_1<0<=m_3`,

```text
Delta_H=m_2^2-m_1*m_3>=m_2^2.                      (2.14)
```

Also

```text
sigma^2*d=m_3+(-m_1)*(2*m_2-m_1^2)>0.              (2.14a)
```

Using `sigma^2=m_2*(1-u^2)` in (1.6) gives

```text
s_0
 <=u*sqrt(1-u^2)/(2-u^2).                          (2.15)
```

The square of the right side has maximum `1/8`, attained at `u^2=2/3`.
Hence `theta_*=1/(1+s_0^2)>=8/9`.  Since (2.14a) makes the numerator in
(2.5) increasing after its unique positive root, its value at the
eight-ninths boundary slope `1/sqrt(8)` is nonnegative.

For sharpness take the two-dimensional Jacobi matrix whose moments at its
first coordinate satisfy

```text
m_1=-sqrt(2/3),       m_2=1,       m_3=0.           (2.16)
```

Equivalently,

```text
J=[[-sqrt(2/3), 1/sqrt(3)],
   [ 1/sqrt(3), 4*sqrt(2/3)]].                      (2.17)
```

It has `sigma=1/sqrt(3)`, `s_0=1/sqrt(8)`, and
`theta_*=8/9`.  QED

## 3. Completion-preserving expansion for the actual coefficients

The nonlinear moments do retain an exact prime--pole--gamma expansion.  It
is important to write it before applying inequalities.

Let `B` be the isometric inclusion of the endpoint-jet and selected-row
quotient into the sign-conjugated critical grid.  With the repository's
normalization, put

```text
C=L^(-2)*B^*(H_arch+H_pole)*B,                       (3.1)

V_n=[2*Lambda(n)/(L^2*sqrt(n))]
       *B^* S_(log n) B,       n=p^k<=X,             (3.2)
```

where `B^*` is the adjoint and the exact one-shift matrix is

```text
S_y(k,k)=(L-y)*cos(tau_k*y),
S_y(k,l)=[sin(tau_l*y)-sin(tau_k*y)]/(tau_k-tau_l)
                                                    (k!=l).             (3.3)
```

Then the actual completed operator, with no changed von Mangoldt
coefficient, is

```text
K=C-P,                  P=sum_(n=p^k<=X) V_n.        (3.4)
```

Thus

```text
m_1=<a,Ca>-<a,Pa>,                                  (3.5)

m_2=||Ca-Pa||^2
   =<a,C^2a>-2*Re<Ca,Pa>+<a,P^2a>,                  (3.6)

m_3=<a,C^3a>
   -2*Re<C^2a,Pa>-<Ca,P*Ca>
   +2*Re<Ca,P^2a>+<Pa,C*Pa>
   -<a,P^3a>.                                       (3.7)
```

Expanding `P` in (3.6)--(3.7) gives, respectively, the exact quadratic and
cubic actual-prime correlations

```text
sum_(n,m) <a,V_n V_m a>,
sum_(n,m,l) <a,V_n V_m V_l a>,                      (3.8)
```

together with every mixed archimedean/pole word and the signs displayed in
(3.7).  Equation (3.6) is a sum of squares only **after all places and all
mixed words have been recombined**.  No analogous recombination gives a sign
to `m_3`, `tau_3`, or `m_2^2-m_1*m_3`.

There is an equivalent exact sharp-square formulation.  If

```text
Phi_x(t)=2*S(t)*sum_k x_k/(t-tau_k),
K=L^(-2)*B^*H_(nu_X)B,                              (3.9)
```

then for `i,j>=0`

```text
m_(i+j+1)
 =L^(-2)*integral nu_X(t)
      conj(Phi_(B K^i a)(t))*Phi_(B K^j a)(t)dt.    (3.10)
```

Here

```text
nu_X=mu+1/[2*pi*(1/4+t^2)]-(1/pi)*Re E_X            (3.11)
```

contains the gamma term, rational pole, continuum center, and every actual
prime power.  Formula (3.10) makes the obstruction exact: `H_0^(r)` is a
Gram matrix for the constant positive multiplier, while `H_1^(r)` is the
same family paired with the signed completed multiplier `nu_X`.  Iteration
does not manufacture a new positive measure.

## 4. A nondegenerate sharp-Loewner countermodel

The failure is not an artifact of the degenerate scalar matrix `-M*I`.
Take

```text
K_bad=diag(-1,-2),          a=(1,1)/sqrt(2).         (4.1)
```

Then

```text
m_1=-3/2,     m_2=5/2,     m_3=-9/2,
sigma=1/2,
H_0=[[1,-3/2],[-3/2,5/2]]>0,
H_1=[[-3/2,5/2],[5/2,-9/2]]<0,                     (4.2)

m_1*m_3-m_2^2=1/2>0.                               (4.3)
```

The Lanczos space is the whole two-dimensional space and every constrained
edge is strictly negative; its largest possible value is `-1`.
Nevertheless every ordinary Hankel matrix of its spectral moments is
positive semidefinite.

This example lies in the exact finite confluent-Loewner class.  At two
critical nodes, at the normalized level `K=L^(-2)H_nu`, choose Hermite data

```text
J(tau_1)=J(tau_2)=0,
J'(tau_1)=-L^2,     J'(tau_2)=-2*L^2.               (4.4)
```

The off-diagonal divided difference is zero and the normalized confluent
diagonal is exactly (4.1).  Equivalently, the unscaled derivative data
`(-1,-2)` realize `H_bad=diag(-1,-2)`, whose normalized copy has the same
strict sign and nonzero-variance obstruction.  The finite signed-multiplier
realization theorem for the
sharp confluent-Loewner class (proved in the constrained sharp-Loewner
audit) realizes these real Hermite data by a signed smooth sharp multiplier.
Adding that multiplier to the fixed gamma and pole density leaves those
completion terms present and prescribes the same total two-dimensional
compression.

Therefore the following package does not imply Lanczos admission:

```text
Hermiticity + sharp square representation
+ confluent Loewner/rank-two displacement
+ all ordinary Krylov Hankel positivities
+ nonzero Lanczos variance.                         (4.5)
```

The model is structural, not an actual-von-Mangoldt counterexample.  An
actual negative example would exhibit precisely the arithmetic failure the
uniform admission theorem is designed to exclude; none is known.

## 5. Research consequence

The Lanczos route survives in one sharply stated form.  In every candidate
configuration with `m_1<0`, prove for the **actual completed** coefficients
that

```text
m_2^2-m_1*m_3>=0                                   (5.1)
```

and that the resulting `theta_*` in (1.6) is bounded below by the carrier
fraction needed on the divisor side.  Equivalently, prove the one-sided
central-skew inequality obtained from (1.8):

```text
tau_3
 >=-[sigma^2/(1-theta)]
      *[m_1+2*sqrt(theta*(1-theta))*sigma]           (5.2)
```

when the boundary witness is used.  For the exact criterion at all signs of
the transverse diagonal, (1.6) is preferable to (5.2).

This is a scalar theorem, but it is not a positive-moment theorem.  Its
prime expansion contains signed cubic correlations and mixed completion
words.  Any proof that estimates those words separately discards the sign
reversal in (5.1).  A viable proof must instead pair or reorganize the words
in (3.7)--(3.8) so that opposite-sign spectral mixing dominates, or derive
the same conclusion directly from the completed signed measure (3.10).

The exact new frontier is therefore narrower than “control `m_1,m_2,m_3`”:

> Prove a carrier-uniform **nonpositive shifted-Hankel determinant** (with the
> quantitative root bound (1.6)) whenever the actual full-carrier completed
> scalar is negative.

That implication is genuinely weaker than `m_1>=0`, and it would convert a
negative full-carrier scalar into a nonnegative sub-full Ritz witness.  It
is not supplied by ordinary moment positivity, Loewner displacement, or the
known separate prime-polynomial estimates.
