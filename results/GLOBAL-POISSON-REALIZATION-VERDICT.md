# Global Poisson realization verdict

Status: identified with Suzuki's shifted-xi canonical-system criterion; not an
independent route, 2026-08-01.

## 1. Exact identification

Set

`E_a(z)=xi(1/2+a-iz)`.

Using conjugation and the functional equation,

`E_a#(z)=conj(E_a(conj(z)))=xi(1/2-a-iz)`.

Hence

`Theta_a(z)=E_a#(z)/E_a(z)`

is exactly the shifted-xi meromorphic function studied by Masatoshi Suzuki
(up to the harmless reciprocal/reflection convention used in our numerical
scan).

The associated de Branges kernel is

`K_(E_a)(z,w)`

` = [E_a(z)conj(E_a(w))-E_a#(z)conj(E_a#(w))]`

`   / [2 pi i (conj(w)-z)]`.

After multiplication by nonvanishing denominator factors, this is the same
Pick defect kernel as the shifted-ratio kernel in our Path B.

## 2. Positivity is exactly the zero-free statement

The following are equivalent for fixed `a>0`:

1. `E_a` is Hermite--Biehler;
2. `Theta_a=E_a#/E_a` is meromorphic inner in the upper half-plane;
3. the de Branges/Pick kernel is positive;
4. a passive Hilbert-space realization of `Theta_a` exists;
5. zeta has no zero with real part greater than `1/2+a`.

The equivalence between the zero-free region and innerness is Suzuki's
Proposition 1.2.  Requiring these properties for every `a>0` is RH.

Thus every exact Hilbert colligation for the shifted ratio has a defect-kernel
factorization of the desired positive kernel.  Constructing it with manifest
positivity is not scaffolding around RH; it proves the load-bearing
Hermite--Biehler condition itself.

## 3. What Poisson/canonical-system theory already supplies

Suzuki constructs the canonical system explicitly and unconditionally in a
safe shifted range (`a>1` in the cited construction), using Fourier/Hankel
machinery related to Burnol's work.  The paper explains that extension to all
`a>0` would yield an RH criterion in which RH appears as positive
semidefiniteness of the family of Hamiltonian matrices.

This matches our audit exactly:

- large shifts lie in an unconditional zero-free/inner regime;
- local Euler factors are not passive;
- the global Hankel/canonical system is the correct completion-native object;
- positivity for small shifts is the unresolved zero-location theorem.

The newer adelic language does not alter the defect kernel.  Any minimal
global Poisson realization with transfer function exactly `Theta_a` must
reproduce the same de Branges kernel; if its state metric is Hilbert, it has
already established the Hermite--Biehler inequality.

## 4. Verdict

We cannot honestly falsify existence of the desired global Hilbert realization
without disproving RH, nor prove it without proving RH.  What is proved by the
audit is that the proposed sliver is not an independently weaker bridge:

> a positive global Poisson/adelic realization of every shifted-xi ratio is
> the known de Branges--Suzuki RH criterion in realization language.

The factorwise construction is structurally falsified by local nonpassivity.
The irreducibly global construction is mathematically viable but carries the
entire RH burden in positivity of its Hamiltonian.  It should therefore be
closed as a separate research path rather than counted as remaining leverage.

Primary source: Masatoshi Suzuki, *A canonical system of differential
equations arising from the Riemann zeta-function*, arXiv:1204.1827.
