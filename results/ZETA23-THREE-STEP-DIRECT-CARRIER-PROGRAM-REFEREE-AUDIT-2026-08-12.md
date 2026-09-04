# Referee audit of the three-step direct-carrier program

Status: **PASS AFTER ONE SCOPE PATCH**, 2026-08-12.

Subsequent correction: the target-only extension left open by this audit was
settled negatively later the same day.  See
[`ZETA23-PHASE-FLIP-AND-SEPARATION-AVERAGE-REFEREE-ADDENDUM-2026-08-12.md`](ZETA23-PHASE-FLIP-AND-SEPARATION-AVERAGE-REFEREE-ADDENDUM-2026-08-12.md).

This audit covers:

1. `ZETA23-SUBFULL-DIRECT-Q-FAILFAST-AND-ARB-CERTIFICATE-2026-08-12.md`;
2. `ZETA23-SUBFULL-RITZ-LOEWNER-ADMISSION-GATE-2026-08-12.md`; and
3. `ZETA23-NEAR-TIE-GRAM-AND-MIRROR-ALIGNMENT-2026-08-12.md`; and
4. `ZETA23-THREE-STEP-SUBFULL-CARRIER-ITERATION-SYNTHESIS-2026-08-12.md`.

The principal formulas, finite computations, and stated negative results
survive hostile review.  One original Step 3 statement incorrectly inferred
an aggregate `o(kappa)` error from a merely polynomial number of collateral
pairs.  That inference has been removed and replaced by the necessary
explicit aggregate weak-block hypothesis.  No zero-free region or bound on
an actual zeta zero is proved or numerically improved.

The combined synthesis is faithful to the three source reports.  I patched
its Ritz display to state the `Delta=0` scalar case explicitly and restored
the free-space projection in its mirror identity; neither patch changes a
conclusion.

## 1. Disposition

| component | verdict | exact scope |
|---|---|---|
| adversarial direct-`q` scan | pass | floating Cartesian sample |
| Arb/Acb negative-dual interface | pass | rigorous specified finite matrix |
| closest full-carrier replay | pass | rigorous one fixed finite matrix |
| two-dimensional carrier Ritz formula | pass | exact finite-dimensional theorem |
| Lanczos moment reduction | pass | exact, but nonlinear in prime data |
| geometry-defined linear companions | pass | exact finite reduction; sign theorem open |
| normalized near-tie Gram/Hermite limit | pass | exact fixed-packet theorem |
| leading mirror-alignment identity | pass | exact after every represented positive row is imposed |
| weak-block transfer | pass after patch | requires explicit aggregate `o(kappa)` control |
| uniform arithmetic admission | open | no change |
| zero-side direct-`q` exclusion | open | no change |

## 2. Step 1: adversarial scan and interval certificate

### 2.1 Floating scan

I independently reran both parameter grids.  The broad boundary run gave

```text
valid arithmetic bases       1,121
valid conditioned points    61,896
negative values                  0
```

and reproduced the reported minimum

```text
T=16, gamma/T=1.31, phi=0.49, aperture=0.32,
m=1, alpha=0.499,
q_kappa=0.004319753120252432,
q_kappa/kappa=0.02576213669350678.
```

The focused run independently reproduced

```text
valid bases       275
valid slices   11,565
skipped slices    810
negative values     0
```

and the three displayed minima at `theta=0.9,0.99,1`, including their dual
multipliers.  These counts are deterministic consequences of the listed
Cartesian grids.  They provide no coverage between grid points.

### 2.2 Phase and endpoint geometry

For

```text
tau_k=gamma+2*pi*(k+phi)/L,
```

sign conjugation leaves the numerator

```text
2 sin(-i*alpha*L/2-pi*phi).
```

The implementation uses this factor.  At `phi=0` it agrees with the earlier
centered fixture.  The exact endpoint kernel formed from `k^r` is the same
kernel as that formed from shifted/scaled polynomial moments: translation,
scaling, and the Legendre change of basis are invertible triangular changes
within degrees below `m`.

### 2.3 Interval arithmetic

The proof path does not promote a floating nullspace.  It uses a rational
RREF basis for the endpoint kernel and an Arb pivot separated from zero to
eliminate the selected positive row.  In the resulting nonorthonormal basis,

```text
G=B^*B,
K=B^* K_ar B,
N=(2/L^2)(B^*y)(B^*y)^*.
```

