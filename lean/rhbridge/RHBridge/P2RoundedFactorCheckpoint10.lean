import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck10_0
import RHBridge.P2RoundedFactorCheckpointCheck10_1
import RHBridge.P2RoundedFactorCheckpointCheck10_2
import RHBridge.P2RoundedFactorCheckpointCheck10_3
import RHBridge.P2RoundedFactorCheckpointCheck10_4
import RHBridge.P2RoundedFactorCheckpointCheck10_5
import RHBridge.P2RoundedFactorCheckpointCheck10_6
import RHBridge.P2RoundedFactorCheckpointCheck10_7
import RHBridge.P2RoundedFactorCheckpointCheck10_8
import RHBridge.P2RoundedFactorCheckpointCheck10_9
import RHBridge.P2RoundedFactorCheckpointCheck10_10
import RHBridge.P2RoundedFactorCheckpointCheck10_11
import RHBridge.P2RoundedFactorCheckpointCheck10_12
import RHBridge.P2RoundedFactorCheckpointCheck10_13
import RHBridge.P2RoundedFactorCheckpointCheck10_14
import RHBridge.P2RoundedFactorCheckpointCheck10_15
import RHBridge.P2RoundedFactorCheckpointCheck10_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel10PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel10PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨10, by decide⟩ := by
  fin_cases i
  · exact panel10Prefix0_eq
  · exact panel10Prefix1_eq
  · exact panel10Prefix2_eq
  · exact panel10Prefix3_eq
  · exact panel10Prefix4_eq
  · exact panel10Prefix5_eq
  · exact panel10Prefix6_eq
  · exact panel10Prefix7_eq
  · exact panel10Prefix8_eq
  · exact panel10Prefix9_eq
  · exact panel10Prefix10_eq
  · exact panel10Prefix11_eq
  · exact panel10Prefix12_eq
  · exact panel10Prefix13_eq
  · exact panel10Prefix14_eq
  · exact panel10Prefix15_eq
  · exact panel10Prefix16_eq
  · exact panel10Prefix17_eq
  · exact panel10Prefix18_eq
  · exact panel10Prefix19_eq
  · exact panel10Prefix20_eq
  · exact panel10Prefix21_eq
  · exact panel10Prefix22_eq
  · exact panel10Prefix23_eq
  · exact panel10Prefix24_eq
  · exact panel10Prefix25_eq
  · exact panel10Prefix26_eq
  · exact panel10Prefix27_eq
  · exact panel10Prefix28_eq
  · exact panel10Prefix29_eq
  · exact panel10Prefix30_eq
  · exact panel10Prefix31_eq
  · exact panel10Prefix32_eq
  · exact panel10Prefix33_eq
  · exact panel10Prefix34_eq
  · exact panel10Prefix35_eq
  · exact panel10Prefix36_eq
  · exact panel10Prefix37_eq
  · exact panel10Prefix38_eq
  · exact panel10Prefix39_eq
  · exact panel10Prefix40_eq
  · exact panel10Prefix41_eq
  · exact panel10Prefix42_eq
  · exact panel10Prefix43_eq
  · exact panel10Prefix44_eq
  · exact panel10Prefix45_eq
  · exact panel10Prefix46_eq
  · exact panel10Prefix47_eq
  · exact panel10Prefix48_eq
  · exact panel10Prefix49_eq
  · exact panel10Prefix50_eq
  · exact panel10Prefix51_eq
  · exact panel10Prefix52_eq
  · exact panel10Prefix53_eq
  · exact panel10Prefix54_eq
  · exact panel10Prefix55_eq
  · exact panel10Prefix56_eq
  · exact panel10Prefix57_eq
  · exact panel10Prefix58_eq
  · exact panel10Prefix59_eq
  · exact panel10Prefix60_eq
  · exact panel10Prefix61_eq
  · exact panel10Prefix62_eq
  · exact panel10Prefix63_eq

theorem panel10DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel10DefectPieces.EnclosesCanonical
      ⟨10, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel10DefectPieces,
      Vector.get_ofFn]
    rw [panel10PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨10, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel10DefectPieces]
    rw [panel10Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨10, by decide⟩

theorem panel10Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel10Cache.EnclosesCanonical
      ⟨10, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel10DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
