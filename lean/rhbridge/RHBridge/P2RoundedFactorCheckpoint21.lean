import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck21_0
import RHBridge.P2RoundedFactorCheckpointCheck21_1
import RHBridge.P2RoundedFactorCheckpointCheck21_2
import RHBridge.P2RoundedFactorCheckpointCheck21_3
import RHBridge.P2RoundedFactorCheckpointCheck21_4
import RHBridge.P2RoundedFactorCheckpointCheck21_5
import RHBridge.P2RoundedFactorCheckpointCheck21_6
import RHBridge.P2RoundedFactorCheckpointCheck21_7
import RHBridge.P2RoundedFactorCheckpointCheck21_8
import RHBridge.P2RoundedFactorCheckpointCheck21_9
import RHBridge.P2RoundedFactorCheckpointCheck21_10
import RHBridge.P2RoundedFactorCheckpointCheck21_11
import RHBridge.P2RoundedFactorCheckpointCheck21_12
import RHBridge.P2RoundedFactorCheckpointCheck21_13
import RHBridge.P2RoundedFactorCheckpointCheck21_14
import RHBridge.P2RoundedFactorCheckpointCheck21_15
import RHBridge.P2RoundedFactorCheckpointCheck21_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel21PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨21, by decide⟩ := by
  fin_cases i
  · exact panel21Prefix0_eq
  · exact panel21Prefix1_eq
  · exact panel21Prefix2_eq
  · exact panel21Prefix3_eq
  · exact panel21Prefix4_eq
  · exact panel21Prefix5_eq
  · exact panel21Prefix6_eq
  · exact panel21Prefix7_eq
  · exact panel21Prefix8_eq
  · exact panel21Prefix9_eq
  · exact panel21Prefix10_eq
  · exact panel21Prefix11_eq
  · exact panel21Prefix12_eq
  · exact panel21Prefix13_eq
  · exact panel21Prefix14_eq
  · exact panel21Prefix15_eq
  · exact panel21Prefix16_eq
  · exact panel21Prefix17_eq
  · exact panel21Prefix18_eq
  · exact panel21Prefix19_eq
  · exact panel21Prefix20_eq
  · exact panel21Prefix21_eq
  · exact panel21Prefix22_eq
  · exact panel21Prefix23_eq
  · exact panel21Prefix24_eq
  · exact panel21Prefix25_eq
  · exact panel21Prefix26_eq
  · exact panel21Prefix27_eq
  · exact panel21Prefix28_eq
  · exact panel21Prefix29_eq
  · exact panel21Prefix30_eq
  · exact panel21Prefix31_eq
  · exact panel21Prefix32_eq
  · exact panel21Prefix33_eq
  · exact panel21Prefix34_eq
  · exact panel21Prefix35_eq
  · exact panel21Prefix36_eq
  · exact panel21Prefix37_eq
  · exact panel21Prefix38_eq
  · exact panel21Prefix39_eq
  · exact panel21Prefix40_eq
  · exact panel21Prefix41_eq
  · exact panel21Prefix42_eq
  · exact panel21Prefix43_eq
  · exact panel21Prefix44_eq
  · exact panel21Prefix45_eq
  · exact panel21Prefix46_eq
  · exact panel21Prefix47_eq
  · exact panel21Prefix48_eq
  · exact panel21Prefix49_eq
  · exact panel21Prefix50_eq
  · exact panel21Prefix51_eq
  · exact panel21Prefix52_eq
  · exact panel21Prefix53_eq
  · exact panel21Prefix54_eq
  · exact panel21Prefix55_eq
  · exact panel21Prefix56_eq
  · exact panel21Prefix57_eq
  · exact panel21Prefix58_eq
  · exact panel21Prefix59_eq
  · exact panel21Prefix60_eq
  · exact panel21Prefix61_eq
  · exact panel21Prefix62_eq
  · exact panel21Prefix63_eq

theorem panel21DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel21DefectPieces.EnclosesCanonical
      ⟨21, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel21DefectPieces,
      Vector.get_ofFn]
    rw [panel21PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨21, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel21DefectPieces]
    rw [panel21Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨21, by decide⟩

theorem panel21Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel21Cache.EnclosesCanonical
      ⟨21, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel21DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
