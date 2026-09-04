# Actual-Lambda GA2: the target deletes itself, leaving a deep-collateral orientation theorem

Status: exact actual-von-Mangoldt coefficient theorem, exact transverse
Gram expansion, actual-candidate divisor reduction, and rigorous scoped
isolation obstruction, 2026-08-13.  No carrier-sized transverse reserve,
zero-free strip, or RH statement is proved.

## 1. Verdict

The proposed coherent two-dimensional reserve is not driven by a new piece
of the selected target's prime resonance.  On the selected-positive quotient
the target contribution is exactly rank one and target-parallel.  Both
transverse quantities

```text
Z_rho=||P_W R_Lambda,rho e||,
lambda_+(rho)=lambda_max(P_W R_Lambda,rho P_W)       (1.1)
```

delete it identically.  If `rho` is an **actual hypothetical zeta zero**, the
Guinand--Weil formula gives

```text
R_Lambda,rho=R_other,rho,                            (1.2)
```

so (1.1) sees only the unselected divisor.

This yields a sharp fail-fast theorem.  In the normalized compact geometry,
let the selected depth be `alpha`, packet separation be `d*log X`, and

```text
K_rho=X^(alpha*d+o(1))/log X.                       (1.3)
```

The proved strip-sampling estimate makes on-line zeros and every collateral
zero of depth at most `alpha*d-epsilon` have total band norm `o(K_rho)`.
Consequently, if there is no deeper collateral and the separately exposed
remote/open remainder is also `o(K_rho)`, then

```text
r_rho=o(K_rho),
Z_rho=o(K_rho),
lambda_+(rho)=o(K_rho),                              (1.4)
```

and every fixed-fraction two-channel reserve fails, for every arithmetic
phase.

At the intended first-strip parameters

```text
alpha=.49,       d=.66,       alpha*d=.3234,         (1.5)
```

a successful GA2 theorem therefore forces, for every fixed gap parameter
`epsilon>0` to which the strip-sampling theorem is applied, at least one
distinct collateral zero with

```text
Re rho' > .8234-epsilon,                            (1.6)
```

and it forces the **aggregate** compression of all such deep collaterals to
have the favorable carrier-scale orientation, unless that scale instead
comes from the presently open completion/remote ledger.  It does not force
one individual collateral row to have fixed-fraction orientation.  In the
target-only sharp fixture `d=1`, it forces a collateral of depth
`>alpha-epsilon` for every fixed `epsilon` covered by the argument.  No
uniform slowly shrinking gap is claimed.

This is not a counterexample made from fake zeros.  The theorem is
conditional on an actual target zero and says what its actual completed
coefficient matrix would have to contain.  It does not assert that zeta has
an isolated off-line zero.  Its conclusion is that GA2 is not an independent
prime lemma: at leading order it is a deep-collateral **existence and signed
orientation theorem**.  No result located in the literature supplies that
theorem.

## 2. Exact finite actual-Lambda matrix

Use the sign-conjugated sharp grid

```text
tau_k=gamma+2*pi*k/L,       L=log X,                 (2.1)
```

and let `U` be the isometric inclusion of the endpoint-flat,
selected-positive-null coefficient space `S`.  For `0<=u<=L`, put

```text
S_ii(u)=(L-u)cos(tau_i*u),
S_ij(u)=[sin(tau_j*u)-sin(tau_i*u)]/(tau_i-tau_j)   (i!=j),
S_tilde(u)=U^*S(u)U.                                (2.2)
```

Let

```text
B_inf=U^*(H_arch+H_pole)U/L^2.                      (2.3)
```

If `y` is the raw selected negative row after imposing the positive null,
put

```text
e=(U^*y)/||U^*y||,
K=2*m_rho*||U^*y||^2/L^2,                           (2.3a)
```

where `m_rho` is the marked multiplicity (`m_rho=1` for a simple selected
pair).  Equivalently one may fold the multiplicity into the carrier row.

Every prime power `n<=X` enters with its actual coefficient

```text
w_n=Lambda(n)/sqrt(n).                              (2.4)
```

The completed arithmetic matrix and selected carrier are exactly

```text
Q_ar=B_inf-(2/L^2)sum_(n<=X) w_n*S_tilde(log n),
N=K*e*e^*,
R_Lambda=Q_ar+N.                                    (2.5)
```

No zero table is used in (2.5).

### Theorem 2.1 (exact mixed actual-Lambda coefficient)

