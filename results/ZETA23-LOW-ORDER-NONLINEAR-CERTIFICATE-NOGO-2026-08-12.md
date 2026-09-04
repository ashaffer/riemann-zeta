# Low-order nonlinear certificates see the pair, but not from the known moments

Status: exact `2 x 2` pair detector, an exact all-low-principal-minors
countermodel with the Zeta23 first two moments and the required positive
mate, and a shifted-Weil domain audit, 2026-08-12.  No zero-free strip is
proved.

## 1. Verdict

There is a genuine low-order zero-side mechanism.  Two normalized
Paley--Wiener packets separated by `D=d_*L` compress one reflected pair to

```text
M_pair=m_L*[[1,C],[C,1]],
C=cosh(alpha*D),          m_L=2*A_alpha^2/L>0.       (1.1)
```

Consequently

```text
det M_pair=-m_L^2*sinh(alpha*D)^2<0.                 (1.2)
```

Thus a `2 x 2` determinant can detect the selected pair before collateral
rows are restored.  This is the nonlinear form of the mirror-block negative
eigenvector.

What fails is the proposed arithmetic shortcut.  The known trace and
Frobenius moments are global.  They neither determine the trace and
Frobenius norm of this selected compression nor control its off-diagonal
entry.  Theorem 3.1 below strengthens the existing exterior-coefficient
countermodel: with the exact Zeta23 first two moments, one carrier-scale
negative eigenvalue, and its required positive mate, **every coordinate
principal submatrix through order `N/(1+3*kappa)` can still be positive
semidefinite**.  In particular, every `2 x 2` coordinate minor can have the
Pick sign.

An adaptively chosen pair of tests can of course find the negative direction.
But its arithmetic determinant is then a target-specific two-correlation
quantity.  Neither the evaluated moments, the rank-two displacement identity,
nor the present KMT bounds control its sign.  The shifted-xi de Branges
kernel detects an offending zero even with one atom, but it has no nonzero
common vector with the compact-support Fourier domain of the certified Weil
form, and below `Re s=1` it has no termwise absolutely convergent prime
expansion.

The binary outcome is therefore

```text
selected zero-side 2x2 detector:                    PASS;
deduction of its arithmetic sign from two moments: FAIL;
fixed finite-window/minor bank from those moments: FAIL;
adaptive completed 2x2 arithmetic theorem:         OPEN, strip-strength;
shifted de Branges import of the certified window: DOMAIN FAIL.          (1.3)
```

## 2. The exact two-packet determinant

Let `u,v` be the two orthonormal packets in (1.1).  The exact eigenvectors
and eigenvalues are

```text
e_+=(u+v)/sqrt(2),       lambda_+=m_L*(1+C),
e_-=(u-v)/sqrt(2),       lambda_-=m_L*(1-C).         (2.1)
```

For `alpha*D -> infinity`, the negative magnitude is

```text
kappa_pair=m_L*(C-1)=X^(alpha*d_*-o(1))/L.          (2.2)
```

For any Hermitian `2 x 2` matrix `G`,

```text
det G=((tr G)^2-tr(G^2))/2.                         (2.3)
```

Applied to (1.1),

```text
tr M_pair=2*m_L,
tr(M_pair^2)=2*m_L^2*(1+C^2),                       (2.4)
```

and (2.3) is exactly (1.2).  Hence a *localized* first and second moment for
this same two-dimensional compression would decide its determinant.  The
Zeta23 identities instead give `tr H` and `tr(H^2)` after summing over the
whole `N`-dimensional window.  Passing from those global quantities to
(2.4) is precisely the missing localization step.

Adding a background `B` also shows why determinant nonlinearity is not free:

```text
det(B+M_pair)
```

contains the target-specific diagonal and off-diagonal entries of `B`.
There is no identity expressing this determinant using only `tr H` and
`tr(H^2)` of the full matrix.

Nor does the certified fixed-support form already contain this detector.
The two packets in (1.1) have physical separation `D=d_*L`, which tends to
infinity.  A common modulation changes their frequency center but not that
physical diameter, and a common translation moves both packets without
shortening it.  They therefore cannot both lie in the fixed
`[-7/16,7/16]` support underlying the certified base theorem.  Rescaling
them into that interval changes the prime translations and the Weil
normalization, so it is not an application of the certificate.  Positivity
of every `2 x 2` Gram matrix wholly inside the certified domain is true but
does not isolate the distant pair.

## 3. Exact all-low-minors moment countermodel

The following strengthens Theorem 4.2 of the endpoint-jet exterior audit.
That theorem made the exterior traces `e_r` nonnegative for a long prefix.
Here every principal compression in a fixed coordinate system is
nonnegative through the same range.

### Theorem 3.1 (one flat defect hidden from all low coordinate minors)

Let `K_N -> 4/3`, let `kappa_N>0`, and assume

```text
kappa_N^2/N ->0.                                    (3.1)
```

For every sufficiently large `N`, there is an `N x N` Hermitian matrix
`H_N` such that

