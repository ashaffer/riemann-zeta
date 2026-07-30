import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck16_0
import RHBridge.P2RoundedFactorCheckpointCheck16_1
import RHBridge.P2RoundedFactorCheckpointCheck16_2
import RHBridge.P2RoundedFactorCheckpointCheck16_3
import RHBridge.P2RoundedFactorCheckpointCheck16_4
import RHBridge.P2RoundedFactorCheckpointCheck16_5
import RHBridge.P2RoundedFactorCheckpointCheck16_6
import RHBridge.P2RoundedFactorCheckpointCheck16_7
import RHBridge.P2RoundedFactorCheckpointCheck16_8
import RHBridge.P2RoundedFactorCheckpointCheck16_9
import RHBridge.P2RoundedFactorCheckpointCheck16_10
import RHBridge.P2RoundedFactorCheckpointCheck16_11
import RHBridge.P2RoundedFactorCheckpointCheck16_12
import RHBridge.P2RoundedFactorCheckpointCheck16_13
import RHBridge.P2RoundedFactorCheckpointCheck16_14
import RHBridge.P2RoundedFactorCheckpointCheck16_15
import RHBridge.P2RoundedFactorCheckpointCheck16_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel16PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel16PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨16, by decide⟩ := by
  fin_cases i
  · exact panel16Prefix0_eq
  · exact panel16Prefix1_eq
  · exact panel16Prefix2_eq
  · exact panel16Prefix3_eq
  · exact panel16Prefix4_eq
  · exact panel16Prefix5_eq
  · exact panel16Prefix6_eq
  · exact panel16Prefix7_eq
  · exact panel16Prefix8_eq
  · exact panel16Prefix9_eq
  · exact panel16Prefix10_eq
  · exact panel16Prefix11_eq
  · exact panel16Prefix12_eq
  · exact panel16Prefix13_eq
  · exact panel16Prefix14_eq
  · exact panel16Prefix15_eq
  · exact panel16Prefix16_eq
  · exact panel16Prefix17_eq
  · exact panel16Prefix18_eq
  · exact panel16Prefix19_eq
  · exact panel16Prefix20_eq
  · exact panel16Prefix21_eq
  · exact panel16Prefix22_eq
  · exact panel16Prefix23_eq
  · exact panel16Prefix24_eq
  · exact panel16Prefix25_eq
  · exact panel16Prefix26_eq
  · exact panel16Prefix27_eq
  · exact panel16Prefix28_eq
  · exact panel16Prefix29_eq
  · exact panel16Prefix30_eq
  · exact panel16Prefix31_eq
  · exact panel16Prefix32_eq
  · exact panel16Prefix33_eq
  · exact panel16Prefix34_eq
  · exact panel16Prefix35_eq
  · exact panel16Prefix36_eq
  · exact panel16Prefix37_eq
  · exact panel16Prefix38_eq
  · exact panel16Prefix39_eq
  · exact panel16Prefix40_eq
  · exact panel16Prefix41_eq
  · exact panel16Prefix42_eq
  · exact panel16Prefix43_eq
  · exact panel16Prefix44_eq
  · exact panel16Prefix45_eq
  · exact panel16Prefix46_eq
  · exact panel16Prefix47_eq
  · exact panel16Prefix48_eq
  · exact panel16Prefix49_eq
  · exact panel16Prefix50_eq
  · exact panel16Prefix51_eq
  · exact panel16Prefix52_eq
  · exact panel16Prefix53_eq
  · exact panel16Prefix54_eq
  · exact panel16Prefix55_eq
  · exact panel16Prefix56_eq
  · exact panel16Prefix57_eq
  · exact panel16Prefix58_eq
  · exact panel16Prefix59_eq
  · exact panel16Prefix60_eq
  · exact panel16Prefix61_eq
  · exact panel16Prefix62_eq
  · exact panel16Prefix63_eq

theorem panel16DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel16DefectPieces.EnclosesCanonical
      ⟨16, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel16DefectPieces,
      Vector.get_ofFn]
    rw [panel16PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨16, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel16DefectPieces]
    rw [panel16Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨16, by decide⟩

theorem panel16Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel16Cache.EnclosesCanonical
      ⟨16, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel16DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
