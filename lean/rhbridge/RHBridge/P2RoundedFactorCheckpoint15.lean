import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck15_0
import RHBridge.P2RoundedFactorCheckpointCheck15_1
import RHBridge.P2RoundedFactorCheckpointCheck15_2
import RHBridge.P2RoundedFactorCheckpointCheck15_3
import RHBridge.P2RoundedFactorCheckpointCheck15_4
import RHBridge.P2RoundedFactorCheckpointCheck15_5
import RHBridge.P2RoundedFactorCheckpointCheck15_6
import RHBridge.P2RoundedFactorCheckpointCheck15_7
import RHBridge.P2RoundedFactorCheckpointCheck15_8
import RHBridge.P2RoundedFactorCheckpointCheck15_9
import RHBridge.P2RoundedFactorCheckpointCheck15_10
import RHBridge.P2RoundedFactorCheckpointCheck15_11
import RHBridge.P2RoundedFactorCheckpointCheck15_12
import RHBridge.P2RoundedFactorCheckpointCheck15_13
import RHBridge.P2RoundedFactorCheckpointCheck15_14
import RHBridge.P2RoundedFactorCheckpointCheck15_15
import RHBridge.P2RoundedFactorCheckpointCheck15_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel15PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨15, by decide⟩ := by
  fin_cases i
  · exact panel15Prefix0_eq
  · exact panel15Prefix1_eq
  · exact panel15Prefix2_eq
  · exact panel15Prefix3_eq
  · exact panel15Prefix4_eq
  · exact panel15Prefix5_eq
  · exact panel15Prefix6_eq
  · exact panel15Prefix7_eq
  · exact panel15Prefix8_eq
  · exact panel15Prefix9_eq
  · exact panel15Prefix10_eq
  · exact panel15Prefix11_eq
  · exact panel15Prefix12_eq
  · exact panel15Prefix13_eq
  · exact panel15Prefix14_eq
  · exact panel15Prefix15_eq
  · exact panel15Prefix16_eq
  · exact panel15Prefix17_eq
  · exact panel15Prefix18_eq
  · exact panel15Prefix19_eq
  · exact panel15Prefix20_eq
  · exact panel15Prefix21_eq
  · exact panel15Prefix22_eq
  · exact panel15Prefix23_eq
  · exact panel15Prefix24_eq
  · exact panel15Prefix25_eq
  · exact panel15Prefix26_eq
  · exact panel15Prefix27_eq
  · exact panel15Prefix28_eq
  · exact panel15Prefix29_eq
  · exact panel15Prefix30_eq
  · exact panel15Prefix31_eq
  · exact panel15Prefix32_eq
  · exact panel15Prefix33_eq
  · exact panel15Prefix34_eq
  · exact panel15Prefix35_eq
  · exact panel15Prefix36_eq
  · exact panel15Prefix37_eq
  · exact panel15Prefix38_eq
  · exact panel15Prefix39_eq
  · exact panel15Prefix40_eq
  · exact panel15Prefix41_eq
  · exact panel15Prefix42_eq
  · exact panel15Prefix43_eq
  · exact panel15Prefix44_eq
  · exact panel15Prefix45_eq
  · exact panel15Prefix46_eq
  · exact panel15Prefix47_eq
  · exact panel15Prefix48_eq
  · exact panel15Prefix49_eq
  · exact panel15Prefix50_eq
  · exact panel15Prefix51_eq
  · exact panel15Prefix52_eq
  · exact panel15Prefix53_eq
  · exact panel15Prefix54_eq
  · exact panel15Prefix55_eq
  · exact panel15Prefix56_eq
  · exact panel15Prefix57_eq
  · exact panel15Prefix58_eq
  · exact panel15Prefix59_eq
  · exact panel15Prefix60_eq
  · exact panel15Prefix61_eq
  · exact panel15Prefix62_eq
  · exact panel15Prefix63_eq

theorem panel15DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel15DefectPieces.EnclosesCanonical
      ⟨15, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel15DefectPieces,
      Vector.get_ofFn]
    rw [panel15PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨15, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel15DefectPieces]
    rw [panel15Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨15, by decide⟩

theorem panel15Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel15Cache.EnclosesCanonical
      ⟨15, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel15DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
