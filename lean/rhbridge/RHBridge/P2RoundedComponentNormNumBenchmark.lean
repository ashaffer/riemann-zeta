import RHBridge.P2CanonicalRounded

namespace RHP2Bridge.P2RoundedCanonical

set_option maxRecDepth 100000
set_option maxHeartbeats 20000000

theorem firstComponentError_normNum :
    (normalizedComponentApprox .even (0 : Fin 24) (0 : Fin 32)).error =
      (46 : ℚ) / 10 ^ 200 := by
  norm_num [normalizedComponentApprox, normalizedComponentExpr, Expr.run,
    RoundedRatPoly.rounded, RoundedRatPoly.errorCeil,
    RoundedRatPoly.roundingError, RoundedRatPoly.roundCoeffs,
    RoundedRatPoly.gridRound, RoundedRatPoly.absBound,
    DenseRatPoly.affine, DenseRatPoly.p2SelectedComponent100ScaleCenterPolynomial,
    DenseRatPoly.p2Spherical100PanelPolynomial,
    DenseRatPoly.p2SphericalRealPolynomial,
    DenseRatPoly.sphericalJRealPolynomial]

end RHP2Bridge.P2RoundedCanonical
