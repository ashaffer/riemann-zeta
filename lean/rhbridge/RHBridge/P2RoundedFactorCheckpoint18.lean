import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck18_0
import RHBridge.P2RoundedFactorCheckpointCheck18_1
import RHBridge.P2RoundedFactorCheckpointCheck18_2
import RHBridge.P2RoundedFactorCheckpointCheck18_3
import RHBridge.P2RoundedFactorCheckpointCheck18_4
import RHBridge.P2RoundedFactorCheckpointCheck18_5
import RHBridge.P2RoundedFactorCheckpointCheck18_6
import RHBridge.P2RoundedFactorCheckpointCheck18_7
import RHBridge.P2RoundedFactorCheckpointCheck18_8
import RHBridge.P2RoundedFactorCheckpointCheck18_9
import RHBridge.P2RoundedFactorCheckpointCheck18_10
import RHBridge.P2RoundedFactorCheckpointCheck18_11
import RHBridge.P2RoundedFactorCheckpointCheck18_12
import RHBridge.P2RoundedFactorCheckpointCheck18_13
import RHBridge.P2RoundedFactorCheckpointCheck18_14
import RHBridge.P2RoundedFactorCheckpointCheck18_15
import RHBridge.P2RoundedFactorCheckpointCheck18_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel18PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨18, by decide⟩ := by
  fin_cases i
  · exact panel18Prefix0_eq
  · exact panel18Prefix1_eq
  · exact panel18Prefix2_eq
  · exact panel18Prefix3_eq
  · exact panel18Prefix4_eq
  · exact panel18Prefix5_eq
  · exact panel18Prefix6_eq
  · exact panel18Prefix7_eq
  · exact panel18Prefix8_eq
  · exact panel18Prefix9_eq
  · exact panel18Prefix10_eq
  · exact panel18Prefix11_eq
  · exact panel18Prefix12_eq
  · exact panel18Prefix13_eq
  · exact panel18Prefix14_eq
  · exact panel18Prefix15_eq
  · exact panel18Prefix16_eq
  · exact panel18Prefix17_eq
  · exact panel18Prefix18_eq
  · exact panel18Prefix19_eq
  · exact panel18Prefix20_eq
  · exact panel18Prefix21_eq
  · exact panel18Prefix22_eq
  · exact panel18Prefix23_eq
  · exact panel18Prefix24_eq
  · exact panel18Prefix25_eq
  · exact panel18Prefix26_eq
  · exact panel18Prefix27_eq
  · exact panel18Prefix28_eq
  · exact panel18Prefix29_eq
  · exact panel18Prefix30_eq
  · exact panel18Prefix31_eq
  · exact panel18Prefix32_eq
  · exact panel18Prefix33_eq
  · exact panel18Prefix34_eq
  · exact panel18Prefix35_eq
  · exact panel18Prefix36_eq
  · exact panel18Prefix37_eq
  · exact panel18Prefix38_eq
  · exact panel18Prefix39_eq
  · exact panel18Prefix40_eq
  · exact panel18Prefix41_eq
  · exact panel18Prefix42_eq
  · exact panel18Prefix43_eq
  · exact panel18Prefix44_eq
  · exact panel18Prefix45_eq
  · exact panel18Prefix46_eq
  · exact panel18Prefix47_eq
  · exact panel18Prefix48_eq
  · exact panel18Prefix49_eq
  · exact panel18Prefix50_eq
  · exact panel18Prefix51_eq
  · exact panel18Prefix52_eq
  · exact panel18Prefix53_eq
  · exact panel18Prefix54_eq
  · exact panel18Prefix55_eq
  · exact panel18Prefix56_eq
  · exact panel18Prefix57_eq
  · exact panel18Prefix58_eq
  · exact panel18Prefix59_eq
  · exact panel18Prefix60_eq
  · exact panel18Prefix61_eq
  · exact panel18Prefix62_eq
  · exact panel18Prefix63_eq

theorem panel18DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel18DefectPieces.EnclosesCanonical
      ⟨18, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel18DefectPieces,
      Vector.get_ofFn]
    rw [panel18PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨18, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel18DefectPieces]
    rw [panel18Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨18, by decide⟩

theorem panel18Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel18Cache.EnclosesCanonical
      ⟨18, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel18DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
