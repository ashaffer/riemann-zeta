import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck1_0
import RHBridge.P2RoundedFactorCheckpointCheck1_1
import RHBridge.P2RoundedFactorCheckpointCheck1_2
import RHBridge.P2RoundedFactorCheckpointCheck1_3
import RHBridge.P2RoundedFactorCheckpointCheck1_4
import RHBridge.P2RoundedFactorCheckpointCheck1_5
import RHBridge.P2RoundedFactorCheckpointCheck1_6
import RHBridge.P2RoundedFactorCheckpointCheck1_7
import RHBridge.P2RoundedFactorCheckpointCheck1_8
import RHBridge.P2RoundedFactorCheckpointCheck1_9
import RHBridge.P2RoundedFactorCheckpointCheck1_10
import RHBridge.P2RoundedFactorCheckpointCheck1_11
import RHBridge.P2RoundedFactorCheckpointCheck1_12
import RHBridge.P2RoundedFactorCheckpointCheck1_13
import RHBridge.P2RoundedFactorCheckpointCheck1_14
import RHBridge.P2RoundedFactorCheckpointCheck1_15
import RHBridge.P2RoundedFactorCheckpointCheck1_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel1PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨1, by decide⟩ := by
  fin_cases i
  · exact panel1Prefix0_eq
  · exact panel1Prefix1_eq
  · exact panel1Prefix2_eq
  · exact panel1Prefix3_eq
  · exact panel1Prefix4_eq
  · exact panel1Prefix5_eq
  · exact panel1Prefix6_eq
  · exact panel1Prefix7_eq
  · exact panel1Prefix8_eq
  · exact panel1Prefix9_eq
  · exact panel1Prefix10_eq
  · exact panel1Prefix11_eq
  · exact panel1Prefix12_eq
  · exact panel1Prefix13_eq
  · exact panel1Prefix14_eq
  · exact panel1Prefix15_eq
  · exact panel1Prefix16_eq
  · exact panel1Prefix17_eq
  · exact panel1Prefix18_eq
  · exact panel1Prefix19_eq
  · exact panel1Prefix20_eq
  · exact panel1Prefix21_eq
  · exact panel1Prefix22_eq
  · exact panel1Prefix23_eq
  · exact panel1Prefix24_eq
  · exact panel1Prefix25_eq
  · exact panel1Prefix26_eq
  · exact panel1Prefix27_eq
  · exact panel1Prefix28_eq
  · exact panel1Prefix29_eq
  · exact panel1Prefix30_eq
  · exact panel1Prefix31_eq
  · exact panel1Prefix32_eq
  · exact panel1Prefix33_eq
  · exact panel1Prefix34_eq
  · exact panel1Prefix35_eq
  · exact panel1Prefix36_eq
  · exact panel1Prefix37_eq
  · exact panel1Prefix38_eq
  · exact panel1Prefix39_eq
  · exact panel1Prefix40_eq
  · exact panel1Prefix41_eq
  · exact panel1Prefix42_eq
  · exact panel1Prefix43_eq
  · exact panel1Prefix44_eq
  · exact panel1Prefix45_eq
  · exact panel1Prefix46_eq
  · exact panel1Prefix47_eq
  · exact panel1Prefix48_eq
  · exact panel1Prefix49_eq
  · exact panel1Prefix50_eq
  · exact panel1Prefix51_eq
  · exact panel1Prefix52_eq
  · exact panel1Prefix53_eq
  · exact panel1Prefix54_eq
  · exact panel1Prefix55_eq
  · exact panel1Prefix56_eq
  · exact panel1Prefix57_eq
  · exact panel1Prefix58_eq
  · exact panel1Prefix59_eq
  · exact panel1Prefix60_eq
  · exact panel1Prefix61_eq
  · exact panel1Prefix62_eq
  · exact panel1Prefix63_eq

theorem panel1DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel1DefectPieces.EnclosesCanonical
      ⟨1, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel1DefectPieces,
      Vector.get_ofFn]
    rw [panel1PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨1, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel1DefectPieces]
    rw [panel1Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨1, by decide⟩

theorem panel1Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel1Cache.EnclosesCanonical
      ⟨1, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel1DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