The interval basis contains the actual selected-null basis.  Dependency
inflation can make the test fail, but cannot create a false successful
certificate.

The archimedean tail enclosure is valid.  For rates separated by two, the
omitted terms are bounded using

```text
sum exp(-rL)/|r-itau|
 <=exp(-r_N L)/(r_N*(1-exp(-2L))),

sum exp(-rL)/|r-itau|^2
 <=exp(-r_N L)/(r_N^2*(1-exp(-2L))).
```

The off-diagonal digamma divided differences and diagonal polygamma formula
then enclose the same matrix used by the floating scout.  A midpoint replay
matches the floating generalized forms to twelve displayed decimal places.
The prime component contains every prime power `n<=T` with coefficient
`log(p)/sqrt(n)`; the pole component is evaluated independently in rank-two
form.

### 2.4 Certificate direction

For rational `mu>=0`, strict interval positivity of

```text
(mu*theta*kappa-delta)G-K-mu*N
```

is in exactly the required direction:

```text
K_ar+mu*N <= (mu*theta*kappa-delta)I
```

and hence the scalar dual gives

```text
q_(theta*kappa)(K_ar) <= -delta.
```

The no-pivot interval `LDL*` test is sufficient, not necessary.  A failed
pivot makes no claim.  The unshifted false calibration is rejected, while
the explicitly labeled `K_ar-I` calibration succeeds.

For `theta=1`, the rank-one carrier forces the generalized direction
`G^(-1)B^*y`.  Its interval Rayleigh quotient rigorously gives

```text
q_kappa =
[0.004319753120250996038800722197058190834782 +/- 2.59e-43] > 0.
```

This is a genuine finite theorem.  By nested feasible sets it also proves
`q_(theta*kappa)>0` for every `theta<=1` at this exact matrix, but it gives no
neighboring-parameter or uniform conclusion.

## 3. Step 2: two-dimensional Ritz/Loewner gate

Let

```text
N=kappa*a*a^*,
K=[[r,b^*],[b,D]],
d=<w,Dw>, c=|<w,b>|, w perpendicular a.
```

Every unit vector in `span{a,w}` with carrier mass `x` has optimized
Rayleigh value

```text
F(x)=x*r+(1-x)*d+2*c*sqrt(x*(1-x)).
```

The function is concave.  The top eigenvalue of `[[r,c],[c,d]]` is

```text
lambda_+=(r+d+sqrt((r-d)^2+4c^2))/2,
```

and its carrier mass is

```text
p_+=(1+(r-d)/sqrt((r-d)^2+4c^2))/2.
```

Therefore the reported branch is exact: use `lambda_+` when
`p_+>=theta`, and otherwise use `F(theta)`.  The scalar-block degeneration
and the endpoint cases are handled correctly.  A dense angular replay over
random blocks agrees with the closed formula.

After shifting both diagonal entries by `epsilon*kappa`, the determinant
alternative when both shifted diagonals are negative and the boundary
alternative when the top eigenvector has insufficient carrier are also in
the correct directions.  The displayed negative-part orientation card is a
stronger sufficient condition, not an asserted equivalence.

For the first Lanczos vector,

```text
m_j=<a,K^j a>,
sigma^2=m_2-m_1^2,
r=m_1,
c=sigma,
d=(m_3-2*m_1*m_2+m_1^3)/sigma^2.
```

Direct expansion verifies all identities.  The report correctly bills the
arithmetic cost: because `K` is linear in the completed prime data, `m_2`
and `m_3` introduce quadratic and cubic correlations.  In contrast, a
background- or geometry-defined companion is independent of the primes, so
its three matrix entries are linear completed scalars.  Taking the modulus
of the cross entry does not alter that provenance statement.

The four actual-coefficient tables reproduce.  One Lanczos step captures
between `97.87%` and `99.32%` of the observed `theta=0.9` finite edge, while
the prime-independent geometric three-space captures between `70.96%` and
`87.05%`.  All values are floating, all sampled carrier diagonals are already
positive, and none tests the desired negative-diagonal cross-compensation
case.

Finally, separate KMT-size estimates for the three linear entries remain at

```text
sqrt(X)/L^(13/10)
```

against carrier `X^alpha/L`; their ratio diverges for fixed `alpha<1/2`.
The scalar negative matrix countermodel correctly shows that Loewner
displacement rank alone cannot supply the missing orientation.  It is an
information-level countermodel, not actual von Mangoldt data.

## 4. Step 3: near ties and mirror alignment

