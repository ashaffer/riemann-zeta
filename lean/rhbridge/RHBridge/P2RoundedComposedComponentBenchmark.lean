import RHBridge.P2CanonicalRounded

namespace RHP2Bridge.P2RoundedCanonical

open RoundedRatPoly

set_option maxRecDepth 100000
set_option maxHeartbeats 20000000

/-- Bounded-denominator alternative to atomizing the complete exact affine
component. -/
def firstComposedComponentExpr : Expr :=
  .mul (.const (RatPoly.p2SelectedPhaseQ .even 0))
    (.mul (.const (p2SelectedScaleCenterQ .even 0))
      (.comp
        (.atom (DenseRatPoly.sphericalJRealPolynomial 0 100))
        (.atom
          [(7 / 16) * p2PanelCenterQ 0,
            (7 / 16) * p2PanelHalfWidthQ 0])))

def firstComposedComponentApprox : Approx :=
  firstComposedComponentExpr.run gridCells 1

#eval
  let a := firstComposedComponentApprox
  (a.coeffs.length,
    decide (a.error < 1 / 10 ^ 100),
    decide (a.error < 1 / 10 ^ 150))

end RHP2Bridge.P2RoundedCanonical
