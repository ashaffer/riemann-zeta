import RHBridge.P2CanonicalRounded

open RHP2Bridge RHP2Bridge.P2RoundedCanonical

def main : IO Unit := do
  IO.println (repr ((1 : ℚ) / 3))
  IO.println (repr (RHP2Bridge.RoundedRatPoly.rounded gridCells 1 [1 / 3, -2 / 7]))
