import RHBridge.P2RoundedFlatFactorCheckpointData5

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel5FlatComponentChunk3 :
    P2RoundedFactorCheckpointData.panel5FlatEven3 =
      (P2RoundedFactorCheckpointData.panel5TruncatedEvenComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel5FlatEven3_eq :
    P2RoundedFactorCheckpointData.panel5FlatEven3 =
      (P2RoundedFactorCheckpointData.panel5TruncatedEvenComponents).get ⟨3, by decide⟩ := by
  exact panel5FlatComponentChunk3

end RHP2Bridge
