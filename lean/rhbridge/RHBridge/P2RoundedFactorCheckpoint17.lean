import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck17_0
import RHBridge.P2RoundedFactorCheckpointCheck17_1
import RHBridge.P2RoundedFactorCheckpointCheck17_2
import RHBridge.P2RoundedFactorCheckpointCheck17_3
import RHBridge.P2RoundedFactorCheckpointCheck17_4
import RHBridge.P2RoundedFactorCheckpointCheck17_5
import RHBridge.P2RoundedFactorCheckpointCheck17_6
import RHBridge.P2RoundedFactorCheckpointCheck17_7
import RHBridge.P2RoundedFactorCheckpointCheck17_8
import RHBridge.P2RoundedFactorCheckpointCheck17_9
import RHBridge.P2RoundedFactorCheckpointCheck17_10
import RHBridge.P2RoundedFactorCheckpointCheck17_11
import RHBridge.P2RoundedFactorCheckpointCheck17_12
import RHBridge.P2RoundedFactorCheckpointCheck17_13
import RHBridge.P2RoundedFactorCheckpointCheck17_14
import RHBridge.P2RoundedFactorCheckpointCheck17_15
import RHBridge.P2RoundedFactorCheckpointCheck17_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel17PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨17, by decide⟩ := by
  fin_cases i
  · exact panel17Prefix0_eq
  · exact panel17Prefix1_eq
  · exact panel17Prefix2_eq
  · exact panel17Prefix3_eq
  · exact panel17Prefix4_eq
  · exact panel17Prefix5_eq
  · exact panel17Prefix6_eq
  · exact panel17Prefix7_eq
  · exact panel17Prefix8_eq
  · exact panel17Prefix9_eq
  · exact panel17Prefix10_eq
  · exact panel17Prefix11_eq
  · exact panel17Prefix12_eq
  · exact panel17Prefix13_eq
  · exact panel17Prefix14_eq
  · exact panel17Prefix15_eq
  · exact panel17Prefix16_eq
  · exact panel17Prefix17_eq
  · exact panel17Prefix18_eq
  · exact panel17Prefix19_eq
  · exact panel17Prefix20_eq
  · exact panel17Prefix21_eq
  · exact panel17Prefix22_eq
  · exact panel17Prefix23_eq
  · exact panel17Prefix24_eq
  · exact panel17Prefix25_eq
  · exact panel17Prefix26_eq
  · exact panel17Prefix27_eq
  · exact panel17Prefix28_eq
  · exact panel17Prefix29_eq
  · exact panel17Prefix30_eq
  · exact panel17Prefix31_eq
  · exact panel17Prefix32_eq
  · exact panel17Prefix33_eq
  · exact panel17Prefix34_eq
  · exact panel17Prefix35_eq
  · exact panel17Prefix36_eq
  · exact panel17Prefix37_eq
  · exact panel17Prefix38_eq
  · exact panel17Prefix39_eq
  · exact panel17Prefix40_eq
  · exact panel17Prefix41_eq
  · exact panel17Prefix42_eq
  · exact panel17Prefix43_eq
  · exact panel17Prefix44_eq
  · exact panel17Prefix45_eq
  · exact panel17Prefix46_eq
  · exact panel17Prefix47_eq
  · exact panel17Prefix48_eq
  · exact panel17Prefix49_eq
  · exact panel17Prefix50_eq
  · exact panel17Prefix51_eq
  · exact panel17Prefix52_eq
  · exact panel17Prefix53_eq
  · exact panel17Prefix54_eq
  · exact panel17Prefix55_eq
  · exact panel17Prefix56_eq
  · exact panel17Prefix57_eq
  · exact panel17Prefix58_eq
  · exact panel17Prefix59_eq
  · exact panel17Prefix60_eq
  · exact panel17Prefix61_eq
  · exact panel17Prefix62_eq
  · exact panel17Prefix63_eq

theorem panel17DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel17DefectPieces.EnclosesCanonical
      ⟨17, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel17DefectPieces,
      Vector.get_ofFn]
    rw [panel17PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨17, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel17DefectPieces]
    rw [panel17Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨17, by decide⟩

theorem panel17Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel17Cache.EnclosesCanonical
      ⟨17, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel17DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
