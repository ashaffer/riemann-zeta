import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck2_0
import RHBridge.P2RoundedFactorCheckpointCheck2_1
import RHBridge.P2RoundedFactorCheckpointCheck2_2
import RHBridge.P2RoundedFactorCheckpointCheck2_3
import RHBridge.P2RoundedFactorCheckpointCheck2_4
import RHBridge.P2RoundedFactorCheckpointCheck2_5
import RHBridge.P2RoundedFactorCheckpointCheck2_6
import RHBridge.P2RoundedFactorCheckpointCheck2_7
import RHBridge.P2RoundedFactorCheckpointCheck2_8
import RHBridge.P2RoundedFactorCheckpointCheck2_9
import RHBridge.P2RoundedFactorCheckpointCheck2_10
import RHBridge.P2RoundedFactorCheckpointCheck2_11
import RHBridge.P2RoundedFactorCheckpointCheck2_12
import RHBridge.P2RoundedFactorCheckpointCheck2_13
import RHBridge.P2RoundedFactorCheckpointCheck2_14
import RHBridge.P2RoundedFactorCheckpointCheck2_15
import RHBridge.P2RoundedFactorCheckpointCheck2_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel2PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨2, by decide⟩ := by
  fin_cases i
  · exact panel2Prefix0_eq
  · exact panel2Prefix1_eq
  · exact panel2Prefix2_eq
  · exact panel2Prefix3_eq
  · exact panel2Prefix4_eq
  · exact panel2Prefix5_eq
  · exact panel2Prefix6_eq
  · exact panel2Prefix7_eq
  · exact panel2Prefix8_eq
  · exact panel2Prefix9_eq
  · exact panel2Prefix10_eq
  · exact panel2Prefix11_eq
  · exact panel2Prefix12_eq
  · exact panel2Prefix13_eq
  · exact panel2Prefix14_eq
  · exact panel2Prefix15_eq
  · exact panel2Prefix16_eq
  · exact panel2Prefix17_eq
  · exact panel2Prefix18_eq
  · exact panel2Prefix19_eq
  · exact panel2Prefix20_eq
  · exact panel2Prefix21_eq
  · exact panel2Prefix22_eq
  · exact panel2Prefix23_eq
  · exact panel2Prefix24_eq
  · exact panel2Prefix25_eq
  · exact panel2Prefix26_eq
  · exact panel2Prefix27_eq
  · exact panel2Prefix28_eq
  · exact panel2Prefix29_eq
  · exact panel2Prefix30_eq
  · exact panel2Prefix31_eq
  · exact panel2Prefix32_eq
  · exact panel2Prefix33_eq
  · exact panel2Prefix34_eq
  · exact panel2Prefix35_eq
  · exact panel2Prefix36_eq
  · exact panel2Prefix37_eq
  · exact panel2Prefix38_eq
  · exact panel2Prefix39_eq
  · exact panel2Prefix40_eq
  · exact panel2Prefix41_eq
  · exact panel2Prefix42_eq
  · exact panel2Prefix43_eq
  · exact panel2Prefix44_eq
  · exact panel2Prefix45_eq
  · exact panel2Prefix46_eq
  · exact panel2Prefix47_eq
  · exact panel2Prefix48_eq
  · exact panel2Prefix49_eq
  · exact panel2Prefix50_eq
  · exact panel2Prefix51_eq
  · exact panel2Prefix52_eq
  · exact panel2Prefix53_eq
  · exact panel2Prefix54_eq
  · exact panel2Prefix55_eq
  · exact panel2Prefix56_eq
  · exact panel2Prefix57_eq
  · exact panel2Prefix58_eq
  · exact panel2Prefix59_eq
  · exact panel2Prefix60_eq
  · exact panel2Prefix61_eq
  · exact panel2Prefix62_eq
  · exact panel2Prefix63_eq

theorem panel2DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel2DefectPieces.EnclosesCanonical
      ⟨2, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel2DefectPieces,
      Vector.get_ofFn]
    rw [panel2PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨2, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel2DefectPieces]
    rw [panel2Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨2, by decide⟩

theorem panel2Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel2Cache.EnclosesCanonical
      ⟨2, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel2DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
