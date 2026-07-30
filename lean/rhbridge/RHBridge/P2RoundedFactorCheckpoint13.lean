import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck13_0
import RHBridge.P2RoundedFactorCheckpointCheck13_1
import RHBridge.P2RoundedFactorCheckpointCheck13_2
import RHBridge.P2RoundedFactorCheckpointCheck13_3
import RHBridge.P2RoundedFactorCheckpointCheck13_4
import RHBridge.P2RoundedFactorCheckpointCheck13_5
import RHBridge.P2RoundedFactorCheckpointCheck13_6
import RHBridge.P2RoundedFactorCheckpointCheck13_7
import RHBridge.P2RoundedFactorCheckpointCheck13_8
import RHBridge.P2RoundedFactorCheckpointCheck13_9
import RHBridge.P2RoundedFactorCheckpointCheck13_10
import RHBridge.P2RoundedFactorCheckpointCheck13_11
import RHBridge.P2RoundedFactorCheckpointCheck13_12
import RHBridge.P2RoundedFactorCheckpointCheck13_13
import RHBridge.P2RoundedFactorCheckpointCheck13_14
import RHBridge.P2RoundedFactorCheckpointCheck13_15
import RHBridge.P2RoundedFactorCheckpointCheck13_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel13PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨13, by decide⟩ := by
  fin_cases i
  · exact panel13Prefix0_eq
  · exact panel13Prefix1_eq
  · exact panel13Prefix2_eq
  · exact panel13Prefix3_eq
  · exact panel13Prefix4_eq
  · exact panel13Prefix5_eq
  · exact panel13Prefix6_eq
  · exact panel13Prefix7_eq
  · exact panel13Prefix8_eq
  · exact panel13Prefix9_eq
  · exact panel13Prefix10_eq
  · exact panel13Prefix11_eq
  · exact panel13Prefix12_eq
  · exact panel13Prefix13_eq
  · exact panel13Prefix14_eq
  · exact panel13Prefix15_eq
  · exact panel13Prefix16_eq
  · exact panel13Prefix17_eq
  · exact panel13Prefix18_eq
  · exact panel13Prefix19_eq
  · exact panel13Prefix20_eq
  · exact panel13Prefix21_eq
  · exact panel13Prefix22_eq
  · exact panel13Prefix23_eq
  · exact panel13Prefix24_eq
  · exact panel13Prefix25_eq
  · exact panel13Prefix26_eq
  · exact panel13Prefix27_eq
  · exact panel13Prefix28_eq
  · exact panel13Prefix29_eq
  · exact panel13Prefix30_eq
  · exact panel13Prefix31_eq
  · exact panel13Prefix32_eq
  · exact panel13Prefix33_eq
  · exact panel13Prefix34_eq
  · exact panel13Prefix35_eq
  · exact panel13Prefix36_eq
  · exact panel13Prefix37_eq
  · exact panel13Prefix38_eq
  · exact panel13Prefix39_eq
  · exact panel13Prefix40_eq
  · exact panel13Prefix41_eq
  · exact panel13Prefix42_eq
  · exact panel13Prefix43_eq
  · exact panel13Prefix44_eq
  · exact panel13Prefix45_eq
  · exact panel13Prefix46_eq
  · exact panel13Prefix47_eq
  · exact panel13Prefix48_eq
  · exact panel13Prefix49_eq
  · exact panel13Prefix50_eq
  · exact panel13Prefix51_eq
  · exact panel13Prefix52_eq
  · exact panel13Prefix53_eq
  · exact panel13Prefix54_eq
  · exact panel13Prefix55_eq
  · exact panel13Prefix56_eq
  · exact panel13Prefix57_eq
  · exact panel13Prefix58_eq
  · exact panel13Prefix59_eq
  · exact panel13Prefix60_eq
  · exact panel13Prefix61_eq
  · exact panel13Prefix62_eq
  · exact panel13Prefix63_eq

theorem panel13DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel13DefectPieces.EnclosesCanonical
      ⟨13, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel13DefectPieces,
      Vector.get_ofFn]
    rw [panel13PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨13, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel13DefectPieces]
    rw [panel13Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨13, by decide⟩

theorem panel13Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel13Cache.EnclosesCanonical
      ⟨13, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel13DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
