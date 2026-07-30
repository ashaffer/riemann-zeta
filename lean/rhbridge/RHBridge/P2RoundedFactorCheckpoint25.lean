import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck25_0
import RHBridge.P2RoundedFactorCheckpointCheck25_1
import RHBridge.P2RoundedFactorCheckpointCheck25_2
import RHBridge.P2RoundedFactorCheckpointCheck25_3
import RHBridge.P2RoundedFactorCheckpointCheck25_4
import RHBridge.P2RoundedFactorCheckpointCheck25_5
import RHBridge.P2RoundedFactorCheckpointCheck25_6
import RHBridge.P2RoundedFactorCheckpointCheck25_7
import RHBridge.P2RoundedFactorCheckpointCheck25_8
import RHBridge.P2RoundedFactorCheckpointCheck25_9
import RHBridge.P2RoundedFactorCheckpointCheck25_10
import RHBridge.P2RoundedFactorCheckpointCheck25_11
import RHBridge.P2RoundedFactorCheckpointCheck25_12
import RHBridge.P2RoundedFactorCheckpointCheck25_13
import RHBridge.P2RoundedFactorCheckpointCheck25_14
import RHBridge.P2RoundedFactorCheckpointCheck25_15
import RHBridge.P2RoundedFactorCheckpointCheck25_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel25PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨25, by decide⟩ := by
  fin_cases i
  · exact panel25Prefix0_eq
  · exact panel25Prefix1_eq
  · exact panel25Prefix2_eq
  · exact panel25Prefix3_eq
  · exact panel25Prefix4_eq
  · exact panel25Prefix5_eq
  · exact panel25Prefix6_eq
  · exact panel25Prefix7_eq
  · exact panel25Prefix8_eq
  · exact panel25Prefix9_eq
  · exact panel25Prefix10_eq
  · exact panel25Prefix11_eq
  · exact panel25Prefix12_eq
  · exact panel25Prefix13_eq
  · exact panel25Prefix14_eq
  · exact panel25Prefix15_eq
  · exact panel25Prefix16_eq
  · exact panel25Prefix17_eq
  · exact panel25Prefix18_eq
  · exact panel25Prefix19_eq
  · exact panel25Prefix20_eq
  · exact panel25Prefix21_eq
  · exact panel25Prefix22_eq
  · exact panel25Prefix23_eq
  · exact panel25Prefix24_eq
  · exact panel25Prefix25_eq
  · exact panel25Prefix26_eq
  · exact panel25Prefix27_eq
  · exact panel25Prefix28_eq
  · exact panel25Prefix29_eq
  · exact panel25Prefix30_eq
  · exact panel25Prefix31_eq
  · exact panel25Prefix32_eq
  · exact panel25Prefix33_eq
  · exact panel25Prefix34_eq
  · exact panel25Prefix35_eq
  · exact panel25Prefix36_eq
  · exact panel25Prefix37_eq
  · exact panel25Prefix38_eq
  · exact panel25Prefix39_eq
  · exact panel25Prefix40_eq
  · exact panel25Prefix41_eq
  · exact panel25Prefix42_eq
  · exact panel25Prefix43_eq
  · exact panel25Prefix44_eq
  · exact panel25Prefix45_eq
  · exact panel25Prefix46_eq
  · exact panel25Prefix47_eq
  · exact panel25Prefix48_eq
  · exact panel25Prefix49_eq
  · exact panel25Prefix50_eq
  · exact panel25Prefix51_eq
  · exact panel25Prefix52_eq
  · exact panel25Prefix53_eq
  · exact panel25Prefix54_eq
  · exact panel25Prefix55_eq
  · exact panel25Prefix56_eq
  · exact panel25Prefix57_eq
  · exact panel25Prefix58_eq
  · exact panel25Prefix59_eq
  · exact panel25Prefix60_eq
  · exact panel25Prefix61_eq
  · exact panel25Prefix62_eq
  · exact panel25Prefix63_eq

theorem panel25DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel25DefectPieces.EnclosesCanonical
      ⟨25, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel25DefectPieces,
      Vector.get_ofFn]
    rw [panel25PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨25, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel25DefectPieces]
    rw [panel25Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨25, by decide⟩

theorem panel25Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel25Cache.EnclosesCanonical
      ⟨25, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel25DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
