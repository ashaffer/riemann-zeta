import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck8_0
import RHBridge.P2RoundedFactorCheckpointCheck8_1
import RHBridge.P2RoundedFactorCheckpointCheck8_2
import RHBridge.P2RoundedFactorCheckpointCheck8_3
import RHBridge.P2RoundedFactorCheckpointCheck8_4
import RHBridge.P2RoundedFactorCheckpointCheck8_5
import RHBridge.P2RoundedFactorCheckpointCheck8_6
import RHBridge.P2RoundedFactorCheckpointCheck8_7
import RHBridge.P2RoundedFactorCheckpointCheck8_8
import RHBridge.P2RoundedFactorCheckpointCheck8_9
import RHBridge.P2RoundedFactorCheckpointCheck8_10
import RHBridge.P2RoundedFactorCheckpointCheck8_11
import RHBridge.P2RoundedFactorCheckpointCheck8_12
import RHBridge.P2RoundedFactorCheckpointCheck8_13
import RHBridge.P2RoundedFactorCheckpointCheck8_14
import RHBridge.P2RoundedFactorCheckpointCheck8_15
import RHBridge.P2RoundedFactorCheckpointCheck8_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel8PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨8, by decide⟩ := by
  fin_cases i
  · exact panel8Prefix0_eq
  · exact panel8Prefix1_eq
  · exact panel8Prefix2_eq
  · exact panel8Prefix3_eq
  · exact panel8Prefix4_eq
  · exact panel8Prefix5_eq
  · exact panel8Prefix6_eq
  · exact panel8Prefix7_eq
  · exact panel8Prefix8_eq
  · exact panel8Prefix9_eq
  · exact panel8Prefix10_eq
  · exact panel8Prefix11_eq
  · exact panel8Prefix12_eq
  · exact panel8Prefix13_eq
  · exact panel8Prefix14_eq
  · exact panel8Prefix15_eq
  · exact panel8Prefix16_eq
  · exact panel8Prefix17_eq
  · exact panel8Prefix18_eq
  · exact panel8Prefix19_eq
  · exact panel8Prefix20_eq
  · exact panel8Prefix21_eq
  · exact panel8Prefix22_eq
  · exact panel8Prefix23_eq
  · exact panel8Prefix24_eq
  · exact panel8Prefix25_eq
  · exact panel8Prefix26_eq
  · exact panel8Prefix27_eq
  · exact panel8Prefix28_eq
  · exact panel8Prefix29_eq
  · exact panel8Prefix30_eq
  · exact panel8Prefix31_eq
  · exact panel8Prefix32_eq
  · exact panel8Prefix33_eq
  · exact panel8Prefix34_eq
  · exact panel8Prefix35_eq
  · exact panel8Prefix36_eq
  · exact panel8Prefix37_eq
  · exact panel8Prefix38_eq
  · exact panel8Prefix39_eq
  · exact panel8Prefix40_eq
  · exact panel8Prefix41_eq
  · exact panel8Prefix42_eq
  · exact panel8Prefix43_eq
  · exact panel8Prefix44_eq
  · exact panel8Prefix45_eq
  · exact panel8Prefix46_eq
  · exact panel8Prefix47_eq
  · exact panel8Prefix48_eq
  · exact panel8Prefix49_eq
  · exact panel8Prefix50_eq
  · exact panel8Prefix51_eq
  · exact panel8Prefix52_eq
  · exact panel8Prefix53_eq
  · exact panel8Prefix54_eq
  · exact panel8Prefix55_eq
  · exact panel8Prefix56_eq
  · exact panel8Prefix57_eq
  · exact panel8Prefix58_eq
  · exact panel8Prefix59_eq
  · exact panel8Prefix60_eq
  · exact panel8Prefix61_eq
  · exact panel8Prefix62_eq
  · exact panel8Prefix63_eq

theorem panel8DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel8DefectPieces.EnclosesCanonical
      ⟨8, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel8DefectPieces,
      Vector.get_ofFn]
    rw [panel8PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨8, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel8DefectPieces]
    rw [panel8Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨8, by decide⟩

theorem panel8Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel8Cache.EnclosesCanonical
      ⟨8, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel8DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
