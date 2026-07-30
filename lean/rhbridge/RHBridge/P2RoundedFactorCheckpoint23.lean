import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck23_0
import RHBridge.P2RoundedFactorCheckpointCheck23_1
import RHBridge.P2RoundedFactorCheckpointCheck23_2
import RHBridge.P2RoundedFactorCheckpointCheck23_3
import RHBridge.P2RoundedFactorCheckpointCheck23_4
import RHBridge.P2RoundedFactorCheckpointCheck23_5
import RHBridge.P2RoundedFactorCheckpointCheck23_6
import RHBridge.P2RoundedFactorCheckpointCheck23_7
import RHBridge.P2RoundedFactorCheckpointCheck23_8
import RHBridge.P2RoundedFactorCheckpointCheck23_9
import RHBridge.P2RoundedFactorCheckpointCheck23_10
import RHBridge.P2RoundedFactorCheckpointCheck23_11
import RHBridge.P2RoundedFactorCheckpointCheck23_12
import RHBridge.P2RoundedFactorCheckpointCheck23_13
import RHBridge.P2RoundedFactorCheckpointCheck23_14
import RHBridge.P2RoundedFactorCheckpointCheck23_15
import RHBridge.P2RoundedFactorCheckpointCheck23_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel23PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨23, by decide⟩ := by
  fin_cases i
  · exact panel23Prefix0_eq
  · exact panel23Prefix1_eq
  · exact panel23Prefix2_eq
  · exact panel23Prefix3_eq
  · exact panel23Prefix4_eq
  · exact panel23Prefix5_eq
  · exact panel23Prefix6_eq
  · exact panel23Prefix7_eq
  · exact panel23Prefix8_eq
  · exact panel23Prefix9_eq
  · exact panel23Prefix10_eq
  · exact panel23Prefix11_eq
  · exact panel23Prefix12_eq
  · exact panel23Prefix13_eq
  · exact panel23Prefix14_eq
  · exact panel23Prefix15_eq
  · exact panel23Prefix16_eq
  · exact panel23Prefix17_eq
  · exact panel23Prefix18_eq
  · exact panel23Prefix19_eq
  · exact panel23Prefix20_eq
  · exact panel23Prefix21_eq
  · exact panel23Prefix22_eq
  · exact panel23Prefix23_eq
  · exact panel23Prefix24_eq
  · exact panel23Prefix25_eq
  · exact panel23Prefix26_eq
  · exact panel23Prefix27_eq
  · exact panel23Prefix28_eq
  · exact panel23Prefix29_eq
  · exact panel23Prefix30_eq
  · exact panel23Prefix31_eq
  · exact panel23Prefix32_eq
  · exact panel23Prefix33_eq
  · exact panel23Prefix34_eq
  · exact panel23Prefix35_eq
  · exact panel23Prefix36_eq
  · exact panel23Prefix37_eq
  · exact panel23Prefix38_eq
  · exact panel23Prefix39_eq
  · exact panel23Prefix40_eq
  · exact panel23Prefix41_eq
  · exact panel23Prefix42_eq
  · exact panel23Prefix43_eq
  · exact panel23Prefix44_eq
  · exact panel23Prefix45_eq
  · exact panel23Prefix46_eq
  · exact panel23Prefix47_eq
  · exact panel23Prefix48_eq
  · exact panel23Prefix49_eq
  · exact panel23Prefix50_eq
  · exact panel23Prefix51_eq
  · exact panel23Prefix52_eq
  · exact panel23Prefix53_eq
  · exact panel23Prefix54_eq
  · exact panel23Prefix55_eq
  · exact panel23Prefix56_eq
  · exact panel23Prefix57_eq
  · exact panel23Prefix58_eq
  · exact panel23Prefix59_eq
  · exact panel23Prefix60_eq
  · exact panel23Prefix61_eq
  · exact panel23Prefix62_eq
  · exact panel23Prefix63_eq

theorem panel23DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel23DefectPieces.EnclosesCanonical
      ⟨23, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel23DefectPieces,
      Vector.get_ofFn]
    rw [panel23PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨23, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel23DefectPieces]
    rw [panel23Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨23, by decide⟩

theorem panel23Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel23Cache.EnclosesCanonical
      ⟨23, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel23DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
