# Fixed-line Poisson mass has the wrong polarity for the arithmetic reserve

Status: exact coupling obstruction and quantitative theorem card,
2026-08-12.  This rules out an **automatic** conversion of the new
fixed-line Green--Poisson surplus into the candidate-relative fractional
arithmetic edge.  It does not rule out a zeta-specific signed correlation,
prove a zero-free strip, or prove RH.

## 1. Verdict

The fixed line used by the improved Green ledger is

```text
Re s=1.4,             x=Re s-1/2=0.9.
```

At a candidate reflected pair of depth
`0.49<=alpha<1/2`, its same-height Poisson charge is at most

```text
K_(0.9,alpha)(0)
 =1/(0.9-alpha)+1/(0.9+alpha)
 <=1/0.4+1/1.4=45/14.                              (1.1)
```

The completed logarithmic derivative forces total positive Poisson mass

```text
(1/2)*L+O(1),                L=log gamma.            (1.2)
```

Consequently, after deleting the selected functional-equation quartet,

```text
Poisson mass of all other zeros
--------------------------------
selected same-height pair mass
 >=(7/45)*L-O(1).                                    (1.3)
```

This is fatal to the proposed positive coupling.  If a positive Poisson
auxiliary is scaled so that its selected atom repairs `eta*K_rho` of the
isolated selected deficit, its all-other/main term has size at least

```text
eta*[(7/45)*L-O(1)]*K_rho.                           (1.4)
```

It enters with the opposite sign when the identity is solved for the
candidate-relative reserve.  The ratio in (1.4) is homogeneous, so the
conditional geometric exponent `0.0253912552...` cannot pay it: scaling
the auxiliary or spending part of the carrier exponent scales the selected
repair and the Poisson main term together.

There are only two ways out of (1.4).

1. Keep a positive-real zero kernel.  Then its positive vertical mass and
   its `log gamma` completion term are unavoidable.
2. Cancel the vertical mass by sigma differencing, horizontal resolvent
   subtraction, or signed harmonic coefficients.  Then the nonzero zero
   kernel has integral zero and changes sign.  Functional-equation pairing
   and conjugation preserve that zero mass.  The remaining assertion is a
   signed, candidate-conditioned zero/prime correlation of the same logical
   content as the missing reserve.

Thus no positive/log-derivative/resolvent identity currently converts the
Green--Poisson geometric surplus into

```text
Q_ar(q_rho)+K_rho>=epsilon*K_rho.                   (1.5)
```

## 2. Exact fixed-line calculation

For a zero `rho'=1/2+b+i*gamma'`, group it with its functional-equation
mate `1/2-b+i*gamma'`.  At centered horizontal coordinate `x>1/2`, their
positive Poisson kernel is

```text
K_(x,b)(v)
 =(x-b)/[(x-b)^2+v^2]
  +(x+b)/[(x+b)^2+v^2],       v=gamma-gamma'.       (2.1)
```

At the fixed line `x=0.9`, the completed logarithmic derivative gives

```text
sum_(all nontrivial zeros rho')
 (1.4-beta')/[(1.4-beta')^2+(gamma-gamma')^2]
 =L/2+O(1).                                         (2.2)
```

The `O(1)` is uniform here because the von Mangoldt series for
`zeta'/zeta(1.4+i*gamma)` is absolutely convergent.  Equation (2.2)
includes critical-line zeros individually and reflected off-line pairs as
in (2.1).

The function in (1.1) increases with `alpha`, proving its upper bound.
The two conjugate members of the selected quartet at ordinate `-gamma`
contribute `O(gamma^(-2))`.  If `A_0` denotes the full selected-quartet
charge and `A_rest` every other nontrivial zero, (2.2) therefore gives

```text
A_0<=45/14+o(1),
A_rest=L/2-A_0+O(1),
A_rest/A_0>=(7/45)*L-O(1).                         (2.3)
```

The same calculation works for a positive multiple or a positive mixture
of copies of this fixed line.  Extra positive centers add completion mass;
they cannot improve the selected-to-background ratio.

For a general line `Re s=1/2+x>1`, put `delta=1-beta=1/2-alpha`.
Since

```text
K_(x,alpha)(0)<=1/delta+1/(1-delta)<=2/delta,
```

