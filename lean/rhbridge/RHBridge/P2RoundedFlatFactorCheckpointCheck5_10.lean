import RHBridge.P2RoundedFlatFactorCheckpointData5

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FlatComponentChunk10 :
    P2RoundedFactorCheckpointData.panel5FlatEven10 =
      (P2RoundedFactorCheckpointData.panel5TruncatedEvenComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel5FlatEven10_eq :
    P2RoundedFactorCheckpointData.panel5FlatEven10 =
      (P2RoundedFactorCheckpointData.panel5TruncatedEvenComponents).get ⟨10, by decide⟩ := by
  exact panel5FlatComponentChunk10

end RHP2Bridge
