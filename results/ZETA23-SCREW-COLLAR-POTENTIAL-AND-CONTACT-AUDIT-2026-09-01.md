# ZETA23 screw-collar potential and contact audit

Date: 2026-09-01.

## 0. Verdict

This pass does **not** prove RH, a uniform zero-free strip, or kernel-null
charge (KNC).  It does resolve the proposed contact calculation and changes
the decision tree in four useful ways.

1. The exact first variation is the collar projection of a single exterior
   potential.  The formula is now typed both in the abstract form Hilbert
   space and in Suzuki's continuous-kernel coordinates.
2. The continuous potential formula extends from the `H_0^1` core to an
   actual closed-form-domain radical.  The apparent endpoint-domain obstacle
   can be removed by moving one derivative onto `g` and using
   `g' in L^2_loc`.
3. The right-collar potential has an explicit pole + gamma/Lerch + prime-ramp
   increment formula.  It is not a finite endpoint flux: it contains all
   shifted window integrals at the active prime-power delays.
4. Generic propagation is false in a much stronger class than the earlier
   scalar block examples.  An even `C^1`, compactly supported convolution
   kernel can be positive semidefinite on the full old interval and charge a
   concrete mean-zero nullvector in every arbitrarily thin collar.  On an
   explicitly stated two-dimensional old sector its radical is exactly one
   dimensional.  The rational integration is replayed exactly in Python,
   while Lean kernel-checks the polynomial sign and negative-direction
   consequence.

Thus the hoped-for automatic boundary conservation law is absent.  The only
live continuation statement is a completed-zeta **constrained gap theorem**
for the explicit exterior potential.  That theorem is equivalent to exact
KNC on the candidate nullstate; it must use more than smoothness, compactness,
difference-kernel structure, the concrete old-window zero-sum degeneracy, or generic
Fredholm factorization.

The formulas below appear to be new to this repository.  A targeted check of
Suzuki's 2023 and 2026 papers found localization, continuity, the continuous
kernel, and mean-periodicity, but no Hadamard support derivative or collar
propagation theorem.  This is not a claim of exhaustive literature-level
novelty.

## 1. Exact abstract block charge

Work in the fixed outer form Hilbert space `(V_B,h)`, with

```text
q(x,y) = h(x,y) + <R_B Jx,Jy> = h((I+G)x,y),
G = J* R_B J.
```

For a nested split

```text
V_b = V_a direct-sum_h W,
W = V_b intersect V_a^(perp_h),
```

the bounded form operator has the exact block matrix

```text
S = [[A,C],[C*,D]],
A = I + P_a G|_(V_a),
C = P_a G|_W,
D = I + P_W G|_W.
```

Suppose `q_a >= 0`, put `N=ker A`, and take `n in N`.  Positivity makes `n`
a radical of the old block, so

```text
q(n,u)=0                       (u in V_a),
q(n,w)=h(P_W G n,w)=<R_B Jn,Jw>  (w in W).
```

The exact vector-valued charge is therefore

```text
chi = P_W J* R_B J|_N = C*|_N,                           (1.1)
```

and

```text
||chi n||_h
 = sup_(w in W, ||w||_h=1) |<R_B Jn,Jw>|.               (1.2)
```

For a variation `u+w`,

```text
d/dt q(n+t(u+w))|_(t=0) = 2 Re h(chi n,w).               (1.3)
```

This is the precise first variation.  It has no old-sector contribution;
all contact information is the collar vector `chi n`.

### 1.1 What Fredholm factorization actually gives

At a Fredholm contact, `A` has closed range and a positive gap on `N^perp`.
Consequently

```text
C = A^(1/2) T + P_N C,
T = A^(dagger 1/2) (I-P_N) C.                            (1.4)
```

The first summand is automatic.  The second is finite rank, and

```text
(P_N C)*|_N = chi.                                       (1.5)
```

Hence

```text
KNC
 iff P_N C=0
 iff C=A^(1/2)T for some bounded T
 iff C C* <= c A for some finite c.                      (1.6)
```

This identifies the failure of the earlier factorization strategy.  The
automatic pseudoinverse factors every non-null component and leaves exactly
the desired nullspace charge as its remainder.  Dropping that remainder is
not a proof of KNC; it is KNC.

