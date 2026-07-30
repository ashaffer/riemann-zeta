import RHBridge.P2RoundedFlatFactorCheckpointData8

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FlatComponentChunk45 :
    P2RoundedFactorCheckpointData.panel8FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel8FlatOdd21_eq :
    P2RoundedFactorCheckpointData.panel8FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨21, by decide⟩ := by
  exact panel8FlatComponentChunk45

end RHP2Bridge
