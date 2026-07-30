import RHBridge.P2RoundedFlatFactorCheckpointData5

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FlatComponentChunk0 :
    P2RoundedFactorCheckpointData.panel5FlatEven0 =
      (P2RoundedFactorCheckpointData.panel5TruncatedEvenComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel5FlatEven0_eq :
    P2RoundedFactorCheckpointData.panel5FlatEven0 =
      (P2RoundedFactorCheckpointData.panel5TruncatedEvenComponents).get ⟨0, by decide⟩ := by
  exact panel5FlatComponentChunk0

end RHP2Bridge