Without closed range, kernel annihilation implies only

```text
range(C) subset closure(range(A^(1/2))),
```

not a bounded Douglas factorization.

## 2. Closed-form-domain exterior-potential theorem

Let `I_a=(-a,a)`, let `g` be Suzuki's continuous even zeta kernel, and let
`q_a` be the closed localized Weil form.  Suppose

```text
n in D(q_a),       n != 0,       q_a >= 0,       q_a(n,n)=0.  (2.1)
```

Extend `n` by zero and use Suzuki's convention `D=i d/dx`.  Since
`g' in L^2_loc`, the function

```text
H_n(x) = i integral_(-a)^a g'(x-y)n(y)dy                 (2.2)
```

is well defined and continuous on every compact interval.

### Theorem 2.1 (domain-safe plateau and collar charge)

For every smooth compactly supported test `z`, with the supports interpreted
inside a common outer interval,

```text
q(n,z) = integral H_n(x) conjugate(i z'(x)) dx.           (2.3)
```

There is a scalar `C_n` such that

```text
H_n(x)=C_n                         (x in I_a).             (2.4)
```

For `b=a+delta`, put

```text
E_(a,b)=I_b minus I_a,
e_(a,b)=(H_n-C_n) 1_(E_(a,b)).                            (2.5)
```

If `P_b` is orthogonal projection onto `L_0^2(I_b)`, the exact
derivative-coordinate charge is

```text
Gamma_(a,b)n=P_b e_(a,b),                                (2.6)
```

with norm

```text
||Gamma_(a,b)n||_2^2
 = integral_E |H_n-C_n|^2
   - (1/(2b)) |integral_E (H_n-C_n)|^2.                  (2.7)
```

Moreover,

```text
KNC(n;a,b)
 iff H_n is constant on I_b
 iff Gamma_(a,b)n=0.                                     (2.8)
```

#### Proof

Choose `n_j in C_c^infinity(I_a)` converging to `n` in a shifted form norm.
This also gives `n_j -> n` in `L^2`.  After zero extension to a fixed outer
interval `I_b`, the form on two old-supported arguments is the same global
Weil form as on `I_a`.  Thus, after choosing one common lower-bound shift,
the `I_b` form-norm difference is the `I_a` form-norm difference plus only a
fixed multiple of the same `L^2` difference; in particular `n_j -> n` in the
common outer form norm as well.  For every compact `K`,

```text
sup_(x in K) |H_(n_j)(x)-H_n(x)|
 <= ||n_j-n||_2 ||g'||_(L^2(K-I_a)) -> 0.                (2.9)
```

On the smooth core, Suzuki's polarized identity followed by integration by
parts in `y` gives (2.3).  Form continuity on the left and (2.9) on the right
pass the identity to `n`.

Because a zero-energy vector of a nonnegative form lies in its radical,
`q(n,z)=0` for every interior test `z`.  Equation (2.3) says that `H_n'=0`
distributionally on `I_a`.  Continuity gives (2.4).

On `I_b`, write `H_n=C_n+e_(a,b)`.  Projection kills the constant, proving
(2.6).  The elementary formula for projection off the constant function is
(2.7).  Finally, smooth collar derivatives separate functions modulo
constants.  Since the old plateau fixes the constant to `C_n`, vanishing of
all collar pairings is equivalent to (2.8).  QED.

This argument removes the earlier `H_0^1` endpoint-trace caveat.  It does not
identify the `L^2` norm in (2.7) with the `h`-harmonic quotient norm in
(1.2); the zero set is exact, but quantitative norms are different.

### 2.1 Automatic flatness is not annihilation

At the right edge, `a-y>=0`.  The one-sided logarithmic modulus satisfies

```text
integral_0^R |log(t+s)-log t|^2 dt = O(s),               (2.10)
```

and each of the finitely many active prime-ramp jumps contributes `O(s)` to
the squared translation modulus.  The smooth terms are smaller.  Therefore

```text
|H_n(a+s)-C_n| <= C_a sqrt(s) ||n||_2,                   (2.11)
||Gamma_(a,a+delta)n||_2 <= C_a delta ||n||_2.           (2.12)
```

For each fixed `n`, normalized one-sided translates converge weakly to zero,
which sharpens (2.12) to

