# Uniform-strip goal, iteration II: four principal-mode audits and one exact theta formula

Date: 2026-08-12.

Status: **no unconditional fixed zero-free strip is proved here, and no
known zero-free region is improved.**  This report records the second goal
iteration after the conductor/Mertens/Wiener synthesis.  The purpose was to
attack routes not covered by the original reciprocal-hyperbola reduction:

1. a zero-aware von Mangoldt model;
2. growing-degree de la Vallee Poussin--Stechkin repulsion;
3. per-zero replication by universality;
4. the exact full-theta Hermite--Biehler kernel.

The first three again lose one distinguished mode.  The fourth does not
reduce to Mobius cancellation, and produced a new exact modular-orbit
formula, but its complete signed sum has not been proved positive.

## 1. Truth boundary

The target is the existence of one fixed `delta>0` such that

```text
zeta(rho)=0, 0<Re(rho)<1  =>  Re(rho)<=1-delta.       (1.1)
```

Every implication below was kept candidate-uniform in the ordinate.  A
finite scan, an almost-all statement, a logarithmic saving, or a theorem
after subtracting the candidate zero is not (1.1).

The first iteration had already reduced a Bergman detector to a complete
signed reciprocal-hyperbola main term and proved that a dyadic Mertens
high-pass has a stable inverse with no exponent gain.  Iteration II asked
whether a zero-aware model, arbitrarily high classical degree, recurrence,
or exact theta arithmetic avoids that endpoint.

## 2. Zero-aware Lambda models delete the candidate residue

For

```text
Z_(X,e)={rho: Re(rho)>=1-10e, |Im(rho)|<=X^1.1},
Lambda_tilde(n)=1-sum_(rho in Z_(X,e)) n^(rho-1),       (2.1)
```

where the zero sum counts multiplicity,

the exact Dirichlet series of the discrepancy is

```text
sum_n [Lambda(n)-Lambda_tilde(n)]n^(-s)
 =-zeta'/zeta(s)-zeta(s)
   +sum_(rho in Z_(X,e))zeta(s+1-rho).                 (2.2)
```

At every modeled zero the two residues in (2.2) cancel, including
multiplicity.  On the actual carrier `Q>=X^(8/9+e/9)`, a horizontally
unmodeled zero at depth `delta>10e` has resonant size

```text
<=X^[-(8/9+e/9)delta+o(1)]=o(X^(-8e)),                (2.3)
```

so it lies below the honest remainder.  A vertically unmodeled zero cannot
be resonantly tested because the model reaches height `X^1.1` while the
test only reaches `X`.

Thus the exact dichotomy is

```text
candidate large enough to matter     => included and canceled;
candidate omitted from the model     => below the stated remainder. (2.4)
```

This explains why the imported short-interval theorem can remain true in
the presence of a near-one zero: it proves distribution after projecting
out precisely that polar direction.  Zero density still permits one such
zero.  The model is a useful quotient, not a strip detector.

## 3. Growing-degree zero repulsion remains on the moving scale

Let

```text
P(theta)=a0+sum_(1<=k<=N)a_k cos(k theta)>=0.          (3.1)
```

If all `a_k>=0` for `k>=1`, normalize `a1>0` and put
`A=sum_(k>=1)a_k`.  Fourier positivity gives

```text
a0>=a1/2,             A>=a1.                         (3.2)
```

For a hypothetical zero `1-epsilon+iT`, the most optimistic target-only
logarithmic-derivative ledger contains

```text
a0[1/r-O(1)]+A[(1/2)log T-O(1)]
 -a1[1/(r+epsilon)+1/(1+r-epsilon)]-O(A/T^2).         (3.3)
```

The exact optimization proves the degree-uniform necessary condition

```text
epsilon log T<=3-2sqrt(2)+o(1).                      (3.4)
```

The constant is deliberately optimistic; the material point is the
`1/log T` scale.  Increasing `N=N(T)` only adds nonnegative `log k`
background.

Allowing signed Fourier coefficients can cancel the explicit Gamma sum,
but if `sum_(k>=1)a_k=0` then the negative coefficient mass is at least
`a1`.  The collateral zero aggregate at those harmonics is at least

```text
(a1/2)log T-O_epsilon(a1).                            (3.5)
```

