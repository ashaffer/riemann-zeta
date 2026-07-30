import RHBridge.P2RoundedSphericalOuter
import RHBridge.P2RoundedFactorCheckpointCheck30_0
import RHBridge.P2RoundedFactorCheckpointCheck30_1
import RHBridge.P2RoundedFactorCheckpointCheck30_2
import RHBridge.P2RoundedFactorCheckpointCheck30_3
import RHBridge.P2RoundedFactorCheckpointCheck30_4
import RHBridge.P2RoundedFactorCheckpointCheck30_5
import RHBridge.P2RoundedFactorCheckpointCheck30_6
import RHBridge.P2RoundedFactorCheckpointCheck30_7
import RHBridge.P2RoundedFactorCheckpointCheck30_8
import RHBridge.P2RoundedFactorCheckpointCheck30_9
import RHBridge.P2RoundedFactorCheckpointCheck30_10
import RHBridge.P2RoundedFactorCheckpointCheck30_11
import RHBridge.P2RoundedFactorCheckpointCheck30_12
import RHBridge.P2RoundedFactorCheckpointCheck30_13
import RHBridge.P2RoundedFactorCheckpointCheck30_14
import RHBridge.P2RoundedFactorCheckpointCheck30_15
import RHBridge.P2RoundedFactorCheckpointCheck30_16

namespace RHP2Bridge

open P2RoundedCanonical P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel30PrefixTerm_eq_computed (i : Fin 64) :
    P2RoundedFactorCheckpointData.panel30PrefixTerm i =
      normalizedPrefixTermAtomApprox i ⟨30, by decide⟩ := by
  fin_cases i
  · exact panel30Prefix0_eq
  · exact panel30Prefix1_eq
  · exact panel30Prefix2_eq
  · exact panel30Prefix3_eq
  · exact panel30Prefix4_eq
  · exact panel30Prefix5_eq
  · exact panel30Prefix6_eq
  · exact panel30Prefix7_eq
  · exact panel30Prefix8_eq
  · exact panel30Prefix9_eq
  · exact panel30Prefix10_eq
  · exact panel30Prefix11_eq
  · exact panel30Prefix12_eq
  · exact panel30Prefix13_eq
  · exact panel30Prefix14_eq
  · exact panel30Prefix15_eq
  · exact panel30Prefix16_eq
  · exact panel30Prefix17_eq
  · exact panel30Prefix18_eq
  · exact panel30Prefix19_eq
  · exact panel30Prefix20_eq
  · exact panel30Prefix21_eq
  · exact panel30Prefix22_eq
  · exact panel30Prefix23_eq
  · exact panel30Prefix24_eq
  · exact panel30Prefix25_eq
  · exact panel30Prefix26_eq
  · exact panel30Prefix27_eq
  · exact panel30Prefix28_eq
  · exact panel30Prefix29_eq
  · exact panel30Prefix30_eq
  · exact panel30Prefix31_eq
  · exact panel30Prefix32_eq
  · exact panel30Prefix33_eq
  · exact panel30Prefix34_eq
  · exact panel30Prefix35_eq
  · exact panel30Prefix36_eq
  · exact panel30Prefix37_eq
  · exact panel30Prefix38_eq
  · exact panel30Prefix39_eq
  · exact panel30Prefix40_eq
  · exact panel30Prefix41_eq
  · exact panel30Prefix42_eq
  · exact panel30Prefix43_eq
  · exact panel30Prefix44_eq
  · exact panel30Prefix45_eq
  · exact panel30Prefix46_eq
  · exact panel30Prefix47_eq
  · exact panel30Prefix48_eq
  · exact panel30Prefix49_eq
  · exact panel30Prefix50_eq
  · exact panel30Prefix51_eq
  · exact panel30Prefix52_eq
  · exact panel30Prefix53_eq
  · exact panel30Prefix54_eq
  · exact panel30Prefix55_eq
  · exact panel30Prefix56_eq
  · exact panel30Prefix57_eq
  · exact panel30Prefix58_eq
  · exact panel30Prefix59_eq
  · exact panel30Prefix60_eq
  · exact panel30Prefix61_eq
  · exact panel30Prefix62_eq
  · exact panel30Prefix63_eq

theorem panel30DefectPieces_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel30DefectPieces.EnclosesCanonical
      ⟨30, by decide⟩ := by
  constructor
  · intro i
    simp only [P2RoundedFactorCheckpointData.panel30DefectPieces,
      Vector.get_ofFn]
    rw [panel30PrefixTerm_eq_computed i]
    exact normalizedPrefixTermAtomApprox_encloses i ⟨30, by decide⟩
  · simp only [P2RoundedFactorCheckpointData.panel30DefectPieces]
    rw [panel30Nonprefix_eq]
    exact normalizedNonprefixAtomApprox_encloses ⟨30, by decide⟩

theorem panel30Cache_enclosesCanonical :
    P2RoundedFactorCheckpointData.panel30Cache.EnclosesCanonical
      ⟨30, by decide⟩ := by
  apply panelCacheOfPieces_enclosesCanonical
      panel30DefectPieces_enclosesCanonical
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .even _ i
  · intro i
    exact componentVectorFromOuters_encloses
      generatedSphericalOuters_enclose .odd _ i

end RHP2Bridge
