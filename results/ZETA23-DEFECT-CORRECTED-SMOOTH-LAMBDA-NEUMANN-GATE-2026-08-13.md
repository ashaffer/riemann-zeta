# Defect-corrected smooth-prime quadrature: Neumann and high-tail gate

**Date:** 2026-08-13

**Candidate:** with a natural von-Mangoldt sampling map `Q`, a low-pass
reconstructor `R`, and `A=R(I-Q)`, form

```text
f_r=sum_(0<=j<r) A^j phi,             lambda=Q f_r.   (0.1)
```

**Verdict:** the Neumann algebra is exact after one corrects the operator
types, but neither required analytic estimate is presently available.
Writing `S=RQ` on the range of `R` and `A=I-S`, one has

```text
S f_r=phi-A^r phi.                                    (0.2)
```

Thus a genuine cyclic contraction for `A` would amplify a subpower defect.
The Vinogradov--Korobov estimate supplies only a bound for the first defect
of a fixed smooth profile.  It does not supply an operator contraction.  In
the natural infinite-dimensional bandlimited space the obstruction is
exact: `Q` is finite sampling, so there are nonzero bandlimited functions
vanishing at every active prime node; for them `Af=f`.  Hence

```text
||A||>=1.                                             (0.3)
```

Restricting to a finite or cyclic subspace replaces (0.3) by a lower-frame
or Schur-margin problem for the prime samples, which is the existing H1
gate.

The requested theorem-grade pointwise high-tail bound is also absent.  For
a fixed smooth shell weight `f`, the available imported estimate gives,
uniformly throughout and far beyond
`Y^.751<=|t|<=Y^(50/33)`,

```text
sum_n Lambda(n)/n f(log(n/Y)) n^(it)
 << N_1(f){(log Y)^(-3/10)+(1+|t|)^(-1)},             (0.4)
```

where `N_1` is a first-order smooth-weight seminorm.  This is a logarithmic,
not fixed-power, saving.  Fourier decomposition of the iterated weight does
not create Vaughan curvature: every Type-II mode still has the exactly
separable phase

```text
(mn)^(i(t+s))=m^(i(t+s))n^(i(t+s)).                   (0.5)
```

An arbitrary-coefficient exponent-pair estimate is therefore false, and a
coefficient-specific fixed-power theorem is strip-strength under the usual
interval/weight uniformity.

There is also zero spectral margin in the literal proposal.  If `R` passes
frequencies through `T_0=Y^.751` and the stop band starts at `T_0`, a Fourier
component of `f_r` at `-T_0` is shifted by the twist `t=T_0` to the untwisted
prime mass.  A guard band is mandatory; it does not repair (0.3)--(0.5).

No zero-free strip is claimed.

---

## 1. Correct operator algebra

Let `X=range(R)` be the reconstructed low-pass space and suppose first that
`R^2=R`.  The continuous identity and the discrete sampling map have
different codomains, so the literal expression `R(I-Q)` means

```text
S=RQ:X->X,
A=I_X-S.                                               (1.1)
```

Assume `phi in X` and put

```text
f_r=sum_(j=0)^(r-1) A^j phi.                          (1.2)
```

### Lemma 1.1 (Neumann telescoping)

One has exactly

```text
RQ f_r=(I-A)f_r=phi-A^r phi.                          (1.3)
```

#### Proof

This is the finite geometric identity

```text
(I-A)sum_(j<r)A^j=I-A^r.                              (1.4)
```

QED

Consequently the Fourier transform of `lambda=Qf_r`, after application of
the low-pass reconstruction, has error `A^r phi`.  The statement is only
on the pass band where `R` is the identity.  It gives no identity for the
unreconstructed high tail `(I-R)Qf_r`.

If a norm and a number `theta_Y<1` satisfied the **cyclic** estimate

```text
||A^j phi||<=theta_Y^j||phi||          for every j,   (1.5)
```

then (1.3) would indeed amplify the saving.  For example, if

```text
theta_Y=exp[-c(log Y)^alpha],                          (1.6)
```

then a fixed target `Y^(-eta)` would require only

```text
r>=(eta/c)(log Y)^(1-alpha).                          (1.7)
```