```text
tr H_N=N,
tr(H_N^2)=K_N*N,                                    (3.2)

spec(H_N) contains -kappa_N and kappa_N+2,
all other eigenvalues are positive and at least 1/3. (3.3)
```

Moreover the unit eigenvector `w_N` for `-kappa_N` can be chosen flat in the
coordinate basis,

```text
abs((w_N)_j)^2=1/N,          1<=j<=N,                (3.4)
```

and every coordinate principal compression `H_(N,S)` obeys

```text
H_(N,S)
 >=[1/3-(kappa_N+1/3)*abs(S)/N]*I_S.                (3.5)
```

Consequently

```text
H_(N,S)>=0 whenever abs(S)<=N/(1+3*kappa_N),        (3.6)
```

so every principal minor contained in every such block is nonnegative.
Nevertheless the full determinant is negative.

#### Proof

Use the exact spectrum constructed in Theorem 4.2 of
`ZETA23-ENDPOINT-JET-EXTERIOR-EDGE-GATE-2026-08-11.md`.  Its two exceptional
eigenvalues are `-kappa_N,kappa_N+2`; its remaining eigenvalues give (3.2)
and are eventually at least `1/3`.  Spectral moments do not depend on the
eigenvectors, so choose the negative eigenvector to be the flat vector
(3.4), and complete it to an orthonormal eigenbasis.

Put

```text
H_(N,+)=H_N+(kappa_N+1/3)*w_N*w_N^*.                (3.7)
```

This replaces the one negative eigenvalue by `1/3` and leaves every other
eigenvalue unchanged.  Hence

```text
H_(N,+)>=(1/3)*I.                                   (3.8)
```

For the coordinate projection `P_S`, (3.4) gives

```text
norm(P_S*w_N)^2=abs(S)/N.                           (3.9)
```

Compress (3.7), use (3.8), and subtract the rank-one term.  Its operator
norm on the compressed space is
`(kappa_N+1/3)*abs(S)/N`, proving (3.5)--(3.6).  Since `H_N` has exactly one
negative eigenvalue and no zero eigenvalue, its determinant is negative.
QED

### Carrier specialization

For the reduced asymmetric carrier,

```text
kappa_N=X^(alpha*d_*-o(1))/L,
N=(1+o(1))*T*L/(2*pi),
alpha<1/2,             d_*<2/3.                     (3.10)
```

Then `kappa_N^2=o(N)`, while the first potentially informative coordinate
minor can be delayed until order

```text
N/kappa_N
 =T*L^2/X^(alpha*d_*+o(1))
 =T^(1-alpha*d_*+o(1)).                             (3.11)
```

This is at least `T^(2/3+o(1))` in the limiting ledger.  Fixed order,
logarithmic order, and every currently tractable exterior degree are far
below it.

The theorem is basis-specific, as every principal-minor statement must be.
It does not say that an adaptive compression cannot find the negative
eigenvector.  It says that the two moments do not identify such a
compression and permit a coordinate realization in which all low minors
have the wrong sign for detection.

### Corollary 3.2 (a predetermined finite test bank can be avoided)

Let `E_N` be any prescribed proper subspace.  The eigenvector for
`-kappa_N` in the same spectral construction may be chosen in `E_N^perp`.
Then

```text
P_(E_N) H_N P_(E_N)>=(1/3)*P_(E_N).                 (3.12)
```

Thus no predetermined finite family of packet windows, and no fixed bank
whose span is a proper subspace, is forced by (3.2) to see the defect.  A
target-adaptive family escapes this corollary, but then needs new arithmetic
control of that selected compression.

## 4. The arithmetic `2 x 2` determinant is a correlation theorem

Let `f_1,f_2` be two admissible packets and let

```text
H_(ij)=integral_R g_i(t)*conj(g_j(t))*nu_X(t)dt,    (4.1)
```

where `nu_X` is the complete signed gamma--pole--prime density.  The
`r=2` case of continuous Cauchy--Binet/Andreief gives

```text
det H
 =1/2*integral_(R^2)
    abs(det[[g_1(t_1),g_1(t_2)],
            [g_2(t_1),g_2(t_2)]])^2
    *nu_X(t_1)*nu_X(t_2) dt_1 dt_2.                 (4.2)
```

The squared determinant is nonnegative, but `nu_X` is signed.  Expanding
the two factors of `nu_X` produces all gamma--prime, pole--prime, and
prime--prime correlations of degree at most two.  The evaluated Frobenius
moment sums related squares over the entire coordinate family; it does not
give the sign of the selected integral (4.2).

The sharp Loewner/Pick representation reaches the same boundary.  For two
Jacobi nodes `lambda_1,lambda_2`, its `2 x 2` determinant contains

```text
F'(lambda_1)*F'(lambda_2)
 -abs((F(lambda_1)-F(lambda_2))/(lambda_1-lambda_2))^2.  (4.3)
```

The diagonal data are the transformed completed quantities `D_X`; they are
not fixed by the off-diagonal divided differences.  Proposition 6.1 of the
sharp Loewner audit proves that arbitrary finite confluent data can be
realized by smooth signed multipliers.  KMT bounds their magnitude but not
the joint sign in (4.3).  Rank-two displacement therefore gives an exact
test, not a positive test.

