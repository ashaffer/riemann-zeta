import RHBridge.P2RoundedFlatFactorCheckpointData28

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FlatComponentChunk38 :
    P2RoundedFactorCheckpointData.panel28FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel28FlatOdd14_eq :
    P2RoundedFactorCheckpointData.panel28FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨14, by decide⟩ := by
  exact panel28FlatComponentChunk38

end RHP2Bridge
