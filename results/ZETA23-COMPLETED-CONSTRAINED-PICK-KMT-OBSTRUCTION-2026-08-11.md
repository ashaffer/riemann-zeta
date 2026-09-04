# The completed constrained Pick edge: the KMT information barrier

Status: exact completion-preserving reduction, an adversarial completed-data
model, and a conditional actual-data obstruction, 2026-08-11.  This note
proves no prime lower edge and no zero-free strip.

## 1. Result

Let `X=exp(L)` be in the transition band

```text
T*(log T)^(-C) <= X <= T*(log T)^C,
```

let `tau_k=tau_0+2*pi*k/L` be a critical grid contained in `[T,2T]`, and
let `W_m` be the endpoint-jet moment-null space.  The complete sharp density
is

```text
nu_X(t)=mu(t)+1/[2*pi*(1/4+t^2)]
        -(1/pi)*Re E_X(t),                            (1.1)

E_X(t)=sum_(n<=X) Lambda(n)n^(-1/2+it)
       -integral_1^X x^(-1/2+it)dx.                  (1.2)
```

Thus the oscillatory part of the zeta-pole term does not disappear: it
centers the **complete** von Mangoldt polynomial by its continuum main term.
Put

```text
A(t)=Im E_X(t),
D(t)=Re[L*E_X(t)+i*E_X'(t)]
    =L*Re E_X(t)-A'(t).                              (1.3)
```

After the harmless `(-1)^k` conjugation, the complete matrix is exactly

```text
H_nu=H_bg+H_E,
H_bg=H_mu+H_0,

H_E(k,l)=2*(A(tau_k)-A(tau_l))/(tau_k-tau_l), k!=l,
H_E(k,k)=-2*D(tau_k),                                (1.4)
```

where `H_0` is the Gram matrix of the positive rational density in (1.1).
No prime, prime power, continuum center, gamma term, or pole term is removed
in (1.1)--(1.4).

The exact background has the one-sided bounds

```text
-2*pi*L*I <= H_bg|W_m <= C_gamma*L^2*I.              (1.5)
```

Consequently the Klurman--Mangerel--Teravainen logarithmic estimate gives
only

```text
lambda_min(L^(-2)*H_nu|W_m)
 >=-O_C(sqrt(X)/L^(13/10)+1/L).                      (1.6)
```

If the actual normalized carrier margin at a fixed depth
`0<alpha<1/2` is

```text
K=(X^alpha/L)*r_T,                                   (1.7)
```

then the **certificate (1.6)** is `o(K)` only if

```text
X^(1/2-alpha)/(L^(3/10)*r_T) -> 0.                  (1.8)
```

In particular it does not close even at `r_T=O(1)`, and it cannot close
uniformly over the much smaller margins allowed by the current tail-rate
carrier theorem.

This comparison is already the core-pair comparison: the distinguished
off-line pair may be kept a fixed positive distance inside `[T,2T]`.  No
collar atom or overbroad `J_D` carrier is used in (1.6)--(1.8), so suppressing
the collar does not affect the obstruction.

Endpoint jets and the completed rank-two/Jacobi displacement do not supply a
missing factor for (1.6).  The coefficient-exact survival theorem below says
more precisely what KMT leaves unresolved.  If, along a sequence of heights,
the **actual centered data** in (1.2)--(1.3) have a positive-density family of
positive diagonal values of size `M`, while their off-diagonal oscillation is
`O(M/L)`, then for `m/d=o(1)` the full completed compression has

```text
lambda_min(L^(-2)*H_nu|W_m)<=-(2*theta+o(1))*M/L^2.  (1.9)
```

Here `theta*M` is the lower bound for those diagonal values and
`M/L^2 -> infinity`; all completion terms are present in (1.9).  Taking

```text
M=sqrt(X)/L^(3/10)                                   (1.10)
```

is compatible with the KMT magnitude bounds.  KMT supplies no sign,
positive-density, or joint `A,D` information that excludes this alternative.
Equation (1.3) does not exclude it either: critical samples of `A` do not
control `A'`.

This is an obstruction to the inference

```text
KMT logarithmic bounds + endpoint jets + rank-two displacement
    => completed normalized negative edge o(K).      (1.11)
```

