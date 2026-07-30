import RHBridge.P2RoundedFlatFactorCheckpointData19

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FlatComponentChunk13 :
    P2RoundedFactorCheckpointData.panel19FlatEven13 =
      (P2RoundedFactorCheckpointData.panel19TruncatedEvenComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel19FlatEven13_eq :
    P2RoundedFactorCheckpointData.panel19FlatEven13 =
      (P2RoundedFactorCheckpointData.panel19TruncatedEvenComponents).get ⟨13, by decide⟩ := by
  exact panel19FlatComponentChunk13

end RHP2Bridge
