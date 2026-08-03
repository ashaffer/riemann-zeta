# Global Möbius--Poisson cancellation gate

Status: the required cross-prime cancellation is constructed exactly; its
natural lift is a signed mixed pairing, not a positive Gram form, 2026-08-01.

## 1. The connected transform

Ordinary Poisson norms expand multiplicatively and contain unwanted products
between distinct prime channels.  The zeta explicit formula does not: its
arithmetic coefficient is the von Mangoldt function because it comes from the
logarithmic derivative of the Euler product.

On the divisor incidence algebra the exact connected transform is

`mu * log = Lambda`.

Coefficientwise,

`sum_(d | n) mu(d) log(n/d) = Lambda(n)`.

Therefore every integer involving at least two distinct primes cancels
algebraically, while a prime power `p^k` leaves `log p`.  This is an
intrinsically nonlocal cancellation: all divisor channels of `n` participate,
and no zeta zero or positivity assertion enters.

For a fixed logarithmic support window the construction is finite.  Only the
prime powers whose logarithmic translations meet the autocorrelation support
occur, and the cancellation for each such `n` uses only its divisors.  Thus no
uncontrolled infinite Euler-product limit is needed at this stage.

The identity is kernel-checked in
`RHBridge.GlobalMobiusCancellation.moebiusLog_eq_vonMangoldt`, using mathlib's
proved arithmetic-function theorem.

## 2. Incidence-space interpretation

For each `n`, put the divisor data

`a_n(d)=mu(d)`, `b_n(d)=log(n/d)`, for `d | n`.

Their mixed incidence pairing is

`<a_n,b_n> = Lambda(n)`.

Tensoring these divisor vectors with the logarithmic translation states of a
test function reproduces the prime autocorrelation coefficient after summing
over `n`.  Distinct-prime composites have disappeared before the analytic
explicit formula is invoked.  This is the requested algebraic cross-place
cancellation.

## 3. Positivity obstruction

The construction naturally produces a mixed pairing

`2 Re <U_mu f, U_log f>`.

Polarization gives

`2 Re <u,v> = ||u+v||^2 - ||u||^2 - ||v||^2`.

It is therefore a connected/cumulant or supertrace expression, not a norm.
If the cross coefficient is nonzero, replacing `v` by `-v` reverses its sign.
Equivalently, the pure block operator

`[[0,C],[C*,0]]`

has paired positive and negative singular directions.  Lean proves both the
polarization identity and this sign obstruction in
`RHBridge.GlobalMobiusCancellation`.

Adding positive diagonal blocks `A,B` can make

`[[A,C],[C*,B]]`

positive only by a Schur/contraction inequality.  That inequality is precisely
the missing completed domination; it is not supplied by Möbius cancellation.
If the lift remains block-diagonal in the output prime powers, the optimal
prime-edge theorem applies and the known pole/archimedean residual is negative.

## 4. Why ordinary global Poisson does not finish the lift

The global Poisson relation unconditionally intertwines Fourier transform with
multiplicative inversion.  In the operator formulation, the hoped-for positive
leakage is `P U* (1-P) U P`.  Connes--Consani's projection lemma shows that its
identification with the signed logarithmic derivative requires the Hardy-space
invariance `P U = P U P`; for scalar multipliers this is exactly an innerness
condition.  The local gamma and Euler ratios are not inner.  For the completed
zeta ratio, innerness is the zero-free/Hermite--Biehler condition carrying the
RH burden.

Thus Poisson gives the functional equation and Möbius gives the connected
prime cancellation, but neither converts the resulting supertrace into a
Hilbert trace unconditionally.

## 5. Surviving nonlocal target

The remaining object must be a **completed incidence complex**, not a single
transform assembled from local squares.  On each support window it must:

1. have the Möbius divisor differential above, so its connected arithmetic
   trace is exactly `Lambda`;
2. include the archimedean place and pole classes in the same differential;
3. derive the Guinand--Weil form as an Euler/supertrace identity;
4. supply an independent Hodge injection or cancellation pairing that removes
   the negative parity sector and turns that supertrace into a norm;
5. remain compatible as the finite divisor lattice grows with support.

Items 1 and the finite-window algebra are now closed.  Item 4 is the decisive
new theorem.  Calling the Euler pairing positive, or taking a square root of
the completed Weil operator, would simply assume it.

The sharpest fail-fast subproblem is to adjoin one archimedean/pole generator
to the finite divisor complex and ask whether a differential with `d^2=0`
can reproduce the exact gamma logarithmic derivative while pairing every odd
arithmetic state.  Failure of `d^2=0`, or an unpaired odd class in the first
prime window, kills this Hodge lift before any large-support analysis.

## Literature alignment

This explains the precise gap in the semilocal program of Connes and Consani:
their global Poisson map exists and the single archimedean Sonin mechanism is
positive, while extension of positivity to growing semilocal sets is the
RH-relevant conjecture.  The divisor-incidence formulation above isolates the
missing ingredient as a Hodge cancellation for the connected Möbius sector,
rather than another Euler-factor estimate.

Primary references:

- Connes--Consani, *The Scaling Hamiltonian*,
  <https://arxiv.org/abs/1910.14368>.
- Connes--Consani, *Weil positivity and Trace formula, the archimedean place*,
  <https://arxiv.org/abs/2006.13771>.
- Connes--Consani--Moscovici, *On q-series and the moment problem associated
  to local factors*, <https://arxiv.org/abs/2403.01247>.