Here (3.5) is in the viable fixed-gap range.

An arbitrary positive measure of Stechkin right shifts has the same
obstruction.  If its retained mass is `C`, global functional-pair
positivity forces its first shift moment to satisfy
`m_1<=C(1+2r)/2`; the fixed-gap target is then `O_epsilon(C)`, while
the Gamma background is `C[(1/2)log T-O(1)]`.
Taking `C` to zero cancels the target proportionally.  Exact radial Gamma
cancellation has zero vertical Poisson mass and is incompatible with a
nonzero globally one-sided pair kernel.

Hence growing harmonic or radial degree cannot produce (1.1) inside the
sign-safe class.  Leaving that class requires a new signed, target-conditioned
correlation of the actual zeta zeros at dilated ordinates.

## 4. Universality cannot replicate a zero without its winding mode

Suppose `rho0=beta+i gamma` is a zero and let a small disc around it lie in
the proposed strip.  If a shift `tau` satisfies full uniform recurrence of
`zeta(s+i tau)` to `zeta(s)` on the boundary, Rouche's theorem creates a
translated zero.  Guth--Maynard density then bounds the measure of such
shifts by

```text
T^[d_r+o(1)],       d_r=(30/13)(1-beta+r).            (4.1)
```

This is the desired replication mechanism in exact form.  Ordinary
universality cannot supply its premise: a compact carrying a closed contour
around a zero has nonzero winding, while the Euler-product approximants are
zero-free.

Cutting the contour restores a connected complement and positive-density
universality, but introduces a gap of length `ell`.  The exact winding-debt
dichotomy is

```text
slit recurrence
  => translated zero
     or sup_gap |(zeta_shift-zeta)'| >= constant/ell. (4.2)
```

Mean square gives only

```text
meas(slit event)<<T^[d_r+o(1)]+T ell^2.              (4.3)
```

For `beta>.99`, matching the density scale requires
`ell<=T^(-127/260+o(1))`; polynomial unwinding of such a gap costs degree
at least `T^(127/130-o(1))`, outside effective universality.

The same fact has a clean derivative form.  Recurrence of the `k`th
derivative determines the function only modulo a polynomial of degree
`k-1`.  At `k=1` the missing mode is exactly

```text
C_tau=zeta(rho0+i tau).                               (4.4)
```

Derivative universality recurs `zeta'` densely but deliberately allows a
large `C_tau`; imposing both derivative recurrence and small `C_tau` returns
to the sparse density event (4.1).  Thus per-zero replication loses one
principal winding constant rather than proving a strip.

## 5. Exact theta autocorrelation and the thin target

Put

```text
X(s)=xi(1/2+s),
Psi(v)=2 Phi(v/2),
K_(a,y)(q)=integral Psi((p+q)/2)Psi((p-q)/2)
                    sinh(ap)sinh(yp) dp.              (5.1)
```

Here `Phi` is the exact Rodgers--Tao theta kernel.  Direct expansion gives

```text
|X(a+y-it)|^2-|X(a-y-it)|^2
   =integral K_(a,y)(q)cos(tq)dq.                     (5.2)
```

The function in (5.1) is positive pointwise.  A fixed strip would follow
from positive definiteness, not pointwise positivity.

For exclusion alone there is a sharper target than full
Hermite--Biehler positivity.  If

```text
D_(a,y)(t):=|X(a+y-it)|^2-|X(a-y-it)|^2>0
for all t and 0<y<1/2-a,                              (5.3)
```

then every centered zero has horizontal displacement at most `a`: an
offending zero at `b+i gamma` makes

```text
D_(a,b-a)(-gamma)=-|X(2a-b+i gamma)|^2<=0.            (5.4)
```

Common shifted zeros and multiplicity do not escape the strict inequality.
Thus choosing

```text
a=0.499999                                             (5.5)
```

reduces the entire strip proof to `0<y<10^(-6)`.

## 6. Fully modular KL formula: exact, convergent, and signed

The theta product can be recompleted before differentiation.  With

```text
h(u)=e^u theta(e^(4u)),
T(p,q)=h((p+q)/2)h((p-q)/2),
L=[(d_p+d_q)^2-1][(d_p-d_q)^2-1],                    (6.1)
```

