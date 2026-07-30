import RHBridge.P2RoundedFlatFactorCheckpointData20

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel20FlatComponentChunk11 :
    P2RoundedFactorCheckpointData.panel20FlatEven11 =
      (P2RoundedFactorCheckpointData.panel20TruncatedEvenComponents).get ⟨11, by decide⟩ := by
  decide +kernel

theorem panel20FlatEven11_eq :
    P2RoundedFactorCheckpointData.panel20FlatEven11 =
      (P2RoundedFactorCheckpointData.panel20TruncatedEvenComponents).get ⟨11, by decide⟩ := by
  exact panel20FlatComponentChunk11

end RHP2Bridge
