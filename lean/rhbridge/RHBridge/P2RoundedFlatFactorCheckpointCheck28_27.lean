import RHBridge.P2RoundedFlatFactorCheckpointData28

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FlatComponentChunk27 :
    P2RoundedFactorCheckpointData.panel28FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨3, by decide⟩ := by
  decide +kernel

theorem panel28FlatOdd3_eq :
    P2RoundedFactorCheckpointData.panel28FlatOdd3 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨3, by decide⟩ := by
  exact panel28FlatComponentChunk27

end RHP2Bridge
