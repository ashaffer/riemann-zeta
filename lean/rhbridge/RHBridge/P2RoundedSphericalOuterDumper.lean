import RHBridge.P2CanonicalRounded

namespace RHP2Bridge.P2RoundedSphericalOuterDumper

open P2RoundedCanonical RoundedRatPoly

def outerCells : ℕ := 10 ^ 300 - 1
def outerDenominator : ℕ := outerCells + 1

def outerApprox (n : Fin 48) : Approx :=
  rounded outerCells 22
    (DenseRatPoly.sphericalJRealPolynomial n.val 100)

def scaledInteger (q : ℚ) : ℤ :=
  Rat.floor (q * outerDenominator)

def coefficientString (p : DenseRatPoly.Poly) : String :=
  String.intercalate "," (p.map (toString ∘ scaledInteger))

def run : IO Unit := do
  IO.println s!"S|{outerDenominator}"
  for n in List.finRange 48 do
    let a := outerApprox n
    IO.println
      s!"J|{n.val}|{scaledInteger a.error}|{coefficientString a.coeffs}"

end RHP2Bridge.P2RoundedSphericalOuterDumper

def main : IO Unit := RHP2Bridge.P2RoundedSphericalOuterDumper.run
