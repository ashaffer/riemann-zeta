import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck14_0
import RHBridge.P2RoundedFactorCheckpointCheck14_1
import RHBridge.P2RoundedFactorCheckpointCheck14_2
import RHBridge.P2RoundedFactorCheckpointCheck14_3
import RHBridge.P2RoundedFactorCheckpointCheck14_4
import RHBridge.P2RoundedFactorCheckpointCheck14_5
import RHBridge.P2RoundedFactorCheckpointCheck14_6
import RHBridge.P2RoundedFactorCheckpointCheck14_7
import RHBridge.P2RoundedFactorCheckpointCheck14_8
import RHBridge.P2RoundedFactorCheckpointCheck14_9
import RHBridge.P2RoundedFactorCheckpointCheck14_10
import RHBridge.P2RoundedFactorCheckpointCheck14_11
import RHBridge.P2RoundedFactorCheckpointCheck14_12
import RHBridge.P2RoundedFactorCheckpointCheck14_13
import RHBridge.P2RoundedFactorCheckpointCheck14_14
import RHBridge.P2RoundedFactorCheckpointCheck14_15
import RHBridge.P2RoundedFactorCheckpointCheck14_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel14PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨14, by decide⟩ := by
  fin_cases i
  · exact panel14Prefix0_eq
  · exact panel14Prefix1_eq
  · exact panel14Prefix2_eq
  · exact panel14Prefix3_eq
  · exact panel14Prefix4_eq
  · exact panel14Prefix5_eq
  · exact panel14Prefix6_eq
  · exact panel14Prefix7_eq
  · exact panel14Prefix8_eq
  · exact panel14Prefix9_eq
  · exact panel14Prefix10_eq
  · exact panel14Prefix11_eq
  · exact panel14Prefix12_eq
  · exact panel14Prefix13_eq
  · exact panel14Prefix14_eq
  · exact panel14Prefix15_eq
  · exact panel14Prefix16_eq
  · exact panel14Prefix17_eq
  · exact panel14Prefix18_eq
  · exact panel14Prefix19_eq
  · exact panel14Prefix20_eq
  · exact panel14Prefix21_eq
  · exact panel14Prefix22_eq
  · exact panel14Prefix23_eq
  · exact panel14Prefix24_eq
  · exact panel14Prefix25_eq
  · exact panel14Prefix26_eq
  · exact panel14Prefix27_eq
  · exact panel14Prefix28_eq
  · exact panel14Prefix29_eq
  · exact panel14Prefix30_eq
  · exact panel14Prefix31_eq
  · exact panel14Prefix32_eq
  · exact panel14Prefix33_eq
  · exact panel14Prefix34_eq
  · exact panel14Prefix35_eq
  · exact panel14Prefix36_eq
  · exact panel14Prefix37_eq
  · exact panel14Prefix38_eq
  · exact panel14Prefix39_eq
  · exact panel14Prefix40_eq
  · exact panel14Prefix41_eq
  · exact panel14Prefix42_eq
  · exact panel14Prefix43_eq
  · exact panel14Prefix44_eq
  · exact panel14Prefix45_eq
  · exact panel14Prefix46_eq
  · exact panel14Prefix47_eq
  · exact panel14Prefix48_eq
  · exact panel14Prefix49_eq
  · exact panel14Prefix50_eq
  · exact panel14Prefix51_eq
  · exact panel14Prefix52_eq
  · exact panel14Prefix53_eq
  · exact panel14Prefix54_eq
  · exact panel14Prefix55_eq
  · exact panel14Prefix56_eq
  · exact panel14Prefix57_eq
  · exact panel14Prefix58_eq
  · exact panel14Prefix59_eq
  · exact panel14Prefix60_eq
  · exact panel14Prefix61_eq
  · exact panel14Prefix62_eq
  · exact panel14Prefix63_eq

theorem panel14DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel14DefectPieces.EnclosesCanonical
      ⟨14, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel14DefectPieces,
      Vector.get_ofFn]
    rw [panel14PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨14, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel14DefectPieces]
    rw [panel14Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨14, by decide⟩

theorem panel14Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel14Cache.EnclosesCanonical
      ⟨14, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel14DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