the coarser uniform ratio is

```text
A_rest/A_0 >=(delta/4)*L-1+lower-order terms.        (2.4)
```

On any candidate not already excluded by the imported
Vinogradov--Korobov region, `delta*L` tends to infinity.  If the evaluation
line is also moved toward `1`, its distance `u=Re(s)-1` must be recorded:
the Dirichlet-series error is `O(1/u)`.  Choosing, for example,
`u asymp delta` makes this `o(L)` and leaves the lower bound in (2.4) of
order `delta*L`.  Thus an admissible move toward `1` changes the constant
but not the asymptotic polarity; taking `u` arbitrarily smaller without
charging `1/u` would not justify (2.4).

## 3. The reserve-polarity identity

For the deterministic candidate state, write the exact selected quotient
as

```text
Q_ar(q_rho)=-K_rho+R_rho,
R_rho=Q_ar(q_rho)+K_rho
     =sum_(unselected rho') h_q(rho').              (3.1)
```

Let `A(rho')>=0` be any positive fixed-line Poisson auxiliary and write

```text
A_0=A(selected quartet),
A_rest=sum_(unselected rho') A(rho').               (3.2)
```

For every `lambda>=0`, adding the exact logarithmic-derivative identity
amounts on the zero side to

```text
R_rho
 =sum_(unselected rho') [h_q(rho')+lambda*A(rho')]
  -lambda*A_rest.                                   (3.3)
```

The sign in (3.3) is the obstruction.  The only rowwise-positive repair of
a negative collateral response uses `+lambda*A`; after summation its known
positive mass is subtracted.

This is sharp, rather than an artifact of an absolute value.  A second copy
of the selected zero belongs to the unselected sum and has

```text
h_q=-K_rho,              A=A_0+o(1).                (3.4)
```

An arbitrarily close simple collateral pair has the same relations up to
`o(K_rho)` by continuity.  Current microscopic bounds permit such a row:
the `beta>=0.99` cap is `0.005L+o(L)`, not zero.  Therefore a universal
positive repair must take

```text
lambda*A_0>=(1-o(1))*K_rho.                         (3.5)
```

Equations (2.3), (3.3), and (3.5) then expose a subtraction of at least

```text
[(7/45)*L-O(1)]*K_rho.                              (3.6)
```

If one asks only that the auxiliary change the selected ledger by
`eta*K_rho`, replace the right side of (3.6) by `eta` times that quantity,
which is (1.4).  Retaining the exact `A_rest` term merely cancels the
auxiliary identity back to (3.1); discarding it loses (3.6).  There is no
third algebraic sign.

Notice also why the Poisson equilibrium cannot be read as a positive
reserve.  Critical-line zeros alone can supply the leading mass `L/2`,
whereas their compact-carrier response is power-negligible relative to
`K_rho`.  The Poisson identity forces positive **unweighted count mass**,
not carrier-aligned positive `h_q` mass.

## 4. Canceling the main term cancels positivity

The natural escape is to cancel (1.2).  It has an exact price.  Let

```text
H(z)=sum_j c_j/(z+a_j),             a_j>=0,          (4.1)
```

be a real finite resolvent combination and put `C=sum_j c_j`.  For every
`x>0`,

```text
integral_R Re H(x+i*y)dy=pi*C.                      (4.2)
```

The same coefficient `C` is the `1/z` tail of `H` and the coefficient of
the leading completed `log gamma` term.  Thus exact removal of (1.2) is
exactly `C=0`.  If the resulting kernel is nonzero and positive at the
target, (4.2) forces it to be negative somewhere.  Pairing
`rho'` with `1-conj(rho')` doubles (4.2), and adding conjugates doubles it
again; neither operation changes the conclusion.

For the prime-positive sigma differences

```text
K_(m,h)(z)
 =sum_(j=0)^m (-1)^j*binom(m,j)/(z+jh)
 =integral_0^infinity e^(-z*u)(1-e^(-h*u))^m du,    (4.3)
```

one has `C=0` for every `m>=1`.  Their prime coefficients are nonnegative,
but their real zero kernel has equal positive and negative vertical mass.
More quantitatively, if a fixed-gap target retains a fraction `r_0` of the
pole response, the audited inequality is