```text
||Gamma_(a,a+delta)n||_2=o(delta).                       (2.13)
```

The little-`o` is uniform on the finite-dimensional contact kernel.

This explains why numerical collar charge can look exceptionally small.
It does not help with exact positivity: if the charge is nonzero, however
small, then for a suitable complex scalar `t`,

```text
q_b(n+t z)=2 Re(conjugate(t) q_b(n,z))+|t|^2q_b(z,z)<0.  (2.14)
```

There is no perturbative tolerance at a zero diagonal.

On the smaller `H_0^1` core, writing `u=Dn in L_0^2` supplies one additional
integration and gives the stronger raw rate `o(delta^2)`.  That extra rate
does not apply to an arbitrary closed-form-domain nullvector and still does
not imply exact KNC.

## 3. Exact completed-zeta contact increment

The abstract charge (1.1) is, on every collar test,

```text
poleCross(n,z) + archimedeanCross(n,z)
  - sum_m primePowerCross_m(n,z).                         (3.1)
```

The pointwise potential makes this cancellation explicit.  Define

```text
c_Gamma = psi(1/4)-log pi,
ell_m   = log m,
w_m     = Lambda(m)/sqrt(m),
L(rho)  = exp(-rho/2) Phi(exp(-2rho),1,1/4).              (3.2)
```

For

```text
0<r<min(2a,log 2),
Delta_n(r)=H_n(a+r)-H_n(a-r)=H_n(a+r)-C_n,               (3.3)
```

direct differentiation of Suzuki's explicit `g` gives

```text
Delta_n(r)
 = -8 i sinh(r/2)
       integral_(-a)^a cosh((a-y)/2)n(y)dy

   - i c_Gamma integral_(a-r)^a n(y)dy

   - (i/2) integral_(-a)^a
       [L(a+r-y)-sgn(a-r-y)L(|a-r-y|)] n(y)dy

   + i sum_(m>=2, ell_m<2a+r) w_m
       integral_(max(-a,a-r-ell_m))^(min(a,a+r-ell_m)) n(y)dy.  (3.4)
```

Empty intervals contribute zero.  The Lerch integrand is defined almost
everywhere and its value at `y=a-r` is immaterial: the integral is the
locally integrable improper integral across the logarithmic singularity, not
a pointwise assignment to `sgn(0)L(0)`.

The prime normalization in (3.4) is important:

- the index is `m`, with weight `Lambda(m)/sqrt(m)`;
- the right-collar sign is `+i`;
- there is no factor `2` in one right-collar increment;
- the familiar factor `2` appears after differentiating the centered moving
  interval at zero or combining the appropriate symmetric contributions.

For `0<s<min(2a,log 2)` and a right-collar test
`z in H_0^1(a,a+s)`, zero-extended,

```text
q_(a+s)(n,z)
 = integral_0^s Delta_n(r) conjugate(i z'(a+r))dr
 = <-g''*n,z>.                                           (3.5)
```

Consequently, right KNC is exactly

```text
Delta_n(r)=0 almost everywhere on (0,s).                 (3.6)
```

Equation (3.4), rather than an endpoint Wronskian, is the sought arithmetic
contact law.  It shows why the finite-interface and finite-jet routes kept
failing: every newly exposed collar width scans translated integrals of the
unknown state at all active prime-power delays, against a simultaneous
continuous Lerch background.

## 4. Exact structured countermodel

The absence of a generic conservation law can be certified without reducing
to an arbitrary matrix.

On `(0,1+delta)`, define the even `C^1`, compactly supported difference
kernel

```text
kappa(s) = 1,                                  |s|<=1,
           1-3r^2+2r^3,  r=|s|-1,             1<=|s|<=2,
           0,                                  |s|>=2.   (4.1)
```

Let

```text
p(t)=t(1/4-t) 1_[0,1/4](t),
n(t)=p(t)-p(t-1/2),
m(t)=p(t)+p(t-1/2).                             (4.2)
```

On the old interval every difference has magnitude at most one, so

```text
q_1(f,h)=(integral f) conjugate(integral h).              (4.3)
```

On `span{n,m}`, the old block is positive semidefinite and has radical
exactly `span{n}`; indeed `integral n=0` and `integral m=1/192`.

For `0<delta<=1/4`, take the collar bump

