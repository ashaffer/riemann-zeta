import RHBridge.P2PoleCoefficientCertificateData
import RHBridge.P2PoleCanonicalDense

namespace RHP2Bridge

set_option maxRecDepth 100000

theorem p2PoleCoeffCertificate0 :
    DenseRatPoly.p2PoleTaylorCoeffScaleCenterQ
        ⟨0, by decide⟩ =
      P2PoleCoefficientCertificateData.poleCoeffQ
        ⟨0, by decide⟩ := by
  decide +kernel

theorem p2PoleCoeffCertificate1 :
    DenseRatPoly.p2PoleTaylorCoeffScaleCenterQ
        ⟨1, by decide⟩ =
      P2PoleCoefficientCertificateData.poleCoeffQ
        ⟨1, by decide⟩ := by
  decide +kernel

theorem p2PoleCoeffCertificate2 :
    DenseRatPoly.p2PoleTaylorCoeffScaleCenterQ
        ⟨2, by decide⟩ =
      P2PoleCoefficientCertificateData.poleCoeffQ
        ⟨2, by decide⟩ := by
  decide +kernel

theorem p2PoleCoeffCertificate3 :
    DenseRatPoly.p2PoleTaylorCoeffScaleCenterQ
        ⟨3, by decide⟩ =
      P2PoleCoefficientCertificateData.poleCoeffQ
        ⟨3, by decide⟩ := by
  decide +kernel

theorem p2PoleCoeffCertificate4 :
    DenseRatPoly.p2PoleTaylorCoeffScaleCenterQ
        ⟨4, by decide⟩ =
      P2PoleCoefficientCertificateData.poleCoeffQ
        ⟨4, by decide⟩ := by
  decide +kernel

theorem p2PoleCoeffCertificate5 :
    DenseRatPoly.p2PoleTaylorCoeffScaleCenterQ
        ⟨5, by decide⟩ =
      P2PoleCoefficientCertificateData.poleCoeffQ
        ⟨5, by decide⟩ := by
  decide +kernel

end RHP2Bridge