```text
integral_R [-Re K_(m,h)(x+i*y)]_+ dy
 >=[e^(-1/2)*cos(1/2)*delta/log(1/r_0)]*K_(m,h)(x). (4.4)
```

At `r_0=1/2` the coefficient is `0.767...*delta`.  The growing-step
`m=1` regime has an actual high-ordinate adverse bulk of order `L` before
signed cancellation.  Hence ordinary zero counts or absolute values do not
turn (4.3) into (1.5).

A nonnegative trigonometric polynomial does not alter the dichotomy.
If its logarithmic-derivative coefficients are used with positive signs,
it is in Sections 2--3.  If signed Fourier coefficients or horizontal
subtractions cancel the leading mass, the translated kernel still has
zero integral and changes sign.  Prime-side nonnegativity does not imply
zero-side positivity.

## 5. Sanity checks

### 5.1 Isolated completed block

For an isolated selected completed pair,

```text
R_rho=0                                                   (5.1)
```

exactly.  Thus no identity which merely adds completed logarithmic
derivatives can imply `R_rho>=epsilon*K_rho`.  It must prove that the
actual von Mangoldt coefficients exclude this isolated self-resonance.
That statement is the missing arithmetic theorem, not a formal consequence
of the Poisson ledger.

### 5.2 Functional-equation polynomial

The matched-quartet factor

```text
[(s-1/2)^2-(alpha+i*gamma)^2]
[(s-1/2)^2-(alpha-i*gamma)^2]                        (5.2)
```

preserves functional-equation symmetry, reality, order, and critical-line
phase, while its matched compact Weil response is strictly negative.  Its
Poisson response is strictly positive.  Hence no coefficient-free
pointwise comparison

```text
h_q(rho')>=c*A(rho'),              c>0,              (5.3)
```

is possible.  Raising (5.2) to a power amplifies the failure.  This is not
an Euler-product counterexample; it identifies the zeta-specific joint
input that a successful coupling must use.

### 5.3 Harmonic-center prime cone

Positive mixtures of logarithmic derivatives produce nonnegative
Laplace/trigonometric prime weights.  The compact sinh-tent
autocorrelation is positive on its early third and negative on its late
half.  Therefore the positive prime cone does not represent the actual
compact arithmetic scalar.  A harmonic polynomial can retain the target
carrier, but it cannot supply its missing sign merely from
`Lambda(n)>=0`.

## 6. Exact surviving theorem

The new Green--Poisson ledger remains valuable for geometric compression,
but it cannot also certify the arithmetic reserve through a positive
copy of the same Poisson identity.  What would revive the coupling is a
genuinely signed statement such as

```text
sum_(unselected rho') h_(q_rho)(rho')
   >=epsilon*K_rho+o(K_rho),                         (6.1)
```

proved from the actual von Mangoldt coefficients jointly with the
candidate equation, before taking absolute values or marginal zero counts.
Equivalently one may prove the one-sided compact prime scalar in the
candidate-relative arithmetic-edge card.  A signed sigma-difference or
resolvent reformulation is useful only if it proves that correlation; it
does not make it automatic.

The binary conclusion is therefore:

```text
fixed-line positive Poisson coupling                 CLOSED;
Gamma-cancelled termwise-positive resolvent coupling CLOSED;
zeta-specific signed target-conditioned coupling     OPEN;
uniform zero-free strip                              NOT PROVED.
```

Primary dependencies:

- `ZETA23-GREEN-POISSON-DUAL-PICK-LEDGER-2026-08-12.md`;
- `ZETA23-CANDIDATE-RELATIVE-FRACTIONAL-ARITHMETIC-EDGE-AUDIT-2026-08-12.md`;
- `R129-SIGMA-DIFFERENCE-LOGDERIVATIVE-GATE.md`;
- `R132-FUNCTIONAL-PAIR-SIGMA-KERNEL-GATE.md`;
- `ZETA23-CENTERED-SINH-TENT-FUNCTIONAL-EQUATION-NOGO-2026-08-12.md`;
- `ZETA23-HARMONIC-CENTER-SINH-TENT-AMPLIFICATION-NOGO-2026-08-12.md`.