This exponent ledger is sound.  The missing statement is (1.5), not the
geometric-series algebra.

---

## 2. A scalar PNT defect does not iterate

A Vinogradov--Korobov PNT estimate can show schematically, for a fixed
profile and a suitable low reconstruction,

```text
||A phi||<=theta_Y C(phi),             theta_Y=Y^(-o(1)).
                                                               (2.1)
```

It gives neither `||A||<=theta_Y` nor
`||A^j phi||<=theta_Y^j C(phi)`.  After the first application, `Aphi` is a
smoothed prime discrepancy rather than another fixed smooth test.  The next
application contains the kernel `QRQ`; further iterations contain

```text
QRQ, QRQRQ, ...                                         (2.2)
```

and therefore multi-prime sampling correlations.  Applying the same
one-function PNT estimate independently at every stage is not legitimate.

There is an exact operator obstruction in the natural low-pass space.

### Theorem 2.1 (finite-sampling eigenvalue one)

Let `R` be the Fourier projection onto a nonempty frequency interval and
let `X=range(R)` in a Paley--Wiener `L2` space.  Suppose `Qf` depends only on
the values of `f` at the `M` active prime-log nodes.  Then

```text
ker(Q|X) is nonzero,                                  (2.3)
```

and every `f` in this kernel satisfies

```text
Af=f.                                                 (2.4)
```

In particular the spectral radius and operator norm of `A` are at least
one in every Hilbert norm for which `R` is orthogonal.

#### Proof

The bandlimited space `X` is infinite-dimensional, while evaluation at the
`M` nodes has rank at most `M`.  Thus it has a nonzero kernel.  For such an
`f`, `RQf=0`, and (1.1) gives (2.4).  QED

One can see (2.3) constructively: choose a smooth Fourier transform in the
pass band from the infinite-dimensional nullspace of the `M` evaluation
functionals.  Equivalently, finite interpolation zeros do not consume the
whole Paley--Wiener space.

This theorem does not prove that the particular cyclic vector `phi` has a
component in the bad kernel.  It proves that (2.1) cannot be promoted to the
operator contraction needed for a black-box Neumann argument.  If one
restricts `X` to a finite-dimensional subspace on which `Q` is injective,
then (1.5) asks for a quantitative lower sampling-frame bound.  In matrix
form it is the same prime-node Gram/Christoffel--Schur margin already left
open by H1.

The carrier-specific version can also be stated exactly.  Suppose, in the
most favorable normalization, that `S=RQ` is self-adjoint with spectrum in
`[0,1]`.  If `mu_phi` is the spectral measure of `phi`, then

```text
||A^r phi||^2=integral_[0,1] (1-lambda)^(2r)dmu_phi(lambda),
                                                               (2.5)

f_r=g_r(S)phi,
g_r(lambda)=[1-(1-lambda)^r]/lambda.                  (2.6)
```

At `lambda=0`, the last expression is understood by continuity as `r`.

The first-defect estimate controls only the same integral with `r=1`.  It
does not exponentiate.  An exact two-eigenvalue countermodel is

```text
phi=sqrt(1-theta^2)e_1+theta e_0,
S e_1=e_1,                    S e_0=0.                (2.7)
```

Then `||Aphi||=theta`, but `||A^r phi||=theta` for every `r>=1`.
Near-zero rather than zero eigenvalues give the same obstruction on the
polylogarithmic iteration scale.  Indeed,

```text
g_r(lambda) asyp min(r,1/lambda),                     (2.8)
```

so the attempted inverse amplifies precisely the poorly sampled modes.
Proving that `mu_phi` has negligible mass there is the carrier-specific
Schur/source condition; it is not a consequence of a one-step VK bound.
In particular, monotone convergence in (2.5) gives

```text
lim_(r->infinity)||A^r phi||^2=mu_phi({0})
 =||projection_(ker S) phi||^2.                       (2.9)
```

This is the irreducible distance from the carrier to the span of the
reconstructed prime sampling kernels.  Asking that it vanish with a
quantitative rate is exactly the carrier-relative range/Christoffel
problem, now written as a Neumann limit.

