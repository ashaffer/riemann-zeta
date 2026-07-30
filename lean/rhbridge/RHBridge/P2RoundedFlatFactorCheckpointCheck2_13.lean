import RHBridge.P2RoundedFlatFactorCheckpointData2

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FlatComponentChunk13 :
    P2RoundedFactorCheckpointData.panel2FlatEven13 =
      (P2RoundedFactorCheckpointData.panel2TruncatedEvenComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel2FlatEven13_eq :
    P2RoundedFactorCheckpointData.panel2FlatEven13 =
      (P2RoundedFactorCheckpointData.panel2TruncatedEvenComponents).get ⟨13, by decide⟩ := by
  exact panel2FlatComponentChunk13

end RHP2Bridge
