import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck27_0
import RHBridge.P2RoundedFactorCheckpointCheck27_1
import RHBridge.P2RoundedFactorCheckpointCheck27_2
import RHBridge.P2RoundedFactorCheckpointCheck27_3
import RHBridge.P2RoundedFactorCheckpointCheck27_4
import RHBridge.P2RoundedFactorCheckpointCheck27_5
import RHBridge.P2RoundedFactorCheckpointCheck27_6
import RHBridge.P2RoundedFactorCheckpointCheck27_7
import RHBridge.P2RoundedFactorCheckpointCheck27_8
import RHBridge.P2RoundedFactorCheckpointCheck27_9
import RHBridge.P2RoundedFactorCheckpointCheck27_10
import RHBridge.P2RoundedFactorCheckpointCheck27_11
import RHBridge.P2RoundedFactorCheckpointCheck27_12
import RHBridge.P2RoundedFactorCheckpointCheck27_13
import RHBridge.P2RoundedFactorCheckpointCheck27_14
import RHBridge.P2RoundedFactorCheckpointCheck27_15
import RHBridge.P2RoundedFactorCheckpointCheck27_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel27PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel27PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨27, by decide⟩ := by
  fin_cases i
  · exact panel27Prefix0_eq
  · exact panel27Prefix1_eq
  · exact panel27Prefix2_eq
  · exact panel27Prefix3_eq
  · exact panel27Prefix4_eq
  · exact panel27Prefix5_eq
  · exact panel27Prefix6_eq
  · exact panel27Prefix7_eq
  · exact panel27Prefix8_eq
  · exact panel27Prefix9_eq
  · exact panel27Prefix10_eq
  · exact panel27Prefix11_eq
  · exact panel27Prefix12_eq
  · exact panel27Prefix13_eq
  · exact panel27Prefix14_eq
  · exact panel27Prefix15_eq
  · exact panel27Prefix16_eq
  · exact panel27Prefix17_eq
  · exact panel27Prefix18_eq
  · exact panel27Prefix19_eq
  · exact panel27Prefix20_eq
  · exact panel27Prefix21_eq
  · exact panel27Prefix22_eq
  · exact panel27Prefix23_eq
  · exact panel27Prefix24_eq
  · exact panel27Prefix25_eq
  · exact panel27Prefix26_eq
  · exact panel27Prefix27_eq
  · exact panel27Prefix28_eq
  · exact panel27Prefix29_eq
  · exact panel27Prefix30_eq
  · exact panel27Prefix31_eq
  · exact panel27Prefix32_eq
  · exact panel27Prefix33_eq
  · exact panel27Prefix34_eq
  · exact panel27Prefix35_eq
  · exact panel27Prefix36_eq
  · exact panel27Prefix37_eq
  · exact panel27Prefix38_eq
  · exact panel27Prefix39_eq
  · exact panel27Prefix40_eq
  · exact panel27Prefix41_eq
  · exact panel27Prefix42_eq
  · exact panel27Prefix43_eq
  · exact panel27Prefix44_eq
  · exact panel27Prefix45_eq
  · exact panel27Prefix46_eq
  · exact panel27Prefix47_eq
  · exact panel27Prefix48_eq
  · exact panel27Prefix49_eq
  · exact panel27Prefix50_eq
  · exact panel27Prefix51_eq
  · exact panel27Prefix52_eq
  · exact panel27Prefix53_eq
  · exact panel27Prefix54_eq
  · exact panel27Prefix55_eq
  · exact panel27Prefix56_eq
  · exact panel27Prefix57_eq
  · exact panel27Prefix58_eq
  · exact panel27Prefix59_eq
  · exact panel27Prefix60_eq
  · exact panel27Prefix61_eq
  · exact panel27Prefix62_eq
  · exact panel27Prefix63_eq

theorem panel27DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel27DefectPieces.EnclosesCanonical
      ⟨27, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel27DefectPieces,
      Vector.get_ofFn]
    rw [panel27PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨27, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel27DefectPieces]
    rw [panel27Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨27, by decide⟩

theorem panel27Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel27Cache.EnclosesCanonical
      ⟨27, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel27DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
