import RHBridge.P2RoundedFlatFactorCheckpointData0

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FlatComponentChunk11 :
    P2RoundedFactorCheckpointData.panel0FlatEven11 =
      (P2RoundedFactorCheckpointData.panel0TruncatedEvenComponents).get ⟨11, by decide⟩ := by
  decide +kernel

theorem panel0FlatEven11_eq :
    P2RoundedFactorCheckpointData.panel0FlatEven11 =
      (P2RoundedFactorCheckpointData.panel0TruncatedEvenComponents).get ⟨11, by decide⟩ := by
  exact panel0FlatComponentChunk11

end RHP2Bridge
