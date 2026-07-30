import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck6_0
import RHBridge.P2RoundedFactorCheckpointCheck6_1
import RHBridge.P2RoundedFactorCheckpointCheck6_2
import RHBridge.P2RoundedFactorCheckpointCheck6_3
import RHBridge.P2RoundedFactorCheckpointCheck6_4
import RHBridge.P2RoundedFactorCheckpointCheck6_5
import RHBridge.P2RoundedFactorCheckpointCheck6_6
import RHBridge.P2RoundedFactorCheckpointCheck6_7
import RHBridge.P2RoundedFactorCheckpointCheck6_8
import RHBridge.P2RoundedFactorCheckpointCheck6_9
import RHBridge.P2RoundedFactorCheckpointCheck6_10
import RHBridge.P2RoundedFactorCheckpointCheck6_11
import RHBridge.P2RoundedFactorCheckpointCheck6_12
import RHBridge.P2RoundedFactorCheckpointCheck6_13
import RHBridge.P2RoundedFactorCheckpointCheck6_14
import RHBridge.P2RoundedFactorCheckpointCheck6_15
import RHBridge.P2RoundedFactorCheckpointCheck6_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel6PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨6, by decide⟩ := by
  fin_cases i
  · exact panel6Prefix0_eq
  · exact panel6Prefix1_eq
  · exact panel6Prefix2_eq
  · exact panel6Prefix3_eq
  · exact panel6Prefix4_eq
  · exact panel6Prefix5_eq
  · exact panel6Prefix6_eq
  · exact panel6Prefix7_eq
  · exact panel6Prefix8_eq
  · exact panel6Prefix9_eq
  · exact panel6Prefix10_eq
  · exact panel6Prefix11_eq
  · exact panel6Prefix12_eq
  · exact panel6Prefix13_eq
  · exact panel6Prefix14_eq
  · exact panel6Prefix15_eq
  · exact panel6Prefix16_eq
  · exact panel6Prefix17_eq
  · exact panel6Prefix18_eq
  · exact panel6Prefix19_eq
  · exact panel6Prefix20_eq
  · exact panel6Prefix21_eq
  · exact panel6Prefix22_eq
  · exact panel6Prefix23_eq
  · exact panel6Prefix24_eq
  · exact panel6Prefix25_eq
  · exact panel6Prefix26_eq
  · exact panel6Prefix27_eq
  · exact panel6Prefix28_eq
  · exact panel6Prefix29_eq
  · exact panel6Prefix30_eq
  · exact panel6Prefix31_eq
  · exact panel6Prefix32_eq
  · exact panel6Prefix33_eq
  · exact panel6Prefix34_eq
  · exact panel6Prefix35_eq
  · exact panel6Prefix36_eq
  · exact panel6Prefix37_eq
  · exact panel6Prefix38_eq
  · exact panel6Prefix39_eq
  · exact panel6Prefix40_eq
  · exact panel6Prefix41_eq
  · exact panel6Prefix42_eq
  · exact panel6Prefix43_eq
  · exact panel6Prefix44_eq
  · exact panel6Prefix45_eq
  · exact panel6Prefix46_eq
  · exact panel6Prefix47_eq
  · exact panel6Prefix48_eq
  · exact panel6Prefix49_eq
  · exact panel6Prefix50_eq
  · exact panel6Prefix51_eq
  · exact panel6Prefix52_eq
  · exact panel6Prefix53_eq
  · exact panel6Prefix54_eq
  · exact panel6Prefix55_eq
  · exact panel6Prefix56_eq
  · exact panel6Prefix57_eq
  · exact panel6Prefix58_eq
  · exact panel6Prefix59_eq
  · exact panel6Prefix60_eq
  · exact panel6Prefix61_eq
  · exact panel6Prefix62_eq
  · exact panel6Prefix63_eq

theorem panel6DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel6DefectPieces.EnclosesCanonical
      ⟨6, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel6DefectPieces,
      Vector.get_ofFn]
    rw [panel6PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨6, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel6DefectPieces]
    rw [panel6Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨6, by decide⟩

theorem panel6Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel6Cache.EnclosesCanonical
      ⟨6, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel6DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
