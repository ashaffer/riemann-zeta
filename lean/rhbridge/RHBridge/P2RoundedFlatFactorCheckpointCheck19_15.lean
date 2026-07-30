import RHBridge.P2RoundedFlatFactorCheckpointData19

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FlatComponentChunk15 :
    P2RoundedFactorCheckpointData.panel19FlatEven15 =
      (P2RoundedFactorCheckpointData.panel19TruncatedEvenComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel19FlatEven15_eq :
    P2RoundedFactorCheckpointData.panel19FlatEven15 =
      (P2RoundedFactorCheckpointData.panel19TruncatedEvenComponents).get ⟨15, by decide⟩ := by
  exact panel19FlatComponentChunk15

end RHP2Bridge
