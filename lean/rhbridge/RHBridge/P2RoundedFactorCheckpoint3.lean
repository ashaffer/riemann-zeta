import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck3_0
import RHBridge.P2RoundedFactorCheckpointCheck3_1
import RHBridge.P2RoundedFactorCheckpointCheck3_2
import RHBridge.P2RoundedFactorCheckpointCheck3_3
import RHBridge.P2RoundedFactorCheckpointCheck3_4
import RHBridge.P2RoundedFactorCheckpointCheck3_5
import RHBridge.P2RoundedFactorCheckpointCheck3_6
import RHBridge.P2RoundedFactorCheckpointCheck3_7
import RHBridge.P2RoundedFactorCheckpointCheck3_8
import RHBridge.P2RoundedFactorCheckpointCheck3_9
import RHBridge.P2RoundedFactorCheckpointCheck3_10
import RHBridge.P2RoundedFactorCheckpointCheck3_11
import RHBridge.P2RoundedFactorCheckpointCheck3_12
import RHBridge.P2RoundedFactorCheckpointCheck3_13
import RHBridge.P2RoundedFactorCheckpointCheck3_14
import RHBridge.P2RoundedFactorCheckpointCheck3_15
import RHBridge.P2RoundedFactorCheckpointCheck3_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel3PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel3PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨3, by decide⟩ := by
  fin_cases i
  · exact panel3Prefix0_eq
  · exact panel3Prefix1_eq
  · exact panel3Prefix2_eq
  · exact panel3Prefix3_eq
  · exact panel3Prefix4_eq
  · exact panel3Prefix5_eq
  · exact panel3Prefix6_eq
  · exact panel3Prefix7_eq
  · exact panel3Prefix8_eq
  · exact panel3Prefix9_eq
  · exact panel3Prefix10_eq
  · exact panel3Prefix11_eq
  · exact panel3Prefix12_eq
  · exact panel3Prefix13_eq
  · exact panel3Prefix14_eq
  · exact panel3Prefix15_eq
  · exact panel3Prefix16_eq
  · exact panel3Prefix17_eq
  · exact panel3Prefix18_eq
  · exact panel3Prefix19_eq
  · exact panel3Prefix20_eq
  · exact panel3Prefix21_eq
  · exact panel3Prefix22_eq
  · exact panel3Prefix23_eq
  · exact panel3Prefix24_eq
  · exact panel3Prefix25_eq
  · exact panel3Prefix26_eq
  · exact panel3Prefix27_eq
  · exact panel3Prefix28_eq
  · exact panel3Prefix29_eq
  · exact panel3Prefix30_eq
  · exact panel3Prefix31_eq
  · exact panel3Prefix32_eq
  · exact panel3Prefix33_eq
  · exact panel3Prefix34_eq
  · exact panel3Prefix35_eq
  · exact panel3Prefix36_eq
  · exact panel3Prefix37_eq
  · exact panel3Prefix38_eq
  · exact panel3Prefix39_eq
  · exact panel3Prefix40_eq
  · exact panel3Prefix41_eq
  · exact panel3Prefix42_eq
  · exact panel3Prefix43_eq
  · exact panel3Prefix44_eq
  · exact panel3Prefix45_eq
  · exact panel3Prefix46_eq
  · exact panel3Prefix47_eq
  · exact panel3Prefix48_eq
  · exact panel3Prefix49_eq
  · exact panel3Prefix50_eq
  · exact panel3Prefix51_eq
  · exact panel3Prefix52_eq
  · exact panel3Prefix53_eq
  · exact panel3Prefix54_eq
  · exact panel3Prefix55_eq
  · exact panel3Prefix56_eq
  · exact panel3Prefix57_eq
  · exact panel3Prefix58_eq
  · exact panel3Prefix59_eq
  · exact panel3Prefix60_eq
  · exact panel3Prefix61_eq
  · exact panel3Prefix62_eq
  · exact panel3Prefix63_eq

theorem panel3DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel3DefectPieces.EnclosesCanonical
      ⟨3, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel3DefectPieces,
      Vector.get_ofFn]
    rw [panel3PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨3, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel3DefectPieces]
    rw [panel3Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨3, by decide⟩

theorem panel3Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel3Cache.EnclosesCanonical
      ⟨3, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel3DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
