import RHBridge.P2RoundedFlatFactorCheckpointData28

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel28FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel28FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel28FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel28FlatComponentChunk25

end RHP2Bridge
