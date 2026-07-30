import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck28_0
import RHBridge.P2RoundedFactorCheckpointCheck28_1
import RHBridge.P2RoundedFactorCheckpointCheck28_2
import RHBridge.P2RoundedFactorCheckpointCheck28_3
import RHBridge.P2RoundedFactorCheckpointCheck28_4
import RHBridge.P2RoundedFactorCheckpointCheck28_5
import RHBridge.P2RoundedFactorCheckpointCheck28_6
import RHBridge.P2RoundedFactorCheckpointCheck28_7
import RHBridge.P2RoundedFactorCheckpointCheck28_8
import RHBridge.P2RoundedFactorCheckpointCheck28_9
import RHBridge.P2RoundedFactorCheckpointCheck28_10
import RHBridge.P2RoundedFactorCheckpointCheck28_11
import RHBridge.P2RoundedFactorCheckpointCheck28_12
import RHBridge.P2RoundedFactorCheckpointCheck28_13
import RHBridge.P2RoundedFactorCheckpointCheck28_14
import RHBridge.P2RoundedFactorCheckpointCheck28_15
import RHBridge.P2RoundedFactorCheckpointCheck28_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel28PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨28, by decide⟩ := by
  fin_cases i
  · exact panel28Prefix0_eq
  · exact panel28Prefix1_eq
  · exact panel28Prefix2_eq
  · exact panel28Prefix3_eq
  · exact panel28Prefix4_eq
  · exact panel28Prefix5_eq
  · exact panel28Prefix6_eq
  · exact panel28Prefix7_eq
  · exact panel28Prefix8_eq
  · exact panel28Prefix9_eq
  · exact panel28Prefix10_eq
  · exact panel28Prefix11_eq
  · exact panel28Prefix12_eq
  · exact panel28Prefix13_eq
  · exact panel28Prefix14_eq
  · exact panel28Prefix15_eq
  · exact panel28Prefix16_eq
  · exact panel28Prefix17_eq
  · exact panel28Prefix18_eq
  · exact panel28Prefix19_eq
  · exact panel28Prefix20_eq
  · exact panel28Prefix21_eq
  · exact panel28Prefix22_eq
  · exact panel28Prefix23_eq
  · exact panel28Prefix24_eq
  · exact panel28Prefix25_eq
  · exact panel28Prefix26_eq
  · exact panel28Prefix27_eq
  · exact panel28Prefix28_eq
  · exact panel28Prefix29_eq
  · exact panel28Prefix30_eq
  · exact panel28Prefix31_eq
  · exact panel28Prefix32_eq
  · exact panel28Prefix33_eq
  · exact panel28Prefix34_eq
  · exact panel28Prefix35_eq
  · exact panel28Prefix36_eq
  · exact panel28Prefix37_eq
  · exact panel28Prefix38_eq
  · exact panel28Prefix39_eq
  · exact panel28Prefix40_eq
  · exact panel28Prefix41_eq
  · exact panel28Prefix42_eq
  · exact panel28Prefix43_eq
  · exact panel28Prefix44_eq
  · exact panel28Prefix45_eq
  · exact panel28Prefix46_eq
  · exact panel28Prefix47_eq
  · exact panel28Prefix48_eq
  · exact panel28Prefix49_eq
  · exact panel28Prefix50_eq
  · exact panel28Prefix51_eq
  · exact panel28Prefix52_eq
  · exact panel28Prefix53_eq
  · exact panel28Prefix54_eq
  · exact panel28Prefix55_eq
  · exact panel28Prefix56_eq
  · exact panel28Prefix57_eq
  · exact panel28Prefix58_eq
  · exact panel28Prefix59_eq
  · exact panel28Prefix60_eq
  · exact panel28Prefix61_eq
  · exact panel28Prefix62_eq
  · exact panel28Prefix63_eq

theorem panel28DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel28DefectPieces.EnclosesCanonical
      ⟨28, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel28DefectPieces,
      Vector.get_ofFn]
    rw [panel28PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨28, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel28DefectPieces]
    rw [panel28Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨28, by decide⟩

theorem panel28Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel28Cache.EnclosesCanonical
      ⟨28, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel28DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
