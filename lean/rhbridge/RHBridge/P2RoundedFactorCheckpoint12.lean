import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck12_0
import RHBridge.P2RoundedFactorCheckpointCheck12_1
import RHBridge.P2RoundedFactorCheckpointCheck12_2
import RHBridge.P2RoundedFactorCheckpointCheck12_3
import RHBridge.P2RoundedFactorCheckpointCheck12_4
import RHBridge.P2RoundedFactorCheckpointCheck12_5
import RHBridge.P2RoundedFactorCheckpointCheck12_6
import RHBridge.P2RoundedFactorCheckpointCheck12_7
import RHBridge.P2RoundedFactorCheckpointCheck12_8
import RHBridge.P2RoundedFactorCheckpointCheck12_9
import RHBridge.P2RoundedFactorCheckpointCheck12_10
import RHBridge.P2RoundedFactorCheckpointCheck12_11
import RHBridge.P2RoundedFactorCheckpointCheck12_12
import RHBridge.P2RoundedFactorCheckpointCheck12_13
import RHBridge.P2RoundedFactorCheckpointCheck12_14
import RHBridge.P2RoundedFactorCheckpointCheck12_15
import RHBridge.P2RoundedFactorCheckpointCheck12_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel12PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨12, by decide⟩ := by
  fin_cases i
  · exact panel12Prefix0_eq
  · exact panel12Prefix1_eq
  · exact panel12Prefix2_eq
  · exact panel12Prefix3_eq
  · exact panel12Prefix4_eq
  · exact panel12Prefix5_eq
  · exact panel12Prefix6_eq
  · exact panel12Prefix7_eq
  · exact panel12Prefix8_eq
  · exact panel12Prefix9_eq
  · exact panel12Prefix10_eq
  · exact panel12Prefix11_eq
  · exact panel12Prefix12_eq
  · exact panel12Prefix13_eq
  · exact panel12Prefix14_eq
  · exact panel12Prefix15_eq
  · exact panel12Prefix16_eq
  · exact panel12Prefix17_eq
  · exact panel12Prefix18_eq
  · exact panel12Prefix19_eq
  · exact panel12Prefix20_eq
  · exact panel12Prefix21_eq
  · exact panel12Prefix22_eq
  · exact panel12Prefix23_eq
  · exact panel12Prefix24_eq
  · exact panel12Prefix25_eq
  · exact panel12Prefix26_eq
  · exact panel12Prefix27_eq
  · exact panel12Prefix28_eq
  · exact panel12Prefix29_eq
  · exact panel12Prefix30_eq
  · exact panel12Prefix31_eq
  · exact panel12Prefix32_eq
  · exact panel12Prefix33_eq
  · exact panel12Prefix34_eq
  · exact panel12Prefix35_eq
  · exact panel12Prefix36_eq
  · exact panel12Prefix37_eq
  · exact panel12Prefix38_eq
  · exact panel12Prefix39_eq
  · exact panel12Prefix40_eq
  · exact panel12Prefix41_eq
  · exact panel12Prefix42_eq
  · exact panel12Prefix43_eq
  · exact panel12Prefix44_eq
  · exact panel12Prefix45_eq
  · exact panel12Prefix46_eq
  · exact panel12Prefix47_eq
  · exact panel12Prefix48_eq
  · exact panel12Prefix49_eq
  · exact panel12Prefix50_eq
  · exact panel12Prefix51_eq
  · exact panel12Prefix52_eq
  · exact panel12Prefix53_eq
  · exact panel12Prefix54_eq
  · exact panel12Prefix55_eq
  · exact panel12Prefix56_eq
  · exact panel12Prefix57_eq
  · exact panel12Prefix58_eq
  · exact panel12Prefix59_eq
  · exact panel12Prefix60_eq
  · exact panel12Prefix61_eq
  · exact panel12Prefix62_eq
  · exact panel12Prefix63_eq

theorem panel12DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel12DefectPieces.EnclosesCanonical
      ⟨12, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel12DefectPieces,
      Vector.get_ofFn]
    rw [panel12PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨12, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel12DefectPieces]
    rw [panel12Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨12, by decide⟩

theorem panel12Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel12Cache.EnclosesCanonical
      ⟨12, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel12DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
