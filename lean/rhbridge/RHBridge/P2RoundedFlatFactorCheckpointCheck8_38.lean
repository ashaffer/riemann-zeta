import RHBridge.P2RoundedFlatFactorCheckpointData8

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FlatComponentChunk38 :
    P2RoundedFactorCheckpointData.panel8FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel8FlatOdd14_eq :
    P2RoundedFactorCheckpointData.panel8FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨14, by decide⟩ := by
  exact panel8FlatComponentChunk38

end RHP2Bridge
