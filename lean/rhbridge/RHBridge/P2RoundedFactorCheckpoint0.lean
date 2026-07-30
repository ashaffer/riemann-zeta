import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck0_0
import RHBridge.P2RoundedFactorCheckpointCheck0_1
import RHBridge.P2RoundedFactorCheckpointCheck0_2
import RHBridge.P2RoundedFactorCheckpointCheck0_3
import RHBridge.P2RoundedFactorCheckpointCheck0_4
import RHBridge.P2RoundedFactorCheckpointCheck0_5
import RHBridge.P2RoundedFactorCheckpointCheck0_6
import RHBridge.P2RoundedFactorCheckpointCheck0_7
import RHBridge.P2RoundedFactorCheckpointCheck0_8
import RHBridge.P2RoundedFactorCheckpointCheck0_9
import RHBridge.P2RoundedFactorCheckpointCheck0_10
import RHBridge.P2RoundedFactorCheckpointCheck0_11
import RHBridge.P2RoundedFactorCheckpointCheck0_12
import RHBridge.P2RoundedFactorCheckpointCheck0_13
import RHBridge.P2RoundedFactorCheckpointCheck0_14
import RHBridge.P2RoundedFactorCheckpointCheck0_15
import RHBridge.P2RoundedFactorCheckpointCheck0_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel0PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨0, by decide⟩ := by
  fin_cases i
  · exact panel0Prefix0_eq
  · exact panel0Prefix1_eq
  · exact panel0Prefix2_eq
  · exact panel0Prefix3_eq
  · exact panel0Prefix4_eq
  · exact panel0Prefix5_eq
  · exact panel0Prefix6_eq
  · exact panel0Prefix7_eq
  · exact panel0Prefix8_eq
  · exact panel0Prefix9_eq
  · exact panel0Prefix10_eq
  · exact panel0Prefix11_eq
  · exact panel0Prefix12_eq
  · exact panel0Prefix13_eq
  · exact panel0Prefix14_eq
  · exact panel0Prefix15_eq
  · exact panel0Prefix16_eq
  · exact panel0Prefix17_eq
  · exact panel0Prefix18_eq
  · exact panel0Prefix19_eq
  · exact panel0Prefix20_eq
  · exact panel0Prefix21_eq
  · exact panel0Prefix22_eq
  · exact panel0Prefix23_eq
  · exact panel0Prefix24_eq
  · exact panel0Prefix25_eq
  · exact panel0Prefix26_eq
  · exact panel0Prefix27_eq
  · exact panel0Prefix28_eq
  · exact panel0Prefix29_eq
  · exact panel0Prefix30_eq
  · exact panel0Prefix31_eq
  · exact panel0Prefix32_eq
  · exact panel0Prefix33_eq
  · exact panel0Prefix34_eq
  · exact panel0Prefix35_eq
  · exact panel0Prefix36_eq
  · exact panel0Prefix37_eq
  · exact panel0Prefix38_eq
  · exact panel0Prefix39_eq
  · exact panel0Prefix40_eq
  · exact panel0Prefix41_eq
  · exact panel0Prefix42_eq
  · exact panel0Prefix43_eq
  · exact panel0Prefix44_eq
  · exact panel0Prefix45_eq
  · exact panel0Prefix46_eq
  · exact panel0Prefix47_eq
  · exact panel0Prefix48_eq
  · exact panel0Prefix49_eq
  · exact panel0Prefix50_eq
  · exact panel0Prefix51_eq
  · exact panel0Prefix52_eq
  · exact panel0Prefix53_eq
  · exact panel0Prefix54_eq
  · exact panel0Prefix55_eq
  · exact panel0Prefix56_eq
  · exact panel0Prefix57_eq
  · exact panel0Prefix58_eq
  · exact panel0Prefix59_eq
  · exact panel0Prefix60_eq
  · exact panel0Prefix61_eq
  · exact panel0Prefix62_eq
  · exact panel0Prefix63_eq

theorem panel0DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel0DefectPieces.EnclosesCanonical
      ⟨0, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel0DefectPieces,
      Vector.get_ofFn]
    rw [panel0PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨0, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel0DefectPieces]
    rw [panel0Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨0, by decide⟩

theorem panel0Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel0Cache.EnclosesCanonical
      ⟨0, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel0DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
