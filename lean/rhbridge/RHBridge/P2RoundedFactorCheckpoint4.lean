import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck4_0
import RHBridge.P2RoundedFactorCheckpointCheck4_1
import RHBridge.P2RoundedFactorCheckpointCheck4_2
import RHBridge.P2RoundedFactorCheckpointCheck4_3
import RHBridge.P2RoundedFactorCheckpointCheck4_4
import RHBridge.P2RoundedFactorCheckpointCheck4_5
import RHBridge.P2RoundedFactorCheckpointCheck4_6
import RHBridge.P2RoundedFactorCheckpointCheck4_7
import RHBridge.P2RoundedFactorCheckpointCheck4_8
import RHBridge.P2RoundedFactorCheckpointCheck4_9
import RHBridge.P2RoundedFactorCheckpointCheck4_10
import RHBridge.P2RoundedFactorCheckpointCheck4_11
import RHBridge.P2RoundedFactorCheckpointCheck4_12
import RHBridge.P2RoundedFactorCheckpointCheck4_13
import RHBridge.P2RoundedFactorCheckpointCheck4_14
import RHBridge.P2RoundedFactorCheckpointCheck4_15
import RHBridge.P2RoundedFactorCheckpointCheck4_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel4PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨4, by decide⟩ := by
  fin_cases i
  · exact panel4Prefix0_eq
  · exact panel4Prefix1_eq
  · exact panel4Prefix2_eq
  · exact panel4Prefix3_eq
  · exact panel4Prefix4_eq
  · exact panel4Prefix5_eq
  · exact panel4Prefix6_eq
  · exact panel4Prefix7_eq
  · exact panel4Prefix8_eq
  · exact panel4Prefix9_eq
  · exact panel4Prefix10_eq
  · exact panel4Prefix11_eq
  · exact panel4Prefix12_eq
  · exact panel4Prefix13_eq
  · exact panel4Prefix14_eq
  · exact panel4Prefix15_eq
  · exact panel4Prefix16_eq
  · exact panel4Prefix17_eq
  · exact panel4Prefix18_eq
  · exact panel4Prefix19_eq
  · exact panel4Prefix20_eq
  · exact panel4Prefix21_eq
  · exact panel4Prefix22_eq
  · exact panel4Prefix23_eq
  · exact panel4Prefix24_eq
  · exact panel4Prefix25_eq
  · exact panel4Prefix26_eq
  · exact panel4Prefix27_eq
  · exact panel4Prefix28_eq
  · exact panel4Prefix29_eq
  · exact panel4Prefix30_eq
  · exact panel4Prefix31_eq
  · exact panel4Prefix32_eq
  · exact panel4Prefix33_eq
  · exact panel4Prefix34_eq
  · exact panel4Prefix35_eq
  · exact panel4Prefix36_eq
  · exact panel4Prefix37_eq
  · exact panel4Prefix38_eq
  · exact panel4Prefix39_eq
  · exact panel4Prefix40_eq
  · exact panel4Prefix41_eq
  · exact panel4Prefix42_eq
  · exact panel4Prefix43_eq
  · exact panel4Prefix44_eq
  · exact panel4Prefix45_eq
  · exact panel4Prefix46_eq
  · exact panel4Prefix47_eq
  · exact panel4Prefix48_eq
  · exact panel4Prefix49_eq
  · exact panel4Prefix50_eq
  · exact panel4Prefix51_eq
  · exact panel4Prefix52_eq
  · exact panel4Prefix53_eq
  · exact panel4Prefix54_eq
  · exact panel4Prefix55_eq
  · exact panel4Prefix56_eq
  · exact panel4Prefix57_eq
  · exact panel4Prefix58_eq
  · exact panel4Prefix59_eq
  · exact panel4Prefix60_eq
  · exact panel4Prefix61_eq
  · exact panel4Prefix62_eq
  · exact panel4Prefix63_eq

theorem panel4DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel4DefectPieces.EnclosesCanonical
      ⟨4, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel4DefectPieces,
      Vector.get_ofFn]
    rw [panel4PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨4, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel4DefectPieces]
    rw [panel4Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨4, by decide⟩

theorem panel4Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel4Cache.EnclosesCanonical
      ⟨4, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel4DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