For every unit `v in W=S intersect e^perp`,

```text
z(v)=<e,R_Lambda v>
    =<e,B_inf v>
     -(2/L^2)sum_(n<=X) Lambda(n)/sqrt(n)
                    *<e,S_tilde(log n)v>.           (2.6)
```

The selected carrier has disappeared because `<e,Nv>=0`.  Formula (2.6) is
the exact arithmetic coefficient whose phase was left unnamed in the
preceding two-channel card.

#### Proof

Insert (2.5) and use `v perpendicular e`.  The finite sum follows from
compact support.  QED

Thus the phase compatible with the algebraic optimum is

```text
phi(v)=-arg z(v).                                   (2.7)
```

For the Schur-optimal direction itself, put

```text
w=P_W R_Lambda e,
Z=||w||,
v_*=w/Z                                              (Z!=0).             (2.8)
```

Up to the inner-product convention, the phase can be absorbed into `v_*`
so that the mixed term is `+Z`.  This does not solve GP: the entire direction
`v_*`, not just one scalar phase, depends on the actual coefficients in
(2.6).  A compatible compact-transfer theorem must be uniform for this
arithmetic-selected direction or verify its geometry after selection.

## 3. The exact two-prime object behind `Z`

Define vectors in `W` by

```text
g_inf=P_W B_inf e,
g_n=-(2/L^2)*Lambda(n)/sqrt(n)
                 *P_W S_tilde(log n)e.              (3.1)
```

Then

```text
w=g_inf+sum_(n<=X)g_n                               (3.2)
```

and hence

```text
Z^2
 =||g_inf||^2
  +2 Re sum_n <g_inf,g_n>
  +sum_(m,n<=X)<g_m,g_n>.                           (3.3)
```

Equation (3.3) is a completed, projected, one-height
`Lambda(m)Lambda(n)` Gram sum.  It retains every off-diagonal pair and the
actual common height.  The Gram matrix in (3.3) is positive semidefinite,
but this gives only the tautology `Z^2>=0`: its off-diagonal terms can delete
the diagonal sum, and the target-adaptive projection can delete the entire
coherent principal vector.

The diagonal alternative is the signed compression

```text
C=P_W B_inf P_W
  -(2/L^2)sum_(n<=X)w_n P_W S_tilde(log n)P_W.       (3.4)
```

The matrices in (3.4) are cosine parts of phase-twisted translation Grams;
they are not positive matrices.  Low displacement rank and Toeplitz
structure therefore do not determine `lambda_max(C)` at a fixed selected
height.

The replay module constructs (2.6) from actual prime powers and independently
constructs (2.5); their mixed entries agree to floating error.  It also
expands (3.3) as the full two-prime Gram sum.

## 4. Exact deletion of the selected target

Now, and only now, assume in a contradiction that

```text
rho=1/2+alpha+i*gamma                               (4.1)
```

is an actual zeta zero, with the whole selected functional-equation orbit
and multiplicity marked consistently.  The completed explicit formula gives
on `S`

```text
Q_ar=-N_rho+R_other,rho.                            (4.2)
```

Since `N_rho=K_rho e e^*`, (2.5) becomes exactly

```text
R_Lambda,rho=Q_ar+N_rho=R_other,rho.                (4.3)
```

Therefore

```text
P_W R_Lambda,rho e=P_W R_other,rho e,
P_W R_Lambda,rho P_W=P_W R_other,rho P_W.           (4.4)
```

This is stronger than saying that a generic covariance might align with the
target.  The target is algebraically absent from both surviving GA2
mechanisms.  Its carrier-sized completed contribution, represented on the
arithmetic side by (2.5)--(2.6), is precisely the component removed by
(4.2)--(4.4).

For a scan point not known to be a zero, (2.5)--(3.4) remain valid arithmetic
identities but (4.2)--(4.4) do not have a divisor interpretation.  This is why
the finite probe cannot be used as evidence that a reserve exists at a zeta
zero.

## 5. Isolation theorem

Let the selected compact packet have separation `dL+O(1)` and carrier

```text
K_rho=X^(alpha*d+o(1))/L.                           (5.1)
```

Split the actual unselected divisor compression as

```text
R_other=R_deep+E_shallow+R_open,                    (5.2)
```

where `R_deep` contains collateral pairs of depth

```text
beta>alpha*d-epsilon,                               (5.3)
```