### 4.1 Gram and confluent limit

The proposed difference-only correlation formula needed correction.  For
normalized packet rows, direct integration gives

```text
rho=M(alpha_0+alpha_1+i*(gamma_1-gamma_0))
    /sqrt(M(2*alpha_0)M(2*alpha_1)).
```

Thus the mean depth is genuine data.  Expanding `log M` at
`2*alpha_bar` gives

```text
det G=Var_(2*alpha_bar)(t)
      *(Delta alpha^2+Delta gamma^2)+O(|Delta|^4).
```

The orthogonalized divided difference converges to the centered Hermite row.
For the four reflected branches at a collision with depth bounded away from
zero, the limiting confluent family is

```text
A, tA, B, tB,
```

with distinct exponential rates.  It is linearly independent.  Hence two
singular values stay of constant size and two are comparable to `|Delta|`
on the stated compact parameter sets.  The numerical tests correctly retain
the missing `|Delta|` factor rather than normalizing it away.

### 4.2 Leading mirror identity

For positive cross weights and leading packet rows,

```text
K_cross=sum_j c_j(U_j V_j^*+V_j U_j^*), c_j>0.
```

Imposing every corresponding positive row gives

```text
U_j(ell)+V_j(r)=0,
```

so direct substitution yields

```text
Re <ell,P_F K_cross r>
 =-sum_j c_j |V_j(r)|^2.
```

This identity is exact and independent of transverse Gram angles.  The
same-lobe block of a genuine pair is smaller than the separated-packet cross
carrier by `O(exp(-alpha D))`, and the reverse cross block by
`O(exp(-2alpha D))`.  This excludes the earlier abstract transverse block
at carrier scale in the stated fixed-width separated-packet class after all
its positive rows are imposed.

### 4.3 Required patch

The first draft said that a fixed or polynomial number of pairs plus
subpower conditioning automatically preserves the leading sign.  That was
too weak: an unrestricted polynomial multiplicity or total weight can
consume a fixed-power block saving.

The final report now introduces the aggregate weak contribution `E_weak`
and explicitly assumes

```text
||E_weak||=o(kappa)
```

on the normalized states, together with retained seed carrier.  It also
states a sufficient weighted-scale condition and puts unrestricted aggregate
multiplicity outside the theorem.  With this patch, the transfer claim is
valid.

The restriction remains substantial.  The exact sign theorem imposes every
collateral positive row represented in the cross sum, whereas the direct
arithmetic quotient imposes only the selected target row.  It also treats
fixed-width separated packets, not the full proportional-width carrier
space, and says nothing directly about the prime/pole/gamma operator.

## 5. Mechanical verification

The combined command

```bash
PYTHONPATH=src python3 -m pytest -q \
  src/test_carrier_slice_support.py \
  src/test_carrier_ritz_loewner_gate.py \
  src/test_subfull_direct_q_failfast.py \
  src/test_near_tie_packet_gram.py
```

returns

```text
22 passed
```

The tests check the scalar carrier dual, the exact two-dimensional branch,
Lanczos identities, finite Ritz lower bounds, rational endpoint kernels,
floating/interval agreement, successful and rejected interval certificates,
mean-depth dependence, collision asymptotics, Hermite convergence, the
four-branch small singular values, the mirror identity, and the packet block
scales.

## 6. Final mathematical assessment

This iteration made three material internal advances:

1. the direct arithmetic edge now has a broad adversarial scout and a valid
   proof-producing finite negative-certificate interface;
2. arithmetic admission has an exact low-dimensional orientation target
   which is strictly weaker than the full-carrier scalar, although no known
   prime estimate proves it; and
3. a tempting near-tie reservoir is excluded in one normalized packet class,
   with the determinant and aggregate-error bookkeeping corrected.

It did **not** prove uniform arithmetic admission, prove that an actual
off-line zero forces a negative edge, control the target-only collateral
geometry, or improve a classical zero-free bound.  The surviving research
question is now narrower: prove a joint completed-prime orientation inequality
for a prime-independent Ritz companion and extend mirror alignment to the
actual target-only, carrier-retaining states—or produce a legal normalized
counterexample in that larger space.  The subsequent phase-flip report
produces the latter: two slightly shallower reciprocal-separation pairs screen
a strictly deepest target.  The surviving divisor alternatives are therefore
finite-list/coherent separation with all arithmetic cross terms retained or
new zeta-specific local spacing/depth input, not a universal target-only
mirror theorem.
