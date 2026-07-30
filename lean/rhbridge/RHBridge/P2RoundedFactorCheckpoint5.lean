import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck5_0
import RHBridge.P2RoundedFactorCheckpointCheck5_1
import RHBridge.P2RoundedFactorCheckpointCheck5_2
import RHBridge.P2RoundedFactorCheckpointCheck5_3
import RHBridge.P2RoundedFactorCheckpointCheck5_4
import RHBridge.P2RoundedFactorCheckpointCheck5_5
import RHBridge.P2RoundedFactorCheckpointCheck5_6
import RHBridge.P2RoundedFactorCheckpointCheck5_7
import RHBridge.P2RoundedFactorCheckpointCheck5_8
import RHBridge.P2RoundedFactorCheckpointCheck5_9
import RHBridge.P2RoundedFactorCheckpointCheck5_10
import RHBridge.P2RoundedFactorCheckpointCheck5_11
import RHBridge.P2RoundedFactorCheckpointCheck5_12
import RHBridge.P2RoundedFactorCheckpointCheck5_13
import RHBridge.P2RoundedFactorCheckpointCheck5_14
import RHBridge.P2RoundedFactorCheckpointCheck5_15
import RHBridge.P2RoundedFactorCheckpointCheck5_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel5PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨5, by decide⟩ := by
  fin_cases i
  · exact panel5Prefix0_eq
  · exact panel5Prefix1_eq
  · exact panel5Prefix2_eq
  · exact panel5Prefix3_eq
  · exact panel5Prefix4_eq
  · exact panel5Prefix5_eq
  · exact panel5Prefix6_eq
  · exact panel5Prefix7_eq
  · exact panel5Prefix8_eq
  · exact panel5Prefix9_eq
  · exact panel5Prefix10_eq
  · exact panel5Prefix11_eq
  · exact panel5Prefix12_eq
  · exact panel5Prefix13_eq
  · exact panel5Prefix14_eq
  · exact panel5Prefix15_eq
  · exact panel5Prefix16_eq
  · exact panel5Prefix17_eq
  · exact panel5Prefix18_eq
  · exact panel5Prefix19_eq
  · exact panel5Prefix20_eq
  · exact panel5Prefix21_eq
  · exact panel5Prefix22_eq
  · exact panel5Prefix23_eq
  · exact panel5Prefix24_eq
  · exact panel5Prefix25_eq
  · exact panel5Prefix26_eq
  · exact panel5Prefix27_eq
  · exact panel5Prefix28_eq
  · exact panel5Prefix29_eq
  · exact panel5Prefix30_eq
  · exact panel5Prefix31_eq
  · exact panel5Prefix32_eq
  · exact panel5Prefix33_eq
  · exact panel5Prefix34_eq
  · exact panel5Prefix35_eq
  · exact panel5Prefix36_eq
  · exact panel5Prefix37_eq
  · exact panel5Prefix38_eq
  · exact panel5Prefix39_eq
  · exact panel5Prefix40_eq
  · exact panel5Prefix41_eq
  · exact panel5Prefix42_eq
  · exact panel5Prefix43_eq
  · exact panel5Prefix44_eq
  · exact panel5Prefix45_eq
  · exact panel5Prefix46_eq
  · exact panel5Prefix47_eq
  · exact panel5Prefix48_eq
  · exact panel5Prefix49_eq
  · exact panel5Prefix50_eq
  · exact panel5Prefix51_eq
  · exact panel5Prefix52_eq
  · exact panel5Prefix53_eq
  · exact panel5Prefix54_eq
  · exact panel5Prefix55_eq
  · exact panel5Prefix56_eq
  · exact panel5Prefix57_eq
  · exact panel5Prefix58_eq
  · exact panel5Prefix59_eq
  · exact panel5Prefix60_eq
  · exact panel5Prefix61_eq
  · exact panel5Prefix62_eq
  · exact panel5Prefix63_eq

theorem panel5DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel5DefectPieces.EnclosesCanonical
      ⟨5, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel5DefectPieces,
      Vector.get_ofFn]
    rw [panel5PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨5, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel5DefectPieces]
    rw [panel5Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨5, by decide⟩

theorem panel5Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel5Cache.EnclosesCanonical
      ⟨5, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel5DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