`E_shallow` contains on-line rows and the remaining pairs in the controlled
dyadic band, and `R_open` contains any remote, collar, inter-scale, or
completion/localization terms not yet proved small in operator norm in this
same packet geometry.

The existing normalized strip-sampling theorem gives

```text
||E_shallow||
 <=X^(alpha*d-epsilon+o(1))*L^O(1)+L^O(1)
 =o(K_rho).                                         (5.4)
```

For the following theorem write

```text
r=<e,R_Lambda e>,
z(v)=<e,R_Lambda v>,
c(v)=<v,R_Lambda v>          (v in W, ||v||=1).     (5.4a)
```

### Theorem 5.1 (two-dimensional isolated-candidate obstruction)

Suppose (4.1) is an actual hypothetical zero.  If `R_deep=0` and

```text
||R_open||=o(K_rho),                                (5.5)
```

then, uniformly for every unit `v in W`,

```text
abs(r)<=o(K_rho),
Z<=o(K_rho),
abs(<v,R_Lambda v>)<=o(K_rho),
abs(lambda_max(P_W R_Lambda P_W))<=o(K_rho).        (5.6)
```

For every fixed `0<eta<1`, the phase-optimized reserve is therefore

```text
eta*r+(1-eta)*c(v)
 +2*sqrt(eta*(1-eta))*abs(z(v))=o(K_rho),           (5.7)
```

and cannot dominate any fixed positive multiple of `eta*K_rho`.

#### Proof

Equations (4.3), (5.2), (5.4), and (5.5) give
`||R_Lambda||=o(K_rho)`.  Every scalar, Schur residual, and compressed
spectral edge in (5.6) is bounded in absolute value by this operator norm.
Substitution proves (5.7).  QED

The band-only statement, with `R_open` omitted and every quantity compressed
to the controlled band, is unconditional under the packet hypotheses of
the strip-sampling theorem.  The full completed statement deliberately
retains (5.5); an unproved remote estimate is not silently imported.

### Corollary 5.2 (what any positive GA2 theorem must prove)

If either

```text
Z_rho>=c*K_rho
```

with a carrier-scale lower bound on the selected transverse diagonal, or

```text
lambda_max(P_W R_Lambda,rho P_W)>=c*K_rho           (5.8)
```

holds for one fixed `c>0`, then at least one of the following must occur:

1. for the chosen fixed `epsilon`, there is a collateral zero of depth
   `>alpha*d-epsilon`;
2. the open remainder has carrier-sized norm;
3. one of the strip-sampling/tail hypotheses used in (5.4)--(5.5) fails.

At `.49,.66`, item 1 is precisely (1.6).  Existence alone is not enough:
the deep compression must also have the favorable mixed angle or positive
edge in (5.8).

## 6. Why the standard analytic tools stop here

### Large sieve and Hilbert inequalities

The Montgomery--Vaughan large sieve and Hilbert inequality control mean
squares or sums over separated evaluation points.  Applied to (3.2), they
can provide upper/Bessel estimates, or averaged information before the
target projection.  The required assertion is a lower bound at one
prescribed candidate height **after** removing the target-parallel component
and the endpoint/positive rows.  No reverse inequality survives an arbitrary
orthogonal projection: a large coherent vector may lie entirely in the
deleted line.  Equation (4.4) says that the selected target vector does so
exactly.

Primary sources:

- H. L. Montgomery and R. C. Vaughan,
  [*The large sieve*](https://doi.org/10.1112/S0025579300004708),
  Mathematika 20 (1973), 119--134.
- H. L. Montgomery and R. C. Vaughan,
  [*Hilbert's inequality*](https://doi.org/10.1112/jlms/s2-8.1.73),
  J. London Math. Soc. 8 (1974), 73--82.

### Toeplitz and finite-section theory

The prime constituents have Toeplitz/translation structure and the sharp
matrix has low Loewner displacement rank.  This does not impose a positive
edge on the signed sum (3.4).  Classical finite-section spectral results
relate sections to the essential range of an appropriate fixed symbol; here
the symbol changes with `X` and the selected height, is signed, and is then
compressed by growing target-dependent constraints.  The hypotheses do not
produce a fixed positive fraction.  See S. Serra-Capizzano,
[*The spectral approximation of multiplication operators via asymptotic
(structured) linear algebra*](https://arxiv.org/abs/math/0512457).

### Explicit formula and positivity criteria

The Guinand--Weil formula is exactly what proves (4.2), but it gives equality,
not a positive collateral fraction.  Weil positivity for the full family of
tests is an RH criterion; importing it here would assume the desired result.
Primary references are A. P. Guinand,
[*Fourier reciprocities and the Riemann zeta-function*](https://doi.org/10.1112/plms/s2-51.6.401),
and A. Weil,
[*Sur les formules explicites de theorie des nombres*](https://doi.org/10.1070/IM1972v006n01ABEH001866).
The global Li/Weil reformulation in E. Bombieri and J. C. Lagarias,
[*Complements to Li's criterion for the Riemann hypothesis*](https://doi.org/10.1006/jnth.1999.2392),
also does not supply a strict candidate-local fraction.

### Zero-density and critical-line results

The newest large-value input of Guth--Maynard proves an upper zero-density
estimate

```text
N(sigma,T)<=T^(30(1-sigma)/13+o(1)).                (6.1)
```

It does not force even one collateral zero at the selected height, much less
its sign in (5.8): L. Guth and J. Maynard,
[*New large value estimates for Dirichlet polynomials*](https://doi.org/10.4007/annals.2026.203.2.6),
Annals of Mathematics 203 (2026), 623--675.

Likewise, results proving a positive global proportion of critical-line
zeros are averaged and their on-line compression is only subcarrier in the
present fixed-power normalization.  See K. Pratt, N. Robles, A. Zaharescu,
and D. Zeindler,
[*More than five-twelfths of the zeros of zeta are on the critical
line*](https://arxiv.org/abs/1802.10521).

No primary source found in this survey proves that an off-line zeta zero has
a distinct companion above `alpha*d-epsilon` for every fixed `epsilon>0`, or
proves a favorable candidate-relative compressed angle for such a companion.
No cited source claims a no-go stronger than the scoped isolation theorem
above.

## 7. Finite probe and what it says

The preceding sharp-Gabor scan had, at `alpha=.49`, absolute values roughly

| `T` | `K` | `Z` | `lambda_max(C)` |
|---:|---:|---:|---:|
| 64 | .45198 | .46102 | 1.09289 |
| 128 | .95085 | .52677 | 1.57176 |
| 256 | 1.49224 | .29845 | 1.79964 |
| 512 | 2.27884 | .49907 | 1.90967 |
| 1024 | 3.26421 | .39823 | 2.05645 |

This explains the declining normalized ratios: in the scan `K` grows while
the observed transverse quantities remain order one.  It is consistent with
the isolation reduction, but it proves no asymptotic statement.  Most
importantly, those scan points are not asserted zeros, so (4.2) cannot be
invoked there.

## 8. Research disposition

```text
exact actual-Lambda mixed coefficient (2.6):          PROVED;
exact projected Lambda(m)Lambda(n) expansion (3.3):   PROVED;
selected target contributes to Z or C:                FALSE exactly;
band shallow/on-line contribution reaches K:          FALSE;
full GA2 under an isolated actual candidate:           FALSE if (5.5);
GA2 forces deep collateral or open carrier term:       PROVED;
known large sieve/Toeplitz theorem gives (5.8):         NO;
known zero-density theorem forces a companion:         NO;
actual favorable deep-collateral orientation:          OPEN;
same-direction, same-phase GP transfer:                OPEN;
uniform zero-free strip:                               NOT PROVED.
```

The minimum honest successor theorem is therefore not merely
`Z=Omega(K)`.  It is:

> For every actual hypothetical first-strip zero, prove that the complete
> unselected divisor contains at least one zero above every fixed depth
> cutoff `alpha*d-epsilon`, and that the aggregate compression above that
> cutoff has either carrier-sized conditional Schur residual with a
> controlled lower transverse edge, or a carrier-sized positive transverse
> eigenvalue, after proving the open remainder is subcarrier; then prove GP
> for that same arithmetic-selected direction.

Without the companion/existence clause, the statement hides its main
arithmetic content.

Reproducibility:

```text
python3 src/test_same_packet_actual_lambda_transverse_gate.py
python3 results/verify_zeta23_same_packet_actual_lambda_transverse_gate.py
```

The checker uses actual prime powers and the actual pole/archimedean matrices
in the finite coefficient identity.  It verifies the finite algebra and
rank-one invisibility; the divisor deletion (4.2)--(4.4) is a symbolic
consequence of the explicit formula under the stated actual-zero hypothesis,
not a numerical zero test.  The checker does not insert a fake scan point
into the zeta divisor.
