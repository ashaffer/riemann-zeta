import RHBridge.P2RoundedFlatFactorCheckpointData5

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FlatComponentChunk4 :
    P2RoundedFactorCheckpointData.panel5FlatEven4 =
      (P2RoundedFactorCheckpointData.panel5TruncatedEvenComponents).get ⟨4, by decide⟩ := by
  decide +kernel

theorem panel5FlatEven4_eq :
    P2RoundedFactorCheckpointData.panel5FlatEven4 =
      (P2RoundedFactorCheckpointData.panel5TruncatedEvenComponents).get ⟨4, by decide⟩ := by
  exact panel5FlatComponentChunk4

end RHP2Bridge