```text
w_delta(u)=(u-1)(1+delta-u) 1_[1,1+delta](u).             (4.4)
```

Exact polynomial integration gives

```text
q(n,w_delta)
 = -delta^7(28delta^2-135delta+90)/60480 < 0,            (4.5)

q(w_delta,w_delta)=delta^6/36.                           (4.6)
```

The two-dimensional block determinant is therefore

```text
-q(n,w_delta)^2<0                                        (4.7)
```

for every arbitrarily thin collar.  The filtration

```text
span{n,m} direct-sum H_0^1(1,b)
```

is nested and compactly embedded in `L^2`.  A standard flat smoothstep can
make a related kernel `C^infinity`, but preservation of the strict sign for
every collar width was not replayed here and is not entered in the theorem
ledger.

Thus all of the following can hold simultaneously without KNC on this
explicit nested subspace filtration:

- nesting and compact embedding;
- an exactly one-dimensional old kernel after the stated two-dimensional
  restriction;
- an even Hermitian difference kernel;
- compact support and `C^1` regularity;
- full old-window positivity, with the form vanishing concretely on every
  zero-integral old vector;
- nonzero charge in every arbitrarily small enlargement.

This refutes deductions from those generic axioms alone.  It does not refute
a theorem that additionally uses the full support-saturated zeta form domain.

The exact arithmetic is replayed by
`src/screw_collar_contact.py`; the sign and negative-direction implication are
kernel-checked in `RHBridge/ScrewCollarHostileModel.lean`.

## 5. The xi mean-periodic identity: useful coordinate, not yet a theorem

Suzuki also proves unconditionally that

```text
g * eta' = 0,                                            (5.1)
```

where

```text
eta(t)=2 exp(-t/2) sum_(k>=1)
  (2 pi^2 k^4 exp(-4t)-3 pi k^2 exp(-2t))
  exp(-pi k^2 exp(-2t)),                                 (5.2)
```

and

```text
Fourier(eta)(z)=xi(1/2-iz).                              (5.3)
```

Hence the global defect `U_n=H_n-C_n` satisfies

```text
U_n * eta'=0,       U_n=0 on I_a.                        (5.4)
```

A safe functional-analytic typing uses the Fesenko--Ricotta--Suzuki
superexponentially decreasing test space

```text
S_exp(R)={phi in C^infinity:
  sup_x exp(m|x|)|phi^(k)(x)|<infinity for every m,k}
```

and its continuous dual.  This is not the ordinary Schwartz/tempered pair.
Suzuki's growth bound puts `g` in the dual, while `eta'` lies in `S_exp`.
Since a compactly supported `L^2` form vector is in `L^1`, direct Fubini with
the superexponentially decaying `eta'` passes (5.4) to the closed-form-domain
potential `H_n=i g'*n`.  This avoids requiring `Dn` to be an ordinary
function.

This turns KNC into a constrained mean-periodic gap problem:

> If `U=i g'*n-C` comes from a compactly supported, support-saturating
> completed-zeta radical and vanishes on its support interval, must it vanish
> on an adjacent collar?

Equation (5.4) is genuine zeta structure, but it holds for every compact
input `n`, not only a radical.  Mean-periodicity alone does not imply unique
continuation.  Indeed, choose a nonzero smooth `2 pi`-periodic function `U`
that vanishes on a proper open arc, and choose the Schwartz annihilator
`rho` by

```text
Fourier(rho)(xi)=exp(-xi^2) sin(pi xi).
```

The Fourier series of `U` is supported at integer frequencies, where
`Fourier(rho)` vanishes, so `U*rho=0` while `U` retains its interval gap.
This is a rigorous generic mean-periodic countermodel.  It is not asserted
to have the special provenance `U=i g'*n-C`, and it is not a counterexample
for Suzuki's actual `eta'`.

For the actual `eta'`, arbitrary spectral weights and the constrained
coefficients coming from one Paley--Wiener transform of `n` are materially
different.  No unconditional actual-`eta'` gap counterexample was certified
in this pass.  Any successful gap theorem must additionally use the
Paley--Wiener provenance of `n`, the exact `xi` zero divisor, and the
pole/gamma/prime coupling in (3.4).  Merely citing (5.1) would re-label, not
solve, the compressed-kernel problem.

