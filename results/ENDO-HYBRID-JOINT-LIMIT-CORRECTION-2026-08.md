# Correction of the phase coupling in Endo's hybrid joint limit

Status: internal erratum and proof audit, 2026-08-04.  This note concerns
version 1 of Kenta Endo's preprint [*Limit theorem for the hybrid joint
universality theorem on zeta and L-functions*](https://arxiv.org/abs/2410.17575).
As of the audit date, arXiv lists only that version.  This note is not an
external erratum issued by the author.  The exact joint law in
Theorems 1.2(i) and 2.1(i) needs a coordinate inversion.  The marginal law,
product-support conclusion, and qualitative hybrid-universality corollaries
survive.  A separate compact-open estimate in Lemma 5.1 also needs the local
repair given in Section 5 below.

## 1. The mismatch

Write

```text
x_p(tau)=p^(i tau).
```

For a smoothed Dirichlet polynomial,

```text
phi_X(s+i tau)
 = sum_n a_phi(n) lambda(n/X) n^(-s)
     product_(p|n) x_p(tau)^(-nu_p(n)).             (1)
```

Thus Kronecker--Weyl equidistribution of the coordinates `x_p(tau)` sends
the pair in (1) to

```text
(phi_X(s,conjugate(omega)), omega_P),               (2)
```

not to `(phi_X(s,omega),omega_P)`.  This is not a convention that Haar
invariance can erase: inversion preserves either marginal, but it changes
their joint correlation.

The proof itself displays the source of the problem.  In Section 4, the
finite-dimensional map has the exponent

```text
product_(p|n) omega(p)^(-nu_p(n)),                  (3)
```

but the last equality in the Mapping Theorem step identifies its Haar
pushforward with the random polynomial having positive powers of `omega`
*and the same finite coordinates*.  That equality is false.

## 2. A decisive one-prime witness

Let `p` be one of the recorded primes.  Haar orthogonality applied to the
finite polynomial gives

```text
E[omega(p) phi_X(s,conjugate(omega))]
   = a_phi(p) lambda(p/X) p^(-s),                   (4)

E[omega(p) phi_X(s,omega)] = 0.                    (5)
```

For zeta, the right side of (4) tends to `p^(-s)`.  For a Dirichlet
L-function it tends to `chi(p)p^(-s)` whenever `p` does not divide the
conductor.  Only the random vertical phase is conjugated; `chi(p)` is not.

The translate side has the matching identity

```text
lim_(T->infinity) 1/T integral_0^T
    p^(i tau) phi_X(s+i tau) d tau
 = a_phi(p) lambda(p/X) p^(-s).                    (6)
```

The mean approximation used in the preprint passes (6) from `phi_X` to
`phi` at an interior point where the mean square is finite.  Consequently,
for zeta and Dirichlet L-functions the claimed and corrected infinite laws
are also separated by this integrable moment.  If a bounded continuous
witness is desired, use, for sufficiently small nonzero `u`,

```text
F_u(f,x)=exp(i u Re(conjugate(chi(p)) x_p f_chi(sigma))). (7)
```

Its expectation is differentiable at `u=0`; the derivatives under the two
candidate laws differ by `i p^(-sigma)`.  For zeta, omit `chi(p)`.

## 3. Corrected theorem

Let `P` be the finite set of recorded primes and let `omega` have product
Haar law.  Define coordinatewise conjugation by
`conjugate(omega)(p)=conjugate(omega(p))`.  Under the hypotheses of Endo's
Theorem 2.1, the corrected convergence is

```text
((phi_j(.+i tau))_j, (p^(i tau))_(p in P))
  => ((phi_j(.;conjugate(omega)))_j, omega_P).       (8)
```

Equivalently, after the Haar-preserving substitution
`u=conjugate(omega)`, it is

```text
((phi_j(.+i tau))_j, (p^(i tau))_(p in P))
  => ((phi_j(.;u))_j, conjugate(u_P)).               (9)
```

Form (9) is the least invasive correction to the preprint: retain every
empirical phase `p^(i tau)` and redefine the proposed limiting measure as
the law of

```text
((phi_j(s,omega))_j, conjugate(omega_P)).            (10)
```

For Dirichlet characters this reads

```text
((L(.+i tau,chi_j))_j, (p^(i tau))_(p in P))
  => ((L(.,chi_j;omega))_j, conjugate(omega_P)).     (11)
```

An equivalent alternative is to record `p^(-i tau)` everywhere.  Then the
original same-phase random law is correct, but every empirical phase
condition and the finite map have to be changed consistently.  Changing
only the exponent in (3) does not fix the proof.

## 4. Proof repair

The bounded-Lipschitz triangle argument needs only the following edits.

1. In the definition of the limiting measure before Theorems 1.2 and 2.1,
   replace `omega_P` by `conjugate(omega_P)` and leave the random Euler
   product unchanged.

2. In the decomposition into `Sigma_1`, `Sigma_2`, and `Sigma_3`, use
   `(phi(s,omega),conjugate(omega_P))` and its smoothed version on the random
   side.

3. Keep the inverse exponent in the finite map (3).  Its Haar pushforward
   is (2), which equals the law of
   `(phi_X(s,omega),conjugate(omega_P))` after the substitution
   `omega -> conjugate(omega)`.

4. The random approximation proposition applies unchanged, because Haar
   inversion is measure preserving.  It sends the corrected smoothed law
   to the corrected full law as `X->infinity`.

No coefficient, Euler parameter, or Dirichlet character is conjugated.

## 5. Independent compact-open repair

The density proof in Lemma 5.1 estimates the higher Euler terms by

```text
m_phi sum_(p>X) sum_(k>=2) 1/(k p^(k sigma_phi)).    (12)
```

When `sigma_phi=1/2`, the `k=2` part of (12) diverges.  The proof does not
need a supremum on the whole open strip; its Frechet topology is uniform
convergence on compact subsets.

For an exhaustion compact `K_(ell,phi)`, put

```text
sigma_(ell,phi)=min_(s in K_(ell,phi)) Re(s)>sigma_phi.
```

If `h_X` denotes the sum of the `k>=2` terms, then uniformly in all tail
phases,

```text
sup_(s in K_(ell,phi)) |h_X(s)|
 <= m_phi sum_(p>X) sum_(k>=2)
        1/(k p^(k sigma_(ell,phi))) -> 0.            (13)
```

Indeed `2 sigma_(ell,phi)>1`.  Hence, for the compact-open metric in the
paper,

```text
sup_w d_phi(h_X(.,w),0)
 <= sum_(ell>=1) 2^(-ell)
      min(1, m_phi sum_(p>X) sum_(k>=2)
                     1/(k p^(k sigma_(ell,phi))))
 -> 0                                                       (14)
```

by dominated convergence.  Replace the global norm in Lemma 5.1 by (14).
The remainder of its density step can be written without the `X`/`X_0`
index collision as follows:

1. Choose `X_0>max P` so that the sum of the metric tails (14) is small.
2. Prescribe `c(p)=z(p)` for `p in P` and, say, `c(p)=1` for the other
   primes `p<=X_0`.
3. Apply the theorem's joint density hypothesis to the targets

   ```text
   f_j-sum_(p<=X_0) log phi_(j,p)(s,c(p))
   ```

   and choose the common phases `c(p)` for `p>X_0`.
4. Add the uniformly compact-open-convergent higher-order tail (14).

This proves the intended density statement also at the important boundary
value `sigma_phi=1/2`.  It simultaneously removes the displayed coefficient
subscript typo `a_(phi_(j,r))` and makes every occurrence of the cutoff use
`X_0` consistently.

## 6. Support and corollaries

Let `nu_plus` be the same-phase law printed in version 1 and define

```text
C(f,z)=(f,conjugate(z)).
```

The corrected law is `C_* nu_plus`.  Since `C` is an involutive
homeomorphism,

```text
supp(C_* nu_plus)=C(supp(nu_plus)).                 (15)
```

After the compact-open repair in Section 5, the product support is therefore
still

```text
product_j H_0(D_(phi_j)) x T^P.                    (16)
```

In the final support proof, this can be implemented by replacing the map
`((f_j),z) -> ((exp(f_j)),z)` with
`((f_j),z) -> ((exp(f_j)),conjugate(z))`.

The qualitative hybrid-universality corollaries are unchanged.  The
empirical coordinate is still `p^(i tau)`, the torus support is still full,
and arbitrary target phases remain arbitrary.  Marginal value-distribution
statements are also unchanged.

Exact conditional laws do change.  For a positive-measure phase box `B`
whose boundary has Haar measure zero, the corrected conditional function
law is

```text
Law(phi(s,conjugate(omega)) | omega_P in B)
 = Law(phi(s,u) | u_P in conjugate(B)).             (17)
```

Boxes made of arcs centered at `1` are conjugation invariant.  Therefore
the conditioned Bagchi-tail calculation in this repository is unchanged:
after deleting a fixed initial Euler block, the remaining coordinates are
still independent Haar variables and the random tail is still zero-free.

## 7. Edit ledger for version 1

The minimal paper-level patch is:

- page 3: redefine the Dirichlet-L limiting measure with finite coordinate
  `conjugate(omega_P)`;
- page 4: make the same change for the general limiting measure;
- pages 15--16: use that corrected target in the three-term weak-convergence
  comparison and fix the final Mapping Theorem equality;
- pages 20--22: use the compact-open estimate (13)--(14), clean the cutoff
  indices, and conjugate the finite coordinate in the final exponential
  support map.

Theorems 1.2(ii) and 2.1(ii), and Corollaries 1.3, 2.2, and 2.3, retain their
stated conclusions.  Additional clerical corrections found in the audit are:

- page 5: “Theorem 1.2 is a special case of Theorem 1.1” should refer to
  Theorem 2.1;
- page 22: `U_(p_(k_n))` should be `V_(p_(k_n))`, and `V_(k_n)` should be
  `V_(p_(k_n))`;
- page 23: the function maximum should run over `1<=j<=r`, not `1<=j<=n`.

## 8. Research impact

This fixes the exact coupling, not an RH obstruction.  It validates the
qualitative hybrid-universality bridge after correction, while preserving
the fixed-cutoff zero-free-support no-go.  In particular, neither Haar
inversion nor the compact-open repair supplies the growing-cutoff,
zero-bearing conditional recurrence estimate that the RH program would
need.
