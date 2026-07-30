import RHBridge.P2RoundedFlatFactorCheckpointData8

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FlatComponentChunk42 :
    P2RoundedFactorCheckpointData.panel8FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨18, by decide⟩ := by
  decide +kernel

theorem panel8FlatOdd18_eq :
    P2RoundedFactorCheckpointData.panel8FlatOdd18 =
      (P2RoundedFactorCheckpointData.panel8TruncatedOddComponents).get ⟨18, by decide⟩ := by
  exact panel8FlatComponentChunk42

end RHP2Bridge