Half-line vanishing would be different: a bilateral Laplace product can then
force propagation, and finite spectral support would give analytic unique
continuation.  The collar potential is two-sided and has infinite zeta
spectrum, so neither theorem applies.

## 6. Decision-tree update

### Closed routes

The following are no longer credible as stand-alone proofs of propagation:

1. a generic Hadamard or endpoint-flux sign;
2. finite endpoint jets or finitely many prime interfaces;
3. compactness/Fredholmness plus a pseudoinverse factorization;
4. continuity or `C^1` regularity of the screw kernel;
5. the concrete fact that the old-window form vanishes on every zero-sum
   old vector;
6. a small-`delta` estimate for the charge.

The exact countermodel kills 1, 4, and 5.  Equations (1.4)--(1.6) kill 3.
Equation (3.4) kills 2.  Equations (2.13)--(2.14) explain why 6 cannot work.

### Live RH-strength target

The strongest honest continuation target is now:

```text
Completed-zeta constrained gap theorem:

For every first-contact radical n, the function
U_n(x)=i integral g'(x-y)n(y)dy-C_n
cannot vanish exactly on I_a and become nonzero immediately outside I_a.
                                                               (6.1)
```

This theorem is exactly KNC in explicit coordinates and remains RH-strength
when required at every contact.  The calculation makes it attackable, but
does not make it logically weaker.

### Better strength-matched target for a uniform strip

For the immediate objective of a fixed zero-free half-plane, unshifted KNC
is stronger than necessary.  Suzuki's shifted function `Psi_omega` satisfies

```text
xi(s) != 0 for Re(s)>1/2+omega
 iff Psi_omega(t)>=0 for all sufficiently large t.       (6.2)
```

Thus a uniform strip is more directly targeted by proving eventual one-sided
positivity for one fixed `0<omega<1/2`.  This is the same strength class as the
repository's R95/R96 one-sided signed-ramp criterion, and the prime part is
explicitly

```text
-sum_(m<=exp t) Lambda(m)m^(-1/2-omega)(t-log m).         (6.3)
```

Direct eventual positivity in (6.2) is already exactly the desired strip,
not a weaker intermediate lemma.  The best next *information-gain
diagnostic* is therefore to put (6.3) and the R95 bounded signed ramp in a
common transform family and ask whether either representation exposes an
independently provable one-sided margin.  It becomes a proof route only if
such a margin is found.  If the goal remains full RH, pursue (6.1); if the
immediate goal is the uniform strip, use this comparison to select a genuine
intermediate lemma for (6.2).

## 7. Reproducibility and status

Artifacts:

- `results/context/zeta23_weil_contact_identity_preflight_v1.json`;
- `src/screw_collar_contact.py`;
- `src/test_screw_collar_contact.py`;
- `lean/rhbridge/RHBridge/ScrewCollarHostileModel.lean`;
- `lean/rhbridge/RHBridge/ScrewCollarHostileModelAudit.lean`.

Checks run:

```text
python3 -m pytest -q src/test_screw_collar_contact.py
13 passed

lake build RHBridge.ScrewCollarHostileModel
build succeeded

lake env lean RHBridge/ScrewCollarHostileModelAudit.lean
axiom audit: only standard Lean axioms
```

Final theorem ledger:

| Claim | Status |
|---|---|
| typed abstract charge `(1.1)`--`(1.3)` | proved |
| Fredholm factorization with finite-rank KNC remainder | proved |
| closed-form-domain plateau theorem | proved on accepted Suzuki/core interfaces |
| exact derivative-coordinate collar norm | proved |
| `o(delta)` raw collar flatness | proved; not the harmonic KNC norm |
| explicit pole/Lerch/prime contact increment | derived and sign/factor audited |
| even convolution arbitrary-collar countermodel | proved and replayed |
| generic boundary conservation | refuted |
| completed-zeta constrained gap theorem / KNC | open |
| uniform zero-free strip | open |
| RH | open |

## 8. Primary sources

- Masatoshi Suzuki, *Weil's quadratic form via the screw function*,
  <https://arxiv.org/html/2606.09096v2>.
- Masatoshi Suzuki, *Aspects of the screw function corresponding to the
  Riemann zeta-function*, <https://arxiv.org/html/2206.03682v4>.