There is also a support incompatibility.  An exact nontrivial Fourier
low-pass sends a compactly supported shell profile to an entire function
which is not compactly supported.  If `Q` is kept finite by reapplying a
hard shell cutoff, that multiplication recreates high Fourier leakage and
adds a commutator to (1.3).  If the cutoff is not reapplied, `Q` is no longer
the finite active-shell map.  A rigorous version must choose one of these
and account for the resulting error.

---

## 3. The actual theorem-grade high-twist bound

The principal-character specialization of Klurman--Mangerel--Teravainen,
Lemma 7.9 and Remark 7.2, gives

```text
sum_(n<=x) Lambda(n)n^(it)
 << x/(log x)^(3/10)+x/(1+|t|)                       (3.1)
```

after optimizing their auxiliary epsilon, uniformly for

```text
|t|<=x^[(log x)^(1/25)].                              (3.2)
```

The exact source statement and Abel-summation specialization are recorded
in `publication/IMPORTED-ANALYTIC-BASELINE.md` and
`ZETA23-SCALAR-PRIME-POLYNOMIAL-FIXED-SAVING-AUDIT-2026-08-11.md`.

Let `f` be supported in a fixed logarithmic shell and set

```text
N_1(f)=||f||_infinity+integral |f'(u)|du.             (3.3)
```

Partial summation in (3.1), using `n asyp Y`, gives uniformly in the full
target aperture

```text
|sum_n Lambda(n)/n f(log(n/Y)) n^(it)|
 <<N_1(f)[(log Y)^(-3/10)+(1+|t|)^(-1)].             (3.4)
```

Harmless fixed support and endpoint constants are suppressed.  A fixed
smooth endpoint can improve the explicit `t`-decay term, but not the
logarithmic main term.  Thus the currently imported pointwise theorem has
saving

```text
Y^(-o(1)),                                            (3.5)
```

not `Y^(-eta)` for any fixed `eta>0`.

The dependence on `N_1(f)` matters for the iterate.  If `R` allows
frequency `T_0`, Bernstein's inequality permits

```text
N_1(f_r)<<T_0 ||f_r||                                 (3.6)
```

in a standard sup-norm ledger.  With `T_0=Y^.751`, (3.4) is then worse than
trivial even if `||f_r||` stays bounded.  A proof based instead on a
controlled Fourier `l1` norm can avoid this particular derivative loss,
but it still retains only the logarithmic saving (3.5).

---

## 4. Smooth iteration does not repair the Vaughan Type-II phase

Partition a Vaughan or Heath--Brown decomposition into smooth dyadic
rectangles `m asyp M`, `n asyp N`, `MN asyp Y`.  Fourier inversion in the
log-product variable writes

```text
f_r(log(mn/Y))
 =integral fhat_r(s) (mn/Y)^(is) ds.                 (4.1)
```

For each `s`, the height phase is exactly

```text
(mn)^(it)(mn/Y)^(is)
 =Y^(-is)m^[i(t+s)]n^[i(t+s)].                        (4.2)
```

Hence every Type-II rectangle is a superposition of rank-one separated
phases.  With coefficient-blind bounds, the legal choices

```text
a_m=m^[-i(t+s)],       b_n=n^[-i(t+s)]                (4.3)
```

saturate the trivial estimate.  Smoothness of `f_r` changes the superposed
parameter `s`; it creates no mixed derivative in `(m,n)`.

The actual Vaughan coefficients are not arbitrary, so (4.3) is not a
logical impossibility theorem for a coefficient-specific proof.  It shows
that a standard exponent-pair/large-sieve transfer does not provide the
requested power.  Exploiting the Möbius--von-Mangoldt coefficients at that
strength is exactly the missing prime cancellation.

Termwise expansion of (0.1) does not help.  The fixed component `phi` alone
has only (3.4), while the remaining terms were designed to cancel it after
application of `R`.  Bounding the terms separately discards that designed
cancellation; retaining it is the original inverse/Schur problem.

---

## 5. The literal passband has zero guard margin

Suppose for illustration that `f_r` is bandlimited in the logarithmic
variable:

```text
supp(fhat_r) subset [-T_0,T_0].                       (5.1)
```

Writing the prime sampling transform schematically as `K_Y`, Fourier
inversion gives

