import RHBridge.P2RoundedFlatFactorCheckpointData28

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FlatComponentChunk39 :
    P2RoundedFactorCheckpointData.panel28FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel28FlatOdd15_eq :
    P2RoundedFactorCheckpointData.panel28FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨15, by decide⟩ := by
  exact panel28FlatComponentChunk39

end RHP2Bridge
