# Zero-side arithmetic cancellation checkpoint

## Proposed route

At a first support where the localized Weil form becomes degenerate, a
nonzero radical vector annihilates every variation.  Guinand--Weil rewrites
that condition as a convergent sum of transform evaluations over nontrivial
zeta zeros.  The proposed shortcut was to use Paley--Wiener completeness to
isolate each functional-equation quartet and force its contribution to vanish
or become positive.

## What survives

Compact support makes the transform entire of finite exponential type.  The
zeta-zero ordinates form a strongly overcomplete exponential family on a
fixed finite interval.  This supports uniqueness of a function whose samples
all vanish; it does not supply variations that select one sample while
annihilating every other sample.

Under RH the distinction disappears because every zero summand is already a
positive square.  Unconditionally, an off-line quartet gives cross-products
of transform values at different complex arguments.  Nonnegativity or
radicality of their infinite sum does not imply termwise nonnegativity or
termwise vanishing.

## Formal countermodel

`ZeroSideOvercompleteness.lean` records the finite-dimensional model

`2 x^2 + 2 y^2 - (x+y)^2 = (x-y)^2 >= 0`.

The three sampling directions are overcomplete in two dimensions, one carries
a negative weight, and `(x,y)=(1,1)` is a nonzero radical vector.  None of its
three individual samples vanishes.  Thus even global nonnegativity plus an
exact radical equation cannot justify separating the zero contributions.

## Verdict

Ordinary completeness, zero density, and Paley--Wiener uniqueness do not close
the arithmetic cancellation problem.  The missing property would be a stable
interpolation or biorthogonal family capable of isolating off-line quartets.
The zeta ordinates are overcomplete rather than interpolating, so such a
family cannot be obtained from density alone.

This retires the naive zero-by-zero isolation route.  A surviving zero-side
approach needs extra structure relating quartet coefficients before
summation--for example, a sign identity detecting horizontal displacement--
not merely vertical zero density or completeness.

## Quartet phase target

For real test data, the four symmetry-related contributions associated with
an off-critical centered zero reduce algebraically to

`4 Re(F(alpha) F(-alpha))`.

This expression can have either sign.  `ZeroQuartetPhase.lean` proves the
quartet identity and gives an explicit negative instance.  Accordingly, the
extra structure needed by a zero-side route is now exact: prove a phase
relation forcing `Re(F(alpha)F(-alpha)) >= 0` for the relevant radical vector,
or prove cancellation of all negative quartet phases by some independently
positive quantity.  Functional-equation symmetry alone supplies neither.

Parity and positivity do not supply it either.  For an even positive pair of
point masses at `+/-x_0`, choosing `gamma*x_0 = pi/2` makes the transform at
`delta+i gamma` purely imaginary and nonzero.  Its square phase is therefore
strictly negative.  Smooth positive even bumps approximate this example while
preserving the strict sign.  Lean formalizes the decisive pure-imaginary
square calculation as `pureImaginary_square_re_neg`.

The reproducible Galerkin diagnostic `src/quartet_phase_scan.py` also tests the
actual positive-window near-ground states at known zeta ordinates while
hypothetically varying horizontal displacement.  Negative quartet phases
occur, confirming that evenness and observed ground-state shape do not create
the missing sign law.  This does not model an actual off-line zeta zero; it
specifically falsifies a universal phase claim about the test function.
