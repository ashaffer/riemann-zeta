import RHBridge.P2RoundedFlatFactorCheckpointData8

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FlatComponentChunk39 :
    P2RoundedFactorCheckpointData.panel8FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨15, by decide⟩ := by
  decide +kernel

theorem panel8FlatOdd15_eq :
    P2RoundedFactorCheckpointData.panel8FlatOdd15 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨15, by decide⟩ := by
  exact panel8FlatComponentChunk39

end RHP2Bridge