```text
widehat(Qf_r)(t)
 =integral_(-T_0)^T_0 fhat_r(s) K_Y(t+s)ds.           (5.2)
```

At the first stop-band point `t=T_0`, the endpoint `s=-T_0` samples
`K_Y(0)`, the order-one untwisted prime mass.  Therefore a passband ending
at `Y^.751` and a high tail beginning at the same height have no spectral
margin.  One needs, for example, support inside `(1-delta)T_0`, a rolloff
estimate for `fhat_r`, or a separate overlap correction.

This issue is repairable by sacrificing part of the already proved band.
It is not the principal obstruction: with a fixed guard band, (3.4) remains
subpower and Theorem 2.1 remains unchanged.

---

## 6. Why the missing power is strip-strength

There is a direct Mellin explanation for the loss of Type-II curvature.
For

```text
F(z)=integral_R f(u)exp(zu)du,                         (6.1)
```

Mellin inversion gives, initially on a right line,

```text
sum_n Lambda(n)/n f(log(n/Y))exp[i t log(n/Y)]
 =1/(2 pi i) integral F(z)Y^(z-it)
                  [-zeta'/zeta](1+z-it) dz.          (6.2)
```

If `rho=beta+i gamma` is a zeta zero, choose `t=-gamma` (or conjugate the
twist).  The logarithmic derivative then has a pole at the **real** point

```text
z=beta-1,                                             (6.3)
```

whose residue in (6.2) has modulus

```text
|F(beta-1)|Y^(beta-1).                                (6.4)
```

For a fixed nonzero nonnegative profile, `F(beta-1)>0`.  Thus a zero at the
target height exactly demodulates into a nonoscillatory power term.  A
pointwise residue can interact with neighboring-zero residues, so (6.4)
alone is not asserted as a one-weight converse.  It shows why a theorem
uniform over the usual local-height and bump family is a zero-detection
theorem rather than a routine phase estimate.

A hypothetical theorem of the standard smooth Vaughan form

```text
|sum_n Lambda(n) W(n/Y)n^(it)|
 <=C(W)Y^(1-eta)                                      (6.5)
```

with fixed `eta>0`, uniformly for all weights in a translation/dilation
stable bump class and for the required moving interval of `t`, would give
the corresponding power estimate for prime intervals after smooth
partition and removal of prime powers.  With the interval and local-height
uniformity used in Turan's criterion, the numerical audit already in
`ZETA23-PRIME-GAP-VORONOI-ANTENNA-AND-HIGH-TAIL-STRIP-GATE-2026-08-13.md`
shows that `eta=.0180303234` permits `beta=.009` and hence the strip

```text
Re(s)>1-.009^2=1-.000081.                             (6.6)
```

Thus no such theorem is available as a routine Vaughan/exponent-pair
input.  A bound only for the data-dependent weights `f_r` would avoid the
full weight quantifier, but then its proof must exploit the `Q,R` inverse
structure.  Equations (2.2) and (4.2) show that this structure is made of
prime sampling correlations, not new phase curvature; proving its power
tail is a genuinely new H1/strip-level theorem.

---

## 7. Decision

```text
Neumann telescoping identity after R:                         EXACT;
subpower-to-power exponent ledger, conditional on contraction: EXACT;
VK first-defect estimate implies cyclic contraction:          FALSE;
natural infinite-dimensional low-pass operator has ||A||<1:   FALSE;
finite-dimensional repair avoids a prime frame/Schur bound:    FALSE;
current fixed-smooth Lambda twist gives a fixed power:          FALSE;
current uniform saving in the target aperture:                 log^(-3/10);
smooth f_r creates nonseparable Vaughan curvature:              FALSE;
literal passband/stopband has positive spectral margin:         FALSE;
defect-corrected construction closes H1:                        NOT PROVED;
uniform zeta zero-free strip:                                  NOT PROVED.
```

The proposal identifies a legitimate conditional mechanism: prove a
carrier-specific cyclic contraction for `A` and simultaneously prove a
fixed-power high-tail bound for the resulting inverse weight without
termwise triangle inequalities.  At present those are respectively the
prime sampling-frame/Schur gate and the natural weighted prime-polynomial
gate.  The Neumann notation does not make either estimate automatic.
