/-
Copyright (c) 2026 Riemann-Zeta project contributors. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Riemann-Zeta project contributors
-/
import RHBridge.P2CanonicalRounded

/-!
# Executable fixed-grid factor dumper

This module is a certificate-generation utility, not part of the trusted
proof.  It prints the `10^200`-scaled integer coefficients and error of all
32 normalized defects and all 1536 normalized selected components.  A later
Lean module treats the output only as proposed data and verifies its small
checkpoint equalities in the kernel.

Line format:

* `D|panel|error|c0,c1,...` for a defect;
* `C|E/O|panel|mode|error|c0,c1,...` for a component.
-/

namespace RHP2Bridge.P2RoundedFactorDumper

open P2RoundedCanonical

def gridDenominator : ℕ := gridCells + 1

/-- Every emitted rational is known by construction to be on this grid.
`floor` is used only to recover its exact integer numerator. -/
def scaledInteger (q : ℚ) : ℤ :=
  Rat.floor (q * gridDenominator)

def coefficientString (p : DenseRatPoly.Poly) : String :=
  String.intercalate "," (p.map (toString ∘ scaledInteger))

def emitDefect (k : Fin 32) : IO Unit := do
  let a := normalizedDefectApprox k
  IO.println s!"D|{k.val}|{scaledInteger a.error}|{coefficientString a.coeffs}"

def emitComponent
    (tag : String) (kind : P2SelectedKind) (k : Fin 32) (i : Fin 24) :
    IO Unit := do
  let a := normalizedComponentApprox kind i k
  IO.println
    s!"C|{tag}|{k.val}|{i.val}|{scaledInteger a.error}|{coefficientString a.coeffs}"

def run : IO Unit := do
  IO.println s!"S|{gridDenominator}"
  for k in List.finRange 32 do
    emitDefect k
    for i in List.finRange 24 do
      emitComponent "E" .even k i
      emitComponent "O" .odd k i

end RHP2Bridge.P2RoundedFactorDumper

def main : IO Unit := RHP2Bridge.P2RoundedFactorDumper.run
