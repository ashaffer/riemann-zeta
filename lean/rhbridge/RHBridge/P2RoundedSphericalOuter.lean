import RHBridge.P2RoundedSphericalOuterCheck0
import RHBridge.P2RoundedSphericalOuterCheck1
import RHBridge.P2RoundedSphericalOuterCheck2
import RHBridge.P2RoundedSphericalOuterCheck3
import RHBridge.P2RoundedSphericalOuterCheck4
import RHBridge.P2RoundedSphericalOuterCheck5
import RHBridge.P2RoundedSphericalOuterCheck6
import RHBridge.P2RoundedSphericalOuterCheck7
import RHBridge.P2RoundedSphericalOuterCheck8
import RHBridge.P2RoundedSphericalOuterCheck9
import RHBridge.P2RoundedSphericalOuterCheck10
import RHBridge.P2RoundedSphericalOuterCheck11

namespace RHP2Bridge

open P2RoundedFactorCheckpointData

theorem generatedSphericalOuter_encloses (n : Fin 48) :
    RoundedRatPoly.Encloses 22
      (RoundedRatPoly.evalReal
        (DenseRatPoly.sphericalJRealPolynomial n.val 100))
      (sphericalOuter n) := by
  fin_cases n
  · rw [sphericalOuter, sphericalOuter0_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter1_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter2_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter3_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter4_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter5_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter6_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter7_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter8_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter9_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter10_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter11_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter12_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter13_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter14_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter15_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter16_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter17_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter18_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter19_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter20_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter21_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter22_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter23_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter24_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter25_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter26_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter27_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter28_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter29_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter30_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter31_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter32_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter33_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter34_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter35_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter36_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter37_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter38_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter39_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter40_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter41_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter42_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter43_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter44_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter45_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter46_eq]
    exact computedSphericalOuter_encloses _
  · rw [sphericalOuter, sphericalOuter47_eq]
    exact computedSphericalOuter_encloses _

theorem generatedSphericalOuters_enclose :
    P2RoundedSharedEvaluator.SphericalOutersEnclose
      sphericalOuters := by
  constructor
  intro n
  simpa [sphericalOuters,
    P2RoundedSharedEvaluator.sphericalOuterExact] using
      generatedSphericalOuter_encloses n

end RHP2Bridge
