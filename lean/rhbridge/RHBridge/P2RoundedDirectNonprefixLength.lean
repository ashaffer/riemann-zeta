import RHBridge.P2CanonicalRounded

namespace RHP2Bridge.P2RoundedCanonical

open RoundedRatPoly

#eval
  (rounded gridCells 1
    (DenseRatPoly.affine DenseRatPoly.p2RationalNonPrefixPoly
      (p2PanelCenterQ 0) (p2PanelHalfWidthQ 0))).coeffs.length

end RHP2Bridge.P2RoundedCanonical