It is not an assertion that the actual zeta data satisfy the saturation
hypothesis of (1.9).  A direct Pick theorem could still exploit arithmetic
joint cancellation which is absent from KMT.  Such a theorem is not proved
here.

There are two logically different obstruction statements below.

1. Section 4.1 constructs an exact completed positive-coefficient model
   obeying the KMT-sized inequalities and all the finite-dimensional
   structural identities, but its coefficient is deliberately **not** the
   von Mangoldt coefficient.  It proves that positivity, completion,
   rank-two displacement, the `A,D` relation, and the KMT inequalities do not
   form a sufficient abstract theorem.
2. Theorem 5.1 and Corollary 5.2 never change a coefficient.  They state what
   happens if the actual centered von Mangoldt data have a sign-density
   pattern which KMT does not exclude.  They do not prove that pattern is
   arithmetically realizable.

This distinction is essential: an adversarial scalar model is not evidence
that the actual primes saturate KMT.

## 2. Exact completion before compression

Write

```text
Z_X(t)=sum_(n<=X) Lambda(n)n^(-1/2+it),
C_X(t)=integral_1^X x^(-1/2+it)dx
      =[X^(1/2+it)-1]/(1/2+it).                      (2.1)
```

The exact Zeta23 pole density is

```text
Pi_X(t)=1/[2*pi*(1/4+t^2)]+(1/pi)*Re C_X(t),         (2.2)
```

and its prime density is `P_X=-(1/pi)*Re Z_X`.
Equations (1.1)--(1.2) follow immediately.  These are the definitions in the
paper and in the official formal artifact; in particular, the continuum term
in (2.2) is not an optional approximation.

Let `H_w` denote the sign-conjugated sharp matrix associated with a real
multiplier `w`.  The one-frequency Cauchy-transform calculation is linear in
the frequency measure.  Applying it to

```text
dPsi_X(y)=sum_(n<=X) Lambda(n)n^(-1/2)*delta_(log n)(dy),
dm_X(y)=1_[0,L](y)*exp(y/2)dy                         (2.3)
```

gives (1.4) with

```text
E_X(t)=integral_[0,L] exp(i*t*y)*(dPsi_X-dm_X)(y).    (2.4)
```

Indeed each frequency `y` contributes the off-diagonal divided difference of
its sine and the diagonal `(L-y)` times its cosine.  Differentiating (2.4)
therefore gives exactly

```text
Re[L*E_X+i*E_X']
 =integral_[0,L] (L-y)*cos(t*y)*(dPsi_X-dm_X)(y),     (2.5)
```

which proves both (1.3) and (1.4).

There is an equivalent completion-preserving time-domain identity.  If
`f` is the admissible sharp packet corresponding to `x in W_m`, put

```text
R_f(y)=integral f(u)*conj(f(u+y))du.                 (2.6)
```

Plancherel gives

```text
x^*H_E*x
 =-2*integral_[1,X] v^(-1/2)*Re R_f(log v)
                       d(psi(v)-v),                 (2.7)
```

where `d psi` has the positive atoms `Lambda(n)`.  Thus positivity of every
von Mangoldt coefficient is retained exactly.  It does not turn (2.7) into a
positive or negative measure pairing: the pole completion changes `d psi` to
the signed discrepancy `d(psi-x)`, and the modulated autocorrelation
`Re R_f` also has no fixed sign.  Endpoint vanishing does not alter either
fact.

## 3. The completed background has normalized size at most constant

Put

```text
r_0(t)=1/[2*pi*(1/4+t^2)].                            (3.1)
```

The proved gamma facts used by Zeta23 include

```text
mu(t)>=mu(0)>-1,
abs(mu(t))<=C*log(2+abs(t)).                          (3.2)
```

Since `r_0>=0` and the constant multiplier has matrix
`H_1=2*pi*L*I`, (3.2) immediately gives the lower inequality in (1.5).

For completeness, the upper inequality uses the endpoint conditions and not
a deletion of the background.  Undo the sign conjugation and write

```text
f(u)=1_[-L/2,L/2](u)*sum_k c_k*exp(-i*tau_k*u),
sum_k abs(c_k)^2=1.                                  (3.3)
```

