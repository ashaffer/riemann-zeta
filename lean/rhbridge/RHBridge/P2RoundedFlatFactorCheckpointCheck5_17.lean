import RHBridge.P2RoundedFlatFactorCheckpointData5

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FlatComponentChunk17 :
    P2RoundedFactorCheckpointData.panel5FlatEven17 =
      (P2RoundedFactorCheckpointData.panel5TruncatedEvenComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel5FlatEven17_eq :
    P2RoundedFactorCheckpointData.panel5FlatEven17 =
      (P2RoundedFactorCheckpointData.panel5TruncatedEvenComponents).get ⟨17, by decide⟩ := by
  exact panel5FlatComponentChunk17

end RHP2Bridge
