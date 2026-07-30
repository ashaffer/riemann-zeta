import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck26_0
import RHBridge.P2RoundedFactorCheckpointCheck26_1
import RHBridge.P2RoundedFactorCheckpointCheck26_2
import RHBridge.P2RoundedFactorCheckpointCheck26_3
import RHBridge.P2RoundedFactorCheckpointCheck26_4
import RHBridge.P2RoundedFactorCheckpointCheck26_5
import RHBridge.P2RoundedFactorCheckpointCheck26_6
import RHBridge.P2RoundedFactorCheckpointCheck26_7
import RHBridge.P2RoundedFactorCheckpointCheck26_8
import RHBridge.P2RoundedFactorCheckpointCheck26_9
import RHBridge.P2RoundedFactorCheckpointCheck26_10
import RHBridge.P2RoundedFactorCheckpointCheck26_11
import RHBridge.P2RoundedFactorCheckpointCheck26_12
import RHBridge.P2RoundedFactorCheckpointCheck26_13
import RHBridge.P2RoundedFactorCheckpointCheck26_14
import RHBridge.P2RoundedFactorCheckpointCheck26_15
import RHBridge.P2RoundedFactorCheckpointCheck26_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel26PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨26, by decide⟩ := by
  fin_cases i
  · exact panel26Prefix0_eq
  · exact panel26Prefix1_eq
  · exact panel26Prefix2_eq
  · exact panel26Prefix3_eq
  · exact panel26Prefix4_eq
  · exact panel26Prefix5_eq
  · exact panel26Prefix6_eq
  · exact panel26Prefix7_eq
  · exact panel26Prefix8_eq
  · exact panel26Prefix9_eq
  · exact panel26Prefix10_eq
  · exact panel26Prefix11_eq
  · exact panel26Prefix12_eq
  · exact panel26Prefix13_eq
  · exact panel26Prefix14_eq
  · exact panel26Prefix15_eq
  · exact panel26Prefix16_eq
  · exact panel26Prefix17_eq
  · exact panel26Prefix18_eq
  · exact panel26Prefix19_eq
  · exact panel26Prefix20_eq
  · exact panel26Prefix21_eq
  · exact panel26Prefix22_eq
  · exact panel26Prefix23_eq
  · exact panel26Prefix24_eq
  · exact panel26Prefix25_eq
  · exact panel26Prefix26_eq
  · exact panel26Prefix27_eq
  · exact panel26Prefix28_eq
  · exact panel26Prefix29_eq
  · exact panel26Prefix30_eq
  · exact panel26Prefix31_eq
  · exact panel26Prefix32_eq
  · exact panel26Prefix33_eq
  · exact panel26Prefix34_eq
  · exact panel26Prefix35_eq
  · exact panel26Prefix36_eq
  · exact panel26Prefix37_eq
  · exact panel26Prefix38_eq
  · exact panel26Prefix39_eq
  · exact panel26Prefix40_eq
  · exact panel26Prefix41_eq
  · exact panel26Prefix42_eq
  · exact panel26Prefix43_eq
  · exact panel26Prefix44_eq
  · exact panel26Prefix45_eq
  · exact panel26Prefix46_eq
  · exact panel26Prefix47_eq
  · exact panel26Prefix48_eq
  · exact panel26Prefix49_eq
  · exact panel26Prefix50_eq
  · exact panel26Prefix51_eq
  · exact panel26Prefix52_eq
  · exact panel26Prefix53_eq
  · exact panel26Prefix54_eq
  · exact panel26Prefix55_eq
  · exact panel26Prefix56_eq
  · exact panel26Prefix57_eq
  · exact panel26Prefix58_eq
  · exact panel26Prefix59_eq
  · exact panel26Prefix60_eq
  · exact panel26Prefix61_eq
  · exact panel26Prefix62_eq
  · exact panel26Prefix63_eq

theorem panel26DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel26DefectPieces.EnclosesCanonical
      ⟨26, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel26DefectPieces,
      Vector.get_ofFn]
    rw [panel26PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨26, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel26DefectPieces]
    rw [panel26Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨26, by decide⟩

theorem panel26Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel26Cache.EnclosesCanonical
      ⟨26, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel26DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