For `m>=1`, the trigonometric polynomial in (3.3) vanishes at both
endpoints, so the zero extension of `f` is in `H^1`.  Critical spacing and
orthogonality give

```text
integral abs(f)^2=L,
integral abs(f')^2=L*sum_k tau_k^2*abs(c_k)^2
                  <=4*T^2*L.                        (3.4)
```

With the paper Fourier convention, Plancherel gives the corresponding
identities for `integral abs(F)^2` and `integral t^2*abs(F)^2`.  The elementary
bound

```text
log(2+abs(t))<=log(2+2*T)+t^2/T^2                   (3.5)
```

then yields

```text
integral abs(F(t))^2*mu(t)dt <= C_gamma*L*log T
                             <= C_gamma'*L^2.        (3.6)
```

Finally `0<=r_0<=2/pi`, so

```text
0<=H_0<=(2/pi)*H_1=4*L*I.                            (3.7)
```

Equations (3.2)--(3.7) prove (1.5) on `W_m` (and the lower inequality even
before compression).  In the isolated-zero normalization `1/L^2`, the
completed gamma--rational background is bounded below by `-2*pi/L` and above
by an absolute constant.  It cannot cancel a power-sized KMT uncertainty by
a deterministic scale estimate.

## 4. What KMT proves for the exact centered data

For `t in [T,2T]`, (2.1) gives

```text
abs C_X(t)<=(sqrt(X)+1)/T,                            (4.1)

abs Re[L*C_X(t)+i*C_X'(t)]
 <=(sqrt(X)+1)/T^2+L/T.                              (4.2)
```

The second formula is the exact identity

```text
integral_1^X x^(-1/2+it)*(L-log x)dx
 =[X^(1/2+it)-1-(1/2+it)*L]/(1/2+it)^2.              (4.3)
```

Define the exact completed scalar size

```text
B_E=osc_k A(tau_k)+(2/L)*max_k abs D(tau_k).         (4.4)
```

The discrete Hilbert-commutator form in (1.4) gives

```text
norm(H_E)<=L*B_E.                                    (4.5)
```

The KMT consequence proved in the scalar audit is, uniformly in the
transition band,

```text
abs Z_X(t)<<_C sqrt(X)/L^(3/10),
abs D_X(t)/L<<_C sqrt(X)/L^(13/10).                  (4.6)
```

Combining (4.1)--(4.6), without changing a von Mangoldt coefficient, gives

```text
B_E<<_C sqrt(X)/L^(3/10).                            (4.7)
```

Orthogonal compression preserves (4.5).  Adding the exact background lower
bound from (1.5) proves (1.6).  Dividing its right side by (1.7) gives

```text
[sqrt(X)/L^(13/10)]/[(X^alpha/L)*r_T]
 =X^(1/2-alpha)/(L^(3/10)*r_T),                      (4.8)
```

which proves (1.8).

Notice that (4.8) is already divergent for every fixed `alpha<1/2` when
`r_T=O(1)`.  The unspecified loss in the current carrier margin only worsens
the comparison.  This is a statement about the strength of the KMT-derived
certificate, not a lower bound for the actual negative eigenvalue.

### 4.1 Exact adversarial completed-data model (not von Mangoldt)

The scale obstruction above can be made algebraically sharp while retaining
the pole and gamma terms.  This model is included only to identify exactly
what the listed structural inputs can and cannot prove.

Take `X=N^2`, `y=log N=L/2`, and choose a permitted critical-grid origin so
that

```text
tau_0*y in 2*pi*Z.
```

Such an origin occurs within `O(1/L)` of any prescribed large starting
height.  Let

```text
M=sqrt(X)/L^(3/10),
a=2*M/L,
Z_ad(t)=a*exp(i*t*y),
E_ad(t)=Z_ad(t)-C_X(t),                               (4.9)
```

and form the **complete** density

```text
nu_ad(t)=mu(t)+Pi_X(t)-(1/pi)*Re Z_ad(t)
         =mu(t)+r_0(t)-(1/pi)*Re E_ad(t).             (4.10)
```

The single sharp coefficient `a` is positive and is supported at the integer
`N<=X`.  It is an artificial coefficient, not `Lambda(N)/sqrt(N)`.

