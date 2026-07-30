import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck20_0
import RHBridge.P2RoundedFactorCheckpointCheck20_1
import RHBridge.P2RoundedFactorCheckpointCheck20_2
import RHBridge.P2RoundedFactorCheckpointCheck20_3
import RHBridge.P2RoundedFactorCheckpointCheck20_4
import RHBridge.P2RoundedFactorCheckpointCheck20_5
import RHBridge.P2RoundedFactorCheckpointCheck20_6
import RHBridge.P2RoundedFactorCheckpointCheck20_7
import RHBridge.P2RoundedFactorCheckpointCheck20_8
import RHBridge.P2RoundedFactorCheckpointCheck20_9
import RHBridge.P2RoundedFactorCheckpointCheck20_10
import RHBridge.P2RoundedFactorCheckpointCheck20_11
import RHBridge.P2RoundedFactorCheckpointCheck20_12
import RHBridge.P2RoundedFactorCheckpointCheck20_13
import RHBridge.P2RoundedFactorCheckpointCheck20_14
import RHBridge.P2RoundedFactorCheckpointCheck20_15
import RHBridge.P2RoundedFactorCheckpointCheck20_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel20PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨20, by decide⟩ := by
  fin_cases i
  · exact panel20Prefix0_eq
  · exact panel20Prefix1_eq
  · exact panel20Prefix2_eq
  · exact panel20Prefix3_eq
  · exact panel20Prefix4_eq
  · exact panel20Prefix5_eq
  · exact panel20Prefix6_eq
  · exact panel20Prefix7_eq
  · exact panel20Prefix8_eq
  · exact panel20Prefix9_eq
  · exact panel20Prefix10_eq
  · exact panel20Prefix11_eq
  · exact panel20Prefix12_eq
  · exact panel20Prefix13_eq
  · exact panel20Prefix14_eq
  · exact panel20Prefix15_eq
  · exact panel20Prefix16_eq
  · exact panel20Prefix17_eq
  · exact panel20Prefix18_eq
  · exact panel20Prefix19_eq
  · exact panel20Prefix20_eq
  · exact panel20Prefix21_eq
  · exact panel20Prefix22_eq
  · exact panel20Prefix23_eq
  · exact panel20Prefix24_eq
  · exact panel20Prefix25_eq
  · exact panel20Prefix26_eq
  · exact panel20Prefix27_eq
  · exact panel20Prefix28_eq
  · exact panel20Prefix29_eq
  · exact panel20Prefix30_eq
  · exact panel20Prefix31_eq
  · exact panel20Prefix32_eq
  · exact panel20Prefix33_eq
  · exact panel20Prefix34_eq
  · exact panel20Prefix35_eq
  · exact panel20Prefix36_eq
  · exact panel20Prefix37_eq
  · exact panel20Prefix38_eq
  · exact panel20Prefix39_eq
  · exact panel20Prefix40_eq
  · exact panel20Prefix41_eq
  · exact panel20Prefix42_eq
  · exact panel20Prefix43_eq
  · exact panel20Prefix44_eq
  · exact panel20Prefix45_eq
  · exact panel20Prefix46_eq
  · exact panel20Prefix47_eq
  · exact panel20Prefix48_eq
  · exact panel20Prefix49_eq
  · exact panel20Prefix50_eq
  · exact panel20Prefix51_eq
  · exact panel20Prefix52_eq
  · exact panel20Prefix53_eq
  · exact panel20Prefix54_eq
  · exact panel20Prefix55_eq
  · exact panel20Prefix56_eq
  · exact panel20Prefix57_eq
  · exact panel20Prefix58_eq
  · exact panel20Prefix59_eq
  · exact panel20Prefix60_eq
  · exact panel20Prefix61_eq
  · exact panel20Prefix62_eq
  · exact panel20Prefix63_eq

theorem panel20DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel20DefectPieces.EnclosesCanonical
      ⟨20, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel20DefectPieces,
      Vector.get_ofFn]
    rw [panel20PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨20, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel20DefectPieces]
    rw [panel20Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨20, by decide⟩

theorem panel20Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel20Cache.EnclosesCanonical
      ⟨20, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel20DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
