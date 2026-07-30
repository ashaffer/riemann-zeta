import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck9_0
import RHBridge.P2RoundedFactorCheckpointCheck9_1
import RHBridge.P2RoundedFactorCheckpointCheck9_2
import RHBridge.P2RoundedFactorCheckpointCheck9_3
import RHBridge.P2RoundedFactorCheckpointCheck9_4
import RHBridge.P2RoundedFactorCheckpointCheck9_5
import RHBridge.P2RoundedFactorCheckpointCheck9_6
import RHBridge.P2RoundedFactorCheckpointCheck9_7
import RHBridge.P2RoundedFactorCheckpointCheck9_8
import RHBridge.P2RoundedFactorCheckpointCheck9_9
import RHBridge.P2RoundedFactorCheckpointCheck9_10
import RHBridge.P2RoundedFactorCheckpointCheck9_11
import RHBridge.P2RoundedFactorCheckpointCheck9_12
import RHBridge.P2RoundedFactorCheckpointCheck9_13
import RHBridge.P2RoundedFactorCheckpointCheck9_14
import RHBridge.P2RoundedFactorCheckpointCheck9_15
import RHBridge.P2RoundedFactorCheckpointCheck9_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel9PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨9, by decide⟩ := by
  fin_cases i
  · exact panel9Prefix0_eq
  · exact panel9Prefix1_eq
  · exact panel9Prefix2_eq
  · exact panel9Prefix3_eq
  · exact panel9Prefix4_eq
  · exact panel9Prefix5_eq
  · exact panel9Prefix6_eq
  · exact panel9Prefix7_eq
  · exact panel9Prefix8_eq
  · exact panel9Prefix9_eq
  · exact panel9Prefix10_eq
  · exact panel9Prefix11_eq
  · exact panel9Prefix12_eq
  · exact panel9Prefix13_eq
  · exact panel9Prefix14_eq
  · exact panel9Prefix15_eq
  · exact panel9Prefix16_eq
  · exact panel9Prefix17_eq
  · exact panel9Prefix18_eq
  · exact panel9Prefix19_eq
  · exact panel9Prefix20_eq
  · exact panel9Prefix21_eq
  · exact panel9Prefix22_eq
  · exact panel9Prefix23_eq
  · exact panel9Prefix24_eq
  · exact panel9Prefix25_eq
  · exact panel9Prefix26_eq
  · exact panel9Prefix27_eq
  · exact panel9Prefix28_eq
  · exact panel9Prefix29_eq
  · exact panel9Prefix30_eq
  · exact panel9Prefix31_eq
  · exact panel9Prefix32_eq
  · exact panel9Prefix33_eq
  · exact panel9Prefix34_eq
  · exact panel9Prefix35_eq
  · exact panel9Prefix36_eq
  · exact panel9Prefix37_eq
  · exact panel9Prefix38_eq
  · exact panel9Prefix39_eq
  · exact panel9Prefix40_eq
  · exact panel9Prefix41_eq
  · exact panel9Prefix42_eq
  · exact panel9Prefix43_eq
  · exact panel9Prefix44_eq
  · exact panel9Prefix45_eq
  · exact panel9Prefix46_eq
  · exact panel9Prefix47_eq
  · exact panel9Prefix48_eq
  · exact panel9Prefix49_eq
  · exact panel9Prefix50_eq
  · exact panel9Prefix51_eq
  · exact panel9Prefix52_eq
  · exact panel9Prefix53_eq
  · exact panel9Prefix54_eq
  · exact panel9Prefix55_eq
  · exact panel9Prefix56_eq
  · exact panel9Prefix57_eq
  · exact panel9Prefix58_eq
  · exact panel9Prefix59_eq
  · exact panel9Prefix60_eq
  · exact panel9Prefix61_eq
  · exact panel9Prefix62_eq
  · exact panel9Prefix63_eq

theorem panel9DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel9DefectPieces.EnclosesCanonical
      ⟨9, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel9DefectPieces,
      Vector.get_ofFn]
    rw [panel9PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨9, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel9DefectPieces]
    rw [panel9Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨9, by decide⟩

theorem panel9Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel9Cache.EnclosesCanonical
      ⟨9, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel9DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
