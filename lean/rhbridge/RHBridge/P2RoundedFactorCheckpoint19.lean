import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck19_0
import RHBridge.P2RoundedFactorCheckpointCheck19_1
import RHBridge.P2RoundedFactorCheckpointCheck19_2
import RHBridge.P2RoundedFactorCheckpointCheck19_3
import RHBridge.P2RoundedFactorCheckpointCheck19_4
import RHBridge.P2RoundedFactorCheckpointCheck19_5
import RHBridge.P2RoundedFactorCheckpointCheck19_6
import RHBridge.P2RoundedFactorCheckpointCheck19_7
import RHBridge.P2RoundedFactorCheckpointCheck19_8
import RHBridge.P2RoundedFactorCheckpointCheck19_9
import RHBridge.P2RoundedFactorCheckpointCheck19_10
import RHBridge.P2RoundedFactorCheckpointCheck19_11
import RHBridge.P2RoundedFactorCheckpointCheck19_12
import RHBridge.P2RoundedFactorCheckpointCheck19_13
import RHBridge.P2RoundedFactorCheckpointCheck19_14
import RHBridge.P2RoundedFactorCheckpointCheck19_15
import RHBridge.P2RoundedFactorCheckpointCheck19_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel19PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨19, by decide⟩ := by
  fin_cases i
  · exact panel19Prefix0_eq
  · exact panel19Prefix1_eq
  · exact panel19Prefix2_eq
  · exact panel19Prefix3_eq
  · exact panel19Prefix4_eq
  · exact panel19Prefix5_eq
  · exact panel19Prefix6_eq
  · exact panel19Prefix7_eq
  · exact panel19Prefix8_eq
  · exact panel19Prefix9_eq
  · exact panel19Prefix10_eq
  · exact panel19Prefix11_eq
  · exact panel19Prefix12_eq
  · exact panel19Prefix13_eq
  · exact panel19Prefix14_eq
  · exact panel19Prefix15_eq
  · exact panel19Prefix16_eq
  · exact panel19Prefix17_eq
  · exact panel19Prefix18_eq
  · exact panel19Prefix19_eq
  · exact panel19Prefix20_eq
  · exact panel19Prefix21_eq
  · exact panel19Prefix22_eq
  · exact panel19Prefix23_eq
  · exact panel19Prefix24_eq
  · exact panel19Prefix25_eq
  · exact panel19Prefix26_eq
  · exact panel19Prefix27_eq
  · exact panel19Prefix28_eq
  · exact panel19Prefix29_eq
  · exact panel19Prefix30_eq
  · exact panel19Prefix31_eq
  · exact panel19Prefix32_eq
  · exact panel19Prefix33_eq
  · exact panel19Prefix34_eq
  · exact panel19Prefix35_eq
  · exact panel19Prefix36_eq
  · exact panel19Prefix37_eq
  · exact panel19Prefix38_eq
  · exact panel19Prefix39_eq
  · exact panel19Prefix40_eq
  · exact panel19Prefix41_eq
  · exact panel19Prefix42_eq
  · exact panel19Prefix43_eq
  · exact panel19Prefix44_eq
  · exact panel19Prefix45_eq
  · exact panel19Prefix46_eq
  · exact panel19Prefix47_eq
  · exact panel19Prefix48_eq
  · exact panel19Prefix49_eq
  · exact panel19Prefix50_eq
  · exact panel19Prefix51_eq
  · exact panel19Prefix52_eq
  · exact panel19Prefix53_eq
  · exact panel19Prefix54_eq
  · exact panel19Prefix55_eq
  · exact panel19Prefix56_eq
  · exact panel19Prefix57_eq
  · exact panel19Prefix58_eq
  · exact panel19Prefix59_eq
  · exact panel19Prefix60_eq
  · exact panel19Prefix61_eq
  · exact panel19Prefix62_eq
  · exact panel19Prefix63_eq

theorem panel19DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel19DefectPieces.EnclosesCanonical
      ⟨19, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel19DefectPieces,
      Vector.get_ofFn]
    rw [panel19PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨19, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel19DefectPieces]
    rw [panel19Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨19, by decide⟩

theorem panel19Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel19Cache.EnclosesCanonical
      ⟨19, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel19DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
