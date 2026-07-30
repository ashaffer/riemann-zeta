import RHBridge.P2RoundedFlatFactorCheckpointData8

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel8FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel8FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel8FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel8FlatComponentChunk34

end RHP2Bridge
