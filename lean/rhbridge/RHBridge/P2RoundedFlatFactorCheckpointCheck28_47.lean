import RHBridge.P2RoundedFlatFactorCheckpointData28

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FlatComponentChunk47 :
    P2RoundedFactorCheckpointData.panel28FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel28FlatOdd23_eq :
    P2RoundedFactorCheckpointData.panel28FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨23, by decide⟩ := by
  exact panel28FlatComponentChunk47

end RHP2Bridge