At the critical nodes, `h*y=pi`, and hence

```text
Im Z_ad(tau_k)=0,
Re[L*Z_ad(tau_k)+i*Z_ad'(tau_k)]=M*(-1)^k.            (4.11)
```

The continuum estimates (4.1)--(4.2) show

```text
L*osc_k Im E_ad(tau_k)=o(M),
Re[L*E_ad+i*E_ad'](tau_k)=M*(-1)^k+o(M).              (4.12)
```

Moreover

```text
abs Z_ad(t)<=2*sqrt(X)/L^(13/10)
             <=2*sqrt(X)/L^(3/10),

abs Re[L*Z_ad+i*Z_ad']/L
             =sqrt(X)/L^(13/10).                     (4.13)
```

Thus the model satisfies the two KMT-sized scalar inequalities, with room in
the first, and it satisfies the exact derivative relation.  Its centered
Loewner matrix is diagonal up to the `o(M)` continuum correction, with
`-2M+o(M)` on half the diagonal.  Since `m/d=o(1)`, Theorem 5.1 below and
the background bound (1.5) give

```text
lambda_min(L^(-2)*H_nu_ad|W_m)
 <=-(2+o(1))*M/L^2.                                  (4.14)
```

Every completion sign and constant in (4.10) is the Zeta23 one: the
`+(1/pi) Re C_X` in `Pi_X` cancels the same term in
`-(1/pi) Re Z_ad`, leaving `-(1/pi) Re E_ad`; the rational pole density and
`mu` remain in the matrix.

The model proves a precise information-level no-go.  It does **not** preserve
the actual coefficient size or the actual von Mangoldt sequence, so (4.14)
is not an arithmetic counterexample.  In particular, the special coefficient
in (4.9) is much larger than `Lambda(N)/sqrt(N)`.  Actual-coefficient
realizability is addressed only by the conditional theorem below.

## 5. Jacobi/Pick form and exact survival through `W_m`

Let `P_m` be the orthogonal projection onto `W_m`, and put

```text
J_m=P_m*diag(tau_k)*P_m|W_m,
B_m=P_m*H_nu*P_m|W_m.                                (5.1)
```

In the discrete orthogonal-polynomial basis, `J_m` is the trailing
irreducible Jacobi matrix.  If `q_(m-1)` is the last discarded orthogonal
polynomial and

```text
r_b=P_m*diag(tau_k)*q_(m-1),
s_b=P_m*H_nu*q_(m-1),                                (5.2)
```

then the **complete** matrix obeys

```text
[J_m,B_m]=s_b*r_b^*-r_b*s_b^*.                       (5.3)
```

After diagonalizing `J_m`, (5.3) is the exact confluent Pick matrix from the
Loewner report.  Its off-diagonal data are divided differences and its
diagonal data are free confluent entries.  In the present arithmetic matrix,
those entries contain the actual `D(tau_k)` of (1.3), transformed together
with the gamma and rational-pole entries.  Rank two in (5.3) does not bound
their sign.

The following theorem makes the endpoint issue quantitative without
replacing the arithmetic coefficients by an arbitrary diagonal.

### Theorem 5.1 (actual completed diagonal survival)

For the coordinate vector `e_k`, set

```text
ell_k=<e_k,(I-P_m)e_k>.
```

If `ell_k<1`, put `u_k=P_m e_k/sqrt(1-ell_k)`.  For every
`0<epsilon<1`, all but at most `m/epsilon` indices have
`ell_k<=epsilon`, and each such index satisfies the exact decomposition

```text
u_k^*H_nu*u_k
 =-2*D(tau_k)+R_k+u_k^*H_bg*u_k,                     (5.4)

abs R_k<=2*L*B_E*sqrt(2-2*sqrt(1-epsilon)),          (5.5)

-2*pi*L<=u_k^*H_bg*u_k<=C_gamma*L^2.                (5.6)
```

#### Proof

The projection has complementary rank `m`, hence

```text
sum_k ell_k=m.                                       (5.7)
```

Markov's inequality gives the exceptional count.  Moreover

```text
norm(u_k-e_k)^2=2-2*sqrt(1-ell_k).                   (5.8)
```