one has exactly

```text
Phi((p+q)/2)Phi((p-q)/2)=(1/256)L T(p,q).            (6.2)
```

After two-dimensional Poisson summation and a
Kontorovich--Lebedev transform, define

```text
lambda_t(k)=sum_(d|k)(d^2/k)^(it/2),
z_k(p)=2*pi*k*e^(2p),
B_t(z)=(z^2+9)K_(it/2)(z)+6z K'_(it/2)(z).           (6.3)
```

Define the Rodgers-scale autocorrelation, distinct from the centered
kernel in (5.1), by

```text
calK_(alpha,eta)(q)
 =integral_R Phi((p+q)/2)Phi((p-q)/2)
    sinh(alpha*p)sinh(eta*p) dp.
```

Then its exact transform is

```text
calKhat_(alpha,eta)(t)
 =1/2 sum_(k>=1)lambda_t(k)
    integral_0^infinity e^p sinh(alpha p)sinh(eta p)
      z_k(p)^2 B_t(z_k(p)) dp.                       (6.4)
```

The orbit integrals are absolutely summable, and the centered detector is

```text
D_(a,y)(t)=16 calKhat_(2a,2y)(2t).                   (6.5)
```

This is a new exact formula for the surviving thin-strip target.  It is not
a positive spectral factorization:

```text
lambda_t(2)=2cos((t/2)log 2),                         (6.6)
```

and already the `k=1` Bessel density changes sign.  The fully modular sum is
positive exactly when the desired detector is positive; individual orbits
are not.

An independent incomplete-gamma recompletion proves that every finite theta
block eventually has the wrong modulus-difference sign.  Its odd boundary
jets cancel only after the complete infinite modular sum.  Finally, the
thin-`y` Taylor expansion has relative parameter

```text
(y log|t|)^2.                                         (6.7)
```

For every fixed `y>0`, however small, this loses uniformity at sufficiently
large height; controlling it relatively requires the shifted-line lower
bound being sought.

The remaining theta theorem is therefore precise:

> Prove that the **complete signed sum** (6.4) is positive for
> `alpha=0.999998`, every real `t`, and `0<eta<2*10^(-6)`.

No finite modular truncation, orbitwise positivity, safe-line Schur
interpolation, or fixed Taylor order proves this statement.

## 7. Consolidated information signature

The four attacks lose different-looking but structurally analogous data.

```text
zero-aware Lambda model      candidate polar residue is projected out;
Stechkin/trig positivity     Gamma cancellation loses collateral-zero sign;
universality on a slit       derivative data lose the winding constant;
Bergman/spectral mollifier   transverse modes lose principal Mobius mode;
exact full theta             retains everything, but only as infinite signed compensation.
```

The first four are not independent opportunities to combine: each has
discarded the one mode on which a single offending zero is visible.  The
theta formula retains that mode and is therefore the only endpoint here not
already identified with a quotient/principal-mode loss.  Its positivity is
still unproved and is itself a fixed-strip-strength coefficient theorem.

## 8. Binary conclusion

```text
explicit fixed delta proved                         NO
known zero-free region improved                     NO
zero-aware model excludes modeled zero              NO -- exact residue cancellation
growing degree beats 1/log T                        NO
universality replicates one zeta zero               NO -- winding mode missing
thin target-only theta reduction                    YES
fully modular KL orbit formula                      YES
positive complete KL sum                            OPEN
```

Primary iteration-II artifacts:

- `ZETA23-ZERO-AWARE-LAMBDA-MODEL-TAUTOLOGY-GATE-2026-08-12.md`;
- `ZETA23-GROWING-DEGREE-STECHKIN-ZERO-REPULSION-GATE-2026-08-12.md`;
- `ZETA23-PER-ZERO-UNIVERSALITY-REPLICATION-PRINCIPAL-MODE-GATE-2026-08-12.md`;
- `ZETA23-SHIFTED-HERMITE-BIEHLER-THETA-AUTOCORRELATION-GATE-2026-08-12.md`;
- `ZETA23-FULL-THETA-KONTOROVICH-LEBEDEV-THIN-DISPLACEMENT-GATE-2026-08-12.md`.

This synthesis is a search-space contraction and an exact formula report,
not the requested strip proof.
