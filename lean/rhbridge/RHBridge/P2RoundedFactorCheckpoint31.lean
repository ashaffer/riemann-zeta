import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck31_0
import RHBridge.P2RoundedFactorCheckpointCheck31_1
import RHBridge.P2RoundedFactorCheckpointCheck31_2
import RHBridge.P2RoundedFactorCheckpointCheck31_3
import RHBridge.P2RoundedFactorCheckpointCheck31_4
import RHBridge.P2RoundedFactorCheckpointCheck31_5
import RHBridge.P2RoundedFactorCheckpointCheck31_6
import RHBridge.P2RoundedFactorCheckpointCheck31_7
import RHBridge.P2RoundedFactorCheckpointCheck31_8
import RHBridge.P2RoundedFactorCheckpointCheck31_9
import RHBridge.P2RoundedFactorCheckpointCheck31_10
import RHBridge.P2RoundedFactorCheckpointCheck31_11
import RHBridge.P2RoundedFactorCheckpointCheck31_12
import RHBridge.P2RoundedFactorCheckpointCheck31_13
import RHBridge.P2RoundedFactorCheckpointCheck31_14
import RHBridge.P2RoundedFactorCheckpointCheck31_15
import RHBridge.P2RoundedFactorCheckpointCheck31_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel31PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨31, by decide⟩ := by
  fin_cases i
  · exact panel31Prefix0_eq
  · exact panel31Prefix1_eq
  · exact panel31Prefix2_eq
  · exact panel31Prefix3_eq
  · exact panel31Prefix4_eq
  · exact panel31Prefix5_eq
  · exact panel31Prefix6_eq
  · exact panel31Prefix7_eq
  · exact panel31Prefix8_eq
  · exact panel31Prefix9_eq
  · exact panel31Prefix10_eq
  · exact panel31Prefix11_eq
  · exact panel31Prefix12_eq
  · exact panel31Prefix13_eq
  · exact panel31Prefix14_eq
  · exact panel31Prefix15_eq
  · exact panel31Prefix16_eq
  · exact panel31Prefix17_eq
  · exact panel31Prefix18_eq
  · exact panel31Prefix19_eq
  · exact panel31Prefix20_eq
  · exact panel31Prefix21_eq
  · exact panel31Prefix22_eq
  · exact panel31Prefix23_eq
  · exact panel31Prefix24_eq
  · exact panel31Prefix25_eq
  · exact panel31Prefix26_eq
  · exact panel31Prefix27_eq
  · exact panel31Prefix28_eq
  · exact panel31Prefix29_eq
  · exact panel31Prefix30_eq
  · exact panel31Prefix31_eq
  · exact panel31Prefix32_eq
  · exact panel31Prefix33_eq
  · exact panel31Prefix34_eq
  · exact panel31Prefix35_eq
  · exact panel31Prefix36_eq
  · exact panel31Prefix37_eq
  · exact panel31Prefix38_eq
  · exact panel31Prefix39_eq
  · exact panel31Prefix40_eq
  · exact panel31Prefix41_eq
  · exact panel31Prefix42_eq
  · exact panel31Prefix43_eq
  · exact panel31Prefix44_eq
  · exact panel31Prefix45_eq
  · exact panel31Prefix46_eq
  · exact panel31Prefix47_eq
  · exact panel31Prefix48_eq
  · exact panel31Prefix49_eq
  · exact panel31Prefix50_eq
  · exact panel31Prefix51_eq
  · exact panel31Prefix52_eq
  · exact panel31Prefix53_eq
  · exact panel31Prefix54_eq
  · exact panel31Prefix55_eq
  · exact panel31Prefix56_eq
  · exact panel31Prefix57_eq
  · exact panel31Prefix58_eq
  · exact panel31Prefix59_eq
  · exact panel31Prefix60_eq
  · exact panel31Prefix61_eq
  · exact panel31Prefix62_eq
  · exact panel31Prefix63_eq

theorem panel31DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel31DefectPieces.EnclosesCanonical
      ⟨31, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel31DefectPieces,
      Vector.get_ofFn]
    rw [panel31PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨31, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel31DefectPieces]
    rw [panel31Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨31, by decide⟩

theorem panel31Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel31Cache.EnclosesCanonical
      ⟨31, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel31DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
