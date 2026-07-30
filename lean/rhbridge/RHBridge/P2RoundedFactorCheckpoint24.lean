import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck24_0
import RHBridge.P2RoundedFactorCheckpointCheck24_1
import RHBridge.P2RoundedFactorCheckpointCheck24_2
import RHBridge.P2RoundedFactorCheckpointCheck24_3
import RHBridge.P2RoundedFactorCheckpointCheck24_4
import RHBridge.P2RoundedFactorCheckpointCheck24_5
import RHBridge.P2RoundedFactorCheckpointCheck24_6
import RHBridge.P2RoundedFactorCheckpointCheck24_7
import RHBridge.P2RoundedFactorCheckpointCheck24_8
import RHBridge.P2RoundedFactorCheckpointCheck24_9
import RHBridge.P2RoundedFactorCheckpointCheck24_10
import RHBridge.P2RoundedFactorCheckpointCheck24_11
import RHBridge.P2RoundedFactorCheckpointCheck24_12
import RHBridge.P2RoundedFactorCheckpointCheck24_13
import RHBridge.P2RoundedFactorCheckpointCheck24_14
import RHBridge.P2RoundedFactorCheckpointCheck24_15
import RHBridge.P2RoundedFactorCheckpointCheck24_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel24PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel24PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨24, by decide⟩ := by
  fin_cases i
  · exact panel24Prefix0_eq
  · exact panel24Prefix1_eq
  · exact panel24Prefix2_eq
  · exact panel24Prefix3_eq
  · exact panel24Prefix4_eq
  · exact panel24Prefix5_eq
  · exact panel24Prefix6_eq
  · exact panel24Prefix7_eq
  · exact panel24Prefix8_eq
  · exact panel24Prefix9_eq
  · exact panel24Prefix10_eq
  · exact panel24Prefix11_eq
  · exact panel24Prefix12_eq
  · exact panel24Prefix13_eq
  · exact panel24Prefix14_eq
  · exact panel24Prefix15_eq
  · exact panel24Prefix16_eq
  · exact panel24Prefix17_eq
  · exact panel24Prefix18_eq
  · exact panel24Prefix19_eq
  · exact panel24Prefix20_eq
  · exact panel24Prefix21_eq
  · exact panel24Prefix22_eq
  · exact panel24Prefix23_eq
  · exact panel24Prefix24_eq
  · exact panel24Prefix25_eq
  · exact panel24Prefix26_eq
  · exact panel24Prefix27_eq
  · exact panel24Prefix28_eq
  · exact panel24Prefix29_eq
  · exact panel24Prefix30_eq
  · exact panel24Prefix31_eq
  · exact panel24Prefix32_eq
  · exact panel24Prefix33_eq
  · exact panel24Prefix34_eq
  · exact panel24Prefix35_eq
  · exact panel24Prefix36_eq
  · exact panel24Prefix37_eq
  · exact panel24Prefix38_eq
  · exact panel24Prefix39_eq
  · exact panel24Prefix40_eq
  · exact panel24Prefix41_eq
  · exact panel24Prefix42_eq
  · exact panel24Prefix43_eq
  · exact panel24Prefix44_eq
  · exact panel24Prefix45_eq
  · exact panel24Prefix46_eq
  · exact panel24Prefix47_eq
  · exact panel24Prefix48_eq
  · exact panel24Prefix49_eq
  · exact panel24Prefix50_eq
  · exact panel24Prefix51_eq
  · exact panel24Prefix52_eq
  · exact panel24Prefix53_eq
  · exact panel24Prefix54_eq
  · exact panel24Prefix55_eq
  · exact panel24Prefix56_eq
  · exact panel24Prefix57_eq
  · exact panel24Prefix58_eq
  · exact panel24Prefix59_eq
  · exact panel24Prefix60_eq
  · exact panel24Prefix61_eq
  · exact panel24Prefix62_eq
  · exact panel24Prefix63_eq

theorem panel24DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel24DefectPieces.EnclosesCanonical
      ⟨24, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel24DefectPieces,
      Vector.get_ofFn]
    rw [panel24PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨24, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel24DefectPieces]
    rw [panel24Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨24, by decide⟩

theorem panel24Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel24Cache.EnclosesCanonical
      ⟨24, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel24DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