For a Hermitian matrix `H` and unit vectors `u,e`,

```text
abs(u^*H*u-e^*H*e)<=2*norm(H)*norm(u-e).             (5.9)
```

Apply (5.9) to the exact centered matrix `H_E`, use
`H_E(k,k)=-2D(tau_k)` and (4.5), and then restore `H_bg` exactly.  Equation
(1.5) proves (5.6).  QED

### Corollary 5.2 (KMT-compatible saturation alternative)

Suppose along a sequence `T -> infinity` that

```text
m/d=o(1),
M/L^2 -> infinity,                                   (5.10)

max_k abs D(tau_k)=O(M),
L*osc_k A(tau_k)=O(M),                               (5.11)
```

and, for fixed `beta,theta>0`,

```text
#{k:D(tau_k)>=theta*M}>=beta*d.                      (5.12)
```

Then

```text
lambda_min(L^(-2)*H_nu|W_m)
 <=-(2*theta+o(1))*M/L^2.                            (5.13)
```

#### Proof

Choose `epsilon=2m/(beta*d)` (with an arbitrary vanishing positive choice
when `m=0`).  For large `T`, (5.7) leaves an index satisfying both (5.12) and
`ell_k<=epsilon`.  Equations (5.10)--(5.11) give

```text
L*B_E=O(M),
sqrt(2-2*sqrt(1-epsilon))=o(1).                      (5.14)
```

Insert this index into (5.4)--(5.6).  The `R_k` term is `o(M)` and the
complete background is `O(L^2)=o(M)`.  The Rayleigh principle and division
by `L^2` prove (5.13).  QED

This is an actual-coefficient theorem: (5.11)--(5.12) refer to the single
pair generated by the complete von Mangoldt sum and its exact continuum
center.  The theorem does not assert those hypotheses.  It says that if the
actual data take this KMT-permitted form, neither the endpoint codimension
nor the gamma/pole completion erases the bad direction.

At the KMT scale (1.10), the assumptions `max|D|=O(M)` and
`L*osc A=O(M)` are consistent with (4.6)--(4.7); KMT does not imply the
stronger oscillation condition, but it also does not exclude it.  Nor does it
give the sign-density negation of (5.12).  The exact relation
`D=L Re E-A'` supplies no such negation because values of `A` on a critical
grid do not stably bound its derivative.  Therefore a direct Pick proof must
add genuinely joint arithmetic information, rather than count the factor
`(1-z)^m` as a saving.

## 6. Fixed-depth disposition

For fixed `0<alpha<1/2`, if (5.10)--(5.12) hold with the KMT scale (1.10),
then the ratio of the surviving negative magnitude in (5.13) to the carrier
scale (1.7) is

```text
[M/L^2]/[(X^alpha/L)*r_T]
 =X^(1/2-alpha)/(L^(13/10)*r_T).                     (6.1)
```

Thus it even dominates a carrier with `r_T=O(1)`.  KMT does not prove this
bad alternative, but it cannot eliminate it.  The exact constrained Pick
route remains open only in the following form:

```text
prove directly, for the actual joint A,D data and the complete H_bg,
that lambda_min(L^(-2)*H_nu|W_m)>=-o(K),

or prove new arithmetic information excluding every diagonal- and
commutator-dominated KMT-scale alternative at the actual carrier K.       (6.2)
```

The scalar KMT estimate, coefficient positivity, the identity
`D=L Re E-A'`, endpoint jets, and the common rank-two Jacobi displacement do
not supply (6.2) in combination.  This note makes no assertion about whether
the actual zeta data realize the unresolved alternative, proves no uniform
negative edge, and implies no zero-free strip.

The positivity question has a definitive limited answer.  The one-sided
Stieltjes fact `d psi>=0` does **not** rule out the sign-density mechanism:
(2.7) pairs it with a sign-changing modulated autocorrelation and the exact
pole completion replaces it by `d(psi-x)`; the positive one-coefficient model
of Section 4.1 realizes the bad pattern.  What remains possible is a theorem
using the **specific** sizes, locations, and multiplicative correlations of
the von Mangoldt atoms.  No such theorem follows from positivity or from the
KMT magnitude estimates, and none is proved here.
