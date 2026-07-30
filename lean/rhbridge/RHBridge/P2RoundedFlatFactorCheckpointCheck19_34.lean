import RHBridge.P2RoundedFlatFactorCheckpointData19

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel19FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel19FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel19FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel19FlatComponentChunk34

end RHP2Bridge
