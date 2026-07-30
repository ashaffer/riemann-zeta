import RHBridge.P2PoleCoefficientCertificateCheck0
import RHBridge.P2PoleCoefficientCertificateCheck1
import RHBridge.P2PoleCoefficientCertificateCheck2
import RHBridge.P2PoleCoefficientCertificateCheck3
import RHBridge.P2PoleCoefficientCertificateCheck4
import RHBridge.P2PoleCoefficientCertificateCheck5
import RHBridge.P2PoleCoefficientCertificateCheck6
import RHBridge.P2PoleCoefficientCertificateCheck7

namespace RHP2Bridge

theorem p2PoleCoeffCertificate (n : Fin 48) :
    DenseRatPoly.p2PoleTaylorCoeffScaleCenterQ n =
      P2PoleCoefficientCertificateData.poleCoeffQ n := by
  fin_cases n
  · exact p2PoleCoeffCertificate0
  · exact p2PoleCoeffCertificate1
  · exact p2PoleCoeffCertificate2
  · exact p2PoleCoeffCertificate3
  · exact p2PoleCoeffCertificate4
  · exact p2PoleCoeffCertificate5
  · exact p2PoleCoeffCertificate6
  · exact p2PoleCoeffCertificate7
  · exact p2PoleCoeffCertificate8
  · exact p2PoleCoeffCertificate9
  · exact p2PoleCoeffCertificate10
  · exact p2PoleCoeffCertificate11
  · exact p2PoleCoeffCertificate12
  · exact p2PoleCoeffCertificate13
  · exact p2PoleCoeffCertificate14
  · exact p2PoleCoeffCertificate15
  · exact p2PoleCoeffCertificate16
  · exact p2PoleCoeffCertificate17
  · exact p2PoleCoeffCertificate18
  · exact p2PoleCoeffCertificate19
  · exact p2PoleCoeffCertificate20
  · exact p2PoleCoeffCertificate21
  · exact p2PoleCoeffCertificate22
  · exact p2PoleCoeffCertificate23
  · exact p2PoleCoeffCertificate24
  · exact p2PoleCoeffCertificate25
  · exact p2PoleCoeffCertificate26
  · exact p2PoleCoeffCertificate27
  · exact p2PoleCoeffCertificate28
  · exact p2PoleCoeffCertificate29
  · exact p2PoleCoeffCertificate30
  · exact p2PoleCoeffCertificate31
  · exact p2PoleCoeffCertificate32
  · exact p2PoleCoeffCertificate33
  · exact p2PoleCoeffCertificate34
  · exact p2PoleCoeffCertificate35
  · exact p2PoleCoeffCertificate36
  · exact p2PoleCoeffCertificate37
  · exact p2PoleCoeffCertificate38
  · exact p2PoleCoeffCertificate39
  · exact p2PoleCoeffCertificate40
  · exact p2PoleCoeffCertificate41
  · exact p2PoleCoeffCertificate42
  · exact p2PoleCoeffCertificate43
  · exact p2PoleCoeffCertificate44
  · exact p2PoleCoeffCertificate45
  · exact p2PoleCoeffCertificate46
  · exact p2PoleCoeffCertificate47

end RHP2Bridge