A successful low-order route would need a new **targeted** inequality of one
of the following equivalent kinds:

```text
det H>=0 for the target-adaptive packets;
tr((P_E H P_E)^2)<=(tr(P_E H P_E))^2 for dim(E)=2;
the completed two-node Pick determinant (4.3) has the required sign.       (4.4)
```

No current first/second moment or fixed-window certificate implies (4.4).

## 5. Shifted-Weil and de Branges domain audit

There is an exact fixed-strip nonlinear criterion, but it does not import
the certified compact-support form.  For

```text
E_omega(z)=xi(1/2+omega-i*z),
```

the de Branges kernel is

```text
K_omega(z,w)
 =[E_omega(z)*conj(E_omega(w))
   -E_omega#(z)*conj(E_omega#(w))]
   /[2*pi*i*(conj(w)-z)].                            (5.1)
```

If `rho=1/2+d+i*gamma`, `d>omega`, and
`z=-gamma+i(d-omega)`, then `E_omega(z)=0` and, except at a discrete set of
shifts where the reflected value also vanishes,

```text
K_omega(z,z)<0.                                     (5.2)
```

So this route detects the offending zero with a `1 x 1` minor.  The problem
is not detector order.

The gamma factor separates its form domain from the certified Weil domain.
If `f in L^2(-a,a)` and `F` is its Fourier transform, then

```text
F/E_omega in L^2(R)  implies  f=0.                  (5.3)
```

Indeed `E_omega(t)` decays like a polynomial times `exp(-pi*abs(t)/4)`;
(5.3) gives an exponentially weighted `L^2` bound on `F`, analytically
continues the zero extension of `f` to a strip, and the identity theorem
forces it to vanish.  Thus the identity Fourier map has no nonzero common
vector between compact-support tests and the shifted de Branges space.

There is a second boundary.  Every exact strip criterion with
`omega<1/2` lies at `Re s=1/2+omega<1`.  Its logarithmic-derivative prime
series is not termwise absolutely convergent.  Keeping the entire xi-product
kernel is legitimate; splitting it into an arithmetic Pick matrix requires
analytic continuation whose zero residues encode the divisor one is trying
to exclude.

Ordinary finite shifts should not be blamed for this mismatch.  Modulation
of a `C_c^2` packet and multiplication by `exp(omega*t)` preserve compact
support and the local Weil form domain.  What fails is the additional claim
that the resulting Fourier transform belongs to `B(E_omega)` or that its
Pick norm is controlled by the certified arithmetic Weil norm.  A viable
shifted route needs a nonidentity gamma-smoothing adapter and an independent
all-place comparison theorem.

## 6. Exact disposition and novelty

The low-order nonlinear family has now separated into two statements.

1. The selected reflected pair has an exact negative `2 x 2` PW/Gabor
   determinant.  This is a useful concrete detector.
2. Proving the opposite arithmetic sign for the same adaptive packets is a
   new two-correlation theorem.  Global moments, low displacement, and fixed
   window positivity do not provide it.

Theorem 3.1 is a strict internal strengthening of the earlier exterior-trace
countermodel: it makes every low coordinate principal block positive, not
only the sum `e_r` of its principal minors.  Its proof is elementary
rank-one compression and should not be advertised as a standalone new
matrix theorem.  The `2 x 2` identity, Andreief formula, matrix determinant
lemma, and de Branges kernel facts are classical.  The potentially
publishable content is their normalization-specific synthesis with the
Zeta23 carrier and moment scales, preferably as part of a broader rigorous
obstruction paper rather than as an isolated claim.

The exact next theorem, if this family is pursued, is (4.4) for the complete
actual von Mangoldt--continuum--gamma data and the target-adaptive two-packet
space.  Calling it a determinant, Pick, exterior, or de Branges condition
does not weaken it: it is the same missing target-specific arithmetic sign.

## Sources inside this project

- [`ZETA23-ASYMMETRIC-PW-MIRROR-BLOCK-REALIZATION-AUDIT-2026-08-12.md`](ZETA23-ASYMMETRIC-PW-MIRROR-BLOCK-REALIZATION-AUDIT-2026-08-12.md)
- [`ZETA23-ENDPOINT-JET-EXTERIOR-EDGE-GATE-2026-08-11.md`](ZETA23-ENDPOINT-JET-EXTERIOR-EDGE-GATE-2026-08-11.md)
- [`ZETA23-CONSTRAINED-SHARP-LOEWNER-PRIME-EDGE-2026-08-11.md`](ZETA23-CONSTRAINED-SHARP-LOEWNER-PRIME-EDGE-2026-08-11.md)
- [`ZETA23-COMPLETED-CONSTRAINED-PICK-KMT-OBSTRUCTION-2026-08-11.md`](ZETA23-COMPLETED-CONSTRAINED-PICK-KMT-OBSTRUCTION-2026-08-11.md)
- [`SHIFTED-WEIL-FIXED-STRIP-GATE-2026-08-11.md`](SHIFTED-WEIL-FIXED-STRIP-GATE-2026-08-11.md)
