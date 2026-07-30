import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck7_0
import RHBridge.P2RoundedFactorCheckpointCheck7_1
import RHBridge.P2RoundedFactorCheckpointCheck7_2
import RHBridge.P2RoundedFactorCheckpointCheck7_3
import RHBridge.P2RoundedFactorCheckpointCheck7_4
import RHBridge.P2RoundedFactorCheckpointCheck7_5
import RHBridge.P2RoundedFactorCheckpointCheck7_6
import RHBridge.P2RoundedFactorCheckpointCheck7_7
import RHBridge.P2RoundedFactorCheckpointCheck7_8
import RHBridge.P2RoundedFactorCheckpointCheck7_9
import RHBridge.P2RoundedFactorCheckpointCheck7_10
import RHBridge.P2RoundedFactorCheckpointCheck7_11
import RHBridge.P2RoundedFactorCheckpointCheck7_12
import RHBridge.P2RoundedFactorCheckpointCheck7_13
import RHBridge.P2RoundedFactorCheckpointCheck7_14
import RHBridge.P2RoundedFactorCheckpointCheck7_15
import RHBridge.P2RoundedFactorCheckpointCheck7_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel7PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨7, by decide⟩ := by
  fin_cases i
  · exact panel7Prefix0_eq
  · exact panel7Prefix1_eq
  · exact panel7Prefix2_eq
  · exact panel7Prefix3_eq
  · exact panel7Prefix4_eq
  · exact panel7Prefix5_eq
  · exact panel7Prefix6_eq
  · exact panel7Prefix7_eq
  · exact panel7Prefix8_eq
  · exact panel7Prefix9_eq
  · exact panel7Prefix10_eq
  · exact panel7Prefix11_eq
  · exact panel7Prefix12_eq
  · exact panel7Prefix13_eq
  · exact panel7Prefix14_eq
  · exact panel7Prefix15_eq
  · exact panel7Prefix16_eq
  · exact panel7Prefix17_eq
  · exact panel7Prefix18_eq
  · exact panel7Prefix19_eq
  · exact panel7Prefix20_eq
  · exact panel7Prefix21_eq
  · exact panel7Prefix22_eq
  · exact panel7Prefix23_eq
  · exact panel7Prefix24_eq
  · exact panel7Prefix25_eq
  · exact panel7Prefix26_eq
  · exact panel7Prefix27_eq
  · exact panel7Prefix28_eq
  · exact panel7Prefix29_eq
  · exact panel7Prefix30_eq
  · exact panel7Prefix31_eq
  · exact panel7Prefix32_eq
  · exact panel7Prefix33_eq
  · exact panel7Prefix34_eq
  · exact panel7Prefix35_eq
  · exact panel7Prefix36_eq
  · exact panel7Prefix37_eq
  · exact panel7Prefix38_eq
  · exact panel7Prefix39_eq
  · exact panel7Prefix40_eq
  · exact panel7Prefix41_eq
  · exact panel7Prefix42_eq
  · exact panel7Prefix43_eq
  · exact panel7Prefix44_eq
  · exact panel7Prefix45_eq
  · exact panel7Prefix46_eq
  · exact panel7Prefix47_eq
  · exact panel7Prefix48_eq
  · exact panel7Prefix49_eq
  · exact panel7Prefix50_eq
  · exact panel7Prefix51_eq
  · exact panel7Prefix52_eq
  · exact panel7Prefix53_eq
  · exact panel7Prefix54_eq
  · exact panel7Prefix55_eq
  · exact panel7Prefix56_eq
  · exact panel7Prefix57_eq
  · exact panel7Prefix58_eq
  · exact panel7Prefix59_eq
  · exact panel7Prefix60_eq
  · exact panel7Prefix61_eq
  · exact panel7Prefix62_eq
  · exact panel7Prefix63_eq

theorem panel7DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel7DefectPieces.EnclosesCanonical
      ⟨7, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel7DefectPieces,
      Vector.get_ofFn]
    rw [panel7PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨7, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel7DefectPieces]
    rw [panel7Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨7, by decide⟩

theorem panel7Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel7Cache.EnclosesCanonical
      ⟨7, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel7DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
