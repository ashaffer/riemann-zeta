import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck11_0
import RHBridge.P2RoundedFactorCheckpointCheck11_1
import RHBridge.P2RoundedFactorCheckpointCheck11_2
import RHBridge.P2RoundedFactorCheckpointCheck11_3
import RHBridge.P2RoundedFactorCheckpointCheck11_4
import RHBridge.P2RoundedFactorCheckpointCheck11_5
import RHBridge.P2RoundedFactorCheckpointCheck11_6
import RHBridge.P2RoundedFactorCheckpointCheck11_7
import RHBridge.P2RoundedFactorCheckpointCheck11_8
import RHBridge.P2RoundedFactorCheckpointCheck11_9
import RHBridge.P2RoundedFactorCheckpointCheck11_10
import RHBridge.P2RoundedFactorCheckpointCheck11_11
import RHBridge.P2RoundedFactorCheckpointCheck11_12
import RHBridge.P2RoundedFactorCheckpointCheck11_13
import RHBridge.P2RoundedFactorCheckpointCheck11_14
import RHBridge.P2RoundedFactorCheckpointCheck11_15
import RHBridge.P2RoundedFactorCheckpointCheck11_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel11PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel11PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨11, by decide⟩ := by
  fin_cases i
  · exact panel11Prefix0_eq
  · exact panel11Prefix1_eq
  · exact panel11Prefix2_eq
  · exact panel11Prefix3_eq
  · exact panel11Prefix4_eq
  · exact panel11Prefix5_eq
  · exact panel11Prefix6_eq
  · exact panel11Prefix7_eq
  · exact panel11Prefix8_eq
  · exact panel11Prefix9_eq
  · exact panel11Prefix10_eq
  · exact panel11Prefix11_eq
  · exact panel11Prefix12_eq
  · exact panel11Prefix13_eq
  · exact panel11Prefix14_eq
  · exact panel11Prefix15_eq
  · exact panel11Prefix16_eq
  · exact panel11Prefix17_eq
  · exact panel11Prefix18_eq
  · exact panel11Prefix19_eq
  · exact panel11Prefix20_eq
  · exact panel11Prefix21_eq
  · exact panel11Prefix22_eq
  · exact panel11Prefix23_eq
  · exact panel11Prefix24_eq
  · exact panel11Prefix25_eq
  · exact panel11Prefix26_eq
  · exact panel11Prefix27_eq
  · exact panel11Prefix28_eq
  · exact panel11Prefix29_eq
  · exact panel11Prefix30_eq
  · exact panel11Prefix31_eq
  · exact panel11Prefix32_eq
  · exact panel11Prefix33_eq
  · exact panel11Prefix34_eq
  · exact panel11Prefix35_eq
  · exact panel11Prefix36_eq
  · exact panel11Prefix37_eq
  · exact panel11Prefix38_eq
  · exact panel11Prefix39_eq
  · exact panel11Prefix40_eq
  · exact panel11Prefix41_eq
  · exact panel11Prefix42_eq
  · exact panel11Prefix43_eq
  · exact panel11Prefix44_eq
  · exact panel11Prefix45_eq
  · exact panel11Prefix46_eq
  · exact panel11Prefix47_eq
  · exact panel11Prefix48_eq
  · exact panel11Prefix49_eq
  · exact panel11Prefix50_eq
  · exact panel11Prefix51_eq
  · exact panel11Prefix52_eq
  · exact panel11Prefix53_eq
  · exact panel11Prefix54_eq
  · exact panel11Prefix55_eq
  · exact panel11Prefix56_eq
  · exact panel11Prefix57_eq
  · exact panel11Prefix58_eq
  · exact panel11Prefix59_eq
  · exact panel11Prefix60_eq
  · exact panel11Prefix61_eq
  · exact panel11Prefix62_eq
  · exact panel11Prefix63_eq

theorem panel11DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel11DefectPieces.EnclosesCanonical
      ⟨11, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel11DefectPieces,
      Vector.get_ofFn]
    rw [panel11PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨11, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel11DefectPieces]
    rw [panel11Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨11, by decide⟩

theorem panel11Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel11Cache.EnclosesCanonical
      ⟨11, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel11DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
