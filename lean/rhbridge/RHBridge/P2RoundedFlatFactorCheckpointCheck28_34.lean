import RHBridge.P2RoundedFlatFactorCheckpointData28

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel28FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel28FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel28FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel28FlatComponentChunk34

end RHP2Bridge
