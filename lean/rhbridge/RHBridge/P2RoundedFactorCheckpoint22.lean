import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck22_0
import RHBridge.P2RoundedFactorCheckpointCheck22_1
import RHBridge.P2RoundedFactorCheckpointCheck22_2
import RHBridge.P2RoundedFactorCheckpointCheck22_3
import RHBridge.P2RoundedFactorCheckpointCheck22_4
import RHBridge.P2RoundedFactorCheckpointCheck22_5
import RHBridge.P2RoundedFactorCheckpointCheck22_6
import RHBridge.P2RoundedFactorCheckpointCheck22_7
import RHBridge.P2RoundedFactorCheckpointCheck22_8
import RHBridge.P2RoundedFactorCheckpointCheck22_9
import RHBridge.P2RoundedFactorCheckpointCheck22_10
import RHBridge.P2RoundedFactorCheckpointCheck22_11
import RHBridge.P2RoundedFactorCheckpointCheck22_12
import RHBridge.P2RoundedFactorCheckpointCheck22_13
import RHBridge.P2RoundedFactorCheckpointCheck22_14
import RHBridge.P2RoundedFactorCheckpointCheck22_15
import RHBridge.P2RoundedFactorCheckpointCheck22_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel22PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel22PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨22, by decide⟩ := by
  fin_cases i
  · exact panel22Prefix0_eq
  · exact panel22Prefix1_eq
  · exact panel22Prefix2_eq
  · exact panel22Prefix3_eq
  · exact panel22Prefix4_eq
  · exact panel22Prefix5_eq
  · exact panel22Prefix6_eq
  · exact panel22Prefix7_eq
  · exact panel22Prefix8_eq
  · exact panel22Prefix9_eq
  · exact panel22Prefix10_eq
  · exact panel22Prefix11_eq
  · exact panel22Prefix12_eq
  · exact panel22Prefix13_eq
  · exact panel22Prefix14_eq
  · exact panel22Prefix15_eq
  · exact panel22Prefix16_eq
  · exact panel22Prefix17_eq
  · exact panel22Prefix18_eq
  · exact panel22Prefix19_eq
  · exact panel22Prefix20_eq
  · exact panel22Prefix21_eq
  · exact panel22Prefix22_eq
  · exact panel22Prefix23_eq
  · exact panel22Prefix24_eq
  · exact panel22Prefix25_eq
  · exact panel22Prefix26_eq
  · exact panel22Prefix27_eq
  · exact panel22Prefix28_eq
  · exact panel22Prefix29_eq
  · exact panel22Prefix30_eq
  · exact panel22Prefix31_eq
  · exact panel22Prefix32_eq
  · exact panel22Prefix33_eq
  · exact panel22Prefix34_eq
  · exact panel22Prefix35_eq
  · exact panel22Prefix36_eq
  · exact panel22Prefix37_eq
  · exact panel22Prefix38_eq
  · exact panel22Prefix39_eq
  · exact panel22Prefix40_eq
  · exact panel22Prefix41_eq
  · exact panel22Prefix42_eq
  · exact panel22Prefix43_eq
  · exact panel22Prefix44_eq
  · exact panel22Prefix45_eq
  · exact panel22Prefix46_eq
  · exact panel22Prefix47_eq
  · exact panel22Prefix48_eq
  · exact panel22Prefix49_eq
  · exact panel22Prefix50_eq
  · exact panel22Prefix51_eq
  · exact panel22Prefix52_eq
  · exact panel22Prefix53_eq
  · exact panel22Prefix54_eq
  · exact panel22Prefix55_eq
  · exact panel22Prefix56_eq
  · exact panel22Prefix57_eq
  · exact panel22Prefix58_eq
  · exact panel22Prefix59_eq
  · exact panel22Prefix60_eq
  · exact panel22Prefix61_eq
  · exact panel22Prefix62_eq
  · exact panel22Prefix63_eq

theorem panel22DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel22DefectPieces.EnclosesCanonical
      ⟨22, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel22DefectPieces,
      Vector.get_ofFn]
    rw [panel22PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨22, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel22DefectPieces]
    rw [panel22Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨22, by decide⟩

theorem panel22Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel22Cache.EnclosesCanonical
      ⟨22, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel22DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
