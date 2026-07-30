import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck29_0
import RHBridge.P2RoundedFactorCheckpointCheck29_1
import RHBridge.P2RoundedFactorCheckpointCheck29_2
import RHBridge.P2RoundedFactorCheckpointCheck29_3
import RHBridge.P2RoundedFactorCheckpointCheck29_4
import RHBridge.P2RoundedFactorCheckpointCheck29_5
import RHBridge.P2RoundedFactorCheckpointCheck29_6
import RHBridge.P2RoundedFactorCheckpointCheck29_7
import RHBridge.P2RoundedFactorCheckpointCheck29_8
import RHBridge.P2RoundedFactorCheckpointCheck29_9
import RHBridge.P2RoundedFactorCheckpointCheck29_10
import RHBridge.P2RoundedFactorCheckpointCheck29_11
import RHBridge.P2RoundedFactorCheckpointCheck29_12
import RHBridge.P2RoundedFactorCheckpointCheck29_13
import RHBridge.P2RoundedFactorCheckpointCheck29_14
import RHBridge.P2RoundedFactorCheckpointCheck29_15
import RHBridge.P2RoundedFactorCheckpointCheck29_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel29PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel29PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨29, by decide⟩ := by
  fin_cases i
  · exact panel29Prefix0_eq
  · exact panel29Prefix1_eq
  · exact panel29Prefix2_eq
  · exact panel29Prefix3_eq
  · exact panel29Prefix4_eq
  · exact panel29Prefix5_eq
  · exact panel29Prefix6_eq
  · exact panel29Prefix7_eq
  · exact panel29Prefix8_eq
  · exact panel29Prefix9_eq
  · exact panel29Prefix10_eq
  · exact panel29Prefix11_eq
  · exact panel29Prefix12_eq
  · exact panel29Prefix13_eq
  · exact panel29Prefix14_eq
  · exact panel29Prefix15_eq
  · exact panel29Prefix16_eq
  · exact panel29Prefix17_eq
  · exact panel29Prefix18_eq
  · exact panel29Prefix19_eq
  · exact panel29Prefix20_eq
  · exact panel29Prefix21_eq
  · exact panel29Prefix22_eq
  · exact panel29Prefix23_eq
  · exact panel29Prefix24_eq
  · exact panel29Prefix25_eq
  · exact panel29Prefix26_eq
  · exact panel29Prefix27_eq
  · exact panel29Prefix28_eq
  · exact panel29Prefix29_eq
  · exact panel29Prefix30_eq
  · exact panel29Prefix31_eq
  · exact panel29Prefix32_eq
  · exact panel29Prefix33_eq
  · exact panel29Prefix34_eq
  · exact panel29Prefix35_eq
  · exact panel29Prefix36_eq
  · exact panel29Prefix37_eq
  · exact panel29Prefix38_eq
  · exact panel29Prefix39_eq
  · exact panel29Prefix40_eq
  · exact panel29Prefix41_eq
  · exact panel29Prefix42_eq
  · exact panel29Prefix43_eq
  · exact panel29Prefix44_eq
  · exact panel29Prefix45_eq
  · exact panel29Prefix46_eq
  · exact panel29Prefix47_eq
  · exact panel29Prefix48_eq
  · exact panel29Prefix49_eq
  · exact panel29Prefix50_eq
  · exact panel29Prefix51_eq
  · exact panel29Prefix52_eq
  · exact panel29Prefix53_eq
  · exact panel29Prefix54_eq
  · exact panel29Prefix55_eq
  · exact panel29Prefix56_eq
  · exact panel29Prefix57_eq
  · exact panel29Prefix58_eq
  · exact panel29Prefix59_eq
  · exact panel29Prefix60_eq
  · exact panel29Prefix61_eq
  · exact panel29Prefix62_eq
  · exact panel29Prefix63_eq

theorem panel29DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel29DefectPieces.EnclosesCanonical
      ⟨29, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel29DefectPieces,
      Vector.get_ofFn]
    rw [panel29PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨29, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel29DefectPieces]
    rw [panel29Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨29, by decide⟩

theorem panel29Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel29Cache.EnclosesCanonical
      ⟨29, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel29DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
