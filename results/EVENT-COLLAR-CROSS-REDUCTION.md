# Event collar and cross reduction

Status: exact reduction proved; the final analytic inequalities remain open.

## Old block

The embedded old block is unchanged at every enlargement. Every newly active
prime shift is at least the old support diameter, so its old-vector
autocorrelation is zero. Thus

`Q_b(embed f) = Q_a(f)`.

## Collar diagonal

For a vector supported in the two collars

`[-b,-a] union [a,b]`,

translation geometry permits autocorrelation only for shifts at most `b-a`
within one side or shifts between `2a` and `2b` across the two sides.

On consecutive prime-power event windows, every active prime shift lies
strictly above the collar width and at or below `2a`. Endpoint overlap is
null. Therefore the complete collar prime term vanishes and Lean proves

`Q_b(collar) = poleTerm_b(collar) + archimedeanTerm_b(collar)`.

This is a substantial simplification: collar positivity is now a prime-free
logarithmic uncertainty problem.

## Cross block

All remaining arithmetic difficulty is in the old--collar cross interaction.
RHBridge now packages a common positive control functional `E_collar`:

1. `0 <= E_collar <= Q_b(collar)`;
2. `cross(old,collar)^2 <= Q_b(old) * E_collar`.

These imply both collar positivity and the sharp Schur bound, hence positivity
of the enlarged form. The construction of such an `E_collar`, uniformly over
event windows, is the decisive unresolved estimate.

## Honest boundary

Neither collar positivity nor the relative cross inequality has been assumed.
The support-overlap identities are standard measure-theoretic literature
inputs and are separately axiom-audited. Proving the prime-free collar form
positive appears approachable through a logarithmic uncertainty inequality.
The cross estimate may retain essentially RH-level difficulty and must be
tested rather than presumed.
